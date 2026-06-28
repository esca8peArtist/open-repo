# Orchestrator State
> Auto-generated at 2026-06-28T20:54:24Z — do not edit. Source: PROJECTS.md, WORKLOG.md, BLOCKED.md, INBOX.md.

## Usage
🟢 Usage: Sonnet 0.1% (902,514 tokens) | All-models 0.1% | Reset in 27h | check: claude.ai → Settings → Usage & billing

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
**Focus**: ✅ **[RESOLVED] PHASE 2 WAVE 1-2 + PHASE 3 SOURCE STAGING COMPLETE (JUNE 23 18:30 UTC)** — **PHASE 2 STATUS**: SCOTUS execution window hard-closed 18:00 UTC (user never verified outcome); all Phase 2 rapid-response infrastructure remains production-ready for retroactive execution if user posts outcome post-deadline. **Autonomous Phase 2 work**: ZERO. **User action ready**: (1) T+7 inbox monitoring + signal classification (June 23-25), (2) Domain 59 Tier 2 sends (EPI/Demos/NELP, June 25-30), ( … *(truncated — prune Current focus in PROJECTS.md)*

### stockbot
**Status**: Active — **STRATEGIC RESET 2026-05-30**: Gate 1 failed 3 consecutive checkpoints (FAR_MISS_C1 May 12, STILL_MISS_B2 May 19, STILL_MISS_B2 May 22). User has directed complete strategy reassessment. 67-session breadth test terminated. Jetson running minimal 2-session config. Priority #1: build proper backtesting pipeline before deploying any model.
**Focus**: ✅ **[DEPLOYMENT COMPLETE] REAL-TIME STREAM FIX DEPLOYED 2026-06-24** — Root cause: aggressive `asyncio.wait_for(timeout=300)` wrapper forcefully closed WebSocket every 5 minutes. Fix: removed timeout wrapper, stream now reconnects naturally on Alpaca direction without forced closure (commit d4b675ba). All 5 sessions healthy (jpm_ridge_wf, amzn/aapl/msft/nvda lgbm_ho), WebSocket registered, real-time IEX stream active. **✅ [OPENSPECS COMPLETE] SESSION 4325 — BOTH PHASE 1 IMPLEMENTATIONS D … *(truncated — prune Current focus in PROJECTS.md)*

### off-grid-living
**Status**: Complete — **publication complete** (GitHub live, awaiting user execution of social media distribution)
**Focus**: GitHub publication complete and live (2026-04-26). Social media execution toolkit ready (`social-media-execution-toolkit.md`). No further autonomous work available — awaiting user execution of distribution plan. All 17 domain documents production-ready and published.

### career-training
**Status**: Complete — **35 reference modules complete; case-study workbook 150/150 scenarios (100% complete)**
**Focus**: ✅ **[DEPLOYMENT IN PROGRESS] GITHUB PAGES PHASE 1 INFRASTRUCTURE COMPLETE (SESSION 4351)** — Created /docs directory structure, copied all 33 modules, built Jekyll _config.yml, created homepage + 6 navigation pages (quick-start, module-reference, industrial/residential/specialty paths, FAQ). Production-ready for GitHub Pages. Next: User creates/enables GitHub repo, configures domain, pushes /docs to main. Phase 2 (email list) and Phase 3 (social media) await user platform setup.
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
**Context**: The June 12 deployment was incorrectly marked as "resolved" in Session 2995, which only clarified the start time (09:00 UTC). The actual deployment never executed. **AUDIT VERIFIED (Session 3682, 15:50–16:45 UTC)** — Three production-ready audit documents confirm deployment DID NOT execute:
- DEPLOYMENT_JUNE_12_OUTCOME_VERIFICATION.md (204 lines): Verified 0/6 infrastructure checks pass; Docker completely empty; no Nginx, PostgreSQL, API runtime, TLS certs; all endpoints return HTTP 000 (connection refused); confidence 99%
- POST_DEPLOYMENT_ISSUES_ASSESSMENT.md (127 lines): 6 prioritized blockers identified; root cause = platform/runtime decision expired June 15 23:59 UTC with no user response
- DEPLOYMENT_JUNE_12_OUTCOME_VERIFICATION.md (204 lines, Session 3770): 0/6 infrastructure checks pass; Docker completely empty; no Nginx, PostgreSQL, API runtime, TLS certs; all endpoints return HTTP 000; confidence 99%
- POST_DEPLOYMENT_ISSUES_ASSESSMENT.md (127 lines, Session 3770): Root cause identified — ISSUE-3: raspby1 host platform/runtime decision (Docker vs systemd) with deadline June 15 23:59 UTC expired, no user response. Blocks both open-repo AND systems-resilience Phase 5.1 simultaneously.

## Recently Resolved (last 5)
• Usage limits — weekly calibration reminder ← 2026-06-25 00:46 UTC (Session 4247 — orchestrator autonomous resolution)
• stockbot — CRITICAL: Phase 1 validation failure (13:30–13:40 UTC) — real-time stream NOT initialized, sessions timing out ← 2026-06-24 14:00 UTC (Session 4186, orchestrator orientation)
• stockbot — CRITICAL: Container API startup was blocked by missing alembic.ini volume mount ← 2026-06-24 09:48 UTC (Session 4160 — orchestrator autonomous fix + verification)
• stockbot — HMM regime initialization NameError (undefined close_prices variable) ← 2026-06-23 21:22 UTC (Session 4092 — orchestrator autonomous fix + deploy)
• resistance-research — SCOTUS Little v. Hecox deadline passed 18:00 UTC; outcome unverified ← 2026-06-23 18:05 UTC (Session 4084+)

## Inbox (unprocessed)
### [2026-06-30 00:05 UTC] USAGE CALIBRATION RESET — Scheduled for Tuesday reset
**Process on or after June 30 00:00 UTC only.** Usage billing week resets at that time.
Run: `python3 scripts/usage-check.py --calibrate 3.0 67.4`
This restores the June 24 calibration (Sonnet 8,909,833 / all-models 15,140,434). The limits were temporarily inflated to 0.1% on June 27 to allow the orchestrator to run freely during the final days of the billing week. After the reset, actual usage is 0, so the June 24 limits will correctly show 0% and normal threshold monitoring resumes.
**Do not process this item before June 30 00:00 UTC.**

## Recent Log (last 40 lines of WORKLOG.md)
  - KIT_ACCOUNT_SETUP_CHECKLIST.md: Dashboard map, API key location, feature audit
  - WELCOME_SEQUENCE_DRAFT.md: 3 production-ready emails based on Module 14
  - EMAIL_DELIVERABILITY_TEST_RESULTS.md: Pre-execution research + test protocol + known limitations flagged
  - **Critical finding**: Conditional branching likely restricted to paid Creator plan; flagged for user awareness
  - Value: De-risks Phase 2 email platform before user GitHub Pages deployment

- ✅ **Item 23** (mfg-farm) — Test print contingency COMPLETE (commit `f14f9d01`)
  - TEST_PRINT_CONTINGENCY_DECISION_TREE.md: Post-print routing (measure gap, classify failure, execute fix)
  - SNAP_ARM_CAD_MODIFICATION_PROCEDURES.md: Single-parameter edits (30-60s changes, no design work)
  - MATERIAL_SUBSTITUTION_PROTOCOL.md: Thermal profiles (PLA+/PETG/ABS), cost, diagnostic flowchart
  - Value: If test print fails, user has instant iteration playbook (2-3 day cycle vs 5-7 day redesign cycle)

**Parallel Execution Summary**:
- 3 agents in parallel: 20:00–20:12 UTC (12 minutes wall-clock)
- 181,920 subagent tokens total (resistance-research 65K, career-training 62K, mfg-farm 54K)
- 3 commits to master: `31e61f15`, `f74b8f93`, `f14f9d01`
- 9 new files created (3 per item)
- All files production-ready; 0 [TODO] placeholders

**Final System State**:
- **Exploration Queue**: Items 2-4, 8-19, 21-23 complete (18 items); Items 1, 5-7, 14, 16 trigger-dependent (6 items); Item 20 deferred to June 29 13:05 UTC (within 2h pre-checkpoint window per protocol)
- **All major projects**: Correctly blocked on user actions/decisions or time-gates
- **Zero autonomous work**: All immediately-actionable items completed
- **Stockbot checkpoint**: June 29 13:15 UTC (17h 30m away) — all infrastructure ready
- **Usage**: Sonnet 0.2%, All-models 0.1% (well within budget after 3-item execution)

**Recommended Next Actions**:
1. **Immediate (user action)**: Execute Domain 59 Tier 2 sends (25-30 min) before June 30 18:00 UTC deadline
2. **By June 29 07:00 UTC**: Resolve seedwarden Red Clover berberine error (5 min)
3. **June 29 13:05 UTC**: Execute Item 20 (Jetson pre-market audit) if within 2h pre-checkpoint window
4. **Post-user-action**: Phase 1 GitHub Pages push triggers Item 14 analytics framework; test print execution routes to Item 23 contingency playbook


**Session 4473 (2026-06-28 20:31 UTC)** — Orchestrator orientation + seedwarden Red Clover fix
- **Orientation**: ORCHESTRATOR_STATE reviewed. All autonomous work complete (Items A-E from June 27 completed). Zero active work items; all projects blocked on user actions or scheduled events.
- **Seedwarden fix**: Pre-sprint gate deadline (June 29 07:00 UTC). Red Clover photo attribution error resolved (commit 6adce418):
  - Issue: "Habit" image was flower close-up (Böhringer Friedrich CC BY-SA 2.5), duplicate of "Flower head" row
  - Fix: Replaced with full-plant habit image (Leonora Enking CC BY-SA 2.0) showing foliage + flower structure
  - Impact: Phase 3 Medicinal Herbs photo attribution log now complete with proper habit/flower distinction
- **Next action**: June 29 13:15 UTC — Jetson pre-market checkpoint (Item 20, within 2h window). All other work time-gated or awaiting user decisions.
