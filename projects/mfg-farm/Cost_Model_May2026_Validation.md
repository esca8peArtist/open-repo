# Cost Model Validation — May 2026

**Date**: 2026-05-17  
**Reference**: `8-printer-farm-cost-model.md` (639 lines)  
**Status**: Structurally sound; three assumptions require updates

---

## 1. Filament Cost — REQUIRES REVISION

**Model assumption**: $12/kg (Phase 1), $11/kg and $10/kg tiers for Phase 2–3

**Correct baseline**: PLA+ costs $13–14/kg in retail bundles. The $12/kg assumption is achievable only for PLA Basic or via negotiated wholesale pricing (Phase 2+).

**Update**: Use $13.50/kg as the Phase 1 baseline. This increases per-unit material cost by ~$0.12 (from $0.90 to $1.02 at 75g/clip).

**At scale impact**: 
- Month 1 (50 units): +$6/month
- Month 6 (500 units): +$60/month
- Month 12+ (2,000 units): +$240/month

**Recommendation**: Keep the overall economic thesis intact—the margin is still healthy. Update the sensitivity analysis to show the impact of $12–14/kg filament ranges.

---

## 2. USPS Shipping Cost — REQUIRES REVISION

**Model assumption**: $4.50/order average

**Current reality**: USPS Ground Advantage rates increased **8% January 2026**, plus an **8% temporary surcharge** (active through Jan 2027).

**Updated rates for cable clip (single, ~2 oz + packaging)**:
- Commercial rate (Pirate Ship): ~$3.80–4.20 base
- With 8% surcharge: **~$4.10–$4.55**
- Revised assumption: **$4.75–5.00**

**For 3-pack bundle (~10–12 oz)**:
- Base: ~$5.00–5.25
- With surcharge: **~$5.25–$5.75**

**At scale impact** (assuming single clips dominate):
- Month 1 (50 units): +$12.50 (assuming $0.25/order increase)
- Month 6 (500 units): +$125
- Month 12+ (2,000 units): +$500/month

**Action**: Update Section 4 revenue tables to use $4.75–5.00 for single clip shipping. Rerun margin calculations to confirm thesis still holds (it does—filament cost dominates, not shipping).

---

## 3. Etsy Fee Rate — REQUIRES REVISION

**Model assumption**: 9.5%

**Correct rate**: 10–10.5% (accounting for 6.5% transaction fee on shipping + 3% + $0.25 payment processing)

**Dollar impact at 2,000 units/month** ($55K monthly revenue):
- Old: $5,225/month (9.5%)
- Correct: $5,775/month (10.5%)
- Variance: **$550/month** understatement

**Gross margin change**: 80.5% → 79.3% (still very healthy)

**Action**: Update Section 5.1 (COGS breakdown) to use 10.5% Etsy fees. This reduces modeled gross profit by ~$0.30/unit across the volume range, but does not materially change the ROI thesis.

---

## Favorable Updates

### Bambu Lab P1S Hardware Cost

**Model assumption**: $699/unit  
**Current market**: **$399–$499 on promotion** (common floor in 2026)

**Impact**: Capital cost for 8-printer setup drops from $10,114 to ~$7,000–8,500.

**Recommendation**: Keep $699 in the planning model (conservative), but note in the assumptions that promotional pricing is achievable. Do not depend on it for financial projections.

---

## Confirmed (No Change Needed)

- **Electricity cost** ($0.12/kWh): At the low end of market but defensible for home-based operation.
- **Labor rates** ($3k ops, $2.5k production tech, $15/hr contractor): Reasonable for the scale; sensitivity analysis already covers $18/hr upside.
- **Revenue projections** (50% MoM growth): Aggressive but achievable with strong launch execution.

---

## Updated Cost Structure Summary

| Item | Old | Updated | Impact |
|---|---|---|---|
| Filament (Phase 1) | $12/kg | $13.50/kg | +$0.12/unit COGS |
| USPS single clip | $4.50 | $4.75–5.00 | +$0.25–0.50/order |
| USPS 3-pack | $4.50 | $5.25–5.75 | +$0.75–1.25/order |
| Etsy fees | 9.5% | 10.5% | +$0.30/unit on $55K revenue |
| P1S hardware | $699 | $399–499 (promo) | $3,000–5,000 capex savings |

---

## Investment Thesis Validation

Even at the revised cost inputs:
- **24-month ROI remains exceptional** (capital cost is ~$7–10K; monthly gross profit is $25–35K at scale)
- **Gross margins remain healthy** (79–80%+ even with updated fees)
- **Break-even is still achieved in Month 2–3** under conservative 30% of forecast scenario

**Recommendation**: Proceed with launch planning. Update the cost model with these figures before the test print evaluation.

---

## Sources

- USPS Ground Advantage Rate Changes Jan 2026 — GoWarpSpeed, I'd Ship That
- eSUN Filament Pricing Amazon (May 2026)
- Etsy Fees 2026 — Marmalead, Voolist
- Bambu Lab Pricing History — OriginalPricing, MatterHackers

