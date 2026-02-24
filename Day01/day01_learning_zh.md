# Day 01: 檔案系統與資料盤點（EDA 專案結構）

## 今日學習重點（詳細版）
- `os` / `pathlib`：跨平台路徑操作、遞迴掃描、檔案 metadata 讀取。
- `glob`：使用 shell pattern 做批次檔案匹配。
- `json` / `csv`：同時輸出給機器流程與人工檢視。
- `collections` / `itertools` / `functools`：統計彙總、分群、累加。
- `shutil` / `tempfile`：安全備份與暫存 staging。

## 範例
### 1) 掃描專案與過濾副檔名（`os`, `pathlib`, `glob`）
```python
from pathlib import Path
import os
import glob

root = Path("mock_project")
allow = {".def", ".lef", ".gds", ".csv"}

files_a = [p for p in root.rglob("*") if p.is_file() and p.suffix.lower() in allow]
files_b = [Path(p) for p in glob.glob(str(root / "**" / "*"), recursive=True)
           if Path(p).is_file() and Path(p).suffix.lower() in allow]

print("pathlib", len(files_a), "glob", len(files_b))
if files_a:
    print("first size", os.stat(files_a[0]).st_size)
```

### 2) 輸出 manifest（`json`, `csv`）
```python
import json, csv
rows = [{"path": "layout/top.def", "size": 1024, "suffix": ".def"}]

with open("manifest.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["path", "size", "suffix"])
    w.writeheader(); w.writerows(rows)

with open("manifest.json", "w", encoding="utf-8") as f:
    json.dump(rows, f, indent=2, ensure_ascii=False)
```

### 3) 統計與備份（`collections`, `itertools`, `functools`, `shutil`, `tempfile`）
```python
from collections import Counter
from itertools import groupby
from functools import reduce
import tempfile, shutil
from pathlib import Path

rows = [{"suffix": ".def", "size": 100}, {"suffix": ".def", "size": 200}, {"suffix": ".csv", "size": 50}]
print(Counter(r["suffix"] for r in rows))
print("total", reduce(lambda a, b: a + b["size"], rows, 0))
for k, g in groupby(sorted(rows, key=lambda x: x["suffix"]), key=lambda x: x["suffix"]):
    print(k, len(list(g)))

with tempfile.TemporaryDirectory() as td:
    Path("backup").mkdir(exist_ok=True)
    Path(td, "manifest.json").write_text("{}", encoding="utf-8")
    shutil.move(str(Path(td, "manifest.json")), "backup/manifest.json")
```

## 今日題目
1. 掃描 `layout/`, `netlist/`, `report/`，只保留 `.def/.lef/.gds/.csv`。
2. 輸出 `manifest.csv` + `manifest.json`（欄位至少含 path/size/mtime/type）。
3. 產生副檔名統計、總容量、Top-10 大檔。
4. 使用 `tempfile` staging 後，再搬移到 `Day01/output`。
