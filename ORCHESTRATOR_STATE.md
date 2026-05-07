# Orchestrator State
> Auto-generated at 2026-05-07T08:44:47Z — do not edit. Source: PROJECTS.md, WORKLOG.md, BLOCKED.md, INBOX.md.

## Usage
🟢 Usage: Sonnet 4.4% (394,896 tokens) | All-models 69.8% | Reset in 111h | check: claude.ai → Settings → Usage & billing

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
**Focus**: **Session 866 (2026-05-07): Domain 42 Distribution Infrastructure COMPLETE + Phase 1 Readiness Assessment**. Domain 42 (Drug Policy) has critical May 28 DEA hearing participation deadline (21 days). All distribution infrastructure for Wave 1 outreach built and committed. Phase 1 is production-ready 
**Blocked**: User distribution path decision (A / A+37 / B)

### cybersecurity-hardening
**Status**: Active — **TIER 1, 2, 3 DISTRIBUTION PREP + TIER 2 MESSAGING TEMPLATES COMPLETE** (Sessions 465, 497, 499), ready for user execution
**Focus**: **Session 866 (2026-05-07): Phase 1 Pre-Launch Threat Accuracy COMPLETE — All flags resolved, production-ready for Tier 1 outreach**. Phase 2 Sequencing Strategy (Session 837) complete with 5,500-word threat model and 12-month roadmap.
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
  2. `phase-1-gist-css-template.html` (production-ready HTML/CSS) — Testable template with responsive design, dark mode support, copy-paste ready
- **Key Finding**: Infrastructure is more complete than initial estimate suggested. Timeline compressed from 90 minutes post-decision to 60 minutes sequential (30–40 minutes with parallelization)
- **Business Value**: User chooses distribution path → Phase 1 Gist creation + field-fill + announcement in <30 minutes instead of 4+ hours
- **Committed**: Both files to master by subagent ac2fe73699c6222ac

✅ **seedwarden: Phase 2 Buyer Retention & Lifecycle Campaign Strategy** (~4 hours, parallel subagent)
- **Deliverable**: `phase-2-buyer-retention-lifecycle-strategy.md` (3,800 words, production-ready)
- **Coverage**: 6 comprehensive sections:
  1. Phase 1 baseline & Phase 2 cohort modeling (Forager/Prepper/Homesteader/Gift Buyer/Herbalist)
  2. Email lifecycle architecture (6 campaigns, 20+ touches, Days 0–90+)
  3. Kit automation configuration (paste-ready sequences, segment logic)
  4. Landing pages & incentive architecture (3 pages, 7 triggers)
  5. Analytics dashboard & decision triggers (daily/weekly/monthly dashboards with thresholds)
  6. Implementation roadmap (6-day pre-launch timeline, contingencies)
- **Key Finding**: Herbalist cohort enters Phase 2 as primary LTV growth lever (3x vs. Gift Buyer 1x). Kit automation is critical path — Zapier Option A / manual CSV Option B split ensures launch-day resilience.
- **Business Value**: Phase 2 launch May 30 → systematic buyer lifecycle campaigns from Day 1; projected 2–3x LTV lift ($28 → $60+/buyer)
- **Committed**: File to master by subagent a56521a4189124113

**Combined Exploration Queue Output**:
- 2 items completed (9,300 words total, production-ready)
- Both documents are fully implemented and testable (not just architectural drafts)
- Both enable parallel pre-launch execution (user can stage these systems before triggering launches)

**Project State After Session 858**:
- **Exploration Queue**: 3 remaining items (1 blocked on May 12 Gate 1 pass; 2 could theoretically be started now but have low immediate value)
  - stockbot: Covered Call Automation (blocked until Gate 1 pass)
  - resistance-research: Phase 1 Distribution Risk Mitigation Playbook (could start)
  - cybersecurity-hardening: Tier 2 Distribution Sequencing (could start)
- **All major projects**: Still awaiting user decisions (path choice, architecture review, test print, tag corrections, Tier 1 approval)
- **Autonomous work remaining**: Limited to lower-priority items without blocking external dependencies

**Blocks Status**: No new blocks identified. All existing blocks remain unchanged (user decisions, external review, physical action)

**Next Autonomous Window**: 
1. Immediately post-user-path-decision → Phase 1 distribution execution (user runs `fill_templates.py` + Gist API)
2. Immediately post-user-architecture-approval → stockbot code refactoring (ARCH-1 through ARCH-7 implementations)
3. May 12 post-Gate-1 checkpoint → contingency implementation or Gate 2 planning
4. Post-test-print-completion → mfg-farm post-launch scaling sequence

**Session 858 complete** — Exploration queue items 2 and 3 (from remaining queue) completed; both critical path files for downstream launches now staged and production-ready.
