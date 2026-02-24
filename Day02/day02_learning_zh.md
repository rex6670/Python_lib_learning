# Day 02: 命名規則解析與資料指紋

## 今日學習重點
- 用 `re` 拆解 EDA 檔名欄位（design/version/corner/voltage/temp）。  
- 用 `datetime`/`time` 記錄時間與效能。  
- 用 `hashlib` 建立 SHA-256 指紋做去重。  

## 範例
```python
import re
pat = re.compile(r"(?P<design>[A-Za-z0-9_]+)_v(?P<version>\d+)_(?P<corner>TT|SS|FF)_(?P<volt>\d+p\d+V)_(?P<temp>-?\d+C)\.def$")
print(pat.match("top_cpu_v12_FF_0p72V_125C.def").groupdict())
```

## 今日題目
1. 解析 500 筆檔名，輸出合法/不合法比例。
2. 建立 `hash -> [paths]` 映射。
