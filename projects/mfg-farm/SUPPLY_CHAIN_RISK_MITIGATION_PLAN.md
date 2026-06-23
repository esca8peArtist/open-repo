---
title: Supply Chain Risk Mitigation Plan — Phase 2
project: mfg-farm (ModRun / Etsy Print Farm)
created: 2026-06-23
session: 4100
status: production-ready
confidence: 90%
scope: >
  Comprehensive risk mitigation covering dual-source architecture, safety stock targets,
  fallback suppliers, contingency scenarios, QA checkpoints, and supplier scorecard template.
  Designed for Phase 1 launch through Phase 3 scaling. Complements and supersedes
  PRE_PRODUCTION_SUPPLY_CHAIN_RISK_MITIGATION.md for the 5 core categories.
related:
  - PHASE_2_SUPPLY_CHAIN_DIVERSIFICATION_RESEARCH.md
  - SUPPLIER_CONTACT_DATABASE.md
  - PHASE_2_TRACK_1_SUPPLY_CHAIN_DIVERSIFICATION.md
  - PRE_PRODUCTION_SUPPLY_CHAIN_RISK_MITIGATION.md
---

# Supply Chain Risk Mitigation Plan — Phase 2

**Lead finding**: ModRun's Phase 2 supply chain risk profile is manageable with three concrete rules: (1) never let any critical material drop below a 2-week on-hand supply before triggering a reorder, (2) maintain at least two validated vendors for filament at all times, and (3) no packaging supplier represents a production-stopping risk because all packaging materials are commodity and available next-day via Amazon Prime. The highest-risk event is not supplier failure — it is an unplanned Bambu P1S printer outage on a single-printer farm. After the printer itself, tariff-driven filament price escalation is the second-highest risk on probability × impact.

---

## Part 1: Redundancy Architecture

### 1.1 Dual-Source Minimum for Critical Materials

**Rule**: Every material categorized as "Critical" in the table below must have a validated second supplier before production begins. "Validated" means an actual test order received and evaluated — not just a company name on a list.

| Material | Criticality | Primary | Secondary | Tertiary (backup) | Dual-Source Status |
|---|---|---|---|---|---|
| PLA+ filament (black) | **Critical** | eSUN 10kg Amazon | Anycubic 50kg pallet | Overture Amazon Prime | Dual-source after AMS validation |
| PLA+ filament (white) | **Critical** | eSUN 10kg Amazon | Polymaker wholesale (Houston TX) | MatterHackers Build PLA | Dual-source after Polymaker account setup |
| PLA+ filament (grey) | High | eSUN 10kg Amazon | Polymaker wholesale | Overture Amazon Prime | Primary only until Month 2 |
| Poly mailers (6×9" or 9×12") | Medium | Amazon bulk (Prime) | ULINE case order | Shop4Mailers 1000-ct | Single-source OK (next-day reorder) |
| Kraft mailer boxes (6×4×2") | Medium | MrBoxOnline | Amazon (RetailSource) | ULINE corrugated | Single-source OK |
| Thank you / insert cards | Low | VistaPrint | Canva + Staples local print | Amazon pre-printed | Single-source OK |
| Printer nozzles (0.4mm) | High | Bambu official store | Amazon 3rd-party P1S compatible | Micro Center in-store | Dual-source at stock replenishment |
| PEI build plate | High | Bambu official store | Amazon 3rd-party (256×256mm) | Micro Center in-store | Dual-source at replacement |

### 1.2 Safety Stock Levels by Phase

**Rule**: Trigger a reorder when on-hand inventory reaches the "Reorder At" threshold. Never let any Critical material reach zero.

#### PLA+ Filament Safety Stock

| Phase | Units/Week | Filament Use/Week | 2-Week Buffer | 4-Week Buffer | Primary Color Reorder At | Cost of 4-Wk Buffer |
|---|---|---|---|---|---|---|
| Phase 1 (launch) | 5–20 | 0.1–0.44 kg | 0.2–0.88 kg | 0.4–1.76 kg | < 2 kg on hand | ~$20–25 |
| Phase 1 (growth) | 20–50 | 0.44–1.1 kg | 0.88–2.2 kg | 1.76–4.4 kg | < 4 kg on hand | ~$50–65 |
| Phase 2 (2-printer) | 50–150 | 1.1–3.3 kg | 2.2–6.6 kg | 4.4–13.2 kg | < 12 kg on hand | ~$130–160 |
| Phase 3 (3-printer) | 150–300 | 3.3–6.6 kg | 6.6–13.2 kg | 13.2–26.4 kg | < 25 kg on hand | ~$265–320 |
| Phase 4 (8-printer farm) | 300–800 | 6.6–17.6 kg | 13.2–35.2 kg | 26.4–70.4 kg | < 70 kg on hand | ~$700–850 |

**Safety stock funding rule**: Safety stock is working capital, not overhead. At Phase 1 scale, $25 in filament buffer prevents $500–800 in lost revenue from a production stoppage. The ROI on maintaining safety stock is always positive.

#### Packaging Safety Stock

| Item | Phase 1 Minimum Stock | Reorder At | Cost |
|---|---|---|---|
| Poly mailers (6×9") | 200 units | < 50 remaining | ~$15–20 |
| Kraft boxes (6×4×2") | 50 units | < 15 remaining | ~$25–40 |
| Thank you cards | 100 units | < 25 remaining | ~$15–25 |
| Thermal labels (4×6" rolls) | 2 rolls (500 labels) | 1 roll remaining | ~$20–30 |

#### Printer Consumables Safety Stock

| Part | Per-Printer Stock | Fleet Stock (8-printer) | Reorder At |
|---|---|---|---|
| Nozzle 0.4mm hardened | 6 units | 24 units | Below 3 per printer |
| PEI build plate | 1 spare | 4 spares | Below 1 per printer |
| Heating cartridge | 1 spare | 4 units | Below 2 fleet total |
| Thermistor | 1 spare | 4 units | Below 2 fleet total |
| PTFE tube (hotend) | 1 meter | 4 tubes | Below 2 fleet total |

---

## Part 2: Fallback Suppliers by Category

### 2.1 PLA+ Filament Fallback Chain

```
Production color out of stock (primary supplier)
├── CHECK: Overture same color (Amazon Prime, 1–2 days) → ORDER
├── CHECK: Hatchbox same color (Amazon Prime, 1–2 days) → ORDER at premium
├── CHECK: SUNLU color mix bundle (if color-flexible, 3–5 days) → ORDER
├── If all major colors unavailable:
│   ├── Switch to nearest available production color; message buyers proactively
│   ├── Set Etsy processing time to 7–10 days
│   └── Order Polymaker wholesale (Houston TX, 3–5 days) as quality fallback
└── If tariff-driven price spike (>15% increase):
    ├── Forward-buy eSUN at pre-increase pricing if cash available
    ├── Activate Polymaker wholesale (full tariff immunity at $14.99/kg)
    ├── Contact Push Plastic for bulk quote (~$22–25/kg US-made)
    └── Monitor: set Google Alert "filament tariff" "Section 301 tariffs 3D printing"
```

**Fallback suppliers ranked by activation speed**:

| Rank | Supplier | Lead Time | Cost Impact | Activation Trigger |
|---|---|---|---|---|
| 1 | Amazon bulk (Overture, Hatchbox) | 1–2 days | +$2–4/kg | Primary OOS on Amazon |
| 2 | Anycubic direct | 3–7 days | -$2/kg (lower cost) | eSUN OOS; already validated |
| 3 | Polymaker wholesale (Houston) | 3–5 days | +$2–3/kg | Quality alternative; tariff hedge |
| 4 | MatterHackers Build PLA | 2–4 days | +$7–10/kg | All China-origin suppliers compromised |
| 5 | Push Plastic (US-made) | 3–5 days | +$10–12/kg | Tariff increase >20%; domestic only |

### 2.2 Packaging Fallback Chain

All packaging materials are commodity — no production-stopping risk if any single supplier fails.

| Scenario | Primary | Fallback 1 | Fallback 2 |
|---|---|---|---|
| Poly mailers OOS | Amazon bulk | ULINE (1–3 day) | Shop4Mailers |
| Kraft boxes OOS | MrBoxOnline | Amazon (RetailSource) | ULINE corrugated |
| Insert cards OOS | VistaPrint | Canva + Staples local (same-day) | Amazon pre-printed cards |
| Custom boxes delayed | Packlane | Plain MrBoxOnline box as interim | Note on order "packaging upgrade coming soon" |
| Tissue paper OOS | Amazon plain white | None needed — skip tissue on rush orders | — |

### 2.3 Printer Hardware Fallback Chain

```
Bambu P1S hardware failure
├── Under warranty (< 1 year):
│   ├── Submit warranty claim to Bambu Lab support (1–3 week resolution)
│   └── While waiting: Place Xometry or JLC3DP order for overflow production (~$2–8/unit, 5–10 days)
├── Out of warranty / quick fix needed:
│   ├── Self-repair with spare parts kit (nozzle, PTFE, heating cartridge) — covers 80% of failures
│   └── If self-repair fails: Order new P1S at $399 (2–5 day delivery); ~10–15 day payback at current revenue
├── Catastrophic failure (mainboard, frame):
│   ├── Order replacement printer
│   ├── Consider P2S ($549) as upgrade replacement (15–20% faster throughput)
│   └── Use JLC3DP/Xometry overflow for 1–2 week production bridge
└── Bambu supply chain disruption (tariff ban, discontinuation):
    ├── Bambu A1 ($349) — same AMS, same PLA profiles, no enclosure — adequate for clips
    ├── Bambu P2S — faster, same ecosystem
    └── Prusa MK4S ($799) — fully open-source, no supply chain dependency; last resort

Fallback printing services for overflow (no printer needed):
- JLC3DP: jlc3dp.com | instant quote | PLA, ABS, TPU | $0.30–4.00/unit | 3–4 day production + 3–7 day ship
- Xometry: xometry.com | instant quote | US domestic shops | $4–25/unit | 1–5 business days
- Craftcloud: craftcloud3d.com | multi-supplier comparison | price varies | 5–15 days | escrow protection
```

---

## Part 3: Contingency Scenarios

### Scenario 1: Primary Filament Supplier Failure (eSUN stockout, 7+ days)

**Probability**: Medium-high (documented 2–4 stockout events/year per color on Amazon)  
**Impact**: Moderate — 7-day production shortfall at single-printer scale = ~$1,000–2,000 lost revenue  
**Response**:

| Day | Action |
|---|---|
| Day 0 (stockout detected) | Check Overture + Hatchbox same color on Amazon → order immediately |
| Day 0 | If OOS across all Amazon options: order Anycubic direct (3–7 day ship) |
| Day 1 | Set Etsy processing time to 7–10 days if order backlog exists |
| Day 1 | Message any pending orders proactively with "processing delay" |
| Day 3 | If Anycubic order not confirmed shipped: contact eSUN direct (email or Alibaba storefront) for expedited order |
| Day 7 | Filament arrives; resume normal production; reset processing time |

**Prevention**: Maintain 4-week filament buffer in all production colors. Reorder at 2-week inventory level, not when empty.

### Scenario 2: Lead Time Extension (supplier delays shipment 2+ weeks)

**Probability**: Medium (seasonal demand spikes, Q4 shipping congestion, Anycubic warehouse events)  
**Impact**: Low-moderate if safety stock maintained; severe if no buffer  
**Response**:

| Step | Action |
|---|---|
| Detection | Day 10 without arrival → contact supplier for tracking update |
| If delay confirmed 1 week | No action if 2-week buffer maintained |
| If delay confirmed 2+ weeks | Order from backup supplier at premium cost |
| If delay is tariff-related | Forward-buy at pre-increase price; activate domestic supplier |
| Post-event | Extend safety stock from 2 weeks to 4 weeks for that SKU |

**Prevention**: Order early; never order when below 1-week stock. Build 4-week buffer during Q1 (January–March) before Q2 demand acceleration.

### Scenario 3: Price Spike (filament cost +15–40%)

**Probability**: High (2026 tariff environment; Chinese filament already +10–75% since 2024–2025)  
**Impact**: $0.15–0.45/unit COGS increase; margin compression 1–3 percentage points  
**Response**:

| Trigger | Action |
|---|---|
| +15% (e.g., eSUN goes from $12 to $13.80/kg) | Forward-buy 1 month supply at pre-increase price; accelerate Polymaker wholesale activation |
| +25% (e.g., eSUN to $15/kg) | Shift 40% of volume to Polymaker domestic ($14.99/kg, tariff-immune); activate eSUN direct wholesale negotiation |
| +40% (e.g., eSUN to $16.80+/kg) | Shift 60–80% to domestic suppliers (Polymaker + Push Plastic); maintain Chinese supply for non-visible colors only |
| Price increase passed through to SKU | Adjust Etsy pricing $0.50–$1.00/unit if COGS increase exceeds 2% margin impact |

**Monitoring**: Google Alerts configured for "filament tariff", "PLA import tariff", "Section 301 3D printing". Review monthly.

### Scenario 4: Etsy Platform Disruption

**Probability**: Low (Etsy is a stable, public company; outages are temporary)  
**Impact**: High if sustained (1-2 day Etsy outage = $50–200 lost sales at Phase 1 scale)  
**Response**:

| Duration | Action |
|---|---|
| < 4 hours | No action; mark orders shipped when platform restores |
| 4–24 hours | Post status update to any social channels; email waiting customers if contact info available |
| > 24 hours | Activate Shopify store (Phase 2 readiness); route new orders through direct channel |
| Permanent suspension (policy violation) | Immediate: activate Amazon; apply to Etsy reinstatement; consult Etsy policy guides |

**Prevention**: Build Phase 2 Shopify direct store as secondary channel before Etsy becomes 100% of revenue. Target: Shopify live at $2,000/month Etsy revenue.

### Scenario 5: Packaging Supply Failure

**Probability**: Very low (all packaging is commodity, multiple domestic suppliers)  
**Impact**: Very low (Amazon Prime next-day eliminates any meaningful outage)  
**Response**: Same-day Amazon order covers any scenario. No further contingency needed.

---

## Part 4: Quality Assurance Checkpoints

### 4.1 New Supplier Qualification Protocol

Before using any new supplier for production, complete all steps:

**For filament suppliers**:
- [ ] Place test order (minimum 5–10kg)
- [ ] Print exact ModRun clip file on production printer
- [ ] Run continuous AMS job for 3+ hours
- [ ] Measure 5 clips with calipers (±0.1mm tolerance on critical dimensions)
- [ ] Record: lead time (order date → doorstep), packaging condition, spool winding quality
- [ ] Accept/reject: <3% defect rate on 50+ unit print run qualifies supplier

**For packaging suppliers**:
- [ ] Order minimum sample quantity (25–50 units)
- [ ] Inspect: seam integrity, print quality (if custom), dimensional accuracy
- [ ] Pack a complete product order; check weight, drop-test seal integrity
- [ ] Accept/reject: all units pass visual inspection and seal test

**For contract manufacturers (overflow / CF)**:
- [ ] Place 10–25 unit sample order
- [ ] Verify orientation (Z-axis print direction for snap arm)
- [ ] Dimensional check: rail channel ±0.3mm, snap arm engagement ±0.5mm
- [ ] Functional test: 20 engagement cycles on rail mock-up
- [ ] Accept/reject: ≥19/20 cycles functional; all dimensions in tolerance

### 4.2 Ongoing Supplier QA

**Monthly supplier review** (15 minutes per supplier, first Monday of each month):

| Metric | Acceptable | Watchlist | Reject/Replace |
|---|---|---|---|
| Lead time vs. quoted | ±1 day | +2–5 days | >5 days consistently |
| Defect rate | <2% | 2–5% | >5% |
| Price stability | ≤5% variance | 5–15% variance | >15% unannounced |
| AMS jam rate | <0.5% of jobs | 0.5–2% | >2% |
| Communication | <24 hrs response | 24–72 hrs | >72 hrs or unresponsive |

**Batch testing protocol**: On arrival of any pallet order (50+ kg), immediately pull 1 spool from each color. Run 30-minute AMS test before storing remainder. Any AMS jam in the first 30 minutes flags that batch for extended testing before production use.

### 4.3 Documentation Requirements

All supplier QA records are maintained in `material-sourcing-scorecard.csv`. Update after every:
- New supplier qualification test
- New material batch arrival (pallet orders)
- Any defect event or AMS failure

**Minimum fields per entry**: Supplier, material/product, batch/lot number if available, order date, arrival date, test date, defect count, defect type, AMS jam count, accept/reject decision, notes.

---

## Part 5: Supplier Scorecard Template

### Monthly Supplier Scorecard

Use this template monthly. Score each metric 1–5 (5 = excellent, 1 = poor). Composite score <12 triggers a performance conversation; <8 triggers replacement evaluation.

```
Supplier: ___________________
Month/Year: ___________________
Material: ___________________
Volume ordered (kg): ___________________

METRIC                    Score (1-5)    Notes
Lead time accuracy         ___           Quoted: ___ days | Actual: ___ days
Quality / defect rate      ___           Units ordered: ___ | Defects: ___ | Rate: ___%
AMS compatibility          ___           Jobs run: ___ | Jams: ___ | Rate: ___%
Price stability            ___           Quoted: $___ | Invoiced: $___
Communication / support    ___           Avg response time: ___ hrs
Packaging / transit        ___           Damage, moisture issues? Y / N
COMPOSITE SCORE            ___/25

Action:
  [ ] No action (score 20+)
  [ ] Monitor closely (score 15–19)
  [ ] Performance conversation (score 12–14)
  [ ] Replacement evaluation (score <12)

Notes:
```

### Annual Supplier Review

At the start of each calendar year (January), complete a full annual review:
- Calculate 12-month composite scores per supplier
- Compare actuals vs. budget (pricing drift)
- Review tariff exposure by supplier country of origin
- Confirm backup suppliers are still validated and active
- Update SUPPLIER_CONTACT_DATABASE.md with current pricing and contact info
- Re-qualify any backup supplier who has not received an order in 6+ months

---

## Part 6: Risk Register Summary

| Risk | Prob. | Impact | Risk Score (P×I) | Mitigation | Review Frequency |
|---|---|---|---|---|---|
| Single printer hardware failure | Medium (30–40%/yr) | High (week+ stoppage) | 12 | Spare parts kit; Xometry overflow; second printer at Phase 2 | Monthly |
| eSUN/Anycubic Amazon stockout (per color) | High (50–60%/yr) | Low-medium (3–7 days) | 8 | 4-week safety stock; Overture/Hatchbox backup; SUNLU color sampling | Weekly inventory check |
| Tariff escalation >15% | High (60%+/yr) | Medium ($0.15–0.45/unit COGS) | 9 | Forward-buy; Polymaker domestic backup; tariff monitoring | Monthly + Google Alerts |
| Anycubic batch quality failure | Low-medium (15–25%) | Medium (2–5% reject rate spike) | 4 | AMS validation before each pallet; dual-source maintains eSUN as fallback | Per-batch arrival |
| 3PL shipping cost inflation | Medium (30–40%/yr) | Medium ($500–1,500/mo over budget) | 6 | Lock per-unit pricing in writing; ShipMonk as cost-lock alternative | At 3PL activation |
| Packaging supplier OOS | Very low (<5%) | Very low (next-day reorder) | 0.3 | Amazon Prime backup eliminates risk | None needed |
| Etsy payment reserve (new shop) | High (90%+) | Medium (cash flow impact) | 9 | Account for 25–50% payout reserve in cash flow model for first 90 days | One-time |
| Etsy platform outage | Very low (<2%) | Medium (1–2 day sales loss) | 0.5 | Phase 2 Shopify backup; no further mitigation needed at Phase 1 | None needed |
| Bambu P1S discontinuation | Low (<10%) | High (hardware supply) | 2 | Purchase in tranches; spare parts stockpile; Prusa contingency | Quarterly |
| Carbon fiber nozzle wear (if activated) | High (90%+ on CF runs) | Low (planned maintenance cost) | 3.6 | Budget 3× nozzle cost vs. PLA runs; hardened steel nozzle mandatory | Per CF run |

**Risk scoring key**: Probability (0.2=5%, 0.5=25%, 1.0=50%, 2.0=75%, 3.0=90%+) × Impact (1=hours, 2=1–2 days, 3=1 week, 4=2+ weeks, 5=permanent)

---

## Part 7: Implementation Timeline

### Immediate (Pre-Launch, Week 0)

- [ ] Stock 4-week filament buffer in all production colors (black 4kg, white 2kg, grey 1kg)
- [ ] Order printer spare parts kit: 6 nozzles, 1 spare PEI plate, PTFE tube, heating cartridge, thermistor
- [ ] Order 100-ct poly mailers + 50-ct kraft boxes for Phase 1 orders
- [ ] Set Etsy processing time to 3–5 business days (buffer against single-printer constraints)
- [ ] Verify eSUN Amazon subscription active (Subscribe & Save for black filament)

### Month 1 (Post-Launch)

- [ ] Place Anycubic 10kg AMS validation order
- [ ] Register Polymaker wholesale account at us-wholesale.polymaker.com
- [ ] Email eSUN wholesale inquiry (Template 2 from PHASE_2_SUPPLIER_PRESTAGING_STRATEGY.md)
- [ ] Create ULINE business account
- [ ] Run first monthly supplier scorecard for eSUN

### Month 2–3

- [ ] Activate Anycubic 50kg pallet if AMS test passed
- [ ] First Polymaker sample order (white + grey); compare vs. eSUN on same file
- [ ] Begin custom packaging (VistaPrint 250 insert cards; Packlane sample kit)
- [ ] Update supplier scorecard after first 90 days of operation
- [ ] Evaluate: is dual-source architecture holding? Any concentration drift?

### Month 4–6 (Phase 2 Scaling)

- [ ] If Standard/Aggressive scenario: activate ShipBob or ShipMonk 3PL (lock per-unit pricing in writing)
- [ ] Confirm blended filament mix: 60% eSUN direct + 25% Anycubic + 15% Polymaker (white/grey)
- [ ] Upgrade poly mailer order to ULINE 5-case ($0.14/unit)
- [ ] eSUN direct wholesale 6-month commitment if response received
- [ ] Annual supplier review planned for January 2027

---

## Sources

- [Supply Chain Diversification Benefits — GEP](https://www.gep.com/blog/strategy/dual-sourcing-benefits-challenges-strategies)
- [Single Supplier Hidden Costs — Value Source Global](https://valuesourceglobal.com/insights/the-hidden-costs-of-single-supplier-dependency-and-how-to-create-a-resilient-sourcing-strategy)
- [JLC3DP FDM 3D Printing — Overflow Supplier](https://jlc3dp.com/3d-printing/fused-deposition-modeling)
- [Xometry Bulk 3D Printing](https://www.xometry.com/capabilities/3d-printing-service/bulk-3d-printing-service/)
- [Push Plastic Bulk Pricing — US Domestic Filament](https://www.pushplastic.com/pages/bulk-pricing)
- [Polymaker US Wholesale — Print Farm](https://us-wholesale.polymaker.com/pages/wholesale-filament-for-print-farms)
- [Etsy Chargebacks Help](https://help.etsy.com/hc/en-us/articles/4403482405527-Chargebacks-on-Etsy)
- [Stripe Chargeback Fees 2026](https://chargebacks911.com/chargeback-types/stripe-chargebacks/stripe-chargeback-fees/)
- [Tariff Impact on 3D Printing — MarketsandMarkets](https://www.marketsandmarkets.com/ResearchInsight/trump-tariffs-impact-3d-printing-market-analysis.asp)
- [Filament Color Crisis 2026 — Sovol](https://www.sovol3d.com/blogs/news/3d-printer-filament-out-of-stock-the-filament-color-crisis-2026)
- [Filament Price Surge 59% — Yanko Design April 2026](https://www.yankodesign.com/2026/04/11/as-3d-printing-filament-prices-surge-59-creality-turns-plastic-scrap-into-new-supply/)
- Internal: PRE_PRODUCTION_SUPPLY_CHAIN_RISK_MITIGATION.md
- Internal: PHASE_2_TRACK_1_SUPPLY_CHAIN_DIVERSIFICATION.md
- Internal: supply-chain-resilience-strategy.md
