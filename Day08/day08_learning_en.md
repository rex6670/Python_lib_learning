# Day 08: Parallel Processing and Job Queues

## Key Learning Points (Detailed)
- `threading` / `ThreadPoolExecutor`: for I/O-bound tasks (read/write/network).
- `multiprocessing` / `ProcessPoolExecutor`: for CPU-bound tasks (geometry/rule checks).
- `queue`: retry control and back-pressure handling.
- `concurrent.futures`: unified API for thread/process parallelism.

## Common Basics
- `ThreadPoolExecutor`: parallel I/O tasks.
- `ProcessPoolExecutor`: parallel CPU tasks.
- `queue.Queue`: producer/consumer coordination.

```python
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=2) as ex:
    print(list(ex.map(lambda i: i*i, [1,2,3])))
```

## Example
```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import queue, threading

# I/O task
def io_job(i):
    return f"io-{i}-ok"

# CPU task
def cpu_job(i):
    s = 0
    for x in range(200000):
        s += (x * i) % 97
    return s

with ThreadPoolExecutor(max_workers=4) as ex:
    print(list(ex.map(io_job, range(5))))
with ProcessPoolExecutor(max_workers=2) as ex:
    print(list(ex.map(cpu_job, range(3))))

q = queue.Queue()
for j in ["blk1", "blk2"]: q.put(j)

def worker():
    while not q.empty():
        job = q.get(); print("retry", job); q.task_done()
threading.Thread(target=worker).start(); q.join()
```

## Exercise
1. Split 200 blocks into I/O preprocessing + CPU validation stages.
2. Retry failed jobs once via `queue`.
3. Report throughput, average latency, and pass rate.
