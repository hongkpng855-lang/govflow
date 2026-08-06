# ESGov 功能模組分類索引 (Module Classification Index)

> **用途：** 每次改動前，先搵出改動屬於邊個模組，睇「涉及位置」一欄就知道要一齊改邊啲檔案。
> 呢份索引係 `MODULES.md` 嘅進階版 — 按**功能模組**分類，而唔係按改動類型。
> 由 130+ bugs 累積嘅 codebase 知識整理。

---

## 目錄

| 模組 ID | 模組名稱 | 涉及檔案數 |
|:-------:|----------|:----------:|
| M01 | 核心產品頁 | 6 |
| M02 | 流程資料 (processes.json) | 4+ |
| M03 | PDF 生成器 | 19 |
| M04 | 首頁 | 1 |
| M05 | Blog | 98 |
| M06 | 導航 / Footer | 全站 |
| M07 | Icons / Lucide | 全站 |
| M08 | Schema / JSON-LD | 全站 |
| M09 | Meta / SEO | 全站 |
| M10 | Sitemap / URL | 1 + 全站 |
| M11 | Google / GSC | 3 |
| M12 | Cloudflare | 1 |
| M13 | Scripts / 工具 | ~10 |
| M14 | Cron Jobs | 2 |
| M15 | 文件 (Docs) | 3 |

---

## M01 — 核心產品頁 (Product Pages)

**功能：** 6 個公司秘書流程指南頁，每個有 step-by-step 流程 + 文件卡 + 互動工具連結

| 檔案 | 說明 |
|------|------|
| `shareholder-transfer/index.html` | 股份轉讓（processes.json 資料源） |
| `company-name-change/index.html` | 公司改名（embedded 資料） |
| `significant-controllers-register/index.html` | SCR（processes.json 資料源） |
| `deregistration/index.html` | 撤銷註冊（embedded 資料） |
| `director-particulars-change/index.html` | 董事詳情變更（embedded 資料） |
| `share-transfer/index.html` | 股份轉讓舊版（embedded 資料） |

**每個頁包含：**
- Head：title / meta / og / twitter / canonical / JSON-LD（Article + FAQPage + HowTo + Breadcrumb + Organization）
- Nav bar + logo
- TL;DR 概覽 + 費用/需時/法律 stat boxes
- Step nav sidebar（`STEP_ICONS` global + x-html）
- Step content（processes.json 或 embedded x-data）
- Document cards（互動工具 / 檢視範例）
- 其他免費指南 cross-links（4 條產品 links）
- 相關指南 blog links
- FAQ accordion + 相關指南 + footer

**涉及模組：** M02（資料）、M06（導航）、M07（icons）、M08（schema）、M09（meta）、M10（links）

**⚠️ 陷阱：**
- embedded 頁（company-name-change, deregistration, director, share-transfer）step details 喺 x-data 入面 — **唔可以加 HTML icons**（會炒頁面）
- `openDoc(doc)` 好容易俾 patch tool 錯改成 `get steps()`（見 AGENT-HANDOFF §6）
- x-data brace balance 一定要 check（`{` vs `}` diff = 1）

---

## M02 — 流程資料 (processes.json)

**功能：** 步驟資料來源（shareholder-transfer + SCR 用），Alpine.js fetch 載入

| 檔案 | 說明 |
|------|------|
| `processes.json` | Share transfer 步驟 |
| `processes-company-name-change.json` | 公司改名步驟 |
| `processes-share-transfer.json` | 股份轉讓步驟 |
| `scr-processes.json` | SCR 步驟 |

**每份包含：** steps[]（stepNumber, title, details, documents[]）、totalSteps、finalDonate

**涉及模組：** M01（渲染）、M07（icons）、M08（schema 一致性）

**⚠️ 陷阱：**
- details 用 `<i data-lucide='icon'>` 單引號（JSON `"` delimiter）
- HTML 改動要 `x-text` → `x-html` 先 render 到
- 改完要 purge cache（Alpine fetch 有 cache）

---

## M03 — PDF 生成器 (Generators)

**功能：** 19 個免費 PDF 生成工具頁

| 類別 | 檔案 |
|------|------|
| 股份轉讓 | `sold-note-generator/`, `instrument-transfer-generator/`, `letter-of-transferee-generator/`, `nar1-generator/`, `nsc1-generator/` |
| 公司改名 | `company-name-change-generator/special-resolution/`, `company-name-change-generator/nnc2/` |
| 撤銷註冊 | `deregistration-checklist-generator/`, `deregistration-ir1263-generator/`, `deregistration-irc3113-generator/`, `deregistration-ndr1-generator/` |
| SCR | `scr-generator/`, `scr-data-collection-generator/`, `scr-identification-checklist-generator/`, `scr-notice-generator/`, `scr-nr2-generator/`, `scr-shareholder-analysis-generator/`, `scr-designated-rep-generator/` |
| 其他 | `audit-report-generator/` |

**涉及模組：** M07（icons）、M09（meta）、M10（sitemap/links）

**⚠️ 陷阱：** 全部已加 Lucide CDN + static icons（2026-07-29）

---

## M04 — 首頁 (Homepage)

**檔案：** `index.html`

**包含：** 全部 meta/schema、nav、trust signals、hero、how-it-works、6 產品卡、blog 區、footer

**涉及模組：** M01（產品卡）、M06（nav）、M07（icons）、M08（schema）、M09（meta）、M10（links）

**⚠️ 陷阱：**
- 產品卡有 id="products" anchor
- hero 用 `#products` CTA
- **用戶唔想要大改 UI** — 只可以隱形改動（meta/schema/links）

---

## M05 — Blog

**檔案：** `blog/*/index.html`（98 篇）

**功能：** SEO 流量主力（95%+ clicks），每篇有 Article schema + FAQ（部分）

**涉及模組：** M07（icons）、M08（schema）、M09（meta）、M10（links）

**⚠️ 陷阱：**
- Blog 唔用 ESGov prefix（keyword-leading 更好）
- Canonical 全部已改 trailing-slash（2026-08-04）
- 舊 `.html` URLs 由 Cloudflare 301 處理（唔好刪 redirect stubs，301 行先）
- 部分 blog 冇 lucide CDN（加 CTA 前要 check）

---

## M06 — 導航 / Footer

**功能：** 全站統一 nav + footer

| 位置 | 說明 |
|------|------|
| 每頁 `<nav>` | Logo + 品牌名 + 返回 |
| 每頁 footer | 版權年份、links |
| 產品頁「其他免費指南」 | 4 條產品 cross-links |
| 產品頁「相關指南」 | 3-4 條 blog links |

**涉及模組：** M01、M04、M10

**⚠️ 陷阱：** 改導航 = 全站 26+ 頁都要改（用 script 批量）

---

## M07 — Icons / Lucide

**功能：** emoji → Lucide SVG 替換

| 位置 | 方法 |
|------|------|
| Static HTML | `<i data-lucide="icon">` + CDN |
| Step NAV | `STEP_ICONS` global + x-html |
| Step content (processes.json) | `<i data-lucide='icon'>` 單引號 + x-html |
| Generator pages | static `<i data-lucide>` + CDN |

**涉及模組：** M01、M02、M03、M04、M05

**⚠️ 陷阱：** 完整流程見 `references/lucide-icon-replacement.md`（唔好喺 x-data 加 HTML、唔好用 scanner）

---

## M08 — Schema / JSON-LD

**功能：** 結構化資料（AEO）

| Schema 類型 | 位置 |
|-------------|------|
| Article | 全部頁（headline 要同 title 一致） |
| FAQPage | 產品頁 + 有 FAQ 嘅 blog |
| HowTo | 產品頁 + NDR1 + 董事秘書 blog（`estimatedCost` 要同費用一致） |
| Speakable | 首頁 |
| BreadcrumbList | 全部頁 |
| Organization / Person | 全部頁 |
| WebSite + SearchAction | 首頁 |

**涉及模組：** M01、M02、M04、M05、M09

**⚠️ 陷阱：** schema 同內文不一致 = Google downgrade rich snippet

---

## M09 — Meta / SEO

**功能：** title / description / og / twitter / canonical

| 位置 | 同步要求 |
|------|----------|
| `<title>` | 同 og:title 同步（SEO checker 扣分如果唔同步） |
| `<meta name="description">` | 100-160 chars；同 og:desc 同步 |
| `og:title` / `og:description` | 同上 |
| `twitter:title` / `twitter:description` | 如有 |
| `<link rel="canonical">` | 全部 trailing-slash（blog） |
| JSON-LD headline/description | 同 meta 同步 |

**涉及模組：** M01、M03、M04、M05、M08

---

## M10 — Sitemap / URL

**功能：** URL 結構 + 索引

| 檔案/位置 | 說明 |
|-----------|------|
| `sitemap.xml` | 由 script 生成，128 URLs（0 .html、0 test） |
| `scripts/generate-sitemap.py` | skip set: .git, scripts, templates, node_modules, assets, .agents, references, scr, test-share-transfer + blog .html stubs |
| `404.html` | .html URL JS redirect handler（fallback） |
| Cloudflare redirects | 18 條 .html → pretty 301（10 dynamic + 1 page rule wildcard） |
| Canonical tags | 95 個 blog → trailing-slash |

**涉及模組：** M01-M05（所有 URLs）

**⚠️ 陷阱：**
- 改 URL 一定要加 Cloudflare 301（舊→新）
- 改完 regenerate sitemap + resubmit GSC + purge cache
- 加新頁要入 sitemap

---

## M11 — Google / GSC

| 項目 | 位置 |
|------|------|
| Token | `~/.hermes/google_token.json` + profile copy |
| **Auto-refresh** | 每次 query 前 refresh_token（access token 1hr 過期） |
| Sitemap submit | PUT webmasters API |
| 每日報告 | Cron jobs（M14） |

**⚠️ 陷阱：** 唔好直接 query — 一定要先 refresh（見 AGENT-HANDOFF §8）

---

## M12 — Cloudflare

| 項目 | 值 |
|------|-----|
| Zone ID | `e36d8aa7f072c1ff42043511ed0750a6` |
| Account ID | `312d4e1b3786fdc7396c57a9b5afb2c5` |
| Credentials | `~/.hermes/profiles/esgov-builder/.env`（CLOUDFLARE_*） |
| SSL/TLS | Full (strict) |
| Redirect rules | 10 dynamic + 1 page rule |
| Cache | **每次 deploy 後要 purge** |

**⚠️ 陷阱：** 全部見 AGENT-HANDOFF §13（regex_replace 要 paid、URL encoding、10 rules 上限等）

---

## M13 — Scripts / 工具

| 檔案 | 用途 |
|------|------|
| `scripts/deep-seo-audit.py` | 21 頁 SEO audit（11 core + 10 top blogs） |
| `scripts/seo-checker.py` | 全站 checker |
| `scripts/generate-sitemap.py` | Sitemap 生成 |
| `scripts/fix-canonicals.py` | Canonical 修復 |
| `scripts/gen-html-redirects.py` | .html stub 生成 |
| `scripts/setup.py` | GSC token auth |

---

## M14 — Cron Jobs

| Job | Schedule | 內容 |
|-----|:--------:|------|
| `b547f4e1a94a` | 每日 09:00 | SEO/AEO/GEO/GSC 全面報告 |
| `eff43bf5bedf` | 每日 17:15 | 下午 GSC 更新 |

**⚠️ 陷阱：** 如果改 token 路徑 / sitemap URL，要 update cron prompt

---

## M15 — 文件 (Docs)

| 檔案 | 用途 |
|------|------|
| `AGENT-HANDOFF.md` | Agent 交接（bugs、recovery、Cloudflare） |
| `MODULES.md` | 改動影響分析（按改動類型） |
| `llms.txt` | GEO（AI crawlers 讀） |
| `robots.txt` | AI crawlers 全 Allow |

**⚠️ 陷阱：** 任何 codebase 大改動後要 update 呢啲 docs

---

## 點用呢份索引（配合 esgov-change-impact skill）

1. 收到改動要求 → 判斷屬於邊個模組（M01-M15）
2. 睇該模組「涉及模組」欄 → 一齊改
3. 睇「⚠️ 陷阱」→ 避開已知 bug
4. Deploy（commit + push + purge cache + verify）
5. 如有 codebase 結構改動 → update M15 docs
