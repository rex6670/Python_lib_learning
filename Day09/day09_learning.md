# Day 09: 可維運性與除錯

## 今日學習重點
- 使用 `logging` 建立標準格式（design/corner/job_id）。
- 使用 `traceback` 追蹤失敗堆疊。
- 使用 `shutil`/`pathlib` 做失敗工件備份。

## 範例
```python
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logging.info("design=top_cpu corner=TT job=42 status=start")
```

## 今日題目（EDA/CAD）
1. 失敗時自動備份到 `failed_artifacts/`。
2. 建立錯誤類型統計（Top 3）。
3. 產出人可讀每日 summary。
