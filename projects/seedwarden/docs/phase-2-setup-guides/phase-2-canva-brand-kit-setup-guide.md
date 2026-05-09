---
title: "Phase 2 Canva Brand Kit Setup Guide"
subtitle: "Kit subscription decision, Brand Kit creation, zone card templates, and 30-day social calendar presets"
date: 2026-05-09
status: production-ready
estimated-time: 30–45 min (padded for first-time Canva setup; experienced: 20–25 min)
prerequisites: Canva account at canva.com, Phase 1 Figma file accessible (or brand hex codes)
references:
  - CANVA_SETUP_AND_EXECUTION_GUIDE.md (zone card grid setup and Brand Kit application)
  - CANVA_TEMPLATE_PROTOTYPE.md (visual design brief and branding rules)
  - CANVA_ZONE_CARD_DESIGN_GUIDE.md (per-zone content specs)
  - docs/phase-2-operations/phase-2-social-posting-scheduler.csv (30-day social calendar)
---

# Phase 2 Canva Brand Kit Setup Guide
## Subscription Decision, Brand Kit, Zone Card Template, and Social Presets

**Purpose**: This guide gets your Canva environment fully configured for Phase 2 production — Brand Kit, zone card master template, and social media presets for the 30-day content calendar. Completing this guide means you can produce any post in `phase-2-social-posting-scheduler.csv` without re-entering brand settings.

**Estimated time**: 30–45 minutes total. Broken out by section:
- Subscription decision tree: 5 minutes
- Brand Kit creation: 10–15 minutes
- Zone card template setup: 10–15 minutes (reference — full zone card build is in `CANVA_SETUP_AND_EXECUTION_GUIDE.md`)
- 30-day social calendar preset creation: 5–10 minutes

---

## Part 1: Subscription Decision (5 minutes)

### Canva Free vs. Canva Pro vs. Canva for Teams

```
SUBSCRIPTION DECISION TREE

Do you need to upload custom fonts (not available in Google Fonts)?
  YES → Canva Pro required ($15/month, cancel after Phase 2 zone card production)
  NO  → Continue to next question

Do you need background removal (photos with complex backgrounds, removing soil/wall behind products)?
  YES → Canva Pro required
  NO  → Continue

Are you working with another person who needs edit access to the same Canva files?
  YES → Canva for Teams ($15/person/month, minimum 2 people = $30/month)
  NO  → Continue

RESULT: Canva Free is sufficient for Phase 2 if:
  - Using Google Fonts (Canva Free includes all Google Fonts)
  - Product images have clean or solid-color backgrounds (no background removal needed)
  - Working solo

RESULT: Canva Pro is justified if:
  - Custom branded fonts (not on Google Fonts) are part of Phase 1 design spec
  - Lifestyle photo backgrounds need removal (outdoor shoot, textured backgrounds)
  - You want the convenience of Brand Kit unlimited color and font storage

CANVA FREE TRIAL NOTE: Canva Pro offers a 30-day free trial. If you need Pro features
only for the May 12–28 production window, you can activate the trial and cancel before
the billing date. The trial does not require a credit card on all plans — check current
terms at canva.com/pricing.
```

**Recommended for most Phase 2 scenarios**: Canva Free. All zone card elements in the CANVA_TEMPLATE_PROTOTYPE.md use Google Fonts (Lora, Inter) and solid color backgrounds. No custom font upload or background removal is required.

**Activate Pro trial if**: You discover during zone card production that a specific element requires a Pro feature. Do not pay for Pro proactively.

---

## Part 2: Brand Kit Creation (10–15 minutes)

The Brand Kit stores your hex colors and font selections so you can apply them in one click across every design. Set this up before building any design element — it eliminates per-file color re-entry for all 30 days of social content.

### Step 2.1 — Access Brand Hub

On the Canva dashboard (canva.com):
- Left sidebar: click "Brand Hub" (or navigate to canva.com/brand-hub)
- If Brand Hub is not visible in the sidebar: click "More" at the bottom of the sidebar to expand all options

**Free tier Brand Kit**: Canva Free allows 1 Brand Kit with up to 3 color palettes and 3 font combinations. This is sufficient for Seedwarden Phase 2.

**Pro Brand Kit**: Unlimited palettes and font combos, plus logo upload with background transparency. Not required for Phase 2.

### Step 2.2 — Create the Seedwarden Brand Kit

1. In Brand Hub: click "Create new brand kit" (or "Add a brand" if this is your first one).
2. Name the kit: `Seedwarden Phase 2`.
3. Click "Create."

### Step 2.3 — Import Color Palette from Phase 1 Figma

**If you have access to the Phase 1 Figma file**:
1. Open the Figma file. In the left panel, look for the color styles (usually shown as filled circles in the "Assets" panel or directly in the design as named color variables).
2. Click on each color swatch to see the hex code in the design panel on the right side (it will show as a 6-character hex code like `#2D4A22` or an RGB value).
3. Copy each hex code.

**If the Figma file is not accessible**: Use the approved Phase 1 Seedwarden hex codes listed below.

**Seedwarden brand colors** (from CANVA_TEMPLATE_PROTOTYPE.md):

| Color name | Hex code | Usage |
|---|---|---|
| Forest Green (primary) | #2D4A22 | Zone card header band, icon backgrounds, primary headings |
| Cream (background) | #F5F0E8 | Card background, light section backgrounds |
| Rust (accent) | #C4622D | Call-to-action elements, alert tags, category labels |
| Charcoal (body text) | #2C2C2C | All body text, table text |
| Sage (secondary) | #7A9E7E | Secondary headings, dividers, soft accent elements |
| White | #FFFFFF | Text on dark backgrounds, icon fills |

**To add colors in Canva Brand Hub**:
1. In your new Brand Kit > Colors section > click "Add color palette."
2. Name the palette: `Seedwarden Core`.
3. Click the "+" to add colors. For each color: paste the hex code in the hex field. Click "Add."
4. Repeat for all 6 colors.

### Step 2.4 — Upload Logo

1. In Brand Hub > Logos section > click "Upload logo."
2. Select `projects/seedwarden/logos/seedwarden_logo_1.png`.
3. Wait for upload to complete. The logo appears in your Brand Kit.

**Transparent background version**: If the logo has a white or colored background, check `projects/seedwarden/logos/` for a file ending in `-transparent.png`. Upload that version if available — it allows placement on any colored background without a visible rectangle around the logo.

### Step 2.5 — Font Selection

Canva Free supports Google Fonts. The Phase 1 Seedwarden type system uses two fonts from Google Fonts:

| Font name | Weight | Usage | Find in Canva |
|---|---|---|---|
| Lora | Bold (700) | Zone card headings, product card titles | Search "Lora" in Canva's font picker |
| Inter | Regular (400) | Body text, table entries, captions | Search "Inter" in Canva's font picker |

**To add fonts to Brand Kit**:
1. Brand Hub > Fonts section > click "Add font combination."
2. For "Heading font": search "Lora" > select Lora Bold.
3. For "Body font": search "Inter" > select Inter Regular.
4. Click "Save combination."

**If Canva does not show Inter**: try "Inter Variable" — it is the same typeface. Alternatively, use "DM Sans" (a very close substitute with identical proportions) if Inter is unavailable in your Canva account region.

---

## Part 3: Zone Card Template Setup (10–15 minutes)

This section provides an overview of the zone card template setup within the Canva environment. The complete step-by-step build guide (including exact grid measurements, column widths, and per-zone content) is in `CANVA_SETUP_AND_EXECUTION_GUIDE.md`. Read that guide before beginning zone card production.

### Step 3.1 — Create the Master Design File

1. Canva dashboard > "Create a design" (top right).
2. In the size picker: click "Custom size" (bottom of the list).
3. Enter: Width **8.5 in**, Height **11 in**, Units **inches**.
4. Click "Create new design."
5. Immediately rename: click the untitled filename at the top > type `Seedwarden Zone 5 Quick-Start Card — MASTER`.

Do not skip the rename. Files named "Untitled" are difficult to locate in Canva's project folder.

### Step 3.2 — Apply Brand Kit to the Design

Once inside the design:
1. In the left toolbar: click the "Brand Hub" icon (looks like a diamond or palette, varies by Canva version).
2. Your Seedwarden Brand Kit will appear. Click "Apply" or click individual colors to apply them to selected elements.

Alternatively, when clicking on any text element or shape, the color picker will show your Brand Kit colors as a quick-access row at the top of the color palette. You do not need to re-enter hex codes manually after the Brand Kit is configured.

### Step 3.3 — Set Up Column Guides

Canva does not have automatic column grids. Set six vertical guides manually for the zone card layout. These guides snap elements into position.

1. View (top menu) > Show Rulers (or press Shift+R).
2. Click and drag from the left ruler to place a guide at each position. To set a precise position: drag roughly, then double-click the guide to enter an exact number.

Required guide positions:
- 0.4 in — left margin
- 3.1 in — right edge of Column 1
- 3.35 in — left edge of Column 2
- 6.05 in — right edge of Column 2
- 6.3 in — left edge of Column 3
- 8.1 in — right margin (0.4 in from the right edge of an 8.5 in canvas)

Column widths this creates:
- Column 1: 2.7 in wide (0.4 in to 3.1 in)
- Column 2: 2.7 in wide (3.35 in to 6.05 in)
- Column 3: 1.8 in wide (6.3 in to 8.1 in)

Detailed build instructions from this point: `CANVA_SETUP_AND_EXECUTION_GUIDE.md` Steps 3–9.

---

## Part 4: Social Media Preset Creation for 30-Day Content Calendar (5–10 minutes)

Setting up presets for the three social post dimensions means you can start any new post without re-entering dimensions or brand settings.

### Step 4.1 — Create an Instagram Post Template

1. Canva dashboard > "Create a design" > Custom size: **1080 × 1080 px** (square post, used for single-image posts and the cover slide of carousels). Click "Create."
2. Rename: `Seedwarden IG Post — MASTER`.
3. Apply Brand Kit colors to the background or a text element to bind the Brand Kit to this file.
4. Add a text element with the Seedwarden logo, brand green background (#2D4A22), and a placeholder caption area at the bottom. Save as a template by duplicating this file for each post type.

**Instagram post dimensions by type**:
- Single image: 1080 × 1080 px (1:1 square)
- Carousel: 1080 × 1080 px per slide (same dimensions, 3–8 slides)
- Story: 1080 × 1920 px (9:16 vertical — create a separate template file)

### Step 4.2 — Create a TikTok / Reels Template

1. Canva > Custom size: **1080 × 1920 px** (9:16 vertical). Click "Create."
2. Rename: `Seedwarden TikTok-Reels — MASTER`.
3. Apply Brand Kit. Add a text overlay zone at the bottom third of the canvas (where TikTok UI does not overlap) and a title zone at the top. This is the safe zone for text that will not be obscured by TikTok's progress bar, like/comment buttons, or caption area.

**Safe zones on TikTok**:
- Top 10%: TikTok username and sound name appear here — keep clear of critical text
- Bottom 25%: TikTok caption, like/comment/share buttons — keep critical text above this area
- Left 10% on mobile: sometimes obscured by navigation — center or right-align text for safety

### Step 4.3 — Create a Pinterest Pin Template

1. Canva > Custom size: **1000 × 1500 px** (2:3 ratio, the Pinterest recommended pin size). Click "Create."
2. Rename: `Seedwarden Pinterest Pin — MASTER`.
3. Pinterest pins must include visible text overlay — a pin without text performs significantly below average in search. Add a text zone at the top or bottom of the canvas for the pin title, and a branding strip at the bottom (logo + seedwarden.com or Kit URL).

**Pinterest design rules**:
- Every pin must have a text overlay — Pinterest is a visual search engine; the text makes pins searchable.
- Use high-contrast text (white text on Forest Green, or Charcoal text on Cream) — pins are small in search results.
- The Seedwarden logo must appear somewhere on the pin to drive brand recognition as impressions accumulate.

### Step 4.4 — Save and Organize Templates

In Canva's left sidebar, click "Projects" > create a new folder called "Seedwarden Phase 2 — Templates."

Move all three master template files into this folder:
- Seedwarden IG Post — MASTER
- Seedwarden TikTok-Reels — MASTER
- Seedwarden Pinterest Pin — MASTER
- Seedwarden Zone 5 Quick-Start Card — MASTER (from Part 3)

For each post in `phase-2-social-posting-scheduler.csv`, create the social asset by:
1. Opening the relevant MASTER template.
2. Duplicating the page (Canva > click three dots on page thumbnail > "Duplicate page").
3. Edit the duplicate — never edit the MASTER page directly.
4. Name the duplicated page with the post date and platform (e.g., "Jun 1 IG — Harvest Handbook").

---

## Part 5: 30-Day Social Calendar Production Setup

The social calendar in `docs/phase-2-operations/phase-2-social-posting-scheduler.csv` specifies an `Image_File` column for every post. Where that column references a file that does not yet exist (i.e., a file that needs to be created in Canva), it will need to be produced using the templates from Part 4.

**Pre-existing image files** (already created in previous Phase 2 sessions):
- `marketing/lifestyle-photos/etsy-ready/cluster-a-hero.jpg` — main lifestyle photo for Seed Saving, Heirloom, Companion Planting products
- `marketing/lifestyle-photos/etsy-ready/cluster-b-slot4.jpg` — main lifestyle photo for Container Growing Blueprint
- `marketing/lifestyle-photos/etsy-ready/cluster-c-slot4.jpg` — main lifestyle photo for Harvest Preservation Handbook
- `assets/zone-cards/zone-5-preview.png` — Zone 5 card preview image

**Files that need to be created** (Canva-produced graphics):
- `marketing/lifestyle-photos/etsy-ready/quote-card.jpg` — testimonial quote card for June 4 post. Create in Canva using the IG Post MASTER template. Forest Green background, white text, Lora Bold for the quote, Inter Regular for attribution.
- `marketing/lifestyle-photos/etsy-ready/cluster-a-bts.jpg` — behind-the-scenes photo or Canva composite for BTS posts. If a physical BTS photo exists from the shoot, use that. If not, create a Canva graphic showing the research/production process.
- `marketing/lifestyle-photos/etsy-ready/cluster-d-composite.jpg` — composite for Cluster D/E products (survival garden posts). Create in Canva using a stock image from `assets/stock-raw/` with a product card overlay.

**Production sequence for social graphics**:
1. Produce quote-card.jpg first — it is needed for June 4 (Day 5 of the calendar).
2. Produce BTS graphic(s) before June 5 (Day 6 of the calendar).
3. Cluster D composite can be produced any time before June 17.

---

## Part 6: Verification Checklist

Before May 30, confirm each item below:

**Brand Kit**:
- [ ] Seedwarden Brand Kit created in Canva Brand Hub
- [ ] 6 brand colors added with correct hex codes
- [ ] Lora + Inter font combination saved
- [ ] Logo uploaded (with transparent background if available)

**Zone Card Template**:
- [ ] Zone 5 MASTER file created at 8.5 × 11 inches
- [ ] 6 column guides placed at correct positions
- [ ] Brand Kit applied to the file

**Social Templates**:
- [ ] IG Post MASTER created at 1080 × 1080 px
- [ ] TikTok-Reels MASTER created at 1080 × 1920 px
- [ ] Pinterest Pin MASTER created at 1000 × 1500 px
- [ ] All three MASTER files in the "Seedwarden Phase 2 — Templates" folder

**Social Graphics Production**:
- [ ] quote-card.jpg created and saved to `/marketing/lifestyle-photos/etsy-ready/`
- [ ] cluster-a-bts.jpg exists or is created
- [ ] cluster-d-composite.jpg created

---

*Estimated time: 30–45 minutes for full Canva Brand Kit and social template setup. Zone card production time (90 minutes for Zone 5 master + 35–45 minutes per additional zone) is separate and documented in `CANVA_SETUP_AND_EXECUTION_GUIDE.md`.*
