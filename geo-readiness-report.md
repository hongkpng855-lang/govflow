# GEO Readiness Report — ESGov

> Date: 2026-06-24  
> Prepared by: ESGov SEO Agent  
> Profile: esgov-seo

---

## 一、GEO 狀態總覽

| Area | Status | Notes |
|:-----|:------:|:------|
| `robots.txt` AI crawler config | ✅ Done | GPTBot, ChatGPT-User, OAI-SearchBot, ClaudeBot, PerplexityBot all allowed |
| `llms.txt` | ✅ Done | 110-line curated summary, links to all core pages + generators |
| `llms-full.txt` | ✅ Done | Full site content dump for AI consumption (1939 lines) |
| Wikipedia backlink draft | ⏳ Submitted | Draft:Significant Controllers Register (Hong Kong) — **⚠️ external link `/scr-guide/` may be broken** |
| Person schema (author bylines) | ✅ ~50/87 blog posts | `@type: Person` confirmed on 50+ blog HTML files |
| FAQPage schema | ✅ 1 page | SCR guide has 6 Q&A entries |
| HowTo schema | ✅ 1 page | SCR guide has 7-step HowTo |
| Article schema | ⏳ Partial | Memory says 22/67 — actual may need audit |
| Question-format H3 headings | ❌ Not found | Context says "4 product pages" but no `<h3>` tags exist on product pages |
| Breadcrumb schema | ⏳ Partial | SCR page only — missing on blog posts & generators |
| Sitemap health | ✅ Fixed | 79 URLs, no `.agents/` included |
| SiteNavigationElement schema | ❌ Missing | No nav schema on any page |
| WebSite schema (SearchAction) | ❌ Missing | No site search action defined |
| Video sitemap | ❌ Missing | No video content indexed |

---

## 二、已完成 GEO 工作

### ✅ `robots.txt` — AI Crawlers 全面開放
- Allow list: GPTBot, ChatGPT-User, OAI-SearchBot, ClaudeBot, Claude-Web, PerplexityBot, anthropic-ai
- Block list: CCBot, Bytespider, cohere-ai, FacebookBot (training crawlers)
- Sitemap linked ✅

### ✅ `llms.txt` + `llms-full.txt`
- `llms.txt` 跟足 [llmstxt.org](https://llmstxt.org) 格式
- Contains: About, Core Products, All PDF Generators, 80+ blog posts, Key Facts
- `llms-full.txt` has full page content for deep AI understanding

### ✅ Wikipedia Draft — High-value GEO Play
- Draft ready: **Significant Controllers Register (Hong Kong)**
- External link includes: `https://esgov.org/scr-guide/`
- **⚠️ Issue: No `/scr-guide/` route exists** — actual page is `/significant-controllers-register/`
- Once published → top citation source for AI search engines

### ✅ Person Schema (EEAT)
- 50+ blog posts have `"@type": "Person"` schema markup
- Author byline structure confirmed across majority of posts

---

## 三、Next Steps — Priority Order

### 🔴 P1: Fix Wikipedia External Link
**Issue:** Draft references `https://esgov.org/scr-guide/` but that path doesn't exist.  
**Fix:** Either:
- (a) Change draft link to `https://esgov.org/significant-controllers-register/`, OR  
- (b) Add a redirect from `/scr-guide/` → `/significant-controllers-register/` and add `<link rel="canonical">`  
**Impact:** Without this, the GEO value of the Wikipedia backlink is zero.

### 🔴 P1: Add Question-Format H3 Headings to Product Pages
**Target pages (4):**
1. `/shareholder-transfer/` — 股份轉讓指南
2. `/company-name-change/` — 公司改名指南
3. `/significant-controllers-register/` — SCR 指南
4. `/deregistration/` — 公司撤銷註冊

**Format:** Each H3 should be a natural question in Cantonese  
**Why:** AI Overviews (Google SGE, ChatGPT) heavily weight question-format subheadings for featured snippets  
**Example:** "股份轉讓要幾耐？" → `<h3>股份轉讓要幾耐？</h3>`  
**GEO Impact:** High — directly influences AI snippet extraction

### 🟡 P2: Expand Article Schema to All Blog Posts
**Current:** ~22/87 blog posts have Article schema (per memory)  
**Action:** Run `python3 scripts/add-blog-schema.py` on remaining ~65 posts  
**Why:** Article schema is a core signal for AI search engines categorizing content  
**GEO Impact:** Medium-High — improves AI content classification

### 🟡 P2: Add Breadcrumb Schema to All Blog Posts & Generators
**Current:** Only SCR guide page has breadcrumb  
**Action:** Run `python3 scripts/add-breadcrumbs.py` on all generator pages and blog posts  
**GEO Impact:** Medium — AI crawlers use breadcrumbs for site structure understanding

### 🟡 P2: Add SiteNavigationElement Schema
**Action:** Add JSON-LD SiteNavigationElement to `index.html` and all product pages  
**Why:** Helps AI crawlers understand site architecture  
**GEO Impact:** Medium

### 🟢 P3: Add WebSite Schema with SearchAction
**Action:** Add to `index.html`:
```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "url": "https://esgov.org",
  "potentialAction": {
    "@type": "SearchAction",
    "target": "https://esgov.org/?s={search_term_string}",
    "query-input": "required name=search_term_string"
  }
}
```
**GEO Impact:** Low-Medium

### 🟢 P3: Add Google Business Profile / Entity
**Action:** Create/claim GBP for ESGov  
**Why:** Knowledge Panel → cited by AI Overviews  
**GEO Impact:** Medium (longer setup)

### 🟢 P3: Quora / Reddit Answers with esgov.org Links
**Action:** Use existing `quora-answer-draft.md` as template  
**Why:** Quora/Reddit are frequently cited by AI search engines  
**GEO Impact:** Medium (needs consistent effort)

---

## 四、GEO Pipeline Summary

```
Current Score: 65/100
├── AI Discoverability (robots.txt/llms.txt) ████████░░ 80%
├── Structured Data (Schema.org)              ██████░░░░ 60%
├── Wikipedia / External Authority            ████░░░░░░ 40% (blocked by broken link)
├── Q&A / Forum Presence                      ██░░░░░░░░ 20%
├── Social Proof / Google Entity              █░░░░░░░░░ 10%
└── Video / Multimedia                        ░░░░░░░░░░  0%

Next Sprint Top 3:
1. Fix Wikipedia draft external link → submit ✅
2. Add question-format H3s to 4 product pages
3. Run Article schema script on remaining blog posts
```

---

## 五、ESGov-SEO Profile 現狀

- Profile loaded at `~/.hermes/profiles/esgov-seo/` ✅
- Profile soul.md (職責: 淨係做 SEO, 唔改 product content/generator code) ✅
- Profile memory.md (記錄歷史 SEO work) ✅
- User communication偏好: 廣東話/英 terms mixed ✅
- **⚠️ 無「esgov-geo」skill** — GEO pipeline needs formal skill definition
- Scripts available: `seo-checker.py`, `deep-seo-audit.py`, `generate-sitemap.py`, `add-blog-schema.py`, `add-breadcrumbs.py`
