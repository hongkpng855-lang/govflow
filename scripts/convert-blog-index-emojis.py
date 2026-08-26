#!/usr/bin/env python3
"""Convert blog index page card emoji icons → Lucide (matching homepage card style).
Also converts 📅 dates, 🏷️ tags, 🆕 badge in card footer rows.
"""
import re

path = "/mnt/c/Users/hongk/Desktop/esgov/blog/index.html"
raw = open(path, encoding="utf-8").read()
orig = raw

# Card main icon mapping (emoji → lucide)
CARD_ICONS = {
    "\u2696\ufe0f": "scale", "\u2696": "scale",
    "\U0001F3E2": "building-2",                    # 🏢
    "\U0001F4CB": "clipboard-list",                # 📋
    "\U0001F4DC": "scroll-text",                   # 📜
    "\U0001F3E6": "landmark",                      # 🏦
    "\U0001F4B0": "coins",                         # 💰
    "\U0001F6E1\ufe0f": "shield", "\U0001F6E1": "shield",
    "\U0001F4C4": "file-text",                     # 📄
    "\U0001F504": "refresh-cw",                    # 🔄
    "\u270D\ufe0f": "pen-line", "\u270D": "pen-line",
    "\U0001F4BB": "monitor",                       # 💻
    "\u26A0\ufe0f": "triangle-alert", "\u26A0": "triangle-alert",
    "\U0001F4DD": "file-text",                     # 📝
    "\U0001F4CA": "bar-chart-3",                   # 📊
    "\U0001F512": "lock",                          # 🔒
    "\U0001F3F7\ufe0f": "tag", "\U0001F3F7": "tag",
    "\U0001F9FE": "receipt",                       # 🧾
    "\U0001F50D": "search",                        # 🔍
    "\U0001F3DB\ufe0f": "landmark", "\U0001F3DB": "landmark",
    "\U0001F30F": "globe",                         # 🌏
    "\U0001F310": "globe",                         # 🌐
    "\U0001F331": "sprout",                        # 🌱
    "\U0001F5A5\ufe0f": "monitor", "\U0001F5A5": "monitor",
    "\U0001F3DD\ufe0f": "palm-tree", "\U0001F3DD": "palm-tree",
    "\U0001F9EE": "calculator",                    # 🧮
    "\U0001F50F": "lock",                          # 🔏
    "\U0001F4C9": "trending-down",                 # 📉
    "\U0001F50E": "search",                        # 🔎
    "\U0001F9D1\u200d\U0001F4BC": "user-round",    # 🧑‍💼
    "\U0001F5F3\ufe0f": "vote", "\U0001F5F3": "vote",
    "\U0001F3C1": "flag",                          # 🏁
    "\U0001F4C5": "calendar",                      # 📅
    "\U0001F4BC": "briefcase",                     # 💼
    "\U0001F4EC": "mail-open",                     # 📬
    "\U0001F4DA": "book-open",                     # 📚
    "\U0001F4B5": "banknote",                      # 💵
    "\U0001F3D7\ufe0f": "construction", "\U0001F3D7": "construction",
    "\U0001F465": "users",                         # 👥
    "\u270F\ufe0f": "pencil", "\u270F": "pencil",
    "\U0001F4D1": "book-open",                     # 📑
    "\U0001F3E7": "landmark",                      # 🏧
    "\U0001F4C7": "contact",                       # 📇
    "\U0001F6AA": "door-open",                     # 🚪
    "\u2705": "check-circle",                       # ✅
    "\U0001F4C8": "trending-up",                   # 📈
    "\U0001F4CC": "pin",                           # 📌
}

# Card footer emoji (per-card metadata row): 📅 日期, 🏷️ tags, 🆕 最新
# These appear as <span>📅 2026.01.01</span> — replace emoji with small lucide icons
FOOTER_MAP = {
    "\U0001F4C5": "calendar",   # 📅
    "\U0001F3F7\ufe0f": "tag",  # 🏷️
    "\U0001F3F7": "tag",
}

def icon_tag(name, size="w-4 h-4"):
    return f'<i data-lucide="{name}" class="{size} inline-block align-middle" aria-hidden="true"></i>'

def card_icon_repl(m):
    """Replace the card emblem div content: <div class="text-3xl shrink-0 mt-1">EMOJI</div>"""
    emoji = m.group(1)
    name = CARD_ICONS.get(emoji)
    if not name:
        return m.group(0)
    # New card emblem: gold rounded box + lucide icon (matches homepage product cards)
    return (f'<div class="shrink-0 mt-1 w-9 h-9 rounded-lg bg-gold/10 flex items-center justify-center">'
            f'<i data-lucide="{name}" class="w-5 h-5 text-gold" aria-hidden="true"></i></div>')

# 1. Card emblem icons
raw = re.sub(
    r'<div class="text-3xl shrink-0 mt-1">([^<]+)</div>',
    card_icon_repl,
    raw
)

# 2. Footer date/tag emoji: <span>📅 2026.01.01</span> → calendar icon + text
#    pattern: <span>📅 YYYY.MM.DD</span>
raw = re.sub(
    r'<span>📅 ([^<]+)</span>',
    lambda m: f'<span>{icon_tag("calendar")} {m.group(1)}</span>',
    raw
)
#    🏷️ tags: <span>🏷️ tag1 · tag2</span>
raw = re.sub(
    r'<span>🏷️ ([^<]+)</span>',
    lambda m: f'<span>{icon_tag("tag")} {m.group(1)}</span>',
    raw
)
#    🆕 最新: <span class="font-bold text-gold">🆕 最新</span> → sparkles icon + text
raw = re.sub(
    r'<span class="font-bold text-gold">🆕 最新</span>',
    lambda m: f'<span class="font-bold text-gold">{icon_tag("sparkles", "w-3.5 h-3.5")} 最新</span>',
    raw
)

# 3. Remaining card emoji (leftover like ⚠️ in texts or misc) — catch single remaining emojis
#    in card metadata rows <span>⚠️ warning</span>
raw = re.sub(
    r'<span>⚠️ ([^<]+)</span>',
    lambda m: f'<span>{icon_tag("triangle-alert")} {m.group(1)}</span>',
    raw
)
raw = re.sub(
    r'<span>⚖️ ([^<]+)</span>',
    lambda m: f'<span>{icon_tag("scale")} {m.group(1)}</span>',
    raw
)

# 4. Ensure lucide CDN present in head
if "unpkg.com/lucide" not in raw:
    cdn = ('  <script defer src="https://unpkg.com/lucide@latest"></script>\n'
           '  <script>document.addEventListener("DOMContentLoaded",function(){lucide.createIcons()});</script>\n')
    raw = raw.replace("</head>", cdn + "</head>", 1)

open(path, "w", encoding="utf-8").write(raw)

# Report
import re as _re
remaining = _re.findall(r'[\u2600-\u27BF\u2B00-\u2BFF\U0001F300-\U0001FAFF\uFE0F]', raw)
print(f"Changed: {raw != orig}")
print(f"Remaining emojis: {len(remaining)}")
from collections import Counter
for e, n in Counter(remaining).most_common(15):
    print(f"  {e!r}: {n}")