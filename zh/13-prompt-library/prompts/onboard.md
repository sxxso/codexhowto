---
description: Get oriented in an unfamiliar codebase
argument-hint: [area-of-interest]
---

Give me a guided tour of this codebase so I can start contributing. Area of
interest (optional): $ARGUMENTS

Explore the repository, then explain:

1. **What it is** — the project's purpose and the problem it solves.
2. **Tech stack** — languages, frameworks, and key dependencies (from the
   manifest and config files).
3. **Layout** — the important directories and what each is responsible for.
4. **Entry points** — where execution starts (main, server bootstrap, CLI, etc.).
5. **Core flow** — trace one representative request/operation end to end.
6. **How to run it** — build, run, and test commands, taken from the actual
   tooling.
7. **Where to start** — 2–3 good first files to read for the area above.

Base everything on files you actually read; reference them with `file:line`.
Prefer concrete pointers over generic description. Do not modify anything.
