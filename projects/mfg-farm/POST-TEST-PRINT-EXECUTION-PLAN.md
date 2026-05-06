---
title: Post-Test-Print Execution Plan — Master Index
project: mfg-farm
created: 2026-05-06
status: EXECUTION-READY — triggers on test-print success confirmation
audience: Anya
scope: 28-day revenue maximization sequence; ModRun refinement + Headphone Hooks launch
---

# POST-TEST-PRINT EXECUTION PLAN

## Overview

This master document indexes all materials for the post-test-print 4-week execution sequence. The moment you confirm "test print is good," this plan launches immediately.

**Target outcome:** $6,900–$7,500/month baseline (ModRun + Product 2 live) vs. $2,500 current

**Timeline:** 28 days (4 weeks) from test-print pass to first revenue from Headphone Hooks listing

**Total effort:** ~23 hours (mostly Week 3 passive print monitoring)

---

## When to Read What

### First 5 Minutes After Test Print Passes

1. **Read:** `post-test-print-quick-reference.md` (this page — print it)
2. **Print it.** Tape to desk.
3. **Start Day 1 tasks** (30 min ModRun refinement).

### Before Each Week Starts (Sunday Night)

1. **Read:** Corresponding week section in `post-test-print-revenue-maximization-sequence.md`
2. **Reference:** `post-test-print-parallel-workflow.md` (identify what can run in parallel)
3. **Check:** `post-test-print-quick-reference.md` daily checklist

### When Planning Parallel Work

**Read:** `post-test-print-parallel-workflow.md`
- Shows which work can run simultaneously
- Identifies bottlenecks
- Clarifies dependencies

### When Metrics Slip or Decision Needed

**Reference:** `post-test-print-parallel-workflow.md` > Decision Tree section
- Shows contingency paths if anything delays
- Alternative actions if metrics miss targets

### For Revenue Tracking

**Template:** `revenue-ramp-metrics.md` (existing document)
- Weekly tracking template
- Margin monitoring protocol
- Scaling triggers

---

## Document Map

### Core Execution Documents

| Document | Purpose | When to Use | Read Time |
|---|---|---|---|
| **post-test-print-revenue-maximization-sequence.md** | Full 28-day day-by-day execution guide with templates, supplier contact scripts, MOQ negotiations, social content, fulfillment SOP | Daily reference for detailed tasks | 45 min (skim), 90 min (full) |
| **post-test-print-parallel-workflow.md** | Visual timeline, critical path, parallel work opportunities, bottleneck analysis, decision tree | Planning weeks 1–4; identifying parallel work; contingency planning | 30 min |
| **post-test-print-quick-reference.md** | Printable checklist (one page per week) | Post on desk; reference daily during execution | 5 min per week |

### Supporting Documents (Existing)

| Document | Purpose | When to Use |
|---|---|---|
| **headphone-hooks-execution-checklist.md** | Detailed Photo Brief, MOQ calculations, fit-test validation | Week 1 fit-testing; photography setup |
| **headphone-hooks-etsy-listing.md** | Complete Etsy listing copy, title, tags, pricing, personalization field | Week 2 listing creation (copy-paste from this) |
| **headphone-hooks-cost-model.md** | BOM, labor, equipment, revenue projections, comparison to ModRun | Margin validation; weekly COGS tracking |
| **revenue-ramp-metrics.md** | Weekly tracking template, margin monitoring, scaling triggers | Every Sunday at 6 PM; update with actuals |
| **cost-model-spreadsheet.csv** | ModRun COGS baseline, volume sensitivity analysis | Reference for pricing decisions |
| **cadquery/headphone_hooks.py** | CadQuery design file (parametric headphone hook) | Week 1 fit-test; STL generation |
| **cadquery/modrun_rail.py** | CadQuery design (ModRun rail); for STL refinement | Day 1 refinement; commit tolerance value |
| **cadquery/modrun_clip.py** | CadQuery design (ModRun clip); for STL refinement | Day 1 refinement; commit tolerance value |

---

## Pre-Test-Print Actions (Do Now)

These should be done **before** test print completes (while waiting):

- [ ] Order silicone bumper pads (AliExpress 100-pack) — 7–14 day lead time
- [ ] Confirm filament: 500g+ Matte Black PLA+ on hand
- [ ] Verify Pirate Ship account; test one label print
- [ ] Review ModRun cost model (mental prep for refinement)
- [ ] Bookmark all Etsy listing templates

**Completion:** All done? When test print passes, you're ready to start Day 1 immediately.

---

## Timeline at a Glance

```
TEST PRINT PASSES
       ↓
WEEK 1 (Days 1–7): Design validation + photography
  ├─ Day 1–3: ModRun STL refine + Hooks fit-test (3 hrs)
  └─ Day 4–7: Photography sessions (2.5 hrs)
       ↓
WEEK 2 (Days 8–14): Etsy listings + supplier outreach
  ├─ Day 8–10: Both listings created/updated (1.5 hrs)
  └─ Day 11–14: Supplier emails sent (0.5 hrs)
       ↓
WEEK 3 (Days 15–21): Inventory production + setup
  ├─ Day 15–16: Print 25mm batch (8 hrs, mostly passive)
  ├─ Day 16–17: Print variants + QA (3 hrs)
  └─ Day 15–19: Packaging + social prep (1.5 hrs)
       ↓
WEEK 4 (Days 22–28): Launch + first orders
  ├─ Day 22: Publish listing + ads + social (1 hr)
  ├─ Day 23: Continue social (optional email) (0.5 hr)
  └─ Day 24–28: Fulfillment + monitoring (2.5 hrs)
       ↓
MONTH 1 COMPLETE: ~$1,000–$1,500 gross revenue
```

---

## Checkpoints & Go/No-Go Gates

### End of Week 1: Design & Photography Lock
**Required to proceed:**
- [ ] ModRun STL refined, tolerance locked, committed
- [ ] Hooks fit-test passed
- [ ] 8+ photographs taken & edited
- [ ] Zero design changes planned for Weeks 2–4

**If any fail:** Resolve within 24 hours before proceeding.

---

### End of Week 2: Listings Ready
**Required to proceed:**
- [ ] ModRun listing updated with new photos + cross-sell copy
- [ ] Hooks listing complete in Etsy draft (all fields filled, photos uploaded, tags set)
- [ ] Supplier emails sent (2–3 vendors)

**If Hooks listing incomplete:** Do NOT proceed to Week 3; finish draft first.

---

### End of Week 3: Inventory Complete
**Required to proceed:**
- [ ] 30 headphone hooks printed, QA'd, padded, bagged
- [ ] Bumper pads installed (or marked "pending" with follow-up plan)
- [ ] Packaging inserts stocked
- [ ] Social content drafted & scheduled
- [ ] Hooks listing ready to publish

**If units not printed:** Delay publication to Day 24–25; complete production first.

---

### End of Week 4: Launch Success
**Success metrics:**
- [ ] Hooks listing live, generating >50 impressions
- [ ] 2–5 orders shipped within stated processing time
- [ ] Etsy Ads running; optimization actions taken if needed
- [ ] Margin on shipped units ≥70%
- [ ] Zero customer complaints (or all resolved)

**Revenue target:** Week 4 $450–$575 gross (from hooks + ModRun combined)

---

## Parallel Workstreams

Three parallel workstreams run simultaneously. Understand dependencies:

### Stream A: Design & Listings
- Week 1: ModRun STL refine + Hooks fit-test + Photography
- Week 2: ModRun listing update + Hooks listing creation
- **Dependency:** Photography must complete before Etsy listing creation

### Stream B: Inventory Production
- Week 3: Print 30 units, QA, pad install, bag
- **Dependency:** Bumper pads must arrive by Day 21 (contingency: ship without pads)
- **Single bottleneck:** Single printer; 11+ hours continuous queue Days 15–16

### Stream C: Social & Launch
- Week 3: Draft content, prep packaging
- Week 4: Publish + post socials + email + fulfillment
- **No dependencies:** Can run fully in parallel

---

## Revenue Tracking

**Every Sunday at 6 PM:**

1. **Record actuals** in `post-test-print-quick-reference.md` Week section
2. **Calculate margin** (should be >70%)
3. **Update** `revenue-ramp-metrics.md` with cumulative totals
4. **Check scaling triggers** (second printer, contractor, etc.)

**Week 1 target:** $125–$200 gross (likely from ModRun; Hooks not live yet)  
**Week 2 target:** $200–$300 gross  
**Week 3 target:** $300–$450 gross  
**Week 4 target:** $450–$575 gross  
**Month 1 total:** $1,075–$1,525 gross

---

## Key Decisions & Decision Points

### Day 1: Tolerance Refinement
**Decision:** Based on test-print results, lock tolerance at 0.10 / 0.15 / 0.20 / 0.25 mm
- Tight fit? Use 0.25
- Good fit? Use 0.20 (recommended)
- Loose fit? Use 0.10
**Documented:** Git commit with final tolerance value

---

### Day 14: Supplier Quotes
**Decision:** Which supplier offers best bulk pricing?
- eSUN wholesale <$11/kg? → Log for Month 2 activation
- Anycubic pallet available? → Not yet justified; defer until 25+ kg/month
- Overture alternative? → Backup option if eSUN out of stock
**Action:** Do NOT switch suppliers yet; stay with Amazon for consistency. Test new supplier in Month 2 with small order.

---

### Day 26: Metrics Performance
**Decision:** If CTR <1% or views <50
- Option A: Replace hero photo with under-desk angle
- Option B: Increase Etsy Ads to $2/day
**Recommendation:** Try A first (free); escalate to B if still below target by Day 27

---

### Day 28: Price Test Setup
**Decision:** If >10 reviews and margin healthy, plan $12.99 → $14.99 test
**Action:** Activate price test in Week 5 (Day 36+); run for 2 weeks; monitor conversion
**Success:** Hold ≥80% of current conversion rate

---

### Week 5 (if needed): Product 3 Acceleration
**Trigger:** If Hooks sales plateau below 3 units/week after 2 weeks of live listing
**Decision:** Accelerate Product 3 (Magnetic Bin Labels) design + cost model from backlog
**Action:** Do NOT abandon Hooks; add parallel second product to drive cross-sell

---

## Contingency Paths (If X Happens, Do Y)

### Test Print FAILS (Design Issue)
**Impact:** Slip 3–7 days (one iteration cycle)
**Action:**
1. Identify failure mode (jaw too tight? snap-fit breaks?)
2. Iterate design (tolerance adjustment or geometry refinement)
3. Reprint single-unit test (25 min)
4. If passes: proceed to Week 1 with new design
5. If fails again: escalate (design flaw; needs deeper investigation)

---

### Bumper Pads DELAYED >7 Days
**Impact:** Pads not installed before shipment
**Action:**
1. Ship units WITHOUT pads
2. Include note: "Bumper pads will ship separately by [DATE]"
3. Have replacement pads pressed and shipped within 2 days
4. Customer gets pad set + new tracking number

---

### Etsy Listing Gets <50 Views by Day 27
**Impact:** Algorithm not picking up listing; ads may not be working
**Action (choose one):**
- Option A: Replace hero photo with under-desk angle shot (free, takes 30 min to re-shoot)
- Option B: Increase Etsy Ads to $2/day for next 2 weeks ($14 additional spend)
**Recommendation:** Try A first. If CTR still <0.5% after 24 hours, escalate to B.

---

### First Order Arrives with FIT PROBLEM
**Impact:** Customer jaw grip too tight or too loose
**Action:**
1. Reply within 4 hours
2. Offer replacement with different tolerance ("I'll send a [looser/tighter] version")
3. Ship replacement next-day priority (cost ~$8)
4. If 2+ similar complaints: tolerance is wrong; adjust design

---

### FILAMENT STOCK RUNS OUT During Production
**Impact:** Printer stops; can't fulfill orders
**Prevention:** Keep 1kg backup spool on shelf at all times once >5 units/week
**Emergency action:**
1. Stop current print immediately (preserve filament)
2. Order emergency spool from Amazon Prime (arrives next day, ~$20)
3. While waiting: prioritize highest-value orders in queue
4. Restart printer as soon as spool arrives

---

## Supply Chain Checklist

**Before Day 15 (Week 3 print):**

| Item | Status | Lead Time | Contingency |
|---|---|---|---|
| Bumper pads (AliExpress) | Ordered pre-test | 7–14 days | Have arrived by Day 14? Emergency Amazon pads if late |
| Filament (existing stock) | 500g+ on hand | In stock | Order backup now |
| Poly mailers (existing) | Stock sufficient | In stock | Shop4Mailers 1000-pack if running low |
| Shipping labels (Pirate Ship) | Account verified | On-demand | USPS or FedEx as backup |
| Thank-you cards | Print yourself | 2 hours | Print Day 14 |
| Bubble wrap | On hand | In stock | Any packaging supply store |

---

## Social Media Content Ready-Made

### Instagram Post
```
New: Parametric Headphone Hook — desk clamp + cable organizer in one. 
Fits 12–40mm desks. $12.99. Pairs with ModRun cable system. [LINK] 
#desksetup #3dprinting #homelablife
```

### TikTok Script (15 seconds)
- Scene 1 (5s): Hook on desk, headphones in it, zoom to cable post
- Scene 2 (5s): Loop cable around post, show organized setup
- Scene 3 (5s): "Finally, a headphone hook that manages cables. Etsy link in bio."

### Reddit r/battlestations Post
```
Designed and printed a headphone hook that actually manages cables. 
Clamps 12–40mm desks, no tools, no scratching. Printed in PLA+. 
Etsy link in comments if curious.
```

### Email Subject Lines
1. "New: Parametric Headphone Hook — 10% off for you"
2. "Headphone cable management that actually works"
3. "Your ModRun kit is incomplete without this"

---

## Key Contacts & Resources

### Suppliers (Filament)
- **eSUN direct:** contact@esun3dstore.com
- **Anycubic:** store.anycubic.com contact form
- **Overture (Amazon):** Use Q&A feature on Amazon listing

### Shipping
- **Pirate Ship:** pirateship.com (USPS labels, bulk discounts)
- **USPS rate:** First Class 60g ~$3.50–$4.00

### Social Scheduling
- **Instagram:** Native scheduling (post 10 AM Thursday)
- **TikTok:** Record 2–3 takes; post best same day
- **Reddit:** Post manually; respond to comments actively

### Community
- **r/EtsySellers:** Get feedback on listings
- **r/battlestations:** Post casually (rule: minimal self-promotion)
- **r/3Dprinting:** Reach designers + makers

---

## Files to Commit Post-Sequence

After Week 4 completion, commit these files to git:

```bash
git add projects/mfg-farm/post-test-print-revenue-maximization-sequence.md
git add projects/mfg-farm/post-test-print-parallel-workflow.md
git add projects/mfg-farm/post-test-print-quick-reference.md
git add projects/mfg-farm/revenue-ramp-metrics.md (updated with Week 1–4 actuals)
git add projects/mfg-farm/stl/modrun_rail_*.stl (refined versions)
git add projects/mfg-farm/stl/modrun_clip_*.stl (refined versions)
git add projects/mfg-farm/stl/headphone_hook_*.stl (final versions)
git add projects/mfg-farm/photos/ (all photo assets)

git commit -m "feat(mfg-farm): Post-test-print revenue maximization — Week 1–4 complete; $1,000+ gross revenue, Hooks live, ModRun optimized"
```

---

## Success Definition: Month 1 Complete

**Revenue:**
- Week 1: $125–$200 ✓
- Week 2: $200–$300 ✓
- Week 3: $300–$450 ✓
- Week 4: $450–$575 ✓
- **Total: $1,075–$1,525 gross** ✓

**Operations:**
- All orders shipped within 1–3 business days ✓
- Zero customer complaints on fit/quality ✓
- Etsy ratings ≥4.5 on first 5 reviews ✓
- ModRun + Hooks cross-sell in 100% of packages ✓

**Scaling readiness:**
- Hooks at 2–5 units/week sustained ✓
- ModRun at 10–15 units/week ✓
- Supplier pricing negotiated OR locked in for Month 2 ✓
- Product 3 (bin labels) design started (optional) ✓

---

## Next Steps: Month 2 (Prepare During Week 4)

While Week 4 executes, start planning Month 2:

1. **Supplier decision:** Activate new bulk pricing if quotes justified
2. **Product 3 acceleration:** Start CadQuery design for Magnetic Bin Labels
3. **Price test:** Set up $14.99 variant for Hooks (activate Day 36 with 10+ reviews)
4. **FBA prep:** Research Amazon Seller Central onboarding (activate around Day 60 if 50+ units sold)
5. **Email list:** Build email capture (link in Etsy listing description; 10% new-customer discount)

---

## Questions?

**Document unclear?** Reference the full `post-test-print-revenue-maximization-sequence.md` for details.

**Need a quick reminder?** Print `post-test-print-quick-reference.md` and keep on desk.

**Need visual timeline?** Reference `post-test-print-parallel-workflow.md` for dependencies and critical path.

---

## Document Status

**Status:** EXECUTION-READY  
**Last updated:** 2026-05-06  
**Trigger:** Test print success confirmation  
**Author:** Claude Code Agent  
**Confidence:** HIGH — all materials complete; dependencies mapped; contingencies documented  

---

**When test print passes, this plan launches immediately.**

*Print post-test-print-quick-reference.md. Tape to desk. Start Day 1. Let's go.*

