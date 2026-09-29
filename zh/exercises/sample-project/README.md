# 示例项目:`expenses` CLI

一个刻意做得很小、也刻意留了毛病的 Python 命令行记账工具。它是
[codexhowto 实验课](../README.md)的练手场——内置了几个人为埋下的 bug、一个
没有测试的模块,以及一个亟需重构的函数。你的任务是用 Codex 把它们全部修好。

## 运行

```bash
cd sample-project
python expenses.py add 12.50 food "lunch"
python expenses.py add 40 travel "train"
python expenses.py list
python expenses.py total
python expenses.py total --category food
python expenses.py report
```

数据写入当前目录下的 `expenses.json`(可用 `--file` 覆盖)。

## 运行测试

```bash
pip install -r requirements.txt
pytest -q
```

有几个测试**故意是红的**——它们描述了代码应有的行为,而埋下的 bug 让它们失败。
不要改测试来让它们通过;要改的是代码。

## 文件

| 文件 | 是什么 |
|------|--------|
| `expenses.py` | CLI + 核心逻辑(`add_expense`、`filter_by_category`、`total`……) |
| `storage.py` | JSON 读写——**目前没有测试** |
| `report.py` | `generate_report`——一个过于臃肿、待重构的函数 |
| `test_expenses.py` | 核心逻辑的测试(部分故意失败) |
| `requirements.txt` | `pytest` |

回到[实验课指南](../README.md)开始逐个练习。
