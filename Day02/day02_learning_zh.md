# Day 02: 命名規則解析與資料指紋

## 今日學習重點（詳細版）
- `re`：使用命名群組解析檔名欄位與驗證合法格式。
- `datetime` / `time`：記錄解析時間與吞吐量（檔案/秒）。
- `hashlib`：SHA-256 指紋用於增量流程與重複檢查。

## 基礎常用用法
- `re.match()`：從字串開頭做格式比對。
- `datetime.now().isoformat()`：標準時間字串。
- `hashlib.sha256(data).hexdigest()`：快速產生摘要。

```python
import re, hashlib
print(bool(re.match(r"^top_", "top_cpu")))
print(hashlib.sha256(b"abc").hexdigest()[:8])
```

## 範例
```python
import re, time, hashlib
from datetime import datetime

pat = re.compile(r"(?P<design>[A-Za-z0-9_]+)_v(?P<ver>\d+)_(?P<corner>TT|SS|FF)_(?P<volt>\d+p\d+V)_(?P<temp>-?\d+C)\.def$")
name = "top_cpu_v12_FF_0p72V_125C.def"

t0 = time.perf_counter()
m = pat.match(name)
print(m.groupdict() if m else "invalid")
print("parsed_at", datetime.now().isoformat(timespec="seconds"))
print("elapsed_s", round(time.perf_counter() - t0, 6))

print(hashlib.sha256(name.encode()).hexdigest())
```

## 今日題目
1. 解析 500 筆命名，輸出合法/不合法比例。
2. 產生 `parsed_manifest.json`（含 parse time）。
3. 建立 `hash -> [paths]` 映射並列出重複檔。
