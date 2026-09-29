# Personal preferences

> Global personal `AGENTS.md`. Place at `~/.codex/AGENTS.md`
> (`%USERPROFILE%\.codex\AGENTS.md` on Windows). These preferences apply to
> every project on this machine. A repository's own `AGENTS.md` overrides
> anything here when they conflict, so keep this file about *how you like to
> work*, not project-specific rules.

## Working style

- Before a large or multi-file change, briefly explain the plan, then proceed.
- Prefer the smallest change that solves the problem. No speculative
  abstractions.
- When a task fails twice the same way, stop and explain the root cause instead
  of retrying the same fix.

## Code preferences

- Prefer standard-library and built-in solutions over adding dependencies.
- Match the style of the surrounding code rather than imposing my own.
- Add comments only where intent is non-obvious; do not narrate every line.

## Tooling

- Use `rg` (ripgrep) for searching, not `grep -r`.
- Use `fd` for finding files when available.
- Assume a POSIX shell unless the project says otherwise.

## Git

- Use Conventional Commits for messages.
- Never commit unless I ask. When I do, stage only the files relevant to the task.
- Never force-push or run destructive git commands without confirming first.

## Communication

- Be concise. Lead with the answer, then the reasoning.
- Report test results honestly — if something is untested or failing, say so.
