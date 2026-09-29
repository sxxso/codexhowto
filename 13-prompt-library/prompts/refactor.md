---
description: Refactor code without changing behavior
argument-hint: [file-or-symbol]
---

Refactor `$1` to improve its clarity and structure while preserving its exact
behavior.

Before changing anything:

- Read the target and its callers so you understand the current contract.
- Confirm there are tests covering it. If there are none, note that and describe
  how you will verify behavior is unchanged.

Then refactor with these priorities:

1. **Names** — make functions and variables say what they do.
2. **Structure** — reduce nesting, split overlong functions, remove duplication.
3. **Dead code** — delete unreachable or unused branches.
4. **Consistency** — match the surrounding style, idioms, and libraries.

Do NOT change the public API, add features, or alter observable behavior. After
refactoring, run the project's tests (or explain how to) and report the result.
Summarize what changed and why in a short list.
