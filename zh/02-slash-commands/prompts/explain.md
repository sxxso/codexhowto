---
description: Explain a file step by step for a new teammate
argument-hint: [file]
---

Explain the file `$1` to a developer who is new to this codebase.

Cover:

1. **Purpose** — what this file is responsible for and where it fits in the project.
2. **Key pieces** — the main functions, classes, or exports and what each does.
3. **Data flow** — how information enters, moves through, and leaves this file.
4. **Dependencies** — what it imports and what depends on it.
5. **Gotchas** — anything surprising, fragile, or easy to misuse.

Read the file before answering. Use short paragraphs and reference specific
symbols with `file:line`. Keep it concrete — no generic filler.
