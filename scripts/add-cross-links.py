#!/usr/bin/env python3
"""Add relevant tool links to blog posts based on content keywords."""

import os, re

BASE = "/mnt/c/Users/hongk/Desktop/esgov"
BASE_URL = "https://esgov.org"

# Link definitions: (keyword, link_text, url)
LINKS = [
    ("股份轉讓", '📄 免費使用 ESGov 股份轉讓文件生成工具', 'https://esgov.org/shareholder-transfer/'),
    ("轉讓股份", '📄 免費使用 ESGov 股份轉讓文件生成工具', 'https://esgov.org/shareholder-transfer/'),
    ("股權轉讓", '📄 免費使用 ESGov 股份轉讓文件生成工具', 'https://esgov.org/shareholder-transfer/'),
    ("公司改名", '🛠️ ESGov 公司改名特別決議 PDF 生成工具', 'https://esgov.org/company-name-change-generator/special-resolution/'),
    ("更改名稱", '🛠️ ESGov 公司改名特別決議 PDF 生成工具', 'https://esgov.org/company-name-change-generator/special-resolution/'),
    ("審計", '📊 ESGov 審計報告範例下載', 'https://esgov.org/audit-report-generator/'),
    ("核數", '📊 ESGov 審計報告範例下載', 'https://esgov.org/audit-report-generator/'),
    ("周年申報", '📋 ESGov NAR1 周年申報表 PDF 填寫工具', 'https://esgov.org/nar1-generator/'),
    ("Sold Note", '📝 ESGov Sold Note 買賣單 PDF 生成工具', 'https://esgov.org/sold-note-generator/'),
    ("Instrument of Transfer", '📝 ESGov 股份轉讓書 PDF 生成工具', 'https://esgov.org/instrument-transfer-generator/'),
]

added = 0
blog_dir = f"{BASE}/blog"

for fn in os.listdir(blog_dir):
    if not fn.endswith('.html') or fn == 'index.html':
        continue
    
    path = f"{blog_dir}/{fn}"
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Find matching keywords (case-insensitive)
    matching_links = set()
    for keyword, link_text, url in LINKS:
        if keyword.lower() in html.lower():
            matching_links.add((link_text, url))
    
    if not matching_links:
        continue
    
    # Build link section HTML
    links_html = '\n\n  <!-- Auto-added: related tool links -->\n  <div class="max-w-3xl mx-auto px-4 mt-10 mb-8">\n    <div class="bg-navy/5 border border-navy/10 rounded-xl p-6">\n      <h3 class="text-lg font-bold text-navy mb-4">📍 相關免費工具</h3>\n      <div class="space-y-3">\n'
    
    for link_text, url in matching_links:
        links_html += f'        <a href="{url}" class="block bg-white border border-navy/10 hover:border-gold/40 hover:shadow-md transition rounded-lg px-4 py-3 text-navy font-medium">{link_text}</a>\n'
    
    links_html += '      </div>\n    </div>\n  </div>\n\n'
    
    # Insert before </body>
    if '</body>' not in html:
        continue
    
    # Check if already has this section
    if 'Auto-added: related tool links' in html:
        continue
    
    html = html.replace('</body>', links_html + '</body>')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    added += 1
    print(f"✅ {fn} ({len(matching_links)} links)")

print(f"\nDone! Added tool links to: {added} blog posts")
