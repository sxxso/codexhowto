#!/usr/bin/env bash
# codemod-plan-then-apply.sh — Safe two-phase codemod with Codex CLI.
#
# Phase 1 plans the change in a read-only sandbox and shows it to you.
# Phase 2 applies it in workspace-write only after you confirm, then runs tests.
# This "plan first, apply second" split keeps a wide-blast-radius change from
# editing everything in one unreviewed pass.
#
# Usage:
#   ./codemod-plan-then-apply.sh "describe the change in one sentence"
# Example:
#   ./codemod-plan-then-apply.sh "replace log.warn(msg) with logger.warning(msg)"

set -euo pipefail

CHANGE="${1:?usage: codemod-plan-then-apply.sh \"change description\"}"
PLAN="codemod-plan.md"

echo "== Phase 1: planning (read-only) =="
# read-only guarantees the planning step cannot touch a single file.
codex exec \
  --sandbox read-only \
  --output-last-message "$PLAN" \
  "Plan this codemod: $CHANGE
   List every affected file with line numbers and the exact before/after.
   Output a plan ONLY — do not edit anything."

echo
cat "$PLAN"
echo
read -r -p "Apply this plan? [y/N] " REPLY
case "$REPLY" in
  y|Y)
    echo "== Phase 2: applying (workspace-write) =="
    # on-request lets Codex pause before anything outside the stated plan.
    codex exec \
      --sandbox workspace-write \
      --ask-for-approval on-request \
      "Apply the codemod described in $PLAN: $CHANGE
       Change only the call sites in that plan. Then run the test suite and
       report the result."
    echo "Done. Review with: git diff --stat"
    ;;
  *)
    echo "Aborted. Plan left in $PLAN for review."
    ;;
esac
