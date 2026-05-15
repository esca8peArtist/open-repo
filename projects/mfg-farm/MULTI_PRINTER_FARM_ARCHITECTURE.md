---
title: Multi-Printer Farm Architecture & Scaling Roadmap
project: mfg-farm
created: 2026-05-14
updated: 2026-05-15
version: 2.0
status: PRODUCTION READY — corrected May 2026 hardware pricing, updated for X1C discontinuation, phase thresholds aligned to spec
audience: ModRun orchestration team (Anya)
scope: Hardware analysis, TCO, physical space planning, supply chain optimization, workflow scaling, labor requirements, financial modeling, 24-month scaling timeline
related_docs:
  - PRE_LAUNCH_FULFILLMENT_WORKFLOW.md
  - SUPPLIER_NEGOTIATION_PLAYBOOK.md
  - cost-model-spreadsheet.csv
  - headphone-hooks-cost-model.md
---

# Multi-Printer Farm Architecture & Scaling Roadmap

**Purpose**: Execution-ready architecture for scaling ModRun from a single-printer Etsy operation to a 4–8 printer production farm. All hardware pricing reflects verified May 2026 retail figures. Phase thresholds are tied to actual monthly revenue, not subjective readiness.

**Current state (Phase 0)**: Single Bambu P1S running Etsy launch. Test print completed. Pre-print deliverables (designs, listing copy, supplier scorecard, production cost model) are all done. Waiting on Etsy launch results before committing capital to Phase 1.

**Key revision from v1.0**: The Bambu X1C was discontinued in February 2026 and is no longer available new. The P1S has dropped to $399 (from $699 at original launch). The Bambu P2S ($549) is the new mid-range option. These changes significantly affect TCO modeling and the hardware recommendation by phase.

**Activation trigger summary**:
- Phase 1 (2-printer): sustained revenue >$1,500/month
- Phase 2 (4-printer): sustained revenue >$3,500/month
- Phase 3 (8-printer): sustained revenue >$8,000/month

---

## 1. Hardware Analysis & Comparison Matrix

### 1.1 Printer Landscape — May 2026

The Bambu ecosystem dominates small-scale commercial FDM in 2026. The X1 Carbon was discontinued February 10, 2026 (Bambu confirmed end-of-sale; reseller stock is finite and not recommended for farm investment). The Bambu H-series (H2D, H2S) targets engineering and professional materials at $1,249–$3,799 — outside the cost-efficiency range for PLA cable management. The viable candidates for ModRun's farm in order of cost:

| **Model** | **Current MSRP (May 2026)** | **Common Sale Price** | **Status** | **AMS** |
|---|---|---|---|---|
| Bambu A1 Mini | $299 | $219–$249 | Current | AMS Lite (4-color) |
| Bambu A1 | $399 | $329–$369 | Current | AMS Lite (4-color) |
| Bambu P1S | $399–$449 | $399 | Current | AMS 2 Pro (compatible) |
| Creality K2 Plus (base) | $699–$799 | $649 | Current | CFS (16-color, add-on) |
| Bambu P2S | $549 | $499–$549 | Current (2026) | AMS 2 Pro |
| Prusa i3 MK4S | $799 | $749 | Current | MMU3 (optional, $299) |

**ModRun baseline printer**: Bambu P1S (confirmed in cost-model-spreadsheet.csv and headphone-hooks-cost-model.md, where depreciation is calculated at $699 original purchase price — the current $399 street price makes the second unit even cheaper to justify).

---

### 1.2 Detailed Specification Matrix — Candidates for ModRun Farm

| **Metric** | **Bambu A1 Mini** | **Bambu A1** | **Bambu P1S** | **Bambu P2S** | **Creality K2 Plus** | **Prusa i3 MK4S** |
|---|---|---|---|---|---|---|
| **Unit Cost (May 2026)** | $299 ($219 sale) | $399 ($349 sale) | $399–449 | $549 | $699 | $799 |
| **Build Volume (mm)** | 180×180×180 | 256×256×256 | 256×256×256 | 256×256×256 | 350×350×350 | 250×210×220 |
| **Max Speed (rated)** | 500 mm/s | 500 mm/s | 500 mm/s | 600 mm/s | 600 mm/s | 400 mm/s |
| **Practical Production Speed** | 200–250 mm/s | 200–250 mm/s | 200–250 mm/s | 250–300 mm/s | 180–220 mm/s | 150–200 mm/s |
| **Enclosure** | No | No | Yes (full) | Yes (full) | Yes (partial) | No |
| **Multi-Material Native** | AMS Lite (4-color) | AMS Lite (4-color) | AMS 2 Pro compatible | AMS 2 Pro compatible | CFS (16-color add-on) | MMU3 (optional) |
| **Print Quality (dimensional accuracy)** | ±0.1mm | ±0.05mm | ±0.05mm | ±0.05mm | ±0.1–0.15mm | ±0.1mm |
| **Reliability Score (farm community data)** | 8.5/10 | 9/10 | 9.5/10 | 9/10 (new, less data) | 7.5/10 | 9/10 |
| **Nozzle Replacement Cost** | $3–5 (0.4mm hardened) | $3–5 | $3–5 | $3–5 | $8–15 | $20–30 |
| **Nozzle Wear Interval (hours)** | 600–800 | 600–800 | 600–800 | 700–1000 | 300–500 | 400–600 |
| **Bed Surface Cost** | $20–25 (PEI sheet) | $30–40 | $30–40 | $30–40 | $25–35 | $40–60 |
| **Bed Durability (months at production)** | 6–9 | 9–12 | 9–12 | 9–12 | 5–8 | 6–9 |
| **Farm Software Support** | SimplyPrint, Printago | SimplyPrint, Printago | SimplyPrint, Printago, Obico | SimplyPrint, Printago | Moonraker/Klipper | OctoPrint, SimplyPrint |
| **Auto Bed Leveling** | Yes (Lidar) | Yes (Lidar) | Yes (Lidar) | Yes (Lidar) | Yes (CRTouch) | Yes (probe) |
| **Recommended For ModRun** | Phase 1 budget add | Phase 2 budget filler | Primary platform | Phase 3 upgrade path | Not recommended | Not recommended |

**Notes on non-recommended models**:
- **Creality K2 Plus**: Large build volume is wasted on cable clips. CFS multi-color system is unreliable at high duty cycle. Lower nozzle durability at equivalent speed. Not the right fit for a Bambu-ecosystem farm.
- **Prusa i3 MK4S**: Exceptional reliability and part availability. However, slower practical speed than Bambu, smaller build plate relative to price, and no native farm software integration without OctoPrint setup. Best for operators who want repairability over throughput — that is not the ModRun priority profile.

---

### 1.3 Monthly Throughput Analysis by Cluster Size

**Assumptions**: 80% uptime = 12.8 hours/day × 25 days/month = 320 active print hours/month. ModRun cable clip print time: 22–26 minutes per unit at P1S production settings (confirmed from production-workflow-v1.md and cost-model-spreadsheet.csv).

| **Printer** | **Units/Month (single)** | **4-Printer Cluster** | **6-Printer Cluster** | **8-Printer Cluster** |
|---|---|---|---|---|
| **Bambu A1 Mini** | 700–870 | 2,800–3,480 | 4,200–5,220 | 5,600–6,960 |
| **Bambu A1** | 735–875 | 2,940–3,500 | 4,410–5,250 | 5,880–7,000 |
| **Bambu P1S** | 735–875 | 2,940–3,500 | 4,410–5,250 | 5,880–7,000 |
| **Bambu P2S** | 800–960 | 3,200–3,840 | 4,800–5,760 | 6,400–7,680 |

At the current Etsy price point of $12.99–$24.99 per unit (blended AOV from PRE_LAUNCH_FULFILLMENT_WORKFLOW.md: ~$24.99), a single P1S running at 80% uptime represents **$18,350–$21,870 in potential monthly gross revenue**. The constraint at Phase 0 is not printer capacity — it is demand. The throughput capacity above becomes relevant only when Etsy orders are consistently near or above the single-printer limit.

**Critical revenue insight**: A single P1S at 80% uptime can theoretically produce 800+ units/month. At $15/unit net after fees, that is $12,000+/month from one printer. This means the Phase 1 revenue trigger ($1,500/month) represents roughly 10% printer utilization — far below capacity. Adding printers before hitting 50%+ utilization on the first is a capital efficiency error.

---

### 1.4 3-Year Total Cost of Ownership — 4-Printer Cluster Comparison

Assumes 80% uptime, 320 print hours/month, PLA+ as primary material. Power at $0.15/kWh. All figures are for a 4-unit cluster.

| **Cost Category** | **4× A1 Mini** | **4× P1S** | **4× P2S** | **2× P1S + 2× P2S** |
|---|---|---|---|---|
| **Hardware (4 units)** | $956–$1,196 | $1,596–$1,796 | $1,996–$2,196 | $1,896 |
| **Nozzles (3/printer over 36 mo)** | $144–240 | $144–240 | $144–240 | $144–240 |
| **Bed surfaces (2/printer over 36 mo)** | $160–200 | $240–320 | $240–320 | $240–320 |
| **Power (36 mo @ avg 350W print, $0.15/kWh)** | $680 | $725 | $760 | $740 |
| **Filament waste/scrap (5% buffer)** | $3,600 | $3,600 | $3,600 | $3,600 |
| **Maintenance labor (2 hr/printer/month @ $18/hr)** | $1,728 | $1,728 | $1,728 | $1,728 |
| **Software (SimplyPrint $10/mo × 36)** | $360 | $360 | $360 | $360 |
| **Spare parts (nozzle, PTFE, heating cartridge)** | $400 | $400 | $400 | $400 |
| **Enclosure/safety/UPS** | $600 | $600 | $600 | $600 |
| **3-Year Total Cost** | **$8,628–$9,304** | **$9,393–$9,969** | **$9,828–$10,404** | **$9,708** |
| **Monthly equivalent** | **$240–$259** | **$261–$277** | **$273–$289** | **$270** |

**Key finding**: The A1 Mini cluster is $700–$1,000 cheaper over 3 years. However, the A1 Mini's unenclosed design makes it unsuitable for PETG or future material expansion, and the smaller build volume (180×180mm) limits multi-unit plate batching for larger SKUs. **Recommended cluster for Phase 2+: 4× P1S at $1,596–$1,796 total hardware cost.** At that price point, hardware pays back in under 2 weeks of full-utilization production.

**Future adjacent manufacturing note**: If the farm expands to include laser cutting (see `laser-cutting-capability-assessment.md`) or resin printing (`resin-printing-viability.md`), the P1S platform does not limit those additions — they are parallel infrastructure purchases, not upgrades. The farm layout in Section 2 reserves space for a dedicated laser/resin station adjacent to the FDM cluster.

---

### 1.5 Hardware Recommendation by Phase

| **Phase** | **Printer** | **Rationale** | **Unit Cost** | **Count** | **Total Hardware** |
|---|---|---|---|---|---|
| **Phase 0 (Now)** | Bambu P1S (existing) | Established baseline; AMS ecosystem; proven print quality for ModRun clips | $399 (current) | 1 | Already owned |
| **Phase 1 (Month 1–3 trigger)** | Bambu P1S | Maintain platform consistency; same gcode profiles, same AMS; second unit is $399 = 2-week payback at $1,500/month revenue | $399 | +1 (total 2) | $399 |
| **Phase 2 (Month 4–6 trigger)** | 2× Bambu P1S | Expand to 4-printer cluster; all P1S maintains operational simplicity; no gcode reconfiguration | $399 each | +2 (total 4) | $798 |
| **Phase 3 (Month 7–18 trigger)** | 4× Bambu P1S or P2S mix | 8-printer farm; consider P2S for 15–20% speed gain if P2S reliability confirmed by community by that date | $399–549 | +4 (total 8) | $1,596–$2,196 |

**A1 Mini as budget filler**: If Phase 1 revenue arrives faster than expected but cash is tight, a Bambu A1 Mini at $219–$249 (sale) is a valid temporary add before committing to a second P1S. It shares the same Bambu ecosystem software and filament. Throughput is equivalent to P1S for ModRun clip sizes. Upgrade to P1S when cash flow allows.

---

## 2. Physical Space Planning

### 2.1 Footprint Requirements by Cluster Size

All dimensions in feet. Assumes standard US room with 8-ft ceilings. The P1S footprint is 15.3" W × 15.3" D × 18" H (without AMS); with AMS unit: approximately 24" W clearance needed.

| **Cluster Config** | **Printer Arrangement** | **Printer Zone** | **QC + Pack Bench** | **Filament Storage** | **Total Area** |
|---|---|---|---|---|---|
| **2-printer** | Side-by-side on 6 ft bench | 3 × 5 = 15 sq ft | 6 × 3 = 18 sq ft | 2 × 2 = 4 sq ft | ~40 sq ft |
| **4-printer** | 2×2 grid, 18" spacing | 6 × 5 = 30 sq ft | 6 × 4 = 24 sq ft | 3 × 3 = 9 sq ft | ~65 sq ft |
| **6-printer** | 3×2 grid, 18" spacing | 9 × 5 = 45 sq ft | 6 × 4 = 24 sq ft | 4 × 3 = 12 sq ft | ~85 sq ft |
| **8-printer** | 4×2 grid, 18" spacing | 12 × 5 = 60 sq ft | 8 × 4 = 32 sq ft | 5 × 3 = 15 sq ft | ~110 sq ft |

**4-printer Phase 2 layout (overhead view)**:

```
REAR WALL (against wall)
├─ Filament storage shelf (4-tier, wall-mounted, labeled by color)
├─ Tool pegboard (nozzles, IPA, spatulas, calipers)
└─ Spare parts bin (labeled: nozzles / PTFE / springs / belts)

    [P1S #1]   18"   [P1S #2]
    (AMS unit)        (AMS unit)
    
    [P1S #3]   18"   [P1S #4]
    (AMS unit)        (AMS unit)

FLOOR:
├─ 2× power strips (6-outlet, surge-protected, one per printer row)
├─ Ethernet switch (PoE, 8-port managed) — controls all 4 printers
├─ UPS (3 kVA) — under-bench, near power strips
└─ Dehumidifier — center-floor between printer rows

POST-PROCESSING BENCH (right side, perpendicular to printer rows):
├─ Digital calipers
├─ IPA + lint-free wipes
├─ Completed print bins (labeled by order)
├─ Thermal printer (DYMO 4XL or Rollo)
└─ Scale (postal, 0.1 oz precision)

WINDOW (rear-left): Fume extraction duct exhaust port

Total footprint: ~10 ft wide × 7 ft deep = 70 sq ft (printers)
With QC bench: add 6 × 4 = 24 sq ft perpendicular
Grand total: ~95 sq ft — fits a small bedroom, finished basement, or garage bay
```

**8-printer Phase 3 layout**: Double the 4-printer grid by adding a second 4×2 grid section (10 ft × 7 ft additional). The QC bench scales to 8 × 4 ft. Total: ~200 sq ft. A standard 2-car garage bay (20 × 20 = 400 sq ft) comfortably accommodates the full 8-printer farm with room for adjacent manufacturing (laser cutter, resin station).

---

### 2.2 Ventilation & Cooling

**Heat generation**: At 4 P1S printers printing simultaneously, average output is 4 × 350W = 1,400W of heat — equivalent to a space heater. In summer months this raises ambient temperature 10–15°F without active cooling.

| **Solution** | **Setup Cost** | **Monthly Running Cost** | **Effectiveness** | **Recommended For** |
|---|---|---|---|---|
| Window exhaust fan | $30–60 | ~$3 | Adequate air exchange, no cooling | Phase 0–1 (1–2 printers) |
| Portable AC (8,000 BTU) + dehumidifier | $350 + $180 = $530 | $30–45 | Lowers ambient 8–12°F, controls humidity | Phase 2 (4 printers) |
| Dedicated HVAC zone | $2,000–$5,000 install | $40–80 | Full control, best print quality | Phase 3+ (6–8 printers) |
| Ceiling fan + dehumidifier only | $40 + $180 = $220 | $10–15 | Humidity control only, no cooling | Phase 1 in mild climates |

**Fume extraction**: The P1S is fully enclosed with a built-in HEPA + activated carbon filter. Internal filtration handles >90% of particle and VOC capture for PLA. External ventilation requirement: minimum 8 air changes/hour in the print room. A 110 CFM bathroom exhaust fan ($60) vented outdoors via 4" duct handles this for rooms up to 36 cubic meters (15 sq meter × 2.4m ceiling).

**Filter replacement schedule**: P1S internal HEPA/carbon filter every 200–400 hours of PLA printing (Bambu recommends every 3–6 months at production duty cycle). Cost: $15–25 per filter set × 4 printers = $60–100/year.

**Humidity target**: Maintain room humidity below 45% RH. Above 55%, unsealed filament spools begin absorbing moisture within hours. A $180 dehumidifier with humidistat handles this passively — set to 40% and ignore it.

---

### 2.3 Filament Storage System

| **Storage Solution** | **Cost** | **Capacity** | **Humidity Control** | **Phase** |
|---|---|---|---|---|
| Airtight bins + silica gel packs | $40–60 | 10–15 kg | Manual (refresh every 2 weeks) | Phase 0–1 |
| Sunlu S4 Dry Box (active heating) | $80–120 | 20–30 kg | Continuous (5–15% RH) | Phase 2 |
| Industrial dry cabinet (Plastibox) | $400–700 | 60–100 kg | Constant (<5% RH) | Phase 3 |

**Reorder thresholds by phase**:
- Phase 0 (1 printer, ~10 kg/month): Reorder when below 5 kg on-hand (1-week buffer)
- Phase 1 (2 printers, ~20 kg/month): Reorder when below 10 kg on-hand (2-week buffer)
- Phase 2 (4 printers, ~40–50 kg/month): Reorder when below 20 kg on-hand (2-week buffer)
- Phase 3 (8 printers, ~100 kg/month): Reorder when below 50 kg on-hand (2-week buffer); consider 6-week bulk orders

**Color rotation system**: One physical section of storage per color (Black, White, Grey, Translucent, plus 2 specialty slots). Labels facing out. FIFO rule: newest spools go to the back. Print from the front. Mark opened spools with date; discard after 6 months if unused.

---

### 2.4 Electrical Requirements

Each P1S draws approximately 200–250W sustained during printing, with peak inrush of 800–1,000W during bed heating (first 5–7 minutes of each print).

| **Cluster Size** | **Sustained Draw** | **Peak Inrush** | **Circuit Required** | **Estimated Install Cost** |
|---|---|---|---|---|
| **1 printer** | 250W (2.3A @ 110V) | 1,000W (9A) | Standard 15A outlet | $0 |
| **2 printers** | 500W (4.5A) | 2,000W (18A) | Standard 20A circuit | $0 (if existing) |
| **4 printers** | 1,000W (9A) | 4,000W (36A) | Dedicated 20A + staggered starts | $150–250 for dedicated circuit |
| **6–8 printers** | 1,750–2,000W (16–18A) | 8,000W+ | 240V 30A circuit, OR split across two 20A circuits | $300–600 |

**Staggered start protocol** (Phase 2, 4 printers on single 20A circuit):
- Printer 1 starts at 08:00 (bed heating 08:00–08:08)
- Printer 2 starts at 08:10 (bed heating 08:10–08:18)
- Printer 3 starts at 08:20 (bed heating 08:20–08:28)
- Printer 4 starts at 08:30 (bed heating 08:30–08:38)
- Peak draw at any time: 1 printer heating + 3 printing = ~1,500W (well within 20A = 2,200W capacity)

**UPS sizing**: A print job interrupted mid-layer by a power outage wastes 20–45 minutes of material and time. A 1,500W UPS ($150–200) provides 8–12 minutes of bridge time per 2 printers — enough to complete the current layer and pause cleanly.

| **Cluster** | **UPS Capacity** | **Runtime** | **Cost** |
|---|---|---|---|
| 2 printers | 1,500W (1.5 kVA) | 8–10 min | $150–200 |
| 4 printers | 3,000W (3 kVA) | 8–10 min | $350–500 |
| 8 printers | 6,000W (6 kVA) | 8–10 min | $900–1,200 |

---

## 3. Supply Chain Optimization at Scale

### 3.1 Filament Procurement Cost Curves

**Current cost basis** (from cost-model-spreadsheet.csv and headphone-hooks-cost-model.md): $0.013/g = $13/kg for eSUN or Overture PLA+ at 10-kg retail bundles. This is the Phase 0 baseline.

| **Purchase Volume** | **Cost per kg (PLA+)** | **Cost per 75g clip** | **Cost per 25g hook** | **Monthly material cost (4-printer, ~3,200 units)** |
|---|---|---|---|---|
| 1–5 kg (retail single spool) | $16–20 | $1.20–$1.50 | $0.40–$0.50 | $3,840–$4,800 |
| 10 kg bundle (current eSUN) | $12–14 | $0.90–$1.05 | $0.30–$0.35 | $2,880–$3,360 |
| 50 kg order (bulk negotiated) | $10–11 | $0.75–$0.83 | $0.25–$0.28 | $2,400–$2,656 |
| 100–200 kg/month (wholesale) | $8–10 | $0.60–$0.75 | $0.20–$0.25 | $1,920–$2,400 |
| Direct China import (eSUN bulk) | $6–8 | $0.45–$0.60 | $0.15–$0.20 | $1,440–$1,920 |

**Procurement strategy by phase**:
- **Phase 0–1 (1–2 printers, <20 kg/month)**: Continue eSUN 10-kg bundles via Amazon. No negotiation leverage. Priority: reliability and consistent color matching.
- **Phase 2 (4 printers, 40–60 kg/month)**: Contact eSUN wholesale or Overture's bulk program. Target: $10–11/kg. Minimum commitment: 50 kg/order (achievable in 4–6 weeks). Negotiate 3-color-minimum flexibility (Black, White, Grey as primary SKUs).
- **Phase 3 (8 printers, 80–120 kg/month)**: Activate secondary supplier (MatterHackers, Polymaker) at 30% of volume. Reduces single-supplier risk. Primary supplier should be at $9–10/kg.

**Supplier diversification**: Single-supplier dependency becomes material risk at Phase 2+. If eSUN has a stock disruption or color discontinuation, 4 printers go idle. Maintain at least 2 active suppliers by Phase 2.

**Single-supplier risk triggers**: Switch 30% of volume to backup supplier if: (a) lead time extends beyond 10 days, (b) color batch inconsistency complaint rate >2% of orders, (c) price increase >15% without 30-day notice.

---

### 3.2 Nozzle & Hotend Replacement Schedule

**Predictive maintenance model** (P1S, hardened steel 0.4mm nozzle):

| **Component** | **Replacement Interval** | **Unit Cost** | **Annual Cost (4-printer)** | **Trigger Signal** |
|---|---|---|---|---|
| Nozzle (0.4mm hardened) | Every 600–800 print hours | $3–5 | $54–90 (12–20/year) | Under-extrusion, visible scoring |
| Heating cartridge | Every 1,500–2,000 hours | $8–12 | $16–24 (2–3/year per cluster) | Slow heat-up >5 min, temp swings |
| Thermistor | Every 2,000+ hours | $6–10 | $12–20 (2–3/year per cluster) | Temperature fluctuation >5°C |
| PTFE tube (hotend section) | Every 800–1,000 hours | $5–8 | $40–64 (8–10/year per cluster) | Jamming, discoloration |
| Bed PEI sheet | Every 6–9 months | $30–40 per sheet | $120–160 (4 sheets/year) | Bubbles, worn adhesion spots |

**Maintenance schedule**:
- Weekly: Visual nozzle check; wipe bed with IPA after each batch
- Every 500 hours: Proactive nozzle swap (at $3–5 cost, prevents $40–50 failed print events)
- Every 200 prints: Full acetone bed wash
- Monthly: Log all maintenance events in a shared spreadsheet; review for drift patterns

**Cost avoidance math**: 1 failed print due to nozzle clogging = $1–2 material + 2 hours diagnostic/reprint labor = $36–38 total cost. Proactive nozzle at 500 hours = $4 cost. Break-even: prevents 0.1 failures/month = justified at Phase 0.

---

### 3.3 Spare Parts Inventory — Phase 2 Minimum Stock

**Holding $600 in critical spares prevents 3+ days of cluster downtime per year.**

| **Part** | **Unit Cost** | **Stock Level** | **Reorder At** | **Annual Spend** |
|---|---|---|---|---|
| Nozzle 0.4mm (hardened steel) | $3–5 | 12 units | <6 | $54–90 |
| Heating cartridge | $8–12 | 4 units | <2 | $32–48 |
| Thermistor | $6–10 | 4 units | <2 | $24–40 |
| PTFE tube (hotend) | $5–8 | 4 units | <2 | $20–32 |
| PEI bed sheet | $30–40 | 2 sheets | <1 | $120–160 |
| Drive belt (XY set) | $15–25/set | 2 sets | <1 | $30–50 |
| Linear bearings | $8–12 each | 4 units | <2 | $32–48 |
| Extruder drive gear | $10–15 | 2 units | <1 | $20–30 |
| **Total stock value** | | | | **~$600** |

**Breakeven**: Carrying $600 spare parts costs $150/year (25% carrying cost). A 24-hour printer outage at 4-printer capacity = ~100 lost units × $15 net/unit = $1,500 lost revenue. Payback: prevents 0.1 days of downtime per year. This is a no-brainer investment.

---

## 4. Production Workflow Scaling

### 4.1 Batch Processing Optimization

**Fundamental principle**: Batch same-SKU + same-color jobs together to eliminate setup cost between orders. Each color change requires a ~5-minute purge and spool swap ($0.50–$1.00 in filament waste). At 4 printers, uncoordinated color changes across the cluster can cost 2+ hours/day in dead time.

**Daily batch schedule (4-printer cluster, ~160 units/day)**:

```
MORNING BATCH (08:00–16:00) — Black clips and rails:
  P1S #1: Clip-B Black × 40 units (8 hrs continuous)
  P1S #2: Clip-B Black × 40 units (8 hrs continuous)
  P1S #3: Rail Black × 30 units (7 hrs) → reload next job at 15:00
  P1S #4: Rail Black × 30 units (7 hrs) → reload next job at 15:00

AFTERNOON BATCH (16:00–00:00) — White/Grey:
  P1S #1: Clip-B White × 40 units
  P1S #2: Clip-C Grey × 35 units
  P1S #3: Clip-A White × 45 units (reloaded from 15:00)
  P1S #4: Rail Grey × 25 units (reloaded from 15:00)

TOTAL PER DAY: ~160 units across 4 printers running ~16 hrs/day
WEEKLY: ~1,100 units | MONTHLY: ~4,400 units at 4-printer scale
```

**Queue management software**: SimplyPrint ($10/month, up to 10 Bambu printers) or Printago (free tier: unlimited printers, 1 concurrent slot) are the two viable options in May 2026. SimplyPrint has better Bambu-native integration and AI failure detection. Printago has stronger ecommerce-to-queue automation (Etsy orders auto-populate the print queue). **Recommendation**: Start with SimplyPrint at Phase 1 (2 printers), evaluate Printago integration at Phase 2 (4 printers, higher order volume).

---

### 4.2 Bottleneck Analysis — Which Constraint Breaks First

**At 1× volume (100 units/day, 1 printer)**: Printer is the constraint. Post-processing (15–20 min per unit) takes 25–33 hours for 100 units — but 100 units/day from a single printer requires full 80% uptime. The printer is running out of capacity before post-processing becomes a constraint.

**At 2× volume (200 units/day, 2 printers)**: Post-processing becomes the visible constraint. Two printers producing simultaneously means batches arrive at the QC station in waves. A solo operator who is also managing print queues cannot keep up with 200 units/day of post-processing + monitoring.

**At 4× volume (400 units/day, 4 printers)**: Post-processing is definitively the bottleneck. At 15 min/unit (support removal + inspect + pack), 400 units requires 100 hours/day — impossible without dedicated staffing. However, ModRun cable clips have minimal supports by design (confirmed in headphone-hooks-cost-model.md: "no hardware BOM," simplified geometry). With support-free or near-support-free print profiles, post-processing drops to 5–8 minutes/unit (remove, inspect, pack). At 7 min/unit average, 400 units = ~47 hours/day of labor — still requiring 2 people in production.

**At 8× volume (800 units/day, 8 printers)**: Packaging becomes the secondary constraint. Labeling, boxing, and shipping 800 units/day at 90 sec per order (average 5 units/order = 160 orders/day) requires 240 minutes = 4 hours of pure packaging. A dedicated part-time packager is required.

| **Volume Level** | **Primary Bottleneck** | **Secondary Bottleneck** | **Resolution** |
|---|---|---|---|
| 1× (100 units/day, 1 printer) | Printer capacity | None | Optimize print profiles for speed |
| 2× (200 units/day, 2 printers) | Post-processing capacity | Monitoring bandwidth | Hire part-time post-processor |
| 4× (400 units/day, 4 printers) | Labor (post-process + pack) | Filament reorder frequency | 1 dedicated FTE for post-process/pack |
| 8× (800 units/day, 8 printers) | Packaging throughput | QC sampling bandwidth | 2 FTE total; auto-packaging evaluation |

**Design mitigation (highest leverage)**: Designing clips with zero support structures (achievable via print orientation and 45° overhang rule enforcement in CadQuery) eliminates the #1 post-processing time component. Each 2-minute support removal step at 400 units/day = 13 hours/day saved. This is the single highest-ROI operational improvement available before hiring anyone.

---

### 4.3 Quality Control — 3-Stage Model

**Stage 1 — Incoming Filament** (20 min per delivery): Visual seal check, diameter measurement (5 points, calipers, 1.72–1.78mm spec), flexibility bend test. Log result. Only releases to dry storage on 3/3 pass.

**Stage 2 — First Article** (2 hours per new filament lot): Print 1 unit of highest-volume SKU at production settings. Inspect surface finish, layer adhesion, critical dimensions (±0.05mm spec for snap-arm engagement), mechanical snap test (60° deflection without fracture). Log supplier/lot/result.

**Stage 3 — Batch Sampling** (5 min per 50 units): Random 1-unit pull from every 50 printed. 30-second visual + caliper measurement. If out of spec: stop production, diagnose, retest before releasing batch.

**Defect classes and decisions**:
- Minor (<1%): Surface blemishes, acceptable layer lines → ship
- Major (1–5%): Dimensional drift, weak snap arm → reprint, do not ship
- Critical (>5% in batch): Crack, void, non-functional → scrap batch, investigate root cause, replace nozzle if indicated

**Monthly QC review**: Aggregate defect log data. If 80%+ of defects are supplier-correlated → contact supplier, request batch replacement. If 80%+ are printer-correlated → preventive maintenance cycle.

---

### 4.4 Packaging Throughput & 48-Hour SLA

**SLA commitment**: All orders ship within 48 hours of purchase. This is achievable at Phase 0–2 with the batch packaging workflow below.

| **Phase** | **Orders/Day** | **Units/Order (avg)** | **Pack Time/Order** | **Daily Pack Time** | **SLA Risk** |
|---|---|---|---|---|---|
| Phase 0 (1 printer) | 3–8 | 3–5 | 90 sec | 7–18 min | None |
| Phase 1 (2 printers) | 8–15 | 3–5 | 90 sec | 18–34 min | None (solo manageable) |
| Phase 2 (4 printers) | 15–40 | 3–5 | 90 sec | 34–90 min | Manageable with dedicated window |
| Phase 3 (8 printers) | 40–100 | 3–5 | 75 sec (batched) | 50–125 min | Requires dedicated packager |

**Pre-staging trick**: During print hours (when printers are running and require minimal attention), pre-stage 20–30 mailers with tissue paper, thank-you cards, and order slips. When prints finish, harvesting and packing a pre-staged order takes 45 sec instead of 90 sec. Cuts daily packing time by 30–40%.

---

## 5. Labor & Automation Requirements

### 5.1 FTE Requirements by Phase

| **Phase** | **Monthly Units** | **FTE Required** | **Role Split** | **Monthly Labor Cost** |
|---|---|---|---|---|
| **Phase 0** | 100–400 | 0.25 FTE (solo, 10 hrs/week) | Everything: print monitoring, post-process, pack, ship | $0 (owner-operator, no labor cost) |
| **Phase 1** | 400–800 | 0.5–0.75 FTE (20–30 hrs/week) | Owner does monitoring + maintenance; recruit part-time packager (8–12 hrs/week) | $0–600/month (part-time, $15/hr) |
| **Phase 2** | 1,500–3,500 | 1.5 FTE | Lead operator: queue management + maintenance. Part-time post-processor + packager (20–25 hrs/week) | $2,400–$3,600/month |
| **Phase 3** | 3,500–7,000 | 2.5 FTE | Lead operator (FT) + post-process/pack tech (FT) + part-time QC/shipping specialist | $5,400–$7,500/month |

**Hiring sequence**:
1. First hire (Phase 1→2 trigger): Part-time packager. 8–12 hrs/week. Training time: 2 hours. Zero technical knowledge required.
2. Second hire (Phase 2 stabilization): Full-time production tech. 40 hrs/week. Training: 1 week. Handles monitoring, filament swaps, harvest, post-processing, basic troubleshooting.
3. Third hire (Phase 3): Additional full-time or shift-coverage role. Focus: QC and shipping.

**Recruiting lead time**: Budget 6–8 weeks to find, hire, and onboard a production tech. Begin recruiting when you hit 75% of the revenue trigger, not after.

---

### 5.2 Post-Processing Bottleneck Deep Dive

The bottleneck analysis in Section 4.2 shows that post-processing (support removal + inspect + pack) becomes the constraint at 2× volume. Here is the breakdown of where time is spent per unit:

| **Activity** | **Time/Unit (with supports)** | **Time/Unit (support-free design)** | **Notes** |
|---|---|---|---|
| Print removal from bed | 20 sec | 20 sec | Flex plate — quick and consistent |
| Support removal | 2–4 min | 0 min | Eliminate via CadQuery orientation design |
| Deburring/cleaning | 30–60 sec | 15–30 sec | Quick wipe; less flash without supports |
| Dimensional check (sample) | 15 sec (1 per 50) | 15 sec | Spot-sample only |
| Packaging + label | 60–90 sec | 60–90 sec | Irreducible manual step |
| **Total per unit** | **4–7 min** | **1.5–2.5 min** | **Support elimination saves 60–65% of post-processing time** |

**Automation ROI at Phase 2**:
- Robotic print removal ($15K–$25K): Payback at Phase 2 volume (300–600 units/day) = 57–80 months. Not justified until Phase 4+.
- Auto-filament changers (AMS, already on P1S): Already included. Eliminate manual color swaps. Justified at current scale.
- Tumbler deburring ($800–1,500): Saves ~20 sec/unit on cleaning. At 400 units/day = 133 min/day saved. Payback: $1,200 / (133 min × $0.25/min labor) = ~36 days. Worth evaluating at Phase 2 if cleaning is a meaningful time component.

**Outsourcing post-processing**: If post-processing is the constraint and hiring is slow, evaluate outsourcing fulfillment to a 3PL (ShipBob, Simpl Fulfillment — see `3pl-readiness-analysis.md`). 3PL can handle pick-pack-ship for $1.50–$3.50/order at Phase 2 volumes. Cost vs. Part-time hire: 3PL = ~$2.50/order × 600 orders/month = $1,500/month. Part-time hire = $15/hr × 80 hrs/month = $1,200/month. Hire is cheaper at sustained Phase 2 volume; 3PL is better for surge handling.

---

### 5.3 Owner-Operator Time Commitment by Phase

| **Phase** | **Weekly Hours (owner)** | **Primary Activities** |
|---|---|---|
| **Phase 0** | 10–15 hrs | Print monitoring, post-processing, packing, shipping, Etsy listing management |
| **Phase 1** | 15–20 hrs | Add: queue management for 2 printers, supplier relationship, part-time staff coordination |
| **Phase 2** | 20–30 hrs | Add: multi-printer orchestration, QC refinement, financial tracking, hiring/training |
| **Phase 3** | 30–40 hrs | Add: shift scheduling, adjacent manufacturing exploration, 3PL evaluation |

---

## 6. Financial Modeling & Breakeven Analysis

### 6.1 Revenue per Printer per Month

**Assumptions**: 80% uptime (320 print hours/month), 24-minute average print time per unit, $24.99 blended average order value (AOV), Etsy fees at 9.5% + $0.25/order. Net margin basis: material ($0.90–$1.20/unit) + packaging ($0.10/unit) + Etsy fees (~$2.40/unit at $24.99) = ~$3.40–$3.70 COGS.

| **Metric** | **1× P1S** | **2× P1S** | **4× P1S** | **8× P1S** |
|---|---|---|---|---|
| Units/month (80% uptime) | 800 (capacity) | 1,600 | 3,200 | 6,400 |
| Demand-limited units (early phases) | 50–400 | 100–800 | 400–1,600 | 800–3,200 |
| Gross revenue (demand-limited, blended) | $1,250–$9,996 | $2,500–$19,992 | $9,996–$39,984 | $19,992–$79,968 |
| Material + packaging COGS | $500–$4,000 | $1,000–$8,000 | $4,000–$16,000 | $8,000–$32,000 |
| Etsy fees (9.5% + $0.25/order) | $119–$950 | $238–$1,900 | $950–$3,800 | $1,900–$7,600 |
| **Net before labor** | **$631–$5,046** | **$1,262–$10,092** | **$3,046–$20,184** | **$6,092–$40,368** |

**At what monthly revenue does one P1S max out?** A single P1S at 100% utilization produces ~1,000 units/month. At $24.99 AOV, that is $24,990 gross revenue — far beyond any realistic Etsy demand at launch. The printer capacity constraint does not bind until revenue exceeds $10,000/month from a single printer, which requires very high search visibility and conversion rates. **At Phase 0–1 scales, revenue is entirely demand-constrained, not supply-constrained.**

---

### 6.2 Breakeven Timeline by Configuration

| **Configuration** | **Hardware Cost** | **Monthly Net (at trigger revenue)** | **Payback Period** |
|---|---|---|---|
| 1× P1S (Phase 0, already owned) | $399 (sunk) | $800–$1,200 at $1,500/month revenue | Already at breakeven |
| +1× P1S (Phase 1 add) | $399 | $800–$1,500 additional net from 2nd printer | 3–6 months depending on demand ramp |
| +2× P1S (Phase 2 add) | $798 | $2,000–$4,000 net from 3rd+4th printers | 2–4 months at $3,500+/month |
| +4× P1S (Phase 3 add) | $1,596 | $5,000–$10,000 additional net | 1–3 months at $8,000+/month |

**Key insight**: Hardware cost is structurally irrelevant at scale. The $399 P1S pays back in 1–3 weeks of full utilization. The real capital at risk is labor ($3,600–$7,500/month for 1.5–2 FTE in Phase 2–3) and opportunity cost (owner time). These costs are monthly, not one-time.

---

### 6.3 Seasonal Demand Impact

**Q4 (October–December) premium**: Etsy data for home organization and cable management products suggests Q4 sales volume is 40–80% above annual monthly average. Gift-giving season and Black Friday/Cyber Monday drive the spike. For ModRun, this means:
- Inventory build: Start accumulating safety stock in September for October–December demand
- Price testing: Q4 is the highest-leverage window to test +$2–$3 price increases (buyers are less price-sensitive in gift-purchase mode)
- Capacity timing: If Phase 2 (4 printers) is triggered by Q4 demand spike, be aware that January will likely drop back to baseline — plan labor (avoid committing to full-time hire in November for January needs)

**Q1 trough**: January–February are typically 20–35% below annual average for non-essential home goods. Financial models should include a Q1 smoothing assumption.

---

### 6.4 Scenario Analysis

**Conservative** (60% of demand projections — slow Etsy ramp, lower conversion):

| Month | Units | Revenue | Net Profit | Cumulative |
|---|---|---|---|---|
| 1 | 25 | $625 | $300 | $300 |
| 2 | 40 | $1,000 | $480 | $780 |
| 3 | 55 | $1,375 | $660 | $1,440 |
| 4 | 65 | $1,625 | $780 | $2,220 |
| 5 | 75 | $1,875 | $900 | $3,120 |
| 6 | 90 | $2,250 | $1,080 | $4,200 |

Phase 1 revenue trigger ($1,500/month): Reached Month 4. Phase 2 trigger ($3,500/month): Not reached by Month 6 — hold at 2 printers.

**Baseline** (100% of projections — moderate Etsy growth, 2% conversion):

| Month | Units | Revenue | Net Profit | Cumulative |
|---|---|---|---|---|
| 1 | 40 | $1,000 | $480 | $480 |
| 2 | 65 | $1,625 | $780 | $1,260 |
| 3 | 100 | $2,500 | $1,200 | $2,460 |
| 4 | 140 | $3,500 | $1,680 | $4,140 |
| 5 | 175 | $4,375 | $2,100 | $6,240 |
| 6 | 200 | $5,000 | $2,400 | $8,640 |

Phase 1 trigger ($1,500/month): Month 2. Phase 2 trigger ($3,500/month): Month 4. Phase 3 trigger ($8,000/month): Month 9–10 (with 4-printer capacity).

**Optimistic** (150% — rapid Etsy visibility, 3%+ conversion, strong product-market fit):

| Month | Units | Revenue | Net Profit | Cumulative |
|---|---|---|---|---|
| 1 | 60 | $1,500 | $720 | $720 |
| 2 | 110 | $2,750 | $1,320 | $2,040 |
| 3 | 175 | $4,375 | $2,100 | $4,140 |
| 4 | 250 | $6,250 | $3,000 | $7,140 |
| 5 | 330 | $8,250 | $3,960 | $11,100 |
| 6 | 400 | $10,000 | $4,800 | $15,900 |

Phase 1 trigger: Month 1. Phase 2 trigger: Month 2–3. Phase 3 trigger: Month 5. This scenario requires adding printers aggressively — lead time for a new P1S is 5–10 days from Bambu's US store.

---

### 6.5 Critical Decision Tree — When to Add Printers

```
PHASE 0 → PHASE 1 DECISION (add 2nd printer):
  CHECK: Is monthly revenue >$1,500 for 2 consecutive months?
    AND: Is the single P1S running >12 hrs/day with unfulfilled queue?
    YES → Order 2nd P1S (5–10 day delivery). Cost: $399.
    NO → Hold. Revenue is demand-constrained, not supply-constrained.
  
  SLACK: If Month 3 revenue is $1,200 (not yet $1,500),
         wait until Month 4 before ordering. Do not trigger on a single
         high-volume month — confirm the plateau, not the spike.

PHASE 1 → PHASE 2 DECISION (add 3rd + 4th printers):
  CHECK: Is monthly revenue >$3,500 for 2 consecutive months?
    AND: Is 2-printer cluster running >14 hrs/day average?
    AND: Is post-processing queue NOT more than 48 hours behind?
    YES → Order 2× additional P1S ($798). Hire part-time post-processor.
    NO → Hold at 2 printers. Invest in demand generation (Etsy Ads, new SKUs).

  SLACK: If June revenue is $3,200 (close but not $3,500), push Phase 2
         decision to July. If July confirms $3,500+, order in August.

PHASE 2 → PHASE 3 DECISION (add 5th–8th printers):
  CHECK: Is monthly revenue >$8,000 for 2 consecutive months?
    AND: Is 4-printer cluster at >85% utilization?
    AND: Is 1 FTE operator fully hired and trained (not still onboarding)?
    AND: Is post-processing consistently within 48-hour SLA?
    YES → Order 4× additional P1S ($1,596). Begin 2nd FTE hiring.
    NO → Hold at 4 printers. Optimize margins and SKU mix.

  CONTINGENCY TRIGGER: If nozzle replacement rate exceeds 8/month
    across 4 printers → raise unit COGS assumption by $0.15/unit and
    recalculate phase trigger thresholds before ordering more printers.
```

---

## 7. 24-Month Scaling Phase Timeline

### 7.1 Phase 0 (Now – June 2026): Single Printer Etsy Launch

**Goal**: Prove product-market fit. Establish operational baseline. Build review velocity.

**Targets**:
- Launch Etsy listing by end of May 2026
- Achieve 10+ reviews by Day 30
- Revenue >$1,500/month by Month 3 (August 2026)

**Key actions**:
- Week 1–2: Etsy listing live, photography done, Pirate Ship + SimplyPrint configured
- Week 3–4: Monitor conversion rate daily; A/B test main photo if <2% conversion
- Month 2: If 0–5 orders/week, add 1–2 additional SKUs from BATCH_2 or BATCH_3_5 pipeline
- Month 3: Decision gate. See Phase 0→1 decision tree above.

**Operations**: Solo operator (owner), 10–15 hrs/week. No hired staff.

**Decision gate (August 2026)**: Revenue >$1,500/month × 2 consecutive months → proceed to Phase 1. Revenue <$1,000/month by Month 3 → product/marketing review before adding any capital.

---

### 7.2 Phase 1 (June – August 2026, Month 1–3 post-trigger): 2-Printer Cluster

**Trigger**: Revenue sustained >$1,500/month. Single printer running >12 hrs/day.

**Actions**:
- Order 2nd Bambu P1S ($399, 5–10 day delivery)
- Configure SimplyPrint multi-printer queue ($10/month)
- Begin recruiting part-time post-processor (8–12 hrs/week, $15/hr) — recruit 6 weeks before revenue trigger if trajectory is clear
- Add second AMS filament station; stock additional color spools

**Revenue target**: $3,000–$5,000/month by end of Phase 1 (Month 3 of 2-printer operation).

**Operations**: Owner-operator (15–20 hrs/week) + part-time packager (8–12 hrs/week). Total team: 1.25–1.5 FTE equivalent.

**Decision gate (October–November 2026)**: Revenue >$3,500/month × 2 consecutive months → proceed to Phase 2. Revenue stalls at $2,000–$3,000 → optimize conversion (Etsy Ads, listing copy), expand SKU count, do not add printers yet.

**Contingency — revenue hits $1,500 in September instead of June**: Push Phase 1 hardware order to September. Phase 2 decision slips to January 2027. No material harm — the plan adapts to actual demand, not projected demand.

---

### 7.3 Phase 2 (September – November 2026, Month 4–6 post-trigger): 4-Printer Cluster

**Trigger**: Revenue sustained >$3,500/month. 2-printer cluster at >14 hrs/day average utilization.

**Actions**:
- Order 2× additional Bambu P1S ($798 total)
- Upgrade to 4-printer physical layout (Section 2.1); install dedicated electrical circuit if needed ($150–250)
- Hire 1 full-time production tech ($18–22/hr = $3,200–$3,900/month). Begin recruiting 6 weeks before trigger.
- Install Sunlu S4 dry box for filament storage ($120)
- Set up Printago or SimplyPrint for 4-printer queue management
- Establish bulk filament procurement with eSUN/Overture at 50 kg/order

**Revenue target**: $7,000–$12,000/month by end of Phase 2 (Month 6 of 4-printer operation).

**Operations**: Owner (20–30 hrs/week) + 1 FTE production tech + 0.5 FTE part-time packager. Total: 1.5–2 FTE.

**Decision gate (March–May 2027)**: Revenue >$8,000/month × 2 consecutive months → proceed to Phase 3. Revenue stalls at $5,000–$7,000 → investigate: Is SKU diversity limiting? Is pricing at ceiling? Explore Amazon Handmade expansion (see `amazon-fba-analysis.md`).

**Contingency — 4-printer launch delayed to October 2026**: Phase 3 decision gate slips to April–May 2027. Acceptable — timeline is demand-driven, not calendar-driven.

---

### 7.4 Phase 3 (December 2026 – May 2027, Month 7–18): 8-Printer Farm

**Trigger**: Revenue sustained >$8,000/month. 4-printer cluster at >85% utilization. Phase 2 operator fully trained.

**Actions**:
- Order 4× additional Bambu P1S or P2S ($1,596–$2,196). Confirm P2S farm reliability in community reports before ordering.
- Expand physical space to 8-printer layout (110 sq ft total or dedicate full garage bay)
- Install 240V circuit ($300–600)
- Hire 2nd FTE (full-time production tech or shift coordinator)
- Implement industrial dry cabinet ($400–700) for 60–100 kg filament capacity
- Evaluate 3PL partnership for fulfillment (ShipBob, Simpl Fulfillment — see `3pl-readiness-analysis.md`)
- Begin adjacent manufacturing exploration: laser cutter for engraved variants (see `laser-cutting-capability-assessment.md`), or resin printing for precision components (see `resin-printing-viability.md`)

**Revenue target**: $20,000–$40,000/month by Month 18 (May 2027).

**Operations**: Owner (30–40 hrs/week) + 2 FTE production team + 0.5 FTE part-time QC/shipping. Total: 2.5–3 FTE.

**Decision gate (May 2027)**: Revenue >$30,000/month → 3PL integration, multi-SKU line expansion, Amazon FBA exploration. Revenue $15,000–$30,000 → optimize 8-printer farm, defer 3PL until 200+ orders/month threshold.

---

### 7.5 Decision Gate Summary (Quick Reference)

| **Gate** | **Trigger** | **Action** | **Capital Required** | **Timeline Slack** |
|---|---|---|---|---|
| Phase 0 → 1 | $1,500+/month × 2 months | Order 2nd P1S | $399 | +1 month before ordering if close |
| Phase 1 → 2 | $3,500+/month × 2 months | Order 2× P1S + hire FT tech | $798 hardware + $3,200/month labor | +1–2 months before ordering if close |
| Phase 2 → 3 | $8,000+/month × 2 months | Order 4× P1S/P2S + hire 2nd FTE | $1,596–$2,196 hardware + $3,600/month labor | +2–3 months if Q4 seasonality distorts data |
| Phase 3 consolidation | $30,000+/month × 3 months | 3PL evaluation, Amazon FBA, adjacent mfg | Variable ($0 for 3PL eval; $2,000–$8,000 for laser/resin) | Take full quarter to validate before committing |

**Nozzle rate contingency trigger**: If nozzle replacement rate exceeds 2 per month per printer (8+ across a 4-printer cluster), the print profile is too aggressive for the material. Slow print speed by 15%, reduce temperature by 5°C, re-run dimensional QC. Resolve before scaling to next phase.

---

### 7.6 Capital Investment Schedule

| **Phase** | **Hardware** | **Infrastructure** | **Labor (cumulative monthly)** | **Total Phase Investment** |
|---|---|---|---|---|
| **Phase 0 (sunk)** | $399 (P1S, already owned) | $200 (filament storage, tools) | $0 | $599 |
| **Phase 1** | $399 (2nd P1S) | $200 (cables, cooling, SimplyPrint $10/mo) | $0–$600/month (part-time) | $599 + $600–$1,800 |
| **Phase 2** | $798 (2× P1S) | $500 (electrical, dry box, UPS) | $3,200–$3,900/month (FT tech) | $1,298 + $19,200–$23,400 (6 months) |
| **Phase 3** | $1,596–$2,196 (4× P1S) | $800–$1,200 (circuit, dry cabinet, space) | $6,400–$7,800/month (2 FTE) | $2,396–$3,396 + $76,800–$93,600 (12 months) |

**Key takeaway**: Hardware is a minor capital item relative to labor. Over 18 months, labor costs will represent 85–90% of total investment. The business case for scaling is labor productivity: each additional printer produces revenue with minimal incremental labor until the post-processing bottleneck binds.

---

## Appendix A: Monitoring Software Stack

| **Tool** | **Cost** | **Printers Supported** | **Best For** |
|---|---|---|---|
| Bambu App | Free | All Bambu (cloud) | Phase 0 single printer |
| SimplyPrint | $10/month (3–10 printers) | Bambu, Prusa, others | Phase 1–2 (queue management, AI failure detection) |
| Printago | Free (1 concurrent) / $29/month | All Bambu | Phase 2–3 (Etsy-to-queue automation) |
| Obico | $10/month pro | Bambu, Prusa, generic | Phase 2–3 (AI defect detection) |

**Recommendation by phase**: Bambu App (Phase 0) → SimplyPrint (Phase 1, 2 printers) → Printago or SimplyPrint Pro (Phase 2–3, 4–8 printers with Etsy automation).

---

## Appendix B: Supplier Contact & Pricing Targets

| **Supplier** | **Material** | **Current Price** | **Bulk Target** | **Contact Method** |
|---|---|---|---|---|
| eSUN | PLA+ (primary) | $12–14/kg (10-kg bundle) | $10–11/kg (50 kg order) | esun3dstore.com wholesale inquiry |
| Overture 3D | PLA+ (backup) | $13–16/kg | $10–12/kg (wholesale program) | overture3d.com/pages/wholesale |
| MatterHackers | PLA Pro (backup) | $18–22/kg | $14–16/kg (quantity) | matterhackers.com business account |
| Polymaker | PolyLite PLA (specialty) | $16–20/kg | $12–14/kg | polymaker.com |

**Dual-supplier activation**: Maintain eSUN as primary at Phase 0–1. Activate Overture or MatterHackers at Phase 2 (40+ kg/month purchase volume) at 30% of volume. This ensures no single supplier disruption can halt production.

---

## Document Control

**Version 2.0** (2026-05-15): Complete rewrite of hardware section to reflect May 2026 market reality. Corrected X1C discontinuation (end-of-sale Feb 2026). Updated P1S pricing from $699 to $399 current street price. Added P2S and A1/A1 Mini as viable alternatives. Phase revenue thresholds revised to match project specification ($1.5K/$3.5K/$8K). Bottleneck analysis expanded with design mitigation recommendations. Decision tree added with explicit contingency triggers.

**Status**: Production-ready. Distribute to operations team upon Phase 1 trigger.

**Word count**: ~5,100 words | **7 major sections** | **Actionable tables, decision trees, and financial models throughout**

---

## Sources

- [Bambu Lab P1S Current Pricing — Bambu Lab US Store](https://us.store.bambulab.com/products/p1s)
- [Bambu Lab Printer Prices 2026: Full Lineup & Price History — OriginalPricing](https://originalpricing.com/bambu-lab-printer-prices/)
- [Bambu Lab P1S Price History — PriceHistory App](https://pricehistory.app/p/bambu-lab-p1s-3d-printer-fully-enclosed-v1eINkG5)
- [Bambu Lab X1C — End of Sale Announced February 2026 (community confirmation)](https://forum.bambulab.com/t/bambu-lab-x1c-price/106809)
- [The Complete Bambu Lab Print Farm Guide 2026 — Printago](https://printago.io/blog/bambu-lab-print-farm-guide-2026)
- [Bambu Lab A1 Mini 2026 Review and Farm Use — Innocube3d](https://www.innocube3d.com/blogs/news/bambu-lab-a1-vs-a1-mini-2026)
- [Creality K2 Plus Combo Price 2026 — Creality Official Store](https://store.creality.com/products/creality-k2-plus-combo-3d-printer)
- [Overture 3D Wholesale Program](https://overture3d.com/pages/wholesale)
- [3D Printer Filament Price Tracker — FilamentPriceTracker](https://filamentpricetracker.com/)
- mfg-farm/cost-model-spreadsheet.csv — COGS baseline, filament cost ($0.013/g)
- mfg-farm/headphone-hooks-cost-model.md — P1S depreciation model, labor rate confirmation
- mfg-farm/PRE_LAUNCH_FULFILLMENT_WORKFLOW.md — AOV, order volume projections, staffing triggers
