---
title: "Open-Repo June 12, 2026 Deployment — Outcome Verification"
project: open-repo
document_type: post-deployment-audit
audit_date: 2026-06-16
audit_host: raspby1 (100.70.184.84, Raspberry Pi 5)
auditor: analyze-agent (autonomous audit)
verdict: DEPLOYMENT DID NOT EXECUTE — NO PRODUCTION INFRASTRUCTURE PRESENT
confidence: 99% (direct system inspection)
---

# June 12 Deployment — Outcome Verification

## Verdict (read first)

**The June 12, 2026 deployment did not occur.** No open-repo production
infrastructure exists on raspby1. This is **not a degraded or failed-but-partial
deployment** — there is no container, no image, no reverse proxy, no database,
no certificate, and no listening service. The environment is in a pre-deployment
state.

Two compounding factors explain this:

1. **The task's framing is based on a false premise.** The audit was requested
   for a "June 12 09:00 UTC deployment." The actual runbook
   (`DEPLOYMENT_JUNE_12_RUNBOOK.md`) targets **20:00 UTC**, not 09:00 UTC, and
   "Session 2995 marked platform deployment resolved" is inaccurate. Session 2995
   resolved only a *deployment start-time conflict requiring user clarification*
   (see `ORCHESTRATOR_STATE.md` line 71), not the deployment itself.

2. **June 12 was a global pause window.** Every git commit on 2026-06-12 reads
   `pause directive stable, checkpoint verification` (sessions 3433–3456). No
   deployment activity of any kind was committed or executed that day.

## Environment Health Check Matrix

| # | Check | Expected | Actual | Status |
|---|-------|----------|--------|--------|
| 1 | open-repo Docker container running | 1+ running container | 0 containers (running or stopped) | ❌ FAIL |
| 2 | Nginx reverse proxy active & configured | active, sites-enabled present | Nginx not installed at all | ❌ FAIL |
| 3 | Database migrated | PostgreSQL reachable, migrations applied | No PostgreSQL service/container; port 5432 closed | ❌ FAIL |
| 4 | API responding 200 OK | HTTP 200 on /api/health | HTTP 000 (connection refused), all endpoints | ❌ FAIL |
| 5 | SSL certificate valid | valid cert in /etc/letsencrypt/live | No certbot, no /etc/letsencrypt | ❌ FAIL |
| 6 | Monitoring dashboards operational | Prometheus/Grafana reachable | No monitoring containers; ports 9090/3000 closed | ❌ FAIL |

**0 of 6 checks pass.**

## Evidence — Commands and Output

### Check 1: Docker container status

The invoking user (`awank`) is not in the `docker` group, so direct calls return
a permission error; the daemon itself is running and was queried via `sudo`.

```
$ docker ps
permission denied while trying to connect to the Docker daemon socket ...

$ id
uid=1000(awank) ... groups=...,27(sudo),... (NOTE: no 'docker' group)

$ systemctl is-active docker
active                                  # daemon IS running

$ sudo -n docker ps -a
CONTAINER ID   IMAGE   COMMAND   CREATED   STATUS   PORTS   NAMES
                                        # ZERO containers — none ever created

$ sudo -n docker images
REPOSITORY   TAG   IMAGE ID   CREATED   SIZE
                                        # ZERO images — nothing built or pulled

$ sudo -n docker volume ls
DRIVER    VOLUME NAME
                                        # ZERO volumes — no DB persistence created
```

**Finding:** Docker daemon is healthy but completely empty. The open-repo
application was never containerized or run on this host.

### Check 2: Nginx reverse proxy

```
$ which nginx
(no output)
$ ls /usr/sbin/nginx
No such file or directory
$ dpkg -l | grep -i nginx
(no output — nginx NOT installed via package manager)
$ ls /etc/nginx/
No such file or directory
$ systemctl is-active nginx
inactive
$ which caddy traefik apache2
(none found)
```

**Finding:** No reverse proxy of any kind is installed. There is no Nginx
binary, package, or configuration directory.

### Check 3: Database migration status

```
$ systemctl is-active postgresql
inactive
$ sudo -n docker ps -a | grep -i postgres
(no output — no postgres container)
$ pg_isready -h 127.0.0.1 -p 5432
pg_isready: command not found      # postgres client not even installed
```

The application expects PostgreSQL (`backend/app/database.py`:10):
```
DATABASE_URL = os.getenv("DATABASE_URL",
    "postgresql+asyncpg://postgres:postgres@localhost:5432/open_repo")
```

Migration files exist in the repo but were never applied (no DB to apply to):
```
$ ls backend/alembic/versions/
001_add_federation_partners.py
002_add_federation_conflicts.py
003_add_zim_exports_table.py
```

**Finding:** No database server exists. Migrations are authored but unapplied.

### Check 4: API endpoint response

```
$ for url in .../api/health .../api/ready .../health :80/ :443/ ; do curl ...; done
http://127.0.0.1:8000/api/health   -> HTTP 000 (connection refused)
http://127.0.0.1:8000/api/ready    -> HTTP 000 (connection refused)
http://127.0.0.1:8000/health       -> HTTP 000 (connection refused)
http://127.0.0.1:80/               -> HTTP 000 (connection refused)
http://127.0.0.1:443/              -> HTTP 000 (connection refused)
```

Listening sockets on the host (no app/web ports present):
```
$ ss -tlnp
127.0.0.1:631   (CUPS)
0.0.0.0:22      (SSH)
0.0.0.0:5125    (unrelated)
*:5900          (VNC)
... no :80, :443, :8000, :5432, :9090, :3000 ...
```

**Finding:** No application is listening. Every endpoint refuses connection.

### Check 5: SSL/TLS certificate

```
$ ls /etc/letsencrypt/live/
No such file or directory
$ which certbot
(not installed)
```

**Finding:** No TLS termination is possible. No certificates provisioned.

### Check 6: Monitoring dashboards

```
$ sudo -n docker ps -a | grep -iE "prometheus|grafana|loki"
(no output)
$ curl http://127.0.0.1:9090/   -> HTTP 000   (Prometheus down)
$ curl http://127.0.0.1:3000/   -> HTTP 000   (Grafana down)
$ curl http://127.0.0.1:9100/   -> HTTP 000   (node_exporter down)
```

**Finding:** No monitoring stack exists.

## Supporting Evidence — Deployment Was Never Initiated

- **No deployment artifacts in the repo.** There is no `docker-compose.yml`,
  no `Dockerfile`, no `.env`, and no `nginx.conf` anywhere under
  `projects/open-repo/` (excluding `node_modules`). The runbook's deployment
  model is a systemd + git-pull + venv flow, none of which is present on the host.
- **Runbook prerequisites are absent on the host:**
  - `/opt/venv/open-repo` — does not exist (runbook Step 5)
  - `/opt/backups` — does not exist (runbook Step 3)
  - `backend/requirements.txt` — does not exist; project uses `uv.lock`/`pyproject.toml`,
    so runbook Step 5 (`pip install -r requirements.txt`) would have failed as written.
  - No `open-repo` systemd unit exists (runbook Steps 2 and 7 would no-op).
- **Git history shows no deployment on June 12.** All 2026-06-12 commits are
  orchestrator pause-checkpoint entries. The "deployment commit" the runbook
  expects on master was never created.
- **Last project file modification is June 6, 2026.** Nothing in
  `projects/open-repo/` has changed in the 10 days spanning the deployment date.
- **Corroborating block in ORCHESTRATOR_STATE.md** (systems-resilience, line 76+)
  independently states raspby1 had "no web services on ports 80/443" and the
  platform was "not deployed on raspby1," pending an unresolved user platform
  decision whose deadline expired June 15 23:59 UTC.

## Conclusion

The June 12 deployment **did not happen**. There is nothing to roll back and no
runtime to recover, because no runtime was ever created. The application
codebase (Phase 5) is complete and tested per `PHASE_5_COMPLETION_SUMMARY.md`
(157 tests passing), but it has never been deployed to this host. The correct
next step is a *first* deployment, not a recovery — see
`RECOVERY_OR_NEXT_PHASE_ROUTING.md`.
