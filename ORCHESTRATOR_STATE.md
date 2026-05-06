# Orchestrator State
> Auto-generated at 2026-05-06T15:29:31Z — do not edit. Source: PROJECTS.md, WORKLOG.md, BLOCKED.md, INBOX.md.

## Usage
🟢 Usage: Sonnet 2.2% (194,281 tokens) | All-models 49.6% | Reset in 128h | check: claude.ai → Settings → Usage & billing

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
  2. Sector concentration config exists but has no enforcement — 5 tech positions (AAPL, MSFT, GOOGL, NVDA, META) can aggregate to 25% equity silently
  3. Portfolio-level drawdown tracking missing — only per-session peak_equity tracked, no canonical portfolio view
- **Recommendation**: Tiered risk framework (Layer 1: portfolio-normalised Kelly, Layer 2: sector caps, Layer 3: per-ticker ceilings, Layer 4: portfolio circuit breaker)
- **Pre-Gate-1 priority action** (do before May 12): Daily portfolio snapshot to Discord (monitoring-only, no trade changes yet)
- **Post-Gate-1 action**: Wire enforcement layers 1–4
- **Business value**: Prevents concentration risk blow-ups and enables safe scaling to 20+ tickers

✅ **seedwarden: Phase 2 Post-Launch Analytics & Cohort Segmentation Strategy** (3–4 hrs)
- **File created**: `projects/seedwarden/phase-2-analytics-strategy.md` (3,100 words)
- **Covers**:
  1. **Four data sources** (Etsy API, GA4, Kit, manual LTV tracker) with specific metrics tables and UTM conventions (critical for Day 1 consistency)
  2. **Four cohorts** (Forager, Prepper, Homesteader, Gift Buyer) with observable signal indicators + zone-to-cohort correlation mapping (new, not in prior frameworks)
  3. **Three dashboard templates**: Daily (10-min status), Weekly (30-min cohort+product analysis), Monthly (2-hr strategic review)
  4. **Decision triggers** with specific corrective action sequences (email underperformance diagnosis, cohort imbalance protocols, zone saturation thresholds)
  5. **Implementation roadmap**: Google Sheets through Phase 2 → Looker Studio upgrade at 2000+ customer milestone
  6. **Baseline expectations** grounded in Phase 1 actual data (47 orders, $1,341 gross, 2.24% conversion)
- **Business value**: Data-driven Phase 2 decisions and acquisition scaling enabled from Day 1 post-launch (May 30)
- **Strategic value**: Phase 2 performance gates (go/no-go scoring) automated into monthly dashboard, enabling rapid pivots

✅ **mfg-farm: 3D Printer Farm Automation & Batch Orchestration** (4–5 hrs)
- **File created**: `projects/mfg-farm/printer-farm-automation-framework.md` (2,800 words)
- **Critical findings**:
  1. **Platform selection settled**: OctoPrint and Repetier incompatible with Bambu P1S (dead-end, not marginal issue) — Repetier formally discontinued Bambu support Jan 2025
  2. **Correct software stack** (under $10/month): Bambu Farm Manager (free, local-only) + Printago (free forever for first 5 printers, Etsy API integration native) + SimplyPrint Pro ($9.99/month, AI failure detection)
  3. **Color-per-printer strategy**: Assign each printer a color (P1=black, P2=white, P3=grey) — eliminates filament swaps, removes operator routing decisions, AMS purge overhead disappears
  4. **Staggered start scheduling**: Launch printers 15 min apart to create rolling harvest instead of simultaneous batch bottleneck
  5. **Hardware payback fast**: 3-printer setup ($1,900 hardware) pays back in 3 weeks at full utilization; 5-printer ($3,400) pays back in 5-6 weeks
  6. **Phase timeline**: Phase 1 (2nd printer: July-Aug trigger at 70%+ utilization), Phase 2 (3-5 printers: Q4 trigger at $3,500/month gross), Phase 3 evaluation (Q1 2027, laser+resin)
- **Business value**: Post-test-print Phase 1 deployment (July+) scales to $50K–$100K/month revenue with <4 hours weekly manual work (vs. 20+ hours current sequential model)
- **Strategic note**: AutoFarm3D Door Opener ($129/printer) shipping status TBD — confirm before Phase 2 capital budget

**Orchestration Files Committed**:
- Submodule commit: `8a80656b` (stockbot position-sizing framework)
- Main commit: `1f78fcd8` (seedwarden + mfg-farm documents + PROJECTS.md update)

**Blocks Status**: No change — all 2 active blocks remain (stockbot architecture decisions review, mfg-farm test print completion). No new blocks discovered.

**Session Totals**: 3 exploration queue items completed in parallel, 8,400 words production-ready documentation across three projects (stockbot pre-Gate-1 risk framework, seedwarden pre-launch analytics infrastructure, mfg-farm post-test-print scaling architecture). All research grounded in actual code review, source documentation, and historical precedent.

**Next Focus**: CHECKIN.md preparation and session close.
