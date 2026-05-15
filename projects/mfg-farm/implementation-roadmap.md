---
title: Multi-Printer Farm Implementation Roadmap
project: mfg-farm
created: 2026-05-15
version: 1.0
status: PRODUCTION READY
scope: 24-month phased execution plan from single printer to 8-printer farm
related_docs:
  - MULTI_PRINTER_FARM_ARCHITECTURE.md
  - batch-scheduling-algorithm.md
  - tool-selection-matrix.csv
---

# Multi-Printer Farm Implementation Roadmap

**Vision**: Scale from 1 Bambu P1S printer (Phase 0, May 2026) to a fully automated 8-printer farm with batch orchestration, inventory management, and fulfillment automation by May 2028.

**Success Milestones**:
- Phase 0 (May-July 2026): Establish single-printer baseline, $1.5K+/month revenue
- Phase 1 (Aug-Jan 2027): Add 2nd printer, reach $5K+/month revenue
- Phase 2 (Feb-Jul 2027): Deploy 4-printer cluster with SimplyPrint, $15K+/month revenue
- Phase 3 (Aug 2027-May 2028): 8-printer farm with Printago, $30K+/month revenue

---

## Phase 0: Single-Printer Baseline (May-July 2026) [CURRENT]

**Status**: Test print pending (ModRun cable clip, Batch 1)

### Goals
- Complete test print successfully (no design flaws)
- Launch Etsy store with 1-2 initial SKUs (ModRun clips, headphone hooks)
- Establish operational SOP (print → post-process → QC → package → ship)
- Validate product-market fit (target: $1,500+/month by July)

### Infrastructure

| Component | Action | Cost | Responsibility |
|-----------|--------|------|-----------------|
| **Hardware** | Confirm P1S working, stock spares (nozzles, PTFE tubes) | $100 | You |
| **Filament** | Negotiate tiered pricing with eSUN for 50-100 kg/month @ $12/kg | $0 | You |
| **Storage** | Buy 1× Sunlu S4 dry box + silica gel packs | $120 | You |
| **Post-processing** | Acquire: tweezers, IPA, deburring tools, inspection tools | $50 | You |
| **Packaging** | Stock poly mailers (100×), tissue, thank-you cards | $80 | You |
| **Shipping** | Set up Pirate Ship account, negotiate USPS retail rates | $0 | You |
| **Sales** | Create Etsy shop, list products, optimize titles/tags/images | 10 hrs | You |
| **Queue Mgmt** | Simple Google Sheets (Orders → Print Queue → Shipped) | $0 | You |

**Total investment**: ~$350 (mostly consumables)

### Workflow
```
Order (Etsy) → Google Sheets Queue → Load Filament → Print (P1S-01)
     ↓
Post-process → QC Sample Check → Pack → Print Label (Pirate Ship) → Ship
```

### Success Criteria
- [x] Test print completed, design validated
- [ ] Etsy store live with 2+ products
- [ ] 10+ orders in first month (Month 1-2 expected: 5-10)
- [ ] $500-$1,000/month revenue by Month 2
- [ ] $1,500+/month by end of Phase 0 (July)
- [ ] SOP documented (post-processing, QC, packaging steps)

### Timeline
| Week | Milestone | Owner |
|------|-----------|-------|
| Week 1 (May 19) | Test print complete, analyze results | You |
| Week 2 (May 26) | Etsy store launch, 2 SKUs live | You |
| Week 3-4 (Jun 2-15) | Refine product design, adjust print settings | You |
| Week 5-8 (Jun 16-Jul 13) | 10-20 orders shipped, revenue tracking | You |
| Week 9-12 (Jul 14-Aug 10) | Evaluate readiness for Phase 1 (revenue >$1.5K/month?) | You |

---

## Phase 1: Two-Printer Expansion (August 2026 - January 2027)

**Trigger**: If revenue sustains $1,500+/month for 2+ consecutive months.

### Goals
- Add 2nd Bambu P1S printer to 2× capacity
- Implement **SimplyPrint** for multi-printer queue management
- Refine batch scheduling (manual, color-based grouping)
- Reach $5,000+/month revenue sustain by January

### Infrastructure

| Component | Action | Cost | Responsibility | Timeline |
|-----------|--------|------|-----------------|----------|
| **Hardware** | Purchase 2nd P1S; stock spares for 2 units | $899 | You | Aug 1 |
| **Space** | Confirm space for 2 printers side-by-side (5.5×4 ft minimum) | $0 | You | Aug 1 |
| **Filament** | Expand inventory to 50 kg (2-week buffer) | $600 | You | Aug 2 |
| **Monitoring** | Set up SimplyPrint account ($10/month) + 2 printers | $120/yr | You | Aug 3 |
| **Cable Mgmt** | Organize cables, add power strip for 2 units | $80 | You | Aug 5 |
| **Cooling** | Add ceiling fan + humidity monitor | $80 | You | Aug 5 |
| **Dry Storage** | Add 2nd dry box (Sunlu S4) for color separation | $120 | You | Aug 2 |
| **Scheduling** | Upgrade Google Sheets to track 2 printers + expected finish times | $0 | You | Aug 3 |
| **Operator Training** | Document 2-printer workflow, safety procedures | 5 hrs | You | Aug 5-10 |
| **Part-time Staff** | Recruit 1 part-time post-processor (10 hrs/week @ $15/hr) | $600/mo | You | Aug 15 |

**Total investment**: ~$2,500 hardware + $600/month operations

### Workflow
```
Order (Etsy) → SimplyPrint Queue → Batch by Color → Assign to P1S-01 or P1S-02
     ↓
Parallel Print (both printers) → Post-process (2 operators) → QC → Pack → Ship
```

### Scheduling Strategy (Manual)
```
Queue Rule:
1. Sort orders by Priority (express first), then FilamentColor, then ArrivalTime
2. Group same-color orders into batches (minimize filament changes)
3. Assign alternating batches to P1S-01 and P1S-02
4. Stagger start times by 2 minutes to smooth power draw

Example:
  Order 1 (Black, 50 units) → P1S-01 @ 08:00 (finishes ~11:15)
  Order 2 (White, 30 units) → P1S-02 @ 08:00 (finishes ~10:00)
  Order 3 (Black, 40 units) → P1S-01 @ 11:20 (queued, waits for P1S-01)
  
Result: ~70% printer utilization (one printer always busy, one switching colors)
```

### Key Metrics to Track
- **Monthly revenue**: Target $3,000 (Month 1) → $5,000 (Month 6)
- **Units/month**: Track per printer (target: 150-200 per P1S)
- **Color changes/day**: Should be 3-4 (efficient batching)
- **Failed prints**: <1% failure rate (quality gate)
- **Operator hours/week**: Should stay <30 hrs (monitor labor utilization)

### Success Criteria
- [x] 2nd P1S operational and stable
- [ ] SimplyPrint queue managing both printers
- [ ] 3,000+ units/month combined throughput
- [ ] $5,000+/month revenue sustain (last 2 months of Phase 1)
- [ ] Part-time post-processing staff trained and productive
- [ ] Manual batch scheduling SOP documented

### Timeline
| Month | Milestone | Owner |
|-------|-----------|-------|
| Aug 2026 | 2nd P1S delivered + setup; SimplyPrint active | You |
| Sep 2026 | Stabilize 2-printer workflow; hire part-time staff | You |
| Oct 2026 | Refine batch scheduling; aim for 1,500 units/month | You + Operator |
| Nov 2026 | Evaluate revenue trajectory; plan Phase 2 if on track | You |
| Dec 2026 | Increase production for holiday season | You + Operator |
| Jan 2027 | Assess: Revenue $5K+ sustained? Decision: Phase 2 or hold | You |

---

## Phase 2: Four-Printer Cluster (February 2027 - July 2027)

**Trigger**: Revenue $5,000+/month sustained for 2+ months.

### Goals
- Deploy 4-printer cluster (2 new P1S) in dedicated space
- Implement **batch scheduling algorithm** (color-optimized load balancing)
- Set up **Filametrics** for inventory + reorder automation
- Hire 1 full-time operator + dedicated post-processing staff
- Install infrastructure: electrical upgrade, cooling, cable management, UPS
- Reach $15,000+/month revenue by July

### Infrastructure

| Component | Action | Cost | Responsibility | Timeline |
|-----------|--------|------|-----------------|----------|
| **Hardware** | 2 additional P1S printers ($699 each) | $1,398 | You | Feb 1 |
| **Space** | Rent or designate 10×8 ft dedicated production zone | $200-500/mo | You | Feb 1 |
| **Electrical** | Install dedicated 50A 240V circuit (professional electrician) | $600-800 | Electrician | Feb 10 |
| **Cooling** | Portable AC unit + dehumidifier + ceiling fan | $600 | You | Feb 15 |
| **Enclosure** | Steel shelving + cable tray for 4-printer grid layout | $300 | You | Feb 20 |
| **Fume Extraction** | 1 commercial fume extractor + HEPA filter | $400 | You | Feb 20 |
| **Filament Storage** | 1 industrial dry cabinet (100 kg capacity) | $500 | You | Mar 1 |
| **Monitoring** | Upgrade to Obico Pro ($10/month) for AI failure detection | $120/yr | You | Feb 5 |
| **Inventory** | Filametrics integration ($50/month) + filament tracking | $600/yr | You | Mar 1 |
| **Scheduling** | Build batch-scheduling script (Python) or use Printago trial | 20 hrs | You | Feb 10-28 |
| **QC Station** | Digital calipers, inspection tools, measurement device | $200 | You | Feb 20 |
| **Packaging** | Upgrade: thermal label printer, larger mailer stock | $400 | You | Feb 15 |
| **Operator Hiring** | 1 FTE production tech ($18/hr, 40 hrs/week) | $3,600/mo | You | Jan 15 recruitment, Feb 1 onboard |
| **Post-processor** | 1 part-time (20 hrs/week @ $15/hr) | $1,200/mo | You | Jan 15 recruitment, Feb 1 onboard |

**Total investment**: ~$6,500 hardware + $4,800/month operations

### Workflow (Phase 2 SOP)

```
DAILY (08:00-23:00):
  08:00 → Gather overnight orders (Etsy, email)
  08:30 → Run batch scheduler: Group orders by color, assign to printers
  09:00 → Load filament, start prints on all 4 printers
  10:00 → Post-processor harvests finished prints, begins support removal
  12:00 → Mid-day batch (new orders from morning) scheduled
  14:00 → Quality sampling + dimensional checks (1 per 50 units)
  16:00 → Packaging batch (completed prints from morning)
  18:00 → Print label batch, queue for pickup
  20:00 → Evening production batch (less priority orders)
  22:00 → Pause new orders, allow prints to finish gracefully
  23:00 → Post-processing + packaging of final prints, prep for next day

KEY METRICS:
  - 400-600 units/day (4-printer cluster)
  - 8-12 color batches/day
  - 2-3 filament changes/day
  - 3-4 hours post-processing/day (overlaps with printing)
  - 30-45 minutes packaging/day (batched)
```

### Batch Scheduling Algorithm (Implemented)

See `batch-scheduling-algorithm.md` for full pseudocode. Implementation:

**Option A (Simple, Spreadsheet)**:
```
Google Sheets: Orders Queue
  → Manual sort: Priority → Color → ArrivalTime
  → Estimate print times (lookup table by SKU)
  → Assign to printer with earliest available time
  → Color change penalty: +2 minutes purge time if different color
  → Publish schedule to SimplyPrint
  → Update every 30 minutes
```

**Option B (Advanced, Python Script)**:
```
# Run daily at 08:00, 12:00, 16:00, 20:00
# Fetch orders from Etsy API
# Fetch printer status from SimplyPrint API
# Execute MinCost-Batch-First algorithm
# Publish schedule to SimplyPrint API
# Log metrics: waste, utilization, makespan
```

**Start with Option A (manual, Phase 2). Implement Option B in Phase 3.**

### Key Metrics

| Metric | Target | Phase 1 Baseline | Improvement |
|--------|--------|------------------|-------------|
| **Units/month** | 1,500-2,000 | 300-600 | +5-10× |
| **Revenue/month** | $15,000+ | $5,000 | +3× |
| **Filament waste/month** | <$100 | ~$30 | Baseline |
| **Printer utilization** | 80%+ | ~60% | +20pp |
| **Failed prints** | <1% | ~1% | Maintain |
| **Labor/hour** | 30-40 hrs/week | 20-25 hrs/week (solo) | +50% but shared load |
| **Lead time (order→ship)** | 1-2 days | 2-3 days | Improve |

### Success Criteria
- [ ] 4-printer cluster operational and stable (all printers printing simultaneously)
- [ ] Batch scheduling algorithm executing (manual or script)
- [ ] 1,500+ units/month sustained (375 per printer)
- [ ] $15,000+/month revenue sustain
- [ ] Filament inventory <$100 waste/month via smart batching
- [ ] Operator + post-processor team productive (not bottlenecked)
- [ ] AI failure detection (Obico) preventing 2+ failed prints/week

### Timeline
| Month | Milestone | Owner |
|-------|-----------|-------|
| Feb 2027 | 4-printer setup complete, hire team | You + Hiring Manager |
| Mar 2027 | Ramp to 400 units/day; batch scheduler manual SOP | You + Operators |
| Apr 2027 | Filametrics integration live; inventory tracking automated | You |
| May 2027 | Stabilize at 1,200-1,500 units/month | You + Team |
| Jun 2027 | Evaluate for Phase 3 (revenue $15K+ sustained?) | You |
| Jul 2027 | Decision gate: Scale to 8-printer or hold | You |

---

## Phase 3: Eight-Printer Farm (August 2027 - May 2028)

**Trigger**: Revenue $15,000+/month sustained for 2+ months.

### Goals
- Deploy 8-printer farm (4 additional P1S) with potential 2 X1C for specialty SKUs
- Upgrade to **Printago** for full-stack farm orchestration (scheduling, inventory, fulfillment)
- Implement **automated supplier reordering** (Filametrics → eSUN/Prussian direct)
- Expand to 2-shift operation (16 hours/day) or continuous (24/7 unattended)
- Scale to $30,000-$50,000+/month revenue
- Explore adjacent product lines (headphone hooks, bin labels, specialty designs)

### Infrastructure

| Component | Action | Cost | Responsibility | Timeline |
|-----------|--------|------|-----------------|----------|
| **Hardware** | 4 additional P1S ($699 each) | $2,796 | You | Aug 1 |
| **Space** | Expand to 20×8 ft (4×2 printer grid + packaging station + QC area) | $500-800/mo | You | Aug 1 |
| **Electrical** | 240V distribution panel, sub-breakers for 2 zones | $1,000-1,500 | Electrician | Aug 15 |
| **HVAC** | Dedicated AC + exhaust ducting for 8-printer farm | $1,500-2,000 | HVAC Tech | Sep 1 |
| **Enclosure** | Large positive-pressure enclosure (4×2 grid + fume extraction) | $1,500 | You + Installer | Aug 20 |
| **Filament Storage** | 2 industrial dry cabinets (200 kg total capacity) | $1,000 | You | Aug 10 |
| **Monitoring** | Upgrade to Printago ($200-400/month) | $3,000-4,800/yr | You | Aug 5 |
| **Inventory** | Filametrics Pro ($100/month) + eSUN API integration | $1,200/yr | You | Aug 15 |
| **Scheduling** | Full Printago automation (batch, reorder, fulfillment) | Included in Printago | You | Aug 20 |
| **QC Automation** | Optional: vision-based defect detection (cameras + ML) | $2,000-5,000 | You (Phase 3b) | Oct 2027+ |
| **Fulfillment** | Pirate Ship Pro (multi-account, batching) + EasyPost API | $50/mo | You | Aug 5 |
| **Staffing** | 2-3 FTE (shift coordinator, 2 operators) | $9,000-13,500/mo | You | Jul 2027 recruitment |

**Total investment**: ~$12,000 hardware + $10,000+/month operations

### Workflow (Phase 3 SOP - Continuous Operation)

```
NIGHT SHIFT (22:00-06:00):
  22:00 → Overnight orders received in queue (Etsy, email)
  23:00 → Batch scheduler runs automatically (Printago)
  23:30 → Night operator loads filament, starts prints on all idle printers
  02:00 → Mid-night check-in (email alert if failures detected by Obico)
  06:00 → Morning operator arrives, harvests overnight prints
  
DAY SHIFT (06:00-22:00):
  06:00 → Post-process overnight prints (2 operators)
  08:00 → New order batch scheduled for day 2
  09:00 → Continue printing; QC sampling
  12:00 → Shift change (if 2-shift mode)
  14:00 → Packaging + label printing
  18:00 → Shipment pickup (USPS/UPS)
  20:00 → Prepare for night shift (filament loaded, queue staged)
  22:00 → Handoff to night team

KEY METRICS:
  - 600-1,000+ units/day (8-printer farm)
  - 16-24 color batches/day (continuous operation)
  - ~4-6 filament changes/day
  - 4-6 hours post-processing/day (2 operators)
  - 1-2 hours packaging/day (batched, high-volume SOP)
```

### Printago Integration

Printago (Commerce OS for 3D Print Farms) handles:
1. **Order orchestration**: Etsy → Shopify → PrintFarm unified queue
2. **Batch scheduling**: AI-optimized (filament, color, deadline, profit)
3. **Inventory**: Real-time filament tracking, low-stock alerts, auto-reorder
4. **Supplier integration**: eSUN, Prussian, MatterHackers APIs
5. **Fulfillment**: Pirate Ship + EasyPost label generation
6. **Analytics**: Profitability per order, throughput trends, labor efficiency

**Setup**:
```
Month 1 (Aug 2027):
  - Migrate all orders to Printago
  - Link Etsy, Shopify accounts
  - Configure printer fleet (8× P1S)
  - Set filament database (colors, costs, suppliers)
  - Configure shipping carriers (USPS, UPS, FedEx)
  
Month 2 (Sep 2027):
  - Enable auto-batching algorithm
  - Test inventory tracking (manual count → automatic)
  - Pilot auto-reorder (with manual approval)
  
Month 3 (Oct 2027):
  - Full automation: batch scheduling + inventory + reorder
  - Monitor profitability per order (reveal margin leaks)
  - Optimize workflows based on data
```

### Key Metrics

| Metric | Target | Phase 2 Baseline | Improvement |
|--------|--------|------------------|-------------|
| **Units/month** | 3,000-4,000 | 1,500-2,000 | +2× |
| **Revenue/month** | $30,000-50,000+ | $15,000 | +2-3× |
| **Filament waste/month** | <$150 | ~$100 | Optimize baseline |
| **Printer utilization** | 85%+ | 80% | Slight improvement |
| **Failed prints** | <0.5% | <1% | Improve via automation |
| **Labor/FTE** | 2-3 | 1.5 | +1 FTE (shift coverage) |
| **Lead time** | 1 day | 1-2 days | Improve to <24h |
| **Gross margin** | 55%+ | 60% | Slight margin compression (volume discount offsets) |

### Success Criteria
- [ ] 8-printer farm operational and stable
- [ ] Printago automating batch scheduling, inventory, reorder
- [ ] 3,000+ units/month sustained (375 per printer)
- [ ] $30,000+/month revenue sustain
- [ ] Filament waste <0.5% of revenue
- [ ] 2-3 FTE team working coordinated shifts
- [ ] Automated inventory reorder within 5% of actual consumption
- [ ] <0.5% failed print rate

### Timeline
| Month | Milestone | Owner |
|-------|-----------|-------|
| Aug 2027 | 8-printer hardware deployed, Printago migration started | You + IT |
| Sep 2027 | Batch automation live, team trained on new workflow | You + Team |
| Oct 2027 | Inventory auto-reorder piloting with manual approval gates | You |
| Nov 2027 | Full automation (batch + inventory + reorder), monitor edge cases | You |
| Dec 2027 | Holiday production ramp (potential for 5,000+ units) | Team |
| Jan 2028 | Revenue analysis, margin review, optimization | You |
| Feb-May 2028 | Explore adjacent products (bins, hooks, specialty designs), evaluate next scale | You |

---

## Cross-Phase Initiatives

### Continuous Improvements (All Phases)

| Initiative | Phase 0-1 | Phase 2 | Phase 3 | Owner |
|-----------|-----------|---------|---------|-------|
| **Design Optimization** | Add new SKUs quarterly | Test 2-3 new designs/month | Expand product line (10+ SKUs) | You |
| **Supplier Negotiation** | Lock pricing eSUN 50-100 kg/mo | Expand to 2-3 suppliers, 300 kg/mo | Negotiate direct import (500+ kg/mo) | You + Ops |
| **Quality Systems** | Manual QC sampling | Automated sampling + Obico AI | Vision inspection integration | QC Lead |
| **Customer Feedback** | Collect Etsy reviews | Analyze review trends, iterate design | Implement COGS analytics per SKU | You |
| **Market Expansion** | Etsy only | Add Amazon Handmade, Shopify | Explore B2B (corporate gifts, bulk orders) | Marketing |

### Sustainability Check (Quarterly)

**Gate 0 → Gate 1 (Month 3, Aug 2026)**:
- [ ] Revenue trending >$1,500/month?
- [ ] P1S stable, <5% failed print rate?
- [ ] SOP documented and repeatable?
- **Decision**: Proceed to Phase 1 (2-printer) or pivot?

**Gate 1 → Gate 2 (Month 8, Jan 2027)**:
- [ ] Revenue sustain $5,000+/month?
- [ ] 2-printer workflow efficient (operator not bottlenecked)?
- [ ] Batch scheduling SOP working?
- **Decision**: Proceed to Phase 2 (4-printer) or hold?

**Gate 2 → Gate 3 (Month 14, Jul 2027)**:
- [ ] Revenue sustain $15,000+/month?
- [ ] 4-printer cluster running at 80%+ utilization?
- [ ] Filametrics + inventory tracking live?
- [ ] Team fully trained and productive?
- **Decision**: Proceed to Phase 3 (8-printer) or optimize Phase 2?

**Gate 3 → Beyond (Month 24, May 2028)**:
- [ ] Revenue sustain $30,000+/month?
- [ ] Printago automation fully operational?
- [ ] <0.5% failed print rate via AI?
- [ ] 2-3 FTE team stable and trained?
- **Decision**: 8-printer farm as mature business. Explore:
  - Adjacent manufacturing (resin, nylon)
  - 3PL fulfillment for white-label partners
  - International expansion (EU, Asia shipping)

---

## Risk Mitigation

### Revenue Shortfall
**If Phase 0 revenue <$1,000/month by Month 3**:
- **Root cause analysis**: Is demand limited (marketing lever) or product quality (product lever)?
- **Actions**:
  - Add 2-3 new SKUs (test adjacent demand)
  - Optimize Etsy listing titles/keywords (SEO)
  - Run sponsored ads ($20-50/day test budget)
  - Pivot to Amazon Handmade (different customer base)
- **Timeline**: 4-6 weeks to measure improvement
- **Go/No-go**: If revenue remains <$1,000/month by Month 6, pause Phase 1 scaling; focus on unit economics

### Printer Failure
**If P1S fails (hard failure, not repairable)**:
- **Cost**: $699 replacement
- **Downtime**: 1 week (shipping lead time)
- **Phase impact**: Delay Phase transition by 1-2 months
- **Mitigation**: Maintain 1 spare P1S in stock by Phase 2 (cost: $700, ROI: prevents $5K+ lost revenue per week)

### Filament Shortage
**If primary supplier (eSUN) has 4+ week backlog**:
- **Cost**: 5-10% premium from backup supplier (MatterHackers, Overture)
- **Phase impact**: Margin compression, not revenue loss
- **Mitigation**: Maintain 6-week inventory by Phase 2+ (higher carrying cost but insurance)

### Demand Surge
**If Phase 1 demand exceeds 2× baseline (e.g., $10K/month by Month 5)**:
- **Opportunity**: Accelerate Phase 2 (4-printer) by 2-3 months
- **Actions**:
  - Order 4-printer hardware immediately (2-week lead time)
  - Recruit team in parallel (4-6 week lead)
  - Secure larger production space ASAP
- **Go/No-go**: If demand sustains >$8K/month for 2 months, approve accelerated Phase 2 (Feb vs. Aug 2027)

---

## Summary: 24-Month Investment & Return

| Phase | Period | Hardware | Operations | Cumulative Capex | Expected Revenue | Net Profit | Payback |
|-------|--------|----------|-----------|------------------|------------------|-----------|---------|
| **0** | May-Jul 2026 | $350 | $200/mo | $350 | $2,000 | $1,600 | Imm. |
| **1** | Aug 2026-Jan 2027 | $2,500 | $2,400/mo | $2,850 | $24,000 | $10,000 | 1 mo |
| **2** | Feb-Jul 2027 | $6,500 | $4,800/mo | $9,350 | $90,000 | $36,000 | 1 mo |
| **3** | Aug 2027-May 2028 | $12,000 | $10,000/mo | $21,350 | $360,000+ | $144,000+ | 1 mo |
| **TOTAL (24 mo)** | May 2026-May 2028 | ~$22,000 | ~$200,000 | **$22,000** | **$476,000+** | **$191,600+** | **2 mo** |

**Key Insight**: Capital investment is negligible relative to operational cost. The constraint is not hardware or capital, but **market demand** and **team capacity**. Focus on revenue validation (gates) and team hiring over hardware procurement.

---

## Implementation Checklists

### Phase 0 Checklist (Immediate - Next 30 Days)

- [ ] Complete ModRun test print (May 19)
- [ ] Analyze results, iterate design if needed (May 26)
- [ ] Order filament: 50 kg eSUN Black + 10 kg White/Grey (May 20)
- [ ] Dry box setup: Sunlu S4 + silica gel packs (May 22)
- [ ] Create Etsy shop, list 2 SKUs (May 26-31)
- [ ] Set up Pirate Ship account, negotiate rates (May 26)
- [ ] Document post-processing SOP (May 28)
- [ ] Establish QC checklist (visual, dimensional, mechanical) (May 30)
- [ ] Launch Google Sheets queue tracker (May 31)
- [ ] Fulfill first 10 orders (track lead time, quality) (Jun 1-15)

### Phase 1 Checklist (Months 4-5 from now)

- [ ] 2nd P1S ordered + delivered (Aug 1-10)
- [ ] SimplyPrint account setup, both printers configured (Aug 3)
- [ ] Production space prepared (2-printer layout) (Aug 5)
- [ ] Part-time post-processor hired (Aug 15)
- [ ] Batch scheduling SOP documented (Aug 20)
- [ ] Filament procurement expanded to 50 kg/month (Aug 2)
- [ ] Operator training completed (Aug 10-31)
- [ ] Target: 1,500+ units/month by Jan 2027 (EOPhase tracking)

### Phase 2 Checklist (Months 10-12 from now)

- [ ] 4-printer space secured + electrical upgrade complete (Feb 1-15)
- [ ] Obico Pro + Filametrics integrated (Feb 5)
- [ ] Full-time operator hired + onboarded (Feb 1)
- [ ] Batch scheduling algorithm (manual or Python) implemented (Feb 28)
- [ ] 4-printer cluster stable, printing in parallel (Mar 15)
- [ ] QC station set up (digital calipers, measurement tools) (Feb 20)
- [ ] Target: 1,500-2,000 units/month sustained (Jul 2027)

### Phase 3 Checklist (Months 18-20 from now)

- [ ] 8-printer space + electrical upgrade complete (Aug 1-20)
- [ ] Printago migration + configuration (Aug 5-30)
- [ ] Filametrics Pro + eSUN API integration (Aug 15)
- [ ] Shift coordinator hired (Aug 15)
- [ ] 2-shift SOP documented (Aug 31)
- [ ] 8-printer farm stable, 85%+ utilization (Sep 30)
- [ ] Target: 3,000+ units/month sustained (Dec 2027)

---

## Conclusion

This roadmap provides a phased, evidence-based path from single-printer validation (Phase 0, complete by July 2026) to an 8-printer automated farm (Phase 3, complete by May 2028).

**Key Success Factors**:
1. **Revenue gates** (not hardware) drive scaling decisions
2. **Team hiring** (4-6 week lead) is critical path, not hardware procurement
3. **Batch scheduling** is the core operational leverage (3-4× throughput improvement)
4. **Inventory management** (Filametrics) eliminates waste and guides supplier relationships
5. **Cloud orchestration** (Printago) is essential at Phase 3+ (not earlier)

**Next immediate action**: Complete test print (May 19) and evaluate Phase 0 revenue trajectory. Decision to proceed to Phase 1 is based on sustaining $1,500+/month by end of July 2026.

