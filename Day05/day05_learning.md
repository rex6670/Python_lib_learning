# Day 05: Pandas 報表整理（QoR / Timing / DRC）

## 今日學習重點
- 使用 `pandas` 匯入多份 QoR 報表並合併。
- 進行 baseline/experiment 的 delta 比較。
- 匯出 CSV/JSON 供流程與儀表板使用。

## 範例
```python
import pandas as pd

base = pd.DataFrame({"group": ["clk", "io"], "wns": [-0.12, -0.03]})
exp = pd.DataFrame({"group": ["clk", "io"], "wns": [-0.07, -0.04]})
out = base.merge(exp, on="group", suffixes=("_base", "_exp"))
out["delta"] = out["wns_exp"] - out["wns_base"]
print(out)
```

## 今日題目（EDA/CAD）
1. 合併多 corner QoR 報表。
2. 識別改善/退化 path groups。
3. 輸出 Top-N worst case 清單。
