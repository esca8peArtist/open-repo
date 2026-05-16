# Systems Resilience — Master Plan

> **Purpose**: Build a practical, actionable knowledge base for when current societal systems fail.
> **Region**: Midwest US (Zone 5, 4 seasons, cold winters, hot summers, variable precipitation)
> **Tracks**: Rural land owner + Suburban homeowner (parallel, with cross-track support notes)
> **Scale**: Individual → Household → Community

---

## Foundation Principles

Every document in this project must meet four standards:

1. **Specific, not conceptual** — exact quantities, measurements, and calculations. Not "plant root vegetables" but "plant 400 sq ft of potatoes to yield ~400 lbs, covering ~20% of a 2,000 calorie/day diet for one adult for a year."

2. **Actionable without infrastructure** — instructions must work when stores are closed, internet is down, professionals are unavailable. Primary sources linked wherever possible.

3. **Progressive disclosure** — each document opens with Day 1-3 (survive), then Week 1-4 (stabilize), then Month 1-6 (build systems), then Year 1+ (self-sufficiency).

4. **Primary sources cited** — link or excerpt real schematics, plans, books, and field guides. Not original text where an authoritative source already exists.

---

## Directory Structure

```
systems-resilience/
├── PLAN.md                     ← this file
├── README.md                   ← project overview + how to use
│
├── individual/                 ← solo competency (one adult)
│   ├── 01-water.md             ← surface → filter → store → drill → pump
│   ├── 02-food.md              ← 1-person 1-year garden + hunting + foraging
│   ├── 03-shelter.md           ← immediate → hardened → tornado-safe
│   ├── 04-energy.md            ← minimal solo power needs
│   ├── 05-healthcare.md        ← without professional support
│   └── 06-education.md         ← self-directed learning when institutions fail
│
├── household/                  ← 2–6 person household
│   ├── 01-water.md
│   ├── 02-food.md
│   ├── 03-shelter.md
│   ├── 04-energy.md
│   ├── 05-healthcare.md
│   └── 06-education.md
│
├── community/                  ← 20–100 person neighborhood/community
│   ├── 01-water.md
│   ├── 02-food.md
│   ├── 03-shelter.md
│   ├── 04-energy.md
│   ├── 05-healthcare.md
│   └── 06-education.md
│
├── tracks/
│   ├── rural.md                ← rural-specific constraints + opportunities
│   └── suburban.md             ← suburban-specific constraints + opportunities
│
├── midwest/
│   ├── calendar.md             ← annual timing for all activities (Zone 5)
│   ├── extreme-weather.md      ← tornado / derecho / ice storm / polar vortex
│   └── foraging-species.md     ← Midwest wild edibles + medicinal plants
│
└── sources/
    ├── books.md                ← annotated book list with where to find free PDFs
    ├── online-resources.md     ← YouTube channels, websites, free guides
    └── schematics.md           ← DIY plans: pumps, wells, solar, shelter
```

---

## Execution Priority

Prioritized by immediacy of need in a failure scenario (Rule of 3: 3 minutes without air, 3 hours without shelter in Midwest winter, 3 days without water, 3 weeks without food):

| Priority | Document | Status | Rationale |
|---|---|---|---|
| 1 | `individual/01-water.md` | ⬜ Not started | Water kills in 3 days; no existing suburban track |
| 2 | `individual/02-food.md` | ⬜ Not started | Planting is seasonal; must know plan before growing season |
| 3 | `midwest/calendar.md` | ⬜ Not started | Required reference for both water and food |
| 4 | `individual/03-shelter.md` | ⬜ Not started | Midwest winter + tornado risk; suburban retrofit missing |
| 5 | `midwest/extreme-weather.md` | ⬜ Not started | Tornado/derecho/ice storm/polar vortex protocols |
| 6 | `individual/05-healthcare.md` | ⬜ Not started | Add to strong existing base (08-medical-health.md) |
| 7 | `individual/04-energy.md` | ⬜ Not started | Solo power needs; suburban grid-tied backup |
| 8 | `midwest/foraging-species.md` | ⬜ Not started | Supplements food; pull from seedwarden |
| 9 | `individual/06-education.md` | ⬜ Not started | Entirely new domain — no existing content |
| 10 | `sources/books.md` | ⬜ Not started | Reference foundation for all documents |
| 11 | `sources/schematics.md` | ⬜ Not started | Hand pumps, wells, solar, shelter builds |
| 12 | `tracks/suburban.md` | ⬜ Not started | Cross-cutting suburban track |
| 13 | `tracks/rural.md` | ⬜ Not started | Cross-cutting rural track |
| 14–19 | `household/*` | ⬜ Not started | Scale up after individual docs complete |
| 20–25 | `community/*` | ⬜ Not started | Scale up after household docs complete |

---

## Content Standard Per Document

Each domain document must include:

### Structure
```
# [Domain] — Individual Scale
## Quick Reference Card (printable, single page equivalent)
## Day 1–3: Immediate Survival
## Week 1–4: Stabilization
## Month 1–6: Building Systems
## Year 1+: Self-Sufficiency
## Rural Track Variations
## Suburban Track Variations
## Midwest-Specific Notes
## Calculations & Sizing
## Equipment & Materials List
## Step-by-Step Procedures
## Primary Sources & Schematics
## Cross-References
```

### Quality Bar
- **Quantities**: every recommendation includes amount (lbs, gallons, sq ft, watts, BTU)
- **Costs**: current estimated costs where relevant
- **Sources**: at least 3 primary sources (books, schematics, or established guides) per major procedure
- **Skills required**: listed explicitly so reader can prepare in advance
- **Tools required**: listed with alternatives for when unavailable
- **Time required**: estimate for each major step

---

## Source Integration Plan

### Pull directly from off-grid-living (do not rewrite, cross-reference)
| Source File | Use In |
|---|---|
| `03-water.md` | `individual/01-water.md` — supplement with suburban + schematics |
| `04-food-production.md` | `individual/02-food.md` — extract 1-person plan, add hunting |
| `05-food-preservation.md` | `individual/02-food.md` — append preservation calendar |
| `06-energy-power.md` | `individual/04-energy.md` — extract solo sizing |
| `07-heating-cooling.md` | `individual/03-shelter.md` — Zone 5 heating section |
| `08-medical-health.md` | `individual/05-healthcare.md` — reuse supply lists |
| `15-disaster-scenarios.md` | `midwest/extreme-weather.md` — extract and deepen Midwest entries |
| `16-skills-knowledge.md` | `individual/06-education.md` — reuse adult learning framework |

### Pull directly from seedwarden
| Source File | Use In |
|---|---|
| `hunting-fishing-trapping-field-manual.md` | `individual/02-food.md` |
| `survival-garden-regional-plans.md` | `individual/02-food.md` |
| `native-plants-regional-guide.md` | `midwest/foraging-species.md` |
| `seed-saving-field-manual.md` | `individual/02-food.md` |
| `meat-fish-preservation-field-manual.md` | `individual/02-food.md` |
| `harvest-preservation-field-manual.md` | `individual/02-food.md` |
| `apartment-growing-complete-guide.md` | `tracks/suburban.md` + `household/02-food.md` |
| `container-growing-blueprint-pack.md` | `tracks/suburban.md` |
| `12-month-urban-growing-planner.md` | `midwest/calendar.md` |
| `small-scale-livestock-field-manual.md` | `household/02-food.md` |
| `medicinal-herbs-candidate-list.md` | `individual/05-healthcare.md` |
| `phase-3-medicinal-herbs-content-outline.md` | `individual/05-healthcare.md` |

### New research needed (agent web research sessions)
| Topic | For Document |
|---|---|
| Hand pump construction schematics (Simple Pump, PVC pitcher pump, cylinder pump) | `individual/01-water.md` + `sources/schematics.md` |
| Well drilling — hand methods (jetting, cable tool, hand auger) + when to hire | `individual/01-water.md` |
| Midwest whitetail deer biology + hunting basics for non-hunters | `individual/02-food.md` |
| Midwest fishing species + seasonal patterns (catfish, bass, bluegill, walleye) | `individual/02-food.md` |
| Torpedo safe room construction — FEMA P-320 / ICC-500 specs | `individual/03-shelter.md` + `midwest/extreme-weather.md` |
| Suburban basement hardening for tornado | `tracks/suburban.md` |
| Passive solar design for Midwest (Zone 5 overhang angles, mass wall sizing) | `individual/03-shelter.md` |
| Grid-tied solar + battery backup for suburban homes (transfer switch, sizing) | `individual/04-energy.md` |
| Cold-climate heat pumps for Midwest (Mitsubishi Hyper Heat, Bosch IDS) | `individual/03-shelter.md` |
| Midwinter cold-snap survival: propane backup, freeze protection | `midwest/extreme-weather.md` |
| Homeschool curriculum resources (Khan Academy offline, printer-ready curricula) | `individual/06-education.md` |
| Offline knowledge infrastructure (Kiwix, Raspberry Pi library servers) | `individual/06-education.md` |
| Free/open-source medical references for non-professionals | `individual/05-healthcare.md` |
| Root cellar construction: concrete block, buried barrel, hillside variants | `individual/02-food.md` |
| Fermentation without modern equipment | `individual/02-food.md` |
| 1-acre garden caloric plan (Zone 5 specific) | `individual/02-food.md` |

---

## Document Template

Use this template for every new document in `individual/`, `household/`, and `community/`:

```markdown
# [Domain] — [Scale] Scale
> **Region**: Midwest US (Zone 5) | **Tracks**: Rural + Suburban
> **Cross-references**: [links to relevant off-grid-living docs]

## Quick Reference Card
<!-- Printable single-page summary: most critical actions, quantities, contacts -->

---

## Day 1–3: Immediate Survival
<!-- What to do right now with what you have. No shopping, no preparation assumed. -->

## Week 1–4: Stabilization
<!-- Getting from crisis to stable. May require some supplies or short trips. -->

## Month 1–6: Building Systems
<!-- Infrastructure investment. Requires planning, budget, physical labor. -->

## Year 1+: Self-Sufficiency
<!-- Full system operation. Maintenance mode. Community integration. -->

---

## Rural Track
<!-- Variations and additional opportunities for rural land owners -->

## Suburban Track
<!-- Variations and constraints for suburban homeowners -->

---

## Midwest Notes
<!-- Zone 5 specifics: timing, weather events, regional species, soil -->

---

## Calculations & Sizing Guide
<!-- All the math: quantities, system sizing, yield estimates -->

## Equipment & Materials List
<!-- Specific items, model numbers where relevant, alternatives -->

## Step-by-Step Procedures
<!-- Numbered steps a non-expert can follow -->

## Primary Sources
<!-- Books, schematics, guides, YouTube channels — with annotations -->
```

---

## Execution Log

| Date | Document | Agent | Status |
|---|---|---|---|
| 2026-05-16 | PLAN.md | orchestrator | ✅ Complete |
| 2026-05-16 | individual/01-water.md | orchestrator + research | ✅ Complete |
| 2026-05-16 | individual/02-food.md | orchestrator + research | ✅ Complete |
| 2026-05-16 | sources/books.md | research agents | ✅ Complete |
| 2026-05-16 | sources/online-resources.md | research agents | ✅ Complete |
| 2026-05-16 | individual/03-shelter.md | orchestrator + research | ✅ Complete |
| 2026-05-16 | midwest/extreme-weather.md | orchestrator + research | ✅ Complete |
