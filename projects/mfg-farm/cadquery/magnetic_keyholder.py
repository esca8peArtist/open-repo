"""
Magnetic Wall Keyholder — Parametric Design (CadQuery)

A wall-mounted keyholder with embedded N52 disc magnet pockets, integrated key hooks,
and M4 countersunk wall-mounting screw holes.

Three variants exported by default:
  keyholder_3hook    — 3 key hooks (standard)
  keyholder_1hook    — 1 key hook (minimalist)
  keyholder_nohook   — no hooks (magnet-only shelf version)

Usage:
    python magnetic_keyholder.py --output-dir ./stl/
    python magnetic_keyholder.py --hooks 2 --output-dir ./stl/
    python magnetic_keyholder.py --width 150 --magnets 4 --output-dir ./stl/

Design notes:
  - Print orientation: flat back face down on build plate (magnets face up)
  - No supports required — magnet pockets open upward, hook tips are simple geometry
  - Recommended settings: 0.20mm layer height, 4 walls, 20% infill on Bambu P1S
  - Estimated print time: 55–70 min per unit at 0.20mm / 20% infill
  - Estimated weight: 30–45g depending on hook count
  - Magnets insert from front face after printing; 0.2mm floor retains magnet flush

Geometry coordinate system (all dimensions in mm):
  - X: left-right (positive = right)
  - Y: front-back (positive = toward viewer)
  - Z: vertical (positive = up)
  - Origin: centre of plate, mid-thickness (Y=0 = centreplane)

DEPENDENCY: cadquery>=2.3
Install:  pip install cadquery
          or: conda install -c conda-forge cadquery
"""

import argparse
import math
import os

import cadquery as cq

# ============================================================
# Parametric constants — adjust these for test-print tuning
# ============================================================

# Base plate
PLATE_WIDTH = 120.0        # mm — left-to-right width of base plate
PLATE_HEIGHT = 60.0        # mm — bottom-to-top height of base plate
PLATE_THICKNESS = 6.0      # mm — front-to-back thickness of base plate
CORNER_RADIUS = 5.0        # mm — base plate rounded corner radius

# Magnet pockets (N52 disc, 10mm dia x 3mm thick is standard)
MAGNET_COUNT = 3           # number of embedded magnet pockets
MAGNET_DIAMETER = 10.0     # mm — magnet outer diameter
MAGNET_HEIGHT = 3.0        # mm — magnet thickness
MAGNET_POCKET_DIAM = 10.2  # mm — pocket bore (0.2mm clearance for press-fit)
MAGNET_POCKET_DEPTH = 2.8  # mm — pocket depth (0.2mm floor retains magnet flush)
MAGNET_ROW_Z = 15.0        # mm — height of magnet centre row above plate bottom

# Key hooks
HOOK_COUNT = 3             # number of key hooks (0, 1, or 3 in exported variants)
HOOK_LENGTH = 25.0         # mm — hook arm length from plate face
HOOK_DIAMETER = 4.0        # mm — hook arm diameter (cylinder)
HOOK_ANGLE_DEG = 30.0      # degrees — downward angle from horizontal
HOOK_LIP_LENGTH = 3.0      # mm — tip lip length to retain keyrings
HOOK_LIP_DIAMETER = 6.0    # mm — diameter of lip ball at hook tip
HOOK_ROW_Z = 8.0           # mm — hook centre height above plate bottom (from centre)
HOOK_Z_FROM_BOTTOM = 8.0   # mm — hook centre height from plate bottom edge

# Wall-mounting screw holes (M4 countersunk)
SCREW_HOLE_DIAMETER = 4.5   # mm — clearance hole for M4 screw shank
COUNTERSINK_DIAMETER = 8.5  # mm — countersink head diameter (DIN 965 M4 = 8mm, +0.5 tolerance)
COUNTERSINK_DEPTH = 3.5     # mm — countersink depth (flush with M4 flat head)
SCREW_HOLE_SPACING = 80.0   # mm — horizontal centre-to-centre between the two screw holes
SCREW_HOLE_Z = 0.0          # mm — offset from plate vertical centre (0 = centred)

FDM_TOLERANCE = 0.15        # mm — general printer compensation tolerance


# ============================================================
# Builder functions
# ============================================================

def make_base_plate() -> cq.Workplane:
    """Rounded-corner base plate, centred at origin."""
    plate = (
        cq.Workplane("XZ")
        .rect(PLATE_WIDTH, PLATE_HEIGHT)
        .extrude(PLATE_THICKNESS)
    )
    # Move so plate is centred at X=0, Z=0, Y spans 0 to PLATE_THICKNESS
    plate = plate.translate((0, -PLATE_THICKNESS / 2, 0))

    # Apply rounded corners on XZ face — select edges parallel to Y axis
    try:
        plate = plate.edges("|Y").fillet(CORNER_RADIUS)
    except Exception:
        pass  # cosmetic — skip if edge selection fails on extreme parameters

    return plate


def make_magnet_pockets(plate: cq.Workplane) -> cq.Workplane:
    """Cut magnet pockets from the front face of the plate."""
    if MAGNET_COUNT == 0:
        return plate

    # Distribute pockets evenly across width, centred
    if MAGNET_COUNT == 1:
        xs = [0.0]
    else:
        spacing = (PLATE_WIDTH - 20.0) / (MAGNET_COUNT - 1)  # 10mm margin each side
        xs = [-(PLATE_WIDTH - 20.0) / 2 + i * spacing for i in range(MAGNET_COUNT)]

    # Pocket Z centre from plate bottom — MAGNET_ROW_Z measured from bottom = plate origin - PLATE_HEIGHT/2 + MAGNET_ROW_Z
    pocket_z = -PLATE_HEIGHT / 2 + MAGNET_ROW_Z

    for x in xs:
        plate = (
            plate
            .faces(">Y")                             # front face
            .workplane()
            .center(x, pocket_z)
            .hole(MAGNET_POCKET_DIAM, MAGNET_POCKET_DEPTH)  # hole() cuts from face inward
        )

    return plate


def make_screw_holes(plate: cq.Workplane) -> cq.Workplane:
    """Cut countersunk M4 screw holes through the plate from the back face."""
    screw_z = SCREW_HOLE_Z  # 0 = centred on plate height axis

    x_left = -SCREW_HOLE_SPACING / 2
    x_right = SCREW_HOLE_SPACING / 2

    for x in [x_left, x_right]:
        # Through-hole (shank clearance)
        plate = (
            plate
            .faces("<Y")                             # back face
            .workplane()
            .center(x, screw_z)
            .hole(SCREW_HOLE_DIAMETER, PLATE_THICKNESS)
        )
        # Countersink: larger bore from back face, limited depth
        plate = (
            plate
            .faces("<Y")
            .workplane()
            .center(x, screw_z)
            .hole(COUNTERSINK_DIAMETER, COUNTERSINK_DEPTH)
        )

    return plate


def make_hook_arm(x_pos: float) -> cq.Workplane:
    """
    Build a single key hook arm: cylinder angled 30° downward, with a spherical lip at tip.

    The hook arm origin is at the plate front face centre; it extends forward in Y
    and downward in Z at HOOK_ANGLE_DEG degrees.

    Args:
        x_pos: X position of hook centre on the plate.
    """
    angle_rad = math.radians(HOOK_ANGLE_DEG)

    # Hook arm cylinder — oriented along Y axis initially, then rotated
    hook = (
        cq.Workplane("YZ")
        .circle(HOOK_DIAMETER / 2)
        .extrude(HOOK_LENGTH)
    )

    # Rotate downward: positive X rotation tilts tip down
    hook = hook.rotate((0, 0, 0), (1, 0, 0), HOOK_ANGLE_DEG)

    # Tip lip: small sphere or cylinder at the end to retain keyrings
    # Tip position after rotation:
    tip_y = HOOK_LENGTH * math.cos(angle_rad)
    tip_z = -HOOK_LENGTH * math.sin(angle_rad)

    lip = (
        cq.Workplane("XZ")
        .sphere(HOOK_LIP_DIAMETER / 2)
        .translate((0, tip_y, tip_z))
    )

    hook = hook.union(lip)

    # Position at hook's mount point: front face of plate at correct X and Z
    hook_z = -PLATE_HEIGHT / 2 + HOOK_Z_FROM_BOTTOM
    hook = hook.translate((x_pos, PLATE_THICKNESS / 2, hook_z))

    return hook


def make_hooks(plate: cq.Workplane, hook_count: int) -> cq.Workplane:
    """Add key hook arms to the plate (0, 1, or N hooks)."""
    if hook_count == 0:
        return plate

    if hook_count == 1:
        xs = [0.0]
    else:
        margin = 20.0
        spacing = (PLATE_WIDTH - margin * 2) / (hook_count - 1)
        xs = [-(PLATE_WIDTH / 2 - margin) + i * spacing for i in range(hook_count)]

    result = plate
    for x in xs:
        arm = make_hook_arm(x)
        result = result.union(arm)

    return result


def build_keyholder(hook_count: int = HOOK_COUNT) -> cq.Workplane:
    """
    Assemble the full keyholder: base plate + magnet pockets + screw holes + hooks.

    Args:
        hook_count: Number of key hook arms to include (0, 1, 2, or 3).

    Returns:
        Complete CadQuery Workplane solid ready for STL export.
    """
    plate = make_base_plate()
    plate = make_magnet_pockets(plate)
    plate = make_screw_holes(plate)
    plate = make_hooks(plate, hook_count)
    return plate


def export_keyholder(hook_count: int, output_path: str) -> None:
    """Build and export a keyholder variant to STL."""
    label = f"hook_count={hook_count}"
    print(f"Building keyholder: {label} → {output_path}")
    part = build_keyholder(hook_count)
    cq.exporters.export(part, output_path)
    print(f"  Exported: {output_path}")


def main():
    # Declare globals first so override assignments later in the function are valid
    global PLATE_WIDTH, PLATE_HEIGHT, MAGNET_COUNT, SCREW_HOLE_SPACING

    parser = argparse.ArgumentParser(
        description="Generate parametric magnetic wall keyholder STL files"
    )
    parser.add_argument(
        "--hooks",
        type=int,
        default=None,
        metavar="N",
        help="Number of key hooks (0–5). If set, only one variant is exported.",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default=".",
        help="Output directory for STL files (default: .)",
    )
    parser.add_argument(
        "--width",
        type=float,
        default=None,
        help=f"Plate width override in mm (default {PLATE_WIDTH}mm)",
    )
    parser.add_argument(
        "--height",
        type=float,
        default=None,
        help=f"Plate height override in mm (default {PLATE_HEIGHT}mm)",
    )
    parser.add_argument(
        "--magnets",
        type=int,
        default=None,
        help=f"Magnet count override (default {MAGNET_COUNT})",
    )
    parser.add_argument(
        "--screw-spacing",
        type=float,
        default=None,
        help=f"M4 screw hole centre spacing in mm (default {SCREW_HOLE_SPACING}mm)",
    )
    args = parser.parse_args()

    # Apply overrides
    if args.width is not None:
        PLATE_WIDTH = args.width
    if args.height is not None:
        PLATE_HEIGHT = args.height
    if args.magnets is not None:
        MAGNET_COUNT = args.magnets
    if args.screw_spacing is not None:
        SCREW_HOLE_SPACING = args.screw_spacing

    os.makedirs(args.output_dir, exist_ok=True)

    if args.hooks is not None:
        # Single variant
        fname = f"keyholder_{args.hooks}hook.stl"
        export_keyholder(args.hooks, os.path.join(args.output_dir, fname))
        print(f"\nDone. 1 variant exported to {args.output_dir}/")
    else:
        # Standard three variants
        variants = [
            (3, "keyholder_3hook.stl"),
            (1, "keyholder_1hook.stl"),
            (0, "keyholder_nohook.stl"),
        ]
        for hook_count, fname in variants:
            export_keyholder(hook_count, os.path.join(args.output_dir, fname))

        print(f"\nDone. {len(variants)} variants exported to {args.output_dir}/")

    print("\nTuning notes:")
    print(f"  Magnets too loose: decrease MAGNET_POCKET_DIAM (now {MAGNET_POCKET_DIAM}mm)")
    print(f"  Magnets too tight: increase MAGNET_POCKET_DIAM by 0.1mm increments")
    print(f"  Screw holes misaligned: adjust SCREW_HOLE_SPACING (now {SCREW_HOLE_SPACING}mm)")
    print(f"  Hook arm too short: increase HOOK_LENGTH (now {HOOK_LENGTH}mm)")
    print(f"  Keys fall off hook: increase HOOK_LIP_DIAMETER (now {HOOK_LIP_DIAMETER}mm)")
    print(f"  Hook droops under load: increase HOOK_DIAMETER (now {HOOK_DIAMETER}mm)")


if __name__ == "__main__":
    main()
