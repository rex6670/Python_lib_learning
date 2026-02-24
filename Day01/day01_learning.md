# Day 01: 檔案系統與資料盤點（EDA 專案結構）

## 今日學習重點
- 使用 `pathlib`/`glob` 掃描目錄，建立可追蹤的檔案清單。
- 使用 `csv`、`json` 輸出 inventory，供後續流程重用。
- 使用 `collections.Counter` 做檔案類型統計。

## 範例
```python
from pathlib import Path
from collections import Counter

root = Path("mock_project")
files = [p for p in root.rglob("*") if p.is_file()]
stats = Counter(p.suffix.lower() for p in files)
print("type stats:", stats)
```

## 今日題目（EDA/CAD）
1. 只收集 `.def/.lef/.gds/.csv`。
2. 產生 `manifest.json`（name/size/mtime/type）。
3. 依副檔名分類複製到 `backup/`。
