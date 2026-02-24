# Day 08: 平行處理與任務佇列

## 今日學習重點（進階版）
- `threading` / `ThreadPoolExecutor`：I/O 密集（讀檔、寫報表）。
- `multiprocessing` / `ProcessPoolExecutor`：CPU 密集（計算檢查）。
- `queue`：failed job 回補重試。
- 串接 Day03 runner 概念，建立可重跑的 job orchestration。

## 範例（補齊 lib）

### A. Thread pool（I/O）
```python
from concurrent.futures import ThreadPoolExecutor

def io_job(i):
    return f"io-{i}-ok"

with ThreadPoolExecutor(max_workers=8) as ex:
    print(list(ex.map(io_job, range(5))))
```

### B. Process pool（CPU）
```python
from concurrent.futures import ProcessPoolExecutor

def cpu_job(i):
    s = 0
    for x in range(200000):
        s += (x * i) % 97
    return s

with ProcessPoolExecutor(max_workers=4) as ex:
    print(list(ex.map(cpu_job, range(4))))
```

### C. 重試佇列（`queue`, `threading`）
```python
import queue
import threading

q = queue.Queue()
for j in ["blk1", "blk2"]:
    q.put(j)

def worker():
    while not q.empty():
        j = q.get()
        try:
            print("run", j)
        finally:
            q.task_done()

threading.Thread(target=worker).start()
q.join()
```

## 今日題目（EDA/CAD）
1. 200 個 block：I/O 前處理用 ThreadPool、檢查核心用 ProcessPool。
2. 失敗任務回 queue 重試一次。
3. 輸出 job latency 分布與成功率。
