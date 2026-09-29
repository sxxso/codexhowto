---
description: Review changed files for bugs, security issues, and style
argument-hint: [focus-area]
---

Review the files changed in this branch (compare against the default branch, or
use the staged/working-tree diff if there is no branch to compare).

Focus area (optional): $ARGUMENTS

For each finding, report:

- **Severity**: blocker / major / minor / nit
- **Location**: `file:line`
- **Problem**: what is wrong and why it matters
- **Fix**: a concrete suggestion or code snippet

Group findings by severity, most severe first. If a focus area was given above,
weight the review toward it but still flag anything critical elsewhere. If you
find nothing worth changing, say so plainly instead of inventing issues.
