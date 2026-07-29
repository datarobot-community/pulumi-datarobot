#!/usr/bin/env bash
# Summarise what changed in the upstream terraform-provider-datarobot between two
# versions, as markdown on stdout. Progress and warnings go to stderr.
#
# Usage: scripts/upstream-changelog.sh <old-version> <new-version>
#   e.g. scripts/upstream-changelog.sh v0.10.42 v0.10.45
#
# Upstream keeps a Keep-a-Changelog CHANGELOG.md but its GitHub Releases have empty
# bodies, so the file is the only prose source. The file also has gaps (0.10.44 has no
# section), so any version without one falls back to a filtered commit list.
#
# Requires: gh (authenticated), jq.
set -euo pipefail

UPSTREAM_REPO="${UPSTREAM_REPO:-datarobot-community/terraform-provider-datarobot}"
UPSTREAM_URL="https://github.com/${UPSTREAM_REPO}"

if [[ $# -lt 2 ]]; then
  echo "Usage: $0 <old-version> <new-version>" >&2
  exit 2
fi

# Versions are compared without the leading "v"; tags carry it.
OLD="${1#v}"
NEW="${2#v}"

log() { echo "$@" >&2; }

# True when $1 sorts strictly before $2 under version ordering.
ver_lt() {
  [[ "$1" != "$2" ]] && [[ "$(printf '%s\n%s\n' "$1" "$2" | sort -V | head -n1)" == "$1" ]]
}

# Commit subjects worth showing a reader: drop merges, CI/chore churn, and the
# release commit itself. Mirrors the exclude list in .goreleaser.yml.
NOISE_RE='^(Merge branch|Merge pull request|Release v?[0-9]|Update pipeline|Bump )|\b(ci|chore|internal)\b'

if [[ "$OLD" == "$NEW" ]]; then
  echo "_No upstream provider change in this release (still \`v${NEW}\`)._"
  exit 0
fi

if ver_lt "$NEW" "$OLD"; then
  log "WARN: new version v${NEW} is older than v${OLD}; reporting as a downgrade"
  echo "_Upstream provider was moved back from \`v${OLD}\` to \`v${NEW}\`._"
  exit 0
fi

log "Collecting upstream changes for ${UPSTREAM_REPO} v${OLD} -> v${NEW}"

# --- upstream tags in (OLD, NEW] -------------------------------------------------

ALL_TAGS="$(gh api "repos/${UPSTREAM_REPO}/tags" --paginate --jq '.[].name' 2>/dev/null \
  | sed 's/^v//' \
  | grep -E '^[0-9]+\.[0-9]+\.[0-9]+$' \
  | sort -V -u || true)"

VERSIONS=()
while IFS= read -r tag; do
  [[ -n "$tag" ]] || continue
  if ver_lt "$OLD" "$tag" && { [[ "$tag" == "$NEW" ]] || ver_lt "$tag" "$NEW"; }; then
    VERSIONS+=("$tag")
  fi
done <<<"$ALL_TAGS"

# If the tag listing failed or is incomplete, at least report the target version.
if [[ ${#VERSIONS[@]} -eq 0 ]]; then
  log "WARN: no upstream tags found in (v${OLD}, v${NEW}]; falling back to v${NEW} alone"
  VERSIONS=("$NEW")
fi

# --- upstream CHANGELOG.md at the new tag ----------------------------------------

CHANGELOG_FILE="$(mktemp)"
trap 'rm -f "$CHANGELOG_FILE"' EXIT

if ! gh api -H "Accept: application/vnd.github.raw" \
     "repos/${UPSTREAM_REPO}/contents/CHANGELOG.md?ref=v${NEW}" >"$CHANGELOG_FILE" 2>/dev/null; then
  log "WARN: could not fetch upstream CHANGELOG.md at v${NEW}; using commit lists only"
  : >"$CHANGELOG_FILE"
fi

# Drop leading and trailing blank lines, preserving internal spacing.
trim_blank_lines() {
  awk '
    NF { while (pending-- > 0) print ""; pending = 0; started = 1; print; next }
    started { pending++ }
  '
}

# Body of the "## [x.y.z] - date" section for $1, with its "### Added"-style headers
# demoted so they nest under the "#### vx.y.z" heading this script emits.
extract_section() {
  awk -v want="$1" '
    /^## / {
      inside = 0
      if (match($0, /\[[^]]+\]/)) {
        v = substr($0, RSTART + 1, RLENGTH - 2)
        sub(/^v/, "", v)
        if (v == want) { inside = 1 }
      }
      next
    }
    inside {
      if ($0 ~ /^### /) { sub(/^### /, "##### ") }
      print
    }
  ' "$CHANGELOG_FILE" | trim_blank_lines
}

# Date from the "## [x.y.z] - 2026-07-27" header, if present.
extract_date() {
  awk -v want="$1" '
    /^## / && match($0, /\[[^]]+\]/) {
      v = substr($0, RSTART + 1, RLENGTH - 2)
      sub(/^v/, "", v)
      if (v == want && match($0, /[0-9]{4}-[0-9]{2}-[0-9]{2}/)) {
        print substr($0, RSTART, RLENGTH)
        exit
      }
    }
  ' "$CHANGELOG_FILE"
}

# Filtered commit subjects between two refs.
commits_between() {
  gh api "repos/${UPSTREAM_REPO}/compare/$1...$2" \
    --jq '.commits[].commit.message | split("\n")[0]' 2>/dev/null \
    | grep -Ev "$NOISE_RE" || true
}

# --- emit -------------------------------------------------------------------------

echo "### Upstream provider changes"
echo
echo "[terraform-provider-datarobot](${UPSTREAM_URL}) \`v${OLD}\` → \`v${NEW}\`"

prev="$OLD"
for version in "${VERSIONS[@]}"; do
  date="$(extract_date "$version")"
  echo
  if [[ -n "$date" ]]; then
    echo "#### [v${version}](${UPSTREAM_URL}/releases/tag/v${version}) — ${date}"
  else
    echo "#### [v${version}](${UPSTREAM_URL}/releases/tag/v${version})"
  fi
  echo

  section="$(extract_section "$version")"
  if [[ -n "$section" ]]; then
    echo "$section"
  else
    log "No CHANGELOG.md entry for v${version}; falling back to commits v${prev}...v${version}"
    echo "_No entry in the upstream CHANGELOG.md. Commits in this range:_"
    echo
    subjects="$(commits_between "v${prev}" "v${version}")"
    if [[ -n "$subjects" ]]; then
      while IFS= read -r subject; do
        [[ -n "$subject" ]] && echo "- ${subject}"
      done <<<"$subjects"
    else
      echo "- _(no notable commits found)_"
    fi
  fi
  prev="$version"
done

echo
echo "Full upstream diff: [${UPSTREAM_URL}/compare/v${OLD}...v${NEW}](${UPSTREAM_URL}/compare/v${OLD}...v${NEW})"
