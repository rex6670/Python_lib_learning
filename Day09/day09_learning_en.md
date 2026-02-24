# Day 09: Observability and Debugging

## Key Learning Points
Build structured logs with design/corner/job_id.
Capture full exception stack with `traceback`.
Configure log level with `configparser` and archive artifacts with `shutil`.

## Example
```python
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logging.info("design=top_cpu corner=TT job=42 status=start")
```

## Exercise
Report Top3 error categories.
Archive failed artifacts into `failed_artifacts/`.
