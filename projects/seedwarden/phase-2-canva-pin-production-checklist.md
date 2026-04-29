---
title: "Seedwarden Phase 2 — Canva Pin Production Checklist"
prepared: 2026-04-29
status: production-ready
scope: 5 pin templates — step-by-step Canva build instructions, batch workflow, keyboard shortcuts
cross-references:
  - pin-template-specs.md (full design specifications — colors, fonts, zone measurements)
  - CANVA_EXECUTION_PLAYBOOK.md (Brand Kit setup — hex codes, fonts)
  - phase-2-mockup-sourcing-inventory.md (which products have lifestyle images available for use)
---

# Phase 2 Canva Pin Production Checklist

**Purpose**: Step-by-step checklist for building all 5 pin templates and then executing the batch production run that fills the full Phase 2 Pinterest/Instagram pin library. Complete the one-time setup (Section 1) before any production. Then run batch sessions using Section 3.

**Output targets** (from `pin-template-specs.md`):
- 21 product pins (Template 1)
- 8–10 educational pins (Template 2)
- 10 lifestyle flat-lay pins (Template 3) — top 10 products by revenue priority
- 4–5 values pins (Template 4) — evergreen
- 4–6 carousel pin covers (Template 5)
- Total: approximately 50–60 pins across both Pinterest and Instagram formats

**Estimated total production time** (after setup is complete):
- Template build session: 3–4 hours (one-time)
- Batch pin production: 5–7 hours for the full 50–60 pin library
- Combined: 8–11 hours across 2–3 sessions

---

## Section 1 — One-Time Setup Checklist

Complete every item in this section once, before starting any template builds. These steps do not need to be repeated between sessions.

---

### 1.1 Brand Kit Configuration

Canva's Brand Kit lives under: Brand Hub > Brand Kit (left sidebar in Canva, or via your account Settings if on Canva Free — Free plan allows one Brand Kit).

**Colors — add all 6 in this order**:

- [ ] Add `#143b28` — name it "Deep Forest Green"
- [ ] Add `#1A3A2A` — name it "Deep Ink Green"
- [ ] Add `#F5EDD6` — name it "Warm Cream"
- [ ] Add `#EDE0C4` — name it "Parchment"
- [ ] Add `#8FA882` — name it "Sage"
- [ ] Add `#A0522D` — name it "Burnt Sienna"

Verify: After adding, the Brand Kit color swatches are visible when you click the color picker inside any design. If they do not appear automatically, click "Brand Kit" tab in the color panel.

**Fonts — add all 3 pairings**:

- [ ] Heading: Playfair Display, Bold — verify it appears in the font list. Canva has this font natively; search "Playfair Display" in the font selector.
- [ ] Body: Lato, Regular — native Canva font; search "Lato."
- [ ] Label/accent: Cormorant Garamond, Italic — native Canva font; search "Cormorant Garamond."

**Logo**:
- [ ] Upload the Seedwarden logo (from `projects/seedwarden/logos/`) to the Brand Kit
- [ ] Verify transparent background. If the logo file has a white fill, re-export from the source with transparency before uploading.

---

### 1.2 Upload Lifestyle Photos

All slot 4 lifestyle images that are ready must be uploaded to a Canva folder before the batch run begins. This prevents mid-session interruptions for uploading.

**Folder to create in Canva**: "Phase 2 Lifestyle Photos — Slot 4"

- [ ] Create the folder in Canva: Uploads > new folder > name it
- [ ] Upload all available slot 4 images from `projects/seedwarden/marketing/lifestyle-photos/etsy-ready/`
- [ ] Name confirmation: file names in the Canva upload match the product slug convention (`[slug]-slot4.jpg`) — do not rename in Canva, just confirm the originals are named correctly before uploading
- [ ] Note which products do not yet have a slot 4 image (stock compositing not yet complete) — those product pins will be built last, after compositing is done

---

### 1.3 Create a Master Template File for Each of the 5 Templates

Each master template is a single Canva design file at 1000×1500px. You will duplicate these files each time you produce a new pin — never edit the master directly.

**Naming convention for master files** (use exactly):
- `MASTER — Product Mockup Pin (Template 1)`
- `MASTER — Educational Hook Pin (Template 2)`
- `MASTER — Lifestyle Flat-Lay Pin (Template 3)`
- `MASTER — Values Perspective Pin (Template 4)`
- `MASTER — Carousel Pin Cover (Template 5)`

These files go in a Canva folder named: "Seedwarden — Phase 2 Pin Masters"

---

## Section 2 — Template Build Instructions (One Per Template)

### Template 1 — Product Mockup Pin

**Canvas size**: 1000×1500px
**Estimated build time**: 30–40 minutes

Steps:

- [ ] Create new design: custom dimensions 1000×1500px
- [ ] **Zone 1 (header band, 0–200px)**: Add a rectangle element, position at top, width 1000px, height 200px, fill `#143b28` (Deep Forest Green). Add text: "SEEDWARDEN", font Cormorant Garamond Italic, 28px, color `#F5EDD6` (Warm Cream), centered horizontally, vertically centered in the band (position text at y ~85px to center in 200px zone).
- [ ] **Zone 2 (product image, 200–1050px)**: Add a placeholder image element, position at x=0 y=200, width 1000px, height 850px. Place any test lifestyle photo here temporarily — it will be swapped in batch production. Add a vignette: rectangle element, same dimensions as Zone 2, fill `#F5EDD6`, opacity 15%, positioned over the bottom 200px of Zone 2 (y=850 to y=1050). This creates the fade into Zone 3.
- [ ] **Zone 3 (product name, 1050–1200px)**: Rectangle element, x=0 y=1050, width 1000px, height 150px, fill `#F5EDD6`. Add text: placeholder "Product Name Here", font Playfair Display Bold, 36px, color `#143b28`, centered horizontally, vertically centered in zone (y ~1115px).
- [ ] **Zone 4 (description + CTA, 1200–1380px)**: Rectangle element, x=0 y=1200, width 1000px, height 180px, fill `#F5EDD6` (matching Zone 3). Add three text elements stacked:
  - Line 1: placeholder "One-sentence product description", Lato Regular 22px, `#1A3A2A`, centered, y ~1220px
  - Line 2: "PDF Download — Instant Access", Cormorant Garamond Italic 18px, `#8FA882`, centered, y ~1265px
  - Line 3: placeholder "$00" — Lato Bold 24px, `#A0522D`, centered, y ~1308px
- [ ] **Zone 5 (footer band, 1380–1500px)**: Rectangle element, x=0 y=1380, width 1000px, height 120px, fill `#143b28`. Add text: "seedwarden.etsy.com", Lato Regular 18px, `#F5EDD6`, centered, y ~1430px. Add optional secondary line: "Free food sovereignty guides at link in bio", Cormorant Garamond 14px, `#8FA882`, centered, y ~1465px.
- [ ] Add logo: place from Brand Kit, position top-center or bottom-center. Confirm 60px clear space on all sides. Set to approximately 120px wide.
- [ ] Review: zoom to 100% and check all text is legible, no overflow, zones align cleanly without visible gaps.
- [ ] Name the file: `MASTER — Product Mockup Pin (Template 1)` — save to "Seedwarden — Phase 2 Pin Masters" folder.

---

### Template 2 — Educational Hook Pin

**Canvas size**: 1000×1500px
**Estimated build time**: 25–35 minutes

Steps:

- [ ] Create new design: 1000×1500px
- [ ] **Full-bleed background (Option A — photo)**: Add an image element, fill full canvas. Place a placeholder lifestyle photo. Add a Deep Ink Green overlay rectangle (`#1A3A2A`) at 50% opacity over the full canvas — this makes text readable over any photo background.
- [ ] **Build Option B variant (flat background)**: duplicate this design after completing Option A, replace the photo with a flat `#EDE0C4` (Parchment) fill, remove the overlay. You now have both variants — keep both as separate masters.
- [ ] **Zone 2 (hook text block, vertically centered)**: Add a rounded rectangle shape, fill `#F5EDD6` (Warm Cream), opacity 92%, rounded corners 16px, width ~860px, position it centered horizontally at y ~400px (upper-third position for Option A). Height adjusts based on text — start with 420px.
  - Header text inside: placeholder "5 Seeds Worth Saving This Year", Playfair Display Bold 48px, `#143b28`, centered inside the shape, top of text block
  - Supporting text below header: 3–4 placeholder lines, Lato Regular 20px, `#1A3A2A`, left-aligned with 24px padding inside the rounded rectangle
- [ ] **Zone 3 (category label, bottom 200px)**: Add a thin horizontal line element, Sage `#8FA882`, 1px, full width, at y=1300px. Below the line: text "SEEDWARDEN — SEED SAVING" (placeholder category), Cormorant Garamond Italic 16px, `#8FA882`, centered, y ~1340px.
- [ ] Review: check that text block is readable over the darkened photo (Option A) and that the flat option reads cleanly without the overlay.
- [ ] Save two master files:
  - `MASTER — Educational Hook Pin (Template 2 — Photo Background)`
  - `MASTER — Educational Hook Pin (Template 2 — Flat Background)`

---

### Template 3 — Lifestyle Flat-Lay Pin

**Canvas size**: 1000×1500px
**Estimated build time**: 20–25 minutes (this is the simplest template)

Steps:

- [ ] Create new design: 1000×1500px
- [ ] **Full-bleed photo**: Add an image element, fill full canvas. Set to 2400×2400px source — the image will overhang left and right. Pan to find the strongest 2:3 crop from the center of the flat-lay. The product should be visible and occupy the center zone of the composition.
- [ ] **Top product name bar**: Add a rectangle element, full width 1000px, height 70px, fill `#F5EDD6`, opacity 90%, position at y=60px (60px from top). Add text: placeholder "Product Name", Playfair Display Bold 28px, `#143b28`, centered in the bar.
- [ ] **Bottom CTA bar**: Add a rectangle element, full width 1000px, height 120px, fill `#143b28`, opacity 95%, position at y=1380px (bottom 120px). Add two text lines:
  - Line 1: placeholder "Core benefit in one line", Lato Regular 20px, `#F5EDD6`, centered, y ~1405px
  - Line 2: "Instant PDF download — seedwarden.etsy.com", Cormorant Garamond Italic 16px, `#8FA882`, centered, y ~1445px
- [ ] Review: the photo should dominate at least 85% of the visual area. If the bars are visually heavy, reduce opacity by 5–10%.
- [ ] Save: `MASTER — Lifestyle Flat-Lay Pin (Template 3)`

---

### Template 4 — Values / Perspective Pin

**Canvas size**: 1000×1500px
**Estimated build time**: 30–40 minutes

Steps:

- [ ] Create new design: 1000×1500px. Build two background variants — create the Green version first, then duplicate for the Parchment version.
- [ ] **Green background version**: Fill canvas `#143b28` (Deep Forest Green).
- [ ] **Upper third — botanical illustration (0–500px)**: Source a public domain botanical illustration from Wikimedia Commons (search "[plant name] botanical illustration public domain"). Download and upload to Canva. Position centered, approximately 200px wide, y=150px. Color: tint the illustration to Sage (`#8FA882`) using Canva's image tint or color filter if the source is a black line drawing.
  - Suggested illustrations (confirmed Wikimedia public domain): dandelion, seed pod, mason jar line drawing, or single leaf
  - If no suitable illustration is available: use a Canva native icon or the Canva "Elements" search — filter for line art style, botanical subject, in Sage color.
- [ ] **Middle third — statement (500–1000px)**: Add text block: placeholder statement "Growing your own food is political. It always has been." Playfair Display Bold, 46px, `#F5EDD6` (Warm Cream on Green background), centered, tight line spacing (line height ~1.2). Position vertically centered in the middle third, approximately y=550–800px. Below the statement: add a thin Sage horizontal rule (line element, `#8FA882`, 1px, 400px wide, centered). Below the rule: 1-sentence elaboration, Lato Regular 20px, `#F5EDD6`, centered, 1 line only.
- [ ] **Lower third (1000–1500px)**: Add text: source or context line ("From the Seedwarden shop" or specific product name), Cormorant Garamond Italic 18px, `#8FA882`, centered, y ~1100px. At the very bottom (y ~1440px): "SEEDWARDEN" in Lato Bold 14px, all caps, `#F5EDD6` or `#8FA882`, centered.
- [ ] Duplicate this design and change the background to `#EDE0C4` (Parchment). Swap text colors: statements become `#143b28`, "SEEDWARDEN" label becomes `#143b28` or `#8FA882`.
- [ ] Save two masters:
  - `MASTER — Values Perspective Pin (Template 4 — Green Background)`
  - `MASTER — Values Perspective Pin (Template 4 — Parchment Background)`

---

### Template 5 — Carousel Pin Cover

**Canvas size**: 1000×1500px (Pinterest); duplicate at 1080×1350px for Instagram
**Estimated build time**: 30–35 minutes

Steps:

- [ ] Create new design: 1000×1500px
- [ ] **Background**: Option A (Parchment `#EDE0C4`) or Option B (lifestyle photo + overlay). Build Option A first — it is cleaner and easier for inner slides. Create Option B by duplicating and adding photo + `#1A3A2A` overlay at 40% opacity.
- [ ] **Dominant number/hook (upper 60%, 0–900px)**: Add text: the large number "3" (or "5" — use a placeholder number), Playfair Display Bold, 130px, `#143b28`. Center it horizontally at y ~200px. Below the number: add the topic line, Playfair Display Regular 36px, `#1A3A2A`, centered, 2 lines maximum, y ~400px (adjust spacing so the two elements feel balanced, not cramped).
- [ ] **Subtext / engagement prompt (lower 30%, 900–1380px)**: Add "Swipe to learn" text, Lato Regular 20px, `#8FA882`, centered, y ~950px. Add a right-pointing chevron character "›" or "→" immediately after the text — in Canva, this is accessible via special characters or typed directly. Below: add one supporting line, Lato Regular 18px, `#1A3A2A`, centered, y ~995px — placeholder "What you'll know after this carousel."
- [ ] **Footer band (bottom 80px, 1420–1500px)**: Rectangle, full width, height 80px, fill `#143b28`. Add "SEEDWARDEN" Lato Bold 16px `#F5EDD6` centered. Optionally add product name below in Cormorant Garamond Italic 14px `#8FA882`.
- [ ] **Inner slide template**: Duplicate this design (remove the large number, add slide number glyph). Replace the large number with the inner slide topic (Playfair Display Bold 34px). Add supporting text area: Lato Regular 20px, left-aligned with 40px margin. Add slide number (2, 3, 4, 5) in top-left, Cormorant Garamond Italic 20px `#8FA882`. Keep footer identical.
- [ ] **Instagram variant**: Duplicate the cover at 1080×1350px. Adjust element positions and font sizes to fit the shorter canvas — the large number may need to reduce to 110px to avoid crowding.
- [ ] Save masters:
  - `MASTER — Carousel Pin Cover (Template 5 — Pinterest)`
  - `MASTER — Carousel Pin Cover (Template 5 — Instagram)`
  - `MASTER — Carousel Inner Slide (Template 5 inner)`

---

## Section 3 — Batch Production Workflow

Use this workflow for every batch session after the masters are built. The goal of each session is to produce as many pins as possible without context-switching — group similar pin types together, not products.

**Recommended batch order** (within a session):
1. All product pins (Template 1) for the products whose slot 4 images are available — complete all 21 before moving on
2. All lifestyle flat-lay pins (Template 3) — same images, different template, fast to produce after Template 1 run
3. Educational pins (Template 2) in batches by topic cluster
4. Values pins (Template 4) — 4–5 total, all at once
5. Carousel covers (Template 5) — build covers and inner slides together for one carousel before moving to the next

**Session target**: 12–15 pins per 90-minute session. At this rate, the full 50–60 pin library completes in 4 sessions.

---

### Per-Pin Production Steps (Product Pin — Template 1)

For each product pin after masters are built:

- [ ] Open: `MASTER — Product Mockup Pin (Template 1)` in Canva
- [ ] Keyboard shortcut: `Ctrl+D` (Windows) or `Cmd+D` (Mac) to duplicate the design. A new copy opens automatically.
- [ ] Rename the duplicate immediately: use the product slug + format, e.g., `seed-saving-field-manual-pin-v1`
- [ ] **Swap Zone 2 image**: Click the placeholder image in Zone 2. Keyboard shortcut: `R` to replace image, or drag the new slot 4 image from the Uploads panel directly onto the Zone 2 element. The zone boundaries hold automatically.
- [ ] **Update Zone 3 product name**: Double-click the product name text. Select all (`Ctrl+A` / `Cmd+A`), type the new product name. Check: does it fit on one line? If two lines are needed, reduce font size to 30px.
- [ ] **Update Zone 4 description**: Double-click line 1 (description), replace with the product's one-sentence benefit statement. Refer to the copy guide in `pin-template-specs.md` Section Template 1 for each product's recommended description text.
- [ ] **Update Zone 4 price** (optional): Update or delete the price line depending on whether the product's price is a conversion signal. Products priced $20+ should show the price. Products priced $5–$10 where the low price is an impulse driver should also show the price. Products at $13–$16 where price is neutral can omit the price line.
- [ ] **Export Pinterest format**: File > Download > JPEG > 1000×1500px > Quality 85%. Filename: `[slug]-pin.jpg`. Save to `projects/seedwarden/marketing/lifestyle-photos/pins/`.
- [ ] **Export Instagram format**: Change canvas size to 1080×1350px (`Resize` button, top right). Adjust the Zone 2 image crop to fill the shorter canvas. Export JPEG at 1080×1350px. Filename: `[slug]-social.jpg`.
- [ ] Log in WORKLOG.md if the slot 4 image used is from a stock source requiring attribution (iStock: no attribution needed; Wikimedia CC BY-SA: log attribution text).

**Time per product pin** (both formats): 4–7 minutes once in rhythm.

---

### Per-Pin Production Steps (Educational Hook Pin — Template 2)

- [ ] Duplicate: `MASTER — Educational Hook Pin (Template 2 — [Photo or Flat] Background)`
- [ ] Rename: e.g., `eduhook-seed-saving-which-seeds-v1`
- [ ] **Background** (photo version only): Replace the placeholder photo with the most relevant cluster lifestyle image or a curated Unsplash photo matching the topic. For flat background version: skip.
- [ ] **Hook text**: Double-click the hook text. Replace with the chosen hook from the hook text library in `pin-template-specs.md`. Keep to 1–2 lines. Keyboard shortcut: `Ctrl+A` to select all text in the element, then type.
- [ ] **Supporting text**: Replace the 3–4 supporting lines with the key points for this educational pin. Each line should be a standalone takeaway, not a continuation of a sentence.
- [ ] **Category label**: Update the "SEEDWARDEN — [CATEGORY]" text at the bottom to match the pin's topic (SEED SAVING, FOOD PRESERVATION, URBAN GROWING, FORAGING, FOOD SOVEREIGNTY).
- [ ] Export: same dual-format export as product pins.
- [ ] No WORKLOG entry needed for educational pins unless the background photo has attribution requirements.

**Time per educational pin**: 5–8 minutes.

---

### Per-Pin Production Steps (Lifestyle Flat-Lay Pin — Template 3)

These are the fastest pins to produce — the photo does most of the work.

- [ ] Duplicate: `MASTER — Lifestyle Flat-Lay Pin (Template 3)`
- [ ] Rename: e.g., `seed-saving-field-manual-flatlay-v1`
- [ ] **Background photo**: Replace the placeholder with the product's slot 4 image. The image will fill the canvas at 2400×2400px and overhang on two sides. Pan left-right to find the strongest 2:3 crop. Keyboard shortcut: double-click the image to enter crop mode, then drag to reposition.
- [ ] **Product name bar**: Update the product name text.
- [ ] **CTA bar**: Update the core benefit line (1 line). Keep the URL line as-is — it does not change between products.
- [ ] Export: dual format as above.

**Time per lifestyle pin**: 3–5 minutes. These are the fastest in the batch.

---

### Per-Pin Production Steps (Values Pin — Template 4)

- [ ] Duplicate: `MASTER — Values Perspective Pin (Template 4 — [Green or Parchment] Background)` — choose based on visual variety (alternate backgrounds across the 4–5 values pins).
- [ ] Rename: e.g., `values-hybrid-seeds-purchase-cycle-v1`
- [ ] **Statement text**: Replace the placeholder with the chosen statement from the values statement library in `pin-template-specs.md`. Keep to 2–3 lines maximum.
- [ ] **Elaboration line**: Replace the 1-sentence elaboration below the rule.
- [ ] **Source line**: Replace with "From the Seedwarden shop" or the specific product name if the statement is directly drawn from guide content.
- [ ] **Botanical illustration**: Check that the existing placeholder illustration is appropriate for this statement's topic. If not: swap the illustration element with a more relevant public domain botanical image or Canva line-art icon.
- [ ] Export: dual format. Note: values pins are evergreen — produce all 4–5 in one session and they last months before needing refresh.

**Time per values pin**: 8–12 minutes (slightly longer due to illustration check/swap).

---

### Per-Pin Production Steps (Carousel Cover — Template 5)

Carousel covers require building the inner slides in the same session — do not build a cover without the inner slides.

- [ ] Plan the full carousel (topic, number of slides, key points per slide) before opening Canva.
- [ ] Duplicate: `MASTER — Carousel Pin Cover (Template 5 — Pinterest)`.
- [ ] Rename: e.g., `carousel-3-preservation-types-cover-v1`.
- [ ] **Cover — large number/hook**: Update the dominant number and the topic line below it.
- [ ] **Cover — subtext**: Update the "What you'll know after this carousel" line.
- [ ] **Inner slides**: For each slide (2 through 5), duplicate the inner slide master. Update the slide number, the slide topic (Playfair Display Bold), and the supporting content (Lato Regular, left-aligned). Each slide should be self-contained — readable as a standalone without the cover.
- [ ] Export all slides: for Pinterest carousels, export each slide as a separate JPEG, named `[topic]-carousel-slide-[n].jpg`. For Instagram, Canva's multi-page design can be downloaded as a ZIP (all pages as separate files).
- [ ] Duplicate and adjust for Instagram format (1080×1350px) for the same carousel.

**Time per carousel (5 slides, both formats)**: 35–50 minutes. Plan 1 carousel per session — do not try to build multiple carousels in one pass.

---

## Section 4 — Keyboard Shortcuts Reference

These shortcuts apply in Canva web (Chrome/Firefox). Mac users substitute `Cmd` for `Ctrl`.

| Action | Shortcut | When to use |
|--------|----------|-------------|
| Duplicate current design (from homepage) | `Ctrl+D` | Before editing any master — always duplicate first |
| Duplicate selected element | `Ctrl+D` | Duplicate a text or shape element within a design |
| Select all elements | `Ctrl+A` | Select all to group-move, or within a text box to replace all text |
| Group selected elements | `Ctrl+G` | Group zone elements (background rect + text) for easier repositioning |
| Ungroup | `Ctrl+Shift+G` | Ungroup to edit individual elements |
| Enter crop mode (on image element) | Double-click | Pan and scale a photo within its container |
| Exit crop mode | `Esc` or click outside | Returns to normal element selection |
| Lock element position | Right-click > Lock | Lock background rectangles after positioning — prevents accidental dragging |
| Send to back / bring to front | `Ctrl+[` / `Ctrl+]` | Stack zone layers correctly (background behind overlay behind text) |
| Toggle rulers | `Ctrl+Shift+R` | Show/hide rulers when aligning zone boundaries |
| Zoom to fit | `Ctrl+Shift+H` | Reset view to see full canvas |
| Zoom in / out | `Ctrl+` / `Ctrl+-` | Zoom for detail work or overview |
| Undo | `Ctrl+Z` | After any accidental edit |
| Replace image (on selected image element) | `R` | Quick image swap without losing element position and size |
| Resize canvas | Resize button (top toolbar) | Switch between Pinterest (1000×1500) and Instagram (1080×1350) formats |
| Download | `Ctrl+Shift+E` | Opens download panel directly |

**Speed tip — template switching**: Keep multiple browser tabs open, one per master template. When batch-producing a mixed set of pins, you can duplicate from the correct master in the relevant tab without navigating back to the folder each time. Canva's tab state persists within a session.

**Speed tip — text replacement**: For product pins where only the product name and description change, use `Tab` to move between text elements after selecting the first one. This avoids mouse clicks between text boxes.

**Speed tip — image uploads**: Upload all slot 4 images to Canva in one batch before the session begins (Section 1.2). During production, drag directly from the Uploads panel onto the Zone 2 element. This is faster than using the "Replace" button for each image.

---

## Section 5 — Quality Check Before Export

Run this check on every pin before exporting. It takes 60–90 seconds per pin and prevents rework after export.

- [ ] Text legibility: zoom to 100%, read every text line. Can you read it easily at this size? If any line requires squinting, the font is too small.
- [ ] No text overflow: all text fits within its zone. No text is cut off at zone boundaries or canvas edges.
- [ ] Product name matches the Etsy listing title (shortened if over 50 characters).
- [ ] Correct lifestyle image is in Zone 2 (not a placeholder from the master).
- [ ] Logo is visible and has adequate clear space (60px on all sides).
- [ ] Color check: Deep Forest Green reads as clearly dark green, not black. Warm Cream reads as warm, not pure white.
- [ ] For lifestyle flat-lay pins: the product (guide pages or tablet screen) is visible in the photo. A pin where the product is not visible in the image does not communicate what is being sold.
- [ ] Export format selected correctly (JPEG not PNG — PNG files are larger and Pinterest does not benefit from PNG transparency for these pins).
