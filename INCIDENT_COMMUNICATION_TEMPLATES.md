---
title: "Open-Repo June 12, 2026 Incident Communication Templates"
project: open-repo
phase: 5 (final production deployment)
document_type: communication-templates
status: PRODUCTION READY
created: 2026-06-06
target_deployment_date: 2026-06-12 (09:00 UTC)
---

# Incident Communication Templates — June 12, 2026

**Purpose**: Ready-to-send communication templates for all deployment outcomes. Fill in bracketed fields with actual values at send time. Do not delay communication to polish the message — send the most accurate version available at the trigger time.

**Channels**: Slack #deployments (primary), Discord (if applicable), email to stakeholders.

**Timing rules**:
- CRITICAL alert fires → notify immediately (do not wait for root cause)
- WARN alert fires → notify after 5-minute mitigation attempt, include outcome
- Rollback decision made → notify immediately on decision, before execution
- Deployment completes → notify within 5 minutes of all health checks passing

---

## Template 1: Deployment Start Notification

**When to send**: 09:00 UTC, when deployment steps begin.
**Channel**: Slack #deployments

```
DEPLOYMENT IN PROGRESS — Open-Repo Phase 5

Deployment started at 09:00 UTC.

Expected completion: 09:45 UTC (45 minutes)
Service status: Temporarily offline during deployment (Steps 2–6)

Active monitoring begins at 09:45 UTC. Full status update to follow by 10:00 UTC.

Avoid infrastructure changes during this window.
```

---

## Template 2: Full Deployment Success

**When to send**: Within 5 minutes of all health check steps passing (expected ~09:50 UTC).
**Channel**: Slack #deployments
**Trigger condition**: /health, /docs, /redoc, OPDS root, OPDS entries all return HTTP 200 with no CRITICAL alerts.

```
DEPLOYMENT COMPLETE — Open-Repo Phase 5

Deployment completed at [ACTUAL_TIME] UTC.

Health check results:
  /health:                  HTTP 200, [X]ms
  /docs (Swagger UI):       HTTP 200, [X]ms
  /redoc:                   HTTP 200, [X]ms
  /api/v2/opds/root.xml:    HTTP 200, [X]ms
  /api/v2/opds/entries:     HTTP 200, [X]ms

No CRITICAL alerts. No data loss. No rollback.

Service is fully operational. Active monitoring continues until [10:45] UTC.
```

**Customisation notes**: Replace [ACTUAL_TIME] with the clock time when all five health checks passed. Replace [X]ms with the actual response times from your curl output. If response times are elevated (>500ms) but still below CRITICAL threshold, note this as: "(elevated, monitoring)".

---

## Template 3: Partial Success — Elevated Response Times

**When to send**: When deployment completes but one or more endpoints show WARN-level response times (500–2000ms) without returning errors.
**Channel**: Slack #deployments
**Trigger condition**: All endpoints HTTP 200, but response times above OK threshold. No data loss, no 5XX errors.

```
DEPLOYMENT COMPLETE (PARTIAL SUCCESS) — Open-Repo Phase 5

Deployment completed at [ACTUAL_TIME] UTC. Service is running.

Health check results:
  /health:                  HTTP 200, [X]ms — [OK / ELEVATED]
  /docs (Swagger UI):       HTTP 200, [X]ms — [OK / ELEVATED]
  /redoc:                   HTTP 200, [X]ms — [OK / ELEVATED]
  /api/v2/opds/root.xml:    HTTP 200, [X]ms — ELEVATED ([X]ms, threshold 1000ms)
  /api/v2/opds/entries:     HTTP 200, [X]ms — ELEVATED

No data loss. No rollback. All endpoints responding.

Issue: OPDS endpoint response times are elevated above normal thresholds.
Likely cause: [database query latency / initial cache warming / high CPU post-startup]
Action: Active monitoring escalated. Re-checking every 1 minute for next 15 minutes.

If response times do not normalise below threshold by [TIME+15min] UTC, rollback decision will be made.

Next update by: [TIME+20min] UTC
```

---

## Template 4: WARN Alert — Active Investigation

**When to send**: Immediately when a WARN-level threshold is breached and investigation begins.
**Channel**: Slack #deployments
**Trigger condition**: Any single WARN threshold from POST_DEPLOYMENT_MONITORING_PLAN.md Section 2 (e.g., error rate 1–5%, response time 500–2000ms, CPU idle 20–50%).

```
DEPLOYMENT ALERT — Open-Repo Phase 5

Alert detected at [TIME] UTC.

Alert type:    [e.g., High response time / Elevated error rate / Low memory]
Current value: [e.g., OPDS response time: 1800ms]
Threshold:     [e.g., WARN threshold: 1000ms, CRITICAL threshold: 5000ms]

Service status: Running. No rollback initiated.

Investigation in progress. Increased monitoring frequency to 1-minute checks.

Next update: [TIME+5min] UTC — will report root cause or escalate to CRITICAL.
```

---

## Template 5: CRITICAL Alert — Immediate Notification

**When to send**: Immediately when a CRITICAL-level threshold is breached. Send before any investigation or action.
**Channel**: Slack #deployments + direct message to team lead
**Trigger condition**: Any CRITICAL threshold (error rate >10%, response time >2000ms on /health or >5000ms on OPDS, memory <1GB, etc.)

```
CRITICAL ALERT — Open-Repo Phase 5

Critical incident detected at [TIME] UTC.

Alert type:    [e.g., Health endpoint timeout / Error rate critical / OPDS failure]
Current value: [e.g., Error rate: 14%]
Threshold:     [e.g., CRITICAL at >10%]

Service impact: [e.g., OPDS endpoints returning HTTP 500 / Response times exceeding thresholds]

Immediate actions underway:
  - Checking application logs
  - Verifying database connectivity
  - Rollback preparation in progress

Decision point by: [TIME+5min] UTC

Next update: [TIME+3min] UTC — will report: fix applied OR rollback initiated.

On-call: [name/handle]
```

---

## Template 6: Rollback — Decision Notification

**When to send**: At the moment the rollback decision is made, before executing rollback steps.
**Channel**: Slack #deployments + direct message to team lead + email if outside working hours
**Trigger condition**: CRITICAL incident that cannot be resolved within 5-minute window, OR explicit rollback trigger from decision tree.

```
ROLLBACK INITIATED — Open-Repo Phase 5

Rollback decision made at [TIME] UTC.

Reason for rollback:
  [One specific sentence. Examples:]
  - Health endpoint non-responsive for >3 minutes with no recovery
  - OPDS endpoints returning HTTP 500 due to failed database migration
  - Error rate at 18% — above 10% CRITICAL threshold with no root cause identified
  - Multiple CRITICAL alerts (cascade): [list alert types]

Pre-rollback state:
  Service status: [running / failed / degraded]
  Last healthy state: [time when service was last confirmed healthy]
  Database backup confirmed: [YES — /opt/db-backups/[filename] / NO — git-only rollback]

Rollback procedure: Restoring pre-deployment backup and restarting previous version.
Estimated completion: [TIME+10min] UTC

User impact: Service temporarily unavailable during rollback (5–10 minutes).

Next update: [TIME+12min] UTC — will confirm rollback complete and service restored.
```

---

## Template 7: Rollback Complete — Service Restored

**When to send**: Within 5 minutes of rollback completing and health checks passing on the previous version.
**Channel**: Slack #deployments + all parties who received rollback notification

```
ROLLBACK COMPLETE — Open-Repo Phase 5

Rollback completed at [TIME] UTC. Service restored to previous version.

Post-rollback health checks:
  /health:               HTTP 200, [X]ms
  /api/v2/opds/root.xml: HTTP 200, [X]ms
  Error rate:            [X]% (previous baseline)

Deployed version: [previous commit hash / "pre-deployment backup"]
Service impact duration: [START_TIME] – [END_TIME] UTC ([N] minutes)

Root cause (preliminary): [1–2 sentences if known, or "Under investigation"]

Next steps:
  - Post-incident audit in progress (see DEPLOYMENT_POST_INCIDENT_AUDIT_CHECKLIST.md)
  - Root-cause analysis to be completed within 24 hours
  - Re-deployment will not be attempted until root cause is confirmed and fix is tested

Full incident report by: [DATE, e.g., June 13, 09:00 UTC]
```

---

## Template 8: All-Clear — End of Active Monitoring

**When to send**: At 10:45 UTC (end of active monitoring window) if deployment was successful or partially successful and stable.
**Channel**: Slack #deployments

```
ALL CLEAR — Open-Repo Phase 5 Active Monitoring Complete

Active monitoring window closed at 10:45 UTC.

Deployment outcome: [FULL SUCCESS / PARTIAL SUCCESS — details below]
Issues during monitoring: [None / list of WARN events that resolved]

Final metrics (09:45–10:45 UTC):
  Error rate:         [X]% (threshold: <1% OK)
  Health endpoint:    [X]ms avg (threshold: <200ms OK)
  OPDS response time: [X]ms avg (threshold: <1000ms OK)
  CPU idle:           [X]% (threshold: >50% OK)
  Memory available:   [X]GB (threshold: >2GB OK)

Transitioning to passive monitoring (24 hours).
Final sign-off check scheduled: June 13, 09:00 UTC.

No further action required unless new alerts fire.
```

---

## Notification Channel Reference

| Condition | Channel | Timing |
|-----------|---------|--------|
| Deployment start | Slack #deployments | Exactly 09:00 UTC |
| WARN alert | Slack #deployments | After 5-min investigation attempt |
| CRITICAL alert | Slack #deployments + team lead DM | Immediately on detection |
| Rollback decision | Slack #deployments + team lead DM + email | At moment of decision |
| Rollback complete | All channels that received rollback notice | Within 5 min of service restore |
| Full success | Slack #deployments | Within 5 min of all health checks passing |
| Active monitoring end | Slack #deployments | 10:45 UTC |

**Team lead contact**: [fill in before June 12]
**Slack #deployments webhook**: [fill in before June 12]
**On-call email**: [fill in before June 12]

---

**Templates Version**: 1.0
**Created**: June 6, 2026
**Valid For**: June 12, 2026 deployment
