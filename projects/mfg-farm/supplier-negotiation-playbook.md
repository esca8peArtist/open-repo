---
title: ModRun Phase 2 — Supplier Negotiation Playbook
date: 2026-04-28
status: ready-for-execution
confidence: high
related: supplier-scorecard.csv, phase-2-supplier-research.md, pricing-strategy.md
---

# ModRun Phase 2: Supplier Negotiation Playbook

**Status**: Ready to execute during Week 1 (parallel with Etsy setup)  
**Timeline**: Week 1-2 (concurrent with product launch prep)  
**Goal**: Lock in primary + backup filament suppliers before Month 2 scaling phase  
**Target outcome**: $0.77–$1.40/unit COGS reduction per supplier-scorecard.csv Session 544 findings  

---

## Executive Summary

This playbook provides the exact sequence, email templates, and negotiation targets to secure favorable volume pricing for ModRun production scaling. The data comes from supplier-scorecard.csv (Session 544 research), which ranked suppliers on price, reliability, lead time, and AMS compatibility.

**Key decision**: Choose between two paths based on Month 1 sales velocity:
- **Path A (eSUN primary)**: Lock in 10kg/month Amazon bundles at $11-13/kg immediately (no negotiation required; available now)
- **Path B (eSUN + Anycubic hedge)**: Establish 50kg/month mix with Anycubic backup for supply security

**Expected outcome**:
- Primary supplier: eSUN at $11-13/kg (commodity tier, high reliability)
- Backup supplier: Anycubic at $10.49/kg (accessible pallet pricing)
- Monthly material cost reduction: $0.77-1.40/unit at 75g per clip (vs. $1.10-1.40 retail pricing)
- Secured supply commitment: 6-month minimum, 2-week lead times

---

## Section 1: Target Suppliers & Ranking

### Supplier Tier 1: Primary Target

**eSUN (via Amazon + direct)**
- Reliability score: 9/10 (highest in commodity tier)
- Price: $11-13/kg (10kg bundles on Amazon)
- Lead time: 2-5 days (Prime) or 2-3 weeks (direct wholesale)
- AMS compatibility: Confirmed excellent (Bambu forum testing)
- Minimum order: None on Amazon; wholesale via direct contact
- **Why primary**: Best combination of price, reliability, and immediate availability
- **Risk**: Potential Amazon stock-outs; batch-to-batch color variation (manageable)

**Anycubic (direct)**
- Reliability score: 7/10 (slightly lower consistency documentation)
- Price: $10.49/kg (50kg pallet deals, verified April 2026)
- Lead time: 3-7 days (express shipping from China warehouse)
- AMS compatibility: Mixed reports (occasional tangles on poorly wound spools; Refill format better)
- Minimum order: No MOQ for bundle deals (purchase directly online)
- **Why backup**: Uniquely accessible pallet-level pricing without wholesale account
- **Risk**: Lower consistency; requires sample validation before 50kg order

### Supplier Tier 2: Secondary Targets (Month 3+)

**Polymaker (wholesale)**
- Reliability score: 9.5/10 (highest quality tier)
- Price: $14.99/kg (PolyLite, case of 10, $1,000 minimum order)
- AMS compatibility: Confirmed excellent; best moisture packaging
- **Timeline**: Activate Month 3-4 when volume justifies $1,000 MOQ
- **Use case**: Quality tier for premium product variants (if demand supports)

**Overture (Amazon + direct)**
- Reliability score: 8/10 (35% wholesale discount available)
- Price: $11-14/kg PLA; $17-19/kg PETG (Amazon or qualified wholesale)
- **Timeline**: Month 2-3 (if PETG demand grows)
- **Use case**: Primary PETG supplier for premium clip variants

---

## Section 2: Negotiation Sequence (Week 1 Execution)

### Phase 1: Research & Qualification (Day 1, ~1 hour)

**Objective**: Verify current pricing and confirm contact information

**Action items**:

1. **eSUN Amazon verification** (5 minutes)
   - Go to amazon.com → search "eSUN PLA 10kg case"
   - ASIN B0G2KSS613 (black PLA Basic): Check current price and Prime availability
   - ASIN B0G2KWC5XL (PLA+ mixed colors): Check current price and availability
   - Note: "Recommended bulk pricing: $11-13/kg" — verify actual current price
   - **Action**: If price >$15/kg, may need to accelerate Anycubic strategy

2. **Anycubic direct store verification** (10 minutes)
   - Go to store.anycubic.com/products/pla-basic-50-100kg-deals
   - Verify 50kg bundle pricing ($524.73 sale price = $10.49/kg per phase-2-supplier-research.md)
   - Check color availability (target: black, white, grey)
   - Note: Sale price may fluctuate; confirm before outreach
   - **Action**: If price changed >10%, adjust COGS targets in Section 2 below

3. **eSUN direct contact research** (10 minutes)
   - Visit esun3dstore.com
   - Locate "wholesale" or "bulk order" contact form
   - Note contact email for outreach (expected response: 2-3 weeks)
   - **Alternative**: eSUN North America sales rep contact (search "eSUN wholesale USA contact")

4. **Anycubic direct contact verification** (5 minutes)
   - Go to store.anycubic.com → Help/Contact
   - Note bulk order email (if not direct online) or confirm online checkout works

**Output**: Contact emails + current pricing snapshot + availability confirmation

---

### Phase 2: Strategy Decision (Day 1, ~20 minutes)

**Decision tree** (based on Month 1 sales projection):

```
IF Month 1 sales trajectory suggests 200+ units/month by Month 2:
  → Use Path A (eSUN primary, Anycubic backup)
  → Start negotiation with eSUN wholesale (longer lead time)
  → Pre-qualify Anycubic 50kg order for Month 2 supply bridge

IF Month 1 sales trajectory suggests 50-150 units/month:
  → Use Path B (eSUN Amazon bundles, immediate)
  → No wholesale negotiation required
  → Lock in Anycubic as Month 3 option

IF uncertain about Month 1 velocity:
  → Use Path B + prepare Path A playbook
  → Let first month's sales data drive Month 2 scaling decisions
  → Continue negotiation prep as parallel activity
```

**Recommendation for Week 1**: Execute Path B (low-risk, no commitment). 
Parallel preparation of Path A (wholesale eSUN contact) as option for Month 2.

---

### Phase 3: Tier 1 - eSUN Wholesale Outreach (Day 2-3)

**Objective**: Establish wholesale relationship if month 2+ demand projections support it

**Email template** (professional, realistic volume):

```
Subject: Wholesale Inquiry - 10-20kg/month PLA+ for Etsy Production

Hello eSUN Sales Team,

I'm launching a 3D-printed cable management product line on Etsy 
(ModRun brand) and am exploring wholesale filament partnerships for 
sustained production.

CURRENT SITUATION:
- Launch date: [Week of April 28, 2026]
- Initial inventory: 100 units printed (approx. 7.5 kg PLA+)
- Etsy shop: [Your shop URL once live]
- Projected volume: 10-20kg/month starting Month 2, scaling to 30-50kg/month 
  by Month 4 if sales trajectory supports

REQUIREMENTS:
- Material: eSUN PLA+ (Professional Plus), black/white/grey
- Format: 10kg case bundles preferred (Amazon is current interim supplier)
- Lead time: 2-3 week target for consistent supply
- Reliability: Bambu P1S/X1C AMS compatibility essential

VOLUME COMMITMENT:
- Month 1-2: Testing phase, variable volume (10-20kg)
- Month 3+: 30-50kg/month minimum if wholesale terms are favorable
- Growth potential: Scaling to 100+ kg/month by Q4 2026 (multi-printer farm)

QUESTION FOR YOUR TEAM:
What is your best pricing on eSUN PLA+ (10kg case quantity, 20+ cases/month) 
and what wholesale terms (MOQ, net payment terms, lead time guarantees) 
would you offer for a committed partner with demonstrated growth trajectory?

I'm currently buying Amazon Prime for immediate supply, but prefer a 
dedicated partnership with reliable lead times and volume pricing.

Please reply with:
1. Wholesale pricing per kg (for 10kg cases, 20+/month, 6-month commitment)
2. Minimum order quantity (MOQ) for wholesale rates
3. Payment terms (net-30, net-60, upfront, other)
4. Lead time guarantee
5. Contact person for ongoing orders

Timeline: Interested in locking this in by mid-May 2026 for Month 2 scaling.

Best regards,
[Your name]
[Email]
[Phone]
[Your business name / ModRun]
```

**Expected response time**: 2-3 weeks (eSUN direct wholesale typically slower than Amazon)

**Follow-up** (if no response in 10 days): Resend email + try calling (search for eSUN US customer service phone number)

**Success criteria**:
- Wholesale pricing: <$13/kg (or ≥ Amazon bulk pricing)
- MOQ: ≤20kg (approx. 2 orders to commitment)
- Payment terms: Net-30 or better
- Lead time: 2-3 weeks guaranteed

---

### Phase 4: Tier 1 Alternative - Anycubic 50kg Pallet Pre-Qualification (Day 2-3)

**Objective**: Pre-test Anycubic supply chain before committing to 50kg order

**Action 1: Sample Order** (Optional but recommended)

If you want to validate AMS compatibility and winding quality before 50kg commitment:

**Email template**:
```
Subject: Sample Order Inquiry - PLA Test for Bambu P1S/X1C

Hello Anycubic Sales,

I'm a small-batch 3D printer operator (Bambu P1S/X1C) launching a 
product line on Etsy, and I've seen your 50kg pallet deals.

Before committing to a full pallet order, I'd like to test 5-10kg 
to validate:
1. Winding consistency with Bambu AMS (occasional community reports 
   of feed issues)
2. Color consistency (black PLA Basic, if available)
3. Moisture packaging for storage

QUESTION:
Can I order a sample 5-10kg bundle with expedited shipping to test 
before placing a full 50kg order? What is your pricing for a 
sample quantity like this?

I'm planning to become a regular customer if the material meets 
my AMS compatibility requirements.

Best regards,
[Name]
```

**Expected outcome**: May offer 10kg sample at partial discount; otherwise, confirm 50kg pricing and order next

**Action 2: Confirm 50kg Order Path** (Without sample)

If you're confident in Anycubic quality, proceed directly to order confirmation:

**Email template**:
```
Subject: 50kg PLA Bundle Order - Pre-Commitment for May 2026

Hello Anycubic,

Following up on your 50kg PLA Basic bundles advertised at $10.49/kg 
(listing: store.anycubic.com/products/pla-basic-50-100kg-deals).

I'm planning a 50kg order for May 2026 delivery (or as soon as stock 
allows). Before ordering, I have a few clarifications:

1. Color availability: Do you have black PLA Basic in stock for a 
   50kg order? (Or mix of black/white/grey?)
2. Winding format: Are these standard spools (plastic) or Refill 
   format (cardboard inner)? Any preference noted?
3. Lead time: Shipping to [Your state]? Estimated delivery time 
   with standard express shipping?
4. Invoice/payment: Do you invoice for bulk orders, or is online 
   checkout the standard path?

I'm an Etsy seller scaling production, so this may become a 
recurring monthly order (50kg+). Interested in discussing a 
partnership if my volume grows.

Ready to order within the next 2 weeks. Please confirm availability 
and I'll proceed with payment.

Best regards,
[Name]
[Contact info]
```

**Expected response**: 2-5 days (Anycubic direct is faster than eSUN wholesale)

**Success criteria**:
- Price: $10.49/kg confirmed
- Color availability: Black confirmed for 50kg
- Lead time: 3-7 days acceptable for May delivery
- Format: Either standard or Refill acceptable

---

### Phase 5: Backup Plan - Polymaker Activation (Month 3 timing, NOT Week 1)

**Do not execute in Week 1.** Polymaker's $1,000 MOQ only makes sense at 50+ kg/month volume.

**Timeline**: Activate in Week 1 of Month 3 (if Month 2 sales hit 500+ units, indicating 30+ kg/month demand)

**Quick overview** (for reference):
- Website: us-wholesale.polymaker.com
- Pricing: ~$14.99/kg PolyLite PLA (case of 10, ~$1,000 order)
- Lead time: 3-7 days
- MOQ: $1,000 minimum
- Upside: Best quality tier, excellent AMS compatibility, vacuum-sealed packaging

---

## Section 3: Email Templates & Negotiation Scripts

### Template 1: Volume Commitment Email (eSUN Wholesale)

*Use this if Month 1 sales support >15kg/month commitment:*

```
Subject: ModRun Etsy — Wholesale Filament Partnership Opportunity

Hi eSUN Sales Team,

I'm the founder of ModRun, an original-design cable management product 
line launching on Etsy this week. We're manufacturing 3D-printed clips 
and rail systems in PLA+ and PETG.

Our Month 1 pilot is live on Etsy (shop URL). Based on initial orders, 
we're projecting 15-30kg/month of filament demand through Q2-Q3 2026, 
with potential to scale to 50+ kg/month by Q4 if growth continues.

Currently, we're buying 10kg Amazon bundles at your standard retail ($12-13/kg). 
We're exploring a wholesale partnership to lock in better pricing and 
ensure consistent supply for production scaling.

PROPOSAL:
- 6-month commitment: 15-30kg/month (starting June 2026)
- Material: eSUN PLA+ (black, white, grey mix)
- Pricing target: <$11/kg for case quantities (if possible)
- Lead time: 2-week guarantee
- Payment: Net-30 preferred

QUESTION FOR DISCUSSION:
What wholesale pricing can you offer for this volume profile and what are 
your standard terms? Also, are there any advantages to committing to 
50+ kg/month if we scale faster than projected?

I believe ModRun could become a 100+ kg/month partner within 12 months if 
our scaling plan executes well. Would like to build a strong relationship 
starting now.

Ready to discuss details and lock in terms ASAP.

Best regards,
[Your name]
[Email]
[Phone]
ModRun Design (Etsy seller)
```

**Negotiation talking points** (if they call back):
- "I'm locked in to Bambu printers (P1S/X1C) — AMS compatibility is essential. Can you confirm this?"
- "What's your best price if I pre-commit to 6 months at 20kg/month?"
- "Do you offer net-30 or net-60 terms for new partners at this volume?"
- "What happens if I need to scale to 50kg/month faster? Can we adjust the commitment?"

---

### Template 2: Volume & Payment Terms Negotiation (Anycubic)

*Use if ordering 50kg pallet:*

```
Subject: 50kg Monthly Orders - Payment Terms Negotiation

Hello Anycubic,

Thank you for confirming the 50kg PLA availability at $10.49/kg. 
Ready to proceed with the order.

Before finalizing, I want to discuss payment terms for a recurring 
monthly order (50kg/month starting May 2026):

CURRENT QUESTION:
Is there a discount available if I commit to recurring 50kg monthly 
orders (6-month minimum) versus a single one-time purchase?

For example:
- Single 50kg order: $524.73 ($10.49/kg)
- Recurring 50kg/month: Any volume discount available?

PAYMENT PREFERENCE:
For recurring orders, would you accept NET-30 or NET-60 payment terms 
(invoice sent at order placement, payment due 30/60 days), or is 
prepayment via credit card required?

If a partnership discount is possible (even 2-3% off recurring volume), 
that would justify a long-term relationship.

Looking forward to your response. Ready to place the May order once we 
confirm terms.

Best regards,
[Name]
```

**Expected outcome**: Likely no discount on already-discounted pallet price, but worth asking. Focus on locking in the $10.49/kg price for 6-month commitment.

---

## Section 4: Volume Tiers & COGS Impact

Based on pricing-tiers.csv and supplier-scorecard.csv, here's the per-unit material cost reduction:

### Current COGS (Retail filament, Amazon Prime)

| Volume Tier | Monthly Volume | $/kg | Per Unit (75g) | Total Monthly Material Cost |
|-------------|----------------|------|----------------|---------------------------|
| Startup | 7.5 kg | $15.00 | $1.13 | $112.50 |
| Month 1 | 10-15 kg | $14.00 | $1.05 | $140-210 |

### Target COGS (Wholesale eSUN or Anycubic)

| Volume Tier | Monthly Volume | $/kg (eSUN) | $/kg (Anycubic) | Per Unit (75g) | Monthly Savings |
|-------------|---|---|---|---|---|
| Path A: 10-20kg | 15 kg | $12.50 | — | $0.94 | $15-30/month |
| Path B: 20-50kg | 35 kg | $11.50 | $10.49 | $0.86 | $60-120/month |
| Path C: 50kg+ | 50 kg | $11.00 | $10.49 | $0.79 | $170-200/month |

### Impact on Unit COGS & Margin

**Example: Basic Clip at $8.99 retail**

| Scenario | Material | Packaging | Shipping | Etsy Fee | Total COGS | Net Margin |
|----------|----------|-----------|----------|----------|-----------|-----------|
| Current (retail filament) | $1.13 | $0.25 | $4.50 | $0.27 | $6.15 | 31.6% |
| Path A (eSUN $12.50/kg) | $0.94 | $0.25 | $4.50 | $0.27 | $5.96 | 33.7% |
| Path B (Anycubic $10.49/kg) | $0.79 | $0.25 | $4.50 | $0.27 | $5.81 | 35.4% |
| Path C (bulk 50kg+) | $0.79 | $0.25 | $3.75* | $0.27 | $5.06 | 43.7% |

*With Pirate Ship commercial rates optimized at scale*

**Key takeaway**: Supplier negotiation + volume pricing can improve unit margin by 4-12% (12-120 basis points). At 500+ units/month, this represents $40-600/month in retained margin.

---

## Section 5: 6-Month Commitment Strategy

Once you secure primary supplier agreement, here's the phased order schedule:

### Month 2 (May 2026)
- **eSUN path**: 10kg case (1-2 orders, via Amazon or wholesale if secured)
- **Anycubic path**: 50kg pallet order (if commitment locked, use 2 weeks printing)
- **Total**: 10-50kg depending on Month 1 sales velocity

### Month 3 (June 2026)
- **eSUN path**: 20kg (2× 10kg cases)
- **Anycubic path**: 50kg pallet (recurring)
- **Polymaker** (optional): If demand hits 30+ kg/month, contact for wholesale setup
- **Total**: 20-50kg

### Month 4 (July 2026)
- **eSUN path**: 30kg (3× 10kg cases) — reassess if demand growing
- **Anycubic path**: 50kg pallet (recurring)
- **Polymaker** (optional): 20-30kg if quality demand warrants
- **Total**: 30-100kg

### Month 5-6 (August-September 2026)
- **Scaling decision point**: If cumulative sales >500 units, activate multi-printer farm architecture
- **Supplier strategy**: Lock in Polymaker $1,000+ orders; expand eSUN relationship if supplier willing
- **New option**: Evaluate direct China imports if monthly volume >100kg (ROI analysis required)

---

## Section 6: Risk Mitigation & Backup Plans

### Risk 1: eSUN Stock-Outs

**Scenario**: eSUN Amazon bundles go out of stock or price spikes >$15/kg

**Mitigation**:
- Pre-commit to Anycubic 50kg pallet (dual sourcing)
- Set up email alerts on Amazon for ASIN availability
- Maintain 2-week inventory buffer (don't let stock drop below 10kg)
- Have SUNLU ($12-14/kg via direct) as tertiary option

### Risk 2: Anycubic Quality Issues (AMS tangling)

**Scenario**: 50kg Anycubic order has AMS compatibility issues (poor winding)

**Mitigation**:
- Request sample 5-10kg before full order (adds 5-7 days to timeline, but worth risk reduction)
- Request Refill format (cardboard spool) instead of plastic spools (fewer tangling issues per phase-2-supplier-research.md)
- Keep eSUN as primary if Anycubic fails validation
- Budget for 10% waste rate in first month (learning curve)

### Risk 3: Lead Time Delays

**Scenario**: Supplier has 2-week lead time; you get supply shortage if demand spikes

**Mitigation**:
- Establish 3-4 week supply buffer (maintain inventory = 4 weeks of production)
- Use Anycubic as emergency top-up (3-7 day lead time vs. eSUN 2-3 weeks)
- Set reorder triggers: Reorder new filament when stock drops below 2 weeks of consumption

### Risk 4: Volume Doesn't Scale as Projected

**Scenario**: Month 2 sales are only 5-8 units (not 50+), wholesale volume commitments not justified

**Mitigation**:
- Path B strategy avoids this: Use Amazon Prime, no contracts
- Reassess scaling in Month 2 before locking long-term commitment
- Keep Anycubic pallet option open (can be ordered on-demand, no MOQ)
- Focus on 6-month commitment with exit clause ("subject to sales volume milestone")

---

## Section 7: Expected Timeline & Success Metrics

### Week 1 Action Items

- [ ] Verify eSUN Amazon pricing and availability (5 min)
- [ ] Verify Anycubic 50kg pricing and colors (5 min)
- [ ] Decide Path A vs. Path B strategy (10 min)
- [ ] Send eSUN wholesale inquiry (Path A) OR confirm Anycubic sample order (10 min)
- [ ] Document supplier contacts and response expectations (5 min)

### Week 2-3 Milestones

- [ ] eSUN wholesale response (expected 2-3 weeks, may arrive Month 2)
- [ ] Anycubic sample order received (if sample requested) — validate quality
- [ ] Anycubic 50kg order placed (if pursuing Path B)

### Month 2 Validation

- [ ] Supplier orders received and tested
- [ ] First 100 units printed using negotiated-supplier filament
- [ ] AMS compatibility confirmed (no feed issues on multi-hour jobs)
- [ ] Cost reduction validated (compare actual COGS to projections)
- [ ] Sales velocity assessed (decide if 6-month commitment justified)

### Success Metrics

**Primary goal achieved** if:
- Filament locked in at ≤$12/kg (eSUN wholesale) OR ≤$10.49/kg (Anycubic)
- Lead time guaranteed at 2-3 weeks
- Monthly supply secured for 6-month minimum
- No AMS compatibility issues identified
- Per-unit COGS reduced by $0.40-0.60 vs. retail (margin improvement)

---

## Appendix: Supplier Contact Information (Updated April 2026)

| Supplier | Primary Contact | Email | Website | Notes |
|----------|-----------------|-------|---------|-------|
| eSUN (Amazon) | N/A (automated) | N/A | amazon.com | ASIN: B0G2KSS613, B0G2KWC5XL |
| eSUN (Wholesale) | Sales dept | wholesale@esun3d.com (est.) | esun3dstore.com | 2-3 week response expected |
| Anycubic (Direct) | Sales dept | support@anycubic.com (est.) | store.anycubic.com | 2-5 day response typical |
| Polymaker | Wholesale team | sales@polymaker.com (est.) | us-wholesale.polymaker.com | Activate Month 3+ |
| SUNLU | Direct store | support@sunlu.com (est.) | sunlu.com | Backup option |

*Note: Email addresses are estimated based on standard corporate patterns. Verify on official websites before sending.*

---

**Document Status**: Ready for Week 1 execution (parallel with Etsy setup)  
**Confidence Level**: High (supplier data from Session 544)  
**Success timeline**: Commitments locked by end of Month 2; COGS reduction validated by Month 3
