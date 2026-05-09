---
title: ModRun Pre-Launch Fulfillment Workflow — End-to-End Operationalization
date: 2026-05-09
version: 1.0
status: ready-for-execution
related:
  - fulfillment-workflow.md
  - DAY1_LAUNCH_OPERATIONS_PLAYBOOK.md
  - post-test-print-fulfillment-dryrun.md
  - post-test-print-launch-checklist.md
  - usps-thermal-printer-integration.md
---

# ModRun Pre-Launch Fulfillment Workflow

**Purpose**: Fill the operational gaps not covered by existing SOPs. `fulfillment-workflow.md` owns print-to-ship operations. `DAY1_LAUNCH_OPERATIONS_PLAYBOOK.md` owns launch-day execution. This document covers: payment processing for direct/custom sales, carrier selection rationale, customer support infrastructure, returns and warranty policy, and the critical-path launch checklist that sequences all prior documents into a 1-2 week setup window.

**Do not re-read the existing SOPs** while working through this document. This is the master index — it tells you which document to consult for each decision, and fills gaps those documents do not address.

---

## 1. Payment Processing

### Context

On Etsy and Amazon, payment processing is handled by the platform (Etsy Payments at 3% + $0.25/order; Amazon at 15% flat). No separate payment processor is needed for marketplace sales. A standalone processor becomes necessary in three scenarios:

1. **Custom orders requested outside Etsy** — a customer contacts you directly for a non-standard variant
2. **Bulk/wholesale inquiries** — a business wants 50+ units billed by invoice
3. **Future own-channel sales** — if you build a Shopify storefront or accept direct orders

For the launch period (Months 1-4), all sales should flow through Etsy or Amazon. Do not divert buyers off-platform — it violates both platforms' terms of service and costs you the platform's built-in buyer protection. The processor comparison below is for Month 4+ when direct sales become a real scenario.

### Comparison

| Factor | Stripe | Square | PayPal |
|---|---|---|---|
| Online rate | 2.9% + $0.30 | 2.9% + $0.30 | 2.99% + $0.49 |
| In-person rate | 2.7% + $0.05 | 2.6% + $0.10 | 2.29% + $0.09 |
| Payout speed | 2 business days (instant available for 1.5% fee) | Next business day standard | Immediate to PayPal balance; 1-3 days to bank |
| Monthly fee | None | None | None (standard) |
| Chargeback fee | $15/dispute | $15/dispute | $15/dispute |
| Developer API | Excellent — easiest to integrate with custom sites | Good | Functional but dated |
| Shopify integration | Native, lowest friction | Native | Native |
| International | Clean — 1% surcharge per currency conversion | US-focused | Steeper: 3-4% on currency conversion |
| Buyer trust signal | Minimal — invisible to buyers | Minimal | High — PayPal brand recognition adds conversion on low-trust buyers |

**Net effect on a $24.99 ModRun order**:
- Stripe: $0.72 + $0.30 = $1.02 fee
- Square: $0.72 + $0.30 = $1.02 fee
- PayPal: $0.75 + $0.49 = $1.24 fee

PayPal costs ~$0.22 more per transaction. On 100 direct orders/month, that is $22/month in excess fees for no operational benefit.

### Recommendation: Stripe

**Why Stripe over Square**: Square's advantage is in-person card readers (2.6% + $0.10). This operation does not do in-person sales. Online, Stripe and Square are identical in rate but Stripe has a cleaner API and broader integration ecosystem. If you add a Shopify store or build a custom order form, Stripe integrations are faster to implement and better documented.

**Why not PayPal**: Higher per-transaction cost. Buyer trust advantage is irrelevant when buyers arrive through Etsy or Amazon where the platform trust signal dominates. For direct custom orders, a simple Stripe payment link is equivalent in friction to PayPal.

**Setup steps** (30 minutes, do in Month 3-4 before needing it):
1. Create account at stripe.com — verify identity and bank account
2. Create a Payment Link (Stripe Dashboard → Payment Links → Create) for the most common custom order amount (e.g., $29.99 for a custom-color Starter Bundle)
3. Store the link in your email signature and Etsy message templates as "Pay securely here for custom orders"
4. Set payout schedule to weekly automatic (avoids cash flow gaps from 2-day rolling holds)

**Monthly operating cost**: $0 fixed. Variable: 2.9% + $0.30 per transaction.

**Integration complexity**: Low. No code required for payment links. If you later build a Shopify store, Stripe is the default payment processor and connects in 2 clicks.

---

## 2. Shipping Integration

### Carrier Comparison

This section focuses on the rationale behind the existing recommendation. `fulfillment-workflow.md` Section 5 and `post-test-print-fulfillment-dryrun.md` Phase 5 contain rate tables — do not duplicate those numbers here.

| Factor | USPS Ground Advantage | FedEx Home Delivery | UPS Ground |
|---|---|---|---|
| Rate <1 lb | $3.50-6.00 (Pirate Ship) | $6.45 base + residential surcharge | $6.50 base + residential surcharge |
| Residential surcharge | None | $6.45 (included above) | ~$4.65-6.50 extra |
| Minimum volume required | None | None (retail rates without account) | None (retail rates without account) |
| Free scheduled pickup | Yes — free carrier pickup at your door via usps.com | Yes (FedEx Ground) | Yes (UPS My Choice) |
| Pickup scheduling lead time | Same-day if scheduled before 2 PM | Next business day | Next business day |
| Label printing | Pirate Ship PDF → thermal printer | FedEx Ship Manager | UPS.com or WorldShip |
| Tracking transparency | Full tracking in buyer-facing Etsy notifications | Full tracking | Full tracking |
| Discount access | Pirate Ship: ~15-20% below USPS retail (free, no monthly fee) | Requires volume account for meaningful discount | Requires volume account |
| Priority consideration | Commercial cubic rates unlock on Pirate Ship for small dense packages | N/A at this volume | N/A at this volume |

**Pickup availability**: USPS free carrier pickup is the most operationally important feature. Schedule at usps.com/pickup by 2 PM for same-day pickup. This eliminates the daily USPS dropoff trip, which at 2+ shipments/day otherwise costs 10-15 minutes of travel. Set a recurring pickup schedule once order volume is consistent.

**FedEx/UPS position**: Use only as contingency if USPS has a service disruption (weather delay, local carrier strike). At launch volumes, neither carrier offers a meaningful cost advantage. Revisit at 200+ shipments/month when a UPS or FedEx volume account becomes negotiable.

**Recommendation**: USPS Ground Advantage via Pirate Ship for all orders through Month 6. This is already the default in `fulfillment-workflow.md` — this section confirms the rationale and adds the USPS free pickup detail.

**Monthly operating cost**: $0 fixed (Pirate Ship has no subscription fee). Variable: carrier cost per label ($3.50-6.00 per package depending on weight and zone).

**Integration complexity**: Low. Pirate Ship connects to Etsy in one OAuth authorization step. Labels import automatically from open Etsy orders — no manual data entry.

---

## 3. Customer Support Workflow

### Volume Projection

At <10 orders/day (Months 1-4), expect 2-5 customer messages per week: order status questions, custom color requests, fit questions, and occasional post-delivery issues. This does not justify a paid ticketing platform.

### Tool Recommendation: Freshdesk Free Tier (Months 1-4), then Gmail + canned responses (permanent fallback)

**Freshdesk free plan** (up to 2 agents, 6-month trial):
- Email ticketing: All Etsy and direct-email customer messages can be forwarded to a Freshdesk inbox
- Knowledge base: Build a self-service FAQ (reduces inbound by ~30% on common questions)
- Ticket dispatch: Auto-tag by message type (order status / fit question / return request)
- Cost: $0 for 6 months

After the 6-month free tier ends, re-evaluate volume. If still under 30 messages/week, a Gmail label system with saved replies ($0) is operationally sufficient and preferable to paying $25/user/month for Help Scout or $19/agent/month for Zendesk. Freshdesk's paid tier starts at $15/agent/month if you need to continue with the platform.

**Zendesk**: Priced for teams, not solo operators. Minimum effective plan is $19/agent/month (Suite Team). Overkill at <10 orders/day. Skip until Month 9+ and only if you have a dedicated support person.

**Help Scout**: $25/user/month. Better UX than Zendesk for small teams, but still $300/year for a solo operator handling 5 messages/week. Unjustifiable at this stage.

### FAQ Structure

Build this once in Freshdesk's knowledge base (or a static page linked from your Etsy shop's FAQ section):

**Section 1: Orders and Production**
- How long until my order ships? (Answer: 1-2 business days, printed to order)
- Can I get a custom color? (Answer: yes, message before ordering; list available colors)
- Do you offer bulk/wholesale pricing? (Answer: yes for 20+ units, message for quote)
- Can I get a custom size/variant? (Answer: yes for cable diameters; detail process)

**Section 2: Shipping and Delivery**
- Which carrier do you use? (USPS Ground Advantage; 2-5 business days after ship date)
- Do you ship internationally? (Answer: not at launch; revisit at Month 6)
- My tracking hasn't updated in 3 days — is this normal? (Answer: yes, USPS Ground Advantage sometimes scans only at origin and destination)
- My package shows delivered but I haven't received it. (Answer: wait 24 hours; check with neighbors and mailbox; file USPS lost mail claim if still missing after 48 hours — provide instructions)

**Section 3: Product and Fit**
- Will this work with my cable diameter? (Answer: specify bore sizes available; note the cable range each clip supports)
- The clip feels tight on the rail — is that normal? (Answer: yes, tight is intentional; it loosens slightly with use; if it won't engage at all, message us)
- The snap arm broke. What do I do? (Answer: covered under 30-day warranty; see warranty section)
- Can I return a product if it doesn't fit my setup? (Answer: 30-day return policy; see below)

### Email Template Library

**Template 1: Order Confirmation + Ship Timeline (send within 2 hours of order)**
```
Subject: Your ModRun order is in the print queue — ships by [DATE]

Hi [FIRST NAME],

Thanks for your order! Your [PRODUCT NAME] is in our print queue and will ship by [DATE] via USPS Ground Advantage. You'll receive tracking automatically from Etsy once it ships.

If you need a different color or have a custom request, reply here and I can adjust before printing.

— [Your name], ModRun
```

**Template 2: Shipped Notification (after generating label, if Etsy auto-notify feels too generic)**
```
Subject: Your ModRun order shipped — tracking inside

Hi [FIRST NAME],

Your [PRODUCT NAME] shipped today via USPS Ground Advantage. Tracking: [NUMBER]

Estimated delivery: [DATE RANGE]. USPS Ground Advantage sometimes skips intermediate scans, so don't worry if tracking doesn't update for a day or two.

Once installed, I'd love to hear how it fits your setup. If anything isn't right, message me directly — I'll make it right.

— [Your name], ModRun
```

**Template 3: Custom Order Confirmation**
```
Subject: Custom ModRun order confirmed — here's what we agreed

Hi [FIRST NAME],

Confirming your custom order:
- Product: [ITEM]
- Color: [COLOR]
- Cable diameter: [SIZE]mm
- Quantity: [QTY]
- Price: $[PRICE]
- Payment link: [STRIPE LINK if outside Etsy] OR "paid via Etsy listing"
- Estimated ship date: [DATE]

If any of this is off, reply before [CUTOFF DATE] and I'll adjust. After that, I'll start printing.

— [Your name], ModRun
```

**Template 4: Return/Issue Response**
```
Subject: Re: Your ModRun order — let me fix this

Hi [FIRST NAME],

Sorry to hear about the issue with your [PRODUCT]. I stand behind the 30-day satisfaction guarantee.

To sort this out: [Choose one]
A) I'll send a replacement [ITEM] right away — no return required. Just confirm your shipping address is still [ADDRESS].
B) If you'd prefer a refund, I'll process it as soon as you confirm — no need to return the item for orders under $30.

Which works best for you?

— [Your name], ModRun
```

**Monthly operating cost**: $0 for Months 1-6 (Freshdesk free tier). $15/agent/month if upgrading to Freshdesk Growth after Month 6.

**Integration complexity**: Low. Forward your support email to Freshdesk inbox during setup (15 minutes). No code required.

---

## 4. Inventory and Quality Control

The granular QA checklist, dimensional tolerance table, defect classification, and batch log structure are fully specified in `fulfillment-workflow.md` Section 3. This section adds the operational framework that `fulfillment-workflow.md` assumes but does not state explicitly.

### Print Queue Management Tool

**Months 1-3**: Google Sheets is sufficient. Column schema is defined in `fulfillment-workflow.md` Section 2. Create the sheet before the first order arrives.

**Month 4+**: If managing 2+ printers and 50+ orders/month, add SimplyPrint (free tier: up to 2 printers). SimplyPrint integrates directly with Bambu Lab printers and provides a multi-printer queue dashboard. Obico (open-source) provides AI failure detection with Bambu integration. Both are free at this scale.

### Quality Checkpoints Summary

Three gates — do not skip any:

1. **Post-print gate** (at the printer): Obico AI failure detection flags print failures automatically. Clear all flagged prints before harvesting. Time: passive monitoring.

2. **Pre-pack gate** (at the packing station): 30-45 second visual + functional check per unit per `fulfillment-workflow.md` Section 3 checklist. This is the gate that prevents defects from reaching customers.

3. **Dimensional spot-check** (1 unit per 5-unit batch): Caliper measurement per `fulfillment-workflow.md` Section 3 tolerance table. Confirms production settings haven't drifted. If a batch-level dimensional issue is found, measure all units in the batch before shipping any.

### Defect Logging

Log all reprints in your print queue Google Sheet (columns: Reject Date, SKU, Defect Type, Root Cause). Reviewing this log monthly surfaces systematic problems (e.g., a specific color consistently delaminating = filament moisture issue; a specific SKU consistently warping = print settings need adjustment). Without the log, you will repeat failures.

### Reprints Policy

Reprint every functional defect without hesitation. The cost arithmetic: reprint costs $0.90-$2.25 in filament. A shipped defect costs $8-15 in return shipping + replacement + risk of a 1-star review that suppresses your listing visibility for months. Reprint. No exceptions for critical or major defects.

---

## 5. Packaging and Fulfillment

The packaging specifications, material procurement list, and branding guidelines are fully covered in `fulfillment-workflow.md` Section 4. Key points not to miss:

**Phase 1 cost per order** (launch through ~200 units/month):
- Poly mailer 9x12": $0.05
- Crinkle paper or tissue: $0.02
- Thank-you card: $0.03-0.05
- Total packaging cost: ~$0.10-0.12 per order

**Phase 2 branded packaging** (200+ units/month): Custom-printed poly mailers from Vistaprint or Smart Shipping Supply. At 500-unit minimum orders, cost rises to $0.38-0.50 per mailer but creates brand differentiation. Lead time: 10-14 days. Order Phase 2 packaging at the end of Month 2 to have it ready before Month 3 volume arrives.

**Sustainable material preference**: When ordering Phase 2 packaging, specify recycled-content poly mailers or Kraft paper mailers. Smart Shipping Supply and EcoEnclose both offer certified recycled options at a ~15-25% premium over standard poly. This is a credible claim to include in Etsy listings ("shipped in recycled-content packaging") which resonates with the hobbyist gardener customer base.

**Unboxing experience**: The thank-you card insert is the highest-leverage dollar spent in the box. The template in `post-test-print-fulfillment-dryrun.md` Phase 2 is production-ready. Print 50 copies before the first order. The card communicates the 30-day guarantee, the installation steps, and the shop URL. It generates repeat visitors and review requests without any additional cost.

**Assembly time per order**: Target 90 seconds at pace (first 5 units will take 2-3 minutes). Time yourself during the dry run (`post-test-print-fulfillment-dryrun.md` Phase 4 labor tracker). If you're over 3 minutes per order after 20 orders, identify the bottleneck — usually it is label affixing or counting clips. Pre-counting clips into zip-lock bags during downtime eliminates the mid-pack counting step.

---

## 6. Returns and Warranty

### 30-Day Return Policy

**Policy statement** (use verbatim in Etsy shop policies section):
> We accept returns within 30 days of delivery. If your ModRun product doesn't fit your setup or you're not satisfied, message us before returning. For orders under $40, we will issue a full refund without requiring a return shipment — it is not cost-effective to ship a $5 part back and forth. For orders over $40, we will provide a prepaid return label.

**Cost impact**: Assuming a 3-4% return rate (industry baseline for functional products, after QA tightening):
- At 50 orders/month × $24.99 average × 3.5% return rate = 1.75 returns/month
- Refund cost: ~$43/month on average
- No-return-required policy for <$40 orders eliminates $4-6 in return postage per claim and takes 5 minutes instead of 30 minutes
- Net: the no-return policy costs roughly the same as requiring returns but generates significantly better customer experience and review outcomes

**What drives returns for 3D printed products**:
- Fit mismatch (cable diameter doesn't match the specific cable) — mitigate by specifying cable diameter ranges clearly in listings
- Color disappointment (screen colors vs. physical PLA color) — mitigate by noting "PLA colors may vary slightly from screen" in listings
- Defects that passed QA — these should be below 1% with the QA protocol in place

### Defect Warranty

**Policy statement**:
> All ModRun products carry a 30-day defect warranty. If a snap arm breaks under normal use, or if dimensional tolerances prevent clip engagement with the rail, we will ship a replacement at no charge. Warranty does not cover damage from use beyond intended load (e.g., suspending heavy objects from a cable clip rated for cable management).

**Warranty cost modeling**: At <1% critical defect rate, warranty claims at 50 orders/month = 0.5 claims/month. Each claim costs $0.90-2.25 to reprint + $3.50-5.00 to ship. Monthly warranty cost: ~$2-4. Negligible.

### Customer Refund Flow

1. Customer messages via Etsy (or email for direct orders)
2. Respond within 24 hours using Template 4 above
3. For defect or fit issue: offer replacement first, refund second
4. If refund: process through Etsy's "Issue a refund" flow (automatically debits your Etsy payment account; no manual payment required)
5. For direct-sale refunds via Stripe: Dashboard → Payments → find transaction → Refund
6. Log the return reason in your defect log — this data feeds QA improvements

---

## 7. Launch Readiness Checklist

**Timeline**: Complete this in order. Dependencies are noted. Total estimated time: 6-8 hours spread across Days 1-7 after test print confirmation. Days 8-14 are for buffer, photography, and listing refinement.

### Critical Path

```
TEST PRINT PASS
    ↓
Day 0-1: Physical validation (1.5 hours)
    → fulfillment-workflow.md Section 3 tolerance checks
    → post-test-print-launch-checklist.md Part 1 go/no-go criteria
    ↓
Day 1-2: Packaging materials ordered (30 minutes)
    → fulfillment-workflow.md Section 4 procurement list
    → Order: poly mailers, postal scale, calipers if not owned
    → Arrival: 2-3 days via Amazon Prime
    ↓
Day 1-2: Accounts setup (2 hours — can run in parallel with ordering)
    → Pirate Ship account + Etsy store connection
    → Etsy shop policies section completed (return policy verbatim from Section 6 above)
    → Freshdesk free account (15 min setup; forward support email to Freshdesk inbox)
    → Google Sheets print queue created (schema: fulfillment-workflow.md Section 2)
    ↓
Day 2-3: Photography (2-3 hours)
    → post-test-print-doc-3-lifestyle-photography-brief.md specifications
    → Minimum: 5 photos per listing (hero, in-use, detail, multi-unit, packaging)
    ↓
Day 3-5: Etsy listings drafted and reviewed (1.5 hours)
    → etsy-listing-modrun.md — all copy pre-written; use verbatim or adapt
    → etsy-seo-strategy.md — title, tags, attributes; use the keyword research
    → Post listings as "draft" (not published) — do not publish until print queue is live
    ↓
Day 5-7: Dry run fulfillment (2 hours)
    → post-test-print-fulfillment-dryrun.md — complete all 7 phases
    → Validate actual margin vs. cost model
    → Validate label pipeline (Pirate Ship → thermal printer or PDF)
    ↓
Day 7: First listings published
    → Etsy: publish 2-3 listings (start narrow — validate demand before expanding catalog)
    → Confirm Etsy shop policies are visible and correct
    → Confirm Pirate Ship + Etsy integration active and pulling orders
    → Confirm Freshdesk support email forwarding active
    ↓
Day 8-14: Buffer and monitoring
    → Build 14-day safety stock of top 2 SKUs during idle print time
    → Monitor Etsy stats daily (views → click rate → conversion)
    → Post first order within 2 business days of receipt (2-day promise active from listing-live)
```

### Setup Dependencies (Nothing Can Start Until These Are Done)

| Dependency | Action Required | Time |
|---|---|---|
| Test print pass | Run post-test-print-launch-checklist.md Part 1 | 90 minutes |
| Bambu P1S operational | Verify bed adhesion, filament dry, nozzle clean | 30 minutes |
| Pirate Ship account | Account creation + Etsy connect | 20 minutes |
| Postal scale (0.1 oz precision) | Order if not owned ($15-20 Amazon) | 2-3 day delivery |
| Digital calipers | Order if not owned ($15-20 Amazon) | 2-3 day delivery |
| Thermal label printer | Rollo or equivalent ($100-130) OR inkjet fallback | If ordering: 2-3 days |

**No-code fallback for label printing**: If you do not have a thermal printer at launch, print labels from Pirate Ship as PDFs on standard paper and tape them to packages. This adds ~$0.05/label (tape + paper) and 30 seconds per label vs. a thermal printer. It is a valid Day 1 solution — order the thermal printer with first week's revenue.

---

## 8. 30-Day Ramp-Up Timeline

### Expected Order Volume

These projections are based on the Etsy algorithm behavior documented in `etsy-seo-strategy.md` and `market-research.md`. New listings get a 2-week visibility boost from Etsy's "new listing" promotional window, then settle into algorithmic placement based on conversion rate and review velocity.

| Period | Expected Weekly Orders | Daily Ship Volume | Notes |
|---|---|---|---|
| Week 1 (listing live) | 0-3 | <1/day | Etsy new listing boost; likely no sales first 48 hours |
| Week 2 | 2-6 | 1/day | First sales from new listing window; first reviews opportunity |
| Week 3-4 | 4-10 | 1-2/day | Settling into base algorithmic position; review velocity starts mattering |
| Month 2 | 10-25/week | 1-4/day | Consistent if 5+ reviews; conversion improving |
| Month 3 | 20-50/week | 3-7/day | Clear signal on demand level; printer utilization meaningful |

### Staffing Needs by Stage

**Months 1-2 (0-25 orders/week)**: Solo operator handles everything. Time allocation per week: 15-18 hours total (per `market-research.md` Section 5 Stage 1 breakdown). No additional help needed.

**Month 3 (25-50 orders/week)**: At 50 orders/week, packaging and shipping takes 4-5 hours/week. Still solo-manageable. If you are also managing 2 printers at this point, you will start feeling the squeeze on packing time — this is the moment to establish a dedicated packing window (e.g., daily 4-6 PM) rather than ad-hoc packing.

**Month 4-5 (50-100 orders/week)**: This is where part-time help becomes valuable. The packing and shipping task is the correct first thing to delegate — it requires no design or technical judgment, the SOP is fully documented, and training takes under 2 hours. Target: 1 part-time person, 8-12 hours/week, paid $15-18/hour. Expect to spend $500-800/month on labor at this stage.

### Scaling Triggers

**Add second printer when**: Monthly revenue consistently exceeds $1,500 AND the single printer is running 16+ hours/day with unfulfilled orders in queue. At that point, a second Bambu P1S (~$700-950) pays back in under 6 weeks. Do not add a printer speculatively — demand must be proven first. Per `market-research.md` Section 5 Stage 2, the second printer is Bambu P1S (not a second X1C).

**Add Amazon Handmade when**: Etsy sales are 20+ orders/month with 25+ reviews on at least 2 SKUs. Amazon Handmade for functional products (cable management, desk organizers) benefits from the platform's purchase-intent search traffic but requires established listing quality to convert. Setting up Amazon before you have proven Etsy listings wastes 4-6 hours of setup time with no return.

**Add part-time help when**: You are spending more than 6 hours/week packing and shipping. That is the signal that your time is worth more on design, marketing, and business operations than on label-affixing.

**Add Craftybase (inventory/COGS tracking) when**: 20+ orders/month. At that point, manual COGS tracking is error-prone and Craftybase's $49/month is justified by time savings and tax season accuracy. Setup guide in `fulfillment-workflow.md` Section 6.

**Add SimplyPrint when**: Operating 2+ printers. SimplyPrint's free tier handles up to 2 printers with queue management, remote monitoring, and Bambu integration. Do not add it for a single-printer operation — the overhead is not justified.

**Consider 3PL (Simpl Fulfillment, ShipMonk) when**: 200+ orders/month. 3PL setup, inventory pre-stocking, and packaging standardization requirements make earlier adoption operationally counterproductive. Full 3PL analysis at `3pl-readiness-analysis.md`.

### Monthly Cost Structure at Scale

| Cost Item | Month 1 | Month 3 | Month 6 |
|---|---|---|---|
| Filament ($15/kg, ~150g/order avg) | $15-30 | $45-90 | $90-180 |
| Packaging materials | $5-10 | $15-30 | $30-60 |
| Shipping (customer-paid, net zero) | $0 | $0 | $0 |
| Pirate Ship | $0 | $0 | $0 |
| Freshdesk | $0 | $0 | $0 (or $15/mo if upgrading) |
| Craftybase | $0 | $49 | $49 |
| Custom packaging (Phase 2) | $0 | $0 | $40-80 |
| Part-time labor | $0 | $0 | $400-800 |
| **Total fixed + variable COGS** | **$20-40** | **$109-169** | **$609-1,169** |
| **Estimated revenue** | **$200-500** | **$800-1,500** | **$2,500-5,000** |
| **Net retained (after platform fees ~15%)** | **$130-385** | **$530-1,110** | **$1,516-3,081** |

---

## Quick Reference: Setup Sequence and Time Budget

For the "1-2 hours of infrastructure setup" target post-test-print:

| Task | Time | When |
|---|---|---|
| Pirate Ship account + Etsy connect | 20 min | Day 1 |
| Freshdesk account + email forward | 15 min | Day 1 |
| Google Sheets print queue (copy schema from fulfillment-workflow.md) | 15 min | Day 1 |
| Etsy shop policies section (copy from Section 6 above) | 10 min | Day 1 |
| Stripe account (for future custom orders) | 20 min | Day 1 (optional, can defer to Month 3) |
| **Total Day 1 infrastructure** | **~80 minutes** | Day 1 |

Photography, listing drafting, and dry run fulfillment extend across Days 2-7. The core accounts that must be live before the first order can be fulfilled are covered in 80 minutes.

---

## Sources

- [Stripe vs Square vs PayPal: 2026 Payment Guide — OneNine](https://onenine.com/stripe-vs-square-vs-paypal/)
- [Stripe vs PayPal vs Square: Which Has the Lowest Fees? — GlobalFeeCalculator](https://globalfeecalculator.com/blog/stripe-vs-paypal-vs-square/)
- [USPS vs UPS vs FedEx: 2026 Cost & Speed Comparison — GoBolt](https://www.gobolt.com/blog/usps-vs-ups-vs-fedex-comparison/)
- [USPS 2026 Rate Increases: What Ecommerce Shippers Need to Know — 3PL Center](https://3plcenter.com/usps-2026-rate-increases/)
- [Which Shipping Carrier Is Cheapest? USPS vs UPS vs FedEx — 3PL Center](https://3plcenter.com/cheapest-shipping-carrier/)
- [2026 Parcel Rates: Why Your Costs Could Exceed The 5.9% GRIs — Transportation Insight](https://transportationinsight.com/resources/2026-parcel-rates-why-your-costs-could-exceed-gris/)
- [Freshdesk Pricing & Plans 2026 — Freshworks](https://www.freshworks.com/freshdesk/pricing/)
- [Freshdesk Pricing 2026: The Complete Guide — Desk365](https://www.desk365.io/blog/freshdesk-pricing/)
- [Help Scout vs. Zendesk: A Deep-Dive Comparison — Help Scout](https://www.helpscout.com/compare/zendesk/)
- [Help Scout Pricing 2026 — SaaSWorthy](https://www.saasworthy.com/product/help-scout/pricing)
- [Zendesk Pricing 2026: $19-$169/Agent Plans — CostBench](https://costbench.com/software/help-desk/zendesk/)
- [Etsy Fees Explained: Complete 2026 Breakdown — SellerToolsHQ](https://sellertoolshq.com/guides/etsy-fees-explained/)
