# Changelog

All notable changes to codexhowto are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

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
