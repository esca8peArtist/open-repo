---
title: Expansion Products Manufacturing Specs & CadQuery Designs
project: mfg-farm
created: 2026-05-06
updated: 2026-05-06
status: ready-to-execute
confidence: high — grounded in product-line-strategy.md research, ModRun build123d codebase, and established cost model
related: product-line-strategy.md, production-workflow-v1.md, cost-model-spreadsheet.csv
cadquery_infrastructure: cadquery/modrun_clip_b123d.py, cadquery/modrun_rail_b123d.py
---

# Expansion Products Manufacturing Specifications

**Status**: Pre-test-print research and design staging. All CadQuery implementation guides are ready for immediate execution upon test-print success (May 6–15 window).

**Orchestrator instruction**: When test print passes, execute designs in this sequence — (1) Headphone Hook, (2) Magnetic Bin Labels, (3) Garden Plant Markers, (4) Pegboard Hook System, (5) Monitor Riser Legs. Each product's CadQuery file should be placed in `projects/mfg-farm/cadquery/` alongside the existing ModRun scripts.

---

## Design Philosophy and Infrastructure Reuse

All five products inherit the ModRun build123d pattern: constants block at the top, composable `make_*` functions, a `build_*` assembly function, and a `main()` with argparse for STL export. This means:

- The same `FDM_TOLERANCE` variable established from the ModRun test print applies directly to all five products
- STL export uses `export_stl()` from build123d, identical to the ModRun scripts
- The `--output-dir` convention writes into `stl/` with the same naming scheme
- Post-test-print, one confirmed `FDM_TOLERANCE` value (expected 0.10–0.20mm) gets applied globally across all product scripts via the `--tolerance` CLI flag

The ModRun infrastructure does not need modification. Each expansion product is a standalone script that imports only from build123d.

---

## Product 1: Desk Headphone Hook

### Overview

- **Target price**: $16.00 single, $45.99 bundle with ModRun starter set
- **Net margin**: 76% at 20 units/week
- **Print time per unit**: 45–55 min
- **Lead time to Etsy listing**: 7–10 days post-test-print
- **Material**: PLA+ (existing stock — zero new sourcing)
- **Launch priority**: First. Same buyer, same desk, same PLA+ spool, cross-sells directly into ModRun orders.

### CadQuery Implementation Guide

**Script location**: `cadquery/headphone_hook_b123d.py`

**Architecture pattern**: Three composable functions — `make_clamp_base()`, `make_hook_arm()`, `make_cable_wrap_post()` — assembled in `build_hook()` and exported via `main()`. Mirrors `modrun_clip_b123d.py` structure.

**Constants block**:

```python
from build123d import *
import argparse, os

# Parametric inputs — adjust desk_thickness per customer order
DESK_THICKNESS = 25.0       # mm — clamp jaw opening, default; range 10–40
ARM_LENGTH = 140.0          # mm — hook arm overhang
WRAP_POST = True            # bool — cable-wrap post enabled
MOUNT_STYLE = "under_desk"  # "under_desk" or "edge_clamp"
FDM_TOLERANCE = 0.15        # mm — import confirmed value from ModRun test print

# Clamp body
CLAMP_W = 50.0; CLAMP_D = 50.0; CLAMP_H = 30.0
JAW_CLEARANCE = 1.0         # mm above desk_thickness for easy installation

# Hook arm
ARM_DIAMETER = 20.0         # mm at root, tapers to 16mm at tip
ARM_TIP_DIAMETER = 16.0

# Cable wrap post
WRAP_POST_DIA = 8.0; WRAP_POST_HEIGHT = 30.0
GROOVE_COUNT = 5; GROOVE_WIDTH = 4.0; GROOVE_DEPTH = 2.0
```

**Key geometry notes**:

`make_clamp_base()` builds a 50×50×30mm box, then cuts a parametric slot through the body: `slot_height = DESK_THICKNESS + JAW_CLEARANCE`. The slot width is `CLAMP_W - 8mm` (leaving 4mm walls on each side). For the `edge_clamp` variant, a second subtraction creates the screw-clearance channel for an M4 bolt. For `under_desk`, two Ø6mm cylindrical cuts (10mm deep) provide wood screw dowel holes.

`make_hook_arm()` builds a swept ellipse along a spline from the clamp body's top face. Root cross-section is Ø20mm, tip tapers to Ø16mm over `ARM_LENGTH`. The spline arc uses a 15mm radius bend at the root-to-arm junction — this eliminates the stress concentration that causes straight-junction hooks to crack under sustained headphone weight. The taper is achieved by lofting two circles rather than sweeping a constant profile.

`make_cable_wrap_post()` is a Ø8mm cylinder (height `WRAP_POST_HEIGHT`) that is subtracted with five equally-spaced rectangular slots (`GROOVE_WIDTH × GROOVE_DEPTH`) to create cable-routing grooves. Slot angles are rotated 72° apart around the Z-axis.

**CLI interface**:

```
python headphone_hook_b123d.py --desk-thickness 25 --mount under_desk --output-dir ./stl/
python headphone_hook_b123d.py --desk-thickness 32 --mount edge_clamp --no-wrap-post --output-dir ./stl/
python headphone_hook_b123d.py --tolerance 0.12 --output-dir ./stl/
```

### Manufacturing Parameters

| Parameter | Value |
|---|---|
| Material | PLA+ (eSUN/Overture, existing stock) |
| Nozzle temp | 220°C |
| Bed temp | 55°C |
| Layer height | 0.2mm |
| Infill | 25% gyroid (matches ModRun clip profile) |
| Walls | 4 loops |
| Support | Tree supports under clamp jaw only, 12% density |
| Print orientation | Horizontal — hook arm parallel to plate, clamp base flat |
| Plate nesting | 4–6 hooks (Bambu Studio auto-arrange) |
| Print time per unit | 45–55 min |
| Post-processing | Support removal (5 min), 100-grit sanding on jaw face (2 min), M4 heat-set nut insert (1 min) |

**Quality gates**: (1) Clamp jaw grips 25mm test rod without slipping. (2) Hook arm shows no visible layer lines on the outer curved face — if visible, reduce outer wall speed to 150mm/s. (3) M4 screw inserts flush with no binding.

### COGS at Volume

| Units/Week | Filament (25g PLA+) | Hardware | Packaging | Etsy Fees | Total COGS | Net/Unit |
|---|---|---|---|---|---|---|
| 20 | $0.33 | — | $0.80 | $2.69 | $3.82 | $12.18 |
| 50 | $0.31 | — | $0.72 | $2.69 | $3.72 | $12.28 |
| 100 | $0.29 | — | $0.68 | $2.69 | $3.66 | $12.34 |

Bulk filament (10kg bundle at $11.50/kg) activates at Month 2+. Packaging compression at 100 units assumes poly mailer in bulk at $0.045 each.

### Etsy Listing Skeleton

**Title**: `Desk Headphone Hanger | 3D Printed Under-Desk Clamp Hook | Custom Desk Thickness | Cable Wrap Post | [Color]`

**Price**: $16.00 single | $45.99 bundle with ModRun cable management starter set

**Variants**: 5 colors (black, white, gray, blue, red) × 2 mount styles = 10 SKUs

**Personalization fields**:
- "Desk thickness in mm (10–40mm, measure with a ruler — default is 25mm)"
- "Mount style: Under-Desk Screws OR Edge-Clamp"
- "Include cable-wrap post? Yes / No"

**Description bullet points**: Parametric clamp matches your exact desk thickness — no loose fit. Integrated cable-wrap post prevents headset cable from dangling. Designed to complement ModRun cable management rail (link in shop). All-original CadQuery design. PLA+ construction holds 500g sustained load.

### Mockup Requirements

- Lifestyle: headphones hung on hook, ModRun rails visible in background, consistent desk setup
- Detail: close-up of cable-wrap post with USB-C cable routed through grooves
- Variant: edge-clamp version showing clamp jaw profile
- Bundle: hook + ModRun rail assembled together on desk edge

### Launch Sequence

Day 1–3: CadQuery design and 3 test print variants (10mm, 25mm, 40mm desk thickness). Day 4–5: photography on existing desk backdrop. Day 6–7: Etsy listing creation, bundle SKU configuration. **Target: listing live by Day 8 post-test-print.**

---

## Product 2: Magnetic Workshop Bin Labels

### Overview

- **Target price**: $22.00 (10-pack), $32.00 (20-pack)
- **Net margin**: 72% at 20 sets/week
- **Print time per tile**: 2–3 min (30 tiles per plate run)
- **Lead time to listing**: 10–14 days (7–14 day magnet delivery from AliExpress is the binding constraint)
- **Material**: PLA+ (existing stock) + N52 disc magnets (15×3mm, ~$0.08 each)
- **Action required on Day 0 post-test-print**: Order 200× N52 magnets immediately — this starts the clock.

### CadQuery Implementation Guide

**Script location**: `cadquery/magnetic_label_b123d.py`

**Architecture**: `make_tile_body()` + `make_magnet_pocket()` + `make_embossed_text()` → `build_label_tile()`. Text input is the only per-order variable; all geometry is otherwise constant. This script is the simplest of the five.

**Constants block**:

```python
from build123d import *
import argparse, os

TILE_W = 50.0; TILE_D = 25.0; TILE_H = 4.0
CORNER_RADIUS = 2.0         # mm — rounded corners for hand comfort
MAGNET_DIA = 15.0           # mm — N52 disc magnet diameter
MAGNET_DEPTH = 3.1          # mm — pocket depth (3mm magnet + 0.1mm press fit)
TEXT_HEIGHT = 3.5           # mm — embossed text font size
TEXT_DEPTH = 1.5            # mm — emboss extrusion depth
FDM_TOLERANCE = 0.15        # mm — apply confirmed ModRun value
```

**Key geometry notes**:

`make_tile_body()` uses `Box(TILE_W, TILE_D, TILE_H)` with `fillet()` applied to all vertical edges at `CORNER_RADIUS`. The top face gets a subtle 1mm dome by intersecting the box with a large-radius sphere — this can be skipped in v1 if it complicates the geometry; flat top also reads cleanly.

`make_magnet_pocket()` cuts a circular pocket from the underside: `Cylinder(MAGNET_DIA/2 + FDM_TOLERANCE, MAGNET_DEPTH)` subtracted from the `<Z` face. The `FDM_TOLERANCE` addition to the pocket radius is critical — without it the magnet will not press in, and with too much clearance it will fall out. At the confirmed `FDM_TOLERANCE` from the ModRun test print, the pocket should produce a snug press fit. If the magnet slips, reduce the tolerance addition by 0.05mm and retest.

`make_embossed_text()` uses build123d's `Text()` primitive: `text_solid = Text(txt=TEXT_CONTENT, font_size=TEXT_HEIGHT, align=(Align.CENTER, Align.CENTER))` extruded to `TEXT_DEPTH`. The text solid is unioned onto the tile's top face with `Pos(0, 0, TILE_H/2) * text_solid`. Font availability depends on the host system; "Arial" is a safe cross-platform fallback.

**CLI interface**:

```
python magnetic_label_b123d.py --text "DRILLS" --output-dir ./stl/
python magnetic_label_b123d.py --text-list "DRILLS,BITS,CABLES,WRENCHES" --output-dir ./stl/
python magnetic_label_b123d.py --batch-from-file customer_order.txt --output-dir ./stl/
```

The `--batch-from-file` flag reads one label text per line, generates one STL per tile, and names them sequentially. This is the customer-personalization automation path.

### Manufacturing Parameters

| Parameter | Value |
|---|---|
| Material | PLA+ black (contrast text clarity) |
| Nozzle temp | 220°C |
| Bed temp | 55°C |
| Layer height | 0.2mm |
| Infill | 15% grid (tiles are non-structural) |
| Support | None (flat tiles print without supports) |
| Print orientation | Tile flat on plate (Z = 4mm) |
| Plate nesting | 30 tiles per plate (6×5 grid) |
| Print time per plate | 60–90 min = 2–3 min effective per tile |
| Post-processing | Magnet press-fit insertion (preheat pocket to 60°C, press N52 disc, cool 5 min for 30 tiles) |

**Magnet insertion protocol**: Batch 30 tiles in a tray. Heat pocket side briefly with heat gun at 60°C (10 seconds per tile — just enough to soften the pocket walls). Press magnet with thumb — it should seat fully flush with the tile underside with a tactile stop. If using heat gun is fussy, a silicone mold press or bench vise with padded jaws at room temperature also works if the tolerance is set correctly.

**Quality gate**: Pull test — a 30-tile batch randomly sampled. Magnet must require >3 lbf to extract (a light pull by hand should not remove it). Failing tiles indicate the pocket is too wide; reduce FDM_TOLERANCE by 0.05mm and reprint a test tile before running the full batch.

### COGS at Volume

| Units/Week | Filament (60g) | Magnets (10×) | Packaging | Etsy Fees | Total COGS | Net/Unit |
|---|---|---|---|---|---|---|
| 20 sets | $0.78 | $0.80 | $0.80 | $3.70 | $6.08 | $15.92 |
| 50 sets | $0.72 | $0.70 | $0.68 | $3.70 | $5.80 | $16.20 |
| 100 sets | $0.68 | $0.60 | $0.60 | $3.70 | $5.58 | $16.42 |

Magnet bulk pricing: 500-pack from AliExpress drops per-unit cost from $0.08 to ~$0.06. Activate at 50 sets/week.

### Etsy Listing Skeleton

**Title**: `Magnetic Workshop Labels | Custom Text 3D Printed Bin Labels | Toolbox Organizer | 10 or 20 Pack`

**Price**: $22.00 (10-pack) | $32.00 (20-pack) | $18.00 (blank 10-pack, no magnets)

**Personalization fields**:
- "Enter category names, one per line (up to 10 for 10-pack, up to 20 for 20-pack). Example: DRILLS, BITS, CABLES, SCREWDRIVERS, PLIERS"
- "Include magnets? Yes (N52, strong hold) / No (blank tiles — add your own adhesive labels)"

**Description bullet points**: Custom buyer-specified text embossed into each tile (not a printed sticker — won't fade). Strong N52 magnets hold to any ferrous surface: toolboxes, filing cabinets, magnetic whiteboards, pegboards. Universal tile size (50×25mm) fits standard bin lip. Repositionable and reusable.

### Mockup Requirements

- Primary: tiles on a metal toolbox drawer, labeled categories clearly readable
- Detail: magnet underside showing flush-seated disc
- Lifestyle: organized workshop bench with 20-tile system fully deployed
- Scale reference: tiles next to a standard tape measure or ruler

### Launch Sequence

Day 0: Order N52 magnets (this is the critical path — do not defer). Day 1–2: CadQuery design and test tile print, magnet press-fit calibration. Day 3–4: batch of 30 tiles, magnet insertion test. Day 5–6: photography. Day 7: Etsy listing draft. **Target: listing live Day 10–12 (after magnets arrive).**

---

## Product 3: Garden Plant Markers

### Overview

- **Target price**: $16.00 (6-pack), $22.00 (10-pack), $34.00 (20-pack)
- **Net margin**: 68% at 15 sets/week
- **Print time per stake**: 5–6 min (20 stakes per plate)
- **Lead time to listing**: 14–18 days (ASA calibration + outdoor photography)
- **Material**: ASA filament — UV-resistant, 5+ year outdoor lifespan. Requires separate P1S print profile.
- **Strategic timing**: May 2026 listing captures spring tail; the real value is listing age for the February–May 2027 peak.

### CadQuery Implementation Guide

**Script location**: `cadquery/plant_marker_b123d.py`

**Architecture**: `make_flag()` + `make_stake()` + `make_mount_connector()` → `build_plant_marker()`. The flag and stake print as a single integrated piece — no assembly required. The mount connector is a slightly thickened transition zone between flag and stake, not a separate hardware joint.

**Constants block**:

```python
from build123d import *
import argparse, os

# Flag
FLAG_W = 30.0; FLAG_H = 25.0; FLAG_THICKNESS = 6.0
FLAG_CORNER_RADIUS = 3.0
TEXT_SIZE = 2.5; TEXT_DEPTH = 1.5

# Stake
STAKE_LENGTH = 150.0; STAKE_DIA_ROOT = 4.0; STAKE_DIA_TIP = 3.8
GROUND_DEPTH_TARGET = 80.0  # advisory — stake must penetrate this depth

# Transition
CONNECTOR_H = 12.0; CONNECTOR_W = 8.0; CONNECTOR_D = 8.0

FDM_TOLERANCE = 0.15        # mm — confirmed from ModRun test print
```

**Key geometry notes**:

`make_flag()` creates `Box(FLAG_W, FLAG_THICKNESS, FLAG_H)` (note: stake is vertical Z, so flag hangs in XZ plane). The top two corners are filleted at `FLAG_CORNER_RADIUS`. Embossed text uses the same `Text()` + `extrude()` pattern as the bin label script — the text lives on the flag's front face (`+Y` direction).

`make_stake()` is a tapered cylinder. Build123d's `Cone()` primitive takes two radii — `Cone(STAKE_DIA_ROOT/2, STAKE_DIA_TIP/2, STAKE_LENGTH)` — and produces the taper automatically. Print orientation is vertical (Z-axis = stake length), which means the stake prints in its insertion direction — optimal for layer adhesion and bending strength.

`make_mount_connector()` is the transition block: a box `(CONNECTOR_W, CONNECTOR_D, CONNECTOR_H)` that blends flag bottom edge to stake top. It is unioned with both and filleted at the junction. There are no screws or inserts — one-piece print.

**ASA profile note**: The `FDM_TOLERANCE` at 245°C for ASA may differ slightly from the PLA+ value. Print one test flag-only piece and measure the text depth. Adjust `TEXT_DEPTH` rather than tolerance if the emboss is reading too shallow or too deep; ASA's higher shrinkage can cause minor Z-axis dimensional differences on thin features.

**CLI interface**:

```
python plant_marker_b123d.py --plant "Tomato" --output-dir ./stl/
python plant_marker_b123d.py --plant-list "Tomato,Basil,Carrot,Lettuce,Pepper,Cucumber" --output-dir ./stl/
python plant_marker_b123d.py --batch-from-file garden_order.txt --stake-length 200 --output-dir ./stl/
```

`--stake-length` override supports longer stakes (200mm) for buyers with deeper raised beds.

### Manufacturing Parameters

| Parameter | Value |
|---|---|
| Material | ASA (Overture or eSUN ASA, 4 colors: terracotta, sage, white, black) |
| Nozzle temp | 245°C |
| Bed temp | 100°C |
| Enclosure | Must be closed — ASA warps in open-air printing |
| Layer height | 0.2mm |
| Infill | 20% gyroid |
| Support | Minimal tree supports under flag bottom edge only, 8% density |
| Print orientation | Stake vertical (Z-axis = 150mm height) |
| Plate nesting | 20 stakes per plate |
| Print time per plate | 90–120 min |
| Post-processing | Support removal, 100-grit sand on flag face if ASA shows layer texture |

**One-time ASA profile calibration**: Print a 5×5×50mm tower with 3 wall loops. Check for warping at base, stringing at top. If warping: increase bed temp by 5°C. If stringing: reduce nozzle temp by 2°C and increase retraction 0.3mm. Save final profile as `ASA_PlantMarkers` in Bambu Studio — do not modify the base PLA+ production profile.

### COGS at Volume

| Units/Week | Filament (80g ASA) | Packaging | Etsy Fees | Total COGS | Net/Unit |
|---|---|---|---|---|---|
| 15 sets (10-pack) | $2.00 | $0.80 | $3.02 | $5.82 | $16.18 |
| 30 sets | $1.86 | $0.72 | $3.02 | $5.60 | $16.40 |
| 60 sets | $1.75 | $0.65 | $3.02 | $5.42 | $16.58 |

ASA at $0.025/g bulk. No hardware BOM. Margin is lower than the PLA+ products due to ASA cost, but there is no meaningful competition at this price point with UV-resistance as the differentiator.

### Etsy Listing Skeleton

**Title**: `Garden Plant Markers | UV-Resistant 3D Printed Stakes | Custom Plant Names | 5+ Year Outdoor Life | Set of 6/10/20`

**Price**: $16.00 (6-pack), $22.00 (10-pack), $34.00 (20-pack)

**Variants**: 3 quantities × 4 colors = 12 SKUs

**Personalization fields**:
- "Enter plant names, one per line (up to 6/10/20 depending on pack). Example: Tomato, Basil, Carrot, Lettuce, Pepper, Cucumber"
- "Color: Terracotta / Sage Green / White / Black"

**Key selling points in description**: ASA filament with 5+ year UV resistance — PLA competitors fade and crack within one season. Custom embossed text (not a painted label). Easy soil insertion (tapered tip). Readable from 1.5m.

### Mockup Requirements

- Outdoor garden bed with markers in soil, seedlings visible in background (requires outdoor shoot — plan for a dry day)
- Close-up: embossed text clarity, ideally in natural sunlight
- Terracotta color on terracotta pot — color matching lifestyle shot
- Size reference: marker held in hand showing stake length

### Launch Sequence

Day 0: Order 4 ASA color spools (1kg each, ~$90). Day 2–4: ASA profile calibration on P1S. Day 5–6: CadQuery design and first batch of 20 stakes. Day 7–10: outdoor photography (weather dependent — build in a buffer day). Day 11–14: listing creation. **Target: listing live Day 14–18.**

---

## Product 4: Pegboard Hook System

### Overview

- **Target price**: $4.99 (individual), $22.00 (10-set), $38.00 (20-set starter kit)
- **Net margin**: 71% on sets
- **Print time**: 3–5 min per hook (size dependent)
- **Lead time to listing**: 14–21 days (3 sizes + IKEA variant design time + photography)
- **Material**: PLA+ (existing stock)
- **Differentiation**: Embossed category labels and branded 20-hook starter set at $38 compete in a different sub-niche than generic plain hooks at $4.99.

### CadQuery Implementation Guide

**Script location**: `cadquery/pegboard_hook_b123d.py`

**Architecture**: `make_peg_socket()` + `make_hook_arm()` + `make_label()` → `build_hook()`. Three hook sizes (small/medium/large) are parameterized via a sizes dictionary. Standard pegboard and IKEA SKADIS peg diameters are constants in the config block.

**Constants block**:

```python
from build123d import *
import argparse, os

HOOK_SIZES = {
    "small":  {"length": 40, "label_offset": 15},
    "medium": {"length": 65, "label_offset": 25},
    "large":  {"length": 90, "label_offset": 35},
}
ARM_THICKNESS = 8.0; ARM_WIDTH = 8.0
PEG_DIA_STANDARD = 14.0    # mm — standard 1/4" pegboard peg
PEG_DIA_IKEA = 17.5        # mm — IKEA SKADIS peg diameter (measured, not nominal)
PEG_INSERT_DEPTH = 25.0    # mm — depth of socket
PEG_WALL = 3.0             # mm — socket wall thickness
TEXT_SIZE = 3.0; TEXT_DEPTH = 1.5
FDM_TOLERANCE = 0.15       # mm — confirmed from ModRun test print
```

**Key geometry notes**:

`make_peg_socket()` is a hollow cylinder — `Cylinder(PEG_DIA/2 + PEG_WALL, PEG_INSERT_DEPTH)` minus `Cylinder(PEG_DIA/2 + FDM_TOLERANCE, PEG_INSERT_DEPTH)`. The `FDM_TOLERANCE` addition to the bore is critical for snug pegboard fit. Peg sockets print tip-up (open end facing down on plate, socket walls pointing up). No supports needed for a simple socket shape.

`make_hook_arm()` extends from the socket's top face as a rectangular bar `(ARM_WIDTH, ARM_THICKNESS, hook_length)` swept in the arm direction, then curves downward at the tip using `fillet()` on the tip edge at radius `ARM_THICKNESS/2`. The downward curve is a cosmetic hook-tip that prevents tools from sliding off.

`make_label()` embosses text on the inward-facing surface of the socket (the face pointing toward the pegboard when installed). This placement means the label is readable at a glance when looking directly at the pegboard. Same `Text()` pattern as the bin label script.

**Print orientation**: Hook tip pointing upward (Z-axis). The peg socket base sits flat on the build plate. This eliminates all supports — the socket walls build vertically and the hook arm extends laterally within bridging range. This is the primary efficiency advantage of the vertical orientation.

**CLI interface**:

```
python pegboard_hook_b123d.py --size medium --label "DRILLS" --standard standard --output-dir ./stl/
python pegboard_hook_b123d.py --size small --no-label --standard ikea --output-dir ./stl/
python pegboard_hook_b123d.py --all-sizes --standard both --output-dir ./stl/
```

### Manufacturing Parameters

| Parameter | Value |
|---|---|
| Material | PLA+ (black, white, gray) |
| Nozzle temp | 220°C |
| Bed temp | 55°C |
| Layer height | 0.2mm |
| Infill | 20% gyroid |
| Support | None (vertical orientation, self-supporting) |
| Print orientation | Socket base on plate, tip pointing up |
| Plate nesting | Small: 25–30/plate; Medium: 20–25/plate; Large: 15–20/plate |
| Print time per hook | 3 min (small), 4 min (medium), 5 min (large) |
| Post-processing | Inspect socket bore for stringing, remove if present; light sanding optional |

**Load test before listing**: One hook of each size installed on a pegboard scrap, loaded with 5kg hanging weight for 5 minutes. Acceptance: no visible deformation, no sliding on peg. If a size fails: increase `PEG_WALL` by 1mm and retest.

### COGS at Volume

| Units/Week | Filament (200g set) | Packaging | Etsy Fees | Total COGS | Net/Set |
|---|---|---|---|---|---|
| 15 sets (20-hook) | $2.60 | $1.20 | $5.38 | $9.18 | $28.82 |
| 30 sets | $2.42 | $1.05 | $5.38 | $8.85 | $29.15 |
| 60 sets | $2.28 | $0.90 | $5.38 | $8.56 | $29.44 |

Packaging cost for 20-hook starter set uses a small flat cardboard box ($0.70) rather than poly mailer.

### Etsy Listing Skeleton

**Title**: `Pegboard Hook System | 3D Printed Organizer Hooks | Labeled Starter Set | Standard & IKEA SKADIS Compatible`

**Price**: $4.99 individual | $22.00 (10-set) | $38.00 (20-set starter kit)

**Variants**: 3 sizes × 2 mount standards × labeled/unlabeled = 12 individual SKUs; 3 starter kit bundles

**Personalization fields**:
- "For starter sets — hook size mix: Assorted (33% each), All Small, All Medium, All Large, or Custom mix"
- "Mount standard: Standard Pegboard (1/4\" holes) or IKEA SKADIS"
- "Label text for labeled hooks (one label per size category, or custom): DRILLS / BITS / CABLES / WRENCHES / SCREWDRIVERS"

**Key selling points**: Original label-hook design — text embossed on hook body (not a sticker). Works with both standard pegboard and IKEA SKADIS. Bulk sets save 30% vs. individual hooks. PLA+ construction supports 5kg+ per hook.

### Mockup Requirements

- Pegboard panel fully loaded with labeled hooks and real tools — this listing will not convert without a fully-populated pegboard photo
- Close-up: "DRILLS" label text on hook face
- Size comparison: small/medium/large hooks side by side
- IKEA SKADIS installed on SKADIS board

### Launch Sequence

Day 1–4: CadQuery 3-size hooks + IKEA variant. Day 5–7: test prints of all 6 variants, load testing. Day 8–10: photography (requires tool props and pegboard panel setup). Day 11–14: Etsy listing with all SKUs and bundle configurations. **Target: listing live Day 14–21.**

---

## Product 5: Monitor Riser Legs

### Overview

- **Target price**: $28.00 (8cm), $32.00 (12cm), $38.00 (16cm with cable channel)
- **Net margin**: 68% at 10 sets/week
- **Print time per set of 4**: 160–220 min (height-dependent; this is the binding constraint)
- **Lead time to listing**: 21–28 days (silicone feet delivery + load testing + extended design time)
- **Material**: PLA+ (existing stock) + silicone bumper feet (Ø10mm, AliExpress, ~$0.05 each)
- **Capacity note**: At 10 sets/week (40 legs), this is ~50 print hours/week on the single P1S. Launch only after the first three products are stable. Price sets processing time at "5–7 business days."

### CadQuery Implementation Guide

**Script location**: `cadquery/monitor_riser_b123d.py`

**Architecture**: `make_leg_body()` + `make_foot_pocket()` + `make_cable_channel()` → `build_riser_leg()`. All four legs in a set are identical — one STL exported, sliced 4× in Bambu Studio. This avoids managing four separate STL variants per height.

**Constants block**:

```python
from build123d import *
import argparse, os

# Leg geometry (parametric by height)
LEG_BASE_W = 30.0; LEG_BASE_D = 30.0
LEG_TOP_W = 20.0; LEG_TOP_D = 20.0
LEG_WALL = 4.0              # mm — wall thickness (hollow legs to reduce print time)
FOOT_POCKET_DIA = 10.0; FOOT_POCKET_DEPTH = 3.0    # silicone bumper insert
CONTACT_GRID_SPACING = 3.0  # mm — anti-slip grid on top surface

# Cable channel
CHANNEL_W = 15.0; CHANNEL_DEPTH = 8.0  # U-slot on inside face of leg

FDM_TOLERANCE = 0.15        # mm — confirmed from ModRun test print

HEIGHT_PRESETS = {
    "80mm":  {"height": 80,  "cable_channel": False},
    "120mm": {"height": 120, "cable_channel": True},
    "160mm": {"height": 160, "cable_channel": True},
}
```

**Key geometry notes**:

`make_leg_body()` builds a hollow tapered column. Outer profile: `Box(LEG_BASE_W, LEG_BASE_D, height)` with the top face shelled inward by `LEG_WALL` using build123d's `Shell()` operation. The taper from 30×30mm base to 20×20mm top is achieved by lofting two rectangles. Hollow construction saves ~40% filament vs. solid at 20% infill, and the wall thickness of 4mm is adequate for 10kg sustained monitor load based on PLA+ tensile yield.

`make_foot_pocket()` cuts a `Cylinder(FOOT_POCKET_DIA/2 + FDM_TOLERANCE, FOOT_POCKET_DEPTH)` from the base underside. The silicone bumper feet (Ø10mm disc) press into this pocket and protrude ~2mm below the base for non-slip contact.

`make_cable_channel()` cuts a `Box(CHANNEL_W, LEG_BASE_D, height)` slot from the inside face of the leg — the face that faces toward the center of the riser group. This creates a U-channel that runs the full height. Only enabled for 120mm and 160mm heights; the 80mm height is too short to benefit from cable routing.

Anti-slip grid on top contact surface: a `RectangularArray()` of small `Box(1, 1, 1)` bumps spaced at `CONTACT_GRID_SPACING` across the top face, then unioned to the leg top. This creates the textured non-slip surface.

**CLI interface**:

```
python monitor_riser_b123d.py --height 120 --output-dir ./stl/
python monitor_riser_b123d.py --height 160 --cable-channel --output-dir ./stl/
python monitor_riser_b123d.py --all-heights --output-dir ./stl/
python monitor_riser_b123d.py --height 120 --no-cable-channel --output-dir ./stl/
```

### Manufacturing Parameters

| Parameter | Value |
|---|---|
| Material | PLA+ (black or white — desk aesthetic) |
| Nozzle temp | 220°C |
| Bed temp | 55°C |
| Layer height | 0.2mm |
| Infill | 20% gyroid |
| Walls | 4 loops |
| Support | Minimal tree support on cable channel opening only (if enabled) |
| Print orientation | Leg standing upright (Z = height), base flat on plate |
| Plate nesting | 80mm: 9/plate; 120mm: 4/plate; 160mm: 2/plate |
| Print time per leg | 40 min (80mm), 55 min (120mm), 75 min (160mm) |
| Post-processing | Insert silicone bumper feet (press-fit, 30 sec per leg), wipe clean |

**Load test protocol before listing**: Four 120mm legs under a 30×30cm board, loaded with 10kg centered for 5 minutes. Acceptance: no audible cracking, no visible base deformation, foot pockets retain bumpers under load. If any leg shows base spread: increase `LEG_WALL` to 5mm and retest.

### COGS at Volume

| Units/Week | Filament (250g) | Rubber Feet | Packaging | Etsy Fees | Total COGS | Net/Set |
|---|---|---|---|---|---|---|
| 10 sets | $3.25 | $0.20 | $1.50 | $5.38 | $10.33 | $21.67 |
| 20 sets | $3.02 | $0.18 | $1.30 | $5.38 | $9.88 | $22.12 |
| 40 sets | $2.84 | $0.15 | $1.10 | $5.38 | $9.47 | $22.53 |

At 10 sets/week this is the lowest-volume product but highest dollar net per order. Packaging is a small flat box ($1.00) to hold 4 legs without rattling.

### Etsy Listing Skeleton

**Title**: `Monitor Riser Legs | 3D Printed Monitor Stand | Custom Height 8/12/16cm | Cable Channel Option | Set of 4`

**Price**: $28.00 (8cm), $32.00 (12cm), $38.00 (16cm with cable channel)

**Variants**: 3 heights × 2 cable-channel options = 6 SKUs (80mm has no cable channel option)

**Personalization fields**:
- "Riser height: 8cm / 12cm / 16cm (measure from desk surface to where you want monitor bottom)"
- "Include cable channel? Yes (routes power + USB cables through leg) / No — only available on 12cm and 16cm"

**Key selling points**: Fully parametric — built to your exact height. Includes 4 silicone non-slip bumper feet. Anti-slip grid on contact surface prevents monitor shelf from shifting. Optional cable channel routes cords cleanly. Bundles with ModRun cable management rail for the complete desk setup. Original design, not adapted from any existing file.

### Mockup Requirements

- Lifestyle: elevated monitor on riser, keyboard and ModRun rails visible — sell the complete desk ecosystem
- Detail: silicone feet and anti-slip grid texture close-up
- Cable channel: power cable routed through leg interior showing clean cable path
- Size comparison: 8cm vs. 12cm vs. 16cm legs side by side

### Launch Sequence

Day 0: Order silicone bumper feet (100-pack, ~$5 from AliExpress). Day 1–4: CadQuery design, all three heights. Day 5–8: test prints (one set per height), load testing. Day 9–12: photography on desk setup. Day 13–21: listing creation with all SKU configurations. **Target: listing live Day 21–28.**

---

## Cost Model Summary

| Product | COGS (20/wk) | COGS (50/wk) | COGS (100/wk) | Sell Price | Net Margin |
|---|---|---|---|---|---|
| Headphone Hook | $3.82 | $3.72 | $3.66 | $16.00 | 76% |
| Magnetic Bin Labels (10-pack) | $6.08 | $5.80 | $5.58 | $22.00 | 72% |
| Plant Markers (10-pack ASA) | $5.82 | $5.60 | $5.42 | $22.00 | 74% |
| Pegboard Hook Set (20-hook) | $9.18 | $8.85 | $8.56 | $38.00 | 76% |
| Monitor Riser Legs (4-pack) | $10.33 | $9.88 | $9.47 | $32.00 | 68% |

**Combined with ModRun at steady state (Month 6)**:

| Product | Units/Week | Weekly Gross | Weekly Net |
|---|---|---|---|
| ModRun (baseline) | 20 | $500 | $364 |
| Headphone Hook | 20 | $320 | $244 |
| Magnetic Bin Labels | 20 sets | $440 | $317 |
| Plant Markers | 15 sets | $330 | $224 |
| Pegboard Hook Sets | 15 sets | $570 | $406 |
| Monitor Riser Legs | 10 sets | $320 | $218 |
| **Total** | | **~$2,480/week** | **~$1,773/week** |

Monthly gross at steady state: approximately $9,900–$10,700. This is a 4× increase over ModRun-only economics. Second printer trigger activates at sustained 35–45 total ModRun-equivalent units/week — expected by Month 4–5.

---

## Launch Sequence and Prioritization Rationale

| Rank | Product | Days Post-Test-Print | Reason |
|---|---|---|---|
| 1 | Headphone Hook | Day 7–10 | Zero new materials, cross-sells ModRun directly, highest margin |
| 2 | Magnetic Bin Labels | Day 10–14 | Fastest print throughput (2 min/tile), only delay is magnet delivery — order Day 0 |
| 3 | Plant Markers | Day 14–18 | Spring 2026 window closing; listing age matters for 2027 season |
| 4 | Pegboard Hook System | Day 14–21 | More design time (3 sizes + IKEA variant), requires pegboard photography setup |
| 5 | Monitor Riser Legs | Day 21–28 | Longest print time per unit, requires silicone feet delivery and load testing |

Products 3 and 4 overlap in their window. If the ASA calibration is fast (one afternoon), plant markers list before pegboard hooks. If ASA gives calibration trouble, swap the order — pegboard hooks use existing PLA+ and can list faster.

---

## Contingency and Risk Notes

**ASA warping**: If three calibration attempts fail to eliminate base warping, switch to PETG (3-season outdoor life, same $0.013/g cost, no enclosure requirement). This halves the material cost difference and simplifies production. The UV-resistance claim weakens slightly but PETG outperforms PLA+ substantially for outdoor use.

**Magnet supply delay**: If AliExpress N52 delivery exceeds 14 days, launch bin labels in the "blank tile" variant immediately (no magnets, buyer adds their own adhesive). Update Etsy listing to show magnet version "coming soon." This preserves momentum without breaking lead time.

**Pegboard hook competition**: A plain J-hook listing at $4.99 will not differentiate. The embossed-label starter set at $38 is the real listing. If early traffic shows poor conversion on the starter set, the diagnostic is photography (needs a fully-loaded pegboard with real tools) before changing price.

**Monitor riser capacity ceiling**: At 10 sets/week (40 legs), the single P1S runs approximately 35–40 print hours per week on risers alone when combined with the other products. If riser demand exceeds 10 sets/week before a second printer is acquired, increase the Etsy processing time to 7–10 business days rather than taking backorders that cause review risk.

---

## Approval Checklist

- [ ] Test print succeeds; ModRun FDM_TOLERANCE value confirmed
- [ ] N52 magnets ordered (Day 0 action)
- [ ] ASA filament (4 colors) ordered (Day 0 action)
- [ ] Silicone bumper feet ordered (Day 0 action)
- [ ] All five CadQuery scripts saved to `projects/mfg-farm/cadquery/` with git timestamps
- [ ] Etsy listings created in draft mode before photography (copy-first workflow)
- [ ] Photography complete for all 5 products (outdoor shoot for plant markers requires planning)
- [ ] Load testing complete for pegboard hooks and monitor riser legs
- [ ] Production workflow tested with first batch of each product

---

*Confidence: High on geometry specifications and cost model (grounded in ModRun build123d codebase and established $0.013/g PLA+ cost basis). Medium on exact ASA print profile parameters — confirmed after calibration run. Medium on magnet press-fit tolerance — requires one test tile before full batch. All CadQuery implementation details follow the build123d API as used in `modrun_clip_b123d.py` and `modrun_rail_b123d.py`.*
