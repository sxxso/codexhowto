# 风格规范

> 为 codexhowto 贡献内容时的约定与格式规则。遵循本规范,让内容保持一致、专业、易于维护。

---

## 目录

- [文件与文件夹命名](#文件与文件夹命名)
- [文档结构](#文档结构)
- [标题](#标题)
- [文本格式](#文本格式)
- [表格](#表格)
- [代码块](#代码块)
- [链接与交叉引用](#链接与交叉引用)
- [图表](#图表)
- [术语](#术语)
- [元数据页脚](#元数据页脚)
- [作者检查清单](#作者检查清单)

---

## 文件与文件夹命名

### 课程文件夹

课程文件夹使用**两位数字前缀**加 **kebab-case** 描述词。数字体现从入门到进阶的学习路径顺序:

```text
01-getting-started/
02-slash-commands/
03-agents-md/
04-config/
05-approvals-sandbox/
```

### 文件名

| 类型 | 约定 | 示例 |
|------|-----------|----------|
| **课程 README** | `README.md` | `05-approvals-sandbox/README.md` |
| **提示词模板** | kebab-case `.md` | `review.md`、`commit.md` |
| **配置模板** | 描述性 `.toml` | `config.toml`、`profiles-config.toml` |
| **脚本** | kebab-case `.sh`/`.yml` | `review-diff.sh`、`codex-review.yml` |
| **记忆模板** | 带作用域前缀 | `project-AGENTS.md`、`personal-AGENTS.md` |
| **顶层文档** | 全大写 `.md` | `CATALOG.md`、`QUICK_REFERENCE.md` |

### 规则

- 文件和文件夹名一律用**小写**(顶层文档如 `README.md`、`CATALOG.md` 除外)。
- 用**连字符**(`-`)分隔单词,不用下划线或空格。
- 名称保持描述性但简洁。

---

## 文档结构

### 课程 README

每个课程 `README.md` 遵循如下顺序:

1. H1 标题(例如 `# Approvals & Sandboxing`)
2. 简短的概述段落
3. 架构图(Mermaid)
4. 详细章节(H2)
5. 实践示例(编号,4-6 个)
6. 最佳实践(Do/Don't 表格)
7. 故障排查
8. 相关指南
9. 元数据页脚

用水平分割线(`---`)分隔主要区块。

---

## 标题

| 层级 | 用途 | 示例 |
|-------|-----|---------|
| `#` H1 | 页面标题(每篇一个) | `# Configuration` |
| `##` H2 | 主要章节 | `## Best Practices` |
| `###` H3 | 子章节 | `### Adding a profile` |

- **每篇文档只有一个 H1。**
- **不要跳级。**
- **使用 sentence case** —— 只有首词和专有名词首字母大写(功能名和命令名保持原样)。中文标题按中文习惯书写。
- 课程标题和正文中不使用装饰性 emoji。

---

## 文本格式

| 样式 | 何时使用 | 示例 |
|-------|------------|---------|
| **加粗** | 关键术语、表格行标签 | `**Installation**:` |
| *斜体* | 技术术语首次出现 | `*frontmatter*` |
| `代码` | 文件名、命令、配置键、取值 | `` `config.toml` `` |

使用带加粗前缀的引用块提示:**Note**、**Important**、**Tip**、**Warning**。

```markdown
> **Warning**: `--dangerously-bypass-approvals-and-sandbox` disables all safety. Use it only in disposable containers.
```

---

## 表格

- 当第一列是行标签时,**将其加粗**。
- 单元格内容保持简洁;命令和路径用 `代码格式`。
- 命令参考、flag 列表和 Do/Don't 对比优先用表格。

---

## 代码块

始终标注语言:

| 语言 | 标签 | 用于 |
|----------|-----|---------|
| Shell | `bash` | CLI 命令、脚本 |
| TOML | `toml` | `config.toml` 片段 |
| JSON | `json` | JSON 负载 |
| YAML | `yaml` | CI 工作流、frontmatter |
| Markdown | `markdown` | Markdown 示例、提示词 |
| 纯文本 | `text` | 目录树、预期输出 |

- 在不显而易见的命令前加一行注释。
- 让每个示例都可直接复制运行。

---

## 链接与交叉引用

内部链接使用相对路径:

```markdown
[Approvals & Sandbox](05-approvals-sandbox/)
[Config precedence](04-config/#precedence)
[Back to main guide](../README.md)
```

外部链接使用完整 URL,并配描述性锚文本。不要用「点这里」。

每篇课程都以 **相关指南** 章节结尾,链接到相关的同级模块。

---

## 图表

所有图表使用 Mermaid(`graph TB`/`graph LR`、`sequenceDiagram`、`flowchart`)。

**配色板:**

| 颜色 | 十六进制 | 用于 |
|-------|-----|---------|
| 浅蓝 | `#e1f5fe` | 主要组件、输入 |
| 浅粉 | `#fce4ec` | 处理、中间层 |
| 浅绿 | `#e8f5e9` | 输出、结果 |
| 浅黄 | `#fff9c4` | 配置、可选项 |
| 浅紫 | `#f3e5f5` | 面向用户、UI |

规则:

- 节点标签用 `["Label text"]`(以支持特殊字符)。
- 图表保持简单(最多 10-12 个节点)。
- 每张图下方加一行文字描述,以便无障碍访问。

---

## 术语

- 使用 **"Codex CLI"** 或 **"Codex"**(不用「这个工具」「OpenAI CLI」)。
- 用 **"AGENTS.md"** 指项目记忆/指令。
- 用 **"custom prompt"** 指 `~/.codex/prompts/` 中用户自定义的斜杠命令。
- 把 **"approval policy"** 和 **"sandbox mode"** 当作两个独立维度。
- 用 **"lesson"** 或 **"module"** 指编号章节,用 **"example"** 指单个模板文件。
- 课程内容中绝不提及其他编码智能体的名称。

---

## 元数据页脚

课程 README 以此结尾:

```markdown
---

**Last Updated**: September 28, 2026
**Tool**: OpenAI Codex CLI (`@openai/codex`)
**Compatible Models**: GPT-5-Codex (default), GPT-5, plus OpenAI-compatible and local (OSS) models
*Part of the [codexhowto](../) guide series*
```

---

## 作者检查清单

- [ ] 文件/文件夹名使用 kebab-case
- [ ] 文档以一个 H1 标题开头
- [ ] 标题层级正确(不跳级)
- [ ] 所有代码块都有语言标签
- [ ] 代码示例可直接复制运行
- [ ] 内部链接使用相对路径
- [ ] 表格格式规范
- [ ] Mermaid 图使用标准配色板且能正确解析
- [ ] 无敏感信息(API key、凭据)
- [ ] 不提及其他编码智能体
- [ ] 相关指南章节链接到相关模块
- [ ] 元数据页脚存在且为最新

---

**最后更新**: September 28, 2026
**工具**: OpenAI Codex CLI (`@openai/codex`)
**兼容模型**: GPT-5-Codex (默认), GPT-5, 以及 OpenAI 兼容和本地 (OSS) 模型
