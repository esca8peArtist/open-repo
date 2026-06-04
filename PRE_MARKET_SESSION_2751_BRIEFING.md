---
title: Pre-Market Session 2751 Briefing — June 4, 11:00 UTC
prepared: 2026-06-04 08:30 UTC (Session 2750)
deadline: 2026-06-04 13:30 UTC (Market Open)
purpose: Execute pre-market health checks, manage decision points, verify market readiness
---

# Pre-Market Session 2751 Briefing

**Session Time**: 11:00–13:00 UTC (2 hours)
**Critical Deadlines**: 13:00 UTC (Seedwarden decision) → 13:30 UTC (Market open)

## Status Overview

### ✅ Completed Work (Session 2750)
- **Item 58 COMPLETE**: stockbot Market Execution Runbook delivered
  - 3 production-ready documents (63K total content)
  - Covers June 4-10 trading period
  - Date corrections applied (Day 1 = June 4)
  - WebSocket 406 error handling included
  - All contingencies documented (IEX/SIP/REST-only)
  - Ready for immediate use at market open

### 🔴 User Decisions Still Pending
1. **Seedwarden Track A/B/Both** (Deadline: 13:00 UTC)
   - No user response received yet
   - Orchestrator will activate **Track B at 13:00 UTC** if no decision
   - Track B activation script prepared: `TRACK_B_ORCHESTRATOR_ACTIVATION_June4_1300UTC.md`
   - Track B timeline: Gates 1-5 (user actions) + autonomous pre-launch → Launch day June 5

2. **Systems-resilience Platform** (Deadline: EOD, lower priority)
   - No user response received yet
   - Will default to Nextcloud+Matrix if not specified
   - Does not block any critical work for today

### 🟢 Stockbot Status
- Trading sessions verified operational (JPM ridge_wf + AMZN lgbm_ho)
- Both sessions sleeping until 13:15 UTC pre-market wake
- Database directory issue fixed (Session 2745)
- Market execution runbooks ready
- Known issue: WebSocket 406 error as of 02:06 UTC restart (must verify cleared by 13:15 UTC)

---

## Session 2751 Tasks (11:00–13:00 UTC)

### Task 1: Pre-Market Health Checks (11:00–12:30 UTC, ~90 minutes)

**Objective**: Verify all systems ready for 13:30 UTC market open

**Checks to run** (from MARKET_EXECUTION_WEEK_1_RUNBOOK.md Pre-Market Checklist):

1. **Jetson SSH Reachability** (13:00 UTC — do NOT run early, matches runbook timeline)
   ```bash
   ssh awank@100.120.18.84 "echo JETSON_OK && uptime && date -u"
   ```
   Expected: `JETSON_OK` on first line, date shows June 4

2. **Docker Container Running** (13:01 UTC)
   ```bash
   ssh awank@100.120.18.84 "docker ps | grep stockbot && docker inspect --format='{{.State.Status}} restarts={{.RestartCount}}' stockbot"
   ```
   Expected: `running` status

3. **WebSocket Feed Healthy** (13:02 UTC) — CRITICAL
   ```bash
   ssh awank@100.120.18.84 "docker logs stockbot --tail=50 2>&1 | grep -E 'started stocks|starting stocks websocket|connection limit exceeded|406|409'"
   ```
   Success indicators: `started stocks stream`, `starting stocks websocket`, `data_feed=iex`
   If 406 present: Execute Contingency 6 (120-second stop/wait/start recovery)

4. **Alpaca API Connectivity** (13:05 UTC)
   ```bash
   ssh awank@100.120.18.84 "curl -s -H 'APCA-API-KEY-ID: $(grep ALPACA_API_KEY_ID /opt/stockbot/.env | cut -d= -f2)' https://paper-api.alpaca.markets/v2/account | python3 -c 'import sys, json; print(json.load(sys.stdin).get(\"portfolio_value\", \"ERROR\"))'"
   ```

5. **Trading Sessions Status** (13:10 UTC)
   ```bash
   ssh awank@100.120.18.84 "docker logs stockbot --tail=100 2>&1 | grep -E 'Session.*Market|woke from sleep' | tail -5"
   ```

6. **AMZN Stale DB Position Reconciliation** (13:12 UTC) — REQUIRED PRE-OPEN
   - Sessions may have stale OPEN record for AMZN from June 1-3
   - Query: Check Alpaca positions match database
   - If mismatch: Update database to reflect zero open position for AMZN

**Decision Gate** (13:15 UTC):
- If ALL checks PASS → **GO** (proceed to market open)
- If ANY check FAIL → **NO-GO** (escalate, troubleshoot, or defer to June 5)
- Record decision in WORKLOG.md

### Task 2: Seedwarden Decision Point Management (13:00 UTC)

**Objective**: Execute Track B activation if no user decision received

**Pre-Execution Check** (13:00 UTC sharp):
1. Read CHECKIN.md top section — is there a user decision on seedwarden Track A/B/Both?
2. Read INBOX.md — any last-minute seedwarden clarification?
3. Check git log for recent user commits

**If user decision found**:
- Follow user guidance (activate Track A, Track B, or Both as specified)
- Update PROJECTS.md focus line accordingly
- Log decision in CHECKIN.md

**If NO user decision found**:
- Execute `TRACK_B_ORCHESTRATOR_ACTIVATION_June4_1300UTC.md` steps 1-4 (~5 min)
  - Update PROJECTS.md seedwarden focus line
  - Update BLOCKED.md if decision block exists
  - Update CHECKIN.md with decision record
  - Commit with message: `chore(orchestrator): Track B activated at 13:00 UTC (decision deadline passed)`

**Post-Activation**:
- User must complete Gates 1-5 per READINESS_REPORT_JUNE_1.md
- Priority: Gate 4 (upload 8 PDFs to Google Drive, 20 min, critical path)
- Launch day: June 5, 07:30 UTC

### Task 3: Final Market-Open Readiness (13:15–13:30 UTC)

**Objective**: Confirm all systems ready for trading

**Final Checks**:
1. Verify pre-market health checks PASSED
2. Confirm trading sessions ready to wake at 13:30 UTC
3. Verify market is actually open (NYSE 13:30 UTC = 08:30 ET)
4. Confirm Alpaca connectivity stable

**Market Open Procedure** (13:30 UTC):
- Sessions wake automatically (scheduled wake time)
- Monitor docker logs for trading session startup messages
- Confirm first signal evaluations begin

---

## Key Files to Reference During Session

1. **Market Execution Runbook**: `projects/stockbot/MARKET_EXECUTION_WEEK_1_RUNBOOK.md`
   - Pre-market checklist (lines 50-100)
   - Contingency paths (if needed)

2. **Seedwarden Track B Activation**: `projects/seedwarden/TRACK_B_ORCHESTRATOR_ACTIVATION_June4_1300UTC.md`
   - Full activation script with step-by-step instructions

3. **Go/No-Go Decision Template**: `projects/stockbot/JUNE_4_10_GO_NO_GO_DECISION_TEMPLATE.md`
   - For post-market assessment (not needed today)

4. **Signal Quality Audit Framework**: `projects/stockbot/SIGNAL_QUALITY_AUDIT_FRAMEWORK.md`
   - For monitoring signal health during trading

---

## Success Criteria

✅ **Session Success Indicators**:
1. All pre-market health checks completed and passed
2. Seedwarden decision point handled (Track B activated if no user input)
3. Market open occurs at 13:30 UTC with sessions executing normally
4. All decisions logged to WORKLOG.md
5. All commits made to master (orchestration files + decision records)

❌ **Session Failure Indicators**:
1. Pre-market checks FAIL and issue cannot be resolved by 13:15 UTC
2. Jetson SSH unreachable (Tailscale down) — blocking failure
3. Docker container not running — blocking failure
4. WebSocket 406 error cannot be cleared — escalate to user decision

---

## Timeline Summary

```
11:00 UTC  → Begin pre-market health checks (DO NOT run SSH checks until 13:00)
12:30 UTC  → All checks should be complete
13:00 UTC  → Seedwarden decision deadline; execute Track B activation if needed
13:15 UTC  → Final market-open readiness verification; sessions wake
13:30 UTC  → Market opens; stockbot sessions begin trading
20:00 UTC  → Market closes; log results
```

---

## Notes for 11:00 UTC Orchestrator

- **Timing is critical**: The runbook specifies exact times (13:00 UTC for Jetson check, 13:15 UTC for final verify, 13:30 UTC for market open). Do NOT run checks early; follow the schedule.
- **Decision deadline is hard**: 13:00 UTC for Seedwarden is a firm deadline. Activation script will execute autonomously if no user decision.
- **WebSocket 406 is the biggest risk**: Monitor docker logs carefully for this error. If present, apply Contingency 6 from the runbook (120-second stop/wait/start).
- **All work from Session 2750 is complete**: Market Execution Runbook is ready; this session is about verification and decision execution, not additional prep work.

---

**Prepared by**: Session 2750 Orchestrator
**Prepared at**: 2026-06-04 08:30 UTC
**Status**: Ready for 11:00 UTC session execution
