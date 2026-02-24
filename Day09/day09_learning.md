# Day 09: 可維運性與除錯

## 今日學習重點（進階版）
- `logging`：統一 log 格式（timestamp/design/corner/job_id/level/message）。
- `traceback`：失敗可追蹤，支援快速 RCA。
- `configparser`：讓 log level / backup policy 可配置。
- `shutil`：失敗工件自動封存。

## 範例（補齊 lib）

### A. 可觀測 logging（`logging`）
```python
import logging

logging.basicConfig(
    filename="run.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s design=%(design)s corner=%(corner)s job=%(job)s msg=%(message)s",
)
logger = logging.LoggerAdapter(logging.getLogger(__name__), {"design": "top_cpu", "corner": "TT", "job": 42})
logger.info("start")
```

### B. 例外追蹤（`traceback`）
```python
import traceback

try:
    1 / 0
except Exception:
    logger.error("failed\n%s", traceback.format_exc())
```

### C. 設定與封存（`configparser`, `shutil`）
```python
import configparser
import shutil
from pathlib import Path

cfg = configparser.ConfigParser()
cfg.read("ops.ini")
Path("failed_artifacts").mkdir(exist_ok=True)
shutil.copy2("run.log", "failed_artifacts/run.log")
```

## 今日題目（EDA/CAD）
1. 錯誤分類（timeout/parse/error/tool-crash）統計 Top3。
2. 失敗 job 的輸入、log、中間檔自動封存。
3. 生成每日運維摘要（成功率、平均耗時、Top errors）。
