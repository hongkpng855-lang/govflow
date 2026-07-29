"""Generate annotated guide PDFs — bakes labels + arrows onto screenshots"""
from PIL import Image, ImageDraw, ImageFont
import os, subprocess

W = 1265  # all base images are 1265px wide

def get_font(size=14):
    """Try to find a CJK-capable font"""
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

def add_label(draw, x, y, text, vocab_text, sub_text, arrow_dir="down",
              font_big=None, font_small=None):
    """Draw a navy label box with gold text + arrow tail pointing at (x,y)"""
    if font_big is None:
        font_big = get_font(13)
    if font_small is None:
        font_small = get_font(10)

    # Measure text
    line1 = f"呢度係 {text}"
    # Build full label text for box sizing
    if sub_text:
        lines = [line1, f"我叫「{vocab_text}」", sub_text]
    else:
        lines = [line1, f"我叫「{vocab_text}」"]

    # Approximate max width
    max_w = max(font_big.getbbox(l)[2] for l in lines[:2])
    if sub_text:
        max_w = max(max_w, font_small.getbbox(sub_text)[2])
    
    pad_x, pad_y = 10, 6
    box_w = max_w + pad_x * 2
    line_h = 18
    total_h = len(lines) * line_h + pad_y * 2

    # Position label box above the arrow (arrow points down from label to target)
    if arrow_dir == "down":
        bx = x - box_w // 2
        by = y - total_h - 14  # 14 = arrow height
    elif arrow_dir == "up":
        bx = x - box_w // 2
        by = y + 14
    elif arrow_dir == "left":
        bx = x - box_w - 14
        by = y - total_h // 2
    else:  # right
        bx = x + 14
        by = y - total_h // 2

    # Clamp to image bounds
    bx = max(2, min(bx, W - box_w - 2))
    by = max(2, by)

    # Draw box background
    draw.rounded_rectangle(
        [bx, by, bx + box_w, by + total_h],
        radius=6, fill=(27, 42, 74, 235)
    )
    
    # Draw text
    cy = by + pad_y
    draw.text((bx + pad_x, cy), line1, fill=(201, 168, 76), font=font_big)
    cy += line_h
    draw.text((bx + pad_x, cy), f"我叫「{vocab_text}」", fill=(251, 191, 36), font=font_big)
    cy += line_h
    if sub_text:
        draw.text((bx + pad_x, cy), sub_text, fill=(209, 213, 219), font=font_small)

    # Draw arrow tail (pointing down to target by default)
    arrow_color = (27, 42, 74, 235)
    if arrow_dir == "down":
        # Arrow from bottom-center of box down to target
        ax1, ay1 = bx + box_w // 2, by + total_h
        ax2, ay2 = x, y
        draw.line([(ax1, ay1), (ax2, ay2)], fill=arrow_color, width=2)
        # Arrowhead
        draw.polygon([
            (ax2, ay2),
            (ax2 - 5, ay2 - 10),
            (ax2 + 5, ay2 - 10)
        ], fill=arrow_color)
    elif arrow_dir == "up":
        ax1, ay1 = bx + box_w // 2, by
        ax2, ay2 = x, y
        draw.line([(ax1, ay1), (ax2, ay2)], fill=arrow_color, width=2)
        draw.polygon([
            (ax2, ay2),
            (ax2 - 5, ay2 + 10),
            (ax2 + 5, ay2 + 10)
        ], fill=arrow_color)
    elif arrow_dir == "left":
        ax1, ay1 = bx + box_w, by + total_h // 2
        ax2, ay2 = x, y
        draw.line([(ax1, ay1), (ax2, ay2)], fill=arrow_color, width=2)
        draw.polygon([
            (ax2, ay2),
            (ax2 + 10, ay2 - 5),
            (ax2 + 10, ay2 + 5)
        ], fill=arrow_color)
    else:  # right
        ax1, ay1 = bx, by + total_h // 2
        ax2, ay2 = x, y
        draw.line([(ax1, ay1), (ax2, ay2)], fill=arrow_color, width=2)
        draw.polygon([
            (ax2, ay2),
            (ax2 - 10, ay2 - 5),
            (ax2 - 10, ay2 + 5)
        ], fill=arrow_color)

# ══════════════════════════════════════
# PAGE 1: HOMEPAGE (guide-homepage.png)
# ══════════════════════════════════════
img = Image.open("/mnt/c/Users/hongk/Desktop/guide-homepage.png").convert("RGBA")
H = img.height
draw = ImageDraw.Draw(img)
font13 = get_font(13)
font10 = get_font(10)

annots = [
    # (x, y, text, vocab, sub, arrow_dir)
    (W//2, 40, "Navigation Bar", "導航欄", "Logo + link", "down"),
    (W//2, 490, "Hero H1", "主標題區", "「香港公司秘書文件 原來可以好簡單」", "down"),
    (W//2, 1620, "點樣運作？H2", "運作方式", "睇步驟 / 睇範例 / 下載模板", "down"),
    (W//2, 2420, "精選產品 H2", "產品區", "產品一 · 產品二 · 產品三", "down"),
    (W//4, 2820, "產品一", "產品一", "股份轉讓完整指南", "left"),
    (3*W//4, 2820, "產品二", "產品二", "更改名稱完整指南", "right"),
    (W//4, 3800, "產品三 (SCR)", "產品三", "重要控制人登記冊", "left"),
    (W//2, 4300, "Blog H2", "最新文章區", "「真實經歷 · 實用貼士」", "down"),
    (W//4, 4760, "Blog cards ×9", "文章卡片", "compact: emoji + title + 1行描述 + date", "left"),
    (W//2, H-60, "FAQ", "常見問題", "", "up"),
]

for x, y, text, vocab, sub, ad in annots:
    add_label(draw, x, y, text, vocab, sub, ad, font13, font10)

out_path = "/mnt/c/Users/hongk/Desktop/p1-homepage.pdf"
img.convert("RGB").save(out_path, "PDF", resolution=150)
print(f"✅ Homepage PDF: {out_path}")

# ══════════════════════════════════════
# PAGE 2: SCR (guide-scr.png)
# ══════════════════════════════════════
img2 = Image.open("/mnt/c/Users/hongk/Desktop/guide-scr.png").convert("RGBA")
H2 = img2.height
draw2 = ImageDraw.Draw(img2)

annots2 = [
    (W//2, 30, "Navigation", "導航欄", "", "down"),
    (380, 80, "Page Title H1", "頁面標題", "重要控制人登記冊(SCR)完整指南", "down"),
    (50, 300, "Steps Sidebar", "步驟欄", "Step 1–7，撳吓轉 step", "left"),
    (400, 300, "Step Content", "步驟內容區", "當前 step 嘅說明 + 文件", "down"),
    (400, 600, "詳細說明", "教學文字", "step 嘅文字教學內容", "down"),
    (400, 1150, "Document Card", "文件卡片", "需要填寫嘅文件", "down"),
    (800, 1200, "demoImage", "範例預覽圖", "有 Generator → 顯示圖片", "right"),
    (400, 1500, "Generator Button", "生成制", "「填寫 + 生成 PDF」", "down"),
    (400, 1660, "常見錯誤", "錯誤提醒", "", "down"),
    (400, 1800, "下一步制", "下一步", "", "down"),
]

for x, y, text, vocab, sub, ad in annots2:
    add_label(draw2, x, y, text, vocab, sub, ad, font13, font10)

out_path2 = "/mnt/c/Users/hongk/Desktop/p2-scr.pdf"
img2.convert("RGB").save(out_path2, "PDF", resolution=150)
print(f"✅ SCR PDF: {out_path2}")

# ══════════════════════════════════════
# PAGE 3: GENERATOR (guide-generator.png)
# ══════════════════════════════════════
img3 = Image.open("/mnt/c/Users/hongk/Desktop/guide-generator.png").convert("RGBA")
H3 = img3.height
draw3 = ImageDraw.Draw(img3)

annots3 = [
    (W//2, 30, "Navigation", "導航欄", "", "down"),
    (W//2, 90, "Preview Card ×2", "預覽卡片", "左：真實範例  右：可修改模板", "down"),
    (W//2, 380, "常見錯誤", "填表須知", "填表前必睇", "down"),
    (W//2, 540, "可編輯表單", "輸入表格", "公司名、股東資料、持股比例", "down"),
    (W//2, 1020, "股東表格", "股東列表", "可加減行數", "down"),
    (W//2, 1400, "分析結果", "結果區域", "判斷 + 簽署欄", "down"),
    (W//2, 1680, "下載制", "下載按鈕", "📄 下載 PDF", "down"),
    (W//2, H3-40, "返回連結", "返回制", "← 返回指南", "up"),
]

for x, y, text, vocab, sub, ad in annots3:
    add_label(draw3, x, y, text, vocab, sub, ad, font13, font10)

out_path3 = "/mnt/c/Users/hongk/Desktop/p3-generator.pdf"
img3.convert("RGB").save(out_path3, "PDF", resolution=150)
print(f"✅ Generator PDF: {out_path3}")

print("\n🎉 All PDFs generated!")
