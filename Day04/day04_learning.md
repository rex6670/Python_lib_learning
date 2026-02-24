# Day 04: CLI 與流程配置

## 今日學習重點（進階版）
- `argparse`：把流程參數標準化（design/corners/threads/output）。
- `configparser`：製程節點、工具路徑、預設參數外部化。
- `pickle`：中間資料快取，縮短重跑時間。
- `sys`：檢查 Python 版本與執行環境。

## 範例（補齊 lib）

### A. CLI（`argparse`）
```python
import argparse

p = argparse.ArgumentParser()
p.add_argument("--design", required=True)
p.add_argument("--corners", default="TT,SS,FF")
p.add_argument("--threads", type=int, default=8)
args = p.parse_args()
print(args.design, args.corners.split(","), args.threads)
```

### B. 設定檔（`configparser`）
```python
import configparser

cfg = configparser.ConfigParser()
cfg.read("flow.ini")
if "N7" in cfg:
    print("N7 tools:", dict(cfg["N7"]))
```

### C. 快取與環境（`pickle`, `sys`）
```python
import pickle
import sys

payload = {"design": "top_cpu", "corners": ["TT", "SS"], "ok": True}
with open("cache.pkl", "wb") as f:
    pickle.dump(payload, f)

print("python:", sys.version.split()[0])
```

## 今日題目（EDA/CAD）
1. 實作 `run_flow.py --design top_cpu --corners TT,SS --threads 8`。
2. 支援 `--node N7|N5`，從 `flow.ini` 讀預設工具參數。
3. 若輸入 hash 相同，直接讀 `cache.pkl` 跳過重算。
