---
title: "CAD Timeline and Batch Planning — Wave 2 Products (Q3-Q4 2026)"
project: mfg-farm (ModRun)
created: 2026-06-28
status: planning-ready
confidence: 85%
scope: >
  Sequencing strategy for designing the 5 new candidates (A-E from Q3_Q4_PRODUCT_CANDIDATES.md)
  alongside the existing 15 SKUs (Q3_Q4_SKU_EXPANSION_MATRIX.md). Identifies which products
  share CAD components, which can design in parallel, time estimates, and resource dependencies.
  Actionable independent of test print result.
related:
  - Q3_Q4_PRODUCT_CANDIDATES.md
  - Q3_Q4_SKU_EXPANSION_MATRIX.md
  - PHASE_2_PRODUCT_SEQUENCING_PLAN.md
---

# CAD Timeline and Batch Planning — Wave 2 Products (Q3-Q4 2026)

**Lead finding**: Three of the five new candidates (A, C, D) share a common core CAD geometry and should be designed in a single parallel batch during one CAD session. The parametric link from the cable chain (Candidate A) adapts directly to the monitor-arm spine (Candidate C) with 1–2 hours additional work. The grommet (Candidate D) is a fast standalone design (2–3 hours, parametric). Two candidates (B, E) should be sequenced after the chain/spine batch because they introduce a new mechanical element (jaw clamp) and a device-specific catalog approach respectively.

---

## Part 1: Shared Part Analysis

### Component Library Across New Candidates + Existing SKUs

| Component | Candidate A (Chain) | Candidate B (Desk Clamp) | Candidate C (Spine Guide) | Candidate D (Grommet) | Candidate E (Hub Mount) | Existing SKU (Surge Protector) | Existing SKU (Under-Desk Organizer) |
|---|---|---|---|---|---|---|---|
| Parametric link / hinge geometry | **Core** | Adapter | **Derived** (narrower, arm-attachment boss) | — | — | — | — |
| Desk-edge jaw mechanism | — | **Core** | — | — | — | — | — |
| Under-desk mounting plate (screw pattern) | — | — | — | — | **Shared** | **Shared** | **Shared** |
| Parametric diameter cylinder | — | — | — | **Core** | — | — | — |
| Cable routing channel (longitudinal slot) | Used | Used | Used | Star-slot variant | Used | Used | Used |
| Rubber pad pocket | — | Jaw face | — | — | — | Used | — |

**Key insight**: The cable routing channel slot is the single most reused geometry across all cable management products. Designing it once as a parametric feature block (depth, width, entry angle) and importing it into each product file saves 30–45 minutes per product on average.

### Batch Group 1 (Design Together — Highest Component Overlap)
- **Candidate A: Standing Desk Cable Chain**
- **Candidate C: Monitor-Arm Cable Spine Guide**
- **Rationale**: Chain link (Candidate A) and spine link (Candidate C) are the same base geometry. A → C adaptation requires only: (1) narrowing link width from ~25mm to ~15mm, (2) adding M3 screw boss for arm attachment, (3) adjusting snap-channel angle for cable capture. Estimated time savings vs. designing separately: 1.5–2.5 hours.

### Batch Group 2 (Design Together — Mounting Plate Shared)
- **Candidate E: USB Hub/Power Brick Mount**
- **Existing SKU 1B: Surge Protector Holder** (if not already designed)
- **Existing SKU 1C: Under-Desk Cable Organizer** (if not already designed)
- **Rationale**: All three use identical rear mounting plate (screw pattern 80mm OC, countersunk M4). Design plate once, export as STEP file, import into all three product bodies. Time savings: 20–30 min per product.

### Standalone (No Batch Efficiency)
- **Candidate B: Desk-Clamp Cable Holder** — jaw mechanism is unique to this product; no other product uses it. Design standalone.
- **Candidate D: Parametric Grommet** — parametric cylinder is the core; fastest design in the set. Standalone but quick.

---

## Part 2: Time Estimates Per Product

### Basis Assumptions

- CAD tooling: CadQuery (Python parametric) — consistent with existing ModRun design approach
- Includes: parametric design, parameter validation (size check), export STL + 3MF
- Does not include: slicing, test print iteration time, listing photography
- Skill level: intermediate CadQuery user who designed the ModRun clip (existing competency)

| Candidate | CAD Design (hrs) | Batch Efficiency Savings | Effective Design Time | Test Print Iterations | Total from Design Start to Etsy-Ready |
|---|---|---|---|---|---|
| A: Standing Desk Cable Chain | 3–5 | –1.5 (if B1 batch) | 2–3.5 hrs | 2 iterations × 60 min = 2 hrs | 5–7 hrs |
| B: Desk-Clamp Cable Holder | 4–6 | 0 (standalone) | 4–6 hrs | 3 iterations × 45 min = 2.25 hrs | 7–9 hrs |
| C: Monitor-Arm Spine Guide | 3–5 | –1.5 (if B1 batch) | 2–3.5 hrs | 2 iterations × 70 min = 2.3 hrs | 5–7 hrs |
| D: Parametric Grommet | 2–3 | 0 (standalone, fast) | 2–3 hrs | 1 iteration × 20 min = 20 min | 3–4 hrs |
| E: USB Hub/Power Brick Mount (per variant) | 1–1.5/variant | –0.3 (shared plate) | 0.7–1.2/variant | 1 iteration × 25 min per variant | 1.5–2.5 hrs/variant |

**Total for all 5 candidates (with batch efficiency applied)**:
- Batch Group 1 (A + C together): 5–7 hrs CAD + 4.3 hrs test print = **9–11 hrs total**
- Candidate D standalone: 2–3 hrs CAD + 0.3 hrs test print = **2.5–3.5 hrs total**
- Candidate B standalone: 4–6 hrs CAD + 2.25 hrs test print = **6–8 hrs total**
- Candidate E (5 device variants): 5–7.5 hrs CAD + 2 hrs test prints = **7–9.5 hrs total**
- **Grand total: 25–32 hours of design+test-print work** for all 5 new candidates

Compared to designing all 5 sequentially without batch thinking: approximately 32–44 hours. Batch + shared parts saves **7–12 hours** (~25%).

---

## Part 3: Sequencing Strategy

### Decision Framework

Priority-sorting criteria (in order):
1. **Revenue speed**: Products closer to market-ready (simpler design, proven market) go first
2. **Batch efficiency**: Pair products that share geometry in the same design session
3. **Supply chain readiness**: No new suppliers needed = can launch sooner
4. **Risk tolerance**: Higher-risk designs (multiple test print iterations needed) go later when cash flow validates continued investment

### Recommended Sequence

**Week 1 (Design Session 1 — Batch Group 1: A + C together)**

Start here because:
- Candidate A (chain) fills the most underserved whitespace (no US English physical-print Etsy competitor)
- Candidate C (monitor spine) shares 60% of the chain geometry — designing C after A is essentially "extending" an already-in-progress design session, not starting fresh
- Both use existing PLA+ or PETG supply chain — no new supplier contacts needed
- Total design+test-print: 9–11 hours across 1 design session + 2–3 print sessions

Deliverables from this session:
- chain_link_v1.step (base parametric link, width and height configurable)
- chain_link_v1.stl (chain set: 8 links, 2 sizes)
- spine_guide_v1.stl (6-link spine guide for standard VESA monitor arm)
- Test prints: 1 set each
- Etsy listing content: drafted, needs photos after test print

**Week 2 (Design Session 2 — Candidate D: Parametric Grommet)**

Standalone but fastest of all candidates. Reasoning:
- 2–3 hours CAD → shortest time-to-Etsy of all new candidates
- Generates 4 SKU variants from one design session (55mm/64mm/80mm/100mm)
- No test print risk (geometry is simple, tolerances are loose — "parametric fit")
- Highest gross margin (74–80%)
- Revenue from grommet starts funding later test prints

Deliverables:
- grommet_v1_{55,64,80,100}mm.stl (4 variants)
- Single test print of 64mm variant (most common IKEA desk hole size)
- Etsy listing: 1 base listing with variants dropdown

**Week 3 (Design Session 3 — Candidate B: Desk-Clamp Cable Holder)**

More complex (jaw mechanism) but critical for ecosystem completeness:
- Shares design language with ModRun cable clip (existing product) — positioning as ecosystem extension
- Jaw mechanism requires careful tolerance test (too tight = cracks desk edge; too loose = slips)
- 3 test print iterations budgeted — allow Week 3 for design + print; list in Week 4

Deliverables:
- clamp_v1.stl (jaw: 15–30mm desk thickness variant)
- clamp_v2.stl (jaw: 30–55mm desk thickness variant)
- Test prints: 3 iterations of jaw mechanism
- Etsy listing: ready Week 4 with test photos

**Week 4 (Design Session 4 — Candidate E: USB Hub/Power Brick Mounts, initial 3 variants)**

Device catalog approach — start with 3 highest-demand devices:
1. Anker PowerExpand 341 USB-C Hub (7-in-1) — most reviewed USB-C hub on Amazon
2. UGREEN Revodok Pro 209 (7-in-1) — second most reviewed, similar form factor
3. Generic "universal slot mount" (adjustable width 55–100mm, no device-specific) — broadest appeal

Reasoning: Starting with Anker (highest Amazon review count) ensures first variant targets the largest installed base. Universal variant catches buyers whose hub isn't specifically listed.

Deliverables:
- hub_mount_anker_7in1.stl
- hub_mount_ugreen_209.stl
- hub_mount_universal_v1.stl (adjustable slot)
- Test prints: 1 each
- Etsy listings: 3 product listings

**Week 5–6 (Expand Candidate E catalog + launch photography)**

- Add 2–3 additional hub mount variants (CalDigit Element Hub, HP USB-G5, Sabrent USB-C Hub)
- Lifestyle photography for all 5 new candidates
- Submit Amazon Handmade application photos (these products photograph well for "handcrafted workspace" context)

---

## Part 4: Interaction with Existing 15-SKU Launch Sequence

The existing Q3_Q4_SKU_EXPANSION_MATRIX.md sequences:
- Wave 1 (July 1): Cable Tray, Surge Protector Holder, Under-Desk Organizer, Magnetic Labels
- Wave 2 (Aug 15): Monitor Riser, Drawer Dividers, Pegboard Labels, Shelf Dividers
- Wave 3 (Sept 1): Cable Clips (Specialty), Name Plate, Miniature Storage, Dice Tower (if resin printer)
- Wave 4 (Oct 1): Plant Stand, Elastic Straps (deferred), Lamp Base (deferred)

**Integration of new candidates into this schedule:**

| New Candidate | Recommended Launch Date | Rationale |
|---|---|---|
| D — Parametric Grommet | **July 15** (after Wave 1) | Fastest design; fits in Week 2 slot while Wave 1 products ramp; generates early revenue |
| A — Standing Desk Cable Chain | **August 1** (with Wave 2 ramp) | Week 1 design complete by mid-July; test print done; complements August standing desk traffic spike (back-to-school/office season) |
| C — Monitor-Arm Spine Guide | **August 1** (same session as A) | Designed together with A; no additional delay |
| B — Desk-Clamp Cable Holder | **August 15** (same day as Wave 2) | Week 3 design; jaw iteration done by August; pairs well with Wave 2 cable management expansion |
| E — USB Hub Mounts (3 variants) | **September 1** (Wave 3 period) | Week 4 design; first 3 variants ready; aligns with Wave 3 specialty expansion window |

This schedule adds 5 new SKUs across 2 months without displacing any existing Wave 1–3 products. Printer utilization impact: new products add ~14–18 additional print hours per month in August (within single-printer capacity; see utilization table in Q3_Q4_SKU_EXPANSION_MATRIX.md — September is the pressure point at 96% utilization).

**Critical path**: If printer utilization hits 96% in September, launch of Candidate E (hub mounts, September 1) should be monitored against Wave 3 products. Defer lowest-performing Wave 3 product if needed to maintain capacity for the higher-margin hub mount catalog.

---

## Part 5: Resource Dependencies

| Dependency | Products Affected | Resolution |
|---|---|---|
| PETG filament stock | A, C | Order with Wave 1 July 1 supply order (1 extra spool = $15–17, stock buffer) |
| M3 screws (arm attachment for spine guide) | C | Amazon Prime, same order as other hardware |
| M4 thumbscrews (desk clamp jaw mechanism) | B | Amazon Prime, lead time 2–3 days |
| Rubber jaw pads (EPDM adhesive strips) | B | Same channel as surge protector adhesive strips |
| Device dimension reference (hub mount variants) | E | Published manufacturer specs + community measurements on Printables comments |
| Test print time (3 iterations for Candidate B jaw) | B | Allow 5 print hours in Week 3 schedule; do not rush jaw tolerance — one bad tolerance = poor reviews |

---

## Part 6: CAD Reuse Library — Recommended File Structure

To capture batch-design efficiency across all 20 products (15 existing + 5 new), maintain a shared component library:

```
cad/
├── components/
│   ├── cable_channel_slot.step        # Reused in A, C, 1A, 1C, 3F
│   ├── mounting_plate_80mm.step       # Reused in E, 1B, 1C
│   ├── rubber_pad_pocket.step         # Reused in B, 1C, 2A
│   ├── parametric_link_base.step      # A → adapt to C
│   └── etsy_text_field_template.step  # Text extrusion for name plates (3C), pegboard labels (2C)
├── products/
│   ├── chain_link_v1.step
│   ├── spine_guide_v1.step
│   ├── grommet_55mm.step
│   ├── grommet_64mm.step
│   ├── grommet_80mm.step
│   ├── grommet_100mm.step
│   ├── clamp_jaw_15_30mm.step
│   ├── clamp_jaw_30_55mm.step
│   └── hub_mount_[model].step         # One file per device variant
└── exports/
    └── [all STL + 3MF exports]
```

Maintaining `components/` prevents redesigning shared geometry for each product. Every future SKU beyond these 20 begins with importing relevant components.

---

*CAD timeline and batch planning completed June 28, 2026. All time estimates assume single designer with intermediate CadQuery competency. Timeline is actionable immediately — no test print result dependency.*
