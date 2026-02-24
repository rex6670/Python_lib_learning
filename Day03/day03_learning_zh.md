# Day 03: 批次呼叫外部 EDA 工具

## 今日學習重點（詳細版）
- `subprocess`：批次執行外部工具並收集 stdout/stderr。
- `signal`：處理 Ctrl+C 或中止訊號，確保流程可安全退出。
- `logging`：輸出標準化 job log（job_id/corner/status）。
- `traceback`：保存完整錯誤堆疊供 debug。

## 範例
```python
import subprocess, signal, logging, traceback

stop = False
signal.signal(signal.SIGINT, lambda s, f: globals().__setitem__("stop", True))
logging.basicConfig(filename="Day03/run.log", level=logging.INFO)

try:
    r = subprocess.run(["python", "-c", "print('mock_sta_ok')"], capture_output=True, text=True, timeout=5)
    logging.info("code=%s out=%s", r.returncode, r.stdout.strip())
except Exception:
    logging.error(traceback.format_exc())
```

## 今日題目
1. 模擬 20 個 corner jobs，包含 timeout 設定。
2. timeout 或失敗 job 輸出 `retry_jobs.csv`。
3. 產生 `summary.json`（成功率、失敗原因 Top3）。
