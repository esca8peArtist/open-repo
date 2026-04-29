# Orchestrator State
> Auto-generated at 2026-04-29T10:15:47Z — do not edit. Source: PROJECTS.md, WORKLOG.md, BLOCKED.md, INBOX.md.

## Usage
🟢 Usage: Sonnet 0.5% (48,020 tokens) | All-models 38.2% | Reset in 134h | check: claude.ai → Settings → Usage & billing

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
     - Time decay model aligned to h=10 hold horizon
     - Portfolio Greeks aggregator (net delta/Vega/theta)
  4. **Phased Implementation**:
     - Phase 1 (May-Aug 2026): Infrastructure build concurrent with equity paper trading
     - Phase 2 (Sep-Nov 2026): Options paper trading post-Gate-2
     - Phase 3 (Dec 2026+): Live options after 60+ days paper trading
  5. **Integration Architecture**:
     - Ensemble signal upstream (no standalone options trades)
     - Covered calls layer on top of equity positions
     - StrategyCoordinator extension to track options leg alongside equity leg
     - Avoids double-entry when covered call written against position

**Status**: Committed to stockbot submodule (commit 803d9ec). Production-ready for review. Feeds into post-Gate-1 roadmap.

### Market Session Preparation (Today 13:30 UTC)
- **Critical Observation**: April 29 is the first live market session since engine restart on 03:31 UTC
- **Expected Activity**:
  - 11-ticker portfolio (AAPL, GOOGL, NVDA, AMZN, META, JPM, XOM, JNJ, UNH, TSLA + 1 other)
  - Each ticker running h=10 LGBM ensemble stacker (180-day backtest baseline: ~0.17-2 trades/month/ticker = ~2-22 trades/month aggregate)
  - HMM regime scaling enabled (adaptive position sizing based on market regime)
  - Market-aware sleep logic: when market closes at 20:00 UTC, engine sleeps until 13:15 UTC next day
- **Monitoring Checklist**:
  - ✅ Engine running pre-market (verified 08:07 UTC)
  - ⏳ Engine cycle execution during 13:30-20:00 UTC trading hours
  - ⏳ Signal generation per ticker (currently all tickers producing 0.0 predicted return?)
  - ⏳ Order submission to Alpaca paper trading account
  - ⏳ Fill confirmation + position table updates
  - ⏳ Discord notification at market close (20:00 UTC) with: signals/ticker, orders placed/filled, total trades, mode, strategy
- **Key Question**: Will multi-ticker portfolio generate ≥1 trade today? Current rate (0.17-2/month/ticker) suggests ~10-15% chance per single day. 11-ticker portfolio → ~60% ensemble chance of at least 1 signal across all tickers today.

**Next Steps**: 
1. **14:00 UTC** (1h into market): Verify engine is cycling and generating signals
2. **16:00 UTC** (during market): Check logs for order submissions
3. **20:15 UTC** (post-market close): Verify Discord summary posted; record round trip count
4. **May 1 Checkpoint**: After 2-3 market sessions, assess whether signal generation thresholds need adjustment

**Blocked on**: Nothing. Engine ready. Paper trading validation in progress. No autonomous work pending.

**Status**: SESSION IN PROGRESS
