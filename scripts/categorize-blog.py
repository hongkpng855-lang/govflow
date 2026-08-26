#!/usr/bin/env python3
"""Categorize all blog articles into 8 categories by title keyword matching.
Outputs a mapping file for use in blog index page.
"""
import os, re, json

BLOG = "/mnt/c/Users/hongk/Desktop/esgov/blog"

# Category → keywords (order matters: first match wins)
CATEGORIES = [
    ("開公司", ["開公司", "公司註冊成立", "創業", "有限公司 vs", "無限公司", "銀行戶口", "虛擬銀行", "外國人", "大灣區", "12 個月必做", "每年合規 checklist", "合規時間表"]),
    ("股份", ["股份轉讓", "股份配發", "股份證明書", "股份回購", "減資", "share", "ESOP", "股東協議", "轉股東", "Sold Note", "Bought"]),
    ("合規", ["SCR", "重要控制人", "條例第622", "違反《公司條例》", "查冊", "法定紀錄", "會計記帳", "資料私隱", "零申報", "Dormant"]),
    ("董事股東", ["董事", "股東", "AGM", "股東大會", "董事袍金", "董事借貸", "股東墊款", "股權", "派息", "分紅", "繼承", "家族企業"]),
    ("報稅審計", ["報稅", "審計", "核數", "印花稅", "厘印", "暫繳稅", "離岸利得", "利得稅", "IR56B", "薪俸", "派息", "分紅"]),
    ("人事", ["僱傭", "員工", "MPF", "強積金", "長期服務金", "遣散費", "解僱", "終止僱傭", "第一次請人", "員工手冊", "勞工"]),
    ("財務保險", ["保險", "D&O", "貸款", "融資", "追數", "信用管理", "商業貸款", "財務管理", "僱員補償", "索償"]),
    ("公司文件", ["授權書", "公司印章", "Company Chop", "電子簽署", "章程", "會議紀錄", "Invoice", "收據", "公證", "文件", "ND2A", "NDR1", "周年申報", "商業登記", "撤銷註冊", "恢復註冊", "清盤", "更改公司名稱", "改名", "註冊地址變更", "公司秘書", "董事公司秘書變更", "審計報告", "商標", "盡職審查", "業務估值", "公司轉讓", "賣公司", "集團架構", "租約", "合約", "糾紛", "網站及網上營銷", "電子簽署", "會計", "銀行", "資本", "法定", "股份賣出單"]),
]

FALLBACK = "其他"

def categorize(title):
    t = title.lower()
    for cat, kws in CATEGORIES:
        for kw in kws:
            if kw.lower() in t:
                return cat
    return FALLBACK

def main():
    result = {}
    for d in sorted(os.listdir(BLOG)):
        idx = os.path.join(BLOG, d, "index.html")
        if not os.path.isfile(idx):
            continue
        raw = open(idx, encoding="utf-8").read()
        m = re.search(r"<title>ESGov \| ([^<]+)</title>", raw)
        title = m.group(1).strip() if m else d
        cat = categorize(title)
        result[d] = {"title": title, "category": cat}

    # Distribution
    from collections import Counter
    dist = Counter(v["category"] for v in result.values())
    print("分類分佈:")
    for cat, n in dist.most_common():
        print(f"  {cat}: {n}")

    # Save
    out = "/mnt/c/Users/hongk/Desktop/esgov/scripts/blog-categories.json"
    json.dump(result, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"\nSaved: {out}")
    print(f"Total: {len(result)}")

if __name__ == "__main__":
    main()