# ESGov 新產品上線 SOP

## 核心原則

**每個新產品跟返產品 1（股份轉讓指南）嘅 format 做 template。**

產品 1 嘅每個 Step 有以下 format：

### Step Format（跟產品 1）
```
每個 Step =
  1. 詳細說明（白話文 + 真實經歷）
  2. 所需文件 card（跟 Step 1 嘅互動工具 format / Step 2-5 嘅文件 format）
  3. Demo 範例圖片（真實案例 + 可修改文件/Word to PDF）
  4. 常見錯誤列表
```

### Step 1 Format（互動工具版本）
```
┌─────────────────────────────────┐
│  [真實案例圖]    [可修改文件圖]    │  ← 兩張並排
│         🏷️ 互動工具             │
├─────────────────────────────────┤
│  文件名稱                        │
│  文件描述                        │
│  🚀 填寫 + 生成 PDF              │  ← link 去 generator
└─────────────────────────────────┘
```
**需要：**
- `{step}-realdemo.png?v=9.0` — 真實填寫範例（user 提供）
- `{step}-wordtopdf.png?v=9.0` — 可編輯文件範本（需要製作）
- `{product-id}-generator.html` — 互動填寫工具頁
- `processes.json` → `hasGenerator: true`

### Step 2-5 Format（文件版本）
```
┌─────────────────────────────────┐
│  📄 文件名稱                     │
│  文件描述                        │
│  👁️ 檢視範例 PDF                 │  ← click 開 overlay
└─────────────────────────────────┘
```
**需要：**
- `{step}-realdemo.png?v=9.0` — 真實範例圖（user 提供）
- `processes.json` → `hasGenerator: false`
- 無 generator page

---

## Phase A：產品內容準備

- [ ] Copy `processes.json` 嘅產品 1 區塊做 template
- [ ] Copy `shareholder-transfer.html` → `{product-id}.html` 改內容
- [ ] 如需 generator：copy `sold-note-generator.html` → `{product-id}-generator.html`
- [ ] 更新 `index.html` featured card（copy 現有 card 改 link + title）
- [ ] 每步準備 demo 圖片（realdemo + wordtopdf）
- [ ] 確認 interaction tool 有 `hasGenerator: true`

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

**Step 3 — 先確認正常，再話完成**

---

## 參考 template

| File | Source |
|------|--------|
| `processes.json` | Copy 產品 1 嘅 JSON block 改資料 |
| `{product-id}.html` | Copy `shareholder-transfer.html` |
| `{product-id}-generator.html` | Copy `sold-note-generator.html` |
| `index.html` featured card | Copy 現有 card 改 href |
| `assets/demo/*.png` | user 提供 realdemo / 自己製作 wordtopdf |
