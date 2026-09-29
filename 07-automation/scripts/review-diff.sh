#!/usr/bin/env bash
#
# review-diff.sh — pipe the current git diff into Codex for a quick review.
#
# Usage:
#   ./review-diff.sh            # review unstaged + staged working-tree changes
#   ./review-diff.sh --staged   # review only staged changes
#   ./review-diff.sh main       # review changes vs a base branch/ref
#
# Auth: run `codex login` once, or set OPENAI_API_KEY for headless use.
# Safety: runs Codex in a read-only sandbox — it inspects, it does not edit.

set -euo pipefail

# --- collect the diff -------------------------------------------------------
if [[ "${1:-}" == "--staged" ]]; then
  DIFF="$(git diff --staged)"
elif [[ -n "${1:-}" ]]; then
  # Treat the argument as a base ref: review "what this branch adds".
  BASE="$1"
  git fetch --quiet origin "$BASE" 2>/dev/null || true
  DIFF="$(git diff "$BASE"...)"
else
  DIFF="$(git diff HEAD)"
fi

# --- bail out early if there is nothing to review --------------------------
if [[ -z "${DIFF//[$'\t\r\n ']/}" ]]; then
  echo "No changes to review."
  exit 0
fi

# --- run the review ---------------------------------------------------------
printf '%s\n' "$DIFF" | codex exec --sandbox read-only "$(cat <<'PROMPT'
You are reviewing a git diff. Report only concrete, actionable findings:
- Bugs and logic errors
- Security issues (injection, secrets, unsafe deserialization)
- Missing error handling or edge cases
Group findings by severity (Blocking / Warning / Nit). If nothing is wrong,
say so in one line. Do not restate the diff.
PROMPT
)"
