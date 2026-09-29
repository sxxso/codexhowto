---
description: Extract a well-named function from a block of code
argument-hint: [file:line-range]
---

Extract a clean, well-named function from the code at `$1`.

Steps:

1. Read the surrounding code to understand what the block does and what it
   depends on (inputs, mutated state, return values).
2. Identify the smallest cohesive unit worth extracting.
3. Choose a name that describes the *what*, not the *how*.
4. Determine the minimal parameter list and return type; avoid passing more state
   than the function needs.
5. Replace the original block with a call to the new function.

Keep behavior identical. Match the file's existing style for signatures, error
handling, and documentation. If the block has side effects that make a clean
extraction impossible, explain the obstacle and propose the smallest change that
makes extraction safe. Show the resulting diff and run the tests if present.
