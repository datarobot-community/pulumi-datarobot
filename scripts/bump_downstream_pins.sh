#!/usr/bin/env bash
# Open a PR in each repo that pins this provider, bumping it to <version>.
# Called by the notify_downstream job in .github/workflows/release.yml once a
# release's SDK is published, so downstream repos stop drifting behind.
#
# Why this lives here rather than in each downstream repo: opening the PRs from
# one place with a PAT means only one credential to configure, no bump workflow
# to keep in step across three repos, and -- because a PAT-opened PR is not
# subject to the rule that GITHUB_TOKEN-opened PRs don't trigger workflows --
# each bump PR gets that repo's normal CI.
#
# The cost is this file: the pin locations below are knowledge about other
# repos' layouts. If a downstream repo moves or restructures its pins, this
# script is what breaks, and the failure shows up as a warning on a release run
# rather than in that repo. Update the per-repo section when that happens.
#
# Nothing here ever merges. Each repo gets a PR for a human to review, and a
# repo that can't be bumped is reported as a warning without failing the
# release -- by the time this runs, the provider is already published, so a
# release must not be marked failed over a downstream problem.
#
# Usage: scripts/bump_downstream_pins.sh <version>     # e.g. 0.11.2
#        DRY_RUN=1 scripts/bump_downstream_pins.sh <version>
#
# DRY_RUN does everything except push and open PRs -- it clones, applies the
# edits and prints the diff each PR would contain. Use it to check this script
# still understands the downstream repos' layouts after they change something.
#
# Requires: git, gh (authenticated with a token that can push and open PRs on
# the downstream repos), jq, curl, python3.
set -euo pipefail

VERSION="${1:-}"

PROVIDER_REPO="datarobot-community/pulumi-datarobot"
PYPI_PACKAGE="pulumi-datarobot"
VERIFY_RETRY_DELAY="${VERIFY_RETRY_DELAY:-15}"
DRY_RUN="${DRY_RUN:-}"

DOWNSTREAM_REPOS=(
  datarobot-community/af-component-base
  datarobot/nbx-kernels
  datarobot/datarobot-user-models
)

BRANCH_PREFIX="auto/bump-pulumi-datarobot"

# ---------------------------------------------------------------------------
# Version availability
# ---------------------------------------------------------------------------

# True when $VERSION is installable from PyPI (a non-yanked release with files)
# and cut as a non-draft, non-prerelease GitHub release. Retried because this
# runs seconds after the SDK publish step and PyPI's index lags its own publish
# API. Bumping a downstream pin to a version pip can't install would break that
# repo's builds, so this gates everything below.
version_available() {
  local attempt pypi_json

  for attempt in 1 2 3 4 5 6; do
    if [ "$attempt" -gt 1 ]; then
      echo "  not visible yet, retrying in ${VERIFY_RETRY_DELAY}s (attempt ${attempt}/6)..."
      sleep "$VERIFY_RETRY_DELAY"
    fi

    if ! pypi_json="$(curl -fsS --retry 3 --retry-delay 2 --max-time 30 \
        "https://pypi.org/pypi/${PYPI_PACKAGE}/${VERSION}/json" 2>/dev/null)"; then
      continue
    fi

    # A version whose files are all yanked is published but not installable.
    if ! jq -e '.urls | length > 0 and any(.[]; .yanked == false)' >/dev/null 2>&1 <<<"$pypi_json"; then
      continue
    fi

    if ! gh release view "v${VERSION}" --repo "$PROVIDER_REPO" \
        --json isDraft,isPrerelease \
        --jq 'select(.isDraft == false and .isPrerelease == false)' >/dev/null 2>&1; then
      continue
    fi

    return 0
  done

  return 1
}

# ---------------------------------------------------------------------------
# Per-repo pin knowledge
#
# Each repo gets a reader that prints the currently pinned version, and an
# editor that rewrites the pins to $VERSION. Both run inside a fresh clone of
# that repo. Editors match exact line shapes rather than doing a blind
# find-and-replace that could hit an unrelated occurrence of the same version.
#
# A reader must fail loudly if the pin isn't the shape it expects -- that means
# the file changed in a way this script doesn't understand, and guessing is
# worse than reporting it.
# ---------------------------------------------------------------------------

BARE_RE='[0-9]+\.[0-9]+\.[0-9]+'

# $VERSION is interpolated into sed replacements, branch names and PR bodies, so
# every path that can write a file checks it. main() validates the argument up
# front; replace_pin re-checks because it is the single choke point all edits
# pass through, and the functions here are sourceable for testing where
# $VERSION would otherwise be whatever the caller left set.
require_valid_version() {
  if ! [[ "${VERSION:-}" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    echo "ERROR: VERSION is '${VERSION:-}', not a bare X.Y.Z version. Refusing to edit any file." >&2
    return 1
  fi
}

# Prints the single version matched by $2 in file $1, or fails.
read_single() {
  local file="$1" line_re="$2" label="$3" count versions distinct

  if [ ! -f "$file" ]; then
    echo "ERROR: ${file} does not exist -- has it moved?" >&2
    return 1
  fi

  count="$(grep -cE "$line_re" "$file" || true)"
  if [ "$count" -ne 1 ]; then
    echo "ERROR: expected exactly 1 ${label} line in ${file}, found ${count}." >&2
    return 1
  fi

  versions="$(grep -oE "$line_re" "$file" | grep -oE "$BARE_RE" | sort -u)"
  distinct="$(printf '%s\n' "$versions" | grep -c . || true)"
  if [ "$distinct" -ne 1 ]; then
    echo "ERROR: could not determine a single ${label} version in ${file}." >&2
    return 1
  fi

  printf '%s' "$versions"
}

# Rewrites $2 -> $VERSION on lines matching sed expression $3 in file $1, then
# confirms both that the old version is gone AND that the exact expected new
# line $4 is present. Checking only that the old version disappeared is not
# enough: a malformed replacement would also remove it, leaving a corrupt pin
# (">=" with no version) that looks like a successful edit. A partial or
# corrupt edit is worse than no edit.
replace_pin() {
  local file="$1" current="$2" sed_expr="$3" expected="$4" escaped
  require_valid_version || return 1
  escaped="$(printf '%s' "$current" | sed -E 's/\./\\./g')"

  sed -E "${sed_expr//__CUR__/$escaped}" "$file" >"${file}.bump_tmp"
  mv "${file}.bump_tmp" "$file"

  if ! grep -qF "$expected" "$file"; then
    echo "ERROR: ${file} does not contain '${expected}' after editing -- the replacement did not apply as expected." >&2
    return 1
  fi

  if grep -qF "$current" "$file"; then
    echo "ERROR: ${current} is still present in ${file} after editing." >&2
    return 1
  fi
}

# --- af-component-base ------------------------------------------------------
# Two pins that must always agree: the Python SDK floor and the pulumi plugin
# binary version. They drifted apart once (a manual bump updated the SDK floor
# and missed the plugin), which is why both move here or neither does. The
# plugin download URL derives from the plugin version, so it follows on its own.
AFCB_PYPROJECT="template/infra/pyproject.toml.jinja"
AFCB_TASKFILE="template/infra/Taskfile.yaml.jinja"
AFCB_SDK_RE='^[[:space:]]*"pulumi-datarobot>='"${BARE_RE}"'",$'
AFCB_PLUGIN_RE='^[[:space:]]*echo "v'"${BARE_RE}"'"$'
AFCB_DERIVED_URL='releases/download/{{ "{{.PULUMI_DATAROBOT_PLUGIN_VERSION}}" }}'

read_af_component_base() {
  local sdk plugin

  # If the URL has been hardcoded again, bumping the two pins would leave it
  # pointing at the old release.
  if ! grep -qF "$AFCB_DERIVED_URL" "$AFCB_TASKFILE"; then
    echo "ERROR: ${AFCB_TASKFILE} no longer derives the plugin download URL from PULUMI_DATAROBOT_PLUGIN_VERSION." >&2
    return 1
  fi

  sdk="$(read_single "$AFCB_PYPROJECT" "$AFCB_SDK_RE" "SDK floor")" || return 1
  plugin="$(read_single "$AFCB_TASKFILE" "$AFCB_PLUGIN_RE" "plugin version")" || return 1

  if [ "$sdk" != "$plugin" ]; then
    echo "ERROR: pins have drifted out of sync (SDK >=${sdk}, plugin v${plugin}). Refusing to guess which is correct." >&2
    return 1
  fi

  printf '%s' "$sdk"
}

edit_af_component_base() {
  local current="$1"
  replace_pin "$AFCB_PYPROJECT" "$current" \
    "s/^([[:space:]]*)\"pulumi-datarobot>=__CUR__\",\$/\\1\"pulumi-datarobot>=${VERSION}\",/" \
    "\"pulumi-datarobot>=${VERSION}\"," || return 1
  replace_pin "$AFCB_TASKFILE" "$current" \
    "s/^([[:space:]]*)echo \"v__CUR__\"\$/\\1echo \"v${VERSION}\"/" \
    "echo \"v${VERSION}\"" || return 1
  STAGE_PATHS=("$AFCB_PYPROJECT" "$AFCB_TASKFILE")
  PR_FILE_NOTES="- \`${AFCB_PYPROJECT}\` — the Python SDK floor
- \`${AFCB_TASKFILE}\` — the pulumi plugin binary version

These two must always agree. The plugin download URL derives from the plugin version, so it follows automatically and is not edited here."
}

# --- nbx-kernels ------------------------------------------------------------
NBX_PIN="kernels/python/requirements-dr-notebooks.txt"
PIN_EQ_RE='^pulumi-datarobot=='"${BARE_RE}"'$'

read_nbx_kernels() { read_single "$NBX_PIN" "$PIN_EQ_RE" "pulumi-datarobot pin"; }

edit_nbx_kernels() {
  local current="$1"
  replace_pin "$NBX_PIN" "$current" \
    "s/^pulumi-datarobot==__CUR__\$/pulumi-datarobot==${VERSION}/" \
    "pulumi-datarobot==${VERSION}" || return 1
  STAGE_PATHS=("$NBX_PIN")
  PR_FILE_NOTES="- \`${NBX_PIN}\` — the pin installed into every Python kernel image

The kernel Dockerfiles are unchanged: they install from this requirements file rather than hardcoding a version."
}

# --- datarobot-user-models --------------------------------------------------
# Bumping the environment's contents obliges us to give it a new
# environmentVersionId, or the platform treats it as unchanged. Harness has
# update_env_version input sets for the public_dropin_environments envs but none
# for the notebook environments, so nothing else does this for python313.
DUM_ENV_DIR="public_dropin_notebook_environments/python313_notebook"
DUM_PIN="${DUM_ENV_DIR}/requirements.txt"
DUM_ENV_INFO="${DUM_ENV_DIR}/env_info.json"

read_datarobot_user_models() { read_single "$DUM_PIN" "$PIN_EQ_RE" "pulumi-datarobot pin"; }

edit_datarobot_user_models() {
  local current="$1"
  replace_pin "$DUM_PIN" "$current" \
    "s/^pulumi-datarobot==__CUR__\$/pulumi-datarobot==${VERSION}/" \
    "pulumi-datarobot==${VERSION}" || return 1

  # The repo's own script, the same one .harness/update_env_version.yaml runs.
  # It only rewrites environmentVersionId; bson comes from pymongo and it makes
  # no network calls.
  if ! python3 -c "import bson" >/dev/null 2>&1; then
    python3 -m pip install --quiet --disable-pip-version-check pymongo >&2 || {
      echo "ERROR: could not install pymongo, needed by tools/env_version_update.py." >&2
      return 1
    }
  fi
  python3 tools/env_version_update.py --file "$DUM_ENV_INFO" >&2 || {
    echo "ERROR: tools/env_version_update.py failed." >&2
    return 1
  }
  if git diff --quiet -- "$DUM_ENV_INFO"; then
    echo "ERROR: ${DUM_ENV_INFO} was not changed -- expected a new environmentVersionId." >&2
    return 1
  fi

  STAGE_PATHS=("$DUM_PIN" "$DUM_ENV_INFO")
  PR_FILE_NOTES="- \`${DUM_PIN}\` — the pin for the Python 3.13 notebook environment
- \`${DUM_ENV_INFO}\` — a fresh \`environmentVersionId\`, so the platform treats this as a new environment version

The \`environmentVersionId\` was regenerated with this repo's own \`tools/env_version_update.py\`. Harness has \`update_env_version\` input sets for the \`public_dropin_environments\` envs but none for the notebook environments, so it is not done automatically here."
}

# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

# Bump one repo. Returns non-zero only on a real problem; "nothing to do" is a
# success.
bump_one() {
  local repo="$1"
  local slug fn_suffix default_branch current branch workdir existing

  slug="${repo##*/}"
  fn_suffix="${slug//-/_}"

  echo "=== ${repo} ==="

  workdir="$(mktemp -d)"
  if ! default_branch="$(gh repo view "$repo" --json defaultBranchRef --jq '.defaultBranchRef.name')"; then
    echo "ERROR: could not read ${repo}." >&2
    return 1
  fi

  # Credentials come from gh's git helper, so the token never appears in a
  # remote URL or in the logs.
  if ! git clone --quiet --depth 1 --branch "$default_branch" \
      "https://github.com/${repo}.git" "${workdir}/repo"; then
    echo "ERROR: could not clone ${repo}." >&2
    return 1
  fi

  pushd "${workdir}/repo" >/dev/null || return 1

  if ! current="$("read_${fn_suffix}")"; then
    popd >/dev/null || true
    return 1
  fi
  echo "  currently pinned: ${current}"

  if [ "$current" = "$VERSION" ]; then
    echo "  already at ${VERSION} -- nothing to do."
    popd >/dev/null || true
    return 0
  fi

  # Don't bump backwards if the repo is pinned ahead for some reason.
  if [ "$(printf '%s\n%s\n' "$VERSION" "$current" | sort -V | tail -n1)" != "$VERSION" ]; then
    echo "  pinned ${current} is newer than ${VERSION} -- leaving it alone."
    popd >/dev/null || true
    return 0
  fi

  branch="${BRANCH_PREFIX}-${current}-to-${VERSION}"

  # De-dup on branch names, compared literally. Matches both this script's
  # branch and Dependabot's (dependabot/pip/.../pulumi-datarobot-<version>), so
  # a repo keeping Dependabot as a backstop never gets two PRs for the same
  # version. Deliberately not `gh pr list --search`, which is a fuzzy full-text
  # query and matches any open PR that merely mentions the version strings.
  existing="$(gh pr list --repo "$repo" --state open --json number,headRefName 2>/dev/null \
    | jq -r --arg branch "$branch" --arg suffix "pulumi-datarobot-${VERSION}" \
        '[.[] | select(.headRefName == $branch or (.headRefName | endswith($suffix)))] | .[0].number // empty' \
    2>/dev/null || true)"
  if [ -n "$existing" ]; then
    echo "  an open PR already proposes ${VERSION} (#${existing}) -- nothing to do."
    popd >/dev/null || true
    return 0
  fi

  # Branch present with no open PR: its PR was closed on purpose. Recreating it
  # would reopen a decision a human already made.
  if git ls-remote --exit-code --heads origin "$branch" >/dev/null 2>&1; then
    echo "  branch ${branch} exists on origin with no open PR -- its PR was probably closed deliberately. Skipping." >&2
    popd >/dev/null || true
    return 0
  fi

  STAGE_PATHS=()
  PR_FILE_NOTES=""
  if ! "edit_${fn_suffix}" "$current"; then
    popd >/dev/null || true
    return 1
  fi

  git checkout -q -b "$branch"
  git -c user.name="github-actions[bot]" \
      -c user.email="41898282+github-actions[bot]@users.noreply.github.com" \
      commit -q -m "chore: bump pulumi-datarobot from ${current} to ${VERSION}" \
      -- "${STAGE_PATHS[@]}"

  if [ -n "$DRY_RUN" ]; then
    echo "  DRY_RUN: would open ${branch} against ${default_branch}. Diff:"
    git --no-pager show --stat --format="    commit %s" HEAD | sed 's/^/    /'
    git --no-pager diff HEAD~1 HEAD -- "${STAGE_PATHS[@]}" \
      | grep -E "^[+-][^+-]" | sed 's/^/      /'
    popd >/dev/null || true
    return 0
  fi

  if ! git push -q -u origin "$branch"; then
    echo "ERROR: could not push ${branch} to ${repo}." >&2
    popd >/dev/null || true
    return 1
  fi

  local body_file
  body_file="$(mktemp)"
  cat >"$body_file" <<BODY
Automated bump of the pinned [pulumi-datarobot](https://github.com/${PROVIDER_REPO}) provider (\`${current}\` → \`${VERSION}\`), opened by that provider's release pipeline.

## Files changed

${PR_FILE_NOTES}

## Verification

\`${VERSION}\` was confirmed installable from PyPI **and** cut as a non-draft, non-prerelease GitHub release before this PR was opened. Beyond that, validation is whatever this repo's own PR checks do with it.

Worth a human eye on the [release notes](https://github.com/${PROVIDER_REPO}/releases/tag/v${VERSION}): \`pulumi-datarobot\` is a \`0.x\` provider, so a minor bump can carry breaking resource changes even when it looks routine.

This automation never auto-merges.
BODY

  if ! gh pr create --repo "$repo" --base "$default_branch" --head "$branch" \
      --title "chore: bump pulumi-datarobot from ${current} to ${VERSION}" \
      --body-file "$body_file"; then
    echo "ERROR: pushed ${branch} to ${repo} but could not open a PR." >&2
    rm -f "$body_file"
    popd >/dev/null || true
    return 1
  fi

  rm -f "$body_file"
  popd >/dev/null || true
  return 0
}

main() {
  if [ -z "$VERSION" ]; then
    echo "Usage: $0 <version>" >&2
    return 1
  fi

  require_valid_version || return 1

  echo "Bumping downstream pins to pulumi-datarobot ${VERSION}"
  echo "Confirming ${VERSION} is installable from PyPI and cut as a GitHub release..."
  if ! version_available; then
    echo "ERROR: pulumi-datarobot ${VERSION} is not available on both PyPI and GitHub. Not opening any PRs." >&2
    return 1
  fi
  echo "Confirmed."
  echo

  # gh's git credential helper, so clones and pushes use GH_TOKEN without it
  # appearing in a URL.
  gh auth setup-git

  local failed="" repo
  for repo in "${DOWNSTREAM_REPOS[@]}"; do
    if ! bump_one "$repo"; then
      failed="${failed} ${repo}"
    fi
    echo
  done

  if [ -n "$failed" ]; then
    echo "Could not bump:${failed}" >&2
    return 2
  fi

  echo "Done."
}

# Sourced (by a test) => definitions only. Executed => run.
if [ "${BASH_SOURCE[0]}" = "${0}" ]; then
  main "$@"
fi
