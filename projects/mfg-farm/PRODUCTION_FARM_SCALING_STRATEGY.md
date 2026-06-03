---
title: "Production Farm Scaling Strategy — ModRun Cable Management"
project: mfg-farm
created: 2026-06-03
status: production-ready
decision-date: 2026-06-03
scope: >
  Unit economics, breakeven analysis, 2-printer and 5-10 printer facility planning,
  adjacent manufacturing ROI, optimal scaling order, and 12-month execution roadmap.
  Written for June 3 decision if test print passes.
depends_on:
  - cost-model-spreadsheet.csv
  - MULTI_PRINTER_SCALING_ROADMAP.md
  - MULTI_PRINTER_FARM_ARCHITECTURE.md
  - 8-printer-farm-cost-model.md
  - ADJACENT_MANUFACTURING_VIABILITY_STUDY.md
  - ETSY_LAUNCH_SEQUENCE_AND_CHECKLIST.md
---

# Production Farm Scaling Strategy — ModRun

**Lead finding**: This is a capital-light, high-margin manufacturing business. Every printer added
after the first pays back in 5–8 weeks at target demand. The primary constraint throughout is
demand, not equipment. Phases are demand-gated — move forward when orders exceed capacity,
not when the calendar says so. At full 5-printer traction the business generates $13,000–14,000
net per month with a total hardware investment of under $2,200.

---

## Section 1: Unit Economics — Single Printer Baseline

The cost model below uses the validated numbers from `cost-model-spreadsheet.csv` and the
blended product mix assumption (70% cable clip bundles, 30% rail orders). All figures are in USD.

### 1.1 Bill of Materials and COGS per Unit

The ModRun product line ships two primary products:

**ModRun Cable Clip** (3mm/6mm/12mm bore variants — `modrun_clip_b123d.py`):
- Print weight: 3–4g per clip, shipped in 3-unit bundles (~12–16g bundle)
- Print time: 22–26 min per clip at 200 mm/s outer wall, 0.20mm layer height, 20% gyroid infill

**ModRun Desk Rail** (desk_clamp or adhesive variant — `modrun_rail_b123d.py`):
- Print weight: 85–100g per rail (200mm × 24mm × 16mm body plus mounting foot)
- Print time: 3.5–5 hr per rail (solo print; no multi-up nesting)

**Blended unit economics at 20 units/week** (steady-state single-printer sweet spot):

| Cost Component | Clip Bundle (3-pack) | Rail | Blended (70/30 mix) |
|---|---|---|---|
| Filament (PLA+ at $12/kg) | $0.19 | $1.08 | $0.46 |
| Scrap allowance (5%) | $0.01 | $0.05 | $0.02 |
| Labor: harvest + QC + pack (90 sec, $15/hr) | $0.38 | $0.38 | $0.38 |
| Packaging (poly mailer + insert) | $0.18 | $0.35 | $0.23 |
| Etsy listing fee ($0.20/transaction) | $0.20 | $0.20 | $0.20 |
| Etsy transaction fee (6.5%) | $1.62 | $2.27 | $1.84 |
| Etsy payment processing (~3%) | $0.75 | $1.05 | $0.85 |
| Equipment depreciation (P1S at $399, 5,000hr life) | $0.10 | $0.70 | $0.28 |
| Electricity ($0.17/kWh, ~0.15 kWh/hr) | $0.09 | $0.77 | $0.29 |
| USPS First Class shipping (absorbed in price) | $4.00 | $5.25 | $4.37 |
| **Total COGS** | **$7.52** | **$12.10** | **$8.92** |
| **Retail price** | **$24.99** | **$34.99** | **$27.50** |
| **Gross profit per unit** | **$17.47** | **$22.89** | **$18.58** |
| **Gross margin** | **69.9%** | **65.4%** | **67.6%** |

**Notes on the numbers**:

- Shipping is the largest single cost component at 15–16% of revenue. The model treats it as
  absorbed into the retail price (free shipping on Etsy improves conversion measurably).
  Switching to a buyer-paid $3.99–4.99 shipping profile would increase net margin by
  approximately $0.50–1.50/unit but may suppress conversion by 10–20% at current Etsy
  competition levels. Recommend free shipping until 50+ reviews establish search position.

- Etsy fees (transaction 6.5% + payment processing ~3% + listing $0.20) total roughly 9.5%
  of gross revenue. This is a fixed platform cost that does not improve with scale on Etsy.
  Amazon FBA fees run 28–32% but eliminate shipping and packaging labor — that tradeoff
  becomes favorable above 50 units/week when labor time cost exceeds the Etsy fee
  advantage.

- At 20 units/week (the single-printer steady state before ordering a second printer), monthly
  gross profit is approximately $1,486. After deducting a $150/month filament replenishment
  run, $30/month in consumables, and a reasonable $100/month allocation for packaging
  supplies, **monthly net cash from the single-printer operation is $1,200–$1,350/month**.

### 1.2 Startup Capital and Time to Cash Flow Positive

| Item | Cost |
|---|---|
| Bambu P1S (existing; sunk cost) | $399 |
| Launch filament kit (3× black, 2× white, 1× grey PLA+) | $72 |
| Packaging supplies 3-month supply | $45 |
| Etsy setup (listings, photography) | $0–50 |
| Pirate Ship / shipping label account | $0 |
| **Total startup capital** | **$516–566** |

**Cash flow positive**: Day 1 of first order. At $24.99 AOV and $8.92 COGS, each order
generates $16+ in gross profit before shipping. Startup capital is recovered in the first
30–35 orders (roughly the first 2–3 weeks at 5 orders/day during launch week).

---

## Section 2: Breakeven Analysis by Configuration

### 2.1 What "Breakeven" Means at Each Phase

At single-printer scale the business is already cash-flow positive from Day 1. The relevant
breakeven questions are:

1. How many units/month to cover the **incremental cost of adding a printer**?
2. At what revenue level does adding a **part-time assistant** become net-positive?
3. What monthly revenue level sustains **each staffing and infrastructure configuration**?

### 2.2 Breakeven Table by Configuration

| Configuration | Fixed Monthly Overhead | Variable COGS/unit | Monthly Units for Overhead Breakeven | Revenue at Breakeven |
|---|---|---|---|---|
| 1 printer, solo | $280 (filament + consumables + Etsy fees) | $8.92 blended | 16 units | $439 |
| 2 printers, solo | $380 (added filament + depreciation) | $8.77 | 22 units | $605 |
| 3 printers + PT assistant (8 hr/wk) | $850 (above + $600/month labor) | $8.50 | 53 units | $1,457 |
| 4 printers + PT assistant (20 hr/wk) | $1,300 (above + expanded labor) | $8.25 | 86 units | $2,365 |
| 5 printers + FT tech + PT packer | $4,200 (labor $3,600 + overhead) | $7.85 | 293 units | $8,058 |

**Key insight on the 5-printer threshold**: The fixed cost jump at 5 printers (full-time tech at
$2,400–$2,880/month) is the largest single discontinuity in this scaling model. Adding a
full-time employee requires sustained monthly revenue above $8,000 before the operation is net
positive again. This is why Printer 5 and the first FT hire are the Phase 3 gates — they require
genuine demand confirmation, not just capacity ambition.

### 2.3 Incremental Printer Breakeven

Each additional Bambu P1S costs $399 (current street price as of May 2026). At the
$18.58/unit gross profit derived above:

| Printer Added | Hardware Cost | Breakeven Units | Breakeven Weeks (at trigger demand) | Breakeven Days |
|---|---|---|---|---|
| Printer 2 | $399 | 21.5 units | ~3 weeks | ~21 days |
| Printer 3 | $399 | 21.5 units | ~2.5 weeks | ~17 days |
| Printer 4 | $399 | 21.5 units | ~2 weeks | ~14 days |
| Printer 5 | $399 | 21.5 units | ~1.5 weeks | ~11 days |

Printer hardware payback accelerates at higher volumes because throughput per unit is higher
and per-unit COGS improves slightly with bulk filament pricing. Every printer addition in this
model pays back in under 4 weeks once added demand absorbs its capacity.

---

## Section 3: 2-Printer Operation

### 3.1 What Triggers Printer 2

The trigger for ordering Printer 2 is **30+ units/week sustained for two consecutive weeks**
with an unfulfilled backlog (processing times set to 5+ days on Etsy, or customers waiting more
than 48 hours for their order to begin printing). Do not order Printer 2 based on a single spike
week — the trigger requires demonstrated sustained demand.

At $399 hardware cost with a 3-week payback at 30 units/week, the cost of **waiting one extra
week** after the trigger is met is $556 in forgone gross profit (30 units × $18.58). Ordering the
printer the day the 2-week trigger is confirmed costs $399. The decision is straightforward.

**Timeline to Printer 2 decision**: If launch is June 3 and Etsy traction follows the baseline
scenario (50% conversion rate from shop visits at 2% conversion), the two-week trigger is
plausible by **late June to mid-July 2026**, depending on how quickly Etsy search position
establishes. The conservative estimate (demand builds slowly) sets Printer 2 arrival in **early
August**.

### 3.2 Investment Required

| Item | Cost |
|---|---|
| Second Bambu P1S | $399 |
| Additional AMS spool (if color expansion) | $0 (use existing AMS strategy) |
| Bambu Farm Manager software | $0 (free, Windows, LAN mode) |
| Additional filament safety stock (3-week buffer, 2nd printer) | ~$75 |
| Dedicated 20A circuit (if not already present) | $0–$250 |
| **Total Printer 2 Investment** | **$399–$724** |

The dedicated circuit is only required if the existing household circuit is already loaded to >80%
with Printer 1 and other devices. Two P1S printers on a single 20A circuit draw ~500W sustained,
well within limits. Peak bed-heating draws 2,000W — stagger starts by 10 minutes to avoid
simultaneous bed preheat.

### 3.3 Facility Constraints

**Space requirement**: Two Bambu P1S units require approximately 15 square feet of bench
space (each unit: 24" wide × 19" deep with 18" side clearance for AMS door access). A standard
6-foot folding table accommodates both units plus a small QC area. The entire 2-printer
operation fits in a spare bedroom, corner of a garage, or basement workshop.

**Electrical**: Two P1S printers at sustained load draw ~500W. No dedicated circuit required
unless the existing circuit is already near capacity. Set Printer 2 to start 10 minutes after
Printer 1 during the bed preheating phase.

**Cooling/ventilation**: P1S includes a HEPA + activated carbon filter enclosure. Two units in a
ventilated room (window or door ajar during printing) is sufficient for PLA+ production.
No exhaust fan required at the 2-printer stage.

**Monitoring**: Bambu Farm Manager (free, Windows) handles 2-printer fleet monitoring with
LAN mode — view both printers simultaneously, push jobs, check status without cloud
dependency.

### 3.4 Expected Economics at 2-Printer Operation

| Metric | Conservative | Realistic | Optimistic |
|---|---|---|---|
| Weekly output (demand-capped) | 50 units | 70 units | 100 units |
| Monthly gross revenue | $5,498 | $7,700 | $10,996 |
| Monthly COGS + overhead | $1,785 | $2,450 | $3,430 |
| Monthly net profit (pre-tax) | $3,713 | $5,250 | $7,566 |
| Printer 2 payback period | 4 weeks | 3 weeks | 2 weeks |

The **realistic** scenario (70 units/week at $27.50 AOV) represents full-traction Etsy with
established reviews (20+), a page-1 search position for 2–3 primary keywords, and an active
bundle SKU in the mix. This is achievable by Month 3 post-launch at normal Etsy growth rates.

---

## Section 4: 5-10 Printer Farm Planning

### 4.1 Physical Space and Infrastructure

**The 5-printer farm fits in a 1-car garage bay** (typically 10×20 ft = 200 sq ft) with room for
all operational zones. Space allocation at full 5-printer configuration:

| Zone | Area Required | Description |
|---|---|---|
| Printer zone (5 units) | 35 sq ft | Two 6-ft benches, printers paired with 18" side clearance |
| QC and finishing bench | 28 sq ft | Inspection light, calipers, snap-test fixture |
| Packaging station | 18 sq ft | Poly mailers, tape dispenser, thermal label printer |
| Filament storage | 12 sq ft | Sealed cabinet with desiccant; 4-week buffer = ~40 spools |
| Electrical panel zone | 4 sq ft | Two dedicated 20A circuits; labeled breakers |
| Finished goods buffer | 20 sq ft | Shelf for pre-printed safety stock (2–5 days demand) |
| **Total** | **~117 sq ft** | Fits within standard 1-car garage with room for workflow movement |

**Electrical requirements at 5 printers**:
- Sustained draw: 1,250W (250W × 5)
- Peak (bed heating, all printers): 5,000W
- Required: Two dedicated 20A circuits (10–14 AWG wire; GFCI protection at the panel)
- Staggered start protocol: Start each printer 8–10 minutes apart to prevent simultaneous
  bed preheat from tripping a circuit. SimplyPrint's scheduled-start feature automates this.
- Electrical setup cost: $300–500 for a licensed electrician to run two dedicated 20A circuits
  from the breaker panel to the printer zone.

**Ventilation at 5 printers**:
- Install a 110 CFM window exhaust fan ($40–60) to achieve 8+ air changes per hour in a
  standard 10×20 garage bay.
- Add a dehumidifier ($150–200) set at 40% RH to protect filament spools and print
  consistency. PLA+ absorbs moisture and begins stringing at >50% RH.
- Total ventilation investment: $200–260 one-time. Running cost: ~$10–15/month.

### 4.2 Capital Investment — 5-Printer Farm

| Item | Timing | Cost |
|---|---|---|
| Printer 1 (existing) | Already owned | $0 |
| Printer 2 | Phase 1 trigger (late June or July) | $399 |
| Printer 3 | Phase 2 trigger (August) | $399 |
| Printer 4 | Phase 3 trigger (September) | $399 |
| Printer 5 | Phase 3+ trigger (October-November) | $399 |
| Bambu Farm Manager + SimplyPrint Starter | Phase 2 | $0 + $10/month |
| Second dedicated 20A circuit | Phase 3 | $150–250 |
| Ventilation (exhaust fan + dehumidifier) | Phase 3 | $200–260 |
| Polymaker wholesale account activation | Phase 3 | $1,000 MOQ (filament inventory, not overhead) |
| Additional shelving and workbench | Phase 2-3 | $300–400 |
| Pre-stocked consumables kit (per new printer) | Each addition | ~$90/printer |
| **Total incremental investment: Printers 2–5** | **Months 1–6** | **$2,600–$3,500** |

**Note**: The $1,000 Polymaker wholesale MOQ is inventory (filament that will be consumed in
production), not a sunk cost. It is treated as working capital, not capex.

### 4.3 Expected Revenue at 5-10 Printers

| Configuration | Monthly Units (80% utilization) | Monthly Gross Revenue | Monthly Net Profit |
|---|---|---|---|
| 5 printers, solo + PT assistant | 700–800 | $19,250–$22,000 | $12,500–$14,500 |
| 6 printers, 1 FT tech | 900–1,050 | $24,750–$28,875 | $14,500–$17,500 |
| 8 printers, 1 FT + 1 PT packer | 1,200–1,400 | $33,000–$38,500 | $18,000–$22,000 |
| 10 printers, small commercial facility | 1,500–1,800 | $41,250–$49,500 | $20,000–$26,000 |

**Critical caveat**: These figures are throughput-ceiling numbers. Actual revenue is
demand-capped through at least Month 6. The printer farm can produce 5× what the Etsy
algorithm will route to a new seller with fewer than 50 reviews. Equipment is ahead of demand
in every phase except Phase 3+. This is intentional — the constraint is market traction, and
the correct response is to invest in Etsy SEO and product diversification, not to hold back printer
purchases that cost less than 3 weeks of production.

### 4.4 Staffing at Scale

| Phase | Weekly Output | Owner Hours/Week | First Hire | Monthly Labor Cost (cash) |
|---|---|---|---|---|
| Phase 0 (1 printer) | 20–50 units | 10–15 hrs | None | $0 |
| Phase 1 (2 printers) | 50–100 units | 15–20 hrs | PT post-processor, 8–12 hrs/wk | $0–$600 |
| Phase 2 (3–4 printers) | 100–200 units | 20–25 hrs | PT post-processor expanded, 20–25 hrs/wk | $1,200–$1,500 |
| Phase 3 (5 printers) | 200–350 units | 25–30 hrs | FT production tech (40 hrs/wk) | $2,400–$2,880 |
| Phase 3+ (6–8 printers) | 350–600 units | 30–35 hrs | FT tech + PT packer | $3,000–$3,780 |

The first hire (part-time post-processor at $15/hour) is purely a time-purchase: the operator
buys back 8–12 hours/week for business development, SEO work, and new product design.
The economic trigger is not "I can afford it" but rather "post-processing is taking more than
2 hours/day and crowding out business development time."

At 8–10 printers, a 10×20 garage bay begins to feel constrained during peak packing days.
This is the trigger point to evaluate a small commercial studio (300–600 sqft at $800–$1,500/month
in most US metro areas), which adds laser and resin capabilities alongside expanded printer
capacity without zoning complications of a residential workspace.

### 4.5 Automation Opportunities

At 3+ printers, automation ROI becomes real:

**SimplyPrint Starter ($10/month)**: AI failure detection via webcam catches spaghetti prints
within 60–90 seconds. One prevented 4-hour overnight failure at $15.50/hr opportunity cost =
$62 in saved machine time. Pays for itself in the first caught failure.

**Printago ($29/month, 5 printers)**: Connects Etsy orders directly to print queue. Eliminates
manual order-to-queue transcription. At 50+ orders/week, this saves 1–2 hours/week of
administrative time.

**Pirate Ship**: Already zero-cost; bulk label printing at 5–15% below retail USPS rates.

**Batch slicing with locked profiles**: Create one master 3MF per SKU. Lock the slicer profile
(0.20mm layer, 20% gyroid, no supports, 200 mm/s outer wall). Per-job slicer time drops from
15 minutes to under 2 minutes. Across 5 printers running 5 jobs/day each, this saves 5+ hours
of slicer overhead weekly.

**Thermal label printer (Rollo or DYMO 4XL at $150–200)**: At 30+ orders/week, label printing
on inkjet wastes 10–15 minutes daily in print queue management. A dedicated thermal label
printer cuts label production to 2–3 seconds per label.

---

## Section 5: Adjacent Manufacturing ROI

The following analysis draws from `ADJACENT_MANUFACTURING_VIABILITY_STUDY.md` and
applies the ROI lens directly to the scaling decision sequence.

### 5.1 ROI Comparison Table

| Process | Setup Capital | Time to First Sale | Monthly Revenue Potential (at scale) | Gross Margin | Payback Period | Customer Overlap |
|---|---|---|---|---|---|---|
| FDM (current) | $0 (sunk) | Day 1 post-launch | $5,000–$15,000+ | 67–74% | Already paid | Baseline |
| Laser engraving (bureau → DIY) | $0 → $1,899 | 2–3 weeks | $3,000–$8,000 incremental | 75–79% (DIY) | 3.2 months | Very high (same buyer) |
| Acrylic label panels (same laser) | $0 additional | 3–4 weeks | $2,000–$5,000 incremental | 82–85% | Same machine | High (same buyer) |
| Resin accessories (MSLA) | $574 | 4–6 weeks | $1,500–$4,000 incremental | 55–75% | 3–5 months | High (premium buyer) |
| CNC aluminum | $4,195–$8,970 | 6–10 weeks | $1,000–$3,000 (thin demand) | 29–66% | 12–18 months | Low (different segment) |

### 5.2 Highest ROI: Laser Engraving

**Laser engraving has the highest adjacent ROI** for ModRun at current scale, for four
compounding reasons:

1. **Zero capital to validate**: Bureau engraving (SendCutSend or local shop) validates demand
   at $50–150 spend before any equipment decision.

2. **Uses the existing product as substrate**: No new design cycle required. The ModRun clip
   already exists; engraving adds a personalized label — "USB-C," "HDMI," "MONITOR," or
   any custom text. This is a pure price-premium play with no complexity increase in production.

3. **Documented Etsy whitespace**: Fewer than 200 listings for "laser engraved cable clip"
   as of May 2026. Top sellers earn 4.8+ ratings. No dominant incumbent.

4. **Margin profile at DIY scale**: Moving from a $12–15 generic clip to a $28–35 personalized
   set increases revenue per order by 133% while COGS increase by only 50–80% (adding $0.08–
   $0.20 in laser operating cost plus $0.50–$1.00 in premium packaging). Gross margin stays at
   75–79% while revenue per order nearly triples.

**Equipment decision**: xTool S1 40W at $1,899. Breakeven at 633 units engraved. At
200 engraved units/month (achievable in Month 3–4 if demand validates), payback in
3.2 months. The machine also handles acrylic cutting for label panels, making the capital
purchase serve two product lines.

### 5.3 Second: Acrylic Label Panels (Same Machine)

**Acrylic cable zone label panels** (5-panel sets: "MONITOR," "AUDIO," "USB HUB,"
"KEYBOARD," "CHARGING") are the natural bundle companion to the ModRun clip. Same buyer,
same Etsy shop, sold as part of a "Complete Desk Cable Organization Kit."

- Material cost per 5-panel set: $0.35–$1.00 (3mm clear acrylic, sourced in full sheets at
  $18–25 per 4×8ft sheet yielding ~350 panels)
- Retail price: $15–28 per set
- Gross margin (DIY laser): 82–85%
- No additional equipment cost beyond the xTool S1 already acquired for engraving

**Bundle economics**: A "Complete Kit" (5 clips + rail + 5 acrylic labels + installation card)
at $55–65 retail generates approximately $40–48 in gross profit per order at 72–75% margin
while increasing average order value from $27 to $60+. This is the highest-leverage revenue
lever in the entire roadmap that does not require a new customer.

### 5.4 Third: Resin Accessories ($574, Month 6)

MSLA resin printing (Elegoo Saturn 4 Ultra 16K + wash station at ~$574 total) adds optical
transparency — a capability neither FDM nor laser provides. Transparent channel covers that
clip over the ModRun rail fill a niche with no dominant Etsy competitor as of May 2026. The
$574 investment breaks even in 3–5 months at modest volumes.

Launch resin after engraving revenue validates the premium buyer segment. The resin buyer is
the same person who paid $35 for engraved clips — they want an aesthetic desk setup, not just
functional cable management.

### 5.5 CNC Aluminum — Do Not Pursue in Year 1

CNC aluminum has the lowest ROI of any adjacent process at current scale:
- Minimum credible equipment ($4,195 for Tormach xsTECH) requires sustained monthly
  revenue from aluminum SKUs to justify
- Etsy market for machined-metal cable hardware has fewer than 100 active listings with
  meaningful volume
- Domestic service bureau path (Protolabs/Xometry) carries $22–48/unit cost against a
  $45–85 retail price, leaving 29–52% gross margin — the worst in the portfolio
- Learning curve: 20–40 hours CAM training plus workholding and feeds/speeds competency

**Year 1 recommendation**: Ignore CNC entirely. If a B2B or corporate client specifically
requests aluminum hardware, fulfill via JLCCNC (China bureau at $8–18/unit) as a one-off.
Do not build inventory or tooling capability until Year 2–3 at the earliest, and only if that
B2B segment generates consistent demand above 50 units/month at $45+.

### 5.6 Bundle vs. Separate Operations

**Bundle operations under one Etsy shop** throughout Year 1. The reasons are arithmetic:

- Etsy's search algorithm rewards shops with higher review counts and consistent sales
  velocity. Splitting into two shops (one FDM, one laser) halves review accumulation speed
  for each shop.
- The buyer is the same person. A desk organization buyer who finds the cable clip listing will
  also buy the engraved version and the acrylic labels in the same cart. Cross-selling within
  a single shop is vastly more efficient than organic search discovery across two shops.
- Etsy "bundles" (Etsy's native bundle feature or custom product listings) allow a single
  $60 transaction to encompass FDM clips, acrylic panels, and rails — generating the same
  gross profit as 3–4 individual small orders without the 4× shipping overhead.

**Separate operations only make sense** if laser or resin revenue grows large enough to
warrant a distinct brand identity (e.g., "ModRun Artisan" for premium handmade resin items
vs. "ModRun" for functional FDM products). This is a Year 2–3 decision, not a Year 1
consideration.

---

## Section 6: Optimal Scaling Order

### 6.1 Phase Definitions

**Phase 1: Single Printer Launch (June 2026)**
- State: 1× Bambu P1S, Etsy shop live, cable clips + rails listed
- Weekly output capacity: 40–50 units (printer ceiling); actual demand: 5–25 units/week
- Revenue: $140–$690/week
- Primary work: SEO refinement, review generation, product photography improvement,
  first bundle listings
- Gate to Phase 2: Sustained 30+ orders/week OR $800/week revenue for 2 consecutive weeks

**Phase 2: Second Printer + Etsy Traction ($1,500/month → add Amazon)**
- Trigger: Phase 1 gate met
- State: 2× P1S, Bambu Farm Manager, part-time post-processor (optional, 8 hrs/wk)
- Weekly output: 50–100 units
- Revenue target: $1,500–$4,000/month
- Primary work: First laser validation run (bureau engraving, 50 units), acrylic label panel
  SKU launch, Etsy bundle listings
- **Amazon FBA trigger within Phase 2**: When Etsy reaches $2,500+/month sustained AND
  the 2-printer cluster runs >80% utilization for 2 consecutive weeks. Amazon adds 28–32%
  fees but provides access to a buyer pool 10× larger than Etsy for functional desk accessories.
  Pre-stage FBA inventory at 100 units minimum before activation.
- Gate to Phase 3: $3,500+/month revenue sustained OR Etsy waitlist forming (processing
  time forced to 7+ days to manage backlog)

**Phase 3: Scale to 3–5 Printers ($3,500/month → full farm)**
- Trigger: Phase 2 gate met
- Hardware: Add Printers 3, 4, 5 over 3–4 months (demand-gated)
- Revenue target: $7,000–$19,000/month
- Infrastructure: SimplyPrint, dedicated circuits, ventilation, filament storage cabinet
- Laser equipment acquisition (xTool S1 at $1,899) when bureau validation confirms 50+
  engraved orders/month
- Full-time production tech hire when reaching 200+ units/week
- Gate to Phase 4: Revenue $8,000+/month with 5-printer cluster at >75% utilization

**Phase 4: Adjacent Manufacturing + Channel Diversification**
- Trigger: Phase 3 gate met
- Laser in-house (xTool S1), acrylic cutting live, resin accessories (Month 9–12)
- Amazon FBA fully integrated (if not already done in Phase 2)
- Consider small commercial facility (300–600 sqft) if 5-printer garage operation is at
  spatial limit and combined revenue exceeds $15,000/month
- Product ecosystem: 25–35 active SKUs, $15,000–$30,000/month gross revenue

### 6.2 Phase Thresholds — Explicit Numbers

| Threshold | Metric | Value | Action |
|---|---|---|---|
| Phase 2 entry | Weekly orders | 30+ for 2 consecutive weeks | Order Printer 2 |
| Amazon FBA entry | Monthly Etsy revenue | $2,500+/month | Pre-stage FBA inventory |
| Phase 3 entry | Monthly revenue | $3,500+/month | Order Printer 3 |
| Laser equipment | Monthly engraved orders | 50+/month (bureau validation) | Buy xTool S1 |
| PT assistant hire | Daily post-processing time | >2 hr/day | Hire at $15/hr, 8–12 hrs/wk |
| Phase 3 full (Printer 5) | Monthly revenue | $7,000+/month | Order Printer 5 |
| FT tech hire | Weekly output | 200+ units/week | Hire at $15–18/hr, 40 hrs/wk |
| Phase 4 entry | Monthly revenue | $8,000+/month from 5-printer cluster | Evaluate facility + resin |
| Commercial facility | Monthly revenue | $15,000+/month | 300–600 sqft studio at $800–$1,500/mo |

---

## Section 7: 12-Month Post-Test-Print Roadmap

This calendar assumes test print passes on or around **June 3, 2026**. All milestone dates
are demand-gated; if demand arrives faster, compress the timeline. If slower, hold phase and
focus on conversion rate optimization before adding capital.

---

### Month 1: June 2026 — Launch and Validation

**Weeks 1–2 (June 3–15): Etsy launch execution**
- Execute ETSY_LAUNCH_SEQUENCE_AND_CHECKLIST.md Part 1 immediately after test print
  pass confirmation.
- List cable clips (3mm, 6mm, 12mm bore) and rails (desk_clamp + adhesive variants) with
  the introductory pricing (-15% for first 5 days, then full price).
- Photography: 5–7 images per listing; hero shot in-context on a desk workspace setup.
- SEO: Primary keywords "cable clip 3D printed," "desk cable organizer," "cable management
  clips." Long-tail: "snap fit cable clip modular," "under desk cable clips PLA."
- Safety stock target: 10–15 clips pre-printed before going live (same-day ship capability).
- Pirate Ship account live; thermal label printer connected if available.

**Weeks 3–4 (June 16–30): Analyze and optimize**
- Collect conversion rate data from Etsy analytics. Target: 2–5% conversion from shop
  visits to purchases.
- If conversion is below 2%: adjust title keyword order, reorder photos (put best-performing
  hero image first), and add $1 temporary discount on slowest-moving SKU.
- If orders are arriving faster than printing capacity (more than 5/day): set processing time
  to 5 business days and begin printing safety stock in all available overnight windows.
- Add one bundle listing: "ModRun Starter Kit" (3-clip bundle + rail) at $39.99, targeting
  $8–10 higher AOV than individual SKUs.
- Begin bureau laser validation: send 20 clips to a local engraving shop or SendCutSend for
  personalized label engraving. Budget $50–100. List as "Custom Labeled Cable Clips" at
  $32–38 per set of 5. This listing has no inventory risk — print on demand per order.

**June metrics target**: 30–80 total orders, 3–10 reviews, conversion rate 2%+, $600–$1,200
gross revenue. Breaking even on startup capital by end of June.

---

### Month 2: July 2026 — Phase 2 Decision Point

**Assess Phase 1 gate**: Review July 1 metrics against the trigger (30+ orders/week sustained).

**If gate met (most likely outcome at normal Etsy growth)**:
- Order Printer 2 immediately (Bambu P1S, ~5–10 day delivery).
- Install Bambu Farm Manager.
- Begin part-time post-processor recruiting (Craigslist, college job boards, local Facebook groups).
  Target: 1099 contractor at $15/hour for 8–12 hours/week.
- Increase filament safety stock to 3-week buffer.

**If gate not yet met**:
- Do not order Printer 2 yet.
- Focus on conversion rate improvement: A/B test title keywords, add lifestyle photos showing
  multiple clips in use, launch $1 off coupon for "CABLE10" code.
- Target Etsy search position: aim for page 1 on at least two long-tail keywords by end of July.
- Reassess Phase 2 gate the last week of July.

**July product expansion (regardless of gate)**:
- Launch acrylic label panel listing using bureau output (SendCutSend run, ~$40–60 for 20 sets).
  Price: $18–22 per set of 5 panels. This validates demand before buying laser equipment.
- Add headphone hook SKU (cadquery/headphone_hooks.py is already designed and ready to slice).
  Headphone hooks are a natural cross-sell to the desk cable management buyer.

**July metrics target**: 100–200 total orders, 8–20 reviews, $2,000–$4,000 gross revenue.
Part-time contractor identified if Phase 2 gate met.

---

### Month 3: August 2026 — 2-Printer Ramp and First Adjacency Validation

**Hardware**: Printer 2 arrives and is validated (72-hour parallel run on same job profile as
Printer 1; compare first-article quality; adjust slicer profile if any deviation).

**Operations**:
- Part-time post-processor begins (8 hrs/week).
- Establish morning/afternoon batch color schedule: all black jobs in the AM batch, white in
  the PM batch. Eliminates purge waste between jobs.
- Order Printer 3 if August revenue is tracking above $3,500/month.

**Product and marketing**:
- Etsy Ads: Begin $2–5/day spend on top-performing listings (cable clip, bundle kit).
  Target ROAS (return on ad spend) of 3× before increasing budget.
- Review milestone: Aim for 25+ reviews by end of August. Etsy algorithm begins surfacing
  shops with 25+ reviews to page-1 positions for established keywords.
- Bureau laser engraving orders: If "Custom Labeled" listing is generating 10+/month,
  scale bureau orders to 50 units/batch and track total monthly spend. Above $200/month
  in bureau fees, run the xTool S1 ROI calculation.

**August metrics target**: 200–350 total orders (cumulative), 20–35 reviews, $4,000–$7,000
monthly gross revenue. 2-printer fleet running at 60–80% utilization.

---

### Month 4: September 2026 — 3-Printer Farm + Laser Decision

**Hardware**: Printer 3 arrives. Install SimplyPrint Starter ($10/month) for AI failure detection
across 3 printers. Install dedicated 20A circuit if not already present.

**Laser decision**: If bureau laser orders exceed 50 units/month for 2 consecutive months,
purchase xTool S1 40W at $1,899 with LightBurn ($60). This is a $1,960 total investment
with 3.2-month payback at 200 units/month throughput on the machine.

- Once xTool S1 is in house: move all engraving in-house; simultaneously launch acrylic
  label panel production on the same machine. Bureau cost disappears; per-unit laser
  operating cost drops from $3–6 to $0.08–0.20.
- New listings to add: "Custom Engraved Cable Clip Set" at $32–38; "Desk Zone Label Panel
  Set" (5 acrylic labels) at $22–28; "Complete Desk Cable Organization Kit" (clips + rail +
  labels) at $55–65.

**Operations**:
- Polymaker wholesale account setup begins (test spool order first; full $1,000 MOQ at 40+ kg/month).
- Part-time post-processor hours increase to 15–20 hrs/week as output climbs above
  100 units/week.

**September metrics target**: $5,000–$8,000 monthly gross revenue, 3-printer cluster at
60–75% utilization, laser validation complete (bureau or in-house).

---

### Month 5: October 2026 — Amazon FBA Pre-Stage

**Amazon FBA onboarding**: If Etsy revenue is at $4,000+/month and the 3-printer cluster is
running above 75% utilization for 2 weeks, begin Amazon FBA registration.

- Product selection for FBA launch: cable clip 3-pack (most reviewed Etsy SKU), headphone
  hook (cross-sell), and acrylic label panel set. These functional products convert on Amazon
  where search intent is transactional, not discovery-based.
- FBA prep: Apply FNSKU labels (printable from Seller Central), package to Amazon's
  polybag + label requirements, ship initial inventory (50–100 units per SKU).
- Amazon fees (~32% of revenue) are higher than Etsy's (~9.5%), but Amazon's buyer pool is
  10× larger for functional desk accessories and FBA enables Prime 2-day shipping without
  any operator fulfillment work.
- First 30 days of FBA: "Honeymoon period" — Amazon gives new listings placement boost.
  Target 10–20 reviews in first 60 days via Amazon's Request a Review tool.

**October also: Q4 stock build**
- Q4 (October–December) is the highest demand period for desk accessories (back-to-school
  tail + holiday gift buying). Build 3–4 weeks of finished goods inventory buffer in October
  before demand spikes in November–December.
- Set Etsy processing time to 3–5 days (from 1–2 days) to protect fulfillment quality under
  surge demand.

**October metrics target**: $6,000–$10,000 monthly gross revenue (Etsy + early Amazon),
35+ Etsy reviews, laser in-house and operational, FBA account live.

---

### Month 6: November 2026 — 4-Printer Farm + Resin Validation

**Printer 4**: If October revenue exceeded $7,000/month and 3-printer cluster is at >80%
utilization, order Printer 4. Designate one printer as the "color specialist" (runs non-black/white
specialty colors for seasonal and custom orders while main printers run black/white
continuously).

**Resin accessories**: Purchase Elegoo Saturn 4 Ultra 16K ($299–399) + Mercury Plus wash
station ($75–100) = $574 total. Design transparent channel cover that clips over the ModRun
rail; order validation samples. Launch as a new listing: "ModRun Transparent Cable Channel
Cover — fits ModRun Rail" at $22–28. This accessory only sells once the rail exists in the
buyer's home — it is the highest-margin repeat-purchase product in the line.

**Q4 holiday push**:
- Seasonal listings: "Desktop Organization Gift Set" (clips + labels + gift box) at $45–55.
  Laser engraves the recipient's name on 2 clips for personalization. This is a $32–38 GP
  order that is completely unique to ModRun's capabilities.
- Etsy Ads: Increase to $10–15/day for November 15 – December 15 window. Target 3× ROAS.
  If ROAS drops below 2×, cut budget and let organic search carry the load.

**November metrics target**: $8,000–$14,000 monthly gross revenue (Etsy + Amazon),
50+ Etsy reviews, Amazon FBA generating $1,000–$3,000 incremental, Printer 4 arriving.

---

### Month 7–8: December 2026 – January 2027 — Peak + Recovery

**December**: Q4 peak. All printers running at near-full utilization. Printer 4 (or 5 if ordered
in October) online. Primary task is fulfillment excellence — 1-day processing, accurate pick-and-
pack, and proactive customer communication on any delays. Do not launch new SKUs in December;
focus entirely on throughput and review capture from the holiday surge.

**January**: Post-peak correction. Order volume drops 30–50% from December peak. Use
this period to:
- Perform maintenance: nozzle swaps (proactive at 600 hours), bed plate replacements,
  belt tension checks.
- Review full-year economics: Which SKUs generated the highest GP? Which had the most
  returns or complaints?
- Plan Batch 3 product SKUs based on customer keyword data (Etsy search query reports,
  Amazon Brand Analytics if enrolled).
- Evaluate Printer 5 if January revenue remains above $8,000/month despite the post-holiday
  correction.

---

### Month 9–12: February – May 2027 — Ecosystem Build and Scaling Decision

**February–March**: Resin accessories fully validated. Transparent channel cover + color
poured organizer pieces live on Etsy. "Complete Ecosystem Bundle" (clips + rail + labels +
channel cover) at $75–90. This is the highest AOV offering in the line.

**April**: 12-month review. At normal growth trajectory, the business is at:
- 30–40 active Etsy SKUs
- 4–5 printers running
- Amazon FBA contributing 20–30% of revenue
- Monthly gross revenue: $12,000–$20,000
- Monthly net profit: $7,000–$13,000 after all costs
- Capital invested (total, all phases): $8,000–$12,000 (printers, laser, resin, infrastructure)
- ROI on total capital: 10–16× annualized

**Scaling decision at Month 12**:
- If revenue is $15,000+/month: evaluate commercial studio space (300–600 sqft at
  $800–$1,500/month) to formalize operations, enable proper ventilation for resin and laser
  at scale, and allow a second full-time employee.
- If revenue is $8,000–$15,000/month: remain in home/garage operation; add Printer 5 and
  continue product line expansion.
- If revenue is below $8,000/month: diagnose conversion rate issues before adding capital.
  The bottleneck at this point is market traction, not production capacity.

---

## Summary: Decision Calendar for June 3

| Date | Decision | Trigger | Action |
|---|---|---|---|
| **June 3** | Test print result | Pass/fail | Pass → execute ETSY_LAUNCH_SEQUENCE_AND_CHECKLIST.md Part 1 |
| **June 3–15** | Etsy shop live | Test print pass | List clips, rails, bundle; build safety stock |
| **Late June** | Phase 2 gate assessment | 30+ orders/week for 2 weeks | Order Printer 2 ($399) |
| **July** | Bureau laser validation | 10+ engraved orders/month | Send 50 clips to bureau ($50–100) |
| **August** | Printer 3 decision | $3,500/month revenue | Order Printer 3 ($399) + SimplyPrint ($10/mo) |
| **September** | Laser equipment decision | 50+ engraved orders/month bureau | Buy xTool S1 + LightBurn ($1,960) |
| **October** | Amazon FBA pre-stage | $4,000+/month Etsy + 75%+ utilization | Register FBA, prep 100 units per SKU |
| **October** | Q4 stock build | Calendar: Oct 1 | Build 3–4 week finished goods buffer |
| **November** | Printer 4 + resin | $7,000+/month + 80% utilization | Printer 4 ($399), Elegoo setup ($574) |
| **December** | Execute Q4 peak | Calendar | Focus on fulfillment quality, not new SKUs |
| **April 2027** | 12-month strategic review | Revenue trajectory | Scale or optimize per revenue bands above |

---

## Risk Register

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Etsy traction slower than expected | Medium | Delays Phase 2 gate by 4–8 weeks | Improve conversion rate before adding capital; Etsy Ads if organic stalls |
| Printer failure (nozzle, bed, AMS jam) | High (at scale) | Moderate (1–3 day downtime) | Pre-stocked consumables kit ($90/printer); Printer 2 provides redundancy |
| Filament tariff increase | Medium | Low (filament is 5% of COGS) | Phase into Polymaker wholesale (US-warehoused) at Phase 2; tariff impact is $0.02–0.04/unit even in 50% price surge |
| Amazon FBA onboarding delay | Low-Medium | Low (Etsy carries revenue during delay) | Begin FBA registration 6–8 weeks before planned inventory send |
| Snap arm quality issues post-launch | Low (pending test print) | High (returns, bad reviews) | Maintain ±0.05mm tolerance per modrun_clip_b123d.py; 500-cycle snap test before batch production |
| Demand never reaches Phase 3 | Low-Medium | Moderate (stranded at 2-printer scale) | 2-printer operation is net-positive at $5,250/month — a viable steady state indefinitely |
| Competing laser-engraved seller emerges | Medium | Low (first-mover advantage, review moat) | Accelerate review count; laser in-house cuts cost below bureau-dependent competitors |

---

## Sources and Confidence Notes

All numbers in this document are derived from existing mfg-farm research documents and
verified against current market pricing. Key references:

- `cost-model-spreadsheet.csv` — COGS model, blended AOV assumptions, breakeven data
- `MULTI_PRINTER_SCALING_ROADMAP.md` — hardware economics, space planning, phase gates
- `MULTI_PRINTER_FARM_ARCHITECTURE.md` — hardware pricing (verified May 2026), TCO
- `8-printer-farm-cost-model.md` — capital phasing, staffing model, infrastructure costs
- `ADJACENT_MANUFACTURING_VIABILITY_STUDY.md` — laser/CNC/resin ROI, bureau pricing
- `ETSY_LAUNCH_SEQUENCE_AND_CHECKLIST.md` — launch economics, listing strategy
- `cadquery/modrun_clip_b123d.py`, `modrun_rail_b123d.py` — product specs, print weights

**Confidence level**: High on unit economics (derived from validated cost model). Medium on
revenue projections (demand is uncertain; all scenarios are modeled against documented Etsy
benchmarks and conversion rate ranges). Low on Month 9–12 figures (compounding Etsy
algorithm effects and competitive entry are inherently uncertain at this lead time).

**Gaps in the evidence**:
- Actual Etsy conversion rate for cable management accessories in June 2026 (will be known
  within 2 weeks of launch)
- Amazon FBA fee structure for sub-$30 desk accessories (fees vary by size tier; requires
  actual product measurement to confirm classification)
- Real snap arm durability under customer use conditions (pending first production batch and
  customer feedback cycle)
