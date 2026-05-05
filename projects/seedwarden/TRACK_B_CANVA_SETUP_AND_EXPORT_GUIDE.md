---
title: "Canva Setup and Export Guide — Brand Kit, Zone Cards, and Social Templates"
date: 2026-05-05
session: 728
status: production-ready — user setup required for Brand Kit (30 min); then build begins
scope: Brand Kit setup, zone card export specs, pin template export, carousel export, upload sequence
references:
  - CANVA_SETUP_STATUS.md (Brand Kit spec and zone card status tracker)
  - CANVA_ZONE_CARD_DESIGN_GUIDE.md (step-by-step Canva build instructions)
  - CANVA_ZONE_CARD_BATCH_WORKFLOW.md (per-zone content tables)
  - CANVA_EXECUTION_PLAYBOOK.md (full Canva implementation guide)
  - pin-template-specs.md (5 pin template specifications)
  - ZONE_CARD_PRODUCTION_TIMELINE.md (build schedule)
---

# Canva Setup and Export Guide

**Purpose**: Technical specifications for every Canva deliverable in Track B. This covers
Brand Kit setup (user action), zone card build sequence and export settings, Pinterest pin
export settings, Instagram carousel export settings, and the Kit + Etsy upload sequence.

**Agent cannot access Canva** — this document gives you all specs in one place so your Canva
session is pure execution: no decisions, no research, no guessing.

---

## Part 1: Brand Kit Setup (One-Time, 30 Minutes)

**Must complete before any other Canva work.** The Brand Kit stores your colors, fonts, and
logo so you can access them with one click in every design.

### Step 1: Open Brand Hub
1. Log in to canva.com using wanka95@gmail.com
2. In the left sidebar, click "Brand Hub" (or find it at canva.com/brand-hub)
3. Click "Create a Brand Kit"
4. Name it: `Seedwarden`

### Step 2: Add Colors
Click "Add a color" and enter each hex code exactly as shown:

| Color Name | Hex Code | Click-path in Canva |
|---|---|---|
| Deep Forest Green | #143b28 | Add color > paste hex > Save |
| Deep Ink Green | #1A3A2A | Add color > paste hex > Save |
| Warm Cream | #F5EDD6 | Add color > paste hex > Save |
| Parchment | #EDE0C4 | Add color > paste hex > Save |
| Sage | #8FA882 | Add color > paste hex > Save |
| Burnt Sienna | #A0522D | Add color > paste hex > Save |

Also add these 4 zone band colors (used only in zone cards, but having them in the Kit saves
time during the card build):

| Zone Group | Hex Code | Zones |
|---|---|---|
| Cool band | #3D6B8A | Zones 3 and 4 |
| Temperate band | #2D5016 | Zones 5 and 6 |
| Warm band | #C9943A | Zones 7 and 8 |
| Hot band | #A0522D | Zones 9 and 10 (same as Burnt Sienna) |

**Total colors to add**: 10 (6 brand colors + 4 zone band colors). Zone bands can be skipped
and manually entered during the card build if you prefer to keep the Brand Kit minimal.

### Step 3: Add Fonts
Click "Add a font" and search by name:

| Role | Font Name | How to Add |
|---|---|---|
| Heading | Playfair Display | Search "Playfair Display" > select the result > Save |
| Body | Lato | Search "Lato" > select the result > Save |
| Accent | Cormorant Garamond | Search "Cormorant Garamond" > select the result > Save |

All three fonts are available free in Canva's font library. No upload required.

If Lato is not in Canva's library, substitute Source Sans 3 — same role, identical in use.

### Step 4: Upload Logo
1. Download `projects/seedwarden/logos/seedwarden_logo_1.png` to your device
2. In Brand Kit > Logos section > click "Upload a logo"
3. Select seedwarden_logo_1.png
4. Canva will store it for use in all designs without re-uploading

### Step 5: Save and Record
1. Click "Save" or "Publish" to confirm the Brand Kit
2. Copy the Brand Kit share link (Brand Kit > "Share" button)
3. Paste the share link into CANVA_SETUP_STATUS.md where it says "Canva Brand Kit URL: _____"

---

## Part 2: Zone Card Build Sequence and Export Specs

### Build Order

Build in this exact order. The order prevents zone-band color errors.

| Build Order | Zone | Zone Band Hex | Duplicate From | Time Estimate |
|---|---|---|---|---|
| 1 — master template | Zone 5 | #2D5016 Temperate | Blank US Letter canvas | 150-180 min |
| 2 | Zone 6 | #2D5016 Temperate | Zone 5 master | 30 min |
| 3 | Zone 3 | #3D6B8A Cool | Zone 5 master | 40 min |
| 4 | Zone 4 | #3D6B8A Cool | Zone 3 | 35 min |
| 5 | Zone 7 | #C9943A Warm | Zone 5 master | 40 min |
| 6 | Zone 8 | #C9943A Warm | Zone 7 | 35 min |
| 7 | Zone 9 | #A0522D Hot | Zone 5 master | 40 min |
| 8 | Zone 10 | #A0522D Hot | Zone 9 | 35 min |

**Total**: 7.5-9 hours across 3 weeks. See ZONE_CARD_PRODUCTION_TIMELINE.md for session schedule.

Full step-by-step Canva instructions for building the master template are in
`CANVA_ZONE_CARD_DESIGN_GUIDE.md`. Full content (every word for every zone) is in
`CANVA_ZONE_CARD_BATCH_WORKFLOW.md`. This document covers only export specs and upload.

### Placeholder Discipline

Before starting any card: set both footer links to their placeholder text. Replace before export.

| Footer Element | Placeholder During Build | Replace With |
|---|---|---|
| Etsy Zone Calendar listing | `[ETSY-ZONE-CALENDAR-LINK]` | Live Etsy listing URL when available |
| Kit landing page | `[KIT-LANDING-PAGE-URL]` | Kit landing page URL (from Action 3 in master guide) |

Rule: Never export a PDF with bracketed placeholder text visible. Do a visual check of all
footer text before every export.

### Zone Card Export Settings

When each card is complete and reviewed:

1. In Canva: File > Download
2. **File type**: PDF Print (not PDF Standard — Print gives higher quality)
3. **Flatten PDF**: Yes (check this box) — prevents font embedding issues
4. **Color profile**: CMYK is ideal if available; RGB is acceptable
5. **Filename**: Use exact naming convention below

**Naming convention**:
```
zone-3-quick-start-card.pdf
zone-4-quick-start-card.pdf
zone-5-quick-start-card.pdf
zone-6-quick-start-card.pdf
zone-7-quick-start-card.pdf
zone-8-quick-start-card.pdf
zone-9-quick-start-card.pdf
zone-10-quick-start-card.pdf
```

**Save location**: `projects/seedwarden/assets/zone-cards/`

The directory exists and is empty. After export, it should contain exactly 8 files.

### Zone Card Quality Check (Before Export)

For each card before downloading:
- [ ] Zone number in header matches the zone band color (Zone 3 and 4 = blue band, Zones 5 and 6 = green band, Zones 7 and 8 = amber band, Zones 9 and 10 = sienna band)
- [ ] Frost date range is correct for the zone (verify in CANVA_ZONE_CARD_BATCH_WORKFLOW.md)
- [ ] "This Month" section shows May 2026 content (May task blocks in CANVA_ZONE_CARD_BATCH_WORKFLOW.md)
- [ ] Footer: no bracketed placeholder text visible
- [ ] Footer: Kit landing page URL correct
- [ ] Seedwarden logo visible in header

### Kit Upload Sequence for Zone Cards

After all 8 PDFs are exported:

1. Upload each PDF to Google Drive
2. Set sharing: "Anyone with the link can view" (not "Anyone can edit")
3. For each file, copy the sharing link
4. These links go into Kit Email 1 (one per zone variant) — see TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md Step 4

Zone PDF Google Drive links (fill in after upload):

| Zone | Google Drive Link |
|---|---|
| Zone 3 | |
| Zone 4 | |
| Zone 5 | |
| Zone 6 | |
| Zone 7 | |
| Zone 8 | |
| Zone 9 | |
| Zone 10 | |

---

## Part 3: Pinterest Pin Export Specs

**Template reference**: All 5 pin templates are fully specified in `pin-template-specs.md`.
**Canva implementation**: Step-by-step in `CANVA_EXECUTION_PLAYBOOK.md`.

### Canvas Size

Set up new Canva design: Custom dimensions 1000px wide x 1500px tall (2:3 ratio)

### Export Settings

When each pin batch is ready:
1. File > Download
2. **File type**: JPEG
3. **Quality**: High (90% or maximum available)
4. **Compression**: Low
5. Do not use PNG for pins — JPEG file size is smaller and loads faster on Pinterest

### Naming Convention

```
[product-slug]-pin-[template-type].jpg
```

Examples:
```
survival-garden-regional-plans-pin-product.jpg
seed-saving-field-manual-pin-educational.jpg
native-plants-regional-guide-pin-lifestyle.jpg
```

**Save location**: `projects/seedwarden/marketing/lifestyle-photos/pins/`

### Scheduling Specs

- Schedule using Pinterest native scheduler (Publish > Schedule)
- Time slots: Tuesday through Friday, 8pm-11pm local time (peak Pinterest engagement)
- Spacing: minimum 2 hours between pins from the same account (Pinterest recommends not posting
  multiple pins within the same hour)
- Batch size for Week 1: 6 pins total, scheduled across Tuesday-Friday of first week

---

## Part 4: Instagram Carousel Export Specs

**Content reference**: Slide copy and sequence for every carousel is in `phase-2-social-content-calendar-60day.md`.
**First carousel**: Day 3 (5 slides, "5 guides for people who want to grow more food")

### Canvas Size

Set up new Canva design: 1080px wide x 1350px tall (4:5 ratio, optimal for Instagram feed reach)

Alternatively: 1080px x 1080px (square) — slightly less feed real estate but simpler to design.
Use 4:5 for all carousels for consistency.

### Slide Structure (Day 3 Carousel)

| Slide | Content | Image |
|---|---|---|
| 1 — Cover | "5 Guides for People Growing Their Own Food in 2026" + Seedwarden logo | Brand pattern or product mockup overlay |
| 2 | Survival Garden Regional Plans — product name + one-sentence description + price | survival-garden-regional-plans-mockup.png from mockups/ |
| 3 | Hunting, Fishing & Trapping Field Manual — same format | hunting-fishing-trapping-field-manual-mockup.png |
| 4 | Livestock Field Manual — same format | small-scale-livestock-field-manual-mockup.png (from stock-raw/ parent dir reference) |
| 5 — Final slide | CTA: "All guides at the link in bio. Get your zone-specific free card while you're there." | Brand pattern, large text |

Full slide copy with exact text is in `phase-2-social-content-calendar-60day.md` Day 3.

### Export Settings

1. File > Download
2. **File type**: PNG (higher quality than JPEG for graphics and text)
3. **Export all pages**: Yes (exports all 5 slides as separate files)
4. Canva will download a ZIP — unzip and use individual slide files

### Naming Convention

```
carousel-day3-slide1.png
carousel-day3-slide2.png
carousel-day3-slide3.png
carousel-day3-slide4.png
carousel-day3-slide5.png
```

Upload to Instagram: tap the multi-image icon when creating a post, add all 5 slides in order.

---

## Part 5: Lifestyle Photo Export Specs (Post-Shoot Editing)

After editing shoot photos in Lightroom Mobile or Snapseed:

### Etsy Listing Images (Slots 4 and 5)

- **Dimensions**: 2400px x 2400px (square, 1:1)
- **Format**: JPEG
- **Quality**: 90% or higher
- **Color space**: sRGB
- **Naming convention**: `[product-slug]-slot4.jpg` and `[product-slug]-slot5.jpg`

Examples:
```
seed-saving-field-manual-slot4.jpg
seed-saving-field-manual-slot5.jpg
fermented-preserved-harvest-handbook-slot4.jpg
fermented-preserved-harvest-handbook-slot5.jpg
```

**Save location**: `projects/seedwarden/marketing/lifestyle-photos/etsy-ready/`

### Social Variant Crops (Optional — Produce If Time Allows)

If time allows after Etsy-ready exports:
- **Instagram (4:5)**: 1080px x 1350px, JPEG, name: `[product-slug]-ig.jpg`
- **Pinterest (2:3)**: 1000px x 1500px, JPEG, name: `[product-slug]-pin.jpg`

**Save location**: `projects/seedwarden/marketing/lifestyle-photos/pins/`

**Priority note**: Etsy-ready exports (2400x2400) take priority. Skip social variants if time
is short — Canva can crop these from the full-size files later, or use mockup images for
social through Week 4.

---

## Part 6: Etsy Upload Sequence

When lifestyle photos are ready, upload by cluster priority. Do not wait for all 21 products.

| Upload Priority | Cluster | Products | Target Date |
|---|---|---|---|
| 1 | D — Stock composited | Survival Garden, Hunting Manual, Livestock Manual, Meat/Fish Preservation | May 15 |
| 2 | E — Wikimedia/Pexels | Native Plants Regional Guide | May 15 (alongside Cluster D) |
| 3 | C — Physical (kitchen) | Harvest Preservation, Fermented Harvest, Grow Your Own Hot Sauce | May 15-17 |
| 4 | B — Physical (urban/window) | Container Blueprint, Apartment Growing, Apartment Plant Catalog, Seed Swap Kit | May 16-18 |
| 5 | A — Physical (flat-lay) | All 9 seed/garden products | May 16-20 |

**Etsy upload rule**: Add exactly 2 images per listing (slot 4 and slot 5). Do not change
any other listing field during this upload — isolate the photography variable for clean
before/after conversion data.

**Attribution for Native Plants slot 4**: The Wikimedia image (Joe Mabel, CC BY-SA 3.0)
requires attribution in the Etsy listing description footer. Add this line:
"Background photo (listing image 4): Joe Mabel, CC BY-SA 3.0, via Wikimedia Commons."

**Log all uploads in WORKLOG.md** with product slug, date, and slot numbers.

---

## Part 7: Cluster D+E Compositing (May 15)

Clusters D and E use staged stock images from `assets/stock-raw/`. These require a Canva
compositing step before upload to Etsy — overlaying the product PDF mockup image on top of
the stock scene.

### Stock Images Already Staged

| Product | Slot 4 File | Slot 5 File | Stock Directory |
|---|---|---|---|
| Survival Garden Regional Plans | survival-garden-regional-plans-slot4.jpg | survival-garden-regional-plans-slot5.jpg | assets/stock-raw/survival-garden-regional-plans/ |
| Hunting, Fishing & Trapping Manual | hunting-fishing-trapping-field-manual-slot4.jpg | hunting-fishing-trapping-field-manual-slot5.jpg | assets/stock-raw/hunting-fishing-trapping-field-manual/ |
| Small Scale Livestock Manual | small-scale-livestock-field-manual-slot4.jpg | small-scale-livestock-field-manual-slot5.jpg | assets/stock-raw/small-scale-livestock-field-manual/ |
| Meat & Fish Preservation Manual | meat-fish-preservation-field-manual-slot4.jpg | meat-fish-preservation-field-manual-slot5.jpg | assets/stock-raw/meat-fish-preservation-field-manual/ |
| Native Plants Regional Guide | native-plants-regional-guide-slot4.jpg | native-plants-regional-guide-slot5.jpg | assets/stock-raw/native-plants-regional-guide/ |

### Compositing Steps (in Canva)

1. Create new design: 2400px x 2400px
2. Upload the stock background image (e.g., survival-garden-regional-plans-slot4.jpg)
3. Upload the corresponding product mockup from `mockups/` directory
4. Position the mockup on top of the background, scaled to occupy 50-60% of the frame
5. Adjust transparency on mockup if needed (stock photos should show through slightly)
6. Export as JPEG, 2400x2400px
7. Save to `marketing/lifestyle-photos/etsy-ready/` with naming convention (e.g., `survival-garden-regional-plans-slot4.jpg`)

Test this compositing technique on one product (Survival Garden) before running all 10.
If the result is unconvincing, use a flat 2D label overlay instead — keep the stock image
as-is and add the product cover as a label/card element in the corner.

Log all composited filenames in WORKLOG.md.

---

## Part 8: Social Media Scheduling Setup (Buffer/Later)

**When**: May 25-29 (after lifestyle photos are edited and launch-week posts are ready)

### Buffer Setup
1. Go to buffer.com > Start free trial (or log in)
2. Connect Instagram Business account (requires Facebook Business Manager connection)
3. Connect Pinterest Business account
4. TikTok: Buffer does not support native TikTok upload — schedule TikTok reminders in
   Buffer as drafts, then upload natively on the day

### Later Setup (Alternative)
1. Go to later.com > Start free trial
2. Connect Instagram, Pinterest, TikTok accounts
3. Later supports native TikTok scheduling on paid plans; free plan sends a push notification
   reminder to upload manually

### Loading the 60-Day Calendar
- Source: `phase-2-social-content-calendar-60day.md`
- Each day's post has: hook, caption text, hashtags, and CTA
- Copy caption from the calendar into Buffer/Later draft
- Attach the corresponding image or video file
- Set posting time per platform cadence below

### Platform-Specific Posting Times

| Platform | Best Times (local) | Frequency |
|---|---|---|
| Instagram (Reels) | Tuesday and Thursday, 7pm-9pm | 1-2 Reels per week |
| Instagram (Carousels) | Monday and Wednesday, 12pm-2pm | 2 per week |
| Instagram (Stories) | Daily, any time | 5-7 per week |
| Pinterest (Pins) | Tuesday-Friday, 8pm-11pm | 7-10 per week |
| TikTok | Tuesday, Thursday, Saturday, 7pm-9pm | 3-4 per week |

### Hashtag Sets (Pre-Built)

Copy these hashtag sets into posts. Use 20-30 hashtags on Instagram Reels (hidden in first
comment or caption), 3-5 on Pinterest, and 3-8 on TikTok.

**Seed saving / heirloom set**:
`#seedsaving #heirloomseeds #openpollinated #seedswap #growyourown #foodsovereignty #heirloomgarden #seedlibrary #saveyourseeds #sustainablegarden`

**Foraging / wild edibles set**:
`#foraging #wildedibles #wildcrafting #forage #wildplants #edibleplants #nativeplants #plantidentification #wildcooking #forager`

**Urban growing / apartment set**:
`#urbangarden #containergardens #balconygarden #apartmentgarden #smallspacegarden #indoorgarden #urbangardening #growfood #cityfarming`

**Food preservation set**:
`#foodpreservation #canning #fermentation #homesteadkitchen #preserving #lactofermentation #wildfermentation #hotpeppers #harvestseason`

**General Seedwarden brand**:
`#seedwarden #fieldguides #realfood #growyourfood #foodindependence #practicalskills #homesteadskills #knowyourfood`

---

*Prepared: 2026-05-05. Session 728. Brand Kit specs source: CANVA_SETUP_STATUS.md and TRACK_B_LAUNCH_STATUS.md
Condition 2. Export specs reflect May 2026 Canva Free tier capabilities. Canva Pro not required for
any Track B deliverable.*
