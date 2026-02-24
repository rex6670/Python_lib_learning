# Day 01: File System & Project Inventory (EDA Structure)

## Key Learning Points
- Use `pathlib`/`glob` to scan directories and build reproducible inventories.
- Export both `json` and `csv` for automation and human review.
- Use `collections.Counter` for suffix statistics.

## Example
```python
from pathlib import Path
from collections import Counter

root = Path("mock_project")
allow = {".def", ".lef", ".gds", ".csv"}
files = [p for p in root.rglob("*") if p.is_file() and p.suffix.lower() in allow]
print(Counter(p.suffix.lower() for p in files))
```

## Exercise
Inventory only `.def/.lef/.gds/.csv`.
Export `manifest.csv` and `manifest.json`.
Report count and size by suffix.
