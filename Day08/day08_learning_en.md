# Day 08: Parallel Processing and Job Queues

## Key Learning Points
`ThreadPoolExecutor` fits I/O-bound tasks.
`ProcessPoolExecutor` fits CPU-bound tasks.
Build retry workflow with `queue` + `threading`.

## Example
```python
from concurrent.futures import ThreadPoolExecutor

def io_job(i):
    return f"job-{i}-ok"

with ThreadPoolExecutor(max_workers=4) as ex:
    print(list(ex.map(io_job, range(5))))
```

## Exercise
Build an I/O + CPU pipeline for 200 blocks.
Retry failed jobs once and report success rate.
