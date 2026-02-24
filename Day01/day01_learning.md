# Day 01: 檔案系統與資料盤點（EDA 專案結構）

## 今日學習重點（進階版）

### 1) 用 `pathlib` + `glob` + `os` 建立可重現的檔案盤點
- `pathlib.Path.rglob()`：跨平台遞迴掃描。
- `glob.glob(..., recursive=True)`：當你要寫 shell-like pattern 時很好用。
- `os.stat()` / `Path.stat()`：拿檔案大小、mtime、inode 供後續追蹤。

### 2) 用 `json` / `csv` 做雙格式輸出（機器 + 人可讀）
- `json`：流程中方便程式讀寫與 API 交換。
- `csv`：EDA 團隊常用 Excel/BI 工具檢視，對 review 友善。

### 3) 用 `collections` / `itertools` / `functools` 做資料彙總
- `Counter`：副檔名統計。
- `groupby`：依 layer / suffix 分群。
- `reduce`：做總大小累積（示範函數式寫法）。

### 4) `shutil` + `tempfile` 做安全備份與 staging
- 先把檔案收斂到臨時資料夾，再原子性搬移到 output。
- 避免半成品輸出污染正式目錄。

## 範例（補齊多個 lib）

### A. 掃描與過濾（`pathlib`, `glob`, `os`）
```python
from pathlib import Path
import glob
import os

root = Path("mock_project")
allow = {".def", ".lef", ".gds", ".csv"}

files_a = [p for p in root.rglob("*") if p.is_file() and p.suffix.lower() in allow]
files_b = [Path(p) for p in glob.glob(str(root / "**" / "*"), recursive=True)
           if Path(p).is_file() and Path(p).suffix.lower() in allow]

print("pathlib count:", len(files_a), "glob count:", len(files_b))
print("first file size:", os.stat(files_a[0]).st_size if files_a else 0)
```

### B. 輸出 manifest（`json`, `csv`）
```python
import csv
import json

rows = [{"path": "layout/top.def", "size": 1024, "suffix": ".def"}]

with open("manifest.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["path", "size", "suffix"])
    w.writeheader(); w.writerows(rows)

with open("manifest.json", "w", encoding="utf-8") as f:
    json.dump(rows, f, indent=2, ensure_ascii=False)
```

### C. 統計與分群（`collections`, `itertools`, `functools`）
```python
from collections import Counter
from itertools import groupby
from functools import reduce

rows = [
    {"suffix": ".def", "size": 100},
    {"suffix": ".def", "size": 200},
    {"suffix": ".csv", "size": 50},
]

print(Counter(r["suffix"] for r in rows))

rows_sorted = sorted(rows, key=lambda x: x["suffix"])
for k, grp in groupby(rows_sorted, key=lambda x: x["suffix"]):
    print(k, len(list(grp)))

total = reduce(lambda a, b: a + b["size"], rows, 0)
print("total bytes:", total)
```

### D. 備份與暫存（`shutil`, `tempfile`）
```python
from pathlib import Path
import shutil
import tempfile

src = Path("manifest.json")
with tempfile.TemporaryDirectory() as td:
    stage = Path(td) / src.name
    shutil.copy2(src, stage)
    Path("backup").mkdir(exist_ok=True)
    shutil.move(str(stage), "backup/manifest.json")
```

## 今日題目（EDA/CAD）
1. 掃描 `layout/`, `netlist/`, `report/`，只收 `.def/.lef/.gds/.csv`。
2. 產生 `manifest.csv` + `manifest.json`（包含 path/size/mtime/type）。
3. 輸出副檔名統計、總容量、最大檔案 Top 10。
4. 以 `tempfile` staging 後再搬移到 `Day01/output/`。
