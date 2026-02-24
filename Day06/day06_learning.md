# Day 06: 大規模座標資料處理（1M objects）
# Day 06: Large-Scale Coordinate Processing (1M objects)

## 今日學習重點 | Key Learning Points
- `numpy` 向量化 bbox/filter 查詢。 / Perform vectorized bbox/filter queries with `numpy`.
- 比較 `list[dict]`、`structured array`、`DataFrame`。 / Compare `list[dict]`, `structured array`, and `DataFrame`.
- `scipy.spatial.cKDTree` 做最近鄰。 / Use `scipy.spatial.cKDTree` for nearest-neighbor search.

## 範例 | Example
```python
import numpy as np
x = np.random.randint(0, 100000, 1_000_000, dtype=np.int32)
y = np.random.randint(0, 100000, 1_000_000, dtype=np.int32)
mask = (10_000 <= x) & (x <= 20_000) & (20_000 <= y) & (y <= 30_000)
print(int(mask.sum()))
```

## 今日題目 | Exercise
1. 比較三種儲存格式的建構時間/記憶體。 / Compare build time and memory across three storage formats.
2. 完成 bbox + layer + nearest-neighbor 報告。 / Deliver bbox + layer + nearest-neighbor report.
