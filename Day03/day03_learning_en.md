# Day 03: Batch Execution for External EDA Tools

## Key Learning Points (Detailed)
- `subprocess`: execute external tools in batch and capture stdout/stderr.
- `signal`: handle interruption gracefully for safe shutdown.
- `logging`: write structured logs (job_id/corner/status).
- `traceback`: preserve full stack traces for debugging.

## Example
```python
import subprocess, signal, logging, traceback

stop = False
signal.signal(signal.SIGINT, lambda s, f: globals().__setitem__("stop", True))
logging.basicConfig(filename="Day03/run.log", level=logging.INFO)

try:
    r = subprocess.run(["python", "-c", "print('mock_sta_ok')"], capture_output=True, text=True, timeout=5)
    logging.info("code=%s out=%s", r.returncode, r.stdout.strip())
except Exception:
    logging.error(traceback.format_exc())
```

## Exercise
1. Simulate 20 corner jobs with timeout control.
2. Write failed/timeout jobs to `retry_jobs.csv`.
3. Generate `summary.json` with pass rate and top failure reasons.
