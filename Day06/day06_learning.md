# Day 06: 大規模座標資料處理（1M objects）

## 今日學習重點（進階版）
- `numpy`：向量化查詢與批次運算（bbox/filter）。
- `pandas`：易讀性高、分析彈性高，但記憶體較高。
- `scipy.spatial.cKDTree`：最近鄰查詢加速。
- 比較 `list[dict]` / `structured array` / `DataFrame` 的建構速度、查詢速度、記憶體。

## 範例（補齊 lib）

### A. NumPy bbox（`numpy`）
```python
import numpy as np

n = 1_000_000
x = np.random.randint(0, 100_000, n, dtype=np.int32)
y = np.random.randint(0, 100_000, n, dtype=np.int32)
mask = (10_000 <= x) & (x <= 20_000) & (20_000 <= y) & (y <= 30_000)
print("bbox count:", int(mask.sum()))
```

### B. DataFrame 分析（`pandas`）
```python
import pandas as pd

df = pd.DataFrame({"x": x, "y": y, "layer": np.random.randint(1, 9, n)})
print(df.query("layer == 3")[ ["x", "y"] ].describe())
```

### C. 最近鄰（`scipy`）
```python
from scipy.spatial import cKDTree

tree = cKDTree(np.column_stack([x, y]))
dist, idx = tree.query([50_000, 50_000], k=5)
print("nearest idx:", idx, "dist:", dist)
```

## 今日題目（EDA/CAD）
1. 建立 1M objects：`x,y,layer,orient`。
2. 比較三種儲存格式：建構時間、bbox 時間、記憶體。
3. 增加 layer filter + nearest-neighbor 報告。
4. 輸出 `storage_benchmark.csv` 與結論建議。
