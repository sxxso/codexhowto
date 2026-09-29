# 快速参考

OpenAI Codex CLI 的单页速查表。想要更深入,见 [CLI 参考](10-cli/)。想把它用起来,见[实战手册](11-recipes/)、[决策指南](12-decision-guides/)、[提示词库](13-prompt-library/),以及动手[练习](exercises/)。

---

## 安装与更新

```bash
npm install -g @openai/codex        # 安装 (npm)
brew install codex                  # 安装 (Homebrew)
npm install -g @openai/codex@latest # 更新
codex --version                     # 验证
```

## 认证

```bash
codex login                         # 用 ChatGPT 套餐登录
codex login --api-key "$OPENAI_API_KEY"  # 或使用 API key
codex login status                  # 查看认证状态
codex logout
```

## 运行

```bash
codex                               # 交互式 TUI
codex "explain this repo"           # 带起始提示词的 TUI
codex exec "fix the failing test"   # 无人值守 / 非交互
codex resume                        # 选择一个历史会话
codex resume --last                 # 恢复最近的会话
```

## 核心标志

| 标志 | 用途 |
|------|---------|
| `-m, --model <name>` | 模型 (如 `gpt-5-codex`、`gpt-5`) |
| `-p, --profile <name>` | 使用 `config.toml` 中的命名 profile |
| `-a, --ask-for-approval <policy>` | `untrusted` \| `on-failure` \| `on-request` \| `never` |
| `-s, --sandbox <mode>` | `read-only` \| `workspace-write` \| `danger-full-access` |
| `--full-auto` | `workspace-write` + 低摩擦审批 |
| `--dangerously-bypass-approvals-and-sandbox` | 无审批、无沙箱 (仅限容器) |
| `-C, --cd <dir>` | 设置工作目录 |
| `-c, --config key=value` | 覆盖某个 `config.toml` 值 |
| `-i, --image <path>` | 给提示词附加图片 |
| `--oss` | 通过 Ollama 使用本地 (OSS) 模型 |
| `--search` | 为本次会话启用网络搜索 |

## 交互式斜杠命令

| 命令 | 用途 |
|---------|---------|
| `/init` | 为仓库生成 `AGENTS.md` |
| `/model` | 选择模型 + 推理强度 |
| `/approvals` | 更改审批策略 + 沙箱模式 |
| `/diff` | 显示当前 git diff |
| `/compact` | 压缩对话以回收上下文 |
| `/new` | 开始新对话 |
| `/status` | 会话、配置和 token 使用情况 |
| `/mcp` | 列出已连接的 MCP 服务器和工具 |
| `/review` | 审查当前改动 |
| `/prompts` | 列出你的自定义提示词 |
| `/clear` | 清屏 |
| `/quit` (`/exit`) | 退出会话 |

在 TUI 里输入 `/` 查看完整菜单。

## 键盘 (TUI)

| 按键 | 动作 |
|-----|--------|
| `Ctrl+C` | 中断智能体 (按两次退出) |
| `Ctrl+D` | 在空提示行退出 |
| `Esc` | 中断 / 编辑 |
| `Shift+Enter` / `Ctrl+J` | 换行 |
| `@` | 引用文件 |
| `↑` / `↓` | 提示词历史 |

## config.toml 要点 (`~/.codex/config.toml`)

```toml
model = "gpt-5-codex"
model_reasoning_effort = "medium"       # minimal | low | medium | high
approval_policy = "on-request"          # untrusted | on-failure | on-request | never
sandbox_mode = "workspace-write"        # read-only | workspace-write | danger-full-access

[sandbox_workspace_write]
network_access = false                  # true 重新启用网络

[tools]
web_search = true

[profiles.deep]
model = "gpt-5-codex"
model_reasoning_effort = "high"

[mcp_servers.filesystem]
command = "npx"
args = ["-y", "@modelcontextprotocol/server-filesystem", "/path"]
```

启动时覆盖任意键: `codex -c model="gpt-5" -c 'sandbox_mode="read-only"'`

## 日常配方

```bash
# 安全的只读审查
codex --sandbox read-only "review the changes on this branch"

# 均衡的日常编码
codex -a on-request -s workspace-write "add tests for utils.ts"

# 管道传入 diff 进行审查
git diff | codex exec "review this diff for bugs"

# 无人值守 CI 卡点 (容器内)
codex exec --full-auto "run the test suite and fix failures"

# 本地 / 离线
codex --oss -m gpt-oss "refactor this function"
```

## 关键文件与环境变量

| 路径 / 变量 | 含义 |
|------------|------|
| `~/.codex/config.toml` | 配置 |
| `~/.codex/AGENTS.md` | 全局个人指令 |
| `./AGENTS.md` | 仓库指令 |
| `~/.codex/prompts/` | 自定义提示词命令 |
| `~/.codex/sessions/` | 已保存的对话 |
| `OPENAI_API_KEY` | API key 认证 |
| `CODEX_HOME` | 覆盖 `~/.codex` |

---

**最后更新**: September 28, 2026
**工具**: OpenAI Codex CLI (`@openai/codex`)
**兼容模型**: GPT-5-Codex (默认), GPT-5, 以及 OpenAI 兼容和本地 (OSS) 模型
