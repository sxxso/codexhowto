# Sample project: `expenses` CLI

A deliberately small, deliberately imperfect Python command-line expense
tracker. It is the playground for the [codexhowto lab](../README.md) — it
ships with a few planted bugs, an untested module, and one function that is
crying out for a refactor. Your job is to fix it all with Codex.

## Run it

```bash
cd sample-project
python expenses.py add 12.50 food "lunch"
python expenses.py add 40 travel "train"
python expenses.py list
python expenses.py total
python expenses.py total --category food
python expenses.py report
```

Data is written to `expenses.json` in the current directory (override with
`--file`).

## Run the tests

```bash
pip install -r requirements.txt
pytest -q
```

Several tests are **red on purpose** — they describe how the code should
behave, and the planted bugs break them. Do not edit the tests to make them
pass; fix the code.

## Files

| File | What it is |
|------|------------|
| `expenses.py` | CLI + core logic (`add_expense`, `filter_by_category`, `total`, …) |
| `storage.py` | JSON load/save — **has no tests yet** |
| `report.py` | `generate_report` — one overgrown function to refactor |
| `test_expenses.py` | Tests for the core logic (some intentionally failing) |
| `requirements.txt` | `pytest` |

Head back to the [lab guide](../README.md) for the guided exercises.
