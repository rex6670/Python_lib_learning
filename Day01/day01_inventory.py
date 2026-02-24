"""Day 1: EDA project inventory.
Scan project folders and export CSV/JSON manifest.
"""
from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path

ALLOWED_SUFFIXES = {".def", ".lef", ".gds", ".csv"}


def scan_project(root: Path) -> list[dict]:
    rows = []
    for path in root.rglob("*"):
        if path.is_file() and path.suffix.lower() in ALLOWED_SUFFIXES:
            stat = path.stat()
            rows.append(
                {
                    "path": str(path.relative_to(root)),
                    "suffix": path.suffix.lower(),
                    "size_bytes": stat.st_size,
                    "mtime": int(stat.st_mtime),
                }
            )
    return rows


def export(rows: list[dict], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    csv_path = out_dir / "manifest.csv"
    json_path = out_dir / "manifest.json"

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["path", "suffix", "size_bytes", "mtime"])
        writer.writeheader()
        writer.writerows(rows)

    with json_path.open("w", encoding="utf-8") as f:
        json.dump(rows, f, indent=2, ensure_ascii=False)

    print(f"Saved: {csv_path}")
    print(f"Saved: {json_path}")
    print("Count by suffix:", Counter(r["suffix"] for r in rows))


if __name__ == "__main__":
    root = Path(".")
    rows = scan_project(root)
    export(rows, Path("Day01/output"))
