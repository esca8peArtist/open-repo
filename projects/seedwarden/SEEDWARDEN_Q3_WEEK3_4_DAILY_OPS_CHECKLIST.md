---
title: "Seedwarden Q3 Week 3-4 Daily Operations Checklist"
date: 2026-07-13
version: 1.0
status: production-ready
sprint-window: July 13 – July 27, 2026
scope: "Day-by-day execution tasks for Sleep bundle (Jul 13), Practitioner tier (Jul 15), Immunity bundle (Jul 20) launches plus peak Week 3-4 revenue tracking"
cross-references:
  - SEEDWARDEN_Q3_WEEK1_2_EXECUTION_MASTER_CHECKLIST.md (Week 1-2 baseline)
  - SEEDWARDEN_Q3_WEEK3_4_CONTRACTOR_DELIVERY_ESCALATION.md (contractor triggers)
  - SEEDWARDEN_Q3_WEEK3_4_SOCIAL_DEEP_DIVE.md (per-platform engagement)
  - SEEDWARDEN_Q3_WEEK3_4_CHURN_MONITORING.md (subscriber tracking)
  - SEEDWARDEN_Q3_WEEK5_6_CONTINGENCY_TRIGGERS.md (downstream contingency)
---

# Seedwarden Q3 Week 3-4 Daily Operations Checklist

**Scope**: Week 3 (Jul 13-19) and Week 4 (Jul 20-27) day-by-day task execution for three bundle launches: Sleep and Nervines (Jul 13), Practitioner Tier (Jul 15), Immunity Support (Jul 20). All times UTC unless otherwise noted. All thresholds are explicit; no judgment calls required at execution time.

**Revenue tracking baseline**: Establish from Week 1-2 actuals. If Week 1-2 revenue data is not yet available at time of Week 3 activation, use the Week 1-2 targets from SEEDWARDEN_Q3_WEEK1_2_EXECUTION_MASTER_CHECKLIST.md as the baseline proxy.

---

## Pre-Week 3 Gate (Jul 12, by 18:00 UTC)

Run this gate the evening before Sleep bundle launch. All items must be checked before proceeding.

### Contractor Photo Verification Gate

- [ ] Photographer Session 2 images received (Sleep bundle herbs: chamomile, passionflower, valerian, lemon balm, lavender)
  - Verify: 5 images delivered, naming convention `sleep-[type]-[seq].jpg`, min 2000×2000px, sRGB
  - If NOT received by Jul 12 18:00 UTC: ACTIVATE Sleep backup template immediately (do not wait for Jul 13 morning)

**Photo Contingency Trigger — Jul 12 18:00 UTC**:
```
IF Sleep bundle photos not confirmed received by Jul 12 18:00 UTC:
  → ACTIVATE: Switch Etsy listing to backup template using licensed herb photos
    (See SEEDWARDEN_Q3_WEEK3_4_CONTRACTOR_DELIVERY_ESCALATION.md, Section 4.1)
  → NOTIFY contractor immediately with deadline: "Photos needed by Jul 13 06:00 UTC
    or we proceed with backup images for launch"
  → Log activation in PHASE_3_EXECUTION_LOG.md with timestamp
  → DO NOT delay Jul 13 launch for missing photos
```

### Platform Readiness Gate (Jul 12 20:00 UTC)

- [ ] Kit.com email draft for Sleep bundle loaded and verified (subject line, body, CTA link to Sleep Etsy listing)
- [ ] Sleep Etsy listing created in DRAFT status (not yet published); all fields complete
- [ ] Sleep social posts (Instagram, LinkedIn) drafted and queued in scheduling tool for Jul 13 09:00 ET / 14:00 UTC
- [ ] Metrics dashboard (Google Sheets) ready to receive Week 3 data (new rows for Jul 13+)
- [ ] Week 1-2 revenue total confirmed and logged as baseline (entry field: "W1-2 Revenue Baseline")

---

## Week 3, Day 1 — Jul 13 (Sleep and Nervines Launch)

### Morning Preparation Block (07:00–08:00 UTC)

- [ ] Final photo check: Confirm Sleep bundle images are uploaded to Etsy draft listing
  - If backup template was activated (Jul 12 contingency): confirm backup images are in place
- [ ] Email pre-send verification: Run 10-point pre-send checklist from SEEDWARDEN_Q3_DAILY_EMAIL_MONITORING_CHECKLIST.md (Part 1)
  - Subject line: no spam phrases, 40-60 chars, preview text differs from subject
  - All CTA links resolve to live Sleep Etsy listing (not 404)
  - Unsubscribe link present and functional
  - Send time confirmed: 13:00 UTC (09:00 ET)
- [ ] Confirm Practitioner Tier brief prepared: Practitioner launch is Jul 15; today's task is confirmation only, no Practitioner publish yet

### Launch Block (08:00–14:30 UTC)

**09:00 ET / 13:00 UTC: Email Send**
- [ ] Send Sleep and Nervines email to full subscriber list
  - Copy subject line and recipient count to execution log before sending
  - Execution log entry: "Jul 13, 13:00 UTC: Email sent to [#] recipients"

**09:30 ET / 13:30 UTC: Etsy Listing Go-Live**
- [ ] Publish Sleep Etsy listing (change DRAFT to ACTIVE)
- [ ] Verify listing appears on Etsy (search "sleep herbs bundle" — listing should appear within 1-4 hours)
- [ ] Copy Etsy listing URL to execution log

**10:00 ET / 14:00 UTC: Social Posts**
- [ ] Instagram post: Launch visual with Sleep bundle herbs, CTA to Etsy listing
- [ ] LinkedIn post: Educational angle ("Why valerian and passionflower work together for sleep")
  - Do NOT include Etsy link in LinkedIn post body — add link in first comment within 5 minutes of publishing
- [ ] Log: "Jul 13, 14:00 UTC: Social posts published — [Instagram URL], [LinkedIn URL]"

### Monitoring Block (14:00–22:00 UTC)

**T+1hr Email Delivery Check (14:00 UTC)**
- [ ] Kit.com delivery rate: target >95%
  - GREEN (>95%): log and proceed
  - YELLOW (90-95%): log, monitor
  - RED (<90%): halt next planned send; escalate per SEEDWARDEN_Q3_DAILY_EMAIL_MONITORING_CHECKLIST.md PROCEDURE 1

**Etsy Live Verification (15:00 UTC)**
- [ ] Confirm listing is searchable (search "sleep herbal guide" or "sleep nervines bundle")
- [ ] Confirm first 3 product images load correctly
- [ ] Confirm price, shipping, and description are accurate

**End-of-Day Metrics (22:00 UTC)**
- [ ] Record in Google Sheets metrics dashboard:
  - Email: delivery rate %, open count (partial — full count at T+24hr), click count (partial)
  - Etsy: impressions (from Etsy Stats dashboard), views, orders (Day 1 expected: 0-5)
  - Revenue: Day 1 total ($0 or first orders × Sleep bundle price)
  - Social: likes + comments across all platforms (Instagram + LinkedIn)
- [ ] Unsubscribe count: Kit.com > Subscribers > Unsubscribes > last 24 hours
  - Calculate rate: count / total subscribers × 100
  - Apply threshold: <0.3% GREEN, 0.3-0.5% YELLOW, >0.5% RED (see SEEDWARDEN_Q3_WEEK3_4_CHURN_MONITORING.md)

### Execution Log Entry (End of Jul 13)

```
Jul 13 LAUNCH DAY LOG
Email send: 13:00 UTC | Recipients: [#] | Delivery: [%]
Etsy listing: LIVE at [URL]
Instagram post: [URL] | Likes at EOD: [#] | Comments: [#]
LinkedIn post: [URL] | Engagement rate: [%]
Orders (Day 1): [#] | Revenue (Day 1): $[amount]
Unsubscribes: [#] ([%]) | Status: GREEN/YELLOW/RED
Contractor photo status: [Original / Backup template] | Photographer notified: Y/N
Notes: [Any unexpected events, escalations, or issues]
```

---

## Week 3, Day 2 — Jul 14

### Morning Check (09:00 ET / 13:00 UTC)

**T+24hr Email Metrics**
- [ ] Open rate at T+24hr (13:00 UTC):
  - GREEN (>22%): log, no action
  - YELLOW (15-22%): log, draft A/B subject line for next email (Email 4, Immunity Jul 20)
  - RED (<15%): run spam placement test immediately; escalate per SEEDWARDEN_Q3_DAILY_EMAIL_MONITORING_CHECKLIST.md PROCEDURE 2
- [ ] Click rate at T+24hr:
  - GREEN (>3%): log, no action
  - YELLOW (1-3%): audit CTA text and placement
  - RED (<1% with opens GREEN or YELLOW): CTA is broken; revise template for Email 4

**Practitioner Tier Pre-Staging (deadline: today by 18:00 UTC)**
- [ ] Practitioner Tier Etsy listing created in DRAFT status
- [ ] Practitioner email draft created in Kit.com (separate email; Practitioner is a separate workflow from standard bundle emails)
- [ ] Practitioner social content queued for Jul 15 09:00 ET

**Photo Contingency Resolution**
- [ ] If Sleep bundle photos were delivered late: run photographer quality gate (Section 3.1 of SEEDWARDEN_Q3_CONTRACTOR_DELIVERABLE_TRACKING.md)
- [ ] If quality gate passes: swap backup images for original photographer images in Etsy listing (update listing photos)
- [ ] If backup template is still in use: note in log; no further action needed unless orders were impacted

### Afternoon Check (14:00 ET / 18:00 UTC)

- [ ] Etsy Sleep listing: check impressions (target: 20-50 by Day 2)
  - If <10 impressions by Day 2 18:00 UTC: verify listing tags (13-15 tags required), confirm listing is Active (not Draft)
- [ ] Respond to any customer questions or comments (within 4 hours of message receipt)

### End-of-Day Metrics (22:00 UTC)

- [ ] Log to Google Sheets: same 8 fields as Jul 13
- [ ] Unsubscribe daily rate: calculate and apply threshold
- [ ] Practitioner Tier prep status: [READY / BLOCKED by: ___]

---

## Week 3, Day 3 — Jul 15 (Practitioner Tier Launch)

**Context**: Practitioner Tier is a separate, higher-price product targeting clinical herbalists and practitioners. It has its own email, its own Etsy listing, and its own social content. It does NOT replace the Sleep bundle follow-up monitoring, which continues in parallel.

### Practitioner Tier Launch (separate workflow from Sleep bundle)

**Photo Gate Check (08:00 UTC)**
- [ ] Confirm Practitioner Tier product images are in place
  - If Practitioner Tier photos not confirmed by Jul 14 18:00 UTC: this contingency should have been activated yesterday
  - If it was not activated: ACTIVATE NOW with same backup protocol as Sleep bundle
  - Log contingency status

**Launch Block (09:00-14:30 UTC)**
- [ ] 09:00 ET / 13:00 UTC: Send Practitioner Tier email (separate from main bundle email)
  - This goes to a SEGMENTED list: practitioners, herbalists, clinical professionals (NOT full list)
  - Verify segment is correct before send
- [ ] 09:30 ET / 13:30 UTC: Publish Practitioner Tier Etsy listing
- [ ] 10:00 ET / 14:00 UTC: Post Practitioner-specific social content
  - LinkedIn: Professional framing ("For clinical herbalists: evidence-based species monographs with dosage + contraindications")
  - Instagram: Visual product shot + practitioner use-case CTA

**Sleep Bundle Day 3 Monitoring (parallel track)**
- [ ] Sleep bundle Etsy impressions: cumulative target through Day 3 = 30-80 impressions
  - If <20 cumulative impressions by Day 3 18:00 UTC: re-verify tags + listing status; repost social content with new angle
- [ ] Sleep bundle orders cumulative (Days 1-3): target 1-5 orders
  - If 0 orders through Day 3: check price competitiveness and listing CTR; see incident response below

**Incident Response: Zero Sleep Orders by Jul 15**
```
IF Sleep bundle has 0 orders by Jul 15 18:00 UTC:
  Step 1: Check Etsy Stats — impressions and CTR
    - If impressions >30 but 0 orders: conversion problem (price, photos, description)
    - If impressions <20: discoverability problem (SEO tags, listing not indexed)
  Step 2: If conversion problem:
    - Review price vs. comparable bundles on Etsy (target: competitive within ±15%)
    - Review first product photo: is it professional and appealing?
    - Add "what's inside" summary to first 3 lines of description
  Step 3: If discoverability problem:
    - Edit listing title to include high-volume keyword ("herbal sleep guide" or "nervines herbal bundle")
    - Add 2-3 missing tags from Etsy's suggested tags panel
    - Republish listing
  Step 4: Log findings and actions in PHASE_3_EXECUTION_LOG.md
  Step 5: Monitor 48 hours post-adjustment; if still 0 orders by Jul 17, escalate to SEEDWARDEN_Q3_WEEK5_6_CONTINGENCY_TRIGGERS.md Section 2
```

### End-of-Day Metrics (22:00 UTC) — Both Tracks

- [ ] Log to Google Sheets:
  - Sleep bundle row: impressions, views, orders, revenue, social engagement
  - Practitioner Tier row: email open rate (T+24hr check Jul 16), Etsy impressions, orders, revenue
- [ ] Combined daily revenue for Jul 15: Sleep + Practitioner Tier combined
- [ ] Unsubscribe rate: calculate across full list (both sends combined)

---

## Week 3, Days 4-5 — Jul 16-17 (Sustain and Monitor)

### Daily Routine (both days, same structure)

**Morning Check (09:00 ET)**
- [ ] Previous day Etsy stats (Sleep + Practitioner): impressions, views, orders
- [ ] Email open/click rate final (T+48hr for Jul 13 email): final open rate recorded; compare to Week 1-2 baseline
- [ ] Respond to any new customer messages or reviews (within 4 hours)

**Practitioner Tier T+24hr and T+48hr Checks (Jul 16 morning)**
- [ ] Jul 16 09:00 UTC: Practitioner Tier email T+24hr open rate
  - Practitioner Tier is a segmented list (practitioners), so open rates are EXPECTED to be higher than main list
  - GREEN (>28%): engaged professional audience; log and proceed
  - YELLOW (20-28%): acceptable; no action
  - RED (<20%): investigate; practitioners are a high-intent segment — low opens suggest delivery or targeting issue

**Social Monitoring (Jul 16-17)**
- [ ] LinkedIn post from Jul 15 (Practitioner): check engagement rate at T+48hr
  - This post should be educational/professional; target engagement rate >8% (practitioners engage more)
- [ ] Instagram post from Jul 13 (Sleep): check saves + shares (saves indicate high interest)
- [ ] Log all platform metrics to Google Sheets

**Revenue Tracking (daily)**
- [ ] Daily revenue entry: [Sleep orders × price] + [Practitioner orders × price]
- [ ] Cumulative Week 3 revenue running total
- [ ] Compare cumulative to Week 1-2 daily average (Week 1-2 daily avg = Week 1-2 total ÷ 14 days)
  - If Week 3 daily revenue <80% of Week 1-2 daily average: note in log; no escalation yet
  - If Week 3 daily revenue <60% of Week 1-2 daily average for 3 consecutive days: escalate to SEEDWARDEN_Q3_WEEK5_6_CONTINGENCY_TRIGGERS.md

---

## Week 3, Days 6-7 — Jul 18-19 (Immunity Bundle Pre-Staging)

### Jul 18: Immunity Bundle Preparation Gate

- [ ] Immunity bundle Etsy listing created in DRAFT status
- [ ] Immunity email draft loaded in Kit.com (Email 4 per SEEDWARDEN_Q3_DAILY_EMAIL_MONITORING_CHECKLIST.md send schedule)
- [ ] Immunity social content (Instagram + LinkedIn) drafted and queued for Jul 20
- [ ] Immunity product images confirmed:
  - Photographer Session 3 should be received or in progress (goldenseal, ashwagandha, elderberry, echinacea)
  - If Session 3 photos not confirmed by Jul 18 18:00 UTC: activate photographer escalation Level 2 (SEEDWARDEN_Q3_WEEK3_4_CONTRACTOR_DELIVERY_ESCALATION.md, Section 3)
- [ ] CITES sidebar (goldenseal) confirmed present in Immunity bundle content: "verbatim sidebar" check per SEEDWARDEN_Q3_CONTRACTOR_DELIVERABLE_TRACKING.md Gate 1, item 4

**Jul 18 Immunity Pre-Stage Gate (18:00 UTC)**
- [ ] Immunity listing DRAFT complete and peer-reviewed
- [ ] Immunity email: all pre-send checks complete (subject, preview, CTA link, unsubscribe link)
- [ ] Immunity social: posts queued for Jul 20 09:00 ET / 14:00 UTC
- [ ] Photographer Session 3 status confirmed (received / in progress / contingency activated)

If any item above is NOT checked by Jul 18 18:00 UTC:
```
GATE FAILURE — Jul 18 Pre-Stage Gate
Status: BLOCKED on [specific item]
Action: Do not proceed with Jul 20 Immunity launch until blocker is resolved
Escalation: Activate SEEDWARDEN_Q3_WEEK5_6_CONTINGENCY_TRIGGERS.md only if launch must be delayed >48hrs
Note: A 24-hour delay (Jul 21 instead of Jul 20) is acceptable without triggering contingency
```

### Jul 19: Final Immunity Pre-Launch Verification

Same structure as Jul 12 Pre-Week 3 Gate:
- [ ] All images in place (Session 3 or backup)
- [ ] Email pre-send verification complete
- [ ] Social posts scheduled
- [ ] Metrics dashboard rows added for Jul 20 Immunity launch

---

## Week 3 Final Checkpoint (Jul 19 evening, by 22:00 UTC)

### Revenue Tracking Checkpoint

Log to Google Sheets "Week 3 Summary" row:

```
Week 3 (Jul 13-19) Summary
Sleep bundle: [#] orders | Revenue: $[amount]
Practitioner Tier: [#] orders | Revenue: $[amount]
Week 3 total revenue: $[amount]
Week 1-2 baseline (daily avg × 7): $[expected]
Week 3 vs baseline: [+/-]% variance

Revenue status:
[ ] GREEN: Week 3 revenue ≥80% of Week 1-2 daily average × 7
[ ] YELLOW: Week 3 revenue 60-80% of baseline
[ ] RED: Week 3 revenue <60% of baseline
  → If RED: activate SEEDWARDEN_Q3_WEEK5_6_CONTINGENCY_TRIGGERS.md Section 1
```

### Contractor Delivery Checkpoint

```
Photographer:
  Session 2 (Sleep): [DELIVERED and APPROVED / PENDING / BACKUP USED]
  Session 3 (Immunity): [DELIVERED / IN PROGRESS / OVERDUE by [# days]]
  Session 3 overdue action taken: [None / Level 1 / Level 2 / Contingency]

Writers:
  Immunity draft (due Jul 18): [DELIVERED and APPROVED / PENDING / REVISION IN PROGRESS]
  Digestive draft (due Jul 22): [Upcoming / At risk]

Specialists:
  Arthur Haines (NE notes revision, due Jul 20): [DELIVERED / PENDING]
```

### Engagement Trending Checkpoint

```
Email performance trend (Emails 1-3):
  Email 1 (Jun 29) open rate: [%]
  Email 2 (Jul 6) open rate: [%]
  Email 3 (Jul 13) open rate: [%]
  Trend: [Stable / Declining / Recovering]

IF Email 3 open rate <15%:
  → Fatigue confirmed. Email 4 (Jul 20) adjusted per SEEDWARDEN_Q3_DAILY_EMAIL_MONITORING_CHECKLIST.md
    PROCEDURE 5: extend gap to Jul 27 AND/OR shift to value-frame subject line.
  → Document decision here: [Proceeding as planned Jul 20 / Adjusted to Jul 27]

Social engagement trend (Week 3 vs Week 1-2):
  Week 1-2 avg daily engagement: [#] interactions
  Week 3 avg daily engagement: [#] interactions
  Platform-level status: See SEEDWARDEN_Q3_WEEK3_4_SOCIAL_DEEP_DIVE.md
```

---

## Week 4, Day 1 — Jul 20 (Immunity Support Launch)

### Pre-Launch Gate Check (08:00 UTC)

- [ ] All Pre-Stage items from Jul 19 confirmed
- [ ] Immunity product images live in Etsy DRAFT listing (Session 3 or backup)
- [ ] Email send verified and ready

### Launch Block (09:00-14:30 UTC)

**09:00 ET / 13:00 UTC: Immunity Email Send**
- [ ] Send Immunity Support email to subscriber list (main list, not segmented)
  - Note: if Email 3 fatigue was confirmed (open rate <15%), this send may have been shifted to Jul 27 per PROCEDURE 5. If shifted, do NOT send today — send Jul 27 instead. Log date decision.
  - If sending today: record subject line, recipient count, send time in execution log

**09:30 ET / 13:30 UTC: Immunity Etsy Go-Live**
- [ ] Publish Immunity Etsy listing (DRAFT → ACTIVE)
- [ ] Verify listing searchable within 2 hours: search "immunity herbs bundle" or "immune support herbal guide"

**10:00 ET / 14:00 UTC: Immunity Social Posts**
- [ ] Instagram: Immunity bundle visual + "Peak season" angle (summer immune prep)
- [ ] LinkedIn: Educational angle ("Elderberry vs. echinacea: which works for which stage of illness")

### End-of-Day Metrics (22:00 UTC)

- [ ] Log to Google Sheets:
  - Immunity bundle: delivery rate %, orders, revenue, Etsy impressions, social engagement
  - Practitioner Tier ongoing: cumulative orders and revenue since Jul 15
  - Sleep bundle ongoing: cumulative orders since Jul 13
- [ ] Combined daily revenue Jul 20: all three active products
- [ ] Unsubscribe rate: combined across all sends today

---

## Week 4, Days 2-3 — Jul 21-22

### Daily Monitoring (same structure both days)

**Morning Check (09:00 ET)**
- [ ] Immunity T+24hr email metrics (Jul 21):
  - Same GREEN/YELLOW/RED thresholds as prior emails (>22% GREEN, 15-22% YELLOW, <15% RED)
  - Email 4 open rate compared to Email 3: is fatigue trend continuing or recovering?
    - Recovery signal: Email 4 open rate ≥ Email 3 open rate (flat or improving)
    - Continued decline: Email 4 open rate < Email 3 open rate by 3+ percentage points → escalate to SEEDWARDEN_Q3_WEEK5_6_CONTINGENCY_TRIGGERS.md Section 3

**Photographer Session 3 Quality Gate (Jul 21-22)**
- [ ] If Session 3 received: run quality gate within 48 hours of receipt (Section 3.1 of SEEDWARDEN_Q3_CONTRACTOR_DELIVERABLE_TRACKING.md)
- [ ] If quality gate passes: release Milestone 3 payment same day; update Immunity Etsy listing with final photographer images (replacing any backup images used at launch)
- [ ] If quality gate fails: send revision notes (Template 3B); set 3-day revision window (revised delivery Jul 25)

**Revenue Tracking (Jul 22 checkpoint)**
- [ ] Cumulative revenue through Day 10 of Week 3-4 (Jul 13-22):
  - Target: depends on Week 1-2 actuals; proxy target if W1-2 data unavailable: $300-$600 (conservative estimate for 3 products × 2 weeks)
  - Log: "Week 3-4 Day 10 cumulative revenue: $[amount]"
  - If cumulative revenue <50% of proxy target: activate SEEDWARDEN_Q3_WEEK5_6_CONTINGENCY_TRIGGERS.md Section 1 (revenue underperformance)

---

## Week 4, Days 4-6 — Jul 23-25

### Digestive Bundle Pre-Staging (Aug 3 launch)

- [ ] Digestive bundle Etsy listing created in DRAFT (by Jul 24)
- [ ] Digestive email draft loaded in Kit.com (Email 5, scheduled Aug 3)
- [ ] Digestive social content drafted (queued for Aug 3)
- [ ] Rebecca Lexa Digestive draft received and in quality gate review (due Jul 22; gate review due Jul 24-25)
  - If Digestive draft not received by Jul 22: activate Level 2 escalation (SEEDWARDEN_Q3_WEEK3_4_CONTRACTOR_DELIVERY_ESCALATION.md)

### Social Deep-Dive Assessment (Jul 24)

- [ ] Run Week 3-4 social engagement deep-dive review (SEEDWARDEN_Q3_WEEK3_4_SOCIAL_DEEP_DIVE.md, Section 5 Weekly Summary)
- [ ] Document: per-platform engagement rates, any RED platform signals, content-type performance
- [ ] Apply content mix adjustment rules (if needed per deep-dive findings) to Jul 25-Aug 3 posts

---

## Week 4 Final Checkpoint (Jul 27, by 22:00 UTC)

### Revenue Final Checkpoint

```
Week 4 (Jul 20-27) Summary
Immunity bundle: [#] orders | Revenue: $[amount]
Sleep bundle (cumulative week 3-4): [#] orders | Revenue: $[amount]
Practitioner Tier (cumulative week 3-4): [#] orders | Revenue: $[amount]
Week 4 total revenue: $[amount]
Week 3-4 combined total revenue: $[amount]

vs. Week 1-2 total revenue: $[W1-2 actual]
Week 3-4 vs Week 1-2 variance: [%]

Revenue status:
[ ] GREEN: Week 3-4 revenue ≥ Week 1-2 revenue (flat or growing)
[ ] YELLOW: Week 3-4 revenue 80-99% of Week 1-2 revenue
[ ] RED: Week 3-4 revenue <80% of Week 1-2 revenue
  → If RED: ACTIVATE SEEDWARDEN_Q3_WEEK5_6_CONTINGENCY_TRIGGERS.md Section 1 (revenue underperformance)
  → This trigger is mandatory — no judgment call required
```

### Email Engagement Final Checkpoint

```
Email open rate trend across all 4 sends:
  Email 1 (Jun 29): [%]
  Email 2 (Jul 6): [%]
  Email 3 (Jul 13): [%]
  Email 4 (Jul 20 or Jul 27): [%]

Trend assessment:
  [ ] Stable or recovering (each email ≥ prior OR within 3 percentage points)
  [ ] Gradual decline (<3pp per email, manageable)
  [ ] Steep decline (>3pp per email, 2+ consecutive)

IF steep decline confirmed:
  → Email 5 (Digestive, Aug 3) subject must be value-frame style
  → Email 5 gap must be at least 14 days from Email 4
  → Document adjustment here: [Send date confirmed: ___ / Subject: ___]
```

### Contractor Final Checkpoint

```
All contractor deliverables status (Week 3-4):

Photographer:
  Session 2 (Sleep): [APPROVED / CONTINGENCY / PENDING M3 PAYMENT]
  Session 3 (Immunity): [APPROVED / CONTINGENCY / PENDING M3 PAYMENT]
  Next: No further photo sessions. Final M4 payment status: [PENDING / RELEASED]

Writers:
  Immunity first draft (Rebecca Lexa, due Jul 18): [APPROVED / REVISION / OVERDUE]
  Digestive first draft (Rebecca Lexa, due Jul 22): [RECEIVED / IN GATE REVIEW / OVERDUE]
  Any escalations active: [None / Level ___ for ___]

Specialists:
  Arthur Haines revision (due Jul 20): [APPROVED / PENDING]
  M3 payments due for: [list any pending]

Overall contractor health:
  [ ] All on track — no escalations active
  [ ] [#] active escalations — see SEEDWARDEN_Q3_WEEK3_4_CONTRACTOR_DELIVERY_ESCALATION.md
```

### Social Engagement Final Checkpoint

```
Week 3-4 social engagement summary:
  LinkedIn: avg engagement rate [%] | Status: GREEN/YELLOW/RED
  Instagram: avg engagement rate [%] | Status: GREEN/YELLOW/RED
  YouTube: [# comments from engagement posts] | Status: GREEN/YELLOW/RED

Any RED platforms: [list]
Content type adjustments made: [Educational/Testimonial/Promotional shift — what was changed?]
DM surge detection (LinkedIn): DMs received this week [#] vs baseline [#]
  If >10 DMs/day: profile flag risk — see SEEDWARDEN_Q3_WEEK3_4_SOCIAL_DEEP_DIVE.md Section 2.2
```

---

## Appendix A: Sunrise/Sunset Metrics (Daily Quick Reference)

For each day of Week 3-4, record these "sunrise" (morning check) and "sunset" (end-of-day) metrics:

**Sunrise (09:00 ET check)**
- Prior day email open rate % (T+24hr if applicable)
- Prior day Etsy orders and revenue
- Any RED alerts overnight (email, social, contractor)

**Sunset (22:00 UTC check)**
- Daily revenue total
- Unsubscribe count and rate
- Etsy impressions added today
- Social engagement (likes + comments across all platforms)
- Contractor delivery status (any overdue items)

### Sunrise/Sunset Log Template

```
Date: [YYYY-MM-DD]
SUNRISE (09:00 ET)
  Prior day email open rate: [%] | Status: GREEN/YELLOW/RED
  Orders yesterday: [#] | Revenue yesterday: $[amount]
  Overnight RED alerts: [None / List]

SUNSET (22:00 UTC)
  Daily revenue: $[amount] | Cumulative W3-4: $[amount]
  Unsubscribes: [#] ([%]) | Status: GREEN/YELLOW/RED
  Etsy impressions (all active listings): [#]
  Social engagement: [#] likes + comments
  Contractor: [All on track / Escalation: ___]
```

---

## Appendix B: All Escalation Triggers — Quick Reference

| Trigger | Condition | Document | Section |
|---------|-----------|----------|---------|
| Sleep photos not received | Jul 12 18:00 UTC | SEEDWARDEN_Q3_WEEK3_4_CONTRACTOR_DELIVERY_ESCALATION.md | Section 4.1 |
| Practitioner photos not received | Jul 14 18:00 UTC | SEEDWARDEN_Q3_WEEK3_4_CONTRACTOR_DELIVERY_ESCALATION.md | Section 4.2 |
| Immunity photos (Session 3) not received | Jul 18 18:00 UTC | SEEDWARDEN_Q3_WEEK3_4_CONTRACTOR_DELIVERY_ESCALATION.md | Section 3 |
| Email open rate <15% | Any email | SEEDWARDEN_Q3_DAILY_EMAIL_MONITORING_CHECKLIST.md | PROCEDURE 2 |
| Unsubscribe >0.5% any day | Any day | SEEDWARDEN_Q3_WEEK3_4_CHURN_MONITORING.md | Section 2 |
| Social RED 2+ consecutive days | LinkedIn or Instagram | SEEDWARDEN_Q3_WEEK3_4_SOCIAL_DEEP_DIVE.md | Section 3.3 |
| LinkedIn DMs >10/day | Jul 13-27 | SEEDWARDEN_Q3_WEEK3_4_SOCIAL_DEEP_DIVE.md | Section 2.2 |
| Weekly revenue <60% of baseline | Jul 19 or Jul 27 | SEEDWARDEN_Q3_WEEK5_6_CONTINGENCY_TRIGGERS.md | Section 1 |
| Contractor content 5+ days late | Any contractor | SEEDWARDEN_Q3_WEEK3_4_CONTRACTOR_DELIVERY_ESCALATION.md | Section 3 |

---

## Appendix C: Decision-Free Execution Summary

This checklist is designed for zero-planning execution. The team executes in order; all decisions are pre-wired:

1. **Every day**: check sunrise metrics → run launch tasks if applicable → check sunset metrics → log in Google Sheets
2. **Every email send**: run pre-send checklist from SEEDWARDEN_Q3_DAILY_EMAIL_MONITORING_CHECKLIST.md before sending
3. **Every contingency trigger**: follow the document referenced in Appendix B; do not improvise
4. **Every checkpoint**: fill in the log template; compare against thresholds; apply GREEN/YELLOW/RED rule
5. **End of Week 4**: run final checkpoint; if RED on revenue, activate SEEDWARDEN_Q3_WEEK5_6_CONTINGENCY_TRIGGERS.md

---

*Document status: Production-ready. Version 1.0 created July 13, 2026. Covers Week 3 (Jul 13-19) and Week 4 (Jul 20-27) launch operations. All thresholds are explicit. No judgment calls required. Cross-references: SEEDWARDEN_Q3_WEEK3_4_CONTRACTOR_DELIVERY_ESCALATION.md, SEEDWARDEN_Q3_WEEK3_4_SOCIAL_DEEP_DIVE.md, SEEDWARDEN_Q3_WEEK3_4_CHURN_MONITORING.md, SEEDWARDEN_Q3_WEEK5_6_CONTINGENCY_TRIGGERS.md.*
