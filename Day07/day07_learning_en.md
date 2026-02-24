# Day 07: Performance Optimization with Numba

## Key Learning Points
Optimize hot loops with `@numba.njit`.
Use `time.perf_counter()` for fair benchmarking.
Compare Python/NumPy/Numba performance.

## Example
```python
import numba as nb
import numpy as np

@nb.njit(cache=True)
def sum_sq(a):
    s = 0.0
    for v in a:
        s += v * v
    return s

print(sum_sq(np.arange(10, dtype=np.float64)))
```

## Exercise
Implement density map (Python vs Numba).
Verify output equivalence and speedup.
