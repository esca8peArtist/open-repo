# Orchestrator State
> Auto-generated at 2026-07-05T00:40:44Z — do not edit. Source: PROJECTS.md, WORKLOG.md, BLOCKED.md, INBOX.md.

## Usage
🟢 Usage: Sonnet 7.2% (777,441 tokens) | All-models 7.9% | Reset in 47h | check: claude.ai → Settings → Usage & billing

## Priority Order
1. stockbot  ← USER ESCALATED 2026-05-08: comprehensive backtesting report (see INBOX)
2. resistance-research
3. cybersecurity-hardening
4. mfg-farm
5. seedwarden
6. open-repo
7. career-training  ← ADDED 2026-06-27: gap modules + deployment (was missing from queue)
8. off-grid-living
9. workout
10. resume
11. open-source-rideshare (Paused)

## Active Projects
### resistance-research
**Status**: Active — Phase 2 Wave 1 execution initiated (Session 3220)
**Focus**: **[DOMAIN M PHASE 1 RESEARCH SPRINT IN PROGRESS; SESSION 4585]** — Phase 2 Wave 1 ALL COMPLETE (all four new actionable guides finished by Session 4582). Domain 51 (Campaign Finance) deadline MISSED June 30 23:59 UTC; Domain M contingency ACTIVE (July 1-15). **Domain M Phase 1 (due today July 5)**: 3,000-4,000-word brief "Direct Democracy Under Supermajority Attack" being written, covering four-state coordinated attack on ballot measures (Missouri, North Dakota, South Dakota, Utah). Phase 2 (J … *(truncated — prune Current focus in PROJECTS.md)*

### stockbot
**Status**: Active — **STRATEGIC RESET 2026-05-30**: Gate 1 failed 3 consecutive checkpoints (FAR_MISS_C1 May 12, STILL_MISS_B2 May 19, STILL_MISS_B2 May 22). User has directed complete strategy reassessment. 67-session breadth test terminated. Jetson running minimal 2-session config. Priority #1: build proper backtesting pipeline before deploying any model.
**Focus**: ✅ **[LIVE_MONITORING PHASE 2 COMPLETE] SESSION 4494 (2026-06-29 03:35 UTC); MODEL_PIPELINE PHASE 2 PRE-STAGING COMPLETE (SESSION 4528 ITEM 39)** — All three Phase 2 anomaly detections implemented, tested, and passing: (2a) FILL_MISMATCH (SQLite↔API reconciliation, delta>1), (2b) POSITION_PHANTOM (2-poll guard, engine↔Alpaca sync), (2c) ORDER_REJECTED + ORDER_REJECTED_ESCALATION (per-ticker daily tracking, 3+ rejections = degraded). Bonus: FILL_DETAIL_MISMATCH (partial fills, price slippa … *(truncated — prune Current focus in PROJECTS.md)*

### open-repo
**Status**: Active — GitHub Pages approach; no Pi server deployment
**Focus**: ✅ **SCHEMA DOCUMENTATION PRODUCTION-READY; PHASE 5 COMPLETE; PHASE 5.2 WAVE 0 STRATEGY STAGED** — Code verdict: all 51 ZIM tests passing. Platform decision resolved: GitHub Pages / GitHub public hosting (no Pi server deployment). Schema documentation (879 lines, 10 sections) production-ready. Phase 5.2 Wave 0 strategy complete: Water Systems Priority 1 domain, contributor onboarding workflow, platform mechanics (GoatCounter analytics, A/B testing, GitHub Pages + Netlify fallback), timeline w … *(truncated — prune Current focus in PROJECTS.md)*

### systems-resilience
**Status**: Active — GitHub Pages approach; no Pi server deployment; Phase 6 Domain A research complete
**Focus**: **[ACTIVE — GITHUB PAGES PATH; PHASE 6 DEMOCRACY TOOLS EXECUTION FRAMEWORK PRODUCTION-READY (ITEM 40); PHASE 6 RESEARCH LAUNCH NOV 4]** — Platform decision resolved (2026-06-28, Decisions 1-2): User rejected Pi hosting, Nextcloud/Matrix, and Discourse. All content (Phase 5.1 corpus 61,611 words, Phase 6 research) will go to GitHub Pages / public GitHub. **Phase 6 status**: ✅ **[SESSION 4492] DEMOCRACY TOOLS DOMAIN PRE-RESEARCH COMPLETE (ITEM 31)** + ✅ **[SESSION 4528] PHASE 6 EXECUTION F … *(truncated — prune Current focus in PROJECTS.md)*

### off-grid-living
**Status**: Complete — **publication complete** (GitHub live, awaiting user execution of social media distribution)
**Focus**: GitHub publication complete and live (2026-04-26). Social media execution toolkit ready (`social-media-execution-toolkit.md`). No further autonomous work available — awaiting user execution of distribution plan. All 17 domain documents production-ready and published.

### career-training
**Status**: Complete — **35 reference modules complete; case-study workbook 150/150 scenarios (100% complete)**
**Focus**: ✅ **[ALL 38 MODULES + 150 SCENARIOS COMPLETE; GITHUB PAGES DEPLOYMENT READY]** — All content production-ready for GitHub Pages deployment or integration into training programs. /docs directory with Jekyll infrastructure complete. **Awaiting user action**: (1) Create/enable GitHub repo, (2) push /docs directory for GitHub Pages live deployment, (3) configure Phase 2 (email list) and Phase 3 (social media) platforms. Zero autonomous work remaining.
## Active Blocks
### Usage limits — weekly calibration reminder
**Date blocked**: 2026-06-30 (auto-added each Tuesday by reset-usage-budget.sh)
**Context**: Plan limits reset today. Token limits in usage-check.py are calibrated estimates that drift over time. Verify against actual UI percentages.
**What I need**: Check claude.ai → Settings → Usage & billing. Run: `bash scripts/verify-calibration.sh <sonnet_pct> <all_pct>`
**Verify with**: `bash scripts/verify-calibration.sh`
**Resolution**: ✅ **RESOLVED** (Session 4585, 2026-07-05 00:25 UTC) — Verification passed: `bash scripts/verify-calibration.sh` returned "OK: limits calibrated 1 days ago (2026-07-04) — within 7-day window." No recalibration needed. Usage budget is current.
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
### systems-resilience — Phase 5 GitHub release requires maintainer push permissions
**Date blocked**: 2026-06-27

## Recently Resolved (last 5)
• resistance-research — Domain 51 Phase 2 Wave 1 Distribution CRITICAL (18:00 UTC cutoff PASSED; contingency activated) ← 2026-06-29 20:12 UTC (Session 4554 — contingency activated)
• open-repo — June 12 deployment never executed; platform decision resolved by user ← 2026-06-28 (Session 4474 — user decision)
• systems-resilience — Phase 5.1 platform deployment blocking June 9 publication ← 2026-06-28 (Session 4474 — user decision)
• stockbot — CRITICAL: Phase 1 validation failure (13:30–13:40 UTC) — real-time stream NOT initialized, sessions timing out ← 2026-06-24 14:00 UTC (Session 4186, orchestrator orientation)
• stockbot — CRITICAL: Container API startup was blocked by missing alembic.ini volume mount ← 2026-06-24 09:48 UTC (Session 4160 — orchestrator autonomous fix + verification)

## Inbox (unprocessed)
*(No unprocessed items)*

## Recent Log (last 40 lines of WORKLOG.md)
   **systems-resilience** (1 task, commit 8c5df6ca):
   - `phase-6/PHASE_6_ZONE_1_2_VOTER_REGISTRATION_AND_TECHNOLOGY.md` (365 lines, 9,400 words, 50 sources) — Zone 1: Callais eliminates VRA Section 2 results test (40% higher purge rates in formerly-covered jurisdictions), SAVE Act blocked 12% of Kansas applicants (31K eligible citizens), 19.1M purges 2020-22, same-day registration (3-7pt youth turnout gain), auto-registration (8.1% registration rate increase). Zone 2: TurboVote 79% vs 64% national turnout, ERIC consortium (27 states), BallotTrax, ACLU $24.5M 2026 investment, AI demobilization risk landscape

**Deployment Gate**: Next market open July 7 (Monday). All 9 features deployed and ready 84h ahead of first trading session.

**Session Total**: 9 stockbot features deployed + 4 research documents (~35,000 words) across resistance-research and systems-resilience. 5 commits.

**Pending User Actions**:
1. **Usage calibration**: Check claude.ai billing, run `bash scripts/verify-calibration.sh <sonnet_pct> <all_pct>`
2. **VeraCrypt**: Restart Windows, complete pre-boot test, click Encrypt (cybersecurity-hardening Phase 1)
3. **Domain M**: July 1-15 execution window — templates at `projects/resistance-research/DOMAIN_M_TIER_1_SEND_TEMPLATES.md`, runbook at `DOMAIN_M_JULY_1_15_ACTIVATION_SEQUENCE.md`; user sends emails
4. **Stockbot July 7**: First market open with all 9 features — monitor Discord for PERCENTILE_GATE restoring JPM signals

## 2026-07-05 00:25 UTC — Session 4585 Orientation Complete

**Orchestrator Status**:
- ✅ 9 stockbot features merged to master and DEPLOY_READY flag set (Sunday, safe)
- ✅ Usage calibration verified (within 7-day window)
- ✅ All Phase 2 Wave 1 new actionable guides completed (surveillance removal, ICE victim support, Flock Safety)
- ✅ Domain 51 deadline passed June 30 23:59 UTC; Domain M contingency ACTIVE

**Autonomous Work Available**:
1. **[PRIORITY] Domain M Research Sprint (Item 44)** — Due TODAY (July 5)
   - Write 3,000-4,000-word brief on "Direct Democracy Under Supermajority Attack"
   - Target: Draft by end of session → Gist creation → Stage for Tier 1 sends July 7-15
   - Status: All sources verified, structure ready, triggers Phase 2-3 distribution

2. **[WAITING] Stockbot — Model Pipeline Phase 2 Launch**
   - Gate condition: 5 consecutive nights search ≥20 DB rows/ticker
   - Expected: ~July 7 (depends on Optuna hyperparameter sweep completing overnight)
   - Status: Pre-staging complete, 0-lag launch ready when gate crosses

3. **[WAITING] Phase 3 Research** (Systems-resilience, November 4 launch)
   - Infrastructure complete; research sprint Nov 4-12
   - User decisions needed: contractor hiring by October 15

**Allocation Decision**:
Spawning resistance-research agent NOW for Domain M Phase 1 Research Sprint.
Completion target: Domain M brief production-ready for Gist + distribution by session end.
