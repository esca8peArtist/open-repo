"""
ModRun Cable Management — Parametric Rail (build123d port)

Generates the mounting rail that accepts ModRun clips.
Two variants:
  desk_clamp — C-shaped clamp grips desk edge 15–30mm thick (no adhesive)
  adhesive   — flat base with 4 recessed pockets for 3M Command 20mm adhesive pads

Usage:
    python modrun_rail_b123d.py --variant desk_clamp --output-dir ./stl/
    python modrun_rail_b123d.py --variant adhesive --output-dir ./stl/
    python modrun_rail_b123d.py --output-dir ./stl/   (generates both)
    python modrun_rail_b123d.py --clamp-gap 25 --output-dir ./stl/

All geometry parameters are at the top — adjust after first test print.
"""

import argparse
import os

from build123d import *

# ============================================================
# Rail body constants (must match modrun_clip_b123d.py)
# ============================================================

RAIL_LENGTH = 200.0   # mm — total length of rail
RAIL_HEIGHT = 16.0    # mm — height of rail body above mounting surface
RAIL_DEPTH = 24.0     # mm — front-to-back depth of rail body

SLOT_COUNT = 6        # number of clip slots
SLOT_PITCH = 30.0     # mm — centre-to-centre slot spacing
SLOT_WIDTH = 8.0      # mm — slot opening width (matches modrun_clip_b123d.py)
SLOT_DEPTH = 6.0      # mm — slot depth (how far clip travels in Z)

# Snap nub recess — counter-geometry to clip snap nub
NUB_RECESS_DEPTH = 1.4   # mm — recess depth (≥ SNAP_NUB_HEIGHT in clip script)
NUB_RECESS_HEIGHT = 2.0  # mm — height of the recess ledge
NUB_RECESS_POS = 4.0     # mm from slot bottom to recess centre

WALL_THICKNESS = 3.0     # mm — wall between slots and rail exterior
FDM_TOLERANCE = 0.15     # mm — printer tolerance compensation

# ============================================================
# Mounting foot constants
# ============================================================

# Desk clamp
CLAMP_ARM_THICKNESS = 4.0    # mm — clamp arm thickness
CLAMP_LOWER_OVERHANG = 28.0  # mm — lower jaw length
CLAMP_GAP = 22.0             # mm — nominal jaw opening (15–30mm range)

# Adhesive base
ADHESIVE_PAD_SIZE = 20.0     # mm — 3M Command pad is 20×20mm
ADHESIVE_PAD_DEPTH = 1.5     # mm — recess depth (flush with pad installed)
ADHESIVE_PAD_COUNT = 4
ADHESIVE_BASE_HEIGHT = 6.0   # mm — slab below rail body


def make_rail_body() -> Solid:
    """Main rail bar with clip slots and snap nub recesses."""
    # Rail is built with origin at bottom-left-front corner for easier slot positioning
    # CentreX = RAIL_LENGTH/2, CentreY = RAIL_DEPTH/2, CentreZ = RAIL_HEIGHT/2
    rail = Box(RAIL_LENGTH, RAIL_DEPTH, RAIL_HEIGHT)

    # Slot X positions — evenly spaced, centred in the rail
    total_span = (SLOT_COUNT - 1) * SLOT_PITCH
    x0 = -(total_span / 2)

    for i in range(SLOT_COUNT):
        slot_x = x0 + i * SLOT_PITCH

        # Slot opening: rectangular pocket from the top face downward
        # Width = SLOT_WIDTH (X), runs full depth (Y), depth = SLOT_DEPTH (Z from top)
        slot_cut = Pos(slot_x, 0, (RAIL_HEIGHT / 2) - (SLOT_DEPTH / 2)) * Box(
            SLOT_WIDTH + FDM_TOLERANCE * 2, RAIL_DEPTH, SLOT_DEPTH
        )
        rail -= slot_cut

        # Nub recess: cut into the back wall of each slot
        # Position: at the back (+Y side) of the slot, NUB_RECESS_POS from slot bottom
        recess_z = (RAIL_HEIGHT / 2) - SLOT_DEPTH + NUB_RECESS_POS
        nub_cut = Pos(
            slot_x,
            (RAIL_DEPTH / 2) - (NUB_RECESS_DEPTH / 2),
            recess_z,
        ) * Box(SLOT_WIDTH - 0.5, NUB_RECESS_DEPTH, NUB_RECESS_HEIGHT)
        rail -= nub_cut

    return rail


def make_desk_clamp(rail: Solid, clamp_gap: float = CLAMP_GAP) -> Solid:
    """Add C-clamp desk-edge mounting foot to the rail."""
    # Clamp back: vertical plate on rear face of rail
    back_height = clamp_gap + CLAMP_ARM_THICKNESS + RAIL_HEIGHT
    clamp_back = Pos(
        0,
        (RAIL_DEPTH / 2) + (CLAMP_ARM_THICKNESS / 2),
        (back_height / 2) - RAIL_HEIGHT,
    ) * Box(RAIL_LENGTH, CLAMP_ARM_THICKNESS, back_height)

    # Lower jaw: horizontal arm extending forward from the bottom of the clamp back
    lower_jaw = Pos(
        0,
        (RAIL_DEPTH / 2) + CLAMP_ARM_THICKNESS - (CLAMP_LOWER_OVERHANG / 2),
        -(clamp_gap + CLAMP_ARM_THICKNESS / 2),
    ) * Box(RAIL_LENGTH, CLAMP_LOWER_OVERHANG, CLAMP_ARM_THICKNESS)

    # Rubber pad recess on inner face of lower jaw (reduces marring, holds bumper)
    pad_recess = Pos(
        0,
        (RAIL_DEPTH / 2) + CLAMP_ARM_THICKNESS - 8.0,
        -(clamp_gap + 1.5),
    ) * Box(RAIL_LENGTH - 10, 15.0, 1.0)
    lower_jaw -= pad_recess

    return rail + clamp_back + lower_jaw


def make_adhesive_base(rail: Solid) -> Solid:
    """Add flat adhesive-pad base to the rail."""
    # Flat slab below rail body
    base = Pos(0, 0, -(ADHESIVE_BASE_HEIGHT / 2)) * Box(
        RAIL_LENGTH, RAIL_DEPTH, ADHESIVE_BASE_HEIGHT
    )

    # Adhesive pad pockets (4 pads, symmetrically placed)
    total_span = (SLOT_COUNT - 1) * SLOT_PITCH
    pad_positions = [
        (-(RAIL_LENGTH / 2) + 25, 0),
        ((RAIL_LENGTH / 2) - 25, 0),
        (-(SLOT_PITCH), 0),
        (SLOT_PITCH, 0),
    ]

    pocket_z = -(ADHESIVE_BASE_HEIGHT - ADHESIVE_PAD_DEPTH / 2)
    for px, py in pad_positions:
        pocket = Pos(px, py, pocket_z) * Box(
            ADHESIVE_PAD_SIZE, ADHESIVE_PAD_SIZE, ADHESIVE_PAD_DEPTH
        )
        base -= pocket

    # Rounded base corners (cosmetic)
    try:
        base = fillet(
            base.edges().filter_by_position(Axis.Z, -ADHESIVE_BASE_HEIGHT - 0.1, -ADHESIVE_BASE_HEIGHT + 0.1),
            radius=2.0,
        )
    except Exception:
        pass  # cosmetic — skip if edge selection fails

    return rail + base


def build_rail(variant: str, clamp_gap: float = CLAMP_GAP) -> Solid:
    body = make_rail_body()
    if variant == "desk_clamp":
        return make_desk_clamp(body, clamp_gap)
    elif variant == "adhesive":
        return make_adhesive_base(body)
    else:
        raise ValueError(f"Unknown variant '{variant}'. Use 'desk_clamp' or 'adhesive'.")


def export_rail(variant: str, output_path: str, clamp_gap: float = CLAMP_GAP) -> None:
    print(f"Building rail: variant={variant} → {output_path}")
    rail = build_rail(variant, clamp_gap)
    export_stl(rail, output_path)
    print(f"  ✓ Exported: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Generate ModRun rail STL files")
    parser.add_argument("--variant", choices=["desk_clamp", "adhesive", "both"],
                        default="both", help="Rail mounting variant (default: both)")
    parser.add_argument("--output-dir", type=str, default=".", help="Output directory")
    parser.add_argument("--clamp-gap", type=float, default=CLAMP_GAP,
                        help=f"Clamp jaw opening in mm (default {CLAMP_GAP}). Range 15–30.")
    parser.add_argument("--length", type=float, default=None,
                        help=f"Rail length override in mm (default {RAIL_LENGTH}mm)")
    args = parser.parse_args()

    if args.length is not None:
        import modrun_rail_b123d as _self
        _self.RAIL_LENGTH = args.length

    os.makedirs(args.output_dir, exist_ok=True)
    variants = ["desk_clamp", "adhesive"] if args.variant == "both" else [args.variant]

    for v in variants:
        output_path = os.path.join(args.output_dir, f"modrun_rail_{v}.stl")
        export_rail(v, output_path, args.clamp_gap)

    print(f"\nDone. {len(variants)} rail(s) exported to {args.output_dir}/")
    print(f"\nTuning notes:")
    print(f"  Clamp doesn't fit desk: adjust --clamp-gap (now {args.clamp_gap}mm)")
    print(f"  Clips don't seat: check SLOT_DEPTH matches clip's SLOT_DEPTH")
    print(f"  Clips fall out: increase NUB_RECESS_DEPTH (now {NUB_RECESS_DEPTH}mm)")


if __name__ == "__main__":
    main()
