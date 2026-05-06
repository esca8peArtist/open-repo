---
title: SKU Batch 2 — Design Specification & Test-Print Guide
project: mfg-farm
created: 2026-05-06
status: READY FOR TEST-PRINT SEQUENCING (post-ModRun/headphone-hooks)
related: product-line-strategy.md, cadquery/sku-batch-2.py, cost-model-spreadsheet.csv
---

# SKU Batch 2: Design Specification & Test-Print Guide

**Overview**: Three high-margin products ready for test-print after the ModRun print completes. All designs are CadQuery parametric scripts in `cadquery/sku-batch-2.py`. Print both ModRun and Batch 2 in parallel once ModRun test confirms the tolerance calibration.

**Timeline**: 
- **Week 1 (post-ModRun pass)**: Test-print 1 sample of each Batch 2 product
- **Week 2-3**: Tolerance iteration (if needed)
- **Week 4**: Photography + listing copy finalization
- **Week 5**: Etsy listing launch (staggered: Labels → Markers → Hooks)

---

## Product 1: Magnetic Workshop Bin Labels

### Specifications

| Parameter | Value | Notes |
|-----------|-------|-------|
| Base dimensions | 50 × 40 × 3.0mm | Adjustable via script parameters |
| Magnet pocket | Ø8mm × 2.2mm depth | N52 disc magnet (AliExpress, $0.02 ea) |
| Text | Embossed, 8pt font | Custom per label tile |
| Print time | 8-12 min per tile | At 0.20mm, 220°C |
| Weight | ~2.5g per tile | PLA+ density |
| Material cost | $0.15 per tile | At $0.013/g PLA+ |
| Hardware cost | $0.02 magnet | 20/pack magnets $0.40 AliExpress |
| **Total COGS** | **$0.17 per tile** | |
| Retail price | $1.50-2.00 per tile | Sell in 20-packs at $28-32 |
| **Net margin** | **72-76%** | After Etsy fees (16.8%) + shipping ($4.00) |

### Design Features

**Top face (buyer-facing)**:
- Embossed category text (BOLTS, BITS, TOOLS, SCREWS, NAILS, WASHERS, etc.)
- Smooth finish, rounded corners for safe handling
- Visible from distance on vertical metal surfaces

**Bottom face (magnet side)**:
- Recessed magnet pocket (Ø8 × 2.2mm depth)
- Pocket walls leave 1.0mm material thickness for stress distribution
- Magnet press-fits with 0.1mm interference for permanent hold (no adhesive needed)

**Material choice**: PLA+ (same as ModRun). No special handling required.

### Tolerance Calibration

Critical tolerance: **Magnet pocket diameter (8.0mm ±0.1mm)**
- Too tight (7.9mm): magnet doesn't fit, requires reaming
- Too loose (8.2mm): magnet falls out under vibration
- Target: 8.0-8.05mm for snug press-fit

**Calibration procedure**:
1. Print test tile with `sku-batch-2.py --product magnetic-label --output-dir ./test_stl/`
2. Test-fit N52 magnet (Ø8mm disc) into pocket
3. If loose: reduce pocket diameter by 0.05mm, reprint
4. If tight: increase pocket diameter by 0.05mm, reprint
5. Record successful diameter in `cadquery/sku-batch-2.py` line ~50 (`magnet_diameter_mm=8.0`)

### Test-Print Sequence

```
1. Print 5 label tiles (one of each category: BOLTS, BITS, TOOLS, SCREWS, NAILS)
   - Print time: 40-60 min total
   - Build plate space: ~150 × 100mm (all 5 fit on one plate)
   - Infill: 25%, walls: 3, layer height: 0.20mm

2. Post-process:
   - Cool 30 min
   - Remove support (if any)
   - Test-fit magnet in each pocket
   - If all fit snugly: continue to adhesive test
   - If any are loose/tight: adjust pocket diameter and reprint 1

3. Adhesion test:
   - Place tile on vertical steel surface (fridge, toolbox)
   - Apply 1kg downward load (water bottle)
   - Magnet should hold indefinitely without adhesive
   - If magnet drops: diameter adjustment needed

4. Documentation:
   - Take photos: top view (embossed text), bottom view (magnet pocket)
   - Note any print defects: layer lines, adhesion issues, dimensional drift
   - Record successful tolerance in git commit message
```

---

## Product 2: UV-Resistant Garden Plant Markers

### Specifications

| Parameter | Value | Notes |
|-----------|-------|-------|
| Base dimensions | 18 × 80 × 3.0mm | Tall vertical stake |
| Ground stake | 8 × 8mm cross-section, 40mm depth | For soil penetration |
| Text area | Upper 30mm (embossed) | Custom plant name or species |
| Print time | 20-25 min per marker | At 0.20mm, 240°C ASA |
| Weight | ~8g per marker | ASA density |
| Material cost | $0.22 per marker | ASA filament ($16/kg) |
| Hardware cost | $0.00 | No hardware required |
| **Total COGS** | **$0.22 per marker** | |
| Retail price | $2.50-3.00 per marker | Sell in 10-packs at $22-26 |
| **Net margin** | **68-72%** | After Etsy fees + USPS First Class $4.50 |

### Design Features

**Vertical body**:
- Tall (80mm) for easy visibility over ground-level plants
- Tapered slightly for easy soil insertion
- Embossed text in upper third (TOMATO, BASIL, SAGE, HERB, FLOWER, etc.)

**Ground stake**:
- Square cross-section (8 × 8mm) for rigidity
- 40mm total length in soil (stake below, body above)
- Pointed tip option (parameterizable) for hard soil

**Material choice**: ASA (UV-resistant)
- PLA degrades in 6-12 months outdoor exposure
- ASA lasts 5+ years in full sun (tested by community on Printables)
- ASA print temperature: 240-250°C (higher than PLA's 220-225°C)
- Cost premium: +$0.06 per unit vs. PLA (worth it for outdoor durability claim)

### Tolerance Calibration

Critical tolerance: **Ground stake width (8.0mm ±0.2mm)**
- Too wide: hard to push into soil, may damage stake
- Too narrow: stake bends under tool weight
- Target: 8.0mm for snug press fit into soil without damage

**Calibration procedure**:
1. Print test marker with ASA: `sku-batch-2.py --product plant-marker --output-dir ./test_stl/`
2. Test soil insertion:
   - Use garden soil in a small pot
   - Push marker stake into soil at 90°
   - Stake should penetrate cleanly without bending or splitting
   - If stake bends: width is too narrow, increase to 8.3mm
   - If stake splits: width is too wide, reduce to 7.7mm
3. Load test: hang 500g weight from top — stake should not deflect >5mm

### Test-Print Sequence (ASA)

```
1. Print 3 marker prototypes
   - Print time: 60-75 min total for 3 markers
   - Build plate space: ~100 × 150mm
   - **CRITICAL**: ASA requires:
     - Bed temperature: 100-110°C (vs. PLA's 60°C)
     - Hotend: 240-250°C (vs. PLA's 220-225°C)
     - Enclosure or draft shield (ASA warps without thermal stability)
     - Bambu P1S has enclosure by default — use it

2. Post-process:
   - Cool 60 min (ASA cools slower than PLA)
   - Remove support (if any)
   - Soil insertion test (see tolerance section above)
   - If any stakes bend: adjust width and reprint 1

3. Durability baseline:
   - Place 1 marker in direct sunlight (outdoor window, no rain)
   - Baseline photos at Day 0
   - Check color/surface at Day 30 for UV resistance verification

4. Documentation:
   - Photo: full marker with text visible
   - Photo: ground stake detail
   - Note ASA printer settings used
   - Record successful stake width in git
```

---

## Product 3: Pegboard Hook System (3 Sizes)

### Specifications

**Small hooks** (hand tools, bits):
| Parameter | Value |
|-----------|-------|
| Hook depth | 35mm |
| Opening width | 12mm |
| Print time | 12-15 min |
| Material cost | $0.16 per hook |
| Retail | $0.80-1.00 per hook |

**Medium hooks** (wrenches, drill bits):
| Parameter | Value |
|-----------|-------|
| Hook depth | 45mm |
| Opening width | 15mm |
| Print time | 15-18 min |
| Material cost | $0.19 per hook |
| Retail | $1.00-1.25 per hook |

**Large hooks** (power tools, heavy items):
| Parameter | Value |
|-----------|-------|
| Hook depth | 55mm |
| Opening width | 18mm |
| Print time | 18-22 min |
| Material cost | $0.22 per hook |
| Retail | $1.25-1.50 per hook |

**Set pricing**:
| Set | Hooks | Retail | COGS | Margin |
|-----|-------|--------|------|--------|
| 20-hook starter | 8S + 8M + 4L | $28-32 | $3.80 | 71% |
| 10-hook assorted | 4S + 4M + 2L | $14-16 | $1.90 | 71% |
| Single hook | Any size | $0.80-1.50 | $0.16-0.22 | 71% |

### Design Features

**Pegboard mounting**:
- Standard 1/4" pegboard hole (6.4mm diameter)
- 8mm peg diameter (0.3mm interference for snug fit)
- Top-mounted for load-bearing stability

**J-hook shape**:
- Vertical post (8mm wide) connects peg to hook arm
- Horizontal arm extends 35-55mm depending on size
- Hook opening 12-18mm for different tool diameters
- Radiused edges for safety (no sharp corners)

**Embossed label**:
- Tool category text on vertical face
- 4pt font to fit small surface area
- Labels: DRILLS, BITS, WRENCHES, SOCKETS, CHISELS, SAW, MISC (customizable)

### Tolerance Calibration

Critical tolerance: **Peg diameter (5.8mm ±0.1mm)**
- Pegboard holes: 6.4mm standard (1/4" diameter)
- Peg diameter: 5.8mm (0.6mm clearance → snug fit, no rattle)
- Too small (5.5mm): peg rattles in hole, hook falls out under load
- Too large (6.0mm): peg doesn't fit, requires reaming

**Calibration procedure**:
1. Print one small hook with standard peg (5.8mm): `sku-batch-2.py --product pegboard-hook --output-dir ./test_stl/`
2. Test-fit on standard 1/4" pegboard
   - Peg should insert with light friction (not loose, not forced)
   - Hook should hang level (no tilt under 1kg weight)
3. Hang load test: 2kg weight on hook
   - Hook should not deflect, peg should not rotate
   - If peg rotates: too small, increase to 5.9mm
   - If peg doesn't fit: too large, decrease to 5.7mm

### Test-Print Sequence

```
1. Print 9 hook prototypes (3 of each size: S, M, L)
   - Print time: 120-160 min total
   - Build plate space: ~200 × 200mm (all fit in 2-3 plate orientations)
   - Infill: 25%, walls: 3, layer height: 0.20mm

2. Post-process:
   - Cool 30 min
   - Remove support (if any)
   - Test fit on pegboard (see tolerance section)
   - If any pegs are loose/tight: adjust and reprint 1

3. Load testing (mechanical):
   - Small hook: hang 2kg load for 5 min — no deflection
   - Medium hook: hang 5kg load — no deflection
   - Large hook: hang 10kg load — no deflection

4. Aesthetic check:
   - Embossed text readability (should be clear from 1m distance)
   - Surface finish (should be smooth, no layer lines visible)
   - Color consistency (all hooks match)

5. Documentation:
   - Photo: all 3 sizes side-by-side
   - Photo: close-up of embossed text on one hook
   - Photo: loaded pegboard with all 3 sizes
```

---

## Test-Print Scheduling

### Week of May 6-12 (ModRun Test Print)

Focus: ModRun rail + clip finalize tolerance calibration.
Batch 2: **Prepare but do not print** (confirm CadQuery scripts are tested, no syntax errors).

```bash
# Week of May 6: Verify all scripts compile without errors
cd projects/mfg-farm
python cadquery/sku-batch-2.py --product magnetic-label --output-dir /tmp/test_stl/ 2>&1 | head -20
# Expected: "Exported: /tmp/test_stl/magnetic-label.stl" (no errors)
```

### Week of May 13-19 (Batch 2 Test-Print)

**Precondition**: ModRun test print PASSED (tolerance calibration done).

**Execution**:
1. Monday 5/13: Print magnetic labels (40-60 min) + plant marker (20-25 min) in parallel
2. Tuesday 5/14: Tolerance adjustments if needed (reprint any failures)
3. Wednesday 5/15: Print pegboard hooks (120-160 min across 2-3 plates)
4. Thursday 5/16-17: Load testing + aesthetic checks
5. Friday 5/18: Documentation photos + git commit

**Plate layout** (Bambu P1S, ~250×250mm build area):
- Plate 1: 5 magnetic label tiles (50-60 min)
- Plate 2: 1 plant marker + space for pegboard hooks (85-100 min)
- Plate 3: remaining pegboard hooks (80-100 min)

### Week of May 20-26 (Photography & Listing)

Once Batch 2 prototypes print successfully:
1. Professional photography (phone or light tent)
   - Magnetic labels: top view (text), bottom view (magnet), mounted on steel
   - Plant markers: garden setting (if possible), ground-stake detail
   - Pegboard hooks: on pegboard with tools hanging, 3 sizes together
2. Etsy listing copy (refine from product-line-strategy.md)
3. Pricing validation (A/B price test: standard $X vs. discounted $X-2 for first 50 sales)

---

## Material & Cost Summary

| Product | Material | COGS | Retail | Margin | Notes |
|---------|----------|------|--------|--------|-------|
| Magnetic Label | PLA+ | $0.17 | $1.50-2.00 | 72-76% | Sold in 20-packs |
| Plant Marker | ASA | $0.22 | $2.50-3.00 | 68-72% | UV-resistant, 5+ year outdoor life |
| Pegboard Hook (S) | PLA+ | $0.16 | $0.80-1.00 | 71% | Part of starter set |
| Pegboard Hook (M) | PLA+ | $0.19 | $1.00-1.25 | 71% | Part of starter set |
| Pegboard Hook (L) | PLA+ | $0.22 | $1.25-1.50 | 71% | Part of starter set |

**Filament sourcing**:
- PLA+ (black or color): eSUN/Overture 10kg spool = $12-15 (already in use for ModRun)
- ASA (white or color): Bambu Lab AMS-compatible spool = $18-22 per kg (new order, AliExpress 5-7 day lead time)

**Hardware sourcing**:
- N52 Magnets (Ø8mm × 2.2mm): 20-pack $0.40 AliExpress (FREE SHIPPING, 2 week lead)
- No other hardware required

---

## Post-Test-Print Execution

### Revenue Impact (Quarterly)

Q2 2026 (May 13-June 30 launch window):
- ModRun: 20 units/week × $12.99 = $259.80/week = $2,598 gross / 4 weeks
- Magnetic Labels: 15 units/week × $1.50/avg = $22.50/week = $225 gross / 4 weeks
- Plant Markers: 10 units/week × $2.75/avg = $27.50/week = $275 gross / 4 weeks
- Pegboard Hooks: 8 starter sets/week × $30 = $240/week = $2,400 gross / 4 weeks

**Total Q2 gross** (May 13-30 launch, 6 weeks): ~$1,850 gross
**Total Q3 (July-Sept, 13 weeks)**: ~$6,000+ gross (assumes ramp to 25-35 units/week per product)

### Next Steps (After Test-Print Pass)

1. **Week of May 27**: Finalize Etsy listing copy, pricing, tags for Batch 2 products
2. **Week of June 3**: Launch Batch 2 on Etsy (staggered: Labels → Markers → Hooks)
3. **Week of June 10**: Monitor conversion rate on Batch 2 products
4. **Week of June 17+**: Decide on Batch 3 (pegboard hooks seem to have highest engagement potential)

---

## Git Workflow

```bash
# After successful test prints, commit:
git add projects/mfg-farm/cadquery/sku-batch-2.py
git add projects/mfg-farm/SKU_BATCH_2_DESIGN_SPEC.md
git commit -m "feat(mfg-farm): SKU Batch 2 CadQuery designs (labels, markers, pegboard hooks) — ready for production test-print"
```

Once test-print tolerance is confirmed, update the cadquery script with final dimensions:

```bash
# Example (after Batch 2 test-print tolerance calibration)
git commit -m "fix(mfg-farm): SKU Batch 2 tolerance calibration — magnet pocket 8.0mm ✓, peg diameter 5.8mm ✓"
```

---

## Questions & Debugging

**Q: ASA print temperature too high — printing fails to adhere?**
A: Ensure Bambu P1S enclosure is closed, bed temperature is 100-110°C, and print speed is reduced to 100-120% of PLA speed (from Bambu default 150%). ASA requires more thermal stability.

**Q: Magnet pocket print fails (filament jam, ooze)?**
A: The Ø8mm pocket is small and requires good Z-resolution. Ensure:
- Layer height: 0.20mm (not 0.16mm, causes extrusion rate peaks)
- Nozzle diameter: 0.40mm standard
- If pocket diameter shows z-artifacts: temporarily increase to 8.2mm for first test, then calibrate downward

**Q: Embossed text doesn't print cleanly?**
A: Text extrusion depth is set to 0.3-0.4mm. If text prints as voids instead of raised:
- Reduce font size by 1-2pt (currently 8pt for labels, 5pt for hooks, 4pt for pegboard text)
- OR increase extrusion distance to 0.5mm

---

## Files Reference

- **CadQuery designs**: `projects/mfg-farm/cadquery/sku-batch-2.py`
- **Product strategy**: `projects/mfg-farm/product-line-strategy.md`
- **Cost model**: `projects/mfg-farm/cost-model-spreadsheet.csv`
- **Modrun calibration**: `projects/mfg-farm/modrun_clip.py`, `modrun_rail.py`
