#!/usr/bin/env python3
"""Deep SEO audit: check all 11 key pages across 12 dimensions."""

import os
import re
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent

KEY_PAGES = [
    "index.html",
    "shareholder-transfer/index.html",
    "sold-note-generator/index.html",
    "letter-of-transferee-generator/index.html",
    "audit-report-generator/index.html",
    "nar1-generator/index.html",
    "nsc1-generator/index.html",
    "instrument-transfer-generator/index.html",
    "company-name-change/index.html",
    "company-name-change-generator/special-resolution/index.html",
    "company-name-change-generator/nnc2/index.html",
]

DIMENSIONS = [
    "title", "title_len", "description", "desc_len", "h1_count",
    "h1_text", "h2_count", "canonical", "og_title", "og_desc",
    "og_url", "og_image", "favicon", "viewport", "html_lang",
    "jsonld", "img_alt_pct", "charset", "clean_urls"
]

def check_page(rel_path):
    full = BASE / rel_path
    if not full.exists():
        return {"error": f"NOT FOUND: {rel_path}"}

    html = full.read_text(encoding="utf-8")
    result = {"path": str(rel_path), "issues": [], "score": 100}
    pt = 100  # start perfect

    # Title
    m = re.search(r'<title>(.*?)</title>', html, re.DOTALL)
    title = m.group(1).strip() if m else ""
    tlen = len(title)
    result["title"] = title[:60] + ("..." if len(title) > 60 else "")
    result["title_len"] = tlen
    if not title:
        result["issues"].append("Missing <title>")
        pt -= 15
    elif tlen < 20:
        result["issues"].append(f"Title too short ({tlen} chars)")
        pt -= 5
    elif tlen < 30:
        result["issues"].append(f"Title could be longer ({tlen} chars)")
        pt -= 2
    elif tlen > 70:
        result["issues"].append(f"Title too long ({tlen} chars)")
        pt -= 3

    # Description
    m = re.search(r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']*)["\']', html)
    desc = m.group(1).strip() if m else ""
    dlen = len(desc)
    result["description"] = desc[:60] + ("..." if len(desc) > 60 else "")
    result["desc_len"] = dlen
    if not desc:
        result["issues"].append("Missing <meta description>")
        pt -= 12
    elif dlen < 50:
        result["issues"].append(f"Description too short ({dlen} chars)")
        pt -= 5
    elif dlen < 100:
        result["issues"].append(f"Description could be longer ({dlen} chars)")
        pt -= 2
    elif dlen > 170:
        result["issues"].append(f"Description too long ({dlen} chars)")
        pt -= 2

    # H1
    h1s = re.findall(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL)
    result["h1_count"] = len(h1s)
    result["h1_text"] = [h.strip()[:50] for h in h1s]
    if len(h1s) == 0:
        result["issues"].append("Missing <h1>")
        pt -= 12
    elif len(h1s) > 1:
        result["issues"].append(f"Multiple <h1> tags ({len(h1s)})")
        pt -= 6

    # H2
    h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', html, re.DOTALL)
    result["h2_count"] = len(h2s)

    # Canonical
    m = re.search(r'<link\s+rel=["\']canonical["\'][^>]*href=["\']([^"\']*)["\']', html)
    result["canonical"] = m.group(1) if m else ""
    if not m:
        result["issues"].append("Missing canonical link")
        pt -= 6

    # OG tags
    result["og_title"] = bool(re.search(r'<meta\s+property=["\']og:title["\']', html))
    result["og_desc"] = bool(re.search(r'<meta\s+property=["\']og:description["\']', html))
    result["og_url"] = bool(re.search(r'<meta\s+property=["\']og:url["\']', html))
    result["og_image"] = bool(re.search(r'<meta\s+property=["\']og:image["\']', html))
    og_missing = sum(1 for v in [result["og_title"], result["og_desc"], result["og_url"], result["og_image"]] if not v)
    if og_missing > 0:
        result["issues"].append(f"Missing {og_missing} OG tag(s)")
        pt -= 3 * og_missing

    # Favicon
    result["favicon"] = bool(re.search(r'<link[^>]*rel=["\'](?:shortcut )?icon["\']', html, re.I))
    if not result["favicon"]:
        result["issues"].append("Missing favicon")
        pt -= 3

    # Viewport
    result["viewport"] = bool(re.search(r'<meta\s+name=["\']viewport["\']', html))
    if not result["viewport"]:
        result["issues"].append("Missing viewport meta")
        pt -= 4

    # html lang
    m = re.search(r'<html[^>]*\slang=["\']([^"\']+)["\']', html)
    result["html_lang"] = m.group(1) if m else ""
    if not m:
        result["issues"].append("Missing html lang attribute")
        pt -= 3

    # JSON-LD
    jld = re.findall(r'<script\s+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', html, re.DOTALL)
    result["jsonld"] = len(jld)
    if not jld:
        result["issues"].append("Missing JSON-LD structured data")
        pt -= 6

    # Charset
    result["charset"] = bool(re.search(r'<meta[^>]*charset=', html))
    if not result["charset"]:
        result["issues"].append("Missing charset declaration")
        pt -= 3

    # Image alt
    imgs = re.findall(r'<img[^>]*>', html)
    total_imgs = len(imgs)
    alt_ok = sum(1 for img in imgs if re.search(r'alt=[\'"]', img))
    result["img_alt_pct"] = f"{alt_ok}/{total_imgs}" if total_imgs > 0 else "0/0"
    if total_imgs > 0 and alt_ok < total_imgs:
        missing_alt = total_imgs - alt_ok
        result["issues"].append(f"{missing_alt} image(s) missing alt text")
        pt -= 2 * missing_alt

    # Clean URLs (no .html in internal links)
    html_links = re.findall(r'href=["\']([^"\']*\.html)["\']', html)
    result["clean_urls"] = len(html_links)
    if html_links:
        sample = ", ".join(html_links[:3])
        result["issues"].append(f"{len(html_links)} internal link(s) with .html extension")
        pt -= 1 * min(len(html_links), 3)

    # Score clamp
    result["score"] = max(0, pt)
    return result


def print_score_table(results):
    print(f"\n{'Page':<55} {'Score':>6}  Issues")
    print("-" * 90)
    for r in results:
        path = r.get("path", "?")
        score = r.get("score", 0)
        issues = "; ".join(r.get("issues", [])) or "✅"
        print(f"{path:<55} {score:>3}/100  {issues}")

    avg = sum(r.get("score", 0) for r in results) / len(results)
    print(f"\n{'─'*90}")
    print(f"{'AVERAGE':<55} {avg:>5.1f}/100")
    print(f"{'TOTAL':<55} {sum(r.get('score', 0) for r in results)}/{len(results)*100}")
    print()


def export_report(results):
    report = {"timestamp": "manual", "results": results}
    report_path = BASE / "seo-audit-report.json"
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False))
    print(f"Report saved: {report_path}")


if __name__ == "__main__":
    print("=" * 80)
    print("DEEP SEO AUDIT — ESGov")
    print("=" * 80)

    results = []
    for page in KEY_PAGES:
        r = check_page(page)
        results.append(r)
        status = "❌" if r.get("issues") else "✅"
        print(f"\n{status} {page}")
        if r.get("issues"):
            for issue in r["issues"]:
                print(f"   ⚠ {issue}")
        print(f"   Score: {r.get('score', '?')}/100")

    print_score_table(results)
    export_report(results)
