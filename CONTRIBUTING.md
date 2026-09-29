# Contributing to codexhowto

Thanks for helping developers master OpenAI Codex CLI. This guide explains how to contribute examples, fixes, and documentation.

## Types of Contributions

- **New examples** — custom prompts, `AGENTS.md` templates, `config.toml` profiles, MCP configs, CI scripts
- **Documentation** — clearer explanations, better diagrams, fixed links
- **Bug fixes** — incorrect commands, outdated behavior, broken examples
- **Translations** — keep the `zh/` mirror in sync, or add a new language tree

## Ground Rules

1. **Teach Codex CLI only.** Do not reference other coding agents by name in lesson content.
2. **Follow the [Style Guide](STYLE_GUIDE.md).** Structure, naming, headings, tables, and diagrams must match.
3. **No secrets.** Never commit real API keys or tokens. Use `OPENAI_API_KEY` and placeholders.
4. **Safe defaults.** Model the tightest approval policy and sandbox mode that still works. Wrap any `--dangerously-bypass-approvals-and-sandbox` example in a **Warning** callout and a container/CI context.
5. **Don't invent facts.** Do not add Codex version numbers, flags, or config keys you cannot verify. Describe behavior without a version claim when unsure.

## Directory Structure

```text
codexhowto/
├── 01-getting-started/     # Each module: README.md + templates
├── 02-slash-commands/
│   └── prompts/            # Custom prompt templates
├── ...
├── 10-cli/
├── zh/                     # Chinese mirror of the English tree
├── README.md               # Main overview
├── INDEX.md                # Complete file index
├── CATALOG.md              # Feature catalog
├── QUICK_REFERENCE.md      # One-page cheat sheet
├── LEARNING-ROADMAP.md     # Guided path
├── STYLE_GUIDE.md          # Formatting conventions
└── AGENTS.md               # Project instructions for Codex
```

## Adding a Module Page

1. Write the module `README.md` following the [lesson structure](STYLE_GUIDE.md#lesson-readme).
2. Add copy-paste templates in the module folder.
3. Update the root `README.md`, `INDEX.md`, `CATALOG.md`, and `LEARNING-ROADMAP.md`.
4. Mirror the change under `zh/`.

## Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/): `type(scope): description`

| Type | Use For |
|------|---------|
| `feat` | New example or guide |
| `fix` | Correction, broken link |
| `docs` | Documentation improvements |
| `refactor` | Restructuring without behavior change |
| `chore` | Build, CI, housekeeping |

The scope is the module name, e.g. `feat(mcp): add GitHub server example`, `docs(config): clarify precedence`.

## Pull Request Process

1. Fork and clone the repository.
2. Create a descriptive branch (`add/mcp-example`, `fix/config-link`).
3. Make your changes following this guide and the Style Guide.
4. Verify all internal links resolve and code fences have language tags.
5. Open a pull request with a clear description of what changed and why.

Need help? Open an issue or discussion.
