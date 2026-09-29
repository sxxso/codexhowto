# Feature Catalog

A complete reference of every Codex CLI feature covered in codexhowto, with what it is, where to put it, and how to use it. For the guided order, see the [Learning Roadmap](LEARNING-ROADMAP.md).

---

## 01. Getting Started

**What**: Install, authenticate, and run your first Codex session.

```bash
npm install -g @openai/codex
codex login
codex "give me a tour of this codebase"
```

**Learn**: [01-getting-started/](01-getting-started/)

---

## 02. Slash Commands & Custom Prompts

**What**: Built-in `/` commands plus reusable custom prompts you define as Markdown files.

**Location**: `~/.codex/prompts/<name>.md` → `/name`

```bash
mkdir -p ~/.codex/prompts
cp 02-slash-commands/prompts/*.md ~/.codex/prompts/
```

**Templates**: `review.md`, `commit.md`, `explain.md`

**Learn**: [02-slash-commands/](02-slash-commands/)

---

## 03. AGENTS.md — Memory & Instructions

**What**: Markdown instructions Codex reads on startup — build/test commands, conventions, do/don't.

**Locations** (merged, most-specific wins): `~/.codex/AGENTS.md` → repo-root `AGENTS.md` → nested `AGENTS.md`

```bash
cp 03-agents-md/project-AGENTS.md ./AGENTS.md
# or scaffold one inside the TUI:
codex
/init
```

**Templates**: `project-AGENTS.md`, `personal-AGENTS.md`, `nested-AGENTS.md`

**Learn**: [03-agents-md/](03-agents-md/)

---

## 04. Configuration (config.toml)

**What**: Central settings — model, reasoning effort, approval policy, sandbox mode, profiles.

**Location**: `~/.codex/config.toml`

```bash
mkdir -p ~/.codex
cp 04-config/config.toml ~/.codex/config.toml
```

**Templates**: `config.toml`, `config-minimal.toml`, `config-power-user.toml`

**Learn**: [04-config/](04-config/)

---

## 05. Approvals & Sandboxing

**What**: The safety model — two axes: **when Codex asks** (approval policy) and **what it can do** (sandbox mode).

| Approval | Sandbox |
|----------|---------|
| `untrusted`, `on-failure`, `on-request`, `never` | `read-only`, `workspace-write`, `danger-full-access` |

```bash
codex -a on-request -s workspace-write "add tests"
```

**Learn**: [05-approvals-sandbox/](05-approvals-sandbox/)

---

## 06. MCP (Model Context Protocol)

**What**: Connect external tools and data sources as MCP servers Codex can call.

**Location**: `[mcp_servers.<name>]` in `config.toml`

**Templates**: `filesystem-mcp.toml`, `github-mcp.toml`, `multi-mcp.toml`

**Learn**: [06-mcp/](06-mcp/)

---

## 07. Automation & CI (codex exec)

**What**: Headless, non-interactive Codex for scripts and CI pipelines.

```bash
git diff | codex exec "review this diff"
codex exec --json "summarize test failures"
```

**Templates**: `scripts/review-diff.sh`, `scripts/batch-docstrings.sh`, `scripts/codex-review.yml`

**Learn**: [07-automation/](07-automation/)

---

## 08. Profiles & Model Providers

**What**: Named bundles of settings, and custom / OpenAI-compatible / local model providers.

```bash
codex --profile deep "design the caching layer"
codex --oss -m gpt-oss "refactor offline"
```

**Templates**: `profiles-config.toml`

**Learn**: [08-profiles/](08-profiles/)

---

## 09. Advanced Features

**What**: Sessions & resume, the `notify` hook, web search, image input, reasoning effort, IDE extension, Codex Cloud, GitHub review, MCP server mode.

**Templates**: `notify.sh`

**Learn**: [09-advanced/](09-advanced/)

---

## 10. CLI Reference

**What**: Every subcommand, flag, config key, and environment variable in one place.

**Learn**: [10-cli/](10-cli/)

---

## 11. Recipes & Workflows

**What**: End-to-end playbooks that combine features into real workflows — onboarding, TDD, CI review, codemods, debugging, bulk docstrings, log triage.

```bash
codex -a on-request -s read-only "map this repo's architecture"
```

**Templates**: `scripts/onboarding-tour.sh`, `scripts/codemod-plan-then-apply.sh`

**Learn**: [11-recipes/](11-recipes/)

---

## 12. Decision Guides

**What**: Flowcharts and decision tables for the choices that trip people up — approval/sandbox pairs, `codex exec` vs TUI, model + reasoning effort, where an instruction belongs, MCP vs shell, which profile.

**Learn**: [12-decision-guides/](12-decision-guides/)

---

## 13. Prompt Library

**What**: A catalog of 14 ready-to-use custom prompts across review, debugging, refactoring, testing, git, docs, and exploration.

```bash
cp 13-prompt-library/prompts/*.md ~/.codex/prompts/
```

**Learn**: [13-prompt-library/](13-prompt-library/)

---

## Hands-on Lab

**What**: A runnable, deliberately broken Python project you repair with Codex — guided exercises plus reference solutions. Turns the reference modules into practice.

```bash
cd exercises/sample-project && pytest -q   # 2 failing on purpose
```

**Learn**: [exercises/](exercises/)

---

## Feature Comparison

| Feature | Where it lives | Persistence | Best for |
|---------|---------------|-------------|----------|
| **Custom prompts** | `~/.codex/prompts/` | Filesystem | Reusable shortcuts |
| **AGENTS.md** | Project + home | Cross-session | Conventions & context |
| **config.toml** | `~/.codex/` | Cross-session | Defaults & profiles |
| **Approvals/Sandbox** | Flags + config | Per-session | Safe autonomy |
| **MCP** | config.toml | Real-time | External tools/data |
| **codex exec** | Terminal/CI | Per-run | Automation |
| **Profiles** | config.toml | Cross-session | Multi-model workflows |

---

**Last Updated**: September 28, 2026
**Tool**: OpenAI Codex CLI (`@openai/codex`)
**Compatible Models**: GPT-5-Codex (default), GPT-5, plus OpenAI-compatible and local (OSS) models
