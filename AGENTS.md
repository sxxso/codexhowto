# AGENTS.md

Tutorial repo. Output is Markdown in numbered modules `01-` through `10-`, not an app. This file is the project instructions Codex CLI (and other agents) read on startup — it is also a live example of what [Module 03](03-agents-md/) teaches.

## What this project is

- A structured, example-driven guide to **OpenAI Codex CLI** (`@openai/codex`).
- 10 numbered tutorial modules, each with a `README.md` plus copy-paste templates (`.md`, `.toml`, `.sh`, `.yml`).
- An English main tree at the repo root and a Chinese mirror under `zh/`.

## Architecture map

- `01-` … `10-` — tutorial modules. **The numbered prefix is the learning order**, not alphabetical. Do not reorganize.
- Each module: `README.md` + templates users copy into their own project or `~/.codex/`.
- `zh/` — Chinese translation mirroring the English tree file-for-file.
- Top-level docs: `README.md`, `INDEX.md`, `CATALOG.md`, `QUICK_REFERENCE.md`, `LEARNING-ROADMAP.md`, `STYLE_GUIDE.md`.

## Hard rules

- **Do not commit or push without an explicit request.**
- Teach **Codex CLI only** — never reference Claude or other tools by name in lesson content.
- Internal links use **relative paths** (e.g. `03-agents-md/README.md`); anchors use `#heading-name`.
- Code fences **must** declare a language (`bash`, `toml`, `json`, `yaml`, `markdown`, …).
- Mermaid diagrams must parse and should use the shared color palette in `STYLE_GUIDE.md`.
- Do not invent Codex version numbers, flags, or config keys. If unsure, describe the behavior without a version claim.
- Keep the `01-`–`10-` numbering stable — the order is the curriculum.

## Style

- Follow `STYLE_GUIDE.md` for structure, naming, headings, tables, and diagrams.
- Each lesson `README.md`: H1 → overview → Mermaid architecture → detailed sections → 4-6 numbered examples → Do/Don't tables → troubleshooting → related guides → metadata footer.
- Tone: professional but approachable, active voice, copy-paste-ready examples, explain the "why".
- Sentence-case headings; no decorative emojis in lesson bodies.

## Workflow preferences

- Small fixes → minimal diff. Don't rewrite a section to fix a typo.
- When adding a module: write the `README.md` + templates first, then update the root `README.md`, `INDEX.md`, `CATALOG.md`, and `LEARNING-ROADMAP.md` if order/timing changes.
- Keep the `zh/` mirror in sync when English content changes.
- Tutorial > library: prioritize clear explanations and working examples over clever abstractions.

## Metadata footer

Every lesson `README.md` ends with:

```markdown
---

**Last Updated**: September 28, 2026
**Tool**: OpenAI Codex CLI (`@openai/codex`)
**Compatible Models**: GPT-5-Codex (default), GPT-5, plus OpenAI-compatible and local (OSS) models
*Part of the [codexhowto](../) guide series*
```
