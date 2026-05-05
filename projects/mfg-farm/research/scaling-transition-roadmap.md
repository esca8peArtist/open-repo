---
title: Scaling Transition Roadmap — ModRun 20 to 100+ Units/Week
date: 2026-05-05
status: production-ready
tags: [mfg-farm, modrun, roadmap, scaling, milestones, hiring, capital-planning]
confidence: high
related: 100-unit-operations-blueprint.md, ../production-scaling-research.md, ../workforce-scaling-research.md, ../post-test-print-launch-prep.md
---

# Scaling Transition Roadmap: ModRun 20 → 100+ Units/Week

**Lead finding:** The single most common failure mode in small 3D print businesses is not technical — it is capital sequencing. Operators buy hardware before demand is proven, carry excess inventory before the SKU mix is known, and hire before revenue is consistent. This roadmap sequences every decision against a demand validation gate: no capital expenditure without two consecutive weeks of demonstrated throughput pressure at the existing configuration.

The test print is the prerequisite to everything below. Nothing in this roadmap is actionable until the test print validates snap arm function, FDM_TOLERANCE calibration, and print orientation. Treat the test print as your Phase 0 gate, not a formality.

---

## Phase 0: Test Print Validation (Pre-Month 1)

**Objective:** Confirm the physical product works before any production investment.

**Key tasks:**
- Print one clip (6mm bore) and one rail (desk_clamp variant) at production settings: 0.20mm layer height, 3 walls, 20% gyroid infill, 222°C nozzle, 55°C bed, minimum layer time 8 seconds.
- Functional tests: (1) clip snaps into rail slot with audible click, no binding, no rattle; (2) 6mm cable seats in bore and is retained without forcing; (3) snap arm survives 5 insertion/removal cycles without cracking or permanent deformation; (4) desk_clamp rail grips a test desk edge without slipping under moderate hand pressure.
- Dimensional check: verify FDM_TOLERANCE = 0.15mm gives correct clip-to-rail fit. If the clip binds (too tight), increment to 0.20mm. If it rattles (too loose), reduce to 0.10mm. Re-export STL from CadQuery and re-slice before any production run.
- Document the passing print settings as `ModRun-PLA-Production-v1` in Bambu Studio. Version-lock the profile. Any future production deviation is a new version increment, not an ad-hoc adjustment.

**Gate criteria to proceed:** All four functional tests pass. If any fail, diagnose, adjust CadQuery parameters, reprint. Do not proceed to Month 1 until the product is physically validated.

**Risk if you skip this gate:** Every unit produced before tolerance calibration is either scrap (if too tight) or a customer return (if too loose). At 20 units/week, that is $300–$700 in wasted revenue in the first month.

---

## Month 1: Etsy Launch + 20-Unit/Week Baseline

**Target throughput:** 20 units/week (12 clips + 8 rails, approximately)

**Operations:**
- Single Bambu P1S. Solo operator. 3–4 hours/day of active operations time.
- Schedule: 1 overnight clip batch per week (1 plate × 12 clips = one overnight run), 4 rail plates per week (run in 3-hour afternoon slots on alternating days).
- Print time: approximately 26 hours/week at this mix. Printer running at ~23% of capacity — not a bottleneck.
- Post-processing: 5–8 seconds per clip (visual inspect + bin), 40–50 seconds per rail (slot deburring + inspect). Total post-processing: under 15 minutes per week.
- Packaging: 90–120 seconds per order. At 20 units = roughly 8–10 orders/week, total packaging: 15–25 minutes per week.

**Sales and listing:**
- Etsy shop live with 3 primary listings: 3-clip bundle ($24.99), individual clip ($9.99), desk_clamp rail ($34.99).
- Listing photography: minimum 5 images per listing — one in-use lifestyle shot (cable routing under a desk or behind a monitor), one on a white background with scale reference, one close-up of snap fit, one showing the clip-on-rail system, one showing installation.
- SEO: titles include "cable clip," "desk cable management," "cable organizer," "3D printed cable clip," "rail mount cable clip." Etsy's search ranking weights recency; list all variants within the first 48 hours.
- Pricing includes free shipping (build shipping cost into product price). Etsy research consistently shows free shipping improves conversion rate more than equivalent price reductions for sub-$50 products.

**Supplier setup:**
- Filament: eSUN PLA+ black and grey, 2 spools each, Amazon Prime. Total: ~$60.
- Packaging: 100 poly mailers ($6–10), 50 small corrugated boxes for rails ($8–12), zip-lock bags for clip bundles ($3–5), Pirate Ship account (free).
- Tools: digital calipers ($15–25), test cable at each bore diameter sold, IPA wipes for bed cleaning, replacement PEI plate on order (lead time 1–2 weeks).

**Key metric to establish in Month 1:**
- Orders fulfilled on time: target 100%.
- Scrap rate: log every plate run. If above 8% after week 2, diagnose before scaling.
- Printer utilization hours/day: log this. It is the primary signal for when to add a printer.

**Month 1 financial target:** 20 units/week × 4.3 weeks = 86 units. At blended ASP of ~$28/order (mix of bundles and rails): approximately $2,400 gross revenue. Net after fees, shipping, and COGS: approximately $1,200–$1,500. Startup capital recovery begins in Month 1.

**Risks to manage:**
- Under-priced listings: resist the urge to discount to generate early sales. At this margin structure, a 20% discount costs more than one extra sale.
- Over-production of unsold inventory: until you have 10+ sales and real demand signals, do not print ahead more than 1 week of stock.
- Test-print issues discovered after listing launch: maintain a "processing time: 3–5 business days" buffer on Etsy so you have room to reprint a replacement if the first production run reveals a tolerance issue.

---

## Month 2: Iterate + Feedback Loop

**Target throughput:** 20–30 units/week (demand-dependent)

**Focus:** Operational refinement, not scaling.

**Key activities:**
- Customer feedback integration: read every Etsy message and review. Any complaint about fit, durability, or usability is a product signal. Three complaints of the same type = a design revision candidate.
- Photography upgrade: if conversion rate on the clip listing is below 3%, reshoot with improved staging. Poor photography is a more common early revenue constraint than product quality.
- Packaging iteration: try both branded thank-you card inserts and no-insert; track review mention of packaging. High-quality packaging correlates with 5-star review mentions.
- Etsy SEO iteration: use Etsy's search analytics (available after 30+ days) to identify which search terms are driving traffic vs. converting. Revise titles and tags based on this data, not assumptions.
- Establish the production log: date, printer, plate config, units produced, pass/fail count, failure mode, filament lot. 30 seconds per plate run. This data becomes essential when troubleshooting at 50+ units/week.

**Decision point: Is demand growing?**
- If week-4 orders are higher than week-1 orders: strong signal. Continue refining, do not scale hardware yet.
- If orders have flatlined at 0–3/week after 30 days: SEO or photography problem, not a production problem. Do not add printers. Fix the listing.
- If printer is running 10+ hours/day for two consecutive weeks: note the date. This is the earliest possible trigger for a second printer, though Month 4–5 is the more likely timing.

**Financial target Month 2:** Same as Month 1 or slightly higher as early SEO compounds. First positive reviews should arrive this month — each 5-star review meaningfully improves Etsy search ranking for a new shop. Target: 5+ reviews by end of Month 2.

---

## Month 3: 50-Unit/Week Threshold + Part-Time Contractor

**Target throughput:** 50 units/week (add second printer if single-printer utilization is at capacity)

**Hardware decision:**
- Add second Bambu P1S only if the first printer has run 14+ hours/day for two consecutive weeks AND orders are being delayed due to production capacity.
- If demand is organically growing toward 50 units/week without printer pressure, hold the hardware decision one more month.
- Second printer cost: $699. Payback at 50 units/week incremental throughput: 3–5 weeks. Do not agonize over this decision; the math is clear once demand is demonstrated.

**Multi-channel expansion:**
- Amazon Handmade listing: submit within 30 days of 10+ Etsy reviews. Amazon Handmade provides exposure to buyers who do not shop Etsy. Fulfillment remains self-handled (not FBA) until you are consistently producing 50+ units/week and want to decouple packaging from your schedule.
- Pricing on Amazon: set 10–15% higher than Etsy to account for Amazon's slightly higher fee structure and to avoid Etsy/Amazon price parity issues.

**Labor:**
- If production + packaging + shipping exceeds 5 hours/day for two consecutive weeks, source a local 1099 packaging contractor (10 hrs/week, $15/hour, $600/month).
- Source: local maker space community board first, Nextdoor second. Do not hire without a written contractor agreement including NDA and QC checklist delivery.
- Contractor scope: packaging, labeling, visual QC (with laminated checklist). Not: print management, slicing, or any access to design files.
- Owner retains: print queue management, functional QC spot-checks, shipping batch upload, Etsy/Amazon account management, design work.

**Product identification:**
- By end of Month 3, you should have enough order data to identify: (a) which bore diameter sells most, (b) rail vs. clip revenue split, (c) whether adhesive or clamp rail dominates. Use this data to concentrate production on the top 2 SKUs and deprioritize slow movers.
- "Most popular product" is the anchor SKU for the next scaling decision. If clips dominate, your capacity constraint is different (clips are fast to print) than if rails dominate (rails are slow).

**Month 3 financial target:** 50 units/week × 4.3 weeks × $28 blended ASP = ~$6,020 gross revenue. Net after all costs including new printer depreciation: approximately $2,800–$3,500/month.

---

## Month 4–5: Winning Product Optimization + Secondary SKU Design

**Target throughput:** 50 units/week (hold at this level, optimize before scaling further)

**Key focus: Deepen, not widen.**

This is the most commonly skipped step in small print businesses. Operators hit 50 units/week and immediately try to jump to 100. The right move is to run 6–8 weeks at 50 units/week to:
- Identify and fix any recurring quality issues (specific printer settings, filament lot problems, snap arm failures in the field)
- Optimize the top-selling SKU's price point (A/B test $24.99 vs. $27.99 vs. $22.99 bundles)
- Document every production procedure in writing (the operations SOP), because Month 6's facility decision requires replicable processes, not tribal knowledge
- Build 3–4 weeks of finished goods buffer in the top 2 SKUs before increasing throughput (prevents stockout during the Month 6 transition)

**Secondary product design:**
- Start CadQuery designs for 1–2 additional products (headphone hook, cable label, under-desk bin) but do not launch them until the primary products are running profitably at 50 units/week.
- Design to share filament color with existing SKUs (reduces inventory complexity).
- Design for support-free printing (the ModRun design philosophy — do not compromise this for a secondary product).
- Target print time under 90 minutes for any new product (long-print products like rails are a utilization bottleneck; clips are ideal).

**Facility planning:**
- If a dedicated workspace is needed (home space is constrained, or local zoning limits expansion), identify target spaces now. You need: 10–14m² minimum, 15A or 20A electrical (two circuits preferred), ventilation, and reasonable climate control.
- Budget: $300–$800/month for a workshop or shared studio rental is typical for this footprint in most markets. This should be modeled against the net revenue at 100 units/week (~$5,000–$7,000/month) to confirm affordability.

---

## Month 6: 100+ Units/Week — Dedicated Setup + Second Employee Decision

**Target throughput:** 100+ units/week

**Hardware at Month 6:**
- 2 Bambu P1S printers (one dedicated clips overnight, one dedicated rails daytime — see `100-unit-operations-blueprint.md` Section 2.1).
- Bambu Farm Manager active from the day the second printer arrives.
- Printago free tier for material-aware routing.
- Thermal label printer (Rollo X1038 or equivalent, ~$180) — at 100 units/week and 15 orders/day, the ergonomic and time savings justify this.
- Postal scale ($20–40) — weight verification prevents USPS surcharges and serves as a secondary QA check.

**Sales channels at Month 6:**
- Etsy: primary channel, 50–60% of revenue. Should have 50+ reviews by this point.
- Amazon Handmade or Amazon.com (FBA): 30–40% of revenue. FBA makes sense at 100+ units/week because it eliminates per-order packing labor for Amazon orders entirely. Ship inventory in bulk weekly; Amazon handles individual fulfillment.
- Shopify storefront (optional): $29/month; primarily valuable if you have a newsletter list or social following that generates direct traffic. Not essential at Month 6 unless a B2B customer needs a net-terms invoicing relationship.

**Labor at Month 6:**
- Contractor at 15–20 hrs/week: packaging for Etsy orders, visual QC, outbound staging. Cost: ~$900–$1,200/month.
- Owner: print queue management, functional QC spot-checks, Amazon FBA shipment prep, design work, Etsy/Amazon listing management, supplier relationships. Target: <5 hours/day on operations, with meaningful time for growth activities.
- IRS 1099 classification check: at 15+ hours/week on a regular schedule, consult a CPA. If the contractor is approaching W-2 territory (regular hours, exclusive relationship, working at your facility), formalize as W-2 before an IRS audit forces the issue. See `workforce-scaling-research.md` Section 3 for the classification framework.

**Month 6 financial model:**

| Item | Monthly figure |
|---|---|
| Gross revenue (100 units/week × $28 blended ASP × 4.3 weeks) | ~$12,040 |
| Platform fees (Etsy 9.5% + Amazon ~20% blended at 60/40 split) | ~$1,500 |
| Filament (100 units × ~52g avg × $12/kg × 4.3 weeks) | ~$269 |
| Packaging (100 units/week × $0.30 avg × 4.3 weeks) | ~$129 |
| Shipping (Etsy: customer-paid; Amazon: FBA fee ~$3.50/unit × 40 units/week × 4.3) | ~$602 |
| Printer depreciation (2 × P1S at $699, 5,000-hr life, 16 hr/day) | ~$56 |
| Contractor labor | ~$1,000 |
| Software (Printago, SimplyPrint, or Bambu Farm Manager) | ~$20 |
| Facility (dedicated space if applicable) | $400–$800 |
| **Total monthly costs** | ~$3,976–$4,376 |
| **Net profit** | ~$7,664–$8,064 |
| **Net margin** | ~64–67% |

Note: This model uses customer-paid shipping on Etsy (free shipping built into price). Adjust if you offer seller-paid shipping.

---

## Supply Chain Scaling by Phase

### Filament Purchasing Strategy

**Phase 1 (1–50 units/week):** Single 1kg spools per color. eSUN or SUNLU PLA+ at $11–14/kg via Amazon Prime. No bulk purchasing needed — single spools reduce cash tied up in inventory and eliminate humidity storage concerns. Keep 2–3 spools on hand per active color. Reorder trigger: down to 1 spool.

**Phase 2 (50–100 units/week):** Transition to 10kg bundles per color ($12/kg average). Monthly filament consumption at 100 units/week: approximately 6–7 kg/month (clip-heavy mix) to 12–14 kg/month (rail-heavy mix). A 10kg bundle lasts 1–3 months per color — reasonable inventory cycle. Storage: sealed dry boxes with desiccant, clearly labeled with purchase date and lot. Filament from different lots may have slightly different dimensional behavior; keep lot-level records in the production log.

**Phase 3 (100–200+ units/week):** Evaluate 25–50kg direct orders from eSUN or SUNLU if consistent color requirements are confirmed. eSUN direct: ~$10–11/kg at 50kg+ orders. Storage requirement: 50kg of PLA+ filament requires approximately 50 sealed 1kg containers or 5 sealed 10kg bags with desiccant packs. A sealed plastic bin with humidity-indicating silica gel (change gel when indicator turns pink) is adequate. Full 50kg orders are only worthwhile above 125+ units/week where monthly consumption exceeds 15kg consistently.

**Tariff risk:** PLA+ is predominantly manufactured in China. Tariffs currently affect filament pricing at the ~10–20% level. US-based PLA+ (Push Plastic, MatterHackers Pro) costs $18–22/kg but eliminates tariff exposure. For a $0.40/unit material cost at 100 units/week, a $10/kg tariff increase ($12→$22/kg) adds $0.48/unit — significant but manageable with a corresponding $1–2 price increase on the product listing.

### Shipping Label Workflow Upgrade

**Pirate Ship (Phase 1–2, up to 75 orders/week):** Pirate Ship has a direct Etsy integration (import open orders, print labels, tracking syncs back). Note: Etsy's October 2024 API changes reduced the depth of third-party integration; some users report needing to manually mark orders as shipped in Etsy even after Pirate Ship label purchase. At 15 orders/day this is a 2–3 minute task. Cost: $0 (no subscription fee; postage-only pricing at commercial USPS rates).

**ShipStation (Phase 2–3, 75+ orders/week):** ShipStation Growth plan ($29.99/month, up to 500 shipments/month) provides full Etsy auto-sync, automation rules (auto-select carrier/service by weight band), and batch label printing. At 100 orders/week (430/month), ShipStation's auto-rules save approximately 20–30 minutes/week of manual carrier selection — worth the $30/month above 75 orders/week. Also provides a unified dashboard if Amazon is added as a second channel.

---

## Year 2+: Multi-Product Portfolio

**Target state:** 500+ units/week, 5+ products, 3–4 FTE, $30–50k/month revenue

**Year 2 expansion logic:**
- Add each new product only after the prior product reaches consistent 100 units/week with under 5% scrap rate.
- Each new product requires 1 additional printer at the 100-unit/week threshold (or shared capacity if print time per unit is very short).
- 5 products × 100 units/week = 500 units/week = 5–7 printers depending on product mix.

**Facility at Year 2:**
- 500–750 sq ft commercial or light industrial unit: $1,000–$2,500/month depending on location.
- Layout: dedicated printer room (2–3 rows of printers), QC/packing room, filament storage room. Separate rooms reduce contamination risk between production zones.
- Staff: 1 full-time production/operations lead ($16–20/hour, $2,800–$3,500/month fully burdened), part-time packaging help as needed.

**White-label and service bureau opportunities (Year 2):**
- Once the operation has 5+ printers and consistent throughput, overflow capacity can be sold to other Etsy sellers or small businesses needing FDM production runs.
- Slant 3D and similar service bureaus demonstrate this model at industrial scale. At 5 printers, you can offer "small-batch 3D printing" services with 5–7 day turnaround for products in the same material/size range as your own.
- Pricing: $0.15–$0.25/cm³ for PLA+ production runs is market rate for small-batch service bureau work (2026). On a 3.5 cm³ clip, that is $0.53–$0.88 service fee versus your $0.04 material cost — high-margin work.
- Risk: white-label work competes with your own production capacity. Only take on service work when you have confirmed excess capacity (printer utilization below 70% for 2+ weeks).

**Business value summary of this roadmap:**

| Business need | Roadmap answer |
|---|---|
| When to buy the second printer | Month 4–5 when single printer runs 14+ hours/day for 2 consecutive weeks |
| When to hire | Month 5–6 contractor at 10 hrs/week; W-2 at 100 units/week if hours justify reclassification |
| Prevent under-capitalization | Never buy hardware ahead of demand; use the demand validation gates at each phase |
| Facility planning | Garage/workshop through Month 6; dedicated commercial space at Year 2 (500+ units/week) |
| Revenue trajectory | Month 1: ~$1,500 net; Month 3: ~$3,200 net; Month 6: ~$7,700 net; Year 2: $15,000–$25,000 net |

---

## Decision Log Template

Use this to document every scaling decision in real time. The discipline of logging decisions against the trigger criteria prevents premature scaling and provides evidence for business loan or investor conversations.

| Date | Decision | Trigger criteria met? | Evidence | Capital committed |
|---|---|---|---|---|
| [Month 1] | Launch Etsy listing | Test print passed all functional tests | Test print log | $0 |
| [Month X] | Add 2nd printer | Printer at 14+ hrs/day for 2 weeks | Production log entries | $699 |
| [Month X] | Hire contractor | Operations >5 hrs/day for 2 weeks | Time log | $600/month |
| [Month X] | Dedicated facility | Revenue >$7,000/month for 2 months | P&L | $400–800/month |
| [Month X] | Amazon FBA | Consistent 50+ units/week for 4 weeks | Order log | $0 (FBA fee structure) |

---

## Sources

- [How to Start and Scale a 3D Print Farm Business — 3DCentral Solutions](https://3dcentral.ca/how-to-start-and-scale-a-3d-print-farm-business-the-complete-guide/)
- [Bambu Lab P1S Specifications](https://us.store.bambulab.com/products/p1s)
- [Bambu Farm Manager Quick Start Guide](https://wiki.bambulab.com/en/software/bambu-farm-manager)
- [Printago: Commerce OS for 3D Print Farms](https://printago.io/)
- [Printago Complete Bambu Lab Print Farm Guide 2026](https://printago.io/blog/bambu-lab-print-farm-guide-2026)
- [Etsy Seller Handbook: Scaling Your Business](https://www.etsy.com/seller-handbook/article/scaling-your-etsy-business/749001073413)
- [Etsy API Changes October 2024 — Third-Party Shipping Impact](https://github.com/etsy/open-api/discussions/1303)
- [Pirate Ship Etsy Integration](https://www.pirateship.com/integrations/etsy)
- [ShipStation vs Pirate Ship — Veeqo Comparison](https://www.veeqo.com/blog/shipstation-vs-pirateship-comparison)
- [ADP Industries: How to Set Up a Bambu Lab Print Farm](https://www.adpindustries.com/blog/bambu-lab-print-farm-setup-guide/)
- [eSUN 10KG PLA+ Bulk Bundle — Amazon](https://www.amazon.com/eSUN-Filament-1-75mm-Bundle-Printing/dp/B0G2KSS613)
- [SUNLU 10KG PLA+ Filament Bundle — Amazon](https://www.amazon.com/SUNLU-Filament-Printing-Tolerance-Accuracy/dp/B09QYQYW6N)
- [3D Printing Filament Price Tracker](https://filamentpricetracker.com/)
- [NextGenModeling Etsy Case Study — eRank](https://help.erank.com/blog/nextgenmodeling-etsy-seo-success-story/)
- [Amazon Handmade Seller Central: Getting Started](https://sell.amazon.com/programs/handmade)
- [Slant 3D: Plug a Print Farm into Your Etsy Store](https://www.slant3d.com/slant3d-blog/version-2-plug-a-print-farm-into-your-3d-printing-etsy-store-today)
- [SBA: How Much Does an Employee Cost You](https://www.sba.gov/blog/how-much-does-employee-cost-you)
- [Simpl Fulfillment vs ShipBob Comparison](https://www.simplfulfillment.com/support-center/simpl-fulfillment-vs-shipbob-comparison)
- Prior ModRun research: `../workforce-scaling-research.md`, `../production-scaling-research.md`, `100-unit-operations-blueprint.md`
