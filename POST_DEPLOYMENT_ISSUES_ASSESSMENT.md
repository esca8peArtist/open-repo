---
title: "Open-Repo June 12 Deployment — Post-Deployment Issues Assessment"
project: open-repo
document_type: issues-assessment
audit_date: 2026-06-16
audit_host: raspby1 (100.70.184.84)
severity_summary: "1 Critical (process/state), 0 runtime incidents (no runtime exists)"
---

# Post-Deployment Issues Assessment

## Framing

This is not a conventional post-incident assessment. There is no live system that
degraded or crashed. The "issue" is that a deployment believed to be complete
**was never executed**, and its status was recorded incorrectly. The issues below
are therefore process/state-tracking issues plus the gating blockers that must be
cleared before any deployment can succeed. There are no runtime error logs to
collect because no service ever ran (`sudo -n docker ps -a` returns zero
containers; `journalctl -u open-repo` would find no unit).

## Prioritized Issue List

### ISSUE-1 (CRITICAL) — Deployment recorded as resolved but never executed
- **What:** Session 2995 marked the open-repo deployment item "resolved"
  (ORCHESTRATOR_STATE.md, Recently Resolved). The actual resolution was only of a
  *deployment start-time conflict requiring user clarification* (line 71), not the
  deployment. No infrastructure was ever stood up.
- **Impact:** False sense of completion. Phase 5.2 (author distribution) planning
  could proceed on the assumption of a live platform that does not exist, leading
  to downstream coordination failures (author onboarding to a dead URL).
- **Evidence:** 0 containers/images/volumes; no Nginx; no DB; HTTP 000 on all
  endpoints; last file change June 6; all June 12 commits are pause checkpoints.

### ISSUE-2 (CRITICAL) — No deployment infrastructure exists on the target host
- **What:** raspby1 has no reverse proxy, no PostgreSQL, no app runtime, no TLS,
  no monitoring. Docker daemon is healthy but empty.
- **Impact:** A first-time deployment is required. The published runbook cannot be
  followed as-is (see ISSUE-4).
- **Evidence:** See DEPLOYMENT_JUNE_12_OUTCOME_VERIFICATION.md, Checks 1–6.

### ISSUE-3 (HIGH) — Deployment blocked by an unresolved user decision (expired)
- **What:** The platform-deployment track for raspby1 is gated on a user platform
  decision (Nextcloud+Matrix vs Discourse) with a hard deadline of
  **June 15 23:59 UTC**, now expired with no decision (ORCHESTRATOR_STATE.md,
  systems-resilience block). open-repo shares the same host and the same
  unprovisioned-platform condition.
- **Impact:** Until the host platform/runtime model is decided and provisioned,
  open-repo cannot be deployed. This is a user-action blocker, not an autonomous fix.
- **Evidence:** ORCHESTRATOR_STATE.md systems-resilience block, lines ~76–84.

### ISSUE-4 (HIGH) — Runbook does not match the actual host or project tooling
- **What:** `DEPLOYMENT_JUNE_12_RUNBOOK.md` assumes:
  - SSH as `ubuntu@100.70.184.84` with `~/.ssh/production_key`
    (this host's user is `awank`; the runbook identity is wrong).
  - A systemd unit `open-repo` (does not exist).
  - `/opt/venv/open-repo` and `/opt/backups` (neither exists).
  - `pip install -r requirements.txt` (no requirements.txt; project is UV-based
    with `uv.lock`/`pyproject.toml`).
  - "No migrations required" (Step 6) — but three Alembic migrations exist and a
    fresh DB would need `alembic upgrade head`.
- **Impact:** Following the runbook verbatim would fail at multiple steps.
- **Evidence:** File checks for /opt paths and requirements.txt returned "not found";
  `backend/alembic/versions/` contains 001–003.

### ISSUE-5 (MEDIUM) — Operator lacks non-privileged Docker access
- **What:** `awank` is not in the `docker` group; all Docker ops require `sudo`.
- **Impact:** Any container-based deployment/automation must use sudo or the user
  must be added to the docker group. Affects automation that assumes group access.
- **Evidence:** `id` shows no docker group; `docker ps` returns permission denied
  while `sudo -n docker ps` succeeds.

### ISSUE-6 (LOW) — Repo hygiene artifacts in project root
- **What:** A zero-byte file with a corrupted name (`\x..I@`) and a 0-byte
  `PHASE_5.1_ACTIVATION_CHECKLIST.md`-adjacent duplication exist in the project
  directory; many near-duplicate Phase 5 checklist variants are present.
- **Impact:** Cosmetic / navigability; risk of editing the wrong checklist version.
- **Evidence:** `ls -la` of project root.

## Root Cause Analysis

**Primary root cause (ISSUE-1):** State was advanced ("resolved") on the basis of
clearing a *clarification* item rather than verifying the *deployment outcome*.
There was no post-deployment verification gate — exactly the gap this audit fills.
The Agent Loop (SPEC→PLAN→IMPLEMENT→REVIEW→FIX) REVIEW step was effectively skipped
for the deployment.

**Secondary root cause (ISSUE-2/3):** The host was never provisioned because the
prerequisite platform decision was never made by the user, and the June 12 window
fell inside a global pause directive. The deployment had no chance to run.

**Tertiary root cause (ISSUE-4):** The runbook was authored against an assumed
generic Ubuntu/systemd host with pip, not against the actual UV-based project on a
Raspberry Pi running as user `awank` with Docker-only access.

## Logs / Error Output

No service logs exist (no runtime). The only relevant "logs" are:
- `sudo -n docker ps -a` → empty table (no container ever created).
- `git log --since=2026-06-12 --until=2026-06-13` → only pause-checkpoint commits.
- `curl` to all endpoints → `HTTP 000` (connection refused), confirming nothing listens.

## Mitigation Paths

| Issue | Mitigation | Owner | Effort |
|-------|-----------|-------|--------|
| ISSUE-1 | Correct state: reopen open-repo deployment item; remove "resolved". Add a mandatory post-deploy verification gate to the Agent Loop REVIEW step. | orchestrator | 15 min |
| ISSUE-2 | Execute a first-time provisioning (see restoration checklist in routing doc). | operator | 4–6 h |
| ISSUE-3 | Obtain user platform/runtime decision (this is a user-action blocker). | user | n/a |
| ISSUE-4 | Rewrite runbook for `awank@raspby1`, UV tooling, Docker-based runtime, and Alembic migrations. | orchestrator | 1–2 h |
| ISSUE-5 | Either run deploy via sudo (self-enforcing automation) or `sudo usermod -aG docker awank`. | operator | 5 min |
| ISSUE-6 | Remove corrupt/zero-byte files; consolidate checklist variants. | orchestrator | 20 min |

## Escalation Procedure

1. **Immediate (orchestrator, autonomous):** Correct the resolved-state record for
   open-repo and surface ISSUE-1 in the next CHECKIN. Do NOT mark deployed.
2. **User decision required (BLOCKER):** ISSUE-3 — confirm host platform/runtime
   model and authorize first-time provisioning of open-repo on raspby1. Without
   this, no deployment can proceed. Flag in INBOX with the systems-resilience
   platform decision (shared host, shared dependency).
3. **If user authorizes deploy:** Proceed with the restoration/first-deploy
   checklist in `RECOVERY_OR_NEXT_PHASE_ROUTING.md`, applying the runbook
   corrections from ISSUE-4. Verify all 6 health checks pass before declaring success.
4. **Do not begin Phase 5.2 author onboarding** until checks 1–6 pass — onboarding
   authors to a non-existent endpoint is the principal downstream risk.
