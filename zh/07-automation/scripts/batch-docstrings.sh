#!/usr/bin/env bash
#
# batch-docstrings.sh — add or fix docstrings across many files with Codex.
#
# Codex edits files here, so it runs in a workspace-write sandbox (--full-auto).
# SAFETY:
#   - Commit or stash your work first; this script changes files in place.
#   - Run inside a clean git tree so you can `git diff` / `git checkout` to undo.
#   - Review the resulting diff before committing.
#
# Usage:
#   ./batch-docstrings.sh "src/**/*.py"
#   ./batch-docstrings.sh "lib/**/*.ts"

set -euo pipefail

PATTERN="${1:?usage: batch-docstrings.sh <glob-pattern>}"

# Refuse to run on a dirty tree so changes stay reviewable.
if [[ -n "$(git status --porcelain)" ]]; then
  echo "Working tree is not clean. Commit or stash first." >&2
  exit 1
fi

# Enable ** recursive globbing in bash.
shopt -s globstar nullglob

count=0
for f in $PATTERN; do
  [[ -f "$f" ]] || continue
  echo "== $f =="
  codex exec --full-auto "Add missing docstrings and fix inaccurate ones in the
file '$f'. Follow the project's existing docstring style. Do NOT change any
runtime behavior, signatures, or logic — comments and docstrings only."
  count=$((count + 1))
done

echo "Processed $count file(s). Review with: git diff"
