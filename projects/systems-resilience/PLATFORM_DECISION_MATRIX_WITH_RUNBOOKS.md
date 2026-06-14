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
| **Known blockers** | OnlyOffice ARM64 unavailable | None |

---

## RECOMMENDATION: Discourse

**Discourse is strongly recommended for this deployment.**

### Reasons

**1. RAM safety**: Discourse uses 2–3 GB at 100 users. Nextcloud+Matrix uses 4.5–5.5 GB at 100 users on a system with 7.3 GB usable. Nextcloud's margin is too thin for confidence. A spike in user traffic or a single memory leak in any of 6 containers can trigger an OOM kill and take down part of the stack.

**2. OnlyOffice is unavailable on ARM64**: The stated advantage of Nextcloud+Matrix for this project — collaborative in-browser document editing — is not achievable on the Pi5 ARM64. OnlyOffice has no ARM64 Docker image. The feature parity between the two platforms on Pi5 is therefore closer than it would be on x86 hardware.

**3. Deployment speed matters**: Discourse deploys in 2–3 hours (including the 15–25 min ARM64 compilation). Nextcloud+Matrix takes 4–6 hours with significantly more configuration surface area (docker-compose.yml, nginx.conf, homeserver.yaml, Element config, two database schemas). Every additional configuration file is a potential error source.

**4. The use case is publication, not collaboration**: Phase 5.1 is publishing 61,611 words of research for community reading and discussion. Discourse's forum model — one topic per document, replies for discussion, threading, categories — is a better interface for this use case than Nextcloud's file-folder metaphor.

**5. Governance is built-in**: Discourse's trust level system automatically promotes engaged readers. Moderating 50–200 members in Nextcloud+Matrix requires manual room management and has no equivalent automation.

**6. Operational simplicity under solo maintenance**: This deployment is maintained by one person (or the orchestrator acting on their behalf). Two to three hours per month of ops overhead (Discourse) is sustainable. Five to eight hours per month (Nextcloud+Matrix) is not.

### When to Choose Nextcloud+Matrix Instead

Choose Nextcloud+Matrix if:
- You require end-to-end encryption for sensitive community communications
- You require Matrix federation (joining the broader Matrix network)
- You have a requirement for offline-first document editing with sync (and are on x86 hardware, not Pi5)
- You have 16 GB RAM available on a non-ARM64 host

None of these conditions apply to the current Pi5 deployment.

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

## Related Documents

- **Technical specs**: `NEXTCLOUD_DEPLOYMENT_TECHNICAL_SPEC.md`, `DISCOURSE_DEPLOYMENT_TECHNICAL_SPEC.md`
- **Installation runbooks**: `DISCOURSE_INSTALLATION_RUNBOOK.md`, `NEXTCLOUD_INSTALLATION_RUNBOOK.md`
- **Comprehensive decision history**: `PLATFORM_DECISION_MATRIX.md` (June 4 analysis, 900+ lines)
- **Infrastructure audit**: `PHASE_5_1_DEPLOYMENT_INFRASTRUCTURE_AUDIT.md` (June 7, confirmed Docker + 189GB)
- **Discourse detailed runbook**: `DISCOURSE_DEPLOYMENT_RUNBOOK.md` (June 8-specific, very detailed)
- **Block record**: BLOCKED.md — systems-resilience entry (blocked June 6, awaiting this decision)
