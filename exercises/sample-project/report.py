"""Report generation for the expense tracker.

The single function below works, but it does far too much in one place:
grouping, totaling, sorting, finding the biggest category, and formatting
are all tangled together. Refactoring it into small, testable helpers
(without changing its output) is one of the lab exercises.
"""


def generate_report(expenses):
    if not expenses:
        return "No expenses recorded yet."

    # group amounts by category (case-insensitively)
    groups = {}
    for e in expenses:
        key = e["category"].lower()
        if key not in groups:
            groups[key] = []
        groups[key].append(e["amount"])

    # total per category
    totals = {}
    for key in groups:
        s = 0.0
        for amt in groups[key]:
            s = s + amt
        totals[key] = round(s, 2)

    # grand total
    grand = 0.0
    for key in totals:
        grand = grand + totals[key]
    grand = round(grand, 2)

    # biggest category
    biggest = None
    biggest_amt = -1.0
    for key in totals:
        if totals[key] > biggest_amt:
            biggest_amt = totals[key]
            biggest = key

    # build the text report, sorted by amount descending
    lines = []
    lines.append("Expense report")
    lines.append("=" * 32)
    ordered = sorted(totals.items(), key=lambda kv: kv[1], reverse=True)
    for key, amt in ordered:
        pct = round(amt / grand * 100, 1) if grand else 0.0
        label = key.capitalize()
        lines.append(f"{label:<16} {amt:>8.2f}  ({pct:>5.1f}%)")
    lines.append("-" * 32)
    lines.append(f'{"Total":<16} {grand:>8.2f}')
    lines.append("")
    lines.append(f"Biggest category: {biggest.capitalize()} ({biggest_amt:.2f})")
    return "\n".join(lines)
