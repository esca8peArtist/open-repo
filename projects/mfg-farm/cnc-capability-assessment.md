---
title: CNC Capability Assessment — Deferral Criteria and Outsourcing Decision Rules
project: mfg-farm
created: 2026-05-05
status: production-ready
session: multi-manufacturing-roadmap
depends_on: cnc-capabilities-analysis.md, ITEM18_ADJACENT_MANUFACTURING_ECONOMICS.md
confidence: high — deepens cnc-capabilities-analysis.md (Session 549) with updated 2026 pricing and specific outsourcing thresholds
---

# CNC Capability Assessment

**Lead finding**: CNC machining remains unjustified for ModRun's current and near-term product line. The core analysis from Session 549 (cnc-capabilities-analysis.md) stands: FDM is technically adequate for all cable management products at the price points ModRun is targeting, and the CNC break-even math strongly favors adding FDM printers over adding a CNC machine at any volume below 1,000 units/month of a precision-required product. The correct approach is selective outsourcing — use Protolabs, JLCCNC, or a local machine shop for specific precision components as needed, without owning a machine. This document adds: (1) specific outsourcing decision rules, (2) updated Shapeoko 5.1 Pro pricing, (3) 2–3 genuinely viable CNC-first product ideas, and (4) a clear "Month 12+ or never" decision framework.

---

## Section 1: Product Opportunities — Where CNC Is the Right Tool

### 1.1 Products FDM Cannot Serve (Technically)

**Heat-set insert bores to precise tolerances:** As established in cnc-capabilities-analysis.md, heat-set inserts (brass M4/M6 inserts pressed in with a soldering iron) replace most threaded-connection CNC applications. Cost: $0.12–0.25 per insert. This is not a CNC product opportunity — it eliminates the need for CNC.

**Aluminum desk mount rails:** Premium desk hardware where aluminum is required for rigidity (not plastic). CNC-milled aluminum rail channel that ModRun cable clips mount into, positioned as a $80–150 desk integration product for standing desk enthusiasts. This is a genuine CNC product opportunity — but it targets a different customer segment (commercial-grade, not consumer DIY) and requires aluminum processing capability. The Shapeoko 5.1 Pro can mill aluminum but requires slow feed rates ($0.05–0.10mm/pass depth in 6061 aluminum), specialized workholding, and cutting fluid. Not a beginner's product.

**Precision jigs and fixtures for production:** CNC-milled acrylic or HDPE fixtures for holding cables or clips during photography, packaging, or quality inspection. These are production aids, not sellable products. Could be outsourced for $50–100 per jig rather than machined in-house.

**Custom tooling for post-processing:** CNC-cut MDF or plywood templates for trimming or punching cable sleeves. Niche use case; outsourced easily.

### 1.2 CNC-First Product Ideas With Positive Economic Case

The critical filter: does CNC enable a product that (a) exists in a verified market, (b) commands price high enough to absorb higher COGS, and (c) is not adequately served by FDM or laser?

**Product Idea 1: Premium Aluminum Cable Rail System ($149–200/set)**

A 2-rail desk cable management system where the structural rails are CNC-milled 6061 aluminum extrusions with precision-routed channels for cable routing and custom T-slot mounting. The existing ModRun FDM clips could clip into these aluminum rails — FDM and CNC working together.

Target customer: professional creator, streaming setup, home studio, standing desk enthusiast. Price expectation: $149–200 for a 2-rail + 12-clip system.

**COGS analysis (outsourced CNC):**
- CNC-milled aluminum rail (outsourced, 200mm × 30mm × 15mm, JLCCNC quote): $12–18/piece at 10 qty, $8–12/piece at 50 qty
- 2 rails per set: $16–36
- 12 FDM clips: $13.80
- Hardware (M4 bolts, rubber feet): $1.50
- Packaging: $1.50
- Total COGS: $33–53 depending on rail volume

At $149–200 retail, this yields 65–78% gross margin — competitive with FDM-only products and justifiable given the premium positioning.

**The catch:** This product requires:
- CNC vendor relationship and lead time management (3–5 days JLCCNC, 1–2 weeks domestic)
- Aluminum sourcing and design for CNC (different tolerances and design rules from FDM)
- Higher product photography investment to justify the $149 price point
- Customer acceptance of aluminum + plastic hybrid — validate before committing to 50+ unit inventory

This product makes sense as a Phase 3–4 addition, not Phase 1–2. If ModRun's FDM line is generating $3,000+/month, a premium aluminum variant justifies the development investment.

**Product Idea 2: CNC-Cut Acrylic Desk Panel System ($45–85)**

Laser cutting and CNC routing are competitive technologies for acrylic panels. However, for panels thicker than 6mm (acrylic or polycarbonate) and panels requiring precise 3D profile routing (not just flat cutting), CNC is more capable than laser. A CNC-routed 10mm acrylic desk panel with cable routing channels and precisely machined clip attachment points is a product that laser cannot produce cleanly.

Target customer: premium desk enthusiast, commercial buyer wanting a branded desk panel.

**Economic analysis:**
- Outsourced CNC for 10mm acrylic panel (200×120mm): $15–25/piece at 10–20 quantity (Protolabs Network / local shop)
- Retail price: $45–65 per panel
- Gross margin: 61–72%

Viable at low volume; requires outsourcing (not own CNC equipment). This product is achievable without owning a CNC machine — file design, outsource to Protolabs or local shop, markup and sell.

**Product Idea 3: Engraved + CNC-Profiled Business Card Holder / Desk Accessory Set ($35–75)**

A precision desk accessory set where FDM provides the structural body, CNC provides precision-milled wood or aluminum inserts for visual accents, and laser provides surface engraving. Three manufacturing modes in one product — a premium "made in-house" narrative that commands $35–75 for a business card holder or pen organizer.

**Economic analysis:**
- FDM body: $1.50 (larger organizer vs. clip)
- CNC-milled wood insert (outsourced, birch, 80×30mm): $3–5 at 20 quantity
- Laser engraving on insert: $0.05 (2-minute operation)
- Packaging: $0.80
- Total COGS: ~$5.35–7.35

At $45–55 retail: 87–88% gross margin.

The limiting factor here is not COGS — it is product development time and customer acquisition cost in the desk accessory segment, which is crowded. This product competes with hundreds of established Etsy sellers. It is viable but is a Phase 4 product (Month 18+).

---

## Section 2: Equipment Analysis — Is Hobbyist CNC Viable?

### 2.1 Current Desktop CNC Market (2026)

**Shapeoko 5.1 Pro** (Carbide 3D): Starting at $3,300. Updated from the Shapeoko 5 Pro (previously $1,990). Uses hardened linear rails and ballscrews for increased rigidity over the belt-drive Shapeoko 4. Machines wood, plastics, and soft aluminum. Work area up to 4×4 feet in largest configuration.

**Onefinity Woodworker:** $1,699–2,299. Ballscrew-driven; better rigidity than the older Shapeoko belt-drive design. Primarily marketed to woodworkers; capable of light aluminum with appropriate speeds.

**Nomad 3 Pro** (Carbide 3D, desktop size): $2,249. 203×203×76mm work envelope. Fully enclosed desktop machine designed for precision work in aluminum, acetal, and engineering plastics. Better choice than Shapeoko for small precision parts due to rigidity and enclosure.

**Tormach xsTECH:** $4,195. Purpose-built for small metal parts. Overkill for ModRun's use case; relevant only if aluminum production runs are the primary application.

### 2.2 Critical Limitations of Hobbyist CNC for Production Use

**Learning curve is steeper than reported:** Marketing materials from Carbide 3D and Onefinity suggest a beginner can start machining within a day. The reality for production-quality parts:
- CAM software (Fusion 360, VCarve) proficiency: 10–20 hours minimum
- Workholding design (the most failure-prone step): 5–10 hours to learn reliably
- Material speeds/feeds calibration for each material: 2–5 hours per new material
- First production-quality job setup: 4–8 hours from file to acceptable part

Total investment to reach consistent production quality: 30–50 hours over 3–4 weeks. Compared to FDM (1–3 hours to produce quality parts) and laser (2–4 hours), CNC requires a substantially higher setup commitment.

**Noise and chips:** CNC machining of aluminum and hard plastics generates metal chips, cutting fluid mist, and 70–90 dB of cutting noise. In a home workshop, this requires:
- Fully enclosed machine or dedicated noise-isolated space
- Chip containment and cleanup protocol
- Coolant/cutting fluid storage and disposal

FDM and laser generate noise levels (35–55 dB) compatible with residential living. CNC at full operation is not.

**Tool wear and consumables:** End mills for aluminum: $15–40 each, lasting 30–200 passes depending on depth of cut, material, and whether coolant is used. Spoilboard replacement (the sacrificial MDF bed): $20–40 every 3–6 months for regular use. Annual consumable budget: $500–1,500 for a lightly-used desktop CNC.

### 2.3 The Outsourcing Alternative — When It's Better

For low-to-medium volume (under 100 units/month of any CNC-required part), outsourcing to JLCCNC, Protolabs Network, or a local machine shop is economically superior to owning equipment:

**JLCCNC (online CNC service):** Upload CAD file, instant quote, 3–5 day turnaround. Pricing for 6061 aluminum small parts (50×50×15mm, moderate complexity): approximately $20–45 per piece at 1–10 quantity, dropping to $8–15 at 50 quantity. Shipping from China: 7–14 days (standard) or 3–5 days (DHL express at additional cost).

**Protolabs Network (formerly Hubs):** US-based partner shops with 3–7 day turnaround. Pricing is approximately 20–40% higher than JLCCNC but eliminates tariff/import uncertainty and provides domestic lead times. Best for prototypes and low-volume critical components.

**Local machine shop:** Variable pricing; typically $80–150/hour shop rate. For a simple part requiring 30 minutes of machining: $40–75. For batch of 10 identical parts: setup (1 hour) + machining (3 hours at 18 minutes/part) = ~$320–600 for 10 parts = $32–60/piece. Competitive with JLCCNC for small batches; domestic lead time advantage.

---

## Section 3: Cost Comparison — Own vs. Outsource

**Basis: 10mm aluminum part, 50×50mm, 4 features, ±0.1mm tolerance**

| Volume/Month | Own (Shapeoko 5.1 Pro, $3,300 amortized 24mo) | JLCCNC Outsource | Local Shop Outsource |
|---|---|---|---|
| 5 units | $149/unit (capex: $137.50 + $12 material + machining) | $35–45/unit | $60–75/unit |
| 20 units | $40/unit | $25–35/unit | $40–55/unit |
| 50 units | $21/unit | $12–18/unit | $28–40/unit |
| 100 units | $14/unit | $8–12/unit | $20–30/unit |
| 200 units | $10/unit (capex amortized; consumables remain) | $6–10/unit | $15–22/unit |
| 300 units | $8.50/unit | $5–8/unit | $12–18/unit |

The table above shows that outsourcing is almost always cheaper at volumes below 200 units/month when the full Shapeoko capex and operator time cost are factored in. Even at 300 units/month, JLCCNC pricing is competitive or cheaper — and JLCCNC does not require the operator's time.

**Hidden cost of ownership not captured above:** Operator setup time per job (20–45 minutes), maintenance ($500–1,500/year), noise management, chip cleanup (30–60 minutes per session). At $25/hour imputed operator time, adding 1 hour per production session to a 100-unit/month production schedule adds $25/month in direct labor plus setup time cost — not trivial.

**Conclusion:** Outsource CNC when volume is under 300 units/month of any single CNC-required part. This is the overwhelming majority of scenarios ModRun will encounter in the first 24 months.

---

## Section 4: Outsourcing Decision Rule

**The decision rule for CNC in the mfg-farm:**

> Outsource CNC when: (1) monthly volume is below 300 units/month of the specific CNC part, OR (2) the per-unit margin gain from in-house CNC vs. outsourced CNC is less than 15%, OR (3) the product line is less than 6 months old (insufficient demand validation for capital commitment).

**All three conditions likely apply throughout the first 18 months of ModRun's operation.** Do not buy a CNC machine during this period unless a specific high-volume product emerges that requires it.

**Secondary rule:** If JLCCNC or Protolabs Network can supply the needed part with acceptable lead times (5–14 days), in-house CNC provides no strategic advantage in product quality or customer lead time that justifies the $3,300 equipment cost.

**The exception that would trigger CNC acquisition:**
A product line generating $2,000+/month in revenue that specifically requires:
- Aluminum or precision acetal parts at 200+ units/month
- Tolerances tighter than outsourcing partner can consistently deliver (±0.1mm is achievable via outsourcing; ±0.05mm may require in-house for batch consistency)
- Lead time requirements incompatible with JLCCNC's 5–14 day cycle (e.g., Etsy personalized orders requiring 3-day fulfillment of CNC parts)

The third condition (lead time) is the most likely real-world trigger. If a high-demand CNC product emerges where customers expect fast fulfillment, in-house CNC becomes necessary regardless of per-unit economics.

---

## Section 5: Timeline — Month 12+ or Never

CNC acquisition should not be planned in the Month 1–12 roadmap. The conditions that would justify acquisition are:

**Month 12 re-evaluation gate:**
- Has any CNC product demand been validated? (Sell first via outsourced CNC; validate price and conversion rate)
- Is JLCCNC/local shop lead time causing lost orders?
- Is monthly CNC-part revenue above $2,000?

If all three are "yes" at Month 12: acquire Nomad 3 Pro ($2,249) for small precision parts, or Shapeoko 5.1 Pro ($3,300) for larger format. If any of the three is "no": defer for another 6 months.

**The "never" scenario:**

If ModRun's revenue at Month 12 comes primarily from FDM cable management + laser engraving, with CNC products representing less than 10% of revenue, CNC acquisition may genuinely never make sense. A business that does $5,000/month from FDM + laser does not need CNC. Adding it would add complexity, noise, and capex without proportional revenue gain.

The most likely outcome: CNC remains an outsourced dependency used selectively for specific components (aluminum rail segments, precision acetal jigs) at low volume, with the outsource relationship to JLCCNC or local machine shop fully sufficient.

---

## Summary Decision Matrix

| Scenario | Recommended Action |
|---|---|
| Month 1–6, no validated CNC product demand | No action — pure FDM + planning |
| Month 1–6, customer requests aluminum hardware | Outsource single batch to JLCCNC; test at 10–20 units |
| Month 6–12, aluminum product selling 20–50/month | Continue outsourcing; monitor lead time |
| Month 12+, aluminum product >100/month + lead time pain | Re-evaluate Nomad 3 Pro ($2,249) acquisition |
| Month 12+, precision acetal parts >200/month | Consider Shapeoko 5.1 Pro ($3,300) |
| Any time, only need laser surface engraving | Do NOT buy CNC — buy xTool S1 or H2D instead |
| Any time, need threaded metal connections | Buy heat-set inserts ($0.15/each) — NOT a CNC purchase |
