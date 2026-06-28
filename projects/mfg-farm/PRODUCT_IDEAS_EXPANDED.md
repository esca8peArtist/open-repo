---
title: Expanded Product Ideas — 18 New Candidates Scored and Ranked
project: mfg-farm
created: 2026-06-28
status: decision-ready
confidence: 80%
scope: >
  18 new product ideas beyond the existing commodity library and Wave 2 candidates.
  Each scored using the same 5-criterion framework established in
  PRODUCT_SELECTION_DECISION_MATRIX.md. Top 5 flagged for immediate design consideration.
related:
  - PRODUCT_SELECTION_DECISION_MATRIX.md
  - COMMODITY_PRODUCT_LIBRARY_Q3_2026.md
  - Q3_Q4_PRODUCT_CANDIDATES.md
  - TOPO_MAPS_PRODUCT_RESEARCH.md
---

# Expanded Product Ideas — 18 New Candidates

**Lead finding**: Five products warrant immediate design investment: articulated flexi animals (P-01), lithophane night light panels (P-04), gaming controller stand (P-05), bedside charging dock (P-09), and magnetic wall key hook with neodymium insert (P-13). Three of these (P-01, P-05, P-13) have zero CAD time required — STL files exist under permissive licenses. The two that require new CadQuery work (P-04, P-09) produce the highest margin-per-print-hour of any product on this list.

---

## Scoring Framework

Identical to PRODUCT_SELECTION_DECISION_MATRIX.md. Scores are 1–5 per criterion. Weighted total = decision metric.

| Criterion | Weight | 5 (Best) | 1 (Worst) |
|---|---|---|---|
| **Demand Signal** | 30% | 300+ Etsy listings with 100+ avg reviews; validated Reddit pain points | <20 listings; no Reddit mentions |
| **Margin Potential** | 25% | ≥75% gross margin; COGS <$1.00; short print time | <60% margin; high hardware BOM; long print time |
| **Design Complexity** (inverted: higher = simpler) | 20% | 1-3 hrs CAD or STL already exists; 1 test iteration | 6+ hrs CAD; 3+ iterations; fit-critical mechanism |
| **Supplier Readiness** | 15% | 100% existing supply chain | New material type; new hardware supplier; 2+ week lead time |
| **UGC Opportunity** | 10% | Natural before/after; r/battlestations format; high visual impact | No visual impact; hard to photograph compellingly |

---

## Desk Organization

### P-01 — Articulated Flexi Animal (Dragon / Octopus / Snake)

**Description**: Multi-segment print-in-place articulated animal toy — the "flexi dragon" is the dominant category. Prints as a single STL with no post-print assembly. No hardware, no adhesives. Available in countless CC0 designs on Printables and MakerWorld.

**Etsy demand signal**: Articulated animals are consistently among the highest-selling 3D printed products on Etsy in 2025-2026. Flexi dragons specifically have 500+ active listings with multiple sellers achieving 200-500+ reviews. The category is competitive but not saturated — quality photography and color options differentiate.

**Unit economics**: Print weight ~60-100g (dragon), print time 1.5-2.5 hours, COGS ~$1.50-2.20 (material + packaging), sell price $12-18, net margin ~79-82%.

| Criterion | Score | Justification |
|---|---|---|
| Demand Signal | 5 | Top 3 search category for 3D printed goods on Etsy; "flexi dragon" alone: 500+ listings with 100+ avg reviews; r/3Dprinting and r/gaming regular posts; gifting angle strong |
| Margin Potential | 4 | 79-82% margin; $1.50-2.20 COGS; 1.5-2.5 hr print time; decent but slightly longer than hardware-free cable clips |
| Design Complexity | 5 | No CAD required; print-in-place STL files freely available CC0 on Printables; 1 test print to verify AMS color assignment |
| Supplier Readiness | 5 | PLA+ only; existing supply; AMS enables multi-color without filament swaps |
| UGC Opportunity | 4 | Highly giftable, photogenic, shareable on social; "look what my printer made" content category; not desk-transformation level but strong |
| **Weighted Total** | **4.65** | 5×0.30 + 4×0.25 + 5×0.20 + 5×0.15 + 4×0.10 = 1.50+1.00+1.00+0.75+0.40 |

**Rating: GO — Priority 1 (design sprint: today)**

---

### P-02 — Modular Drawer Dividers (Adjustable-Width Set)

**Description**: Interlocking drawer organizer dividers for kitchen or desk drawers. Multiple width and depth options from a parametric design. No hardware — friction fit against drawer walls.

**Etsy demand signal**: Drawer organizers are a developed market on Etsy. Multiple sellers have 50-150 reviews. Not explosive growth but steady demand. Primary appeal: standard retail organizers don't fit non-standard drawer dimensions.

**Unit economics**: Print weight 80-120g per divider, print time 1.5-2.5 hrs per piece, sell as sets of 4-6 pieces. COGS ~$3.50-5.00 per set, sell price $18-28, net margin ~72-76%.

| Criterion | Score | Justification |
|---|---|---|
| Demand Signal | 3 | 50-120 active Etsy listings; steady but not growing demand; IKEA Skubb and Muji products dominate mass market; 3D printed angle is "fits non-standard drawers" |
| Margin Potential | 4 | 72-76% margin; slightly below cable clips but acceptable; batch-printing 6 pieces per plate is efficient |
| Design Complexity | 3 | Parametric CadQuery design needed — 3-4 hrs for a set with adjustable width, depth, and height parameters; 2 test iterations for fit validation |
| Supplier Readiness | 5 | PLA+ only; no hardware; existing supply |
| UGC Opportunity | 3 | "Before: junk drawer chaos. After: organized" — works but is a well-worn format with many competitors doing it better |
| **Weighted Total** | **3.50** | 3×0.30 + 4×0.25 + 3×0.20 + 5×0.15 + 3×0.10 = 0.90+1.00+0.60+0.75+0.30 |

**Rating: WATCH — Strong supply chain fit but crowded market. Evaluate after Wave 2 launch.**

---

### P-03 — Laptop Stand / Riser (Single-Piece or Folding)

**Description**: Laptop riser in a single-print or fold-flat design that elevates a laptop 80-120mm above desk surface. Work-from-home demand is sustained post-2022.

**Etsy demand signal**: "Laptop stand 3d printed" has 200+ Etsy listings, several with 100+ reviews. However, mass-market aluminum stands from Nexstand and Rain Design dominate at $25-40. The 3D printed angle is "custom height" and "print farm quality" positioning.

**Unit economics**: Large print — 200-280g, 4-7 hours. COGS ~$6-8, sell price $28-38, net margin ~70-74%. Print time is the limiting factor — 4-7 hours per unit competes with topo maps for printer time.

| Criterion | Score | Justification |
|---|---|---|
| Demand Signal | 4 | 200+ Etsy listings; WFH category is sustained; multiple sellers with 100+ reviews; however, strong non-3D competition at the same price point (aluminum stands from Amazon) |
| Margin Potential | 3 | 70-74% margin, $6-8 COGS — acceptable, but high print time (4-7 hrs) reduces per-hour revenue vs. cable clips |
| Design Complexity | 3 | Parametric CadQuery: 3-5 hrs; 2 iterations for stability testing; non-folding variant is simpler (2 hrs) |
| Supplier Readiness | 5 | PLA+ or PETG; no hardware; existing supply |
| UGC Opportunity | 3 | "Raised laptop = better ergonomics" — real but less visual than cable transformation; requires lifestyle context to communicate the benefit |
| **Weighted Total** | **3.45** | 4×0.30 + 3×0.25 + 3×0.20 + 5×0.15 + 3×0.10 = 1.20+0.75+0.60+0.75+0.30 |

**Rating: WATCH — Good demand but print time economics compete with other priorities.**

---

### P-04 — Lithophane Night Light Panel

**Description**: A flat panel with a photographic image embedded as variable wall thickness — when backlit with an LED, the image reveals itself. Buyers provide a photo; you generate the lithophane STL (free tools: itslithophane.com or Cura's built-in lithophane generator) and print it. Frame it in a simple printed PLA border; buyer supplies or you include an LED strip/puck.

**Etsy demand signal**: "3d printed lithophane" has 400+ listings with 4.8+ average reviews and strong personalized-gift positioning. Multiple sellers achieve $40-80 per panel. High emotional resonance — the photo reveal when held to light creates a unique unboxing moment. Reddit gift recommendation threads frequently cite lithophanes.

**Unit economics**: Print weight ~80-120g for a 150×150mm panel at 3mm thickness, print time 2.5-4 hours, COGS ~$2.00-3.00 (material + packaging + optional LED puck $1-2), sell price $35-65, net margin ~85-87%.

| Criterion | Score | Justification |
|---|---|---|
| Demand Signal | 5 | 400+ Etsy listings; high average review scores; strong gifting angle; multiple sellers at $40-65 with 200+ reviews; r/3Dprinting and r/gifts regularly recommend lithophanes |
| Margin Potential | 5 | 85-87% gross margin; COGS $2-3; print time reasonable at 2.5-4 hrs; customization surcharge on top of base product price |
| Design Complexity | 4 | Zero CAD required — free lithophane generators handle STL generation from buyer photo; 1-2 test prints for optimal wall thickness settings; file prep per order: ~15-20 minutes |
| Supplier Readiness | 4 | PLA+ only for panel; if selling with LED: LED puck or strip ($1-2, AliExpress or Amazon); new supplier required but minimal MOQ and low risk |
| UGC Opportunity | 5 | "Photo reveals when held to light" is inherently viral content; before (opaque white panel) and after (glowing photo) is one of the most shareable 3D printed product demonstrations |
| **Weighted Total** | **4.75** | 5×0.30 + 5×0.25 + 4×0.20 + 4×0.15 + 5×0.10 = 1.50+1.25+0.80+0.60+0.50 |

**Rating: GO — Priority 2. Gifting angle, premium margin, zero CAD. Test print one panel this week.**

---

## Gaming and Hobby

### P-05 — Gaming Controller Stand (Generic, Brand-Agnostic)

**Description**: A desktop stand for game controllers. Designed to fit the approximate dimensions of PS5 DualSense, Xbox Series, and Switch Pro Controller without using brand-specific trademarked geometry. Prints in one piece, no hardware. AMS enables color matching to controller color.

**Etsy demand signal**: "Controller stand 3d printed" has 300+ listings. Several sellers have 100-300+ reviews. The brand-agnostic ("fits most controllers") angle avoids IP risk while covering the majority of buyers. Reviews consistently mention: great gift for gamers, looks clean on desk, works as advertised.

**Unit economics**: Print weight ~70-90g, print time 1.5-2.5 hours, COGS ~$1.80-2.50 (material + packaging), sell price $14-22, net margin ~80-83%.

| Criterion | Score | Justification |
|---|---|---|
| Demand Signal | 5 | 300+ listings; several sellers with 200+ reviews; gaming desk accessories are a high-growth Etsy category; "gamer gift" angle strong; r/battlestations features controller stands regularly |
| Margin Potential | 4 | 80-83% margin; $1.80-2.50 COGS; 1.5-2.5 hr print; decent throughput |
| Design Complexity | 5 | CC0 and CC-BY designs widely available on Printables (many "universal controller stand" and "gamepad holder" designs); 1 test print for AMS color assignment |
| Supplier Readiness | 5 | PLA+ only; no hardware; existing supply; AMS multi-color is a differentiation lever |
| UGC Opportunity | 4 | Gaming setup transformation; "cluttered gaming desk → organized with controller on stand" is a well-established format on r/battlestations; not as high-impact as cable transformation but above average |
| **Weighted Total** | **4.65** | 5×0.30 + 4×0.25 + 5×0.20 + 5×0.15 + 4×0.10 = 1.50+1.00+1.00+0.75+0.40 |

**Rating: GO — Priority 3. Zero CAD. List alongside flexi dragon for gaming audience crossover.**

---

### P-06 — Dice Tray (Tabletop Gaming, Hexagonal or Rectangular)

**Description**: A shallow tray for rolling dice in tabletop RPG (D&D) and board game settings. Prevents dice from rolling off the table. Hexagonal shape is the category-dominant aesthetic. Felt liner is optional (adhesive felt sheet: $1.50 per set of cut pieces).

**Etsy demand signal**: "Dice tray" has 500+ listings. Well-established market. Top sellers have 300-1000+ reviews. Felt-lined versions command $18-35. Unlined versions $12-20. Competition is significant; differentiation comes from shape variety, color options, and modular stacking (dice tray + dice tower combo).

**Unit economics**: Print weight ~100-150g, print time 2-3 hours, COGS ~$2.80-4.20 (material + packaging + optional felt liner $1.50), sell price $18-28, net margin ~74-79%.

| Criterion | Score | Justification |
|---|---|---|
| Demand Signal | 5 | 500+ listings; top sellers have 300-1000+ reviews; established tabletop gaming market; TTRPG community (D&D) has grown significantly; strong gift segment |
| Margin Potential | 4 | 74-79% margin; COGS $2.80-4.20 with felt liner; 2-3 hr print; acceptable per-hour revenue |
| Design Complexity | 4 | CC0 designs abundantly available on Printables and MakerWorld; hexagonal shape is a 30-minute CadQuery exercise if you want your own design; 1 test print |
| Supplier Readiness | 4 | PLA+ primary; adhesive felt liner requires one new low-risk supplier (felt sheets, Amazon: ~$8 for 30 precut circles); low MOQ |
| UGC Opportunity | 4 | "Dice rolling in the tray" photo is satisfying and shareable; tabletop gaming community posts to r/DnD, r/boardgames; dice photography (colorful polyhedral dice in a nice tray) is inherently photogenic |
| **Weighted Total** | **4.35** | 5×0.30 + 4×0.25 + 4×0.20 + 4×0.15 + 4×0.10 = 1.50+1.00+0.80+0.60+0.40 |

**Rating: GO — Strong demand but more competition than controller stands. Use as a "second batch" gaming SKU after P-05 is listed.**

---

### P-07 — Miniature Display Base Set (D&D / Warhammer Style)

**Description**: Blank 25mm, 32mm, and 40mm round bases for tabletop miniatures, sold in packs of 10-20. Plain bases are a pure consumable — players constantly need them for resin casts or conversions. The texture-top variant (cobblestone, dungeon stone, grass texture) commands higher prices.

**Etsy demand signal**: "Miniature bases 3d printed" has 200+ listings. Several sellers with 100-200 reviews. However, PETG or resin bases are preferred for miniatures (PLA+ is brittle at thin sections). Mass-produced resin bases from AliExpress undercut FDM on price. The value-add is textured tops or unusual sizes.

**Unit economics**: Very fast print — 25mm base takes 8-12 minutes, 32mm takes 12-18 minutes. Batch 20 on a plate in 3-4 hours. COGS ~$0.08-0.12 per base material, $0.35 for pack packaging. Sell a 10-pack of 25mm bases at $7.99-10.99. Net margin ~70-75%.

| Criterion | Score | Justification |
|---|---|---|
| Demand Signal | 3 | 200+ listings but competitive; AliExpress resin base undercuts significantly on price; value is in texture variants and unusual sizes; r/DnD demand is real but price-sensitive |
| Margin Potential | 3 | 70-75% margin but low absolute dollars per sale ($5-8 net per 10-pack); requires high volume or premium texture to lift revenue meaningfully |
| Design Complexity | 4 | 25mm and 32mm plain bases: 30 min CadQuery; textured variants (cobblestone texture): 1-2 hrs using OpenSCAD or Fusion360 texture mapping; Printables has many CC0 textured base designs |
| Supplier Readiness | 5 | PLA+ or PETG; no hardware; existing supply |
| UGC Opportunity | 2 | Bases are not visually interesting to the general buyer; appealing only within the miniatures hobby; not shareable outside that community |
| **Weighted Total** | **3.10** | 3×0.30 + 3×0.25 + 4×0.20 + 5×0.15 + 2×0.10 = 0.90+0.75+0.80+0.75+0.20 |

**Rating: NO-GO (current). Low absolute margin per unit, resin price competition, limited UGC. Revisit if a textured variant emerges.**

---

## Home and Garden

### P-08 — Geometric Wall Planter / Hanging Planter (Succulent Size)

**Description**: A geometric faceted planter for small succulents, cacti, or air plants. Designed for wall mounting (keyhole slot in back) or hanging (built-in loop). Geodesic or low-poly aesthetic is the category signature look. White or terracotta PLA+ are the best-converting colors.

**Etsy demand signal**: "Geometric planter 3d printed" has 400+ listings. Multiple sellers achieving 200+ reviews. Price range: $9-25 per single planter, $22-45 for hanging sets of 3. High Pinterest and Instagram engagement. Peak demand: March-June (spring). Seasonal consideration.

**Unit economics**: Print weight ~60-100g, print time 1.5-2.5 hours, COGS ~$1.60-2.50, sell price $14-22, net margin ~79-82%.

| Criterion | Score | Justification |
|---|---|---|
| Demand Signal | 4 | 400+ listings; strong Pinterest/Instagram pull; multiple sellers with 200+ reviews; peak spring demand (March-June); moderate off-season sales for gifting; overlap with "plant mom" gift buyer |
| Margin Potential | 4 | 79-82% margin; $1.60-2.50 COGS; 1.5-2.5 hr print; good throughput |
| Design Complexity | 4 | Multiple CC0 geometric planter designs on Printables and Thingiverse; parametric variants achievable in 2 hrs CadQuery; 1 test print for drainage hole sizing |
| Supplier Readiness | 5 | PLA+ or PETG; no hardware; existing supply; terracotta PLA color is available from most suppliers |
| UGC Opportunity | 4 | Plant + planter photography is inherently appealing; "unboxing a small succulent in a geometric planter" is a Pinterest/Instagram standard; before/after (ugly plastic pot → geometric planter) is shareable |
| **Weighted Total** | **4.10** | 4×0.30 + 4×0.25 + 4×0.20 + 5×0.15 + 4×0.10 = 1.20+1.00+0.80+0.75+0.40 |

**Rating: GO — Strong summer demand coming. Launch before May 2027 spring season for best timing advantage.**

---

### P-09 — Bedside Charging Station Organizer

**Description**: A nightstand dock that holds one or two phones, provides a pass-through for charging cables (with cable management notches), and has an integrated slot for earbuds case or watch. Prints in two pieces (main body + cable management base tray). Target: 150mm wide × 100mm deep × 100mm tall.

**Etsy demand signal**: "Charging station organizer 3d printed" has 100-200 listings with several sellers achieving 50-100+ reviews. Strong WFH and tech-household buyer. The multi-device angle (phone + earbuds + watch) is the premium position. Amazon has many injection-molded versions at $15-30 which validates the market but the 3D printed angle is "exact dimensions, colors, no plastic seams."

**Unit economics**: Print weight ~180-220g (two-piece), print time 3.5-5 hours, COGS ~$5.00-6.50, sell price $34-44, net margin ~77-81%.

| Criterion | Score | Justification |
|---|---|---|
| Demand Signal | 4 | 100-200 Etsy listings; confirmed mass-market demand (Amazon injection-molded versions sell well); Reddit: r/BuyItForLife and r/malelifestyle both feature cable management regularly; strong tech-household buyer who upgrades their bedroom organization |
| Margin Potential | 4 | 77-81% margin; $5-6.50 COGS; 3.5-5 hr print time is the constraint; good absolute margin ($28-35 net/unit) |
| Design Complexity | 2 | Original CadQuery design required — no off-the-shelf design matches the phone + earbuds + watch slot configuration without brand-specific dimensions; 4-6 hrs design; 2-3 test iterations for cable notch sizing |
| Supplier Readiness | 5 | PLA+ or PETG; no hardware (notches accept standard cables natively); existing supply |
| UGC Opportunity | 4 | "Clean nightstand" is a well-established lifestyle photo category; before (cable rats-nest on nightstand) after (organized dock with all devices in place) is compelling |
| **Weighted Total** | **3.70** | 4×0.30 + 4×0.25 + 2×0.20 + 5×0.15 + 4×0.10 = 1.20+1.00+0.40+0.75+0.40 |

**Rating: GO — Strong market, good margin. Prioritize after Wave 2 CAD work is complete (design session 3). The design investment is real but the product is highly differentiated.**

---

### P-10 — Garden Plant Marker Set (Herb / Vegetable Labels)

**Description**: A set of 8-12 stake-style plant markers with text slots or pre-printed herb/vegetable names. Sold as seasonal spring/summer items. PLA+ degrades slowly in outdoor sun; PETG is better for outdoor durability. Alternatively, offer as chalk-paintable PLA+ markers for "customize your own."

**Etsy demand signal**: "Plant markers 3d printed" has 300+ listings. Many sellers with 50-150 reviews. Strong spring seasonal peak. Price: $8-18 for a set of 8-12. The personalized angle (custom names) commands $15-28. Demand is real but seasonally concentrated and price-sensitive.

**Unit economics**: Very fast — a single stake is 5-15g, prints in 10-25 minutes. Batch 16-24 per plate. Set of 12 stakes COGS ~$0.70-1.00 (filament + packaging), sell price $10-16, net margin ~85-88% — the highest percentage margin of any product on this list, but lowest absolute dollars.

| Criterion | Score | Justification |
|---|---|---|
| Demand Signal | 4 | 300+ listings; seasonal spring demand; personalized variant has year-round gifting angle (custom vegetable garden markers as housewarming gift); Pinterest heavily features this category |
| Margin Potential | 3 | 85-88% gross margin percentage but only $8-14 absolute net per set; high percentage does not translate to high revenue per hour without very high volume |
| Design Complexity | 5 | Basic stake shape: 30 minutes CadQuery; text variants: parametric text extrusion 1-2 hrs; CC0 designs also available on Printables for immediate use |
| Supplier Readiness | 5 | PLA+ (indoor/chalk-board version) or PETG (outdoor-durable version); no hardware; existing supply |
| UGC Opportunity | 3 | Garden/herb box flat-lay is appealing but seasonal and not shareable outside the gardening community; limited viral potential |
| **Weighted Total** | **3.85** | 4×0.30 + 3×0.25 + 5×0.20 + 5×0.15 + 3×0.10 = 1.20+0.75+1.00+0.75+0.30 |

**Rating: WATCH — Excellent volume-filler when printer capacity is available (sub-30-minute prints, batch 20+ per plate). Not a priority design investment; use existing CC0 STLs to list immediately.**

---

### P-11 — Bird Feeder (Modular Tube Style)

**Description**: A 3D printed bird feeder body (clear PETG or opaque PLA) with a standard 1-inch diameter tube or pre-cut PVC pipe insert for the seed column. Hardware: two small eye-bolts for hanging wire. The 3D printed body provides the perch, seed port, and rain guard; standard hardware handles the seed reservoir.

**Etsy demand signal**: "3d printed bird feeder" has 80-150 listings. Several sellers with 30-80 reviews. Price range: $15-35. Less competitive than desk accessories but also lower demand. Seasonal — spring/fall peak.

**Unit economics**: Print weight ~100-160g (body, excluding hardware), print time 2-4 hours, COGS ~$3.00-5.00 (material + packaging + eye-bolts $0.40), sell price $20-28, net margin ~73-78%.

| Criterion | Score | Justification |
|---|---|---|
| Demand Signal | 3 | 80-150 Etsy listings; steady outdoor market; birding hobby is growing; however, mass-market metal/plastic feeders at $8-15 from Amazon undercut hard; 3D printed angle is "modular/repairable/colorful" |
| Margin Potential | 3 | 73-78% margin; $3-5 COGS including hardware; 2-4 hr print; acceptable but not outstanding |
| Design Complexity | 3 | Original design needed for a good fit to standard PVC pipe; 3-4 hrs CadQuery; 2 test iterations (seed port size, drainage holes, hardware mounting points); moderate complexity |
| Supplier Readiness | 4 | PLA+ body (existing); eye-bolts or hanging hardware require a small Amazon order (~$5 for 50); new but trivial |
| UGC Opportunity | 3 | Outdoor feeder with birds is genuinely appealing photography but requires having birds, waiting for them to land, and good outdoor lighting — practically difficult to shoot product photos for |
| **Weighted Total** | **3.10** | 3×0.30 + 3×0.25 + 3×0.20 + 4×0.15 + 3×0.10 = 0.90+0.75+0.60+0.60+0.30 |

**Rating: NO-GO (current). Crowded by cheap mass-market options, difficult product photography, design time not justified at current scale. Revisit at 4+ printer capacity.**

---

## Organization and Home

### P-12 — Invisible Shelf Bracket / Floating Shelf Clip

**Description**: A wall-mount bracket that accepts a standard 2×6 or 2×8 lumber shelf board, making the shelf appear to float. Printed in PETG for load-bearing strength. Pair sells at $18-30 for a set of 2 (needed per shelf).

**Etsy demand signal**: "Floating shelf bracket 3d printed" has 50-100 listings. Modest review counts. Competition from Amazon-sold metal brackets is intense. The differentiation angle is custom color matching (print to match wall color) and non-standard shelf depths that mass-market brackets do not support.

**Unit economics**: Print weight ~90-120g in PETG, print time 2-3 hours, COGS ~$3.50-5.00 per pair, sell price $18-28, net margin ~73-78%.

| Criterion | Score | Justification |
|---|---|---|
| Demand Signal | 2 | 50-100 listings; modest reviews; strong Amazon metal competition at $10-15 per pair; differentiation argument weak without a compelling custom-color or specialty-size position |
| Margin Potential | 3 | 73-78% margin; COGS reasonable but 2-3 hr print time for a $28 sale is lower per-hour return than cable clips; returns risk if load-bearing failure |
| Design Complexity | 3 | Simple rectangular channel with wall-anchor holes; 2-3 hrs CadQuery; structural testing important — PETG at 40% infill for load-bearing |
| Supplier Readiness | 5 | PETG existing; no hardware (buyer supplies own screws/anchors) |
| UGC Opportunity | 3 | Floating shelf look is aspirational but the bracket itself is invisible — the product is inherently hard to photograph convincingly |
| **Weighted Total** | **2.95** | 2×0.30 + 3×0.25 + 3×0.20 + 5×0.15 + 3×0.10 = 0.60+0.75+0.60+0.75+0.30 |

**Rating: NO-GO. Low demand signal, IP liability risk if bracket fails under load, competition intense. Do not invest design time.**

---

### P-13 — Magnetic Wall Key Hook (Neodymium Magnet Insert)

**Description**: A wall-mount key hook with a neodymium magnet embedded in the base. Keys with a metal ring stick magnetically; additional hooks hold fobs and passes. Sold as a single-piece print with a pre-formed magnet pocket (magnets inserted after printing — 6mm × 2mm N52 neodymium, $5 for 50-pack on Amazon).

**Etsy demand signal**: "Magnetic key holder wall mount" has 150-250 listings. Several sellers achieving 100+ reviews. Price: $12-24. The magnetic-insert design is a premium tier over standard hook designs. Reviews consistently note the "satisfying snap" as a product highlight.

**Unit economics**: Print weight ~40-60g, print time 0.8-1.2 hours, COGS ~$1.20-1.80 (material + 2-4 magnets × $0.10 + packaging), sell price $14-22, net margin ~82-85%.

| Criterion | Score | Justification |
|---|---|---|
| Demand Signal | 4 | 150-250 listings; several with 100+ reviews; "key organization" is a perennial home category; magnetic variant is a premium differentiator; r/homeimprovement and r/malelifestyle recommend magnetic key holders regularly |
| Margin Potential | 5 | 82-85% margin; COGS ~$1.20-1.80; 0.8-1.2 hr print; one of the best per-print-hour products on this list |
| Design Complexity | 4 | Simple hook body with 6mm circular magnet pocket: 1-2 hrs CadQuery; magnet pocket depth must be precise (magnet should sit flush or 0.3mm below surface); 1 test print |
| Supplier Readiness | 4 | PLA+ existing; 6mm × 2mm N52 neodymium magnets: Amazon pack ~$5 for 50 units (sourced as one-time order; reorder at 40 units sold) |
| UGC Opportunity | 3 | Key-sticking-to-wall satisfying demo; "before: keys on counter everywhere, after: all keys on magnetic wall hook" is real; less dramatic than desk transformation but functional and clean |
| **Weighted Total** | **4.20** | 4×0.30 + 5×0.25 + 4×0.20 + 4×0.15 + 3×0.10 = 1.20+1.25+0.80+0.60+0.30 |

**Rating: GO — Priority 4. Fast print, high margin, simple hardware BOM, clear differentiation over plain hooks.**

---

### P-14 — House Number Address Sign (Modern Minimalist)

**Description**: Modern flat-face address number sign for residential homes, using extruded numerals mounted on a backer plate. Printed in weather-resistant PETG or ASA. Sold in sets covering 2-5 digit addresses. Mounting hardware (short screws, adhesive strips) included.

**Etsy demand signal**: "House number sign 3d printed" has 200-300 listings. Several sellers with 50-200 reviews. Price: $20-55 depending on character count and size. Moderate repeat-purchase potential (buyers move, gift to neighbors). IP-safe — numbers are not trademarked.

**Unit economics**: Variable by address. 3 large numerals + backer: ~120-180g PETG, print time 2-4 hours, COGS ~$4.50-7.00 (material + hardware + packaging), sell price $28-40, net margin ~72-78%.

| Criterion | Score | Justification |
|---|---|---|
| Demand Signal | 4 | 200-300 listings; confirmed custom order market; gift potential (housewarming); design differentiation through font choice drives repeat patterns; buyers who find a font they like return |
| Margin Potential | 3 | 72-78% margin; 2-4 hr print; decent absolute margin ($20-30 net) but not the most efficient use of print hours |
| Design Complexity | 3 | CadQuery text extrusion for numerals: 2-3 hrs; backer plate: 1 hr; total 3-4 hrs + per-order customization time (15-20 min to generate new address STL) |
| Supplier Readiness | 4 | PETG (existing); mounting hardware (short self-tapping screws + adhesive foam tape strips — Amazon ~$8 for a supply of 50 units); new but trivial |
| UGC Opportunity | 3 | "New house number" is photogenic as an installation shot; neighborhood context makes a good lifestyle photo; limited viral potential |
| **Weighted Total** | **3.40** | 4×0.30 + 3×0.25 + 3×0.20 + 4×0.15 + 3×0.10 = 1.20+0.75+0.60+0.60+0.30 |

**Rating: WATCH — Good market, real custom order potential, but per-order customization time adds overhead. Viable after a parametric CadQuery script automates STL generation from numeric input.**

---

## Novelty and Gifts

### P-15 — Corner Bookmarks (Patterned Set)

**Description**: Triangular corner page markers that clip over a book page corner. Novelty / gift item. Simple geometry (45° triangle with precise lip depth). Can incorporate small embossed designs (geometric, floral, animal). Sold in sets of 4-6.

**Etsy demand signal**: "3d printed bookmark" has 150-250 listings. Several sellers with 50-150 reviews. Price: $8-16 per set of 4-6. Gift and stationery buyer. Lightweight — postal weight is minimal (whole set <20g); low shipping cost.

**Unit economics**: Single bookmark: 3-6g, prints in 8-15 minutes. Set of 6: <36g total, print time ~1 hour for a full plate of mixed designs. COGS per set ~$0.40-0.60 (filament + packaging), sell price $9-14, net margin ~83-86%.

| Criterion | Score | Justification |
|---|---|---|
| Demand Signal | 3 | 150-250 listings; reading/gift market; lighter demand signal than desk accessories; strong gift potential (book clubs, teacher appreciation, school events) but seasonal |
| Margin Potential | 4 | 83-86% gross margin; $0.40-0.60 COGS; very fast print — 60+ sets per P1S per day; excellent per-hour throughput at volume |
| Design Complexity | 5 | Corner bookmark geometry: 30 min CadQuery; embossed pattern variants: 1-2 hrs; CC0 designs on Printables available immediately |
| Supplier Readiness | 5 | PLA+ only; no hardware; existing supply; multiple color options = multiple SKUs from one design |
| UGC Opportunity | 2 | Bookmarks are not visually exciting; "closed book with bookmark peeking out" is the standard photo; limited before/after narrative |
| **Weighted Total** | **3.65** | 3×0.30 + 4×0.25 + 5×0.20 + 5×0.15 + 2×0.10 = 0.90+1.00+1.00+0.75+0.20 |

**Rating: WATCH — Excellent margin percentage and zero design time (use existing STLs). Valid as a high-volume, low-effort SKU to fill plates during light production periods. Not a priority design investment.**

---

### P-16 — Custom Keychain (Name / Initial / Mini Shape)

**Description**: Personalized keychains with embossed or cut-through names, initials, or small geometric shapes. Sold as custom order (buyer specifies name/text). Very fast per-unit print; batched in large quantities per plate.

**Etsy demand signal**: "Custom keychain 3d printed" consistently ranks as one of the highest-searched 3D printed categories on Etsy in 2025-2026. 1000+ active listings. Many sellers with 500-2000+ reviews. Price: $5-12 per keychain. High competition but also high volume.

**Unit economics**: 5-10g per keychain, 15-25 minutes each, batch 30-40 per plate. COGS ~$0.25-0.40 (filament + packaging), sell price $7-12, net margin ~85-88%.

| Criterion | Score | Justification |
|---|---|---|
| Demand Signal | 5 | Top-10 3D printed Etsy category; 1000+ listings; multiple sellers with 1000+ reviews; gifting + events (weddings, graduations, corporate); well-established demand |
| Margin Potential | 3 | 85-88% gross margin percentage; however, $6-10 net per unit requires high volume to generate meaningful revenue; competitive price ceiling limits sale price |
| Design Complexity | 4 | CadQuery parametric text extrusion: 2-3 hrs; per-order customization: 5-10 min to generate new name STL; CC0 keychain frames available on Printables |
| Supplier Readiness | 5 | PLA+ only; split rings (keychain hardware): 200-pack for $5 on Amazon; minimal new supplier |
| UGC Opportunity | 2 | Keychains are low-drama product photography; "pile of colorful keychains" is the standard shot; limited before/after narrative |
| **Weighted Total** | **3.80** | 5×0.30 + 3×0.25 + 4×0.20 + 5×0.15 + 2×0.10 = 1.50+0.75+0.80+0.75+0.20 |

**Rating: WATCH — High demand, high competition. Only viable with a parametric CadQuery script that automates per-name STL generation (otherwise custom order overhead kills economics). Not a priority until that script exists.**

---

### P-17 — Fidget Spinner / Infinity Cube (Simple Fidget Toy)

**Description**: Print-in-place or 2-3 piece fidget toys. The "print-in-place" category (cube turns itself, no assembly) is the key technical differentiator. Note: basic fidget spinners are saturated; the premium is in novel geometry (infinity cubes, gear-based mechanisms).

**Etsy demand signal**: "Fidget toy 3d printed" has 500+ listings. Competitive; market includes both print-in-place (no assembly) and assembled mechanical designs. Top sellers have 200-500 reviews. Buyer segment overlaps with articulated animal buyers (P-01).

**Unit economics**: Print weight ~30-60g, print time 1-2 hours, COGS ~$1.00-1.60, sell price $10-18, net margin ~80-83%.

| Criterion | Score | Justification |
|---|---|---|
| Demand Signal | 4 | 500+ listings; well-established market; sensory toy buyer (ADHD focus product) is a strong niche; Amazon mass-market plastic versions set price ceiling; 3D printed angle is "unique mechanism, custom colors" |
| Margin Potential | 4 | 80-83% margin; $1-1.60 COGS; 1-2 hr print; good throughput |
| Design Complexity | 4 | Many CC0 print-in-place designs on Printables (cube twisting mechanism); test print required for mechanism play/feel; gear mesh tolerance testing if doing gear-based design |
| Supplier Readiness | 5 | PLA+ or PETG (stiffer = better for mechanisms); no hardware; existing supply |
| UGC Opportunity | 3 | "Satisfying mechanism" video is the standard format; gif or short video of the cube mechanism turning is shareable; less impactful without video capability |
| **Weighted Total** | **4.00** | 4×0.30 + 4×0.25 + 4×0.20 + 5×0.15 + 3×0.10 = 1.20+1.00+0.80+0.75+0.30 |

**Rating: WATCH — Strong market but overlaps significantly with P-01 (flexi animals). If P-01 succeeds, add fidget cube as a complement to the same buyer segment. Do not prioritize before P-01.**

---

### P-18 — 3D Printed Topo Map (Catalog SKU)

**Description**: Physical 3D printed topographic terrain map as a desktop or wall-mount product. See TOPO_MAPS_PRODUCT_RESEARCH.md for full analysis.

**Summary unit economics**: Medium map (200×200mm), print time 6 hrs, COGS $5.11, sell price $59.99, net margin $48.98 (81.6%).

| Criterion | Score | Justification |
|---|---|---|
| Demand Signal | 4 | 40-80 physical-print Etsy sellers; $25-140 price range; custom location premium $20-40; 4.8+ avg reviews; under-served relative to demand; similar whitespace to Gridfinity before it grew |
| Margin Potential | 4 | 81-82% gross margin; $5-8 COGS; high absolute net ($33-73/unit); however, 4-10 hr print time limits throughput |
| Design Complexity | 5 | TouchTerrain generates STL in 5-10 minutes; no CAD required; one slicer configuration to document; test print one standard map |
| Supplier Readiness | 5 | PLA+ only (standard catalog); no hardware; existing supply |
| UGC Opportunity | 3 | Geographic terrain is visually interesting; painted finish (elevation gradient) is highly photogenic; less "before/after" narrative than desk organization; niche audience |
| **Weighted Total** | **4.10** | 4×0.30 + 4×0.25 + 5×0.20 + 5×0.15 + 3×0.10 = 1.20+1.00+1.00+0.75+0.30 |

**Rating: GO — Zero CAD, premium price point, excellent fit for overnight long-run prints. List 3 catalog maps (Yosemite, Grand Canyon, Colorado) to test before expanding. Full analysis in TOPO_MAPS_PRODUCT_RESEARCH.md.**

---

## Master Rankings

### All 18 Candidates by Weighted Score

| Rank | ID | Product | Score | Rating |
|---|---|---|---|---|
| 1 | P-04 | Lithophane Night Light Panel | **4.75** | GO |
| 2 | P-01 | Articulated Flexi Dragon / Animal | **4.65** | GO |
| 3 | P-05 | Gaming Controller Stand | **4.65** | GO |
| 4 | P-06 | Dice Tray (Tabletop Gaming) | **4.35** | GO |
| 5 | P-13 | Magnetic Wall Key Hook | **4.20** | GO |
| 6 | P-18 | 3D Printed Topo Map | **4.10** | GO |
| 7 | P-08 | Geometric Wall Planter | **4.10** | GO |
| 8 | P-17 | Fidget Spinner / Infinity Cube | **4.00** | WATCH |
| 9 | P-09 | Bedside Charging Station | **3.70** | GO |
| 10 | P-10 | Garden Plant Marker Set | **3.85** | WATCH |
| 11 | P-16 | Custom Keychain | **3.80** | WATCH |
| 12 | P-15 | Corner Bookmarks | **3.65** | WATCH |
| 13 | P-02 | Modular Drawer Dividers | **3.50** | WATCH |
| 14 | P-14 | House Number Address Sign | **3.40** | WATCH |
| 15 | P-03 | Laptop Stand / Riser | **3.45** | WATCH |
| 16 | P-12 | Invisible Shelf Bracket | **2.95** | NO-GO |
| 17 | P-07 | Miniature Display Base Set | **3.10** | NO-GO |
| 18 | P-11 | Bird Feeder | **3.10** | NO-GO |

---

## Top 5 for Immediate Design Consideration

### Priority 1 — P-04: Lithophane Night Light Panel (Score: 4.75)

**Why first**: Highest combined score of any product analyzed (new or Wave 2). Zero CAD required — standard lithophane generators handle STL creation. The print-reveal photo or video (opaque panel glows with a photo) is the most inherently viral product demonstration in this entire catalog. 85-87% gross margin with $35-65 price point. **Action**: Generate one test lithophane from a free stock photo, print at 0.10mm layer height, backlight, photograph. If the visual quality is acceptable, list within a week.

### Priority 2 — P-01: Articulated Flexi Dragon / Animal (Score: 4.65)

**Why second**: Zero design time — CC0 STL files are production-ready on Printables. The AMS multi-color capability is a direct competitive differentiator (most sellers printing single-color flexi dragons; AMS enables green body + orange fins + red claws in one print). Immediate revenue with no design investment. **Action**: Download top-rated CC0 flexi dragon STL from Printables (verify CC0 license), configure AMS color assignment, run one test print, photograph, list.

### Priority 3 — P-05: Gaming Controller Stand (Score: 4.65)

**Why third**: Same reasoning as flexi dragon — zero design investment, high demand, AMS color customization is a differentiator. The gaming buyer segment is entirely separate from the cable management buyer, meaning controller stands expand reach without cannibalizing existing traffic. **Action**: Download CC0 universal controller stand STL, verify fit with DualSense-sized controller, list alongside flexi dragon for gaming audience.

### Priority 4 — P-13: Magnetic Wall Key Hook (Score: 4.20)

**Why fourth**: Highest per-print-hour net margin of any hardware-containing product. The magnet insert is a simple BOM addition (100 magnets for $5) with minimal operational overhead. Fast print (under 1.5 hours). Clean differentiation from the plain key hooks (H-03) already in the commodity library. **Action**: Design magnet pocket in CadQuery (extend existing H-03 key hook design with 6mm pocket, estimated 1.5-2 hrs), order N52 magnets, print test batch of 4, verify magnet retention and key adhesion.

### Priority 5 — P-18: Topo Map Catalog SKU (Score: 4.10)

**Why fifth**: Zero CAD time. $49-73 net margin per print for a single overnight run. The product occupies the printer during hours when cable clips and hooks are not batching, maximizing capital utilization with no additional fixed cost. **Action**: Generate 3 STLs via TouchTerrain (Yosemite Valley, Grand Canyon South Rim, Colorado state with terrain fill). Print one of each. Photograph with side-lighting to emphasize terrain texture. List all three as separate Etsy listings with location-specific SEO titles.

---

## Notes on Products Not Scored (Ruled Out During Analysis)

The following were considered but not formally scored due to clear disqualifying factors:

- **Wall art / geometric panel**: Extremely competitive, requires artistic differentiation, printing flat panels with fine surface detail is challenging on FDM (layer lines visible front-face). Resin is better for this. NO-GO until resin capability exists.
- **3D printed jewelry**: Requires post-processing (sanding, painting, or resin casting) to look premium. FDM layer lines are fatal for jewelry aesthetics. NO-GO.
- **Custom phone case**: Brand-specific dimension designs carry trademark risk. Generic cases have extremely low WTP ($5-8). NO-GO.
- **Replacement parts / jigs**: High design time per unit (customer-specific), very low volume, requires exact measurements. B2B channel, not Etsy. Deferred.

---

## Sources

- [Best Selling 3D Printed Products on Etsy 2026 — Insight Agent](https://www.insightagent.app/guides/best-selling-3d-printed-items-etsy)
- [23 Best Things to 3D Print and Sell in 2026 — EufyMake](https://www.eufymake.com/blogs/business-ideas/best-3d-print-sell-profitable-items)
- [15 Best Selling 3D Printed Items on Etsy 2026 — Hyper3D](https://hyper3d.ai/blog/best-selling-3d-printed-items)
- [10 Profitable 3D Prints That Actually Sell on Etsy — Get3DSTL](https://get3dstl.com/profitable-3d-prints-etsy/)
- [Top 3D Models to Sell in 2026 — PrintPal Blog](https://blog.printpal.io/top-3d-models-to-sell-in-2026-profitable-designs-for-etsy-and-online-marketplaces/)
- [Most Popular 3D Printed Items on Etsy — Insight Agent](https://www.insightagent.app/guides/popular-3d-printed-items-etsy)
- [3D Printed Dice Tray Etsy Market](https://www.etsy.com/market/3d_print_dice_tray)
- [Etsy 3D Printing Strategy for 2026 — PrintPal](https://printpal.io/resources/3d-printing-strategy-to-make-1000s-on-etsy-in-2026)
