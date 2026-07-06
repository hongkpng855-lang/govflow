# builder_soul.py
# ESGov Builder Operating Definitions & Collective Knowledge
# ============================================================
# This file is the SINGLE SOURCE OF TRUTH for all ESGov development
# patterns, Mode definitions, completed work, lessons learned,
# available skills, and tools inventory.
#
# Every builder agent MUST load this file before starting any work.
# Update this file whenever you discover a new pitfall, complete a
# product, or learn a non-obvious pattern.
# ============================================================

"""
==================================================
ESGov 步驟模式定義（Mode A / B / C）
==================================================

每步（step）分為三種模式，定義如下：

---

## Mode A — 互動填表工具（Interactive Generator）

hasGenerator: true
有互動工具（jsPDF）可以直接填寫 + 生成 PDF。

Card 顯示：
  - generator 圖片（xxx-template.png，乾淨 form 截圖，NOT 全頁 screenshot）
  - 「可修改文件」按鈕 → 互動表格
  - 🚀 填寫 + 生成 PDF

Generator 頁面 include：
  - Info banner（optional）
  - Interactive form with jsPDF
  - Preview card（可修改文件截圖）
  - 常見錯誤
  - 返回按鈕

參考：
  - Product 1（股份轉讓）Step 1（Sold Note）
  - Product 4（撤銷註冊）Step 1（Checklist）, Step 6（IRC3113 — 之前係 A，而家改咗 B）

---

## Mode B — 官方表格範例檢視（Official Form Viewer）

hasGenerator: false
generatorUrl → 官方 PDF link（CR / IRD official fillable PDF）
冇互動工具，純粹官方表格展示 + download。

Card 顯示：
  - 官方表格截圖（PyMuPDF render from official PDF，200 DPI）
  - 📄 文件名稱（官方表格）
  - 按鈕：📄 下載官方表格

Generator 頁面 include（跟 NR2 pattern）：
  - 📌 Info banner（說明前提條件）
  - 🖼️ 官方表格 full image（clickable → lightbox modal）
  - ⚠️ 常見錯誤
  - 📥 下載官方表格（trigger email gate first → then open PDF in new tab）
  - ← 返回按鈕

Email Gate Requirement（v12.50+）：
  - ALL Mode B generator pages MUST have email gate BEFORE downloading
  - Pattern：button → checkEmailGate() → submit email → openOfficialPDF()
  - Same FormSubmit endpoint + localStorage flag as Mode A generators
  - `openOfficialPDF()` opens the government PDF URL in `_blank`

參考：
  - SCR Step 7（NR2）— 原型
  - Product 4（撤銷註冊）Step 2（IR1263）, Step 3（NDR1）, Step 6（IRC3113）

---

## Mode C — 純步驟說明（Pure Step Instructions）

hasGenerator: false（冇 generator）
generatorUrl: N/A
冇 documents array（或 documents 為空）
純粹資訊 / 指引頁，冇 form、冇工具、冇下載。

Card 顯示：
  - 步驟標題 + summary
  - 冇 generator card image
  - **所需文件 section 必須有 dashed card：**「此步驟不需要提交任何文件」

關鍵 implementation note：
  - 必須在 HTML template 包含 BOTH blocks：`s.documents && s.documents.length >= 1` AND `(!s.documents || s.documents.length === 0)`
  - 唔好忘記加 Mode C card！deregistration/index.html v12.46 就係漏咗，v12.47 先 retrofitted

參考：
  - Product 2（公司改名）Step 1（查冊公司名 + 檢查商標）— Mode C prototype
  - Product 4（撤銷註冊）Step 4（憲報公告）, Step 5（正式解散）

---

## 每個 Step 嘅 JSON 結構判斷方式

| Mode | hasGenerator | documents | generatorUrl | officialFormUrl |
|------|-------------|-----------|-------------|----------------|
| A    | true        | 有（1+ items） | 有（指向 generator） | optional |
| B    | false       | 有（1+ items） | = official PDF URL | required |
| C    | N/A         | 冇 / 空   | N/A         | N/A |

---

==================================================
已完成產品狀態（Completed Products）
==================================================

## Product 1：股份轉讓（shareholder-transfer）
路徑：/shareholder-transfer/
Steps：5 步，全部完成
- Step 1 Sold Note → Mode A ✅
- Step 2 Instrument of Transfer → Mode A ✅
- Step 3 Letter of Transferee → Mode A ✅
- Step 4 Audit Report → Mode A ✅
- Step 5 NAR1/NSC1 → Mode A ✅
Generators：sold-note-generator, instrument-transfer-generator, letter-of-transferee-generator, nar1-generator, nsc1-generator, audit-report-generator

## Product 2：公司改名（company-name-change）
路徑：/company-name-change/
Steps：5 步，全部完成
- Step 1 查冊公司名 → Mode C ✅（純步驟 prototype）
- Step 2 特別決議 → 有 generator（special-resolution）
- Step 3 NNC2 → 有 generator（nnc2）
- Step 4 領取證書 → 純步驟
- Step 5 更新記錄 → 純步驟

## Product 3：SCR（significant-controllers-register）
路徑：/significant-controllers-register/
Steps：7 步，全部完成
多位 generators：
- scr-shareholder-analysis-generator
- scr-identification-checklist-generator
- scr-notice-generator
- scr-designated-rep-generator
- scr-data-collection-generator
- scr-generator（main SCR register）
- scr-nr2-generator（Mode B prototype — NR2）
Known issue：secretary pricing ~$1,000/次 not $500/年

## Product 4：撤銷註冊（deregistration）
路徑：/deregistration/
Steps：6 步，全部完成 ✅ v12.49
- Step 1 資格檢査 → Mode A ✅（checklist generator）
- Step 2 申請 NNO（IR1263）→ Mode B ✅（official IRD form）
- Step 3 提交撤銷（NDR1）→ Mode B ✅（official CR form）
- Step 4 憲報公告 → Mode C ✅（純步驟）
- Step 5 正式解散 → Mode C ✅（純步驟）
- Step 6 解散後跟進（IRC3113）→ Mode B ✅（official IRD form，v12.49 從 A 轉 B）

---

==================================================
重大錯誤 / 教訓（Lessons Learned）
==================================================

### PATTERN: Double-escape `\\n` 陷阱
patch tool 會將 `\\n` double-escape 做 `\\\\n`。
Fix：patch 之後一定要 re-read file confirm，必要時再做一次 patch fix。
Affects：deregistration/index.html Step 4 details string（v12.46 → v12.47 hotfix）

### PATTERN: Cloudflare Cache
Cache max-age=600s（10分鐘）。
每次 deploy 後 curl confirm source，但 browser 可能 show old version。
Workaround：curl 直 check GitHub raw source，或者等 10 分鐘。

### PATTERN: Mode C Card 漏加
當建立新 product guide page 時，必須包括 BOTH template blocks upfront：
  - `s.documents && s.documents.length >= 1`（正常 document cards）
  - `(!s.documents || s.documents.length === 0)`（Mode C dashed card）
Reference：Product 2 Step 1（company-name-change/index.html）有正確 implementation。
deregistration/index.html v12.46 漏咗 → v12.47 retrofitted。

### PATTERN: Generator Image 政策
- Mode A：用 `xxx-template.png`（乾淨 form crop，html2canvas render from HTML template）
- Mode B：用 `xxx-official.png`（PyMuPDF 200 DPI render from official government PDF）
- 絕不能用全頁 screenshot 代替 form crop（v12.38 犯過 → v12.39 revert）

### PATTERN: Official Form 圖片生成
流程：
  1. curl -sL official PDF URL
  2. python3 fitz（PyMuPDF）render page 1 at 200 DPI
  3. save to assets/demo/{form-name}-official.png
  4. 用呢張圖 for ALL refs（main card + generator + lightbox）

### PATTERN: v12.41 IR1263 Mode B Rollback
最初改 Step 2 IR1263 做 Mode B 但未準備好（generator page 未 rewrite），
v12.41 revert 咗，v12.42 先正式完成。
Lesson：Mode 轉換要同時改 guide page CARD + generator page，唔可以分開。

### RULE: NO agent deploys without user approval
ESGov deploys to production (esgov.org via GitHub Pages + Cloudflare).
All agents work locally only by default.
Deploy requires explicit verbal go-ahead (e.g. "deploy", "上架", "push").
Exception: routine git pushes that don't affect live site.

---

==================================================
可用 Skills 索引（Available Skills）
==================================================

### ESGov-specific Skills（必讀）
- esgov-deploy：Deploy SOP + Cloudflare cache handling + verification
- esgov-page-dev：頁面開發流程、processes.json 結構、Step Icon 系統、HTML 模板規範、已知錯誤
- esgov-pdf-generator：html2canvas + jsPDF 開發指南 + 所有陷阱
- esgov-product-creation：新產品開發完整流程（research → 產品頁 → generators → deploy → SEO）
- esgov-generator-creation：互動 PDF generator 建立流程
- esgov-seo：SEO 操作流程（blog management、keyword strategy、article pipeline）
- esgov-blog-agent：專用 blog 出版 agent（寫文 → HTML → deploy）
- blog-seo-pipeline：Blog SEO article pipeline（brief → research → write → review → deploy）
- linkedin-automation：LinkedIn 自動化（login、Company Pages、publishing）
- cloudflare-api：Cloudflare API（token auth、Transform Rules、cache purge）

### General Development Skills
- web-development：網站開發、GitHub Pages、HTML/CSS/JS
- github-pr-workflow：PR lifecycle（branch → commit → open → CI → merge）
- github-code-review：Code review via gh CLI
- github-repo-management：Clone/create/fork repos
- systematic-debugging：4-phase root cause debugging
- test-driven-development：RED-GREEN-REFACTOR
- spike：Throwaway experiments

### Infrastructure Skills
- python-webapp-deploy：Flask/FastAPI/Django 部署（Railway、Render、Fly.io）
- gguf-quantization：GGUF + llama.cpp
- serving-llms-vllm：vLLM serving
- modal-serverless-gpu：Serverless GPU

### Media / Design Skills
- claude-design：HTML artifacts（landing, deck, prototype）
- excalidraw：Hand-drawn diagrams
- popular-web-designs：54 real design systems
- sketch：HTML mockups
- ui-cloning：Pixel-perfect UI recreation
- p5js：Generative art

### Productivity
- notion：Notion API
- google-workspace：Gmail/Calendar/Drive
- linear：Linear issue management
- ocr-and-documents：PDF text extraction（pymupdf, marker-pdf）
- word-document-creation：Word .docx creation
- nano-pdf：PDF text editing

---

==================================================
常用工具（Available Tools）
==================================================

### File Operations
- read_file：睇文件（唔好用 cat/head/tail）
- write_file：建立/覆蓋文件（唔好用 echo/cat heredoc）
- patch：Find-and-replace edit（唔好用 sed/awk）
- search_files：搜尋文件內容或檔名（唔好用 grep/rg/find/ls）

### Terminal & Execution
- terminal：Shell commands、builds、git、deploy、network
- execute_code：Python 腳本（多步處理、tool chaining、filtering）
- process：Background process management（poll/wait/log/kill）

### Browser
- browser_navigate：Load page + compact snapshot
- browser_snapshot：Full page content / accessibility tree
- browser_vision：Screenshot + visual analysis
- browser_console：JS debug、DOM inspection、page state extraction
- browser_click/browser_type/browser_scroll：Page interaction

### Web & Research
- web_search：Search web（supports operators: site:, filetype:, etc.）
- web_extract：Extract page content / PDF text

### AI & Workflow
- delegate_task：Parallel subagents for research / code review / debugging
- skill_view / skill_manage：Load / create / update skills
- memory：Persistent memory across sessions
- session_search：Search past conversations
- cronjob：Scheduled tasks
- todo：Task list management
- clarify：Ask user for clarification

### Communication
- send_message：Send to connected platforms（Telegram, Discord, etc.）
- text_to_speech：TTS audio generation

|
|==================================================
|產品頁精簡佈局（2026-07-06）
|==================================================
|
|由 share-transfer/ 頁面開始，產品頁改用以下新佈局：
|
|順序（由上到下）：
|  1. 📌 快速概覽（merged box）
|     - 3格卡片：🕐 需時 / 💰 費用 / ⚖️ 法律
|     - 底部 1句定義（含關鍵數據）
|     - 取代咗：⚡ Quick Answer + Description + 📊 Official Data（3 blocks→1）
|  2. 📊 比較表（預設收埋，點「▼ 睇對比」先展開）
|     - Alpine.js x-data="{ open: false }" + x-show="open"
|  3. Step-by-step 內容
|     - ☕ Donate micro-text 只喺 Step 1 顯示（x-show="s.stepNumber === 1"）
|  4. 📄 開始免費指南 CTA（生成文件）
|  5. 📚 相關指南（搬咗落生成文件下面）
|  6. 📝 Cite this（原格式保留，bg-gray-100 box）
|
|生產文件（doc cards、step details、generator links、demo images）完全唔郁。
|
|其餘 3 個產品頁（company-name-change、scr、deregistration）需要用相同佈局改動。
|

"""
