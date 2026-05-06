"""
SKU Batch 2 — Magnetic Workshop Bin Labels (build123d)

Generates press-fit magnetic label tiles for workshop/tool storage bins.
N52 disc magnets (Ø8mm × 2.2mm) press-fit into rear pocket — no adhesive required.
Embossed text on face for visibility at distance on vertical steel surfaces.

Usage:
    python sku_batch_2_magnetic_labels.py --output-dir ./stl/
    python sku_batch_2_magnetic_labels.py --label BOLTS --output-dir ./stl/
    python sku_batch_2_magnetic_labels.py --all --output-dir ./stl/
    python sku_batch_2_magnetic_labels.py --magnet-diameter 8.05 --output-dir ./stl/

Print settings (PLA+):
    Layer height:  0.20mm
    Infill:        25%
    Walls:         3
    Hotend:        220–225°C
    Bed:           60°C
    Supports:      None
    Print time:    8–12 min per tile

Cost:
    Filament:    ~$0.15 per tile (PLA+ @ $0.013/g, ~11g per tile)
    Hardware:    ~$0.02 per tile (N52 Ø8×2mm magnet, 20-pack $0.40 AliExpress)
    COGS total:  ~$0.17 per tile
    Retail:      $1.50–2.00 per tile; 20-pack at $28–32 (72–76% net margin)
"""

import argparse
import os

from build123d import *

# ============================================================
# Geometry constants — adjust after first test print
# ============================================================

TILE_WIDTH = 50.0        # mm — label tile width (X)
TILE_HEIGHT = 40.0       # mm — label tile height (Y)
TILE_THICKNESS = 3.0     # mm — tile thickness (Z)

CORNER_RADIUS = 2.0      # mm — rounded corners (cosmetic + safe handling)

# Magnet pocket — CRITICAL TOLERANCE
# Target: Ø8.0mm pocket for Ø8.0mm N52 disc magnet
# 0.0mm interference = press-fit (magnet held by friction, no adhesive)
# Tolerance sensitivity: ±0.05mm changes fit from snug to loose/stuck
# If magnet falls out under vibration: decrease MAGNET_DIAMETER by 0.05mm
# If magnet requires tool pressure (risks cracking tile): increase by 0.05mm
MAGNET_DIAMETER = 8.0    # mm — N52 disc magnet pocket diameter (adjust ±0.05mm)
MAGNET_DEPTH = 2.2       # mm — N52 disc magnet thickness (2.0mm + 0.2mm clearance)
MAGNET_OFFSET_X = 0.0    # mm — pocket X offset from tile center (keep centered)
MAGNET_OFFSET_Y = 0.0    # mm — pocket Y offset from tile center (keep centered)

# Material remaining below magnet pocket (structural check)
# TILE_THICKNESS - MAGNET_DEPTH = 0.8mm minimum. Do not reduce MAGNET_DEPTH above 2.5mm
# without increasing TILE_THICKNESS to maintain this margin.
_MAGNET_WALL_BELOW = TILE_THICKNESS - MAGNET_DEPTH   # = 0.8mm at defaults

# Text emboss
TEXT_DEPTH = 0.4         # mm — emboss extrusion above tile face
                         # 0.3–0.5mm prints cleanly at 0.20mm layer height
                         # Increase to 0.5mm if text reads as flat under raking light
TEXT_FONT_SIZE = 8.0     # pt — font size for embossed label text
                         # Reduce to 7pt if long labels (WASHERS) don't fit width

# Label variants — text printed on face
LABEL_VARIANTS = [
    "BOLTS",
    "BITS",
    "TOOLS",
    "SCREWS",
    "NAILS",
    "WASHERS",
]


def make_label_tile(label_text: str = "LABEL") -> Solid:
    """
    Build a single magnetic label tile with embossed text and magnet pocket.

    Geometry:
      - Base tile with rounded vertical corners
      - Embossed text centered on +Z face (buyer-facing)
      - Circular magnet pocket centered on -Z face (magnet side)

    The tile is built with Z=0 at the bottom face, Z=TILE_THICKNESS at top face.
    Print orientation: flat on build plate (+Z face down, text printing last = cleanest surface).
    """
    # --- Base tile ---
    tile = Box(TILE_WIDTH, TILE_HEIGHT, TILE_THICKNESS)

    # Round the four vertical edges (Z-axis edges) for safe handling
    try:
        tile = fillet(
            tile.edges().filter_by(Axis.Z),
            radius=CORNER_RADIUS,
        )
    except Exception:
        pass  # cosmetic — skip if edge filter fails on unusual geometry

    # --- Embossed text (top face, +Z direction) ---
    # Text is a raised solid, unioned onto the tile top face
    try:
        text_solid = Text(
            label_text,
            font_size=TEXT_FONT_SIZE,
            align=(Align.CENTER, Align.CENTER),
        )
        # Extrude text upward from zero plane, then translate to top of tile
        text_extrude = extrude(text_solid, amount=TEXT_DEPTH)
        # Position: centered XY, sitting on top of tile (+Z face)
        text_extrude = Pos(
            MAGNET_OFFSET_X,
            MAGNET_OFFSET_Y,
            TILE_THICKNESS / 2,  # move to top face (tile is centered on Z=0)
        ) * text_extrude
        tile = tile + text_extrude
    except Exception as e:
        print(f"  WARNING: Text emboss failed ({e}). Exporting tile without text.")

    # --- Magnet pocket (bottom face, -Z direction) ---
    # Pocket opens downward from -Z face (magnet pressed in from below after printing)
    pocket = Cylinder(
        radius=MAGNET_DIAMETER / 2,
        height=MAGNET_DEPTH,
    )
    # Position pocket: centered XY, pocket base at tile bottom (-Z face)
    pocket = Pos(
        MAGNET_OFFSET_X,
        MAGNET_OFFSET_Y,
        -(TILE_THICKNESS / 2) + MAGNET_DEPTH / 2,  # flush with bottom face
    ) * pocket
    tile = tile - pocket

    return tile


def export_label(label_text: str, output_path: str) -> None:
    print(f"Building label: '{label_text}' → {output_path}")
    tile = make_label_tile(label_text)
    export_stl(tile, output_path)
    print(f"  Exported: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate magnetic bin label STL files (SKU Batch 2)"
    )
    parser.add_argument(
        "--label",
        type=str,
        default=None,
        help="Single label text to export (e.g. BOLTS). Default: exports all variants.",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Export all label variants (BOLTS, BITS, TOOLS, SCREWS, NAILS, WASHERS)",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="./stl",
        help="Output directory for STL files (default: ./stl)",
    )
    parser.add_argument(
        "--magnet-diameter",
        type=float,
        default=None,
        help=f"Override magnet pocket diameter in mm (default {MAGNET_DIAMETER}). "
             f"Increase 0.05mm if magnet won't insert; decrease 0.05mm if it falls out.",
    )
    parser.add_argument(
        "--text-depth",
        type=float,
        default=None,
        help=f"Override text emboss depth in mm (default {TEXT_DEPTH}). "
             f"Increase to 0.5mm if text is hard to read.",
    )
    parser.add_argument(
        "--width",
        type=float,
        default=None,
        help=f"Override tile width in mm (default {TILE_WIDTH})",
    )
    parser.add_argument(
        "--height",
        type=float,
        default=None,
        help=f"Override tile height in mm (default {TILE_HEIGHT})",
    )
    parser.add_argument(
        "--thickness",
        type=float,
        default=None,
        help=f"Override tile thickness in mm (default {TILE_THICKNESS}). "
             f"Min recommended: {MAGNET_DEPTH + 0.8:.1f}mm (magnet depth + 0.8mm wall).",
    )
    args = parser.parse_args()

    # Apply parameter overrides
    import sku_batch_2_magnetic_labels as _self
    if args.magnet_diameter is not None:
        _self.MAGNET_DIAMETER = args.magnet_diameter
        print(f"Using custom magnet diameter: {args.magnet_diameter}mm")
    if args.text_depth is not None:
        _self.TEXT_DEPTH = args.text_depth
        print(f"Using custom text depth: {args.text_depth}mm")
    if args.width is not None:
        _self.TILE_WIDTH = args.width
    if args.height is not None:
        _self.TILE_HEIGHT = args.height
    if args.thickness is not None:
        _self.TILE_THICKNESS = args.thickness

    os.makedirs(args.output_dir, exist_ok=True)

    # Determine which labels to export
    if args.all or args.label is None:
        labels = LABEL_VARIANTS
    else:
        labels = [args.label.upper()]

    for label in labels:
        safe_name = label.lower().replace(" ", "_")
        output_path = os.path.join(args.output_dir, f"magnetic_label_{safe_name}.stl")
        export_label(label, output_path)

    print(f"\nDone. {len(labels)} label(s) exported to {args.output_dir}/")
    print(f"\nTuning notes (adjust constants at top of file, or pass as CLI args):")
    print(f"  Magnet won't insert:    increase --magnet-diameter (now {MAGNET_DIAMETER}mm)")
    print(f"  Magnet falls out:       decrease --magnet-diameter (now {MAGNET_DIAMETER}mm)")
    print(f"  Text hard to read:      increase --text-depth (now {TEXT_DEPTH}mm)")
    print(f"  Text overhangs edge:    reduce TEXT_FONT_SIZE (now {TEXT_FONT_SIZE}pt)")
    print(f"  Tile snaps under force: increase --thickness (now {TILE_THICKNESS}mm)")
    print(f"\nMagnet wall remaining: {TILE_THICKNESS - MAGNET_DEPTH:.2f}mm "
          f"(min recommended 0.8mm)")
    print(f"\nPrint orientation: flat on plate, text face UP (cleaner top surface).")
    print(f"Press magnet in after cooling — pocket should grip without adhesive.")


if __name__ == "__main__":
    main()
