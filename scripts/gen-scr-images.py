#!/usr/bin/env python3
"""Generate 7 SCR step demo images using Pillow."""
from PIL import Image, ImageDraw, ImageFont
import os, textwrap

OUT = "/mnt/c/Users/hongk/Desktop/esgov/assets/demo"
os.makedirs(OUT, exist_ok=True)

# Find a Chinese font
FONT_PATHS = [
    "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
    "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/truetype/noto/NotoSansSC-Regular.otf",
]
FONT = None
for p in FONT_PATHS:
    if os.path.exists(p):
        FONT = p
        break
if not FONT:
    # fallback: scan
    import subprocess
    r = subprocess.run(["fc-match", "-f", "%{file}", "sans:lang=zh"], capture_output=True, text=True)
    if r.stdout:
        FONT = r.stdout.strip()

print(f"Using font: {FONT}")

def make_img(step_num, title, fields, width=800, height=560):
    """Create a professional form-style demo image."""
    img = Image.new("RGB", (width, height), "#FFFFFF")
    draw = ImageDraw.Draw(img)

    # Title bar
    draw.rectangle([(0, 0), (width, 56)], fill="#1B2A4A")
    title_font = ImageFont.truetype(FONT, 22) if FONT else ImageFont.load_default()
    subtitle_font = ImageFont.truetype(FONT, 16) if FONT else ImageFont.load_default()
    body_font = ImageFont.truetype(FONT, 13) if FONT else ImageFont.load_default()
    small_font = ImageFont.truetype(FONT, 11) if FONT else ImageFont.load_default()

    draw.text((24, 14), f"步驟 {step_num}: {title}", fill="#C9A84C", font=title_font)

    # Info bar
    draw.rectangle([(0, 56), (width, 80)], fill="#F5F5F5")
    draw.text((24, 60), "ESGov 範例文件 · 僅供參考", fill="#888888", font=small_font)

    # Header accent
    draw.rectangle([(0, 80), (6, height)], fill="#1B2A4A")

    y = 100
    for label, value in fields:
        draw.text((24, y), label, fill="#1B2A4A", font=subtitle_font)
        y += 22
        # Value box
        draw.rectangle([(24, y), (width - 24, y + 28)], fill="#F8F8F8", outline="#DDDDDD")
        if isinstance(value, list):
            for v in value:
                draw.text((34, y + 6), v, fill="#333333", font=body_font)
                y += 28
        else:
            draw.text((34, y + 6), value, fill="#333333", font=body_font)
        y += 38

    # Footer
    draw.rectangle([(0, height - 36), (width, height)], fill="#1B2A4A")
    draw.text((24, height - 28), f"ESGov · scr-step{step_num}.png · 僅供參考示意", fill="#FFFFFF", font=small_font)
    draw.text((width - 140, height - 28), "📄 免費生成工具", fill="#C9A84C", font=small_font)

    # Watermark
    draw.text((width//2 - 100, height//2 - 20), "示 範 圖 片", fill="#EEEEEE", font=ImageFont.truetype(FONT, 36) if FONT else ImageFont.load_default())
    return img

# === STEP 1: 股權結構分析表 ===
img1 = make_img(1, "分析公司股權結構", [
    ("公司名稱", "ABC TRADING LIMITED"),
    ("公司編號", "1234567"),
    ("已發行股份總數", "10,000 股"),
    ("股東名稱／持股數／持股比例／投票權", [
        "張大文   5,000 股 (50%)   5,000 票   關聯方：張小文（兄弟）",
        "李志強   3,000 股 (30%)   3,000 票   關聯方：—",
        "王美玲   2,000 股 (20%)   2,000 票   關聯方：張大文（配偶）",
    ]),
    ("關連人士持股合計", "張大文（50%）+ 王美玲（20%）= 合共 70% 控制權"),
    ("初步判斷", "⚠️ 張大文透過直接 + 關連持股合計 70%，符合 25%+ 控制權條件，需進一步識別"),
])
img1.save(f"{OUT}/scr-step1.png")

# === STEP 2: 重要控制人識別檢查表 ===
img2 = make_img(2, "識別重要控制人（5項測試）", [
    ("公司名稱", "ABC TRADING LIMITED"),
    ("測試日期", "2026 年 6 月"),
    ("條件 1：直接或間接持有公司 25%+ 股份", "✅ 張大文（50%）、王美玲（20%）[與張大文關連合計 70%]"),
    ("條件 2：直接或間接持有公司 25%+ 表決權", "✅ 張大文（50% 投票權）— 通過"),
    ("條件 3：直接或間接有權委任或罷免董事會多數成員", "❌ 未有證據顯示"),
    ("條件 4：對公司有重大影響力或控制權", "✅ 張大文為唯一董事，對公司營運有重大影響力"),
    ("條件 5：對信託或合夥有重大影響力（如適用）", "❌ 不適用"),
    ("最終識別結果", "⚠️ 張大文（重要控制人）、王美玲（透過關連關係，需進一步確認）"),
])
img2.save(f"{OUT}/scr-step2.png")

# === STEP 3: 書面通知書 ===
img3 = make_img(3, "發出書面通知俾疑似控制人", [
    ("公司名稱", "ABC TRADING LIMITED (公司編號: 1234567)"),
    ("收件人", "張大文"),
    ("地址", "香港灣仔告士打道 123 號 20 樓"),
    ("通知日期", "2026 年 6 月 15 日"),
    ("法定依據", "公司條例 (第622章) 第 653ZH 條"),
    ("通知內容", [
        "根據公司條例第 653ZH 條，本公司有理由相信 閣下可能為公司之重要控制人。",
        "現根據法例要求，請 閣下於 1 個月內確認是否符合以下任何一項控制權條件：",
        "① 持有公司 25% 或以上已發行股份",
        "② 持有公司 25% 或以上表決權",
        "③ 有權委任或罷免董事會多數成員",
        "④ 對公司有重大影響力或控制權",
    ]),
    ("回覆期限", "2026 年 7 月 15 日或之前"),
    ("授權簽署", "____________________ (公司授權人)"),
])
img3.save(f"{OUT}/scr-step3.png")

# === STEP 4: 控制人資料收集表 ===
img4 = make_img(4, "收集控制人法定資料", [
    ("重要控制人姓名", "張大文"),
    ("身份證明文件", "香港身份證：A123456(7)"),
    ("住址", "香港北角電氣道 100 號 8 樓 B 室"),
    ("控制權性質", [
        "☑ 持有公司 25%+ 股份（直接持股 50%）",
        "☐ 持有公司 25%+ 表決權",
        "☐ 有權委任/罷免董事會多數成員",
        "☑ 對公司有重大影響力（唯一董事）",
    ]),
    ("成為重要控制人日期", "2020 年 3 月 1 日（公司註冊日）"),
    ("備註", "關連人士：王美玲（配偶）— 已發出書面通知確認中"),
])
img4.save(f"{OUT}/scr-step4.png")

# === STEP 5: 指定代表委任決議 ===
img5 = make_img(5, "委任指定代表（董事會決議）", [
    ("公司名稱", "ABC TRADING LIMITED (公司編號: 1234567)"),
    ("會議日期", "2026 年 6 月 15 日"),
    ("決議編號", "BR-2026-003"),
    ("決議內容", [
        "經董事會決議，正式委任下列人士為公司之指定代表（Designated Representative）：",
        "",
        "姓名：陳大明",
        "職位：公司秘書",
        "身份：TCSP 持牌人（牌照編號：TC123456）",
        "生效日期：2026 年 6 月 15 日",
        "",
        "職責：",
        "1. 備存及維護重要控制人登記冊 (SCR)",
        "2. 在辦公時間內提供 SCR 俾執法人員查閱",
        "3. 接獲查閱要求後 1 小時內提供 SCR",
    ]),
    ("董事簽署", "____________________ (張大文 — 董事)"),
])
img5.save(f"{OUT}/scr-step5.png")

# === STEP 6: SCR 登記冊 ===
# Based on CR Annex A format
img6 = make_img(6, "重要控制人登記冊（SCR）", [
    ("公司名稱", "ABC TRADING LIMITED (公司編號: 1234567)"),
    ("登記冊備存日期", "2026 年 6 月"),
    ("控制人姓名", "張大文"),
    ("控制權性質詳情", [
        "控制權條件：第 1 類（持 25%+ 股份）及第 4 類（重大影響力）",
        "持股比例：50%（直接持有 5,000 股 / 總發行 10,000 股）",
        "成為控制人日期：2020 年 3 月 1 日",
    ]),
    ("所需詳情", [
        "姓名：張大文",
        "身份證：A123456(7)",
        "住址：香港北角電氣道 100 號 8 樓 B 室",
        "通知日期：2026 年 6 月 15 日",
        "回覆日期：2026 年 6 月 22 日",
        "備註：—",
    ]),
    ("指定代表", "陳大明（公司秘書 · TCSP 持牌）"),
    ("登記冊存放地點", "☑ 公司註冊辦事處（香港灣仔告士打道 123 號）"),
])
img6.save(f"{OUT}/scr-step6.png")

# === STEP 7: NR2 指明地點通知書 ===
img7 = make_img(7, "備存同維護 SCR（NR2 通知書）", [
    ("公司名稱", "ABC TRADING LIMITED (公司編號: 1234567)"),
    ("表格類型", "NR2 — 指明地點通知書"),
    ("提交日期", "2026 年 6 月 15 日"),
    ("SCR 存放地點", [
        "☐ 公司註冊辦事處（無需提交 NR2）",
        "☑ 其他地點：香港北角電氣路 200 號 5 樓",
        "   （公司秘書辦公室）",
    ]),
    ("提交期限", "存放地點變更後 15 天內"),
    ("維護要求", [
        "✅ 資料變更後 7 天內更新登記冊",
        "✅ 備存期：公司解散後至少 6 年",
        "✅ 年度審查：每年檢查股權結構變動",
        "✅ 指定代表 1 小時內提供 SCR 查閱",
        "✅ NAR1 每年申報 SCR 存放地點",
    ]),
])
img7.save(f"{OUT}/scr-step7.png")

print("All 7 SCR demo images generated!")
for i in range(1, 8):
    path = f"{OUT}/scr-step{i}.png"
    size = os.path.getsize(path)
    print(f"  scr-step{i}.png  ({size//1024}KB)")
