---
title: "Canva Zone Card Design Guide — Production-Ready Build Reference"
date: 2026-04-30
status: production-ready
context: Phase 2, Track B — Canva build execution reference
references:
  - ZONE_QUICKSTART_CARD_SPEC.md (content and design spec)
  - ZONE_CARD_PRODUCTION_TIMELINE.md (weekly build schedule)
  - PHASE_2_EMAIL_STRATEGY.md (Kit delivery integration)
---

# Canva Zone Card Design Guide
## Production-Ready Build Reference for the 8-Zone Quick-Start Card Series

**Purpose**: This document is the hands-on Canva execution guide. Where ZONE_CARD_PRODUCTION_TIMELINE.md is the schedule and ZONE_QUICKSTART_CARD_SPEC.md is the content brief, this document is what you open in a second window during your Canva session. It covers: template selection rationale, step-by-step build sequence with exact Canva menu paths, design decisions already made (so you do not make them during the session), zone color application by card, footer copy verification, and PDF export process. Execute this document against Week 0 and Week 1 of ZONE_CARD_PRODUCTION_TIMELINE.md.

**Time to complete this entire guide**: Week 0 (30 min Brand Kit) + Week 1 (approximately 4 hours for master template and Zones 5 and 6).

---

## Footer Copy Verification — Complete This Before Opening Canva

The card footer contains two links. Both must be locked before any card is built. Verified against ZONE_CARD_PRODUCTION_TIMELINE.md Pre-Canva Checklist footer lock table:

| Footer Element | Confirmed Value to Use at Build Time |
|---|---|
| Left side — Etsy Zone Calendar link | Use placeholder text: `[ETSY-ZONE-CALENDAR-LINK]` — update to live URL before final export. Do not build cards with this unfilled and unmarked. |
| Right side — Kit landing page URL | Use placeholder text: `seedwarden.com/zone` — update to live Kit landing page URL before final export. |

**Placeholder discipline**: Both placeholders must be visually distinct from live text during the build phase. Use ALL CAPS and brackets (as shown above) so they are impossible to miss during the Week 3 full-set review. Never export a final PDF with bracketed placeholder text visible.

**When to replace placeholders with live URLs**:
- Etsy Zone Calendar link: replace when the Etsy listing is live and the listing URL is confirmed
- Kit landing page URL: replace after Kit setup (Part 4 of PHASE_2_EMAIL_STRATEGY.md) is complete and the landing page URL is confirmed

---

## Part 1: Template Selection

### Why No Pre-Made Template — and What to Use Instead

Canva's template library (searched via "planner," "reference card," "educational PDF," or "fact sheet") does not contain a template that matches the Zone Quick-Start Card's structure: three-column body with a full-width spotlight band, zone-coded color, and dense typographic hierarchy. Adapting a mismatched template takes longer than building from a blank canvas.

**Selection decision: blank US Letter canvas, portrait orientation.**

Rationale:
- The three-column layout with specific percentage widths (35 / 35 / 30) requires precise element placement that pre-made templates do not accommodate without extensive deconstruction.
- The full-width Variety Spotlight band requires a background element that spans the page — this conflicts with most template frame structures.
- Building from blank canvas takes approximately 90 minutes for the master template but produces a cleaner, more controllable design that duplicates correctly across all 8 zones.

**What to search in Canva to find useful reference inspiration (not to copy):**
- "seed packet label" — useful for understanding typographic hierarchy at small sizes
- "plant care card" — useful for three-column layout examples at 8.5x11

Do not use these as starting templates. Use them as reference for hierarchy decisions only, then close them and build from blank.

---

## Part 2: Canva Session Setup — Before First Design Element

### Starting the Design File

Open Canva. In the top navigation, click "Create a design." In the size selector:

1. Click "Custom size"
2. Width: 8.5 inches
3. Height: 11 inches
4. Units: inches
5. Resolution: this is set by Canva internally — select "PDF Print" as the export format later (not "PDF Standard") and Canva applies 300 DPI automatically

Name the file immediately: `Seedwarden Zone [5] Quick-Start Card — MASTER`

Do not name it "Untitled" and rename later — lost files in Canva happen most often when files are untitled and saved to the wrong project folder.

### Setting Background Color

With the blank canvas open:
1. Click anywhere on the canvas (not an element — the blank page itself)
2. The background color selector appears in the top toolbar
3. Click the color swatch
4. In the color picker, click "+" or enter the hex value directly: `F5EDD6`
5. The canvas background changes to Warm Cream

This is the background for all 8 zone cards. It does not change between zones.

---

## Part 3: Building the Master Template — Zone 5 First

Build every element in this exact order. Each element is placed before moving to the next. Do not jump between sections.

### Block 1: Header Zone (estimated time: 20 minutes)

The header occupies the top 1.5 inches of the page (approximately).

**Element 1.1 — Seedwarden wordmark (left side of header)**

In Canva, add a text box:
- Click the "Text" tool in the left sidebar
- Click to add a text box in the top-left area of the canvas
- Type: `SEEDWARDEN`
- Font: Playfair Display (search in the font selector at the top)
- Size: 16pt
- Style: click "AA" to access letter spacing — set tracking to +50 (Canva calls this "Letter spacing")
- Color: `#2D5016` (Forest Green — Primary, from the Brand Kit)
- Enable small caps: In Canva, small caps are approximated by typing in all-caps and adjusting the font size — Playfair Display does not have a native small-caps setting in Canva. Use all-caps at 16pt; this reads as the correct wordmark style.
- Position: top-left, approximately 0.3 inches from the left edge, 0.25 inches from the top

**Element 1.2 — "Zone Quick-Start Card" label (right side of header)**

Add a second text box:
- Type: `Zone Quick-Start Card`
- Font: Montserrat Light
- Size: 12pt
- Color: `#7A7060` (Warm Grey — Footer)
- Position: top-right, aligned to the right margin, same vertical position as the wordmark
- This label is subtle — its role is to identify the document type, not to compete with the zone number

**Element 1.3 — Zone number (dominant typographic element)**

Add a text box centered or slightly left of center in the header area:
- Type: `5`
- Font: Playfair Display Bold
- Size: 72pt (minimum — can go to 80pt if the layout accommodates it)
- Color: `#A0522D` (Burnt Sienna — Accent)
- Position: below the wordmark and label, occupying the visual center of the header block
- This is the largest element on the page. If any element competes visually for dominance, reduce it.

**Element 1.4 — Region name (below zone number)**

Add a text box:
- Type: `Central Corridor, Southern New England, Mid-Elevation West`
- Font: Playfair Display Italic
- Size: 18pt
- Color: `#2D5016` (Forest Green)
- Position: directly below the zone number, centered or left-aligned to match the zone number

**Element 1.5 — Zone color band (horizontal rule below the header block)**

The zone color band is a solid rectangle, full page width, 12 pixels tall (in Canva, work in inches: 12px at 96 DPI ≈ 0.125 inches).

To add it:
1. In the left sidebar, click "Elements"
2. Search "line" or use "Shapes" to find a rectangle
3. Draw a rectangle the full width of the canvas (8.5 inches), height 0.125 inches
4. Fill color: `#2D5016` (Forest Green — Temperate; this is the Zone 5 color)
5. No border/stroke — the fill color is the band
6. Position: immediately below the header text area, flush with the left and right edges of the page

**Zone band color by zone — apply this per card:**

| Zone | Band Color | Hex |
|---|---|---|
| Zone 3 | Cool Slate Blue | `#3D6B8A` |
| Zone 4 | Cool Slate Blue | `#3D6B8A` |
| Zone 5 | Forest Green (Temperate) | `#2D5016` |
| Zone 6 | Forest Green (Temperate) | `#2D5016` |
| Zone 7 | Warm Amber | `#C9943A` |
| Zone 8 | Warm Amber | `#C9943A` |
| Zone 9 | Terracotta | `#A0522D` |
| Zone 10 | Terracotta | `#A0522D` |

When duplicating the Zone 5 master to build subsequent zones, the first edit is always changing this rectangle's fill color to the correct zone band value.

---

### Block 2: Three-Column Body (estimated time: 40 minutes)

The three-column body occupies the middle section of the page, from approximately 1.75 inches from the top to approximately 7.75 inches from the top (leaving the bottom 3.25 inches for the Variety Spotlight and footer).

**Column widths** (based on 8.5-inch page with 0.4-inch margins on each side = 7.7 inches usable):
- Column 1: 2.7 inches (35% of 7.7 in)
- Column 2: 2.7 inches (35%)
- Column 3: 2.3 inches (30%)
- Gap between columns: 0.25 inches each (included in the percentage widths above)

Canva does not have automatic column guides. Set up guides manually:
- View > Rulers and Guides > Show Rulers
- Drag a guide to: 0.4" (left margin), 3.1" (end of column 1), 3.35" (start of column 2), 6.05" (end of column 2), 6.3" (start of column 3), 8.1" (right margin)

**Column 1: Frost Dates and Season**

Element 2.1 — Calendar icon
- Left sidebar > Elements > search "calendar outline" or "botanical calendar outline"
- Select a line-style (not filled) icon
- Size: 24px (in Canva, this is approximately 0.25 inches)
- Color: `#2D5016` (Forest Green)
- Position: top of Column 1, centered within the column width

Element 2.2 — Column header
- Text box
- Type: `FROST DATES AND SEASON`
- Font: Montserrat
- Size: 11pt
- All caps (type in caps or use "Uppercase" toggle in Canva text settings)
- Letter spacing: +50
- Color: `#2D5016`

Element 2.3 — Body content block (Zone 5 content)
- Text box, full Column 1 width
- Font: Montserrat Light
- Size: 10pt
- Line height: 1.4
- Color: `#2C2C2C` (Dark Charcoal)
- Content from ZONE_QUICKSTART_CARD_SPEC.md Part 5, Zone 5:

```
Last frost: April 15 – May 10
First frost: October 1 – October 20
Growing season: 150–180 days

Denver CO, Des Moines IA,
Boston MA suburbs

THIS MONTH — APRIL 2026

1. Transplant broccoli, cauliflower,
cabbage, kale, and onion starts
outdoors now (mid-April) — frost-
tolerant and need to establish
before heat arrives.

2. Direct sow beets, carrots, and
succession lettuce through April.

3. Start cucumbers, squash, pumpkins,
and melons indoors late April (3–4
weeks before last frost). Do not
start too early — cucurbits resent
root disturbance.
```

Note on "THIS MONTH" label styling: make "THIS MONTH — APRIL 2026" slightly larger or bolder (Montserrat Regular or Medium at 10pt, with the rest of the block in Montserrat Light) to create visual break between the static frost data and the time-sensitive task block.

**Column 2: Quick-Start Crops**

Element 2.4 — Seed envelope icon
- Elements > search "seed envelope outline" or "seed packet minimal"
- Same size and color as the calendar icon

Element 2.5 — Column header
- Type: `QUICK-START CROPS`
- Same styling as Column 1 header

Element 2.6 — Body content block (Zone 5)
```
1. Dragon Tongue bush bean (H)
Direct sow after last frost. 57 days,
no staking, high yield. Best easy bean
in Zone 5.

2. Mortgage Lifter tomato (H)
80 days, large beefsteak. Forgiving for
beginners. Full Zone 5 season.

3. Lemon cucumber (H)
65 days, compact vine, prolific,
less bitter than slicing types.
Great for containers.
```

**Column 3: Storage and Preservation**

Element 2.7 — Mason jar icon
- Elements > search "mason jar outline" or "canning jar line"
- Same size and color

Element 2.8 — Column header
- Type: `STORAGE AND PRESERVATION`
- Same styling

Element 2.9 — Body content block (Zone 5)
```
Zone 5 has two preservation
windows: early summer (peas,
greens — freeze) and late summer
(tomatoes, peppers, beans — can,
ferment, or dehydrate).

Tomato sauce is the highest-value
project. One canning day in August
yields 18–24 quarts.

Hot sauce fermentation: low-effort,
uses peppers that ripen before frost.
Ferment 2–3 weeks, refrigerate —
no canning needed.
```

---

### Block 3: Variety Spotlight Section (estimated time: 20 minutes)

The Variety Spotlight occupies the lower third of the body area, approximately 7.75 inches from the top to 10.3 inches from the top (leaving 0.7 inches for the footer).

**Element 3.1 — Background band**
- Shapes > Rectangle
- Full page width (8.5 inches), height approximately 2.5 inches
- Fill color: `#EDE0C4` (Parchment — Spotlight Band)
- No stroke
- Position: flush with left and right page edges

**Element 3.2 — Seedling icon**
- Elements > search "seedling sprout outline"
- Size: 24px, color: `#2D5016`
- Position: left-aligned within the band, top of the band

**Element 3.3 — Section header**
- Type: `HEIRLOOM VARIETY SPOTLIGHT`
- Font: Montserrat, all caps, 11pt, letter spacing +50
- Color: `#2D5016`

**Element 3.4 — Variety content (Zone 5)**

Three rows, each containing variety name and one-line note. Format:
- Variety name: Montserrat, 10pt, italic (for the species name portion)
- Note text: Montserrat Light, 10pt, `#2C2C2C`

```
Mortgage Lifter tomato (H): 80 days, bred by M.C. Byles for home gardeners. Exceptionally large,
sweet pink beefsteak. Seed-saveable, true to type.

Dragon Tongue bean (H): Yellow with purple streaks, 57 days, no staking. The variety that converts
non-bean-growers.

Chioggia beet (H): 55 days, candy-stripe interior, dual-purpose root and greens, grows in 12 inches
of soil. Ideal for raised beds and containers.
```

---

### Block 4: Footer (estimated time: 10 minutes)

The footer occupies the bottom 0.7 inches of the page, below the Variety Spotlight band.

**Element 4.1 — Footer text**
- Single text box spanning full page width (within margins)
- Font: Montserrat Light, 8pt
- Color: `#7A7060` (Warm Grey)
- Line height: 1.4

Left-aligned text:
`Get the full Zone 5 Calendar — [ETSY-ZONE-CALENDAR-LINK]`

Right-aligned text (same text box, right-aligned tab or separate text box):
`Free guide: seedwarden.com/zone`

In Canva, the easiest approach is two separate text boxes aligned to the left and right margins respectively, both at 8pt Warm Grey.

---

## Part 4: Saving and Duplicating the Master Template

### Save the Zone 5 Master

After completing all four blocks for Zone 5:

1. Click the design title at the top of Canva (where it says the file name)
2. Confirm the name is: `Seedwarden Zone [5] Quick-Start Card — MASTER`
3. Canva auto-saves — this is not a manual save step, but verify the name is correct before navigating away

**Optional: Convert to a Canva template**
Right-click the design in the Canva home page (after navigating away and back) and select "Use as template." This creates a reusable template in your account. This step is optional — you can also duplicate from the original file.

### Duplicate Process for Each Subsequent Zone

For each zone after Zone 5:
1. Open the Zone 5 master
2. In the top-right, click the three-dot menu (...) > "Duplicate"
3. Rename immediately: `Seedwarden Zone [X] Quick-Start Card` (replace X)
4. Make changes in this exact order (zone band color first — it affects visual confirmation):

**Duplication change checklist per zone:**

| Change | Canva location | Zone 3 | Zone 4 | Zone 6 | Zone 7 | Zone 8 | Zone 9 | Zone 10 |
|---|---|---|---|---|---|---|---|---|
| Zone number | Header text box | 3 | 4 | 6 | 7 | 8 | 9 | 10 |
| Zone band color | Rectangle fill | `#3D6B8A` | `#3D6B8A` | `#2D5016` | `#C9943A` | `#C9943A` | `#A0522D` | `#A0522D` |
| Region line | Header text box | Northern Plains, Mountain Interior, Upper Great Lakes | Upper Midwest, Northern New England, Mountain Valleys | Mid-Atlantic, Ohio Valley, Central Transition Zone | Piedmont South, Oklahoma, North Texas, Maritime Northwest | Deep South, Coastal Pacific Northwest, Central Texas | Gulf Coast, Southern Texas, Central Florida, SoCal Inland | South Florida, Coastal Southern California, Hawaii |
| Footer Zone reference | Footer text box | Zone 3 | Zone 4 | Zone 6 | Zone 7 | Zone 8 | Zone 9 | Zone 10 |
| All body content | Columns 1–3, Variety Spotlight | See ZONE_QUICKSTART_CARD_SPEC.md Zone 3 section | See spec Zone 4 | See spec Zone 6 | See spec Zone 7 | See spec Zone 8 | See spec Zone 9 | See spec Zone 10 |

Do not change: background color, font choices, column widths, icon choices, footer Warm Grey color, Variety Spotlight background color. These are identical across all 8 cards.

---

## Part 5: May 2026 Content Update — "This Month" Block

The content tables in ZONE_QUICKSTART_CARD_SPEC.md Part 5 are dated to April 2026. If the cards launch in May 2026 or later, update the "This Month" block in every zone before final export.

**ZONE_CARD_PRODUCTION_TIMELINE.md confirms**: If this is a May 2026 launch, update the "This Month" block to May tasks before building — it is faster to update 8 spec entries than to re-export 8 PDFs after the fact.

The month label in Column 1 reads: `THIS MONTH — APRIL 2026`

Update this to: `THIS MONTH — MAY 2026` and replace the three task bullets with May-appropriate tasks for each zone.

**May 2026 "This Month" tasks by zone** (derived from the Zone-by-Zone Seed Starting Calendar product):

| Zone | May Task 1 | May Task 2 | May Task 3 |
|---|---|---|---|
| Zone 3 | Transplant tomatoes, peppers, and basil after May 15 last frost — do not rush this. Frost on transplants sets back the entire season. | Direct sow beans, corn, cucumbers, and squash immediately after last frost. These are the summer workhorses for Zone 3. | Continue succession-sowing lettuce, spinach, and radishes for spring harvest — soil is still cool enough to germinate them. |
| Zone 4 | Transplant tomatoes, peppers, eggplants, and cucurbits after May 10–25 last frost. Zone 4's window is narrow — transplant on time. | Direct sow beans, corn, and succession beets and carrots throughout May as soil warms above 60 F. | Harvest peas, spinach, and lettuce planted in April before they bolt in late May heat — their season is ending. |
| Zone 5 | Transplant tomatoes, peppers, eggplants after last frost (May 10 at the latest). Cucumbers and squash transplant now from indoor starts. | Direct sow beans, corn, basil, and summer squash after May 10. Zone 5's main planting month. | Succession sow beets, carrots, and lettuce through mid-May — last chance for a spring harvest before summer heat. |
| Zone 6 | May is mid-season maintenance: tomatoes, peppers, and cucurbits are in the ground. Side-dress with compost, stake tomatoes, and install trellis for beans and pole crops. | Direct sow okra, southern peas, and sweet potato slips throughout May. Zone 6's summer crops go in warm soil now. | Harvest spring crops (brassicas, peas) before they finish — bolting is starting. Succession plant beans for a second harvest. |
| Zone 7 | Tomatoes and peppers are growing rapidly — stake, prune suckers (indeterminate varieties), and water consistently as May heats up. | Plant sweet potato slips after soil reaches 65 F (early-to-mid May Zone 7). This is the primary staple crop for summer. | Succession sow okra and southern peas through May. Zone 7's summer is long — staggered planting extends the harvest window. |
| Zone 8 | May is active growing season — harvest cucumbers, squash, and beans regularly to keep plants productive. Do not let zucchini go to bat-size. | Begin heat management: mulch deeply around tomatoes and peppers to moderate soil temperature and retain moisture through Zone 8's summer. | Start fall transplants indoors in late May — broccoli, cauliflower, and kale for September transplanting. Zone 8's fall garden requires an early start. |
| Zone 9 | Zone 9 spring crops are finishing: harvest everything remaining from the spring garden before Zone 9's summer heat peaks in June. | Plant okra, southern peas, and sweet potato slips now — these are the crops that tolerate Zone 9's summer. Heat-tolerant crops only from here. | Begin fall planning: order seeds for fall garden (Zone 9 fall starts in August). The best time to plan is while the spring garden is still visible. |
| Zone 10 | Cool-season crops are done — clear beds and add compost now before summer heat sets in. Leaving spent plants in the ground wastes bed space and harbors pests. | Plant Malabar spinach, heat-tolerant herbs (lemon basil, Vietnamese coriander), and tropical edibles for summer production. | In Florida: prepare for rainy season management (drainage, fungal pressure). In SoCal: begin irrigation planning for the dry season. |

Copy the appropriate row's three tasks into the "THIS MONTH" block for each zone card.

---

## Part 6: PDF Export Process

### Canva Export Settings

For each zone card, export via:
1. Top right corner: "Share" button
2. Select "Download"
3. File type: **PDF Print** (not PDF Standard — PDF Print outputs at print-ready 300 DPI)
4. Color profile: RGB (Canva does not offer CMYK in free or Pro — RGB is correct for screen/home print distribution)
5. Flatten PDF: check this box if available — reduces file size by flattening layers
6. Click "Download"

**Expected file size**: 800 KB – 1.2 MB per card at PDF Print quality. If a file comes in over 2 MB, the background color may have been set as an embedded image rather than a flat color. Check: click the background area, confirm it shows as a solid color fill (not an uploaded image).

### File Naming and Storage

Name each exported file exactly as follows (lowercase, hyphens, no spaces):

| Zone | Filename |
|---|---|
| Zone 3 | `zone-3-quick-start-card.pdf` |
| Zone 4 | `zone-4-quick-start-card.pdf` |
| Zone 5 | `zone-5-quick-start-card.pdf` |
| Zone 6 | `zone-6-quick-start-card.pdf` |
| Zone 7 | `zone-7-quick-start-card.pdf` |
| Zone 8 | `zone-8-quick-start-card.pdf` |
| Zone 9 | `zone-9-quick-start-card.pdf` |
| Zone 10 | `zone-10-quick-start-card.pdf` |

Save all 8 PDFs to: `/projects/seedwarden/assets/zone-cards/`

The directory has been created and is ready.

After saving, log each file in WORKLOG.md with: filename, Canva file name, export date, and whether the "This Month" block has been updated to the current month.

---

## Part 7: Pre-Export Quality Check Per Card

Before exporting each zone's PDF, run through this check inside Canva (zoom to 100% in the Canva preview):

| Check Item | What to Confirm |
|---|---|
| Zone number visible and dominant | 72pt+ Burnt Sienna number is the first thing the eye goes to |
| Zone band color is correct | Matches the table in Part 3 for this zone |
| "This Month" header shows correct month | "MAY 2026" (or current month) not "APRIL 2026" |
| Footer left text includes zone number | "Zone [X]" matches the zone on the card |
| Footer placeholder text is marked | `[ETSY-ZONE-CALENDAR-LINK]` visible in brackets if Etsy link is not yet live |
| Footer right text matches | `seedwarden.com/zone` or the confirmed landing page URL |
| No text clipping | All text boxes are fully visible, no text cut off at edges |
| Font rendering | Playfair Display and Montserrat appear correctly (not substituted) |
| Background color consistent | Warm Cream `#F5EDD6` across entire page |
| Variety Spotlight band visible | Parchment `#EDE0C4` section visible at bottom |

---

## Part 8: Kit Upload Sequence

After all 8 PDFs are exported and stored locally, upload to Kit in this order. This order matches the zone routing sequence in PHASE_2_EMAIL_STRATEGY.md.

1. In Kit: navigate to Content > Files
2. Upload `zone-3-quick-start-card.pdf` — after upload, copy the generated download URL. Paste immediately into a dedicated note (or directly into WORKLOG.md under a "Kit file URLs" section). Label it: `Zone 3 Kit URL:`
3. Repeat for zones 4, 5, 6, 7, 8, 9, 10 in sequence
4. Verify each link by opening it in a private/incognito browser window before building the email automation

**WORKLOG.md Kit URL logging format** (add this section to WORKLOG.md after upload):

```
## Kit Zone Card File URLs — [upload date]

Zone 3: [paste URL here]
Zone 4: [paste URL here]
Zone 5: [paste URL here]
Zone 6: [paste URL here]
Zone 7: [paste URL here]
Zone 8: [paste URL here]
Zone 9: [paste URL here]
Zone 10: [paste URL here]
```

---

## Design Decision Log

The following decisions are made. Do not revisit them during a Canva session — decision fatigue during design work causes drift.

| Decision | Chosen Option | Rationale |
|---|---|---|
| Orientation | Portrait (8.5 x 11 vertical) | Spec default; prints on any home printer without configuration |
| Format | 8 individual zone PDFs | One clean file per subscriber; easier to update per zone |
| Template approach | Blank canvas, not a pre-made template | No pre-made template matches the three-column + spotlight band structure |
| Font system | Playfair Display (headings) + Montserrat (body) | Both free in Canva; spec-specified; strong typographic contrast |
| Zone number size | 72pt minimum | Dominant element rule — zone number must be immediately visible |
| Body text size | 10pt Montserrat Light | Smallest readable size on home-printed 8.5x11; tighter than this risks legibility |
| Icon style | Line-style (not filled) | All icons must be from one visual family; filled icons conflict with the text-forward design |
| Color mode | RGB | Canva does not support CMYK; RGB is correct for digital delivery and home printing |
| "This Month" update cadence | Monthly (first business day of each month) | Spec default; keeps the card seasonally useful |
| Footer URL status at build | Placeholder text in brackets | Both URLs are not yet live; placeholders prevent accidental publication of broken links |

---

*Prepared: 2026-04-30. Execute against ZONE_CARD_PRODUCTION_TIMELINE.md Week 0 and Week 1. Zone content is in ZONE_QUICKSTART_CARD_SPEC.md Part 5. Kit delivery setup is in PHASE_2_EMAIL_STRATEGY.md Part 4.*
