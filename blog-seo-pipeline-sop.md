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
| `gold-box`（黃色貼士/真實案例） | `bg-amber-50 border-amber-200`（自創顏色，除咗「僅供參考」banner） |
| `warn-box`（紅色警告/風險） | `bg-red-50 border-red-200` |
| `tip-box`（藍色提示） | `bg-blue-50 border-blue-200` |
| `compare-box`（比較內容） | `bg-gray-50` 自創 box |
| `btn-gov btn-gov-primary`（CTA 按鈕） | 自創 button style |
| `text-gold font-medium`（內文 link） | `text-blue-600 underline` |
| navy/gold 品牌色 | default Tailwind 色（blue/indigo/emerald 等） |

**做法：**
1. Copy 現有文章（例如 `blog/香港公司授權書PowerOfAttorney終極指南/index.html`）嘅 head + `<style>` block，保留佢哋嘅 box classes 定義
2. 全部 box 用 `gold-box` / `warn-box` / `tip-box` / `compare-box` / `step-card` / `flag-item`
3. CTA 用 `btn-gov btn-gov-primary`（參考現有文章用法）
4. **唔好跟 tailwind.config 整新色** — 用已定義嘅 navy/gold 就算

### 3a-2. Icon 規範（⚠️ 唔可以用 emoji 當 icon）

**所有 icon 必須用 Lucide SVG（`<i data-lucide="...">`），唔可以用 emoji（❌⚠️💡📑🔍 等）做裝飾 icon：**

| Emoji | 換做 Lucide |
|-------|------------|
| ❌（錯誤） | `circle-x` |
| ⚠️（警告） | `triangle-alert` |
| 💡（貼士） | `lightbulb` |
| 📑（目錄） | `list` |
| 🔍（真實案例） | `flag` |
| ✅（完成） | `circle-check` |

**做法：**
1. 文章 head 加 Lucide CDN（同全站一致）：
   ```html
   <script defer src="https://unpkg.com/lucide@latest"></script>
   <script>document.addEventListener("DOMContentLoaded",function(){lucide.createIcons()});</script>
   ```
2. Icon 寫法：`<i data-lucide="circle-x" class="w-4 h-4 inline-block mr-1" aria-hidden="true"></i>`（decorative icon 加 `aria-hidden="true"`，跟 ui-ux-pro-max skill 指引）
3. **單一 icon 家族**（Lucide）— 唔可以混 Phosphor/Heroicons
4. 發佈前 check：`grep -cE "❌|⚠️|💡|📑|🔍" 文章` 要 = 0（正文自然用到嘅除外，例如「請教專業人士」唔撓）

### 3b. 免責聲明（⚠️ 必做）

**涉及法律 / 程序 / 費用 / 合規內容嘅文章，必須加「僅供參考」警告 banner，而且要放「最上 + 最下」兩個位置：**

1. **⬆️ 最上**（文章開頭、目錄之前）：
   ```html
   <div class="bg-amber-50 border-2 border-amber-300 rounded-xl p-4 sm:p-5 mb-8 flex items-start gap-3">
     <div class="w-9 h-9 shrink-0 rounded-full bg-amber-400/20 flex items-center justify-center">
       <i data-lucide="triangle-alert" class="w-5 h-5 text-amber-600" aria-hidden="true"></i>
     </div>
     <div>
       <p class="font-bold text-amber-800">僅供參考</p>
       <p class="text-sm text-amber-700 leading-relaxed">本文章內容只係一般資訊分享，<strong class="text-amber-800">唔構成法律意見</strong>。涉及[主題]，強烈建議先諮詢[專業人士]。每單[案件/情況]嘅細節都唔同，適用[程序/規則]可能因情況而異。</p>
     </div>
   </div>
   ```
2. **⬇️ 最下**（文章完結之後、Author Bio 之前）：
   ```html
   <div class="bg-amber-50 border-2 border-amber-300 rounded-xl p-4 sm:p-5 flex items-start gap-3">
     <div class="w-9 h-9 shrink-0 rounded-full bg-amber-400/20 flex items-center justify-center">
       <i data-lucide="triangle-alert" class="w-5 h-5 text-amber-600" aria-hidden="true"></i>
     </div>
     <div>
       <p class="font-bold text-amber-800">僅供參考</p>
       <p class="text-sm text-amber-700 leading-relaxed">本文章內容只係一般資訊分享，<strong class="text-amber-800">唔構成法律意見</strong>。實際[情況]嘅[程序/費用/可行性]會因個別情況而有重大分別，決定自行處理之前，請務必諮詢[執業律師]。</p>
     </div>
   </div>
   ```
   （⚠️ 呢個 amber banner 係唯一容許用 `bg-amber-50 border-amber-300` 嘅地方 — 佢係醒目標示，唔係普通 box）

3. **Footer 都要有**：`© 2026 ESGov · 香港公司文件指南（所有內容僅供參考，不構成法律意見）`

4. 措辭按文章主題調整，但「僅供參考」+「唔構成法律意見」+「建議諮詢專業人士」三點一定要有

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

### 3d. 文章分類（⚠️ 必做 — 分類系統）

**每篇文章必須歸入 8 大分類之一，blog 首頁 filter 靠 `data-category` tag 分組：**

| 分類 | 涵蓋主題 | 例子 |
|------|---------|------|
| `開公司` | 公司註冊成立、創業比較、銀行戶口、數碼轉型、開公司後清單 | 開公司終極指南、銀行戶口實戰 |
| `股份` | 股份轉讓、配發、回購、減資、ESOP、股東協議、轉股東 | 股份轉讓流程、Sold Note |
| `合規` | SCR、條例622、查冊、法定紀錄、罰則、會計記帳、零申報、e-Services | SCR終極指南、合規時間表 |
| `董事股東` | 董事職責/辭任/袍金/借貸、股東大會AGM、股權、派息、繼承 | 董事辭任、AGM暨書面決議 |
| `報稅審計` | 利得稅、審計核數、印花稅厘印、暫繳稅、離岸利得、IR56B | 第一次報稅、審計實戰 |
| `人事` | 僱傭條例、MPF、員工手冊、解僱、長期服務金 | 僱傭條例、第一次請人 |
| `財務保險` | 保險(D&O/勞保)、貸款融資、追數、政府資助、跨境資金 | D&O保險、商業貸款 |
| `公司文件` | 授權書、公章、電子簽署、章程、ND2A/NDR1、周年申報、撤銷註冊、清盤、改名、秘書 | ND2A教學、公司印章 |

**做法：**
1. 寫文時判斷文章屬於邊個分類（對照上表）
2. 新 card 加喺 `blog/index.html` 時，一定要加 `data-category="{分類名}"` 喺 card 嘅 `<a>` tag：
   ```html
   <a href="/blog/{slug}/" data-category="合規" class="block bg-white rounded-xl border-2 border-gold/30 p-5 hover:shadow-lg hover:border-gold transition-all duration-300 group bg-gold/[0.02]">
   ```
   （❌ 唔加 data-category = 文章唔會喺任何分類 filter 出現，淨係喺「全部」見到）
3. **部 tab 數字**（例如「合規（12）」）要同步 +1：
   ```html
   <button data-filter="合規" ...>合規（13）</button>
   ```
4. 分類 mapping 檔 `scripts/blog-categories.json` 更新新文章：
   ```bash
   python3 scripts/categorize-blog.py   # 重新生成（keyword 自動分類）
   ```
5. 發佈後驗證：喺 blog 首頁 click 對應分類 tab，確認新 card 出現

**分類判斷輔助：** `scripts/categorize-blog.py` 用 keyword matching 自動分類，如果文章標題包含分類關鍵字就會自動歸類。手動加入新文章時可以行一次呢個 script 檢查分類準確性。

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
- [ ] **文章已歸入正確分類（data-category tag + tab 數字更新）**（見 3d）

### 4b. Technical Setup
- [ ] 文章放 `blog/{article-slug}.html`
- [ ] 更新 `blog/index.html`（加新 card 做第一條 + **data-category tag** + **tab 數字 +1**）
- [ ] 更新 `index.html`（主頁 blog section — 加新 card 做第一條）
- [ ] 更新 `scripts/blog-categories.json`（行 `python3 scripts/categorize-blog.py`）
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
