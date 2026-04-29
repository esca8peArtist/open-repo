# Orchestrator State
> Auto-generated at 2026-04-29T04:15:26Z — do not edit. Source: PROJECTS.md, WORKLOG.md, BLOCKED.md, INBOX.md.

## Usage
🟢 Usage: Sonnet 0.5% (48,020 tokens) | All-models 33.2% | Reset in 140h | check: claude.ai → Settings → Usage & billing

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
**Status**: Active — **Feature count bug FIXED (Session 560), ready for market open 2026-04-28 09:30 ET** — awaiting user engine restart
**Focus**: **Session 560 FIX COMPLETE**. Feature count mismatch resolved. Root cause: Ensemble stackers expect 61 features with `1d_` prefix from MTF extractor + PipelineIntegrator. Previous fallback logic called `FeatureEngineer.transform()` which produces different feature names, causing shape mismatch → s
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
### mfg-farm — Test print required before launch prep continues
**Date blocked**: 2026-04-12
**Context**: Business plan, CadQuery designs (modrun_rail.py, modrun_clip.py), market research, and listing copy are all complete. Orchestrator cannot proceed with launch prep until a physical test print confirms the designs are printable.
**What I need**: Run a test print of the CadQuery rail and clip designs and confirm they printed correctly.
**Verify with**: `# manual — cannot auto-verify`
**Resolution**:
---

## Inbox (unprocessed)
*(no new items)*

## Recent Log (last 40 lines of WORKLOG.md)
- Added to PROJECTS.md Exploration Queue

**Primary Work Item — Stockbot Engine Orchestration Script**:

**Deliverable**: `projects/stockbot/scripts/launch_stacker_sessions.py` (360 lines, production-ready)

**Scope**: Create wrapper script that reads `active-sessions.json` and launches all configured stacker-based trading sessions in parallel on a shared asyncio event loop.

**Key Features**:
- Reads `active-sessions.json` configuration (67 sessions loaded in test)
- Creates TradingSession instances directly with proper stacker strategy parsing ("stacker:<uuid>" format)
- Launches all sessions in parallel with graceful lifecycle management
- Supports paper/live mode selection via --mode flag
- Proper signal handling for clean shutdown (Ctrl+C)
- Comprehensive logging and error handling
- CLI args: --config PATH, --mode {paper,live}, --verbose, --dry-run

**Architecture Decision**: Direct use of TradingSession class instead of retrofitting run_live_trading.py CLI script. TradingSession already supports stacker strategies natively — script just needed to bridge the gap between JSON configuration and TradingSession instantiation.

**Testing**:
- Syntax validation: ✓ Passed (`py_compile`)
- Config loading: ✓ Loaded active-sessions.json (67 sessions)
- Session creation: ✓ Created 67 TradingSession instances without errors
- Session startup: ✓ All 67 sessions started and running on event loop
- Graceful timeout: ✓ Sessions responded to timeout signal as expected

**Usage**:
```bash
cd projects/stockbot
.venv/bin/python scripts/launch_stacker_sessions.py --config active-sessions.json --mode paper
```

**Next Steps**:
- User verifies Alpaca API credentials are valid and account has sufficient buying power
- User restarts engine with new orchestration script before next market open (2026-04-29 13:30 UTC)
- Orchestrator monitors process and verifies no 401 auth errors in logs
- Once engine running successfully, BLOCKED.md item is resolved

**Status**: Exploration item COMPLETE. Orchestration script production-ready and tested. Stockbot engine startup is now unblocked — remaining blocker is user Alpaca account verification.
