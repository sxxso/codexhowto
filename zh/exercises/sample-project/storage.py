"""Persistence layer for the expense tracker.

Expenses are stored as a JSON array of objects on disk. Each expense is:

    {"id": int, "date": "YYYY-MM-DD", "amount": float,
     "category": str, "note": str}

NOTE: this module ships with no tests of its own — writing them is one of
the lab exercises (see ../README.md).
"""

import json
import os


def load_expenses(path):
    """Load the list of expenses from a JSON file at ``path``.

    Should return an empty list when the file does not exist yet, so the
    very first run of the CLI works without a pre-created data file.
    """
    with open(path) as f:
        return json.load(f)


def save_expenses(path, expenses):
    """Write ``expenses`` (a list of dicts) to ``path`` as JSON."""
    with open(path, "w") as f:
        json.dump(expenses, f, indent=2)


def next_id(expenses):
    """Return the id to assign to the next expense."""
    if not expenses:
        return 1
    return max(e["id"] for e in expenses) + 1
