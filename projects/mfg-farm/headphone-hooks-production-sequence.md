---
title: Headphone Hooks — Production & Launch Sequence
project: mfg-farm
created: 2026-05-06
status: active — awaiting ModRun test-print completion to start clock
related: headphone-hooks-design-spec.md, headphone-hooks-etsy-listing.md, headphone-hooks-sku-strategy.md, post-test-print-execution.md
---

# Headphone Hooks — Production & Launch Sequence

**Lead finding:** From ModRun test-print completion to a live Etsy listing is 4 weeks. The critical path is: print 3 variants (Day 1–2) → fit test and photography (Day 3–7) → Etsy draft + photos (Week 2) → list live (Week 3). No new materials, no new tooling, no new suppliers — this is the fastest-to-revenue expansion product in the lineup.

---

## Pre-Launch Dependencies

These must be true before starting the headphone hooks sequence:

- [x] `cadquery/headphone_hooks.py` is written and builds without errors
- [ ] ModRun test-print has passed QA (clamp fit verified on actual desk)
- [ ] PLA+ filament in Matte Black (minimum 500g available)
- [ ] AMS loaded and ready (for color variant test prints in Week 2)
- [ ] Silicone bumper pads ordered (100-pack, AliExpress — 7–14 day lead time)

**Action now (before ModRun test-print completes):** Order the silicone bumper pads. Lead time is 7–14 days. Order today so they arrive during or before Week 2 QA.

---

## Week 1 — Generate STLs, First Prints, Initial QA

### Day 1 (first day after ModRun test-print passes)

**Task 1: Generate STL files**
```bash
cd projects/mfg-farm/cadquery
python headphone_hooks.py --output-dir ../stl/
```

This generates:
- `headphone_hook_12mm_with_post.stl`
- `headphone_hook_25mm_with_post.stl`
- `headphone_hook_40mm_with_post.stl`

**Task 2: Slice all three variants in Bambu Studio**
- Import all three STLs
- Profile: PLA+, 0.20mm layer height, 25% gyroid infill, 3 perimeters
- Note sliced weight and time for each — record in design-spec.md iteration log
- Export to P1S via Bambu Handy or USB

**Task 3: Print the 25mm standard variant first (single unit)**
- Print time: ~25 min
- While printing: measure actual desk thickness in workspace (caliper)
- Compare measured thickness to 25mm target

### Day 2

**Task 4: Fit test — 25mm variant**
Checklist:
- [ ] Hook slides onto 25mm desk edge with light hand pressure (not tight, not loose)
- [ ] Hook does not rock side-to-side by more than 1mm when headphones (~300–400g) are hung
- [ ] Hook does not slide toward desk edge under headphone weight over 30 seconds
- [ ] Rubber pad pockets accept 3M Bumpon pads flush (or within 0.2mm)
- [ ] Hook arm angle holds headphones — headband does not slide off hook tip
- [ ] Cable post diameter accommodates 3.5mm and USB-C cables comfortably

**If fit test passes:** Print 12mm and 40mm variants (single unit each).

**If jaw gap is too tight:** Re-run script with `--tolerance 0.25` or `--tolerance 0.30`. Reprint 25mm variant. Repeat fit test.

**If jaw gap is too loose (excessive rocking):** Reduce `FDM_TOLERANCE` constant in `headphone_hooks.py` to 0.10mm. Reprint.

### Day 3–4

**Task 5: Print thin and thick variants**
- Print `headphone_hook_12mm_with_post.stl` (single)
- Print `headphone_hook_40mm_with_post.stl` (single)
- Fit test both on appropriate reference boards (thin: 12mm plywood scrap; thick: 40mm lumber)

**Task 6: Weight verification**
- Weigh each variant with kitchen scale
- Record actual weights — update design-spec.md and cost-model.md if >2g deviation from estimate
- Confirm filament cost per unit is within $0.29–$0.36 range

**Task 7: Print first production batch (5 units, 25mm standard)**
- 4-per-plate layout in Bambu Studio
- One plate of 4 + one single = 5 units
- Total plate time: ~95 min (4-unit plate) + 25 min (single) = ~2 hrs
- This becomes the inventory for photography + QA

### Day 5–7

**Task 8: Install rubber pads on all 5 production units**
- If bumper pads have arrived: install now (press-fit into jaw pockets, firm hand pressure)
- If bumper pads have not arrived: mark units "pads pending" and process after arrival
- Inspect all 5 units for layer adhesion, dimensional consistency, tip smoothness

**Task 9: Initial photography session (lifestyle + detail)**
Using existing ModRun desk setup:
- Photo 1: Hero — headphones hanging on hook, desk in background
- Photo 2: Cable wrap post in use (USB-C cable wrapped twice around post)
- Photo 3: Three sizes side by side (12mm, 25mm, 40mm) on white sheet or desk
- Photo 4: Under-desk angle showing clamp grip on desk edge
- Photo 5: ModRun rail + headphone hook together (ecosystem shot)

Photography brief: see `headphone-hooks-etsy-listing.md` Photo Brief section.

---

## Week 2 — QA Refinement, Color Variants, Etsy Draft

### Day 8–10

**Task 10: Tolerance iteration (if needed)**
If fit test from Day 2 required adjustments, now is the time to run the adjusted tolerance through a 5-unit batch and re-verify fit. Document final tolerance in design-spec.md iteration log.

**Task 11: Print 2–3 color variant samples**
- Matte White (second most requested color in desk accessories)
- One accent color (Terracotta or Deep Blue) for photo variety
- These are for listing photos only — not inventory

**Task 12: Color photo shoot**
- Photo 6: Color options flat lay (5 colors: black, white, gray, blue, terracotta)
- Photo 7: Scale reference (hook with ruler alongside)

### Day 11–14

**Task 13: Create Etsy listing draft**
- Import all listing copy from `headphone-hooks-etsy-listing.md`
- Fill all {{VARIABLES}}: processing time, city/state, current color stock
- Upload all 5+ photos in order specified in photo brief
- Set price: $12.99 (standard hook)
- Set personalization field: desk thickness + color selection (copy from listing doc)
- Set shipping: buyer pays, USPS First Class, existing ModRun shipping profile
- **Do not publish yet** — complete photo editing first

**Task 14: Photo editing**
- Crop, color-correct hero and detail photos in phone app (Lightroom Mobile or Snapseed)
- Add text overlay to Photo 8 (optional): "No Tools Required"
- Export at 2000×2000px minimum for Etsy

---

## Week 3 — Publish, Initial Ads, Cross-Sell Setup

### Day 15

**Task 15: Publish Etsy listing**
- Review all listing content one final time
- Publish on Thursday between 10 AM and 2 PM
- Set Etsy Ads: $1.00/day maximum CPC, broad match targeting, all 13 tags included

**Task 16: Update ModRun packaging insert**
- Add headphone hook listing URL to existing thank-you card or create a separate "complete your setup" insert
- Reorder business cards if current stock does not mention the hook
- Add hook listing link to ModRun Etsy listing description ("Complete your desk setup — see our headphone hook in this shop")

### Day 16–21

**Task 17: Prepare production batch for inventory**
- Print 20 units of standard 25mm variant (5 plates × 4 units = 20)
- Print 5 units each of 12mm and 40mm variants (2 plates × 2 units + 1 single each)
- Total: 30 units as launch inventory
- Install rubber pads, inspect, bag in zip-lock 4×6" bags, box or shelf-store

**Task 18: Create 3-pack bundle listing**
- Duplicate single hook listing
- Update title: "Headphone Hook 3-Pack | Desk Clamp Cable Organizer | Custom Color"
- Update description with bundle copy (reference `headphone-hooks-sku-strategy.md`)
- Set price: $32.99
- Personalization: "3 desk thicknesses + 3 colors (one per line)"

---

## Week 4 — Stabilize Production, Monitor Performance

### Day 22–28

**Task 19: First sales processing**
- Print and ship orders within stated processing time
- Package: hook in zip-lock bag, poly mailer, handwritten thank-you card, packaging insert linking ModRun listing
- Photo the first few packages before sealing — document for future SOP

**Task 20: Day 7 listing performance check**
Metrics to review in Etsy Shop Manager:
- Listing views
- Search impressions
- Click-through rate (target: >1%)
- Favorites added
- Sales (any)

If CTR < 0.5%: rotate hero photo and/or switch to Alt Title A (see listing doc).
If views < 50 in first 7 days: increase Etsy Ads budget to $2/day for 2 weeks.

**Task 21: Request first review**
Include in shipment: handwritten or printed note — "If your hook works well, an honest review helps our small shop a lot. Thank you."

---

## Key Milestones Summary

| Milestone | Target Date (relative to ModRun test-print pass) | Owner |
|---|---|---|
| STLs generated, first print complete | Day 1–2 | Anya |
| Fit test pass (25mm variant) | Day 2–3 | Anya |
| All 3 variants fit-tested | Day 4–5 | Anya |
| Silicone bumper pads arrive | ~Day 7–14 (order now) | Anya |
| Photography complete (5 photos min) | Day 7 | Anya |
| Etsy listing draft complete | Day 11–14 | Anya |
| Listing published live | Day 15 (Week 3) | Anya |
| 30-unit inventory batch complete | Day 21 | Anya |
| 3-pack bundle listing published | Day 18–21 | Anya |
| First sale | Day 15–30 (dependent on Etsy algorithm) | — |
| 10 reviews | ~Day 60–90 | — |
| Price test: $14.99 | After 50 reviews | Anya |

---

## Risk Log

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Jaw gap tolerance off on first print | Medium | Low — simple reprint | Run 1 test unit before batch; FDM_TOLERANCE tunable in script |
| Bumper pads don't arrive in time for Week 1 photography | Medium | Low — photograph without pads installed, install before shipping | Order pads immediately (today); use masking tape as stand-in for initial QA photo |
| ModRun test-print delays (extends schedule) | Low | Medium — entire launch sequence delays | Designs are ready; no dependency blocks design work |
| Etsy listing takes 7–14 days to rank | Certain | Low — normal for new listings | Etsy Ads compensates; launch timing is not critical-path for revenue |
| Competitor adds cable post feature | Low | Medium — reduces differentiation | Ecosystem match (ModRun bundle) remains exclusive; move to dual-hook premium SKU as primary differentiator |

---

## Sources

- mfg-farm/headphone-hooks-design-spec.md — print specs, tolerance notes
- mfg-farm/headphone-hooks-etsy-listing.md — listing copy, photo brief
- mfg-farm/headphone-hooks-sku-strategy.md — SKU architecture, pricing
- mfg-farm/post-test-print-execution.md — ModRun production sequence reference
- mfg-farm/DAY1_LAUNCH_OPERATIONS_PLAYBOOK.md — operational workflow patterns
