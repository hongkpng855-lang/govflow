#!/usr/bin/env python3
"""Render CR guide key pages as high-res PNGs for use as demo images."""
import fitz
import os

PDF_PATH = "/mnt/c/Users/hongk/Desktop/esgov/assets/demo/Guidelines_scr_c.pdf"
OUT = "/mnt/c/Users/hongk/Desktop/esgov/assets/demo"
doc = fitz.open(PDF_PATH)

# Extract Annex pages as hi-res PNG
# Page 53-56: Figures 1-5 (shareholding structure diagrams)
# Page 81-87: Annex pages with forms

page_map = {
    53: "cr_fig1_direct_holding",   # Figures 1-2
    54: "cr_fig3_chain_ownership",   # Figure 3
    55: "cr_fig4_other_examples",    # Figure 4  
    56: "cr_fig5_excluded",          # Figure 5
    81: "cr_annex_g_p1",             # Annex G page 1
    82: "cr_annex_g_p2",
    83: "cr_annex_g_p3",
    84: "cr_annex_g_p4",
    85: "cr_annex_g_p5",
    86: "cr_annex_g_p6",
    87: "cr_annex_g_p7",
}

for page_num, name in page_map.items():
    page = doc[page_num - 1]  # 0-indexed
    # Render at 2x resolution (high quality)
    mat = fitz.Matrix(2, 2)
    pix = page.get_pixmap(matrix=mat)
    fpath = os.path.join(OUT, f"{name}.png")
    pix.save(fpath)
    print(f"Saved: {fpath} ({pix.width}x{pix.height}, {os.path.getsize(fpath)//1024}KB)")

doc.close()
print("Done!")
