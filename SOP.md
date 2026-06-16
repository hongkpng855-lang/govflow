# ESGov 內容 SOP — 免費 + 付費內容框架

> 適用於每個流程產品，無論係股份轉讓、周年申報表、定其他政府流程。

---

## 核心原則

### 🚨 黃金規則：先問後做（Agent 必須遵守）

當 user 講「X都要這樣」或任何含糊指示，**必須先確認具體邊個部分**先郁手。
- ❌ 錯：user 話「產品二都要這樣」→ Agent 自己估係 subtitle 定 button width
- ✅ 對：user 話「產品二都要這樣」→ 問「你指邊個部分？button width、subtitle、定全部？」

任何 UI 改動（移除元素、改位置、改 spacing）前，必須先問 user 確認，唔好擅自執行。

每部 Step 都要有 **3 種內容**：

| # | 內容類型 | processes.json 字段 | 免費 (Step 1-2) | 付費 (Step 3-7) |
|---|---------|-------------------|--------------|--------------|
| 1 | 🖼️ **別人做過的 Demo（範例對照）** | `steps[].documents[].demoImage` | ✅ 有 | ✅ 有 |
| 2 | 📥 **可供下載的可更改文件（模板）** | `steps[].documents[].templateFile` | ✅ 有 | ✅ 有 |
| 3 | 📖 **講解要準備的文件** | `steps[].details` + `documents[].description` + `documents[].commonMistakes` | ✅ 有 | ✅ 有 |

**免費 vs 付費嘅唯一分別**：頭 2 步唔鎖，第 3 步起鎖。
**內容質素完全一樣**，確保用戶免費睇到嘅已經感受到價值，先至願意解鎖。

---

## 逐欄填寫指引

### 流程層級 (`processes.json` root)

```json
{
  "processId": "xxx",
  "title": "香港有限公司XXX完整指南",
  "description": "一句講晒個流程做咩、幫到邊啲人",
  "estimatedTime": "預計需時",
  "difficulty": "容易 / 中等 / 困難",
  "totalSteps": 7,
  "freeSteps": 2,
  "price": 149,
  "currency": "HKD",
  "steps": [...]
}
```

### 每個 Step 嘅內容

```json
{
  "stepNumber": 1,
  "title": "步驟名稱（要具體，例如「準備股份轉讓書」）",
  "summary": "一句 summary，講呢步要做咩、注意咩（免費用戶會最先見到）",
  "isFree": true,
  "details": "白話文詳細說明。用「你」/「我」口吻，好似朋友教路咁。\n\n必須包含：\n- 呢份文件係咩\n- 點解要做\n- 常見錯誤（我當初點樣錯過）\n- 正確做法\n- 特別注意事項",
  "documents": [
    {
      "name": "文件正式名稱",
      "description": "呢份文件係咩、用嚟做咩",
      "demoImage": "assets/demo/stepX-filename.jpg（真實填寫範例 screenshot）",
      "templateFile": "templates/filename.docx（可編輯 Word 模板）",
      "commonMistakes": [
        "錯誤 1：XXX",
        "錯誤 2：XXX",
        "錯誤 3：XXX"
      ]
    }
  ],
  "rejectionRisks": [
    "風險 1：XXX → 後果",
    "風險 2：XXX → 後果"
  ]
}
```

---

## 💰 價格比較（增加說服力）

每個流程產品都要加入價格比較，突顯 ESGov 嘅價值：

### 標準句式
```
💰 會計公司行政費 ~~$1,000+~~ → ESGov 只需 HK$149
```

### 放喺網站嘅位置
| 位置 | 頁面 | 作用 |
|------|------|------|
| Trust Signals（置頂） | index.html | 一入嚟就見到 |
| Hero 區 | index.html | 強化價值主張 |
| 流程頁 Step 內容上方 | shareholder-transfer.html | 引導解鎖前提醒 |

### 點樣決定比較價格
- 去 Google 搜尋「[流程名] 報價」
- 睇會計公司/秘書公司嘅收費
- 取最低嘅市場報價做比較基準
- 如果流程係免費嘅（如自行遞交），比較嘅係「時間成本」

### processes.json 設定
每個流程嘅 `priceComparison` 字段決定顯示內容：
```json
{
  "price": 149,
  "priceComparison": {
    "benchmark": 1000,
    "benchmarkLabel": "會計公司行政費",
    "savings": "85%",
    "note": "自行準備文件，唔使俾人食價"
  }
}
```
- `benchmark`：市場價格數字
- `benchmarkLabel`：顯示名稱（如「會計公司行政費／秘書公司收費」）
- 網站會自動顯示「💰 benchmarkLabel ~~$benchmark+~~ → ESGov 只需 $price」

### 例子：股份轉讓
- 會計公司行政費：$1,000 - $3,000
- 比較用最低價：$1,000+
- ESGov 價：$149
- 節省：**85%+**

---

## 3 種內容嘅具體要求

### 1. 🖼️ 別人做過的 Demo（範例對照）

**位置**：`documents[].demoImage`

**要求**：
- 真實填寫過嘅範例（可遮蓋個人資料）
- 用紅色圈/箭嘴標記重點填寫位置
- 圖片放 `assets/demo/` 目錄
- **免費 Step (1-2)**：直接顯示，用戶 click 文件 card 即睇
- **付費 Step (3-7)**：解鎖後同一樣顯示

**格式建議**：JPG/PNG，寬度 1200px，檔案 < 200KB

### 2. 📥 可供下載的可更改文件（模板）

**位置**：`documents[].templateFile`

**要求**：
- Microsoft Word (.docx) 格式
- 已設好格式、留空位俾人填
- 如有需要，加填寫說明 footnote
- 文件放 `templates/` 目錄
- **免費 Step**：免費下載
- **付費 Step**：解鎖後下載

### 3. 📖 講解要準備的文件

**位置**：`details` + `documents[].description` + `documents[].commonMistakes`

**要求**：
- `details`：用口語化廣東話，好似同朋友 WhatsApp 傾偈咁
  - 開頭：呢份文件係咩
  - 中間：點樣準備、注意咩位
  - 結尾：我當初點樣錯過（建立共鳴）
- `documents[].description`：簡介呢份文件嘅用途（1-2 句）
- `documents[].commonMistakes`：列舉 2-4 個最常見嘅錯誤，用「我」角度

---

## 內容生產流程（創辦人適用）

```
1. 揀流程
   └→ 決定總共有幾多 step（一般 5-7 步）

2. 填 processes.json
   ├→ 逐 step 寫 title + summary + details（先寫晒文字）
   ├→ 每步列出所需文件（documents[]）
   ├→ 標記頭 2 步為 isFree: true
   └→ 填 rejectionRisks

3. 製作範例圖片（demoImage）
   ├→ 真實填寫一份，遮蓋個人資料
   ├→ screenshot + 標記重點
   └→ 放入 assets/demo/

4. 製作 Word 模板（templateFile）
   ├→ 開新 .docx，設好格式
   ├→ 留空填寫位
   └→ 放入 templates/

5. 測試
   ├→ 免費 Step 1-2 內容完整顯示
   ├→ 付費 Step 3-7 有鎖 + CTA
   └→ Console 無 error

6. 部署
   └→ bash deploy.sh "新流程：XXX"
```

---

## 品質 Check List（每個 Step 出街前對）

- [ ] **🚨 Agent：改任何 UI 前有問清楚 user 指示**
- [ ] `title` 具體明確（唔係「第一步」咁 hea）
- [ ] `summary` 吸引、有價值（免費用戶會見到）
- [ ] `details` 用口語廣東話、有真實經歷
- [ ] 最少 1 個 `documents[]`
- [ ] 每個 document 有 `demoImage`（範例圖）
- [ ] 每個 document 有 `templateFile`（可下載模板）
- [ ] 每個 document 有 2+ `commonMistakes`
- [ ] `rejectionRisks` 有 1-2 個（用家最驚呢啲）
- [ ] Console 冇 JavaScript errors
- [ ] Mobile 上所有步驟可點擊

---

*SOP 版本: 3.0 · 2026-06-11*

---

## 📋 新產品研發流程（Product Expansion SOP）

當需要研發新產品時，跟以下步驟自動執行：

### Phase 1：產品揀選（選定流程）
選擇同類別嘅公司秘書/政府流程，例如：
- 公司註銷（Dissolution / Deregistration）
- 董事變更 / 辭任（Change / Resignation of Director）
- 公司改名（Change of Company Name）
- 股份配發（Allotment of Shares）
- 重要控制人登記冊（SCR / Significant Controllers Register）
- 公司秘書變更（Change of Company Secretary）
- 註冊地址變更（Change of Registered Address）
- 商業登記更新（Business Registration Update）

### Phase 2：資料搜集（Research）— 詳細爬蟲 SOP

#### Step 2.1 — 搜尋流程（搵 8-10 個來源）
1. 用 web_search 搜尋最少 3 組關鍵字（中文 + 英文）：
   - `香港 [流程名] 流程 步驟`
   - `Hong Kong [process name] procedure steps`
   - `[流程名] 條件 費用 所需文件`
2. 每組取前 10 結果，揀 8-10 個 **唔同 domain** 嘅獨立網站
   - 優先採集：gov.hk、cr.gov.hk（官方）
   - 然後：accounting firm 網站（patcpa、osome、acaccountinghk 等）
   - 最後：創業/商業資訊網站
3. 用 web_extract 取得每個網站嘅完整流程內文

#### Step 2.2 — 比對確認流程
- 比較各網站嘅：步驟數、順序、費用、所需文件清單
- **確認標準**：如果 80% 以上網站流程一致 → 流程有效
- 如有差異：以官方來源（gov.hk / cr.gov.hk / ird.gov.hk）爲準

#### Step 2.3 — 搜尋真實案例同痛點
1. 搜尋討論區：`[流程名] 經歷 陷阱 中伏 罰款 site:lihkg.com OR site:discuss.com.hk`
2. 搜尋經驗分享：`[流程名] 經驗分享 犯錯 被退回`
3. 記錄每個痛點（原文引用）+ 來源
4. 搜尋真實範例：
   - `[流程名] 範例 樣本`
   - `[流程名] specimen sample filled`
   - 去 cr.gov.hk 搵 Specimen / fillable 版本

#### Step 2.4 — 搜集官方表格
- cr.gov.hk：搵相關表格（PDF + Word fillable 版本）
- ird.gov.hk：搵稅局相關表格（IR1263、IRC3113 等）
- 用 curl / web_fetch 直接 download

#### Step 2.5 — 記錄市場價格
- Google「[流程名] 報價 會計公司」
- 取最低市場報價做比較基準
- 記錄政府費用總和

#### 完成 Output
- 將所有 findings 整合成一個 JSON research file：`{product-id}-research.json`
- 格式參考 `company-dissolution-research.json`

### Phase 3：內容製作（Content Creation）
1. 決定總 steps（一般 5-7 步，每步對應一份核心文件）
2. 為每個 step 寫 content（title + summary + details + common mistakes）
3. 製作 processes.json 完整區塊（copy step 1 嘅格式做 template）
4. 建立產品 HTML 頁（copy shareholder-transfer.html 做基礎）
5. **Generator 製作：任何 Step 都可以有 Generator**（唔限 Step 1）
   - 見 `product-launch-sop.md` →「Generator 製作流程」詳細步驟
   - 已實現嘅 Generator 基準：`letter-of-transferee-generator.html`（最新）
   - 亦可以參考：`sold-note-generator.html`、`instrument-transfer-generator.html`
   - 每個 generator 需要：
     - Generator HTML 頁面（copy 現有 generator → 改 form layout）
     - `processes.json` → document 加 `hasGenerator: true` + `generatorUrl`
     - `deploy.sh` → 加新頁到 ALLOWED_PAGES
     - `scripts/generate-sitemap.py` → 加新頁到 PRIORITY

### Phase 4：文件製作（Templates & Images）
1. 從官方 source download 表格作為 template 基礎
2. 如需 Word 模板：製作可編輯 .docx
3. 如需 demo 圖：製作範例 screenshot（遮蓋個人資料）
4. 如需 wordtopdf 圖：跟 Wordtopdf 製作流程

### Phase 5：儲存（Save for Review）
- 所有檔案放喺 /mnt/c/Users/hongk/Desktop/esgov/ 對應目錄
- processes.json → 加新產品區塊但 mark 爲 `"isActive": false`
- HTML 頁面 → 建立但唔 deploy
- 完成後整理一份清單俾用戶 review

---

## 📋 Wordtopdf 製作流程（Generator Demo 圖片）

每次製作/更新 Generator 嘅 Demo 圖（wordtopdf）時：

### 1. 製作流程
1. 根據用戶提供嘅最新 Word 模板，製作 HTML 模擬版
2. 用 Chromium headless cap 圖生成 PNG（2x scale 確保清晰）
3. 圖片必須包含 **水印**（右下角「示範範例 · ESGov」）
4. 儲存到 `assets/demo/{product-id}-wordtopdf.png`
5. 將生成好嘅 PNG **原件副本** 傳俾用戶確認

### 2. Generator PDF 水印規範
所有 generator 下載嘅 PDF 必須有：
- **跨頁斜水印**：半透明（12% opacity）灰字「ESGov · 示範範例」
- 斜線排列，左上至右下分佈
- 不能遮蓋主要內容（水印放底層）
- 顏色：`rgb(180,180,180)`

### 3. Demo 圖片水印規範
- 所有 `assets/demo/` 嘅 product demo 圖必須有水印
- 位置：右下角
- 文字：「示範範例 · ESGov」
- 顏色：淺灰半透明

### 4. 驗收清單
- [ ] 已將原件副本 send 俾用戶
- [ ] Demo 圖有水印（右下角「示範範例 · ESGov」）
- [ ] Generator PDF 有跨頁斜水印
- [ ] 水印透明度合適（唔遮內容但又清晰可見）

---

## 📋 WYSIWYG Generator 製作流程（html2canvas + jsPDF 多頁模式）

適用於互動填寫後截圖生成 PDF 嘅 Generator（SCR 系列 generator 標準模式）。

### 架構要點

```
User 填寫 <input>/<select>/<textarea> →
  html2canvas 截取 #pdf-form →
  canvas slice 多頁 →
  每頁 addImage → jsPDF save
```

### 1. Generator HTML 結構

- 載入套件：html2canvas 1.4.1 + jsPDF 2.5.1（CDN）
- 表單容器：`<div id="pdf-form">` — 模擬 A4 紙張外觀
- 所有輸入用標準 `<input type="text">` / `<select>` / `<textarea>`
- Field 命名：`f-{fieldname}`（如 `f-company`, `f-date`）

### 2. ⚠️ html2canvas input rendering fix（必做）

html2canvas **唔識 render** `<input>` / `<select>` / `<textarea>` 嘅文字值。Capture 前必須替換：

```javascript
// Capture 前：將 input 替換為 span（保留文字）
const inputReplacements = [];
document.querySelectorAll('#pdf-form input:not([type=checkbox]):not([type=hidden]), #pdf-form select, #pdf-form textarea').forEach(function(el) {
  var span = document.createElement('span');
  span.className = 'input-replacement';
  if (el.tagName === 'SELECT') {
    span.textContent = el.options[el.selectedIndex] ? el.options[el.selectedIndex].text : '';
  } else {
    span.textContent = el.value || '';
  }
  var style = getComputedStyle(el);
  span.style.cssText = 'font:' + style.font + ';color:' + style.color + ';border-bottom:1px solid #999;background:transparent;padding:2px 4px;white-space:pre-wrap;display:inline-block;min-width:80px;';
  el.parentNode.insertBefore(span, el);
  el.style.display = 'none';
  inputReplacements.push({ original: el, replacement: span });
});

// Capture 後：還原 inputs
inputReplacements.forEach(function(item) {
  item.replacement.remove();
  item.original.style.display = '';
});
```

### 3. 📄 多頁 PDF split（必做）

避免成個 document 縮落一頁 A4 導致文字 cut off：

```javascript
const imgData = canvas.toDataURL('image/png');
const doc = new jsPDF('p', 'mm', 'a4');
const pageW = 210, pageH = 297, margin = 10;
const contentW = pageW - margin * 2;
const contentH = pageH - margin * 2;

// 計算 canvas slice 高度
const pxRatio = canvas.width / contentW;
const pagePxH = contentH * pxRatio;
const totalPages = Math.ceil(canvas.height / pagePxH);

for (let i = 0; i < totalPages; i++) {
  if (i > 0) doc.addPage();
  const srcY = i * pagePxH;
  const srcH = Math.min(pagePxH, canvas.height - srcY);
  const tempCanvas = document.createElement('canvas');
  tempCanvas.width = canvas.width;
  tempCanvas.height = srcH;
  const ctx = tempCanvas.getContext('2d');
  ctx.drawImage(canvas, 0, srcY, canvas.width, srcH, 0, 0, canvas.width, srcH);
  const pageImgData = tempCanvas.toDataURL('image/png');
  const pageImgH = contentW * (srcH / canvas.width);
  const yOffset = margin + (contentH - Math.min(pageImgH, contentH)) / 2;
  doc.addImage(pageImgData, 'PNG', margin, yOffset, contentW, Math.min(pageImgH, contentH));
}
```

### 4. 生成前 sync 所有動態字段

Capture 前確保所有 JS 更新嘅數值已同步：

```javascript
// Call all sync functions
updateDeadlineDisplay();
updateTestTable();
// ... etc
await new Promise(r => setTimeout(r, 300));
```

### 5. Email Gate 整合（選用）

下載前彈出 email modal，留低 email 後先繼續生成：

```javascript
// 按「下載」→ check email gate
const emailDone = localStorage.getItem('esgov_email_done');
if (!emailDone) { showEmailGate(); return; }

// Email submit → save to localStorage + generate PDF
function submitDownloadEmail() {
  const email = document.getElementById('downloadEmail').value;
  if (!email.includes('@')) return;
  localStorage.setItem('esgov_email_done', 'true');
  closeEmailGate();
  setTimeout(function(){ generatePDF(); }, 100);
}
```

### 6. Debug 要點

- html2canvas logging 設 false（否則 console 好嘈）：`html2canvas(el, { logging: false, ... })`
- scale=3 確保高清（但會慢啲，手機要考慮）
- capture-mode class：隱藏非表單 UI（header, footer, buttons）再 capture
- `await document.fonts.ready` — 確保字型載入先 capture
- Watermark 用 `doc.saveGraphicsState()` + `setGState({ opacity: 0.12 })` + `restoreGraphicsState()`
