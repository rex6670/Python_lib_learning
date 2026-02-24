# Day 08: 平行處理與任務佇列
# Day 08: Parallel Processing and Job Queues

## 今日學習重點 | Key Learning Points
- `ThreadPoolExecutor` 適合 I/O 密集。 / `ThreadPoolExecutor` fits I/O-bound tasks.
- `ProcessPoolExecutor` 適合 CPU 密集。 / `ProcessPoolExecutor` fits CPU-bound tasks.
- `queue` + `threading` 做重試機制。 / Build retry workflow with `queue` + `threading`.

## 範例 | Example
```python
from concurrent.futures import ThreadPoolExecutor

def io_job(i):
    return f"job-{i}-ok"

with ThreadPoolExecutor(max_workers=4) as ex:
    print(list(ex.map(io_job, range(5))))
```

## 今日題目 | Exercise
1. 200 個 block 分成 I/O + CPU pipeline。 / Build an I/O + CPU pipeline for 200 blocks.
2. 失敗任務重試一次並統計成功率。 / Retry failed jobs once and report success rate.
