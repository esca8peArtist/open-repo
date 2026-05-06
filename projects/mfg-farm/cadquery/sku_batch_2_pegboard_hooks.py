"""
SKU Batch 2 — Pegboard Hook System — 3 sizes (build123d)

Generates J-hook style pegboard hooks with embossed category labels.
Fits standard 1/4" (6.35mm) pegboard holes via a press-fit peg.
Three size variants (Small/Medium/Large) for different tool weights.

Usage:
    python sku_batch_2_pegboard_hooks.py --output-dir ./stl/
    python sku_batch_2_pegboard_hooks.py --size small --output-dir ./stl/
    python sku_batch_2_pegboard_hooks.py --all --output-dir ./stl/
    python sku_batch_2_pegboard_hooks.py --peg-diameter 5.9 --output-dir ./stl/

Print settings (PLA+):
    Layer height:  0.20mm
    Infill:        40%  (higher than labels — hooks take mechanical load)
    Walls:         4    (one extra wall vs. label tiles for shear resistance)
    Hotend:        220–225°C
    Bed:           60°C
    Supports:      None if printed peg-down (hook arm prints as overhang — acceptable)
    Orientation:   Peg pointing UP, hook arm pointing DOWN and forward
    Print time:    12–15 min (small), 15–18 min (medium), 18–22 min (large)

Cost:
    Small:    ~$0.16 filament;  retail $0.80–1.00
    Medium:   ~$0.19 filament;  retail $1.00–1.25
    Large:    ~$0.22 filament;  retail $1.25–1.50
    Starter set (8S + 8M + 4L): retail $28–32 (71% net margin)
"""

import argparse
import os

from build123d import *

# ============================================================
# Geometry constants — adjust after first test print
# ============================================================

# Pegboard peg — CRITICAL TOLERANCE
# Standard pegboard hole: 6.35mm (1/4 inch) diameter.
# Peg printed at 5.8mm gives 0.55mm total clearance → snug fit, no rattle.
# Tolerance sensitivity:
#   < 5.7mm: peg rattles in hole; hook falls under load
#   > 6.1mm: peg won't insert without reaming
# Adjust ±0.05–0.1mm after test-fitting actual pegboard.
PEG_DIAMETER = 5.8       # mm — hook peg OD (target: 0.5–0.6mm under pegboard hole)
PEG_LENGTH = 9.0         # mm — peg insertion depth (must clear pegboard thickness ~4–6mm)
PEGBOARD_HOLE = 6.35     # mm — reference only (standard 1/4" pegboard); not used in geometry

# Vertical post (connects peg socket to hook arm)
POST_WIDTH = 8.0         # mm — post width (X)
POST_DEPTH = 6.0         # mm — post depth (Y, front to back)

# Hook arm — J-hook horizontal section
# Arm extends forward from the post base at an angle slightly upward to prevent tool slide-off.
ARM_UPTURN = 5.0         # mm — upward curve at arm tip (prevents tools sliding off)
ARM_THICKNESS = 4.0      # mm — arm cross-section height (vertical dimension under load)
ARM_WIDTH = POST_WIDTH   # mm — arm cross-section width (same as post, no ledge)

# Wall thickness constants
WALL_THICKNESS = 3.0     # mm — minimum wall in peg socket region

# Text emboss on front face of post
TEXT_FONT_SIZE = 4.5     # pt — small font to fit on post face (4–5pt range)
TEXT_DEPTH = 0.35        # mm — emboss extrusion (shallow — post face is narrow)

# Size variants — drives hook arm depth and opening height
SIZE_CONFIGS = {
    "small": {
        "hook_depth": 35.0,    # mm — arm horizontal reach from post face
        "opening": 12.0,       # mm — vertical opening below arm (tool clearance)
        "post_height": 28.0,   # mm — vertical post height
        "label_default": "BITS",
    },
    "medium": {
        "hook_depth": 45.0,
        "opening": 15.0,
        "post_height": 32.0,
        "label_default": "WRENCHES",
    },
    "large": {
        "hook_depth": 55.0,
        "opening": 18.0,
        "post_height": 36.0,
        "label_default": "DRILLS",
    },
}

# Label variants (user selects at export time)
LABEL_VARIANTS = ["DRILLS", "BITS", "WRENCHES", "SOCKETS", "CHISELS", "MISC"]


def make_peg_socket(post_height: float) -> Solid:
    """
    Cylindrical peg that inserts into pegboard hole.

    The peg attaches to the top of the vertical post.
    Geometry: solid cylinder (no internal features needed — FDM gives sufficient friction).
    The peg overhangs the post top — print with peg pointing UP for clean layer adhesion.
    """
    peg = Cylinder(
        radius=PEG_DIAMETER / 2,
        height=PEG_LENGTH,
    )
    # Position peg so it sits on top of post (+Y direction = up)
    # Peg center Y = post_height/2 + PEG_LENGTH/2
    peg = Pos(0, post_height / 2 + PEG_LENGTH / 2, 0) * peg

    return peg


def make_post(post_height: float) -> Solid:
    """
    Vertical rectangular post — main structural member.
    Peg attaches to top; hook arm attaches to front face at bottom.
    Origin at post center (0, 0, 0).
    """
    post = Box(POST_WIDTH, post_height, POST_DEPTH)
    return post


def make_hook_arm(hook_depth: float, opening: float, post_height: float) -> Solid:
    """
    J-hook arm assembly — horizontal arm extending forward from post base.

    Geometry:
      - Horizontal arm extends forward (Z direction) from post front face
      - Arm cross-section: ARM_WIDTH × ARM_THICKNESS
      - Arm tip turns upward by ARM_UPTURN mm (prevents tool slide-off)
      - Opening = vertical gap between arm top and the wall behind it
                  (determines max tool shaft diameter that fits)

    The arm connects to the post at Y = -(post_height/2) + ARM_THICKNESS/2
    (flush with post base, on front face of post).
    """
    # Horizontal arm body
    arm = Box(ARM_WIDTH, ARM_THICKNESS, hook_depth)
    # Position: centered on post X; flush to post bottom Y; extending forward from post front face
    arm_z = POST_DEPTH / 2 + hook_depth / 2   # forward of post
    arm_y = -(post_height / 2) + ARM_THICKNESS / 2  # at post bottom
    arm = Pos(0, arm_y, arm_z) * arm

    # Upturn at tip (small riser prevents tools sliding off end)
    if ARM_UPTURN > 0:
        upturn = Box(ARM_WIDTH, ARM_UPTURN, ARM_THICKNESS)
        upturn_y = arm_y + ARM_THICKNESS / 2 + ARM_UPTURN / 2
        upturn_z = POST_DEPTH / 2 + hook_depth - ARM_THICKNESS / 2
        upturn = Pos(0, upturn_y, upturn_z) * upturn
        arm = arm + upturn

    return arm


def make_hook(size: str, label_text: str) -> Solid:
    """
    Assemble peg + post + arm + embossed label into a complete pegboard hook.

    Print orientation: Peg pointing UP (+Y), hook arm extending toward printer door.
    This orientation means:
      - Peg layers are horizontal (strong in tension when hook is loaded downward)
      - Post layers are vertical (strong in bending)
      - Hook arm layers are horizontal (strong in tension from hanging weight)
    No support material required in this orientation.
    """
    cfg = SIZE_CONFIGS[size]
    post_height = cfg["post_height"]
    hook_depth = cfg["hook_depth"]
    opening = cfg["opening"]

    post = make_post(post_height)
    peg = make_peg_socket(post_height)
    arm = make_hook_arm(hook_depth, opening, post_height)

    hook = post + peg + arm

    # Fillet post vertical edges for cleaner appearance
    try:
        hook = fillet(
            hook.edges().filter_by(Axis.Y),
            radius=1.0,
        )
    except Exception:
        pass  # cosmetic

    # Embossed text on front face (+Z) of post, centered vertically
    try:
        text_solid = Text(
            label_text,
            font_size=TEXT_FONT_SIZE,
            align=(Align.CENTER, Align.CENTER),
        )
        text_extrude = extrude(text_solid, amount=TEXT_DEPTH)
        # Position: centered XY on post, on front face (+Z face)
        text_extrude = Pos(
            0,
            0,                      # vertical center of post
            POST_DEPTH / 2,         # front face of post
        ) * text_extrude
        hook = hook + text_extrude
    except Exception as e:
        print(f"  WARNING: Text emboss failed ({e}). Exporting hook without text.")

    return hook


def export_hook(size: str, label_text: str, output_path: str) -> None:
    cfg = SIZE_CONFIGS[size]
    print(f"Building hook: size={size}, label='{label_text}', "
          f"depth={cfg['hook_depth']}mm → {output_path}")
    hook = make_hook(size, label_text)
    export_stl(hook, output_path)
    print(f"  Exported: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate pegboard hook STL files (SKU Batch 2)"
    )
    parser.add_argument(
        "--size",
        choices=["small", "medium", "large"],
        default=None,
        help="Hook size to export. Default: exports all three sizes.",
    )
    parser.add_argument(
        "--label",
        type=str,
        default=None,
        help="Label text to emboss. Default: uses size default (BITS/WRENCHES/DRILLS).",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Export all sizes × all labels (24 STL files total: 3 sizes × 8 labels)",
    )
    parser.add_argument(
        "--all-sizes",
        action="store_true",
        help="Export all 3 sizes with default labels (3 STL files)",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="./stl",
        help="Output directory for STL files (default: ./stl)",
    )
    parser.add_argument(
        "--peg-diameter",
        type=float,
        default=None,
        help=f"Override peg OD in mm (default {PEG_DIAMETER}). "
             f"Standard pegboard hole is {PEGBOARD_HOLE}mm. "
             f"Increase if peg rattles; decrease if peg won't insert.",
    )
    parser.add_argument(
        "--text-depth",
        type=float,
        default=None,
        help=f"Override text emboss depth in mm (default {TEXT_DEPTH}). "
             f"Increase to 0.5mm if text washes out under studio lighting.",
    )
    parser.add_argument(
        "--arm-thickness",
        type=float,
        default=None,
        help=f"Override hook arm thickness in mm (default {ARM_THICKNESS}). "
             f"Increase if arm deflects under rated load.",
    )
    args = parser.parse_args()

    # Apply parameter overrides
    import sku_batch_2_pegboard_hooks as _self
    if args.peg_diameter is not None:
        _self.PEG_DIAMETER = args.peg_diameter
        print(f"Using custom peg diameter: {args.peg_diameter}mm")
    if args.text_depth is not None:
        _self.TEXT_DEPTH = args.text_depth
        print(f"Using custom text depth: {args.text_depth}mm")
    if args.arm_thickness is not None:
        _self.ARM_THICKNESS = args.arm_thickness
        print(f"Using custom arm thickness: {args.arm_thickness}mm")

    os.makedirs(args.output_dir, exist_ok=True)

    # Determine export scope
    if args.all:
        # All sizes × all labels
        exports = [
            (size, label)
            for size in ["small", "medium", "large"]
            for label in LABEL_VARIANTS
        ]
    elif args.all_sizes:
        # All sizes, default label per size
        exports = [
            (size, SIZE_CONFIGS[size]["label_default"])
            for size in ["small", "medium", "large"]
        ]
    elif args.size is not None:
        # Specific size, optionally with label override
        label = args.label.upper() if args.label else SIZE_CONFIGS[args.size]["label_default"]
        exports = [(args.size, label)]
    else:
        # Default: all sizes, default labels
        exports = [
            (size, SIZE_CONFIGS[size]["label_default"])
            for size in ["small", "medium", "large"]
        ]

    for size, label in exports:
        safe_label = label.lower().replace(" ", "_")
        filename = f"pegboard_hook_{size}_{safe_label}.stl"
        output_path = os.path.join(args.output_dir, filename)
        export_hook(size, label, output_path)

    print(f"\nDone. {len(exports)} hook(s) exported to {args.output_dir}/")
    print(f"\nTuning notes (adjust constants at top of file, or pass as CLI args):")
    print(f"  Peg rattles in pegboard:     increase --peg-diameter (now {PEG_DIAMETER}mm)")
    print(f"  Peg won't insert:            decrease --peg-diameter (now {PEG_DIAMETER}mm)")
    print(f"  Arm deflects under load:     increase --arm-thickness (now {ARM_THICKNESS}mm)")
    print(f"  Text hard to read:           increase --text-depth (now {TEXT_DEPTH}mm)")
    print(f"  Hook slides off peg:         increase PEG_LENGTH (now {PEG_LENGTH}mm)")
    print(f"\nPrint orientation: peg UP (+Y), arm extending toward front of printer.")
    print(f"Infill 40% recommended (higher than labels) — hooks take real mechanical load.")
    print(f"\nLoad test targets:")
    print(f"  Small:  2 kg sustained (hand tools, bit sets)")
    print(f"  Medium: 5 kg sustained (wrenches, drill bits)")
    print(f"  Large:  10 kg sustained (power tools, heavy items)")


if __name__ == "__main__":
    main()
