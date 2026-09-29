---
description: Explain an error message or stack trace
argument-hint: [error-text]
---

Explain this error and how to fix it: $ARGUMENTS

Cover, in plain language:

1. **What it means** — translate the error/stack trace into what actually went
   wrong, without jargon.
2. **Where it originates** — the specific line or call in this codebase that
   triggered it (read the referenced files to confirm, don't assume).
3. **Why it happened** — the underlying condition or mistake that produced it.
4. **How to fix it** — the concrete change, with a code snippet.
5. **How to prevent it** — a guard, test, or pattern that stops it recurring.

If the error points outside this project (a dependency or the runtime), say so
and explain how our code triggers it. Keep it concrete and reference `file:line`.
