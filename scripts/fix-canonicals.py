#!/usr/bin/env python3
"""Fix all blog canonical tags to point to trailing-slash URLs (matching sitemap)."""
import os, re

BLOG = "/mnt/c/Users/hongk/Desktop/esgov/blog"

fixed = 0
errors = []
for d in sorted(os.listdir(BLOG)):
    idx = os.path.join(BLOG, d, "index.html")
    if not os.path.isfile(idx):
        continue
    with open(idx, encoding="utf-8") as f:
        content = f.read()

    m = re.search(r'<link rel="canonical" href="([^"]+)"', content)
    if not m:
        continue
    url = m.group(1)

    # Determine correct canonical: directory name + trailing slash
    correct = f"https://esgov.org/blog/{d}/"

    if url != correct:
        new_content = content.replace(m.group(0), f'<link rel="canonical" href="{correct}"')
        with open(idx, "w", encoding="utf-8") as f:
            f.write(new_content)
        fixed += 1
        print(f"✅ {d}: {url[:60]}... → {correct}")
    else:
        errors.append(f"OK {d}")

print(f"\n{fixed} canonical tags fixed")
