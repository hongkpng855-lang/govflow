#!/usr/bin/env python3
"""Add BreadcrumbList JSON-LD to all HTML pages."""

import os, re, json

BASE = "/mnt/c/Users/hongk/Desktop/esgov"
BASE_URL = "https://esgov.org"

# Breadcrumb definitions per path pattern
BREADCRUMBS = {
    # root
    "": [{"name": "首頁", "url": ""}],
    # core generators
    "shareholder-transfer": [
        {"name": "首頁", "url": ""},
        {"name": "股份轉讓文件", "url": "shareholder-transfer"},
    ],
    "sold-note-generator": [
        {"name": "首頁", "url": ""},
        {"name": "股份轉讓文件", "url": "shareholder-transfer"},
        {"name": "Sold Note 買賣單", "url": "sold-note-generator"},
    ],
    "letter-of-transferee-generator": [
        {"name": "首頁", "url": ""},
        {"name": "股份轉讓文件", "url": "shareholder-transfer"},
        {"name": "承讓人確認信", "url": "letter-of-transferee-generator"},
    ],
    "instrument-transfer-generator": [
        {"name": "首頁", "url": ""},
        {"name": "股份轉讓文件", "url": "shareholder-transfer"},
        {"name": "股份轉讓書", "url": "instrument-transfer-generator"},
    ],
    "audit-report-generator": [
        {"name": "首頁", "url": ""},
        {"name": "審計報告", "url": "audit-report-generator"},
    ],
    "nar1-generator": [
        {"name": "首頁", "url": ""},
        {"name": "NAR1 周年申報表", "url": "nar1-generator"},
    ],
    "nsc1-generator": [
        {"name": "首頁", "url": ""},
        {"name": "NSC1 股份申報表", "url": "nsc1-generator"},
    ],
    "company-name-change": [
        {"name": "首頁", "url": ""},
        {"name": "公司改名指南", "url": "company-name-change"},
    ],
    "company-name-change-generator/special-resolution": [
        {"name": "首頁", "url": ""},
        {"name": "公司改名指南", "url": "company-name-change"},
        {"name": "特別決議 PDF", "url": "company-name-change-generator/special-resolution"},
    ],
    "company-name-change-generator/nnc2": [
        {"name": "首頁", "url": ""},
        {"name": "公司改名指南", "url": "company-name-change"},
        {"name": "NNC2 表格", "url": "company-name-change-generator/nnc2"},
    ],
    "blog": [
        {"name": "首頁", "url": ""},
        {"name": "Blog", "url": "blog"},
    ],
}

added = 0
skipped = 0

for dirpath, dirnames, filenames in os.walk(BASE):
    skip_dirs = {'.git', 'scripts', 'templates', 'node_modules'}
    dirnames[:] = [d for d in dirnames if d not in skip_dirs]
    
    for fn in filenames:
        if not fn.endswith('.html') or fn == '404.html':
            continue
        
        path = os.path.join(dirpath, fn)
        
        # Determine breadcrumb key
        rel_dir = os.path.relpath(dirpath, BASE)
        if rel_dir == '.':
            if fn == 'index.html':
                key = ''
            else:
                continue  # skip root .html files that aren't index
        else:
            key = rel_dir
        
        # Blog posts get blog breadcrumb
        if key.startswith('blog') and fn != 'index.html':
            key = 'blog'
        
        if key not in BREADCRUMBS:
            skipped += 1
            continue
        
        with open(path, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # Skip if breadcrumb already exists
        if 'BreadcrumbList' in html:
            skipped += 1
            continue
        
        crumbs = BREADCRUMBS[key]
        breadcrumb_schema = {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": i + 1,
                    "name": c["name"],
                    "item": f"{BASE_URL}/{c['url']}" if c["url"] else BASE_URL
                }
                for i, c in enumerate(crumbs)
            ]
        }
        
        schema_tag = f'\n  <script type="application/ld+json">\n  {json.dumps(breadcrumb_schema, indent=2, ensure_ascii=False)}\n  </script>'
        
        # Insert before </head>
        if '</head>' not in html:
            skipped += 1
            continue
        
        html = html.replace('</head>', schema_tag + '\n  </head>')
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        
        added += 1
        short = path.replace(BASE, '').lstrip('/')
        print(f"✅ {short}")

print(f"\nDone! Added: {added}, Skipped: {skipped}")
