"""Day 7: Numba optimization starter."""
from __future__ import annotations

import time

import numba
import numpy as np


@numba.njit(cache=True)
def density_bin(x: np.ndarray, y: np.ndarray, grid: int, max_xy: int) -> np.ndarray:
    out = np.zeros((grid, grid), dtype=np.int64)
    scale = grid / max_xy
    for i in range(x.shape[0]):
        gx = min(grid - 1, int(x[i] * scale))
        gy = min(grid - 1, int(y[i] * scale))
        out[gx, gy] += 1
    return out


if __name__ == "__main__":
    n = 1_000_000
    rng = np.random.default_rng(0)
    x = rng.integers(0, 100_000, n, dtype=np.int32)
    y = rng.integers(0, 100_000, n, dtype=np.int32)

    t0 = time.perf_counter()
    heatmap = density_bin(x, y, grid=100, max_xy=100_000)
    dt = time.perf_counter() - t0
    print("numba density map done, sum=", int(heatmap.sum()), "time=", round(dt, 4), "s")
