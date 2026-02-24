# Day 10: Capstone (EDA/CAD Automation Pipeline)

## Key Learning Points
Integrate Day01~Day09 into one full pipeline.
Use `argparse`/`concurrent.futures` for CLI and parallel execution.
Produce `summary.csv`, `summary.json`, and `run.log`.

## Example
```python
from concurrent.futures import ThreadPoolExecutor

def check_job(i):
    return {"job_id": i, "status": "PASS" if i % 7 else "FAIL"}

with ThreadPoolExecutor(max_workers=4) as ex:
    rows = list(ex.map(check_job, range(50)))
print(rows[:3])
```

## Exercise
Support full and incremental modes.
Compare runtime between full and incremental runs.
