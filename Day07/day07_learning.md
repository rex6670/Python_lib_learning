# Day 07: 效能優化（Numba）

## 今日學習重點（進階版）
- `numba.njit`：把 Python 迴圈 JIT 成機器碼。
- `time`：公平 benchmark（warm-up 與多次量測）。
- 和 Day06 串接：對 hotspot 計算做優化。

## 範例（補齊 lib）

### A. Numba hotspot（`numba`, `numpy`）
```python
import numba as nb
import numpy as np

@nb.njit(cache=True)
def manhattan_sum(x, y):
    s = 0
    for i in range(x.shape[0]):
        s += abs(int(x[i]) - int(y[i]))
    return s

x = np.arange(100000, dtype=np.int32)
y = np.arange(100000, dtype=np.int32)[::-1]
print(manhattan_sum(x, y))
```

### B. 量測（`time`）
```python
import time

t0 = time.perf_counter()
_ = manhattan_sum(x, y)   # 第一次會有編譯成本
first = time.perf_counter() - t0

t1 = time.perf_counter()
_ = manhattan_sum(x, y)   # 第二次較接近真實執行成本
steady = time.perf_counter() - t1
print(first, steady)
```

## 今日題目（EDA/CAD）
1. 實作 density map binning：純 Python 與 Numba 版本。
2. 比較 warm-up 後平均時間。
3. 驗證兩版本輸出完全一致（sum / 每格值）。
