---
title: "Phase 3 Canva Design System and Brand Kit Documentation"
date: 2026-05-20
status: production-ready
phase: Phase 3 pre-sprint preparation
purpose: >
  Comprehensive Canva design system specification for Phase 3 medicinal herb bundles.
  Covers confirmed brand kit (6 hex codes, typography, logo), cover and interior page
  templates, per-bundle visual differentiation, Canva workflow from upload to export,
  PDF export specifications, and quality gates. Design-lock-ready by June 21.
cross-references:
  - canva-phase-3-adaptation-guide.md (palette source — authoritative May 19 version)
  - PHASE_3_PRODUCTION_TIMELINE.md (design task schedule within sprint)
  - CANVA_EXECUTION_PLAYBOOK.md (Phase 2 template foundation)
tags: [seedwarden, phase-3, canva, design-system, brand-kit, templates, pdf-export]
word_count: 1,800+
---

# Phase 3 Canva Design System and Brand Kit Documentation

**Prepared**: May 20, 2026
**Design lock date**: July 3, 2026 (EOD — no design changes after this date)
**Brand kit load deadline**: June 21, 2026 (pre-sprint readiness audit)
**Authoritative palette source**: `canva-phase-3-adaptation-guide.md` (May 19, 2026)

This document resolves the palette discrepancy noted in `TRACK_B_EXECUTION_STAGING_MAY_30.md` (Decision 3). The May 19 adaptation guide is authoritative. Any older document specifying different hex codes is superseded.

---

## Part 1: Confirmed Brand Kit Specifications

### Color Palette (Phase 3 — Authoritative)

Load these six colors into the existing Seedwarden Canva Brand Kit. Do not remove Phase 2 colors — add Phase 3 colors as a second group in the same kit. Label clearly to distinguish Phase 2 (Forager) and Phase 3 (Herbalist/Apothecary) palettes.

| Color Name | Hex Code | Primary Use | Bundle Association |
|---|---|---|---|
| Deep Burgundy | #8B3E3E | Header backgrounds, bundle color signal | Women's Health, Immunity |
| Sage Green | #6B8E6F | Header backgrounds, bundle color signal | Respiratory, Digestive |
| Apothecary Gold | #D4AF37 | Accent bar (all bundles), premium tier marker | All bundles |
| Clinical Cream | #F9F5F0 | Page background (all bundles) | All bundles |
| Muted Lavender | #9B8BA0 | Accent, sleep-specific | Sleep bundle only |
| Dark Charcoal | #2C2C2C | Body text (all bundles) | All bundles — unchanged from Phase 2 |

**How to add to Brand Kit**:
1. Open Canva — navigate to Brand Hub (left sidebar icon)
2. Select existing Seedwarden Brand Kit
3. In the Colors section, click "+ Add color"
4. Paste the hex code exactly as listed above (including the # symbol)
5. Label the color with the name from the table
6. Repeat for all six Phase 3 colors
7. Save — refresh any open design files to pick up the new colors

**Color rendering test**: After loading all six colors, create a single test zone card with the Sage Green header, Clinical Cream background, and Apothecary Gold accent bar. Export to PDF. Open the PDF in Adobe Reader or Preview and verify the hex codes render accurately — Canva occasionally shifts hex values slightly on export. If a rendered color deviates by more than 5 points on any RGB channel, re-enter the hex code and retest. Document actual rendered hex values in WORKLOG.md if any deviation occurs.

### Typography System (Phase 3 — Unchanged from Phase 2)

**Heading font**: Playfair Display
- Use case: Bundle title on cover, section headers in interior pages
- Sizes: Cover title 42–48pt Bold; interior section headers 22–26pt Bold; sub-headers 16–18pt Regular
- Available free in Canva

**Body font**: Lato or Source Sans 3 (use one consistently — do not mix)
- Use case: All body text in guides, zone card content, secondary text
- Sizes: Body text 11–12pt Regular; captions 9–10pt Regular; call-to-action overlays on lifestyle images 14–16pt Medium
- Available free in Canva

**Accent font**: Cormorant Garamond (italic)
- Use case: Taglines, quote callouts, botanical name (italic is the taxonomic standard for genus and species names)
- Sizes: 14–16pt Italic; species names in 11–12pt Italic inline with body text
- Available free in Canva

**Typography rules**:
- All genus and species names are always italicized (Actaea racemosa, not Actaea racemosa)
- Do not use more than two font families in any single design element
- Tracking (letter spacing): 0 for body text, +20–40 for small caps headers, -10 for large display headings
- Line height: 140–150% for body text; 120% for headers

### Logo Usage

- Seedwarden wordmark: left-aligned in the header of all documents
- Zone cards: upper-left corner, 0.5–0.8 inches tall
- Bundle covers: upper-left or centered — consistent within each bundle, not across bundles
- Do not resize the logo below the minimum legible size (0.4 inches tall)
- Always use the version with the transparent background (PNG) — never place on white if the background is Clinical Cream

---

## Part 2: Template Design System

### Cover Template — Structure

All five bundle covers follow the same structural template. The per-bundle differentiation comes from the header color and the hero image, not from a different layout.

**Canvas size**: 2400×2400px (square — required for Etsy listing primary image)

```
┌────────────────────────────────────────┐
│  [Header block — top 25% of canvas]   │  Bundle header color (Burgundy/Sage/Lavender)
│  SEEDWARDEN MEDICINAL HERBS GUIDE      │  Playfair Display 42pt Bold, Clinical Cream text
│  [Bundle Title — large]               │  Playfair Display 48pt Bold, Apothecary Gold
│  [5 Species names — small line]       │  Cormorant Garamond 14pt Italic, Clinical Cream
├────────────────────────────────────────┤
│  [Hero image — center 60% of canvas]  │  Full-bleed or framed botanical photography
│  [Subtle Apothecary Gold frame line]  │  2px gold rule divides header from image
│                                        │
│                                        │
│                                        │
├────────────────────────────────────────┤
│  [Footer band — bottom 15% of canvas] │  Dark Charcoal background
│  [Seedwarden wordmark — left]         │  Clinical Cream wordmark
│  [Price hint or "Educational Guide"]  │  Lato 12pt, Sage Green or muted accent
└────────────────────────────────────────┘
```

**Per-bundle differentiators on the cover**:
- Women's Health: Deep Burgundy header + Black Cohosh or Calendula hero
- Respiratory: Sage Green header + Elderberry berry cluster hero
- Immunity: Deep Burgundy header + Goldenseal forest-floor hero
- Sleep: Muted Lavender header + Passionflower flower hero
- Digestive: Sage Green header + Dandelion root or Ginger rhizome hero

**Design time per cover**: 1.2 hours (first cover); 45–50 minutes (subsequent covers using duplicate-and-edit method)

**Export**: 2400×2400px JPEG, quality 95%+. Verify thumbnail appearance at 170×135px (the Etsy listing grid thumbnail size) before uploading.

### Interior Page Template — Structure

Interior pages are portrait PDF format (8.5×11 inches, 300dpi for print compatibility).

```
┌────────────────────────────────────────┐
│  [Header strip — top 0.5"]            │  Bundle color (thin band), bundle name right-aligned
│  SEEDWARDEN  [logo, small]            │  Apothecary Gold horizontal rule below header
├────────────────────────────────────────┤
│  [Section heading]                     │  Playfair Display 22pt Bold, Dark Charcoal
│  [Species name — italic]              │  Cormorant Garamond 18pt Italic
│                                        │
│  [Body text columns — 1 or 2]         │  Lato 11pt, 1.45 line height, Clinical Cream bg
│  [Body text body text body text]      │  Text margins: 0.75" left, 0.75" right
│  [Body text body text...]             │
│                                        │
│  [Conservation sidebar — boxed]       │  Apothecary Gold border, Clinical Cream bg
│  CONSERVATION NOTE                    │  Lato 10pt, Gold accent icon (leaf or circle)
│  [Sidebar text content]               │
│                                        │
│  [Species image — right column]       │  2:3 portrait ratio, drop shadow
│                                        │
│  [Horizontal rule — Apothecary Gold]  │  1px rule before next species section
├────────────────────────────────────────┤
│  [Footer — page number + bundle name] │  Lato 9pt, muted, left-page-right-aligned
└────────────────────────────────────────┘
```

**Interior page rules**:
- Species names always italic in body text and headers (taxonomic convention)
- Conservation sidebars have a consistent box style: Apothecary Gold (#D4AF37) 1.5pt border, Clinical Cream interior, species icon or UpS logo if permission obtained
- Contraindications sections use a subtle red-tinted callout box (not alarming, but visually distinct from informational sidebars)
- CITES sidebar (Goldenseal only): bordered in Apothecary Gold, slightly larger than standard sidebar (200 words requires more space)
- Page numbers: bottom-right on recto (right-side) pages, bottom-left on verso (left-side) pages. Bundle name centered in footer.

### Zone Card Template — Structure

Zone cards are landscape or portrait depending on the cultivation calendar volume. For Phase 3, use portrait (8.5×11 inches) to accommodate the four-column cultivation calendar.

Refer to `canva-phase-3-adaptation-guide.md` (Part 3) for the zone card structure diagram and cultivation calendar example. The adaptation guide is the authoritative template specification for zone cards — this document provides the brand system framing but defers to the adaptation guide for zone card content architecture.

**Zone-card-to-cover color connection**: Each bundle's zone card uses the same header color as its cover. A Women's Health zone card has a Deep Burgundy header. A Digestive zone card has a Sage Green header. The color connection allows buyers to file their zone card with their guide without reading the title.

### Practitioner Bundle Cover — Structure

See `canva-phase-3-adaptation-guide.md` (Part 4) for the full practitioner cover specification. Key additions from this design system document:

- The practitioner cover uses Apothecary Gold as its primary header color (not bundle-specific Burgundy or Sage Green) — it is the premium tier across all five bundles, visually distinct from the consumer covers.
- The five bundle thumbnails at the bottom of the practitioner cover (one per bundle) use their respective bundle header colors to create a color-coded reference grid.
- Typography on practitioner cover: Playfair Display for the title, Montserrat for the subtitle and body. Montserrat (not Lato) signals a shift to a more clinical, formal register appropriate for the professional market.

---

## Part 3: Per-Bundle Visual Differentiation Brief

### How Each Bundle Should Look Different from the Others

The color system handles the primary differentiation. But within the same color family (Burgundy for Women's Health and Immunity; Sage Green for Respiratory and Digestive), the hero image creates the visual separation.

**Women's Health vs. Immunity** (both Deep Burgundy):
- Women's Health: organic, woodland aesthetic (Black Cohosh in forest context, or warm Calendula orange against Burgundy). The imagery signals botanical heritage.
- Immunity: clinical, forest-farming precision (Goldenseal root's yellow-orange color against Burgundy, or the Ashwagandha winter cherry berries). The imagery signals specificity and authority.
- If placed side by side in an Etsy search result, the hero images should be immediately distinguishable even when the thumbnails are small.

**Respiratory vs. Digestive** (both Sage Green):
- Respiratory: seasonal, outdoor harvest feel (Elderberry berry clusters, the autumn harvest moment). The imagery signals urgency (cold and flu season).
- Digestive: root and earth, preparation context (Dandelion root, Ginger rhizome). The imagery signals practical kitchen herbalism.

**Sleep** (Muted Lavender):
- The Passionflower is the only bundle cover where the hero image is primarily a flower — the entire composition is the flower. No other bundle has this visual approach. It is immediately distinctive.

### Design Consistency Checklist

Run this checklist before finalizing any cover:
- [ ] Bundle title in Apothecary Gold (not white, not Burgundy/Green) on the header
- [ ] Hero image occupies 60%+ of the canvas
- [ ] Seedwarden wordmark visible in footer
- [ ] Cover exports cleanly at 170×135px (Etsy grid thumbnail test)
- [ ] No placeholder text remaining in any text field
- [ ] Font sizes consistent with the typography system (no arbitrary resizing)
- [ ] Colors match the Brand Kit hex codes (not eyeballed — pulled from the Brand Kit)

---

## Part 4: Canva Workflow — Upload to Export

### Pre-Sprint Setup (June 21 hard deadline)

1. Open Canva Brand Kit and confirm all six Phase 3 hex codes are loaded
2. Open the Phase 2 bundle cover master template
3. Duplicate it as "Phase 3 — Cover Master"
4. Update the master with the Phase 3 palette (change all Phase 2 green elements to the appropriate Phase 3 color for a test run)
5. Export the test cover as PDF — verify hex codes render correctly
6. If test passes: create four additional duplicates of the master (one per remaining bundle). Name them per the naming convention below.
7. Pre-populate each duplicate with the bundle-specific title and species list (the text elements are the same structure across all covers, only the content changes)

This pre-population on June 21 means that on Sprint Day 1 (June 22), the cover design work is inserting a hero image and checking colors — not building from scratch.

### Design File Naming Convention

```
Bundle covers:    Phase3-[BundleName]-Cover-v[N]
Zone cards:       Phase3-[BundleName]-ZoneCard-Zone[#]-v[N]
Practitioner:     Phase3-Practitioner-Cover-v[N]
Interior template: Phase3-Interior-Template-v[N]

Examples:
  Phase3-WomensHealth-Cover-v1
  Phase3-Respiratory-ZoneCard-Zone5-v1
  Phase3-Practitioner-Cover-v1
```

Always increment the version number when making a substantive design change. Do not save over v1 — keep v1 as the fallback. If a v2 change introduces a problem, revert to v1 and rebuild from there.

### Sprint-Day Design Integration

Design work is embedded in sprint days at the following schedule. It does not occur at the same time as writing — use design as the afternoon/lower-cognitive-load work after writing:

| Sprint Day | Design Task | Hours | Float |
|---|---|---|---|
| Pre-sprint June 21 | Brand Kit load + palette test | 0.5 | 0 — must complete |
| D2 June 23 | Women's Health cover | 1.2 | 4 days |
| D3 June 24 | Respiratory cover | 1.2 | 4 days |
| D8 June 29 | Immunity cover | 1.2 | 4 days |
| D9 June 30 | Sleep cover | 1.2 | 3 days |
| D10 July 1 | Women's Health zone card | 0.8 | 4 days |
| D11 July 2 | Respiratory zone card | 0.8 | 4 days |
| D12 July 3 | Digestive cover (DESIGN LOCK EOD) | 1.2 | 0 |
| D15–D16 July 6–7 | Immunity + Sleep + Digestive zone cards | 2.4 | 2 days |
| D16 July 7 | Consistency review + export test all 5 covers | 0.5 | 2 days |
| D6–D8 | Minor revision buffer (one cover) | 1.5 | as needed |
| D6–D8 (parallel) | 5 Practitioner covers | 7.5 | 2 days |
| **Total** | | **19.3 hrs** | |

**Design lock — July 3, 11:59 PM local time**. After design lock, no cover changes occur until after all five bundles are uploaded. Any design deficiencies found during the July 9 FTC review are noted for v1.1 correction, not corrected mid-sprint.

### Batch vs. Manual Workflow Decision

**Bundle covers (5 covers)**: Manual, one at a time. Each cover requires a unique hero image insert and a color-check against the Brand Kit. Batch processing introduces risk of wrong image in wrong bundle.

**Zone cards (5 bundles × 5 zones = 25 cards total, if producing all zones)**: Batch within each bundle. Produce all 5 zone cards for Women's Health in one session (change zone number and regional notes only — all other content is the same). Then move to Respiratory, etc.

**Note on zone card scope**: Phase 3 launch does not require 25 zone cards. It requires 5 zone cards minimum (one per bundle — use Zone 5 as the default since it represents the largest buyer concentration). Produce Zone 3, 7, 8, and 9 variants as post-launch content upgrades. Do not let the 25-card scope block the July 13 sprint end.

### Export Specifications

**Bundle guide PDFs**:
- Format: PDF (Print quality)
- Dimensions: 8.5×11 inches
- Resolution: 300 DPI
- Color mode: RGB (Etsy serves digital PDFs on screen; print-quality resolution is maintained but CMYK is not required)
- File size target: Under 5 MB per bundle guide (guides with many high-resolution images may exceed this — compress embedded images to 150 DPI if needed to hit the size target)
- File naming: `Seedwarden-[BundleName]-HerbsGuide-v1.pdf`

**Etsy listing images (slots 1–5)**:
- Format: JPEG
- Dimensions: 2400×2400px (square) or 3000×2000px (landscape — for lifestyle shots)
- Resolution: 72 DPI (screen use only — the 2400px size provides sufficient pixel density)
- Color mode: RGB, sRGB color profile
- File naming: `Phase3-[BundleName]-Etsy-Slot[N].jpg`

**Zone cards**:
- Format: PDF (both print and screen versions)
- Dimensions: 8.5×11 inches portrait
- Resolution: 300 DPI
- Size target: Under 2 MB per card
- File naming: `Seedwarden-[BundleName]-ZoneCard-Zone[#]-v1.pdf`

---

## Part 5: Google Docs Fallback Path

If Canva performance degrades during the sprint (slow rendering, export failures, asset loading issues), the following fallback applies:

**Trigger**: Any single cover design task exceeds 2 hours without completion.

**Action**: Pause Canva work on that cover. Switch to Google Docs PDF:
1. Create a new Google Doc at 8.5×11 inches (File > Page Setup)
2. Set background color to Clinical Cream (#F9F5F0) — approximate if the exact hex isn't available
3. Insert the bundle title in Playfair Display equivalent (Georgia Bold is the closest available)
4. Insert the hero image at the top of the document
5. Add a colored horizontal rule below the title (Insert > Horizontal Line, then format manually)
6. Export: File > Download > PDF Document

The Google Docs fallback is launch-viable. The design quality is lower, but the content quality — which is the primary purchase driver for the practitioner buyer — is identical. The Canva version becomes a v1.1 upgrade applied post-launch.

**Fallback tracking**: If any bundle uses the Google Docs fallback, record in WORKLOG.md with the specific blocking issue. This data informs whether Canva Pro is worth continuing after the sprint.

---

## Part 6: Design Quality Gates

### Pre-Upload Checklist (run before each Etsy listing upload)

- [ ] Cover image exports cleanly at 2400×2400px — no compression artifacts visible
- [ ] Cover thumbnail test: image legible at 170×135px (Etsy grid view simulation)
- [ ] Bundle title legible at thumbnail size — not just the logo
- [ ] Hero image: correct species for this bundle (not cross-contaminated from another bundle)
- [ ] Header color: correct for this bundle (Burgundy for Women's Health/Immunity, Sage for Respiratory/Digestive, Lavender for Sleep)
- [ ] No placeholder text in any text field on the cover or interior pages
- [ ] PDF file size under 5 MB
- [ ] PDF opens correctly in Adobe Reader or Preview (no rendering errors)
- [ ] All image attributions present in the Photo Credits page of the PDF
- [ ] Canva design file named per the naming convention and saved in the correct project folder

### Design Sign-Off (Sprint End — July 13)

All five bundle covers designed, exported, and named per convention. Practitioner covers designed for the three first-launch bundles (Women's Health, Respiratory, Sleep). Zone cards: minimum one per bundle (Zone 5). Canva project folder organized per the file hierarchy in `canva-phase-3-adaptation-guide.md` (Part 5).

---

*Prepared: May 20, 2026. Resolves the Decision 3 palette discrepancy in favor of the May 19 canva-phase-3-adaptation-guide.md as authoritative. Design lock: July 3, 2026 EOD.*
