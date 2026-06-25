#!/usr/bin/env python3
"""
ESGov Sitemap Generator
Scan all .html files and generate sitemap.xml
Usage: python3 scripts/generate-sitemap.py
"""
import os, datetime
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

ROOT = '/mnt/c/Users/hongk/Desktop/esgov'
BASE_URL = 'https://esgov.org'
OUTPUT = os.path.join(ROOT, 'sitemap.xml')

# Priority mapping
PRIORITY = {
    '': 1.0,
    '/share-transfer/': 0.9,
    '/shareholder-transfer/': 0.9,
    '/sold-note-generator/': 0.8,
    '/instrument-transfer-generator/': 0.8,
    '/letter-of-transferee-generator/': 0.8,
    '/audit-report-generator/': 0.8,
    '/nar1-generator/': 0.8,
    '/nsc1-generator/': 0.8,
    '/company-name-change/': 0.7,
    '/company-name-change-generator/special-resolution/': 0.8,
    '/company-name-change-generator/nnc2/': 0.8,
    '/deregistration/': 0.9,
    '/deregistration-checklist-generator/': 0.8,
    '/deregistration-ir1263-generator/': 0.8,
    '/deregistration-ndr1-generator/': 0.8,
    '/deregistration-irc3113-generator/': 0.8,
    '/stamp-duty-calculator/': 0.8,
    '/articles-check-tool/': 0.8,
    '/post-transfer-checklist/': 0.8,
}

urlset = Element('urlset', xmlns='http://www.sitemaps.org/schemas/sitemap/0.9')

today = datetime.date.today().isoformat()

for dirpath, dirnames, filenames in os.walk(ROOT):
    # Skip .git, scripts, assets, templates
    skip = {'.git', 'scripts', 'templates', 'node_modules', 'assets', '.agents', 'references'}
    dirnames[:] = [d for d in dirnames if d not in skip]
    
    for fn in filenames:
        if not fn.endswith('.html'): continue
        if fn == '404.html': continue
        
        rel_dir = os.path.relpath(dirpath, ROOT)
        if rel_dir == '.':
            url_path = fn
        else:
            url_path = f'{rel_dir}/{fn}'
        
        # Skip old redirect stubs at root (e.g. shareholder-transfer.html)
        if rel_dir == '.' and fn != 'index.html':
            continue
        
        # Clean up index.html
        if fn == 'index.html':
            url_path = url_path.replace('/index.html', '')
            if url_path == 'index.html':
                url_path = ''
            else:
                url_path = url_path + '/'  # Add trailing slash for folder URLs
        
        # Strip .html extension for clean URLs (GitHub Pages serves without .html)
        if url_path.endswith('.html') and url_path != '':
            url_path = url_path[:-5]  # Remove .html
        
        full_url = f'{BASE_URL}/{url_path}'
        priority = PRIORITY.get(url_path, 0.5)
        
        url = SubElement(urlset, 'url')
        loc = SubElement(url, 'loc')
        loc.text = full_url
        lastmod = SubElement(url, 'lastmod')
        lastmod.text = today
        changefreq = SubElement(url, 'changefreq')
        changefreq.text = 'monthly'
        prio = SubElement(url, 'priority')
        prio.text = str(priority)

# Pretty print XML
xml_str = minidom.parseString(tostring(urlset)).toprettyxml(indent='  ')
with open(OUTPUT, 'w', encoding='utf-8') as f:
    f.write(xml_str)

count = len(urlset.findall('url'))
print(f'✅ sitemap.xml generated: {count} URLs')
