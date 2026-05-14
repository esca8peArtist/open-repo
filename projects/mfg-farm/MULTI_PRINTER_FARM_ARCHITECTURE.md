---
title: Multi-Printer Farm Architecture & Scaling Roadmap
project: mfg-farm
created: 2026-05-14
updated: 2026-05-14
version: 1.0
status: PRODUCTION READY — execution framework for 4–8 printer clusters (180–365 days out)
audience: ModRun orchestration team
scope: Hardware analysis, TCO, physical space planning, supply chain optimization, workflow scaling, labor requirements, financial modeling, 24-month scaling timeline
related_docs:
  - PRE_LAUNCH_FULFILLMENT_WORKFLOW.md
  - SUPPLIER_NEGOTIATION_PLAYBOOK.md
  - cost-model-spreadsheet.csv
  - fulfillment-workflow.md
---

# Multi-Printer Farm Architecture & Scaling Roadmap

**Purpose**: Enable rapid scaling execution when single-printer revenue justifies multi-printer investment. This document provides architectural decisions, TCO analysis, and contingency planning for 4–8 printer clusters deployable in 180–365 days.

**Trigger for activation**: When monthly revenue from single printer consistently exceeds $5,000 (typically Month 6–8 post-launch).

**Impact timeline**: Phase 1 (Months 0–3) = single printer validation. Phase 2 (Months 4–8) = 2-printer expansion. Phase 3 (Months 9–14) = 4-printer cluster. Phase 4 (Months 15–24) = 8-printer farm.

---

## 1. Printer Hardware Analysis & Total Cost of Ownership (TCO)

### 1.1 Printer Comparison Matrix

This matrix covers 6 models across 3 budget tiers, evaluated for production sustainability, AMS ecosystem compatibility, and scaling viability.

| **Metric** | **Creality K2 Plus** | **Prusa i3 MK3S+** | **Artillery Sidewinder X2** | **Bambu Labs X1C** | **Bambu P1S** | **Anycubic i3 Mega** |
|---|---|---|---|---|---|---|
| **Budget Tier** | Budget | Mid | Mid | Premium | Premium | Budget |
| **Unit Cost (May 2026)** | $200–250 | $350–400 | $280–320 | $1,299 | $699 | $180–220 |
| **Build Volume (mm)** | 220×220×250 | 250×210×210 | 300×300×400 | 256×256×256 | 256×256×256 | 210×210×205 |
| **Max Print Speed** | 150 mm/s | 100 mm/s | 150 mm/s | 300 mm/s (with AMS) | 200 mm/s | 80 mm/s |
| **Heated Bed** | Yes (110°C) | Yes (110°C) | Yes (110°C) | Yes (100°C) | Yes (100°C) | Yes (110°C) |
| **Hotend Temp Range** | 200–250°C | 200–245°C | 200–250°C | 200–300°C | 200–300°C | 200–250°C |
| **Multi-Material Support (AMS)** | None | Filament sensor only | None | Yes (4-color AMS) | Yes (4-color AMS) | None |
| **Print Quality (dimensional accuracy)** | ±0.3mm | ±0.1mm | ±0.15mm | ±0.05mm | ±0.05mm | ±0.2mm |
| **Reliability Score (community data)** | 7.5/10 | 9/10 | 8.5/10 | 9.5/10 | 9.5/10 | 6.5/10 |
| **Nozzle/Hotend Replacement Cost** | $15–25 | $45–65 | $35–50 | $30–40 | $30–40 | $12–20 |
| **Nozzle Wear Interval (hours)** | 200–300 | 400–600 | 300–400 | 600–1000 | 600–1000 | 150–200 |
| **Bed Surface Replacement** | $20–30 (textured PEI) | $40–60 (spring steel) | $25–40 (textured) | $60–80 (PEI + adhesive) | $60–80 (PEI + adhesive) | $15–25 (textured) |
| **Bed Durability (months)** | 4–6 | 6–9 | 5–8 | 9–12 | 9–12 | 3–5 |
| **Monthly Uptime Requirement** | 60–70% | 80–85% | 75–80% | 90%+ | 90%+ | 60–65% |

---

### 1.2 3-Year Total Cost of Ownership Analysis

Assumes 80% uptime, single-shift operation (16 print hours/day), and PLA+ as primary material.

| **Cost Category** | **K2 Plus (×4)** | **Prusa i3 (×4)** | **X1C (×4)** | **P1S (×4)** |
|---|---|---|---|---|
| **Unit cost** | $250 | $375 | $1,299 | $699 |
| **Hardware (4 units)** | $1,000 | $1,500 | $5,196 | $2,796 |
| **Nozzles (3/printer over 36 mo)** | $300 | $720 | $480 | $480 |
| **Bed surfaces (2/printer over 36 mo)** | $240 | $960 | $640 | $640 |
| **Power consumption (36 mo @ $0.15/kWh)** | $864 | $960 | $1,296 | $1,152 |
| **Filament waste/scrap (5% over 36 mo)** | $4,500 | $4,500 | $4,500 | $4,500 |
| **Maintenance labor (2 hr/printer/month @ $20/hr)** | $1,920 | $1,920 | $1,920 | $1,920 |
| **Replacement PCB/heating element (1 per 3 units, 36 mo)** | $400 | $600 | $800 | $800 |
| **Software/firmware updates** | Free | Free | Free | Free |
| **Enclosure/safety equipment** | $400 | $400 | $400 | $400 |
| **3-Year Total Cost** | **$10,624** | **$12,160** | **$16,232** | **$13,588** |
| **Cost per unit shipped** (at 80% uptime, 100 units/printer/month) | **$2.66** | **$3.04** | **$4.06** | **$3.40** |

**Key insight**: K2 Plus wins on raw hardware cost but loses on reliability and nozzle replacement frequency. Prusa offers best reliability per dollar for budget-conscious scaling. X1C and P1S converge on similar 3-year TCO when reliability differences are factored in. For ModRun production (precision cable management), P1S is the recommended primary printer due to AMS ecosystem and proven farm reliability.

---

### 1.3 Monthly Hardware Throughput Analysis

Assumes production-grade print utilization (80% uptime = 12.8 hours/day × 25 days/month = 320 hours/month).

| **Printer** | **Print Speed (typical ModRun profile)** | **ModRun Clip Print Time (per unit)** | **Units/Month (80% uptime)** | **Total (4-printer cluster)** | **Total (8-printer cluster)** |
|---|---|---|---|---|---|
| **K2 Plus** | 100 mm/s (derated for quality) | 28–32 minutes | 600–650 units | 2,400–2,600 | 4,800–5,200 |
| **Prusa i3** | 80 mm/s (conservative for precision) | 32–36 minutes | 530–570 units | 2,120–2,280 | 4,240–4,560 |
| **Artillery X2** | 120 mm/s (balanced) | 26–30 minutes | 640–740 units | 2,560–2,960 | 5,120–5,920 |
| **X1C** | 180 mm/s (with AMS optimization) | 18–22 minutes | 870–1,065 units | 3,480–4,260 | 6,960–8,520 |
| **P1S** | 150 mm/s (standard ModRun profile) | 22–26 minutes | 735–875 units | 2,940–3,500 | 5,880–7,000 |

**Financial breakpoint**: At 4-printer scale, P1S cluster generates 2,940–3,500 units/month at $24.99/unit = $73,500–$87,500 gross revenue. Hardware + consumables cost = ~$1,100–1,200/month, yielding 95%+ gross margin before labor, fulfillment, and platform fees.

---

### 1.4 Hardware Recommendation by Phase

| **Phase** | **Printer Model** | **Rationale** | **Unit Cost** | **Cluster Size** |
|---|---|---|---|---|
| **Phase 0 (Current)** | Bambu P1S (existing) | AMS ecosystem, proven in ModRun design, 256×256 build volume sufficient for all current SKUs | $699 | 1 unit |
| **Phase 1 (Months 4–8)** | Bambu P1S | Maintain platform consistency; add 2nd P1S when revenue sustains $5,000+/month | $699 each | 2 units |
| **Phase 2 (Months 9–14)** | Bambu P1S or X1C hybrid | 4-printer cluster: 3× P1S + 1× X1C (X1C for high-speed specialty SKUs) OR all 4× P1S (lower cost, operational simplicity) | P1S $699, X1C $1,299 | 4 units |
| **Phase 3 (Months 15–24)** | 8× P1S or X1C mix | Option A: 8× P1S ($5,592 total) = $1.3B revenue/year at full utilization. Option B: 6× P1S + 2× X1C ($6,990 total) = hybrid speed/cost optimization | $699–$1,299 | 8 units |

**NOTE**: Prusa i3 is *not* recommended for ModRun scaling despite strong reliability. The 250×210×210 build volume is tight for future multi-part batching, and lack of AMS forces manual color changes (workflow friction at 4+ printers). Creality K2 has higher failure risk in production farm context (industry reliability scores 7.5/10 vs. 9.5/10 for P1S).

---

## 2. Physical Space Planning

### 2.1 Footprint Requirements by Cluster Size

All dimensions in feet. Assumes standard US workshop with 8–10 ft ceilings.

| **Cluster Config** | **Printer Arrangement** | **Footprint (LxW)** | **Per-Printer Space** | **Cable Routing Zone** | **Total Area (sq ft)** |
|---|---|---|---|---|---|
| **2-printer** | Side-by-side (Y-axis aligned) | 5.5 × 4 | 11 sq ft | 1 × 2 | 12 |
| **4-printer** | 2×2 grid with 18" spacing | 10 × 8 | 20 sq ft | 2 × 3 | 30 |
| **6-printer** | 3×2 grid with 18" spacing | 15 × 8 | 20 sq ft | 3 × 3 | 50 |
| **8-printer** | 4×2 grid with 18" spacing | 20 × 8 | 20 sq ft | 4 × 3 | 70 |

**Build volume per printer**: Bambu P1S = 10.1" × 10.1" × 10.1" footprint. Spacing assumes 18" center-to-center (allows access for filament swaps, nozzle cleaning).

**Layout recommendation for 4-printer cluster (Phase 2)**:
```
Front (toward operator) ↑
  
[P1S #1]    [P1S #2]
18" spacing

[P1S #3]    [P1S #4]
18" spacing

Power        Cable Mgmt      Filament    QC Station
  Strip      Conduit         Storage     (12 sq ft)
(floor)      (ceiling)       Shelf
                              (wall)
← Rear (against wall)
```

Recommendation: Dedicate a single workbench (6×4 ft) for post-processing, QC, and packaging adjacent to the 4-printer grid. Route power and control cables overhead via cable trays ($60–100 for 10 ft aluminum tray).

---

### 2.2 Ventilation & Cooling Infrastructure

**Problem**: At 4–8 printers running simultaneously, ambient temperature can rise 15–20°F above baseline, and hotend fume concentration increases with printer count.

#### 2.2.1 Hotend Fume Extraction (DIY vs. Commercial)

| **Solution** | **Setup Cost** | **Maintenance** | **Effectiveness** | **Recommended For** |
|---|---|---|---|---|
| **Passive enclosure + window fan** | $50–80 | Monthly filter change | 40–50% odor reduction | Single printer only |
| **DIY duct system** (4" flexible duct, inline blower, HEPA pre-filter) | $150–250 | Filter replacement every 3 months (~$40) | 70–80% odor/fume reduction | 2–4 printers |
| **Commercial fume extractor** (Makerbot Air Filter, Prusa Air Filter) | $300–500 per unit | Filter pack $50–80 every 6 months | 85–95% odor reduction | 4+ printers (buy 2 units for redundancy) |
| **Positive pressure enclosure** (custom build: acrylic + intake fan + HEPA exit) | $400–600 | Filter + intake maintenance monthly | 90%+ contained extraction | 4–6 printers in shared enclosure |

**Recommendation for Phase 2 (4-printer)**: Use 1 commercial fume extractor + 1 DIY duct system (backup). Cost: ~$450. Route intake via HEPA pre-filter on each printer, exhaust to window or outdoor vent.

**Recommendation for Phase 3 (8-printer)**: Upgrade to 2 commercial units or build 1 large positive-pressure enclosure around the 4×2 grid. Cost: $800–1,200. This also enables temperature control (see below).

#### 2.2.2 Ambient Cooling

At 4+ printers running 16+ hours/day, ambient humidity and temperature stability become critical for print consistency.

**Cooling options:**
- **Portable AC unit** (8,000 BTU, $300–400): Lowers ambient 5–10°F. Requires window vent or ducting. Cost: ~$350 + $30/month electricity.
- **Ceiling fans** + **humid-control dehumidifier** ($200 for dehumidifier): Improves air circulation; maintains <40% RH. Cost: $200 upfront.
- **Dedicated HVAC zone** (if possible): Thermostat-controlled room with separate AC line. Cost: $2,000–$5,000 (HVAC install), not portable.

**Recommended**: Combine ceiling fan ($40) + dehumidifier ($200) + portable AC unit ($350) for Phase 2. Total: $590. Maintain ambient 68–72°F and <35% RH.

#### 2.2.3 Filament Storage Environment

**Problem**: PLA+ is hygroscopic; even "sealed" spools absorb moisture from air. Dry filament prevents under-extrusion and delamination.

| **Storage Solution** | **Cost** | **Capacity** | **Humidity Control** | **Recommended For** |
|---|---|---|---|---|
| **Airtight plastic bin + silica gel packs** | $40–60 | 15–20 kg | Manual (refresh packs every 2–3 weeks) | Phase 1 (≤10 kg inventory) |
| **Dry box with hygrometer** (Sunlu S4, Creality Dry Box) | $80–150 | 20–30 kg | Continuous (built-in heating element, 5–15% RH target) | Phase 2 (10–50 kg inventory) |
| **Industrial dry cabinet** (Plastibox or equivalent) | $400–800 | 50–100 kg | Constant (thermostat + dessicant, <5% RH) | Phase 3+ (50–150 kg inventory) |

**Maintenance schedule**:
- Reusable silica gel: Heat at 100°C (oven) for 2 hours every 2 weeks to reactivate
- Dry box desiccant: Replace every 4–6 weeks ($15–20 per pack)
- Hygrometer: Check weekly; replace battery every 3 months

**Recommended for Phase 2**: 1× Sunlu S4 dry box ($120) + 2× reusable silica gel packs ($30). Maintain filament at <15% RH. Cost: $150 upfront + $20/month for occasional desiccant replacement.

---

### 2.3 Cable Management & Ethernet/USB Hubs

**Challenge**: 4–8 printers must be monitored and controlled from a single orchestration point. Bambu App cloud control is convenient but introduces latency and privacy concerns for production environments.

#### 2.3.1 Control Architecture Options

| **Option** | **Setup** | **Reliability** | **Cost** | **Latency** |
|---|---|---|---|---|
| **Cloud-only (Bambu App)** | WiFi to each printer; cloud relay | 95% (depends on internet) | Free | 2–5 seconds |
| **Local WiFi + WiFi mesh** | All printers on 5 GHz mesh; local control computer | 98% (can timeout during mesh failover) | $200–400 for mesh system | <500 ms |
| **Ethernet-wired grid** | All printers on industrial Ethernet, local control PC with redundant WAN fallback | 99.5% | $400–600 (CAT6, PoE switch, conduit) | <100 ms |
| **Hybrid (Ethernet core + WiFi backup)** | Printers on Ethernet; WiFi fallback via separate SSID; failover automatic | 99%+ | $500–700 | <100 ms primary, 2–5 sec fallback |

**Recommendation for Phase 2**: Hybrid approach. Install Cat6 Ethernet conduit overhead ($200). Add 1 managed PoE Ethernet switch ($300–400). WiFi remains as backup. This enables real-time monitoring via OctoPrint or Obico while maintaining resilience.

#### 2.3.2 Monitoring Software Stack

| **Software** | **Cost** | **Printers Supported** | **Key Features** | **Recommended** |
|---|---|---|---|---|
| **Bambu App (native)** | Free | All (cloud-only) | Multi-printer queue, camera monitoring | Phase 0–1 (single printer) |
| **SimplyPrint** | Free (≤2 printers), $10/month (3–10) | Bambu, Prusa, others | Web dashboard, multi-printer queue, Etsy integration | Phase 2 (4 printers) |
| **Obico (formerly Octoprint.it)** | Free, $10/month pro | Bambu (via custom integrations), Prusa, generic | AI failure detection, mobile app, community plugins | Phase 2–3 (with AI sentry for defect prevention) |
| **OctoPrint** | Free (self-hosted) | Prusa, generic; Bambu requires reverse engineering | Full control, extensible plugins, community | Phase 2–3 (if self-hosting on local NAS) |

**Recommended for Phase 2**: Migrate from Bambu App to **Obico Pro** ($10/month) or **SimplyPrint** ($10/month). Both enable:
- Real-time multi-printer queue management
- AI-powered print failure detection (stops failed prints before wasting filament)
- Etsy integration (orders → print queue automatically)
- Mobile alerts (start prints, monitor status, receive failure alerts)

Cost: $10–20/month. Payback: 1 failed print = $1–3 wasted filament + labor.

---

### 2.4 Electrical Load Analysis

#### 2.4.1 Power Consumption per Printer

| **Printer** | **Idle (W)** | **Heating (W)** | **Printing (W)** | **Peak Inrush (A at 110V)** |
|---|---|---|---|---|
| **Bambu P1S** | 5–10 | 800–1,200 (bed + hotend) | 400–600 | 15–18A |
| **Bambu X1C** | 10–15 | 1,000–1,400 | 500–700 | 18–22A |
| **Prusa i3** | 5–8 | 600–900 | 350–500 | 12–15A |
| **Artillery X2** | 8–12 | 850–1,100 | 400–600 | 14–18A |

#### 2.4.2 Cluster-Level Power Requirements

**Scenario 1: 4×P1S cluster, all printing simultaneously**
- Continuous draw: 4 × 600W (printing avg) = 2,400W = 21.8A @ 110V
- Peak inrush (bed + hotend heating): 4 × 1,200W = 4,800W = 43.6A @ 110V (requires 60A circuit)

**Scenario 2: 4×P1S cluster, staggered printing (2 active, 2 heating)**
- Continuous draw: 2 × 600W (active) + 2 × 1,000W (heating) = 3,200W = 29A @ 110V
- Peak: 40A @ 110V (requires 50A circuit)

**Scenario 3: 8×P1S cluster, all printing simultaneously**
- Continuous: 8 × 600W = 4,800W = 43.6A @ 110V (exceeds single-circuit limit)
- Must use 240V supply: 4,800W / 240V = 20A (standard 30A circuit sufficient)

#### 2.4.3 Circuit Breaker & Electrical Recommendations

| **Cluster Size** | **Recommended Circuit** | **Voltage** | **Breaker Size** | **Cable Gauge** | **Cost** |
|---|---|---|---|---|---|
| **2-printer** | Single circuit | 110V | 20A standard | 12 AWG | $0 (use existing) |
| **4-printer** | Dedicated circuit OR 240V | 110V (if separate circuit) OR 240V | 50A @ 110V OR 30A @ 240V | 8 AWG @ 110V, 10 AWG @ 240V | $200–400 |
| **6–8 printer** | 240V preferred | 240V | 50–60A | 6 AWG | $400–800 |

**Staggering strategy**: Program print start times with 10–15 minute offsets to avoid simultaneous bed heating. Example:
- Printer 1: Start at 00:00 (heat bed 00:00–00:10)
- Printer 2: Start at 00:15 (heat bed 00:15–00:25)
- Printer 3: Start at 00:30 (heat bed 00:30–00:40)
- Printer 4: Start at 00:45 (heat bed 00:45–00:55)

This reduces peak inrush from 43.6A to ~25A (acceptable on a single 30A 110V circuit).

**Recommended for Phase 2**: Install dedicated 50A @ 240V circuit ($600 install + permit). This eliminates staggering complexity and ensures headroom for Phase 3 expansion.

#### 2.4.4 UPS (Uninterruptible Power Supply) Sizing

At $25/unit revenue and 30 minutes of unfinished prints @ 4 printers = $50 worth of in-progress work, a UPS is justified to prevent print loss during brief power interruptions.

| **Cluster Size** | **UPS Capacity (W)** | **Runtime (minutes)** | **Cost** | **Recommended** |
|---|---|---|---|---|
| **1 printer** | 1,500W (1.5 kVA) | 10–15 min | $150–200 | Optional |
| **2 printers** | 2,500W (2.5 kVA) | 8–10 min | $300–400 | Recommended |
| **4 printers** | 4,000W (4 kVA) | 8–10 min | $600–900 | Strongly recommended |
| **8 printers** | 8,000W (8 kVA) | 8–10 min | $1,500–2,000 | Required |

**Benefit**: 10 minutes runtime allows completion of current layer and safe printer shutdown (preventing nozzle blockage).

**Recommended for Phase 2**: 1× 3 kVA UPS ($400) per 4-printer cluster. Total investment: $400–800 for dual redundancy.

---

### 2.5 Space Planning Layout Diagram (4-Printer Phase 2 Example)

```
OVERHEAD VIEW — Phase 2 (4-printer cluster setup)
Scale: 1 cell = 2 feet

         ENTRY/OFFICE
            ↑
      
    CEILING CONDUIT (power, Ethernet, fume duct)
    ────────────────────────────────

    [P1S]  18"   [P1S]      QC & PACKAGING BENCH (6×4 ft)
    [#1]         [#2]       ├─ Digital calipers
    
    [P1S]  18"   [P1S]      ├─ Postprocessing tools
    [#3]         [#4]       ├─ Poly mailers, labels
                             ├─ Thermal printer
    FLOOR:                   └─ Scale & measuring device
    ├─ Power strip (6-outlet)   
    ├─ Ethernet switch (PoE)    
    ├─ UPS backup battery       
    ├─ Dehumidifier
    └─ Filament dry box (mounted on wall at eye level)

    WALL (rear):
    ├─ Filament storage shelf (4-tier, wall-mounted)
    ├─ Tool pegboard
    └─ Maintenance log whiteboard
    
    WINDOW (for fume extraction duct exhaust):
    └─ Fume extractor + HEPA filter (mounted above printers)

Total footprint: 10 ft (width) × 8 ft (depth) = 80 sq ft
With QC bench: 80 + 25 = 105 sq ft (small bedroom or garage section)
```

---

## 3. Supply Chain Optimization

### 3.1 Filament Procurement at Scale

Based on SUPPLIER_NEGOTIATION_PLAYBOOK.md (May 2026 pricing), procurement cost-per-kg evolves dramatically with volume.

#### 3.1.1 Cost per Unit vs. Order Quantity

Assumes PLA+ at primary supplier (eSUN or Prusament) + backup diversity (MatterHackers, Amazon Basics).

| **Volume Tier** | **100 kg/month** | **500 kg/month** | **1,000 kg/month** | **2,000 kg/month** |
|---|---|---|---|---|
| **Cost per kg (primary)** | $12–14 | $10–11 | $9–10 | $8–9 |
| **Cost per 75g clip** | $0.90–$1.05 | $0.75–$0.83 | $0.68–$0.75 | $0.60–$0.68 |
| **Backup supplier premium** | 5–10% higher | 3–5% higher | 2–3% higher | 1–2% higher |
| **Monthly material cost (100-unit baseline)** | $2,160–$2,520 | $1,800–$1,980 | $1,632–$1,800 | $1,440–$1,632 |

**Pricing negotiation strategy**:

1. **Month 0–3 (0–100 kg/month)**: Use eSUN 10 kg bundles @ $12/kg via Amazon Prime. No bulk discount negotiation needed.
2. **Month 4–6 (100–300 kg/month)**: Contact eSUN wholesale or Prusament direct. Negotiate tiered pricing: $11/kg @ 100kg, $10/kg @ 200kg, $9.50/kg @ 300kg commitment. Lock in 6-month agreement.
3. **Month 7–12 (300–750 kg/month)**: Activate secondary supplier (Overture or Anycubic) at 30–50% of volume to reduce single-supplier risk. Maintain negotiated rates with primary.
4. **Month 13+ (750+ kg/month)**: Consider direct China import (JinmuFilament, eSUN direct bulk). Lead time: 4–6 weeks. Requires $5,000+ prepayment and import duty management.

#### 3.1.2 Inventory Carrying Costs

| **Phase** | **Target Inventory** | **Shelf Space** | **Cost per Month** | **Rationale** |
|---|---|---|---|---|
| **Phase 1 (1 printer)** | 10 kg (~2 weeks) | 0.5 cu ft (1 bin) | $15 (desiccant only) | Just-in-time; fast supplier turnaround |
| **Phase 2 (2–4 printers)** | 30 kg (~4 weeks) | 2 cu ft (dry box) | $50 (dry box maintenance) | Buffer against 2-week lead times |
| **Phase 3 (6–8 printers)** | 100 kg (~6 weeks) | 5 cu ft (wall shelf + cabinet) | $150 (dry cabinet + desiccant) | Protection against tariff disruptions |

**Decision gate**: At Phase 3, evaluate import direct (4–6 week lead time) vs. domestic warehouse (1–2 week lead time). If tariffs increase >20%, direct import becomes cost-effective despite higher working capital.

---

### 3.2 Consumables Replacement Schedule

#### 3.2.1 Hotend & Nozzle Wear

| **Component** | **P1S Wear Interval** | **Replacement Cost** | **Annual Cost (4-printer cluster)** | **Trigger for Replacement** |
|---|---|---|---|---|
| **Nozzle (0.4mm)** | 600–800 print hours | $3–5 (hardened steel) | $30–60 (16–20 nozzles/year) | Under-extrusion, visible scoring on nozzle face |
| **Heating cartridge** | 1,500–2,000 hours | $12–18 | $30–45 (2–3 per year) | Slow heat-up (>5 min to 220°C), temperature swings |
| **Thermistor** | 2,000+ hours | $8–12 | $20–30 (2–3 per year) | Temperature reading errors, fluctuation >5°C |
| **PTFE tube (hotend)** | 1,000 hours | $5–8 | $40–60 (8–10 per year for active use) | Discoloration, jamming, visible degradation |

**Preventive maintenance schedule**:
- **Weekly**: Inspect nozzle visually; if white residue visible, soak in acetone overnight and scrub gently
- **Monthly**: Measure nozzle dimensions with micrometer; replace if >0.01mm drift from 0.4mm spec
- **Every 500 hours**: Proactive nozzle swap (before failure) = $3–5 cost, prevents print failures
- **Every 1,500 hours**: Proactive heating cartridge replacement + thermistor check

**Cost avoidance math**: 1 failed print = $5–10 material loss + 2 hours labor (reprint + diagnosis) = $40–50 total cost. Proactive $3 nozzle replacement every 500 hours is 10:1 ROI.

#### 3.2.2 Bed Surface Degradation

| **Component** | **Bambu P1S Spec** | **Wear Interval** | **Replacement Cost** | **Annual Cost (4-printer)** |
|---|---|---|---|---|
| **PEI print surface** | Adhesive-backed PEI sheet | 6–9 months @ high use | $60–80 | $240–320 (4 sheets/year) |
| **Spring steel baseplate** | Magnetic attachment | 18–24 months | $40–60 | $40–60 (1 replacement per 2 years) |
| **Adhesion promoter** | Bambu Labs proprietary | Monthly reapplication | $15–20/bottle (lasts 2–3 months) | $80–100 |

**Bed maintenance schedule**:
- **After every 50 prints**: Wipe bed with lint-free cloth + IPA (isopropyl alcohol) to remove dust
- **Every 200 prints**: Full acetone wash (removes accumulated oils)
- **Every 2–3 months**: Inspect PEI for bubbles or worn spots; replace if >3 small spots visible
- **Every 6–9 months**: Full PEI replacement + adhesion promoter reapplication

**Cost tracking**: Log bed change dates in QC spreadsheet. At 4 printers × 200 prints/month = 800 prints/month shared bed cost = $60–80 / 800 prints = $0.075–0.10 per print (built into COGS).

#### 3.2.3 Spare Parts Inventory

**Critical spares list for Phase 2 (4-printer cluster)**:

| **Part** | **Unit Cost** | **Reorder Level** | **Safety Stock** | **Annual Cost** |
|---|---|---|---|---|
| Nozzle (0.4mm hardened) | $3–5 | <5 on hand | 10 units | $30–50 |
| Heating cartridge | $12–18 | <2 on hand | 4 units | $48–72 |
| Thermistor | $8–12 | <2 on hand | 4 units | $32–48 |
| PTFE tube (hotend) | $5–8 | <2 on hand | 4 units | $20–32 |
| PEI bed sheet | $60–80 | <1 on hand | 2 sheets | $120–160 |
| Spring steel baseplate | $40–60 | <1 on hand | 1 extra | $40–60 |
| Bed springs (set of 4) | $15–20 | <1 set | 2 sets | $30–40 |
| Drive belts (XY/Z) | $20–30/set | <1 set | 2 sets | $40–60 |
| Bearings (linear) | $10–15 each | <2 | 4 units | $40–60 |

**Breakeven analysis**: Holding $500 in critical spare parts costs $500 × 0.25 (annual carrying cost) = $125/year. A single printer down for 24 hours = 100–150 lost units = $2,500–3,750 lost revenue. Breakeven: 3 days of downtime prevented per year.

**Recommended policy**: Stock all items listed above. Establish a monthly reorder trigger at 40% of safety stock level.

---

### 3.3 Filament Storage & Inventory Rotation (FIFO)

**System**: Google Sheets or Craftybase inventory tracker.

| **Column** | **Purpose** | **Example** |
|---|---|---|
| **Date Received** | Timestamp for FIFO rotation | 2026-05-14 |
| **Supplier** | Track supplier performance | eSUN / Prusament / MatterHackers |
| **Color** | SKU mapping for production | Black, White, Grey, Translucent |
| **Quantity (kg)** | Initial weight | 10 kg |
| **Spool Count** | For batch-level tracking | 10 spools × 1kg |
| **Storage Location** | Bin/shelf for retrieval | Dry Box #1, Shelf A |
| **Humidity at Receipt (%)** | QC gate 1 check | 3–5% |
| **Status** | Open / Sealed / In Use / Depleted | Sealed |
| **Date Opened** | Trigger desiccant refresh | 2026-05-20 |
| **Expiration** | 6 months from opening (industry guideline) | 2026-11-20 |

**Inventory rotation rule**: 
- All new stock goes to the **back** of the dry box
- Print jobs always pull from the **front** (oldest first, FIFO)
- When opening a new spool, note date and refresh desiccant packs
- Discard any filament older than 6 months from opening (unlikely to perform well)

**Monthly inventory audit** (10 minutes):
1. Count all spools in dry box
2. Verify count matches spreadsheet (recount if variance >5%)
3. Check humidity reading on dry box; if >20%, replace desiccant immediately
4. Note any opened spools approaching 6-month expiration; prioritize use

---

## 4. Production Workflow Scaling

### 4.1 Batch Processing Optimization

**Challenge at 4+ printers**: Without orchestration, operators can create bottlenecks (all printers waiting for post-processing, or prints stacking while QC is backlogged).

#### 4.1.1 Parallel vs. Sequential Batch Scheduling

**Scenario 1: Sequential (avoid this)**
```
Order 1 (100 clips) → Print on P1S #1 (10 hours)
                   → Post-process + QC (2 hours)
                   → Pack + ship (1 hour)
Order 2 → Print on P1S #2 (10 hours)
       → Post-process + QC (2 hours)
       → Pack + ship (1 hour)

Total time for 2 orders: 26 hours
Revenue: 2 × $25 = $50 / 26 hours = $1.92/hour
```

**Scenario 2: Parallel (recommended)**
```
Orders 1–4 arrive simultaneously (4 × 100 clips each = 400 clips)
Queue all 4 print jobs on P1S #1–4 (start times staggered by 2 minutes)
All 4 print simultaneously (10 hours total clock time, not sequential)
Post-process in parallel: 2-hour window (rotate operators across 4 batches)
QC in parallel: 30 minutes per batch (sample check)
Pack in parallel: 30 minutes per batch (2 operators)

Total time for 4 orders: 13 hours (post-process overlaps with print finish)
Revenue: 4 × $25 = $100 / 13 hours = $7.69/hour
Throughput gain: 4x improvement in revenue per hour
```

#### 4.1.2 Print Job Queue Management

**Tool**: SimplyPrint (free tier, up to 2 printers; $10/month for 3–10) or spreadsheet-based (Google Sheets if <50 orders/month).

**Queue structure**:
```
OrderID | Customer | SKU | Quantity | Filament Color | Printer Assigned | Est. Print Time | Start Time | End Time | Status
———————
1234    | Smith    | Clip-B | 50 | Black | P1S #1 | 10h | 00:00 | 10:00 | PRINTING
1235    | Johnson  | Rail  | 20 | White | P1S #2 | 8h  | 00:15 | 08:15 | QUEUED
1236    | Williams | Clip-B | 30 | Black | P1S #3 | 6h  | 00:30 | 06:30 | QUEUED
1237    | Brown    | Clip-B | 40 | Grey  | P1S #4 | 8h  | 00:45 | 08:45 | QUEUED
```

**Scheduling rules**:
1. Group same SKU + color together (amortizes setup cost for filament/nozzle changes)
2. Assign jobs to printers to balance runtime (no printer idle while others print)
3. Stagger print starts by 10–15 minutes to smooth power demand
4. Prioritize oldest orders first (FIFO by order date, not SKU)

**Example: Load-balanced 4-printer queue (May 28, 2026)**
```
08:00 – P1S #1 starts Clip-B Black (100 units, 10 hrs) → ends 18:00
08:10 – P1S #2 starts Rail White (50 units, 8 hrs) → ends 16:10
08:20 – P1S #3 starts Clip-B Black (80 units, 8h) → ends 16:20
08:30 – P1S #4 starts Clip-C Grey (60 units, 7h) → ends 15:30

16:10 – P1S #2 available; load next job (Clip-A Green, 50 units, 5h) → ends 21:10
15:30 – P1S #4 available; load next job (Clip-C Black, 90 units, 9h) → ends 00:30
16:20 – P1S #3 available; load next job (Rail Black, 40 units, 6h) → ends 22:20
18:00 – P1S #1 available; load next job (Clip-B White, 70 units, 7h) → ends 01:00

Result: 4-printer cluster runs nearly 24/7 with minimal idle time, printing 490 units in ~17 hours
```

#### 4.1.3 Multi-Material Batch Scheduling (AMS Strategy)

**Problem**: Switching PLA colors requires either (a) purging (waste $0.50–$1 worth of filament), or (b) sequential batching (filament stays loaded between jobs).

**Recommended for Phase 2**: 
- **Batch 1 (08:00–10:00)**: All BLACK clips + rails (uses black filament across P1S #1 + #3)
- **Purge + swap (10:00–10:15)**: Drain residual black, prime white, verify color output
- **Batch 2 (10:15–12:15)**: All WHITE clips + rails (uses white filament across P1S #2 + #4)
- **Repeat**: Batch 3 = GREY, Batch 4 = alternate colors

**Cost of this strategy**: ~4 filament swaps/day × $0.75 purge waste = $3/day = $60/month. At $25/unit revenue, this is acceptable (<0.3% of revenue).

**AMS benefit at Phase 3+**: X1C includes 4-color AMS (no purging needed, automatic color changes). Running X1C in the farm eliminates color-change friction entirely but adds $600 to hardware cost (breakeven at ~800 multi-color units/month).

---

### 4.2 Quality Control Procedures (3-Stage Model)

#### 4.2.1 Stage 1: Incoming Filament Inspection (Pre-Production)

**Timing**: Upon delivery from supplier. Takes 20 minutes per delivery.

**Checklist**:
```
☐ Visual inspection: No external damage, seal intact, no moisture condensation
☐ Diameter check: 5-point measurement with calipers, all within 1.72–1.78mm
☐ Flexibility test: Unwind 50cm, bend to 30°, confirm no brittleness
☐ Log result: Supplier / Date / Color / QC Pass/Fail
☐ If fail: Contact supplier for replacement; use backup supplier if waiting >3 days
```

**Decision gate**: Release to dry storage only if all 3 tests pass.

#### 4.2.2 Stage 2: Pre-Production Validation Print (First Batch per Supplier)

**Timing**: Before using new supplier filament for customer orders. Takes 2 hours.

**Procedure**:
1. Load new filament into AMS slot 1
2. Print 1 unit of highest-demand SKU (e.g., Clip-B) with production settings (220°C, 60 mm/s, 100% infill)
3. Inspect: Surface finish, layer adhesion, color uniformity
4. Measure critical dimensions with calipers (snap arm width, clip opening, tolerance ±0.02mm)
5. Mechanical test: Snap-arm flexibility at 60° bend (should flex, not shatter)
6. Log result: Supplier / Material Lot / Dimensions / Pass/Fail
7. If pass: Release filament to production. If fail: Discard batch or return to supplier.

**Failure modes & troubleshooting**:
- **Under-extrusion** (insufficient material): Increase hotend temp by 5°C or reduce print speed by 10%
- **Over-extrusion** (blobs/strings): Decrease hotend temp by 5°C or increase print speed by 10%
- **Brittleness** (cracks during mechanical test): Filament is too dry; refresh desiccant or reject batch
- **Discoloration** (darkening mid-print): Nozzle is too hot; reduce temp by 10°C

#### 4.2.3 Stage 3: Batch Sampling During Production

**Timing**: Continuous during customer order production. Takes 5 minutes per 50 units.

**Procedure**:
```
For every 50 units printed:
  ☐ Randomly select 1 unit from the batch
  ☐ 30-second visual check: Surface finish, layer adhesion
  ☐ Dimensional check: Measure critical dimension (e.g., snap-arm width)
  ☐ If within spec: Release batch to post-processing
  ☐ If out of spec: STOP production, diagnose root cause:
      - Nozzle clogging? → Clean/replace nozzle, retest
      - Print settings drift? → Check slicer profile, reload from template
      - Filament quality? → Check diameter, humidity
  ☐ Log result: Batch ID / Unit sampled / Dimension / Pass/Fail / Action
```

**Defect classification**:
- **Minor** (<1%): Surface blemishes, layer lines (acceptable, ship as-is)
- **Major** (1–5%): Dimensional out-of-spec (±0.05mm), weak snap arm (reprint)
- **Critical** (>5%): Cracks, voids, non-functional (scrap, investigate root cause)

**Monthly QC review**: Aggregate defect data to identify trends:
- If 80%+ of defects are supplier-related (diameter variance): Contact supplier, request replacement
- If 80%+ are printer-related (nozzle scoring, temperature swings): Perform preventive maintenance
- If defect rate >5%: Pause production, diagnose before continuing

---

### 4.3 Packaging Throughput at Scale

| **Phase** | **Orders/Day** | **Units/Order** | **Packaging Time/Unit** | **Daily Packaging Time** | **Staffing** |
|---|---|---|---|---|---|
| **Phase 1 (single printer)** | 2–3 | 25–50 | 90 sec | 45–90 min | Solo operator |
| **Phase 2 (2–4 printers)** | 5–10 | 25–50 | 90 sec | 2–4 hours | 1 person (dedicated afternoons) |
| **Phase 3 (6–8 printers)** | 15–25 | 25–50 | 60 sec (batched) | 4–6 hours | 1–2 part-time staff |

**Packaging SOP for Phase 2 (4-printer cluster, 200 units/day)**:

1. **08:00–09:00**: Harvest prints from printers (30 minutes), initial QC check (30 min)
2. **09:00–10:00**: Batch poly mailers, tissue, thank-you cards by order (prep 20 packages)
3. **10:00–11:00**: Pack 20 units + affix labels (60 sec per order × 20 = 20 min; rest is batching)
4. **11:00–12:00**: Generate USPS labels in Pirate Ship, batch for pickup
5. **Repeat** 2x/day for 200-unit daily throughput

**Efficiency lever**: Pre-batch packaging materials during print idle time (when printers are between jobs). Stock 20 poly mailers + tissue + card per tray, ready to grab during harvest window. This reduces active packing time by 25%.

---

## 5. Labor & Automation Requirements

### 5.1 Operator Role Definition (4–8 Printer Farm)

**Job description**: Print Farm Operator (multi-skilled production role)

| **Task** | **Frequency** | **Time per Task** | **Daily Load** | **Weekly Load** |
|---|---|---|---|---|
| Print queue monitoring (visual checks) | Every 2 hours | 5 min | 40 min | 4 hrs |
| Filament swap + nozzle clean | 1–2× per day | 15 min | 30 min | 2.5 hrs |
| Pause/resume handling (print errors) | 2–3× per week | 10 min | 15 min | 1 hr |
| Print harvest + initial QC | 2× per day (morning + afternoon) | 30 min | 60 min | 5 hrs |
| Post-processing (support removal, cleaning) | Continuous (during print time) | 2 min per unit | 1.5 hours @ 200 units/day | 7.5 hrs |
| Packaging + labels | Batch after prints finish | 1.5 min per order | 2 hours @ 100 orders/day | 10 hrs |
| Dimensional QC sampling | 1 per 50 units | 3 min | 12 min | 1 hr |
| Equipment maintenance (nozzle inspection, bed cleaning) | Daily | 10 min | 10 min | 1 hr |

**Total weekly time @ 4-printer Phase 2 cluster (200–300 units/day)**: ~32 hours

**Staffing model**:
- **Phase 2** (200 units/day): 1 full-time operator (40 hrs/week) + weekend coverage (8 hrs) = 1 FTE
- **Phase 3** (400–600 units/day): 1.5–2 FTE needed
  - Operator 1: Print queue management + equipment maintenance
  - Operator 2: Post-processing + packaging (can be part-time, 20–30 hrs/week)

**Wage assumptions**:
- Full-time operator: $18–22/hr (skilled print farm tech) = $900–1,100/week
- Part-time post-processing: $15–18/hr (less skilled) = $300–540/week

**Monthly labor cost**:
- Phase 2 (1 FTE): $3,600–4,400/month
- Phase 3 (1.5–2 FTE): $5,400–9,000/month

---

### 5.2 Post-Processing Bottleneck Analysis

**Problem**: At high volumes, print removal and post-processing becomes the constraint, not printing.

| **Activity** | **Time per Unit** | **100 units/day** | **400 units/day** | **Bottleneck?** |
|---|---|---|---|---|
| Print removal from bed | 20 sec | 33 min | 2.2 hrs | No (parallel across 4 printers) |
| Support removal (if applicable) | 2 min | 3.3 hrs | 13+ hrs | YES (serial, skilled labor) |
| Cleaning + deburring | 30 sec | 50 min | 3.3 hrs | Maybe (if extensive cleaning) |
| Inspection + dimensional check | 15 sec | 25 min | 1.7 hrs | No |
| Packaging | 90 sec | 2.5 hrs | 10 hrs | YES (high volume) |

**Mitigation strategies**:

1. **Reduce support design** (Phase 0–1): Design clips with minimal supports (undercut overhangs avoided via design). Saves 50% post-processing time per unit.

2. **Support removal automation** (Phase 2+): Evaluate tumbler deburring system ($800–1,500) or water jet post-processing ($3,000+). ROI: Saves 1.5 min/unit. At 400 units/day = 10 hours/day saved = 50 hours/month.

3. **Dedicated post-processing operator** (Phase 2+): Hire 1 part-time staff member (20 hrs/week @ $15/hr = $1,200/month) to focus purely on support removal and packaging. This frees up lead operator for queue management and equipment maintenance.

4. **Pre-staging post-processing materials**: During print time, pre-sort completed units by order, lay out packaging materials. This allows rapid packing once prints are cool.

---

### 5.3 Automation ROI Analysis

#### 5.3.1 Robotic Print Removal ($15K–$25K)

**Option**: Greydon Autonomous Print Removal System (3D printer arm + vacuum gripper + conveyor)

| **Cost Component** | **Amount** |
|---|---|
| Robotic arm (used SCARA or Cobot) | $8,000–$15,000 |
| End-effector (vacuum gripper + camera) | $3,000–$5,000 |
| Conveyor + pallet system | $2,000–$4,000 |
| Control software + integration | $1,000–$2,000 |
| **Total system cost** | **$14,000–$26,000** |

**Payback calculation** (Phase 2, 4-printer):
- Current labor for print removal: 20 sec × 200 units/day = 1.1 hrs/day = 5.5 hrs/week = 22 hrs/month @ $20/hr = $440/month
- Automation saves: $440/month × 80% (leaving human oversight) = $352/month
- Payback period: $20,000 / $352 per month = **57 months** (not justified)

**Verdict**: Robotic print removal does NOT justify $20K+ investment at Phase 2 scale. Defer to Phase 4+ (600+ units/day), where labor costs alone exceed $2,000/month.

#### 5.3.2 Automatic Filament Changers ($500–$1,200)

**Option**: EIBOS Multi-Material Extruder (MMU) or Bambu AMS (already included with X1C)

**Cost benefit**:
- Current manual filament swap: 2× per day × 15 min = 30 min/day = 2.5 hrs/week
- Labor cost: 2.5 hrs × $20/hr = $50/week = $200/month
- Automatic changer cost: $800 (one-time)
- Payback: $800 / $200 per month = **4 months** ✅

**Verdict**: Auto-filament changers are justified if running multi-color batches frequently. At Phase 2, **upgrade to Bambu X1C** (includes AMS) rather than adding external MMU to P1S. Cost delta: $600 (X1C $1,299 vs. P1S $699). Payback: 3 months if enabling 20%+ faster color-change batching.

#### 5.3.3 Auto-Nozzle Cleaning / Maintenance Stations ($1,500–$3,000)

**Option**: Bambu Labs offers integrated nozzle cleaning on X1C; aftermarket options for P1S exist.

**ROI**: Marginal. Manual nozzle cleaning takes 5 minutes every 500 hours (not daily). Automation cost is not justified unless it prevents 3+ print failures per month (currently ~1 failure/month in well-maintained farm).

**Verdict**: Skip at Phase 2. Monitor failure rate; if exceeds 2 failures/month due to nozzle issues, revisit.

---

### 5.4 Staffing Model by Phase

| **Phase** | **Monthly Units** | **FTE Required** | **Operator Role** | **Labor Cost/Month** |
|---|---|---|---|---|
| **Phase 1** | 50–100 | 0.5 FTE | Solo: everything (operator + post-process + pack) | $900–$1,100 (if paid contractor) |
| **Phase 2** | 300–600 | 1 FTE | Lead: queue mgmt + maintenance. Post-proc is bottleneck. | $3,600–$4,400 (1 full-time) |
| **Phase 3** | 800–1,500 | 1.5 FTE | Lead + dedicated post-proc tech + part-time packing | $5,400–$7,500 |
| **Phase 4** | 2,000+ | 2–3 FTE | Shift coverage + multi-role redundancy | $9,000–$13,500 |

**Hiring strategy**:
- Phase 2: Recruit 1 full-time production technician (6–12 week lead time for training)
- Phase 3: Add 1 part-time post-processing specialist (flexible schedule, focused on high-volume activities)
- Phase 4: Add evening shift coordinator or second full-time operator for redundancy

---

## 6. Financial Modeling & Scaling Phases

### 6.1 Revenue Projections per Printer

Based on cost-model-spreadsheet.csv (May 2026) and PRE_LAUNCH_FULFILLMENT_WORKFLOW.md projections.

**Single P1S assumptions**:
- Uptime: 80% (320 hours/month active print time)
- Average order: 2–3 units per order
- Average order value (AOV): $24.99 (blended clips + rails)
- Conversion rate: 2–3% (Etsy platform average)

| **Phase** | **Monthly Orders** | **Monthly Units** | **Monthly Revenue** | **COGS** | **Gross Margin %** | **Platform Fees (15% + 3%)** | **Net Revenue** |
|---|---|---|---|---|---|
| **Phase 1a** (Month 1–2) | 10–15 | 30–50 | $300–400 | $120–160 | 60% | $45–60 | $155–235 |
| **Phase 1b** (Month 3–4) | 20–30 | 60–90 | $600–900 | $240–360 | 60% | $90–135 | $315–550 |
| **Phase 1c** (Month 5–6) | 40–60 | 120–180 | $1,200–1,800 | $480–720 | 60% | $180–270 | $630–1,050 |
| **Phase 2 (Month 7–8)** | 60–100 | 180–300 | $1,800–3,000 | $720–1,200 | 60% | $270–450 | $945–1,575 |

**Adding 2nd printer (Phase 1c trigger at ~$1,500/month revenue)**:

With 2× P1S running in parallel:
- Monthly orders: 80–150 (2× single-printer capacity)
- Monthly units: 300–600
- **Monthly revenue: $3,600–$7,500**
- COGS: $1,440–$3,000
- Gross margin: 60%
- Platform fees: $540–$1,125
- **Net revenue: $1,890–$3,938**

---

### 6.2 Breakeven Analysis by Configuration

| **Cluster Config** | **Hardware Cost** | **Monthly Margin (60% COGS)** | **Monthly Payback (months)** |
|---|---|---|---|
| **1× P1S** | $699 | $630–1,050 (@ $1,200–1,800 revenue) | Already broken even in Phase 1c |
| **2× P1S** | $1,398 | $1,890–$3,938 (@ $3,600–7,500 revenue) | <1 month (at Phase 2 volume) |
| **4× P1S** | $2,796 | $3,780–$7,875 (@ $7,200–15,000 revenue) | <1 month at Phase 3 volume |
| **8× P1S** | $5,592 | $7,560–$15,750 (@ $14,400–30,000 revenue) | <1 month at Phase 4 volume |

**Key insight**: Hardware cost is negligible relative to monthly margin at production scale. The decision to add printers should be driven by **order demand**, not hardware cost.

---

### 6.3 Scenario Analysis: 3 Demand Trajectories

#### 6.3.1 Conservative Scenario (60% of projections)

Assumes slower Etsy growth, lower conversion rate (1.5% vs. 2.5%), seasonal demand dips.

| **Month** | **Units Sold** | **Revenue** | **COGS (40%)** | **Platform Fees (18%)** | **Labor** | **Net Profit** |
|---|---|---|---|---|---|
| Month 1 | 20 | $500 | $200 | $90 | $0 | $210 |
| Month 2 | 30 | $750 | $300 | $135 | $0 | $315 |
| Month 3 | 40 | $1,000 | $400 | $180 | $0 | $420 |
| Month 4 | 50 | $1,250 | $500 | $225 | $0 | $525 |
| Month 5 | 60 | $1,500 | $600 | $270 | $200 (part-time) | $430 |
| Month 6 | 70 | $1,750 | $700 | $315 | $400 | $335 |
| **6-month cumulative** | **270 units** | **$6,750** | **$2,700** | **$1,215** | **$600** | **$2,235** |

**Scaling trigger NOT MET**: Revenue plateaus below $5K/month; do not add 2nd printer. Instead, optimize current setup for margin improvement.

#### 6.3.2 Realistic Scenario (100% baseline)

Assumes moderate Etsy growth, 2–2.5% conversion, stable seasonal demand.

| **Month** | **Units Sold** | **Revenue** | **COGS (40%)** | **Platform Fees (18%)** | **Labor** | **Net Profit** |
|---|---|---|---|---|---|
| Month 1 | 30 | $750 | $300 | $135 | $0 | $315 |
| Month 2 | 50 | $1,250 | $500 | $225 | $0 | $525 |
| Month 3 | 80 | $2,000 | $800 | $360 | $0 | $840 |
| Month 4 | 120 | $3,000 | $1,200 | $540 | $400 | $860 |
| Month 5 | 150 | $3,750 | $1,500 | $675 | $600 | $975 |
| Month 6 | 180 | $4,500 | $1,800 | $810 | $800 | $1,090 |
| **6-month cumulative** | **610 units** | **$15,250** | **$6,100** | **$2,745** | **$1,800** | **$4,605** |

**Scaling trigger MET by Month 5**: Revenue crosses $5K/month. **Decision point**: Add 2nd P1S printer (cost $699, payback <1 month at Phase 2 volume).

#### 6.3.3 Optimistic Scenario (150% of baseline)

Assumes rapid Etsy visibility gain, 3%+ conversion, strong product-market fit, premium pricing possible.

| **Month** | **Units Sold** | **Revenue** | **COGS (40%)** | **Platform Fees (18%)** | **Labor** | **Net Profit** |
|---|---|---|---|---|---|
| Month 1 | 50 | $1,250 | $500 | $225 | $0 | $525 |
| Month 2 | 90 | $2,250 | $900 | $405 | $0 | $945 |
| Month 3 | 150 | $3,750 | $1,500 | $675 | $400 | $1,175 |
| Month 4 | 210 | $5,250 | $2,100 | $945 | $800 | $1,405 |
| Month 5 | 270 | $6,750 | $2,700 | $1,215 | $1,200 | $1,635 |
| Month 6 | 330 | $8,250 | $3,300 | $1,485 | $1,600 | $1,865 |
| **6-month cumulative** | **1,100 units** | **$27,500** | **$11,000** | **$4,950** | **$4,000** | **$7,550** |

**Scaling trigger MET by Month 3**: Add 2nd printer. **Month 4+**: Evaluate 4-printer cluster (Phase 2 expansion).

**Cumulative 12-month projection** (optimistic): 2,200+ units shipped, $55K+ revenue, $12K+ net profit, capacity for 8-printer cluster by Month 12.

---

### 6.4 12-Month P&L Model for 4-Printer Phase 2 Cluster

**Starting month**: Month 9 post-launch (when 2-printer cluster proves demand).

| **Month** | **Units/Month** | **Monthly Revenue** | **Material (35%)** | **Packaging (5%)** | **Filament Waste (5%)** | **Labor (1 FTE)** | **Platform Fees (18%)** | **Equipment Maintenance** | **Net Profit** |
|---|---|---|---|---|---|---|---|---|
| Month 9 | 400 | $10,000 | $3,500 | $500 | $500 | $3,600 | $1,800 | $300 | $800 |
| Month 10 | 500 | $12,500 | $4,375 | $625 | $625 | $3,600 | $2,250 | $350 | $1,675 |
| Month 11 | 600 | $15,000 | $5,250 | $750 | $750 | $3,600 | $2,700 | $400 | $2,550 |
| Month 12 | 750 | $18,750 | $6,563 | $938 | $938 | $4,000 (add part-time) | $3,375 | $450 | $3,486 |
| Month 13 | 900 | $22,500 | $7,875 | $1,125 | $1,125 | $5,200 (1.5 FTE) | $4,050 | $500 | $3,625 |
| Month 14 | 1,050 | $26,250 | $9,188 | $1,313 | $1,313 | $5,200 | $4,725 | $600 | $4,311 |

**12-month subtotal** (4-printer cluster, Months 9–14):
- **Total revenue**: $104,750
- **Total COGS**: $37,351
- **Total labor**: $25,200
- **Total net profit**: $18,449

**Capital requirements for Phase 2 (4-printer)**: $2,796 (hardware) + $500 (enclosure) + $400 (monitoring) + $800 (spare parts) = **$4,496 total investment**, recovered in Month 10.

---

## 7. 24-Month Scaling Phase Timeline & Decision Gates

### 7.1 Phase Structure & Revenue Triggers

```
PHASE 0 (Months 0–3): CURRENT STATE — Single Printer Validation
├─ Goal: Prove product-market fit, establish operational baseline
├─ Revenue target: $1,000–$2,000/month by Month 3
├─ Decision gate (Month 3): Revenue >$1,500/month?
│  ├─ YES → Proceed to Phase 1
│  └─ NO → Reassess product, pricing, or marketing

PHASE 1 (Months 4–8): TWO-PRINTER EXPANSION
├─ Goal: 2× capacity to capture surging demand
├─ Hardware: Add 2nd Bambu P1S ($699)
├─ Revenue target: $5,000–$7,500/month by Month 8
├─ Decision gate (Month 8): Revenue >$5,000/month sustained (2+ months)?
│  ├─ YES → Proceed to Phase 2 (4-printer cluster)
│  └─ NO → Remain at 2-printer; optimize margins instead

PHASE 2 (Months 9–14): FOUR-PRINTER CLUSTER
├─ Goal: Establish production farm baseline, refine workflows
├─ Hardware: Add 2 more P1S units ($1,398); optional 1×X1C ($1,299) for specialty SKUs
├─ Revenue target: $15,000–$20,000/month by Month 14
├─ Staffing: Add 1 full-time operator + part-time post-processing
├─ Decision gate (Month 14): Revenue >$15,000/month sustained?
│  ├─ YES → Proceed to Phase 3 (8-printer farm)
│  └─ NO → Maintain 4-printer cluster; explore adjacent product lines

PHASE 3 (Months 15–24): EIGHT-PRINTER FARM
├─ Goal: Multi-shift operations, adjacent manufacturing exploration
├─ Hardware: Add 4 more P1S units ($2,796); or hybrid (2×P1S + 2×X1C)
├─ Revenue target: $30,000–$50,000/month by Month 24
├─ Staffing: 2–3 FTE across 2 shifts
├─ Decision gate (Month 24): Revenue >$30,000/month sustained?
│  ├─ YES → Explore 3PL fulfillment, multi-SKU expansion, adjacent tech (resin, nylon)
│  └─ NO → Maintain 8-printer cluster; focus on margin improvement
```

---

### 7.2 Resource Allocation by Phase (Hours per Week for Orchestration)

| **Phase** | **Months** | **Revenue** | **Orchestrator Hours/Week** | **Primary Activity** |
|---|---|---|---|---|
| **Phase 0** | 0–3 | $1,000–$2,000 | 5–10 hrs | Supplier negotiation, listing optimization, process documentation |
| **Phase 1** | 4–8 | $5,000–$7,500 | 15–20 hrs | 2nd printer setup, workflow scaling, operator hiring |
| **Phase 2** | 9–14 | $15,000–$20,000 | 20–30 hrs | Multi-printer orchestration, QC refinement, 3-operator coordination |
| **Phase 3** | 15–24 | $30,000–$50,000 | 30–40 hrs | Farm operations, shift scheduling, adjacent mfg exploration, potential 3PL integration |

**NOTE**: Orchestrator hours reflect direct management/decision-making. Operators handle day-to-day execution.

---

### 7.3 Capital Investment Schedule

| **Phase** | **Months** | **Hardware** | **Infrastructure** | **Staffing** | **Total Capital** | **Cumulative** |
|---|---|---|---|---|---|
| **Phase 0** | 0–3 | $699 (existing P1S) | $200 (filament storage) | $0 | $899 | $899 |
| **Phase 1** | 4–8 | $699 (2nd P1S) | $300 (cables, cooling) | $3,600 (4 mo part-time) | $4,599 | $5,498 |
| **Phase 2** | 9–14 | $1,398 (2×P1S) | $500 (enclosure, UPS, ductwork) | $14,000 (6 mo FTE + part-time) | $15,898 | $21,396 |
| **Phase 3** | 15–24 | $2,796 (4×P1S) | $1,000 (enclosure expansion, HVAC) | $48,000 (10 mo, 2–3 FTE) | $51,796 | **$73,192** |

**Payback timeline**:
- Phase 0: Recovered Month 1 (low cost)
- Phase 1: Recovered Month 2 of Phase 1 (2-printer cluster already profitable)
- Phase 2: Recovered Month 2 of Phase 2 (4-printer generates $15K+ revenue, $3K+ monthly net profit)
- Phase 3: Recovered Month 3 of Phase 3 (8-printer at scale generates $6K–$8K monthly net)

**Total 24-month capital to reach 8-printer farm: ~$73K, recovered by Month 21 if optimistic scenario holds.**

---

### 7.4 Contingency Scaling Rules

**If revenue grows faster than baseline** (e.g., 2× optimistic scenario):
- Accelerate Phase 2 → Phase 3 transition from Month 15 to Month 12
- Add 4 printers immediately instead of staggering
- Hire 2 FTE operators simultaneously rather than incrementally

**If revenue stalls** (e.g., conservative scenario, <$3K/month by Month 6):
- Hold at single printer; do not invest in 2nd printer yet
- Investigate: Is demand limited by Etsy visibility (marketing lever), or by product design (feature lever)?
- Options:
  - Expand SKU variety (add new designs to capture adjacent demand)
  - Pivot to alternate platform (Amazon Handmade, direct sales)
  - Test premium line (PETG printing, specialty colors, higher price point)
- Scaling decision revisited at Month 9

**If operational bottleneck identified** (e.g., post-processing consistently 2+ days behind):
- Before adding printers, invest in post-processing efficiency:
  - Hire dedicated post-processing staff ($400–600/month)
  - Evaluate support reduction design changes (0–2 month iteration)
  - Consider outsourcing (e.g., tumbler deburring service $50–100/month)
- Only add printer once post-processing backlog clears

---

## Summary & Next Steps

### Success Criteria for Each Phase

| **Phase** | **Completion Criteria** | **Checkpoint Date** |
|---|---|---|
| **Phase 0** | Single P1S live on Etsy, $1,500+/month recurring, SOP documented | Month 3 (Aug 2026) |
| **Phase 1** | 2 P1S running, $5,000+/month sustained, operator trained | Month 8 (Jan 2027) |
| **Phase 2** | 4 P1S + 1 FTE operator, $15,000+/month, Phase 3 infrastructure planned | Month 14 (Jul 2027) |
| **Phase 3** | 8 P1S + 2–3 FTE team, $30,000+/month, 3PL or adjacent mfg exploration begun | Month 24 (May 2028) |

### Key Documents for Execution

1. **Printer selection**: Use Section 1.4 recommendation (P1S primary, X1C optional at Phase 2+)
2. **Space planning**: Section 2.5 provides 4-printer layout; scale to 8 by adding second 4×2 grid
3. **Supply chain**: Lock Prussian or eSUN at tiered pricing (Section 3.1) before reaching 500 kg/month
4. **Workflow**: Implement SimplyPrint or Obico by Phase 2 (Section 2.3.2)
5. **Staffing**: Begin operator recruitment 4–6 weeks before reaching revenue trigger (Phase 1 → Phase 2)

### Immediate Actions (Next 30 Days)

1. **Month 0**: Confirm single-printer Phase 0 operations are stable (SOP documented, revenue trending >$1,500)
2. **Month 1**: Research 2nd printer availability; pre-order if needed (lead time 1–2 weeks)
3. **Month 2**: Identify suitable production space for 4-printer cluster (visit candidates, confirm electrical service)
4. **Month 3**: Establish supplier relationship with Prussian or eSUN; negotiate pricing structure for 100–300 kg/month volume

---

**Document Status**: Production-ready. Distribute to operations team upon Phase 1 trigger (Month 4+). Update quarterly with actual cost data, lead times, and scaling decisions.

**Total word count**: 4,200 words | **7 major sections** | **Actionable checklists and financial models included**

