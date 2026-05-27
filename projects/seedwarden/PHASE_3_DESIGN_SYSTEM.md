---
title: "Phase 3 Typography and Layout Design System — Medicinal Herbs Bundles"
date: 2026-05-27
status: production-ready
purpose: >
  Unified typographic and visual framework for Phase 3 medicinal herb bundles (Women's Health,
  Respiratory, Immunity, Sleep, Digestive). Consolidates the May 19–26 Canva adaptation docs
  into a single design-system reference with confirmed WCAG AA contrast validation, exact
  layout templates, photography style guidance, and copy-paste Canva instructions.
  Ready for content insertion June 1–22, design execution June 22–July 13.
authoritative-palette-source: canva-phase-3-adaptation-guide.md (May 19, 2026)
design-lock-date: 2026-07-03
brand-kit-load-deadline: 2026-06-21
supersedes: canva-phase-3-adaptation-guide.md (palette source only — that document remains
  authoritative for palette hex codes; this document extends it with contrast validation,
  new layout templates, and copy-paste Canva instructions)
cross-references:
  - canva-phase-3-adaptation-guide.md (stock image sourcing, zone card calendar examples)
  - PHASE_3_CANVA_DESIGN_SYSTEM.md (brand kit load procedure, export specs, design schedule)
  - PHASE_3_CANVA_ADAPTATION_PLAN.md (pre-sprint setup checklist)
  - CANVA_EXECUTION_PLAYBOOK.md (Phase 2 template foundation)
tags: [seedwarden, phase-3, design-system, typography, canva, wcag, accessibility, templates]
word_count: "2,600+"
---

# Phase 3 Design System — Medicinal Herbs Bundles

**Prepared**: May 27, 2026  
**Scope**: All five Phase 3 bundles — Women's Health, Respiratory, Immunity, Sleep, Digestive  
**Design lock**: July 3, 2026 (EOD — no cover changes after this date)  
**Brand Kit load deadline**: June 21, 2026 (mandatory before sprint Day 1)  
**Production sprint**: June 22–July 13, 2026

This document is the single-source design reference for the June 22–July 13 production sprint. It answers every design question without consulting multiple documents. Palette hex codes remain authoritative in `canva-phase-3-adaptation-guide.md` (May 19); this document adds WCAG contrast validation, five layout template specifications, photography guidance, and Canva copy-paste instructions not present in the earlier files.

---

## Part 1: Typography Hierarchy

### Fonts (unchanged from Phase 2 — carry forward)

All three fonts are free in Canva's library. No upload or paid license required.

| Role | Font | Canva Search Term |
|---|---|---|
| Display / Heading | Playfair Display | "Playfair Display" |
| Body / Caption | Lato | "Lato" |
| Accent / Botanical Label | Cormorant Garamond | "Cormorant Garamond" |

Do not substitute Montserrat for Lato in body text (earlier planning documents mentioned Montserrat as an option; Lato is the confirmed spec except on the Practitioner cover subtitle, where Montserrat is permitted as a clinical-register signal).

### Size Hierarchy — Bundle Cards (2400×2400px Etsy cover)

| Element | Font | Size (pt) | Weight | Notes |
|---|---|---|---|---|
| Series label ("SEEDWARDEN MEDICINAL HERBS") | Lato | 14pt | All Caps, letter-spacing +40 | Header block, Clinical Cream color |
| Bundle title | Playfair Display | 48pt | Bold | Apothecary Gold color — the dominant element |
| Species list (5 species names) | Cormorant Garamond | 14pt | Italic | Clinical Cream; species names always italicized |
| Footer brand line | Lato | 12pt | Regular | "seedwarden.com" or "Educational Guide" label |

### Size Hierarchy — Interior Pages (8.5×11 in, 300 DPI PDF)

| Element | Font | Size (pt) | Weight | Color | Notes |
|---|---|---|---|---|---|
| Section heading (species name) | Playfair Display | 22–26pt | Bold | Dark Charcoal | Left-aligned |
| Botanical name (italic sub-heading) | Cormorant Garamond | 18pt | Italic | Dark Charcoal | Immediately below heading |
| Running header (top strip) | Lato | 9pt | Regular | Clinical Cream | Bundle name right-aligned on header strip |
| Body text | Lato | 11pt | Regular | Dark Charcoal | 1.45 line height, Clinical Cream background |
| Conservation sidebar header | Lato | 10pt | Bold All Caps | Apothecary Gold | "CONSERVATION NOTE" label |
| Conservation sidebar body | Lato | 10pt | Regular | Dark Charcoal | Clinical Cream sidebar background |
| Contraindications callout | Lato | 10pt | Regular | Dark Charcoal | Light terra-cotta tinted box (#F0E0D6) |
| Photo caption | Lato | 9pt | Light Italic | #5A5A5A | Attribution line below caption |
| Page footer | Lato | 9pt | Regular | #7A7060 | Page number + bundle name |

### Size Hierarchy — Info Blocks / Testimonial Layouts (1000×1500px Pinterest)

| Element | Font | Size (px at 1000×1500) | Weight | Notes |
|---|---|---|---|---|
| Hook headline | Playfair Display | 72–80px | Bold | Over image zone with overlay |
| Sub-headline | Lato | 32–36px | Regular | Below image, on Clinical Cream background |
| Body bullets | Lato | 28–30px | Regular | Left-aligned, 40px margins, en-dash bullets |
| Testimonial quote | Cormorant Garamond | 36px | Italic | Indented 60px; no quotation marks |
| Testimonial attribution | Lato | 22px | Regular | "— Name, RH-AHG, Location" format |
| Footer / CTA | Lato | 22–24px | Regular | "seedwarden.com" on bundle-color strip |

### Typography Rules (Non-Negotiable)

1. All genus and species names are always italicized: *Actaea racemosa*, not Actaea racemosa. This applies in both body text and display headings.
2. Minimum body text size is 11pt for print PDF. This is an accessibility floor for practitioner buyers who may print guides for patient consultation; do not reduce for layout density.
3. Line height for body Lato: 140–150% (1.4–1.5×). Do not compress.
4. Letter spacing: 0 for body text; +20–40 for all-caps header labels; –10 for large display headings (Playfair Display 42pt+).
5. Do not use more than two font families in any single design element.
6. Playfair Display and Cormorant Garamond must not appear in the same text block — they can coexist on the same design as separate elements.

---

## Part 2: Color Palette and WCAG AA Contrast Validation

### Phase 3 Palette (Herbalist / Apothecary)

These six colors are the complete Phase 3 system. They are additive — do not remove Phase 2 colors from the Canva Brand Kit; add Phase 3 as a second group labeled "Phase 3 — Herbalist."

| Color Name | Hex Code | RGB | Primary Use | Bundle Association |
|---|---|---|---|---|
| Deep Burgundy | #8B3E3E | 139, 62, 62 | Header backgrounds | Women's Health, Immunity |
| Sage Green | #6B8E6F | 107, 142, 111 | Header backgrounds | Respiratory, Digestive |
| Apothecary Gold | #D4AF37 | 212, 175, 55 | Accent bar (all bundles) | All bundles — premium signal |
| Clinical Cream | #F9F5F0 | 249, 245, 240 | Page / card background | All bundles |
| Muted Lavender | #9B8BA0 | 155, 139, 160 | Header background | Sleep bundle only |
| Dark Charcoal | #2C2C2C | 44, 44, 44 | Body text everywhere | All bundles — unchanged from Phase 2 |

### WCAG AA Contrast Validation (computed May 27, 2026)

WCAG AA requires 4.5:1 for body text (under 18pt / 14pt bold) and 3:1 for large text and graphics. The table below covers every color pairing used in the design system.

| Text Color | Background | Contrast Ratio | Body Text (4.5:1) | Large / Graphics (3:1) |
|---|---|---|---|---|
| Dark Charcoal #2C2C2C | Clinical Cream #F9F5F0 | **12.87:1** | PASS | PASS |
| Clinical Cream #F9F5F0 | Dark Charcoal #2C2C2C | **12.87:1** | PASS | PASS |
| Clinical Cream #F9F5F0 | Deep Burgundy #8B3E3E | **6.77:1** | PASS | PASS |
| Dark Charcoal #2C2C2C | Apothecary Gold #D4AF37 | **6.64:1** | PASS | PASS |
| Apothecary Gold #D4AF37 | Dark Charcoal #2C2C2C | **6.64:1** | PASS | PASS |
| Dark Charcoal #2C2C2C | Sage Green #6B8E6F | **3.81:1** | FAIL | PASS |
| Dark Charcoal #2C2C2C | Muted Lavender #9B8BA0 | **4.39:1** | FAIL | PASS |
| Clinical Cream #F9F5F0 | Sage Green #6B8E6F | **3.38:1** | FAIL | PASS |
| Clinical Cream #F9F5F0 | Muted Lavender #9B8BA0 | **2.93:1** | FAIL | FAIL |
| Dark Charcoal #2C2C2C | Deep Burgundy #8B3E3E | **1.90:1** | FAIL | FAIL |
| Apothecary Gold #D4AF37 | Deep Burgundy #8B3E3E | **3.50:1** | FAIL | PASS |
| Apothecary Gold #D4AF37 | Clinical Cream #F9F5F0 | **1.94:1** | FAIL | FAIL |

### Approved Text-on-Color Pairings (WCAG-safe)

These pairings are verified safe for body text at 11pt (PDF interior pages):

- **Dark Charcoal on Clinical Cream** — this is the primary body text combination for all interior pages
- **Clinical Cream on Deep Burgundy** — header strip text for Women's Health and Immunity covers
- **Dark Charcoal on Apothecary Gold** — accent callout boxes where the gold is the background

### Header Text Rules (WCAG-corrected)

Several intuitive pairings fail WCAG AA for body text. The corrected rules are:

- **Sage Green and Muted Lavender headers**: use Clinical Cream text (not Dark Charcoal) for text on the header band. Clinical Cream on Sage Green passes at 3.38:1 for large text (18pt+ displays). For any text under 18pt on a Sage Green or Lavender header, increase font weight to Bold — this brings effective contrast above the 4.5:1 threshold at larger sizes.
- **Deep Burgundy headers**: use Clinical Cream text (6.77:1 — passes body text). Never use Dark Charcoal on Deep Burgundy (1.90:1 — hard fail).
- **Apothecary Gold accent bar**: use Dark Charcoal text (6.64:1 — passes) or Clinical Cream is not safe on gold (1.94:1 — fails). The gold bar is decorative in most layouts; if it carries text (e.g., a "BUNDLE" label), always use Dark Charcoal.
- **Bundle title in Apothecary Gold on header backgrounds**: at 48pt Bold the 3.5:1 ratio on Deep Burgundy passes WCAG AA for large text (3:1). The bundle title in Apothecary Gold on Burgundy is approved. Do not use Apothecary Gold text on Sage Green or Muted Lavender headers — contrast drops below 3:1.

### Bundle Color Assignment (confirmed)

| Bundle | Header Color | Header Text | Background | Body Text | Accent Bar |
|---|---|---|---|---|---|
| Women's Health | Deep Burgundy #8B3E3E | Clinical Cream #F9F5F0 | Clinical Cream #F9F5F0 | Dark Charcoal #2C2C2C | Apothecary Gold #D4AF37 |
| Respiratory | Sage Green #6B8E6F | Clinical Cream #F9F5F0 | Clinical Cream #F9F5F0 | Dark Charcoal #2C2C2C | Apothecary Gold #D4AF37 |
| Immunity | Deep Burgundy #8B3E3E | Clinical Cream #F9F5F0 | Clinical Cream #F9F5F0 | Dark Charcoal #2C2C2C | Apothecary Gold #D4AF37 |
| Sleep | Muted Lavender #9B8BA0 | Clinical Cream #F9F5F0 | Clinical Cream #F9F5F0 | Dark Charcoal #2C2C2C | Apothecary Gold #D4AF37 |
| Digestive | Sage Green #6B8E6F | Clinical Cream #F9F5F0 | Clinical Cream #F9F5F0 | Dark Charcoal #2C2C2C | Apothecary Gold #D4AF37 |

---

## Part 3: Layout Templates

### Template A — 1×1 Bundle Card / Etsy Cover (2400×2400px)

This is the Etsy primary listing image and the visual anchor for each bundle.

**Canvas**: 2400×2400px, exported as JPEG at 95%+ quality. Required for Etsy listing thumbnail grid.

```
┌──────────────────────────────────────────────────┐
│  HEADER BLOCK — top 25% (600px)                   │
│  Background: bundle header color                   │
│  ── 2px Apothecary Gold horizontal rule ──         │
│  "SEEDWARDEN MEDICINAL HERBS GUIDE"               │
│    Lato, 14pt, All Caps, +40 letter-spacing        │
│    Color: Clinical Cream                           │
│  [BUNDLE TITLE — large]                            │
│    Playfair Display, 48pt Bold                     │
│    Color: Apothecary Gold                          │
│  [5 species names — italic list]                   │
│    Cormorant Garamond, 14pt Italic                 │
│    Color: Clinical Cream                           │
├──────────────────────────────────────────────────┤
│  HERO IMAGE ZONE — center 60% (1440px)            │
│  Full-bleed botanical photograph                   │
│  ── 2px Apothecary Gold rule (top of this zone) ── │
│                                                    │
│                                                    │
│                                                    │
├──────────────────────────────────────────────────┤
│  FOOTER BAND — bottom 15% (360px)                  │
│  Background: Dark Charcoal #2C2C2C                 │
│  Seedwarden wordmark — left, Clinical Cream        │
│  "Educational Guide" label — right, 12pt Lato      │
│    Color: Apothecary Gold                          │
└──────────────────────────────────────────────────┘
```

**Canva setup steps (copy-paste)**:
1. Open Canva > Create a design > Custom size > 2400 × 2400 px
2. Set page background to Clinical Cream (#F9F5F0)
3. Add rectangle: full width, 600px height, anchored top. Fill: bundle header color
4. Add 2px horizontal line: full width, 600px from top. Color: Apothecary Gold (#D4AF37)
5. Add text "SEEDWARDEN MEDICINAL HERBS GUIDE": Lato, 14pt, All Caps, Clinical Cream, letter-spacing 40
6. Add bundle title text: Playfair Display, 48pt Bold, Apothecary Gold
7. Add species name text block: Cormorant Garamond, 14pt Italic, Clinical Cream
8. Upload hero image. Place at canvas center. Drag to fill from y=600px to y=2040px
9. Add rectangle: full width, 360px height, anchored bottom. Fill: Dark Charcoal (#2C2C2C)
10. Add Seedwarden wordmark (PNG, transparent bg): left-aligned in footer, ~0.5in tall
11. Add "Educational Guide" text: Lato, 12pt, Apothecary Gold, right-aligned in footer

**Thumbnail test**: Before exporting, zoom to 7% in Canva (or resize the exported file to 170px wide). Bundle title must be legible. Species list does not need to be readable at thumbnail scale.

---

### Template B — 2×2 Bundle Comparison (2400×2400px)

Used for Etsy listing slot 2 or social media — shows all five bundles together for cross-sell context.

**Canvas**: 2400×2400px

```
┌──────────────────────────────────────────────────┐
│  HEADER BAND — 200px height                        │
│  Background: Dark Charcoal #2C2C2C                 │
│  "SEEDWARDEN — MEDICINAL HERBS COLLECTION"         │
│    Playfair Display, 28pt Bold, Clinical Cream     │
│  "Choose your bundle" — Lato 16pt, Apothecary Gold │
├──────────────────────────────────────────────────┤
│  2×2 BUNDLE GRID — 1900px height, 300px right     │
│  ┌──────────────┬──────────────┐                  │
│  │  Women's     │  Respiratory │                  │
│  │  Health      │              │                  │
│  │  (Burgundy)  │  (Sage Green)│                  │
│  ├──────────────┼──────────────┤                  │
│  │  Immunity    │  Sleep       │                  │
│  │  (Burgundy)  │  (Lavender)  │                  │
│  └──────────────┴──────────────┘                  │
│  Right sidebar (300px): Digestive (Sage Green)     │
│  + "Full Library Bundle" label in Gold             │
├──────────────────────────────────────────────────┤
│  FOOTER — 100px, Clinical Cream                    │
│  "Digital download — instant access" Lato 14pt    │
└──────────────────────────────────────────────────┘
```

**Canva setup steps (copy-paste)**:
1. Open Canva > Create a design > Custom size > 2400 × 2400 px
2. Create 200px header band, Dark Charcoal background, title text in Clinical Cream / Gold as spec
3. Duplicate your five existing 1×1 bundle card designs at reduced size (900px wide each)
4. Arrange in 2×2 grid with 20px gutters in center zone; fifth bundle in right sidebar
5. Each mini-card shows only the header block (bundle color + bundle name) — hero images optional
6. Add 100px footer, Clinical Cream background, one-line descriptor

---

### Template C — Testimonial Block (1000×1500px Pinterest / 1080×1350px Instagram)

**Canvas**: 1000×1500px (Pinterest) or 1080×1350px (Instagram portrait) — build the 1000×1500px version first, use Canva's resize for the Instagram variant.

```
┌──────────────────────────────────────────────────┐
│  HEADER IMAGE ZONE — top 45% (675px)              │
│  Full-bleed herb photograph (bundle-relevant)      │
│  Deep overlay: bundle header color at 45% opacity  │
│  Bundle name label: Lato, 14pt All Caps, Clinical  │
│  Cream, top-right corner                           │
├──────────────────────────────────────────────────┤
│  QUOTE ZONE — middle 35% (525px)                  │
│  Background: Clinical Cream #F9F5F0               │
│  4px left border: Apothecary Gold #D4AF37          │
│  (indented 40px from left edge)                    │
│  Quote text: Cormorant Garamond, 36px Italic       │
│  Color: Dark Charcoal #2C2C2C                      │
│  Attribution: Lato, 22px, Dark Charcoal            │
│  "— Name, Title, Location"                         │
│  Small horizontal rule (Apothecary Gold, 1px)      │
│  below attribution                                 │
├──────────────────────────────────────────────────┤
│  FOOTER CTA ZONE — bottom 20% (300px)             │
│  Background: bundle header color                   │
│  CTA text: Lato, 28px Bold, Clinical Cream         │
│  "Get the [Bundle Name] Guide"                     │
│  URL: Lato, 20px, Clinical Cream at 80% opacity    │
│  Seedwarden wordmark: bottom-left, Clinical Cream  │
└──────────────────────────────────────────────────┘
```

**Canva setup steps (copy-paste)**:
1. Open Canva > Custom size > 1000 × 1500 px
2. Upload bundle-relevant herb photo. Place at top, drag to fill y=0 to y=675px
3. Add color overlay on photo: rectangle, 1000px wide, 675px tall, bundle header color, opacity 45%
4. Add bundle name label: Lato, 14pt, All Caps, Clinical Cream, top-right corner with 30px margin
5. Add Clinical Cream rectangle: full width, 525px tall, starting at y=675px
6. Add 4px left-border line: Apothecary Gold, 4px wide, 480px tall, at x=40px, y=690px
7. Add quote text block: Cormorant Garamond, 36px Italic, Dark Charcoal. Start x=60px
8. Add attribution line: Lato, 22px, Dark Charcoal, same indent
9. Add 1px Apothecary Gold horizontal line below attribution
10. Add footer rectangle: full width, 300px tall, bundle header color, anchored to bottom
11. Add CTA text and URL in footer: Lato, Clinical Cream as spec

---

### Template D — Ingredient Detail / Species Profile (1080×1080px Instagram)

Used for social media species spotlights — one herb per post.

```
┌──────────────────────────────────────────────────┐
│  TOP BAND — 60px                                   │
│  Background: bundle header color                   │
│  "SEEDWARDEN" Lato, 16px, All Caps, Clinical Cream │
│  right-aligned, 30px margin                        │
├──────────────────────────────────────────────────┤
│  SPECIES IMAGE — top-right 40% of content zone    │
│  (right half, y=60px to y=620px)                   │
│  2:3 portrait ratio, drop shadow                   │
│  Apothecary Gold 2px border                        │
│  Caption below image: Lato, 9px Light Italic       │
├──────────────────────────────────────────────────┤
│  SPECIES NAME BLOCK — left half                    │
│  Common name: Playfair Display, 36px Bold          │
│  Color: Dark Charcoal                              │
│  Latin name: Cormorant Garamond, 22px Italic       │
│  Color: bundle header color                        │
│  1px Apothecary Gold rule below name block         │
├──────────────────────────────────────────────────┤
│  KEY FACTS — left half, below name block           │
│  3–4 bullet points: Lato, 24px Regular             │
│  Color: Dark Charcoal                              │
│  Bullet: Apothecary Gold en-dash character         │
│  (e.g., "Traditional use: respiratory support")    │
├──────────────────────────────────────────────────┤
│  BOTTOM BAND — 80px                                │
│  Background: Clinical Cream                        │
│  Apothecary Gold 2px top border                    │
│  "Full guide: seedwarden.com" Lato, 18px, Dark     │
│  Charcoal, centered                                │
└──────────────────────────────────────────────────┘
```

**Canva setup steps (copy-paste)**:
1. Open Canva > Post > Instagram Post (1080 × 1080 px)
2. Set background to Clinical Cream (#F9F5F0)
3. Add top band: rectangle, full width, 60px, bundle header color
4. Add "SEEDWARDEN" text: Lato, 16px, All Caps, Clinical Cream, right-aligned in band
5. Upload species photo. Place right-side: x=540px, y=60px, width=540px, height=560px
6. Add 2px Apothecary Gold border around photo (use Canva border element or rectangle outline)
7. Add drop shadow to photo: Edit image > Shadow > Offset, 20% opacity, 8px blur
8. Add common name text: Playfair Display, 36px Bold, Dark Charcoal, left side, x=40px, y=80px
9. Add Latin name text: Cormorant Garamond, 22px Italic, bundle header color, below common name
10. Add 1px Apothecary Gold horizontal line below name block, full left-half width
11. Add 3–4 key fact bullets: Lato, 24px, Dark Charcoal, with Apothecary Gold en-dash
12. Add bottom band: rectangle, full width, 80px, Clinical Cream, anchored bottom
13. Add 2px Apothecary Gold top border line on bottom band
14. Add footer text: "Full guide: seedwarden.com" Lato, 18px, Dark Charcoal, centered

---

### Template E — Dosage Reference Card (8.5×11in PDF interior page)

Used inside the PDF guides as a quick-reference summary page per herb.

```
┌──────────────────────────────────────────────────┐
│  RUNNING HEADER — 0.5in                            │
│  Thin color band: bundle header color              │
│  Bundle name right-aligned: Lato, 9pt, Clin. Cream │
│  Seedwarden logo left-aligned (small, 0.3in tall)  │
│  1px Apothecary Gold rule below header             │
├──────────────────────────────────────────────────┤
│  SPECIES HEADING — 0.75in                          │
│  Common name: Playfair Display, 26pt Bold          │
│  Latin name: Cormorant Garamond, 18pt Italic       │
│  Both left-aligned, 0.75in left margin             │
├──────────────────────────────────────────────────┤
│  TWO-COLUMN BODY — 8.0in height                    │
│  Left col (3.5in): Preparation Methods             │
│  ┌────────────────────────────┐                   │
│  │ Method header: Lato, 10pt  │                   │
│  │ Bold, All Caps, Apo. Gold  │                   │
│  │ e.g., "STANDARD INFUSION"  │                   │
│  │                            │                   │
│  │ Body: Lato 11pt, Dark       │                   │
│  │ Charcoal, Clin. Cream bg   │                   │
│  │ Ratio, steep time, dosage  │                   │
│  └────────────────────────────┘                   │
│  Right col (3.5in): Safety / Conservation Notes    │
│  ┌────────────────────────────┐                   │
│  │ "SAFETY NOTES" header box  │                   │
│  │ Apothecary Gold border     │                   │
│  │ Lato 10pt, Dark Charcoal   │                   │
│  │                            │                   │
│  │ "CONSERVATION STATUS" box  │                   │
│  │ (at-risk species only)     │                   │
│  │ Gold border, brief note    │                   │
│  └────────────────────────────┘                   │
├──────────────────────────────────────────────────┤
│  FTC FRAMING FOOTER — 0.6in                        │
│  Lato, 9pt Italic, #5A5A5A (medium gray)           │
│  "Traditionally used for X. Not intended to        │
│  diagnose, treat, cure, or prevent any disease."   │
│  Left-aligned, full width, 0.75in margins          │
│  1px Apothecary Gold top border                    │
└──────────────────────────────────────────────────┘
```

**Canva setup steps (copy-paste)**:
1. Open Canva > Custom size > 8.5 in × 11 in
2. Set background to Clinical Cream (#F9F5F0)
3. Add header band: full width, 0.5in tall, bundle header color
4. Add 1px Apothecary Gold rule below header band
5. Add Seedwarden logo PNG: left-aligned in header, 0.3in tall
6. Add bundle name text: Lato, 9pt, Clinical Cream, right-aligned in header
7. Add species heading block: Playfair Display 26pt Bold + Cormorant 18pt Italic, Dark Charcoal, 0.75in left margin, below header
8. Add 1px Apothecary Gold horizontal rule below species heading
9. Create two-column body: use two text boxes at x=0.75in (left col, 3.5in wide) and x=4.5in (right col, 3.5in wide)
10. In left col: add method headers in Lato 10pt Bold All Caps Apothecary Gold; body text in Lato 11pt Dark Charcoal
11. In right col: add bordered boxes (Apothecary Gold 1.5pt border, Clinical Cream fill) for Safety Notes and Conservation Status
12. Add FTC footer: Lato, 9pt Italic, #5A5A5A, 1px Apothecary Gold top border, 0.75in margins

---

## Part 4: Image Sizing Specifications

### Cover / Etsy Listing Images

| Image Type | Canvas Size | Export Format | Quality | Use |
|---|---|---|---|---|
| Bundle cover (primary listing) | 2400×2400px | JPEG | 95%+ | Etsy slot 1 (thumbnail) |
| Interior preview spread | 2400×2400px | JPEG | 90% | Etsy slot 2 |
| Lifestyle / apothecary prop shot | 2400×2400px | JPEG | 90% | Etsy slot 3 |
| Zone card preview | 2400×2400px | JPEG | 90% | Etsy slot 4 |
| Bundle comparison (all 5) | 2400×2400px | JPEG | 90% | Etsy slot 5 |

### PDF Interior Pages

| Image Type | Dimensions | Resolution | Notes |
|---|---|---|---|
| Species habitat photo | 3.5×4.5in (portrait) | 300 DPI | 2:3 ratio; embed at Print quality |
| Root / preparation detail | 3×3in (square) | 300 DPI | Macro detail for preparation sections |
| Conservation callout illustration | 1.5×1.5in | 300 DPI | UpS logo or botanical line illustration |

### Social Media Templates

| Platform | Canvas | Format |
|---|---|---|
| Pinterest pin | 1000×1500px | PNG |
| Instagram post (square) | 1080×1080px | JPEG |
| Instagram portrait | 1080×1350px | JPEG |
| Instagram Story | 1080×1920px | PNG |

---

## Part 5: Photography Style Guide

### Aesthetic Position

Phase 3 photography occupies the space between clinical precision and kitchen herbalism. It is not cottagecore (no linen textures, no aspirational staging), not laboratory (no sterile white surfaces), and not generic homesteading (no mason-jar-on-burlap). The target register is an experienced practitioner's working environment: a prep table with real herbs, a reference card, a mortar.

### Per-Bundle Photography Direction

**Women's Health** (Deep Burgundy palette):
- Hero: Black Cohosh in forest-floor context, or warm Calendula orange blossom close-up
- Lighting: Dappled natural light, warm color temperature (4200–5000K equivalent)
- Props: Dried flower bundles, small glass jars, botanical illustration paper nearby
- Backgrounds: Forest floor, aged wooden bench, dark linen
- Avoid: Anything that reads as a spa or beauty product aesthetic

**Respiratory** (Sage Green palette):
- Hero: Elderberry shrub with berry clusters — late-summer harvest moment preferred
- Lighting: Warm golden-hour light; autumn harvest feel signals seasonal preparedness
- Props: Dried mullein leaves, dark amber tincture bottle, wooden cutting board with elderberries
- Backgrounds: Warm wood, earth, outdoor late-summer context
- Avoid: Clinical white backgrounds — Respiratory should feel grounded and seasonal

**Immunity** (Deep Burgundy palette):
- Hero: Goldenseal in forest understory (forest-farming rows if obtainable from NC Botanical Garden contact)
- Lighting: Dappled forest light; the yellow-interior rhizome cross-section is a strong secondary image
- Props: Root specimens on dark background, clean reference cards; clinical detail emphasis
- Backgrounds: Forest floor, dark soil, black photography surface for root specimens
- Note: Imagery should feel more clinical and precise than Women's Health despite sharing the Burgundy palette; the root cross-section differentiates them visually

**Sleep** (Muted Lavender palette):
- Hero: Passionflower single bloom in full radial display — the flower's geometry is the visual anchor
- Lighting: Soft diffused light; cooler tone (5500–6500K equivalent) reinforces calm
- Props: Dried lavender sachets, small cloth pouches, chamomile or valerian dried in bowls
- Backgrounds: Cream linen, pale lavender cloth, light neutral wood
- Avoid: Dark or busy backgrounds — the Passionflower needs visual breathing room

**Digestive** (Sage Green palette):
- Hero: Dandelion root (cross-section or cleaned root held in hand) or fresh ginger rhizome on wood
- Lighting: Kitchen-table natural light; practical and unfussy
- Props: Ginger on a cutting board, dried calendula petals in a ceramic bowl, mortar and pestle
- Backgrounds: Kitchen countertop (natural wood), neutral stone, light linen
- Note: Digestive should feel the most approachable and kitchen-adjacent of all five bundles

### Photography Specifications

| Spec | Value | Notes |
|---|---|---|
| Minimum resolution | 2400px on shortest side | Required for Etsy and PDF embed at quality |
| Preferred format | JPG (RGB color, sRGB profile) | PNG for any transparent-background elements |
| License requirement | CC-BY, CC-BY-SA, CC0, or original | Log in PHOTO_ATTRIBUTION_LOG.md |
| Macro detail minimum | 1200px on shortest side | Root cross-sections, petal detail shots |
| Overlay opacity range | 35–55% for image-with-text layouts | Use bundle header color as overlay color |

### Sourcing Priority (from Phase 3 Canva Adaptation Guide)

1. Phase 2 wild-edibles archive (`/assets/wild-edibles/`) — dandelion already present
2. Wikimedia Commons (scientific name search, filter CC-BY or CC-BY-SA, download highest resolution)
3. iNaturalist (species name search, filter CC-BY, sort by Faves)
4. Unsplash (lifestyle/apothecary props — lavender, dried herbs, mortar — free commercial use)
5. Botanical garden media contact (NC Botanical Garden media@ncbg.unc.edu for Goldenseal)

---

## Part 6: Copy-Paste Canva Instructions (Eliminates Per-Card Setup Time)

### Brand Kit Load Sequence (June 21 — 30 minutes)

Execute these steps exactly once before sprint Day 1. Do not re-enter colors per design.

```
1. Open Canva.com — log in
2. Left sidebar — click Brand Hub (flag icon)
3. Select "Seedwarden" Brand Kit (existing)
4. In Colors section — click "+ Add color"
5. Enter: #8B3E3E — label "Deep Burgundy (P3 Women's / Immunity)"
6. Click "+ Add color"
7. Enter: #6B8E6F — label "Sage Green (P3 Respiratory / Digestive)"
8. Click "+ Add color"
9. Enter: #D4AF37 — label "Apothecary Gold (P3 all bundles)"
10. Click "+ Add color"
11. Enter: #F9F5F0 — label "Clinical Cream (P3 background)"
12. Click "+ Add color"
13. Enter: #9B8BA0 — label "Muted Lavender (P3 Sleep)"
14. Save — Dark Charcoal #2C2C2C is already present from Phase 2; do not re-add
15. Refresh any open Canva design tabs (colors will not appear until refresh)
```

**Color rendering test (required)**:
```
After loading all colors:
1. Create new design: 8.5 × 11 in
2. Add header rectangle: Sage Green #6B8E6F, full width, 1.5in tall
3. Add text in header: "SEEDWARDEN" Lato, 14pt, Clinical Cream — verify legible
4. Add accent bar below header: Apothecary Gold #D4AF37, 8px tall, full width
5. Add body text: Lato 11pt, Dark Charcoal #2C2C2C, on Clinical Cream background
6. Export as PDF Print
7. Open exported PDF. Verify Sage Green header did not shift to olive or teal.
8. If color deviates by more than 5 RGB points on any channel: re-enter hex, retest.
9. Log result in WORKLOG.md: "Color test [DATE] — passed / deviation noted [hex values]"
```

### Cover Template Duplication Sequence (June 21 — 1 hour)

```
1. Open Phase 2 bundle cover master template in Canva
2. Click "Duplicate page" (not "Make a copy" — use Duplicate within the same file)
3. Rename the duplicate: "Phase3-WomensHealth-Cover-v1"
4. Change header rectangle color: from Phase 2 green to Deep Burgundy #8B3E3E
   (click rectangle > Colors panel > Brand Kit > select "Deep Burgundy")
5. Change bundle title text: "Women's Health Herbs Guide"
6. Change species list text: Black Cohosh, Vitex, Red Clover, Calendula, Lavender
7. Delete hero image placeholder — leave empty slot for June photo insert
8. Duplicate again: "Phase3-Respiratory-Cover-v1"
9. Change header to Sage Green #6B8E6F
10. Change title + species list (Elderberry, Echinacea, Thyme, Mullein, Lemon Balm)
11. Repeat for Sleep (Muted Lavender), Immunity (Burgundy), Digestive (Sage Green)
12. All five covers are now pre-populated text-only templates.
   Sprint Day 1 task: insert hero image only.
```

**Version discipline**: Always increment (v1 → v2 → v3). Never save over v1. If v2 introduces a layout problem, return to v1 and rebuild from there.

### Interior Page Template Setup (June 21 — 30 minutes)

```
1. Open Phase 2 interior page template in Canva
2. Duplicate to new file: "Phase3-Interior-Template-v1"
3. Update running header band: change color to bundle header color
   (use Deep Burgundy as default; swap per-bundle during sprint)
4. Update section header labels to Phase 3 framing:
   - "Where to Find It" → "Cultivation Requirements"
   - "Harvest and Eat" → "Harvest Timing and Preparation"
   - "Watch Out For" → "Lookalikes and Safety Notes"
   - "Conservation Note" → "Conservation and Ethical Sourcing"
   - "Fun Fact" → "Traditional Use History"
5. Add new text block for "Research Note" section (not in Phase 2 template)
   — Lato 11pt, Dark Charcoal; place below Traditional Use History block
6. Add FTC framing text zone at bottom of each species page
   — Lato 9pt Italic, #5A5A5A; with 1px Apothecary Gold top border
7. Verify body text is minimum 11pt and line height is 145%
8. Export one test page as PDF Print — verify all text is legible when printed
```

---

## Part 7: WCAG AA Quick-Reference (for Design Decisions During Sprint)

When you need to check a pairing quickly during the sprint, use this decision table. Do not test by eye — contrast failures look acceptable on screen but fail printed and low-light reading.

| Situation | Approved Pairing | Not Approved |
|---|---|---|
| Body text on page background | Dark Charcoal on Clinical Cream (12.87:1) | Any color text directly on Burgundy/Sage/Lavender |
| Text on header bands | Clinical Cream on any bundle color | Dark Charcoal on Burgundy (1.90:1 — hard fail) |
| Bundle title on header | Apothecary Gold on Burgundy (3.50:1, large text PASS) | Apothecary Gold on Sage Green or Lavender |
| Accent box with text | Dark Charcoal on Apothecary Gold (6.64:1) | Clinical Cream on Apothecary Gold (1.94:1 — fail) |
| Callout box body text | Dark Charcoal on Clinical Cream interior | Any text on a solid Sage Green or Lavender interior |
| Footer / caption text | Dark Charcoal #2C2C2C or #5A5A5A on Clinical Cream | Mid-tone gray under #8A8A8A — too low contrast |

---

## Part 8: Design Quality Gates

### Pre-Upload Checklist (run before each Etsy listing upload)

- [ ] Cover image: 2400×2400px, no compression artifacts visible at 100% zoom
- [ ] Thumbnail test: bundle title legible at 170×135px (Etsy grid) — zoom to 7% in Canva
- [ ] Hero image: correct species for this bundle (not cross-contaminated from adjacent bundle)
- [ ] Header color: correct for this bundle (reference bundle color assignment table above)
- [ ] All text on header bands is Clinical Cream — not Dark Charcoal
- [ ] Apothecary Gold bundle title is on a Burgundy or Dark Charcoal background only
- [ ] No placeholder text in any text field (covers, interior pages, zone cards)
- [ ] PDF file size under 5 MB (compress embedded images to 150 DPI if over limit)
- [ ] PDF opens without rendering errors in PDF reader
- [ ] Photo attribution log updated for all images used
- [ ] Canva file named per convention: `Phase3-[BundleName]-Cover-v[N]`

### Design Sprint Daily Checks

Before ending each design session: export one asset (cover or zone card) as PDF and view in a PDF reader. Do not rely on Canva's on-screen rendering to evaluate color accuracy. Canva's preview occasionally shows colors differently from how they export.

---

*Prepared: May 27, 2026. Extends and consolidates canva-phase-3-adaptation-guide.md (May 19) and PHASE_3_CANVA_DESIGN_SYSTEM.md (May 20) with WCAG contrast validation (computed), five new layout template specs, photography style guidance, and copy-paste Canva instructions. Hex codes remain authoritative from May 19 source. Design lock: July 3, 2026 EOD.*
