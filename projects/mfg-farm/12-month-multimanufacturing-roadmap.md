---
title: 12-Month Multi-Manufacturing Roadmap — Capability Sequence, Capital Allocation, and Trigger Criteria
project: mfg-farm
created: 2026-05-05
status: production-ready
session: multi-manufacturing-roadmap
depends_on: multi-color-fdm-strategy.md, resin-printing-viability.md, laser-cutting-capability-assessment.md, cnc-capability-assessment.md, production-scaling-research.md
confidence: high
---

# 12-Month Multi-Manufacturing Roadmap

**Lead finding**: The optimal manufacturing capability sequence is not a technology-first decision — it is a revenue-first decision. Add capabilities only when existing revenue validates demand for what that capability unlocks. The sequence that maximizes revenue with minimal capex: (1) FDM core business at full execution, (2) sequential-batch color validation for free, (3) AMS 2 Pro multi-color at Month 3 ($286), (4) laser engraving at Month 4–5 ($1,899–2,099), (5) resin specialty products at Month 6–9 ($574), (6) CNC deferred to Month 12+ or sourced externally. Total 12-month multi-manufacturing capex budget: $2,759–$2,959 if all triggers are met. If they're not, stay FDM — which remains profitable at $3,000–$5,000/month with a single printer and no additional investment.

---

## Section 1: Capability Addition Sequence

### Why Sequence Matters

Each manufacturing technology requires an operator learning curve, workspace allocation, and ongoing management attention. Adding two capabilities simultaneously halves the time available to master either one. The recommended sequence ensures that each technology is validated and operationalized before the next is added.

**The core principle:** ModRun's FDM product is the proven foundation. Every additional capability must either (a) increase the revenue per unit of an existing product (multi-color, laser engraving), or (b) open a new product category with identified demand (resin, laser cutting). Neither justifies acquisition unless ModRun's core FDM business is generating consistent orders.

### Capability Sequence (Revenue-Maximizing, Capital-Minimizing)

```
Month 0–2:     FDM Core + Free Color Validation
Month 3–4:     AMS 2 Pro Multi-Color ($286)
Month 4–5:     Laser Outsource Validation ($100–150)
Month 5–6:     Laser Equipment ($1,899–2,099)
Month 6–9:     Resin Specialty Products ($574)
Month 10–12:   FDM Farm Expansion (2nd printer at $399)
Month 12+:     CNC (defer unless triggered)
```

Total committed capex through Month 9 (if all triggers met): $2,759–2,959
FDM expansion (Month 10–12) adds: $399
Grand total through Month 12: $3,158–$3,358

---

## Section 2: Trigger Conditions by Capability

### Trigger 1: AMS 2 Pro Multi-Color (Month 3 target, $286)

**Entry condition:** Any of the following:
- 25+ custom color-coded orders in a single month using the sequential-batch method
- Color-coded Etsy listings showing >20% higher conversion rate than standard listings
- Customer reviews specifically mentioning color-coding as a purchase motivator

**What it unlocks:**
- Unattended multi-color production (overnight batch runs)
- 4-color simultaneous capability (USB-C blue, power red, audio green, HDMI orange)
- Color-coded 5-pack and 12-pack SKUs as distinct Etsy listings

**Do not buy if:** Month 1–2 color tests show no measurable conversion premium over standard clips. This is a data-driven trigger, not a calendar trigger.

**Confidence that trigger will be met:** High. The desk-setup community actively values color-coded organization, and ModRun's parametric design makes color variants trivial to implement. The risk is low.

---

### Trigger 2: Laser Equipment (Month 4–6 target, $1,899–$2,099)

**Prerequisite:** 30-50 outsourced custom engraved orders in Month 2–3 (validation phase, $100–150 spend)

**Entry condition:** Either:
- Custom engraved order rate exceeds 40 units/month, OR
- Outsourced turnaround time (3–10 days from job shop) is causing customer complaints or missed orders

**Equipment decision within laser:**
- If current printer is the throughput bottleneck AND laser is also needed: buy Bambu H2D Laser Combo 40W (~$2,499–2,699) — gets you both a second printer and laser capability
- If printer throughput is not constrained: buy xTool S1 40W ($1,899–2,099) — more capable as a standalone laser, slightly lower cost

**What it unlocks:**
- Same-day engrave + ship on personalized orders
- Acrylic zone labels, wood veneer badges, desk nameplates (new product lines, not just upgrades)
- Potential $800–2,500/month additional revenue from laser-specific products

**Do not buy if:** Outsource validation (Month 2–3) shows custom engraved clips do not convert at meaningful premium. Return rate from the $100–150 validation must show clear positive signal before committing $1,900+.

---

### Trigger 3: Resin Specialty Products (Month 6–9 target, $574)

**Entry condition:**
- A specific resin product has been identified with validated price point and demand (transparent cable covers, precision organizer pieces, or miniatures if applicable)
- FDM line generating $1,000+/month (operations are stable enough to manage parallel learning curve)
- Workspace has adequate ventilation (resin fumes require airflow)

**Equipment:** Elegoo Saturn 4 Ultra 16K ($499) + Mercury Plus wash/cure station ($75) = $574 total

**What it unlocks:**
- Transparent cable channel covers (no FDM equivalent)
- Precision snap-fit organizers (sub-0.1mm tolerance)
- High-detail decorative accessories
- Potential $500–1,500/month from resin-specific products

**Do not buy if:** No specific resin product has been identified with validated demand. "Resin might be useful" is not a trigger — "I have 3 customers asking for transparent cable covers" is a trigger. The $574 capital risk is low enough that an exploratory purchase is arguably acceptable, but the post-processing labor overhead means an unused resin printer imposes ongoing time cost even when idle (cleaning, resin shelf life, FEP film conditioning).

---

### Trigger 4: Second FDM Printer (Month 10–12, $399–549 for P1S)

**Entry condition:**
- Monthly production volume consistently requires more than 18–20 printer-hours/day for 2+ consecutive weeks
- Demand backlog is measurably limiting revenue (orders placed but unable to fulfill in <7 days)
- Monthly revenue exceeds $2,000 (validating that capacity addition generates return)

**Equipment:** Bambu P1S ($399 current price) — identical to existing printer, enabling shared tooling/filament/profiles.

**Interaction with multi-manufacturing:** A second P1S can run single-color FDM while the first P1S runs AMS multi-color. This is the recommended configuration:
- Printer 1 (with AMS 2 Pro): multi-color jobs, custom color-coded orders
- Printer 2 (standalone P1S): high-volume single-color production batches

Or alternatively:
- Printer 1 retains AMS for multi-color
- The H2D (if purchased instead of xTool S1 for laser) serves as both the laser engraver and a second printer for large parts (rails, desk accessories requiring the H2D's 350×320mm bed)

---

### Trigger 5: CNC (Month 12+, $2,249–3,300 if warranted)

**Entry condition (all three required):**
1. A specific CNC product has been validated at 100+ units/month
2. JLCCNC/Protolabs lead time is causing lost orders or customer dissatisfaction
3. Monthly CNC-required-part revenue exceeds $2,000 consistently

If all three conditions are not met by Month 12: defer CNC indefinitely. Continue outsourcing.

---

## Section 3: Monthly Milestones

### Months 0–2: Foundation (FDM Core)

**Objective:** Test print confirmation, first Etsy sales, production workflow validation.

**Manufacturing:** Single-color FDM only (Bambu P1S, PLA+)
- Weeks 1–2: Test print pass/fail → if pass, proceed to production
- Weeks 2–4: First 5–10 Etsy orders fulfilled; production workflow documented
- Month 2: 20–40 units/month production pace established

**Multi-manufacturing prep actions (no spend):**
- Design color stripe variant of ModRun clip in Bambu Studio (1 hour)
- List one color-coded clip variant using sequential-batch method; measure conversion
- Contact local makerspace or search Thumbtack/Craigslist for laser engraving service; get quote for 15 custom-engraved clips

**Revenue target:** $200–800 (early adoption phase, limited reviews)

---

### Month 3: AMS 2 Pro Acquisition (if triggered)

**Trigger check:** Has sequential-batch color validation shown demand?
- If yes: order AMS 2 Pro ($286)
- If no: continue sequential batch; re-evaluate Month 4

**Setup tasks (AMS 2 Pro, ~2 hours):**
1. Connect AMS 2 Pro to P1S via supplied interface board
2. Load 4 colors: black, white, signal blue, power red (start with 2 accents)
3. Configure Bambu Studio for multi-color slicing on clip design
4. Run 2–3 test plates to calibrate flush volumes and purge-into-infill settings
5. Create 4 new Etsy listings: color-coded clip 5-pack (blue), (red), (green), assorted

**Revenue target Month 3:** $500–1,500

---

### Month 4: Laser Outsource Validation

**Spend:** $100–150 at local makerspace or online laser service

**Execution:**
1. Create LightBurn-compatible SVG file with cable function labels
2. Outsource engraving of 20–30 clips (bring finished FDM clips to makerspace, or ship to online service)
3. List 3 engraved clip sets on Etsy (5-clip labeled set at $38–45)
4. Measure: order rate, any customer messages, conversion vs. standard listings

**Decision gate at Month 5:** If 10+ orders received → proceed to laser equipment purchase. If <5 orders → continue FDM and AMS, hold on laser for 60 days.

**Revenue target Month 4:** $800–2,000

---

### Month 5: Laser Equipment Acquisition (if triggered)

**Equipment decision:**
- If printer capacity is not yet constrained: xTool S1 40W ($1,899–$2,099)
- If printer capacity is beginning to constrain output AND laser is validated: Bambu H2D 40W Laser Combo (~$2,499–2,699)

**Setup tasks (~10 hours over first week):**
1. Assemble and test laser on scrap PLA/wood
2. Install LightBurn ($60 license if not already purchased)
3. Create production templates: clip function label, clip initials, acrylic zone label
4. Calibrate power/speed settings on PLA surface and 3mm acrylic
5. Establish ventilation setup (4" duct to window)

**First production week:** Engrave backlog from Etsy validation orders; photograph finished products for listing updates.

**New Etsy listings to create:**
- Custom engraved clip 12-pack with function labels ($42–48)
- Acrylic zone label set ($16–22)
- Wood veneer cable clip 5-pack ($28–35)
- Personalized desk nameplate ($18–28)

**Revenue target Month 5:** $1,200–2,500

---

### Months 6–8: Resin Evaluation and Product Development

**If resin trigger conditions are met ($574 spend):**

Month 6: Order Elegoo Saturn 4 Ultra 16K + Mercury Plus. Allocate 2 weeks to calibration and first print validation (not sold publicly yet). Learn:
- Support placement for the specific product being developed
- Resin handling and workspace safety protocol
- Post-processing workflow (wash, cure, inspection cycle)

Month 7: Launch 1–2 resin SKUs. Target:
- Transparent cable channel cover for ModRun rail (premium upgrade product)
- Precision desk organizer piece (small tray, sub-0.1mm fit to existing clip system)

Month 8: Evaluate resin demand. If resin products generating $300+/month: continue development. If under $200/month: hold at current resin SKUs, do not expand.

**If resin trigger not met:** Skip resin entirely in Month 6–8. Use this time to deepen laser product line (expand from 4 listings to 8–10) and build FDM production efficiency.

**Revenue target Months 6–8:** $2,000–4,000/month (FDM + AMS + laser contributions combined)

---

### Months 9–12: Scaling and Integration

**Revenue milestone evaluation:**
- Month 9: If total revenue $3,000+/month → evaluate second printer ($399 P1S)
- Month 10: If printer utilization exceeds 80% consistently → order second printer
- Month 11: Configure 2-printer workflow (multi-color + high-volume single-color lanes)
- Month 12: Full 12-month capability review and Year 2 planning

**Potential product integrations emerging by Month 12:**
- Laser-engraved clips + resin transparent covers as a premium bundle ($55–75)
- FDM rail + acrylic laser-cut side panels as a design upgrade kit ($38–55)
- Personalized gift sets combining FDM + laser + branded packaging ($45–75 per set, giftable holiday product)

**Revenue target Month 12:** $4,000–7,000/month (3-capability operation, 2 printers)

---

## Section 4: Capital Budget Allocation — 12-Month

### Base Scenario (All Triggers Met)

| Item | Month | Cost | Cumulative |
|---|---|---|---|
| AMS 2 Pro (multi-color) | Month 3 | $286 | $286 |
| Laser outsource validation | Month 4 | $150 | $436 |
| xTool S1 40W + LightBurn | Month 5 | $1,959 | $2,395 |
| Elegoo Saturn 4 Ultra + wash/cure | Month 6 | $574 | $2,969 |
| Second Bambu P1S | Month 10 | $399 | $3,368 |
| LightBurn license renewal + consumables | Monthly | ~$30/mo avg | +$360 |
| Resin consumables (IPA, FEP, resin) | Monthly (Mo 6+) | ~$50/mo avg | +$350 |
| **Total 12-month capex + consumables** | | | **~$4,078** |

### Conservative Scenario (Laser Only, No Resin, No Second Printer)

| Item | Month | Cost | Cumulative |
|---|---|---|---|
| AMS 2 Pro | Month 3 | $286 | $286 |
| Laser outsource validation | Month 4 | $150 | $436 |
| xTool S1 40W + LightBurn | Month 5 | $1,959 | $2,395 |
| Consumables (filament, packaging) | Monthly | ~$20/mo | +$240 |
| **Total** | | | **~$2,635** |

At $2,635 total capex, the break-even against a $2,000–3,000/month revenue trajectory is approximately 1–2 months at full production.

### H2D Substitution Scenario (Replaces Both xTool S1 and Second Printer)

If at Month 5 both laser AND additional printer capacity are needed:

| Item | Month | Cost | Cumulative |
|---|---|---|---|
| AMS 2 Pro | Month 3 | $286 | $286 |
| Laser outsource validation | Month 4 | $150 | $436 |
| Bambu H2D 40W Laser Combo | Month 5 | $2,699 | $3,135 |
| Elegoo Saturn 4 Ultra (if triggered) | Month 7 | $574 | $3,709 |
| **Total** | | | **~$3,709 + consumables** |

The H2D scenario costs $1,074 more than the conservative scenario but delivers: a second high-volume printer (350×320mm bed for rails), 40W laser, and AMS capability — all in one machine footprint. Appropriate if the operator's physical workspace is space-constrained.

---

## Section 5: Supplier Ecosystem Planning

### FDM Filament Suppliers (Ongoing)

- **eSUN PLA+** (primary): $15–18/kg from Amazon; reliable at 220–225°C; available in 30+ colors
- **Bambu Lab filament** (AMS multi-color): $19–25/kg; RFID auto-configuration; reduced friction in multi-color workflow
- **Polymaker PolyTerra PLA** (eco premium option): $18–22/kg; matte finish; strong visual appeal in desk-setup photography
- Bulk purchasing (10kg+) reduces per-kg cost by 10–15%; trigger bulk orders once monthly filament spend exceeds $100/month

### Laser Materials

- **Acrylic sheets:** Amazon or local plastics supplier. Black 3mm acrylic (A4/letter sheet): $8–15. Clear 3mm: $10–18. Smoked gray: $12–20. Stock 10–15 sheets per color at all times once laser is operational.
- **Baltic birch plywood (3mm):** Local hardwood supplier or Amazon. $15–25 for A3 sheet. Higher quality than "craft plywood" from big-box stores — cleaner edges, no voids, consistent thickness.
- **Wood veneer sheets:** Amazon, Woodcraft. Cherry or maple veneer at $8–15 per A4 sheet. Yields 40–60 cable clip badges per sheet.

### Resin Materials (if resin path is taken)

- **Elegoo ABS-Like 3.0 Pro:** Elegoo direct store or Amazon, $25–35/kg. Keep 2–3 bottles in rotation.
- **Siraya Tech Blu (tough resin):** Siraya Tech direct or Amazon, $28–40/kg. For functional parts.
- **IPA (99% isopropyl):** Hardware store or Amazon, $30–45/gallon. Stock 2 gallons minimum.
- **FEP replacement film:** Elegoo direct store, $12–20 per sheet. Stock 3 sheets.

### Outsourcing Partners (CNC and Overflow)

- **JLCCNC:** jlccnc.com — CNC aluminum/acetal parts, 3–5 day production + shipping. Account setup before needed; get first quote on any precision part.
- **Protolabs Network (Hubs):** hubs.com — US-based shops, instant quote. Premium pricing but domestic lead time. Use for urgent or first-prototype orders.
- **Local laser engraving shop:** Identify one local makerspace or laser shop within 20 miles. Used for Month 4 validation and as overflow capacity during peak seasons.
- **Local machine shop:** Optional; use only if JLCCNC lead times are causing order fulfillment problems.

---

## Section 6: Risk Mitigation

### Risk 1: Test Print Fails or ModRun Demand Is Lower Than Projected

**Scenario:** ModRun clips don't sell at target prices, or the test print requires 2–3 iterations before production-ready.

**Impact on multi-manufacturing roadmap:** Delays every downstream trigger. All capability additions are demand-gated — if ModRun demand isn't validated, no additional manufacturing investment is justified.

**Response:**
- Do not buy AMS 2 Pro or laser until core FDM business generates $500+/month
- Use the delay period to design Phase 3 product variants (desk accessories, organizer ecosystem) that can launch alongside or instead of ModRun if clip demand is insufficient
- The Bambu P1S retains $250–350 resale value if the business is abandoned — capital loss is bounded

### Risk 2: Multi-Color Demand Does Not Materialize

**Scenario:** Color-coded clips don't command a meaningful price premium; the AMS 2 Pro sits largely idle.

**Impact:** $286 loss (the AMS 2 Pro has limited resale market); ongoing slight workflow complexity from managing multi-color slicer profiles.

**Response:** Revert to single-color production; use the AMS 2 Pro for filament backup (its automatic spool-switching feature is useful for unattended single-color printing regardless). Net loss: minimal.

### Risk 3: Laser Acquisition Precedes Validated Demand

**Scenario:** Operator buys xTool S1 based on enthusiasm rather than validation data; laser products don't sell at target volume.

**Impact:** $1,899–$2,099 capital commitment without commensurate revenue.

**Response:** This is why the outsource validation step (Month 4, $100–150) exists. Do not buy laser before outsource validation shows >10 orders. If laser doesn't justify purchase, the machine has $1,200–1,500 resale value in the secondary market (laser engravers hold value well among hobbyists/Etsy sellers).

**Mitigation rule:** The outsource step is mandatory, not optional. It is insurance against an $1,800+ mistake.

### Risk 4: Resin Post-Processing Labor Exceeds Capacity

**Scenario:** Resin products sell well but post-processing (wash, cure, support removal) takes 4+ hours/week, cutting into FDM and laser production time.

**Response:** 
- Cap resin production at 40 units/month until throughput is validated
- Stagger wash/cure cycles (wash during print, cure during harvest — automate scheduling)
- If resin products generate $600+/month and post-processing time is the bottleneck: add a second Mercury Plus wash station ($75) to run parallel batches; this reduces time overhead by ~30%

### Risk 5: Demand Grows Faster Than Capabilities Can Scale

**Scenario:** The positive failure mode: ModRun demand hits $5,000+/month before multi-manufacturing capabilities are operational.

**Response:** This is not a risk — it is the best case. Prioritize FDM capacity addition first (second printer at $399) over any specialty manufacturing. Revenue is the priority; capability diversification is secondary to servicing existing demand.

At $5,000/month demand with a single printer at capacity: buy the second P1S first ($399), then the third if needed ($399), before spending $1,899 on a laser. More FDM printing capacity multiplies the proven revenue generator; laser adds a new capability with uncertain incremental demand.

---

## Section 7: Integration Timeline — How New Capabilities Work Together

### Month 5 State (FDM + AMS + Laser): First Integration Opportunities

**Product: "Complete Setup Kit"**
- 10 color-coded FDM clips (AMS, 2 colors)
- 1 set of 4 laser-engraved acrylic zone labels
- Bundled in kraft box with foam insert
- Price: $52–65; COGS: ~$18–22; gross margin: 66–72%

This is the first product that could not exist without two capabilities working together. List it separately from components — bundles have higher perceived value than the sum of parts.

### Month 9 State (FDM + AMS + Laser + Resin): Premium Tier Emerges

**Product: "Premium Cable System" (transparent + color-coded)**
- 8 color-coded FDM clips (AMS)
- 2 transparent resin cable channel covers (Saturn 4 Ultra)
- 4 laser-engraved acrylic zone labels
- Custom-engraved wood nameplate
- Price: $85–110; COGS: ~$28–35; gross margin: 68–74%

This product has no direct FDM-only equivalent on Etsy. It combines material types (PLA, resin, acrylic, wood) in a single desk organization system. The differentiation is structural — competitors cannot replicate it without the same 3-technology stack.

### Seasonal / Holiday Integration (Month 10–12)

**Product: "Personalized Desk Gift Set"**
- 5-clip custom-engraved set (customer's name, color of choice)
- Laser-engraved wood nameplate
- Packaged as a gift with branded tissue paper
- Designed for Q4 holiday season (October–December)
- Price: $45–65 per set; 70%+ margin

Holiday desk gifts are a proven Etsy category. A desk setup gift with personalized components (laser name, custom clip colors) targets the gift-giver looking for something more original than a generic organizer. The multi-manufacturing stack enables a differentiated product that appears "premium made" — the kind of item a person is proud to give or receive.

---

## Quick Reference: Capability Decision Matrix

| Capability | Cost | Month Target | Trigger Condition | Skip Condition |
|---|---|---|---|---|
| Sequential batch color | $0 | Month 1 | Always | Never |
| AMS 2 Pro | $286 | Month 3 | 25+ color orders/month | <10 orders; no conversion lift |
| Laser outsource validation | $100–150 | Month 4 | Always (before buying laser) | Never |
| xTool S1 40W or H2D | $1,899–$2,699 | Month 5 | 40+ engraved orders/month | Validation fails |
| Elegoo Saturn 4 Ultra | $574 | Month 6 | Specific product ID'd | No clear resin product |
| Second P1S | $399 | Month 10 | Revenue >$2K + capacity constrained | Demand not there |
| CNC equipment | $2,249+ | Month 12+ | 100+ CNC units/month + lead time issues | Default: outsource |
