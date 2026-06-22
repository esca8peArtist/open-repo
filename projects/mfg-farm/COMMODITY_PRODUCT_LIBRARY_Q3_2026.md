---
title: Commodity Product Library — Q3 2026 (20+ SKUs)
project: mfg-farm
created: 2026-06-22
status: reference
scope: Full unit economics for 20+ commodity SKUs across five categories; design-readiness status; Etsy market price validation
related:
  - BATCH_3_5_PRODUCT_SELECTION_DEMAND_RESEARCH.md
  - ITEM24_ALTERNATIVE_PRODUCT_CATEGORIES.md
  - pricing-strategy.md
  - cost-model-spreadsheet.csv
  - PRODUCTION_FARM_SCALING_STRATEGY.md
---

# Commodity Product Library — Q3 2026

**Purpose**: Single-reference table of 20+ listable commodity SKUs with full unit economics. Use this to fill printer capacity, diversify Etsy search entry points, and build toward a 30+ listing store. Updated: June 22, 2026.

---

## Cost Assumptions (Consistent Across All SKUs)

| Component | Rate | Notes |
|---|---|---|
| PLA+ filament | $0.022/g | US domestic (Polar Filament PLA $18.99/kg → approx $0.019/g; use $0.022/g with 15% scrap buffer) |
| PETG filament | $0.030/g | MatterHackers MH Build PETG $20.99/kg → $0.021/g; use $0.030/g with scrap + moisture loss |
| Machine time | $0.28/hr | $399 P1S over 5,000-hr life ($0.08 depreciation) + electricity $0.17/kWh at 150W avg ($0.026/hr) + wear parts amortized; rounds to $0.28/hr |
| Packaging | $0.35/unit | Poly mailer ($0.12), tissue paper ($0.05), label ($0.03), thank-you insert ($0.08), tape ($0.07) |
| Etsy listing fee | $0.20/transaction | Fixed per sale |
| Etsy transaction fee | 6.5% of sale price | Applied to gross sale price |
| Etsy payment processing | 3.0% of sale price | Applied to gross sale price |
| Combined Etsy take | ~9.5% + $0.20 | Used in net margin calculations below |

**Net margin formula**: (Sale Price − Material Cost − Machine Cost − Packaging − $0.20 − 9.5% × Sale Price) / Sale Price

**Design-ready definition**: An STL file is freely available on Printables, MakerWorld, or Thingiverse under a non-commercial or Creative Commons license that permits selling printed copies, OR the SKU uses the existing ModRun/headphone hook CadQuery source. These can be listed immediately. SKUs marked "Needs Design" require new CadQuery or parametric CAD work estimated at 2–6 hours each.

---

## Category 1: Cable Management (6 SKUs)

Market context: The Etsy cable management category had 200–350 active physical-product sellers as of April–June 2026 (down from 800+ pre-policy-purge). Prices cluster: economy $5–12, standard $12–22, modular $18–35. ModRun occupies the $12–18 standard band. These commodity SKUs extend into adjacent sub-niches.

| # | Product Name | Material | Print Weight (g) | Print Time (hrs) | Material Cost | Machine Cost | Packaging | Subtotal COGS | Etsy Price | Etsy Fees | Net Margin | Net % | Design Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C-01 | ModRun Cable Clip 3-pack (3mm/6mm/12mm) | PLA+ | 14g | 0.55 | $0.31 | $0.15 | $0.35 | $0.81 | $12.99 | $1.43 | $10.75 | 82.8% | **Design-Ready** (existing) |
| C-02 | Under-Desk Cable Management Tray (no-drill clamp) | PETG | 120g | 3.2 | $3.60 | $0.90 | $0.35 | $4.85 | $24.99 | $2.57 | $17.57 | 70.3% | **Design-Ready** (Printables — multiple CC-licensed designs) |
| C-03 | Wall-Mount Cable Channel (180mm, adhesive backer) | PLA+ | 45g | 1.1 | $0.99 | $0.31 | $0.35 | $1.65 | $11.99 | $1.34 | $9.00 | 75.1% | **Design-Ready** (Printables, various CC0 designs) |
| C-04 | Under-Desk Power Strip Holder (PETG, clamp-on) | PETG | 95g | 2.5 | $2.85 | $0.70 | $0.35 | $3.90 | $19.99 | $2.10 | $13.99 | 70.0% | **Design-Ready** (Printables — Shix design, CC-BY) |
| C-05 | Monitor Cable Spine / Sleeve Bracket (2-piece, desk-clamp) | PLA+ | 30g | 0.75 | $0.66 | $0.21 | $0.35 | $1.22 | $9.99 | $1.15 | $7.62 | 76.3% | **Design-Ready** (Printables CC0) |
| C-06 | Cable Tie / Velcro Holder Wall Mount (3-pack) | PLA+ | 18g | 0.45 | $0.40 | $0.13 | $0.35 | $0.88 | $8.99 | $1.05 | $6.86 | 76.3% | **Design-Ready** (Printables, multiple options) |

**Category notes**:
- C-01 is the existing ModRun clip — listed first as the proven anchor.
- C-04 PETG is mandatory; power strip holders sit near heat sources.
- C-02 and C-04 are the highest-margin-absolute products in this category ($13–17 net per unit). Prioritize these when the second P1S is online and can dedicate a plate to longer-run parts.
- C-03 and C-06 are fast-print volume fillers (under 1 hour). Batch 8–12 units per plate.

---

## Category 2: Desk Organization (5 SKUs)

Market context: Desk organization is a well-developed Etsy category. Differentiation comes from aesthetic coherence (designs that match an existing product line aesthetic like ModRun) and material quality. Price range: $9–$28 for individual items; $25–$50 for multi-piece sets. Competitive reviews average 4.7–4.9 stars.

| # | Product Name | Material | Print Weight (g) | Print Time (hrs) | Material Cost | Machine Cost | Packaging | Subtotal COGS | Etsy Price | Etsy Fees | Net Margin | Net % | Design Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D-01 | Monitor Riser Legs (flat-pack 4-leg set, 200mm height) | PLA+ | 280g | 4.5 | $6.16 | $1.26 | $0.35 | $7.77 | $28.99 | $2.95 | $18.27 | 63.0% | **Needs Design** (parametric, CadQuery, ~4 hrs) |
| D-02 | Under-Desk Headphone Hanger (desk-clamp, cable wrap post) | PLA+ | 38g | 1.0 | $0.84 | $0.28 | $0.35 | $1.47 | $14.99 | $1.62 | $11.90 | 79.4% | **Design-Ready** (existing headphone hook design) |
| D-03 | Pen / Pencil Organizer (2-compartment, 90mm tall) | PLA+ | 65g | 1.4 | $1.43 | $0.39 | $0.35 | $2.17 | $12.99 | $1.43 | $9.39 | 72.3% | **Design-Ready** (Printables, many CC0 options) |
| D-04 | Sticky Note Holder (single pad, angled base) | PLA+ | 28g | 0.6 | $0.62 | $0.17 | $0.35 | $1.14 | $8.99 | $1.05 | $6.60 | 73.4% | **Design-Ready** (Printables CC0) |
| D-05 | Business Card Holder (double-fan display, 50-card capacity) | PLA+ | 35g | 0.8 | $0.77 | $0.22 | $0.35 | $1.34 | $10.99 | $1.24 | $8.41 | 76.5% | **Design-Ready** (Printables, multiple options) |

**Category notes**:
- D-01 (monitor riser) has the highest absolute margin ($18.27/unit) but requires new CadQuery design. Print weight is high; batch 2 sets per plate max on P1S.
- D-02 is the headphone hook product already in the launch sequence — include here for completeness. IMMEDIATE launch candidate.
- D-03 through D-05 are sub-1.5-hour prints, ideal for overnight batch plates (10–14 units per P1S plate).
- Bundle opportunity: D-03 + D-04 + D-05 "Desk Starter Set" at $27.99 captures bundle search traffic; COGS ~$4.65, margin ~$19.37 (69%).

---

## Category 3: Workshop / Gridfinity (5 SKUs)

Market context (from ITEM24 research, May 2026): The Gridfinity open-source ecosystem has a large install base of makers who do not own printers. Pre-printed Gridfinity bins on Etsy sell at $6–15 per bin for standard sizes, $18–35 for kits of 4–8 pieces. The Milwaukee Packout-compatible listings (brand-specific) sell at $12–22 per piece with 100–200+ reviews. No active Gridfinity seller has more than 400–500 reviews, indicating the category is not yet saturated. Gridfinity uses 42mm grid pitch, 7mm base height, 4.8mm magnet pockets — all dimensions are fixed in the open standard.

| # | Product Name | Material | Print Weight (g) | Print Time (hrs) | Material Cost | Machine Cost | Packaging | Subtotal COGS | Etsy Price | Etsy Fees | Net Margin | Net % | Design Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| G-01 | Gridfinity 1×1 Standard Bin (42mm, 46mm tall, single) | PETG | 28g | 0.75 | $0.84 | $0.21 | $0.35 | $1.40 | $7.99 | $0.96 | $5.63 | 70.5% | **Design-Ready** (Printables — Zack Freedman CC-BY-NC, pre-printed sales allowed) |
| G-02 | Gridfinity 2×2 Deep Bin (84mm, 74mm tall, single) | PETG | 95g | 2.1 | $2.85 | $0.59 | $0.35 | $3.79 | $14.99 | $1.62 | $9.58 | 63.9% | **Design-Ready** (same Gridfinity standard files) |
| G-03 | Gridfinity 1×2 Screwdriver Insert (6-slot, 46mm tall) | PETG | 65g | 1.5 | $1.95 | $0.42 | $0.35 | $2.72 | $13.99 | $1.53 | $9.74 | 69.6% | **Design-Ready** (MakerWorld — multiple CC-licensed screwdriver inserts) |
| G-04 | French Cleat Tool Holder Blade (customizable, 150mm) | PETG | 55g | 1.3 | $1.65 | $0.36 | $0.35 | $2.36 | $11.99 | $1.34 | $8.29 | 69.1% | **Needs Design** (CadQuery parametric, ~3 hrs — parametric width makes this sellable at multiple sizes) |
| G-05 | Pegboard Hook Set (5mm + 10mm, 6-piece mix pack) | PETG | 42g total | 1.1 | $1.26 | $0.31 | $0.35 | $1.92 | $10.99 | $1.24 | $7.83 | 71.2% | **Design-Ready** (Printables CC0 — many peg hook designs) |

**Category notes**:
- G-01 at $5.63 net margin seems low in isolation. Sell in 2-packs at $13.99 (COGS $3.15, net $9.64 = 68.9%) or 4-packs at $22.99 (COGS $5.95, net $15.39 = 66.9%) to improve absolute margin per transaction. The $0.20 listing fee costs less per unit at higher quantities.
- G-02 fills the "deep storage" need. Batch 3 per plate (horizontal orientation, no supports needed for Gridfinity bins).
- G-03 is the highest-priority new Gridfinity SKU for a workbench user — screwdrivers are the tool category with the highest search volume on Etsy for "gridfinity insert."
- G-04: French cleat blades are a high-velocity workshop category independent of Gridfinity. Use PETG for strength. Parametric width (100mm / 150mm / 200mm) creates multiple SKU variants from one design.
- Gridfinity license note: Zack Freedman's original Gridfinity design is CC-BY-NC. "Non-commercial" is the restriction. Multiple interpretations exist in the community — the safest approach is to create your own Gridfinity-compatible designs in CadQuery using the published specification dimensions (which are freely documented), not to print and sell Freedman's original STL files directly.

---

## Category 4: Home / Garden (3 SKUs)

| # | Product Name | Material | Print Weight (g) | Print Time (hrs) | Material Cost | Machine Cost | Packaging | Subtotal COGS | Etsy Price | Etsy Fees | Net Margin | Net % | Design Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| H-01 | Self-Watering Planter Insert (succulent size, 80mm pot) | PLA+ | 40g | 1.1 | $0.88 | $0.31 | $0.35 | $1.54 | $9.99 | $1.15 | $7.10 | 71.1% | **Design-Ready** (Printables CC0 — multiple planter insert designs) |
| H-02 | Phone / Tablet Wall Mount (articulating arm, drywall anchor) | PLA+ | 55g | 1.4 | $1.21 | $0.39 | $0.35 | $1.95 | $12.99 | $1.43 | $9.61 | 74.0% | **Design-Ready** (Printables, various CC options; pick non-brand-specific design) |
| H-03 | Key Hook Wall Organizer (5-hook bar, 200mm, keyhole mount) | PLA+ | 60g | 1.3 | $1.32 | $0.36 | $0.35 | $2.03 | $11.99 | $1.34 | $8.62 | 71.9% | **Design-Ready** (Printables CC0) |

**Category notes**:
- H-01: Self-watering inserts solve a real problem (succulent/cactus overwatering). Print in white PLA+ for broad appeal. Sell in 2-packs at $15.99 for better margin optics ($11.11 net, 69.5%).
- H-02: Phone/tablet mounts are a crowded category — differentiate with adjustable arm or minimalist aesthetic. Avoid brand-specific designs (MagSafe, iPad-specific) to reduce IP risk.
- H-03: Key hooks are simple, high-margin, fast-print. Excellent for batch production. List in black PLA+ (most popular) with color options at +$1.00.

---

## Category 5: Seasonal / Q4 (4 SKUs)

These are fully documented in `Q4_2026_SEASONAL_SKU_ROADMAP.md`. Summary unit economics here for cross-reference.

| # | Product Name | Material | Print Weight (g) | Print Time (hrs) | Material Cost | Machine Cost | Packaging | Subtotal COGS | Etsy Price | Etsy Fees | Net Margin | Net % | Design Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| S-01 | Stackable Ornament Base Set (4-pack, 60mm diameter) | PLA+ | 88g total | 2.2 | $1.94 | $0.62 | $0.35 | $2.91 | $18.99 | $2.01 | $14.07 | 74.1% | **Design-Ready** (Printables — sphere/bell ornament bases CC0) |
| S-02 | Personalized Cable Clip 4-pack (initials embossed) | PLA+ | 28g total | 0.7 | $0.62 | $0.20 | $0.35 | $1.17 | $14.99 | $1.62 | $12.20 | 81.4% | **Needs Design** (CadQuery emboss text on existing clip, ~2 hrs) |
| S-03 | Holiday Countdown Block Display Base (numbered 1–25 set) | PLA+ | 210g total | 5.5 | $4.62 | $1.54 | $0.35 | $6.51 | $34.99 | $3.52 | $24.96 | 71.3% | **Needs Design** (Tinkercad or CadQuery, ~3 hrs for parametric number font) |
| S-04 | Desk Name Plate (block letter base, 3 initials, 150mm) | PLA+ | 50g | 1.2 | $1.10 | $0.34 | $0.35 | $1.79 | $14.99 | $1.62 | $11.58 | 77.3% | **Needs Design** (CadQuery text extrusion, ~2 hrs; parametric = infinite variants) |

---

## Design-Readiness Summary

### Design-Ready Now (13 SKUs — can list immediately)

These use existing CadQuery source (ModRun/headphone hook) or freely licensed Printables/MakerWorld files that permit sale of printed copies.

| SKU | Product |
|---|---|
| C-01 | ModRun Cable Clip 3-pack |
| C-02 | Under-Desk Cable Management Tray |
| C-03 | Wall-Mount Cable Channel |
| C-04 | Under-Desk Power Strip Holder |
| C-05 | Monitor Cable Spine Bracket |
| C-06 | Cable Tie Holder Wall Mount |
| D-02 | Under-Desk Headphone Hanger |
| D-03 | Pen / Pencil Organizer |
| D-04 | Sticky Note Holder |
| D-05 | Business Card Holder |
| G-01 | Gridfinity 1×1 Bin |
| G-02 | Gridfinity 2×2 Deep Bin |
| G-03 | Gridfinity 1×2 Screwdriver Insert |
| G-05 | Pegboard Hook Set |
| H-01 | Self-Watering Planter Insert |
| H-02 | Phone / Tablet Wall Mount |
| H-03 | Key Hook Wall Organizer |
| S-01 | Stackable Ornament Base Set |

### Needs Design Work (6 SKUs — prioritized below by effort and revenue potential)

| SKU | Product | Design Tool | Estimated Hours | Priority |
|---|---|---|---|---|
| D-01 | Monitor Riser Legs | CadQuery (parametric leg profile) | 4 hrs | High — highest absolute margin in category |
| G-04 | French Cleat Tool Holder | CadQuery | 3 hrs | High — high search volume, no dominant FDM seller |
| S-02 | Personalized Cable Clip 4-pack | CadQuery (add text emboss to existing clip) | 2 hrs | High — trivial extension of existing work |
| S-04 | Desk Name Plate | CadQuery (text extrusion) | 2 hrs | Medium — good Q4 gifting item |
| S-03 | Holiday Countdown Block Display | Tinkercad or CadQuery | 3 hrs | Medium — high price point but high print time |
| F-04 | French Cleat (wide variant) | CadQuery parametric | 1 hr extra | Low — extend G-04 once designed |

**Total design hours needed to complete all 6**: approximately 15 hours across 2–3 sessions.

---

## Library-Level Economics Summary

At full-library listing (all 23 SKUs live with 2 units/week average sell-through per SKU), the blended commodity portfolio generates:

| Metric | Value |
|---|---|
| Active Etsy listings | 23 |
| Avg units/week across all SKUs | ~46 units/week |
| Avg net margin per unit | ~72% |
| Avg sale price (blended) | ~$14.50 |
| Weekly gross revenue | ~$667 |
| Weekly net revenue (after fees) | ~$480 |
| Monthly net revenue (commodity tier only) | ~$1,920 |

These are conservative at 2 units/week per SKU. The top 20% of listings (cable clips, headphone hooks, Gridfinity) will likely generate 5–10 units/week once reviews accumulate, pulling the actual monthly figure to $2,500–$3,500 for commodity tier alone at single-printer capacity.

---

## Sources and Market Research Basis

- Etsy cable management category research: April–June 2026 (pricing-strategy.md, BATCH_3_5_PRODUCT_SELECTION_DEMAND_RESEARCH.md)
- Gridfinity market data: ITEM24 research, May 2026; validated against current Etsy search results June 2026
- Filament pricing: MatterHackers ($20.99/kg PETG), Polar Filament ($18.99/kg PLA), ITEM24 supplier section
- Gridfinity open standard specification: [Zack Freedman's GitHub repository](https://github.com/zackfreedman/gridfinity)
- Etsy search results validation: June 2026 searches for "gridfinity bins," "cable management desk," "headphone hook"
- TouchTerrain (premium tier tool, referenced for context): [touchterrain.geol.iastate.edu](https://touchterrain.geol.iastate.edu/)
