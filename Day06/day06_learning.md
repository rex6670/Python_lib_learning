# Day 06: 大規模座標資料處理（1M objects）

## 今日學習重點
- 使用 `numpy` 儲存/查詢大量座標資料。
- 比較 `list[dict]`、structured array、DataFrame 的成本。
- 使用 `scipy.spatial.cKDTree` 做最近鄰查詢。

## 範例
```python
import numpy as np

n = 1_000_000
x = np.random.randint(0, 20000, size=n, dtype=np.int32)
y = np.random.randint(0, 20000, size=n, dtype=np.int32)
mask = (x >= 1000) & (x <= 5000) & (y >= 1000) & (y <= 5000)
print("bbox count:", int(mask.sum()))
```

## 今日題目（EDA/CAD）
1. 實作 1M object 的三種儲存格式比較。
2. 完成 bbox query 與 layer filter。
3. 輸出建立時間/查詢時間/記憶體報告。
