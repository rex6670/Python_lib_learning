# Day 03: 批次呼叫外部 EDA 工具

## 今日學習重點
- `subprocess` 批次執行工具。
- `signal` 處理中斷、`traceback` 保存錯誤。
- `logging` 建立可追溯 job log。

## 範例
```python
import subprocess
r = subprocess.run(["python", "-c", "print('STA done')"], capture_output=True, text=True, timeout=5)
print(r.returncode, r.stdout.strip())
```

## 今日題目
1. 模擬 20 個 corner jobs。
2. 超時任務輸出 `retry_jobs.csv`。
