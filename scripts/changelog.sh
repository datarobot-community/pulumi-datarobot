#!/usr/bin/env bash
# Maintain CHANGELOG.md. The section format lives here and nowhere else, so the
# upgrade workflow (which writes) and the release workflow (which reads) stay in sync.
#
# Usage:
#   scripts/changelog.sh insert <version> <notes-file>   # add/replace a version section
#   scripts/changelog.sh extract <version>               # print a version's body
#
# extract exits non-zero when the version has no section, so callers can fall back.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.."; pwd)"
CHANGELOG="${CHANGELOG:-$ROOT/CHANGELOG.md}"

log() { echo "$@" >&2; }

usage() {
  echo "Usage: $0 insert <version> <notes-file>" >&2
  echo "       $0 extract <version>" >&2
  exit 2
}

# Drop leading and trailing blank lines, preserving internal spacing.
trim_blank_lines() {
  awk '
    NF { while (pending-- > 0) print ""; pending = 0; started = 1; print; next }
    started { pending++ }
  '
}

cmd_insert() {
  local version="${1#v}"
  local notes_file="$2"
  local date="${CHANGELOG_DATE:-$(date -u +%Y-%m-%d)}"

  [[ -f "$notes_file" ]] || { log "ERROR: notes file $notes_file not found"; exit 1; }
  [[ -f "$CHANGELOG" ]] || { log "ERROR: $CHANGELOG not found"; exit 1; }

  local stripped inserted preserved
  stripped="$(mktemp)"
  inserted="$(mktemp)"
  preserved="$(mktemp)"
  trap 'rm -f "$stripped" "$inserted" "$preserved"' RETURN

  # "### Provider changes" is hand-written (repo-local changes that upstream knows
  # nothing about), so carry it over instead of letting a regenerate drop it.
  awk -v want="$version" '
    /^## / {
      insec = 0
      if (match($0, /\[[^]]+\]/)) {
        v = substr($0, RSTART + 1, RLENGTH - 2)
        sub(/^v/, "", v)
        if (v == want) { insec = 1 }
      }
      next
    }
    insec && /^### / { keep = ($0 == "### Provider changes") }
    insec && keep { print }
  ' "$CHANGELOG" | trim_blank_lines >"$preserved"

  if [[ -s "$preserved" ]]; then
    log "Preserving the existing '### Provider changes' block for v${version}"
  else
    preserved=""
  fi

  # Remove any existing section for this version so re-running is idempotent.
  awk -v want="$version" '
    /^## / {
      drop = 0
      if (match($0, /\[[^]]+\]/)) {
        v = substr($0, RSTART + 1, RLENGTH - 2)
        sub(/^v/, "", v)
        if (v == want) { drop = 1 }
      }
    }
    !drop { print }
  ' "$CHANGELOG" >"$stripped"

  # Splice the new section in above the newest released version, leaving
  # "## [Unreleased]" (and any hand-written entries under it) untouched.
  awk -v hdr="## [$version] - $date" -v notes="$notes_file" -v preserved="$preserved" '
    function emit_section(   line) {
      print hdr
      print ""
      if (preserved != "") {
        while ((getline line < preserved) > 0) { print line }
        close(preserved)
        print ""
      }
      while ((getline line < notes) > 0) { print line }
      close(notes)
      print ""
    }
    !done && /^## \[/ && tolower($0) !~ /^## \[unreleased\]/ {
      emit_section()
      done = 1
    }
    { print }
    END { if (!done) { print ""; emit_section() } }
  ' "$stripped" >"$inserted"

  # Collapse any run of blank lines introduced by the splice down to one.
  awk 'NF { blank = 0; print; next } { if (!blank++) print }' "$inserted" >"$CHANGELOG"

  log "Wrote CHANGELOG.md section for v${version} (${date})"
}

cmd_extract() {
  local version="${1#v}"
  [[ -f "$CHANGELOG" ]] || { log "ERROR: $CHANGELOG not found"; exit 1; }

  local body
  body="$(awk -v want="$version" '
    /^## / {
      if (found) { exit }
      if (match($0, /\[[^]]+\]/)) {
        v = substr($0, RSTART + 1, RLENGTH - 2)
        sub(/^v/, "", v)
        if (v == want) { found = 1 }
      }
      next
    }
    found { print }
    END { if (!found) { exit 1 } }
  ' "$CHANGELOG" | trim_blank_lines)" || {
    log "No CHANGELOG.md section for v${version}"
    return 1
  }

  if [[ -z "$body" ]]; then
    log "CHANGELOG.md section for v${version} is empty"
    return 1
  fi

  printf '%s\n' "$body"
}

[[ $# -ge 2 ]] || usage

case "$1" in
  insert)  [[ $# -eq 3 ]] || usage; cmd_insert "$2" "$3" ;;
  extract) [[ $# -eq 2 ]] || usage; cmd_extract "$2" ;;
  *)       usage ;;
esac
