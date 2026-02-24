# Day 08: 平行處理與任務佇列

## 今日學習重點
- `ThreadPoolExecutor` 適合 I/O 密集。
- `ProcessPoolExecutor` 適合 CPU 密集。
- `queue` + `threading` 做重試機制。

## 範例
```python
from concurrent.futures import ThreadPoolExecutor

def io_job(i):
    return f"job-{i}-ok"

with ThreadPoolExecutor(max_workers=4) as ex:
    print(list(ex.map(io_job, range(5))))
```

## 今日題目
1. 200 個 block 分成 I/O + CPU pipeline。
2. 失敗任務重試一次並統計成功率。
