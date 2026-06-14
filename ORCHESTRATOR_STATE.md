# Orchestrator State
> Auto-generated at 2026-06-14T19:21:40Z — do not edit. Source: PROJECTS.md, WORKLOG.md, BLOCKED.md, INBOX.md.

## Usage
🟢 Usage: Sonnet 2.3% (203,964 tokens) | All-models 27.1% | Reset in 29h | check: claude.ai → Settings → Usage & billing

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
**Focus**: ✅ **[P3 RESOLVED + MODELS DEPLOYED — JUNE 14] AAPL + MSFT LGBM_HO JETSON LIVE** — (1) **Status**: AAPL lgbm_ho (OOS Sharpe 2.444) + MSFT lgbm_ho (OOS Sharpe 1.573) deployed to Jetson June 14 15:15 UTC. 4-session config active (JPM ridge_wf + AMZN lgbm_ho + AAPL lgbm_ho + MSFT lgbm_ho), container healthy ✅. (2) **Next Trigger**: **June 16 13:30 UTC market open** — verify signal generation + trade execution on AAPL/MSFT. (3) **Hard deadline**: June 18 EOD — both models must execute tra … *(truncated — prune Current focus in PROJECTS.md)*

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

## Recently Resolved (last 5)
• stockbot — AAPL lgbm_ho + MSFT ridge_wf feature mismatch during walk-forward evaluation ← 2026-06-14 13:42 UTC (user decision, session 3538)
• stockbot — Sprint 3 INV-1 fix ready for Jetson deployment (user approval required) ← 2026-06-11 17:02 UTC (Session 3202 — orchestrator processing)
• open-repo — Deployment start time conflict (user clarification required) ← 2026-06-11 02:58 UTC (Session 2995 — orchestrator autonomous resolution)
• Usage limits — weekly calibration reminder ← 2026-06-10 (Session 2977 — automated verification)
• systems-resilience — Phase 5.1 PDF bundle missing; regeneration required before June 9 ← 2026-06-06 21:15 UTC

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

**Deliverable 2 — Domain 59 (Economic Precarity) Rapid-Activation Runbook** ✅
- 5 research zones: Dallas Fed causal evidence, OBBBA provision-to-pathway, housing instability/eviction, gig economy temporal exclusion, post-2027 reform coalition framing
- 50+ pre-linked sources (all verified June 10 contact audit)
- Express Senate outreach path (45 min, independent of research sprint): AFL-CIO, CBPP, NWLC with copy-paste email templates + send timing
- 8 expert contacts verified (Chiraag Bains departure from Demos correctly routed to Taifa Smith Butler at Demos)
- 6 contingency paths (Senate bill passage, AFL-CIO pivot, bounce recovery, CBPP fallback, Senate window closure)
- File: `projects/resistance-research/DOMAIN_59_RAPID_ACTIVATION_RUNBOOK.md` (production-ready)

**Deliverable 3 — Domain 51/59 Sequential Activation Timing Coordination** ✅
- Core finding: Domain 59 takes priority (Senate Finance CTC window June 25-30 closes before California ballot messaging July 1)
- 2-day stagger: Domain 59 Day 0 (checkpoint day), Domain 51 Day 1
- Resource allocation matrix: zero contact overlap, both domains runnable in same 7-day window
- Minimum viable path (75 min total): 45 min Domain 59 express + 30 min Domain 51 Tier 1
- 3 cross-domain integration points identified (FEC enforcement as structural amplifier, OBBBA narrative convergence, GOTV synthesis for AFL-CIO/MomsRising/Common Cause)
- 5 failure mode recovery paths (one domain stalls, both stall, Senate window closes, California ballot removal, bandwidth constraint)
- File: `projects/resistance-research/DOMAINS_51_59_SEQUENTIAL_ACTIVATION_TIMING.md` (production-ready)

**Quality Metrics**:
- Confidence: 90%+ (immediately executable, not exploratory)
- Specificity: Named expert contacts with verification status, exact email addresses, routing corrections applied
- Contingency depth: 3-5 failure modes per critical step
- Sources: 65 + 50 pre-linked, all verified against prior resistance-research docs + June 10 contact audit

**Business Value**:
When user approves Phase 2 Domains 51/59 on June 17-18 Day 7 checkpoint, execution can begin immediately with zero discovery overhead. This removes decision paralysis and accelerates Phase 2 expansion to full activation timeline.

**Status**:
All three files staged for commit. Committed to master with this session.

**Next Phase 2 Trigger**:
- **User execution window**: June 14-15 23:59 UTC (Wave 1-2 email campaigns, ~75 min total)
- **June 17-18 Day 7 checkpoint**: Coalition leverage analysis + Gist tracking review + activate Domains 51/59 if engagement metrics support (using these runbooks for instant execution)
- **Hard deadline July 1**: Phase 2 completion by July 1 per user roadmap

**Token Usage**: ~124K (agent: general-research, 755s wall-clock for Domain research + synthesis).

**Assessment**:
Orchestrator fully standing-by. All active work (stockbot, resistance-research) is either awaiting external triggers (June 16 market open, user Wave 1-2 execution) or blocked on user decisions (cybersecurity VeraCrypt restart, mfg-farm test print, systems-resilience platform choice). Exploration Queue item completed. Next autonomous work window: June 16 13:30 UTC market validation + subsequent Phase 2 Day 7 checkpoint routing.
