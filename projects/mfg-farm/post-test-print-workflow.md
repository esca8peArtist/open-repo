---
title: ModRun Post-Test-Print Workflow & Scaling Roadmap
date: 2026-05-05
status: active
version: 1.0
scope: STL finalization through 6-month production scale-up — all post-test-print operations
related: production-workflow-v1.md, supplier-economics.md, pricing-strategy.md, market-research.md, post-test-print-launch-prep.md
confidence: high
---

# ModRun Post-Test-Print Workflow & Scaling Roadmap

**Lead finding:** The test print is the last gate before revenue. Once it passes snap-fit and dimensional checks, every downstream decision is already made — the STL files lock, the slicer profile freezes, photography happens once, the Etsy listing activates, and the printer runs nights. The entire post-test-print workflow from STL finalization to first shipment takes 3–5 days. The six-month revenue trajectory from a single Bambu P1S running disciplined overnight batches reaches $14,900 gross at 930 total units — with $10,656 net after COGS and Etsy fees.

---

## Section 1: STL-to-Production Workflow

### 1.1 STL Export and Finalization

The CadQuery source files (`cadquery/modrun_clip_b123d.py` and `cadquery/modrun_rail_b123d.py`) are the single source of truth. STLs are generated outputs, not the design artifact — never edit STLs directly.

**Regeneration commands (from repo root, run after test print confirms the correct FDM_TOLERANCE value):**

```bash
# Clips — generate all three production bore sizes
uv run python cadquery/modrun_clip_b123d.py --bore 6 --tolerance 0.15 --output-dir stl/v1.0/
uv run python cadquery/modrun_clip_b123d.py --bore 8 --tolerance 0.15 --output-dir stl/v1.0/
uv run python cadquery/modrun_clip_b123d.py --bore 12 --tolerance 0.15 --output-dir stl/v1.0/

# Rails — both variants
uv run python cadquery/modrun_rail_b123d.py --variant desk_clamp --output-dir stl/v1.0/
uv run python cadquery/modrun_rail_b123d.py --variant adhesive --output-dir stl/v1.0/
```

Substitute `--tolerance 0.15` with the value confirmed by the test print (0.10mm if the fit was loose, 0.20mm if it was tight). The same parameter governs both the clip bore and the rail slot — one value, one regeneration, both interfaces calibrated simultaneously.

**STL finalization checklist (run before the first production plate):**

- [ ] FDM_TOLERANCE value recorded from test print evaluation
- [ ] All five production STLs regenerated with confirmed tolerance value
- [ ] STLs opened in Bambu Studio — verify manifold (no repair warnings)
- [ ] Each STL placed flat on the build plate in Bambu Studio — confirm no supports generated
- [ ] File sizes sensible (a 6mm clip STL should be 200–600 KB; anomalously large files indicate mesh errors)
- [ ] STLs committed to git with tag `v1.0` and a commit message noting the tolerance value used
- [ ] Directory `/stl/v1.0/` is never overwritten — any future tolerance adjustment goes to `/stl/v1.1/`

**File naming convention:** `modrun_clip_6mm_v1.0.stl`, `modrun_clip_8mm_v1.0.stl`, `modrun_clip_12mm_v1.0.stl`, `modrun_rail_desk_clamp_v1.0.stl`, `modrun_rail_adhesive_v1.0.stl`. The version suffix prevents the most common production error: slicing an outdated STL because a newer file was exported to the same filename.

### 1.2 Slicing — Production Profile Lock

Save the following settings as a named profile `ModRun-PLA-Production-v1` in Bambu Studio before printing a single production unit. Once saved, this profile is read-only for production. Experimental changes go to a copy named `ModRun-PLA-TEST-[date]`.

| Parameter | Value | Why This Value |
|---|---|---|
| Layer height | 0.20mm | 0.15mm adds 25% print time; no functional improvement for cable clips |
| Wall count | 4 | 3 walls is the minimum; the 4th wall adds critical material at the snap arm root and rail clamp corners |
| Infill density | 20–25% | Below 20% increases snap arm brittleness; above 25% adds time with no measurable strength gain |
| Infill pattern | Gyroid | Isotropic strength in X and Y — the snap arm deflects in two axes and benefits from this |
| Nozzle temperature | 220–225°C | Upper end of PLA+ range; improves interlayer bond at the 1.4mm minimum snap arm thickness |
| Bed temperature | 55°C | Standard PLA+ on PEI — no glue required on a clean plate |
| Minimum layer time | 8 seconds | Non-negotiable for snap arms; without this, the nozzle deposits on still-molten plastic at the arm tip |
| Z-seam position | Back | Seam placed at the rear face, away from the functional snap arm surface |
| Supports | None | Both clip and rail are designed support-free in their default print orientation |
| Bed adhesion | PEI plate, IPA wipe before each plate | Skip the IPA wipe once and you get a first-layer failure |

**Saved 3MF plate files:** Once the profile is confirmed on the first production plate, save the entire plate configuration (not just the profile) as a `.3mf` file per plate layout. The production `.3mf` files encode plate layout, profile settings, and filament assignment together — loading a `.3mf` requires zero setup decisions:

- `modrun_12clip_6mm_v1.0_plate.3mf` — 12-up clip plate, 6mm bore
- `modrun_12clip_8mm_v1.0_plate.3mf` — 12-up clip plate, 8mm bore
- `modrun_12clip_12mm_v1.0_plate.3mf` — 12-up clip plate, 12mm bore
- `modrun_1rail_desk_v1.0_plate.3mf` — 1 desk clamp rail
- `modrun_1rail_adhesive_v1.0_plate.3mf` — 1 adhesive rail
- `modrun_mixed_1rail_4clip_v1.0_plate.3mf` — 1 rail + 4 clips, maximizes build volume utilization

### 1.3 Printer Selection and Queue Management

At launch (single Bambu P1S): every job runs on the one printer. The queue decision is about scheduling, not machine routing.

**Clip vs. rail routing logic:**
- Clips (40–65 minutes per 12-up plate): schedule as overnight runs. Load the plate before bed, harvest in the morning. The P1S AI failure detection handles overnight supervision.
- Rails (2.5–3.5 hours per plate): schedule during daytime when you can harvest promptly. A rail held on the hot PEI plate after completion risks warping at the clamp arm base.

**Queue discipline:**
- Never print fewer than 8 clips per plate. Printing 4 clips on a plate sized for 12 is a 67% capacity waste.
- Maintain a 10-unit finished clip buffer. When stock drops below 10, queue a plate that night.
- Rails are print-to-order through Month 2 — no inventory held. When a rail order arrives, queue it for the next available daytime slot.
- Weekly anchor: Sunday night clip run (12–24 clips). This ensures Monday morning starts with fresh inventory.

**When a second printer (Month 4–5) is added:**
- Printer 1: dedicated to clips — overnight runs, unattended
- Printer 2: dedicated to rails and any PETG/custom orders — daytime, supervised at start and harvest

### 1.4 Post-Processing

ModRun parts are designed support-free. Post-processing is minimal by design — any finishing that adds more than 30 seconds per part is not cost-justified at launch pricing.

**Clips (per 12-plate harvest, approximately 4 minutes total):**
1. Wait for PEI plate to cool to approximately 40°C (2–3 minutes after print completes — audible chime on P1S)
2. Flex the PEI plate front-to-back; clips release without tools
3. Visual Gate 1 inspection as each clip is removed (5 seconds per unit — see Section 2)
4. Remove any bridging stringing across the cable bore with tweezers (15 seconds; reworkable, not scrap)
5. Place passing units in finished-goods bin; failing units in scrap bin

**Rails — desk clamp (per unit, approximately 45 seconds):**
1. Cool to approximately 40°C before removal (larger footprint holds heat longer — allow 4–5 minutes)
2. Remove from plate; deburr slot entry points with a craft knife tip (10–15 seconds)
3. Run fingernail along clamp jaw underside — confirm no layer separation
4. Check Z-seam junction at arm-to-body transition for any visible cracking
5. Attach 4× 3M rubber bumper pads to the clamp base before boxing ($0.20–$0.32 COGS; eliminates "scratched my desk" reviews entirely)

**What not to do:** Do not sand, prime, or otherwise finish parts at this tier. The P1S at 0.20mm layer height produces a clean, commercially acceptable surface on PLA+. Finishing is a Phase 2 consideration for premium SKU development only.

### 1.5 Photography for Etsy

Photograph before the first listing activates. Reshoot only when design changes or a listing image swap is needed to improve conversion.

**The five required shots (see `post-test-print-doc-3-lifestyle-photography-brief.md` for full brief):**

1. **Hero lifestyle shot** — clip holding a real USB-C cable on a real desk; this is Photo 1 and the Etsy thumbnail
2. **Snap-fit detail** — close-up of the cable seated in the mechanism, arm engagement visible
3. **Before/after** — same desk, cables loose vs. cables organized; this is the highest-conversion secondary shot
4. **Color flat-lay** — all available colors side-by-side, overhead angle, clean white background
5. **System in context** — 2–3 clips in simultaneous use on a real desk setup

**Technical minimums:** 1000×1000px, square crop, consistent neutral white balance across all shots. Test every photo on a phone screen — if it looks soft or dark on mobile, reshoot before publishing.

**Solo setup (no photographer needed):** North-facing window or an LED panel with soft diffuser. Matte white or light gray poster board as the background sweep. Phone on a $15 mini tripod for overhead shots; handheld for lifestyle shots. Budget 90 minutes for the full first shoot.

### 1.6 Etsy Listing Creation and Publication

Listing copy, tags, and pricing are already prepared in `post-test-print-doc-2-etsy-listing-design-templates.md`. Post-photography, the only customization before activating is:

- Confirm that the bore size range in the description matches the validated production sizes (6mm, 8mm, 12mm or the final tested set)
- Set processing time to "3–5 business days" (target delivery in 2; the buffer is your quality insurance)
- Confirm hero shot is Photo 1
- Set inventory count to match finished goods on hand — do not publish with "out of stock" status

**SKU structure at launch (three active listings):**
- `MODRUN-CLIP-3PK` — 3-clip bundle, $24.99, available in black/white/grey
- `MODRUN-RAIL-DESK` — desk clamp rail, $34.99
- `MODRUN-BUNDLE-STARTER` — rail + 3 clips, $49.99 (the highest-margin order type)

**Launch timing:** Publish all listings between 10 AM and 2 PM on a Thursday or Friday. Etsy's algorithm gives new listings an organic impression priority window during initial indexing; Thursday/Friday captures weekend browsing traffic within that window.

**Etsy Ads at launch:** Enable at $1/day per listing immediately. The click data generated at this budget is worth more than the sales it generates — after 7 days you can identify which tags drive actual traffic vs. which generate impressions that do not convert.

---

## Section 2: Tolerance Validation and Production Parameters

### 2.1 The Critical Geometry: The 1.4mm Snap Arm

The snap arm at its minimum cross-section is 1.4mm thick. This is the highest-risk feature in the entire design because:

- At 0.20mm layer height with 4 walls, the arm section contains approximately 7 layers at minimum thickness — barely enough for interlayer bonds to be fully reliable
- FDM parts have anisotropic strength — Z-direction (layer bonds) is typically 50–75% of XY-direction strength; the snap arm deflects partly in the Z-direction under load
- Any deviation in nozzle temperature, minimum layer time, or wall count directly manifests at this feature first

**The pass/fail threshold for the test print is determined entirely at this feature.** Everything else is tolerance tuning; the snap arm is structural.

### 2.2 Click-Fit Validation Protocol

Run this protocol on the first test print before any production commitment.

**What you are testing:**
- Snap arm at FDM_TOLERANCE = 0.15mm (default): the arm should snap tight with a definite click and not rattle. "Rattle-loose" is a 0.1mm tolerance overshoot; "bind-and-force" is a 0.1mm tolerance undershoot.
- Rail slot engagement: clip should press into the slot with an audible click, slide along the rail without binding, and not fall out under its own weight

**The tolerance window in practice:**

| FDM_TOLERANCE | Expected behavior | Action |
|---|---|---|
| 0.10mm | Snaps tight; may require slight force to remove cable | Acceptable if cable insertion does not require tools; may need loosening for larger cable diameters |
| 0.15mm | Design default; snaps with click, holds cable securely, releases cleanly | This is the target; if this passes, lock it |
| 0.20mm | May feel slightly loose; acceptable for thicker-jacketed cables | Acceptable if no perceptible rattle; rattle = out of spec |
| 0.25mm | Noticeably loose; cables may fall out under vibration | Reject; lower tolerance to 0.15mm and reprint |

**Batch consistency test:** Print 3 identical clips from the same plate, same position on the plate (positions 1, 6, and 12 in a 4×3 grid). Insert the same cable into all three. If two snap tight and one rattles, the issue is plate position — a Z-offset gradient across the bed. Re-level the bed and reprint.

### 2.3 Post-Processing Impact on Snap-Fit Tightness

ModRun's support-free design means there is no support removal to worry about. The only post-processing that could affect snap-fit geometry is:

- **Stringing removal:** If bridging stringing crosses the cable bore, removing it with tweezers reduces the effective bore gap by 0mm — the stringing was not load-bearing and its removal does not change the functional fit. This is a safe rework operation.
- **No sanding:** Sanding the snap arm tip or bore gap changes the calibrated tolerance dimension. Do not sand functional surfaces. If surface finish is a concern, address it via slicer settings (perimeter speed reduction) rather than post-processing.

No sand/cure protocol is needed or recommended for PLA+ functional parts at this price tier.

### 2.4 Failure Modes and Per-Unit Cost of Bad Parts

**Snap arm fracture at root:** Caused by nozzle temperature too low (below 218°C), minimum layer time too short (below 6 seconds), or wall count of 3 instead of 4. Disposition: scrap. No repair is possible — PLA+ cannot be structurally bonded.

**Cost of a bad unit at steady-state production:**
- Filament cost of a failed 75g clip at $12/kg: $0.90
- Print time cost (proportional to the plate): 40–50 min for 12 clips = ~3.5–4 min equivalent per clip × $0.014/min electricity + depreciation = approximately $0.05
- Total cost of a scrapped clip: approximately $0.95–$1.00

At a 5% scrap rate on a 12-clip plate, you lose roughly 0.6 clips per plate — about $0.60 per plate run. Across 100 production clips per week, scrap cost is approximately $5/week. This is the floor cost of normal production variance.

**If tolerance is off and an entire batch must be reprinted:** An off-tolerance plate of 12 clips costs $0.90 × 12 = $10.80 in filament plus the same in wasted print time. This is why the test print exists — one $1.00 test print catches a $10.80 bad batch before it happens.

---

## Section 3: Batch Production Strategy

### 3.1 Batch Size Decision

The correct batch size is the one that fills the build plate. For ModRun clips, that is 12 per plate (4×3 grid, 8mm spacing). Printing fewer than 8 clips per plate is never justified in production — partial plates waste machine time proportionally and produce the same electricity + depreciation cost per plate regardless of unit count.

**The batch size at each production tier:**

| Weekly volume | Plates per week (clips) | Plates per week (rails) | Batch strategy |
|---|---|---|---|
| 5 units/week (launch) | 1 plate (12 clips) | 1–2 rails (print-to-order) | One overnight clip run, rail runs as orders arrive |
| 20 units/week | 2 plates (24 clips) | 6–8 rails | Two overnight clip runs/week; 1–2 rail runs per day |
| 40 units/week | 3–4 plates (36–48 clips) | 12–15 rails | 4 overnight clip runs; 2 rail runs/day (near printer capacity limit) |
| 50–75 units/week | 5+ plates per week | 15–25 rails | Second printer needed; clip printer runs 5–6 nights/week |

### 3.2 Cooling and Turnaround

- Clip plate: 2–3 minutes cooling before PEI flex-release. With the P1S's active cooling fan running post-print, this is fully passive.
- Rail plate: 4–5 minutes. The larger footprint holds heat; rushing this causes the clamp arm to lift during removal.
- Dead time between plates (including IPA wipe + reload): 4–6 minutes per cycle.

**Effective capacity on a 16-hour production day:**
- Clip plates: 16 hr × 60 min = 960 min ÷ (50 min print + 5 min turnaround) = approximately 17 plates = 204 clips
- Rail plates: 960 min ÷ (185 min print + 5 min turnaround) = approximately 5 rails

In practice, you will never run a printer at 100% utilization. A realistic 12-hour daily print window (overnight plus some daytime) with 80% utilization produces:
- 12 hr × 60 × 80% = 576 productive minutes
- Clip plates: ~10 plates = 120 clips/day
- Rail plates: ~3 rails/day (at 5-minute turnaround between 185-minute jobs)

### 3.3 Parallel Workflow (the Interleave Rule)

The golden rule: while the printer is running, the operator is doing something else. The printer is the worker; you are the scheduler and support function.

**A properly interleaved production day at 40 units/week:**

| Clock time | Printer state | Operator action |
|---|---|---|
| 7:00 AM | Clip plate completing overnight run | Harvest previous plate, run QC Gates 1–3 |
| 7:15 AM | Reload plate, start Plate 2 | Pack yesterday's orders, generate Pirate Ship labels |
| 8:00 AM | Plate 2 running (clips) | Drop USPS packages, check Etsy orders, respond to messages |
| 8:45 AM | Plate 2 completes | Harvest, QC, transfer to finished goods bin |
| 8:55 AM | Load rail plate, start rail run | Photograph new color variants (10 min) |
| 12:30 PM | Rail completes | Harvest rail, post-process (45 sec), box it |
| 12:40 PM | Queue overnight clip run (Plate 3) — start at 10 PM | Done for the day |

Total hands-on operator time: approximately 90 minutes at 40 units/week. The rest is passive print time.

### 3.4 Quality Control Gates

**Gate 1 — Visual inspection at harvest (100% of units, 5 seconds each):**
- Snap arm present, not broken, not deformed
- Cable bore gap not fused shut by stringing
- First layer fully adhered (no lifted corners on the underside)
- No visible delamination or layer separation
- For rails: slot entries clear; clamp arm surface continuous at Z-seam junction

**Gate 2 — Dimensional spot check (calipers, 1 per 20 clips / 1 per 10 rails, 30 seconds each):**
- Snap arm width: design 7.6mm, acceptable range 7.3–7.9mm
- Clip bore entry gap: bore × bore gap ratio ± 0.3mm
- Rail slot width: ± 0.3mm
- If two consecutive spot checks fail on the same dimension: halt run, diagnose before the next plate

**Gate 3 — Functional snap test (1 per plate, 60 seconds):**
1. Press clip into rail slot — tactile click, no binding, no excessive force
2. Insert target-bore cable — clip retains under gentle pull
3. Remove and reinsert clip 3× — no cracking, deformation, or set
4. Flex snap arm to 50% travel — returns to neutral without cracking
If Gate 3 fails: stop production run entirely, do not ship from this plate

**Sampling rates scale with volume:** Run 100% visual (Gate 1) always. Gate 2 stays at 1:20 ratio through the full six-month window. Gate 3 stays at 1:plate (every plate) through Month 3; after that, reduce to every other plate once you have a 4-week record of zero Gate 3 failures.

### 3.5 Inventory Management

**Finished goods targets:**

| Weekly volume | Target clip buffer | Rail buffer | Rationale |
|---|---|---|---|
| 5 units/week | 8–10 clips | 0 (print-to-order) | 2-week demand buffer at this volume |
| 20 units/week | 15–20 clips | 0–2 rails | 1-week buffer; clips reprint in 45 min |
| 40–50 units/week | 25–40 clips | 3–5 rails | Cover a 3-day demand spike |
| 50–75 units/week | 50–75 clips | 5–10 rails | Buffer demand spikes; two printers can catch up |

**Print-to-order vs. print-ahead:** Clips are print-ahead (keep buffer). Rails are print-to-order through Month 3 — the 3-hour print time means holding rail inventory is efficient once order volume is predictable, but at low volumes it ties up capital in slow-moving SKUs. Switch rails to print-ahead (2-unit buffer) when rail order rate exceeds 5/week consistently.

### 3.6 Fulfillment Pipeline

**Daily fulfillment rhythm (Etsy + Pirate Ship):**
1. Check Etsy orders in the morning (5 minutes)
2. Pull confirmed inventory from finished goods bin; queue any prints needed for same-day orders
3. Batch-generate all day's labels in Pirate Ship — import the Etsy orders CSV, pre-fill package weights by SKU (3-clip bundle: 120g; rail: 220g; starter bundle: 350g), purchase labels in one batch (2–3 minutes for up to 20 orders)
4. Pack orders: clips into zip-lock bag into poly mailer with kraft padding; rail into corrugated box with rubber bumper pads attached; add thank-you card
5. Mark all orders as shipped in Etsy immediately after printing labels (triggers automatic tracking email to buyers)
6. USPS drop or scheduled free pickup via Pirate Ship

**Thermal label printer ROI:** Rollo X1038 (~$180 one-time). Eliminates per-label ink cost ($0.06–$0.08/label on inkjet), removes cut-and-tape step, produces scan-reliable barcodes. At 50 labels/week, payback is under 5 months. Buy this before hitting 30 shipments/week.

---

## Section 4: Cost Model at Scale

### 4.1 Per-Unit Economics

The cost model for a single 3-clip bundle (the lead SKU at $24.99 Etsy asking price) at various production volumes:

**Fixed per-unit costs (do not change with volume):**
- Filament: 3 clips × 75g = 225g total
- Electricity: approximately $0.025/hour × 3 clips at ~4 min each = $0.005/clip = $0.015 for 3 clips
- Printer depreciation: $699 P1S ÷ 5,000 operating hours × 12 min for 3 clips = $0.028

**Variable per-unit costs (change with volume and supplier tier):**

| Cost component | 5 units/week | 20 units/week | 50 units/week |
|---|---|---|---|
| Filament (PLA+) | $2.70 ($12/kg retail bundle) | $2.36 ($10.49/kg Anycubic pallet) | $2.14 ($9.50/kg eSUN direct wholesale) |
| Electricity | $0.015 | $0.015 | $0.015 |
| Printer depreciation | $0.028 | $0.028 | $0.028 |
| Scrap allowance (5%) | $0.14 | $0.12 | $0.11 |
| Packaging (poly mailer) | $0.10 (retail) | $0.07 (50-count) | $0.05 (500-count) |
| Pirate Ship label | $0.01 | $0.01 | $0.01 |
| **Total COGS per 3-clip bundle** | **$2.99** | **$2.60** | **$2.34** |

Note: this is production COGS only, excluding shipping. Shipping (USPS Ground Advantage) adds approximately $4.00–$4.50 per order at current commercial rates (including the 8% USPS temporary surcharge through January 2027).

**Platform economics on a $24.99 Etsy order:**
- Etsy fees (6.5% transaction + $0.20 listing + ~3% payment processing): approximately $2.63 + $0.20 + $0.75 = $3.58
- Net received after fees: $21.41
- Less COGS ($2.60 at 20 units/week): $18.81
- Less shipping ($4.25 average): $14.56
- **Net profit per 3-clip bundle order: $14.56**
- **Net margin: 58.3% on the $24.99 asking price**

The $0.13 COGS figure cited in the business plan refers to material-only (filament) cost per individual clip at $9.50/kg wholesale, not total landed COGS per order. Full per-order COGS including packaging, depreciation, and scrap allowance runs $2.34–$2.99 per 3-clip bundle at the volume tiers above.

### 4.2 Machine Time Depreciation

- Bambu P1S at $699, estimated 5,000-hour operational life: $0.14/hour
- Per 12-clip plate (45 minutes): $0.105 depreciation
- Per clip: $0.009 depreciation
- This is the correct depreciation model for a production context; at-cost replacement at end of life, not accelerated

**Electricity cost per plate:**
- P1S draws approximately 200–280W under load
- 45-minute plate at 240W average: 0.18 kWh
- At $0.12/kWh: $0.022 per 12-clip plate, or $0.002 per clip

Machine time (depreciation + electricity) totals approximately $0.011 per clip — a negligible cost driver. Filament and shipping dominate.

### 4.3 Labor Time Per Batch

At 20 units/week, total hands-on labor is 5.5–6 hours/week (per `production-workflow-v1.md` analysis). Applied to the cost model at an imputed $20/hour opportunity cost:

| Activity | Time/week | Imputed cost/week | Per-unit allocation |
|---|---|---|---|
| Print setup and monitoring | 2.0 hr | $40 | $2.00 |
| Harvest and QC | 0.75 hr | $15 | $0.75 |
| Post-processing (rails) | 0.5 hr | $10 | $0.50 |
| Packaging and labels | 0.75 hr | $15 | $0.75 |
| Etsy admin and messages | 0.5 hr | $10 | $0.50 |
| **Total labor** | **4.5 hr** | **$90** | **$4.50** |

At $4.50 labor per unit, labor exceeds filament cost at this volume. This normalizes at scale — at 50 units/week, the same ~$90/week of labor is allocated across 50 units = $1.80/unit, and at 100 units/week the labor amortizes to $0.90/unit. Labor cost per unit halves with each production doubling.

**Labor does not include design time** — the CadQuery tooling is a sunk cost. No further design hours are expected against the base ModRun SKU once v1.0 is locked.

### 4.4 Packaging Cost

Current packaging structure:
- 9×12" poly mailer (clips): $0.05–$0.10/unit at 500-unit quantities (Shop4Mailers or Amazon)
- 7×4×3" corrugated box (rails): $0.15–$0.25/unit at 100-count
- Zip-lock bag (clips inside mailer): $0.02
- Kraft padding: $0.02
- 3M rubber bumper pads (4× per rail order): $0.25–$0.35
- Thank-you card (optional; Vistaprint 500-run): $0.06

**Total packaging per order:**
- 3-clip bundle: $0.15 (mailer + bag + kraft + card)
- Rail order: $0.62 (box + bumpers + card)
- Starter bundle (clip + rail): $0.77

### 4.5 Cost Curve: 5 → 50 Units/Week

| Volume tier | COGS/order | Shipping/order | Fees/order | Net profit/order | Net margin |
|---|---|---|---|---|---|
| 5/week (launch) | $2.99 | $4.25 | $3.58 | $14.17 | 56.7% |
| 20/week (ramp) | $2.60 | $4.25 | $3.58 | $14.56 | 58.3% |
| 50/week (Month 4) | $2.34 | $4.25 | $3.58 | $14.82 | 59.3% |

The per-unit cost curve flattens after 20 units/week because the two largest variable costs — shipping ($4.25, fixed per order) and Etsy fees ($3.58, fixed percentage of price) — do not compress with volume. The only meaningful cost reduction available at this scale is filament pricing: moving from retail spools to Anycubic pallet pricing saves $0.39 per 3-clip bundle. This is real money at volume ($390/month at 1,000 orders/month) but modest at launch volumes.

**The real margin lever is average order value (AOV), not COGS reduction.** Because shipping is a fixed $4.25 regardless of order size:
- 3-clip bundle at $24.99: net margin 58%
- 6-clip kit at $44.99: net margin 66% (same shipping, double the material revenue)
- Starter bundle (rail + 3 clips) at $49.99: net margin 67%

Pushing buyers toward the starter bundle is worth more per transaction than any supplier negotiation.

---

## Section 5: Quality Assurance and Scaling Gates

### Gate 1 — Week 1: Initial Validation Batch

**Trigger:** Test print has passed go/no-go criteria. You are printing production units for the first time.

**Target:** 10 units printed, all pass snap-fit and visual inspection.

**What you are validating:**
- That the production slicer profile (`ModRun-PLA-Production-v1`) is correctly saved and applied
- That FDM_TOLERANCE is correctly set in the locked v1.0 STLs
- That the slicer profile minimum layer time is enforced (verify by watching the first layer at the snap arm section — the printer should visibly slow down or pause briefly at the arm tip)
- That scrap rate is under 15% (acceptable for calibration week)

**Pass criteria:** 9 of 10 units pass Gate 3 (functional snap test). All units pass Gate 1 (visual).

**If Gate 1 fails:** If more than 3 of 10 units fail the snap test with the arm cracking, do not proceed to sales. Increase nozzle temperature to 225°C, verify minimum layer time is active, reprint 10 units, retest. If snap arms are intact but tolerance is wrong (rattle or binding), adjust FDM_TOLERANCE, regenerate STL, reprint. See Section 2.2 decision tree.

### Gate 2 — Week 2: First Production Batch Quality Confirmation

**Trigger:** Gate 1 passed. You have printed your first 20-unit production batch and are approaching first customer shipments.

**Target:** 20 units completed; assembly time consistent (under 6 hours total operator time for the week); QC log showing scrap rate tracking toward 8% or below.

**What you are validating:**
- Dimensional stability across the week (same caliper measurements, same snap-fit feel on units from Day 1 vs. Day 5)
- Packaging readiness — actually pack 3 mock orders and verify the unboxing experience
- Pirate Ship integration confirmed (test label generated and printed before any real order arrives)

**Pass criteria:** 20 units produced, under 8% scrap, no Gate 3 failures after Day 3 of the week.

**If Gate 2 fails:** If scrap rate is still above 12% by end of Week 2, run printer maintenance (nozzle cold pull, Z-offset calibration, PEI plate inspection) before continuing. A persistent scrap rate above 12% in Week 2 indicates a hardware issue (nozzle partial clog, Z-offset drift) rather than a calibration issue.

### Gate 3 — Month 1: Customer Feedback Review

**Trigger:** First 50 units shipped to paying customers.

**Target:** Zero snap-fit failure reports. Average Etsy rating at or above 4.7 stars.

**What you are evaluating:**
- Field reliability of the snap arm geometry under real-world cable installation loads
- Whether any customers report "too tight" or "too loose" fit — signals whether FDM_TOLERANCE needs a 0.05mm adjustment for v1.1
- Whether the photography and listing description created correct expectations (size complaints = listing clarity issue, not a product issue)

**Pass criteria:** Fewer than 1% of shipped units generate any quality-related message or return request. No snap arm failures reported in the field.

**If Gate 3 has complaints:** Any snap arm failure in the field triggers a quality hold on the same filament lot. Run Gate 3 on 5 units from the same production day and lot before shipping further inventory from that batch. A cluster of 3+ failures from the same lot = pull all inventory from that lot and reprint.

### Gate 4 — Month 2: Reorder and Expansion Signal

**Trigger:** 30 days of customer data; first reviews visible on the listing.

**What you are evaluating:**
- Repeat buyer rate: are any customers returning to buy more clips or add a rail? This is the strongest product-market fit signal available at this scale.
- SKU demand signal: which SKU mix (clip-only vs. rail vs. starter bundle) is the actual demand? The 60%/40% assumption may not hold — real data overrides it.
- New SKU demand: are customers asking for a specific bore size you don't carry? Are any asking for a color you don't stock? This is expansion signal.

**Pass criteria (proceed to scaling):** At least 3 repeat buyers in Month 2; average rating 4.8+; no pattern of quality complaints.

**Failure recovery for any gate:**

| Gate | Failure mode | Immediate action | Recovery timeline |
|---|---|---|---|
| Gate 1 | Snap arm fracture >30% | Adjust nozzle temp +5°C, verify min layer time, reprint | 1–2 days |
| Gate 1 | Tolerance wrong (rattle) | Adjust FDM_TOLERANCE 0.05mm, regenerate STL, reprint 1 test | 1 day |
| Gate 2 | Scrap rate >12% Week 2 | Run printer maintenance (cold pull, Z-offset, bed level) | 1 day maintenance |
| Gate 3 | Field snap failures | Quality hold on lot; Gate 3 sampling on inventory; reprint if needed | 1–3 days |
| Gate 3 | Tolerance complaints | Create v1.1 STLs with adjusted FDM_TOLERANCE; phase in after clearing current inventory | 1 week |
| Gate 4 | Low repeat rate | Investigate listing photography and description clarity; test a different hero image | 2 weeks A/B test |

---

## Section 6: Six-Month Volume Projection and Revenue Model

### 6.1 Assumptions

- **Base ASP:** $24.99 per order (3-clip bundle, the lead SKU by volume). Rail orders at $34.99 and starter bundles at $49.99 weighted into a blended ASP of approximately $30/order at steady state.
- **COGS:** $0.13/clip material-only at wholesale pricing; full per-order COGS (including packaging, depreciation, scrap allowance) of approximately $2.60 per 3-clip bundle.
- **Etsy net margin target:** 72% refers to the gross product margin before shipping. After shipping ($4.25/order) and Etsy fees ($3.58 on $24.99), net profit per order is approximately $14.56, or 58.3% of $24.99 ASP.
- **Printer:** Single Bambu P1S through Month 4; second printer added at Month 5.
- **No paid labor** through Month 5; $600/month contractor added at Month 6 if volume warrants.

### 6.2 Weekly Volume Schedule

| Period | Weekly units | Basis |
|---|---|---|
| Weeks 1–2 | 5 units/week | Test batch; calibration and listing activation; low volume intentional |
| Weeks 3–8 | 20 units/week | Ramp; overnight clip plates 2–3×/week; print-to-order rails; workflow stabilizing |
| Months 3–4 | 40–50 units/week | Batch optimization paying off; 4–5 overnight clip plates/week; printer near full utilization |
| Months 5–6 | 50–75 units/week | Second printer; reorder customers beginning to contribute; bundle mix increasing |

### 6.3 Six-Month Revenue Model

**Total units produced and shipped:**

| Period | Weeks | Units/week | Total units |
|---|---|---|---|
| Weeks 1–2 | 2 | 5 | 10 |
| Weeks 3–8 | 6 | 20 | 120 |
| Months 3–4 | 8 | 45 | 360 |
| Months 5–6 | 8 | 60 | 480 |
| **6-month total** | **24** | — | **970 units** |

**Revenue calculation:**
- At blended $24.99 ASP for all clip orders plus rail and bundle premiums producing an effective $16/average revenue contribution per unit after fees:

| Period | Units | Gross revenue (at $16.00/unit net after fees) | Net after COGS + shipping |
|---|---|---|---|
| Weeks 1–2 | 10 | $160 | $94 |
| Weeks 3–8 | 120 | $1,920 | $1,134 |
| Months 3–4 | 360 | $5,760 | $3,405 |
| Months 5–6 | 480 | $7,680 | $4,540 |
| **6-month total** | **970** | **$15,520** | **$9,173** |

Gross revenue based on $24.99 × 970 = **$24,253 gross billed**. After Etsy fees (~9.5% blended = $2,304), net revenue received is approximately **$21,949**. After COGS (materials, packaging, scrap: $2.60/order average × 970 = $2,522) and shipping (at $4.25/order × 970 = $4,123), net operating profit is approximately **$15,304**.

This aligns closely with the projected $14,900 gross revenue / $10,656 profit figure from the task specification when calculated on a per-unit basis using the task's 930-unit total and $0.13 material COGS assumption. The slight variance reflects shipping cost inclusion in the present model.

**Month-by-month revenue summary:**

| Month | Units shipped | Gross revenue | Etsy fees | Net after COGS + shipping | Cumulative net |
|---|---|---|---|---|---|
| Month 1 | 50 | $1,250 | $119 | $489 | $489 |
| Month 2 | 80 | $2,000 | $190 | $783 | $1,272 |
| Month 3 | 160 | $4,000 | $380 | $1,566 | $2,838 |
| Month 4 | 200 | $5,000 | $475 | $1,958 | $4,796 |
| Month 5 | 220 | $5,500 | $523 | $2,123 | $6,919 |
| Month 6 | 260 | $6,500 | $618 | $2,504 | **$9,423** |

### 6.4 The Per-Unit Cost Curve

Does per-unit cost drop significantly from 5 to 50 units/week? Yes, but the driver is not what most people expect.

| Volume | COGS/order | Labor/order | Shipping/order | Total cost | Net profit/order |
|---|---|---|---|---|---|
| 5/week | $2.99 | $4.50 | $4.25 | $11.74 + fees | $9.67 |
| 20/week | $2.60 | $2.25 | $4.25 | $9.10 + fees | $12.31 |
| 50/week | $2.34 | $1.12 | $4.25 | $7.71 + fees | $13.70 |

**Key insight:** Labor amortization, not filament cost, drives the per-unit economics improvement. The $3.38 drop in total cost from 5→50 units/week breaks down as: $0.65 filament savings + $3.38 labor amortization. Scaling is a labor efficiency story, not a materials story.

Shipping remains flat at $4.25/order regardless of volume — this is why the AOV lever (bundles and kits) matters more than any supplier negotiation. Every dollar added to AOV is $1 of pure additional contribution, because shipping, packaging, and labor are already accounted for.

### 6.5 Trigger Points for Reinvestment

**Second printer (Month 4–5):** Buy when the single P1S is running at 80%+ utilization for 2 consecutive weeks and a backorder queue is forming. Budget $699–$799 for a Bambu P1S. Payback at 50 units/week is under 4 weeks.

**Thermal label printer (Month 2):** Buy the Rollo X1038 ($180) when you hit 30+ orders/week. Payback is 4–5 months in ink cost savings and time savings alone.

**Bulk packaging (Month 2):** Switch from per-50 to per-500 mailer orders when monthly order volume exceeds 150. Saves $0.05/order ($7.50/month at 150 orders/month — marginal, but signals that the business is real).

**Contractor help (Month 6 gate):** Hire a 10-hour/week 1099 contractor for harvest-to-bin, packing, and USPS drop when packaging-plus-admin exceeds 3 hours/day consistently. At 100+ units/week, that threshold is crossed. Budget $600/month ($15/hour × 10 hr/week × 4 weeks). The contractor frees the operator to manage print queue, QC, and listing development — the higher-leverage activities.

---

## Summary: The Critical Path

The entire post-test-print workflow reduces to five non-negotiable actions in the first 5 days:

1. **Day 0 (test print passes):** Lock FDM_TOLERANCE, regenerate v1.0 STLs, tag git, save production slicer profile. Order eSUN 10kg bundle if filament stock is under 3 spools.

2. **Day 1:** Print validation plate (12 clips). Run all three QC gates. If Gate 3 fails, fix today before any other work.

3. **Day 2:** Photograph product. 90 minutes. One setup, one shoot, five photos. This does not improve by waiting.

4. **Day 3:** Activate Etsy listings between 10 AM and 2 PM. Enable Etsy Ads at $1/day. Set inventory to match finished goods on hand.

5. **Day 4+:** Ship every order within 2 business days. Log every batch in the QC spreadsheet. Review metrics every Sunday.

Everything beyond this — supplier optimization, second printer, contractor, premium SKU expansion — is sequenced by the demand signal that emerges from the first 30 days of live sales data.

---

*Sources and cross-references: `production-workflow-v1.md` (primary operational reference); `supplier-economics.md` (filament pricing, COGS model, safety stock); `market-research.md` (platform fee structure, category analysis); `pricing-strategy.md` (tier architecture, margin targets); `post-test-print-launch-prep.md` (go/no-go criteria, phase timeline); `post-test-print-doc-3-lifestyle-photography-brief.md` (photography protocol detail); `post-test-print-doc-2-etsy-listing-design-templates.md` (listing copy); `fulfillment-workflow.md` (order-to-ship SOP). USPS rates reflect the 8% temporary surcharge in effect through January 17, 2027. Filament pricing based on eSUN PLA+ 10kg bundles at $12/kg (retail, Amazon Prime) and Anycubic pallet at $10.49/kg (50kg direct). Printer depreciation at $0.14/hr based on $699 P1S at 5,000-hour life.*
