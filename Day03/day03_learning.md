# Day 03: 批次呼叫外部 EDA 工具
# Day 03: Batch Execution for External EDA Tools

## 今日學習重點 | Key Learning Points
- `subprocess` 批次執行工具。 / Run tools in batch with `subprocess`.
- `signal` 處理中斷、`traceback` 保存錯誤。 / Handle interruption with `signal` and capture errors via `traceback`.
- `logging` 建立可追溯 job log。 / Build traceable per-job logs using `logging`.

## 範例 | Example
```python
import subprocess
r = subprocess.run(["python", "-c", "print('STA done')"], capture_output=True, text=True, timeout=5)
print(r.returncode, r.stdout.strip())
```

## 今日題目 | Exercise
1. 模擬 20 個 corner jobs。 / Simulate 20 corner jobs.
2. 超時任務輸出 `retry_jobs.csv`。 / Write timeout jobs into `retry_jobs.csv`.
