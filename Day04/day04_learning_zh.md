# Day 04: CLI 與流程配置

## 今日學習重點
- `argparse` 定義流程參數。
- `configparser` 管理製程/工具設定。
- `pickle` 快取中間結果、`sys` 檢查執行環境。

## 範例
```python
import argparse
p = argparse.ArgumentParser()
p.add_argument("--design", required=True)
p.add_argument("--corners", default="TT,SS")
args = p.parse_args()
print(args.design, args.corners.split(","))
```

## 今日題目
1. 支援 `--design --corners --threads --node`。
2. 同 hash 輸入時直接讀取快取。
