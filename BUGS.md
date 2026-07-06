# 🐛 ESGov Bugs Document

記錄開發過程中發現嘅 bugs、原因、修復方法，避免再次發生。

---

## HTML / CSS Bugs

### B001 — Generator 頁面 HTML Line Number Corruption

**發現日期：** 2026-07-07
**影響範圍：** `deregistration-ir1263-generator`、`deregistration-ndr1-generator`、`deregistration-irc3113-generator`

**症狀：**
- 顏色錯亂（brand colors navy/gold 冇生效）
- 按鈕變晒 default style
- Logo styling 失效
- Button text 出現「119|」「120|」等奇怪數字前綴

**原因：**
- 編輯 HTML 時唔小心 paste 咗 editor 嘅 line numbers（如 `118|`、`119|`）入 file
- 由某一行開始，全部 200+ 行嘅 content 前面都有 `NN|` 前綴
- HTML parser 將 `NN|` 當做普通 text，破壞咗 HTML structure

**修復方法：**
```python
# 用 regex 清除行號前綴
import re
content = re.sub(r'\n(\d+\|)', '\n', content)
content = re.sub(r'^\d+\|', '', content)
```

**預防措施：**
- ✅ 編輯 HTML 時唔好用顯示行號嘅 editor copy/paste
- ✅ 如果用 VS Code / Sublime 等，確保 copy 時冇選取行號欄
- ✅ commit 前做一次 syntax check / HTML validation

---

### B002 — Unclosed `<script>` Tag（Tailwind CDN）

**發現日期：** 2026-07-07
**影響範圍：** `deregistration-ir1263-generator`、`deregistration-ndr1-generator`、`deregistration-irc3113-generator`

**症狀：**
- Tailwind CSS 完全冇 load
- 所有 `bg-navy`、`bg-gold`、`text-white` 等 class 失效
- 跟 B001 同時發生，加劇咗版面錯亂

**原因：**
```html
<!-- ❌ 錯誤 -->
<script src="https://cdn.tailwindcss.com">
<link rel="stylesheet" href="/assets/css/style.css" />

<!-- ✅ 正確 -->
<script src="https://cdn.tailwindcss.com"></script>
<link rel="stylesheet" href="/assets/css/style.css" />
```
- `<script>` tag 冇 close (`</script>`)
- 後面嘅 `<link>` 被當做 script 嘅內容，永遠唔會生效

**修復方法：**
- 補返 `</script>` closing tag

**預防措施：**
- ✅ HTML `<script>` tag 一定要成對（`<script>...</script>`）
- ✅ 唔好用 self-closing `<script src="..." />`（HTML5 唔支援）
- ✅ 用 HTML validator 檢查

---

### B003 — Generator 頁面 Document Preview Image 係 Webpage Screenshot

**發現日期：** 2026-07-07
**影響範圍：** `deregistration-checklist-generator`（`dereg-checklist-template.png`）

**症狀：**
- 「可修改文件」預覽圖顯示嘅係 ESGov 網站嘅 webpage screenshot
- 應該顯示 checklist document form 嘅截圖

**原因：**
- 之前用 browser screenshot 時 capture 咗成個 page（包括 navbar、button 等），而唔係淨係個 form

**修復方法：**
- 用 `html2canvas` capture 淨係個 form element
```javascript
html2canvas(formElement, { scale: 2, backgroundColor: '#ffffff' })
  .then(canvas => { /* save as PNG */ });
```

**預防措施：**
- ✅ Document preview 圖片應該只顯示 document 內容，唔包含網站 UI
- ✅ 用 `html2canvas` 或類似工具 capture 特定 element，唔係成個 page

---

## SEO / Meta Bugs

### B004 — Twitter Card 同 OG Tags 冇更新

**發現日期：** 2026-07-06
**影響範圍：** `shareholder-transfer/index.html`

**症狀：**
- `<title>` 同 meta description 已更新
- 但 Twitter Card 嘅 `twitter:title` / `twitter:description` 仲係舊 content
- `og:title` / `og:description` 亦冇同步更新

**原因：**
- 做 title/meta 更新時漏咗同步更新 social meta tags

**修復方法：**
- 每次改 `<title>` 同步改：
  - `twitter:title`
  - `twitter:description`
  - `og:title`
  - `og:description`

**預防措施：**
- ✅ 每次更新 title/description，檢查晒所有相關 meta tags
- ✅ 4 個位要同步：`<title>` → `meta description` → `og:title/description` → `twitter:title/description`
- ✅ Article Schema 嘅 `headline` / `description` 都要同步

---

### B005 — Duplicate `og:title` Meta Tag

**發現日期：** 2026-07-06
**影響範圍：** `blog/公司秘書辭任更換指南/index.html`

**症狀：**
- HTML `<head>` 入面有兩個 `og:title` meta tag
- Second one 係舊嘅未 delete

**原因：**
- Patch 嘅時候加入咗新 `og:title`，但冇刪除舊嗰個

**修復方法：**
- 人手刪除 duplicate `<meta property="og:title">`

**預防措施：**
- ✅ 每次 patch HTML head section，檢查有冇殘留嘅 duplicate tags
- ✅ 可以用 `grep -c 'property="og:title"'` 檢查

---

## Git / Deploy Bugs

### B006 — GitHub Pages Build Failure（Infrastructure）

**發現日期：** 2026-07-06
**影響範圍：** 所有 deploy

**症狀：**
- GitHub Actions build 喺 `syncing_files` / `deploy_to_pages` 階段 fail
- Error message：「Deployment failed, try again later」
- Re-run 或者 empty commit 可以解決

**原因：**
- GitHub Pages infrastructure issue（2026-07-02 都有同樣嘅 Pages incident）
- 唔係 code 問題

**修復方法：**
- Re-run build（`gh run rerun`）
- 或者推 empty commit（`git commit --allow-empty -m "retry" && git push`）

**預防措施：**
- ✅ Build fail 嘅時候先 check GitHub Status（https://www.githubstatus.com/）
- ✅ 如果係 infrastructure issue，簡單 retry 就得
- ✅ 唔好改 code 去「fix」唔係 code 嘅問題

---

## Content Bugs

### B007 — Blog 回數.html 變數顯示問題

**發現日期：** 2026-06-??（之前 session）
**影響範圍：** 部分 blog pages

**症狀：**
- 頁面顯示 `回數` 而不是正確嘅 number
- Liquid template variable 冇正確 render

**原因：**
- Jekyll 嘅 `{% raw %}` / `{% endraw %}` 處理問題

**修復方法：**
- 用 `{: }` 或者 HTML entity 代替

---

## Checklist（新 Page 或修改時必 check）

- [ ] `<script>` tag 有成對 `</script>`？
- [ ] HTML 冇意外嘅 line number prefixes？
- [ ] `<title>` 同以下 4 個位同步？
  - `meta name="description"`
  - `meta property="og:title"`
  - `meta property="og:description"`
  - `meta name="twitter:title"` + `twitter:description`
- [ ] Article Schema 嘅 `headline` / `description` 同步？
- [ ] 冇 duplicate meta tags？
- [ ] Document preview images 係純 document（唔係 webpage）？
- [ ] Tailwind classes 全部正確（`bg-navy`、`bg-gold` 等）？
- [ ] Build 成功？（Check GitHub Actions）

---

> 發現新 bug 時請更新呢份 document 🙏
