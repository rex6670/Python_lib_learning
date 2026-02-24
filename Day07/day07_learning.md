# Day 07: 效能優化（Numba）

## 今日學習重點
- 將熱點函式改寫為數值陣列導向。
- 使用 `@numba.njit` 加速迴圈。
- 對照純 Python 與 Numba 的 benchmark。

## 範例
```python
import numba as nb
import numpy as np

@nb.njit
def sum_sq(a):
    s = 0.0
    for v in a:
        s += v * v
    return s

print(sum_sq(np.arange(10, dtype=np.float64)))
```

## 今日題目（EDA/CAD）
1. 實作 density map binning。
2. 比較 Python/NumPy/Numba 三版本時間。
3. 驗證三者輸出一致。
