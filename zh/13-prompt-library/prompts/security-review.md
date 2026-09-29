---
description: Audit changed code for security vulnerabilities
argument-hint: [focus-area]
---

Perform a focused security review of the files changed in this branch (compare
against the default branch, or use the staged/working-tree diff if there is no
branch to compare).

Focus area (optional): $ARGUMENTS

Look specifically for:

- **Injection** — SQL/NoSQL/command/template injection from untrusted input.
- **AuthN/AuthZ** — missing or broken authentication and access-control checks.
- **Secrets** — hardcoded credentials, tokens, or keys; secrets written to logs.
- **Input validation** — unvalidated request data, path traversal, SSRF.
- **Crypto** — weak algorithms, missing verification, predictable randomness.
- **Data exposure** — PII or sensitive fields leaked in responses or errors.

For each finding, report:

- **Severity**: critical / high / medium / low
- **Location**: `file:line`
- **Vulnerability**: the class of issue and how it could be exploited
- **Fix**: a concrete remediation or code snippet

Order findings by severity, most severe first. Do not invent issues — if the
diff is clean, say so and note anything that would benefit from a deeper audit.
