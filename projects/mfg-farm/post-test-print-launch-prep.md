---
title: ModRun Post-Test-Print Launch Preparation Package
date: 2026-04-28
version: 2.0
status: ready-for-execution
confidence: high
related: supplier-negotiation-playbook.md, fulfillment-workflow.md, launch-checklist.json, pricing-strategy.md, supplier-scorecard.csv
---

# ModRun Post-Test-Print Launch Preparation Package

**Status**: Ready for immediate execution upon successful test print confirmation
**Timeline**: 6 phases spanning 8 weeks from test print go/no-go decision
**Scope**: Complete operational and commercial launch from test print through $1,500+/month revenue run rate
**COGS Reduction Target**: 20% reduction from current retail-filament baseline through supplier negotiation

---

## Executive Summary

This package converts a successful test print confirmation into a live, revenue-generating Etsy operation in approximately two weeks, then scales to multi-product, multi-supplier operations through Month 3. All product design, pricing strategy, market research, and supplier analysis is complete (Sessions 290-544). This document provides the phased execution roadmap across six sequential phases, with parallel workstreams clearly identified.

**Key assumption**: Test print confirms ModRun clips (both modrun_clip and modrun_rail variants) meet dimensional tolerances within ±0.5mm, surface finish is commercially acceptable, and mechanical fit between rail and clip variants is satisfactory without post-processing.

**COGS reduction math**: Current retail PLA runs $14-15/kg. Supplier negotiation target is $10.49-12.50/kg (eSUN wholesale or Anycubic pallet). At 75g per unit, that is $0.97 vs $1.13 per unit — a 14% material cost reduction. Combined with Pirate Ship commercial rates vs. retail USPS (saving $0.80-1.50/shipment) and bulk packaging (poly mailers from $0.10 retail to $0.05 wholesale), the blended 20% COGS reduction target is achievable by Month 2.

**Etsy original design compliance**: As of June 2025, Etsy requires 3D-printed items to be based on the seller's original design. ModRun's CadQuery-parametric design files constitute original design work and are fully compliant. Do not sell prints of third-party STL files. Keep design provenance documentation (CadQuery source files, commit history) as evidence of originality if Etsy ever audits.

---

## Phase 1: Test Print Go/No-Go Decision (Day 0-1)

**Trigger**: Test print completes. This phase takes 1-2 hours.

### Go Criteria (All Must Pass)

Before proceeding to Phase 2, verify each criterion:

**Dimensional tolerances (±0.5mm)**
- [ ] Clip width at engagement face: target per CAD, tolerance ±0.5mm
- [ ] Rail channel width: target per CAD, tolerance ±0.5mm
- [ ] Clip-to-rail mechanical fit: snap engagement satisfying (not too tight, not too loose)
- [ ] Cable channel diameter range: 3-10mm cables seat without binding

**Surface quality**
- [ ] No visible layer separation or delamination
- [ ] No warping exceeding 1mm at any edge
- [ ] Surface finish acceptable for commercial sale (light layer lines are acceptable; rough or stringy is not)
- [ ] Color consistent throughout part

**Functional test**
- [ ] Clip snaps onto rail and releases cleanly in 5+ cycles without fatigue cracking
- [ ] Assembled clip+rail holds 5mm cable without slipping under gentle hand pull
- [ ] No sharp edges or burrs that would require post-processing before shipping

**Print reliability**
- [ ] Print job completed without manual intervention
- [ ] No failed layers or spaghetti detected
- [ ] Bambu P1S settings confirmed for production (210°C nozzle, 60°C bed, 0.2mm layer, 15% infill for PLA)

### No-Go Criteria (Any One Fails the Launch)

- Dimensional deviation >1.0mm on engagement surfaces (redesign required)
- Clip-to-rail fit fails — too tight to engage or falls off (redesign required)
- Warping >2mm at any edge (investigate bed adhesion, print settings)
- Layer separation visible — structural integrity concern (investigate settings, humidity)

### If No-Go: Immediate Corrective Actions

1. Document exact failure mode with calipers and photos
2. Adjust CadQuery parameters for dimensional issues
3. Adjust print settings for surface/warp issues
4. Re-print single test part (1-2 hours)
5. Re-evaluate against go criteria
6. Do not proceed to Phase 2 until go criteria pass

---

## Phase 2: Business Foundation (Days 1-5, Parallel Track A)

**Run in parallel with Phase 3. Estimated total time: 6-10 hours across multiple days.**

This phase is the administrative bedrock. None of these take long individually; the delays come from waiting for external responses (bank verification, state filing). Start all of them on Day 1.

### Business Entity and Registration

**Day 1 actions (1-2 hours)**:

1. **Decide on entity type**: Sole proprietor (simplest, file a DBA if desired) vs. LLC (liability protection, tax flexibility, $50-500 filing fee depending on state). For a product business with product liability exposure, LLC is recommended. Consult a tax professional for state-specific advice.

2. **Obtain EIN**: Free, instant online at irs.gov/ein. Takes 10 minutes. Do this before opening a business bank account.

3. **File LLC (if chosen)**: Submit Articles of Organization to your state's Secretary of State. Most states accept online filing. Processing time: instant (online, many states) to 4 weeks (paper, some states). Do not wait for this before starting other tasks — you can operate as a sole proprietor while LLC processes.

4. **Home occupation permit**: Check your county/city requirements. Search "[your municipality] home occupation permit." Most small-scale 3D printing operations qualify as low-impact home businesses. Cost: $0-300.

5. **Product liability insurance**: Contact TechInsurance or Hiscox for a $1M occurrence / $2M aggregate product liability policy. For non-load-bearing cable management accessories, expect $300-600/year. Do not launch without this.

### Business Banking

**Day 1-2 (30 minutes + 3-5 day verification wait)**:

6. **Open business checking account**: Recommended: Mercury Bank (no fees, instant online setup, business-friendly) or your current bank's business checking. Use your EIN (not SSN) if LLC. This creates the legal separation between personal and business finances that the IRS expects.

7. **Order business debit card**: Used for supplier purchases. Keeps expenses separate from personal spending.

### Tax Setup

8. **Confirm Etsy W-9 submission**: Etsy requires a W-9 (US sellers). This is filled out within the Etsy Payments setup. If you already have a personal Etsy account, you may need to update with business EIN.

9. **Set up basic bookkeeping**: Recommended: Craftybase ($49/month Studio plan — Etsy-native, tracks material COGS automatically as orders come in, generates IRS Schedule C data). Alternative: free Google Sheets with manual COGS tracking. Craftybase is worth $49/month once you have 20+ orders/month; before that, the manual spreadsheet is adequate.

### Insurance and Compliance Checklist

Before listing goes live:
- [ ] Business entity registered (LLC filed or sole proprietor established)
- [ ] EIN obtained from IRS
- [ ] Business bank account open and funded
- [ ] Product liability insurance policy active
- [ ] Home occupation permit obtained (or confirmed not required)
- [ ] Etsy W-9 submitted with correct business EIN/SSN

---

## Phase 3: Etsy Store Configuration (Days 1-5, Parallel Track B)

**Run in parallel with Phase 2. Estimated total time: 3-4 hours.**

### Etsy Account and Shop Creation

1. Create Etsy seller account at etsy.com/sell (or convert existing buyer account)
2. Shop name: "ModRun Design" or "ModRun Studio" — lock this in immediately, it cannot be changed without creating a new shop
3. Primary location: your state
4. Operating hours: 24/7 online; processing time: 2 business days (set on all listings)

### Shop Settings Configuration (Shop Manager → Settings)

**Basic tab**
- Shop announcement: "Original parametric cable management systems for creators and professionals." (160 character limit)
- Shop icon: 300x300px minimum. Use a clean product photo or simple ModRun wordmark.

**Shop Sections (create 3)**
- "ModRun Essentials" — Basic clips, single rail
- "ModRun Pro" — Premium clips, modular kits, starter bundles
- "ModRun Professional" — Designer clips, professional systems, deluxe kits

### Payments and Tax (Shop Manager → Finances)

1. Add bank account (routing + account number from business checking). Etsy verifies with 2 micro-deposits over 2-3 business days.
2. Submit W-9 / tax identification (EIN preferred; SSN acceptable for sole proprietor)
3. Confirm Etsy Managed Payments is enabled (default for new US shops; includes PayPal + credit card processing at 3% + $0.25 per transaction)

### Shipping Profiles (Shop Manager → Settings → Shipping)

**Profile 1 — "Standard Domestic USPS Ground Advantage"**
- Processing time: 2 business days
- Origin: your city/state
- Shipping method: USPS Ground Advantage
- Type: Calculated (Etsy calculates zone rates by customer ZIP)
- Representative weight for single clip order: 0.27 lbs (includes 4oz product + mailer)
- Note: Pirate Ship's 2026 rates include the 8% temporary USPS surcharge (through January 2027); budget accordingly.

**Profile 2 — "Express Domestic USPS Priority Mail" (optional)**
- Same setup, select Priority Mail
- Customers pay higher rate for 1-3 day delivery
- Available as upsell at checkout

### Return Policy (Shop Manager → Settings → Policies)

- Return window: 30 days
- Return shipping: Seller pays (prepaid return label)
- Restocking fee: None
- This reduces buyer hesitation on first purchase from an unknown brand. Expected return rate at launch: 2-5%.

### Policy Pages (Shop Manager → About)

**About page** (post this verbatim or adapt):
"ModRun is an original cable management system designed by engineers for creators, professionals, and desk enthusiasts. Every product is designed from scratch using parametric CAD, manufactured on-demand to order, and tested to tolerances. We back all products with a 30-day satisfaction guarantee."

**Terms of Service** (minimal, can use Etsy default template):
Key clauses: IP ownership (customer owns the physical item, not the design), liability limitation, dispute resolution via Etsy.

**Privacy Policy**: Etsy provides a template; customize with your contact email and data retention policy (3 years, IRS requirement).

### Shop Visual Assets

- Banner: 3360x840px. Use Canva (free) with product hero photo + "Original Design. Precision Manufacturing." tagline.
- Profile image: 500x500px. Product photo or simple geometric logo.
- Estimated time: 30 minutes in Canva.

---

## Phase 4: Product Listing Upload (Days 5-10)

**Timeline: After Phase 2 (business setup) and Phase 3 (shop config) are complete.**
**Estimated time: 4-6 hours for all 5 SKUs.**

All product copy derives from pricing-tiers.csv and market research. Upload listings in draft status, then review all before simultaneous publish.

### Listing Pricing Reference (pricing-tiers.csv)

| SKU | Single Price | 3-Pack Price | Target Margin (0-500/mo) |
|-----|-------------|-------------|--------------------------|
| Basic Clips (PLA) | $8.99 | $22.99 | 54.3% |
| Rail System (single) | $12.99 | $32.99 | 62.0% |
| Premium Clips (PETG) | $14.99 | $38.99 | 60.0% |
| Modular Rail Kit | $18.99 | $48.99 | 63.4% |
| Starter Bundle | $28.99 | $74.99 | 65.6% |
| Designer Clips (PETG Colors) | $22.99 | $59.99 | 63.1% |
| Deluxe Professional Kit | $69.99 | $179.99 | 71.5% |

**Launch inventory recommendation**: List all tiers but set conservative quantities. Economy tier (15 units), Standard tier (20 units), Premium tier (5 units). Total: ~40 units achievable in 2-3 print days.

### Key SEO Guidance

Use eRank (free tier) to verify tags before publishing. Target tags with 10,000+ monthly searches and fewer than 5,000 active listings. Proven high-volume tags for this category: "cable clips," "cable management," "desk organizer," "3d printed," "cable organizer," "desk accessories," "home office," "workspace," "office organization."

Avoid over-broad tags: "handmade," "gift," "accessory" (too generic to rank).

### Product Photos (Minimum Per Listing)

Etsy's algorithm rewards listings with 5+ photos. For each product:
1. Hero shot: Product on white/neutral background, angled view showing design detail
2. In-context: Mounted on desk with cables organized
3. Detail: Close-up of mechanical fit, material texture
4. Lifestyle: Full desk setup with ModRun installed (shoot once, reuse across listings)
5. Variants: All color options side-by-side (Black, White, Grey)

Photography setup: White foamcore background ($3 from dollar store), natural window light or $20 ring light. Target 2048x2048px minimum (Etsy auto-compresses above this).

### Variants to Configure

Per listing (Etsy supports 2 variant properties):
- **Property 1 — Material**: PLA (standard, $0 premium) vs. PETG (premium, +$2-3 per unit)
- **Property 2 — Color**: Black, White, Grey

At launch, stock Black as primary inventory. White and Grey print-to-order in first 60 days (list as available, queue when ordered).

### Listing Upload Checklist (repeat for each of 5 SKUs)

- [ ] Title: keyword-rich, <140 characters, no caps-spam
- [ ] Category: Home & Living → Home Organization → Desk Organizers
- [ ] Description: 1,500+ characters, features + use cases + 30-day guarantee + shipping note
- [ ] Price: matched to pricing-tiers.csv, margin verified ≥54%
- [ ] Quantity: conservative launch stock entered
- [ ] Photos: minimum 2 uploaded, recommend 5
- [ ] Tags: 13 tags per listing, eRank-verified
- [ ] Shipping profile: Standard Domestic applied
- [ ] Variants: Material + Color configured
- [ ] Return policy: 30-day guarantee linked
- [ ] Draft saved, not yet published

---

## Phase 5: Pre-Launch Production and Supplier Negotiation (Days 1-14, Parallel Track C)

**This runs in parallel with Phases 2-4. Start filament procurement and initial inventory printing on Day 1.**

### Initial Inventory Print Run

**Target: 40-50 units by launch day (Day 10-12)**

Print schedule (single Bambu P1S, 16-hour operating window):

| Day | Jobs | Estimated Output | Notes |
|-----|------|-----------------|-------|
| 1 | Modrun_clip batch x8 (black PLA) | 8 clips | Validate settings from test print |
| 2 | Modrun_rail x4 (black PLA) | 4 rails | Rail print time ~1.5-2h each |
| 3 | Modrun_clip batch x8 (white PLA) | 8 clips | Color change from black |
| 4 | Modrun_clip PETG x6 (black) | 6 premium clips | Profile switch to PETG |
| 5 | Mixed queue (rails + clips) | 10-14 units | Fill to 40-unit target |

**Quality checkpoint each day**: Run through fulfillment-workflow.md Section 2 QA checklist before adding to finished goods inventory.

### Supplier Negotiation (Week 1, parallel)

**Target: Lock in ≤$12/kg primary supplier, ≤$10.49/kg secondary**

Detailed negotiation playbook in `supplier-negotiation-playbook.md`. Summary of actions for Week 1:

Day 1-2:
- Verify eSUN Amazon pricing (ASIN B0G2KSS613 for black PLA Basic)
- Verify Anycubic 50kg pallet pricing at store.anycubic.com/products/pla-basic-50-100kg-deals
- Decide Path A (wholesale eSUN negotiation) vs. Path B (Amazon bundles + Anycubic pallet)

Day 2-3:
- Send eSUN wholesale inquiry (see supplier-negotiation-playbook.md Section 2, Phase 3 email template)
- Contact Anycubic to pre-qualify 50kg order (see playbook Section 2, Phase 4)

**COGS reduction targets by supplier path**:

| Scenario | $/kg | Per unit (75g) | vs. retail baseline | Monthly savings at 100 units |
|----------|------|----------------|--------------------|-----------------------------|
| Current (retail Amazon) | $15.00 | $1.13 | baseline | — |
| eSUN wholesale $12.50 | $12.50 | $0.94 | -17% | $19/mo |
| Anycubic pallet $10.49 | $10.49 | $0.79 | -30% | $34/mo |
| Combined with Pirate Ship | varies | +$0.80-1.50/order savings | adds ~8% | adds ~$40-80/mo |
| Combined with bulk packaging | $0.05/mailer vs $0.10 retail | adds ~1% | adds ~$5/mo |
| **Blended 20% COGS reduction** | — | — | **-20%** | **~$60-100/mo at 100 units** |

### Packaging Procurement (Week 1)

Order packaging materials in Week 1 so they arrive before first orders ship:

**Immediate (Days 1-3)**:
- Shop4Mailers poly mailers 9x12" 2.5mil: Order 500-unit pack ($25). These are the primary launch packaging. Ship single and 3-pack orders in this mailer.
- Packing tape, 2" clear: 6-pack ($12)
- Digital scale (0.1oz precision): $15-25 if not already owned

**Month 3 upgrade (plan now, order later)**:
- Custom-printed poly mailers: Vistaprint or Smart Shipping Supply. 500-unit MOQ, $0.38-0.50/unit with full-color logo printing. Lead time 10-14 days. Order at 200+ units/month sales velocity.
- Custom boxes for Deluxe Kit: Packlane or Arka. $0.76-1.10/unit at 500 units. Lead time 10-14 days.

**Thermal label printer** (optional but highly recommended): Rollo or DYMO 4XL, $100-200. Eliminates ink costs and dramatically speeds up label printing. Pays for itself in 3-4 months at 50+ orders/month.

---

## Phase 6: Launch Day and First-Month Operations (Days 10-30)

### Launch Day Sequence (Recommended: Thursday afternoon)

Avoid Monday (returns backlog) and Friday (minimal support if issues arise).

1. **Final review**: All 5 listings in draft status; review each for accuracy, typos, margin verification
2. **Simultaneous publish**: Click Publish on all 5 listings at once (10 AM - 2 PM Thursday is optimal per Etsy algorithm data)
3. **Confirm live**: Search Etsy for "ModRun" — all products should appear within 15-30 minutes
4. **Test purchase flow**: Add item to cart as a customer; verify shipping calculates correctly
5. **Enable Etsy Stats**: Dashboard → Stats — set to daily view; check first 4 hours for any technical issues
6. **Announce launch**: Post to any social channels, personal contacts, or email list you have. Even 10 shares from friends creates early engagement signals that the Etsy algorithm rewards.

### First Week Operations

**Daily routine (15-30 minutes/day)**:
- Morning: Check Etsy orders (email notification) + add to print queue
- 8 AM: Start print job for any overnight or morning orders
- Afternoon: QC prints, prepare packages
- 2-4 PM: Generate Pirate Ship labels, ship packages
- Evening: Mark orders as shipped in Etsy (triggers auto-email to customer with tracking)

**Integration: Etsy → Pirate Ship**:
Pirate Ship's Etsy integration auto-imports open orders. Log in to Pirate Ship, click "Import Orders," select Etsy store, all open orders populate with customer address pre-filled. Select carrier (USPS Ground Advantage), confirm package weight, purchase label in bulk. Fastest path from order to label is 2-3 minutes per order.

**Integration: Etsy → Craftybase (Month 2)**:
Once orders exceed 15-20/month, connect Craftybase ($49/month Studio). Connect under Settings → Integrations → Etsy. Craftybase then auto-deducts material inventory as orders sync, calculates actual COGS per order (using your material recipe — e.g., 75g PLA + 5min setup labor), and generates weekly/monthly profit reports. This becomes essential for tax preparation by end of Year 1.

### Supplier Negotiation — First Month Goals

**Week 2-3 actions** (supplier responses typically arrive):
- If eSUN responds with wholesale quote: Evaluate against $12.50/kg target. If at or below, accept and place first wholesale order for next month's supply.
- If Anycubic responds: Confirm 50kg black PLA availability and $10.49/kg pricing. Place order if Month 1 sales trajectory suggests >50 units/month by Month 2.
- If no response: Follow up on Day 10 (email) and Day 14 (phone if available).

**Month 1 supplier decision gate**:
- 0-20 units sold → Continue Amazon Prime (no commitment), contact suppliers again Month 2
- 20-50 units sold → Commit to eSUN wholesale OR Anycubic 50kg pallet (either hits 20% COGS target)
- 50+ units sold → Commit to both eSUN wholesale (primary) + Anycubic (backup), activate Polymaker inquiry for Month 4 quality tier

---

## Section 7: Production Workflow Optimization

### Print Queue Management

**Batch printing rules for cost efficiency**:

1. **Color consolidation**: Print all black PLA jobs before switching to white or grey. Each color change requires a 5-10 minute purge cycle that consumes ~5g of filament. On 20 color changes/month, that is 100g wasted ($1.50 retail, $0.79 wholesale). Consolidate by color in daily queue.

2. **Material consolidation**: Print all PLA jobs before PETG jobs in a session. PLA → PETG transition requires nozzle temp ramp from 210°C to 235°C + 5-minute stabilization. PETG → PLA requires purge to clear PETG residue. Minimize transitions by batching same-material jobs together.

3. **Plate batching**: ModRun clips are small. A Bambu P1S build plate (256x256mm) can hold 6-8 clips simultaneously without quality loss. At 6 clips/plate vs. 1 clip/plate, you reduce overall print time by approximately 60% (the fixed setup overhead is amortized). Use Bambu Studio's "Auto Arrange" to optimize plate packing.

4. **Pre-print inventory**: On days with no orders, use idle printer capacity to build 1-week buffer stock. This decouples order fulfillment from same-day print requirements — an order received at 4 PM can ship from buffer stock rather than waiting for an overnight print.

**Queue software**: Google Sheets is adequate through Month 3. Columns: Order ID, Customer, SKU, Color, Quantity, Plate Batch, Start Time, End Time, Status (Queued/Printing/QC/Packaged/Shipped), Notes.

### Print Settings (Production-Validated)

These settings are production targets — validate against your test print results and adjust if needed:

**PLA (eSUN PLA+ or equivalent)**:
- Nozzle: 210-215°C
- Bed: 60°C (PEI plate, no brim needed)
- Layer height: 0.2mm
- Infill: 15% (gyroid pattern — better strength distribution for clips)
- Speed: 200mm/s outer perimeter, 300mm/s infill (Bambu P1S performance profile)
- Supports: None (geometry designed to be support-free)
- Estimated time: modrun_clip single: 22-30 minutes; modrun_rail single: 70-90 minutes

**PETG (Overture or eSUN PETG)**:
- Nozzle: 230-235°C
- Bed: 80°C
- Layer height: 0.2mm
- Infill: 20% (PETG benefits from slightly higher infill for stiffness)
- Speed: 150mm/s outer perimeter (PETG is more sensitive to speed artifacts)
- Supports: None
- Estimated time: modrun_clip single: 30-40 minutes; modrun_rail single: 100-120 minutes

### QA Process (Production Standard)

The ±0.5mm tolerance check is critical for customer satisfaction. A clip that requires force to engage, or falls off the rail under light handling, will generate returns and negative reviews.

**Per-batch QA (every 5th print)**:
- Measure clip engagement width with digital calipers (target: CAD spec ±0.5mm)
- Measure rail channel width (target: CAD spec ±0.5mm)
- Physical fit test: clip onto reference rail, cycle 5 times
- If dimensional deviation >0.5mm on 2 consecutive measurements: pause batch, check bed leveling, verify filament diameter consistency

**Per-unit visual QA (every print)**:
- No layer delamination
- No warping visible from above
- Color consistent (no streaks from filament transition)
- No stringing on PETG (trim with craft knife if present)
- Weight within ±5g of reference (indicates complete fill)

**Defect rates and actions**:

| Reject Rate | Action |
|-------------|--------|
| <3% | Normal — continue operations |
| 3-5% | Investigate: nozzle, filament batch, bed leveling |
| >5% | Stop batch, diagnose, adjust, reprint |

---

## Section 8: Fulfillment Logistics

Detailed fulfillment workflow in `fulfillment-workflow.md`. Key logistics summary:

### Shipping Partner Comparison

| Service | Rate (under 1 lb, Zone 4) | Delivery | Best For |
|---------|--------------------------|----------|---------|
| USPS Ground Advantage (Pirate Ship) | $3.85-4.60 | 2-5 days | Primary: all orders under 1 lb |
| USPS Priority Mail (Pirate Ship) | $7.50-9.50 | 1-3 days | Premium tier + time-sensitive |
| USPS Priority Mail Cubic | $6.50-8.00 | 1-3 days | Unlocked via Pirate Ship; best for dense small packages |
| FedEx/UPS | $8-15 | 2-3 days | Avoid until 50+ lbs/day volume justifies account |

**Note**: USPS has an 8% temporary surcharge on all services from April 26, 2026 through January 17, 2027. This is already reflected in Pirate Ship's rate calculator. Factor this into COGS models through January 2027.

### Packaging Cost Model by SKU

| SKU | Package Type | Pkg Cost | Shipping (Zone 4 avg) | Total Fulfillment Cost |
|-----|-------------|----------|----------------------|----------------------|
| Basic Clip (single) | 6x9" poly mailer | $0.05 | $4.10 | $4.15 |
| Rail System (single) | 9x12" poly mailer | $0.05 | $4.60 | $4.65 |
| Premium Clips (3-pack) | 9x12" poly mailer | $0.05 | $4.85 | $4.90 |
| Starter Bundle | Small box 8x6x4" | $0.30 | $5.50 | $5.80 |
| Deluxe Kit | Medium box 10x8x6" | $0.75 | $7.20 | $7.95 |

### Pirate Ship Setup and Etsy Integration

1. Create account at pirateship.com (free, no monthly fee)
2. Add credit card for label purchases
3. Connect Etsy store: Settings → Store Integrations → Etsy → Authorize
4. To ship: Click "Ship" → "Import Orders" → Select all open orders → Add weight → Purchase labels
5. Print labels (thermal printer recommended; standard 8.5x11 with label sticker also works)
6. Drop at USPS counter or use Pirate Ship's USPS pickup scheduling

**Commercial rate savings vs. retail USPS** (at current 2026 rates):
- Ground Advantage 4oz: Pirate Ship $3.85 vs. USPS retail $5.75 = $1.90 savings per shipment
- At 50 shipments/month: $95/month saved
- This saving alone partially offsets supplier negotiation benefits

---

## Section 9: Inventory Management

### Stock Forecasting (Month 1-3)

**Conservative demand curve (per market research and Etsy launch benchmarks)**:

| Month | Expected Orders | Average Units/Order | Units/Month | Filament Needed |
|-------|----------------|---------------------|-------------|-----------------|
| Month 1 | 5-10 | 1.5 | 8-15 | ~0.8-1.5 kg |
| Month 2 | 15-25 | 2.0 | 30-50 | ~3-5 kg |
| Month 3 | 40-70 | 2.5 | 100-175 | ~10-17 kg |
| Month 4 | 80-120 | 3.0 | 240-360 | ~24-36 kg |

**Filament procurement aligned to this curve**:
- Month 1: Use existing stock + 5-10 kg Amazon Prime (no commitment)
- Month 2: Lock in eSUN wholesale OR Anycubic pallet (15-50 kg order)
- Month 3: Activate wholesale contract (50+ kg/month)

### Reorder Points and Safety Stock

**Rule**: Maintain 14-day forward supply as safety stock. Reorder when stock drops below this level.

| SKU | Daily Rate (M2 est.) | 14-day Safety Stock | Reorder Trigger |
|-----|---------------------|---------------------|-----------------|
| Basic Clip | 1.5 units/day | 21 units | <21 finished |
| Rail System | 0.8 units/day | 11 units | <11 finished |
| Premium Clips | 0.7 units/day | 10 units | <10 finished |
| Starter Bundle | 0.5 units/day | 7 units | <7 finished |

**Daily inventory check (2 minutes every morning)**: Walk to storage shelf, count finished units per SKU, add any SKU below trigger to that day's print queue.

### Finished Goods Storage

**Location requirements**: Low humidity (40-50% RH), 20-26°C, no direct sunlight.

**Organization (simple shelving system)**:
```
Shelf 1: Basic Clips — labeled bins by color (Black / White / Grey)
Shelf 2: Rail Systems — labeled bins by color
Shelf 3: Premium Clips — labeled bins by color
Shelf 4: Kits and Bundles — labeled by SKU
Shelf 5: SCRAP/REWORK — items that failed QC but may be salvageable
```

**Bin labeling**: 3x5" index cards with: Product name, Color, Quantity, Last-printed date.

**Storage tip**: PLA is hygroscopic. Finished PLA products are stable (already printed), but unprocessed filament spools stored open will absorb moisture and cause print quality issues. Store open spools in sealed bags with desiccant packets, or in an active dry box.

---

## Section 10: Launch Timeline and Milestone Checklist

### Condensed Timeline

| Day | Phase | Key Actions |
|-----|-------|-------------|
| 0 | Test Print | Run go/no-go criteria. If pass, proceed. |
| 0-1 | Phase 2 Start | File LLC, apply for EIN, start insurance, open business bank. |
| 0-1 | Phase 3 Start | Create Etsy shop, configure settings, shipping profiles, policies. |
| 0-1 | Phase 5 Start | Verify supplier pricing, send eSUN wholesale inquiry, order packaging materials. |
| 1-3 | Production | Begin initial inventory print run (target 40 units over 5 days). |
| 3-5 | Phase 4 | Write product descriptions, take product photos, configure listings in draft. |
| 5-7 | Review | Final review of all listings, verify shipping calculations, confirm bank account verified. |
| 7-10 | Phase 6 | All listings published. Launch. Monitor first 24-48 hours. |
| 10-14 | Operations | Daily print + ship cycle. Supplier responses expected. |
| 30 | Month 1 Gate | Assess sales velocity. Make supplier commitment decision. Plan Month 2 scaling. |
| 60 | Month 2 Gate | Assess growth trajectory. Decide on second printer. Activate wholesale contract. |

### Phase-by-Phase Milestone Summary

**Phase 1 (Day 0)**: Test print passes go/no-go — launch authorized.
**Phase 2 (Days 1-7)**: Business entity registered, EIN obtained, insurance active, bank account open.
**Phase 3 (Days 1-7)**: Etsy shop created with all settings, shipping profiles, and policy pages complete.
**Phase 4 (Days 3-10)**: All 5 product listings in draft status with photos, descriptions, tags, and pricing.
**Phase 5 (Days 1-14)**: Initial 40-unit inventory printed and QC'd; supplier outreach sent; packaging arrived.
**Phase 6 (Day 10)**: Etsy shop goes live. First sales expected within 1-7 days (Etsy algorithm indexes new listings within 24-48 hours, but search rank builds over time).

### Month 1 Success Criteria (Decision Gate for Phase 2 Scaling)

If these criteria are met, proceed to supplier contract and printer 2 evaluation:
- [ ] 5+ orders received (validates product-market fit)
- [ ] Zero shipping complaints (validates fulfillment workflow)
- [ ] Print success rate ≥97% (validates production reliability)
- [ ] First customer review received (validates product quality)
- [ ] Average order value ≥$15 (validates pricing acceptance)
- [ ] Gross margin tracking at ≥54% after all fees (validates business model)

If criteria are NOT met (fewer than 3 orders in first 30 days):
- Review product photos (most common Etsy conversion issue)
- Review tags/SEO (use eRank to identify underperforming tags)
- Consider 10-15% promotional discount for 30 days to drive first reviews
- Do not scale supplier commitments until demand is confirmed

---

## Appendix: Key External Resources

- **Etsy Seller Handbook**: etsy.com/seller-handbook
- **Etsy Creativity Standards (3D printing compliance)**: etsy.com/legal/creativity
- **Pirate Ship USPS rates**: pirateship.com/usps/ground-advantage
- **Craftybase**: craftybase.com (Etsy-native inventory/COGS tracking)
- **eRank** (free Etsy SEO keyword tool): erank.com
- **IRS EIN application**: irs.gov/ein
- **eSUN wholesale**: esun3dstore.com
- **Anycubic pallet pricing**: store.anycubic.com/products/pla-basic-50-100kg-deals
- **Canva** (free design for shop banners): canva.com
- **Shop4Mailers** (poly mailers): shop4mailers.com

---

**Document Status**: Ready for execution upon test print confirmation
**Version**: 2.0 (expanded from Session 590 scope requirements)
**Confidence Level**: High (all source data from Sessions 290-590)
**Estimated effort**: 2 weeks pre-launch through live shop; Month 2 supplier commitments; Month 3 scaling
