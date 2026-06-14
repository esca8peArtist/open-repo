# Orchestrator State
> Auto-generated at 2026-06-14T13:21:20Z — do not edit. Source: PROJECTS.md, WORKLOG.md, BLOCKED.md, INBOX.md.

## Usage
🟢 Usage: Sonnet 1.9% (166,125 tokens) | All-models 19.2% | Reset in 35h | check: claude.ai → Settings → Usage & billing

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
**Focus**: ✅ **[PHASE 2 WAVE 1-2 EXECUTION READY — ALL STEP-BY-STEP CHECKLISTS STAGED (SESSION 3514)]** — **PHASE 2 EXECUTION STATUS**: 

### stockbot
**Status**: Active — **STRATEGIC RESET 2026-05-30**: Gate 1 failed 3 consecutive checkpoints (FAR_MISS_C1 May 12, STILL_MISS_B2 May 19, STILL_MISS_B2 May 22). User has directed complete strategy reassessment. 67-session breadth test terminated. Jetson running minimal 2-session config. Priority #1: build proper backtesting pipeline before deploying any model.
**Focus**: ✅ **P1/P2/ML-1/2/3/WB-1/2/3 ALL COMPLETE — P3 DECISION-READY (3 BRANCHES STAGED, USER DECIDES JUNE 15 EOD)** — User unpause June 13 15:57 UTC. Signal restoration verified June 14 02:15 UTC (AMZN buy_prob=0.33+). **Completed**: P1 (Signal Health Monitor, 90 tests), P2 (Quick-eval flag, 56 tests), ML-1/2/3 (142 tests total: Monte Carlo G7 + news sentiment + drawdown metrics), WB-1/2/3 (29 tests total: candidates.yaml + weekend_batch.py + promote_to_paper.py). **P3 STATUS (SESSION 3514)**: Fe … *(truncated — prune Current focus in PROJECTS.md)*

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
### systems-resilience — Phase 5.1 platform deployment blocking June 9 publication
**Date blocked**: 2026-06-06
**Context**: Phase 5.1 publication deployment is scheduled for June 9 13:00–15:00 UTC. Pre-flight verification completed (Session 2964, Agent a8509b87e34e2aa5b). All content is production-ready (61,611 words, 336+ citations documented). However, the publication platform is not deployed on raspby1. As of June 6 20:05 UTC: Docker was not installed (resolved in Session 2965), no Nextcloud or Discourse containers exist, no web services on ports 80/443. The deployment runbook assumes the platform will be deployed by June 8 18:00 UTC and will begin using it at 12:30 UTC June 9. Platform choice (Nextcloud+Matrix vs Discourse) is pending user decision from Session 2965 CHECKIN.
**What I need**: User decision on which platform to deploy (Nextcloud+Matrix or Discourse). Recommendation: Discourse is more suitable for this Raspberry Pi 5 (8GB RAM recommended vs Nextcloud's 16GB) and deploys faster (2-3 hours vs 4-6 hours). If Discourse chosen, provide public IP + domain for platform, and SMTP credentials for email notifications. If Nextcloud+Matrix chosen, confirm acceptance of memory risk (system has 7.9GB total RAM). Once choice is confirmed, orchestrator will execute platform deployment by June 8 18:00 UTC deadline.
**Verify with**: `docker ps | grep -E "nextcloud|discourse"` should show running container, and `curl http://[platform-ip]:80` or `curl https://[platform-domain]:443` should return 200 OK
**Resolution**: [leave blank]
---
### stockbot — AAPL lgbm_ho + MSFT ridge_wf feature mismatch during walk-forward evaluation

## Recently Resolved (last 5)
• stockbot — Sprint 3 INV-1 fix ready for Jetson deployment (user approval required) ← 2026-06-11 17:02 UTC (Session 3202 — orchestrator processing)
• open-repo — Deployment start time conflict (user clarification required) ← 2026-06-11 02:58 UTC (Session 2995 — orchestrator autonomous resolution)
• Usage limits — weekly calibration reminder ← 2026-06-10 (Session 2977 — automated verification)
• systems-resilience — Phase 5.1 PDF bundle missing; regeneration required before June 9 ← 2026-06-06 21:15 UTC
• stockbot — Phase 3 Infrastructure Blockers (Container Restart Policy + Alpaca DNS) ← 2026-06-06 17:45 UTC (Session 2953 continuation — autonomous infrastructure fixes)

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
- Verified `feature/p3-option-a-7-feature-reduction`, `feature/p3-option-b-14-feature-parity`, `feature/p3-staging-both-options` all exist in stockbot repo ✅
- Confirmed P3 staged state: current HEAD on feature/p3-option-a-7-feature-reduction
- Verified all orchestration files (PROJECTS.md, BLOCKED.md, CHECKIN.md) in sync describing standing-by state
- No code changes, no infrastructure modifications, no new work
- Preparing for June 16 00:00 UTC auto-activation trigger if no user decisions made

**Critical User Decisions Status** (All Due June 15 EOD):
1. **Stockbot P3 Architecture** — Both Option A (41 tests ✅) and Option B (47 tests ✅) fully staged in feature branches. Ready for user merge decision.
2. **Systems-Resilience Platform** — Nextcloud vs Discourse specs staged. Awaiting user choice.
3. **Resistance-Research Wave 1-2 Execution** — All email templates + execution checklists staged. Optional June 14-15 recovery window.
4. **Cybersecurity-Hardening VeraCrypt** — Phase 1.3 waiting for Windows restart (manual user action).

**Exploration Queue Status** (All conditional, trigger on user decisions):
- **4 items staged**: Post-Retrain Validation, Phase 3 Onboarding, Phase 5.1 Deployment Config, Phase 4 Implementation Strategy
- **Trigger**: June 16 00:00 UTC auto-activation if no P3/platform/Wave-2 decisions made
- **Confidence**: 85-92% across all items

**Project Status Summary**:
- **stockbot**: P1/P2/ML-1/2/3/WB-1/2/3 ✅ complete. P3 decision-ready (branches staged). Phase 4 pre-planning complete.
- **resistance-research**: Phase 2 Wave 1-2 execution infrastructure ✅ complete and staged. Phase 3 Domains 49-50 research framework complete. Ready for post-Wave-2 onboarding.
- **cybersecurity-hardening**: Paused at Phase 1.3 VeraCrypt (manual action required).
- **mfg-farm**: Paused on test print execution (manual action required).
- **off-grid-living**: Complete, awaiting user social media execution.
- **systems-resilience**: Wave 2 author assignment complete. Phase 5.1 deployment specs staged (awaiting platform decision).
- **open-source-rideshare**: Paused.
- **seedwarden, workout, resume, mom-projects**: Not active this cycle.

**Recommended User Actions** (Priority, All Due Tomorrow):
1. **TODAY**: Decide stockbot P3 (Option A: 7 features, 1-2h | Option B: 14 features, 2-4h RECOMMENDED) — Review decision guide in `feature/p3-staging-both-options` PR
2. **TODAY**: Decide platform (Nextcloud+Matrix vs Discourse RECOMMENDED for 8GB RAM) — Will trigger June 16-19 deployment execution
3. **OPTIONAL**: Execute Wave 1-2 emails (30-45 min Wave 1 + 45-60 min Wave 2) — Recovery for June 9-10 slip
4. **OPTIONAL**: Execute cybersecurity Phase 1.3 VeraCrypt restart (15-20 min) + mfg-farm test print (120 min parallel)

**Next Orchestrator Action**:
- **If decisions by June 16 00:00 UTC**: Execute AAPL/MSFT retrains immediately (5.5-7h), then activate queue items post-decision
- **If no decisions by June 16 00:00 UTC**: Activate 3 queue items autonomously (Phase 4 strategy, Phase 3 onboarding, deployment config) — can work without waiting further
- **Checkpoint**: All files committed to master. Standing by for user direction.

**Token Usage**: 34K this session (minimal standing-by verification, no agent work).
