---
title: "Phase 3 Canva Starter Projects — Setup and Template Instructions"
date: 2026-05-27
status: production-ready
purpose: >
  Step-by-step instructions for building the five Phase 3 Canva starter templates
  (bundle card, info block, testimonial, ingredient detail, dosage reference).
  Templates are built once on June 21, then reused across the June 22–July 13 sprint.
  Typography and colors are pre-loaded; sprint work is content insertion only.
cross-references:
  - PHASE_3_DESIGN_SYSTEM.md (authoritative specs for all layout templates)
  - PHASE_3_CANVA_ADAPTATION_PLAN.md (pre-sprint checklist)
  - canva-phase-3-adaptation-guide.md (palette source, stock image guidance)
tags: [seedwarden, phase-3, canva, templates, starter-projects]
---

# Phase 3 Canva Starter Projects

**Build deadline**: June 21, 2026 (day before sprint Day 1)  
**Total build time**: 2.5–3 hours across two sessions  
**Prerequisite**: Phase 3 colors loaded in Canva Brand Kit (see Brand Kit Load Sequence in `PHASE_3_DESIGN_SYSTEM.md` Part 6)

This document replaces per-card setup time during the June 22–July 13 production sprint. Each template is built once, duplicated five times (one per bundle), and entered with bundle-specific content during the sprint. Design decisions are pre-locked — sprint work is text and image insertion only.

---

## Session 1: June 21 Morning (90 minutes)

Build Templates 1 and 2 (the highest-production-volume templates).

---

## Template 1 — Bundle Card Cover

**Purpose**: Etsy primary listing image (slot 1). Five variants — one per bundle.  
**Canvas**: 2400×2400 px  
**Build time**: 35 minutes for master; 10 minutes per bundle variant (50 minutes total for all 5)

### Build the Master (Women's Health as the base)

**Step 1 — Create the canvas**

```
Canva > Create a design > Custom size > 2400 × 2400 px
Rename the file: "Phase3-BundleCard-MASTER"
Set page background: Clinical Cream (#F9F5F0)
```

**Step 2 — Header block**

```
Add > Elements > Rectangle
Width: 2400px, Height: 600px
Position: x=0, y=0 (anchored top-left)
Fill color: Deep Burgundy #8B3E3E (from Brand Kit)
```

**Step 3 — Apothecary Gold accent rule**

```
Add > Elements > Line (horizontal)
Width: 2400px, Height: 2px
Position: x=0, y=600px
Color: Apothecary Gold #D4AF37
```

**Step 4 — Series label text**

```
Add > Text > Text box
Font: Lato
Size: 14pt
Weight: Regular
Case: ALL CAPS (use Canva's caps toggle, not manual typing)
Letter spacing: +40
Color: Clinical Cream #F9F5F0
Content: "SEEDWARDEN MEDICINAL HERBS GUIDE"
Position: centered horizontally in header, y=70px from top of header block
```

**Step 5 — Bundle title text**

```
Add > Text > Text box
Font: Playfair Display
Size: 48pt
Weight: Bold
Color: Apothecary Gold #D4AF37
Content: "Women's Health Herbs"
Position: centered horizontally in header, y=200px from top
```

**Step 6 — Species list text**

```
Add > Text > Text box
Font: Cormorant Garamond
Size: 14pt
Weight: Italic (species names are always italicized)
Color: Clinical Cream #F9F5F0
Content (one species per line, 5 lines):
  Black Cohosh · Vitex · Red Clover · Calendula · Lavender
Position: centered horizontally in header, y=370px from top
Note: use a centered dot (·) or thin separator between species names on one line
      to save vertical space; or use 5 short lines if space allows
```

**Step 7 — Hero image placeholder**

```
Add > Elements > Rectangle (placeholder only — not a design element)
Width: 2400px, Height: 1440px
Position: x=0, y=602px
Fill: #CCCCCC (neutral gray — this gets replaced by the real hero image)
Add a text label over it: "INSERT HERO IMAGE HERE" in Lato 24pt, #666666
This placeholder is deleted when the real image is inserted during the sprint.
```

**Step 8 — Footer band**

```
Add > Elements > Rectangle
Width: 2400px, Height: 360px
Position: x=0, y=2040px
Fill: Dark Charcoal #2C2C2C
```

**Step 9 — Seedwarden wordmark in footer**

```
Upload > Seedwarden logo PNG (transparent background)
Source file: projects/seedwarden/logos/ (use the existing logo file)
Position: left-aligned in footer, x=80px, vertically centered in footer band
Height: ~120px (maintain aspect ratio)
```

**Step 10 — Footer label text**

```
Add > Text > Text box
Font: Lato
Size: 12pt
Weight: Regular
Color: Apothecary Gold #D4AF37
Content: "Educational Guide"
Position: right-aligned in footer, x=~2320px, vertically centered in footer band
```

**Step 11 — Save and verify**

```
File > Download > JPEG (Quality: 95%)
Open the downloaded file.
Resize your image viewer to show the file at approximately 170px wide.
Verify: bundle title "Women's Health Herbs" is legible at this size.
If legible: master is approved. Proceed to variants.
If not: increase bundle title font size by 4pt and retest.
```

### Create Bundle Variants (10 minutes each)

With the master saved, create five duplicates:

```
In Canva project view: right-click "Phase3-BundleCard-MASTER" > Make a copy
Rename copy: "Phase3-WomensHealth-Cover-v1"
```

Women's Health (v1) is already complete — it matches the master.

```
Duplicate master again > rename "Phase3-Respiratory-Cover-v1"
Changes to make:
  - Header rectangle color: change to Sage Green #6B8E6F
  - Bundle title text: "Respiratory Health Herbs"
  - Species list: Elderberry · Echinacea · Thyme · Mullein · Lemon Balm
  - Hero image placeholder: leave as-is (will be replaced during sprint)
```

```
Duplicate master again > rename "Phase3-Immunity-Cover-v1"
Changes:
  - Header color: Deep Burgundy #8B3E3E (same as master — no color change needed)
  - Bundle title: "Immunity Support Herbs"
  - Species list: Goldenseal · Echinacea · Ashwagandha · Elderberry · Astragalus
```

```
Duplicate master again > rename "Phase3-Sleep-Cover-v1"
Changes:
  - Header color: Muted Lavender #9B8BA0
  - Bundle title: "Sleep and Nervines Guide"
  - Species list: Passionflower · Valerian · Lemon Balm · Lavender · Chamomile
```

```
Duplicate master again > rename "Phase3-Digestive-Cover-v1"
Changes:
  - Header color: Sage Green #6B8E6F (same as Respiratory)
  - Bundle title: "Digestive Support Herbs"
  - Species list: Dandelion · Ginger · Calendula · Lemon Balm · Marshmallow Root
```

**Status after Session 1, Template 1**: Five bundle card templates ready for hero image insertion. All text is live. Sprint Day 1 task = insert one hero image per cover (15 minutes per cover).

---

## Template 2 — Info Block (Interior Page / Zone Card)

**Purpose**: Interior PDF pages (8.5×11in) and zone cultivation cards. One master; adapted per bundle by changing the header color.  
**Canvas**: 8.5 × 11 in (Canva uses inches for print templates)  
**Build time**: 25 minutes for master

**Step 1 — Create canvas**

```
Canva > Create a design > Custom size > 8.5 in × 11 in
Rename: "Phase3-InfoBlock-MASTER"
Page background: Clinical Cream #F9F5F0
```

**Step 2 — Running header band**

```
Add > Elements > Rectangle
Width: full page width (8.5in)
Height: 0.5 in
Position: top of page
Fill: Deep Burgundy #8B3E3E
(changed per-bundle during sprint)
```

**Step 3 — Gold accent rule below header**

```
Add > Elements > Line
Width: full page width
Height: 1px
Position: directly below header band (y = 0.5in)
Color: Apothecary Gold #D4AF37
```

**Step 4 — Seedwarden logo (small) in header**

```
Upload logo PNG, place left-aligned in header band
Height: 0.3in, maintain aspect ratio
Position: x=0.3in from left edge, vertically centered in header
```

**Step 5 — Bundle name label in header**

```
Add > Text
Font: Lato, 9pt, Regular, Clinical Cream
Content: "[BUNDLE NAME]" (placeholder — replaced per-bundle)
Position: right-aligned in header, x=~8.2in, vertically centered
```

**Step 6 — Species heading block**

```
Add > Text (two separate text boxes, stacked)
Text box 1: Playfair Display, 22pt, Bold, Dark Charcoal
  Content: "Common Name" (placeholder)
  Position: x=0.75in, y=0.75in

Text box 2: Cormorant Garamond, 18pt, Italic, Dark Charcoal
  Content: "Genus species" (placeholder — italics are the standard for Latin names)
  Position: x=0.75in, y=1.1in
```

**Step 7 — Apothecary Gold divider under species heading**

```
Add > Elements > Line
Width: 7.0in (text width — page width minus 0.75in margins each side)
Height: 1px
Color: Apothecary Gold #D4AF37
Position: x=0.75in, y=1.45in
```

**Step 8 — Body text zone (main content)**

```
Add > Text
Font: Lato, 11pt, Regular, Dark Charcoal #2C2C2C
Line height: 145% (click the text box > spacing > line height 1.45)
Content: "[Body text placeholder — content inserted during sprint]"
Width: 7.0in (margins 0.75in each side)
Position: x=0.75in, y=1.6in
Height: approximately 5.5in (leave room for conservation sidebar below)
```

**Step 9 — Conservation sidebar box (right column)**

```
Note: this is a sidebar element that occupies the right ~2.5in of the body zone.
The body text in Step 8 should be set to left column width (~4.0in) when a sidebar is present.

Add > Elements > Rectangle (bordered box)
Width: 2.5in
Height: 2.0in
Position: x=5.75in (right margin), y=4.0in (below mid-page)
Fill: Clinical Cream #F9F5F0
Border: 1.5pt, Apothecary Gold #D4AF37

Add text inside box:
  "CONSERVATION NOTE" — Lato, 10pt, Bold All Caps, Apothecary Gold
  (positioned at top of box with 0.1in padding)
  
  Sidebar body text — Lato, 10pt, Regular, Dark Charcoal
  (placeholder text: "Conservation status and sourcing notes go here.")
```

**Step 10 — FTC framing footer**

```
Add > Elements > Line (separator)
Width: 7.0in, 1px, Apothecary Gold #D4AF37
Position: x=0.75in, y=10.1in

Add > Text
Font: Lato, 9pt, Italic, #5A5A5A
Content: "Traditionally used for [purpose]. This information is for educational purposes only 
and is not intended to diagnose, treat, cure, or prevent any disease. 
Consult a qualified healthcare practitioner before use."
Width: 7.0in, position x=0.75in, y=10.2in
```

**Step 11 — Page number footer**

```
Add > Text
Font: Lato, 9pt, Regular, #7A7060
Content: "1  |  SEEDWARDEN"
Position: bottom of page, centered, y=10.7in
```

**Step 12 — Save and test**

```
File > Download > PDF (Print)
Open in PDF reader. Zoom to 100%.
Verify: body text at 11pt is readable without magnification.
Verify: Apothecary Gold sidebar border is visible (not washed out).
Verify: FTC footer is present at bottom.
If any element misaligned: correct now before duplicating.
```

**Session 1 complete** — two core templates built, five bundle card variants ready.

---

## Session 2: June 21 Afternoon (60 minutes)

Build Templates 3, 4, and 5.

---

## Template 3 — Testimonial Block

**Purpose**: Social media (Pinterest, Instagram) — buyer testimonials and authority quotes.  
**Canvas**: 1000×1500 px  
**Build time**: 20 minutes

**Step 1 — Canvas and image zone**

```
Canva > Create a design > Custom size > 1000 × 1500 px
Rename: "Phase3-Testimonial-MASTER"

Add image placeholder at top:
  Rectangle, full width, 675px tall, fill #CCCCCC (placeholder for herb photo)
  Label: "INSERT HERB PHOTO HERE" Lato, 18px, #666666, centered

Add color overlay on image zone:
  Rectangle, 1000px wide, 675px tall, fill Deep Burgundy #8B3E3E, opacity 45%
  Position over the image placeholder
  This overlay stays during sprint — only the photo beneath it changes
```

**Step 2 — Bundle label on image**

```
Add > Text
Font: Lato, 14px, All Caps, Letter-spacing +40
Color: Clinical Cream #F9F5F0
Content: "[BUNDLE NAME]"
Position: top-right corner of image zone, 30px margin from top and right edges
```

**Step 3 — Quote zone (Clinical Cream background)**

```
Add > Elements > Rectangle
Width: 1000px, Height: 525px
Position: x=0, y=675px
Fill: Clinical Cream #F9F5F0
```

**Step 4 — Gold left border accent**

```
Add > Elements > Rectangle (used as a vertical line — thin rectangle)
Width: 4px, Height: 480px
Position: x=40px, y=690px
Fill: Apothecary Gold #D4AF37
```

**Step 5 — Quote text**

```
Add > Text
Font: Cormorant Garamond, 36px, Italic
Color: Dark Charcoal #2C2C2C
Content: "[Buyer quote goes here. One to three sentences. No quotation marks.]"
Position: x=60px (right of gold border), y=700px
Width: 880px
Line height: 145%
```

**Step 6 — Attribution line**

```
Add > Text
Font: Lato, 22px, Regular
Color: Dark Charcoal #2C2C2C
Content: "— Name, RH-AHG, Location"
Position: x=60px, below quote text, approximately y=1050px
```

**Step 7 — Thin rule below attribution**

```
Add > Elements > Line
Width: 860px, Height: 1px
Color: Apothecary Gold #D4AF37
Position: x=60px, y=~1095px
```

**Step 8 — CTA footer band**

```
Add > Elements > Rectangle
Width: 1000px, Height: 300px
Position: x=0, y=1200px
Fill: Deep Burgundy #8B3E3E (changes to correct bundle color per variant)

CTA text in footer:
  Font: Lato, 28px, Bold, Clinical Cream
  Content: "Get the Women's Health Guide"
  Position: centered horizontally, y=1230px

URL text:
  Font: Lato, 20px, Regular, Clinical Cream, opacity 80%
  Content: "seedwarden.com"
  Position: centered, y=1310px
  
Seedwarden wordmark:
  Upload logo PNG, Clinical Cream recolor if needed
  Position: bottom-left of footer, x=40px, y=1410px, height ~60px
```

**Step 9 — Export and verify**

```
File > Download > PNG
Open the file.
Verify: testimonial quote text is readable at viewing size.
Verify: gold left border is visible on Clinical Cream background.
Verify: CTA text in footer has sufficient contrast (Clinical Cream on Burgundy — approved pairing).
```

---

## Template 4 — Ingredient Detail (Instagram 1080×1080px)

**Purpose**: Social species spotlights — one herb per post, species name + key facts.  
**Canvas**: 1080×1080 px  
**Build time**: 20 minutes

**Step 1 — Canvas and top band**

```
Canva > Post > Instagram Post (1080 × 1080 px)
Rename: "Phase3-IngredientDetail-MASTER"
Background: Clinical Cream #F9F5F0

Top band:
  Rectangle, 1080px wide, 60px tall, Deep Burgundy #8B3E3E
  "SEEDWARDEN" text: Lato, 16px, All Caps, Clinical Cream, right-aligned, 30px margin
```

**Step 2 — Species photo placeholder (right side)**

```
Add > Elements > Rectangle
Width: 540px, Height: 560px
Position: x=540px, y=60px
Fill: #CCCCCC
Label: "INSERT SPECIES PHOTO"

Add a 2px Apothecary Gold border around the placeholder:
  This can be done by adding a slightly larger rectangle (544px × 564px) behind the gray one,
  filled with Apothecary Gold #D4AF37, creating a visible border frame.

Drop shadow:
  Select photo placeholder > Edit image > Shadow > Offset
  Opacity: 20%, Blur: 8px, Offset X: 3px, Offset Y: 5px
```

**Step 3 — Species name block (left side)**

```
Common name text:
  Font: Playfair Display, 36px, Bold, Dark Charcoal #2C2C2C
  Content: "Black Cohosh" (placeholder)
  Position: x=40px, y=80px
  Width: 480px

Latin name text:
  Font: Cormorant Garamond, 22px, Italic
  Color: Deep Burgundy #8B3E3E (the bundle's header color — signals the bundle)
  Content: "Actaea racemosa" (placeholder)
  Position: x=40px, y=140px
  Width: 480px
```

**Step 4 — Divider below name block**

```
Add > Elements > Line
Width: 460px, Height: 1px
Color: Apothecary Gold #D4AF37
Position: x=40px, y=195px
```

**Step 5 — Key facts bullets**

```
Add > Text
Font: Lato, 24px, Regular, Dark Charcoal #2C2C2C
Content (3 lines with Apothecary Gold en-dash bullet):
  "— Traditional use: hormonal balance"
  "— Primary action: adaptogenic"
  "— Harvest: fall, year 3+"
Position: x=40px, y=215px
Width: 480px
Line height: 145%
Note: type the bullet character "—" manually (en-dash). Canva's bullet list 
      formatting can be unreliable; use a simple text block with line breaks.
```

**Step 6 — Bottom band**

```
Add > Elements > Rectangle
Width: 1080px, Height: 80px
Position: anchored to bottom (y=1000px)
Fill: Clinical Cream #F9F5F0

Add 2px Apothecary Gold top border line:
  Line element, 1080px wide, 2px, Apothecary Gold, y=1000px

Footer text:
  Font: Lato, 18px, Regular, Dark Charcoal #2C2C2C
  Content: "Full guide: seedwarden.com"
  Position: centered horizontally, y=1020px
```

**Step 7 — Export and verify at 50px size**

```
File > Download > JPEG
Zoom to 25% in Canva (or resize in image viewer to ~270px wide).
This simulates approximate social feed thumbnail size.
Verify: common species name is readable. Latin name does not need to be readable at this size.
Verify: Apothecary Gold divider line is visible against Clinical Cream background.
```

---

## Template 5 — Dosage Reference Card (8.5×11in PDF)

**Purpose**: Interior PDF quick-reference page — one per species in each guide.  
**Canvas**: 8.5 × 11 in  
**Build time**: 20 minutes  
**Note**: This extends the Info Block template (Template 2) with specific dosage table formatting. Build as a separate file — do not modify the Info Block master.

**Step 1 — Canvas setup**

```
Canva > Custom size > 8.5 in × 11 in
Rename: "Phase3-DosageCard-MASTER"
Page background: Clinical Cream #F9F5F0
```

**Step 2 — Copy running header and species heading from Template 2**

```
Open Template 2 (Phase3-InfoBlock-MASTER) in a separate Canva tab
Select all elements in the header section (top 1.5in):
  - Header band rectangle
  - Gold accent rule
  - Logo
  - Bundle name label
  - Species heading text boxes
  - Gold divider under species heading
Copy (Cmd+C / Ctrl+C)
Switch to Template 5 tab
Paste (Cmd+V / Ctrl+V)
The elements land in approximately the correct position.
Adjust positioning if needed to match the spec.
```

**Step 3 — Two-column preparation table**

```
Left column (Preparation Methods) — x=0.75in, y=1.6in, width=3.5in:

  Column header box:
    Rectangle: 3.5in wide, 0.35in tall, fill Deep Burgundy #8B3E3E
    Text: "PREPARATION METHODS" Lato, 10pt, Bold All Caps, Clinical Cream
    Centered in the header box

  Method entry rows (3 rows, alternating background):
    Row A background: Clinical Cream #F9F5F0
    Row B background: #F0EDE8 (very light warm tint, one step darker than Clinical Cream)
    Each row height: ~0.8in
    Row content text: Lato, 11pt, Dark Charcoal
    Method label: "Standard Infusion" Lato, 10pt, Bold, Dark Charcoal
    Dosage text: "1 tsp per cup, steep 10 min. 2–3 cups daily." Lato, 11pt, Regular
    
    Build 3 rows for: Standard Infusion, Tincture, Decoction (most common forms)
    Leave method content as placeholder text — filled during sprint

Right column (Safety and Conservation) — x=4.5in, y=1.6in, width=3.5in:

  Safety Notes box:
    Rectangle: 3.5in wide, 2.0in tall
    Border: 1.5pt, Apothecary Gold #D4AF37
    Fill: Clinical Cream #F9F5F0
    "SAFETY NOTES" label: Lato, 10pt, Bold All Caps, Apothecary Gold #D4AF37
    Position: top of box with 0.1in padding
    Body text: Lato, 10pt, Regular, Dark Charcoal (placeholder: "Contraindications noted here.")

  Conservation Status box (below Safety Notes, 0.15in gap):
    Rectangle: 3.5in wide, 1.5in tall
    Border: 1.5pt, Apothecary Gold #D4AF37
    Fill: Clinical Cream #F9F5F0
    "CONSERVATION STATUS" label: Lato, 10pt, Bold All Caps, Apothecary Gold #D4AF37
    Body text: Lato, 10pt, Regular, Dark Charcoal
    Placeholder: "At-risk or common designation + sourcing recommendation."
    Note: For Goldenseal (Immunity bundle), this box gets the CITES Appendix II note.
           For common herbs, it reads "Widely cultivated — no conservation concern."
```

**Step 4 — FTC footer (same as Template 2)**

```
Copy the FTC footer elements from Template 2:
  - 1px Apothecary Gold separator line at y=10.1in
  - Lato 9pt Italic #5A5A5A disclaimer text
Paste into Template 5. Adjust position if needed.
```

**Step 5 — Export and test**

```
File > Download > PDF (Print)
Print one test page at 100% on a standard printer (or use Print Preview at 100%).
Verify: all body text is readable when printed.
Verify: the two-column layout does not collapse or overflow.
Verify: Gold borders on sidebar boxes print correctly (not washed out or missing).
```

---

## Template Status After Session 2

All five templates are built and verified. Here is the complete template inventory:

| Template | File Name | Canvas | Sprint Use |
|---|---|---|---|
| 1 — Bundle Card Cover | Phase3-[Bundle]-Cover-v1 (×5) | 2400×2400px | Etsy slot 1; insert hero image during sprint |
| 2 — Info Block | Phase3-InfoBlock-MASTER | 8.5×11in | Interior PDF pages; duplicate per species |
| 3 — Testimonial Block | Phase3-Testimonial-MASTER | 1000×1500px | Pinterest / Instagram social; add quotes |
| 4 — Ingredient Detail | Phase3-IngredientDetail-MASTER | 1080×1080px | Instagram species spotlight; change species |
| 5 — Dosage Reference | Phase3-DosageCard-MASTER | 8.5×11in | PDF quick-reference pages; fill per species |

---

## Sprint Workflow: How to Use These Templates (June 22+)

Each sprint task involving design follows this three-step sequence:

**Step 1 — Open the relevant master template**  
Never edit the master directly. Always duplicate first.

```
Canva project view > right-click master > Make a copy
Rename: "[TemplateName]-[BundleName]-[SpeciesOrPurpose]-v1"
Example: "Phase3-IngredientDetail-WomensHealth-BlackCohosh-v1"
```

**Step 2 — Replace the placeholder content**  
Change only the variable elements: text content, hero images. Do not change layout, font sizes, or colors — those are locked from the template.

```
Text elements to replace per use:
  - Species common name
  - Latin name (keep italic — do not change formatting)
  - Body text / facts / dosage details
  - Bundle name label (header)
  
Image elements to replace:
  - Delete the gray placeholder rectangle and label
  - Upload the real species photograph
  - Drag photo to exactly fill the image zone
  - Apply drop shadow if the template includes one (settings are already in the template)
```

**Step 3 — Export and log**

```
File > Download > appropriate format (see PHASE_3_DESIGN_SYSTEM.md Part 4 for format table)
Save to: projects/seedwarden/assets/phase-3-medicinal-herbs/[bundle-name]/
Log in WORKLOG.md: file name, bundle, date produced
```

---

## Canva Folder Structure (Create June 21)

Create this folder structure in Canva before building templates, so all files land in the right place:

```
Seedwarden (existing top-level project)
└── Phase 3 — Medicinal Herbs
    ├── Masters (do not edit — source files only)
    │   ├── Phase3-InfoBlock-MASTER
    │   ├── Phase3-Testimonial-MASTER
    │   ├── Phase3-IngredientDetail-MASTER
    │   └── Phase3-DosageCard-MASTER
    ├── Bundle Covers
    │   ├── Phase3-WomensHealth-Cover-v1
    │   ├── Phase3-Respiratory-Cover-v1
    │   ├── Phase3-Immunity-Cover-v1
    │   ├── Phase3-Sleep-Cover-v1
    │   └── Phase3-Digestive-Cover-v1
    ├── Interior Pages (working files during sprint)
    ├── Social Media (working files during sprint)
    └── Exports (exported JPEGs and PDFs — not Canva design files)
```

The "Masters" folder is read-only by convention. Any time you need to create a new asset from a master, make a copy first, move it to the appropriate subfolder, then edit. This discipline prevents accidental overwriting of the master templates.

---

## Troubleshooting: Common Issues During Sprint

**Issue**: Color in exported PDF does not match the screen preview.  
**Fix**: Canva occasionally shifts hex values on export, especially for mid-range colors (Sage Green, Muted Lavender). Re-enter the hex code in the element's color picker (click the element > Colors > "+" icon > type hex manually). Export again. If deviation persists, log the actual rendered hex in WORKLOG.md and adjust the Brand Kit entry to match the rendered value, not the target value.

**Issue**: Bundle title text overflows the header block on narrow screens.  
**Fix**: Reduce Playfair Display bundle title from 48pt to 42pt. The 6pt reduction is within spec range. Do not reduce below 38pt — title becomes illegible at Etsy thumbnail size.

**Issue**: The Apothecary Gold accent bar disappears in the exported PDF.  
**Fix**: Canva sometimes drops thin line elements in PDF export. Replace the line element with a very thin rectangle (1px height = approximately 0.014in). Rectangles export more reliably than line elements. Refill with Apothecary Gold #D4AF37.

**Issue**: Testimonial quote text runs longer than the quote zone.  
**Fix**: Testimonials should be no more than three sentences (approximately 50–70 words). If a testimonial is longer, edit it to the key sentence. The quote zone in Template 3 holds approximately 60 words at 36px Cormorant Garamond. Do not reduce font size below 32px to fit longer quotes — reduce the quote instead.

**Issue**: Logo is not the right color on the dark footer.  
**Fix**: Use the Clinical Cream version of the logo (white/light version on transparent PNG background). If only a dark logo version is available, apply Canva's color filter: select logo > Edit image > Duotone > set highlight color to Clinical Cream #F9F5F0, shadow color to transparent.

---

*Prepared: May 27, 2026. Build all five templates by June 21. Sprint-ready for June 22 content insertion.*
