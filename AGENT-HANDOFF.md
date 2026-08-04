# ESGov — Agent Handoff Document

> 上一手 Agent：Hermes (DeepSeek V4 Flash via OpenCode Go)
> 日期：2026-08-04（更新）
> 用途：下一手 Agent 可以直接跟呢份文件嚟做嘢，唔使重新摸索

---

## 1. Project Overview

| Item | Value |
|------|-------|
| Site | https://esgov.org |
| Source | `/mnt/c/Users/hongk/Desktop/esgov/` |
| Blog | `/home/hongk/blog-repo/` (Jekyll, 1341 posts) |
| Stack | Vanilla HTML + Tailwind CSS (CDN) + Alpine.js (CDN) |
| Hosting | GitHub Pages + **Cloudflare (Proxied)** |
| Theme | Navy `#1B2A4A`, Gold `#C9A84C` |
| Auth | Google OAuth (webmasters write scope) + Cloudflare Global API Key |

### Cloudflare Access (2026-08-04 added)
- **Zone**: esgov.org — zone ID `e36d8aa7f072c1ff42043511ed0750a6`
- **Account ID**: `312d4e1b3786fdc7396c57a9b5afb2c5`
- **Auth**: Global API Key (NOT bearer token) via headers `X-Auth-Email: tbstbs0613@gmail.com` + `X-Auth-Key: cfk_...`
- **Saved in**: `~/.hermes/profiles/esgov-builder/.env` (CLOUDFLARE_API_KEY / CLOUDFLARE_EMAIL / CLOUDFLARE_ZONE_ID)
- **DNS**: apex + www both **Proxied (orange cloud)** — SSL/TLS mode = Full (strict)
- **Redirects**: `.html` blog URLs → pretty URLs (see section 12)

## 2. Current State (2026-08-04)

### ✅ Working
- **Static icons**: 44-88 `<i data-lucide>` tags on main pages; 17 icons on all **19 generator pages**
- **Step NAV icons**: `STEP_ICONS` global variable + `x-html` — **proven working** on all 6 product pages
- **Document card buttons**: 🚀 👁️ 📎 replaced with Lucide on all product pages
- **Step content**: Renders correctly from processes.json (shareholder-transfer, SCR) or embedded data
- **Interactive tool cards**: All demo images, template links, and generator buttons display correctly
- **SEO score**: **100/100** (deep-seo-audit.py — 21 pages incl. top 10 blogs)
- **GSC**: Token with webmasters write scope, sitemap submitted (204) — **auto-refresh before query** (access token expires hourly; refresh token still valid)
- **GEO**: robots.txt (491 bytes) + llms.txt (standard markdown links) both present
- **AEO**: FAQPage + HowTo + Article + Speakable on all product pages (director HowTo added 2026-08-04)
- **Canonicals**: All 95 blog canonical tags → trailing-slash (2026-08-04, fixed cannibalization)
- **Sitemap**: 128 URLs, 0 `.html`, 0 test URLs (test-share-transfer removed)
- **Cloudflare Proxied**: apex + www, Full (strict) SSL, 18/18 `.html` → true 301 redirects
- **Cron jobs**: SEO Report 09:00 + 17:15 (detailed, auto-refresh GSC token)

### ❌ Known Issues
- **Step details emoji**: Embedded-data pages (company-name-change, deregistration, director, share-transfer) have step DETAILS with emoji instead of Lucide icons. This is INTENTIONAL — HTML tags inside x-data single-quoted strings break Alpine.js. Only NAV icons and doc card buttons are replaceable on these pages.
- **processes.json pages (shareholder-transfer, SCR)**: Step details DO have Lucide icons (replaced in processes.json). Some emoji remain in the detail text if they were NOT in the processes.json file (e.g., inline generator pages).
- **OpenCode Go Vision**: API returns 403 (subscription expired). Cannot do Vision AI image analysis. Use Playwright `page.evaluate()` for icon counting instead.
- **Cloudflare cache**: PROXIED — cache can hold old content up to 1hr+. **Always purge cache via API after deploy** (see section 7). Do NOT rely on waiting.
- **Remaining 8 low-traffic `.html` stubs**: still exist as files (meta-refresh) — harmless because Cloudflare 301 now fires first. Can delete files later if desired.

## 3. Icon Replacement — The Only Safe Way

### NEVER Do These (they crashed the site repeatedly)
1. ❌ Put HTML with `"` inside `x-data="..."` attributes — terminates the body tag, renders JS as visible text
2. ❌ Put HTML with unescaped `'` inside single-quoted JS strings in x-data — breaks Alpine.js parsing
3. ❌ Use post-render emoji scanners (TreeWalker) — emoji chars cause JS syntax errors
4. ❌ Put helper functions (formatDetails) inside x-data — "Invalid or unexpected token"
5. ❌ Use `patch` tool for changes inside x-data — escapes quotes wrong, introduces `\\n` literal bytes

### ✅ Safe Approach

#### A. Static Icons (pages / static HTML)
```html
<i data-lucide="icon-name" class="w-4 h-4 inline-block"></i>
<script defer src="https://unpkg.com/lucide@latest"></script>
<script>document.addEventListener("DOMContentLoaded",function(){lucide.createIcons()});</script>
```

#### B. Step NAV Icons (Alpine.js dynamic)
```html
<!-- GLOBAL variable — NOT inside x-data -->
<script>const STEP_ICONS={
  hasDocs:'<i data-lucide="file-text" class="w-5 h-5 inline-block"></i>',
  noDocs:'<i data-lucide="footprints" class="w-5 h-5 inline-block"></i>'
};</script>

<!-- x-data references the global -->
<body x-data="{
  getStepIcon(step) {
    return step.documents && step.documents.length > 0 ? STEP_ICONS.hasDocs : STEP_ICONS.noDocs;
  },
}">

<!-- Use x-html, NOT x-text -->
<span x-html="getStepIcon(s)"></span>
```

In `init()`, add retry loop for late Alpine.js renders:
```javascript
var _i=0;var _t=setInterval(function(){
  if(typeof lucide!=='undefined'){try{lucide.createIcons()}catch(e){}}
  _i++;if(_i>10){clearInterval(_t)}
},500);
```

#### C. Step Content (processes.json pages: shareholder-transfer, SCR)
1. Edit processes.json: replace emoji with `<i data-lucide='icon-name'>` (SINGLE quotes)
2. Change `x-text="s.details"` to `x-html="s.details"`
3. JSON uses `"` delimiters, so HTML attributes MUST use `'`

#### D. Step Content (embedded-data pages: company-name-change, deregistration, director, share-transfer)
⚠️ **These pages have step details INLINE in the x-data** (e.g. `details: '第一步：...'`).
HTML tags with quotes CANNOT be safely used here because the outer string delimiter is `'` and the x-data attribute delimiter is `"`. Any HTML tag will break one of these delimiters.

**Keep emoji as-is for step details on these pages.** Only replace static icons and step NAV icons.

## 4. Pre-Deploy Checklist

Run ALL of these before pushing any icon/JS change:

```bash
# 1. x-data brace balance
grep -o '{' file.html | wc -l
grep -o '}' file.html | wc -l
# diff should be 1 (body tag >)

# 2. openDoc(doc) corruption
grep -n 'get steps()' file.html
# 1 match only = good
# 2+ = openDoc(doc) got corrupted

# 3. \\'undefined\\' byte corruption
python3 -c "
with open('file.html','rb') as f: d=f.read()
c=d.count(b\"\\\\'\")
if c>0: print(f'WARNING: {c} backslash-quote sequences')
"

# 4. literal \\n in JS
sed -n '238,250p' file.html | cat -A | grep -E '\\\\\\\\n|\\\\\\\\$'

# 5. Icon name validation
python3 << 'PYEOF'
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    icons_to_test = ['dumbbell', 'moon', 'vote', 'smile']
    page.set_content('<html><body>' + ''.join(f'<i data-lucide=\"{n}\"></i>' for n in icons_to_test) + '<script src=\"https://unpkg.com/lucide@latest\"></script><script>lucide.createIcons()</script></body></html>')
    import time; time.sleep(2)
    bad = page.evaluate('Array.from(document.querySelectorAll(\"i[data-lucide]\")).map(e => e.getAttribute(\"data-lucide\"))')
    if bad: print(f'INVALID: {bad}')
    else: print('All valid')
    browser.close()
PYEOF
```

## 5. Recovery Procedure (Site Broken)

### Symptom: JavaScript code visible at top of page, Alpine.js fails
This means the `x-data` attribute on the `<body>` tag was terminated early by an unescaped `"`.

### Quick fix:
```bash
# Revert last commit
git revert --no-edit HEAD
git push origin main

# If reverts conflict:
git checkout <clean-hash> -- <broken-file>
git add -A
git commit -m "Revert: restore <file> to clean state"
git push origin main
```

### Know clean base commits:
- `1fb917e` — Original clean state (emoji icons, no Lucide)
- `5458021` — Clean state with STEP_ICONS + static Lucide icons (safe)

### Recovery steps:
1. `git checkout 1fb917e -- file.html` (original clean)
2. Add Lucide CDN
3. Add STEP_ICONS global
4. Change x-text→x-html for step icons
5. Add setInterval lucide init
6. **Do NOT** add: formatDetails, scanner scripts, inline HTML in x-data

## 6. Common Patch-Tool Bugs

### Bug 1: `\\'undefined\\'` corruption
**Symptom:** Alpine.js "Invalid or unexpected token"
**Cause:** patch tool introduces `\\\\'` (double backslash) instead of `'` (single quote)
**Detection:** `grep -n "'undefined'" file.html` — should show `!=='undefined'`
**Fix:**
```python
with open('file.html', 'rb') as f: data = f.read()
data = data.replace(b"!==\\\\'undefined\\\\'", b"!=='undefined'")
with open('file.html', 'wb') as f: f.write(data)
```

### Bug 2: `\\n` literal newlines
**Symptom:** JavaScript syntax error, broken braces
**Cause:** patch tool writes `\\\\n` (0x5C 0x6E) instead of real newline
**Detection:** `sed -n '240,245p' file.html | cat -A` — look for literal `\\n`
**Fix:**
```python
with open('file.html', 'rb') as f: data = f.read()
data = data.replace(b'\\\\n', b'\\n')
with open('file.html', 'wb') as f: f.write(data)
```

### Bug 3: `openDoc(doc)` → `get steps()` corruption
**Symptom:** Alpine.js reports "init is not defined"
**Cause:** patch tool matches wrong `get steps()` occurrence and renames openDoc
**Detection:** `grep -n 'get steps()' file.html` — should be 1 match, not 2+
**Fix:**
```bash
sed -i 's/^  get steps()$/  openDoc(doc) {/' file.html
```

### Bug 4: Unescaped single quotes in x-data strings
**Symptom:** "Unexpected identifier 'xxx'" in console, Alpine.js partially works
**Cause:** `<i data-lucide='xxx'>` inside single-quoted JS string `'...<i data-lucide='xxx'...>'` — the `'xxx'` closes the outer string
**Context:** Step DETAILS on embedded-data pages use single-quoted strings in x-data
**Fix:** Remove the `<i data-lucide>` tags from these strings entirely, keep emoji

## 7. Cache Layers (VERIFY DEPLOY CORRECTLY)

| Layer | What | Duration | Verify with |
|-------|------|----------|-------------|
| raw.githubusercontent.com | GitHub raw CDN | sec-min | `curl "https://raw.githubusercontent.com/..."` |
| Cloudflare CDN | Live site (PROXIED since 2026-08-04) | **up to 1hr+** | `curl -s https://esgov.org/page/` |
| Browserbase proxy | Browser tool | 5-10 min | **curl only** — ignore browser tool snapshot |

**⚠️ Since Cloudflare Proxied (2026-08-04):**
- Cache can hold old content for **up to 1 hour+** (worse than the old 10-min GitHub cache)
- After deploy, **PURGE CACHE immediately** via API:
  ```bash
  curl -s -X POST "https://api.cloudflare.com/client/v4/zones/e36d8aa7f072c1ff42043511ed0750a6/purge_cache" \
    -H "X-Auth-Email: tbstbs0613@gmail.com" -H "X-Auth-Key: <CLOUDFLARE_API_KEY>" \
    -H "Content-Type: application/json" -d '{"purge_everything":true}'
  ```
- Verify proxy is active: `curl -sI https://esgov.org/ | grep -i 'server\|cf-ray'` → should show `server: cloudflare` + `cf-ray`

**Debugging order:**
1. `curl -s "https://raw.githubusercontent.com/hongkpng855-lang/govflow/main/path" | grep -c 'marker'`
2. `curl -s https://esgov.org/page/ | grep -c 'marker'`
3. ONLY THEN use browser tool (which has its own cache)

The browser tool's accessibility tree often shows stale/garbled content even when curl confirms the site is correct. **Do NOT diagnose from browser tool snapshot alone.**

## 8. GSC Token Management

| Item | Path |
|------|------|
| Token (main) | `~/.hermes/google_token.json` |
| Token (profile) | `~/.hermes/profiles/esgov-builder/google_token.json` |
| Client secret | `~/.hermes/google_client_secret.json` |

### Token refresh:
```bash
# Generate auth URL
python3 ~/.hermes/profiles/esgov-builder/skills/productivity/google-workspace/scripts/setup.py --auth-url

# Exchange code (user sends redirect URL)
python3 ~/.hermes/profiles/esgov-builder/skills/productivity/google-workspace/scripts/setup.py --auth-code "URL_OR_CODE"
```

**Important:** For webmasters write scope (sitemap submission), generate a URL with ONLY webmasters scope:
```python
params = {
    'response_type': 'code',
    'client_id': '401623198560-1onfqcgs8lioo4ju7amtvlhapg73n562.apps.googleusercontent.com',
    'redirect_uri': 'http://localhost:1',
    'scope': 'https://www.googleapis.com/auth/webmasters',
    'access_type': 'offline',
    'prompt': 'consent'
}
```

Save token to **BOTH** locations after renewal.

## 9. Product Pages

| Product | Path | Data source | Generators | Icons |
|---------|------|-------------|------------|:-----:|
| Share Transfer | `/shareholder-transfer/` | processes.json ✅ | Sold Note, Instrument of Transfer, Letter, etc. | ✅ 74 |
| Company Name | `/company-name-change/` | embedded ⚠️ | NNC2 PDF, Special Resolution PDF | ✅ 83 |
| SCR | `/significant-controllers-register/` | processes.json ✅ | SCR Form, Data Collection, NR2, etc. | ✅ 35 |
| Deregistration | `/deregistration/` | embedded ⚠️ | Dereg Checklist, IR1263, IRC3113, NDR1 | ✅ 37 |
| Director Details | `/director-particulars-change/` | embedded ⚠️ | ND2B Generator (pending) | ✅ 54 |
| Share Transfer (old) | `/share-transfer/` | embedded ⚠️ | — | ✅ 28 |

⚠️ **embedded** = step details are INLINE in the x-data attribute. HTML icons in step DETAILS cannot be used here. Only NAV icons and doc card buttons are replaceable.

## 10. Quick Commands

```bash
# Deploy
git add -A && git commit -m "..." && git push origin main

# Verify site clean
curl -s https://esgov.org/page/ | grep -c "'; }, goToStep"  # 0 = clean

# Verify icons
curl -s https://esgov.org/page/ | grep -c 'data-lucide='

# Playwright rendered check
python3 << 'PYEOF'
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('https://esgov.org/page/', timeout=10000)
    page.wait_for_timeout(5000)
    lucide = page.evaluate('document.querySelectorAll("[data-lucide]").length')
    emoji = page.evaluate('[...document.body.innerText].filter(c => c.codePointAt(0) > 0x1F300 && c.codePointAt(0) < 0x1FA00 && c !== "\\uD83D\\uDCC5").length')
    print(f"Lucide: {lucide}, Emoji: {emoji}")
    browser.close()
PYEOF

# Deep SEO audit
cd /mnt/c/Users/hongk/Desktop/esgov && python3 scripts/deep-seo-audit.py

# GSC query
python3 -c "
import json, urllib.request
tok = json.load(open('/home/hongk/.hermes/google_token.json'))
req = urllib.request.Request('https://www.googleapis.com/webmasters/v3/sites/sc-domain:esgov.org/searchAnalytics/query',
    data=json.dumps({'startDate':'2026-06-29','endDate':'2026-07-29','dimensions':['query'],'rowLimit':10}).encode(),
    headers={'Authorization': f'Bearer {tok[\"token\"]}', 'Content-Type': 'application/json'})
r = json.loads(urllib.request.urlopen(req).read().decode())
for row in r.get('rows',[]): print(f\"{row['keys'][0][:40]:40s} C:{row.get('clicks',0)} I:{row.get('impressions',0)}\")
"
```

## 11. Known Invalid Lucide Icon Names

| Invalid Name | Use Instead | Original Emoji |
|-------------|-------------|----------------|
| `muscle` | `dumbbell` | 💪 |
| `sleep` | `moon` | 😴 |

**Always validate icon names before bulk deploy** (see checklist #5).

## 12. Comparison Table Colored Dots

The comparison tables (自己搞 vs 會計公司 vs 秘書公司) use 🟢🟡🔴 as SEMANTIC indicators.
**DO NOT** replace them with `<i data-lucide='circle'>` — the color IS the meaning.
A generic circle creates blank gaps that look broken.

## 13. Cloudflare Redirects (.html → pretty URLs)

### Setup (2026-08-04)
All 18 legacy `.html` blog URLs now 301-redirect to pretty URLs via Cloudflare:

| Method | What | Limit |
|--------|------|-------|
| Dynamic Redirect Rules (10 rules) | Top 10 `.html` URLs by impressions | 10 rules/phase (free) |
| Page Rules (1 rule, wildcard) | `*esgov.org/blog/*.html` → `https://esgov.org/blog/$1/` | 3 page rules (free) |

**Result: 18/18 `.html` URLs return true 301** ✅

### Page Rule (the one that matters)
```
Pattern: *esgov.org/blog/*.html
Action: Forwarding URL, 301, https://esgov.org/blog/$1/
```

### ⚠️ Cloudflare API Bugs/Lessons (2026-08-04)
1. **`regex_replace` in target_url requires Business/WAF plan** — on Free plan, use static `value` targets instead of dynamic expressions. Error: `not entitled: the use of function regex_replace is not allowed, a Business plan or a WAF Advanced plan is required`
2. **Dynamic Redirect Rules phase limit = 10 rules** on Free plan (error: `exceeded the maximum number of rules in the phase`)
3. **Cloudflare matches URL-encoded paths** — `http.request.uri.path` returns PERCENT-ENCODED paths for non-ASCII URLs. An expression with raw Chinese characters (`eq "/blog/香港公司..."`) will NOT match. Must use `urllib.parse.quote()`:
   ```
   eq "/blog/%E9%A6%99%E6%B8%AF..."  ← correct
   eq "/blog/香港公司..."            ← won't match
   ```
4. **POST create ruleset → rules may show 0** — after POST, verify rules count; if 0, re-PUT with `{"rules": [...]}`. GET by phase (`/rulesets/phase/...`) may return not_found — use `/rulesets/<id>` instead.
5. **Bulk Redirect Lists (rules/lists)** — list creation works, but **adding items fails with `filters.api.invalid_json`** on this account. Worked around with Page Rules instead.
6. **Global API Key ≠ API Token** — Global key uses `X-Auth-Email` + `X-Auth-Key` headers, NOT `Authorization: Bearer`. Token-format keys start with `cfk_` but need email+key headers.
7. **List/rule names can't contain hyphens or spaces?** — `invalid_name` error; use lowercase alphanumeric names.
8. **Cache purge after changes** — after any Cloudflare redirect/rule change, `purge_everything` to clear stale 200s, else old status lingers up to 1hr.

### Verification commands
```bash
# Check a redirect works (should be 301 + location)
curl -sI "https://esgov.org/blog/香港公司股份轉讓流程2026.html" | grep -i 'HTTP\|location'
# URL-encode the Chinese path segment first:
python3 -c "import urllib.parse; print(urllib.parse.quote('香港公司股份轉讓流程2026'))"
```

---

*End of handoff document. Last updated: 2026-08-04*
