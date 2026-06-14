---
title: Phase 2 Product Expansion Research — Beyond ModRun
project: mfg-farm
created: 2026-06-14
status: active
confidence: high — market data from live Etsy search results, web searches, and established mfg-farm research base
related: market-research.md, product-expansion-research.md, BATCH_2_PRODUCT_RESEARCH.md
---

# Phase 2 Product Expansion Research

**Lead finding:** Seven product candidates stand out as high-potential Phase 2 additions beyond the ModRun Rail Clip. The top recommendation for immediate launch is the **custom cookie cutter set** — lowest design complexity, fastest print time (8–20 min each), highest search volume on Etsy, and a proven seasonal + evergreen demand profile. Second priority is the **wall-mount magnetic keyholder system**, which targets the same desk/home-setup buyer as ModRun while commanding $18–35 per unit. All seven candidates use the same Bambu P1S + PLA/PETG workflow established for ModRun; none require supports when designed correctly.

---

## Context and Methodology

**What "Phase 2" means:** ModRun is a niche B2B product (cable management for server rack rails). Phase 2 expands into higher-volume consumer product categories while reusing the same printer, materials, and CadQuery design workflow. The goal is to reach $3,000–$5,000/month revenue by Month 6.

**Market data methodology:** Etsy listing counts and price ranges derived from live Etsy market pages and search results (June 2026). Review counts on competitor listings used as proxy for sell-through velocity (exact sales data is not publicly visible on Etsy). Margin calculations use the established mfg-farm cost basis: PLA+ at $0.013/g, Etsy effective fee rate of ~16.8% on a typical $16–$32 sale (6.5% transaction + 3% payment processing + $0.25 + $0.20 listing amortized).

**Key constraint (Etsy June 2025 policy):** All designs must be original — designs purchased from Cults3D, MakerWorld, or Printables do not qualify even with a commercial license. All candidates below assume original CadQuery-designed files owned by the shop.

---

## Candidate 1: Custom Cookie Cutter Sets

### Product description
Custom-shaped food-safe cookie cutters printed in PETG (food-safe material, heat-tolerant up to ~80°C). Sold in themed sets: holiday shapes, pet outlines, wedding/baby shower monograms, name initial sets, business logo cutters. Each cutter is a thin-wall frame with a rolled edge for clean cookie cuts. Sets of 3–6 cutters ship in a poly mailer.

**Problem solved:** Mass-market cookie cutters come in generic shapes. Custom logo cutters for events, personalized initial sets, and unusual theme sets (specific animal silhouettes, local landmarks) are impossible to find in stores and highly giftable.

### Target market
Home bakers, wedding/event planners, small bakeries needing branded marketing tools, parents planning birthday parties. Predominantly female buyers on Etsy; gift purchase occasion is high.

### Estimated demand
Etsy searches for "3d printed cookie cutter," "custom cookie cutter 3D print," and "personalized cookie cutter" return **5,000–10,000+ active listings** across all variants — one of the highest-volume 3D printing categories on the platform. Top sellers have 1,000–3,000+ reviews. The category spikes seasonally (Halloween, Christmas, Valentine's Day) but has strong evergreen demand for personalized/custom shapes year-round. Custom cutters (buyer provides logo or name) have essentially zero price-comparison competition because each order is unique.

**Price range observed:** $6–$18 per individual cutter; $18–$45 for themed sets of 4–6. Personalized business logo cutters command $25–$55 per unit.

### Printability score: 9/10
- **Complexity:** Low. A cookie cutter is an extruded 2D profile, 3–5mm thick wall, no infill. One of the simplest 3D printing geometries.
- **Supports:** None required. Flat profile prints directly on bed.
- **Material:** PETG is required for food contact safety and heat resistance — wash temperature tolerance. PETG costs ~$0.014–0.018/g vs. PLA+ at $0.013/g, negligible difference.
- **Print time:** 8–20 minutes per cutter on P1S at production speeds. A plate of 12 small cutters prints in ~90 minutes. Very high throughput.
- **Post-processing:** None. Pop off PEI plate, inspect edge sharpness. Done.

### Margin estimate

| Item | Set of 4 cutters (~20g PETG each = 80g total) |
|---|---|
| Filament cost (80g PETG @ $0.016/g) | $1.28 |
| Packaging (poly mailer) | $0.80 |
| Etsy fees on $24 sale (~16.8%) | $4.03 |
| **Total COGS + fees** | **$6.11** |
| Sell price | $24.00 |
| **Net margin** | **~74.5%** |

Personalized sets (custom name/logo): sell for $28–$40, maintaining 72–78% net margins. The personalization component adds 5–10 minutes of design work per order (importing SVG outlines into CadQuery, extruding the profile) — manageable at low volume, and can be priced at a $6–$10 premium over generic sets.

### Uniqueness and differentiation angle
The market has many sellers, but **custom-logo and custom-name cutters are inherently non-comparable** — a buyer wanting their business logo cannot comparison-shop between sellers. Differentiation angles: (1) fast turnaround ("design approval in 24 hours"), (2) food-safe PETG with explicit FDA-compliant material callout in the listing, (3) multi-color two-tone cutters using AMS for premium gift sets.

### Risk
- **IP:** Moderate. Do not accept requests for Disney/trademarked character outlines. Stick to buyer-provided logos, custom text, and original silhouettes. The buyer submitting their own design is a natural IP filter.
- **Food safety disclosure:** Label clearly as "for decorative use, hand wash only" — this is the standard approach that protects against food safety liability claims.
- **Print failure rate:** Very low on flat profiles. PETG warping is the main risk; mitigated with PEI plate adhesion on the P1S.
- **Seasonality:** Revenue will peak Oct–Dec and Feb–Apr; plan inventory and print queues accordingly.

**Overall assessment:** Highest search volume of all candidates. Fastest print time. Strongest seasonal demand spikes. Weakest direct competition on custom/personalized variants. **Top recommendation for Phase 2 launch.**

---

## Candidate 2: Wall-Mount Magnetic Keyholder System

### Product description
A wall-mounted keyholder panel with embedded N52 neodymium magnets that hold metal keys (and optionally a key fob, mail slot, or phone shelf). Sold in small (2 key hook positions), medium (4 positions), and large (6 positions with shelf). The panel mounts to the wall with two screws; magnets are press-fit into recesses in the back face. Optional engraved family name or house number on the face plate. Design is minimal/architectural — fits entryway aesthetic.

**Problem solved:** Keys are the most commonly lost household item. A clean wall-mount solution near the door is a household staple gift item with evergreen demand.

### Target market
Homeowners (25–55), new home gifting occasion (housewarming), apartment dwellers, families. Also sells as a couple's gift. Strong Etsy buyer profile — emotional/gift purchase.

### Estimated demand
Etsy search for "magnetic key holder wall mount" and "3D printed key holder wall" returns **600–1,200 active listings**. One listing (JushoDesign magnetic wall mount key organizer) has **3,928 favorites** — among the highest favorited counts observed in the category, indicating strong buyer intent signals. Top sellers show 200–800+ reviews on well-established listings.

**Price range:** $16–$45. Small 2-hook panels at $16–$22; large engraved family name panels at $35–$55.

### Printability score: 8/10
- **Complexity:** Low-medium. A flat wall panel with countersunk screw holes, magnet recesses (17mm diameter × 3mm deep), and optional embossed text. Simple CadQuery geometry.
- **Supports:** None for flat panels. Only needed if integrating a shelf projection > 45-degree overhang — solvable with geometry.
- **Material:** PLA+ for indoor use is fine. PETG for premium tier.
- **Print time:** 30–60 minutes per panel depending on size. A plate of 6 small panels prints overnight.
- **Assembly:** Press-fit 3×15mm N52 disc magnets — 5–10 seconds per magnet, no glue. BOM cost: $0.04–$0.08/magnet in bulk from AliExpress.

### Margin estimate

| Item | Medium panel, 4 positions, engraved name (~90g PLA+) |
|---|---|
| Filament cost (90g @ $0.013/g) | $1.17 |
| Magnets (4 × $0.06) | $0.24 |
| Packaging (padded mailer) | $1.00 |
| Etsy fees on $28 sale (~16.8%) | $4.70 |
| **Total COGS + fees** | **$7.11** |
| Sell price | $28.00 |
| **Net margin** | **~74.6%** |

### Uniqueness and differentiation angle
The high favoriting rate on the JushoDesign listing (3,928 favorites) confirms strong buyer intent with moderate conversion — many people want this product. Differentiation: (1) personalized name engraving is standard in the premium tier; (2) offer color options (matte black, white, earth tones); (3) add a mail slot or phone charging shelf as a premium variant.

### Risk
- **IP:** Very low. Functional organizer with no character reference.
- **Magnet sourcing:** N52 disc magnets require AliExpress lead time (14–21 days for bulk orders). Order early and maintain 4–6 weeks of stock.
- **Competition:** The listing count is large but many sellers are in the $10–$14 range with no personalization — differentiate on quality and custom text, not price.

---

## Candidate 3: Modular Desk Cable Management System (Consumer-Facing)

### Product description
A family of 5–8 interlocking desk cable management pieces designed for consumer desk setups: edge-clip cable channels, adhesive-mount desk cable guides, monitor cable routing brackets, multi-cable spine clips, power strip mounting trays, and a cable hub with pass-through ports. Sold as individual pieces and as a "Desk Setup Starter Kit" bundle. Original design with a minimal aesthetic — matte black or white, clean lines, compatible with common desk materials.

**Problem solved:** The consumer desk setup market is enormous. Cable clutter is the #1 complaint in desk setup communities (r/battlestations, r/desksetups). Existing cable management products are ugly, don't fit modern desks, or require power tools.

**Note on ModRun distinction:** ModRun is for server rack rail infrastructure — B2B, technical, small niche. This product is consumer desk cable management — B2C, aesthetic, large market. They share a manufacturing method but serve entirely different customers.

### Target market
Remote workers, gamers, streaming setup enthusiasts, home office workers. 18–40 demographic. Strong Reddit, YouTube, and Instagram discovery channel — lifestyle photography drives discovery.

### Estimated demand
Etsy "3D printed cable organizer" and "desk cable management" returns **2,000–4,000+ active physical-product listings** in 2026, with multiple recently added listings (June 2026 timestamps visible). Individual listings show 70–200+ favorites. Amazon "cable management" is a massive category — over 10,000 listings across all product types.

**Price range:** $8–$22 per piece; $32–$65 for curated desk setup bundles.

### Printability score: 9/10
- **Complexity:** Low. Edge clips, cable channels, and spine brackets are simple extrusions with clip geometry. No support needed when designed with clip hooks printing flat.
- **Print time:** 15–40 minutes per piece. Overnight plate batch produces 15–25 pieces.
- **Material:** PLA+ for desktop use is fine. PETG for any pieces near heat sources.
- **AMS value:** Two-color variants (black body, white label text) command $2–4 premium and are trivial on AMS.

### Margin estimate

| Item | 5-piece desk bundle (~120g total PLA+) |
|---|---|
| Filament cost (120g @ $0.013/g) | $1.56 |
| Packaging (small flat box) | $1.20 |
| Etsy fees on $38 sale (~16.8%) | $6.38 |
| **Total COGS + fees** | **$9.14** |
| Sell price | $38.00 |
| **Net margin** | **~76%** |

### Uniqueness and differentiation angle
Market has competitors but few with a **cohesive, aesthetically matched system** in a single shop. Differentiation: (1) all pieces from one shop with matching aesthetic; (2) desk-specific fit (include a desk thickness parameter at checkout); (3) matte black variant in a filament that photographs exceptionally well.

### Risk
- **Saturation:** The cable management category is the most competitive in this list. Must differentiate on design and photography, not price.
- **Etsy policy:** Original designs required. Do not adapt any Printables/MakerWorld cable clip designs.
- **Market fit:** This product is better suited to Amazon Handmade than Etsy for the functional purchase — prioritize Amazon launch alongside Etsy.

---

## Candidate 4: Wall-Mounted Tool and Entryway Organizer (Pegboard-Free)

### Product description
A modular wall-mount organizer that doesn't require a pegboard backing — it mounts directly to drywall with two standard screws. Individual hook modules in sizes S/M/L (for keys, umbrellas, bags, coats) snap together or mount independently. A tray module holds mail, sunglasses, and AirPods. Each module has a clean rectangular face with a subtle lip — no industrial look. Sold individually and as "entryway starter set" (2 hook modules + 1 tray).

**Problem solved:** Pegboard looks industrial and requires significant wall modification. This product is for urban apartments and modern homes that want functional entryway organization without the pegboard aesthetic.

### Target market
Urban apartment renters, millennial/Gen Z homeowners, new home gift buyers. Female Etsy buyer demographic skews toward this product.

### Estimated demand
Etsy "wall organizer 3D printed" and "wall storage 3D printed" return **400–900 active listings**. Wall storage with a premium minimal design has significantly less competition than desk accessories. A JushoDesign wall organizer listing shows high favoriting rates. Price range: $18–$45 for individual modules; $45–$80 for starter sets.

### Printability score: 8/10
- **Complexity:** Medium. Snap-together modules require precision fit (± 0.2mm tolerance on snap geometry). Flat-back wall mounts print cleanly with no supports.
- **Print time:** 25–50 minutes per module. A starter set (3 modules) takes 75–150 minutes total.
- **Material:** PETG preferred for weight-bearing hooks (holding bags, coats). PLA+ fine for light-duty mail tray.
- **Post-processing:** None if fit is well-calibrated. Test print recommended before full production run.

### Margin estimate

| Item | 3-module entryway set (~180g PETG) |
|---|---|
| Filament cost (180g PETG @ $0.016/g) | $2.88 |
| Packaging (small flat box) | $1.50 |
| Etsy fees on $45 sale (~16.8%) | $7.56 |
| **Total COGS + fees** | **$11.94** |
| Sell price | $45.00 |
| **Net margin** | **~73.5%** |

### Uniqueness and differentiation angle
The "no pegboard needed" design is a genuine differentiator. Most 3D printed hook systems are pegboard-dependent. Direct-mount modular wall organizers that look premium are underserved on Etsy.

### Risk
- **Structural:** PETG required for weight-bearing applications. Must communicate material clearly in listing. Include max weight rating.
- **Returns:** If a module snaps incorrectly or warps, the customer will complain. QC check snap geometry on each production run.
- **Drywall anchors:** Include a note in the listing about wall anchor requirements for heavy loads — manages customer expectations.

---

## Candidate 5: Articulated Flexi Animal Figures (Original Line)

### Product description
A line of 6–10 original print-in-place articulated creatures: a geometric axolotl, a faceted sea turtle, a modular snake form, a honeycomb dragon, and 2–3 fantasy insects. Each prints fully articulated in a single print — no assembly, no supports (designed for in-place hinges). Sold individually and in themed bundles (3-pack "ocean bundle," 5-pack "fantasy bundle"). Multi-color variants using AMS (silk gradient, glow-in-dark) at premium tier.

**Problem solved:** Gift and novelty item that doesn't fit any utility category — it's a fidget toy, desk decoration, and conversation piece. Strong gift-occasion purchase.

### Target market
Gift buyers (birthdays, stocking stuffers), gamers and tabletop RPG fans, children's novelty (not a toy — labeled as "decorative"), collector and desk-accessory buyers.

### Estimated demand
Etsy "articulated animal 3D printed" and "flexi dragon 3D print" return **2,000–5,000+ active listings**. Top flexi dragon listings show 21,000+ all-time sales (the Flexi Mech Dragon). Articulated axolotls, turtles, and snakes each have listings with 1,000–5,000+ reviews. The category is high volume but thinned after Etsy's June 2025 policy (many sellers ran licensed STL files and were removed). Original-design sellers now have less competition.

**Price range:** $8–$18 single figures; $30–$55 for bundles. Silk PLA or glow-in-dark variants command $3–$6 premium.

### Printability score: 8/10
- **Complexity:** Medium-high on design (articulated hinges require careful tolerance), but once calibrated it's a zero-post-process print.
- **Supports:** None if designed correctly — in-place hinges print over a 0.2–0.3mm gap.
- **Print time:** 45–90 minutes per figure. Batching 4–6 on a plate reduces effective time to 15–25 min/figure.
- **AMS upside:** Significant. Multi-color articulated figures (e.g., axolotl with pink gills + dark body) command 30–50% price premium. AMS is a genuine competitive moat here.

### Margin estimate

| Item | Single figure, silk PLA gradient (~55g) |
|---|---|
| Filament cost (55g silk PLA @ $0.018/g) | $0.99 |
| Packaging (padded mailer) | $0.80 |
| Etsy fees on $16 sale (~16.8%) | $2.69 |
| **Total COGS + fees** | **$4.48** |
| Sell price | $16.00 |
| **Net margin** | **~72%** |

5-pack bundle at $50: net margin ~76% on $5.20 total material + $2.50 packaging + $8.40 fees = $16.10 COGS.

### Uniqueness and differentiation angle
The IP risk culled the field significantly — original-design sellers now have structural SEO advantage. Differentiation: (1) silk/gradient AMS variants no single-color competitor can match; (2) a cohesive creature aesthetic line (matching design language across all figures); (3) bundle packaging that looks gift-ready in photos.

### Risk
- **IP:** Critical — do not design anything visually evocative of Toothless, Pokemon, or other active enforcement targets. "Geometric axolotl" and "faceted sea turtle" are safe. Character-inspired = not safe.
- **Design time:** Each figure requires more CadQuery work than a cable clip (articulated hinges are complex). Budget 2–4 hours per creature design.
- **Price competition:** The bottom end of this market is price-raced to $5–$8. Do not compete there — differentiate on multi-color and original design to hold $14–$18 floor.

---

## Candidate 6: Custom Plant Pot Labels and Garden Stake Sets

### Product description
Outdoor garden stake markers for labeling plants, herbs, vegetables, and flowers. Flag-style or tombstone-style stake with embossed or raised custom text (plant name, or buyer-specified names). Printed in ASA (UV-resistant, 5+ year outdoor life). Sold in sets of 6, 10, or 20 with customized names at checkout via Etsy personalization field. Also a "standard herb set" (BASIL, THYME, ROSEMARY, etc.) for buyers who don't want to type.

**Problem solved:** The stakes that come with seed packets fade and break after one season. Wire markers from garden centers feel flimsy. Custom, colorful, weatherproof named stakes are a gift item and a practical solution.

### Target market
Home gardeners (35–65 demographic, skews older than desk accessories), vegetable and herb gardeners, gift buyers for gardeners. Spring is the dominant purchasing season (Feb–May).

### Estimated demand
Etsy "3D printed plant markers," "custom garden labels," and "herb garden stakes" return **2,000–5,000+ active listings across all materials**. The 3D-printed subset is 300–600 listings. One top seller (custom garden markers with icon options) has strong review velocity at $3.99–$18 per set. **Spring 2026 purchase window is now — June is the tail end; September and February are the next peak windows.**

**Price range:** $3.99 single to $18–$28 for custom 10-pack.

### Printability score: 9/10
- **Complexity:** Low. Flat flag/tombstone stake shape, pointed end, embossed text via CadQuery text module.
- **Supports:** None. Slight taper on stake point prints cleanly at 45°.
- **Material:** ASA required for UV resistance. Print temp 240–250°C; P1S enclosure is required (compatible). Calibration print needed to establish profile. ASA at ~$0.025/g vs PLA+ $0.013/g — 92% more per gram but each stake uses only 5–12g, so per-unit impact is $0.06–$0.18 more.
- **Print time:** 8–15 minutes per stake. Plate of 20 stakes: 90–120 minutes total.

### Margin estimate

| Item | Set of 10 custom stakes (80g ASA) |
|---|---|
| Filament cost (80g ASA @ $0.025/g) | $2.00 |
| Packaging (poly mailer) | $0.80 |
| Etsy fees on $18 sale (~16.8%) | $3.02 |
| **Total COGS + fees** | **$5.82** |
| Sell price | $18.00 |
| **Net margin** | **~67.7%** |

The lowest margin of the candidates, but still strong. Custom text sets at $22 → net margin improves to ~71%.

### Uniqueness and differentiation angle
Custom-named sets are the differentiator — a buyer asking for their specific plant names cannot compare-shop. ASA material is a legitimate selling point over PLA+ competitors ("will last 5+ years outdoors, not 6 months").

### Risk
- **Seasonality:** Strong spring concentration means revenue will be lumpy. Build in October–November for gift season (herb garden sets are popular Christmas gifts for gardeners).
- **ASA profile setup:** One afternoon of calibration required. Not complex, just a new material profile on the P1S.
- **Competition:** Generic pre-labeled sets face price competition. Custom-text sets are protected.

---

## Candidate 7: Desk Phone and Tablet Stand System

### Product description
A parametric phone/tablet stand family: a phone cradle stand for MagSafe-compatible wireless charging (with cable pass-through), a landscape tablet stand (adjustable to 3 positions), and a hybrid phone + cable organizer combo. All original design. The MagSafe-compatible version has a recessed 52mm disc cutout in the back that aligns with Apple MagSafe charger puck (no licensed parts — the geometry is a functional accommodation, not a trademark).

**Problem solved:** Most 3D printed phone stands are generic and don't account for wireless charging. A stand designed specifically for MagSafe workflow addresses the 200M+ iPhone user base and is a mainstream Etsy search.

### Target market
iPhone users, remote workers, students, desk setup enthusiasts. Broad market. Also sells as a gift item.

### Estimated demand
Etsy "3D printed phone stand MagSafe" and "desk phone holder 3D printed" return **1,000–2,500+ active listings**. MagSafe-compatible designs are a growing sub-niche as MagSafe adoption expands. Price range: $12–$30 for single stands; $35–$55 for phone + cable organizer combo.

### Printability score: 8/10
- **Complexity:** Medium. The adjustable angle mechanism requires pivot geometry; MagSafe cutout requires precision (± 1mm tolerance on the 52mm disc recess).
- **Supports:** Minimal — only on the angle-adjustment slot if designed with bridging overhang. Solvable with geometry.
- **Print time:** 40–75 minutes per stand.
- **Material:** PETG preferred for daily-use durability.

### Margin estimate

| Item | MagSafe phone stand + cable organizer (~100g PETG) |
|---|---|
| Filament cost (100g PETG @ $0.016/g) | $1.60 |
| Packaging (padded mailer) | $1.00 |
| Etsy fees on $26 sale (~16.8%) | $4.37 |
| **Total COGS + fees** | **$6.97** |
| Sell price | $26.00 |
| **Net margin** | **~73.2%** |

### Uniqueness and differentiation angle
MagSafe-specific accommodations are a niche within a niche — many stand sellers don't design for wireless charging. "Works with MagSafe puck" is a searchable product attribute that filters out generic competitors.

### Risk
- **IP:** Moderate. Do not use Apple logos, "MagSafe" branding, or iPhone imagery in the listing title — use "compatible with MagSafe charger" language. The geometry accommodation is legal (functional fair use); the trademark is not yours to use freely.
- **Product fit:** As MagSafe evolves, design may need updates. Keep parametric parameters documented.

---

## Prioritized Candidate Summary

| Rank | Product | Etsy Listing Count | Price Range | Net Margin | Print Time | Time to Market | Key Risk |
|---|---|---|---|---|---|---|---|
| 1 | Custom Cookie Cutters | 5,000–10,000+ | $18–$45/set | ~74% | 8–20 min/cutter | 2 weeks | IP on character shapes |
| 2 | Magnetic Keyholder | 600–1,200 | $16–$45 | ~75% | 30–60 min | 3 weeks | Magnet lead time |
| 3 | Desk Cable Mgmt System | 2,000–4,000+ | $32–$65/bundle | ~76% | 15–40 min/piece | 3–4 weeks | Saturated category |
| 4 | Wall-Mount Organizer | 400–900 | $45–$80/set | ~73% | 25–50 min/module | 4 weeks | Structural QC |
| 5 | Flexi Animal Figures | 2,000–5,000+ | $16–$55 | ~72–76% | 45–90 min/figure | 4–6 weeks | IP design risk |
| 6 | Garden Plant Stakes | 300–600 (3D) | $18–$28/set | ~68–71% | 8–15 min/stake | 3 weeks | Spring seasonality |
| 7 | Phone/Tablet Stand | 1,000–2,500+ | $26–$55 | ~73% | 40–75 min | 3–4 weeks | IP (MagSafe branding) |

---

## Top Recommendation: Custom Cookie Cutters First

Cookie cutters represent the ideal Phase 2 launch because:

1. **Highest search volume** of all candidates (5,000–10,000+ Etsy listings = massive buyer pool)
2. **Fastest print time** (8–20 min each) — highest throughput per printer hour
3. **Personalization premium** — custom orders are immune to price comparison
4. **No new materials** — PETG is already a planned material for ModRun's PETG variant
5. **Gift occasion alignment** — Etsy's buyer base is gift-purchase motivated; cookie cutters fit perfectly
6. **Seasonal momentum** — the summer → fall → holiday baking season cycle means demand builds from July onward

**Pairing recommendation:** Launch cookie cutters and magnetic keyholders simultaneously. Cookie cutters demonstrate the shop's breadth; keyholders show functional home organization capability. These serve different Etsy buyer personas (baker/gift buyer vs. homeowner/organizer) and cross-list to different search intents, reducing listing cannibalization.

---

## Shared Production Advantages

All seven candidates share the same manufacturing infrastructure as ModRun:
- Bambu P1S printer (no new hardware for candidates 1–7)
- PLA+ or PETG filament (candidate 6 needs ASA — budget 1 afternoon for profile calibration)
- CadQuery parametric design workflow (text emboss module used in cookie cutters, stakes, and keyholders)
- Same poly mailer packaging (small and medium)
- Same Etsy shop infrastructure

**Only new BOM component:** N52 disc magnets for keyholders and bin labels (~$4–6/100 from AliExpress, 14–21 day lead time). Order immediately if pursuing candidates 2 and 7.

---

## Sources

- [Hyper3D: 15 Best Selling 3D Printed Items on Etsy 2026](https://hyper3d.ai/blog/best-selling-3d-printed-items)
- [Accio: Top Selling 3D Printed Items on Etsy](https://www.accio.com/business/top-selling-3d-printed-items-on-etsy)
- [Eufymake: 23 Best Selling 3D Printed Items 2026](https://www.eufymake.com/blogs/business-ideas/best-3d-print-sell-profitable-items)
- [Insight Agent: Best Selling 3D Printed Products on Etsy 2026](https://www.insightagent.app/guides/best-selling-3d-printed-items-etsy)
- [BakePress: Most Profitable 3D Print Items 2026](https://www.bakepress.com/blog/most-profitable-things-to-3d-print-and-sell)
- [Sloyd: Best-Selling 3D Printed Items 2025](https://www.sloyd.ai/blog/best-selling-3d-printed-items-in-2025---top-products-to-sell-60089)
- [PrintPal: Etsy 3D Printing Strategy for 2026](https://printpal.io/resources/3d-printing-strategy-to-make-1000s-on-etsy-in-2026)
- [Marmalead: Etsy Algorithm 2026](https://blog.marmalead.com/etsy-algorithm-2026/)
- [Seller Tools HQ: Etsy Algorithm 2026](https://sellertoolshq.com/guides/etsy-algorithm-2026/)
- [Etsy market/3d_printed_desk_accessories](https://www.etsy.com/market/3d_printed_desk_accessories) — live listing verification
- [Etsy market/magnetic_key_holder_wall_mount](https://www.etsy.com/market/magnetic_key_holder_wall_mount) — live listing verification
- [Etsy market/3d_printed_cookie_cutter](https://www.etsy.com/market/3d_printed_cookie_cutter) — live listing verification
- [mfg-farm/market-research.md](market-research.md) — margin baseline and Etsy fee structure
- [mfg-farm/product-expansion-research.md](product-expansion-research.md) — prior Phase 2 candidates (headphone hook, pegboard hooks, plant markers, riser legs, bin labels)
