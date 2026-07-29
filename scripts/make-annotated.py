"""ESGov Guide PDF — accurate annotations based on live site element coordinates"""
from PIL import Image, ImageDraw, ImageFont
import os

FONT_PATH = "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc"
IMG_DIR = "/mnt/c/Users/hongk/Desktop"

def get_font(size):
    return ImageFont.truetype(FONT_PATH, size)

def add_rounded_box(draw, x, y, w, h, r=6, fill=(27,42,74,230)):
    draw.rounded_rectangle([x, y, x+w, y+h], radius=r, fill=fill)

def draw_arrow(draw, x1, y1, x2, y2, color=(27,42,74,230)):
    """Draw line + arrowhead from (x1,y1) to (x2,y2)"""
    draw.line([(x1,y1), (x2,y2)], fill=color, width=2)
    # Arrowhead at (x2,y2) pointing in direction from (x1,y1)
    dx, dy = x2-x1, y2-y1
    length = (dx*dx + dy*dy)**0.5
    if length == 0: return
    ux, uy = dx/length, dy/length
    # Arrowhead triangle
    hx, hy = 8, 5
    p1 = (x2, y2)
    p2 = (x2 - ux*hx - uy*hy, y2 - uy*hx + ux*hy)
    p3 = (x2 - ux*hx + uy*hy, y2 - uy*hx - ux*hy)
    draw.polygon([p1, p2, p3], fill=color)

def add_label(draw, target_x, target_y, title, vocab, sub="", direction="down",
              font_big=None, font_small=None):
    """Draw navy label with arrow pointing at (target_x, target_y)"""
    if font_big is None: font_big = get_font(13)
    if font_small is None: font_small = get_font(10)
    
    lines = [f"呢度係 {title}"]
    if vocab:
        lines.append(f"我叫「{vocab}」")
    if sub:
        lines.append(sub)
    
    # Measure label box
    pad_x, pad_y = 8, 5
    line_h = 17
    max_w = max(font_big.getbbox(lines[0])[2], 
                font_big.getbbox(lines[1])[2] if len(lines)>1 else 0,
                font_small.getbbox(sub)[2] if sub else 0)
    bw = max_w + pad_x*2
    bh = len(lines)*line_h + pad_y*2
    
    # Position label box relative to target
    gap = 14  # arrow length
    if direction == "down":
        # Label above target, arrow points down
        by = target_y - bh - gap
        bx = target_x - bw//2
        ax1, ay1 = bx + bw//2, by + bh
        ax2, ay2 = target_x, target_y
    elif direction == "up":
        by = target_y + gap
        bx = target_x - bw//2
        ax1, ay1 = bx + bw//2, by
        ax2, ay2 = target_x, target_y
    elif direction == "left":
        bx = target_x - bw - gap
        by = target_y - bh//2
        ax1, ay1 = bx + bw, by + bh//2
        ax2, ay2 = target_x, target_y
    else:  # right
        bx = target_x + gap
        by = target_y - bh//2
        ax1, ay1 = bx, by + bh//2
        ax2, ay2 = target_x, target_y
    
    # Clamp to image bounds
    img_w, img_h = 1265, 5041  # homepage
    bx = max(2, min(bx, img_w - bw - 2))
    by = max(2, by)
    
    # Draw background box
    draw.rounded_rectangle([bx, by, bx+bw, by+bh], radius=6, fill=(27,42,74,235))
    
    # Text
    cy = by + pad_y
    draw.text((bx+pad_x, cy), lines[0], fill=(201,168,76), font=font_big)
    cy += line_h
    if len(lines) > 1:
        draw.text((bx+pad_x, cy), lines[1], fill=(251,191,36), font=font_big)
        cy += line_h
    if sub:
        draw.text((bx+pad_x, cy), sub, fill=(209,213,219), font=font_small)
    
    # Arrow
    draw_arrow(draw, ax1, ay1, ax2, ay2)


# ══════════════════════════════════════
# HOMEPAGE — 1265x5041
# ══════════════════════════════════════
print("🏠 Processing homepage...")
img = Image.open(os.path.join(IMG_DIR, "guide-homepage.png")).convert("RGBA")
d = ImageDraw.Draw(img)
fb = get_font(13)
fs = get_font(10)

cx = 633  # content center x on 1265px image

# Based on live site element coordinates (page-relative y on 5041px tall page)
annotations_home = [
    # (target_x, target_y, title, vocab, sub, direction)
    (cx, 26,     "Navigation Bar", "導航欄", "Logo + link", "down"),
    (cx, 250,    "Hero H1", "主標題區", "「香港公司秘書文件 原來可以好簡單」", "down"),
    (cx, 920,    "點樣運作？", "運作方式", "睇步驟 · 睇範例 · 下載模板", "down"),
    (cx, 1310,   "精選產品 H2", "產品區", "🔥 精選產品 — 人氣最高 · 全部免費 🆓", "down"),
    (240, 1650,  "產品一", "產品一", "香港有限公司股份轉讓完整指南 · 5步驟", "left"),
    (850, 1650,  "產品二", "產品二", "香港有限公司更改名稱完整指南 · 5步驟", "right"),
    (240, 2150,  "產品三 (SCR)", "產品三", "重要控制人登記冊 · 免費睇全部", "left"),
    (cx, 2700,   "Blog H2", "最新文章區", "「真實經歷 · 實用貼士」 — 最新文章", "down"),
    (300, 3000,  "Blog cards ×9", "文章卡片", "emoji + title + 1行描述 + date", "right"),
    (cx, 3820,   "FAQ", "常見問題", "常見問題", "down"),
    (cx, 4600,   "Footer", "頁尾", "☕ 請咖啡 · Email", "down"),
]

for x, y, title, vocab, sub, ddir in annotations_home:
    add_label(d, x, y, title, vocab, sub, ddir, fb, fs)

# Save a cropped version — split into 2 pages for readability
# Page 1: top to below products (~y=0 to y=2650)
img_p1 = img.crop((0, 0, 1265, 2650))
out_p1 = os.path.join(IMG_DIR, "p1-homepage-annotated.png")
img_p1.save(out_p1)
print(f"  → Homepage top half saved ({img_p1.size})")

# Page 2: blog to footer (~y=2600 to y=5041)
img_p2 = img.crop((0, 2600, 1265, 5041))
out_p2 = os.path.join(IMG_DIR, "p2-blog-faq.png")
img_p2.save(out_p2)
print(f"  → Blog+FAQ saved ({img_p2.size})")


# ══════════════════════════════════════
# SCR PAGE — 1265x1978
# ══════════════════════════════════════
print("📋 Processing SCR page...")
img2 = Image.open(os.path.join(IMG_DIR, "guide-scr.png")).convert("RGBA")
d2 = ImageDraw.Draw(img2)
w2, h2 = 1265, 1978
c2x = 633  # content center

# For SCR, I need positions. Let me estimate from the snapshot data
annotations_scr = [
    (c2x, 25,    "Navigation Bar", "導航欄", "常用詞彙 · 精選產品 · Blog", "down"),
    (c2x, 90,    "Page Title H1", "頁面標題", "重要控制人登記冊 (SCR) 完整指南", "down"),
    (100, 230,   "Steps Sidebar", "步驟欄", "Step 1–7 · 撳吓轉 step", "left"),
    (400, 230,   "Step Content", "步驟內容區", "當前 step 嘅說明 + 文件", "down"),
    (400, 500,   "詳細說明 Text", "教學文字", "step 嘅文字教學內容", "down"),
    (400, 900,   "Document Card", "文件卡片", "需要填寫嘅文件 — 頂圖 + title + 描述 + 制", "down"),
    (800, 950,   "demoImage", "範例預覽圖", "有 Generator → 顯示圖片\n冇 → show 🛠️ 準備中", "right"),
    (400, 1300,  "Generator Button", "生成制", "「填寫 + 生成 PDF」", "down"),
    (400, 1550,  "常見錯誤提醒", "錯誤提醒", "常見錯誤提示", "down"),
    (400, 1730,  "下一步制", "下一步", "→ 下一步", "down"),
]

for x, y, title, vocab, sub, ddir in annotations_scr:
    add_label(d2, x, y, title, vocab, sub, ddir, fb, fs)

out_scr = os.path.join(IMG_DIR, "p2-scr-annotated.png")
img2.save(out_scr)
print(f"  → SCR saved ({img2.size})")


# ══════════════════════════════════════
# GENERATOR PAGE — 1265x1880
# ══════════════════════════════════════
print("⚙️ Processing Generator page...")
img3 = Image.open(os.path.join(IMG_DIR, "guide-generator.png")).convert("RGBA")
d3 = ImageDraw.Draw(img3)
w3, h3 = 1265, 1880

annotations_gen = [
    (c2x, 25,    "Navigation Bar", "導航欄", "", "down"),
    (c2x, 90,    "Preview Card ×2", "預覽卡片", "左：真實案例（範例圖片）· 右：可修改文件（同款圖片）", "down"),
    (c2x, 310,   "常見錯誤", "填表須知", "填表前必睇", "down"),
    (c2x, 480,   "可編輯表單", "輸入表格", "公司名、股東資料、持股比例", "down"),
    (c2x, 900,   "股東表格", "股東列表", "可加減行數", "down"),
    (c2x, 1300,  "分析結果", "結果區域", "判斷 + 簽署欄", "down"),
    (c2x, 1600,  "下載制", "下載按鈕", "📄 下載 PDF", "down"),
    (c2x, h3-35, "返回連結", "返回制", "← 返回指南", "up"),
]

for x, y, title, vocab, sub, ddir in annotations_gen:
    add_label(d3, x, y, title, vocab, sub, ddir, fb, fs)

out_gen = os.path.join(IMG_DIR, "p3-generator-annotated.png")
img3.save(out_gen)
print(f"  → Generator saved ({img3.size})")

print("\n✅ All annotated images done!")
