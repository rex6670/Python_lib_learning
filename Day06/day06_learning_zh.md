# Day 06: 大規模座標資料處理（1M objects）

## 今日學習重點
- `numpy` 向量化 bbox/filter 查詢。
- 比較 `list[dict]`、`structured array`、`DataFrame`。
- `scipy.spatial.cKDTree` 做最近鄰。

## 範例
```python
import numpy as np
x = np.random.randint(0, 100000, 1_000_000, dtype=np.int32)
y = np.random.randint(0, 100000, 1_000_000, dtype=np.int32)
mask = (10_000 <= x) & (x <= 20_000) & (20_000 <= y) & (y <= 30_000)
print(int(mask.sum()))
```

## 今日題目
1. 比較三種儲存格式的建構時間/記憶體。
2. 完成 bbox + layer + nearest-neighbor 報告。
