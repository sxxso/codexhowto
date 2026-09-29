# src/api conventions

> Nested `AGENTS.md`. Place at `src/api/AGENTS.md` (or any subdirectory). These
> rules apply only while Codex is working inside this subtree, and they take
> priority over the repo-root file when they conflict. Keep it to the rules that
> are specific to this directory — everything general belongs in the repo-root
> `AGENTS.md`.

## Scope

This directory holds the HTTP API: route handlers, request/response schemas, and
service-layer logic. It must stay independent of the web/UI layer.

## Rules

- Validate every request body and query with `zod` before use. Reject invalid
  input with a 400 and the `problem+json` error shape from `src/api/errors.ts`.
- Do not import from `src/web/`. The API layer must not depend on UI code.
- All database access goes through the repositories in `src/api/repos/`. Handlers
  must not build SQL or call the driver directly.
- Handlers stay thin: parse and validate, delegate to a service, format the
  response. Business logic lives in `src/api/services/`.

## Testing

- Every handler needs an integration test in `tests/api/` covering the success
  path and at least one validation-failure path.
- Use the test client in `tests/api/client.ts`; do not start a real server in
  unit tests.

## Security

- Never log request bodies or headers that may contain tokens.
- Rate-limit new public endpoints via the `withRateLimit` wrapper.
