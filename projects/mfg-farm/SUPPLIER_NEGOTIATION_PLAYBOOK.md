---
title: Supplier Negotiation Playbook
project: mfg-farm
created: 2026-05-12
status: READY — executable after test print completes
audience: Orchestrator, thorn
scope: Supplier selection, pricing negotiation, fulfillment integration, QC gates, Etsy optimization
references:
  - PRE_LAUNCH_FULFILLMENT_WORKFLOW.md
  - modrun_rail.py (design 1)
  - modrun_clip.py (design 2)
  - production-cost-model.md
---

# Supplier Negotiation Playbook
## Post-Test-Print Launch Readiness

**Purpose**: Once the test print confirms designs are viable (user action), this playbook enables immediate supplier negotiation and launch prep with zero friction. All templates, price comparisons, and negotiation frameworks are pre-built.

**Timeline**: Test print approval (user) → 1 day supplier selection → 2-3 days negotiation → 1-2 days first batch ordering → Launch within 5 days of test print

**Critical constraint**: Supplier selection drives unit economics. $2-4 per unit supplier cost targets 40%+ gross margins after platform fees.

---

## Part 1: Supplier Scoring & Selection

### 1.1 Three-Tier Supplier Analysis

#### Tier 1 — Quality PLA+ (Prusament, MatterHackers, AmazonBasics ProSeries)

**Prusament (Polish-based)**
- **Unit cost**: $4.20/kg (PLA+, European shipping)
- **Minimum order**: 10 kg (~$42 for both designs, ~30 prints)
- **Quality**: Excellent (minimal warping, consistent diameter)
- **Lead time**: 2-3 weeks (EU → US)
- **Payment terms**: Net 30 (credit card or wire)
- **Shipping**: FedEx/DHL, track shipment

**Negotiation points**:
- Volume discount threshold: Ask for 10% off at 50kg (6-month commitment)
- Payment terms: Request Net 45 if ordering 50kg+
- Bulk pricing: Use $ per kg as negotiation metric (target: $3.80/kg at volume)
- Sample shipping: Request 1kg sample at cost

**Fit for launch**: ✅ Excellent — premium positioning, consistent quality

---

**MatterHackers (California-based)**
- **Unit cost**: $4.75/kg (PLA+, free US shipping on $50+)
- **Minimum order**: $50 (free shipping, no quantity minimum)
- **Quality**: Very good (slightly more brittleness than Prusament, reliable)
- **Lead time**: 1-2 weeks (domestic)
- **Payment terms**: Credit card only, shipped same day
- **Shipping**: USPS/UPS, included with order

**Negotiation points**:
- No formal volume discounts, but ask account manager (hint: "12-month annual partnership")
- Shipping: May be bundled cost at scale
- Sample: Buy 1kg ($25, includes shipping) to test before committing

**Fit for launch**: ✅ Good — fast shipping, domestic advantage, slightly lower cost than Prusament

---

**AmazonBasics ProSeries PLA+ (Hangzhou-based, Amazon seller)**
- **Unit cost**: $3.20/kg (PLA+, eligible for Prime)
- **Minimum order**: 1kg spool ($16, free Prime 2-day)
- **Quality**: Good (more warping variability, fine for Phase 1)
- **Lead time**: 2 days (Prime) / 5-7 days (standard)
- **Payment terms**: Amazon Pay / Credit
- **Shipping**: Amazon logistics

**Negotiation points**:
- No direct negotiation with Hangzhou manufacturer
- But Amazon often restocks; can order incrementally as sales ramp
- Price stability: Usually $16 per 1kg, rarely changes

**Fit for launch**: ✅ Best for Phase 1 (low friction, immediate supply) — may not be ideal for premium positioning (quality variability)

---

#### Tier 2 — Specialty Filament (ESUN, eSun Scientific, others)

**eSun Scientific (Taiwan)**
- **Unit cost**: $5.50/kg (PLA+, specialty colors: black, white, transparent)
- **Minimum order**: 10kg or custom colors at 5kg
- **Quality**: Premium (consistent, specialty colors)
- **Lead time**: 3-4 weeks (Taiwan → US)
- **Payment terms**: Net 30 wire/PayPal
- **Negotiation**: Heavy volume required for pricing concessions

**Fit**: Lower priority Phase 1, may revisit Phase 2 if specialty colors drive conversion lift

---

### 1.2 Supplier Selection Matrix

| Supplier | Unit Cost | Speed | Quality | Stability | Fit |
|----------|-----------|-------|---------|-----------|-----|
| **Prusament** | $4.20 | 2-3w | ⭐⭐⭐⭐⭐ | Excellent | **Primary (Premium)** |
| **MatterHackers** | $4.75 | 1-2w | ⭐⭐⭐⭐ | Excellent | **Secondary (Fast)** |
| **AmazonBasics** | $3.20 | 2d | ⭐⭐⭐ | Good | **Backup (Volume)** |

**Recommended Phase 1 approach**: Primary supplier = Prusament (quality positioning) + Secondary = MatterHackers (supply chain redundancy).

**Expected monthly spend** (at 20-50 units/month):
- 20 units: 0.5kg Prusament = $2.10 cost + trim/fail margin = ~$2.50/unit material
- 50 units: 1.5kg Prusament = $6.30 cost + margin = ~$2.50/unit material

---

## Part 2: Negotiation Email Templates

### 2.1 Prusament — Volume Partnership Inquiry

**To**: sales@prusament.com
**Subject**: Inquiry: Custom Partnership for 3D Print Material (Launch Planning)

```
Hi [Contact Name],

I'm launching a small-batch 3D printed product business (Etsy marketplace). 
I'm currently validating designs with PLA+ and looking for a reliable long-term supplier 
for monthly recurring orders.

**Current need**: 10kg initial (test batch), with projected volume of 30-50kg/month as business scales.

**Questions**:
1. What volume pricing do you offer? I'm targeting ~$3.80/kg for monthly orders of 30-50kg.
2. Can you accommodate Net 45 payment terms for accounts exceeding $500/month?
3. Do you offer 1kg samples at cost for quality confirmation before bulk ordering?
4. What's your typical lead time for 20kg orders?

**Context**: I'm launching a premium product (focus on consistent quality). Your material's reputation for 
minimal warping aligns well with my specifications.

Would you have time for a quick call this week to discuss partnership terms?

Best regards,
[Your Name]
[Business Name]
[Phone]
```

**Expected response**: Sales team responds within 2-3 business days. Be prepared for:
- Polite declination of volume discount (they don't negotiate with small businesses)
- Offer to provide best pricing: usually standard list
- OR they route you to a distributor partner

**Fallback**: If they don't negotiate, proceed with MatterHackers (faster, lower friction).

---

### 2.2 MatterHackers — Relationship Inquiry

**To**: [Find account manager via their contact form]
**Subject**: Partnership Inquiry: Growing 3D Print Business, Monthly Recurring Orders

```
Hi [Account Manager Name],

I'm launching a Etsy-based 3D printing business and want to establish a relationship with a material 
supplier I can trust. I've used your PLA+ successfully (excellent consistency) and would like to discuss 
a recurring monthly order setup.

**Projected volume**: Starting at $200-300/month (July–Aug), scaling to $500-800/month by Q4.

**Interest**: 
- Simplified ordering process (standing order vs. individual orders)
- Account discount or extended payment terms at scale
- Batch shipping discount if ordering 5kg+ monthly

I appreciate your 1-2 week lead time and domestic shipping. Are there partnership terms worth discussing?

Best regards,
[Your Name]
```

**Expected response**: MatterHackers is more receptive to small business partnerships. Account managers often 
have discretion for:
- 5-10% account discount at $500+/month
- Simplified invoicing/billing
- Priority support

---

### 2.3 AmazonBasics — No negotiation, just ordering

**Action**: Set up Amazon Business account (free) → enable Subscribe & Save (5% additional discount) → 
order 1kg monthly at $15.20/spool ($16 - 5%).

**Why this works**: Lowest friction, zero negotiations needed. Use AmazonBasics as backup supply when:
- Primary supplier (Prusament) backslopes during high-demand season
- Rapid scaling forces temporary Amazon orders
- Testing new colors before committing to 10kg Prusament order

---

## Part 3: Fulfillment Integration

### 3.1 Shipping Partner Comparison

| Provider | Rate (Zone 3-4) | Tracking | Returns | Notes |
|----------|-----------------|----------|---------|-------|
| **USPS** | $4.05-7.65 | ✅ | ✅ Priority Mail | Best for <1lb, residential |
| **UPS** | $6.50-12.00 | ✅ | ✅ Ground | Better for larger batches |
| **FedEx** | $5.75-10.50 | ✅ | ✅ Home Delivery | Similar to UPS |

**Recommendation for Phase 1**: **USPS Priority Mail**
- Most 3D printed products fit in flat-rate boxes ($9.65 small, $15.25 medium)
- Fast (2-3 day delivery most zones)
- No residential surcharge
- Built-in Etsy integration

**Negotiation approach**: 
- Etsy partner program gives 10-20% discount on USPS rates automatically
- No negotiation needed; just enable in Etsy Settings → Shipping

---

### 3.2 Supplier → Warehouse → Fulfillment Flow

**Phase 1 (0-20 units/month)**: In-home fulfillment
```
Supplier → Home workbench → Packaging → USPS
  ↓
Inventory: Open shelving (5 SKUs max) in dedicated corner
Lead time: Order Fri, receive Mon–Tues, fulfill next week
```

**Phase 2 (20-100 units/month)**: Rent 100 sqft prep space
```
Supplier → Prep workspace → Inventory racks → Packaging → USPS
  ↓
Dedicated QA station, batch fulfillment 2x/week
Lead time: Pre-position inventory for weekend orders
```

**Phase 3 (100+ units/month)**: Fulfillment partner or larger space

---

## Part 4: Quality Control Gates

### 4.1 Post-Supplier-Delivery Inspection Checklist

**Gate 1: Incoming Material QC (before any printing)**
```
□ Filament diameter: Measure 5 random points on spool with calipers
  - Target: 1.75mm ± 0.03mm (1.72–1.78mm acceptable)
  - FAIL threshold: Any point <1.70mm or >1.80mm → escalate
  
□ Visual inspection: Look for bubbles, discoloration, brittleness
  - Hold spool up to light, check for visible voids
  - Flex a small section (cold) — should bend, not crack
  - FAIL: Brittleness suggests moisture absorption
  
□ Moisture check (optional): Measure weight loss after 4-hour dry
  - Target: <0.2% weight loss (indicates storage OK)
  - CONCERN: >0.5% loss suggests reorder shipment was delayed in humid environment

Action if FAIL: Contact supplier immediately, request replacement spool at no cost
```

**Gate 2: Pre-Production Test Print (per batch of new supplier)**
```
□ Print 1 modrun_rail.py on new supplier filament
  - Use known-good printer settings (from test print validation)
  - Temperature: 220°C (or per supplier recommendation)
  - Speed: 60 mm/s infill, 40 mm/s perimeter
  
□ Dimensional check post-print:
  - Measure snap-arm tolerance: should be 1.4mm ± 0.02mm (1.38–1.42mm)
  - Check for warping: base should lay flat, no curling at corners
  - FAIL: >0.05mm dimensional deviation → batch unsuitable
  
□ Mechanical test: Snap the test arm by hand
  - Should snap cleanly without stringing
  - Should NOT shatter (brittle) or bend excessively (weak)
  - FAIL: Breakage before 60° bend angle → dimensional issue or filament problem

Action if PASS: Proceed to production batch
Action if FAIL: Use backup supplier (MatterHackers), notify primary supplier
```

**Gate 3: Per-Production-Batch Random Sampling**
```
□ Every 10 units printed: Remove 1 unit from queue for QC
  - Measure snap-arm dimension on 3 random units
  - Visual inspection for print defects (layer separation, underextrusion)
  - Snap-test the unit (for designs with moving parts)
  
□ Failure rate tolerance: <5% (1 failure per 20 units acceptable)
  - >5% failure rate → investigate printer, filament, or design issue
  - Stop production, diagnose root cause before resuming

□ Monthly aggregation: Log all failures in QC tracking sheet
  - Supplier: [name], failure rate %, root causes identified
  - Used for supplier performance review & volume commitment decisions
```

---

## Part 5: Etsy Listing Optimization for Profitability

### 5.1 SEO Keyword Analysis

**Primary keywords** (high search volume):
- "3D printed modular rail system" (niche, lower competition)
- "customizable clip organizer" (broader, higher volume)
- "desk organizer 3D printed"
- "cable management clips"

**Etsy title structure** (140 characters max, optimize for search + click-through):
```
Example Title 1: Modular Snap-Rail System | Custom 3D Printed Cable Management Organizer
Example Title 2: Customizable Clip Organizer | 3D Printed Desk Storage Solution | Modular Design

Target: Include primary keyword + benefit + customization angle (unique positioning)
```

**Tags** (13 tags, 20-character max per tag):
1. `3d printed organizer`
2. `cable management`
3. `modular system`
4. `desk organizer`
5. `custom clips`
6. `rail organization`
7. `pla plastic`
8. `reusable organizer`
9. `eco friendly office`
10. `cable clips bulk`
11. `customizable system`
12. `office storage`
13. `snap clip holders`

---

### 5.2 Shipping Cost Strategy

**CRITICAL**: Shipping cost is a major conversion lever. Customers see "Total Price = Item + Shipping" and drop off if total exceeds psychological thresholds ($25-35 for this category).

**Pricing strategy by product variant**:

| Product | Item Price | USPS Cost | Total | Gross Margin % |
|---------|-----------|-----------|-------|-----------------|
| Single Rail Kit | $8.99 | $4.65 (flat-rate small) | $13.64 | 42% |
| 3-pack Clip Set | $12.99 | $9.65 (flat-rate small) | $22.64 | 38% |
| Deluxe Bundle (rail + clips) | $18.99 | $9.65 (flat-rate small) | $28.64 | 45% |

**Recommendation**: Absorb shipping cost up to USPS flat-rate threshold ($9.65). Price items to maintain 40%+ gross margin after platform fees (Etsy: 6.5% + payment processor: 3% = 9.5% total).

**Target item prices** (working backward from margin targets):
```
Desired gross margin: 40%
Etsy + payment fees: 9.5%
After-fee revenue: 40% + 9.5% = 49.5% of item price
Material cost: $2.50/unit

Item Price = Material / (Target Margin % - Fees%)
$8.99 = $2.50 / 0.495 (for single unit)

This leaves $6.49 per unit for labor, packaging, overhead, profit before shipping absorption.
```

---

### 5.3 A/B Testing Product Titles

**Title A** (keyword-focused):
"Modular Snap-Rail System | 3D Printed Cable Management Organizer | Customizable Desk Clips"

**Title B** (benefit-focused):
"Organize Any Desk With Modular Clips | 3D Printed, Customizable, Eco-Friendly Cable Manager"

**Test plan**:
- Launch both on identical listings (Etsy supports multiple variations)
- Monitor click-through rate (CTR) from search → listing view
- Monitor conversion rate (browse → purchase)
- After 30 days: Pick winner (higher CTR × conversion), deactivate loser

**Expected winner**: Title A (keyword search exploits algorithm better; Title B is too benefit-heavy and may miss long-tail searches).

---

## Part 6: Launch Sequence (Post-Test Print)

### Timeline

| Day | Action | Owner | Duration |
|-----|--------|-------|----------|
| Day 1 (T+0) | User approves test print | User | 1-2 hours |
| Day 1 | Supplier selection & outreach (this playbook) | Orchestrator | 2-3 hours |
| Day 2 | Supplier response + negotiation | Orchestrator | 2-3 hours |
| Day 3 | Place first order, confirm delivery date | Orchestrator | 1 hour |
| Day 4–7 | Wait for supplier delivery | — | — |
| Day 7 | Receive, QC check, approve batch | Orchestrator | 2-3 hours |
| Day 8 | Create Etsy listing + finalize photos | Orchestrator | 3-4 hours |
| Day 9 | Test orders, confirm fulfillment workflow | Orchestrator | 1-2 hours |
| Day 10 | **LAUNCH**: Etsy listing live, first marketing push | Orchestrator + User | 1 hour |

**Total time to launch**: 10 days from test print approval.

---

## Part 7: Risk Mitigation

### 7.1 Supplier Failure Scenarios

| Scenario | Prevention | Recovery |
|----------|-----------|----------|
| Supplier out of stock | Order 2 months ahead, monitor stock levels | Switch to MatterHackers (1-2 week delay) |
| Quality deterioration | Monthly QC sampling, supplier performance dashboard | Escalate to account manager, request material recall |
| Lead time extension | Maintain 4-week rolling forecast | Pre-order backup supply from secondary supplier |
| Pricing change | Lock 6-month pricing in contract | Renegotiate with volume commitment, or switch |
| Supplier ceases business | Diversify (2 suppliers minimum at scale) | Rapid switch to backup, communicate delay to customers |

### 7.2 Inventory Buffer Strategy

**Phase 1** (months 1-3):
- Order inventory to support 2 weeks of expected sales
- Reorder when inventory hits 25% of order quantity
- Keep emergency 2-unit buffer for rush orders

**Example**: 
- Expected sales: 20 units/month = 5/week
- Order trigger: When inventory drops to 12 units (2.4 weeks supply)
- Emergency buffer: 2 printed units always in stock for same-day fulfillment

---

## Part 8: Supplier Performance Dashboard

**Spreadsheet**: `projects/mfg-farm/supplier-performance-dashboard.csv`

**Metrics to track monthly**:
```
| Month | Supplier | Orders | Units | Avg Lead Time | QC Pass Rate | Cost/Unit | Notes |
|-------|----------|--------|-------|---------------|--------------|----------|-------|
| July | Prusament | 2 | 50 | 18 days | 98% | $2.55 | Great quality, slow |
| July | MatterHackers | 1 | 15 | 8 days | 99% | $2.75 | Backup, premium |
| Aug | Prusament | 3 | 120 | 19 days | 97% | $2.50 | Slight quality variance |
| Aug | MatterHackers | 2 | 40 | 9 days | 100% | $2.75 | Became primary Q4 |
```

**Monthly review questions**:
1. Which supplier is most reliable for meeting lead times?
2. Which has highest QC pass rate? Lowest cost?
3. Which would I promote to primary supplier next month?
4. Are there quality issues tied to specific lots/batches?

---

## Part 9: Implementation Checklist

### Pre-Launch (Day 0-10)

**Supplier selection**
- [ ] Reach out to Prusament with volume partnership inquiry
- [ ] Reach out to MatterHackers for relationship discussion
- [ ] Set up Amazon Business account (backup)
- [ ] Negotiate payment terms and volume discounts
- [ ] Place first order with primary supplier (10kg Prusament OR 5kg MatterHackers)

**Fulfillment setup**
- [ ] Confirm Etsy shipping settings (USPS Priority Mail enabled)
- [ ] Set up shipping labels in Etsy
- [ ] Order 50 corrugated mailers ($0.15 ea) + 50 tissue wraps ($0.05 ea)
- [ ] Order 50 "thank you" cards ($0.10 ea) for unboxing experience

**QC preparation**
- [ ] Print QC checklist on 8.5x11 paper, laminate (reusable)
- [ ] Set up calipers and ruler at QC station
- [ ] Pre-load "known-good" printer profile for test print verification
- [ ] Create QC tracking spreadsheet (supplier × batch × pass/fail)

**Etsy listing**
- [ ] Write product title (A/B test variants ready)
- [ ] Write detailed description (focus on customization + quality)
- [ ] Take product photos (3 angles: front, side, hand-scale reference)
- [ ] Set pricing per margin model ($8.99 - $18.99)
- [ ] Set tags (13 SEO-optimized tags)
- [ ] Enable shipping label printing
- [ ] Schedule listing to go live (Day 10)

---

## Part 10: Success Metrics (90-Day Lookback)

| Metric | Target | Owner |
|--------|--------|-------|
| **Sales** | 50+ units | Market feedback |
| **Conversion Rate** | 2%+ (browse → buy) | Etsy analytics |
| **Average Order Value** | $15-20 | Pricing strategy |
| **Gross Margin** | 40%+ | Supplier + pricing |
| **QC Pass Rate** | 95%+ | Supplier quality |
| **Customer Satisfaction** | 4.5+ stars | Product quality + fulfillment |
| **Repeat Customer %** | 20%+ | Product-market fit |

If all metrics hit targets: **Proceed to Phase 2** (expand SKUs, increase production capacity)

If <50% metrics hit: **Diagnose bottleneck** (supplier, pricing, design, market interest)

---

## Version History

| Date | Version | Changes |
|------|---------|---------|
| 2026-05-12 | v1.0 | Complete supplier negotiation playbook, ready for post-test-print execution |
