# codexhowto — Complete Index

A complete index of every file in the guide, organized by module. For the guided order, see the [Learning Roadmap](LEARNING-ROADMAP.md); for feature-by-feature usage, see the [Catalog](CATALOG.md).

## Summary

- **13 tutorial modules** (`01-` … `13-`) plus a hands-on lab (`exercises/`)
- **Copy-paste templates**: custom prompts, `AGENTS.md` files, `config.toml` examples, MCP configs, profiles, CI scripts, a prompt library
- **Chinese mirror** under `zh/`

---

## 01. Getting Started

| File | Description |
|------|-------------|
| `01-getting-started/README.md` | Install, login, first session, TUI basics |

## 02. Slash Commands & Custom Prompts

| File | Description |
|------|-------------|
| `02-slash-commands/README.md` | Built-in commands + custom prompts guide |
| `02-slash-commands/prompts/review.md` | Code-review custom prompt |
| `02-slash-commands/prompts/commit.md` | Conventional-commit message prompt |
| `02-slash-commands/prompts/explain.md` | Explain-a-file prompt (`$1`) |

**Install**: copy into `~/.codex/prompts/`

## 03. AGENTS.md

| File | Description | Location |
|------|-------------|----------|
| `03-agents-md/README.md` | Memory & instructions guide | — |
| `03-agents-md/project-AGENTS.md` | Repo-root template | `./AGENTS.md` |
| `03-agents-md/personal-AGENTS.md` | Global personal template | `~/.codex/AGENTS.md` |
| `03-agents-md/nested-AGENTS.md` | Subdirectory template | `./src/api/AGENTS.md` |

## 04. Configuration

| File | Description |
|------|-------------|
| `04-config/README.md` | `config.toml` reference & precedence |
| `04-config/config.toml` | Well-commented starter config |
| `04-config/config-minimal.toml` | Minimal safe config |
| `04-config/config-power-user.toml` | Advanced multi-profile config |

**Install**: copy to `~/.codex/config.toml`

## 05. Approvals & Sandboxing

| File | Description |
|------|-------------|
| `05-approvals-sandbox/README.md` | Approval policy × sandbox mode, presets, platform notes |

## 06. MCP (Model Context Protocol)

| File | Description |
|------|-------------|
| `06-mcp/README.md` | MCP client/server guide |
| `06-mcp/filesystem-mcp.toml` | Filesystem server snippet |
| `06-mcp/github-mcp.toml` | GitHub server snippet |
| `06-mcp/multi-mcp.toml` | Multiple servers together |

## 07. Automation & CI

| File | Description |
|------|-------------|
| `07-automation/README.md` | Headless `codex exec`, CI, scripting |
| `07-automation/scripts/review-diff.sh` | Pipe `git diff` into review |
| `07-automation/scripts/batch-docstrings.sh` | Batch docstring updates |
| `07-automation/scripts/codex-review.yml` | GitHub Actions PR review |

## 08. Profiles & Model Providers

| File | Description |
|------|-------------|
| `08-profiles/README.md` | Profiles + model providers + `--oss` |
| `08-profiles/profiles-config.toml` | Fast/deep/readonly/local profiles |

## 09. Advanced Features

| File | Description |
|------|-------------|
| `09-advanced/README.md` | Sessions, notify, web search, images, IDE, cloud |
| `09-advanced/notify.sh` | Example `notify` hook script |

## 10. CLI Reference

| File | Description |
|------|-------------|
| `10-cli/README.md` | Full command, flag, config, and env reference |

## 11. Recipes & Workflows

| File | Description |
|------|-------------|
| `11-recipes/README.md` | End-to-end playbooks combining features |
| `11-recipes/scripts/onboarding-tour.sh` | Read-only repo tour |
| `11-recipes/scripts/codemod-plan-then-apply.sh` | Two-phase plan → apply codemod |

## 12. Decision Guides

| File | Description |
|------|-------------|
| `12-decision-guides/README.md` | Flowcharts for approvals, exec vs TUI, model choice, instruction placement, MCP, profiles |

## 13. Prompt Library

| File | Description |
|------|-------------|
| `13-prompt-library/README.md` | Catalog of 14 ready-to-use custom prompts |
| `13-prompt-library/prompts/*.md` | Review, debug, refactor, testing, git, docs, exploration prompts |

**Install**: copy into `~/.codex/prompts/`

## Hands-on Lab

| File | Description |
|------|-------------|
| `exercises/README.md` | Guided lab: fix a broken project with Codex |
| `exercises/SOLUTIONS.md` | Reference answers |
| `exercises/sample-project/` | Runnable Python project with planted bugs |

---

## Top-Level Documentation

| File | Description |
|------|-------------|
| `README.md` | Main overview |
| `INDEX.md` | This index |
| `CATALOG.md` | Feature catalog |
| `QUICK_REFERENCE.md` | One-page cheat sheet |
| `LEARNING-ROADMAP.md` | Guided path |
| `STYLE_GUIDE.md` | Formatting conventions |
| `AGENTS.md` | Project instructions for Codex |
| `CONTRIBUTING.md` | How to contribute |
| `SECURITY.md` | Safe-template policy |
| `CODE_OF_CONDUCT.md` | Community standards |
| `CHANGELOG.md` | Release history |
| `LICENSE` | MIT license |

---

## File Tree

```text
codexhowto/
├── README.md
├── INDEX.md
├── CATALOG.md
├── QUICK_REFERENCE.md
├── LEARNING-ROADMAP.md
├── STYLE_GUIDE.md
├── AGENTS.md
├── CONTRIBUTING.md
├── SECURITY.md
├── CODE_OF_CONDUCT.md
├── CHANGELOG.md
├── LICENSE
├── 01-getting-started/
│   └── README.md
├── 02-slash-commands/
│   ├── README.md
│   └── prompts/
│       ├── review.md
│       ├── commit.md
│       └── explain.md
├── 03-agents-md/
│   ├── README.md
│   ├── project-AGENTS.md
│   ├── personal-AGENTS.md
│   └── nested-AGENTS.md
├── 04-config/
│   ├── README.md
│   ├── config.toml
│   ├── config-minimal.toml
│   └── config-power-user.toml
├── 05-approvals-sandbox/
│   └── README.md
├── 06-mcp/
│   ├── README.md
│   ├── filesystem-mcp.toml
│   ├── github-mcp.toml
│   └── multi-mcp.toml
├── 07-automation/
│   ├── README.md
│   └── scripts/
│       ├── review-diff.sh
│       ├── batch-docstrings.sh
│       └── codex-review.yml
├── 08-profiles/
│   ├── README.md
│   └── profiles-config.toml
├── 09-advanced/
│   ├── README.md
│   └── notify.sh
├── 10-cli/
│   └── README.md
├── 11-recipes/
│   ├── README.md
│   └── scripts/
│       ├── onboarding-tour.sh
│       └── codemod-plan-then-apply.sh
├── 12-decision-guides/
│   └── README.md
├── 13-prompt-library/
│   ├── README.md
│   └── prompts/           # 14 custom prompts
├── exercises/
│   ├── README.md
│   ├── SOLUTIONS.md
│   └── sample-project/    # runnable Python project with planted bugs
└── zh/                     # Chinese mirror
```

---

**Last Updated**: September 28, 2026
**Tool**: OpenAI Codex CLI (`@openai/codex`)
**Compatible Models**: GPT-5-Codex (default), GPT-5, plus OpenAI-compatible and local (OSS) models
