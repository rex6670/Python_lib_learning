"""Day 3: Batch subprocess runner with logging and timeout."""
from __future__ import annotations

import logging
import subprocess
import traceback
from pathlib import Path

logging.basicConfig(
    filename="Day03/tool_runner.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)


def run_job(cmd: list[str], timeout_s: int = 30) -> tuple[int, str, str]:
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout_s, check=False)
        return result.returncode, result.stdout, result.stderr
    except Exception:
        logging.error("Job failed: %s", cmd)
        logging.error(traceback.format_exc())
        return 1, "", "exception"


if __name__ == "__main__":
    Path("Day03").mkdir(exist_ok=True)
    jobs = [["python", "-c", "print('corner TT ok')"], ["python", "-c", "print('corner SS ok')"]]
    for job in jobs:
        code, out, err = run_job(job)
        logging.info("cmd=%s code=%s out=%s err=%s", job, code, out.strip(), err.strip())
        print(job, code)
