---
title: "Phase 3 Medicinal Herbs — Critical Path Analysis & Production Timeline"
date: 2026-05-21
version: 8.0
status: production-ready
phase: Phase 3 pre-execution
decision-deadline: May 30, 2026
execution-window: June 22 – July 13, 2026 (22 calendar days)
gate-status:
  forager-cohort: CLEARED (21.3%, gate >20%)
  native-plants-conversion: CLEARED (2.24%, gate >1.5%)
word-count: ~3200
companion-csv: phase-3-medicinal-herbs-gantt.csv
supersedes: v7.0 (2026-05-21, PHASE_3_MEDICINAL_HERBS_CRITICAL_PATH.md)
cross-references:
  - phase-3-medicinal-herbs-sourcing-guide.md
  - phase-3-medicinal-herbs-content-outline.md
  - medicinal-herbs-candidate-list.md
  - phase-3-medicinal-herbs-gantt.csv
tags: [seedwarden, phase-3, critical-path, production-timeline, medicinal-herbs, decision-support]
---

# Phase 3 Medicinal Herbs — Critical Path Analysis & Production Timeline

**Version**: 8.0
**Prepared**: May 21, 2026
**Decision deadline**: May 30, 2026 (three decisions required; all are user gates)
**Execution window**: June 22 – July 13, 2026 (22 calendar days, 108 total hours across all tracks)
**Launch gates**: BOTH CLEARED — forager cohort 21.3% (gate >20%), native plants conversion 2.24% (gate >1.5%)
**Companion spreadsheet**: `phase-3-medicinal-herbs-gantt.csv` (22-day sprint Gantt with start dates, durations, float days, critical-path flags, and parallel-track visibility)

---

## Executive Summary

Phase 3 medicinal herbs production is authorized to execute. Both demand-validation gates cleared before Phase 2 Track B launches May 30. The June 22–July 13 sprint is feasible for a single writer producing five bundles at 4–5 focused hours per day (Option A) or three priority bundles at 3–4 hours per day (Option C — recommended).

**The binding constraint is writing.** At 56–66 adjusted hours for all five bundles, the critical path runs exclusively through writing: Women's Health complete June 28 → upload June 29 → Respiratory upload July 6–7 → Sleep upload July 13. Design (14 hours total) and photography (18 hours pre-sprint, 10 in-sprint) carry 3–14 days of float on every task and do not threaten any upload date.

**Three user decisions are required by May 30**, flagged [USER GATE] throughout:
1. Sprint scope: Option A (all 5 bundles), Option B (split across two writers), or Option C (3-bundle priority — recommended)
2. Goldenseal sourcing path: live order by June 8, or Wikimedia CC path (recommended under Option C)
3. Canva palette: confirm six production hex codes by June 15 or auto-lock applies

**June 22 go/no-go decision criteria** (all conditions must hold on June 20 gate check):
- Forager cohort conversion remains ≥20% (current: 21.3%)
- Native plants conversion remains ≥1.5% (current: 2.24%)
- Attribution log complete in WORKLOG.md
- Canva Brand Kit Phase 3 palette loaded
- Sprint scope decision logged (May 30 gate)

If both metrics drop below threshold on June 20, the sprint defers to a July 1 re-check. Pre-sprint photography, design, and supplier activities continue regardless.

---

## Critical Path Map — Zero-Float Sequence

```
[May 30]  [USER GATE 1] Sprint scope decision logged — Option A / B / C
[May 30]  [USER GATE 2] Goldenseal path decision logged — Path 1 or Path 2
[May 30]  [USER GATE 3] Palette decision or defer to June 15 auto-lock
     |
[June 8]  HARD DEADLINE: Goldenseal order confirmed OR CC path logged in WORKLOG.md
[June 8]  AHG peer reviewer outreach initiated — must start today, not June 22
     |
[June 15] HARD DEADLINE: Elderberry order placed (Prairie Moon or local nursery)
[June 15] Mountain Rose Herbs dried herbs ordered (13 species, 1 oz each)
[June 15] PALETTE LOCK: hex codes confirmed or auto-locked
     |
[June 20] GO/NO-GO CHECK: forager cohort ≥20% + native plants ≥1.5% confirmed
[June 21] ZERO FLOAT: attribution log complete in WORKLOG.md
[June 21] ZERO FLOAT: Canva Brand Kit Phase 3 palette loaded
     |
[June 22] SPRINT DAY 1: Women's Health writing begins (Black Cohosh, ~700 words)
     |
[June 24] PACE GATE: WH must reach 2,500 words by EOD — if not, activate Option C
     |
[June 28] Women's Health writing complete (3,800 words) + PDF export QA
     |
[June 29] UPLOAD: Women's Health ($22) — MILESTONE 1 — REVENUE BEGINS
     |
[July 2]  Immunity writing complete through Goldenseal CITES sidebar
     |
[July 3]  DESIGN LOCK: all 5 Canva covers finalized — no changes after EOD
     |
[July 5]  Sleep writing complete (3,500 words)
     |
[July 6]  UPLOAD: Respiratory ($20) — MILESTONE 2
     |
[July 12] Float Day 1 (8 hours — absorbs Week 3 overrun)
     |
[July 13] UPLOAD: Sleep ($20) — MILESTONE 3 / SPRINT CLOSE
     |
[July 15] Practitioner tier live ($120–150, 3-bundle minimum met)
[July 20] UPLOAD: Immunity ($22) — post-sprint Milestone 4
[Aug  3]  UPLOAD: Digestive ($20) — full 5-bundle launch complete
```

---

## Section 1: Medicinal Herb Selection Finalization (~800 words)

### Five-Bundle Roster — Production-Locked

All five bundles are finalized. Species selection was locked in `phase-3-medicinal-herbs-etsy-listings.md` (May 7, 2026) and confirmed in `medicinal-herbs-candidate-list.md`. No further species selection decisions are required.

| Bundle | Species (21 slots, 14 unique) | SKU | Price | Upload Target |
|---|---|---|---|---|
| Women's Health | Black Cohosh, Vitex, Red Clover, Calendula, Lavender | MH-BUNDLE-WH-001 | $22 | June 29 |
| Respiratory Health | Elderberry, Mullein, Echinacea purpurea, E. angustifolia, Thyme | MH-BUNDLE-RH-001 | $20 | July 6–7 |
| Sleep and Nervines | Valerian, Passionflower, Lemon Balm, Lavender | MH-BUNDLE-SN-001 | $20 | July 13 |
| Immunity Support | Echinacea, Ashwagandha, Elderberry, Goldenseal | MH-BUNDLE-IM-001 | $22 | July 20 |
| Digestive Support | Dandelion, Calendula, Lemon Balm, Ginger | MH-BUNDLE-DS-001 | $20 | August 3 |

Seven species appear in two bundles (Echinacea, Elderberry, Lavender, Calendula, Lemon Balm — plus Echinacea and Elderberry's dual roles). Second-occurrence writing requires ~40% of first-occurrence effort, reducing raw hours from 64–74 to 56–66 adjusted hours.

### Sourcing Timeline Per Supplier

**Tier 1 — Hard Deadline June 8 (5–6 week lead, zero float for physical specimens)**

These two species carry the longest lead times and conservation significance. An order after June 8 arrives after the July 13 sprint close.

| Species | Bundle | Supplier | Lead Time | Cost | Conservation Note |
|---|---|---|---|---|---|
| Goldenseal (*Hydrastis canadensis*) | Immunity | Prairie Moon Nursery — rhizome division; prairiemoon.com | 5–6 weeks | $15–22 | CITES Appendix II. Cultivated only. FGV sourcing documentation required in guide body. |
| Black Cohosh (*Actaea racemosa*) | Women's Health | Strictly Medicinal Seeds — 2-year seedling; strictlymedicinalseeds.com | 5–6 weeks (May 25 optimal = June 21–28 arrival) | $10–15 | UpS At-Risk. 95%+ commercially wild-harvested. 150-word conservation sidebar mandatory. |

[USER GATE 2 — Goldenseal] Declare path by May 30, order by June 8 if Path 1:
- **Path 1 (live specimen)**: Order Prairie Moon or Strictly Medicinal by June 8. Arrives July 13–20. Writing and design unaffected. Recommended under Option A or B only.
- **Path 2 (Wikimedia CC — recommended under Option C)**: Confirm CC path by June 7. Email media@ncbg.unc.edu (NC Botanical Garden) and media@mobot.org (Missouri Botanical Garden). Zero cost, zero schedule risk. Immunity launches July 20 under Option C — CC is full launch quality.

**June 8 hard sign-off**: Log path decision in WORKLOG.md. Path 1: supplier name, order confirmation, expected arrival. Path 2: three Goldenseal CC-BY-SA filenames logged in PHOTO_ATTRIBUTION_LOG.md.

**Tier 2 — Deadline June 15 (3–4 week lead, 5–7 day float)**

| Species | Bundle(s) | Supplier | Lead Time | Cost | Fallback | Expected Arrival |
|---|---|---|---|---|---|---|
| Elderberry (*Sambucus nigra*) | Respiratory, Immunity | Prairie Moon Nursery bare-root; info@prairiemoon.com | 4 weeks | $15–25 | Local nursery potted 2-gal (order June 22 if Prairie Moon OOS) | ~July 13–20 |
| Dried herbs — 13 species, 1 oz each | All 5 bundles | Mountain Rose Herbs; wholesale@mountainroseherbs.com | 3–5 business days | $93–141 | Frontier Co-op — 3–5 day ship | June 17–18 if ordered June 15 |

Mountain Rose Herbs is the single highest-impact supplier action for photography quality. The dried herb studio session (June 17–21) produces all five bundle flat-lay images for Etsy listing slots. Request a Certificate of Analysis for Goldenseal root confirming cultivated origin.

**Tier 3 — Deadline June 22 (2–3 week lead, order sprint start day)**

Wide availability with verified photo fallbacks. No launch risk under any scope option.

Species: Echinacea purpurea (Prairie Moon or Strictly Medicinal), Echinacea angustifolia (Strictly Medicinal), Ashwagandha (Strictly Medicinal), Passionflower (Prairie Moon), Valerian (Prairie Moon or Strictly Medicinal), Ginger (Strictly Medicinal or grocery rhizome), Vitex (local landscape nursery).

**Photo-only — no specimen order needed**: Red Clover, Mullein, Thyme, Lemon Balm, Lavender, Calendula, Dandelion. All have exceptional Wikimedia Commons CC-BY-SA coverage. Dandelion images already in wild-edibles archive at `assets/wild-edibles/`.

### Order Deadline Summary

| Deadline | Action | Float if Missed |
|---|---|---|
| May 25 (optimal) | Black Cohosh order — Strictly Medicinal Seeds | Arrives July 13–20; CC fallback ready regardless |
| June 8 (hard) | Goldenseal order (Path 1) OR CC path confirmed | Zero — writing unaffected either way |
| June 15 (hard) | Elderberry order + Mountain Rose Herbs dried herbs | 5 days (Frontier Co-op backup) |
| June 22 (soft) | Tier 3 specimen orders | 2–3 weeks; CC covers all photography needs at launch quality |

---

## Section 2: Writing Schedule (~600 words)

### Total Writing Budget

Writing velocity for research-dense medicinal content from pre-compiled outlines: 300–350 words per hour. Hour counts include drafting, research integration, contraindication verification, FTC compliance review, and one self-edit pass per bundle.

| Bundle | Target Words | Raw Hours | Adjusted Hours | Critical Path Weight |
|---|---|---|---|---|
| Women's Health | 3,800 | 14–16 | 14–16 | Highest — leads sprint; contains deepest compliance requirements |
| Respiratory Health | 3,600 | 12–14 | 12–14 | Second — Elderberry toxicity framing most complex single section |
| Sleep and Nervines | 3,500 | 12–14 | 11–13 | Third — Valerian/Passionflower drug interaction warnings |
| Immunity Support | 3,800 | 14–16 | 10–12 | Fourth — Goldenseal CITES sidebar + Ashwagandha (900 words) |
| Digestive Support | 3,600 | 12–14 | 9–11 | Fifth — 2 shared species reduce adjusted hours to 9–11 |
| **Total** | **18,300** | **64–74** | **56–66** | Writing is the sole binding constraint on all 22 sprint days |

### Parallel vs. Sequential Tradeoffs

Writing is **strictly sequential per bundle**: Day 1 content (Black Cohosh identification/conservation sidebar) must precede Day 3 Women's Health self-edit pass. The contraindication blocks cannot be inserted retroactively — they are mandatory per-species sections written in sequence.

Design and photography are **fully parallel to writing on every sprint day**. No design or photography task blocks writing output. If writing falls behind pace, design and photography yield — writing never stops.

**Key sequential constraint — Pace Gate at D3 (June 24 EOD)**: This is the single point where the scope decision crystallizes. If Women's Health is below 2,500 words at EOD June 24, Option A (5-bundle single-writer) is not viable. Option C activates immediately. Upload dates for the three priority bundles remain June 29 / July 6–7 / July 13 regardless.

### Writing Bottleneck Identification

The binding constraint is writing velocity on every sprint day. The critical path runs through writing alone — no other track has a zero-float task during the sprint. The three bottleneck points are:

1. **June 24 EOD (D3)** — Pace gate. WH must be 2,500 words or Option C activates. No deferral possible.
2. **June 28 EOD (D7)** — Women's Health PDF must be export-ready for June 29 upload. Slipping this by one day (to June 30) delays Respiratory upload to July 8 and Sleep to July 15.
3. **July 3 EOD (D12)** — Design lock. Writing for Sleep continues. The design lock is not a writing blocker, but it marks the transition point where all Canva cover assets are frozen.

If writing falls behind daily pace on any non-gate day, Option C provides two additional structural float days (4 total vs. 2 under Option A) that absorb schedule variation without upload-date impact.

---

## Section 3: Canva Design Timeline (~400 words)

### Design Scope and Template Reuse Strategy

Phase 3 design is adaptation work, not rebuild work. All five bundle covers use the Phase 2 Canva template with three changes only: (1) hero image swap to the Phase 3 species, (2) bundle title and Latin binomials updated, (3) palette swapped to the Phase 3 medicinal hex codes. Estimated time per cover: 1.2 hours including pre-staging hero candidates.

Zone cards follow an identical pattern: the Phase 2 zone card template requires a 4-field content fill (bundle name, primary species, cultivation zone range, harvest timing) with no structural redesign.

Total design hours: 14. All 14 design hours have 3–14 days of float. Design is never the reason writing stops.

| Design Task | Hours/Unit | Units | Total Hours | Float | Notes |
|---|---|---|---|---|---|
| Palette pre-test (one zone card, color render check) | 0.5 | 1 | 0.5 | Pre-sprint | Confirms hex codes render correctly in Canva PDF |
| Bundle covers (hero + title + palette swap) | 1.2 | 5 | 6.0 | 3–4 days each | Pre-stage 3–5 hero candidates before each session |
| Zone cards (4-field fill, existing template) | 0.8 | 5 | 4.0 | 4 days each | Phase 2 zone card reuse: zero rebuild time |
| Practitioner bundle cover (8.5"×11", Gold/Burgundy premium layout) | 1.5 | 1 | 1.5 | 5 days post-sprint | Lowest urgency; produced after all 5 covers complete |
| Consistency review + export test all 5 covers | 0.5 | 1 | 0.5 | 2 days | Thumbnail crop 170×135px; hex code match; Playfair Display/Lato Italic |
| Revision buffer | — | — | 1.5 | Float absorption | One minor cover adjustment accounted for |
| **Total** | | | **14.0** | All non-blocking | Parallel to writing on every sprint day |

### Phase 3 Color Palette — Production Version

[USER GATE 3 — Palette] Confirm the six hex codes below by June 15. Auto-lock applies if no decision received.

| Color Name | Hex Code | Bundle Assignment |
|---|---|---|
| Deep Burgundy | #8B3E3E | Women's Health, Immunity |
| Sage Green | #6B8E6F | Respiratory, Digestive |
| Apothecary Gold | #D4AF37 | All bundles — accent |
| Clinical Cream | #F9F5F0 | All bundles — background |
| Muted Lavender | #9B8BA0 | Sleep and Nervines only |
| Dark Charcoal | #2C2C2C | All bundles — body text |

**Design lock: July 3 EOD.** Any cover revision after this date requires 1.2 hours of rework per cover already produced. Google Docs PDF export is the launch-viable fallback for any bundle if a Canva template issue is unresolvable on a critical-path day.

### Per-Bundle Design Schedule

| Task | Date | Float | Critical Path? |
|---|---|---|---|
| Brand Kit palette load + pre-test | June 21 | 1 day | Zero-float (must run before sprint Day 1) |
| Women's Health cover | June 23 | 4 days | No |
| Respiratory cover | June 24 | 4 days | No |
| Immunity cover | June 29 | 4 days | No |
| Sleep cover | June 30 | 3 days | No |
| WH + Resp zone cards | July 1–2 | 4 days | No |
| Digestive cover | July 3 | **0 days** | **YES — Design Lock EOD** |
| Immunity + Sleep + Digestive zone cards | July 6–7 | 2 days | No |
| Consistency review + export test | July 9 | 2 days | No |

---

## Section 4: Photography Staging (~500 words)

### Photography Strategy

All photography is executed in an indoor studio with north-facing window light and one reflector card. No outdoor location photography is required, eliminating weather dependency and permit risk. Photography is secondary to writing on every sprint day — if writing falls behind pace, photography sessions are compressed or deferred.

**Photography has 12-day float from its June 20 planned window to July 2.** Wikimedia Commons CC-BY-SA and iNaturalist CC-BY sources cover 100% of photography needs for all 14 unique species at guide launch quality. Live specimens ordered from suppliers improve v1.1 quality but are not v1.0 requirements.

### Fresh vs. Dried vs. CC Stock Decision Matrix

| Shot Type | Fresh Required? | Dried Acceptable? | CC Stock Primary? | Primary Source for v1.0 Launch |
|---|---|---|---|---|
| Cover / hero image | Preferred | Yes (well-staged) | YES | Wikimedia Commons CC-BY-SA |
| Identification / habit shot | No | N/A | YES | Wikimedia Commons; iNaturalist CC-BY |
| Root / rhizome preparation | No | YES — primary | Supplementary | Mountain Rose Herbs dried material |
| Flat-lay bundle shot (Etsy slot 4) | No | YES — primary | N/A | Dried herbs, staged per bundle theme |
| Lifestyle shot (guide on desk) | No | YES — props | N/A | Studio, dried herb props |

### Pre-Sprint Photography Track (June 3–21)

This track runs before the sprint and does not compete with sprint writing time.

| Activity | Duration | Window | Float | Notes |
|---|---|---|---|---|
| Props acquisition: kraft paper, mortar/pestle, glass jars, linen, wooden tray, white reflector 18"×24" | 2 hr | June 3–9 | 12 days | Budget $60–100 |
| Seedling photography: Calendula, Red Clover, Lemon Balm, Thyme, Lavender (seeds sown by May 26) | 4 hr | June 3–9 | 10 days | 30–40 images; cull to 20–30 keepers |
| Mature/flowering specimen photography (Black Cohosh, Tier 1 arrivals within 3 days of arrival) | 5 hr | June 10–16 | 5 days | iNaturalist CC-BY Appalachian range is automatic fallback |
| Dried herb studio session — Mountain Rose Herbs material, 5 bundle-themed flat-lays | 3 hr | June 17–21 | 1 day | 100–150 raw images; cull to 50–60 keepers. Bundle backgrounds: linen (WH) / white+elderberry (Resp) / dark wood (Imm) / grey muslin (Sleep) / kraft paper (Dgt) |
| Photo editing: cull; warm preset (+0.2 exp / -20 highlights / +15 shadows); export 2400×2400px | 3 hr | June 19–21 | 1 day | Create PHOTO_MANIFEST.csv |
| Attribution logging: all Wikimedia CC + iNaturalist sources in WORKLOG.md | 1 hr | June 21 | **0 days** | **Zero-float. Must complete before sprint Day 1.** |

**Target photo inventory by June 21**: 8–12 studio images per bundle (40–60 total), 3–5 hero/cover candidates per bundle (15–25 usable), attribution records complete.

### Supplier Coordination — Timing Sensitivity for Fresh Photography

Most live specimens arrive at or after sprint end. This is expected and planned. The v1.0 launch does not require live specimens.

| Species | Order Deadline | Expected Arrival | Sprint Impact |
|---|---|---|---|
| Black Cohosh | May 25 (optimal) | June 21–28 (if ordered May 25) | Within Sprint Week 1 if ordered May 25; CC fallback ready regardless |
| Goldenseal | June 8 (Path 1 only) | July 13–20 | Zero sprint impact — Path 2 CC recommended |
| Elderberry | June 15 | July 13–20 | Post-sprint arrival; CC-BY-SA berry cluster coverage is excellent |
| Echinacea | June 22 | July 8–15 | Wikimedia CC-BY-SA abundant for E. purpurea; iNaturalist for E. angustifolia |
| Passionflower | June 22 | July 12–19 | iNaturalist CC-BY SE US is the best visual source in Phase 3 |

**Supplier coordination to avoid last-minute fresh shortages**: The only scenario that would force a last-minute change is if Mountain Rose Herbs dried herbs fail to arrive by June 21 (studio session window). Contingency: order Frontier Co-op same day as MRH delay confirmed (3–5 business day ship). Both suppliers carry comparable species coverage.

---

## Section 5: Upload Sequence and Launch Gates (~400 words)

### Gate Status

| Gate | Threshold | Current Reading | Status | Margin |
|---|---|---|---|---|
| Phase 2 Forager Cohort conversion | >20% | 21.3% | CLEARED | +1.3 pp |
| Native Plants Regional Guide conversion | >1.5% | 2.24% | CLEARED | +0.74 pp |

Monitoring continues weekly May 30–July 13. A single gate dropping below threshold does not affect sprint writing — it affects upload authorization only if **both** drop simultaneously (see Fallback B).

### June 22 Go/No-Go Decision Criteria

Execute this gate check on June 20. The sprint launches June 22 if all five conditions are met:

1. Forager cohort ≥20% confirmed on June 20 analytics pull
2. Native plants conversion ≥1.5% confirmed on June 20 analytics pull
3. Attribution log complete in WORKLOG.md (zero-float, due June 21)
4. Canva Brand Kit Phase 3 palette loaded (zero-float, due June 21)
5. Sprint scope decision logged in WORKLOG.md (user gate, due May 30)

If conditions 1–2 both fail: defer sprint start to July 1 gate re-check. Pre-sprint activities (photography, design, supplier orders) continue regardless.

### Staggered Upload Sequence — June 22–August 3

| Upload Date | Bundle | Price | Spacing | Strategic Logic |
|---|---|---|---|---|
| June 29 | Women's Health | $22 | First | Black Cohosh: uncontested Tier 3 Etsy keyword; practitioner-buyer year-round intent |
| July 6–7 | Respiratory Health | $20 | 7–8 days | Cold/flu research intent builds July–August as buyers prep for autumn |
| July 13 | Sleep and Nervines | $20 | 7 days | July burnout-resolution peak; 3-bundle minimum met |
| July 15 | Practitioner tier live | $120–150 | 2 days | 3-bundle clinical library minimum reached; AHG cold outreach activates |
| July 20 | Immunity Support | $22 | 7 days | Review accumulation before November–December cold/flu gifting peak |
| August 3 | Digestive Support | $20 | 14 days | Autumn gut-health intent; Kit FORAGER20 dandelion cross-sell trigger |

**Stagger rationale**: Simultaneous uploads suppress individual listing momentum. Each new listing receives approximately 72 hours of Etsy algorithmic discovery as newest in its search category. Seven-day spacing maximizes each bundle's individual discovery window.

### Phase 2 Slip Impact on Phase 3

If Phase 2 Track B launch slips past May 30, cascade impact on Phase 3 is limited but documented:

| Phase 2 Slip | Phase 3 Impact |
|---|---|
| 5 days (launches June 4) | Gate metrics delayed 5 days; June 20 gate check shifts to June 25. Sprint launch slips to June 27. First upload shifts to July 4. Sleep upload shifts to July 18. Float absorbed. |
| 10 days (launches June 9) | Gate metrics delayed 10 days; June 20 gate check shifts to June 30. Sprint launch slips to July 1. First upload shifts to July 8. Sleep upload shifts to July 22. Practitioner tier shifts to July 24. August 17 all-bundles-live date; compresses review accumulation before November–December peak. |
| 14+ days | Escalate: review scope for reduction to 3 bundles before sprint begins; extend execution window or reduce Canva customization. |

---

## Section 6: Risk Analysis and Mitigation (~500 words)

### Risk Scoring Matrix

Probability: 1 = Low (15–25%), 2 = Medium (30–45%), 3 = High (50%+). Impact: 1 = Low, 2 = Medium, 3 = High.

| Risk | P | I | Score | Float Available | Primary Mitigation | Contingency Trigger |
|---|---|---|---|---|---|---|
| Goldenseal order missed (June 8) | 2 | 1 | 2 | Writing unaffected | Wikimedia CC path confirmed before June 8 | June 7 EOD: email NC + Missouri Botanical Gardens same day |
| Mountain Rose Herbs delayed | 1 | 2 | 2 | 5 days (Frontier Co-op backup) | Order June 15; Frontier Co-op 3–5 day ship | Not shipped by June 20: Frontier Co-op order same day |
| Canva design revision loops | 2 | 2 | 4 | 3–4 days per cover | Pre-stage 3–5 hero candidates; design lock July 3 | Any cover exceeds 2 hours: simplify to color-block header; Google Docs PDF fallback |
| Writing velocity below 300 words/hour | 2 | 2 | 4 | 2 float days | Pre-compiled outlines reduce research time | June 24 EOD WH below 2,500 words: activate Option C immediately |
| Daily pace unsustainable (5+ hrs/day required) | 2 | 2 | 4 | 2 float days (more under Option C) | Option C scope absorbs pace variation | June 26 writing 4+ hours behind pace: shift Resp to July 13, Sleep to July 20 |
| Palette revision after June 15 | 2 | 2 | 4 | 0 days post-design start | Confirm palette June 15; auto-lock if undecided | June 15 undecided: hex codes lock automatically; no further action required |
| AHG peer reviewer not secured by June 21 | 2 | 2 | 4 | 0 days (revenue ceiling only, not launch blocker) | Outreach June 8; follow-up June 15; expand to UpS network | June 21 no reviewer: begin sprint June 22; add quote retroactively when secured |
| Both Phase 2 gates drop below threshold | 1 | 2 | 2 | Pre-sprint activities unaffected | Continue pre-sprint prep; hold upload only | June 20 gate check both below: re-check July 1 |
| FTC compliance gap discovered in review | 1 | 3 | 3 | 2 days (D18 + Float Day 1) | FTC Quick Reference in Appendix A; review pass D18 | Uncorrectable claim found: hold bundle 48 hours for correction |
| Phase 2 Track B launch slips | 1 | 2 | 2 | Up to 10 days absorbed within structure | Pre-sprint activities continue regardless of Phase 2 slip | See Phase 2 Slip Impact table in Section 5 |

### Float-Day Allocation Per Risk

**Float Day 1 (July 12, 8 hours)** is the primary end-of-sprint buffer. Allocation priority:
1. Writing overrun from Week 3 (D17 Ginger, D18 FTC review)
2. Sleep upload staging and practitioner variant QA
3. WORKLOG.md final update

**Float Day 2 (July 13 afternoon, 4 hours)** — secondary buffer after the Sleep upload. Absorbs corrections to queued listings for Immunity and Digestive.

**Supplier delay float allocation**: Black Cohosh delayed 2 weeks — zero sprint impact, iNaturalist CC-BY activated same day. Mountain Rose Herbs 7-day delay — Frontier Co-op order same day. Elderberry delayed 2 weeks — Wikimedia CC-BY-SA berry cluster coverage is the best of any Phase 3 species; zero impact on any upload date.

### Contingency Branches by Scenario

**Scenario A — Option C activation on June 24**: WH, Resp, Sleep proceed on original dates. Immunity defers to July 20. Digestive defers to August 3. Revenue difference versus Option A at sprint close: $0 (same three bundles live on July 13). Estimated 90-day revenue difference: approximately $745, closing by September from ongoing sales momentum.

**Scenario B — All Tier 1 and 2 suppliers delayed**: CC fallback covers 100% of photography needs at launch quality for all 5 bundles. Writing and design proceed unchanged. Upload dates unaffected. The only difference is lower-quality Etsy listing photos — the guide content, which drives practitioner purchase decisions, is unchanged.

**Scenario C — Phase 2 slip 5 days (launches June 4)**: Sprint defers to June 27 start. First upload shifts to July 4. Sleep upload shifts to July 18. All three core upload dates shift 5 days in parallel. Float absorption complete with no scope reduction required.

**Scenario D — Writing velocity drops to 250 words/hour**: Activate Option C on June 24 pace gate. Condense shared-species second-occurrence sections to 300 words each (saves 4–8 hours). All three priority bundle upload dates preserved.

---

## Section 7: Critical Path Summary and Gantt Timeline (~300 words)

### Critical Path Identification

**The critical path is the writing track on every sprint day.** No other track has zero float on any sprint day. This means:

- Writing falls behind: upload dates slip.
- Design falls behind: write on; design catches up in its float days.
- Photography falls behind: write on; CC sources cover launch quality at zero schedule cost.
- Supplier delays occur: write on; CC fallback activates same day.

The zero-float sequence from May 30 to August 3 is fully documented in the Critical Path Map above. Every node in that chain has zero float. Every item not in that chain has float measured in days.

### 22-Day Sprint Gantt (June 22 – July 13)

```
        JUNE 22–28 (WEEK 1)      JUNE 29–JULY 5 (WEEK 2)    JULY 6–13 (WEEK 3)
        ─────────────────────    ───────────────────────    ──────────────────────
D1-D7   WRITING: WH + Resp ███████████████████████████▌
D1-D3   DESIGN: WH cover      ████                         
D4-D6   DESIGN: Resp cover        ████                     
D7      WH PDF QA              ██ │
                                  ↓ UPLOAD WH (June 29)
D8-D11                           WRITING: Immunity ████████████
D12-D14                          WRITING: Sleep        ████████████
D8-D9                            DESIGN: Imm+Sleep covers  ████████
D9-D10                           DESIGN: WH+Resp zone cards     ████
D11-D12                          DESIGN LOCK July 3          ▓ ████
                                           ↓
D15+                                                WRITING: Digestive ████████
D15-D17                                             DESIGN: Imm+Slp+Dgt zone cards ████
D18                                                 FTC review ███
D19                                                 SEO + PDF export ████
D20                                                 Upload prep ██
D21     FLOAT DAY 1 (July 12)                                            ░░░░░░░░
D22     UPLOAD Sleep (July 13)                                                ▌

PHOTOGRAPHY: [Pre-sprint track June 3–21, fully outside sprint window — 12-day float to July 2]
MILESTONES: ◆ June 29 WH Upload | ◆ July 6–7 Resp Upload | ◆ July 13 Sleep Upload

CRITICAL PATH (zero float): ██
PARALLEL TRACKS (float ≥3 days): ████
FLOAT DAYS: ░░░░

Post-sprint:
July 15 Practitioner tier live
July 20 Immunity upload
August 3 Digestive upload + Kit FORAGER20 trigger
```

### Float Days Summary

| Buffer | Date | Hours | Absorbs |
|---|---|---|---|
| Pre-sprint buffer | June 15–21 | 5 days available | Supplier or photography issues before sprint |
| Design float (all 5 covers) | June 23–27 | 3–4 days per cover | No cover is critical path |
| Pace gate buffer (D3) | June 24 | 1 hr | D2–D3 overrun; triggers Option C if needed |
| Sprint Float Day 1 | July 12 | 8 hrs | Week 3 writing/admin overrun |
| Sprint Float Day 2 | July 13 afternoon | 4 hrs | Post-upload corrections to queued listings |
| Post-sprint Immunity buffer | July 14–19 | 6 days | Sprint overrun before Immunity upload July 20 |

### User Decision Gates — Flagged for May 30

| Gate | Decision | Deadline | Consequence if Missed |
|---|---|---|---|
| [USER GATE 1] Sprint scope | Option A / B / C selection | May 30 | Blocks resource allocation; slips all supplier deadlines |
| [USER GATE 2] Goldenseal path | Path 1 (live order) or Path 2 (CC) | May 30 → order by June 8 | Zero sprint impact either path; clarity needed for supplier outreach June 1 |
| [USER GATE 3] Canva palette | Confirm 6 hex codes or defer to auto-lock | May 30 → deadline June 15 | Auto-lock June 15; any palette change after June 23 costs 1.2 hrs/cover |
| [GO/NO-GO] June 22 sprint start | Analytics gate check | June 20 | Defer sprint to July 1 if both gates below threshold |

---

## Appendix A: FTC Language Quick Reference

All five bundles must use qualifying language for any therapeutic claims. The table below covers the highest-risk phrasings in Phase 3.

| Do NOT write | Write instead |
|---|---|
| "Black Cohosh relieves menopause symptoms" | "Traditionally used in Cherokee and Appalachian folk medicine for women's hormonal transitions" |
| "Elderberry prevents colds" | "Studied in randomized controlled trials for cold duration and severity outcomes" |
| "Valerian cures insomnia" | "Studied in clinical trials for sleep-related outcomes, with mixed results across study designs" |
| "Goldenseal is antimicrobial" | "Contains berberine, an alkaloid studied in vitro and in clinical settings for antimicrobial activity" |
| "Ashwagandha reduces cortisol" | "Contains withanolides, studied in randomized controlled trials for stress-related physiological markers" |
| "Passionflower treats anxiety" | "Contains flavonoids including chrysin and vitexin, studied for GABA and serotonin receptor interactions" |

**Mandatory CITES sidebar — verbatim in Immunity bundle body**: "Goldenseal (*Hydrastis canadensis*) is listed in CITES Appendix II. International trade in wild-harvested material requires export permits. This guide recommends cultivated sources only. Forest Grown Verified (FGV) certified sources are available via the United Plant Savers participant directory at unitedplantsavers.org/forest-grown-verified."

**Mandatory per-species contraindication blocks** (non-deferrable to v1.1):
- Vitex: not for use during pregnancy or while taking hormonal medications including oral contraceptives
- Ashwagandha: not for use with thyroid medications or during pregnancy without medical supervision; may stimulate immune activity
- Valerian: potentiates CNS depressants and benzodiazepines; avoid before driving; do not combine with anesthetics
- Passionflower: contraindicated with MAOIs; drowsiness effect; do not combine with other sedatives
- Lemon Balm: may inhibit TSH binding; caution with thyroid conditions and thyroid medications
- Black Cohosh: do not use during pregnancy; avoid in hormone-sensitive conditions without medical supervision

---

## Appendix B: Pre-Sprint Action Checklist (May 21–June 21)

| Date | Action | Zero Float? |
|---|---|---|
| May 30 | Sprint scope decision (Option A / B / C) logged in WORKLOG.md | YES |
| May 30 | Goldenseal path decision (Path 1 or Path 2) logged in WORKLOG.md | YES |
| May 30 | Palette decision — confirm or defer to June 15 auto-lock | No (June 15 deadline) |
| June 1 | Email Prairie Moon + Strictly Medicinal: Goldenseal and Black Cohosh availability check | No |
| June 3–9 | Seedling photography window (Calendula, Red Clover, Lemon Balm, Thyme, Lavender starts) | No (10-day float) |
| **June 8** | **AHG peer reviewer outreach — 5–8 RH practitioners, Women's Health specialty** | **YES (2–3 week response cycle)** |
| June 8 | HARD DEADLINE: Goldenseal order placed OR CC path confirmed in WORKLOG.md | YES |
| June 10–16 | Mature/flowering specimen photography window | No (5-day float) |
| June 15 | HARD DEADLINE: Elderberry order placed (Prairie Moon or local nursery) | YES |
| June 15 | Mountain Rose Herbs dried herb order placed; request Goldenseal cultivated CoA | YES |
| June 15 | PALETTE DECISION DEADLINE — auto-lock if no decision | YES |
| June 17–21 | Dried herb studio photography session | No (1-day float) |
| June 19–21 | Photo editing: cull to 50–60 keepers; export 2400×2400px | No (1-day float) |
| **June 20** | **GO/NO-GO GATE CHECK: forager cohort ≥20% + native plants ≥1.5%** | **YES — defers sprint to July 1 if both fail** |
| June 21 | Attribution logging: all Wikimedia CC + iNaturalist sources in WORKLOG.md | YES |
| June 21 | Canva Brand Kit Phase 3 palette loaded (15-minute action) | YES |
| **June 21** | **AHG peer reviewer written confirmation should be in hand** | **Revenue ceiling if missed; not launch blocker** |
| June 22 | Tier 3 plant orders placed (Echinacea, Ashwagandha, Passionflower, Valerian, Ginger, Vitex) | No |
| June 22 | SPRINT BEGINS — Women's Health Day 1 | — |

---

*Document version 8.0 — May 21, 2026. Supersedes v7.0 (PHASE_3_MEDICINAL_HERBS_CRITICAL_PATH.md, 2026-05-21).*
*Companion CSV: `phase-3-medicinal-herbs-gantt.csv` (22-day sprint Gantt, June 22–July 13 execution window).*
*Source files: `medicinal-herbs-candidate-list.md`, `phase-3-medicinal-herbs-sourcing-guide.md`, `phase-3-medicinal-herbs-content-outline.md`.*
*Five launch gates: (1) forager cohort >20% — PASSED; (2) native plants conversion >1.5% — PASSED; (3) sprint scope by May 30 — PENDING; (4) supplier confirmation by June 8 — PENDING; (5) writing pace gate June 24 — PENDING.*
*Next reviews: May 30 (3 user decisions), June 8 (Goldenseal hard deadline + AHG outreach), June 15 (palette + Tier 2 supplier deadline + AHG follow-up), June 20 (go/no-go gate check), June 22 (sprint launch), June 24 (D3 pace gate).*
