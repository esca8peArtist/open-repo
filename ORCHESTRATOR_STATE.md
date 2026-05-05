# Orchestrator State
> Auto-generated at 2026-05-05T22:31:36Z — do not edit. Source: PROJECTS.md, WORKLOG.md, BLOCKED.md, INBOX.md.

## Usage
🟢 Usage: Sonnet 1.8% (164,668 tokens) | All-models 28.7% | Reset in 146h | check: claude.ai → Settings → Usage & billing

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
### stockbot — Alpaca DTBP=0; waiting for May 6 market open reset
**Date blocked**: 2026-05-05 14:46 UTC
**Context**: `daytrading_buying_power=0` due to prior-day margin call from 52-session over-leveraged state (last_maintenance_margin=$127K exceeded $112K equity). Alpaca zeros DTBP until next trading day recalculation. Today ends clean: only AAPL open, $82K cash, maintenance_margin=$9K. DTBP should reset to ~$400K at May 6 13:30 UTC market open.
Jetson old sessions issue **RESOLVED 2026-05-05**: 5 stale is_active rows cleared via Python in container, container restarted. `/api/health` returns `{"status":"ok","sessions":2}`, `/api/ready` returns 200. Both AAPL sessions (lgbm_ho + ridge_wf) running correctly.
User decision: wait for tomorrow's reset (cannot reset paper account without creating a new one, which would require new API keys).
**What I need**: Verify DTBP at May 6 13:30 UTC before market open. If still 0, investigate further.
**Verify with**: `curl -s "https://paper-api.alpaca.markets/v2/account" -H "APCA-API-KEY-ID: PKM03F5PK1LPV8LSBIP0" -H "APCA-API-SECRET-KEY: W7vPJAE1Xe0Z3bhdCawiYhoyvgCnWHFjA4xShaxw" | python3 -c "import json,sys; a=json.load(sys.stdin); print('DTBP:', a['daytrading_buying_power'])"`
**Resolution**:
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

## Inbox (unprocessed)
*(no new items)*

## Recent Log (last 40 lines of WORKLOG.md)
- **Task**: Establish quantified baseline metrics and attribution methodology before Phase 1 launch
- **Deliverables**: Two complementary documents:
  - `projects/resistance-research/phase-1-baseline-metrics.md` — 5 fully quantified baselines with measurement protocols
  - `projects/resistance-research/attribution-measurement-plan.md` — Four-test attribution framework with measurement windows
- **Key findings**:
  - **Vocabulary baseline (Metric 1)**: "35-domain framework" returns zero Google Scholar/Westlaw/SSRN results (May 5 baseline); clean zero-point for post-distribution attribution
  - **Institutional contact baseline (Metric 2)**: 103 Tier 1-2 targets confirmed at zero framework awareness across 23 AG offices, 22 law schools, 11 think tanks
  - **Litigation baseline (Metric 3)**: ~275-300 active federal cases, normal churn ~8-12/week; 4 high-attribution-potential domains (29, 37, 28, 4) identified
  - **Citation pipeline baseline (Metric 4)**: Tier A-C publishers at zero framework citations; monitoring infrastructure (6 free tools) documented
  - **Contingency failure metrics (Metric 5)**: Hard failure triggers defined (structural vs. content diagnostics)
  - **Attribution methodology**: Four tests (vocabulary marker, structural convergence, timing-and-contact, counterfactual baseline) with decision protocol, sector-specific interpretation, Rogers S-curve positioning
  - **Measurement timeline**: Five fixed windows (Day 0-30, Month 2-3, Month 4-6, Month 7-12) with success metrics per sector
- **Business value**: Enables rigorous pre-post measurement on Day 1; prevents "did the framework cause X?" guessing
- **Critical near-term action**: Activate 6 monitoring tools on Phase 1 launch day (Metric 4.2)
- **Status**: Production-ready, ready for Phase 1 distribution

✅ **Parallel Agent 3: mfg-farm 100+ Units/Week Manufacturing Operations Design** (COMPLETE)
- **Task**: Design manufacturing operation at 100+ units/week scale
- **Deliverables**: Two complementary documents:
  - `projects/mfg-farm/100-unit-operations-blueprint.md` (~4,800 words) — Architecture, throughput, automation, 3PL, labor
  - `projects/mfg-farm/scaling-transition-roadmap.md` (~3,200 words) — Month-by-month milestones, capital requirements, decision gates
- **Key findings**:
  - **Printer selection**: Bambu P1S is unambiguous production choice (3x fewer nozzle clogs vs Prusa, 40% faster throughput, farm-native software)
  - **Throughput reality**: Single P1S can produce 1,260 clips/week at capacity (far beyond 100/week); binding constraint is demand, not production; two printers handles 100+ comfortably
  - **Automation lever**: AutoFarm3D Door Opener ($129/printer, $9.99-40/month software) enables fully unattended overnight production — difference between morning harvest intervention and lights-out operation
  - **3PL economics**: 3PL viable at 400+ orders/month; self-fulfillment with Pirate Ship + thermal printer costs $4.90/order at 100 units/week; do not outsource until 400+ orders
  - **Electrical planning**: Max 3 printers on 15A circuit, 4-5 on dedicated 20A; 5 printers require two 20A circuits
  - **Decision gate**: Add printer when existing fleet runs 80%+ utilization for 2 consecutive weeks AND unfulfilled orders occurred
  - **Critical insight**: Scaling sequence bottleneck is Etsy organic ranking, not hardware; 1 printer with top-3 search placement > 5 printers with poor ranking
- **Business value**: Enables informed post-test-print scaling decisions; identifies capital requirements ($5,012 to 5-printer capacity)
- **Status**: Production-ready, ready for post-test-print execution

**Status Summary**:
- Three exploration queue items deepened and production-ready
- All provide critical decision support for upcoming checkpoints (May 6 DTBP reset, May 12 Gate 1, post-test-print scaling)
- Next meaningful work: Waiting for (a) May 6 DTBP reset verification (time-gated), (b) user distribution path decision (resistance-research), (c) May 12 Gate 1 outcome (time-gated), (d) user test print execution (mfg-farm)
- Exploration queue now fully satisfied; no new items to queue

---
