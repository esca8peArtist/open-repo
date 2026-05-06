---
title: Post-Test-Print Parallel Workflow Diagram & Critical Path
project: mfg-farm
created: 2026-05-06
scope: 4-week execution timeline (Days 1–28); visual dependencies and parallel execution paths
audience: Anya — reference during execution to identify what can run in parallel
---

# Post-Test-Print Parallel Workflow Diagram

## Visual Timeline: Weeks 1–4

```
WEEK 1: VALIDATION & PHOTOGRAPHY FOUNDATION
│
├─ Stream A: Design Refinement (ModRun + Hooks)
│  ├─ Day 1: ModRun STL refinement (30 min) → Commit to git
│  ├─ Day 1–3: Headphone hooks print + fit-test (3 hr active)
│  └─ Day 4–7: Photography sessions (90 min ModRun + 60 min Hooks, parallel)
│
├─ Stream B: Inventory Preparation (Hooks QA)
│  ├─ Day 1–3: Print 4-unit QA batch (90 min)
│  └─ Day 4–7: Color sample prints if time permits (optional)
│
└─ CHECKPOINT 1 (End Week 1): All designs locked, photos ready, 4 units printed


WEEK 2: ETSY LISTINGS & SUPPLIER NEGOTIATION
│
├─ Stream A: Etsy Listing Creation (Parallel, no dependencies)
│  ├─ Day 8–10: ModRun listing update (30 min) — 3 new photos
│  └─ Day 8–10: Headphone hooks listing draft (60 min) — all copy, tags, pricing
│
├─ Stream B: Supplier Outreach (Parallel, no dependencies)
│  ├─ Day 11–14: Send 2–3 supplier emails (20 min)
│  └─ Day 14–21: Log responses as they arrive
│
└─ CHECKPOINT 2 (End Week 2): ModRun updated, Hooks listing ready to publish, supplier quotes logged


WEEK 3: INVENTORY BUILD & LAUNCH SETUP
│
├─ Stream A: Headphone Hooks Production (Critical path — 8 hr)
│  ├─ Day 15–16: Print 25mm batch (5 plates × 95 min = 475 min = 8 hr)
│  ├─ Day 16–17: Print variants (2 plates × 95 min = 190 min = 3 hr)
│  ├─ Day 16–17: QA all 30 units (90 min)
│  └─ Day 16–17: Install bumper pads on all 30 units (45 min)
│
├─ Stream B: Packaging & Cross-Sell Setup (Parallel, 1 hr)
│  ├─ Day 15: Print 30 thank-you cards + cross-sell inserts (20 min)
│  └─ Day 16–19: Prepare packaging staging area
│
├─ Stream C: Social Content Prep (Parallel, 1 hr)
│  └─ Day 19: Draft Instagram/TikTok/Reddit content + email
│
└─ CHECKPOINT 3 (End Week 3): 30 units printed, packaged, listed, ready to publish


WEEK 4: LAUNCH & FIRST ORDERS
│
├─ Stream A: Publication & Social Launch (Day 22–23, critical)
│  ├─ Day 22 10 AM: Publish headphone hooks listing
│  ├─ Day 22 10:30 AM: Enable Etsy Ads ($1/day)
│  ├─ Day 22 11 AM: Post Instagram
│  ├─ Day 22 5 PM: Post TikTok
│  ├─ Day 23 2 PM: Post Reddit
│  └─ Day 24 9 AM: Send email (if list exists)
│
├─ Stream B: Fulfillment & Optimization (Ongoing, 10 min/order)
│  ├─ Day 24–28: Check Etsy daily for orders
│  ├─ Day 24–28: Ship each order within 3 days
│  ├─ Day 24–28: Respond to Q&A within 4 hours
│  └─ Day 26–28: Monitor metrics; adjust if needed
│
└─ CHECKPOINT 4 (End Week 4): Launched, 2–5 orders shipped, metrics healthy


MONTH 1 TOTAL EFFORT: ~30 hrs (70% design/listing/photography, 30% production/fulfillment)
```

---

## Critical Path Analysis

**Critical path** (longest dependency chain, no slack):

```
Day 1: Test print completes
  ↓
Day 1–3: Hooks fit-test (if fails, reprint costs 1–2 days)
  ↓
Day 4–7: Photography (can't create listings without photos)
  ↓
Day 8–10: Etsy listings created (can't publish without listings ready)
  ↓
Day 15–17: Inventory production (can't fulfill orders without stock)
  ↓
Day 22: Publish listing
  ↓
Day 22+: First orders arrive → fulfillment begins
```

**Total critical path duration: 22 days (3.1 weeks)**

**Slack time (parallel work without blocking critical path):**
- Supplier outreach (Days 11–14) — responses don't affect launch, only future pricing
- Social content prep (Days 15–19) — can be pre-written and scheduled
- Packaging prep (Days 15–19) — doesn't delay publication
- ModRun listing updates (Days 8–10) — optional, doesn't affect hooks launch

---

## Parallel Work Opportunities (Run These Simultaneously)

### Week 1: Design + Photography
```
Day 1–3:                 Day 4–7:
  [Hooks fit-test]         [Photography sessions]
  [ModRun STL refine] ←---- [Use same setup]
        ↓                       ↓
        └─── Both streams complete by Day 7 ───┘
```
**Opportunity:** ModRun refinement and hooks fit-testing can run in parallel (same person, different printers/tasks).

### Week 2: Listings + Supplier Outreach
```
Day 8–10:                    Day 11–14:
  [ModRun update]              [Supplier emails]
  [Hooks listing draft] ←------ [No dependency]
        ↓                           ↓
        └─ All complete by Day 14 ──┘
```
**Opportunity:** Etsy work is independent of supplier outreach. Can parallelize perfectly.

### Week 3: Production + Setup
```
Day 15–16:                  Day 15–19:
  [Print 5 plates]            [Package prep]
  [Print 2 plates]            [Social content]
  [QA 30 units]               [Email draft]
  [Install pads] ←───────────- [No dependency]
        ↓
        └─ All complete by Day 19 ──┘
```
**Opportunity:** Printing is single-threaded (one printer), but packaging prep and content creation can run in parallel.

### Week 4: Launch + Fulfillment
```
Day 22:                      Day 24–28:
  [Publish listing]            [Process orders]
  [Enable Etsy Ads]            [Monitor metrics]
  [Post socials] ────────→     [Restock if needed]
        ↓                           ↓
        └────────── Continuous feedback loop ────┘
```
**Opportunity:** Orders won't start arriving until Day 22 afternoon. First fulfillment likely Day 23–24.

---

## Bottleneck Analysis

### Week 1: Photography
**Single bottleneck:** Lighting/setup time.
**Mitigation:** Use existing ModRun setup (no new purchases). Batch shots: 10 shots in 90 min is achievable.

### Week 3: Print Queue
**Single bottleneck:** Single printer running 11+ hours continuously (Days 15–16).
**Risk level:** Medium (printer reliability). 
**Mitigation:** 
- Don't queue both ModRun + Hooks simultaneously; start Hooks first, add ModRun fills only if printer has idle time
- Have backup spool filament (already have 500g Matte Black)
- If print fails mid-queue, 2-hour reprint slots you back 2 hours (manageable)

### Week 3: Bumper Pad Delivery
**Single bottleneck:** AliExpress lead time (7–14 days).
**Risk level:** Medium (out of control).
**Mitigation:** 
- Order bumper pads NOW (before test print) → arrives by Day 14–21
- If late: ship units without pads; follow up with replacement
- Contingency: have replacement pads in stock by Day 21 maximum

### Week 4: Etsy Algorithm Traction
**Single bottleneck:** Listing impressions depend on Etsy algorithm.
**Risk level:** Low (Etsy Ads mitigate completely).
**Mitigation:** $1–2/day Etsy Ads ensure >50 views in first 7 days.

---

## Resource Allocation by Week

### Week 1 (Design + Photography)
```
Hours breakdown:
  ModRun STL refinement:        0.5 hr (design)
  Hooks fit-test + print:       3.0 hr (design + production)
  Photography sessions:         2.5 hr (photography)
  ──────────────────────────────────
  TOTAL:                        6.0 hrs
  
Key person: Anya (solo — no external dependencies)
```

### Week 2 (Listings + Supplier)
```
Hours breakdown:
  ModRun listing update:        0.5 hr (content)
  Hooks listing draft:          1.0 hr (content)
  Supplier emails + follow-up:  0.5 hr (research)
  ──────────────────────────────────
  TOTAL:                        2.0 hrs
  
Key person: Anya (solo)
Async dependencies: Supplier response time (1–3 days, non-blocking)
```

### Week 3 (Production + Setup)
```
Hours breakdown:
  Headphone hooks printing:     8.0 hr (passive monitoring, active restart)
  QA + bumper pad install:      2.0 hr (active)
  Packaging prep:               0.5 hr (physical)
  Social content + email:       1.0 hr (content)
  ──────────────────────────────────
  TOTAL:                        11.5 hrs
  
Key person: Anya (solo; most time is passive print monitoring)
Constraint: Single printer running 11+ hours continuously
```

### Week 4 (Launch + Fulfillment)
```
Hours breakdown:
  Publication + Etsy Ads:       0.25 hr (one-time)
  Social posting:               0.5 hr (one-time)
  Daily operations (Days 24–28):
    Order fulfillment:          0.5 hr/day × 5 days = 2.5 hrs
    Metric monitoring:          0.1 hr/day × 5 days = 0.5 hrs
  ──────────────────────────────────
  TOTAL:                        3.75 hrs ongoing
  
Key person: Anya (solo; new daily rhythm)
```

**Total Month 1 effort: ~23.25 hours** (much of Week 3 is passive print monitoring)

---

## Decision Tree: If Something Slips

### If test print FAILS (design issue)
```
Impact: Slip 3–7 days (one iteration cycle)
Timeline becomes:
  Day 1–3: Reprint variant, debug
  Day 4–10: Photography (now pushed to Day 8–14)
  Day 15+: Listings ready (now Day 15–18)
  Day 22: Hooks can still launch Week 4 IF iteration is done by Day 14
  
Probability: Low (10%) — designs pre-validated
Recommendation: Skip any non-critical design variations
              (e.g., color samples can wait until Month 2)
```

### If bumper pads DON'T ARRIVE by Day 21
```
Impact: Pads install delayed
Decision: Ship units WITHOUT pads; include note:
  "Bumper pads will be installed and shipped separately by [DATE]"
  
Fulfillment process:
  1. Ship hook + cable post (unpadded)
  2. Have replacement pads pressed + shipped within 2 days
  3. Customer gets pad set + new tracking number
  
Risk level: Low — customer experience slightly degraded, but manageable
Recommendation: Confirm AliExpress tracking every 3 days; if day 15 shows
              "stuck in transit," order emergency pads from Amazon
              ($20, same-day delivery) as backup
```

### If Etsy listing gets <50 VIEWS by Day 27
```
Impact: Ad spend or title not resonating
Decision: Increase Etsy Ads to $2/day OR swap hero photo
  
Action (choose one):
  Option A: Double Etsy Ads budget → aim for 100+ views by Day 30
  Option B: Replace hero photo with under-desk angle → test organic ranking
  
Recommendation: Try Option B first (free); escalate to Option A if CTR <0.5%
Monitoring: Check Etsy stats daily Day 26–30 (5 min/day)
```

### If first order arrives with FIT PROBLEM (jaw too tight/loose)
```
Impact: Single-unit issue; may indicate tolerance problem
Decision: Respond within 4 hours; offer replacement with different tolerance OR refund

Response template (use in headphone-hooks-execution-checklist.md):
  "Hi [Customer], thank you for your order! I'm sorry the fit isn't perfect.
  I can send a replacement with a [looser/tighter] jaw immediately, or 
  provide a full refund if you'd prefer. Just let me know!"
  
Shipping: Next-day replacement; use Priority Mail
Cost: ~$8 (assume one bad fit per 30 units = rare)
Recommendation: Fix tolerance if 2+ similar complaints arrive
              (indicates systematic issue, not one-off)
```

### If supply of FILAMENT runs out during production
```
Impact: Printer stops; can't fulfill orders
Prevention: Pre-order Day 15; have backup spool on shelf
  
Action if it happens:
  1. Stop current print immediately (preserve filament)
  2. Order emergency spool from Amazon Prime (arrive next day)
  3. Prioritize highest-value orders in queue
  
Cost: ~$20 (retail price for 1kg spool vs. $12 bulk)
Recommendation: Keep 1kg backup on shelf at all times once Volume >5/week
```

---

## Weekly Go/No-Go Gates

### End of Week 1
**Required to proceed to Week 2:**
- [ ] ModRun STL refined and committed
- [ ] Hooks fit-test passed (tolerance locked)
- [ ] 8+ photographs taken and edited
- [ ] Zero design changes planned for Weeks 2–4

**If any fail:** 
- Resolve within 24 hours
- If can't resolve: slip Week 2 by 1–2 days, don't proceed

---

### End of Week 2
**Required to proceed to Week 3:**
- [ ] ModRun listing updated with new photos
- [ ] Hooks listing complete in Etsy draft (all fields filled, photos uploaded, tags set)
- [ ] Supplier emails sent (2–3 vendors)

**If any fail:**
- ModRun update: non-blocking; can do Week 3
- Hooks listing incomplete: do NOT proceed to printing; finish draft first

---

### End of Week 3
**Required to proceed to Week 4:**
- [ ] 30 headphone hooks printed, QA'd, padded, bagged
- [ ] Bumper pads installed (or marked "pending" with plan to follow up)
- [ ] Packaging inserts stocked
- [ ] Social content drafted and scheduled
- [ ] Hooks listing still in draft, ready to publish

**If any fail:**
- If units not printed: delay publication to Day 24–25 while finishing production
- If pads pending: proceed with publication; ship without pads

---

### End of Week 4
**Success criteria:**
- [ ] Hooks listing live and generating >50 impressions
- [ ] 2–5 orders shipped within stated processing time
- [ ] Etsy Ads running; optimization actions taken if needed
- [ ] Margin on shipped units ≥70%
- [ ] Zero customer complaints (or all resolved)

---

## Time Allocation Checklist: Week-by-Week

### Week 1
- [ ] Day 1: 30 min (STL refine + commit)
- [ ] Day 1–3: 3 hours (hooks fit-test, print, QA)
- [ ] Day 4–7: 2.5 hours (photography)
- **Week 1 total: 5.5 hrs**

### Week 2
- [ ] Day 8–10: 1.5 hrs (ModRun update + hooks listing)
- [ ] Day 11–14: 0.5 hrs (supplier emails)
- **Week 2 total: 2 hrs**

### Week 3
- [ ] Day 15–16: 8 hrs (printing; mostly passive)
- [ ] Day 16–17: 2 hrs (QA + pad install)
- [ ] Day 15–19: 1.5 hrs (packaging + social prep)
- **Week 3 total: 11.5 hrs**

### Week 4
- [ ] Day 22: 1 hr (publish + ads + social)
- [ ] Day 23: 30 min (email)
- [ ] Day 24–28: 2.5 hrs (fulfillment + monitoring)
- **Week 4 total: 4 hrs**

**Grand total: ~23 hours for Month 1 launch (including 8 hrs passive print monitoring)**

---

## Outsourcing Opportunities (Optional, if time-constrained)

If you're unable to dedicate full time, these tasks can be outsourced:

| Task | Cost | Impact | Outsource? |
|---|---|---|---|
| Photography editing (crop, brightness, export) | $50–100 | Low — repetitive but quick | Maybe |
| Etsy listing copy review (grammar check) | $30–50 | Low — copy is pre-written | No |
| Packaging prep (print inserts, organize supplies) | $20/hr × 2 hrs = $40 | Low — solo work | No |
| Supplier follow-up (chase quotes) | $20/hr × 1 hr = $20 | Low — async emails | No |
| Print monitoring (watch print queue, restart on finish) | $15/hr × 8 hrs = $120 | HIGH — critical for timeline | Maybe if you have a trusted colleague |
| Inventory QA (inspect + pad installation) | $15/hr × 2 hrs = $30 | Medium — detail-oriented | Maybe |

**Recommendation:** Skip outsourcing until Week 5. Month 1 is learning phase; do it yourself to understand the business.

---

## Success Checklist: Month 1 Complete

Print this and check off as you execute:

**Week 1 validation:**
- [ ] Test print completed
- [ ] ModRun STL refined
- [ ] Hooks fit-test passed
- [ ] Photography done
- [ ] All design work locked

**Week 2 listings:**
- [ ] ModRun listing updated
- [ ] Hooks listing in draft (complete)
- [ ] Supplier emails sent

**Week 3 production:**
- [ ] 30 hooks printed
- [ ] Bumper pads installed
- [ ] Packaging stocked
- [ ] Social content ready

**Week 4 launch:**
- [ ] Hooks listing published
- [ ] Etsy Ads running
- [ ] Social posts live
- [ ] First orders shipped
- [ ] Margin >70%

**Month 1 revenue:**
- [ ] Week 1: $125–$200 (any sales)
- [ ] Week 2: $200–$300 (ramping)
- [ ] Week 3: $300–$450 (momentum)
- [ ] Week 4: $450–$575 (stabilizing)
- [ ] **Total: $1,075–$1,525 gross** ← Update `revenue-ramp-metrics.md`

---

**Document status:** REFERENCE — use alongside `post-test-print-revenue-maximization-sequence.md`  
**Best for:** Quick visual check of dependencies, parallel work opportunities, and timeline management
