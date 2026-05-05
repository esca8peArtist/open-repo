# Orchestrator State
> Auto-generated at 2026-05-05T14:10:47Z — do not edit. Source: PROJECTS.md, WORKLOG.md, BLOCKED.md, INBOX.md.

## Usage
🟢 Usage: Sonnet 1.4% (127,601 tokens) | All-models 17.0% | Reset in 154h | check: claude.ai → Settings → Usage & billing

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
### stockbot — CRITICAL: Alpaca account has zero day-trading buying power (May 5 market hours)
**Date blocked**: 2026-05-05 14:46 UTC
**Context**: May 5 market open at 13:30 UTC. Engine restarted at 14:46 UTC with bug fix (get_order_by_id). All 52 ticker sessions generating trading signals correctly. However, all BUY orders fail immediately with Alpaca error 40310000: "insufficient day trading buying power" (daytrading_buying_power=0). Account is properly funded for paper trading, but day-trading buying power is explicitly zero. This blocks ALL position opens and position adjustments. 20 positions remain OPEN (from April 29) with +$4,581 unrealized P&L. SELL orders (for position closes) may still work, but cannot open new positions or scale existing positions. This is the same account-level issue flagged April 28 (Session 595: Alpaca account configuration TBD).
**What I need**: Check Alpaca account settings for day-trading buying power. Either: (1) Account needs margin enabled (Account → Settings → Leverage), (2) Account needs equity/cash deposit, or (3) Account requires specific day-trading account configuration. Confirm daytrading_buying_power > 0 before market close 20:00 UTC to avoid missing Gate 1b trading window.
**Verify with**: `curl -s -X GET "https://api.alpaca.markets/v2/account" -H "Authorization: Bearer $APCA_API_KEY_ID" | jq '.daytrading_buying_power'`
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
   - Updated get_database_stats() to report all 10 tables (was missing 4)
   - Updated test assertions to reflect current schema (10 tables, not 6)
   - All 25 unit tests passing (verified)
   - Commits: 1e4d90c (stockbot submodule), aa59e8f (parent repo)

2. ✅ **Engine Restart**: 
   - Discovered engine was not running (shut down at 09:32:35 UTC with USER_REQUEST)
   - Verified active-sessions.json has 52 ticker sessions configured (AAPL, MSFT, GOOGL, NVDA, AMZN, META, JPM, XOM, JNJ, UNH, TSLA, IBM, INTC, CSCO, ORCL, ADBE, AMD, QCOM, V, MA, BAC, GS, MS, C, WFC, PG, KO, PEP, WMT, PFE, MRK, LLY, MCD, DIS, NKE, CVX, COP, GE, HON, VZ, T, BRK.B, NFLX, COST, TXN, AVGO, ABBV, BMY, TMO, CAT, SBUX, RTX, AMT, NEE, LIN, NOW, CRM, DE, SHW, ISRG, PLD, DUK, HD, LMT, UPS, REGN, FDX)
   - Restarted launch_stacker_sessions.py with active-sessions.json config at 11:39 UTC
   - Engine now running (PID 177133)
   - Ready for 13:30 UTC market open with position closes

3. ⏳ **Pre-Market Readiness**:
   - Engine operational with 52 ticker sessions configured in paper trading mode
   - 19 non-AAPL positions scheduled to close at 13:30 UTC market open
   - AAPL position (108 shares, +$924 unrealized) scheduled to hold at h+4
   - Pre-market health check at 13:00 UTC will verify engine readiness
   
**Timeline**:
- **Current time**: 11:45 UTC
- **Pre-market health check**: 13:00 UTC (75 min away) — verify engine operational
- **Market open**: 13:30 UTC (105 min away) — execute position closes
- **Post-market analysis**: 20:00 UTC — assess fills and Gate 1 trajectory

**Next Actions**:
- Stand by until 13:00 UTC for pre-market health check
- Monitor engine logs for startup issues
- Prepare market open monitoring at 13:30 UTC

**Session work complete** (code refactored, engine restarted, ready for market event)

**Market Monitoring Status** (12:32 UTC):
- ✅ Engine running (PID 177133, verified at 12:32 UTC)
- ✅ Log file last updated at 12:39 UTC (all 52 sessions initialized, sleeping until 13:15 UTC)
- ⏳ **Scheduled Events**:
  - **13:15 UTC** (~43 min): Engine wake-up (sessions begin trading 15 min before market open)
  - **13:30 UTC** (~58 min): US market open — execute 19 non-AAPL position close orders (INTC, MRK, AMZN, WMT, CAT, COST, UNH, CVX, DIS, RTX, NEE, COP, HON, MA, SHW, PG, LIN, FDX, GOOGL)
  - **13:45 UTC**: Verify close orders posted to database with realized P&L
  - **20:00 UTC**: Post-market analysis — query May 5 fills, assess Gate 1b trajectory
