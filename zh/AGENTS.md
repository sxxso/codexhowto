# AGENTS.md

教程仓库。产出是 `01-` 到 `10-` 编号模块中的 Markdown,而不是一个应用程序。本文件是 Codex CLI(以及其他智能体)启动时读取的项目说明——它同时也是 [模块 03](03-agents-md/) 所讲内容的一个活例子。

## 本项目是什么

- 一份结构化、以示例驱动的 **OpenAI Codex CLI**(`@openai/codex`)指南。
- 10 个编号教程模块,每个都有一个 `README.md`,外加可复制粘贴的模板(`.md`、`.toml`、`.sh`、`.yml`)。
- 仓库根目录是英文主干,`zh/` 下是中文镜像。

## 结构地图

- `01-` … `10-` —— 教程模块。**编号前缀就是学习顺序**,不是字母序。请勿重新组织。
- 每个模块:`README.md` + 用户复制到自己项目或 `~/.codex/` 的模板。
- `zh/` —— 逐文件镜像英文主干的中文翻译。
- 顶层文档:`README.md`、`INDEX.md`、`CATALOG.md`、`QUICK_REFERENCE.md`、`LEARNING-ROADMAP.md`、`STYLE_GUIDE.md`。

## 硬性规则

- **未经明确请求,不要提交或推送。**
- 只教 **Codex CLI**——在课程内容中绝不提及其他工具的名字。
- 内部链接使用 **相对路径**(如 `03-agents-md/README.md`);锚点使用 `#heading-name`。
- 代码围栏 **必须** 声明语言(`bash`、`toml`、`json`、`yaml`、`markdown` 等)。
- Mermaid 图必须能解析,并应使用 `STYLE_GUIDE.md` 中的共享配色。
- 不要编造 Codex 的版本号、flag 或配置键。不确定时,就描述行为、不做版本断言。
- 保持 `01-`–`10-` 编号稳定——顺序即课程。

## 风格

- 结构、命名、标题、表格、图示遵循 `STYLE_GUIDE.md`(英文)。
- 每个课程 `README.md`:H1 → 概述 → Mermaid 架构图 → 详细小节 → 4-6 个编号示例 → Do/Don't 表格 → 故障排查 → 相关指南 → 元数据页脚。
- 语气:专业而易读,主动语态,示例可直接复制粘贴,解释"为什么"。
- 标题用句首大写;课程正文不用装饰性 emoji。

## 工作流偏好

- 小修改 → 最小 diff。不要为改个错别字而重写整节。
- 新增模块时:先写 `README.md` + 模板,再更新根 `README.md`、`INDEX.md`、`CATALOG.md`、`LEARNING-ROADMAP.md`(若顺序/时长有变)。
- 英文内容变化时,同步更新 `zh/` 镜像。
- 教程优先于抽象:清晰的解释和可用示例胜过精巧的抽象。

## 元数据页脚

每个课程 `README.md` 以此结尾:

```markdown
---

**Last Updated**: September 28, 2026
**Tool**: OpenAI Codex CLI (`@openai/codex`)
**Compatible Models**: GPT-5-Codex (default), GPT-5, plus OpenAI-compatible and local (OSS) models
*Part of the [codexhowto](../) guide series*
```

---

**最后更新**: September 28, 2026
**工具**: OpenAI Codex CLI (`@openai/codex`)
**兼容模型**: GPT-5-Codex (默认), GPT-5, 以及 OpenAI 兼容和本地 (OSS) 模型
*[codexhowto](../) 指南系列的一部分*
