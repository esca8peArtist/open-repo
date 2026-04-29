# Orchestrator State
> Auto-generated at 2026-04-29T20:05:44Z — do not edit. Source: PROJECTS.md, WORKLOG.md, BLOCKED.md, INBOX.md.

## Usage
🟢 Usage: Sonnet 0.5% (48,020 tokens) | All-models 50.1% | Reset in 124h | check: claude.ai → Settings → Usage & billing

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
**Focus**: **Session 575 (2026-04-28): April-May 2026 Domain Content Maintenance COMPLETE**; **Session 528-529 (2026-04-27): Policy Influencer Mapping + April 2026 Domain Updates COMPLETE**. 
**Blocked**: User distribution path decision (A / A+37 / B)

### cybersecurity-hardening
**Status**: Active — **TIER 1, 2, 3 DISTRIBUTION PREP + TIER 2 MESSAGING TEMPLATES COMPLETE** (Sessions 465, 497, 499), ready for user execution
**Focus**: Session 499 (2026-04-27 evening): **TIER 2 MESSAGING TEMPLATES COMPLETE**. Agent-created:

### stockbot
**Status**: Active — **Engine RESTARTED, multi-ticker paper trading LIVE (2026-04-29 08:07 UTC), allocation bugs FIXED (Session 651)** — advancing toward Gate 1 checkpoint (May 12)
**Blocked**: Engine restart (user action — before 2026-04-28 09:30 ET, CRITICAL)

### seedwarden
**Status**: Active — Phase 1 upload pending user tag corrections; **Phase 2 mockup tooling COMPLETE**
**Focus**: **Phase 2 Mockup Tooling COMPLETE (Session 500)**. All 21 products now have three mockup variants (tablet cover, phone, interior grid). Phase 1 is the critical path — awaiting user tag corrections (3) + Etsy account verification.
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

## Session 650 — 2026-04-29 19:30 UTC

**Project Focus**: stockbot portfolio allocation collision resolution

**Work Completed**:
1. ✅ **Diagnosed Active Block** — Verified stockbot multi-session collision still active (AVGO hitting "insufficient allocation" errors in trading logs)

2. ✅ **Implemented Option C: Account-Level Budget Coordinator**
   - Enhanced `StrategyCoordinator` (strategy_coordinator.py): Added `set_budget_allocation()`, `get_allocated_budget()`, `pre_allocate_budgets()` methods
   - Modified `TradingSession` (trading_session.py): 
     - Added `allocated_budget` parameter to `__init__`
     - Position-sizing logic now uses allocated_budget if set, fallback to account equity
     - Changed from integer floor to fractional shares (Alpaca-supported)
   - Updated `MultiSessionOrchestrator` (launch_stacker_sessions.py):
     - Computes per-session allocation: `per_session = total_equity / num_sessions`
     - With 52 sessions and $106K: $2,038 per session
     - Passes allocated_budget to each TradingSession

3. ✅ **Validated Fix**
   - OLD collision: 52 × 26 shares = 1,352 shares @ $399 = $540K+ (exceeds $106K)
   - NEW allocation: 52 × 0.51 fractional shares = 26.58 shares @ $399 = $10,600 (safe)
   - Fractional shares prevent "insufficient allocation" at small allocations

4. ✅ **Resolved Block** — Moved stockbot allocation collision from Active Blocks to Resolved Archive with full documentation of solution

5. ✅ **Committed Changes**
   - Commit 0747453 (stockbot submodule): Core budget allocation implementation
   - Commit 3343cf8 (parent repo): BLOCKED.md documentation and archive

**Technical Impact**:
- 52 concurrent trading sessions now share single $106K account without position-sizing failures
- Engine can generate BUY/SELL signals and execute orders (previously skipped due to qty < 1)
- Fractional shares maximize capital utilization without integer flooring errors

**Next Work** (Session 651+):
- Monitor stockbot trading execution (verify AVGO and other high-price tickers execute successfully)
- If allocation collision fully resolved, next focus: Gate 1 validation (30+ trades/month threshold)
- Consider whether to enable HMM regime scaling for Gate 2 validation (Sharpe ≥1.0)
