---
description: Generate changelog entries from recent commits
argument-hint: [since-ref]
---

Generate changelog entries for the changes since `$1` (a tag, commit, or date).
If nothing was given, use the commits since the most recent tag.

Read the commit history and diffs for that range, then group user-facing changes
under Keep a Changelog headings, omitting any that are empty:

```
### Added
### Changed
### Deprecated
### Removed
### Fixed
### Security
```

Rules:

- Write for users, not for the repo — describe the effect, not the internal
  refactor. Skip purely internal churn (formatting, test-only, CI) unless it
  affects users.
- One clear line per entry, imperative or past tense, consistent throughout.
- If commit messages follow Conventional Commits, map `feat`→Added/Changed,
  `fix`→Fixed, etc.
- Do not invent version numbers or dates. Output the Markdown for me to paste.
