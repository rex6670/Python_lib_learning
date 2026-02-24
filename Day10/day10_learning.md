# Day 10: Capstone（EDA/CAD 自動化檢查管線）

## 今日學習重點（進階版）
- 把 Day01~Day09 串成完整 pipeline：
  1. inventory
  2. parse/hash
  3. runner
  4. QoR compare
  5. 1M object analysis
  6. observability
- `concurrent.futures`：平行跑 jobs。
- `argparse`：輸入/輸出/worker/模式（full/incremental）。
- `json`/`csv`：輸出 summary 給人與機器。

## 範例（整合多 lib）
```python
import argparse
import json
import csv
from concurrent.futures import ThreadPoolExecutor

parser = argparse.ArgumentParser()
parser.add_argument("--workers", type=int, default=4)
args = parser.parse_args()

def check_job(i):
    return {"job_id": i, "status": "PASS" if i % 7 else "FAIL"}

with ThreadPoolExecutor(max_workers=args.workers) as ex:
    rows = list(ex.map(check_job, range(50)))

with open("summary.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["job_id", "status"])
    w.writeheader(); w.writerows(rows)

with open("summary.json", "w", encoding="utf-8") as f:
    json.dump(rows, f, indent=2)
```

## 今日題目（EDA/CAD）
1. 至少 50 jobs，支援 `--workers`。
2. 支援 full/incremental（以 hash 判斷是否重跑）。
3. 產生 `summary.csv`, `summary.json`, `run.log`, `status_count.csv`。
4. 附一段結論：全量與增量時間差、主要瓶頸、下一步優化。
