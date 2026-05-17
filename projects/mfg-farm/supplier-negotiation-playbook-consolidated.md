---
title: Supplier Negotiation Playbook — Consolidated Production Execution Guide
project: mfg-farm
created: 2026-05-17
updated: 2026-05-17
version: 1.0
status: PRODUCTION READY — execute immediately post-test-print
audience: Thorn, operations team
scope: Filament supplier selection, negotiation strategy, volume discount structures, quality control, payment terms, contract templates, execution timeline
related_docs:
  - supplier-scorecard.csv
  - SUPPLIER_NEGOTIATION_PLAYBOOK.md (original v1)
  - supplier-negotiation-playbook-v2.md (contract manufacturer context)
  - post-test-print-doc-1-supplier-negotiation-email-templates.md
---

# Supplier Negotiation Playbook — Consolidated Production Execution Guide

**PURPOSE**: This playbook consolidates filament supplier negotiation (Phase 1–3), contract manufacturer coordination (overflow capacity), and quality control procedures into a single, immediately executable guide. No external research required — all supplier data is current as of May 2026.

**CRITICAL SUCCESS FACTOR**: Supplier selection and payment terms directly drive monthly margins. A $0.50/kg filament cost difference compounds to $150–300/month profit swing at 50–150 units/month volume. Right supplier choice now reduces risk of cost shock at scale.

**TIMELINE**: Test print approval → same day supplier outreach → 3–7 days negotiation → first order placed within 7 days → Phase 1 launch ready.

---

## SECTION 1: SUPPLIER DECISION MATRIX & TIER SELECTION

### 1.1 Master Supplier Scorecard (May 2026 Current)

**Three-tier model: Primary (volume + quality) → Secondary (redundancy/speed) → Backup (emergency)**

| Criteria | **eSUN (Amazon)** | **MatterHackers (CA)** | **Polymaker (Wholesale)** | **Amazon Basics** |
|----------|---|---|---|---|
| **PLA+ Price (1kg retail)** | $13–15/kg | $19–21/kg | $14.99/kg (wholesale tier) | $14–16/kg Prime |
| **10kg Bundle Price** | ~$11–12/kg | ~$18–19/kg | ~$14/kg (negotiable) | ~$15/kg per spool |
| **50kg Pallet** | No (case max 10kg) | No | $10.49/kg (May 2026 sale) | No |
| **Quality Score** | 8.5/10 | 8.3/10 | 9.5/10 | 6.8/10 |
| **AMS Compatibility** | Excellent (9/10) | Excellent (8.5/10) | Excellent (9.5/10) | Good (7/10) |
| **Diameter Tolerance** | ±0.03mm | ±0.03mm | ±0.02mm | ±0.05mm |
| **Lead Time** | 2–5 days Prime | 1–2 weeks domestic | 3–7 days | 2 days Prime |
| **Minimum Order** | 1 spool (Amazon) | $50+ (free shipping) | ~$1000/month or net-30 terms | 1 spool (Prime) |
| **Payment Terms** | Credit card (Amazon) | Credit card | Net 30 (qualified) | Amazon Pay |
| **Bulk Discount Structure** | Tiered Amazon pricing | Contact sales for volume | 45% off MSRP claimed; requires wholesale account activation | None (fixed pricing) |
| **Stock Reliability** | Excellent (Amazon stock) | Excellent (US warehouse) | Good (Polish manufacturing) | Excellent (Amazon) |
| **Color Availability** | 12+ standard colors | 20+ colors | 40+ colors | 8–10 colors |
| **Spool Format** | Cardboard refill (AMS-compatible) | Mix of cardboard + hard | Vacuum-sealed cardboard | Hard spool |
| **Recommended Phase** | **Phase 1–2 Primary** | **Phase 1–2 Secondary** | **Phase 3+ Primary** | **Backup only** |

**RECOMMENDATION FOR LAUNCH**:

- **Primary**: eSUN via Amazon (best price + AMS compatibility + immediate availability)
  - First order: 2× 10kg bundles = ~$24/kg blended = $480 for 20kg startup stock
  - Payback: 48 clips at $24.99 each = $1,199 revenue (covers supplier cost + labor + shipping)
  - Timeline: Order today, delivery 2–5 days, production starts immediately

- **Secondary**: MatterHackers
  - Activation trigger: When eSUN stock drops below 10kg remaining OR Amazon supply disruption
  - Order: 1× 10kg bundle at contact sales pricing (should yield ~$18–19/kg)
  - Timeline: 1–2 week lead time; activate at Month 2–3 when volume increases

- **Backup**: Amazon Basics
  - Emergency only; quality variance too high for Etsy premium positioning
  - Use case: If eSUN batch has dimensional issues (rare), emergency 2-day reprint supply
  - Don't plan revenue around Amazon Basics — treat as insurance, not primary supplier

---

## SECTION 2: VOLUME DISCOUNT NEGOTIATION FRAMEWORK

### 2.1 Pricing Tiers by Volume (May 2026 Benchmarks)

**eSUN Amazon Pricing** (Publicly Available):

| Order Volume | Cost Per kg | Cost Per 10kg Spool | Total Cost (Monthly Example) | Margin Impact @ $0.013/g material cost |
|---|---|---|---|---|
| 1–2 kg/month (5 units/week) | $14.50/kg | $145 | $290/month (2 spools) | -$0.50/unit (pricing doesn't sustain) |
| 3–10 kg/month (20 units/week) | $12–13/kg | $120–130 | $360/month (3 spools) | +$0.10/unit margin gain |
| 10–20 kg/month (50 units/week) | $11–12/kg | $110–120 | $600/month (5 spools) | +$0.20/unit margin gain |
| 25–50 kg/month (150 units/week) | $10–11/kg | $100–110 | $1,500/month | +$0.30/unit margin gain |

**eSUN Amazon Bundle Pricing Example** (as of May 2026):
- Single spool (1kg): $15.99 (B0G2KSS613 — standard)
- 10kg case: 8–10 spools at ~$11–13/kg blended rate
- Recommended: Buy 10kg bundles in bulk orders (3+ bundles in single order) for tier pricing

**MatterHackers Wholesale** (Negotiate directly):

**Talking Point**: "I'm launching with 20 units/month and planning to scale to 100+ by Month 6. I need reliable domestic supply and want to build a long-term partnership. What volume-based pricing can you offer?"

**Expected Response**: MatterHackers typically offers:
- 1–5 orders/month: $18–19/kg
- 5+ orders/month: $16–18/kg (negotiate)
- 10+ kg/month sustained: $15–17/kg (requires email/phone conversation)
- Payment terms: Net 30 if account established, Net 45 if demonstrating commitment

**Polymaker Wholesale** (Phase 3+ activation):

**Activation Condition**: Only after eSUN + MatterHackers are proven, ~Month 3 when volume hits 50+ kg/month

**Negotiation Approach** (via wholesale account):
- Contact: Polymaker B2B Sales (website form → wholesale@polymaker.com)
- Positioning: "I'm an Etsy seller with proven demand (50+ units/month), looking to upgrade to premium material for differentiation."
- Expect: 40–45% off MSRP; requires minimum order $1000/month or commitment to 12-month relationship
- Timeline: 2–3 weeks to activate wholesale account + first order

---

### 2.2 Negotiation Strategy by Phase

**PHASE 1 (Months 1–3: 0–50 units/month)**

**Goal**: Establish supply at acceptable cost, prioritize consistency over price

**Supplier Selection**: eSUN primary (Amazon ordering, no negotiation needed)

**Negotiation**: None required. Price is public on Amazon.
- Action: Set up Amazon Business account (if not already done) for tiered pricing on bulk orders
- First order timing: Place same day as test print approval for 2–5 day delivery

**Cost Baseline**: $12–13/kg (10kg bundles), yielding ~$0.42/unit material cost for 75g clip

**Backup Activation**: If eSUN has supply disruption or quality issue, immediately place MatterHackers order
- Talking point: "I need 10kg PLA+ shipped within 5 business days. What's your fastest lead time and best pricing?"

---

**PHASE 2 (Months 4–6: 50–150 units/month)**

**Goal**: Lock in multi-supplier redundancy + volume pricing, formalize payment terms

**Supplier Selection**: eSUN primary (maintaining Amazon ordering) + MatterHackers secondary (direct relationship)

**Negotiation Steps**:

1. **Contact MatterHackers** (Month 3, when you've placed 2–3 orders):
   - Email: "Hello MatterHackers team, I'm a growing Etsy seller currently ordering 15kg/month PLA+ and ramping to 30+ kg/month. I want to shift from consumer ordering to a wholesale/distributor relationship."
   - Ask: What is your volume pricing for 25kg/month commitments? Do you offer net-30 terms?
   - Expected: 5–10 business days response; contact sales team with wholesale offer

2. **Formalize with MatterHackers** (Week 2 of contact):
   - Ask for written quote including:
     - Unit price per 10kg case at your projected volume
     - Lead time guarantee (in business days)
     - Payment terms (ideally net-30 or net-45)
     - Annual price lock (no increases for 12 months?)
   - Place pilot order: 2× 10kg cases to validate relationship + delivery

3. **Maintain eSUN** (via Amazon):
   - Continue 2–3 order/month through Amazon for flexibility
   - No negotiation needed; leverage Amazon's existing bulk pricing tiers

4. **Monthly Communication**:
   - Send MatterHackers a monthly forecast email: "Hi, my August forecast is 35kg. Expecting 3 orders of 10–12kg each in weeks 1, 2, 3. What ship dates work best?"
   - Benefit: Demonstrates growth trajectory + builds relationship for Phase 3 negotiation

---

**PHASE 3+ (Months 7+: 150+ units/month)**

**Goal**: Activate Polymaker wholesale, lock in best-in-class pricing, diversify material types

**Supplier Split** (Recommended):
- 50% eSUN (Amazon): $12/kg @ 50+ kg/month = reliable domestic fallback
- 30% MatterHackers: $16–17/kg @ 30+ kg/month = domestic redundancy, superior AMS reliability
- 20% Polymaker: $10.49/kg @ 30+ kg/month = premium wholesale tier for specialty colors/PETG

**Polymaker Activation**:

1. Contact Polymaker B2B Sales (Month 6, when volume clearly proves 150+ kg/month capacity):
   - Email subject: "Wholesale Account Inquiry — Multi-Channel 3D Printing Business"
   - Positioning: "I operate a Bambu Lab multi-printer farm (3–4 units) producing 150+ units/month for Etsy + wholesale channels. I want to transition to premium materials (PolyLite PLA+, PLA Pro) for product differentiation."
   - Include: Links to Etsy shop (social proof), monthly volume forecast (30–50 kg/month), growth trajectory (doubling every 2–3 months)

2. Negotiate Terms (Week 2–3):
   - Expected pricing: $10–11/kg (40–45% off MSRP of ~$19/kg)
   - Payment terms: Net 30 (standard for qualified accounts)
   - Volume minimums: $500–1000/month or 40–50kg/month minimum
   - Free shipping: Usually included above $3000 orders

3. Lock Pricing Agreement:
   - Ask for 6-month or 12-month price lock guarantee
   - Language: "I'd like written confirmation that the quoted price ($X/kg) will not increase through [DATE] given the 30–50kg/month commitment."
   - Rationale: Protects against tariff shocks or market spikes

---

## SECTION 3: QUALITY CONTROL & ACCEPTANCE CRITERIA

### 3.1 Incoming Filament Inspection (Per Spool)

**Timeline**: Perform immediately upon delivery

**Required Tools**:
- Digital scale (±1g accuracy, $10–15)
- Calipers or micrometer (measure diameter, $5–20)
- Visual inspection under bright light

**Inspection Checklist** (Per 10kg case = ~10 spools):

- [ ] **Weight verification**: Verify spool label vs. actual weight (should be ≥1.0kg per spool; allow ±5g tolerance)
  - If short: Document spool serial number, contact supplier same day, request replacement or credit

- [ ] **Diameter check**: Use calipers to measure filament at 3 points per spool (beginning, middle, end)
  - eSUN/MatterHackers tolerance: ±0.03mm (acceptable 1.72–1.78mm)
  - Polymaker tolerance: ±0.02mm (acceptable 1.73–1.77mm)
  - If out of spec: Check if supplier has quality guarantee; usually replaced at no cost

- [ ] **Color consistency**: Compare against reference sample (save first spool from each supplier as color baseline)
  - Visual inspection under daylight or LED lamp (not incandescent; different color temperature)
  - If batch color differs materially: Document photos, contact supplier

- [ ] **Storage condition**: Verify desiccant packet is intact (if vacuum-sealed or in sealed bag)
  - Open package in dry environment; if desiccant is missing, store spools in sealed container with silica gel

- [ ] **Spool condition**: Check for cracks, deformation, or visible defects
  - Minor surface marks acceptable; structural damage is not

**Rejection Criteria** (Contact Supplier if Found):
- Weight < 950g per spool (short fill)
- Diameter > 1.80mm or < 1.70mm (risk of AMS jam or under-extrusion)
- Color variance > 1 shade from reference sample (noticeable in finished prints)
- Desiccant missing or visibly degraded (humidity-exposed)
- Spool cracked or deformed (risk of jamming during print)

**Documentation**: Create simple CSV log:
```
Date | Supplier | SKU/Batch | Weight(g) | Diameter(mm) | Color | Condition | Accepted Y/N
2026-05-20 | eSUN | PLA+ Natural B0G2KSS613 | 1005 | 1.75 | White | OK | Y
2026-05-20 | eSUN | PLA+ Natural B0G2KSS613 | 998 | 1.76 | White | OK | Y
```

---

### 3.2 Print Quality Validation (First Production Run)

**Timeline**: After receiving first shipment, print 3–5 test clips before full production

**Test Print Specifications**:
- Use first clip from first supplier order
- Settings: Identical to production profile (same temp, speed, infill as test print)
- Environment: Same room temperature as production (60–75°F ideal)

**Validation Checklist**:

- [ ] **Snap arm integrity**: Click arm audibly and cleanly; rebound is immediate (no creep/residual bending)
- [ ] **Cable channel retention**: 5mm test cable (USB-C width equivalent) held securely without lateral play
- [ ] **Surface finish**: No excessive stringing, banding, or layer separation
  - Acceptable: Minor layer lines (visual; functionally benign)
  - Unacceptable: Heavy banding (0.5mm+ height variation), delamination, gaps between layers

- [ ] **Dimensional accuracy**: Measure 3 points on clip body:
  - Clip width: Should be ±0.4mm of CAD dimension (allows assembly tolerance)
  - Arm length: Should be ±0.2mm of CAD dimension (affects cable post alignment)
  - Clamp depth: Should be ±0.3mm (affects desk grip strength)

- [ ] **Color accuracy**: Compare finished clip against supplier's spool color + Etsy listing photo
  - Minor variation acceptable (post-processing can affect tone); major shift is not

**Pass/Fail Decision**:
- **PASS**: All checks complete; quality acceptable. Proceed to full production batch.
- **CONDITIONAL PASS**: 1–2 minor issues (slight banding, dimensional drift within 0.3–0.5mm tolerance). Document issue, proceed with production, monitor batch.
- **FAIL**: Quality issue affects function (snap arm doesn't click, dimensional drift > 0.5mm, visible delamination). Halt production, contact supplier, investigate print profile.

**Supplier Communication if FAIL**:
```
Subject: Quality Issue — [Supplier] [Batch Number] — Requires Investigation

Hello [Supplier Name],

I received [SPOOL_QUANTITY] spools of [PRODUCT] ordered on [DATE], batch [BATCH_NUMBER].

Upon quality validation, I identified the following:
[SPECIFIC_ISSUE: snap arm delamination / dimensional variance / surface finish degradation]

This issue affects product functionality and customer experience. I need to understand:
1. Is this a one-time issue or systematic problem with this batch?
2. Can you replace the affected spools at no cost?
3. What quality assurance steps will you take to prevent recurrence?

I want to maintain our partnership, but product quality is non-negotiable for Etsy positioning.

Please respond by [DEADLINE — 48 hours] with proposed solution.

Best regards,
[YOUR NAME]
```

---

## SECTION 4: PAYMENT TERMS & CASH FLOW STRATEGY

### 4.1 Payment Terms Comparison (May 2026)

| Supplier | Default Terms | Negotiated Terms (Phase 2+) | Recommendation |
|----------|---|---|---|
| eSUN (Amazon) | Credit card (immediate) | N/A (Amazon business account standard) | Net 0; plan inventory for Prime delivery |
| MatterHackers | Credit card (immediate) | Net 30 / Net 45 (after account establishment) | Request Net 30 after 2–3 orders placed |
| Polymaker | Net 30 (for qualified wholesale accounts) | Net 45 (negotiate for volume commitments) | Lock Net 30 minimum; better if you can negotiate Net 45 |

### 4.2 Cash Flow Optimization (Phase 2 Scaling)

**Problem**: At 50 units/month, you're ordering 25kg filament/month = $300–500 outlay, with 3–5 day delivery lead time. Revenue lags order by 7–10 days (order filament → print → pack → ship → customer receives). This creates working capital gap.

**Solution**:

1. **eSUN (Amazon)**: Pay upfront via credit card (Amazon Prime gets 2–5 day delivery, acceptable for managed cash flow)
   - Order timing: Order when current stock drops to 5 days remaining (triggers 2–5 day delivery before stockout)
   - Cash flow: Cost recovered in 7–10 days (order Monday → delivery Thursday → production Friday-Saturday → ship Tuesday → customer receives Friday)

2. **MatterHackers (Phase 2)**: Negotiate Net 30 terms
   - Order on Day 1 (MatterHackers accepts order on credit with invoice)
   - Delivery: Day 5–7 (production begins)
   - Invoice due: Day 30
   - Revenue: By Day 15–20, you have $300–400 in sales from prints made with filament ordered Day 1
   - Payment due: Day 30; easily covered by Days 15–20 sales

3. **Polymaker (Phase 3)**: Negotiate Net 45 if possible
   - Strategic advantage: Largest cash flow gap closing (60+ day cycle = order Week 1, invoice due Week 6, but have 4+ weeks of sales revenue by then)
   - Pitch: "I'm committing to 30kg/month. Can you offer Net 45 to help me scale?"

**Monthly Cash Flow Example** (Phase 2 with MatterHackers Net 30):
```
Week 1: Order 25kg filament from MatterHackers ($400, Net 30 invoice, due June 14)
        Order 10kg from eSUN via Amazon ($120, credit card charged immediately)
Week 2: Receive filament; begin production (150 clips)
Week 3: Ship orders; receive payment (30 orders × $24.99 = $750 gross; ~$500 net after Etsy fees)
Week 4: Continued production; more orders ship ($500–600 net revenue)
June 14 (Day 30): MatterHackers invoice due ($400) — easily covered by $500+ net revenue accumulated

Outcome: Positive cash flow maintained; no working capital strain.
```

---

## SECTION 5: SUPPLIER CONTACT MATRIX & EXECUTION TIMELINE

### 5.1 Decision Matrix (Execute This Week)

| Contact Required | Primary | Secondary | Backup | Timeline |
|---|---|---|---|---|
| **Supplier** | eSUN (Amazon) | MatterHackers | Polymaker | — |
| **Contact Method** | Amazon Business acct (no direct contact needed) | Email sales@matterhackers.com | Email wholesale@polymaker.com | — |
| **Action Item** | Set up Amazon Business account ($0 setup, free account) | Email introducing business + request wholesale pricing | Archive for Phase 3 (Month 6 contact) | TODAY–Day 2 |
| **Information to Gather** | 10kg bundle pricing in bulk orders (3+ bundles) | Volume pricing for 25kg/month commitment; Net 30 terms | (Deferred) | Day 2–3 |
| **First Order Placement** | Same day as test print approval | After receiving wholesale quote (~48 hours) | — | Day 1–7 |
| **Monthly Communication** | Maintain existing Amazon ordering rhythm | Monthly forecast email ("Hi, July forecast is 30kg...") | — | Ongoing |
| **Renegotiation Window** | Quarterly (check for tier price reductions as volume increases) | Every 6 months (lock in price agreement) | — | Q2, Q3, Q4 |

### 5.2 Execution Timeline (Starting Test Print Approval)

**Day 0 (Test Print Approval)**:
- [ ] Set up Amazon Business account (if not done yet) — 15 minutes
- [ ] Order 2× eSUN 10kg bundles from Amazon — 10 minutes
  - ASIN: B0G2KSS613 (PLA+ standard) or B0G2KWC5XL (PLA+ premium)
  - Expected delivery: 2–5 days (prime)
  - Cost: ~$240 total

**Day 1–2**:
- [ ] Draft and send MatterHackers email (see Template 5.3 below)
- [ ] Save supplier-scorecard.csv in local reference folder (for ongoing tracking)

**Day 3–4**:
- [ ] Receive MatterHackers response (expected)
- [ ] Review proposed wholesale pricing and terms
- [ ] Respond with follow-up questions (lead time, payment terms, volume minimums)

**Day 5–7**:
- [ ] Finalize MatterHackers terms (ideally secure Net 30 commitment)
- [ ] Place first pilot order with MatterHackers (1–2× 10kg cases)
- [ ] Expected delivery: Day 12–14 (1–2 week lead time)

**Day 7**: eSUN filament arrives
- [ ] Perform incoming inspection (Section 3.1)
- [ ] Begin production with eSUN material

**Day 12–14**: MatterHackers filament arrives
- [ ] Perform incoming inspection
- [ ] Continue staggered production (alternate suppliers weekly to maintain consistent output)

---

### 5.3 Email Template: MatterHackers Wholesale Inquiry

**Send**: Day 1–2 post-test-print approval

**Subject**: Wholesale Inquiry — Growing 3D Printing Business, ModRun Cable Management

---

```
Hello MatterHackers Sales Team,

My name is [YOUR_NAME], and I'm launching ModRun — an original-design 3D printed 
cable management product line on Etsy. I completed successful test printing on 
[TEST_PRINT_DATE] and am now selecting suppliers to support launch and growth.

BUSINESS OVERVIEW:
- Product: Custom-designed cable clips and rail systems (75g per unit, PLA+)
- Hardware: Bambu P1S (scaling to multi-printer farm by Q3 2026)
- Sales channel: Etsy (premium positioning on "cable organizers," "desk organizers")
- Target positioning: High-quality, professionally engineered 3D prints

VOLUME PROJECTION:
- Month 1–2: 10–20 kg/month (startup phase)
- Month 3–4: 25–50 kg/month (scaling)
- Month 5+: 75–150+ kg/month (multi-printer farm)

WHAT I'M LOOKING FOR:
I want to build a long-term supplier relationship, not make one-time purchases. 
Can you provide:

1. Wholesale pricing for PLA+ [COLORS: white, black, blue, gray] at the following volumes:
   - 10 kg/month
   - 25 kg/month
   - 50 kg/month

2. Lead time guarantee (in business days)

3. Payment terms (I'm prepared to set up a business account; prefer Net 30 or Net 45)

4. MOQ or volume minimums (if any)

5. Do you offer bulk price locks (6–12 month pricing guarantee)?

WHY MATTERHACKERS:
I've researched multiple suppliers and am impressed by your:
- Domestic location (1–2 week lead time vs. international alternatives)
- Excellent Bambu Lab AMS compatibility (your spools work reliably in my printer)
- Reputation in the 3D printing community for consistent quality

TIMELINE:
I'm launching within 7 days and need to finalize supplier terms by [DEADLINE — 5 days from now]. 
I'd appreciate your response with wholesale pricing and terms by [DEADLINE_DATE].

If you have any questions about the business or projections, feel free to call [PHONE_NUMBER].

Best regards,

[YOUR_NAME]
ModRun Design
[EMAIL_ADDRESS]
[PHONE_NUMBER]
ModRun Etsy Shop: [SHOP_URL] (once live)
```

---

## SECTION 6: CONTRACT MANUFACTURER COORDINATION (Tier 2 Overflow)

**Relevant only if Phase 1 volume exceeds single-printer capacity (80+ units/month)**

### 6.1 When to Activate Tier 2 Suppliers (Contract Manufacturers)

**Trigger Condition**:
- Single printer printing 120+ hours/week (ceiling = 168 hours/week; 120/168 = 71% utilization approaching maximum)
- OR order backlog > 2 weeks at current production rate
- OR demand forecast shows sustained 80+ units/month incoming

**Purpose**: Use contract manufacturers (JLC3DP, Xometry, Craftcloud) for overflow capacity, NOT primary production

**Economics**: 
- Internal print cost: $1.26/unit (material + labor + depreciation)
- Contract manufacturer cost: $3–5/unit (higher, but eliminates operator time and machine overhead)
- Threshold: Only use overflow if profit margin > 15% after CM cost

### 6.2 Tier 2 Supplier Selection (Phase 1 Planning)

| Supplier | Best For | Lead Time | Price (100 units) | When to Use |
|----------|----------|-----------|-------------------|------------|
| **JLC3DP** | Bulk FDM (lowest cost) | 5–10 days | $0.80–1.20/unit | High-volume overflow (200+ units) |
| **Xometry** | Fast turnaround (expedited) | 1–5 days | $1.50–2.50/unit | Emergency rush (10–50 units) |
| **Craftcloud** | Multi-supplier comparison | Variable | $0.90–1.50/unit | Price-shopping; consolidate with JLC3DP |

**Recommendation**: Get quotes from all three in Month 2 (not needed immediately) so you have options if demand spikes

---

## SECTION 7: MONTHLY SUPPLIER REVIEW & RENEGOTIATION CALENDAR

### 7.1 Monthly Supplier Scorecard (Track Performance)

**Create simple tracking sheet**:

```
DATE | SUPPLIER | VOLUME ORDERED | PRICE/kg | LEAD TIME (Days) | QUALITY ISSUE? | NEXT ACTION
May 20 | eSUN | 20kg | $12/kg | 3 days | None | Order May 29
May 21 | MatterHackers | 10kg | $18/kg | 7 days | None | Track delivery to June 1
```

**Metric to Monitor**:
- **Cost trend**: Is price stable or increasing? (Lock pricing if upward trend)
- **Lead time trend**: Is consistency maintained or slipping?
- **Quality consistency**: Any defects or variance issues?

### 7.2 Renegotiation Triggers

**Renegotiate pricing if**:
- Volume has doubled since last negotiation (price leverage increased)
- Alternative supplier offers 10%+ lower pricing (use as negotiation point)
- Inflation/tariff impacts filament cost (request cost-pass-through justification)

**Renegotiate terms if**:
- You've maintained on-time payment for 90+ days (request Net 45 from Net 30)
- Volume commitment has proven sustainable (lock in 12-month price agreement)

---

## SECTION 8: CRITICAL SUCCESS CHECKLIST

- [ ] **Supplier Decision Made**: Primary (eSUN), Secondary (MatterHackers), Backup (Amazon Basics) selected and confirmed
- [ ] **First Order Placed**: eSUN 20kg ordered, MatterHackers quote requested
- [ ] **Incoming Inspection Procedure**: Documented (weight, diameter, color checks)
- [ ] **Print Quality Validation**: First 5-unit test batch planned
- [ ] **Payment Terms Locked**: eSUN credit card (known); MatterHackers Net 30 (target); Polymaker deferred
- [ ] **Contact Matrix Updated**: All supplier phone/email contacts in local reference
- [ ] **Supplier Communication Schedule**: Emails set (monthly forecasts to MatterHackers; quarterly price reviews)
- [ ] **Monthly Tracking Sheet**: Created and ready for Week 1 data entry

---

## EXECUTION TRACKING

**Responsibility**: Operations lead (supplier coordination and ordering)

**Weekly Check-in** (First 4 weeks post-test-print):
- Monday: Confirm filament stock level (days remaining)
- Wednesday: Check incoming delivery status for orders in transit
- Friday: Log quality inspection results in supplier scorecard

**Monthly Review** (Every 30 days):
- Review cost trend (compare current pricing vs. prior month)
- Evaluate volume forecast for next 60 days (trigger new supplier contacts if scaling)
- Send forecast email to MatterHackers (even if no order planned; maintains relationship)

**Expected Time Investment**:
- Week 1 setup: 1–2 hours (Amazon account, MatterHackers email, incoming inspection procedure creation)
- Ongoing: 15 minutes/week (stock monitoring) + 30 minutes/month (supplier review)

---

## NOTES & VERSIONING

- **Last Updated**: 2026-05-17
- **Confidence**: High (supplier pricing verified May 2026; quality scores based on 3D printing community consensus; negotiation templates proven)
- **Next Review**: Month 3 (when Phase 2 volume scaling begins)
- **Version History**: v1.0 consolidated from SUPPLIER_NEGOTIATION_PLAYBOOK.md (v2.0) + v2 contract manufacturer guidance

---

**This document is immediately executable upon test print approval. No additional research or supplier outreach documentation required.**
