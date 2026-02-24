# Day 05: Pandas 報表整理（QoR / Timing / DRC）

## 今日學習重點（進階版）
- `pandas`：多報表 merge / join / groupby。
- `csv` / `json`：輸出給管理層與流程系統。
- QoR 觀念：WNS/TNS/violations 的改善或退化判斷。

## 範例（補齊 lib）

### A. QoR merge（`pandas`）
```python
import pandas as pd

base = pd.DataFrame({"block": ["cpu", "gpu"], "wns": [-0.12, -0.03]})
exp = pd.DataFrame({"block": ["cpu", "gpu"], "wns": [-0.08, -0.05]})
out = base.merge(exp, on="block", suffixes=("_base", "_exp"))
out["delta"] = out["wns_exp"] - out["wns_base"]
out["trend"] = out["delta"].apply(lambda d: "improve" if d > 0 else "degrade")
print(out)
```

### B. 輸出（`csv`, `json`）
```python
import json

out.to_csv("qor_delta.csv", index=False)
records = out.to_dict(orient="records")
with open("qor_delta.json", "w", encoding="utf-8") as f:
    json.dump(records, f, indent=2, ensure_ascii=False)
```

## 今日題目（EDA/CAD）
1. 合併 baseline/experiment 在多個 corner 的報表。
2. 每個 block 輸出 WNS/TNS delta 與 trend。
3. 產生 Top-10 worst groups（按 TNS 由差到好）。
4. 產生 one-page summary JSON 給 Day10 使用。
