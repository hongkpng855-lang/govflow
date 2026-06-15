#!/usr/bin/env python3
"""Extract figures and annex pages from CR SCR guidelines PDF."""
import fitz  # PyMuPDF
import os

PDF_PATH = "/mnt/c/Users/hongk/Desktop/esgov/assets/demo/Guidelines_scr_c.pdf"
OUT = "/mnt/c/Users/hongk/Desktop/esgov/assets/demo"

doc = fitz.open(PDF_PATH)
print(f"PDF has {len(doc)} pages")

# Key pages of interest:
# - Annex A: SCR register format (pages ~24-25)
# - Annex B: Figures 1-5 (shareholding structure diagrams)
# - Annex C: Extra matters wording
# - Annex D: Notice format
# - Annex E: Nature of control wording
# - Flow diagrams

# Extract all images embedded in PDF
for page_num in range(len(doc)):
    page = doc[page_num]
    images = page.get_images(full=True)
    if images:
        print(f"Page {page_num+1}: {len(images)} images")
        for img_idx, img in enumerate(images):
            xref = img[0]
            base_image = doc.extract_image(xref)
            img_bytes = base_image["image"]
            ext = base_image["ext"]
            # Save with descriptive name
            fname = f"cr_guide_p{page_num+1}_img{img_idx+1}.{ext}"
            fpath = os.path.join(OUT, fname)
            with open(fpath, "wb") as f:
                f.write(img_bytes)
            print(f"  Saved: {fname} ({len(img_bytes)//1024}KB)")

# Also render key pages as PNG for reference
key_pages = {
    1: "cr_guide_cover",
    2: "cr_guide_toc",
    # Figures/Body pages
}

# Find Annex pages by scanning text
print("\n--- Scanning for Annexes ---")
for page_num in range(len(doc)):
    page = doc[page_num]
    text = page.get_text()
    if "附件" in text or "Annex" in text or "圖" in text:
        lines = [l.strip() for l in text.split('\n') if l.strip()]
        key_lines = [l for l in lines if any(k in l for k in ['附件','Annex','圖','圖1','圖2','Figure','範例'])]
        if key_lines:
            print(f"Page {page_num+1}: {' | '.join(key_lines[:3])}")

doc.close()
print("\nDone!")
