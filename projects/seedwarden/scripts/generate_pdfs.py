"""
Seedwarden PDF Generator
Converts markdown product files to branded PDFs using Montserrat + Lato fonts.
"""

import re
from pathlib import Path

from fpdf import FPDF
from fpdf.enums import XPos, YPos

# ── Brand colours ────────────────────────────────────────────────────────────
GREEN = (20, 59, 40)  # #143b28  – exact logo green
WHITE = (255, 255, 255)
CREAM = (248, 244, 236)
TERRACOTTA = (180, 90, 60)  # accent
DARK_TEXT = (30, 30, 30)
MID_TEXT = (80, 80, 80)
RULE_COLOR = (200, 220, 200)  # light green rule line

# ── Paths ─────────────────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).parent
FONTS_DIR = SCRIPT_DIR / "fonts"
OUTPUT_DIR = SCRIPT_DIR / "output"
PRODUCTS_DIR = SCRIPT_DIR.parent / "products"
LOGO_PATH = SCRIPT_DIR.parent / "logos" / "seedwarden_logo_1.png"

OUTPUT_DIR.mkdir(exist_ok=True)


class SeedwardenPDF(FPDF):
    def __init__(self, title: str, subtitle: str = ""):
        super().__init__("P", "mm", "A4")
        self.doc_title = title
        self.doc_subtitle = subtitle
        self.set_margins(20, 20, 20)
        self.set_auto_page_break(auto=True, margin=20)
        self._register_fonts()

    def _register_fonts(self):
        self.add_font(
            "Montserrat", style="", fname=str(FONTS_DIR / "Montserrat-Regular.ttf")
        )
        self.add_font(
            "Montserrat", style="B", fname=str(FONTS_DIR / "Montserrat-Bold.ttf")
        )
        self.add_font("Lato", style="", fname=str(FONTS_DIR / "Lato-Regular.ttf"))
        self.add_font("Lato", style="B", fname=str(FONTS_DIR / "Lato-Bold.ttf"))

    # ── Header / footer ──────────────────────────────────────────────────────
    def header(self):
        if self.page_no() == 1:
            return  # cover page has its own layout
        self.set_fill_color(*GREEN)
        self.rect(0, 0, 210, 8, "F")
        self.set_font("Montserrat", "B", 7)
        self.set_text_color(*WHITE)
        self.set_xy(10, 1.5)
        self.cell(0, 5, "SEEDWARDEN", align="L")
        self.set_xy(10, 1.5)
        self.cell(
            0, 5, self.doc_title.upper(), align="R", new_x=XPos.LMARGIN, new_y=YPos.NEXT
        )
        self.set_text_color(*DARK_TEXT)
        self.ln(4)

    def footer(self):
        if self.page_no() == 1:
            return
        self.set_y(-14)
        self.set_draw_color(*RULE_COLOR)
        self.set_line_width(0.3)
        self.line(20, self.get_y(), 190, self.get_y())
        self.ln(1)
        self.set_font("Lato", "", 8)
        self.set_text_color(*MID_TEXT)
        self.cell(0, 5, f"seedwarden.co  ·  page {self.page_no() - 1}", align="C")

    # ── Cover page ────────────────────────────────────────────────────────────
    def cover_page(self, price: str = ""):
        self.add_page()
        # Green background top half
        self.set_fill_color(*GREEN)
        self.rect(0, 0, 210, 148, "F")

        # Logo
        if LOGO_PATH.exists():
            self.image(str(LOGO_PATH), x=80, y=18, w=50)

        # Title
        self.set_font("Montserrat", "B", 26)
        self.set_text_color(*WHITE)
        self.set_xy(15, 80)
        self.multi_cell(180, 12, self.doc_title, align="C")

        # Subtitle
        if self.doc_subtitle:
            self.set_font("Lato", "", 13)
            self.set_text_color(180, 220, 180)
            self.set_x(15)
            self.multi_cell(180, 7, self.doc_subtitle, align="C")

        # Price badge
        if price:
            self.set_font("Montserrat", "B", 14)
            self.set_fill_color(*TERRACOTTA)
            self.set_text_color(*WHITE)
            self.set_xy(85, 130)
            self.cell(40, 10, price, align="C", fill=True)

        # Cream lower section – tagline
        self.set_fill_color(*CREAM)
        self.rect(0, 148, 210, 149, "F")
        self.set_font("Lato", "", 11)
        self.set_text_color(*MID_TEXT)
        self.set_xy(15, 158)
        self.multi_cell(
            180,
            7,
            "Open-pollinated · Community-grown · Food sovereignty for everyone",
            align="C",
        )

        # Bottom green strip
        self.set_fill_color(*GREEN)
        self.rect(0, 282, 210, 15, "F")
        self.set_font("Montserrat", "B", 9)
        self.set_text_color(*WHITE)
        self.set_xy(15, 284)
        self.cell(0, 8, "seedwarden.co", align="C")


class MarkdownRenderer:
    """Converts a markdown file into a SeedwardenPDF."""

    H1_SIZE = 20
    H2_SIZE = 15
    H3_SIZE = 12
    BODY_SIZE = 10
    SMALL_SIZE = 9

    def __init__(self, pdf: SeedwardenPDF):
        self.pdf = pdf

    def _set_body(self):
        self.pdf.set_font("Lato", "", self.BODY_SIZE)
        self.pdf.set_text_color(*DARK_TEXT)

    # Map Unicode box-drawing / special chars to Lato-safe ASCII equivalents
    _CHAR_MAP = str.maketrans(
        "┌┬┐├┼┤└┴┘─│╔╦╗╠╬╣╚╩╝═║◄►★░",
        "+++++++++--+++++++++=-+>*.",
    )

    def _normalize(self, text: str) -> str:
        return text.translate(self._CHAR_MAP)

    def _inline_formats(self, text: str) -> str:
        """Strip markdown bold/italic markers for plain text output."""
        text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
        text = re.sub(r"\*(.+?)\*", r"\1", text)
        text = re.sub(r"`(.+?)`", r"\1", text)
        return self._normalize(text)

    def render_line(self, line: str, in_table: bool = False):
        pdf = self.pdf
        stripped = line.rstrip()

        # HTML tags (e.g. page-break divs) — skip silently
        if stripped.startswith("<") and stripped.endswith(">"):
            return

        # ── Orphan prevention: add page break if too close to bottom ──
        if stripped.startswith("#") and not stripped.startswith("###### "):
            if self.pdf.get_y() > 240:
                self.pdf.add_page()

        # H1
        if stripped.startswith("# ") and not stripped.startswith("## "):
            pdf.set_font("Montserrat", "B", self.H1_SIZE)
            pdf.set_text_color(*GREEN)
            pdf.ln(4)
            pdf.multi_cell(
                0,
                9,
                self._inline_formats(stripped[2:]),
                new_x=XPos.LMARGIN,
                new_y=YPos.NEXT,
            )
            pdf.set_draw_color(*GREEN)
            pdf.set_line_width(0.5)
            pdf.line(pdf.get_x(), pdf.get_y(), 190, pdf.get_y())
            pdf.ln(3)
            self._set_body()
            return

        # H2
        if stripped.startswith("## "):
            pdf.set_font("Montserrat", "B", self.H2_SIZE)
            pdf.set_text_color(*GREEN)
            pdf.ln(4)
            pdf.multi_cell(
                0,
                8,
                self._inline_formats(stripped[3:]),
                new_x=XPos.LMARGIN,
                new_y=YPos.NEXT,
            )
            pdf.set_draw_color(*RULE_COLOR)
            pdf.set_line_width(0.3)
            pdf.line(pdf.get_x(), pdf.get_y(), 190, pdf.get_y())
            pdf.ln(2)
            self._set_body()
            return

        # H3 — each plant entry starts on its own page
        if stripped.startswith("### "):
            # Only force new page if we're not near the top (i.e., real content exists above)
            if pdf.get_y() > 55:
                pdf.add_page()
            pdf.set_font("Montserrat", "B", self.H3_SIZE)
            pdf.set_text_color(*TERRACOTTA)
            pdf.ln(2)
            pdf.multi_cell(
                0,
                7,
                self._inline_formats(stripped[4:]),
                new_x=XPos.LMARGIN,
                new_y=YPos.NEXT,
            )
            pdf.ln(1)
            self._set_body()
            return

        # H4
        if stripped.startswith("#### "):
            pdf.set_font("Montserrat", "B", self.SMALL_SIZE)
            pdf.set_text_color(*DARK_TEXT)
            pdf.ln(1)
            pdf.multi_cell(
                0,
                6,
                self._inline_formats(stripped[5:]),
                new_x=XPos.LMARGIN,
                new_y=YPos.NEXT,
            )
            self._set_body()
            return

        # Horizontal rule
        if stripped in ("---", "***", "___"):
            pdf.ln(2)
            pdf.set_draw_color(*RULE_COLOR)
            pdf.set_line_width(0.3)
            pdf.line(20, pdf.get_y(), 190, pdf.get_y())
            pdf.ln(3)
            return

        # Bullet point
        if stripped.startswith(("- ", "* ", "+ ")):
            self._set_body()
            indent = 6
            bullet = "•"
            text = self._inline_formats(stripped[2:])
            x_before = pdf.get_x()
            pdf.set_x(pdf.get_x() + indent)
            pdf.set_font("Lato", "B", self.BODY_SIZE)
            pdf.cell(4, 6, bullet)
            pdf.set_font("Lato", "", self.BODY_SIZE)
            pdf.multi_cell(0, 6, text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            return

        # Numbered list
        m = re.match(r"^(\d+)\. (.+)", stripped)
        if m:
            self._set_body()
            num = m.group(1)
            text = self._inline_formats(m.group(2))
            pdf.set_x(pdf.get_x() + 6)
            pdf.set_font("Lato", "B", self.BODY_SIZE)
            pdf.cell(6, 6, f"{num}.")
            pdf.set_font("Lato", "", self.BODY_SIZE)
            pdf.multi_cell(0, 6, text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            return

        # Table row — basic support
        if stripped.startswith("|") and stripped.endswith("|"):
            if re.match(r"^\|[-| :]+\|$", stripped):
                return  # separator row
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            col_w = 170 / max(len(cells), 1)
            pdf.set_font("Lato", "B", self.SMALL_SIZE)
            pdf.set_text_color(*DARK_TEXT)
            for i, cell in enumerate(cells):
                pdf.cell(col_w, 6, self._inline_formats(cell)[:40], border=1, align="L")
            pdf.ln()
            self._set_body()
            return

        # Inline image  ![alt text](path)
        img_match = re.match(r"^!\[([^\]]*)\]\(([^)]+)\)$", stripped)
        if img_match:
            alt_text = img_match.group(1)
            img_rel = img_match.group(2)
            img_path = SCRIPT_DIR / img_rel
            if img_path.exists():
                # Ensure enough vertical space; move to next page if needed
                if pdf.get_y() > 230:
                    pdf.add_page()
                img_w = 110  # mm — roughly half-page width for a field guide
                x = (210 - img_w) / 2
                pdf.ln(2)
                try:
                    pdf.image(str(img_path), x=x, w=img_w)
                except Exception:
                    pass  # skip broken images silently
                if alt_text:
                    pdf.set_font("Lato", "", 7.5)
                    pdf.set_text_color(100, 100, 100)
                    pdf.cell(
                        0, 4, alt_text, align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT
                    )
                    self._set_body()
                pdf.ln(2)
            return

        # Blank line
        if not stripped:
            pdf.ln(3)
            return

        # Regular paragraph
        self._set_body()
        # Handle inline bold
        parts = re.split(r"(\*\*[^*]+\*\*)", stripped)
        if len(parts) > 1:
            for part in parts:
                if part.startswith("**") and part.endswith("**"):
                    pdf.set_font("Lato", "B", self.BODY_SIZE)
                    pdf.write(6, part[2:-2])
                    pdf.set_font("Lato", "", self.BODY_SIZE)
                else:
                    if part:
                        pdf.write(6, part)
            pdf.ln()
        else:
            pdf.multi_cell(
                0,
                6,
                self._inline_formats(stripped),
                new_x=XPos.LMARGIN,
                new_y=YPos.NEXT,
            )

    def render_file(self, md_path: Path):
        self.pdf.add_page()
        lines = md_path.read_text(encoding="utf-8").splitlines()
        in_code_block = False
        for line in lines:
            stripped = line.rstrip()
            if stripped.startswith("```"):
                in_code_block = not in_code_block
                if in_code_block:
                    self.pdf.ln(2)
                else:
                    self.pdf.ln(2)
                continue
            if in_code_block:
                self._render_code_line(stripped)
            else:
                self.render_line(line)

    def _render_code_line(self, line: str):
        pdf = self.pdf
        y = pdf.get_y()
        pdf.set_fill_color(240, 240, 235)
        pdf.rect(20, y, 170, 5.5, "F")
        pdf.set_font("Lato", "", 7.5)
        pdf.set_text_color(50, 50, 50)
        pdf.set_x(22)
        pdf.cell(0, 5.5, self._normalize(line), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self._set_body()


# ── Product definitions ───────────────────────────────────────────────────────
PRODUCTS = [
    (
        "food-sovereignty-starter-guide.md",
        "Food Sovereignty Starter Guide",
        "A practical guide to seed saving & food independence",
        "$8",
    ),
    (
        "seed-saving-field-manual.md",
        "Seed Saving Field Manual",
        "The complete reference for saving seeds from 8 vegetables",
        "$14",
    ),
    (
        "apartment-seed-starting-kit.md",
        "Apartment Seed Starting Kit",
        "Grow food in small spaces — from seed to harvest",
        "$9",
    ),
    (
        "12-month-urban-growing-planner.md",
        "12-Month Urban Growing Planner",
        "Printable monthly planner for balcony & container gardeners",
        "$7",
    ),
    (
        "container-growing-blueprint-pack.md",
        "Container Growing Blueprint Pack",
        "5 complete layout plans for every container type",
        "$12",
    ),
    (
        "seed-swap-hosting-kit.md",
        "Seed Swap Hosting Kit",
        "Everything you need to run a community seed swap",
        "$10",
    ),
    (
        "heirloom-variety-selection-guide.md",
        "Heirloom Variety Selection Guide",
        "40+ varieties chosen for small spaces & easy seed saving",
        "$11",
    ),
    (
        "fermented-preserved-harvest-handbook.md",
        "Fermented & Preserved Harvest Handbook",
        "Small-batch preservation for the urban grower",
        "$13",
    ),
    (
        "grow-your-own-hot-sauce.md",
        "Grow Your Own Hot Sauce",
        "From heirloom pepper seed to bottled hot sauce",
        "$15",
    ),
    (
        "anti-catalog-30-heirlooms.md",
        "Anti-Catalog: 30 Heirlooms Worth Growing",
        "Opinionated profiles of 30 varieties worth protecting",
        "$10",
    ),
    (
        "small-scale-livestock-field-manual.md",
        "Small-Scale Livestock Field Manual",
        "Chickens, ducks, quail, rabbits, goats, pigs, turkeys, and bees",
        "$18",
    ),
    (
        "meat-fish-preservation-field-manual.md",
        "Meat, Fish & Animal Products Preservation Field Manual",
        "12 methods for preserving meat, fish, and animal products at home",
        "$18",
    ),
    (
        "harvest-preservation-field-manual.md",
        "Harvest Preservation Field Manual",
        "12 methods to preserve your harvest from season to season",
        "$16",
    ),
    (
        "native-plants-regional-guide.md",
        "Native Plants Regional Guide",
        "Wild edibles & useful plants across 9 US regions — with safety",
        "$18",
    ),
    (
        "apartment-plant-catalog.md",
        "Apartment Plant Catalog",
        "Edible & decorative plants for every small-space growing situation",
        "$14",
    ),
    (
        "survival-garden-regional-plans.md",
        "Survival Garden Regional Plans",
        "Complete food production plans for 5 US regions — two growing systems",
        "$18",
    ),
    (
        "hunting-fishing-trapping-field-manual.md",
        "Hunting, Fishing & Trapping Field Manual",
        "Survival hunting, fishing, and trapping across all US regions",
        "$20",
    ),
    (
        "companion-planting-chart.md",
        "The Companion Planting Chart",
        "What to Plant Together and What to Keep Apart",
        "$5",
    ),
    (
        "free-5-easiest-vegetables.md",
        "5 Easiest Vegetables to Start in an Apartment",
        "A free guide from Seedwarden",
        "FREE",
    ),
]


def generate_all():
    print(f"Generating {len(PRODUCTS)} PDFs...\n")
    for filename, title, subtitle, price in PRODUCTS:
        md_path = PRODUCTS_DIR / filename
        if not md_path.exists():
            print(f"  SKIP  {filename} (not found)")
            continue

        pdf = SeedwardenPDF(title, subtitle)
        pdf.cover_page(price)

        renderer = MarkdownRenderer(pdf)
        renderer.render_file(md_path)

        out_name = filename.replace(".md", ".pdf")
        out_path = OUTPUT_DIR / out_name
        pdf.output(str(out_path))
        pages = pdf.page  # total pages
        print(f"  ✓  {out_name}  ({pages} pages)")

    print(f"\nDone. PDFs saved to:\n  {OUTPUT_DIR}")


if __name__ == "__main__":
    generate_all()
