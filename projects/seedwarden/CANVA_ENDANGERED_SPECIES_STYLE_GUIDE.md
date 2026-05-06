---
title: "Canva Template Style Guide — Endangered Species Series"
date: 2026-05-06
status: ready to implement — requires Canva Brand Kit (existing Seedwarden Kit + endangered species overrides)
scope: Wave 1 guides (Ginseng, Goldenseal, Black Cohosh, Ramps) + Etsy listing images
references:
  - CANVA_EXECUTION_PLAYBOOK.md (native plants template reference)
  - CANVA_ZONE_CARD_DESIGN_GUIDE.md (zone card aesthetic reference)
  - TRACK_B_CANVA_SETUP_AND_EXPORT_GUIDE.md (export specs)
  - phase-2-production-progress.md
---

# Canva Template Style Guide — Endangered Species Series

**Purpose**: Design system for the Appalachian Medicinals endangered species guide series. Differentiated from native plants / forager catalog aesthetic while remaining within the Seedwarden brand system. The endangered species series communicates gravity, conservation urgency, and deep knowledge — a different register than the abundance-and-accessibility feel of the native plants guides.

---

## Part 1: Design Principle — Differentiation From Native Plants Guides

The existing Seedwarden catalog (native plants, seed saving, zone cards) reads as: *approachable, abundant, practical, earthy-warm.*

The endangered species series reads as: *authoritative, measured, conservation-serious, respect-for-rarity.*

The two series must be visually distinct enough that a buyer looking at both product thumbnails understands they are different things — one is "here's what's growing everywhere," the other is "here's what's disappearing and why it matters."

The differentiation mechanism is **the color palette** (darker, deeper soil tones vs. the warmer cream-and-green of the native plants palette) and **typography weight** (heavier, more formal heading treatment vs. the lighter botanical-guide style of existing guides).

---

## Part 2: Color Palette — "Deep Soil" (Endangered Species Series)

These colors supplement the existing Seedwarden Brand Kit. Add them as a second palette group in Canva: label it "Endangered Species Series" to distinguish from the main Seedwarden palette.

| Color Name | Hex Code | Use |
|---|---|---|
| Deep Forest Floor | #1C2B1A | Primary dark background for section headers; replaces Deep Forest Green for this series |
| Aged Bark | #3B2A1A | Secondary dark — used for dividers, accent bars, rule lines |
| Pale Parchment | #F0E6C8 | Body text background fields; same register as Seedwarden Warm Cream but cooler |
| Sage Mist | #7A9A6E | Accent lines, bullet points, section markers |
| Bone White | #F5F1E8 | Full-page background (off-white, not stark white — maintains warmth) |
| Conservation Red | #8B2000 | Used sparingly — conservation status callout boxes only |
| Species Gold | #C49A2A | Pull quote highlights, species name accents, "Quick Reference" card header |

**Critical**: Conservation Red (#8B2000) is a high-signal color for this series. It appears only in conservation status callout boxes ("CITES Appendix II," "State Endangered," "UpS At-Risk"). It should not appear in general body content or decorative elements.

**Relationship to existing palette**: Deep Forest Floor (#1C2B1A) replaces Deep Forest Green (#143b28) as the primary header color. Pale Parchment (#F0E6C8) replaces Warm Cream (#F5EDD6). All other base elements (Sage, Burnt Sienna) carry over and unify the two series visually.

---

## Part 3: Typography

Same fonts as the main Seedwarden system — no change. Differentiation comes from weight and size hierarchy, not font choice.

| Role | Font | Weight/Style | Size |
|---|---|---|---|
| Guide title (cover) | Playfair Display | Bold | 36–48pt |
| Species name (cover, Latin) | Cormorant Garamond | Italic | 24–30pt |
| Section headers (inside pages) | Playfair Display | Regular | 18–22pt |
| Body text | Lato | Regular | 10–11pt |
| Caption text | Lato | Light Italic | 8–9pt |
| Quick Reference card labels | Lato | Bold | 9–10pt |
| Conservation status callout | Playfair Display | Bold Italic | 11pt |
| Series tagline | Cormorant Garamond | Italic | 14pt |

**Cover treatment**: Species scientific name in Cormorant Garamond Italic, centered beneath the common name in Playfair Display Bold. This creates a two-line cover identity — common name large and accessible, scientific name smaller and authoritative. Consistent across all four Wave 1 guides.

---

## Part 4: Cover Template Specification

Each guide cover uses the same template with species-specific photo and accent color swaps.

### Layout (8.5 x 11 inches, portrait)

**Background**: Full-bleed habitat photograph (the habit photo sourced per ENDANGERED_SPECIES_PHOTO_PIPELINE.md). Apply a dark overlay at 55–65% opacity using Deep Forest Floor (#1C2B1A) to ensure text legibility over the photo.

**Top bar** (1.5 inches from top): Seedwarden logo (white) left-aligned. Series name "APPALACHIAN MEDICINALS" in Lato Bold, small caps, letter-spaced, right-aligned. Both on the dark overlay strip.

**Center block** (vertically centered in the lower two-thirds of the page):
- Series title: "Appalachian Medicinals — Wave 1" in Lato, 11pt, Sage Mist, letter-spaced
- Species common name: Playfair Display Bold, 42pt, Bone White
- Species Latin name: Cormorant Garamond Italic, 22pt, Species Gold (#C49A2A)
- Tagline line: "Know it. Grow it. Protect it." in Lato Regular, 12pt, Pale Parchment
- Thin rule (2px, Sage Mist) above and below the species name block

**Bottom bar** (1 inch from bottom): Conservation status badge left-aligned. Use a pill-shaped badge with Conservation Red fill (#8B2000), white text, Lato Bold 9pt. Text: "CITES APPENDIX II" or "UPS AT-RISK" or "STATE LISTED ENDANGERED" as appropriate per species.

**Bottom right**: "seedwarden.com" in Lato Light, 9pt, Sage Mist.

### Conservation Status Badge Per Species

| Species | Badge Text |
|---|---|
| American Ginseng | CITES APPENDIX II |
| Goldenseal | CITES APPENDIX II |
| Black Cohosh | UPS AT-RISK |
| Ramps | STATE PROTECTED — MULTIPLE STATES |

---

## Part 5: Interior Page Template Specification

### Page Layout (8.5 x 11 inches, portrait, 0.75-inch margins all sides)

**Header bar** (top of every interior page): 0.25-inch deep bar in Deep Forest Floor (#1C2B1A). Left: species common name in Lato Bold 9pt Bone White. Right: guide title in Lato Light 9pt Pale Parchment. This is the running header.

**Section headers**: Playfair Display Regular, 18pt, Deep Forest Floor. Preceded by a 1px Sage Mist rule. Left-aligned.

**Body text**: Lato Regular, 10.5pt, leading 14pt. Color: #2A2A2A (very dark gray, not pure black — reduces eye strain). Two-column layout for Quick Reference Card; single column for all narrative sections.

**Conservation Status Callout Box** (appears once per guide, near the top of Section 2 or 3):
- Background: Conservation Red (#8B2000) at 15% opacity (very light tint, not solid red)
- Border: 2px left rule in Conservation Red at 100% opacity
- Header text: "CONSERVATION STATUS" in Lato Bold 9pt Conservation Red
- Body text: Status information in Lato Regular 10pt Deep Forest Floor
- This is the only red element in the interior pages

**Quick Reference Card** (final section of every guide):
- Background: Pale Parchment (#F0E6C8)
- Header: "QUICK REFERENCE" in Playfair Display Bold 14pt, Species Gold color bar behind it
- Two-column table, alternating row tint (white and Bone White)
- Border: 1px Aged Bark (#3B2A1A) on outer frame

**Photo captions**: Lato Light Italic, 8pt, Sage Mist. Attribution line below caption in same style. Example: *"American ginseng (Panax quinquefolius) in mature hardwood understory, Pennsylvania, September. Photo: [observer name], CC BY 4.0, iNaturalist."*

---

## Part 6: Etsy Listing Image Specs (Endangered Species Guides)

These are distinct from the native plants and forager product listing images already in production. The endangered species listings need their own image set.

### Image Slot Strategy (Per Guide)

| Slot | Content | Dimensions | Canva Size |
|---|---|---|---|
| 1 (thumbnail) | Cover design with species photo + title overlay | 2400 x 2400px | Square crop of cover design |
| 2 (interior preview) | 2-page spread mockup (Quick Reference Card + Section 1) | 2400 x 2400px | Interior page preview |
| 3 (conservation context) | Split image: conservation status callout + seed supplier info | 2400 x 2400px | Custom layout |
| 4 (lifestyle) | Printed pages on forest floor or wooden surface with leaves | 2400 x 2400px | Photo-based (lifestyle shoot) |
| 5 (bundle preview) | All 4 Wave 1 guide covers arranged as a bundle visual | 2400 x 2400px | Bundle collage layout |

**For initial Etsy launch (pre-lifestyle-photo)**: Slots 1–3 only. Slots 4–5 added in Phase 2 once lifestyle photography is available.

### Thumbnail Design (Slot 1) — Critical

The Etsy thumbnail is the single most important design decision for the endangered species series. Competing listings in the "endangered plants guide" category are predominantly text-heavy, low-contrast designs. Differentiation comes from:

1. A striking habitat photograph (full-bleed, species in natural context)
2. Legible species name text at thumbnail scale (Playfair Display Bold, at minimum 18pt equivalent at full size — appears as approximately 3px at thumbnail; must be visible)
3. The Conservation Red badge as a distinctive signal element — buyers in the conservation-conscious naturalist cohort will recognize CITES Appendix II as a quality signal

**Test the thumbnail at 50px x 50px in Canva** (reduce canvas view to 25% zoom while designing). If the species name is not readable and the photo is not striking at that size, the design needs revision before export.

---

## Part 7: Bundle Design — "Appalachian Medicinals Wave 1"

The four-guide bundle ($32) needs a specific bundle cover design for the Etsy listing thumbnail.

**Layout**: Four guide covers arranged in a 2x2 grid, each at 45% of the bundle image size, with a 5% gap between covers. Bundle title "APPALACHIAN MEDICINALS" in Playfair Display Bold, centered above the grid. Price badge optional (omit — Etsy shows price separately).

**Background**: Aged Bark (#3B2A1A) at 90% — dark, serious, differentiated from any existing Seedwarden product.

**Subtitle**: "Know It. Grow It. Protect It." in Cormorant Garamond Italic, centered below the grid. Bone White. 14pt.

**Seedwarden logo**: Bottom center. White.

---

## Part 8: Production Sequence

Execute in this order:

1. **Add endangered species palette to existing Canva Brand Kit** (10 minutes — add the 7 new hex codes as a second color group labeled "Endangered Species Series")
2. **Build American Ginseng cover** as the master template (45–60 minutes)
3. **Duplicate cover template** three times; swap species photo, name, and badge for Goldenseal, Black Cohosh, Ramps (15 minutes each)
4. **Build interior page master** (30–45 minutes): set up running header, section header style, conservation callout box, Quick Reference card layout
5. **Duplicate interior page master** and apply to each guide (20 minutes each — same template, content-swap only)
6. **Export all four guide PDFs** per settings in TRACK_B_CANVA_SETUP_AND_EXPORT_GUIDE.md: PDF Print, CMYK (even for digital — preserves quality), all pages
7. **Export Etsy thumbnails (Slot 1)**: PNG, 2400 x 2400px, per guide
8. **Build bundle cover design** (30 minutes)
9. **Log all exports** in phase-2-production-progress.md

---

**Prepared**: 2026-05-06 (Phase 2 production kickoff)
**Design owner**: User (Canva execution)
**Content owner**: Agent (guide text and spec)
**Status**: Ready to implement — no blockers
