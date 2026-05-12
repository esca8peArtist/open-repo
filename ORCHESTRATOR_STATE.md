# Orchestrator State
> Auto-generated at 2026-05-12T19:01:27Z — do not edit. Source: PROJECTS.md, WORKLOG.md, BLOCKED.md, INBOX.md.

## Usage
🟢 Usage: Sonnet 66.7% (870,186 tokens) | All-models 4.3% | Reset in 149h | check: claude.ai → Settings → Usage & billing

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
**Focus**: Session 938: All pre-print deliverables complete — designs (`modrun_rail.py`, `modrun_clip.py`), listing copy, supplier scorecard, production cost model. **Blocking gate**: test print at 0.20mm layer height, PLA+, 3 walls, 220–225°C — evaluate snap-arm FDM_TOLERANCE (1.4mm is highest-risk feature). Post-print: Etsy listing + supplier negotiation (all materials ready in project dir).
**Blocked**: Test print (user action required — see focus above)

### resistance-research
**Status**: Active — Phase 1-5 COMPLETE, **36-Domain Diagnostic Framework + Phase 2 Expansion COMPLETE** (Sessions 502-524, Session 907) — Core proposal architecture complete, completeness assessment done, all 35+ domain documents verified production-ready, distribution infrastructure finalized (Session 520), April-May 2026 domain updates + tracker maintenance current (Sessions 521, 524, 876, 907)
**Focus**: Session 938: 38+ domains production-ready (Phase 1+2 complete, trackers current May 9). Domain 42 DEA hearing deadline May 28. **Blocked**: user distribution path decision — A / A+37 (recommended) / B.
**Blocked**: User distribution path decision (A / A+37 / B)

### cybersecurity-hardening
**Status**: Active — **TIER 1, 2, 3 DISTRIBUTION PREP + TIER 2 MESSAGING TEMPLATES COMPLETE** (Sessions 465, 497, 499), ready for user execution
**Focus**: Session 938: Phase 2 Scenario Playbooks complete (all 4 playbooks, May 2026 threat intel). Phase 1 Tier 1 infrastructure ready (25 contacts verified, 7-week timeline). **Blocked**: user approval for Phase 1 launch + Day 1 send date.
**Blocked**: None — Phase 1 ready for user approval and execution

### stockbot
**Status**: Active — **2-session Jetson-only architecture (AAPL lgbm_ho + AAPL ridge_wf)**. Reduced from 67 sessions. 19 positions closing May 5 13:30 UTC open. AAPL (108 shares, +$924 unrealized) stays open.
**Focus**: Session 938: ARCH cleanup deployed (AAPL lgbm_ho + ridge_wf running on Jetson). Gate 1 checkpoint May 12 20:00 UTC — classify outcome per MAY_12_OUTCOME_ROADMAP.md. Gate 2 prep follows checkpoint. Cron PATH fix + Jetson disk cleanup required before Gate 2 deployment.
**Blocked**: Cron PATH fix + Jetson disk cleanup required before Gate 2 deployment (see BLOCKED.md)

### seedwarden
**Status**: Active — Phase 1 upload pending user tag corrections; **Phase 2 execution ready (May 30 launch target)**; **Phase 3 execution-layer assets COMPLETE (June 15–July 1 launch ready)**
**Focus**: Session 938: Phase 3 execution assets complete — 7 production-ready files (execution guide, Canva briefs, broadcast sequence, social templates, KPI dashboard, landing pages). Phase 2 target May 30, Phase 3 June 15–July 1. Track B unblocked. **Blocked (Track A)**: tag corrections + Etsy account verification.
**Blocked**: Tag corrections + Etsy account verification (user action, Track A only). Track B has no blockers.

### open-repo
**Status**: Active — Phase 4 COMPLETE, **PR #1 open, awaiting review/merge** (Session 486: 2026-04-26)
**Focus**: **PR #1 OPEN** (2026-04-26): https://github.com/esca8peArtist/open-repo/pull/1

### off-grid-living
**Status**: Complete — **publication complete** (GitHub live, awaiting user execution of social media distribution)
**Focus**: Session 938: GitHub publication complete. Social media execution toolkit ready (`social-media-execution-toolkit.md`). No further autonomous work available — awaiting user execution of distribution plan.

### workout
**Status**: Active
**Focus**: `comprehensive-plan.md` (1,053 lines) complete — covers all 3 equipment tiers (no equipment, bands, full gym) × multiple frequencies (3/4/5/6 days), with full exercise libraries, progression systems, calisthenics skill ladders, and mobility protocols. Awaiting user review and selection.
## Active Blocks
### Usage limits — weekly calibration reminder
**Date blocked**: 2026-05-12 (auto-added each Tuesday by reset-usage-budget.sh)
**Context**: Plan limits reset today. Token limits in usage-check.py are calibrated estimates that drift over time. Verify against actual UI percentages.
**What I need**: Check claude.ai → Settings → Usage & billing. Run: `bash scripts/verify-calibration.sh <sonnet_pct> <all_pct>`
**Verify with**: `bash scripts/verify-calibration.sh`
**Resolution**:
---
### stockbot — Manual DB sync verification (May 11 cron PATH issue, action window passed)
**Date blocked**: 2026-05-09
**Date superseded**: 2026-05-12 (relevance audit)
**Context**: Originally flagged because Jetson nightly DB sync via cron was not running (PATH env var not set in crontab, so `sync_db_from_alpaca.py` couldn't find `uv` binary). Action window was May 11 evening / May 12 morning before the 20:00 UTC checkpoint. Time has now elapsed. AAPL time-stop SELL was expected to fire May 11–13 (h+10).
**What I need (revised)**: At 20:00 UTC checkpoint today, verify whether the AAPL h+10 SELL fill (if it occurred) is in trading.db. If absent, run `uv run python scripts/sync_db_from_alpaca.py --since 2026-04-29 --db database/trading.db` immediately before classifying outcome. Permanent cron PATH fix is still needed to prevent recurrence — track separately as ongoing infrastructure issue.
**Verify with**: `ssh user@jetson "crontab -l | grep -E 'PATH|sync_db'"` (must show PATH line at top of crontab, then sync_db entry)
**Resolution**: PENDING — depends on user verification at 20:00 UTC checkpoint. Move to Resolved Archive after checkpoint runs.
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

## Recently Resolved (last 5)
• stockbot — Database persistence gap blocks May 12 checkpoint time-stop exit logic ← 2026-05-09 (Session 922)
• stockbot — Docker API container stuck in initialization loop; HTTP endpoint unreachable ← 2026-05-09 (Session 919)
• stockbot — Engine API auth failed; database partially recovered; checkpoint at risk ← 2026-05-09 (Session 911)
• stockbot — Architecture decisions from full code review (ARCH-1 through ARCH-7) ← 2026-05-08
• stockbot — Alpaca DTBP=0; waiting for May 6 market open reset ← 2026-05-06 09:56 UTC (Session 819)

## Inbox (unprocessed)
- [WEEKLY-MAINTENANCE] Prune PROJECTS.md: trim each project's 'Current focus' to ≤2 paragraphs / 500 chars. Review quiescent projects (workout, off-grid-living, resume, open-repo) — pause any with no active work this week. Archive any BLOCKED.md Resolved Archive entries older than 30 days.
*(no new items)*

## Recent Log (last 40 lines of WORKLOG.md)

**Trigger**: User requested cleanup and relevance audit of orchestrator state (date 2026-05-12).

**Scope**: Read all state files (PROJECTS.md, INBOX.md, ORCHESTRATOR_STATE.md, BLOCKED.md, CHECKIN.md, recent WORKLOG), assess each block and project status against today's date, process the INBOX Path Model item, refresh stale entries.

### Findings

1. **Stockbot architecture cleanup landed today** (commit `2372f1d` in submodule, 2026-05-12 02:11 UTC). Resolved ARCH-1 (RiskManager wired into TradingSession, LiveEngine deleted), ARCH-2 (risk thresholds extracted), ARCH-4/6/7, M5/7/8. Container restarted on Jetson and confirmed healthy. ORCHESTRATOR_STATE.md still showed "May 5 13:30 UTC" stale focus — refreshed.

2. **DB sync block** (May 11 cron PATH issue) past its action window. Reframed as 20:00 UTC checkpoint-time verification rather than pre-emptive block. Permanent cron PATH fix tracked as ongoing infrastructure issue.

3. **Session 937 "Jetson unreachable" + "ridge_wf placeholder" critical alerts** are no longer current — confirmed by today's healthy container restart on Jetson.

4. **INBOX Path Model item** moved to stockbot Exploration Queue with full design scope (LSTM/Transformer for 63-day daily price PATH prediction, complementing the Return Forecast Engine's endpoint-only output). Source attribution preserved.

5. **mfg-farm test print** block unchanged (still genuinely the gating user action since 2026-04-12).

6. **stockbot Jetson disk at 87%** kept active — relevant after May 12 checkpoint per its own resolution criteria.

### Files modified

- `INBOX.md` — Path Model cleared, processing note added
- `PROJECTS.md` — Path Model added as Session 938 stockbot exploration item; header date refreshed
- `ORCHESTRATOR_STATE.md` — Full rewrite; stockbot status reflects today's architecture cleanup deployment; blocks pruned
- `BLOCKED.md` — DB sync block reframed as superseded
- `CHECKIN.md` — Session 938 audit entry appended (top)
- `WORKLOG.md` — This entry appended

### What is genuinely actionable today

In time order:
1. **TODAY 20:00 UTC**: Run stockbot Gate 1 checkpoint query, classify outcome, follow `MAY_12_OUTCOME_ROADMAP.md`. If AAPL h+10 SELL fill missing from `database/trading.db`, run manual sync first.
2. **By May 28**: Resistance-research distribution path decision (16 days to DEA Domain 42 deadline)
3. **When ready**: Cybersecurity Phase 1 Tier 1 launch approval
4. **No deadline**: Mfg-farm test print, seedwarden plant orders + photography window confirmation

### Next session

Pick up after 20:00 UTC checkpoint to classify outcome, archive resolved DB sync block, and execute post-checkpoint roadmap (`POST_CHECKPOINT_ARCHITECTURE_ROADMAP.md`).
