---
title: ModRun Supplier Negotiation Playbook
date: 2026-04-28
version: 2.0
status: ready-for-execution
confidence: high
related: supplier-scorecard.csv, phase-2-supplier-research.md, pricing-strategy.md, post-test-print-launch-prep.md
---

# ModRun Supplier Negotiation Playbook

**Status**: Execute Week 1 in parallel with Etsy store setup
**Timeline**: Week 1 outreach → Week 2-3 responses → Month 2 commitment decision
**Goal**: Lock in primary + backup filament suppliers at target rates before Month 2 scaling phase
**COGS Reduction Target**: 20% blended reduction vs. retail baseline by Month 2

---

## Executive Summary

This playbook provides a 7-step negotiation sequence for securing filament supply at competitive rates. The data derives from supplier-scorecard.csv (Session 544 research), which ranked suppliers on price, reliability, lead time, and AMS compatibility. The strategy is designed to progress from zero supplier relationship to a locked 6-month primary supply agreement without requiring upfront volume commitments that the business cannot yet support.

**Core principle**: At launch volume (10-50 units/month), you have no leverage to demand deep wholesale discounts. The leverage comes from credibly articulating the growth trajectory — multi-printer farm roadmap, 6-month commitment in exchange for pricing, and genuine long-term partnership framing. Suppliers at this tier (eSUN, Anycubic, Polymaker) sell to hundreds of small operators. The ones who advance get better terms are the ones who are professional, committed, and clearly articulate a volume roadmap.

**Path selection based on Month 1 velocity**:

```
Month 1 units sold < 20:
  → Path A: Amazon Prime (no commitment required)
  → Supplier negotiation: deferred to Month 2
  → Risk: none; costs remain at retail

Month 1 units sold 20-50:
  → Path B: eSUN wholesale inquiry + Anycubic pallet pre-qualification
  → Commitment: 6-month rolling order at 10-20 kg/month
  → COGS reduction: 15-18% vs. retail

Month 1 units sold 50+:
  → Path C: eSUN wholesale (primary) + Anycubic 50kg (secondary) + Polymaker inquiry
  → Commitment: 6-month at 20-30 kg/month, with Anycubic as buffer
  → COGS reduction: 20-25% vs. retail
```

---

## Supplier Rankings (from supplier-scorecard.csv)

### Tier 1: Primary Production Suppliers

| Rank | Supplier | Product | Price | MOQ | Reliability | AMS Compat | Best For |
|------|----------|---------|-------|-----|-------------|-----------|----------|
| 1 | eSUN (Amazon) | PLA+ 1.75mm 10kg case | $11-13/kg | 10 spools | 9/10 | Confirmed excellent | Primary PLA (immediate) |
| 2 | Anycubic (direct) | PLA Basic 50kg pallet | $10.49/kg | None | 7/10 | Mixed reports | Secondary/pallet top-up |
| 3 | Polymaker (wholesale) | PolyLite PLA + Pro | $14.99/kg | ~$1,000 order | 9.5/10 | Confirmed excellent | Month 3+ quality tier |
| 4 | Overture (Amazon) | PLA + PETG 1.75mm | $11-14/kg PLA; $17-19/kg PETG | None | 8/10 | Confirmed good | PETG primary + PLA backup |

### Tier 2: Packaging and Fulfillment Suppliers

| Rank | Supplier | Product | Price | MOQ | Reliability | Phase |
|------|----------|---------|-------|-----|-------------|-------|
| 1 | Pirate Ship | USPS labels | $3.50-6.00/label | None | 10/10 | Phase 1 primary |
| 1 | Shop4Mailers | Poly mailers 9x12" | $0.05/unit | 100 units | 9/10 | Phase 1 primary |
| 2 | Packlane | Custom printed mailer box | $0.76-1.10/unit | 1 unit | 8/10 | Phase 2 gift bundles |
| 3 | EcoEnclose | Custom recycled box | $1.50-3.00/unit | 100 units | 8.5/10 | Month 4-6 eco tier |

### Tier 3: 3PL Suppliers (Phase 3 Evaluation)

| Rank | Supplier | Cost | MOV | Best For | Phase |
|------|----------|------|-----|----------|-------|
| 1 | Simpl Fulfillment | $5-8/order | None | 1-500 orders/month | Phase 3 (7,000+ units/mo) |
| 2 | ShipMonk | $4-7/order | 50 orders/mo | 50-500 orders/month | Phase 3 alternative |
| 3 | Amazon FBA | $2.50-5.00/unit + 15% | Per-ASIN | Top 2-3 SKUs Amazon | Phase 3 Amazon channel |

---

## The 7-Step Negotiation Sequence

### Step 1: Baseline Research and Pricing Snapshot (Day 1, ~30 minutes)

**Objective**: Establish current pricing reality before any outreach. Supplier prices fluctuate. Do not negotiate based on historical data without verifying current rates.

**Action checklist**:

1. **eSUN Amazon price check** (5 minutes)
   - Navigate to amazon.com
   - Search ASIN B0G2KSS613 (eSUN PLA Basic 10kg, black)
   - Search ASIN B0G2KWC5XL (eSUN PLA+ mixed colors)
   - Note current price per kg, Prime availability, estimated delivery
   - Note: If price is above $14/kg on Amazon bundles, the eSUN path may be less compelling than Anycubic

2. **Anycubic direct price check** (5 minutes)
   - Navigate to store.anycubic.com
   - Search or navigate to 50kg/100kg pallet deals
   - Verify current pricing (target: ~$10.49/kg as documented in session 544)
   - Note color availability for black PLA Basic
   - Note: Sale pricing fluctuates; lock in by ordering promptly if sale price confirmed

3. **Polymaker wholesale price check** (5 minutes)
   - Navigate to us-wholesale.polymaker.com
   - Verify PolyLite PLA pricing ($14.99/kg target at case quantity)
   - Note minimum order value (approximately $1,000)
   - Note: Only relevant for Month 3+; document for planning purposes today

4. **Overture price check** (5 minutes)
   - Navigate to amazon.com and search Overture PETG 1.75mm
   - Note current price per kg (target: $17-19/kg for PETG)
   - This is the primary PETG supplier path if premium clips drive demand

**Output**: Record current prices in a simple table. If prices have moved >15% from scorecard targets, adjust COGS projections accordingly before committing to any volume.

**Decision gate**: If eSUN Amazon is currently ≤$13/kg AND Anycubic 50kg is ≤$11/kg, proceed with the playbook as written. If both are above these thresholds, note the higher baseline and recalibrate COGS reduction targets for this document.

---

### Step 2: Strategy Selection and Path Commitment (Day 1, ~20 minutes)

**Objective**: Select your negotiation path based on current pricing and Month 1 velocity expectations. Commit to one path for Week 1 execution — do not hedge across multiple strategies simultaneously.

**Decision tree**:

```
Are Month 1 sales projections above 50 units?
  YES → Path C (Full dual-source engagement)
  NO →
    Are Month 1 sales projections 20-50 units?
      YES → Path B (eSUN wholesale + Anycubic pre-qual)
      NO → Path A (Amazon Prime, defer negotiation to Month 2)
```

**Path A: Amazon Prime Only (Low Volume, No Negotiation Required)**
- Who: Sellers projecting <20 units/month
- Supplier: eSUN via Amazon Prime (ASIN B0G2KSS613)
- Cost: $11-13/kg (standard retail, no discount)
- Lead time: 2-5 days (Prime)
- Action: None. Just buy from Amazon. Begin negotiation in Month 2 if sales exceed 20/month.
- Downside: No COGS reduction in Month 1. This is acceptable given low volume.

**Path B: Wholesale Engagement (Medium Volume)**
- Who: Sellers projecting 20-50 units/month
- Primary: eSUN wholesale inquiry (15-20 kg/month commitment)
- Secondary: Anycubic 50kg pallet pre-qualification (sample test option)
- Cost target: $11-12.50/kg (eSUN wholesale) OR $10.49/kg (Anycubic pallet)
- Actions: Send eSUN email Day 2. Contact Anycubic Day 2-3.
- Expected savings: $0.15-0.25/unit vs. retail Amazon

**Path C: Full Dual-Source Engagement (Higher Volume)**
- Who: Sellers projecting 50+ units/month
- Primary: eSUN wholesale (volume commitment for pricing)
- Secondary: Anycubic 50kg pallet (immediate supply, backup)
- Tertiary: Polymaker inquiry started (for Month 4 quality upgrade)
- Cost target: $10.49-12.50/kg combined
- Actions: Send eSUN email Day 2. Contact Anycubic Day 2. Contact Polymaker Day 5 (reference only, no commitment).
- Expected savings: $0.25-0.34/unit vs. retail Amazon

**Recommendation for Day 1**: If you are unsure about Month 1 velocity (which is normal before launch), execute Path B as your default. It commits to outreach without requiring volume commitments that may not materialize.

---

### Step 3: Tier 1 — eSUN Wholesale Outreach (Day 2-3)

**Objective**: Establish a direct wholesale relationship with eSUN at below-Amazon pricing.

**Contact method**: Email to eSUN wholesale department. Visit esun3dstore.com to find the current wholesale contact form or email address. The standard corporate email pattern is wholesale@esun3d.com (verify before sending).

**Talking points for email**:
- Production context: Etsy-based manufacturing, original design product line (ModRun)
- Current purchase behavior: Buying Amazon Prime (establishes you as already a customer)
- Volume trajectory: 10-20 kg/month now, scaling to 30-50 kg by Month 4, 100+ kg by Q4 2026 with multi-printer farm
- Multi-printer farm roadmap: Specifically mention the farm architecture — this signals you are a serious producer, not a hobbyist
- Long-term partnership: Framing as a "committed partner" rather than a one-time bulk buyer

**Email template**:

```
Subject: Wholesale Inquiry — ModRun Etsy Production, 15-30 kg/month PLA+

Hello eSUN Sales Team,

My name is [Name], and I'm launching ModRun — an original-design cable
management product line on Etsy (shop URL once live).

I'm currently purchasing eSUN PLA+ via Amazon (ASIN B0G2KSS613) and have
been impressed with AMS compatibility on my Bambu P1S fleet. I'd like to
explore a direct wholesale relationship as production scales.

CURRENT SITUATION:
- Printer: Bambu P1S (1 unit now, scaling to 5 printers by Q4 2026)
- Material: eSUN PLA+ exclusively (black, white, grey)
- Current volume: 10-15 kg/month (Amazon interim supply)
- Launch: April/May 2026 on Etsy

PROJECTED VOLUME:
- Month 2-3: 15-30 kg/month
- Month 4-6: 30-60 kg/month (second and third printers added)
- Q4 2026: 80-120 kg/month (5-printer farm, additional product lines)

I am specifically interested in:
1. Wholesale pricing for eSUN PLA+ (10kg cases, 15-30 cases/month)
2. Minimum order quantity for wholesale tier
3. Payment terms (net-30 preferred for established relationship)
4. Lead time guarantee for consistent production planning

I prefer eSUN for AMS reliability and color consistency, and I'd like to
build a long-term partnership rather than relying on Amazon availability.

Could you provide your current wholesale pricing sheet and terms? I'm
targeting a Month 2 commitment (June 2026).

Best regards,
[Name]
[Business name]
[Email]
[Phone]
[Etsy shop URL]
```

**Expected response time**: 2-3 weeks (eSUN wholesale is slower than Amazon)

**Follow-up cadence**:
- Day 10 (if no response): Resend email with "Following up" subject line
- Day 14 (if still no response): Call eSUN US customer service number (search eSUN USA phone number)
- Day 21 (if no response): Conclude eSUN wholesale is not accessible at current volume; proceed with Amazon Prime + Anycubic

**Success criteria for this step**:
- Response received with pricing below $13/kg
- MOQ at or below 20 kg
- Net-30 payment terms offered
- Lead time guarantee of 2-3 weeks

---

### Step 4: Tier 1 Alternative — Anycubic 50kg Pallet Pre-Qualification (Day 2-3)

**Objective**: Pre-qualify the Anycubic 50kg pallet supply chain before committing to a full order. This runs in parallel with eSUN outreach.

**Why Anycubic matters**: At $10.49/kg for a 50kg pallet, Anycubic offers the most accessible pallet-level pricing without requiring a formal wholesale account. The risk is AMS compatibility — some community reports of winding inconsistencies on Bambu AMS. A sample test before a 50kg order reduces this risk.

**Option A: Sample Order Path (Recommended if Anycubic is secondary)**

Email to support@anycubic.com or use the contact form at store.anycubic.com:

```
Subject: Sample Order Inquiry — PLA Bambu AMS Compatibility Test

Hello Anycubic,

I'm a small-batch Etsy seller (Bambu P1S/X1C) planning to place a 50kg
PLA order. Before committing, I'd like to test a 5-10 kg sample to
validate AMS winding consistency (I've seen some community reports of
feed issues on 8+ hour jobs).

Could you offer a 5-10 kg sample quantity at a reasonable price, with
expedited shipping? I'd like to confirm material quality and AMS
compatibility before committing to the full pallet.

Black PLA Basic preferred. What's available?

Best regards,
[Name]
[Contact info]
```

**Option B: Direct 50kg Order (If You Have Confidence in Anycubic Quality)**

```
Subject: 50kg PLA Pallet — Pre-Order Inquiry for May 2026

Hello Anycubic,

I'm interested in your 50kg PLA Basic pallet deal. I have a few questions
before placing the order:

1. Black PLA Basic availability: Is 50kg of black available now?
2. Spool format: Are these standard plastic spools or Refill cardboard format?
   (Cardboard Refill preferred for Bambu AMS — fewer winding issues reported)
3. Lead time: Shipping to [Your state]? Estimated delivery?
4. Recurring orders: If I place a monthly 50kg order, is there any
   partnership discount available?

Ready to order within 2 weeks pending your confirmation.

Best regards,
[Name]
[Contact info]
```

**Expected response time**: 2-5 days (Anycubic direct is faster than eSUN wholesale)

**Talking points if they respond with questions**:
- Volume trajectory: 50 kg/month now, scaling to 150 kg/month by Q4 2026 (5-printer farm)
- Recurring relationship: Emphasize you want a reliable monthly supply partner, not a one-time buyer
- Format preference: Ask specifically for cardboard "Refill" spool format for Anycubic PLA — reduces AMS tangling risk per phase-2-supplier-research.md findings
- Payment terms: Ask if net-30 is available for recurring orders (likely no at this scale, but worth asking)

**Success criteria for this step**:
- Pricing confirmed at $10.49/kg or below
- Black PLA Basic availability confirmed for 50kg
- Lead time: 3-7 days acceptable
- Spool format confirmed (Refill preferred)

---

### Step 5: Counter-Offer and Terms Negotiation (Week 2-3)

**Objective**: When supplier responds with initial terms, negotiate toward target rates using these leverage points.

**Leverage points by supplier**:

**eSUN leverage**:
- Multi-printer farm roadmap: "My current 1-printer setup is scaling to 5 printers by Q4 2026. At that scale, I'm projecting 100+ kg/month of eSUN PLA+. I'd like to lock in pricing now that works for both of us at that volume."
- Competitive alternative: "Anycubic has quoted me $10.49/kg for pallet quantities. I prefer eSUN for AMS reliability, but I need the pricing to be competitive."
- Long-term partnership: "I'm not looking for a one-time discount — I want a multi-year supply relationship as ModRun scales. That's worth more than a short-term margin hit."
- Payment terms: "If net-30 isn't possible yet, could we discuss a 10% upfront discount on 6-month prepayment?"

**Anycubic leverage**:
- At $10.49/kg (already a sale price), limited room to negotiate price further
- Focus leverage on: Refill spool format preference, shipping speed guarantee, and recurring order pricing if they offer a subscription model
- Alternative ask: "Can you guarantee this pricing for 6 monthly orders of 50kg?" (locks in price stability rather than discount)

**Counter-offer framework**:

| Supplier Quote | Your Counter | Your Walk-Away |
|---------------|-------------|----------------|
| eSUN at $14/kg (no wholesale discount) | "Can we agree on $12/kg for 20 kg/month, 6-month commitment?" | Walk away at >$13.50/kg; use Amazon Prime |
| eSUN at $12.50/kg | "I can commit to 20 kg/month for 6 months at $12.50. Can we add net-30 terms?" | Accept at $12.50 with any payment terms |
| Anycubic at $10.49/kg | "Can you confirm this pricing for recurring monthly orders?" | Accept if <$11/kg with lead time ≤7 days |
| Anycubic at $11.50/kg | "Your listing shows $10.49/kg — has that sale ended?" | Walk away if >$11/kg; use eSUN instead |

---

### Step 6: Contract and Commitment Formalization (Week 3-4)

**Objective**: Lock in agreed terms in writing before first wholesale order.

**What "in writing" means at this scale**: For small-volume wholesale relationships, a formal contract is rare. "In writing" means:
- Email thread confirming price, quantity, payment terms, and lead time guarantee
- Screenshot or PDF of the supplier's wholesale pricing page showing your agreed rate
- Order confirmation from the supplier's system

**Terms to confirm in writing**:
1. Price per kg (exact, with any volume tier thresholds)
2. Payment terms (credit card, net-30, or prepayment)
3. Lead time commitment (stated delivery window, not just "typically")
4. Return policy for defective spools (what is the process if 5% of a batch is defective?)
5. Price change notice (ask for 30-day advance notice before any price increase)

**For Anycubic** (simpler — order from their website):
- Retain all order confirmations and receipts
- Screenshot the pricing page at time of purchase
- Request an email confirmation with order details if not automatically sent

**For eSUN wholesale** (formal relationship):
- Request a written quote or wholesale agreement before first wire transfer
- Confirm all terms in a reply email: "To confirm our agreement: [price per kg], [MOQ], [lead time], [payment terms]. I'll place the first order by [date]. Please confirm."

---

### Step 7: Supplier Performance Monitoring and Decision Gates (Ongoing from Month 2)

**Objective**: Establish ongoing performance tracking to catch supplier quality degradation, price creep, or lead time violations before they impact customer fulfillment.

**Monthly supplier scorecard (update in Google Sheets)**:

| Metric | eSUN Target | Anycubic Target | Action if Below Target |
|--------|-------------|-----------------|------------------------|
| Price per kg | ≤$12.50 | ≤$11.00 | Renegotiate or switch primary |
| Lead time (days) | ≤14 | ≤7 | Issue warning; trigger backup order |
| AMS failure rate | <2% of spools | <5% of spools | Request replacement batch; escalate |
| Color consistency | Consistent lot-to-lot | Acceptable variation | Switch to eSUN for color-critical SKUs |
| Stock availability | Always in stock | ≥80% of color requests | Maintain 3-week buffer; pre-order |

**Decision gates for supplier switching**:

```
IF eSUN price rises above $14/kg AND Anycubic holds at ≤$11/kg:
  → Switch primary to Anycubic; use eSUN for PETG specialty only
  → Activate Polymaker inquiry for quality tier

IF Anycubic AMS failure rate exceeds 10% in any month:
  → Pause Anycubic orders; complete existing inventory
  → Accelerate Polymaker activation ($14.99/kg but superior quality)
  → Document failures and request credit from Anycubic

IF both Tier 1 suppliers unavailable (stock-out or price spike):
  → SUNLU as emergency backup ($12-14/kg via direct, 3-7 day lead)
  → Overture as PETG-quality backup ($17-19/kg PETG via Amazon)
  → Notify Etsy customers of extended processing time (update all listings to 3-5 business days)
```

**Quarterly supplier review (add to calendar)**:
- Review actual spend vs. projected for each supplier
- Compare current pricing against market (search Amazon for competing products every 90 days)
- Assess whether volume has crossed into next tier (and renegotiate if so)
- Evaluate whether supplier issues have accumulated to justify a switch

---

## Pricing Tiers and Volume Discounts

Based on pricing-tiers.csv and supplier-scorecard.csv data, here is the complete COGS reduction picture as volume scales:

### Filament Cost by Volume

| Monthly Volume | $/kg (eSUN) | $/kg (Anycubic) | Per Unit @75g (eSUN) | Per Unit @75g (Anycubic) |
|---------------|-------------|-----------------|----------------------|--------------------------|
| 0-10 kg (retail) | $14-15 | N/A | $1.06-1.13 | N/A |
| 10-20 kg (eSUN wholesale) | $12.50 | $10.49 | $0.94 | $0.79 |
| 20-50 kg | $11.50 | $10.49 | $0.86 | $0.79 |
| 50-100 kg | $11.00 | $10.49 | $0.83 | $0.79 |
| 100 kg+ | $10.50 | ~$9.90 est. | $0.79 | $0.74 |

### Impact on Per-SKU COGS and Margins

**Example: Basic Clip ($8.99 retail, 75g PLA)**

| Supply Scenario | Material | Pkg | Shipping | Etsy fee | Total COGS | Net Margin |
|----------------|----------|-----|----------|----------|-----------|-----------|
| Retail Amazon $15/kg | $1.13 | $0.10 | $4.10 | $0.27 | $5.60 | 37.7% |
| eSUN wholesale $12.50/kg | $0.94 | $0.05 | $3.85 | $0.27 | $5.11 | 43.2% |
| Anycubic $10.49/kg | $0.79 | $0.05 | $3.85 | $0.27 | $4.96 | 44.8% |
| Anycubic + Pirate Ship + bulk pkg | $0.79 | $0.05 | $3.85 | $0.27 | $4.96 | 44.8% |

Note: For the Economy tier at $8.99, shipping cost dominates COGS. The primary margin lever is to increase average order value (push 3-packs and kits) rather than chase marginal filament savings. A $22.99 3-pack has a 59.4% margin vs. 37.7% for a single clip — without any supplier discount.

**Example: Starter Bundle ($28.99 retail, estimated 250g PLA)**

| Supply Scenario | Material | Pkg | Shipping | Etsy fee | Total COGS | Net Margin |
|----------------|----------|-----|----------|----------|-----------|-----------|
| Retail Amazon $15/kg | $3.75 | $0.30 | $5.00 | $0.87 | $9.92 | 65.8% |
| eSUN wholesale $12.50/kg | $3.13 | $0.15 | $4.60 | $0.87 | $8.75 | 69.8% |
| Anycubic $10.49/kg | $2.62 | $0.15 | $4.60 | $0.87 | $8.24 | 71.6% |

At bundle level, 20% COGS reduction is fully achievable. The Starter Bundle margin improves from 65.8% to 71.6% with wholesale filament + Pirate Ship rates — a 5.8 percentage point improvement that represents $1.68 per bundle in additional profit.

### Volume Discount Strategy for Customers

The pricing negotiation with suppliers enables offering volume discounts to customers without sacrificing margins:

**Customer volume pricing targets** (from pricing-strategy.md):
- 3-pack bundle: 8-10% per-unit discount vs. single (drives AOV, improves fulfillment efficiency)
- Starter Bundle: Complete system at $28.99 vs. $25.98 if components purchased separately (13% savings, justifies margin with 65%+ bundle margin)
- Corporate bulk (20+ clips): 35-40% off retail — only viable at 500+/month volume where wholesale filament costs apply

---

## Risk Mitigation

### Risk 1: eSUN Stock-Out or Price Spike

**Probability**: Medium (Amazon inventory fluctuates seasonally)
**Impact**: High (production stoppage if no backup)
**Mitigation**:
- Maintain 3-week filament buffer (never let stock drop below this)
- Pre-qualify Anycubic before eSUN stock becomes critical
- Set up Amazon stock alert for ASIN B0G2KSS613 (use CamelCamelCamel or similar)
- SUNLU direct ($12-14/kg, 3-7 day lead) as emergency tertiary

### Risk 2: Anycubic AMS Compatibility Issues

**Probability**: Medium (community reports exist for some batches)
**Impact**: Medium (increased scrap rate, potential for mid-job failures)
**Mitigation**:
- Request cardboard Refill spool format specifically (fewer winding issues)
- Order sample 10 kg before committing to 50 kg pallet
- Run extended AMS test (8-hour overnight print with new batch) before committing to production
- If issues persist, escalate to eSUN primary and Polymaker quality tier

### Risk 3: Volume Doesn't Justify Wholesale Commitments

**Probability**: Medium (launch volume is uncertain)
**Impact**: Low (no firm commitments required until Month 2)
**Mitigation**:
- Do not sign any binding contracts in Week 1
- Path A (Amazon Prime) has no commitment requirement — use it if Month 1 is slow
- Anycubic 50kg is an online purchase with no formal contract — order only when demand justifies
- eSUN wholesale commitment is month-to-month unless you negotiate otherwise

### Risk 4: Lead Time Violations (Supply Gaps During Demand Spikes)

**Probability**: Low (established suppliers rarely have 2-3 week lead time failures)
**Impact**: High (order delays lead to bad reviews)
**Mitigation**:
- 3-week buffer stock prevents supplier lead time from affecting customer experience
- Track inventory level daily (2-minute count every morning)
- Place reorder when stock hits 2-week supply level (not 1-week — the lead time may eat into your buffer)
- Communicate proactively with Etsy customers if a delay is unavoidable

### Risk 5: Payment Terms Not Available at Launch Volume

**Probability**: High (net-30 is typically only for established wholesale accounts with proven payment history)
**Impact**: Low (credit card payment is fine at launch volume)
**Mitigation**:
- Accept credit card terms for first 3-6 months; build payment history
- Request net-30 terms after 6 months of consistent ordering
- Use a business credit card with a grace period for effective 20-30 day terms

---

## Supplier Selection Decision Tree

```
START: Need to select primary filament supplier

Q1: Is eSUN Amazon price currently ≤$13/kg?
  YES → eSUN Amazon is viable primary (no negotiation required)
    Q2: Is Anycubic pallet pricing ≤$11/kg?
      YES → Anycubic is strong secondary. 
            Use eSUN (primary) + Anycubic (secondary).
      NO → Use eSUN primary only. Evaluate SUNLU as backup.
  NO → eSUN retail is too expensive.
    Q3: Has eSUN wholesale responded with ≤$12.50/kg?
      YES → eSUN wholesale is primary. Order monthly.
      NO → Anycubic pallet is primary (lowest cost option).
            SUNLU as backup.

Q4: Is PETG demand growing (>20% of orders)?
  YES → Activate Overture PETG ($17-19/kg) as PETG primary.
         Do not use eSUN PETG unless price-competitive.
  NO → Use eSUN PLA+ for all current production.
       Revisit when PETG SKUs launch.

Q5: Is monthly volume exceeding 30 kg?
  YES → Contact Polymaker wholesale (quality tier upgrade).
         $14.99/kg is justified for premium SKUs at scale.
  NO → Defer Polymaker to Month 3-4.
```

---

## Contact Reference Table

| Supplier | Contact Path | Expected Response | Priority |
|----------|-------------|-------------------|---------|
| eSUN (Amazon) | ASIN B0G2KSS613 — direct purchase | Instant | Primary Month 1 |
| eSUN (Wholesale) | esun3dstore.com → Contact/Wholesale | 2-3 weeks | Primary Month 2+ |
| Anycubic | store.anycubic.com → Contact | 2-5 days | Secondary Month 1+ |
| Polymaker | us-wholesale.polymaker.com | 1-2 weeks | Month 3+ |
| Overture | Amazon direct or overture3d.com contact | 3-7 days | PETG demand trigger |
| SUNLU | sunlu.com direct store | 3-7 days | Emergency backup |

---

## Week 1 Action Checklist

Complete these 7 actions in Days 1-5 (parallel with Etsy setup):

- [ ] **Day 1**: Verify eSUN Amazon pricing and availability (5 min)
- [ ] **Day 1**: Verify Anycubic 50kg pallet pricing (5 min)
- [ ] **Day 1**: Decide Path A / B / C based on Month 1 projection (15 min)
- [ ] **Day 2**: Send eSUN wholesale inquiry email (if Path B or C) (15 min)
- [ ] **Day 2-3**: Contact Anycubic (sample inquiry or 50kg pre-qualification) (15 min)
- [ ] **Day 5**: Order packaging materials (Shop4Mailers poly mailers, packing tape, scale) (15 min)
- [ ] **Day 7**: Document all supplier contacts and expected response dates in tracking sheet

---

**Document Status**: Ready for Week 1 execution
**Version**: 2.0 (7-step sequence with full pricing tiers, decision trees, risk mitigation)
**Confidence Level**: High (supplier data from Session 544; pricing verified April 2026)
**Success timeline**: Primary supplier locked in by end of Month 2; 20% COGS reduction validated by Month 3
