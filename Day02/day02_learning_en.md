# Day 02: Naming Rule Parsing & File Fingerprints

## Key Learning Points
- Use `re` to parse structured EDA filenames.
- Use `datetime`/`time` for timestamping and performance measurement.
- Use `hashlib` SHA-256 fingerprints for deduplication.

## Example
```python
import re
pat = re.compile(r"(?P<design>[A-Za-z0-9_]+)_v(?P<version>\d+)_(?P<corner>TT|SS|FF)_(?P<volt>\d+p\d+V)_(?P<temp>-?\d+C)\.def$")
print(pat.match("top_cpu_v12_FF_0p72V_125C.def").groupdict())
```

## Exercise
Parse 500 names and report valid/invalid ratio.
Build a `hash -> [paths]` map.
