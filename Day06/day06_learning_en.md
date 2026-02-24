# Day 06: Large-Scale Coordinate Processing (1M objects)

## Key Learning Points
Perform vectorized bbox/filter queries with `numpy`.
Compare `list[dict]`, `structured array`, and `DataFrame`.
Use `scipy.spatial.cKDTree` for nearest-neighbor search.

## Example
```python
import numpy as np
x = np.random.randint(0, 100000, 1_000_000, dtype=np.int32)
y = np.random.randint(0, 100000, 1_000_000, dtype=np.int32)
mask = (10_000 <= x) & (x <= 20_000) & (20_000 <= y) & (y <= 30_000)
print(int(mask.sum()))
```

## Exercise
Compare build time and memory across three storage formats.
Deliver bbox + layer + nearest-neighbor report.
