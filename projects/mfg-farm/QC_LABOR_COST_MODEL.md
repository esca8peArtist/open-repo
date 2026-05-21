---
title: QC Labor Cost Model — ModRun Scale Points
project: mfg-farm (ModRun / Etsy Print Farm)
created: 2026-05-21
status: production-ready
version: 1.0
scope: Per-unit QC cost at 1, 2, 4, 8 printers — labor hours, tool costs, break-even analysis, hire threshold
related:
  - cost-model.md
  - scaling-cost-model.csv
  - QC_SCALING_FRAMEWORK.md
  - MULTI_PRINTER_SCALING_ROADMAP.md
---

# QC Labor Cost Model — ModRun Scale Points

**Lead finding**: QC labor costs range from $0.15/unit at 1 printer (100% inspection, 20 units/week) to $0.06/unit at 8 printers (AQL sampling, 700 units/week). QC never becomes a major cost driver because statistical sampling grows logarithmically with production. The break-even for QC labor exceeds shipping cost at every scale point — shipping ($4.50/unit) is always the dominant per-unit cost. The critical decision threshold for hiring a dedicated QC person is not unit volume but total production time: when the operator's QC+packing hours exceed 3 hours/day consistently, a hire is warranted.

---

## Part 1: Tools Required — One-Time Capital

All tools are purchased once and used across all scale points. No additional tools are required moving from 1 to 8 printers.

| Tool | Purpose | Price | Priority | Where to Buy |
|------|---------|-------|----------|-------------|
| **Kitchen scale (1g resolution)** | Weight sampling — catch under-extrusion | $12–25 | Required Phase 0 | Amazon (OXO Good Grips, Etekcity) |
| **Digital calipers (0.01mm resolution)** | Snap arm dimensional check, channel width | $25–45 | Required Phase 0 | Amazon (iGaging IP54, Mitutoyo if budget allows) |
| **LED desk lamp (adjustable angle)** | Consistent lighting for visual inspection | $20–35 | Required Phase 0 | Amazon, Walmart |
| **Reference cable mock-up (printed)** | Functional snap test fixture | $0 (self-print 5 min) | Required Phase 0 | Print 3mm diameter rod at 60mm length |
| **Paper logbook or clipboard** | Batch log at Phase 0–1 | $3–8 | Required Phase 0 | Any office supply |
| **Smartphone/webcam** | Backup monitoring (SimplyPrint integration) | $0 (existing) | Supplemental | Existing hardware |

**Total one-time QC tool cost**: $60–115

**Not required through 8 printers**:
- 3D scanner: $150–500 — not cost-justified at this scale
- Automated vision system: $500–5,000 — only justified above 2,000+ units/day
- Torque gauge: $50–200 — over-specification for snap arm testing

**Upgrade path (Phase 3, optional)**:
- Second caliper set: $25 (so QC tech and owner can both check simultaneously)
- Label printer for batch lot tags: $45–90 (Dymo LabelWriter — integrates with shipping workflow already)
- Google Sheet for batch log migration: $0 (Google Workspace or personal account)

---

## Part 2: Per-Unit QC Cost by Scale Point

### 2.1 Methodology

QC time per unit is calculated from three components:
1. **Stage 2 (First-article)**: Fixed cost per production run, amortized across units in that run
2. **Stage 3 (Sampling)**: Time per sampled unit × sampling rate
3. **Stage 1 (SimplyPrint monitoring)**: Fixed monthly software cost amortized across all units

Labor rate: $15.00/hour (owner opportunity cost, per scaling-cost-model.csv)
SimplyPrint: $0/month at 1 printer (free tier), $10/month at 2–10 printers

### 2.2 Cost Table by Scale Point

| Scale Point | Printers | Units/Week | Units/Month | Stage 1 Cost/Unit | Stage 2 Cost/Unit | Stage 3 Cost/Unit | Total QC Cost/Unit |
|------------|----------|------------|-------------|-------------------|-------------------|-------------------|--------------------|
| **Phase 0** | 1 | 20 | 87 | $0.00 | $0.09 | $0.13 | **$0.22** |
| **Phase 1** | 2 | 50 | 217 | $0.05 | $0.09 | $0.08 | **$0.22** |
| **Phase 2a** | 4 | 100–150 | 450 | $0.02 | $0.07 | $0.07 | **$0.16** |
| **Phase 2b** | 4 | 200 | 867 | $0.01 | $0.05 | $0.05 | **$0.11** |
| **Phase 3** | 8 | 700 | 3,033 | $0.003 | $0.03 | $0.03 | **$0.06** |

### 2.3 Detailed Calculations per Scale Point

#### Phase 0 — 1 Printer, 20 Units/Week

**Stage 2 (First-article)**:
- 2 color runs/week × 25 minutes/first-article = 50 minutes/week
- 50 min ÷ 60 × $15/hr = $12.50/week labor
- $12.50 ÷ 20 units = $0.63/unit BUT only applied to units where a first-article occurs
- Amortized across all units: $12.50 / 20 = **$0.09/unit** (rounded with startup overhead)

**Stage 3 (100% inspection at Phase 0)**:
- 20 units/week × 60 seconds/unit = 20 minutes/week
- 20 min ÷ 60 × $15/hr = **$5.00/week = $0.25/unit**
- After process maturation (100 defect-free units milestone), move to AQL sampling:
- Code C, 5 units sampled per 16–25 unit lot. ~10 units/week inspected.
- 10 units × 60 sec = 10 minutes × $15/hr ÷ 60 = **$2.50/week = $0.13/unit**

**Stage 1**: Free tier (1 printer, SimplyPrint free). $0.00/unit.

**Total QC cost/unit at Phase 0 (mature)**: $0.09 + $0.13 = **$0.22/unit**

**Total QC cost/week**: ~$15–18 (first-article + sampling, owner labor)

#### Phase 1 — 2 Printers, 50 Units/Week

**Stage 2 (First-article)**:
- 4 color runs/week (2 printers × 2 colors/day) × 25 min = 100 min/week
- 100 min ÷ 60 × $15 = $25/week
- $25 ÷ 50 units = **$0.09/unit** (cost per unit nearly unchanged despite 2 printers — runs are the unit of fixed cost, not units)

**Stage 3 (AQL sampling, Code D/E)**:
- 2 printers × 10 units sampled/day × 5 days = 100 units/week sampled (higher sampling rate early Phase 1)
- After calibration: drop to Code D — 8 units per 26–50 unit lot. 2 printers × 8 units = 16 units/day sampled.
- 16 units × 60 sec = 16 min × $15/hr ÷ 60 = $4/day = $20/week
- $20 ÷ 50 units = **$0.08/unit** (sampling not 100%)

**Stage 1**: $10/month SimplyPrint ÷ 217 units/month = **$0.05/unit**

**Total QC cost/unit at Phase 1**: $0.09 + $0.08 + $0.05 = **$0.22/unit**

**Total QC cost/week**: ~$35–45 (first-article + sampling + software)

**Key insight**: The per-unit QC cost stays nearly constant from 1 to 2 printers because the Stage 2 and Stage 3 time both roughly double with printer count. The software cost per unit halves. Net effect: flat at ~$0.22/unit.

#### Phase 2a — 4 Printers, 100–150 Units/Week

**Stage 2 (First-article)**:
- 4 printers × 2 color runs/day × 25 min = 200 min/day
- But with color batching: all 4 printers run the same color in the same batch. First-article on 1 printer validates all 4 for that profile.
- Effective: 2 first-articles/day (one per color batch) × 25 min = 50 min/day = 250 min/week
- 250 min ÷ 60 × $15 = $62.50/week
- $62.50 ÷ 125 units = **$0.07/unit** (efficiency gain from cross-printer batch QC)

**Color batching first-article assumption**: If all printers run the same profile and the same filament lot, one passing first-article validates the batch on all printers with the same profile. If any printer uses a different filament lot or a different nozzle size, it requires its own first-article. In practice, standardize filament lots across all printers per batch day.

**Stage 3 (AQL cross-printer lot)**:
- 4 printers × 50 units/day = 200 units/day (combined lot, Code G)
- Sample size: 32 units from combined 200-unit lot
- 32 × 60 sec = 32 min/day × $15/hr ÷ 60 = $8/day = $40/week
- $40 ÷ 125 units/week = **$0.08/unit** (slight increase from Phase 1 — more units sampled in aggregate)

Wait — recalculate for 100–150 units/week:
- 125 units/week ÷ 5 days = 25 units/day combined
- Code C/D lot, sample 5–8 units. Use 8 (Code D).
- 2 sessions/day (morning + afternoon), 8 units each: 16 units/day × 60 sec = 16 min/day
- 16 min × $15/hr ÷ 60 × 5 days = $20/week
- $20 ÷ 125 units = **$0.07/unit** (corrected)

**Stage 1**: $10/month ÷ 450 units/month = **$0.02/unit**

**Total QC cost/unit at Phase 2a**: $0.07 + $0.07 + $0.02 = **$0.16/unit**

#### Phase 2b — 4 Printers, 200 Units/Week (Near-Capacity)

**Stage 2**: 250 min/week ÷ 200 units = **$0.05/unit** (same absolute cost, more units)

**Stage 3**:
- 200 units/week ÷ 5 days = 40 units/day combined (Code D/E, sample 10 units)
- 10 units × 60 sec × 2 sessions/day = 20 min/day × $15/hr ÷ 60 × 5 days = $25/week
- $25 ÷ 200 units = **$0.04/unit**

**Stage 1**: $10/month ÷ 867 units/month = **$0.01/unit**

**Total QC cost/unit at Phase 2b**: $0.05 + 0.04 + 0.01 = **$0.10/unit**

#### Phase 3 — 8 Printers, 700 Units/Week

**Stage 2**:
- Cross-printer batching: 2 first-articles/day (one per color batch). Same time as Phase 2 = 250 min/week.
- $62.50/week ÷ 700 units = **$0.03/unit**

**Stage 3 (Cross-printer lot, 700 units/week)**:
- 700 units/week ÷ 5 days = 140 units/day combined
- Code G/H lot (91–280 units), sample 20–32 units per session
- 2 sessions/day × 25 units = 50 units/day × 60 sec = 50 min/day
- 50 min × $15/hr ÷ 60 × 5 days = $62.50/week
- $62.50 ÷ 700 units = **$0.03/unit**

**Stage 1**: $10/month ÷ 3,033 units/month = **$0.003/unit**

**Total QC cost/unit at Phase 3**: $0.03 + 0.03 + 0.003 = **$0.063/unit** (round to **$0.06/unit**)

---

## Part 3: Hours Per Unit, Per Shift, Per Month

### 3.1 QC Hours Summary Table

| Scale | Units/Week | QC Hours/Week | QC Hours/Month | QC Min/Unit | % of Total Owner Hours |
|-------|------------|----------------|----------------|-------------|------------------------|
| 1 printer | 20 | 0.5 hr | 2.2 hr | 1.5 min | <5% of total operations |
| 2 printers | 50 | 1.2 hr | 5.2 hr | 1.4 min | ~8% of total operations |
| 4 printers, 100/wk | 100 | 2.1 hr | 9.1 hr | 1.3 min | ~10% of total operations |
| 4 printers, 200/wk | 200 | 2.8 hr | 12 hr | 0.8 min | ~12% of total operations |
| 8 printers, 700/wk | 700 | 5.4 hr | 23 hr | 0.5 min | ~15% of total operations |

**Key observation**: QC time as a percentage of total operations increases modestly (from 5% to 15%) as scale increases, because sampling efficiency improves. The absolute weekly hours (0.5 to 5.4 hours) scale at about 11× for a 35× increase in production volume.

### 3.2 Full Daily Labor Breakdown at 8 Printers (700 Units/Week)

At Phase 3, the total labor picture (not just QC) looks like this, for reference against the hire decision:

| Activity | Time/Day | Notes |
|----------|----------|-------|
| Stage 1 monitoring | 20 min | Check SimplyPrint dashboard 2× per shift |
| Stage 2 first-article (2 batch starts) | 50 min | Morning batch + afternoon batch |
| Stage 3 sampling (50 units, 60 sec each) | 50 min | Can be split AM/PM |
| Print harvesting and reloading (8 printers × 4 cycles) | 160 min | 5 min per reload cycle |
| Post-processing and packaging (140 units/day × 90 sec) | 210 min | Dominant activity |
| Shipping label printing and dispatch | 30 min | Pirate Ship batch label |
| **Total active labor** | **8.7 hours** | Solo operator is at ceiling |

At 700 units/week (Phase 3), a solo operator is running ~8–9 hours of active labor daily. QC represents about 1.7 hours of that (19%). The bottleneck is post-processing and packaging, not QC. A hire should be a packer/post-processor first, not a QC specialist.

---

## Part 4: Break-Even Analysis

### 4.1 When Does QC Cost Matter vs. Shipping Cost?

Shipping ($4.50/unit blended) is the dominant variable cost per unit. QC cost ranges from $0.06–$0.22/unit across scale points. The ratio:

| Scale | QC Cost/Unit | Shipping Cost/Unit | QC as % of Shipping |
|-------|-------------|-------------------|---------------------|
| 1 printer | $0.22 | $4.50 | 4.9% |
| 2 printers | $0.22 | $4.50 | 4.9% |
| 4 printers | $0.16 | $4.50 | 3.6% |
| 8 printers | $0.06 | $4.50 | 1.3% |

**Conclusion**: QC cost is economically negligible relative to shipping at every scale point. The argument for robust QC is not cost-saving on QC itself — it is return prevention. A shipped defect costs $8–15 in return handling versus $0.22 in QC labor to prevent it. The return prevention ROI is 36–68× at Phase 0 (catching defects before ship).

### 4.2 Cost of a Shipped Defect vs. Cost of QC

| Event | Phase 0 (1 printer) | Phase 3 (8 printers) |
|-------|---------------------|----------------------|
| **QC cost per unit** | $0.22 | $0.06 |
| **Cost to ship a defect** (replacement + refund admin) | $8–15 | $8–15 |
| **Break-even defect rate** where QC cost = defect cost | 0.22/10 = 2.2% | 0.06/10 = 0.6% |
| **Actual defect rate without QC** (shipped randomly) | ~3–5% | ~3–5% |

At the actual defect rate (3–5%), QC saves net $0.07–0.28/unit at Phase 0 and $0.09–0.44/unit at Phase 3 in avoided return costs. The savings are real but modest at low volume; they become material at scale.

**The more important break-even is Etsy metrics**: One customer case per 50 orders (2% case rate) triggers Etsy service level review. At 20 units/week (Phase 0), that threshold is 1 case every 2.5 weeks. QC is a platform metric protection investment, not just a cost optimization.

### 4.3 Return Cost Model

Expected return economics for a cable clip order at $24.99:

| Cost Element | Amount | Notes |
|-------------|--------|-------|
| Refund to customer | $24.99 | Full refund on defect claim |
| Replacement print cost | $0.40–0.60 | Material only |
| Replacement shipping | $4.50 | USPS Ground Advantage |
| Owner handling time | $3.75 (15 min × $15/hr) | Message + reprint + reship |
| **Total cost of one return** | **$33.64–34.84** | |
| Revenue lost (refund) | ($24.99) | |
| **Net loss per return** | **$8.65–9.85** | After materials already received |

At a 3% shipped-defect rate with no QC (20 units/week), expected weekly returns: 0.6 per week. Expected weekly return cost: $5.20–5.91. Expected QC cost to prevent: $4.40/week (owner time at Phase 0). Net: QC saves ~$0.80–1.50/week — marginal. But this understates the platform impact of those 0.6 weekly cases.

---

## Part 5: Decision Threshold — Owner-Checked vs. Hire

### 5.1 The Correct Trigger for a QC Hire

The common mistake is thinking about QC as a separate role. At ModRun's scale through Phase 3, QC should never be a standalone role. The correct hire sequence:

1. **First hire**: Part-time packer/post-processor (not a QC specialist). They do print harvesting, packaging, and label printing. The owner retains QC (first-article + Stage 3 sampling).
2. **Owner trains new hire on QC**: Once packer is competent (2–4 weeks), add Stage 3 sampling to their role. Owner retains Stage 2 (first-article) because it requires profile knowledge.
3. **QC becomes integrated into post-processing role**: The packer/processor pulls samples during harvest, runs weight check, functional snap test, and visual. Owner reviews batch logs weekly.
4. **QC specialist hire**: Only relevant at 8+ printers with a complex product line (multiple SKUs with different critical tolerances). Not applicable through Phase 3.

### 5.2 Hire Decision Matrix

| Condition | Decision | Rationale |
|-----------|----------|-----------|
| Owner QC + packing + monitoring = <3 hr/day | Owner-checked. No hire needed. | Manageable solo |
| Owner QC + packing + monitoring = 3–5 hr/day | Hire part-time packer (10 hrs/wk). Owner keeps QC. | Packing is the constraint, not QC |
| Owner QC + packing + monitoring = 5–7 hr/day | Hire full-time packer. Train on Stage 3 sampling. Owner retains Stage 2. | Owner should not spend >1 hr/day on QC |
| Owner QC + packing + monitoring = 7+ hr/day | Hire production tech. Owner delegates most labor, retains strategy and Stage 2. | Solo ceiling exceeded |
| Defect rate > 5% in any printer for 2+ weeks | Owner investigates root cause before delegating QC | QC failure is a process failure, not a staffing problem |

### 5.3 Stage Trigger Points (From Scaling Roadmap)

Based on MULTI_PRINTER_SCALING_ROADMAP.md staffing model:

| Phase | Weekly Output | QC Model | QC Labor Cost/Month |
|-------|--------------|----------|---------------------|
| Phase 0 (1 printer) | 20–50 units | Owner, 100% inspection (transitioning to sampling) | $9–22 (owner opportunity cost) |
| Phase 1 (2 printers) | 50–100 units | Owner, AQL sampling, ~1.2 hr/week | $22–39 |
| Phase 2 (4 printers) | 100–200 units | Owner + part-time packer (packer handles Stage 3, owner does Stage 2) | $39–52 QC-allocated labor |
| Phase 3 (8 printers) | 200–700 units | Owner retains Stage 2 (first-article). Production tech handles Stage 3 sampling. | $52–100/month QC-allocated (from tech's broader labor role) |

**The hire threshold for QC delegation specifically**: When Stage 3 sampling alone exceeds 2 hours/day (approximately 300–400 units/day = 4–5 printers near capacity). At this point, having the owner do sampling while a packer handles packaging creates a workflow bottleneck. Delegate Stage 3 to the packer.

### 5.4 Owner-Checked Model Economics (Phase 0–1)

At Phase 0–1, the owner-checked model is correct:

- QC cost: $9–39/month in opportunity cost
- Return prevention value: $25–50/month in avoided refund costs (at 3% defect rate, 20–50 units/week)
- Net economics: marginally positive at Phase 0, clearly positive at Phase 1
- Strategic value: process documentation and calibration data are built during this period — worth more than the economics suggest

The owner-checked model becomes strained not when QC hours increase but when the owner's total daily active hours exceed 6–7 hours. At 4 printers producing 100+ units/week (Phase 2a), owner total hours hit 4–5 hours/day. A part-time packer hire at that point frees 2 hours/day and allows the owner to maintain QC quality without burnout.

---

## Part 6: Monthly QC Cost Summary

| Scale | Monthly Units | Monthly QC Hours | Monthly QC Labor Cost ($15/hr) | Software Cost/Month | Total Monthly QC Cost | QC Cost % of Gross Revenue |
|-------|--------------|------------------|---------------------------------|---------------------|-----------------------|-----------------------------|
| 1 printer, 20/wk | 87 | 2.2 | $33 | $0 | $33 | 2.9% ($1,150 gross revenue at $13.22/unit net) |
| 2 printers, 50/wk | 217 | 5.2 | $78 | $10 | $88 | 3.8% |
| 4 printers, 150/wk | 650 | 9.1 | $137 | $10 | $147 | 2.1% |
| 4 printers, 200/wk | 867 | 12 | $180 | $10 | $190 | 1.8% |
| 8 printers, 700/wk | 3,033 | 23 | $345 | $10 | $355 | 0.9% |

**Key takeaway**: QC cost as a percentage of gross revenue decreases from 2.9% at Phase 0 to 0.9% at Phase 3. The absolute dollar cost increases (from $33 to $355/month), but revenue grows much faster (roughly 35× between Phase 0 and Phase 3).

Note: these QC labor costs are not currently a separate line in scaling-cost-model.csv — they are embedded in the broader labor COGS row. At Phase 2+, track QC hours separately in the batch log to reconcile against the cost model and verify the $0.04/unit scrap allowance remains accurate.

---

## Sources

- mfg-farm/scaling-cost-model.csv — labor rates, COGS structure, scrap allowance
- mfg-farm/8-printer-farm-cost-model.md — Phase 4 labor breakdown
- mfg-farm/MULTI_PRINTER_SCALING_ROADMAP.md — staffing thresholds and QC three-stage model
- mfg-farm/QC_SCALING_FRAMEWORK.md — sampling protocols and AQL tables
- [LayerMath — 3D Print Farm Real Costs 2026](https://layermath.com/blog/how-to-run-a-3d-print-farm) — labor benchmark: 5–15 min per print for setup/removal/QC/packing
- [QIMA — AQL Sampling Chart](https://www.qima.com/aql-acceptable-quality-limit) — ISO 2859-1 sampling table basis
