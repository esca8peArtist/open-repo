---
title: "Phase 3 Timeline Gantt Charts — 10 Decision Combinations"
date: 2026-05-21
version: 1.0
status: execution-ready
phase: Phase 3 execution prep
cross-references:
  - PHASE_3_IMPLEMENTATION_CHECKLIST_MATRIX.md
  - PHASE_3_MEDICINAL_HERBS_CRITICAL_PATH.md (v6.0)
  - PHASE_3_OPTION_ANALYSIS.md
tags: [seedwarden, phase-3, gantt, timeline, visualization]
---

# Phase 3 Timeline Gantt Charts
## Visual Timelines for All 10 Decision Combinations

**Prepared**: May 21, 2026
**Execution window**: May 30 (decision) through August 31 (monitoring complete)
**Key hard dates**: June 22 sprint start; July 13 sprint close (Options A/C); July 22 full library live (Option B); August 3 Digestive upload (Options A/C/deferred)

**Legend**:
- `[===]` Active writing or production
- `[---]` Float / buffer / parallel track
- `[UPL]` Upload milestone
- `[DEC]` Decision gate
- `[REV]` Review window
- `[HRE]` Writer hire window
- `*** ` Critical path (zero float)

---

## Chart 1 — Combination 1: Option A Solo, Path 1

```
DATE        MAY30 JUN1  JUN8  JUN15 JUN22 JUN29 JUL6  JUL13 JUL20 AUG3  AUG31
            |     |     |     |     |     |     |     |     |     |     |
DECISIONS   [DEC] ...   ...   ...   ...   ...   ...   ...   ...   ...   ...
                  |
BLACK COHOSH ORD [*]   [==SHIP=======ARRIVE==]
                  |     |
GOLDENSEAL ORD  [DEC] [*ORD] [==SHIP=============ARRIVE==]
                              |
MTN ROSE HERBS               [*ORD][==SHIP]
                              |
ELDERBERRY                   [*ORD][===========SHIP]
                              |     |
PHOTO SESSIONS         [==PRE-SPRINT PHOTOS==][--in-sprint--]           [v1.1 GOLD]
                                               |     |
CANVA DESIGN                          [--covers starts--][=LOCK=]
                                               |     |     |     |
WRITING/SPRINT                        [*=====SPRINT====*] |     |
                                               |     |     |     |
UPLOAD/REVENUE                                [WH]  [RSP] [SLP] [IMM]  [DIG]
                                                                  |
PRACTITIONER TIER                                           [PTIER live Jul 15]
                                                                        |
PEER REVIEW WH                                        [REV window=====]
PEER REVIEW IMM                                             [======REV=====]
                                                                        |
AFFILIATE/KIT                                         [KIT] [KIT] [KIT] [KIT] [KIT]
                                                                              |
MONITORING                                                         [====monitoring====]
                                                                              |
GOLDENSEAL v1.1                                                         [photo+update]
```

**Key dependency chain (critical path)**:
May 30 DEC → Jun 8 Goldenseal order → Jun 22 sprint start → Jun 24 pace gate → Jun 29 WH upload → Jul 6 Resp upload → Jul 13 Sleep upload → Jul 15 practitioner tier → Jul 20 Immunity upload → Aug 3 Digestive upload

**Path 1 Goldenseal impact**: Adds Jun 8 hard deadline with zero float. Specimen arrives July 13–20 for v1.1 photography. v1.0 Immunity uses Wikimedia CC hero. No writing or upload date is affected.

---

## Chart 2 — Combination 2: Option A Solo, Path 2

```
DATE        MAY30 JUN1  JUN7  JUN15 JUN22 JUN29 JUL6  JUL13 JUL20 AUG3  AUG31
            |     |     |     |     |     |     |     |     |     |     |
DECISIONS   [DEC] ...   ...   ...   ...   ...   ...   ...   ...   ...   ...
                  |     |
WIKIMEDIA CC [research Jun 1-7] [email NCBG/MOBOT Jun 7][attrib log Jun 21]
                  |     |
BLACK COHOSH ORD [*]   [==SHIP=======ARRIVE==]
                              |
MTN ROSE HERBS               [*ORD][==SHIP]
                              |
ELDERBERRY                   [*ORD][===========SHIP]
                              |     |
PHOTO SESSIONS         [==PRE-SPRINT PHOTOS==][--in-sprint--]
                                               |     |
CANVA DESIGN                          [--covers starts--][=LOCK=]
                                               |     |     |     |
WRITING/SPRINT                        [*=====SPRINT====*] |     |
                                               |     |     |     |
UPLOAD/REVENUE                                [WH]  [RSP] [SLP] [IMM]  [DIG]
                                                                  |
PRACTITIONER TIER                                           [PTIER live Jul 15]
                                                                        |
AFFILIATE/KIT                                         [KIT] [KIT] [KIT] [KIT] [KIT]
                                                                              |
MONITORING                                                         [====monitoring====]
```

**Key difference from Chart 1**: Jun 8 Goldenseal hard deadline is removed. Wikimedia CC research window (Jun 1–7) replaces the order. Attribution log must be complete by Jun 21 (zero float). No v1.1 photography required.

**Path 1 vs. Path 2 sourcing timeline comparison**:

| Milestone | Path 1 (Chart 1) | Path 2 (Chart 2) | Difference |
|---|---|---|---|
| Decision action | Jun 8 order placed | Jun 7 email to NCBG | 1 day earlier, no payment |
| Goldenseal ready for design | Jul 13–20 (specimen) or CC backup | Jun 21 (CC images logged) | Path 2 is available 3 weeks earlier |
| Schedule risk | Zero float on Jun 8 | No float risk | Path 2 eliminates the risk |
| v1.0 Immunity cover | CC hero (same) | CC hero | Identical |
| v1.1 upgrade path | Available post-sprint | Optional (order after sprint) | No structural difference |

---

## Chart 3 — Combination 3: Option B, Path 1, Second Writer

```
DATE        MAY30 JUN1  JUN8  JUN15 JUN22 JUL1  JUL8  JUL15 JUL22 AUG1  AUG31
            |     |     |     |     |     |     |     |     |     |     |
DECISIONS   [DEC] ...   ...   ...   ...   ...   ...   ...   ...   ...   ...
                  |     |
WRITER HIRE [HRE==confirm Jun1==] ...
                  |     |
CONTRACT    [---25%dep---]                                          [25%final]
                  |     |     |
WRITER ONBOARD    [====briefing=====]
                              |
WRITER SPRINT                 [==RESP==][==IMMUN==][==DIGEST==]
                              |     |     |     |     |
USER SPRINT                   [=WH==][==SLEEP==]
                              |
GOLDENSEAL ORD          [*ORD] [==SHIP==========ARRIVE==]
                              |     |
MTN ROSE + ELDERBERRY        [*ORD][SHIP]
                              |     |
PHOTO SESSIONS        [==PRE-SPRINT PHOTOS==][--parallel--]            [v1.1]
                                              |
CANVA DESIGN                         [--covers starts--][=LOCK=]
                                              |     |     |     |
WRITER DELIVERIES                            [RESP] [IMMUN]    [DIG]
USER REVIEWS                                 [REV1] [REV2]     [REV3]
                                              |     |     |     |
UPLOAD SEQUENCE                               [WH] [RSP] [SLP] [IMM] [DIG]
                                                    |     |     |     |
                     Jun29  Jul1-2  Jul8  Jul10 Jul15 Jul22
PRACTITIONER TIER                             [PTIER live Jul 10]
                                                                  |
MONITORING                                                [====monitoring====]
```

**Upload timeline under Option B (Chart 3)**:

| Bundle | Writer | Upload Date |
|---|---|---|
| Women's Health | User | June 29 |
| Respiratory | Second writer | July 1–2 |
| Sleep | User | July 8 |
| Immunity | Second writer | July 15 |
| Digestive | Second writer | July 22 |
| Practitioner tier live | — | July 10 |

**Solo vs. hired-writer timeline differences**:

| Dimension | Solo (Charts 1–2) | Second Writer (Charts 3–4) |
|---|---|---|
| First upload | June 29 | June 29 (identical) |
| Respiratory upload | July 6–7 | July 1–2 (5 days earlier) |
| Sleep upload | July 13 | July 8 (5 days earlier) |
| Immunity upload | July 20 | July 15 (5 days earlier) |
| Digestive upload | August 3 | July 22 (12 days earlier) |
| Practitioner tier | July 15 | July 10 (5 days earlier) |
| Full library live | August 3 | July 22 (12 days earlier) |
| User daily pace | 5+ hrs/day | 3 hrs/day |
| Writer hire prep | None | May 30 – June 1 (2-day window) |

---

## Chart 4 — Combination 4: Option B, Path 2, Second Writer

Identical structure to Chart 3 with Path 2 Goldenseal substitution. The Jun 7–8 Goldenseal order steps are replaced by Jun 1–7 Wikimedia CC research. All upload dates and writer timeline are identical to Chart 3.

```
DATE        MAY30 JUN1  JUN7  JUN15 JUN22 JUL1  JUL8  JUL15 JUL22 AUG1  AUG31
            |     |     |     |     |     |     |     |     |     |     |
DECISIONS   [DEC] ...   ...   ...   ...   ...   ...   ...   ...   ...   ...
                  |     |
WRITER HIRE [HRE==confirm Jun1==]
WIKIMEDIA CC [research Jun 1-7][email NCBG Jun 7][attrib log Jun 21]
                  |
CONTRACT    [25%dep]                                                [25%final]
                  |     |
WRITER ONBOARD    [====briefing Jun 1-14====]
                              |
WRITER SPRINT                 [==RESP==][==IMMUN==][==DIGEST==]
USER SPRINT                   [=WH==][==SLEEP==]
                              |
MTN ROSE + ELDERBERRY        [*ORD][SHIP]
CANVA DESIGN                         [--covers--][=LOCK=]
                                              |     |     |     |
UPLOAD                                        [WH] [RSP] [SLP] [IMM] [DIG]
                                   Jun29 Jul1-2 Jul8 Jul15 Jul22
PRACTITIONER TIER                             [live Jul 10]
MONITORING                                                [====monitoring====]
```

---

## Chart 5 — Combination 5: Option C Solo, Path 1

```
DATE        MAY30 JUN1  JUN8  JUN15 JUN22 JUN29 JUL6  JUL13 JUL20 AUG3  AUG31
            |     |     |     |     |     |     |     |     |     |     |
DECISIONS   [DEC] ...   ...   ...   ...   ...   ...   ...   ...   ...   ...
                  |     |
BLACK COHOSH ORD [*]   [==SHIP=======ARRIVE==]
GOLDENSEAL ORD  [DEC] [*ORD] [==SHIP=============ARRIVE Jul13-20]
                              |                             |
                              |                     [photo if arrived Jul17 or earlier]
MTN ROSE HERBS               [*ORD][==SHIP]
ELDERBERRY                   [*ORD][===========SHIP]
                              |     |
PHOTO SESSIONS        [==PRE-SPRINT==][--in-sprint--]
CANVA DESIGN                 [--covers--][=LOCK=]
                                               |     |     |     |
WRITING SPRINT (3 BUNDLES)            [*=WH+RESP+SLEEP=*]
                                               |     |     |
IMMUNITY (post-sprint)                               [=====WRITE IMM=====]
DIGESTIVE (post-sprint)                                          [=====WRITE DIG=====]
                                               |     |     |     |     |
UPLOAD SEQUENCE                               [WH]  [RSP] [SLP] [IMM] [DIG]
                                          Jun29  Jul6 Jul13 Jul20 Aug3
PRACTITIONER TIER                                       [live Jul 15]
AFFILIATE/KIT                                    [KIT] [KIT] [KIT] [KIT] [KIT]
MONITORING                                                    [====monitoring====]
```

**Sprint formal close**: July 13 (Sleep upload). Immunity and Digestive writing begins July 14 at post-sprint pace (2–3 hours/day). No upload dates change relative to Chart 1 — the timeline is identical for all 5 uploads; the difference is pace pressure (3–4 hrs/day vs. 5+ hrs/day for Weeks 1–2).

**Path 1 under Option C**: Goldenseal specimen arrives July 13–20. If it arrives July 17 or earlier, v1.0 Immunity uses live photography. If July 18–20, Wikimedia CC is used for v1.0 and specimen is photographed for v1.1. The June 8 order is still the relevant deadline, but the risk profile is lower than under Option A because Immunity is post-sprint.

---

## Chart 6 — Combination 6: Option C Solo, Path 2 (RECOMMENDED)

```
DATE        MAY30 JUN1  JUN7  JUN15 JUN22 JUN29 JUL6  JUL13 JUL20 AUG3  AUG31
            |     |     |     |     |     |     |     |     |     |     |
DECISIONS   [DEC]
                  |
BLACK COHOSH ORD [*] [==SHIP=======ARRIVE==]
WIKIMEDIA CC [research Jun 1-7][email NCBG Jun 7][attrib log Jun 21]
                              |
MTN ROSE HERBS               [*ORD][==SHIP]
ELDERBERRY                   [*ORD][===========SHIP]
CANVA HEX               [confirm][--or auto-lock Jun15--]
                              |     |
PHOTO SESSIONS        [==PRE-SPRINT PHOTOS==][--parallel--]
CANVA DESIGN                         [--covers--][=LOCK Jul3=]
                                               |     |     |
WRITING SPRINT                        [*=WH+RESP+SLEEP=*]  |     |
                                               |     |     |
IMMUNITY WRITING (post-sprint)                       [=======WRITE Jul14-19=======]
DIGESTIVE WRITING (post-sprint)                                   [=====WRITE Jul21-Aug2=====]
                                               |     |     |     |     |
UPLOAD                                        [WH]  [RSP] [SLP] [IMM] [DIG]
                                          Jun29  Jul6 Jul13 Jul20 Aug3
PRACTITIONER TIER                                       [live Jul 15]
PEER REVIEW WH                                    [======REV due Jun27======]
PEER REVIEW IMM                                               [===REV due Jul10===]
AFFILIATE/KIT                                    [KIT] [KIT] [KIT] [KIT] [KIT]
MONITORING                                                    [====monitoring====]
```

**Why Combination 6 is the recommended default**:
- No June 8 hard deadline (Path 2 removes it)
- No writer hire risk (solo)
- 4 sprint float days vs. 2 under Option A
- Sprint closes July 13 at identical upload dates to Option A
- 90-day revenue difference vs. Option A is ~$745 (closes by September)
- Pace gate at June 24 is a check, not a crisis: if WH is below 2,500 words, nothing changes — the 3–4 hr/day Option C pace already accommodates this

---

## Chart 7 — Combination 7: Option A, Path 1, Partial Second Writer

```
DATE        MAY30 JUN1  JUN8  JUN15 JUN22 JUN29 JUL6  JUL13 JUL20 AUG3  AUG31
            |     |     |     |     |     |     |     |     |     |     |
DECISIONS   [DEC]
WRITER HIRE [HRE=confirm Jun1=]
CONTRACT    [25%dep]                                              [25%final]
                  |     |
GOLDENSEAL ORD  [DEC] [*ORD] [==SHIP=============ARRIVE==]
BLACK COHOSH ORD [*]   [==SHIP=======ARRIVE==]
MTN ROSE + ELDERBERRY        [*ORD][SHIP]
PHOTO SESSIONS        [==PRE-SPRINT==][--parallel--]              [v1.1 GOLD]
CANVA DESIGN                 [--covers--][=LOCK Jul3=]
                                               |
WRITER SPRINT (RESP only)             [=====WRITE RESP====]
USER SPRINT (WH+IMM+SLP+DIG)         [==========FULL SPRINT===========]
                                               |     |     |     |     |
UPLOAD                                        [WH]  [RSP] [SLP] [IMM] [DIG]
                                          Jun29  Jul1-2 Jul13 Jul20 Aug3
PRACTITIONER TIER                                        [live Jul 15]
MONITORING                                                     [====monitoring====]
```

**Partial writer benefit**: Respiratory is the lowest-risk delegation bundle. Delegating it saves the user approximately 12–14 hours in Week 1, reducing daily pace from 5+ hrs/day to approximately 3–4 hrs/day in Weeks 1–2. Upload dates for all other bundles remain on the Option A schedule.

---

## Chart 8 — Combination 8: Option A, Path 2, Partial Second Writer

Same as Chart 7 with Wikimedia CC substitution for Goldenseal. Remove Jun 8 order deadline; add Jun 1–7 CC research window. All upload dates identical to Chart 7.

---

## Chart 9 — Combination 9: Option C, Path 1, Partial Second Writer

```
DATE        MAY30 JUN1  JUN8  JUN15 JUN22 JUN29 JUL6  JUL13 JUL20 AUG3  AUG31
            |     |     |     |     |     |     |     |     |     |     |
DECISIONS   [DEC]
WRITER HIRE [HRE=confirm Jun1=]
CONTRACT    [25%dep]                                    [25%final Jul20]
GOLDENSEAL ORD  [DEC] [*ORD] [==SHIP=============ARRIVE==]
BLACK COHOSH ORD [*]   [==ARRIVE==]
MTN ROSE + ELDERBERRY        [*ORD][SHIP]
PHOTO SESSIONS        [==PRE-SPRINT==][--parallel--]
CANVA DESIGN                 [--covers--][=LOCK Jul3=]
WRITER SPRINT (RESP only)             [=====WRITE RESP====]
USER SPRINT (WH + SLEEP only)         [=WH=] [=SLEEP=]
IMMUNITY (post-sprint, user)                 [===WRITE Jul14-19===]
DIGESTIVE (post-sprint, user)                             [===WRITE Jul21-Aug2===]
                                               |     |     |     |     |
UPLOAD                                        [WH]  [RSP] [SLP] [IMM] [DIG]
                                          Jun29  Jul1-2 Jul13 Jul20 Aug3
PRACTITIONER TIER                                        [live Jul 15]
MONITORING                                                     [====monitoring====]
```

**Comparison: Option C solo (Chart 6) vs. Option C + partial writer (Chart 9)**:

| Dimension | Chart 6 (solo) | Chart 9 (partial writer) |
|---|---|---|
| User writing hours | 36–44 | ~22 |
| Daily pace | 3–4 hrs/day | 2–3 hrs/day |
| Respiratory upload | July 6–7 | July 1–2 (5 days earlier) |
| Writer cost | $0 | $400–600 |
| Net 90-day revenue | $2,030–2,670 | $990–1,840 (after writer cost) |
| Recommended if | Default | Writing time severely constrained |

---

## Chart 10 — Combination 10: Option C, Path 2, Partial Second Writer

Same as Chart 9 with Path 2 Wikimedia CC substitution. Remove Jun 8 Goldenseal order; add Jun 1–7 CC research. All other dates identical to Chart 9.

---

## June 22 Hard Launch Date — Position Across All Options

The June 22 date is the sprint start, not a public launch date. The first public launch (Women's Health upload) is June 29 for all combinations. June 22 is the internal execution trigger.

| Option | June 22 Action | June 29 |
|---|---|---|
| A or C, solo | Writing begins (Women's Health D1) | Women's Health goes live |
| B, second writer | Sprint briefing call + both writers begin | Women's Health goes live |
| Partial writer | Both user and writer begin their respective bundles | Women's Health goes live |

If the May 30 decision is delayed beyond May 30, the June 22 date slides by the same number of days. A May 31 decision → June 23 sprint start → June 30 first upload. A June 1 decision → June 24 sprint start → July 1 first upload. Each day of decision delay costs one day of the first upload window.

---

## Dependency Visualization — All Combinations

The following dependencies are shared across all 10 combinations. No combination escapes these structural dependencies.

```
DECISION LAYER (May 30)
    |
    +---> Scope decision (A/B/C) --> writing pace requirement
    |
    +---> Goldenseal path (1/2) --> supplier order OR attribution logging
    |
    +---> Writer decision (solo/partial/second) --> hire by Jun 1 or confirm solo
    |
    v
PRE-SPRINT LAYER (Jun 1–21)
    |
    +---> Supplier orders (Black Cohosh Jun 1, Goldenseal Jun 8 if Path 1, Elderberry Jun 15, MTN Rose Jun 15)
    |
    +---> CC attribution logging (Jun 21, zero float before sprint)
    |
    +---> Canva Brand Kit loaded (Jun 21)
    |
    +---> Photo sessions completed (Jun 17–21 dried herb studio)
    |
    v
SPRINT LAYER (Jun 22 – Jul 13)
    |
    +---> Writing is the ONLY binding constraint
    +---> Design runs parallel; cannot block writing
    +---> Photography runs parallel; cannot block writing
    |
    +---> Jun 24 pace gate: if WH below 2,500 words, activate Option C
    |
    v
UPLOAD LAYER (Jun 29 – Aug 3)
    |
    +---> Each upload requires: PDF export complete, cover image ready, FTC review passed, attribution logged
    |
    +---> Practitioner tier activates Jul 10 (Option B) or Jul 15 (A/C) after 3-bundle minimum met
    |
    v
POST-LAUNCH LAYER (Jul 15 – Aug 31)
    |
    +---> Kit broadcasts at each upload
    +---> Affiliate code monitoring weekly
    +---> Aug 3 FORAGER20 trigger for Digestive
    +---> Sep 2026: revenue gap between options closes
```

---

*Version 1.0 — May 21, 2026. All charts reference PHASE_3_MEDICINAL_HERBS_CRITICAL_PATH.md v6.0 for source dates and hours.*
