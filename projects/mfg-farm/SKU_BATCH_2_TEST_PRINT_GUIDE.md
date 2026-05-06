---
title: SKU Batch 2 — Test-Print Guide
project: mfg-farm
created: 2026-05-06
status: READY (execute week of May 13–19, post-ModRun gate)
related: SKU_BATCH_2_DESIGN_SPEC.md, cadquery/sku_batch_2_magnetic_labels.py, cadquery/sku_batch_2_plant_markers.py, cadquery/sku_batch_2_pegboard_hooks.py
---

# SKU Batch 2 Test-Print Guide

**Gate condition**: Execute this guide only after ModRun test print passes tolerance calibration.

**Goal**: Print one functional prototype of each Batch 2 product, calibrate tolerances, document settings, and confirm print quality before batch production.

---

## Generating STL Files

Run from the repo root after installing build123d (`uv pip install build123d` or `pip install build123d`):

```bash
# Magnetic labels — 6 variants
python projects/mfg-farm/cadquery/sku_batch_2_magnetic_labels.py \
  --all --output-dir projects/mfg-farm/stl/batch2/

# Plant markers — 8 variants
python projects/mfg-farm/cadquery/sku_batch_2_plant_markers.py \
  --all --output-dir projects/mfg-farm/stl/batch2/

# Pegboard hooks — 3 sizes (default labels)
python projects/mfg-farm/cadquery/sku_batch_2_pegboard_hooks.py \
  --all-sizes --output-dir projects/mfg-farm/stl/batch2/
```

For the initial test-print, one of each type is sufficient:

```bash
python projects/mfg-farm/cadquery/sku_batch_2_magnetic_labels.py \
  --label BOLTS --output-dir projects/mfg-farm/stl/batch2/

python projects/mfg-farm/cadquery/sku_batch_2_plant_markers.py \
  --plant TOMATO --output-dir projects/mfg-farm/stl/batch2/

python projects/mfg-farm/cadquery/sku_batch_2_pegboard_hooks.py \
  --size small --output-dir projects/mfg-farm/stl/batch2/
```

---

## Product 1: Magnetic Workshop Bin Labels

### Print Settings (PLA+)

| Parameter | Value | Notes |
|-----------|-------|-------|
| Layer height | 0.20mm | 0.16mm not needed — increases print time without quality gain |
| Infill | 25% | Grid or gyroid; label tiles don't take mechanical load |
| Walls | 3 | 3 perimeters give adequate stiffness at 3mm thickness |
| Hotend | 220–225°C | Standard PLA+ (same as ModRun) |
| Bed | 60°C | PEI plate, no brim required |
| Fan | 100% after layer 3 | Full cooling for sharp text edges |
| Supports | None | Flat tile, no overhangs |
| Orientation | Flat — text face UP | Text printed last = best surface detail |
| Speed | Standard (150–200mm/s) | Reduce to 100mm/s if text edges show ringing |

### Expected Print Times and Material

| Quantity | Time | Filament | Notes |
|----------|------|----------|-------|
| 1 tile | 8–12 min | ~11g | Single label test |
| 5 tiles (1 plate) | 40–55 min | ~55g | Plate: BOLTS, BITS, TOOLS, SCREWS, NAILS |
| 20 tiles (batch) | ~160 min | ~220g | Full production batch (4 plates) |

### Critical Tolerance: Magnet Pocket (MAGNET_DIAMETER)

The magnet pocket diameter is the only tolerance-critical dimension on this product.

**Target**: N52 disc magnet (Ø8.0mm × 2.0mm) press-fits with firm hand pressure, holds without adhesive on vertical steel surface.

**Calibration procedure**:
1. Print 1 tile at default settings (MAGNET_DIAMETER = 8.0mm)
2. Press the N52 magnet into the rear pocket with thumb pressure
3. Evaluate fit:
   - **Good**: Magnet seats with moderate thumb pressure, does not rattle, holds tile against vertical steel surface
   - **Too tight** (magnet requires tool or pliers): Re-run with `--magnet-diameter 8.1` and reprint 1 tile
   - **Too loose** (magnet falls out with gentle tapping): Re-run with `--magnet-diameter 7.9` and reprint 1 tile
4. Record the successful diameter in the script constants for all subsequent exports

**Adhesion test**: Place calibrated tile on vertical steel surface (toolbox door, fridge). Apply 1 kg downward load for 60 seconds. Tile should not slide.

### Success Criteria

- [ ] Embossed text is crisp and legible from 60cm
- [ ] Tile corners are smooth (no sharp edges from fillet)
- [ ] Magnet pocket accepts N52 magnet with hand pressure
- [ ] Magnet holds tile against vertical steel surface under 1 kg load
- [ ] No warping or delamination visible on underside

---

## Product 2: UV-Resistant Garden Plant Markers

### Print Settings (ASA — read carefully, differs from PLA)

| Parameter | Value | Notes |
|-----------|-------|-------|
| Layer height | 0.20mm | Same as PLA — 0.20mm optimal for text quality |
| Infill | 25% | Grid pattern |
| Walls | 3 | 3 perimeters; increase to 4 if stake bends under load |
| **Hotend** | **240–250°C** | CRITICAL — ASA at 220°C causes poor adhesion between layers |
| **Bed** | **100–110°C** | CRITICAL — ASA at 60°C will warp and lift from plate |
| **Enclosure** | **CLOSED** | Bambu P1S: close all panels. Open enclosure = warp guaranteed |
| Fan | Off for first 5 layers, then 20–30% max | ASA needs thermal stability |
| Supports | None | Print with stake end UP |
| Orientation | Stake tip pointing UP, body face (+Z) toward front | Best text quality; no support needed |
| Speed | 100–120% of default | Reduce from P1S default (150–200%) for better ASA adhesion |

**Bambu P1S slicer profile**: Use "ASA" filament profile, not "PLA". The profile sets hotend/bed temperatures and fan curves automatically. Verify temperatures in preview before sending to printer.

### Expected Print Times and Material

| Quantity | Time | Filament | Notes |
|----------|------|----------|-------|
| 1 marker | 20–25 min | ~14g | Single marker test |
| 3 markers (1 plate) | 60–75 min | ~42g | TOMATO, BASIL, SAGE |
| 10 markers (batch) | ~200 min | ~140g | Full 10-pack batch |

### Critical Tolerance: Ground Stake (STAKE_WIDTH)

**Target**: Stake inserts cleanly into garden soil with hand pressure, holds upright under 500g lateral load without bending.

**Calibration procedure**:
1. Print 1 marker at default settings (STAKE_WIDTH = 8.0mm)
2. Test soil insertion in a small pot of damp garden soil:
   - **Good**: Stake pushes in with consistent hand pressure; marker stands vertical; no deflection when you push the top laterally
   - **Too wide** (stake splits or requires mallet): Re-run with `--stake-width 7.7` and reprint
   - **Too narrow** (stake bends under lateral load): Re-run with `--stake-width 8.3` and reprint
3. Note: ASA's mechanical properties are slightly different from PLA — stake may need wider cross-section than an equivalent PLA print

**UV durability baseline**: Place one marker outside in direct sunlight on the test-print date. Photograph it. Check again at 30 days for discoloration or surface degradation. Expect zero change with ASA.

### ASA Warping Troubleshooting

If the marker warps during printing (lifts from plate on one end):

1. Increase bed temperature to 110°C
2. Reduce fan speed to 15% (or off for all layers)
3. Add a brim (5mm) in slicer — remove after printing
4. Verify enclosure temperature is >40°C before starting (pre-heat enclosure 10 min)
5. If still warping: try first-layer height 0.25mm (improves bed adhesion for ASA)

### Success Criteria

- [ ] Marker prints without lifting or warping
- [ ] No layer delamination visible (hold up to light — should not see separation)
- [ ] Embossed text is legible from 30cm at eye level
- [ ] Stake penetrates damp soil cleanly with hand pressure
- [ ] Marker stands vertical in soil without support
- [ ] Stake does not deflect noticeably when top is pushed laterally (1 kg force)

---

## Product 3: Pegboard Hook System (3 Sizes)

### Print Settings (PLA+)

| Parameter | Value | Notes |
|-----------|-------|-------|
| Layer height | 0.20mm | Standard |
| Infill | **40%** | Higher than labels — hooks take real mechanical load |
| Walls | **4** | One extra vs. labels — resists shear from hanging weight |
| Hotend | 220–225°C | Standard PLA+ |
| Bed | 60°C | PEI plate |
| Fan | 100% after layer 3 | Full cooling |
| Supports | None | Print peg-up (see orientation) |
| Orientation | Peg UP (+Y), arm extending forward | Peg layers horizontal = maximum tensile strength |
| Speed | Standard | Reduce to 100mm/s for peg cylinder for dimensional accuracy |

**Peg printing tip**: Bambu P1S tends to run slightly fast on small cylindrical features. If peg diameter measures consistently oversize (caliper check), reduce outer wall speed to 80mm/s in Bambu Studio for this model only.

### Expected Print Times and Material

| Size | Time | Filament | Notes |
|------|------|----------|-------|
| Small | 12–15 min | ~12g | 35mm arm depth |
| Medium | 15–18 min | ~15g | 45mm arm depth |
| Large | 18–22 min | ~17g | 55mm arm depth |
| 9 hooks (3×S, 3×M, 3×L) | 135–165 min | ~126g | Full test-print set — 3 plates |

### Build Plate Layout (250×250mm Bambu P1S)

Plate 1 (small hooks): 3× small hooks, arrange peg-up in a row. Estimated: ~40–45 min.
Plate 2 (medium hooks): 3× medium hooks. Estimated: ~50–55 min.
Plate 3 (large hooks): 3× large hooks. Estimated: ~55–65 min.

Alternatively, mix sizes on one plate if build area allows — check no hooks collide in slicer preview.

### Critical Tolerance: Peg Diameter (PEG_DIAMETER)

The peg inserts into a standard 1/4" (6.35mm) pegboard hole. Default peg OD is 5.8mm.

**Calibration procedure**:
1. Print 1 small hook at default settings (PEG_DIAMETER = 5.8mm)
2. Test-fit on your actual pegboard:
   - **Good**: Peg inserts with light friction; hook hangs level; no rattle when you wiggle it
   - **Too loose** (peg rattles, hook rotates under load): Re-run with `--peg-diameter 5.9` and reprint 1 hook
   - **Too tight** (peg won't insert or requires mallet): Re-run with `--peg-diameter 5.7` and reprint 1 hook
3. Check with digital calipers after printing — FDM cylinders often print 0.1–0.2mm undersize due to cooling. Measure actual OD and adjust accordingly.

**Note**: Peg hole diameters vary between pegboard brands (6.0–6.5mm). If you have non-standard pegboard, measure your hole diameter first and set PEG_DIAMETER = (hole_diameter - 0.5mm).

### Load Testing

After tolerance calibration:

| Size | Test Load | Duration | Pass Criteria |
|------|-----------|----------|---------------|
| Small | 2 kg | 5 min | No arm deflection, peg stays in hole |
| Medium | 5 kg | 5 min | No arm deflection, peg stays in hole |
| Large | 10 kg | 5 min | <2mm arm tip deflection, peg stays in hole |

Use a luggage scale or calibrated weights. Hang from arm tip (worst-case load position).

### Success Criteria

- [ ] Peg inserts into pegboard with moderate hand pressure
- [ ] Hook hangs level (arm parallel to floor when loaded)
- [ ] Peg does not rotate or pull out under rated load
- [ ] Embossed text is legible from 1m distance (label readability test)
- [ ] No arm deflection beyond 2mm under rated load
- [ ] Fillets and corners are clean — no sharp edges

---

## Test-Print Schedule (Week of May 13–19)

| Day | Activity | Duration |
|-----|----------|----------|
| Monday 5/13 | Generate all STL files; print magnetic labels (1 tile test) | 30–60 min |
| Monday 5/13 | Print plant marker (1 marker, ASA — separate from PLA print) | 25–30 min print |
| Tuesday 5/14 | Tolerance calibration — magnet pocket + stake width | 30–60 min |
| Tuesday 5/14 | Print pegboard hooks (9 hooks, 3 plates) | 135–165 min unattended |
| Wednesday 5/15 | Peg tolerance calibration + load testing | 45–60 min |
| Thursday 5/16 | Documentation photos — all three products | 30–45 min |
| Friday 5/17 | Git commit with calibrated parameters; update PROJECTS.md | 15 min |

Total active effort: approximately 4–5 hours across the week (mostly unattended print time).

---

## Material Checklist Before Printing

- [ ] PLA+ filament loaded in P1S (same spool as ModRun — no changeover needed)
- [ ] ASA filament ordered and received (Bambu Lab AMS-compatible spool, 5–7 day AliExpress lead time — order now if not yet ordered)
- [ ] N52 Ø8mm × 2mm magnets received (20-pack AliExpress, 2-week lead — order now)
- [ ] Digital calipers available for peg OD and magnet pocket measurement
- [ ] Small pot with damp garden soil for stake insertion test
- [ ] Metal surface for magnet adhesion test (toolbox, fridge, steel shelf)
- [ ] Standard 1/4" pegboard panel for peg fit test

---

## Common Failure Modes and Fixes

**Magnetic labels**

| Symptom | Cause | Fix |
|---------|-------|-----|
| Text looks flat, no raised surface | TEXT_DEPTH too small | Reprint with `--text-depth 0.5` |
| Text overhangs tile edge | Font too large for label width | Reduce TEXT_FONT_SIZE to 7pt in script |
| Magnet pocket has z-artifacts (ridges inside pocket) | Layer height artifact | Print at 0.20mm (not 0.16mm); pocket Ø8mm is narrow |
| Tile warps (edges lift) | Bed temp or PEI adhesion issue | Clean PEI with IPA; verify 60°C bed |

**Plant markers**

| Symptom | Cause | Fix |
|---------|-------|-----|
| Marker lifts from plate mid-print | ASA warping | Increase bed to 110°C, close enclosure, add brim |
| Layer delamination (splits horizontally) | Hotend too cool for ASA | Verify hotend at 245°C (not 220°C) |
| Stake snaps when pressed into hard soil | Too narrow or wrong orientation | Increase to 8.3mm width; confirm stake prints along Y-axis (not Z) |
| Text washed out / barely visible | Text depth too shallow | Reprint with `--text-depth 0.5` |

**Pegboard hooks**

| Symptom | Cause | Fix |
|---------|-------|-----|
| Peg too large for pegboard hole | FDM overextrusion on cylinders | Reduce outer wall speed to 80mm/s; reprint with `--peg-diameter 5.7` |
| Hook arm bends under light load | Infill too low | Reprint at 50% infill; verify 4 walls |
| Text not legible from 1m | Font size too small | Increase TEXT_FONT_SIZE to 5pt and reprint |
| Peg rotates under load | Peg too small | Reprint with `--peg-diameter 5.9` |

---

## Post-Test-Print Checklist

After all three products pass tolerance and load tests:

- [ ] Record calibrated MAGNET_DIAMETER in `sku_batch_2_magnetic_labels.py` (line constant at top)
- [ ] Record calibrated STAKE_WIDTH in `sku_batch_2_plant_markers.py`
- [ ] Record calibrated PEG_DIAMETER in `sku_batch_2_pegboard_hooks.py`
- [ ] Commit calibrated scripts: `git commit -m "fix(mfg-farm): SKU Batch 2 tolerance calibration complete"`
- [ ] Take product photos (see `post-test-print-doc-3-lifestyle-photography-brief.md`)
- [ ] Order ASA filament if not already done (Bambu Lab AMS-compatible, 1 kg minimum)
- [ ] Order N52 magnets if not already done (20-pack minimum; 100-pack for production)
- [ ] Update `product-line-strategy.md` with confirmed COGS (filament weight confirmed from print)
- [ ] Begin Etsy listing copy (adapt from design spec specs table)
- [ ] Update PROJECTS.md exploration queue item to COMPLETE
