# Day 03: 批次呼叫外部 EDA 工具

## 今日學習重點
- 使用 `subprocess.run` 執行外部命令。
- 使用 `logging` 記錄每個 job 的 stdout/stderr。
- 使用 timeout 與 `traceback` 增加除錯可讀性。

## 範例
```python
import subprocess

cmd = ["python", "-c", "print('mock_sta_ok')"]
out = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
print(out.stdout.strip())
```

## 今日題目（EDA/CAD）
1. 模擬執行 20 個 corner job。
2. 任一 job 超時時標記失敗並寫入 `retry_jobs.csv`。
3. 將錯誤訊息彙整成 `run.log`。
