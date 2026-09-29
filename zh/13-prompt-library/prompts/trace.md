---
description: Trace an end-to-end flow through the codebase
argument-hint: [feature-or-entry-point]
---

Trace how `$1` works from entry point to result, following the real call chain
through this codebase.

Do the legwork:

1. **Find the entry point** — the route, command, event handler, or function
   where this flow begins.
2. **Follow the calls** — step through each function/module the flow passes
   through, in order. Read the code; do not guess at names.
3. **Note the data** — what the input is, how it is transformed at each hop, and
   what comes out.
4. **Flag branches** — important conditionals, error paths, and side effects
   (I/O, DB writes, external calls) along the way.

Present the trace as an ordered walkthrough with `file:line` at each step, and
end with a short summary of the full path. Point out anything fragile or
surprising. Read-only — do not change any code.
