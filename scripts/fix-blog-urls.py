#!/usr/bin/env python3
"""Fix og:url and canonical in blog posts — strip .html extension."""

import os, re

BASE = "/mnt/c/Users/hongk/Desktop/esgov/blog"
fixed = 0

for fn in sorted(os.listdir(BASE)):
    if not fn.endswith('.html') or fn == 'index.html':
        continue
    
    path = os.path.join(BASE, fn)
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    original = html
    
    # Fix og:url — remove .html
    html = re.sub(
        r'(<meta\s+property=["\']og:url["\'][^>]*content=["\']https://esgov\.org/blog/[^"\']*)\.html(["\'][^>]*/>)',
        r'\1\2',
        html
    )
    
    # Fix canonical — remove .html
    html = re.sub(
        r'(<link\s+rel=["\']canonical["\'][^>]*href=["\']https://esgov\.org/blog/[^"\']*)\.html(["\'][^>]*/>)',
        r'\1\2',
        html
    )
    
    if html != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        fixed += 1
        print(f"✅ {fn}")

print(f"\nFixed: {fixed} blog posts")
