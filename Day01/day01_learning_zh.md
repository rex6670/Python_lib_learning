# Day 01: 檔案系統與資料盤點（EDA 專案結構）

## 今日學習重點
- 使用 `pathlib`/`glob` 掃描目錄，建立可重現清單。  
- 用 `json` + `csv` 同時輸出，兼顧機器與人工檢視。  
- 用 `collections.Counter` 做副檔名統計。  

## 範例
```python
from pathlib import Path
from collections import Counter

root = Path("mock_project")
allow = {".def", ".lef", ".gds", ".csv"}
files = [p for p in root.rglob("*") if p.is_file() and p.suffix.lower() in allow]
print(Counter(p.suffix.lower() for p in files))
```

## 今日題目
1. 只盤點 `.def/.lef/.gds/.csv`。
2. 輸出 `manifest.csv`、`manifest.json`。
3. 依副檔名統計數量與容量。
