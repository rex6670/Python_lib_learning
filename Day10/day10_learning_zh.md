# Day 10: Capstone（EDA/CAD 自動化檢查管線）

## 今日學習重點（詳細版）
- `argparse`：提供完整 CLI（input/output/workers/mode）。
- `concurrent.futures`：平行跑 50+ jobs。
- `json` / `csv`：輸出 summary 與 status 統計。
- `logging`：整合流水線可觀測性。
- 串接 Day01~Day09：inventory → parse/hash → runner → QoR → spatial → report。

## 基礎常用用法
- `argparse`：接收執行參數。
- `ThreadPoolExecutor.map()`：平行跑 job。
- `json.dump` / `csv.DictWriter`：輸出結果。

```python
import json
print(json.dumps({"ok": True}))
```

## 範例
```python
import argparse, csv, json, logging
from concurrent.futures import ThreadPoolExecutor

p = argparse.ArgumentParser()
p.add_argument("--workers", type=int, default=4)
args = p.parse_args([])
logging.basicConfig(filename="Day10/run.log", level=logging.INFO)

def check_job(i):
    status = "PASS" if i % 7 else "FAIL"
    return {"job_id": i, "status": status}

with ThreadPoolExecutor(max_workers=args.workers) as ex:
    rows = list(ex.map(check_job, range(50)))

with open("Day10/summary.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["job_id", "status"])
    w.writeheader(); w.writerows(rows)
json.dump(rows, open("Day10/summary.json", "w", encoding="utf-8"), indent=2)
```

## 今日題目
1. 支援 `full` / `incremental` 兩種模式（用 hash 判斷重跑）。
2. 至少處理 50 jobs，輸出 `summary.csv`、`summary.json`、`run.log`。
3. 附加效能報告：全量 vs 增量時間差、主要瓶頸。
