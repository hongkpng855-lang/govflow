# ESGov Blog Article Pipeline SOP

## 總覽

SEO agent 主導成個流程，Researcher 同 Writer 喺中間執行。

```
SEO（起點）→ Researcher → Writer → SEO（終點+deploy）
```

---

## Phase 1：SEO — Topic Selection + Brief

### 1a. Keyword Research
- 用 web_search 確認 keyword 搜尋量 + 競爭程度
- 優先選擇：
  - 高搜尋量 + 低競爭（Quick win）
  - 長尾關鍵字（高轉換意圖）
  - Product-related keywords（直接 funnel 去產品頁）
- 記錄 target keyword + related keywords

### 1b. Content Brief 格式

每篇文開一個 brief file：`blog/_briefs/{article-slug}-brief.md`

```markdown
# SEO Brief: {article title}

## Target Keyword
{primary keyword}

## Related Keywords
- {kw1}
- {kw2}

## Search Intent
{資訊型 / 比較型 / 行動型}

## Target Audience
{descriptions}

## Structure Outline
1. H2: {section title}
2. H2: {section title}
   - H3: {subsection}
3. H2: {section title}

## Key Points to Cover
- {point 1}
- {point 2}

## Internal Links Required
- [{product page name}](/product-url/) — 放喺 {section}
- [{generator page}](/generator-url/) — 放喺 {section}

## CTA
{讀完文之後想佢做咩}

## Word Count Target
{800-1500 / 1500-3000}
```

---

## Phase 2：Researcher — 資料搜集

收到 SEO brief 後：
1. 搵官方來源（gov.hk / cr.gov.hk / ird.gov.hk）
2. 搵真實案例 / 討論區痛點（lihkg / discuss.com.hk）
3. 搵競爭對手文章（睇佢哋 cover 咗咩、漏咗咩）
4. 整理成 research notes
5. 交俾 Writer

---

## Phase 3：Writer — 內容創作

收到 SEO brief + Research notes 後：
1. 跟 structure outline 寫文
2. 用口語廣東話，真實經歷口吻
3. 自然融入 target keyword（H2/H3/內文）
4. 文章結尾加 CTA link 去 product page
5. 交俾 SEO review

---

## Phase 4：SEO — Review + Optimize + Deploy

### 4a. SEO Review Checklist
- [ ] Title 含 target keyword（< 60 chars）
- [ ] Meta description 含 keyword + CTA（120-160 chars）
- [ ] H1 得一個，含 keyword
- [ ] H2/H3 結構合理，含 related keywords
- [ ] Internal links 已加（最少 2 個 product links）
- [ ] Keyword density natural（唔好 stuffing）
- [ ] Canonical URL 正確
- [ ] OG tags 有齊
- [ ] Article schema 已加
- [ ] Breadcrumb 已加

### 4b. Technical Setup
- [ ] 文章放 `blog/{article-slug}.html`
- [ ] 更新 `blog/index.html`（加新 card）
- [ ] 更新 `sitemap.xml`
- [ ] 行 seo-checker.py 確認 0 issues
- [ ] Deploy（等 user 批准）

---

## Quality Gates

| Gate | 負責人 | 通過條件 |
|:----:|:------:|---------|
| Brief 完成 | SEO | Keyword + structure 清晰 |
| Research 完成 | Researcher | 有官方來源 + 案例 |
| Draft 完成 | Writer | 跟 outline、自然含 keywords |
| SEO Review 完成 | SEO | Checklist 全部通過 |
| Deploy | SEO | User 批准 + 0 issues |
