# codexhowto —— 完整索引

本指南每个文件的完整索引,按模块组织。想看引导顺序,见[学习路线图](LEARNING-ROADMAP.md);想按功能逐项了解用法,见[目录](CATALOG.md)。

## 概要

- **13 个教程模块**(`01-` … `13-`),外加一套动手实验(`exercises/`)
- **可复制粘贴的模板**:自定义 prompt、`AGENTS.md` 文件、`config.toml` 示例、MCP 配置、profile、CI 脚本、提示词库
- **中文镜像**位于 `zh/`

---

## 01. 入门

| 文件 | 说明 |
|------|------|
| `01-getting-started/README.md` | 安装、登录、首次会话、TUI 基础 |

## 02. Slash 命令与自定义 prompt

| 文件 | 说明 |
|------|------|
| `02-slash-commands/README.md` | 内置命令 + 自定义 prompt 指南 |
| `02-slash-commands/prompts/review.md` | 代码审查自定义 prompt |
| `02-slash-commands/prompts/commit.md` | Conventional-commit 信息 prompt |
| `02-slash-commands/prompts/explain.md` | 解释文件的 prompt(`$1`) |

**安装**:复制到 `~/.codex/prompts/`

## 03. AGENTS.md

| 文件 | 说明 | 位置 |
|------|------|------|
| `03-agents-md/README.md` | 记忆与说明指南 | — |
| `03-agents-md/project-AGENTS.md` | 仓库根模板 | `./AGENTS.md` |
| `03-agents-md/personal-AGENTS.md` | 全局个人模板 | `~/.codex/AGENTS.md` |
| `03-agents-md/nested-AGENTS.md` | 子目录模板 | `./src/api/AGENTS.md` |

## 04. 配置

| 文件 | 说明 |
|------|------|
| `04-config/README.md` | `config.toml` 参考与优先级 |
| `04-config/config.toml` | 带注释的起步配置 |
| `04-config/config-minimal.toml` | 最小安全配置 |
| `04-config/config-power-user.toml` | 进阶多 profile 配置 |

**安装**:复制到 `~/.codex/config.toml`

## 05. 审批与沙箱

| 文件 | 说明 |
|------|------|
| `05-approvals-sandbox/README.md` | 审批策略 × 沙箱模式、预设、平台说明 |

## 06. MCP(模型上下文协议)

| 文件 | 说明 |
|------|------|
| `06-mcp/README.md` | MCP 客户端/服务端指南 |
| `06-mcp/filesystem-mcp.toml` | 文件系统 server 片段 |
| `06-mcp/github-mcp.toml` | GitHub server 片段 |
| `06-mcp/multi-mcp.toml` | 多 server 一起配置 |

## 07. 自动化与 CI

| 文件 | 说明 |
|------|------|
| `07-automation/README.md` | 无头 `codex exec`、CI、脚本化 |
| `07-automation/scripts/review-diff.sh` | 把 `git diff` 管道进审查 |
| `07-automation/scripts/batch-docstrings.sh` | 批量更新 docstring |
| `07-automation/scripts/codex-review.yml` | GitHub Actions PR 审查 |

## 08. Profile 与模型提供方

| 文件 | 说明 |
|------|------|
| `08-profiles/README.md` | Profile + 模型提供方 + `--oss` |
| `08-profiles/profiles-config.toml` | fast/deep/readonly/local profile |

## 09. 进阶功能

| 文件 | 说明 |
|------|------|
| `09-advanced/README.md` | 会话、notify、联网搜索、图片、IDE、云 |
| `09-advanced/notify.sh` | 示例 `notify` 钩子脚本 |

## 10. CLI 参考

| 文件 | 说明 |
|------|------|
| `10-cli/README.md` | 完整的命令、flag、配置和环境变量参考 |

## 11. 实战手册与工作流

| 文件 | 说明 |
|------|------|
| `11-recipes/README.md` | 组合各功能的端到端剧本 |
| `11-recipes/scripts/onboarding-tour.sh` | 只读的仓库巡览 |
| `11-recipes/scripts/codemod-plan-then-apply.sh` | 两阶段:先规划 → 再应用的批量改代码 |

## 12. 决策指南

| 文件 | 说明 |
|------|------|
| `12-decision-guides/README.md` | 审批、exec vs TUI、模型选择、指令归属、MCP、profile 的决策流程图 |

## 13. 提示词库

| 文件 | 说明 |
|------|------|
| `13-prompt-library/README.md` | 14 个开箱即用自定义 prompt 的目录 |
| `13-prompt-library/prompts/*.md` | 审查、调试、重构、测试、git、文档、探索类 prompt |

**安装**:复制到 `~/.codex/prompts/`

## 动手实验

| 文件 | 说明 |
|------|------|
| `exercises/README.md` | 引导式实验:用 Codex 修好一个破项目 |
| `exercises/SOLUTIONS.md` | 参考答案 |
| `exercises/sample-project/` | 埋了 bug 的可运行 Python 项目 |

---

## 顶层文档

| 文件 | 说明 |
|------|------|
| `README.md` | 主概览 |
| `INDEX.md` | 本索引 |
| `CATALOG.md` | 功能目录 |
| `QUICK_REFERENCE.md` | 一页速查表 |
| `LEARNING-ROADMAP.md` | 引导式路径 |
| `../STYLE_GUIDE.md` | 格式规范(英文) |
| `AGENTS.md` | 给 Codex 的项目说明 |
| `CONTRIBUTING.md` | 如何贡献 |
| `../SECURITY.md` | 安全模板政策(英文) |
| `../CODE_OF_CONDUCT.md` | 社区准则(英文) |
| `../CHANGELOG.md` | 发布历史(英文) |
| `../LICENSE` | MIT 许可证 |

---

## 文件树

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
│   └── prompts/           # 14 个自定义 prompt
├── exercises/
│   ├── README.md
│   ├── SOLUTIONS.md
│   └── sample-project/    # 埋了 bug 的可运行 Python 项目
└── zh/                     # 中文镜像
```

---

**最后更新**: September 28, 2026
**工具**: OpenAI Codex CLI (`@openai/codex`)
**兼容模型**: GPT-5-Codex (默认), GPT-5, 以及 OpenAI 兼容和本地 (OSS) 模型
