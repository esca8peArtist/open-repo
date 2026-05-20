---
title: "Phase 3 Medicinal Herbs — Critical Path Analysis & Production Timeline"
date: 2026-05-20
version: 6.0
status: production-ready
phase: Phase 3 pre-execution
decision-deadline: May 30, 2026
execution-window: June 22 – July 13, 2026 (22 calendar days)
gate-status:
  forager-cohort: CLEARED (21.3%, gate >20%)
  native-plants-conversion: CLEARED (2.24%, gate >1.5%)
word-count: 3,200+
companion-csv: phase-3-medicinal-herbs-gantt-timeline.csv
supersedes: v5.0 (2026-05-20)
tags: [seedwarden, phase-3, critical-path, production-timeline, medicinal-herbs]
---

# Phase 3 Medicinal Herbs — Critical Path Analysis & Production Timeline

**Version**: 6.0  
**Prepared**: May 20, 2026  
**Decision deadline**: May 30, 2026  
**Execution window**: June 22 – July 13, 2026 (22 calendar days)  
**Launch gates**: BOTH CLEARED — forager cohort 21.3% (gate >20%), native plants conversion 2.24% (gate >1.5%)  
**Companion file**: `phase-3-medicinal-herbs-gantt-timeline.csv` (milestones + float days, June 22–July 13)

---

## Executive Summary

Phase 3 is authorized to execute. Both demand-validation gates are cleared. The June 22–July 13 sprint is feasible for a single writer producing all five bundles at 3–5 focused hours per day, with a 3-bundle priority path (Women's Health, Respiratory, Sleep) recommended as the standard scope. Writing is the binding constraint at 56–66 adjusted hours. Design and photography run in parallel and do not compete with writing time on any critical-path day. Supplier specimens are quality upgrades for post-launch guide versions — all 14 unique species have verified Wikimedia Commons CC-BY-SA or iNaturalist CC-BY photo coverage sufficient for launch quality.

**Three decisions are required by May 30** and are marked `[DECISION]` throughout this document.

---

## Section 1: Medicinal Herb Selection — Finalized Species Map

All five bundles are production-locked. No further species decisions are required.

| Bundle | Species (5 each) | SKU | Price | Upload Target |
|---|---|---|---|---|
| Women's Health | Black Cohosh, Vitex, Red Clover, Calendula, Lavender | MH-BUNDLE-WH-001 | $22 | June 29 |
| Respiratory Health | Elderberry, Mullein, Echinacea purpurea, E. angustifolia, Thyme | MH-BUNDLE-RH-001 | $20 | July 6–7 |
| Sleep and Nervines | Valerian, Passionflower, Lemon Balm, Lavender | MH-BUNDLE-SN-001 | $20 | July 13 |
| Immunity Support | Echinacea, Ashwagandha, Elderberry, Goldenseal | MH-BUNDLE-IM-001 | $22 | July 20 |
| Digestive Support | Dandelion, Calendula, Lemon Balm, Ginger | MH-BUNDLE-DS-001 | $20 | August 3 |
| **Total** | **21 species slots — 14 unique; 7 appear in 2 bundles** | — | $21 avg | — |

**Shared-species efficiency**: Echinacea, Elderberry, Calendula, Lavender, and Lemon Balm each appear in two bundles. Second-occurrence writing requires approximately 40% of first-occurrence effort. This reduces adjusted writing hours to 56–66 from 64–74 raw.

**Upload sequence rationale**: Women's Health first — Black Cohosh is uncontested at Etsy Tier 3 keyword with high practitioner intent. Respiratory second — cold/flu research intent builds July–August (buyers research in summer). Sleep third — July burnout-resolution peak. Immunity fourth for review accumulation before November cold/flu season. Digestive last, aligned with autumn gut-health intent and the dandelion cross-sell from the wild-edibles forager cohort.

---

## Section 2: Supplier Sourcing Timeline

Physical plant specimens are supplementary to production. All 14 unique species have verified photo coverage for launch quality. Live plants improve photography but do not gate writing or design. Three supplier tiers are distinguished by lead time and criticality.

### Tier 1 — Hard deadline June 8 (5–6 week lead time; ZERO float)

These are the two conservation-significant species with the longest lead times and limited cultivated stock. An order placed after June 8 arrives after the July 13 sprint end.

| Species | Bundle | Primary Supplier | Lead Time | Cost | Fallback Path | Complexity Note |
|---|---|---|---|---|---|---|
| Goldenseal (*Hydrastis canadensis*) | Immunity | Prairie Moon Nursery — rhizome division; prairiemoon.com; 866-417-8156 | 5–6 weeks | $15–22 | Strictly Medicinal Seeds ($12–18); then Wikimedia CC-BY-SA (USDA PLANTS + NC Botanical Garden) | CITES Appendix II. Mandatory cultivation-only framing. FGV sourcing documentation required. Berberine framing in guide body. |
| Black Cohosh (*Actaea racemosa*) | Women's Health | Strictly Medicinal Seeds — 2-year seedling; strictlymedicinalseeds.com | 5–6 weeks (ordered May 25 = June 21–28 arrival; within sprint Week 1) | $10–15 | Prairie Moon Nursery ($12–18); then iNaturalist CC-BY (Appalachian sources, excellent coverage) | UpS At-Risk. 150-word conservation sidebar. Cherokee traditional use framing requires accuracy review. |

`[DECISION 1]` **Goldenseal sourcing — declare by May 30, order by June 8:**
- Path 1: Order from Prairie Moon or Strictly Medicinal by June 8. Plant arrives July 13–20 for v1.1 photography. No writing impact.
- Path 2 (recommended under 3-bundle scope): Confirm Wikimedia CC path now. Email media@ncbg.unc.edu and media@mobot.org. Zero cost, zero schedule risk. Under Option C, Immunity does not launch until July 20 — Path 2 is fully sufficient for launch quality. Path 1 is a quality upgrade decision, not a launch requirement.

**June 8 sign-off required**: Log path decision in WORKLOG.md. If Path 1: record tracking number. If Path 2: confirm image filenames in PHOTO_ATTRIBUTION_LOG.md.

### Tier 2 — Deadline June 15 (4-week lead time)

| Species | Bundle | Primary Supplier | Lead Time | Cost | Fallback | Arrival |
|---|---|---|---|---|---|---|
| Elderberry (*Sambucus nigra*) | Respiratory + Immunity | Prairie Moon — bare-root; info@prairiemoon.com | 4 weeks | $15–25 | Local nursery — potted 2-gal, 1–2 weeks; order by June 22 if Prairie Moon OOS | ~July 13–20 |
| Dried herbs — all 13 species, 1 oz each | All 5 bundles | Mountain Rose Herbs — wholesale@mountainroseherbs.com | 3–5 business days | $93–141 total | Frontier Co-op — 3–5 day ship, comparable species coverage | June 17–18 if ordered June 15 |

Mountain Rose Herbs dried herb order is the single highest-impact supplier action for photography quality. It enables the dried herb studio session (June 17–21) that produces flat-lay content for all five bundle Etsy listing images. Request a Certificate of Analysis for Goldenseal root confirming cultivated origin when placing the order.

**Budget summary by tier**:

| Tier | Items | Low | High |
|---|---|---|---|
| Tier 1 | Goldenseal + Black Cohosh (Path 1 only) | $22 | $37 |
| Tier 2 | Elderberry | $15 | $25 |
| Tier 3 | Echinacea, Ashwagandha, Passionflower, Valerian, Ginger, Vitex | $65 | $105 |
| Dried herbs (MRH) | 13 species × 1 oz | $93 | $141 |
| Studio props | Kraft paper, mortar/pestle, jars, linen | $60 | $100 |
| **Total (Path 1)** | | **$255** | **$408** |
| **Total (Path 2 — no Goldenseal order)** | | **$233** | **$371** |

### Tier 3 — Deadline June 22 (2–3 week lead time; order sprint start day)

These species have wide availability and all have verified Wikimedia Commons or iNaturalist CC photo fallback. No launch risk.

| Species | Bundle | Primary Supplier | Fallback Photo |
|---|---|---|---|
| Echinacea purpurea | Respiratory, Immunity | Prairie Moon or Strictly Medicinal | Wikimedia CC-BY-SA — abundant |
| Echinacea angustifolia | Respiratory, Immunity | Strictly Medicinal Seeds | iNaturalist CC-BY — prairie range |
| Ashwagandha | Immunity | Strictly Medicinal Seeds | iNaturalist CC-BY (India observations) |
| Passionflower (*P. incarnata*) | Sleep | Prairie Moon | iNaturalist CC-BY — SE US, exceptional |
| Valerian (*V. officinalis*) | Sleep | Prairie Moon or Strictly Medicinal | iNaturalist CC-BY — NE US populations |
| Ginger (*Zingiber officinale*) | Digestive | Strictly Medicinal or grocery store | No fallback needed — grocery rhizome valid |
| Vitex (*V. agnus-castus*) | Women's Health | Local nursery (landscape shrub) | Wikimedia CC-BY-SA — widely cultivated |

**Photo-only species (no specimen order needed)**: Red Clover, Mullein, Thyme, Lemon Balm, Lavender, Calendula, Dandelion — all have exceptional Wikimedia Commons CC-BY-SA coverage. Dandelion photos already exist in the Seedwarden wild-edibles archive.

**Supplier backup reference**:

| Primary Fails | Species | Backup 1 | Backup 2 |
|---|---|---|---|
| Prairie Moon | Goldenseal | Strictly Medicinal Seeds | NC Botanical Garden photo license (free) |
| Strictly Medicinal | Black Cohosh | Prairie Moon Nursery | iNaturalist CC-BY |
| Prairie Moon | Elderberry | Local nursery (potted, +$5–15) | Wikimedia CC-BY-SA |
| Mountain Rose Herbs | All dried herbs | Frontier Co-op (3–5 day emergency ship) | Local health food co-op |

---

## Section 3: Writing Schedule

### Total Writing Budget

Writing velocity: 300–350 words per hour for research-dense medicinal herb content working from pre-compiled outlines in `phase-3-medicinal-herbs-content-outline.md`. Hour counts include research integration, drafting, contraindications verification, FTC language review, and one self-edit pass.

| Bundle | Target Words | Species | Raw Hours | Adjusted Hours (shared-species) | Primary Peer Review |
|---|---|---|---|---|---|
| Women's Health | 3,800 | 5 (0 shared) | 14–16 | 14–16 | RH-AHG reviewer (Black Cohosh / Vitex accuracy) |
| Respiratory Health | 3,600 | 5 (0 shared at time of writing) | 12–14 | 12–14 | Optional — Echinacea two-species comparison review |
| Sleep and Nervines | 3,500 | 4 (1 shared: Lavender) | 12–14 | 11–13 | Pharmacist or ND (sedative drug interaction review) |
| Immunity Support | 3,800 | 4 (2 shared: Echinacea, Elderberry) | 14–16 | 10–12 | RH-AHG reviewer (Goldenseal CITES, Ashwagandha) |
| Digestive Support | 3,600 | 4 (2 shared: Calendula, Lemon Balm) | 12–14 | 9–11 | Optional — lowest-risk bundle |
| **Total** | **18,300** | **21 slots (14 unique)** | **64–74** | **56–66** | |

### Per-Bundle Writing Dates and Daily Breakdown

**Week 1: June 22–28 — Women's Health + start Respiratory**

Women's Health leads because it contains the two species with the deepest compliance requirements (Black Cohosh conservation sidebar, Vitex invasive-species note) and has the earliest upload target (June 29). Week 1 is the most intensive writing week.

| Day | Date | Writing Task | Word Target | Hours | Float | Critical Path |
|---|---|---|---|---|---|---|
| D1 | June 22 | WH front matter + introduction + Black Cohosh (identification, habitat, 150-word conservation sidebar, cultivation, harvest, active constituents, contraindications) | ~700 | 5 | 1 day | YES |
| D2 | June 23 | WH: Vitex complete (invasive note SE states, berry harvest timing, dopaminergic framing, contraindications) + Red Clover complete (isoflavone framing, forager-edible crossover, pregnancy caution) | ~1,000 | 5 | 1 day | YES |
| D3 | June 24 | WH: Calendula + Lavender (3-cultivar comparison: Hidcote, Munstead, Phenomenal) + preparation methods + practitioner section + WH self-edit pass | ~1,100 | 5 | 0 days | YES — WH complete by June 28 for June 29 upload |
| — | June 25 | Resp: Front matter + introduction + Elderberry (800 words — raw berry toxicity, sambunigrin, elderflower forager crossover) | ~800 | 5 | 1 day | YES |
| — | June 26 | Resp: Mullein (biennial lifecycle, first-year rosette vs. second-year spike, ear oil preparation) + Echinacea two-species (600 words — E. purpurea vs. E. angustifolia, UpS At-Risk sidebar) | ~1,100 | 5 | 1 day | YES |
| — | June 27 | Resp: Thyme (500 words — thymol framing, pregnancy caution at large doses) + shared sections + WH final self-edit pass | ~900 | 4 | 2 days | No |
| — | June 28 | Resp self-edit pass + WH PDF export QA (5MB limit check, placeholder scan, attribution confirm, thumbnail crop test at 170×135px) | — | 2 | 2 days | No |

**Pace gate at D3 (June 24 EOD)**: If Women's Health is below 2,500 words at end of Day 3, the single-writer 5-bundle Option A path is not viable. Activate Option C (3-bundle scope: Women's Health + Respiratory + Sleep) immediately. The June 29 / July 6–7 / July 13 upload dates remain intact under Option C.

**Week 1 milestone**: Women's Health complete (3,800 words), export-ready by June 28. Respiratory complete (3,600 words). First Etsy upload June 29.

**Peer review window for Women's Health (June 22–29)**: Contact an AHG-directory RH practitioner (Women's Health specialty filter) by June 22 with a draft preview of the Black Cohosh section. The review does not need to be formal — a written "reviewed for botanical accuracy and contraindication completeness" confirmation is sufficient. This review quote becomes an Etsy listing credibility signal before July 13 when AHG directory outreach begins. Target: one reviewer response by June 27.

---

**Week 2: June 29–July 5 — Immunity + Sleep**

Week 2 opens with the Women's Health upload (2 hours, June 29 morning) and pivots immediately to Immunity. Goldenseal (CITES Appendix II sidebar, FGV sourcing, berberine framing) and Ashwagandha (900 words — the longest single species section in Phase 3) together account for 1,800 of the 3,800 Immunity words and require the most precision of any content in Phase 3.

| Day | Date | Writing Task | Word Target | Hours | Float | Critical Path |
|---|---|---|---|---|---|---|
| D8 | June 29 | WH upload AM (2 hrs) + Imm: Introduction + Echinacea condensed (immunity framing, 60% of Resp length) | ~600 | 3 + 2 upload | 1 day | YES |
| D9 | June 30 | Imm: Ashwagandha complete (900 words — Rasayana context, withanolide RCT framing, cultivation zones 8–12 perennial / 5–7 annual, MANDATORY thyroid + pregnancy warning) | ~900 | 5 | 1 day | YES |
| D10 | July 1 | Imm: Elderberry condensed (fermentation note, immunity framing) + Goldenseal introduction + CITES Appendix II sidebar (200 words — MANDATORY in guide body) | ~700 | 5 | 1 day | YES |
| D11 | July 2 | Imm: Goldenseal cultivation + FGV sourcing documentation + berberine active constituents + all shared sections + self-edit | ~900 | 5 | 1 day | YES |
| D12 | July 3 | Sleep: Front matter + Introduction + Valerian complete (800 words — second-year root harvest, valerenic acid framing, sedative drug interaction MANDATORY) | ~800 | 4 | 2 days | No |
| D13 | July 4 | Sleep: Passionflower complete (700 words — maypop forager crossover, trellis requirements, chrysin/vitexin framing, MAOI interaction note MANDATORY) | ~700 | 4 | 2 days | No |
| D14 | July 5 | Sleep: Lemon Balm condensed (nervine framing, TSH caution MANDATORY) + Lavender condensed (linalool/aromatherapy framing distinct from Women's Health salve angle) + shared sections + self-edit | ~1,000 | 4 | 2 days | No |

**Week 2 milestone**: Immunity complete (3,800 words). Sleep complete (3,500 words). Respiratory upload July 6–7. Sleep upload staged for July 13.

**Peer review for Immunity (July 1–10)**: The Goldenseal CITES sidebar and Ashwagandha thyroid warning are the two mandatory accuracy-review items. Email the PHASE_3_HERBALIST_NETWORK_PRESTAGING.md contact list (ND or RH with clinical herbal medicine focus) by July 2 with the Immunity draft Goldenseal and Ashwagandha sections. Request review by July 10. A practitioner review of the CITES sidebar is the single most important credibility action for the Immunity bundle, given the UpS and FGV sourcing claims.

---

**Week 3: July 6–13 — Digestive + Final Passes + Uploads**

Digestive benefits from two shared species (Calendula, Lemon Balm) and the Dandelion section is the most strategically important content in Phase 3 — it is the direct cross-sell hook from the Phase 2 wild-edibles forager cohort.

| Day | Date | Task | Type | Hours | Float | Critical Path |
|---|---|---|---|---|---|---|
| D15 | July 6 | Resp upload AM (2 hrs) + Digestive: Introduction + Dandelion complete (900 words — bitters, wild-edibles cross-sell hook, roasted root coffee substitute, inulin/taraxacin framing) | Write + Upload | 5 + 2 | 1 day | YES |
| D16 | July 7 | Digestive: Calendula condensed (digestive framing — internal infusion, mucosal healing, not topical salve angle) + Lemon Balm condensed (carminative framing, post-meal gas relief) + shared sections | Write | 4 | 1 day | No |
| D17 | July 8 | Digestive: Ginger complete (700 words — cultivation zones, grocery store rhizome warning, gingerol/shogaol framing, nausea RCT evidence base) + Digestive self-edit | Write | 4 | 2 days | No |
| D18 | July 9 | FTC language compliance review all 5 bundles (priority: WH Black Cohosh/Vitex → Immunity Goldenseal CITES/Ashwagandha thyroid → Sleep sedative interactions → Resp → Digestive) | Review | 3 | 2 days | No |
| D19 | July 10 | SEO optimization pass (Etsy title/tag keyword density) + PDF export all 5 bundles (5MB limit, no placeholder text, attribution complete) + sources compilation | Admin | 4 | 1 day | No |
| D20 | July 11 | File naming convention + practitioner variant staging + Etsy listing QA for Sleep + Immunity + Digestive queued bundles | Admin | 2 | 1 day | No |
| D21 | July 12 | FLOAT DAY 1 — absorbs writing overrun from any Week 3 day | Float | 0–4 | — | No |
| D22 | July 13 | Sleep upload live + sprint retrospective + WORKLOG.md update | Upload | 2 + 2 | 4 hrs | YES |

**Week 3 milestone**: Digestive complete (3,600 words). All 5 PDFs export-ready. Women's Health + Respiratory + Sleep live on Etsy. Immunity and Digestive staged for July 20 and August 3 uploads.

### Revision Buffers

Each bundle has 1.5–2 hours of revision buffer embedded in its writing week beyond the minimum writing pace. Beyond this, two structural buffers are available:

1. **Float Day 1 (July 12)**: 8 hours available for writing overrun from any Week 3 day.
2. **Float Day 2 (July 13 afternoon post-upload)**: 4 hours available for last-minute corrections to any queued listing.

If both float days are consumed, the recovery path is to defer Digestive from August 3 to August 10 (zero revenue impact in the sprint window).

---

## Section 4: Canva Design Timeline

### Design Scope and Hours

Phase 3 design is adaptation work built on Phase 2 templates. No template rebuild is required. Design runs fully parallel to writing — no writing day is blocked by design and no design task is blocked by writing.

| Task | Hours/Unit | Units | Total Hours | Notes |
|---|---|---|---|---|
| Palette pre-test (one zone card, color rendering check) | 0.5 | 1 | 0.5 | Pre-sprint; must complete before June 22 |
| Bundle cover (hero image + title + palette swap) | 1.2 | 5 | 6.0 | |
| Zone card (existing template, 4-field content fill per bundle) | 0.8 | 5 | 4.0 | |
| Practitioner bundle cover (8.5"×11", premium tier visual) | 1.5 | 1 | 1.5 | Produced after all 5 covers complete |
| Consistency review + export test all 5 covers | 0.5 | 1 | 0.5 | |
| Revision buffer (1 cover, minor adjustment) | — | — | 1.5 | |
| **Total** | | | **14.0 hours** | All parallel to writing; no critical-path conflicts |

### Phase 3 Color Palette — Authoritative Version (May 19, 2026)

`[DECISION 2]` **Palette must be finalized by June 15.** Load into Canva Brand Kit on June 21. Any revision after June 23 requires rebuilding completed covers (approximately 1.2 hours of rework per cover already produced).

| Color Name | Hex Code | Bundle Assignment | Use Case |
|---|---|---|---|
| Deep Burgundy | #8B3E3E | Women's Health, Immunity | Primary header background |
| Sage Green | #6B8E6F | Respiratory, Digestive | Primary header background |
| Apothecary Gold | #D4AF37 | All bundles | Accent bar, highlights (premium tier signal) |
| Clinical Cream | #F9F5F0 | All bundles | Page background |
| Muted Lavender | #9B8BA0 | Sleep bundle only | Bundle-specific accent |
| Dark Charcoal | #2C2C2C | All bundles | Body text |

**Note on palette version history**: `phase-3-canva-mockup-brief.md` (May 9) contains an older five-color palette (Herb Brown #6B4F35 as primary). The May 19 palette above is the authoritative production version. Deep Burgundy (#8B3E3E) replaces Herb Brown — it is more appropriate for the apothecary/clinical positioning of Phase 3.

**June 15 deadline note**: If no palette decision is confirmed by June 15, the six hex codes above lock automatically. They are production-ready as written.

### Per-Bundle Design Schedule

Design tasks are scheduled to parallel the writing day for the same bundle. Float is 3–4 days on all cover tasks because Wikimedia Commons hero images are pre-confirmed available for all five bundles.

| Task | Scheduled Date | Float | Dependency | Notes |
|---|---|---|---|---|
| Brand Kit palette pre-test + 1 zone card export | June 21 | 1 day | Palette confirmed by June 15 | 30-minute action; confirms hex codes render correctly in Canva |
| Women's Health cover (Black Cohosh or Calendula hero, Deep Burgundy) | June 23 | 4 days | Hero photo available from Wikimedia CC | Parallel to D2 writing |
| Respiratory cover (Elderberry berry cluster hero, Sage Green) | June 24 | 4 days | Hero photo available | Parallel to D3 writing |
| Immunity cover (Goldenseal root or Ashwagandha hero, Deep Burgundy) | June 29 | 4 days | Hero photo available | Parallel to D8 Immunity writing |
| Sleep cover (Passionflower flower hero, Muted Lavender) | June 30 | 3 days | iNaturalist CC-BY Passiflora available | Passionflower is visually superior on CC compared to most live specimens |
| Women's Health zone card (cultivation calendar, Zone 5 reference) | July 1 | 4 days | WH cover complete | 4-field template fill |
| Respiratory zone card | July 2 | 4 days | Resp cover complete | |
| Digestive cover (Dandelion root or Ginger rhizome hero, Sage Green) | July 3 | 0 days | Hero photo available | **DESIGN LOCK — no cover changes after July 3 EOD** |
| Immunity + Sleep + Digestive zone cards (three 0.8-hr sessions) | July 6–7 | 2 days | All covers complete | Schedule alongside D15–D16 writing |
| Practitioner bundle cover (8.5"×11", Gold/Burgundy premium layout) | July 8 | 5 days | All 5 covers complete | Low-urgency; practitioner tier goes live July 15 |
| Consistency review + export test all 5 covers + zone cards | July 9 | 2 days | All design tasks complete | Final check before D19 PDF export pass |

**Design lock: July 3 EOD.** After this date, no cover changes are made until after launch. Google Docs PDF export is the fallback if any Canva template issue is unresolvable on a critical day — guide content is the primary purchase driver for practitioner buyers, not design polish.

**Branding consistency checks**: Each cover is verified against three standards before export: (1) hex codes match the Brand Kit exactly, (2) Playfair Display Bold used for all headers, (3) Latin binomials in Lato Italic. A single consistency check session on July 9 confirms all five covers before the PDF export pass on July 10.

---

## Section 5: Photography Staging

### Photography Strategy

Indoor studio with north-facing window light plus one reflector is the primary plan for all five bundles. No outdoor location photography is required — all identification, habit, and preparation photography can be completed at this setup. This eliminates permit risk, weather dependency, and travel cost.

Most ordered live specimens arrive at or after sprint end (July 12–20). This is expected. Wikimedia Commons CC-BY-SA and iNaturalist CC-BY sources cover 100% of photography needs at guide launch quality. Live specimens are photographed post-sprint for v1.1 updates.

### Fresh vs. Dried vs. Stock Photo Decision Matrix

| Shot Type | Fresh Required? | Dried Acceptable? | CC Stock Acceptable? | Primary Source for Launch |
|---|---|---|---|---|
| Cover / hero image | Preferred | Yes (well-staged) | YES — primary for most species | Wikimedia Commons CC-BY-SA |
| Identification / habit shot | No | N/A | YES — primary source | Wikimedia Commons; iNaturalist CC-BY |
| Root / rhizome preparation | No | YES — primary path | Supplementary | Mountain Rose Herbs dried material |
| Flat-lay bundle shot (Etsy slot 4) | No | YES — primary path | N/A | Dried herbs from Mountain Rose Herbs |
| Lifestyle shot (guide on desk) | No | YES (dried props) | N/A | Studio staged with dried herb props |

**Lighting setup requirements**: North-facing window 9am–2pm (consistent diffuse light). White reflector card (18"×24") for fill on shadow side. Kraft paper or linen background. No ring light (creates harsh catchlights on botanical specimens). Warm preset in post: +0.2 exposure / -20 highlights / +15 shadows. Export at 2400×2400px minimum for Canva.

### Pre-Sprint Photography Track (June 3–21)

This track runs before the sprint and does not compete with sprint writing time.

| Activity | Duration | Window | Float | Notes |
|---|---|---|---|---|
| Props acquisition (kraft paper, mortar/pestle, glass jars, linen, wooden tray, white reflector) | 2 hr | June 3–9 | 12 days | Budget $60–100 |
| Seedling photography (Calendula, Red Clover, Lemon Balm, Thyme, Lavender starts — seeds sown by May 26) | 4 hr | June 3–9 | 10 days | Target 30–40 images; cull to 20–30 keepers |
| Mature / flowering specimen photography (Black Cohosh arrival ~June 21; Elderberry if ordered June 15) | 5 hr | June 10–16 | 5 days | Photograph within 3 days of arrival; iNaturalist CC-BY is automatic fallback for any species not yet arrived |
| Dried herb studio session — Mountain Rose Herbs material (bundles, jars, mortar staging) | 3 hr | June 17–21 | 1 day | 5 bundle-themed flat-lays; 100–150 raw images; cull to 50–60 keepers |
| Photo editing — cull to 50–60 keepers; warm preset; export at 2400×2400px | 3 hr | June 19–21 | 1 day | Create PHOTO_MANIFEST.csv and PHOTO_ATTRIBUTION_LOG.md |
| Attribution logging — all Wikimedia CC and iNaturalist sourced images logged in WORKLOG.md | 1 hr | June 21 | 0 days | ZERO TOLERANCE on unlicensed images in published guides |

**Target photo inventory by June 21**: 8–12 studio images per bundle (40–60 total), 3–5 hero/cover candidates per bundle (15–25 usable), all attribution records complete.

### Supplier Scheduling for Live Specimens

All Tier 1–2 specimens ordered for photography arrive at or after sprint end. This is planned, not a problem.

| Species | Order Deadline | Expected Arrival | Photography Plan | Guide Version |
|---|---|---|---|---|
| Goldenseal | June 8 (Path 1 only) | July 13–20 | Wikimedia CC for sprint; live specimen post-sprint if ordered | v1.1 upgrade |
| Black Cohosh | May 25 (optimal) / June 8 (latest) | June 21–28 or July 13–20 | iNaturalist CC-BY (Appalachian, abundant) for sprint | v1.1 upgrade if late |
| Elderberry | June 15 | July 13–20 | Wikimedia Commons CC-BY-SA (exceptional coverage) | v1.1 upgrade |
| Echinacea | June 22 | July 8–15 | Wikimedia Commons (abundant E. purpurea) | v1.1 upgrade |
| Passionflower | June 22 | July 12–19 | iNaturalist CC-BY SE US (abundant, high visual quality) | v1.1 upgrade |

### In-Sprint Studio Sessions (June 23–26, parallel with Week 1 writing)

Photography is secondary during the sprint. Writing takes priority on any day where time is constrained.

| Day | Species Photographed | Shot Types | Hours |
|---|---|---|---|
| June 23 | Calendula + Red Clover seedlings | Flat-lay on linen; seedling in pot; leaf close-up | 2 |
| June 24 | Lavender + Lemon Balm + Thyme (local nursery starts) | Full plant habit; stem close-up; dried bundle staged | 3 |
| June 25 | Dried herb studio — Immunity bundle props (Mountain Rose Herbs) | Mortar-and-pestle; glass jars; Immunity bundle flat-lay | 3 |
| June 26 | Edit + cull June 23–25 photos | Rate, select keepers; export at 2400×2400px | 2 |

---

## Section 6: Upload Sequence and Launch Gates

### Gate Status — Both Cleared

| Gate | Threshold | Actual | Status | Margin |
|---|---|---|---|---|
| Phase 2 Forager Cohort conversion | >20% | 21.3% | CLEARED | +1.3 pp |
| Native Plants Regional Guide conversion | >1.5% | 2.24% | CLEARED | +0.74 pp |

Both gates are cleared with margin. Monitoring continues weekly May 30–July 13. Gate drop below thresholds does not affect sprint writing or design — it affects only upload authorization if both drop simultaneously (see Fallback B below).

### Staggered Upload Sequence and Spacing

Simultaneous multi-listing uploads suppress individual listing momentum. Each new listing receives approximately 72 hours of Etsy algorithmic discovery window as "newest" in its search category. 7-day spacing maximizes each bundle's individual discovery window.

| Upload Date | Bundle | SKU | Price | Days Since Previous | Seasonal and Strategic Alignment |
|---|---|---|---|---|---|
| June 29 | Women's Health | MH-BUNDLE-WH-001 | $22 | First upload | Practitioner intent year-round; Black Cohosh uncontested keyword |
| July 6–7 | Respiratory Health | MH-BUNDLE-RH-001 | $20 | 7–8 days | Cold/flu research builds July–August |
| July 13 | Sleep and Nervines | MH-BUNDLE-SN-001 | $20 | 7 days | July burnout-resolution peak |
| July 15 | Practitioner tier live | MH-PRAC-10 | $120–150 | 2 days after Sleep | Practitioner 3-bundle minimum met at Sleep upload |
| July 20 | Immunity Support | MH-BUNDLE-IM-001 | $22 | 7 days | Review accumulation before November cold/flu peak |
| August 3 | Digestive Support | MH-BUNDLE-DS-001 | $20 | 14 days | Autumn gut-health positioning; dandelion forager cross-sell email trigger |

### Per-Bundle Upload Checklist

Execute before publishing each listing:

1. PDF export from Canva: under 5MB, no placeholder text, all images attributed in sources section
2. Cover image: 2400×2400px; verify thumbnail crop at 170×135px (Etsy preview size)
3. Etsy title: under 140 characters, primary keyword in first 40 characters
4. Tags: 13 tags, each under 20 characters; keyword density checked on July 10 SEO pass
5. Price: match master price list above
6. Category: Digital Downloads > Patterns & How To > Other Patterns & How To
7. Test download as buyer: purchase test copy, confirm PDF opens and all images render correctly
8. Practitioner 10-pack listing: upload simultaneously ($120–150; practitioner license variant with 10-copy terms explicitly stated)

### Conditional Dependencies on Phase 2 Performance

Phase 2 Track B launches May 30. The upload sequence has two conditional fallback paths depending on Phase 2 post-launch metrics:

**Fallback A — Forager cohort drops below 20% by June 15**: Continue all pre-sprint activities (Canva, photography, sourcing). Hold Women's Health Etsy upload until June 22 re-check shows recovery. Sprint writing begins June 22 as planned. Zero quality impact.

**Fallback B — Both gates missed by June 22**: Execute pre-sprint photography and sourcing (sunk cost under $120 in plant orders). Hold writing sprint until July 1 gate re-check. Delay first upload from June 29 to July 13. Women's Health September launch target preserved.

**Current assessment**: Both gates are cleared with margin (forager cohort 1.3 pp buffer; native plants 0.74 pp buffer). Fallback B probability is low. No action needed before the June 20 pre-sprint gate check.

---

## Section 7: Risk Analysis and Mitigation

### Risk Scoring Matrix

Probability: 1 = Low (15–25%), 2 = Medium (30–45%), 3 = High (50%+). Impact: 1 = Low, 2 = Medium, 3 = High.

| Risk | P | I | Score | Float Available | Primary Mitigation | Contingency Trigger |
|---|---|---|---|---|---|---|
| Goldenseal order missed (June 8) | 2 | 1 | **2** | 0 days for photo; writing unaffected | Wikimedia CC path confirmed before June 8 | June 7 EOD no order receipt: email NC Botanical Garden + Missouri Botanical Garden same day |
| Mountain Rose Herbs dried herbs delayed | 1 | 2 | **2** | 5 days | Order June 15; Frontier Co-op 3–5 day backup | Not shipped by June 20: Frontier Co-op order same day |
| Canva design revision loops | 2 | 2 | **4** | 1–4 days per cover | Pre-test brand kit June 21; design lock July 3; Google Docs PDF fallback | Any cover exceeds 2 hours first attempt: simplify template, remove background image layer |
| Writing velocity below 300 words/hour | 2 | 2 | **4** | 2 float days = 8 hours | Pre-compiled outlines reduce research time | June 24 EOD WH below 2,500 words: activate Option C immediately |
| Week 1 daily pace unsustainable (5+ hrs/day) | 2 | 2 | **4** | 2 float days | 3-bundle scope absorbs pace variation | June 26 writing 4+ hours behind: shift Respiratory to July 13, Sleep to July 20 |
| Palette revision after June 15 | 2 | 2 | **4** | 0 days post-design start | Confirm palette June 15; default to documented hex codes | June 15 undecided: lock hex codes above automatically |
| Photography equipment failure | 1 | 1 | **1** | 7–10 days pre-sprint float | Indoor studio only; Wikimedia CC is primary source | No trigger required — photography is not a launch blocker |
| Both Phase 2 gates drop below threshold | 1 | 2 | **2** | Sprint writing unaffected | Continue pre-sprint prep regardless; hold upload only | June 20 gate check both below threshold: re-check July 1 before authorizing upload |

### Supplier Delay Recovery Sequence

Built-in 3-day recovery window separates each supplier deadline from its downstream photography gate:

1. Day 0 (expected ship date): Check order status. No ship confirmation: proceed to Step 2 same day — do not wait.
2. Day 0: Identify the photo fallback path for the affected species. Confirm Wikimedia Commons CC-BY-SA coverage is pre-staged. For Goldenseal: confirm NC Botanical Garden or Missouri Botanical Garden has been emailed.
3. Day 1: Activate photo fallback. Log in WORKLOG.md with date and rationale. Continue writing and design on original schedule.
4. Day 3: If still not shipped, cancel and activate backup supplier if window permits. For Mountain Rose Herbs: order Frontier Co-op immediately.

### Design Revision Loop Mitigation

The highest revision risk bundles are Immunity (Goldenseal hero image may require multiple sourcing attempts) and Sleep (Passionflower requires selecting best available CC image). Mitigation steps:

1. Pre-stage 3–5 hero image candidates per bundle in Canva before starting cover design — do not open cover design with only one image option.
2. Women's Health and Respiratory have the lowest revision risk (Calendula and Elderberry berry clusters have the widest CC selection of any Phase 3 species).
3. If any cover exceeds 2 hours on first attempt, simplify: remove background image layer, use color block header with text only. Google Docs PDF export is the launch-viable fallback for any single bundle.

### Writing Bottleneck Resolution Order

If pace falls behind the daily targets:
1. **First response**: Reduce scope to Option C (3-bundle). Activate at the June 24 pace gate if Women's Health is below 2,500 words.
2. **Second response**: Condense shared-species second-occurrence sections to 300 words each (from 600–800). Saves 4–8 hours with minimal quality impact.
3. **Third response**: Defer FTC compliance review for the least legally sensitive bundles (Digestive, Respiratory) to post-launch v1.1. Reserve dedicated FTC pass for Women's Health and Immunity.
4. **Accept post-sprint uploads**: Immunity July 20 and Digestive August 3 are already post-sprint by design. Accepting these dates as plan-of-record removes all pressure from Weeks 2–3.

### Float Days Summary

| Buffer | Date | Hours | Purpose |
|---|---|---|---|
| Pace gate buffer built into D3 | June 24 | 1 hr | Absorbs Day 2–3 overrun |
| Design float (covers) | June 23–27 | 3–4 days | No cover is critical path; writing always takes priority |
| Pre-sprint buffer | June 15–21 | 5 days | Any supplier or photography issue before sprint |
| Sprint Float Day 1 | July 12 | 8 hrs | Absorbs any Week 3 writing or admin overrun |
| Sprint Float Day 2 | July 13 afternoon | 4 hrs | Post-Sleep-upload corrections to queued listings |
| Post-sprint buffer (Immunity) | July 14–19 | 6 days | Immunity upload July 20 has 6 full days post-sprint |

---

## Section 8: Three Decisions Required by May 30

`[DECISION 1]` **Sprint Scope** — Which bundles execute in June 22–July 13?

| Option | Bundles | Writing Hours | First Upload | Risk | Recommendation |
|---|---|---|---|---|---|
| A — All 5 bundles | Women's Health, Resp, Sleep, Immunity, Digestive | 56–66 hrs adjusted | June 29 | Medium — 5+ hrs/day Weeks 1–2 | If 5 hrs/day confirmed available |
| B — Two writers | Split 5 bundles across two writers | ~40 + 26 hrs split | June 29 | Low-Medium (coordination) | If trusted herbalist writer available |
| **C — 3-bundle priority** | **Women's Health, Respiratory, Sleep** | **36–44 hrs** | **June 29** | **Very Low** | **Recommended** |

**Option C recommendation rationale**: Writing quality is preserved at 3–5 hours per bundle for editing. The practitioner tier unlocks on July 13 when Sleep goes live (3-bundle minimum). Immunity and Digestive defer to July 20 and August 3 at zero sprint-window revenue cost. The 90-day revenue gap versus Option A (~$745 total) closes entirely by September. Goldenseal drops off the critical path entirely under Option C — the June 8 decision becomes a quality-upgrade option, not a hard gate.

`[DECISION 2]` **Canva Palette** — Confirm the six hex codes above by June 15.

No changes accepted after June 23 (covers in production). Default: hex codes in this document lock automatically on June 15 if no decision is recorded.

`[DECISION 3]` **Goldenseal Sourcing Path** — Path 1 (live order by June 8) or Path 2 (Wikimedia CC).

Under Option C (recommended), Immunity launches July 20. Path 1 order arrives July 13–20 — workable but zero float. Path 2 has no risk and is launch-quality. Path 1 is justified only if live-specimen photography is a deliberate brand priority and the June 8 order deadline is confirmed.

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

**Mandatory warnings per species**: Vitex — not for use during pregnancy or while taking hormonal medications. Ashwagandha — not for use with thyroid medications or during pregnancy without medical supervision. Valerian — potentiates CNS depressants and benzodiazepines. Passionflower — contraindicated with MAOIs. Lemon Balm — may affect TSH levels; caution with thyroid conditions.

---

## Appendix B: Pre-Sprint Action Checklist (May 20–June 21)

| Date | Action | Owner |
|---|---|---|
| May 30 | Sprint scope decision (Option A / B / C) confirmed | USER |
| May 30 | Goldenseal path decision confirmed | USER |
| May 30 | Palette finalization — confirm or record revision | USER |
| June 1 | Email Strictly Medicinal Seeds + Prairie Moon: Goldenseal and Black Cohosh availability | USER |
| June 3–9 | Begin seedling photography window (Calendula, Red Clover, Lemon Balm, Thyme) | USER |
| June 7 EOD | Goldenseal order check: if no order receipt by EOD, email NC Botanical Garden + Missouri Botanical Garden | USER |
| June 8 | HARD DEADLINE: Goldenseal order placed OR CC path confirmed in writing | USER |
| June 10–16 | Mature/flowering specimen photography window | USER |
| June 15 | HARD DEADLINE: Elderberry order placed | USER |
| June 15 | Mountain Rose Herbs dried herb order placed ($93–141) | USER |
| June 15 | PALETTE DECISION DEADLINE: Confirm hex codes | USER |
| June 17–21 | Dried herb studio photography session | USER |
| June 19–21 | Photo editing: cull to 50–60 keepers, warm preset, export at 2400×2400px | USER |
| June 21 | Attribution logging for all sourced images (WORKLOG.md) | USER |
| June 21 | Canva brand kit Phase 3 palette loaded (15-minute action) | USER |
| June 22 | Tier 3 plant orders placed (Echinacea, Ashwagandha, Passionflower, Valerian, Ginger, Vitex) | USER |
| June 22 | SPRINT BEGINS | — |

---

*Document version 6.0 — May 20, 2026. Supersedes v5.0.*  
*Companion CSV: `phase-3-medicinal-herbs-gantt-timeline.csv` (milestones + float days).*  
*Source files: `phase-3-medicinal-herbs-content-outline.md`, `phase-3-medicinal-herbs-sourcing-guide.md`, `PHASE_3_SUPPLIER_CONFIRMATION_TRACKER.md`, `canva-phase-3-adaptation-guide.md`, `HERBALIST_PRACTITIONER_ECOSYSTEM.md`, `TRACK_B_MAY_30_DECISION_PACKAGE.md`.*  
*Next review: June 8 (Goldenseal deadline), June 15 (palette + supplier deadline), June 21 (pre-sprint readiness), June 22 (sprint launch).*
