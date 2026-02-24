# Day 10: Capstone（EDA/CAD 自動化檢查管線）

## 今日學習重點
- 串接 Day01~Day09 成完整流程。
- 用 `argparse`/`concurrent.futures` 管理 CLI 與平行執行。
- 輸出 `summary.csv`、`summary.json`、`run.log`。

## 範例
```python
from concurrent.futures import ThreadPoolExecutor

def check_job(i):
    return {"job_id": i, "status": "PASS" if i % 7 else "FAIL"}

with ThreadPoolExecutor(max_workers=4) as ex:
    rows = list(ex.map(check_job, range(50)))
print(rows[:3])
```

## 今日題目
1. 支援 full/incremental 模式。
2. 比較全量與增量執行時間。
