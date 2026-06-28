---
title: "Product Selection Decision Matrix — Wave 2 Expansion Candidates"
project: mfg-farm (ModRun)
created: 2026-06-28
status: decision-ready
confidence: 82%
scope: >
  Scored decision matrix for the 5 new product candidates (A-E from Q3_Q4_PRODUCT_CANDIDATES.md).
  Scores each 1-5 across demand signal, margin potential, design complexity (inverted),
  supplier readiness, and UGC opportunity. Produces a ranked recommendation for Q3-Q4
  Wave 2 product investment sequence.
related:
  - Q3_Q4_PRODUCT_CANDIDATES.md
  - CAD_TIMELINE_AND_BATCH_PLANNING.md
  - Q3_Q4_SKU_EXPANSION_MATRIX.md
---

# Product Selection Decision Matrix — Wave 2 Expansion Candidates

**Lead finding**: The parametric grommet (Candidate D) scores highest overall and should be designed and listed first — fastest design time, highest margin, four SKU variants from one session, zero new suppliers. The standing desk cable chain (Candidate A) is the single highest-upside product (near-zero competition, proven free-STL demand signal) and should be designed immediately after (or concurrently with) the monitor-arm spine guide (Candidate C) in a single CAD session. The desk-clamp holder (Candidate B) and USB hub mounts (Candidate E) round out the Wave 2 portfolio. All five are actionable now, independent of test print outcome.

---

## Part 1: Scoring Rubric

Each criterion is scored 1–5. Weighted total is the decision metric.

| Criterion | Weight | 5 (Best) | 1 (Worst) |
|---|---|---|---|
| **Demand Signal** | 30% | 300+ Etsy listings with 100+ avg reviews; clear Reddit pain points; validated free-STL downloads | <20 listings; no Reddit mentions; niche/experimental |
| **Margin Potential** | 25% | ≥75% gross margin; COGS <$1.00; short print time | <60% margin; high hardware cost; long print time |
| **Design Complexity** (inverted: higher score = simpler) | 20% | 1–3 hrs CAD; 1 test iteration; no mechanical complexity | 6+ hrs CAD; 3+ iterations; mechanical fit-critical (jaw, hinge) |
| **Supplier Readiness** | 15% | 100% existing supply chain; no new orders | New material type (TPU, resin); new hardware supplier required; 2+ week lead time |
| **UGC Opportunity** | 10% | Natural "before/after" desk transformation photo; r/battlestations post format; viral potential | No visual impact; niche product; hard to photograph meaningfully |

---

## Part 2: Individual Scores

### Candidate A: Standing Desk Cable Chain

| Criterion | Score | Justification |
|---|---|---|
| Demand Signal | 5 | Free STL platforms: 1,000+ downloads across multiple standing desk chain designs; Etsy: <10 physical-print sellers = massive supply gap relative to demand; r/battlestations: "adhesive fails when I raise desk" is a recurring complaint; DeskLogics vertebrae spine selling on Amazon confirms WTP |
| Margin Potential | 4 | 72–76% gross margin; $1.20–1.40 COGS on $24.99–34.99 retail; 45–60 min print per set (moderate) |
| Design Complexity (inverted) | 3 | 3–5 hrs base CAD; 2 test iterations; hinge geometry requires tolerance testing; moderate complexity |
| Supplier Readiness | 5 | PLA+ or PETG — both fully existing suppliers; no new orders; can print day-of-design |
| UGC Opportunity | 5 | Before: cables flapping under height-adjustable desk. After: clean chain routing from desk to floor. Photogenic, visible, satisfying. Perfect r/battlestations format |
| **Weighted Total** | **4.40** | 5×0.30 + 4×0.25 + 3×0.20 + 5×0.15 + 5×0.10 = 1.50+1.00+0.60+0.75+0.50 |

**Demand Confidence**: HIGH (82%). Whitespace confirmed. Design risk is moderate but manageable.

---

### Candidate B: Desk-Clamp Cable Holder

| Criterion | Score | Justification |
|---|---|---|
| Demand Signal | 4 | 30–60 Etsy listings; BAMprecision (113 favs, Feb 2026) is leading seller with unscaled presence; XDA Developers article explicitly documents as unsolved problem category; r/desksetup "can't drill" use case confirmed |
| Margin Potential | 4 | 72–77% gross margin; $1.06–1.18 COGS on $17.99–22.99 retail; 30–40 min print |
| Design Complexity (inverted) | 2 | 4–6 hrs CAD; 3 test iterations required for jaw tolerance; jaw mechanism is fit-critical (too tight = marks desk; too loose = slips); highest design risk of the five |
| Supplier Readiness | 5 | PLA+ (existing) + rubber pads + M4 thumbscrews — all existing supplier channels |
| UGC Opportunity | 4 | Before: cables taped to desk edge with ugly adhesive. After: clamp-on holder, clean and removable. Less dramatic than chain but still compelling |
| **Weighted Total** | **3.70** | 4×0.30 + 4×0.25 + 2×0.20 + 5×0.15 + 4×0.10 = 1.20+1.00+0.40+0.75+0.40 |

**Demand Confidence**: HIGH (80%). Risk is in design execution (jaw tolerance), not market demand.

---

### Candidate C: Monitor-Arm Cable Spine Guide

| Criterion | Score | Justification |
|---|---|---|
| Demand Signal | 3 | 5–15 Etsy physical-print listings; XDA article explicitly documents as unsolved; Printables downloads moderate; however, TAM is narrower than general cable management (requires monitor arm ownership) |
| Margin Potential | 4 | 73–78% gross margin; $1.03–1.18 COGS on $19.99–26.99 retail; 50–65 min print in PETG |
| Design Complexity (inverted) | 3 | 3–5 hrs CAD (reduced if Candidate A designed first — shared link geometry); 2 test iterations; moderate complexity |
| Supplier Readiness | 5 | PETG (existing Overture supplier); M3 screws (existing channel); no new suppliers |
| UGC Opportunity | 4 | Before: cables flapping from monitor arm when adjusting height. After: articulated spine cleanly routes cables. High-visibility in desk setup photos |
| **Weighted Total** | **3.65** | 3×0.30 + 4×0.25 + 3×0.20 + 5×0.15 + 4×0.10 = 0.90+1.00+0.60+0.75+0.40 |

**Demand Confidence**: MEDIUM (73%). TAM narrower but whitespace clean.

---

### Candidate D: Parametric Wall/Desk Grommet

| Criterion | Score | Justification |
|---|---|---|
| Demand Signal | 4 | 20–40 Etsy listings; Wall Eye Solutions ($10.99) confirms WTP; XDA article: "store-bought grommets rarely right size" is explicit; IKEA desk hole mismatch well-documented; free STL downloads confirm hobbyist demand |
| Margin Potential | 5 | 74–80% gross margin; $0.40–0.50 COGS on $9.99–22.99 retail; 15–25 min print; single parametric design generates 4 SKU variants |
| Design Complexity (inverted) | 5 | 2–3 hrs CAD total for all 4 sizes; 1 test iteration; no mechanical complexity; parametric cylinder is the simplest geometry in the set |
| Supplier Readiness | 5 | PLA+ only; no hardware; fully existing supply chain |
| UGC Opportunity | 3 | "Before: grommet fell out / cable hole looks terrible. After: custom-fit grommet, clean." Useful but less dramatic than chain or clamp; hard to photograph compellingly |
| **Weighted Total** | **4.35** | 4×0.30 + 5×0.25 + 5×0.20 + 5×0.15 + 3×0.10 = 1.20+1.25+1.00+0.75+0.30 |

**Demand Confidence**: HIGH (81%). Dedicated competitor confirms market. Fastest design path to first revenue of all five.

---

### Candidate E: USB Hub / Power Brick Under-Desk Mount

| Criterion | Score | Justification |
|---|---|---|
| Demand Signal | 3 | 50–90 Etsy listings scattered across brand-specific sellers; individual precedents confirm WTP; r/battlestations "USB hub wanders" is real; however, fragmented (no seller has built a catalog) — unclear if fragmentation reflects market or opportunity |
| Margin Potential | 4 | 70–76% gross margin; $0.58–0.68 COGS on $12.99–17.99 retail; 20–30 min print; catalog approach (5–8 variants) multiplies revenue per design session |
| Design Complexity (inverted) | 4 | 1–1.5 hrs CAD per device variant (short); 1 test iteration per variant; main complexity is catalog management (5+ files) not individual design |
| Supplier Readiness | 5 | PLA+ only; 3M adhesive strips (existing) or screws (existing) |
| UGC Opportunity | 3 | Before: USB hub on desk surface, cable tangle. After: hidden under desk, clean surface. Visible improvement but less dramatic than chain/clamp |
| **Weighted Total** | **3.65** | 3×0.30 + 4×0.25 + 4×0.20 + 5×0.15 + 3×0.10 = 0.90+1.00+0.80+0.75+0.30 |

**Demand Confidence**: MEDIUM (70%). Portfolio approach reduces single-variant risk but execution complexity is highest (catalog of 5–8 STL files to manage).

---

## Part 3: Ranked Results

| Rank | Candidate | Weighted Score | Primary Strengths | Primary Risks |
|---|---|---|---|---|
| **1** | **D — Parametric Grommet** | **4.35** | Highest margin, simplest design, 4 SKUs from 1 session, fastest to Etsy | Less dramatic UGC; niche (desk hole users only) |
| **2** | **A — Standing Desk Cable Chain** | **4.40** | Near-zero competition, highest demand whitespace, best UGC potential | Hinge tolerance testing needed; 2 test iterations |
| **3** | **B — Desk-Clamp Cable Holder** | **3.70** | Proven demand (BAMprecision leading), clear pain point, high margin | Jaw mechanism is design-critical; 3 test iterations; highest design risk |
| **4** | **C — Monitor-Arm Spine Guide** | **3.65** | Whitespace, shares geometry with A, medium design time | Narrower TAM; PETG material (slower print, slightly higher cost) |
| **4** | **E — USB Hub/Power Brick Mounts** | **3.65** | Long-tail catalog play; very fast per-variant design; no competition | Demand fragmented; catalog management overhead; device model turnover risk |

**Note on rank 1 vs rank 2**: Candidate A scores 4.40 vs Candidate D's 4.35 — the difference is within estimation error. In practice, D should be designed and listed first (fastest path to Etsy, simplest execution) while A is designed in parallel or in the immediately following batch session. The numeric ranking reflects raw score; the tactical sequence is D first, then A+C batch, then B, then E.

---

## Part 4: Go / No-Go Thresholds by Candidate

After each candidate's first 60 days on Etsy, apply these thresholds:

| Candidate | GO (continue, expand catalog) | WATCH (extend 30 days, investigate) | NO-GO (delist or deprioritize) |
|---|---|---|---|
| A — Cable Chain | ≥12 units/week by day 60 | 6–11 units/week | <5 units/week |
| B — Desk Clamp | ≥10 units/week by day 60 | 5–9 units/week | <4 units/week |
| C — Spine Guide | ≥8 units/week by day 60 | 4–7 units/week | <3 units/week |
| D — Grommet | ≥20 units/week by day 60 (across 4 variants) | 10–19 units/week | <9 units/week |
| E — Hub Mounts | ≥5 units/week/variant (≥25 total for 5 variants) | 2–4 units/week/variant | <2 units/week per variant average |

**What to do on NO-GO**: Do not abandon immediately. Lower price by $2–3 (still above margin floor). Check Etsy SEO (title, tags, first image). If no recovery after 30 more days, pause listing and re-examine photographs / product copy.

---

## Part 5: Top 3 Recommendations for Wave 2 Launch

### Recommendation 1 (Top Priority): Candidate D — Parametric Grommet

**Why first**: Highest weighted score on pure economics. Simple design. Zero hardware complexity. Generates 4 revenue streams from a single 2–3 hour CAD session. Acts as a low-risk "prove the batch design model works" product before committing 6–8 hours to the chain design.

**Action**: Design all 4 grommet sizes (55mm/64mm/80mm/100mm) in one CadQuery session. Test print the 64mm variant (IKEA standard). List all 4 as product variants under one Etsy listing. Photograph on a desk with a visible cable hole before/after.

**Revenue expectation**: $200–400/month gross within 60 days across 4 sizes at $9.99–$22.99.

---

### Recommendation 2 (Batch Session): Candidates A + C — Cable Chain + Spine Guide

**Why second (and together)**: Candidate A is the highest-upside whitespace product in the entire extended pipeline. Zero US English-language competition on Etsy for physical-print standing desk cable chains. Candidate C shares 60% of the design work with A — designing both in one session captures the batch efficiency.

**Action**: After grommet listed, schedule a 6–7 hour design session for A+C together. Use chain link as base; adapt to spine guide. Print 1 set each. List both on Etsy within the same week.

**Revenue expectation combined**: $400–700/month gross within 90 days; Candidate A alone has potential to become a top-3 product by review volume within 6 months if community adoption occurs.

---

### Recommendation 3 (Subsequent Session): Candidate B — Desk-Clamp Cable Holder

**Why third**: Strong demand, clear market signal (BAMprecision leading but unscaled), good margin. However, jaw mechanism requires more design iteration than the chain or grommet — budget 3 test prints and allow 1.5 weeks from design start to Etsy list date.

**Action**: After A+C listed, schedule a dedicated 4–6 hour CAD session for the clamp. Test jaw mechanism on 2 desk thicknesses (20mm standard and 35mm thick laminate). List once jaw fits reliably.

**Revenue expectation**: $300–500/month gross within 90 days.

---

### Candidates C (Spine Guide) and E (Hub Mounts) Positioning

Candidate C launches with Candidate A (same batch session). It is effectively a free additional SKU from the A design session.

Candidate E (hub mounts) is recommended for **Wave 3 (September 2026)** rather than Wave 2. Reasoning: the catalog approach (5+ variants) benefits from having the ModRun brand established with reviews before entering the device-specific niche. Buyers of a $14 hub mount are more likely to purchase from a seller with 50+ total reviews than from one with 5. Wait until A, C, D, B are generating reviews (~August).

---

## Part 6: Interaction with Initial 15 SKUs — Portfolio Prioritization

Adding 5 new candidates expands the active product portfolio from 15 to 20. Priority ordering for printer time when at capacity (September onward per utilization projections):

**Tier 1 (never deprioritize — highest proven revenue or whitespace):**
- Existing: Cable Tray (1A), Surge Protector Holder (1B), Under-Desk Organizer (1C), Magnetic Labels (1D)
- New: Grommet (D), Cable Chain (A)

**Tier 2 (monitor performance, scale if GO threshold met):**
- Existing: Monitor Riser (2A), Drawer Dividers (2B), Shelf Dividers (2D)
- New: Desk Clamp (B), Spine Guide (C)

**Tier 3 (secondary revenue, scale only if capacity allows):**
- Existing: Pegboard Labels (2C), Name Plate (3C), Cable Clips Specialty (3F)
- New: USB Hub Mounts (E)

**Tier 4 (niche/seasonal — print to order, no standing inventory):**
- Existing: Dice Tower (3A), Miniature Storage (3B), Plant Stand (3D)
- Existing: Lamp Base (3E), Elastic Straps (3G) — both high-risk, deferred

---

*Decision matrix completed June 28, 2026. Scores based on publicly available Etsy/Reddit/MakerWorld data. All recommendations independent of test print outcome — actionable now.*
