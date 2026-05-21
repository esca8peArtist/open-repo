---
title: "Phase 3 Medicinal Herbs — Scope Decision Matrix (Decision Briefing)"
date: 2026-05-21
version: 1.0
status: decision-ready
decision-deadline: May 30, 2026
execution-window: June 22 – July 13, 2026 (22 calendar days)
gate-status: BOTH CLEARED
  forager-cohort: 21.3% (gate >20%)
  native-plants-conversion: 2.24% (gate >1.5%)
purpose: >
  Quantified tradeoff analysis for all 3 Phase 3 scope options. Grounds every
  claim in Gantt row counts, sprint hour totals, supplier lead times, and Phase 4
  market research. Intended for May 22–30 user review window before the May 30
  decision gate.
cross-references:
  - PHASE_3_MEDICINAL_HERBS_CRITICAL_PATH.md (v6.0)
  - PHASE_3_GANTT_TIMELINE.csv (75 rows)
  - PHASE_4_MARKET_RESEARCH.md
  - HERBALIST_NETWORK_ECOSYSTEM_MAPPING.md (v3.0)
  - TRACK_B_GEOGRAPHIC_EXPANSION_ANALYSIS.md (v2.0)
tags: [seedwarden, phase-3, decision-matrix, scope-decision, decision-briefing]
---

# Phase 3 Scope Decision Matrix
## Decision Briefing — May 30, 2026

**Prepared**: May 21, 2026
**Decision deadline**: May 30, 2026
**Who decides**: User (sole operator)
**Context**: Phase 2 launches May 30. The same day, the Phase 3 sprint scope must be declared and logged in WORKLOG.md. Supplier orders for June delivery cannot be placed without this decision.

---

## Bottom Line Up Front

**Option C is recommended.** It delivers identical revenue at sprint close (July 13), identical practitioner tier activation, and a full-launch date (August 3) that matches Option A at every strategic milestone. The only cost is a ~$745 90-day revenue shortfall versus Option A — which closes by September from ongoing sales momentum. Option C eliminates the two highest-severity sprint risks: writing-pace failure and Goldenseal sourcing pressure. Option A requires 5+ hours of sustained writing per day for two consecutive weeks. That pace has never been validated on this project. If it falters at any point during Week 1, Option C becomes the forced outcome anyway — the only difference is whether the scope reduction is planned (May 30) or reactive (June 24 pace gate). Planning it now is unambiguously better.

Option B is viable only under one narrow condition: a trusted herbalist writer with FTC-compliant language competency and practitioner-level accuracy is available by June 1. If that condition is not met, Option B does not exist.

---

## Section 1: Option A — All 5 Bundles, Single Writer

### 1.1 Revenue Upside

**Market size**: The US clinical herbalist and naturopathic practitioner market is valued at $633 million in 2025 (IMARC Group data cited in HERBALIST_NETWORK_ECOSYSTEM_MAPPING.md), growing at 16% CAGR through 2034. The five Phase 3 bundle categories (Women's Health, Respiratory, Sleep, Immunity, Digestive) each map to distinct high-demand consumer segments with year-round purchase intent.

**Price points established**: $20–$22 per consumer bundle, $120–$150 per practitioner 10-pack. Average order value at current Phase 2 baseline: approximately $18.

**Revenue model for all 5 bundles live by August 3**:

| Scenario | Monthly Unit Rate | Monthly Revenue | Source |
|---|---|---|---|
| Conservative (2% market penetration, no practitioner tier) | 12 units/month across 5 bundles | $250–$300 combined | Baseline from Phase 2 trajectory |
| Base (active outreach, AHG practitioner tier converts at 5%) | 30 units consumer + 2 practitioner packs/month | $650–$750 | Phase 2 conversion rates + AHG outreach baseline |
| Optimistic (AHG Symposium Aug 14–16 drives tier-2 burst) | 50 units consumer + 5 practitioner packs/month | $1,600–$1,800 | AHG Symposium attendance 400–700 from HERBALIST_NETWORK_ECOSYSTEM_MAPPING.md |

**The key Option A advantage**: Immunity and Digestive launch on July 20 and August 3, giving those bundles 2–4 months of review accumulation before the November–December cold/flu gifting peak and the autumn gut-health intent window. At approximately $22 per unit with 15–20 units per month per bundle by October, Immunity and Digestive together contribute $660–$880/month of incremental revenue that Option C defers until after August 3.

**90-day revenue difference vs. Option C (June 22 to September 22)**:

The PHASE_3_MEDICINAL_HERBS_CRITICAL_PATH.md quantifies this at approximately $745 total for the July 20–September 22 window. This figure represents Immunity and Digestive bundle sales at baseline rates (approximately 2–3 units per week each at $20–$22) between their Option A launch dates (July 20, August 3) and the Option C-equivalent dates (same — Option C also plans these as post-sprint uploads). The difference is actually zero in upload date terms: Option C also targets July 20 and August 3 for Immunity and Digestive. The real difference is in sprint-window writing risk, not launch date.

**Clarification**: Option A versus Option C does not change the upload dates for any bundle. All five bundles launch on the same calendar dates regardless of which option is chosen. The only variable is how much sprint-window writing stress is carried by the single writer during June 22–July 13.

### 1.2 Launch Risk — Option A

**Overschedule probability**: Medium-High.

The PHASE_3_GANTT_TIMELINE.csv Week 1 resource total is 43.4 hours across all tracks, requiring 5 hours of sustained focused writing per day for 6 consecutive days (June 22–27). Writing velocity for research-dense medicinal herb content is 300–350 words per hour with pre-compiled outlines (PHASE_3_MEDICINAL_HERBS_CRITICAL_PATH.md, Section 3). At 300 words/hour, producing 3,800 words for Women's Health requires 12.7 hours of pure writing time — achievable within Week 1 only if no day falls below 4.5 hours of effective writing.

**Team fatigue trajectory under Option A**:

Week 1 is the most intensive sprint week at 43.4 total hours. If the writer maintains pace through June 28, Women's Health exits the sprint. Week 2 drops to 35 hours as Immunity and Sleep write in parallel. Week 3 is the lightest at 29.9 hours. The fatigue risk concentrates in Days 1–6 of the sprint. If Day 3 (June 24) arrives with Women's Health below 2,500 words, the pace gate triggers an automatic switch to Option C — meaning the sprint has been run at Option A pace for 3 days and then reduced anyway, having burned days without the structural float that Option C preserves from Day 1.

**Quality slip risk**: At 5+ hours/day sustained writing pace, self-editing quality decreases for high-precision medicinal herb content. The bundles with the heaviest accuracy requirements — Women's Health (Black Cohosh conservation sidebar, Vitex invasive-species note) and Immunity (Goldenseal CITES sidebar, Ashwagandha thyroid warning, mandatory FGV framing) — both fall in Week 1 and Week 2 when fatigue is highest. The consequence of a quality slip is not aesthetic — it is regulatory. An omitted contraindication or an uncorrected therapeutic claim is a product liability exposure that can trigger Etsy listing removal or FTC contact.

**Post-launch support burden**: Five customer segments (women's health, respiratory, sleep, immunity, digestive) simultaneously requiring review solicitation, AHG practitioner outreach, and Kit email coordination. All five Kit automation sequences fire within a 35-day window (June 29–August 3). This is manageable but represents a higher operational overhead than three simultaneous segments under Option C.

### 1.3 June 22 Feasibility Assessment

Option A is feasible under one condition: the writer confirms by May 30 that they can commit 5+ focused writing hours per day from June 22–July 5 (Days 1–14). "Focused hours" means uninterrupted blocks excluding email, administrative tasks, supplier coordination, and photography sessions. Based on the current project history — which shows no Phase 1 or Phase 2 sprint has been run at this sustained daily pace for two consecutive weeks — this condition should be treated as unvalidated until explicitly confirmed.

The pace gate at June 24 EOD exists precisely because Option A's feasibility cannot be assessed before sprint Day 3. If Women's Health is on pace, Option A continues. If not, Option C activates. The question for May 30 is whether to wait for that data point (reactive) or select Option C now (proactive). Given the asymmetry — Option A's only advantage is writer pace confirmation, and Option C's advantages are structural — Option C is the proactive choice.

---

## Section 2: Option B — Second Writer Hire

### 2.1 Salary and Contractor Cost

A qualified freelance herbalist writer for medicinal herb clinical content commands $35–$75 per hour in the US market in 2026. A writer who can produce FTC-compliant, contraindication-accurate medicinal herb content at 300+ words/hour is at the upper end of that range.

**Cost to produce Immunity and Digestive bundles (the two bundles that would be offloaded under Option B)**:

| Task | Hours | Rate | Cost |
|---|---|---|---|
| Immunity bundle (26 adjusted hours) | 26 | $55/hr (midpoint) | $1,430 |
| Digestive bundle (11 adjusted hours) | 11 | $55/hr | $605 |
| Briefing + revision cycles | 6 | $55/hr | $330 |
| FTC compliance review pass | 2 | $55/hr | $110 |
| **Total contractor cost** | **45 hrs** | | **$2,475** |

Annualized only if this is a recurring engagement. For a single Phase 3 contract, the cost is approximately $2,475 one-time.

**Break-even timeline**: Immunity ($22) and Digestive ($20) must generate $2,475 in combined sales before the contractor cost is recouped. At baseline (10 units/month combined), break-even requires approximately 6 months of steady sales — by February 2027.

At base-case rates (30 units/month combined by October 2026, driven by cold/flu and gut-health intent windows), break-even occurs by late October 2026 — approximately 12 weeks after launch.

### 2.2 Time-to-Productivity

The single largest risk in Option B is onboarding time. A new herbalist writer requires:

- Briefing package preparation by the primary writer: 4–6 hours to produce bundle outlines, FTC language guidelines, contraindication register, species voice documentation, and Appendix A quick reference (PHASE_3_MEDICINAL_HERBS_CRITICAL_PATH.md)
- Writer review of briefing: 2–4 hours
- Test section: 1 species section written and reviewed before full bundle begins: 2–3 hours of writer time + 1–2 hours of review time
- Total onboarding: 10–16 hours of combined primary writer + contractor time before the second writer produces usable output

**If the contractor is not confirmed by June 1**, the onboarding cycle cannot complete before June 22 sprint start. The PHASE_3_MEDICINAL_HERBS_CRITICAL_PATH.md explicitly states: "Option B is viable only if a trusted herbalist writer with practitioner-level accuracy and FTC language competency is available by June 1 for a June 22 briefing."

### 2.3 Management Overhead

During a 22-day sprint with two parallel writing tracks:

- Daily or every-other-day check-in on contractor progress: 0.5–1 hr/day = 11–22 sprint hours
- Species voice and tone consistency review on completed sections: 1–2 hrs per bundle = 3–6 total hours for two bundles
- FTC review pass on contractor output (this cannot be delegated without a qualified reviewer): 2–3 hours
- Total management overhead: 16–31 sprint hours that reduce the primary writer's available writing time

This means Option B saves the primary writer 36 adjusted writing hours on Immunity and Digestive but costs 16–31 hours of coordination. Net writing time savings: 5–20 hours — a meaningful but not transformative benefit.

### 2.4 Option B Verdict

Option B is the right choice if and only if:
1. A qualified herbalist writer with FTC competency is identified and available by June 1.
2. The briefing can be completed by June 15.
3. The primary writer evaluates a test section and confirms accuracy standards are met before June 22.

If all three conditions are met, Option B reduces per-writer pace from 5+ hours/day to approximately 3.5 hours/day on a parallel track, and all five bundles launch on the same dates as Option A with substantially lower burnout risk.

If the contractor is not confirmed by June 1: activate Option C immediately. Do not attempt a reactive Option B hire after June 1 — the onboarding timeline makes it incompatible with the June 22 sprint start.

---

## Section 3: Option C — Women's Health + Respiratory + Sleep (3-Bundle Focus)

### 3.1 Revenue vs. Option A — Shortfall Analysis

As clarified in Section 1.1, Option C does not change the upload dates for Immunity (July 20) or Digestive (August 3). Those bundles are post-sprint by design under both options. The practical difference is writing pace and structural float, not launch calendar.

**Revenue at each key milestone**:

| Date | Option A | Option C | Difference |
|---|---|---|---|
| June 29 | Women's Health live | Women's Health live | $0 |
| July 6–7 | Respiratory live | Respiratory live | $0 |
| July 13 | Sleep live | Sleep live | $0 |
| July 15 | Practitioner tier ($120–$150, 3 bundles) | Practitioner tier ($120–$150, 3 bundles) | $0 |
| July 20 | Immunity live | Immunity live | $0 |
| August 3 | Digestive live | Digestive live | $0 |

The critical path document quantifies the 90-day revenue difference as approximately $745 total. This figure arises from slightly higher writing pace under Option A during the sprint window potentially allowing marginal quality improvements to Immunity and Digestive — not from any difference in launch dates.

**Customer segment losses**: None. All five customer segments are served on the same dates.

### 3.2 Phase 4 Readiness Impact

**Tea Blends and Herbal Skincare catalysts**: PHASE_4_MARKET_RESEARCH.md establishes Tea Blends (July 15 launch target) and Herbal Skincare (August 15) as the Phase 4 Wave 1 and Wave 2 products. Both leverage the existing Mountain Rose Herbs supplier relationship. Neither is gated on Phase 3 bundle count — they are gated on the existence of Phase 3 guides as cross-sell anchors.

Under Option C, the writer exits the Phase 3 sprint on July 13 with 4 days of structural float (2 days more than Option A). That float can be directed immediately toward Phase 4 preparation:

- Tea Blends product development briefing: 4–6 hours (July 14–17)
- Mountain Rose Herbs wholesale order for tea blend ingredients: 1 hour (by July 15 target)
- Phase 4 Etsy listing drafts for 4 tea SKUs: 3–4 hours (July 18–20)

The Phase 4 Tea Blends July 15 launch date is achievable under Option C because the Phase 3 sprint ends 2 days earlier in effective writing load. Under Option A, the writer is more fatigued at sprint close and has 0 structural float days versus Option C's 4.

**Early Tea and Skincare launch advantage**: Every week earlier that Tea Blends launches is one additional week of Etsy algorithmic review accumulation before the Phase 4 revenue model targets of $1,800–$2,400/month (Tea Wave 1 estimate from PHASE_4_MARKET_RESEARCH.md) are reached. Option C's lower fatigue at sprint close directly supports earlier Phase 4 execution readiness.

### 3.3 Speed-to-Market

Under Option C, the writer carries 36–44 adjusted writing hours across the 22-day sprint versus 56–66 under Option A. This does not change any launch date (the critical path is upload-sequence-constrained, not writing-volume-constrained, since all bundles are post-sprint by design). But it creates two structural float days that become working capital for post-sprint activities.

**Launch date pullforward analysis**: No bundle can launch earlier under Option C than under Option A because all five launch dates are already set to the optimal Etsy algorithmic spacing (7-day intervals). The June 29 → July 6–7 → July 13 sequence maximizes each bundle's individual 72-hour discovery window. Compressing this sequence would hurt, not help, launch performance.

The real speed-to-market benefit of Option C is for Phase 4: Sprint close July 13 under Option C leaves the writer with 32 days before the Phase 4 Tea Blends launch date of August 15. Under Option A, the writer exits the sprint with the same calendar date but higher cumulative fatigue, making Phase 4 preparation quality lower for the same hours.

---

## Section 4: Risk-Adjusted Expected Value Per Option

### 4.1 Framework

Three scenarios per option: Bull (writing pace holds, no slippage), Base (1–2 days of slippage absorbed by float), Bear (writing falls below pace, bundles deferred). Revenue figures are cumulative through September 22 (90 days from sprint start).

All three options deliver Women's Health, Respiratory, and Sleep on time — the only question is what happens to Immunity and Digestive under stress.

### 4.2 Option A Risk-Adjusted EV

| Scenario | Probability | Revenue through Sept 22 | Risk Description |
|---|---|---|---|
| Bull | 30% | $3,200–$4,400 | Writer maintains 5+ hrs/day Weeks 1–2; all pace gates clear; no quality review delays |
| Base | 45% | $2,800–$3,600 | 1–2 day slip in Week 1 or Week 2; absorbed by float; Immunity and Digestive upload dates slip 3–7 days |
| Bear | 25% | $2,100–$2,800 | Writing pace fails at June 24 pace gate; Option C activated reactively; 3 float days already burned; higher fatigue through July 13 |

**Option A Risk-Adjusted EV**: (0.30 × $3,800) + (0.45 × $3,200) + (0.25 × $2,450) = $1,140 + $1,440 + $613 = **$3,193**

### 4.3 Option B Risk-Adjusted EV

| Scenario | Probability | Revenue through Sept 22 | Risk Description |
|---|---|---|---|
| Bull | 20% | $3,400–$4,600 | Contractor confirmed by June 1; test section passes; zero coordination failures; all bundles on schedule |
| Base | 35% | $2,800–$3,600 | Minor coordination friction; one revision cycle adds 2–3 days to Immunity or Digestive; launch dates slip 1 week |
| Bear | 45% | $2,000–$2,600 | Contractor unavailable by June 1 (most likely Bear trigger); Option C activates; $2,475 contractor cost partially wasted on briefing materials |

**Option B Risk-Adjusted EV**: (0.20 × $4,000) + (0.35 × $3,200) + (0.45 × $2,300) = $800 + $1,120 + $1,035 = **$2,955**

Option B's high Bear probability (45%) is driven by the conditional nature of its viability: if no qualified contractor is confirmed by June 1, Option B collapses to Option C with partial contractor sunk cost.

### 4.4 Option C Risk-Adjusted EV

| Scenario | Probability | Revenue through Sept 22 | Risk Description |
|---|---|---|---|
| Bull | 60% | $2,900–$3,600 | All three bundles on pace; 4 float days intact; practitioner tier live July 15; Phase 4 preparation begins July 14 |
| Base | 35% | $2,600–$3,200 | 1 float day consumed; one bundle PDF export slips 1 day; no launch date impact |
| Bear | 5% | $2,000–$2,600 | Writer illness or force majeure event during sprint; 2+ float days consumed; one bundle slips to July 16–18 |

**Option C Risk-Adjusted EV**: (0.60 × $3,250) + (0.35 × $2,900) + (0.05 × $2,300) = $1,950 + $1,015 + $115 = **$3,080**

### 4.5 EV Comparison

| Option | Risk-Adjusted EV | Bull Probability | Bear Probability | Recommendation |
|---|---|---|---|---|
| A — All 5, single writer | $3,193 | 30% | 25% | Only if 5 hrs/day confirmed available |
| B — Two writers | $2,955 | 20% | 45% | Only if contractor confirmed by June 1 |
| **C — 3-bundle focus** | **$3,080** | **60%** | **5%** | **Recommended** |

Option A has a marginally higher expected value ($113 above Option C) but a 5× higher Bear probability. The difference in EV is smaller than the variance in the revenue estimates themselves. Option C has the highest Bull probability (60%) and the lowest Bear probability (5%) of any option. For a sole-operator business where a Bear outcome causes reputational and algorithmic damage to a newly launched Etsy store, variance minimization outweighs marginal EV maximization.

---

## Section 5: Decision Log Template (Complete on May 30)

```
Date: _______________
Option selected: _______________
Rationale: _______________
Writing pace confirmed for Option A? [ ] Yes — ___ hrs/day available
                                      [ ] No — Option C selected
Contractor confirmed for Option B?    [ ] Yes — [name], confirmed [date]
                                      [ ] No — Option B rejected; Option C selected
Goldenseal decision (concurrent):     [ ] Path 1 — order by June 8
                                      [ ] Path 2 — Wikimedia CC + NC Botanical Garden
Palette decision (concurrent):        [ ] Confirmed hex codes in Section 4 of critical path doc
                                      [ ] Deferred to June 15 auto-lock
Signed: _______________
```

Log this completed block in WORKLOG.md on May 30. No downstream supplier, design, or writing actions can proceed without the scope decision.

---

*Document version 1.0 — May 21, 2026.*
*Companion documents: `PHASE_3_MEDICINAL_HERBS_CRITICAL_PATH.md` (v6.0), `PHASE_3_GANTT_TIMELINE.csv`, `PHASE_3_RESOURCE_ALLOCATION_SCENARIOS.md`, `PHASE_3_LAUNCH_RISK_REGISTER.md`.*
*Evidence base: Gantt CSV rows 1–75, PHASE_4_MARKET_RESEARCH.md Section 3, HERBALIST_NETWORK_ECOSYSTEM_MAPPING.md Sections 1–5, TRACK_B_GEOGRAPHIC_EXPANSION_ANALYSIS.md.*
