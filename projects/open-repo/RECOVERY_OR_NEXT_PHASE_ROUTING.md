---
title: "Open-Repo June 12 Deployment — Recovery / Next-Phase Routing"
project: open-repo
document_type: routing-decision
audit_date: 2026-06-16
routing_decision: RESTORATION PATH (first-time deployment) — Phase 5.2 NOT yet eligible
gating_blocker: "User platform/runtime decision for raspby1 (expired June 15 23:59 UTC)"
---

# Recovery / Next-Phase Routing

## Routing Decision

**Path selected: RESTORATION (first-time deployment), NOT Phase 5.2 advancement.**

The audit found the deployment was never executed and no production infrastructure
exists on raspby1 (see `DEPLOYMENT_JUNE_12_OUTCOME_VERIFICATION.md`). Therefore the
"deployment succeeded → Phase 5.2 readiness" branch does not apply. We route to the
restoration/first-deploy branch.

**Phase 5.2 (author distribution coordination) is BLOCKED** and must not start.
Onboarding authors requires a live, reachable platform with a valid TLS endpoint.
None exists. Wave 2 author onboarding has no operational target.

## Why This Is a First Deploy, Not a Recovery

There is no prior running state to restore — zero containers, images, volumes, DB,
proxy, certs, or monitoring. "Restoration" here means standing the platform up for
the first time, then verifying.

## Blocker That Must Clear First (USER ACTION)

Per ORCHESTRATOR_STATE.md, raspby1's platform/runtime model is gated on a user
decision (shared with the systems-resilience Phase 5.1 platform decision) whose
deadline expired **June 15 23:59 UTC** with no response. Until the user confirms:
- the host runtime model (Docker-based stack on raspby1), and
- authorization to provision open-repo's first production deployment,

no autonomous deployment may proceed. This is consistent with the project rule
that fixes must be self-enforcing and must not silently bind services or make
unilateral infra choices.

## Restoration / First-Deploy Checklist

Resolve in order. Each item maps to a failed health check (C1–C6) and/or an issue
(ISSUE-n) from the assessment.

### Phase A — Pre-provision prerequisites
- [ ] **A1 (ISSUE-3, BLOCKER):** Obtain user authorization + runtime decision for
      raspby1 first deploy. Do not proceed without it.
- [ ] **A2 (ISSUE-5):** Decide Docker access model — run all deploy steps via `sudo`
      (preferred: self-enforcing, no host change) OR `sudo usermod -aG docker awank`
      then re-login. Document the choice.
- [ ] **A3 (ISSUE-4):** Produce a corrected runbook for `awank@raspby1`:
      replace `ubuntu`/`production_key` with the real identity; replace
      systemd/pip/venv flow with a Docker Compose stack; add Alembic migration step.

### Phase B — Provision infrastructure (→ fixes C1, C2, C3, C5, C6)
- [ ] **B1 (→C3):** Stand up PostgreSQL (container), bound to `127.0.0.1:5432`
      ONLY (never 0.0.0.0). Create `open_repo` database and app credentials.
- [ ] **B2 (→C3):** Run `alembic upgrade head` from `backend/` against the new DB;
      confirm tables for migrations 001–003 exist.
- [ ] **B3 (→C1):** Author `Dockerfile` + `docker-compose.yml` for the FastAPI app
      using UV (`uv sync`/`uv run uvicorn`), bind app to `127.0.0.1:8000` only.
      Build image and start container.
- [ ] **B4 (→C2):** Install and configure Nginx (or chosen proxy) as reverse proxy
      to `127.0.0.1:8000`; listen on a specific interface IP / 127.0.0.1, never 0.0.0.0.
- [ ] **B5 (→C5):** Provision TLS (certbot or self-signed for Tailscale-only access),
      install cert, enable HTTPS in the proxy.
- [ ] **B6 (→C6):** Deploy monitoring (Prometheus + Grafana + node_exporter),
      all bound to loopback / specific interface; import baseline dashboards from
      `POST_DEPLOYMENT_MONITORING_PLAN.md`.

### Phase C — Verify (all six must pass before declaring success)
- [ ] **C1:** `sudo docker ps` shows the open-repo app container "Up" and healthy.
- [ ] **C2:** Proxy active; `curl -I http://127.0.0.1/` returns 200/301.
- [ ] **C3:** DB reachable; migrations at head; app connects without error in logs.
- [ ] **C4:** `curl http://127.0.0.1:8000/api/health` (and `/docs`, `/redoc`,
      `/api/v2/opds/root.xml`) return 200 with valid bodies.
- [ ] **C5:** `curl -Iv https://<endpoint>/` shows a valid, non-expired certificate.
- [ ] **C6:** Prometheus targets UP; Grafana dashboards rendering live data.
- [ ] **C7 (ISSUE-1):** Update ORCHESTRATOR_STATE/WORKLOG with the *verified* outcome
      and the evidence (do not mark resolved until C1–C6 pass).

### Phase D — Cleanup
- [ ] **D1 (ISSUE-6):** Remove the corrupt zero-byte file and consolidate duplicate
      Phase 5 checklist variants.

## Phase 5.2 Readiness Assessment (deferred)

| Gate | Required state | Current | Eligible? |
|------|----------------|---------|-----------|
| Live platform endpoint | reachable, 200 OK | HTTP 000 | ❌ |
| Valid TLS for author-facing URL | valid cert | none | ❌ |
| OPDS endpoints serving | 200 + valid Atom | not running | ❌ |
| Monitoring for onboarding traffic | operational | none | ❌ |
| Stable deploy ≥ 48–72h | n/a | not deployed | ❌ |

**Phase 5.2 is not eligible.** The application code is ready (Phase 5 complete,
157 tests passing per `PHASE_5_COMPLETION_SUMMARY.md`), but readiness is gated on a
running, verified platform. **Do not publish a Wave 2 author-onboarding timeline
until C1–C6 pass.** Once they do, the earliest Phase 5.2 kickoff is a 48–72h soak
after a clean verification, i.e., roughly 2–4 days after the first successful deploy,
not a fixed calendar date — the prior "June 12" anchor is void.

## Summary and Next Actions

1. **Correct the record now (autonomous, ISSUE-1):** open-repo is NOT deployed.
   Reopen the deployment item; add a post-deploy verification gate to the REVIEW step.
2. **Escalate the blocker (user, ISSUE-3):** request authorization + runtime decision
   for the first raspby1 deployment; bundle with the expired systems-resilience
   platform decision since they share the host.
3. **On authorization:** execute Phases A→D using the corrected, UV/Docker-based
   runbook; verify all six checks; only then mark deployed.
4. **Hold Phase 5.2:** keep author-distribution coordination and Wave 2 onboarding
   paused until a verified, soaked deployment exists.

**Bottom line:** Nothing failed in production because nothing was in production.
The recovery action is a correctly-scoped, user-authorized first deployment
followed by mandatory six-point verification — and an explicit fix to the
state-tracking gap that let a non-deployment be recorded as "resolved."
