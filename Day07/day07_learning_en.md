# Day 07: Performance Optimization with Numba

## Key Learning Points (Detailed)
- `numba.njit`: JIT-compile Python loops to reduce hotspot cost.
- `numpy`: contiguous arrays improve Numba performance.
- `time`: separate first-run compile cost from steady-state runtime.

## Common Basics
- `@numba.njit`: accelerate numeric loops.
- `time.perf_counter()`: accurate timing.
- warm-up first, then benchmark.

```python
import time
s = time.perf_counter(); _ = sum(range(1000)); print(time.perf_counter()-s)
```

## Example
```python
import numba as nb, numpy as np, time

@nb.njit(cache=True)
def density(x, y, grid, max_xy):
    out = np.zeros((grid, grid), dtype=np.int64)
    scale = grid / max_xy
    for i in range(x.shape[0]):
        out[min(grid-1, int(x[i]*scale)), min(grid-1, int(y[i]*scale))] += 1
    return out

x = np.random.randint(0, 100000, 200000, dtype=np.int32)
y = np.random.randint(0, 100000, 200000, dtype=np.int32)
t0=time.perf_counter(); density(x,y,100,100000); t1=time.perf_counter()
t2=time.perf_counter(); density(x,y,100,100000); t3=time.perf_counter()
print("compile+run", t1-t0, "steady", t3-t2)
```

## Exercise
1. Implement density map in Python and Numba.
2. Report steady-state speedup after warm-up.
3. Verify output equivalence (total sum and bin values).
