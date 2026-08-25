# 📋 esgov.org 主站 Blog 發文流程（完整版）

> 來源：另一部電腦嘅 agent handoff（2026-08）— 參考用
> 用途：接手 agent 發 blog 時跟呢份流程

## 基本資料

- **網站**：https://esgov.org（Blog 喺 `/blog/`）
- **Source**：`/mnt/c/Users/hongk/Desktop/esgov/`，Repo `hongkpng855-lang/govflow`
- **技術**：純 HTML + Tailwind CDN + Alpine.js，冇 build step
- **Hosting**：GitHub Pages + Cloudflare Proxied（Full strict SSL）
- **文章格式**：`blog/{中文名}/index.html`，全部「終極指南」格式（500-600 行）
- **定位**：香港老闆公司秘書文件指南，口語廣東話、真實經歷者角度
- **商業模式**：免費文章引流 → HK$149 付費指南 → generator 工具

---

## 一、發文 Pipeline（blog-seo-pipeline-sop.md）

**SEO（揀題+Brief）→ Researcher（官方來源+案例）→ Writer（寫文）→ SEO（Review+Deploy）**

1. **SEO 揀題**：web_search 確認 keyword 搜尋量/競爭；優先高搜尋低競爭 + product-related keywords；開 brief file `blog/_briefs/{slug}-brief.md`
2. **Researcher**：gov.hk / cr.gov.hk / ird.gov.hk 官方來源（合規內容必須有官方根據）+ lihkg 痛點 + 競品分析
3. **Writer**：口語廣東話「你」「我」朋友教路 + 真實犯錯故事；自然融入 keyword；結尾 CTA 去產品頁
4. **SEO Review + Deploy**：見下面 checklist → 更新 `blog/index.html`（新 card 置頂）+ 主頁 blog section + sitemap → seo-checker 0 issues → `./deploy.sh "msg"` → purge Cloudflare cache

---

## 二、SEO 處理（每篇必做）

- Title `ESGov | ` 50-60 chars 含 keyword
- Description 120-160 chars 含 keyword + CTA
- Canonical 要 trailing slash（`https://esgov.org/.../`）
- OG tags 齊（og:title/description/url/image）
- 只有一個 H1 含 keyword；所有 img 有 alt
- Internal links 最少 2 個（product page / generator）
- Article + Breadcrumb + FAQPage schema
- 每週行 seo-checker.py + 提交新 URL 去 GSC；每月 regenerate sitemap

---

## 三、AEO 處理（AI 答問引擎引用）

目標：令 AI（ChatGPT/Perplexity/AI Overviews）喺答案引用你。報告：`aeo-research-report.md`

- **Phase 1 Quick Wins**：
  - 產品頁 step headings 改問題式：`Step 1: 準備文件` → `股份轉讓要準備咩文件？`（2.8x citation lift）
  - SCR guide FAQ 6 → 15-20 條；印花稅 guide 加 FAQPage schema
  - 修正 Wikipedia draft 錯 link（`/scr-guide/` → `/significant-controllers-register/`）
- **Phase 2**：每個 section 開頭加 Answer-First Opening（40-60 字 direct answer，例如「股份轉讓喺香港需要 5 個步驟，約 1-2 星期完成…」）；其餘 3 個產品頁加 HowTo schema；高價值 blog（查冊/印花稅/MPF）加 QAPage schema
- **Phase 3**：Article schema 擴展到全部 87 篇；加 SiteNavigationElement + WebSite SearchAction schema

---

## 四、GEO 處理（生成式 AI 引用）

報告：`geo-readiness-report.md`。已完成：

- robots.txt：AI crawlers 全部 Allow（GPTBot/ClaudeBot/PerplexityBot 等），training crawlers Block（CCBot/Bytespider/FacebookBot）
- llms.txt（110 行 curated）+ llms-full.txt（1939 行全站 dump）
- Person schema（EEAT）~50/87 篇
- Wikipedia draft 已提交（要修 link）

未做：H3 問題式、Breadcrumb 全站覆蓋、SiteNavigationElement、WebSite SearchAction

---

## 五、Deploy（⚠️ 最重要陷阱）

- `./deploy.sh "msg"`（有 safety check，新 HTML page 未批准會 abort）
- **Cloudflare Proxied cache hold 舊內容 up to 1 小時+** → deploy 後必須即刻 purge cache（API call 用 zone `e36d8aa7f072c1ff42043511ed0750a6`，key 喺 `~/.hermes/profiles/esgov-builder/.env`）
- **驗證順序**：① GitHub raw ② live curl ③ 先至用 browser（browser tool 自己 cache 會 stale，唔好淨靠佢）
- GSC token：`~/.hermes/google_token.json`，每小時過期，query 前 auto-refresh