---
description: Track down the root cause of a bug
argument-hint: [symptom-or-description]
---

Investigate this bug and find its root cause: $ARGUMENTS

Work like a debugger, not a guesser:

1. **Restate** the observed symptom and what the correct behavior should be.
2. **Locate** the relevant code paths. Read the files involved before theorizing.
3. **Trace** how data flows to the failure point; identify the exact line where
   behavior diverges from intent.
4. **Explain** the root cause — not just the surface symptom.
5. **Propose** the minimal fix, with a code snippet, and note any edge cases the
   fix must also handle.

If you need to reproduce it, suggest a concrete command or test input. If the
cause is genuinely ambiguous, list the top candidates ranked by likelihood with
the evidence for each. Do not apply the fix yet — show me the diagnosis first.
