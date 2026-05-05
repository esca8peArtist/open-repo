# ModRun Production Workflow v1.0

**Status**: Production-ready operational blueprint  
**Date Created**: 2026-05-05  
**Purpose**: Post-test-print operational execution guide for Month 1 launch and scaling

---

## Executive Summary

Once the test print confirms FDM_TOLERANCE calibration and design printability, ModRun manufacturing becomes repeatable. This document defines:

1. **Per-unit production timeline** — STL approval to ship-ready: 36 calendar hours, 28 active labor minutes
2. **Batch queueing strategy** — 5-unit batches, overlap post-processing with printing
3. **Quality gates & failure recovery** — tolerance criteria, reprints, customer warranties
4. **Volume scaling roadmap** — 1→5→20→100+ units/week operational changes
5. **Month 1-6 production targets** — realistic demand and capacity planning

**Key Finding**: Printer capacity (1,260+ clips/week) far exceeds demand. Binding constraint is labor-intensive post-processing and fulfillment, not printing.

---

## Part 1: Post-Test-Print Workflow

### 1.1 Test Print Outcomes (May 6-15 Window)

**What the test print answers:**
- Snap arm functional? (click-fit without rattle)
- Tolerance achievable? (0.05mm swing)
- Support removal clean? (no feature damage)
- Finish acceptable? (layer lines, smoothness)

**Approval gates:**
- **PASS**: All 4 criteria → proceed immediately
- **NEAR-PASS**: 3/4 criteria → fix tolerance, reprint (1 week)
- **FAIL**: <3/4 criteria → iterate design (2-3 week)

**Assumption for this workflow**: Test print PASSES.

### 1.2 STL Approval & Slicing

**Software**: Bambu Studio (native to Bambu P1S)

**Production parameters** (locked post-test-print):
- Layer height: 0.20mm
- Infill: 22%
- Walls: 3
- Nozzle temp: 223°C (PLA+ 215-230°C range)
- Bed temp: 60°C
- Print speed: 200 mm/s

**Print time estimates**:
- Clip: 2.5 hours
- Rail: 1.8 hours
- Bundle: 4.3 hours

### 1.3 Print Execution

**Batch setup**:
- Queue: 5 units/batch (2 clips, 2 rails, 1 combo)
- Print duration: 22-24 hours (4.3 hrs × 5 + 10% overhead)
- Cool-down: 3-4 hours

**Monitoring**: Bambu Cloud native dashboard + notifications at 50%, 90%, 100%

**Failure modes**:
- Nozzle jam (1-2%): Auto-detect → manual clean → resume (15 min)
- Poor adhesion (0.5%): Restart batch (30 min + reprint)
- Filament runout (1-2%): Auto-pause → load spool → resume (10 min)

### 1.4 Post-Processing

**Timeline per 5-unit batch** (2.5 hours labor):
- Cool-down (unattended): 2-4 hours
- Support removal: 45 min (9 min/unit)
- Cleaning: 30 min (6 min/unit, hot water + brush)
- QC inspection: 20 min (4 min/unit)

**Quality gate**: All parts pass snap test (smooth clicks, no grinding)

**Rejection rate**: ~2% (typical FDM tolerance variance)

### 1.5 Packaging & Fulfillment

**Per order**:
- Product: 1 clip + 1 rail
- Box: Kraft 6×4×2" (USPS priority compatible)
- Padding: $0.08-0.12/unit
- Assembly: 2 min/order
- Shipping: USPS Priority $7.50-9.50/unit

**Turnaround**: Order → shipped within 24 hours

---

## Part 2: Batch Queueing

### 2.1 Single-Printer Strategy (Month 1-3, ~20 units/week)

**Weekly schedule**:

| Day | Activity | Notes |
|-----|----------|-------|
| Mon | Batch 1 printing starts (8am) | 24 hrs |
| Tue | B1 post-proc + B2 printing | Parallel workflow |
| Wed | B2 post-proc + B3 printing | Parallel workflow |
| Thu | B3 post-proc + B4 printing | Parallel workflow |
| Fri | B4 post-proc + packaging | Weekly wrap-up |

**Output**: 20 units/week (4 batches × 5 units, minus 2% rejects = 19.2 net)

**Labor**: ~12.5 hours/week (flexible, can compress to 3 days)

**Utilization**: 71% printer uptime (sustainable)

### 2.2 Two-Printer Strategy (Month 4-6, ~50 units/week)

**Trigger**: When single printer runs 80%+ utilization 2 consecutive weeks AND unfulfilled orders exist

**Changes**:
- Stagger printer starts (offset by 4 hours)
- Parallel printing maintains continuous post-processing
- Add AutoFarm3D Door Opener ($129 + $10-40/month) for overnight unattended operation

**Output**: 40-50 units/week

**Labor**: 20-22 hours/week (still single-operator)

---

## Part 3: Quality & Failure Recovery

### 3.1 Acceptance Criteria

**Dimensional**:
- Snap arm: 1.35-1.45mm (±0.05mm from 1.40mm)
- Clip gap: 7.5-8.5mm
- Rail bore: 6.0-6.2mm

**Functional**:
- Snap test: 5 insertion/extraction cycles, no cracking
- Load test: Support 500g without deformation
- Retention: Cord stays seated at 45° for 10 seconds

**Finish**:
- Surface: Layer lines visible, <0.2mm peak-to-valley
- Color: Uniform
- Support scars: <1mm diameter, non-visible underside
- Defects: Zero cracks, warping, blobs

**Rejection triggers**:
- Snap arm <1.30mm or >1.50mm
- Functional test fails
- Surface defect >2mm visible
- Warping detectable

### 3.2 Reprint Protocol

**Tracking**: Reject bin + spreadsheet log (date, unit ID, defect type)

**Reprint decisions**:
- Single reject: Reprint 1, add next batch
- Batch rate >3%: Investigate cause
- Consistent pattern: Adjust tolerance, test before resuming

**Warranty**: 30-day satisfaction guarantee (free replacement). Assume <1% return rate.

---

## Part 4: Monthly Targets (Months 1-6)

### 4.1 Demand Forecast

**Binding constraint**: Demand (not printer capacity)

| Month | Units/week | Notes |
|-------|-----------|-------|
| 1 | 20 | Existing email list + organic |
| 2 | 25 | First Etsy reviews |
| 3 | 35 | Review velocity accelerating |
| 4 | 50 | Add 2nd printer |
| 5 | 60 | Proven model |
| 6 | 80-100 | Summer seasonal ramp |

### 4.2 Per-Unit Timeline

**Calendar time**: Monday start → Wednesday ship = 36 hours

**Active labor**: ~28 minutes (spread across 2 days)

**Batch of 5**:
- Calendar: 36 hours
- Labor: 2.5 hours
- Cost: $37.50 (at $15/hr)
- Per-unit labor cost: $7.50

### 4.3 Month 1 Economics (Example)

| Item | Value |
|------|-------|
| **Production** | |
| Batches | 4/week |
| Units/week | 20 |
| Labor | 10 hrs/week |
| Printer utilization | 71% |
| **Monthly (80 units)** | |
| Filament (12g/unit) | $6.40 |
| Packaging | $24 |
| Electricity | $3.20 |
| Rejects (2%) | $1.76 |
| Labor | $150 |
| **Total COGS** | **$185** |
| **Revenue ($24.99/unit)** | **$1,999** |
| **Gross margin** | **90.7%** |

---

## Part 5: Automation Decisions

### 5.1 AutoFarm3D Door Opener (Month 2-3)

**Cost**: $129 + $10-40/month

**Benefit**: Unattended overnight printing (saves 2 hrs/week)

**ROI**: 4.3 weeks payback at $15/hr

**Buy when**: Volume ≥25 units/week

### 5.2 Bulk Filament (Month 3-4)

**Savings**: $0.17/unit (bulk $0.126 vs. retail $0.30)

**At 50 units/week**: $34/month savings

**Switch when**: Volume hits 40+ units/week

### 5.3 Post-Processing Automation (Month 5+)

**Options**:
- Manual + optimization: Sustainable to 100+ units/week
- Wet-blasting: $500-2k, reduces labor 30%
- Robot: $15k+, overkill for <150 units/week

**Recommendation**: Manual through Month 6; revisit at 150-200 units/week demand

---

## Part 6: Implementation Checklist

**Phase A: Setup (Day 1)**
- [ ] Lock Bambu Studio params from test print
- [ ] Save 5-unit batch template
- [ ] Verify print time estimates

**Phase B: First Production (Week 1)**
- [ ] Run 1 batch (5 units)
- [ ] Document actual timings
- [ ] Photograph for Etsy

**Phase C: Operations (Week 2-4)**
- [ ] 4 batches/week (20 units)
- [ ] Daily fulfillment routine
- [ ] Maintain 5-10 unit buffer
- [ ] Monitor Etsy reviews

**Phase D: Optimization (Week 5-8)**
- [ ] Evaluate AutoFarm3D ROI
- [ ] Order bulk filament (4-6 week lead)
- [ ] Plan 2-printer trigger

**Phase E: Scaling (Week 9+)**
- [ ] Implement 2-printer strategy at 50+ units/week
- [ ] Hire part-time post-processor
- [ ] Plan facility if ≥75 units/week

---

## Part 7: Risk Mitigation

**Printer failure**: 2-week filament buffer + spare nozzles. Service contract optional.

**Supply chain**: Retail filament backup for emergency. Stagger bulk orders.

**Demand miss**: Single printer handles 5-100 units/week with no capex.

**Demand surge**: Pre-queue batches; add 2nd printer at first sustained backlog.

---

**Version**: 1.0  
**Date**: 2026-05-05  
**Status**: Production-ready  
**Next Review**: Post-test-print (May 15-20)
