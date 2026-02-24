# Day 04: CLI 與流程配置

## 今日學習重點
- 使用 `argparse` 建立可重現的命令列介面。
- 使用 `configparser` 將製程與流程參數外部化。
- 使用 `pickle` 快取中間計算結果。

## 範例
```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--design", required=True)
parser.add_argument("--corners", default="TT")
args = parser.parse_args()
print(args.design, args.corners.split(","))
```

## 今日題目（EDA/CAD）
1. 支援 `--design --corners --threads`。
2. 讀取 `flow.ini` 中不同節點（N7/N5）的設定。
3. 將前次結果快取到 `cache.pkl`。
