---
title: Supplier Outreach & Negotiation Sequence
project: mfg-farm
created: 2026-05-06
status: ready-to-execute
audience: Anya — execute Day 0 immediately after test print passes
scope: Day-by-day supplier contact sequence, pre-filled templates, MOQ negotiation, sample workflow, contract checklist
related: phase-2-supplier-research.md, post-test-print-execution.md, post-test-print-doc-1-supplier-negotiation-email-templates.md
confidence: high
---

# Supplier Outreach & Negotiation Sequence

**Lead finding:** Three supplier relationships must be activated in the first seven days — not because you need them all immediately, but because supplier response cycles run 3–14 days and you need options on the table before the Month 2 volume step. Contact eSUN first (fastest to production); Anycubic second (validates your 50kg pallet option); Polymaker third (sets up the Month 3 quality upgrade). Do not wait to be "ready" — readiness here means having placed the first Amazon order and having a live Etsy listing URL. Both happen on Day 0.

---

## Day 0: Immediate Actions (Same Day as Passing Test Print)

### Priority 1: eSUN Amazon — Order Now, Negotiate Later

This is not a negotiation. Place the order immediately.

**What to order:**
- 1× eSUN PLA+ 10kg case, black (ASIN B0G2KWC5XL or search "eSUN 10kg PLA+ black")
- 1× eSUN PLA 1kg spool, white (for initial listing photos; verify your production recipe works in white)
- Expected total: $120–145 with Prime shipping

**Do not wait for a better price.** The difference between Amazon bundle pricing ($12/kg) and retail ($15/kg) on a 10kg first order is $30. The difference between getting filament in 3 days vs. 10 days is your entire launch timeline. Pay the extra $30.

**Concurrent action — send the eSUN wholesale introduction email:**

```
Subject: Wholesale Inquiry — ModRun Cable Clips, 20+ kg/month, Original Design

To: contact@esun3dstore.com

Hello eSUN Team,

My name is [YOUR NAME]. I'm launching ModRun, an original-design cable management 
system on Etsy ([ETSY SHOP URL once live — or omit and add later]).

I've been using eSUN PLA+ and am impressed with the AMS compatibility and 
consistency. I'm currently ordering via Amazon bundles, but as production scales 
toward 20–30 kg/month in the next 60 days, I'd like to explore direct wholesale 
pricing.

Current setup:
- Printer: Bambu P1S
- Primary material: PLA+ 1.75mm, colors: black, white, grey
- Current volume: 10 kg/month (growing)
- Product: Etsy-sold cable management clips, made-to-order

Growth plan:
- Month 2–3: 20–30 kg/month
- Month 4–6: 40–60 kg/month (multi-printer)

I'm not looking to negotiate against your Amazon pricing — I want to understand 
what a direct wholesale relationship looks like at 20–50 kg/month. Specifically:
1. Is there a direct wholesale pricing tier for this volume?
2. What is the minimum order for direct pricing?
3. Are Net-15 or Net-30 payment terms available at any volume?

Happy to share production specs and my Etsy shop link once listings go live.

Best regards,
[YOUR NAME]
ModRun — [PHONE OR EMAIL]
```

**Expected response time:** 2–3 weeks. eSUN wholesale is slow to respond. This email plants the seed — you are not expecting a same-week answer.

---

### Priority 2: Anycubic — Place Test Order Today

Do not wait for the eSUN wholesale response before pre-qualifying Anycubic. These are parallel tracks.

**What to order:**
- Navigate to store.anycubic.com
- Find the PLA Basic bundle, any available weight that gives you 5–10 kg of black (the most common color option)
- If only 50kg pallet is available, order one standard 1kg spool instead — enough to run the AMS validation test
- Expected cost: $15–70 depending on available increments

**Purpose of this order:** AMS compatibility validation only. You are not buying Anycubic to use at scale today. You are buying it to confirm it works in your P1S before you need the 50kg pallet later. If it passes the AMS test (see stl-refinement.md Gate 4 protocol), Anycubic becomes your Month 3 bulk option at $10.49/kg. If it fails, you know before you need it.

**No email needed.** Anycubic is a direct-purchase, no-negotiation supplier at the bundle pricing level. Place the order via the storefront.

---

## Day 1–3: Sample Validation Protocol

When the Anycubic filament arrives (7–10 day lead time), run this before using it in production.

### Anycubic AMS Validation Test

**Setup:**
- Load one Anycubic spool into the AMS on your P1S
- Do not mix with eSUN in the same print job for this test

**Validation print:**
- Slice and print one full 12-clip plate using the ModRun-PLA-Production-v1 slicer profile
- Monitor the print for the first 30 minutes for AMS feed errors (the most common Anycubic failure mode)
- Let the full plate complete without intervention if no feed errors occur

**Measurement check:**
- Measure 3 clips from the Anycubic plate with calipers
- Snap arm width must be within ±0.3 mm of the same measurement from eSUN filament
- If dimensions match: Anycubic is qualified for production use

**Pass/fail criteria:**

| Result | Decision |
|---|---|
| Zero feed errors, dimensions match eSUN ±0.3mm | Pass — Anycubic is qualified; proceed to pre-order pallet at Month 3 |
| 1–2 minor feed errors (self-recovering), dimensions match | Conditional pass — monitor one more plate; if clean, qualify |
| Feed errors requiring manual intervention, or dimensions off >0.3mm | Fail — do not use Anycubic for production; note lot number in supplier log |

**Document the result** in your supplier scorecard. You need this data before placing a $524 pallet order.

---

## Day 3–5: Overture Introduction Email

Overture is your PETG primary and PLA backup. Contact them before you need them.

```
Subject: Wholesale Introduction — ModRun Cable Management, PLA+ and PETG

To: wholesale@overture3d.com

Hello Overture Team,

I'm [YOUR NAME], launching ModRun — an original-design cable management product 
on Etsy (launching [MONTH] 2026). I'm currently sourcing PLA+ via eSUN but am 
evaluating suppliers for a second-source relationship and for PETG as I add 
premium SKUs.

Current situation:
- Printer: Bambu P1S
- Primary need: PLA+ 1.75mm (black, white, grey), 10–20 kg/month near-term
- Secondary need: PETG 1.75mm (black, white) for premium tier products launching 
  Month 2–3; 3–5 kg/month initially

I've seen your 35% wholesale discount program mentioned online. I'd like to 
understand the qualification requirements and whether 10–20 kg/month PLA+ 
qualifies for wholesale pricing.

Can you share:
1. Volume threshold to qualify for wholesale pricing
2. PETG pricing at 5 kg/month quantity
3. Lead time for orders, and whether Prime-equivalent expedited shipping is available

I'm not in an emergency — I'm planning supply relationships for the next 3–6 months.

Best regards,
[YOUR NAME] / ModRun
[EMAIL / PHONE]
```

**Expected response time:** 3–7 business days. Overture is more responsive than eSUN wholesale.

**What to do with the response:** Compare Overture PLA+ pricing to your live eSUN Amazon bundle price. If Overture wholesale is within $1/kg of Amazon bundles, add Overture to your approved supplier list and rotate orders between them to reduce single-supplier dependency. If Overture is more expensive, keep them as PETG-only and note in the supplier scorecard.

---

## Day 5–7: Polymaker Wholesale Account Registration

Polymaker wholesale is a Month 3–4 activation, but the account registration takes time and you should do it before you need it.

**Registration steps:**
1. Go to `us-wholesale.polymaker.com`
2. Click "Apply for Wholesale" (or equivalent account registration link)
3. Fill in: business name (your Etsy shop name is sufficient), printer model, monthly volume projection (enter "20–50 kg/month, growing"), primary products (cable management accessories)
4. Submit

**What happens next:** Polymaker may take 5–10 business days to approve the wholesale account and provide login credentials. Once approved, PolyLite PLA pricing is visible at approximately $14.99/kg for case-of-10 orders.

**Do not place an order yet.** The Polymaker account registration is just that — registration. The first order comes at Month 3 when you need white or grey filament at a quality tier above eSUN (for product photography and premium SKUs). At $14.99/kg vs. eSUN's $12/kg, the $2–3/kg premium is only justifiable when the aesthetic quality of the visible surface is a customer-facing differentiator.

---

## Week 2: MOQ Negotiation Preparation

By the end of Week 1, you should have:
- eSUN case ordered (in transit or delivered)
- Anycubic test order placed
- Overture introduction email sent
- Polymaker wholesale registration submitted

**Week 2 action:** When Overture or eSUN wholesale responds with pricing, run this decision logic.

### MOQ Negotiation Talking Points

The suppliers you are dealing with at this scale (eSUN direct, Overture wholesale) are accustomed to small-business operators. The following talking points work at 10–30 kg/month volume and will get you 5–15% below initial quotes:

**Talking point 1 — Volume commitment over time:**
"I'm committing to a 6-month relationship with a primary supplier. I'm at 10 kg/month today and projecting 30–50 kg/month by Month 4. I'd rather give you more volume at a consistent price than shop around every month. What does 20 kg/month for 6 months look like?"

**Talking point 2 — Color flexibility:**
"I primarily need black and white PLA+. I'm flexible on the exact SKU and spool format (cardboard refill or standard spool both work). Does the format affect pricing?"

**Talking point 3 — Payment terms over price:**
"If your list price is firm at [X]/kg, I understand. Can we structure Net-30 payment terms instead of credit card on order? That helps my cash flow significantly and I'd commit to 6 months of Net-30 orders at your list price."

**What to accept immediately:**
- Any price at or below $12/kg for 10kg+ case quantities
- Net-15 or Net-30 terms at any price (cash flow value exceeds the $0.50–1.00/kg price difference you'd otherwise negotiate)
- A tiered discount: e.g., "10kg at $13, 20kg at $12, 30kg at $11.50"

**What to counter:**
- Any first-order MOQ above 20 kg (you don't have the storage or cash flow to justify this yet)
- Any prepay requirement above 50% of order value with no Net-anything terms
- Any "no price guarantee" clause (you need at least 90-day price stability)

**What to walk away from:**
- Any supplier requiring a minimum 50kg first order with full prepayment
- Any supplier with lead times greater than 14 days without expedited option (too risky during demand spikes)

---

## Month 1: Contract Negotiation Checklist

When a supplier relationship is confirmed and you are ready to move beyond test orders, use this checklist before committing to repeat orders.

**Before placing any order above $200:**
- [ ] Lead time is stated in writing (email is sufficient — forward to yourself for records)
- [ ] Color availability for your 3 primary colors (black, white, grey) is confirmed
- [ ] Defect replacement policy is stated: full replacement or credit — not "contact us to discuss"
- [ ] Diameter tolerance is specified (eSUN: ±0.03mm; Anycubic: ±0.05mm acceptable)

**Before placing any order above $500:**
- [ ] Price is confirmed locked for minimum 60 days from order date
- [ ] Net-15 or Net-30 terms available (or documented reason why not and your decision to proceed anyway)
- [ ] Point of contact (specific person, not just info@supplier.com) is established
- [ ] You have tested at least 1 kg of their filament in production (not just a test print)

**Before committing to a pallet order ($500+, single shipment):**
- [ ] Anycubic pallet ($524 for 50kg): AMS validation test has passed — full plate printed, zero feed errors, dimensions match production spec
- [ ] Storage capacity confirmed: 50kg requires approximately 50 spools of filament storage; confirm your storage area can accommodate this
- [ ] Cash flow check: pallet order should not exceed 25% of your current month's gross revenue

---

## Supplier Contact Reference

| Supplier | Contact | Method | Priority | When to Contact |
|---|---|---|---|---|
| eSUN Amazon | amazon.com checkout | Direct order | Day 0 | Order immediately |
| eSUN wholesale | contact@esun3dstore.com | Email | Day 0 | Send intro email same day as Amazon order |
| Anycubic direct | store.anycubic.com | Direct order | Day 0 | Order test quantity same day |
| Overture wholesale | wholesale@overture3d.com | Email | Day 3–5 | Send intro after eSUN order confirmed delivered |
| Polymaker wholesale | us-wholesale.polymaker.com | Account registration | Day 5–7 | Register account; no order yet |
| SUNLU | support@3dsunlu.com | Email | Day 10–14 | Color sampling only; contact when standard colors are confirmed |
| Pirate Ship | pirateship.com | Account setup | Day 0 | Connect Etsy integration same day |
| Shop4Mailers | shop4mailers.com | Direct order | Day 0 | Order 1,000-pack poly mailers immediately |

---

## Cost Reduction Opportunities by Supplier

Track these as monthly review items, not Day 0 priorities.

**eSUN (Amazon vs. direct wholesale):**
- Current: $11–13/kg (10kg Amazon bundle)
- Potential: $8.50–10/kg (eSUN direct at 20–40 kg/month commitment)
- Activation: Contact direct when monthly consumption exceeds 20 kg for 2 consecutive months
- Monthly savings at 30 kg/month: up to $90–135 vs. Amazon bundle pricing

**Anycubic (test order vs. pallet):**
- Test order (5–10 kg): ~$10.50–12/kg
- Pallet (50 kg): $10.49/kg
- The pricing is nearly the same — Anycubic's pallet is a cash-flow and storage commitment decision, not a per-kg savings decision
- Primary benefit of pallet: fewer reorder events, lower risk of stock-outs during peak periods

**Packaging (early vs. scale):**
- Month 1: Amazon basics poly mailers at ~$0.10/unit
- Month 2+ at 1,000 units: Shop4Mailers at $0.05/unit
- Savings: $50/1,000 units — worth ordering the 1,000-pack from Day 1 rather than dribbling through Amazon packs

**Shipping (retail vs. Pirate Ship):**
- USPS retail label: ~$5.50 for a 4oz Ground Advantage package
- Pirate Ship commercial rate: ~$4.00–4.50 (same service)
- Savings per order: $1.00–1.50
- At 20 orders/week: $80–120/month — this is the single highest-ROI cost reduction available
- Action: Open Pirate Ship account and connect Etsy integration on Day 0; no volume minimum

---

## Confidence Notes

**High confidence:** All pricing figures are drawn directly from phase-2-supplier-research.md verified pricing (April 2026). Email addresses for eSUN and Overture are sourced from that document. Pirate Ship savings estimate uses confirmed commercial rate data from post-test-print-execution.md.

**Gap:** eSUN wholesale email (contact@esun3dstore.com) was documented in post-test-print-execution.md as the correct address but has not been live-tested for deliverability. If email bounces, alternative is the contact form at esun3dstore.com or a Facebook Messenger message to their business page.
