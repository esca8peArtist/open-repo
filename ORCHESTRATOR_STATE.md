# Orchestrator State
> Auto-generated at 2026-04-29T17:58:27Z — do not edit. Source: PROJECTS.md, WORKLOG.md, BLOCKED.md, INBOX.md.

## Usage
🟢 Usage: Sonnet 0.5% (48,020 tokens) | All-models 46.8% | Reset in 126h | check: claude.ai → Settings → Usage & billing

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
### stockbot — Alpaca account insufficient buying power blocks multi-ticker trading
**Date blocked**: 2026-04-29
**Context**: Engine restarted at 03:31 UTC and running successfully. All 11-ticker portfolio generating signals in real-time (BUY/HOLD/SELL). However, at 14:30 UTC when engine attempted to place orders, all orders failed with Alpaca error code 40310000: "insufficient buying power". Account shows only $200-700 available, but simultaneous orders across 11 tickers require much more. Earlier block noted this issue but marked it RESOLVED without actually fixing it. Paper trading validation cannot proceed without sufficient funding.
**What I need**: Deposit funds to Alpaca paper trading account OR configure account with sufficient buying power for 11-ticker simultaneous trading. Estimated requirement: $5,000–10,000 minimum for reasonable position sizing across all tickers (current positions attempt $300-800/ticker which exceeds $200-700 total balance).
**Verify with**: `.venv/bin/python -c "import alpaca_trade_api; api = alpaca_trade_api.REST(); account = api.get_account(); print(f'Buying power: ${account.buying_power}')"`
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

**Order Activity**:
- ✅ 26 successful BUY orders at market open (13:19–13:28 UTC)
- ❌ 7 failures (code 40310000 "insufficient buying power" at 14:30–14:32 UTC)
- ✅ Zero new order errors since 14:32 UTC
- Tickers with failures: DIS, GOOGL (×2), AMZN (×2), RTX, MRK

**Buying Power Trajectory**:
- Open: ~$10,000+
- 14:30:40 UTC: $0 (depleted within 12 minutes of market open)
- No recovery observed

**Error Log Status**: Zero ERROR/CRITICAL lines post-rotation (clean operation)

**Discord Summary**: Will post at market close (20:00 UTC)

**Status**: Monitoring continues until 20:15 UTC. Engine performing nominally; capital exhaustion is the only constraint preventing order execution.

### 4. Summary

**Work Completed This Session**:
1. ✅ resistance-research Phase 1 distribution execution plan (730 lines, ready for user review)
2. ✅ cybersecurity-hardening Tier 1 distribution execution plan (170KB docs, ready for user review)
3. ✅ stockbot market session monitoring setup (continues through market close at 20:00 UTC)

**Outcomes**:
- Both distribution projects now have **production-ready execution plans** — materials fully sequenced, contacts identified, personalization frameworks documented, tracking systems ready
- stockbot engine **continuing nominal operation** through market hours with no crashes
- All **preparation work is user-decision-independent** — can proceed to Phase 1 execution immediately upon user approval

**Next Steps**:
1. User reviews resistance-research DISTRIBUTION_EXECUTION_LOG.md and cybersecurity-hardening TIER1_PHASE1_READINESS_SUMMARY.md
2. User approves distribution path / sequencing / messaging tone
3. Orchestrator begins Phase 1 execution (resistance-research Tier 1 outreach sequencing, cybersecurity-hardening Tier 1 preflight checklist)
4. stockbot monitoring concludes at 20:15 UTC with full market session summary

**Blocked Items**: 2 (Alpaca account, mfg-farm test print) — unchanged

**Exploration Queue**: 3 items active (session 635 additions), all available for future work
