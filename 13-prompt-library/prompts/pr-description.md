---
description: Draft a pull request title and description from the branch changes
argument-hint: [base-branch]
---

Draft a pull request for the current branch. Compare against `$1` if a base
branch was given above, otherwise against the default branch.

Read the diff and commit messages before writing. Produce:

**Title** — a concise, imperative summary under 70 characters.

**Description** — in Markdown:

- **Summary** — what this PR does and why, in 1–3 sentences.
- **Changes** — a bullet list of the notable changes, grouped if large.
- **Testing** — how the changes were verified (tests added/run, manual checks).
- **Notes** — anything reviewers should know: tradeoffs, follow-ups, blocked
  items, or breaking changes.

Base the content only on what the diff actually shows — do not invent testing
that was not done or features that are not present. Output the title and
description as text I can copy; do not open the PR yourself.
