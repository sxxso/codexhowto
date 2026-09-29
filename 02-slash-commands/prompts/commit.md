---
description: Generate a Conventional Commit message from the current diff
argument-hint: [optional-scope]
---

Look at the staged changes (`git diff --cached`). If nothing is staged, use the
full working-tree diff (`git diff`).

Write a single commit message in Conventional Commits format:

```
type(scope): short summary in the imperative mood

- optional bullet explaining a notable change
- optional bullet for another
```

Rules:

- `type` is one of: feat, fix, docs, style, refactor, perf, test, build, ci, chore.
- If a scope was provided ($ARGUMENTS), use it; otherwise infer a sensible scope from the changed paths.
- Keep the summary under 72 characters and in the imperative ("add", not "added").
- Only add body bullets when the change is non-trivial.
- Do not commit anything. Just print the proposed message so I can review it.
