#!/usr/bin/env bash
# Diff the generated Pulumi schema between two revisions and describe the change as
# markdown on stdout. Progress and warnings go to stderr.
#
# Usage: scripts/schema-diff.sh [<old-ref>] [<new-path-or-ref>]
#   scripts/schema-diff.sh                    # origin/main -> working tree
#   scripts/schema-diff.sh HEAD~1             # previous commit -> working tree
#   scripts/schema-diff.sh 8f50d6e^ 8f50d6e   # between two commits
#
# schema.json is committed, so this needs no build. It answers the question the
# upstream changelog cannot: what actually reached the generated SDKs.
#
# Requires: jq, git. Uses pulumi/schema-tools for breaking-change detection when the
# binary is on PATH.
set -euo pipefail

SCHEMA_PATH="provider/cmd/pulumi-resource-datarobot/schema.json"

OLD_REF="${1:-origin/main}"
NEW_REF="${2:-}"

log() { echo "$@" >&2; }

WORK_DIR="$(mktemp -d)"
trap 'rm -rf "$WORK_DIR"' EXIT
OLD_JSON="$WORK_DIR/old.json"
NEW_JSON="$WORK_DIR/new.json"

if ! git show "${OLD_REF}:${SCHEMA_PATH}" >"$OLD_JSON" 2>/dev/null; then
  log "WARN: no ${SCHEMA_PATH} at ${OLD_REF}; skipping schema diff"
  echo "### Pulumi SDK surface"
  echo
  echo "_Could not resolve a baseline schema at \`${OLD_REF}\`; diff skipped._"
  exit 0
fi

if [[ -z "$NEW_REF" ]]; then
  # Working tree.
  if [[ ! -f "$SCHEMA_PATH" ]]; then
    log "ERROR: $SCHEMA_PATH not found; run 'make tfgen' first"
    exit 1
  fi
  cp "$SCHEMA_PATH" "$NEW_JSON"
  NEW_LABEL="working tree"
elif [[ -f "$NEW_REF" ]]; then
  cp "$NEW_REF" "$NEW_JSON"
  NEW_LABEL="$NEW_REF"
else
  git show "${NEW_REF}:${SCHEMA_PATH}" >"$NEW_JSON"
  NEW_LABEL="$NEW_REF"
fi

log "Diffing Pulumi schema: ${OLD_REF} -> ${NEW_LABEL}"

echo "### Pulumi SDK surface"
echo
echo "_Diff of the generated \`schema.json\` — what actually reached the SDKs._"
echo

jq -n --slurpfile old "$OLD_JSON" --slurpfile new "$NEW_JSON" -r '
  def keyset(o): (o // {}) | keys;
  def bullets(xs): (xs | map("- `" + . + "`") | join("\n"));

  $old[0] as $o
  | $new[0] as $n
  | (keyset($n.resources) - keyset($o.resources)) as $newRes
  | (keyset($o.resources) - keyset($n.resources)) as $goneRes
  | (keyset($n.functions) - keyset($o.functions)) as $newFn
  | (keyset($o.functions) - keyset($n.functions)) as $goneFn
  | (keyset($n.types) - keyset($o.types)) as $newTypes
  | (keyset($o.types) - keyset($n.types)) as $goneTypes
  # Most bridged changes land on nested block types, not on the resource itself,
  # so a key-set diff of types alone would miss them.
  | [ (keyset($o.types) - $goneTypes)[]
      | . as $k
      | {
          token: $k,
          added:   (keyset($n.types[$k].properties) - keyset($o.types[$k].properties)),
          removed: (keyset($o.types[$k].properties) - keyset($n.types[$k].properties))
        }
      | select([.added, .removed] | map(length) | add > 0)
    ] as $changedTypes
  | [ (keyset($o.resources) - $goneRes)[]
      | . as $k
      | {
          token: $k,
          addedInputs:   (keyset($n.resources[$k].inputProperties) - keyset($o.resources[$k].inputProperties)),
          removedInputs: (keyset($o.resources[$k].inputProperties) - keyset($n.resources[$k].inputProperties)),
          addedOutputs:  (keyset($n.resources[$k].properties)      - keyset($o.resources[$k].properties)),
          removedOutputs:(keyset($o.resources[$k].properties)      - keyset($n.resources[$k].properties))
        }
      | select([.addedInputs, .removedInputs, .addedOutputs, .removedOutputs] | map(length) | add > 0)
    ] as $changed
  | (($newRes | length) + ($goneRes | length) + ($newFn | length) + ($goneFn | length)
     + ($changed | length) + ($newTypes | length) + ($goneTypes | length)
     + ($changedTypes | length)) as $total
  | if $total == 0 then
      "No change to the Pulumi schema surface."
    else
      [
        (if ($newRes | length) > 0 then
          "**New resources (\($newRes | length))**\n\n" + bullets($newRes) else empty end),
        (if ($goneRes | length) > 0 then
          "**⚠️ Removed resources (\($goneRes | length))**\n\n" + bullets($goneRes) else empty end),
        (if ($newFn | length) > 0 then
          "**New functions (\($newFn | length))**\n\n" + bullets($newFn) else empty end),
        (if ($goneFn | length) > 0 then
          "**⚠️ Removed functions (\($goneFn | length))**\n\n" + bullets($goneFn) else empty end),
        (if ($changed | length) > 0 then
          "**Changed resources (\($changed | length))**\n\n" +
          ($changed | map(
            "- `" + .token + "`" +
            (if (.addedInputs | length) > 0    then "\n  - new inputs: "     + (.addedInputs   | map("`"+.+"`") | join(", ")) else "" end) +
            (if (.removedInputs | length) > 0  then "\n  - ⚠️ removed inputs: " + (.removedInputs | map("`"+.+"`") | join(", ")) else "" end) +
            (if (.addedOutputs | length) > 0   then "\n  - new outputs: "    + (.addedOutputs  | map("`"+.+"`") | join(", ")) else "" end) +
            (if (.removedOutputs | length) > 0 then "\n  - ⚠️ removed outputs: " + (.removedOutputs| map("`"+.+"`") | join(", ")) else "" end)
          ) | join("\n"))
        else empty end),
        (if (($newTypes | length) + ($goneTypes | length) + ($changedTypes | length)) > 0 then
          "<details><summary>Nested types: " +
          "\($newTypes | length) added, \($goneTypes | length) removed, " +
          "\($changedTypes | length) changed</summary>\n\n" +
          (if ($newTypes | length) > 0 then "Added:\n\n" + bullets($newTypes) + "\n\n" else "" end) +
          (if ($goneTypes | length) > 0 then "⚠️ Removed:\n\n" + bullets($goneTypes) + "\n\n" else "" end) +
          (if ($changedTypes | length) > 0 then "Changed:\n\n" +
            ($changedTypes | map(
              "- `" + .token + "`" +
              (if (.added | length) > 0   then "\n  - new: "        + (.added   | map("`"+.+"`") | join(", ")) else "" end) +
              (if (.removed | length) > 0 then "\n  - ⚠️ removed: " + (.removed | map("`"+.+"`") | join(", ")) else "" end)
            ) | join("\n")) + "\n\n"
          else "" end) +
          "</details>"
        else empty end)
      ] | join("\n\n")
    end
'

# schema-tools knows the bridge's breaking-change rules; use it when available.
if command -v schema-tools >/dev/null 2>&1; then
  log "Running schema-tools compare for breaking-change detection"
  BREAKING="$(schema-tools compare -p datarobot --old-path "$OLD_JSON" --new-path "$NEW_JSON" 2>/dev/null || true)"
  if [[ -n "$BREAKING" ]]; then
    echo
    echo "<details><summary>schema-tools compare</summary>"
    echo
    echo '```'
    echo "$BREAKING"
    echo '```'
    echo
    echo "</details>"
  fi
else
  log "schema-tools not on PATH; reporting key-set diff only"
fi
