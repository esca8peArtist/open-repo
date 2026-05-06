---
title: Expansion Products Manufacturing Specs & CadQuery Designs
project: mfg-farm
created: 2026-05-06
status: ready-to-execute
confidence: high — based on product-line-strategy.md research (May 2026)
related: product-line-strategy.md, production-workflow-v1.md, cost-model-spreadsheet.csv
---

# Expansion Products Manufacturing Specifications

**Status**: Pre-test-print research and design staging. Ready for immediate CadQuery implementation upon test-print success (May 2026).

**Deliverable for orchestrator**: When test print succeeds, execute designs in this sequence: (1) Headphone Hook, (2) Magnetic Bin Labels, (3) Garden Plant Markers, (4) Pegboard Hook System, (5) Monitor Riser Legs.

---

## Overview & Design Philosophy

All five products follow the ModRun design-to-production workflow:
1. **Parametric CadQuery design** with user-configurable variables (desk thickness, height, text, colors)
2. **Bambu Studio optimization** for batch printing (nesting, support strategy, print orientation)
3. **Etsy personalization** fields for buyer customization (text input, dimension selection)
4. **Manufacturing template** (reusable print profiles, part nesting, post-processing checklist)

This document specifies the CadQuery geometry, manufacturing parameters, and production workflow for each product. All designs are **original CadQuery work** with git-timestamped commit history (Etsy June 2025 compliance).

---

## Product 1: Desk Headphone Hook

### Overview
- **Target price**: $14–$18 single unit, $45–$55 bundle with ModRun
- **Margin**: 76% net
- **Design complexity**: Low–Medium (parametric clamp + hook arm + cable wrap)
- **Print time per unit**: 45 min
- **Lead time for launch**: 7–10 days post-test-print (fastest to market)

### CadQuery Design Specification

**Variables** (parametric inputs):
```
desk_thickness_mm: 10–40  # clamp jaw opening, default 25
arm_length_mm: 120–180    # hook arm overhang, default 140
wrap_post: True/False     # cable-wrap post enabled, default True
color_name: "black", "white", "gray", "blue", "red"  # Etsy variant
mount_style: "under-desk", "edge-clamp"  # two mount options
```

**Geometry**:
1. **Clamp base** (50 × 50 × 30mm body)
   - Two-jaw clamp mechanism with M4 threaded screw (nut insert, heat-set on print)
   - Jaw faces: cork-texture imprint (2mm pattern) for grip
   - Inner jaw clearance: desk_thickness + 1mm (parametric)
   - Screw hole spacing: 25mm (IKEA CAPITA hardware compatible, optional)

2. **Hook arm** (Ø 20mm cylindrical, arm_length_mm overhang)
   - Tapering to Ø 16mm at tip
   - Smooth radius bends (R=15mm) at junction to base (no sharp angles)
   - Strength analysis: support 500g sustained (headphone weight + cable slack)

3. **Cable-wrap post** (if enabled)
   - Ø 8mm post extending 30mm above hook arm
   - Five spiral grooves (4mm wide, 2mm deep) for cable routing
   - Grooves pre-shaped to wrap standard 3.5mm and USB-C cables
   - Optional: embossed ModRun logo (5mm) on clamp face

4. **Mounting variants**
   - Under-desk: two dowel holes (Ø 6mm) for M6 wood screws to desk underside
   - Edge-clamp: screw-clamp mechanism (M4) for 10–40mm desk edge thickness

**CadQuery snippet** (pseudocode):
```python
import cadquery as cq

def create_headphone_hook(
    desk_thickness=25, arm_length=140, 
    wrap_post=True, mount_style="under-desk"
):
    # Clamp base with jaw mechanism
    clamp_base = cq.Workplane("XY").box(50, 50, 30, centered=True)
    
    # Parametric jaw clearance
    jaw = clamp_base.faces(">Z").workplane() \
        .slot2D(30, desk_thickness + 1) \
        .cutBlind(-10)
    
    # Hook arm (smooth curve from base)
    hook_arm = jaw.faces(">Z").workplane().moveTo(10, 0) \
        .spline([(0, 0), (50, 0), (arm_length, 0)]) \
        .sweep(cq.Workplane("XY").circle(10))
    
    # Cable wrap post
    if wrap_post:
        wrap = hook_arm.faces(">Z").workplane().moveTo(arm_length, 0) \
            .circle(4).extrude(30)
        # Add spiral grooves for cable routing
        wrap = add_spiral_grooves(wrap, num_grooves=5, groove_depth=2)
    else:
        wrap = hook_arm
    
    # Mount holes based on style
    if mount_style == "under-desk":
        final = add_dowel_holes(wrap, hole_dia=6, spacing=25)
    else:  # edge-clamp
        final = add_clamp_screw_hole(wrap)
    
    return final
```

### Manufacturing Parameters

**Bambu P1S profile**:
- **Material**: PLA+ (eSUN or Overture)
- **Temperature**: 220°C nozzle, 55°C bed
- **Speed**: standard (100 mm/s)
- **Layer height**: 0.2mm
- **Support**: minimal tree supports under clamp jaw only (12% support density)
- **Print orientation**: horizontal (hook arm parallel to plate) — minimizes supports
- **Plate nesting**: 4–6 hooks per plate run (Bambu Studio auto-arrange)
- **Print time per hook**: 45–55 min
- **Post-processing**: remove supports (5 min), 100-grit sanding on clamp jaw (2 min), heat-set nut insert for M4 screw (1 min, heat gun)

**Quality gates**:
1. Visual: no layer lines visible on hook arm (critical for aesthetics)
2. Mechanical: clamp jaw grips 25mm test rod without slipping (cork texture must have texture)
3. Assembly: M4 screw inserts smoothly into heat-set nut

### Etsy Listing Skeleton

**Title**: "Desk Headphone Hanger | 3D Printed Under-Desk Clamp | Custom Desk Cable Manager [Color]"

**Price**: $16.00 (single), $45.99 (bundle with ModRun starter set)

**Variants**: 5 colors (black, white, gray, blue, red)

**Personalization fields**:
- "Desk thickness (10–40mm, default 25mm) — provide exact measurement"
- "Mount style: under-desk OR edge-clamp"
- "Include cable-wrap post? Yes / No"

**Key selling points** (in description):
- Fully parametric — matches your exact desk thickness
- Integrated cable-wrap post prevents cable slack
- Complements ModRun modular rail system
- 3D-printed in PLA+ for durability
- Original design (git-timestamped, Etsy compliant)

**Photography requirements**:
- Mounted on desk with headphones hung; ModRun rails visible in background
- Close-up of cable-wrap post with cable routed through grooves
- Top-down view showing clamp jaw on edge-clamp variant
- Lifestyle shot: complete desk setup with hook + riser + ModRun

### Launch Timeline
- Design: 2–3 days (CadQuery build + test prints of 3 thickness variants)
- Photography: 1 day (reuse existing desk setup backdrop)
- Listing creation: 1 day (Etsy template, variant configuration, personalization fields)
- **Ready for listing**: Day 7–8 post-test-print

---

## Product 2: Magnetic Workshop Bin Labels

### Overview
- **Target price**: $18–$32 per 10-pack, $40–$55 for 20-pack
- **Margin**: 72–76% net
- **Design complexity**: Low (flat tile + magnet pocket + text emboss)
- **Print time per unit**: 2–3 min (30 tiles per plate)
- **Lead time for launch**: 10–14 days (magnet supply chain)
- **Special material**: N52 disc magnets (15×3mm), AliExpress lead time 7–14 days

### CadQuery Design Specification

**Variables**:
```
tile_width_mm: 50     # flat label tile
tile_depth_mm: 25     # depth (left-right)
tile_height_mm: 4     # thin label format
magnet_dia: 15        # N52 disc magnet diameter (fixed)
magnet_depth: 3.1     # pocket depth (magnet thickness + 0.1mm press fit)
text_content: "DRILLS", "BITS", "CABLES", etc.  # buyer-specified
text_height_mm: 3.5   # embossed text size
```

**Geometry**:
1. **Flat tile** (50 × 25 × 4mm base)
   - Rounded corners (R=2mm) for hand comfort
   - Slight dome top (1mm curve) for visual appeal
   - Bottom surface flat and smooth for magnet grip

2. **Magnet pocket** (on underside, recessed)
   - Circular pocket: Ø 15mm × 3.1mm deep (0.1mm interference fit for N52 disc)
   - Pocket positioned 12mm from left edge (centered in recess zone)
   - Pocket design prevents magnet from popping out under normal use (~5 lbf holding force per N52 spec)

3. **Embossed text** (on top surface)
   - CadQuery text module: 3.5mm height, sans-serif font (Optima or similar)
   - Emboss depth: 1.5mm (readable but subtle)
   - Text centered on tile
   - Custom buyer text via Etsy personalization field

4. **Variant: Blank tile**
   - Same geometry, no embossed text, allows buyer to add adhesive labels after purchase

**CadQuery snippet** (pseudocode):
```python
import cadquery as cq

def create_magnetic_label_tile(
    text_content="DRILLS",
    width=50, depth=25, height=4
):
    # Base flat tile with rounded corners
    base = cq.Workplane("XY").box(width, depth, height, centered=True) \
        .edges("|Z").fillet(2)  # round corners
    
    # Dome on top
    dome = base.faces(">Z").workplane().sphere(50, centered=True) \
        .intersect(cq.Workplane("XY").box(width, depth, 2, centered=True))
    
    # Magnet pocket on underside
    pocket = dome.faces("<Z").workplane() \
        .moveTo(0, 0).circle(7.5).cutBlind(-3.1)  # 0.1mm press fit
    
    # Embossed text on top
    text_solid = cq.Workplane("XY").text(
        text_content, fontsize=3.5, distance=1.5,
        font="optima"
    )
    
    final = pocket.union(text_solid)
    return final
```

### Manufacturing Parameters

**Bambu P1S profile**:
- **Material**: PLA+ (black preferred for contrast with magnet)
- **Temperature**: 220°C nozzle, 55°C bed
- **Speed**: standard (100 mm/s)
- **Layer height**: 0.2mm
- **Support**: none (flat tiles print without supports)
- **Print orientation**: tile laying flat (Z-axis = 4mm height)
- **Plate nesting**: 30 tiles per plate run (Bambu Studio array: 6×5 grid)
- **Print time per plate**: 60–90 min (batch of 30 = 2–3 min per tile)
- **Post-processing**: 
  1. Remove tiles from plate (5 min for 30)
  2. Heat-set magnet inserts: preheat tile pocket to 60°C, press N52 disc 1mm deeper (slight sinking), allow to cool. Magnet locks via plastic deformation (~5 min for 30 tiles in batches)
  3. Inspect text clarity (should be crisp emboss)
  4. Wipe with damp cloth for clean finish

**Magnet insertion quality check**:
- Magnet should sit flush with tile bottom (no protruding edges)
- Pull test: 3–5 lbf to remove magnet from tile (verify press fit holds)
- Polarity: check with test metal rod — should hold firmly to ferrous surface

### Etsy Listing Skeleton

**Title**: "Magnetic Workshop Labels | Custom Text Bin Labels 3D Printed | Toolbox Organizer [Qty]"

**Price**: $18.00 (10-pack), $28.00 (20-pack)

**Variants**: 3 quantities (10-pack, 20-pack, blank 10-pack)

**Personalization fields**:
- "Enter category names (one per line, max 10 for 10-pack, max 20 for 20-pack). Examples: DRILLS, BITS, CABLES, SCREWDRIVERS."
- "Include magnets? Yes (recommended) / No (blank tiles, add your own labels)"

**Key selling points**:
- Fully customizable — buyer-specified category text
- Strong N52 magnets for secure hold on any ferrous surface
- Works on metal toolboxes, filing cabinets, storage shelves, workshop pegboards
- Professional embossed text (not vinyl sticker)
- Reusable and repositionable
- Original design, 3D-printed on demand

**Photography requirements**:
- Close-up: tiles on actual metal toolbox or magnetic whiteboard
- Lifestyle: workshop/garage setting with labeled storage visible
- Detail: macro shot showing magnet pocket and embossed text clarity
- Before/after: disorganized bins → organized bins with labels

### Launch Timeline
- **Material lead time**: Order N52 magnets (7–14 days from AliExpress)
- **Design**: 2 hours (CadQuery tile + text module + pocket test print)
- **Test prints**: 1 batch (30 tiles with magnets, quality check insertion)
- **Photography**: 1 day
- **Listing creation**: 1 day
- **Ready for listing**: Day 10–12 post-test-print (waiting on magnet delivery)

---

## Product 3: Garden Plant Markers

### Overview
- **Target price**: $16–$34 per set (6, 10, or 20 stakes)
- **Margin**: 68–72% net
- **Design complexity**: Low–Medium (flag-stake design with text emboss)
- **Print time per unit**: 5–6 min (20 stakes per plate)
- **Material**: ASA filament (UV-resistant, 5+ year outdoor life)
- **Lead time for launch**: 14–21 days (ASA calibration + test prints)

### CadQuery Design Specification

**Variables**:
```
plant_name: "Tomato", "Basil", "Carrot", etc.  # buyer-specified
flag_width_mm: 30    # label flag width
flag_height_mm: 25   # label flag height
flag_thickness_mm: 6 # thickness for text emboss
stake_length_mm: 150 # ground stake height
stake_diameter_mm: 4 # stake diameter (fits soil easily)
ground_depth_mm: 80  # depth for soil insertion
text_height_mm: 2.5  # embossed text on flag
color: "terracotta", "sage", "white", "black"  # ASA variant
```

**Geometry**:
1. **Flag assembly** (30 × 25 × 6mm)
   - Rectangular tag with rounded top corners (R=3mm)
   - Embossed plant name on front (2.5mm height, 1.5mm depth)
   - Back surface flat (for potential adhesive labels)
   - Mounting post: 12mm square connector at bottom

2. **Stake** (Ø 4mm, 150mm total length)
   - Top 70mm: standard stake for soil grip
   - Bottom 80mm: slightly tapered (Ø 4.5mm to Ø 3.8mm) for soil insertion
   - Strength: support 300g lateral load (wind resistance + marker weight)
   - Grain-texture surface (helps with soil traction, added via texture emboss)

3. **Flag-to-stake connection**
   - Heat-set brass insert (M3) in mounting post
   - Allows flag to pivot slightly (±15°) without breaking
   - M3 screw: ~$0.01 BOM addition

4. **Text emboss**
   - Plant name embossed 1.5mm deep on flag face
   - Font: sans-serif (Optima or similar)
   - Readable from 1.5m distance (outdoor garden use case)

**CadQuery snippet** (pseudocode):
```python
import cadquery as cq

def create_garden_stake(
    plant_name="Tomato",
    flag_width=30, flag_height=25,
    stake_length=150, stake_dia=4
):
    # Flag assembly (30 × 25 × 6mm)
    flag = cq.Workplane("XY").box(flag_width, flag_height, 6, centered=True) \
        .faces("+Y").fillet(3)  # rounded top
    
    # Embossed text on flag front
    text_solid = cq.Workplane("XY") \
        .text(plant_name, fontsize=2.5, distance=1.5, font="optima")
    flag_with_text = flag.union(text_solid)
    
    # Mounting post (M3 insert pocket)
    mounting_post = cq.Workplane("XY").moveTo(0, -15) \
        .circle(2).extrude(12)
    flag_final = flag_with_text.union(mounting_post)
    
    # Stake (Ø 4mm, 150mm length, tapered at bottom)
    stake = cq.Workplane("XY").moveTo(0, -15) \
        .circle(2).extrude(70) \
        .faces(">Z").workplane() \
        .cone(0.3, 80)  # taper from 4mm to 3.8mm
    
    # Heat-set insert pocket (M3)
    insert_pocket = cq.Workplane("XY").moveTo(0, -15) \
        .circle(1.5).cutBlind(-10)  # pocket for M3 insert
    
    final = flag_final.union(stake).union(insert_pocket)
    return final
```

### Manufacturing Parameters

**Material & Profile**:
- **Material**: ASA (UV-resistant, Overture or eSUN ASA)
- **Temperature**: 245°C nozzle, 100°C bed (critical for ASA)
- **Enclosure**: Bambu P1S enclosure MUST be closed during print (ASA warps in open air)
- **Speed**: standard (100 mm/s, no fast mode for ASA)
- **Layer height**: 0.2mm
- **Support**: minimal supports under flag only (tree support, 8% density)
- **Print orientation**: stake vertical (Z-axis = 150mm), flag horizontal
- **Plate nesting**: 20 stakes per plate (Bambu Studio auto-arrange)
- **Print time per plate**: 90–120 min (5–6 min per stake)
- **Post-processing**:
  1. Remove from plate (10 min for 20)
  2. Remove supports around flag (5 min)
  3. Sand flat surfaces with 100-grit sandpaper (2 min per stake)
  4. Heat-set M3 brass inserts in mounting posts (1 min per stake, heat gun to 220°C)
  5. Insert M3 screw through flag + mounting post (pre-assemble)
  6. Wipe clean; allow ASA to cool completely (5 min)

**ASA profile calibration** (one-time setup):
- Print a test tower (5 × 5 × 50mm) with 3 wall layers
- Check for warping, oozing, stringing
- Adjust bed temp ±5°C and nozzle temp ±2°C if needed
- Save final profile as "ASA_Plant_Markers" in Bambu Studio

### Etsy Listing Skeleton

**Title**: "Garden Plant Markers | UV-Resistant 3D Printed Stakes | Personalized Plant Labels [Qty]"

**Price**: $16.00 (6-pack), $22.00 (10-pack), $34.00 (20-pack)

**Variants**: 3 quantities × 4 colors (12 SKUs total)

**Personalization fields**:
- "Enter plant names (one per line, max 6/10/20 depending on pack size). Examples: Tomato, Basil, Carrot, Lettuce, Pepper."
- "Color preference: terracotta, sage green, white, or black"

**Key selling points**:
- UV-resistant ASA material — 5+ year outdoor lifespan (vs. PLA's 6–12 months)
- Fully customizable plant names
- Embossed text (not printed label that fades)
- Taper design for easy soil insertion
- Readable from 1.5m distance
- Original design, manufactured on demand

**Photography requirements**:
- Outdoor garden bed with markers in soil, plant seedlings visible
- Close-up: embossed text clarity on marker face
- Lifestyle: full garden scene with multiple markers organized
- Detail: side view showing taper and soil depth marker
- Include size comparison (hand holding marker, or ruler)

### Launch Timeline
- **Material**: Order 4 colors ASA (1kg each, ~$90 total) — ships with standard orders
- **Profile setup**: 2–3 hours (test prints of tall tower, optimize enclosure temp)
- **Design**: 2 hours (CadQuery flag + stake, text module, M3 insert pocket)
- **Test prints**: 1 batch (20 stakes, magnet insertion test, outdoor UV stability check visual)
- **Photography**: 1.5 days (requires outdoor garden setting, natural lighting)
- **Listing creation**: 1 day
- **Ready for listing**: Day 14–18 post-test-print (waiting on ASA calibration + outdoor photography)

---

## Product 4: Pegboard Hook System

### Overview
- **Target price**: $4.99 per individual hook, $22 (10-set), $38 (20-set starter kit)
- **Margin**: 71% net on sets
- **Design complexity**: Medium (3 hook sizes, optional label variant, IKEA compatibility)
- **Print time per unit**: 3–5 min (20–25 hooks per plate depending on size)
- **Lead time for launch**: 14–21 days (design time, photography setup)

### CadQuery Design Specification

**Variables**:
```
hook_size: "small" (40mm), "medium" (65mm), "large" (90mm)
arm_thickness_mm: 8      # hook thickness
hook_tip_dia_mm: 14      # peg insertion diameter
label_text: optional     # embossed label on hook face (e.g., "DRILLS")
label_included: True/False
mount_standard: "IKEA_SKADIS" or "standard_pegboard"
```

**Geometry**:

1. **J-Hook (three sizes)**
   - Small: 40mm total length, Ø 14mm peg insertion diameter, 8mm arm thickness
   - Medium: 65mm total length, same insertion diameter
   - Large: 90mm total length, same insertion diameter
   - Tip radius: R=2mm (prevents peg splitting)
   - Peg insertion: snug fit, ~0.5mm clearance (pushes onto pegboard peg, doesn't rattle)

2. **Hook arm geometry** (optimized for no supports)
   - Printed vertically (hook tip pointing up, Z-axis)
   - Wall thickness: 4mm (adequate for 500g hanging load test)
   - Transition from peg to arm: smooth blend curve (avoids sharp stress concentration)
   - Grain-texture emboss on arm exterior (visual grip indication)

3. **Label variant** (optional)
   - Embossed text (3mm height) on peg-facing surface (e.g., "DRILLS", "SCREWDRIVERS")
   - Text centered, 1.5mm emboss depth
   - Available on all three sizes
   - Buyers can opt for labeled or unlabeled via Etsy variant

4. **IKEA SKADIS variant** (alternate mounting standard)
   - Alternative peg-insertion design for IKEA pegboard systems
   - Slightly different peg diameter (17.5mm vs. 14mm for standard pegboard)
   - Same hook arm geometry otherwise
   - Listed as separate variant ("Standard Pegboard" vs. "IKEA SKADIS")

**CadQuery snippet** (pseudocode):
```python
import cadquery as cq

def create_pegboard_hook(
    hook_size="medium",  # "small", "medium", "large"
    label_text=None,
    mount_standard="standard_pegboard"
):
    # Hook geometry varies by size
    sizes = {
        "small": {"length": 40, "arm_thick": 8},
        "medium": {"length": 65, "arm_thick": 8},
        "large": {"length": 90, "arm_thick": 8},
    }
    params = sizes[hook_size]
    
    # Peg diameter (pegboard standard = 14mm, IKEA = 17.5mm)
    peg_dia = 17.5 if mount_standard == "IKEA_SKADIS" else 14
    
    # J-hook main body
    peg = cq.Workplane("XY").cylinder(30, peg_dia/2) \
        .edges(">Z").fillet(2)  # rounded tip
    
    arm = peg.faces("+Z").workplane().moveTo(0, 0) \
        .spline([(0, 0), (params["length"]/2, 0), (params["length"], 0)]) \
        .sweep(cq.Workplane("XY").box(8, 8, 1))  # arm shape
    
    # Add grain texture (visual appearance)
    arm = add_texture_pattern(arm, pattern="grain", depth=0.5)
    
    # Label text (optional)
    if label_text:
        label = cq.Workplane("XY").text(
            label_text, fontsize=3, distance=1.5,
            font="optima"
        )
        final = arm.union(label)
    else:
        final = arm
    
    return final
```

### Manufacturing Parameters

**Bambu P1S profile**:
- **Material**: PLA+ (black, white, gray, or color options)
- **Temperature**: 220°C nozzle, 55°C bed
- **Speed**: standard (100 mm/s)
- **Layer height**: 0.2mm
- **Support**: none (hooks print vertically with no supports)
- **Print orientation**: hook tip pointing up (Z-axis), peg base on bed
- **Plate nesting**:
  - Small hooks: 25–30 per plate
  - Medium hooks: 20–25 per plate
  - Large hooks: 15–20 per plate
- **Print time per hook**: 3–5 min (size dependent)
- **Post-processing**:
  1. Remove from plate (10 min for mixed-size batch of 20)
  2. Inspect peg-insertion for debris or stringing (remove if present)
  3. Visual check: no layer lines visible on arm (critical for aesthetics)
  4. Optional: light sanding of arm (100-grit) for matte finish
  5. Wipe clean

**Quality gates**:
1. Peg insertion: should snap onto pegboard peg with slight resistance (no rattle, no forced insertion)
2. Load test: hang 5kg weight from hook arm for 1 min — should not sag or crack
3. Text clarity: label text should be crisp and readable (if labeled variant)

### Etsy Listing Skeleton

**Title**: "Pegboard Hooks | 3D Printed Organizer System | Bulk Starter Set [Size & Qty]"

**Price**: 
- Individual: $4.99 each
- 10-hook set: $22 (mixed sizes or single size)
- 20-hook starter set: $38 (assorted small/medium/large)

**Variants**: 
- 3 hook sizes × 2 mount standards × labeled/unlabeled (12 individual SKUs)
- 3 starter kits (10-set, 20-set, professional 30-set)

**Personalization fields**:
- "Preferred hook size mix (for starter sets): 33% small + 33% medium + 33% large (recommended) OR custom mix"
- "Mount standard: Standard Pegboard OR IKEA SKADIS"
- "Label hooks? Yes (e.g., DRILLS, BITS, CABLES) OR No (plain)"

**Key selling points**:
- Fully customizable hook sizes and mount standards
- Available in labeled and plain variants
- Professional embossed labels (text won't fade)
- Bulk discounts for 10-hook and 20-hook starter kits
- Works with standard pegboard and IKEA systems
- Original design, 3D-printed on demand
- Strong PLA+ construction — supports 5kg+ per hook

**Photography requirements**:
- Pegboard panel with variety of tools hung (drills, bits, screwdrivers, cables)
- Close-up: hook detail showing peg insertion and arm clarity
- Lifestyle: organized workshop wall with pegboard system fully loaded
- Detail: size comparison (small vs. medium vs. large hooks side-by-side)
- IKEA variant: mounted on IKEA SKADIS pegboard system
- Labeled variant: close-up of embossed text on hook face

### Launch Timeline
- **Design**: 3–4 days (CadQuery 3-size hooks + optional label module + IKEA variant)
- **Test prints**: 1–2 batches (sample of each size, load testing, peg fit verification)
- **Photography**: 2 days (requires tool props, pegboard panel, workshop or studio lighting)
- **Listing creation**: 1.5 days (multiple SKUs, bundle configurations)
- **Ready for listing**: Day 14–21 post-test-print

---

## Product 5: Monitor Riser Legs

### Overview
- **Target price**: $28–$38 per 4-leg set
- **Margin**: 68% net
- **Design complexity**: Medium (parametric height + shelf thickness + cable channel)
- **Print time per unit**: 40–55 min per set of 4 (limited by geometry, not plate efficiency)
- **Lead time for launch**: 21–28 days (design + material orders + load testing)
- **Special material**: Silicone bumper feet (AliExpress lead time 7–10 days)
- **Capacity note**: Monitor risers have the longest print time and should launch only after first 3 products are stable

### CadQuery Design Specification

**Variables**:
```
height_mm: 80, 120, 160   # riser height, user-selectable
shelf_thickness_mm: 18, 25  # shelf board thickness for sizing
cable_channel: True/False  # optional cutout for cable routing
num_legs: 4  # quantity per set (always 4)
foot_style: "rubber_feet", "felt_pads"  # bumper feet type
```

**Geometry**:

1. **Leg assembly** (4 identical legs per set)
   - Height: 80/120/160mm (user-selectable via Etsy personalization)
   - Leg footprint: 30 × 30mm base, tapering to 20 × 20mm at top
   - Wall thickness: 4mm throughout (adequate strength for ~10kg monitor load)
   - Foot pocket: Ø 10mm × 3mm deep (for silicone bumper insert)

2. **Shelf contact surface** (top of leg)
   - Flat mating surface, slightly domed (1mm curve) for pressure distribution
   - Sized for shelf_thickness_mm contact (parametric sizing for different shelf boards)
   - Anti-slip texture emboss (grid pattern, 1mm spacing) on contact surface

3. **Cable channel** (optional)
   - U-shaped slot: 15mm wide × 8mm deep, running along inside of leg group
   - Allows power cable + USB cables to route through riser without sharp bending
   - Channel opens at back (away from user view)
   - Only available on 120mm and 160mm heights (80mm too short for cable routing)

4. **Connection method** (leg-to-leg)
   - Four separate legs (no brackets or connectors required)
   - Optional: mounting plate (thin plastic plate, 40 × 40 × 3mm) that connects legs if user wants to treat riser as single unit
   - Mounting plate: adheres with thermal bonding or press-fits onto leg posts

**CadQuery snippet** (pseudocode):
```python
import cadquery as cq

def create_monitor_riser_leg(
    height=120, shelf_thickness=18, cable_channel=False
):
    # Leg body (30 × 30 base tapering to 20 × 20 top)
    base_foot = cq.Workplane("XY").box(30, 30, 10)
    leg_body = cq.Workplane("XY").box(20, 20, height) \
        .union(base_foot)  # base + leg
    
    # Taper from base to top
    leg_tapered = leg_body.faces("+Z").workplane() \
        .box(20, 20, height - 10)
    
    # Anti-slip texture on top surface
    contact_surface = leg_tapered.faces("+Z").workplane() \
        .rect(20, 20).offset2D(-1) \
        .sketch().grid(1).finalize().extrude(1)
    
    # Rubber foot pocket (Ø 10mm × 3mm)
    foot_pocket = contact_surface.faces("+Z").workplane() \
        .circle(5).cutBlind(-3)
    
    # Cable channel (optional, U-shaped)
    if cable_channel and height >= 120:
        channel = foot_pocket.faces("+Z").workplane() \
            .slot2D(15, height, 8).cutBlind(-8)
    else:
        channel = foot_pocket
    
    return channel
```

### Manufacturing Parameters

**Bambu P1S profile**:
- **Material**: PLA+ (black or white preferred for monitor aesthetic)
- **Temperature**: 220°C nozzle, 55°C bed
- **Speed**: standard (100 mm/s)
- **Layer height**: 0.2mm
- **Support**: minimal (tree supports on cable channel cutout only, if enabled)
- **Print orientation**: leg standing upright (Z-axis = height), flat orientation on bed
- **Plate nesting**: limited by height
  - 80mm legs: 9–12 per plate (3 × 3 or 4 × 3 grid)
  - 120mm legs: 4–6 per plate (2 × 2 grid, legs too tall for dense nesting)
  - 160mm legs: 2–4 per plate (2 × 1 grid)
- **Print time per leg**: 40–55 min (height dependent)
- **Print time per set of 4**: 160–220 min per plate run
- **Post-processing**:
  1. Remove legs from plate (10 min for 4 legs)
  2. Remove supports from cable channel (if enabled)
  3. Inspect contact surface texture for clarity (should have grid pattern visible)
  4. Clean foot pockets (remove any residue)
  5. Insert silicone bumper feet via press-fit or light heating (1 min)
  6. Wipe clean; allow to cool

**Load testing** (critical before listing):
- Place 4 legs under 30×30cm shelf board
- Load with 10kg weight center
- Monitor for deformation or cracking
- Verify foot pockets hold bumper feet under load

### Etsy Listing Skeleton

**Title**: "Monitor Riser Legs | 3D Printed Monitor Stand | Custom Height [Qty/Height]"

**Price**: 
- $28 (8cm height)
- $32 (12cm height)
- $38 (16cm height with cable channel)

**Variants**: 3 heights × 2 shelf thicknesses × 2 cable-channel options (12 SKUs)

**Personalization fields**:
- "Riser height: 8cm / 12cm / 16cm (measured from shelf board top to monitor bottom)"
- "Shelf board thickness: 18mm / 25mm (for proper leg sizing)"
- "Include cable channel? Yes (12cm and 16cm only) / No"

**Key selling points**:
- Fully parametric — matches your exact height and shelf board
- Includes 4 silicone bumper feet (non-slip, protect furniture)
- Optional cable routing channel (16cm option)
- Anti-slip texture on contact surface (prevents monitor sliding)
- Stackable design — add a second riser for extra height
- Original design, 3D-printed on demand

**Photography requirements**:
- Lifestyle: desk setup with monitor elevated on riser legs, showing cable routing underneath
- Detail: close-up of leg contact surface showing anti-slip texture
- Cable channel: photo showing power cable routed through channel (if applicable)
- Size comparison: riser in place with common objects (coffee cup, keyboard) for scale
- Load test: monitor resting stably on riser with no visible sag

### Launch Timeline
- **Material**: Order silicone bumper feet (100-pack, ~$5 from AliExpress) — lead time 7–10 days
- **Design**: 3–4 days (CadQuery parametric legs, cable channel, texture emboss, height variants)
- **Test prints**: 2 batches (one of each height variant, load testing with 10kg weight, contact surface texture verification)
- **Load testing**: 1–2 days (monitor placement, weight distribution validation)
- **Photography**: 1.5 days (desk setup photos, cable routing detail)
- **Listing creation**: 1 day
- **Ready for listing**: Day 21–28 post-test-print (latest of all products due to material lead time + extended design)

---

## Production Workflow Template

Once each product design is complete, follow this standardized workflow:

### Pre-Production
1. **CadQuery design review** — Check parametric variables, test with 2–3 configurations
2. **STL export** — Verify mesh integrity (no errors in Bambu Studio import)
3. **Bambu Studio nesting** — Optimize plate utilization, support strategy
4. **Print profile validation** — Test with 1 batch, measure dimensional accuracy
5. **Post-processing protocol** — Document steps for each product type

### Production
1. **Print batch** — Follow optimized plate layout, monitor for anomalies
2. **Post-processing** — Follow product-specific checklist (supports, inserts, finish)
3. **Quality inspection** — Visual check (layer lines, texture clarity), mechanical check (fits, holds, loads)
4. **Packaging** — Place in product box, include care card with outdoor/handling instructions
5. **Weigh and label** — USPS weight, Pirate Ship batch upload

### Etsy Integration
1. **Generate preview images** — 3D CAD render + lifestyle photo + detail shot
2. **List configuration** — Title, description, variants, personalization fields, price
3. **Set processing time** — Default "3–5 business days" (adjust for long-lead materials)
4. **Shipping policy** — First Class mail, weight-based (Pirate Ship integration)
5. **Monitor early sales** — First 5 orders: verify personalization accuracy, shipping feedback

---

## Cost Model Summary (refresh from product-line-strategy.md)

| Product | COGS | Sell Price | Net Margin |
|---|---|---|---|
| Headphone Hook | $3.82 | $16.00 | 76% |
| Magnetic Bin Labels (10-pack) | $6.08 | $22.00 | 72% |
| Garden Plant Markers (10-pack ASA) | $5.82 | $18.00 | 68% |
| Pegboard Hook Set (20 hooks) | $9.18 | $32.00 | 71% |
| Monitor Riser Legs (4-pack) | $10.33 | $32.00 | 68% |

**Combined with ModRun** (20 units/week baseline + expansion):
- Total monthly gross: $6,900–$7,500
- Total monthly net: $6,800–$7,500
- Printer utilization: 80–90% capacity at 5-product steady state
- Second printer trigger: 35–45 ModRun-equivalent units/week

---

## Contingency & Risk Mitigation

### ASA calibration failure
- **Risk**: ASA profile doesn't yield clean prints after multiple attempts
- **Mitigation**: Fall back to PETG (3-season outdoor, ~$0.025/g same cost)
- **Timeline**: Adds 1 week to plant marker launch

### Magnet supply delay
- **Risk**: AliExpress N52 magnets delayed >14 days
- **Mitigation**: Launch bin labels without magnets (blank tiles), allow buyer to add adhesive labels
- **Timeline**: Reduces launch delay to 7–10 days

### Pegboard hook loads test failure
- **Risk**: 5kg load causes cracking or permanent deformation
- **Mitigation**: Increase wall thickness to 5mm (adds ~2 min print time), retest
- **Timeline**: Adds 3–5 days to design cycle

### Monitor riser cable-channel interference
- **Risk**: Cable channel too narrow or inhibits leg strength
- **Mitigation**: Offer two variants (with/without channel), default to non-channel
- **Timeline**: No launch delay; channel becomes optional SKU

---

## Approval Checklist (Pre-Launch)

- [ ] Test print succeeds; design parametrization verified
- [ ] All CadQuery designs saved to `projects/mfg-farm/designs/` with git timestamps
- [ ] Etsy listings created in draft mode (ready to publish)
- [ ] Photography complete for all 5 products
- [ ] Quantity projections reviewed with mfg-farm cost model
- [ ] Supplier orders placed (magnets, ASA filament, rubber feet) with expected delivery dates
- [ ] Production workflow documented and tested with first batch
- [ ] Risk mitigation plan reviewed and contingency supplies ordered (fallback filaments, etc.)

---

## Next Steps

**Upon test-print success**:
1. Commit this document to git (record date, orchestrator session)
2. Execute designs in order: Headphone Hook (Day 1) → Magnetic Labels (Day 3) → Plant Markers (Day 7) → Pegboard Hooks (Day 14) → Monitor Riser Legs (Day 21)
3. Batch print and photograph each product immediately upon design completion
4. List on Etsy within 24 hours of batch completion
5. Log weekly sales and customer feedback for Phase 2 iteration

**Metrics to track**:
- Units sold per product per week
- Customer feedback (Etsy reviews, repeat purchase rate)
- Printer utilization (print hours per week)
- Margin validation vs. cost model estimates

