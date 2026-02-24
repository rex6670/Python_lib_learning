# Day 05: Pandas 報表整理（QoR / Timing / DRC）

## 今日學習重點（詳細版）
- `pandas`：merge/groupby/sort_values 做 QoR 對比。
- `csv` / `json`：輸出 summary 與 delta 報告。
- QoR 指標：WNS/TNS/violations 的改善與退化判斷。

## 範例
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

## 今日題目
1. 合併 baseline/experiment 多 corner 報表。
2. 依 block/corner 輸出 Top-N worst path group。
3. 產出可供 Day10 使用的 `summary.json`。
