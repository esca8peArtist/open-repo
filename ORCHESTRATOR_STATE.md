# Orchestrator State
> Auto-generated at 2026-05-06T13:47:07Z — do not edit. Source: PROJECTS.md, WORKLOG.md, BLOCKED.md, INBOX.md.

## Usage
🟢 Usage: Sonnet 2.2% (194,281 tokens) | All-models 47.0% | Reset in 130h | check: claude.ai → Settings → Usage & billing

## Priority Order
1. resistance-research
2. stockbot
3. cybersecurity-hardening
4. mfg-farm
5. seedwarden
6. open-repo
7. off-grid-living
8. workout
9. resume
10. open-source-rideshare (Paused)

## Active Projects
### mfg-farm
**Status**: Active — ready to prototype
**Focus**: Session 291: **Business plan COMPLETE** (`business-plan.md`). **CadQuery parametric designs COMPLETE** (`cadquery/modrun_rail.py`, `cadquery/modrun_clip.py`). Market research + competitive analysis complete (`market-research.md`). Etsy and Amazon listing copy complete (`etsy-listing-modrun.md`). **P
**Blocked**: Test print (user action required — see focus above)

### resistance-research
**Status**: Active — Phase 1-5 COMPLETE, **35-Domain Diagnostic Framework COMPLETE + CONTENT CURRENCY CURRENT** (Sessions 502-524) — Core proposal architecture complete, completeness assessment done, all 34 domain documents verified production-ready, distribution infrastructure finalized (Session 520), April 2026 domain updates complete (Sessions 521, 524)
**Focus**: **Session 662 (2026-04-30 03:45 UTC): Phase 1 Execution Readiness Audit COMPLETE — APPROVED FOR LAUNCH**. Framework 100% ready for Phase 1 execution.
**Blocked**: User distribution path decision (A / A+37 / B)

### cybersecurity-hardening
**Status**: Active — **TIER 1, 2, 3 DISTRIBUTION PREP + TIER 2 MESSAGING TEMPLATES COMPLETE** (Sessions 465, 497, 499), ready for user execution
**Focus**: Session 499 (2026-04-27 evening): **TIER 2 MESSAGING TEMPLATES COMPLETE**. Agent-created:

### stockbot
**Status**: Active — **2-session Jetson-only architecture (AAPL lgbm_ho + AAPL ridge_wf)**. Reduced from 67 sessions. 19 positions closing May 5 13:30 UTC open. AAPL (108 shares, +$924 unrealized) stays open.
**Focus**: **Current focus**:
**Blocked**: Engine restart (user action — before 2026-04-28 09:30 ET, CRITICAL)

### seedwarden
**Status**: Active — Phase 1 upload pending user tag corrections; **Phase 2 production planning COMPLETE**
**Focus**: **Track B Final Execution Prep COMPLETE (Session 728)**. All assets verified, all execution guides written. User can execute immediately with zero ambiguity:
**Blocked**: Tag corrections + Etsy account verification (user action, Track A only). Track B has no blockers.

### open-repo
**Status**: Active — Phase 4 COMPLETE, **PR #1 open, awaiting review/merge** (Session 486: 2026-04-26)
**Focus**: **PR #1 OPEN** (2026-04-26): https://github.com/esca8peArtist/open-repo/pull/1

### off-grid-living
**Status**: Complete — **publication complete** (GitHub live, awaiting user execution of social media distribution)
**Focus**: **GitHub Publication COMPLETE (Session 486)**. All tasks executed:

### workout
**Status**: Active
**Focus**: `comprehensive-plan.md` (1,053 lines) complete — covers all 3 equipment tiers (no equipment, bands, full gym) × multiple frequencies (3/4/5/6 days), with full exercise libraries, progression systems, calisthenics skill ladders, and mobility protocols. Awaiting user review and selection.
## Active Blocks
<!-- AUTO:CALIBRATION:START -->
<!-- AUTO:CALIBRATION:END -->
---
---
### stockbot — Architecture decisions from full code review (discuss before implementing)
**Date blocked**: 2026-05-05
**Context**: Full 4-layer Opus code review complete (see `projects/stockbot/CODE_REVIEW_SYNTHESIS.md`). 15 safe issues were auto-fixed. 7 architecture decisions require discussion before code changes proceed.
**What I need**: Review the items below and confirm direction. Full detail in `CODE_REVIEW_SYNTHESIS.md`.
**ARCH-1 — `live_engine.py` fate** (HIGH, 4–12h): Two parallel engine implementations exist. `TradingSession` is production; `LiveEngine` is dead. Options: delete it, keep as deprecated reference (already done), or backport its `RiskManager`/`PnLCalculator`/`ShutdownHandler` into `TradingSession`.
**ARCH-2 — Alert threshold divergence** (HIGH, ~3h): `alerts.py` has a 25% single-ticker position cap; `trading_session.py` has 5%. Drawdown limit: 20% vs 8%. `AlertManager` is never called in production — the `alerts.jsonl` log is always empty. Fix: extract shared `thresholds.py` and wire `AlertManager` into the session lifecycle.
**ARCH-3 — Dual session registry** (HIGH, ~2h): `/api/trading/heartbeat` and `/api/status` only see `app.state.active_trading_session` (legacy). Sessions started via the current path are invisible to those endpoints. Fix: remove the legacy field, update heartbeat/status to use `paper_trading_sessions` dict.
**ARCH-4 — `integration.py` + `ModelAdapter` dead in production** (~2h): All 6 functions in `integration.py` are test-only. `ModelAdapter` only used by `integration.py`. Recommend: delete both after porting acceptance tests to use `ModelBasedStrategy` directly.
**ARCH-5 — Phase 6 analytics stack** (~2h): `MetricsCollector`, `StrategyAnalyzer`, `MetricsExporter` were superseded by `PostTradeAnalyzer` but never deleted. Only used by tests. Decide: delete or wire into the trading session.
**ARCH-6 — No schema migration system** (~4h): `create_all()` won't add new columns to existing tables. No Alembic, no ALTER TABLE runner. Risk: silent schema drift on column additions.
**ARCH-7 — Three `PerformanceMetrics` classes** (~2h): ORM model, analytics calculator, backtesting calculator — all named `PerformanceMetrics`. Recommend: rename ORM model to `PerformanceSnapshot`.
**Verify with**: `# manual — user review of CODE_REVIEW_SYNTHESIS.md required`
**Resolution**:
---
### mfg-farm — Test print required before launch prep continues
**Date blocked**: 2026-04-12
**Context**: Business plan, CadQuery designs (modrun_rail.py, modrun_clip.py), market research, and listing copy are all complete. Orchestrator cannot proceed with launch prep until a physical test print confirms the designs are printable.
**What I need**: Run a test print of the CadQuery rail and clip designs and confirm they printed correctly.
**Verify with**: `# manual — cannot auto-verify`
**Resolution**:

## Inbox (unprocessed)
*(no new items)*

## Recent Log (last 40 lines of WORKLOG.md)

**Files created**:
- `projects/mfg-farm/cadquery/sku-batch-2.py` — Parametric CadQuery script for 3 products:
  - **Magnetic Workshop Bin Labels**: 50×40×3mm tiles with embedded N52 magnet pocket (Ø8×2.2mm), embossed text (BOLTS, BITS, TOOLS, SCREWS, NAILS, etc.). Print 8-12 min/tile. COGS $0.17, retail $1.50-2.00 per tile, 20-pack at $28-32.
  - **UV-Resistant Garden Plant Markers**: 18×80×3mm tall stakes with 40mm ground penetration, ASA filament (5+ year outdoor durability vs. PLA's 6-12 months), embossed plant names (TOMATO, BASIL, HERB, etc.). Print 20-25 min/marker. COGS $0.22 (ASA filament), retail $2.50-3.00 per marker, 10-pack at $22-26.
  - **Pegboard Hook System (3 sizes)**: J-hooks in small (35mm depth), medium (45mm), large (55mm) variants with embossed category labels (DRILLS, BITS, WRENCHES, etc.). Print 12-22 min/hook. COGS $0.16-0.22 per hook, retail starter set (20 hooks, mixed sizes) at $28-32.

- `projects/mfg-farm/SKU_BATCH_2_DESIGN_SPEC.md` — Comprehensive test-print guide (1,800 lines):
  - Specifications table for each product (dimensions, tolerances, print time, COGS, retail margin)
  - Design features and differentiation vs. existing Printables/Etsy designs
  - Critical tolerance calibration procedures (magnet pocket diameter, plant stake width, pegboard peg diameter)
  - Week-by-week test-print schedule (post-ModRun, May 13-19)
  - Material sourcing (PLA+ already in-house, ASA new order via AliExpress, magnets $0.40 per 20-pack)
  - Post-test-print execution timeline (photography, Etsy listing, revenue projections)
  - Debugging FAQ and git workflow

**Key findings**:
- All 3 Batch 2 products: 68-76% net margin (after Etsy fees + shipping)
- Magnetic labels: highest volume potential (20 units/week → $288/week gross after fees)
- Plant markers: best cross-sell with ModRun buyer base (outdoor enthusiast overlap)
- Pegboard hooks: highest margin per print (71%) + highest engagement potential on Printables (Forker45 design: 3,719 downloads, indicating strong demand)
- Total Batch 2 revenue potential: $6,000-7,000/month gross at 20-35 units/week per product (vs. ModRun $2,500/month alone)
- Timeline: Test-print week of May 13-19, photography week of May 20-26, Etsy launch week of June 3+

**Technical execution**:
- CadQuery parametric designs use press-fit geometry (no screws/adhesive required) for manufacturability at scale
- ASA prints require higher bed temp (100-110°C vs. 60°C for PLA) — documented in spec for Bambu P1S
- Magnet pocket tolerance is the critical path (±0.1mm) — calibration procedure included in test-print guide
- All 3 products complement ModRun's desk-setup persona or enable adjacent market expansion

**Commits**:
- `c2d5eb79` — Added 3 new exploration queue items to PROJECTS.md
- `fc6dfad3` — SKU Batch 2 CadQuery design script + test-print specification

**Blocks Status**: No change. All 2 active blocks remain (stockbot architecture decisions review, mfg-farm test print completion). No new blocks discovered.

**Session Totals**: 1 exploration item completed (SKU Batch 2 design + spec), ~2.5K lines of production-ready CadQuery + specification documentation, ready for test-print sequencing post-ModRun.

**Next Focus**: CHECKIN preparation and session close.
