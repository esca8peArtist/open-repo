---
title: "Open-Repo June 12, 2026 Deployment Communication Templates"
project: open-repo
phase: 5 (final production deployment)
document_type: communication-templates
status: READY TO EXECUTE — populate [BRACKETED] fields before sending
created: 2026-06-12
deployment_date: June 12, 2026
deployment_start_time: "[REQUIRED USER INPUT] — 09:00 UTC or 20:00 UTC (see Date Conflict Notice)"
---

# Deployment Communication Templates
## June 12, 2026

**Purpose**: Copy-paste ready notification templates for all deployment phases. Replace every `[BRACKETED]` placeholder with actual values before sending. Instructions for each template appear before the template block.

**Distribution channels**: Slack `#deployments` channel, email distribution list, any community forums or GitHub Discussions.

---

## Date Conflict Notice — Affects Template Timing

A confirmed conflict exists between the deployment SOP documents regarding the start time:

- **09:00 UTC**: Used in DEPLOYMENT_JUNE_12_FINAL_PROCEDURES.md, DEPLOYMENT_JUNE12_PRECHECK_ENVIRONMENT.md, DEPLOYMENT_JUNE12_RISK_MITIGATION.md, and this document (as written)
- **20:00 UTC**: Used in DEPLOYMENT_JUNE_12_RUNBOOK.md, DEPLOYMENT_JUNE_12_GO_LIVE_CHECKLIST.md, and PHASE_5_COMPLETION_SUMMARY.md

**User action required**: Confirm the canonical start time and update all `[DEPLOYMENT_START_TIME]` and `[DEPLOYMENT_END_TIME]` placeholders across the templates below with the confirmed time. If 20:00 UTC is canonical, all "09:00 UTC" references in this document must be updated to "20:00 UTC" before any template is sent.

---

## Template Customization Reference

**Placeholders used across all templates**:

```
[DEPLOYER_NAME]          The person executing the deployment
[DEPLOYER_SLACK]         Slack handle of the deployer, e.g. @jsmith
[CONTACT_EMAIL]          Deployer's email address
[ON_CALL_SLACK]          Slack handle of on-call engineer during monitoring window
[DEPLOYMENT_START_TIME]  09:00 UTC or 20:00 UTC (confirm before sending)
[DEPLOYMENT_END_TIME]    09:45 UTC or 20:45 UTC (45 minutes after start)
[MONITORING_END_TIME]    10:45 UTC or 21:45 UTC (60 minutes after end)
[STATUS_CHECK_TIME]      20:00 UTC on June 12 (or 06:00 UTC June 13 if 20:00 UTC start)
[ACTUAL_COMPLETION_TIME] The real clock time when deployment finished
[ACTUAL_DURATION_MIN]    Actual minutes the deployment took
[COMMIT_HASH]            Short git commit hash, e.g. abc123d
[ERROR_DESCRIPTION]      One sentence describing what went wrong
[FAILURE_STEP]           Which step failed, e.g. "Step 6: Database Migrations"
[ROLLBACK_ETA]           Estimated UTC time when rollback will complete
[UPTIME_HOURS]           Hours since deployment completed (should be ~10 by Template 5)
[ERROR_RATE]             Current error rate, e.g. "0.00%" or "<0.01%"
[USER_FEEDBACK]          One sentence summarizing any user-reported issues
```

**How to use these templates**:
1. Open the template section you need
2. Copy the entire body between the triple-backtick fences
3. Paste into Slack / email
4. Use Find and Replace (Ctrl+H) to substitute every [BRACKETED] value
5. Verify no placeholder remains before sending
6. Send to the appropriate channel

---

## Template 1: Pre-Deployment Announcement

**When to send**: June 11 EOD (by 18:00 UTC the day before deployment). This gives stakeholders at least 12 hours of notice before the maintenance window opens.

**Recipient**: `#deployments` Slack channel; email list of all active contributors and any external users of the OPDS catalog.

**Subject** (email): `[SCHEDULED MAINTENANCE] open-repo deployment scheduled June 12, [DEPLOYMENT_START_TIME] UTC`

---

```
Subject: [SCHEDULED MAINTENANCE] open-repo deployment scheduled June 12, [DEPLOYMENT_START_TIME] UTC

Hello,

We are scheduling a production deployment for the open-repo project.

Deployment details:
  Date:             June 12, 2026
  Start time:       [DEPLOYMENT_START_TIME] UTC
  Expected finish:  [DEPLOYMENT_END_TIME] UTC (45 minutes)
  Maximum window:   2 hours from start

What is being deployed:
  - Phase 5 WCAG 2.1 AA accessibility compliance verification
  - 6 resolved accessibility violations (color contrast, screen reader support)
  - Enhanced keyboard navigation
  - No breaking changes to existing OPDS API endpoints

Expected impact during the deployment window:
  - The OPDS catalog endpoint (/api/v2/opds/*) will be temporarily unavailable
  - The Swagger UI (/docs) and ReDoc (/redoc) pages will be temporarily unavailable
  - Existing data is safe — no data loss is expected or planned
  - Estimated service downtime: 25–35 minutes within the 2-hour window

Rollback plan:
  If any issue is detected, the previous stable version will be restored within
  10 minutes. You will be notified immediately if rollback is initiated.

What you should do:
  - Plan to access the service before [DEPLOYMENT_START_TIME] UTC or after [DEPLOYMENT_END_TIME] UTC
  - Do not initiate data exports or heavy operations during the window
  - If you have time-sensitive needs during this window, contact [DEPLOYER_NAME] at [CONTACT_EMAIL]

Questions:
  Reply to this message or reach out to [DEPLOYER_SLACK] on Slack.

Thank you for your patience.

[DEPLOYER_NAME]
open-repo project
```

---

## Template 2: Deployment Start Notification

**When to send**: At the moment deployment begins — specifically when the pre-flight checklist in DEPLOYMENT_JUNE12_PRECHECK_ENVIRONMENT.md is complete and the deployer is beginning DEPLOYMENT_JUNE_12_FINAL_PROCEDURES.md.

**Recipient**: `#deployments` Slack channel.

**Subject** (email): `[IN PROGRESS] open-repo deployment — [DEPLOYMENT_START_TIME] UTC start`

---

```
Subject: [IN PROGRESS] open-repo deployment — [DEPLOYMENT_START_TIME] UTC start

Deployment is now in progress.

Start time: [DEPLOYMENT_START_TIME] UTC
Expected completion: [DEPLOYMENT_END_TIME] UTC
Current step: Pre-flight environment verification complete. Beginning deployment.

Pre-flight results (all pass required before proceeding):
  Environment checks:     PASS
  Test suite (157/157):   PASS
  A11y tests (72/72):     PASS
  Database state:         PASS
  Backup created:         PASS

What to expect:
  The service will be unavailable starting now and through approximately [DEPLOYMENT_END_TIME] UTC.
  Status updates will be posted to this thread every 15 minutes.

If you observe issues after [DEPLOYMENT_END_TIME] UTC:
  Contact [DEPLOYER_SLACK] immediately on Slack or [ON_CALL_SLACK] for urgent issues.

Next update: [DEPLOYMENT_START_TIME + 15 min] UTC

[DEPLOYER_NAME]
```

---

## Template 3: Deployment Success Notification

**When to send**: Once all post-deployment verification steps in DEPLOYMENT_JUNE_12_FINAL_PROCEDURES.md Section 5 have passed and the deployment is confirmed successful. This is expected at approximately [DEPLOYMENT_END_TIME] UTC.

**Recipient**: `#deployments` Slack channel; email list (same as Template 1).

**Subject** (email): `[COMPLETE] open-repo deployment successful — [ACTUAL_COMPLETION_TIME] UTC`

---

```
Subject: [COMPLETE] open-repo deployment successful — [ACTUAL_COMPLETION_TIME] UTC

The June 12 open-repo production deployment has completed successfully.

Completion time:  [ACTUAL_COMPLETION_TIME] UTC
Duration:         [ACTUAL_DURATION_MIN] minutes (target was 45 minutes)
Deployed commit:  [COMMIT_HASH]
Rollback needed:  No

Post-deployment verification results:
  Health endpoint (/health):              PASS — HTTP 200
  OPDS root catalog (/api/v2/opds/root.xml): PASS — HTTP 200, valid Atom XML
  OPDS entries (/api/v2/opds/entries):    PASS — HTTP 200, valid Atom XML
  Swagger UI (/docs):                     PASS — HTTP 200
  ReDoc (/redoc):                         PASS — HTTP 200
  Application error logs:                 PASS — 0 CRITICAL/ERROR entries
  System resources:                       PASS — within normal range

What was deployed:
  Phase 5 WCAG 2.1 AA accessibility compliance:
  - All 11 WCAG 2.1 AA criteria now verified passing
  - 72 automated accessibility tests confirm zero violations
  - Color contrast fixes on Swagger UI and ReDoc (6 violations resolved)
  - Keyboard navigation verified across all interactive pages
  - Screen reader compatibility improved

The service is fully operational.

Active monitoring is in progress through [MONITORING_END_TIME] UTC.
A status report will be sent at [STATUS_CHECK_TIME] UTC (approximately 10 hours post-deployment).

If you notice any issues, contact [DEPLOYER_SLACK] or [ON_CALL_SLACK] immediately.

[DEPLOYER_NAME]
```

---

## Template 4: Escalation Notification

**When to send**: Immediately — within 1 minute of detecting a failure or initiating rollback. Do not wait to investigate before sending the initial notification. Update the thread as the situation evolves.

**Recipient**: `#deployments` Slack channel + direct message to team lead + [ON_CALL_SLACK].

**Subject** (email): `[ISSUE] open-repo deployment encountered issue — rolling back`

---

### 4a: Initial Failure Alert (send within 1 minute of detection)

```
Subject: [ISSUE] open-repo deployment encountered issue — rolling back

The open-repo June 12 deployment has encountered an issue.

Detected at: [DETECTED_TIME] UTC
Failed at:   [FAILURE_STEP]
Error:       [ERROR_DESCRIPTION]

Rollback initiated. The previous stable version is being restored.
Estimated service restoration: [ROLLBACK_ETA] UTC (7–9 minutes from now)

What you should expect:
  - Service is currently unavailable
  - The previous version (before today's deployment) will be restored
  - No data loss is expected — a backup was taken at [BACKUP_TIME] UTC

I am actively working on restoration. Updates will follow every 2 minutes.

Contact [DEPLOYER_SLACK] with urgent questions.

[DEPLOYER_NAME]
```

---

### 4b: Rollback Progress Update (send 2 minutes after 4a)

```
Rollback update — [CURRENT_TIME] UTC (2 minutes elapsed)

Rollback progress:
  Step 1 (stop service):         DONE
  Step 2 (restore database):     IN PROGRESS
  Step 3 (revert code):          PENDING
  Step 4 (reinstall deps):       PENDING
  Step 5 (start service):        PENDING
  Step 6 (verify endpoints):     PENDING

Current status: [BRIEF_STATUS]
Estimated completion: [ROLLBACK_ETA] UTC

Next update in 5 minutes.
```

---

### 4c: Rollback Complete Notification (send when service is verified restored)

```
Rollback complete — service restored — [RESTORE_TIME] UTC

The previous version has been successfully restored.

Rollback duration: [ROLLBACK_DURATION_MIN] minutes
Total service downtime: [TOTAL_DOWNTIME_MIN] minutes
Data loss: None — backup from [BACKUP_TIME] UTC used

Verification:
  Health endpoint (/health):        PASS — HTTP 200
  OPDS root (/api/v2/opds/root.xml): PASS — HTTP 200
  Swagger UI (/docs):               PASS — HTTP 200

The service is operational on the previous stable version.

Next steps:
  - Active monitoring continues through [MONITORING_END_TIME] UTC
  - Root cause investigation underway
  - Incident post-mortem scheduled for [POSTMORTEM_DATE]
  - Re-deployment not scheduled until investigation is complete

Thank you for your patience. I will publish a post-mortem within 24 hours.

[DEPLOYER_NAME]
```

---

## Template 5: Post-Deployment Status Report

**When to send**: Approximately 10 hours after deployment completion — at [STATUS_CHECK_TIME] UTC on June 12 (or June 13 if deployment started at 20:00 UTC). This closes the active monitoring period and gives stakeholders confidence that the deployment is stable.

**Recipient**: `#deployments` Slack channel; email list (same as Template 1).

**Subject** (email): `[POST-DEPLOYMENT] open-repo status report — all metrics nominal`

---

```
Subject: [POST-DEPLOYMENT] open-repo status report — all metrics nominal

10-hour post-deployment status report for the June 12 open-repo deployment.

Deployment completed: [ACTUAL_COMPLETION_TIME] UTC
This report covers: [ACTUAL_COMPLETION_TIME] UTC to [STATUS_CHECK_TIME] UTC ([UPTIME_HOURS] hours)

Service health summary:
  Uptime since deployment:     100% ([UPTIME_HOURS] hours, 0 interruptions)
  Health endpoint (/health):   Responding 200 OK, continuous
  Error rate (HTTP 4xx/5xx):   [ERROR_RATE] (baseline: <0.01%)
  Average response latency:    within normal range

User feedback:
  [USER_FEEDBACK]

  (If no issues received: "No user-reported issues in the first 10 hours.")

Active monitoring window: CLOSED as of this message
Passive monitoring: Continues through June 13, [ACTUAL_COMPLETION_TIME] UTC (24 hours total)

What was deployed (reminder):
  Phase 5 WCAG 2.1 AA accessibility compliance — all 11 criteria verified
  Deployed commit: [COMMIT_HASH]
  Zero breaking changes to existing API

Next monitoring checkpoint:
  June 13, [ACTUAL_COMPLETION_TIME] UTC — 24-hour passive monitoring report
  Contact [ON_CALL_SLACK] if any issue arises before then

Thank you to everyone who coordinated during the maintenance window.

[DEPLOYER_NAME]
```

---

## Template Selection Reference

| Situation | Template | When |
|-----------|----------|------|
| Day before — notify stakeholders | Template 1 (Announcement) | June 11 EOD, by 18:00 UTC |
| Deployment window opens | Template 2 (Start) | Immediately at deployment start |
| All verification steps pass | Template 3 (Success) | Within 5 min of final verification |
| Any failure or rollback initiated | Template 4a (Alert) | Within 1 min of detection |
| Rollback in progress, 2 min update | Template 4b (Progress) | +2 min, then every 5 min |
| Rollback complete, service live | Template 4c (Restored) | Within 2 min of verification |
| 10 hours post-deployment | Template 5 (Status Report) | [STATUS_CHECK_TIME] UTC |

---

## Placeholder Completion Checklist

Complete this before the deployment window opens. Record actual values here for reference during deployment.

```
[DEPLOYER_NAME]          = ________________________________
[DEPLOYER_SLACK]         = ________________________________
[CONTACT_EMAIL]          = ________________________________
[ON_CALL_SLACK]          = ________________________________
[DEPLOYMENT_START_TIME]  = ________________________________ UTC  (resolve date conflict first)
[DEPLOYMENT_END_TIME]    = ________________________________ UTC
[MONITORING_END_TIME]    = ________________________________ UTC
[STATUS_CHECK_TIME]      = ________________________________ UTC
[BACKUP_TIME]            = ________________________________ UTC  (filled in during pre-flight)
[POSTMORTEM_DATE]        = ________________________________      (fill in if rollback occurs)
```

**Do not send any template with unfilled [BRACKETED] placeholders.**

---

**Document Version**: 2.0
**Created**: June 12, 2026
**Supersedes**: DEPLOYMENT_JUNE12_COMMUNICATION_TEMPLATES.md v1.0 (June 6, 2026)
**Valid For**: June 12, 2026 deployment
**Reference Documents**: DEPLOYMENT_JUNE_12_FINAL_PROCEDURES.md, DEPLOYMENT_JUNE12_RISK_MITIGATION.md
