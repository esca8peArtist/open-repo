---
title: Product Line Expansion Research — ModRun Adjacent Products
project: mfg-farm
created: 2026-05-04
status: active
confidence: high — market data from live Etsy search results, community signals, and existing mfg-farm research base
related: market-research.md, phase-3-product-validation-research.md, pricing-strategy.md, production-scaling-research.md
---

# Product Line Expansion Research

**Lead finding:** Three products stand out as highest-priority additions within six months: a desk headphone hook (fastest path to revenue, 2–3 weeks to first listing, near-identical manufacturing to ModRun clips), a workshop/garage pegboard hook system (higher per-unit revenue, strong community demand, same PLA+ on same printer), and an outdoor garden plant marker set (seasonal demand spike aligns with spring launch timing, low design complexity, opens a new buyer persona). All five candidates evaluated below use the same Bambu P1S printer, the same PLA+ filament, similar print settings to ModRun, and can share packaging. None require support structures when designed correctly.

---

## Context: ModRun Baseline

ModRun cable management clips print in approximately 20–35 minutes per plate of 12–16 units. COGS is $0.08–$0.13/clip. Net margin after Etsy fees (~10.5% effective transaction + payment fee for a typical $12–$25 sale) runs 65–72%. The Bambu P1S with PLA+ is the manufacturing platform. All expansion products are evaluated against this baseline: can they use the same machine, same material, same workflow, and deliver comparable or better margins?

---

## Product 1: Desk Headphone Hook (Under-Desk Clamp)

### What it is / problem it solves

A desk-edge clamp that holds a gaming or studio headset under or to the side of the desk surface, freeing up desktop space. The clamp body grips a desk edge 12–40mm thick via a printed screw mechanism with a silicone or foam pad insert; the hook arm curves to hold the headband of any over-ear headset. Optional integrated cable-wrap post to keep the headphone cable from dragging.

This is a near-exact sibling product to ModRun: same buyer persona (desk setup enthusiast), same distribution channel (Etsy), same material and printer, same form-factor (small clip mechanism). A buyer purchasing a ModRun cable management set is a high-propensity customer for a matching headphone hook.

### Market size

Etsy searches for "headphone hook," "3D printed under desk headphone mount," and "desk clamp headphone hanger" return 300–600 active physical-product listings (distinct from STL file listings). Top sellers show review counts of 200–500+ across multiple shops, signaling consistent sell-through over time. One listing (5DPrintFactory's desk clamp hanger) has 264+ reviews at approximately 4.7 stars. The category is active without being oversaturated — generic hooks have competition, but hooks with a cable-wrap feature, aesthetic matching to desk setups, or multiple color offerings have clear differentiation space.

Price range observed: $12–$22 for single hooks. Sellers offering 30 color variants command the higher end of the range. The sweet spot for a well-photographed listing with color options is $14–$18.

Competitor count in physical-product listings: approximately 200–350 shops. Competition is medium — lower than ModRun's base cable management category (~45K–60K listings), but requiring a clearer aesthetic story to stand out.

### Print complexity

- Print time: 25–45 minutes per hook (single piece or two-part clamp body). The clamp mechanism requires a moveable jaw and a screw post; designed split into two bodies, both print flat with no supports. A cable-wrap post adds a few minutes.
- Filament use: 15–30 grams per hook (clamp body + hook arm + optional cable wrap post)
- Design difficulty: Low-medium. The clamp geometry is parametric — input desk thickness range (12mm–40mm), arm length, and hook curve radius. CadQuery handles this cleanly. One design file, variable output. No supports needed if the clamp jaw is split along the flat mating face.
- Can it be parametric like ModRun? Yes. Desk thickness range, hook arm length, and cable-wrap post presence are all CadQuery parameters. One code file generates 3–4 SKU variants.

### Margin analysis

| Item | Value |
|---|---|
| Filament cost (25g PLA+ @ $0.013/g) | $0.33 |
| Packaging (poly mailer + tissue) | $0.80 |
| Etsy fees on $16 sale (~16.8%) | $2.69 |
| Total COGS + fees | $3.82 |
| Sell price | $16.00 |
| Net margin | ~76% |

At $14 (lower bound): net ~72%. At $18 (premium with cable wrap): net ~78%. These are ModRun-tier or better margins because the hook uses marginally more material than a clip but commands a higher sell price.

### Synergy with ModRun

- Same PLA+ material, same Bambu P1S, same 0.20mm layer height, same 20–25% infill. Zero new tooling or settings.
- Designed in the same aesthetic language as ModRun (clean angles, parametric fit) — photographs well as a "matching set."
- Shared packaging: same poly mailer size as ModRun clips.
- Cross-sell: include a business card in ModRun orders pointing to the headphone hook listing. Etsy's "complete your setup" narrative is effective for this buyer.
- Combined bundle listing ("Cable Management + Headphone Hook Desk Bundle") increases AOV from ~$16 to ~$28–$32 with one combined shipping cost.

### Time to market

- Week 1–2: CadQuery design, tolerance test print, refinement
- Week 2–3: Photography, Etsy listing copy, color variants sliced
- **First listing live: 3 weeks from decision**

---

## Product 2: Pegboard Hook System (Workshop/Garage)

### What it is / problem it solves

A set of 3D-printed hooks and accessory brackets designed to fit standard 1/4" pegboard (the kind found in most garages and workshops) and/or IKEA SKADIS pegboard. Variants include J-hooks in 3 sizes (small for screwdrivers/markers, medium for hand tools, large for cords/cables), a bin bracket for small parts containers, and a tool-specific holder for cordless drill batteries (a high-search-volume specific niche). The value proposition is color coding (organize by tool type), custom labeling text embedded in the hook face, and higher weight tolerance than standard stamped metal hooks for overloaded applications.

Garage and workshop organization is a large, stable Etsy category with strong male buyer demographics — a different persona than ModRun's desk-setup buyer, which diversifies revenue risk.

### Market size

Etsy searches for "3D printed pegboard hooks," "3d printed peg board hooks," and "pegboard accessories 3D printing" return 400–800 active physical-product listings. The IKEA SKADIS-specific niche is active with 100–200 listings and strong review velocity; top SKADIS hook sets show 150–300+ reviews. Tool-brand-specific hooks (Milwaukee M12 battery holder, Dewalt battery charger bracket) are a high-intent sub-niche with 50–150 listings each.

Price range: $8–$22 for hook sets (5–10 hooks). Individual specialty holders (drill holder, battery charger bracket): $12–$28. A full starter pack of 20 mixed-size hooks sells for $28–$45. Price range is wider than headphone hooks, with high-end sets commanding real money for tool-specific designs.

Competitor count: 300–500 physical-product shops. Medium-high for generic hooks; medium-low for tool-brand-specific holders and SKADIS-specific premium sets.

**Important note on Etsy compliance:** All designs must be original — do not adapt the IKEA SKADIS connector geometry without designing an original interface. The standard 1/4" pegboard hole pitch (1" center-to-center) is an open standard, fully safe. SKADIS connector geometry is an IKEA-defined form; create an original push-fit connector that functions equivalently but is a distinct original design.

### Print complexity

- Print time: 8–20 minutes per hook (J-hooks are small, fast). A plate of 20 small J-hooks prints in ~90 minutes total — roughly 4.5 min/hook effective time. Specialty holders (drill battery bracket) are larger and run 35–60 minutes each.
- Filament use: 5–20 grams per hook depending on size. A full starter set of 20 hooks uses 150–250g total.
- Design difficulty: Low. J-hooks are simple extruded shapes. A parametric CadQuery approach generates all sizes from a single hook height, peg pitch, and hook depth parameter. Embossed label text on the hook face is a minor addition that adds perceived value.
- Supports needed: None if hooks are oriented hook-tip-up on the print bed. The hook curve is the only overhang and it typically stays within 45 degrees for J-hook geometry.

### Margin analysis

| Item | Starter Set (20 hooks, ~200g) | Single J-hook (5g) |
|---|---|---|
| Filament cost | $2.60 | $0.065 |
| Packaging | $1.20 (box) | $0.80 (mailer) |
| Etsy fees on $32 / $9 sale | $5.38 / $1.51 | - |
| Total | $9.18 | - |
| Net margin | ~71% | ~81% |

Sell single hooks at $8–$10 each or $28–$40 for a 20-pack starter set. The set pricing is 2–3x the price of a single hook sold individually — Etsy buyers respond well to set framing because it solves the "how many do I need" friction point.

### Synergy with ModRun

- Same PLA+ material, same printer settings. The main difference from ModRun is orientation on the plate (hook-tip-up vs. flat), but no new slicer configuration required.
- Pegboard hooks share the "organization" theme with ModRun but serve a different room (garage vs. desk). This deliberately diversifies the buyer base — the ModRun buyer is office/gaming-focused; the pegboard buyer is workshop/maker-focused.
- Shared packaging: small hooks ship in a poly mailer identical to ModRun clips. Starter sets need a small cardboard box (already in the existing packaging budget for rails).
- Design time synergy: The same CadQuery workflow used for ModRun clips applies directly. A single afternoon of design work produces 4–5 hook size variants.

### Time to market

- Week 1: CadQuery design of 3 hook sizes + bin bracket (all simple forms, parametric)
- Week 1–2: Test prints, tolerance check for pegboard hole fit (1/4" peg = 6.35mm — design hole at 6.5mm for easy snap-fit)
- Week 2–3: Photography (use an actual pegboard panel as the photo backdrop — looks professional), Etsy listing copy
- **First listing live: 3–4 weeks from decision**

---

## Product 3: Custom Garden Plant Markers (Outdoor Stakes)

### What it is / problem it solves

A set of outdoor garden stake markers for labeling plants, herbs, vegetables, and seedlings. Each marker is a flag-style or tombstone-style stake with embossed or raised custom text (plant name, or buyer-specified name/emoji/icon). Printed in ASA filament (UV-resistant, weatherproof, the same polymer used in automotive trim) or PETG for moderate outdoor use. Sold in sets of 6, 10, or 20 with buyer-customized names via Etsy personalization at checkout.

Plant markers solve a universal gardener problem — the stakes that come with seed packets are illegible after one season, and the wire-flag options from garden centers feel cheap. A set of custom-colored, weatherproof, named stakes feels like a gift item and photographs beautifully in a garden bed.

### Market size

Etsy searches for "3D printed plant markers," "custom garden labels," and "garden plant stakes" return 2,000–5,000 active listings across all material types (wood, acrylic, 3D printed, terracotta). The 3D-printed subset is 300–600 listings. "Vegetable garden markers" and "herb garden labels" are high-volume searches on Etsy, particularly in the February–May window when gardeners are planning spring planting.

Price range: $3.99 per single marker to $18–$28 for a set of 6–10 custom-labeled stakes. One top seller starts at $3.99 with a 10% multi-item discount. The premium end for a set of 10 custom-named, UV-resistant, bright-colored stakes is $18–$25.

Seasonal demand: This category has a strong spring spike (February–May) and a smaller late-summer spike (August–September for fall planting). Listing in time for the spring window is significant for first-year revenue.

Competitor count in 3D-printed specifically: 300–600 physical listings. Lower than desk accessories. Moderate-low competition for custom personalized variants; moderate competition for generic pre-labeled ("BASIL," "TOMATO") sets.

### Print complexity

- Print time: 8–15 minutes per stake (small flat flag or rounded tombstone shape, 5–8mm thick, 15cm tall). A plate of 20 stakes prints in 90–120 minutes — 4.5–6 min/stake effective time. Very efficient.
- Filament use: 5–12 grams per stake depending on size. A set of 10 stakes uses 60–100g.
- Design difficulty: Low-medium. The stake body is a simple extrusion. Raised text is an emboss operation in CadQuery using a font module. The parametric variable is the text string — customers specify names, the shop operator runs the CadQuery script with each customer's list, and the STLs are generated per order. This is the same workflow established for any ModRun custom variant.
- Supports needed: None for flat-face stake shapes. The pointed ground stake is the only challenging geometry and can be designed with a slight taper that prints cleanly with no support at 45 degrees.
- Material note: Standard PLA+ degrades in UV after 6–12 months outdoors. PETG lasts 2–3 seasons; ASA lasts 5+ years. For outdoor use, ASA is the correct choice. ASA costs ~$22–30/kg vs. $14–18/kg for PLA+ — filament cost increases by ~60% per gram but the stakes use very little material, so per-unit COGS impact is small. Print setting change required: ASA needs an enclosure (the P1S is enclosed — compatible) and 240–250°C nozzle temp. This is a minor setting change, not a workflow overhaul.

### Margin analysis

| Item | Set of 10 custom stakes (ASA, ~80g) |
|---|---|
| Filament cost (80g ASA @ $0.025/g) | $2.00 |
| Packaging (poly mailer + tissue) | $0.80 |
| Etsy fees on $18 sale (~16.8%) | $3.02 |
| Total COGS + fees | $5.82 |
| Sell price | $18.00 |
| Net margin | ~68% |

At $22 (premium large set): net ~72%. The personalization component (customer provides names at checkout) justifies a $4–6 premium over generic pre-labeled sets and virtually eliminates direct price comparison — a shopper can't compare "a set with their specific herbs spelled correctly" to a generic set.

### Synergy with ModRun

- ASA uses a different temperature profile and requires the enclosed P1S — no new hardware. Print settings are a separate Bambu Studio profile, not a separate printer.
- Small footprint on the plate shares space efficiently. Stakes can be batched on the same plate run as other small items.
- Different buyer persona (gardener vs. desk enthusiast) — little cross-sell, but no conflict either. This is intentional: diversification.
- Packaging is identical format (poly mailer for sets up to 20 stakes).
- One risk to monitor: ASA filament sourcing. PLA+ is available from multiple US suppliers at competitive pricing. ASA has fewer domestic options — qualify two suppliers before committing to volume production.

### Time to market

- Week 1: CadQuery design (simple — flag stake shape, emboss text module)
- Week 1: ASA test print, settings calibration for P1S enclosure (1–2 hours of printer tuning)
- Week 2: Photography with sample names in a garden bed setting (strong seasonal aesthetic)
- Week 2–3: Etsy listing with personalization field, set sizes (6, 10, 20)
- **First listing live: 2–3 weeks from decision** — fastest of all five candidates because the design complexity is lowest

---

## Product 4: Monitor Riser / Desk Shelf Legs

### What it is / problem it solves

A set of four parametric riser legs that lift a standard wooden or MDF shelf board (from IKEA, Home Depot, or any lumber yard) to a specified height, converting it into a monitor riser or general desk shelf. The legs have a slot or groove to capture the shelf edge for stability, a rubber foot pad insert at the base (a silicone bumper, ~$0.05/unit sourced in bulk), and optionally a cable pass-through channel cut into the leg body. Sold as a set of 4 legs; buyer supplies their own shelf board from any hardware store.

This solves a real problem: most commercial monitor risers are either too short (4"), too expensive ($40–$80 for aluminum versions), or don't fit non-standard shelf depths. Parametric legs let buyers specify height (8cm, 12cm, 16cm) and shelf thickness (18mm, 25mm) at checkout, and get a set printed to their exact configuration — something no mass-market product can offer.

### Market size

Etsy "3D printed desk riser" and "monitor riser 3D printed" return 800–1,200 active listings, with many sellers offering digital files (STL downloads) and fewer offering pre-printed physical sets. Physical pre-printed monitor riser legs have 100–300 active physical-product listings, significantly less crowded than the file market.

Price range: $18–$45 for a set of 4 legs (physical product). One Etsy seller ("RISE Monitor Stand Legs") lists at prices suggesting ~$25–35 per set. The premium end (cable channel legs + rubber feet) commands $35–$50.

Competitor count for physical pre-printed leg sets: 100–200 shops. Moderate-low competition, especially for parametric height/thickness variants.

### Print complexity

- Print time: 25–45 minutes per leg depending on height. A set of 4 legs at 12cm height: approximately 120–180 minutes total print time (3–4.5 hours for the set, or 30–45 min/leg).
- Filament use: 40–80 grams per leg. A set of 4 legs at 12cm height: 200–320g total filament.
- Design difficulty: Low. A leg is essentially a rectangular column with a shelf-capture groove at the top, cable channel cutout optionally, and rubber foot pocket at the base. CadQuery handles this in under 100 lines of code. Parametric variables: height, shelf_thickness, include_cable_channel.
- Supports needed: None. The shelf groove and foot pocket are through-cuts or blind pockets that print cleanly with no overhangs beyond 45 degrees.
- Print time risk: This is the heaviest product in the expansion set by weight. A set of 4 legs at 300g total is 2.5x the filament of a 20-hook pegboard set. Print time is correspondingly longer. This means lower units per 24-hour cycle compared to clips or stakes.

### Margin analysis

| Item | Set of 4 legs, 12cm, standard (250g PLA+) |
|---|---|
| Filament cost (250g @ $0.013/g) | $3.25 |
| Rubber foot pads (4 × $0.05) | $0.20 |
| Packaging (larger flat-rate mailer or small box) | $1.50 |
| Etsy fees on $32 sale (~16.8%) | $5.38 |
| Total COGS + fees | $10.33 |
| Sell price | $32.00 |
| Net margin | ~68% |

At $38 (premium: cable channel legs): net ~72%. The higher absolute filament cost is offset by the higher sell price. Margins are slightly lower than headphone hooks or plant stakes on a percentage basis, but the absolute dollar net per unit ($22–$28) is higher than any of the smaller products.

### Synergy with ModRun

- Same PLA+ filament, same printer, same settings. The only difference is longer print runs.
- Direct desk-setup buyer overlap with ModRun: the buyer who organizes cables with ModRun is the buyer who wants a riser shelf. High cross-sell potential. Bundle opportunity: "ModRun + Riser Legs starter kit" at $45–$55 increases AOV significantly.
- Packaging: requires a slightly larger shipping box for sets (4 legs stacked). Adds ~$0.70 to packaging cost vs. ModRun clips.
- Design compatibility: the cable channel in the riser leg echoes the cable routing in ModRun rails — coherent visual ecosystem.

### Time to market

- Week 1–2: CadQuery design, test print of one leg variant, tolerance check for shelf slot
- Week 2–3: Print full set (4 legs), photograph on a real desk with a shelf board
- Week 3–4: Etsy listing with personalization for height and shelf thickness
- **First listing live: 3–4 weeks from decision**

---

## Product 5: Magnetic Workshop Bin Labels

### What it is / problem it solves

Small rectangular label tiles (~50mm × 25mm × 4mm thick) with embossed category text, designed with an embedded N52 neodymium magnet pocket in the back, so they snap onto any metal surface — toolbox drawers, magnetic pegboard panels, steel shelving. Sold in sets of 10 or 20 with either pre-labeled common workshop categories ("SCREWS," "DRILL BITS," "ELECTRICAL," "WRENCHES," etc.) or custom text at buyer-specified. The magnet insert is sourced from AliExpress in bulk ($3–5 per 50 magnets — a negligible BOM cost per label).

This is the smallest and simplest product in the expansion set, requires the least design time, and has one of the best margin profiles because the sell price is driven by the magnet feature and custom label value, not by material volume.

### Market size

Etsy searches for "magnetic toolbox labels," "3D printed tool drawer labels," and "workshop bin labels 3D printed" return 200–400 active listings. Multiple sellers show 100+ reviews on this specific product (custom magnetic toolbox labels 10-pack). Top listings include "Custom Magnetic Toolbox Labels, 3D Printed Tool Organizers (10 Pack)" with documented high ratings and reviewer comments noting strong magnet hold and clean embossed lettering.

Price range: $18–$35 for a set of 10 labels. $28–$55 for a set of 20. Custom text (buyer specifies all category names) commands a $5–8 premium over preset-category sets.

Competitor count: 150–300 shops. Lowest competition of all five candidates — the magnetic feature and custom text combination creates a genuine niche that generic plastic label holders and printed-paper label systems don't serve.

### Print complexity

- Print time: 5–10 minutes per label tile. A plate of 30 label tiles (6×5 grid on a 256×256mm bed) prints in approximately 60–90 minutes — 2–3 min/label effective time. This is the most efficient product in this set.
- Filament use: 5–8 grams per label. A set of 10 labels: 50–80g.
- Design difficulty: Low. A flat rectangular tile with a magnet pocket (17mm diameter × 3mm deep, sized for standard 15×3mm N52 discs) and embossed text using a CadQuery text module. Each custom order triggers a script run to generate labeled STLs from customer text input.
- Assembly: press-fit the magnet into the pocket (no glue needed if pocket is sized to 0.1mm undersize of the magnet diameter). This is 5–10 seconds per label — negligible labor.
- Supports needed: None. Flat tile on the bed, text embossing faces up.

### Margin analysis

| Item | Set of 10 labels, custom (60g PLA+ + 10 magnets) |
|---|---|
| Filament cost (60g @ $0.013/g) | $0.78 |
| Magnet cost (10 × $0.08) | $0.80 |
| Packaging (poly mailer) | $0.80 |
| Etsy fees on $22 sale (~16.8%) | $3.70 |
| Total COGS + fees | $6.08 |
| Sell price | $22.00 |
| Net margin | ~72% |

At $28 (set of 20, preset categories): net ~73%. At $32 (custom text, set of 20): net ~76%. The magnet BOM adds only $0.80 to a $22–$32 sale but enables pricing significantly above plain printed label sets (~$10–$14 without magnets). High ROI on the $0.80 magnet investment.

### Synergy with ModRun

- Same PLA+ filament, same printer, same settings (0.20mm, 20% infill, no support).
- Different buyer (workshop/garage owner vs. desk-setup enthusiast), which provides buyer base diversification.
- Production synergy: because labels are tiny and fast-printing, they can fill otherwise-idle plate space alongside other products. A plate of 12 ModRun clips can often accommodate 6–8 label tiles in unused corners of the build volume. Free capacity utilization.
- Magnet sourcing: requires a new BOM component (N52 disc magnets, 15×3mm). Source in bulk (100+ pack) from AliExpress at ~$4–6/100 = $0.04–$0.06/magnet. One order covers ~100–150 sets of 10. This is the only non-filament material cost in the entire expansion set.

### Time to market

- Week 1: CadQuery design (< 2 hours for flat tile + magnet pocket + emboss text)
- Week 1: Test print, magnet fit check, order bulk magnets (AliExpress, 7–14 day delivery)
- Week 2–3: Photography (labels stuck to a real toolbox drawer — visually clear)
- Week 3: Etsy listing while waiting for magnet stock
- **First listing live: 3 weeks; fully stocked: 3–4 weeks (waiting on magnet delivery)**

---

## Recommended Sequencing

**Priority order for maximum return on design and test-print time:**

1. **Garden Plant Markers** — Fastest design, no new tooling, spring seasonal timing is urgent in May 2026. List within 2–3 weeks. Low-complexity ASA profile work on the P1S.

2. **Headphone Hook** — Direct ModRun sibling, same buyer, highest cross-sell value. 3 weeks to listing. Enables bundle pricing immediately.

3. **Magnetic Workshop Bin Labels** — Lowest per-unit print time (2–3 min/label), lowest design time, strong margins. The magnet lead time (2 weeks) is the only delay. Can be designed in parallel with hooks.

4. **Pegboard Hook System** — Moderate design time for 3 hook sizes. Strong per-unit revenue on sets. 3–4 weeks to listing.

5. **Monitor Riser Legs** — Highest absolute dollar net per sale ($22–$28), longest print time per unit, heaviest per-plate filament use. Best added once the four faster products have proven Etsy traction.

All five products can be live within 10–12 weeks from a design-start decision, with the first listings live within 2–3 weeks of that decision.

---

## Shared Infrastructure Advantages

**Filament:** Four of the five products (all except plant markers) run on the same PLA+ filament stock already in use for ModRun. ASA for plant markers is a new material; source a 1kg spool of each major color (terracotta, sage green, white, black) for ~$90 total initial investment.

**Printer settings:** All products use the same 0.20mm layer height, 20–25% infill, 3-wall profile as ModRun clips. Monitor riser legs benefit from 30% infill for structural rigidity; otherwise no deviation required.

**Packaging:** All five products ship in the same poly mailer format used for ModRun clips (except full pegboard hook starter sets and monitor riser leg sets, which need a small flat box for dimensional stability). Packaging inventory does not require significant new SKUs.

**Photography:** All five products photograph well in the same lighting setup used for ModRun. Plant markers need an outdoor garden setting; all desk products share the same desk-setup backdrop.

**Design tool:** CadQuery handles all five products. The text embossing module (for plant markers and bin labels) is a standard CadQuery feature, not a new dependency.

---

## Risks and Mitigations

**ASA filament for plant markers:** ASA is less forgiving than PLA+ in print settings (needs enclosure heat, higher temps, slower first layer). The P1S's enclosure makes it compatible, but calibration prints are required. Budget one afternoon for ASA profile setup before committing to production.

**Magnet sourcing lead time:** N52 magnets from AliExpress take 7–21 days. Order early; list the bin labels on Etsy with a "ships in 2–3 weeks" processing time initially, then reduce once stock arrives.

**Etsy original design requirement:** All five products must be original designs. The headphone hook clamp mechanism, pegboard hook connector, stake shape, and bin label design must not adapt existing Printables/MakerWorld geometry. The CadQuery-from-scratch workflow establishes provenance — design files are timestamped in git, confirming original authorship.

**Pegboard design originality:** The 1/4" pegboard hole pitch is an open standard. The hook geometry must be original, not adapted from any existing design. A simple J-hook extruded in CadQuery is unambiguously original.

**Monitor riser print time:** At 200–320g per set, this product ties up the printer for 3–4.5 hours per order. At 20+ orders/week, the printer is saturated on riser legs alone — this is a capacity constraint. Address by batching (one overnight run produces 2 sets) and pricing to compensate for print time.

---

## Sources

- [Etsy 3D print cable organizer market page](https://www.etsy.com/market/3d_print_cable_organizer) — listing count and price range verification
- [Etsy 3D printed desk hook market page](https://www.etsy.com/market/3d_printed_desk_hook) — headphone hook category
- [Desk Clamp Headphone Hanger, 5DPrintFactory Etsy listing](https://etsy.com/listing/856089072/headphone-hanger-studio-monitor-holder) — competitor review count
- [3D Printed Headphone Hook Desk Clamp — 264 reviews listing](https://www.etsy.com/listing/1647983070/3d-printed-headphone-hook-desk-clamp) — competitor price and review data
- [Etsy pegboard accessories 3D printing market](https://www.etsy.com/market/pegboard_accessories_3d_printing) — category breadth
- [IKEA Skadis pegboard hooks Etsy — Tough Hooks listing](https://www.etsy.com/listing/1421873959/tough-hooks-for-ikea-skadis-heavy-duty) — product format and pricing
- [Pegboard hook for power tool battery chargers Etsy](https://www.etsy.com/listing/1063700975/pegboard-hook-for-power-tool-battery) — tool-specific niche pricing
- [3D printed plant markers set of 6 Etsy](https://www.etsy.com/listing/991511823/3d-printed-plant-markers-set-of-6-custom) — category existence and format
- [Custom garden markers Etsy listing](https://www.etsy.com/listing/4299400767/custom-garden-markers-3d-printed-icon) — personalization at checkout model
- [3D printed garden marker signs — PETG weatherproof](https://www.etsy.com/listing/4295703515/3d-printed-garden-marker-signs) — material differentiation
- [Custom magnetic toolbox labels 10-pack Etsy](https://www.etsy.com/listing/4302747188/custom-magnetic-toolbox-labels-3d) — bin label product format and pricing
- [Magnetic toolbox labels Etsy](https://www.etsy.com/listing/4316143500/magnetic-toolbox-labels-custom-3d) — magnetic feature validation
- [RISE Monitor Stand Legs Etsy physical print listing](https://www.etsy.com/listing/1812017583/rise-monitor-stand-legs-3d-printed) — monitor riser legs format
- [3D Printed Monitor Riser With Drawers Etsy](https://www.etsy.com/listing/4349478823/3d-printed-monitor-riser-with-drawers) — category pricing
- [Desk accessories market size $12.19B — ReportPrime](https://www.reportprime.com/desk-accessories-r12385) — market context
- [mfg-farm market-research.md](market-research.md) — cable management margin baseline and Etsy fee structure
- [mfg-farm phase-3-product-validation-research.md](phase-3-product-validation-research.md) — competitive benchmarking, WTP analysis, community intelligence
- [mfg-farm pricing-strategy.md](pricing-strategy.md) — ModRun COGS baseline and Etsy competitor data
- [mfg-farm production-scaling-research.md](production-scaling-research.md) — print time, batch utilization, plate saturation data

---

*Confidence note: Etsy listing counts and price ranges are estimated from search result analysis (April–May 2026). Exact sales volumes for competitor listings are not publicly visible — review counts are used as a proxy for sell-through velocity. Margin calculations use the mfg-farm-established PLA+ cost basis of $0.013/g and Etsy effective fee rate of ~16.8% on a $16–$32 sale. ASA cost basis estimated at $0.025/g from market research appendix. All figures should be validated against actual Etsy listing prices at time of product launch.*
