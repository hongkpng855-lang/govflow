# ESGov 新產品上線 SOP

## 核心原則

**每個新產品跟返產品 1（股份轉讓指南）嘅 format 做 template。**

### Generator 頁面 — 兩種模式

所有文件都要有獨立 Generator 頁面，分兩種模式：

#### 模式 A：🚀 互動填寫（WYSIWYG — 截圖生成 PDF）

適用於需要填寫後生成 PDF 嘅文件（Step 1-6）。**最新標準係 html2canvas + jsPDF 截圖模式**（SCR 系列 generator），唔再用 contenteditable。

```html
<!-- CDN 載入 -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>

<!-- 表單容器：模擬 A4 紙張 -->
<div id="pdf-form">
  <input type="text" id="f-company" />
  <select id="f-type">...</select>
  <textarea id="f-address">...</textarea>
</div>

<!-- 生成按鈕 -->
<button onclick="generatePDF()">📄 下載 PDF</button>
```

```
┌─────────────────────────────────┐
│  [真實案例圖]    [可修改文件圖]    │  ← 兩張並排 + modal 放大
│         🏷️ 互動工具              │
├─────────────────────────────────┤
│  文件說明 + 常見錯誤             │
├─────────────────────────────────┤
│  📄 線上填寫表單 (input/select)  │  ← 用標準 HTML input fields
│  [field 1], [field 2], ...      │
├─────────────────────────────────┤
│  🚀 下載 PDF（一鍵生成）          │  ← html2canvas + jsPDF 多頁
└─────────────────────────────────┘
```

**需要：**
- `{step}-realdemo.png` — 真實填寫範例
- `{step}-wordtopdf.png` — 空白模板 screenshot
- `{product-id}-generator.html` — **標準 HTML 表單（input/select/textarea）**
- `processes.json` → `hasGenerator: true` + `generatorUrl`
- 卡面顯示：**🚀 填寫 + 生成 PDF**

**⚠️ 關鍵坑（v12.1-v12.2 已 fix）：**
1. **html2canvas input rendering** → capture 前必須將 `<input>/<select>/<textarea>` 替換為 `<span>`，capture 後還原（見 SOP.md WYSIWYG section）
2. **多頁 PDF split** → 唔可以將整頁縮落一頁 A4，要用 canvas slice 逐頁 addImage（見 SOP.md）
3. **Capture mode** → capture 前加 `capture-mode` class 隱藏 header/footer/buttons

#### 模式 B：👁️ 範例+下載（淨係連結去官方嘅文件版本）

適用於政府官方表格或第三方文件唔需要互動填寫（Step 4-5）。

```
┌─────────────────────────────────┐
│         🖼️ 範例圖片              │  ← 官方 PDF 截圖 / SVG
├─────────────────────────────────┤
│  文件說明 + 常見錯誤             │
├─────────────────────────────────┤
│  📥 下載官方 fillable PDF        │  ← 官方表格下載
│  📄 查看官方表格（公司註冊處）    │  ← 官網連結
│  ← 返回完整指南                  │
└─────────────────────────────────┘
```

**需要：**
- `{step}-demo.png` 或 `{step}-demo.svg` — 示範圖片（官方 PDF 截圖優先）
- `templates/{filename}.pdf` 或 `.docx` — 可供下載嘅模板
- `processes.json` → `generatorUrl`（有但 `hasGenerator` 唔 set / `false`）
- 卡面顯示：**👁️ 檢視範例 PDF**

---

## 兩種模式比較

| 特性 | 模式 A 🚀 互動填寫 | 模式 B 👁️ 範例+下載 |
|------|:---:|:---:|
| 線上編輯表單 | ✅ | ❌ |
| 一鍵生成 PDF | ✅ | ❌ |
| 官方表格下載 | ❌（用自訂 template） | ✅ |
| 官方網站連結 | ❌ | ✅ |
| `hasGenerator` | `true` | 唔 set |
| `generatorUrl` | `{id}-generator.html` | `{id}-generator.html` |
| 卡面按鈕 | 🚀 填寫 + 生成 PDF | 👁️ 檢視範例 PDF |
| 示例 | Sold Note, Instrument, Letter | Audit Report, NAR1, NSC1 |

---

## Phase A：產品內容準備

- [ ] Copy `processes.json` 嘅產品區塊做 template
- [ ] Copy `shareholder-transfer.html` → `{product-id}.html` 改內容
- [ ] 如需 generator：按照下面「Generator 製作流程」建立
- [ ] 更新 `index.html` featured card（copy 現有 card 改 link + title）
- [ ] 每步準備 demo 圖片（realdemo + wordtopdf）

## Generator 製作流程（詳細）

當需要為某個 Step 製作 Generator 時，先決定用 **模式 A（互動填寫）** 定 **模式 B（範例+下載）**。

### 模式 A：互動填寫 Generator（WYSIWYG html2canvas 模式 — SCR 系列 generator 標準）

最新 generator 使用 **html2canvas + jsPDF 截圖模式**（唔再用 contenteditable）。

#### Step 1 — Copy 現有 Generator 做 Template
- Copy `scr-notice-generator/index.html` → `{product-id}-generator/index.html`
- 或者 copy `scr-shareholder-analysis-generator/index.html`（table-based layout）

#### Step 2 — 修改 Head + Navigation
- `<title>` — 產品名稱
- `<meta name="description">` — 產品描述
- OG / canonical — 對應更新
- 導航 back link：指向產品頁

#### Step 3 — 參考圖片
```html
<img src="/assets/demo/{step}-realdemo.png?v=12.x" alt="真實案例" />
<img src="/assets/demo/{step}-wordtopdf.png?v=12.x" alt="可修改文件" />
```
更新 modal 內嘅兩個 tab 圖片 src

#### Step 4 — 文件說明 + 常見錯誤
更新文件名稱、描述同常見錯誤列表（從 processes.json copy）

#### Step 5 — 表單結構 (#pdf-form)
- 用 `<input type="text">` / `<select>` / `<textarea>`（標準 HTML，唔係 contenteditable）
- Field id：`f-{fieldname}`（如 `f-company`, `f-date`）
- 日期 field 用 `<input type="date">`
- 簽名位用 `<input type="text" placeholder="親筆簽署後掃描">`
- **Field ID 命名同 getVals/sync 對應**

#### Step 6 — PDF 生成邏輯 (generatePDF)
參考 `scr-notice-generator/index.html` 嘅 `generatePDF()` 函數，包括：
- input→span 替換（html2canvas rendering fix）
- canvas slice 多頁 split
- capture mode class toggle
- email gate 檢查
- watermark 疊加

#### Step 7 — 更新 processes.json
```json
{
  "hasGenerator": true,
  "generatorUrl": "/{product-id}-generator"
}
```

#### Step 8 — 更新 deploy.sh
- 加 `{product-id}-generator/index.html` 到 SED_FILES

#### Step 9 — 更新 sitemap.py
- 加新頁到 PRIORITY dict（generator 統一 priority `0.8`）

> **舊 pattern（contenteditable，已 deprecated）：**
> 如果需要參考舊嘅 contenteditable generator（`sold-note-generator.html`），可以睇 git history 嘅 v12.0 以前版本。
> 主要分別：contenteditable 用 `div[contenteditable=true]` 配合 `textContent` 提取數值；html2canvas 模式用標準 input fields + canvas capture 保證 WYSIWYG 輸出。

### 模式 B：範例+下載 Generator（Audit Report, NAR1, NSC1 模式）

#### Step 1 — Copy 現有 Generator 做 Template
- Copy `nar1-generator.html` → `{product-id}-generator.html`

#### Step 2 — 修改以下部分
- **Head meta tags**：title, description, OG, canonical
- **Navigation**：back link → 指向產品頁
- **Trust Banner**：改為對應嘅說明文字
- **Demo 圖片**：`src="assets/demo/{step}-demo.png"`
  - 優先使用官方 PDF 第一頁截圖（`pdftoppm -png -r 150 -f 1 -l 1`）
  - 如果冇官方 PDF，用自製 SVG
- **文件說明 + 常見錯誤**：從 `processes.json` copy 對應內容
- **下載按鈕**：`href="templates/{filename}.pdf"`（官方 fillable PDF）
- **官方表格連結**：指向 cr.gov.hk 或其他政府網站（如適用）

#### Step 3 — 更新 processes.json
- 該文件嘅 document 加：
  ```json
  "generatorUrl": "{product-id}-generator.html",
  "templateFile": "templates/{filename}.pdf",
  "officialFormUrl": "https://...（如有）"
  ```
- 唔好 set `hasGenerator`（留空 = false）

#### Step 4 — 更新 deploy.sh + sitemap.py（同模式 A）

### 卡面顯示邏輯（shareholder-transfer.html）
- `hasGenerator == true` + `generatorUrl` → **🚀 填寫 + 生成 PDF**（模式 A）
- `generatorUrl` 有但 `hasGenerator` 唔 set → **👁️ 檢視範例 PDF**（模式 B）
- 冇 `generatorUrl` + 有 `templateFile` → **📥 下載可編輯模板**（overlay 內）
- 兩樣都冇 → 「（此文件暫無可編輯模板）」

---

## Phase B：SEO 關鍵字研究
- [ ] 確定 1 主關鍵字 + 2-3 related keywords
- [ ] Keyword research via Google Suggest

## Phase C：On-Page SEO
- [ ] title, description, canonical, OG tags
- [ ] 內容 keyword optimization
- [ ] Internal linking

## Phase D：技術部署
- [ ] `python3 scripts/generate-sitemap.py`
- [ ] `python3 scripts/seo-checker.py`
- [ ] `bash deploy.sh "message" vX.Y`
- [ ] Browser visual check（見下面 Verification SOP）
- [ ] Google Search Console submit URL

## Phase E：追蹤優化
- [ ] 第 1-4 週 monitor Search Console

---

## ✅ Deployment Verification SOP（每次 deploy 後必做）

**Step 1 — Server check**
- [ ] File accessible（200 OK）
- [ ] processes.json path 正確
- [ ] version.json 已更新

**Step 2 — Browser visual check**
- [ ] 開 browser 去受影響頁面
- [ ] 檢查對應元素是否 visible（snapshot / screenshot）
- [ ] 如係圖片 → 確認 `<img>` 有載入
- [ ] 如係 interactive → 實際 click 一次
- [ ] generator 頁面 form fields 正常顯示
- [ ] generator「下載 PDF」掣運作正常

**Step 3 — 先確認正常，再話完成**

---

## 參考 template

| File | Source |
|------|--------|
| `processes.json` | Copy 產品嘅 JSON block 改資料 |
| `{product-id}.html` | Copy `shareholder-transfer.html` |
| `{product-id}-generator.html`（模式 A 🚀） | Copy `sold-note-generator.html`（互動填寫） |
| `{product-id}-generator.html`（模式 B 👁️） | Copy `nar1-generator.html`（範例+下載） |
| `index.html` featured card | Copy 現有 card 改 href |
| `assets/demo/*.png` | 用戶提供 realdemo / `pdftoppm` 官方 PDF 截圖 |
| `deploy.sh` | 加新 HTML 到 ALLOWED_PAGES |
| `scripts/generate-sitemap.py` | 加新 HTML 到 PRIORITY |
