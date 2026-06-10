---
title: FDM Material Capability Matrix — Snap-Arm Clip Design
created: 2026-06-10
phase: Phase 2 contingency
scope: PLA+, ABS+, PETG for ModRun snap-arm clip
tolerance_target: 1.25–1.55 mm wall section
status: decision-support (do not purchase yet)
---

# FDM Material Capability Matrix — Snap-Arm 3D-Printed Clip

**Decision trigger:** Use this document when test print results arrive. Match observed dimensional output against the 1.25–1.55 mm target and cross-reference the failure modes listed below.

---

## 1. Mechanical Properties

All values from published datasheets and peer-reviewed literature (ResearchGate, Wevolver, Ultimaker). FDM-printed values are ~15–25% lower than injection-molded equivalents due to layer-bonding anisotropy.

| Property | PLA+ | ABS+ | PETG |
|---|---|---|---|
| Tensile Strength (MPa) | 50–60 | 34–40 | 40–55 |
| Elongation at Break (%) | 4–8 | 6–10 | 10–15 |
| Flexural Modulus (GPa) | 3.5–4.0 | 2.0–2.5 | 2.0–2.6 |
| Impact Resistance (kJ/m²) | Low (brittle) | Medium–High | Medium–High |
| Glass Transition Temp (°C) | 55–60 | 95–105 | 75–85 |
| Heat Deflection Temp (°C) | 52–58 | 88–98 | 65–72 |
| Layer Adhesion | Good | Good (warps) | Excellent |
| UV Stability | Poor | Poor–Fair | Fair |
| Chemical Resistance | Low | Moderate | Good |

**Key finding for snap-arm design:** PETG is the standout. Its 10–15% elongation at break means the snap arm can deflect and return without fracturing — critical for a reusable clip. PLA+'s 4–8% elongation means fracture risk at the root radius if the cantilever is thin. ABS+ matches PLA+ for snap-fit durability but requires an enclosure to print without warping.

---

## 2. Snap-Arm Feature Tolerance Analysis

**Target wall section:** 1.25–1.55 mm  
**Target clearance range:** 0.30–0.50 mm total (per snap-fit design conventions for FDM)

### FDM Dimensional Accuracy by Material

| Material | Typical X/Y Accuracy | Z Accuracy | Shrinkage | Post-Shrink Correction Needed? |
|---|---|---|---|---|
| PLA+ | ±0.10–0.20 mm | ±0.15–0.25 mm | 0.1–0.3% | Rarely |
| ABS+ | ±0.15–0.30 mm | ±0.20–0.35 mm | 0.8–1.6% | **Yes — scale model +1.2% in XY** |
| PETG | ±0.10–0.20 mm | ±0.15–0.25 mm | 0.2–0.5% | Occasionally (minor) |

**Implication for 1.25–1.55 mm target (0.30 mm window):**
- PLA+ and PETG can hit this window on a well-tuned printer without correction.
- ABS+ requires scaling and enclosure; its 0.3 mm window is eaten by thermal shrinkage variance alone. **ABS+ is disqualifying for this tolerance class unless you have an enclosed, temperature-controlled chamber with verified compensation dialed in.**

### Snap-Arm Design Rules Confirmed

From Protolabs Network, Hubs, and Mandarin3D:
- Minimum beam thickness at snap root: **1.0 mm** (our 1.25–1.55 mm target is safely above this)
- Taper the beam 50% from root to tip to distribute stress
- Fillet radius at root: minimum 0.5× beam thickness → at 1.4 mm wall, fillet ≥ 0.7 mm
- PETG: 1.5–2.5 mm arm thickness for hand-force assembly
- PLA+: increase thickness by ~20% vs PETG for equivalent fatigue life
- ABS+: requires orientation with layer lines parallel to flex direction

---

## 3. Print Reliability Score (0–10)

Scoring criteria: dimensional consistency, first-layer adhesion, warping risk, inter-layer bond strength, humidity sensitivity, failure rate in production conditions.

| Material | Score | Notes |
|---|---|---|
| PLA+ | 8.5/10 | Most forgiving; prints at 200–220°C; no heated chamber needed; brittle under cyclic flex |
| ABS+ | 5.0/10 | Warps without enclosure; acetone-smoothable; needs 240–260°C; 1.2% shrinkage is unpredictable without controlled airflow |
| PETG | 9.0/10 | Excellent layer adhesion; minimal warping; 230–250°C; slight stringing manageable with retraction; best all-round choice |

**Production farm note:** On a Bambu A1/P1S farm running unattended, PETG is significantly more reliable than ABS+ because it does not require chamber temperature management. First-print failure rates: PLA+ ~5%, PETG ~5–7% (stringing), ABS+ ~15–25% (warp/delamination).

---

## 4. Cost Per Part — Quantity Tiers

### Assumptions
- Clip volume: ~3.5 cm³ estimated (small snap-arm clip, ~4 g printed weight)
- Filament density: PLA 1.24 g/cm³, PETG 1.27 g/cm³, ABS 1.04 g/cm³
- Printed weight after 15% infill and supports: ~4–6 g per clip
- Using 5 g average for calculation
- Electricity: $0.16/kWh, printer 150W, ~15 min print time → $0.006/part (negligible, omitted below)
- Printer amortization and labor accounted in farm overhead (see 8-printer-farm-cost-model.md)

### Material Cost Per Part by Supplier (USD, per-gram basis, June 2026 pricing)

| Supplier | PLA+ $/kg | PETG $/kg | ABS+ $/kg | PLA+ per clip | PETG per clip | ABS+ per clip |
|---|---|---|---|---|---|---|
| Prusament | $38–42 | $38–44 | $36–40 | $0.19–0.21 | $0.19–0.22 | $0.18–0.20 |
| Bambu Lab | $27–32 | $28–33 | $26–30 | $0.14–0.16 | $0.14–0.17 | $0.13–0.15 |
| eSUN | $16–19 | $18–22 | $17–20 | $0.08–0.10 | $0.09–0.11 | $0.09–0.10 |
| Creality | $14–18 | $16–20 | $15–18 | $0.07–0.09 | $0.08–0.10 | $0.08–0.09 |
| MatterHackers PRO | $24–29 | $25–30 | $23–28 | $0.12–0.15 | $0.13–0.15 | $0.12–0.14 |

**Note:** Bambu Lab filament carries a 23% tariff-driven premium as of 2026 vs. pre-tariff pricing. eSUN and Creality filament is imported separately from printers and faces lower duties (~10% effective IEEPA rate post-truce) since filament is classified differently from electronics hardware.

### Scaled Cost Per Unit (Material Only, 5 g average clip, PETG)

| Supplier | 100 units | 1,000 units | 10,000 units |
|---|---|---|---|
| Prusament | $9.50–$11.00 | $95–$110 | $950–$1,100 |
| Bambu Lab | $7.00–$8.50 | $70–$85 | $700–$850 |
| eSUN | $4.50–$5.50 | $45–$55 | $450–$550 |
| Creality | $4.00–$5.00 | $40–$50 | $400–$500 |
| MatterHackers PRO | $6.50–$7.50 | $65–$75 | $650–$750 |

**Recommendation for cost-sensitive production:** eSUN or Creality PETG for bulk runs. Prusament for qualification/first-article prints where dimensional consistency needs to be documented.

---

## 5. Supplier Supply Chain — Lead Times (June 2026)

### Filament Lead Times to US Delivery

| Supplier | Country of Origin | USA Warehouse? | Standard Lead Time | Bulk Lead Time (>50 spools) | Tariff Risk |
|---|---|---|---|---|---|
| Prusament | Czech Republic (EU) | No — ships from Prague | 7–14 days | 10–21 days | Low (EU, not China); no Section 301 duty |
| Bambu Lab | China | **Yes** (US stock for common colors) | 2–5 days (stocked SKUs) | 7–14 days | Medium — IEEPA 10% + Section 301 in effect |
| eSUN | China | **Yes** (MatterHackers, Antinsky) | 3–7 days (via distributor) | 7–14 days | Medium — same tariff structure |
| Creality | China | Partial (limited colors) | 3–10 days | 10–21 days | Medium |
| MatterHackers PRO | USA-sourced / China-mfg | **Yes** (Lake Forest, CA) | 2–5 days | 3–7 days | Low (US warehouse, pre-landed) |

**Key risk:** Chinese filament lead times are stable now, but any escalation to 145% tariff rates (as briefly occurred in April 2025) would triple material costs overnight. Prusament and MatterHackers are the lowest-tariff-risk options. MatterHackers has domestic warehouse stock that insulates from sudden tariff shocks.

### Color/Variant Lead Time Notes

- Prusament: 15+ standard PETG colors in stock; custom/special orders 4–8 weeks
- eSUN: 20+ PETG colors via US distributors; odd colors may need 2–3 week China ship
- MatterHackers PRO: 12+ PETG colors in US stock, replenishment 5–10 days

---

## 6. Material Recommendation for Snap-Arm Clip

**Primary recommendation: PETG (eSUN or MatterHackers PRO)**

Rationale:
1. Best snap-fit fatigue life — 10–15% elongation at break prevents catastrophic fracture
2. Highest print reliability (9.0/10) on open-frame FDM farm
3. Dimensional accuracy ±0.10–0.20 mm is achievable within the 1.25–1.55 mm target window without scaling corrections
4. No enclosure required — compatible with Bambu A1/P1S farm
5. $0.09–$0.11 per clip at eSUN pricing is cost-competitive
6. MatterHackers PRO provides US-warehoused supply chain with lowest tariff disruption risk

**Secondary option: PLA+ (eSUN or Creality)**

Use only if: (a) thermal environment of the final product is <50°C, (b) the snap arm is a single-use or low-cycle-count application, or (c) cost must be minimized below $0.09/clip. PLA+ is cheaper and slightly easier to print, but fracture risk under repeated flexing is materially higher.

**Disqualified: ABS+**

The 0.8–1.6% shrinkage defeats the 1.25–1.55 mm tolerance window on open-frame printers. Only reconsider if: an enclosed thermal-stable farm is operational AND snap arms need heat resistance above 70°C (PETG's deflection limit).

---

## 7. First-Article Print Protocol

Before committing to a production material, run this qualification sequence:

1. Print 5 clips in each candidate material (PETG, PLA+) at standard settings
2. Measure wall section at 3 points per clip with digital calipers; record mean and std deviation
3. Target: mean within 1.25–1.55 mm, std dev <0.10 mm
4. Perform 50-cycle flex test on 2 clips per material (full deployment + return)
5. Inspect for micro-cracks at root radius under 10x loupe
6. Pass criteria: zero fractures, dimensional mean within spec, std dev <0.10 mm
7. If PETG passes, lock in eSUN PETG as Phase 2 production material

---

## Sources

- [PLA vs ABS vs PETG: Wevolver](https://www.wevolver.com/article/comparison-of-pla-abs-and-petg-filaments-for-3d-printing)
- [PETG vs PLA vs ABS Strength Comparison — Ultimaker](https://ultimaker.com/learn/petg-vs-pla-vs-abs-3d-printing-strength-comparison/)
- [Snap-Fit Design Guide — Hubs/Protolabs Network](https://www.hubs.com/knowledge-base/how-design-snap-fit-joints-3d-printing/)
- [Snap-Fit Design Tips — Mandarin3D](https://mandarin3d.com/blog/how-to-design-parts-that-snap-fit-together/)
- [FDM Tolerances — Snapmaker](https://www.snapmaker.com/blog/3d-printing-tolerances/)
- [Filament Prices 2026 — LayerMath](https://layermath.com/filament-prices)
- [Best Filaments for Bambu/Creality/Prusa — Makers101](https://makers101.com/best-filaments-for-bambu-creality-prusa/)
- [Complete Filament Brand Comparison 2026 — 3DPut](https://3dput.com/complete-filament-brand-comparison-2026-tolerance-quality-value-ratings/)
- [ResearchGate: Mechanical Properties of PLA, PETG, ABS on High-Speed Printer](https://www.researchgate.net/publication/391466129_Mechanical_Properties_of_PLA_PETG_and_ABS_Samples_Printed_on_a_High-Speed_3D_Printer)
- [SigmaFilament 2026 Buyer's Guide](https://sigmafilament.com/pla-vs-petg-vs-abs-filament-guide/)
