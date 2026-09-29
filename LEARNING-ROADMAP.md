# Learning Roadmap

A guided path to mastering OpenAI Codex CLI — from your first `codex` session to headless CI pipelines. Work through the modules in order; each builds on the last.

---

## Find Your Level

Answer honestly. Your first "no" is where to start.

1. Have you installed Codex CLI and signed in? → No: **[Getting Started](01-getting-started/)**
2. Can you create a custom prompt in `~/.codex/prompts/`? → No: **[Slash Commands](02-slash-commands/)**
3. Does your repo have an `AGENTS.md` that Codex actually uses? → No: **[AGENTS.md](03-agents-md/)**
4. Can you read and edit `~/.codex/config.toml` confidently? → No: **[Configuration](04-config/)**
5. Can you explain approval policy vs. sandbox mode? → No: **[Approvals & Sandbox](05-approvals-sandbox/)**
6. Have you connected an MCP server? → No: **[MCP](06-mcp/)**
7. Have you run `codex exec` in a script or CI job? → No: **[Automation](07-automation/)**
8. Do you use profiles for different models/tasks? → No: **[Profiles](08-profiles/)**
9. Do you use sessions, notify, web search, or the IDE extension? → No: **[Advanced](09-advanced/)**
10. Answered yes to all? → Apply it: **[Recipes](11-recipes/)**, **[Decision Guides](12-decision-guides/)**, **[Prompt Library](13-prompt-library/)**, and prove it on the **[Hands-on Lab](exercises/)**. Keep the **[CLI Reference](10-cli/)** open as a cheat sheet.

---

## The Full Path

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

Ten reference modules (beginner → advanced), then an applied tier — recipes, decision guides, and a prompt library (11–13) — and a hands-on lab to prove it all.

---

## Weekend Plan

### Saturday morning — Foundations (~2 hours)

| Module | Time | Outcome |
|--------|------|---------|
| [01 Getting Started](01-getting-started/) | 30 min | Installed, signed in, first session run |
| [02 Slash Commands](02-slash-commands/) | 30 min | Your first custom prompt in the `/` menu |
| [03 AGENTS.md](03-agents-md/) | 45 min | Codex knows your project conventions |

### Saturday afternoon — Control (~2.5 hours)

| Module | Time | Outcome |
|--------|------|---------|
| [04 Configuration](04-config/) | 45 min | A `config.toml` you understand |
| [05 Approvals & Sandbox](05-approvals-sandbox/) | 1 hour | Confident, safe autonomy |
| [06 MCP](06-mcp/) | 1 hour | Live tools and data connected |

### Sunday — Scale (~3 hours)

| Module | Time | Outcome |
|--------|------|---------|
| [07 Automation](07-automation/) | 1.5 hours | A `codex exec` CI review job |
| [08 Profiles](08-profiles/) | 1 hour | Fast/deep/local profiles ready |
| [09 Advanced](09-advanced/) | 1.5 hours | Sessions, notify, web search, IDE |

Keep [10 CLI Reference](10-cli/) open throughout.

### Sunday evening — Apply it (~2 hours, optional but recommended)

| Module | Time | Outcome |
|--------|------|---------|
| [11 Recipes](11-recipes/) | 1 hour | Real workflows combining what you learned |
| [12 Decision Guides](12-decision-guides/) | 45 min | Confident choices on approvals, models, placement |
| [13 Prompt Library](13-prompt-library/) | 30 min | 14 reusable prompts installed |
| [Hands-on Lab](exercises/) | 1.5 hours | You fixed a real broken project with Codex |

---

## Learning Tracks by Goal

### "I just want safe autonomy"

1. [Approvals & Sandbox](05-approvals-sandbox/)
2. [Configuration](04-config/)
3. [Profiles](08-profiles/)

### "I want Codex in my CI"

1. [Automation](07-automation/)
2. [Approvals & Sandbox](05-approvals-sandbox/) (read-only / container YOLO)
3. [AGENTS.md](03-agents-md/) (so CI runs match your conventions)

### "I want Codex to know my codebase"

1. [AGENTS.md](03-agents-md/)
2. [Slash Commands](02-slash-commands/)
3. [MCP](06-mcp/)

---

**Last Updated**: September 28, 2026
**Tool**: OpenAI Codex CLI (`@openai/codex`)
**Compatible Models**: GPT-5-Codex (default), GPT-5, plus OpenAI-compatible and local (OSS) models
