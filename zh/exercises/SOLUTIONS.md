# 实验课参考答案

每个练习都先自己做,再看这里。实验课的重点是与 Codex 协作的*过程*——驱动它、
再验证——而不是这些 diff 本身。只要测试通过、行为保持一致,你的改法和这里不同
也完全正确。

## 埋下的问题一览

| # | 位置 | 症状 | 根因 |
|---|------|------|------|
| Bug 1 | `expenses.filter_by_category` | `total --category food` 漏掉 `Food` 的记录;测试红 | `==` 区分大小写 |
| Bug 2 | `expenses.total` | `test_total_rounds_to_cents` 红(`0.30000000000000004`) | 浮点求和未四舍五入到分 |
| Bug 3 | `storage.load_expenses` | 全新检出即崩溃 | 未处理文件不存在的情况 |
| 坏味道 | `report.generate_report` | 一个 40 行的函数 | 分组 + 求和 + 格式化纠缠在一起 |
| 缺口 | `storage.py` | 没有测试文件 | 持久化层没被测试覆盖 |

---

## 练习 2 —— 数据文件缺失

```python
def load_expenses(path):
    if not os.path.exists(path):
        return []
    with open(path) as f:
        return json.load(f)
```

(`os` 已经导入。)现在 `list`、`total`、`report` 在第一次 `add` 之前都能正常
工作。

## 练习 3 —— 两个红测试

**`total` —— 四舍五入到分:**

```python
def total(expenses):
    return round(sum(e["amount"] for e in expenses), 2)
```

**`filter_by_category` —— 不区分大小写:**

```python
def filter_by_category(expenses, category):
    target = category.lower()
    return [e for e in expenses if e["category"].lower() == target]
```

两处修好后,`pytest -q` → `5 passed`,并且 `total --category food` 现在与
`report` 的分类汇总一致了(两者都把 `Food`/`food` 归为一类)。

## 练习 4 —— 给 `storage.py` 写测试

一个合理的 `test_storage.py`:

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

`tmp_path` 让测试不碰你真实的 `expenses.json`。

## 练习 5 —— 重构 `generate_report`

目标是保持行为不变的结构调整,例如拆成 `_totals_by_category(expenses)`、
`_grand_total(totals)`、`_biggest(totals)`、`_format(totals, grand, biggest)`,
由 `generate_report` 负责串起来。真正重要的是验证:

```bash
python expenses.py report | diff - report.golden.txt   # 必须无输出
```

只要 `diff` 无输出,不论辅助函数怎么命名、怎么拆,重构就是安全的。

## 练习 6 —— CSV 导出

一种写法(还有很多):新增一个接收路径参数的 `export` 子命令,以及一个用 `csv`
模块的 `DictWriter` 按固定列写出的 `export_expenses(expenses, path)` 辅助函数。
验收标准是一份合法 CSV 加上全绿的测试——让 Codex 提出结构,你再确认它能跑。

---

## 元层面的收获

注意你每次都在重复同一个套路:

1. **自己复现**故障(跑一遍,读错误)。
2. **把具体症状交给 Codex**,而不是含糊的"修一下 bug"。
3. **给它加约束**("别动测试"、"行为必须完全一致")。
4. 每次都用同一条命令**验证**(`pytest`、`diff`)。

这个循环——复现、带约束地委派、验证——就是全部要领。选择安全姿态见
[12-decision-guides](../12-decision-guides/),把它们变成可复用的工作流见
[11-recipes](../11-recipes/)。

---

**最后更新**: September 28, 2026
**工具**: OpenAI Codex CLI (`@openai/codex`)
**兼容模型**: GPT-5-Codex (默认), GPT-5, 以及 OpenAI 兼容和本地 (OSS) 模型
*[codexhowto](../) 指南系列的一部分*
