---
title: ModRun Supplier Negotiation Email Templates
date: 2026-05-05
status: pre-staging-ready
scope: 5 negotiation email templates with fill-in variables
related: supplier-scorecard.csv, supplier-negotiation-playbook.md, pricing-strategy.md
---

# ModRun Supplier Negotiation Email Templates

## Overview

Five ready-to-customize email templates for negotiating filament supply, payment terms, quality agreements, and repeat order incentives. All templates include {{FILL-IN VARIABLES}} for specific details. Copy, customize, and send after test print confirms success.

**Execution flow**:
1. Update all {{variables}} with your specifics
2. Day 1 after test print success: Send Template 1 (Initial Contact) to top 3 suppliers
3. Day 3-5: Template 2 (Volume Pricing Negotiation) if quotes are too high
4. Day 7-10: Template 3 (Payment Terms) upon agreement on pricing
5. Day 10-14: Template 4 (Quality Agreement) before first bulk order ships
6. Month 2+: Template 5 (Repeat Order Incentive) to lock in preferred supplier

---

## Template 1: Initial Contact — Establish Wholesale Relationship

**Subject Line**: Wholesale Inquiry — ModRun Cable Clips, {{VOLUME_PROJECTION}} kg/month, Original Design

**Best For**: First approach to a new supplier. Establishes you as a serious operator with growth plans, not a one-time bulk buyer.

**Send To**: wholesale@{{SUPPLIER_NAME}}.com or sales contact from their website

**When to Use**: Day 1-2 after test print confirms success

**Key Variables to Customize**:
- {{SUPPLIER_NAME}}: eSUN, Anycubic, Polymaker, Overture, etc.
- {{ESTIMATED_MONTHLY_VOLUME}}: Based on your printer capacity and market validation (recommend 15-30 kg/month for realistic startup)
- {{TIMELINE}}: Month 2 (June 2026) or your actual target
- {{DESIGN_SPECS_ATTACHMENT}}: Attach STL file, CadQuery spec sheet, or material requirements doc
- {{ETSY_SHOP_URL}}: Your live Etsy shop URL (link to your ModRun listing once published)
- {{PRINTER_FLEET}}: Bambu P1S (or X1C, or current setup)

---

**Email Body**:

```
Hello {{SUPPLIER_NAME}} Sales Team,

My name is {{YOUR_NAME}}, and I'm launching ModRun — an original-design
cable management product line on Etsy ({{ETSY_SHOP_URL}}).

I'm currently sourcing {{MATERIAL_TYPE}} PLA+ via {{CURRENT_SUPPLIER}} and
am impressed with your {{POSITIVE_CHARACTERISTIC}} (AMS compatibility /
pricing / reliability / etc.). I'd like to explore a direct wholesale
relationship as production scales.

CURRENT SITUATION:
- Printer: {{PRINTER_FLEET}}
- Primary Material: {{MATERIAL_TYPE}} PLA+ (colors: {{COLOR_LIST}})
- Current Volume: {{CURRENT_VOLUME}} kg/month (temporary retail supply)
- Launch: {{TIMELINE}} on Etsy with original design product line

GROWTH TRAJECTORY:
- Months 2-3: {{VOLUME_PROJECTION}} kg/month (current printer + one additional)
- Months 4-6: {{VOLUME_MID}} kg/month (multi-printer farm, 3-4 active units)
- Q4 2026 and beyond: {{VOLUME_PROJECTION_Q4}} kg/month (5-8 printer farm,
  multiple product lines)

WHAT I NEED:
1. Wholesale pricing for {{MATERIAL_TYPE}} PLA+ in {{VOLUME_PROJECTION}} kg/month
   quantities ({{SPOOL_TYPE}}: {{SPOOL_SIZE}} cases/month)
2. Minimum order quantity to qualify for wholesale pricing
3. Payment terms (preferably net-30, open to negotiation)
4. Lead time guarantee for consistent production planning
5. Color options available ({{COLOR_LIST}})
6. Spool format (bulk cases, cardboard refill format, or other)

PARTNERSHIP VISION:
I'm not looking for a one-time discount — I want to build a long-term supply
relationship with a partner who can grow with my business. ModRun is designed
for Bambu AMS compatibility and precision tolerances, so material quality is
critical to customer satisfaction and repeat orders.

TIMELINE:
I'm targeting a {{TIMELINE}} commitment. I need your current wholesale pricing
sheet and terms by {{RESPONSE_DEADLINE}}.

Could you provide your wholesale pricing for the quantities and materials I've
outlined? I'm prepared to place the first order within 2 weeks of agreement.

Best regards,

{{YOUR_NAME}}
{{BUSINESS_NAME}} — ModRun Cable Management
{{EMAIL_ADDRESS}}
{{PHONE_NUMBER}}
{{ETSY_SHOP_URL}}
```

---

**Expected Response Time**: 2-5 business days (Anycubic, Overture); 2-3 weeks (eSUN wholesale, Polymaker)

**Follow-Up Cadence**:
- Day 10 (if no response): Resend with subject "Following up: Wholesale inquiry"
- Day 14 (if still no response): Call supplier customer service or try alternative contact email
- Day 21 (if no response): Conclude supplier is unresponsive; move to backup supplier list

**What to Look For in Their Response**:
- ✓ Price below {{TARGET_PRICE_PER_KG}}/kg (your walk-away threshold)
- ✓ MOQ at or below {{VOLUME_PROJECTION}} kg
- ✓ Net-30 or better payment terms
- ✓ Lead time guarantee (3-14 days stated clearly)
- ✓ Color availability for your primary colors

---

## Template 2: Volume Pricing Negotiation — Counter-Offer to Initial Quote

**Subject Line**: Re: Wholesale Inquiry — Volume Commitment Discussion

**Best For**: When supplier responds with a quote that's above your target. Negotiates pricing down using your volume projection and competitive alternatives as leverage.

**When to Use**: Day 3-5 after receiving supplier's initial quote (if quote is higher than target)

**Key Variables to Customize**:
- {{SUPPLIER_QUOTE}}: The price they quoted (e.g., "$14.50/kg at 20 kg minimum")
- {{TARGET_PRICE}}: Your target (e.g., "$12.00/kg")
- {{VOLUME_COMMITMENT}}: Number of kg you'll commit to (e.g., "20 kg/month for 6 months = 120 kg total")
- {{GROWTH_TIMELINE}}: When you'll hit higher volume tiers (e.g., "100+ kg/month by Q4 2026")
- {{COMPETITIVE_QUOTE}}: Price from alternative supplier (if you have one; e.g., "Anycubic at $10.49/kg")
- {{PARTNERSHIP_VALUE}}: Long-term benefit to supplier (e.g., "This relationship scales to 500+ kg/month within 18 months")

---

**Email Body**:

```
Hello {{SUPPLIER_NAME}},

Thank you for your quote of {{SUPPLIER_QUOTE}}. I appreciate the quick response.

I want to move forward with {{SUPPLIER_NAME}} — your material quality and
AMS compatibility are exactly what ModRun needs. However, I'd like to
discuss pricing to make sure we align on volume tiers and long-term value.

YOUR QUOTE vs. MY TARGETS:
- Your quote: {{SUPPLIER_QUOTE}}
- My target for commitment: {{TARGET_PRICE}}/kg
- Volume I'm committing to: {{VOLUME_COMMITMENT}}

MARKET CONTEXT:
I've also contacted {{COMPETITIVE_SUPPLIER}} and received a quote of
{{COMPETITIVE_QUOTE}}. I prefer {{SUPPLIER_NAME}} because {{REASON}} (AMS
reliability, color consistency, supplier reputation, etc.), but the pricing
needs to be competitive.

MY PROPOSAL:
I will commit to {{VOLUME_COMMITMENT}} ({{MONTHLY_KG}} kg/month for 6 months)
if you can meet me at {{TARGET_PRICE}}/kg. This gives you:

1. Predictable demand: You know you'll ship {{MONTHLY_KG}} kg to ModRun
   every month for the next 6 months
2. Growth potential: When I scale to multi-printer farm, I'll hit
   {{GROWTH_VOLUME}} kg/month by {{GROWTH_TIMELINE}}
3. Long-term partnership: I'm looking to scale to {{LONGTERM_VOLUME}} kg/month
   within 18 months — a partner who locks in pricing now will have first
   access to this volume

TIER STRUCTURE OPTION:
If you can't move to {{TARGET_PRICE}} immediately, could we structure a tier:
- Month 1-2: {{MONTH_1_PRICE}}/kg (your quote)
- Month 3-4: {{MONTH_3_PRICE}}/kg (middle point)
- Month 5-6+: {{MONTH_5_PRICE}}/kg (my target) with auto-renewal if volume holds

TIMELINE:
I need to finalize supply by {{DECISION_DEADLINE}}, so I can launch production
at {{TIMELINE}}.

Can we work toward {{TARGET_PRICE}}/kg with a 6-month commitment? If not,
what's the lowest price you can guarantee for 120 kg over 6 months?

Looking forward to building this relationship.

Best regards,
{{YOUR_NAME}}
```

---

**Negotiation Thresholds** (Walk-Away Points):
- ✓ Accept if they meet your {{TARGET_PRICE}}/kg
- ✓ Accept if they offer a tiered discount that reaches {{TARGET_PRICE}} by month 3-4
- ✗ Walk away if they cannot go below {{WALK_AWAY_PRICE}}/kg (typically 5% above target)

**Alternative Counter-Offers** (if they refuse to lower price):
1. "Can you offer net-30 terms to offset the higher per-kg cost?" (Reduces cash flow friction)
2. "Can you guarantee this pricing locks in for 6 months, even if market rates rise?" (Price stability)
3. "Can you provide a 5-10% discount on orders above {{HIGHER_VOLUME_TIER}}?" (Volume tiering)

---

## Template 3: Payment Terms Negotiation — Cash Flow Optimization

**Subject Line**: Re: Wholesale Agreement — Payment Terms Discussion

**Best For**: After agreeing on unit price, negotiate payment terms (net-30, advance deposit, etc.) to align with your cash flow and order timing.

**When to Use**: Day 7-10, once pricing is locked in, before first order

**Key Variables to Customize**:
- {{AGREED_PRICE}}: The price you negotiated (e.g., "$12.00/kg")
- {{MONTHLY_ORDER_VALUE}}: Typical monthly spend (e.g., "{{MONTHLY_KG}} kg × {{AGREED_PRICE}}/kg = ${{MONTHLY_SPEND}}")
- {{CASH_FLOW_ISSUE}}: Your constraint (e.g., "I need sales to complete before paying for materials" or "I can provide 50% upfront")
- {{PROPOSED_TERMS}}: Your ask (e.g., "Net-30 upon delivery," "50% advance, 50% on delivery," "Prepay for 3-month supply upfront")
- {{ETSY_PAYMENT_TIMING}}: When you receive customer payments (usually 2-3 days after order ships)

---

**Email Body**:

```
Hello {{SUPPLIER_NAME}},

I'm pleased that we've agreed on {{AGREED_PRICE}}/kg for {{VOLUME_COMMITMENT}}.
I'm ready to place the first order.

Before I do, I'd like to align on payment terms that work for both of us.

MY SITUATION:
- Typical monthly order: {{MONTHLY_KG}} kg ≈ {{MONTHLY_SPEND}}/month
- Cash flow: I operate as a made-to-order service (customers pay via Etsy,
  I pay suppliers from sales revenue)
- Etsy payment cycle: Customers pay when they order; I receive funds 2-3
  days after shipment

MY PROPOSAL:
I'd like to request {{PROPOSED_TERMS}}:

Option A (Net-30):
- I order {{MONTHLY_KG}} kg on the 1st of each month
- You invoice on delivery
- I pay within 30 days of invoice
- This aligns my cash inflow (customer payment) with my outflow (supplier payment)

Option B (Advance Deposit + Balance on Delivery):
- I provide 50% deposit upfront to secure the order
- You ship the order
- I pay the remaining 50% within 10 days of delivery
- This reduces your risk while letting me finance from sales

Option C (Prepay Discount):
- I prepay for {{QUARTER_VOLUME}} kg (3-month supply) upfront
- You discount by {{PREPAY_DISCOUNT}}% off the agreed price
- This gives you early cash and me better pricing

Which of these works for {{SUPPLIER_NAME}}? I'm flexible and want to find
terms that are sustainable for both of us long-term.

Once we confirm payment terms, I'll place the first {{MONTHLY_KG}} kg order
immediately.

Best regards,
{{YOUR_NAME}}
```

---

**Payment Terms Hierarchy** (Best to Acceptable):
1. Net-30 (you pay 30 days after invoice; best for cash flow)
2. 50% advance / 50% on delivery (balanced risk)
3. Net-15 (half of net-30; acceptable for established suppliers)
4. Prepay for discount (slightly negative but acceptable for certainty)
5. COD (collect on delivery; acceptable for larger suppliers)

**Avoid**:
- ✗ Prepay with no discount (money sits with supplier)
- ✗ Net-60 or longer (too much working capital tied up)

---

## Template 4: Quality Agreement and Specifications — Define Standards Before First Batch

**Subject Line**: Quality Standards and Inspection Protocol

**Best For**: Before the first bulk order ships, establish clear quality expectations, defect handling, and tolerance specs so there are no surprises.

**When to Use**: Day 10-14, right before placing the first 20+ kg order

**Key Variables to Customize**:
- {{MATERIAL_SPEC}}: Material and properties (e.g., "eSUN PLA+ 1.75mm ± 0.03mm diameter, natural drying before use")
- {{INSPECTION_PROTOCOL}}: Your quality check (e.g., "Visual inspection for brittleness, diameter consistency, color uniformity")
- {{DEFECT_THRESHOLD}}: Maximum acceptable defect rate (e.g., "No more than 3% of spools exhibiting winding inconsistency")
- {{REWORK_PROCESS}}: What happens if defects occur (e.g., "Full replacement of defective batch at no cost, or credit toward next order")
- {{STORAGE_REQUIREMENTS}}: How you'll store material (e.g., "Sealed bags in climate-controlled storage")
- {{LEAD_TIME_SLA}}: Your lead time requirement (e.g., "Guaranteed delivery within 10 business days of order")

---

**Email Body**:

```
Hello {{SUPPLIER_NAME}},

I'm excited to place the first order of {{FIRST_ORDER_QTY}} kg. Before I do,
I want to confirm we're aligned on quality standards and inspection protocol
so the partnership runs smoothly.

MATERIAL SPECIFICATIONS:
I need {{MATERIAL_SPEC}}:
- Diameter tolerance: {{DIAMETER_SPEC}}
- Moisture content: {{MOISTURE_SPEC}} (or industry standard if not critical)
- Color batch consistency: Acceptable variance of {{COLOR_VARIANCE}}
- Spool format: {{SPOOL_FORMAT}} (please confirm)
- Packaging: {{PACKAGING_REQ}} (vacuum-sealed, moisture-proof if applicable)

DELIVERY & HANDLING:
- Delivery window: {{LEAD_TIME_SLA}} after order placement
- Shipping carrier: {{PREFERRED_CARRIER}} (or your preference)
- Signature required on delivery: {{YES_NO}}

QUALITY & INSPECTION PROTOCOL:
I will inspect every batch upon arrival for:
1. {{INSPECTION_CHECK_1}} (visual consistency, winding tension, etc.)
2. {{INSPECTION_CHECK_2}}
3. {{INSPECTION_CHECK_3}}

If I identify defects exceeding {{DEFECT_THRESHOLD}}, I will:
1. Take photos of defective spools
2. Contact you within 2 business days with documentation
3. Expect either: full replacement batch shipped at no cost, or {{CREDIT_PERCENTAGE}}% credit toward next order

REWORK & RETURN PROCESS:
In the case of defective spools:
- I will return photos (no need to ship damaged goods unless you request)
- You will replace at no cost, or issue credit
- Timeline for replacement: Within {{REPLACEMENT_DAYS}} business days

LEAD TIME & REORDER:
- Standard monthly reorder: {{MONTHLY_KG}} kg
- Lead time commitment: Guaranteed shipment within {{LEAD_TIME_SLA}}, or
  I receive {{PENALTY}} off that order (or you suggest alternative)
- Any price increases: 30-day notice required before implementation

DOCUMENTATION:
Please include the following with each shipment:
- Packing slip with material specs, batch date, and spool count
- Certificate of material properties (if available)
- Your contact info for any defect claims

COMMUNICATION:
For any issues, questions, or concerns, I'll reach out to {{PRIMARY_CONTACT}}
at {{CONTACT_EMAIL_OR_PHONE}}. I expect a response within 24 business hours
for urgent issues (defect discovery, missed lead time, etc.).

Does this align with {{SUPPLIER_NAME}}'s standard process? If any of these
terms need adjustment, please let me know before I place the order.

I'm committed to a long-term partnership with clear expectations on both sides.

Best regards,
{{YOUR_NAME}}
```

---

**Critical Quality Specs to Confirm**:
- ✓ Diameter tolerance (industry standard is ±0.05mm; negotiate for ±0.03mm if critical)
- ✓ Color consistency (acceptable batch-to-batch variation)
- ✓ Spool format (cardboard refill is best for AMS; confirm compatibility)
- ✓ Moisture packaging (vacuum-sealed preferred for PLA+)
- ✓ Lead time guarantee (written, not estimated)
- ✓ Defect replacement process (cost and timeline)

---

## Template 5: Repeat Order Incentive — Lock in Preferred Supplier at Scale

**Subject Line**: Volume Growth & Preferred Supplier Agreement (Month 2+)

**Best For**: After 2-3 months of successful orders, lock in a preferred supplier relationship with volume bonuses to incentivize priority treatment and best pricing as you scale.

**When to Use**: Month 2-3, after you've proven reliable payment and order patterns

**Key Variables to Customize**:
- {{PROVEN_VOLUME}}: Total kg you've ordered in first 2-3 months (e.g., "60 kg")
- {{UPCOMING_VOLUME}}: Projected 6-month volume (e.g., "100+ kg/month, 600 kg total")
- {{BONUS_THRESHOLD}}: Volume at which you hit a bonus (e.g., "500 kg within 6 months")
- {{BONUS_INCENTIVE}}: What you're offering (e.g., "Automatic 10% discount on all orders above 100 kg/month")
- {{PRIORITY_TREATMENT}}: What you need (e.g., "Priority fulfillment, dedicated account contact, 7-day lead time guarantee")
- {{EXCLUSIVE_COMMITMENT}}: What you're offering (e.g., "Commit to {{SUPPLIER_NAME}} as primary supplier through Q4 2026, no competing orders")

---

**Email Body**:

```
Hello {{SUPPLIER_NAME}},

Over the past {{MONTHS_WORKING}} months, we've successfully completed {{ORDER_COUNT}}
orders totaling {{PROVEN_VOLUME}} kg of {{MATERIAL_TYPE}}. I'm very happy with
the quality, lead times, and our working relationship.

I'm reaching out to propose a formal preferred supplier agreement as ModRun
scales.

HERE'S WHERE WE ARE NOW:
- Monthly volume: {{CURRENT_MONTHLY}} kg/month
- Payment history: {{PAYMENT_RECORD}} (100% on-time)
- Quality satisfaction: {{SATISFACTION_LEVEL}} ({{DEFECT_RATE}}% defect rate)
- Communication: Excellent responsiveness and problem-solving

HERE'S WHERE WE'RE GOING:
- Months 3-4: {{MID_VOLUME}} kg/month (second printer coming online)
- Months 5-6: {{HIGHER_VOLUME}} kg/month (multi-printer farm)
- Q4 2026+: {{Q4_VOLUME}} kg/month (5-8 printer farm, multiple product lines)

Total projected volume in next 12 months: {{ANNUAL_PROJECTION}} kg (vs. {{PROVEN_VOLUME}} in first 3 months)

MY PROPOSAL: PREFERRED SUPPLIER AGREEMENT

I want to commit {{SUPPLIER_NAME}} as my primary {{MATERIAL_TYPE}} supplier through
Q4 2026. In exchange, I'm asking for:

1. PRIORITY PRICING:
   - Current: {{CURRENT_PRICE}}/kg at {{CURRENT_VOLUME}} kg/month
   - Tier 1 (50+ kg/month): {{TIER_1_PRICE}}/kg
   - Tier 2 (100+ kg/month): {{TIER_2_PRICE}}/kg (automatic when you hit this)
   - Locked-in rates: No price increases without 30-day notice

2. PRIORITY FULFILLMENT:
   - Dedicated account contact: {{PRIMARY_CONTACT_NAME}} or similar
   - Lead time guarantee: 7-10 business days on all orders
   - Priority in allocation during shortages

3. VOLUME BONUS INCENTIVE:
   - If I reach {{BONUS_THRESHOLD}} kg by {{BONUS_DATE}}, you provide {{BONUS_INCENTIVE}}
     (e.g., 10% retroactive discount on all orders that quarter, or automatic upgrade
     to next tier pricing)

WHAT I'M COMMITTING TO:
- {{EXCLUSIVE_COMMITMENT}} (ModRun commits {{SUPPLIER_NAME}} as primary supplier)
- Consistent {{MONTHLY_PROJECTION}} kg/month minimum orders
- Payment within {{PAYMENT_TERMS}} (currently {{CURRENT_TERMS}})
- Long-term partnership: I don't shop around if you deliver on lead time and quality
- Growth notification: I'll give you 30-day notice before scaling to each new volume tier

MUTUAL BENEFIT:
For you: Predictable revenue of {{ANNUAL_PROJECTION}} kg over 12 months, with growth
visibility into a 5-8 printer farm operation. This is a supplier relationship that
scales.

For me: Price certainty, priority treatment, and a partner who helps ModRun scale
without supply chain risk.

TIMELINE:
I'd like to finalize this agreement by {{AGREEMENT_DATE}}. In exchange, I'm committing
to increasing orders from {{CURRENT_MONTHLY}} kg/month to {{MID_VOLUME}} kg/month starting
{{NEXT_MONTH}}.

Can we schedule a brief call or email exchange to align on these terms? I'm flexible
on the specific percentages and pricing tiers — I want this to work for both of us
long-term.

Looking forward to scaling together.

Best regards,
{{YOUR_NAME}}
ModRun
{{EMAIL_ADDRESS}}
{{PHONE_NUMBER}}
```

---

**Bonus Incentive Examples** (Customize Based on Your Situation):
1. **Percentage discount at volume tier**: "At 500+ kg total, you receive 10% retroactive discount on all previous orders that quarter"
2. **Tiered pricing ladder**: "Every 100 kg ordered unlocks a $0.25/kg reduction on future orders"
3. **Exclusive color priority**: "As a preferred supplier, you get first access to new custom colors or limited-edition materials"
4. **Extended payment terms at scale**: "At 500+ kg, terms upgrade from net-30 to net-45"
5. **Reserved inventory**: "Your top 3 colors are reserved for ModRun; no allocation rationing during shortages"

**Lock-In Language**:
Use language like "preferred supplier," "primary supplier," and "long-term partnership" — this signals commitment without a formal legal contract. Most small suppliers will respond positively to clear growth visibility.

---

## Summary: Execution Checklist

After test print success, execute in this order:

**Week 1**:
- [ ] Day 1: Customize Template 1 (Initial Contact) with your variables
- [ ] Day 1: Send Template 1 to top 3 suppliers
- [ ] Day 3: Monitor for responses; start phone calls if no email response

**Week 2**:
- [ ] Day 3-5: If quote too high, customize and send Template 2 (Negotiation) to top target
- [ ] Day 7-10: Upon pricing agreement, customize and send Template 3 (Payment Terms)
- [ ] Day 10-14: Finalize payment terms; send Template 4 (Quality Agreement) before first bulk order

**Month 2-3**:
- [ ] After 2-3 successful orders: Customize and send Template 5 (Repeat Order Incentive) to preferred supplier

---

## Fill-In Variables Reference Table

| Variable | Example Value | Notes |
|----------|---|---|
| {{SUPPLIER_NAME}} | eSUN | Name of supplier |
| {{YOUR_NAME}} | John Smith | Your name |
| {{BUSINESS_NAME}} | ModRun Design | Shop name |
| {{ESTIMATED_MONTHLY_VOLUME}} | 20 | kg/month projected |
| {{TIMELINE}} | June 2026 | When you'll place first order |
| {{DESIGN_SPECS_ATTACHMENT}} | ModRun_cable_clip_specs.stl | File you attach |
| {{ETSY_SHOP_URL}} | https://www.etsy.com/shop/ModRunDesign | Your shop once live |
| {{MATERIAL_TYPE}} | PLA+ | Material name |
| {{CURRENT_SUPPLIER}} | Amazon Prime | Where you currently buy |
| {{PRINTER_FLEET}} | Bambu P1S | Your printer model |
| {{COLOR_LIST}} | Black, White, Grey | Colors you need |
| {{CURRENT_VOLUME}} | 10 | Your current monthly kg |
| {{VOLUME_MID}} | 40 | Projected 4-6 month volume |
| {{VOLUME_PROJECTION_Q4}} | 100 | Projected Q4 volume |
| {{TARGET_PRICE_PER_KG}} | $12.00 | Your walk-away price |
| {{VOLUME_COMMITMENT}} | 20 kg/month for 6 months | Total commitment |
| {{MONTHLY_KG}} | 20 | kg per month |
| {{WALK_AWAY_PRICE}} | $13.00 | Price above which you don't negotiate |
| {{RESPONSE_DEADLINE}} | May 15, 2026 | When you need their response |
| {{TARGET_PRICE}} | $12.00 | Your ideal price |
| {{SUPPLIER_QUOTE}} | $14.50/kg | What they initially quoted |
| {{COMPETITIVE_SUPPLIER}} | Anycubic | Alternative supplier |
| {{COMPETITIVE_QUOTE}} | $10.49/kg | Their price |
| {{REASON}} | AMS compatibility | Why you prefer this supplier |
| {{GROWTH_VOLUME}} | 100 | kg/month at full scale |
| {{GROWTH_TIMELINE}} | Q4 2026 | When you'll hit that volume |
| {{LONGTERM_VOLUME}} | 500 | Ultimate monthly volume goal |
| {{MONTH_1_PRICE}} | $14.50/kg | Initial month pricing |
| {{MONTH_3_PRICE}} | $13.25/kg | 3-month pricing |
| {{MONTH_5_PRICE}} | $12.00/kg | Target month pricing |
| {{DECISION_DEADLINE}} | May 20, 2026 | When you decide |
| {{MONTHLY_SPEND}} | $240 | {{MONTHLY_KG}} × {{AGREED_PRICE}} |
| {{AGREED_PRICE}} | $12.00/kg | Price you negotiated |
| {{CASH_FLOW_ISSUE}} | Sales cycle lag | Your constraint |
| {{PROPOSED_TERMS}} | Net-30 | Your payment ask |
| {{QUARTER_VOLUME}} | 60 | 3-month supply (25% discount) |
| {{PREPAY_DISCOUNT}} | 5% | Discount for advance payment |
| {{FIRST_ORDER_QTY}} | 20 | First bulk order in kg |
| {{MATERIAL_SPEC}} | eSUN PLA+ 1.75mm ±0.03mm | Exact material spec |
| {{DIAMETER_SPEC}} | ±0.03mm | Tolerance |
| {{MOISTURE_SPEC}} | <0.2% | Moisture content target |
| {{COLOR_VARIANCE}} | ±2 Delta E | Color tolerance |
| {{SPOOL_FORMAT}} | Cardboard refill | Type of spool |
| {{PACKAGING_REQ}} | Vacuum-sealed | How to package |
| {{PREFERRED_CARRIER}} | FedEx | Shipping preference |
| {{YES_NO}} | Yes | Signature required |
| {{INSPECTION_CHECK_1}} | Visual winding consistency | First inspection point |
| {{INSPECTION_CHECK_2}} | Diameter spot checks | Second point |
| {{INSPECTION_CHECK_3}} | Color batch consistency | Third point |
| {{DEFECT_THRESHOLD}} | 3% | Max defects acceptable |
| {{CREDIT_PERCENTAGE}} | 100 | % refund for defects |
| {{REPLACEMENT_DAYS}} | 10 | Days to replace defects |
| {{PENALTY}} | ${{MONTHLY_SPEND}} × 10% | Cost of missing lead time |
| {{PRIMARY_CONTACT}} | John Smith, Sales | Supplier contact name |
| {{CONTACT_EMAIL_OR_PHONE}} | john@supplier.com | Contact info |
| {{MONTHS_WORKING}} | 3 | How long you've been ordering |
| {{ORDER_COUNT}} | 4 | Number of orders placed |
| {{PROVEN_VOLUME}} | 60 | Total kg ordered so far |
| {{MATERIAL_TYPE}} | PLA+ | Material |
| {{CURRENT_MONTHLY}} | 20 | Current monthly kg |
| {{PAYMENT_RECORD}} | On-time 100% | Payment history |
| {{SATISFACTION_LEVEL}} | Excellent | Your satisfaction |
| {{DEFECT_RATE}} | 2 | % defects observed |
| {{MID_VOLUME}} | 40 | 4-6 month projection |
| {{HIGHER_VOLUME}} | 60 | 5-6 month projection |
| {{Q4_VOLUME}} | 100 | Q4 projection |
| {{ANNUAL_PROJECTION}} | 600 | Total year projection |
| {{CURRENT_PRICE}} | $12.00/kg | Current unit price |
| {{TIER_1_PRICE}} | $11.50/kg | 50+ kg/month price |
| {{TIER_2_PRICE}} | $11.00/kg | 100+ kg/month price |
| {{BONUS_THRESHOLD}} | 500 | kg to unlock bonus |
| {{BONUS_DATE}} | December 31, 2026 | When bonus is awarded |
| {{BONUS_INCENTIVE}} | 10% discount | Bonus type |
| {{EXCLUSIVE_COMMITMENT}} | Use ModRun as primary supplier | Your commitment |
| {{MONTHLY_PROJECTION}} | 20+ | Minimum monthly order |
| {{PAYMENT_TERMS}} | Net-30 | Your standard terms |
| {{CURRENT_TERMS}} | Net-30 | Current terms |
| {{AGREEMENT_DATE}} | May 31, 2026 | When agreement finalizes |
| {{NEXT_MONTH}} | June 2026 | When volume increases start |

---

## Tips for Maximum Effectiveness

1. **Personalize ruthlessly** — Generic emails get generic responses. Use specific numbers, printer models, and timelines. Suppliers want to see you're serious.

2. **Lead with growth** — Suppliers care about trajectory. "20 kg/month growing to 500+ kg" is more interesting than "I need 20 kg."

3. **Establish urgency without pressure** — Include a decision deadline ("need answer by May 15") but don't demand same-day responses. 3-5 business days is reasonable.

4. **Mention competition carefully** — You can reference alternative quotes, but frame it as "I prefer your company, but pricing needs to be competitive" not "Your competitor is cheaper, beat it or you lose me."

5. **Build the long-term frame** — Phrase requests around partnership, not transactions. "I want a 6-month committed relationship" is stronger than "Can you give me a discount?"

6. **Follow up relentlessly** — First email goes to ~30% response rate. Second follow-up email (at day 10-14) gets another 15-20%. Phone call at day 21 gets another 10%. Don't give up after one email.

7. **Document everything** — Forward the final agreement email chain to yourself and save in a "Supplier Agreements" folder. If there's ever a dispute, you'll have proof of what you agreed to.
