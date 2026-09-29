# Project: acme-web

> Repo-root `AGENTS.md` for a TypeScript / Node project. Copy to your repository
> root, then edit to match your stack. Codex reads this at the start of every
> session in this repository.

## Overview

`acme-web` is a TypeScript web application. The frontend is React (Vite); the
backend is a Node HTTP service. Code is organized as a small monorepo managed
with pnpm workspaces.

## Commands

Use these exact commands — the project standardizes on pnpm.

- **Install**: `pnpm install`
- **Dev server**: `pnpm dev`
- **Build**: `pnpm build`
- **Test (all)**: `pnpm test`
- **Test (one file)**: `pnpm test -- path/to/file.test.ts`
- **Lint**: `pnpm lint`
- **Format**: `pnpm format`
- **Type-check**: `pnpm typecheck`

Before considering any task done, run `pnpm lint && pnpm typecheck && pnpm test`.

## Project layout

- `src/web/` — React components, hooks, and pages.
- `src/api/` — HTTP handlers and service logic. See `src/api/AGENTS.md`.
- `src/shared/` — types and utilities used by both web and api.
- `generated/` — code generated from the OpenAPI spec. **Do not edit by hand.**
- `scripts/` — repo automation (build, release, codegen).
- `tests/` — integration tests. Unit tests live next to the code they cover.

## Code style

- Formatter: Prettier (config in `.prettierrc`). Never hand-format; run `pnpm format`.
- Linter: ESLint. Fix warnings; do not disable rules inline without a comment
  explaining why.
- Use named exports. Avoid default exports except for React page components.
- Prefer `const`; use `type` aliases over `interface` unless declaration merging
  is needed.
- Imports: absolute paths from `src/` via the `@/` alias, not deep relative paths.

## Conventions

- Errors: throw `AppError` from `src/shared/errors.ts`; never throw bare strings.
- Async: use `async/await`, not raw promise chains.
- Logging: use the `logger` from `src/shared/logger.ts`, not `console.log`.
- State: server state via TanStack Query; local UI state via React hooks.
- Tests: Vitest. Co-locate unit tests as `*.test.ts` beside the source file.

## Do and don't

- **Do** add or update tests for any behavior change.
- **Do** keep changes scoped to the task; avoid drive-by refactors.
- **Don't** edit anything under `generated/`.
- **Don't** add a new dependency without noting why in the PR description.
- **Don't** commit secrets or `.env` files.

## Commit and PR rules

- Branch names: `codex/<short-description>` (e.g. `codex/fix-login-redirect`).
- Commits: Conventional Commits (`feat:`, `fix:`, `docs:`, `refactor:`, `test:`).
- Do not push to `main`. Open a pull request.
- A PR is ready only when `pnpm lint && pnpm typecheck && pnpm test` all pass.
