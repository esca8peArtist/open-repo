"""
Seedwarden Zone Quick-Start Card Generator
Produces 8 single-page landscape PDFs (US Letter, 11x8.5 in) for Zones 3-10.

Layout per spec (ZONE_QUICKSTART_CARD_SPEC.md):
  - Header: wordmark left / "Zone Quick-Start Card" right / zone color band
  - Zone number (large) + region name
  - Three columns: Frost & Season | Quick-Start Crops | Storage & Preservation
  - Heirloom Variety Spotlight band (full width)
  - Footer with Etsy and landing page links

Fonts used:
  - Montserrat Bold  — zone number, wordmark, column headers
  - Montserrat Regular — body text, footer
  (Playfair Display not available offline; Montserrat Bold at large size
   fulfills the same visual hierarchy role specified in the spec.)
"""

from fpdf import FPDF
from fpdf.enums import XPos, YPos
from pathlib import Path

# ── Paths ─────────────────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).parent
FONTS_DIR = SCRIPT_DIR / "fonts"
OUTPUT_DIR = SCRIPT_DIR.parent / "assets" / "zone-cards"
LOGO_PATH = SCRIPT_DIR.parent / "logos" / "seedwarden_logo_1.png"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ── Brand palette (from ZONE_QUICKSTART_CARD_SPEC.md Part 4) ─────────────────
FOREST_GREEN   = (45,  80,  22)    # #2D5016  primary brand, headers, borders
WARM_CREAM     = (245, 237, 214)   # #F5EDD6  page background
BURNT_SIENNA   = (160,  82,  45)   # #A0522D  accent, icons, zone number, hot band
DARK_CHARCOAL  = (44,   44,  44)   # #2C2C2C  body text
PARCHMENT      = (237, 224, 196)   # #EDE0C4  variety spotlight band
WARM_GREY      = (122, 112,  96)   # #7A7060  footer text

# Zone temperature band colours
BAND_COOL      = (61,  107, 138)   # #3D6B8A  zones 3-4
BAND_TEMPERATE = (45,   80,  22)   # #2D5016  zones 5-6  (same as FOREST_GREEN)
BAND_WARM      = (201, 148,  58)   # #C9943A  zones 7-8
BAND_HOT       = (160,  82,  45)   # #A0522D  zones 9-10 (same as BURNT_SIENNA)

def _band_color(zone: int):
    if zone in (3, 4):   return BAND_COOL
    if zone in (5, 6):   return BAND_TEMPERATE
    if zone in (7, 8):   return BAND_WARM
    return BAND_HOT  # 9, 10


# ── Per-zone content (from ZONE_QUICKSTART_CARD_SPEC.md Part 5) ──────────────
ZONES = {
    3: {
        "region": "Northern Plains, Mountain Interior, Upper Great Lakes",
        "last_frost": "May 15 – June 1",
        "first_frost": "September 5 – September 20",
        "season_days": "95–125 days",
        "cities": "International Falls MN · Bismarck ND",
        "this_month": [
            "Start cucumbers, squash, melons & pumpkins indoors now (3–4 weeks before last frost). Zone 3's short season demands this head start.",
            "Direct sow peas, spinach & radishes as soon as soil is workable — these tolerate frost and should go in even if snow is still possible.",
            "Finish pepper & eggplant seedlings under lights — started in Feb, they need 4–6 more weeks before outdoor temps allow transplanting.",
        ],
        "crops": [
            ("Bush beans (Provider OP)", "Direct sow after last frost. 55-day crop, reliable in short seasons."),
            ("Kale (Lacinato H)", "Cold-hardy; harvest June through first hard freeze. Frost improves flavor."),
            ("Stupice tomato (OP)", "52–65 day short-season variety — the standard Zone 3 tomato."),
        ],
        "storage": [
            "Batch-process at harvest peak. Lacto-ferment greens: no canning equipment needed, 20 min hands-on per batch.",
            "Root cellar (cool basement corner, 35–40°F) extends beets, carrots & potatoes into spring.",
            "Freeze or dehydrate beans in July when Zone 3 bush beans all ripen within two weeks.",
        ],
        "spotlight": [
            ("Stupice tomato (H)", "Czech heirloom, 52–65 days. Small red fruits, reliable in Zone 3. Save seed year after year."),
            ("Waltham 29 broccoli (H)", "74-day compact heads, handles Zone 3 cold. Plant in March for June harvest."),
            ("Golden Bantam sweet corn (H)", "75 days, historic American heirloom. Grows in Zone 3's warmest microsites. Direct sow after last frost."),
        ],
    },
    4: {
        "region": "Upper Midwest, Northern New England, Mountain Valleys",
        "last_frost": "May 5 – May 25",
        "first_frost": "September 15 – October 5",
        "season_days": "120–150 days",
        "cities": "Minneapolis MN · Burlington VT · Madison WI",
        "this_month": [
            "Direct sow peas, spinach, lettuce, arugula, radishes & turnips — soil is workable in April and these need 4–6 weeks before summer heat.",
            "Start cucumbers, squash, pumpkins, melons & watermelons indoors in late April (3–4 weeks before mid-May last frost).",
            "Plant onion sets and seed potatoes as soon as soil is workable — both handle light frost once in the ground.",
        ],
        "crops": [
            ("Brandywine tomato (H)", "80 days, full Zone 4 season. The tomato worth growing here."),
            ("Sugar snap peas (OP)", "Direct sow April, harvest by June, done before summer heat. Highest reward-to-effort ratio."),
            ("Detroit Dark Red beet (H)", "Direct sow mid-April, harvest July–October, stores months in a cool space."),
        ],
        "storage": [
            "Canning supplies ready before harvest — Zone 4's August–September canning season hits stores hard.",
            "Dehydrate herbs (dill, basil, parsley) at harvest peak in July — they bolt fast. 20 min prep, 12 months of flavor.",
            "Root cellar or garage: beets, carrots, potatoes & winter squash store 4–6 months at 35–45°F. Cure squash 2 weeks first.",
        ],
        "spotlight": [
            ("Brandywine tomato (H)", "The benchmark heirloom, 80 days, full Zone 4 season. Pink beefsteak, rich flavor."),
            ("Long Island Improved Brussels sprouts (H)", "90 days — Zone 4 is just long enough. Frost improves flavor; harvest into October."),
            ("Scarlet Nantes carrot (H)", "Direct sow April, reliable germinator in Zone 4 soil, 65 days. The heirloom carrot standard."),
        ],
    },
    5: {
        "region": "Central Corridor, Southern New England, Mid-Elevation West",
        "last_frost": "April 15 – May 10",
        "first_frost": "October 1 – October 20",
        "season_days": "150–180 days",
        "cities": "Denver CO · Des Moines IA · Boston MA suburbs",
        "this_month": [
            "Transplant broccoli, cauliflower, cabbage, kale & onion starts outdoors mid-April — frost-tolerant and need to establish before heat.",
            "Direct sow beets, carrots & succession lettuce through April — these are your spring harvests.",
            "Start cucumbers, squash, pumpkins & melons indoors in late April (3–4 weeks before last frost). Don't start too early — cucurbits resent root disturbance.",
        ],
        "crops": [
            ("Dragon Tongue bush bean (H)", "Direct sow after last frost. 57 days, no staking, high yield, great container performer."),
            ("Mortgage Lifter tomato (H)", "80 days, large beefsteak, forgiving for beginners, full Zone 5 season with time to spare."),
            ("Lemon cucumber (H)", "65 days, compact vine, prolific, less bitter than slicing types, great for small spaces."),
        ],
        "storage": [
            "Two preservation windows: early summer (peas, greens — blanch & freeze) and late summer (tomatoes, peppers, beans).",
            "Tomato sauce is the highest-value project. A day of canning in August produces 18–24 quarts — 6 months of pasta sauce.",
            "Hot sauce fermentation uses peppers that ripen just before frost. Ferment 2–3 weeks, refrigerate — no canning needed.",
        ],
        "spotlight": [
            ("Mortgage Lifter tomato (H)", "80 days, bred by M.C. Byles for home gardeners. Exceptionally large sweet pink beefsteak. Seed-saveable."),
            ("Dragon Tongue bean (H)", "Yellow with purple streaks, 57 days, no staking. The variety that converts non-bean-growers."),
            ("Chioggia beet (H)", "55 days, candy-stripe interior, dual-purpose (root + greens), grows in 12 inches of soil."),
        ],
    },
    6: {
        "region": "Mid-Atlantic, Ohio Valley, Central Transition Zone",
        "last_frost": "April 5 – April 25",
        "first_frost": "October 10 – November 1",
        "season_days": "170–200 days",
        "cities": "St. Louis MO · Philadelphia PA · Kansas City MO",
        "this_month": [
            "Tomatoes, peppers & eggplants can go out by late April after 7–10 day hardening off — last frost is early April in most of Zone 6.",
            "Direct sow beans and corn after mid-April (soil above 60°F) — Zone 6 is warm enough now.",
            "Plant potatoes (if not done in March) and succession-sow lettuce, radishes & arugula for a second spring round before summer heat.",
        ],
        "crops": [
            ("Cherokee Purple tomato (H)", "72–80 days, signature Zone 6 heirloom. Rich complex flavor, harvests July through October."),
            ("Rattlesnake pole bean (H)", "65–70 days, drought-tolerant, distinctive purple-streaked pods. Direct sow after mid-April."),
            ("Clemson Spineless okra (H)", "Zone 6 is warm enough for productive okra. Direct sow after mid-April, harvest July–October."),
        ],
        "storage": [
            "Two full preservation seasons: early (peas, spring brassicas in June) and main (tomatoes, peppers, beans, corn in Aug–Sept).",
            "Zone 6's long tomato season (July–Oct) means enough volume to can, ferment hot sauce, and still dry some for winter.",
            "Fermented pickles (cucumbers, green beans) peak in Zone 6's July harvest window — low equipment, high reward.",
        ],
        "spotlight": [
            ("Cherokee Purple tomato (H)", "72–80 days, deeply flavored dark red-purple beefsteak with green shoulders. Zone 6–7 staple."),
            ("Rattlesnake pole bean (H)", "Named for its markings. Drought-tolerant, 65–70 days, continuous producer if picked regularly."),
            ("Wando pea (OP)", "The heat-tolerant pea — direct sow March or April, keeps producing into Zone 6's early summer heat."),
        ],
    },
    7: {
        "region": "Piedmont South, Oklahoma, North Texas, Maritime Northwest",
        "last_frost": "March 22 – April 15",
        "first_frost": "October 20 – November 10",
        "season_days": "190–225 days",
        "cities": "Raleigh NC · Oklahoma City OK · Seattle WA inland",
        "this_month": [
            "Tomatoes, peppers & eggplants are in the ground or going in now — last frost is behind most of Zone 7 by early April.",
            "Direct sow beans, corn, cucumber, squash, zucchini & okra throughout April — Zone 7 is warm enough for all of them.",
            "Harvest cool-season crops before they bolt — peas, lettuce, spinach, broccoli & cauliflower finish by late May. Pick at peak.",
        ],
        "crops": [
            ("Okra — Clemson Spineless (H) or Hill Country Red (OP)", "Direct sow April, harvest June–October. Zone 7 is the sweet spot for okra."),
            ("Sweet potato — Beauregard (OP)", "Plant slips late April (soil 65°F+). Harvest October. Stores for months."),
            ("Amish Paste tomato (H)", "85 days, large paste type, exceptional for sauce, heat-tolerant for Zone 7 summers."),
        ],
        "storage": [
            "Main preservation window July–October: sweet potatoes, tomatoes, peppers, okra & beans.",
            "Okra freezes better than it cans — blanch 3 min, freeze on sheet pan, bag. Maintains texture.",
            "Sweet potato curing (10 days at 85–90°F, then 55–60°F storage) extends shelf life to 6–12 months.",
        ],
        "spotlight": [
            ("Amish Paste tomato (H)", "85 days, large meaty paste type, adapted to Southeastern heat. Superior sauce tomato for Zone 7."),
            ("Clemson Spineless okra (H)", "1939 All-America Selections winner, still the standard. Productive, spineless, 56 days."),
            ("Beauregard sweet potato (OP)", "90 days, copper skin, orange flesh. Most reliable sweet potato for Zone 7 home gardeners."),
        ],
    },
    8: {
        "region": "Deep South, Coastal Pacific Northwest, Central Texas",
        "last_frost": "March 5 – March 25",
        "first_frost": "November 1 – November 25",
        "season_days": "225–265 days",
        "cities": "Portland OR · Dallas TX · Atlanta GA",
        "this_month": [
            "All warm-season crops are established or in the ground — last frost passed in March. April is full growing season in Zone 8.",
            "Plant sweet potato slips now (soil above 65°F). Plant okra and southern peas for summer harvest.",
            "Harvest spring crops (lettuce, broccoli, peas) before they bolt. Succession sow beans and corn for summer.",
        ],
        "crops": [
            ("Homestead tomato (OP)", "80 days, heat-tolerant, disease-resistant, bred for the South. Reliable where heirlooms struggle."),
            ("Clemson Spineless okra (H)", "Zone staple. Direct sow March–April, harvest June–November. Thrives in Zone 8 heat."),
            ("Seminole pumpkin (H)", "Heat-and-humidity-tolerant heirloom. Resists vine borers, stores one year without refrigeration."),
        ],
        "storage": [
            "Summer ferments are reliable in Zone 8 — active cultures out-compete spoilage. Kimchi and dilly beans work well.",
            "Sweet potato curing and long storage is highest-ROI: one 4×8 ft bed yields 50–80 lbs, stores 8–12 months cured.",
            "Dehydration shines here: hot peppers, okra & tomatoes reduce to compact shelf-stable storage.",
        ],
        "spotlight": [
            ("Homestead tomato (OP)", "Bred for Southern conditions. 80 days, disease-resistant. Reliably productive where Brandywine fails in July humidity."),
            ("Seminole pumpkin (H)", "The historically grown squash of the Southeast. Pest-resistant, 12-month storage, sprawling vine."),
            ("Rattlesnake watermelon (H)", "90 days, 25–40 lbs, thrives in Zone 8 heat and humidity. A Southern heirloom worth growing."),
        ],
    },
    9: {
        "region": "Gulf Coast, Southern Texas, Central Florida, SoCal Inland",
        "last_frost": "February 10 – March 5",
        "first_frost": "November 20 – December 15",
        "season_days": "260–300 days",
        "cities": "Houston TX · Jacksonville FL · Sacramento CA",
        "this_month": [
            "Spring garden in full production — harvest cucumbers & squash frequently to maximize yield before summer heat peaks.",
            "Cool-season window has closed: remove spent lettuce, spinach, peas & broccoli now. Do not let them bolt and deplete soil.",
            "Begin planning summer survival: okra, southern peas & sweet potatoes are the summer workhorses. Get okra in the ground now.",
        ],
        "crops": [
            ("Okra — Cow Horn (H) or Clemson Spineless (H)", "Sow April, harvest June–November. High success, minimal care, productive in Zone 9 heat."),
            ("Heat Wave II or Solar Fire tomato (OP)", "Bred for heat-set — these set fruit at high temperatures when standard varieties drop their blossoms."),
            ("California Blackeye cowpea (OP)", "Southern pea for Zone 9 summer. Direct sow April–June, nitrogen-fixing and edible beans."),
        ],
        "storage": [
            "Two preservation windows: spring (Feb–April, before heat) and fall (Oct–Dec, after heat). Plan canning sessions around these.",
            "Process spring tomatoes April–May before the crop is finished. Fall tomatoes ripen October–November for a second session.",
            "Freeze crushed tomatoes if April heat makes kitchen canning impractical — process them in October when temperatures are bearable.",
        ],
        "spotlight": [
            ("Tropic tomato (OP)", "Bred at University of Florida for tropical heat. 72 days, disease-resistant, heat-set. The Zone 9 workhorse."),
            ("Cow Horn okra (H)", "Longer pods (8–12 in), classic Southern heirloom, prolific in Zone 9 heat. Harvest at 4–6 in for best texture."),
            ("Zipper Cream cowpea (OP)", "Named for the easy-to-shell pod. Rich, creamy texture. Most popular Southern pea for Zone 9 home gardeners."),
        ],
    },
    10: {
        "region": "South Florida, Coastal Southern California, Hawaii",
        "last_frost": "January 31 or earlier; many areas frost-free year-round",
        "first_frost": "December 15 or later; many areas frost-free",
        "season_days": "300–365 days (essentially year-round)",
        "cities": "Miami FL · San Diego CA · Honolulu HI",
        "this_month": [
            "Cool-season crops are finishing fast — harvest all remaining lettuce, spinach, peas & broccoli now and clear the beds.",
            "Okra, southern peas & sweet potatoes are the priority. Succession-sow okra through April for a staggered harvest.",
            "Plan your July–August strategy: mulch heavily, solarize empty beds, and start fall crops indoors in late July.",
        ],
        "crops": [
            ("Everglades tomato (H)", "Native South Florida cherry tomato, essentially perennial in Zone 10. Prolific, disease-resistant, heat-set. Self-sows."),
            ("Seminole pumpkin (H)", "Native to Florida, bred for Zone 10 conditions. Resists vine borers, stores 12 months, sprawling vine."),
            ("Malabar spinach (OP)", "The heat-loving vine that fills the spinach role in Zone 10 summer. Productive trellis plant, very easy to grow."),
        ],
        "storage": [
            "Cool-season window (Oct–April) is the primary preservation season — process spring tomatoes and root vegetables while temperatures allow.",
            "Tropical fruit preservation is the Zone 10 opportunity: dehydrated mango, fig preserves, and avocado products are high-value shelf-stable items.",
            "Fermented hot sauce is ideal for Zone 10's prolific hot pepper harvest — Zone 10 temperatures accelerate lacto-fermentation.",
        ],
        "spotlight": [
            ("Everglades cherry tomato (H)", "Native Florida heirloom. Produces through conditions that kill standard tomatoes. Marble-sized, intensely sweet. Self-sows."),
            ("Seminole pumpkin (H)", "Historically significant Florida heirloom. Pest-resistant, 12-month storage without refrigeration, heat-adapted."),
            ("Datil pepper (H)", "St. Augustine FL's locally famous hot pepper. Habanero heat with fruitier flavor. The defining Zone 10 Florida pepper for sauces."),
        ],
    },
}


# ── PDF layout constants (US Letter landscape: 279.4 x 215.9 mm) ──────────────
PAGE_W = 279.4   # mm
PAGE_H = 215.9   # mm
MARGIN = 12.0    # mm
BODY_W = PAGE_W - 2 * MARGIN          # 255.4 mm usable width

COL1_W = BODY_W * 0.335               # ~85.6 mm  Frost & Season
COL2_W = BODY_W * 0.335               # ~85.6 mm  Quick-Start Crops
COL3_W = BODY_W * 0.330               # ~84.3 mm  Storage & Preservation
COL_GAP = 0.0                         # zero gap; whitespace is in text padding

# ── Helper: wrap text to width and return list of lines (simple word-wrap) ───
def _wrap(text: str, pdf: FPDF, max_w: float) -> list[str]:
    """Word-wrap *text* to fit *max_w* mm using the current pdf font."""
    words = text.split()
    lines = []
    current = ""
    for word in words:
        test = (current + " " + word).strip()
        if pdf.get_string_width(test) <= max_w:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


class ZoneCardPDF(FPDF):
    """Single-page landscape US Letter zone card."""

    def __init__(self):
        super().__init__(orientation="L", unit="mm", format="Letter")
        self.set_margins(MARGIN, MARGIN, MARGIN)
        self.set_auto_page_break(auto=False)
        self._register_fonts()

    def _register_fonts(self):
        self.add_font("Montserrat", style="",  fname=str(FONTS_DIR / "Montserrat-Regular.ttf"))
        self.add_font("Montserrat", style="B", fname=str(FONTS_DIR / "Montserrat-Bold.ttf"))

    # ── Core rendering helpers ─────────────────────────────────────────────────

    def _set_color(self, rgb):
        self.set_text_color(*rgb)

    def _fill_rect(self, x, y, w, h, rgb):
        self.set_fill_color(*rgb)
        self.rect(x, y, w, h, style="F")

    def _text_cell(self, x, y, w, h, text, font, size, color, align="L", ln=False):
        self.set_xy(x, y)
        self.set_font(font, size=size)
        self._set_color(color)
        self.cell(w, h, text, align=align, new_x=XPos.LMARGIN if ln else XPos.RIGHT,
                  new_y=YPos.NEXT if ln else YPos.TOP)

    def _multi_text(self, x, y, w, text, font, size, color, line_h=4.2):
        """Render wrapped multi-line text, return final y position."""
        self.set_font(font, size=size)
        self._set_color(color)
        lines = _wrap(text, self, w - 2)   # 2mm padding
        for line in lines:
            self.set_xy(x + 1, y)
            self.cell(w - 2, line_h, line, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            y += line_h
        return y

    # ── Column header ─────────────────────────────────────────────────────────
    def _col_header(self, x, y, w, label):
        self.set_font("Montserrat", style="B", size=8)
        self._set_color(FOREST_GREEN)
        # Small caps simulation: upper-case with tracking emulated by spacing
        self.set_xy(x + 1, y)
        self.cell(w - 2, 4.5, label.upper(), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        # Thin rule under header
        rule_y = y + 5
        self.set_draw_color(*FOREST_GREEN)
        self.set_line_width(0.25)
        self.line(x + 1, rule_y, x + w - 1, rule_y)
        return rule_y + 1.5

    # ── Bullet item: label (bold) + description ────────────────────────────────
    def _bullet_item(self, x, y, w, label, desc, line_h=4.0):
        self.set_font("Montserrat", style="B", size=7.5)
        self._set_color(DARK_CHARCOAL)
        label_w = min(self.get_string_width(label) + 3, w - 4)
        self.set_xy(x + 2, y)
        self.cell(label_w, line_h, label)
        # Bullet dot
        self.set_font("Montserrat", style="", size=7.5)
        self._set_color(DARK_CHARCOAL)
        # Description text wrapped
        desc_lines = _wrap(desc, self, w - 4)
        if desc_lines:
            self.set_xy(x + 2, y + line_h)
            for dl in desc_lines:
                self.set_xy(x + 4, self.get_y())
                self.set_font("Montserrat", style="", size=7.5)
                self._set_color(DARK_CHARCOAL)
                self.cell(w - 5, 3.8, dl, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            return self.get_y() + 1.0
        return y + line_h + 1.0

    # ── Numbered task item ─────────────────────────────────────────────────────
    def _numbered_item(self, x, y, w, num, text, line_h=3.8):
        self.set_font("Montserrat", style="B", size=7.5)
        self._set_color(BURNT_SIENNA)
        self.set_xy(x + 1, y)
        self.cell(5, line_h, f"{num}.")
        self.set_font("Montserrat", style="", size=7.5)
        self._set_color(DARK_CHARCOAL)
        lines = _wrap(text, self, w - 7)
        first = True
        for line in lines:
            self.set_xy(x + 6 if first else x + 8, self.get_y() if not first else y)
            self.cell(w - 8, line_h, line, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            first = False
        return self.get_y() + 1.0

    def _plain_item(self, x, y, w, text, line_h=3.8):
        self.set_font("Montserrat", style="", size=7.5)
        self._set_color(DARK_CHARCOAL)
        lines = _wrap(text, self, w - 3)
        for line in lines:
            self.set_xy(x + 2, y)
            self.cell(w - 3, line_h, line, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            y += line_h
        return y + 1.0

    # ── Main card builder ──────────────────────────────────────────────────────
    def build_card(self, zone: int, data: dict):
        self.add_page()
        band_color = _band_color(zone)

        # ── PAGE BACKGROUND ──────────────────────────────────────────────────
        self._fill_rect(0, 0, PAGE_W, PAGE_H, WARM_CREAM)

        # ── HEADER BAND (top green bar) ──────────────────────────────────────
        header_h = 14.0
        self._fill_rect(0, 0, PAGE_W, header_h, FOREST_GREEN)

        # Logo (if available)
        logo_x = MARGIN
        if LOGO_PATH.exists():
            try:
                self.image(str(LOGO_PATH), x=logo_x, y=1.5, h=11, keep_aspect_ratio=True)
            except Exception:
                pass

        # Wordmark
        self.set_font("Montserrat", style="B", size=9)
        self.set_text_color(255, 255, 255)
        self.set_xy(MARGIN + 14, 4.5)
        self.cell(50, 5, "SEEDWARDEN", align="L")

        # "Zone Quick-Start Card" label (right side of header)
        self.set_font("Montserrat", style="", size=8)
        self.set_text_color(200, 220, 200)
        self.set_xy(PAGE_W - MARGIN - 70, 4.5)
        self.cell(70, 5, "Zone Quick-Start Card", align="R")

        # ── ZONE COLOR BAND (12px rule below header) ─────────────────────────
        band_y = header_h
        band_px_h = 4.2   # ~12px at 72dpi → ~4.2mm
        self._fill_rect(0, band_y, PAGE_W, band_px_h, band_color)

        # ── ZONE NUMBER + REGION NAME block ──────────────────────────────────
        zone_block_y = band_y + band_px_h + 2.5
        # Zone number — large, in accent color, right-aligned in a dedicated zone badge block
        zone_badge_w = 38.0
        self.set_font("Montserrat", style="B", size=36)
        self._set_color(BURNT_SIENNA)
        self.set_xy(PAGE_W - MARGIN - zone_badge_w, zone_block_y - 1)
        self.cell(zone_badge_w, 16, str(zone), align="R")

        # "ZONE" label above number
        self.set_font("Montserrat", style="B", size=7)
        self._set_color(WARM_GREY)
        self.set_xy(PAGE_W - MARGIN - zone_badge_w, zone_block_y - 1)
        self.cell(zone_badge_w, 5, "ZONE", align="R")

        # Region name below zone number
        self.set_font("Montserrat", style="", size=7.5)
        self._set_color(FOREST_GREEN)
        region_lines = _wrap(data["region"], self, zone_badge_w)
        ry = zone_block_y + 14.5
        for rl in region_lines:
            self.set_xy(PAGE_W - MARGIN - zone_badge_w, ry)
            self.cell(zone_badge_w, 3.8, rl, align="R")
            ry += 3.8

        # Cities line
        self.set_font("Montserrat", style="", size=6.5)
        self._set_color(WARM_GREY)
        self.set_xy(PAGE_W - MARGIN - zone_badge_w, ry + 1)
        self.cell(zone_badge_w, 3.5, data["cities"], align="R")

        # Thin divider between badge and body columns
        div_x = PAGE_W - MARGIN - zone_badge_w - 3
        self.set_draw_color(*WARM_GREY)
        self.set_line_width(0.2)
        self.line(div_x, band_y + band_px_h + 2, div_x, band_y + band_px_h + 42)

        # ── THREE COLUMN BODY ─────────────────────────────────────────────────
        body_top = zone_block_y + 1.0
        usable_w = div_x - MARGIN - 2
        c1w = usable_w * 0.355
        c2w = usable_w * 0.330
        c3w = usable_w * 0.315

        x1 = MARGIN
        x2 = x1 + c1w
        x3 = x2 + c2w

        # -- Column 1: Frost Dates & Season -----------------------------------
        cy = body_top
        cy = self._col_header(x1, cy, c1w, "Frost Dates & Season")

        # Frost/season data
        frost_lines = [
            ("Last frost:",  data["last_frost"]),
            ("First frost:", data["first_frost"]),
            ("Season:",      data["season_days"]),
        ]
        for label, val in frost_lines:
            self.set_font("Montserrat", style="B", size=7.5)
            self._set_color(FOREST_GREEN)
            self.set_xy(x1 + 1, cy)
            self.cell(20, 4.0, label)
            self.set_font("Montserrat", style="", size=7.5)
            self._set_color(DARK_CHARCOAL)
            lines = _wrap(val, self, c1w - 23)
            self.set_xy(x1 + 22, cy)
            self.cell(c1w - 23, 4.0, lines[0] if lines else val)
            cy += 4.3
            for extra in lines[1:]:
                self.set_xy(x1 + 22, cy)
                self.set_font("Montserrat", style="", size=7.5)
                self._set_color(DARK_CHARCOAL)
                self.cell(c1w - 23, 4.0, extra)
                cy += 4.0

        cy += 2.0

        # This Month label
        self.set_font("Montserrat", style="B", size=7.5)
        self._set_color(BURNT_SIENNA)
        self.set_xy(x1 + 1, cy)
        self.cell(c1w - 2, 4.2, "THIS MONTH — MAY 2026")
        cy += 5.0

        for i, task in enumerate(data["this_month"], 1):
            cy = self._numbered_item(x1, cy, c1w, i, task)

        # -- Column 2: Quick-Start Crops ---------------------------------------
        cy2 = body_top
        cy2 = self._col_header(x2, cy2, c2w, "Quick-Start Crops")

        for label, desc in data["crops"]:
            cy2 = self._bullet_item(x2, cy2, c2w, label, desc)

        # -- Column 3: Storage & Preservation ---------------------------------
        cy3 = body_top
        cy3 = self._col_header(x3, cy3, c3w, "Storage & Preservation")

        for tip in data["storage"]:
            self.set_font("Montserrat", style="", size=7.5)
            self._set_color(DARK_CHARCOAL)
            # Small bullet
            self.set_xy(x3 + 1, cy3)
            self.cell(4, 3.8, "•")
            lines = _wrap(tip, self, c3w - 6)
            first = True
            for ln in lines:
                self.set_xy(x3 + 5, cy3)
                self.cell(c3w - 6, 3.8, ln, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                cy3 += 3.8
                first = False
            cy3 += 1.0

        # ── VARIETY SPOTLIGHT BAND ────────────────────────────────────────────
        spotlight_top = max(cy, cy2, cy3) + 4.0
        # Keep it from running off the page
        spotlight_top = min(spotlight_top, PAGE_H - 34)

        spotlight_h = PAGE_H - spotlight_top - 10.0  # leaves room for footer
        self._fill_rect(0, spotlight_top, PAGE_W, spotlight_h + 2, PARCHMENT)

        self.set_font("Montserrat", style="B", size=8)
        self._set_color(FOREST_GREEN)
        self.set_xy(MARGIN, spotlight_top + 2.5)
        self.cell(BODY_W, 5, "HEIRLOOM VARIETY SPOTLIGHT", align="L")

        # Three variety entries across full width
        entry_w = BODY_W / 3
        for i, (name, desc) in enumerate(data["spotlight"]):
            ex = MARGIN + i * entry_w
            ey = spotlight_top + 8.5
            self.set_font("Montserrat", style="B", size=7.5)
            self._set_color(BURNT_SIENNA)
            self.set_xy(ex + 1, ey)
            self.cell(entry_w - 2, 4.0, name[:52])   # truncate if too long
            ey += 4.2
            self.set_font("Montserrat", style="", size=7.0)
            self._set_color(DARK_CHARCOAL)
            dlines = _wrap(desc, self, entry_w - 4)
            for dl in dlines:
                self.set_xy(ex + 2, ey)
                self.cell(entry_w - 4, 3.5, dl)
                ey += 3.5

        # ── FOOTER ────────────────────────────────────────────────────────────
        footer_y = PAGE_H - 8.5
        self._fill_rect(0, footer_y - 0.5, PAGE_W, 9.5, FOREST_GREEN)

        self.set_font("Montserrat", style="", size=6.5)
        self.set_text_color(*WARM_CREAM)
        self.set_xy(MARGIN, footer_y + 0.5)
        self.cell(BODY_W / 2, 4.0,
                  f"Get the full Zone {zone} Calendar — seedwarden.co/zone-calendar",
                  align="L")
        self.set_xy(MARGIN + BODY_W / 2, footer_y + 0.5)
        self.cell(BODY_W / 2, 4.0,
                  "Free guides: seedwarden.co/zone  |  Unsubscribe anytime",
                  align="R")


def generate_all_zone_cards():
    print("Generating Zone Quick-Start Cards (Zones 3–10)...\n")
    for zone_num in range(3, 11):
        data = ZONES[zone_num]
        pdf = ZoneCardPDF()
        pdf.build_card(zone_num, data)

        filename = f"seedwarden-zone-{zone_num}-quickstart-card.pdf"
        out_path = OUTPUT_DIR / filename
        pdf.output(str(out_path))

        size_kb = out_path.stat().st_size // 1024
        print(f"  Zone {zone_num}  ->  {out_path}  ({size_kb} KB)")

    print(f"\nAll 8 cards saved to:\n  {OUTPUT_DIR}")
    return OUTPUT_DIR


if __name__ == "__main__":
    generate_all_zone_cards()
