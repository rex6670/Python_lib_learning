# Day 04: CLI 與流程配置

## 今日學習重點（詳細版）
- `argparse`：建立可重現 CLI 介面（design/corners/threads/node）。
- `configparser`：把製程節點與工具參數外部化。
- `pickle`：快取中間結果減少重跑時間。
- `sys`：檢查 Python 版本、平台資訊。

## 範例
```python
import argparse, configparser, pickle, sys

p = argparse.ArgumentParser()
p.add_argument("--design", required=True)
p.add_argument("--corners", default="TT,SS,FF")
p.add_argument("--threads", type=int, default=8)
args = p.parse_args([])

cfg = configparser.ConfigParser(); cfg.read("Day04/flow.ini")
pickle.dump(vars(args), open("Day04/cache.pkl", "wb"))
print("py", sys.version.split()[0], "sections", cfg.sections())
```

## 今日題目
1. 完成 `run_flow.py --design top_cpu --corners TT,SS --threads 8 --node N7`。
2. 若輸入 hash 未變，直接讀取 `cache.pkl`。
3. 將本次實際使用參數落盤到 `run_config.json`。
