---
description: Add or improve docstrings/comments for a file
argument-hint: [file]
---

Add or improve the documentation comments in `$1`.

Read the file first so the docs describe what the code actually does. Then:

- Document every public function, class, and exported symbol using the language's
  standard docstring/comment convention (JSDoc, Python docstrings, rustdoc, etc.)
  — match whatever this project already uses.
- For each, cover: purpose, parameters, return value, raised errors/exceptions,
  and any non-obvious side effects.
- Add brief inline comments only where the code is genuinely non-obvious; do not
  narrate self-explanatory lines.
- Keep wording tight and accurate. Do not change any code behavior.

If existing docs are wrong or stale, correct them. Preserve the file's existing
comment density and tone. Show the diff when done.
