# AEO（Answer Engine Optimization）研究報告 — ESGov 應用方案

> **日期：** 2026-06-24  
> **對象：** ESGov（esgov.org）— 香港公司秘書及合規顧問服務  
> **準備：** ESGov SEO 團隊  
> **版本：** v1.0

---

## 目錄

1. [咩係 AEO？核心概念與定義](#1-咩係-aeo核心概念與定義)
2. [AEO vs GEO vs SEO — 詳細比較](#2-aeo-vs-geo-vs-seo--詳細比較)
3. [主流 Answer Engine 一覽](#3-主流-answer-engine-一覽)
4. [AEO 最佳實踐](#4-aeo-最佳實踐)
5. [Answer Engine 點樣揀選內容？](#5-answer-engine-點樣揀選內容)
6. [AEO 對 esgov.org 嘅可行性分析](#6-aeo-對-esgovorg-嘅可行性分析)
7. [具體行動計劃](#7-具體行動計劃)
8. [Quick Wins vs 長期策略](#8-quick-wins-vs-長期策略)
9. [測量 AEO 成效](#9-測量-aeo-成效)
10. [附錄：參考資源](#10-附錄參考資源)

---

## 1. 咩係 AEO？核心概念與定義

### 1.1 AEO 定義

**Answer Engine Optimization（AEO）** 係優化網站內容令 AI 驅動嘅 Answer Engine（例如 ChatGPT Search、Perplexity、Google AI Overviews、Claude、Gemini、Bing Copilot）喺回答問題嗰陣，引用你嘅網站作為來源嘅策略。

> 傳統 SEO 目標係「令人 clicked 入你個網站」；  
> AEO 目標係「令 AI 喺佢嘅答案入面引用你」——就算個 user 從來唔 clicked 入去。

### 1.2 核心轉變：從「Click-Based」到「Citation-Based」

| 傳統搜尋 | AI 搜尋 |
|:---------|:---------|
| User 搜尋 → 見到 10 條 link → Click 入去 | User 問問題 → AI 直接俾答案 → 可能永遠唔 Click |
| 成功指標：Traffic、Rankings、CTR | 成功指標：Citations、Mentions、Share of Voice |
| 你同 Google 競争 keyword rankings | 你同其他網站競争被 AI 引用嘅機會 |

### 1.3 關鍵數據點

| 指標 | 數據 | 來源 |
|:-----|:-----|:-----|
| ChatGPT 每月活躍用戶 | 8.83 億 | Frase.io |
| ChatGPT 每日查詢量 | 20 億 | Frase.io |
| Perplexity 每月查詢量 | 5 億+ | DOJO AI |
| AI 搜尋轉換率 vs 傳統 SEO | **4.4x 更高** | Semrush |
| AI 搜尋 sessions 冇 click 率 | **93%** | Frase.io |
| Google 零點擊搜尋率 | **58.5%**（US） | SparkToro |
| AI Overviews 出現時 Position 1 CTR 跌幅 | **-58%** | Ahrefs |
| Gartner 預測傳統搜尋流量跌幅（by 2026） | **-25%** | Gartner |
| AI-referred sessions YoY 增長 | **+527%** | Frase.io |
| 順序 H2>H3>H4 標題結構帶嚟嘅 citation lift | **2.8x** | AirOps |

---

## 2. AEO vs GEO vs SEO — 詳細比較

### 2.1 三者定位

```
SEO ──→ 傳統搜尋引擎（Google, Bing）—— Ranking + Traffic
GEO ──→ 生成式引擎（LLM 訓練/輸出）—— 塑造 AI 語言用詞
AEO ──→ 答案引擎（ChatGPT, Perplexity, AI Overviews）—— 被引用做來源
```

### 2.2 詳細對比表

| 維度 | 傳統 SEO | GEO（Generative Engine Optimization） | AEO（Answer Engine Optimization） |
|:-----|:---------|:--------------------------------------|:----------------------------------|
| **目標** | 提高排名 → 吸引 Clicks | 塑造 AI 生成內容嘅語言同 framing | 被 AI 答案引用做來源 |
| **成功指標** | Rankings, Traffic, CTR, Backlinks | AI 模型輸出嘅語言偏好 | Citation 次數、Brand Mentions |
| **優化單位** | Page-level（Title, H1, Content） | Entity-level + Corpus-level（整體網站） | Fact-level（定義、統計、步驟） |
| **Content 結構** | 長篇 comprehensive coverage | 統計數據、獨特見解、說服性 framing | 直接答案 first、modular chunks |
| **Keyword 策略** | Search volume, Keyword difficulty | Entity 密度、語義相關性 | Question patterns、Conversational queries |
| **Tech 重點** | Crawlability, Speed, Meta Tags | Semantic HTML, Topical Authority Signals | Schema.org（FAQPage/HowTo/QAPage） |
| **User 互動** | Click-through to website | 無直接互動（AI 訓練用） | Zero-click citation |
| **Freshness** | 定期更新 | 持續更新 | 強烈偏好近期內容（商用 83% <12 個月） |

### 2.3 AEO 同 SEO 嘅互補關係

**重點：AEO 唔係取代 SEO，係延伸。**

- 38% 嘅 AI Overviews citation 嚟自 Google top 10 排名頁面（雖然呢個比例由 76% 跌到 38%）
- 即係話：好嘅 SEO 基礎仍然係 AEO 嘅 prerequisite
- 但 AEO 多咗一層：你嘅 content 必須要 **結構化到 AI 可以直接抽取答案**

---

## 3. 主流 Answer Engine 一覽

### 3.1 Google AI Overviews（前稱 SGE）

| 特性 | 詳情 |
|:-----|:------|
| **運作方式** | 喺 Google SERP 頂部顯示 AI 生成摘要，附來源連結 |
| **覆蓋率** | ~47% US searches（2026） |
| **零點擊率** | 83%（當 AIO 出現時） |
| **引用偏好** | 偏好多來源綜合，偏好共識性內容 |
| **Freshness** | 引用嘅 URLs 平均比傳統結果 **年輕 25.7%** |
| **格式偏好** | 段落摘要、Bullet points、Tables |
| **對 ESGov 重要性** | ⭐⭐⭐⭐⭐ 最高 — HK 公司秘書查詢好多係 informational |

### 3.2 ChatGPT Search

| 特性 | 詳情 |
|:-----|:------|
| **運作方式** | 對話式介面，可以追問、clarify |
| **用戶基礎** | 8.83 億 monthly active users |
| **引用偏好** | 偏好 comprehensive 內容，需要上下文 context |
| **內容風格** | Conversational 但要有深度，唔好只係表面 answer |
| **對 ESGov 重要性** | ⭐⭐⭐⭐⭐ — 最多人用嘅 AI search platform |

### 3.3 Perplexity

| 特性 | 詳情 |
|:-----|:------|
| **運作方式** | 透明引用每個答案嘅來源，inline citations |
| **引用偏好** | 偏好多來源、權威性內容、即時資訊 |
| **獨特點** | 最 transparency 嘅 citation 平台 — 每個答案有 numbered inline citations |
| **Reddit/Forum** | 46.7% top citations 嚟自 Reddit |
| **對 ESGov 重要性** | ⭐⭐⭐⭐ — 好適合 step-by-step guides 同 definitions |

### 3.4 Claude（Anthropic）

| 特性 | 詳情 |
|:-----|:------|
| **運作方式** | 對話式，重視詳細分析同 nuance |
| **引用偏好** | 偏好深度、多角度分析嘅內容 |
| **Bullet Points** | 比 Google 多 30% 機會引用 bullet-pointed pages |
| **對 ESGov 重要性** | ⭐⭐⭐ — Developer 社群多，general public 使用率較低 |

### 3.5 Google Gemini（前稱 Bard）

| 特性 | 詳情 |
|:-----|:------|
| **運作方式** | Google 生態系統整合，同 Google Search 深度連結 |
| **引用偏好** | 同 AI Overviews 類似，偏好多來源綜合 |
| **對 ESGov 重要性** | ⭐⭐⭐⭐ — 同 Google 深度整合，使用率持續增長 |

### 3.6 Microsoft Bing Copilot

| 特性 | 詳情 |
|:-----|:------|
| **運作方式** | Bing search + GPT-4 整合 |
| **引用偏好** | 偏向引用 Bing index 入面嘅內容 |
| **對 ESGov 重要性** | ⭐⭐⭐ — Desktop search 有一定佔有率 |

### 3.7 各 Answer Engine 引用偏好總表

| Platform | 內容偏好 | Schema 重視度 | Freshness 重視度 | 權威性重視度 |
|:---------|:---------|:--------------|:-----------------|:-------------|
| **Google AI Overviews** | 綜合多來源、列出式 | 高 | 高 | 高 |
| **ChatGPT Search** | Comprehensive + Context | 中高 | 中 | 高（E-E-A-T） |
| **Perplexity** | 事實性、即時資訊 | 中 | 非常高 | 非常高 |
| **Claude** | 深度分析、多角度 | 中 | 中 | 高 |
| **Gemini** | 同 Google AIO 近似 | 高 | 高 | 高 |
| **Bing Copilot** | 結構化內容 | 中 | 中 | 中 |

---

## 4. AEO 最佳實踐

### 4.1 Answer-First Content Structure（答案優先內容結構）

**呢個係 AEO 最重要嘅單一原則。**

每個 Section 應該：

1. **先俾直接答案**（40-60 字內，獨立完整段落）
2. **然後提供證明**（數據、例子、tradeoffs）
3. **最後引入下一個 logical question**

```
✅ 好嘅寫法：
「股份轉讓需要 1-2 星期完成，視乎文件齊全程度。
關鍵步驟包括：(1) 簽署股份轉讓文件 (2) 打釐印（交印花稅）
(3) 更新股東名冊 (4) 提交 NAR1 周年申報表。」

❌ 差嘅寫法：
「喺香港，有限公司股份轉讓係一個需要經過多個政府部門
同埋文件處理流程嘅過程⋯⋯」（冗長引言，冇 direct answer）
```

### 4.2 Semantic Chunking（語義分塊）

每個 Section 必須係 self-contained 嘅獨立單元：

- 每個 H2/H3 heading 用 **自然問題形式**（「股份轉讓要幾耐？」）
- 每段 200-400 字，有 clear boundaries
- 用 Bullet points、Numbered lists、Tables
- **Direct answer 放最前**

### 4.3 Schema Markup 策略

| Schema Type | 對 AEO 影響 | 應用建議 |
|:------------|:-----------|:---------|
| **FAQPage** | ⭐⭐⭐⭐⭐ 最高 | 每個產品頁/指南頁加 FAQ section |
| **HowTo** | ⭐⭐⭐⭐⭐ 最高 | 每個 step-by-step 指南用 HowTo schema |
| **QAPage** | ⭐⭐⭐⭐ 高 | Blog Q&A 格式內容用 QAPage |
| **Article** | ⭐⭐⭐⭐ 高 | 所有 blog posts 要有 Article schema |
| **BreadcrumbList** | ⭐⭐⭐ 中 | 全站 breadcrumb navigation |
| **Organization** | ⭐⭐⭐ 中 | 公司資料 schema |
| **Person** | ⭐⭐⭐⭐ 高 | Author byline + credentials |
| **Speakable** | ⭐⭐ 中低 | Voice search 優化用 |
| **WebSite (SearchAction)** | ⭐⭐ 中低 | Site search 功能 |

**Schema 黃金法則：**
> 只用來標記 **頁面上實際可見** 嘅內容。  
> 永遠唔好標記 hidden 或 implied 內容 — AI 會 detect 到不一致並降低信任。

### 4.4 Featured Snippet / Position Zero 策略

雖然 Google AI Overviews 開始取代部分 featured snippets，但 featured snippets 仍然係 AEO 嘅重要「練習場」：

1. **Identify snippet opportunities**：Search Console 入面 high impressions + low CTR = snippet 機會
2. **Define concept clearly**：冇 hedging，直接定義
3. **40-60 word direct answer**：每個 H2 開頭放
4. **List/Table/Paragraph format**：根據 query type 選擇
5. **同時優化 voice search**：Speakable schema + conversational language

### 4.5 Conversational Content Optimisation

Answer Engine 用 natural language processing（NLP），所以 content 要：

- **用 complete questions 做 headings**（唔好剩係 keyword：「股份轉讓」→「股份轉讓要點做？」）
- **用 conversational long-tail queries**（「點樣自己搞股份轉讓唔使俾會計公司錢」）
- **Answer follow-up questions**（FAQ 要覆蓋相關嘅追問）
- **Write as you speak**（廣東話書面語 mixed with English terms 對 ESGov 好 natural）

### 4.6 E-E-A-T Signals（Experience, Expertise, Authoritativeness, Trustworthiness）

AI 引擎極度重視 E-E-A-T：

| Signal | ESGov 現狀 | 建議加強 |
|:-------|:-----------|:---------|
| **Experience** | 已有「真實經歷者整理」| 增加具體案例、數字、時間線 |
| **Expertise** | Author bylines ✅ | 增加 credentials、linked profiles |
| **Authoritativeness** | llms.txt, Wikipedia draft | 更多 external citations、backlinks |
| **Trustworthiness** | Disclaimer, accurate content | Schema markup 一致性、更新日期 |

### 4.7 Freshness（新鮮度）

- **商用內容：** 83% AI citations 嚟自 <12 個月嘅 pages
- **高意圖查詢：** 60%+ citations 嚟自最近 6 個月內更新過嘅 pages
- **每季冇更新 = 3x 更可能失去 citations**

### 4.8 Topical Authority（主題權威性）

Answer Engines 唔係淨係睇一條問題嘅答案 — 佢哋會睇你成個網站對某個主題嘅整體 coverage：

- 每個 major topic 要有一條 comprehensive primary guide
- 加上 supporting pages（comparisons, edge cases, FAQs）
- 用 descriptive internal links 連接佢哋
- Question tree model：每個 major question → related sub-questions

---

## 5. Answer Engine 點樣揀選內容？

了解呢個機制對優化好重要：

### RAG Pipeline（Retrieval-Augmented Generation）

```
User Query → Query Interpretation（唔係 keywords，係 entities）
    → Retrieval（semantically relevant documents）
        → Ranking & Selection（relevance + authority + freshness）
            → Answer Generation（extract + synthesise）
                → Citation（clear, citable facts 優先）
```

### Ranking Factors（非 official，基於研究推斷）

| Factor | 相對重要性 | 點樣優化 |
|:-------|:----------|:---------|
| **Content-Relevance Match** | ⭐⭐⭐⭐⭐ | Answer-first structure, question headings |
| **Structured Data** | ⭐⭐⭐⭐ | FAQPage, HowTo, Article schema |
| **Freshness** | ⭐⭐⭐⭐ | Regular updates, publish dates visible |
| **Credibility Signals** | ⭐⭐⭐⭐ | Author bylines, citations, E-E-A-T |
| **Topical Authority** | ⭐⭐⭐⭐ | Topic clusters, internal linking |
| **Page Authority** | ⭐⭐⭐ | Backlinks, domain trust |
| **Content Format** | ⭐⭐⭐ | Lists, tables, clear headings |
| **Brand Mentions** | ⭐⭐⭐ | Wikipedia, forums, third-party sites |

**關鍵 insight：** 只有 **38%** AI Overview citations 嚟自 Google top 10 ranking pages（由 76% 跌到 38%）。即係話：**就算你唔係 Google 排名第一，你仍然有機會被 AI 引用** — 條件係你嘅 content structure 同 schema 做得更好。

---

## 6. AEO 對 esgov.org 嘅可行性分析

### 6.1 ESGov 現有 AEO 基礎評估

| Area | 現狀 | AEO 評分 |
|:-----|:-----|:---------|
| **llms.txt / llms-full.txt** | ✅ 已完成 | ⭐⭐⭐⭐ |
| **robots.txt AI crawlers** | ✅ 已開放 | ⭐⭐⭐⭐ |
| **FAQPage schema** | ⚠️ 只有 SCR guide 有（6 條 Q&A） | ⭐⭐ |
| **HowTo schema** | ⚠️ 只有 SCR guide 有（7 steps） | ⭐⭐ |
| **Person schema（Author bylines）** | ✅ 50+ blog posts | ⭐⭐⭐⭐ |
| **Article schema** | ⚠️ ~22/87 blog posts | ⭐⭐ |
| **Breadcrumb schema** | ⚠️ SCR page only | ⭐ |
| **Question-format H3 headings** | ❌ 未做 | ⭐ |
| **Answer-first content structure** | ⚠️ 部分頁面有 FAQ 但冇 direct answer sections | ⭐⭐ |
| **QAPage schema** | ❌ 未用 | ⭐ |
| **SiteNavigationElement** | ❌ 未用 | ⭐ |
| **WebSite SearchAction** | ❌ 未用 | ⭐ |
| **Blog content freshness** | ⚠️ 部分文章有 update date | ⭐⭐⭐ |
| **Step-by-step guides** | ✅ 產品頁係 step-by-step 格式 | ⭐⭐⭐⭐ |
| **FAQ sections on pages** | ✅ 首頁同部分 blog 有 FAQ | ⭐⭐⭐ |

**整體 AEO 準備度：45/100** — 基礎已有但 Schema 同 Content Structure 仲有好多空間。

### 6.2 ESGov 內容類型 AEO 適合度分析

#### 🔥 高適合度（直接可優化）

| 內容類型 | 例子 | AEO 適合度 | 原因 |
|:---------|:-----|:----------|:------|
| **Step-by-step guides** | 股份轉讓 5 步驟、SCR 7 步驟 | ⭐⭐⭐⭐⭐ | 天然適合 HowTo schema |
| **Definition content** | 「咩係 SCR？」「咩係厘印費？」 | ⭐⭐⭐⭐⭐ | Answer engines 最愛定義類 |
| **FAQ sections** | 首頁 FAQ、Blog FAQ | ⭐⭐⭐⭐⭐ | FAQPage schema 直接對應 |
| **流程教學** | 點樣查冊、點樣交印花稅 | ⭐⭐⭐⭐⭐ | HowTo + Step-by-step 完美 match |
| **比較內容** | 免費查冊 vs 收費查冊 | ⭐⭐⭐⭐ | Table format 適合 snippet |

#### ⚠️ 中等適合度（需要改結構）

| 內容類型 | 例子 | AEO 適合度 | 原因 |
|:---------|:-----|:----------|:------|
| **Blog posts（一般）** | MPF 指南 | ⭐⭐⭐ | 需要加 direct answer 開頭 |
| **Product pages** | 股份轉讓 landing page | ⭐⭐⭐ | 需要重組 content hierarchy |
| **Checklist 內容** | Due diligence checklist | ⭐⭐⭐ | 需要用 list schema |
| **真實經驗分享** | 血淚教訓、親身經歷 | ⭐⭐⭐ | 對 E-E-A-T 有幫助 |

#### ❌ 低適合度（AEO 唔係 priority）

| 內容類型 | 例子 | 原因 |
|:---------|:-----|:------|
| **PDF 生成工具** | 線上 PDF generator | Answer engines 唔會引用 tools |
| **Homepage pitch** | 首頁介紹文字 | 太 general，唔係 specific query |
| **Disclaimer / Legal** | 免責聲明 | 冇 AEO 價值 |

### 6.3 ESGov 嘅 AEO 競爭優勢

1. **Niche 優勢：** 香港公司秘書文件呢個 niche 好 specific，competitors 少做 content marketing
2. **Step-by-step 內容：** 天然適合 HowTo schema 同 AI citation
3. **真實經歷：** First-hand experience = E-E-A-T gold
4. **繁體中文 + 廣東話：** 香港本地 content 好珍貴，AI search engines 對 non-English content 嘅 citation 競爭冇咁激烈
5. **已做 GEO 基礎：** llms.txt, robots.txt, schema basics 已經有

### 6.4 Priority Pages for AEO Optimisation

| Priority | Page | AEO 機會 | 建議 Action |
|:---------|:-----|:---------|:------------|
| **🔴 P1** | `/shareholder-transfer/`（股份轉讓） | Highest traffic, High intent | +FAQPage, +HowTo, +direct answers |
| **🔴 P1** | `/significant-controllers-register/`（SCR） | Already has some schema | Expand FAQPage, add QAPage |
| **🔴 P1** | `/company-name-change/`（公司改名） | New guide | Add full schema stack |
| **🔴 P1** | `/deregistration/`（撤銷註冊） | Coming soon | Build with AEO from day 1 |
| **🟡 P2** | Blog: 公司查冊終極指南 | High informational value | +FAQPage schema, answer-first restructure |
| **🟡 P2** | Blog: 印花稅終極指南 | FAQ-friendly content | +FAQPage schema, tables for snippets |
| **🟡 P2** | Blog: MPF 終極指南 | Common employer query | +HowTo schema, answer-first sections |
| **🟢 P3** | Blog: 其他 80+ posts | Batch process | Add Article schema + direct answers |

---

## 7. 具體行動計劃

### 7.1 Phase 1 — Immediate Quick Wins（呢個月做）

#### Action 1.1：加 Question-Format H3 Headings 到 4 個產品頁

**點做：** 將每個產品頁嘅 step headings 改為自然問題形式

**放喺邊頁：**
- `/shareholder-transfer/`
- `/company-name-change/`
- `/significant-controllers-register/`
- `/deregistration/`

**例子：**
```
❌ 而家：Step 1: 準備文件
✅ 改做：股份轉讓要準備咩文件？
```

**預計影響：** High — 直接提升 AI snippet extraction 機會（2.8x citation lift）

---

#### Action 1.2：Expand FAQPage Schema — SCR Guide

**點做：** 將 SCR guide 嘅 FAQ 從 6 條擴展到 15-20 條，涵蓋所有常見追問

**預計影響：** Medium-High — FAQPage 係最高 impact AEO schema

---

#### Action 1.3：Add FAQPage Schema to 印花稅 Guide

**點做：** 印花稅 guide 已經有 7 條 FAQ 喺 page 底，直接加 FAQPage JSON-LD

**預計影響：** Medium — 現成 FAQ content，只需加 schema

---

#### Action 1.4：Fix Wikipedia Draft Link

**點做：** 改 draft 入面嘅 scr-guide link 去正確 URL

**預計影響：** High — Wikipedia citation 係 AI search engines 最信任嘅來源之一

---

### 7.2 Phase 2 — Content Structure Overhaul（下個月做）

#### Action 2.1：Add Answer-First Openings to All Major Guides

**點做：** 每個 major guide 嘅每個 section，開頭加 40-60 字 direct answer

**放喺邊頁：**
- 所有 4 個產品頁 + 3 個 flagship blog posts（查冊、印花稅、MPF）

**格式模板：**
```
## 股份轉讓要點做？

股份轉讓喺香港需要 5 個步驟，約 1-2 星期完成：
首先簽署股份轉讓文件，然後去稅局打釐印（繳交 0.2% 印花稅），
之後更新公司股東名冊，發出新股票證書，
最後提交 NAR1 周年申報表俾公司註冊處。
```

**預計影響：** High — Answer-first structure 係 AEO 核心

---

#### Action 2.2：Add HowTo Schema to Remaining 3 Product Pages

**點做：** 複製 SCR guide 嘅 HowTo schema pattern 到：
- `/shareholder-transfer/`
- `/company-name-change/`
- `/deregistration/`

**預計影響：** High — HowTo schema 係 step-by-step content 嘅最佳 schema

---

#### Action 2.3：Add QAPage Schema to High-Value Blog Posts

**點做：** 以下 blog posts 有 Q&A format content，加 QAPage schema：
- 公司查冊終極指南（有 FAQ section）
- 印花稅終極指南（有 FAQ section）
- MPF 終極指南（有 FAQ section）

**預計影響：** Medium — QAPage schema 專為 Q&A 內容設計

---

#### Action 2.4：Add Breadcrumb Schema to All Pages

**點做：** 用 script 批量加 breadcrumb JSON-LD 到所有 blog posts 同 generator pages

**預計影響：** Medium — AI crawlers 用 breadcrumbs 理解 site structure

---

### 7.3 Phase 3 — Schema Foundation（呢季做）

#### Action 3.1：Expand Article Schema to All 87 Blog Posts

**點做：** Run existing `add-blog-schema.py` script on remaining ~65 posts

**預計影響：** Medium-High — Article schema 係 AI content classification core signal

---

#### Action 3.2：Add SiteNavigationElement Schema

**點做：** 加 JSON-LD SiteNavigationElement 到 `index.html` 同所有 product pages

**預計影響：** Medium — 幫助 AI crawlers 理解 site architecture

---

#### Action 3.3：Add WebSite Schema with SearchAction

**點做：** 加 WebSite schema 到 `index.html`

**預計影響：** Low-Medium — 但係 standard best practice

---

### 7.4 Phase 4 — Advanced AEO（長期策略）

#### Action 4.1：Create Topic Clusters / Question Trees

**點做：** 每個 major service（股份轉讓、SCR、公司改名）建立 content cluster：
- One primary guide（已存在）
- 3-5 supporting blog posts answering related questions
- Internal links connecting them

**例子（股份轉讓 cluster）：**
```
Primary: 股份轉讓完整指南
├── Blog: 股份轉讓印花稅點計？
├── Blog: 股份轉讓要幾耐？
├── Blog: 股份轉讓 vs 饋贈（Gift）有咩分別？
├── Blog: 股份轉讓後點樣更新公司紀錄？
└── Blog: 股份轉讓失敗嘅 5 個常見原因
```

**預計影響：** High — Topic authority 係 AI citation 嘅關鍵因素

---

#### Action 4.2：Freshness Schedule

**點做：** 建立 content freshness calendar：
- 每季 review 更新所有 product guides
- 每月 review 更新 high-traffic blog posts
- 所有 pages 顯示最後更新日期

**預計影響：** High — Freshness 係 AI citation 嘅 major factor（商用內容 83% <12 個月）

---

#### Action 4.3：Off-Site AEO — Earn Citations

**點做：**
1. **Wikipedia:** Submit 已準備好嘅 Significant Controllers Register draft
2. **Quora/Reddit:** 用 `quora-answer-draft.md` template 回答相關問題，link 到 ESGov
3. **Guest articles:** 喺 HK business blogs/forums 投稿
4. **Google Business Profile:** Create/claim ESGov GBP

**預計影響：** Medium — External citations build authority signals

---

#### Action 4.4：Speakable Schema for Voice Search

**點做：** 喺每個 guide 嘅關鍵定義段落加 Speakable schema

**預計影響：** Low-Medium — Voice search 正在增長但 ESGov 嘅 voice search volume 有限

---

### 7.5 Technical Changes 彙總

| Change | Type | Effort | Impact |
|:-------|:-----|:-------|:-------|
| Question-format H3s 加到 4 個產品頁 | Content | 低 | 高 |
| FAQPage schema 擴展 + 新增 | Schema | 低 | 高 |
| HowTo schema 加到 3 個產品頁 | Schema | 中 | 高 |
| Answer-first 段落加到 guides | Content | 中 | 高 |
| QAPage schema 加到 blog posts | Schema | 低 | 中 |
| Breadcrumb schema 加到全站 | Schema | 中 | 中 |
| Article schema 擴展到全 blog | Schema | 中 | 中高 |
| Topic clusters 建立 | Content | 高 | 高 |
| Freshness schedule | Process | 中 | 高 |
| Off-site citations | Marketing | 高 | 中高 |
| SiteNavigationElement schema | Schema | 低 | 中 |
| WebSite SearchAction schema | Schema | 低 | 低中 |

---

## 8. Quick Wins vs 長期策略

### 8.1 Quick Wins（1-2 星期內見效）

| # | Action | 預計投入 | 預計 AEO Impact |
|:-:|:-------|:---------|:----------------|
| 1 | 加 question-format H3s 到 4 個產品頁 | 2 小時 | 🟢 高 |
| 2 | 擴展 SCR FAQPage schema（6→15+ 條） | 1 小時 | 🟢 高 |
| 3 | 加 FAQPage schema 到印花稅 guide | 30 分鐘 | 🟢 中 |
| 4 | Fix Wikipedia draft link | 15 分鐘 | 🟢 高 |
| 5 | 加 QAPage schema 到 3 個 blog posts | 1 小時 | 🟡 中 |
| 6 | 加 Breadcrumb schema 到全站（用 script）| 2 小時 | 🟡 中 |
| 7 | 加 WebSite SearchAction schema | 15 分鐘 | 🔵 低中 |

### 8.2 Medium-Term（呢季完成）

| # | Action | 預計投入 | 預計 AEO Impact |
|:-:|:-------|:---------|:----------------|
| 8 | Add HowTo schema to 3 product pages | 3-4 小時 | 🟢 高 |
| 9 | Answer-first 重寫 4 個 product guides | 8-12 小時 | 🟢 高 |
| 10 | Article schema 擴展到所有 blog posts | 用 script batch run | 🟢 中高 |
| 11 | Answer-first 重寫 3 個 flagship blog posts | 6-8 小時 | 🟢 中高 |
| 12 | SiteNavigationElement schema | 1 小時 | 🟡 中 |

### 8.3 Long-Term Strategy（呢半年）

| # | Action | 預計投入 | 預計 AEO Impact |
|:-:|:-------|:---------|:----------------|
| 13 | Topic clusters 建立（每個 service 3-5 篇 supporting posts）| 20-30 小時 | 🟢 高 |
| 14 | Freshness schedule 執行 | Ongoing | 🟢 高 |
| 15 | Wikipedia page submission | 5-10 小時 | 🟢 高 |
| 16 | Quora/Reddit/Guest blogging campaign | Ongoing | 🟡 中高 |
| 17 | Google Business Profile | 2 小時 | 🟡 中 |
| 18 | AEO performance tracking dashboard | 4-6 小時 | 🔵 低（但必需） |

---

## 9. 測量 AEO 成效

### 9.1 傳統 SEO 指標仍然適用嘅部分

- **Organic traffic**（AI referral traffic 都會 reflected 喺呢度）
- **Search Console impressions**（特別係 high impressions + low CTR = snippet 機會）
- **Keyword rankings**（仍然同 AI citation 有關聯）

### 9.2 新嘅 AEO 指標

| Metric | 點樣測量 | Target |
|:-------|:---------|:-------|
| **AI Citation 次數** | 手動 query ChatGPT/Perplexity/Gemini 每週 | 每月 +20% |
| **Brand Mentions in AI** | SE Ranking / Semrush AI visibility | 每月新增 5+ mentions |
| **Featured Snippet Count** | Ahrefs / Semrush / Moz | 每月 +2-3 snippets |
| **AI Referral Traffic** | GA4（filter by referrer: chatgpt.com, perplexity.ai 等）| 每月 +30% |
| **Share of Voice in AI** | 手動 + tools | 逐漸提升 |
| **llms.txt Access** | Server logs（crawler hits to llms.txt）| 每週有 crawler activity |
| **零點擊 Brand Exposure** | Estimated from Search Console + AI mention data | 每季 review |

### 9.3 手動 AEO 檢查清單（每週）

```
[ ] Query ChatGPT Search: 「香港公司 股份轉讓 要點做」— ESGov 出現？
[ ] Query Perplexity: 「香港 SCR 重要控制人登記冊」— ESGov 被引用？
[ ] Query Google: 「股份轉讓 印花稅 點計」— Featured snippet？
[ ] Query Gemini: 「香港有限公司 撤銷註冊」— ESGov 出現？
[ ] Check GA4 for AI referrer traffic
[ ] Check Search Console for new impressions
```

### 9.4 Tools 推薦

| Tool | 用途 | 費用 |
|:-----|:-----|:-----|
| **Semrush** | AI visibility tracking, keyword research | Paid |
| **SE Ranking** | AI mention tracking | Paid |
| **Ahrefs** | Featured snippet tracking, content gap | Paid |
| **Google Search Console** | Free — impressions, clicks, queries | Free |
| **AnswerThePublic** | Question discovery | Free/Paid |
| **AlsoAsked** | Follow-up question research | Free/Paid |
| **AirOps** | Enterprise AEO tracking | Paid |
| **Otterly.ai** | AI citation monitoring | Paid |

---

## 10. 附錄：參考資源

### 10.1 關鍵研究來源

| 來源 | URL | 重點 |
|:-----|:----|:-----|
| AirOps AEO Guide 2026 | https://www.airops.com/blog/aeo-answer-engine-optimization | 7 strategies, data points |
| Frase.io AEO Guide 2026 | https://www.frase.io/blog/what-is-answer-engine-optimization | RAG pipeline, 6-step framework |
| CXL AEO Guide 2026 | https://cxl.com/blog/answer-engine-optimization-aeo-the-comprehensive-guide | 5 strategies, success stories |
| Parachute Design AEO Guide | https://parachutedesign.ca/blog/answer-engine-optimization | Designer-focused, AEO vs GEO vs ASK |
| DOJO AI AEO Guide 2026 | https://www.dojoai.com/blog/answer-engine-optimization-aeo-guide-dynamic-ai-seo | Citation economy, platform-specific |
| Semrush AEO vs SEO | https://www.semrush.com/blog/aeo-vs-seo | Core differences, measurement |
| Digital Guider AEO Guide | https://digitalguider.com/blog/answer-engine-optimization | Beginner-friendly, 7 steps |
| Search Engine Land — Featured Snippets | https://searchengineland.com/guide/featured-snippets | Position Zero deep dive |

### 10.2 Schema.org Resources

| Resource | URL |
|:---------|:----|
| FAQPage Schema | https://schema.org/FAQPage |
| HowTo Schema | https://schema.org/HowTo |
| QAPage Schema | https://schema.org/QAPage |
| Article Schema | https://schema.org/Article |
| BreadcrumbList | https://schema.org/BreadcrumbList |
| Google Structured Data Guide | https://developers.google.com/search/docs/appearance/structured-data |

### 10.3 ESGov 現有檔案參考

| File | Path | 用途 |
|:-----|:-----|:-----|
| `llms.txt` | `esgov.org/llms.txt` | AI curated summary |
| `llms-full.txt` | `esgov.org/llms-full.txt` | Full site content dump |
| `robots.txt` | `esgov.org/robots.txt` | AI crawler config |
| `geo-readiness-report.md` | Project root | Previous GEO audit |
| `quora-answer-draft.md` | Project root | Quora answer template |

---

## 總結

### AEO 對 ESGov 嘅關鍵機會

1. **ESGov 嘅 step-by-step guides 係 AEO 嘅黃金內容** — 只需加正確嘅 schema（FAQPage + HowTo）同 answer-first structure
2. **香港公司秘書 niche 競爭細** — 全球 AEO 資源幾乎全部英文，繁體中文 content 係藍海
3. **已經有 GEO 基礎** — llms.txt、robots.txt、schema basics 已就位，差最後一里路
4. **Quick wins 可以好快見效** — 最快 impact 嘅 actions（question-format H3s、FAQPage schema）每項只需 1-2 小時

### 下一步建議

1. **今個星期：** 完成 Phase 1（Quick Wins）— 7 項 actions，共 ~7 小時
2. **下個月：** 完成 Phase 2（Content Structure Overhaul）— Answer-first + 更多 schema
3. **呢季：** 完成 Phase 3（Schema Foundation）+ Phase 4 開始（Topic Clusters）
4. **持續：** 建立 AEO monitoring routine（每週手動 check + 每月 tool-based tracking）

---

*本報告基於 2026 年 6 月最新研究，AEO 領域發展迅速，建議每季檢討策略。*
