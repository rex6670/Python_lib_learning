# Day 06: 大規模座標資料處理（1M objects）

## 今日學習重點（詳細版）
- `numpy`：大規模向量化 bbox 查詢與 layer filter。
- `pandas`：高可讀分析與記憶體統計。
- `scipy.spatial.cKDTree`：最近鄰查詢。
- 比較 `list[dict]` / `structured array` / `DataFrame` 的速度與記憶體。

## 範例
```python
import numpy as np, pandas as pd
from scipy.spatial import cKDTree

n = 1_000_000
x = np.random.randint(0, 100_000, n, dtype=np.int32)
y = np.random.randint(0, 100_000, n, dtype=np.int32)
layer = np.random.randint(1, 11, n, dtype=np.int16)

bbox = (10_000 <= x) & (x <= 20_000) & (20_000 <= y) & (y <= 30_000)
print("bbox count", int(bbox.sum()))

df = pd.DataFrame({"x": x, "y": y, "layer": layer})
print("mem_mb", round(df.memory_usage(deep=True).sum() / 1024 / 1024, 2))

tree = cKDTree(np.column_stack([x, y]))
print(tree.query([50_000, 50_000], k=3))
```

## 今日題目
1. 三種儲存格式比較（build/query/memory）。
2. 完成 bbox query + layer filter + nearest-neighbor。
3. 輸出 `storage_benchmark.csv`。
