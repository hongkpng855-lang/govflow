#!/usr/bin/env python3
"""Generate redirect stub files for old .html blog URLs → pretty URLs."""
import os, html, re, urllib.parse

BLOG = "/mnt/c/Users/hongk/Desktop/esgov/blog"

pages = [
    "香港公司股份轉讓流程2026",
    "香港公司股份證明書ShareCertificate終極指南",
    "有限公司更換核數師終極指南",
    "香港公司董事會議紀錄終極指南",
    "香港公司查冊終極指南",
    "香港公司集團架構控股子公司終極指南",
    "香港有限公司公司印章CompanyChop終極指南",
    "hk-company-share-allotment",
    "董事公司秘書變更指南",
    "香港中小企AI自動化工具終極指南",
    "香港中小企ESG入門終極指南",
    "香港公司僱傭條例EmploymentOrdinance終極指南",
    "香港公司商業租約CommercialLease終極指南",
    "香港公司強積金MPF安排終極指南",
    "香港公司文件公證認證加簽終極指南",
    "香港公司盡職審查DueDiligence終極指南",
    "香港公司章程修改完整指南",
    "香港公司開銀行戶口2026實戰指南",
]

created = 0
for name in pages:
    pretty_dir = os.path.join(BLOG, name)
    if not os.path.isdir(pretty_dir):
        print(f"SKIP (no dir): {name}")
        continue

    # Get title from the real page
    title = "ESGov 指南"
    real_index = os.path.join(pretty_dir, "index.html")
    if os.path.exists(real_index):
        with open(real_index, encoding="utf-8") as f:
            m = re.search(r"<title>(.*?)</title>", f.read(), re.DOTALL)
            if m:
                title = m.group(1).strip()

    pretty_url = f"https://esgov.org/blog/{urllib.parse.quote(name)}/"
    stub_path = os.path.join(BLOG, name + ".html")

    stub = f"""<!DOCTYPE html>
<html lang="zh-HK">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{html.escape(title)}</title>
  <meta name="robots" content="noindex, follow" />
  <link rel="canonical" href="{pretty_url}" />
  <meta http-equiv="refresh" content="0; url={pretty_url}" />
  <script>window.location.replace("{pretty_url}");</script>
</head>
<body>
  <p>此頁面已移動到 <a href="{pretty_url}">{html.escape(title)}</a>。</p>
</body>
</html>
"""
    with open(stub_path, "w", encoding="utf-8") as f:
        f.write(stub)
    created += 1
    print(f"✅ {name}.html → {name}/")

print(f"\n{created} redirect stubs created")
