# Day 05: Pandas Report Processing (QoR / Timing / DRC)

## Key Learning Points
Merge baseline/experiment reports with `pandas`.
Compute WNS/TNS deltas and classify improve/degrade.
Export `csv`/`json` for downstream automation.

## Example
```python
import pandas as pd
base = pd.DataFrame({"block": ["cpu"], "wns": [-0.12]})
exp = pd.DataFrame({"block": ["cpu"], "wns": [-0.08]})
out = base.merge(exp, on="block", suffixes=("_base", "_exp"))
out["delta"] = out["wns_exp"] - out["wns_base"]
print(out)
```

## Exercise
Merge multi-corner reports and output Top-N worst.
Generate a one-page summary JSON.
