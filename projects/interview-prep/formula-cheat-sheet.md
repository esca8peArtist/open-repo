# Formula Cheat Sheet — SpaceX Build Reliability Engineer (Starship)

> Print this. Know every formula cold before your interview.

---

## GD&T Formulas

### True Position (Positional Deviation)

```
Positional deviation = 2 × √[(x_actual − x_nominal)² + (y_actual − y_nominal)²]
```

The × 2 converts radial distance to diameter (position tolerance is always a diameter).

**Must be ≤** stated position tolerance + any bonus tolerance.

**Example:** Hole measured at (10.15, 20.08). Nominal at (10.00, 20.00).
Δx = 0.15, Δy = 0.08
Deviation = 2 × √(0.15² + 0.08²) = 2 × √(0.0225 + 0.0064) = 2 × 0.170 = **0.340 mm**

---

### Bonus Tolerance (MMC)

```
Effective tolerance = Stated tolerance + (Actual size − MMC size)    [for a hole]
Effective tolerance = Stated tolerance + (MMC size − Actual size)    [for a pin]
```

**Example:** Hole: MMC = ∅20.00 mm, position tolerance = ∅0.50 at MMC.
Actual hole = ∅20.30 mm → Bonus = 0.30 → Effective tolerance = ∅0.80 mm

---

### Virtual Condition

```
External feature (pin) at MMC:  VC = MMC_size + position_tolerance
Internal feature (hole) at MMC: VC = MMC_size − position_tolerance
```

---

## Process Capability Formulas

```
Cp  = (USL − LSL) / 6σ                          [spread only, ignores mean]

Cpk = min[(USL − μ) / 3σ,  (μ − LSL) / 3σ]     [actual capability, centering included]

Pp  = (USL − LSL) / 6s_overall                  [long-term spread]

Ppk = min[(USL − μ) / 3s,  (μ − LSL) / 3s]     [long-term actual capability]
```

Where:
- σ = short-term (within-subgroup) standard deviation
- s = overall (long-term) standard deviation
- μ = process mean
- USL = Upper Specification Limit, LSL = Lower Specification Limit

**Targets:**

| Cpk | Process Status |
|---|---|
| < 1.00 | Incapable — immediate action |
| 1.00 – 1.33 | Marginal — monitor closely |
| ≥ 1.33 | Capable (4σ process) |
| ≥ 1.67 | Highly capable (5σ) — required for flight-critical features |

**Sigma level from Cpk:** σ_level ≈ 3 × Cpk (approximate)

**Process centering ratio (k):**
```
k = |μ − midpoint| / [(USL − LSL)/2]     [0 = perfectly centered, 1 = at spec limit]

Cpk = Cp × (1 − k)
```

---

## Weibull Reliability Formulas

### Two-Parameter Weibull

```
PDF:       f(t) = (β/η)(t/η)^(β−1) × e^(−(t/η)^β)

CDF:       F(t) = 1 − e^(−(t/η)^β)         [probability of failure by time t]

Reliability: R(t) = e^(−(t/η)^β)            [probability of survival to time t]
```

Where:
- **β** = shape parameter (slope on Weibull paper)
- **η** = scale parameter = characteristic life (time at which F = 63.2%)

### Characteristic Life Interpretation

```
At t = η:   F(η) = 1 − e^(−1) = 1 − 0.368 = 0.632 = 63.2%
```

η is NOT the same as MTBF unless β = 1.

### Shape Parameter (β) Interpretation

| β Value | Failure Type | Physical Meaning |
|---|---|---|
| β < 1 | Infant mortality | Mfg defects, latent flaws — burn-in helps |
| β = 1 | Random | Exponential dist.; MTBF applies; constant failure rate |
| β ≈ 2 | Early wear-out | Fatigue, gradual wear |
| β > 3 | Steep wear-out | Failures cluster tightly around η |

### B-Life (Percentile Life)

```
B_X life = η × [−ln(1 − X/100)]^(1/β)
```

**B10 life** (10% of population failed): `B10 = η × [−ln(0.90)]^(1/β)`

**B50 life** (median): `B50 = η × [ln(2)]^(1/β) = η × 0.693^(1/β)`

### Median Rank (for plotting Weibull paper)

```
F_i ≈ (i − 0.3) / (n + 0.4)
```

Where i = failure rank (1, 2, 3...) and n = total sample size.

### Weibull Linearization (for plotting)

Take double natural log of the reliability equation:
```
ln(ln(1/R(t))) = β × ln(t) − β × ln(η)
```

Plot Y = ln(ln(1/R)) vs X = ln(t). Slope = β. Y-intercept = −β × ln(η).

---

## Exponential Reliability (Constant Failure Rate — β = 1)

```
MTBF = 1/λ            [λ = failure rate]

R(t) = e^(−λt)        [reliability at time t]

F(t) = 1 − e^(−λt)   [probability of failure by time t]

R(t) = e^(−t/MTBF)
```

**Series system (all must work):**
```
R_system = R₁ × R₂ × R₃ × ...

λ_system = λ₁ + λ₂ + λ₃ + ...

MTBF_system = 1/λ_system
```

**Parallel system (any one sufficient):**
```
R_system = 1 − (1−R₁)(1−R₂)...

F_system = F₁ × F₂ × ... (independent failures)
```

---

## Fault Tree Analysis Probabilities

```
AND gate:  P(output) = P(A) × P(B)     [assumes independence]

OR gate:   P(output) = 1 − (1−P(A)) × (1−P(B))
                     ≈ P(A) + P(B)     [for small probabilities]
```

---

## FMEA Risk Priority Number

```
RPN = Severity (S) × Occurrence (O) × Detection (D)
```

Each rated 1–10. Max RPN = 1000.

**Warning:** Do not use RPN in isolation. A high Severity rating (≥ 8) is always a priority regardless of RPN.

---

## Welding Heat Input

```
H = (V × I × 60) / TS
```

Where:
- H = heat input (J/mm)
- V = arc voltage (volts)
- I = welding current (amps)
- TS = travel speed (mm/min)

**Lower H** = less distortion, smaller HAZ, less risk of sensitization in stainless

**Preheat and interpass temperature** for 304L stainless: max interpass = **150°C (300°F)**

---

## Tolerance Stack-Up

**Worst case (conservative — use for safety-critical):**
```
Total tolerance = t₁ + t₂ + t₃ + ... + tₙ
```

**RSS — Root Sum Square (statistical — use for production):**
```
Total tolerance = √(t₁² + t₂² + t₃² + ... + tₙ²)
```

RSS assumes tolerances are independent and normally distributed. Use with caution when distributions are unknown.

---

## Statistical Control Chart Limits

**X-bar and R Chart:**
```
UCL_Xbar = X̄ + A₂ × R̄
LCL_Xbar = X̄ − A₂ × R̄

UCL_R = D₄ × R̄
LCL_R = D₃ × R̄
```

*A₂, D₃, D₄ are constants from standard SPC tables (depend on subgroup size n)*

**Individuals (I-MR) Chart:**
```
UCL_I = X̄ + 2.66 × MR̄
LCL_I = X̄ − 2.66 × MR̄

UCL_MR = 3.267 × MR̄
LCL_MR = 0
```

**Standard deviation estimate from range:**
```
σ̂ = R̄ / d₂     [d₂ is from SPC constants table; for n=5: d₂ = 2.326]
```

---

## Defect / Quality Metrics

**First Pass Yield:**
```
FPY = (Units passing first inspection) / (Total units inspected) × 100%
```

**Rolled Throughput Yield (RTY) — multiple steps:**
```
RTY = FPY₁ × FPY₂ × FPY₃ × ...
```

**Defects Per Unit (DPU):**
```
DPU = Total defects / Total units inspected
```

**Defects Per Million Opportunities (DPMO):**
```
DPMO = (Total defects / (Units × Opportunities per unit)) × 1,000,000
```

**Sigma level from DPMO (approximate):**
```
3.4 DPMO   = 6σ
6,210 DPMO = 4σ
66,807 DPMO = 3σ
```

**Escape rate:**
```
Escape rate = Defects reaching next level / Total defects found
```

---

## Material Properties Quick Reference

| Material | Density (g/cm³) | UTS (MPa) | Yield (MPa) | Max service temp |
|---|---|---|---|---|
| 304L SS | 7.93 | 480–620 | 170–310 | ~870°C (short term ~1000°C) |
| 316L SS | 7.98 | 480–620 | 170–310 | ~870°C |
| Inconel 718 (aged) | 8.19 | 1240–1400 | 1030–1100 | ~650°C (creep limit) |
| Ti-6Al-4V | 4.43 | ~950 | ~880 | ~315°C (sustained load) |
| Al 7075-T6 | 2.81 | ~570 | ~500 | ~150°C |
| Al 6061-T6 | 2.70 | ~310 | ~276 | ~175°C |

**Cryogenic performance (LOX at -183°C):**
- 304L SS: Yield strength **increases** ~50% → ~465 MPa vs ~310 MPa at room temp
- Al alloys: Strength increases slightly but ductility decreases (concern for crack propagation)
- Carbon fiber: Epoxy matrix becomes brittle; microcracking risk

---

## LOX Cleanliness / Oxygen Service

Per ASTM G93 and CGA G-4.1:
- **Cleanliness level for LOX wetted surfaces:** Typically < 100 mg/m² nonvolatile residue
- **Particle contamination:** < 1000 ppm by mass for most LOX applications
- **UV light check:** Hydrocarbons fluoresce under UV — used for quick verification

---

## SQL Quick Reference

```sql
-- Window function for first inspection per part:
ROW_NUMBER() OVER (PARTITION BY part_id ORDER BY inspection_date ASC)

-- DATEDIFF:
DATEDIFF(day, date_opened, GETDATE())   -- SQL Server
DATEDIFF(date_opened, CURDATE())        -- MySQL  
julianday('now') - julianday(date_opened) -- SQLite

-- Safe division (avoid divide-by-zero):
DIVIDE(numerator, denominator, 0)       -- Power BI DAX
numerator / NULLIF(denominator, 0)      -- SQL

-- Conditional aggregation:
SUM(CASE WHEN condition THEN 1 ELSE 0 END)
COUNT(CASE WHEN condition THEN 1 END)
```

---

## Power BI DAX Quick Reference

```dax
-- First Pass Yield:
FPY % = DIVIDE(
    COUNTROWS(FILTER(Inspections, Inspections[first_result] = "pass")),
    COUNTROWS(Inspections),
    0
)

-- Defect Rate:
Defect Rate % = DIVIDE([Total Defects], [Total Inspections], 0) * 100

-- NCMR Age (days open):
Days Open = DATEDIFF(NCMR[date_opened], TODAY(), DAY)

-- Pareto cumulative %:
Cumulative % = DIVIDE(
    CALCULATE([Defect Count], FILTER(ALL(Defects), Defects[cumulative_rank] <= MAX(Defects[cumulative_rank]))),
    [Total Defects]
)

-- Rolling 30-day count:
Rolling 30d = CALCULATE([Defect Count], DATESINPERIOD(Date[Date], LASTDATE(Date[Date]), -30, DAY))
```

---

## Key Standards and Specifications Summary

| Standard | Domain | Key Requirement |
|---|---|---|
| ASME Y14.5-2018 | GD&T | Current US GD&T standard |
| AS9100 Rev D | Quality Management | Aerospace QMS; includes FAI, key characteristics |
| AS9102 | First Article Inspection | FAI procedure for first production part |
| AWS D17.1 | Aerospace Welding | Classes A/B/C; weld acceptance criteria |
| ASNT SNT-TC-1A | NDT Personnel | Qualification and certification for NDT inspectors |
| NAS 410 | Aerospace NDT | NDT certification requirements |
| ASTM G93 | LOX Cleanliness | Cleaning and handling for oxygen service |
| MIL-STD-882E | System Safety | Hazard analysis; risk matrix |
| MMPDS | Materials | Material properties database for aerospace structures |
| Nadcap | Special Processes | Third-party accreditation for welding, NDT, heat treat |
