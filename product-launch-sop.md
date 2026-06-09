# ESGov 新產品上線 SOP

## 分階段執行流程

---

## Phase A：產品內容準備

**目標：準備好產品資料同內容**

- [ ] 確認產品名稱（e.g.「香港公司股份轉讓完整指南」）
- [ ] 確認步驟數量（Step 1-5）
- [ ] 收集每步所需文件清單
- [ ] 撰寫 Step 1-5 嘅詳細內容（白話文、真實經歷）
- [ ] 準備範例圖片 / 可下載模板
- [ ] 更新 `processes.json`
- [ ] 建立新 HTML 頁（copy 現有 template）
- [ ] 更新首頁 featured card
- [ ] Deploy

---

## Phase B：SEO 關鍵字研究

**目標：找出產品相關嘅主要關鍵字**

- [ ] 用 Google Search Console 睇 existing keywords
- [ ] 用 Google Suggest（打關鍵字睇 autocomplete）
- [ ] 睇競爭對手 page title
- [ ] 確定 1 個主關鍵字 + 2-3 個 related keywords
- [ ] 記錄落 keyword tracker

| 關鍵字 | 搜尋量（估算） | 競爭度 | 目標頁 |
|--------|-------------|-------|-------|
| e.g. 香港公司股份轉讓 | 高 | 中 | shareholder-transfer.html |

---

## Phase C：On-Page SEO 優化

**目標：針對關鍵字優化頁面元素**

### C1 — Meta Data
- [ ] `<title>`：`ESGov | [主關鍵字] | [副標題]`（50-60 chars）
- [ ] `<meta description>`：含主關鍵字 + CTA（120-160 chars）
- [ ] `<link rel="canonical">`：指向正確 URL
- [ ] Open Graph tags（og:title, og:description, og:url, og:image）

### C2 — 內容結構
- [ ] 只有一個 `<h1>`，含主關鍵字
- [ ] `<h2>` / `<h3>` 自然含 related keywords
- [ ] 內容大約 800-1500 字
- [ ] 圖片全部有 `alt`（含關鍵字）
- [ ] 內文自然重複主關鍵字 3-5 次

### C3 — Internal Linking
- [ ] 喺相關 blog 文章加 link 去新產品頁
- [ ] 喺新產品頁加 link 去相關 blog
- [ ] Anchor text 用自然描述（唔好用「按這裡」）

### C4 — Structured Data
- [ ] FAQPage JSON-LD（如有 FAQ）
- [ ] Product schema（如有價錢）

---

## Phase D：技術部署

**目標：確保技術上 correctly deployed**

- [ ] 行 `python3 scripts/generate-sitemap.py` 更新 sitemap
- [ ] 行 `python3 scripts/seo-checker.py` 確認冇 error
- [ ] Deploy 上線
- [ ] 提交新 URL 去 Google Search Console →「要求索引編制」
- [ ] 檢查 Google Search Console 有冇 error

---

## Phase E：追蹤 & 優化（上線後）

**目標：監察成效，持續改善**

### 第 1 週
- [ ] Check Google Search Console 新頁面有冇被 index
- [ ] 如果有 error → 修正

### 第 2-4 週
- [ ] 睇 Search Console「成效」：曝光次數、點擊率、平均排名
- [ ] Check 邊個 keyword 帶最多 traffic
- [ ] 如果排名唔理想 → 改善內容 / 加 internal links

### 每月
- [ ] 更新 sitemap
- [ ] 檢查 Search Console「涵蓋範圍」
- [ ] 比較 keyword 排名變化

---

## 📐 新產品快速 Checklist

```
□ Phase A: 內容準備
□ Phase B: 關鍵字研究
□ Phase C1: Meta Data
□ Phase C2: 內容結構
□ Phase C3: Internal Linking
□ Phase C4: Structured Data
□ Phase D: 技術部署
□ Phase E: 追蹤優化
```

---

## 相關檔案

| 檔案 | 用途 |
|------|------|
| `SEO-SOP.md` | Google 曝光操作指南 |
| `scripts/seo-checker.py` | 全站 SEO 健康檢查 |
| `scripts/generate-sitemap.py` | 自動生成 sitemap.xml |
| `~/.openclaw/workspace/AGENTS.md` | Agent 開發指引（含 SEO checklist） |
| `~/.openclaw/workspace/skills/esgov-seo/SKILL.md` | SEO 完整技能檔案 |
