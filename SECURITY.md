# Security Policy

## Scope

codexhowto is a documentation and template repository. It ships no runtime service. The main security considerations are:

- **Template safety** — example `config.toml`, scripts, and prompts should model safe defaults.
- **No secrets** — no real API keys, tokens, or credentials in any file.

## Reporting a Vulnerability

If you find a template that could lead users into an unsafe configuration (for example, a script that defaults to `--dangerously-bypass-approvals-and-sandbox` outside a container, or an example that leaks secrets), please open a private report rather than a public issue.

1. Use the repository's private vulnerability reporting, or
2. Contact the maintainers directly.

Do **not** open a public issue for security concerns.

## Safe-Template Guidelines

Contributors must follow these rules for any example:

- Default to the **tightest** approval policy and sandbox mode that still lets the task run (`on-request` + `workspace-write` for everyday work; `read-only` for review).
- Only show `--dangerously-bypass-approvals-and-sandbox` inside a clearly labeled container/CI context, always with a **Warning** callout.
- Never hardcode credentials. Use environment variables (`OPENAI_API_KEY`) and placeholders.
- Never enable `network_access` in `[sandbox_workspace_write]` without explaining the risk.

See [Approvals & Sandboxing](05-approvals-sandbox/) for the full safety model.
