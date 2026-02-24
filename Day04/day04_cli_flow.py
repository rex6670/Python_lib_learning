"""Day 4: CLI + config parser + pickle cache."""
from __future__ import annotations

import argparse
import configparser
import pickle
from pathlib import Path


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="EDA flow CLI starter")
    p.add_argument("--design", required=True)
    p.add_argument("--corners", default="TT")
    p.add_argument("--threads", type=int, default=4)
    p.add_argument("--config", default="Day04/flow.ini")
    return p.parse_args()


def load_config(path: Path) -> configparser.ConfigParser:
    cfg = configparser.ConfigParser()
    if path.exists():
        cfg.read(path)
    return cfg


if __name__ == "__main__":
    Path("Day04").mkdir(exist_ok=True)
    args = parse_args()
    cfg = load_config(Path(args.config))
    payload = {"design": args.design, "corners": args.corners.split(","), "threads": args.threads}
    cache = Path("Day04/cache.pkl")
    with cache.open("wb") as f:
        pickle.dump(payload, f)
    print("Saved cache:", cache)
    print("Config sections:", cfg.sections())
