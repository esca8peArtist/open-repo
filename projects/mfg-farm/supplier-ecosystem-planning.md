---
title: Supplier Ecosystem Planning — Equipment Acquisition, Outsourcing Strategy, and Scaling Pathway
project: mfg-farm
created: 2026-05-06
status: production-ready
session: Item-16-multi-manufacturing-capability-roadmap
depends_on: multi-color-fdm-strategy.md, resin-printing-viability.md, laser-cutting-capability-assessment.md, cnc-capability-assessment.md, 12-month-multimanufacturing-roadmap.md, production-scaling-research.md
confidence: high — based on verified vendor pricing (May 2026), Clicklease/Affirm financing program terms, and JLCCNC/Protolabs outsourcing benchmarks
---

# Supplier Ecosystem Planning

**Lead finding**: The optimal equipment strategy for the first 18 months is own the FDM printers, own the laser (once validated), outsource the resin printer decision until Month 6, and outsource CNC entirely until 300+ units/month of a CNC-specific product. The financing ecosystem (Affirm, Clicklease) makes it possible to stage all capital additions within monthly cash flow — but using financing for equipment before demand is validated is precisely the wrong move. The stronger discipline is: validate with outsourcing, buy only when the revenue trigger is met, and use financing only when the equipment purchase would otherwise interrupt working capital. This document provides the vendor relationships, pricing, facility requirements, and scaling pathway to execute that discipline.

---

## Section 1: Equipment Ownership vs. Outsourcing Decision by Technology

### The Core Principle

Each manufacturing technology has a different ownership equation based on: (1) how much operator time ownership saves vs. outsourcing, (2) how quickly turnaround time matters for Etsy order fulfillment, and (3) whether the economics of outsourcing are competitive at the expected volume.

| Technology | Ownership Verdict | Reason |
|---|---|---|
| FDM (Bambu P1S / P2S) | Own from Day 1 | Core production; no outsource equivalent for custom parametric parts |
| Multi-color FDM (AMS 2 Pro) | Own at Month 3 trigger | $286 incremental; enables unattended overnight production |
| Laser engraving | Own at Month 4–5 trigger | Etsy personalization requires same-day turnaround; job shops incompatible |
| Resin printing | Own at Month 6 trigger, or defer | Low capital risk ($574); but post-processing labor is the real cost |
| CNC machining | Outsource indefinitely | Per-unit economics favor JLCCNC until 300+ units/month |

---

## Section 2: FDM Printer Ecosystem — Vendor Directory

### 2.1 New Equipment Sources

**Bambu Lab US Direct Store** (us.store.bambulab.com)
- P1S standard: $399
- P1S Combo (with AMS 2 Pro): $549
- P2S standard: $549
- P2S Combo (with AMS 2 Pro): $799
- AMS 2 Pro add-on (standalone): $286
- Warranty: 1 year, US-based support
- Financing: Affirm available at checkout (split into 4 payments or monthly)
- Note: Bambu's direct store typically has the best bundle pricing; Micro Center matches pricing and allows in-person pickup

**Micro Center** (microcenter.com)
- Carries P1S, P2S, H2D, and AMS 2 Pro at comparable pricing to direct store
- Advantage: in-person pickup same day; no shipping wait
- Useful for time-sensitive additions (e.g., AMS 2 Pro needed before a peak order period)

**B&H Photo** (bhphotovideo.com)
- Stocks AMS 2 Pro unit, P1S, P2S
- No-sales-tax option for most states; educational pricing not applicable here
- Reliable for standalone AMS 2 Pro units when Bambu direct is out of stock

### 2.2 Used/Refurbished Equipment

**Facebook Marketplace (local search)**
- P1S: $250–350 for well-maintained units (common; the P1S was widely purchased in 2024–2025)
- AMS 2 Pro: $180–230 (less common than P1S; inspecting cutter mechanism is critical before purchase)
- Timing: after Bambu product launches, earlier-gen hardware floods the used market; watch for P1S pricing drops following P2S adoption

**eBay**
- P1S: $280–370; AMS 2 Pro: $200–250
- Shipping risk on heavy precision equipment; prefer local pickup when possible

**r/3Dprinting and r/BambuLab (Reddit forums)**
- Direct seller listings; often better-condition equipment with more seller history than eBay
- Search "P1S for sale" + "AMS 2 Pro for sale" with location filter

**Risk on used AMS 2 Pro:** The buffer tube and cutter mechanism are the most failure-prone components. Before purchasing used, ask the seller for a video of the AMS loading and unloading filament cleanly through 2–3 cycles. Do not buy without this confirmation.

### 2.3 P1S vs. P2S Acquisition Decision

The P2S ($549 vs. P1S $399) is a meaningful upgrade for production use:
- Servo extruder (not stepper): 70% more extrusion force; better for abrasive and flexible filaments
- 5-inch color touchscreen: faster job management without a connected computer
- 1080p AI camera with NPU: better spaghetti detection, fewer wasted prints overnight
- Adaptive airflow: quieter enclosure management; more consistent chamber temps

**For the first printer (already owned, likely P1S):** No upgrade justification. The P1S is sufficient for all ModRun production requirements.

**For the second printer (Month 10–12 acquisition):** The $150 premium for the P2S over the P1S is worth paying at the second-printer stage — the servo extruder and improved AI detection reduce overnight failure rates, which matters when you're running two printers simultaneously and cannot monitor both constantly.

---

## Section 3: Laser Equipment Ecosystem

### 3.1 Primary Recommendation: xTool S1 40W

**xTool direct store** (xtool.com)
- S1 40W basic bundle: ~$1,299–$1,499 (on sale; MSRP varies by configuration)
- S1 40W with air assist + honeycomb bed: ~$1,899 (full production bundle)
- Note: xTool runs 15–20% discount events regularly; sign up for email alerts to time the purchase
- Financing: Affirm and Clicklease available (Clicklease lease-to-own, 24–60 month terms)

**Amazon** (B0CQ84BDTX — Rotary Bundle; B0CQ7ZW5KK — Basic Bundle)
- Pricing matches xTool direct with the advantage of Prime 2-day shipping and easier returns
- Useful if a discount event on Amazon is active

**LightBurn license** (lightburnsoftware.com)
- $60 one-time license for DSP/Galvo; the xTool S1 uses the gantry (diode) license at $40
- Required for production-grade job management; the included xTool Creative Space software is adequate for simple jobs but LightBurn's array/batch/overlay tools are essential for Etsy production workflows

**Total S1 40W acquisition cost:** $1,499–$1,899 (equipment) + $40 (LightBurn) + ~$20 (fixture/jig acrylic for holding clips) = **$1,559–$1,959 all-in**

### 3.2 Alternative: Bambu H2D Laser Full Combo 40W

**Pricing update (May 2026):** The H2D Laser Full Combo 40W is now priced at $3,199–$3,499 depending on retailer. This is significantly higher than was anticipated in earlier research ($2,499–$2,699). At this price point, the H2D Laser Combo is harder to justify as a "second printer + laser" consolidation:

- H2D Laser Full Combo 40W: $3,199–$3,499 (Dynamism, Bambu Lab direct, Polyfab3D)
- Equivalent: P2S Combo ($799) + xTool S1 40W ($1,899) = $2,698

The H2D delivers advantages (BirdsEye camera alignment ±0.3mm, 350×320mm print bed for larger parts, unified workflow) but at a $500–$800 premium over buying separate machines. At the current pricing, the separate-machine path is the better value unless workspace space constraints are severe.

**H2D sources:**
- Bambu Lab direct store: H2D Laser Full Combo 40W
- Dynamism (dynamism.com): typically in stock; authorized reseller; strong support reputation
- 3D Universe (shop3duniverse.com): US authorized reseller with good return policy

### 3.3 Laser Equipment Financing

xTool and laser equipment generally have robust financing options:
- **Affirm:** 0% APR (12 weeks, 4 payments) or 10–30% APR for longer terms. At $1,899: 4 × $474.75 with 0% APR if eligible. Does not require business credit history.
- **Clicklease:** Equipment lease-to-own, $500–$25,000 limit, 24–60 month terms. Monthly payment on $1,899 equipment at 36 months: approximately $65–$85/month depending on credit profile. Available through Abunda (shopabunda.com) for xTool.
- **Acquisition rule:** Do not finance laser equipment until the outsource validation (Month 4, $100–150) shows >10 orders in the validation window. Financing before demand validation converts a capital experiment into a debt obligation.

---

## Section 4: Resin Printer Ecosystem

### 4.1 Primary Recommendation: Elegoo Saturn 4 Ultra 16K

**Elegoo direct store** (us.elegoo.com)
- Saturn 4 Ultra 16K: $499 (confirmed May 2026)
- Mercury Plus V3 wash/cure station: ~$75
- Total all-in: $574

**Amazon** (B0DT8PV51T)
- Typically matches Elegoo direct pricing; Prime shipping advantage
- Check for bundle deals that include Mercury Plus at reduced combined price

**Elegoo filament and resin** (us.elegoo.com)
- ABS-Like 3.0 Pro resin: $25–35/bottle (1kg)
- Available in grey, black, white, clear, skin, and specialty colors
- Stock 2–3 bottles in primary production color + 1 clear

**Siraya Tech resins** (sirayatech.com)
- Blu (tough resin): $28–40/liter — primary recommendation for functional parts
- Tenacious (flexible additive): $32–45/liter — mix 10–25% with Blu for snap-fit parts
- Can be ordered direct or via Amazon

### 4.2 IPA and Consumables

- **99% Isopropyl Alcohol (IPA):** Home Depot, Lowe's, or Amazon. $30–45/gallon. Buy 2 gallons minimum at startup; 1 gallon lasts approximately 30–40 wash cycles.
- **FEP replacement film:** Elegoo direct store, $12–20 per sheet. Compatible with Saturn 4 Ultra's vat size. Stock 3 sheets minimum — FEP replacement after a failed print that sticks to the vat saves the printer from damage.
- **Nitrile gloves:** Costco or Amazon, 100-pack. $12–18. Use exclusively with resin; never latex.
- **Activated carbon filter cartridges:** Saturn 4 Ultra includes one filter; replacements ~$8–15 every 2–3 months depending on print frequency.

### 4.3 Resin Disposal and Regulatory Compliance

Liquid (uncured) resin is a regulated waste in most US jurisdictions — it cannot be poured down the drain. Used IPA containing dissolved/suspended resin is similarly regulated.

**Compliant disposal options:**
1. **Sun-cure method:** Pour used IPA into a shallow tray, expose to direct sunlight for 4–8 hours. UV light cures the suspended resin particles into solid plastic. Solid plastic can be disposed of in standard trash in most jurisdictions. Remaining IPA (now clear) can be reused or disposed of via household hazardous waste.
2. **UV lightbox method:** Same as above but uses a UV lamp in a box rather than sunlight — works year-round, takes 2–4 hours. A $25–40 UV lamp from Amazon completes this process.
3. **Municipal Household Hazardous Waste (HHW) facilities:** Most US counties accept uncured resin and IPA at HHW drop-off events (typically monthly). Check earth911.com for nearest location.

**Etsy compliance note:** Etsy's 2025 updated policies require that items sold as "made by seller" using computerized tools (including 3D printers) be based on original designs. This is relevant for resin products but not specifically a disposal regulation — it is a product originality requirement. ModRun designs are original (CadQuery parametric), so this is not an issue.

---

## Section 5: CNC Outsourcing Supplier Directory

No CNC equipment purchase is recommended before Month 12. The following suppliers handle all CNC outsourcing needs:

### 5.1 JLCCNC (Primary for Cost)

**URL:** jlccnc.com
**Use case:** Small-to-medium aluminum and engineering plastic parts, 3–5 day production turnaround
**Pricing benchmark (6061 aluminum, 50×50×15mm, 4 features, ±0.1mm tolerance):**
- 1–10 units: $20–45/piece
- 10–50 units: $12–25/piece
- 50–100 units: $8–15/piece

**Process:** Upload STEP file → instant automated quote → confirm → pay → production. No account manager needed for standard parts. 2–3 week total cycle including China-to-US shipping (standard); DHL express adds $30–80 but cuts to 5–7 days.

**Limitation:** Lead time is incompatible with Etsy's 3–5 day fulfillment expectations for custom orders. JLCCNC is appropriate for standardized components (aluminum rails, bulk inserts) ordered in advance, not for on-demand personalized CNC work.

### 5.2 Protolabs Network (Hubs) — Domestic Option

**URL:** hubs.com
**Use case:** US-based shops, 3–7 day domestic turnaround, instant quote
**Pricing:** Approximately 20–40% higher than JLCCNC on comparable parts; $35–65/piece at 1–10 quantity for simple aluminum parts
**Best for:** First prototype of a new CNC component (domestic turnaround for iteration); urgent orders where JLCCNC lead time would miss order fulfillment

### 5.3 Xometry — Scale Option

**URL:** xometry.com
**Use case:** Large volume (50+ units/order) where JLCCNC minimum order size becomes limiting; complex parts requiring multi-axis machining
**Pricing:** Competitive with JLCCNC at higher volumes; "Uber-style" network of 4,375+ partners; instant quote
**Best for:** Month 12+ when CNC volume justifies larger batch ordering

### 5.4 Local Machine Shop — Time-Critical Option

Identify one local machine shop (search: "machine shop [city name]" on Google Maps) before the first CNC order is needed. Get a quote on a standard small aluminum part to benchmark their rates. Local shops typically charge $80–150/hour.

**Best for:** True emergencies where a custom CNC part is needed within 24–48 hours (incompatible with any online service). Relationship established before need = faster response.

---

## Section 6: Facility Requirements by Manufacturing Mode

### 6.1 FDM-Only (Months 0–2)

**Space:** Counter or table space ~600×600mm per printer. Bambu P1S footprint: 389×389mm. Minimal clearance required.

**Ventilation:** Recommended but not strictly required for PLA/PETG. Bambu P1S has a HEPA + carbon filter. Keep a window cracked or add a small USB fan moving air away from the print area. Note: ABS and ASA do require enclosed ventilation; these materials are not part of ModRun's production BOM.

**Electrical:** Standard 110V/15A outlet. P1S draws ~350W peak during heatup, ~120W during printing. A standard household outlet supports 2 P1S printers running simultaneously without issue.

**Storage:** Filament dry storage box (Sunlu or eSUN drybox, $25–40 each) for each spool in rotation. Moisture-damaged filament causes bubbling, stringing, and layer defects — especially relevant in humid climates.

### 6.2 Adding Laser (Months 4–5)

**Space:** xTool S1 footprint: 655×840mm with enclosure closed. Requires dedicated counter or table at comfortable working height (~900mm). Cannot be stored in a closet between uses — setup/teardown friction kills the workflow.

**Ventilation:** xTool S1 is fully enclosed (Class 1) and includes a 4" exhaust port. Connect 4" flexible aluminum duct from the back of the machine to a window or exterior vent. A booster fan (6" inline duct fan, $25–40) improves extraction effectiveness and reduces smoke odor.

**Smoke and residue:** Laser cutting PLA, acrylic, and wood generates fine particulate and VOCs. Even with the built-in filter, a 4" window duct connection is required for extended production runs. Set up the duct before the first real production session — not during it.

**Electrical:** xTool S1 40W draws approximately 450W during full-power cutting operation. Standard 110V outlet. No special wiring required.

**Fire safety:** Keep a CO2 fire extinguisher within reach of the laser. The xTool S1's enclosure contains small fires within the build area, but a flare-up in a jig or thick material can breach containment. This is a low-probability risk but merits a $30 extinguisher that is always present.

### 6.3 Adding Resin (Month 6+)

**Space:** Elegoo Saturn 4 Ultra 16K footprint: approximately 320×220mm printer + 350×300mm Mercury Plus wash/cure station. Total footprint: ~700×300mm side-by-side on dedicated surface. This surface must be:
- Level (resin printing requires <1mm tilt across the build plate)
- Easy to clean (resin drips and spills occur; avoid fabric or wood surfaces — use waterproof shelf liner or aluminum sheet)
- Away from direct sunlight (UV light cures exposed resin; a window-adjacent workspace will cause premature curing of uncovered resin containers)

**Ventilation:** This is the most critical requirement for resin. The Saturn 4 Ultra has an activated carbon filter in the lid, but it is insufficient as the sole ventilation source for extended printing. Resin VOCs (primarily acrylate monomers) are respiratory sensitizers. Requirements:
- Minimum: crack a window in the same room and run a small fan moving air from the printer toward the window
- Recommended: 4" duct to exterior (same setup as the laser) positioned near the printer lid's exhaust
- Ideal: dedicated ventilation enclosure (an inexpensive grow tent with an inline fan and carbon filter creates a fully contained ventilation zone for $80–150)

**Chemical storage:** Keep resin bottles upright in a dark cabinet, away from heat sources. Store IPA in a metal cabinet or on a shelf away from open flames. Maximum storage in a home workshop: 1 gallon IPA + 5kg resin (staying well below fire code limits for Class 3 flammable liquids).

**PPE station:** Establish a dedicated PPE station adjacent to the resin printer: nitrile gloves dispenser, eye protection, paper towels, and a small bowl of IPA for initial cleaning of spills before they cure. The station must be set up before the first print — not assembled in response to a spill.

**Regulatory note:** Most US residential zoning does not prohibit small-scale resin printing, but commercial-scale operations (multiple printers, significant chemical storage) may trigger zoning or home-occupation permit requirements in some jurisdictions. At 1 printer producing 20–50 units/month, this is not an issue in practice. If scaling beyond 3 resin printers, consult local zoning codes.

### 6.4 Full Farm (Month 10–12): 2–3 FDM + Laser + Resin

**Total footprint:** 2 × P1S (or P2S) = ~800mm wide × 400mm deep; xTool S1 = ~840mm wide × 700mm deep; Saturn 4 Ultra + Mercury Plus = ~750mm wide × 300mm deep. Combined, these require approximately 8–10 feet of dedicated counter space (linear), or a 4×8-foot workbench with overhead storage.

**Power distribution:** 2 FDM printers + laser (when running) + resin printer + wash station = peak draw of approximately 1,400W. A standard 15A/110V circuit safely handles 1,800W continuous — this is adequate for all equipment running simultaneously, but on a single dedicated circuit (not shared with other high-draw appliances like space heaters or microwaves).

**Noise:** FDM printers at 35–55 dB, laser engraver at 50–60 dB during cutting (mostly fan noise), resin printer at 30–40 dB. Combined operational noise is acceptable in a home office or garage setting. No noise control measures required at this scale for residential settings.

---

## Section 7: Equipment Leasing Programs — Available Options

### 7.1 Affirm (Most Accessible)

Available at: Bambu Lab, xTool, Elegoo, and most major 3D printing retailers
- No hard credit check for soft inquiry at checkout
- 4 bi-weekly 0% APR payments for small purchases (<$400): ideal for AMS 2 Pro ($286)
- Monthly installments (6–36 months) with interest for larger equipment
- Best for: AMS 2 Pro (4 × $71.50), resin printer ($574 over 4–6 payments)

### 7.2 Clicklease (Equipment Lease-to-Own)

Available at: xTool (via Abunda), Bambu Lab (via Abunda), Formlabs (via authorized resellers)
- Equipment limit: $500–$25,000
- Terms: 24–60 months
- No documents required for equipment under $10,000; soft credit check
- Monthly payments on $1,899 xTool S1: approximately $65–95/month at 24–36 months
- At end of term: option to purchase (typically $1 buyout or small residual)
- Best for: xTool S1 40W when capital preservation is important (e.g., the $1,899 is needed in working capital for inventory/supplies)

**Clicklease acquisition rule:** Leasing a laser adds a fixed monthly commitment to the cost structure regardless of revenue. Do not lease the laser until revenue exceeds $500/month from existing operations — the fixed lease payment should represent less than 15% of current monthly revenue before adding it. At $500/month FDM revenue, $75–95/month laser lease = 15–19% of revenue, which is marginal. At $1,000/month FDM revenue, the same payment is 7.5–9.5% — comfortable.

### 7.3 Formlabs Form 4 Financing (Post-Month-18 Only)

Formlabs offers Affirm financing at checkout (formlabs.com). For the Form 4 at $3,499:
- Example: $700 down + 12 monthly payments at 15% APR ≈ $230/month
- Or 24 months: ≈ $145/month

The Form 4 is a Month 18–24 decision at the earliest (see resin-printing-viability.md trigger conditions). Mention here only to confirm the financing path exists when the trigger is reached.

---

## Section 8: Scaling Pathway — Home-Based Single Printer to 3–5 Printer Farm

### Phase 0 — Current State (Single P1S, Pre-Launch)

Operations: 1 × Bambu P1S producing ModRun clips and rails. Single-color FDM only. Test print pending.

No supplier relationships to establish yet except:
- Primary filament vendor (eSUN or Bambu brand, whichever the operator prefers)
- One local makerspace identified for Month 4 laser validation

### Phase 1 — First 90 Days Post-Launch (Months 1–3)

**FDM:** P1S at full production; establish repeatable plate configurations and batch workflow.

**Supplier relationships to establish:**
- Bambu Lab direct store account: ensure P1S warranty registered; monitor for AMS 2 Pro promotions
- eSUN or Polymaker as primary filament supplier: set up auto-reorder at minimum stock threshold (2 spools of each production color)
- JLCCNC account: create account, upload a simple test part, get a quote (5 minutes) — relationship established before it is needed

**Facility:** No changes from current setup. This is a single-printer operation.

**Capital committed this phase:** $0 new capex if AMS 2 Pro trigger is not yet met.

### Phase 2 — AMS 2 Pro + Laser (Months 3–5)

**FDM:** P1S + AMS 2 Pro. Color-coded production begins.

**Laser:** xTool S1 40W acquired after outsource validation. LightBurn licensed. Workspace now requires 4" duct and dedicated laser table.

**New supplier relationships:**
- xTool: direct purchase (or via Amazon). Register on xTool community forum for firmware updates and settings profiles.
- Acrylic supplier: local plastics shop or Amazon. Identify a local plastics supplier for sheets larger than Amazon's standard A4 offerings — useful once producing acrylic zone labels and tray inserts in volume.
- Baltic birch plywood: local hardwood supplier or Woodcraft. Stock 10+ A3 sheets in 3mm thickness.
- Wood veneer: Woodcraft or Amazon. Cherry/maple veneer, A4 sheets.

**Facility changes:** Counter space for xTool S1 (adjacent to or near the FDM printer). 4" duct connection to exterior.

**Capital committed this phase:** $286 (AMS 2 Pro) + $1,559–$1,959 (xTool S1 + LightBurn). Total: $1,845–$2,245.

### Phase 3 — Resin Specialty Products (Months 6–9, conditional)

**Resin:** Elegoo Saturn 4 Ultra 16K + Mercury Plus, if specific product with identified demand.

**New supplier relationships:**
- Elegoo direct store: resin account, subscribe for stock notifications on ABS-Like 3.0 Pro
- Siraya Tech: direct account for Blu tough resin and Tenacious flexible additive
- IPA: ongoing monthly purchase (Home Depot or Amazon); establish bulk-buy cadence at 2 gallons/month

**Facility changes:** Dedicated resin workstation with waterproof surface liner, adjacent ventilation, PPE station. If space is limited, resin can share the same room as FDM + laser but requires the duct ventilation to service the resin printer as well.

**Capital committed this phase:** $574 (Saturn 4 Ultra + Mercury Plus). Consumables: approximately $50/month ongoing.

### Phase 4 — Farm Expansion (Months 10–12)

**FDM expansion:** Second printer (P2S recommended for new purchase at $549–$799 with AMS 2 Pro Combo) once revenue trigger and capacity constraint are both confirmed.

**Configuration:**
- Printer 1 (P1S + AMS 2 Pro): Multi-color jobs, custom color-coded orders, clip plates
- Printer 2 (P2S): High-volume single-color production batches, rail production (larger parts fit better in P2S at same bed size, but with better extruder reliability)

Or if space permits:
- Printer 1 (P1S + AMS 2 Pro): Multi-color
- Printer 2 (P2S or second P1S): Single-color bulk
- xTool S1 40W: Laser engraving (independent of print jobs)
- Saturn 4 Ultra 16K: Resin specialty products (running in parallel)

**All four stations running simultaneously** is a realistic one-person operation at this scale. Print jobs run unattended; laser and resin require intermittent operator attention (every 20–45 minutes during active laser batches; every 2–4 hours during resin print cycles). Total active production management time: 2–4 hours/day at $5,000–$7,000/month revenue, the rest being unattended runs.

**Capital committed this phase:** $549–$799 (second printer). Cumulative 12-month capex: $3,158–$3,368 (base scenario; see 12-month-multimanufacturing-roadmap.md for full capital table).

### Phase 5 — Potential CNC Integration (Month 12+)

**Decision gate:** If premium aluminum rail product (see cnc-capability-assessment.md Product Idea 1) has been validated at 100+ units/month via JLCCNC outsourcing, and JLCCNC lead times are causing order fulfillment problems.

**Acquisition path:** Nomad 3 Pro ($2,249) for precision small parts, or Shapeoko 5.1 Pro ($3,300) for larger format. Finance via Affirm if capital is not available outright.

**Most likely outcome at Month 12:** CNC remains outsourced. The $2,249–$3,300 capex is better deployed as a third P2S ($799) + laser materials inventory than as a CNC machine requiring 30–50 hours of operator learning investment. Only acquire CNC if the specific revenue trigger is met AND the operator has genuine interest in machining operations.

---

## Section 9: Material Supplier Consolidated Directory

### FDM Filament

| Supplier | Product | Cost | Where to Order |
|---|---|---|---|
| eSUN | PLA+ (primary) | $15–18/kg | Amazon, eSUN direct |
| Bambu Lab | PLA Basic / PETG (AMS multi-color) | $19–25/kg | us.store.bambulab.com |
| Polymaker | PolyTerra PLA (matte, premium look) | $18–22/kg | Amazon, Polymaker direct |
| Overture | PLA (budget option) | $13–16/kg | Amazon |

**Bulk buy trigger:** When monthly filament spend exceeds $100 (approximately 6–7kg/month), switch to 5–10kg purchases for 10–15% cost reduction.

### Laser Materials

| Material | Spec | Cost | Where to Order |
|---|---|---|---|
| Black acrylic 3mm | A4 sheet | $8–15/sheet | Amazon, local plastics shop |
| Clear acrylic 3mm | A4 sheet | $10–18/sheet | Amazon, local plastics shop |
| Baltic birch plywood 3mm | A3 sheet | $15–25/sheet | Woodcraft, Amazon, local |
| Cherry/maple veneer | A4 sheet | $8–15/sheet | Woodcraft, Amazon |
| Wood veneer (economy) | A4 sheet | $5–10/sheet | Amazon (craft veneer packs) |

**Local plastics supplier advantage:** For orders of 20+ acrylic sheets, a local plastics shop (Tap Plastics, ePlastics, or regional equivalents) offers cut-to-size service and better per-sheet pricing than Amazon. Identify one before scaling laser production.

### Resin and Consumables

| Item | Cost | Reorder Trigger | Where to Order |
|---|---|---|---|
| Elegoo ABS-Like 3.0 Pro | $25–35/kg | <2 bottles in stock | Elegoo direct, Amazon |
| Siraya Tech Blu (tough) | $28–40/liter | <1 bottle in stock | Siraya Tech direct, Amazon |
| IPA 99% | $30–45/gallon | <1 gallon in reserve | Home Depot, Amazon |
| FEP film (Saturn 4 Ultra) | $12–20/sheet | <2 sheets in stock | Elegoo direct |
| Nitrile gloves (100-pack) | $12–18 | <20 gloves remaining | Costco, Amazon |

### CNC Outsourcing (No Inventory Needed)

| Supplier | Use Case | Lead Time | URL |
|---|---|---|---|
| JLCCNC | Standard aluminum/plastic parts | 3–5 days production + shipping | jlccnc.com |
| Protolabs Network (Hubs) | Urgent domestic orders | 3–7 days | hubs.com |
| Xometry | High-volume (50+ units) or complex parts | 5–10 days | xometry.com |
| Local machine shop | Emergency (<48hr) | Same day–2 days | Google Maps search |

---

## Appendix: Key Price References (May 2026)

All prices verified May 2026. Prices subject to change; verify at purchase time.

| Item | Price | Source |
|---|---|---|
| Bambu P1S standard | $399 | Bambu Lab US direct |
| Bambu P1S Combo (AMS 2 Pro) | $549 | Bambu Lab US direct |
| Bambu P2S standard | $549 | Bambu Lab US direct |
| Bambu P2S Combo (AMS 2 Pro) | $799 | Bambu Lab US direct |
| Bambu AMS 2 Pro (standalone) | $286 | Bambu Lab US direct |
| Bambu H2D Laser Full Combo 40W | $3,199–$3,499 | Dynamism, Bambu direct |
| xTool S1 40W (full bundle) | $1,299–$1,899 | xTool direct, Amazon |
| LightBurn license (gantry/diode) | $40 | lightburnsoftware.com |
| Elegoo Saturn 4 Ultra 16K | $499 | Elegoo direct, Amazon |
| Elegoo Mercury Plus V3 | ~$75 | Elegoo direct, Amazon |
| Elegoo ABS-Like 3.0 Pro resin | $25–35/kg | Elegoo direct |
| Siraya Tech Blu resin | $28–40/liter | Siraya Tech direct |
| JLCCNC aluminum part (50mm, 10 qty) | $12–25/piece | jlccnc.com |
| Protolabs aluminum part (50mm, 10 qty) | $35–65/piece | hubs.com |
| Nomad 3 Pro CNC | $2,249 | Carbide 3D direct |
| Shapeoko 5.1 Pro CNC | $3,300+ | Carbide 3D direct |
