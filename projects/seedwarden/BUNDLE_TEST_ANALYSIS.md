---
title: "Bundle Test Analysis — Decision Framework"
date: 2026-04-30
status: production-ready
context: Evaluation criteria and pivot logic for May–July 2026 bundle tests
references: BUNDLE_A_B_TEST_PLAN.md, BUNDLE_TEST_TRACKING.md, BUNDLE_TEST_DATA.csv
---

# Bundle Test Analysis
## Decision Framework: How to Read Your Data and When to Act

**Purpose**: This document tells you what to do with the numbers you collect. BUNDLE_TEST_TRACKING.md tells you how to collect them. This document tells you how to interpret them, when a result is actionable vs. noise, and exactly what decisions to make at each milestone.

**How to use it**: After completing each weekly data entry and Monthly Summary in BUNDLE_TEST_TRACKING.md, open this document and find the matching decision gate. Read the inputs and compare to your data. Make the decision stated. Do not revisit a made decision mid-test unless a catastrophic failure flag is triggered (defined below).

---

## Decision Gate Architecture

There are five decision points across the three-month test window. Each gate has defined inputs, a decision rule, and exactly two or three outputs (no ambiguous "it depends" endings without a tie-breaking rule).

| Gate | Timing | Question | Output Options |
|---|---|---|---|
| Gate 0 | May 1 | Is the bundle listed correctly? | Proceed / Fix first |
| Gate 1 | May 8 (end of Week 1) | Early cannibalization signal? | Continue / Escalate |
| Gate 2 | June 1 (end of Month 1) | Did Spring Forager Bundle pass? | Keep + expand / Adjust + retry / Remove + pause |
| Gate 3 | July 1 (end of Month 2) | Did seasonal demand materialize? | Run pricing test / Run pricing test with adjusted bar |
| Gate 4 | August 1 (end of Month 3) | Which price wins? | Set permanent price at $25 / Set permanent price at $28 / Run Phase 3 test |

---

## Gate 0 — May 1: Listing Sanity Check

**Run this before recording any data.**

Confirm each item below before the bundle test clock starts. If any item fails, fix it before recording the May 1 start date in BUNDLE_TEST_DATA.csv.

| Check | Pass Criteria | Action If Fail |
|---|---|---|
| Spring Forager Bundle listing is live on Etsy | Listing URL is accessible, not draft | Publish listing before entering any test data |
| Bundle price is $22 | Etsy listing price shows $22.00 | Correct price, wait 1 hour for Etsy indexing |
| Both individual listings are still live | Wild Edibles Guide and Zone Calendar are both findable on Etsy | Do not remove individual listings — they are the control condition |
| Bundle title includes savings mention | Title contains "Saves $3" or equivalent | Update title — pricing psychology requires the savings signal in the title |
| Bundle description follows BUNDLE_A_B_TEST_PLAN.md Part 1 framing | Lead with dollar savings, not percentage; both products named | Update description if needed |
| April 21–27 baseline is captured in BUNDLE_TEST_DATA.csv | Both individual product rows have Views, Conversions, Revenue filled in | Export baseline data from Etsy Stats for April 21–27 before May 1 midnight |

**Gate 0 output**: All checks pass — test clock starts May 1.

---

## Gate 1 — May 8: Early Cannibalization Check

**Run after entering the May 1–7 data row in BUNDLE_TEST_DATA.csv.**

This check runs only in Month 1. It catches cannibalization before it damages an entire month of individual product revenue.

### Input: Calculate Individual Product Conversion Ratios

**Wild Edibles Guide:**
```
May 1-7 conversion rate / April 21-27 baseline conversion rate = ratio
```

**Zone Calendar:**
```
May 1-7 conversion rate / April 21-27 baseline conversion rate = ratio
```

### Decision Rule

| Ratio Result | Signal | Decision |
|---|---|---|
| Both ratios ≥ 0.85 | No cannibalization | Continue test as planned. Note in weekly log. |
| Either ratio 0.70–0.84 | Mild signal | Continue test. Flag in weekly log. Watch Week 2 — if ratio stays below 0.85 in Week 2, escalate to strong signal protocol. |
| Either ratio < 0.70 | Strong cannibalization signal | Escalate immediately — see Catastrophic Failure Protocol below |

**Note on natural variance**: Etsy weekly traffic varies ±20% due to algorithm shifts, day-of-week patterns, and search cache updates. A single week below 0.85 that recovers the next week is statistical noise. The signal becomes actionable when it persists across two consecutive weeks.

---

## Gate 2 — June 1: Month 1 Post-Test Decision

**Run after entering the final May data rows and completing the Monthly Summary in BUNDLE_TEST_TRACKING.md.**

This is the most consequential decision in the three-month window. The outcome here determines whether the Phase 2 bundle strategy continues.

### Input: Pull These Values From Your Monthly Summary

- **A**: Average bundle conversion rate across all May weeks (Conversion_Rate_Pct average)
- **B**: Wild Edibles Guide average conversion rate in May vs. April 21–27 baseline (ratio)
- **C**: Zone Calendar average conversion rate in May vs. April 21–27 baseline (ratio)
- **D**: Total bundle revenue for May (sum of Revenue column for Spring Forager Bundle rows)
- **E**: Did any week show a Mild or Strong cannibalization signal in Gate 1?

### Decision Tree

**Step 1: Check primary metric**

Is A (average bundle conversion rate) ≥ 3.0%?

- Yes: proceed to Step 2
- No: skip to Outcome C (Failure)

**Step 2: Check cannibalization**

Are both B and C ≥ 0.85 (individual products maintained conversion rates)?

- Yes: proceed to Step 3
- No, but both ≥ 0.70: proceed to Outcome B (Ambiguous)
- No, either < 0.70: proceed to Outcome C (Failure)

**Step 3: Confirm revenue direction**

Is D (total May bundle revenue) positive and meaningful?
- This is a sanity check — if A ≥ 3% and there are conversions, D should be positive
- If D = $0 despite positive conversions: Etsy tracking error — verify manually in Etsy orders list

**Outcome A — Success**: Proceed with bundle strategy.
- Keep Spring Forager Bundle live. Do not adjust price or title.
- Create Harvest Season Bundle listing (launch June 1 per schedule).
- Begin Month 2 tracking in BUNDLE_TEST_DATA.csv.
- Note: "Month 1 — Success. Proceeding to Month 2 seasonal tracking."

**Outcome B — Ambiguous**: Bundle converts but cannibalizes.
- Keep Spring Forager Bundle live for now.
- Do NOT launch Harvest Season Bundle on June 1. Delay by 2 weeks.
- Run a 2-week pause test: on June 1, temporarily remove the Spring Forager Bundle listing (or change to "sold out" if Etsy allows). Measure whether Wild Edibles and Zone Calendar conversion rates revert to baseline in the two weeks of June.
  - If they revert: cannibalization confirmed. Reduce bundle discount to $1–2 (price to $23–24) and re-launch around June 15. Re-run Gate 1 protocol.
  - If they do not revert: seasonal traffic shift is the cause, not the bundle. Re-launch Spring Forager Bundle at $22 and launch Harvest Season Bundle on June 15.
- Note: "Month 1 — Ambiguous. Cannibalization signal present. Running 2-week pause test June 1–14."

**Outcome C — Failure**: Bundle did not meet threshold.
- Remove Spring Forager Bundle listing from Etsy immediately.
- Do NOT launch Harvest Season Bundle in June.
- Write a one-paragraph post-mortem: which metric failed (conversion rate / cannibalization / both) and the most likely root cause from this list:
  1. Pricing: $22 is not an obvious enough savings vs. $25 combined. Hypothesis: bundle needs a deeper discount or a higher perceived-value framing.
  2. Seasonal timing: buyers who find Seedwarden in May are at peak urgency for zone-specific content, not bundles. They buy the Zone Calendar alone. Test: retry Spring Forager Bundle in July when search urgency is lower and buyers browse more.
  3. Product pairing: Wild Edibles + Zone Calendar is not an intuitive pair to buyers. Hypothesis: buyers do not perceive these as "goes together." Test: pair Wild Edibles with the Seed Saving Field Manual (both forager/wild-food focused) instead.
  4. Photography/description gap: bundle listing did not communicate value clearly. Hypothesis: if lifestyle photos were not ready by May 1, the bundle listing underperformed on presentation. Test: relaunch in July with lifestyle photos.
- Note outcome and root cause in WORKLOG.md. Do not proceed to Month 2 or Month 3 tests until root cause is resolved.

---

## Gate 3 — July 1: Seasonal Demand Validation

**Run after completing the Month 2 (June) Monthly Summary in BUNDLE_TEST_TRACKING.md.**

This gate answers one question: did seasonal demand for the preservation category materialize in June? The answer determines the confidence level going into the July pricing test.

### Input: Calculate Preservation Category Revenue

**May baseline** (individual products only, since the Harvest Season Bundle was not live in May):
```
May total = sum of Revenue for Fermented Harvest Handbook + Harvest Preservation Field Manual + Grow Your Own Hot Sauce (individual product rows, all of May)
```

**June total** (individual products + Harvest Season Bundle):
```
June total = sum of Revenue for all four preservation-related rows (bundle + three individual products, all of June)
```

**Percent change:**
```
(June total - May total) / May total × 100 = seasonal demand signal %
```

### Decision Rule

| Seasonal Signal | Decision |
|---|---|
| June total > May total by 30%+ | Strong seasonal demand confirmed. Proceed with pricing test as planned. Success threshold for July test remains: 30% unit increase at $25. |
| June total > May total by 10–29% | Moderate seasonal signal. Proceed with pricing test. Raise the success bar: require 40% unit increase at $25 to justify the price cut (you need more elasticity to compensate for weaker baseline demand). |
| June total ≤ May total (flat or decline) | No seasonal demand signal in June. Proceed with pricing test anyway — a lower price may surface latent demand. Set an even higher bar: require 50% unit increase at $25. If this bar is not met, the issue is demand visibility (title/SEO/social) rather than price. |

**In all three cases**: proceed with the pricing test. The decision here adjusts the success threshold, not whether to test.

---

## Gate 4 — August 1: Pricing Decision

**Run after completing the Month 3 (July) Monthly Summary in BUNDLE_TEST_TRACKING.md.**

This gate makes the permanent pricing decision for the Harvest Season Bundle.

### Input: Pull These Values

- **Units at $28** (July 1–14): total Conversions for the Harvest Season Bundle in the two $28 weeks
- **Revenue at $28**: total Revenue for those two weeks
- **Units at $25** (July 15–31): total Conversions for the Harvest Season Bundle in the two $25 weeks (note: this period is 17 days, not 14 — normalize to per-week rate for the comparison)
- **Revenue at $25**: total Revenue for those two weeks (17-day period, normalize)
- **Success threshold**: determined at Gate 3 (30%, 40%, or 50% unit increase required)

### Normalization for Unequal Periods

July 1–14 is 14 days. July 15–31 is 17 days. To compare fairly:
```
$28 weekly rate = Units at $28 / 2 weeks
$25 weekly rate = Units at $25 / (17/7) weeks = Units at $25 / 2.43
```
Use the weekly rates for the comparison.

### Decision Tree

**Step 1: Did units at $25 increase enough to meet the Gate 3 threshold?**

```
($25 weekly rate - $28 weekly rate) / $28 weekly rate × 100 = unit elasticity %
```

Is unit elasticity % ≥ Gate 3 threshold (30% / 40% / 50%)?

- Yes: proceed to Step 2
- No: Outcome B (keep $28)

**Step 2: Did total revenue increase at $25?**

```
$25 weekly revenue vs. $28 weekly revenue — which is higher?
```

- $25 weekly revenue ≥ $28 weekly revenue: Outcome A (switch to $25)
- $25 weekly revenue < $28 weekly revenue: Outcome B (keep $28) — price cut added units but did not add revenue; the math does not support the cut

### Outcomes

**Outcome A — Set permanent price to $25.**
- Change Harvest Season Bundle price to $25.
- Update all references in bundle-listings.md and PHASE_2_BUNDLE_STRATEGY.md.
- Note: "July pricing test — $25 wins on revenue. Permanent price set."
- For Phase 3 planning: $25 is the validated anchor price for the preservation bundle tier.

**Outcome B — Keep permanent price at $28.**
- No price change needed.
- Note: "July pricing test — $28 wins or ties. Price is optimized."
- For Phase 3 planning: test $29–30 as the next upward price experiment (demand is price-inelastic; the market may absorb a slight increase).

**Outcome C — Insufficient data (fewer than 3 total units sold across both periods).**
- Do not make a pricing decision from fewer than 3 units — the sample is too small for any conclusion.
- Keep price at $28.
- In Phase 3, run the pricing test again in August or September with 60+ days of bundle visibility behind it.
- Diagnosis: if fewer than 3 units sold across July despite the bundle being live for 31 days, the problem is traffic/visibility, not price. Investigate: Is the bundle showing in Etsy search? Is the bundle title optimized for "canning bundle" or "preservation guide bundle" search terms?

---

## Catastrophic Failure Protocol

**Trigger**: Any of the following at any point during the test:

1. Bundle conversion rate <1% for two consecutive weeks during Month 1 (less than 1 sale per 100 views for two weeks in a row)
2. Individual product conversion rates drop below 50% of baseline for two consecutive weeks (cannibalization is severe)
3. A buyer leaves a negative review or sends a message indicating the bundle caused confusion about what was purchased
4. Etsy removes the listing for a policy violation

**Response** (same regardless of which trigger):

1. Remove the bundle listing immediately. Do not wait for the end of a test period.
2. Verify that individual product listings are still live and functioning.
3. Write a one-paragraph incident note in WORKLOG.md with: date, trigger, immediate action taken.
4. Do not relaunch any bundle until root cause is investigated and documented.
5. If the trigger is a negative review: respond professionally to the buyer, resolve the purchase, and treat the confusion as a product description gap — update the bundle description before any relaunch.

---

## Reading Your Numbers: Common Misinterpretations

These are the most common errors in interpreting Etsy analytics data for small-volume sellers. Avoid them.

**Misinterpretation 1: Small absolute numbers look like big percentage changes.**

Example: Week 1 bundle has 1 conversion (1.3% rate). Week 2 has 2 conversions (2.5% rate). This looks like a 92% week-over-week rate increase. It is actually just variance — 1 extra sale. Do not react to weekly percentage changes when weekly conversion counts are below 5 units.

Rule: Do not make a decision based on a single week's data unless the Catastrophic Failure Protocol is triggered. Decisions are monthly, not weekly.

**Misinterpretation 2: Confusing Etsy impressions with listing views.**

Impressions = how many times the listing appeared in a search result or related product feed. Views = how many times a buyer clicked through to the listing page. Conversion rate uses Views as the denominator, not Impressions. The BUNDLE_TEST_DATA.csv tracks both, but Conversion_Rate_Pct always uses Conversions / Views, not Conversions / Impressions.

**Misinterpretation 3: Seasonal traffic shifts misread as bundle effects.**

Etsy organic traffic shifts week-to-week based on search algorithm changes, competitor listings, and seasonal keyword demand. A 20% drop in individual product views during a week you also see a drop in bundle views is likely a traffic shift, not a bundle effect. Cross-check: if both the bundle and the individual products decline together in the same week, the cause is external (Etsy traffic down) not cannibalization.

**Misinterpretation 4: Comparing two different two-week windows without normalizing for time.**

July's pricing test uses a 14-day $28 window and a 17-day $25 window. Always normalize to a per-day or per-week rate before comparing. BUNDLE_TEST_ANALYSIS.md Gate 4 includes the normalization formula — use it.

---

## Phase 2 Bundle Test Results Summary (Complete August 1)

When all three months are complete, write a summary entry in WORKLOG.md using this structure:

```
## Phase 2 Bundle Test Results — August 2026

**Spring Forager Bundle (Month 1):**
- Outcome: [Success / Ambiguous / Failure]
- Average conversion rate: [X]%
- Cannibalization signal: [None / Mild / Strong]
- Action taken: [Description]

**Harvest Season Bundle Seasonal Demand (Month 2):**
- June vs. May preservation revenue change: [X]%
- Seasonal demand signal: [Strong / Moderate / Absent]
- Gate 3 threshold set: [30% / 40% / 50%] unit elasticity required for July test

**Harvest Season Bundle Pricing Test (Month 3):**
- $28 weekly rate: [X] units/week, $[Y] revenue/week
- $25 weekly rate: [X] units/week, $[Y] revenue/week
- Unit elasticity: [X]%
- Revenue direction: [$25 higher / $28 higher / parity]
- Permanent price decision: [$25 / $28]

**Key insight for Phase 3:**
[One sentence on what the data told you about bundle buyer behavior that should inform Phase 3 bundle strategy]
```
