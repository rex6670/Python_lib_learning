"""Day 5: Pandas QoR report merge template."""
from __future__ import annotations

import json
from pathlib import Path

import pandas as pd


def build_demo_frames() -> tuple[pd.DataFrame, pd.DataFrame]:
    baseline = pd.DataFrame([
        {"block": "cpu", "corner": "TT", "wns": -0.10, "tns": -10.2},
        {"block": "gpu", "corner": "TT", "wns": -0.05, "tns": -4.0},
    ])
    exp = pd.DataFrame([
        {"block": "cpu", "corner": "TT", "wns": -0.08, "tns": -8.0},
        {"block": "gpu", "corner": "TT", "wns": -0.07, "tns": -5.1},
    ])
    return baseline, exp


if __name__ == "__main__":
    out_dir = Path("Day05")
    out_dir.mkdir(exist_ok=True)
    b, e = build_demo_frames()
    merged = b.merge(e, on=["block", "corner"], suffixes=("_base", "_exp"))
    merged["wns_delta"] = merged["wns_exp"] - merged["wns_base"]
    merged["tns_delta"] = merged["tns_exp"] - merged["tns_base"]
    merged.to_csv(out_dir / "qor_delta.csv", index=False)
    (out_dir / "qor_delta.json").write_text(merged.to_json(orient="records", indent=2), encoding="utf-8")
    print(json.loads((out_dir / "qor_delta.json").read_text(encoding="utf-8")))
