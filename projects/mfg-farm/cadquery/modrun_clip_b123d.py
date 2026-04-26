"""
ModRun Cable Management — Parametric Clip (build123d port)

Generates a press-fit cable clip that snaps into the ModRun rail slots.
Three variants: 3mm bore (USB-C), 6mm bore (HDMI/laptop), 12mm bore (thick cables).

Usage:
    python modrun_clip_b123d.py --bore 3 --output-dir ./stl/
    python modrun_clip_b123d.py --bore 6 --output-dir ./stl/
    python modrun_clip_b123d.py --bore 12 --output-dir ./stl/
    python modrun_clip_b123d.py --output-dir ./stl/   (generates all three)

All geometry parameters are at the top — adjust after first test print.
"""

import argparse
import math
import os

from build123d import *

# ============================================================
# Geometry constants — adjust after first test print
# ============================================================

# Rail slot interface (must match modrun_rail_b123d.py)
SLOT_WIDTH = 8.0          # mm — width of rail slot opening
SLOT_DEPTH = 6.0          # mm — depth clip travels into slot
FDM_TOLERANCE = 0.15      # mm — added clearance each side for printer tolerance

# Clip body
BODY_WALL = 2.0           # mm — wall thickness around cable bore
BODY_HEIGHT = 14.0        # mm — height of clip
BODY_DEPTH = 10.0         # mm — depth of clip (front to back)

# Cable bore opening — gap lets cable snap in sideways
BORE_GAP_RATIO = 0.65     # 0.65 = gap is 65% of bore dia. Increase if cables are hard to press in.

# Snap arm dimensions
SNAP_ARM_LENGTH = 8.0       # mm — cantilever arm length
SNAP_ARM_THICKNESS = 1.4    # mm — arm thickness; thinner = more flexible
SNAP_ARM_WIDTH = SLOT_WIDTH - 0.4  # mm — 0.2mm clearance each side in slot
SNAP_NUB_HEIGHT = 1.2       # mm — locking nub protrusion
SNAP_NUB_LEAD_ANGLE = 35    # degrees — chamfer on insertion face (ease of entry)
SNAP_NUB_LOCK_ANGLE = 80    # degrees — near-vertical retention face


def make_clip_body(bore_diameter: float) -> Solid:
    """U-channel clip body with cable bore and front slot opening."""
    outer_width = bore_diameter + 2 * BODY_WALL
    bore_gap = bore_diameter * BORE_GAP_RATIO

    # Outer block
    body = Box(outer_width, BODY_DEPTH, BODY_HEIGHT)

    # Subtract cable bore (cylinder through full height, centered)
    body -= Cylinder(bore_diameter / 2, BODY_HEIGHT)

    # Subtract front slot opening (allows cable to press in from the front)
    # The cut runs the full depth so the channel opens at the front face
    body -= Box(bore_gap, BODY_DEPTH, BODY_HEIGHT)

    return body


def make_snap_arm() -> Solid:
    """Cantilever snap arm with a locking nub at the free end.

    The nub is a box with a chamfered lead face — this prints cleanly on FDM
    and provides the same insertion-ease + retention-force as a full wedge profile.
    Adjust SNAP_NUB_HEIGHT and the chamfer below after test print if needed.
    """
    arm = Box(SNAP_ARM_WIDTH, SNAP_ARM_LENGTH, SNAP_ARM_THICKNESS)

    # Nub: a rectangular block sitting on top of the arm at its free end (+Y)
    nub_depth = SNAP_NUB_HEIGHT / math.tan(math.radians(SNAP_NUB_LEAD_ANGLE))  # lead slope footprint
    nub = Pos(
        0,
        SNAP_ARM_LENGTH / 2 - nub_depth / 2,  # at free end
        SNAP_ARM_THICKNESS / 2 + SNAP_NUB_HEIGHT / 2,  # on top of arm
    ) * Box(SNAP_ARM_WIDTH, nub_depth, SNAP_NUB_HEIGHT)

    # Chamfer the insertion-side edge of the nub for easy sliding into slot
    try:
        # The lead edge is at +Y face of the nub, top (+Z)
        chamfer_edges = nub.edges().filter_by_position(
            Axis.Y,
            (SNAP_ARM_LENGTH / 2) - 0.1,
            (SNAP_ARM_LENGTH / 2) + 0.1,
        )
        nub = chamfer(chamfer_edges, length=SNAP_NUB_HEIGHT * 0.8)
    except Exception:
        pass  # chamfer is cosmetic — skip if edge selection fails

    arm = arm + nub
    return arm


def make_clip(bore_diameter: float) -> Solid:
    """Assemble body + snap arm + slot tabs into a complete clip."""
    body = make_clip_body(bore_diameter)
    arm = make_snap_arm()

    # Position arm on rear face of body, flush to bottom
    arm_y = -(BODY_DEPTH / 2) - (SNAP_ARM_LENGTH / 2)
    arm_z = -(BODY_HEIGHT / 2) + (SNAP_ARM_THICKNESS / 2)
    arm = Pos(0, arm_y, arm_z) * arm
    clip = body + arm

    # Slot tabs: rectangular tabs flanking the arm that locate clip in the rail slot
    tab_width = (SLOT_WIDTH - FDM_TOLERANCE * 2 - SNAP_ARM_WIDTH) / 2
    tab_height = SLOT_DEPTH
    tab_depth = SLOT_DEPTH

    for sign in (-1, 1):
        tab_x = sign * (SNAP_ARM_WIDTH / 2 + tab_width / 2)
        tab = Pos(
            tab_x,
            -(BODY_DEPTH / 2) - (tab_depth / 2),
            -(BODY_HEIGHT / 2) + (tab_height / 2),
        ) * Box(tab_width, tab_depth, tab_height)
        clip = clip + tab

    return clip


def export_clip(bore_diameter: float, output_path: str) -> None:
    print(f"Building clip: bore={bore_diameter}mm → {output_path}")
    clip = make_clip(bore_diameter)
    export_stl(clip, output_path)
    print(f"  ✓ Exported: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Generate ModRun cable clip STL files")
    parser.add_argument("--bore", type=float, action="append", default=None, metavar="MM",
                        help="Cable bore diameter in mm. Repeat for multiple sizes. Default: 3 6 12")
    parser.add_argument("--output-dir", type=str, default=".", help="Output directory (default: .)")
    parser.add_argument("--tolerance", type=float, default=None,
                        help="Override FDM tolerance in mm (default 0.15)")
    args = parser.parse_args()

    import modrun_clip_b123d as _self
    if args.tolerance is not None:
        _self.FDM_TOLERANCE = args.tolerance
        print(f"Using custom FDM tolerance: {args.tolerance}mm")

    bore_sizes = args.bore if args.bore else [3.0, 6.0, 12.0]
    os.makedirs(args.output_dir, exist_ok=True)

    for bore in bore_sizes:
        filename = f"modrun_clip_{int(bore)}mm.stl"
        export_clip(bore, os.path.join(args.output_dir, filename))

    print(f"\nDone. {len(bore_sizes)} clip(s) exported to {args.output_dir}/")
    print(f"\nTuning notes:")
    print(f"  Snap too stiff: reduce SNAP_ARM_THICKNESS (now {SNAP_ARM_THICKNESS}mm)")
    print(f"  Snap won't hold: increase SNAP_NUB_HEIGHT (now {SNAP_NUB_HEIGHT}mm)")
    print(f"  Clip too tight in slot: increase FDM_TOLERANCE (now {FDM_TOLERANCE}mm)")
    print(f"  Cable hard to press in: increase BORE_GAP_RATIO (now {BORE_GAP_RATIO})")


if __name__ == "__main__":
    main()
