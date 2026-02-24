# Day 03: Batch Execution for External EDA Tools

## Key Learning Points
Run tools in batch with `subprocess`.
Handle interruption with `signal` and capture errors via `traceback`.
Build traceable per-job logs using `logging`.

## Example
```python
import subprocess
r = subprocess.run(["python", "-c", "print('STA done')"], capture_output=True, text=True, timeout=5)
print(r.returncode, r.stdout.strip())
```

## Exercise
Simulate 20 corner jobs.
Write timeout jobs into `retry_jobs.csv`.
