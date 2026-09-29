# 更新记录

本文件记录 codexhowto 的所有重要变更。

格式参考 [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)。

## [1.2.0] - 2026-09-29

### 新增

- **Verify 工作流**(`.github/workflows/verify.yml`)—— 每次 push 和 pull request 都会运行的 CI:
  - 断言动手实验在英文和 `zh/` 两份示例项目中都保持预期的 `2 failed, 3 passed` 基线,这样一旦有人悄悄「修好」了埋的 bug,构建就会失败。
  - 对每个 Markdown 文件运行相对链接检查(`.github/scripts/check_links.py`)。
- **Verify 状态徽章**以及 `README.md`(英文 + `zh/`)中的「本仓库如何验证」表格,明确说明哪些是自动检查的,以及 Codex CLI 命令并未针对某个特定版本做认证。
- **「真实会话长什么样」**—— 在实验 `README.md`(英文 + `zh/`)中为练习 3 加入一段节选、示意性的 `codex` 会话记录。
- **GitHub 模板** —— issue 模板(命令报错、内容修正、新增内容)与 pull request 模板,与 `CONTRIBUTING.md` 和 `STYLE_GUIDE.md` 对齐。
- **中文镜像**:补齐其余顶层文档 `zh/CHANGELOG.md`、`zh/CODE_OF_CONDUCT.md`、`zh/SECURITY.md`、`zh/STYLE_GUIDE.md`。

## [1.1.0] - 2026-09-29

### 新增

- 应用层 —— 三个把参考材料转化为实践的新模块:
  - 11 Recipes 与工作流(端到端剧本 + `onboarding-tour.sh`、`codemod-plan-then-apply.sh`)
  - 12 决策指南(针对审批/沙箱、exec vs TUI、模型 + 推理强度、指令存放位置、MCP vs shell、profile 的 Mermaid 流程图 + 表格)
  - 13 提示词库(覆盖审查、调试、重构、测试、git、文档、探索的 14 个开箱即用自定义提示词)
- `exercises/` 下的动手实验 —— 一个可运行、故意写坏的 Python 项目(`sample-project/`),埋有 bug,配有引导式 `README.md` 和 `SOLUTIONS.md`。
- 以上全部内容的中文镜像,位于 `zh/`。
- 更新 `README.md`、`INDEX.md`、`CATALOG.md`、`LEARNING-ROADMAP.md` 和 `QUICK_REFERENCE.md`(英文 + `zh/`),列出新模块和实验。

## [1.0.0] - 2026-09-28

### 新增

- 首个版本,包含 10 个讲解 OpenAI Codex CLI 的教程模块:
  - 01 入门(安装、登录、首次会话)
  - 02 斜杠命令与自定义提示词
  - 03 AGENTS.md(记忆与指令)
  - 04 配置(`config.toml`)
  - 05 审批与沙箱
  - 06 MCP(Model Context Protocol)
  - 07 自动化与 CI(`codex exec`)
  - 08 Profile 与模型提供方
  - 09 进阶功能
  - 10 CLI 参考
- 顶层文档:`README.md`、`INDEX.md`、`CATALOG.md`、`QUICK_REFERENCE.md`、`LEARNING-ROADMAP.md`、`STYLE_GUIDE.md`、`AGENTS.md`。
- 可复制的模板:自定义提示词、`AGENTS.md` 文件、`config.toml` 示例、MCP 配置、profile 和 CI 脚本。
- `zh/` 下的中文翻译。
