# Day 10: Capstone（EDA/CAD 自動化檢查管線）

## 今日學習重點
- 串接前 9 天模組形成完整 pipeline。
- 提供 CLI、平行執行與最終報表輸出。
- 導入增量重跑（hash-based）降低全量時間。

## 範例
```python
summary = {
    "jobs": 50,
    "pass": 46,
    "fail": 4,
    "outputs": ["summary.csv", "summary.json", "run.log"],
}
print(summary)
```

## 今日題目（EDA/CAD）
1. 至少處理 50 個 jobs。
2. 輸出 `summary.csv`、`summary.json`、`run.log`。
3. 比較全量與增量模式執行時間差異。
