#!/usr/bin/env python3
"""
ESGov SEO Checker
Check every HTML file for SEO best practices.
Usage: python3 scripts/seo-checker.py
"""
import os, re

ROOT = '/mnt/c/Users/hongk/Desktop/esgov'

def check_file(fp):
    issues = []
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    
    rel = os.path.relpath(fp, ROOT)
    
    # Meta title
    m = re.search(r'<title>(.*?)</title>', content)
    if not m:
        issues.append('❌ Missing <title>')
    else:
        t = m.group(1)
        if len(t) < 10:
            issues.append(f'⚠️ Title too short ({len(t)} chars): {t}')
        elif len(t) > 70:
            issues.append(f'⚠️ Title too long ({len(t)} chars)')
        if not t.startswith('ESGov'):
            issues.append(f'⚠️ Title should start with ESGov')
    
    # Meta description
    m = re.search(r'<meta name="description" content="([^"]*)"', content)
    if not m:
        issues.append('❌ Missing meta description')
    else:
        d = m.group(1)
        if len(d) < 50:
            issues.append(f'⚠️ Description too short ({len(d)} chars)')
        elif len(d) > 165:
            issues.append(f'⚠️ Description too long ({len(d)} chars)')
    
    # H1
    h1s = re.findall(r'<h1[^>]*>(.*?)</h1>', content, re.DOTALL)
    if len(h1s) == 0:
        issues.append('❌ Missing <h1>')
    elif len(h1s) > 1:
        issues.append(f'⚠️ Multiple <h1> tags ({len(h1s)})')
    
    # Image alt text
    imgs = re.findall(r'<img[^>]+>', content)
    for img in imgs:
        if 'alt=' not in img and 'alt="' not in img:
            issues.append('❌ Image missing alt text')
            break
    
    # OG tags
    og_title = re.search(r'<meta property="og:title"', content)
    og_desc = re.search(r'<meta property="og:description"', content)
    og_url = re.search(r'<meta property="og:url"', content)
    if not all([og_title, og_desc, og_url]):
        missing = []
        if not og_title: missing.append('og:title')
        if not og_desc: missing.append('og:description')
        if not og_url: missing.append('og:url')
        issues.append(f'⚠️ Missing OG tags: {", ".join(missing)}')
    
    # Canonical
    if not re.search(r'<link rel="canonical"', content):
        issues.append('⚠️ Missing canonical URL')
    
    # H2 structure
    h2s = re.findall(r'<h2[^>]*>', content)
    if len(h2s) == 0 and os.path.basename(fp) != '404.html':
        issues.append('⚠️ No <h2> tags')
    
    # Favicon
    if not re.search(r'rel="icon"|rel="shortcut icon"|rel="apple-touch-icon"', content):
        issues.append('⚠️ Missing favicon')
    
    return issues

total = 0
issues_found = 0

for dirpath, dirnames, filenames in os.walk(ROOT):
    if '.git' in dirpath: continue
    if 'scripts' in dirpath: continue
    for fn in filenames:
        if not fn.endswith('.html'): continue
        fp = os.path.join(dirpath, fn)
        issues = check_file(fp)
        total += 1
        if issues:
            issues_found += 1
            rel = os.path.relpath(fp, ROOT)
            print(f'\n📄 {rel}')
            for issue in issues:
                print(f'   {issue}')

print(f'\n{"="*40}')
print(f'Checked: {total} files')
print(f'Files with issues: {issues_found}')
print(f'✅ All clean!' if issues_found == 0 else f'⚠️ {issues_found} files need attention')
