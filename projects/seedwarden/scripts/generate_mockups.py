"""
generate_mockups.py
Renders product pages onto device frames and saves high-res PNGs suitable for
Etsy listings (>=2000px long side).

Frame design: drawn programmatically with Pillow — no external assets, no
licensing concerns.

Usage:
    uv run python projects/seedwarden/scripts/generate_mockups.py
    uv run python projects/seedwarden/scripts/generate_mockups.py --frame portrait
    uv run python projects/seedwarden/scripts/generate_mockups.py --frame interior

Options:
    --frame portrait (default: tablet)
        Draw a portrait smartphone frame (iPhone 13 proportions: 390x844px screen
        area) instead of the default tablet frame. Output files are named
        {stem}_phone.png and saved to the same output directory.

        Phone frame dimensions: 440x950px phone body (within a 2400x2400 canvas),
        with a 390x844px screen inset 25px from each screen edge. Frame color is
        matte black with a subtle highlight and drop shadow matching the tablet
        style.

    --frame interior
        Draw a tablet frame showing a 2x2 grid of interior pages (pages 2-5),
        demonstrating content depth and product substance. Output files are named
        {stem}_interior.png. Useful for showing product variety and value beyond
        the cover.

        Interior grid shows four consecutive pages in a 2x2 layout with subtle
        dividers. Each page is scaled to fit, showing actual content from the
        product interior.
"""

import argparse
import math
import pathlib
import sys

import pypdfium2 as pdfium
from PIL import Image, ImageDraw, ImageFilter

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
REPO_ROOT = pathlib.Path("/home/awank/dev/SuperClaude_Framework")
PDF_DIR = REPO_ROOT / "projects/seedwarden/scripts/output"
OUT_DIR = REPO_ROOT / "projects/seedwarden/mockups"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# Canvas / frame geometry  (all in pixels at final resolution)
# ---------------------------------------------------------------------------
CANVAS_W = 2400
CANVAS_H = 2400

# Tablet outer dimensions
TABLET_W = 1200
TABLET_H = 1580
TABLET_X = (CANVAS_W - TABLET_W) // 2          # centred horizontally
TABLET_Y = (CANVAS_H - TABLET_H) // 2          # centred vertically
TABLET_RADIUS = 80                              # outer corner radius

# Bezel width on each side
BEZEL_TOP    = 90
BEZEL_BOTTOM = 90
BEZEL_SIDE   = 60

# Screen area inside the bezel
SCREEN_X = TABLET_X + BEZEL_SIDE
SCREEN_Y = TABLET_Y + BEZEL_TOP
SCREEN_W = TABLET_W - BEZEL_SIDE * 2
SCREEN_H = TABLET_H - BEZEL_TOP - BEZEL_BOTTOM

# Home-button / camera nub sizes
CAMERA_R = 14          # small circle near top centre
BUTTON_W = 70          # home button at bottom
BUTTON_H = 70

# ---------------------------------------------------------------------------
# Phone frame geometry (iPhone 13 proportions, scaled to canvas)
# ---------------------------------------------------------------------------
# Phone body: 440x950px total (phone body + bezel)
PHONE_W = 880          # scaled up 2x for the 2400px canvas (440 * 2)
PHONE_H = 1900         # scaled up 2x (950 * 2)
PHONE_X = (CANVAS_W - PHONE_W) // 2
PHONE_Y = (CANVAS_H - PHONE_H) // 2
PHONE_RADIUS = 100     # outer corner radius (notched modern phone look)

# Phone bezel widths
PHONE_BEZEL_TOP    = 100   # extra room for notch area
PHONE_BEZEL_BOTTOM = 100   # chin / home indicator area
PHONE_BEZEL_SIDE   = 30    # thin side bezels

# Phone screen area
PHONE_SCREEN_X = PHONE_X + PHONE_BEZEL_SIDE
PHONE_SCREEN_Y = PHONE_Y + PHONE_BEZEL_TOP
PHONE_SCREEN_W = PHONE_W - PHONE_BEZEL_SIDE * 2
PHONE_SCREEN_H = PHONE_H - PHONE_BEZEL_TOP - PHONE_BEZEL_BOTTOM

# Phone detail sizes
PHONE_NOTCH_W  = 200   # dynamic island / notch width
PHONE_NOTCH_H  = 40    # notch height
PHONE_CAMERA_R = 14    # small dot inside notch area

# ---------------------------------------------------------------------------
# Colours
# ---------------------------------------------------------------------------
BG_TOP    = (242, 245, 240)     # very light warm white/sage — background gradient top
BG_BOTTOM = (225, 232, 222)     # slightly deeper sage — background gradient bottom

BEZEL_LIGHT = (215, 217, 214)   # light aluminium
BEZEL_MID   = (190, 193, 189)
BEZEL_DARK  = (160, 163, 158)

SCREEN_BG   = (255, 255, 255)

SHADOW_COLOR = (100, 110, 100, 80)   # RGBA — soft drop shadow

# Matte black phone frame colours
PHONE_FRAME_DARK  = (28, 28, 30)     # near-black body
PHONE_FRAME_MID   = (44, 44, 46)     # slightly lighter for gradient
PHONE_FRAME_LIGHT = (60, 60, 62)     # highlight edge

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def rounded_rect_mask(draw: ImageDraw.ImageDraw, xy, radius: int, fill):
    """Draw a rounded rectangle using pieslice arcs + rectangles."""
    x0, y0, x1, y1 = xy
    r = radius
    draw.rectangle([x0 + r, y0, x1 - r, y1], fill=fill)
    draw.rectangle([x0, y0 + r, x1, y1 - r], fill=fill)
    draw.pieslice([x0, y0, x0 + 2*r, y0 + 2*r], 180, 270, fill=fill)
    draw.pieslice([x1 - 2*r, y0, x1, y0 + 2*r], 270, 360, fill=fill)
    draw.pieslice([x0, y1 - 2*r, x0 + 2*r, y1], 90, 180, fill=fill)
    draw.pieslice([x1 - 2*r, y1 - 2*r, x1, y1], 0, 90, fill=fill)


def vertical_gradient(img: Image.Image, top_color, bottom_color):
    """Fill image with a vertical linear gradient."""
    w, h = img.size
    draw = ImageDraw.Draw(img)
    for y in range(h):
        t = y / (h - 1)
        r = int(top_color[0] + t * (bottom_color[0] - top_color[0]))
        g = int(top_color[1] + t * (bottom_color[1] - top_color[1]))
        b = int(top_color[2] + t * (bottom_color[2] - top_color[2]))
        draw.line([(0, y), (w, y)], fill=(r, g, b))
    return img


def make_bezel_gradient(draw, x0, y0, x1, y1, radius):
    """Draw a 3-stop gradient bezel: light -> mid at top, mid -> dark at bottom."""
    # Draw in two halves — top half lighter, bottom half darker
    mid_y = (y0 + y1) // 2
    # Top half
    for y in range(y0, mid_y + 1):
        t = (y - y0) / max(mid_y - y0, 1)
        col = tuple(int(BEZEL_LIGHT[i] + t * (BEZEL_MID[i] - BEZEL_LIGHT[i])) for i in range(3))
        draw.line([(x0, y), (x1, y)], fill=col)
    # Bottom half
    for y in range(mid_y, y1 + 1):
        t = (y - mid_y) / max(y1 - mid_y, 1)
        col = tuple(int(BEZEL_MID[i] + t * (BEZEL_DARK[i] - BEZEL_MID[i])) for i in range(3))
        draw.line([(x0, y), (x1, y)], fill=col)


def render_pdf_page(pdf_path: pathlib.Path, target_w: int, target_h: int, page_num: int = 0) -> Image.Image:
    """Render a specific page of a PDF to a PIL Image, zoomed into the top 55% of the page.

    Args:
        pdf_path: Path to the PDF file.
        target_w: Target width for the rendered image.
        target_h: Target height for the rendered image.
        page_num: Zero-indexed page number (default 0 = first page).

    For cover pages (page 0), crops to the top 55% where the rich header is.
    For interior pages, shows the full page (or crops to top 85% if page is very tall).
    """
    # Cover pages have a rich header and blank area — crop to 55%.
    # Interior pages show full content — use 85% to avoid excessive blank space at bottom.
    CROP_FRACTION = 0.55 if page_num == 0 else 0.85

    doc = pdfium.PdfDocument(str(pdf_path))
    if page_num >= len(doc):
        page_num = len(doc) - 1  # fallback to last page
    page = doc[page_num]

    pw, ph = page.get_width(), page.get_height()

    # Render at a scale that fits target_w at full page width.
    # We'll crop vertically after, so only constrain by width.
    scale = target_w / pw
    # Render at 2x then downscale for better antialiasing
    render_scale = scale * 2
    bitmap = page.render(scale=render_scale, rotation=0)
    pil_img = bitmap.to_pil()

    # Convert to RGB
    if pil_img.mode != "RGB":
        bg = Image.new("RGB", pil_img.size, (255, 255, 255))
        if pil_img.mode == "RGBA":
            bg.paste(pil_img, mask=pil_img.split()[3])
        else:
            bg.paste(pil_img)
        pil_img = bg

    # Crop to top CROP_FRACTION of the rendered page
    crop_h = int(pil_img.height * CROP_FRACTION)
    pil_img = pil_img.crop((0, 0, pil_img.width, crop_h))

    # Downscale cropped region to target dimensions, preserving aspect ratio
    crop_aspect = pil_img.width / pil_img.height
    target_aspect = target_w / target_h
    if crop_aspect > target_aspect:
        # wider than target — fit height
        new_h = target_h
        new_w = int(new_h * crop_aspect)
    else:
        # taller than target — fit width
        new_w = target_w
        new_h = int(new_w / crop_aspect)
    pil_img = pil_img.resize((new_w, new_h), Image.LANCZOS)

    # Centre-crop to exact target size
    left = (new_w - target_w) // 2
    top = (new_h - target_h) // 2
    pil_img = pil_img.crop((left, top, left + target_w, top + target_h))

    doc.close()
    return pil_img


def render_interior_grid(pdf_path: pathlib.Path, target_w: int, target_h: int) -> Image.Image:
    """Render a 2x2 grid of interior pages (pages 2-5) from a PDF.

    Creates a grid showing pages 2-5 in a 2x2 layout with subtle dividers.
    This demonstrates content depth and product substance. If the PDF has fewer
    than 5 pages, wraps around to available pages.

    Args:
        pdf_path: Path to the PDF file.
        target_w: Total target width (grid width).
        target_h: Total target height (grid height).

    Returns:
        A PIL Image of the grid composite.
    """
    # Load document to check page count
    doc = pdfium.PdfDocument(str(pdf_path))
    page_count = len(doc)
    doc.close()

    # Page numbers to show (1-indexed in PDF, so pages 2-5 are indices 1-4)
    # If PDF is short, wrap around
    page_indices = []
    for i in range(1, 5):
        idx = min(i, page_count - 1) if i < page_count else (page_count - 1)
        page_indices.append(idx)

    # Grid is 2x2, so each cell is half the target size
    # Leave a small gap (2px) between cells for divider
    gap = 2
    cell_w = (target_w - gap) // 2
    cell_h = (target_h - gap) // 2

    # Render each page to cell size
    page_imgs = []
    for page_idx in page_indices:
        img = render_pdf_page(pdf_path, cell_w, cell_h, page_num=page_idx)
        page_imgs.append(img)

    # Build 2x2 grid: top-left, top-right, bottom-left, bottom-right
    grid = Image.new("RGB", (target_w, target_h), (255, 255, 255))

    # Top-left (page 2 or 1 if only 1 page)
    grid.paste(page_imgs[0], (0, 0))
    # Top-right (page 3 or wrapped)
    grid.paste(page_imgs[1], (cell_w + gap, 0))
    # Bottom-left (page 4 or wrapped)
    grid.paste(page_imgs[2], (0, cell_h + gap))
    # Bottom-right (page 5 or wrapped)
    grid.paste(page_imgs[3], (cell_w + gap, cell_h + gap))

    # Draw subtle dividers (light gray lines)
    divider = ImageDraw.Draw(grid)
    divider_color = (220, 220, 220)
    # Vertical divider
    divider.rectangle([cell_w, 0, cell_w + gap, target_h], fill=divider_color)
    # Horizontal divider
    divider.rectangle([0, cell_h, target_w, cell_h + gap], fill=divider_color)

    return grid


def build_tablet_frame(screen_img: Image.Image) -> Image.Image:
    """Composite screen_img into a drawn tablet frame on a neutral background."""

    # 1. Background canvas with gradient
    canvas = Image.new("RGB", (CANVAS_W, CANVAS_H))
    vertical_gradient(canvas, BG_TOP, BG_BOTTOM)

    # --- Drop shadow (blurred dark rect behind tablet) ---
    shadow_layer = Image.new("RGBA", (CANVAS_W, CANVAS_H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow_layer)
    shadow_offset = 18
    shadow_spread = 30
    rounded_rect_mask(
        sd,
        (
            TABLET_X - shadow_spread + shadow_offset,
            TABLET_Y - shadow_spread + shadow_offset,
            TABLET_X + TABLET_W + shadow_spread + shadow_offset,
            TABLET_Y + TABLET_H + shadow_spread + shadow_offset,
        ),
        TABLET_RADIUS + shadow_spread,
        (60, 70, 60, 100),
    )
    shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(radius=30))
    canvas = canvas.convert("RGBA")
    canvas = Image.alpha_composite(canvas, shadow_layer)
    canvas = canvas.convert("RGB")

    # 2. Bezel body — draw gradient on a temporary image then mask to rounded rect
    bezel_img = Image.new("RGB", (CANVAS_W, CANVAS_H), BEZEL_MID)
    bezel_draw = ImageDraw.Draw(bezel_img)
    make_bezel_gradient(
        bezel_draw,
        TABLET_X, TABLET_Y,
        TABLET_X + TABLET_W, TABLET_Y + TABLET_H,
        TABLET_RADIUS,
    )

    # Mask the gradient to a rounded rect
    mask = Image.new("L", (CANVAS_W, CANVAS_H), 0)
    mask_draw = ImageDraw.Draw(mask)
    rounded_rect_mask(
        mask_draw,
        (TABLET_X, TABLET_Y, TABLET_X + TABLET_W, TABLET_Y + TABLET_H),
        TABLET_RADIUS,
        255,
    )
    canvas.paste(bezel_img, mask=mask)

    # 3. Thin inner edge highlight (top-left edge of bezel looks lighter)
    highlight_layer = Image.new("RGBA", (CANVAS_W, CANVAS_H), (0, 0, 0, 0))
    hl_draw = ImageDraw.Draw(highlight_layer)
    rounded_rect_mask(
        hl_draw,
        (TABLET_X + 2, TABLET_Y + 2, TABLET_X + TABLET_W - 2, TABLET_Y + TABLET_H - 2),
        TABLET_RADIUS - 2,
        (255, 255, 255, 35),
    )
    canvas = canvas.convert("RGBA")
    canvas = Image.alpha_composite(canvas, highlight_layer)
    canvas = canvas.convert("RGB")

    # 4. Screen area — paste rendered PDF page
    canvas.paste(screen_img, (SCREEN_X, SCREEN_Y))

    # 5. Thin screen bezel border (subtle 2px dark line around screen)
    final_draw = ImageDraw.Draw(canvas)
    final_draw.rectangle(
        [SCREEN_X - 1, SCREEN_Y - 1, SCREEN_X + SCREEN_W, SCREEN_Y + SCREEN_H],
        outline=(140, 143, 138),
        width=2,
    )

    # 6. Camera dot (top centre)
    cam_cx = TABLET_X + TABLET_W // 2
    cam_cy = TABLET_Y + BEZEL_TOP // 2
    final_draw.ellipse(
        [cam_cx - CAMERA_R, cam_cy - CAMERA_R, cam_cx + CAMERA_R, cam_cy + CAMERA_R],
        fill=(130, 133, 128),
        outline=(100, 103, 98),
        width=2,
    )

    # 7. Home button (bottom centre)
    btn_cx = TABLET_X + TABLET_W // 2
    btn_cy = TABLET_Y + TABLET_H - BEZEL_BOTTOM // 2
    btn_r = BUTTON_W // 2
    final_draw.ellipse(
        [btn_cx - btn_r, btn_cy - btn_r, btn_cx + btn_r, btn_cy + btn_r],
        fill=(BEZEL_MID[0] - 15, BEZEL_MID[1] - 15, BEZEL_MID[2] - 15),
        outline=(140, 143, 138),
        width=3,
    )
    # Inner ring on home button
    inner_r = btn_r - 8
    final_draw.ellipse(
        [btn_cx - inner_r, btn_cy - inner_r, btn_cx + inner_r, btn_cy + inner_r],
        fill=None,
        outline=(160, 163, 158),
        width=2,
    )

    return canvas


def _draw_phone_frame(canvas: Image.Image) -> Image.Image:
    """Draw a matte-black portrait smartphone frame onto canvas.

    Draws the phone body, side buttons, and a Dynamic Island-style notch.
    Returns the modified canvas (RGB). The caller is responsible for pasting
    the screen image before calling this function — this function draws the
    frame chrome on top.

    Frame geometry is based on PHONE_* module-level constants (scaled 2x from
    iPhone 13 proportions to fit the 2400x2400 canvas at high resolution).
    """
    draw = ImageDraw.Draw(canvas)

    # ---- Phone body (matte black rounded rect) ----
    rounded_rect_mask(
        draw,
        (PHONE_X, PHONE_Y, PHONE_X + PHONE_W, PHONE_Y + PHONE_H),
        PHONE_RADIUS,
        PHONE_FRAME_DARK,
    )

    # ---- Thin highlight ring (1px lighter edge, top-left) ----
    # Achieved by drawing a slightly smaller rounded rect in PHONE_FRAME_LIGHT
    # then the body colour on top again — gives a subtle rim-light effect.
    highlight_layer = Image.new("RGBA", (CANVAS_W, CANVAS_H), (0, 0, 0, 0))
    hl_draw = ImageDraw.Draw(highlight_layer)
    rounded_rect_mask(
        hl_draw,
        (PHONE_X + 2, PHONE_Y + 2, PHONE_X + PHONE_W - 2, PHONE_Y + PHONE_H - 2),
        PHONE_RADIUS - 2,
        (255, 255, 255, 18),   # very faint white rim
    )
    canvas = canvas.convert("RGBA")
    canvas = Image.alpha_composite(canvas, highlight_layer)
    canvas = canvas.convert("RGB")
    draw = ImageDraw.Draw(canvas)

    # ---- Dynamic Island / notch (pill shape at top centre of screen) ----
    notch_cx = PHONE_X + PHONE_W // 2
    notch_cy = PHONE_Y + PHONE_BEZEL_TOP // 2
    notch_x0 = notch_cx - PHONE_NOTCH_W // 2
    notch_x1 = notch_cx + PHONE_NOTCH_W // 2
    notch_y0 = notch_cy - PHONE_NOTCH_H // 2
    notch_y1 = notch_cy + PHONE_NOTCH_H // 2
    notch_r  = PHONE_NOTCH_H // 2
    # Draw pill: two semicircles + rectangle
    rounded_rect_mask(
        draw,
        (notch_x0, notch_y0, notch_x1, notch_y1),
        notch_r,
        PHONE_FRAME_DARK,
    )

    # ---- Side buttons (power button right side, volume buttons left side) ----
    btn_color = PHONE_FRAME_MID
    btn_outline = PHONE_FRAME_LIGHT
    # Power button (right side)
    pw_x0 = PHONE_X + PHONE_W - 6
    pw_x1 = PHONE_X + PHONE_W + 14
    pw_y0 = PHONE_Y + PHONE_H // 2 - 100
    pw_y1 = PHONE_Y + PHONE_H // 2 + 100
    draw.rectangle([pw_x0, pw_y0, pw_x1, pw_y1], fill=btn_color, outline=btn_outline, width=2)

    # Volume up button (left side)
    vu_x0 = PHONE_X - 14
    vu_x1 = PHONE_X + 6
    vu_y0 = PHONE_Y + PHONE_H // 3 - 80
    vu_y1 = PHONE_Y + PHONE_H // 3 + 80
    draw.rectangle([vu_x0, vu_y0, vu_x1, vu_y1], fill=btn_color, outline=btn_outline, width=2)

    # Volume down button (left side)
    vd_x0 = vu_x0
    vd_x1 = vu_x1
    vd_y0 = PHONE_Y + PHONE_H // 3 + 120
    vd_y1 = PHONE_Y + PHONE_H // 3 + 280
    draw.rectangle([vd_x0, vd_y0, vd_x1, vd_y1], fill=btn_color, outline=btn_outline, width=2)

    # ---- Screen border (thin 1px line where glass meets bezel) ----
    draw.rectangle(
        [PHONE_SCREEN_X - 1, PHONE_SCREEN_Y - 1,
         PHONE_SCREEN_X + PHONE_SCREEN_W, PHONE_SCREEN_Y + PHONE_SCREEN_H],
        outline=(50, 50, 52),
        width=2,
    )

    # ---- Home indicator bar (thin pill at bottom of screen) ----
    ind_w = 200
    ind_h = 12
    ind_x = PHONE_X + PHONE_W // 2 - ind_w // 2
    ind_y = PHONE_Y + PHONE_H - PHONE_BEZEL_BOTTOM // 2 - ind_h // 2
    rounded_rect_mask(
        draw,
        (ind_x, ind_y, ind_x + ind_w, ind_y + ind_h),
        ind_h // 2,
        (80, 80, 82),
    )

    return canvas


def build_phone_frame(screen_img: Image.Image) -> Image.Image:
    """Composite screen_img into a drawn smartphone frame on a neutral background.

    Uses a matte-black portrait phone frame (iPhone 13 proportions, scaled 2x
    for the 2400x2400 canvas). The screen area is PHONE_SCREEN_W x PHONE_SCREEN_H
    pixels. Frame chrome (notch, buttons, home indicator) is drawn on top.

    The background gradient and drop shadow match the tablet variant for visual
    consistency across mockup sets.
    """
    # 1. Background canvas with same gradient as tablet variant
    canvas = Image.new("RGB", (CANVAS_W, CANVAS_H))
    vertical_gradient(canvas, BG_TOP, BG_BOTTOM)

    # 2. Drop shadow behind phone body
    shadow_layer = Image.new("RGBA", (CANVAS_W, CANVAS_H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow_layer)
    shadow_offset = 20
    shadow_spread = 35
    rounded_rect_mask(
        sd,
        (
            PHONE_X - shadow_spread + shadow_offset,
            PHONE_Y - shadow_spread + shadow_offset,
            PHONE_X + PHONE_W + shadow_spread + shadow_offset,
            PHONE_Y + PHONE_H + shadow_spread + shadow_offset,
        ),
        PHONE_RADIUS + shadow_spread,
        (30, 35, 30, 120),   # darker shadow for dark phone body
    )
    shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(radius=35))
    canvas = canvas.convert("RGBA")
    canvas = Image.alpha_composite(canvas, shadow_layer)
    canvas = canvas.convert("RGB")

    # 3. Paste screen image first (frame chrome will draw over the bezel areas)
    canvas.paste(screen_img, (PHONE_SCREEN_X, PHONE_SCREEN_Y))

    # 4. Draw phone frame chrome on top
    canvas = _draw_phone_frame(canvas)

    return canvas


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def process_all(frame_mode: str = "tablet"):
    """Render mockups for all PDFs in PDF_DIR.

    Args:
        frame_mode: "tablet" (default) for the iPad-style frame showing the cover,
                    "portrait" for a matte-black smartphone frame showing the cover,
                    or "interior" for a tablet frame showing a 2x2 grid of interior
                    pages (pages 2-5) to demonstrate product content and depth.
    """
    pdfs = sorted(PDF_DIR.glob("*.pdf"))
    if not pdfs:
        print("No PDFs found — check PDF_DIR path.", file=sys.stderr)
        sys.exit(1)

    use_phone = frame_mode == "portrait"
    use_interior = frame_mode == "interior"

    if use_interior:
        frame_label = "interior"
    elif use_phone:
        frame_label = "phone"
    else:
        frame_label = "tablet"

    if use_phone:
        screen_w = PHONE_SCREEN_W
        screen_h = PHONE_SCREEN_H
    else:
        screen_w = SCREEN_W
        screen_h = SCREEN_H

    print(f"Found {len(pdfs)} PDFs. Generating {frame_label} mockups...")
    success = []
    failures = []

    for pdf_path in pdfs:
        stem = pdf_path.stem
        if use_interior:
            out_name = f"{stem}_interior.png"
        elif use_phone:
            out_name = f"{stem}_phone.png"
        else:
            out_name = f"{stem}-mockup.png"
        out_path = OUT_DIR / out_name
        try:
            # Render pages to screen dimensions
            if use_interior:
                # Interior grid shows pages 2-5 in a 2x2 layout
                page_img = render_interior_grid(pdf_path, screen_w, screen_h)
            else:
                # Cover mockups show the first page
                page_img = render_pdf_page(pdf_path, screen_w, screen_h, page_num=0)

            # Build full composite with device frame
            if use_phone:
                mockup = build_phone_frame(page_img)
            else:
                # Both tablet (cover) and interior use the tablet frame
                mockup = build_tablet_frame(page_img)

            # Save at high quality
            mockup.save(str(out_path), "PNG", optimize=False)
            size_kb = out_path.stat().st_size // 1024
            w, h = mockup.size
            print(f"  OK  {out_name}  [{w}x{h}  {size_kb} KB]")
            success.append(out_path.name)
        except Exception as exc:
            print(f"  FAIL  {stem}: {exc}", file=sys.stderr)
            failures.append((stem, str(exc)))

    print(f"\nDone: {len(success)} generated, {len(failures)} failed.")
    if failures:
        print("Failures:")
        for name, err in failures:
            print(f"  {name}: {err}")
    return len(failures) == 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate Seedwarden product mockups (tablet, phone, or interior frame)."
    )
    parser.add_argument(
        "--frame",
        choices=["portrait", "interior"],
        default=None,
        help=(
            "Frame variant. Omit for default tablet/iPad frame (shows cover). "
            "Pass 'portrait' for a smartphone portrait frame. "
            "Pass 'interior' for a tablet frame showing a 2x2 grid of interior pages."
        ),
    )
    args = parser.parse_args()

    frame_mode = args.frame if args.frame else "tablet"
    ok = process_all(frame_mode=frame_mode)
    sys.exit(0 if ok else 1)
