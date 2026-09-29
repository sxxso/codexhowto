# Style Guide

> Conventions and formatting rules for contributing to codexhowto. Follow this guide to keep content consistent, professional, and easy to maintain.

---

## Table of Contents

- [File and Folder Naming](#file-and-folder-naming)
- [Document Structure](#document-structure)
- [Headings](#headings)
- [Text Formatting](#text-formatting)
- [Tables](#tables)
- [Code Blocks](#code-blocks)
- [Links and Cross-References](#links-and-cross-references)
- [Diagrams](#diagrams)
- [Vocabulary](#vocabulary)
- [Metadata Footer](#metadata-footer)
- [Checklist for Authors](#checklist-for-authors)

---

## File and Folder Naming

### Lesson Folders

Lesson folders use a **two-digit numbered prefix** followed by a **kebab-case** descriptor. The number reflects the learning path order from beginner to advanced:

```text
01-getting-started/
02-slash-commands/
03-agents-md/
04-config/
05-approvals-sandbox/
```

### File Names

| Type | Convention | Examples |
|------|-----------|----------|
| **Lesson README** | `README.md` | `05-approvals-sandbox/README.md` |
| **Prompt template** | Kebab-case `.md` | `review.md`, `commit.md` |
| **Config template** | Descriptive `.toml` | `config.toml`, `profiles-config.toml` |
| **Script** | Kebab-case `.sh`/`.yml` | `review-diff.sh`, `codex-review.yml` |
| **Memory template** | Scope-prefixed | `project-AGENTS.md`, `personal-AGENTS.md` |
| **Top-level docs** | UPPER_CASE `.md` | `CATALOG.md`, `QUICK_REFERENCE.md` |

### Rules

- Use **lowercase** for file and folder names (except top-level docs like `README.md`, `CATALOG.md`).
- Use **hyphens** (`-`) as word separators, never underscores or spaces.
- Keep names descriptive but concise.

---

## Document Structure

### Lesson README

Each lesson `README.md` follows this order:

1. H1 title (e.g., `# Approvals & Sandboxing`)
2. Brief overview paragraph
3. Architecture diagram (Mermaid)
4. Detailed sections (H2)
5. Practical examples (numbered, 4-6 examples)
6. Best practices (Do's and Don'ts tables)
7. Troubleshooting
8. Related guides
9. Metadata footer

Use horizontal rules (`---`) to separate major regions.

---

## Headings

| Level | Use | Example |
|-------|-----|---------|
| `#` H1 | Page title (one per document) | `# Configuration` |
| `##` H2 | Major sections | `## Best Practices` |
| `###` H3 | Subsections | `### Adding a profile` |

- **One H1 per document.**
- **Never skip levels.**
- **Use sentence case** — capitalize the first word and proper nouns only (feature and command names stay as-is).
- No decorative emojis in lesson headers or body.

---

## Text Formatting

| Style | When to Use | Example |
|-------|------------|---------|
| **Bold** | Key terms, table row labels | `**Installation**:` |
| *Italic* | First use of a technical term | `*frontmatter*` |
| `Code` | File names, commands, config keys, values | `` `config.toml` `` |

Use blockquote callouts with bold prefixes: **Note**, **Important**, **Tip**, **Warning**.

```markdown
> **Warning**: `--dangerously-bypass-approvals-and-sandbox` disables all safety. Use it only in disposable containers.
```

---

## Tables

- **Bold the first column** when it is a row label.
- Keep cell content concise; use `code formatting` for commands and paths.
- Prefer tables for command references, flag lists, and Do/Don't comparisons.

---

## Code Blocks

Always specify a language tag:

| Language | Tag | Use For |
|----------|-----|---------|
| Shell | `bash` | CLI commands, scripts |
| TOML | `toml` | `config.toml` snippets |
| JSON | `json` | JSON payloads |
| YAML | `yaml` | CI workflows, frontmatter |
| Markdown | `markdown` | Markdown examples, prompts |
| Plain text | `text` | Directory trees, expected output |

- Add a comment line before non-obvious commands.
- Make every example copy-paste ready.

---

## Links and Cross-References

Use relative paths for internal links:

```markdown
[Approvals & Sandbox](05-approvals-sandbox/)
[Config precedence](04-config/#precedence)
[Back to main guide](../README.md)
```

Use full URLs with descriptive anchor text for external links. Never use "click here".

End every lesson with a **Related guides** section linking to relevant sibling modules.

---

## Diagrams

Use Mermaid for all diagrams (`graph TB`/`graph LR`, `sequenceDiagram`, `flowchart`).

**Color palette:**

| Color | Hex | Use For |
|-------|-----|---------|
| Light blue | `#e1f5fe` | Primary components, inputs |
| Light pink | `#fce4ec` | Processing, middleware |
| Light green | `#e8f5e9` | Outputs, results |
| Light yellow | `#fff9c4` | Configuration, optional |
| Light purple | `#f3e5f5` | User-facing, UI |

Rules:

- Use `["Label text"]` for node labels (enables special characters).
- Keep diagrams simple (max 10-12 nodes).
- Add a one-line text description below each diagram for accessibility.

---

## Vocabulary

- Use **"Codex CLI"** or **"Codex"** (not "the tool", "OpenAI CLI").
- Use **"AGENTS.md"** for project memory/instructions.
- Use **"custom prompt"** for user-defined slash commands in `~/.codex/prompts/`.
- Use **"approval policy"** and **"sandbox mode"** as two distinct axes.
- Use **"lesson"** or **"module"** for the numbered sections, **"example"** for individual template files.
- Never reference other coding agents by name in lesson content.

---

## Metadata Footer

Lesson READMEs end with:

```markdown
---

**Last Updated**: September 28, 2026
**Tool**: OpenAI Codex CLI (`@openai/codex`)
**Compatible Models**: GPT-5-Codex (default), GPT-5, plus OpenAI-compatible and local (OSS) models
*Part of the [codexhowto](../) guide series*
```

---

## Checklist for Authors

- [ ] File/folder names use kebab-case
- [ ] Document starts with one H1 title
- [ ] Heading hierarchy is correct (no skipped levels)
- [ ] All code blocks have language tags
- [ ] Code examples are copy-paste ready
- [ ] Internal links use relative paths
- [ ] Tables are properly formatted
- [ ] Mermaid diagrams use the standard color palette and parse
- [ ] No sensitive information (API keys, credentials)
- [ ] No references to other coding agents
- [ ] Related guides section links to relevant modules
- [ ] Metadata footer is present and current

---

**Last Updated**: September 28, 2026
**Tool**: OpenAI Codex CLI (`@openai/codex`)
**Compatible Models**: GPT-5-Codex (default), GPT-5, plus OpenAI-compatible and local (OSS) models
