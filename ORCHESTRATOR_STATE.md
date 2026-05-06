# Orchestrator State
> Auto-generated at 2026-05-06T23:22:24Z — do not edit. Source: PROJECTS.md, WORKLOG.md, BLOCKED.md, INBOX.md.

## Usage
🟢 Usage: Sonnet 4.2% (373,422 tokens) | All-models 60.7% | Reset in 121h | check: claude.ai → Settings → Usage & billing

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
**Focus**: **Session 837 (2026-05-06): May 2026 Domain Maintenance COMPLETE; Phase 1 Domains Current + Ready for Distribution**. Three domains updated with FISA 702 final outcome and Callais redistricting cascade. Framework 100% ready for Phase 1 execution.
**Blocked**: User distribution path decision (A / A+37 / B)

### cybersecurity-hardening
**Status**: Active — **TIER 1, 2, 3 DISTRIBUTION PREP + TIER 2 MESSAGING TEMPLATES COMPLETE** (Sessions 465, 497, 499), ready for user execution
**Focus**: **Session 837 (2026-05-06): Phase 2 Sequencing Strategy COMPLETE**. Updated threat model identifies 5 capability gaps; advanced protection playbooks designed; 12-month Phase 2 roadmap complete. Three urgent pre-launch flags identified for Phase 1.

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
- Date changed to 2026-05-07 (May 7)
- Oriented to ORCHESTRATOR_STATE.md + PROJECTS.md for active work
- Found all major Phase 2 research work already complete from prior sessions
- Selected highest-priority unblocked work: Item 15 (Workout Nutrition)

**Autonomous Work Completed**:

✅ **Phase 2 Validation (Parallel Agents)** — All work from Sessions 850-851 confirmed complete:
1. **resistance-research Domain 23**: Already production-ready (10,758 words, Session 521)
2. **seedwarden Wild Edibles PDF credits**: Already complete with photo credits page (Session 851, commit 4ed31f8f)
3. **cybersecurity-hardening pre-launch flags**: Flags 1 & 3 updated with new commits (7b9428f4, aa6049d8); Flag 2 already implemented

✅ **Workout Nutrition & Meal Planning Framework** (EXPLORATION_QUEUE.md Item 15):
- **Deliverable**: 6 comprehensive documents (16,748 words total)
  1. `nutrition-01-macro-micronutrient-framework.md` (2,515 words) — Protein/carb/fat targets by goal, micronutrient protocols with blood test thresholds
  2. `nutrition-02-meal-timing-nutrient-timing.md` (2,650 words) — Pre-workout, intra-workout, post-workout timing; sleep nutrition stack; daily meal architecture
  3. `nutrition-03-meal-planning-templates.md` (3,530 words) — 3×7-day meal plans (hypertrophy, strength, conditioning), vegan adaptations, budget tiers
  4. `nutrition-04-supplementation-guide.md` (2,711 words) — Tier 1/2/3 supplements with evidence grades, dosing, timing, monthly cost analysis
  5. `nutrition-05-periodization.md` (2,437 words) — Macro cycling, caloric models (surplus/maintenance/deficit), body recomposition, annual periodization calendar
  6. `nutrition-06-recovery-optimization.md` (2,905 words) — Sleep quality nutrition, hydration protocols, stress management, injury recovery phases, monitoring signals
- **Sources**: 12 peer-reviewed studies from 2024–2025; IOC consensus guidelines
- **Integration**: Fully aligned with Phase 1 comprehensive workout programs (16,927 words) and Phase 2 sports-specific extensions
- **Commit**: Committed to master by workout agent

**Projects Status After Session 853**:
- **resistance-research**: All 44 domain documents production-ready (35 Phase 1 + 9 Phase 2 high-priority). Phase 1 launch-ready; awaiting user path decision (A/A+37/B).
- **workout**: All 3 phases complete: Phase 1 (comprehensive programs), Phase 2 (sports extensions), Phase 3 (nutrition framework). 33,675 total words. Production-ready for user review.
- **seedwarden**: Phase 1 tag corrections pending; Phase 2 (Track B) completely ready for publication.
- **cybersecurity-hardening**: All Tiers production-ready; awaiting user distribution approval.
- **stockbot**: May 12 checkpoint 5 days away; architecture review pending.
- **mfg-farm**: Test print block unchanged; all post-test sequences staged.
- **open-repo**: PR #1 awaiting external review.

**Blocks Status**: No new blocks. Previous 2 blocks remain user-action-dependent (stockbot ARCH decisions, mfg-farm test print).

**Exploration Queue Status**: Item 15 (Workout Nutrition) completed; remaining queued items blocked on external triggers (user path decision for Item 6, PR #1 merge for Item 5, etc.). Queue will auto-refresh when user triggers Phase 1 execution.

**Key Metric**: Session completed autonomous research work; all major discovery/documentation complete. Next session will focus on Phase 1 execution or user-decision-dependent work.

---
