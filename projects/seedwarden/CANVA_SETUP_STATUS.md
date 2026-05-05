---
title: "Canva Brand Kit and Zone Card Template — Setup Status"
date: 2026-05-05
session: 724
status: specifications-complete — user setup required (30 min Brand Kit, then Canva zone card build)
references:
  - CANVA_ZONE_CARD_DESIGN_GUIDE.md (step-by-step build guide)
  - CANVA_ZONE_CARD_BATCH_WORKFLOW.md (per-zone content tables)
  - CANVA_EXECUTION_PLAYBOOK.md (full Canva implementation guide)
  - ZONE_QUICKSTART_CARD_SPEC.md (design brief)
  - ZONE_CARD_PRODUCTION_TIMELINE.md (week-by-week build schedule)
  - TRACK_B_LAUNCH_STATUS.md Condition 2 (brand colors and fonts confirmed)
---

# Canva Brand Kit and Zone Card Template — Setup Status

**Purpose**: Track the Canva Brand Kit configuration and zone card template build status.
The Brand Kit is a one-time 30-minute setup; it is the prerequisite for all Canva work
(zone cards, Pinterest pins, carousels, banners). Zone card templates are built afterward
following CANVA_ZONE_CARD_DESIGN_GUIDE.md.

**Agent cannot access Canva** — this document records specifications and status for user
execution. All design decisions are resolved below.

---

## Brand Kit Status

**Canva Brand Kit URL**: NOT YET CREATED (fill in after setup)

| Item | Specification | Status |
|---|---|---|
| Brand Kit created in Canva | — | NOT STARTED |
| Brand colors added (6 colors) | See table below | NOT STARTED |
| Brand fonts added (3 fonts) | See table below | NOT STARTED |
| Logo uploaded | seedwarden_logo_1.png from logos/ | NOT STARTED |

---

## Brand Kit Specification

### Colors (paste these hex codes exactly into Canva Brand Kit)

| Color Name | Hex Code | Use |
|---|---|---|
| Deep Forest Green | #143b28 | Primary — headers, zone band accents |
| Deep Ink Green | #1A3A2A | Secondary — body text dark backgrounds |
| Warm Cream | #F5EDD6 | Background — card body, light sections |
| Parchment | #EDE0C4 | Background variant — alternate sections |
| Sage | #8FA882 | Accent — icons, dividers, subtle callouts |
| Burnt Sienna | #A0522D | Accent — hot zone band, highlight elements |

### Zone Band Colors (used only in zone cards — add to Brand Kit palette)

| Zone Group | Hex Code | Zones |
|---|---|---|
| Cool | #3D6B8A | Zones 3 and 4 |
| Temperate | #2D5016 | Zones 5 and 6 |
| Warm | #C9943A | Zones 7 and 8 |
| Hot | #A0522D | Zones 9 and 10 |

### Fonts (all available free in Canva — no upload needed)

| Role | Font Name | Use |
|---|---|---|
| Heading | Playfair Display | Product names, main overlays, card zone number |
| Body | Lato or Source Sans 3 | Secondary text, taglines, body paragraphs |
| Accent | Cormorant Garamond | Label text, subtle overlays, footer credits |

### Logo

File path: `projects/seedwarden/logos/seedwarden_logo_1.png`

Download this file and upload it to Canva Brand Kit via:
Canva > Brand Hub > Brand Kit > Logo > Upload

Upload the PNG version (transparent background preferred). Canva will store it for use
across all templates without re-uploading.

---

## Zone Card Template Build Status

The build sequence and all per-zone content are in `CANVA_ZONE_CARD_BATCH_WORKFLOW.md`.
The step-by-step Canva instructions are in `CANVA_ZONE_CARD_DESIGN_GUIDE.md`.

### Build Order (from CANVA_ZONE_CARD_BATCH_WORKFLOW.md Part 1)

| Build Order | Zone | Zone Band Color | Duplicate From | Status |
|---|---|---|---|---|
| 1 (master template) | Zone 5 | #2D5016 Temperate | Blank US Letter canvas | NOT STARTED |
| 2 | Zone 6 | #2D5016 Temperate | Zone 5 master | NOT STARTED |
| 3 | Zone 3 | #3D6B8A Cool | Zone 5 master | NOT STARTED |
| 4 | Zone 4 | #3D6B8A Cool | Zone 3 | NOT STARTED |
| 5 | Zone 7 | #C9943A Warm | Zone 5 master | NOT STARTED |
| 6 | Zone 8 | #C9943A Warm | Zone 7 | NOT STARTED |
| 7 | Zone 9 | #A0522D Hot | Zone 5 master | NOT STARTED |
| 8 | Zone 10 | #A0522D Hot | Zone 9 | NOT STARTED |

### Time Estimates Per Session

| Session | Work | Time |
|---|---|---|
| Week 0 | Brand Kit setup | 30 min |
| Week 1, Session 1A | Zone 5 master — layout only (header, columns, spotlight band, footer) | 90 min |
| Week 1, Session 1B | Zone 5 master — populate content from batch workflow doc | 60 min |
| Week 1, Session 2A | Zone 6 (duplicate + update content) | 30 min |
| Week 2, Sessions | Zones 3, 4, 7, 8 (35–45 min each) | ~3 hours |
| Week 3, Sessions | Zones 9, 10 + full-set review and PDF export | ~2 hours |
| **Total** | All 8 cards + Brand Kit | **7.5–9 hours across 3 weeks** |

---

## Footer Placeholder Lock (Complete Before Starting Any Card)

Both footer links must be set before building begins. Record them here and use placeholders
during build until the live URLs are available.

| Footer Element | Status | Live URL (fill in when available) |
|---|---|---|
| Left: Etsy Zone Calendar listing link | PENDING — Etsy listing not yet live | |
| Right: Kit landing page sign-up URL | PENDING — Kit account not yet created | |

**During build**: Use `[ETSY-ZONE-CALENDAR-LINK]` and `[KIT-LANDING-PAGE-URL]` in ALL CAPS
with brackets so the placeholders are impossible to miss. Replace before final PDF export.
Never export a final card with bracketed placeholder text visible.

---

## Output Paths

| Output | Path | Status |
|---|---|---|
| Zone card PDFs (8 files) | `projects/seedwarden/assets/zone-cards/zone-[number]-quick-start-card.pdf` | Directory exists; PDFs not yet produced |
| Canva design file (shareable link) | Record below after creation | |

**Canva design link**: _____________________ (fill in after creating the file)

**Canva Brand Kit URL**: _____________________ (fill in after setup)

---

## Other Canva Work — Status Tracking

The Brand Kit also unblocks these other Track B Canva deliverables:

| Deliverable | Specification Document | Status |
|---|---|---|
| 5 Pinterest pin templates | pin-template-specs.md | NOT STARTED — unblocked after Brand Kit |
| Instagram carousel slides (2/week) | phase-2-social-content-calendar-60day.md | NOT STARTED |
| Instagram Story templates | MAY_CONTENT_EXECUTION_PLAN.md | NOT STARTED |
| Etsy shop banner | LIFESTYLE_PHOTOGRAPHY_STRATEGY.md (dimensions: 3360x840px) | NOT STARTED |

The zone cards are the highest-priority Canva build because they are the gating deliverable
for the Kit email funnel. Do not start pin templates or carousel slides until the Zone 5
master template and at least Zones 5 and 6 cards are exported.

---

## Canva Account Notes

**Canva plan required**: Free tier is sufficient for all zone card work. Canva Pro is needed
for premium elements but none are specified in the current zone card design. Do not upgrade
unless a specific needed element is locked behind Pro.

**Canva team vs. individual**: Individual account is sufficient. No team collaboration is
needed.

**Account to use**: Create or use existing Canva account linked to wanka95@gmail.com for
consistency with all other platform accounts.

---

*Prepared: 2026-05-05. All design decisions resolved in this document and referenced specs.
Canva account and Brand Kit not yet created. Zone card PDF output directory:
projects/seedwarden/assets/zone-cards/. Session 724.*
