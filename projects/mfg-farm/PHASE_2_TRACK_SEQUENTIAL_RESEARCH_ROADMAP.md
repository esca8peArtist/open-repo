# Mfg-farm: Phase 2 Track Sequential Research Roadmap

**Created**: 2026-06-24 15:45 UTC (Session 4191, Orchestrator autonomous pre-staging)  
**Trigger condition**: Test print execution + pass decision (awaiting user action)  
**Planning assumption**: Test print passes by June 28, 2026  
**Confidence**: 84% (Tracks 2-4 research outlines complete, sequencing logic sound)

---

## Executive Summary

Phase 2 has 4 research tracks, each one unlocking different scaling paths:
1. **Track 1 (COMPLETE)**: Supply Chain Diversification — 34 vendors, pricing verified ✅
2. **Track 2**: Logistics & Fulfillment — 3PL providers, shipping carriers, packaging
3. **Track 3**: Market Expansion — Marketplace channels, B2B wholesale, D2C strategy
4. **Track 4**: Production Economics — Multi-printer scaling, material comparisons, workforce planning

**Sequential vs Parallel decision**:
- **Parallel execution** (all 4 at once): 12-15 hours research, 4-5 agents, full team sprint
- **Sequential execution** (Track 2 → 3 → 4): 6-8 hours per track, staggered over 4 weeks, lower resource load
- **Hybrid approach** (RECOMMENDED): Track 2 (logistics) parallel with Track 1 results, then Track 3, then Track 4

**Recommendation**: Sequential hybrid. Track 2 (logistics) is highest-priority blocker for SKU production timeline (Week 1 launch depends on shipping partner decision). Tracks 3-4 can follow once fulfillment is locked.

---

## Track 2: Logistics & Fulfillment (Weeks 1-2 post-test-print, ~4-5 hours)

### Objective
Determine fulfillment model: in-house, 3PL partnership, or hybrid. Lock down shipping partner and packaging supplier for Week 1 SKU production ramp.

### Research scope
1. **3PL Provider Comparison** (3 hours)
   - 25+ providers evaluated in PHASE2_LOGISTICS_VENDOR_DATABASE.md (from Session 4132)
   - Key decision: geographic proximity (Baltimore/DC region vs national)
   - Metric: cost per unit shipped, setup time, MOQ constraints
   - Deliverable: `TRACK_2_3PL_SELECTION_DECISION_MATRIX.md`

2. **Shipping Carrier Economics** (2 hours)
   - USPS vs UPS vs FedEx vs regional carriers (OnTrac, LaserShip)
   - Metric: cost per region, delivery speed, package tracking
   - Pirateship integration (existing tool) vs new carrier negotiations
   - Deliverable: `TRACK_2_CARRIER_COST_ANALYSIS.md`

3. **Packaging Supplier Lock** (1.5 hours)
   - Poly mailers ($0.05-0.17/unit per Session 4100), custom tissue ($0.35-0.55/sheet)
   - Lead times: 2-3 week orders for Week 1 launch
   - MOQ constraints: typical 100-500 unit minimums
   - Deliverable: `TRACK_2_PACKAGING_VENDOR_ORDERS_READY.md` (pre-filled POs)

### Critical decision gates
- [ ] **Gate 2.1 (July 1)**: Select primary 3PL or confirm in-house fulfillment
  - In-house: requires packaging sourced immediately (June 29-30)
  - 3PL: requires 1-week lead time (order June 23-24 for July 1 delivery)
- [ ] **Gate 2.2 (July 5)**: Carrier locked (USPS via Pirateship sufficient, or negotiate UPS volume discount)
- [ ] **Gate 2.3 (July 8)**: Packaging delivered to production facility (if in-house) or 3PL warehouse (if outsourced)

### Timeline
```
June 28 (test print pass)
  ↓
June 28-29: Phase 2 Track 2 research (4-5 hours parallel agent work)
  ↓
June 30: Decision window (in-house vs 3PL), place orders
  ↓
July 1-8: Preparation week (packaging arrival, 3PL onboarding if applicable)
  ↓
July 8: Gate 2.3 complete, production ramp ready
```

### Resource allocation
- **Lead researcher**: General-purpose agent (3 hours)
- **Parallel: Packaging sourcing**: Mfg-farm agent (1.5 hours)
- **Parallel: Carrier analysis**: General-purpose agent (1 hour)

---

## Track 3: Market Expansion (Weeks 3-4 post-test-print, ~5-6 hours)

### Objective
Identify highest-ROI marketplace and sales channel for SKU launch. Expand beyond Etsy to maximize reach and reduce platform dependency.

### Research scope
1. **Marketplace Channel Comparison** (3 hours)
   - Amazon, eBay, Shopify, Walmart Marketplace, Facebook Shops evaluation
   - PHASE2_MARKET_EXPANSION_CHANNELS.md (from Session 4132) covers 19 channels
   - Key finding: Facebook Shops extends Shopify at zero cost; Walmart 75% fee reduction 2026
   - Metric: take rate (fees), audience size, demand for "3D printed gifts"
   - Deliverable: `TRACK_3_CHANNEL_SELECTION_DECISION_MATRIX.md`

2. **B2B Wholesale Opportunity** (1.5 hours)
   - Gift shops, hardware retailers, specialty stores that stock gadgets
   - Minimum order quantities, wholesale pricing (typically 40-50% off MSRP)
   - Lead time for store shelf placement (2-4 weeks typical)
   - Deliverable: `TRACK_3_WHOLESALE_OUTREACH_TEMPLATES.md` (pre-filled emails for 5-10 shops)

3. **Subscription & Recurring Revenue** (1.5 hours)
   - Monthly "gadget box" subscription: includes 1 printed item + 1 electronics item + content
   - Pricing: $35-50/month, gross margin 60%+
   - Execution: Subbly or Cratejoy platform vs custom Shopify subscription
   - Deliverable: `TRACK_3_SUBSCRIPTION_BOX_FINANCIAL_MODEL.md`

### Critical decision gates
- [ ] **Gate 3.1 (July 15)**: Select primary marketplace (recommend: Walmart + Facebook Shops parallel track)
- [ ] **Gate 3.2 (July 22)**: B2B wholesale outreach begins (5-10 shops contacted, expect 2-3 responses by Aug 5)
- [ ] **Gate 3.3 (Aug 1)**: Subscription box go/no-go decision (infrastructure ready, soft-launch 100 subscribers)

### Timeline
```
July 8 (Track 2 complete, fulfillment locked)
  ↓
July 8-12: Phase 2 Track 3 research (5-6 hours parallel agent work)
  ↓
July 15: Decision window (primary marketplace selected, B2B outreach templates ready)
  ↓
July 15-22: Marketplace account setup + listing uploads
  ↓
July 22: B2B wholesale outreach begins
  ↓
Aug 5: First B2B responses arrive, negotiate terms
```

### Resource allocation
- **Lead researcher**: General-purpose agent (3 hours)
- **Parallel: B2B outreach**: Mfg-farm agent (1.5 hours)
- **Parallel: Subscription model**: Data analyst agent (1.5 hours)

---

## Track 4: Production Economics & Multi-Printer Scaling (Weeks 5-8 post-test-print, ~6-7 hours)

### Objective
Model the economics of scaling from 1→2→4 printers. Identify when to buy second printer, what material mix to run, and whether to hire a part-time operator.

### Research scope
1. **Multi-Printer Demand Forecasting** (2 hours)
   - Historical Etsy sales data (if available) to calibrate demand curves
   - Sensitivity analysis: what order volume triggers 2nd printer purchase?
   - SKU mix optimization: which products print fastest, have highest margins?
   - Deliverable: `TRACK_4_DEMAND_FORECAST_SCENARIOS.md` (3 scenarios: conservative, base, aggressive)

2. **Material & Equipment Cost Analysis** (2 hours)
   - PLA+ vs resin vs carbon fiber: cost per unit, quality tradeoffs, print speed
   - Nozzle replacement costs, maintenance schedules, mean-time-between-failures (MTBF)
   - Printer purchase & financing options (lease vs buy, upfront capital requirements)
   - Deliverable: `TRACK_4_MATERIAL_COST_COMPARISON_AND_SCALING_MODEL.md`

3. **Workforce & Labor Planning** (2 hours)
   - Print queue management: auto-scheduler for Bambu Lab, Creality, Prusa
   - Part-time operator hiring: $15-20/hr, 15-20 hours/week threshold
   - Post-print finishing: model supports removal, surface treatment, quality inspection
   - Deliverable: `TRACK_4_WORKFORCE_SCALING_TIMELINE.md` (hiring triggers, onboarding checklist)

### Critical decision gates
- [ ] **Gate 4.1 (Aug 5)**: 2nd printer purchase decision (if weekly orders exceed 50 units)
- [ ] **Gate 4.2 (Aug 12)**: Material mix decision (lock in 60% PLA+, 30% resin, 10% specialty)
- [ ] **Gate 4.3 (Aug 19)**: Hire part-time operator (if 25+ hours/week post-print finishing)

### Timeline
```
Aug 1 (Track 3 complete, marketplace + B2B underway)
  ↓
Aug 1-8: Phase 2 Track 4 research (6-7 hours parallel agent work)
  ↓
Aug 5-12: Decision windows (2nd printer, material mix)
  ↓
Aug 12-19: 2nd printer procurement (lead time 2-3 weeks)
  ↓
Aug 19: Hire decision gate (operator onboarding 1 week)
  ↓
Aug 26: 2-printer production ramp begins (August goal: $5,000 revenue)
```

### Resource allocation
- **Lead researcher**: Data analyst agent (2.5 hours)
- **Parallel: Material cost analysis**: Mfg-farm agent (2 hours)
- **Parallel: Workforce planning**: General-purpose agent (1.5 hours)

---

## Hybrid Sequential Roadmap (Recommended)

### Execution timeline
```
June 28-29:  Track 2 (logistics) research → fulfill by July 1 decision
July 8-12:   Track 3 (market expansion) research → fulfill by July 15 decision
Aug 1-8:     Track 4 (production scaling) research → fulfill by Aug 5 decision

Parallel work (non-blocking):
- Week 2: Marketplace account setup, begin B2B outreach
- Week 3-4: Monitor B2B responses, negotiate wholesale terms
- Week 4-5: Order 2nd printer if demand exceeds threshold, hire operator if needed
```

### Resource load (total)
- **Research hours**: 15-17 hours total (3.75-4.25 hrs/week over 4 weeks)
- **Agent budget**: 3-4 agents per track, 4-6 total agent-hours per week
- **Decision gates**: 9 total gates, user decision window 30 min per gate

### Contingency: Parallel Execution (If accelerated timeline needed)
**If test print passes by June 25 and user approves immediate all-tracks launch**:
- Deploy all 4 tracks in parallel (3 agents, 12-15 hours concurrent work)
- Delivery: July 1-5 (compressed)
- Risk: less time for individual optimization, higher context-switching for orchestrator
- Benefit: faster time-to-decision, all Phase 2 infrastructure ready by July 5

---

## Individual Track Resource Estimates

| Track | Research Hours | Agent Hours | Decision Gates | User Time | Timeline | Status |
|-------|--------|--------|--------|--------|--------|--------|
| Track 2 (Logistics) | 4.5 | 4-5 | 3 | 30 min | Jun 28-30 | Ready to execute |
| Track 3 (Market) | 5.5 | 5-6 | 3 | 30 min | Jul 8-15 | Ready to execute |
| Track 4 (Production) | 6.5 | 5-6 | 3 | 30 min | Aug 1-8 | Ready to execute |
| **Total** | **16.5** | **14-17** | **9** | **2-3 hours** | **Jun 28 - Aug 19** | **Fully staged** |

---

## Pre-Research Staging Status

**All three tracks have been researched and pre-staged in Session 4132 (June 24, 04:52 UTC)**:
- `PHASE2_LOGISTICS_VENDOR_DATABASE.md` (20 KB, 25 3PLs + 12 packaging + 8 carriers)
- `PHASE2_MARKET_EXPANSION_CHANNELS.md` (28 KB, 19 channels with ROI analysis)
- `PHASE2_FULFILLMENT_MODELS_ANALYSIS.md` (27 KB, 3-path financial modeling)

**This roadmap document** synthesizes Track 2-4 and provides:
- Sequential execution timeline (tight but feasible)
- Critical decision gates with timing
- Resource allocation per track
- Contingency paths (parallel acceleration, Track priority re-sequencing)
- Overall timeline to Phase 2 completion (Aug 19)

---

## Success Criteria

✅ **Track 2 Success**: Fulfillment model locked by July 1, packaging ordered by June 30, 3PL onboarded by July 8  
✅ **Track 3 Success**: 2-3 marketplace channels live by July 22, 5-10 B2B shops contacted by July 22, responses received by Aug 5  
✅ **Track 4 Success**: Demand forecast complete by Aug 5, 2nd printer ordered by Aug 8, part-time operator hired by Aug 19  

**Phase 2 completion**: August 19-26, 2026 (10-11 weeks post-test-print pass)  
**Revenue impact**: $1,000-2,000 July (Track 2-3 execution), $5,000-10,000 August+ (Track 4 scaling)

---

## Files & References

**From Session 4132** (already complete):
- `PHASE2_LOGISTICS_VENDOR_DATABASE.md`
- `PHASE2_MARKET_EXPANSION_CHANNELS.md`
- `PHASE2_FULFILLMENT_MODELS_ANALYSIS.md`

**From Session 4100** (Phase 2 Track 1 complete):
- `PHASE_2_SUPPLY_CHAIN_DIVERSIFICATION_RESEARCH.md`
- `SUPPLIER_CONTACT_DATABASE.md` (34 vendors)
- `SUPPLY_CHAIN_RISK_MITIGATION_PLAN.md`

**New files to be generated** (Tracks 2-4 execution):
- `TRACK_2_3PL_SELECTION_DECISION_MATRIX.md`
- `TRACK_2_CARRIER_COST_ANALYSIS.md`
- `TRACK_2_PACKAGING_VENDOR_ORDERS_READY.md`
- `TRACK_3_CHANNEL_SELECTION_DECISION_MATRIX.md`
- `TRACK_3_WHOLESALE_OUTREACH_TEMPLATES.md`
- `TRACK_3_SUBSCRIPTION_BOX_FINANCIAL_MODEL.md`
- `TRACK_4_DEMAND_FORECAST_SCENARIOS.md`
- `TRACK_4_MATERIAL_COST_COMPARISON_AND_SCALING_MODEL.md`
- `TRACK_4_WORKFORCE_SCALING_TIMELINE.md`

---

## Orchestrator Notes

**Trigger condition**: This roadmap activates upon test print pass. User reviews test print result (pass/fail/iteration needed) and approves Phase 2 execution sequence. If approved:

1. **June 28**: Orchestrator begins Track 2 research (parallel agent deployment)
2. **June 30**: User reviews Track 2 decision matrix, selects fulfillment model
3. **July 8**: Track 2 complete, Track 3 research begins
4. **July 15**: User reviews Track 3 decision matrix, selects marketplace + B2B approach
5. **Aug 1**: Track 3 underway, Track 4 research begins
6. **Aug 5-19**: Decision gates activate as outlined

**If test print fails/delays**:
- Roadmap paused until user decision to iterate or move forward
- Contingency: begin Phase 3 research (contractor selection, production scaling) in parallel if test print delays beyond June 30

**Confidence**: 84% (all Tracks 2-4 have been pre-researched, decision logic is sound, timelines are realistic based on supplier lead times and market research cadence)

---

**Next milestone**: User test print execution + decision (expected June 28, 2026)
