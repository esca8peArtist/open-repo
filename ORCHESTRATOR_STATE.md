# Orchestrator State
> Auto-generated at 2026-05-07T03:02:23Z — do not edit. Source: PROJECTS.md, WORKLOG.md, BLOCKED.md, INBOX.md.

## Usage
🟢 Usage: Sonnet 4.4% (394,896 tokens) | All-models 63.3% | Reset in 117h | check: claude.ai → Settings → Usage & billing

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
- Session 856 task: finalize outstanding items, commit orchestration state, prepare for user input

**Autonomous Work Completed**:

✅ **Exploration Queue Items Committed**:
1. **ITEM19 — Path A Distribution Playbook** (36 KB) — day-by-day execution guide for institutional outreach Path A, production-ready
2. **ITEM19 — Path B Distribution Playbook** (38 KB) — day-by-day execution guide for public platform Path B, production-ready
3. **ITEM19 — Path Hybrid Distribution Playbook** (34 KB) — day-by-day execution guide for blended Path, production-ready
4. **ITEM21 — Seedwarden Market Expansion** (76 KB) — adjacent category analysis (garden tools, seeds, digital), B2B channel mapping, 18-month expansion roadmap, production-ready

**Project State (Session 856)**:
- **resistance-research**: Phase 1 launch infrastructure 100% ready (35 domains, 3 distribution path playbooks). Awaiting user path decision (A/B/Hybrid).
- **stockbot**: 2-session Jetson deployment live. May 12 Gate 1 checkpoint 5 days away. 7 architecture decisions pending user review.
- **seedwarden**: Phase 1 (Track A) awaiting tag corrections + Etsy verification. Phase 2 (Track B) production-ready for Etsy listing. Market expansion research (ITEM21) complete.
- **cybersecurity-hardening**: All Tiers production-ready. Tier 1 templates ready for distribution upon user approval.
- **mfg-farm**: All prep complete. Awaiting physical test print execution.
- **open-repo**: PR #1 open, awaiting external maintainer review.
- **off-grid-living**: Published. Social distribution awaiting user execution.
- **workout**: Nutrition framework complete (33,675 words total across 3 phases). Awaiting user review.
- **open-source-rideshare**: Paused.

**Blocks Status**:
- No new blocks. All previous blockers remain active (user decisions, external review, physical action, time-based event).

**Exploration Queue Status**:
- **Active items**: 0 (all pending items blocked on external conditions)
- **Items prepared for execution**: 3 path playbooks + market expansion research (awaiting preconditions)
- **Queue status**: Stable; will auto-refresh when user decisions unlock primary work

**Key Metrics**:
- **Total production-ready deliverables**: 44 domain documents + 3 distribution playbooks + nutrition framework + market expansion research
- **Phase 1 readiness**: 100% (infrastructure, contact templates, playbooks, tracking systems)
- **Autonomous work remaining**: 0 (awaiting external blockers)

**Next autonomous window**: 
1. Immediately post-user-path-decision → Phase 1 launch (3-4h autonomous execution)
2. May 12 post-Gate-1 → May 12 contingency implementation or post-Gate-1 architecture work
3. Post-user-approvals (seedwarden tags, cybersecurity Tier 1, stockbot ARCH) → implementation work

**Session 856 complete** (2026-05-07 04:30 UTC) — Exploration queue items ITEM19 and ITEM21 committed; orchestration state finalized. Standing by for user decisions and May 12 checkpoint.
