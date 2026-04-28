---
title: ModRun Fulfillment Workflow — Print-to-Ship Operations
date: 2026-04-28
status: ready-for-execution
confidence: high
related: multi-printer-architecture.md, pricing-strategy.md
---

# ModRun Fulfillment Workflow: Print-to-Ship Operations

**Status**: Ready to activate upon Etsy launch (Week 2)  
**Timeline**: Daily operations starting Week 2, Month 1  
**Scope**: Order receipt → Print → Finish → Packaging → Ship within 2 business days  
**Throughput**: 15-20 units/day per printer (P1S) at realistic capacity  

---

## Executive Summary

This document defines the end-to-end fulfillment process from Etsy order receipt to shipped package. The workflow is designed for a single Bambu P1S printer operating 16-18 hours/day, producing 50-100 units/month during Phase 1, with clear scaling path to multi-printer farm (Section 5).

**Key design principles**:
- **Predictable cycle time**: Order → Print (next morning) → Finish (same day or next) → Ship (within 2 business days)
- **Quality gates**: Visual inspection + dimension check post-print to catch defects before packaging
- **Inventory efficiency**: "Just-in-time" printing reduces storage footprint; safe reorder triggers prevent stock-outs
- **Cost tracking**: Per-unit COGS accounting (material + labor + overhead) informs pricing adjustments

**Critical assumption**: Test print confirms ModRun clips print reliably without post-processing on Bambu P1S at 210°C, 60°C bed, 0.2mm layer height, 15% infill.

---

## Section 1: Daily Print Queue Management

### 1.1 Print Queue Process

**Morning routine** (7:00 AM):
1. Check Etsy orders received in past 24 hours (automatic email notification from Etsy)
2. Create daily print queue list (simple Google Sheet or paper log)
3. Assign to printer based on file and estimated print time
4. Load filament (if color change needed from previous day)
5. Slice file in Bambu Studio (optimize for speed if multi-unit batch)
6. Start first job by 8:00 AM

**Queue management structure**:

```
DAILY PRINT QUEUE (Example: Monday, May 1st)

ORDER #1 | Customer: Smith | SKU: Basic Clip x3 (black PLA) | Print time: 1.5h
ORDER #2 | Customer: Jones | SKU: Rail System (black PLA) | Print time: 2.5h
ORDER #3 | Customer: Lee | SKU: Premium Clip x3 (PETG, white) | Print time: 2.5h
[COLOR CHANGE — load white PETG filament]
ORDER #4 | Customer: Wang | SKU: Starter Bundle (white PETG) | Print time: 3.5h

TOTAL DAILY QUEUE: ~9.5 hours (fits in 16-hour operating window)
PRIORITY: Same-day shipment for orders received before 10 AM
```

### 1.2 Print Time Estimation

Use these baseline estimates (Bambu P1S, 210°C, 0.2mm layer height):

| Component | Material | Print Time | Notes |
|-----------|----------|-----------|-------|
| modrun_clip (single) | PLA | 25-35 min | Lightweight, minimal supports |
| modrun_clip (single) | PETG | 35-45 min | Slower extrusion speed |
| modrun_rail (single) | PLA | 1.5-2h | Larger component |
| 3-pack clips | PLA | 1-1.5h | Can batch 3 on single plate |
| Starter Bundle | Mixed | 3-4h | Rail + 4 clips sequential prints |

**Optimization strategies**:
- **Batch prints**: Load 3-4 clips per build plate (reduces per-unit time via parallelization)
- **Material economy**: Print all PLA jobs before PETG (avoids repeated color changes)
- **Plate stacking**: Use Bambu multi-plate feature if available (P1S only; X1C supports up to 4 plates)

### 1.3 Realistic Daily Throughput

**Single Bambu P1S, 16-hour operating window, 210°C PLA**:

| Scenario | Daily Unit Output | Example |
|----------|-------------------|---------|
| Conservative (print on-demand) | 8-12 units | 4 dual-clip jobs + 1 rail |
| Optimized (batched) | 15-20 units | 6 3-clip batches + 2 rails |
| Maximum (continuous) | 25-30 units | Multi-plate batching, no breaks |

**Recommendation for Phase 1**: Plan for 12-15 units/day (achievable with moderate batch optimization, accounts for failed prints, color changes, maintenance).

**Monthly capacity** (conservative):
- 12 units/day × 22 working days = ~264 units/month per printer
- Expected Month 1 demand: 5-10 units (test phase) → well within capacity
- Expected Month 2+ demand: 30-80 units/month → still single-printer capable

### 1.4 Print Queue Tracking

**Simple logging approach** (Google Sheets recommended):

Create a spreadsheet with columns:
- Order ID (from Etsy)
- Customer name
- SKU/Product
- Material/Color
- Quantity
- Estimated print time
- Actual print time (fill after print completes)
- Start time
- Finish time
- Print status (Printing / Complete / Failed / In progress)
- Notes (quality issues, color mismatch, etc.)

**Review daily**:
- Morning: Create today's queue
- Evening: Log all completions and note any issues
- Weekly: Summarize print success rate, average print time, reorder triggers

**File location**: Google Drive or Dropbox (access from mobile for remote monitoring)

---

## Section 2: Post-Print Processing

**Timeline**: 1-2 hours per batch of 10 units (parallel with next print job)

### 2.1 Support Removal & Cleanup

**For modrun_clip components** (designed for zero support):

1. **Remove from build plate** (immediately after print finishes)
   - Wait 3-5 minutes for nozzle to cool
   - Use plastic spatula or metal shim to pry part off plate
   - Do not force — wiggle gently if stuck
   - Risk: Denting part or damaging PEI plate (use proper removal tool, $5-15)

2. **Inspect for defects**
   - Visual inspection under good lighting (LED ring light recommended)
   - Look for: Layer adhesion issues, warping, color streaks, nozzle crashes
   - Check critical dimensions with calipers (optional, do 1 per batch of 5)
   - If defect found: Set aside as "scrap/rework" (reprint later), mark in queue log

3. **Cleanup** (if needed)
   - PLA prints clean generally; minimal post-processing needed
   - PETG may have slight stringing: Quick trim with craft knife
   - Sand rough edges only if visible to customer (light 150-grit, 5 minutes)
   - Wipe with dry cloth (remove dust)

**Time estimate**: 2-3 minutes per unit

### 2.2 Sanding & Finishing (Optional)

**Decision tree**:
- IF test print shows excellent surface finish (smooth, no layer lines visible) → Skip sanding
- IF test print shows obvious layer lines → Consider light sanding for premium SKUs only

**Finishing approach** (if needed):
- Material: 150-grit sandpaper or sanding pad
- Duration: 30-60 seconds per unit (light abrading, not aggressive)
- Target: Smooth layer line texture, no color change (don't over-sand)
- Cleanup: Wipe dust with dry cloth

**Cost**: Negligible (single pad lasts 500+ units)

**Recommendation for Phase 1**: Do NOT sand unless test print clearly shows rough finish. Extra labor cost ($0.10-0.20/unit) not justified by customer feedback at launch.

### 2.3 Quality Checkpoint

Before packaging, run quick QC:

**Checklist per unit**:
- [ ] Part is fully printed (not interrupted mid-job)
- [ ] No visible defects (cracks, layer separation, warping)
- [ ] Correct color/material for order
- [ ] Dimensions look correct (compare to reference sample if available)
- [ ] Surface finish acceptable (not requiring sanding)
- [ ] Weight reasonable (single clip should feel light, not dense)

**Failure rate acceptable**: 2-5% (occasional print failures). If >5%, investigate printer settings (nozzle clog, bad filament batch, bed leveling issue).

---

## Section 3: Inventory Management

### 3.1 Finished Goods Storage

**Storage location**: Low-humidity area (40-50% RH), 20-26°C, away from direct sunlight

**Organization**:
```
FINISHED GOODS STORAGE (Example shelving)

Shelf 1 (top):
├── Basic Clips (black PLA) — 8 units
├── Basic Clips (white PLA) — 4 units
└── Basic Clips (grey PLA) — 2 units

Shelf 2:
├── Rail System (black PLA) — 6 units
└── Rail System (white PLA) — 3 units

Shelf 3:
├── Premium Clips (black PETG) — 5 units
└── Premium Clips (white PETG) — 3 units

[Box labeled "DAMAGED/SCRAP" — rework items]
```

**Labeling**: Use simple index cards with product name, color, quantity, print date

**Reason for organization**: Quick visual scan tells you what's in stock and what needs reprinting

### 3.2 Reorder Triggers

**Rule**: Reorder when finished goods stock drops below 7-day supply

**Example calculation** (assuming 12 units/day throughput):
- 7-day supply = 84 units
- If you have <84 units finished, queue a reprint batch

**Specific triggers**:

| SKU | Daily consumption (estimate) | Reorder trigger |
|-----|-----|---|
| Basic Clip | 3 units/day | <21 units finished |
| Rail System | 2 units/day | <14 units finished |
| Premium Clip | 1 unit/day | <7 units finished |

**Process**:
1. Every morning, do 2-minute inventory count (walk to shelf, count units)
2. If any SKU below trigger, add to that day's print queue
3. Log reorder trigger in spreadsheet ("Reorder: Basic Clip, qty 25")

**Note**: Month 1 initial inventory (40 units) will last 3-4 days. Plan daily reprinting after first week.

### 3.3 Per-Product COGS Tracking

Track actual cost per unit printed (for pricing validation and margin tracking).

**Example COGS breakdown** (modrun_clip, Basic, 75g PLA):

| Cost Component | Value | Notes |
|---|---|---|
| Filament (75g @ $12/kg) | $0.90 | Wholesale eSUN pricing |
| Electricity (35 min @ $0.03/hr) | $0.02 | P1S power draw ~200W avg |
| Printer depreciation (35 min / 5000-hr life) | $0.05 | P1S cost $700, 5000-hr lifespan |
| **Material COGS** | **$0.97** | Sum of above |
| Packaging (poly mailer) | $0.05 | $0.05/unit at 1000-pack |
| Shipping label (USPS) | $3.50-5.00 | Zone-dependent, fold into per-order cost |
| **Fulfillment COGS** | **$3.55-5.05** | Per order (not per unit) |
| **Total COGS per unit** | **$1.02-1.07** | Assuming 1 unit per order (worst case) |

**Multi-unit order example** (3-pack):
- Material COGS: $2.91 (3 × $0.97)
- Packaging: $0.10 (larger mailer)
- Shipping: $4.20 (zone avg.)
- **Total per 3-pack**: $7.21
- **Per-unit COGS**: $2.40
- **Retail price**: $22.99
- **Gross margin**: 79.6% (excellent)

**Action**: Track these numbers monthly. If COGS creeps up >10%, investigate (supplier price increase, higher rejection rate, etc.)

---

## Section 4: Shipping & Fulfillment Workflow

### 4.1 Order-to-Print Workflow

**Timeline: Order received (Etsy) → Shipped (USPS) = 2 business days**

**Detailed timeline**:

```
DAY 1 (Order placed):
07:00 — Customer purchases on Etsy (e.g., "Basic Clips x3")
07:15 — Etsy sends order notification email to your address
08:00 — You receive order, add to daily print queue
08:15 — Start print job (modrun_clip 3-pack batch)
10:00 — Print completes
10:15 — QC check, move to finished goods shelf
14:00 — Prepare shipment (see Section 4.2)

DAY 2 (Next business day):
08:00 — Create USPS label via Pirate Ship
08:15 — Apply label to package, drop at USPS (or use pickup service)
09:00 — Package in USPS system, tracking available
12:00 — Customer receives Etsy message "Your order shipped!" with tracking

CUSTOMER RECEIPT:
DAY 3-5 (depending on zone) — Package arrives at customer
```

**Key points**:
- Processing time stated to customer: 2 business days (actual is often faster, but this is safe promise)
- Beating stated processing time improves reviews (aim for next-day ship when possible)
- Track all orders in Etsy → Print Queue → Finished Goods → Ship

### 4.2 Packaging Workflow

**Materials needed**:
- Poly mailers 6×9" (Shop4Mailers, $0.05/unit)
- Packing tape (clear, 2")
- USPS shipping labels (printed from Pirate Ship)
- Optional: Tissue paper for premium tier (adds perceived value)
- Optional: Thank-you card (laser printed, <1 minute per order)

**Packing sequence** (1-unit order):

1. **Prepare mailer**
   - Take poly mailer (6×9")
   - Fold ModRun clip(s) in tissue paper (optional)
   - Place in mailer
   - Seal top with clear packing tape

2. **Weigh package**
   - Use digital scale (measure in ounces)
   - Log weight (feed into Pirate Ship for shipping calculation)
   - Example: Basic Clip 3-pack = 3.5 oz

3. **Generate shipping label**
   - Open Pirate Ship (pirateship.com)
   - Click "Create Shipment"
   - Enter customer address (auto-populate from Etsy order)
   - Select USPS service: **Ground Advantage** (usually cheapest for <4oz)
   - Confirm weight and zone
   - Generate label (PDF)
   - Print label (thermal printer recommended, or on standard paper with label sticker)

4. **Apply label & ship**
   - Tape label to top-right of package (address-side up)
   - Drop at USPS (no postage needed, already prepaid on label)
   - OR use USPS pickup service if available (Pirate Ship arranges, no extra cost)

**Cost per unit shipped** (Ground Advantage, zone-dependent):
- Local (Zone 1-2): $3.50-3.85
- Medium (Zone 3-4): $4.20-4.60
- Far (Zone 5-8): $4.95-5.50

**Time per order**: 5-8 minutes (from finished goods to USPS)

### 4.3 Etsy Order Management

**Daily checklist**:

- [ ] **Morning**: Review new orders received (automated email from Etsy)
- [ ] **Check Etsy messages**: Respond to customer questions within 4 hours (or next morning)
- [ ] **Log order details**: Order ID, customer name, SKU, address, in spreadsheet
- [ ] **Add to print queue**: Assign to printer, note color/material
- [ ] **Track print completion**: Log actual print time in queue sheet
- [ ] **Generate shipping label**: As soon as print is complete (before EOD)
- [ ] **Mark as shipped**: Log tracking number in Etsy (triggers auto-email to customer with tracking)
- [ ] **Archive order**: Move to completed section of spreadsheet after shipped

**System integration** (optional, for Month 2+):
- Use Etsy's "Shipping Labels" feature directly (integrated with USPS)
- Or continue using Pirate Ship (preferred for cheaper rates + batch processing)

---

## Section 5: Scaling Timeline (1 Printer → N Printers)

### Month 1-2: Single Printer, Manual Queue

**Capacity**: 50-100 units/month (ample for 5-10 expected sales)

**Operations**:
- 1× Bambu P1S, 16 hr/day
- Daily print queue (hand-managed, Google Sheet)
- Per-order processing (print, finish, ship same cycle)
- Finished goods shelf (basic organization)

**What NOT to do yet**:
- Don't buy second printer (demand not proven)
- Don't invest in queue management software (manual tracking is fine)
- Don't pre-print inventory (on-demand is lean)

### Month 3-4: Add Second Printer, Basic Queue Optimization

**Trigger**: If Month 2 sales >30 units (indicating 60+ units/month run rate)

**New setup**:
- 2× Bambu P1S printers
- Parallel printing (2 different SKUs simultaneously)
- Shared print queue (Google Sheet updated in real-time)
- Coordinated finishing station (2 operators or 1 operating serially)

**Capacity**: 100-250 units/month (meets projected Month 3-4 demand)

**Operations change**:
- Printer #1: Basic clips (high volume, all colors)
- Printer #2: Rails + premium clips (specialty items)
- Both print simultaneously → daily output up to 20-25 units

**Hardware needed**:
- Printer 2 + AMS: ~$1,400
- Workspace expansion (additional bench): ~$200
- Optional: Webcam per printer (remote monitoring): ~$50 × 2

**Labor**: 1-2 hours/day (vs. 0.5-1 hour with single printer)

### Month 5+: Multi-Printer Farm (3-5 Printers)

**Trigger**: If Month 4 sales >100 units (indicating 300+ units/month capability)

**Architecture** (detailed in multi-printer-architecture.md):
- 5× Bambu P1S/X1C printers in row configuration
- Zone-separated workspace (print zone, finish zone, pack zone)
- Queue management system (either advanced Google Sheets or lightweight app)
- Staffing: 2-3 operators full-time

**Capacity**: 500-1,000 units/month (support adjacent products, multi-channel sales)

**Monthly revenue projection** (at Month 5 scale):
- 500 units × $18.99 avg price = $9,495 gross revenue
- Less Etsy fees (3%) = $9,213 net revenue
- Less COGS (material, packaging, shipping): $4,000-5,000
- **Net profit**: $4,000-5,000/month per single-printer focused operation

---

## Section 6: Customer Service & Quality Assurance

### 6.1 Quality Standards

**Defect classification**:

| Severity | Issue | Action |
|----------|-------|--------|
| Critical | Part doesn't fit clips to rail; cracks visible | Reject, reprint, free reship |
| Major | Layer separation, warping, visible nozzle crash | Reject, reprint, free reship |
| Minor | Slight color variation, minor layer lines | Ship as-is (acceptable for 3D printed) |
| Cosmetic | Single microscopic imperfection | Ship as-is |

**Failure rate target**: <3% rejection rate (aim for 97% first-pass success)

**If failure rate >5%**:
- Check printer: Nozzle clog? Bed leveling off?
- Check filament: New batch? Moisture absorbed?
- Check print settings: Did you change temp or speed?
- Review print job: Slice settings still optimal?

### 6.2 Customer Communication

**Order confirmation email** (automatic from Etsy, but review):
- Confirms order details, color, material
- States processing time: "Your order will ship within 2 business days"
- Provides your shop email for questions

**Shipment notification** (Etsy auto-sends):
- "Your order has shipped!"
- Includes USPS tracking number
- Tracking automatically updates (customer can see delivery date estimates)

**Thank-you follow-up** (optional, adds value):
- Send 3-5 days after estimated delivery: "Hope you're happy with your ModRun clips! Feedback welcome."
- Encourages reviews on Etsy (improves search visibility)
- Opens door for repeat business

**Handling returns/complaints**:
- Response SLA: 24 hours (even if just acknowledging, will get back within 24hr)
- Defective product: Ship replacement immediately, no questions (30-day guarantee)
- Customer unhappy: Full refund, no questions (30-day guarantee)
- Track reason: Log in spreadsheet to identify patterns

### 6.3 Review Generation

**Goal**: Build to 20+ reviews by end of Month 2 (proof of social trust)

**Strategies**:
- Exceed shipping promise (ship same-day when possible)
- Include a brief thank-you note in package
- Request review subtly in follow-up email: "If you're happy with ModRun, reviews help us grow!"
- Respond to every review (even negative ones) professionally and thoughtfully

**Expected review rate**: 20-30% of customers leave reviews (if product is good + you ask)

---

## Section 7: Monthly Operations Dashboard

**Create a simple spreadsheet to track monthly KPIs**:

| KPI | Month 1 | Month 2 | Month 3 | Target |
|-----|---------|---------|---------|--------|
| Units shipped | — | — | — | 10-20 (M1), 30-50 (M2), 100+ (M3) |
| Orders completed | — | — | — | 5-10 (M1), 15-25 (M2), 50+ (M3) |
| Print success rate | — | — | — | ≥97% |
| Fulfillment time | — | — | — | <2 days avg |
| Customer reviews | — | — | — | 5+ (M1), 15+ (M2), 50+ (M3) |
| Return rate | — | — | — | <5% |
| Repeat customer % | — | — | — | >10% (M2+) |
| **Revenue** | — | — | — | $0 (M1), $400-800 (M2), $2K+ (M3) |
| **COGS cost** | — | — | — | $50-100 (M1), $200-400 (M2), $1K+ (M3) |
| **Net margin %** | — | — | — | 55-70% |

**Review and adjust monthly**: Any metric falling below target indicates a process improvement needed.

---

## Section 8: Troubleshooting & Common Issues

### Issue: Print Fails Mid-Job

**Symptoms**: Printer stops mid-print, filament tangles, nozzle clog

**Diagnosis**:
- Check Bambu App for error message
- Inspect nozzle for material buildup
- Verify filament path in AMS (for multi-color jobs)

**Solutions**:
1. Clear nozzle (heat to 210°C, extrude, clean with metal wire)
2. Reload filament and restart job
3. Use fresh filament if batch suspected

**Prevention**: Maintain printer weekly (nozzle check, bed leveling)

### Issue: Parts Look Rough/Warped

**Symptoms**: Layer lines visible, edges uneven, slight warping

**Causes**:
- Bed temperature too low (increase by 5°C)
- Print speed too high (reduce to 180mm/s)
- Nozzle too far from bed (re-level)
- Filament moisture (dry filament in oven at 60°C for 2 hours)

**Solution**: Run test print with adjusted settings. If improved, use new settings going forward.

### Issue: Delays in Shipping

**Symptoms**: USPS label generated but package not actually dropped for 2+ days

**Prevention**:
- Set daily "ship time" (e.g., 2 PM) to create labels and drop at USPS
- Use USPS pickup service if available (arranges automatic daily pickup)
- Never let packages sit >24 hours after labeling

### Issue: Customer Receives Damaged Item

**Response**:
- Apologize, offer immediate replacement shipment
- Ask customer to photos for your quality log
- Root cause analysis: Packaging issue (fragile item, poor cushioning) or shipping damage?
- If packaging issue: Upgrade to thicker mailers or add padding

---

## Appendix: Tools & Resources

**Software**:
- Google Sheets (queue tracking, inventory, KPI dashboard)
- Etsy App (mobile order notifications)
- Pirate Ship (shipping labels, bulk batch processing)
- Bambu Studio (slicing software, optimal print settings)
- Digital scale (shipping weight measurement)

**Hardware**:
- Thermal printer (label printing, optional but recommended)
- LED ring light (QC inspection)
- Digital calipers (dimension verification)
- Craft tools (spatula, knife, sandpaper)

**Suppliers** (for packaging, shipping):
- Shop4Mailers (poly mailers, $0.05/unit)
- Pirate Ship (USPS shipping, commercial rates)
- Amazon (packing tape, labels, scale)

**Reference documents**:
- multi-printer-architecture.md (scaling guidance)
- supplier-negotiation-playbook.md (filament sourcing)
- pricing-strategy.md (COGS validation)

---

**Document Status**: Ready for activation Week 2 (upon Etsy launch)  
**Confidence Level**: High (derived from multi-printer-architecture.md + operational best practices)  
**Next update**: End of Month 1 (validate actual throughput vs. projections, adjust timelines)
