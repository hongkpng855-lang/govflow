# GovFlow 內容 SOP — 免費 + 付費內容框架

> 適用於每個流程產品，無論係股份轉讓、周年申報表、定其他政府流程。

---

## 核心原則

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

每個流程產品都要加入價格比較，突顯 GovFlow 嘅價值：

### 標準句式
```
💰 會計公司行政費 ~~$1,000+~~ → GovFlow 只需 HK$149
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
- 網站會自動顯示「💰 benchmarkLabel ~~$benchmark+~~ → GovFlow 只需 $price」

### 例子：股份轉讓
- 會計公司行政費：$1,000 - $3,000
- 比較用最低價：$1,000+
- GovFlow 價：$149
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

*SOP 版本: 1.0 · 2026-06-04*
