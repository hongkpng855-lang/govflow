# ESGov 新產品上線 SOP

## 核心原則

**每個新產品跟返產品 1（股份轉讓指南）嘅 format 做 template。**

### Step Format（跟產品 1）
```
每個 Step =
  1. 詳細說明（白話文 + 真實經歷）
  2. 所需文件 card（如有 Generator 用互動工具格式，冇就用文件格式）
  3. Demo 範例圖片（真實案例 + 可修改文件/Word to PDF）
  4. 常見錯誤列表
```

### 互動工具格式（任何 Step 都可以有 Generator）
```
┌─────────────────────────────────┐
│  [真實案例圖]    [可修改文件圖]    │  ← 兩張並排
│         🏷️ 互動工具              │
├─────────────────────────────────┤
│  文件名稱                        │
│  文件描述                        │
│  🚀 填寫 + 生成 PDF              │  ← link 去 generator
└─────────────────────────────────┘
```
**需要：**
- `{step}-realdemo.png?v=9.x` — 真實填寫範例（已 blur/watermark）
- `{step}-wordtopdf.png?v=9.x` — 可編輯文件範本（空白模板 screenshot）
- `{product-id}-generator.html` — **根據真實文件重新設計 form layout**
- `processes.json` → `hasGenerator: true` + `generatorUrl`

### 文件格式（冇 Generator）
```
┌─────────────────────────────────┐
│  📄 文件名稱                     │
│  文件描述                        │
│  👁️ 檢視範例 PDF                 │  ← click 開 overlay
└─────────────────────────────────┘
```
**需要：**
- `{step}-realdemo.png?v=9.x` — 真實範例圖
- `processes.json` → `hasGenerator: false`（default）
- 無 generator page

---

## Phase A：產品內容準備

- [ ] Copy `processes.json` 嘅產品區塊做 template
- [ ] Copy `shareholder-transfer.html` → `{product-id}.html` 改內容
- [ ] 如需 generator：按照下面「Generator 製作流程」建立
- [ ] 更新 `index.html` featured card（copy 現有 card 改 link + title）
- [ ] 每步準備 demo 圖片（realdemo + wordtopdf）

## Generator 製作流程（詳細）

當需要為某個 Step 製作 Generator 時，跟以下步驟：

### Step 1 — 分析 Word 模板
```bash
python3 -c "
from docx import Document
doc = Document('templates/{filename}.docx')
for i, p in enumerate(doc.paragraphs):
    if p.text.strip():
        print(f'{i}: {p.text}')
"
```
- 標記所有 fillable fields（公司名、人名、日期、簽名等）
- 留意 checkbox / radio 選項
- 記錄簽名位（通常需要「親筆簽署後掃描」提示）

### Step 2 — Copy 現有 Generator 做 Template
- Copy `sold-note-generator.html` → `{product-id}-generator.html`
- 修改以下部分：

#### 2a. Head meta tags
- `<title>` — 改為新產品名稱
- `<meta name="description">` — 改為新產品描述
- `<meta property="og:title">` / `og:description` / `og:url` — 對應更新
- `<link rel="canonical">` — 更新為新網址

#### 2b. Navigation
- Back link: `href="shareholder-transfer.html"`（指向產品頁）

#### 2c. 參考圖片
```html
<img src="assets/demo/{step}-realdemo.png?v=9.x" alt="真實案例" />
<img src="assets/demo/{step}-wordtopdf.png?v=9.x" alt="可修改文件" />
```
更新 `openTemplateModal()` 嘅兩個 tab 嘅圖片 src

#### 2d. 文件說明 + 常見錯誤
- 更新文件名稱同描述
- 更新常見錯誤列表（從 processes.json 直接 copy）

#### 2e. 表單 FORM（最重要部分）
- Header bar：改標題（`LETTER OF TRANSFEREE OF SHARES`、中文名）
- 設計 field layout 跟 Word template 結構
- 每個 field 用 `contenteditable="true"` 嘅 `div`
- Field ID 命名：`f1`, `f2`, ... `fN`
- 日期 field 加 `class="field-date"`
- 特殊互動（checkbox/radio 選項）用 JavaScript 自訂

#### 2f. getVals() 更新
```javascript
function val(id) { return (document.getElementById(id).textContent || '').trim(); }
function sig(id) { const v=val(id); return (v && v !== '親筆簽署後掃描') ? v : '________________'; }
return {
  f1: val('f1'),
  f2: val('f2'),
  ...
  fN: sig('fN'),  // 簽名位用 sig()
  fDate: dateStr,
  // 如有選項邏輯：
  selectedOption: selectedOption || '1',
};
```

#### 2g. downloadPDF() 更新
- Field map：`const vMap = { f1:'f1', f2:'f2', ..., fN:'fN' }`
- PDF filename：`doc.save('{Product_Name}_Filled.pdf')`
- Email gate fields：
  - `page: '{product-id}-generator'`
  - `docType: '{文件中文名（英文名）}'`
  - `_subject: '📬 ESGov 新下載（{中文名}）：' + email`

### Step 3 — 更新 processes.json
- 該文件嘅 document 加：
  ```json
  "hasGenerator": true,
  "generatorUrl": "{product-id}-generator.html"
  ```

### Step 4 — 更新 deploy.sh
- 加新頁名到 `ALLOWED_PAGES` 變數
- 加新頁名到 version badge sed 命令

### Step 5 — 更新 sitemap.py
- 加新頁到 `PRIORITY` dict（generator 統一 priority `0.8`）

### Step 6 — 更新 overlay 邏輯（如有需要）
- `shareholder-transfer.html` 嘅 overlay 已自動支援任何有 `generatorUrl` 嘅 step
- 預設 template 邏輯：
  ```
  有 generatorUrl → 「🚀 前往 PDF 生成器」
  冇 generatorUrl + 有 templateFile → 「📥 下載可編輯模板」
  兩樣都冇 → 「（此文件暫無可編輯模板）」
  ```

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
| `{product-id}-generator.html` | Copy `letter-of-transferee-generator.html`（最新基準） |
| `index.html` featured card | Copy 現有 card 改 href |
| `assets/demo/*.png` | 用戶提供 realdemo / 自己製作 wordtopdf |
| `deploy.sh` | 加新 HTML 到 ALLOWED_PAGES |
| `scripts/generate-sitemap.py` | 加新 HTML 到 PRIORITY |
