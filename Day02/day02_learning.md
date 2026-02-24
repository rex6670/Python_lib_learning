# Day 02: 命名規則解析與資料指紋

## 今日學習重點（進階版）
- `re`：用命名群組解析 `design/version/corner/voltage/temp`，同時處理不合法命名。
- `datetime` + `time`：產生 parse timestamp、量測 parse throughput。
- `hashlib`：SHA-256 做增量判斷與去重。

## 範例（補齊 lib）

### A. 命名解析（`re`）
```python
import re

pat = re.compile(
    r"(?P<design>[A-Za-z0-9_]+)_v(?P<version>\d+)_(?P<corner>TT|SS|FF)_(?P<volt>\d+p\d+V)_(?P<temp>-?\d+C)\.def$"
)

name = "top_cpu_v12_FF_0p72V_125C.def"
m = pat.match(name)
print(m.groupdict() if m else "invalid")
```

### B. 時間與效能（`datetime`, `time`）
```python
from datetime import datetime
import time

start = time.perf_counter()
# parse many names ...
elapsed = time.perf_counter() - start
print("parsed_at:", datetime.now().isoformat(timespec="seconds"))
print("elapsed_s:", round(elapsed, 6))
```

### C. 檔案指紋（`hashlib`）
```python
import hashlib
from pathlib import Path

p = Path("layout/top.def")
h = hashlib.sha256()
with p.open("rb") as f:
    for chunk in iter(lambda: f.read(1024 * 1024), b""):
        h.update(chunk)
print(h.hexdigest())
```

## 今日題目（EDA/CAD）
1. 解析 500 筆命名，輸出合法/不合法比例。
2. 合法資料輸出 `parsed_manifest.json`。
3. 建立 `hash -> [paths]` 映射，找重複檔。
4. 輸出 parse throughput（檔案數/秒）。
