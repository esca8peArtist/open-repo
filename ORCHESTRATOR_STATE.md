# Orchestrator State
> Auto-generated at 2026-04-28T20:52:02Z — do not edit. Source: PROJECTS.md, WORKLOG.md, BLOCKED.md, INBOX.md.

## Usage
🟢 Usage: Sonnet 0.0% (0 tokens) | All-models 24.0% | Reset in 147h | check: claude.ai → Settings → Usage & billing

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
### stockbot — Engine did not run during market hours; Alpaca account configuration TBD
**Date blocked**: 2026-04-28
**Context**: ORCHESTRATOR_STATE.md reported engine running at 15:05 UTC, but verification (Session 596) shows: (1) Engine was NOT running during market hours 13:30–20:00 UTC on 2026-04-28. (2) Last log activity 08:36 UTC (before market open at 13:30 UTC); engine shut down cleanly with user request. (3) Database unchanged since 2026-04-27 15:12 UTC (no trading occurred today). (4) Background: Session 595 identified Alpaca paper trading account has zero day-trading buying power — order submissions fail with error code 40310000: "insufficient day trading buying power". Root cause is either unfunded account or margin account misconfiguration.
**Investigation (Session 596)**: 
- Log file `/home/awank/dev/SuperClaude_Framework/projects/stockbot/logs/live_trading_20260428.log` (422 KB, modified 09:47 UTC)
- Timestamps show engine started ~00:26 UTC, shut down repeatedly 00:27–08:36 UTC with USER_REQUEST/UNKNOWN reasons
- No market hours activity (13:30–20:00 UTC) in logs
- No process running: `ps aux | grep trading` returns empty
- Database (stockbot.db): last modified 2026-04-27 15:12 UTC, zero April 28 trades
**What I need**:
1. **Immediate** (before next market session): Restart engine and confirm operation during market hours
2. **Before restart**: Verify Alpaca account configuration:
   - Log in to https://app.alpaca.markets/ → "Paper Trading" tab
   - Check **Account Type**: Must be "CASH" (not "MARGIN")
   - Check **Account Balance**: Should show > $0 (Alpaca default $25,000 for new paper accounts)
   - If issues: Reset account or contact Alpaca support
3. **After restart**: Monitor logs for first successful FILL (should appear within 5 minutes if account is configured)
**Verify with**: `tail -20 /home/awank/dev/SuperClaude_Framework/projects/stockbot/logs/live_trading_*.log | grep -i "fill\|execution" | head -1` — if successful order fill appears, account is operational
**Resolution**:
---
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

**Work Completed** — stockbot Signal Threshold Analysis:

**Deliverable**: `projects/stockbot/signal-threshold-analysis.md` (2,400 words, production-ready)

**Scope**:
- Analyzed current signal mechanism (volatility-adaptive threshold in `ensemble_stacker.py`)
- Formula: `threshold = max(rolling_std * threshold_multiplier, 0.002)`
- Current config: threshold_multiplier=0.5 → ~0.60–0.75% effective threshold
- **Root cause of Gate 1 failure**: Current threshold requires ~2.28% return prediction (2.28/0.75≈3x rolling std) → extremely conservative → only ~1 trade per 180 days

**Key Findings**:
1. **Signal Frequency Bottleneck**: Current threshold generates 0.17 trades/month per ticker (AAPL single-ticker); need 30/month for Gate 1
2. **Multi-ticker Path**: 11 tickers at current threshold → ~1.9 trades/month (still 15x short of Gate 1)
3. **Optimization Lever**: Reducing threshold_multiplier from 0.5 to 0.40 → 1.5–2× signal frequency increase
4. **Expected Outcome**: 11 tickers at 0.40 threshold → 3–5 trades/month per stacker → 30–55 trades/month portfolio (exceeds Gate 1)

**Recommendations**:
- **Option A (Conservative, Recommended)**: threshold_multiplier 0.50 → 0.40 (20% reduction)
  - Expected: Gate 1 achievement within 2 weeks of paper trading at 11-ticker portfolio
  - Risk: Low (meta-learner confidence filtering already active)
  
- **Option B (Aggressive, If Needed)**: threshold_multiplier 0.50 → 0.30 (40% reduction)
  - Expected: Gate 1 achievement within 1 week
  - Risk: Medium–High (may increase false positives, reduce Sharpe)

**Implementation Sequence**:
1. Validate Option A (0.40) via backtest (Session 608)
2. Deploy to 11-ticker paper trading (after engine restart)
3. Daily monitoring via `paper_trading_monitor.py`
4. Gate 1 pass/fail decision on May 12 checkpoint

**Next Steps**:
- User reviews signal-threshold-analysis.md
- Orchestrator awaits engine restart (user action, CRITICAL)
- Once engine running: Apply threshold_multiplier=0.40 to active-sessions.json
- Monitor paper trading daily; expect Gate 1 achievement by May 10–12

**Status**: Exploration item COMPLETE. Analysis ready for user review and backtest validation.
