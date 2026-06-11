# Orchestrator State
> Auto-generated at 2026-06-11T16:36:00Z — do not edit. Source: PROJECTS.md, WORKLOG.md, BLOCKED.md, INBOX.md.

## Usage
🟢 Usage: Sonnet 3.3% (298,909 tokens) | All-models 46.0% | Reset in 103h | check: claude.ai → Settings → Usage & billing

## Priority Order
1. stockbot  ← USER ESCALATED 2026-05-08: comprehensive backtesting report (see INBOX)
2. resistance-research
3. cybersecurity-hardening
4. mfg-farm
5. seedwarden
6. open-repo
7. off-grid-living
8. workout
9. resume
10. open-source-rideshare (Paused)

## Active Projects
### stockbot
**Status**: Active — **STRATEGIC RESET 2026-05-30**: Gate 1 failed 3 consecutive checkpoints (FAR_MISS_C1 May 12, STILL_MISS_B2 May 19, STILL_MISS_B2 May 22). User has directed complete strategy reassessment. 67-session breadth test terminated. Jetson running minimal 2-session config. Priority #1: build proper backtesting pipeline before deploying any model.
**Focus**: ✅ **SPRINT 3 ITEMS 1-2 COMPLETE** + **M-1 COMPLETE**: 

### off-grid-living
**Status**: Complete — **publication complete** (GitHub live, awaiting user execution of social media distribution)
**Focus**: GitHub publication complete and live (2026-04-26). Social media execution toolkit ready (`social-media-execution-toolkit.md`). No further autonomous work available — awaiting user execution of distribution plan. All 17 domain documents production-ready and published.

### career-training
**Status**: Complete — **35 reference modules complete; case-study workbook 150/150 scenarios (100% complete)**
**Focus**: All 35 modules complete with 150 total scenarios (100% of target). Complete curriculum: foundation through business development, all 150 scenarios with full worked answers. Production-ready, awaiting user review and deployment.
## Active Blocks
### stockbot — Sprint 3 INV-1 fix ready for Jetson deployment (user approval required)
**Date blocked**: 2026-06-11
**Context**: Sprint 3 Item INV-1 (buy_prob flatline root cause fix) is complete and tested locally. Root cause was z-scores going out-of-distribution on AMZN/JPM features. Fix: z-score clipping to [-5, 5] range. 32 tests passing, committed to master (commit c0ff785c). Deployment to Jetson is held pending user approval per DEPLOY BLACKOUT RULE (no deploys during market hours 13:30–20:00 UTC). Deploy window opens 20:00 UTC tonight.
**What I need**: Approve Jetson deployment of the buy_prob z-score fix. Reply `!resolve stockbot deploy approved` and the orchestrator will push to Jetson at next post-market window (after 20:00 UTC today).
**Verify with**: `ssh xxsb-01 "docker logs stockbot --tail 20 2>&1 | grep buy_prob"` — should show non-zero buy_prob values after deploy
**Resolution**: [leave blank]
---
### cybersecurity-hardening — Phase 1 walkthrough in progress (user restart required)
**Date blocked**: 2026-05-16
**Context**: Walking through PERSONAL_OPSEC_PLAN.md Phase 1 steps with user. Paused mid-session for VeraCrypt pre-boot test restart.
**Progress so far**:
- ✅ 1.1 Signal — complete (username set, phone number hidden, disappearing messages on)
- ✅ 1.2 iPhone tracking — steps 1-3 done (tracking off, location audited, personalized ads off). Step 4 (Advanced Data Protection) pending 24-48hr Apple security delay — complete tomorrow
- 🔄 1.3 VeraCrypt — installed, encryption wizard run, **needs restart to complete pre-boot test**, then click Encrypt to start background encryption
- ⏳ 1.4 Ente Auth — not started (install from App Store, switch email + financial accounts off SMS 2FA, set carrier SIM PIN)
- ⏳ 1.5 Bitwarden password manager — not started
- ⏳ 1.6 Data broker opt-outs — not started (10 sites + 3 federal opt-outs, ~45 min)
- ⏳ 1.7 iPhone passcode over Face ID — not started (5 min, do anytime)
**What I need**: Restart Windows machine, type VeraCrypt pre-boot password when prompted, let Windows boot normally, then click Encrypt in VeraCrypt to start background encryption. Then resume Phase 1 walkthrough from step 1.4.
**Verify with**: `# manual — cannot auto-verify`
**Resolution**: [leave blank]
---
### mfg-farm — Test print execution (user action required)
**Date blocked**: 2026-05-13
**Context**: All pre-print deliverables are complete: ModRun cable clip designs (`modrun_rail.py`, `modrun_clip.py`), Etsy listing copy, supplier scorecard, production cost model. Test print is required to evaluate snap-arm tolerance (1.4mm is highest-risk feature) and validate design before production scale.
**What I need**: Execute single test print with specifications: 0.20mm layer height, PLA+, 3 walls, 220–225°C. Evaluate snap-arm clearance (FDM_TOLERANCE target) and report whether clip function is acceptable.
**Verify with**: `ls -la projects/mfg-farm/test-print-results/` — should contain test-print-evaluation.md with pass/fail decision
**Resolution**: [leave blank]
---
### systems-resilience — Phase 5.1 platform deployment blocking June 9 publication

## Recently Resolved (last 5)
• open-repo — Deployment start time conflict (user clarification required) ← 2026-06-11 02:58 UTC (Session 2995 — orchestrator autonomous resolution)
• Usage limits — weekly calibration reminder ← 2026-06-10 (Session 2977 — automated verification)
• systems-resilience — Phase 5.1 PDF bundle missing; regeneration required before June 9 ← 2026-06-06 21:15 UTC
• stockbot — Phase 3 Infrastructure Blockers (Container Restart Policy + Alpaca DNS) ← 2026-06-06 17:45 UTC (Session 2953 continuation — autonomous infrastructure fixes)
• stockbot — June 5 market execution failure: 0 trades executed (root cause identified + fix deployed, awaiting verification) ← 2026-06-06 13:33 UTC (Session 2948 — continuous 20-minute verification monitoring, zero credential errors detected)

## Inbox (unprocessed)
(NONE — all pending items processed from Session 3201)

## Recent Log (last 40 lines of WORKLOG.md)
     - `calculate_max_drawdown_from_returns(returns, initial_equity)` — reconstructs equity curve
     - `calculate_max_drawdown_from_equity_curve(equity_curve)` — direct equity-curve version
     - `calculate_calmar_ratio(ann_return, max_drawdown)` — simple wrapper
  2. Updated walk_forward_engine.py imports (added performance_metrics imports)
  3. Replaced duplicate function definitions with import aliases (backward compatible)
  4. All existing call sites now use canonical implementations (no signature changes)
- Phase 4 (REVIEW): Testing & Verification
  - Ran unit test suite: **1000+ tests PASSING** (including all metrics/performance tests)
  - Verified no regressions in walk-forward engine integration tests
  - Spot-checked metric calculations match previous implementations
- Commit: fb09dcf (feat: Sprint 3 Item M-1 — Performance metrics consolidation)

✅ **Code metrics**:
- Performance metrics module: +170 lines (new wrapper functions) 
- Walk forward engine: -47 lines (removed duplicate definitions, added 4-line alias section)
- Net change: +123 lines (added 4 functions to canonical module, removed from duplicate)
- Test coverage: 1000+ unit tests passing (no new test code needed, existing tests validate consolidation)

**Sprint 3 Status Summary**:
| Item | Status | Details |
|------|--------|---------|
| Item 1: buy_prob fix | ✅ Code complete | z-score clipping [-5,5], 32 tests passing, ready for Jetson deployment |
| Item 2: H-5 DB unification | ✅ Code complete | ORM integration, backward compatible, committed |
| M-1: Metrics consolidation | ✅ Code complete | Canonical module, 4 wrapper functions, backward compatible, 1000+ tests passing |
| M-2 to M-10: Medium tech debt | 🔄 Queued | 10 medium-severity items ready for next session |

**Remaining Work**:
1. **Next session**: M-2 (TradingSession.__init__ refactoring — 270+ line constructor reduction)
2. **Post-market window**: Optional quick-win M items (M-8, M-7, M-4 configuration consolidation)
3. **Phase 4 integration tests**: Hook up H-5 results to backtest pipeline once all M items complete

**Session duration**: ~66 minutes (PLAN, IMPLEMENT, REVIEW, COMMIT, DOCUMENT)

**Key learnings**:
- Consolidating duplicate code requires finding the correct abstraction level (match existing call signatures)
- Walk-forward engine metrics had subtle differences (statistics vs numpy) — unified to statistics (pure Python)
- Import aliases provide instant backward compatibility (no call-site changes needed)
- Comprehensive test coverage caught zero regressions (confidence in refactoring)

**Next**: Stand by for next session or user approval for M-2 refactoring.
