---
title: Batch 3–4 Launch Sequencing — mfg-farm
project: mfg-farm
created: 2026-05-07
status: active
confidence: high — based on single-printer capacity model, ModRun cost baseline, eRank category signals, Etsy policy constraints
related: batch-3-candidate-research.md, batch-3-margin-validation.csv, product-line-strategy.md
---

# Batch 3–4 Launch Sequencing

**Lead finding:** Run Batch 2 (headphone hooks) and Batch 3-A (magnetic bin labels) simultaneously — they are plate-compatible and do not compete for print time. Monitor riser legs follow 3–4 weeks later once the magnet calibration is validated and bin labels are live. Pegboard hooks and plant markers launch in Month 3–4, sequenced by which calibration (peg tolerance or ASA profile) completes first. At 20–25 units/week blended across all active SKUs, the second printer trigger activates in Month 4–5, not Month 6 — earlier than the product-line-strategy.md conservative projection.

---

## Section 1: Launch Calendar

### Current State (Week 0, May 2026)

- **Batch 1 (ModRun cable clips/rails):** Awaiting test-print approval. First production run pending.
- **Batch 2 (headphone hooks):** Design complete (`cadquery/headphone_hooks.py`). Listing copywriting and photography next.
- **Batch 3+ products:** Research complete (this document). Design work on monitor riser legs is the only remaining pre-design gap.

### Month 1 — Batch 1 Production + Batch 2 Launch + Batch 3 Design

**Week 1–2:**
- ModRun test print approved → first 12-unit production batch → Etsy listing goes live.
- Order N52 magnets for bin labels (200× 8mm × 2mm from Amazon domestic, 1–2 day delivery — skip AliExpress to avoid 14-21 day delay). Cost premium: ~$30 vs. $8 for AliExpress equivalent. Worth it to compress time-to-launch.
- Begin CadQuery design work on monitor riser legs (3–4 hours).

**Week 3–4:**
- Headphone hooks: test print → photograph with ModRun cables visible → Etsy listing live.
- Bin labels test print: one 30-tile plate → calibrate magnet press-fit → adjust `MAGNET_DIAMETER` if needed → confirm.
- Monitor riser legs: design complete → 1 test leg printed → screw pocket depth validated.

**End of Month 1 state:** ModRun live, headphone hooks live, bin labels design validated (magnets confirmed press-fit). Monitor riser legs design built. Printers are running: ModRun clips in primary slots, headphone hooks in secondary slots, bin label tiles filling unused plate corners.

### Month 2 — Batch 3-A Live + Batch 3-B Approaching

**Week 5–6:**
- Magnetic bin labels: Etsy listing live. Set Etsy processing time to "3–5 business days" (you have validated stock in hand and magnets on shelf).
- Personalization field active: "Enter your category names, one per line (10 or 20)." Process each order with a 5-minute CadQuery custom STL export from the CLI `--label` flag.
- Monitor riser legs: remaining test leg variants (8cm and 16cm height, both shelf thicknesses) printed and validated.

**Week 7–8:**
- Monitor riser legs: Etsy listing live. 3 variants (8cm/$28, 12cm/$32, 16cm/$38). Personalization field: "Select height (8cm / 12cm / 16cm) and shelf board thickness (18mm / 25mm)."
- Launch bundle listing: "ModRun + Monitor Riser Starter Desk Kit" at $54–$60 (ModRun starter pack + 12cm riser legs). Cross-sell insert in all ModRun orders.

**End of Month 2 state:** Four active Etsy listings (ModRun, headphone hooks, bin labels, monitor riser legs). Printer running at estimated 35–45 hours/week across all SKUs.

### Month 3 — Batch 4-A (Pegboard Hooks) + Batch 4-B Begin

**Week 9–10:**
- Pegboard hooks: test print (small peg + all three sizes) → calibrate peg diameter against actual pegboard panel → adjust `PEG_DIAMETER` via CLI → confirm all three sizes.
- Photograph pegboard hooks on a real pegboard with tools hung — this photo is the primary conversion driver for this SKU.
- Begin ASA print profile calibration for plant markers (parallel activity, does not conflict with PLA production).

**Week 11–12:**
- Pegboard hooks: Etsy listing live. Formats: individual hook ($1.50–$2.50 each depending on size), 10-hook set ($18–$22), 20-hook starter set ($32–$38 with mixed sizes and embossed labels).
- Plant marker ASA calibration complete → test print 10 markers → soil insertion test.

### Month 4 — Batch 4-B (Plant Markers) + Second Printer Assessment

**Week 13–14:**
- Garden plant markers: Etsy listing live. 6-pack ($14), 10-pack ($22), 20-pack ($38). Personalization field: "Enter up to 10 plant names, one per line."
- Review second printer economics: if Batch 3 SKUs are generating 15+ orders/week combined, the second P1S acquisition trigger is approaching (30 ModRun-equivalent units/week sustained demand). At $699–$799, payback is 3–5 weeks at that volume.

---

## Section 2: Dependencies and Parallel Printing

### Can Batch 2 + Batch 3 Print Simultaneously?

Yes, with one structural advantage: bin label tiles are tiny (50mm × 40mm × 3mm). On a 256mm × 256mm P1S build plate, 30 tiles fit simultaneously. The headphone hook is 80–120mm in footprint — approximately 4–6 per plate. A mixed plate of 12 bin label tiles + 3 headphone hooks is feasible and efficient: one plate run produces half a bin label 10-pack and 3 headphone hooks.

**Practical approach:** Do not force mixed plates unnecessarily. Run dedicated hook plates (4–6 units) and dedicated label plates (30 tiles) based on order demand. Mixed plates are a "fill the gaps" technique for idle plate space, not a primary strategy.

### Monitor Riser Legs vs. Other SKUs

Monitor riser legs are the capacity constraint. At 2 legs per plate and 75–90 minutes per plate, a 4-leg set consumes 150–180 minutes of print time. During a monitor riser print run, smaller SKUs (bin labels, headphone hooks, ModRun clips) cannot run on the same printer. This is acceptable at 4–6 riser sets/week (600–1,080 minutes = 10–18 hours of riser-dedicated print time), leaving 50–60 hours/week for other SKUs.

**Rule:** Dedicate overnight runs to monitor riser legs (2 plate runs per night = 1 set per night = 7 sets/week maximum). Daytime runs produce bin labels, headphone hooks, and ModRun clips at faster cycle times. This fully utilizes the printer without overcommitment.

---

## Section 3: Revenue Forecast

**Assumptions:** Conservative conversion estimate — 0.5% of monthly impressions convert. Etsy search volume proxies used from category listing depth and review velocity signals (not direct eRank API data, which requires a paid subscription). Revenue forecasts use the 20-unit/week baseline unless noted.

| Product | Monthly Etsy Impressions (est.) | Conversion Rate | Units/Month | Sell Price | Monthly Gross | Monthly Net |
|---|---|---|---|---|---|---|
| ModRun (cable clips) | 2,000–4,000 | 1.0% (established) | 20 sets | $24.99 | $500 | $364 |
| Headphone hooks | 1,500–3,000 | 0.8% | 15–20 | $16.00 | $240–$320 | $183–$244 |
| Magnetic bin labels | 2,500–5,000 | 0.7% | 18–20 sets | $26.00 | $468–$520 | $339–$377 |
| Monitor riser legs | 1,000–2,000 | 1.0% (high-intent buyer) | 8–12 sets | $32.00 | $256–$384 | $177–$266 |
| **Month 2 total** | | | | | **~$1,464–$1,724** | **~$1,063–$1,251** |

**Month 3–4 additions (Pegboard Hooks + Plant Markers):**

| Product | Units/Month | Sell Price | Monthly Gross | Monthly Net |
|---|---|---|---|---|
| Pegboard hook sets | 12–15 sets | $32.00 | $384–$480 | $271–$339 |
| Plant markers | 10–15 sets | $22.00 | $220–$330 | $143–$215 |
| **Month 4 total (all products)** | | | **~$2,068–$2,534** | **~$1,477–$1,805** |

**Month 6 steady-state (from product-line-strategy.md projection):** ~$2,420/week gross, ~$1,743/week net — achieved when all five products have Etsy algorithm traction (50+ reviews each, consistent review velocity).

**Revenue forecast confidence:** Low-medium. These are first-listing projections before any reviews exist. Etsy algorithm traction (ranking in search) typically requires 20–50 reviews per listing, which takes 4–8 weeks at low initial volume. The actual revenue ramp is S-shaped: slow first month, accelerating months 2–4 as reviews compound. Do not use these figures for capital planning — use them as directional targets only.

---

## Section 4: Cash Flow and Second Printer Payoff

### Does Batch 3 Accelerate Second Printer Acquisition?

Yes, materially. The product-line-strategy.md conservative projection had the second printer trigger at Month 4–6. With Batch 3 (bin labels + monitor risers) launching in Month 2, the additional revenue accelerates the payback timeline.

**Second printer trigger math:**
- Trigger condition: 30+ ModRun-equivalent units/week sustained demand AND printer at 80%+ utilization.
- At Month 2 steady-state: ModRun (20 units) + headphone hooks (15 units) + bin labels (20 sets) + monitor riser legs (8 sets) = approximately 63 "units" per week by count, but bin labels are 4-minute prints and monitor risers are 150-minute sets. Actual printer-hours/week at this volume: approximately 45–55 hours.
- P1S at 14+ hours/day = 98 hours/week theoretical max. 60–75 hours realistic sustained. At 55 hours of demand, the printer is at ~75–85% utilization — approaching the 80% trigger.
- **Expected second printer trigger: Month 3**, not Month 4–6.

**Second P1S investment: $699–$799.** At Month 3 revenue of ~$1,500–$1,800/month net, payback period is under 1 month of incremental capacity. The investment is self-funding within 4–5 weeks of the purchase.

**Second printer operating model:** Dedicate Printer 1 to ModRun + headphone hooks (the established SKUs with known demand). Dedicate Printer 2 to Batch 3+ products (bin labels, monitor risers, pegboard hooks) while profile calibration occurs. This eliminates cross-contamination risk between PLA+ production and ASA calibration runs.

---

## Section 5: MOQ + Inventory Strategy

### First-Run Batch Size for Batch 3 Products

**Magnetic Bin Labels:** Follow the ModRun post-test-print 12-unit batch model — but for labels, the unit is a "10-pack set," and each plate produces 3 sets (30 tiles). First run after calibration: **3 plate runs = 9 sets = 90 tiles.** Cost of first production run: ~$25 in materials (magnets + filament + packaging). Sell price: $234 (9 × $26). This covers materials and generates $209 in gross before fees — essentially zero risk on the first production batch.

**Monitor Riser Legs:** First run: **4 sets (16 legs, 4 plate runs at 2 legs/plate).** Total print time: ~6 hours. Filament cost: ~$13. Packaging: ~$6. Sell price: $128 (4 × $32). First-run risk is negligible.

**Post-first-sale strategy (both products):** List with "ships in 3–5 business days" (print to order). Do not pre-build inventory for products without Etsy review history. At 5–10 orders/week per SKU, print-to-order is sustainable solo. Transition to pre-built inventory (2 weeks of stock) once reviews exceed 20 and order velocity is predictable.

**Reorder triggers:**
- Bin labels: reorder N52 magnets at 100 sets sold (~1,000 magnets consumed, reorder 500 units from AliExpress for $4–8 delivered).
- Monitor riser legs: no consumable BOM reorder needed (silicone feet are the only component, 100-pack lasts ~25 sets).
- Filament: maintain 2 spools of each active color for labels (black, grey primary; add colors as demand signals emerge). 1 spool of ASA per color for plant markers.

---

## Sources

- [mfg-farm product-line-strategy.md](product-line-strategy.md) — monthly revenue projections, launch sequence framework
- [mfg-farm production-scaling-research.md](production-scaling-research.md) — printer utilization model, capacity analysis
- [mfg-farm batch-3-candidate-research.md](batch-3-candidate-research.md) — product COGS, margin analysis, design status
- [mfg-farm batch-3-margin-validation.csv](batch-3-margin-validation.csv) — per-product cost breakdown
- [mfg-farm cadquery/sku_batch_2_magnetic_labels.py](cadquery/sku_batch_2_magnetic_labels.py) — print time per tile, plate capacity
- [mfg-farm cadquery/sku_batch_2_pegboard_hooks.py](cadquery/sku_batch_2_pegboard_hooks.py) — print time per hook, plate capacity
- [mfg-farm cadquery/sku_batch_2_plant_markers.py](cadquery/sku_batch_2_plant_markers.py) — ASA print settings, print time

---

*Confidence note: Revenue projections are directional estimates from listing count and review velocity proxies. Actual Etsy search volume data requires eRank paid subscription not accessed in this research. Second printer trigger timing assumes linear demand growth — actual growth may be faster (reviews compound) or slower (new listing cold start). Printer utilization estimates assume 0.20mm layer height, 20–40% infill per SKU, and production-tuned print profiles.*
