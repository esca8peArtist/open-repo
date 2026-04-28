---
title: ModRun Fulfillment Workflow — Print-to-Ship Operations
date: 2026-04-28
version: 2.0
status: ready-for-execution
confidence: high
related: multi-printer-architecture.md, pricing-strategy.md, supplier-negotiation-playbook.md
---

# ModRun Fulfillment Workflow: Print-to-Ship Operations

**Status**: Activate upon Etsy launch (Week 2)
**Timeline**: Daily operations from first order through scaling phase
**Scope**: Order receipt → Print queue → QA → Packaging → Ship within 2 business days
**Throughput**: 12-20 units/day per printer (single P1S); 50-100 units/day at 5-printer farm

---

## Executive Summary

This document defines the complete end-to-end fulfillment process for ModRun cable management products, from Etsy order receipt through USPS delivery. The workflow is designed around a single Bambu P1S printer at launch, with explicit scaling inflection points for 2-printer and 5-printer configurations.

**Three design principles drive every decision**:

1. **2-business-day promise is inviolable.** Beating it earns reviews. Missing it kills them. Every workflow decision is made with this constraint as the binding limit.

2. **Quality gates before packaging.** A single defective unit shipped costs more in returns, replacement shipping, and review damage than 10 rejected prints. Catch defects at the printer, not in the customer's hands.

3. **Automation compounds.** The Craftybase → Etsy → Pirate Ship integration chain means a single order creates zero manual data entry steps by Month 2. Invest 2 hours setting this up before the first 10 orders arrive.

---

## Section 1: Order-to-Shipping Workflow

### Master Workflow (Single Printer, Phase 1)

```
ORDER PLACED (Etsy)
    ↓
EMAIL NOTIFICATION → Your inbox (automatic from Etsy)
    ↓
MORNING REVIEW (7-8 AM daily) → Add to print queue
    ↓
CRAFTYBASE SYNC (automatic every 4 hours on Studio plan)
    ↓
PRINT JOB ASSIGNED → Bambu P1S queue
    ↓
PRINT COMPLETES → QA checkpoint (Section 3)
    ↓
PASS QA → Move to finished goods shelf
FAIL QA → Scrap; reprint; do not ship defect
    ↓
PACKAGE PREPARATION (Section 4)
    ↓
PIRATE SHIP LABEL GENERATION (Section 5)
    ↓
SHIP (USPS dropoff or pickup)
    ↓
MARK AS SHIPPED IN ETSY → Customer auto-notified with tracking
    ↓
CRAFTYBASE ORDER CLOSED → COGS recorded automatically
```

### Daily Timeline (Target: 2-Business-Day Fulfillment)

**Day 0 (Order placed)**:
- Any time: Customer places order on Etsy
- Etsy sends email notification instantly
- Note: Orders placed after 5 PM count as "Day 0" for 2-business-day clock starting next business morning

**Day 1 (First business morning after order)**:
- 7:00 AM: Review all new orders from past 24 hours
- 7:15 AM: Add to print queue (see Section 2 for queue management)
- 7:30 AM: Check Craftybase sync — confirm order appears and material inventory is deducting correctly
- 8:00 AM: Start first print job
- [Print time: 25-35 min for single clip; 70-90 min for rail; batch times per Section 2]
- 10:00 AM - 2:00 PM: Prints complete for morning jobs; begin QA
- 2:00 PM: Prepare packages (Section 4)
- 3:00 PM: Generate Pirate Ship labels; prepare for shipment

**Day 2 (Second business day)**:
- 8:00 AM: Drop packages at USPS (or schedule USPS pickup for same-day)
- 8:30 AM: Mark orders as shipped in Etsy (enter tracking numbers)
- USPS tracking activates; customer receives automatic notification from Etsy

**Result**: Customer receives "Your order shipped" email within 1-2 business days of ordering. Package arrives 2-5 days after shipping depending on USPS zone.

**Exceeding the promise**: Target same-day ship for orders placed before noon. This creates positive review language ("Shipped same day!") that directly improves Etsy search ranking.

---

## Section 2: Print Queue Management

### Queue Structure

Maintain a daily print queue log. Google Sheets is sufficient through Month 3. Column definitions:

| Column | Content | Example |
|--------|---------|---------|
| Order ID | Etsy order number | #1234-5678 |
| Customer | First name only (privacy) | "Smith" |
| SKU | Product variant | modrun_clip_basic_black_3pk |
| Quantity | Units in order | 3 |
| Material | PLA or PETG | PLA |
| Color | Black / White / Grey | Black |
| Batch Group | For plate batching | Batch A |
| Est. Print Time | From lookup table | 90 min (3-pack plate) |
| Start Time | Actual start | 8:15 AM |
| End Time | Actual completion | 9:45 AM |
| Status | Queued / Printing / QC / Packaged / Shipped | Shipped |
| Notes | Defects, delays, customer notes | "Color variation noted, shipped" |

### Print Time Reference Table

| SKU | Material | Single | Per Plate (max units) | Plate Print Time |
|-----|----------|--------|----------------------|-----------------|
| modrun_clip (single) | PLA | 22-28 min | 8 clips | 75-90 min |
| modrun_clip (single) | PETG | 30-40 min | 8 clips | 100-120 min |
| modrun_rail (single) | PLA | 70-90 min | 2 rails | 90-110 min |
| modrun_rail (single) | PETG | 95-120 min | 2 rails | 120-140 min |
| 3-pack clips | PLA | N/A | 3-pack = 1 batch | 50-65 min |
| Starter Bundle (rail+3clips) | PLA | N/A | 1 bundle | 105-130 min |

**Plate batching rule**: Maximize plate utilization before any color or material change. At 8 clips per plate, run 3 plates of 8 black PLA clips (24 units, ~280 min) before switching to white. Each color change costs ~10 minutes + 5g purge filament.

### Color/Material Change Protocol

**PLA color change (e.g., black → white)**:
1. Load white PLA in AMS slot
2. In Bambu Studio or app: Select "Change Filament"
3. Purge 3-5g of black → white transition until clean extrusion
4. Verify extruded color is pure white before starting print
5. Time cost: ~8-12 minutes

**PLA → PETG material change**:
1. Load PETG in AMS slot
2. Increase nozzle temp from 210°C to 235°C (wait 2-3 min to stabilize)
3. Increase bed temp from 60°C to 80°C (wait 2-3 min)
4. Purge 5g+ to clear PLA residue
5. Verify PETG is extruding cleanly
6. Time cost: ~15 minutes

**PETG → PLA material change**:
1. Lower nozzle temp from 235°C to 210°C
2. Lower bed temp from 80°C to 60°C
3. Purge 5g+ at PLA temp to clear PETG
4. Note: PETG can leave residue at PLA temps — do a more thorough cold pull if stringing appears on first PLA print
5. Time cost: ~15-20 minutes

### Throughput Optimization

**Daily throughput targets by printer count**:

| Printers | Operating Hours/Day | Daily Output (clips) | Daily Output (rails) | Monthly Capacity |
|----------|---------------------|---------------------|---------------------|------------------|
| 1× P1S | 16 hours | 12-20 | 6-10 | 260-440 units |
| 2× P1S | 16 hours | 24-40 | 12-20 | 520-880 units |
| 5× P1S | 16 hours | 60-100 | 30-50 | 1,300-2,200 units |

**Note**: Monthly capacity far exceeds expected demand in Months 1-3. Do not add printers until monthly sales consistently exceed 150+ units (indicates demand justifies printer 2 ROI payback within 6 weeks).

---

## Section 3: QA Checklist and Tolerance Standards

### Dimensional Tolerance Standards

ModRun clips must meet ±0.5mm tolerances on engagement surfaces for reliable clip-to-rail fit. Tolerances tighter than this exceed FDM capability; looser than this creates visible fit variation between units.

**Measurement protocol**: Use digital calipers, minimum 0.01mm resolution ($15-25 from Amazon or Harbor Freight).

**Critical dimensions to check (measure 1 unit per batch of 5)**:

| Dimension | Target (from CAD) | Tolerance | Measurement Point |
|-----------|-----------------|-----------|------------------|
| Clip engagement width | CAD value | ±0.5mm | Inside face of clip engagement lip |
| Rail channel width | CAD value | ±0.5mm | Interior rail channel at widest point |
| Cable channel diameter | 6-10mm range | ±0.5mm | Diameter of cable retention groove |
| Clip wall thickness | CAD value | ±0.3mm | Thinnest wall section |

**When to measure**:
- Always: First unit of a new filament spool (batch variation check)
- Always: After any print setting change (temp, speed, layer height)
- Spot-check: 1 unit per 5-unit production batch
- Full-batch check: If a dimensional issue is found in spot-check, measure all units in the batch

### Per-Unit Visual QA Checklist

Complete this check for every single unit before packaging. Total time: 30-45 seconds per unit.

**Structural**:
- [ ] No layer delamination visible (hold up to light — look for gaps between layers)
- [ ] No warping at base or edges (place on flat surface — should not rock)
- [ ] No nozzle crash artifacts (gouges, blobs, or grooves from nozzle dragging through print)
- [ ] Part is fully printed to completion (not truncated mid-print)

**Surface quality**:
- [ ] Surface finish acceptable for commercial sale (light layer lines are acceptable; obvious roughness, stringing, or blobs are not)
- [ ] No visible color streaks from filament transition (if color change was recent)
- [ ] For PETG: No significant stringing (trim with craft knife if minor stringing present)
- [ ] For PLA: No elephant's foot at base (indicates bed temp too high or first layer squish excessive)

**Dimensional and functional**:
- [ ] Clip engages reference rail without binding or excessive force
- [ ] Clip retains on rail under gentle hand load (no accidental release)
- [ ] Cable channel accepts a 5mm cable without binding
- [ ] Weight within ±5g of reference unit (indicates consistent fill density)

### Defect Classification and Action

| Severity | Defect | Action | Customer Communication |
|----------|--------|--------|----------------------|
| Critical | Clip won't engage rail; visible crack; >1mm warp | Reject, reprint, do not ship | N/A (never ships) |
| Major | Layer separation visible; nozzle crash gouge | Reject, reprint, do not ship | N/A |
| Minor | Slight elephant's foot; minimal stringing trimmed | Ship — document in batch log | None required |
| Cosmetic | Single small blob; barely visible surface artifact | Ship — acceptable for handmade 3D product | None required |

**Target defect rates**:
- Critical reject rate: <1% (1 in 100 prints)
- Major reject rate: <2% (2 in 100 prints)
- Total scrap rate: <3% (3 in 100 prints)

**If scrap rate exceeds 5%**:
1. Stop production batch immediately
2. Check printer: Nozzle clog? Bed adhesion? Z-offset calibration?
3. Check filament: Open new spool if current spool has been open >48 hours in humid conditions (filament moisture causes stringing and poor layer adhesion)
4. Run calibration print before resuming production
5. If issue persists: Contact Bambu support or review print settings

### Batch QC Log

Record in your print queue spreadsheet, add these columns:

| Column | Content |
|--------|---------|
| Batch QC Date | Date of check |
| Units Printed | Total in batch |
| Units Rejected | Number scrapped |
| Reject Reason | What failed |
| Dimensional Check | Pass/Fail (if measured) |
| Notes | Filament lot, settings used, anomalies |

---

## Section 4: Packaging Specifications

### Packaging by SKU

**Phase 1 Packaging (Launch through ~200 units/month)**:

| SKU | Package Type | Box/Mailer Size | Weight (package+product) | Cost/Unit |
|-----|-------------|-----------------|-------------------------|-----------|
| Single clip | Poly mailer 6x9" 2.5mil | 6×9 inches | ~3.5 oz | $0.05 |
| 3-pack clips | Poly mailer 9x12" 2.5mil | 9×12 inches | ~7 oz | $0.05 |
| Rail system (single) | Poly mailer 9x12" 2.5mil | 9×12 inches | ~6 oz | $0.05 |
| Starter Bundle | Small corrugated box | 8×6×4 inches | ~12 oz | $0.30 |
| Deluxe Professional Kit | Medium corrugated box | 12×10×6 inches | ~28 oz | $0.75 |

**Phase 2 Packaging (200+ units/month, branded packaging)**:

| SKU | Package Type | Size | Cost/Unit | Lead Time |
|-----|-------------|------|-----------|-----------|
| Single/3-pack clips | Custom-printed poly mailer | 9×12 inches | $0.38-0.50 | 10-14 days |
| Rail/kit | Custom kraft box (Packlane) | 8×6×4 inches | $0.76-1.10 | 10-14 days |
| Deluxe Kit | Custom kraft rigid box (Arka) | 12×10×6 inches | $1.80-2.50 | 14-21 days |

### Packaging Content Specifications

**All orders (Phase 1)**:
- Product in biodegradable crinkle paper or tissue wrap (adds minimal weight, prevents scratching, perceived value upgrade for $0.02)
- Thank-you card: 3×4" card, printed on home laser/inkjet printer with "Thank you for supporting ModRun" + "30-day satisfaction guarantee" + shop URL. Cost: <$0.05 per card.

**Standard and Premium tier additions (Phase 1)**:
- Installation instructions: Half-letter sheet (5.5×8.5"), fold in thirds, print duplex. Cover: ModRun logo + product name. Inside: 5-step installation diagram. Cost: <$0.05 per insert.

**Deluxe Kit additions (Phase 1)**:
- Full-color installation guide: 4 pages, letter size, folded to booklet. Color print at FedEx Office (~$0.80 per copy). Justified at $179.99 price point.
- Warranty card: 3×5" card with "Lifetime Mechanical Warranty" header + claim instructions
- Personal note (optional): Handwritten or printed note from founder adds authenticity

### Branded Packaging Print Template (Phase 2 Reference)

When ordering custom-printed poly mailers at Month 3, provide this artwork specification:

**Custom poly mailer design spec (for Vistaprint or Smart Shipping Supply)**:
- Size: 9×12 inches (standard mailer size)
- Color: White base (for clean brand look) or grey base (premium feel)
- Front side print area: Full bleed
- Design elements:
  - ModRun wordmark (top-left, minimum 30pt font for readability when package is small)
  - Tagline: "Original Cable Management" (underneath wordmark)
  - Simple geometric pattern or cable motif (full-bleed background in 15% opacity)
  - Bottom: "Made in [your state] — Original Design" (reinforces Etsy compliance)
- Back side print area: Full bleed
- Design elements:
  - "Thank you for your order" (top)
  - Social media handles if active (@modrundesign or similar)
  - QR code linking to Etsy shop or review page
  - "30-Day Satisfaction Guarantee" badge

**File specifications for custom mailer order**:
- Format: PDF or PNG at 300 DPI minimum
- Color mode: CMYK (not RGB — printers use CMYK)
- Bleed: 0.125" on all edges
- Safe zone: Keep text/logos 0.25" from edges
- Recommend: Use Canva Pro ($12/month) for template → export as print-ready PDF

### Packaging Materials Procurement

**Phase 1 immediate order (Days 1-3 after test print go)**:

| Item | Supplier | Qty | Cost | Link |
|------|---------|-----|------|------|
| Poly mailers 9×12" 2.5mil | Shop4Mailers | 500 units | ~$25 | shop4mailers.com |
| Packing tape 2" clear | Amazon | 6-pack | ~$12 | Search "packing tape 6 pack" |
| Digital scale (0.1oz precision) | Amazon | 1 unit | ~$20 | Search "postal scale ounces" |
| Crinkle paper (filler) | Amazon | 1 lb pack | ~$8 | Optional but adds value |
| Thank-you card stock | Amazon/Staples | 50-sheet pack | ~$8 | Print at home |

**Total Phase 1 packaging startup cost**: ~$73

---

## Section 5: Shipping Label Generation — Pirate Ship Workflow

### Pirate Ship Account Setup

1. Create account at pirateship.com (free — no monthly fees; Pirate Ship earns a carrier margin)
2. Add credit card as payment method
3. Verify account email
4. Connect Etsy store: Settings → Store Connections → Etsy → Authorize

### Daily Shipping Workflow (Per Order)

**Option A: Pirate Ship Etsy Import (Recommended)**

1. Log in to Pirate Ship
2. Click "Ship" → "Import Orders" tab
3. Select your Etsy store → click "Import Orders"
4. All open (unshipped) Etsy orders appear, pre-populated with:
   - Customer name and delivery address
   - Product name (from Etsy listing)
   - No weight pre-populated — you must enter this
5. For each order:
   - Select carrier: USPS Ground Advantage (default for <1 lb)
   - Enter package weight (from reference table: single clip = 3.5 oz, etc.)
   - Enter package dimensions (for cubic rate calculation)
   - Click "Get Rates" — Pirate Ship shows all available rates
   - Select cheapest appropriate service
   - Click "Buy Label"
6. Print all labels as PDF → print on thermal printer (preferred) or standard paper with label sticker
7. Apply labels to packages

**Option B: Manual Shipment (for orders outside Etsy)**

Same as above but click "Ship From Scratch" and manually enter recipient address.

### Rate Selection Guide

**For packages under 1 lb (most ModRun orders)**:
- Default: USPS Ground Advantage (cheapest, 2-5 days)
- Check: Pirate Ship auto-rates between Weight-Based and Cubic — always shows cheapest

**For packages 1-2 lbs (kits and bundles)**:
- Compare: Ground Advantage vs. Priority Mail — sometimes Priority is nearly same price for much faster delivery
- Rule of thumb: If Priority is <$1.50 more than Ground Advantage, upgrade to Priority (better customer experience for minimal cost)

**For Deluxe Kit (~28 oz)**:
- Likely crosses into Priority Mail territory at this weight/price
- Always use Pirate Ship's rate comparison before purchasing

### 2026 Rate Reference (Pirate Ship, USPS Ground Advantage, includes 8% temporary surcharge)

| Weight | Zone 1-2 | Zone 3-4 | Zone 5-6 | Zone 7-8 |
|--------|----------|----------|----------|----------|
| Under 1 oz | $3.78 | $4.05 | $4.40 | $4.73 |
| 2-4 oz | $3.78 | $4.15 | $4.52 | $4.86 |
| 5-8 oz | $4.48 | $5.13 | $5.94 | $6.67 |
| 9-13 oz | $5.13 | $6.05 | $7.13 | $8.32 |
| 14-16 oz | $6.27 | $7.65 | $9.11 | $10.67 |

Note: The 8% surcharge applies through January 17, 2027. After that date, rates will revert (Pirate Ship will update automatically).

### Marking Orders Shipped in Etsy

After purchasing labels in Pirate Ship:
1. Pirate Ship can auto-update Etsy if integration is enabled (Settings → Store Connections → Etsy → "Auto-mark as shipped" toggle)
2. If not using auto-update: Log into Etsy → Orders → Open order → "Mark as Shipped" → Enter USPS tracking number
3. Etsy sends automatic "Your order has shipped" email to customer with tracking link

**Do not delay marking as shipped.** Etsy's seller score includes "ship-on-time rate." Marking late (even if physically shipped on time) degrades your seller rating.

---

## Section 6: Craftybase Integration (Month 2+ Operations)

### Why Craftybase

At 20+ orders/month, manually tracking material usage, COGS per order, and inventory levels becomes error-prone. Craftybase's Etsy integration automates this:

- Every Etsy order auto-imported
- Each order deducts the correct material quantity from your material inventory (e.g., 75g PLA from Basic Clip inventory)
- COGS calculated per order using your material purchase prices
- Revenue recorded with Etsy fees already deducted
- IRS Schedule C report generated for tax season

**Cost**: $49/month (Studio plan, 250 order lines/month). Justified at 20+ orders/month where manual tracking risk exceeds the cost.

### Craftybase Setup Workflow

**One-time setup (1-2 hours)**:

1. Create account at craftybase.com, select Studio plan ($49/month), start 14-day trial
2. Connect Etsy: Settings → Integrations → Etsy → Authorize
3. Create your materials in Craftybase:
   - Material: "eSUN PLA+ Black" — unit: grams — purchase price: $0.012/g (at $12/kg)
   - Material: "eSUN PLA+ White" — same pricing
   - Material: "eSUN PETG Black" — unit: grams — purchase price: $0.018/g (at $18/kg)
   - Material: "Shop4Mailers Poly Mailer 9×12" — unit: each — purchase price: $0.05
4. Create your products (recipes) in Craftybase, linking them to Etsy listings:
   - Product: "modrun_clip_basic_black_single"
   - Recipe: 75g eSUN PLA+ Black + 1× poly mailer
   - Linked Etsy listing: "ModRun Basic Cable Clips - Set of 3 PLA"
5. Test: Place a test order (or manually trigger sync) — verify material inventory deducts correctly

### Ongoing Craftybase Workflow

**Automatic (no action required)**:
- Etsy orders sync every 4 hours (Studio plan)
- Material inventory deducts as orders close
- COGS calculated per order

**Manual (5 minutes/week)**:
- Log new material purchases when filament arrives: Craftybase → Materials → [Material Name] → Add Purchase
  - Enter: quantity in grams, total price paid, supplier, date
  - Craftybase recalculates rolling average cost automatically
- Review weekly COGS report: Craftybase → Reports → Manufacturing Cost

**Monthly (10 minutes)**:
- Review low-inventory alerts (Craftybase notifies when material stock drops below threshold you set)
- Download monthly P&L summary for bookkeeping
- Verify Etsy revenue matches Craftybase imported revenue (reconciliation)

---

## Section 7: Cost Modeling by Fulfillment Method

### Phase 1: In-House Fulfillment (Launch through ~500 orders/month)

**Total per-order cost breakdown (average order = $22 at 1.5 units)**:

| Cost Component | Economy Clip | Standard Kit | Premium Deluxe Kit |
|----------------|-------------|-------------|-------------------|
| Material (75g PLA @ $12/kg) | $0.90 | $2.25 | $4.50 |
| Electricity ($0.03/print-hour) | $0.02 | $0.06 | $0.15 |
| Printer depreciation | $0.05 | $0.13 | $0.35 |
| Packaging | $0.05 | $0.30 | $0.75 |
| Etsy transaction fee (3%) | $0.27 | $0.87 | $2.10 |
| USPS Ground Advantage (Zone 4 avg) | $4.15 | $5.50 | $7.20 |
| Labor (5 min packaging @ $20/hr) | $1.67 | $1.67 | $3.33 |
| **Total Fulfillment Cost** | **$7.11** | **$10.78** | **$18.38** |
| **Retail Price** | **$8.99** | **$28.99** | **$69.99** |
| **Gross Margin** | **21%** | **62.8%** | **73.7%** |

**Important note on Economy Clip margin**: The single clip at $8.99 has poor margin (21%) due to shipping cost dominance. This is why the pricing strategy pushes customers to 3-packs ($22.99, margin ~59%) and bundles ($28.99, margin ~63%). Do not optimize the $8.99 SKU as a primary revenue driver.

### Phase 2: Wholesale Filament Impact on Margins

At eSUN wholesale $12.50/kg (vs $15 retail) and Anycubic $10.49/kg:

| SKU | Retail Price | Phase 1 Margin | Phase 2 Margin (eSUN $12.50/kg) | Delta |
|-----|-------------|---------------|--------------------------------|-------|
| Basic Clip single | $8.99 | 21.0% | 23.0% | +2.0pp |
| 3-Pack Clips | $22.99 | 58.1% | 60.0% | +1.9pp |
| Starter Bundle | $28.99 | 62.8% | 65.0% | +2.2pp |
| Deluxe Kit | $69.99 | 73.7% | 74.8% | +1.1pp |

**Key insight**: Supplier negotiation improves margins modestly. The biggest margin lever is **average order value** — every bundle sale vs. single-unit sale adds $15-20 in revenue with minimal additional cost.

### Phase 3: 3PL Evaluation (500+ orders/month)

At 500+ orders/month, self-fulfillment labor becomes the bottleneck (at 5 minutes/order × 500 = ~42 hours/month = 1 part-time employee). Evaluate 3PL options:

| Option | Cost/Order | Monthly (500 orders) | Advantage | Break-Even vs. Self-Fulfill |
|--------|-----------|---------------------|-----------|---------------------------|
| Self-fulfill | $8-12 labor+overhead | $4,000-6,000 | Control, flexibility | N/A |
| Simpl Fulfillment | $5-8/order + storage | $2,500-4,000 | Scale without staff | >400 orders/month |
| ShipMonk | $4-7/order | $2,000-3,500 | Lower cost at volume | >600 orders/month |
| Amazon FBA (top SKUs) | $2.50-5.00 + 15% | ~$3,500 total | Prime badge | >300 units/month on Amazon |

**Recommendation**: Do not evaluate 3PL until Month 5 (6+ months of sales data). 3PL setup requires minimum order volumes, packaging standardization, and stable SKU mix — all of which require time to establish.

---

## Section 8: Integration with Print Queue

### Batch Sizes for Throughput Optimization

**Rule: Never print fewer than 3 units of the same SKU+color in a single session if demand supports it.**

Reasoning: The fixed cost of printer setup, plate preparation, and post-print cleanup is the same whether you print 1 or 6 clips per plate. Batching to plate capacity reduces per-unit fixed cost significantly.

**Recommended batch triggers**:

| SKU | Minimum Batch Size | Maximum Plate Capacity | Print Once Per |
|-----|-------------------|----------------------|----------------|
| Basic Clips | 6 units | 8 units/plate | Day (if demand) |
| Premium Clips | 3 units | 8 units/plate | 2 days |
| Rail System | 2 units | 2 units/plate | 2 days |
| Starter Bundle | 1 unit (kit) | 1 kit/session | Per order |
| Deluxe Kit | 1 unit (kit) | 1 kit/session | Per order |

**Buffer stock printing**: On days with zero or few orders, use idle printer time to build safety stock. Target 14-day supply of top 3 SKUs (Basic Clips, Premium Clips, Rail System) as buffer. This decouples fulfillment from same-day print dependency.

### Print Queue and Order Integration

**Morning routine (15 minutes)**:
1. Review Etsy orders from past 24 hours (Craftybase sync already imported them)
2. In Craftybase: Check "Orders to Fulfill" queue — these are open orders not yet marked shipped
3. Cross-reference with finished goods shelf (some orders may ship from buffer stock without printing)
4. Add any orders requiring new prints to daily print queue (Google Sheet)
5. Assign color/material priority — batch same-material jobs first
6. Start first print job

**Evening routine (5 minutes)**:
1. Log all completed prints in queue sheet (actual vs. estimated time)
2. Move QC-passed units to finished goods shelf with label (SKU, color, date)
3. Log any defects/failures
4. Verify Etsy orders shipped today are marked in Etsy + Craftybase
5. Set up overnight print job if printer can run unattended (multi-plate batch of single SKU, stable settings)

---

## Section 9: Scaling Timeline

### Stage 1: Single Printer, Manual Queue (Months 1-3)

**Target capacity**: 50-200 units/month
**Operations**: 1× P1S, daily queue management, Google Sheets tracking, manual Pirate Ship labeling
**Do not yet**: Craftybase (optional — justified at 20+ orders/month), second printer, 3PL evaluation

**Key actions**:
- Establish consistent daily print+ship rhythm
- Validate 2-business-day promise (track actual vs. stated)
- Document actual vs. projected print times (update lookup table)
- Track defect rates (this is data for Month 3 process review)

### Stage 2: Two Printers, Basic Optimization (Month 3-4)

**Trigger**: Monthly sales consistently exceeding 30 units (≈150 units/month run rate)
**Investment**: Second Bambu P1S + AMS (~$1,400), additional bench space (~$200)

**Operational changes**:
- Printer 1: Basic Clips (high volume, fast prints, all colors)
- Printer 2: Rails + Premium Clips (longer prints, specialty)
- Dual print queue in same Google Sheet (add "Printer #" column)
- Craftybase mandatory at this point (inventory tracking requires automation)
- USPS pickup scheduling (2+ drop-offs/day becomes inefficient)

**Expected throughput**: 100-300 units/month

### Stage 3: Multi-Printer Farm (Month 5-8)

**Trigger**: Monthly sales exceeding 100 units (≈500 units/month run rate)
**Architecture**: Per multi-printer-architecture.md (5× P1S row configuration, zone separation)
**Staffing**: Consider 1 part-time operator (10-15 hours/week) for harvest, QC, packaging

**Operational changes**:
- Zone-separated workflow (print zone, harvest+QC zone, pack zone)
- Craftybase Business plan ($129/month, 5,000 order lines, hourly sync)
- Consider custom printed packaging (Packlane/Vistaprint at 500+ units/month)
- Evaluate Simpl Fulfillment or ShipMonk 3PL at this scale

**Expected throughput**: 500-1,500 units/month

---

## Section 10: Monthly Operations Dashboard

Track these KPIs monthly in your Craftybase reports + Google Sheets:

| KPI | Month 1 Target | Month 2 Target | Month 3 Target | How to Measure |
|-----|---------------|---------------|---------------|----------------|
| Units shipped | 8-15 | 30-50 | 80-120 | Etsy order count |
| Average order value | $15-20 | $18-25 | $22-30 | Revenue / orders |
| Fulfillment speed (avg days) | <2 days | <2 days | <2 days | Etsy fulfillment tracker |
| Print success rate | ≥95% | ≥97% | ≥97% | Batch QC log |
| Defect rate (per unit) | <5% | <3% | <2% | Batch QC log |
| Return rate | <7% | <5% | <4% | Etsy returns |
| Customer reviews | 2+ | 10+ | 20+ | Etsy reviews tab |
| Review rating | ≥4.5 stars | ≥4.5 stars | ≥4.7 stars | Etsy reviews tab |
| Gross margin % | ≥55% | ≥58% | ≥62% | Craftybase P&L |
| Monthly net profit | $0-50 | $100-250 | $400-700 | Craftybase P&L |

**Monthly review process (30 minutes at month end)**:
1. Export Craftybase monthly P&L report
2. Calculate actual gross margin by SKU
3. Compare actual print times vs. table (update table if significant deviation)
4. Review defect log — identify any recurring issues
5. Calculate Etsy conversion rate (Etsy Stats: Views / Orders)
6. Document one process improvement for next month

---

## Appendix: Tools and Resources

**Software**:
- Pirate Ship (shipping labels, commercial USPS rates): pirateship.com
- Craftybase (Etsy COGS tracking, inventory): craftybase.com
- Etsy Seller App (mobile order notifications): iOS / Android
- Bambu Studio (print slicing and queue management): bambulab.com/software
- Google Sheets (queue tracking, inventory): sheets.google.com

**Hardware**:
- Rollo Thermal Printer (4×6" labels, $100-130): rollo.com
- Digital calipers (±0.01mm precision, $15-20): Amazon search "digital calipers"
- Digital postal scale (0.1oz precision, $15-20): Amazon search "postal scale"
- LED task light for QC inspection ($20-30): Any desk lamp with CRI ≥90

**Packaging suppliers**:
- Shop4Mailers (poly mailers, budget): shop4mailers.com
- Vistaprint (custom-printed poly mailers, Phase 2): vistaprint.com/packaging
- Smart Shipping Supply (eco-certified custom mailers): smartshippingsupply.com
- Packlane (custom boxes, Phase 2 gift bundles): packlane.com

**Reference documents**:
- multi-printer-architecture.md (scaling guidance and farm layout)
- supplier-negotiation-playbook.md (filament sourcing and cost reduction)
- pricing-strategy.md (COGS validation and tier margins)
- post-test-print-launch-prep.md (full launch sequence)

---

**Document Status**: Ready for activation on Etsy launch day
**Version**: 2.0 (expanded with Craftybase integration, packaging specs, QA tolerances, cost modeling)
**Confidence Level**: High
**Next review**: End of Month 1 — validate actual throughput vs. projections, update lookup tables
