"""Day 8: Parallel jobs with ThreadPool and ProcessPool."""
from __future__ import annotations

from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from pathlib import Path


def io_task(i: int) -> str:
    p = Path(f"Day08/tmp_{i}.txt")
    p.write_text(f"job={i}\n", encoding="utf-8")
    return p.name


def cpu_task(i: int) -> int:
    s = 0
    for x in range(200_000):
        s += (x * i) % 97
    return s


if __name__ == "__main__":
    Path("Day08").mkdir(exist_ok=True)
    with ThreadPoolExecutor(max_workers=8) as ex:
        files = list(ex.map(io_task, range(20)))
    print("I/O generated:", len(files))

    with ProcessPoolExecutor(max_workers=4) as ex:
        vals = list(ex.map(cpu_task, range(8)))
    print("CPU results sample:", vals[:3])
