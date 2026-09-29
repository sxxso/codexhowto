---
description: Find and fill gaps in test coverage
argument-hint: [module-or-path]
---

Analyze the test coverage for $ARGUMENTS (or the whole project if nothing was
given) and fill the most important gaps.

1. **Map** what is tested versus what exists. If the project has a coverage tool,
   suggest or run the command to generate a report; otherwise reason from the
   code and existing tests.
2. **Rank** the untested or under-tested areas by risk — prioritize complex
   logic, error handling, and code that changed recently.
3. **Report** the gaps as a short prioritized list before writing anything.
4. **Write** tests for the top gaps, matching the project's existing framework
   and style.

Focus on meaningful assertions over raw line coverage — a test that would catch
a real regression beats one that just executes a line. Run the suite when done
and report the result.
