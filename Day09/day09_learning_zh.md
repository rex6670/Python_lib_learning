# Day 09: 可維運性與除錯

## 今日學習重點（詳細版）
- `logging`：統一欄位格式（design/corner/job_id/level/message）。
- `traceback`：將異常堆疊落盤，縮短 RCA 時間。
- `configparser`：用設定檔控制 log level、備份策略。
- `shutil`：失敗工件封存。

## 範例
```python
import logging, traceback, configparser, shutil
from pathlib import Path

cfg = configparser.ConfigParser(); cfg.read("ops.ini")
log_level = getattr(logging, cfg.get("logging", "level", fallback="INFO"))
logging.basicConfig(filename="Day09/run.log", level=log_level)

try:
    1 / 0
except Exception:
    logging.error("failed\n%s", traceback.format_exc())

Path("Day09/failed_artifacts").mkdir(parents=True, exist_ok=True)
shutil.copy2("Day09/run.log", "Day09/failed_artifacts/run.log")
```

## 今日題目
1. 將錯誤分類為 parse/tool/timeout/resource 四類並統計 Top3。
2. 失敗時封存輸入檔、中間檔、log。
3. 輸出 `daily_ops_summary.json`。
