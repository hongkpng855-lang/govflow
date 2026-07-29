"""PDF pages for glossary, how-to-say table, URL map"""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 595, 842  # A4 portrait at 72 DPI

def get_font(size=14):
    paths = [
        "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
        "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/noto-cjk/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for p in paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

def new_page(title):
    img = Image.new("RGB", (W, H), (249, 250, 251))
    draw = ImageDraw.Draw(img)
    # Header bar
    draw.rectangle([0, 0, W, 50], fill=(27, 42, 74))
    draw.text((20, 12), "ESGov 溝通指南", fill=(201, 168, 76), font=get_font(18))
    # Title
    draw.text((20, 65), title, fill=(27, 42, 74), font=get_font(16))
    return img, draw

def wrap_text(text, font, max_w):
    """Simple word wrap - returns list of lines"""
    words = list(text)  # Chinese chars can be split per char
    lines = []
    cur = ""
    for ch in words:
        test = cur + ch
        if font.getbbox(test)[2] <= max_w:
            cur = test
        else:
            lines.append(cur)
            cur = ch
    if cur:
        lines.append(cur)
    return lines

# ═══════════════════════
# PAGE P4: 常用詞彙 (Glossary)
# ═══════════════════════
img4, d4 = new_page("📖 常用詞彙")
f14 = get_font(14)
f12 = get_font(12)
f10 = get_font(10)

terms = [
    ("產品一", "主頁第一個 product card", "股份轉讓完整指南 · /shareholder-transfer", (27,42,74), (201,168,76)),
    ("產品二", "主頁第二個 product card", "更改名稱完整指南 · /company-name-change", (27,42,74), (201,168,76)),
    ("產品三", "主頁第三個 product card / SCR 產品", "重要控制人登記冊 · /significant-controllers-register", (27,42,74), (201,168,76)),
    ("Step N", "SCR 產品頁嘅第 N 個步驟（1-7）", "例：「Step 3 嘅 document card」", (59,130,246), (219,234,254)),
    ("Generator", "可填寫 + 生成 PDF 嘅工具頁面", "例：「/scr-notice-generator 嘅表頭」", (147,51,234), (243,232,255)),
    ("Document Card", "SCR 頁面每份文件嘅 card", "頂圖 + title + 描述 + 制", (22,163,74), (220,252,231)),
    ("Blog card", "主頁/Blog listing 嘅文章 card", "emoji + title + 簡述 + date", (234,88,12), (255,237,213)),
    ("demoImage", "SCR document card 嘅頂部預覽圖", "有 Generator 嘅 steps 先有", (236,64,122), (252,231,243)),
    ("準備中", "未有真實範例嘅 placeholder", "顯示 🛠️ 準備中 badge", (202,138,4), (254,243,199)),
]

x, y = 20, 100
col_w = (W - 60) // 2  # two columns

# cards
cx, cy = 20, 90
for i, (name, desc, example, fg, bg) in enumerate(terms):
    col = i % 2
    row = i // 2
    cx = 20 + col * (col_w + 20)
    cy = 95 + row * 120
    
    # Card bg
    d4.rounded_rectangle([cx, cy, cx + col_w, cy + 105], radius=8, fill=(255,255,255), outline=(229,231,235))
    
    # Badge
    badge = name
    bw = f10.getbbox(badge)[2] + 16
    d4.rounded_rectangle([cx+8, cy+6, cx+8+bw, cy+6+22], radius=999, fill=bg)
    d4.text((cx+8+8, cy+6+3), badge, fill=fg, font=f10)
    
    # Description
    d4.text((cx+8, cy+35), desc, fill=(75,85,99), font=f12)
    d4.text((cx+8, cy+58), example, fill=(156,163,175), font=f10)

out4 = "/mnt/c/Users/hongk/Desktop/p4-glossary.pdf"
img4.save(out4, "PDF", resolution=200)
print(f"✅ Glossary PDF: {out4}")

# ═══════════════════════
# PAGE P5: 點樣同我講 (How to Say It table)
# ═══════════════════════
img5, d5 = new_page("💬 點樣同我講")
d5.text((20, 90), "用左邊嘅詞彙同我講，我就明你講邊度", fill=(107, 114, 128), font=f12)

rows = [
    ("產品一嘅步驟數改做 7", "主頁第一個 product card 嘅 badge 數字"),
    ("產品三 Step 2 嘅 document card 張圖", "SCR 頁面 Step 2 嘅「重要控制人識別檢查表」card 嘅頂圖"),
    ("Generator 頁面嘅真實範例擺喺左邊", "Generator 頁頂嘅 2 張 preview card 調位"),
    ("主頁 Blog 第 4 個 card 改 title", "主頁第四篇 blog 文章嘅標題"),
    ("Step 6 冇 generator image，show 準備中", "SCR Step 6 嘅文件因為冇真實範例圖，show 🛠️ 準備中"),
    ("Blog listing 第 2 頁嘅第 1 篇文", "blog/index.html?page=2 嘅第一篇 article card"),
]

# Table header
y = 120
col1, col2 = 20, 300
d5.rectangle([10, y, W-10, y+32], fill=(27, 42, 74))
d5.text((col1, y+6), "你講", fill=(201, 168, 76), font=f14)
d5.text((col2, y+6), "我會明", fill=(201, 168, 76), font=f14)
y += 32

for i, (you, me) in enumerate(rows):
    bg = (255,255,255) if i % 2 == 0 else (249,250,251)
    d5.rectangle([10, y, W-10, y+45], fill=bg)
    d5.text((col1, y+5), you, fill=(27,42,74), font=f12)
    d5.text((col2, y+5), me, fill=(75,85,99), font=f12)
    d5.line([(10, y+45), (W-10, y+45)], fill=(229,231,235), width=1)
    y += 45

out5 = "/mnt/c/Users/hongk/Desktop/p5-howtosay.pdf"
img5.save(out5, "PDF", resolution=200)
print(f"✅ How-to-say PDF: {out5}")

# ═══════════════════════
# PAGE P6: Generator URL 對照
# ═══════════════════════
img6, d6 = new_page("🗺️ Generator URL 對照")
d6.text((20, 90), "每個 SCR Step 對應嘅 Generator 頁面 URL", fill=(107, 114, 128), font=f12)

urls = [
    ("Step 1", "/scr-shareholder-analysis-generator"),
    ("Step 2", "/scr-identification-checklist-generator"),
    ("Step 3", "/scr-notice-generator"),
    ("Step 4", "/scr-data-collection-generator"),
    ("Step 5", "/scr-designated-rep-generator"),
    ("Step 6", "/scr-generator"),
    ("Step 7", "/scr-nr2-generator"),
    ("SCR 主頁", "/significant-controllers-register"),
]

x, y = 20, 120
for step, url in urls:
    bw = f12.getbbox(step)[2] + 16
    d6.rounded_rectangle([x, y, x+180, y+42], radius=8, fill=(255,255,255), outline=(229,231,235))
    d6.rounded_rectangle([x+6, y+6, x+6+bw, y+6+22], radius=999, fill=(27,42,74))
    d6.text((x+6+8, y+6+3), step, fill=(201,168,76), font=f10)
    d6.text((x+8, y+28), url, fill=(107,114,128), font=f10)
    y += 52

out6 = "/mnt/c/Users/hongk/Desktop/p6-urlmap.pdf"
img6.save(out6, "PDF", resolution=200)
print(f"✅ URL Map PDF: {out6}")

# ═══════════════════════
print("\n🎉 All reference PDFs done!")
