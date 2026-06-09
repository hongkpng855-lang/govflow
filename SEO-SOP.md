# ESGov SEO SOP — Google 曝光操作指南

## 📋 每週／每月清單

### ✅ 每週（有新內容時）
- [ ] 行 `python3 scripts/seo-checker.py` 確認冇 error
- [ ] 新頁面 title + description 符合規範
- [ ] 提交新 URL 去 Google Search Console

### ✅ 每月
- [ ] 行 `python3 scripts/generate-sitemap.py` 更新 sitemap
- [ ] 提交 sitemap 去 Google Search Console
- [ ] Check「涵蓋範圍」有冇 error

---

## ⚙️ 工具

### SEO Checker
```bash
cd /mnt/c/Users/hongk/Desktop/esgov
python3 scripts/seo-checker.py
```
Check 每頁：title、description、H1、alt、OG tags、canonical

### Sitemap Generator
```bash
python3 scripts/generate-sitemap.py
```
自動 scan 所有 .html → 生成 sitemap.xml（54+ URLs）

---

## 📐 新頁面 Checklist
- [ ] `<title>ESGov | [50-60 chars]</title>`
- [ ] `<meta name="description" content="[120-160 chars]" />`
- [ ] `<link rel="canonical" href="https://esgov.org/..." />`
- [ ] Open Graph: og:title, og:description, og:url, og:image
- [ ] 只有一個 `<h1>`
- [ ] 所有 `<img>` 有 `alt`
- [ ] 自然含關鍵字喺內容

---

## 🔍 Google Search Console 使用
1. https://search.google.com/search-console
2. Property: `https://esgov.org`
3. Sitemap: `https://esgov.org/sitemap.xml`
4. 定期睇「成效」同「涵蓋範圍」
