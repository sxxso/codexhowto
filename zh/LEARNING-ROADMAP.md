# 学习路线图

一条精通 OpenAI Codex CLI 的引导式路径——从第一次 `codex` 会话到无人值守的 CI 流水线。按顺序学完各模块;每个都建立在上一个之上。

---

## 找到你的水平

如实回答。第一个"否"就是你该开始的地方。

1. 你安装 Codex CLI 并登录了吗? → 否: **[入门](01-getting-started/)**
2. 你会在 `~/.codex/prompts/` 里创建自定义提示词吗? → 否: **[斜杠命令](02-slash-commands/)**
3. 你的仓库有一个 Codex 真正会用的 `AGENTS.md` 吗? → 否: **[AGENTS.md](03-agents-md/)**
4. 你能自信地读写 `~/.codex/config.toml` 吗? → 否: **[配置](04-config/)**
5. 你能解释审批策略 vs 沙箱模式吗? → 否: **[审批与沙箱](05-approvals-sandbox/)**
6. 你连接过 MCP 服务器吗? → 否: **[MCP](06-mcp/)**
7. 你在脚本或 CI 任务里运行过 `codex exec` 吗? → 否: **[自动化](07-automation/)**
8. 你会为不同模型/任务使用 profile 吗? → 否: **[Profile](08-profiles/)**
9. 你会用会话、notify、网络搜索或 IDE 扩展吗? → 否: **[进阶](09-advanced/)**
10. 全部回答"是"? → 去应用它:**[实战手册](11-recipes/)**、**[决策指南](12-decision-guides/)**、**[提示词库](13-prompt-library/)**,并在**[动手实验](exercises/)**里验证。把 **[CLI 参考](10-cli/)** 当速查表随时开着。

---

## 完整路径

```mermaid
graph LR
    A["01 Getting Started"] --> B["02 Slash Commands"]
    B --> C["03 AGENTS.md"]
    C --> D["04 Config"]
    D --> E["05 Approvals & Sandbox"]
    E --> F["06 MCP"]
    F --> G["07 Automation"]
    G --> H["08 Profiles"]
    H --> I["09 Advanced"]
    I --> J["10 CLI Reference"]
    J --> K["11–13 Applied"]
    K --> L["Hands-on Lab"]

    style A fill:#e1f5fe,stroke:#333,color:#333
    style E fill:#fff9c4,stroke:#333,color:#333
    style G fill:#fce4ec,stroke:#333,color:#333
    style J fill:#e8f5e9,stroke:#333,color:#333
    style L fill:#f3e5f5,stroke:#333,color:#333
```

十个参考模块(入门 → 进阶),然后是一层进阶应用——实战手册、决策指南、提示词库(11–13)——最后用一套动手实验把它全部验证一遍。

---

## 周末计划

### 周六上午 —— 基础 (约 2 小时)

| 模块 | 时间 | 成果 |
|--------|------|---------|
| [01 入门](01-getting-started/) | 30 分钟 | 装好、登录、跑完第一次会话 |
| [02 斜杠命令](02-slash-commands/) | 30 分钟 | 你的第一个自定义提示词出现在 `/` 菜单里 |
| [03 AGENTS.md](03-agents-md/) | 45 分钟 | Codex 了解你的项目约定 |

### 周六下午 —— 掌控 (约 2.5 小时)

| 模块 | 时间 | 成果 |
|--------|------|---------|
| [04 配置](04-config/) | 45 分钟 | 一份你看得懂的 `config.toml` |
| [05 审批与沙箱](05-approvals-sandbox/) | 1 小时 | 自信而安全的自主运行 |
| [06 MCP](06-mcp/) | 1 小时 | 接入实时工具与数据 |

### 周日 —— 扩展 (约 3 小时)

| 模块 | 时间 | 成果 |
|--------|------|---------|
| [07 自动化](07-automation/) | 1.5 小时 | 一个 `codex exec` 的 CI 审查任务 |
| [08 Profile](08-profiles/) | 1 小时 | 备好 fast/deep/local profile |
| [09 进阶](09-advanced/) | 1.5 小时 | 会话、notify、网络搜索、IDE |

全程把 [10 CLI 参考](10-cli/) 开着。

### 周日晚上 —— 应用它 (约 2 小时,可选但推荐)

| 模块 | 时间 | 成果 |
|--------|------|---------|
| [11 实战手册](11-recipes/) | 1 小时 | 把学到的东西组合成真实工作流 |
| [12 决策指南](12-decision-guides/) | 45 分钟 | 在审批、模型、指令归属上做出笃定选择 |
| [13 提示词库](13-prompt-library/) | 30 分钟 | 装好 14 个可复用 prompt |
| [动手实验](exercises/) | 1.5 小时 | 你用 Codex 修好了一个真实的破项目 |

---

## 按目标分的学习线路

### "我只想要安全的自主运行"

1. [审批与沙箱](05-approvals-sandbox/)
2. [配置](04-config/)
3. [Profile](08-profiles/)

### "我想把 Codex 用进 CI"

1. [自动化](07-automation/)
2. [审批与沙箱](05-approvals-sandbox/) (只读 / 容器内 YOLO)
3. [AGENTS.md](03-agents-md/) (让 CI 运行符合你的约定)

### "我想让 Codex 了解我的代码库"

1. [AGENTS.md](03-agents-md/)
2. [斜杠命令](02-slash-commands/)
3. [MCP](06-mcp/)

---

**最后更新**: September 28, 2026
**工具**: OpenAI Codex CLI (`@openai/codex`)
**兼容模型**: GPT-5-Codex (默认), GPT-5, 以及 OpenAI 兼容和本地 (OSS) 模型
