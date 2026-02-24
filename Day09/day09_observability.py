"""Day 9: Logging/traceback + backup scaffold."""
from __future__ import annotations

import logging
import shutil
import traceback
from pathlib import Path

LOG = Path("Day09/run.log")


def setup() -> None:
    Path("Day09").mkdir(exist_ok=True)
    logging.basicConfig(filename=LOG, level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


def risky_step(x: int) -> float:
    return 10 / x


if __name__ == "__main__":
    setup()
    for x in [5, 2, 0, 1]:
        try:
            y = risky_step(x)
            logging.info("x=%s y=%s", x, y)
        except Exception:
            logging.error("failed x=%s", x)
            logging.error(traceback.format_exc())

    backup_dir = Path("Day09/backup")
    backup_dir.mkdir(exist_ok=True)
    shutil.copy2(LOG, backup_dir / "run.log")
    print("backup created:", backup_dir / "run.log")
