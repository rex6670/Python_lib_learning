# Day 03: 批次呼叫外部 EDA 工具

## 今日學習重點（進階版）
- `subprocess`：批次執行 mock STA/DRC/LVS。
- `signal`：超時或中斷時清理子程序。
- `logging`：建立 job 級別的可追蹤紀錄。
- `traceback`：錯誤時保存完整 call stack。

## 範例（補齊 lib）

### A. 基本執行（`subprocess`）
```python
import subprocess

cmd = ["python", "-c", "print('STA done')"]
r = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
print(r.returncode, r.stdout.strip())
```

### B. 設定訊號處理（`signal`）
```python
import signal

stop = False

def on_sigint(signum, frame):
    global stop
    stop = True

signal.signal(signal.SIGINT, on_sigint)
```

### C. 錯誤追蹤（`logging`, `traceback`）
```python
import logging
import traceback

logging.basicConfig(filename="run.log", level=logging.INFO)
try:
    1 / 0
except Exception:
    logging.error("job failed")
    logging.error(traceback.format_exc())
```

## 今日題目（EDA/CAD）
1. 模擬 20 個 corner jobs（TT/SS/FF + mode）。
2. 每個 job 記錄 cmd/return_code/stdout/stderr。
3. timeout job 進 `retry_jobs.csv`。
4. 失敗摘要輸出 `Day03/summary.json`。
