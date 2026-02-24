# Day 05: Pandas 報表整理（QoR / Timing / DRC）
# Day 05: Pandas Report Processing (QoR / Timing / DRC)

## 今日學習重點 | Key Learning Points
- 用 `pandas` 合併 baseline/experiment 報表。 / Merge baseline/experiment reports with `pandas`.
- 計算 WNS/TNS delta 與改善/退化。 / Compute WNS/TNS deltas and classify improve/degrade.
- 輸出 `csv`/`json` 給自動化流程。 / Export `csv`/`json` for downstream automation.

## 範例 | Example
```python
import pandas as pd
base = pd.DataFrame({"block": ["cpu"], "wns": [-0.12]})
exp = pd.DataFrame({"block": ["cpu"], "wns": [-0.08]})
out = base.merge(exp, on="block", suffixes=("_base", "_exp"))
out["delta"] = out["wns_exp"] - out["wns_base"]
print(out)
```

## 今日題目 | Exercise
1. 合併多 corner 報表並輸出 Top-N worst。 / Merge multi-corner reports and output Top-N worst.
2. 產生一份 summary JSON。 / Generate a one-page summary JSON.
