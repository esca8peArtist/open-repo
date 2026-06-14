---
title: "Phase 2 Decision Gate Checklist — Post-Test-Print Activation"
project: mfg-farm
created: 2026-06-14
status: production-ready
confidence: 88%
scope: >
  Pre-execution validation checklist enabling immediate Phase 2 activation upon test print
  completion. Guides user through decision-critical verifications and scenario selection,
  producing decision artifacts (scenario choice, capital plan, hardware sourcing checklist)
  ready for implementation.
depends_on:
  - PHASE_2_SCALING_DECISION_MATRIX.md
  - CAPITAL_RAISE_STRATEGY_CONTINGENCY.md
  - ADJACENT_MANUFACTURING_ROI_UPDATE.md
  - modrun_rail.py, modrun_clip.py (design files)
---

# Phase 2 Decision Gate Checklist — Post-Test-Print Activation

## Executive Summary

This checklist runs **immediately after Phase 1 test print completion**. It validates design readiness, measures Phase 1 traction, gates scenario selection, and produces a decision artifact (PHASE_2_EXECUTION_DECISION.md) containing:
- Selected scenario (Conservative/Standard/Aggressive)
- Capital plan ($600–$15,600 across scenarios)
- Hardware sourcing checklist with lead times
- Friends+family outreach plan (if applicable)
- Phase 2 timeline and monthly targets

**Estimated execution time**: 45–90 minutes (mostly measurement + decision-making, not development work)

**Output file**: PHASE_2_EXECUTION_DECISION.md (to be created during this checklist)

---

## Part 1: Test Print Validation (15 minutes)

Use this section to evaluate whether the test print result supports moving to Phase 2 manufacturing.

### 1.1 Snap-Arm Tolerance Measurement

**Required**: Measure snap-arm clearance (tolerance target: 1.25–1.55mm per FDM_MATERIAL_CAPABILITY_MATRIX.md)

```
SNAP-ARM TOLERANCE MEASUREMENT

Specification (from modrun_clip.py):
- Target snap-arm thickness: 1.4mm nominal
- FDM tolerance range: ±0.15mm (1.25–1.55mm acceptable)
- Material: PLA+ (tighter tolerance than PLA due to better flow control)

Measurement approach:
1. Use digital calipers or precision gauge to measure snap-arm thickness
2. Take 3 measurements at different points along arm (base, middle, tip)
3. Calculate average
4. Confirm all 3 measurements fall within 1.25–1.55mm range

Results (fill in after measurement):
- Measurement 1: _____ mm
- Measurement 2: _____ mm
- Measurement 3: _____ mm
- Average: _____ mm
- In tolerance range (1.25–1.55mm)? ☐ YES ☐ NO
- Snap-arm function test (clip holds wire securely): ☐ YES ☐ NO
```

### 1.2 Print Quality Assessment

**Required**: Evaluate overall print quality across 5 dimensions

| Quality Dimension | Pass Criteria | Result | Notes |
|---|---|---|---|
| **Layer adhesion** | No visible delamination or layer separation | ☐ PASS ☐ FAIL | Flex clip gently; layers should not separate |
| **Surface finish** | Minimal stringing; acceptable cosmetic quality for Etsy listing | ☐ PASS ☐ FAIL | Should look acceptable in product photos |
| **Wall coverage** | 3 walls (0.6mm nominal) — no visible holes or thin spots | ☐ PASS ☐ FAIL | Inspect internal walls if clip is translucent |
| **Snap-arm deflection** | Arm bends smoothly without cracking; returns to original position | ☐ PASS ☐ FAIL | Cycle snap 10 times; should not show white stress marks |
| **Clip geometry** | Rails align; clip closes symmetrically; no visible warping | ☐ PASS ☐ FAIL | Insert test wire; clip should grip centered |

**Gate decision**:
- ✅ **PASS** if ALL 5 dimensions marked PASS → Proceed to Part 2 (traction measurement)
- ❌ **FAIL** if ANY dimension marked FAIL → **STOP** — Do not proceed to Phase 2. Document failure, iterate design, re-test.

---

## Part 2: Phase 1 Traction Measurement (20 minutes)

Measure cumulative Phase 1 revenue + sales to determine capital raise eligibility and scenario selection.

### 2.1 Revenue & Sales Data Collection

**Required**: Gather cumulative sales data from June 3–30 (Phase 1 launch window)

| Metric | Target Period | Value | Notes |
|---|---|---|---|
| **Gross revenue (all listings)** | June 3–June 30 | $_____ | Etsy dashboard > Stats > Revenue |
| **Units sold (clips only)** | June 3–June 30 | _____ units | Count all cable clip orders |
| **Shop rating** | As of June 30 | _____ stars | Etsy dashboard > Shop Stats |
| **Number of reviews** | As of June 30 | _____ reviews | Should be ≥5 for meaningful signal |
| **Repeat customer %** | June 3–30 | _____ % | Etsy app > Orders |
| **Avg order value (AOV)** | June 3–30 | $_____ | Total revenue ÷ number of orders |
| **Conversion rate estimate** | June 3–30 | _____ % | (Orders ÷ shop visits) |

### 2.2 Traction Level Classification

**Use this table to classify Phase 1 outcome and unlock scenario eligibility:**

| Traction Level | Revenue (cumulative) | Reviews | Star Rating | Conversion Est. | Decision |
|---|---|---|---|---|---|
| **High** | ≥$3,000 | ≥15 | ≥4.8 | ≥2.5% | Eligible for Aggressive + Standard scenarios; friends+family raise recommended |
| **Moderate** | $1,000–$3,000 | 10–14 | 4.6–4.8 | 1.5–2.5% | Eligible for Standard + Conservative; defer friends+family raise (organic growth) |
| **Low** | <$1,000 | <10 | <4.6 | <1.5% | Eligible for Conservative only; stay bootstrapped, focus on PMF validation |

**Your Phase 1 traction level**: ☐ **HIGH** ☐ **MODERATE** ☐ **LOW**

---

## Part 3: Scenario Selection (10 minutes)

**Use this gate to select which scenario to execute in Phase 2.**

### 3.1 Scenario Eligibility & Recommendation

Based on your traction level above, which scenarios are available?

**If traction = HIGH**:
- ✅ **Aggressive scenario eligible** (3 printers, $10.6K–$15.6K capital raise)
- ✅ **Standard scenario eligible** (2 printers, $1.4K–$4.7K capital available)
- ✅ **Conservative scenario eligible** (1 printer, $600–$800 self-funded)
- **Recommendation**: Aggressive or Standard

**If traction = MODERATE**:
- ❌ **Aggressive scenario NOT RECOMMENDED**
- ✅ **Standard scenario eligible** (2 printers)
- ✅ **Conservative scenario eligible** (1 printer)
- **Recommendation**: Standard with organic cash flow

**If traction = LOW**:
- ❌ **Aggressive scenario NOT RECOMMENDED**
- ❌ **Standard scenario NOT RECOMMENDED**
- ✅ **Conservative scenario eligible** (1 printer, organic growth, no raise)
- **Recommendation**: Conservative

### 3.2 Your Scenario Selection

**Circle one** (or document decision):

- ☐ **AGGRESSIVE** (3 printers, $10.6K–$15.6K raise, Q2–Q3 execution)
- ☐ **STANDARD** (2 printers, $1.4K–$4.7K capital, Q3 execution)
- ☐ **CONSERVATIVE** (1 printer, $600–$800 self-funded, organic growth)

**Rationale for selection**:

```
Why did you choose this scenario?
_________________________________________
```

---

## Part 4: Capital & Contingency Planning (15 minutes)

Based on your scenario selection, fill in the capital plan and contingency triggers.

### 4.1 Capital Requirement & Deployment Timeline

| Item | Amount | Timing | Notes |
|---|---|---|---|
| Printer 2 (Anycubic A1 Mini) | $_____ | July–Aug | From PHASE_2 scenarios table |
| Printer 3 (if Aggressive) | $_____ | July–Aug | If Aggressive scenario only |
| Initial filament + supplies | $_____ | July 1 | Order immediately upon decision |
| Etsy Ads (optional, 2-month budget) | $_____ | July–Aug | Recommend 20–30% of scenario capex |
| Laser engraving validation (bureau) | $_____ | July–Aug | $50–150 for test batches |
| **Total Phase 2 Capex** | **$_____** | **July–September** | — |

### 4.2 Capital Sourcing Plan

**How will you fund the capex above?**

**Scenario A: Self-funded**
- Personal cash available: $_____ (from Phase 1 profit)
- Additional savings available? ☐ YES ☐ NO (amount: $_______)
- **Total available**: $__________
- **Sufficient to cover Phase 2 capex?** ☐ YES ☐ NO

**Scenario B: Friends+Family Pre-Raise**
- **Will you pursue friends+family raise?** ☐ YES ☐ NO
- If YES: Target raise amount: $__________
- If YES: Target close date: [Date]
- If YES: Investors identified? ☐ YES ☐ NO

### 4.3 Contingency Decision Triggers

Define decision points if Phase 2 execution diverges from plan:

```
CONTINGENCY 1: Capex costs higher than expected
Decision:  ☐ Delay Printer 3  ☐ Reduce Ads  ☐ Scale back to 1 printer  ☐ Proceed as planned

CONTINGENCY 2: Friends+family raise comes in below target
Decision: ☐ Defer Printer 3 to Q4  ☐ Use credit card 0% APR  ☐ Revert to Conservative scenario

CONTINGENCY 3: Phase 2 revenue ramp is slow
Decision: ☐ Reduce Ads spend  ☐ Pause laser/resin  ☐ Survey customer feedback  ☐ Defer future capex
```

---

## Part 5: Hardware Sourcing Checklist (20 minutes)

### 5.1 Printer Hardware Sourcing

**For CONSERVATIVE scenario (1 printer)**:
- [ ] Confirm Anycubic A1 Mini price ($399–$499)
- [ ] Confirm lead time (in-stock or <5 days?)
- [ ] Confirm filament needs ($15–20/roll)
- [ ] Confirm shipping cost ($0–$10)
- [ ] Create calendar reminder for order date (July 1)

**For STANDARD scenario (2 printers)**:
- [ ] Confirm 2x Anycubic A1 Mini pricing ($799–$999)
- [ ] Confirm lead time for 2-unit order
- [ ] Check bulk discount available (sometimes 5–10% off 2nd unit)
- [ ] Confirm additional platform/nozzle kit ($30–50 optional)
- [ ] Confirm filament sourcing ($100–150 for 2-printer kit)
- [ ] Create calendar reminder for order date (July 1)

**For AGGRESSIVE scenario (3 printers)**:
- [ ] Confirm 3x Anycubic A1 Mini pricing ($1,197–$1,497)
- [ ] Confirm lead time for 3-unit order
- [ ] Confirm bulk discount (often 10% on 3rd unit)
- [ ] Confirm additional platforms/nozzle kits ($60–100)
- [ ] Confirm filament sourcing ($200–300 for 3-printer kit)
- [ ] **CRITICAL: Nov 1, 2026 tariff deadline** — Order 3rd printer before Oct 31 to lock in pre-tariff pricing (40% increase estimated Nov 1). Create calendar reminder for Sept 15.
- [ ] Create calendar reminder for order date (July 1)

### 5.2 Adjacency Equipment Sourcing (if pursuing laser/resin)

**Laser Engraving (xTool S1, Phase 2A)**:
- [ ] Confirm xTool S1 40W price ($1,799–$1,899)
- [ ] Confirm lead time (<10 days?)
- [ ] Confirm LightBurn software license ($60, perpetual)
- [ ] Decision gate: Order xTool only if >50 cumulative engraved units by August 15
- [ ] Create decision reminder for August 15, 2026

**Resin Printing (Elegoo Saturn 4 Ultra 16K, Phase 3)**:
- [ ] Confirm Elegoo Saturn 4 Ultra 16K price ($299–$349)
- [ ] Confirm Mercury Plus wash station ($75–$99)
- [ ] Confirm resin cost ($20–$25/liter bulk)
- [ ] Defer resin purchase to October 2026 per Phase 3 timeline
- [ ] Create reminder for October 1, 2026

---

## Part 6: Friends+Family Outreach Plan (if applicable)

**Only complete if your scenario requires capital raise (HIGH traction + Aggressive/Standard).**

### 6.1 Investor Target List

Identify 5–8 friends/family investors:

| Name | Relationship | Estimated Availability | Contact Method | Interest |
|---|---|---|---|---|
| Person 1 | Friend / family / colleague | $_____ | Email / Phone | ☐ Likely ☐ Maybe ☐ Unlikely |
| Person 2 | Friend / family / colleague | $_____ | Email / Phone | ☐ Likely ☐ Maybe ☐ Unlikely |
| Person 3 | Friend / family / colleague | $_____ | Email / Phone | ☐ Likely ☐ Maybe ☐ Unlikely |

**Total estimated availability**: $__________ (sum of estimates)

### 6.2 Pitch Deck Outline

Prepare 3-slide pitch deck:

- [ ] Slide 1: **Unit Economics** (cost per clip, retail price, gross margin, monthly profit)
- [ ] Slide 2: **Market Opportunity** (construction/factory demand for cable management)
- [ ] Slide 3: **Phase 2 Plan** (3-scenario overview, capital needs, timeline to profitability, investor payback timeline)

---

## Part 7: Execution Readiness Verification (5 minutes)

**Before finalizing, confirm you've completed all critical items:**

### 7.1 Pre-Execution Checklist

- [ ] **Test Print Validation**: Snap-arm tolerance measured and within 1.25–1.55mm range
- [ ] **Test Print Quality**: All 5 quality dimensions marked PASS
- [ ] **Phase 1 Traction Measured**: Revenue, units, rating, reviews, conversion rate documented
- [ ] **Scenario Selected**: Conservative/Standard/Aggressive choice made and rationale documented
- [ ] **Capital Plan Confirmed**: Capex amount, sourcing, timeline documented
- [ ] **Hardware Sourcing Verified**: Printer lead times, pricing, backup suppliers confirmed
- [ ] **Friends+Family Plan Ready** (if applicable): Investor list identified, pitch deck outline created
- [ ] **Contingency Triggers Defined**: Decision points for cost overruns, slow ramp, capital shortfall documented

### 7.2 Success Criteria

- All test print validation items complete
- Phase 1 traction snapshot documented
- Scenario selected and rationale documented
- Capital plan and sourcing verified
- All contingency decision triggers defined

---

**Total checklist execution time**: 45–90 minutes

**On completion**: You're ready to begin Phase 2 hardware orders, friends+family outreach (if applicable), and scaling production within 48–72 hours of decision gate clearance.

---

## Appendix: Reference Links

- **PHASE_2_SCALING_DECISION_MATRIX.md** — Detailed scenario comparisons (capital, timeline, revenue, profitability)
- **CAPITAL_RAISE_STRATEGY_CONTINGENCY.md** — Friends+family fundraising mechanics and timeline
- **ADJACENT_MANUFACTURING_ROI_UPDATE.md** — Laser/resin/CNC analysis for Phase 2A–3
- **modrun_rail.py** — Cable clip rail design file
- **modrun_clip.py** — Cable clip snap-arm design file
