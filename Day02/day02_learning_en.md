# Day 02: Naming Rule Parsing & File Fingerprints

## Key Learning Points (Detailed)
- `re`: parse and validate filename fields with named groups.
- `datetime` / `time`: record parse timestamps and throughput.
- `hashlib`: use SHA-256 for deduplication and incremental flow control.

## Common Basics
- `re.match()`: validate from string start.
- `datetime.now().isoformat()`: standard timestamp format.
- `hashlib.sha256(...).hexdigest()`: stable digest.

```python
import re, hashlib
print(bool(re.match(r"^top_", "top_cpu")))
print(hashlib.sha256(b"abc").hexdigest()[:8])
```

## Example
```python
import re, time, hashlib
from datetime import datetime

pat = re.compile(r"(?P<design>[A-Za-z0-9_]+)_v(?P<ver>\d+)_(?P<corner>TT|SS|FF)_(?P<volt>\d+p\d+V)_(?P<temp>-?\d+C)\.def$")
name = "top_cpu_v12_FF_0p72V_125C.def"

t0 = time.perf_counter()
m = pat.match(name)
print(m.groupdict() if m else "invalid")
print("parsed_at", datetime.now().isoformat(timespec="seconds"))
print("elapsed_s", round(time.perf_counter() - t0, 6))

print(hashlib.sha256(name.encode()).hexdigest())
```

## Exercise
1. Parse 500 names and report valid/invalid ratio.
2. Export `parsed_manifest.json` with parse timestamp.
3. Build `hash -> [paths]` map and list duplicate files.
