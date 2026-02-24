# Day 05: Pandas Report Processing (QoR / Timing / DRC)

## Key Learning Points (Detailed)
- `pandas`: use merge/groupby/sort for QoR comparison.
- `csv` / `json`: export summary and delta reports.
- QoR metrics: classify WNS/TNS/violations as improvement or degradation.

## Example
```python
import pandas as pd, json

base = pd.DataFrame({"block": ["cpu", "gpu"], "corner": ["TT", "TT"], "wns": [-0.12, -0.03], "tns": [-10.2, -4.0]})
exp  = pd.DataFrame({"block": ["cpu", "gpu"], "corner": ["TT", "TT"], "wns": [-0.08, -0.05], "tns": [-8.0, -5.1]})

m = base.merge(exp, on=["block", "corner"], suffixes=("_base", "_exp"))
m["wns_delta"] = m["wns_exp"] - m["wns_base"]
m["trend"] = m["wns_delta"].apply(lambda x: "improve" if x > 0 else "degrade")

m.to_csv("Day05/qor_delta.csv", index=False)
json.dump(m.to_dict(orient="records"), open("Day05/qor_delta.json", "w", encoding="utf-8"), indent=2)
```

## Exercise
1. Merge baseline/experiment reports across multiple corners.
2. Output Top-N worst path groups by block/corner.
3. Generate `summary.json` for Day10 pipeline input.
