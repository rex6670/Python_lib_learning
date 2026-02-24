# Day 02: 命名規則解析與資料指紋

## 今日學習重點
- 使用 `re` 解析 EDA 檔名欄位（design/version/corner/voltage/temp）。
- 使用 `datetime` 產生標準化時間戳。
- 使用 `hashlib` 建立檔案 fingerprint。

## 範例
```python
import re

name = "top_cpu_v12_FF_0p72V_125C.def"
pat = r"(?P<design>\w+)_v(?P<ver>\d+)_(?P<corner>TT|SS|FF)_(?P<volt>\d+p\d+V)_(?P<temp>-?\d+C)\.def"
m = re.match(pat, name)
print(m.groupdict() if m else "no match")
```

## 今日題目（EDA/CAD）
1. 解析 100 筆檔名，輸出結構化 JSON。
2. 對每個檔案產生 SHA-256。
3. 找出重複檔（同 hash 不同路徑）。
