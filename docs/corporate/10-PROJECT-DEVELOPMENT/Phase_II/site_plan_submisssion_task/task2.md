from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A3, landscape
from reportlab.lib import colors
from reportlab.lib.units import mm

def arrow(c, x1, y1, x2, y2, size=4, color=colors.black):
    c.setStrokeColor(color)
    c.line(x1, y1, x2, y2)
    # arrow head at (x2, y2)
    import math
    ang = math.atan2(y2 - y1, x2 - x1)
    left = (x2 - size * math.cos(ang - math.pi / 6),
            y2 - size * math.sin(ang - math.pi / 6))
    right = (x2 - size * math.cos(ang + math.pi / 6),
             y2 - size * math.sin(ang + math.pi / 6))
    c.line(x2, y2, left[0], left[1])
    c.line(x2, y2, right[0], right[1])

def dim_with_text(c, x1, y1, x2, y2, txt, off=0, horiz=True):
    # Draw dimension line with arrows and centered text
    if horiz:
        y1 += off; y2 += off
    else:
        x1 += off; x2 += off
    arrow(c, x1, y1, x2, y2)
    arrow(c, x2, y2, x1, y1)
    # place text centered
    if horiz:
        cx = (x1 + x2) / 2.0
        cy = y1 + 6
        c.setFont("Helvetica", 9)
        c.drawCentredString(cx, cy, txt)
    else:
        cx = x1 + 6
        cy = (y1 + y2) / 2.0
        c.saveState()
        c.translate(cx, cy)
        c.rotate(90)
        c.setFont("Helvetica", 9)
        c.drawCentredString(0, 0, txt)
        c.restoreState()

def draw_title_block(c, page_w, page_h, margin_l, margin_r, margin_b, block_h=32*mm):
    c.setLineWidth(0.8)
    c.setStrokeColor(colors.black)
    y0 = margin_b
    c.rect(margin_l, y0, page_w - margin_l - margin_r, block_h, stroke=1, fill=0)
    # vertical splits
    right = page_w - margin_r
    # Simple three-field layout: Description (big), Project/Client, Drawing info
    desc_w = (page_w - margin_l - margin_r) * 0.50
    proj_w = (page_w - margin_l - margin_r) * 0.25
    info_w = (page_w - margin_l - margin_r) * 0.25
    x1 = margin_l + desc_w
    x2 = x1 + proj_w
    c.line(x1, y0, x1, y0 + block_h)
    c.line(x2, y0, x2, y0 + block_h)
    # horizontal split in info area for metadata rows
    row_h = block_h / 3.0
    c.line(x2, y0 + row_h, right, y0 + row_h)
    c.line(x2, y0 + 2 * row_h, right, y0 + 2 * row_h)
    # Text
    pad = 6
    c.setFont("Helvetica-Bold", 10)
    c.drawString(margin_l + pad, y0 + block_h - 14, "DESCRIPTION:")
    c.setFont("Helvetica", 9)
    c.drawString(margin_l + pad, y0 + block_h - 28, "Typical wire-mesh fence panel and footing (NTS)")
    c.drawString(margin_l + pad, y0 + block_h - 42, "As-built structural design and compliance verification")

    c.setFont("Helvetica-Bold", 10)
    c.drawString(x1 + pad, y0 + block_h - 14, "PROJECT:")
    c.setFont("Helvetica", 9)
    c.drawString(x1 + pad, y0 + block_h - 28, "Perimeter Fencing and Gates (As-built)")
    c.drawString(x1 + pad, y0 + block_h - 42, "Location: NPA Lighter Terminal, Ikorodu")
    c.drawString(x1 + pad, y0 + block_h - 56, "Client: GK & A Logistics Services Ltd")

    c.setFont("Helvetica-Bold", 9)
    c.drawString(x2 + pad, y0 + 2*row_h + row_h - 14, "DRAWING TITLE")
    c.setFont("Helvetica", 9)
    c.drawString(x2 + pad, y0 + 2*row_h + 4, "Wire-Mesh Panel - Typical")
    c.setFont("Helvetica-Bold", 9)
    c.drawString(x2 + pad, y0 + row_h + row_h - 14, "SCALE")
    c.setFont("Helvetica", 9)
    c.drawString(x2 + pad, y0 + row_h + 4, "NTS")
    c.setFont("Helvetica-Bold", 9)
    c.drawString(x2 + pad, y0 + row_h - 14, "DATE")
    c.setFont("Helvetica", 9)
    from datetime import date
    c.drawString(x2 + pad, y0 + 4, date.today().isoformat())
    c.setFont("Helvetica-Bold", 9)
    c.drawRightString(page_w - margin_r - pad, y0 + 2*row_h + row_h - 14, "DRAWING No.")
    c.setFont("Helvetica", 9)
    c.drawRightString(page_w - margin_r - pad, y0 + 2*row_h + 4, "GKA-FEN-AB-001")
    c.setFont("Helvetica-Bold", 9)
    c.drawRightString(page_w - margin_r - pad, y0 + row_h + row_h - 14, "DRAWN / CHECK")
    c.setFont("Helvetica", 9)
    c.drawRightString(page_w - margin_r - pad, y0 + row_h + 4, "By: ———  /  Chk: ———")
    c.setFont("Helvetica-Bold", 9)
    c.drawRightString(page_w - margin_r - pad, y0 + row_h - 14, "REV")
    c.setFont("Helvetica", 9)
    c.drawRightString(page_w - margin_r - pad, y0 + 4, "A")

def draw_notes(c, x, y, w, h):
    c.setStrokeColor(colors.black)
    c.setLineWidth(0.6)
    c.rect(x, y, w, h, stroke=1, fill=0)
    pad = 8
    t = c.beginText()
    t.setTextOrigin(x + pad, y + h - pad - 2)
    t.setFont("Helvetica-Bold", 11)
    t.textLine("NOTES")
    t.setFont("Helvetica", 9)
    t.textLine("")
    t.setFont("Helvetica-Bold", 9)
    t.textLine("Scope:")
    t.setFont("Helvetica", 9)
    t.textLines("As-built structural design and compliance verification for approximately "
                "785 m of perimeter fencing and gates for GK & A Logistics Services Ltd at "
                "the NPA Lighter Terminal, Ikorodu.")
    t.textLine("")
    t.setFont("Helvetica-Bold", 9)
    t.textLine("Installed system:")
    t.setFont("Helvetica", 9)
    t.textLines("- 257 wire-mesh panels (≈ 2.44 m high × 3.05 m long; total area ≈ 1,914 m²)"
                " supported on 288 posts.")
    t.textLines("- Typical line-post footing 350×350×900 mm, C25/30; larger bases at ends, "
                "corners, strainers, and gates.")
    t.textLine("")
    t.setFont("Helvetica-Bold", 9)
    t.textLine("Outcome:")
    t.setFont("Helvetica", 9)
    t.textLines("With SHS 60×60×3.0 mm S355 line posts, mesh porosity typical of chain-link/"
                "weldmesh, and the specified foundations and coatings, the fence satisfies "
                "structural and durability requirements for the Ikorodu wind and marine-"
                "corrosion environment.")
    c.drawText(t)

def draw_typical_panel(c, x, y, panel_w_mm=220, panel_h_mm=None):
    # Proportion the panel to 3.05 m (w) × 2.44 m (h)
    if panel_h_mm is None:
        panel_h_mm = panel_w_mm * (2.44 / 3.05)

    # Convert to points
    pw = panel_w_mm * mm
    ph = panel_h_mm * mm

    # Ground line
    ground_y = y + 18 * mm
    c.setLineWidth(1.2)
    c.line(x - 20*mm, ground_y, x + pw + 20*mm, ground_y)

    # Posts (60×60×3 SHS) shown schematically
    post_w = 8 * mm
    left_post_x = x - post_w/2
    right_post_x = x + pw - post_w/2
    post_top = ground_y + ph
    post_bot = ground_y - 0   # above ground portion
    c.setFillColor(colors.black)
    c.rect(left_post_x, post_bot, post_w, ph, fill=0, stroke=1)
    c.rect(right_post_x, post_bot, post_w, ph, fill=0, stroke=1)

    # Footings 350×350×900 (typ.) schematic
    footing_w = 22 * mm
    footing_h = 28 * mm
    c.setLineWidth(0.8)
    c.rect(left_post_x + (post_w - footing_w)/2, ground_y - footing_h, footing_w, footing_h, fill=0, stroke=1)
    c.rect(right_post_x + (post_w - footing_w)/2, ground_y - footing_h, footing_w, footing_h, fill=0, stroke=1)

    # Mesh panel rectangle
    c.setLineWidth(1)
    c.rect(x, ground_y, pw, ph, fill=0, stroke=1)

    # Mesh hatch (light grid to hint wire mesh)
    c.setLineWidth(0.2)
    c.setStrokeColor(colors.grey)
    grid_spacing = 6  # points
    gx = x
    while gx <= x + pw:
        c.line(gx, ground_y, gx, ground_y + ph)
        gx += grid_spacing
    gy = ground_y
    while gy <= ground_y + ph:
        c.line(x, gy, x + pw, gy)
        gy += grid_spacing
    c.setStrokeColor(colors.black)

    # Labels
    c.setFont("Helvetica", 9)
    c.drawString(right_post_x + post_w + 6, ground_y + ph/2, "Wire-mesh panel")
    c.drawString(right_post_x + post_w + 6, ground_y + ph/2 - 14, "2.44 m height × 3.05 m length (typ.)")
    c.drawString(right_post_x + post_w + 6, ground_y - 10, "Existing ground level")
    c.drawString(left_post_x - 2, ground_y - footing_h - 14, "350×350×900 mm")
    c.drawString(left_post_x - 2, ground_y - footing_h - 26, "C25/30 mass concrete base (typ.)")
    c.drawString(left_post_x - 2, ground_y + ph + 8, "SHS 60×60×3.0 mm")
    c.drawString(left_post_x - 2, ground_y + ph - 4, "S355 line post (typ.)")

    # Horizontal dimension (panel length 3.05 m)
    dim_with_text(c, x, ground_y - 30, x + pw, ground_y - 30, "3.05 m", off=0, horiz=True)
    # Vertical dimension (panel height 2.44 m)
    dim_with_text(c, x - 30, ground_y, x - 30, ground_y + ph, "2.44 m", off=0, horiz=False)

    # Caption under the drawing
    c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(x + pw/2, ground_y - 48, "Typical Wire-Mesh Fence Panel (NTS)")

def main():
    c = canvas.Canvas("GK_A_Fence_AsBuilt.pdf", pagesize=landscape(A3))
    page_w, page_h = landscape(A3)

    margin_l = 18 * mm
    margin_r = 18 * mm
    margin_t = 14 * mm
    margin_b = 14 * mm

    # Title block
    block_h = 32 * mm
    draw_title_block(c, page_w, page_h, margin_l, margin_r, margin_b, block_h=block_h)

    # Notes box on left
    notes_w = 120 * mm
    notes_h = 90 * mm
    notes_x = margin_l
    notes_y = page_h - margin_t - notes_h
    draw_notes(c, notes_x, notes_y, notes_w, notes_h)

    # Typical panel drawing to the right
    draw_x = notes_x + notes_w + 18 * mm
    draw_y = notes_y - 10 * mm  # drop a bit to center
    draw_typical_panel(c, draw_x, draw_y, panel_w_mm=240)

    # Add a small legend for quantities
    c.setFont("Helvetica-Bold", 10)
    c.drawString(notes_x, notes_y - 28, "Quantities (As-built):")
    c.setFont("Helvetica", 9)
    c.drawString(notes_x, notes_y - 44, "- Panels: 257 pcs (≈ 1,914 m² total)")
    c.drawString(notes_x, notes_y - 58, "- Posts: 288 pcs (incl. ends/corners/strainers/gates)")

    # Footer disclaimer
    c.setFont("Helvetica", 8)
    c.setFillColor(colors.grey)
    c.drawString(margin_l, margin_b + block_h + 4, "All dimensions in metres unless noted. Do not scale from this drawing. NTS schematic.")
    c.setFillColor(colors.black)

    c.showPage()
    c.save()

if __name__ == "__main__":
    main()