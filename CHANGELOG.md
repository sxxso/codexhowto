# Changelog

All notable changes to codexhowto are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [1.2.0] - 2026-09-29

### Added

- **Verify workflow** (`.github/workflows/verify.yml`) — CI that runs on every push and pull request:
  - Asserts the hands-on lab keeps its intended `2 failed, 3 passed` baseline in both the EN and `zh/` sample projects, so a silently "fixed" planted bug fails the build.
  - Runs a relative-link checker (`.github/scripts/check_links.py`) across every Markdown file.
- **Verify status badge** and a "How this repo is verified" table in `README.md` (EN + `zh/`), stating plainly what is automated and that Codex CLI commands are not certified against a specific release.
- **"What a real session looks like"** — an abbreviated, representative `codex` transcript for Exercise 3 in the lab `README.md` (EN + `zh/`).
- **GitHub templates** — issue templates (broken command, content fix, new content) and a pull request template aligned with `CONTRIBUTING.md` and `STYLE_GUIDE.md`.
- **Chinese mirrors** of the remaining top-level docs: `zh/CHANGELOG.md`, `zh/CODE_OF_CONDUCT.md`, `zh/SECURITY.md`, `zh/STYLE_GUIDE.md`.

## [1.1.0] - 2026-09-29

### Added

- Applied tier — three new modules that turn the reference material into practice:
  - 11 Recipes & Workflows (end-to-end playbooks + `onboarding-tour.sh`, `codemod-plan-then-apply.sh`)
  - 12 Decision Guides (Mermaid flowcharts + tables for approvals/sandbox, exec vs TUI, model + reasoning effort, instruction placement, MCP vs shell, profiles)
  - 13 Prompt Library (14 ready-to-use custom prompts across review, debug, refactor, testing, git, docs, exploration)
- Hands-on lab under `exercises/` — a runnable, deliberately broken Python project (`sample-project/`) with planted bugs, a guided `README.md`, and `SOLUTIONS.md`.
- Chinese mirror for all of the above under `zh/`.
- Updated `README.md`, `INDEX.md`, `CATALOG.md`, `LEARNING-ROADMAP.md`, and `QUICK_REFERENCE.md` (EN + `zh/`) to list the new modules and lab.

## [1.0.0] - 2026-09-28

### Added

- Initial release with 10 tutorial modules covering OpenAI Codex CLI:
  - 01 Getting Started (install, login, first session)
  - 02 Slash Commands & Custom Prompts
  - 03 AGENTS.md (memory & instructions)
  - 04 Configuration (`config.toml`)
  - 05 Approvals & Sandboxing
  - 06 MCP (Model Context Protocol)
  - 07 Automation & CI (`codex exec`)
  - 08 Profiles & Model Providers
  - 09 Advanced Features
  - 10 CLI Reference
- Top-level docs: `README.md`, `INDEX.md`, `CATALOG.md`, `QUICK_REFERENCE.md`, `LEARNING-ROADMAP.md`, `STYLE_GUIDE.md`, `AGENTS.md`.
- Copy-paste templates: custom prompts, `AGENTS.md` files, `config.toml` examples, MCP configs, profiles, and CI scripts.
- Chinese translation under `zh/`.
