# Orchestrator State
> Auto-generated at 2026-05-05T15:28:49Z — do not edit. Source: PROJECTS.md, WORKLOG.md, BLOCKED.md, INBOX.md.

## Usage
🟢 Usage: Sonnet 1.8% (161,414 tokens) | All-models 18.9% | Reset in 152h | check: claude.ai → Settings → Usage & billing

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
   - Selected to maximize token budget utilization while awaiting user signals

**Next Steps**:
   - Assess remaining unblocked queue items (Item 48, 49, or others)
   - Market close at 20:00 UTC; can continue research work until then
   - Prepare check-in once all available autonomous work exhausted or time constraints hit

---

## 2026-05-05 15:30+ UTC — Item 48: Resistance-Research Phase 2 Domain Prioritization Framework

✅ **Item 48: Phase 2 Candidate Comparison & Execution Roadmap** — Decision framework for Domains 38-40 prioritization
   - Agent research execution on unblocked queue item (independent of Phase 1 path decision)
   - Three documents created to `projects/resistance-research/`:
   - **phase-2-domain-prioritization-matrix.md** (3,200 words)
     - Eight-criterion scoring matrix: urgency, coalition strength, research complexity, policy window, litigation vector, media narrative gap, implementation difficulty, reversibility
     - Weighted scoring: urgency 1.5x, litigation vector 1.4x, reversibility 1.3x, others 1.0-1.2x
     - Final tier ranking: Tier 1 (87-82 score) has 4 top candidates, Tier 2 (78-75) has 5 candidates
   - **domain-38-40-strategic-analysis.md** (4,100 words)
     - Top candidates detailed: Disability Rights (41-B, 87.1, fastest research 10-14h, highest narrative gap), Voting Systems (38-B, 84.1, elevated post-Callais SCOTUS ruling April 29), Intel Oversight (38-A, 81.6, June 12 FISA deadline is hard constraint), Tribal Sovereignty (40-B, 78.8, triggered by Trump v. Barbara ruling)
     - Policy window analysis per candidate (when do action windows close?)
     - Coalition alignment mapping to existing Phase 1 Tier 1 contacts
   - **phase-2-execution-roadmap.md** (2,100 words)
     - Sequential vs. parallel vs. hybrid execution options
     - **Critical finding**: June 12 FISA deadline + November 3 midterm are concurrent constraints that sequential execution cannot serve
     - **Recommended architecture**: Track A (Voting Systems → Repro Rights → Labor → Fiscal Authority sequential) + Track B (Intel Oversight + Tribal Sovereignty parallel) — enables both June deadline (Intel) and midterm prep (Voting Systems)
     - Resource allocation and decision gates
     - Timeline with Month 1-12 Phase 2 execution calendar
   - **Total additions**: 9,400 words of Phase 2 prioritization framework

**Key Strategic Insight**:
   - Item 12 (Domain 38 candidates) was completed before Callais SCOTUS ruling (April 29, 2026 striking down VRA Section 2 discriminatory-effects standard)
   - Callais elevated Voting Systems from Tier 2 to Tier 2 candidate in priority rank (84.1 score)
   - FISA 45-day extension (not multi-year reauth) compressed June 12 deadline window
   - Item 48 synthesis integrates April-May 2026 developments that shift Phase 2 prioritization

**Combined Session Output** (Items 47-48):
   - Total: 25,327 words across 7 documents (4 workout + 3 resistance-research)
   - Both items cleared from Exploration Queue
   - Workout Phase 2 ready for user review; Phase 2 prioritization framework ready for strategic Phase 1→Phase 2 transition planning
