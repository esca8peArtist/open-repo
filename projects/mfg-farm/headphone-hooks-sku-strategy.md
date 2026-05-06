---
title: Headphone Hooks — SKU Strategy & Variants
project: mfg-farm
created: 2026-05-06
status: active
related: headphone-hooks-cost-model.md, headphone-hooks-etsy-listing.md, product-line-strategy.md
---

# Headphone Hooks — SKU Strategy & Variants

**Lead finding:** The core SKU architecture is five listings (3 desk-thickness variants + dual-hook premium + bundle 3-pack) across a $9.99–$34.99 price ladder. This maximizes average order value (AOV) without complicating production — all variants print from the same `headphone_hooks.py` script with different parameters. The bundle SKU drives the highest absolute net per order at $29.70 on a 3-pack.

---

## 1. SKU Architecture Overview

| SKU ID | Description | Print File | Sell Price | COGS | Net Margin |
|---|---|---|---|---|---|
| HH-S | Standard hook, 25mm desk (most common) | headphone_hook_25mm_with_post.stl | $12.99 | $3.13 | 75.9% |
| HH-THIN | Thin desk hook, 12mm | headphone_hook_12mm_with_post.stl | $12.99 | $3.08 | 76.3% |
| HH-THICK | Thick desk hook, 40mm | headphone_hook_40mm_with_post.stl | $12.99 | $3.18 | 75.5% |
| HH-DUAL | Dual-hook stereo variant, 25mm | headphone_hook_dual_25mm.stl (Month 2) | $19.99 | $4.50 | 77.5% |
| HH-WALL | Wall-mount variant, no clamp | headphone_hook_wall.stl (Month 2) | $9.99 | $2.80 | 72.0% |
| HH-3PK | Bundle: 3× standard hook (any thickness) | 3× single hook files | $32.99 | $7.50 | 77.3% |

**Note:** Dual-hook and wall-mount STLs require ~2–3 additional hours of CadQuery design work each. These are Month 2 additions. Launch with HH-S, HH-THIN, HH-THICK, and HH-3PK in Month 1.

---

## 2. Desk-Thickness Variant Logic

### Why three sizes instead of one adjustable design
Competitor designs using screw-adjustment have consistent negative feedback about installation complexity ("had to find a screwdriver," "strip risk," "awkward to tighten one-handed"). A friction-fit clamp sized exactly for the desk thickness installs in seconds with no tools.

The three sizes cover the overwhelming majority of desk surfaces:
- **12mm (HH-THIN):** IKEA KALLAX shelves used as desk tops, thin plywood panels, shelf desks
- **25mm (HH-S, standard):** IKEA LINNMON (25mm), IKEA BEKANT (23mm), most 1-inch particleboard desk tops — this is >60% of the buyer market
- **40mm (HH-THICK):** Solid wood tops, standing desk bamboo surfaces, butcher-block worktops

### At-checkout variant selection
Etsy personalization field (at listing level, not separate SKU): "Select desk thickness: 12mm / 25mm / 40mm — if unsure, 25mm is the most common." Print the selected variant on receipt of each order.

Alternatively, create three separate listings with different primary photos (thin IKEA desk, standard desk, thick butcher block). Three listings increases Etsy search surface area at the cost of slightly more listing management.

**Recommendation for launch:** Single listing with personalization dropdown. If listings don't convert at 3% within 30 days, split into three listings for search exposure.

---

## 3. Dual-Hook Stereo Variant (Month 2)

### Concept
Two hook arms extending from a single, wider clamp body. Designed for users with:
- Two headsets (gaming + office/casual, or gaming + audiophile)
- A headset on one hook and a gaming controller/joystick on the other
- Stereo monitor headphones where both sides hang simultaneously

### Design parameters (to be implemented in CadQuery, Month 2)
- Clamp body width: 70mm (vs. 38mm standard)
- Two hook arms, 40mm apart (center-to-center), same arm geometry as single hook
- Cable posts between and/or flanking the two arms
- Same desk-thickness variant logic (12mm / 25mm / 40mm)

### Pricing rationale
- Print weight: ~45–50g (approximately 2× single hook)
- Filament COGS: ~$0.59–$0.65
- Total COGS: ~$4.50 (slightly less than 2× single due to shared clamp body)
- Sell price: $19.99 — 54% premium over single hook for <2× material cost
- Net margin: ~77.5%

### Marketing angle
"The only desk clamp designed for dual-headset setups. Gaming + studio, wireless + wired — both hang within reach." No current Etsy listing addresses this use case with a physical product.

---

## 4. Wall-Mount Variant (Month 2)

### Concept
The single-hook arm and cable post geometry, mounted to a flat back plate with M3 through-holes or keyhole slots for wall mounting. No clamp jaw. For users with:
- Pegboard setups (hooks into the pegboard pattern)
- Wall-mounted monitor arm post (zip tie or bracket mount)
- Under-cabinet kitchen use (tablet/phone holder extension)

### Design parameters
- Back plate: 40×50mm, 4mm thick
- Four M3 through-holes at 30mm square pattern (standard pegboard spacing)
- Optional keyhole slot for drywall screw (no bolt visible)
- Same hook arm + cable post geometry as standard hook

### Pricing
- Print weight: ~18–20g (lightest SKU — no lower jaw or clamp arms)
- Filament COGS: ~$0.23–$0.26
- Total COGS: ~$2.80
- Sell price: $9.99 (entry-price tier, volume driver)
- Net margin: ~72.0%

### Note
Lower margin than clamp variants due to lower sell price, not higher cost. Consider bundling: "Buy 2 wall-mount hooks, get 1 free." This drives AOV while clearing inventory of the entry SKU.

---

## 5. Bundle SKU: 3-Pack

### Concept
Three standard hooks (any combination of desk thicknesses), bundled at 15% discount from three individual purchases ($12.99 × 3 = $38.97 → $32.99 bundle).

### Target buyer
- Home with multiple desks (home office desk + bedroom gaming setup + kitchen shelf)
- Buys for self + partner
- Gift purchase ("desk setup upgrade gift for gamer")
- Studio/office buyer outfitting multiple workstations

### Economics
| Metric | 3-Pack |
|---|---|
| Sell price | $32.99 |
| Filament × 3 | $0.99 |
| Rubber pads × 6 | $0.15 |
| Packaging (single larger mailer) | $0.15 |
| Labor × 3 | $3.00 |
| Equipment depreciation × 3 | $0.33 |
| Etsy fees | ~$3.37 |
| **Total COGS** | **$8.00** |
| **Net profit per bundle** | **$24.99** |
| **Net margin** | **75.7%** |

**AOV impact:** A 3-pack at $32.99 vs. three singles at $38.97 increases per-order net profit from ~$29.58 (3 × $9.86) to $24.99. The bundle earns $4.59 less net per three-hook event — this is the cost of the 15% discount. However, the bundle drives AOV from $12.99 average to $32.99, which:
1. Improves Etsy algorithm ranking (Etsy rewards higher-AOV listings)
2. Amortizes shipping cost over more units
3. Reduces the number of separate orders to package per equivalent revenue

**Bundle discount can be narrowed to 10% ($35.07) once 50+ reviews accumulate** and price sensitivity is better understood.

---

## 6. Color Strategy

### Standard colors (launch)
Five colors from existing PLA+ inventory. Match ModRun product color options where possible for cross-sell visual consistency.

| Color | Notes | Price Premium |
|---|---|---|
| Matte Black | Default, highest sell-through in desk accessories | None |
| Matte White | Clean desk aesthetic, popular with minimalist setups | None |
| Space Gray | IKEA-compatible neutral, works with white or dark desks | None |
| Deep Blue / Navy | Gaming/homelab aesthetic, r/battlestations demographic | None |
| Terracotta / Burnt Orange | Warm workspace accent, differentiated from competitors | None |

### Premium multi-color (Month 2+)
The Bambu P1S supports AMS multi-color printing. A two-tone hook (e.g., black clamp body + orange/white hook arm accent) is achievable with ≤5-minute slicer setup change.

| Multi-color scheme | Additional print time | Price premium | Net impact |
|---|---|---|---|
| Two-tone body/arm | +2–4 min | +$2.00 | $1.50–$1.80 net after fees |
| Three-color (body/arm/post) | +4–6 min | +$3.00 | $2.40–$2.70 net after fees |

**Recommendation:** Offer two-tone as optional upgrade at +$2.00 at checkout. Add AMS-format options only after the standard product is stable and printing consistently.

### Color selection mechanic
Etsy personalization field: "Color (select one): Matte Black / Matte White / Space Gray / Deep Blue / Terracotta / Other (describe in notes)." "Other" allows Anya to print any color in current inventory — reduces inventory management vs. stocking every color variant as a separate listing.

---

## 7. Pricing Ladder Summary

| SKU | Launch Price | After-Review Price | Rationale |
|---|---|---|---|
| HH-WALL (wall-mount) | $9.99 | $9.99 | Entry, volume driver |
| HH-S / HH-THIN / HH-THICK | $12.99 | $14.99 | Below dominant competitor; raise after 50 reviews |
| HH-DUAL | $19.99 | $21.99 | Premium, no competition |
| HH-3PK | $32.99 | $34.99 | Bundle, AOV driver |

This ladder gives a clean $9.99 / $12.99 / $19.99 / $32.99 entry-to-premium range covering four distinct buyer scenarios: minimal wall mount, standard clamp, premium dual-hook, bulk purchase.

---

## 8. ModRun Cross-Sell SKU

After ModRun cable management listings are live, create a bundle listing: "ModRun Cable Clip Starter Set + Headphone Hook."

| Bundle Contents | Retail Value | Bundle Price | Discount | Net/Bundle |
|---|---|---|---|---|
| ModRun 3-clip set + 1 headphone hook | $24.99 + $12.99 = $37.98 | $32.99 | 13% | ~$25.50 |

This bundle is the primary vehicle for converting ModRun buyers into headphone hook buyers and vice versa. It should be created as a separate Etsy listing in the "Desk Setup" shop section alongside both parent listings.

---

## Sources

- mfg-farm/headphone-hooks-cost-model.md — COGS and margin calculations
- mfg-farm/cost-model-spreadsheet.csv — ModRun COGS baseline for comparison
- mfg-farm/product-line-strategy.md — 76% margin target, desk-thickness variant rationale
- mfg-farm/headphone-hooks-market-analysis.md — competitor price distribution, dual-hook gap identification
- [Etsy AOV and search ranking dynamics](https://www.etsy.com/seller-handbook/) — bundle pricing algorithm interaction
