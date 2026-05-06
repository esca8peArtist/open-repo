# Orchestrator State
> Auto-generated at 2026-05-06T10:54:52Z — do not edit. Source: PROJECTS.md, WORKLOG.md, BLOCKED.md, INBOX.md.

## Usage
🟢 Usage: Sonnet 2.2% (194,281 tokens) | All-models 43.8% | Reset in 133h | check: claude.ai → Settings → Usage & billing

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

1. ✅ **Exploration Queue Refresh** (Session 815)
   - Added 3 high-value exploration items to PROJECTS.md:
     - resistance-research: Post-Phase-1 Community Adaptation & Feedback Integration Deep Dive (3-4 hrs)
     - stockbot: Post-Gate-1 Live Trading Launch Operational Architecture (4-5 hrs)
     - mfg-farm: Etsy Organic Discovery & SEO Strategy for 3D Printing Niche (3-4 hrs)
   - Rationale: Per protocol, Exploration Queue was empty post-Session 814; maintain 2-3 active items minimum

2. ✅ **mfg-farm: Etsy SEO Strategy & Keyword Research** (COMPLETE — Session 815)
   - **Deliverables**:
     - `projects/mfg-farm/etsy-seo-strategy.md` (43 KB, ~3,500 words, 8 sections)
     - `projects/mfg-farm/keyword-research-data.csv` (13 KB, 70 keywords)
   - **Key findings**:
     - Etsy Listing Quality Score dominated by conversion rate (1.5-2.5% target for new 3D-printed shops vs. 3-5% for established)
     - June 2025 ban on template-based 3D prints removed commodity competition — original-design sellers like ModRun are algorithmically advantaged
     - Four seasonal peaks: Jan (120-150% baseline, critical), March-May (moving/spring), July-Sept (back-to-school), Nov-Dec (gift)
     - Whitespace: standing-desk-specific cable management (under 200 listings, high buyer intent), minimalist positioning
     - Optimal bundle: Tier 2 (20 clips + 2 rails, $24-28, $4.50 COGS) = 84-86% gross margin with best AOV/profitability balance
     - Video demonstrations outperform lifestyle photos 2.5-3x in click-through rate for 3D-printed products
   - **Business value**: Post-test-print revenue optimization, informs listing strategy (title/tag), seasonal launch timing, bundle architecture, paid-ad allocation
   - **Agent**: general-research (distributed research, WebSearch + WebFetch + analysis)
   - **Commit**: 651e1473 (feat: mfg-farm Etsy SEO strategy & keyword research)
   - **Status**: Ready for immediate post-test-print execution; recommend eRank validation of keyword volumes before finalizing copy

**Block Status** (unchanged):
- ⏳ **DTBP Reset**: 13:30 UTC today (May 6) — automatic verification pending
- 🔴 **Architecture decisions** (stockbot): awaiting user review of CODE_REVIEW_SYNTHESIS.md
- 🔴 **Distribution path** (resistance-research): awaiting user selection for Phase 1 launch (A / A+37 / B)
- 🔴 **mfg-farm test print**: awaiting user execution of CadQuery designs (SEO research completed independently)
- 🔴 **seedwarden tag corrections**: awaiting user action on Track A (Track B ready)
- 🔴 **cybersecurity Tier 1 approval**: awaiting user approval to begin outreach

**System Status**: Excellent. All projects at maximum readiness. Exploration Queue now has 2 active items (post-Phase-1-launch and post-Gate-1 research items, both awaiting user decisions to unblock). No errors or degradation.

**Next Milestone**:
- **Primary**: May 6 13:30 UTC DTBP reset verification (auto-triggered)
- **Secondary**: User decisions on 5 pending items unlock 3-4+ hours of autonomous work per decision

**Session Duration**: ~35 minutes (orientation + research agent execution)
**Tokens Used**: ~65K (research agent)
