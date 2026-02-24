# Day 04: CLI and Flow Configuration

## Key Learning Points (Detailed)
- `argparse`: build a reproducible CLI interface (design/corners/threads/node).
- `configparser`: externalize node/tool parameters.
- `pickle`: cache intermediate payloads to reduce rerun time.
- `sys`: inspect Python/runtime environment.

## Common Basics
- `argparse.ArgumentParser()`: define CLI arguments.
- `configparser.ConfigParser().read(...)`: load ini configs.
- `pickle.dump/load`: write/read cache payloads.

```python
import argparse
p = argparse.ArgumentParser(); p.add_argument("--design", default="top")
print(p.parse_args([]).design)
```

## Example
```python
import argparse, configparser, pickle, sys

p = argparse.ArgumentParser()
p.add_argument("--design", required=True)
p.add_argument("--corners", default="TT,SS,FF")
p.add_argument("--threads", type=int, default=8)
args = p.parse_args([])

cfg = configparser.ConfigParser(); cfg.read("Day04/flow.ini")
pickle.dump(vars(args), open("Day04/cache.pkl", "wb"))
print("py", sys.version.split()[0], "sections", cfg.sections())
```

## Exercise
1. Implement `run_flow.py --design top_cpu --corners TT,SS --threads 8 --node N7`.
2. Reuse `cache.pkl` when input hash is unchanged.
3. Persist effective runtime options into `run_config.json`.
