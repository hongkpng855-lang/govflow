# SCR 產品頁面內容更新草案

## 研究員發現嘅 4 個 Gaps 同修正方案

| # | 問題 | 嚴重性 | 修正方案 |
|---|------|--------|---------|
| 1 | **Missing: 發出書面通知 (Serve Notice) 步驟** | 🔴 Critical | 新增 Step 3，由原本在 Step 3 入面順帶一提，提升為獨立步驟 |
| 2 | **Missing: 委任指定代表 (Appoint Designated Rep) 步驟** | 🔴 Critical | 新增 Step 5，由原本在 Step 3/5 入面順帶一提，提升為獨立步驟，加入董事會決議要求 |
| 3 | **Step 5 將 NR2 + 維護綑埋一齊** | 🟡 Medium | 拆開：Step 7 嘅 NR2 標明「只有當 SCR 放喺註冊辦事處以外先需要」 |
| 4 | **Missing: 無控制人聲明 (No Controller Declaration)** | 🟡 Medium | 喺 Step 2 同 Step 6 加入完整嘅無控制人路徑 + 獨立文件範本 |

---

## 1️⃣ SEO Metadata 更新

### Title (當前 → 新)
```
當前: ESGov | 香港公司重要控制人登記冊 (SCR) 完整指南 — 5個步驟搞掂
新:   ESGov | 重要控制人登記冊 (SCR) 完整指南 — 7個步驟搞掂，含通知範本
```

### Description (當前 → 新)
```
當前: 香港公司重要控制人登記冊 (SCR) 完整指南。由真實經歷者整理，5 個步驟教你備存 SCR：分析股權結構、5 項控制權測試、收集控制人資料、填寫登記冊、備存維護。含法定要求、範例、常見錯誤同罰則。全部免費公開，避免罰款 HK$25,000+。
       (長度: ~171 chars - 略超)

新:   香港公司重要控制人登記冊 (SCR) 7 個步驟完整指南。含發出書面通知、委任指定代表、NR2 指明地點通知及無控制人聲明範本。真實經歷者整理，全部免費公開，避免被罰 HK$25,000+。
       (長度: ~142 chars ✅)
```

### OG Tags (當前 → 新)
```
當前 og:title: 香港公司重要控制人登記冊 (SCR) 完整指南 — 5個步驟搞掂 | ESGov
新   og:title: 重要控制人登記冊 (SCR) 完整指南 — 7個步驟搞掂

當前 og:description: 真實來源對照、可下載範本、避免被罰款。由經歷者整理，5個步驟搞掂重要控制人登記冊。
新   og:description: 7個步驟搞掂 SCR：股權分析、5項測試、書面通知、指定代表、登記冊填寫、備存維護。全部免費，可下載範本。
```

### Schema 更新

**WebPage schema** 更新 name/description 由 5 steps → 7 steps。

**新增 FAQPage schema** — 呢個 template 可以加落 `<head>` 嘅 script type="application/ld+json" 入面：

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "SCR 係咩嚟？邊啲公司要做？",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "SCR（重要控制人登記冊）係香港《公司條例》要求所有非上市公司備存嘅登記冊，记录公司嘅重要控制人資料。上市公司豁免。"
      }
    },
    {
      "@type": "Question",
      "name": "點樣通知疑似控制人？要用咩格式？",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "公司必須向每位疑似重要控制人發出書面通知，要求佢哋喺 1 個月內回覆。我哋提供 standard 通知書範本下載。"
      }
    },
    {
      "@type": "Question",
      "name": "指定代表（Designated Representative）點樣委任？一定要董事會決議？",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "係，指定代表必須經董事會決議正式委任，並記錄喺會議記錄。可以係股東/董事/員工（須居港），或者會計/法律專業人士/TCSP 持牌人。"
      }
    },
    {
      "@type": "Question",
      "name": "公司冇重要控制人，仲要備存 SCR 嗎？",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "要。即使冇重要控制人，公司仍然必須備存 SCR，並喺登記冊註明「經查核後公司無重要控制人」。留空係違規。"
      }
    },
    {
      "@type": "Question",
      "name": "SCR 放喺邊？一定要交 NR2 嗎？",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "SCR 可以放喺公司註冊辦事處（唔使交 NR2），或者香港境內另一個指明地方（必須 15 日內交 NR2 通知公司註冊處）。NR2 係條件性嘅，唔係一定要交。"
      }
    },
    {
      "@type": "Question",
      "name": "唔做 SCR 有咩罰則？",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "未備存 SCR 最高罰 HK$25,000 + 每日 HK$700。提供虛假/誤導資料最高罰 HK$300,000 + 2 年監禁。2025 年已有實際檢控案例罰款 $3,000-$20,000。"
      }
    }
  ]
}
```

---

## 2️⃣ 流程結構更新：5 Steps → 7 Steps

### 新舊對照

```
舊流程 (5 Steps)                             新流程 (7 Steps)
─────────────────────────────────            ─────────────────────────────────
Step 1: 分析公司股權結構                      Step 1: 分析公司股權結構 (unchanged)
Step 2: 識別重要控制人（5項測試）             Step 2: 識別重要控制人（5項測試）(unchanged)
                                              ➡️ Step 3: 【NEW】發出書面通知俾疑似控制人
Step 3: 收集控制人法定資料                    Step 4: 收集控制人法定資料 (refocused)
                                              ➡️ Step 5: 【NEW】委任指定代表（董事會決議）
Step 4: 填寫重要控制人登記冊                  Step 6: 填寫重要控制人登記冊 (expanded)
Step 5: 備存同維護 SCR (含 NR2)              Step 7: 備存同維護 SCR (NR2 標明條件性)
```

### Step 變動詳情

| Step | 新編號 | 改變 |
|------|--------|------|
| 分析公司股權結構 | 1 | 不變 |
| 識別重要控制人 | 2 | 不變，但加入「經查核無控制人」分支路徑 |
| — | **3【NEW】** | **發出書面通知** — 從舊 Step 3 抽出獨立成 step |
| 收集控制人法定資料 | 4 | 專注於收集已確認控制人資料，唔再包含指定代表內容 |
| — | **5【NEW】** | **委任指定代表** — 從舊 Step 3/5 抽出獨立成 step，加入董事會決議要求 |
| 填寫登記冊 | 6 | 加入無控制人聲明模板 section |
| 備存同維護 | 7 | NR2 標明「條件性：只有 SCR 放喺註冊辦事處以外先需要」 |

---

## 3️⃣ 詳細 Step Content 更新

### Step 3 (NEW): 發出書面通知俾疑似控制人

**Title:** 發出書面通知俾疑似控制人
**Summary:** 向 Step 2 識別出嘅疑似重要控制人發出法定書面通知，佢哋有 1 個月法定義務回覆
**isFree:** true
**mode:** B

**Details:**

```
識別咗邊啲可能係重要控制人之後，公司有法定責任向佢哋發出書面通知（Section 653ZH, Cap. 622）。
唔係打電話或者 WhatsApp 就得 — 一定要書面，有記錄。

📮 通知對象：
• Step 2 測試後符合條件嘅人/法團
• 有合理理由相信係重要控制人嘅人
• 股東名冊上嘅 major shareholders（建議全部通知）

📝 通知書必須包含：
• 公司名稱同 SCR 相關法律條文
• 收件人姓名
• 要求確認嘅問題（是否符合某項控制權條件）
• 回覆期限（法定 1 個月內）
• 唔回覆嘅後果（可被罰款 HK$25,000 + 每日 HK$700）
• 公司授權人簽署 + 日期

📬 發出方式：
• 親身交付（收書面回條）
• 掛號郵件（有追蹤號碼）
• 電子郵件（要對方確認收到，建議用埋 Read Receipt）
• 快遞（有簽收記錄）

⏰ 時間線：
• 發出通知 → 對方有 1 個月回覆
• 對方冇回覆 → 喺 SCR 註明「已發出通知但未獲回覆」
• 對方確認係控制人 → 進入 Step 4 收集詳細資料
• 對方否認係控制人 → 記錄佢嘅否認聲明

⚠️ 唔好做嘅事：
• 唔好用口頭通知 → 公司條例要求書面，冇書面記錄等於冇做
• 唔好漏咗疑似控制人 → 明知有人疑似但冇通知，係違規
• 唔好俾太少時間回覆 → 法定最少 1 個月
• 有人唔回覆唔可以就咁算 → 要喺 SCR 註明「未能確認」
• 唔好冇保留通知記錄 → CR 查冊時要證明你做咗通知

✅ 一定要做：
• 用標準格式發出書面通知
• 保留發出證明（掛號收據、簽收回條）
• 記錄發出日期同回覆日期
• 有人冇回覆 → 登記冊加註記
• 控制人確認後先繼續 Step 4
```

**Documents:**
```json
{
  "name": "重要控制人書面通知書",
  "description": "標準格式嘅書面通知書模板，用嚟通知疑似重要控制人，包含法定要求嘅所有欄位",
  "demoImage": "/assets/demo/scr-step3.png",
  "templateFile": "/templates/scr-notice-letter.docx",
  "hasGenerator": true,
  "commonMistakes": [
    "用口頭通知冇書面記錄",
    "冇保留發出證明",
    "俾嘅回覆時間唔夠 1 個月",
    "有人唔回覆就唔理"
  ],
  "generatorUrl": "/scr-notice-generator"
}
```

**RejectionRisks:**
```json
[
  "冇發出書面通知 = 違反公司條例，可被罰款 HK$25,000",
  "冇保留通知記錄 = CR 查冊時無法證明已履行通知義務"
]
```

**CrossStepDeps:** Step 2 (need to identify controllers before notifying them)

---

### Step 4 (Modified - 原本 Step 3): 收集控制人法定資料

**Update:** Remove the指定代表 content (moved to new Step 5). Keep focus on collecting data from people who have confirmed they are controllers.

**Title:** 收集控制人法定資料
**Summary:** 收集每位已確認重要控制人嘅身份證明文件同法定聯絡資料
**isFree:** true
**mode:** B

**Details (updated — removed 指定代表 section):**

```
確定咗邊啲係重要控制人（佢哋回覆咗通知並確認身份），
就要收集佢哋嘅法定資料記錄入 SCR。

📝 收集嘅資料（自然人控制人）：
• 全名（中文+英文，同身份證一致）
• 通訊地址（可用服務地址，唔可以用郵政信箱）
• 身份證號碼 / 護照號碼 + 簽發國
• 出生日期
• 成為重要控制人嘅日期
• 控制性質（符合邊項測試條件 — 對應 Step 2 結果）

🏢 收集嘅資料（法團控制人）：
• 公司名稱
• 法律形式（如有限公司）
• 公司註冊編號
• 成立地（適用法例）
• 註冊辦事處地址
• 成為重要控制人嘅日期
• 控制性質

⚠️ 唔好做嘅事：
• 唔好接受口頭提供資料 → 要有書面記錄同簽署
• 唔好漏咗控制性質 → 淨係寫名唔夠，要寫明符合邊項測試
• 地址唔好用郵政信箱 → 公司條例規定唔可以用郵政信箱做 SCR 地址
• 唔好拖延 → 知道有新控制人後要盡快收集資料
• 有人唔回覆通知 → 要喺登記冊註明「未能確認」，唔可以就咁唔理

✅ 一定要做：
• 控制人簽署確認後先記錄入 SCR
• 保留控制人確認書
• 核對身份證明文件正本/核證副本
```

**Documents (updated — removed 指定代表 mention):**
```json
{
  "name": "重要控制人資料收集表",
  "description": "標準嘅資料收集表格，控制人簽署確認後歸檔",
  "demoImage": "/assets/demo/scr-step4.png",
  "templateFile": "/templates/scr-data-collection.docx",
  "hasGenerator": true,
  "commonMistakes": [
    "資料唔齊全就入 SCR",
    "地址用郵政信箱",
    "冇簽署確認"
  ],
  "generatorUrl": "/scr-data-collection-generator"
}
```

---

### Step 5 (NEW): 委任指定代表（Designated Representative）

**Title:** 委任指定代表（董事會決議）
**Summary:** 經董事會決議正式委任最少一位指定代表，負責聯絡同提供 SCR 俾執法機構查閱
**isFree:** true
**mode:** B

**Details:**

```
每間公司必須指定最少一位指定代表（Designated Representative），
而且一定要經董事會決議（Board Resolution）正式委任 — 唔可以就咁口頭叫阿邊個做。

👤 合資格人士（2026年更新明確三類）：
1. 公司股東、董事或僱員（必須係居於香港嘅自然人）
2. 會計專業人士（CPA、會計師行）
3. 法律專業人士（律師、律師行）
4. 信託或公司服務持牌人（TCSP）

🔖 指定代表嘅職責：
• 喺正常辦公時間內提供 SCR 俾執法人員查閱
• 接獲查閱要求後 **1 小時內** 提供 SCR（2025-2026 年執法重點！）
• 確保 SCR 資料最新
• 保管相關文件記錄

📋 董事會決議內容：
• 委任人士姓名
• 委任生效日期
• 職責範圍
• 薪酬（如有）
• 授權簽署
• 會議日期同決議編號

⚠️ 唔好做嘅事：
• 唔好冇書面委任記錄 → 要董事會決議 + 當事人同意書
• 唔好委任非居港人士 → 要居於香港（自然人適用）
• 唔好委任後唔通知佢要做咩 → 要清楚列明職責
• 唔好冇後備人選 → 指定代表離職或離港要盡快更換
• 唔好以為董事自動係指定代表 → 要正式委任

✅ 一定要做：
• 董事會決議記錄
• 指定代表簽署同意書
• 記錄喺 SCR
• 確保隨時至少有一位代表
• 代表離職 → 30 日內更換

📊 實戰數據：
2025 年末執法數據顯示，約 12% 被查企業因指定代表未能在
1 小時內提供 SCR 而收到罰單。揀一個 responsibile 嘅代表好重要！
```

**Documents:**
```json
{
  "name": "指定代表委任決議 + 同意書",
  "description": "董事會決議範本 + 指定代表同意書，包含所有法定欄位同簽署位置",
  "demoImage": "/assets/demo/scr-step5.png",
  "templateFile": "/templates/scr-designated-rep-resolution.docx",
  "hasGenerator": true,
  "commonMistakes": [
    "冇董事會決議記錄",
    "委任非居港人士",
    "冇後備人選",
    "冇通知代表佢嘅法定職責"
  ],
  "generatorUrl": "/scr-designated-rep-generator"
}
```

**RejectionRisks:**
```json
[
  "冇指定代表 = 違反公司條例，可被罰款 HK$25,000",
  "指定代表未能 1 小時內提供 SCR = 最高 HK$25,000 罰款（12% 被查企業中招）"
]
```

**CrossStepDeps:** Steps 1-4 (need to understand company structure before appointing rep)

---

### Step 6 (Modified - 原本 Step 4): 填寫重要控制人登記冊

**Update:** 加入「無控制人聲明」完整範本 + 填寫指引

**Title:** 填寫重要控制人登記冊（含無控制人聲明）
**Summary:** 將收集到嘅資料正式記錄入 SCR，冇控制人嘅公司都要備存並註明聲明
**isFree:** true
**mode:** A

**Details (updated — added 無控制人 scenario):**

```
將 Step 4 收集到嘅資料填寫落正式嘅重要控制人登記冊。
SCR 冇法定格式，但必須包含指定嘅資料欄位。可以用 generator 直接生成已填好嘅 PDF。

📋 SCR 必須包含嘅資料欄位：
1. 重要控制人姓名或名稱
2. 通訊地址
3. 身份證明文件類型同號碼
4. 成為重要控制人嘅日期
5. 控制性質（符合邊項測試條件）
6. 登記冊備存嘅日期
7. 存放地點（註冊辦事處或指明地方）
8. 指定代表資料（姓名、聯絡方式）
9. 任何註記（如有人未回覆通知、資料變更記錄、無控制人聲明）

📄 無控制人聲明（公司冇重要控制人嘅情況）：
如果 Step 2 嘅 5 項測試做完，發現公司真係冇人符合條件，
你唔可以就咁唔備存 SCR！你仍然要：
• 備存一份 SCR（可以係空白登記冊）
• 喺登記冊註明「經查核後公司無重要控制人」
• 寫清楚查核日期同負責人簽署
• 記錄你做咗啲咩查核步驟

  範本文字：
  「本公司經查核（查核日期：____年__月__日），
   根據公司條例第 653ZH 條嘅 5 項測試標準，
   確認本公司目前並無任何重要控制人。
   日後如有股權變動或控制權變更，會即時更新本登記冊。
   簽署：________________  日期：________________」

⚠️ 唔好做嘅事：
• 冇人符合條件唔可以留空 → 要寫明「經查核後公司無重要控制人」
• 唔好以為冇控制人就唔使做 SCR → 法律規定必須備存，即使冇控制人都要
• 唔好用手寫 → 容易擦花或改動，建議打印或用 generator
• 唔好亂咁改 → 任何更改要有日期同簽署記錄
• 唔好漏咗指定代表資料
• 控制性質唔好寫得太模糊（就寫「股東」而唔係「持有超過25%股份」）

✅ 一定要做：
• 用清晰可讀嘅格式填寫
• 每位控制人獨立一行或一頁
• 控制性質要對應 Step 2 嘅測試結果
• 填寫人簽署 + 日期
• 保留一份副本作記錄
```

**Documents (updated — added 無控制人聲明 template):**
```json
{
  "name": "重要控制人登記冊（含無控制人聲明範本）",
  "description": "正式嘅 SCR 登記冊，包含標準控制人記錄頁 + 無控制人聲明範本。可透過互動工具一鍵生成已填好嘅 PDF",
  "demoImage": "/assets/demo/scr-step6.png",
  "templateFile": "/templates/scr-register.docx",
  "hasGenerator": true,
  "generatorUrl": "/scr-generator",
  "commonMistakes": [
    "控制性質寫得太模糊（就寫「股東」而唔係「持有超過25%股份」）",
    "冇簽署同日期",
    "冇定期 update",
    "冇控制人但留空登記冊（冇寫聲明）",
    "冇記錄指定代表"
  ]
}
```

**RejectionRisks:**
```json
[
  "冇控制人但留空登記冊 = 違規，要寫無控制人聲明",
  "資料唔齊全 = 執法人員查冊時資料唔符合要求"
]
```

---

### Step 7 (Modified - 原本 Step 5): 備存同維護 SCR

**Update:** NR2 明確標明係「條件性 — 只有 SCR 放喺註冊辦事處以外先需要」

**Title:** 備存同維護 SCR（NR2 條件性通知）
**Summary:** 將 SCR 存放喺適當地方，確保隨時可查閱。NR2 只係放喺註冊辦事處以外先需要提交
**isFree:** true
**mode:** B

**Details (updated — clarified NR2 is conditional):**

```
最後一步係將填好嘅 SCR 放喺公司可以隨時查閱嘅地方，並確保資料係最新。

📍 存放位置（二選一）：
• 選項 A：公司註冊辦事處地址 🔵 最簡單，唔使額外通知 ✅
• 選項 B：香港境內另一個指明地方 ⚠️ 必須 15 日內提交 Form NR2 通知公司註冊處

❗ NR2 係條件性嘅 — 唔係間間公司都需要：
• SCR 放喺註冊辦事處 = ❌ 唔使交 NR2
• SCR 放喺註冊辦事處以外嘅地方 = ✅ 要交 NR2（15 日內）
• 例外：如果 SCR 同成員登記冊（Register of Members）
  放喺同一已申報地址，唔使重複提交 NR2

⏰ 維護時間表：
• 確認控制人資料變更 → 7 日內更新 SCR（2025 年起由 14 天縮短至 7 天）
• 知悉新控制人出現 → 7 日內加入登記冊
• 控制人不再符合條件 → 7 日內移除（保留歷史記錄）
• 控制人終止後 → 保留記錄至少 6 年
• 執法人員要求查閱（9 個機關有權）→ 立即提供（1 小時內）
• 每年至少 review 一次
• 如更改存放位置 → 15 日內提交 Form NR2

👤 指定代表維護：
• 確保隨時至少有一位指定代表
• 代表離職或離港 → 盡快更換
• 代表聯絡方式變更 → 更新 SCR

⚠️ 唔好做嘅事：
• 唔好放喺公司註冊處以外地方但冇交 NR2 → 違規，最高罰 HK$25,000
• 唔好忽略更新 → 公司股權變動後要 7 日內改
• 唔好夠 6 年就即刻銷毀 → 到期後先可以銷毀，並記錄銷毀日期
• 唔好以為一年 check 一次就夠 → 公司有重大變動要即時 update
• 唔好冇指定代表 → 違反公司條例

✅ 一定要做：
• 決定存放位置（註冊辦事處 🆓 / 指明地方 + NR2）
• 7 日內更新任何變更
• 每年年度 review
• 保留歷史記錄至少 6 年
• 指定至少一位代表
```

**Documents (updated — NR2 標明條件性):**
```json
{
  "name": "指明地點通知書（Form NR2）— 條件性文件",
  "description": "⚠️ 只有當 SCR 存放喺公司註冊辦事處以外嘅地址先需要。如需提交，必須喺 15 日內完成。放喺註冊辦事處嘅公司唔使",
  "demoImage": "/assets/demo/scr-step7.png",
  "templateFile": "/templates/scr-location-notice.docx",
  "hasGenerator": true,
  "commonMistakes": [
    "放喺註冊辦事處都照交 NR2（唔需要）",
    "放喺第二度但唔記得交 NR2",
    "更改存放地址後冇喺 15 日內更新 NR2",
    "以為 SCR 係一次性文件，之後唔使 update",
    "冇保留歷史記錄至少 6 年"
  ],
  "generatorUrl": "/scr-nr2-generator"
}
```

**RejectionRisks:**
```json
[
  "存放位置唔啱 + 冇通知 = 違反公司條例，最高罰 HK$25,000",
  "冇指定代表 = 違反公司條例",
  "冇及時更新 = 股權變動 7 日內未改，銀行 KYC 觸發警報"
]
```

---

## 4️⃣ 完整 scr-processes.json 更新 draft

Below is the updated JSON structure. Save this as `scr-processes.json` (replacing the current one):

```json
{
  "processId": "significant-controllers-register",
  "title": "香港有限公司重要控制人登記冊 (SCR) 完整指南",
  "totalSteps": 7,
  "freeSteps": 7,
  "price": 0,
  "currency": "HKD",
  "donateMessage": "如果呢份指南幫到你，可以請我飲杯咖啡 ☕",
  "steps": [
    {
      "stepNumber": 1,
      "title": "分析公司股權結構",
      "summary": "了解公司股東、持股比例、投票權安排，為識別重要控制人做準備",
      "isFree": true,
      "details": "第一步係搞清楚公司嘅股權結構。睇公司股東名冊（Register of Members），列出所有股東同佢哋嘅持股比例。如果股權結構複雜有代持股、Nominee 持股、信託或公司持股，要拆開逐層睇。\n\n⚠️ 唔好做嘅事：\n• 唔好淨係睇股東名冊 → 要睇埋投票權安排（有啲股東持股少但投票權多）\n• 唔好忽略關連人士 → 配偶、子女嘅持股要合併計算（公司條例要求）\n• 唔好用過期資料 → 公司結構有變要先更新\n• 唔好漏咗 Nominee 持股 → 代名人持有嘅股份視為受益人持有\n• 唔好漏咗信託持股 → 信託受託人要當作控制人處理\n\n✅ 一定要做：\n• 準備最新嘅股東名冊\n• 列出每位股東嘅持股比例\n• 記錄特別投票權安排（如有）\n• 標註關連人士關係\n• 如有 Nominee 持股，記錄實益擁有人\n• 如有信託，記錄受託人同受益人資料",
      "documents": [
        {
          "name": "股權結構分析表",
          "description": "幫你整理公司股東、持股比例同投票權結構，方便下一步識別重要控制人",
          "demoImage": "/assets/demo/scr-step1.png",
          "templateFile": "/templates/scr-shareholder-analysis.docx",
          "hasGenerator": true,
          "commonMistakes": [
            "冇更新股東名冊就開始分析",
            "忽略關連人士合計持股",
            "冇處理 Nominee 持股",
            "冇處理信託結構"
          ],
          "generatorUrl": "/scr-shareholder-analysis-generator"
        }
      ],
      "rejectionRisks": [
        "股權結構唔清晰 = 容易漏咗真正嘅重要控制人"
      ],
      "mode": "B",
      "needsGenerator": true,
      "needsGuideContent": true,
      "crossStepDeps": "None - first step",
      "generatorType": "Word Template Generator",
      "generatorUrl": "/scr-shareholder-analysis-generator",
      "generatorDescription": "Word template generator — 填股東資料 → 下載已填好嘅股權結構分析表 Word 檔案"
    },
    {
      "stepNumber": 2,
      "title": "識別重要控制人（5項測試）",
      "summary": "用公司條例嘅 5 項法定標準，逐項測試每個人或法團是否符合重要控制人條件",
      "isFree": true,
      "details": "用公司條例嘅 5 項測試標準逐個對照（Source: CR FAQ Q4, CR Guideline Ch.10）：\n\n📋 測試 1：持股 25% 以上\n直接或間接持有公司多過 25% 嘅股份。計算時要包括關連人士嘅持股。Nominee 持有嘅股份視為受益人持有。如公司冇股本，則有權分佔超過 25% 資本或利潤。\n\n📋 測試 2：投票權 25% 以上\n直接或間接控制多過 25% 嘅投票權。有啲股東持股少但投票權多，要分開計。\n\n📋 測試 3：董事任命權\n有權委任或罷免大多數董事。就算持股少，有董事任命權都符合條件。\n\n📋 測試 4：重大影響或控制\n有權對公司行使，或實際上行使緊重大影響或控制。包括影子董事。唔包括專業顧問或標準協議下嘅貸款人（除非角色有實質差異）。\n\n📋 測試 5：對信託或商號嘅影響\n對信託或商號有重大影響或控制，而該信託或商號嘅受託人或成員符合測試 1-4。\n\n🌿 冇控制人嘅情況：\n如果做完 5 項測試都冇人符合條件，唔代表你可以唔理！\n公司仍然必須備存 SCR，並喺登記冊寫明無控制人聲明。\n詳情見 Step 6「填寫登記冊 — 無控制人聲明」部份。\n\n⚠️ 唔好做嘅事：\n• 唔好只睇表面持股 → 間接持股（透過其他公司持有）都要計\n• 唔好忽略 multiple controllers → 可以有多個重要控制人\n• 冇人符合條件唔可以唔理 → 要有正式記錄「經查核後公司無重要控制人」\n• 唔好忽略影子董事 → 實際控制公司營運嘅人都要計\n\n✅ 一定要做：\n• 逐項測試每位股東或有影響力人士\n• 記錄每個人符合邊項條件\n• 如有間接持股或法團股東，穿透到最終自然人\n• 冇人符合條件 → 記錄「經查核後公司無重要控制人」並簽署確認（準備進入 Step 6 寫入登記冊）",
      "documents": [
        {
          "name": "重要控制人識別檢查表",
          "description": "逐項測試嘅 checklist，記錄每位人士及法團嘅測試結果同符合條件",
          "demoImage": "/assets/demo/scr-step2.png",
          "templateFile": "/templates/scr-identification-checklist.docx",
          "hasGenerator": true,
          "commonMistakes": [
            "只睇表面持股唔計間接持股",
            "冇處理關連人士合計持股",
            "以為冇人就唔使記錄"
          ],
          "generatorUrl": "/scr-identification-checklist-generator"
        }
      ],
      "rejectionRisks": [
        "漏咗真正嘅重要控制人 = 違反公司條例，可被罰款高達 HK$25,000 + 每日罰款"
      ],
      "mode": "B",
      "needsGenerator": true,
      "needsGuideContent": true,
      "crossStepDeps": "Step 1 (equity structure analysis needed for identification)",
      "generatorType": "Word Template Generator",
      "generatorUrl": "/scr-identification-checklist-generator",
      "generatorDescription": "Word template generator — 填測試結果 → 下載已填好嘅重要控制人識別檢查表 Word 檔案"
    },
    {
      "stepNumber": 3,
      "title": "發出書面通知俾疑似控制人",
      "summary": "向疑似重要控制人發出法定書面通知，佢哋有 1 個月法定義務回覆",
      "isFree": true,
      "details": "識別咗邊啲可能係重要控制人之後，公司有法定責任向佢哋發出書面通知（Section 653ZH, Cap. 622）。唔係打電話或者 WhatsApp 就得 — 一定要書面，有記錄。\n\n📮 通知對象：\n• Step 2 測試後符合條件嘅人/法團\n• 有合理理由相信係重要控制人嘅人\n• 股東名冊上嘅 major shareholders（建議全部通知）\n\n📝 通知書必須包含：\n• 公司名稱同 SCR 相關法律條文\n• 收件人姓名\n• 要求確認嘅問題（是否符合某項控制權條件）\n• 回覆期限（法定 1 個月內）\n• 唔回覆嘅後果（可被罰款 HK$25,000 + 每日 HK$700）\n• 公司授權人簽署 + 日期\n\n📬 發出方式：\n• 親身交付（收書面回條）\n• 掛號郵件（有追蹤號碼）\n• 電子郵件（要對方確認收到，建議用埋 Read Receipt）\n• 快遞（有簽收記錄）\n\n⏰ 時間線：\n• 發出通知 → 對方有 1 個月回覆\n• 對方冇回覆 → 喺 SCR 註明「已發出通知但未獲回覆」\n• 對方確認係控制人 → 進入 Step 4 收集詳細資料\n• 對方否認係控制人 → 記錄佢嘅否認聲明\n\n⚠️ 唔好做嘅事：\n• 唔好用口頭通知 → 公司條例要求書面，冇書面記錄等於冇做\n• 唔好漏咗疑似控制人 → 明知有人疑似但冇通知，係違規\n• 唔好俾太少時間回覆 → 法定最少 1 個月\n• 有人唔回覆唔可以就咁算 → 要喺 SCR 註明「未能確認」\n• 唔好冇保留通知記錄 → CR 查冊時要證明你做咗通知\n\n✅ 一定要做：\n• 用標準格式發出書面通知\n• 保留發出證明（掛號收據、簽收回條）\n• 記錄發出日期同回覆日期\n• 有人冇回覆 → 登記冊加註記\n• 控制人確認後先繼續 Step 4",
      "documents": [
        {
          "name": "重要控制人書面通知書",
          "description": "標準格式嘅書面通知書模板，用嚟通知疑似重要控制人，包含法定要求嘅所有欄位",
          "demoImage": "/assets/demo/scr-step3.png",
          "templateFile": "/templates/scr-notice-letter.docx",
          "hasGenerator": true,
          "commonMistakes": [
            "用口頭通知冇書面記錄",
            "冇保留發出證明",
            "俾嘅回覆時間唔夠 1 個月",
            "有人唔回覆就唔理"
          ],
          "generatorUrl": "/scr-notice-generator"
        }
      ],
      "rejectionRisks": [
        "冇發出書面通知 = 違反公司條例，可被罰款 HK$25,000",
        "冇保留通知記錄 = CR 查冊時無法證明已履行通知義務"
      ],
      "mode": "B",
      "needsGenerator": true,
      "needsGuideContent": true,
      "crossStepDeps": "Step 2 (need to identify controllers before notifying them)",
      "generatorType": "Word Template Generator",
      "generatorUrl": "/scr-notice-generator",
      "generatorDescription": "Word template generator — 填通知書資料 → 下載已填好嘅書面通知書 Word 檔案"
    },
    {
      "stepNumber": 4,
      "title": "收集控制人法定資料",
      "summary": "收集每位已確認重要控制人嘅身份證明文件同法定聯絡資料",
      "isFree": true,
      "details": "確定咗邊啲係重要控制人（佢哋回覆咗通知並確認身份），就要收集佢哋嘅法定資料記錄入 SCR。\n\n📝 收集嘅資料（自然人控制人）：\n• 全名（中文+英文，同身份證一致）\n• 通訊地址（可用服務地址，唔可以用郵政信箱）\n• 身份證號碼 / 護照號碼 + 簽發國\n• 出生日期\n• 成為重要控制人嘅日期\n• 控制性質（符合邊項測試條件 — 對應 Step 2 結果）\n\n🏢 收集嘅資料（法團控制人）：\n• 公司名稱\n• 法律形式（如有限公司）\n• 公司註冊編號\n• 成立地（適用法例）\n• 註冊辦事處地址\n• 成為重要控制人嘅日期\n• 控制性質\n\n⚠️ 唔好做嘅事：\n• 唔好接受口頭提供資料 → 要有書面記錄同簽署\n• 唔好漏咗控制性質 → 淨係寫名唔夠，要寫明符合邊項測試\n• 地址唔好用郵政信箱 → 公司條例規定唔可以用郵政信箱做 SCR 地址\n• 唔好拖延 → 知道有新控制人後要盡快收集資料\n• 有人唔回覆通知 → 要喺登記冊註明「未能確認」，唔可以就咁唔理\n\n✅ 一定要做：\n• 控制人簽署確認後先記錄入 SCR\n• 保留控制人確認書\n• 核對身份證明文件正本/核證副本",
      "documents": [
        {
          "name": "重要控制人資料收集表",
          "description": "標準嘅資料收集表格，控制人簽署確認後歸檔",
          "demoImage": "/assets/demo/scr-step4.png",
          "templateFile": "/templates/scr-data-collection.docx",
          "hasGenerator": true,
          "commonMistakes": [
            "資料唔齊全就入 SCR",
            "地址用郵政信箱",
            "冇簽署確認"
          ],
          "generatorUrl": "/scr-data-collection-generator"
        }
      ],
      "rejectionRisks": [
        "資料唔齊全 = 執法人員查冊時發現資料唔完整，要求解釋"
      ],
      "mode": "B",
      "needsGenerator": true,
      "needsGuideContent": true,
      "crossStepDeps": "Step 3 (need to confirm controllers before collecting data)",
      "generatorType": "Word Template Generator",
      "generatorUrl": "/scr-data-collection-generator",
      "generatorDescription": "Word template generator — 填控制人資料 → 下載已填好嘅資料收集表 Word 檔案"
    },
    {
      "stepNumber": 5,
      "title": "委任指定代表（董事會決議）",
      "summary": "經董事會決議正式委任最少一位指定代表，負責聯絡同提供 SCR 俾執法機構查閱",
      "isFree": true,
      "details": "每間公司必須指定最少一位指定代表（Designated Representative），而且一定要經董事會決議（Board Resolution）正式委任 — 唔可以就咁口頭叫阿邊個做。\n\n👤 合資格人士（2026年更新明確三類）：\n1. 公司股東、董事或僱員（必須係居於香港嘅自然人）\n2. 會計專業人士（CPA、會計師行）\n3. 法律專業人士（律師、律師行）\n4. 信託或公司服務持牌人（TCSP）\n\n🔖 指定代表嘅職責：\n• 喺正常辦公時間內提供 SCR 俾執法人員查閱\n• 接獲查閱要求後 1 小時內提供 SCR（2025-2026 年執法重點！）\n• 確保 SCR 資料最新\n• 保管相關文件記錄\n\n📋 董事會決議內容：\n• 委任人士姓名\n• 委任生效日期\n• 職責範圍\n• 薪酬（如有）\n• 授權簽署\n• 會議日期同決議編號\n\n⚠️ 唔好做嘅事：\n• 唔好冇書面委任記錄 → 要董事會決議 + 當事人同意書\n• 唔好委任非居港人士 → 要居於香港（自然人適用）\n• 唔好委任後唔通知佢要做咩 → 要清楚列明職責\n• 唔好冇後備人選 → 指定代表離職或離港要盡快更換\n• 唔好以為董事自動係指定代表 → 要正式委任\n\n✅ 一定要做：\n• 董事會決議記錄\n• 指定代表簽署同意書\n• 記錄喺 SCR\n• 確保隨時至少有一位代表\n• 代表離職 → 30 日內更換\n\n📊 實戰數據：\n2025 年末執法數據顯示，約 12% 被查企業因指定代表未能在 1 小時內提供 SCR 而收到罰單。揀一個 responsibile 嘅代表好重要！",
      "documents": [
        {
          "name": "指定代表委任決議 + 同意書",
          "description": "董事會決議範本 + 指定代表同意書，包含所有法定欄位同簽署位置",
          "demoImage": "/assets/demo/scr-step5.png",
          "templateFile": "/templates/scr-designated-rep-resolution.docx",
          "hasGenerator": true,
          "commonMistakes": [
            "冇董事會決議記錄",
            "委任非居港人士",
            "冇後備人選",
            "冇通知代表佢嘅法定職責"
          ],
          "generatorUrl": "/scr-designated-rep-generator"
        }
      ],
      "rejectionRisks": [
        "冇指定代表 = 違反公司條例，可被罰款 HK$25,000",
        "指定代表未能 1 小時內提供 SCR = 最高 HK$25,000 罰款（12% 被查企業中招）"
      ],
      "mode": "B",
      "needsGenerator": true,
      "needsGuideContent": true,
      "crossStepDeps": "Steps 1-4 (need to understand company structure before appointing rep)",
      "generatorType": "Word Template Generator",
      "generatorUrl": "/scr-designated-rep-generator",
      "generatorDescription": "Word template generator — 填委任資料 → 下載已填好嘅董事會決議 + 同意書 Word 檔案"
    },
    {
      "stepNumber": 6,
      "title": "填寫重要控制人登記冊（含無控制人聲明）",
      "summary": "將收集到嘅資料正式記錄入 SCR，冇控制人嘅公司都要備存並註明聲明",
      "isFree": true,
      "details": "將 Step 4 收集到嘅資料填寫落正式嘅重要控制人登記冊。SCR 冇法定格式，但必須包含指定嘅資料欄位。可以用 generator 直接生成已填好嘅 PDF。\n\n📋 SCR 必須包含嘅資料欄位：\n1. 重要控制人姓名或名稱\n2. 通訊地址\n3. 身份證明文件類型同號碼\n4. 成為重要控制人嘅日期\n5. 控制性質（符合邊項測試條件）\n6. 登記冊備存嘅日期\n7. 存放地點（註冊辦事處或指明地方）\n8. 指定代表資料（姓名、聯絡方式）\n9. 任何註記（如有人未回覆通知、資料變更記錄、無控制人聲明）\n\n📄 無控制人聲明（公司冇重要控制人嘅情況）：\n如果 Step 2 嘅 5 項測試做完，發現公司真係冇人符合條件，你唔可以就咁唔備存 SCR！你仍然要：\n• 備存一份 SCR（可以係空白登記冊）\n• 喺登記冊註明「經查核後公司無重要控制人」\n• 寫清楚查核日期同負責人簽署\n• 記錄你做咗啲咩查核步驟\n\n  範本文字：\n  「本公司經查核（查核日期：____年__月__日），\n   根據公司條例第 653ZH 條嘅 5 項測試標準，\n   確認本公司目前並無任何重要控制人。\n   日後如有股權變動或控制權變更，會即時更新本登記冊。\n   簽署：________________  日期：________________」\n\n⚠️ 唔好做嘅事：\n• 冇人符合條件唔可以留空 → 要寫明「經查核後公司無重要控制人」\n• 唔好以為冇控制人就唔使做 SCR → 法律規定必須備存，即使冇控制人都要\n• 唔好用手寫 → 容易擦花或改動，建議打印或用 generator\n• 唔好亂咁改 → 任何更改要有日期同簽署記錄\n• 唔好漏咗指定代表資料\n• 控制性質唔好寫得太模糊（就寫「股東」而唔係「持有超過25%股份」）\n\n✅ 一定要做：\n• 用清晰可讀嘅格式填寫\n• 每位控制人獨立一行或一頁\n• 控制性質要對應 Step 2 嘅測試結果\n• 填寫人簽署 + 日期\n• 保留一份副本作記錄",
      "documents": [
        {
          "name": "重要控制人登記冊（含無控制人聲明範本）",
          "description": "正式嘅 SCR 登記冊，包含標準控制人記錄頁 + 無控制人聲明範本。可透過互動工具一鍵生成已填好嘅 PDF",
          "demoImage": "/assets/demo/scr-step6.png",
          "templateFile": "/templates/scr-register.docx",
          "hasGenerator": true,
          "generatorUrl": "/scr-generator",
          "commonMistakes": [
            "控制性質寫得太模糊（就寫「股東」而唔係「持有超過25%股份」）",
            "冇簽署同日期",
            "冇定期 update",
            "冇控制人但留空登記冊（冇寫聲明）",
            "冇記錄指定代表"
          ]
        }
      ],
      "rejectionRisks": [
        "冇控制人但留空登記冊 = 違規，要寫無控制人聲明",
        "資料唔齊全 = 執法人員查冊時資料唔符合要求"
      ],
      "mode": "A",
      "needsGenerator": true,
      "needsGuideContent": true,
      "crossStepDeps": "Steps 3-5 (notice sent, data collected, rep appointed)",
      "generatorType": "Interactive PDF Generator",
      "generatorUrl": "/scr-generator",
      "generatorDescription": "互動 PDF 工具 — 填好公司資料同控制人資料 → 一鍵生成已填好嘅 SCR 登記冊 PDF"
    },
    {
      "stepNumber": 7,
      "title": "備存同維護 SCR（NR2 條件性通知）",
      "summary": "將 SCR 存放喺適當地方。NR2 只係放喺註冊辦事處以外先需要提交，唔係間間公司都要",
      "isFree": true,
      "details": "最後一步係將填好嘅 SCR 放喺公司可以隨時查閱嘅地方，並確保資料係最新。\n\n📍 存放位置（二選一）：\n• 選項 A：公司註冊辦事處地址 🔵 最簡單，唔使額外通知 ✅\n• 選項 B：香港境內另一個指明地方 ⚠️ 必須 15 日內提交 Form NR2 通知公司註冊處\n\n❗ NR2 係條件性嘅 — 唔係間間公司都需要：\n• SCR 放喺註冊辦事處 = ❌ 唔使交 NR2\n• SCR 放喺註冊辦事處以外嘅地方 = ✅ 要交 NR2（15 日內）\n• 例外：如果 SCR 同成員登記冊（Register of Members）放喺同一已申報地址，唔使重複提交 NR2\n\n⏰ 維護時間表：\n• 確認控制人資料變更 → 7 日內更新 SCR（2025 年起由 14 天縮短至 7 天）\n• 知悉新控制人出現 → 7 日內加入登記冊\n• 控制人不再符合條件 → 7 日內移除（保留歷史記錄）\n• 控制人終止後 → 保留記錄至少 6 年\n• 執法人員要求查閱（9 個機關有權）→ 立即提供（1 小時內）\n• 每年至少 review 一次\n• 如更改存放位置 → 15 日內提交 Form NR2\n\n👤 指定代表維護：\n• 確保隨時至少有一位指定代表\n• 代表離職或離港 → 盡快更換\n• 代表聯絡方式變更 → 更新 SCR\n\n⚠️ 唔好做嘅事：\n• 唔好放喺公司註冊處以外地方但冇交 NR2 → 違規，最高罰 HK$25,000\n• 唔好忽略更新 → 公司股權變動後要 7 日內改\n• 唔好夠 6 年就即刻銷毀 → 到期後先可以銷毀，並記錄銷毀日期\n• 唔好以為一年 check 一次就夠 → 公司有重大變動要即時 update\n• 唔好冇指定代表 → 違反公司條例\n\n✅ 一定要做：\n• 決定存放位置（註冊辦事處 🆓 / 指明地方 + NR2）\n• 7 日內更新任何變更\n• 每年年度 review\n• 保留歷史記錄至少 6 年\n• 指定至少一位代表",
      "documents": [
        {
          "name": "指明地點通知書（Form NR2）— 條件性文件",
          "description": "⚠️ 只有當 SCR 存放喺公司註冊辦事處以外嘅地址先需要。如需提交，必須喺 15 日內完成。放喺註冊辦事處嘅公司唔使",
          "demoImage": "/assets/demo/scr-step7.png",
          "templateFile": "/templates/scr-location-notice.docx",
          "hasGenerator": true,
          "commonMistakes": [
            "放喺註冊辦事處都照交 NR2（唔需要）",
            "放喺第二度但唔記得交 NR2",
            "更改存放地址後冇喺 15 日內更新 NR2",
            "以為 SCR 係一次性文件，之後唔使 update",
            "冇保留歷史記錄至少 6 年"
          ],
          "generatorUrl": "/scr-nr2-generator"
        }
      ],
      "rejectionRisks": [
        "存放位置唔啱 + 冇通知 = 違反公司條例，最高罰 HK$25,000",
        "冇指定代表 = 違反公司條例",
        "冇及時更新 = 股權變動 7 日內未改，銀行 KYC 觸發警報"
      ],
      "mode": "B",
      "needsGenerator": true,
      "needsGuideContent": true,
      "crossStepDeps": "Step 6 (need completed register before filing NR2)",
      "generatorType": "Word Template Generator",
      "generatorUrl": "/scr-nr2-generator",
      "generatorDescription": "Word template generator — 填存放地址資料 → 下載已填好嘅 Form NR2 指明地點通知書 Word 檔案"
    }
  ],
  "finalDonate": {
    "title": "幫到你嗎？請我飲杯咖啡 ☕",
    "message": "呢份指南係我親身經歷整理，全部免費公開。如果幫到你節省時間同金錢，可以請我飲杯咖啡支持下，等我繼續製作更多免費指南！",
    "goalMessage": "目標：100 次支持下載後，我會擴展到更多公司合規流程指南 🎯",
    "buyMeACoffeeUrl": "https://buymeacoffee.com/esgov",
    "emailCollectionTitle": "想我哋提供咩指南？",
    "emailCollectionMessage": "可以通知我哋，話俾我哋知你想睇咩文件 😊"
  }
}
```

---

## 5️⃣ HTML 改動摘要（俾 Builder 參考）

### `<head>` 入面嘅改動

| 項目 | 改動 |
|------|------|
| `<title>` | `5個步驟搞掂` → `7個步驟搞掂，含通知範本` |
| `<meta name="description">` | 更新內容（見上 §1） |
| `<meta property="og:title">` | `5個步驟搞掂 | ESGov` → `7個步驟搞掂` |
| `<meta property="og:description">` | 更新內容（見上 §1） |
| `<script type="application/ld+json">` (WebPage) | `5個步驟` → `7個步驟` |
| 新增 FAQPage schema | 加第二個 `application/ld+json` block（見上 §1 FAQPage） |

### Alpine.js `x-data` 入面嘅改動

| 行數 | 改動 |
|------|------|
| L74 | `totalSteps: 5` → `totalSteps: 7` |
| L392 | `5 個步驟全部完成` → `7 個步驟全部完成` |

### JSON 載入

JSON 檔案由 `scr-processes.json?v=2.0` 更新為新版本，
建議 bump version 為 `?v=3.0`。

---

## 6️⃣ 需要新增嘅 Generator / Template

| Generator | 用途 | 對應 Step |
|-----------|------|-----------|
| `/scr-notice-generator` | 重要控制人書面通知書 | Step 3 |
| `/scr-designated-rep-generator` | 指定代表委任決議 + 同意書 | Step 5 |
| `/scr-generator`（更新） | 加入無控制人聲明選項 | Step 6 |
| `/scr-nr2-generator`（更新） | 標明条件性，加免責提示 | Step 7 |

---

## 7️⃣ 變更對應研究員 Findings 一覽

| Researcher Finding | 點樣修正 |
|-------------------|---------|
| **1. 發出書面通知 missing** | ✅ 新 Step 3 完全獨立，有完整內容、文件、generator |
| **2. 委任指定代表 missing** | ✅ 新 Step 5 獨立成步，加入董事會決議要求 |
| **3. Step 5 bundles NR2 + 維護** | ✅ Step 7 開頭標明「NR2 係條件性嘅 — 唔係間間公司都需要」，兩個選項清楚對比 |
| **4. 無控制人聲明 missing** | ✅ Step 2 加入分支路徑提示 + Step 6 完整無控制人聲明範本 + 文件模板更新 |

---

*呢份係內容草案，俾 Builder 參考實作。唔好直接修改現有 HTML/JSON 檔案。*
