---
description: Draft or refresh the project README
argument-hint: [audience]
---

Draft (or update) this project's `README.md`. Intended audience: $ARGUMENTS
(default to developers who are new to the project).

First, understand the project: read the package/manifest file, entry points, and
directory layout so the README reflects reality — not assumptions.

Produce a README with these sections, skipping any that do not apply:

1. **Title & one-line description** — what it is.
2. **Features / what it does** — the key capabilities.
3. **Installation** — the actual steps, derived from the project's tooling.
4. **Usage** — a minimal working example, plus common commands.
5. **Configuration** — important options/env vars, if any.
6. **Development** — how to build, test, and contribute.
7. **License** — from the existing license file, if present.

Use real commands and paths from this repo. Do not invent installation steps,
badges, or features that do not exist. If a README already exists, improve it in
place rather than discarding accurate content.
