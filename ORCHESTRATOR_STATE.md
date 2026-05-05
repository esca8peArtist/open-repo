# Orchestrator State
> Auto-generated at 2026-05-05T19:13:52Z — do not edit. Source: PROJECTS.md, WORKLOG.md, BLOCKED.md, INBOX.md.

## Usage
🟢 Usage: Sonnet 1.8% (161,414 tokens) | All-models 23.3% | Reset in 149h | check: claude.ai → Settings → Usage & billing

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
### stockbot — May 5 Engine crashed; 67-session config still active, DTBP=0 blocks all trading
**Date blocked**: 2026-05-05 14:47 UTC
**Context**: May 5 market open planned 19 position CLOSE orders + 2-session architecture reduction (67→2 AAPL sessions). Engine never executed closures. At 14:46-14:47 UTC, engine attempted BUY orders on all 67 tickers (LIN, HON, MRK, etc.) but all failed with code 40310000 "insufficient day trading buying power" (DTBP=0 due to Apr 29-May 4 margin call). Error log shows BUY attempts on 17 tickers failing sequentially. Engine is not currently running (ps aux shows no process). 19 positions remain OPEN: INTC, MRK, AMZN, WMT, CAT, COST, UNH, CVX, DIS, RTX, NEE, COP, HON, MA, SHW, PG, LIN, FDX, GOOGL. AAPL 108 shares held (correct). Root cause: active-sessions.json still contains 67-session configuration (from May 4 plan to reduce to 2); reduction was never implemented.
**What I need**: (1) User restarts engine after DTBP reset tomorrow (May 6 13:30 UTC). (2) Before restart, replace active-sessions.json with active-sessions-2session.json (contains only AAPL lgbm_ho + AAPL ridge_wf). (3) Verify engine starts cleanly with 2 sessions only.

## Inbox (unprocessed)
*(no new items)*

## Recent Log (last 40 lines of WORKLOG.md)

**Actions Taken**:
- Created corrected 2-session config file: `active-sessions-2session.json` (contains only AAPL lgbm_ho + AAPL ridge_wf)
- Added new BLOCKED.md entry with root cause, recovery steps, and verification command
- Attempted Discord notification (webhook URL not available in local .env; notification failed silently)

**Current State**:
- 19 positions remain OPEN: INTC, MRK, AMZN, WMT, CAT, COST, UNH, CVX, DIS, RTX, NEE, COP, HON, MA, SHW, PG, LIN, FDX, GOOGL
- AAPL 108 shares held (correct, per plan)
- DTBP=0 expected to reset May 6 13:30 UTC market open
- Engine crash prevents any new trading until restart (cannot trade with DTBP=0 anyway)

**User Action Required** (post-DTBP-reset May 6):
1. Replace `active-sessions.json` with `active-sessions-2session.json`
2. Restart engine: `cd projects/stockbot && .venv/bin/python scripts/launch_stacker_sessions.py --config active-sessions.json --mode paper`
3. Verify 2 sessions start (AAPL lgbm_ho + AAPL ridge_wf) only

**Next Checkpoint**: May 6 13:30 UTC market open — verify DTBP reset to ~$400K and engine can execute trades

✅ **Item 14: cybersecurity-hardening Step-by-Step Implementation Guides** — Session 752 (16:20 UTC)
   - Agent research execution on unblocked queue item (independent of distribution)
   - All 6 implementation guides created to `projects/cybersecurity-hardening/`:
   - **encrypted-messaging-implementation-guide.md** (2,980 words) — Signal/Matrix/Briar verification workflows, NSA QR malware attack warning, account isolation strategies
   - **vpn-and-network-hardening-guide.md** (2,009 words) — Five/Nine/Fourteen Eyes jurisdictional analysis, Mullvad/Proton audit verification, WireGuard cipher suite explained, kill switch verification steps
   - **tor-and-anonymity-guide.md** (1,838 words) — GPG signature verification pre-installation, guard relay pinning (predecessor attack prevention), obfs4/Snowflake bridge config, stream isolation, circuit correlation NSA risk assessment
   - **device-hardening-implementation-guide.md** (2,422 words) — macOS (FileVault, pf firewall rules), Linux (UFW default-deny, AppArmor, sysctl hardening), Windows (BitLocker, WDAC vs AppLocker), Firefox hardening (uBlock Origin, resistFingerprinting, WebRTC disable)
   - **operational-security-workflows-guide.md** (2,042 words) — Compartmentalization models (2-layer vs 3-layer), VirtualBox VM isolation, Whonix routing, metadata removal (mat2, exiftool), digital dead-drop techniques, two full scenarios (journalist/protest, activist/repressive country) with decision trees
   - **identity-recovery-and-breach-response-guide.md** (2,080 words) — Hour-by-hour playbook, MFA hierarchy (hardware key > TOTP > email > SMS), contact notification template, SIM-swap risk, Aegis TOTP setup, Signal Registration Lock recovery
   - **Total additions**: 13,371 words across 6 guides
   - **Quality features**: Verified sources (EFF, Tor Project, Signal, Mullvad audits, CISA), OS-specific code blocks (ready-to-copy), clear threat models per persona, danger warnings where users could accidentally weaken security

**Strategic Value**: Cybersecurity-hardening project now complete end-to-end: (1) distribution infrastructure (Tier 1-3 templates + messaging), (2) comprehensive OpSec playbook (existing), (3) immediately actionable implementation guides (NEW). Users receiving outreach can execute guides immediately without external dependencies. Guides address common pitfalls (QR code attacks, tab correlation, SIM-swap) that many users are unaware of.

**Next Steps**:
- Guides ready for integration into Tier 1 outreach templates (user review recommended)
- Optional: Create video tutorials or interactive decision trees for visual learners
- Optional: Build community forum/wiki for peer support on guide execution

---
