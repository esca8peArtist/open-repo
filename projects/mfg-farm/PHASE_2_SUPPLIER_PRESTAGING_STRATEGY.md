---
title: "Phase 2 Supplier Pre-Staging Strategy — ModRun Print Farm"
created: 2026-05-30
status: execution-ready
scope: "June 1–15 outreach execution, supplier account establishment, volume pricing negotiation, inventory pre-staging for August–September production ramp to 8-printer farm"
confidence: high
related:
  - BAMBU_LAB_FARM_SUPPLIER_CONTACTS.md
  - phase-2-supplier-research.md
  - POLYMAKER_WHOLESALE_ONBOARDING_GUIDE.md
  - MULTI_PRINTER_FARM_ARCHITECTURE.md
  - 8-printer-farm-cost-model.md
  - PHASE_2_CAPITAL_DEPLOYMENT_TIMELINE.md
  - post-test-print-doc-5-supplier-contact-matrix.md
  - PRINTER_FARM_EQUIPMENT_SPECIFICATIONS.md
independence_note: "This pre-staging work is INDEPENDENT of May 30 test print outcome. Supplier relationships and account establishment proceed regardless — they serve Phase 2 regardless of Phase 1 pass or fail."
---

# Phase 2 Supplier Pre-Staging Strategy — ModRun Print Farm

**Lead finding:** Phase 2 supplier pre-staging requires three parallel tracks executed simultaneously in June 1–15: (1) printer hardware — contact MatterHackers and Bambu Lab B2B for 3–4 P1S unit quotes, locking in lead times before Q3 demand spikes make availability unpredictable; (2) filament — register Polymaker wholesale, place an Anycubic 50kg sample, and establish the eSUN direct wholesale relationship, which together will cut blended filament cost from $12–14/kg to $10–11/kg at 8-printer volumes; and (3) consumables — build the predictive maintenance parts inventory that prevents one nozzle clog from idling an 8-printer cluster for 24+ hours. None of these tracks require the May 30 test print to succeed. They serve any Phase 2 scenario.

**Phase 2 target:** 8-printer P1S farm producing 2,000–2,400 units/month, blended COGS $6.50–7.50/unit, gross margin 70%+, with zero supply chain lag at the August–September production ramp. The operational window that risks supply delay without this pre-staging: July 15 – August 30, when Etsy Q4 demand acceleration coincides with the printer expansion tranche and most commodity filament suppliers take 7–14 days to fulfill bulk orders.

---

## Section 1: Supplier Landscape Analysis

### 1.1 Printer Manufacturers

#### Bambu Lab (Primary Platform)

ModRun's entire farm is Bambu P1S. The P1S is the only recommended fleet printer through Phase 3: uniform gcode profiles, shared spare parts kit, AMS 2 Pro multi-color ecosystem, and a 9.5/10 reliability score from print farm community data. No mixing with Creality K2 Plus (CFS reliability issues) or Prusa MK4S (25% slower throughput, no Bambu Farm Manager integration).

**Current pricing (May 2026):** P1S base $399 MSRP (was $699 at launch). P1S Combo with AMS 2 Pro: $649–$750 depending on retailer and sale timing.

**B2B Direct channel:** bambulab.com/en/corporate-sales — accepts formal purchase orders, tax-exempt setup, net-30 for qualified business accounts. Volume discount expectation for 10+ units: 5–15% off list, negotiated per inquiry. Lead time: 3–7 business days in-stock, 2–3 weeks during demand spikes.

**Account type:** B2B portal is wholesale-equivalent. No public tiered pricing; all volume pricing is quote-based. Submit inquiry framed as "production print farm build-out, planning 10 P1S units across 3 tranches (June, July, August)."

**Minimum order quantity:** No formal MOQ on B2B portal. PO format accepted for any quantity.

---

#### MatterHackers (Primary US Distributor, Recommended)

MatterHackers is the only US Bambu Lab distributor with formally packaged print farm bundles. For Phase 2, they are the preferred printer procurement channel because the 2-year extended warranty (vs. 1-year Bambu direct) and the included setup training hours justify a modest per-printer premium.

**Print farm bundles (confirmed structure, May 2026):**
- 6-Printer bundle: 6 printers + hotend assemblies + PEI plates + 48 spools MH Build PLA + 3 hours setup guidance + 2-year warranties. Pricing range: $28,900–$174,900 for X1C configuration. P1S equivalent is significantly lower — contact sales for current P1S farm bundle price.
- 12-Printer bundle: 12 printers + proportional consumables + 6 hours setup guidance + 2-year warranties.

**Contact:** sales@matterhackers.com | +1 (800) 613-4290

**Account type:** Business account with PO invoicing available on request. No formal wholesale program distinct from retail; pricing advantage comes from the bundle structure.

**Lead time:** In-stock items 3–7 business days. Custom bundle configuration adds 1–2 weeks.

**Payment terms:** Credit card standard. PO-based purchasing available by request to sales team.

**Phase 2 procurement recommendation:** Purchase Tranche 1 (3–4 P1S units) through MatterHackers to get the 2-year warranty. At $399 per printer and estimated $100–150 per-printer warranty value, the MatterHackers bundle is cost-neutral or better vs. Bambu direct over a 2-year production cycle.

---

#### Dynamism (Enterprise Backup Channel)

Dynamism is the national 3D printer specialist with 25+ years of enterprise sales history and visibility into Bambu Lab's US allocation pipeline. Use Dynamism if MatterHackers cannot fulfill a specific tranche on schedule.

**Contact:** sales@dynamism.com | 1-800-711-6277

**Account type:** Enterprise accounts with dedicated contact, PO support.

**Value:** Dynamism holds US warehouse stock on popular Bambu SKUs and can flag upcoming stock events or model transitions. For Phase 2 Tranche 3 (July–August, 4 additional units), Dynamism is the fallback if MatterHackers is backlogged.

---

#### Prusa (Contingency Only)

Prusa i3 MK4S ($799, $549 kit) is the repairability hedge if Bambu hardware supply becomes a risk — tariff-driven import restriction, new model cannibalization causing P1S discontinuation, or a quality recall. Prusa's fully open-source, user-serviceable design makes it the most resilient platform long-term. Do not mix with the Bambu fleet at Phase 2; introduce only as replacement for failed printers if Bambu parts become unavailable.

Not recommended for new procurement in Phase 2. Exists on this list for scenario planning.

---

#### Creality (Not Recommended)

The Creality K2 Plus ($649–799) has a 350×350mm build volume that is wasted on cable clips, a CFS multi-color system with documented high-duty-cycle reliability issues, and 300–500 hour nozzle wear intervals versus P1S's 600–800 hours. It requires a separate Klipper/Moonraker monitoring stack that fragments the software environment. Excluded from Phase 2 consideration.

---

### 1.2 Filament Vendors

#### eSUN (Primary, Phases 0–3)

**Why primary:** Most consistently documented commodity brand for Bambu P1S/X1C AMS compatibility in 2026. Diameter tolerance ±0.03mm. Zero AMS feed errors on multi-hour jobs. Amazon Prime delivery means a 24-hour stockout pivot is always available.

**Pricing tiers (May 2026, PLA+, 1.75mm):**

| Volume | Channel | Price/kg | Notes |
|---|---|---|---|
| 1 spool (1kg) | Amazon retail | $15–20 | Varies by color |
| 10 spools (10kg) | Amazon bundle | $11–13 | Prime shipped; operational sweet spot |
| 25+ kg | eBay wholesale listings | $9–12 | Variable availability |
| 50+ kg/month | esun3dstore.com direct | Quote required | 2-week response; allow lead time |
| 12-month commitment (40–60 kg/month) | eSUN direct wholesale | $8.50–10/kg | Requires volume commitment letter |

**MOQ:** No minimum on Amazon. Direct wholesale requires volume commitment letter to unlock pricing negotiation.

**Lead time:** Amazon Prime 2–5 days. eSUN direct 2–3 weeks.

**Volume discount structure:** Amazon bundles have no negotiation. eSUN direct reps have ~15% discretionary discount authority below listed bulk pricing. A 12-month commitment at 40–60 kg/month is required to access $8.50–10/kg tier.

**Payment terms:** Amazon: credit card. eSUN direct: net-30 available for established US accounts.

**Account type:** No wholesale account required for Amazon. Direct wholesale requires contact via esun3dstore.com wholesale inquiry form.

**AMS compatibility:** Excellent (9/10 reliability). Weakness: batch-to-batch color variation visible over months, moisture packaging less rigorous than Polymaker.

---

#### Polymaker (Premium Tier, Phase 2 Activation)

**Why activate in Phase 2:** Polymaker wholesale is the strongest premium-tier filament program for print farm operators in 2026. ±0.02mm diameter tolerance, vacuum-sealed foil bags with desiccant, published certificates of analysis on request, and Bambu AMS certification mean batch QC is predictable across 5–10 printers. The $0.30/unit premium over eSUN at 75g/unit is offset by fewer failed prints, better review-visible surface quality on white/grey, and tariff immunity (US-warehoused in Houston, TX).

**Pricing tiers (May 2026, PolyLite PLA wholesale):**

| Volume/Order | Price/kg | Threshold | Notes |
|---|---|---|---|
| $1,000 minimum order (~67kg) | $14.99/kg | MOQ | Shipping calculated at checkout |
| $3,000+ order (~200kg) | $14.99/kg + free shipping | Free shipping threshold | Effective $14.99/kg |
| Sustained 50kg/month commitment | Negotiable 5–10% below base | Contact support.na@polymaker.com | Discretionary rep authority |

**MOQ:** $1,000 per order (~67kg at $14.99/kg). Below this threshold, purchase retail at shop.polymaker.com.

**Lead time:** 3–5 business days from Houston warehouse.

**Payment terms:** Credit card, PayPal, BNPL (Shopify checkout). Net-30 available after 2–3 prepaid orders; request from support.na@polymaker.com.

**Account type:** Wholesale account — self-service registration at us-wholesale.polymaker.com, no approval wait, no cost.

**Activation timing for ModRun:** Register account now (June 1). Place first $1,000 trial order in Month 3 (when 50kg/month production is confirmed and the order represents 2–3 weeks of supply, not 6 months). Use for white and grey only initially; continue eSUN for black.

---

#### Anycubic (Backup/Pallet Hedge)

**Why maintain:** Anycubic is the only commodity-tier brand with a publicly listed 50kg/100kg bulk deal requiring no wholesale account. At $10.49/kg for 50kg, it is the lowest publicly accessible filament price in the US market for this volume tier. Use as the quarterly hedge against eSUN stock-outs and price spikes.

**Pricing tiers (May 2026, PLA Basic direct store):**

| Volume | Sale Price | $/kg | Notes |
|---|---|---|---|
| 10–20kg bundle | $104.99 | ~$10.50 | Verify current sale status |
| 50kg bundle | $524.73 | $10.49 | Effectively evergreen sale pricing |
| 100kg | Quote varies | ~$9–10 est. | Not publicly listed |

**MOQ:** No MOQ — purchase directly online.

**Lead time:** 3–7 business days, 24-hour dispatch from Anycubic warehouse.

**Payment terms:** Credit card only. No net-30 for storefront orders.

**AMS compatibility:** 7/10 — occasional winding issues. Test with a 10kg sample before committing to 50kg pallet. Use Refill (cardboard spool) format to reduce winding complaints.

**Risk:** AMS winding inconsistency is the primary concern. Validate with sample order placed by June 15, result evaluated by June 22, before treating Anycubic as confirmed secondary.

---

#### Overture (PETG Primary, PLA Backup)

**Why maintain:** Overture has the strongest PETG track record for Bambu AMS in 2026, making it the designated primary PETG supplier when ModRun expands to heat-adjacent products or premium-tier SKUs. For PLA, use as a same-day Amazon Prime fill when eSUN's specific color is out of stock.

**Pricing (May 2026):**

| Product | Amazon | Wholesale (direct) |
|---|---|---|
| PLA 1.75mm | $11–14/kg (10kg bundle) | Up to 35% off via overture3d.com/pages/wholesale |
| PETG 1.75mm | $17–19/kg | Quote required |

**MOQ:** No minimum on Amazon. Wholesale program requires direct contact.

**AMS compatibility:** PLA 8/10, PETG 9/10. Best-tested PETG option for Bambu printers per community data.

---

#### MatterHackers Build Series PLA (Domestic Secondary)

**Why maintain:** MatterHackers' own filament brand (NatureWorks 4043D Ingeo PLA, domestically sourced) provides a second domestic supply channel alongside Polymaker, with no MOQ requirement and free shipping on orders over $35. Use for color variants not available at Polymaker, or as surge fill when Polymaker orders are in transit.

**Pricing (May 2026):** $19–23/kg retail, wholesale pricing available via business account. Not cost-competitive with commodity brands at primary volumes, but zero-MOQ structure makes it ideal for 2–5 spool gap fills.

---

#### SUNLU (Color Sampling Only)

**Why maintain:** SUNLU's mix-and-match bulk option (6 spools minimum, any color combination) is operationally useful for testing new color velocity before committing to a 10kg eSUN case. Not suitable for primary production due to AMS winding inconsistencies on multi-spool jobs.

**Pricing (May 2026):** $12–14/kg for 6kg mix-and-match bundles. Reseller tier at $10–12/kg available with 50-box initial order (contact support@3dsunlu.com).

**Use case:** Order one 6kg SUNLU bundle in any new specialty color before committing to 10kg eSUN. If velocity confirms demand, switch to eSUN for that color.

---

### 1.3 Consumables — Nozzles, Bed Surfaces, Heating Elements

These suppliers are not vendor relationships requiring outreach — they are Amazon/Bambu direct channels where the action is bulk stocking, not negotiation.

**Nozzle suppliers (Bambu P1S, 0.4mm hardened steel):**

| Source | Unit Cost | Pack Options | Notes |
|---|---|---|---|
| Bambu Lab official store (us.store.bambulab.com) | $3–5 each | Single, 5-pack | Genuine hardened steel; direct compatibility guaranteed |
| Amazon compatible brands | $8–15 for 5-pack | 5-pack standard | Community-confirmed compatible; ±5% quality variance |

**Wear interval:** 600–800 print hours per nozzle. At 8 printers × 320 production hours/month = 2,560 printer-hours/month. Fleet consumes approximately 3–4 nozzles per month. Safety stock target: 24 nozzles (6-month supply). Cost: $72–120. Reorder when below 12.

**Bed surface (Bambu P1S PEI sheet):**

| Source | Unit Cost | Notes |
|---|---|---|
| Bambu Lab official store | $30–40/sheet | Exact fit; 9–12 months at production duty cycle |
| Amazon compatible PEI sheets | $20–30/sheet | Check dimensional fit; some warping reports at full production |

**Safety stock target:** 2 sheets per printer (16 sheets for 8-printer farm). Replace at 9-month intervals or when adhesion spots appear. Annual fleet cost: $480–640.

**Heating cartridge and thermistor:**

| Part | Bambu source cost | Replacement interval | 8-printer annual cost |
|---|---|---|---|
| Heating cartridge | $8–12 | 1,500–2,000 hours | $32–48 |
| Thermistor | $6–10 | 2,000+ hours | $24–40 |

**PTFE tube (hotend section):**

| Source | Cost | Interval | 8-printer annual cost |
|---|---|---|---|
| Bambu official / Amazon | $5–8/tube | 800–1,000 hours | $40–64 |

**Phase 2 minimum parts inventory (8-printer fleet):**

| Part | Stock Level | Cost | Reorder At |
|---|---|---|---|
| Nozzle 0.4mm hardened | 24 units | $72–120 | Below 12 |
| Heating cartridge | 8 units | $64–96 | Below 4 |
| Thermistor | 8 units | $48–80 | Below 4 |
| PTFE tube (hotend) | 8 tubes | $40–64 | Below 4 |
| PEI bed sheet | 4 sheets | $120–160 | Below 2 |
| Drive belt (XY set) | 4 sets | $60–100 | Below 2 |
| Extruder drive gear | 4 units | $40–60 | Below 2 |
| **Total fleet parts inventory** | | **~$444–680** | |

The $600 parts investment prevents 24+ hours of cluster downtime per year. One day of 8-printer idle time at 200 units/day × $15 net = $3,000 in lost revenue. Carrying cost of $150/year vs. $3,000 downtime risk makes this a mandatory operating expense from Phase 2 day one.

---

## Section 2: Pre-Staging Timeline

### Phase Windows and Logic

The pre-staging strategy operates on three overlapping windows chosen deliberately so that no action depends on the May 30 test print result.

**Why this is test-print-independent:** Supplier accounts, volume pricing negotiations, and sample orders build the infrastructure for Phase 2 regardless of whether Phase 1 succeeds quickly or slowly. If Phase 1 fails and the product needs a redesign, the supplier relationships established in June are still valid for re-launch. If Phase 1 succeeds faster than projected (optimistic scenario: $1,500/month revenue by Month 1–2), the supplier network is already in place to support Tranche 1 printer purchases without a 2-week outreach lag.

---

### Window 1: June 1–15 — Account Establishment and Quote Requests

**Goal:** Establish the business relationships before you need them. No commitments, no orders — just accounts, quotes, and introductions.

| Date | Action | Vendor | Owner | Time Required |
|---|---|---|---|---|
| June 1 | Register Polymaker wholesale account (free, instant) | Polymaker | Thorn | 15 min |
| June 1 | Email MatterHackers for 4-unit P1S quote (see template in Section 4) | MatterHackers | Thorn | 20 min |
| June 1 | Submit Bambu Lab B2B inquiry for 3 P1S units | Bambu Lab B2B portal | Thorn | 20 min |
| June 1 | Order 30kg eSUN PLA+ via Amazon (10kg black, 10kg white, 10kg grey) | Amazon | Thorn | 10 min |
| June 3 | Email support.na@polymaker.com introducing ModRun + requesting PolyLite PLA white/grey sample | Polymaker | Thorn | 15 min |
| June 3 | Order Anycubic 10kg test sample (verify AMS compatibility before 50kg commitment) | Anycubic direct | Thorn | 10 min |
| June 5 | Follow up with MatterHackers if no quote response (call +1 800-613-4290) | MatterHackers | Thorn | 10 min |
| June 7 | Email eSUN direct wholesale inquiry with monthly volume projection (see template in Section 4) | esun3dstore.com | Thorn | 20 min |
| June 8 | Request Dynamism quote for 4-unit P1S as price comparison benchmark | Dynamism | Thorn | 15 min |
| June 10 | Evaluate Anycubic test sample on P1S (AMS feed test, dimensional check) | — | Thorn | 2 hrs |
| June 10 | Email Overture wholesale inquiry for PETG pricing (future Phase 2 SKU expansion) | overture3d.com | Thorn | 15 min |
| June 12 | Confirm printer procurement decision: MatterHackers vs. Bambu B2B vs. Dynamism | All three | Thorn | 30 min |
| June 15 | Place printer Tranche 1 pre-order (3–4 P1S units) with winning vendor | MatterHackers (pref.) | Thorn | 30 min |
| June 15 | Log all supplier quotes and relationships in contact matrix | — | Thorn | 30 min |

**Expected outcomes by June 15:**
- Polymaker wholesale account active, sample requested
- MatterHackers and Bambu B2B quotes in hand for 3–4 printer purchase
- Anycubic AMS compatibility validation complete (pass/fail)
- eSUN direct wholesale conversation initiated
- Printer Tranche 1 order placed or pre-staged for July delivery

---

### Window 2: June 15–30 — Sample Orders and Quality Validation

**Goal:** Validate each vendor against production standards before committing to Phase 2 volumes. This is the risk-reduction phase.

| Date | Action | Vendor | Expected Outcome |
|---|---|---|---|
| June 15 | Evaluate eSUN wholesale response; initiate negotiation if quote received | eSUN | Pricing visibility at 40–60 kg/month |
| June 15–20 | Polymaker sample arrives; run parallel QC test (Polymaker vs. eSUN same file, same printer) | Polymaker | Quality comparison data for white/grey |
| June 18 | Evaluate Anycubic AMS test results; make pass/fail decision on 50kg pallet | Anycubic | Confirm or disqualify as secondary |
| June 20 | If Anycubic passes: order 50kg pallet ($524.73) as Q3 filament buffer | Anycubic | 50kg buffer stock arriving late June |
| June 22 | Printers (Tranche 1) arrive from MatterHackers; unbox and SimplyPrint enrollment | MatterHackers | 3–4 printers active in farm |
| June 22 | Order consumables bulk package: 24 nozzles, 8 PTFE tubes, 8 heating cartridges | Amazon/Bambu | Fleet parts inventory complete |
| June 25 | Evaluate Overture wholesale PETG response; decide if PETG sample order warranted | Overture | PETG supplier confirmed or deferred |
| June 28 | Contact support.na@polymaker.com with 3-month volume projection; negotiate volume discount | Polymaker | Establish whether 5–10% additional discount is available |
| June 30 | Monthly supplier scorecard update: lead time, quality, pricing actuals vs. quotes | All vendors | Data for July decision-making |

**Expected outcomes by June 30:**
- All filament vendors validated against production quality standards
- Anycubic 50kg buffer in transit or arrived
- Polymaker quality comparison complete; decision on white/grey primary made
- Fleet parts inventory stocked for 6-month supply
- Printer Tranche 1 physically installed and configured in SimplyPrint

---

### Window 3: July 1 Onward — Full Phase 2 Rollout

**Trigger:** July 1 rollout does not require Phase 1 revenue validation — it is a capital-light pre-staging that is running in parallel. However, the July printer tranches (Tranche 2 and Tranche 3) are gated on Phase 1 revenue triggers:

| Tranche | Units | Activation Trigger | Capital |
|---|---|---|---|
| Tranche 1 (June 15 order) | 3–4 P1S | None — pre-staged now | $1,197–$1,596 |
| Tranche 2 | 2–3 P1S | Phase 1 revenue >$1,500/month × 2 consecutive months | $798–$1,197 |
| Tranche 3 | 2–3 P1S (to reach 8 total) | Phase 1 revenue >$3,500/month × 2 consecutive months | $798–$1,197 |

**July filament actions:**
- If Polymaker quality test passed in June: Place first $1,000 order (~67kg white/grey) targeting August arrival
- Expand eSUN Amazon standing order to 20kg/month (10kg black, 5kg white, 5kg grey) as baseline
- If Anycubic validated: integrate as 25–30% of black filament volume at $10.49/kg, saving ~$0.19/kg vs. eSUN

**July consumables actions:**
- Review nozzle consumption rate after first month of 4-printer operation
- Adjust safety stock if actual wear interval deviates from the 600–800 hour projection
- Order second Sunlu S4 dry box if running more than 6 active color slots simultaneously

---

## Section 3: Account Optimization Matrix

### Per-Unit Economics by Vendor and Volume

The following table shows the per-unit material cost impact (at 75g/unit average) at Phase 2 target volumes. Phase 2 is defined as 4 printers producing 1,500–1,600 units/month; Phase 3 (8 printers) as 3,000–3,200 units/month.

| Filament Vendor | Price/kg | Cost/unit (75g) | Phase 2 Monthly Cost (1,500 units) | Phase 3 Monthly Cost (3,000 units) |
|---|---|---|---|---|
| eSUN Amazon 10kg bundle | $12/kg | $0.90 | $1,350 | $2,700 |
| eSUN direct wholesale (50kg/month) | $10/kg | $0.75 | $1,125 | $2,250 |
| Anycubic 50kg pallet | $10.49/kg | $0.79 | $1,181 | $2,363 |
| Polymaker wholesale ($1,000 MOQ) | $14.99/kg | $1.12 | $1,680 | $3,360 |
| Blended optimal (60% eSUN + 25% Anycubic + 15% Polymaker) | $11.25/kg | $0.84 | $1,267 | $2,534 |
| Blended premium (40% eSUN + 20% Anycubic + 40% Polymaker) | $12.25/kg | $0.92 | $1,380 | $2,760 |

**Recommended Phase 2 blend:** 60% eSUN direct wholesale + 25% Anycubic + 15% Polymaker (white/grey only). Effective cost: ~$11.25/kg. Savings vs. all-eSUN-Amazon: ~$0.75/kg × 100kg/month = $75/month. At Phase 3 (200kg/month): $150/month saved.

---

### Vendor Priority Matrix

| Category | Vendor | Priority | MOQ | Lead Time | Payment Terms | API/Batch Order | Phase |
|---|---|---|---|---|---|---|---|
| Printer (primary) | MatterHackers | 1 | None | 3–7 days | Credit/PO | Quote system | Phase 2 |
| Printer (B2B) | Bambu Lab B2B | 2 | None | 3–7 days | Credit/Net-30 | Inquiry portal | Phase 2 |
| Printer (backup) | Dynamism | 3 | None | 3–7 days | Credit/PO | Quote system | Contingency |
| Filament PLA (primary) | eSUN (Amazon + direct) | 1 | None (Amazon) | 2–5 days (Amazon) | Credit / Net-30 (direct) | Amazon Subscribe & Save | Phases 0–3 |
| Filament PLA (premium) | Polymaker | 2 | $1,000 order | 3–5 days | Credit / Net-30 | Shopify checkout | Phase 2+ |
| Filament PLA (hedge) | Anycubic | 3 | None | 3–7 days | Credit card | Online checkout | Phases 1–3 |
| Filament PLA (backup) | Overture | 4 | None (Amazon) | 2–5 days | Credit | Amazon | Emergency fill |
| Filament PETG | Overture | 1 | None | 2–5 days | Credit | Amazon | Phase 3 SKU exp. |
| Nozzles | Bambu official / Amazon | 1 | 1 unit | 2–5 days | Credit | Amazon Subscribe | Ongoing |
| Bed sheets | Bambu official | 1 | 1 unit | 2–5 days | Credit | Bambu store | Ongoing |
| Heating parts | Bambu official / Amazon | 1 | 1 unit | 2–5 days | Credit | Amazon | Ongoing |
| Packaging | Shop4Mailers | 1 | 100 units | 3–5 days | Credit | Online order | Phases 1–3 |
| Custom boxes | Packlane | 1 | 1 unit | 10–14 days | Credit | Online designer | Phase 2+ |
| Fulfillment | Pirate Ship (self) | 1 | None | Instant | None (free) | Etsy API | Phases 0–3 |

**API/batch ordering note:** No filament vendor in this stack has a publicly documented REST API for automated batch ordering. "API access" for batch ordering is achieved via Amazon Subscribe & Save (eSUN), Polymaker's Shopify checkout with recurring orders, and Anycubic's standard storefront. At Phase 2 volumes, automated reordering is triggered by inventory tracking in a spreadsheet with manual order placement, not automated API calls. This is sufficient until Phase 3 volumes (200+ kg/month) justify building a custom procurement automation.

---

## Section 4: Volume Negotiation Scripts

### Template 1: Printer Quote Request — MatterHackers (June 1)

Send to: sales@matterhackers.com
Subject: Print Farm Quote Request — 4× Bambu Lab P1S, Phase 2 Build-Out

---

Hello MatterHackers Sales Team,

My name is [NAME], founder of ModRun Design, a production print farm building a cable management product line on Etsy and Amazon. We are expanding from our current single-printer setup to a 4-printer farm in June–July 2026, with a target of 8 printers by Q4.

I'm reaching out because MatterHackers is the only US distributor I've found with formally structured print farm bundles, and the 2-year extended warranty coverage is a key factor in our decision.

**What I need a quote on:**
- 4× Bambu Lab P1S printers (base or Combo with AMS 2 Pro — please quote both)
- Any farm bundle pricing that applies to a 4-unit purchase
- Extended warranty coverage options
- Lead time for current stock
- Payment options — do you support net-30 purchase orders for business accounts?

**Context for your sales team:**
- Current setup: 1× Bambu P1S, operational
- Phase 2 target: 4-printer cluster, June 2026
- Phase 3 target: 8-printer cluster, Q3–Q4 2026
- Product: Cable management clips (PLA+), Etsy and Amazon sales channel
- We're a serious multi-unit buyer planning two additional tranches before year-end

Could you provide a quote and lead time confirmation by June 7? I'm ready to place the order within the week of receiving a satisfactory quote.

Best regards,
[NAME]
ModRun Design
[EMAIL] | [PHONE]

---

### Template 2: Filament Volume Pricing — eSUN Direct Wholesale (June 7)

Send to: wholesale@esun3d.com (or contact form at esun3dstore.com)
Subject: Wholesale Inquiry — 40–60 kg/Month PLA+ Purchase Commitment

---

Hello eSUN Sales Team,

I'm the founder of ModRun Design, a production 3D print farm in the US producing cable management products at increasing volume. We've been sourcing eSUN PLA+ through Amazon bundles and are ready to establish a direct wholesale relationship.

**Current consumption:** 20 kg/month across 3 colors (black, white, grey)

**Projected consumption (6-month horizon):**
- July 2026: 40 kg/month
- October 2026: 80 kg/month
- Q1 2027: 100+ kg/month

**Why eSUN:** Your PLA+ is our benchmarked primary filament for Bambu P1S AMS compatibility. We've had zero feed errors over extended runs. We want to transition from Amazon-based purchasing to a direct supplier relationship.

**What I'm requesting:**
1. Wholesale pricing for PolyLite PLA+ at 40 kg/month and 80 kg/month tiers, for black, white, and grey 1.75mm
2. Available spool formats (standard cardboard refill preferred for AMS)
3. Payment terms — our target is net-30 with a 6-month volume commitment
4. Lead time from order placement to US delivery
5. Whether a 12-month pricing guarantee is available

I'm prepared to commit to a 6-month minimum purchase schedule at agreed volume with a written purchase schedule.

Please reply with your wholesale pricing sheet or connect me with the appropriate account manager.

Best regards,
[NAME]
ModRun Design
[EMAIL] | [PHONE]

---

### Template 3: Premium Tier Introduction — Polymaker (June 3)

Send to: support.na@polymaker.com
Subject: Print Farm Wholesale Introduction — ModRun Design, Houston Account

---

Hello Polymaker Support Team,

I've just registered a wholesale account at us-wholesale.polymaker.com and wanted to introduce ModRun Design — a production Bambu P1S print farm producing cable management products for Etsy and Amazon.

**Why Polymaker:** We're building toward 8-printer scale with rigorous QC standards. Polymaker's ±0.02mm diameter tolerance, vacuum-sealed packaging, and published CoA documentation make you the right partner for our white and grey production runs, where surface quality is most visible to buyers.

**Where we are:**
- Current: 1-printer operation, ~20 kg/month
- June 2026: 4-printer cluster, targeting 40–50 kg/month
- Q4 2026: 8-printer cluster, targeting 100+ kg/month

**What I'd like:**
1. Samples of PolyLite PLA in white and light grey for qualification testing against our current eSUN baseline
2. Confirmation of current wholesale pricing on PolyLite PLA per your website ($14.99/kg) — and whether a sustained 50+ kg/month commitment unlocks additional volume pricing
3. Guidance on the fastest path to net-30 payment terms
4. Your recommended print profile for PolyLite PLA on Bambu P1S (temperature, speed, AMS settings)

We plan to place our first $1,000+ order in August once we confirm quality performance in our production environment. I'd like to establish the relationship now so we're not starting from scratch when we need supply.

Thank you for your time. Looking forward to building a long-term supplier partnership.

Best regards,
[NAME]
ModRun Design
[EMAIL] | [PHONE]

---

### Template 4: Standing Order Negotiation — eSUN (Month 3, ~August 2026)

Use once eSUN direct wholesale relationship is established and 40 kg/month production is confirmed.

Send to: [eSUN wholesale account manager]
Subject: 12-Month Standing Order Proposal — ModRun Design

---

Hello [Contact Name],

We've been purchasing eSUN PLA+ through your wholesale program for [X months] and have been consistently hitting [40–50] kg/month. I'd like to propose converting to a formal monthly standing order with a 12-month commitment in exchange for locked pricing.

**Proposed standing order structure:**
- Volume: 50 kg/month (committed, with ±20% flexibility for demand variance)
- Colors: Black (25 kg), White (15 kg), Grey (10 kg)
- Format: Standard 1kg spools on cardboard cores (AMS-compatible)
- Delivery: Monthly, first week of each month
- Terms: Net-30 from invoice date

**What I'm offering:**
- 12-month commitment, reducing your forecasting uncertainty
- Consistent 3-color order, simplifying picking and packing
- On-time payment history of [X months] — no exceptions

**What I need in return:**
- Locked pricing at [$10.00–10.50]/kg for the commitment period (currently paying [$X]/kg)
- 30-day advance notice if pricing must change (not a retroactive increase)
- Priority fulfillment window if there is a stock allocation event

This standing order represents $6,000–$6,300 in annual purchases. I'm prepared to sign a simple letter of intent on this structure.

Can we schedule a 15-minute call this week to finalize terms?

Best regards,
[NAME]
ModRun Design

---

### Template 5: SLA and Technical Support Agreement — Polymaker (Month 4+)

Use once Polymaker is established as primary white/grey supplier.

Send to: support.na@polymaker.com
Subject: Technical Support SLA and Volume Agreement — ModRun

---

Hello [Contact Name],

We've been sourcing PolyLite PLA from your wholesale program for [X months] and are scaling to 8-printer production. As we grow, I want to formalize a few items to ensure we have a dependable production supply relationship.

**Volume projection (next 6 months):**
- Current: [40–50] kg/month
- Target by [date]: 100 kg/month
- Annual total projection: 1,000+ kg

**What I'm requesting:**
1. Designated account contact at support.na@polymaker.com for batch issues (response within 24 business hours for production-impacting failures)
2. Batch-to-batch CoA documentation included with each order (or on request, same-day response)
3. Discussion of an additional 5–10% volume discount at 100 kg/month threshold
4. Advance notice of 30+ days for any pricing changes or product discontinuations
5. Evaluation of net-30 payment terms given our order history

**From our side:**
- Consistent monthly orders, no missed payments
- 6-month forward consumption projections provided quarterly
- Product tag credit in Etsy listings ("Printed with Polymaker PolyLite PLA")
- Willingness to participate in a case study if beneficial to Polymaker's print farm marketing

This is a long-term supplier relationship proposal. What can Polymaker offer an operator at our scale?

Best regards,
[NAME]
ModRun Design
[EMAIL] | [PHONE]

---

## Section 5: Inventory Pre-Staging Strategy

### What to Order in June–July to Prevent August–September Supply Chain Gaps

The August–September production ramp is the highest-risk supply window in the Phase 2 timeline. By August, the 8-printer farm (assuming Tranches 1–3 arrive on schedule) will consume approximately 100 kg/month of filament. Without pre-staged inventory, a single 7-day supplier delay during this ramp creates a 100-unit production shortfall that compounds into Etsy order delays and review damage exactly when Q4 demand is accelerating.

**Filament pre-staging (June–July orders, targeting August buffer):**

| Item | Quantity | Vendor | Order Date | Arrival Target | Cost | Purpose |
|---|---|---|---|---|---|---|
| eSUN PLA+ black 10kg case | 20kg (2 cases) | Amazon | June 1 | June 5 | $220–260 | Immediate production |
| eSUN PLA+ white 10kg case | 10kg (1 case) | Amazon | June 1 | June 5 | $110–130 | Immediate production |
| eSUN PLA+ grey 10kg case | 10kg (1 case) | Amazon | June 1 | June 5 | $110–130 | Immediate production |
| Anycubic PLA 10kg test | 10kg | Anycubic direct | June 3 | June 10 | $105 | AMS validation |
| Anycubic PLA 50kg pallet | 50kg (if validated) | Anycubic direct | June 20 | June 27 | $525 | Q3 buffer hedge |
| Polymaker PolyLite white/grey | 67kg ($1,000 order) | Polymaker wholesale | August 1 | August 7 | $1,000 | Phase 2 primary (month 3) |

**Total filament pre-staged June–July:** 90–165 kg (depending on Anycubic validation outcome). This represents 6–8 weeks of 4-printer operation and 3–4 weeks of 8-printer operation — adequate buffer for August ramp without excess.

---

### Filament Seasonal Storage Best Practices

PLA is hygroscopic. Above 55% relative humidity, unsealed spools absorb moisture within hours, causing bubbling, stringing, and layer adhesion failures that manifest as defective prints and customer returns.

**Phase 2 storage infrastructure:**

| Equipment | Cost | Capacity | Humidity | Phase |
|---|---|---|---|---|
| Airtight bins + silica gel packs | $40–60 | 10–15 kg | Manual refresh every 2 weeks | Phase 0–1 (already in place) |
| Sunlu S4 Active Dry Box (2 units) | $160–240 total | 8–12 spools active | 5–15% RH continuous | Phase 2 (order June 1) |
| Industrial dry cabinet | $400–700 | 60–100 kg | <5% RH constant | Phase 3 (order when 5-printer farm confirmed) |

**Seasonal storage rules:**
- New spools arriving June–August: Store in sealed airtight bins with fresh desiccant until loaded into Sunlu S4 for active use
- Black filament (most volume): Less moisture-sensitive for cosmetic purposes; still store sealed
- White and grey filament (quality-visible): Priority placement in Sunlu S4 active drying; never leave unsealed overnight
- Opened spools: Mark with opening date; discard (or quality-test before use) after 90 days if stored in bin only, 180 days if stored in S4
- Anycubic Refill format (cardboard spool): More moisture-sensitive than spooled; prioritize S4 drying
- Polymaker spools (when active): Vacuum-sealed foil bag with desiccant; leave sealed until loaded into S4 for print run

**Reorder thresholds by printer count (minimum on-hand buffer = 2-week supply):**
- 4-printer farm (40–50 kg/month): Reorder when below 20 kg on-hand
- 8-printer farm (80–100 kg/month): Reorder when below 50 kg on-hand; order in 6-week batches

---

### Replacement Parts Pre-Staging (Phase 2 Fleet of 4–8 Printers)

Order these by June 22 (coinciding with Tranche 1 printer arrival) to have inventory available from Day 1 of 4-printer operation.

**Phase 2 parts order (Amazon + Bambu official, June 22):**

| Part | Quantity | Unit Cost | Total | Source | Notes |
|---|---|---|---|---|---|
| Nozzle 0.4mm hardened steel | 24 | $3–5 | $72–120 | Bambu store / Amazon | 6-month supply at 3–4/month consumption |
| PTFE tube hotend section | 8 | $5–8 | $40–64 | Bambu store / Amazon | 4-unit supply with 2 spares |
| Heating cartridge | 8 | $8–12 | $64–96 | Bambu store / Amazon | 4-unit supply with 2 spares |
| Thermistor | 8 | $6–10 | $48–80 | Bambu store / Amazon | 4-unit supply with 2 spares |
| PEI bed sheet | 8 | $30–40 | $240–320 | Bambu official | 2 per printer at Phase 2 |
| Drive belt XY set | 4 | $15–25 | $60–100 | Amazon compatible | 1 per printer backup |
| Extruder drive gear | 4 | $10–15 | $40–60 | Amazon compatible | 1 per printer backup |
| HEPA/carbon filter set | 8 | $15–25 | $120–200 | Bambu official | 1 replacement per printer; replace at 200–400 hours |
| **Total parts order** | | | **$684–1,040** | | Order together for single shipment |

**Phase 2 parts order (scale-up at Tranche 3, ~August 2026 when 8-printer farm complete):**
- Increase nozzle stock to 48 units (12+ months supply at 8-printer scale)
- Add 8 additional PTFE tubes, heating cartridges, and thermistors
- Add 8 additional bed sheets
- Budget: additional $400–600 above Phase 2 initial order

---

### Failure Rate Data from Phase 1 (Calibration Inputs)

Phase 1 is a single-printer operation. The expected failure rates below are derived from community data and the maintenance model in MULTI_PRINTER_FARM_ARCHITECTURE.md. Update these with actual Phase 1 data after 90 days of operation.

| Failure Type | Expected Rate (P1S, PLA+) | Cost per Event | Annual Events (8-printer) | Mitigation |
|---|---|---|---|---|
| Nozzle clog requiring replacement | 1 per 600–800 hours per printer | $4 (proactive) or $40–80 (reactive) | 3–4/month at 8-printer scale | Proactive swap at 500 hours |
| Bed adhesion failure (print pop-off) | 1–2% of print jobs | $0.90–1.50 (material) + 22-26 min print time | 40–60 events/month at 8 printers | IPA wipe before each print; replace PEI at 9 months |
| AMS feed jam | 0.5–1% of multi-hour jobs | 1–4 hours diagnostic + material waste | 15–30 events/month | Moisture control; nozzle cleanliness |
| Heating cartridge failure | 1 per 1,500–2,000 hours | $8–12 part + 1 hr downtime | 1–2/month at 8 printers | Carry 8 units in spare stock |
| Thermistor failure | 1 per 2,000+ hours | $6–10 part + 30 min downtime | 0–1/month | Carry 8 units in spare stock |

**Key Phase 1 data to collect:** Track nozzle swap intervals, AMS jam frequency, and bed replacement timing on the single printer. If nozzle wear interval deviates significantly from 600–800 hours (e.g., consistently below 400 hours), increase bulk stock before Phase 2 launch.

---

## Section 6: Risk Mitigation

### Supply Chain Diversification Rules

**Primary constraint:** No single vendor may supply more than 40% of any consumable category's monthly volume. This applies to filament by color and by material.

**Rationale:** eSUN black filament via Amazon is currently the only source for the highest-volume color. A single stock-out event at Amazon (occurs 2–4 times per year on high-demand colors) with no backup stocks the 8-printer farm with no primary material. At 100 kg/month and a 7-day Amazon Prime restock lag, a stock-out costs 3,500 units × $15 net = $52,500 in delayed production revenue (assuming backlogged orders rather than lost orders).

**Diversification targets by Phase 2 full operation (8 printers):**

| Material | Primary Vendor | % Volume | Secondary Vendor | % Volume | Tertiary | % Volume |
|---|---|---|---|---|---|---|
| PLA+ Black | eSUN direct wholesale | 40% | Anycubic 50kg pallet | 40% | eSUN Amazon | 20% |
| PLA+ White | Polymaker wholesale | 40% | eSUN direct | 40% | MatterHackers Build | 20% |
| PLA+ Grey | Polymaker wholesale | 40% | eSUN direct | 40% | eSUN Amazon | 20% |
| PLA+ Specialty colors | SUNLU (sample/low vol.) | 60% | eSUN Amazon | 40% | — | — |
| PETG (Phase 3) | Overture | 70% | MatterHackers | 30% | — | — |
| Nozzles | Bambu official | 60% | Amazon compatible | 40% | — | — |
| Bed sheets | Bambu official | 100% | — | — | — | — |

---

### Alternative Vendors for Critical Items

**Filament emergency escalation path:**

If eSUN black is simultaneously unavailable on Amazon AND eSUN direct:
1. Anycubic black 10kg bundle — order immediately (3–7 day delivery)
2. Overture black 10kg bundle (Amazon Prime, 2–5 days)
3. SUNLU black 6kg mix bundle — bridge purchase
4. Hatchbox black (premium tier, $25–28/kg) — worst-case 2-day bridge at 2× cost

**Printer emergency escalation path:**

If Bambu Lab P1S becomes unavailable (discontinuation, tariff disruption):
1. Bambu P2S ($549) — same ecosystem, same AMS, 15–20% faster throughput; community reliability data accumulating in 2026
2. Bambu A1 ($349–399 on sale) — no enclosure, same AMS Lite, same throughput for PLA clips; acceptable for clip-only production
3. Prusa i3 MK4S ($799) — slowest fallback but fully open-source, fully serviceable, no supply chain dependency

**Nozzle emergency escalation path:**

If Bambu official hardened steel nozzle supply is constrained:
1. Amazon third-party hardened steel nozzles — confirm compatibility with P1S hotend thread spec before bulk order
2. E3D compatible nozzles (if third-party supplier confirmed to fit P1S) — US-based supply chain

---

### Warehouse Space Requirements

**4-printer Phase 2 footprint:** 65 sq ft dedicated to printer zone + 24 sq ft QC bench = ~90 sq ft minimum. A standard spare bedroom (10×12 = 120 sq ft) accommodates a 4-printer farm with space for filament storage and QC bench.

**8-printer Phase 3 footprint:** 110 sq ft printer zone + 32 sq ft QC bench = ~145 sq ft. Requires a dedicated room (second bedroom, finished basement, or single-car garage bay at minimum 20×10 = 200 sq ft to include filament storage and packaging station).

**Filament storage space:**
- 50 kg on-hand (Phase 2 2-week buffer): 6–8 cubic feet (one standard shelving unit)
- 100 kg on-hand (Phase 3 2-week buffer): 12–15 cubic feet (two shelving units or one dry cabinet)

**No external warehouse required through Phase 3 (8-printer farm).** A standard 2-car garage (400 sq ft) accommodates the 8-printer farm, QC bench, filament storage, packaging station, and a dedicated shipping area with room to spare. External warehouse evaluation begins only if Phase 4 revenue triggers a 3PL integration (~$20,000+/month revenue, 200+ orders/month).

---

### Obsolescence Management

**Printer model obsolescence:** The Bambu X1C was discontinued February 2026 without warning. The P1S is the current production model with no announced successor at the time of writing (May 2026). Risk: if Bambu announces a P3S or similar successor, P1S resale value drops and spares may become scarce. Mitigation: (a) purchase in tranches not bulk, (b) maintain the spare parts inventory above, (c) monitor Bambu Lab announcements — any "introducing the successor to P1S" announcement triggers an immediate evaluation of whether to accelerate Phase 2 printer purchases at current P1S pricing.

**Filament color obsolescence:** eSUN and Anycubic periodically discontinue specific colors. Black, white, and grey are commodity colors with no discontinuation risk. Specialty colors (silk, dual-color, metallic variants) are high risk. SUNLU's role as the color sampling vendor is specifically to avoid committing 10kg+ to a color before velocity is confirmed.

**Software obsolescence:** SimplyPrint and Bambu Farm Manager are subscription/free tools. If either is discontinued, the fallback is Printago ($29/month, unlimited printers) or OctoPrint with a custom Bambu plugin. No lock-in risk is present given the number of viable alternatives.

---

## Section 7: Execution Checklist — June 1–15 Outreach Window

### Day-by-Day Actions (June 1–15)

**June 1 (Day 1 — Account Setup):**
- [ ] Register Polymaker wholesale account at us-wholesale.polymaker.com (15 min)
- [ ] Place eSUN PLA+ order via Amazon: 10kg black + 10kg white + 10kg grey (10 min)
- [ ] Email MatterHackers quote request using Template 1 above (20 min)
- [ ] Submit Bambu Lab B2B inquiry at bambulab.com/en/corporate-sales (20 min)

**June 3 (Day 3 — Filament Outreach):**
- [ ] Email Polymaker using Template 3 above (15 min)
- [ ] Order Anycubic 10kg PLA sample for AMS validation (10 min)

**June 5 (Day 5 — Follow-Ups):**
- [ ] If no MatterHackers email response: call +1 (800) 613-4290 (10 min)
- [ ] If no Bambu B2B response: check portal for response status (10 min)

**June 7 (Day 7 — eSUN Direct):**
- [ ] Email eSUN wholesale inquiry using Template 2 above (20 min)

**June 8 (Day 8 — Price Benchmarking):**
- [ ] Email Dynamism quote request: sales@dynamism.com for 4× P1S pricing (15 min)
- [ ] Email Overture wholesale inquiry for PETG pricing: overture3d.com/pages/wholesale (15 min)

**June 10 (Day 10 — Validation):**
- [ ] Receive Anycubic sample; run AMS validation test (2 hrs)
- [ ] Record results: pass/fail, feed error frequency, dimensional check
- [ ] Compare MatterHackers, Bambu B2B, and Dynamism printer quotes; select vendor (30 min)

**June 12 (Day 12 — Decisions):**
- [ ] Confirm printer Tranche 1 vendor selection
- [ ] If Anycubic passed AMS test: prepare 50kg pallet order for June 20
- [ ] Evaluate eSUN direct response if received; if no response, follow up by phone

**June 15 (Day 15 — Orders Placed):**
- [ ] Place printer Tranche 1 order (3–4 P1S units, selected vendor) ($1,197–$1,596)
- [ ] Place Anycubic 50kg pallet order if validated ($524.73)
- [ ] Order consumables bulk package (June 22 target delivery, 24 nozzles + PTFE + heating cartridges + bed sheets) ($684–$1,040)
- [ ] Update supplier contact matrix (post-test-print-doc-5-supplier-contact-matrix.md) with all contacts, quotes, and statuses
- [ ] Log all actions in WORKLOG.md

**Total June 1–15 outreach budget (Phase 2 pre-staging, minimum viable):**

| Item | Cost |
|---|---|
| eSUN PLA+ 30kg via Amazon (June 1) | $330–390 |
| Anycubic 10kg validation sample (June 3) | $105 |
| Anycubic 50kg pallet (June 20, if validated) | $524 |
| Printer Tranche 1 — 3× P1S via MatterHackers | $1,197–$1,596 |
| Consumables bulk package (June 22) | $684–$1,040 |
| **Total June outreach spend** | **$2,840–$3,655** |

Excluding Tranche 1 printers (which are capital-gated on Phase 1 revenue triggers), the consumables and filament pre-staging cost is **$1,119–$1,535** — a supply chain insurance investment against the August–September ramp lag risk.

---

### Success Criteria for June 15 Checkpoint

By June 15, the following must be true for Phase 2 supplier pre-staging to be on track:

- [ ] Polymaker wholesale account registered and sample request submitted
- [ ] MatterHackers or Bambu B2B printer quote received and evaluated
- [ ] Anycubic AMS validation test complete with documented result
- [ ] eSUN direct wholesale conversation initiated (response or follow-up scheduled)
- [ ] At least 40kg of filament on-hand or in transit for 4-printer ramp
- [ ] Consumables bulk order placed or scheduled
- [ ] Printer Tranche 1 order placed or held pending Phase 1 revenue trigger

---

## Document Control

**Status:** Execution-ready for June 1, 2026. All supplier contacts, pricing, and templates are based on verified May 2026 data from the following internal research documents: BAMBU_LAB_FARM_SUPPLIER_CONTACTS.md, phase-2-supplier-research.md, POLYMAKER_WHOLESALE_ONBOARDING_GUIDE.md, MULTI_PRINTER_FARM_ARCHITECTURE.md, 8-printer-farm-cost-model.md, PHASE_2_CAPITAL_DEPLOYMENT_TIMELINE.md, PRINTER_FARM_EQUIPMENT_SPECIFICATIONS.md, and post-test-print-doc-5-supplier-contact-matrix.md.

**Independence from test print:** This document's entire execution window (June 1–15 outreach, June 15–30 validation, July pre-staging) does not depend on the May 30 test print outcome. Supplier relationships, account establishment, and inventory pre-staging serve Phase 2 under any Phase 1 scenario.

**Next update:** July 1, 2026 — incorporate actual Phase 1 failure rate data, confirmed Anycubic AMS validation result, eSUN direct wholesale pricing response, and Phase 1 revenue actuals against trigger thresholds.

**Confidence notes:**
- High confidence: All pricing is from verified May 2026 sources (internal research documents with cited URLs)
- Medium confidence: Anycubic AMS compatibility is community-reported mixed; validation test in June will convert to high or low confidence
- Medium confidence: eSUN direct wholesale pricing at 40–60 kg/month tier requires a live quote — the $10–11/kg estimate is from community-reported data, not a verified quote
- Lower confidence: Printer tranche timing assumes stable P1S availability; any Bambu supply event (new model launch, tariff action) would require timeline revision
