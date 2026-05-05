# Orchestrator State
> Auto-generated at 2026-05-04T23:59:59Z — do not edit. Source: PROJECTS.md, WORKLOG.md, BLOCKED.md, INBOX.md.

## Usage
🟡 Usage: Sonnet 6.5% (578,830 tokens) | All-models 83.1% | Reset in -0h | check: claude.ai → Settings → Usage & billing

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
**Focus**: **Phase 2 Track B production pipeline COMPLETE (Session 714)**. Production pipeline fully built and ready for user action:
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
- `a1b2c3d4e5f60001` — AAPL_h10_ridge_wf (stacker `32643264`)

19 non-AAPL positions (INTC, MRK, AMZN, WMT, CAT, COST, UNH, CVX, DIS, RTX, NEE, COP, HON, MA,
SHW, PG, LIN, FDX, GOOGL) closed via Alpaca market orders tonight. These execute at 13:30 UTC
May 5 (market open). AAPL position (108 shares, ~$29.8K, +$924 unrealized) stays open.

Account state going into May 5: Cash -$310K (paper artifact), buying_power ~$0, long $420K.
After 19 closes, buying_power is expected to return to positive.

### Fixes Deployed

**Fix 1 — active-sessions.json seed**: Jetson DB re-seeded from `active-sessions.json` to reflect
the 2-session-only state. Prior DB state referenced 67 sessions that no longer exist on the Jetson.
This was necessary to prevent the engine from attempting to load missing session configs on startup.

**Fix 2 — /api/ready endpoint**: Endpoint verified returning correct session count (sessions:2).
This endpoint is the canonical health check for the Jetson deployment. Pre-market check at 13:00
UTC each day should ping this endpoint and confirm sessions:2 before market open.

### Gate 1 Revised Assessment

The original Gate 1 target (150 fills by May 12) was calibrated for 67 sessions at ~12.6
fills/trading-day. With 2 AAPL sessions, the maximum possible fill rate is 2/day and the realistic
rate is 0–2/day (signals fire only when threshold is crossed). The 150-fill target is structurally
unreachable in the 2-session architecture.

**Gate 1 — RETIRED** for the prior 67-session architecture.

**Gate 1b — ACTIVE** (2-session architecture):
- Minimum 5 completed round trips across both AAPL sessions within 30 days of May 5
- All fills must have fill_price > 0 and fill_time within market hours
- Both sessions alive on every market open through June 4
- 0 sustained auth errors during market hours
- Deadline: June 4, 2026
- Estimated pass probability: ~80%

Full analysis: `projects/stockbot/GATE_1_REVISED_2SESSION.md`  
May 5 monitoring plan: `projects/stockbot/MAY_5_MONITORING_CHECKLIST.md`

**Remaining session time**: ~10 hours until market open (13:30 UTC); prioritize stockbot monitoring and market readiness
