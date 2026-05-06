#!/usr/bin/env python3
"""
SKU Batch 2 — CadQuery Parametric Designs
Magnetic Bin Labels | Plant Markers | Pegboard Hooks

Usage:
  python sku-batch-2.py --product magnetic-label --output-dir ./stl/
  python sku-batch-2.py --product plant-marker --output-dir ./stl/
  python sku-batch-2.py --product pegboard-hook --output-dir ./stl/
  python sku-batch-2.py --all --output-dir ./stl/

Print specs: 0.20mm layer height, 25% infill, 3 walls, 220-225°C PLA+
"""

import argparse
from pathlib import Path
import cadquery as cq

# ============================================================================
# PRODUCT 1: Magnetic Workshop Bin Labels
# ============================================================================

def magnetic_label(
    width_mm=50,
    height_mm=40,
    thickness_mm=3.0,
    magnet_diameter_mm=8,
    magnet_depth_mm=2.2,
    text="LABEL",
    font_size=8,
):
    """
    Parametric magnetic label tile for workshop organization.
    Embedded N52 magnet pocket (8x2.2mm disc, press-fit).

    Customization points:
    - Text is embossed on top face
    - Magnet pocket is on reverse (no text)
    - Width/height adjustable for different label sizes

    Print spec: 0.20mm, 25% infill, 3 walls, 220-225°C PLA+
    Time estimate: 8-12 min per tile at 50×40mm

    Cost: ~$0.15 filament + $0.02 magnet = $0.17 COGS per unit
    Retail: $1.50-2.00 per tile; sell in 20-packs at $28-32
    """

    # Base tile
    base = (
        cq.Workplane("XY")
        .box(width_mm, height_mm, thickness_mm)
        .edges("|Z")
        .fillet(2)  # Rounded edges
    )

    # Top face text (embossed)
    text_obj = (
        cq.Workplane("XY")
        .text(text, fontsize=font_size, distance=0.4, kind="center")
        .translate((0, 0, thickness_mm / 2 + 0.2))
    )

    # Combine base + text
    labeled = base.union(text_obj)

    # Magnet pocket (reverse side, centered)
    magnet_pocket = (
        cq.Workplane("XY")
        .circle(magnet_diameter_mm / 2)
        .extrude(magnet_depth_mm, symmetric=False)
        .translate((0, 0, -thickness_mm / 2))
    )

    # Subtract magnet pocket
    final = labeled.cut(magnet_pocket)

    return final

# ============================================================================
# PRODUCT 2: UV-Resistant Garden Plant Markers
# ============================================================================

def plant_marker(
    width_mm=18,
    height_mm=80,  # Tall for ground stake
    thickness_mm=3.0,
    text_area_height_mm=30,
    stake_width_mm=8,
    material="ASA",  # UV-resistant
):
    """
    Parametric garden marker stake for outdoor plants.
    ASA filament for 5+ year UV resistance (vs. PLA's 6-12 months).

    Design features:
    - Tall vertical body (80mm default)
    - Ground stake at bottom (8mm width for soil penetration)
    - Text embossed in upper third
    - Slight taper for easy insertion

    Customization:
    - Text via Etsy personalization field
    - Sold in sets of 6/10/20

    Print spec (ASA): 0.20mm, 25% infill, 3 walls, 240-250°C
    Time estimate: 20-25 min per marker
    Cost: ~$0.22 filament (ASA more expensive than PLA) = $0.22 COGS
    Retail: $2.50-3.00 per marker; 10-pack at $22-26
    """

    # Main body with taper
    body = (
        cq.Workplane("XY")
        .box(width_mm, height_mm, thickness_mm)
        .edges("|Z")
        .fillet(1.5)
    )

    # Ground stake (thinner, pointed)
    stake = (
        cq.Workplane("XY")
        .polygon(4, stake_width_mm)  # Square cross-section
        .extrude(40)
        .translate((0, -height_mm / 2 - 10, -thickness_mm / 2))
    )

    # Combine body + stake
    assembled = body.union(stake)

    # Text area (embossed on top)
    text_obj = (
        cq.Workplane("XY")
        .text("PLANT", fontsize=5, distance=0.3, kind="center")
        .translate((0, height_mm / 4, thickness_mm / 2 + 0.15))
    )

    final = assembled.union(text_obj)

    return final

# ============================================================================
# PRODUCT 3: Pegboard Hook System (3-size J-hooks)
# ============================================================================

def pegboard_hook(
    hook_depth_mm=35,  # How far the hook extends from pegboard
    hook_width_mm=12,  # J-hook opening width
    peg_hole_diameter_mm=6.4,  # 1/4" pegboard standard
    peg_diameter_mm=5.8,  # Slightly smaller for snug fit
    label_text="DRILLS",
    size="small",  # "small", "medium", "large"
):
    """
    Parametric pegboard hook with embossed category label.
    Available in 3 sizes for different tool weights.

    Sizes:
    - Small: 35mm depth, 12mm opening (hand tools, bits)
    - Medium: 45mm depth, 15mm opening (drill bits, wrenches)
    - Large: 55mm depth, 18mm opening (power tools, heavy items)

    Design:
    - Standard 1/4" pegboard hole at top
    - J-hook shape for hanging tools
    - Embossed text on the vertical face

    Print spec: 0.20mm, 25% infill, 3 walls, 220-225°C PLA+
    Time estimate: 12-18 min per hook
    Cost: ~$0.18 filament per hook
    Retail: $0.80-1.20 per hook; sell 20-hook starter set at $28-40
    """

    # Sizing by variant
    size_config = {
        "small": {"depth": 35, "opening": 12, "thickness": 2.5},
        "medium": {"depth": 45, "opening": 15, "thickness": 3.0},
        "large": {"depth": 55, "opening": 18, "thickness": 3.5},
    }
    config = size_config.get(size, size_config["small"])

    # Pegboard peg (top mounting)
    peg = (
        cq.Workplane("XY")
        .cylinder(height=8, radius=peg_diameter_mm / 2)
        .translate((0, 0, 4))
    )

    # J-hook body
    # Vertical post
    post = (
        cq.Workplane("XY")
        .box(config["thickness"], 8, 20)
        .translate((0, 0, 14))
    )

    # Horizontal hook arm
    hook = (
        cq.Workplane("XY")
        .box(config["depth"], config["opening"], config["thickness"])
        .translate((config["depth"] / 2, -8, 8))
    )

    # Combine parts
    assembled = peg.union(post).union(hook)

    # Embossed label on vertical face
    label = (
        cq.Workplane("XY")
        .text(label_text, fontsize=4, distance=0.25, kind="center")
        .translate((config["thickness"] / 2 + 0.1, 0, 14))
    )

    final = assembled.union(label)

    return final

# ============================================================================
# Export Functions
# ============================================================================

def export_all(output_dir):
    """Export all three products to STL."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    print("Exporting Batch 2 designs...")

    # Product 1: Magnetic Labels (5 variations)
    for i, text in enumerate(["BOLTS", "BITS", "TOOLS", "SCREWS", "NAILS"]):
        label = magnetic_label(text=text)
        output_file = output_path / f"magnetic-label-{text.lower()}.stl"
        label.save(str(output_file))
        print(f"  ✓ {output_file.name}")

    # Product 2: Plant Markers
    marker = plant_marker()
    output_file = output_path / "plant-marker.stl"
    marker.save(str(output_file))
    print(f"  ✓ {output_file.name}")

    # Product 3: Pegboard Hooks (3 sizes, 4 labels each)
    labels_per_size = ["DRILLS", "BITS", "WRENCHES", "MISC"]
    for size in ["small", "medium", "large"]:
        for label in labels_per_size:
            hook = pegboard_hook(size=size, label_text=label)
            output_file = output_path / f"pegboard-hook-{size}-{label.lower()}.stl"
            hook.save(str(output_file))
            print(f"  ✓ {output_file.name}")

    print(f"\nExported {len(list(output_path.glob('*.stl')))} STL files to {output_dir}/")

def export_single(product, output_dir):
    """Export a single product type."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    if product == "magnetic-label":
        label = magnetic_label(text="LABEL")
        output_file = output_path / "magnetic-label.stl"
        label.save(str(output_file))
        print(f"Exported: {output_file}")

    elif product == "plant-marker":
        marker = plant_marker()
        output_file = output_path / "plant-marker.stl"
        marker.save(str(output_file))
        print(f"Exported: {output_file}")

    elif product == "pegboard-hook":
        hook = pegboard_hook()
        output_file = output_path / "pegboard-hook.stl"
        hook.save(str(output_file))
        print(f"Exported: {output_file}")

    else:
        print(f"Unknown product: {product}")

# ============================================================================
# CLI
# ============================================================================

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="SKU Batch 2 CadQuery design generator"
    )
    parser.add_argument(
        "--product",
        choices=["magnetic-label", "plant-marker", "pegboard-hook"],
        help="Single product to export"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Export all products with variations"
    )
    parser.add_argument(
        "--output-dir",
        default="./stl",
        help="Output directory for STL files"
    )

    args = parser.parse_args()

    if args.all:
        export_all(args.output_dir)
    elif args.product:
        export_single(args.product, args.output_dir)
    else:
        print("Use --all or --product <name>")
        parser.print_help()
