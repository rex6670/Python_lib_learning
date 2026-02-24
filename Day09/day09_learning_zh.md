# Day 09: 可維運性與除錯

## 今日學習重點
- `logging` 建立標準欄位（design/corner/job_id）。
- `traceback` 追蹤異常堆疊。
- `configparser` 控制 log level，`shutil` 封存失敗工件。

## 範例
```python
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logging.info("design=top_cpu corner=TT job=42 status=start")
```

## 今日題目
1. 分類錯誤類型 Top3。
2. 自動封存失敗資料到 `failed_artifacts/`。
