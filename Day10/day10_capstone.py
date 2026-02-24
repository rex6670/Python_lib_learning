"""Day 10 capstone starter: end-to-end EDA/CAD mini pipeline."""
from __future__ import annotations

import argparse
import csv
import json
import logging
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import numpy as np
import pandas as pd


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--input", default=".")
    p.add_argument("--output", default="Day10/output")
    p.add_argument("--workers", type=int, default=4)
    return p.parse_args()


def check_job(i: int) -> dict:
    rng = np.random.default_rng(i)
    wns = float(rng.normal(-0.1, 0.03))
    status = "PASS" if wns >= -0.12 else "FAIL"
    return {"job_id": i, "wns": round(wns, 4), "status": status}


if __name__ == "__main__":
    args = parse_args()
    out_dir = Path(args.output)
    out_dir.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(filename=out_dir / "run.log", level=logging.INFO)
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        rows = list(ex.map(check_job, range(50)))

    df = pd.DataFrame(rows)
    df.to_csv(out_dir / "summary.csv", index=False)
    (out_dir / "summary.json").write_text(df.to_json(orient="records", indent=2), encoding="utf-8")

    with (out_dir / "status_count.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["status", "count"])
        for k, v in df["status"].value_counts().items():
            w.writerow([k, int(v)])

    print(json.dumps({"output": str(out_dir), "jobs": len(rows)}, ensure_ascii=False))
