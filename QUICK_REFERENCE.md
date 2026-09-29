# Quick Reference

A one-page cheat sheet for OpenAI Codex CLI. For depth, see the [CLI Reference](10-cli/). To apply it, see [Recipes](11-recipes/), [Decision Guides](12-decision-guides/), the [Prompt Library](13-prompt-library/), and the hands-on [Exercises](exercises/).

---

## Install & Update

```bash
npm install -g @openai/codex        # install (npm)
brew install codex                  # install (Homebrew)
npm install -g @openai/codex@latest # update
codex --version                     # verify
```

## Auth

```bash
codex login                         # sign in with ChatGPT plan
codex login --api-key "$OPENAI_API_KEY"  # or use an API key
codex login status                  # check auth
codex logout
```

## Run

```bash
codex                               # interactive TUI
codex "explain this repo"           # TUI with a starting prompt
codex exec "fix the failing test"   # headless / non-interactive
codex resume                        # pick a past session
codex resume --last                 # resume the most recent
```

## Core Flags

| Flag | Purpose |
|------|---------|
| `-m, --model <name>` | Model (e.g. `gpt-5-codex`, `gpt-5`) |
| `-p, --profile <name>` | Use a named profile from `config.toml` |
| `-a, --ask-for-approval <policy>` | `untrusted` \| `on-failure` \| `on-request` \| `never` |
| `-s, --sandbox <mode>` | `read-only` \| `workspace-write` \| `danger-full-access` |
| `--full-auto` | `workspace-write` + low-friction approvals |
| `--dangerously-bypass-approvals-and-sandbox` | No approvals, no sandbox (containers only) |
| `-C, --cd <dir>` | Set the working directory |
| `-c, --config key=value` | Override a `config.toml` value |
| `-i, --image <path>` | Attach an image to the prompt |
| `--oss` | Use a local (OSS) model via Ollama |
| `--search` | Enable web search for the session |

## Interactive Slash Commands

| Command | Purpose |
|---------|---------|
| `/init` | Scaffold an `AGENTS.md` for the repo |
| `/model` | Pick model + reasoning effort |
| `/approvals` | Change approval policy + sandbox mode |
| `/diff` | Show the current git diff |
| `/compact` | Summarize the conversation to reclaim context |
| `/new` | Start a fresh conversation |
| `/status` | Session, config, and token usage |
| `/mcp` | List connected MCP servers and tools |
| `/review` | Review the current changes |
| `/prompts` | List your custom prompts |
| `/clear` | Clear the screen/scrollback |
| `/quit` (`/exit`) | Leave the session |

Type `/` in the TUI to see the full menu.

## Keyboard (TUI)

| Key | Action |
|-----|--------|
| `Ctrl+C` | Interrupt the agent (twice to quit) |
| `Ctrl+D` | Exit on an empty prompt |
| `Esc` | Interrupt / edit |
| `Shift+Enter` / `Ctrl+J` | Newline |
| `@` | Mention a file |
| `↑` / `↓` | Prompt history |

## config.toml Essentials (`~/.codex/config.toml`)

```toml
model = "gpt-5-codex"
model_reasoning_effort = "medium"       # minimal | low | medium | high
approval_policy = "on-request"          # untrusted | on-failure | on-request | never
sandbox_mode = "workspace-write"        # read-only | workspace-write | danger-full-access

[sandbox_workspace_write]
network_access = false                  # true re-enables network

[tools]
web_search = true

[profiles.deep]
model = "gpt-5-codex"
model_reasoning_effort = "high"

[mcp_servers.filesystem]
command = "npx"
args = ["-y", "@modelcontextprotocol/server-filesystem", "/path"]
```

Override any key at launch: `codex -c model="gpt-5" -c 'sandbox_mode="read-only"'`

## Everyday Recipes

```bash
# Safe read-only review
codex --sandbox read-only "review the changes on this branch"

# Balanced everyday coding
codex -a on-request -s workspace-write "add tests for utils.ts"

# Pipe a diff for review
git diff | codex exec "review this diff for bugs"

# Headless CI gate (container)
codex exec --full-auto "run the test suite and fix failures"

# Local / offline
codex --oss -m gpt-oss "refactor this function"
```

## Key Files & Env

| Path / Var | What |
|------------|------|
| `~/.codex/config.toml` | Configuration |
| `~/.codex/AGENTS.md` | Global personal instructions |
| `./AGENTS.md` | Repo instructions |
| `~/.codex/prompts/` | Custom prompt commands |
| `~/.codex/sessions/` | Saved conversations |
| `OPENAI_API_KEY` | API-key auth |
| `CODEX_HOME` | Override `~/.codex` |

---

**Last Updated**: September 28, 2026
**Tool**: OpenAI Codex CLI (`@openai/codex`)
**Compatible Models**: GPT-5-Codex (default), GPT-5, plus OpenAI-compatible and local (OSS) models
