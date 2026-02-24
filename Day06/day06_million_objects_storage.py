"""Day 6: 1M object storage benchmark scaffold.
Compare list[dict], numpy structured array, pandas DataFrame.
"""
from __future__ import annotations

import time
from dataclasses import dataclass

import numpy as np
import pandas as pd
from scipy.spatial import cKDTree


@dataclass
class Result:
    name: str
    build_s: float
    query_s: float
    mem_mb: float


def generate_data(n: int = 1_000_000, seed: int = 42):
    rng = np.random.default_rng(seed)
    x = rng.integers(0, 100_000, size=n, dtype=np.int32)
    y = rng.integers(0, 100_000, size=n, dtype=np.int32)
    layer = rng.integers(1, 11, size=n, dtype=np.int16)
    orient = rng.choice(np.array(["N", "S", "E", "W"]), size=n)
    return x, y, layer, orient


def bbox_numpy(x, y, x1, x2, y1, y2):
    m = (x >= x1) & (x <= x2) & (y >= y1) & (y <= y2)
    return int(m.sum())


def main(n: int = 1_000_000) -> None:
    x, y, layer, orient = generate_data(n)
    results: list[Result] = []

    t0 = time.perf_counter()
    lod = [
        {"x": int(xi), "y": int(yi), "layer": int(li), "orient": oi}
        for xi, yi, li, oi in zip(x, y, layer, orient)
    ]
    build = time.perf_counter() - t0
    t1 = time.perf_counter()
    cnt = sum(1 for r in lod if 10_000 <= r["x"] <= 20_000 and 20_000 <= r["y"] <= 30_000)
    query = time.perf_counter() - t1
    mem_mb = (sum(r.__sizeof__() for r in lod[:1000]) / 1000) * len(lod) / (1024**2)
    results.append(Result("list[dict]", build, query, mem_mb))
    print("list[dict] bbox count:", cnt)

    t0 = time.perf_counter()
    arr = np.zeros(n, dtype=[("x", "i4"), ("y", "i4"), ("layer", "i2"), ("orient", "U1")])
    arr["x"], arr["y"], arr["layer"], arr["orient"] = x, y, layer, orient
    build = time.perf_counter() - t0
    t1 = time.perf_counter()
    cnt = int(((arr["x"] >= 10_000) & (arr["x"] <= 20_000) & (arr["y"] >= 20_000) & (arr["y"] <= 30_000)).sum())
    query = time.perf_counter() - t1
    mem_mb = arr.nbytes / (1024**2)
    results.append(Result("numpy_structured", build, query, mem_mb))
    print("numpy bbox count:", cnt)

    t0 = time.perf_counter()
    df = pd.DataFrame({"x": x, "y": y, "layer": layer, "orient": orient})
    build = time.perf_counter() - t0
    t1 = time.perf_counter()
    cnt = len(df.query("10000 <= x <= 20000 and 20000 <= y <= 30000"))
    query = time.perf_counter() - t1
    mem_mb = df.memory_usage(deep=True).sum() / (1024**2)
    results.append(Result("pandas", build, query, mem_mb))
    print("pandas bbox count:", cnt)

    tree = cKDTree(np.column_stack([x, y]))
    _, idx = tree.query([50000, 50000], k=5)
    print("Nearest neighbors sample indexes:", idx.tolist())

    out = pd.DataFrame([r.__dict__ for r in results])
    out.to_csv("Day06/storage_benchmark.csv", index=False)
    print(out)


if __name__ == "__main__":
    main()
