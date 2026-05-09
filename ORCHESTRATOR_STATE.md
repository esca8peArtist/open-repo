# Orchestrator State
> Auto-generated at 2026-05-09T15:25:55Z — do not edit. Source: PROJECTS.md, WORKLOG.md, BLOCKED.md, INBOX.md.

## Usage
🟢 Usage: Sonnet 58.9% (1,095,745 tokens) | All-models 52.5% | Reset in 57h | check: claude.ai → Settings → Usage & billing

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
### mfg-farm
**Status**: Active — ready to prototype
**Focus**: Session 291: **Business plan COMPLETE** (`business-plan.md`). **CadQuery parametric designs COMPLETE** (`cadquery/modrun_rail.py`, `cadquery/modrun_clip.py`). Market research + competitive analysis complete (`market-research.md`). Etsy and Amazon listing copy complete (`etsy-listing-modrun.md`). **P
**Blocked**: Test print (user action required — see focus above)

### resistance-research
**Status**: Active — Phase 1-5 COMPLETE, **36-Domain Diagnostic Framework + Phase 2 Expansion COMPLETE** (Sessions 502-524, Session 907) — Core proposal architecture complete, completeness assessment done, all 35+ domain documents verified production-ready, distribution infrastructure finalized (Session 520), April-May 2026 domain updates + tracker maintenance current (Sessions 521, 524, 876, 907)
**Focus**: **Session 907 (2026-05-09): May 2026 Tracker Maintenance COMPLETE + Phase 2 Domain 39 (Immigration Enforcement & Detention Infrastructure) COMPLETE**. 
**Blocked**: User distribution path decision (A / A+37 / B)

### cybersecurity-hardening
**Status**: Active — **TIER 1, 2, 3 DISTRIBUTION PREP + TIER 2 MESSAGING TEMPLATES COMPLETE** (Sessions 465, 497, 499), ready for user execution
**Focus**: **Session 905 (2026-05-09): Phase 2 Scenario Playbooks COMPLETE** (Commit ae86d735). Phase 2 research infrastructure now 100% ready:
**Blocked**: None — Phase 1 ready for user approval and execution

### stockbot
**Status**: Active — **2-session Jetson-only architecture (AAPL lgbm_ho + AAPL ridge_wf)**. Reduced from 67 sessions. 19 positions closing May 5 13:30 UTC open. AAPL (108 shares, +$924 unrealized) stays open.
**Focus**: 🔴 MAY 12 CHECKPOINT PREPARATION — COMPLETE (Session 922)
**Blocked**: Engine restart (user action — before 2026-04-28 09:30 ET, CRITICAL)

### seedwarden
**Status**: Active — Phase 1 upload pending user tag corrections; **Phase 2 execution ready (May 30 launch target)**; **Phase 3 execution-layer assets COMPLETE (June 15–July 1 launch ready)**
**Focus**: **Session 907 (2026-05-09): Phase 3 Asset Completion COMPLETE**. 
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
### stockbot — Manual DB sync required on May 11 before checkpoint (cron PATH broken)
**Date blocked**: 2026-05-09
**Context**: Jetson nightly DB sync via cron is not running. Root cause: `PATH` environment variable not set in crontab, so `sync_db_from_alpaca.py` cannot find `uv` binary. The AAPL time-stop exit is expected to fire on May 11 (h+10 trigger). If the sync doesn't run, the May 12 checkpoint query will show 0 confirmed round trips even if the SELL fill executed. Database must be manually synced on May 11 evening or May 12 morning before the 20:00 UTC checkpoint query.
**What I need**: On May 11 evening (after market close ~20:00 UTC) or May 12 morning, manually run: `uv run python scripts/sync_db_from_alpaca.py --since 2026-04-29 --db database/trading.db` to capture the time-stop SELL fill if it fired.
**Verify with**: `crontab -l | grep sync_db` should show PATH=/... at top, then sync_db_from_alpaca.py entry with proper path. Command to test: `ssh user@jetson "crontab -e && add PATH=/home/awank/.local/bin:/usr/local/bin:/usr/bin:/bin"`
**Resolution**:
### mfg-farm — Test print required before launch prep continues
**Date blocked**: 2026-04-12
**Context**: Business plan, CadQuery designs (modrun_rail.py, modrun_clip.py), market research, and listing copy are all complete. Orchestrator cannot proceed with launch prep until a physical test print confirms the designs are printable.
**What I need**: Run a test print of the CadQuery rail and clip designs and confirm they printed correctly.
**Verify with**: `# manual — cannot auto-verify`
**Resolution**:
### stockbot — Jetson disk at 87% (29 GB free remaining)
**Date blocked**: 2026-05-09
**Context**: Jetson root filesystem is at 87% capacity (188 GB of 227 GB used, 29 GB free). Root causes: /var/log at 74 GB, Docker build cache at 22.66 GB (6 GB reclaimable). This is NOT a May 12 checkpoint blocker — 29 GB is sufficient for 3 days of trading logs. However, disk must be cleaned before Gate 2 deployment to prevent crashes due to log rotation failures or container failures.
**What I need**: After May 12 checkpoint, clean up: (1) identify and archive old logs in /var/log (keep last 7 days), (2) run `docker builder prune` to reclaim build cache, (3) verify free space ≥50 GB before Gate 2 work.
**Verify with**: `ssh user@jetson "df -h / && du -sh /var/log && docker system df"`
**Resolution**:

## Inbox (unprocessed)
*(no new items)*

## Recent Log (last 40 lines of WORKLOG.md)
- Research: Examined SCENARIO_PLAYBOOK_INDEX.md, existing Tier 1/2 materials
- Deliverable: `projects/cybersecurity-hardening/TIER_2_PILOT_LAUNCH_READINESS.md` (17 KB, 5 sections)
- Content: 8-week pilot plan (3-5 organizations), success metrics (60%+ adoption), parallel prep timeline, contingency plans
- Pilot cohort: FPF (Playbook 5, journalist security), NLG (Playbook 3, activist organizing), CLS (Playbook 1, immigration evasion)
- Key insight: Parallel preparation during Phase 1 (Weeks 1-3) compresses overall timeline by 2 weeks
- Committed to master (commit b8497cbd)

### Other Commits
1. **Domain 53 — Mutual Aid Networks** (6,800 words, Phase 2 expansion) committed to master (commit d8f04754)
2. **stockbot checkpoint artifacts** (GATE_1_CHECKPOINT_VALIDATION.md, JETSON_RESILIENCE_ASSESSMENT.md, POST_GATE_1_ROADMAP_v2.md) committed to submodule
3. **EXPLORATION_QUEUE.md** created and updated (commit 1dd83b71, 86484e4e)
4. **CHECKIN.md** session summary (commit f980c53c)

### Total Effort
- Research + writing: 8.5 hours
- Document output: 7.5+ KB across 3 projects
- Commits: 6 commits on master + 1 on stockbot submodule

### What's Ready for User Input

1. **resistance-research**: Distribution guide ready for all 3 paths → user chooses → orchestrator executes immediately
2. **stockbot**: May 12 checkpoint prep complete; May 11 manual DB sync needed (user action); post-Gate-1 architecture plan ready
3. **cybersecurity-hardening**: Tier 2 pilot plan ready for launch immediately after Phase 1 approval

### Critical Dates Ahead

- **May 11 evening**: Manual stockbot DB sync required (Jetson cron PATH still unfixed)
- **May 12 20:00 UTC**: stockbot Gate 1 checkpoint execution (3 days away)
- **May 28**: resistance-research Domain 42 + Domain 37 Congressional submission deadline (if Path A+37 chosen)
- **May 30**: seedwarden Phase 2 launch target (user action items: photo logistics, Kit setup, Canva design)

### Project Status Summary (No Changes)
- **stockbot**: Checkpoint prep COMPLETE; May 11-12 user actions required
- **resistance-research**: Phase 1 COMPLETE, Domain 53 COMPLETE, execution plans READY; distribution path decision needed
- **cybersecurity-hardening**: Phase 1+2 COMPLETE, Tier 2 pilot plan READY; Phase 1 approval needed
- **mfg-farm**: All pre-production COMPLETE; test print blocker remains
- **seedwarden**: Phase 2 READY; user action items identified (photos, Kit, Canva)

---
