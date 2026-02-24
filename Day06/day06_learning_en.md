# Day 06: Large-Scale Coordinate Processing (1M objects)

## Key Learning Points (Detailed)
- `numpy`: vectorized bbox and layer filtering at scale.
- `pandas`: readable analytics and memory inspection.
- `scipy.spatial.cKDTree`: nearest-neighbor queries.
- Compare `list[dict]` / `structured array` / `DataFrame` for speed and memory.

## Example
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

## Exercise
1. Benchmark three storage formats (build/query/memory).
2. Implement bbox query + layer filter + nearest-neighbor.
3. Export `storage_benchmark.csv`.
