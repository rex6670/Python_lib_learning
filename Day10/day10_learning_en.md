# Day 10: Capstone (EDA/CAD Automation Pipeline)

## Key Learning Points (Detailed)
- `argparse`: complete CLI (input/output/workers/mode).
- `concurrent.futures`: run 50+ jobs in parallel.
- `json` / `csv`: output summaries and status counts.
- `logging`: end-to-end observability.
- Integrate Day01~Day09: inventory → parse/hash → runner → QoR → spatial → report.

## Example
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

## Exercise
1. Support both `full` and `incremental` modes (hash-based rerun decision).
2. Process at least 50 jobs and generate `summary.csv`, `summary.json`, and `run.log`.
3. Add a performance note: full vs incremental runtime and main bottlenecks.
