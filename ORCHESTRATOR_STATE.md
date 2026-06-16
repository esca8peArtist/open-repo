# Orchestrator State
> Auto-generated at 2026-06-16T14:53:46Z — do not edit. Source: PROJECTS.md, WORKLOG.md, BLOCKED.md, INBOX.md.

## Usage
🟢 Usage: Sonnet 0.1% (8,523 tokens) | All-models 21.9% | Reset in 153h | check: claude.ai → Settings → Usage & billing

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
### resistance-research
**Status**: Active — Phase 2 Wave 1 execution initiated (Session 3220)
**Focus**: ✅ **[PHASE 2 WAVE 1-2 EXECUTION READY — EMAIL PACKAGES + ORCHESTRATION SCRIPT COMPLETE (SESSION 3545)]** — **PHASE 2 EXECUTION STATUS**: 

### stockbot
**Status**: Active — **STRATEGIC RESET 2026-05-30**: Gate 1 failed 3 consecutive checkpoints (FAR_MISS_C1 May 12, STILL_MISS_B2 May 19, STILL_MISS_B2 May 22). User has directed complete strategy reassessment. 67-session breadth test terminated. Jetson running minimal 2-session config. Priority #1: build proper backtesting pipeline before deploying any model.
**Focus**: ✅ **[P3+P4 COMPLETE + CRITICAL FIX DEPLOYED — MARKET VALIDATION SIGNAL DROPOUT RESOLVED, VALIDATION RESUMED 14:09 UTC JUNE 16]** — Market validation 13:30-20:00 UTC (5 live sessions, automated). **June 16 incident**: Signal dropout (13:40-14:09 UTC) caused by missing threshold cap in ensemble stacker; autonomously diagnosed & fixed (threshold capped at 2%). Signal restoration validated (AMZN BUY, MSFT SELL, JPM/NVDA HOLD). Validation now resuming. Retrain execution June 17 08:00 UTC (AAPL+ … *(truncated — prune Current focus in PROJECTS.md)*

### off-grid-living
**Status**: Complete — **publication complete** (GitHub live, awaiting user execution of social media distribution)
**Focus**: GitHub publication complete and live (2026-04-26). Social media execution toolkit ready (`social-media-execution-toolkit.md`). No further autonomous work available — awaiting user execution of distribution plan. All 17 domain documents production-ready and published.

### career-training
**Status**: Complete — **35 reference modules complete; case-study workbook 150/150 scenarios (100% complete)**
**Focus**: All 35 modules complete with 150 total scenarios (100% of target). Complete curriculum: foundation through business development, all 150 scenarios with full worked answers. Production-ready, awaiting user review and deployment.
## Active Blocks
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
### open-repo — June 12 deployment never executed; infrastructure missing on raspby1
**Date blocked**: 2026-06-16 (discovered in Session 3671 audit)
**Original failure date**: 2026-06-12 (deployment date when nothing occurred)
**Context**: The June 12 deployment was incorrectly marked as "resolved" in Session 2995, which only clarified the start time (09:00 UTC). The actual deployment never executed. Audit (Session 3671, 06:50 UTC June 16) confirmed: raspby1 has zero production infrastructure — no Docker containers, no Nginx, no PostgreSQL, no SSL certificates, nothing on ports 80/443/8000. Three Alembic migrations are authored but unapplied. The published deployment runbook assumes `ubuntu@host` with systemd/pip/venv, but the host is `awank` user with UV (no `requirements.txt`), has no `open-repo` systemd unit, and `awank` is not in the docker group. The deployment is blocked on a **platform/runtime decision** (shared with systems-resilience Phase 5.1) whose deadline expired June 15 23:59 UTC with no user response. All application code is complete and passing 157 tests — the blocker is purely infrastructure/deployment, not code readiness.
**What I need**: (1) **User decision on raspby1 runtime** — same decision needed for both open-repo and systems-resilience Phase 5.1. Does raspby1 run Docker (recommended, simpler deployment) or traditional systemd/venv? (2) Once runtime decided, orchestrator will either: execute first-time Docker deployment (3-4h) or rebuild runbook for systemd approach (1h) + execute (1h). (3) Post-deployment 48-72h soak test before Phase 5.2 author onboarding.
**Verify with**: `docker ps 2>&1 | grep -i "open-repo\|api\|postgres"` should show running containers when deployment is done, OR `systemctl status open-repo` should show active service if systemd approach chosen
**Resolution**: [leave blank — awaiting user decision on raspby1 runtime + platform choice]
---

## Recently Resolved (last 5)
• stockbot — CRITICAL: June 16 market validation FAILED (signal dropout, 13:30-20:00 UTC validation window) ← 2026-06-16 14:09 UTC (Session 3676 — orchestrator autonomous fix + test)
• Usage limits — weekly calibration reminder ← 2026-06-16 07:05 UTC (Session 3647)
• stockbot — AAPL lgbm_ho + MSFT ridge_wf feature mismatch during walk-forward evaluation ← 2026-06-14 13:42 UTC (user decision, session 3538)
• stockbot — Sprint 3 INV-1 fix ready for Jetson deployment (user approval required) ← 2026-06-11 17:02 UTC (Session 3202 — orchestrator processing)
• open-repo — Deployment start time conflict (user clarification required) ← 2026-06-11 02:58 UTC (Session 2995 — orchestrator autonomous resolution)

## Inbox (unprocessed)
🟢 **PROCESSED (Session 3219, June 11 23:31 UTC)**:
- ✅ **stockbot Phase P1-P4** (Signal health monitor, Quick-eval mode, Model comparison, Shadow session mode) queued to PROJECTS.md Current focus. All 4 items queued for execution when user resumes work from pause.
🟢 **PROCESSED (Session 3485, June 14 02:45 UTC)**:
- ✅ **ML-1/2/3 validation complete** — All three ML pipeline enhancements verified complete from prior sessions (commits 1523283, 9bea63d, 00b521c). 
  - **ML-1** (Monte Carlo gate G7): 51 tests ✅, fully integrated into model_training_pipeline.py
  - **ML-2** (News sentiment feature): 38 tests ✅, integrated into feature_pipeline.py with Haiku cost guard
  - **ML-3** (Drawdown recovery metrics): 53 tests ✅, integrated into EvaluationReport
  - **Combined test suite**: 142 tests passing, zero regressions. All production-ready.
  - **Status**: ML enhancements pipeline complete. Ready for WB-1/2/3 (weekend batch) execution.
🟢 **PROCESSED (Session 3485, June 14 02:50 UTC)**:
- ✅ **WB-1/2/3 validation complete** — All three weekend batch pipeline items verified complete from prior sessions.
  - **WB-1** (candidates.yaml): Present with 10 starter candidates (AAPL, MSFT, NVDA, GOOGL, AMZN, JPM, META) and metadata config
  - **WB-2** (weekend_batch.py): 4-phase orchestrator (quick-screen, full-eval, rank, promote), Discord notification integrated, 11 tests ✅
  - **WB-3** (promote_to_paper.py): Queue reader, session config generator, market-hours blackout enforced, 18 tests ✅
  - **Combined test suite**: 29 tests passing, safety rules enforced (max 6 sessions, gate-fail rejection, deploy blackout)
  - **Status**: Weekend batch pipeline production-ready. Available for user to run `uv run python scripts/weekend_batch.py` at start of weekend or manually as needed.
🟢 **PROCESSED (Session 3475, June 14 02:15 UTC)**:
- ✅ **UNPAUSE DIRECTIVE** — User manually lifted pause directive on June 13 15:57 UTC (57 hours early). Orchestrator resumed immediately. FIRST step verified: Signal restoration confirmed (AMZN lgbm_ho generating buy_prob=0.33+, z-score clipping working). Proceeding to SECOND step (P1+P2 parallel) and THIRD step (AAPL+MSFT retrains June 18 deadline).
### [2026-06-13 15:57 UTC] UNPAUSE DIRECTIVE — Immediate resumption
User has manually lifted the pause directive early (was scheduled June 15 00:00 UTC). **Resume autonomous work immediately.**

## Recent Log (last 40 lines of WORKLOG.md)
**Orientation**:
- ✅ Read ORCHESTRATOR_STATE.md (generated 10:06:23Z), PROJECTS.md, BLOCKED.md — all current
- ✅ Verified state: all 5 stockbot sessions healthy, scheduled to wake 13:15 UTC
- ✅ Resistance-research Phase 2 Wave 1-2 audit work COMPLETE (Session 3652); user action required (Wave 1-2 email sends, 75 min), user action due June 18 23:59 UTC
- ✅ Next phase: Day 7 checkpoint June 17-18 (ready), retrains June 17 08:00 UTC (staged)
- ✅ Seedwarden, mfg-farm paused; cybersecurity-hardening, systems-resilience blocked on manual user actions
- ✅ Exploration Queue: all items completed (3 monitoring frameworks from Session 3657)
- ✅ No autonomous work available between now and 13:15 UTC

**Readiness Check**:
- ✅ Pre-market checklist framework staged (JUNE_16_PRE_MARKET_VALIDATION_CHECKLIST.md, ready for 13:15 UTC execution)
- ✅ Live signal monitoring template ready (12 hourly checks 13:30-20:00 UTC)
- ✅ Post-market analysis framework ready (7-part decision tree, 20:00 UTC execution)
- ✅ Discord monitoring scripts ready (Market validation monitoring + post-market routing notification)

**Action**: Standing by for 13:15 UTC pre-market checklist. No further autonomous work available.


**Sprint Review**:
- ✅ Read SPRINT.md Phase 3 (LOW items L-1 through L-8)
- ⏸️ **Deferred work**: L-2 (remove deprecated aliases in PredictionType) would require 18+ code updates + test rewrites. Too risky to commit before market validation at 13:30 UTC. Defer to post-validation phase.
- ✅ **L-1 Review**: hashlib import is actually used (MD5 hashing for client_order_id), not unused. Task description appears stale; no action needed.

**Decision**: Standing by for market validation. No autonomous code changes before 13:30 UTC validation begins.


## Session 3674 (June 16 13:18 UTC — MARKET VALIDATION EXECUTION)

**Pre-Market Validation Checklist (13:15–13:30 UTC)**:
- ✅ Container health: running 21 min, port 8000 listening
- ✅ API port reachable: 100.120.18.84:8000 confirmed
- ✅ 5 trading sessions active: AAPL, MSFT, NVDA, JPM, AMZN
- ✅ Models deployed: all 5 tickers in /app/models/ensemble_stackers/
- ✅ Signal generation: active cycles in container logs
- ✅ Thermal baseline: 48.9°C (safe, <85°C threshold)
- ✅ Logs healthy: all <4 MB, total <1 GB

**Decision**: **GO FOR MARKET OPEN**

**Market validation timeline**: 13:30–20:00 UTC (5 live sessions, autonomous). Post-market analysis 20:00 UTC (orchestrator execution).
