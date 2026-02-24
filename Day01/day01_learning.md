# Day 01: 檔案系統與資料盤點（EDA 專案結構）
# Day 01: File System & Project Inventory (EDA Structure)

## 今日學習重點 | Key Learning Points
- 使用 `pathlib`/`glob` 掃描目錄，建立可重現清單。  
  Use `pathlib`/`glob` to scan directories and build reproducible inventories.
- 用 `json` + `csv` 同時輸出，兼顧機器與人工檢視。  
  Export both `json` and `csv` for automation and human review.
- 用 `collections.Counter` 做副檔名統計。  
  Use `collections.Counter` for suffix statistics.

## 範例 | Example
```python
from pathlib import Path
from collections import Counter

root = Path("mock_project")
allow = {".def", ".lef", ".gds", ".csv"}
files = [p for p in root.rglob("*") if p.is_file() and p.suffix.lower() in allow]
print(Counter(p.suffix.lower() for p in files))
```

## 今日題目 | Exercise
1. 只盤點 `.def/.lef/.gds/.csv`。 / Inventory only `.def/.lef/.gds/.csv`.
2. 輸出 `manifest.csv`、`manifest.json`。 / Export `manifest.csv` and `manifest.json`.
3. 依副檔名統計數量與容量。 / Report count and size by suffix.
