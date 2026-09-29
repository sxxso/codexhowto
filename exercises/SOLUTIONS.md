# Lab solutions

Try each exercise before reading these. The point of the lab is the *process*
of working with Codex — driving it, then verifying — not the diffs themselves.
Your fix may look different and still be correct, as long as the tests pass
and behaviour is preserved.

## The planted problems, at a glance

| # | Location | Symptom | Root cause |
|---|----------|---------|------------|
| Bug 1 | `expenses.filter_by_category` | `total --category food` misses `Food` entries; test red | `==` is case-sensitive |
| Bug 2 | `expenses.total` | `test_total_rounds_to_cents` red (`0.30000000000000004`) | float sum not rounded to cents |
| Bug 3 | `storage.load_expenses` | crashes on a fresh checkout | no handling for a missing file |
| Smell | `report.generate_report` | one 40-line function | grouping + totals + formatting tangled |
| Gap | `storage.py` | no test file | untested persistence layer |

---

## Exercise 2 — missing data file

```python
def load_expenses(path):
    if not os.path.exists(path):
        return []
    with open(path) as f:
        return json.load(f)
```

(`os` is already imported.) Now `list`, `total`, and `report` all work before
the first `add`.

## Exercise 3 — the two red tests

**`total` — round to cents:**

```python
def total(expenses):
    return round(sum(e["amount"] for e in expenses), 2)
```

**`filter_by_category` — case-insensitive:**

```python
def filter_by_category(expenses, category):
    target = category.lower()
    return [e for e in expenses if e["category"].lower() == target]
```

After both fixes, `pytest -q` → `5 passed`, and `total --category food` now
agrees with the `report` breakdown (both group `Food`/`food` together).

## Exercise 4 — tests for `storage.py`

A reasonable `test_storage.py`:

```python
import storage


def test_load_missing_file_returns_empty(tmp_path):
    assert storage.load_expenses(str(tmp_path / "nope.json")) == []


def test_save_then_load_round_trips(tmp_path):
    path = str(tmp_path / "data.json")
    rows = [{"id": 1, "date": "2026-09-01", "amount": 5.0,
             "category": "food", "note": ""}]
    storage.save_expenses(path, rows)
    assert storage.load_expenses(path) == rows


def test_next_id_starts_at_one_and_increments():
    assert storage.next_id([]) == 1
    assert storage.next_id([{"id": 4}, {"id": 2}]) == 5
```

`tmp_path` keeps the tests off your real `expenses.json`.

## Exercise 5 — refactoring `generate_report`

The goal is behaviour-preserving structure, e.g. splitting into
`_totals_by_category(expenses)`, `_grand_total(totals)`,
`_biggest(totals)`, and `_format(totals, grand, biggest)`, with
`generate_report` orchestrating them. The verification is what matters:

```bash
python expenses.py report | diff - report.golden.txt   # must print nothing
```

If `diff` is silent, the refactor is safe regardless of how the helpers are
named or split.

## Exercise 6 — CSV export

One shape (there are many): a new `export` subparser taking a path, and a
`export_expenses(expenses, path)` helper using the `csv` module with a
`DictWriter` over the fixed columns. The acceptance check is a valid CSV plus
green tests — let Codex propose the structure, then confirm it runs.

---

## The meta-lesson

Notice the pattern you repeated every time:

1. **Reproduce** the failure yourself (run it, read the error).
2. **Hand Codex the concrete symptom**, not a vague "fix the bug."
3. **Constrain** it ("don't touch the tests", "behaviour must be identical").
4. **Verify** with the same command every time (`pytest`, `diff`).

That loop — reproduce, delegate with constraints, verify — is the whole game.
See [12-decision-guides](../12-decision-guides/) for choosing the safety
posture, and [11-recipes](../11-recipes/) for turning these into repeatable
workflows.

---

**Last Updated**: September 28, 2026
**Tool**: OpenAI Codex CLI (`@openai/codex`)
**Compatible Models**: GPT-5-Codex (default), GPT-5, plus OpenAI-compatible and local (OSS) models
*Part of the [codexhowto](../) guide series*
