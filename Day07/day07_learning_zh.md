# Day 07: 效能優化（Numba）

## 今日學習重點（詳細版）
- `numba.njit`：將 Python 迴圈 JIT 化，降低熱點成本。
- `numpy`：用連續陣列提升 Numba 效果。
- `time`：分別量測第一次編譯成本與穩定執行時間。

## 基礎常用用法
- `@numba.njit`：加速純數值迴圈。
- `time.perf_counter()`：精準量測。
- 先 warm-up 再 benchmark。

```python
import time
s = time.perf_counter(); _ = sum(range(1000)); print(time.perf_counter()-s)
```

## 範例
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

## 今日題目
1. 實作 Python 版與 Numba 版 density map。
2. 報告 warm-up 後加速比。
3. 驗證兩版結果一致（sum 與格點值）。
