---
title: "Phase 3 Medicinal Herbs — Critical Path Analysis & Production Timeline"
date: 2026-05-20
version: 3.0
status: production-ready — decision document for May 30 scope authorization
phase: Phase 3 pre-execution
decision-deadline: May 30, 2026
execution-window: June 22 – July 13, 2026 (22 calendar days)
gate-status:
  forager-cohort: CLEARED (21.3%, gate >20%)
  native-plants-conversion: CLEARED (2.24%, gate >1.5%)
supersedes: v2.0 (2026-05-19)
cross-references:
  - phase-3-medicinal-herbs-gantt-timeline.md
  - phase-3-medicinal-herbs-gantt-timeline.csv
  - phase-3-medicinal-herbs-content-outline.md
  - phase-3-medicinal-herbs-sourcing-guide.md
  - PHASE_3_PHOTOGRAPHY_LOGISTICS_PLAN.md
  - PHASE_3_ASSETS_VERIFICATION.md
  - PHASE_3_BUNDLE_CONTENT_OUTLINE_DETAILED.md
  - PHASE_3_PHOTO_SOURCING_AND_BRIEF_REFINED.md
  - canva-phase-3-adaptation-guide.md
  - HERBALIST_PRACTITIONER_ECOSYSTEM.md
tags: [seedwarden, phase-3, medicinal-herbs, critical-path, production-timeline, decision-support]
---

# Phase 3 Medicinal Herbs — Critical Path Analysis & Production Timeline

**Version**: 3.0
**Prepared**: May 20, 2026 (consolidates v2.0 May 19 + v6.0 lowercase May 20; adds peer review windows, practitioner tier design, mandatory contraindication register, risk scoring updates)
**Decision deadline**: May 30, 2026 — scope authorization required before Phase 2 launches
**Execution window**: June 22 – July 13, 2026 (22 calendar days)
**Both launch gates**: CLEARED — forager cohort 21.3% (gate >20%), native plants conversion 2.24% (gate >1.5%)
**Word count**: ~4,200 words

---

## Executive Summary

Phase 3 is authorized. Both demand-validation gates are cleared before Phase 2 launches. The June 22 – July 13 sprint is feasible for a single writer producing all five bundles at 4–5 hours/day, with a three-bundle priority path (Women's Health + Respiratory + Sleep) recommended as the standard scope.

**The binding constraint is writing (56–66 adjusted hours), not design (14 hours) or photography (parallel pre-sprint track).** The critical path runs through writing alone: Women's Health complete June 28 → upload June 29 → Respiratory upload July 6–7 → Sleep upload July 13. Design and photography run parallel to writing and carry 3–14 days of float on every task.

**Three decisions are required by May 30:**

1. **Sprint scope**: Option A (5-bundle, single writer, 5 hrs/day) vs. Option B (two parallel writers, 22-day window) vs. Option C (3-bundle priority launch: Women's Health + Respiratory + Sleep — recommended).
2. **Goldenseal path**: Order live specimen from Prairie Moon or Strictly Medicinal by June 8, OR confirm the Wikimedia CC photo substitution path. One or the other must be logged in WORKLOG.md by June 8 — not both, not neither.
3. **Second writer**: If Option B, brief that writer by May 25 using `phase-3-medicinal-herbs-content-outline.md` and `PHASE_3_BUNDLE_CONTENT_OUTLINE_DETAILED.md`. Do not wait until June.

**Minimum viable launch** (if all five bundles cannot execute in 22 days): Women's Health + Respiratory + Sleep. These three bundles cover 10,700 words, represent the highest Etsy search intent in the medicinal herbs category, and upload June 29, July 6–7, and July 13 respectively. Immunity and Digestive defer to July 20 and August 3 at no cost to the November–December holiday review window.

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

**Shared-species efficiency**: Echinacea, Elderberry, Calendula, Lavender, and Lemon Balm each appear in two bundles. Second-occurrence writing requires approximately 40% of first-occurrence effort (reframing only — cultivation and identification sections are condensed to 300 words vs. 600–800 for first occurrence). This reduces adjusted writing hours to 56–66 from the 64–74 raw estimate.

**Upload sequence rationale**: Women's Health first — Black Cohosh is uncontested at Etsy Tier 3 keyword with high practitioner intent. Respiratory second — cold/flu research intent builds July–August (buyers research in summer for autumn preparations). Sleep third — July burnout-resolution peak. Immunity fourth for review accumulation before the November cold/flu season. Digestive last, aligned with autumn gut-health intent and the Dandelion cross-sell from the Phase 2 wild-edibles forager cohort.

---

## Section 2: Supplier Sourcing Timeline

Physical plant specimens are supplementary to production quality. All 14 unique species have verified photo coverage for launch quality via Wikimedia Commons CC-BY-SA or iNaturalist CC-BY (documented in `phase-3-medicinal-herbs-sourcing-guide.md` and `PHASE_3_PHOTO_SOURCING_AND_BRIEF_REFINED.md`). Live plants improve photography but do not gate writing or design.

### Tier 1 — Hard Deadline June 8 (5–6 week lead time; ZERO float)

These are the two conservation-significant species with the longest lead times and limited cultivated stock. An order placed after June 8 arrives after the July 13 sprint end.

| Species | Bundle | Primary Supplier | Lead Time | Cost | Fallback Path | Complexity Note |
|---|---|---|---|---|---|---|
| Goldenseal (*Hydrastis canadensis*) | Immunity | Prairie Moon Nursery — rhizome division; prairiemoon.com; 866-417-8156 | 5–6 weeks | $15–22 | Strictly Medicinal Seeds ($12–18); then Wikimedia CC-BY-SA (USDA PLANTS + NC Botanical Garden media@ncbg.unc.edu) | CITES Appendix II. Mandatory cultivation-only framing. FGV sourcing documentation required in guide body. |
| Black Cohosh (*Actaea racemosa*) | Women's Health | Strictly Medicinal Seeds — 2-year seedling; strictlymedicinalseeds.com | 5–6 weeks (ordered May 25 → June 21–28 arrival) | $10–15 | Prairie Moon Nursery ($12–18); then iNaturalist CC-BY (Appalachian sources, excellent coverage) | UpS At-Risk. 150-word conservation sidebar mandatory. Cherokee traditional use framing requires accuracy review. |

**`[DECISION 1]` Goldenseal sourcing — declare by May 30, order by June 8 if Path 1.**

- Path 1: Order from Prairie Moon or Strictly Medicinal by June 8. Plant arrives July 13–20 for v1.1 photography. No writing impact. Recommended only under Option A or B.
- Path 2 (recommended under Option C): Confirm Wikimedia CC path now. Email media@ncbg.unc.edu and media@mobot.org. Zero cost, zero schedule risk. Under Option C, Immunity does not launch until July 20 — Path 2 is fully sufficient for launch quality. Path 1 is a quality upgrade, not a launch requirement.

**June 8 sign-off required**: Log the decision in WORKLOG.md. If Path 1: record order confirmation + expected arrival date. If Path 2: confirm three Wikimedia CC-BY-SA Goldenseal image filenames in `PHOTO_ATTRIBUTION_LOG.md`.

### Tier 2 — Deadline June 15 (4-week lead time)

| Species | Bundle | Primary Supplier | Lead Time | Cost | Fallback | Arrival |
|---|---|---|---|---|---|---|
| Elderberry (*Sambucus nigra*) | Respiratory + Immunity | Prairie Moon — bare-root; info@prairiemoon.com | 4 weeks | $15–25 | Local nursery — potted 2-gal, 1–2 weeks (order by June 22 if Prairie Moon OOS) | ~July 13–20 |
| Dried herbs — 13 species, 1 oz each | All 5 bundles | Mountain Rose Herbs — wholesale@mountainroseherbs.com | 3–5 business days | $93–141 total | Frontier Co-op — 3–5 day ship | June 17–18 if ordered June 15 |

Mountain Rose Herbs is the single highest-impact supplier action for photography quality. The dried herb studio session (June 17–21) produces the flat-lay content for all five bundle Etsy listing images. Request a Certificate of Analysis for Goldenseal root confirming cultivated origin when placing this order.

### Tier 3 — Deadline June 22 (2–3 week lead time; order sprint start day)

These species have wide availability and all have verified Wikimedia Commons or iNaturalist CC photo fallback. No launch risk.

| Species | Bundle | Primary Supplier | Fallback Photo |
|---|---|---|---|
| Echinacea purpurea | Respiratory, Immunity | Prairie Moon or Strictly Medicinal | Wikimedia CC-BY-SA — abundant |
| Echinacea angustifolia | Respiratory, Immunity | Strictly Medicinal Seeds | iNaturalist CC-BY — prairie range |
| Ashwagandha | Immunity | Strictly Medicinal Seeds | iNaturalist CC-BY (India observations) |
| Passionflower (*P. incarnata*) | Sleep | Prairie Moon | iNaturalist CC-BY — SE US, exceptional visual quality |
| Valerian (*V. officinalis*) | Sleep | Prairie Moon or Strictly Medicinal | iNaturalist CC-BY — NE US populations |
| Ginger (*Zingiber officinale*) | Digestive | Strictly Medicinal or grocery store | Grocery store rhizome is fully valid for studio photography |
| Vitex (*V. agnus-castus*) | Women's Health | Local nursery (landscape shrub) | Wikimedia CC-BY-SA — widely cultivated |

**Photo-only species (no specimen order needed)**: Red Clover, Mullein, Thyme, Lemon Balm, Lavender, Calendula, Dandelion — all have exceptional Wikimedia Commons CC-BY-SA coverage. Dandelion photos already exist in the Seedwarden wild-edibles archive (`assets/wild-edibles/`).

**Budget summary by tier**:

| Tier | Items | Low | High |
|---|---|---|---|
| Tier 1 (Path 1 only) | Goldenseal + Black Cohosh | $22 | $37 |
| Tier 2 | Elderberry + Mountain Rose Herbs dried herbs | $108 | $166 |
| Tier 3 | Echinacea, Ashwagandha, Passionflower, Valerian, Ginger, Vitex | $65 | $105 |
| Studio props | Kraft paper, mortar/pestle, jars, linen, wooden tray | $60 | $100 |
| **Total (Path 1)** | | **$255** | **$408** |
| **Total (Path 2 — no Goldenseal order)** | | **$233** | **$371** |

---

## Section 3: Writing Production Schedule

### Total Writing Budget

Writing velocity: 300–350 words per hour for research-dense medicinal herb content when working from pre-compiled outlines in `phase-3-medicinal-herbs-content-outline.md`. Hour counts include research integration, drafting, contraindications verification, FTC language review, and one self-edit pass. A peer review window for Women's Health and Immunity is included in the schedule below.

| Bundle | Target Words | Species | Raw Hours | Adjusted Hours | Peer Review? |
|---|---|---|---|---|---|
| Women's Health | 3,800 | 5 (0 shared) | 14–16 | 14–16 | YES — AHG-directory RH practitioner (Black Cohosh / Vitex accuracy) |
| Respiratory Health | 3,600 | 5 (0 shared) | 12–14 | 12–14 | Optional — Echinacea two-species comparison review |
| Sleep and Nervines | 3,500 | 4 (1 shared: Lavender) | 12–14 | 11–13 | Recommended — pharmacist or ND (sedative drug interaction review) |
| Immunity Support | 3,800 | 4 (2 shared: Echinacea, Elderberry) | 14–16 | 10–12 | YES — RH-AHG reviewer (Goldenseal CITES, Ashwagandha thyroid warning) |
| Digestive Support | 3,600 | 4 (2 shared: Calendula, Lemon Balm) | 12–14 | 9–11 | Optional — lowest-risk bundle |
| **Total** | **18,300** | **21 slots (14 unique)** | **64–74** | **56–66** | |

### Mandatory Contraindication Register — Per-Species, Non-Negotiable FTC Language

Before writing begins, every species in this table must receive its contraindication section verbatim or in direct paraphrase. Omitting any of these creates Etsy product liability exposure.

| Species | Bundle | Mandatory Warning Language |
|---|---|---|
| Black Cohosh | Women's Health | "Individuals who are pregnant or breastfeeding should not use black cohosh. Do not use for longer than 6 months without consulting a healthcare provider." |
| Vitex (Chasteberry) | Women's Health | "Vitex is considered invasive in Tennessee and North Carolina. Individuals using hormonal contraceptives, prescription fertility medications, or dopaminergic medications should consult a healthcare provider before use." |
| Goldenseal | Immunity | "Goldenseal (*Hydrastis canadensis*) is listed in CITES Appendix II. International trade in wild-harvested material requires export permits. This guide recommends cultivated sources only. Individuals who are pregnant, breastfeeding, or managing high blood pressure should not use goldenseal preparations." |
| Ashwagandha | Immunity | "Individuals who are pregnant, breastfeeding, or managing a thyroid condition should consult a qualified healthcare provider before using ashwagandha preparations." |
| Valerian | Sleep | "Valerian may potentiate the effects of sedative medications, benzodiazepines, and sleep medications. Individuals taking any prescription sedative should consult a healthcare provider before use." |
| Passionflower | Sleep | "Passionflower may potentiate the effects of MAOI medications and sedative medications. Individuals taking any prescription sedative or MAOI should consult a healthcare provider before use." |
| Lemon Balm | Sleep + Digestive | "Individuals managing thyroid conditions should consult a healthcare provider before regular use of lemon balm, as it may affect TSH levels." |
| Elderberry | Respiratory + Immunity | "Raw elderberries and elderberry leaves contain sambunigrin and should not be consumed uncooked. All preparations in this guide use only properly processed (cooked or dried) elderberry material." |
| Echinacea | Respiratory + Immunity | "Individuals with autoimmune conditions or taking immunosuppressive medications should consult a healthcare provider before use." |

### Per-Bundle Writing Schedule

**Week 1: June 22–28 — Women's Health + Respiratory Start**

| Day | Date | Writing Task | Word Target | Hours | Float | Critical Path |
|---|---|---|---|---|---|---|
| D1 | June 22 | WH: Front matter + Introduction + Black Cohosh (identification, habitat, 150-word conservation sidebar, cultivation, harvest, active constituents, contraindications) | ~700 | 5 | 1 day | YES |
| D2 | June 23 | WH: Vitex complete (invasive note SE states, dopaminergic framing, contraindications) + Red Clover complete (isoflavone framing, forager-edible crossover, pregnancy caution) | ~1,000 | 5 | 1 day | YES |
| D3 | June 24 | WH: Calendula + Lavender (3-cultivar comparison: Hidcote, Munstead, Phenomenal) + preparation methods + practitioner section + WH self-edit pass | ~1,100 | 5 | 0 days | YES — WH complete by June 28 for June 29 upload |
| D4 | June 25 | Resp: Front matter + Introduction + Elderberry (800 words — raw berry toxicity, sambunigrin note, elderflower forager crossover) | ~800 | 5 | 1 day | YES |
| D5 | June 26 | Resp: Mullein (biennial lifecycle, first-year rosette vs. second-year spike, ear oil preparation) + Echinacea two-species (600 words — E. purpurea vs. E. angustifolia, UpS At-Risk sidebar) | ~1,100 | 5 | 1 day | YES |
| D6 | June 27 | Resp: Thyme (500 words — thymol framing, pregnancy caution at large doses) + shared sections + WH final self-edit pass | ~900 | 4 | 2 days | No |
| D7 | June 28 | Resp self-edit pass + WH PDF export QA (5MB limit check, placeholder scan, attribution confirm, thumbnail crop test at 170×135px) | — | 2 | 2 days | No |

**Pace gate at D3 (June 24 EOD)**: If Women's Health is below 2,500 words at end of Day 3, activate Option C (3-bundle scope) immediately. Upload dates June 29 / July 6–7 / July 13 remain intact under Option C. Do not compress quality to preserve Option A.

**Peer review window for Women's Health (June 22–29)**: Contact an AHG-directory RH practitioner (Women's Health specialty) by June 22 with a draft of the Black Cohosh section. The review can be informal — a written confirmation of botanical accuracy and contraindication completeness is sufficient. Target: one practitioner confirmation by June 27. This becomes the credibility signal for the Etsy listing before the AHG directory outreach begins July 13.

**Week 1 milestone**: Women's Health complete (3,800 words), export-ready by June 28. Respiratory complete (3,600 words). First Etsy upload June 29.

---

**Week 2: June 29–July 5 — Immunity + Sleep**

| Day | Date | Writing Task | Word Target | Hours | Float | Critical Path |
|---|---|---|---|---|---|---|
| D8 | June 29 | WH upload AM (2 hrs) + Imm: Introduction + Echinacea condensed (immunity framing, 60% of Resp length) | ~600 | 3 + 2 upload | 1 day | YES |
| D9 | June 30 | Imm: Ashwagandha complete (900 words — Rasayana context, withanolide RCT framing, cultivation zones 8–12 perennial / 5–7 annual, MANDATORY thyroid + pregnancy warning) | ~900 | 5 | 1 day | YES |
| D10 | July 1 | Imm: Elderberry condensed (fermentation note, immunity framing) + Goldenseal introduction + CITES Appendix II sidebar (200 words — mandatory in guide body) | ~700 | 5 | 1 day | YES |
| D11 | July 2 | Imm: Goldenseal cultivation + FGV sourcing documentation + berberine active constituents + all shared sections + self-edit | ~900 | 5 | 1 day | YES |
| D12 | July 3 | Sleep: Front matter + Introduction + Valerian complete (800 words — second-year root harvest, valerenic acid framing, sedative drug interaction MANDATORY) | ~800 | 4 | 2 days | No |
| D13 | July 4 | Sleep: Passionflower complete (700 words — maypop forager crossover, trellis requirements, chrysin/vitexin framing, MAOI interaction note MANDATORY) | ~700 | 4 | 2 days | No |
| D14 | July 5 | Sleep: Lemon Balm condensed (nervine framing, TSH caution MANDATORY) + Lavender condensed (linalool/aromatherapy angle, distinct from WH salve framing) + shared sections + self-edit | ~1,000 | 4 | 2 days | No |

**Peer review for Immunity (July 1–10)**: The Goldenseal CITES sidebar and Ashwagandha thyroid warning are the two mandatory accuracy-review items. Email the `HERBALIST_PRACTITIONER_ECOSYSTEM.md` contact list (ND or RH with clinical herbal medicine focus) by July 2 with the Immunity draft Goldenseal and Ashwagandha sections. Request review by July 10. A practitioner review of the CITES sidebar is the single most important credibility action for the Immunity bundle, given the UpS and FGV sourcing claims.

**Week 2 milestone**: Immunity complete (3,800 words). Sleep complete (3,500 words). Respiratory upload July 6–7. Sleep upload staged for July 13.

---

**Week 3: July 6–13 — Digestive + Final Passes + Uploads**

| Day | Date | Task | Type | Hours | Float | Critical Path |
|---|---|---|---|---|---|---|
| D15 | July 6 | Resp upload AM (2 hrs) + Digestive: Introduction + Dandelion complete (900 words — bitters, wild-edibles cross-sell hook, roasted root coffee substitute, inulin/taraxacin framing) | Write + Upload | 5 + 2 | 1 day | YES |
| D16 | July 7 | Digestive: Calendula condensed (digestive framing — internal infusion, mucosal healing, NOT topical salve angle) + Lemon Balm condensed (carminative framing, post-meal gas relief) + shared sections | Write | 4 | 1 day | No |
| D17 | July 8 | Digestive: Ginger complete (700 words — cultivation zones, grocery store rhizome warning, gingerol/shogaol framing, nausea RCT evidence base) + Digestive self-edit | Write | 4 | 2 days | No |
| D18 | July 9 | FTC language compliance review all 5 bundles (priority: WH Black Cohosh/Vitex → Immunity Goldenseal CITES/Ashwagandha thyroid → Sleep sedative interactions → Resp → Digestive) | Review | 3 | 2 days | No |
| D19 | July 10 | SEO optimization pass (Etsy title/tag keyword density) + PDF export all 5 bundles (5MB limit, no placeholder text, attribution complete) + sources compilation | Admin | 4 | 1 day | No |
| D20 | July 11 | File naming convention + practitioner variant staging + Etsy listing QA for Sleep, Immunity, Digestive queued bundles | Admin | 2 | 1 day | No |
| D21 | July 12 | FLOAT DAY 1 — absorbs writing overrun from any Week 3 day | Float | 0–4 | — | No |
| D22 | July 13 | Sleep upload live + sprint retrospective + WORKLOG.md update | Upload | 2 + 2 | 4 hrs | YES |

**Week 3 milestone**: Digestive complete (3,600 words). All 5 PDFs export-ready. Women's Health + Respiratory + Sleep live on Etsy. Immunity and Digestive staged for July 20 and August 3 uploads.

---

## Section 4: Canva Design Timeline

### Design Scope

Phase 3 design is adaptation work built on Phase 2 templates. No template rebuild is required. Design runs fully parallel to writing — no writing day is blocked by design, and no design task is blocked by writing.

| Task | Hours/Unit | Units | Total Hours | Notes |
|---|---|---|---|---|
| Palette pre-test (one zone card, color rendering check) | 0.5 | 1 | 0.5 | Pre-sprint; must complete before June 22 |
| Bundle cover (hero image + title + palette swap) | 1.2 | 5 | 6.0 | |
| Zone card (existing template, 4-field content fill per bundle) | 0.8 | 5 | 4.0 | |
| Practitioner bundle cover (8.5"×11", premium tier visual) | 1.5 | 1 | 1.5 | Produced after all 5 covers complete; practitioners receive this for $120–150 10-pack |
| Consistency review + export test all 5 covers | 0.5 | 1 | 0.5 | |
| Revision buffer (1 cover, minor adjustment) | — | — | 1.5 | |
| **Total** | | | **14.0 hours** | All parallel to writing; no critical-path conflicts |

### Phase 3 Color Palette — Authoritative Version

`[DECISION 2]` **Palette must be finalized by June 15.** Load into Canva Brand Kit by June 21. Any revision after June 23 requires rebuilding already-completed covers (1.2 hours rework per affected cover).

| Color Name | Hex Code | Bundle Assignment | Use Case |
|---|---|---|---|
| Deep Burgundy | #8B3E3E | Women's Health, Immunity | Primary header background |
| Sage Green | #6B8E6F | Respiratory, Digestive | Primary header background |
| Apothecary Gold | #D4AF37 | All bundles | Accent bar, highlights (premium tier signal) |
| Clinical Cream | #F9F5F0 | All bundles | Page background |
| Muted Lavender | #9B8BA0 | Sleep bundle only | Bundle-specific accent |
| Dark Charcoal | #2C2C2C | All bundles | Body text |

**Palette version note**: `phase-3-canva-mockup-brief.md` (May 9) contains an older five-color palette with Herb Brown #6B4F35 as primary. The palette above is the authoritative production version. Deep Burgundy (#8B3E3E) replaces Herb Brown — it is more appropriate for the apothecary/clinical positioning of Phase 3. If no decision is confirmed by June 15, the six hex codes above lock automatically.

### Per-Bundle Design Schedule

| Task | Scheduled Date | Float | Dependency |
|---|---|---|---|
| Brand Kit palette pre-test + 1 zone card export | June 21 | 1 day | Palette confirmed by June 15 |
| Women's Health cover (Black Cohosh or Calendula hero, Deep Burgundy) | June 23 | 4 days | Hero photo available from Wikimedia CC |
| Respiratory cover (Elderberry berry cluster hero, Sage Green) | June 24 | 4 days | Hero photo available |
| Immunity cover (Goldenseal root or Ashwagandha hero, Deep Burgundy) | June 29 | 4 days | Hero photo available (Wikimedia CC confirmed) |
| Sleep cover (Passionflower flower hero, Muted Lavender) | June 30 | 3 days | iNaturalist CC-BY Passiflora available |
| Women's Health zone card (cultivation calendar, Zone 5 reference) | July 1 | 4 days | WH cover complete |
| Respiratory zone card | July 2 | 4 days | Resp cover complete |
| Digestive cover (Dandelion root or Ginger rhizome hero, Sage Green) | July 3 | 0 days | Hero photo available; **DESIGN LOCK — no cover changes after July 3 EOD** |
| Immunity + Sleep + Digestive zone cards | July 6–7 | 2 days | All covers complete |
| Practitioner bundle cover (8.5"×11", Gold/Burgundy premium layout) | July 8 | 5 days | All 5 covers complete |
| Consistency review + export test all 5 covers + zone cards | July 9 | 2 days | All design tasks complete |

**Design lock rationale**: The July 3 design lock gives a full 10 days before the July 13 Sleep upload. Any post-lock revision triggers a cascade: re-export affected cover, re-QA the PDF, re-upload the listing image. The Google Docs PDF fallback (described in Section 6, Contingency 4) eliminates design as a launch blocker if Canva produces unresolvable issues.

---

## Section 5: Photography Staging and Requirements

### Pre-Sprint Photography Track (May 26–June 21)

Photography runs entirely outside the 22-day sprint window. The sprint begins with photos already available.

| Activity | Duration | Start | End | Float | Priority |
|---|---|---|---|---|---|
| Props acquisition (kraft paper, mortar/pestle, glass jars, linen, wooden tray, reflector) | 2 hrs | May 26 | June 2 | 14 days | LOW |
| Studio location scout (north-facing window, 36×24 inch minimum table, test 9am/12pm/2pm light) | 2 hrs | May 26 | May 27 | 14 days | LOW |
| Seedling photography: Calendula, Red Clover, Lemon Balm, Thyme, Lavender starts | 4 hrs | June 3 | June 9 | 10 days | MEDIUM |
| Mature/flowering specimen photography: Black Cohosh, Elderberry, Echinacea | 5 hrs | June 10 | June 16 | 5 days | MEDIUM |
| Dried herb studio session (Mountain Rose Herbs stock delivered June 17–18) | 3 hrs | June 17 | June 21 | 1 day | HIGH |
| Photo editing: cull 100–150 raw to 50–60 keepers; warm preset (+0.2 exp, -20 highlights, +15 shadows) | 3 hrs | June 19 | June 21 | 1 day | HIGH |
| Attribution log complete for all sourced CC images | 1 hr | June 21 | June 21 | 0 days | CRITICAL |

### Fresh vs. Dried State Decision Matrix

| Species | Fresh State Photography | Dried State Photography | Studio Source |
|---|---|---|---|
| Black Cohosh | iNaturalist CC-BY (Appalachian June bloom) or Strictly Medicinal live plant | N/A (root not dried for photography) | Wikimedia Commons fallback |
| Elderberry | Wikimedia CC-BY-SA berry cluster | Mountain Rose Herbs dried berries | Both needed per bundle |
| Echinacea | iNaturalist CC-BY + Wikimedia Commons | Mountain Rose Herbs dried root | Both in Resp and Immunity |
| Calendula | Wikimedia CC-BY-SA fresh flower (vivid orange) | Mountain Rose Herbs dried petals | Both in WH and Digestive |
| Valerian | iNaturalist CC-BY (NE US, flowering state) | Mountain Rose Herbs dried root (dark, sliced) | Both needed |
| Passionflower | iNaturalist CC-BY SE US (exceptional) | Mountain Rose Herbs dried herb | Fresh state is hero image |
| Ashwagandha | Wikimedia Commons (moderate quality) | Mountain Rose Herbs dried root powder | Dried is primary for Studio |
| Goldenseal | NC Botanical Garden / Missouri Botanical Garden (media outreach) | Mountain Rose Herbs dried root | Live arrival post-sprint (v1.1) |
| Dandelion | Wild-edibles archive already exists (`assets/wild-edibles/`) | Mountain Rose Herbs dried root | Cross-sell visual: fresh = food, dried = medicine |

### In-Sprint Studio Sessions (June 22–26, parallel to Day 1–5 writing)

| Day | Date | Species | Shot Types | Hours |
|---|---|---|---|---|
| D2 | June 23 | Calendula + Red Clover seedlings | Flat-lay on linen, seedling in pot, leaf close-up | 2 |
| D3 | June 24 | Lavender + Lemon Balm + Thyme starts | Full plant habit, stem close-up, dried bundle staged | 3 |
| D4 | June 25 | Dried herb Immunity props (Mountain Rose stock) | Mortar-and-pestle, glass jars, flat-lay by bundle theme | 3 |
| D5 | June 26 | Edit + cull (days 2–4 material) | Rate and select keepers, export at 2400×2400px for Canva | 2 |

**Target inventory by June 21 (Day 0 of sprint)**: 8–12 studio images per bundle = 40–60 total; 3–5 hero/cover candidates per bundle = 15–25 usable; attribution complete for all sourced images.

**Lighting setup**: North-facing window, 9 AM–2 PM natural light window. White bedsheet or 3×3 ft diffusion panel. No ring light — reads as influencer content, not practitioner reference material.

**Backgrounds by bundle**: Women's Health: linen cloth, warm rose/cream tones. Respiratory: white poster board + dried elderberry branch prop. Immunity: dark wood plank or slate (cool, clinical feel). Sleep: neutral grey backdrop + dried lavender sachet. Digestive: kraft paper (earthy/apothecary) + dandelion root prop.

---

## Section 6: Upload Sequence and Launch Gates

### Gate Status

Both Phase 3 launch gates confirmed cleared as of May 19, 2026:

| Gate | Threshold | Status |
|---|---|---|
| Phase 2 Forager cohort conversion | >20% of buyers in forager cohort | **CLEARED — 21.3%** |
| Native Plants Regional Guide conversion | >1.5% conversion rate | **CLEARED — 2.24%** |

No further gate checks are required before sprint begins. Monitoring continues post-Phase-2-launch (June 6 and June 13 check-in dates documented in the Gantt CSV) but gates are cleared with meaningful margin.

### Staggered Upload Sequence

Simultaneous multi-listing uploads suppress individual listing Etsy algorithm momentum. Each new listing receives a 72-hour discovery window as the newest in the medicinal herbs category. Staggering by 7–8 days maximizes each bundle's individual window.

| Upload Date | Bundle | SKU | Price | Days from Prior | Etsy Algorithm Note |
|---|---|---|---|---|---|
| June 29 | Women's Health | MH-BUNDLE-WH-001 | $22 | — (first upload) | First new-listing boost; Black Cohosh uncontested at Tier 3 |
| July 6–7 | Respiratory Health | MH-BUNDLE-RH-001 | $20 | 7–8 days | Cold/flu research intent peaks July–August |
| July 13 | Sleep and Nervines | MH-BUNDLE-SN-001 | $20 | 7 days | Summer burnout peak; July resolution-intent window |
| July 20 | Immunity Support | MH-BUNDLE-IM-001 | $22 | 7 days | Builds toward November cold/flu peak |
| August 3 | Digestive Support | MH-BUNDLE-DS-001 | $20 | 14 days | Extended gap — autumn gut-health positioning |

**Per-bundle upload checklist**:
1. PDF export from Canva: verify under 5MB, no placeholder text, all images attributed
2. Cover image: 2400×2400px, test thumbnail crop at 170×135px (Etsy preview size)
3. Etsy title: under 140 characters
4. Tags: 13 tags, each under 20 characters; verify keyword density matches SEO pass
5. Price: match master price list above
6. Category: Digital Downloads > Patterns & How To > Other Patterns & How To
7. Test download as buyer: purchase test copy, confirm PDF opens cleanly
8. Practitioner 10-pack listing: upload simultaneously ($120–$150, includes practitioner license page PDF)

### Email Sequence Activation per Bundle

Kit herbalist list segmentation (7 tags: women-health-interest, respiratory-interest, immunity-interest, sleep-interest, digestive-interest, all-bundles-preview, phase2-buyers) triggers upon each upload. No new email infrastructure required — Kit sequences are pre-staged per `KIT_EMAIL_LAUNCH_SEQUENCE.md`.

---

## Section 7: Risk Analysis

### Risk Scoring Matrix

Scoring: Probability (P1 = Low 15–20%, P2 = Medium 25–40%, P3 = High 50%+) × Impact (I1 = Low, I2 = Medium, I3 = High) = Risk Score. Score ≥4 requires explicit contingency trigger with defined activation date.

| Risk | P | I | Score | Float Available | Primary Mitigation | Contingency Trigger Date |
|---|---|---|---|---|---|---|
| Goldenseal order missed (June 8) | P2 | I1 (photo only; writing unaffected) | **2** | 0 days for photo | Pre-confirm Wikimedia CC path before June 8 as the default | June 7 EOD: if no order confirmation, activate CC path immediately |
| Supplier delay — Tier 1 species | P2 | I1 (photo) / I0 (writing) | **2** | 7–14 days (photo) | All 14 species have pre-staged CC photo fallbacks | Any order without confirmed ship date by June 21 → activate substitution |
| Mountain Rose Herbs delayed | P1 | I2 (studio shots delayed) | **2** | 5 days | Order June 15; Frontier Co-op is 3–5 day emergency backup | June 20: if not shipped → Frontier Co-op same day |
| Canva design revision loops | P2 | I2 (1–2 days per bundle) | **4** | 1–3 days per cover | Pre-test brand kit June 21; design lock July 3; Google Docs PDF fallback | Any single cover takes >2 hours → simplify template, remove background image layer |
| Writing velocity below 300 words/hour | P2 | I2 (8–12 hour overrun total) | **4** | 2 float days = 8–10 hours | Pre-compiled outlines; shared-species savings; condensed shared sections | June 24 EOD: if Women's Health below 2,500 words → activate Option C |
| Week 1 burnout (6–8 hr/day unsustainable) | P2 | I2 | **4** | 2 float days | Accept reduced daily target in Weeks 2–3; stagger uploads vs. compress writing | June 26 EOD: if writing more than 4 hours behind plan → shift Respiratory to July 13, Sleep to July 20 |
| Phase 2 post-launch monitoring conflict | P1 | I1 | **1** | 24-day separation (May 30 → June 22) | Phase 2 sprint May 27–29; Phase 3 begins June 22 — structural separation | No trigger required |
| FTC review expands beyond 3 hours | P2 | I1 | **2** | 2 days (July 9 has 2-day float) | Per-species mandatory language register (Section 3) flags issues during writing | July 9: if FTC review exceeds 4 hours → defer Digestive contraindications pass to post-launch v1.1 |
| Photography window disruption | P1 | I0 (indoor studio primary) | **1** | 7–10 days pre-sprint float | Indoor studio is primary plan; no bundle requires outdoor photography | No trigger required |
| Design revision escalates post-lock | P1 | I2 | **2** | 5 days post-lock before first export | Design lock July 3; Google Docs fallback covers any bundle that fails Canva export | July 10: if any cover export fails after 2 attempts → activate Google Docs PDF version |

### Contingency Decision Tree

**Contingency 1 — Activate Wikimedia CC photo path for Goldenseal**
- Trigger: June 7 EOD with no order confirmation
- Actions: (a) Email media@ncbg.unc.edu and media@mobot.org; (b) Download and log three best Wikimedia CC-BY-SA Goldenseal images; (c) Note in WORKLOG.md
- Cost: $0. Zero schedule impact.

**Contingency 2 — Activate Option C (3-bundle scope)**
- Trigger: June 24 EOD, Women's Health word count below 2,500
- Actions: Complete WH + Resp + Sleep on current schedule; defer Immunity and Digestive writing to late July for August uploads. Upload sequence unchanged for first three bundles.
- Revenue impact: Immunity delayed ~3 weeks; Digestive delayed ~3 weeks. Full revenue model preserved.

**Contingency 3 — Upload stagger instead of compressing writing**
- Trigger: July 5 EOD, Immunity writing not complete
- Actions: Upload WH June 29 and Resp July 6–7 on schedule; move Immunity upload from July 20 to July 27; move Digestive from August 3 to August 10. Sleep remains July 13.
- Revenue impact: Negligible. One-week slip on Immunity and Digestive.

**Contingency 4 — Activate Google Docs PDF fallback for design**
- Trigger: Any single cover design exceeds 2 hours on first attempt due to Canva template/font/export issues
- Actions: Create Google Docs template with header image placeholder, bundle title, and zone indicator as text. Export as PDF. Use as the launch version. Canva version becomes v1.1 design upgrade post-launch.
- Quality impact: Cover is simpler. Conversion data from Phase 2 shows guide content drives purchase decisions among practitioner buyers — not cover design.

**Contingency 5 — Minimum viable launch**
- Trigger: July 9 (Day 18), fewer than 3 bundles written and export-ready
- Priority order: (1) Women's Health — highest practitioner intent, Black Cohosh uncontested at Etsy Tier 3; (2) Sleep and Nervines — highest visual appeal, summer burnout peak; (3) Respiratory Health — cold/flu season search begins July
- Actions: Upload whichever 2–3 bundles are ready by July 13. Defer remaining bundles to August–September. Log sprint retrospective in WORKLOG.md with root-cause analysis.

### Writing Bottleneck Recovery Order

If actual pace is slower than estimate, the lever order is:
1. **Reduce scope** (Option C) before compressing quality. A shorter, accurate bundle outperforms a rushed, error-prone one on Etsy.
2. **Condense shared-species sections** — second occurrence of Elderberry, Echinacea, Calendula, Lemon Balm can be 300 words each (vs. 600–800 for first occurrence). Saves 4–8 hours with minimal quality impact.
3. **Defer FTC review to post-launch** — for Digestive and Respiratory (lowest FTC sensitivity), a careful writing pass can substitute for a separate review pass. Reserve the dedicated FTC pass for Women's Health and Immunity.
4. **Accept August launch for Immunity and Digestive** — the upload sequence already plans these at July 20 and August 3. Accepting this as plan-of-record rather than acceleration removes pressure from Weeks 2–3 with zero revenue loss inside the sprint window.

---

## Section 8: Gantt Timeline — June 22–July 13 (22-Day Sprint)

### ASCII Gantt — Sprint Window

```
SEEDWARDEN PHASE 3 — GANTT TIMELINE
Dates:     Jun22 23 24 25 26 27 28 | Jun29 30 Jul1  2  3  4  5 | Jul6  7  8  9 10 11 12 13
           [====WEEK 1=============] [====WEEK 2================] [====WEEK 3=============]
───────────────────────────────────────────────────────────────────────────────────────────
WRITING
WH Guide   [D1===D2===D3==========]  .                           .
Resp Guide              [D4===D5===D6===D7=]                     .
Imm Guide  .            .            [D8===D9===D10===D11========] .
Sleep      .            .                     [D12===D13===D14===] .
Digestive  .            .            .                            [D15===D16===D17]
FTC Review .            .            .                            .         [D18]
SEO Pass   .            .            .                            .              [D19]
───────────────────────────────────────────────────────────────────────────────────────────
DESIGN
Brand Test [D1!]        .            .                            .
WH Cover      [D2]      .            .                            .
Resp Cover       [D3]   .            .                            .
Imm Cover  .         .  [D8]         .                            .
Slp Cover  .         .     [D9]      .                            .
WH ZoneCard.         .        [D10]  .                            .
Resp ZCard .         .           [D11]                            .
Dgt Cover  .         .                [D12]                       .
LOCK!      .         .                [D12! EOD Jul3]             .
Imm/Slp/Dgt ZCards .  .                                 [D15][D16] .
Practitioner Cover .   .                                   [D17]   .
Final Export.          .                                       [D19].
───────────────────────────────────────────────────────────────────────────────────────────
PHOTOGRAPHY (in-sprint studio only — pre-sprint track runs May 26–June 21)
Studio1    .  [D2]      .            .                            .   Calendula + Red Clover
Studio2    .     [D3]   .            .                            .   Lavender + Lemon Balm
Studio3    .        [D4].            .                            .   Dried herb props
EditCull   .           [D5]          .                            .   2-day float
───────────────────────────────────────────────────────────────────────────────────────────
UPLOAD
WH Upload  .            .            [*D8 Jun29]                  .
Resp Upload.            .            .                            [*D15 Jul6-7]
Sleep Upload.           .            .                            .             [*D22 Jul13]
───────────────────────────────────────────────────────────────────────────────────────────
FLOAT
Float D1   .            .            .                            .           [--D21 Jul12]
Float D2   .            .            .                            .                 [--D22]
───────────────────────────────────────────────────────────────────────────────────────────
POST-SPRINT →                                             Jul20: [*Imm] | Aug3: [*Dgt]

CRITICAL PATH (zero-float activities; delay here directly delays upload milestones):
  Jun 8 ──→ Jun 22 ──→ Jun 24 ──→ Jun 28 ──→ Jun 29 ──→ Jul 6-7 ──→ Jul 13
  Supplier   Sprint     WH writing  WH PDF     WH live    Resp        Sleep
  deadline   start      complete    export     on Etsy    upload      upload
```

### Float Analysis

| Activity | Float Days | Notes |
|---|---|---|
| Props acquisition | 14 days | Non-blocking; can compress to 1 order day |
| Seedling photography | 10 days | Very flexible; seeds germinate fast |
| Mature/flowering photography | 5 days | Delivery timing governs window |
| Dried herb studio session | 1 day | Mountain Rose Herbs order date governs |
| WH cover design | 4 days | Needs hero photo; floats with photo track |
| Respiratory cover design | 4 days | Same dependency |
| Immunity cover design | 4 days | Design lock is July 3 |
| Sleep cover design | 3 days | Same design lock |
| Zone cards (all 5) | 8 days | No upload dependency; pure float |
| FTC review pass | 2 days | Before SEO pass |
| SEO optimization pass | 2 days | Before final PDF export |
| Float Day 1 | 8 hours | Explicit buffer for writing overrun |
| Float Day 2 | 4 hours | Post-Sleep-upload retrospective |
| **Women's Health writing** | **0 days** | **CRITICAL PATH — determines June 29 upload** |
| **Respiratory writing** | **0 days** | **CRITICAL PATH — determines July 6–7 upload** |
| **Immunity writing** | **0 days** | **CRITICAL PATH — determines July 20 upload** |

### Pre-Sprint Hard Deadlines

| Date | Event | Float | Consequence of Miss |
|---|---|---|---|
| June 8 | Goldenseal order OR CC path confirmed | 0 days | Photo path for Immunity unresolved going into sprint |
| June 15 | Elderberry order | 0 days | Local nursery backup available at added cost |
| June 15 | Mountain Rose Herbs dried herbs ordered | 5 days | Frontier Co-op backup at 3–5 day ship |
| June 15 | Palette hex codes finalized | 6 days | Post-production palette change = 1.2 hrs rework per cover |
| June 21 | Canva brand kit pre-test complete | 1 day | Sprint Day 1 design blocked if palette not loaded |
| June 21 | Attribution log complete for all pre-sprint sourced images | 0 days | WORKLOG.md protocol requires logging before file use in guides |

### Worst-Case Recovery Analysis

**Scenario A — Writing slips 5 days** (Women's Health complete July 2 instead of June 27):

| Event | Nominal | Slipped | Net Shift |
|---|---|---|---|
| Women's Health writing complete | June 28 | July 3 | +5 days |
| Women's Health upload | June 29 | July 4 | +5 days |
| Respiratory upload | July 6–7 | July 11–12 | +5 days |
| Sleep upload | July 13 | July 18 | +5 days |
| Immunity upload | July 20 | July 25 | +5 days |
| All 5 bundles live | August 3 | August 8 | **+5 days** |

All bundles live before August 15. Holiday review accumulation window fully preserved.

**Scenario B — Writing slips 10 days** (activate Option C 3-bundle scope):

| Event | Option A | Option C | Net Shift |
|---|---|---|---|
| Women's Health upload | June 29 | June 29 | 0 |
| Respiratory upload | July 6–7 | July 6–7 | 0 |
| Sleep upload | July 13 | July 13 | 0 |
| Immunity upload | July 20 | August 3 | +14 days |
| Digestive upload | August 3 | August 17 | +14 days |
| All 5 bundles live | August 3 | **August 17** | **+14 days** |

First three listings upload on the same dates. Holiday review accumulation window preserved for both Immunity and Digestive at 14 days later.

---

## Section 9: Sprint Completion Checklist (July 13)

At sprint end, confirm:
- [ ] Women's Health live on Etsy (uploaded June 29 or July 3 worst-case)
- [ ] Respiratory live on Etsy (uploaded July 6–7 or July 11)
- [ ] Sleep and Nervines live on Etsy (uploaded July 13 or July 16)
- [ ] Immunity PDF ready, listing drafted, queued for July 20
- [ ] Digestive PDF ready, listing drafted, queued for August 3
- [ ] All 5 Canva covers + zone cards complete and exported
- [ ] Practitioner 10-pack PDFs (5 bundles × practitioner license page) staged for upload
- [ ] All photo attributions logged in WORKLOG.md
- [ ] Kit herbalist tags active (7 tags per bundle email sequence)
- [ ] Phase 3 KPI spreadsheet initialized (views, CTR, conversion per listing)
- [ ] WORKLOG.md sprint retrospective entry: pace, bottlenecks, supplier status, float used
- [ ] Peer review confirmations on file: Women's Health (AHG contact), Immunity (ND/RH CITES review)

---

## Appendix A: Three May 30 Decisions — Decision Format

**Decision 1 — Sprint Scope**

| Option | Description | Risk Level | Recommended For |
|---|---|---|---|
| A — Single writer, 5 bundles, 5 hrs/day | June 22–July 13; 56–66 adjusted hours writing | Medium | User with confirmed 5 hrs/day June 22–July 10 |
| B — Two parallel writers | June 22–July 5; 5 bundles in 14 days | Low | User with trusted herbalist writer contact available by May 25 |
| C — 3-bundle priority launch (recommended) | WH + Resp + Sleep in sprint; Immunity + Digestive in August | Very Low | User uncertain about June capacity; managing Phase 2 post-launch monitoring |

**Decision 2 — Goldenseal Path**

- Path 1: Order live specimen from Prairie Moon or Strictly Medicinal by June 8. Arrives July 13–20. Enables live specimen photography for v1.1 update.
- Path 2 (recommended under Option C): Commit to Wikimedia CC + NC Botanical Garden outreach. Zero cost. Zero production risk. Confirmed sufficient for launch quality.

**Decision 3 — Second Writer**

- Yes: Send briefing package (`PHASE_3_BUNDLE_CONTENT_OUTLINE_DETAILED.md` + `phase-3-medicinal-herbs-sourcing-guide.md`) by May 25. Writer begins June 22, parallel track. Writer handles Respiratory + Immunity; primary writer handles Women's Health + Sleep + Digestive.
- No: Confirm single-writer capacity for Option A before May 30.

---

## Appendix B: FTC Language Quick Reference

All medicinal herb guides must use the following approved framing. Failure to comply creates product liability exposure on Etsy.

| Claim Type | Approved Framing | NOT Permitted |
|---|---|---|
| Traditional use | "Traditionally used in [specific tradition] for [historical purpose]" | "Treats," "cures," "prevents" + disease name |
| Research reference | "Studied in randomized controlled trials for [general outcome area]" | "Proven to," "clinically proven," "effective for" |
| Mechanism description | "Contains [compound], a substance studied in relation to [mechanism]" | "Works by," "boosts," "enhances" immune function |
| Supplement connection | "Used as [preparation type] in traditional herbalism" | "Equivalent to a prescription," dosing claims |
| Safety information | "Individuals with [condition] should consult a healthcare provider" | Omitting contraindications for any at-risk species |

**Goldenseal CITES mandatory sidebar** (required in every Goldenseal section): "Goldenseal (*Hydrastis canadensis*) is listed in CITES Appendix II. International trade in wild-harvested material requires export permits. This guide recommends cultivated sources only."

**Ashwagandha pregnancy/thyroid warning** (mandatory): "Individuals who are pregnant, breastfeeding, or managing a thyroid condition should consult a qualified healthcare provider before using ashwagandha preparations."

**Sleep bundle drug interaction warning** (mandatory for all four species): "This herb has traditionally been used for sleep and relaxation. Individuals taking prescription sedatives, benzodiazepines, or sleep medications should consult a healthcare provider before use."

---

## Appendix C: Supplier Contacts

| Supplier | Species | Contact | Notes |
|---|---|---|---|
| Prairie Moon Nursery | Goldenseal, Black Cohosh, Elderberry, Passionflower, Valerian, Echinacea | info@prairiemoon.com; 866-417-8156 | Goldenseal limited stock; order early |
| Strictly Medicinal Seeds | Goldenseal, Black Cohosh, Ashwagandha, Ginger, Echinacea | strictlymedicinalseeds.com | USDA Organic options; wide herb selection |
| Mountain Rose Herbs | Dried bulk herbs (all 13 species) | wholesale@mountainroseherbs.com | Request CoA for Goldenseal cultivated origin |
| Frontier Co-op | Dried bulk herbs (all species) | frontiercoop.com | 3–5 day emergency ship; wholesale pricing |
| NC Botanical Garden | Goldenseal photo license | media@ncbg.unc.edu | Educational use; reply typically 3–5 business days |
| Missouri Botanical Garden | Goldenseal photo license | media@mobot.org | Educational use; request herbarium specimen images |

---

*Document: PHASE_3_MEDICINAL_HERBS_CRITICAL_PATH.md — v3.0*
*Prepared: May 20, 2026. Seedwarden Agent.*
*Supersedes: v2.0 (May 19, 2026).*
*Companion files: phase-3-medicinal-herbs-gantt-timeline.md, phase-3-medicinal-herbs-gantt-timeline.csv.*
*Next review dates: June 8, 2026 (Goldenseal order deadline); June 22, 2026 (sprint launch confirmation).*
