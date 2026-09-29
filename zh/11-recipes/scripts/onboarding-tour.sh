#!/usr/bin/env bash
# onboarding-tour.sh — Read-only guided tour of an unfamiliar repository.
#
# Runs Codex CLI in a strictly read-only sandbox so it can explore but never
# edit. Writes the tour to a file you can commit as onboarding notes.
#
# Usage:
#   ./onboarding-tour.sh [output-file]
# Default output: REPO-TOUR.md in the current directory.

set -euo pipefail

OUT="${1:-REPO-TOUR.md}"

# on-request + read-only: Codex may read anything, but cannot modify files
# and will surface (not silently take) any action that needs more access.
codex exec \
  --sandbox read-only \
  --output-last-message "$OUT" \
  "You are onboarding a new engineer to this repository. Produce, in Markdown:
   1. One paragraph on what this project does.
   2. The top-level layout, one line per directory.
   3. Main entry points and how control flows through them.
   4. Build, test, and run commands — read them from config files, do not guess.
   5. The five files worth reading first, and why.
   Do not modify anything."

echo "Tour written to $OUT"
