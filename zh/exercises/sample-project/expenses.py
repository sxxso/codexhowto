"""A tiny expense-tracker CLI used as the codexhowto practice project.

Usage:
    python expenses.py add 12.50 food "lunch"
    python expenses.py list
    python expenses.py total
    python expenses.py total --category food
    python expenses.py report

The data file defaults to ./expenses.json (override with --file).

This project has a few planted bugs and one function that is overdue for a
refactor. Work through ../README.md with Codex to find and fix them.
"""

import argparse
import datetime

import storage
from report import generate_report

DEFAULT_FILE = "expenses.json"


def add_expense(expenses, amount, category, note=""):
    """Append a new expense and return it."""
    expense = {
        "id": storage.next_id(expenses),
        "date": datetime.date.today().isoformat(),
        "amount": float(amount),
        "category": category,
        "note": note,
    }
    expenses.append(expense)
    return expense


def filter_by_category(expenses, category):
    """Return the expenses that belong to ``category``.

    Categories are meant to be case-insensitive: "Food", "food" and "FOOD"
    should all be treated as the same category.
    """
    return [e for e in expenses if e["category"] == category]


def total(expenses):
    """Return the summed amount of ``expenses``, in dollars."""
    return sum(e["amount"] for e in expenses)


def list_expenses(expenses):
    """Return a human-readable, one-per-line listing of expenses."""
    lines = []
    for e in expenses:
        lines.append(
            f'#{e["id"]:<3} {e["date"]}  {e["amount"]:>8.2f}  '
            f'{e["category"]:<12} {e["note"]}'
        )
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Track expenses.")
    parser.add_argument("--file", default=DEFAULT_FILE, help="data file path")
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="add an expense")
    p_add.add_argument("amount")
    p_add.add_argument("category")
    p_add.add_argument("note", nargs="?", default="")

    sub.add_parser("list", help="list all expenses")

    p_total = sub.add_parser("total", help="sum expenses")
    p_total.add_argument("--category", default=None)

    sub.add_parser("report", help="print a category breakdown")

    args = parser.parse_args(argv)
    expenses = storage.load_expenses(args.file)

    if args.command == "add":
        e = add_expense(expenses, args.amount, args.category, args.note)
        storage.save_expenses(args.file, expenses)
        print(f'Added #{e["id"]}: {e["amount"]:.2f} to {e["category"]}')
    elif args.command == "list":
        print(list_expenses(expenses))
    elif args.command == "total":
        rows = expenses
        if args.category:
            rows = filter_by_category(expenses, args.category)
        print(f"Total: {total(rows):.2f}")
    elif args.command == "report":
        print(generate_report(expenses))


if __name__ == "__main__":
    main()
