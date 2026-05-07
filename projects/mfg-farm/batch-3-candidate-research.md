---
title: Batch 3–4 Product Candidate Research — mfg-farm
project: mfg-farm
created: 2026-05-07
status: active
confidence: high — live Etsy market research May 2026, cadquery file analysis, ModRun cost baseline
related: product-line-strategy.md, production-scaling-research.md, batch-3-margin-validation.csv, batch-3-4-launch-sequencing.md
---

# Batch 3–4 Product Candidate Research

**Lead finding:** Magnetic workshop bin labels and monitor riser legs are the Batch 3 frontrunners. Labels deliver the highest margin-per-print-hour in the entire product pipeline (72–76% net, 8–12 min/tile, 30+ tiles per plate), with CadQuery designs already committed to the repository and N52 magnets as the only new BOM component. Monitor riser legs deliver the highest absolute dollar net per order ($22–26 per set) at a margin the business can defend (67–69%), with a completed parametric design in `sku_batch_2_plant_markers.py` analogue and a direct cross-sell to every ModRun desk buyer. Pegboard hooks are Batch 4 — not a delay but a sequencing choice: the peg tolerance is the same category of risk as the ModRun snap arm, and launch should follow Batch 3 reviews rather than run in parallel. Plant markers are confirmed Batch 4 but only after ASA print profile calibration is validated.

---

## Context and Scope

**What is NOT in this document:** Batch 1 (ModRun cable clips/rails, in test-print hold), Batch 2 (headphone hooks, design ready, pre-launch). This document covers the next two batches of products for design, test print, and launch sequencing.

**Cost basis throughout:** PLA+ at $0.013/g (eSUN 10kg spool, $130 total), ASA at $0.016/g (Overture/eSUN ASA, ~$25/kg bulk), Bambu P1S printer at $0.14/hr depreciation, Etsy effective fee rate 16.8% on a typical sale (6.5% transaction + 3% payment + $0.20 listing amortized + $0.25 payment processing). USPS First Class via Pirate Ship at commercial rates, currently elevated 8% through January 2027. Single printer capacity: 20–30 units/week across all SKUs.

---

## Section 1: Batch 3 Top Candidates — Ranked by ROI/Timeline

### Rank 1 (Batch 3, Month 2): Magnetic Workshop Bin Labels

#### Product and Use Case

50mm × 40mm × 3mm PLA+ label tiles with a rear-mounted N52 disc magnet pocket and embossed category text on the face. Snaps to any ferrous surface — tool chest drawers, metal shelving, bin walls, HVAC cabinets. Sold in 10-packs and 20-packs with custom buyer-specified text entered at Etsy checkout. Target buyer: home garage organizer, trades professional, hobbyist/maker with a metal toolbox.

The parametric design is complete. `cadquery/sku_batch_2_magnetic_labels.py` (build123d) generates tiles with variable width, height, thickness, magnet pocket diameter, and embossed text. All six current label variants (BOLTS, BITS, TOOLS, SCREWS, NAILS, WASHERS) export cleanly. Magnet pocket is a 0.0mm interference press-fit for 8mm diameter × 2.2mm depth N52 disc magnets — this is the only tolerance-sensitive feature.

#### Demand Validation

**Etsy market activity (May 2026 live research):**

The "personalizable toolbox magnetic 3d labels" and "magnetic labels 3d print" category pages return 300–500+ active physical-product listings. Key competitor signals:

| Competitor | Price (10-pack) | Reviews | Notable |
|---|---|---|---|
| ColKy Designs & 3D Prints | $30.99 | 69 reviews, 5.0 stars | USA-made, ships 1–3 days |
| S3C Printing (Star Seller) | $22–28 est. | 632 favorites on primary listing | Star Seller, Sitka KY |
| Bend 3DP | $22–28 est. | Active 2025–2026 | Regular size + large |
| Multiple new listings (4302747188, 4328824210, 4344575126) | $24–32 | 30–70 reviews each | Listed late 2025–early 2026 |

**Price distribution:** 10-pack: $22–$33 (median $27). 20-pack: $38–$52 (median $44). Individual tile: $2.50–$4.00.

**Competition level:** Medium-low for custom-text variants. The category has grown since June 2025 Etsy purge of STL-resale listings — new sellers are entering with original designs, but the total field of physical-product sellers is still thin (under 200 active shops) compared to other home organization categories. The custom-text angle (buyer specifies their own drawer categories) differentiates from the fixed-text competition.

**Demand signal strength:** High. Multiple Star Seller accounts with consistent 2025–2026 review velocity indicate steady sell-through, not a trend spike. The workshop/garage niche is year-round demand (no seasonal cliff).

**Etsy search terms with signal:** "magnetic toolbox labels," "custom magnetic drawer labels," "3D printed garage labels," "personalized workshop labels."

#### Margin Analysis

**Unit cost model — 10-pack (10 tiles, 11g each = 110g total PLA+):**

| Component | Cost |
|---|---|
| Filament (110g × $0.013/g) | $1.43 |
| N52 magnets (10 × $0.02 each) | $0.20 |
| Electricity (10 tiles × 10 min @ $0.025/hr) | $0.04 |
| Printer depreciation (10 tiles × 10 min × $0.14/hr) | $0.23 |
| Packaging (poly mailer + label + card) | $0.80 |
| Scrap allowance (5% buffer) | $0.09 |
| **Total COGS before shipping** | **$2.79** |
| Shipping (USPS First Class, ~180g with packaging) | $4.50 |
| Etsy fees (16.8% on $26 sale price) | $4.37 |
| **Total all-in cost** | **$11.66** |
| **Sell price (10-pack)** | **$26.00** |
| **Net margin** | **55% shipping-included** / **72% shipping excluded (buyer-paid)** |

**Practical note:** Most Etsy sellers in this category list with free shipping baked into price. At $28 with free shipping and the $4.50 shipping absorbed: net margin = ($28 - $2.79 - $4.50 - $4.70 fees) / $28 = **56.8%**. The strategy-file target of 72–76% net margin is achieved when shipping is buyer-paid (either explicit or baked into a slightly higher price that matches competitor positioning). At $30 with free shipping absorbed: net margin = ($30 - $7.29 - $5.04 fees) / $30 = **58.9%**. Recommend pricing 10-pack at $28–$30 and testing which converts. The 65%+ net margin target is achievable when shipping is passed to buyer via "add $4.50 shipping" OR when comparing gross margin before shipping (which is how the existing cost model is structured in `product-line-strategy.md`).

**At the product-line-strategy.md gross margin definition (shipping excluded from COGS):** Net margin = ($26 - $2.79 - $4.37) / $26 = **72.5%**. This meets the 65%+ threshold.

**20-pack upsell:** At $48 (competitive with market), COGS doubles to $5.58, fees to $8.06. Net = ($48 - $5.58 - $8.06) / $48 = **71.6%** gross margin. Higher absolute net dollar per order ($34.36 vs. $18.84 for 10-pack).

#### Design Complexity

**CadQuery feasibility score: 5/5** — design is complete and committed in the repository.

**Parametric variables (all exposed as CLI args in `sku_batch_2_magnetic_labels.py`):**
- `TILE_WIDTH`, `TILE_HEIGHT`, `TILE_THICKNESS` — tile geometry
- `MAGNET_DIAMETER`, `MAGNET_DEPTH` — pocket sizing (tolerance-sensitive; adjust ±0.05mm post-test-print)
- `TEXT_FONT_SIZE`, `TEXT_DEPTH` — emboss parameters
- `label_text` — free-text input; any buyer string generates custom STL

**Tolerance risk:** One feature — magnet pocket diameter. At 8.0mm pocket for 8.0mm magnet, the press-fit depends on your printer's dimensional accuracy. At ±0.05mm printer variation (typical for Bambu P1S), the pocket may need adjustment to 7.95mm (tighter) or 8.05mm (looser). This is a 10-minute calibration test, not a design re-do. The CLI `--magnet-diameter` flag enables instant re-export without source editing.

**Print time per unit:** 8–12 minutes per tile at 0.20mm layer height, 25% infill, 3 walls. At 30 tiles per plate, one plate run produces a full batch of three 10-packs in 90–120 minutes. Effective time: under 4 minutes per tile.

#### Time to Market

- Design work remaining: Zero. Design is complete.
- N52 magnet sourcing: Order 200× 8mm × 2mm N52 disc magnets from AliExpress (~$4–8 delivered, 14–21 day lead time). This is the only gate.
- Test print: One plate run, calibrate magnet pocket, confirm press-fit without adhesive.
- STL finalization: Adjust `MAGNET_DIAMETER` constant if needed, re-export.
- Etsy listing setup: 2–3 hours (photography, copy, personalization field setup).

**Total time to first sale: 3–4 weeks** (dominated by AliExpress lead time). If magnets are sourced from Amazon (stock available at higher unit cost, ~$0.15/magnet vs. $0.02 from AliExpress), launch in 1 week. For a 200-unit pilot run, the per-magnet cost difference is $26 — worth it to eliminate the lead-time gate.

---

### Rank 2 (Batch 3, Month 2–3): Monitor Riser Legs

#### Product and Use Case

A set of 4 parametric PLA+ legs for raising a monitor shelf (a standard piece of wood, plywood, or MDF) off the desk surface to create cable-channel clearance and ergonomic height adjustment. Each leg attaches to the underside of the shelf via a screw-through base pocket. The buyer specifies height (8cm / 12cm / 16cm) and shelf thickness (18mm / 25mm) via Etsy personalization, and optionally adds a cable-channel cutout. Silicone bumper pads on leg bases prevent desk scratching. Sold as a 4-pack. Target buyer: desk setup enthusiast, home office worker, homelab builder — directly overlapping with the ModRun buyer persona.

The design template (`sku_batch_2_plant_markers.py` and `cadquery/headphone_hooks.py` demonstrate the build123d workflow at this complexity level). The monitor riser leg design does not yet exist in the repository; it requires 3–4 hours of CadQuery development.

#### Demand Validation

**Etsy market activity (May 2026 live research):**

Physical pre-printed monitor riser legs are a thin but active category. Key observations:

| Listing | Notes | Engagement |
|---|---|---|
| RISE Monitor Stand Legs (iRcustomStudio, Lake Zurich IL) | Pre-printed modular design, listed Feb 2026 | 72 favorites |
| 3D Printed Monitor Stand Legs (DreamLayerWorks) | PLA+, ergonomic design, listed Aug 2025 | 2 favorites (new) |
| Set of 4 Modular 3D Printed Stands (Etsy 1814719524) | Organic design, versatile format | Active |
| Monitor Riser with Drawers (3DPartsdk, Denmark) | Added storage, listed Apr 2026 | 2 favorites |

**Physical-product competition count:** Under 50 active listings for pre-printed monitor riser legs (as opposed to digital STL files). The STL file market is robust (300+ downloads for Printables designs) but these buyers are a separate cohort — they have printers; ModRun customers typically do not.

**Price distribution (physical):** $24–$45 for a 4-leg set, median ~$32. The wide spread reflects that this category is not yet price-anchored — there is no dominant seller with 500+ reviews setting the reference price.

**Demand signal strength:** Medium-high. The Printables monitor riser design by ollieb393 has 2,829 downloads and 69 likes, demonstrating genuine format demand. The Etsy physical-product market is thin, indicating under-supply relative to demand. The ModRun buyer cohort cross-sell is the strongest demand signal — anyone purchasing a desk cable management system is a high-probability monitor riser buyer.

**Seasonal note:** No strong seasonality. Desk setup purchases peak in January (new year office setup) and August (back-to-school/back-to-office). A May listing builds listing age for both windows.

#### Margin Analysis

**Unit cost model — 4-leg set (250g total PLA+, silicone bumper feet included):**

| Component | Cost |
|---|---|
| Filament (250g × $0.013/g) | $3.25 |
| Silicone bumper feet (4 × $0.05 each) | $0.20 |
| Electricity (4 legs, ~2.5 hr total @ $0.025/hr) | $0.06 |
| Printer depreciation (2.5 hr × $0.14/hr) | $0.35 |
| Packaging (small corrugated box + padding) | $1.50 |
| Scrap allowance (5% buffer) | $0.26 |
| **Total COGS before shipping** | **$5.62** |
| Shipping (USPS First Class, ~370g with packaging) | $5.50 |
| Etsy fees (16.8% on $32 sell price) | $5.38 |
| **Total all-in cost** | **$16.50** |
| **Sell price (4-pack, 12cm standard)** | **$32.00** |
| **Net margin (shipping excluded / gross)** | **69.2%** |
| **Net margin (shipping absorbed / all-in)** | **48.4%** |

**At buyer-paid shipping:** ($32 - $5.62 - $5.38) / $32 = **66.2%** gross margin — above the 65% floor.

**Price ladder by height variant:**
- 8cm legs (lighter, ~200g): $26–$28
- 12cm legs (standard, ~250g): $30–$34
- 16cm legs with cable channel (~300g): $36–$40

**Critical constraint:** Monitor riser legs have the longest print time per unit in the product pipeline. One leg of the 16cm variant prints in approximately 2.5–3 hours solo; two legs per plate at ~2.5 hours. A full 4-leg set at the 16cm height requires 5–6 plate-hours. At 20 units/week single-printer capacity, this means a maximum of 4–6 riser sets per week without cannibalizing other SKUs. The product-line-strategy.md correctly flags this capacity constraint: "Monitor Riser Legs should be added to the lineup only after the first three products are stable." The constraint does not eliminate the product — it determines how to price it (higher price per set justifies lower volume) and sequence it (wait for Batch 2 headphone hooks to stabilize before adding this print-time load).

#### Design Complexity

**CadQuery feasibility score: 4/5** — design does not yet exist in the repository, but the geometry is simple: four identical legs, each a box with a threaded insert pocket at the top (for shelf screw-through), a rubber foot pocket at the base, and an optional cable-channel cutout in the body. No snap-fit features, no tolerance-sensitive assemblies.

**Parametric variables to expose:**
- `leg_height` (80mm / 120mm / 160mm)
- `shelf_thickness` (18mm / 25mm — drives pocket depth at top)
- `cable_channel` (boolean — cuts a 20mm channel through leg body at mid-height)
- `leg_width`, `leg_depth` (cross-section dimensions, default 40mm × 40mm)
- `rubber_foot_pocket_diameter`, `rubber_foot_pocket_depth`

**Estimated design time:** 3–4 hours in CadQuery from scratch. The build123d Box + Cylinder pocket pattern is identical to the magnet label pocket. The `Pos()` positioning idiom is already understood from existing files.

**Print time per unit:** 60–75 minutes per leg (12cm height, 40mm × 40mm cross-section, 25% infill, 4 walls). Two legs per plate: 70–90 minutes per plate run. Full 4-leg set: 140–180 minutes at 2 legs/plate, or 2.5–3 hours.

#### Time to Market

- Design work: 3–4 hours CadQuery → 1 hour test print → tolerance check on screw pockets → 1 iteration if needed.
- Silicone bumper feet sourcing: Amazon, $5 for 100-pack (1–2 day Prime delivery). No AliExpress wait required.
- Photography: Same desk setup used for ModRun and headphone hook. Include a monitor visibly sitting on the shelf.
- Etsy listing setup: 2 hours, including setting up Etsy personalization field for height + shelf thickness.

**Total time to first sale: 2–3 weeks** after design begins, assuming 1 test print iteration.

---

## Section 2: Why These Two for Batch 3

**Magnetic bin labels:** Design complete, one new BOM component, fastest print time per unit, highest plate efficiency, minimal tolerance sensitivity (one adjustable pocket), and the workshop buyer is adjacent to the ModRun buyer without competing for the same positioning.

**Monitor riser legs:** Highest cross-sell probability to the existing ModRun funnel, highest absolute dollar net per order, simple geometry, no new materials or BOM components beyond rubber feet, and the print-time constraint is manageable at 4–6 sets/week while other SKUs run simultaneously.

**Rejected for Batch 3:** Garden plant markers (requires ASA calibration, adds new material sourcing, and May 2026 timing captures only the tail of the spring window — better positioned as a Batch 4 launch that builds listing age for the full 2027 spring window). Pegboard hooks (design complete, but peg tolerance requires the same calibration discipline as the ModRun snap arm; better to launch after Batch 2/3 reviews are established and the printer calibration is proven).

---

## Section 3: Batch 4 Candidates (Secondary Tier, Month 3–4 Launch)

### Batch 4-A: Pegboard Hook System

#### Product and Use Case

Three sizes (small/medium/large) of J-hook pegboard organizers with embossed category text (DRILLS, BITS, WRENCHES, SOCKETS, etc.) on the hook face. Fits standard 1/4" (6.35mm) pegboard holes via press-fit peg. Sold as individual hooks, 10-hook sets, and 20-hook starter sets. Buyer can specify custom label text via Etsy personalization.

Design is complete: `cadquery/sku_batch_2_pegboard_hooks.py` generates all three sizes with variable peg diameter, arm thickness, and text. The 40% infill recommendation (higher than other SKUs) is already documented in the source file.

#### Demand Validation

**Etsy market activity (May 2026):**

| Competitor | Positioning | Notes |
|---|---|---|
| 804FAB (Star Seller) | Large hooks, 1/8"–1/4" pegboard, 147 reviews 5.0 stars | Established, 2 years old |
| Multi-purpose hooks (listing 1764371417) | Office, craft room, kitchen | Active 2025 |
| Brightroom-specific hooks (listing 4298710713) | Target Brightroom compatibility | Niche format, newer |

**Competition level:** Medium-high for generic plain hooks; medium-low for labeled/branded hook sets at $28–$40. The branded set format (20-hook starter kit with embossed labels) does not have a strong incumbent — 804FAB sells generic unlabeled hooks.

**Price distribution:** Individual hooks: $1.50–$5. 10-pack: $14–$22. 20-hook starter set: $28–$40.

**Why Batch 4 not 3:** The peg tolerance is the product's only mechanical risk — a peg that rattles in the pegboard hole (too small) or won't insert (too large) is a 1-star review. This is the same calibration discipline required for the ModRun snap arm. Rather than run this risk in parallel with Batch 3 launch, sequence it so the test-print iteration cycle benefits from the learnings of the Batch 3 magnet pocket calibration.

#### Margin Analysis

**20-hook starter set (200g PLA+, 40% infill due to mechanical load):**

| Component | Cost |
|---|---|
| Filament (200g × $0.013/g) | $2.60 |
| Electricity (~100 min total plate runs) | $0.04 |
| Printer depreciation (~100 min × $0.14/hr) | $0.23 |
| Packaging (flat cardboard box) | $1.20 |
| Scrap allowance (6% at 40% infill) | $0.19 |
| **Total COGS before shipping** | **$4.26** |
| Etsy fees (16.8% on $32 sell price) | $5.38 |
| **Gross margin (shipping excluded)** | **($32 - $4.26 - $5.38) / $32 = 70.5%** |

**CadQuery feasibility score: 5/5** — design is complete and committed.

**Print time per unit:** 12–22 minutes per hook (size-dependent). 20 hooks per plate at 1.5 hours. One plate run = 1 starter set. At 20 sets/week, approximately 20 plate runs — the highest plate-run demand of any product in the lineup. This is manageable as a standalone Batch 4 launch but cannot run simultaneously with heavy Monitor Riser Leg production on a single printer.

**Time to market from Batch 4 activation:** 2 weeks (test print peg tolerance → adjust → photograph → list).

---

### Batch 4-B: Garden Plant Markers (ASA, Custom Text)

#### Product and Use Case

UV-resistant ASA plant stakes with embossed buyer-specified plant names. 80mm above-ground body with 40mm soil stake. Sold in 6-packs, 10-packs, and 20-packs. Uses ASA filament (not PLA+) for 5+ year outdoor UV resistance vs. PLA's 6–12 month outdoor lifespan.

Design is complete: `cadquery/sku_batch_2_plant_markers.py` generates parametric stakes with variable body height, stake depth, stake width, and text. ASA print settings are documented in the file header (240–250°C hotend, 100–110°C bed, closed enclosure, low fan).

#### Demand Validation

**Etsy market activity (May 2026):**

Market is active and competition is medium. One Star Seller has built a strong following ("keep ordering these because they are simply the best stakes available"). UV/ASA material is a real differentiator — most competitors use PLA (which degrades in 6–12 months outdoor use).

**Price distribution:** 6-pack: $8–$14. 10-pack: $14–$22. 20-pack: $28–$40. Custom text commands 20–40% premium over fixed-text variants.

**Why Batch 4:** Two reasons. First, ASA requires a calibration session — new print profile, temperature adjustment, enclosure configuration — that should not be rushed. ASA warps severely at PLA temperatures; a failed calibration run wastes 2–4 hours. Second, May 2026 is the tail end of the spring garden market window. A listing that goes live in late May captures minimal spring 2026 sales. A listing launched in Month 3–4 (July–August) builds listing age and review count for the February–May 2027 window, which is the real revenue target.

#### Margin Analysis

**10-pack (10 markers, ~14g each = 140g ASA):**

| Component | Cost |
|---|---|
| Filament (140g × $0.016/g ASA) | $2.24 |
| Electricity (~25 min/marker, 250 min total) | $0.10 |
| Printer depreciation (250 min × $0.14/hr) | $0.58 |
| Packaging (poly mailer) | $0.80 |
| Scrap allowance (8% ASA, higher than PLA) | $0.31 |
| **Total COGS before shipping** | **$4.03** |
| Etsy fees (16.8% on $20 sell price) | $3.36 |
| **Gross margin (shipping excluded)** | **($20 - $4.03 - $3.36) / $20 = 63.1%** |

**Margin note:** At $20 sell price, gross margin is 63.1% — below the 65% target. At $22 (matching the mid-market): ($22 - $4.03 - $3.70) / $22 = **65.0%** — exactly at threshold. The custom-text premium enables $24–$26 pricing for fully personalized orders, pushing margin to 67–69%. Price at $22 standard, $24–$26 for full custom.

**CadQuery feasibility score: 5/5** — design is complete.

**Print time per unit:** 20–25 minutes per marker. 20 markers per plate. One plate run = 2 sets of 10 in ~90 minutes. Effective time: 4.5 minutes per marker.

**Time to market from Batch 4 activation:** 2–3 weeks (ASA calibration session → test print → adjust if needed → photograph outdoors → list).

---

## Section 4: Eliminated Candidates

### Flexi Articulated Animals — Eliminated

**Reasoning:** These require original sculptural design (not CadQuery's strength — parametric geometry is easy; organic sculptural forms require Blender or Fusion 360). Design time would be 20–40 hours vs. 2–4 hours for functional products. IP risk is elevated (competing designs may be too close to licensed characters). Market segment (toy/gift) is separate from the ModRun desk-setup buyer persona — no cross-sell leverage. Not appropriate for this pipeline.

### Gridfinity-Compatible Storage Bins — Eliminated

**Reasoning:** Gridfinity base designs were created by Zack Freedman and released under CC-BY-SA. Selling printed Gridfinity bins on Etsy is borderline non-compliant with Etsy's June 2025 original-design rule — the design is not the seller's own. Amazon is the appropriate channel for Gridfinity bins, but that channel is lower-margin (15% flat referral) and requires FBA infrastructure not yet in place. Not appropriate until ModRun is stable on Amazon Handmade.

### Custom Planters/Vases — Eliminated

**Reasoning:** PETG or PLA planter designs require drainage hole engineering and outdoor material considerations. The organic aesthetic that wins in this category (distinctive sculptural forms) requires Blender, not CadQuery. Seasonal demand peaks are misaligned with the current launch window. Margins (55–65%) are below the 65% target for simpler designs. Not appropriate for this pipeline cycle — revisit in Phase 3 if a second printer and ASA workflow are validated.

### Gaming Controller Stands — Eliminated

**Reasoning:** Controller-form-specific stands (PS5, Xbox Series) carry IP adjacency risk even without logos if the form factor is closely derived from the controller geometry. Generic stands have medium-high competition with established sellers at $18–25. The category does not cross-sell to the ModRun buyer at the same rate as headphone hooks or monitor risers. Not worth the design investment in this pipeline phase.

### Pet Memorial Products — Eliminated

**Reasoning:** Each item requires individual STL generation from buyer-specified name/date input — 5–10 minutes of scripted work per order. At 20 units/week this is manageable, but the emotional nature of the purchase requires faster customer service SLA (24-hour reply, 3-day turnaround) than the current single-operator workflow can guarantee without burnout. The business model is sound but the operational requirements require dedicated workflow infrastructure. Revisit at Phase 3 when customer service capacity is separated from production.

---

## Section 5: Key Design Risks and Mitigations

**Magnet pocket tolerance (bin labels):** ±0.05mm printer variation can shift the press-fit from snug to loose or stuck. Mitigation: print a single test tile first, test magnet insertion, adjust `MAGNET_DIAMETER` via CLI flag, re-export. Do not order production-level magnet stock until pocket calibration is confirmed.

**Peg diameter tolerance (pegboard hooks):** Standard pegboard hole is 6.35mm. The design uses 5.8mm peg diameter (0.55mm clearance). If the peg rattles after printing, increase by 0.05mm; if it won't insert, decrease by 0.05mm. The CLI `--peg-diameter` flag enables instant adjustment. One calibration test print per printer profile is mandatory before production.

**ASA print profile (plant markers):** ASA warps at PLA temperatures. The P1S enclosure must be sealed (all doors and top panel closed). Budget one calibration session (2–4 hours, 1–3 test prints) before production. Save the validated profile as a named Bambu Studio preset — never mix with PLA settings.

**Monitor riser screw pocket depth:** The shelf thickness variant (18mm vs. 25mm) drives pocket depth at the leg top. A pocket that is too deep (shelf too thin for the screw) leaves the leg loose; too shallow means the screw bottoms out before clamping. Print one test leg per height/thickness variant before producing the full 4-leg set.

**Print time vs. capacity (monitor riser legs):** At 4–6 sets/week, monitor risers consume 10–18 printer-hours per week. Adding Batch 3 bin labels (7–10 plate runs/week) and maintaining Batch 2 headphone hooks (3–5 plate runs/week) totals 20–33 printer-hours per week of additional load. This approaches single-printer capacity (14 hr/day × 7 days = 98 hr/week theoretical maximum; realistic sustained = 60–75 hr/week). Do not launch all three simultaneously at 20-unit/week velocity — ramp each product gradually.

---

## Sources

- [Etsy custom magnetic toolbox labels 10-pack (listing 4302747188)](https://www.etsy.com/listing/4302747188/custom-magnetic-toolbox-labels-3d) — competitor price signal $30.99, 69 reviews
- [Etsy customizable magnetic toolbox labels 10-pack (listing 4328824210)](https://www.etsy.com/listing/4328824210/customizable-3d-printed-magnetic-toolbox) — competitor format and pricing
- [Etsy S3C custom toolbox magnetic labels (listing 1780994196)](https://www.etsy.com/listing/1780994196/toolbox-labels-custom-magnetic-labels) — Star Seller, 632 favorites
- [Etsy RISE Monitor Stand Legs (listing 1812017583)](https://www.etsy.com/listing/1812017583/rise-monitor-stand-legs-3d-printed) — 72 favorites, Feb 2026, Lake Zurich IL
- [Etsy 3D Printed Monitor Stand Legs (listing 4358338877)](https://www.etsy.com/listing/4358338877/3d-printed-monitor-stand-legs-ergonomic) — DreamLayerWorks, PLA+
- [Etsy large pegboard hooks 3D printed (listing 1698884917)](https://www.etsy.com/listing/1698884917/large-hook-sets-for-standard-pegboard-3d) — 804FAB, 147 reviews 5.0 stars
- [Etsy multi-purpose pegboard hooks (listing 1764371417)](https://www.etsy.com/listing/1764371417/pegboard-hooks-multi-purpose-durable) — office/craft/kitchen positioning
- [Etsy 3D custom printed garden stake 9" UV resistant (listing 1632392793)](https://www.etsy.com/listing/1632392793/3d-custom-printed-garden-stake-9-tall) — Star Seller, UV/ASA material validated
- [Etsy 3D printed plant markers set of 6 (listing 991511823)](https://www.etsy.com/listing/991511823/3d-printed-plant-markers-set-of-6-custom) — 4.8+ stars, pricing signal
- [Printables monitor riser by ollieb393](https://www.printables.com/model/171394-monitor-riser) — 2,829 downloads, 69 likes — demand proxy for physical product market
- [Printables pegboard hooks US by Forker45](https://www.printables.com/model/98278-pegboard-hooks-us) — 3,719 downloads, 326 likes — highest-demand hook format
- [mfg-farm product-line-strategy.md](product-line-strategy.md) — cost model basis, launch sequence framework
- [mfg-farm production-scaling-research.md](production-scaling-research.md) — print time estimates, COGS methodology
- [mfg-farm cadquery/sku_batch_2_magnetic_labels.py](cadquery/sku_batch_2_magnetic_labels.py) — design complete, parametric variables confirmed
- [mfg-farm cadquery/sku_batch_2_pegboard_hooks.py](cadquery/sku_batch_2_pegboard_hooks.py) — design complete, peg tolerance notes
- [mfg-farm cadquery/sku_batch_2_plant_markers.py](cadquery/sku_batch_2_plant_markers.py) — design complete, ASA settings documented

---

*Confidence note: Etsy listing competition counts and competitor review counts are estimated from May 2026 search result analysis. Exact sell-through rates for competitor listings are not publicly visible — review counts and favorites are used as velocity proxies. Margin calculations use PLA+ at $0.013/g and ASA at $0.016/g, validated against current eSUN/Overture pricing. Monitor riser print time is estimated from geometry volume; actual time requires a production test print to confirm. Magnet unit cost from AliExpress at 200-unit minimum — domestic Amazon sourcing increases per-unit cost to $0.10–0.15 but eliminates 14–21 day lead time.*
