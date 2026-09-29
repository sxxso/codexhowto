# 为 codexhowto 做贡献

感谢你帮助开发者掌握 OpenAI Codex CLI。本指南说明如何贡献示例、修复和文档。

## 贡献类型

- **新示例** —— 自定义 prompt、`AGENTS.md` 模板、`config.toml` profile、MCP 配置、CI 脚本
- **文档** —— 更清晰的解释、更好的图示、修复链接
- **修复缺陷** —— 错误的命令、过时的行为、失效的示例
- **翻译** —— 保持 `zh/` 镜像同步,或新增一个语言目录树

## 基本原则

1. **只教 Codex CLI。** 课程内容中不要提及其他编码智能体的名字。
2. **遵循[风格指南](../STYLE_GUIDE.md)。** 结构、命名、标题、表格和图示必须一致。
3. **不含机密。** 绝不提交真实的 API key 或 token。使用 `OPENAI_API_KEY` 和占位符。
4. **安全默认。** 示范能完成任务的最紧审批策略与沙箱模式。任何 `--dangerously-bypass-approvals-and-sandbox` 示例都要包在 **Warning** 提示块里,并置于容器/CI 语境中。
5. **不要编造事实。** 不要添加你无法核实的 Codex 版本号、flag 或配置键。不确定时就描述行为、不做版本断言。

## 目录结构

```text
codexhowto/
├── 01-getting-started/     # 每个模块:README.md + 模板
├── 02-slash-commands/
│   └── prompts/            # 自定义 prompt 模板
├── ...
├── 10-cli/
├── zh/                     # 英文主干的中文镜像
├── README.md               # 主概览
├── INDEX.md                # 完整文件索引
├── CATALOG.md              # 功能目录
├── QUICK_REFERENCE.md      # 一页速查表
├── LEARNING-ROADMAP.md     # 引导式路径
├── STYLE_GUIDE.md          # 格式规范
└── AGENTS.md               # 给 Codex 的项目说明
```

## 新增模块页面

1. 按[课程结构](../STYLE_GUIDE.md)编写模块 `README.md`。
2. 在模块文件夹中加入可复制粘贴的模板。
3. 更新根 `README.md`、`INDEX.md`、`CATALOG.md` 和 `LEARNING-ROADMAP.md`。
4. 在 `zh/` 下同步该变更。

## 提交信息

遵循 [Conventional Commits](https://www.conventionalcommits.org/):`type(scope): description`

| 类型 | 用于 |
|------|------|
| `feat` | 新示例或指南 |
| `fix` | 修正、失效链接 |
| `docs` | 文档改进 |
| `refactor` | 不改变行为的重构 |
| `chore` | 构建、CI、杂务 |

scope 是模块名,例如 `feat(mcp): add GitHub server example`、`docs(config): clarify precedence`。

## Pull Request 流程

1. Fork 并克隆仓库。
2. 创建一个描述性分支(`add/mcp-example`、`fix/config-link`)。
3. 按本指南和风格指南进行修改。
4. 核实所有内部链接可解析、代码围栏都有语言标签。
5. 开一个 PR,清楚说明改了什么、为什么。

需要帮助?开一个 issue 或 discussion。

---

**最后更新**: September 28, 2026
**工具**: OpenAI Codex CLI (`@openai/codex`)
**兼容模型**: GPT-5-Codex (默认), GPT-5, 以及 OpenAI 兼容和本地 (OSS) 模型
