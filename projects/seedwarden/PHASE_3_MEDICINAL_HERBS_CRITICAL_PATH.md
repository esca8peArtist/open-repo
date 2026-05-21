---
title: "Phase 3 Medicinal Herbs — Critical Path Analysis & Production Timeline"
date: 2026-05-21
version: 5.0
status: production-ready
phase: Phase 3 pre-execution
decision-deadline: May 30, 2026
execution-window: June 22 – July 13, 2026 (22 calendar days)
gate-status:
  forager-cohort: CLEARED (21.3%, gate >20%)
  native-plants-conversion: CLEARED (2.24%, gate >1.5%)
word-count: 4,800+
supersedes: v4.0 (2026-05-20)
companion-csv: phase-3-timeline.csv
cross-references:
  - phase-3-medicinal-herbs-gantt-timeline.csv
  - phase-3-medicinal-herbs-sourcing-guide.md
  - phase-3-medicinal-herbs-content-outline.md
  - HERBALIST_PRACTITIONER_ECOSYSTEM.md
  - HERBALIST_NETWORK_ECOSYSTEM_MAPPING.md
  - TRACK_B_FINAL_EXECUTION_GUIDE.md
  - PHASE_3_PRODUCTION_GANTT.csv
tags: [seedwarden, phase-3, critical-path, production-timeline, medicinal-herbs, decision-support]
---

# Phase 3 Medicinal Herbs — Critical Path Analysis & Production Timeline

**Version**: 5.0
**Prepared**: May 21, 2026
**Decision deadline**: May 30, 2026 (Track B launches; Phase 3 June supply-chain orders must be authorized)
**Execution window**: June 22 – July 13, 2026 (22 calendar days)
**Launch gates**: BOTH CLEARED — forager cohort 21.3% (gate >20%), native plants conversion 2.24% (gate >1.5%)
**Companion spreadsheet**: `phase-3-timeline.csv` (milestone-level; start date, duration, resource, dependencies, float days, gate dates)

---

## Executive Summary

Phase 3 is authorized. Both demand-validation gates are cleared with margin before Phase 2 launches May 30. The June 22–July 13 sprint is feasible for a single writer producing all five bundles at 4–5 focused hours per day. The recommended scope is three bundles (Women's Health + Respiratory + Sleep), which keeps the critical path at 36–44 adjusted writing hours and carries 2 structural float days.

The binding constraint is writing. At 56–66 adjusted hours for all five bundles, the critical path runs through writing alone: Women's Health complete June 28 → upload June 29 → Respiratory upload July 6–7 → Sleep upload July 13. Design (14 hours total) and photography (parallel pre-sprint track, 18 hours total) carry 3–14 days of float on every task and do not threaten any launch date under the recommended scope.

**Supplier orders for June delivery must be placed before May 30 for two species** (Black Cohosh has a 5–6 week lead time; a May 25 order yields a June 21–28 arrival within sprint Week 1). All other sourcing deadlines fall in June and require no action today.

**Three decisions are required by May 30** and are flagged `[DECISION]` throughout this document:

1. **Sprint scope** — Option A (all 5 bundles, single writer, 5 hrs/day Weeks 1–2), Option B (split between two writers), or Option C (3-bundle priority: Women's Health + Respiratory + Sleep — recommended).
2. **Goldenseal path** — Order live specimen from Prairie Moon or Strictly Medicinal by June 8, or confirm Wikimedia CC photo path. One path must be logged in WORKLOG.md by June 8.
3. **Canva palette** — Confirm the six hex codes in Section 4 by June 15 or they lock automatically.

Under Option C (recommended), Immunity and Digestive defer to July 20 and August 3 respectively. The 90-day revenue difference versus Option A closes entirely by September. The practitioner 10-bundle tier ($120–$150) unlocks July 13 when Sleep goes live, meeting the minimum 3-bundle clinical library threshold.

---

## Section 0: Critical Path Map and Float Summary

This section is the single-reference summary for the production critical path. All supporting detail is in Sections 1–8. The companion spreadsheet `phase-3-timeline.csv` contains the full milestone table with start dates, durations, resources, predecessors, float days, and gate dates.

### Critical Path Sequence (Zero-Float Activities Only)

```
[May 30]  DECISIONS: Sprint scope + Goldenseal path + Palette (user)
     |
[June 1]  Black Cohosh order placed — Strictly Medicinal (5–6 wk lead)
     |
[June 8]  HARD DEADLINE: Goldenseal order placed OR CC path confirmed
     |
[June 15] HARD DEADLINE: Elderberry order + Mountain Rose Herbs dried herbs + Palette decision
     |
[June 21] Attribution log complete + Canva brand kit loaded
     |
[June 22] SPRINT D1: Women's Health writing begins (700 words — Black Cohosh)
     |
[June 24] PACE GATE: WH must be at 2,500 words EOD — if not, activate Option C immediately
     |
[June 28] Women's Health PDF export QA complete (3,800 words)
     |
[June 29] UPLOAD: Women's Health ($22) — MILESTONE 1
     |
[July 2]  Immunity writing complete (Goldenseal cultivation + CITES sidebar)
     |
[July 3]  DESIGN LOCK: Digestive cover finalized — no cover changes after EOD
     |
[July 5]  Sleep writing complete (3,500 words)
     |
[July 6]  UPLOAD: Respiratory ($20) — MILESTONE 2
     |
[July 11] Digestive writing complete (3,600 words) + all 5 PDFs export-ready
     |
[July 12] FLOAT DAY 1 (8 hrs — absorbs Week 3 overrun)
     |
[July 13] UPLOAD: Sleep ($20) — MILESTONE 3 / Sprint close
     |
[July 15] Practitioner tier live ($120–$150, 3-bundle minimum met)
     |
[July 20] UPLOAD: Immunity ($22) — post-sprint
     |
[Aug  3]  UPLOAD: Digestive ($20) — full 5-bundle launch complete
```

### Float Summary by Track

| Track | Total Hours | Critical-Path Hours | Float Hours | Float Days |
|---|---|---|---|---|
| Writing | 56–66 adj. hrs | 56–66 hrs | 8 hrs (2 float days) | 2 days |
| Design | 14.0 hrs | 0 hrs (fully parallel) | 3–14 days per task | 3–14 days |
| Photography | 18.0 hrs (pre-sprint) | 0 hrs (pre-sprint only) | 5–14 days per activity | 5–14 days |
| Supplier — Tier 1 | 2 orders | 0 (float = 0 if writing-only path) | 0 days if Path 1; infinite if Path 2 | 0 or infinite |
| Supplier — Tier 2 | 2 orders | 0 (quality only) | 5 days (MRH); 7 days (Elderberry) | 5–7 days |

**Critical path diagnosis**: Writing is the only binding constraint. Design and photography are fully parallel and carry enough float to absorb any single-bundle overrun without threatening an upload date. Photography is not a launch blocker — all 14 unique species have verified Wikimedia Commons CC-BY-SA or iNaturalist CC-BY coverage. The two Tier 1 supplier orders (Black Cohosh and Goldenseal) affect photography quality in v1.1, not launch dates for v1.0.

### May 30 Gate — Decisions Required Before June 1 Supplier Orders

The following three decisions must be logged in WORKLOG.md by May 30 to enable June 1 supplier contact and June 8 order placement:

| Decision | Options | Recommendation | Consequence if Deferred |
|---|---|---|---|
| Sprint scope | A (5 bundles) / B (2 writers) / C (3 bundles) | C | Cannot brief second writer by June 1 deadline (Option B only) |
| Goldenseal path | Path 1 (order June 8) / Path 2 (Wikimedia CC) | Path 2 under Option C | Immunity photography plan unresolved entering sprint |
| Canva palette | Confirm 6 hex codes / accept auto-lock June 15 | Accept auto-lock if no strong preference | No consequence — auto-lock is production-ready |

---

## Section 1: Medicinal Herb Selection — Finalized Species Map

All five bundles are production-locked. No further species selection decisions are required.

| Bundle | Species (5 per bundle) | SKU | Price | Upload Target |
|---|---|---|---|---|
| Women's Health | Black Cohosh, Vitex, Red Clover, Calendula, Lavender | MH-BUNDLE-WH-001 | $22 | June 29 |
| Respiratory Health | Elderberry, Mullein, Echinacea purpurea, Echinacea angustifolia, Thyme | MH-BUNDLE-RH-001 | $20 | July 6–7 |
| Sleep and Nervines | Valerian, Passionflower, Lemon Balm, Lavender | MH-BUNDLE-SN-001 | $20 | July 13 |
| Immunity Support | Echinacea, Ashwagandha, Elderberry, Goldenseal | MH-BUNDLE-IM-001 | $22 | July 20 |
| Digestive Support | Dandelion, Calendula, Lemon Balm, Ginger | MH-BUNDLE-DS-001 | $20 | August 3 |
| **Total** | **21 species slots — 14 unique; 7 appear in 2 bundles** | — | $21 avg | — |

**Shared-species efficiency**: Echinacea, Elderberry, Calendula, Lavender, and Lemon Balm each appear in two bundles. Second-occurrence writing requires approximately 40% of first-occurrence effort (reframing the cultivation and identification content to the new bundle angle rather than full redrafting). This reduces adjusted writing hours from 64–74 raw to 56–66.

**Upload sequence rationale**: Women's Health first — Black Cohosh is uncontested at Etsy Tier 3 keyword with high practitioner intent. Respiratory second — cold and flu research intent builds July–August as buyers prepare for autumn. Sleep third — the July burnout-resolution peak is a real seasonal signal. Immunity fourth, allowing review accumulation before the November–December cold/flu peak. Digestive last, positioned for the autumn gut-health intent window and synchronized with the Dandelion cross-sell email trigger to Phase 2 wild-edibles forager cohort buyers.

---

## Section 2: Supplier Sourcing Timeline

Physical specimens are supplementary to production quality. All 14 unique species have verified Wikimedia Commons CC-BY-SA or iNaturalist CC-BY photo coverage sufficient for launch quality (documented in `phase-3-medicinal-herbs-sourcing-guide.md`). Live plants improve photography for v1.1 but do not gate writing or design.

### Tier 1 — Hard Deadline June 8 (5–6 week lead time; ZERO float)

These are the two conservation-significant species with the longest lead times and the most limited cultivated stock. An order placed after June 8 arrives after the July 13 sprint end.

| Species | Bundle | Primary Supplier | Lead Time | Cost | Fallback Path | Complexity Note |
|---|---|---|---|---|---|---|
| Goldenseal (*Hydrastis canadensis*) | Immunity | Prairie Moon Nursery — rhizome division; prairiemoon.com; 866-417-8156 | 5–6 weeks | $15–22 | Strictly Medicinal Seeds ($12–18); then Wikimedia CC-BY-SA via media@ncbg.unc.edu + media@mobot.org | CITES Appendix II. Mandatory cultivation-only framing. FGV sourcing documentation required in guide body. Berberine active-constituent framing required. |
| Black Cohosh (*Actaea racemosa*) | Women's Health | Strictly Medicinal Seeds — 2-year seedling; strictlymedicinalseeds.com | 5–6 weeks (ordered May 25 = June 21–28 arrival) | $10–15 | Prairie Moon Nursery ($12–18); then iNaturalist CC-BY (Appalachian range, abundant June–August) | UpS At-Risk. 150-word conservation sidebar mandatory. Cherokee traditional-use framing requires accuracy review in peer review window. |

`[DECISION 1 — Goldenseal]` Declare by May 30, order by June 8 if Path 1:
- Path 1: Order from Prairie Moon or Strictly Medicinal by June 8. Plant arrives July 13–20 for v1.1 photography. No writing impact. Recommended only if Option A or B chosen for sprint scope.
- Path 2 (recommended under Option C): Confirm Wikimedia CC path now. Email media@ncbg.unc.edu and media@mobot.org by June 7. Zero cost, zero schedule risk. Under Option C, Immunity launches July 20 — Path 2 is fully sufficient for launch-quality guide.

**June 8 hard sign-off**: Log in WORKLOG.md. If Path 1: record supplier, order confirmation, expected arrival. If Path 2: confirm three Goldenseal Wikimedia CC-BY-SA image filenames in PHOTO_ATTRIBUTION_LOG.md.

### Tier 2 — Deadline June 15 (4-week lead time)

| Species | Bundle | Primary Supplier | Lead Time | Cost | Fallback | Expected Arrival |
|---|---|---|---|---|---|---|
| Elderberry (*Sambucus nigra*) | Respiratory + Immunity | Prairie Moon — bare-root; info@prairiemoon.com | 4 weeks | $15–25 | Local nursery — potted 2-gal, 1–2 weeks (order June 22 if Prairie Moon OOS) | ~July 13–20 |
| Dried herbs — 13 species, 1 oz each | All 5 bundles | Mountain Rose Herbs — wholesale@mountainroseherbs.com | 3–5 business days | $93–141 total | Frontier Co-op — 3–5 day ship, comparable species coverage | June 17–18 if ordered June 15 |

Mountain Rose Herbs is the single highest-impact supplier action for photography quality. The dried herb studio session (June 17–21) produces flat-lay content for all five bundle Etsy listing images. Request a Certificate of Analysis for Goldenseal root confirming cultivated origin when placing this order.

### Tier 3 — Deadline June 22 (2–3 week lead time; order sprint start day)

| Species | Bundle | Primary Supplier | Fallback Photo |
|---|---|---|---|
| Echinacea purpurea | Respiratory, Immunity | Prairie Moon or Strictly Medicinal | Wikimedia CC-BY-SA — abundant |
| Echinacea angustifolia | Respiratory, Immunity | Strictly Medicinal Seeds | iNaturalist CC-BY — Kansas, Nebraska, South Dakota prairie range |
| Ashwagandha | Immunity | Strictly Medicinal Seeds | iNaturalist CC-BY — Southern US cultivation zones |
| Passionflower (*Passiflora incarnata*) | Sleep | Prairie Moon | iNaturalist CC-BY — SE US, exceptional visual quality |
| Valerian (*Valeriana officinalis*) | Sleep | Prairie Moon or Strictly Medicinal | iNaturalist CC-BY — NE US and Pacific NW |
| Ginger (*Zingiber officinale*) | Digestive | Strictly Medicinal Seeds or grocery store | Grocery rhizome valid for studio photography |
| Vitex (*V. agnus-castus*) | Women's Health | Local nursery (landscape shrub) | Wikimedia CC-BY-SA — widely cultivated |

**Photo-only species (no specimen order required)**: Red Clover, Mullein, Thyme, Lemon Balm, Lavender, Calendula, Dandelion. All have exceptional Wikimedia Commons CC-BY-SA coverage. Dandelion photos already exist in the Seedwarden wild-edibles archive (`assets/wild-edibles/`).

**Budget summary by tier**:

| Tier | Items | Low | High |
|---|---|---|---|
| Tier 1 — Path 1 only | Goldenseal + Black Cohosh | $22 | $37 |
| Tier 2 | Elderberry + Mountain Rose Herbs dried herbs | $108 | $166 |
| Tier 3 | Echinacea, Ashwagandha, Passionflower, Valerian, Ginger, Vitex | $65 | $105 |
| Studio props | Kraft paper, mortar/pestle, glass jars, linen, tray | $60 | $100 |
| **Total (Path 1)** | | **$255** | **$408** |
| **Total (Path 2 — Wikimedia CC for Goldenseal)** | | **$233** | **$371** |

**Supplier backup reference**:

| Primary Fails | Species | Backup 1 | Backup 2 |
|---|---|---|---|
| Prairie Moon | Goldenseal | Strictly Medicinal Seeds | NC Botanical Garden photo license (free, email media@ncbg.unc.edu) |
| Strictly Medicinal | Black Cohosh | Prairie Moon Nursery | iNaturalist CC-BY — Appalachian range |
| Prairie Moon | Elderberry | Local nursery (potted, +$5–15) | Wikimedia CC-BY-SA |
| Mountain Rose Herbs | All dried herbs | Frontier Co-op (3–5 day emergency ship) | Local health food co-op, bulk section |

---

## Section 3: Writing Schedule

### Total Writing Budget

Writing velocity: 300–350 words per hour for research-dense medicinal herb content written from pre-compiled outlines in `phase-3-medicinal-herbs-content-outline.md`. Hour counts include research integration, drafting, contraindication verification, FTC compliance review, and one self-edit pass.

| Bundle | Target Words | Species | Raw Hours | Adjusted Hours (shared-species) | Peer Review |
|---|---|---|---|---|---|
| Women's Health | 3,800 | 5 (0 shared at time of first write) | 14–16 | 14–16 | RH-AHG reviewer — Black Cohosh and Vitex accuracy check |
| Respiratory Health | 3,600 | 5 (0 shared at time of first write) | 12–14 | 12–14 | Optional — Echinacea two-species framing |
| Sleep and Nervines | 3,500 | 4 (1 shared: Lavender) | 12–14 | 11–13 | Pharmacist or ND — sedative drug interaction review |
| Immunity Support | 3,800 | 4 (2 shared: Echinacea, Elderberry) | 14–16 | 10–12 | RH-AHG reviewer — Goldenseal CITES sidebar, Ashwagandha thyroid warning |
| Digestive Support | 3,600 | 4 (2 shared: Calendula, Lemon Balm) | 12–14 | 9–11 | Optional — lowest FTC risk bundle |
| **Total** | **18,300** | **21 slots (14 unique)** | **64–74** | **56–66** | |

### Per-Bundle Writing Dates — Day-by-Day Schedule

**Week 1: June 22–28 — Women's Health + Respiratory begin**

Women's Health leads because it contains the two species with the deepest compliance requirements (Black Cohosh conservation sidebar, Vitex invasive-species note) and the earliest upload target (June 29). Week 1 is the most intensive writing week.

| Day | Date | Task | Word Target | Hours | Float | Critical Path |
|---|---|---|---|---|---|---|
| D1 | June 22 | WH front matter + intro + Black Cohosh (identification, habitat, 150-word conservation sidebar, cultivation, harvest, active constituents, contraindications) | ~700 | 5 | 1 day | YES |
| D2 | June 23 | WH: Vitex (invasive note SE states, berry harvest timing, dopaminergic framing, contraindications) + Red Clover (isoflavone framing, forager-edible crossover, pregnancy caution) | ~1,000 | 5 | 1 day | YES |
| D3 | June 24 | WH: Calendula + Lavender (3-cultivar comparison: Hidcote, Munstead, Phenomenal) + preparation methods + practitioner section + WH self-edit | ~1,100 | 5 | 0 days | YES — WH complete by June 28 for June 29 upload |
| D4 | June 25 | Resp: Front matter + intro + Elderberry (800 words — raw berry toxicity, sambunigrin, elderflower forager crossover) | ~800 | 5 | 1 day | YES |
| D5 | June 26 | Resp: Mullein (biennial lifecycle, first-year rosette vs. second-year spike, ear oil preparation) + Echinacea two-species (600 words — E. purpurea vs. E. angustifolia, UpS At-Risk sidebar) | ~1,100 | 5 | 1 day | YES |
| D6 | June 27 | Resp: Thyme (500 words — thymol framing, pregnancy caution at large doses) + shared sections | ~900 | 4 | 2 days | No |
| D7 | June 28 | Resp self-edit + WH PDF export QA (5MB limit, placeholder scan, attribution confirm, thumbnail crop test at 170×135px) | — | 2 | 2 days | No |

**Pace gate at D3 (June 24 EOD)**: If Women's Health is below 2,500 words at end of Day 3, single-writer 5-bundle Option A is not viable. Activate Option C (3-bundle scope) immediately. The June 29 / July 6–7 / July 13 upload dates remain intact under Option C.

**Week 1 milestone**: Women's Health complete (3,800 words, export-ready by June 28). Respiratory complete (3,600 words). First Etsy upload June 29.

**Peer review — Women's Health (June 22–29)**: Contact one AHG RH practitioner with a Women's Health specialty by June 22. Share a draft of the Black Cohosh section. A written confirmation of botanical and contraindication accuracy is sufficient and becomes a credibility signal in the Etsy listing. Target: response by June 27.

---

**Week 2: June 29–July 5 — Immunity + Sleep**

Week 2 opens with the Women's Health upload (2 hours June 29 morning) and pivots to Immunity. Goldenseal (CITES sidebar + FGV sourcing + berberine framing) and Ashwagandha (900 words — the longest single species section in Phase 3) together account for 1,800 of the 3,800 Immunity words and require the most precision of any content in the entire project.

| Day | Date | Task | Word Target | Hours | Float | Critical Path |
|---|---|---|---|---|---|---|
| D8 | June 29 | WH upload AM (2 hrs) + Imm: intro + Echinacea condensed (immunity framing, 60% of Resp length) | ~600 | 3+2 upload | 1 day | YES |
| D9 | June 30 | Imm: Ashwagandha (900 words — Rasayana context, withanolide RCT framing, cultivation zones 8–12 perennial / 5–7 annual, MANDATORY thyroid + pregnancy warning) | ~900 | 5 | 1 day | YES |
| D10 | July 1 | Imm: Elderberry condensed (fermentation note, immunity framing) + Goldenseal intro + CITES Appendix II sidebar (200 words — MANDATORY) | ~700 | 5 | 1 day | YES |
| D11 | July 2 | Imm: Goldenseal cultivation + FGV sourcing documentation + berberine active constituents + all shared sections + self-edit | ~900 | 5 | 1 day | YES |
| D12 | July 3 | Sleep: Front matter + intro + Valerian (800 words — second-year root harvest, valerenic acid framing, MANDATORY sedative drug interaction warning) | ~800 | 4 | 2 days | No |
| D13 | July 4 | Sleep: Passionflower (700 words — maypop forager crossover, trellis requirements, chrysin/vitexin framing, MANDATORY MAOI interaction note) | ~700 | 4 | 2 days | No |
| D14 | July 5 | Sleep: Lemon Balm condensed (nervine framing, MANDATORY TSH caution) + Lavender condensed (linalool/aromatherapy framing — distinct from WH salve angle) + shared sections + self-edit | ~1,000 | 4 | 2 days | No |

**Week 2 milestone**: Immunity complete (3,800 words). Sleep complete (3,500 words). Respiratory upload July 6–7. Sleep upload staged for July 13.

**Peer review — Immunity (July 1–10)**: Email PHASE_3_HERBALIST_NETWORK_PRESTAGING.md contact list (ND or RH with clinical herbal medicine focus) by July 2 with the Goldenseal CITES sidebar and Ashwagandha thyroid warning sections. Request review by July 10. These two items are the mandatory accuracy-review targets for the Immunity bundle.

---

**Week 3: July 6–13 — Digestive + Final Passes + Uploads**

Digestive benefits from two shared species (Calendula, Lemon Balm) reducing adjusted hours to 9–11. The Dandelion section is the most strategically important content in Phase 3 — the direct cross-sell hook from Phase 2 wild-edibles forager cohort buyers.

| Day | Date | Task | Type | Hours | Float | Critical Path |
|---|---|---|---|---|---|---|
| D15 | July 6 | Resp upload AM (2 hrs) + Digestive: intro + Dandelion (900 words — bitters preparation, wild-edibles cross-sell hook, roasted root coffee substitute, inulin/taraxacin framing) | Write + Upload | 5+2 | 1 day | YES |
| D16 | July 7 | Digestive: Calendula condensed (digestive framing — internal infusion, mucosal healing angle, not topical salve) + Lemon Balm condensed (carminative framing, post-meal gas relief) + shared sections | Write | 4 | 1 day | No |
| D17 | July 8 | Digestive: Ginger (700 words — cultivation zones, grocery rhizome note, gingerol/shogaol framing, nausea RCT evidence) + Digestive self-edit | Write | 4 | 2 days | No |
| D18 | July 9 | FTC compliance review all 5 bundles (priority order: WH Black Cohosh/Vitex → Immunity Goldenseal/Ashwagandha → Sleep sedative interactions → Resp → Digestive) | Review | 3 | 2 days | No |
| D19 | July 10 | SEO optimization pass (Etsy title/tag keyword density) + PDF export all 5 bundles (5MB limit check, no placeholder text, attribution complete) + sources compilation | Admin | 4 | 1 day | No |
| D20 | July 11 | File naming convention confirmation + practitioner variant staging + Etsy listing QA for Sleep + Immunity + Digestive queued bundles | Admin | 2 | 1 day | No |
| D21 | July 12 | FLOAT DAY 1 — absorbs writing overrun from any Week 3 day | Float | 0–4 | — | No |
| D22 | July 13 | Sleep upload live + sprint retrospective + WORKLOG.md update | Upload | 2+2 | 4 hrs | YES |

**Week 3 milestone**: Digestive complete (3,600 words). All 5 PDFs export-ready. Women's Health + Respiratory + Sleep live on Etsy. Immunity and Digestive staged for July 20 and August 3 uploads.

### Revision Buffers

Each bundle has 1.5–2 hours of revision buffer embedded in its writing week. Two structural buffers are available beyond these:

1. **Float Day 1 (July 12)**: 8 hours available for any Week 3 overrun.
2. **Float Day 2 (July 13 afternoon post-upload)**: 4 hours available for corrections to queued listings.

If both float days are consumed, the recovery path is to defer Digestive from August 3 to August 10 — zero revenue impact in the sprint window.

---

## Section 4: Canva Design Timeline

### Design Scope and Hours

Phase 3 design is adaptation work built on Phase 2 templates. No template rebuild is required. Design runs fully parallel to writing — no writing day is blocked by design, and no design task is blocked by writing.

`[DECISION 2 — Palette]` Confirm the six hex codes below by June 15. Any revision after June 23 requires rebuilding completed covers (~1.2 hours per cover reworked).

| Color Name | Hex Code | Bundle Assignment | Use Case |
|---|---|---|---|
| Deep Burgundy | #8B3E3E | Women's Health, Immunity | Primary header background |
| Sage Green | #6B8E6F | Respiratory, Digestive | Primary header background |
| Apothecary Gold | #D4AF37 | All bundles | Accent bar, highlights — premium tier signal |
| Clinical Cream | #F9F5F0 | All bundles | Page background |
| Muted Lavender | #9B8BA0 | Sleep bundle only | Bundle-specific accent |
| Dark Charcoal | #2C2C2C | All bundles | Body text |

**Version note**: `phase-3-canva-mockup-brief.md` (May 9) contains an older 5-color palette with Herb Brown #6B4F35 as primary. The May 20 palette above is the production version. Deep Burgundy (#8B3E3E) replaces Herb Brown for the apothecary/clinical positioning of Phase 3.

**If no palette decision is recorded by June 15**: The six hex codes above lock automatically. No further action required.

| Design Task | Hours | Scheduled Date | Float | Dependency |
|---|---|---|---|---|
| Palette pre-test + 1 zone card export | 0.5 | June 21 | 1 day | Palette confirmed by June 15 |
| Women's Health cover (Black Cohosh or Calendula hero, Deep Burgundy) | 1.2 | June 23 | 4 days | Wikimedia CC hero pre-staged |
| Respiratory cover (Elderberry berry cluster hero, Sage Green) | 1.2 | June 24 | 4 days | Wikimedia CC hero pre-staged |
| Immunity cover (Goldenseal root or Ashwagandha hero, Deep Burgundy) | 1.2 | June 29 | 4 days | Hero photo confirmed |
| Sleep cover (Passionflower flower hero, Muted Lavender) | 1.2 | June 30 | 3 days | iNaturalist CC-BY Passiflora available |
| WH + Resp zone cards | 1.6 | July 1–2 | 4 days | Covers complete |
| Digestive cover (Dandelion root or Ginger hero, Sage Green) | 1.2 | July 3 | 0 days | **DESIGN LOCK — no cover changes after July 3 EOD** |
| Immunity + Sleep + Digestive zone cards | 2.4 | July 6–7 | 2 days | All covers complete |
| Practitioner bundle cover (8.5"×11", Gold/Burgundy premium layout) | 1.5 | July 8 | 5 days | All 5 covers complete |
| Consistency review + export test all 5 covers + zone cards | 0.5 | July 9 | 2 days | All design tasks complete |
| Revision buffer | 1.5 | July 10 | — | — |
| **Total** | **14.0 hrs** | | | |

**Design lock**: July 3 EOD. After this date no cover changes are accepted until after the Sleep upload July 13. Google Docs PDF export is the launch-viable fallback for any single bundle if a Canva template issue is unresolvable on a critical day.

**Branding consistency checks per cover**: (1) hex codes match Brand Kit exactly, (2) Playfair Display Bold on all headers, (3) Latin binomials in Lato Italic. Single consistency-check session July 9 before the PDF export pass July 10.

---

## Section 5: Photography Staging

### Photography Strategy

Indoor studio with north-facing window light plus one reflector is the primary plan for all five bundles. No outdoor location photography is required. This eliminates permit risk, weather dependency, and travel cost.

Most ordered live specimens arrive at or after sprint end (July 12–20). This is expected and planned. Wikimedia Commons CC-BY-SA and iNaturalist CC-BY sources cover 100% of photography needs at launch quality. Live specimens are photographed post-sprint for v1.1 updates.

**Lighting setup**: North-facing window 9am–2pm (consistent diffuse light). 18"×24" white reflector for fill on shadow side. Kraft paper or linen background. No ring light (creates harsh catchlights on botanical specimens). Post-processing warm preset: +0.2 exposure / -20 highlights / +15 shadows. Export at 2400×2400px minimum.

### Fresh vs. Dried vs. Stock Photo Decision Matrix

| Shot Type | Fresh Required? | Dried Acceptable? | CC Stock Acceptable? | Primary Source for Launch |
|---|---|---|---|---|
| Cover / hero image | Preferred | Yes (well-staged) | YES — primary for most species | Wikimedia Commons CC-BY-SA |
| Identification / habit shot | No | N/A | YES — primary source | Wikimedia Commons; iNaturalist CC-BY |
| Root / rhizome preparation | No | YES — primary path | Supplementary | Mountain Rose Herbs dried material |
| Flat-lay bundle shot (Etsy slot 4) | No | YES — primary path | N/A | Dried herbs from Mountain Rose Herbs |
| Lifestyle shot (guide on desk) | No | YES (dried props) | N/A | Studio staged with dried herb props |

### Pre-Sprint Photography Track (June 3–21)

This track runs before the sprint and does not compete with sprint writing time.

| Activity | Duration | Window | Float | Notes |
|---|---|---|---|---|
| Props acquisition (kraft paper, mortar/pestle, glass jars, linen, wooden tray, white reflector) | 2 hr | June 3–9 | 12 days | Budget $60–100 |
| Seedling photography (Calendula, Red Clover, Lemon Balm, Thyme, Lavender — seeds sown May 26) | 4 hr | June 3–9 | 10 days | Target 30–40 images; cull to 20–30 keepers |
| Mature/flowering specimen photography (Black Cohosh if ordered May 25, Elderberry if ordered June 15) | 5 hr | June 10–16 | 5 days | Photograph within 3 days of arrival; iNaturalist CC-BY is automatic fallback for any species not yet arrived |
| Dried herb studio session — Mountain Rose Herbs material | 3 hr | June 17–21 | 1 day | 5 bundle-themed flat-lays; 100–150 raw images; cull to 50–60 keepers |
| Photo editing — cull, warm preset, export at 2400×2400px | 3 hr | June 19–21 | 1 day | Create PHOTO_MANIFEST.csv and PHOTO_ATTRIBUTION_LOG.md |
| Attribution logging — all Wikimedia CC and iNaturalist images logged in WORKLOG.md | 1 hr | June 21 | 0 days | ZERO TOLERANCE on unlicensed images in published guides |

**Target photo inventory by June 21**: 8–12 studio images per bundle (40–60 total), 3–5 hero/cover candidates per bundle (15–25 usable), all attribution records complete.

---

## Section 6: Upload Sequence and Launch Gates

### Gate Status — Both Cleared

| Gate | Threshold | Actual | Status | Margin |
|---|---|---|---|---|
| Phase 2 Forager Cohort conversion | >20% | 21.3% | CLEARED | +1.3 pp |
| Native Plants Regional Guide conversion | >1.5% | 2.24% | CLEARED | +0.74 pp |

Monitoring continues weekly May 30–July 13. Gate drop below thresholds does not affect sprint writing or design — it affects upload authorization only if both gates drop simultaneously (see Fallback B below).

### Staggered Upload Sequence

Simultaneous multi-listing uploads suppress individual listing momentum. Each new listing receives approximately 72 hours of Etsy algorithmic discovery window as "newest" in its search category. 7-day spacing maximizes each bundle's individual window.

| Upload Date | Bundle | SKU | Price | Days Since Previous | Alignment |
|---|---|---|---|---|---|
| June 29 | Women's Health | MH-BUNDLE-WH-001 | $22 | First upload | Black Cohosh uncontested keyword; practitioner intent year-round |
| July 6–7 | Respiratory Health | MH-BUNDLE-RH-001 | $20 | 7–8 days | Cold/flu research intent builds July–August |
| July 13 | Sleep and Nervines | MH-BUNDLE-SN-001 | $20 | 7 days | July burnout-resolution peak; practitioner tier activates |
| July 15 | Practitioner tier live | MH-PRAC-10 | $120–$150 | 2 days after Sleep | 3-bundle minimum met; $120–$150 practitioner bundle goes live |
| July 20 | Immunity Support | MH-BUNDLE-IM-001 | $22 | 7 days | Review accumulation before November cold/flu peak |
| August 3 | Digestive Support | MH-BUNDLE-DS-001 | $20 | 14 days | Autumn gut-health positioning; Dandelion cross-sell trigger |

### Per-Bundle Upload Checklist

Execute before publishing each listing:

1. PDF export from Canva: under 5MB, no placeholder text, all images attributed in sources section
2. Cover image: 2400×2400px; verify thumbnail crop at 170×135px
3. Etsy title: under 140 characters, primary keyword in first 40 characters
4. Tags: 13 tags, each under 20 characters; keyword density checked on July 10 SEO pass
5. Price: match master price list above
6. Category: Digital Downloads > Patterns & How To > Other Patterns & How To
7. Test download as buyer: purchase test copy, confirm PDF opens and all images render correctly
8. Practitioner 10-pack listing: upload simultaneously with July 15 practitioner tier activation ($120–$150; 10-copy client license terms explicitly stated)

### Conditional Fallback Paths

**Fallback A — Forager cohort drops below 20% by June 15**: Continue all pre-sprint activities. Hold Women's Health upload until June 22 re-check shows recovery. Sprint writing begins June 22 as planned. Zero quality impact.

**Fallback B — Both gates missed by June 22**: Execute pre-sprint photography and sourcing (sunk cost under $120). Hold writing sprint until July 1 gate re-check. Delay first upload from June 29 to July 13. Women's Health September launch target preserved.

**Current assessment**: Both gates cleared with margin. Fallback B probability is low. No action before the June 20 pre-sprint gate check.

---

## Section 7: Risk Analysis and Mitigation

### Risk Scoring Matrix

Probability: 1 = Low (15–25%), 2 = Medium (30–45%), 3 = High (50%+). Impact: 1 = Low, 2 = Medium, 3 = High.

| Risk | P | I | Score | Float Available | Primary Mitigation | Contingency Trigger |
|---|---|---|---|---|---|---|
| Goldenseal order missed (June 8) | 2 | 1 | 2 | 0 days for photo; writing unaffected | Wikimedia CC path confirmed before June 8 | June 7 EOD no order receipt: email NC Botanical Garden + Missouri Botanical Garden same day |
| Mountain Rose Herbs dried herbs delayed | 1 | 2 | 2 | 5 days | Order June 15; Frontier Co-op 3–5 day backup | Not shipped by June 20: Frontier Co-op order same day |
| Canva design revision loops | 2 | 2 | 4 | 1–4 days per cover | Pre-test brand kit June 21; design lock July 3; Google Docs fallback | Any cover exceeds 2 hours first attempt: simplify — remove background image layer |
| Writing velocity below 300 words/hour | 2 | 2 | 4 | 2 float days = 8 hours | Pre-compiled outlines reduce research time | June 24 EOD WH below 2,500 words: activate Option C immediately |
| Week 1 daily pace unsustainable | 2 | 2 | 4 | 2 float days | Option C scope absorbs variation | June 26 writing 4+ hours behind: shift Respiratory to July 13, Sleep to July 20 |
| Palette revision after June 15 | 2 | 2 | 4 | 0 days post-design start | Confirm palette June 15; hex codes above lock automatically if undecided | June 15 undecided: lock hex codes above automatically |
| Photography equipment failure | 1 | 1 | 1 | 7–10 days pre-sprint float | Indoor studio only; Wikimedia CC is primary source | No trigger required — photography is not a launch blocker |
| Both Phase 2 gates drop below threshold | 1 | 2 | 2 | Sprint writing unaffected | Continue pre-sprint prep regardless | June 20 gate check both below threshold: re-check July 1 before authorizing upload |

### Supplier Delay Recovery Sequence

1. Day 0 (expected ship date): No ship confirmation received — proceed to Step 2 same day. Do not wait.
2. Day 0: Identify photo fallback for the affected species. Confirm Wikimedia CC-BY-SA coverage is pre-staged. For Goldenseal: confirm NC and Missouri Botanical Garden have been emailed.
3. Day 1: Activate photo fallback. Log in WORKLOG.md with date and rationale. Continue writing and design on original schedule.
4. Day 3: If still not shipped, cancel and activate backup supplier if window permits. For Mountain Rose Herbs: order Frontier Co-op immediately.

### Writing Bottleneck Resolution Order

If pace falls behind daily targets:
1. Reduce scope to Option C. Activate at the June 24 pace gate if Women's Health is below 2,500 words.
2. Condense shared-species second-occurrence sections to 300 words (from 600–800). Saves 4–8 hours with minimal quality impact.
3. Defer FTC compliance review for lowest-risk bundles (Digestive, Respiratory) to post-launch v1.1. Reserve the full FTC pass for Women's Health and Immunity.
4. Accept Immunity (July 20) and Digestive (August 3) as post-sprint uploads by design — they are already planned that way and removing all sprint pressure from Weeks 2–3 writing.

### Float Days Summary

| Buffer | Date | Hours | Purpose |
|---|---|---|---|
| Pace gate buffer built into D3 | June 24 | 1 hr | Absorbs D2–D3 overrun; triggers scope decision if needed |
| Design float (all covers) | June 23–27 | 3–4 days | No cover is critical path; writing always takes priority on any day |
| Pre-sprint buffer | June 15–21 | 5 days | Any supplier or photography issue before sprint opens |
| Sprint Float Day 1 | July 12 | 8 hrs | Absorbs any Week 3 writing or admin overrun |
| Sprint Float Day 2 | July 13 afternoon | 4 hrs | Post-Sleep-upload corrections to queued listings |
| Post-sprint Immunity buffer | July 14–19 | 6 days | 6 full days before Immunity upload July 20 |

---

## Section 8: Gantt-Style Timeline — June 22–July 13

The table below shows each day of the 22-day sprint. Critical-path items are indicated. Float days are labeled. Dependencies are indicated by bundle abbreviation in the Dependency column.

| Day | Date | Week | Writing | Design | Photography | Upload/Admin | Critical Path | Float |
|---|---|---|---|---|---|---|---|---|
| D1 | June 22 | W1 | WH: Black Cohosh full section | — | — | Tier 3 plant orders placed | YES | 1 day |
| D2 | June 23 | W1 | WH: Vitex + Red Clover | WH cover (Burgundy) | Calendula + Red Clover seedlings | — | YES | 1 day |
| D3 | June 24 | W1 | WH: Calendula + Lavender + self-edit | Resp cover (Sage) | Lavender + Lemon Balm + Thyme | PACE GATE EOD | YES | 0 days |
| D4 | June 25 | W1 | Resp: Elderberry full | Imm cover (Burgundy) | Dried herbs studio Day 1 | — | YES | 1 day |
| D5 | June 26 | W1 | Resp: Mullein + Echinacea | Sleep cover (Lavender) | Dried herbs studio Day 2 | — | YES | 1 day |
| D6 | June 27 | W1 | Resp: Thyme + shared sections | WH zone card | Edit + cull photos | — | No | 2 days |
| D7 | June 28 | W1 | Resp self-edit + WH PDF QA | Resp zone card | — | WH export-ready | No | 2 days |
| D8 | June 29 | W2 | Imm: intro + Echinacea condensed | Dig cover (Sage) | — | **WH UPLOAD** | YES | 1 day |
| D9 | June 30 | W2 | Imm: Ashwagandha full (900 words) | Sleep zone card | — | — | YES | 1 day |
| D10 | July 1 | W2 | Imm: Elderberry condensed + Goldenseal intro + CITES sidebar | Imm zone card | — | — | YES | 1 day |
| D11 | July 2 | W2 | Imm: Goldenseal cultivation + FGV + berberine + self-edit | Dig zone card | — | — | YES | 1 day |
| D12 | July 3 | W2 | Sleep: Valerian full (800 words) | Practitioner cover | — | **DESIGN LOCK EOD** | No | 2 days |
| D13 | July 4 | W2 | Sleep: Passionflower full (700 words) | — | — | — | No | 2 days |
| D14 | July 5 | W2 | Sleep: Lemon Balm + Lavender condensed + self-edit | Consistency review | — | Resp export-ready | No | 2 days |
| D15 | July 6 | W3 | Dig: intro + Dandelion full (900 words) | Export test all covers | — | **RESP UPLOAD** | YES | 1 day |
| D16 | July 7 | W3 | Dig: Calendula + Lemon Balm condensed | — | — | — | No | 1 day |
| D17 | July 8 | W3 | Dig: Ginger full (700 words) + self-edit | — | — | — | No | 2 days |
| D18 | July 9 | W3 | FTC compliance review all 5 bundles | — | — | — | No | 2 days |
| D19 | July 10 | W3 | SEO pass + PDF export all 5 | — | — | — | No | 1 day |
| D20 | July 11 | W3 | File naming + practitioner staging + Etsy QA | — | — | — | No | 1 day |
| D21 | July 12 | W3 | **FLOAT DAY 1** — absorbs any W3 overrun | — | — | — | No | Float |
| D22 | July 13 | W3 | Sprint retrospective + WORKLOG update | — | — | **SLEEP UPLOAD** | YES | 4 hrs |

**Critical path sequence**: D1 WH start → D3 pace gate → D7 WH export → D8 upload → D10 CITES sidebar → D11 Goldenseal complete → D12 design lock → D15 Resp upload → D22 Sleep upload → July 15 practitioner tier live.

**Slack days with float**: D6, D7, D12, D13, D14, D17, D18, D20, D21. These days absorb scope changes without threatening critical-path dates.

**Post-sprint uploads (planned, not overrun)**: July 15 practitioner tier, July 20 Immunity, August 3 Digestive.

---

## Section 9: Three Decisions Required by May 30

`[DECISION 1]` **Sprint Scope** — Which bundles execute June 22–July 13?

| Option | Bundles | Adjusted Writing Hours | First Upload | Risk | Recommendation |
|---|---|---|---|---|---|
| A — All 5 bundles, single writer | WH, Resp, Sleep, Imm, Dig | 56–66 hrs | June 29 | Medium — requires 5+ hrs/day Weeks 1–2 | Only if 5 hrs/day is confirmed available |
| B — Two writers | Split 5 bundles | ~40 + 26 hrs split | June 29 | Low-Medium (coordination overhead) | Only if a trusted herbalist writer is available |
| **C — 3-bundle priority (recommended)** | **WH, Resp, Sleep** | **36–44 hrs** | **June 29** | **Very Low** | **Recommended for single writer** |

Option C rationale: The practitioner tier ($120–$150) unlocks July 13 when Sleep goes live — the 3-bundle minimum clinical library threshold is met. Immunity and Digestive defer to July 20 and August 3 at zero sprint-window revenue cost. The estimated 90-day revenue difference versus Option A is approximately $745 total, which closes by September from ongoing sales momentum on the first three live bundles. Under Option C, Goldenseal drops off the critical path entirely — the June 8 decision becomes a quality-upgrade option, not a hard gate.

`[DECISION 2]` **Canva Palette** — Confirm the six hex codes in Section 4 by June 15.

No changes accepted after June 23 when covers enter production. If no decision by June 15, the hex codes in Section 4 lock automatically. No further action is required.

`[DECISION 3]` **Goldenseal Sourcing Path** — Path 1 (live order by June 8) or Path 2 (Wikimedia CC + NC Botanical Garden).

Under Option C, Immunity launches July 20. Path 1 order arrives July 13–20 — workable but zero float. Path 2 has no risk and is launch quality. Path 1 is justified only if live-specimen photography is a deliberate brand priority and the June 8 order deadline is confirmed.

---

## Appendix A: FTC Language Quick Reference

All five bundles must use qualifying language for any therapeutic claims.

| Do NOT write | Write instead |
|---|---|
| "Black Cohosh relieves menopause symptoms" | "Traditionally used in Cherokee and Appalachian folk medicine for women's hormonal transitions" |
| "Elderberry prevents colds" | "Studied in randomized controlled trials for cold duration outcomes" |
| "Valerian cures insomnia" | "Studied in clinical trials for sleep-related outcomes with mixed results across study designs" |
| "Goldenseal is antimicrobial" | "Contains berberine, an alkaloid studied in vitro and in clinical settings for antimicrobial activity" |
| "Ashwagandha reduces cortisol" | "Contains withanolides, compounds studied in randomized controlled trials for stress-related physiological markers" |

**CITES sidebar (mandatory in Immunity bundle body)**: "Goldenseal (*Hydrastis canadensis*) is listed in CITES Appendix II. International trade in wild-harvested material requires export permits. This guide recommends cultivated sources only. Forest Grown Verified (FGV) certified sources are available via the United Plant Savers participant directory at unitedplantsavers.org/forest-grown-verified."

**Mandatory per-species warnings**: Vitex — not for use during pregnancy or with hormonal medications. Ashwagandha — not for use with thyroid medications or during pregnancy without medical supervision. Valerian — potentiates CNS depressants and benzodiazepines. Passionflower — contraindicated with MAOIs. Lemon Balm — may affect TSH levels; caution with thyroid conditions.

---

## Appendix B: Pre-Sprint Action Checklist (May 20–June 21)

| Date | Action | Owner |
|---|---|---|
| May 30 | Sprint scope decision (Option A / B / C) — log in WORKLOG.md | USER |
| May 30 | Goldenseal path decision — log in WORKLOG.md | USER |
| May 30 | Palette decision — confirm or defer to June 15 auto-lock | USER |
| June 1 | Email Strictly Medicinal Seeds + Prairie Moon: Goldenseal and Black Cohosh availability confirmation | USER |
| June 3–9 | Begin seedling photography window (Calendula, Red Clover, Lemon Balm, Thyme, Lavender starts) | USER |
| June 7 EOD | Goldenseal order check: if no receipt by EOD, email NC Botanical Garden + Missouri Botanical Garden same day | USER |
| June 8 | HARD DEADLINE: Goldenseal order placed OR CC path confirmed in writing — log in WORKLOG.md | USER |
| June 10–16 | Mature/flowering specimen photography window | USER |
| June 15 | HARD DEADLINE: Elderberry order placed | USER |
| June 15 | Mountain Rose Herbs dried herb order placed ($93–141); request Goldenseal CoA | USER |
| June 15 | PALETTE DECISION DEADLINE — hex codes auto-lock if no decision logged | USER |
| June 17–21 | Dried herb studio photography session | USER |
| June 19–21 | Photo editing: cull to 50–60 keepers, warm preset, export at 2400×2400px | USER |
| June 21 | Attribution logging for all sourced images — WORKLOG.md | USER |
| June 21 | Canva Brand Kit Phase 3 palette loaded (15-minute action) | USER |
| June 22 | Tier 3 plant orders placed (Echinacea, Ashwagandha, Passionflower, Valerian, Ginger, Vitex) | USER |
| June 22 | SPRINT BEGINS | — |

---

---

## Appendix C: Accelerated Upload Sequence — If Gates Pass Mid-July

Both gates are already cleared. If Phase 2 forager cohort exceeds 30% (strong overperformance) by mid-July, the upload sequence can be accelerated by 7 days per bundle:

| Accelerated Date | Bundle | Original Date | Condition |
|---|---|---|---|
| July 13 | Women's Health + Respiratory simultaneously | June 29 + July 6 | Only if both are written and export-ready early |
| July 18 | Sleep | July 13 | 5-day acceleration |
| July 22 | Practitioner tier | July 15 | After Sleep live |
| July 25 | Immunity | July 20 | 5-day acceleration |
| August 10 | Digestive | August 3 | Minimal acceleration justified |

**Acceleration trigger**: If both post-Phase 2 gate checks (June 6 and June 13) show forager cohort above 27%, accelerate Respiratory upload to July 2 (same day as Immunity writing completion). This yields 7 additional days of Etsy discovery window before the July burnout-resolution peak. Log in WORKLOG.md if triggered.

---

*Document version 5.0 — May 21, 2026. Supersedes v4.0 (2026-05-20).*
*Companion CSV: `phase-3-timeline.csv` (milestone spreadsheet — start date, duration, resource, dependencies, float days, gate dates).*
*Source files: `phase-3-medicinal-herbs-content-outline.md`, `phase-3-medicinal-herbs-sourcing-guide.md`, `PHASE_3_SUPPLIER_CONFIRMATION_TRACKER.md`, `canva-phase-3-adaptation-guide.md`, `HERBALIST_PRACTITIONER_ECOSYSTEM.md`, `HERBALIST_NETWORK_ECOSYSTEM_MAPPING.md`, `TRACK_B_FINAL_EXECUTION_GUIDE.md`, `TRACK_B_MAY_30_DECISION_PACKAGE.md`, `PHASE_3_PRODUCTION_GANTT.csv`.*
*Next reviews: May 30 (3 decisions), June 1 (Black Cohosh order), June 8 (Goldenseal deadline), June 15 (palette + Tier 2 supplier deadline), June 20 (pre-sprint gate check), June 22 (sprint launch), June 24 (D3 pace gate).*
