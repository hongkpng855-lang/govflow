#!/usr/bin/env python3
"""Convert emoji icons in all blog articles to Lucide SVG icons (batch).
Follows blog-seo-pipeline-sop.md 3a-2 icon guidelines.
Text-natural emojis (☕ 請飲咖啡等) are EXCLUDED per SOP ("正文自然用到嘅除外").
"""
import os, re, glob

BLOG = "/mnt/c/Users/hongk/Desktop/esgov/blog"

# Emoji → Lucide mapping (icon purposes only)
ICON_MAP = {
    "\u2705": "check-circle",        # ✅
    "\u274C": "circle-x",            # ❌
    "\u26A0\uFE0F": "triangle-alert", # ⚠️ (with VS16)
    "\u26A0": "triangle-alert",       # ⚠ (no VS16)
    "\u2192": "arrow-right",          # →
    "\u2190": "arrow-left",           # ←
    "\u2610": "square",               # ☐ checkbox
    "\u270D\uFE0F": "pen-line",       # ✍️
    "\u270D": "pen-line",             # ✍
    "\u270F\uFE0F": "pencil",         # ✏️
    "\u270F": "pencil",               # ✏
    "\u2753": "circle-help",          # ❓
    "\u2696\uFE0F": "scale",          # ⚖️
    "\u2696": "scale",                # ⚖
    "\u2713": "check",                # ✓
    "\u2714": "check",                # ✔
    "\u2B07": "arrow-down",           # ⬇
    "\u2796": "minus",                # ➖
}

# Emojis that are natural text (keep as-is)
KEEP_EMOJI = {"\u2615"}  # ☕ 請飲咖啡

# Common pattern for icon usage: emoji sits at start of list item, box, or after tag
# e.g. <li>✅ 完成</li>, <strong>❌ 錯誤</strong>, <p>💡 免費範本

def add_lucide_cdn(html):
    """Add lucide CDN + init script to head if missing."""
    if "unpkg.com/lucide" in html:
        return html, False
    # Insert before </head>
    cdn = ('  <script defer src="https://unpkg.com/lucide@latest"></script>\n'
           '  <script>document.addEventListener("DOMContentLoaded",function(){lucide.createIcons()});</script>\n')
    if "</head>" in html:
        html = html.replace("</head>", cdn + "</head>", 1)
        return html, True
    return html, False

def replace_emoji_icon(match):
    """Replace an emoji icon with a Lucide <i> tag."""
    emoji = match.group(0)
    name = ICON_MAP.get(emoji)
    if not name:
        return emoji
    return f'<i data-lucide="{name}" class="w-4 h-4 inline-block align-middle" aria-hidden="true"></i>'

def process_article(path):
    raw = open(path, encoding="utf-8").read()
    orig = raw

    # 1. Add lucide CDN
    raw, added_cdn = add_lucide_cdn(raw)

    # 2. Replace emoji icons (only icon-purpose emojis)
    # Build regex from icon map keys (longest first)
    keys = sorted(ICON_MAP.keys(), key=len, reverse=True)
    pattern = re.compile("|".join(re.escape(k) for k in keys))
    raw = pattern.sub(replace_emoji_icon, raw)

    if raw != orig:
        open(path, "w", encoding="utf-8").write(raw)
        return True, added_cdn
    return False, added_cdn

def main():
    total_files = 0
    total_icons = 0
    changed = 0
    for idx in sorted(glob.glob(os.path.join(BLOG, "*", "index.html"))):
        total_files += 1
        changed_flag, cdn = process_article(idx)
        if changed_flag:
            changed += 1
        # Count icons added
        html = open(idx, encoding="utf-8").read()
        icons = len(re.findall(r'data-lucide="(check-circle|circle-x|triangle-alert|arrow-right|arrow-left|square|pen-line|pencil|circle-help|scale|arrow-down|minus)"', html))
        total_icons += icons

    print(f"Articles scanned: {total_files}")
    print(f"Articles changed: {changed}")
    print(f"Lucide icon tags (new set): {total_icons}")

    # Remaining emoji check
    remaining = 0
    for idx in glob.glob(os.path.join(BLOG, "*", "index.html")):
        raw = open(idx, encoding="utf-8").read()
        for k in ICON_MAP:
            remaining += raw.count(k) if k else 0
    print(f"Remaining icon emojis: {remaining}")

if __name__ == "__main__":
    main()