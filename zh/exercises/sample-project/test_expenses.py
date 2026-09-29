"""Tests for the expense-tracker core logic.

Run from inside the sample-project directory:

    pytest -q

Some of these tests currently FAIL — that is intentional. They pin down
the behaviour the code is supposed to have; the planted bugs make them
red. Fixing the code (with Codex's help) should turn them green without
changing the tests. See ../README.md.

storage.py has no test file at all yet — writing one is Exercise 2.
"""

import expenses as ex


def sample():
    return [
        {"id": 1, "date": "2026-09-01", "amount": 10.0, "category": "Food", "note": ""},
        {"id": 2, "date": "2026-09-02", "amount": 0.1, "category": "food", "note": ""},
        {"id": 3, "date": "2026-09-03", "amount": 0.2, "category": "Travel", "note": ""},
    ]


def test_add_expense_assigns_next_id():
    rows = []
    ex.add_expense(rows, "5.00", "food", "snack")
    assert rows[0]["id"] == 1
    assert rows[0]["amount"] == 5.0
    assert rows[0]["category"] == "food"


def test_total_of_whole_numbers():
    rows = [
        {"id": 1, "date": "2026-09-01", "amount": 3.0, "category": "a", "note": ""},
        {"id": 2, "date": "2026-09-01", "amount": 7.0, "category": "b", "note": ""},
    ]
    assert ex.total(rows) == 10.0


def test_total_rounds_to_cents():
    # 0.1 + 0.2 must come back as 0.30, not 0.30000000000000004
    rows = [
        {"id": 1, "date": "2026-09-01", "amount": 0.1, "category": "a", "note": ""},
        {"id": 2, "date": "2026-09-01", "amount": 0.2, "category": "b", "note": ""},
    ]
    assert ex.total(rows) == 0.3


def test_filter_by_category_is_case_insensitive():
    # "Food" and "food" are the same category
    rows = sample()
    matched = ex.filter_by_category(rows, "food")
    assert len(matched) == 2


def test_filter_by_category_ignores_other_categories():
    # exact-case lookup — should work regardless of the case bug
    rows = sample()
    matched = ex.filter_by_category(rows, "Travel")
    assert len(matched) == 1
    assert matched[0]["id"] == 3
