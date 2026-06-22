---
title: "Phase 2 Scaling Research Outline — Supply Chain, Logistics, Market Expansion, Fulfillment"
project: mfg-farm
created: 2026-06-22
status: framework-ready
confidence: 90%
scope: >
  Post-test-print research agenda for Phase 2 launch (awaiting test print completion).
  Four research tracks: supply chain diversification, logistics optimization, market 
  expansion strategy, and fulfillment workflow. Estimated 35-45 hours of research 
  work across all tracks; modular execution path allows parallel research initiation 
  once test print unblocks.
depends_on:
  - COMMODITY_PRODUCT_LIBRARY_Q3_2026.md
  - PHASE_2_SCALING_DECISION_MATRIX.md
  - PRODUCTION_FARM_SCALING_STRATEGY.md
  - post-test-print-quick-reference.md
related:
  - ADJACENT_MANUFACTURING_ROI_UPDATE.md
  - fulfillment-workflow.md
  - batch-3-4-launch-sequencing.md
---

# Phase 2 Scaling Research Outline

**Purpose**: Define research work required to unblock Phase 2 execution (after test print passes). This outline maps four parallel research tracks with specific deliverables, effort estimates, and decision gates tied to traction signals from Phase 1 (June 30 data).

**Current status**: Q3 2026 commodity library complete (23 SKUs). Phase 1 Etsy launch scheduled June 3-15. Phase 2 scaling decision matrix complete (Conservative/Standard/Aggressive scenarios). Research agenda outlined below for execution timing.

---

## Research Tracks Overview

| Track | Focus Area | Lead Questions | Est. Hours | Trigger | Output |
|---|---|---|---|---|---|
| **Track A** | Supply Chain Diversification | Where else can we source PLA+, nozzles, beds reliably? | 8–10 | Conservative→Standard escalation | Supplier comparison matrix, negotiation templates, MOQ/pricing contracts |
| **Track B** | Logistics Optimization | How much does weight/packaging cost per unit? Regional shipping variations? | 7–9 | All scenarios (baseline cost model) | Shipping cost analysis by region/weight; packaging optimization study |
| **Track C** | Market Expansion | What products can we scale to? Second printer, material variants, adjacent channels? | 12–15 | Standard→Aggressive decision | Product-market fit validation, Amazon FBA category research, TikTok Shop assessment |
| **Track D** | Fulfillment Workflow | How do we manage queue, QC, packaging at 100+ units/week? | 8–12 | All scenarios (Phase 2 prerequisite) | Standard operating procedures, quality control checklist, inventory management system design |

---

## TRACK A: Supply Chain Diversification

**Purpose**: De-risk filament, nozzle, and print bed sourcing by validating alternative suppliers before Phase 2 capital deployment.

### A.1: Filament Supply Chain Mapping

**Current state**: Polar Filament ($18.99/kg PLA), MatterHackers ($20.99/kg PETG). Cost model assumes $0.022/g PLA+, $0.030/g PETG.

**Research questions**:
1. **PLA+ Alternatives**: Are there 2-3 additional US-based suppliers with <$0.020/g pricing? (Target: 30% cost reduction if scaled to bulk MOQ)
2. **Bulk MOQ trade-offs**: At 100kg/month (2-printer utilization), what MOQ discounts unlock? (Estimate: $16.99/kg at 50kg MOQ, $14.99/kg at 100kg+)
3. **International suppliers**: Could we import from MatterHackers or Prusament (EU) at favorable pricing? (Logistics cost may offset filament savings)
4. **Recycled/reclaimed filament**: Is there a market for recycled PLA offcuts? (Potential cost recovery on scrap)

**Research method**:
- Competitive analysis: Search industrial filament suppliers (Stratasys, 3DFils, Prusament, MatterHackers, Overture, Prusament, Filamentive)
- Direct outreach: Request bulk pricing from 5+ suppliers (50kg, 100kg, 200kg MOQs)
- Cost comparison spreadsheet: Build dynamic pricing model (unit cost vs. MOQ, including shipping)
- Supplier scorecards: Evaluate reliability (lead time, defect rate, return policy, customer reviews)

**Deliverable**: `FILAMENT_SOURCING_COMPARISON_MATRIX.md`
- Table: 8-10 supplier options with pricing at 3 MOQ tiers
- MOQ negotiation templates (email outreach, follow-up scripts)
- Recommendation: primary + 2 backup suppliers for each material type
- Cost impact: estimated $X savings at 100kg/month if scaled negotiation succeeds

**Effort**: 8–10 hours (research, outreach, analysis, documentation)

**Decision gate**: 
- **Conservative**: Use current suppliers (risk acceptable for low volume)
- **Standard**: Negotiate bulk pricing with 1–2 alternatives (aim for 10–15% cost reduction)
- **Aggressive**: Commit to bulk MOQ contract with primary + verified backup (lock in pricing June–September)

---

### A.2: Nozzle & Print Bed Supply Chain

**Current state**: Bambu P1S standard nozzle pack (5 nozzles, ~$25). Flex plate replacements. Assume replacement cost $40–50/printer/quarter.

**Research questions**:
1. **Third-party nozzles**: Do aftermarket nozzles (Dyze, E3D, MK8) work reliably with P1S? (Risk of jamming, reduced reliability)
2. **Flex plate durability**: What's the real lifespan at 100+ unit/week production? (Data: expect 500–1,000 prints per plate before wear)
3. **Bulk consumables sourcing**: Can we pre-buy 20 nozzles + 10 flex plates at 20–30% discount?
4. **Preventive maintenance schedule**: When should nozzles/plates be replaced to minimize downtime?

**Research method**:
- Supplier search: 3D Sonicware, Bambu Lab official, Dyze Design, E3D Online, MatterHackers
- Community forums: Prusa Forum, r/BambuLab (real user experiences with wear rates, downtime)
- Direct outreach: Request bulk consumables pricing from suppliers
- Burn-in test: Optional (if time permits) — run 100 test prints, track plate wear progression

**Deliverable**: `CONSUMABLES_DURABILITY_AND_SUPPLY_CHAIN.md`
- Table: Nozzle/plate lifespan estimates at different utilization rates
- Bulk pricing for consumables (20 nozzle pack, 10 flex plate pack)
- Preventive maintenance schedule (recommended replacement intervals)
- Recommended pre-buy quantities for Standard/Aggressive scenarios (e.g., 40 nozzles + 20 plates for 3-printer operation)

**Effort**: 7–9 hours (research, community survey, supplier outreach, documentation)

**Decision gate**:
- **Conservative**: Buy as-needed from Bambu Lab official store
- **Standard**: Pre-buy 1 consumables kit per printer (20 nozzles, 10 plates) at startup
- **Aggressive**: Establish quarterly bulk order schedule (lock in pricing, ensure zero downtime)

---

## TRACK B: Logistics Optimization

**Purpose**: Quantify shipping costs, packaging economics, and regional fulfillment strategies to optimize margin at scale.

### B.1: Shipping Cost Analysis by Product & Region

**Current assumptions**: $0.35 packaging + Etsy's calculated shipping (USPS First Class, ~$4–6 per order depending on weight/distance).

**Research questions**:
1. **Regional variation**: How much does shipping cost vary from West Coast vs. East Coast? (USPS, UPS, FedEx pricing tiers)
2. **Weight optimization**: Can lighter packaging reduce shipping cost? (Current: poly mailer + tissue + label + insert + tape ≈ 10–15g + product)
3. **Bundle shipping economics**: Do 2-packs or 3-packs reduce per-unit shipping cost? (Volume discount potential)
4. **Regional fulfillment hubs**: Could we partner with a 3PL for regional fulfillment to reduce shipping costs? (ROI breakeven at what scale?)

**Research method**:
- USPS/UPS/FedEx rate lookup: Build shipping cost calculator for sample SKUs (lightweight cable clip, heavier gridfinity bin, bundle packs)
- Etsy shipping label data: Review all Phase 1 orders (June 3–30) to extract actual carrier, weight, cost paid
- 3PL research: Identify regional fulfillment providers (ShipBob, Flexport, FedEx SameDay) — costs and MOQs
- Packaging optimization: Test 2–3 lighter packaging alternatives (reduced tissue, downsized poly mailer) and compare cost + perceived quality

**Deliverable**: `SHIPPING_COST_OPTIMIZATION_AND_3PL_ANALYSIS.md`
- Regional shipping cost matrix (West/Midwest/South/Northeast) for 5 representative SKUs
- Shipping cost as % of sale price (identify highest-margin, lowest-cost fulfillment combos)
- Bundle shipping analysis: compare 1×clip ($12.99) vs 3×clip 3-pack ($27.99) shipping cost per unit
- 3PL evaluation table: 3–5 providers with rates, minimums, integration effort, breakeven volume
- Recommendation: Etsy self-fulfillment for Phase 1–2 (volumes <500 units/month); 3PL evaluation gate at 1,000+ units/month

**Effort**: 7–9 hours (rate research, data analysis, 3PL outreach, ROI modeling)

**Decision gate**:
- **Conservative**: Self-fulfill via USPS; no optimization planned
- **Standard**: Optimize packaging to reduce weight 10%; explore 3PL quotes (decision gate: 500+ units/month)
- **Aggressive**: Implement lightweight packaging immediately; stage 3PL integration plan (decision gate: 1,000+ units/month or 2-printer utilization >80%)

---

### B.2: Amazon FBA Logistics & Pricing Implications

**Current state**: FBA is optional in Standard/Aggressive scenarios. FBA fees typically 30–40% of sale price (storage, fulfillment, referral) vs. 9.5% Etsy fees.

**Research questions**:
1. **FBA category fees**: What are actual FBA fees for cable management, desk organization, workshop products? (Vary widely: 25–40% depending on category, weight, dimensions)
2. **Dimensional weight penalties**: Do our SKUs exceed FBA's dimensional weight thresholds? (e.g., gridfinity bins with air cushioning may be flagged)
3. **FBA inventory costs**: At what volume does storage cost become significant? (Estimate: $0.87/cubic foot/month; small products may store 50+ units per cubic foot)
4. **FBA fulfillment tier**: Are our products eligible for FBA or only Fulfillment by Merchant (FBM)? (Restrictions on bulk packs, personalized items)

**Research method**:
- Amazon Seller Central fee calculator: Input sample SKUs (cable clip, gridfinity bin, laser-engraved clip), check calculated FBA fees
- Competitor analysis: 5–10 similar cable management / desk org sellers on Amazon; extract their pricing vs. Etsy (note: may differ due to FBA cost structure)
- FBA dimensions check: Verify each SKU against FBA size/weight tiers (small standard, large standard, oversize)
- Profitability comparison: Build FBA vs. Etsy margin analysis for Standard scenario (2-printer, 60 units/week average)

**Deliverable**: `AMAZON_FBA_COST_ANALYSIS_AND_LAUNCH_READINESS.md`
- FBA fee breakdown for 5 representative SKUs (referral, fulfillment, storage, closing fees)
- Dimensional weight analysis: which SKUs exceed thresholds? Opportunities to consolidate/repackage?
- Profitability comparison table: Etsy margin vs. FBA margin for 50 units/week, 100 units/week, 150 units/week scenarios
- FBA launch readiness checklist: what prep work is needed? (UPC codes, packaging requirements, ASINs, etc.)
- Recommendation: Recommended SKUs for FBA (lowest fee burden), optimal bundle strategy (reduce dimensional weight), timing (when to launch)

**Effort**: 6–8 hours (Amazon fee research, competitor analysis, margin modeling, documentation)

**Decision gate**:
- **Conservative**: Skip FBA; Etsy-only
- **Standard**: Research FBA for 2–3 highest-margin SKUs; defer launch decision to September (based on Phase 1 traction)
- **Aggressive**: Begin FBA prep in August (UPC codes, packaging requirements); launch in September with initial inventory (50 units per SKU)

---

## TRACK C: Market Expansion Strategy

**Purpose**: Identify next product opportunities, material variants, and distribution channels to drive growth beyond Phase 1 baseline.

### C.1: Adjacent Product Categories & Scaling Potential

**Current library**: 23 SKUs across 5 categories (cable management, desk org, gridfinity, home, seasonal). Best candidates: ModRun clips, headphone hooks, gridfinity bins.

**Research questions**:
1. **What's the next high-volume category?** Search Etsy for "desk accessories," "office organization," "workshop storage" — identify 3–5 underserved niches with 50+ but <500 reviews
2. **Bundles as revenue multiplier**: Can we create bundles (e.g., "Desk Starter Set," "Workshop Kit") that increase AOV without significant production cost?
3. **Material variants**: Would customers pay +$2–3 for colors (beyond standard black/white)? How much does material cost increase? (e.g., specialty PLA: Prusament Galaxy Black +$0.05/g vs. standard PLA)
4. **Second product line opportunity**: After cable management/desk org prove out, what's the next category? (E.g., wall-mounted planters, kitchen organizers, bathroom caddies — search trends)

**Research method**:
- Etsy search trends: Use Etsy search bar autocomplete + eRank (search volume, trend slope) for 10–15 potential categories
- Competitive landscape: 3–5 top sellers per category — extract pricing, review count, average rating, what makes them successful
- Customer research: Read 10–20 recent reviews across top competitors — what do customers want that's missing?
- Design complexity audit: For each identified category, estimate design effort (1–3h existing designs, 4–6h new designs)
- Profit modeling: Estimate COGS, market price, margin for 5 most-promising categories

**Deliverable**: `PRODUCT_EXPANSION_ROADMAP_AND_MARKET_OPPORTUNITIES.md`
- Table: 10–15 potential product categories with Etsy search volume, competitor count, average price, estimated margin
- Top 5 recommended categories ranked by (margin × demand × design effort)
- Bundle strategy recommendations (3–5 bundle configurations with projected AOV uplift)
- Color/material variant analysis: cost impact, pricing strategy, demand potential
- Phased expansion roadmap: Q3 launch (current 23 SKUs), Q4 add (3–5 new categories), Q1 2027 (color variants, bundles)

**Effort**: 10–12 hours (market research, competitive analysis, design feasibility assessment, roadmap documentation)

**Decision gate**:
- **Conservative**: Stay focused on current 23 SKUs through Q4; re-evaluate bundling in Q1 2027
- **Standard**: Add 2–3 new high-margin categories by October (e.g., wall-mounted organizers, custom name plates)
- **Aggressive**: Parallel development of 2 new categories + color variant rollout by Q1 2027; aim for 40+ unique SKUs by year-end

---

### C.2: TikTok Shop & Secondary Distribution Channels

**Current state**: Etsy is primary channel. Amazon FBA is optional add-on. TikTok Shop, Instagram Shop, Shopify are unexplored.

**Research questions**:
1. **TikTok Shop feasibility**: Is TikTok Shop available in US (as of June 2026)? What are the fee structure, content requirements, growth potential?
2. **TikTok audience fit**: Are cable management clips, desk organizers, gridfinity bins viable on TikTok? (Audience typically younger, trend-driven; desk org content performs well — see #desksetup)
3. **Organic content opportunity**: Could we generate UGC (user-generated content) or creator partnerships? (E.g., "organize your desk" creators selling our clips)
4. **Shopify vs. TikTok Shop**: Build independent Shopify store + TikTok Shop sync, or TikTok Shop only?

**Research method**:
- TikTok Shop research: Official docs, fee structure, seller eligibility (US only? age restrictions?), growth stats
- Competitor audit: Search TikTok Shop sellers selling desk accessories / 3D-printed products (if any); extract engagement metrics
- Content viability: Search #desksetup #organize #gridfinity on TikTok; estimate audience size, top trending videos
- Creator partnership exploration: Identify 5–10 "organization influencers" on TikTok with 100K–1M followers; assess partnership feasibility

**Deliverable**: `SECONDARY_CHANNELS_ROADMAP_TIKTOK_INSTAGRAM_SHOPIFY.md`
- TikTok Shop status in US (as of June 2026) + eligibility requirements
- Fee/commission comparison table: Etsy vs. Amazon FBA vs. TikTok Shop vs. Shopify (independent store)
- Content strategy outline for TikTok (organic setup, fulfillment, creator partnerships)
- Recommendation: Prioritized channel expansion timeline (e.g., FBA Aug 2026, TikTok Shop Sept 2026, Shopify Dec 2026)

**Effort**: 5–7 hours (channel research, competitor analysis, feasibility assessment)

**Decision gate**:
- **Conservative**: Etsy-only; no secondary channels
- **Standard**: Evaluate TikTok Shop + Amazon FBA for Q4; make expansion decision by October 1
- **Aggressive**: Begin TikTok Shop setup in September; FBA launch simultaneously; stage Shopify for Q1 2027

---

## TRACK D: Fulfillment Workflow & Operations

**Purpose**: Design standard operating procedures, quality control, and inventory management systems required to handle 100+ units/week production at scale.

### D.1: Queue Management & Production Scheduling

**Current state**: Solo operation, no formal queue. Phase 2 introduces 2–3 printers, multiple SKUs, variable print times.

**Research questions**:
1. **Print queue optimization**: How should we prioritize orders? (FIFO vs. batch-by-SKU vs. batch-by-profit-margin)
2. **Print time distribution**: How long does each SKU take? Can we batch low-time SKUs (cable clips: 30–45 min) with high-time SKUs (gridfinity bins: 2–3 hrs) for efficient plate utilization?
3. **Failed print handling**: What's the expected failure rate? How do we handle reprints and customer communication?
4. **Multi-printer scheduling**: At 2–3 printers, can we run different SKUs in parallel to minimize idle time? (Plate 1: cable clips, Plate 2: gridfinity bins, Plate 3: seasonal items)

**Research method**:
- Print time audit: Test print each of the 23 SKUs; record time from slice to completion (including supports/cleanup)
- Queue simulation: Build spreadsheet or simple scheduling algorithm to simulate queue under different prioritization schemes
- Failure rate estimation: Run 20 test prints; document any failures (nozzle jams, bed adhesion, cooling issues), calculate failure rate
- Batch optimization study: Can we fit 10 cable clips + 2 gridfinity bins on one P1S plate? (plate area ~250×220mm; test layout)

**Deliverable**: `PRODUCTION_QUEUE_MANAGEMENT_AND_SCHEDULING_SYSTEM.md`
- Print time database: all 23 SKUs with estimated print time, weight, material type, plate utilization efficiency
- Prioritization logic: recommended queue management strategy (recommend: profit-margin-weighted batch scheduling to maximize hourly revenue)
- Batch layout templates: CAD/image files showing optimal plate arrangements for common product mixes
- Failure rate estimates: expected defect rate, reprinting policy, customer communication scripts
- Multi-printer scheduling strategy: how to allocate SKUs across 2–3 printers to minimize idle time

**Effort**: 8–10 hours (printing test battery, data analysis, simulation, templates, documentation)

**Decision gate**:
- **Conservative**: Manual queue management; no formal scheduling system
- **Standard**: Implement batch-by-SKU scheduling with print time database (spreadsheet-based)
- **Aggressive**: Build priority-weighted scheduling algorithm (spreadsheet or simple Python script); track queue health metrics (efficiency %, idle time %)

---

### D.2: Quality Control & Inspection Workflow

**Current state**: Visual inspection only; no formal QC checklist.

**Research questions**:
1. **Defect types & detection**: What are common defect modes for each product? (E.g., cable clips: snap-arm stress fracture, dimensional variance; gridfinity bins: layer adhesion, support scars)
2. **QC workflow efficiency**: Can we inspect 100 units/week in <2 hours? (Estimate: 1–2 min per unit for visual inspection)
3. **Dimensional tolerance**: Do products need to meet exact specifications, or is visual consistency enough? (E.g., gridfinity bins must have ±0.5mm height to stack reliably)
4. **Customer return handling**: What's the expected return rate? How do we process refunds/replacements?

**Research method**:
- Defect analysis: Print 10 test units of each SKU; inspect for common failure modes (stress cracks, dimensional variance, surface quality)
- QC time study: Perform mock QC inspection on 50 units; time each inspection; calculate average time per unit
- Tolerance testing: For gridfinity bins and modular products, measure actual printed dimensions; verify fit/stacking
- Customer research: Review similar sellers' reviews to identify common complaints (loose fits, warping, paint/color inconsistency)

**Deliverable**: `QUALITY_CONTROL_PROCEDURES_AND_CUSTOMER_RETURNS_POLICY.md`
- Defect database: common defect modes per SKU with photos/descriptions and pass/fail criteria
- QC inspection checklist template: printable form with checkboxes for each product (visual inspection, dimensional check, functional test)
- Expected defect rate + return rate estimates (baseline: <2% defect rate, <1% returns)
- Customer communication scripts: how to handle returns, replacements, refunds
- Return policy recommendation: (e.g., full refund for defects, flat $3 reshipping fee)

**Effort**: 6–8 hours (defect testing, QC design, policy documentation)

**Decision gate**:
- **Conservative**: Visual inspection only; accept 2–3% defect rate (assume customer absorption)
- **Standard**: Formal QC checklist; target <1% defect rate; accept returns for defects
- **Aggressive**: Dimensional QC for modular products (gridfinity); <0.5% defect rate target; generous return policy to build 4.9+ star rating

---

### D.3: Inventory Management & Supply Planning

**Current state**: Just-in-time filament purchasing; no inventory of finished goods.

**Research questions**:
1. **Finished goods buffer**: Should we keep finished goods inventory? (Safety stock for fast shipping vs. working capital tie-up)
2. **Supply forecasting**: Can we predict demand per SKU from Phase 1 data? (E.g., if cable clips get 10 orders/week in June, expect 12–15 in July)
3. **Material lead time**: How long to reorder filament? (Typically 3–5 days for US suppliers; what's the safety stock needed?)
4. **Inventory system**: How do we track units printed, sold, returned? (Spreadsheet, Etsy inventory sync, third-party tool?)

**Research method**:
- Inventory modeling: Build simple spreadsheet model with three scenarios (Conservative/Standard/Aggressive) showing material purchases, finished goods stock, turnover rates
- Etsy inventory sync research: Does Etsy have inventory management API? (Yes, partially; can use Zapier or manual sync)
- Demand forecasting: Use Phase 1 data (June 3–30) to project demand curve for July–December (assume growth rate of 10–20% per month)
- Lead time documentation: Record actual lead time from Polar Filament + MatterHackers for future planning

**Deliverable**: `INVENTORY_MANAGEMENT_AND_SUPPLY_PLANNING_SYSTEM.md`
- Inventory model spreadsheet: tracks material purchases, print schedule, finished goods, sales, turnover
- Demand forecast: projected monthly units per SKU for Phase 2 (July–December 2026)
- Material reorder schedule: recommended reorder points and quantities (e.g., when filament drops below 5kg, order 20kg)
- Etsy integration guide: how to sync Etsy orders with inventory tracking (manual or automated)
- Recommendation: target 2–3 week finished goods buffer (e.g., 50 cable clips, 20 gridfinity bins) for Phase 2 Standard scenario

**Effort**: 6–7 hours (modeling, forecasting, system design documentation)

**Decision gate**:
- **Conservative**: Just-in-time material purchasing; no finished goods inventory
- **Standard**: 1–2 week safety stock of key SKUs (cable clips, headphone hooks); manual Etsy inventory sync
- **Aggressive**: 2–3 week finished goods buffer; automated Etsy inventory sync via Zapier or custom script

---

## TRACK D.4 (Optional): Logistics & Packaging Workflow

**Current state**: Manual order picking, packing, label printing.

**Research questions**:
1. **Packing workflow optimization**: Can we automate label printing? Use packing slips? (Target: <5 min per order for solo operation)
2. **Packaging consistency**: How do we ensure uniform branding + product quality perception? (Tissue paper, inserts, thank-you cards, etc.)
3. **Shipping label workflow**: Currently manual via Etsy; can we integrate with shipping software (Pirate Ship, ShipStation)?
4. **Returns handling**: Where do returned items go? How do we verify and restock?

**Research method**:
- Workflow time study: Time a mock order-to-ship cycle (pick from shelf, inspect, pack, print label, bag); identify bottlenecks
- Tool evaluation: Test Pirate Ship or ShipStation free tier for label printing integration
- Packaging audit: Review 5 top-reviewed Etsy sellers in cable management category; evaluate unboxing experience

**Deliverable**: `SHIPPING_AND_PACKAGING_WORKFLOW_PROCEDURES.md`
- Packing checklist template
- Recommended label printing integration (Pirate Ship vs. manual)
- Returns handling procedures
- Packaging style guide (brand consistency, insert templates)

**Effort**: 4–6 hours (workflow analysis, tool evaluation, documentation)

---

## Execution Timeline & Trigger Conditions

### Phase 1 Baseline (June 3–30)
- Test print execution (unblocks research start)
- Etsy launch + Phase 1 data collection (June 3–30)
- Q3 library verification (complete; see Section 1 findings below)

### Phase 2 Research Initiation (June 30 onwards)
Once Phase 1 traction data is available (cumulative revenue, order count, product mix by SKU), activate research tracks in parallel:

| Scenario | Trigger Date | Research Tracks Activated | Effort/Week | Timeline to Completion |
|---|---|---|---|---|
| **Conservative** | July 1 | Track D (fulfillment) only | 3–4h/week | Complete by July 15; leverage for Solo operation optimization |
| **Standard** | July 1 | Tracks A, B, D in parallel | 12–15h/week | All complete by Aug 1; results inform Aug capex/supplier negotiation |
| **Aggressive** | July 1 | Tracks A, B, C, D in parallel | 20–25h/week | All complete by July 20; results inform July capex/FBA/channel expansion decisions |

### Research Completion & Application

- **Mid-August gate** (after Standard scenario Phase 2 hardware deployment): Re-evaluate Track C (market expansion) based on phase 2 traction
- **September decision** (after Aggressive scenario Phase 2 + laser acquisition): Finalize Track C recommendations for Q4 product launches
- **Q4 2026**: Execute product expansion + new channel launches (FBA, TikTok Shop) based on research findings

---

## Key Findings & Recommendations (Placeholder for Research Results)

### Q3 Library Verification ✅ COMPLETE

**Status**: COMMODITY_PRODUCT_LIBRARY_Q3_2026.md committed in Session 3901.

**Contents verified**:
- ✅ 23 SKUs across 5 categories (cable management, desk org, gridfinity, home, seasonal)
- ✅ Full unit economics: material cost, machine time, packaging, Etsy fees, net margin per SKU
- ✅ Design-readiness status: 13 SKUs design-ready (can list immediately), 6 need CadQuery work (~15 hours total)
- ✅ Market research basis: Etsy pricing validation (June 2026), competitor analysis, supply chain pricing current
- ✅ Library-level economics: $1,920/month net revenue projected at 2 units/week per SKU (conservative); $2,500–$3,500 at realistic sell-through

**Confidence**: 90% (unit economics locked from production cost model; design readiness verified; market pricing validated June 2026)

### Post-Library Research Priorities (to be populated during execution)

*[Track A findings will populate here after research executes]*
*[Track B findings will populate here after research executes]*
*[Track C findings will populate here after research executes]*
*[Track D findings will populate here after research executes]*

---

## Resource Allocation & Parallelization

### Recommended Execution Path (Standard Scenario)

**Week of June 24–30**:
- Await test print completion (user action)
- Begin Track D.1 (queue management) — design-independent, can start immediately post-test-print
- Prep Track B research (gather shipping cost data from Phase 1 orders)

**Week of July 1–7**:
- Execute Tracks A, B, D in parallel (12–15 hours total)
- Complete Track A supplier outreach (contact 5+ filament suppliers for bulk pricing)
- Complete Track B shipping cost analysis from Phase 1 data
- Document Track D queue management system

**Week of July 8–14**:
- Compile Track A supplier comparison matrix
- Complete Track B 3PL research and FBA cost analysis
- Finalize Track D fulfillment procedures

**August 1**: All Standard scenario research complete. Results inform Printer 2 acquisition decision + supplier negotiation.

### Recommended Execution Path (Aggressive Scenario)

**Week of June 24–30**: Same as Standard + prep Track C (competitive market research)

**Week of July 1–7**: 
- All 4 tracks (A, B, C, D) in parallel
- Allocate 5–6h/track minimum
- Intensive competitive analysis for Track C

**By July 20**: All research complete. Results inform Printer 2/3 acquisition decision + market expansion strategy.

---

## Success Criteria & Measurement

### Research Quality Gates

1. **Track A** (Supply Chain): ≥3 qualified suppliers contacted, 2 comparison proposals received, cost reduction potential quantified
2. **Track B** (Logistics): Regional shipping cost matrix built from Phase 1 data, 3PL breakeven analysis complete, FBA fee impact modeled
3. **Track C** (Market Expansion): ≥10 product categories researched, top 5 ranked by ROI/demand/effort, bundle strategy modeled
4. **Track D** (Fulfillment): All 23 SKUs print-tested, QC defect modes documented, inventory model simulates all three scenarios

### Decision Readiness

By August 1 (Standard scenario) or July 20 (Aggressive scenario):
- Supplier negotiations staged and ready to execute
- Shipping strategy finalized (3PL decision made or deferred)
- Market expansion roadmap locked (product priorities, timeline, resource allocation)
- Fulfillment workflow procedures documented and testable

---

## Appendix: Open Questions for Phase 1 Data Validation

Once Phase 1 data arrives (June 30), the following questions should be re-evaluated:

1. **Demand distribution**: Which product categories drove sales? (Cable clips, gridfinity, seasonal?) — informs Track C prioritization
2. **Regional shipping patterns**: Did West Coast orders incur higher shipping? — validates Track B assumptions
3. **Return/defect rate**: How many defective products were returned? — informs Track D QC strategy
4. **Bundle viability**: Did any bundle listings outperform individual SKU sales? — informs Track C bundle strategy
5. **Time-to-first-review**: How quickly did Phase 1 orders generate reviews? — affects Track C launch timing

These findings will be incorporated into the final research deliverables and Phase 2 execution plan.

---

**Status**: Framework-ready for Phase 2 research execution.
**Next step**: Await test print completion; activate research tracks based on Phase 1 traction signal and scenario selection (June 30).
