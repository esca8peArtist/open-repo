# Orchestrator State
> Auto-generated at 2026-05-06T21:14:11Z — do not edit. Source: PROJECTS.md, WORKLOG.md, BLOCKED.md, INBOX.md.

## Usage
🟢 Usage: Sonnet 2.2% (194,281 tokens) | All-models 56.3% | Reset in 123h | check: claude.ai → Settings → Usage & billing

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
**Focus**: **Session 837 (2026-05-06): May 2026 Domain Maintenance COMPLETE; Phase 1 Domains Current + Ready for Distribution**. Three domains updated with FISA 702 final outcome and Callais redistricting cascade. Framework 100% ready for Phase 1 execution.
**Blocked**: User distribution path decision (A / A+37 / B)

### cybersecurity-hardening
**Status**: Active — **TIER 1, 2, 3 DISTRIBUTION PREP + TIER 2 MESSAGING TEMPLATES COMPLETE** (Sessions 465, 497, 499), ready for user execution
**Focus**: **Session 837 (2026-05-06): Phase 2 Sequencing Strategy COMPLETE**. Updated threat model identifies 5 capability gaps; advanced protection playbooks designed; 12-month Phase 2 roadmap complete. Three urgent pre-launch flags identified for Phase 1.

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
**Verify with**: `# manual — cannot auto-verify`
**Resolution**:

## Inbox (unprocessed)
*(no new items)*

## Recent Log (last 40 lines of WORKLOG.md)
✅ **resistance-research: Feedback Integration & Amendment Protocol** (~1.5 hours)
- **Output**: `feedback-integration-protocol.md` (3,100 words, production-ready)
- **Problem solved**: Framework is about to be distributed to 100+ institutional adopters. Need a systematic protocol for incorporating feedback without breaking production integrity.
- **Key design decisions**:
  1. **Feedback taxonomy**: 5 categories (typo, interpretation, new finding, localization, out-of-scope) with decision tree
  2. **Semantic versioning**: MAJOR.MINOR.PATCH adapted for policy (not software): e.g., 1.0.0 → 1.0.1 for typo fix, 1.0.0 → 1.1.0 for new domain
  3. **Amendment process**: 6-step workflow with explicit timelines (1-2 weeks depending on type)
  4. **Governance**: Single-author authority (Anya makes final decisions); domain experts consulted for specific domains
  5. **Versioning mechanism**: GitHub releases/tags ensure permanent backward compatibility (can always cite "v1.0.0, Domain 5" and get exact text)
- **Historical precedent research**: Model Penal Code (36 states adopted selectively, shows localization is expected not a failure), ABA Model Rules (continuous updates, 50-state coverage), IETF RFC process (consensus model, different from single-author policy)
- **Business value**: Enables Phase 1 distribution to proceed with confidence that feedback will be managed systematically; prevents framework fragmentation while remaining open to improvement
- **Location**: `projects/resistance-research/feedback-integration-protocol.md` (committed)

**Exploration Queue Regenerated**:
- Discovered all prior exploration items marked COMPLETE from Session 833
- Added 3 new strategic items per orchestrator protocol (when queue < 3 items):
  1. **resistance-research: Feedback Integration & Amendment Protocol** ✅ COMPLETED THIS SESSION
  2. **cybersecurity-hardening: Organizational OpSec Playbook** (estimated 4-5 hours) — Extend Phase 2 from individual to organizational contexts (NGOs, labor unions, legal service providers)
  3. **mfg-farm: Multi-Product Supply Chain & Scaling Strategy** (estimated 2-3 hours) — Post-test-print, design supplier resilience and product diversification roadmap

**Project Status Summary**:
- **resistance-research**: Phase 1 production-ready (35 domains complete), Phase 1 distribution infrastructure now complete (feedback protocol documented), awaiting user path decision (A / A+37 / B)
- **cybersecurity-hardening**: Phase 2 scenario playbooks ALL COMPLETE (6 total: immigration + 5 others); awaiting Phase 2 distribution execution (Tier 2 launch ~4 weeks post-Tier-1)
- **stockbot**: 2-session Jetson deployment active, May 12 Gate 1 checkpoint in 6 days, 7 architecture decisions pending user review
- **mfg-farm**: Test print required (user action block); Exploration Queue item regenerated for post-test-print product diversification
- **seedwarden**: Track B production-ready (no blockers); Phase 1 upload blocked on 3 user tag corrections
- **open-repo**: PR #1 open awaiting external review/merge
- **off-grid-living**: Publication complete, social media distribution awaiting user execution

**Key Metrics**:
- **Autonomous work this session**: 1 infrastructure document (feedback integration protocol)
- **Exploration Queue**: 3 items active (1 completed, 2 pending)
- **Blocks status**: 2 active blocks unchanged (stockbot arch decisions, mfg-farm test print)
- **Next autonomous work**: cybersecurity-hardening organizational playbook (estimated 4-5 hours) or wait for user to unblock primary projects

**Technical Notes**:
- Feedback integration protocol designed to prevent the most common distributed framework failure: fragmentation (multiple incompatible versions in use). Solution: permanent version archival via GitHub releases + version-pinned citations
- Model Penal Code case study: Shows that selective adoption + localization is expected behavior for distributed frameworks, not a failure mode
- arXiv model: Permanent identifiers (v1, v2, v3) mean old citations remain valid forever even as framework evolves
