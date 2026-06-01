---
title: "Phase 2 Pricing Negotiation Playbook — ModRun Print Farm"
created: 2026-06-01
status: production-ready
scope: "Wholesale discount strategy, per-unit cost at 4/10/20/50 printer scale, discount tier analysis, lead-time trade-offs, payment terms negotiation, and multi-year volume commitment frameworks for ModRun Phase 2 supplier relationships"
confidence: high
related:
  - PHASE_2_SUPPLIER_RFQ_TEMPLATES.md
  - PHASE_2_CAPITAL_ALLOCATION_TIMELINE.md
  - PHASE_2_SUPPLIER_PRESTAGING_STRATEGY.md
  - MULTI_PRINTER_SCALING_ROADMAP.md
  - PRINTER_FARM_EQUIPMENT_SPECIFICATIONS.md
---

# Phase 2 Pricing Negotiation Playbook — ModRun Print Farm

**Lead finding:** The largest per-unit cost lever available to ModRun in Phase 2 is not printer count — it is filament sourcing. Shifting from retail eSUN ($12–14/kg) to a blended wholesale strategy (eSUN direct at $10/kg + Anycubic $10.49/kg + Polymaker $14.99/kg weighted toward black at eSUN pricing) cuts filament COGS from $1.00–1.05/unit to $0.75–0.84/unit at 75g average weight. On 500 units/month, this saves $80–150/month. On 2,000 units/month (4-printer farm at Phase 2 full), savings reach $320–600/month. Printer hardware pricing has far less negotiation room — Bambu Lab's 5–15% B2B discount on a $399 printer is $20–60/unit, a one-time benefit versus monthly recurring filament savings.

---

## Part 1: Retail vs. Wholesale Pricing Breakdown

### 1.1 Per-Unit COGS at Each Scale Point

The following table assumes 75g average part weight (ModRun cable clip baseline), 80% printer utilization, and blended filament strategies that improve with volume.

| Printer Count | Phase | Filament Strategy | Filament/unit | Platform Fees | Packaging | Shipping | Labor | Total COGS/unit |
|---|---|---|---|---|---|---|---|---|
| 1 (Phase 0) | Etsy launch | eSUN Amazon retail | $1.05 | $3.99 (14.5%) | $0.10 | $4.75 | $0.90 | $8.28 |
| 2 (Phase 1) | 2-printer cluster | eSUN Amazon 10kg bundle | $0.90 | $3.85 (14%) | $0.09 | $4.60 | $0.75 | $8.08 |
| 3–4 (Phase 2 mid) | 3–4 printers | eSUN bundle + Anycubic | $0.82 | $3.85 | $0.08 | $4.50 | $0.65 | $7.80 |
| 4 (Phase 2 full) | 4-printer farm | Blended eSUN/Anycubic/Polymaker | $0.78 | $3.85 | $0.08 | $4.40 | $0.55 | $7.40 |
| 5+ (Phase 3) | 5-printer farm | Polymaker wholesale primary | $0.84 | $3.85 | $0.08 | $4.35 | $0.42 | $7.10 |
| 10 (Phase 3 extended) | 8–10 printers | Polymaker + eSUN direct wholesale | $0.75 | $3.85 | $0.07 | $4.25 | $0.35 | $6.50 |

**Key observations:**
- The jump from 1 to 4 printers saves $0.88/unit in COGS — mainly from filament purchasing efficiency, reduced per-unit labor, and shipping rate improvements
- From 4 to 10 printers, additional savings are $0.90/unit — similar magnitude but delivered over a longer ramp
- Shipping is the most stable COGS line (USPS commercial rates via Pirate Ship are volume-independent at Etsy/Amazon self-fulfillment scale)
- Platform fees are the largest single COGS component and cannot be reduced through negotiation

### 1.2 Revenue and Gross Margin by Printer Count

| Printer Count | Units/Month (80% utilization, demand-capped early) | Gross Revenue at $27.50 AOV | COGS Total | Gross Profit | Gross Margin |
|---|---|---|---|---|---|
| 1 | ~150 (demand-capped) | $4,125 | $1,242 | $2,883 | 69.9% |
| 2 | ~280 (demand-growing) | $7,700 | $2,262 | $5,438 | 70.6% |
| 4 | ~560 (demand-growing) | $15,400 | $4,144 | $11,256 | 73.1% |
| 8 | ~1,100 (demand at traction) | $30,250 | $7,150 | $23,100 | 76.4% |
| 10 | ~1,400 (demand at full traction) | $38,500 | $9,100 | $29,400 | 76.4% |

**Note:** Demand-capped figures reflect realistic Etsy organic growth. At Phase 2 launch (June 2026), demand will constrain output more than printer capacity. By Q4 2026 with established SEO and reviews, 4-printer capacity approaches full utilization.

---

## Part 2: Discount Tier Analysis — What Quantities Unlock What Pricing

### 2.1 Printer Hardware Discounts

**Bambu Lab P1S ($399 base, $649–750 Combo):**

| Purchase Volume | Channel | Discount | Notes |
|---|---|---|---|
| 1–3 units | US Store retail | 0% | MSRP; may catch sale events |
| 3–9 units | B2B inquiry | 5–8% est. | Not published; negotiated per rep |
| 10+ units | B2B + volume commitment | 10–15% est. | Requires multi-tranche plan framing |
| Bundle w/ consumables (MatterHackers) | Farm bundle pricing | Variable | Compare vs. a-la-carte pricing |

**Discount value in dollars at P1S pricing:**
- 5% on $399 = $20/unit — negligible vs. the $100–150 warranty value of MatterHackers
- 10% on $399 = $40/unit — modest; at 10 units saves $400 total
- MatterHackers 2-year extended warranty = ~$100–150/printer in avoided repair risk — the more valuable benefit

**Conclusion on printer hardware negotiation:** Do not spend significant time negotiating printer price. The 2-year warranty from MatterHackers is worth more than any realistic discount from Bambu direct. Purchase from MatterHackers, frame as a multi-tranche buyer, and accept whatever modest pricing they offer.

---

### 2.2 Filament Discount Tiers — The Primary Negotiation Target

#### eSUN PLA+ (Primary Commodity Source)

| Volume Tier | Channel | Price/kg | Threshold | Notes |
|---|---|---|---|---|
| Single spool | Amazon retail | $15–20 | 1 spool | No negotiation |
| 10kg case bundle | Amazon bundle | $11–13 | 10kg minimum | Operational sweet spot for Phase 0–2 |
| 25kg+ | eBay wholesale lots | $9–12 | 25kg minimum | Variable availability; no guaranteed restocking |
| 40–60 kg/month committed | eSUN direct wholesale | $8.50–10 | 12-month commitment letter | Best commodity price; requires relationship |
| 80–100 kg/month committed | eSUN direct (negotiated) | $8–9 | 12-month; quantity guarantee | Theoretical ceiling of eSUN direct pricing |

**Volume thresholds that matter:**
- 10kg/order: The Amazon bundle tier — no outreach, just purchase
- 40 kg/month sustained: The trigger for initiating eSUN direct wholesale conversation
- 12-month commitment letter: The key that unlocks sub-$10/kg pricing from eSUN direct

#### Polymaker PolyLite PLA (Premium Tier)

| Volume Tier | Channel | Price/kg | Threshold | Notes |
|---|---|---|---|---|
| Under $1,000 order | Retail shop.polymaker.com | $20–24 | No minimum | Do not use for production volumes |
| $1,000–$2,999 order (~67–200 kg) | Wholesale portal | $14.99 + shipping | $1,000 MOQ | Baseline wholesale; shipping ~$25–60 |
| $3,000+ order (~200+ kg) | Wholesale portal | $14.99 + free shipping | $3,000 MOQ | Effective $14.99/kg net |
| 50+ kg/month sustained commitment | Negotiated via support.na | $13.50–14.25 est. | Volume letter | 5–10% additional off wholesale base |
| 100+ kg/month sustained | Strategic account | $13–13.50 est. | Long-term agreement | Top negotiated tier; requires 6-month history |

**Volume thresholds that matter:**
- $1,000 single order (~67 kg): Access to wholesale pricing
- $3,000 single order (~200 kg): Free shipping threshold; effective lowest cost per kg
- 50 kg/month sustained: The trigger for volume discount negotiation conversation
- 100 kg/month sustained: The reference customer threshold; enables co-marketing and strategic account treatment

#### Anycubic PLA Basic (Pallet Hedge)

| Volume | Price | Price/kg | Notes |
|---|---|---|---|
| 10–20kg bundle | ~$104.99 | ~$10.50 | Online purchase, no negotiation |
| 50kg pallet | ~$524.73 | $10.49 | Evergreen sale pricing — no negotiation needed |
| 100kg | Not publicly listed | ~$9–10 est. | Contact Anycubic sales for quote |

**Anycubic strategy:** No negotiation is needed or available at pallet level. The $10.49/kg is effectively the public floor price. Use as a quarterly hedge order to buffer against eSUN stockouts.

---

### 2.3 Blended Filament Cost Optimization by Phase

**Phase 2 (4 printers, ~50 kg/month):**

Recommended blend: 60% eSUN Amazon bundles + 25% Anycubic 50kg pallet + 15% Polymaker (white/grey only)

| Vendor | Volume Share | Price/kg | Weighted Cost |
|---|---|---|---|
| eSUN Amazon 10kg bundles | 60% (30 kg) | $12/kg | $7.20/kg |
| Anycubic 50kg pallet | 25% (12.5 kg) | $10.49/kg | $2.62/kg |
| Polymaker wholesale | 15% (7.5 kg) | $14.99/kg | $2.25/kg |
| **Blended cost** | 100% | | **$12.07/kg** |
| Cost/unit at 75g | | | **$0.91/unit** |

**Phase 3 (8 printers, ~100 kg/month, Polymaker activated as primary):**

Recommended blend: 40% eSUN direct + 25% Anycubic + 35% Polymaker

| Vendor | Volume Share | Price/kg | Weighted Cost |
|---|---|---|---|
| eSUN direct wholesale | 40% (40 kg) | $9.50/kg | $3.80/kg |
| Anycubic 50kg pallet | 25% (25 kg) | $10.49/kg | $2.62/kg |
| Polymaker wholesale | 35% (35 kg) | $14.99/kg | $5.25/kg |
| **Blended cost** | 100% | | **$11.67/kg** |
| Cost/unit at 75g | | | **$0.88/unit** |

**Monthly filament savings vs. all-retail baseline ($16/kg retail average):**
- Phase 2 blended ($12.07): saves $3.93/kg × 50 kg = **$197/month**
- Phase 3 blended ($11.67): saves $4.33/kg × 100 kg = **$433/month**

---

## Part 3: Lead-Time Trade-Offs

### 3.1 Printer Hardware Lead Times

| Supplier | Lead Time (in-stock) | Lead Time (custom/bundle) | Expedite Option | Cost of Delay |
|---|---|---|---|---|
| Bambu Lab B2B | 3–7 business days | 2–3 weeks (high demand) | None (no paid expedite) | 1 week idle = ~$1,400 lost gross profit at 4-printer Phase 2 run rate |
| MatterHackers | 3–7 business days | 1–2 extra weeks (custom bundle) | Call sales; limited inventory | Same as above |
| Dynamism | 3–7 business days (in-stock) | — | Call sales; may have warehouse stock | Same |
| Micro Center (backup) | Same-day (in-store pickup) | N/A | 25+ US locations | Emergency fill; retail price, no discount |

**Trade-off conclusion:** Standard lead times are acceptable. Never delay a printer purchase to wait for a volume discount that saves $20–60 — one week of delayed 4-printer operation costs $1,400 in gross profit. Order at the phase trigger, not when "the price is right."

**High-demand periods to avoid:** Post-new-model launch, back-to-school (August), and Black Friday windows may push lead times from 3–7 to 2–3 weeks. If procuring in August, order by August 1 to avoid back-to-school stock pressure.

### 3.2 Filament Lead Times and Ordering Cadence

| Supplier | Standard Lead Time | Out-of-Stock Risk | Buffer Stock Needed | Order Cadence |
|---|---|---|---|---|
| eSUN Amazon Prime | 2–5 days | 2–4 times/year on specific colors | 2-week supply minimum | Weekly auto-order when below threshold |
| Anycubic direct | 3–7 days | Low for black; moderate for specialty | 2-week buffer on validated colors | Quarterly 50kg pallet |
| Polymaker wholesale | 3–5 days (Houston) | Low — domestic warehouse | 3-week buffer (given MOQ) | Monthly order at Phase 2+; quarterly at $3,000+ |
| eSUN direct wholesale | 2–3 weeks | Low once relationship established | 4-week buffer (longer lead time) | Monthly on standing order |

**Expedite cost on filament:** There is no paid expedite option with filament suppliers. The expedite is "have safety stock" — buffer inventory is the only insurance against a production stoppage. At 4-printer Phase 2 (50 kg/month), maintain a minimum 20 kg on-hand buffer at all times. Reorder at 20 kg to target 40 kg before the order arrives.

**Shipping cost trade-off (Polymaker):**
- Orders under $3,000: ~$25–60 shipping from Houston; effective cost ~$15.37–15.89/kg
- Orders over $3,000 (200+ kg): free shipping; effective cost $14.99/kg
- The $0.38–0.90/kg shipping premium on sub-$3,000 orders is offset by not overbuying inventory. At Phase 2 (50 kg/month), a $1,000 order (~67 kg) arrives at ~$15.66/kg effective. Acceptable.
- At Phase 3 (100 kg/month), a 2-month $2,000 order is approaching the free-shipping threshold; quarterly $3,000+ orders unlock free shipping and save $75–180 per order.

---

## Part 4: Payment Terms Negotiation

### 4.1 Payment Terms Framework by Supplier

| Supplier | Default Terms | Net-30 Available | Path to Net-30 | Value of Net-30 at Phase 2 |
|---|---|---|---|---|
| Bambu Lab B2B | Credit card | Yes (qualified business accounts) | Business documentation + B2B portal approval | $400–800/month float (printer tranches) |
| MatterHackers | Credit card | Yes (contact sales) | Request via sales@matterhackers.com; PO process | $1,200–2,000/tranche deferred |
| Dynamism | Credit card | Yes (qualified accounts) | Contact sales@dynamism.com | Same as MatterHackers |
| Polymaker wholesale | Credit card / PayPal / BNPL | Yes (after 2–3 prepaid orders) | Email support.na@polymaker.com after 3rd order | $1,000–2,000/month float at Phase 3 |
| eSUN Amazon | Credit card | No | N/A — Amazon does not offer net-30 | N/A |
| eSUN direct | Credit card | Yes (established US accounts) | 6-month history + request | $400–600/month float |
| Anycubic | Credit card | No | N/A — storefront only | N/A |

**Cash flow value of net-30 at Phase 2 scale (4 printers, $1,500–2,000/month in supply spend):**
- Net-30 on a $1,000/month Polymaker order = $1,000 in float each month
- This float covers 6–8 weeks of eSUN Amazon purchases or one printer tranche deposit
- Net-30 is worth pursuing aggressively with Polymaker (achievable after 3 orders) and eSUN direct (achievable after 6 months of volume)

**Net-30 negotiation sequence:**
1. Pay first 2–3 Polymaker orders on time via credit card (June–August)
2. In Month 3 (August), email support.na@polymaker.com: "We've placed 3 prepaid orders totaling $X. We'd like to request net-30 payment terms for our ongoing monthly orders. Our payment history shows consistent on-time payment. What documentation do you need?"
3. With eSUN direct: same approach but after 4–5 months of direct relationship
4. With MatterHackers: request net-30 at the time of Tranche 2 purchase (July) — the Tranche 1 history establishes credibility

---

### 4.2 Upfront Discount vs. Net-30 Trade-Off

Some suppliers offer a small discount (1–2%) for early payment or prepayment in lieu of net-30 terms. The trade-off:

- 2% early-pay discount on a $1,000/month Polymaker order = $20/month saved in exchange for $1,000 in tied-up working capital
- If working capital earns 5% annual return (conservative), $1,000 in float is worth $50/year = $4.17/month
- The $20/month early-pay discount exceeds the $4.17 opportunity cost → take the discount if offered
- If Polymaker does not offer an early-pay discount (not currently documented), pursue net-30 for cash flow

**Recommendation:** Pursue net-30 from Polymaker and eSUN direct as the primary working capital lever. Do not sacrifice net-30 for a small early-pay discount unless the discount exceeds 1.5%.

---

### 4.3 Payment Terms Summary Script (Polymaker)

**When:** After 3rd prepaid Polymaker order (approximately August 2026)

**Script for support.na@polymaker.com:**

"Hi [Contact Name], we've now placed three orders totaling approximately $3,000 in PolyLite PLA, all paid on time. We're projecting $1,000–1,500 per month in Polymaker orders as our farm scales to 8 printers. We'd like to formally request net-30 payment terms going forward. What information do you need from us — business entity documentation, bank references, or something else? We're ready to provide whatever is standard for your wholesale program."

---

## Part 5: Multi-Year Volume Commitments

### 5.1 When to Commit vs. When to Stay Flexible

**Guiding principle:** Do not commit to minimum volume agreements before demand confirms the floor. A 12-month eSUN commitment at 40 kg/month is only appropriate when you have 2–3 consecutive months of actual 40 kg/month consumption.

**Commitment timeline:**
- Month 1–2 (June–July 2026): Zero commitments; Amazon-based purchasing only
- Month 3 (August 2026): Initiate eSUN direct conversation; no commitment yet — gather quote
- Month 4 (September 2026): If demand confirms 40 kg/month for 2 straight months, commit to 6-month eSUN direct standing order
- Month 6 (November 2026): Convert eSUN 6-month to 12-month if pricing is favorable; initiate Polymaker net-30 and 6-month forward projection
- Month 9 (February 2027): If Phase 3 (8+ printers) is operational and 100 kg/month confirmed, negotiate the strategic Polymaker account ($13–13.50/kg tier)

### 5.2 Equipment Lease vs. Purchase Analysis

**Conclusion up front:** Purchase, do not lease. Bambu P1S at $399 has a 4–8 week payback period. Leasing adds 15–25% total cost over a standard 24-month term and introduces early-termination penalties that constrain scaling decisions.

**Numbers:**
- Purchase price: $399
- Incremental monthly net income per printer: $1,800–2,800 at Phase 2 demand levels
- Payback period: 1.5–2.5 months
- Equivalent 24-month lease payment (if available): ~$18–22/month = $432–528 total — more than purchase price with 2+ months to pay off
- Any leasing arrangement that costs more than $399 over any period is economically inferior to outright purchase

**When leasing might make sense:** Only if capital is truly constrained and you cannot access $399 from Phase 1 revenue or a personal credit line. In that scenario, a business line of credit at 8–12% APR (common for LLC/sole proprietors) costs approximately $32–48 total interest over 12 months on a $399 draw — far cheaper than a lease structure. Use a business credit card or LOC, not a printer lease.

### 5.3 SimplyPrint Software Commitment

**Monthly vs. Annual pricing comparison:**

| Plan | Monthly | Annual (monthly equivalent) | Annual Savings |
|---|---|---|---|
| Starter (up to 10 printers) | $10/month | ~$8.33/month (est., if annual option exists) | ~$20/year |
| Print Farm (unlimited) | $31.49/month | ~$26.24/month (est.) | ~$63/year |

**Recommendation:** Start on monthly billing until Phase 2 (4 printers) is confirmed stable for 60+ days. Switch to annual at Phase 3 (8 printers) to save $75+ per year. The savings do not justify annual commitment risk if you are still validating the software stack.

**Printago evaluation:** The free tier (unlimited printers, 1 concurrent slot) is the evaluation path. Do not commit to the $29/month paid tier until Etsy-to-queue automation has been tested and confirmed to save 30+ minutes per day of operator time. Run Printago free alongside SimplyPrint for 30 days before deciding.

---

## Part 6: Negotiation Leverage Points by Phase

### 6.1 Phase 2 (4 Printers, June–September 2026)

**Available leverage:**
- Multi-tranche framing: "This is the first of three purchases; we plan 8 total printers by Q4."
- Payment history: After 3 Polymaker orders, net-30 terms are accessible
- Volume projection letters: Credible 3-month forward projections open discount conversations

**Realistic outcomes:**
- MatterHackers: 2-year warranty (primary win), 0–5% price improvement
- Bambu B2B: 5–10% discount on 4+ unit purchase if the rep is responsive
- Polymaker: No additional discount at Phase 2 volumes ($14.99/kg is already the wholesale base); net-30 after 3 orders is the win
- eSUN Amazon: No negotiation; maintain 10kg bundle cadence

### 6.2 Phase 3 (8 Printers, October 2026 onward)

**Available leverage:**
- Demonstrated 6-month purchase history with Polymaker
- Confirmed 100 kg/month consumption (represents ~$18,000/year in Polymaker revenue)
- Reference customer status — Polymaker case study offer is real leverage for $1/kg discount

**Realistic outcomes:**
- Polymaker: 5–10% volume discount at 100 kg/month ($13.50–14.25/kg vs. $14.99 base) = saves $75–150/month = $900–1,800/year
- eSUN direct: $9–10/kg on 12-month standing order at 40–60 kg/month = saves $2–4/kg vs. Amazon bundles = $80–240/month
- Combined Phase 3 filament savings vs. all-Amazon baseline: $150–400/month

### 6.3 What Not to Negotiate

**Do not spend time negotiating:**
- eSUN Amazon pricing: It is non-negotiable; the bundle price is the price
- Anycubic pallet pricing: It is effectively fixed at $10.49/kg
- Bambu Lab warranty extension: MatterHackers' 2-year warranty is the better path than negotiating with Bambu direct
- Software subscriptions: The monthly cost of SimplyPrint ($10) and Printago ($29) are already minimal; discount requests will not be honored

---

## Part 7: Negotiation Scripts and Key Phrases

### 7.1 Multi-Tranche Framing (Printer Vendors)

"We are procuring this tranche as the first of three planned purchases — 4 units in June, 2–3 additional in July, and a final batch of 2–3 to reach 8–10 total by Q4. We are treating this supplier relationship as a long-term partnership, and we are giving you first right of refusal on all tranches. What can you offer on pricing and terms to make this the right choice?"

### 7.2 Volume Commitment Framing (Filament Vendors)

"We are projecting X kg/month across three colors for the next 12 months, which is $Y annually in purchases. I am willing to put that in a letter of intent in exchange for locked pricing at $Z/kg. What can you offer?"

### 7.3 Net-30 Request Framing

"We have now placed [N] orders totaling $X, all paid on time. Our monthly purchasing is growing and we would like to establish net-30 terms to manage our working capital as we scale. What does your qualification process look like?"

### 7.4 Quality Discount Framing (If Batch Failure Occurs)

"We received a shipment in lot [batch number] that showed [failure mode] affecting [X]% of our production run. We would like a credit toward the next order and confirmation that this batch has been reviewed by your QC team. What is your process for handling documented production failures?"

---

## Sources

- [Bambu Lab B2B Corporate Sales](https://bambulab.com/en/corporate-sales)
- [Bambu Lab P1S Pricing — Original Pricing Tracker](https://originalpricing.com/bambu-lab-printer-prices/)
- [Polymaker US Wholesale Portal](https://us-wholesale.polymaker.com/)
- [Polymaker Wholesale FAQ](https://us-wholesale.polymaker.com/pages/wholesale-faq)
- [Polymaker Print Farm Program](https://us-wholesale.polymaker.com/pages/wholesale-filament-for-print-farms)
- [Anycubic PLA Basic 50–100kg Deals](https://store.anycubic.com/products/pla-basic-50-100kg-deals)
- [ADP Industries: Best Filament for Bambu Lab Printers 2026](https://www.adpindustries.com/blog/best-filament-bambu-lab-2026/)
- [Printago vs SimplyPrint Comparison](https://printago.io/alternatives/simplyprint)
- [SimplyPrint Pricing 2026](https://simplyprint.io/pricing)
- Internal: MULTI_PRINTER_SCALING_ROADMAP.md (Section 2.1 — hardware economics), phase-2-supplier-research.md (Section 5 — negotiation strategy), PHASE_2_SUPPLIER_PRESTAGING_STRATEGY.md (Section 3 — per-unit economics matrix), scaling-cost-model.csv
