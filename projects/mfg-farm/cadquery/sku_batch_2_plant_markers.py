"""
SKU Batch 2 — UV-Resistant Garden Plant Markers (build123d)

Generates parametric garden stake markers printed in ASA filament.
ASA (Acrylonitrile Styrene Acrylate) provides 5+ year UV resistance vs. PLA's 6–12 months.
Vertical body with embossed plant name; square-section stake for soil penetration.

Usage:
    python sku_batch_2_plant_markers.py --output-dir ./stl/
    python sku_batch_2_plant_markers.py --plant TOMATO --output-dir ./stl/
    python sku_batch_2_plant_markers.py --all --output-dir ./stl/
    python sku_batch_2_plant_markers.py --stake-width 8.3 --output-dir ./stl/

CRITICAL — ASA print settings (NOT PLA settings):
    Layer height:  0.20mm
    Infill:        25%
    Walls:         3
    Hotend:        240–250°C  (vs. PLA's 220–225°C — do NOT skip this)
    Bed:           100–110°C  (vs. PLA's 60°C — ASA warps severely at 60°C)
    Enclosure:     CLOSED     (Bambu P1S: close all doors and top panel)
    Fan:           Off or 15% max for first 5 layers, then 20–30%
    Supports:      None (orient stake-down on plate)
    Print time:    20–25 min per marker

Cost:
    Filament:    ~$0.22 per marker (ASA @ $0.016/g, ~14g per marker)
    Hardware:    None
    COGS total:  ~$0.22 per marker
    Retail:      $2.50–3.00 per marker; 10-pack at $22–26 (68–72% net margin)
"""

import argparse
import os

from build123d import *

# ============================================================
# Geometry constants — adjust after first test print
# ============================================================

# Body (above-ground portion — buyer-facing)
BODY_WIDTH = 18.0        # mm — marker body width (X)
BODY_TOTAL_HEIGHT = 80.0 # mm — total height of body segment (Y, above ground)
BODY_THICKNESS = 3.0     # mm — marker thickness (Z)
BODY_CORNER_RADIUS = 1.5 # mm — rounded body corners

# Ground stake (below-ground, hidden in soil)
# Square cross-section provides rigidity without the stake spinning.
# CRITICAL TOLERANCE: STAKE_WIDTH affects soil insertion force.
# Too wide (8.5+mm): stake splits under tool pressure in hard soil.
# Too narrow (7.5mm): stake bends under lateral load (heavy tomatoes in wind).
# Tune after first soil insertion test — adjust ±0.3mm.
STAKE_WIDTH = 8.0        # mm — square stake cross-section width (adjust ±0.3mm)
STAKE_DEPTH = 40.0       # mm — stake depth into soil (below body base)
STAKE_TAPER = 2.0        # mm — each side tapers from STAKE_WIDTH to tip over STAKE_DEPTH

# Text area — embossed on upper body
TEXT_FONT_SIZE = 6.0     # pt — plant name font size
TEXT_DEPTH = 0.4         # mm — emboss extrusion above body face
                         # Increase to 0.5mm if text washes out in photography
TEXT_Y_OFFSET = 15.0     # mm above body center (upper third of body)

# Full marker total height (body + stake)
# Used for positioning — stake starts at body base, extends downward
FULL_HEIGHT = BODY_TOTAL_HEIGHT + STAKE_DEPTH

# Plant name variants
PLANT_VARIANTS = [
    "TOMATO",
    "BASIL",
    "SAGE",
    "HERB",
    "CARROT",
    "FLOWER",
    "PEPPER",
    "MINT",
]


def make_body() -> Solid:
    """
    Main above-ground marker body — vertical rectangle with rounded corners.
    Origin at body center (midpoint of BODY_TOTAL_HEIGHT, mid-Z of BODY_THICKNESS).
    """
    body = Box(BODY_WIDTH, BODY_TOTAL_HEIGHT, BODY_THICKNESS)

    try:
        body = fillet(
            body.edges().filter_by(Axis.Z),
            radius=BODY_CORNER_RADIUS,
        )
    except Exception:
        pass  # cosmetic

    return body


def make_stake() -> Solid:
    """
    Below-ground square stake with tapered tip for soil penetration.

    Cross-section: STAKE_WIDTH × STAKE_WIDTH at the top (body junction),
    tapering to (STAKE_WIDTH - 2×STAKE_TAPER) at the tip.
    The taper provides a piercing point in hard soil without weakening the mid-shaft.

    Print orientation note: stake prints horizontally (length along Y).
    Layer lines run perpendicular to bending load — optimal orientation.
    """
    # Build stake as a loft from full-width profile at top to tapered profile at tip
    # Tip width = STAKE_WIDTH - 2*STAKE_TAPER on each side
    tip_width = max(STAKE_WIDTH - 2 * STAKE_TAPER, 2.0)  # floor at 2mm to prevent knife edge

    with BuildPart() as stake_part:
        with Locations(Pos(0, 0, 0)):  # top of stake (body junction)
            # Simple extrude + chamfer approach — more print-reliable than loft
            stake_box = Box(STAKE_WIDTH, STAKE_DEPTH, BODY_THICKNESS)

        # Taper the tip: chamfer the bottom Y face corners
        try:
            bottom_edges = stake_box.edges().filter_by_position(
                Axis.Y,
                -STAKE_DEPTH / 2 - 0.1,
                -STAKE_DEPTH / 2 + 0.1,
            )
            stake_box = chamfer(bottom_edges, length=STAKE_TAPER)
        except Exception:
            pass  # cosmetic — rectangular stake still functions fine

    return stake_part.part


def make_plant_marker(plant_name: str = "PLANT") -> Solid:
    """
    Assemble body + stake + embossed text into a complete plant marker.

    Layout (Y-axis):
      +Y tip of body at BODY_TOTAL_HEIGHT/2 above origin
      Center of body at Y=0 (origin)
      -Y base of body at -BODY_TOTAL_HEIGHT/2
      Stake runs from -BODY_TOTAL_HEIGHT/2 down to -(BODY_TOTAL_HEIGHT/2 + STAKE_DEPTH)

    Print flat on plate: body+stake printed together in one orientation.
    Recommended: stake tip DOWN, body/text face UP — text prints with best detail.
    """
    body = make_body()

    # Stake: position so it starts at body base and extends downward
    # Body base = -BODY_TOTAL_HEIGHT/2; stake center Y = body_base - STAKE_DEPTH/2
    stake_y = -(BODY_TOTAL_HEIGHT / 2) - (STAKE_DEPTH / 2)

    # Build stake as a simple tapered box (more reliable than build123d loft in FDM context)
    # We use a standard box + chamfer approach
    try:
        tip_w = max(STAKE_WIDTH - 2 * STAKE_TAPER, 2.0)
        # Full stake box
        stake = Box(STAKE_WIDTH, STAKE_DEPTH, BODY_THICKNESS)
        # Chamfer bottom edges to form tip
        try:
            stake = fillet(
                stake.edges().filter_by_position(
                    Axis.Y,
                    -STAKE_DEPTH / 2 - 0.1,
                    -STAKE_DEPTH / 2 + 0.1,
                ),
                radius=min(STAKE_TAPER, STAKE_WIDTH / 2 - 0.5),
            )
        except Exception:
            pass
        stake = Pos(0, stake_y, 0) * stake
    except Exception:
        # Fallback: plain rectangular stake
        stake = Pos(0, stake_y, 0) * Box(STAKE_WIDTH, STAKE_DEPTH, BODY_THICKNESS)

    marker = body + stake

    # Embossed text on front face (+Z) of body, upper third
    try:
        text_solid = Text(
            plant_name,
            font_size=TEXT_FONT_SIZE,
            align=(Align.CENTER, Align.CENTER),
        )
        text_extrude = extrude(text_solid, amount=TEXT_DEPTH)
        text_extrude = Pos(
            0,
            TEXT_Y_OFFSET,          # upper portion of body
            BODY_THICKNESS / 2,     # on the +Z face
        ) * text_extrude
        marker = marker + text_extrude
    except Exception as e:
        print(f"  WARNING: Text emboss failed ({e}). Exporting marker without text.")

    return marker


def export_marker(plant_name: str, output_path: str) -> None:
    print(f"Building plant marker: '{plant_name}' → {output_path}")
    marker = make_plant_marker(plant_name)
    export_stl(marker, output_path)
    print(f"  Exported: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate garden plant marker STL files in ASA (SKU Batch 2)"
    )
    parser.add_argument(
        "--plant",
        type=str,
        default=None,
        help="Single plant name to export (e.g. TOMATO). Default: exports all variants.",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Export all plant name variants",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="./stl",
        help="Output directory for STL files (default: ./stl)",
    )
    parser.add_argument(
        "--stake-width",
        type=float,
        default=None,
        help=f"Override ground stake width in mm (default {STAKE_WIDTH}). "
             f"Increase if stake bends; decrease if stake won't penetrate soil.",
    )
    parser.add_argument(
        "--stake-depth",
        type=float,
        default=None,
        help=f"Override ground stake depth in mm (default {STAKE_DEPTH}). "
             f"Increase for loose/sandy soil that doesn't grip short stakes.",
    )
    parser.add_argument(
        "--body-height",
        type=float,
        default=None,
        help=f"Override body height in mm (default {BODY_TOTAL_HEIGHT}). "
             f"Taller body = more visible over ground-level foliage.",
    )
    parser.add_argument(
        "--text-depth",
        type=float,
        default=None,
        help=f"Override text emboss depth in mm (default {TEXT_DEPTH}). "
             f"Increase to 0.5mm if text washes out in photos.",
    )
    args = parser.parse_args()

    # Apply parameter overrides
    import sku_batch_2_plant_markers as _self
    if args.stake_width is not None:
        _self.STAKE_WIDTH = args.stake_width
        print(f"Using custom stake width: {args.stake_width}mm")
    if args.stake_depth is not None:
        _self.STAKE_DEPTH = args.stake_depth
        print(f"Using custom stake depth: {args.stake_depth}mm")
    if args.body_height is not None:
        _self.BODY_TOTAL_HEIGHT = args.body_height
        print(f"Using custom body height: {args.body_height}mm")
    if args.text_depth is not None:
        _self.TEXT_DEPTH = args.text_depth
        print(f"Using custom text depth: {args.text_depth}mm")

    os.makedirs(args.output_dir, exist_ok=True)

    # Determine which plants to export
    if args.all or args.plant is None:
        plants = PLANT_VARIANTS
    else:
        plants = [args.plant.upper()]

    for plant in plants:
        safe_name = plant.lower().replace(" ", "_")
        output_path = os.path.join(args.output_dir, f"plant_marker_{safe_name}.stl")
        export_marker(plant, output_path)

    print(f"\nDone. {len(plants)} marker(s) exported to {args.output_dir}/")
    print(f"\nTuning notes (adjust constants at top of file, or pass as CLI args):")
    print(f"  Stake bends in soil:        increase --stake-width (now {STAKE_WIDTH}mm)")
    print(f"  Stake won't penetrate hard soil: decrease --stake-width (now {STAKE_WIDTH}mm)")
    print(f"  Marker too short/tall:      adjust --body-height (now {BODY_TOTAL_HEIGHT}mm)")
    print(f"  Text not legible:           increase --text-depth (now {TEXT_DEPTH}mm)")
    print(f"\nASA PRINT REMINDER:")
    print(f"  Hotend:    240–250°C  (PLA setting 220°C will cause poor layer adhesion)")
    print(f"  Bed:       100–110°C  (PLA setting 60°C will cause ASA warping)")
    print(f"  Enclosure: CLOSED     (open enclosure = warp + delamination)")
    print(f"  Fan:       Off for first 5 layers, then 20–30% max")


if __name__ == "__main__":
    main()
