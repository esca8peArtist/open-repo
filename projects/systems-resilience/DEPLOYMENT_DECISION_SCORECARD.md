---
title: "Deployment Decision Scorecard — June 2026"
project: systems-resilience
phase: "5.1 — Deployment Unblock"
created: 2026-06-17
status: FINAL
purpose: "8-factor scoring matrix with per-factor comparison and overall recommendation. This is the single document to read to make the platform decision."
companion_docs:
  - PLATFORM_SELECTION_FINAL_ANALYSIS_JUNE_2026.md
  - DEPLOYMENT_TIMELINE_COMPARISON_JUNE_2026.md
---

# Deployment Decision Scorecard — June 2026

**Platform A**: Nextcloud 34 + Matrix Synapse  
**Platform B**: Discourse (ARM64 Docker, launcher method)  
**Hardware**: Raspberry Pi 5, 8 GB RAM, raspby1 (100.70.184.84)  
**Date**: June 17, 2026. Deadline already passed. Decide today.

---

## 8-Factor Scoring Matrix

Scores: 1 (poor) to 10 (excellent). Weight reflects importance to Phase 5.1 success.

| # | Factor | Weight | Nextcloud+Matrix | Discourse | Winner |
|---|--------|--------|-----------------|-----------|--------|
| 1 | Deployment speed | 20% | 4 | 9 | Discourse |
| 2 | Operational overhead | 20% | 4 | 9 | Discourse |
| 3 | Feature fit for Phase 5.1 | 20% | 6 | 7 | Discourse (marginal) |
| 4 | Community health | 10% | 8 | 8 | Tie |
| 5 | Docker on ARM64 compatibility | 10% | 10 | 9 | Nextcloud (marginal) |
| 6 | Security posture | 10% | 8 | 6 | Nextcloud |
| 7 | Upgradability | 5% | 5 | 9 | Discourse |
| 8 | Long-term roadmap | 5% | 8 | 7 | Nextcloud (marginal) |
| **TOTAL (weighted)** | | | **6.05** | **7.90** | **Discourse** |

---

## Factor-by-Factor Detail

### Factor 1: Deployment Speed (Weight: 20%)

**Nextcloud+Matrix — Score: 4/10**

Deployment requires configuring 4 config files (~310 lines), pulling 6 Docker images, and initializing 6 services in dependency order. Total wall-clock time: 5-6 hours under optimal conditions. A single service misconfiguration adds 30-60 minutes of debugging. First-time deployers should budget 7 hours.

Why this matters now: the deadline has already passed. Every hour saved in deployment is an hour closer to Phase 5 go-live.

**Discourse — Score: 9/10**

One config file (app.yml, ~80 lines). One bootstrap command. Typical Pi5 completion: 2 hours 30 minutes including SSL and first login. The IPv6 workaround (W1) adds 5 minutes and must be done before bootstrap. With W1 pre-applied, deployment is straightforward and the launcher handles everything else.

**Edge case**: If bootstrap fails for any reason, `./launcher rebuild app` retries from scratch (adds ~40 min, but the path is clear and documented).

---

### Factor 2: Operational Overhead (Weight: 20%)

**Nextcloud+Matrix — Score: 4/10**

6 containers to monitor, 6 log streams, 6 images to update, 6 volumes to back up. Monthly admin time: 6-8 hours under normal conditions, 9+ hours if an incident occurs. Managing Nextcloud and Matrix separately means two different admin interfaces, two different update cycles, and two different troubleshooting domains.

Admin training to operational independence: 10-15 hours over weeks 1-2.

**Discourse — Score: 9/10**

1 container managed by the launcher. Admin dashboard is a web GUI at `/admin`. Backups are automated (daily by default, produces a single `.tar.gz`). Updates are `git pull && ./launcher rebuild app`. Monthly admin time: 2-3 hours.

Admin training to operational independence: 3-5 hours over week 1. The admin panel has inline documentation for every setting.

---

### Factor 3: Feature Fit for Phase 5.1 (Weight: 20%)

**Nextcloud+Matrix — Score: 6/10**

What it provides well:
- Offline document authoring (Nextcloud Desktop sync — valuable if authors have spotty connectivity)
- File versioning and large file support
- E2E encryption for sensitive coordination (Matrix rooms)
- Calendar/contacts (GroupDAV, useful for coordinating review timelines)

What it does NOT provide on Pi5 ARM64:
- Real-time document co-editing (OnlyOffice is x86-only; not available on ARM64)
- Good moderation tooling (Matrix rooms are chat, not structured forums)
- Trust levels / author reputation system

**Discourse — Score: 7/10**

What it provides well:
- Superior threaded discussion (research domain topics, peer review threads)
- Trust levels (auto-escalate authors who engage consistently)
- Moderation queue (prevent spam/off-topic without manual review of every post)
- File attachments (research PDFs, up to 100 MB per file by default)
- Better user adoption curve (30 min vs 2-3 hrs for Nextcloud+Matrix)

What it does NOT provide:
- Offline authoring (requires internet for every interaction)
- E2E encryption (TLS only; admin can read all content)
- Large file hosting (file system management)
- Real-time collaboration (also absent, same as Nextcloud on ARM64)

**The tie-breaker within this factor**: Neither platform offers real-time document co-editing on Pi5 ARM64 (OnlyOffice unavailable). This was the main feature advantage previously attributed to Nextcloud. Without it, Discourse's superior discussion model, user adoption curve, and moderation tooling give it a narrow edge for a 40-50 person research collaboration.

**Override condition**: If offline authoring is a hard requirement for Phase 5 authors (e.g., significant portion working from locations with unreliable internet), Nextcloud wins this factor decisively (10/10 vs 0/10 for offline authoring alone).

---

### Factor 4: Community Health (Weight: 10%)

**Nextcloud+Matrix — Score: 8/10**

- Nextcloud: Large community, backed by Nextcloud GmbH, active development (v34 released June 11, 2026). EU government adoption validates longevity.
- Matrix: Open standard (Matrix.org Foundation governance), growing adoption, multiple server implementations (Synapse, Dendrite, Conduit) prevent single-vendor lock-in.
- ARM64 support: Both have active ARM64 maintenance.

**Discourse — Score: 8/10**

- Large commercial community (Discourse Inc.), excellent official support at meta.discourse.org.
- Active development: Regular monthly releases (2026.5.x as of June 2026).
- ARM64 support: Native ARM64 images since ~2022, regularly maintained.
- Potential concern: Commercial company competes with its own self-hosted offering (Discourse.org hosted service). Risk that self-hosted support deprioritizes over time.

**Result**: Tie. Both platforms are healthy communities with active ARM64 support.

---

### Factor 5: Docker on ARM64 Compatibility (Weight: 10%)

**Nextcloud+Matrix — Score: 10/10**

- Nextcloud 34: Official `arm64v8/nextcloud:34` image. No known Pi5-specific issues.
- Matrix Synapse v1.134: ARM64 build in official Docker Hub. Pi5 deployment confirmed at 8 GB RAM.
- Redis, PostgreSQL, Nginx: All have mature ARM64 images with zero known Pi5 issues.
- OnlyOffice: NOT available on ARM64. This is an accepted limitation (co-editing not possible on Pi5).

**Discourse — Score: 9/10**

- Native ARM64 tags on Docker Hub (`discourse/discourse:2026.5.0-arm64`). Confirmed.
- Pi5 blocker: IPv6 loopback issue during bootstrap. Workaround W1 is 5 minutes, pre-deployment. Confirmed working.
- One-point deduction for the required workaround vs Nextcloud's clean zero-issue deployment.

**Result**: Nextcloud wins by 1 point (marginal). Discourse's workaround is trivial and should not be a decisive factor.

---

### Factor 6: Security Posture (Weight: 10%)

**Nextcloud+Matrix — Score: 8/10**

- Matrix provides genuine E2E encryption for room content. Even if server is compromised, encrypted room messages are not readable by attacker.
- Nextcloud file storage is not encrypted at rest by default (optional server-side encryption available but with performance cost).
- 6 attack surfaces (one per container) vs Discourse's 1. Higher patch cadence required. However, all components are open-source and audited.
- Data sovereignty: Full. No external dependencies.

**Discourse — Score: 6/10**

- TLS in transit: Yes (Let's Encrypt via launcher).
- No E2E encryption: Admin and server operator can read all content. For research content that is eventually published, this is acceptable. For sensitive pre-publication discussions, this is a limitation.
- 1 attack surface (single container). Easier to monitor for vulnerabilities, but entire platform fails if that one surface is compromised.
- Data sovereignty: Full. No external dependencies.
- Security patch cadence: Monthly releases typically include security fixes. Single `./launcher rebuild app` applies all patches.

**Result**: Nextcloud+Matrix wins on security depth due to E2E encryption. If Phase 5 content is not sensitive (published research, not private data), the gap narrows but Nextcloud still has architectural advantage.

---

### Factor 7: Upgradability (Weight: 5%)

**Nextcloud+Matrix — Score: 5/10**

Upgrade involves coordinating 6 image updates. Must check compatibility between Nextcloud, Synapse, and database schema changes. Occasional breaking changes between major versions require manual database migrations. Typical upgrade cycle: 60-90 minutes per major release.

Risk: One service upgrades successfully but breaks integration with another service (e.g., Nextcloud API change affects Matrix bridge). Debugging this requires multi-service log analysis.

**Discourse — Score: 9/10**

`git pull && ./launcher rebuild app`. The launcher handles all internal service upgrades (Rails, PostgreSQL, Redis, Nginx) as a coordinated unit. Typical upgrade: 20-40 minutes. Rollback path exists (restore from auto-backup or use previous container).

**Result**: Discourse wins decisively. Upgrade complexity is a significant long-term operational difference.

---

### Factor 8: Long-Term Roadmap (Weight: 5%)

**Nextcloud+Matrix — Score: 8/10**

- Nextcloud is on a strong trajectory with Hub releases (Hub 26 in June 2026). Federation features for cross-instance collaboration are actively developed — relevant if Phase 6+ involves multiple Pi5 nodes.
- Matrix is an open standard. Even if Matrix Synapse development slows, the protocol persists and alternative implementations exist.
- Open-source governance reduces vendor lock-in risk.

**Discourse — Score: 7/10**

- Discourse Inc. is a stable commercial company (founded 2013, over a decade of continuous development).
- Self-hosted support is reliable as of 2026; risk is a 5-10 year horizon where commercial priorities shift to hosted Discourse.org.
- Plugin ecosystem is large but some plugins are commercial (not a current issue, but a trend to monitor).
- Data export is standard (full PostgreSQL dump + S3 backup format) — migration out is achievable.

**Result**: Nextcloud+Matrix wins marginally on long-term open-source governance.

---

## Overall Recommendation

| Platform | Weighted Score | Confidence |
|----------|---------------|------------|
| Nextcloud+Matrix | 6.05 / 10 | N/A |
| Discourse | 7.90 / 10 | N/A |
| **RECOMMENDATION** | **Discourse** | **87%** |

**Recommendation: Deploy Discourse.**

The 1.85-point weighted advantage is driven by deployment speed and operational overhead — the two highest-weighted factors (20% each). These are not abstract preferences; they directly determine how quickly Phase 5.1 unblocks and how much admin time is consumed per month for the project lifetime.

The IPv6 workaround is not a meaningful objection. It is 5 minutes of one-time configuration that has been confirmed working on Pi5 by multiple community members. It is not a stability risk post-deployment.

Confidence is 87%, not higher, because the feature fit factor (Factor 3) is sensitive to one unknown: whether offline authoring is a hard requirement for Phase 5 authors. If offline authoring is confirmed as required, Nextcloud+Matrix is the correct choice despite its operational disadvantages.

---

## Decision Gate: Two Questions to Answer Right Now

Before deploying anything, answer these two questions honestly:

**Question 1**: Do any Phase 5 authors need to edit documents offline (without internet access)?

- YES → Deploy Nextcloud+Matrix. Discourse cannot serve this requirement at all.
- NO → Continue to Question 2.

**Question 2**: Is E2E encryption required for the content sensitivity of Phase 5 discussions?

- YES → Deploy Nextcloud+Matrix (Matrix provides E2E; Discourse does not).
- NO → Deploy Discourse.

If the answer to both questions is NO, deploy Discourse. No further analysis needed.

---

## Deployment Activation Instructions

### If Discourse Chosen

Provide to orchestrator:

```
PLATFORM DECISION: Discourse

Required values:
1. Hostname: ___________________
   (Options: Tailscale MagicDNS e.g. raspby1.tailnet.ts.net, OR custom domain)
2. SMTP host: ___________________
3. SMTP port: ___________________
4. SMTP username: ___________________
5. SMTP password: ___________________
6. Admin email: ___________________
   (e.g. wanka95@gmail.com)
7. GitHub OAuth: YES / NO
   (If YES, provide GitHub OAuth App Client ID + Secret)
```

Orchestrator will then execute `DISCOURSE_INSTALLATION_RUNBOOK.md`. Go-live in ~2.5 hours.

### If Nextcloud+Matrix Chosen

Provide to orchestrator:

```
PLATFORM DECISION: Nextcloud+Matrix

Required values:
1. Nextcloud hostname: ___________________
2. Matrix hostname: ___________________
3. Element Web hostname: ___________________
4. SMTP host: ___________________
5. SMTP port: ___________________
6. SMTP username: ___________________
7. SMTP password: ___________________
8. Admin email: ___________________
9. Confirm OnlyOffice unavailable on ARM64: YES / NO
10. Confirm offline authoring is primary reason for this choice: YES / NO
```

Orchestrator will then execute `NEXTCLOUD_MATRIX_DEPLOYMENT_SOP.md`. Go-live in ~5.5 hours.

---

## Summary Table

| | Discourse | Nextcloud+Matrix |
|--|-----------|-----------------|
| **Weighted score** | **7.90 / 10** | 6.05 / 10 |
| **Recommended?** | **YES** | Only if offline or E2E required |
| **Deployment time** | **2.5 hours** | 5.5 hours |
| **Monthly ops** | **2-3 hrs** | 6-8 hrs |
| **Pi5 blockers** | 1 (5-min workaround) | None |
| **Offline authoring** | NO | YES |
| **E2E encryption** | NO | YES |
| **Admin learning curve** | 3-5 hrs | 10-15 hrs |
| **OOM risk at 50 users** | Negligible | Low |
| **Confidence** | **87%** | 87% (if offline/E2E needed) |

---

## Appendix: Scoring Methodology Notes

Weights were assigned to reflect Phase 5.1 context:

- **Deployment speed (20%)** and **Operational overhead (20%)** are co-equal at top weight because: (a) the deadline has already been missed — speed is critical, and (b) the platform will operate for 3-6 months during Phase 5 — operational burden is a recurring cost that compounds.
- **Feature fit (20%)** is high weight because a platform that doesn't fit the use case creates downstream author friction.
- **Community health (10%)**, **ARM64 compatibility (10%)**, **Security (10%)** are secondary but real factors.
- **Upgradability (5%)** and **Long-term roadmap (5%)** are low weight because Phase 5 is a 3-6 month horizon; long-term concerns are real but not the deciding factor today.

---

## Document Confidence Statement

Confidence: 87% on Discourse recommendation.

Gaps that could change the recommendation:
1. Offline authoring requirement not explicitly confirmed or denied for Phase 5 cohort.
2. Content sensitivity classification not explicitly stated (MODERATE was assumed from project context).
3. Long-term admin capacity unknown (if admin time is very constrained, operational overhead gap becomes larger; Discourse advantage grows).

None of these gaps require further research. They require a 5-minute conversation with the project lead to clarify. The two decision-gate questions above are sufficient to resolve all three gaps.

---

*Analysis produced by General Research Agent, Session 3780 equivalent, June 17, 2026. Based on: Session 3563 findings, Session 3773 updates, live Discourse meta.discourse.org thread data, Docker Hub ARM64 image confirmation, Nextcloud 34 changelog, community Pi5 deployment reports.*
