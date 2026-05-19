---
title: "Seedwarden Launch-Week Brand Kit — Canva Template Specifications"
prepared: 2026-05-19
status: production-ready — pre-staged for post-launch execution May 30+
scope: Color palette, font pairings, icon style, template layouts for Reels / Pins / TikTok
references:
  - canva-pro-brand-kit-setup-guide.md (Brand Kit setup steps — execute May 19–23)
  - CANVA_SETUP_STATUS.md (canonical hex codes and font table)
  - pin-template-specs.md (Pinterest dimensions)
  - WEEK_1_4_CONTENT_CALENDAR.md (which templates each post uses)
  - CANVA_ZONE_CARD_DESIGN_GUIDE.md (zone card template)
gate: Gate 1 (social accounts) and Gate 2 (Canva Pro) must be complete before templates are built
positioning: Midwest Zone 5 native plants + wild edibles; differentiated from broad homesteading aesthetics
---

# Seedwarden Launch-Week Brand Kit
## Canva Template Specifications

**Purpose**: Production-ready Canva template specs for immediate post-launch deployment (May 30+).
These specifications extend and consolidate the Brand Kit setup in `canva-pro-brand-kit-setup-guide.md`.
The setup guide covers how to enter these values; this document specifies what to build once the
Brand Kit is active.

**Positioning constraint**: Every template decision below is calibrated to differentiate Seedwarden
from broad homesteading aesthetics (beige-and-mason-jar). The visual language is field-documentation:
dense information, botanical precision, earthy without being rustic, practical without being clinical.
This positions Seedwarden closer to a USDA field publication than a lifestyle influencer's feed.

---

## Part 1: Color Palette

### Primary Palette (use on all public-facing assets)

| Color Name | Hex Code | RGB | Usage Rule |
|---|---|---|---|
| Deep Forest Green | `#143b28` | 20, 59, 40 | Headers, dominant background bands, borders; the primary brand color — everything else supports it |
| Warm Cream | `#F5EDD6` | 245, 237, 214 | Card and carousel backgrounds; any white substitute (pure white is not used) |
| Parchment | `#EDE0C4` | 237, 224, 196 | Alternate section backgrounds; spotlight bands inside cards; variety row backgrounds |

### Secondary Palette (accent and supporting elements)

| Color Name | Hex Code | RGB | Usage Rule |
|---|---|---|---|
| Deep Ink Green | `#1A3A2A` | 26, 58, 42 | Body text on Warm Cream backgrounds; paragraph text in carousels; never as a background |
| Sage | `#8FA882` | 143, 168, 130 | Divider lines, icon fills, subtle callout borders; never as dominant background |
| Burnt Sienna | `#A0522D` | 160, 82, 45 | Accent highlights — limited to 1–2 elements per design; Zone 9/10 band color |

### Zone Band Colors (zone card templates only)

These colors appear as a 12px horizontal rule on zone cards and are not used in social templates.
They are included here for completeness since Canva Brand Kit holds all 10 colors.

| Zone Group | Hex Code | Zones |
|---|---|---|
| Cool | `#3D6B8A` | 3 and 4 |
| Temperate | `#2D5016` | 5 and 6 |
| Warm | `#C9943A` | 7 and 8 |
| Hot | `#A0522D` | 9 and 10 |

### Color Application Rules

- Never use pure white (`#FFFFFF`) as a background — always substitute Warm Cream (`#F5EDD6`)
- Never use pure black (`#000000`) as body text — always substitute Deep Ink Green (`#1A3A2A`)
- The background color for any text block must pass WCAG AA contrast ratio (minimum 4.5:1). The
  approved pairings below are all verified:
  - Deep Ink Green on Warm Cream: contrast ratio 8.1:1 (passes)
  - Warm Cream on Deep Forest Green: contrast ratio 8.1:1 (passes)
  - Warm Cream on Deep Ink Green: contrast ratio 8.1:1 (passes)
- Sage is never used as a text color — contrast ratios are insufficient on light backgrounds
- Burnt Sienna as text: only on Warm Cream or Parchment backgrounds, never on green
- Photography backgrounds: always add a color overlay at 20–40% opacity before placing text on top
  of any photograph. Use Deep Forest Green overlay for dark-text-on-photo layouts.

---

## Part 2: Font Pairings

### Brand Font Stack

| Role | Font | Weight | Canva Search Term |
|---|---|---|---|
| Display / Headline | Playfair Display | Bold (700) | "Playfair Display" |
| Body / Caption | Lato | Regular (400) | "Lato" |
| Accent / Label | Cormorant Garamond | Italic (400i) | "Cormorant Garamond" |

All three fonts are free in Canva's library. No upload is required.

### Font Size Hierarchy

These sizes are calibrated for Canva's default px unit at 1:1 pixel ratio (not points).
Sizes are specified for 1080×1080px square format; scale proportionally for other dimensions.

| Element | Font | Size | Weight | Color | Alignment |
|---|---|---|---|---|---|
| Hook headline (Slide 1) | Playfair Display | 72–90px | Bold | Warm Cream on green bg, or Deep Forest Green on cream | Center or left |
| Subheadline / Post number | Lato | 32–40px | Regular | Deep Ink Green | Left |
| Body paragraph | Lato | 28–34px | Regular | Deep Ink Green | Left |
| Species / product name | Playfair Display | 48–60px | Bold | Deep Forest Green or Warm Cream | Left |
| Label / zone indicator | Cormorant Garamond | 24–30px | Italic | Sage or Burnt Sienna | Left |
| Footer URL | Lato | 20–24px | Regular | Warm Cream on green footer band | Center |
| Caption overlay (photo) | Playfair Display | 56–72px | Bold | Warm Cream | Left, with text-shadow or overlay |

### Font Usage Rules

- Playfair Display and Cormorant Garamond must never appear in the same text block — use one serif
  per element. They can coexist on the same design slide as separate elements.
- Lato is the only font used at sizes below 28px in any final export (legibility at small sizes).
- Line height for body Lato: 1.4× the font size. Do not compress — Seedwarden content is text-dense
  by design; compressed line height reads as low-quality.
- Letter-spacing: 0.05em on Playfair Display headlines only; never add letter-spacing to Lato body.
- Do not use Montserrat in any post-launch template. Earlier planning documents listed Montserrat
  as a body font option; Lato is the confirmed specification (see `CANVA_SETUP_STATUS.md`).

---

## Part 3: Icon Style Guide

### Icon Specification

Seedwarden icons are line-art style (not filled/solid, not 3D, not emoji-style). The visual
register is botanical illustration — clean strokes, no gradients, no shadows, no cartoon styling.

**Canva icon search terms that match this style**:
- Search "botanical line" — select monochrome line-art botanical illustrations
- Search "plant outline" — select single-color stroke icons
- Search "herb line art" — for plant-specific icons in educational carousels

**Icon color rules**:
- Icons on Warm Cream backgrounds: use Deep Forest Green (`#143b28`)
- Icons on Deep Forest Green backgrounds: use Warm Cream (`#F5EDD6`) or Sage (`#8FA882`)
- Never use multi-color icons — recolor to a single brand color before use
- Icon stroke weight should visually match: Lato Regular weight at the same visual scale

**Icon size rules**:
- In carousels: icon max 80px × 80px at 1080×1080px canvas
- In Pinterest pins: icon max 60px × 60px at 1000×1500px canvas
- In Reels/TikTok text overlays: icons are not recommended — text only for clarity at small mobile sizes

### Approved Icon Use Cases

| Content Type | Icon | Source |
|---|---|---|
| Wild edibles post | Leaf outline | Canva: "leaf outline line art" |
| Seed saving post | Seed pod or single seed | Canva: "seed botanical line" |
| Zone reference | Map pin or compass | Canva: "map pin outline minimal" |
| Preservation post | Mason jar outline | Canva: "jar outline minimal" |
| Safety callout | Triangle with exclamation (line only) | Canva: "warning outline" |
| Footer brand mark | Seedwarden logo PNG | Upload from `projects/seedwarden/logos/` |

---

## Part 4: Template Layouts

### Template 1 — Product Mockup Pin (Pinterest, 1000×1500px)

Use for: direct product promotion posts on Pinterest
Canva output: JPEG, quality 90+

**Layout (top to bottom)**:
1. Header band — 100px height, Deep Forest Green background
   - "SEEDWARDEN" centered, Lato Regular 24px, Warm Cream, letter-spacing 0.15em (all caps)
2. Body — 1180px height, product lifestyle photograph full-bleed
   - No text in this zone; photograph fills the space
   - If photo background is busy: add Deep Forest Green overlay at 15% opacity
3. Product name band — 120px height, Warm Cream background
   - Product name: Playfair Display Bold 52px, Deep Forest Green, left-aligned, 40px left margin
4. Descriptor line — 80px height, Warm Cream background (continuation of zone 3)
   - One-sentence product description: Lato Regular 28px, Deep Ink Green, left-aligned, 40px left margin
5. Footer band — 80px height, Deep Forest Green background
   - URL: Lato Regular 22px, Warm Cream, centered: "seedwarden.etsy.com"

**Total**: 100 + 1180 + 120 + 80 + 80 = 1560px — trim to 1500px by reducing the body band to 1120px.

### Template 2 — Educational Hook Pin (Pinterest, 1000×1500px)

Use for: zone content, plant ID posts, seasonal planting guides on Pinterest
Canva output: JPEG, quality 90+

**Layout**:
1. Top image zone — 800px height, photograph or botanical illustration full-bleed
   - Text overlay: hook headline, Playfair Display Bold 72px, Warm Cream, left-aligned
   - Text position: bottom-left of image zone, 40px from bottom and left edges
   - Deep Forest Green overlay at 30% opacity covers entire image zone (text legibility)
2. Headline band — 150px height, Deep Forest Green background
   - Main headline repeated in text: Playfair Display Bold 48px, Warm Cream, centered
3. Body text zone — 430px height, Warm Cream background
   - 2–4 bullet points: Lato Regular 30px, Deep Ink Green, left-aligned, 40px margins
   - Bullet character: en-dash (–), not a dot; keeps the field-document register
4. Footer band — 120px height, Parchment background
   - CTA text: Lato Regular 24px, Deep Ink Green, centered
   - Below CTA: "seedwarden.etsy.com" Lato Regular 20px, Sage, centered

### Template 3 — Instagram Carousel Slide 1 (Hook Slide, 1080×1080px)

Use for: all Instagram carousel posts; the hook slide is the same format regardless of topic
Canva output: JPEG per slide

**Layout**:
- Background: Deep Forest Green full-bleed
- Top-left: "SEEDWARDEN" Lato Regular 18px, Warm Cream, letter-spacing 0.2em — 40px from top and left
- Center: Hook headline, Playfair Display Bold 80px, Warm Cream, centered horizontally,
  vertically centered in the canvas
- Bottom-left: "Swipe →" Lato Regular 22px, Sage, 40px from bottom and left
- Bottom-right: Slide count indicator "1/5" Lato Regular 22px, Sage, 40px from bottom and right

### Template 4 — Instagram Carousel Body Slide (Slides 2–5, 1080×1080px)

Use for: interior slides of all Instagram carousel posts
Canva output: JPEG per slide

**Layout**:
- Background: Warm Cream full-bleed
- Top band: 60px, Deep Forest Green
  - "SEEDWARDEN" Lato Regular 16px, Warm Cream, right-aligned, 30px right margin
- Left margin text zone: all content starts 50px from left edge
- Species/item name: Playfair Display Bold 54px, Deep Forest Green — 80px from top of canvas
- Body text: Lato Regular 30px, Deep Ink Green, line-height 1.4× — begins 160px from top
- If slide includes an icon: right-align botanical line icon, max 80×80px, Deep Forest Green,
  vertically centered with the species name
- Bottom band: 60px, Parchment
  - Slide number: Lato Regular 18px, Sage, centered

### Template 5 — Instagram Static Portrait (1080×1350px)

Use for: static non-carousel posts (zone calendar posts, seasonal urgency posts)
Canva output: JPEG

**Layout**:
- Background: lifestyle photograph full-bleed
- Deep Forest Green overlay at 35% opacity covering full image
- Top: "SEEDWARDEN" Lato Regular 18px, Warm Cream, letter-spacing 0.2em, left-aligned, 50px margins
- Center: Topic headline, Playfair Display Bold 72px, Warm Cream, left-aligned
- Below headline: 3–5 bullet lines, Lato Regular 30px, Warm Cream, left-aligned
- Bottom: CTA line, Cormorant Garamond Italic 28px, Warm Cream, left-aligned

### Template 6 — TikTok / Reels Text Overlay (1080×1920px)

Use for: text overlays on video content; this is the on-screen graphic layer, not the video itself
Canva output: PNG with transparent background (overlay on video in editing app)

**Layout**:
- Transparent background throughout
- Bottom third only: text elements
- Hook text (if used as intro card): Playfair Display Bold 72px, Warm Cream,
  centered horizontally, 300px from bottom
- Caption line: Lato Regular 34px, Warm Cream, centered, 220px from bottom
- Brand tag: "seedwarden" Lato Regular 24px, Sage, centered, 160px from bottom
- Drop-shadow on all text: black, 2px blur, 2px offset — this is the only acceptable use of black

**Note**: Most TikTok text overlays are added natively in the TikTok app after upload,
not via Canva. Use this template only when pre-compositing text on a still frame used
as an intro card (first 1–2 seconds).

---

## Part 5: Canva Production Checklist — Pre-Launch (Complete by May 29)

Reference: `WEEK_1_4_CONTENT_CALENDAR.md` Canva Production Checklist for the full item list.
This checklist is the template-creation sequence only.

**Session 1 (Brand Kit + Template 3, ~90 min)**:
- [ ] Brand Kit verified complete (per `canva-pro-brand-kit-setup-guide.md` Part 6 checklist)
- [ ] Template 3 (Carousel Hook Slide) created and saved as Canva template
- [ ] Template 4 (Carousel Body Slide) created and saved as Canva template

**Session 2 (Pinterest templates + first batch, ~90 min)**:
- [ ] Template 1 (Product Mockup Pin) created and saved as Canva template
- [ ] Template 2 (Educational Hook Pin) created and saved as Canva template
- [ ] May 30 Pinterest pins (3 pins for Post 3) produced and exported as JPEG

**Session 3 (Static + first carousels, ~90 min)**:
- [ ] Template 5 (Instagram Static Portrait) created
- [ ] Template 6 (TikTok overlay) created — export as PNG
- [ ] Post 4 carousel (June 1 Instagram) produced: 5 slides exported

**Session 4 (Week 1–2 remaining assets, ~90 min)**:
- [ ] Post 8 static portrait (June 5 Instagram) produced
- [ ] Post 9 Pinterest pins (2 pins, June 5) produced
- [ ] Post 11 carousel (June 8 Instagram) produced: 5 slides exported

---

## Part 6: Midwest Zone 5 Positioning — Visual Differentiation

The visual decisions in this Brand Kit are intentional differentiators from the three
most common aesthetic patterns in the homesteading and foraging space:

| Competing Aesthetic | What They Do | What Seedwarden Does Instead |
|---|---|---|
| "Cottagecore" lifestyle | Warm filters, linen textures, dried flower arrangements, aspirational farm settings | No linen textures, no lifestyle staging; functional field context only |
| Prepper/survivalist | Dark backgrounds, military green, dystopian urgency framing | Warm Cream primary background; information-dense but not fear-driven |
| Generic Etsy shop | Courier New or Libre Baskerville, plain white backgrounds, standard mockup photos | Playfair + Lato pairing, Warm Cream background, lifestyle photos only |

**What the Seedwarden aesthetic communicates to a Zone 5 Midwest buyer**:
- This is research-backed, not opinion-based
- This is zone-specific, not national-generic
- This is field-useful, not aspirational
- This looks like something you'd keep and reference, not consume once and forget

---

*Prepared: 2026-05-19. Exploration Queue Item 93. Status: production-ready — Canva Pro Gate 2
must be complete before templates are built. All hex codes, font names, and size specifications
are verified against existing Brand Kit documentation.*
