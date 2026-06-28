# Project Status Report — June 27, 2026

Generated from orchestrator state, PROJECTS.md, per-project planning docs, BLOCKED.md, and direct file inspection.

---

## Quick Reference

| Project | Status | Autonomous Work Available | User Decision Needed |
|---|---|---|---|
| stockbot | Active | Specs implementing now | No |
| resistance-research | Active — user sends pending | No | YES — sends + Gist creation |
| cybersecurity-hardening | Paused (Phase 1 blocked) | YES — threat updates queued | YES — VeraCrypt restart |
| seedwarden | Paused — awaiting approval | No (pending approval) | YES — bundle review |
| mfg-farm | Blocked | No | YES — test print |
| open-repo | Blocked — platform decision | YES — schemas + medical outreach queued | YES — Docker vs systemd |
| systems-resilience | Blocked — platform decision | YES — Phase 5 release queued | YES — platform + Phase 6 status |
| off-grid-living | Complete — Phase 2 ready | YES — signal analysis queued | No |
| career-training | Complete — expansion ready | YES — 3 gap modules queued | No |
| open-source-rideshare | Paused | No | No (user unpause signal) |
| workout | Paused | No | YES — select a plan |
| resume | Paused | No | No (user unpause signal) |

---

## Project Detail

---

### STOCKBOT
**Status**: Active — implementation in progress  
**Priority**: #1 (user-escalated)

**What just happened**: The orchestrator picked up the unpause directive (June 27 ~20:18 UTC, Session 4321) and is implementing two open specs in parallel:
- **LIVE_MONITORING_OPENSPEC Phase 1**: Fixes the `_last_alert` persistence bug (10-min alert cooldown was resetting every cron invocation), adds fill reconciliation vs. Alpaca, daily Discord performance digest, container memory/restart checks, Jetson thermal monitoring (WARN >90°C / CRITICAL >93°C)
- **MODEL_PIPELINE_OPENSPEC Phase 1**: Nightly Optuna TPE model search per ticker (21:15 UTC post-market), per-stock candidate SQLite DB, daily Discord report of best candidate vs. live model — no auto-deploy in Phase 1

**Also queued as prerequisite**: Create `session_signal_snapshots` table via Alembic migration before Monday 13:30 UTC market open (June 29). The entire monitoring/validation framework references this table but it didn't exist in the DB.

**Current live system health**:
- 5 sessions running: JPM ridge_wf, AMZN/AAPL/MSFT/NVDA lgbm_ho
- Container up ~45 hours, WebSocket healthy, no 406 errors
- Account equity: $106,388 | Open positions: 16 | Unrealized P&L: +$8,033
- Last fill: June 22 (no fills since pre-fix period — consistent with low-frequency model behavior)
- Sessions stalled this weekend (normal) — resume Monday 13:30 UTC

**Future work (not yet started)**:
- Phase 3: Exit model training (needs 50+ live round trips — currently 6 fills in 30d, roughly 8 weeks out at current pace)
- Phase 3: MSFT gradient_boosting session (Sharpe 3.190 in backtest)
- Phase 3: Inverse ETF session (PSQ/SH for bear-regime hedge)
- MODEL_PIPELINE Phase 2: Auto-deployment when candidate beats live model on all 6 gates + OOS Sharpe (after Phase 1 validated)

**No user decisions needed** at this time.

---

### RESISTANCE-RESEARCH
**Status**: Active — infrastructure complete, user execution pending  
**Priority**: #2

**What's done**: Phase 2 Waves 1-2 fully executed (June 23). Phase 3 source staging complete for Domains K, H, and 57. T+7 monitoring framework operational. Escalation thresholds built (Item 27).

**What's ready and waiting on you**:

1. **Domain 59 Tier 2 sends** — 3 email templates (EPI, Demos, NELP) are production-ready and personalized. Send window was June 25-30 aligned to Senate Finance CTC markup. Window is **partially elapsed** as of today (June 27). Estimated time: 25-30 minutes. This is time-sensitive.

2. **Domain 51/48 Wave 1 sends** — All templates finalized. Only prerequisite is creating two GitHub Gists (Domain 51 and Domain 48 file names) to include as links. Estimated time: **10 minutes**. Unblocks the entire Wave 1 distribution.

3. **SCOTUS Little v. Hecox** — Execution window closed June 23 18:00 UTC without you verifying the outcome. The rapid-response infrastructure remains production-ready for retroactive use if the outcome is still actionable.

**No autonomous work available** beyond what's already complete — this phase is entirely user-execution.

**Future work**: Phase 3 (Domains K, H, 57 — November 4 launch timeline) is fully staged with source databases, expert contacts, and research runbooks. No action needed until after Wave 1 sends complete.

---

### CYBERSECURITY-HARDENING
**Status**: Paused at Phase 1 Step 1.3  
**Priority**: #3

**Where we stopped**:
- ✅ 1.1 Signal — complete
- ✅ 1.2 iPhone tracking — steps 1-3 done; Step 4 (Advanced Data Protection) was pending a 24-48hr Apple security delay
- 🔄 1.3 VeraCrypt — **needs you to restart Windows**, type the pre-boot password, let Windows load normally, then click Encrypt to begin background encryption
- ⏳ 1.4 Ente Auth (install, switch email + financial accounts off SMS 2FA, set carrier SIM PIN)
- ⏳ 1.5 Bitwarden password manager
- ⏳ 1.6 Data broker opt-outs (10 sites + 3 federal, ~45 min)
- ⏳ 1.7 iPhone passcode over Face ID (5 min)

**Autonomous work now queued** (independent of Phase 1): Threat currency updates to all 6 Phase 2 playbooks — Thomson Reuters CLEAR status, Chatrie geofence ruling footnote, Flock Safety litigation update. These don't require Phase 1 to be complete.

**Phase 2** (LUKS2 full-disk encryption on Linux, backup automation, provisioning hardening) is fully planned and production-ready. 3 spec docs committed. Estimated 15 step-by-step procedures ready to execute once Phase 1 is done.

---

### SEEDWARDEN
**Status**: Paused — awaiting content approval  

**What's ready**: Q3 medicinal bundles (5 total) are production-ready with vendor verification, CITES compliance, and unit economics ($3.40-$4.10 COGS). Content has been sitting since June 23.

**What needs you (~2 hours total)**:
1. **Review and approve the 5 Q3 bundle drafts** (~30-45 min). Once approved, Canva design work (4-5h) and launch execution are fully autonomous.
2. **Send 11 contractor outreach emails** (~30-45 min) — templates pre-written, contacts verified. This gates the Phase 3 contractor selection.
3. After above: staggered **publish Q3 bundles starting June 29** per the launch checklist.

**Also ready**: Rare plants market research is complete (RARE_PLANTS_MARKET_RESEARCH.md). Three high-value outreach targets identified (NC Botanical Garden, Missouri Botanical Garden, United Plant Savers) with templates written. ~30 min of your time to send.

**Q4 strategy** is research-complete and decision-ready. October launch for Q4-A, November 1 for Q4-D.

---

### MFG-FARM
**Status**: Blocked on physical user action

**What's done**: All pre-print deliverables complete — ModRun cable clip CAD designs, Etsy listing copy, supplier scorecard, production cost model, Q3 library (23 SKUs), Phase 2 supply chain research (34 vendors).

**What needs you**: Execute one test print.
- Settings: 0.20mm layer height, PLA+, 3 walls, 220-225°C
- Evaluate snap-arm clearance (1.4mm is the highest-risk feature)
- Report pass/fail back (by message or editing test-print-results/)

That result unblocks Phase 2 Tracks 2-4. Nothing can proceed until it exists.

---

### OPEN-REPO
**Status**: Blocked — platform decision expired June 15  

**What's done**: Code is 100% merge-ready (51 ZIM tests passing). Full infrastructure audit confirmed 0/6 production checks pass — Docker is empty, no Nginx, no PostgreSQL, no API runtime, no TLS certs. June 12 deployment never happened.

**Autonomous work now queued**: Phase 5.2 Wave 0 schema design (5 content-type schemas) and medical reviewer outreach draft — both can proceed independently of the deployment decision.

**What needs you**: See Decision #1 below.

**Future work once deployed**: Phase 5.2 Waves 1-3 (medical reference, water systems, seed preservation, food preservation, botanical knowledge) — all staged and ready. ~55-75 hours of implementation work gated behind deployment.

---

### SYSTEMS-RESILIENCE
**Status**: Blocked — platform decision expired; Phase 6 status unclear  

**What's done**: Phase 5 integrated corpus (45,380 words across 5 Wave documents) is production-ready since June 1. GitHub release was staged for June 5 but may not have been published — the orchestrator will verify before executing the release.

**Key finding**: Auto-fallback was activated June 1 (confirmed in PHASE_5_6_EXECUTION_SUMMARY.md). This means Phase 6 Domain A research was supposed to begin autonomously. Current status of that execution is unknown — the orchestrator has not been running since June 25.

**Autonomous work now queued**: Phase 5 GitHub release (v5.0-wave-1-2-production) — will verify first to avoid duplicate publication.

**What needs you**: See Decision #1 (same raspby1 platform decision as open-repo) and Decision #5 below.

---

### OFF-GRID-LIVING
**Status**: Complete (Phase 1) — Phase 2 not yet started  

**What's done**: All 17 domain documents published to GitHub (April 26). Social media distribution toolkit is production-ready.

**What's queued**: Phase 2 signal analysis — review GitHub issues/traffic/community comments to rank which domains need deepening. Output: ranked list of top 3-5 content expansion candidates.

**What needs you**: Execute the social media distribution per `social-media-execution-toolkit.md`. This is user-execution only; the toolkit is already written.

---

### CAREER-TRAINING
**Status**: Complete — expansion not yet started, not in orchestration queue

**What's done**: 33 modules (~336,000 words) + 150-scenario case-study workbook (~121,000 words). Full curriculum from industrial GC foundations through residential specialty, California-specific throughout.

**Critical gap**: This project has been **invisible to the orchestrator** — it's not in the PROJECTS.md priority list.

**What's queued**: 3 gap modules (each ~10K words) + deployment infrastructure:
- Module 34: Residential Scheduling Practice (Last Planner System, 3-week lookahead)
- Module 35: Safety Program Construction (IIPP writing, toolbox talks, incident response)
- Module 36: Construction Insurance Program Design (COI reading, OCIP/CCIP, builder's risk, E&O)
Plus: GitHub Pages deployment plan + distribution channel activation

**No user decisions needed** — all 3 modules are fully scoped with success criteria in module-gap-analysis.md.

---

### OPEN-SOURCE-RIDESHARE
**Status**: Paused — awaiting your unpause signal. No autonomous work queued.

### WORKOUT
**Status**: Paused — comprehensive plan (1,053 lines, 3 equipment tiers, full progression) is complete. Needs you to select a plan and start. No autonomous work available.

### RESUME
**Status**: Paused — awaiting your unpause signal.

---

## Decisions You Need to Make

---

### DECISION 1 — raspby1 Platform Choice (unblocks open-repo AND systems-resilience simultaneously)

**What it is**: Both open-repo and systems-resilience need to deploy to raspby1 (your Pi). Nothing can deploy until you choose how.

**Option A: Docker**
- Pros: Clean isolation, easy rollback, matches Jetson production setup, well-documented
- Cons: ~3-4h setup time, Pi 5 RAM pressure if running multiple containers
- Estimated effort: 3-4h autonomous orchestrator work after your decision

**Option B: systemd + venv**  
- Pros: Lighter on RAM, simpler for a Pi, faster to set up
- Cons: Less isolation, manual dependency management, harder to rollback
- Estimated effort: 2-3h autonomous orchestrator work after your decision

**Recommendation: Docker.**  
You already run Docker on Jetson for stockbot and it's working well. Keeping the same runtime across both machines reduces your mental overhead and makes incident response simpler — you already know Docker's operational model. The RAM concern is real but the Pi 5 (8GB) should handle it fine for what's being deployed. The 1 extra hour of setup is worth the consistency.

---

### DECISION 2 — Platform for open-repo Content (Nextcloud+Matrix vs Discourse)

**What it is**: The open-repo project needs a platform for hosting community content and discussion on raspby1.

**Option A: Nextcloud + Matrix**  
- Pros: Full data sovereignty, works offline, no corporate dependency, integrates with your existing setup
- Cons: Higher maintenance burden, less familiar UX for casual visitors, IPv6 bug noted on Pi 5
- Score from prior analysis: 8/10

**Option B: Discourse**
- Pros: Best-in-class community forum UX, strong SEO, easy for new users
- Cons: Heavier resource usage, Pi 5 IPv6 bug documented (same issue as Nextcloud), less aligned with off-grid/sovereignty philosophy of the project
- Score from prior analysis: 5/10

**Recommendation: Nextcloud + Matrix.**  
The project's own philosophy is data sovereignty and community resilience. Running Discourse (which ultimately depends on corporate infrastructure for updates and plugins) contradicts the project's stated values. The IPv6 bug affects both options equally so it's not a differentiator. Nextcloud + Matrix also integrates with seedwarden's distribution and your existing communication stack.

---

### DECISION 3 — Resistance-Research: Domain 59 Sends (time-sensitive)

**What it is**: 3 emails to EPI, Demos, and NELP aligned to the Senate Finance Committee CTC markup window (June 25-30). Templates are production-ready and personalized.

**The decision**: Do you want to send them? Window closes June 30. Today is June 27 — 3 days left.

**Recommendation: Send today.**  
The window is almost closed. Even if the markup timing has shifted slightly, these organizations operate on rolling engagement windows — a send on June 27 vs June 25 is not materially different. The cost of not sending is losing this alignment opportunity entirely. Estimated time: 25-30 minutes. The templates are copy-paste ready.

---

### DECISION 4 — Resistance-Research: GitHub Gist Creation for Wave 1 Sends

**What it is**: Creating 2 GitHub Gists (one for Domain 51 content, one for Domain 48 content) to include as links in the Wave 1 send templates. Without these, the sends can't go out.

**The decision**: Create the Gists. Estimated time: 10 minutes.

**Recommendation: Do it now.**  
This is a 10-minute mechanical task that unlocks the entire Wave 1 distribution. There's no meaningful downside. The content is finalized and committed. This should happen in the same session as Decision 3.

---

### DECISION 5 — Systems-Resilience Phase 6 Status Check

**What it is**: Auto-fallback was activated June 1, meaning Phase 6 Domain A research was supposed to begin executing autonomously. The orchestrator has been paused since June 25, so the last 2 days are a gap — but the prior 24 days should have seen activity.

**The decision**: Do you know whether Phase 6 Domain A research actually ran? If yes, what's the status? If no, it needs to be restarted.

**Recommendation**: The orchestrator should verify this as its first systems-resilience action. If Domain A research ran, commit whatever was produced and move to Domain B. If it didn't run (e.g., because the orchestrator spent those sessions on standby instead of this work), it needs to be explicitly queued. I'll flag this for the orchestrator to investigate and report back.

---

### DECISION 6 — Seedwarden Q3 Bundle Review (30-45 min)

**What it is**: 5 medicinal bundle drafts are sitting approved-pending-review since June 23. Your review unlocks 4-5 hours of autonomous Canva design work and the July 1 launch.

**The decision**: Set aside 30-45 minutes to review the bundle content at `projects/seedwarden/Q3_MEDICINAL_BUNDLES_COMPLETION_TRACKER.md`.

**Recommendation: Do this weekend.**  
The July 1 launch date is 4 days away. If design work (4-5h) doesn't start by Sunday, the launch slips to the following week. The bundles have been ready for 4 days. This is the highest-leverage 45 minutes available to you across all projects right now.

---

### DECISION 7 — VeraCrypt Pre-Boot Test (15 min)

**What it is**: You installed VeraCrypt and ran the encryption wizard. The last step before background encryption begins is: restart Windows, type the pre-boot password when prompted, let Windows boot normally, then click Encrypt in VeraCrypt. Background encryption then runs without interruption.

**Recommendation: Do this at your next Windows session.**  
It's a 15-minute task that's been blocked for weeks. Phase 2 (full Linux disk encryption, backup automation) cannot start until Phase 1 is done. The security posture improvement is material.

---

### DECISION 8 — Mfg-Farm Test Print

**What it is**: Print one ModRun cable clip at 0.20mm layer height, PLA+, 3 walls, 220-225°C and report whether the 1.4mm snap-arm clearance passes.

**Recommendation: Next time you're near the printer.**  
This is a physical action with no prep needed — all CAD files and settings are documented. The entire Phase 2 supply chain and production scale-up is gated on this single print.

---

## What the Orchestrator Is Doing Right Now

As of June 27 ~20:18 UTC (Session 4321), the orchestrator picked up the inbox directive and is running:
- 2 parallel stockbot agents (LIVE_MONITORING_OPENSPEC + MODEL_PIPELINE_OPENSPEC)
- Expected completion: ~2-3 hours

Next inbox items queued (Items A-E) will be picked up in the following session(s):
- A: cybersecurity-hardening threat currency updates
- B: open-repo Phase 5.2 Wave 0 schema design + medical reviewer outreach
- C: off-grid-living Phase 2 signal analysis
- D: systems-resilience Phase 5 GitHub release (with pre-check)
- E: career-training gap modules (3x ~10K words) + deployment plan

---

*Report generated June 27, 2026. Next update recommended after: stockbot spec implementation completes, systems-resilience Phase 6 status verified, and user completes Decisions 3-4 (resistance-research sends).*
