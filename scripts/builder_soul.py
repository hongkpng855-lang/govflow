# builder_soul.py
# ESGov Builder Operating Definitions — Mode A / B / C
# This file documents the three step modes used across all ESGov products.
# Refer to this when building or converting step cards and generator pages.

"""
==================================================
ESGov 步驟模式定義（Mode A / B / C）
==================================================

每步（step）分為三種模式，定義如下：

---

## Mode A — 互動填表工具（Interactive Generator）

hasGenerator: true
有互動工具（jsPDF）可以直接填寫 + 生成 PDF。

Card 顯示：
  - generator 圖片（xxx-template.png，乾淨 form 截圖，NOT 全頁 screenshot）
  - 「可修改文件」按鈕 → 互動表格
  - 🚀 填寫 + 生成 PDF

Generator 頁面 include：
  - Info banner（optional）
  - Interactive form with jsPDF
  - Preview card（可修改文件截圖）
  - 常見錯誤
  - 返回按鈕

參考：
  - Product 1（股份轉讓）Step 1（Sold Note）
  - Product 4（撤銷註冊）Step 1（Checklist）, Step 6（IRC3113）

---

## Mode B — 官方表格範例檢視（Official Form Viewer）

hasGenerator: false
generatorUrl → 官方 PDF link（CR / IRD official fillable PDF）
冇互動工具，純粹官方表格展示 + download。

Card 顯示：
  - 官方表格截圖（PyMuPDF render from official PDF）
  - 📄 NDR1 / IR1263 撤銷註冊申請書（官方表格）
  - 按鈕：📄 下載官方表格

Generator 頁面 include（跟 NR2 pattern）：
  - 📌 Info banner（說明前提條件）
  - 🖼️ 官方表格 full image（clickable → lightbox modal）
  - ⚠️ 常見錯誤
  - 📥 下載官方 NDR1 / IR1263 表格（直接 link 到 CR official PDF）
  - ← 返回按鈕

參考：
  - SCR Step 7（NR2）
  - Product 4（撤銷註冊）Step 2（IR1263）, Step 3（NDR1）

---

## Mode C — 純步驟說明（Pure Step Instructions）

hasGenerator: false（冇 generator）
generatorUrl: N/A
冇 documents array（或 documents 為空）
純粹資訊 / 指引頁，冇 form、冇工具、冇下載。

Card 顯示：
  - 步驟標題 + summary
  - 冇 generator card image
  - 冇按鈕（冇 download / 填寫 button）

Generator 頁面：N/A（唔存在 generator page）
Step 只顯示 details 內容（⚠️ 注意事項 + ✅ 要做嘅嘢）

參考：
  - Product 2（公司改名）Step 1（查冊公司名 + 檢查商標）
  - 通用於所有純資訊步驟（research、checklist、注意事項等）

---

## 每個 Step 嘅 JSON 結構判斷方式

| Mode | hasGenerator | documents | generatorUrl | officialFormUrl |
|------|-------------|-----------|-------------|----------------|
| A    | true        | 有（1+ items） | 有（指向 generator） | optional |
| B    | false       | 有（1+ items） | = official PDF URL | required |
| C    | N/A         | 冇 / 空   | N/A         | N/A |

"""
