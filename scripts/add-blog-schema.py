#!/usr/bin/env python3
"""Add JSON-LD Article schema to blog posts missing it."""

import os, re, json

BASE = "/mnt/c/Users/hongk/Desktop/esgov/blog"
BASE_URL = "https://esgov.org"

added = 0
skipped = 0

for fn in sorted(os.listdir(BASE)):
    if not fn.endswith('.html') or fn == 'index.html':
        continue
    
    path = os.path.join(BASE, fn)
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Skip if already has JSON-LD
    if re.search(r'application/ld\+json', html):
        skipped += 1
        continue
    
    # Extract title
    t = re.search(r'<title>(.*?)</title>', html, re.DOTALL)
    if not t:
        skipped += 1
        continue
    title = t.group(1).strip()
    
    # Extract description
    d = re.search(r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']*)["\']', html)
    desc = d.group(1).strip() if d else title
    
    # Build clean URL (remove .html)
    url_name = fn[:-5]  # remove .html
    
    schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": desc,
        "url": f"{BASE_URL}/blog/{url_name}",
        "author": {
            "@type": "Person",
            "name": "ESGov"
        },
        "publisher": {
            "@type": "Organization",
            "name": "ESGov"
        }
    }
    
    schema_html = f'\n  <script type="application/ld+json">\n  {json.dumps(schema, indent=2, ensure_ascii=False)}\n  </script>'
    
    # Insert before </head>
    html = html.replace('</head>', schema_html + '\n  </head>')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    added += 1
    print(f"✅ {fn}")

print(f"\nDone! Added: {added}, Skipped (had schema): {skipped}")
