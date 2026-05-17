---
title: Launch Readiness Validation — Post-Test-Print Materials Audit
project: mfg-farm
created: 2026-05-17
updated: 2026-05-17
status: VALIDATED — 3 action items required before execution
scope: Etsy checklist UI drift, supplier scorecard accuracy, cost model assumption verification
---

# Launch Readiness Validation — Post-Test-Print Materials Audit

**Date**: May 17, 2026
**Validator**: Research Agent (automated, sourced)
**Status**: Ready for immediate launch post-test-print — with 3 mandatory updates noted below

---

## Executive Summary

- **Etsy checklist**: Largely accurate. Two material gaps found: (1) the $15 identity verification / setup fee is not mentioned anywhere in the checklist — new shops will hit this surprise cost at onboarding; (2) subcategory selection is now mandatory in the listing form, which affects the documented Home Organization path. Both are low-effort fixes. (VERIFIED May 17, 2026)
- **Supplier scorecard**: Filament cost assumptions are materially optimistic. US tariffs pushed eSUN PLA+ single-spool pricing to approximately $18–22/kg retail, well above the $11–13/kg documented baseline. The 10kg bulk bundle pricing appears partially intact but requires verification. Pirate Ship shipping rates are confirmed accurate within the documented $3.50–6.00 range with the April 2026 8% surcharge already baked into rates. (MEDIUM confidence — Amazon direct pricing blocked; sourced from third-party trackers and industry reports)
- **Cost model**: Electricity assumption ($0.12/kWh) is outdated — US commercial average is now $0.14/kWh and residential is $0.18/kWh. Bambu P1S equipment price assumption ($699) is correct but promotional pricing is now frequently $399–$499, improving ROI. Filament cost assumptions at $12/kg are the most significant model risk: single-spool retail has increased ~50–70% due to tariffs, but bulk/bundle pricing through established channels remains more stable. The USPS cost model needs a ~21% cumulative rate increase acknowledgment.

---

## Section 1: Etsy Shop Setup Checklist Validation

**Document reviewed**: `etsy-listing-launch-checklist.md` (648 lines, v1.0)

### Confirmed Accurate (VERIFIED May 17, 2026)

- **Transaction fee rate (9.5%)**: Confirmed. Etsy charges 6.5% transaction + 3% + $0.25 payment processing on US sales. The checklist's 9.5% aggregate is a reasonable rounded working number. No fee increase announced for 2026.
- **13 tags allowed**: Confirmed still accurate as of May 2026.
- **140-character title limit**: Confirmed; first 70 characters dominate search display.
- **5,000-character description limit**: Confirmed.
- **Photo minimums and format (JPG, 500×500px minimum)**: Confirmed.
- **Shop announcement character limit (200 characters)**: Confirmed still accurate.
- **AI-generated background prohibition (June 2025 policy)**: Confirmed — this policy remains active in May 2026.
- **Category: Home & Living > Home Organization > Storage & Organization**: The category path exists and is appropriate. 3D-printed home organization products are a confirmed market on Etsy in 2026.

### UI Drift Found — Action Required

**Finding 1 — Missing: $15 Setup Fee + Identity Verification (HIGH PRIORITY)**

Etsy introduced a one-time setup fee ranging from $15–$29 (depending on region and fraud-risk profile) for new shops, plus mandatory photo-ID verification via Persona (third-party). The fee is non-refundable. Neither requirement appears anywhere in the checklist's Section 1.2 (Shop Standards & Billing) or Section 9 (Pre-Launch Final Checklist).

Action: Add to Section 1.2 and Section 9:
- "One-time Etsy setup fee: $15–$29 (charged at shop creation; non-refundable)"
- "Identity verification: Upload government-issued photo ID + selfie via Persona (required before shop goes live)"

Confidence: HIGH — confirmed via Etsy official handbook, eRank, and multiple seller community sources. (as of May 17, 2026)

**Finding 2 — Changed: Subcategory Selection Now Mandatory**

Etsy's listing form now requires subcategory selection — sellers can no longer submit a listing with only a top-level category selected. The listing form prefills some fields from existing listings and has removed the separate Materials tag field (materials now captured only via the Materials attribute). The checklist's Section 3.3 documents the category path but does not note that subcategory is mandatory and that failing to select one will block listing publication.

Action: Add note to Section 3.3: "Subcategory selection is now required — Etsy will block listing publication if only the top-level category is selected. Choose the most specific subcategory available."

Confidence: HIGH — confirmed via Etsy seller handbook and multiple 2026 seller guides. (as of May 17, 2026)

**Finding 3 — Changed: Listing Form Now Asks Production Method**

The updated listing form requires sellers to answer how items were made: "made from scratch," "assembled from purchased parts," "altered," or "curated sets." It also asks whether AI tools were used in design creation. 3D-printed items using the seller's original design are fully compliant. The checklist does not mention this disclosure step.

Action: Add to Section 3.3 or Section 6.3 Pre-Launch Final Checklist: "Complete production method disclosure in listing form: select '3D printed from original design.' Disclose if AI was used in design."

Confidence: HIGH — confirmed via Marmalead policy update and Etsy seller handbook. (as of May 17, 2026)

**Finding 4 — Shipping Rates: 21% Cumulative Increase Not Reflected**

The checklist documents USPS Ground Advantage as the primary shipping method and cites $4.50 as an example Zone 4 rate. USPS implemented a 7.8–12.2% increase on January 18, 2026, followed by an 8% temporary surcharge on April 26, 2026 (active through January 17, 2027). Combined, lightweight sub-1-lb packages have increased approximately 21% year-over-year. The Pirate Ship commercial discount partially offsets this. A third-party guide confirms Ground Advantage at approximately $4.25 for 8 oz, Zone 4 via Pirate Ship. The checklist's $4.50 estimate remains in the right ballpark but should be understood as the lower bound.

Action: Note in Section 5.3 and Section 1.1: "USPS Ground Advantage rates increased ~21% cumulatively since Jan 2026. Current Pirate Ship commercial rate for a typical 50g clip (under 2 oz, Zone 4) is estimated at $3.80–4.50. Validate at pirateship.com before setting flat shipping price."

Confidence: MEDIUM — percentage increases confirmed via USPS official and Stamps.com; exact current dollar rates for sub-2oz packages not directly confirmed due to Pirate Ship rate wall.

### No Action Needed

- Marmalead and eRank recommended in Appendix A: Both tools remain active in 2026.
- Snapseed and Lightroom Mobile recommended in Appendix B: Both remain free and available.
- Conversion benchmarks in Appendix C: Figures are plausible for 2026 market context and not contradicted by any current sources.

---

## Section 2: Supplier Scorecard Validation

**Document reviewed**: `supplier-scorecard.csv` (14 rows)

Vendors audited: eSUN, Overture, Polymaker, Pirate Ship (4 vendors)

### eSUN (Primary Filament Supplier — Row 2)

**Documented**: $11–13/kg (10 spool / 10kg Amazon bundle tier)

**Current finding**: Tariffs have significantly impacted eSUN retail single-spool pricing. Multiple industry sources (LayerDepth review, 3DPrintedDecor guide, general market reports from Feb–May 2026) consistently cite eSUN PLA+ at $16–22/kg for 1kg spools on Amazon. A price tracker source found eSUN PLA Basic at $17.99 for a 1kg spool. European market data shows eSUN spools jumping from €15–16 to €25–26 in early 2026. US 10kg bundle pricing appears more stable due to bulk warehouse inventory effects, but current pricing for B0G2KWC5XL (the documented PLA+ 10kg bundle ASIN) could not be directly confirmed — Amazon blocked direct fetch.

**Verdict**: PRICE CHANGE — single-spool retail is approximately 40–70% higher than documented. 10kg bulk bundle pricing unclear. Recommend spot-checking bundle ASIN B0G2KWC5XL before ordering.

**Updated estimate**: $15–18/kg for bulk 10kg bundle (was $11–13/kg). Per-unit filament cost impact: +$0.03–0.07/unit for a 75g clip.

Confidence: MEDIUM (retail increase confirmed via multiple independent sources; bulk bundle exact price not directly verified)

### Overture (PETG + PLA Backup — Row 5)

**Documented**: $11–14/kg PLA, $17–19/kg PETG; 35% off wholesale program

**Current finding**: No contradicting data found. Overture is US-distributed and partially domestic-manufactured, giving it some tariff insulation. General market reports confirm Overture remains competitive. The 35% wholesale program was not independently verified as currently active.

**Verdict**: PRICES LIKELY STABLE — no evidence of major price change beyond general market drift. Wholesale program status unconfirmed.

Confidence: LOW (no current direct price data retrieved for this vendor)

### Polymaker (Phase 3 Quality Tier — Row 4)

**Documented**: $14.99/kg (case), Net 30, ~$1,000 MOQ

**Current finding**: Polymaker announced a minimum 10% price increase effective May 1, 2025, citing tariff pressures. By May 2026, this increase has been in effect for over a year and the documented $14.99/kg likely reflects pre-increase pricing.

**Verdict**: PRICE CHANGE — documented $14.99/kg is likely now $16.50–18/kg. Verify via Polymaker wholesale portal before activating in Phase 3.

Confidence: MEDIUM (May 2025 increase confirmed via market reports; exact May 2026 wholesale price not directly fetched)

### Pirate Ship (Primary Shipping Platform — Row 7)

**Documented**: $3.50–6.00/label, 8% temporary surcharge Apr 26 – Jan 17, 2027 already baked into rates

**Current finding**: Confirmed. The scorecard already documented the April 2026 surcharge. A third-party 2026 shipping guide confirmed Ground Advantage at approximately $4.25 for an 8 oz, Zone 4 package via Pirate Ship. The $3.50–6.00 range remains accurate for the ModRun product weight profile.

**Verdict**: CONFIRMED ACCURATE. No action required.

Confidence: HIGH (range confirmed via multiple 2026 sources; exact sub-2oz rate not directly confirmed but within documented range)

### Summary

4 vendors checked, 2 price changes, 0 lead time updates.

| Vendor | Documented Price | Current Estimate | Change | Confidence |
|--------|-----------------|-----------------|--------|------------|
| eSUN PLA+ 10kg bulk | $11–13/kg | $15–18/kg | +~40% | Medium |
| Overture PLA/PETG | $11–14 / $17–19/kg | Likely stable | ~0% | Low |
| Polymaker wholesale | $14.99/kg | ~$16.50–18/kg | +~10–20% | Medium |
| Pirate Ship Ground Advantage | $3.50–6.00/label | Confirmed in range | 0% | High |

Verification date: May 17, 2026

---

## Section 3: Cost Model Assumptions Verification

**Document reviewed**: `8-printer-farm-cost-model.md` (639 lines, v1.0)

### Assumption 1: Filament Cost — $12/kg eSUN bulk

**Documented basis**: eSUN bulk pricing at 75+ kg/month volume; 10–20kg tier at $12.50/kg

**Verification**: As noted in Section 2, tariffs have pushed eSUN retail pricing to $16–22/kg for 1kg spools. Bulk 10kg bundle pricing is more stable but likely in the $15–18/kg range vs. the documented $11–13/kg. The model's $12/kg working assumption is based on volume purchasing at 75+ kg/month — a scale not yet reached at Phase 1 launch. For Phase 1 (10–20kg/month), the realistic cost is closer to $15–18/kg.

**Updated assumption**: $15–18/kg for Phase 1 launch (was $12/kg). At Phase 4 (150+ kg/month with wholesale negotiation), $12–14/kg may be achievable but cannot be assumed.

**Impact on model**: At 50 units/month (Phase 1), each 75g clip uses $0.075 of filament at $12/kg vs. $0.11–0.14 at $15–18/kg. COGS increases ~$0.03–0.06/unit — minor at small scale, but the model's $12/kg baseline should be updated for Phase 1 planning.

Confidence: MEDIUM — tariff impact confirmed broadly; exact bulk bundle price requires direct spot check

**Status**: UPDATED — $12/kg is now optimistic for Phase 1; model should use $15–18/kg for launch planning.

### Assumption 2: Shipping Cost — $4.50/order average (USPS Ground Advantage)

**Documented basis**: USPS Ground Advantage, Zone 4 average

**Verification**: The January 2026 USPS rate increase (7.8–12.2%) plus April 2026 temporary 8% surcharge combine to approximately 21% cumulative increase year-over-year for sub-1-lb packages. A 50g clip in basic packaging is approximately 1.5–2 oz total. A third-party guide confirmed commercial Ground Advantage at approximately $4.25 for 8 oz, Zone 4 via Pirate Ship. Sub-2oz packages would be somewhat cheaper. The $4.50 estimate remains reasonable as a national average assumption (blending near and far zones) but should be validated at pirateship.com before setting fixed shipping prices.

**Status**: VERIFIED within range — $4.50 is a defensible national average for a single clip order. 3-pack order (3 clips, ~200g shipped) would be closer to $5.00–5.50 at current rates.

Confidence: MEDIUM — directional confirmation only; exact sub-2oz rate not directly confirmed

### Assumption 3: Electricity — $0.12/kWh

**Documented basis**: "US average commercial rate: $0.12/kWh"

**Verification**: The US commercial average electricity rate as of May 2026 is $0.14/kWh (up from $0.12 in prior years; a 5% year-over-year increase; confirmed via Electric Choice May 2026 data). The residential average is $0.18/kWh. Home-based operations (the model's Phase 1–3 assumption) would pay residential rates. The model uses the commercial rate, which understates cost for home-based operations.

**Updated assumption**:
- Home-based (Phase 1–3): $0.18/kWh (residential) — was $0.12/kWh
- Dedicated facility (Phase 4): $0.14/kWh (commercial) — was $0.12/kWh

**Impact on model at 8 printers**: Monthly electricity cost was modeled at $89/month at $0.12/kWh. At $0.18/kWh (residential), actual cost is ~$134/month. Per-unit electricity cost rises from $0.04 to $0.07/unit — still negligible relative to total COGS.

**Status**: UPDATED — $0.12/kWh is outdated. Home-based Phase 1–3 operations should use $0.18/kWh; facility-based Phase 4 should use $0.14/kWh. Financial impact is minor but the model should reflect accurate assumptions.

Confidence: HIGH — sourced from Electric Choice monthly rate tracker, May 2026, confirmed against EIA data.

### Assumption 4: Labor Rate — $15/hour

**Documented basis**: Owner opportunity cost and PT contractor rate

**Verification**: The model documents Phase 2 PT contractor labor at $15/hour. The federal minimum wage remains $7.25/hour as of May 2026, making $15/hour reasonable for light manufacturing/fulfillment work. No evidence of mandatory rate increases above $15/hour for this type of work at the national level. State and local minimums vary widely (California $16.50+, New York $16+). For a home-based operation in a lower-cost state, $15/hour is defensible. If operating in a high-cost state, budget $17–20/hour.

**Status**: VERIFIED — $15/hour is nationally accurate; adjust upward based on operating state minimum wage.

Confidence: MEDIUM — federal minimum confirmed; state-specific adjustment needed

### Assumption 5: Bambu Lab P1S Equipment Price — $699

**Documented basis**: Listed as $699 unit cost throughout capital tables

**Verification**: The Bambu Lab P1S officially carries a $699 MSRP, but promotional pricing has dropped it to $399 "so frequently that $699 feels like a distant memory" (originalpricing.com, May 2026). Amazon was confirmed at $399 as of May 13, 2026. The model's $699 assumption is conservative from an ROI perspective — if printers are acquired at $399–499 promotional pricing, the capital payback period shortens further.

**Updated assumption**: Use $399–$499 for acquisition planning if purchasing during promotional windows (common); keep $699 as conservative planning assumption for capital budgeting.

**Status**: VERIFIED CONSERVATIVE — $699 is correct MSRP; actual acquisition cost likely $100–300 lower, improving ROI.

Confidence: HIGH — multiple sources confirm promotional pricing at $399; MSRP at $699 confirmed.

### Assumption 6: Etsy Fees — 9.5%

**Documented basis**: "Etsy fees: 9.5% (transaction + payment processing)"

**Verification**: Etsy's current fee structure is 6.5% transaction fee + 3% + $0.25 payment processing (US). On a $14.99 item, this is 6.5% + 3% = 9.5% + $0.25 flat. The 9.5% approximation is accurate for items above ~$15 where the $0.25 flat becomes negligible. Additionally, sellers earning over $10,000/year face a mandatory Offsite Ads fee of 12–15% on sales attributed to Etsy's advertising. The model does not account for this; at scale, if >$10K revenue, budget an additional 1–2% blended fee impact.

**Status**: VERIFIED — 9.5% is accurate for Phase 1. Flag Offsite Ads fee for Phase 3+ modeling.

Confidence: HIGH — Etsy fees confirmed via official fee schedule and multiple 2026 sources.

### Summary of Cost Model Changes

| Assumption | Documented Value | Verified/Updated Value | Change | Impact |
|------------|-----------------|----------------------|--------|--------|
| Filament (Phase 1, retail) | $12/kg | $15–18/kg | +25–50% | +$0.03–0.06/unit COGS |
| Filament (Phase 4, wholesale) | $10/kg | $12–14/kg estimate | +20–40% | +$0.02–0.04/unit COGS |
| Electricity (home-based) | $0.12/kWh | $0.18/kWh | +50% | +$0.03/unit COGS (negligible) |
| Electricity (facility) | $0.12/kWh | $0.14/kWh | +17% | Negligible |
| Bambu P1S equipment | $699 | $399–699 (promo common) | 0 to -43% | Improves ROI |
| Etsy fees | 9.5% | 9.5% (+Offsite Ads at scale) | Verified | No change at Phase 1 |
| Labor | $15/hr | $15–20/hr (state-dependent) | 0–33% | Varies |
| Shipping average | $4.50/order | $4.25–5.50 depending on SKU | ~0–22% | Minor |

---

## Recommended Actions

**Priority 1 — Update Etsy checklist before execution (30 minutes work)**:
1. Add $15–29 setup fee and Persona identity verification requirement to Section 1.2 and Section 9 critical checklist
2. Add note that subcategory is mandatory in the listing form (Section 3.3)
3. Add production method disclosure reminder to Section 6.3 (3D printed from original design)
4. Update shipping cost guidance to note 21% USPS increase since 2025

**Priority 2 — Spot-check filament pricing before first order**:
- Visit amazon.com and check current prices for B0G2KWC5XL (eSUN PLA+ 10kg) and B0G2KSS613 (eSUN PLA Basic 10kg)
- If bulk price is above $15/kg, update COGS model in `8-printer-farm-cost-model.md` and `scaling-cost-model.csv`
- Consider domestic US suppliers (Polar Filament at ~$18–22/kg, Push Plastic) as tariff-insulated backup

**Priority 3 — Update electricity assumption in cost model**:
- Change $0.12/kWh to $0.18/kWh for home-based phases in `8-printer-farm-cost-model.md`
- Financial impact is small but the assumption should be accurate for credible projections

---

## Confidence Summary

| Validation Area | Confidence | Key Uncertainty |
|----------------|------------|-----------------|
| Etsy UI/policy verification | HIGH | UI drift findings confirmed via current seller guides |
| Filament pricing (retail) | MEDIUM | Amazon direct fetch failed; sourced from trackers + industry reports |
| Filament pricing (bulk) | LOW | Bulk 10kg bundle price not directly confirmed |
| USPS rate increase | HIGH | Confirmed via USPS official and Stamps.com |
| Electricity rates | HIGH | Confirmed via Electric Choice May 2026 data |
| Bambu P1S price | HIGH | Confirmed $399 promo / $699 MSRP via multiple sources |
| Etsy fees | HIGH | Confirmed via Etsy official fee schedule |

---

## Sources

- [Etsy Policy Changes 2026 — CEDCommerce](https://cedcommerce.com/blog/etsy-policy-changes-2026-what-shopify-etsy-sellers-must-fix-to-stay-compliant-visible-and-profitable/)
- [Etsy Policy Updates 2026 — Marmalead](https://blog.marmalead.com/etsy-policy-updates/)
- [Etsy Setup Fee — eRank Help](https://help.erank.com/blog/understanding-etsys-new-15-setup-fee/)
- [Etsy Fees 2026 — Printify](https://printify.com/blog/how-much-does-etsy-take-per-sale/)
- [Bambu Lab Printer Prices 2026 — originalpricing.com](https://originalpricing.com/bambu-lab-printer-prices/)
- [USPS 2026 Rate Hikes — Warpspeed](https://gowarpspeed.com/blog/usps-2026-rate-hikes)
- [2026 USPS Rate Changes — Stamps.com](https://www.stamps.com/article/2026-usps-rate-and-service-changes/)
- [Pirate Ship Ground Advantage Rates](https://www.pirateship.com/usps/ground-advantage)
- [Pirate Ship Rate Guide 2026 — ListingForge](https://www.listing-forge.com/blog/pirate-ship-shipping-rates)
- [Electricity Rates by State — Electric Choice, May 2026](https://www.electricchoice.com/electricity-prices-by-state/)
- [How Tariffs Are Reshaping Filament Market — Z-Ventures](https://z-ventures.cc/3d-printer-filament-tariffs/)
- [eSUN PLA+ Review 2026 — LayerDepth](https://layerdepth.com/reviews/esun-pla-plus/)
- [Filament Prices 2026 — LayerMath](https://layermath.com/filament-prices)
- [Tariffs Hit Hard: 3D Printer Prices — iFun3D](https://ifun3d.com/news/us-3d-printer-tariff-price-hike-vs-american-filament)
- [USPS Recommends Competitive Price Changes July 2026 — USPS Newsroom](https://about.usps.com/newsroom/national-releases/2026/0511-usps-recommends-competitive-price-changes-for-july-2026.htm)
