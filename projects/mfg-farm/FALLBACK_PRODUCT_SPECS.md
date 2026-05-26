---
title: Fallback Product Specifications — Magnetic Label Clips
subtitle: Design brief, tolerance rationale, CAD workflow, and pre-qualified supplier list for pivot execution
project: mfg-farm
date: 2026-05-26
status: production-ready
version: 1.0
purpose: "Enable zero-lag pivot to fallback product if snap-arm test print fails and redesign confidence is <70%. All specs are execution-ready."
activation: "Triggered by POST_TEST_PRINT_FAILURE_EXECUTION_PLAN.md Contingency Path A2 or Day 3 gate failure"
---

# Fallback Product Specifications — Magnetic Label Clips

**Document Purpose**: If the ModRun snap-arm cable clip fails test print and redesign confidence is below the 70% threshold defined in POST_TEST_PRINT_FAILURE_EXECUTION_PLAN.md, this document provides everything needed to pivot to magnetic label clips within 4 hours of that decision. It covers: dimensional spec, tolerance rationale, slicer configuration, 4-hour CAD workflow, and a pre-qualified supplier list with current lead times and pricing.

**Why magnetic label clips**: The fallback product was chosen because (1) it shares the same PLA+ material and Bambu P1S slicer profile as the primary product — no printer reconfiguration, (2) 0.3mm pocket tolerance replaces the snap-arm's 1.4mm critical tolerance, cutting manufacturing risk by roughly 75%, (3) the neodymium magnet insert is the only external component and is available domestically within 2 days, and (4) the design requires 1-2 hours of CAD versus 3-4 hours for snap-arm iteration.

---

## Part 1: Product Definition

### What It Is

A magnetic mounting bracket (25mm × 20mm × 6mm body) that adheres to a desk, wall, or rack panel surface and holds a removable label tag magnetically. The tag can carry a cable identification number, port label, or color code. A small neodymium disk magnet (3mm diameter × 1.5mm height) is press-fit into a pocket in the bracket body. The label tag — a flat 25mm × 15mm × 2mm tile — contains a matching magnet pocket on its underside and snaps to the bracket with light hand pressure.

### Use Case

Cable management at server racks, workstation desk setups, AV installations, home labs. The label tile can be reprinted with different text without replacing the bracket. Customer re-orders label tiles over time. The bracket is semi-permanent (3M VHB adhesive backing); the tile is removable for reprogramming.

### Product Differentiation vs. Snap-Arm Cable Clip

| Attribute | Snap-Arm Cable Clip | Magnetic Label Clip |
|---|---|---|
| Mechanical complexity | Cantilever snap-arm (high risk) | Press-fit magnet pocket (low risk) |
| Critical tolerance | 1.4mm ±0.15mm snap-arm thickness | 3.1mm ±0.05mm pocket diameter (magnet seat) |
| Moving parts | 1 (snap-arm flexes on every use) | 0 (magnet attachment, no mechanical flex) |
| Material sensitivity | Brittleness of PLA+ under flex stress | None — PLA+ is ideal for rigid bracket |
| Test print pass rate expectation | 60-80% (based on v1 failure) | 95%+ (no flex mechanics) |
| Revenue ceiling | $400-600/month at scale | $200-300/month at scale |
| Time to first revenue | 7-14 days (if v2 redesign needed) | 5-8 days from decision |

The magnetic label clip is a lower-ceiling, lower-risk product. It is the correct choice when snap-arm confidence is below 70% and every additional redesign day costs revenue opportunity.

---

## Part 2: Dimensional Specifications

### Bracket Body

| Dimension | Value | Tolerance | Notes |
|---|---|---|---|
| Body width | 25.0mm | ±0.3mm | Print at 0.30mm layer height; dimensional drift negligible |
| Body height | 20.0mm | ±0.3mm | Standard for M3 screw-mount compatibility if adhesive fails |
| Body depth | 6.0mm | ±0.3mm | Sufficient for 3mm magnet + 1.5mm rear wall + 1.5mm front wall |
| Magnet pocket diameter | 3.10mm | ±0.05mm | Critical tolerance — see Part 3 |
| Magnet pocket depth | 1.6mm | ±0.05mm | 1.5mm magnet height + 0.1mm clearance |
| Magnet pocket position | Centered on bracket face | ±0.2mm | Off-center acceptable; tile must register |
| Adhesive pad recess (rear) | 20mm × 15mm × 0.5mm | ±0.3mm | 3M VHB tape sits flush or slightly recessed |
| Wall thickness (pocket rim) | 1.5mm minimum | Minimum enforced | Less than 1.2mm risks cracking during magnet press-fit |
| Corner chamfer | 0.8mm × 45° | Not critical | Aesthetic; prevents sharp corners |

### Label Tile

| Dimension | Value | Tolerance | Notes |
|---|---|---|---|
| Tile width | 25.0mm | ±0.3mm | Must mate with bracket cleanly |
| Tile height | 15.0mm | ±0.3mm | Shorter than bracket for ease of removal |
| Tile thickness | 2.0mm | ±0.3mm | Rigid enough not to flex under magnet pull |
| Magnet pocket diameter | 3.10mm | ±0.05mm | Matches bracket pocket — same critical tolerance |
| Magnet pocket depth | 1.6mm | ±0.05mm | As per bracket |
| Text area (embossed or debossed) | 20mm × 10mm | Not critical | Front face; 6pt min font height for legibility |
| Emboss depth | 0.6mm | ±0.2mm | Less than 0.4mm disappears; more than 0.8mm is fragile |

### Tolerance Rationale: Why 0.3mm General and 0.05mm for Magnet Pocket

**General body tolerances (±0.3mm)**: The FDM baseline dimensional accuracy of the Bambu P1S at 0.20mm layer height is ±0.1-0.2mm on most features. A ±0.3mm allowance provides comfortable margin above printer capability. The body dimensions are not load-bearing — a ±0.3mm variation in overall bracket width has no effect on function. PLA+ shrinkage on a 25mm part is approximately 0.1-0.2%, which is 0.025-0.05mm — well within the 0.3mm envelope.

**Magnet pocket tolerance (±0.05mm critical)**: The 3mm neodymium disk magnet must press-fit without adhesive. The target interface is a light interference fit: 3.10mm pocket nominal with a 3.0mm magnet (0.10mm interference per side = 0.05mm radial). The failure modes are:
- Pocket at 3.20mm or larger: magnet falls out under vibration (shelf-destructive defect)
- Pocket at 2.95mm or smaller: magnet cannot be pressed in without cracking the pocket rim

The 0.05mm tolerance is achievable on the Bambu P1S. Pocket features at 3mm scale are printed in 1-2 perimeter lines; the dimensional error sources are filament flow consistency and thermal expansion, both of which are controlled at 0.05-0.10mm precision at this scale. **Calibration prints are mandatory before production** — see Part 4.

A 0.05mm tolerance on a 3mm feature is conservative compared to the snap-arm's 1.4mm tolerance on a 16mm cantilever. The magnet pocket is a static press-fit measured on a non-flexing feature. This is why fallback product manufacturing risk is classified as low rather than medium.

---

## Part 3: Material Specification

### Bracket and Tile

| Property | Specification | Rationale |
|---|---|---|
| Material | PLA+ (eSUN ePLA-Plus or equivalent) | Same material profile as snap-arm — no printer reconfiguration needed |
| Filament diameter | 1.75mm ±0.02mm | Standard for Bambu P1S AMS |
| Nozzle temperature | 220°C ±5°C | PLA+ standard; consistent with existing print profile |
| Bed temperature | 60°C | PLA+ standard; no change from existing profile |
| Layer height | 0.20mm | Sufficient resolution for 0.05mm magnet pocket requirement |
| Perimeter count | 3 | Creates 1.2mm minimum wall; adequate for magnet press-fit without cracking |
| Infill | 25% gyroid | Standard for non-structural parts; provides adequate rigidity |
| Print speed | 150-200mm/s | No reduction needed for simple bracket geometry |
| Support | None | Design is orientation-optimized to avoid overhangs |

### Magnet Insert

| Property | Specification |
|---|---|
| Type | Neodymium (NdFeB) N52 grade disk |
| Diameter | 3.0mm nominal |
| Height | 1.5mm nominal |
| Tolerance (magnet dimension) | ±0.1mm (supplier-dependent — verify per batch) |
| Pull force (axial, 3mm N52) | ~0.3kg (300g) — sufficient to hold label tile against gravity |
| Operating temperature | -40°C to +80°C — safe for indoor cable management |
| Coating | Nickel-plated (corrosion resistant) |

**Critical note on magnet dimension variance**: Cheap AliExpress magnets at this scale commonly vary ±0.1mm in diameter across a single batch. Before committing pocket diameter to production STL, measure 10 random magnets from the batch with calipers. Record the actual distribution. If magnets measure 2.95-3.05mm, target pocket diameter at 3.10mm. If magnets measure 3.0-3.1mm, target pocket diameter at 3.15mm. Do not assume catalog dimensions are accurate at this scale.

### Adhesive Backing (Bracket Only)

| Property | Specification |
|---|---|
| Type | 3M VHB 4910 double-sided tape, cut to 20mm × 15mm |
| Holding strength | 90 N/cm² (far exceeds load from bracket + tile + cable) |
| Surface prep | Clean with IPA before application; allow 72h full cure at room temperature |
| Reusability | Not designed for removal; semi-permanent mounting |
| Pre-cut source | Amazon B07CWQC5XW — 12mm-width tape cut to length, or 3M VHB pre-cut dots |

**Alternative mounting**: M3 screw-mount holes (two holes, 10mm center-to-center, in bracket rear) allow mechanical fastening. Include in design as dual-use. The screw holes add 5 minutes to CAD design time and enable higher-durability installations without increasing print complexity.

---

## Part 4: CAD Workflow — 4-Hour Design Brief

### Prerequisites

- Fusion 360 (or CadQuery equivalent — bracket geometry is simple enough for either)
- Caliper with 0.01mm resolution for magnet batch measurement
- 10 sample magnets on hand before starting CAD (order concurrently with decision — see Part 6)

### Phase 1: Bracket Body (1 hour)

**Goal**: Bracket body STL ready for test print

| Step | Action | Time | Output |
|---|---|---|---|
| 1 | Open Fusion 360. Create new component "magnetic_bracket_v1" | 2 min | Clean workspace |
| 2 | Sketch base rectangle: 25mm × 20mm on XY plane | 3 min | Body footprint |
| 3 | Extrude 6mm | 1 min | Solid body |
| 4 | Sketch magnet pocket: circle Ø3.10mm, centered at 12.5mm, 10mm from base | 3 min | Pocket footprint |
| 5 | Extrude-cut pocket: 1.6mm deep | 2 min | Magnet seat |
| 6 | Sketch adhesive recess on rear face: 20mm × 15mm rectangle | 3 min | VHB pad seat |
| 7 | Extrude-cut recess: 0.5mm deep | 1 min | Tape recess |
| 8 | Fillet all exterior edges: 0.8mm | 5 min | Clean geometry |
| 9 | Add 2× M3 screw holes (optional, 3.2mm diameter, 10mm center-to-center) | 8 min | Mechanical mount option |
| 10 | Export STL: File → 3D Print → export to .stl at 0.001mm chord length | 2 min | Print-ready file |
| 11 | Open in Bambu Studio, slice with standard PLA+ profile, verify magnet pocket geometry in preview | 8 min | Confirmed sliceable |
| **Total Phase 1** | | **~40 min** | `magnetic_bracket_v1.stl` |

**Critical check in slicer preview**: Zoom into the magnet pocket cross-section in Bambu Studio layer view. Verify the pocket walls show 3 perimeter lines (approximately 1.2mm wall thickness) with no gaps between perimeters. If the pocket shows only 1-2 perimeters, increase perimeter count to 4 for this file.

### Phase 2: Label Tile (45 minutes)

**Goal**: Tile STL with 2 text variants ready for test print

| Step | Action | Time | Output |
|---|---|---|---|
| 1 | New component "magnetic_label_tile_v1" | 2 min | Clean workspace |
| 2 | Sketch tile base: 25mm × 15mm rectangle | 2 min | Tile footprint |
| 3 | Extrude 2mm | 1 min | Solid tile |
| 4 | Magnet pocket on rear face: Ø3.10mm, 1.6mm deep, centered | 5 min | Matches bracket pocket exactly |
| 5 | Text emboss on front face: sketch text tool, choose font, size ~6-8pt, position in 20mm × 10mm area | 15 min | Embossed/debossed label |
| 6 | Extrude text: 0.6mm above or below tile face | 3 min | Readable at distance |
| 7 | Fillet edges 0.5mm | 3 min | Finish |
| 8 | Export STL | 2 min | `magnetic_tile_v1_cable1.stl` |
| 9 | Clone component, change text to second variant (e.g., "CABLE 2") | 5 min | `magnetic_tile_v1_cable2.stl` |
| 10 | Open both in Bambu Studio, verify slice | 5 min | Both confirmed |
| **Total Phase 2** | | **~45 min** | Two tile STLs |

**Text options for initial production run**: CAB1, CAB2, CAB3, USB-A, USB-C, HDMI, ETH, POWER, AUX, AUDIO. Design with parametric text if using CadQuery (script generates all variants automatically from a string list). In Fusion 360, manual text clone is faster for initial 10-variant batch.

### Phase 3: Calibration Print and Tolerance Verification (1 hour)

**Goal**: Confirm magnet pocket tolerance before committing production STL

| Step | Action | Time |
|---|---|---|
| 1 | Print 3 bracket bodies (calibration run, single plate) | 20 min print + 15 min cool |
| 2 | While printing: measure 10 magnets with caliper, record min/max diameter | 10 min |
| 3 | Press-fit test: press magnet into bracket pocket by hand | 2 min each × 3 = 6 min |
| 4 | Evaluate fit: snug (nominal), falls out (pocket too large), won't press in (pocket too small) | 5 min |
| 5a | If snug: record pocket diameter as confirmed, lock STL for production | 2 min |
| 5b | If falls out: reduce pocket by 0.05mm in Fusion 360, re-export, reprint 1 bracket | 25 min loop |
| 5c | If won't press in: increase pocket by 0.05mm, re-export, reprint 1 bracket | 25 min loop |
| 6 | After confirmed fit: print 1 full assembly (bracket + tile) and test magnetic registration | 15 min |
| **Total Phase 3** | | **45-90 min** depending on iteration count |

**Expected iterations**: 0-1. At Bambu P1S default settings, 3.10mm pocket on a 3.00mm magnet should fit on first attempt. One iteration is the most likely scenario if magnet batch measures 3.05mm nominal. Zero iterations if magnet batch is consistent with catalog spec.

### Phase 4: Production STL Finalization and Documentation (30 minutes)

| Step | Action | Time |
|---|---|---|
| 1 | Lock confirmed pocket diameter in Fusion 360 (note: actual value used) | 2 min |
| 2 | Export final production STLs: bracket body + 10 tile variants | 10 min |
| 3 | Create Bambu Studio project file with confirmed print profile (save as .3mf) | 5 min |
| 4 | Document in project log: confirmed pocket diameter, magnet batch measured range, print settings used | 8 min |
| 5 | File naming convention: `modrun_magnetic_bracket_v1_FINAL.stl`, `modrun_tile_CAB1_v1_FINAL.stl` (through CAB10) | 5 min |
| **Total Phase 4** | | **~30 min** |

**Total CAD-to-production-STL workflow: 3.0-3.5 hours (within 4-hour target)**

---

## Part 5: Production Cost Model

### Per-Unit COGS (Bracket Assembly)

| Component | Unit Cost | Source | Notes |
|---|---|---|---|
| PLA+ filament (bracket body, ~3g) | $0.04 | eSUN at $13/kg | 3g × $0.013/g |
| PLA+ filament (label tile, ~1g) | $0.013 | eSUN at $13/kg | 1g × $0.013/g |
| Neodymium magnet × 2 (one per piece) | $0.06-0.20 | AliExpress or Amazon (see Part 6) | 2 magnets per assembly (1 bracket + 1 tile) |
| 3M VHB tape cut | $0.08 | Amazon, bulk per-cut cost | 20mm × 15mm piece |
| Packaging (poly mailer, tissue, label) | $0.40-0.50 | Shop4Mailers + Pirate Ship | Standard ModRun packaging |
| **Total COGS per assembly** | **$0.59-0.81** | | Bracket + 1 tile |

### Revenue Assumptions

| SKU | Contents | Retail Price | COGS | Gross Margin | After Etsy Fees (16.8%) | Net Margin |
|---|---|---|---|---|---|---|
| Single set (1 bracket + 2 tiles) | 4g PLA + 4 magnets + tape | $4.49 | $0.90 | 80% | $3.73 net | ~68% |
| 5-pack bundle (5 brackets + 10 tiles) | 20g PLA + 20 magnets + tape | $18.99 | $3.80 | 80% | $15.78 net | ~70% |
| 10-pack bundle | 40g PLA + 40 magnets + tape | $32.99 | $7.20 | 78% | $27.43 net | ~68% |

**Retail pricing note**: The magnetic label clip is a lower average order value than the snap-arm clip ($4.49-18.99 vs. $5.99-24.99 for snap-arm sets). Monthly revenue at 40-60 units/month: $180-360 (vs. $240-600 for snap-arm). This is the primary downside of the fallback path and why it is second-choice, not first.

**Magnet add-on opportunity**: Offer a "tile refill pack" — 5 blank tiles for $8.99 ($0.07 COGS each). Recurring revenue as customers customize and reuse brackets. This partially compensates for lower unit price.

---

## Part 6: Pre-Qualified Supplier List

### Magnet Suppliers (Critical Path — Order Day 1 of Pivot Decision)

Magnets have a 2-5 day lead time from most sources. Order immediately upon committing to pivot. Do not wait for calibration prints.

| Supplier | Product | Unit Cost (100 pk) | Unit Cost (1000 pk) | Lead Time | Order Link | Priority |
|---|---|---|---|---|---|---|
| **Amazon Prime — DIYMAG** | 3mm × 1.5mm N52 Nickel Neodymium Disk | $0.15/unit ($14.99/100) | $0.08/unit | **2 days (Prime)** | Search "3mm 1.5mm N52 neodymium disc magnets" on Amazon | 1 — Primary (fast) |
| **Amazon Prime — FINDMAG** | 3mm × 1.5mm N35-N52 disc | $0.12/unit ($11.99/100) | $0.07/unit | **2 days (Prime)** | Search "FINDMAG 3x1.5mm neodymium magnets" | 1 — Backup (same lead) |
| **AliExpress — Generic N52** | 3mm × 1.5mm N52 Nickel Disk | $0.03-0.05/unit (100 pk) | $0.02/unit (1000 pk) | 15-30 days (standard) | aliexpress.com, search "3mm 1.5mm N52 neodymium disc" | 3 — Long-term bulk only |
| **McMaster-Carr 5862K102** | 3mm dia × 1.5mm thick N42 Neodymium | $0.45/unit (10 pk) | $0.28/unit (100 pk) | **1-2 days (US warehouse)** | mcmaster.com, search 5862K102 | 2 — Quality-guaranteed, higher cost |
| **K&J Magnetics BD3** | 3/32" dia × 1/16" N52 | $0.54/unit (small qty) | $0.11/unit (250 pk) | **2-3 days (US)** | kjmagnetics.com/product.asp?pcode=BD3 | 2 — Precise US-spec, good for production |

**Recommendation for fallback pivot execution**:
- **Day 1**: Order 200 units from Amazon Prime (DIYMAG or FINDMAG, ~$25-30). Arrives before calibration prints are needed. These cover 100 production units (2 magnets per assembly).
- **Day 7+ (if launch confirms demand)**: Place 1000-unit bulk order from AliExpress ($20-50 for 2000 magnets covering 500 assemblies). 15-30 day lead time; arrives before second production batch is needed.
- Do not use AliExpress for initial production — lead time incompatible with 8-day pivot timeline.

### Filament Suppliers (No Change From Snap-Arm — Same Material)

The fallback product uses the same PLA+ filament as the snap-arm. No new supplier relationship required.

| Supplier | Product | Cost | Lead Time | Notes |
|---|---|---|---|---|
| eSUN (existing primary) | ePLA-Plus 1.75mm, 1kg | $12-13/kg | 3-7 days | Same as snap-arm. If stock on hand from previous order: zero lead time. |
| Amazon (Bambu brand PLA) | Bambu PLA Basic 1kg | $14.99/kg | 2 days Prime | Premium, slightly higher cost; confirmed AMS compatibility. |
| MatterHackers MH Build PLA | MH Build PLA+ | $19.99/kg | 2-5 days | US-made; consistent spec. Use if eSUN stock is exhausted. |

**Consumption estimate for 100-unit production batch**: 100 brackets × 3g + 100 tiles × 1g = 400g total. One 1kg spool covers 2 full production batches with margin. If current filament stock is ≥500g, no filament order is needed during the pivot.

### 3M VHB Adhesive Tape

| Supplier | Product | Cost | Lead Time | Notes |
|---|---|---|---|---|
| Amazon Prime — 3M | 3M VHB 4910 tape, 1/2" × 5yd roll | $8-12 | 2 days | Cut to 20mm × 15mm per bracket. 5yd roll covers ~225 brackets. |
| Amazon Prime — 3M | 3M VHB Mounting Tape 4910 (pre-cut 1" dots) | $12 for 25 dots | 2 days | Alternative: pre-cut dots, minor size mismatch, acceptable for first batch. |

**Consumption for 100 brackets**: 100 pieces × 20mm × 15mm = ~3,000 cm² = ~1.3 yards of 1/2" tape. One 5-yard roll covers first 3-4 production batches. Order 1 roll on Day 1 of pivot (same Prime order as magnets).

### Packaging Suppliers (No Change From Snap-Arm)

Same poly mailer and label stock as snap-arm. No new supplier relationship needed.

---

## Part 7: Etsy Listing Configuration

### Title Template (80 char max)

```
Magnetic Cable Label Clips — Desk Organizer, 3D Printed, Removable Labels
```

Alternative titles for A/B testing:
```
3D Printed Cable Labels — Magnetic Clips for Desk & Server Rack Organization
Magnetic Label Mount Clips — Removable Cable Tags, 3D Printed PLA
```

### Description Template (Abbreviated)

```
Magnetic Cable Label Clips — ModRun Precision

Keep every cable identified without fumbling through a bundle. These 3D-printed magnetic clips mount permanently to your desk or rack with 3M VHB adhesive, and the label tiles snap on and off magnetically so you can swap labels without moving anything.

WHAT'S INCLUDED
• [Qty] × Magnetic bracket (25 × 20 × 6mm, adhesive pre-installed)
• [Qty] × Label tile (text options: CAB1–CAB3, USB-A, USB-C, HDMI, ETH, POWER, AUDIO, or custom)
• Each assembly holds with N52 neodymium magnet — no tools, no residue

SPECS
• Bracket: 25mm × 20mm × 6mm, PLA+ (same material as our cable clips)
• Adhesive: 3M VHB (semi-permanent; leaves minimal residue if removed)
• Magnet pull: 300g axial — holds tile securely under gravity

CUSTOM OPTIONS
Message for custom text (up to 12 characters per tile, any font we carry).
```

### Pricing Launch Strategy

| Phase | Price | Rationale |
|---|---|---|
| Days 1-7 (fallback launch) | $3.99 single / $16.99 five-pack | Introductory; build first 5 reviews quickly |
| Days 8-30 | $4.49 single / $18.99 five-pack | Standard pricing after first review anchor |
| Month 2+ | $4.49 / $18.99 / $29.99 (10-pack) | Add 10-pack when inventory is predictable |

---

## Part 8: Integration With Failure Execution Plan

This document integrates with the following decision gates in POST_TEST_PRINT_FAILURE_EXECUTION_PLAN.md:

### Day 3 Gate (Snap-Arm v2 Feasibility)

If answer is NO at Day 3 gate (confidence <70%, redesign unlikely to succeed):

1. Make pivot decision by end of Day 3 afternoon (document in project log)
2. Order Day 1 supplies immediately: 200 magnets from Amazon Prime, 1 roll 3M VHB tape, any filament gaps
3. Begin Phase 1 CAD (bracket body) Day 3 afternoon — 40 minutes
4. Begin Phase 2 CAD (label tile) Day 3 afternoon — 45 minutes
5. Run calibration print Day 4 morning when Amazon order arrives (Day 3 PM order → Day 4 AM delivery with Prime)
6. Confirm pocket tolerance Day 4 late morning
7. Print production batch (20-50 units for launch stock) Day 4-5

**Timeline from Day 3 pivot decision to Etsy launch**:
- Day 3 afternoon: CAD complete
- Day 4 morning: Calibration print + tolerance confirm
- Day 4 afternoon: Production batch started (50 units, ~10 hours print time)
- Day 5: Photography + Etsy listing copy
- Day 6: Etsy shop prep + listing finalized
- Day 7-8: Launch (aligns with POST_TEST_PRINT_FAILURE_EXECUTION_PLAN.md Day 8 launch target)

### Day 7 Gate (v2 Launch Readiness)

If v2 test batch fails at Day 7 gate (quality issues persist, confidence still below threshold):

- This document's Day 3 materials have already been ordered (delivered Day 4-5)
- CAD is already complete (done Day 3)
- If calibration print was not yet run: run immediately (4-hour delay)
- Production batch ordered same day
- Launch within 48 hours of Day 7 gate confirmation

### Day 14 Gate (Supply Chain Contingency)

If at Day 14 the primary launch is still blocked (iterating snap-arm v3+):

- Fallback product should already be live at this point (launched Day 8)
- Day 14 gate decision becomes: scale fallback product while continuing snap-arm iteration independently
- Allocate additional production capacity to fallback: print 50-unit batch per week
- Snap-arm iteration continues off critical path with no revenue pressure

---

## Appendix A: Quick-Start Checklist (Day of Pivot Decision)

Use this 15-minute checklist immediately after committing to the fallback pivot:

- [ ] Write decision in project log: "Pivoting to magnetic label clips. Date: [DATE]. Reason: [snap-arm v2 confidence <70% / Day 7 gate failure / other]"
- [ ] Open Amazon, place order: 200 × 3mm × 1.5mm N52 neodymium magnets (search DIYMAG or FINDMAG) + 1 roll 3M VHB 4910 tape. Confirm Prime 2-day delivery.
- [ ] Open Fusion 360, begin bracket body sketch (Part 4, Phase 1)
- [ ] Set Bambu P1S for PLA+ standard profile — no changes needed
- [ ] Pull magnet calibration samples from delivery: measure 10 magnets with caliper before starting CAD pocket diameter
- [ ] Email any snap-arm suppliers: "Design change in progress. Holding current order. Will update specs by [Day 7 date]."
- [ ] Notify Orchestrator: pivot confirmed, activate fallback Etsy listing prep

**Time to first action from decision**: 0 minutes. No planning lag. All information is in this document.

---

## Appendix B: Risk Matrix

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Magnet pocket too loose on first print | Medium (30%) | Low — single reprint | Calibration print protocol in Phase 3 |
| Amazon magnet order delayed (non-Prime) | Low (10%) | Medium — 1-2 day slip | Order from two Prime suppliers simultaneously ($25 each) |
| PLA+ filament out of stock | Very Low (5%) | Medium — 1-2 day slip | 99% chance sufficient stock on hand from snap-arm production |
| Etsy does not index fallback listing | Low (15%) | Low — 2-3 day organic index lag | Submit listing, add Etsy Offsite Ads ($1/day) for first week |
| Magnetic hold insufficient for heavy cables | Medium (25%) | Low — niche functional issue | Label tiles are for identification, not cable support. Reframe listing accordingly. |
| 3M VHB adhesive leaves residue on surface | Low (15%) | Low — customer expectation | Note in listing description: "Semi-permanent. 3M VHB; leaves minimal residue." |

---

**Document Status**: Production-ready
**Version**: 1.0
**Created**: 2026-05-26
**Related Documents**:
- POST_TEST_PRINT_FAILURE_EXECUTION_PLAN.md (activation trigger document)
- FAILURE_SCENARIO_DECISION_TREE.md (routing logic)
- FAILURE_SCENARIO_RESOURCE_ALLOCATION_MATRIX.md (capital allocation)
- SKU_BATCH_2_DESIGN_SPEC.md (related magnetic workshop bin labels — different product, shared magnet sourcing)
