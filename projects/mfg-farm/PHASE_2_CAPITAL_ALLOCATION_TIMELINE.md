---
title: "Phase 2 Capital Allocation Timeline — ModRun Print Farm"
created: 2026-06-01
status: production-ready
scope: "Capital requirements, funding scenarios, and deployment timeline for June 3 – July 15 Phase 2 ramp: 4-printer farm build-out, trademark filing, filament inventory, SimplyPrint activation, and working capital planning through July 15 operational readiness"
confidence: high
related:
  - PHASE_2_SUPPLIER_RFQ_TEMPLATES.md
  - PHASE_2_PRICING_NEGOTIATION_PLAYBOOK.md
  - TRADEMARK_FILING_STRATEGY.md
  - BAMBU_LAB_FARM_SUPPLIER_CONTACTS.md
  - PRINTER_FARM_EQUIPMENT_SPECIFICATIONS.md
  - MULTI_PRINTER_SCALING_ROADMAP.md
---

# Phase 2 Capital Allocation Timeline — ModRun Print Farm

**Lead finding:** The 4-printer farm operational by July 15 requires $2,140–$3,640 in capital, depending on whether Tranche 1 uses P1S base or Combo units and whether a consumables kit is purchased at Phase 2 entry or deferred. The trademark filing ($350, June 1) is the single highest-leverage capital deployment in the entire Phase 2 window because it unlocks Amazon Brand Registry access on Day 0 — no waiting for registration. Capital can be sequenced: $670–900 deploys June 1–3 with no dependencies; the printer Tranche 1 ($1,197–2,000+) deploys June 3–5 contingent on Phase 1 test-print validation; consumables and filament inventory deploy progressively through June.

**June 3 Phase 2 start is achievable regardless of Phase 1 test-print timing.** The trademark filing, Polymaker account setup, eSUN filament order, and all supplier outreach execute June 1 with no dependency on test-print completion. The printer purchase is the only item gated on Phase 1 — and even there, the gate is confirmation of production viability, not revenue targets.

---

## Section 1: Capital Requirements Map

### 1.1 Total Phase 2 Capital (June 3 – July 15 Operational Readiness)

| Bucket | Item | Low Estimate | High Estimate | Deployment Date | Gate |
|---|---|---|---|---|---|
| **Trademark** | USPTO Class 20 word mark (MODRUN) | $350 | $350 | June 1 | None |
| **Filament — initial inventory** | 30kg eSUN PLA+ (10 black, 10 white, 10 grey) via Amazon | $330 | $390 | June 1 | None |
| **Filament — validation sample** | Anycubic 10kg AMS validation | $105 | $105 | June 3 | None |
| **Packaging supplies** | 1,000 poly mailers + thermal labels | $55 | $75 | June 1 | None |
| **Software** | SimplyPrint Starter first month | $10 | $10 | June 15 (with printers) | Phase 1 gate |
| **Printer hardware — Tranche 1** | 3× P1S base at $399 | $1,197 | $1,197 | June 3–5 | Phase 1 gate |
| *(alternative: P1S Combo w/ AMS)* | *3× P1S Combo at $650–750* | *$1,950* | *$2,250* | *June 3–5* | *Phase 1 gate* |
| **Consumables kit — 4-printer fleet** | Nozzles (24), PTFE, cartridges, plates, belts | $444 | $680 | June 22 | Printers delivered |
| **Filament — Phase 2 production buffer** | 50kg Anycubic pallet (contingent on validation) | $525 | $525 | June 20 | Anycubic AMS pass |
| **Working capital reserve** | Returns, refunds, unexpected COGS | $150 | $200 | Hold | Released if needed |
| **Total (P1S base + validation sample + all)** | | **$3,166** | **$3,532** | | |
| **Total (P1S Combo + validation sample + all)** | | **$3,919** | **$4,585** | | |
| **Minimum viable (no Combo, no 50kg pallet)** | | **$2,146** | **$2,502** | | |

### 1.2 Minimum Viable Phase 2 (Bootstrap $2,000–2,500)

For a constrained cash scenario where Phase 1 revenue has not yet materialized:

| Item | Cost |
|---|---|
| Trademark filing (Class 20) | $350 |
| eSUN 30kg Amazon order | $360 |
| Packaging supplies (1,000 mailers) | $60 |
| 3× P1S base units | $1,197 |
| SimplyPrint first month | $10 |
| Working capital reserve | $150 |
| **Total minimum viable** | **$2,127** |

At this floor, Phase 2 launches with 4 printers (3 new + 1 existing), 30kg filament on hand (6 weeks at 4-printer Phase 2 entry), and the trademark filing in motion. The consumables kit and Anycubic pallet are deferred to Month 2 when Phase 1 revenue is available.

---

## Section 2: Equipment Capital — 4-Printer Farm Build-Out

### 2.1 Per-Printer Economics

**P1S base at $399 (recommended for fleet uniformity):**

| Metric | Value |
|---|---|
| Purchase price | $399 |
| Estimated gross profit per printer per month (at Phase 2 demand) | $1,800–2,400 |
| Hardware payback period | 1.5–2.5 months |
| 12-month net return (after hardware cost) | ~$21,600–28,800 |
| Warranty (Bambu direct) | 1 year |
| Warranty (MatterHackers) | 2 years (worth ~$100–150 in avoided repair risk) |

**P1S Combo at $649–750 (includes AMS 2 Pro for multi-color):**

| Metric | Value |
|---|---|
| Purchase price | $649–750 |
| Incremental cost vs. P1S base | +$250–351 |
| AMS 2 Pro value: enables multi-color without manual spool swaps | Saves ~2–3 min/color-change × 8 changes/day = 16–24 min/day/printer |
| Payback on AMS premium at $15/hour operator time | $250 / ($3/day saved) = 83 days |
| Recommendation | Buy Combo if budget allows — AMS pays back in under 3 months |

**Tranche-based acquisition math:**

| Tranche | Timing | Units | Unit Config | Total Hardware Cost |
|---|---|---|---|---|
| Tranche 1 (existing) | In service | 1× P1S | Base | Sunk |
| Tranche 2 | June 3–5 | 3× P1S | Base ($399) recommended | $1,197 |
| *(Combo upgrade option)* | June 3–5 | 3× P1S Combo | $649–750 | $1,947–2,250 |
| Tranche 3 (Phase 3, demand-gated) | July 1–15 | +1 P1S | Base or Combo | $399–750 |
| 4-printer total (all Tranche 2 base) | | 4 printers | 3× base + 1× sunk | **$1,197 new** |

### 2.2 Breakeven Analysis — 4-Printer Farm

**At 4 printers producing 560 units/month (80% utilization, demand-capped early Phase 2):**

| Revenue / Cost Item | Monthly Value |
|---|---|
| Gross revenue (560 units × $27.50 AOV) | $15,400 |
| Filament COGS (560 × $0.90) | ($504) |
| Platform fees (560 × $3.85) | ($2,156) |
| Packaging (560 × $0.08) | ($45) |
| Shipping (560 × $4.60) | ($2,576) |
| Labor / post-processing (560 × $0.65) | ($364) |
| Software (SimplyPrint $10) | ($10) |
| **Gross profit** | **$9,745/month** |
| **Gross margin** | **63.3%** |
| Tranche 2 hardware payback ($1,197) | **~7 days** |

**Note:** At Phase 2 entry, demand will constrain output below 560 units. A more conservative 200 units/month early demand scenario:
- Revenue: $5,500
- COGS + fees + shipping: ($3,400)
- Gross profit: ~$2,100/month
- Hardware payback: ~17 days

Payback is fast under any realistic demand scenario. Hardware capital is not the constraint — demand building is.

### 2.3 SimplyPrint Cost-Benefit at 4-Printer Scale

| Scenario | Monthly Cost | Benefit | ROI |
|---|---|---|---|
| SimplyPrint Starter ($10/month, up to 10 printers) | $10 | AI failure detection catches 1 failed overnight print per month | 1 failure = ~$2.60 material saved + 4 hours × $15 opportunity cost = $62.60 value |
| Bambu Farm Manager (free) | $0 | LAN monitoring, batch dispatch, no AI detection | Misses overnight failures; ~$62.60/month in avoidable losses |
| **Net value of SimplyPrint over free alternative** | | | **+$52.60/month net** |

SimplyPrint at $10/month is the correct choice from the moment 3 printers are operational. The AI failure detection alone justifies it by preventing one overnight failure per month.

---

## Section 3: Trademark Filing — Costs, Timeline, and Decision

### 3.1 Filing Cost

**Single class, Section 1(a) use-in-commerce application (recommended if any Etsy sale has occurred):**

| Fee Item | Amount | Notes |
|---|---|---|
| Base application fee (per class) | $350 | Current USPTO fee effective February 18, 2025 |
| Surcharge for ID Manual compliance failure | $0 | Avoided by using exact ID Manual language |
| Surcharge for free-form goods description | $0 | Avoided by using ID Manual |
| Statement of Use (Section 1(b) only) | $150 | Applicable ONLY if filing Section 1(b) Intent-to-Use |
| Attorney fee (optional) | $800–2,500 | DIY is viable for a clean word mark like MODRUN |
| **Total DIY Section 1(a)** | **$350** | |
| **Total DIY Section 1(b)** | **$500** | Includes Statement of Use when products launch |
| **Total with attorney** | **$1,150–2,850** | Adds certainty against Office Actions |

**Class recommendation:** International Class 20 only — "cable management clips made of plastic; desk organizer accessories made of plastic; non-electric cable organizing accessories made of plastic." Single class, $350. Class 9 (digital STL files) is a Phase 3+ consideration if digital file sales materialize.

### 3.2 Standard Timeline vs. Expedite Options

| Path | Filing | Examination | Publication | Registration | Total |
|---|---|---|---|---|---|
| **Standard (recommended)** | June 1 | 8–10 months | Month 11–13 | Month 14–16 | Aug–Oct 2027 |
| **Track One (USPTO Prioritized Exam)** | June 1 | ~6 months | Month 7–9 | Month 10–12 | Apr–Jun 2027 |
| Section 1(b) + conversion | June 1 | 8–10 months + SoU step | Month 14–16 | Month 17–19 | Nov 2027–Jan 2028 |

**Track One (USPTO Prioritized Examination):**
- Additional fee: $200/class (total $550 vs. $350)
- Compresses first examination from 8–10 months to ~6 months
- Reduces total timeline by approximately 3–4 months
- **Recommended for ModRun?** Yes, if Amazon Brand Registry enrollment is time-critical. However, the pending application serial number is sufficient for Amazon Brand Registry — Track One only accelerates the final registration date, not the Brand Registry unlock. Standard track at $350 is sufficient.

**Cost-benefit of Track One ($200 additional):**
- Benefit: Registration arrives April–June 2027 vs. August–October 2027 (4 months earlier)
- Value of 4 months earlier registration: Earlier access to anti-counterfeiting tools and brand enforcement on Amazon. Worth $200 if competitors are already copying products; less critical if market is uncrowded.
- **Recommendation:** File standard track ($350) on June 1. If a copycat appears on Amazon or Etsy by Q3 2026, consider filing Track One for a second mark or paying the $200 upgrade if USPTO allows it during examination.

### 3.3 Amazon Brand Registry Unlock

**Critical point:** Filing date = Brand Registry day. The pending trademark serial number (assigned same day as filing) is sufficient to enroll in Amazon Brand Registry. Registration is not required.

| Milestone | Date | Action |
|---|---|---|
| File trademark (Standard, $350) | June 1 | Serial number assigned same day |
| Apply for Amazon Brand Registry | June 1–2 | Use serial number at brandregistry.amazon.com |
| Brand Registry approval | June 2–15 (typically 1–14 days) | Unlocks Vine, A+ content, brand storefront |
| Vine enrollment | June 15–July 1 | Enroll Amazon ASIN; request 30 Vine units |
| First Vine reviews live | July 15–August 15 | Cold-start social proof for Amazon listing |

**Brand Registry is the primary business reason to file the trademark now** — not legal protection (which arrives at registration 14+ months later).

### 3.4 Expedite Analysis Summary

| Option | Cost | Total Timeline | Brand Registry | Recommendation |
|---|---|---|---|---|
| Standard 1(a) | $350 | ~16 months to registration | Day 0 (serial number) | **Best choice for ModRun** |
| Track One 1(a) | $550 | ~12 months to registration | Day 0 (serial number) | Use only if copycat threat materializes |
| With attorney (Standard) | $1,150–2,850 | ~16 months | Day 0 | Use if TESS search finds potential conflicts |
| Section 1(b) Intent-to-Use | $350 + $150 SoU = $500 | ~18–20 months | Day 0 | Use only if no Etsy sales exist yet |

**File June 1, standard track, $350.**

---

## Section 4: Filament Inventory Planning

### 4.1 Initial 30kg Inventory (June 1 Order)

**Colors and rationale (from production velocity data and ModRun product mix):**

| Color | kg Ordered | Monthly Consumption (4 printers, Phase 2) | Weeks of Stock | Reason |
|---|---|---|---|---|
| Black | 10kg | 20–25 kg/month (40–50% of volume) | ~2–2.5 weeks | Highest velocity; most cable runs are black |
| White | 10kg | 12–15 kg/month (25–30%) | ~3–4 weeks | Second highest; high review visibility |
| Grey | 10kg | 8–10 kg/month (20%) | ~4–5 weeks | Third; professional neutral for office installations |
| **Total** | **30kg** | **40–50 kg/month** | | |

**Reorder threshold:** Reorder when any color drops below 5 kg on-hand. At 4-printer Phase 2 volumes, black will hit this threshold in approximately 2 weeks — meaning a standing weekly reorder of 10kg black (Amazon, Prime) is appropriate from Day 1.

**Safety stock rule:** Never fall below 2 weeks of supply on any production color. At 50 kg/month (Phase 2 full), 2 weeks = ~25 kg total. The initial 30kg order provides this buffer for approximately 3 weeks until consumption patterns are confirmed.

### 4.2 Anycubic Pallet — Contingent Inventory Strategy

**Decision tree:**
- Order 10kg Anycubic sample on June 3 ($105)
- Run AMS validation test June 10 (3-hour production run, document feed error count)
- **If pass (zero AMS feed errors):** Order 50kg pallet on June 20 ($524.73)
- **If fail:** Exclude Anycubic; maintain eSUN Amazon as sole commodity source

**Pallet economics if validated:**
- 50kg pallet at $10.49/kg vs. eSUN 10kg bundle at $12/kg = saves $1.51/kg × 50 kg = $75.50 per pallet order
- At 25 kg/month Anycubic allocation (Phase 2 full), quarterly pallet ($524.73) vs. equivalent eSUN bundles ($450) = marginal $75 savings
- Primary value: supply chain diversification, not price savings — reduces dependence on eSUN Amazon availability

### 4.3 100–200 kg Initial Inventory (Phase 3 Planning)

**Phase 3 (8 printers, ~100 kg/month) initial inventory position:**

The PHASE_2_SUPPLIER_PRESTAGING_STRATEGY.md calls for pre-staging 90–165 kg by end of July to cover the August–September ramp without supply chain gaps. Specific composition:

| Item | Qty | Cost | Order Date |
|---|---|---|---|
| eSUN black 10kg (× 2 cases) | 20kg | $220–260 | June 1 |
| eSUN white 10kg (× 1 case) | 10kg | $110–130 | June 1 |
| eSUN grey 10kg (× 1 case) | 10kg | $110–130 | June 1 |
| Anycubic 10kg test sample | 10kg | $105 | June 3 |
| Anycubic 50kg pallet (if validated) | 50kg | $525 | June 20 |
| Polymaker PolyLite PLA white/grey | 67kg | $1,000 | August 1 |
| **Total filament pre-staged by August 1** | **167kg** | **$2,070–2,150** | |

**Storage requirements at 167 kg:**
- Active Sunlu S4 dry box capacity: 4–6 spools (4–6 kg)
- Airtight bin storage: 30 kg per standard 66-quart bin × 3 bins = 90 kg
- Open shelf (sealed bags): remaining 71 kg
- Industrial dry cabinet (Phase 3 investment): $400–700 for 60–100 kg capacity

**Rotation strategy:**
1. First-In-First-Out (FIFO) strictly enforced — date each box on receipt
2. Polymaker vacuum-sealed spools: store in sealed foil until loaded into Sunlu S4 for print run
3. eSUN/Anycubic: transfer to airtight bin with fresh desiccant pack on arrival; do not open until production run
4. After opening: load into Sunlu S4 immediately; print within 7 days; discard (or dry-test) any opened spool stored unsealed for more than 3 days above 50% RH

---

## Section 5: June–July Capital Deployment Calendar

### 5.1 Week-by-Week Deployment (June 1 – July 15)

| Date | Item | Amount | Gate | Cumulative Deployed |
|---|---|---|---|---|
| **June 1** | Trademark filing (USPTO, Class 20) | $350 | None | $350 |
| **June 1** | eSUN 30kg filament (Amazon Prime) | $360 | None | $710 |
| **June 1** | Packaging: 1,000 poly mailers + thermal labels | $65 | None | $775 |
| **June 1** | Email MatterHackers + Bambu B2B (quotes only) | $0 | None | $775 |
| **June 1** | Register Polymaker wholesale account | $0 | None | $775 |
| **June 3** | Phase 1 validation assumed complete | $0 | Phase 1 gate | $775 |
| **June 3** | Anycubic 10kg validation sample | $105 | None | $880 |
| **June 3** | Email Polymaker introduction | $0 | None | $880 |
| **June 5** | Select printer vendor (MatterHackers vs. Bambu B2B) | $0 | Quote received | $880 |
| **June 5** | Place Tranche 2 printer order (3× P1S base) | $1,197 | Phase 1 gate | **$2,077** |
| **June 7** | eSUN direct wholesale inquiry email | $0 | None | $2,077 |
| **June 8** | Dynamism benchmark quote request | $0 | None | $2,077 |
| **June 10** | Anycubic AMS validation test | $0 | Sample arrived | $2,077 |
| **June 12** | Printer arrival (MatterHackers, 3 units) | (already paid) | | $2,077 |
| **June 15** | SimplyPrint Starter activation | $10 | Printers installed | $2,087 |
| **June 15** | File Polymaker sample request if not yet received | $0 | | $2,087 |
| **June 20** | Anycubic 50kg pallet (if validation passed) | $525 | AMS test pass | **$2,612** |
| **June 22** | Consumables kit: 24 nozzles, PTFE, cartridges, plates | $684 | Printers installed | **$3,296** |
| **June 28** | Polymaker volume discount negotiation email | $0 | | $3,296 |
| **July 1** | Phase 2 30-day review checkpoint | $0 | | $3,296 |
| **July 1** | Tranche 3 printer decision (1 more P1S if demand gate met) | $0–399 | Demand gate | $3,296–3,695 |
| **July 15** | 4-printer farm operational target | (running costs only) | | Target met |

### 5.2 Capital by Month

| Month | Hardware | Filament | Trademark | Consumables | Software | Total |
|---|---|---|---|---|---|---|
| June (deployment) | $1,197 | $465 | $350 | $684 | $10 | **$2,706** |
| June (if Anycubic validated) | $1,197 | $990 | $350 | $684 | $10 | **$3,231** |
| July (Tranche 3 if gate met) | $399 | $460 | $0 | $100 | $10 | **$969** |
| July (no Tranche 3) | $0 | $460 | $0 | $100 | $10 | **$570** |

**Running monthly operating costs (post-capital deployment, 4 printers):**
- Filament (eSUN Amazon + Anycubic blend): ~$460–520/month at 50 kg/month
- Software (SimplyPrint): $10/month
- Packaging (1,000 mailers/month at $0.06–0.08): $60–80/month
- **Total monthly operating costs (non-labor):** ~$530–610/month

---

## Section 6: Funding Scenarios

### 6.1 Scenario A — Full Bootstrap from Phase 1 Revenue

**Assumption:** Phase 1 Etsy launch (May 30+) generates $400–600 in gross profit before June 3 Phase 2 start date.

**Capital sequence:**
1. Pre-Phase 1: $0 deployed (waiting for test print)
2. June 1 (independent of Phase 1 revenue): $775 deployed (trademark + filament + packaging) from personal cash
3. June 3–5 (post-Phase 1 gate): $1,197 printer Tranche 2 — sourced from personal credit card, repaid from Phase 1 revenue within 30 days
4. June 22 (consumables kit): $684 — sourced from combined Phase 1 revenue + operating cash

**Bootstrap feasibility:** The $775 June 1 deployment is non-negotiable for the trademark filing (highest-priority action). This is funded from personal savings, not Phase 1 revenue. The printer Tranche 2 ($1,197) is the first large deployment and the one most likely to require a short-term credit card bridge. Payback from Phase 2 printer output arrives within 7–17 days of printers becoming operational.

**Cash flow projection:**
- June 1–14: Deploy $2,072 ($775 non-dependent + $1,197 printers + $100 misc)
- June 15–July 1: 4 printers generate ~200 units/month at Phase 2 ramp entry = ~$5,500 revenue − $3,400 COGS = ~$2,100 gross profit for the period
- By July 1: Cash flow positive; consumables kit ($684) funded from operations
- **Bootstrap verdict: Viable.** No external funding required if printers are purchased on a credit card with 30-day grace period.

### 6.2 Scenario B — Phase 2 Funded from External Source

**If personal savings or cash are insufficient for the printer Tranche 2 ($1,197):**

| Option | Amount | Cost | Timeline | Notes |
|---|---|---|---|---|
| Business credit card (0% APR intro) | $1,200–2,000 | $0 for 12–15 months | Immediate | Best option — no interest during intro period; payback in 7–17 days from operations |
| Personal credit card | $1,200 | 20–28% APR; ~$20–30 if paid in 30 days | Immediate | Acceptable for 30-day bridge; pay in full by statement close |
| Business line of credit (LLC/DBA) | $2,000–5,000 | 8–12% APR | 2–4 weeks to establish | Best for Phase 3 printer tranches; start application now |
| Small business microloan (Kiva US) | $5,000 | 0% interest | 2–8 weeks | Non-dilutive; slow; use for Phase 3 only |
| Crowdfunding (Kickstarter/IGG) | Variable | ~5–8% platform fee | 30–60 days | Inappropriate for Phase 2 — too slow and too much operational distraction |

**Recommendation:** Personal or business credit card for the June printer purchase; apply for a business line of credit now for Phase 3 tranche funding. A $5,000 LOC at an established bank or credit union covers Tranche 3 (printers 5–8) without touching personal savings.

### 6.3 Scenario C — Phased Capital Deployment (Conservative)

**If risk tolerance is low and capital is truly limited:**

Deploy in three sub-phases, each funded by the previous phase's revenue:

**Sub-Phase 2A (June 1–15, ~$1,200):**
- Trademark ($350) + filament ($360) + packaging ($65) + 1× additional P1S ($399) = $1,174
- 2-printer farm operation begins immediately
- Revenue from 2 printers: ~$2,700 gross profit/month at 100 units/month demand
- Fund Sub-Phase 2B from this revenue

**Sub-Phase 2B (June 15–30, ~$400):**
- +1 additional P1S ($399) + SimplyPrint ($10) = $409
- 3-printer farm operational by June 22
- Revenue from 3 printers: ~$4,100 gross profit/month at 150 units/month

**Sub-Phase 2C (July 1–15, ~$400):**
- +1 final P1S ($399) = $399 (4-printer target met)
- 4-printer farm operational by July 15
- Revenue baseline: ~$5,400 gross profit/month at 200 units/month

**Conservative scenario total capital deployed by July 15:** ~$2,000 (all sourced from personal cash + Phase 1 revenue)

**Trade-off:** Conservative scenario delays 4-printer operational readiness by 4–6 weeks vs. purchasing Tranche 2 as a 3-printer block on June 3. At $2,800/month incremental revenue per 2 additional printers, the 4-week delay costs approximately $700 in foregone gross profit — more than the amount saved by conservative sequencing. The credit card bridge (Scenario B) is economically superior to conservative sequential deployment.

---

## Section 7: Trademark Filing Decision — Expedite vs. Standard

### 7.1 Decision Framework

| Factor | Standard ($350) | Track One Expedite ($550) |
|---|---|---|
| Brand Registry unlock | Day 0 (serial number) — identical | Day 0 (serial number) — identical |
| First examination | 8–10 months | ~6 months |
| Estimated registration | August–October 2027 | April–June 2027 |
| Months saved | — | 3–4 months |
| Extra cost | — | $200 |
| Value of 4 months earlier: anti-counterfeiting tools | Depends on competitor threat | Depends on competitor threat |

**Decision rule:**
- If no competitors are selling ModRun-branded knockoffs by September 2026: File standard ($350). Save $200.
- If a copycat appears on Etsy or Amazon using "ModRun" or a confusingly similar brand by September 2026: Upgrade to Track One in the next filing (or pay the Track One upgrade fee mid-examination if USPTO allows it). The anti-counterfeiting tools that arrive with registration are the primary value.
- If Amazon Brand Registry access is the only urgent goal: File standard. Brand Registry unlocks on Day 0 regardless of track.

**Verdict: File standard track on June 1. Save the $200. Monitor for copycats. Reassess Track One upgrade in Q3 2026.**

### 7.2 Second Class Consideration (Class 9 — Digital Files)

If ModRun begins selling digital STL/3MF files for 3D printing (a future Phase 3+ revenue stream):
- File a second trademark application in International Class 9 ("downloadable design files for three-dimensional printing")
- Cost: additional $350 (standard track)
- Timing: File when digital file revenue exceeds $500/month — not before
- This is not a June 2026 action

---

## Section 8: Working Capital — Operations Buffer

### 8.1 Reserve Allocation

| Reserve Purpose | Amount | Release Condition |
|---|---|---|
| Printer failure / emergency replacement part | $100 | Any production-stopping hardware failure requiring an unplanned part |
| Phase 1 redesign delay (if needed) | $75 | If test print requires a design revision, print another test batch |
| Filament stockout bridge (emergency 1-week supply) | $50 | If eSUN Amazon is out of stock on a critical color |
| Returns and refunds buffer (first 60 days) | $50 | Expected 2–3% return rate on first 100 Etsy orders |
| Ad spend overage (if Amazon PPC spike) | $50 | If CPC exceeds bid cap and daily spend spikes |
| **Total working capital reserve** | **$325** | Released only on condition; not routine operating expense |

### 8.2 Break-Even at 4-Printer Scale

**At 100 units/month (conservative Phase 2 entry demand):**

| Line Item | Monthly |
|---|---|
| Revenue (100 × $27.50) | $2,750 |
| Filament COGS (100 × $0.90) | ($90) |
| Platform fees (100 × $3.85) | ($385) |
| Packaging (100 × $0.08) | ($8) |
| Shipping (100 × $4.60) | ($460) |
| Software (SimplyPrint) | ($10) |
| Filament inventory restock | ($120) |
| **Net operating income** | **$1,677** |

**At 300 units/month (moderate Phase 2 traction):**

| Line Item | Monthly |
|---|---|
| Revenue (300 × $27.50) | $8,250 |
| COGS + fees + shipping (300 × $9.43 total per-unit cost) | ($2,829) |
| Software | ($10) |
| Filament restock | ($270) |
| **Net operating income** | **$5,141** |

**4-printer hardware amortization:** At $1,197 total hardware investment and $5,141/month net at 300 units/month demand, the hardware is recovered in approximately 7 days of operation. Capital is not the risk — demand growth rate is.

---

## Section 9: Summary Timeline for July 15 Operational Readiness

| Milestone | Target Date | Capital Required | Status |
|---|---|---|---|
| Trademark filed (Class 20, standard) | June 1 | $350 | Gate: None |
| Amazon Brand Registry applied | June 1–2 | $0 | Gate: Serial number received |
| eSUN 30kg filament ordered | June 1 | $360 | Gate: None |
| Polymaker wholesale account registered | June 1 | $0 | Gate: None |
| MatterHackers + Bambu B2B quotes requested | June 1 | $0 | Gate: None |
| Anycubic 10kg AMS validation ordered | June 3 | $105 | Gate: None |
| Phase 1 test-print validation confirmed | June 3 | $0 | Gate: Test print |
| Tranche 2 printer order placed (3× P1S) | June 3–5 | $1,197 | Gate: Phase 1 validation |
| Brand Registry approval received | June 3–15 | $0 | Gate: Amazon review |
| SimplyPrint Starter activated | June 15 | $10 | Gate: Printers installed |
| Anycubic AMS validation test | June 10 | $0 | Gate: Sample arrived |
| Anycubic 50kg pallet ordered (if pass) | June 20 | $525 | Gate: AMS validation |
| Printers arrive + installed | June 12–22 | (paid) | Gate: Lead time |
| Consumables kit ordered (24 nozzles, PTFE, etc.) | June 22 | $684 | Gate: Printers installed |
| Polymaker volume discount conversation | June 28 | $0 | Gate: Account registered |
| 4-printer farm fully operational | **July 15** | | Target |
| **Total capital deployed by July 15** | | **$3,231–$3,931** | |

---

## Sources

- [USPTO Trademark Fee Schedule (Effective February 18, 2025)](https://www.uspto.gov/learning-and-resources/fees-and-payment/uspto-fee-schedule)
- [USPTO Summary of 2025 Trademark Fee Changes](https://www.uspto.gov/trademarks/fees-payment-information/summary-2025-trademark-fee-changes)
- [USPTO Track One Prioritized Examination](https://www.uspto.gov/trademarks/apply/prioritized-examination-track-one)
- [Amazon Brand Registry Requirements 2026](https://brandregistry.amazon.com)
- [Bambu Lab P1S Pricing — US Store](https://us.store.bambulab.com/products/p1s)
- [Bambu Lab P1S Price History 2026](https://originalpricing.com/bambu-lab-printer-prices/)
- [Polymaker US Wholesale Portal](https://us-wholesale.polymaker.com/)
- [Polymaker Wholesale FAQ](https://us-wholesale.polymaker.com/pages/wholesale-faq)
- [Anycubic 50–100kg PLA Deals](https://store.anycubic.com/products/pla-basic-50-100kg-deals)
- [SimplyPrint Pricing 2026](https://simplyprint.io/pricing)
- [Kiva US Small Business Microloans](https://www.kiva.org/borrow/us)
- [USPTO Trademark Budget Calculator 2026](https://trademarkbudget.com/)
- Internal: TRADEMARK_FILING_STRATEGY.md, PHASE_2_CAPITAL_DEPLOYMENT_TIMELINE.md, PRINTER_FARM_EQUIPMENT_SPECIFICATIONS.md (Section 6 — cost summary tables), MULTI_PRINTER_SCALING_ROADMAP.md (Section 2.1 — hardware economics, Section 3 — implementation timeline)
