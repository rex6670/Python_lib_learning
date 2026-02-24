# Day 10: Capstone（EDA/CAD 自動化檢查管線）
# Day 10: Capstone (EDA/CAD Automation Pipeline)

## 今日學習重點 | Key Learning Points
- 串接 Day01~Day09 成完整流程。 / Integrate Day01~Day09 into one full pipeline.
- 用 `argparse`/`concurrent.futures` 管理 CLI 與平行執行。 / Use `argparse`/`concurrent.futures` for CLI and parallel execution.
- 輸出 `summary.csv`、`summary.json`、`run.log`。 / Produce `summary.csv`, `summary.json`, and `run.log`.

## 範例 | Example
```python
from concurrent.futures import ThreadPoolExecutor

def check_job(i):
    return {"job_id": i, "status": "PASS" if i % 7 else "FAIL"}

with ThreadPoolExecutor(max_workers=4) as ex:
    rows = list(ex.map(check_job, range(50)))
print(rows[:3])
```

## 今日題目 | Exercise
1. 支援 full/incremental 模式。 / Support full and incremental modes.
2. 比較全量與增量執行時間。 / Compare runtime between full and incremental runs.
