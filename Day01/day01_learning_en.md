# Day 01: File System & Project Inventory (EDA Structure)

## Key Learning Points (Detailed)
- `os` / `pathlib`: cross-platform path handling, recursive scanning, metadata collection.
- `glob`: shell-style pattern matching for batch file selection.
- `json` / `csv`: dual output for automation and human review.
- `collections` / `itertools` / `functools`: aggregation, grouping, reduction.
- `shutil` / `tempfile`: safe backup and staging.

## Common Basics
- `Path.exists()`: check path existence.
- `Path.mkdir(parents=True, exist_ok=True)`: create output folders.
- `Path.rglob("*.def")`: recursively find files.

```python
from pathlib import Path
out = Path("Day01/output")
out.mkdir(parents=True, exist_ok=True)
print(out.exists())
```

## Examples
### 1) Scan and filter files (`os`, `pathlib`, `glob`)
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

### 2) Export manifest (`json`, `csv`)
```python
import json, csv
rows = [{"path": "layout/top.def", "size": 1024, "suffix": ".def"}]

with open("manifest.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["path", "size", "suffix"])
    w.writeheader(); w.writerows(rows)

with open("manifest.json", "w", encoding="utf-8") as f:
    json.dump(rows, f, indent=2)
```

### 3) Aggregate and backup (`collections`, `itertools`, `functools`, `shutil`, `tempfile`)
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

## Exercise
1. Scan `layout/`, `netlist/`, `report/` and keep only `.def/.lef/.gds/.csv`.
2. Export `manifest.csv` + `manifest.json` (path/size/mtime/type).
3. Report suffix counts, total size, and Top-10 largest files.
4. Use `tempfile` staging before moving outputs into `Day01/output`.
