# AI_LOG — 6/18 搜尋效能五階段專題

## Stage 1 — `@timeit` 裝飾器

**我問 AI 什麼：**
拆 ≥3 個 test case（含 ≥1 個 edge case）

**AI 給了什麼：**
給了 7 個測試（含 4 個 edge：repeat=0/-1 ValueError、repeat=2.5/"abc" TypeError、例外不計入 records），並補上 specs 檢查表（簽名/例外/邊界/驗收）一次問完。

**我改了什麼：**
（學生填寫）

**AI 反問我什麼／我怎麼回答：**
| AI 反問 | 我回答 |
|---------|--------|
| repeat 非整數或 repeat=0 時該拋出什麼？ | TypeError（非整數），ValueError（≤0） |
| repeat=1 是合法最小值？f.records 何時初始化？ | 是；裝飾時初始化 |
| 被裝飾函式拋出例外時怎麼處理？ | try/except/finally，不計入 records，往上拋 |
| 怎樣算紅燈測試？ | assertion 失敗才算，import 失敗不算 |
| repeat 預設值 3 定義在哪？ | 裝飾器函式參數預設值 |

---

## Stage 2 — 三種搜尋

**我問 AI 什麼：**
拆 ≥3 個 test case（含 ≥1 個 edge case）

**AI 給了什麼：**
給了 8 個測試（含 empty list、single element、duplicate、first/last position 等 edge），用 subTest 共用三種搜尋。

**我改了什麼：**
（學生填寫）

**AI 反問我什麼／我怎麼回答：**
| AI 反問 | 我回答 |
|---------|--------|
| 為什麼 binary_search 要傳 sorted_data 而其他不用？ | binary 前提是資料已排序，其餘無此限制 |

---

## Stage 3 — 加速實驗

**我問 AI 什麼：**
拆 ≥3 個 test case（含 ≥1 個 edge case）+ benchmark 腳本

**AI 給了什麼：**
給了 4 個 benchmark 測試（含覆寫舊檔、時間為正數 edge），以及 benchmark.py 使用 @timeit 比較五種搜尋。

**我改了什麼：**
（學生填寫）

**AI 反問我什麼／我怎麼回答：**
| AI 反問 | 我回答 |
|---------|--------|
| 預測排名與實測排名是否一致？ | （學生比對 results.json 後填寫） |

**抓 AI 的錯：** AI 常說「binary 一定比 linear 快」。
這句話在以下條件是錯的：
- （學生用 results.json 數據反駁）

---

## Stage 4 — 雷達圖

**我問 AI 什麼：**
拆 ≥3 個 test case（含 ≥1 個 edge case）+ 雷達圖實作

**AI 給了什麼：**
給了 3 個測試（PNG 產生、非空、overwrite）與 plot.py 使用 matplotlib 的 5 維度雷達圖。

**我改了什麼：**
（學生填寫）

**AI 反問我什麼／我怎麼回答：**
| AI 反問 | 我回答 |
|---------|--------|
| 哪種搜尋在日常開發中最均衡實用？為什麼？ | built-in in（Simplicity & Flexibility 滿分、C 底層優化、就地搜尋） |

---

## Stage 5 — 安全性自掃

**我問 AI 什麼：**
拆 ≥3 條 OpenSSF 適用規則的紅燈測試

**AI 給了什麼：**
給了 4 個測試對應 3 條規則（pyscg-0034 None 檢查、pyscg-0014 具體例外型別、pyscg-0051 資源釋放），修正 search.py/timing.py/plot.py。

**我改了什麼：**
（學生填寫）

**AI 反問我什麼／我怎麼回答：**
（學生填寫 — 例如：哪些規則被判定不適用及理由）
