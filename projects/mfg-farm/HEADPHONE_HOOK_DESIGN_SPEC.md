---
title: Headphone Hook — Design Specification & Manufacturing Guide
project: mfg-farm
created: 2026-05-06
status: production-ready
related: cadquery/headphone_hooks.py, product-line-strategy.md, cost-model-spreadsheet.csv
---

# Headphone Hook — Design Specification & Manufacturing Guide

**Product:** Desk-edge clamp with integrated headphone hook and cable-wrap post  
**Lead product:** Launch immediately post-ModRun test-print (Month 1 of expansion roadmap)  
**Target margin:** 76% net  
**Production status:** CadQuery design complete, ready for test-print validation  

---

## Part 1: Design Overview

### Product Concept

A parametric desk-edge clamp that grips desk thicknesses from 12–40mm and holds a headphone hook arm with integrated cable-wrap post. The clamp is designed to match the ModRun aesthetic and cross-sell directly to the existing ModRun buyer base.

**Key differentiator:** No other headphone hook design on Etsy or Printables includes both a desk-clamp grip AND an integrated cable-wrap post in the same assembly.

### Design File

- **File:** `cadquery/headphone_hooks.py`
- **Framework:** build123d (Python-native CAD)
- **CLI-ready:** Yes — generates parametric variants for 12mm, 25mm, 40mm desk thicknesses
- **Variants supported:**
  - Desk thickness: 12–40mm (adjustable via `FDM_TOLERANCE` constant)
  - Cable-wrap post: Optional (boolean flag)
  - Tolerance tuning: Exposed `FDM_TOLERANCE` parameter for post-test-print adjustments

---

## Part 2: Design Specifications

### Clamp Body Geometry

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Clamp body width** | 38mm | Left-to-right span when viewing from above |
| **Clamp body depth** | 28mm | Front-to-back depth; upper jaw only (lower jaw extends 22mm) |
| **Wall thickness** | 3.0mm | Minimum for PLA+ at 25% infill without support failure |
| **Upper arm thickness** | 4.0mm | Top jaw contact surface |
| **Lower arm thickness** | 4.0mm | Bottom jaw (under-desk) contact surface |
| **Lower jaw overhang** | 22.0mm | How far lower jaw extends under desk edge |
| **FDM tolerance** | 0.20mm | Clearance between jaw and desk (each side) — **CRITICAL** tolerance to validate post-test-print |
| **Jaw gap (total)** | desk_thickness + 0.4mm | Total gap for press-fit grip |

### Hook Arm Geometry

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Arm length** | 55mm | Horizontal reach forward from clamp body |
| **Arm width** | 20mm | Left-to-right width (side-to-side) |
| **Arm thickness** | 4.0mm | Vertical thickness for headphone headband support |
| **Arm angle** | 8 degrees | Slight upward tilt to prevent headphones sliding off |
| **Attachment height** | 25mm | Z-distance above top jaw contact surface |
| **Tip radius** | 6mm | Rounded end (prevents cable kinking) |
| **Overhang angle** | ≤45° | Print orientation allows no-support hook arm |

### Cable-Wrap Post Geometry

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Post height** | 30mm | Rises above hook arm attachment point |
| **Post diameter** | 8mm | Sized for 4–8mm cables with comfortable grip space |
| **Offset from centerline** | 15mm | Positioned toward clamp body, not at tip |
| **Top radius** | 2mm | Fillet to prevent cable abrasion |
| **Mount location** | Base of hook arm | Attaches where arm meets clamp body |

### Desk Protection

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Rubber pad pocket (upper jaw)** | 20×8×1.5mm | Recess for self-adhesive silicone feet |
| **Rubber pad pocket (lower jaw)** | 20×8×1.5mm | Recess for rubber pad under desk |
| **Pad material (recommended)** | 3M Bumpon SJ5302 or equivalent | 1.5mm self-adhesive silicone feet |

---

## Part 3: Manufacturing Specifications

### Print Settings (Bambu P1S)

**Default Profile (recommended for all variants):**

| Setting | Value | Rationale |
|---------|-------|-----------|
| **Layer height** | 0.20mm | Standard detail; faster than 0.1mm for this geometry |
| **Infill** | 25% (grid) | Sufficient for clamp jaw strength; balance with print time |
| **Wall perimeters** | 3 | 3.0mm wall thickness = 3 perimeters at 1.0mm line width |
| **Support** | None required | Hook arm angle ≤45°; no support islands |
| **Nozzle temp** | 220–225°C | PLA+ standard (eSUN/Overture default) |
| **Bed temp** | 60°C | PLA+ standard |
| **Print speed** | Default (Bambu Studio profile) | ~25–30 mm/s for perimeters; 60–80 mm/s for infill |
| **Cooling** | Enabled from layer 2 | PLA+ needs partial cooling for dimensional accuracy |

**Print Orientation:**

- **Clamp body:** Flat side down (jaw surface parallel to build plate)
- **Hook arm:** Pointing forward and slightly upward
- **Rationale:** Minimizes support material; uses natural gravity for overhangs

### Print Time & Weight

| Variant | Print Time | Estimated Weight | Notes |
|---------|-----------|------------------|-------|
| 12mm desk (thin) | 22–24 min | 22–24g | Smallest jaw gap; fastest print |
| 25mm desk (standard) | 25–26 min | 25–26g | Most common desk thickness |
| 40mm desk (thick) | 28–30 min | 28–30g | Standing desks, thick worktops |

**Total weight:** 22–30g including cable-wrap post. Post-print weight after rubber pads: +2g.

### Post-Print Finishing

1. **Remove support material:** None required; inspect for any bridging artifacts on hook arm.
2. **Inspect clamp jaw tolerances:**
   - Test-fit the hook on a test desk thickness (use wood shim or cardboard to simulate)
   - Jaw should grip firmly without requiring excessive force (< 10 lbs downward hand pressure)
   - If too tight: increase `FDM_TOLERANCE` by 0.1mm and reprint
   - If too loose: decrease `FDM_TOLERANCE` by 0.05mm and reprint
3. **Add rubber pads:**
   - Cut 3M Bumpon feet to fit the 20×8mm pocket recesses
   - Apply to upper jaw (desk contact) and lower jaw (underside)
   - Pads must be < 1.5mm thickness to fit pocket depth
4. **Visual inspection:**
   - Check hook arm for layer squish or bridging artifacts
   - Check cable post for any support remnants
   - Check rubber pad pocket recesses are clean (no stringy PLA)
5. **Optional finishing:**
   - Light sand (120–180 grit) the hook arm tip to remove any sharp edges
   - Vapor smooth (acetone) for glossy finish (optional, not required)

---

## Part 4: Tolerance Calibration (Critical Path Item)

The **FDM clamp jaw tolerance is the highest-risk dimensional tolerance in the entire design**. The difference between a perfectly gripping hook and a loose one is ±0.10mm.

### Tolerance Testing Protocol

**Pre-launch, execute this procedure on Bambu P1S:**

1. **Test Print #1: Baseline (FDM_TOLERANCE = 0.20mm)**
   - Print one 25mm desk variant on Bambu P1S using standard profile
   - Cool to room temperature (30 min)
   - Test-fit on 25mm wood shim (exact thickness)
   - **Acceptance criteria:**
     - Clamp can be applied by hand without excessive force (< 10 lbs)
     - Clamp does not fall off when shaken gently (non-slipping grip)
     - No binding or friction noise when applying/removing

2. **If PASS → Full production:** Proceed with the 0.20mm tolerance for all desk thicknesses.

3. **If FAIL (too tight):**
   - Increase `FDM_TOLERANCE` to 0.30mm in the code
   - Print variant #2
   - Test-fit and repeat

4. **If FAIL (too loose):**
   - Decrease `FDM_TOLERANCE` to 0.15mm in the code
   - Print variant #2
   - Test-fit and repeat

5. **Record final tolerance value:** Once passing, document the final `FDM_TOLERANCE` value and add a note to the git commit: "Tolerance calibrated for [printer/material/nozzle] — FDM_TOLERANCE=[X]mm."

6. **Print all three desk thicknesses (12mm, 25mm, 40mm):**
   - Validate that the same tolerance works across all three variants
   - Document any variation between thicknesses (e.g., 40mm may need ±0.05mm adjustment)

7. **Production lock-in:**
   - Once all three desk thicknesses pass, the tolerance is locked for production
   - Update the code constant in the default parameters
   - Any future print batches use this finalized tolerance value

**Why this matters:** The clamp jaw tolerance directly impacts customer satisfaction. Too tight = impossible to fit on desk = 1-star reviews. Too loose = headphones fall off = returned items. This is the do-or-die specification.

---

## Part 5: Material & Consumables

### Filament

| Material | Quantity (per unit) | Cost/unit | Notes |
|----------|-------------------|-----------|-------|
| **PLA+ (eSUN/Overture)** | 26g (average) | $0.34 | Standard material; 25° upward angle supports no-support printing |
| **PETG** | 26g | $0.34 | Alternative for workshop environments (no plastic smell concerns) |
| **ASA** | — | — | Not recommended; low strength for clamp jaw |

### Hardware & Consumables

| Item | Quantity | Cost | Notes |
|------|----------|------|-------|
| 3M Bumpon SJ5302 feet (or equiv.) | 2 per unit | $0.08 | Silicone feet for desk/underside protection |
| Poly mailer (6×9", 2.5mil) | 1 per order | $0.08 | Shipping package |
| Bubble wrap / packing material | ~10g | $0.05 | Protection in mailer |
| Etsy inserts / business cards | 1 per order | $0.10 | Cross-sell for ModRun bundle |
| **Total consumables** | — | **$0.31** | — |

### Total COGS Per Unit

| Component | Cost |
|-----------|------|
| Filament (26g PLA+ @ $0.013/g) | $0.34 |
| Rubber pads | $0.08 |
| Packaging / shipping materials | $0.23 |
| Post-print labor (assembly of pads, QC) | $0.15 (5 min @ $0.50/min) |
| **Total COGS** | **$0.80** |

**Comparison to ModRun:** ModRun COGS is $1.28 for a 72.9% margin at $4.50 sell price. Headphone hook COGS of $0.80 at $16 sell price = 95% gross margin before Etsy fees. At 76% net margin: $12.16 net profit per unit.

---

## Part 6: Variations & Product Tiers

### Variant A: Standard (Cable-Wrap Post Included)

- **For:** Desk-setup enthusiasts with cable management needs
- **Price:** $16 (single), or bundle with ModRun at $28 (cable mgmt combo)
- **COGS:** $0.80
- **Etsy listing:** Primary product listing

### Variant B: Minimal (Cable-Wrap Post Omitted)

- **For:** Users who prefer a cleaner aesthetic
- **Price:** $12 (single)
- **COGS:** $0.72 (no post = 8g less filament)
- **Etsy listing:** Secondary listing or variant SKU option
- **Strategy:** Offer at checkout: "Standard with cable post ($16)" vs. "Minimal without post ($12)"

### Variant C: Color Options

- **Available colors:** Black, white, natural PLA, dark gray, translucent smoke
- **Cost impact:** None (all use same filament cost, different color spools)
- **Etsy listing strategy:**
  - Primary: Single listing with color selection in personalization field at checkout
  - OR: Separate listing per color (tests which color sells best)

### Variant D: Desk Thickness Selection (Buyer-Specified at Checkout)

- **Etsy personalization field:** "Desk thickness (select one): 12mm / 25mm / 40mm"
- **Logic:** At order time, order management script generates correct STL variant and prints immediately
- **Advantage:** Single Etsy listing, custom-filled per order
- **Disadvantage:** Adds 5-minute STL generation per order (automation via Python + Bambu API possible but scope creep)
- **Initial recommendation:** Start with pre-generated inventory (12mm, 25mm, 40mm variants stocked), offer as variant selection in listing

---

## Part 7: Quality Assurance Checklist

**Pre-Production (Test Print Phase):**

- [ ] Tolerance calibration passes (Section 4 protocol)
- [ ] All three desk thicknesses (12, 25, 40mm) test-fit successfully
- [ ] Hook arm has no visible layer artifacts or bridging failures
- [ ] Rubber pad pockets are clean and accept Bumpon feet without gaps
- [ ] Cable-wrap post is round (no faceting from layer stacking)
- [ ] Cable post can hold 4–8mm cable loop without deforming

**Per-Batch Production (every 20-unit batch):**

- [ ] First hook of batch: full QC (all checks above)
- [ ] Random sample (every 5th unit): clamp jaw grip test
- [ ] Random sample: hook arm visual inspection
- [ ] 100% packaging: rubber pads applied, inserts included

**Per-Order Fulfillment:**

- [ ] Correct desk thickness variant shipped
- [ ] Rubber pads present on both jaw surfaces
- [ ] Etsy business card included (cross-sell ModRun)
- [ ] No visible defects or layer artifacts
- [ ] Weight within expected range (22–30g)

---

## Part 8: Design Tuning Guide (Post-Test-Print)

If the test print reveals issues, use this table to adjust the CadQuery parameters:

| Symptom | Adjustment | Parameter | Action |
|---------|-----------|-----------|--------|
| Clamp too tight on desk | Increase jaw gap | `FDM_TOLERANCE` | +0.10mm; reprint test variant |
| Clamp too loose / falls off | Decrease jaw gap | `FDM_TOLERANCE` | -0.05mm; reprint test variant |
| Hook arm too short for headphones | Extend reach | `HOOK_ARM_LENGTH` | +5–10mm; reprint and test fit |
| Headphones slide off hook | Increase upward angle | `HOOK_ARM_ANGLE` | +2–3°; reprint and test grip |
| Cable post too thin / bends under load | Thicken post | `CABLE_POST_DIAMETER` | +1–2mm; reprint and check print time |
| Print too heavy (packaging cost concern) | Reduce dimensions | `CLAMP_BODY_DEPTH` or `HOOK_ARM_WIDTH` | -2–3mm; retest grip/reach |
| Layer artifacts on hook arm | Improve cooling | Bambu Studio profile | Enable higher cooling fan percentage (≥ 50%) |
| Cable post cracks / brittleness | Reduce brittleness | Material change | Switch to PETG instead of PLA+ (same cost) |

---

## Part 9: Production Timeline

**Week 1 (Post-ModRun Test Print):**
- Execute tolerance calibration (Section 4)
- Print all three desk thickness variants
- Document final `FDM_TOLERANCE` value in git

**Week 2:**
- Prepare Etsy listing (copy, photos, tags, pricing)
- Print 60 units (3 variants × 20 units each for initial stock)
- QC and apply rubber pads

**Week 3:**
- Launch Etsy listing
- Begin printing to fulfill pre-orders (if any)
- Monitor first 10 customer reviews for jaw-grip feedback

**Month 2+:**
- Sustain 20-unit/week production
- Adjust variant mix based on customer feedback (if 12mm is underselling, reduce future batches)
- Monitor for tolerance drift on Bambu P1S (revalidate every 100 units or monthly, whichever comes first)

---

## Part 10: Known Constraints & Mitigation

### Constraint: FDM Jaw Tolerance Drift

**Issue:** 3D printer tolerances drift over time (wear, temperature variation, belt slop). A hook that fits perfectly today might be too tight or loose next month.

**Mitigation:**
- Revalidate tolerance every 100 units printed OR monthly, whichever comes first
- Keep a "reference desk sample" (25mm thickness hardwood or acrylic) in the print workspace
- Quick-fit test on reference sample: every 5th hook from the batch
- If grip changes, adjust `FDM_TOLERANCE` by ±0.05mm and print a test batch

### Constraint: Cable Post Fragility Under Impact

**Issue:** The 8mm diameter cable post is relatively thin. If someone yanks the cable hard, the post might fracture at the attachment point.

**Mitigation:**
- Use PETG instead of PLA+ (higher impact resistance) if customer damage reports occur
- Fillet the connection point between hook arm and cable post (already done: 2mm radius)
- In Etsy listing: include care note "Designed for cable loop wrapping, not cable yanking"

### Constraint: Desk Thickness Variant Management

**Issue:** Offering 3 desk thickness variants (12mm, 25mm, 40mm) complicates inventory and SKU management.

**Mitigation:**
- Start with 25mm as the default / primary SKU
- Offer 12mm and 40mm as custom-order options with 2–3 week lead time
- Simplifies initial inventory; scales SKU count only if customer demand justifies it

---

## Appendices

### Appendix A: CadQuery Design File Parameters

All parameters exposed at the top of `cadquery/headphone_hooks.py` for easy tuning:

```python
# Clamp body constants
CLAMP_BODY_WIDTH = 38.0           # mm
CLAMP_BODY_DEPTH = 28.0           # mm
CLAMP_WALL_THICKNESS = 3.0        # mm
CLAMP_ARM_THICKNESS = 4.0         # mm
CLAMP_LOWER_OVERHANG = 22.0       # mm
FDM_TOLERANCE = 0.20              # mm — CRITICAL CALIBRATION PARAM

# Hook arm constants
HOOK_ARM_LENGTH = 55.0            # mm
HOOK_ARM_WIDTH = 20.0             # mm
HOOK_ARM_THICKNESS = 4.0          # mm
HOOK_ARM_ANGLE = 8.0              # degrees
HOOK_TIP_RADIUS = 6.0             # mm
HOOK_ATTACHMENT_HEIGHT = 25.0     # mm

# Cable-wrap post constants
CABLE_POST_ENABLED = True         # Set False to omit post
CABLE_POST_HEIGHT = 30.0          # mm
CABLE_POST_DIAMETER = 8.0         # mm
CABLE_POST_OFFSET_X = 15.0        # mm

# Rubber pad pocket
PAD_POCKET_LENGTH = 20.0          # mm
PAD_POCKET_WIDTH = 8.0            # mm
PAD_POCKET_DEPTH = 1.5            # mm
```

### Appendix B: STL Export Command Reference

```bash
# Generate all three variants (12mm, 25mm, 40mm) to ./stl/ directory
python cadquery/headphone_hooks.py --output-dir ./stl/

# Generate single 25mm variant
python cadquery/headphone_hooks.py --desk-thickness 25 --output-dir ./stl/

# Generate custom thickness
python cadquery/headphone_hooks.py --desk-thickness 18 --output-dir ./stl/

# Generate without cable-wrap post
python cadquery/headphone_hooks.py --cable-post false --output-dir ./stl/

# Customize FDM tolerance (for post-test-print tuning)
python cadquery/headphone_hooks.py --tolerance 0.25 --output-dir ./stl/
```

### Appendix C: Print Profile JSON (Bambu Studio)

Save this profile as "headphone-hooks-pla-plus.json" in Bambu Studio for one-click loading:

```json
{
  "name": "Headphone Hooks — PLA+ (no support)",
  "material": "PLA+",
  "nozzle_diameter": 0.4,
  "layer_height": 0.2,
  "wall_thickness": 1.2,
  "infill_percentage": 25,
  "infill_type": "grid",
  "support": false,
  "nozzle_temperature": 220,
  "bed_temperature": 60,
  "cooling": true,
  "print_speed": "default"
}
```

---

**Document status:** PRODUCTION-READY  
**Last updated:** 2026-05-06  
**Next review:** After first test-print batch (tolerance validation)
