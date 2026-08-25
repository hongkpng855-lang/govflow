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

### 3a. UI 規範（⚠️ 唔可以用 default UI）

文章 UI 一定要跟 site 既有 custom classes，**唔准**用 default Tailwind 色當風格：

| ✅ 用呢啲 | ❌ 唔好用 |
|-----------|---------|
| `gold-box`（黃色貼士/真實案例） | `bg-amber-50 border-amber-200`（自創顏色） |
| `warn-box`（紅色警告/風險） | `bg-red-50 border-red-200` |
| `tip-box`（藍色提示） | `bg-blue-50 border-blue-200` |
| `compare-box`（比較內容） | `bg-gray-50` 自創 box |
| `btn-gov btn-gov-primary`（CTA 按鈕） | 自創 button style |
| `text-gold font-medium`（內文 link） | `text-blue-600 underline` |
| navy/gold 品牌色 | default Tailwind 色（blue/indigo/emerald 等） |

**做法：**
1. Copy 現有文章（例如 `blog/香港公司授權書PowerOfAttorney終極指南/index.html`）嘅 head + `<style>` block，保留佢哋嘅 box classes 定義
2. 全部 box 用 `gold-box` / `warn-box` / `tip-box` / `compare-box`
3. CTA 用 `btn-gov btn-gov-primary`（參考現有文章用法）
4. **唔好跟 tailwind.config 整新色** — 用已定義嘅 navy/gold 就算

### 3b. 免責聲明（⚠️ 必做）

**涉及法律 / 程序 / 費用 / 合規內容嘅文章，必須加「僅供參考」聲明：**

1. **Intro 內**（第一段之後）：一個 `warn-box`：
   ```html
   <div class="warn-box mt-4">
     <p><strong>⚠️ 僅供參考：</strong>本文章嘅內容只係一般資訊分享，唔構成法律意見。涉及實際訴訟或授權書簽署，強烈建議先諮詢執業律師。每單案件嘅情況都唔同，適用程序可能因案件而異。</p>
   </div>
   ```
   （措辭按文章主題調整，但「僅供參考」+「唔構成法律意見」+「建議諮詢專業人士」三點一定要有）

2. **Footer 都要有**：`© 2026 ESGov · 香港公司文件指南（所有內容僅供參考，不構成法律意見）`

### 3c. 範本處理（⚠️ 唔好全文 show 範本）

**文章有範本（授權書/信模板/表格樣本）時：**
- ❌ **唔好**喺文章內文全文 display 成個範本（長 text block）
- ✅ **改為**：
  - 描述範本包含咩欄位/要咩資料（用 checklist 或者一段文字）
  - 加 `tip-box` 引導去 site 有範本嘅頁面：
    ```html
    <div class="tip-box mt-4">
      <p><strong>💡 免費範本：</strong>我哋已經準備咗一份「XXX」參考範本，喺<a href="/blog/XXX/" class="text-gold font-medium">XXX 頁面</a>入面可以攞到，跟住改資料就用到。</p>
    </div>
    ```
  - 如果 site 有 generator（例如 `nar1-generator`），直接 link generator 頁面
- 原因：一個係 SEO（唔想 template 內容做成 duplicate content），一個係引導用戶去 site 其他頁面（內連深度）

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
- [ ] 更新 `blog/index.html`（加新 card 做第一條）
- [ ] 更新 `index.html`（主頁 blog section — 加新 card 做第一條）
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
