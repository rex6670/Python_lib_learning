# Day 09: Observability and Debugging

## Key Learning Points (Detailed)
- `logging`: use structured fields (design/corner/job_id/level/message).
- `traceback`: persist full exception stack for faster RCA.
- `configparser`: configure log level and backup policy.
- `shutil`: archive failed artifacts.

## Example
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

## Exercise
1. Classify errors into parse/tool/timeout/resource and report Top3.
2. Archive input/intermediate/log artifacts on failures.
3. Export `daily_ops_summary.json`.
