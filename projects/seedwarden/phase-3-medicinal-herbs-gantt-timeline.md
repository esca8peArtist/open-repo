---
title: "Phase 3 Medicinal Herbs — Gantt Timeline and Resource Allocation"
date: 2026-05-19
status: production-ready
phase: Phase 3 pre-execution
scope: June 22 – July 13, 2026 (22-day execution window) + pre-sprint (May 26–June 21) + post-sprint (July 14–August 3)
cross-references:
  - PHASE_3_MEDICINAL_HERBS_CRITICAL_PATH.md
  - phase-3-medicinal-herbs-content-outline.md
  - phase-3-medicinal-herbs-sourcing-guide.md
tags: [seedwarden, phase-3, gantt, timeline, resource-allocation, medicinal-herbs]
---

# Phase 3 Medicinal Herbs — Gantt Timeline and Resource Allocation

**Prepared**: May 19, 2026
**Execution window**: June 22 – July 13, 2026 (22 calendar days)
**Total resource allocation**: 68–78 hours (writing 56–66 hrs + design 12.5 hrs + upload 6 hrs)

---

## Visual Gantt Chart

Key:
- `[=====]` = active task
- `[--]`    = float (slack) days
- `[*]`     = milestone or upload event
- `[!]`     = hard deadline (zero float)
- Numbers at right = cumulative writing hours at end of that row

```
PHASE 3 — CRITICAL PATH OVERVIEW
Days:     │ Pre-Sprint ─────────────── │ Wk1 ─────────────────────── │ Wk2 ────────────────────────── │ Wk3 ─────────────── │Post│
          │May26   Jun8  Jun15  Jun22  │ 22  23  24  25  26  27  28  │ 29  30  Jul1  2   3   4   5   │ 6   7   8   9  10  11 12  13│→  │
──────────┼────────────────────────────┼────────────────────────────────┼──────────────────────────────────┼────────────────────────────────┼────┤
SUPPLIER  │                            │                                │                                  │                                │    │
Goldenseal│[!ORDER Jun8]               │                                │                  [delivery Jul13]│                                │    │
BlkCohosh │      [!Jun8]               │                                │                  [delivery Jul13]│                                │    │
Elderberry│           [!Jun15]         │                                │             [delivery Jul13-20]  │                                │    │
Tier3 all │                [!Jun22]    │                                │             [delivery Jul12-19]  │                                │    │
MtRoseHrbs│        [ORDER by Jun15]    │                                │                                  │                                │    │
──────────┼────────────────────────────┼────────────────────────────────┼──────────────────────────────────┼────────────────────────────────┼────┤
PHOTO     │                            │                                │                                  │                                │    │
Props     │[=== acquire May26–Jun2 ===]│                                │                                  │                                │    │
Seedling  │         [== Jun3–9 ======] │                                │                                  │                                │    │
Mature    │               [= Jun10–16]│                                │                                  │                                │    │
Dried     │                 [Jun17–21]│                                │                                  │                                │    │
StudioSht │                 [Jun17–21]│  [Jun23-26 in-sprint batch]    │                                  │                                │    │
EditCull  │                    [Jun21]│     [Jun23–26 editing]         │                                  │                                │    │
──────────┼────────────────────────────┼────────────────────────────────┼──────────────────────────────────┼────────────────────────────────┼────┤
DESIGN    │                            │                                │                                  │                                │    │
BrandTest │                            │[!Jun22]                        │                                  │                                │    │
WH Cover  │                            │  [Jun23]                       │                                  │                                │    │
Resp Cover│                            │     [Jun24]                    │                                  │                                │    │
Imm Cover │                            │                                │[Jun29]                           │                                │    │
Sleep Covr│                            │                                │       [Jun30]                    │                                │    │
WH ZoneCard                            │                                │             [Jul1]               │                                │    │
Resp ZoneC│                            │                                │               [Jul2]             │                                │    │
Imm ZoneC │                            │                                │                                  │[Jul6]                          │    │
Slp ZoneC │                            │                                │                                  │    [Jul7]                      │    │
Dgt Cover │                            │                                │                 [Jul3]           │                                │    │
Dgt ZoneC │                            │                                │                                  │[Jul6]                          │    │
[DESIGN   │                            │                                │                 LOCK Jul3]       │                                │    │
──────────┼────────────────────────────┼────────────────────────────────┼──────────────────────────────────┼────────────────────────────────┼────┤
WRITING   │                            │                                │                                  │                                │    │
WH Guide  │                            │[Jun22======Jun24]              │                                  │                                │15hr│
Resp Guide│                            │            [Jun25===Jun27]     │                                  │                                │28hr│
Imm Guide │                            │                                │[Jun29===Jul2]                    │                                │39hr│
Sleep     │                            │                                │           [Jul3====Jul5]         │                                │50hr│
Digestive │                            │                                │                                  │[Jul6==Jul8]                    │61hr│
FTC Review│                            │                                │                                  │       [Jul9]                   │64hr│
SEO Pass  │                            │                                │                                  │           [Jul10]              │66hr│
──────────┼────────────────────────────┼────────────────────────────────┼──────────────────────────────────┼────────────────────────────────┼────┤
UPLOAD    │                            │                                │                                  │                                │    │
WH Upload │                            │                                │[*Jun29]                          │                                │    │
Resp Upld │                            │                                │                                  │[*Jul6-7 or Jul11]              │    │
Sleep Upld│                            │                                │                                  │               [*Jul13]         │    │
Imm Upload│                            │                                │                                  │                                │[*Jul20]
Dgt Upload│                            │                                │                                  │                                │→Aug3
──────────┼────────────────────────────┼────────────────────────────────┼──────────────────────────────────┼────────────────────────────────┼────┤
FLOAT     │                            │                                │                                  │                                │    │
Float D1  │                            │                                │                                  │            [--Jul12]           │    │
Float D2  │                            │                                │                                  │                 [--Jul13]      │    │
──────────┴────────────────────────────┴────────────────────────────────┴──────────────────────────────────┴────────────────────────────────┴────┘

CRITICAL PATH (hard constraints, zero float):
  June 8 ──→ June 22 ──→ June 29 ──→ July 6–7 ──→ July 13 ──→ July 20 ──→ August 3
  (Goldenseal order)    (WH upload)  (Resp upload)  (Sleep upload)(Imm upload)(Dgt upload)
```

---

## Daily Milestone Table — 22-Day Execution Window

**Legend**: WRITE = writing track | DESIGN = design track | PHOTO = photography | UPLOAD = Etsy listing | FLOAT = available buffer

| Day | Date | Track | Task | Target Hours | Float | Critical Path? | Notes |
|---|---|---|---|---|---|---|---|
| Pre | May 26–Jun 2 | PHOTO | Props acquisition + plant order Tier 1 | 3 | 2 days | YES | Goldenseal hard deadline Jun 8 |
| Pre | Jun 3–9 | PHOTO | Seedling/juvenile state photography | 4 | 7 days | No | Annual starts: Calendula, Red Clover, Ginger |
| Pre | Jun 8 | SUPPLIER | **Goldenseal order DEADLINE** | 0.5 | **0 days** | **YES** | Prairie Moon or Strictly Medicinal; CC path if missed |
| Pre | Jun 10–16 | PHOTO | Mature/flowering state photography | 5 | 5 days | No | Black Cohosh, Elderberry arrive ~Jun 15 |
| Pre | Jun 15 | SUPPLIER | **Elderberry order DEADLINE** | 0.5 | **0 days** | **YES** | Local nursery backup if Prairie Moon out of stock |
| Pre | Jun 17–21 | PHOTO | Dried herb photography + editing + cull | 6 | 1 day | No | Mountain Rose Herbs dried herbs available |
| Pre | Jun 21 | DESIGN | Canva brand kit pre-test (zone card) | 0.5 | 1 day | No | Confirm Phase 3 palette loads correctly |
| D1 | Jun 22 | WRITE + DESIGN | WH: Intro + Black Cohosh; Brand kit load | 5 + 0.5 | 1 day | YES | Sprint begins; design track starts |
| D2 | Jun 23 | WRITE + PHOTO | WH: Vitex + Red Clover; Studio batch Day 1 | 5 + 2 | 1 day | YES | Studio shoot: Calendula, Red Clover seedlings |
| D3 | Jun 24 | WRITE + DESIGN + PHOTO | WH: Calendula + Lavender + WH shared sections; WH cover design; Studio batch Day 2 | 5 + 1.2 + 3 | 1 day | YES | WH cover needs hero photo available by today |
| D4 | Jun 25 | WRITE + DESIGN + PHOTO | Resp: Intro + Elderberry; Resp cover design; Studio batch Day 3 | 5 + 1.2 + 3 | 1 day | YES | |
| D5 | Jun 26 | WRITE + PHOTO | Resp: Mullein + Echinacea; Studio batch Day 4 (dried herbs) + edit | 5 + 2 | 1 day | YES | |
| D6 | Jun 27 | WRITE | Resp: Thyme + shared sections; WH self-edit pass | 4 | 2 days | No | Lighter writing day |
| D7 | Jun 28 | WRITE | Resp self-edit + PDF export test WH; Week 2 prep | 2 | 2 days | No | WH export ready by EOD |
| **D8** | **Jun 29** | **UPLOAD + WRITE** | **[MILESTONE] WH uploaded to Etsy; Imm: Intro + Echinacea condensed** | **2 + 3** | **1 day** | **YES** | **First listing live** |
| D9 | Jun 30 | WRITE + DESIGN | Imm: Ashwagandha complete (900 words); Imm cover design | 5 + 1.2 | 1 day | YES | Most complex species section |
| D10 | Jul 1 | WRITE + DESIGN | Imm: Elderberry condensed + Goldenseal intro + CITES sidebar; WH zone card | 5 + 0.8 | 1 day | YES | CITES sidebar is mandatory content |
| D11 | Jul 2 | WRITE + DESIGN | Imm: Goldenseal cultivation + FGV sourcing + contraindications + shared sections; Resp zone card | 5 + 0.8 | 1 day | YES | Goldenseal section: 900 words, legal precision required |
| D12 | Jul 3 | WRITE + DESIGN | Sleep: Intro + Valerian; Digestive cover; **DESIGN LOCK** | 4 + 1.2 | 1 day | No | Design lock EOD — no further design changes |
| D13 | Jul 4 | WRITE | Sleep: Passionflower complete (maypop forager crossover) | 4 | 2 days | No | |
| D14 | Jul 5 | WRITE | Sleep: Lemon Balm + Lavender condensed + shared sections + self-edit | 4 | 2 days | No | Imm + Sleep complete by EOD |
| **D15** | **Jul 6** | **UPLOAD + WRITE + DESIGN** | **[MILESTONE] Resp uploaded; Digestive: Intro + Dandelion; Imm + Sleep zone cards (2)** | **2 + 5 + 1.6** | **1 day** | **YES** | **Second listing live (7 days after WH)** |
| D16 | Jul 7 | WRITE + DESIGN | Digestive: Calendula (digestive framing) + Lemon Balm (carminative); Imm zone card if not done | 4 + 0.8 | 1 day | No | Shared species condensation saves ~2 hrs |
| D17 | Jul 8 | WRITE | Digestive: Ginger complete (700 words — cultivation zones, untreated rhizome sourcing) | 4 | 2 days | No | |
| D18 | Jul 9 | WRITE + DESIGN | FTC language review all 5 bundles + contraindications check; Digestive zone card | 3 + 0.8 | 2 days | No | Critical compliance pass |
| D19 | Jul 10 | WRITE + UPLOAD | SEO optimization pass; PDF export all 5; Etsy tags/title QA | 2 + 2 | 1 day | No | Final writing day |
| D20 | Jul 11 | UPLOAD | Resp Etsy upload (if delayed from Jul 6); Sleep upload prep | 2 | 1 day | No | Alternate Resp upload date if Jul 6 missed |
| **D21** | **Jul 12** | **FLOAT** | Float: absorb overrun OR begin Sleep upload staging | 0–4 | **8 hours float** | No | **Float day 1 — absorbs up to 8 hours overrun** |
| **D22** | **Jul 13** | **UPLOAD + FLOAT** | **[MILESTONE] Sleep uploaded; Sprint retrospective; WORKLOG.md update** | **2 + 2** | **4 hours float** | **YES** | **Third listing live (7 days after Resp)** |

---

## Critical Path Highlighted

The critical path is the longest sequential chain of tasks with zero float. Any delay on a
critical path task directly delays the corresponding upload milestone.

```
CRITICAL PATH CHAIN — JUNE 22 TO JULY 13

[June 8]             [June 22]           [June 24]      [June 28]      [June 29]
Goldenseal  ──────►  Sprint      ──────► WH Guide  ───► WH PDF  ─────► WH Upload
Order Due            Begins              Complete        Export          Live on Etsy
  │                                                                         │
  │              [June 25]         [June 27]        [July 6-7]             │
  └────────────► Resp Guide ──────► Resp PDF ──────► Resp Upload ──────────┘
                 Begins             Export            Live (Day 14)
                                                          │
                          [June 29]       [July 5]    [July 13]           │
                          Imm/Sleep ─────► Sleep PDF ─► Sleep Upload ─────┘
                          Writing         Export        Live (Day 22)
                          Begins
```

**Hard deadlines (zero float, appear on critical path)**:

| Date | Event | Why Zero Float |
|---|---|---|
| June 8 | Goldenseal order (live specimen path) | 5–6 week lead time; missing means committing to CC photo path before sprint begins |
| June 8 | Black Cohosh order | Same 5–6 week lead time constraint |
| June 15 | Elderberry order | 4-week lead time; missing means local nursery substitute only |
| June 22 | Sprint start | All downstream milestones cascade from this date |
| June 29 | Women's Health upload | First Etsy discovery window opens; delays compress upload spacing |
| July 3 | Design lock | After this date, design changes consume writing time from Week 3 |
| July 6–7 | Respiratory upload | 7-day Etsy spacing from Women's Health; compressing harms both listings' momentum |
| July 13 | Sleep upload | 7-day spacing from Respiratory; end of sprint window |

**Float days marked per task**:

Tasks with the most float (lower-risk, can slip without affecting uploads):
- Props acquisition (May 26–Jun 2): 7-day float before seedling photography
- Seedling photography (Jun 3–9): 10-day float before mature photography
- Studio batch Days 2–4 (Jun 24–26): 2-day float each (photography is supplementary, not critical path)
- Design tasks (all): 1–3 day float each (design runs parallel to writing; design lock Jul 3 provides 5-day buffer before final uploads)
- FTC review pass (Jul 9): 2-day float (FTC review is Day 18 of 22; can compress to Day 19 if Week 3 writing runs long)

---

## Resource Allocation by Week and Role

### Hours Per Week Summary

| Week | Writing | Design | Photography | Upload Admin | Total |
|---|---|---|---|---|---|
| Pre-sprint (May 26–Jun 21) | 0 | 0.5 (brand kit pre-test) | 15–18 | 0 | 15–19 |
| Week 1 (Jun 22–28) | 31 | 2.4 | 10 (studio batch) | 0 | 43 |
| Week 2 (Jun 29–Jul 5) | 28 | 4.0 | 0 | 2 (WH upload) | 34 |
| Week 3 (Jul 6–13) | 16 | 4.6 | 0 | 6 (3 uploads + QA) | 27 |
| Post-sprint (Jul 14–Aug 3) | 2 (edits) | 0 | 0 | 4 (2 uploads) | 6 |
| **Total** | **77** | **11.5** | **25–28** | **12** | **125–128** |

Note: Photography hours include pre-sprint studio batches and are separate from Wikimedia CC
photo sourcing (included in writing hours as research time, approx. 0.5–1 hour per species).

### Hours Per Week by Role (Single-Writer Scenario — Option A)

One person executing all tracks:

| Week | Daily Hours | Days | Total Hours | Sustainability |
|---|---|---|---|---|
| Pre-sprint photog. | 3–4 hours/day | 4 shoot days + 2 edit | 15–18 hrs across 4 weeks | Low intensity |
| Week 1 (Jun 22–28) | 6–8 hours/day | 6 days | 37–45 hours | HIGH — most intensive week |
| Week 2 (Jun 29–Jul 5) | 5–6 hours/day | 6 days | 30–36 hours | MEDIUM-HIGH |
| Week 3 (Jul 6–13) | 4–5 hours/day | 6 days | 24–30 hours | MEDIUM (float days available) |
| **Sprint total** | **5.5–6.5 avg** | **18 active days** | **91–111 hrs** | |

Week 1 is the hardest week. It contains the two longest bundles (Women's Health 14–16 hrs,
Respiratory 12–14 hrs) plus the studio photography batch and first two cover designs. If Week 1
average drops below 4.5 hours/day on writing, activate Option C (3-bundle scope).

### Hours Per Week by Role (Two-Writer Scenario — Option B)

Writer A: Women's Health + Immunity + Digestive (40–44 hours writing)
Writer B: Respiratory + Sleep (26–30 hours writing)
Design and photography remain with Writer A (or single designer).

| Week | Writer A Writing | Writer B Writing | Design | Photography | Total |
|---|---|---|---|---|---|
| Week 1 | Women's Health + Imm start (18 hrs) | Respiratory (13 hrs) | 2.4 hrs | 10 hrs | 43 hrs |
| Week 2 | Immunity complete + Digestive start (15 hrs) | Sleep (13 hrs) | 4.0 hrs | 0 | 32 hrs |
| Week 3 | Digestive complete + edits (10 hrs) | Edits + support (3 hrs) | 4.6 hrs | 0 | 18 hrs |

Option B completion date: July 5–7 for all writing (vs. July 10 for Option A). All 5 uploads
can occur within the 22-day window with comfortable spacing. Risk level: Low.

---

## Pre-Sprint vs. Sprint vs. Post-Sprint Task Split

### What Happens BEFORE June 22 (Pre-Sprint)

These tasks are active RIGHT NOW (May 19–June 21) and are critical to enabling the June 22
sprint start.

| Task | Deadline | Owner | Status |
|---|---|---|---|
| Scope decision (5-bundle vs. 3-bundle vs. 2-writer) | **May 30** | User | Pending |
| Goldenseal order placed | **June 8** | User | Pending |
| Black Cohosh order placed | **June 8** | User | Pending |
| Elderberry order placed | June 15 | User | Pending |
| Mountain Rose Herbs dried herbs ordered | June 15 | User | Pending |
| Tier 3 species ordered (Echinacea, Ashwagandha, Passionflower, Valerian, Ginger, Vitex) | June 22 | User | Pending |
| Studio props acquired | June 15 | User | Pending |
| Seedling photography session | June 3–9 | User | Pending |
| Mature/flowering photography session | June 10–16 | User | Pending |
| Dried herb photography + editing | June 17–21 | User | Pending |
| Canva brand kit Phase 3 palette loaded | June 21 | User | 15-min action per PHASE_3_EXECUTION_GUIDE.md Action 3 |
| Kit herbalist tags created (7 tags) | June 22 | User | 15-min action |

**The single most important pre-sprint action**: Place the Goldenseal and Black Cohosh orders
by June 8. Every other pre-sprint task can slip by 1–2 weeks without blocking the June 22 start.
The June 8 supplier deadline is absolute.

### What Happens DURING the Sprint (June 22–July 13)

See daily milestone table above. Summary:
- Days 1–7: Women's Health + Respiratory writing + first cover designs + studio photography batch
- Days 8–14: Immunity + Sleep writing + remaining covers + zone cards + Women's Health live
- Days 15–22: Digestive writing + FTC/SEO passes + PDF exports + Respiratory and Sleep uploads + float

### What Happens AFTER the Sprint (July 14–August 3)

Post-sprint requires approximately 6 hours of admin across 3 weeks:

| Date | Task | Hours |
|---|---|---|
| July 20 | Immunity Support listing uploaded to Etsy | 2 |
| July 20 | Practitioner 10-pack PDFs queued (5 × practitioner license version) | 1 |
| August 3 | Digestive Support listing uploaded to Etsy | 2 |
| August 3 | Phase 3 analytics spreadsheet initialized (per `phase-3-kpi-dashboard.md`) | 1 |

---

## Gate Summary Table

| Gate | Type | Date | Threshold | Status |
|---|---|---|---|---|
| Phase 2 Forager Cohort | Launch authorization | May 30 | >20% of buyers in forager cohort | **CLEARED (21.3%)** |
| Native Plants Conversion | Launch authorization | May 30 | >1.5% conversion rate | **CLEARED (2.24%)** |
| Scope Decision | User decision | May 30 | 5-bundle vs. 3-bundle vs. 2-writer | Pending user decision |
| Goldenseal Order | Supplier hard deadline | June 8 | Order placed OR CC path confirmed | Pending |
| Black Cohosh Order | Supplier hard deadline | June 8 | Order placed | Pending |
| Elderberry Order | Supplier hard deadline | June 15 | Order placed | Pending |
| Sprint Launch | Execution gate | June 22 | Pre-sprint checklist complete | Pending |
| Women's Health Upload | Sprint milestone | June 29 | Guide written + PDF exported + listing created | Pending |
| Design Lock | Design gate | July 3 | All 5 covers + 4 zone cards complete | Pending |
| Respiratory Upload | Sprint milestone | July 6–7 | Guide written + PDF exported + listing created | Pending |
| Sleep Upload | Sprint end gate | July 13 | Guide written + PDF exported + listing created | Pending |
| Immunity Upload | Post-sprint | July 20 | Guide written + PDF exported + listing created | Pending |
| Digestive Upload | Post-sprint | August 3 | Guide written + PDF exported + listing created | Pending |

---

## May 30 Decisions Required

The following decisions must be made before Phase 2 launches on May 30 to enable a June 22
start without blockers. These are the only decisions that have a hard dependency on the May 30
date — all other decisions can be made during June.

**Decision 1 — Sprint Scope**

Options:
- Option A: Full 5-bundle sprint, single writer (June 22–July 13, ~5 hrs/day)
- Option B: Full 5-bundle sprint, two parallel writers (June 22–July 5, lower risk)
- Option C: 3-bundle priority launch (Women's Health + Respiratory + Sleep), Immunity +
  Digestive deferred to August

Recommendation: Option A if you can confirm 5 hours/day June 22–July 10. Option C if June
capacity is uncertain.

**Decision 2 — Goldenseal Path**

Options:
- Path 1: Order live Goldenseal rhizome from Prairie Moon or Strictly Medicinal by June 8
  (enables live specimen photography window July 13–20)
- Path 2: Commit to Wikimedia CC photos + NC Botanical Garden / Missouri Botanical Garden
  outreach (zero cost, sufficient for guide quality, no order required)

Recommendation: Path 2 unless you specifically want a live Goldenseal specimen for photography.
The guide content does not require a live specimen — Wikimedia CC-BY-SA coverage is confirmed
sufficient in `phase-3-medicinal-herbs-sourcing-guide.md`.

**Decision 3 — Second Writer Engagement**

Options:
- Engage a second writer for Option B execution
- Confirm single-writer capacity for Option A

Note: If a second writer is engaged, send them `phase-3-medicinal-herbs-content-outline.md` and
`phase-3-medicinal-herbs-sourcing-guide.md` as briefing documents. The outlines are detailed
enough for an herbalist writer to execute without additional direction.

---

*Document prepared: May 19, 2026. Seedwarden Agent.*
*Source files: PHASE_3_MEDICINAL_HERBS_CRITICAL_PATH.md, phase-3-medicinal-herbs-content-outline.md,*
*phase-3-medicinal-herbs-sourcing-guide.md, PHASE_3_PHOTOGRAPHY_LOGISTICS_PLAN.md.*
*Next review: June 22, 2026 (sprint launch).*
