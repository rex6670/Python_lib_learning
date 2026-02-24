"""Day 2: Parse naming rule and compute file hashes."""
from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime
from pathlib import Path

PATTERN = re.compile(
    r"(?P<design>[a-zA-Z0-9]+)_v(?P<version>\d+)_(?P<corner>TT|SS|FF)_(?P<voltage>\d+p\d+V)_(?P<temp>-?\d+C)\.def$"
)


def parse_name(filename: str) -> dict | None:
    m = PATTERN.match(filename)
    if not m:
        return None
    data = m.groupdict()
    data["parsed_at"] = datetime.now().isoformat(timespec="seconds")
    return data


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


if __name__ == "__main__":
    sample = "top_cpu_v12_FF_0p72V_125C.def"
    parsed = parse_name(sample)
    print("Parsed:", json.dumps(parsed, indent=2, ensure_ascii=False))

    readme = Path("README.md")
    if readme.exists():
        print("README sha256:", sha256_file(readme))
