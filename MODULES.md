# ESGov 改動影響分析 (Change Impact Analysis)

> **核心原則：** 每次改動之前，先查呢張表。ESGov 係 static HTML + JSON + schema 多層結構 —
> 改一個地方，通常要**一齊改 3-5 個地方**，否則會出現內容唔一致（例如日期唔同步、費用唔一致、URL 404）。

---

## 1. 時間 / 日期改動（例如「最後更新：2026年X月」）

**典型觸發：** 用戶話「更新個日期」「freshness 改月份」

| # | 位置 | 檔案 |
|:-:|------|------|
| 1 | 首頁 freshness | `index.html`（最後更新 footer + meta） |
| 2 | 產品頁 freshness（6 個） | `shareholder-transfer/`, `company-name-change/`, `significant-controllers-register/`, `deregistration/`, `director-particulars-change/`, `share-transfer/` 各 `index.html` |
| 3 | JSON-LD `datePublished` / `dateModified` | 每個頁面 head 嘅 Article schema |
| 4 | 相關 blog posts 最後更新 | `blog/*/index.html`（視乎內容） |
| 5 | sitemap `lastmod` | 由 `scripts/generate-sitemap.py` 重新生成 |

**驗證：** `grep -c "2026年X月" *.html */index.html`

---

## 2. 費用改動（政府費用、收費、罰款）

**典型觸發：** 用戶話「NDR1 加價」「費用改 HK$XXX」

| # | 位置 | 檔案 |
|:-:|------|------|
| 1 | 產品頁內文費用 | 相關產品 `index.html`（費用比較 box / step content） |
| 2 | processes.json 費用 | `processes.json`, `processes-*.json`（step details 提到費用） |
| 3 | Blog posts 費用段落 | `blog/*/index.html` |
| 4 | FAQPage schema 費用答案 | 相關頁面 JSON-LD |
| 5 | HowTo schema `estimatedCost` | 相關頁面 JSON-LD |
| 6 | llms.txt 描述（如提到費用） | `llms.txt` |
| 7 | Meta description（如提到費用） | 相關頁面 meta tag |

---

## 3. URL / 路徑改動（產品路徑、blog 路徑、anchor）

**典型觸發：** 用戶話「改個 URL」「搬 page」「加個新頁」

| # | 位置 | 檔案 |
|:-:|------|------|
| 1 | 首頁產品卡 links | `index.html` |
| 2 | 其他產品頁 cross-links（「其他免費指南」section） | 全部產品 `index.html` |
| 3 | Blog 內部 links（相關指南 section） | 產品頁 + blog posts |
| 4 | **Sitemap regenerate + resubmit** | `scripts/generate-sitemap.py` → `sitemap.xml` → GSC PUT |
| 5 | llms.txt | `llms.txt` |
| 6 | **Cloudflare redirect rules**（舊 URL → 新 URL） | Cloudflare API（見 AGENT-HANDOFF §13） |
| 7 | Canonical tags | 受影響頁面 `<link rel="canonical">` |
| 8 | 404.html redirect handler | `404.html`（如適用） |

**⚠️ 改 URL 一定要加 Cloudflare 301**（舊 → 新），否則舊 links 全斷。

---

## 4. 標題 / 品牌改動

**典型觸發：** 用戶話「改 title」「改品牌名」

| # | 位置 | 檔案 |
|:-:|------|------|
| 1 | `<title>` | 頁面 head |
| 2 | `og:title` | 同上（要同步） |
| 3 | `twitter:title`（如有） | 同上 |
| 4 | JSON-LD `headline` / `name` | 同上 |
| 5 | llms.txt 標題 | `llms.txt` |
| 6 | Logo / favicon 路徑 | `<link rel="icon">` |

**⚠️ `<title>` 同 `og:title` 唔同步 = SEO checker 扣分（og_title dimension）。**

---

## 5. Meta Description 改動

**典型觸發：** 用戶話「改 description」「CTR 優化」

| # | 位置 | 檔案 |
|:-:|------|------|
| 1 | `<meta name="description">` | 頁面 head |
| 2 | `og:description` | 同上（要同步） |
| 3 | `twitter:description`（如有） | 同上 |
| 4 | JSON-LD `description` | 同上（Article/HowTo schema） |

---

## 6. Schema 改動（FAQ / HowTo / Article / Speakable）

**典型觸發：** 用戶話「加 FAQ」「加 HowTo schema」

| # | 位置 | 檔案 |
|:-:|------|------|
| 1 | 目標頁面 JSON-LD block | 頁面 head |
| 2 | 內文內容 | 內容要同 schema 一致（Google 會對比） |
| 3 | 驗證 | rich result test / `grep -c "FAQPage"` |

**⚠️ Schema 同內文唔一致 = Google 可能 downgrade rich snippet。**

---

## 7. Icon / Emoji 改動

見 `references/lucide-icon-replacement.md`（完整流程 + 陷阱）。

| # | 位置 | 檔案 |
|:-:|------|------|
| 1 | Static icons | 頁面 HTML |
| 2 | Step NAV icons | `STEP_ICONS` global + x-html |
| 3 | Step content icons | `processes.json`（唔可以喺 embedded x-data 加 HTML） |

---

## 8. 任何內容改動後 — 必須 Deploy 流程

| # | Step | Command |
|:-:|------|---------|
| 1 | Git commit + push | `git add -A && git commit -m "..." && git push origin main` |
| 2 | **Cloudflare purge cache** | `curl -s -X POST "https://api.cloudflare.com/client/v4/zones/e36d8aa7f072c1ff42043511ed0750a6/purge_cache" -H "X-Auth-Email: tbstbs0613@gmail.com" -H "X-Auth-Key: $CLOUDFLARE_API_KEY" -H "Content-Type: application/json" -d '{"purge_everything":true}'` |
| 3 | Verify live | `curl -s https://esgov.org/page/ | grep -c 'marker'` |
| 4 | Verify rendered（JS 改動） | Playwright page.evaluate |

**⚠️ Proxied 之後 cache 可以 hold 1hr+ — 每次 deploy 都要 purge！**

---

## 9. 全站快速檢查命令

```bash
# 檢查某字串出現喺邊啲檔案（改動影響分析第一步）
grep -rln "要改嘅字串" /mnt/c/Users/hongk/Desktop/esgov/ --include='*.html' --include='*.json' --include='*.txt' | grep -v '.git\|test-share-transfer'

# 檢查日期同步
grep -rn "最後更新：2026年" */index.html index.html | wc -l

# 檢查費用同步
grep -rn "HK\$420\|HK\$270" *.html */index.html blog/*/index.html 2>/dev/null | wc -l

# SEO audit
cd /mnt/c/Users/hongk/Desktop/esgov && python3 scripts/deep-seo-audit.py

# Sitemap regenerate
python3 scripts/generate-sitemap.py
```

---

## 10. 改動影響分析工作流（每次改動前）

1. **收到改動要求** → 判斷屬於邊個類型（§1-§7）
2. **`grep -rln` 搵晒所有受影響檔案**
3. **列出行動清單**（改邊啲檔案、改咩）
4. **一齊改**（同一批次，唔好分開）
5. **Deploy**（§8：commit + push + purge + verify）
6. **報告**：「改咗 N 個位置，全部同步」
