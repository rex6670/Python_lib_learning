# Day 04: CLI 與流程配置
# Day 04: CLI and Flow Configuration

## 今日學習重點 | Key Learning Points
- `argparse` 定義流程參數。 / Define flow parameters with `argparse`.
- `configparser` 管理製程/工具設定。 / Manage node/tool configs using `configparser`.
- `pickle` 快取中間結果、`sys` 檢查執行環境。 / Cache intermediate results with `pickle` and inspect runtime with `sys`.

## 範例 | Example
```python
import argparse
p = argparse.ArgumentParser()
p.add_argument("--design", required=True)
p.add_argument("--corners", default="TT,SS")
args = p.parse_args()
print(args.design, args.corners.split(","))
```

## 今日題目 | Exercise
1. 支援 `--design --corners --threads --node`。 / Support `--design --corners --threads --node`.
2. 同 hash 輸入時直接讀取快取。 / Reuse cache when input hash is unchanged.
