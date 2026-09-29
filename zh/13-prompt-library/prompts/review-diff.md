---
description: Review a specific commit range or diff
argument-hint: [git-ref-or-range]
---

Review the diff for `$1` (for example a commit hash, a branch name, or a range
like `main..HEAD`). If no ref was given above, review the staged changes, and
fall back to the working-tree diff if nothing is staged.

Run the appropriate `git diff`/`git show` yourself to see the exact changes
before commenting.

For each finding, report:

- **Severity**: blocker / major / minor / nit
- **Location**: `file:line`
- **Problem**: what is wrong and why it matters
- **Fix**: a concrete suggestion or code snippet

Cover correctness, edge cases, error handling, and readability. Call out any
change that alters behavior without a corresponding test. Group findings by
severity, most severe first. If nothing needs changing, say so plainly.
