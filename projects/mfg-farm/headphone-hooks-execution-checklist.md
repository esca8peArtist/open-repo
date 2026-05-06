---
title: Headphone Hooks — Go-to-Market Execution Checklist
project: mfg-farm
created: 2026-05-06
status: ready — clock starts on ModRun test-print pass
related: headphone-hooks-design-spec.md, headphone-hooks-cost-model.md, cadquery/headphone_hooks.py
---

# Headphone Hooks — Go-to-Market Execution Checklist

**Summary:** Four weeks from ModRun test-print pass to a live, photographed, SEO-tagged Etsy listing. No new materials, no new suppliers, no new tooling. This is the fastest-to-revenue expansion product in the lineup. Execute in order; do not skip tolerance validation.

---

## Pre-Start: Do These Before Day 1

- [ ] **Order silicone bumper pads now.** AliExpress 100-pack 3M Bumpon SJ5302-equivalent (1.5mm height, self-adhesive). Lead time 7–14 days. One order covers 50 hooks. Cost: ~$5. Do not wait for ModRun to complete — order today.
- [ ] Confirm at least 500g of Matte Black PLA+ is on the spool (covers ~20 hooks with margin).
- [ ] STL generation command is ready: `python cadquery/headphone_hooks.py --output-dir ./stl/`

---

## Week 1: Print, Fit-Test, Initial QA

### Day 1 (first day after ModRun test-print passes)

- [ ] Generate all three STL variants:
  ```bash
  cd projects/mfg-farm/cadquery
  python headphone_hooks.py --output-dir ../stl/
  ```
  Outputs: `headphone_hook_12mm_with_post.stl`, `headphone_hook_25mm_with_post.stl`, `headphone_hook_40mm_with_post.stl`
- [ ] Slice the 25mm variant in Bambu Studio: 0.20mm layer height, 25% gyroid infill, 3 perimeters, no supports. Note the slicer's weight and time estimate. Record in design-spec iteration log.
- [ ] Print one 25mm hook (single unit, ~25 min). While printing: measure actual desk thickness in workspace with calipers.

### Day 2: Fit Test — 25mm Variant (Critical Path)

- [ ] Cool 30 min before handling. Test-fit on 25mm desk edge (or 25mm shim).
  - Pass criteria: slides on with light one-hand pressure, no side-to-side rock >1mm, does not slide under 300–400g static load over 30 seconds.
- [ ] If jaw too tight: `python headphone_hooks.py --tolerance 0.25 --output-dir ../stl/` Reprint and retest.
- [ ] If jaw too loose: edit `FDM_TOLERANCE = 0.10` in `headphone_hooks.py`. Reprint and retest.
- [ ] If fit passes: document final tolerance value in a git commit message. Example: `"Tolerance calibrated: FDM_TOLERANCE=0.20mm on Bambu P1S with eSUN PLA+"`
- [ ] Check hook arm tip — run fingertip across tip, should be smooth with no sharp edge.
- [ ] Check cable post — loop USB-C cable (5mm OD) around post, should loop with clearance. Post should not wobble at base.

### Day 3–4: Thin and Thick Variants

- [ ] Print `headphone_hook_12mm_with_post.stl` (single). Fit-test on 12mm plywood or shim.
- [ ] Print `headphone_hook_40mm_with_post.stl` (single). Fit-test on 40mm lumber.
- [ ] Weigh all three variants with kitchen scale. Target: 22–28g each. If >2g deviation from estimate, update cost model.
- [ ] Print first production run: 4-unit plate of the 25mm standard (one plate = ~95 min). This is your photography inventory.

### Day 5–7: Rubber Pads and Photography Round 1

- [ ] If bumper pads have arrived: press-fit into upper and lower jaw pockets on all QA units. Pad must sit flush or 0.1–0.2mm below surrounding surface.
- [ ] If pads have not arrived yet: photograph without pads; mark units "pads pending." Do not ship without pads installed.
- [ ] Photography session — minimum 5 shots (see Photo Brief below). Use existing ModRun desk setup.

---

## Week 2: Color Samples, Etsy Draft, Tolerance Lock

### Day 8–10

- [ ] If tolerance was adjusted: print 5-unit batch at final tolerance. Verify all 5 pass fit test. This is the production-locked tolerance.
- [ ] Print 2–3 color variant samples for photography (Matte White + one accent color). These are photo props, not inventory.
- [ ] Shoot color variant flat-lay: all 5 colors (black, white, gray, blue, terracotta) arranged on white background. Label in photo edit.
- [ ] Shoot scale reference photo: hook alongside a ruler or common object.

### Day 11–14: Etsy Listing Draft

- [ ] Create listing in Etsy (do not publish yet — draft mode).
- [ ] Set listing title: `Desk Headphone Hook with Cable Manager | 3D Printed Clamp | Custom Color`
- [ ] Upload photos in order: hero → cable post in use → three sizes → under-desk clamp → ecosystem shot → color flat-lay → scale reference.
- [ ] Paste listing description (copy from `headphone-hooks-etsy-listing.md` Section 2, fill all `{{VARIABLES}}`).
- [ ] Set personalization field label: `Select desk thickness + color`. Instructions: `1. DESK THICKNESS: 12mm / 25mm (standard) / 40mm. 2. COLOR: Matte Black / Matte White / Space Gray / Deep Blue / Terracotta. If unsure about thickness, choose 25mm.`
- [ ] Set price: **$12.99** (launch price; test $14.99 after 50 reviews).
- [ ] Set shipping: buyer pays, USPS First Class, existing ModRun shipping profile.
- [ ] Set processing time: 3–5 business days.
- [ ] Set quantity: 100 (printed to order; high number prevents "last 1!" pressure).
- [ ] Add all 13 tags (in priority order): `headphone hook`, `desk headphone holder`, `headset stand desk`, `3d printed desk accessory`, `headphone desk clamp`, `cable organizer desk`, `gaming desk setup`, `headset hanger`, `desk organizer`, `gamer gift`, `home office accessory`, `headphone stand`, `custom 3d print`
- [ ] Review draft — read all text as a buyer, not a maker. Does it answer: what is it, will it fit my desk, how does it install, what if it doesn't fit?

---

## Week 3: Publish and Cross-Sell Setup

### Day 15 (publish day — target Thursday 10 AM–2 PM)

- [ ] Final review of Etsy draft — confirm no `{{VARIABLES}}` remain unfilled.
- [ ] Publish listing.
- [ ] Enable Etsy Ads: $1.00/day maximum CPC, broad match, all 13 tags included. (Jump-starts algorithm placement before organic reviews build.)
- [ ] Share on social: Twitter/X caption: `New: Parametric Headphone Hook — desk clamp with built-in cable management. Fits 12–40mm desks. $12.99. Pairs with our ModRun cable system. [link] #desksetup #3dprinting`
- [ ] Post in r/battlestations or r/workspaces: casual format, honest product photo, non-salesy caption. Example: `Designed and printed a headphone hook that actually manages cables. Clamps any desk 12–40mm, no screwdriver. Etsy link in comments if curious.`
- [ ] Update ModRun packaging insert: add headphone hook Etsy URL to thank-you card or create a separate "complete your setup" insert card.
- [ ] Add hook listing link to ModRun Etsy listing description: `Complete your desk setup — see our headphone hook (cable management included) in this shop.`

### Day 16–21: Inventory Build

- [ ] Print 20-unit batch: 25mm standard (5 plates × 4 units, ~7.5 hr total print time).
- [ ] Print 5 units each of 12mm and 40mm variants (~2 additional plates).
- [ ] Total launch inventory target: 30 units (20× 25mm, 5× 12mm, 5× 40mm).
- [ ] QC all 30: jaw grip, rubber pad installed, no visible layer artifacts, tip smooth.
- [ ] Bag in 4×6" zip-lock bags, store on shelf by variant.

### Day 18–21: Bundle Listing

- [ ] Duplicate single hook listing in Etsy.
- [ ] Update title: `Headphone Hook 3-Pack | Desk Clamp Cable Organizer | 3D Printed | Custom Color`
- [ ] Set price: **$32.99** (saves ~$6 vs. 3× single, matches ~77% net margin).
- [ ] Update personalization field: `List 3 desk thicknesses + 3 colors (one per line). Example: 25mm Black / 12mm White / 25mm Gray`
- [ ] Publish 3-pack listing.

---

## Week 4: First Orders and Optimization

### Day 22–24

- [ ] Process first orders within stated 3–5 day window. Print on demand if pre-sell occurs.
- [ ] Wrap each hook in bubble wrap, poly mailer, add thank-you card + ModRun cross-sell insert.
- [ ] Print shipping label via Pirate Ship. Confirm USPS First Class for <4oz shipments ($3.50–$4.00).
- [ ] Photo the first packaged order before sealing — document for future SOP reference.
- [ ] Include in every shipment: `"An honest review helps our small shop grow — thank you!"`

### Day 25–28: Performance Check

- [ ] Review Etsy stats in Shop Manager:
  - Views (target: >50 in first 7 days)
  - Click-through rate (target: >1% from search impressions)
  - Favorites added
  - Sales count
- [ ] If CTR < 0.5%: swap hero photo to under-desk lifestyle shot; or switch title to Alt A: `3D Printed Headphone Clamp Stand | Desk Hook + Cable Organizer | Custom Color`
- [ ] If views < 50 in 7 days: increase Etsy Ads to $2/day for 2 weeks.
- [ ] Respond to any Q&A within 4 hours. Response time is a ranking factor.

---

## MOQ and Inventory Calculations

### Minimum Order Quantities

| Scenario | Units | Print Time | Plate Runs | Revenue | Net Profit |
|---|---|---|---|---|---|
| Test-print validation | 3 (one each variant) | ~75 min | 3 single runs | — | — |
| Launch inventory (conservative) | 30 | ~10 hr | 8 plates | $390 at sell-through | ~$296 |
| Weekly steady-state | 20 | ~7.5 hr | 5 plates | $260/wk | ~$197/wk |
| Break-even point | 200 cumulative | ~75 hr | 50 plates | $2,598 | Design cost recovered |

**Cost basis for MOQ decisions:**
- Filament: $0.013/g × 26g avg = $0.34/unit
- Rubber pads: $0.08/unit (2 pads × $0.04)
- Packaging: $0.16/unit
- Etsy fees (at $12.99): $1.48/unit
- Total COGS: ~$3.13/unit (Etsy fees included)
- Net per unit: ~$9.86

**Silicone pad reorder trigger:** 100-pack covers 50 hooks. Reorder when 40 hooks have shipped (~2 weeks into steady-state production).

---

## Photo Brief (Minimum 5 shots for launch)

All shots use existing ModRun desk setup — no new backdrop or lighting required.

| # | Shot | Description | Priority |
|---|---|---|---|
| 1 | Hero lifestyle | Hook on desk, headphones hanging, cable looped on post. Natural window light. Desk organized. | Required |
| 2 | Cable post in use | Close-up of cable looped around post. This is the primary differentiator — make the post the subject. | Required |
| 3 | Three sizes | 12mm / 25mm / 40mm side by side on white background, labeled. Shows buyer the selection option. | Required |
| 4 | Under-desk clamp | Angle shot showing rubber pads, jaw geometry, and desk contact. Answers "will this scratch my desk?" | Required |
| 5 | Ecosystem shot | Hook + ModRun rail in same frame. Cross-sell trigger. Use in both listings. | Required |
| 6 | Color flat-lay | 5 colors on white background, each labeled. Reduces color-choice hesitation. | Recommended |
| 7 | Scale reference | Hook next to a ruler or common household object. | Recommended |
| 8 | Text overlay | Hero shot with bold text overlay: `No Tools Required`. A/B test as thumbnail. | Optional |

**Post-processing (phone editor or Lightroom Mobile):**
- Crop to 80% subject, 20% whitespace
- Brightness +10–15% for indoor shots
- Contrast +5–10%
- Export JPEG, 2000×2000px minimum, 500KB–2MB file size
- Filenames: `headphone-hook-01-hero.jpg`, `headphone-hook-02-cablepost.jpg`, etc.

---

## Listing Copy Template (Condensed Reference)

Full copy in `headphone-hooks-etsy-listing.md`. Key elements for go-live:

**Title (88 chars):** `Desk Headphone Hook with Cable Manager | 3D Printed Clamp | Custom Color`

**Opening hook (first 3 sentences — buyers see this before "see more"):**
> Keep your headphones off the desk and your headset cable actually organized. Unlike standard hooks, this one includes a built-in cable-wrap post so you're not left with loose cable coiling on your desk. Installs in seconds — no screwdriver, no assembly.

**Five bullet features (above the fold):**
1. Parametric clamp fits 12mm, 25mm, or 40mm desk tops — select at checkout
2. Built-in cable-wrap post (8mm diameter, rounded top) — no separate cable hook needed
3. Rubber pads on both jaws protect desk surface, no slipping
4. 55mm hook arm with slight upward angle — headphones stay put
5. Original CadQuery design, printed to order

**Customer service templates (common Q&A):**

Q: Will this fit my 15mm desk?
> The 12mm variant is designed for desks 12–18mm thick. For 15mm, the 12mm variant fits with a small amount of flex. Message me your exact measurement and I'll confirm the right size.

Q: How strong is the cable post?
> The post is 8mm diameter PLA+, designed for cable loop wrapping (not yanking). It holds standard audio cables and USB-C easily. For high-stress cable management, I'd recommend PETG version — just note that in your order.

Q: Different from the $12 Amazon hook?
> Three differences: (1) Parametric clamp fits desks 12–40mm thick with no tools. (2) Integrated cable-wrap post — no other desk clamp hook has this. (3) Original design, made by me, QC'd by me, 30-day guarantee.

---

## Post-Launch Monitoring (Weekly, First 60 Days)

| Metric | Target | Action if Below Target |
|---|---|---|
| Views/week | 50–100 | Increase Etsy Ads to $2/day |
| Click-through rate | >1% | Replace hero photo; test Alt Title A |
| Favorites/week | 5–10 | Check that personalization field is clear |
| Conversion rate | 5–10% of views | Review listing opening text; add detail photos |
| Average review | 4.8+ | Investigate cause immediately if first reviews are <4.5 |
| Return rate | <2% | If >5%, tolerance issue — revalidate jaw gap |

**Milestones and actions:**
- Review 10: Include thank-you card explicitly requesting review. Quote in listing copy if 5-star.
- Review 50: Test price increase to $14.99. Run for 2 weeks. If conversion rate holds (within 20%), keep higher price.
- Day 60: Add "Customers also bought" bundle note in description. Link to ModRun listing.
- Month 2: Design dual-hook SKU (HH-DUAL, $19.99). ~2–3 hrs CadQuery work. Captures premium tier.
- Month 3: Add wall-mount variant (HH-WALL, $9.99). ~30 min CadQuery work (remove lower jaw, add M3 through-holes).

---

## Etsy Compliance Checklist

- [ ] Design is original — created in CadQuery from scratch, not adapted from Printables/Thingiverse geometry
- [ ] Git commit history documents design provenance (timestamped commits)
- [ ] All materials accurately described (PLA+, silicone pads)
- [ ] Photos are of actual printed product, not renders or stock images
- [ ] Price and shipping accurately stated
- [ ] Processing time is achievable at current print capacity
- [ ] "Made to order" stated in listing
- [ ] No dropshipping — designed, printed, and shipped by seller

---

## Risk and Contingency

| Risk | Probability | Response |
|---|---|---|
| Jaw tolerance off on first print | Medium | Re-run with `--tolerance 0.25` and reprint; built into Day 2 checklist |
| Bumper pads not arrived by photography day | Medium | Photograph without pads; use masking tape as stand-in. Install pads before any unit ships. |
| ModRun test-print delayed >2 weeks | Low | Designs are complete; no blockers. Use delay to order pads, build photography backdrop. |
| Etsy listing takes >14 days to generate impressions | Certain | Normal. Etsy Ads at $1–2/day compensates in first 30 days. Do not panic-edit listing in first 7 days. |
| Competitor adds cable-post feature | Low | ModRun ecosystem bundling remains exclusive. Move HH-DUAL to front of queue as primary differentiator. |

---

*Document status: EXECUTION-READY — all actions are blocked only on ModRun test-print pass. Silicone pad order should be placed before ModRun completes.*
