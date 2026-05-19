---
title: "Canva Template Architecture — Seedwarden Phase 2 Design System"
created: 2026-05-19
session: 1333
status: READY — use this as the pre-production design brief before May 24 Canva session
scope: Zone cards (May 24–25), Pinterest pins (post-launch), Instagram carousels (post-launch)
references:
  - CANVA_ZONE_CARD_DESIGN_GUIDE.md (zone card Canva execution guide)
  - CANVA_ZONE_CARD_BATCH_WORKFLOW.md (zone card content tables)
  - pin-template-specs.md (Pinterest pin template specifications)
  - CANVA_SETUP_STATUS.md (Brand Kit color reference)
  - phase-2-social-content-calendar-60day.md (social content dimensions)
---

# Canva Template Architecture — Seedwarden Phase 2

**Purpose**: This document defines the full Canva template structure for all Seedwarden
Phase 2 design assets: zone cards, Pinterest pins, and Instagram carousels. It answers
"how do the templates fit together?" so the May 24 production session starts with a clear
design system rather than ad hoc decisions.

**Relationship to other documents**: This is the pre-production architecture brief.
`CANVA_ZONE_CARD_DESIGN_GUIDE.md` is the execution guide for zone cards specifically.
`pin-template-specs.md` is the execution guide for Pinterest pins. This document is the
umbrella that explains how all templates relate and what the Brand Kit enables across them.

---

## The Canva File Hierarchy

Seedwarden's Canva workspace should be organized as follows. Create these folders in Canva
before the May 24 production session.

```
Brand Hub
  └── Brand Kit: Seedwarden (10 colors, 3 fonts, logo)

Canva Projects Folder: Seedwarden
  ├── Zone Cards/
  │     └── Seedwarden Zone 5 Quick-Start Card — MASTER
  │         (7 duplicates: Zones 3, 4, 6, 7, 8, 9, 10)
  │
  ├── Pinterest Pins/
  │     ├── Pin Template 1 — Product Mockup MASTER
  │     ├── Pin Template 2 — Educational Hook MASTER
  │     ├── Pin Template 3 — Zone Card Preview MASTER
  │     ├── Pin Template 4 — Values/Story MASTER
  │     └── Pin Template 5 — Carousel Cover MASTER
  │
  └── Instagram/
        ├── Carousel Slide Template — MASTER (1080 × 1080 px)
        └── Story Template — MASTER (1080 × 1920 px)
```

**Why organize this way**: All templates live in named folders. When you need to produce
Week 3 Instagram carousels in June, you open the Carousel Slide MASTER, duplicate it, and
update content — without hunting through an unsorted workspace.

**Build order by priority**:
1. Zone Cards (May 24–25) — gating deliverable for Kit Email 1 and the May 30 launch
2. Pinterest Pins (May 30–June 7) — first week post-launch social output
3. Instagram Carousels (June 1+) — Week 1 post-launch engagement driver

---

## Template 1: Zone Quick-Start Card

**Priority**: HIGHEST — must be complete before May 30 launch

### Dimensions and Canvas

| Property | Value |
|---|---|
| Format | US Letter, portrait |
| Width | 8.5 inches |
| Height | 11 inches |
| Canvas setup in Canva | File > Create a design > Custom size > 8.5 in × 11 in |
| Export format | PDF Print (Canva applies 300 DPI automatically) |

### Layer Structure (top to bottom)

| Layer name | Position | Height | Content |
|---|---|---|---|
| Header | 0–1.5 in from top | 1.5 in | Wordmark (left), "Zone Quick-Start Card" label (right), large zone number (72pt), region name |
| Zone Color Band | 1.5–1.625 in | 0.125 in (12 px) | Full-width solid color bar — the zone's band color |
| Three-Column Body | 1.75–7.75 in | 6 in | Col 1: Frost dates + season; Col 2: Quick-start crops; Col 3: Storage tips |
| Variety Spotlight Band | 7.75–10.3 in | 2.55 in | Parchment background, 3 variety entries |
| Footer | 10.3–11 in | 0.7 in | Etsy link (left) + Kit landing page (right) |

### Column Widths

Usable width after 0.4 in margins each side: 7.7 in

| Column | Width | Percentage |
|---|---|---|
| Column 1 (Frost dates) | 2.7 in | 35% |
| Column 2 (Quick-start crops) | 2.7 in | 35% |
| Column 3 (Storage tips) | 2.3 in | 30% |
| Gap between columns | 0.25 in | — |

### Typography System

| Use | Font | Weight | Size | Color |
|---|---|---|---|---|
| Wordmark | Playfair Display | Regular | 16pt | Deep Forest Green `#143b28` |
| Zone number (dominant) | Playfair Display | Bold | 72pt | Burnt Sienna `#A0522D` |
| Region name | Playfair Display | Italic | 18pt | Deep Forest Green `#143b28` |
| Column headers | Lato | All Caps, tracked | 11pt | Deep Forest Green `#143b28` |
| Body text | Lato | Light | 10pt | Dark Charcoal `#2C2C2C` |
| Variety names | Cormorant Garamond | Italic | 11pt | Deep Forest Green `#143b28` |
| Variety descriptions | Lato | Light | 10pt | Dark Charcoal `#2C2C2C` |
| Footer text | Lato | Light | 8pt | Warm Grey `#7A7060` |

### Color Application Per Zone

The only element that changes color between zones is the 12px Zone Color Band.
All other colors are identical across all 8 cards.

| Zone | Band Color | Hex |
|---|---|---|
| 3, 4 | Cool | `#3D6B8A` |
| 5, 6 | Temperate | `#2D5016` |
| 7, 8 | Warm | `#C9943A` |
| 9, 10 | Hot | `#A0522D` |

### Build Strategy

Build one master (Zone 5), then duplicate 7 times. Only zone-specific elements change per
duplicate (zone number, band color, region name, all body text). Layout, fonts, and colors
remain locked from the master.

**Build order** (prevents zone-band color errors):
5 (master) → 6 → 3 → 4 → 7 → 8 → 9 → 10

**Full execution guide**: `CANVA_ZONE_CARD_DESIGN_GUIDE.md`
**All text content copy-paste ready**: `CANVA_ZONE_CARD_BATCH_WORKFLOW.md`

---

## Template 2: Pinterest Pin Templates

**Priority**: HIGH — needed for May 30 launch day posts and Week 1 social output
**When to build**: After zone cards are exported (May 25–26 or early June)

### Dimensions

| Property | Value |
|---|---|
| Width | 1000 px |
| Height | 1500 px |
| Aspect ratio | 2:3 (Pinterest native optimal) |
| Canvas setup in Canva | File > Create a design > Custom size > 1000 × 1500 px |
| Export format | PNG (not PDF; Pinterest requires image format) |

### Five Pin Templates

Each template is a separate Canva master file. Build all 5 before launching.
All share the same Brand Kit colors and typography system.

#### Pin Template 1 — Product Mockup Pin

**Purpose**: Drive direct Etsy product discovery. Commercial intent.

| Zone | Content |
|---|---|
| Top 60% | Product mockup image (tablet or phone mockup from `/projects/seedwarden/marketing/mockups/`) |
| Bottom 40% | Deep Forest Green `#143b28` background; product name (Playfair Display 28pt Warm Cream); one-sentence descriptor (Lato 14pt Warm Cream); price or CTA (Cormorant Garamond italic 16pt Sage) |
| Seedwarden wordmark | Bottom-right corner, Lato 10pt, Warm Cream, all caps |

**Layers in Canva**:
1. Background: solid Deep Forest Green `#143b28`
2. Image placeholder element (top 60%) — swap product mockup per pin
3. Gradient overlay at image-text boundary (Deep Forest Green, 80% opacity, 40px height) — optional, use if image colors clash with text
4. Product name text box
5. Descriptor text box
6. CTA text box
7. Wordmark text box (locked element — do not move between pins)

#### Pin Template 2 — Educational Hook Pin

**Purpose**: Discovery via informational search. Non-commercial, builds trust.

| Zone | Content |
|---|---|
| Full background | Warm Cream `#F5EDD6` |
| Top accent bar | Zone-specific band color (12px height, full width) OR Sage `#8FA882` for non-zone content |
| Hook headline | Playfair Display Bold 36pt, Deep Forest Green — provocative question or "X things about [topic]" |
| Subhead | Lato Regular 16pt, Deep Ink Green — 1 sentence expanding the hook |
| Icon or botanical illustration | Centered, line-style, 120×120 px, Sage color |
| Seedwarden wordmark | Bottom-left, Lato 10pt All Caps, Deep Forest Green |

**Content variety for educational pins**:
- "The 3 crops that store the longest in Zone 5"
- "What foragers call 'poverty vegetables' (and why you should know them)"
- "How to tell chickweed from toxic lookalikes"
- "Last frost dates: Zone 3 vs Zone 9 side by side"

Full hook library: `SOCIAL_ACCOUNT_ARCHITECTURE.md` and `WEEK_1_4_CONTENT_CALENDAR.md`

#### Pin Template 3 — Zone Card Preview Pin

**Purpose**: Drive signups to the Kit landing page. Lead magnet promotion.

| Zone | Content |
|---|---|
| Top 65% | Cropped screenshot of a zone card (the header block + column headers, not full text) |
| Bottom 35% | Parchment `#EDE0C4` background |
| Headline | Playfair Display Bold 26pt, Deep Forest Green: "Your Free [Zone X] Quick-Start Card" |
| CTA | Lato Regular 14pt: "Get yours free — link in bio" |
| Band color accent | 4px left border in zone band color |

**One pin per zone**: Build 8 variants of this template (one per zone). The crop of the
zone card image changes per pin; all other elements are identical.

#### Pin Template 4 — Values / Story Pin

**Purpose**: Brand identity and community building. No hard CTA.

| Zone | Content |
|---|---|
| Full background | Deep Forest Green `#143b28` |
| Quote or statement | Playfair Display Italic 32pt, Warm Cream — 1–2 sentences max |
| Seedwarden wordmark | Bottom-center, Lato 10pt All Caps, Sage `#8FA882` |

**Content examples**:
- "Food sovereignty starts with knowing what grows where you live."
- "The most resilient seed is the one your grandmother saved."
- "Heirloom varieties are not nostalgia. They are insurance."

#### Pin Template 5 — Carousel Cover

**Purpose**: Drives saves and click-through on multi-image Pinterest carousel pins.

| Zone | Content |
|---|---|
| Background | Product mockup or landscape (depending on topic) |
| Overlay | Warm Cream gradient from bottom 40%, 70% opacity |
| Number badge | "5 things" / "3 mistakes" badge: circle, Deep Forest Green background, Playfair Display Bold 24pt white number + Lato 10pt white text |
| Title | Playfair Display Bold 30pt, Deep Forest Green |
| Subhead | Lato Regular 14pt, Deep Ink Green |

---

## Template 3: Instagram Carousel Slides

**Priority**: MEDIUM — needed for Week 1 post-launch but not required for launch day
**When to build**: June 1–3 (after zone cards and pins are live)

### Dimensions

| Property | Value |
|---|---|
| Width | 1080 px |
| Height | 1080 px |
| Aspect ratio | 1:1 (square — Instagram native optimal for carousels) |
| Canvas setup in Canva | File > Create a design > Post > Instagram Post (1080 × 1080) |
| Export format | PNG (separate file per slide) |

### Carousel Slide Architecture

Each carousel has a consistent structure:

**Slide 1 (Cover)**:
- Bold hook headline (Playfair Display Bold 42pt, Deep Forest Green)
- Subheadline (Lato Regular 18pt, Deep Ink Green)
- Seedwarden wordmark (bottom-right, small)
- Background: Warm Cream OR product image with overlay
- Swipe prompt: Cormorant Garamond italic 14pt, Sage — "Swipe to see all 5 →"

**Slides 2–N (Content slides)**:
- Consistent header band (Deep Forest Green, 60px height, full width)
- Slide number: Lato Bold 14pt Warm Cream in header band, right side ("2 of 5")
- Main content area: Warm Cream background
- Heading: Playfair Display Bold 28pt, Deep Forest Green
- Body: Lato Regular 14pt, Dark Charcoal `#2C2C2C`, line height 1.5
- Icon (if applicable): 60×60 px, line style, Sage color
- Zone band color strip (4px, left side): use the relevant zone band color if content is zone-specific

**Final slide (CTA)**:
- Deep Forest Green full-background
- CTA headline: Playfair Display Bold 32pt, Warm Cream
- CTA action: Lato Regular 16pt, Warm Cream ("Link in bio" or "Get the free zone card")
- Seedwarden wordmark: Lato 12pt All Caps, Sage

### Magic Resize Path (Canva Pro)

With Canva Pro's Magic Resize feature, once the carousel master is built at 1080×1080, you
can generate a 1080×1920 Instagram Story version in one click (File > Resize). The Story
version needs manual adjustment to the text layout (not all elements fit in the taller
canvas without repositioning), but the Brand Kit colors and fonts carry over automatically.

---

## Export Formats Quick Reference

| Asset | Format | Dimensions | Canva export setting |
|---|---|---|---|
| Zone cards | PDF Print | 8.5 × 11 in | Share > Download > PDF Print |
| Zone card preview (social) | PNG | 1080 × 1080 px | Use Magic Resize from zone card (crop header) |
| Pinterest pins | PNG | 1000 × 1500 px | Share > Download > PNG |
| Instagram carousel slide | PNG | 1080 × 1080 px | Share > Download > PNG |
| Instagram Story | PNG | 1080 × 1920 px | Share > Download > PNG |
| Etsy shop banner | PNG or JPG | 3360 × 840 px | Share > Download > PNG |

---

## Brand Kit Usage in Canva — How It Works

When a Brand Kit is configured, every template built in Canva has one-click access to all
Brand Kit assets through the left sidebar "Brand" panel. Specifically:

**Colors**: The Brand panel shows all 10 Seedwarden colors as swatches. Clicking any
element, then clicking a swatch, applies that exact color without typing a hex code.

**Fonts**: When you select a text box and the Brand Kit fonts are configured, Canva
suggests Playfair Display, Lato, and Cormorant Garamond as the first font options.

**Logo**: The logo is accessible directly from the Brand panel and can be dragged onto
any canvas without re-uploading.

**Template application**: If you save any of the above masters as Canva "Brand Templates"
(available on Pro), other designs can use them as starting points. This is the mechanism
for producing the 7 zone card duplicates without building from scratch.

---

## Pre-Production Confirmation (Run Before May 24)

- [ ] Canva workspace has a "Seedwarden" project folder created
- [ ] Sub-folders "Zone Cards", "Pinterest Pins", "Instagram" created within Seedwarden
- [ ] Brand Kit "Seedwarden" is visible in Brand Hub with 10 colors, 3 fonts, logo
- [ ] `pin-template-specs.md` reviewed — confirm all 5 pin template specs are understood
- [ ] `CANVA_ZONE_CARD_BATCH_WORKFLOW.md` open in separate tab — all 8 zones' text confirmed
      present and complete
- [ ] Export folder exists at `projects/seedwarden/assets/zone-cards/` (confirmed from
      prior session audit)

---

*Created: 2026-05-19. Session 1333. This document synthesizes zone card architecture from
CANVA_ZONE_CARD_DESIGN_GUIDE.md and CANVA_ZONE_CARDS_PRODUCTION_PLAN.md, Pinterest pin
architecture from pin-template-specs.md, and Brand Kit configuration from
CANVA_SETUP_STATUS.md. It is an architecture brief only — execution is handled by the
per-template reference documents listed in each section.*
