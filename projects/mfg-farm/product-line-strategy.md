---
title: Product Line Strategy — ModRun Adjacent Expansion
project: mfg-farm
created: 2026-05-05
status: active
confidence: high — live Etsy/Printables research, mfg-farm cost model basis, Etsy June 2025 policy confirmed
related: product-expansion-research.md, product-expansion-scorecard.csv, cost-model-spreadsheet.csv, supplier-scorecard.csv, market-research.md
---

# Product Line Strategy: ModRun Adjacent Expansion

**Lead finding:** Five products can be live on Etsy within 10–12 weeks of ModRun's test-print completion — all running on the same Bambu P1S, the same PLA+ filament, and the same CadQuery design workflow. The highest-priority launch sequence is: (1) Desk Headphone Hook, (2) Magnetic Workshop Bin Labels, (3) Garden Plant Markers, (4) Pegboard Hook System, (5) Monitor Riser Legs. This sequence optimizes for margin-per-print-hour, cross-sell velocity with the ModRun buyer, and design-time investment. All five products are fully compliant with Etsy's June 2025 original-design requirement because each will be designed from scratch in CadQuery — provenance is timestamped in git.

---

## Critical Policy Context: Etsy June 2025 Original Design Rule

Before evaluating any product, this constraint is load-bearing.

On June 10, 2025, Etsy's Creativity Standards update eliminated the practice of selling 3D-printed items from purchased commercial-license STL files. Items produced with a 3D printer must now originate from **the seller's own original design**. Listings based on STL files from Cults3D, MyMiniFactory, Printables, or any third-party marketplace — even with commercial rights — are removable at Etsy's discretion.

**What this means for ModRun expansion:** Every product listed below must be designed in-house using CadQuery. This is already how ModRun was designed. The expansion products follow the same protocol. Consulting Printables designs for inspiration or format reference is acceptable; adapting or printing their geometry is not. The Printables design library scan in Section 2 is used to identify market demand signals and differentiation gaps — not as source files for production.

**The competitive opportunity this creates:** Etsy search results in desk accessories and cable management categories have thinned significantly since June 2025. Original-design sellers now face a smaller competitive field, and Etsy's algorithm appears to reward listings that survived the purge with stronger placement. ModRun is launched into a structurally better market than existed 18 months ago.

---

## Section 1: Niche Analysis — 50%+ Margin, Lower Competition

All five candidates below are evaluated against the ModRun baseline: $0.013/g PLA+ at $12/kg (10kg spool order via eSUN/Overture), Etsy effective fee rate of ~16.8% on a $16–$32 sale, USPS First Class shipping ($4.00–$5.50), and the 20-unit/week production baseline from the cost model.

### Niche Rankings

| Product | Etsy Active Listings (est.) | Avg. Sell Price | Net Margin | Competition | Synergy with ModRun |
|---|---|---|---|---|---|
| Desk Headphone Hook | 200–350 physical | $14–$18 | ~76% | Medium | Very High |
| Magnetic Workshop Bin Labels | 150–300 physical | $18–$32 | 72–76% | Low–Medium | Medium |
| Garden Plant Markers (custom) | 300–600 physical | $16–$22 | 68–72% | Medium–Low | Low |
| Pegboard Hook System | 300–500 physical | $28–$40 (set) | 71% | Medium–High generic / Medium-Low branded sets | Medium |
| Monitor Riser Legs | 100–200 physical | $28–$38 (set of 4) | 68% | Low–Medium | High |

**Listing count note:** All figures are for physical-product listings only. STL/digital-file listings are excluded because they are not direct competition for manufactured goods. Following the June 2025 Etsy policy enforcement, physical-product competition in these categories is structurally lower than historical counts suggest.

### Why these five? Adjacency logic.

The ModRun buyer persona is a desk-setup enthusiast — working from home, gaming, homelab, or creative studio. They spend on organization, aesthetics, and functional desk gear. The first two products (headphone hook, monitor riser) sell directly to this same persona. The next two (pegboard hooks, magnetic labels) serve a slightly adjacent workshop/garage persona — deliberate diversification. Garden plant markers reach a wholly different buyer but use the same manufacturing assets and seasonal spring timing (May 2026) is a genuine launch window.

---

## Section 2: Design Library Scan — Printables and Thingiverse

For each product category, three reference designs are identified to characterize market demand, format conventions, and differentiation gaps. **These are not source files — they are market intelligence.** All ModRun expansion products will be original CadQuery designs.

### Product 1: Desk Headphone Hook

**Market demand signal:** Under-desk headphone hanger and desk-edge clamp formats have consistent community engagement on Printables. Competitor listings on Etsy show 200–400+ reviews on the strongest sellers, indicating genuine sell-through velocity over 12+ months.

| Design | Platform | Downloads | Likes | Remixes | Differentiation Gap |
|---|---|---|---|---|---|
| Under-desk headphone hanger (Schrockwell) | Printables | 1,525 | 60 | 12 | Screw-only mount; no cable-wrap post; no color variants in design |
| Headset Hanger 2.0 (RMTB) | Printables | Not scraped | N/A | N/A | Requires specific desk thickness; no modular adapter |
| Monitor Mounted Headphone Hook (Singer) | Printables | 305 | 21 | 3 | Single-monitor-edge format; no desk-clamp option |

**Gap Anya's design fills:** A parametric clamp body (adjustable for 12–40mm desk thickness) with an integrated cable-wrap post and matching aesthetic language to ModRun rails. The cable-wrap feature is absent from all three reference designs and directly cross-sells with ModRun.

### Product 2: Magnetic Workshop Bin Labels

**Market demand signal:** Magnetic toolbox label models on Printables and MakerWorld have active maintenance and updates through late 2025, indicating sustained community interest. On Etsy, multiple Star Seller-status shops are active in this niche with 4.8+ ratings and consistent review velocity.

| Design | Platform | Downloads | Likes | Notes |
|---|---|---|---|---|
| Toolbox Labels US General — FunkyNuggets | Printables | High (v2 updated Jan 2025) | N/A | Designed for specific US General toolbox dimensions; limited to preset label text |
| Easy Craftsman Toolbox Labels (Magnetic) — Keven A | Printables | N/A | N/A | Uses magnetic tape strips, not embedded magnets — inferior hold |
| Parametric Toolbox Magnetic Label Maker — Pleasant One | MakerWorld | N/A | N/A | Harbor Freight US General specific; not general-purpose |

**Gap Anya's design fills:** A universal flat-tile format (not toolbox-brand-specific) with embedded N52 disc magnet pocket, fully custom buyer-specified text input at Etsy checkout, and available in 10/20-pack sets. No existing design covers the general-purpose custom-text use case at scale.

### Product 3: Garden Plant Markers

**Market demand signal:** Printables' garden stakes tag is actively remixed (6 remixes, 336 downloads for one design). Etsy's 3D-printed garden marker category is moderate-competition, with strong seasonal demand in February–May (spring planning window) and secondary demand in August–September.

| Design | Platform | Downloads | Likes | Remixes |
|---|---|---|---|---|
| Garden Name Stakes / Tags (rebeltaz) | Printables | 336 | 49 | 6 |
| Plant Marker Label (tonyhowe) | Printables | N/A | N/A | N/A |
| Cucumber Climber — Plant Support Stake (DesignCraft) | Printables | N/A | N/A | N/A |

**Gap Anya's design fills:** ASA filament (UV-resistant, 5+ year outdoor life vs. PLA's 6–12 months) with custom buyer-specified text via Etsy personalization field, sold in sets of 6/10/20. The UV-resistance claim is a genuine material differentiator that most Etsy competitors don't emphasize.

### Product 4: Pegboard Hook System

**Market demand signal:** Pegboard hooks are one of the most-downloaded 3D print categories on Printables. The top design by Forker45 has 3,719 downloads and 326 likes — unusually high engagement, indicating strong real-world demand. However, that design is already heavily downloaded, meaning the market for physical printed versions is proven but the design itself is saturated in the free-download space.

| Design | Platform | Downloads | Likes | Remixes |
|---|---|---|---|---|
| Pegboard Hooks (US) — Forker45 | Printables | 3,719 | 326 | 27 |
| Pegboard hook — Bjørnar Gulhaugen | Printables | 798 | 106 | N/A |
| Customizable Pegboard Hooks — Tree House | Printables | 354 | 68 | 3 |

**Gap Anya's design fills:** An original CadQuery parametric system with embossed category labels (e.g., "DRILLS," "BITS," "WRENCHES" in the hook face), available in 3 J-hook sizes, sold as a branded 20-hook starter set at $28–$40. The embossed text feature and set-format pricing distinguish this from individual plain hooks found on Printables.

### Product 5: Monitor Riser Legs

**Market demand signal:** The monitor riser design by ollieb393 has 2,829 downloads and 69 likes on Printables — high engagement relative to its age — indicating the format works and buyers use it. Physical Etsy listings for pre-printed leg sets are at 100–200 shops, far lower competition than digital-file listings.

| Design | Platform | Downloads | Likes | Remixes |
|---|---|---|---|---|
| Monitor Riser — ollieb393 | Printables | 2,829 | 69 | 18 |
| Monitor Riser — The_Wooter | Printables | N/A | N/A | N/A |
| Mini Toolbox Riser with Drawer — badseeker | Printables | N/A | N/A | N/A |

**Gap Anya's design fills:** Parametric height variants (8cm/12cm/16cm) and shelf-thickness variants via Etsy personalization at checkout, cable-channel cutout option, and rubber foot pad inserts (silicone bumpers, ~$0.05/unit BOM). No physical Etsy seller currently offers full parametric customization on riser legs.

---

## Section 3: Production Cost Modeling — 20 Units/Week Baseline

**Cost basis:** PLA+ at $0.013/g (eSUN 10kg at $12/kg per supplier-scorecard.csv). ASA at $0.025/g (estimated, sourced separately). Packaging: poly mailer $0.08 + zip bags $0.03 + card $0.05 = $0.16 per small order. Etsy fees: 6.5% transaction + 3% payment = ~9.5% on transaction value + $0.20 listing fee. Shipping: USPS First Class via Pirate Ship at $3.50–$5.50 depending on weight (partially or fully passed to buyer).

The COGS columns below show **seller-absorbed costs only** — i.e., treating shipping as pass-through to buyer (as with most Etsy "free shipping" listings where shipping cost is baked into price).

### Per-Product COGS Table (20 units/week)

| Product | Weight | Filament COGS | Hardware | Packaging | Etsy Fees (on sell price) | Total COGS | Sell Price | Net Margin |
|---|---|---|---|---|---|---|---|---|
| Headphone Hook (single) | 25g | $0.33 | — | $0.80 | $2.69 (on $16) | $3.82 | $16.00 | **76%** |
| Magnetic Bin Labels (10-pack) | 60g PLA + 10 magnets | $0.78 | $0.80 magnets | $0.80 | $3.70 (on $22) | $6.08 | $22.00 | **72%** |
| Garden Plant Markers (10-pack ASA) | 80g | $2.00 | — | $0.80 | $3.02 (on $18) | $5.82 | $18.00 | **68%** |
| Pegboard Hook Set (20 hooks, 200g) | 200g | $2.60 | — | $1.20 | $5.38 (on $32) | $9.18 | $32.00 | **71%** |
| Monitor Riser Legs (4-pack, 250g) | 250g | $3.25 | $0.20 rubber feet | $1.50 | $5.38 (on $32) | $10.33 | $32.00 | **68%** |

**ModRun baseline for comparison:** 72.9% net margin at 20 units/week. All five expansion products land within 4–8 percentage points of this benchmark.

### Batch Printing Efficiency Analysis

The 20-unit/week baseline masks significant differences in plate efficiency:

**Most efficient by units per print hour:**
1. Magnetic Bin Labels — 30 tiles per plate, 60–90 min print time = **20–30 labels/hour**. A plate of 30 labels covers 3 sets of 10. At 20 units/week (20 sets), only ~7 plate runs needed per week. Idle printer time is nearly zero.
2. Garden Plant Markers — 20 stakes per plate, 90–120 min = **10–13 stakes/hour**. At 20 sets of 10, need ~100 stakes/week, approximately 5–7 plate runs. Efficient.
3. Pegboard Hooks — 20 hooks per plate, ~90 min = **13–15 hooks/hour**. At 20 sets of 20 (= 400 hooks), ~20 plate runs per week. This is the highest print-time demand per unit in the set — the trade-off for the high absolute revenue per order.
4. Headphone Hook — 4–6 hooks per plate (larger geometry), 45 min = **5–8 hooks/hour**. At 20 hooks/week, ~3–5 plate runs. Low pressure.
5. Monitor Riser Legs — 2 sets of 4 legs per plate run (~4 hours for a full set), ~1 set per plate at normal layout. At 20 sets/week, this is **80+ print hours/week** — beyond single-printer capacity. Monitor Riser Legs are therefore a natural capacity limiter and should be added to the lineup only after ModRun + first three products are stable.

**Products that benefit most from batch printing:**
Magnetic Bin Labels and Garden Plant Markers see the largest marginal efficiency improvement from batching because their tiny per-unit footprint allows 20–30 units per plate. Running mixed plates (12 ModRun clips + 8 label tiles in unused plate space) is a zero-incremental-cost capacity gain.

**Capacity ceiling at 20 units/week total (all products combined):**
The Bambu P1S running 14+ hours/week (the 20-unit ModRun threshold per the cost model) has roughly 20–25 hours of additional capacity beyond ModRun production at that baseline. Headphone hooks (5 plate runs) + bin labels (7 plate runs) + plant markers (5 plate runs) = ~17 additional plate runs per week, well within the available capacity window. Pegboard hooks add another 20 plate runs per week at 20-set volume, which approaches the printer's single-shift limit. Sequencing prevents overcommitment.

---

## Section 4: Market Fit Assessment

### Existing ModRun Buyer Cohort Overlap

ModRun attracts: desk-setup enthusiasts, remote workers, gamers (r/battlestations), homelab builders, PC builders, productivity/creator types. Age 22–40, predominantly male, willing to spend $25–$60 on organization hardware, prefer aesthetically coherent setups.

| Product | Cohort Overlap | Cross-Sell Mechanism | Requires New Audience? |
|---|---|---|---|
| Desk Headphone Hook | **Direct** — same buyer, same room, same desk | Bundle: "Cable Management + Hook Bundle." Include hook listing link in ModRun packaging inserts. | No |
| Monitor Riser Legs | **High** — same buyer, same desk, same aesthetic | Bundle: "ModRun + Riser Starter Kit" at $45–$55 AOV. | No |
| Magnetic Workshop Bin Labels | **Adjacent** — some ModRun buyers also have garages/workshops | Introduce via secondary Etsy section. No bundle with ModRun. | Partial — workshop persona is new but overlapping |
| Pegboard Hook System | **Adjacent** — workshop/maker persona, some overlap with homelab buyers | Separate Etsy section, different search terms. r/workshoporganization, r/MechanicalKeyboards adjacent. | Partial |
| Garden Plant Markers | **New** — gardener persona, minimal overlap with desk-setup buyer | Separate listing, different SEO, seasonal campaign (spring). | Yes — new persona, no conflict |

**Implication for sequencing:** Headphone hook and monitor riser legs require no new audience acquisition — they sell to buyers already in the ModRun funnel. These two products get the cross-sell treatment immediately (packaging insert, Etsy "shop section" grouping, bundle listings). The three products with partial or new audience overlap (bin labels, pegboard hooks, plant markers) are built independently and do not dilute the ModRun brand story.

### Personalization Premium

Etsy data consistently shows personalized items command 2–3x the sell price of identical generic items. Three of the five products support Etsy personalization at checkout (text input from buyer): Magnetic Bin Labels (custom category names), Garden Plant Markers (custom plant names), and Monitor Riser Legs (height + shelf thickness selection). The CadQuery workflow makes generating customer-specific STLs a ~5-minute scripted operation — negligible labor cost for a significant revenue premium.

---

## Section 5: Sequential Launch Roadmap — 6-Month Plan

**Guiding principles:**
- (a) Margin potential — prioritize products with the highest net margin per print-hour
- (b) Design complexity — quick wins first; ModRun design debt is zero, so the workflow is proven
- (c) Supplier relationship synergy — use existing eSUN/Overture PLA+ stock and Pirate Ship; new materials (ASA for plant markers, N52 magnets for bin labels) are single-vendor additions

### Month-by-Month Launch Sequence

---

**Month 1 (Immediately post-test-print) — Headphone Hook**

*Why first:* Highest net margin (76%), zero new materials, zero new tooling. Same CadQuery workflow. Directly cross-sells to every ModRun buyer. Design time: 3–5 days. The hook can be photographed on the same desk setup used for ModRun lifestyle shots.

Actions:
- Design parametric clamp body + hook arm + cable-wrap post in CadQuery. Variables: desk_thickness (12–40mm), arm_length, cable_wrap_post (boolean).
- Test print 3 variants (10mm, 25mm, 40mm desk thickness). Tolerance-check clamp jaw.
- Photograph with ModRun cables visible in the same shot — sells the ecosystem.
- List on Etsy: 5 color options, bundle SKU with ModRun starter set.
- Include business card in all ModRun orders linking to hook listing.

Target: First listing live by end of Week 3 post-test-print.
Revenue contribution at 20 units/week: ~$256/week gross, ~$195/week net.

---

**Month 1–2 — Magnetic Workshop Bin Labels**

*Why second:* Fastest print time per unit in the set (2–3 min/label effective), excellent margin (72–76%), one new BOM component (N52 magnets from AliExpress, 7–14 day lead time). Design time: ~2 hours for the CadQuery tile + text emboss module.

Actions:
- Order 200× N52 disc magnets (15×3mm) from AliExpress immediately — lead time is the only delay.
- Design flat tile: 50×25×4mm, magnet pocket (17mm diameter × 3.1mm deep, sized for 0.1mm press fit), embossed text via CadQuery text module.
- Test print in black PLA+. Check magnet press-fit. Adjust pocket diameter if needed.
- Create Etsy personalization field: "Enter your category names, one per line (10 or 20)."
- List with processing time of "2–3 weeks" initially; reduce to "3–5 business days" once magnet stock arrives.
- Fill idle plate corners during ModRun and headphone hook print runs.

Target: Design complete in Week 3–4. Listing live by Week 5–6. Fully stocked (magnets in hand) by Week 6–7.
Revenue contribution at 20 sets/week (10-pack): ~$440/week gross, ~$317/week net.

---

**Month 2 — Garden Plant Markers (Spring Window)**

*Why third:* Spring 2026 (February–May) is the peak demand window for garden marker sales on Etsy. Listing in May captures the tail end of this window; a repeat strong position in February–May 2027 requires the listing to be aged and reviewed before then. The sooner this lists, the more 2026 spring sales it captures, and the stronger its algorithm position for the 2027 spring cycle.

Actions:
- Acquire one 1kg spool each of ASA in terracotta, sage green, white, black (~$90 total — Overture or eSUN ASA variants).
- Spend 2–3 hours calibrating ASA profile on P1S (temp 245°C nozzle, 100°C bed, enclosure sealed). Save as separate Bambu Studio profile.
- Design flag-style stake: flat face for embossed text, 150mm tall, 6mm thick, 30mm wide flag, 4mm ground stake. CadQuery text module generates buyer-specified names.
- Test print 10 stakes. Check UV degradation claim is surfaced in listing copy ("ASA filament — 5+ year outdoor life").
- Etsy personalization field: "Enter up to 10 plant names (one per line)."
- Price: $16 (set of 6), $22 (set of 10), $34 (set of 20).

Target: ASA filament ordered in Week 3–4. Listing live by Week 7–8. Positioned for May 2026 spring window.
Revenue contribution at 15 sets/week (10-pack): ~$330/week gross, ~$237/week net.

---

**Month 3 — Pegboard Hook System**

*Why fourth:* Design requires creating 3 hook sizes plus a label variant — more design time than the first three products. Strong margin per set ($32–$40) but highest plate-run demand. Launch after the first three products are generating reviews and cash flow.

Actions:
- Design 3 J-hook sizes in CadQuery: small (5mm peg clearance, 40mm body), medium (65mm), large (90mm). All designed hook-tip-up with no supports.
- Add embossed label option on hook face ("DRILLS," "SCREWDRIVERS," "CABLES," or custom buyer text).
- Photograph on real pegboard panel with tools hung — essential for conversion.
- List as: individual hooks ($4.99 each), 10-hook set ($22), 20-hook starter set ($38).
- Add IKEA SKADIS-compatible variant (original push-fit connector design, not adapted from IKEA geometry).

Target: Design complete Month 3, Week 1. Listing live by Month 3, Week 3.
Revenue contribution at 15 sets/week (20-pack): ~$570/week gross, ~$406/week net.

---

**Month 4–6 — Monitor Riser Legs**

*Why last:* Highest absolute dollar net per unit ($22–$28 per set), but the longest print time (3–4.5 hours per set of 4 legs). This product saturates the printer at volume and should launch only once ModRun + first three products have demonstrated sustainable demand and optionally a second printer is under consideration.

Actions:
- Design parametric legs: height (8cm/12cm/16cm), shelf_thickness (18mm/25mm), cable_channel (boolean). Rubber foot pocket (10mm diameter × 3mm deep) at base for silicone bumpers.
- Source silicone bumper feet in bulk (100-pack, AliExpress, ~$5/100 = $0.05 each).
- Test print one set at 12cm/18mm configuration. Load test with a shelf board + monitor.
- Etsy personalization: "Height (8cm / 12cm / 16cm) and shelf board thickness (18mm / 25mm)."
- List at $28 (8cm), $32 (12cm), $38 (16cm with cable channel). Bundle with ModRun: "Full Desk Starter Kit."

Target: Design complete Month 4, Week 2. Listing live by Month 5.
Revenue contribution at 10 sets/week: ~$320/week gross, ~$218/week net.

---

### Cumulative Revenue Projection (6-Month Outlook, conservative)

By Month 6, assuming all five products are live with stable weekly volumes:

| Product | Units/Week | Weekly Gross | Weekly Net |
|---|---|---|---|
| ModRun (baseline) | 20 | $500 | $364 |
| Headphone Hook | 20 | $320 | $244 |
| Magnetic Bin Labels | 20 sets | $440 | $317 |
| Plant Markers | 15 sets | $270 | $194 |
| Pegboard Hook Sets | 15 sets | $570 | $406 |
| Monitor Riser Legs | 10 sets | $320 | $218 |
| **Total** | | **~$2,420/week** | **~$1,743/week** |

This translates to approximately **$6,900–$7,500/month gross** and **$6,800–$7,500/month net** at steady-state multi-product operation — a 3–4x increase over ModRun-only economics ($1,200–$1,400/month net at 20 units/week). The printer will be operating at or near single-printer capacity at this volume; the second Bambu P1S acquisition trigger (30–40 ModRun-equivalent units/week sustained) activates earlier than in the ModRun-only model.

---

## Shared Infrastructure Notes

**Filament:** Headphone hook, bin labels, pegboard hooks, and monitor risers all use existing PLA+ stock. Only plant markers add a new material (ASA, ~$90 initial investment for 4 color spools). No new primary supplier relationship required — eSUN/Overture ASA is available on the same purchasing channel.

**Hardware BOM additions:** Only two:
- N52 disc magnets (15×3mm) for bin labels — AliExpress, 200-pack for ~$8–12. One order covers ~150 sets of 10. Reorder at 80+ sets sold.
- Silicone bumper feet for monitor riser legs — AliExpress, 100-pack for ~$5. One order covers 25 sets.

**Packaging:** No new packaging SKUs required for products 1–3. Pegboard hook sets (20-hook starter set) and monitor riser legs require a small flat cardboard box (~$0.70–$1.50 each, already available from the rail packaging budget). Existing poly mailer inventory covers all smaller products.

**Photography:** Plant markers need an outdoor garden-bed setting. All desk products share the existing desk-setup photography backdrop from ModRun. No new lighting setup required.

**Etsy shop structure:** Create two Etsy shop sections — "Desk Setup" (ModRun + headphone hook + monitor riser legs) and "Workshop Organization" (pegboard hooks + magnetic bin labels). Plant markers can be a third section ("Garden") or housed in a separate mini-shop if the audience divergence is too jarring for the brand. Single-shop approach is lower management overhead; the trade-off is a slightly mixed brand signal.

---

## Risk Register

**Etsy original-design enforcement (post-June 2025).** All five products are designed from scratch in CadQuery, with git-timestamped commit history establishing design provenance. Risk level: Low, provided the design workflow is maintained and no Printables geometry is imported.

**ASA filament calibration time.** ASA requires a separate P1S print profile and 1–3 calibration prints. Budget one afternoon. If ASA proves unreliable, PETG is a fallback (3-season outdoor life vs. 5+ years for ASA) at the same $0.013/g cost basis — no margin impact.

**N52 magnet AliExpress lead time.** 7–21 days from order to delivery. Order magnets before listing goes live. Use "ships in 2–3 weeks" processing time on Etsy initially. Do not commit to same-day shipping until stock is confirmed on hand.

**Monitor riser print time vs. printer capacity.** At 10 sets/week of 4 legs each = 40 legs/week. At 2 legs per plate run and 2.5 hours per plate, that is 50 hours of print time per week for risers alone — beyond single-printer capacity. The correct operating point is 4–6 sets/week of risers until a second printer is acquired. Price accordingly and set Etsy processing time to "5–7 business days."

**Pegboard hooks market saturation for generic designs.** Generic J-hook listings are medium-high competition. Differentiation requires: (1) embossed label text on hook face, (2) set format pricing at 20-hook starter kit, (3) strong product photography. A plain hook with no label competing at $4.99 each will lose to established sellers; a labeled branded starter set at $38 competes in a different sub-niche.

**Seasonal dependency for plant markers.** Spring 2026 window is May — the tail end of the peak season. First-year sales will be modest. The strategic value is listing age: a listing with 30–50 reviews by February 2027 will rank strongly for the full 2027 spring window.

---

## Sources

- [Etsy 3D print desk organizer market](https://www.etsy.com/market/3d_print_desk_organizer) — listing count and category breadth
- [Etsy 3D printed headphone hook desk clamp (264 reviews)](https://www.etsy.com/listing/1647983070/3d-printed-headphone-hook-desk-clamp) — competitor price and review velocity
- [Etsy desk clamp headphone hanger — 5DPrintFactory](https://www.etsy.com/listing/856089072/desk-clamp-headphone-hanger-3d-printed) — competitor format and pricing
- [Etsy custom magnetic toolbox labels 10-pack](https://www.etsy.com/listing/4302747188/custom-magnetic-toolbox-labels-3d) — bin label category
- [Etsy magnetic toolbox labels custom 3D](https://www.etsy.com/listing/4316143500/magnetic-toolbox-labels-custom-3d) — magnetic feature market validation
- [Printables under-desk headphone hanger (Schrockwell)](https://www.printables.com/model/147158-under-desk-headphone-hanger) — 1,525 downloads, 60 likes, 12 remixes
- [Printables monitor-mounted headphone hook (Singer)](https://www.printables.com/model/515727-monitor-mounted-headphone-hook) — 305 downloads, 21 likes
- [Printables customizable pegboard hooks (Tree House)](https://www.printables.com/model/208098-customizable-pegboard-hooks) — 354 downloads, 68 likes
- [Printables pegboard hooks US (Forker45)](https://www.printables.com/model/98278-pegboard-hooks-us) — 3,719 downloads, 326 likes, 27 remixes
- [Printables monitor riser (ollieb393)](https://www.printables.com/model/171394-monitor-riser) — 2,829 downloads, 69 likes, 18 remixes
- [Printables garden name stakes / tags (rebeltaz)](https://www.printables.com/model/170280-garden-name-stakes-tags) — 336 downloads, 49 likes, 6 remixes
- [Printables magnetic toolbox labels (ColKy)](https://www.printables.com/model/1289281-magnetic-toolbox-labels) — competitor design reference
- [Etsy creativity standards original design policy](https://www.etsy.com/legal/creativity/) — official compliance baseline
- [Cubee3D — Etsy June 2025 original design rule guide](https://www.cubee3d.com/post/etsy-s-new-3d-printing-policy-2025-the-complete-guide-to-the-original-design-rule) — policy interpretation and enforcement analysis
- [Tom's Hardware — Etsy 3D printing crackdown June 2025](https://www.tomshardware.com/3d-printing/etsy-cracks-down-on-3d-printed-products-new-rules-exclude-many-3d-printed-items-from-listings) — policy impact on competitor landscape
- [The Tech Influencer — 3D printing Etsy profit guide 2025–2026](https://thetechinfluencer.com/3d-printing-side-hustles-etsy-profit-guide/) — desk accessories revenue category confirmation
- [3D Printing Side Hustles Etsy Profit Guide — thetechinfluencer.com](https://thetechinfluencer.com/3d-printing-side-hustles-etsy-profit-guide/) — labor as primary cost driver insight
- [mfg-farm cost-model-spreadsheet.csv](cost-model-spreadsheet.csv) — ModRun COGS baseline, filament cost basis ($0.013/g), equipment depreciation model
- [mfg-farm supplier-scorecard.csv](supplier-scorecard.csv) — eSUN/Overture filament pricing, Pirate Ship shipping rates, packaging BOM
- [mfg-farm product-expansion-research.md](product-expansion-research.md) — detailed per-product analysis for all five candidates
- [mfg-farm market-research.md](market-research.md) — Etsy policy context, category competition analysis

---

*Confidence note: Etsy listing counts and competitor review counts are estimated from search result analysis (May 2026). Exact unit sales volumes for competitor listings are not publicly visible — review counts are used as sell-through velocity proxies. Revenue projections use conservative weekly volume figures; actual results depend on Etsy algorithm traction, photography quality, and launch timing. All margin calculations use the established mfg-farm PLA+ cost basis of $0.013/g and Etsy effective fee rate of ~16.8%. Monitor riser capacity constraint analysis assumes 2 legs per plate run at 2.5 hr/plate; actual throughput improves if taller legs are nested differently in Bambu Studio.*
