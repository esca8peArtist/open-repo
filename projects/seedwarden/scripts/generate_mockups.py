"""
generate_mockups.py
Renders the first page of each Seedwarden PDF onto a clean tablet/iPad portrait
frame and saves a high-res PNG suitable for Etsy listings (≥2000px long side).

Frame design: drawn programmatically with Pillow — no external assets, no
licensing concerns.

Usage:
    uv run python projects/seedwarden/scripts/generate_mockups.py
"""

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
# Colours
# ---------------------------------------------------------------------------
BG_TOP    = (242, 245, 240)     # very light warm white/sage — background gradient top
BG_BOTTOM = (225, 232, 222)     # slightly deeper sage — background gradient bottom

BEZEL_LIGHT = (215, 217, 214)   # light aluminium
BEZEL_MID   = (190, 193, 189)
BEZEL_DARK  = (160, 163, 158)

SCREEN_BG   = (255, 255, 255)

SHADOW_COLOR = (100, 110, 100, 80)   # RGBA — soft drop shadow

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
    """Draw a 3-stop gradient bezel: light → mid at top, mid → dark at bottom."""
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


def render_pdf_page(pdf_path: pathlib.Path, target_w: int, target_h: int) -> Image.Image:
    """Render first page of a PDF to a PIL Image, zoomed into the top 55% of the page.

    The cover designs have a rich header (dark banner + title + price button) in the
    top half and a mostly-blank cream area below. Cropping to the top 55% fills the
    screen with the visually interesting part and avoids the empty lower half.
    """
    CROP_FRACTION = 0.55  # show only the top 55% of the page

    doc = pdfium.PdfDocument(str(pdf_path))
    page = doc[0]

    pw, ph = page.get_width(), page.get_height()

    # Render at a scale that fits target_w at full page width.
    # We'll crop vertically after, so only constrain by width.
    scale = target_w / pw
    # Render at 2× then downscale for better antialiasing
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


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def process_all():
    pdfs = sorted(PDF_DIR.glob("*.pdf"))
    if not pdfs:
        print("No PDFs found — check PDF_DIR path.", file=sys.stderr)
        sys.exit(1)

    print(f"Found {len(pdfs)} PDFs. Generating mockups...")
    success = []
    failures = []

    for pdf_path in pdfs:
        stem = pdf_path.stem
        out_path = OUT_DIR / f"{stem}-mockup.png"
        try:
            # Render first page to screen dimensions
            page_img = render_pdf_page(pdf_path, SCREEN_W, SCREEN_H)
            # Build full tablet composite
            mockup = build_tablet_frame(page_img)
            # Save at high quality
            mockup.save(str(out_path), "PNG", optimize=False)
            size_kb = out_path.stat().st_size // 1024
            w, h = mockup.size
            print(f"  OK  {stem}-mockup.png  [{w}x{h}  {size_kb} KB]")
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
    ok = process_all()
    sys.exit(0 if ok else 1)
