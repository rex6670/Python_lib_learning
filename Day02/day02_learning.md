# Day 02: 命名規則解析與資料指紋
# Day 02: Naming Rule Parsing & File Fingerprints

## 今日學習重點 | Key Learning Points
- 用 `re` 拆解 EDA 檔名欄位（design/version/corner/voltage/temp）。  
  Use `re` to parse structured EDA filenames.
- 用 `datetime`/`time` 記錄時間與效能。  
  Use `datetime`/`time` for timestamping and performance measurement.
- 用 `hashlib` 建立 SHA-256 指紋做去重。  
  Use `hashlib` SHA-256 fingerprints for deduplication.

## 範例 | Example
```python
import re
pat = re.compile(r"(?P<design>[A-Za-z0-9_]+)_v(?P<version>\d+)_(?P<corner>TT|SS|FF)_(?P<volt>\d+p\d+V)_(?P<temp>-?\d+C)\.def$")
print(pat.match("top_cpu_v12_FF_0p72V_125C.def").groupdict())
```

## 今日題目 | Exercise
1. 解析 500 筆檔名，輸出合法/不合法比例。 / Parse 500 names and report valid/invalid ratio.
2. 建立 `hash -> [paths]` 映射。 / Build a `hash -> [paths]` map.
