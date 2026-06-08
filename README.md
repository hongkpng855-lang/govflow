# ESGov — 香港政府流程指南平台

一個為香港老闆而設嘅公司秘書文件指南平台。由真實經歷者整理，逐個步驟帶你完成文件程序。

## MVP 範圍

**香港有限公司股份轉讓完整指南**
- 7 個步驟，頭 2 步免費試睇
- 15+ 份文件模板可下載
- 真實填寫範例對照
- 一次性解鎖 HK$149

## 技術棧

- **HTML** + **Tailwind CSS** (CDN) + **Alpine.js**
- 內容由 **JSON** 驅動（創辦人可直接編輯）
- 無需 build 步驟，可直接上傳至任何靜態主機

## 專案結構

```
esgov/
├── index.html                  # 首頁
├── shareholder-transfer.html   # 股份轉讓流程詳情頁
├── processes.json              # ⭐ 內容資料（創辦人編輯呢個檔）
├── assets/
│   ├── css/style.css           # 自訂樣式
│   ├── js/app.js               # Alpine.js 應用邏輯
│   └── demo/                   # 範例圖片放呢度
├── templates/                  # 可下載 Word 模板放呢度
└── esgov_flow.txt            # 原始技術規格
```

## 創辦人手冊

### 如何修改內容（唔使寫 Code）

1. 打開 `processes.json`
2. 修改 `steps` 陣列入面嘅資料：
   - `title` — 步驟名稱
   - `summary` — 簡短說明
   - `details` — 詳細內容（用繁體白話文）
   - `documents` — 所需文件列表
   - `rejectionRisks` — 常見錯誤導致補交
3. 儲存檔案即時生效（直接重新整理頁面）

### 如何加入範例圖片

1. 將圖片放入 `assets/demo/` 資料夾
2. 喺 `processes.json` 中對應嘅 `demoImage` 欄位填上圖片路徑
3. 建議圖片尺寸：16:9 比例，寬度至少 800px

### 如何加入下載模板

1. 將 Word / PDF 檔案放入 `templates/` 資料夾
2. 喺 `processes.json` 中對應嘅 `templateFile` 欄位填上檔案路徑

### 如何設定付款

1. 去 [Stripe](https://stripe.com) 建立一個 Payment Link
2. 或者用 [Lemon Squeezy](https://lemonsqueezy.com)
3. 將付款連結貼入 `shareholder-transfer.html` 中嘅 `goToPayment()` 函數（搜尋 `buy.stripe.com`）

### 如何部署

#### GitHub Pages（推薦）

1. 開一個 GitHub repo，推送上所有檔案
2. 去 repo Settings → Pages → 選擇 Branch `main` / `(root)`
3. 一分鐘內網站就會上線

#### Cloudflare Pages

1. 登入 Cloudflare Pages
2. 建立新專案 → 連線 GitHub repo
3. Build settings 可以全部留空（純靜態）
4. 部署完成

## 免責聲明

本網站提供嘅內容僅供參考，並不構成法律意見。如有具體法律問題，請諮詢執業律師或專業公司秘書。

---

*由 ESGov 開發者維護*
