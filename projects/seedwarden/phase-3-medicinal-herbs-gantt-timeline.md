---
title: "Phase 3 Medicinal Herbs — Gantt Timeline (June 22–July 13)"
date: 2026-05-20
version: 2.0
status: production-ready
phase: Phase 3 pre-execution
execution-window: June 22 – July 13, 2026 (22 calendar days)
companion-document: phase-3-medicinal-herbs-critical-path.md
tags: [seedwarden, phase-3, gantt, timeline, critical-path, medicinal-herbs]
---

# Phase 3 Medicinal Herbs — Gantt Timeline (June 22–July 13)

**Execution window**: June 22 – July 13, 2026 (22 calendar days)
**Total resource allocation**: 56–66 hours writing + 12.5 hours design + 10 hours upload admin = 78–88 hours
**Critical path summary**: Writing determines all upload dates. Design and photography have float. Three upload milestones — June 29, July 6–7, July 13 — are the sprint's hard delivery events.

---

## Legend

```
[=====]   Active task (writing, design, photography, admin)
[--]      Float (slack — can slip without affecting upload milestones)
[*]       Upload milestone (Etsy listing goes live)
[!]       Hard deadline (zero float — missing this delays all downstream events)
CRIT      On the critical path (zero float; delay directly delays upload)
FLOAT     Off the critical path (has slack; can be moved without cascade)
```

---

## Pre-Sprint Timeline (May 26–June 21)

The pre-sprint window runs from now through the day before sprint start. These activities do not compete with sprint writing time. The single most important pre-sprint action is placing Goldenseal and Black Cohosh orders by June 8. Every other pre-sprint task can slip by 1–2 weeks without blocking June 22.

```
PRE-SPRINT: May 26 → June 21
─────────────────────────────────────────────────────────────────────────────
         May26    Jun1    Jun8    Jun15   Jun21
           │        │       │       │       │
SUPPLIER   │        │       │       │       │
  Goldenseal────────[!ORDER Jun8]───────────│  → arrives ~Jul13–20
  BlackCohosh───────[!ORDER Jun8]───────────│  → arrives ~Jul13–20
  Elderberry────────────────[!ORDER Jun15]──│  → arrives ~Jul13–20
  MountainRose───────────────[ORDER Jun15]──│  (dried herbs, studio)
  Tier3_all ─────────────────────────────[Jun22] (sprint-start day orders)

PHOTOGRAPHY │        │       │       │       │
  Props     [== May26–Jun2 ==]│       │       │  7-day float FLOAT
  Seedlings │     [== Jun3–9 ==]      │       │  10-day float FLOAT
  Mature/Flwr│               [=Jun10–16=]    │  5-day float FLOAT
  DriedStudio│               │[= Jun17–21 =] │  1-day float FLOAT
  EditCull   │               │   [Jun19–21]  │  1-day float FLOAT
  Attribution│               │              [!Jun21] 0-day float CRIT

DESIGN     │        │       │       │       │
  BrandKitTest────────────────────────────[!Jun21] (palette must load before D1)
  PaletteDec ────────────────[!Jun15]──────│  PALETTE DECISION DEADLINE CRIT
─────────────────────────────────────────────────────────────────────────────
```

**Pre-sprint hard deadlines**:

| Date | Event | Float | Consequence of Miss |
|---|---|---|---|
| June 8 | Goldenseal + Black Cohosh order placed OR CC path confirmed in writing | **0 days** | Photo path for Immunity bundle is unresolved going into sprint; must be decided before Day 1 |
| June 15 | Elderberry order placed | 0 days | Local nursery backup available by June 22 at added cost |
| June 15 | Mountain Rose Herbs dried herbs ordered | 5 days | Frontier Co-op backup at 3–5 day ship |
| June 15 | Palette hex codes finalized | 6 days before cover design starts | Each post-production palette change = 1.2 hours rework per affected cover |
| June 21 | Canva brand kit pre-test (palette loaded, one zone card verified) | 1 day | Sprint Day 1 design is blocked if palette not loaded |
| June 21 | Attribution logging complete for all sourced pre-sprint images | 0 days | WORKLOG.md protocol requires logging before file use in guides |

---

## Sprint Gantt — 22-Day Execution Window (June 22–July 13)

```
SPRINT: June 22 → July 13
Dates:      22  23  24  25  26  27  28 │ 29  30 Jul1   2   3   4   5 │  6   7   8   9  10  11  12  13
            [======= WEEK 1 =========] │ [======== WEEK 2 ===========] │ [======== WEEK 3 ===========]
────────────────────────────────────────┼────────────────────────────────┼─────────────────────────────────
WRITING                                 │                                │
  WH Guide  [D1  D2  D3]               │                                │   15 hrs → DONE Jun 24 CRIT
  Resp Guide             [D4  D5  D6-D7]│                               │  +16 hrs → DONE Jun 27 CRIT
  Imm Guide              .              │[D8  D9  D10 D11]               │  +18 hrs → DONE Jul 2  CRIT
  Sleep      .           .              │            [D12 D13 D14]       │  +12 hrs → DONE Jul 5  FLOAT
  Digestive  .           .              │                                │[D15 D16 D17]
  FTC Review .           .              │                                │         [D18]              FLOAT
  SEO Pass   .           .              │                                │             [D19]           FLOAT
────────────────────────────────────────┼────────────────────────────────┼─────────────────────────────────
DESIGN                                  │                                │
  BrandKit  [D1!]        .              │                                │   4-day float FLOAT
  WH Cover      [D2]     .              │                                │   4-day float FLOAT
  Resp Cover        [D3] .              │                                │   4-day float FLOAT
  Imm Cover  .           .              │[D8]                            │   4-day float FLOAT
  Sleep Cover.           .              │    [D9]                        │   3-day float FLOAT
  WH ZoneCard.           .              │        [D10]                   │   4-day float FLOAT
  Resp ZoneC .           .              │            [D11]               │   4-day float FLOAT
  Dgt Cover  .           .              │                [D12]           │   0-day float CRIT (design lock)
  [LOCK! Jul3]           .              │                [!Jul3 EOD]     │
  Imm ZoneC  .           .              │                                │[D15]           2-day float FLOAT
  Slp ZoneC  .           .              │                                │    [D16]       2-day float FLOAT
  Dgt ZoneC  .           .              │                                │[D15]           2-day float FLOAT
  ExportTest .           .              │                                │    [D16]       2-day float FLOAT
────────────────────────────────────────┼────────────────────────────────┼─────────────────────────────────
PHOTOGRAPHY                             │                                │
  Studio1    .   [D2]    .              │                                │   Calendula, Red Clover seedling
  Studio2    .       [D3].              │                                │   Lavender, Lemon Balm, Thyme
  Studio3    .           [D4]           │                                │   Dried herb Immunity props
  EditCull   .               [D5]       │                                │   2-day float FLOAT
────────────────────────────────────────┼────────────────────────────────┼─────────────────────────────────
UPLOAD                                  │                                │
  WH Upload  .           .              │[*D8 Jun29]                     │   7-day spacing → CRIT
  Resp Upload.           .              │                                │[*D15 Jul6-7]     CRIT
  Sleep Upload.          .              │                                │              [*D22 Jul13] CRIT
────────────────────────────────────────┼────────────────────────────────┼─────────────────────────────────
FLOAT                                   │                                │
  FloatDay1  .           .              │                                │            [--D21 Jul12] 8 hrs
  FloatDay2  .           .              │                                │                  [--D22] 4 hrs
────────────────────────────────────────┼────────────────────────────────┼─────────────────────────────────
POST-SPRINT →                                                                     Jul20:[*Imm] | Aug3:[*Dgt]
```

---

## Critical Path Highlighted

The critical path is the sequence of tasks with zero float. Any delay on a critical path task directly delays the corresponding upload milestone. The critical path in Phase 3 is entirely driven by writing — specifically, the three sequenced writing blocks that feed the three upload milestones within the sprint window.

```
CRITICAL PATH CHAIN — June 22 to July 13

[June 8]        [June 22]       [June 24]      [June 28]      [June 29]
Goldenseal  ──► Sprint     ──► WH Writing ──► WH PDF    ──► WH Upload
Photo Path      Starts          Complete        Export          LIVE
(photo; not                        │
writing gate)                       │
                                    │ (concurrent, not blocking)
                [June 25]       [June 27]      [July 6–7]
                Respiratory ──► Resp PDF  ──► Resp Upload
                Writing         Export          LIVE
                Starts                            │
                                                  │ (concurrent, not blocking)
                [June 29]       [July 5]       [July 13]
                Immunity    ──► Sleep PDF  ──► Sleep Upload
                Writing         Export          LIVE
                Starts
```

**Why Goldenseal is on the pre-sprint critical path but NOT on the writing critical path**: Goldenseal photography (photo source decision) must be resolved by June 8 to avoid an unresolved attribution question going into the sprint. However, guide writing for Immunity does not begin until June 29 (Day 8) and does not require live specimens — the content is written from the research compiled in `phase-3-medicinal-herbs-content-outline.md`. The Goldenseal June 8 deadline gates photography quality, not writing quality.

---

## Float Days Identified

Float represents scheduling slack — tasks that can slip without delaying upload milestones.

### High-Float Activities (Can Slip 4+ Days Without Impact)

| Activity | Scheduled Date | Latest Start | Float | Notes |
|---|---|---|---|---|
| Props acquisition | May 26 | June 8 | 14 days | Non-blocking; can compress to one order |
| Seedling photography | June 3 | June 15 | 12 days | Annual seeds germinate fast; very flexible |
| Mature/flowering photography | June 10 | June 21 | 11 days | Delivery timing governs window |
| Women's Health cover design | June 23 | June 27 | 4 days | Floats with writing track; design lock is July 3 |
| Respiratory cover design | June 24 | June 28 | 4 days | Same design lock |
| Zone cards (all 5) | July 1 | July 9 | 8 days | No upload dependency |
| FTC review pass | July 9 | July 11 | 2 days | Can compress to July 10 if Week 3 writing runs long |
| SEO optimization pass | July 10 | July 12 | 2 days | Before final PDF export; 2-day float |

### Zero-Float Activities (Critical Path — Miss = Milestone Delay)

| Activity | Scheduled Date | Consequence of 1-Day Slip |
|---|---|---|
| Women's Health writing complete | June 24–28 | Women's Health upload shifts from June 29 to June 30+; compresses Respiratory spacing |
| Women's Health PDF export | June 28 | Blocks Women's Health upload; cannot upload without exported PDF |
| Women's Health upload | June 29 | Opens first Etsy discovery window; delays compress all subsequent spacing |
| Respiratory writing complete | June 27–28 | Respiratory upload shifts from July 6–7; compresses Sleep spacing |
| Respiratory upload | July 6–7 | 7-day spacing from Women's Health; compressing harms both listings' momentum |
| Digestive cover design | July 3 | This is the design lock date; post-lock changes consume Week 3 writing time |
| Sleep upload | July 13 | End of sprint window; 7-day spacing from Respiratory |

**Float Day 1 (July 12)**: 8 hours available. Absorbs writing overrun from any single Week 3 day. If Days 15–19 run on schedule, this day frees up for early Sleep upload staging.

**Float Day 2 (July 13)**: 4 hours available after Sleep upload (2 hours). Available for sprint retrospective and WORKLOG.md update.

---

## Dependencies Clearly Marked

### Upstream → Downstream Dependencies

```
DEPENDENCY MAP

Palette decision (Jun 15)
    └──► Brand kit loaded (Jun 21)
             └──► Cover design sessions (Jun 23 onward)
                      └──► Design lock (Jul 3)
                               └──► Zone cards + export (Jul 6–7)
                                        └──► Final PDF exports (Jul 10)

WH writing complete (Jun 24–28)
    └──► WH PDF export (Jun 28)
             └──► WH upload (Jun 29) [CRIT]
                      └──► 7-day spacing
                               └──► Resp upload (Jul 6–7) [CRIT]
                                        └──► 7-day spacing
                                                 └──► Sleep upload (Jul 13) [CRIT]

Resp writing complete (Jun 27–28)
    └──► Resp PDF export (Jun 28)
             └──► Resp upload (Jul 6–7) [CRIT]

Imm writing complete (Jul 2)
    └──► Imm PDF export (Jul 10 with all bundles)
             └──► Imm upload (Jul 20) [post-sprint]

Sleep writing complete (Jul 5)
    └──► Sleep PDF export (Jul 10 with all bundles)
             └──► Sleep upload (Jul 13) [CRIT] or July 20 [contingency]

Digestive writing complete (Jul 8)
    └──► Dgt PDF export (Jul 10 with all bundles)
             └──► Dgt upload (Aug 3) [post-sprint]

Supplier orders (Jun 8)
    └──► Plant arrival (Jul 13–20)
             └──► Live specimen photography (post-sprint, v1.1)
             [NOT a dependency for writing or design — parallel path]

Mountain Rose Herbs order (Jun 15)
    └──► Dried herb delivery (Jun 17–21)
             └──► Dried studio photography (Jun 17–21)
                      └──► Studio photos available for cover design (Jun 23+)
```

### Cross-Bundle Writing Dependencies

The shared species create a specific dependency: second-occurrence sections cannot be started until the first-occurrence section is drafted. The framing shift requires reading what was written for the first bundle.

| Shared Species | First Bundle (write first) | Second Bundle (write second) | Dependency |
|---|---|---|---|
| Lavender | Women's Health (D3, June 24) | Sleep and Nervines (D14, July 5) | Sleep lavender section reframes aromatherapy/linalool angle; requires reading Women's Health lavender section first |
| Echinacea | Respiratory Health (D5, June 26) | Immunity Support (D8, June 29) | Immunity section condenses cultivation and adds immunity framing; requires reading Respiratory two-species section first |
| Elderberry | Respiratory Health (D4, June 25) | Immunity Support (D10, July 1) | Immunity section adds fermentation note; requires reading Respiratory elderberry section first |
| Calendula | Women's Health (D3, June 24) | Digestive Support (D16, July 7) | Digestive section shifts from salve/oil to tea/infusion; requires reading Women's Health section first |
| Lemon Balm | Sleep and Nervines (D14, July 5) | Digestive Support (D16, July 7) | Digestive shifts from nervine to carminative framing; requires reading Sleep section first |

---

## Risk Mitigation Checkpoints

Three formal checkpoints during the sprint. At each checkpoint, evaluate actual progress against the pace targets below and activate contingencies if triggers are met.

### Checkpoint 1: June 30 Milestone

**What to verify**:
- Women's Health (3,800 words): Complete and export-ready. Uploaded to Etsy June 29. If not uploaded: check if PDF export is the blocker or if writing is incomplete. If writing is incomplete and today is June 30, activate Contingency 2 (Option C scope reduction) immediately.
- Respiratory (3,600 words): Writing complete or within 2 hours of completion by June 30 EOD.
- Immunity: Introduction + Echinacea condensed section complete (approximately 1,200 words). If Immunity is not started, Week 2 is already running behind.
- Design: Women's Health cover and Respiratory cover complete. Immunity and Sleep covers in progress or scheduled.
- Photography: Studio batch Days 1–3 complete (June 23–25). Edit/cull complete (June 26).

**Contingency trigger at June 30**:
- Women's Health not uploaded by June 30 EOD: Activate upload date slip. New Women's Health upload date: July 3. Respiratory shifts to July 10. Sleep shifts to July 17. No scope reduction required — just date slip.
- Immunity writing not started by June 30 AM: Evaluate Option C seriously. If Option A is still the chosen path, Immunity must catch up by July 3 (Design lock day doubles as writing pressure point).

**June 30 green condition**: Women's Health live on Etsy, Respiratory complete, Immunity writing started, design 2 of 5 covers done.

---

### Checkpoint 2: July 7 Milestone

**What to verify**:
- Respiratory: Uploaded to Etsy July 6–7. If not uploaded and today is July 7, check PDF readiness. Respiratory upload can slip to July 11 (Day 20) with Sleep uploading July 13 intact — this costs only 4 days of Respiratory discovery window.
- Immunity (3,800 words): Complete and export-ready by July 5 EOD. If Immunity is not complete at July 7 check-in, push Immunity upload from July 20 to July 27.
- Sleep (3,500 words): Writing complete by July 5, self-edited by July 7. Sleep upload is July 13 — 6 days of float remain.
- Digestive: Introduction + Dandelion section (900 words) complete by July 6 EOD. Digestive must reach approximately 1,500 words by July 7 for the August 3 upload to remain on track.
- Design: All 5 covers complete (design lock was July 3). Zone cards 1–3 complete. Zone cards 4–5 in progress.
- FTC review: Not started yet (scheduled July 9). No contingency required unless writing is not complete.

**Contingency trigger at July 7**:
- Sleep writing not complete at July 7: Sleep upload shifts from July 13 to July 16 (3-day slip, still before Immunity's July 20 upload date). No cascade impact.
- Digestive writing below 1,500 words at July 7: Digestive upload shifts from August 3 to August 10. No cascade impact on any other bundle.
- Fewer than 3 bundles written and export-ready at July 7: Activate Contingency 5 (minimum viable launch). Prioritize Women's Health + Sleep + Respiratory for July 13.

**July 7 green condition**: Respiratory live on Etsy, Immunity and Sleep writing complete, Digestive writing at 1,500+ words, all 5 covers complete.

---

### Checkpoint 3: July 13 Hard Launch Date

**What to verify**:
- Sleep and Nervines: Uploaded to Etsy July 13. This is the sprint's hard delivery event — the third listing upload that defines sprint completion.
- All 5 bundle PDFs: Export-ready (under 5MB, no placeholders, attribution complete) regardless of upload date.
- Immunity: PDF staged, Etsy listing drafted, queued for July 20. No writing or design work remaining.
- Digestive: PDF staged, Etsy listing drafted, queued for August 3. No writing or design work remaining.
- WORKLOG.md: Sprint retrospective entry written. Includes pace note, float used, supplier status, photo source log for all 14 unique species.

**July 13 sprint completion checklist**:
- [ ] Women's Health live on Etsy (uploaded June 29 or July 3 worst-case)
- [ ] Respiratory live on Etsy (uploaded July 6–7 or July 11)
- [ ] Sleep and Nervines live on Etsy (uploaded July 13 or July 16)
- [ ] Immunity PDF ready and listing queued for July 20
- [ ] Digestive PDF ready and listing queued for August 3
- [ ] All 5 Canva covers exported at final resolution
- [ ] All 5 zone cards exported
- [ ] All photo attributions logged in WORKLOG.md
- [ ] Practitioner 10-pack variants (5 bundles × practitioner license page) staged for upload
- [ ] Phase 3 KPI spreadsheet initialized (views, CTR, conversion per listing)
- [ ] WORKLOG.md sprint retrospective entry: pace, bottlenecks, supplier status, float used

---

## Daily Milestone Reference Table

| Day | Date | Track | Task | Hours | Float | Critical Path? |
|---|---|---|---|---|---|---|
| Pre | Jun 8 | SUPPLIER | Goldenseal + Black Cohosh order deadline | 0.5 | **0 days** | **YES** |
| Pre | Jun 15 | SUPPLIER | Elderberry + Mountain Rose Herbs order deadline | 0.5 | **0 days** | **YES** |
| Pre | Jun 15 | DESIGN | Palette decision deadline | 0 | 6 days to Jun 21 | CRIT if undecided |
| Pre | Jun 21 | DESIGN | Canva brand kit palette loaded + pre-test | 0.5 | 1 day | CRIT |
| D1 | Jun 22 | WRITE | WH: Front matter + Introduction + Black Cohosh | 5 | 1 day | CRIT |
| D2 | Jun 23 | WRITE + PHOTO | WH: Vitex + Red Clover; Studio batch: Calendula + Red Clover | 5 + 2 | 1 day | CRIT |
| D3 | Jun 24 | WRITE + DESIGN + PHOTO | WH: Calendula + Lavender + shared sections; WH cover; Studio batch: Lavender + Lemon Balm | 5 + 1.2 + 3 | 0 days | **CRIT — WH complete by Jun 28** |
| D4 | Jun 25 | WRITE + DESIGN + PHOTO | Resp: Intro + Elderberry; Resp cover; Studio batch: dried herb Immunity props | 5 + 1.2 + 3 | 1 day | CRIT |
| D5 | Jun 26 | WRITE + PHOTO | Resp: Mullein + Echinacea; Studio edit/cull | 5 + 2 | 1 day | CRIT |
| D6 | Jun 27 | WRITE | Resp: Thyme + shared sections + WH self-edit | 4 | 2 days | No |
| D7 | Jun 28 | WRITE | Resp self-edit + WH PDF export test + Week 2 prep | 2 | 2 days | No |
| D8 | Jun 29 | UPLOAD + WRITE | **[MILESTONE] WH uploaded**; Imm: Intro + Echinacea condensed | 2 + 3 | 1 day | **YES** |
| D9 | Jun 30 | WRITE + DESIGN | Imm: Ashwagandha complete (900 words); Imm cover | 5 + 1.2 | 1 day | CRIT |
| D10 | Jul 1 | WRITE + DESIGN | Imm: Elderberry condensed + Goldenseal intro + CITES sidebar; WH zone card | 5 + 0.8 | 1 day | CRIT |
| D11 | Jul 2 | WRITE + DESIGN | Imm: Goldenseal cultivation + FGV + active constituents + shared sections; Resp zone card | 5 + 0.8 | 1 day | CRIT |
| D12 | Jul 3 | WRITE + DESIGN | Sleep: Intro + Valerian; Digestive cover; **DESIGN LOCK EOD** | 4 + 1.2 | 1 day | CRIT (design lock) |
| D13 | Jul 4 | WRITE | Sleep: Passionflower complete | 4 | 2 days | No |
| D14 | Jul 5 | WRITE | Sleep: Lemon Balm condensed + Lavender condensed + shared sections + self-edit | 4 | 2 days | No |
| D15 | Jul 6 | UPLOAD + WRITE + DESIGN | **[MILESTONE] Resp uploaded**; Digestive: Intro + Dandelion (900 words); Imm + Dgt zone cards | 2 + 5 + 1.6 | 1 day | **YES** |
| D16 | Jul 7 | WRITE + DESIGN | Digestive: Calendula + Lemon Balm + shared sections; Sleep zone card; Export test | 4 + 1.6 | 1 day | No |
| D17 | Jul 8 | WRITE | Digestive: Ginger complete; Digestive self-edit | 4 | 2 days | No |
| D18 | Jul 9 | REVIEW | FTC language compliance review all 5 bundles; contraindications accuracy; sources | 3 | 2 days | No |
| D19 | Jul 10 | REVIEW + UPLOAD PREP | SEO pass; PDF export all 5 bundles; tags/title QA | 2 + 2 | 1 day | No |
| D20 | Jul 11 | UPLOAD PREP | File naming; practitioner variant staging; Sleep listing QA | 2 | 1 day | No |
| D21 | Jul 12 | FLOAT | Float Day 1 — absorb overrun or Sleep upload staging | 0–4 | **8 hours float** | No |
| D22 | Jul 13 | UPLOAD + FLOAT | **[MILESTONE] Sleep uploaded**; Sprint retrospective; WORKLOG.md | 2 + 2 | 4 hours | **YES** |
| Post | Jul 20 | UPLOAD | Immunity Support uploaded | 2 | — | — |
| Post | Aug 3 | UPLOAD | Digestive Support uploaded | 2 | — | — |

---

## Worst-Case Recovery Paths

### If Writing Slips 5 Days (July 20 Contingency Path)

A 5-day writing overrun shifts Women's Health from June 28 complete to July 3 complete. All downstream dates shift by 3–4 days at most. The full 5-bundle launch date shifts from August 3 to August 6–7. The holiday review accumulation window is fully preserved.

| Event | Nominal Date | Slipped Date (5-day overrun) | Net Shift |
|---|---|---|---|
| Women's Health writing complete | June 28 | July 3 | +5 days |
| Women's Health upload | June 29 | July 4 | +5 days |
| Respiratory upload | July 6–7 | July 11–12 | +5 days |
| Sleep upload | July 13 | July 18 | +5 days |
| Immunity upload | July 20 | July 25 | +5 days |
| Digestive upload | August 3 | August 8 | +5 days |
| All 5 bundles live | August 3 | **August 8** | **+5 days** |

A 5-day writing slip results in a 5-day slip in the final launch date. All bundles remain live before August 15. The upload sequence spacing (7 days Women's Health → Respiratory → Sleep, 7 days to Immunity, 14 days to Digestive) is fully preserved.

### If Writing Slips 10 Days (Option C 3-Bundle Scope Activation)

Activating Option C (3-bundle priority): Women's Health + Respiratory + Sleep complete by July 13. Immunity writing begins July 14. Digestive writing begins July 22.

| Event | Option A Date | Option C Date | Net Slip |
|---|---|---|---|
| Women's Health upload | June 29 | June 29 (unchanged) | 0 |
| Respiratory upload | July 6–7 | July 6–7 (unchanged) | 0 |
| Sleep upload | July 13 | July 13 (unchanged) | 0 |
| Immunity upload | July 20 | August 3 | +14 days |
| Digestive upload | August 3 | August 17 | +14 days |
| All 5 bundles live | August 3 | **August 17** | **+14 days** |

The first three listings (Women's Health, Respiratory, Sleep) upload on the same dates. The 14-day slip on Immunity and Digestive does not affect the holiday review accumulation window — both bundles have 3+ months before the November–December peak.

---

## Gate and Milestone Summary

| Date | Event | Type | Float | Status |
|---|---|---|---|---|
| NOW (21.3%) | Forager cohort >20% | Launch gate | — | **CLEARED** |
| NOW (2.24%) | Native Plants conversion >1.5% | Launch gate | — | **CLEARED** |
| May 30 | Scope decision (A/B/C) | User decision | 0 days | Pending |
| June 8 | Goldenseal order OR CC path confirmed | Supplier deadline | 0 days | Pending |
| June 8 | Black Cohosh order | Supplier deadline | 0 days | Pending |
| June 15 | Elderberry order | Supplier deadline | 0 days | Pending |
| June 15 | Palette finalized | Design decision | 6 days | Pending |
| June 21 | Brand kit loaded + pre-tested | Design execution | 1 day | Pending |
| June 22 | Sprint starts | Execution gate | — | Pending |
| June 29 | Women's Health live on Etsy | Upload milestone | 0 days (critical path) | Pending |
| June 30 | Checkpoint 1 review | Pace verification | — | Pending |
| July 3 | Design lock | Design gate | 0 days | Pending |
| July 6–7 | Respiratory live on Etsy | Upload milestone | 0 days (critical path) | Pending |
| July 7 | Checkpoint 2 review | Pace verification | — | Pending |
| July 13 | Sleep live on Etsy | Upload milestone | 0 days (hard launch date) | Pending |
| July 13 | Checkpoint 3 + sprint retrospective | Sprint close | 4 hours float | Pending |
| July 20 | Immunity live on Etsy | Post-sprint upload | — | Pending |
| August 3 | Digestive live on Etsy | Post-sprint upload | — | Pending |

---

*Document prepared: May 20, 2026 (v2.0).*
*Seedwarden Agent. Companion document: phase-3-medicinal-herbs-critical-path.md.*
*Next review: June 22, 2026 (sprint launch).*
