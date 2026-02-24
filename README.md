# EDA / CAD Engineer Python Bootcamp（10 天）

這是一份給 **EDA / CAD Engineer** 的 10 天 Python 實戰課程。  
課程形式參考 30 Days 系列：每天都有「主題模組、實作任務、練習題、今日產出」。

> 核心目標：能在實務中處理大量設計資料（例如 1M objects 的位置資訊）、批次流程、自動化檢查與報表。

---

## 每日學習說明檔（快速入口）

- Day01： [中文](Day01/day01_learning_zh.md) | [English](Day01/day01_learning_en.md)
- Day02： [中文](Day02/day02_learning_zh.md) | [English](Day02/day02_learning_en.md)
- Day03： [中文](Day03/day03_learning_zh.md) | [English](Day03/day03_learning_en.md)
- Day04： [中文](Day04/day04_learning_zh.md) | [English](Day04/day04_learning_en.md)
- Day05： [中文](Day05/day05_learning_zh.md) | [English](Day05/day05_learning_en.md)
- Day06： [中文](Day06/day06_learning_zh.md) | [English](Day06/day06_learning_en.md)
- Day07： [中文](Day07/day07_learning_zh.md) | [English](Day07/day07_learning_en.md)
- Day08： [中文](Day08/day08_learning_zh.md) | [English](Day08/day08_learning_en.md)
- Day09： [中文](Day09/day09_learning_zh.md) | [English](Day09/day09_learning_en.md)
- Day10： [中文](Day10/day10_learning_zh.md) | [English](Day10/day10_learning_en.md)

---

## Day 0 — 環境準備

### 安裝

```bash
pip install numpy pandas scipy numba
```

### 開發工具

- Python 3.10+
- VS Code
- Git

---

## Day 1 — 檔案系統與資料盤點（EDA 專案結構）

**模組**
- `os`, `sys`, `pathlib`, `glob`, `shutil`, `tempfile`
- `json`, `csv`, `collections`, `itertools`, `functools`

**實作任務**
1. 掃描 `layout/`, `netlist/`, `report/` 目錄。
2. 建立檔案索引（名稱、大小、修改時間、類型）。
3. 匯出 CSV/JSON 清單供後續流程使用。

**練習題（EDA 版）**
- 針對一個 mock 專案目錄，實作 `inventory.py`：
  - 只收集 `.def/.lef/.gds/.csv`。
  - 按檔案類型分資料夾備份。
  - 產生 `manifest.json` 給後續流程讀取。

**今日產出**
- `day01_inventory.py`

---

## Day 2 — 命名規則解析與資料指紋

**模組**
- `re`, `datetime`, `time`, `hashlib`

**實作任務**
1. 解析檔名中的 block 名稱、版本、corner（TT/SS/FF）。
2. 建立標準命名格式。
3. 用 hash 去除重複輸入檔。

**練習題（EDA 版）**
- 給定 `top_cpu_v12_FF_0p72V_125C.def` 這類字串：
  - 用 regex 拆出 `design/version/corner/voltage/temp`。
  - 轉成標準 key-value JSON。

**今日產出**
- `day02_parse_and_hash.py`

---

## Day 3 — 批次呼叫外部 EDA 工具

**模組**
- `subprocess`, `signal`, `traceback`, `logging`

**實作任務**
1. 批次呼叫外部命令（例如 mock 的 STA/DRC 腳本）。
2. 設定 timeout 與中斷機制。
3. 保存 stdout/stderr 與失敗追蹤。

**練習題（EDA 版）**
- 寫一個 runner：
  - 依序執行 20 個 corner 工作。
  - 超過 5 分鐘自動 timeout。
  - 產生失敗重跑清單 `retry_jobs.csv`。

**今日產出**
- `day03_tool_runner.py`

---

## Day 4 — CLI 與流程配置

**模組**
- `argparse`, `configparser`, `pickle`

**實作任務**
1. 把流程做成 CLI（輸入路徑、輸出路徑、corner 清單）。
2. 用 `.ini` 管理 flow 參數。
3. 用 pickle 快取中間結果。

**練習題（EDA 版）**
- 做一個 `run_flow.py`：
  - `--design top_cpu --corners TT,SS,FF --threads 8`
  - 設定檔可切換不同製程節點（N7/N5）。

**今日產出**
- `day04_cli_flow.py`

---

## Day 5 — Pandas 報表整理（QoR / Timing / DRC）

**模組**
- `pandas`, `csv`, `json`

**實作任務**
1. 匯入多份 QoR/timing 報表。
2. 對 WNS/TNS/violations 做 merge 與比較。
3. 輸出 summary 與 delta 報告。

**練習題（EDA 版）**
- 合併 `baseline` 與 `experiment` 報表：
  - 標記改善/退化 path group。
  - 依 block 與 corner 做 Top-N worst case 排序。

**今日產出**
- `day05_qor_analysis.py`

---

## Day 6 — 大規模座標資料處理（1M objects 位置資訊）

**模組**
- `numpy`, `scipy`

**實作任務**
1. 建立/讀取 1,000,000 個 objects 的 `(x, y, layer, orient)`。
2. 使用 NumPy 向量化完成座標平移/旋轉/區域查詢。
3. 使用 SciPy 做最近鄰或距離分析。

**練習題（重點）**
- 題目：**如何存 1M object 位置資訊，兼顧記憶體與查詢速度？**
- 要求：
  1. 設計資料結構並比較：
     - `list[dict]`
     - `numpy structured array`
     - `pandas DataFrame`
  2. 統計每種方式的記憶體占用。
  3. 完成兩種查詢：
     - Bounding box query：`x1<=x<=x2, y1<=y<=y2`
     - Layer filter：指定 layer 的物件數量與座標範圍
  4. 輸出效能報告（建立時間、查詢時間、記憶體）。

**今日產出**
- `day06_million_objects_storage.py`

---

## Day 7 — 效能優化（Numba）

**模組**
- `numba`, `time`

**實作任務**
1. 找出 Day 6 的熱點函式。
2. 用 `@numba.njit` 優化計算。
3. 做 benchmark 與結果一致性檢查。

**練習題（EDA 版）**
- 實作 hotspot density map：
  - 將 1M objects 映射到 grid bin。
  - 比較純 Python / NumPy / Numba 三種版本效能。

**今日產出**
- `day07_numba_opt.py`

---

## Day 8 — 平行處理與任務佇列

**模組**
- `threading`, `multiprocessing`, `concurrent.futures`, `queue`

**實作任務**
1. I/O 任務用 ThreadPool。
2. CPU 任務用 ProcessPool。
3. queue 管理 job 與結果回收。

**練習題（EDA 版）**
- 將 200 個 block 的檢查工作平行化：
  - 每個 block 要做資料載入、規則檢查、輸出報表。
  - 失敗工作要回寫 queue 重試一次。

**今日產出**
- `day08_parallel_jobs.py`

---

## Day 9 — 可維運性與除錯

**模組**
- `logging`, `traceback`, `configparser`, `shutil`

**實作任務**
1. 建立標準 log 格式（含 design/corner/job_id）。
2. 實作例外追蹤與錯誤分類。
3. 產生每日備份與歸檔。

**練習題（EDA 版）**
- 當流程中途失敗時：
  - 自動保存現場資料到 `failed_artifacts/`。
  - 生成人可讀 summary（失敗率、最常見錯誤 Top 3）。

**今日產出**
- `day09_observability.py`

---

## Day 10 — Capstone：EDA/CAD 自動化檢查管線

**整合模組（至少）**
- `os`, `pathlib`, `argparse`, `logging`, `json`, `csv`
- `numpy`, `pandas`, `scipy`, `numba`
- `concurrent.futures`, `subprocess`

**專題目標**
- 批次讀入多個設計資料，完成：
  1. 命名/版本規則檢查
  2. 1M object 座標資料分析
  3. QoR/Timing 差異報表
  4. 最終總結輸出（CSV + JSON + log）

**MVP 條件**
1. CLI 可設定輸入路徑、corner、平行 worker 數。
2. 至少處理 50 個 jobs。
3. 生成 `summary.csv`, `summary.json`, `run.log`。

**練習題（EDA 版）**
- 進階題：加入「增量模式」
  - 只重跑變更過的 block（透過 hash 判斷）。
  - 比較全量 vs 增量執行時間差異。

**今日產出**
- `day10_capstone.py`

---

## 套件覆蓋清單（已對應課程）

- 標準庫：
  `os`, `sys`, `subprocess`, `re`, `argparse`, `logging`, `json`, `csv`, `pathlib`, `collections`, `itertools`, `functools`, `shutil`, `glob`, `time`, `datetime`, `threading`, `multiprocessing`, `concurrent.futures`, `queue`, `tempfile`, `signal`, `traceback`, `configparser`, `pickle`, `hashlib`
- 第三方：
  `numpy`, `pandas`, `scipy`, `numba`

---

## 每日節奏（建議 2.5~3 小時）

- 30 分鐘：觀念 + 文件
- 90 分鐘：完成主任務
- 30 分鐘：完成當日練習題
- 30 分鐘：寫心得與優化點

---

## 下一步

如果你要，我可以下一步直接幫你建立：
1. `Day01~Day10` 資料夾與 starter code。  
2. Day 6「1M objects 儲存與查詢」完整範例（含 benchmark）。  
3. Day 10 capstone 可直接執行版。
