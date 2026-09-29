---
description: Write thorough tests for a file or function
argument-hint: [file-or-symbol]
---

Write tests for `$1`.

First, discover the setup:

- Find the test framework and runner this project already uses (check config
  files and existing tests). Match its conventions exactly — do not introduce a
  new framework.
- Read the target so you understand its inputs, outputs, and error paths.

Then write tests that cover:

1. **Happy path** — typical, valid inputs.
2. **Edge cases** — empty, boundary, and unusual-but-valid inputs.
3. **Error paths** — invalid input and failure conditions, asserting the right
   error or handling.
4. **Regressions** — any behavior that would be easy to break.

Keep each test focused and clearly named for what it verifies. Use the project's
existing fixtures/mocks style. After writing, run the test suite and report
whether it passes; fix any failures in the tests you added.
