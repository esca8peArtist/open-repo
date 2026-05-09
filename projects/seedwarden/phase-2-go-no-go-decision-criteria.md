---
title: "Phase 2 Go/No-Go Decision Criteria"
subtitle: "Executable decision tree for June 15, June 30, and September 1 checkpoints"
date: 2026-05-09
status: production-ready
scope: >
  Thresholds table, outcome matrix, action paths per outcome, escalation rules,
  Phase 3 (women's health) specific decision logic
checkpoints:
  - "June 15, 2026 — Day 16 post-launch: early warning"
  - "June 30, 2026 — Day 31: first monthly gate"
  - "September 1, 2026 — Day 94: Phase 3 women's health decision"
references:
  - PHASE_2_CUSTOMER_SUCCESS_FRAMEWORK.md (prediction model, tier definitions)
  - phase-2-customer-success-framework.md (v2.0 — Scenario 1/2/3/4 protocol)
  - phase-2-analytics-strategy.md (dashboard data sources)
  - phase-3-decision-framework.md (Options A/B/C/D)
---

# Phase 2 Go/No-Go Decision Criteria

**How to use this document**: Open it on each checkpoint date. Follow the steps in order.
Each step takes between 5 and 15 minutes. The decision at the end of each checkpoint is
binary or three-way — it never ends in "monitor and decide later" unless the checkpoint
itself is designated Conditional. In that case, the next checkpoint date is automatically
set for you.

**You can read this without the dashboard open.** But the decisions are faster and more
accurate if you have Etsy Shop Manager > Stats and your Google Sheets LTV tracker open
when you start.

---

## Checkpoint 1: June 15, 2026 (Day 16 Post-Launch)

### Step 1: Read the Dashboard

Open Etsy Shop Manager > Stats. Record these four numbers:

```
Date: June 15, 2026 (Day 16)

A. Total orders since May 30:          ___
B. Gross revenue since May 30:         $___
C. Conversion rate (listed in Stats):  ___%
D. Repeat purchase count
   (buyers with 2+ orders):            ___
```

Also open your Google Sheets LTV tracker and record:

```
E. Kit subscribers added since May 30:      ___
F. Phase 1 buyers who made a Phase 2
   purchase (check order_2 column):          ___  (out of 47)
```

**Time required: 10 minutes.**

---

### Step 2: Locate Your Metrics on the Thresholds Table

| Metric | Go Threshold | Conditional Threshold | No-Go Threshold |
|--------|--------------|----------------------|-----------------|
| Orders (Day 16) | 15+ | 8–14 | below 8 |
| Revenue (Day 16) | $400+ | $200–$399 | below $200 |
| Conversion rate | 2%+ | 1–2% | below 1% |
| Repeat purchases | 3+ | 1–2 | 0 |
| Kit subscribers added | 25+ | 10–24 | below 10 |
| Phase 1 buyers returned | 3+ | 1–2 | 0 |

Circle or highlight the column that matches each metric. Most metrics will cluster in the
same column. If they split across columns, go to Step 3 to resolve.

---

### Step 3: Find Your Outcome Cell

Count how many metrics land in each column:

```
Go count:           ___
Conditional count:  ___
No-Go count:        ___
```

**Resolution rule (if metrics split):**
- 4+ metrics in Go column: outcome is Go
- 4+ metrics in No-Go column: outcome is No-Go
- Everything else, or a split with no clear majority: outcome is Conditional

Record your outcome: **GO / CONDITIONAL / NO-GO**

---

### Step 4: Follow the Action Path for Your Outcome

**Action Path: GO (Day 16)**

Congratulations — launch velocity is tracking correctly. Execute these three actions before
June 22:

1. Continue current posting schedule. Do not change social content strategy. Something is
   working — do not introduce new variables.

2. Review which product had the most orders. Check its listing views vs. conversion rate in
   Etsy Stats. If conversion is above 2.5%, this listing is your current star — write one
   additional Pinterest pin for it this week.

3. Set a calendar reminder for June 30 (Day 31) as your first formal monthly gate. No other
   decisions required from this checkpoint.

**Next checkpoint: June 30.**

---

**Action Path: CONDITIONAL (Day 16)**

You have partial signal. Some metrics are on track, others are not. This is normal for Day 16
and does not require major changes — but it requires a diagnosis to prevent the metrics from
sliding to No-Go by Day 31.

Run this diagnosis. It takes 15 minutes and identifies the actual problem:

**Diagnosis Question 1: Are orders low but Kit subscribers are growing?**
If yes: you have list-building success but conversion failure. Check the top 3 listings in
Etsy Stats. If conversion rate is below 1% on any listing that has 50+ views, that listing
has a cover image or price problem — not a traffic problem. Update the cover image and the
opening sentence of the description before June 22.

**Diagnosis Question 2: Are orders and Kit both low?**
If yes: traffic is not reaching the store. Check the traffic sources in Etsy Stats. If social
referral is below 5% of traffic, the social content from launch week did not drive clicks.
This week: post one piece of high-urgency, product-focused content on Instagram with the
direct Etsy link in bio. Not educational — a direct "this guide is available now" post.

**Diagnosis Question 3: Are orders on track but Kit is flat?**
If yes: buyers are arriving through Etsy organic but not joining the email list. Check that
the Etsy listing descriptions contain the Kit landing page CTA and that the link is not broken.
If it is missing, add it today.

Set the June 30 checkpoint as your binding gate. The Conditional Day 16 outcome does not
require escalating to the user — it is a normal diagnostic moment.

**Next checkpoint: June 30. This is now the binding gate.**

---

**Action Path: NO-GO (Day 16)**

Revenue below $200 and fewer than 8 orders in 16 days is a significant underperformance
against Phase 1 baseline (which produced 47 orders in roughly 30 days with no email system).

**Escalate immediately. Contact Anya (wanka95@gmail.com) within 24 hours.**

Before contacting, pull two additional data points:

1. Total listing views across all active Phase 2 listings (from Etsy Stats). If total views
   are below 200 since launch: this is a visibility problem, not a conversion problem. The
   listings may not be indexed, or the launch social content did not generate any traffic.
   Action: verify all listings are active and not in draft status.

2. Kit: is the landing page live? Submit a test email address. If Kit does not send the
   zone card within 5 minutes, the email automation has failed and every signup since May 30
   was lost. Reactivate immediately and manually re-send the zone card to anyone who signed
   up since launch.

**Do not wait for June 30 if this checkpoint is No-Go.** The escalation path starts today.

---

### Step 5: Record and File

Write the following in WORKLOG.md before closing the document:

```
## Day 16 Go/No-Go Checkpoint — June 15, 2026
Outcome: GO / CONDITIONAL / NO-GO
Orders: ___ | Revenue: $___ | Conversion: ___% | Repeat: ___
Kit subscribers: ___ | Phase 1 returns: ___
Action taken: ___
Next checkpoint: June 30, 2026
```

---

## Checkpoint 2: June 30, 2026 (Day 31 — First Monthly Gate)

### Step 1: Read the Dashboard

This is your most important early checkpoint. By Day 31 you have a full month of data and
can make reliable pattern-level observations.

```
Date: June 30, 2026 (Day 31)

A. Total orders since May 30:          ___
B. Gross revenue (June):               $___
C. Repeat purchase rate:
   (buyers with 2+ orders / all buyers)  ___%
D. Average order value:                $___

E. Kit subscribers total:              ___
F. Phase 1 buyers who returned
   (check order_2 in LTV tracker):      ___  (out of 47)
G. Phase 1 return rate:                ___% (F ÷ 47 × 100)

H. Top product by revenue:             ___
I. Cohort distribution (estimate from
   LTV tracker cohort_tag column):
   Forager ___% | Prepper ___% |
   Homesteader ___% | Gift Buyer ___% |
   Unknown ___%
```

**Time required: 30 minutes (including LTV tracker update).**

---

### Step 2: Locate Your Metrics on the Thresholds Table

| Metric | Go Threshold | Conditional Threshold | No-Go Threshold |
|--------|--------------|----------------------|-----------------|
| Orders (Day 31) | 35+ | 20–34 | below 20 |
| Revenue (June) | $800+ | $400–$799 | below $400 |
| Repeat purchase rate | 15%+ | 8–15% | below 8% |
| AOV | $25+ | $18–$24 | below $18 |
| Phase 1 return rate | 10%+ (5+ buyers) | 4–9% (2–4 buyers) | below 4% (0–1 buyers) |
| Kit subscribers | 60+ | 30–59 | below 30 |
| Unknown cohort % | below 20% | 20–35% | above 35% |

---

### Step 3: Find Your Outcome Cell (Outcome Matrix)

Use this matrix to resolve your outcome when conversion rate and repeat purchase rate split:

```
OUTCOME MATRIX — Day 31

               | Repeat rate 15%+ | Repeat rate 8-15% | Repeat rate <8%
---------------------------------------------------------------------------
Orders 35+     | STRONG GO        | STANDARD GO       | CONDITIONAL
Orders 20-34   | STANDARD GO      | CONDITIONAL       | NO-GO
Orders <20     | CONDITIONAL*     | NO-GO             | NO-GO

* High repeat rate with low orders means a very loyal but very small cohort.
  This is a traffic problem, not a product problem.
```

**Record your cell: ___________________________**

---

### Step 4: Follow the Action Path for Your Outcome

**Action Path: STRONG GO or STANDARD GO (Day 31)**

The launch is working. Execute these actions:

1. Update LTV tracker with all June orders. Calculate each cohort's repeat rate individually.
   Identify the cohort with the highest repeat rate — that cohort gets priority in July's
   newsletter and Kit email sequence.

2. Confirm which products are Stars (high revenue + above 1.5% conversion) in the monthly
   dashboard. A Star product earns a dedicated Pinterest board, additional pin production,
   and a featured position in Campaign 3 (cross-zone upsell email).

3. Set September 1 as the Phase 3 go/no-go date on your calendar. No Phase 3 decisions
   before then. Between now and September 1: focus entirely on Phase 2 cohort deepening.

4. If STRONG GO: begin drafting the September 1 Phase 3 checklist (Checkpoint 3 below).
   The Women's Health bundle content development requires 7–10 weeks; if Phase 3 launches
   September 15, content development must start by July 15 at the latest. STRONG GO at Day 31
   gives you a 2-week head start.

**Next checkpoint: September 1.**

---

**Action Path: CONDITIONAL (Day 31)**

Partial signal. Diagnose before setting the September 1 checkpoint as binding.

The most common Day 31 Conditional pattern is: decent order volume but low repeat rate. This
means new buyers are coming in but the email retention sequence is not triggering second
purchases. The diagnosis sequence:

**Diagnosis Step 1:** Open Kit > Automations > Campaign 3 (cross-zone upsell). Check the
activity log. How many emails sent in June? If fewer than 10 (and you had 20+ orders in June),
Campaign 3 is not triggering. Most likely cause: the trigger condition is set to require the
`vip` tag, but buyers are not receiving the `vip` tag because they have not yet reached the
two-purchase threshold. Temporarily set Campaign 3 to trigger on `purchased` tag instead of
`vip`. Fire it for all June buyers immediately.

**Diagnosis Step 2:** Is the low repeat rate concentrated in one cohort? Filter the LTV tracker
by cohort_tag. If Gift Buyer cohort is 25%+ of buyers, a low aggregate repeat rate is expected
and normal — gift buyers do not repeat at 30 days. Recalculate repeat rate excluding gift
buyers. If the non-gift repeat rate is above 12%, you have a healthy core with a gift-buyer
overhang. This is a segmentation finding, not a retention failure.

**Diagnosis Step 3:** Is the Unknown cohort above 25%? If yes, the post-purchase survey is
not reaching buyers. Check the Kit sequence: the cohort survey link should appear in Campaign
1 Email 2 (Day 7). If it is missing or broken, add it immediately and re-send Email 2 to all
June buyers who have not completed the survey.

Set July 15 as an interim checkpoint. Run a quick 15-minute assessment on July 15: has repeat
rate moved above 10%? If yes: September 1 becomes the Phase 3 gate. If still below 8% at July 15:
escalate to Anya before September 1 because Phase 3 launch may need to move to January 2027.

**Next checkpoint: July 15 (interim), then September 1.**

---

**Action Path: NO-GO (Day 31)**

Below 20 orders and below 8% repeat rate at Day 31 is a structural issue, not a bad week.

**Escalate to Anya immediately (wanka95@gmail.com). Phase 3 is paused.**

Before the escalation call, prepare this diagnostic summary:

```
NO-GO DIAGNOSTIC BRIEF — [DATE]
=================================
Orders in 31 days:        ___ (below threshold: 20)
Revenue:                  $___ (below threshold: $400)
Repeat rate:              ___% (below threshold: 8%)

Root cause hypothesis (circle one):
  TRAFFIC PROBLEM — total Etsy listing views below 1,000 in June
  CONVERSION PROBLEM — views above 1,000 but orders below 20
  EMAIL PROBLEM — Kit open rate below 25% or Campaign 3 not firing
  PRODUCT PROBLEM — all listings below 1% conversion despite adequate traffic

Evidence for hypothesis:
  Etsy listing views (June total): ___
  Top listing conversion rate: ___%
  Kit Email 1 open rate: ___%
  Campaign 3 sent in June: ___ (number of emails)

Recommended action by hypothesis:
  TRAFFIC: increase social posting frequency to 2x/day for 2 weeks;
           review Pinterest board SEO
  CONVERSION: revise cover images and description hooks on top 3 listings
  EMAIL: test Kit automation with a fresh test subscriber; fix broken trigger
  PRODUCT: pull the 3 lowest-performing listings and rewrite from scratch
```

**Auto-execute decision if No-Go:** Phase 3 September 1 date is suspended. Women's Health
tier development does not begin. Focus all work on Phase 2 recovery. Revisit Phase 3 timing
at the October 1 monthly review.

---

### Step 5: Record and File

```
## Day 31 Go/No-Go Checkpoint — June 30, 2026
Outcome: STRONG GO / STANDARD GO / CONDITIONAL / NO-GO
Orders: ___ | Revenue: $___ | Repeat rate: ___% | AOV: $___
Phase 1 return rate: ___% (___ of 47) | Kit subscribers: ___
Top product: ___
Cohort mix: Forager ___% | Prepper ___% | Homesteader ___% | Gift ___% | Unknown ___%
Action taken: ___
Phase 3 September 1 decision date: CONFIRMED / DEFERRED TO [DATE]
```

---

## Checkpoint 3: September 1, 2026 (Day 94 — Phase 3 Women's Health Decision)

### Step 1: Read the Dashboard (Full Pull — Allow 45 Minutes)

This is the binding Phase 3 decision date. Pull all of these:

```
Date: September 1, 2026 (Day 94)

A. Total Phase 2 orders (May 30–Aug 31):    ___
B. Total gross revenue (June–August):       $___
C. Average monthly revenue (B ÷ 3):        $___
D. Overall repeat purchase rate:
   (buyers with 2+ orders / all buyers)     ___%
E. Phase 1 return rate (cumulative):
   ___ of 47 Phase 1 buyers returned        = ___%
F. Average order value:                     $___
G. Kit total subscribers:                   ___
H. Kit active (opened any email in 30 days):___

COHORT-SPECIFIC DATA (from LTV tracker):
I.  Herbalist/Medicinal buyers (count):     ___
J.  Herbalist % of all buyers:              ___% (I ÷ total buyers × 100)
K.  Herbalist average LTV:                  $___
L.  Herbalist 30-day repeat rate:           ___%

M.  Homesteader buyers (count):             ___
N.  Homesteader 30-day repeat rate:         ___%
O.  Homesteader average LTV:                $___

WOMEN'S HEALTH SPECIFIC:
P.  Did any Phase 2 product target women's
    health or reproductive wellness?         YES / NO
Q.  If YES — that product's order count:    ___
```

---

### Step 2: Thresholds Table — Phase 3 Women's Health

| Metric | Go Threshold | Conditional Threshold | No-Go Threshold |
|--------|--------------|----------------------|-----------------|
| Monthly revenue avg (C) | $1,200+ | $600–$1,199 | below $600 |
| Repeat purchase rate (D) | 25%+ | 15–25% | below 15% |
| Phase 1 return rate (E) | 15%+ (7+ buyers) | 8–14% (4–6 buyers) | below 8% (0–3) |
| Herbalist segment (J) | 15%+ of buyers | 8–14% of buyers | below 8% |
| Herbalist LTV (K) | $40+ | $25–$39 | below $25 |
| AOV trend (F vs. Phase 1 $28.54) | 20%+ above ($34+) | flat to +20% ($28–$33) | below Phase 1 ($28-) |

---

### Step 3: Phase 3 Decision Logic (Women's Health Specific)

**The Phase 3 Women's Health decision has two gates, not one.** Both must pass for a Go:

**Gate 1 — Business viability (is Phase 2 strong enough to support Phase 3 launch?):**
Monthly revenue above $600 AND repeat rate above 15%.

**Gate 2 — Herbalist audience confirmed (is the target audience for Women's Health present?):**
Herbalist segment above 8% of buyers AND Herbalist LTV above $25.

If both gates pass: GO.
If Gate 1 passes but Gate 2 fails: Conditional — Phase 3 pivots to a different tier (see below).
If Gate 1 fails: No-Go on all Phase 3, regardless of Gate 2.

---

### Step 4: Action Paths

**Action Path: GO — Women's Health Phase 3 Launch**

Both gates passed. Phase 3 development begins within 7 days of September 1.

1. **By September 8:** Begin content development for Women's Health themed bundle (minimum 3
   herb profiles for the bundle: red raspberry leaf, chaste tree, ashwagandha — highest search
   volume herbalism-and-women-health intersections). Use the Canva templates in `phase-3-assets/`
   for mockup production.

2. **By September 15:** Etsy listing for Women's Health Bundle Live (at minimum a pre-order
   listing or a single-guide listing to test demand while full bundle is completed).

3. **By September 15:** Send Kit broadcast to Herbalist segment specifically — not a general
   broadcast. Subject line should reference the bundle without using promotional language:
   "The herbs most commonly asked about for women's hormonal health" with a CTA to the new guide.

4. **Practitioner outreach (if Herbalist LTV is above $40 and repeat rate above 25%):**
   Begin B2B outreach to herbalism schools, doula networks, midwifery training programs.
   Use B2B_DISTRIBUTION_STRATEGY.md Tier 2 templates. This is an optional amplification step,
   not a Phase 3 requirement.

Revenue expectation: Women's Health tier adds $600–$1,200/month by December 2026 at a
conservative 1.5% conversion from existing Herbalist segment traffic.

---

**Action Path: CONDITIONAL — Gate 1 Passes, Gate 2 Fails (Herbalist Absent)**

Business is viable but the Women's Health audience has not materialized in Phase 2 data. The
medicinal herb content did not build a distinct practitioner segment.

This does not mean women's health is not viable — it means the September launch window is the
wrong entry point. Instead:

1. **September 2026 Phase 3 launch alternative:** Launch an expansion of the Forager or
   Homesteader tier instead. If homesteader repeat rate (N) is above 20%: launch the Seed
   Library System concept (a seed saving deep-dive product line). This is lower risk because
   the audience is already confirmed present and purchasing.

2. **Herbalist audience building (September–December):** The ginseng season broadcast (September
   content calendar) becomes a Herbalist acquisition tool. Create one piece of highly specific
   medicinal content per month from September through December. Measure Herbalist segment growth.
   If it reaches 12%+ by January 1, 2027: launch Women's Health tier January 15, 2027 (aligned
   with New Year wellness resolution buying pattern — a naturally higher-intent window than
   September anyway).

3. **Set October 1 as a mini-checkpoint:** Has Herbalist segment grown since September 1? If it
   is growing at 2+ new herbalist buyers per week, the audience is building and January launch
   is confirmed. If still flat at October 1, escalate to Anya: Women's Health tier may need to
   be deprioritized in favor of a tier with confirmed demand.

---

**Action Path: NO-GO — Gate 1 Fails**

Monthly revenue below $600 after 3 months means Phase 2 has not established itself as a
sustainable revenue source. Launching Phase 3 would divide execution resources across two
unproven tiers without either having the buyer base to justify development investment.

**Auto-execute immediately:**

1. Phase 3 September launch is cancelled. No new product development begins.

2. Focus for September–October: diagnose the specific Phase 2 failure mode using the v2.0
   framework's Churn Risk protocol (Section 4, Scenario 3). Is the problem traffic, conversion,
   or product? Each has a specific 2-week remediation sequence.

3. Set Phase 3 reconsideration date: January 1, 2027. If Phase 2 reaches $600+/month by
   December, recalibrate Phase 3 for Q1 2027. If Phase 2 is still below $400/month in December,
   a deeper strategic review with Anya is required before any Phase 3 investment.

4. **Escalate to Anya (wanka95@gmail.com) within 48 hours of September 1 if No-Go.** The
   user needs to decide whether to continue Phase 2 recovery or pivot the product strategy
   entirely. This is not a decision an automated framework can make — it requires the operator.

---

### Step 5: Escalation Rules Summary

| Situation | Who Decides | Timing |
|-----------|-------------|--------|
| Day 16 GO or CONDITIONAL | Auto-execute per action path | Same day |
| Day 16 NO-GO | Escalate to Anya immediately | Within 24 hours |
| Day 31 STRONG GO or STANDARD GO | Auto-execute per action path | Same day |
| Day 31 CONDITIONAL | Auto-execute diagnosis; set July 15 interim | Same day |
| Day 31 NO-GO | Escalate to Anya immediately | Within 24 hours |
| September 1 GO | Auto-execute Phase 3 development | Within 7 days |
| September 1 CONDITIONAL (Gate 2 fail) | Auto-execute pivot; set October 1 mini-check | Within 7 days |
| September 1 NO-GO | Escalate to Anya within 48 hours | Within 48 hours |
| Any Day 7 NPS score below 6 | Personal reply to buyer + escalate | Same day |
| 0 orders for 5+ consecutive days | Escalate to Anya | Same day |

**"Escalate to Anya" means**: send a message to wanka95@gmail.com with the diagnostic brief
(metrics, root cause hypothesis, evidence, recommended action). The message does not need to
be long — the diagnostic template in the Day 31 No-Go section is the format. State the
outcome label (NO-GO), the most likely root cause, and the recommended immediate action.
The framework has already done the diagnosis; escalation is the handoff.

---

### Step 5: Record and File

```
## September 1 Phase 3 Decision — Day 94
Outcome: GO / CONDITIONAL (Gate 2 fail) / NO-GO

Business viability gate (Gate 1):
  Monthly avg revenue: $___ — PASS / FAIL (threshold: $600+)
  Repeat rate: ___% — PASS / FAIL (threshold: 15%+)

Herbalist audience gate (Gate 2):
  Herbalist % of buyers: ___% — PASS / FAIL (threshold: 8%+)
  Herbalist LTV: $___ — PASS / FAIL (threshold: $25+)

Phase 3 decision:
  Women's Health September launch: CONFIRMED / DEFERRED / CANCELLED
  Alternative September launch (if conditional): ___
  January 2027 Women's Health date: CONFIRMED / TBD

Escalation sent to Anya: YES / NO
Action items arising:
  1. ___
  2. ___
  3. ___
```

---

## Reference: Full Thresholds Table (All Checkpoints)

| Metric | Go | Conditional | No-Go | Checkpoint |
|--------|-----|-------------|-------|------------|
| Day 16 orders | 15+ | 8–14 | below 8 | June 15 |
| Day 16 revenue | $400+ | $200–$399 | below $200 | June 15 |
| Day 16 repeat count | 3+ | 1–2 | 0 | June 15 |
| Day 16 Kit subscribers | 25+ | 10–24 | below 10 | June 15 |
| Day 31 orders | 35+ | 20–34 | below 20 | June 30 |
| Day 31 revenue | $800+ | $400–$799 | below $400 | June 30 |
| Day 31 repeat rate | 15%+ | 8–15% | below 8% | June 30 |
| Day 31 Phase 1 return rate | 10%+ | 4–9% | below 4% | June 30 |
| Day 94 monthly avg revenue | $1,200+ | $600–$1,199 | below $600 | Sept 1 |
| Day 94 repeat rate | 25%+ | 15–25% | below 15% | Sept 1 |
| Day 94 Phase 1 return rate | 15%+ | 8–14% | below 8% | Sept 1 |
| Day 94 Herbalist % | 15%+ | 8–14% | below 8% | Sept 1 |
| Day 94 Herbalist LTV | $40+ | $25–$39 | below $25 | Sept 1 |
| Day 94 AOV vs Phase 1 | +20%+ ($34+) | flat–+20% | below Phase 1 | Sept 1 |

---

*Prepared: 2026-05-09. This document is intended to be standalone — the user can execute
all checkpoints using only this document plus the Etsy Shop Manager dashboard, Google Sheets
LTV tracker, and Kit dashboard. No other documents are required during a checkpoint session.
For full context on prediction model tiers, segmentation logic, and seasonal calendar,
see `PHASE_2_CUSTOMER_SUCCESS_FRAMEWORK.md`. For the full Scenario 1/2/3/4 protocol and
Day 1 launch activation, see `phase-2-customer-success-framework.md` (v2.0).*
