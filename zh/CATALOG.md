# 功能目录

codexhowto 覆盖的每个 Codex CLI 功能的完整参考:它是什么、放在哪里、怎么用。想看引导顺序,见[学习路线图](LEARNING-ROADMAP.md)。

---

## 01. 入门

**是什么**:安装、认证,并运行你的第一个 Codex 会话。

```bash
npm install -g @openai/codex
codex login
codex "give me a tour of this codebase"
```

**学习**:[01-getting-started/](01-getting-started/)

---

## 02. Slash 命令与自定义 prompt

**是什么**:内置 `/` 命令,外加你以 Markdown 文件定义的可复用自定义 prompt。

**位置**:`~/.codex/prompts/<name>.md` → `/name`

```bash
mkdir -p ~/.codex/prompts
cp 02-slash-commands/prompts/*.md ~/.codex/prompts/
```

**模板**:`review.md`、`commit.md`、`explain.md`

**学习**:[02-slash-commands/](02-slash-commands/)

---

## 03. AGENTS.md —— 记忆与说明

**是什么**:Codex 启动时读取的 Markdown 说明——构建/测试命令、约定、do/don't。

**位置**(合并,最具体者优先):`~/.codex/AGENTS.md` → 仓库根 `AGENTS.md` → 嵌套 `AGENTS.md`

```bash
cp 03-agents-md/project-AGENTS.md ./AGENTS.md
# 或在 TUI 内脚手架生成一个:
codex
/init
```

**模板**:`project-AGENTS.md`、`personal-AGENTS.md`、`nested-AGENTS.md`

**学习**:[03-agents-md/](03-agents-md/)

---

## 04. 配置 (config.toml)

**是什么**:核心设置——模型、推理强度、审批策略、沙箱模式、profile。

**位置**:`~/.codex/config.toml`

```bash
mkdir -p ~/.codex
cp 04-config/config.toml ~/.codex/config.toml
```

**模板**:`config.toml`、`config-minimal.toml`、`config-power-user.toml`

**学习**:[04-config/](04-config/)

---

## 05. 审批与沙箱

**是什么**:安全模型——两个维度:**Codex 何时询问**(审批策略)和**它能做什么**(沙箱模式)。

| 审批策略 | 沙箱模式 |
|----------|---------|
| `untrusted`、`on-failure`、`on-request`、`never` | `read-only`、`workspace-write`、`danger-full-access` |

```bash
codex -a on-request -s workspace-write "add tests"
```

**学习**:[05-approvals-sandbox/](05-approvals-sandbox/)

---

## 06. MCP(模型上下文协议)

**是什么**:把外部工具和数据源接入为 Codex 可调用的 MCP server。

**位置**:`config.toml` 中的 `[mcp_servers.<name>]`

**模板**:`filesystem-mcp.toml`、`github-mcp.toml`、`multi-mcp.toml`

**学习**:[06-mcp/](06-mcp/)

---

## 07. 自动化与 CI (codex exec)

**是什么**:面向脚本和 CI 流水线的无头、非交互 Codex。

```bash
git diff | codex exec "review this diff"
codex exec --json "summarize test failures"
```

**模板**:`scripts/review-diff.sh`、`scripts/batch-docstrings.sh`、`scripts/codex-review.yml`

**学习**:[07-automation/](07-automation/)

---

## 08. Profile 与模型提供方

**是什么**:命名的设置组合,以及自定义 / OpenAI 兼容 / 本地模型提供方。

```bash
codex --profile deep "design the caching layer"
codex --oss -m gpt-oss "refactor offline"
```

**模板**:`profiles-config.toml`

**学习**:[08-profiles/](08-profiles/)

---

## 09. 进阶功能

**是什么**:会话与恢复、`notify` 钩子、联网搜索、图片输入、推理强度、IDE 扩展、Codex Cloud、GitHub 审查、MCP server 模式。

**模板**:`notify.sh`

**学习**:[09-advanced/](09-advanced/)

---

## 10. CLI 参考

**是什么**:所有子命令、flag、配置键和环境变量,汇于一处。

**学习**:[10-cli/](10-cli/)

---

## 11. 实战手册与工作流

**是什么**:把各功能组合成真实工作流的端到端剧本——上手新仓库、TDD、CI 审查、批量改代码、调试、批量 docstring、日志排查。

```bash
codex -a on-request -s read-only "map this repo's architecture"
```

**模板**:`scripts/onboarding-tour.sh`、`scripts/codemod-plan-then-apply.sh`

**学习**:[11-recipes/](11-recipes/)

---

## 12. 决策指南

**是什么**:针对易错抉择的流程图与决策表——审批/沙箱组合、`codex exec` vs TUI、模型 + 推理强度、指令该放哪、MCP vs shell、用哪个 profile。

**学习**:[12-decision-guides/](12-decision-guides/)

---

## 13. 提示词库

**是什么**:14 个开箱即用的自定义 prompt 目录,覆盖审查、调试、重构、测试、git、文档和探索。

```bash
cp 13-prompt-library/prompts/*.md ~/.codex/prompts/
```

**学习**:[13-prompt-library/](13-prompt-library/)

---

## 动手实验

**是什么**:一个可运行、故意做坏的 Python 项目,让你用 Codex 修好它——分步练习加参考答案。把参考模块变成真正的实践。

```bash
cd exercises/sample-project && pytest -q   # 2 个故意失败
```

**学习**:[exercises/](exercises/)

---

## 功能对比

| 功能 | 存放位置 | 持久性 | 最适合 |
|------|---------|--------|--------|
| **自定义 prompt** | `~/.codex/prompts/` | 文件系统 | 可复用快捷方式 |
| **AGENTS.md** | 项目 + home | 跨会话 | 约定与上下文 |
| **config.toml** | `~/.codex/` | 跨会话 | 默认值与 profile |
| **审批/沙箱** | flag + 配置 | 单次会话 | 安全的自主性 |
| **MCP** | config.toml | 实时 | 外部工具/数据 |
| **codex exec** | 终端/CI | 单次运行 | 自动化 |
| **Profile** | config.toml | 跨会话 | 多模型工作流 |

---

**最后更新**: September 28, 2026
**工具**: OpenAI Codex CLI (`@openai/codex`)
**兼容模型**: GPT-5-Codex (默认), GPT-5, 以及 OpenAI 兼容和本地 (OSS) 模型
