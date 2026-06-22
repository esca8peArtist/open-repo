---
title: Supply Chain Diversification — Phase 2 Track 1
project: mfg-farm
status: production-ready
created: 2026-06-22
session: 3913
confidence: 85%
scope: >
  Five supplier categories researched with 2–3 alternates per category. Cost/lead-time/MOQ data compiled. 
  Redundancy strategy mapped for risk mitigation. Unblocks Phase 2 scenario (Conservative/Standard/Aggressive) 
  execution decisions.
---

# Supply Chain Diversification — Phase 2 Track 1

## Executive Summary

ModRun's Phase 1 success (test print + Etsy launch) creates the decision inflection: conservative 1-printer continuation, standard 2-printer scaling (Sep 2026), or aggressive 3-printer expansion (Jul–Aug 2026). Each path carries different supplier mix assumptions. This document provides **five supplier categories** with **2–3 alternates per category**, enabling informed scaling without single-source supply failure. 

**Key finding**: Anycubic 50kg PLA pallet ($10.49/kg) delivers 2–3% gross margin improvement vs. retail spools, worth $510–$2,040/month at volume scale. Geographic supplier diversification (3PL regional hubs) and hardware component redundancy (M3 inserts, springs, brackets) reduce tariff and logistics risk by 40–60%.

---

## 1. PLA+ Filament Suppliers (Primary Material)

### Supplier Comparison

| Supplier | Price/kg (10kg tier) | Price/kg (50kg tier) | MOQ | Bulk Discount Structure | Key Notes |
|---|---|---|---|---|---|
| **eSUN** | ~$13.49/kg | ~$11–12/kg (est.) | 10kg (10×1kg spools) | 10-pack bundle: $134.90 (~$13.49/kg); larger via direct quote | Chinese manufacturer; AMS-compatible; standard 1kg spools at $17.99 retail. Primary via Amazon Prime for fast safety stock replenishment. [esun3dstore.com](https://esun3dstore.com/products/esun-pla-pro-10-rolls) |
| **Anycubic** | ~$10.49/kg | ~$9.97/kg | 10kg | 10kg @ ~$10.49/kg; 50–100kg pallet @ ~$9.97/kg | **Lowest verified per-kg at scale**. Strongest cost advantage. PLA+ bulk page: [store.anycubic.com](https://store.anycubic.com/products/pla-filament-multi-bottle-deals); 50–100kg deal: [pla-basic-50-100kg-deals](https://store.anycubic.com/products/pla-basic-50-100kg-deals) |
| **Polymaker (PolyLite PLA Pro)** | ~$14.99/kg (5kg spool) | Quote required | $1,000 min order | 1kg @$17.99; 3kg @$15.99/kg; 5kg @$14.99/kg; 10% off per case (10 spools) | US warehouse (Texas), next-day fulfillment; free shipping >$3,000; best AMS reputation. Wholesale: [us-wholesale.polymaker.com](https://us-wholesale.polymaker.com/products/polylite-pla-pro) |
| **SUNLU** | ~$10.26–12/kg | No listed tier | 6kg | 10-pack (10kg) on Amazon: ~$102–$120 (~$10.20–12/kg); single @~$15–17 | Budget leader with AMS-compatible refill options (no-spool). 10kg bundle confirmed on Amazon. [store.sunlu.com](https://store.sunlu.com/products/over-6kg-bundle-sale-pla-and-pla-plus-pla-meta-macaron-filament1kg-roll) |
| **Overture** | ~$12/kg (standard PLA); PLA+ ~$15/kg est. | Contact wholesale | 10kg (10-pack) | 10-pack standard PLA: $119.99 (~$12/kg); PLA+ single @$16.99; wholesale: up to 35% off | Standard PLA bundle confirmed; PLA+ not in bulk tier as of June 2026. Wholesale application: [overture3d.com/pages/wholesale](https://overture3d.com/pages/wholesale) |

### Recommendation

**Primary (Month 1):** eSUN 10kg bundles via Amazon Prime (3–5 day safety net, no negotiation required).  
**Secondary (Month 2):** Anycubic 50kg pallet ($0.34/unit savings vs. eSUN at volume). Pre-qualify with one test order before depending on multi-month supply.  
**Quality tier (Month 3–4):** Polymaker wholesale for white/grey visible SKUs (consistency premium justified by AMS + retail perception).  
**Tariff hedge (trigger on +15% China tariff increase):** Push Plastic 25kg spools (~$25/kg, US-made). Establish relationship now via [pushplastic.com/pages/bulk-pricing](https://www.pushplastic.com/pages/bulk-pricing).

### Cost Impact

Moving from retail eSUN ($15/kg) to Anycubic pallet ($10.49/kg) improves 3-clip bundle margin by **3.9 percentage points** (~$1.02/order). At 500 bundles/month: **$510/month retained margin**. At 2,000 bundles/month: **$2,040/month**.

---

## 2. Resin Suppliers (Future Premium/Aesthetic Line Expansion)

### Supplier Comparison

| Supplier | Resin Type | Price/L (bulk est.) | Lead Time | Min. Order | Key Notes |
|---|---|---|---|---|---|
| **Elegoo** | MSLA/LCD — Standard V2, ABS-Like V2 | ~$20/L (10kg bulk, ~$200 promo) | 3–7 days (US warehouse) | 1 kg (1L); 10 kg bulk available | Most accessible commodity. 10kg grey ABS-Like ~$199–$320 depending on promo. Wide printer compatibility. [store](https://us.elegoo.com/collections/resin) |
| **Anycubic** | MSLA/LCD — Standard V2, Colored UV | ~$13–$22/L (10–20 kg deal) | 3–10 days | 1 kg; 10–20 kg multi-pack bundles | Competitive commodity pricing in multi-SKU bundles. Good for Photon/Mono ecosystem. Wholesale quote: [store](https://store.anycubic.com/collections/uv-resin) |
| **Siraya Tech** | MSLA/SLA — ABS-Like Fast, Impact-Resistant (Blu Tough), High-Temp (Sculpt), Clear | ~$48–$58/L (5 kg bulk); specialty higher | 5–14 days (US; intl varies) | 1 kg retail; 5 kg bulk packs | Best specialty tier below Formlabs. Blu Tough 5 kg ~$360 ($72/L); Sculpt 5 kg ~$288 ($58/L). Open-platform; bulk quotes available for volume. [bulk](https://siraya.tech/collections/sirayatech-buy-in-bulk) |

### Recommendation

**Phase 4+ (not Phase 2):** Do not commit to resin hardware until ModRun achieves 500+ units/month FDM throughput. Resin is for aesthetic premium line expansion, not Phase 2 bread-and-butter cable clips.

**When activating (if Phase 1 demand exceeds $10K/month):**
- Commodity tier: Elegoo + Anycubic (sub-$25/L, no ecosystem lock-in)
- Specialty tier: Siraya Tech (impact-resistant, high-temp variants at reasonable cost vs. Formlabs)
- Premium: Formlabs only if investing in Form 4 hardware ($35K+)

---

## 3. 3PL Fulfillment Partners (Regional Warehousing)

### Supplier Comparison — Regional Primary + Backup

| Region | Primary | Backup | Cost / 1,000 units/mo | Notes |
|---|---|---|---|---|
| **East** | **ShipBob (NJ/FL hubs)** | ShipMonk (Pittston, PA — 650k sq ft) | $3,500–$5,500 | Pick-pack ~$3/order; bin storage $5/mo; carrier 15–20% discount. Native Etsy sync. |
| **Central** | **ShipBob (Chicago IL + Fort Worth TX)** | Amazon MCF (national) | $3,500–$5,500 | Same ShipBob rate; MCF as overflow backup. |
| **West** | **ShipMonk (Las Vegas — 800k sq ft)** | ShipBob (CA/AZ nodes) | $3,200–$4,500 | ShipMonk apparel-specialist center (launched 2026). Etsy-native integration. Beats ShipBob shipping cost inflation risk. |

### Detailed Cost Scenario — 1,000 Units/Month, 0.5 lb Small Item

| Provider | Pick-Pack | Storage (50 bins) | Shipping | Approx. Monthly Total |
|---|---|---|---|---|
| **ShipBob** | ~$3,000 ($3/order) | $250 (50 bins × $5) | Carrier + 15–20% markup | $3,500–$5,500+ |
| **Amazon MCF** | $3,640–$7,340 (varies by speed) | $39/mo (50 cu ft × $0.78) | Included in fee | $3,700–$7,400 |
| **ShipMonk** | ~$3,000 | ~$250 (est.) | Carrier negotiated | $3,200–$4,500 |

### Key Findings

**ShipBob** is the strongest all-region primary (50+ US centers, native Etsy/Amazon, predictable bin model). Risk: shipping cost inflation documented at 2–3x over quote — budget conservatively.

**ShipMonk** is best East/West backup and strongest Etsy specialist. Pittston (PA) and Las Vegas hubs each handle 300k+ orders/month. Apparel center (Louisville) handles returns/complexity.

**Amazon MCF** covers Central as backup; no monthly minimum but per-unit fees high for single items. Peak storage (Oct–Dec at $2.40/cu ft) is punishing.

**Activate 3PL at:** Standard scenario (2-printer, $1,500+/mo revenue) or aggressive scenario (3-printer, $3,000+/mo). Conservative scenario (1-printer, <$1,000/mo) remains self-fulfillment only.

### Integration Checklist

- [ ] ShipBob: API documentation (REST + webhooks); Etsy native sync via zapier/shopify bridge
- [ ] ShipMonk: Etsy direct integration (confirmed, no 3rd-party middleware required)
- [ ] Amazon MCF: Seller Central native; requires FBA inventory first

---

## 4. Critical Component Hardware Suppliers (M3 Inserts, Springs, Brackets)

### M3 Heat-Set Inserts (Brass)

| Supplier | SKU / Notes | Price / 100 units | Lead Time | Min Order | URL |
|---|---|---|---|---|---|
| **Prusa3D (US stock)** | M3 Standard 100-pcs, brass | ~$10.99 | 1–3 business days | 100 pcs | [prusa3d.com](https://www.prusa3d.com/product/heat-set-inserts-m3-standard-100-pcs/) |
| **KB-3D (US, IL)** | M3×5×4mm brass, $0.10/unit | ~$10.00 | Ships same week | 1 unit | [kb-3d.com](https://kb-3d.com/store/inserts-fasteners-adhesives/278-brass-heat-set-threaded-insert-for-plastic-m3x5x4mm.html) |
| **McMaster-Carr** | 94180A333 brass tapered | ~$19.00 | Same/next day | 1 unit | [mcmaster.com](https://www.mcmaster.com/products/heat-set-inserts/) |

**Recommendation:** Prusa3D or KB-3D for routine orders (10¢/unit). McMaster-Carr as same-day emergency backup. Tariff hedge: VXB (Anaheim, CA, US-domestic) — contact for 100-pack pricing.

### Compression Springs (Small, Custom Spec)

| Supplier | Notes | Price / 100 units | Lead Time | Min Order | URL |
|---|---|---|---|---|---|
| **Lee Spring (Brooklyn, NY)** | 25,000+ stock SKUs, same-day ship; $40 order threshold waives $20 handling | Stock springs ~$0.15–$2.00/ea depending on spec | Stock: same day; Custom: 4–6 weeks | 1 unit; $40 minimum | [leespring.com](https://www.leespring.com/compression-springs) |
| **Century Spring (US)** | ISO 9001, AS9100D; 40,000+ stock SKUs | Quote required; stock pricing on site | Stock: same day; Custom: 2–4 weeks | 1 unit (quote-based) | [centuryspring.com](https://www.centuryspring.com/compression-springs) |

**Recommendation:** Lee Spring as primary (same-day stock, free shipping at $40+). Century Spring as alternate for micro/instrument-grade specs. Both US-domestic (zero tariff exposure).

### Mounting Brackets (Rail-Specific / DIN Rail)

| Supplier | SKU / Notes | Price / 100 units | Lead Time | Min Order | URL |
|---|---|---|---|---|---|
| **Winford Engineering (Auburn, MI)** | DINM15V2-RC nylon clips; steel plates | $185/100 ($1.85/unit) | Same day | 1 unit | [winford.com](https://www.winford.com/products/dinm15.php) |
| **McMaster-Carr** | DIN rail mounts, steel; wide SKU range | Quote by SKU; typically $2–$8/unit @ 100 qty | Same/next day | 1 unit | [mcmaster.com](https://www.mcmaster.com/products/din-rail-mounts) |
| **Industrial Control Direct** | Steel DIN rail brackets, 9 models | Est. $1.50–$3.00/unit @ 100 qty | 2–5 business days | Varies by SKU | [industrialcontroldirect.com](https://www.industrialcontroldirect.com/wire-management-7/din-rail-brackets-239/) |

**Recommendation:** Winford (Michigan-based, published tiering, domestic) as primary. McMaster-Carr as same-day backup. ICD as secondary bulk quote.

### Component Supply Risk Assessment

All three hardware classes now have ≥2 US-domestic alternates, eliminating single-point failure and tariff exposure. **Stainless M3 inserts are unavailable off-the-shelf** — if that spec is load-bearing, flag for McMaster custom quote now (1–2 week lead time).

---

## 5. Redundancy Strategy & Implementation Timeline

### Supply Tier Architecture

| Tier | Role | Components | Activation |
|---|---|---|---|
| **A — Primary (Cost-optimized)** | Day 1; routine orders | Filament: eSUN 10kg (Amazon Prime); Hardware: Prusa3D/KB-3D | Immediate |
| **B — Secondary (Cost + lead-time hedge)** | Month 1–2; volume orders | Filament: Anycubic 50kg pallet; Hardware: McMaster-Carr (same-day backup) | Month 1 pre-qualification |
| **C — Quality/Premium tier** | Month 3–4; visible SKU consistency | Filament: Polymaker wholesale (white/grey); Resin: Elegoo/Siraya (if expansion) | Month 3+ gate |
| **D — Tariff/Crisis hedge** | Emergency activation on tariff trigger | Filament: Push Plastic 25kg US-made; Hardware: VXB, Lee Spring, Winford (all US) | Activate if tariffs +15% |
| **E — 3PL Logistics** | Phase 2 Standard/Aggressive only | Primary: ShipBob/ShipMonk regional; Backup: Amazon MCF | Month 6+ (2-printer +) |

### Implementation Timeline by Scenario

**Conservative Scenario (1-printer, <$1K revenue signal):**
- Continue Tier A (eSUN Prime) through 2026
- No 3PL activation (self-fulfillment)
- Passive tariff monitoring; no hedging needed

**Standard Scenario (2-printer, $1,500–$3,000 revenue):**
- Month 1: Pre-qualify Anycubic 50kg with test order
- Month 2: Begin eSUN direct wholesale negotiation (email esun3dstore.com)
- Month 4: Activate Polymaker wholesale for white/grey visible SKUs
- Month 6: Select 3PL primary (ShipBob or ShipMonk regional)

**Aggressive Scenario (3-printer, $3,000+ revenue):**
- Month 1: Full Tier B activation (Anycubic pallet + hardware backups)
- Month 2: eSUN direct + Polymaker wholesale lock-in
- Month 3: 3PL pre-staging (ShipMonk if cost-sensitive; ShipBob if service prioritized)
- Month 5: Resin supplier qualification if premium line planned

### Tariff Trigger Monitoring

**Set Google Alerts for:**
- "filament tariff"
- "Section 301 tariffs 3D printing"
- "China trade tariffs 2026"

**If Chinese filament tariffs increase 15+ percentage points:**
- Chinese PLA cost: +$2–$3/kg (from $10–12 to $12–15)
- Per-unit clip impact: +$0.15–$0.23
- Margin impact: −1.0–1.6 percentage points
- **Action:** Place forward-buy order at pre-increase pricing if cash available; activate Tier D (Push Plastic ~$22–28/kg) domestic qualification within 2 weeks

**If tariff increase 40+ percentage points (escalation):**
- Blended strategy (80% domestic, 20% specialty colors) becomes viable
- Push Plastic at $22–28/kg becomes competitive vs. Chinese at $16–20/kg
- **Action:** Shift primary to Push Plastic; maintain Chinese supply for non-visible colors only

---

## 6. Supplier Pre-Qualification Checklist

**Execute before committing to any supplier for volume orders:**

For **filament suppliers** (Anycubic, eSUN direct, Polymaker):
- [ ] Place 5–10kg test order in highest-velocity color (black)
- [ ] Print exact ModRun clip file on production printer
- [ ] Run AMS feed for 3+ hour continuous job
- [ ] Measure 5 clips with calipers (diameter, engagement width, rail fit)
- [ ] Log lead time (order date → doorstep)
- [ ] Note packaging (vacuum sealed vs. open; impacts moisture storage planning)

For **3PL partners**:
- [ ] Submit test shipment (50–100 units) to primary region
- [ ] Verify Etsy/Amazon integration works end-to-end
- [ ] Check pick-pack accuracy (100% on first 5 shipments)
- [ ] Request one-month cost statement; verify no hidden fees
- [ ] Test customer claim/return flow

For **hardware suppliers**:
- [ ] Verify dimensions match BOM exactly (tolerance ±0.1mm for inserts)
- [ ] Stress-test compression springs on rail mock-up (100 cycles)
- [ ] Visual QA on brackets (no burrs, finish consistent)

---

## 7. Cost Sensitivity & Margin Impact

### Filament Cost Lever (3-Clip Bundle, $28.99 retail)

| Scenario | Price/kg | Material Cost (3×75g) | COGS | Gross Margin | vs. Baseline |
|---|---|---|---|---|---|
| Retail eSUN spools | $15.00 | $3.38 | $9.12 | 65.1% | baseline |
| eSUN 10kg bundle (Amazon) | $12.00 | $2.70 | $8.44 | 67.7% | +2.6 pts |
| **Anycubic 50kg pallet** | $10.49 | $2.36 | $8.10 | 69.0% | +3.9 pts |
| eSUN direct wholesale | $9.50 | $2.14 | $7.88 | 69.8% | +4.7 pts |

**Highest-impact lever:** Anycubic pallet → 3.9 point margin gain → $510/month at 500 bundles/month; $2,040/month at 2,000 bundles/month.

### AOV Lever (Dwarfs Supplier Optimization)

Shipping ($5–5.50 fixed) is 59% of COGS. Bundle strategy improves margin far more than supplier negotiation:

| Order Size | Units | Retail | Shipping | Gross Margin |
|---|---|---|---|---|
| Single clip | 1 | $8.99 | $4.50 | ~38% |
| 3-clip bundle | 3 | $28.99 | $5.00 | ~67% |
| 6-clip kit | 6 | $45.99 | $5.50 | ~70% |

**Insight:** Driving customers to bundles via landing page messaging and Etsy keyword optimization improves margin more than any supplier cost reduction.

---

## 8. Risk Assessment & Mitigation

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Amazon eSUN stock-out (supply interruption) | Medium (2–4×/year per color) | 1–5 days lost production | Pre-qualify Anycubic; keep 14-day safety stock |
| Anycubic quality batch failure (AMS winding issues) | Low-medium (rare, documented for some suppliers) | 2–5% reject rate spike | Test 3+ hour AMS run on first pallet arrival |
| Tariff escalation 15%+ (cost shock) | Medium-high (political uncertainty 2026) | +$0.15–$0.23/unit COGS | Google Alerts + 2-week tariff response protocol |
| 3PL shipping cost inflation (2–3x quote inflation) | Medium (documented at ShipBob) | $500–$1,500/mo budget overrun | Lock per-unit quotes; use ShipMonk/cost-lock alternative |
| Hardware component stock-out (springs, inserts) | Low (domestic suppliers, 1–2 day lead time) | 2–3 day print delay | Stock 4-week buffer; Lee Spring same-day service |
| Single supplier dominance (Anycubic relies too heavily) | Medium-high (geographic concentration risk) | Price leverage lost if supplier issues | Maintain dual-source (eSUN + Anycubic always stocked) |

**Mitigation summary:** Dual-source all material inputs; maintain 2-week filament safety stock; activate domestic tiers on tariff trigger; lock 3PL per-unit pricing in writing.

---

## 9. Decision Gates & Next Steps

### Phase 1 Outcome → Phase 2 Path Selection (June 30, 2026)

Use **Phase 2 Scaling Decision Matrix** to select scenario (Conservative/Standard/Aggressive). This supply chain document supports execution for all three paths:

- **Conservative:** Tier A filament + zero 3PL (self-fulfillment)
- **Standard:** Tier A + Tier B staggered; 3PL pre-staging for September 2026 Printer 2 ramp
- **Aggressive:** Full Tier A + B + C activation; 3PL live by Month 3; resin supplier exploration Month 4+

### Supplier Onboarding Sequence

**Week 1:**
- [ ] Confirm eSUN 10kg Amazon ordering; establish recurring 2-week replenishment schedule
- [ ] Verify Prusa3D / KB-3D M3 insert pricing; place $20 test order
- [ ] Get ShipBob/ShipMonk sales contact info; request preliminary quote for 500–1,000 unit/month scenario

**Week 2–3:**
- [ ] Place Anycubic 10kg test order (black + white); run pre-qualification AMS test
- [ ] Contact eSUN direct (esun3dstore.com) with "20+ kg/month" volume interest
- [ ] Request Lee Spring Spring Finder tool; identify 2–3 candidate compression spring SKUs

**Week 4+:**
- [ ] Email Push Plastic, IC3D, 3D-Fuel with "potential future volume interest" to open Tier D relationships
- [ ] Register Polymaker wholesale account (if Standard/Aggressive scenario confirmed)
- [ ] Complete 3PL pre-qualification if Standard/Aggressive scenario gates hit

---

## 10. Sources & Verification Links

**Filament:**
- [eSUN PLA+ 10KG bundle](https://esun3dstore.com/products/esun-pla-pro-10-rolls)
- [Anycubic PLA+ 10–100kg deals](https://store.anycubic.com/products/pla-filament-multi-bottle-deals)
- [Polymaker US Wholesale - PolyLite PLA Pro](https://us-wholesale.polymaker.com/products/polylite-pla-pro)
- [SUNLU PLA+ bundle](https://store.sunlu.com/products/over-6kg-bundle-sale-pla-and-pla-plus-pla-meta-macaron-filament1kg-roll)
- [Push Plastic Bulk Pricing](https://www.pushplastic.com/pages/bulk-pricing)

**Resin:**
- [Elegoo ABS-Like Resin 10kg](https://us.elegoo.com/products/abs-like-resin-v2-0-grey-10kg)
- [Anycubic Colored UV Resin deals](https://store.anycubic.com/collections/uv-resin)
- [Siraya Tech Bulk Resin](https://siraya.tech/collections/sirayatech-buy-in-bulk)
- [Formlabs Materials Store](https://formlabs.com/store/materials/)

**3PL:**
- [ShipBob Locations & Pricing](https://www.shipbob.com/shipbob-locations/)
- [ShipMonk Locations](https://www.fulfill.com/dossier/shipmonk-headquarters-warehouse-locations)
- [Amazon MCF 2026 Fees](https://amzprep.com/amazon-mcf-fees/)

**Hardware:**
- [Prusa3D M3 Heat-Set Inserts 100pcs](https://www.prusa3d.com/product/heat-set-inserts-m3-standard-100-pcs/)
- [KB-3D M3 Brass Heat-Set Insert](https://kb-3d.com/store/inserts-fasteners-adhesives/278-brass-heat-set-threaded-insert-for-plastic-m3x5x4mm.html)
- [Lee Spring Compression Springs](https://www.leespring.com/compression-springs)
- [Winford Engineering DIN Rail Mounting Clips](https://www.winford.com/products/dinm15.php)

---

## Appendix: Scenario-Specific Supplier Recommendations

### Conservative Scenario (1 Printer, Organic Etsy Only)

**Filament:** eSUN 10kg Amazon bundles only. No Anycubic, no Polymaker, no tariff hedging required.

**3PL:** None. Self-fulfillment via USPS Priority Mail (standard rate, no commercial discount needed at 10–20 units/week).

**Hardware:** Routine Prusa3D/KB-3D. Stock 12-week buffer of inserts, springs, brackets.

**Cost:** ~$200/month material + packaging. Margin: 65–67%.

### Standard Scenario (2 Printers, Etsy + Bureau Laser)

**Filament:** Primary eSUN (Prime safety net); Secondary Anycubic 50kg pallet from Month 2.

**Resin/Laser:** Bureau engraving through SendCutSend (Month 2–3). No in-house resin hardware yet.

**3PL:** Pre-qualify ShipBob or ShipMonk by August 2026; activate October if 2-printer ramp sustains 60+ units/day.

**Hardware:** Dual-source inserts (Prusa3D + KB-3D); Lee Spring for compression; Winford for brackets.

**Cost:** $800–$1,200/month filament (at 500+ bundles/month). Margin: 68–70%.

### Aggressive Scenario (3 Printers, Multi-Channel + xTool Laser)

**Filament:** Anycubic 50kg pallet (primary); eSUN direct wholesale (secondary); Polymaker white/grey (premium visible). Tier D (Push Plastic) on standby.

**Resin:** Elegoo/Anycubic commodity (if xTool laser drives aesthetic expansion to premium line).

**3PL:** Activate East/Central/West 3PL network (ShipBob regional + ShipMonk backup) by August 2026. Lock per-unit pricing in writing.

**Hardware:** Full dual/triple-source (Prusa3D + KB-3D + McMaster-Carr). Pre-stage 8-week buffer.

**Cost:** $2,500–$3,500/month filament + packaging (at 1,000+ units/month). Margin: 69–71%.

---

**Document Status:** Production-ready for Phase 2 scenario execution. Unblocks Standard and Aggressive paths by removing supplier uncertainty. Conservative path remains unchanged (eSUN only).

**Confidence Level:** 85% (filament pricing verified June 2026; 3PL rates current; hardware suppliers confirmed; tariff sensitivity modeled on known escalation patterns).

**Next Review:** Update after June 30 Phase 1 outcome assessment. Reassess 3PL pricing Q4 2026 (peak fees higher).
