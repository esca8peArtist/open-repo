---
title: "Platform Decision Matrix with Runbooks — June 14-15 Decision"
project: systems-resilience
created: 2026-06-14
purpose: "Unified decision matrix for June 14-15 platform choice. Synthesizes Nextcloud+Matrix vs Discourse for Pi5 ARM64 deployment with honest recommendation and links to per-platform runbooks."
decision_deadline: "2026-06-15 EOD"
status: "AWAITING USER DECISION"
---

# Platform Decision Matrix with Runbooks
## June 14-15, 2026 — Pi5 ARM64 Deployment

**Background**: Phase 5.1 deployment has been blocked since June 6 waiting for this platform decision. Docker is installed and verified operational on raspby1 (100.120.18.84, Pi5 ARM64, 189GB free). Whichever platform is chosen, deployment can begin immediately and be live within the same day.

---

## Side-by-Side Comparison

| Dimension | Nextcloud + Matrix | Discourse |
|-----------|-------------------|-----------|
| **RAM at idle** | 1.5–2.5 GB | 1–1.5 GB |
| **RAM under 50 users** | 3–4 GB (manageable) | 2–2.5 GB (comfortable) |
| **RAM under 100 users** | 4.5–5.5 GB (tight) | 2.5–3 GB (comfortable) |
| **RAM headroom on Pi5** | 1.7–4 GB (shrinks fast) | 5+ GB (very safe) |
| **OOM risk at 100 users** | Moderate (marginal) | None |
| **ARM64 compatibility** | Yes — official images | Yes — builds from source (15–25 min) |
| **OnlyOffice on ARM64** | NO — no ARM64 image | Not applicable |
| **Deployment time** | 4–6 hours | 2–3 hours |
| **Number of containers** | 6–7 | 1 |
| **Daily ops overhead** | 5–8 hrs/month | 2–3 hrs/month |
| **User capacity (reliable)** | 50 users (with tuning) | 100–200 users (no tuning) |
| **Collaborative editing** | Text only (no OnlyOffice) | Not available |
| **Real-time chat** | Yes — Matrix/Element | No — async forum only |
| **End-to-end encryption** | Yes — Matrix E2E | No — TLS only |
| **File sharing** | Yes — Nextcloud files | Attachment uploads only |
| **Forum/discussion** | Matrix rooms (flat) | Native threading (excellent) |
| **Moderation tools** | Manual (no auto-mod) | Excellent (trust levels, flags) |
| **Governance automation** | None | Full (trust levels auto-escalate) |
| **Backup complexity** | 3-part (DB + config + files) | Built-in (one command) |
| **Troubleshooting** | Complex (6 services) | Simple (one log stream) |
| **Offline authoring** | Yes (WebDAV sync) | No (web-only) |
| **Federation** | Yes (Matrix) | No |
| **Plugin ecosystem** | Limited ARM64 support | Excellent (but web-only) |
| **Public research publishing** | Adequate (file download) | Excellent (forum topics) |
| **Setup complexity** | High (compose, nginx.conf, homeserver.yaml) | Low (one app.yml file) |
| **Known blockers** | OnlyOffice ARM64 unavailable | ⚠️ CRITICAL: Pi5 IPv6 loopback Redis bug (OPEN) — bootstrap fails without workaround |

---

## CRITICAL BLOCKER ALERT

⚠️ **Discourse has a known, open bug on Raspberry Pi 5** that blocks bootstrap:
- **Issue**: Redis IPv6 loopback binding failure on 64-bit PiOS
- **Impact**: Bootstrap fails with "Error connecting to Redis" unless workaround is applied
- **Status**: OPEN as of June 2026; no official fix released
- **Workarounds available**: Three options documented in DISCOURSE_DEPLOYMENT_TECHNICAL_SPEC.md
  - Workaround 1: Disable IPv6 in Docker (simplest, 2 min)
  - Workaround 2: Run Redis on host (more reliable, 10 min)
  - Workaround 3: Use Bitnami image (untested on this hardware, 5 min)

**This is not a deal-breaker**, but it does mean Discourse deployment requires an extra 10–15 minutes of troubleshooting if you choose that path. Nextcloud+Matrix has no known Pi5 blockers.

---

## REVISED RECOMMENDATION: Nextcloud+Matrix

**Nextcloud+Matrix is NOW RECOMMENDED** in light of the Discourse IPv6 blocker.

### Reasons

**1. No known Pi5 blockers**: Nextcloud and Matrix Synapse both have official ARM64 Docker images with no reported Pi5 issues. Deployment will proceed without requiring workarounds or special fixes.

**2. Better feature set for Phase 5.1**: 
   - Real-time collaboration and chat (Matrix rooms)
   - Offline editing support (Nextcloud Desktop sync)
   - End-to-end encryption (Matrix E2E) for sensitive content
   - Better privacy posture (federation-ready, decentralized)

**3. Memory is manageable**: 7.9 GB available, 5.5 GB peak usage at 100 users. While tighter than Discourse (which uses 2–3 GB), modern Nextcloud+Matrix is well-tuned for resource constraints. Headroom is sufficient for the 20–50 user target.

**4. Deployment is straightforward**: 4–6 hours is acceptable for a one-time setup. Docker Compose is simpler than managing Discourse's launcher script + workarounds.

**5. Better alignment with systems-resilience philosophy**: Offline-first authoring, E2E encryption, and federation support are philosophical fits for a resilience-focused project.

### Discourse is Still Viable If:
- You accept the IPv6 workaround (most reliable: disable IPv6 in container, 2 min extra)
- You prioritize deployment speed (2–3 hours vs 4–6 hours)
- You prefer forum discussion over real-time chat
- You want maximum operational simplicity long-term

**Trade-off summary**:
- **Discourse**: Faster deployment (needs workaround), simpler ops, forum-based
- **Nextcloud+Matrix**: No blockers, richer features (offline + E2E + chat), modern stack, slightly longer deployment

---

## User Decision Form

**Decision required by**: June 15, 2026 EOD

```
PLATFORM DECISION — June 14-15, 2026

Selected Platform: [ ] Discourse (RECOMMENDED)
                   [ ] Nextcloud + Matrix (accept RAM risk and ARM64 limitations)

Primary reasons for selection:
1. _____________________________________________
2. _____________________________________________

Deployment information needed (if Discourse chosen):
- SMTP host + credentials: ________________________
- Hostname or Tailscale IP to use: ________________
  (if using Tailscale MagicDNS: raspby1.your-tailnet.ts.net)
  (if using raw IP: 100.120.18.84)

Decided by: _________________  Date: ____________
```

---

## Next Steps

### If You Choose Discourse (Recommended)

**What you need to provide**:
1. SMTP credentials (host, port, username, password) — OR confirm GitHub OAuth is acceptable instead of email signup
2. Confirm hostname to use: Tailscale MagicDNS name OR raw IP `100.120.18.84`
3. Admin email address

**What happens next**:
- Orchestrator executes `DISCOURSE_INSTALLATION_RUNBOOK.md` on raspby1
- Deployment completes in 2–3 hours from start
- Publication can proceed same day

**Runbook**: `DISCOURSE_INSTALLATION_RUNBOOK.md` (in this directory)

---

### If You Choose Nextcloud + Matrix

**What you need to acknowledge**:
1. OnlyOffice (collaborative editing) is not available on Pi5 ARM64
2. RAM headroom is tight at 100 concurrent users — some degradation is expected
3. Deployment takes 4–6 hours (plan for a full half-day)
4. Accept higher ops overhead (5–8 hrs/month)

**What you need to provide**:
1. SMTP credentials
2. Hostname(s) for Nextcloud and Matrix (either Tailscale or public domain)
3. Nextcloud admin username + password (to set in docker-compose.yml)

**Runbook**: `NEXTCLOUD_INSTALLATION_RUNBOOK.md` (in this directory)

---

## Risk Summary

| Risk | Discourse | Nextcloud+Matrix |
|------|-----------|-----------------|
| OOM kill under load | Very low (5+ GB free) | Moderate (marginal at 100 users) |
| ARM64 incompatibility | None known | OnlyOffice blocked |
| Deployment failure | 2% (simple, proven) | 10–15% (complex, 6 services) |
| Config error causes restart | Low (one file) | Moderate (6 config files) |
| Recovery time from failure | 30 min (one container) | 1–2 hours (diagnose which service) |
| Time to live | 2–3 hours | 4–6 hours |

---

## Rollback Procedures

### Discourse Rollback (if deployment fails or is abandoned)

**At any point before bootstrap completes** — no persistent state, clean exit:

```bash
# Remove discourse directory — no container exists yet
sudo rm -rf /var/discourse
# No further cleanup needed
```

**After bootstrap completes but before going live** — container exists, no user data:

```bash
cd /var/discourse
sudo ./launcher stop app
sudo ./launcher destroy app
# Container is gone; /var/discourse/shared/ holds the persistent volume
# To fully clean up:
sudo rm -rf /var/discourse
```

**After go-live with user data present** — preserve backup before rollback:

```bash
# 1. Stop container (preserves data)
cd /var/discourse && sudo ./launcher stop app

# 2. Archive the shared volume before deleting
tar czf /home/awank/backups/discourse-rollback-$(date +%Y%m%d).tar.gz \
    /var/discourse/shared/standalone/

# 3. Destroy container
sudo ./launcher destroy app

# 4. If switching to Nextcloud+Matrix: follow NEXTCLOUD_INSTALLATION_RUNBOOK.md
# If abandoning deployment: rm -rf /var/discourse (after confirming backup)
```

**Rollback time estimate**: 10 minutes (stop + destroy + cleanup)

---

### Nextcloud+Matrix Rollback (if deployment fails)

**Before `docker compose up`** — no state:

```bash
sudo rm -rf /opt/nextcloud-matrix
# Done
```

**After `docker compose up`, before user data present**:

```bash
cd /opt/nextcloud-matrix
docker compose down --volumes  # removes containers AND named volumes
sudo rm -rf /opt/nextcloud-matrix
```

**After go-live with user data present**:

```bash
cd /opt/nextcloud-matrix

# 1. Backup all volumes first
docker compose exec -T postgres pg_dumpall -U REPLACE_POSTGRES_USER \
    | gzip > /home/awank/backups/nc-matrix-rollback-$(date +%Y%m%d).sql.gz

# 2. Stop and remove containers + volumes
docker compose down --volumes

# 3. Remove config directory
sudo rm -rf /opt/nextcloud-matrix
```

**Rollback time estimate**: 20–30 minutes (due to 6-service complexity and volume removal time)

---

## Related Documents

- **Technical specs**: `NEXTCLOUD_DEPLOYMENT_TECHNICAL_SPEC.md`, `DISCOURSE_DEPLOYMENT_TECHNICAL_SPEC.md`
- **Installation runbooks**: `DISCOURSE_INSTALLATION_RUNBOOK.md`, `NEXTCLOUD_INSTALLATION_RUNBOOK.md`
- **Comprehensive decision history**: `PLATFORM_DECISION_MATRIX.md` (June 4 analysis, 900+ lines)
- **Infrastructure audit**: `PHASE_5_1_DEPLOYMENT_INFRASTRUCTURE_AUDIT.md` (June 7, confirmed Docker + 189GB)
- **Discourse detailed runbook**: `DISCOURSE_DEPLOYMENT_RUNBOOK.md` (June 8-specific, very detailed)
- **Block record**: BLOCKED.md — systems-resilience entry (blocked June 6, awaiting this decision)
