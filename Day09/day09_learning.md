# Day 09: 可維運性與除錯
# Day 09: Observability and Debugging

## 今日學習重點 | Key Learning Points
- `logging` 建立標準欄位（design/corner/job_id）。 / Build structured logs with design/corner/job_id.
- `traceback` 追蹤異常堆疊。 / Capture full exception stack with `traceback`.
- `configparser` 控制 log level，`shutil` 封存失敗工件。 / Configure log level with `configparser` and archive artifacts with `shutil`.

## 範例 | Example
```python
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logging.info("design=top_cpu corner=TT job=42 status=start")
```

## 今日題目 | Exercise
1. 分類錯誤類型 Top3。 / Report Top3 error categories.
2. 自動封存失敗資料到 `failed_artifacts/`。 / Archive failed artifacts into `failed_artifacts/`.
