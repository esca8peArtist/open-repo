# Supplier Scorecard Update — May 2026

**Date**: 2026-05-17  
**Reference**: `supplier-negotiation-playbook-consolidated.md`  
**Status**: Key vendors verified; one critical pricing update

## eSUN PLA+ Filament — PRICING UPDATE REQUIRED

**Scorecard assumption**: $11–12/kg  
**Current market reality**: **$13–14/kg** for PLA+ (10kg bundles on Amazon)

### What happened:

The scorecard appears to have confused **PLA Basic** (ASIN B0G2KSS613, ~$9.50/kg) with **PLA+** (ASIN B0G2KWC5XL, ~$13.60/kg).

- eSUN 10kg PLA+ bundle: **$135.84** (5% Amazon discount) = **$13.58/kg**
- eSUN 10kg PLA Basic bundle: ~$94.99 = ~$9.50/kg

### Impact on COGS:

At 75g per cable clip:
- Old calculation: 75g × $0.012/g = **$0.90/unit**
- New calculation: 75g × $0.01360/g = **$1.02/unit**
- **Cost increase: +$0.12/unit** (13% higher)

At 50 units/month: +$6/month (negligible)  
At 2,000 units/month: +$240/month (notable)

**Action**: Update the cost model to use **$13–14/kg as the Phase 1 baseline** for PLA+. The $11–12/kg tier is achievable only via negotiated wholesale pricing (Phase 2+), not through retail channels like Amazon.

---

## MatterHackers Retail — Confirmed Within Range

**Scorecard assumption**: $19–21/kg  
**Current pricing**: $22.99/kg (single spool), bulk discount to $19.31/kg

**Assessment**: The wholesale negotiation target ($16–18/kg via sales email) remains realistic. No change needed.

**Lead time & Quality**: Confirmed consistent with prior ratings (1–2 weeks domestic, high AMS compatibility).

---

## Polymaker Wholesale — Significantly Higher Than Assumed

**Scorecard assumption**: $10.49/kg (May 2026 sale pricing)  
**Current market**: **$17.99/kg** at wholesale site (28% off MSRP, regularly $24.99)

**Note**: This is for **Phase 3+ only** (deferred until $1,000 MOQ is justified). The Phase 1–2 strategy remains eSUN + MatterHackers. No immediate action needed, but update Phase 3 cost projections to expect $16–18/kg, not $10–11/kg.

---

## Supply Chain Context

No significant disruptions to PLA+ supply as of May 2026. Tariff risk (China-sourced filament) remains an active concern per the cost model's own analysis. The dual-sourcing strategy (eSUN + MatterHackers) is appropriate for this risk profile.

---

## Summary

| Vendor | Assumption | Current | Action |
|---|---|---|---|
| eSUN PLA+ | $11–12/kg | $13–14/kg | Update Phase 1 baseline |
| MatterHackers | $19–21/kg | $22.99 retail, $19.31 bulk | No change |
| Polymaker | $10.49/kg | $17.99/kg | Update Phase 3 only |

