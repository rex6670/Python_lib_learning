# Day 08: 平行處理與任務佇列

## 今日學習重點（詳細版）
- `threading` / `ThreadPoolExecutor`：I/O 密集工作（讀檔、寫檔、網路請求）。
- `multiprocessing` / `ProcessPoolExecutor`：CPU 密集工作（幾何計算、規則檢查）。
- `queue`：失敗任務重試與背壓控制。
- `concurrent.futures`：統一 thread/process 平行抽象。

## 範例
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

## 今日題目
1. 200 個 block 分成 I/O 前處理 + CPU 核心檢查。
2. 失敗任務回 `queue` 重試一次。
3. 報告吞吐量、平均 latency、成功率。
