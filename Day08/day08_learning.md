# Day 08: 平行處理與任務佇列

## 今日學習重點
- I/O 密集任務使用 `ThreadPoolExecutor`。
- CPU 密集任務使用 `ProcessPoolExecutor`。
- 使用 `queue` 管理重試流程。

## 範例
```python
from concurrent.futures import ThreadPoolExecutor

def run_job(i):
    return f"job-{i}-ok"

with ThreadPoolExecutor(max_workers=4) as ex:
    print(list(ex.map(run_job, range(5))))
```

## 今日題目（EDA/CAD）
1. 平行處理 200 個 block 檢查任務。
2. 失敗任務回佇列重試一次。
3. 彙整成功率與平均耗時。
