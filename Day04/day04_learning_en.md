# Day 04: CLI and Flow Configuration

## Key Learning Points
Define flow parameters with `argparse`.
Manage node/tool configs using `configparser`.
Cache intermediate results with `pickle` and inspect runtime with `sys`.

## Example
```python
import argparse
p = argparse.ArgumentParser()
p.add_argument("--design", required=True)
p.add_argument("--corners", default="TT,SS")
args = p.parse_args()
print(args.design, args.corners.split(","))
```

## Exercise
Support `--design --corners --threads --node`.
Reuse cache when input hash is unchanged.
