# Day 07: 效能優化（Numba）

## 今日學習重點
- 用 `@numba.njit` 優化迴圈熱點。
- 用 `time.perf_counter()` 做公平 benchmark。
- 比較 Python/NumPy/Numba 效能。

## 範例
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

## 今日題目
1. 實作 density map（Python vs Numba）。
2. 驗證輸出一致性與加速比。
