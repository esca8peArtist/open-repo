# Orchestrator State
> Auto-generated at 2026-05-07T13:59:02Z — do not edit. Source: PROJECTS.md, WORKLOG.md, BLOCKED.md, INBOX.md.

## Usage
🟡 Usage: Sonnet 4.4% (394,896 tokens) | All-models 75.3% | Reset in 106h | check: claude.ai → Settings → Usage & billing

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
**Focus**: **Session 876 (2026-05-07): Tracker Maintenance COMPLETE + Phase 1 Distribution Risk Mitigation Playbook COMPLETE**. All Phase 1 distribution infrastructure and risk mitigation now production-ready. Domain 42 (Drug Policy) has critical May 28 DEA hearing participation deadline (21 days). All distrib
**Blocked**: User distribution path decision (A / A+37 / B)

### cybersecurity-hardening
**Status**: Active — **TIER 1, 2, 3 DISTRIBUTION PREP + TIER 2 MESSAGING TEMPLATES COMPLETE** (Sessions 465, 497, 499), ready for user execution
**Focus**: **Session 876 (2026-05-07): Phase 2 Scenario Playbooks v1.1 (May 2026 Intelligence) COMPLETE**. Phase 1 threat accuracy verified; all distribution infrastructure ready. Phase 2 expansion staging with current threat intelligence.
**Blocked**: None — Phase 1 ready for user approval and execution

### stockbot
**Status**: Active — **2-session Jetson-only architecture (AAPL lgbm_ho + AAPL ridge_wf)**. Reduced from 67 sessions. 19 positions closing May 5 13:30 UTC open. AAPL (108 shares, +$924 unrealized) stays open.
**Focus**: **Current focus**:
**Blocked**: Engine restart (user action — before 2026-04-28 09:30 ET, CRITICAL)

### seedwarden
**Status**: Active — Phase 1 upload pending user tag corrections; **Phase 2 production planning COMPLETE**
**Focus**: **Phase 2 + Phase 3 Execution Prep Complete (Sessions 728, 861)**. Phase 2 launches May 30, 2026. Phase 3 (Medicinal Herbs) implementation assets production-ready.
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

### 2. Item 1 Execution — stockbot Post-Trade Analytics Stack Unification

**Deliverable**: `projects/stockbot/framework-unified-analytics-architecture.md` (514 lines, design document, production-ready)

**What it covers**:
- Current state analysis (PostTradeAnalyzer + Phase 6 stack + naming collisions)
- Unified architecture (5 components: realtime engine, round-trip attribution, snapshots, post-trade analysis, API)
- Implementation roadmap (Phase 1: rename + consolidate 5h; Phase 2: extend PostTradeAnalyzer 4h; Phase 3: API 3h; Phase 4: testing 2h)
- Migration path (zero breaking changes; renamed classes, new methods, no removed APIs)
- Success criteria (PerformanceMetrics properly namespaced, Phase 6 dead code removed, new endpoints tested)

**Key Insights**:
- RealtimeMetricsEngine encapsulates Phase 6 logic; interface stable, internal refactoring only
- PerformanceSnapshot (rename from ORM PerformanceMetrics) consolidates storage; no schema changes
- PostTradeAnalyzer extended with attribution_summary(), signal_effectiveness(), strategy_comparison()
- Unified AnalyticsReport composes realtime + historical + post-trade into single API response
- Feasible pre-Gate-2 launch; implementation begins immediately post-Gate-1 (May 12)

**Business Value**: 
- Removes technical debt before multi-ticker scaling
- Enables production-grade dashboards (history + realtime + analysis)
- No breaking changes; existing code continues working

**Committed**: `projects/stockbot/framework-unified-analytics-architecture.md` (stockbot submodule, commit e923399)

---

**Project Status**:
- All prior blocks unchanged (resistance-research path decision, stockbot ARCH decisions, mfg-farm test print, seedwarden Track A)
- Queue refreshed with 3 ready-to-work items (no prerequisites, independent of user decisions)
- Item 1 (stockbot) design-complete; implementation ready post-Gate-1

**Next Session Options**:
1. Work remaining 2 exploration items (5-9 hours) if time available
2. Wait for user decisions to unblock project work
3. Monitor May 12 Gate 1 checkpoint; if Pass, begin Gate 2 implementation immediately

**Suggested Priority**: Items 1-2 are research/design (no risks); execute before May 12 if time available to build readiness.
