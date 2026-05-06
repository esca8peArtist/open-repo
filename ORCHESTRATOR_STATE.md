# Orchestrator State
> Auto-generated at 2026-05-06T21:25:25Z — do not edit. Source: PROJECTS.md, WORKLOG.md, BLOCKED.md, INBOX.md.

## Usage
🟢 Usage: Sonnet 2.2% (194,281 tokens) | All-models 56.9% | Reset in 123h | check: claude.ai → Settings → Usage & billing

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
  8. **Institutional Design** (Part 8): Risk analysis and safeguards against weaponization

- **Key findings**: 
  - Federal official corruption prosecutions declined from 150–180/year (2009–2016) to 70–85/year (2025 pace)
  - Senate ethics: 181 violations reviewed in 2025, zero disciplinary actions issued, continuing 19-year pattern
  - Singapore model offers centralized anti-corruption architecture; South Korea's prosecution reform offers democratic-safe prosecution separation
  - Germany's audit-office model offers independence without prosecution authority concentration
  
- **Business value**: Closes structural gap in Phase 1 proposal (corruption as democratic failure); opens distribution channel to ethics watchdog organizations (POGO, Common Cause, state AGs); grounds reform proposals in international precedent

- **Status**: Production-ready; integration with Phase 1 domains (cross-references to Domains 1, 6, 34, 35); ready for Phase 2 distribution decision

- **Committed**: commit 804e26f2

---

**Session 849 Summary**:

Autonomous work: 1 major deliverable (Domain 20 research)

Projects Status:
- **resistance-research**: Phase 2 domain research expanded (1 of 8 high-priority Phase 2 domains COMPLETE; others: 23, 27-29, 31, 33-34 in progress from earlier sessions)
- **cybersecurity-hardening**: Phase 1 ready, all Phase 2 scenario playbooks complete (immigration, activist, financial, whistleblower, journalist, DV survivor), awaiting user distribution path decision
- **stockbot**: 2-session Jetson deployment active, May 12 Gate 1 checkpoint 6 days away, 7 architecture decisions pending user review
- **mfg-farm**: Test print required (user action); supplier research COMPLETE from earlier sessions
- **seedwarden**: Phase 1 upload pending tag corrections; Phase 2 production-ready (Track B), no blockers
- **open-repo**: PR #1 open awaiting external review/merge
- **off-grid-living**: Publication complete; social media distribution awaiting user
- **workout**: Comprehensive plan complete; user review pending

Exploration Queue Status:
- Previous items: 1 completed, 1 in progress (pending user decision), 1 blocked (test print)
- New items added this session: 3 (Journalist deep dive adjusted — already complete from Session 844; Domain 20 research — COMPLETED; Medicinal herbs strategy — pending)
- Queue maintenance: Kept backlog current with executable items

Key Metrics:
- **Autonomous work this session**: 1 major deliverable (5,700-word domain document)
- **Phase 2 progress**: resistance-research now has 1 additional high-priority domain; cybersecurity-hardening fully prepared for Phase 2 distribution
- **Next checkpoint**: May 12 stockbot Gate 1 formal evaluation
