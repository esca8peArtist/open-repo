---
title: "Phase 6 Platform Decision Support Checklist — June 3 Decision Gate"
project: systems-resilience
phase: 6
status: DECISION-READY
created: 2026-06-02
decision_deadline: 2026-06-03
operational_target: 2026-06-05 00:00 UTC
cross_references:
  - PHASE_6_PLATFORM_ANALYSIS_v2.md
  - PHASE_6_IMPLEMENTATION_GUIDE_OPTION_A_DISCOURSE.md
  - PHASE_6_IMPLEMENTATION_GUIDE_OPTION_B_MIGHTY_NETWORKS.md
  - PHASE_6_IMPLEMENTATION_GUIDE_OPTION_C_NEXTCLOUD_MATRIX.md
---

# Phase 6 Platform Decision Support Checklist

**Decision required by June 3. Platform must be operational by June 5 00:00 UTC.**

---

## Quick-Reference Comparison

| Dimension | Option A: Discourse | Option B: Mighty Networks | Option C: Nextcloud + Matrix |
|---|---|---|---|
| Score | 8.0/10 | 5.5/10 | 8.5/10 |
| Annual cost | $60–$300 | $950 | $0 on raspby1 |
| Setup time | 6–7 hours | 3–4 hours | 7–10 hours |
| Technical requirement | Docker, DNS | None | Docker Compose |
| Offline support | Read-only (PWA cache) | None | Full (files + messages) |
| Document collaboration | No | No | Yes (real-time co-editing) |
| Mobile app | PWA (web-based) | Native iOS/Android | Native iOS/Android (both apps) |
| Moderation automation | Best (Akismet + trust levels) | Adequate | Adequate (Mjolnir bot) |
| GitHub Pages integration | Best (embed widget) | Links only | Good (share links) |
| Vendor lock-in | None (self-hosted AGPL) | High | None (self-hosted AGPL) |
| Can go live by June 5? | Yes (DNS is main variable) | Yes (same day) | Yes (if raspby1 ready) |

---

## Decision Flowchart (Answer in order — stop at first match)

**Q1: Is off-grid or connectivity-uncertain access a real requirement for community members?**
- Yes → **Option C** is the only viable choice. No other platform functions without internet.

**Q2: Does the community need to co-author documents (shared protocol development, resource guide editing)?**
- Yes → **Option C** (Nextcloud is the only platform with real-time collaborative editing).
- No → Continue to Q3.

**Q3: Is $950/year a comfortable budget allocation for this platform?**
- No (budget is tight; $0–$300/yr preferred) → **Option A** (Discourse) or **Option C** (raspby1 at $0).
- Yes → Continue to Q4.

**Q4: Is minimizing setup complexity the top priority (no Docker, no server, no DNS)?**
- Yes → **Option B** (Mighty Networks — operational in one afternoon, zero technical steps).
- No → **Option A** or **Option C** (lower cost, more control).

**Q5: Is GitHub Pages embed/integration a priority?**
- Yes → **Option A** (Discourse embed widget is superior; no other platform offers it).

---

## Fastest Setup to Operational

**Winner: Option B (Mighty Networks)** — 3–4 hours, entirely in a browser, no server, no DNS wait.

If the June 5 deadline is in jeopardy due to other commitments or if technical capacity is uncertain, Option B is the lowest-risk path to "operational by June 5." The 14-day trial means no financial commitment until June 17.

**Second fastest: Option A (Discourse)** — 6–7 hours, but DNS propagation adds 1–24 hours of calendar time that cannot be compressed. Start DNS on the same day the decision is made.

**Most complex: Option C (Nextcloud + Matrix)** — 7–10 hours of active configuration, all sequential (cannot parallelize Nextcloud and Matrix setup meaningfully). If raspby1 has any unexpected disk, memory, or Docker issues, the timeline extends into June 5.

---

## Lowest Ongoing Cost

**Winner (tied): Option C on raspby1 ($0/year software) and Option A self-hosted ($60–$180/year VPS).**

Option C on raspby1 has zero marginal cost since raspby1 is already running. Option A requires a VPS ($5–15/month) but adds the Discourse moderation infrastructure and GitHub Pages integration that Option C lacks.

Option B ($950/year) costs 5–15x more than the self-hosted options with lower scores in 6 of 8 dimensions.

---

## Offline / Off-Grid Support

**Winner: Option C (Nextcloud + Matrix)** — the only platform with full offline capability.

- Nextcloud desktop and mobile apps sync files locally; accessible without internet.
- Element X (Matrix client) stores messages locally; readable and composable offline; sends on reconnect.
- Can run entirely on LAN (no internet required for internal community use).

Option A provides read-only access via PWA service worker (previously loaded pages are readable). Option B provides no offline access whatsoever.

**If any Phase 6 community members are rural, semi-rural, or in connectivity-uncertain situations, only Option C meets their needs.**

---

## Decision Summary for June 3

| If your situation is... | Choose |
|---|---|
| Need offline support or document co-editing | **C** |
| Lowest cost on existing hardware | **C** |
| Fastest setup, no technical capacity available | **B** |
| Best moderation + GitHub Pages integration, moderate budget | **A** |
| Budget is $0/year, Docker available | **C** |
| Prefer no vendor dependency, long-term control | **A or C** |

**Recommendation from scoring**: Option C (8.5/10) is the highest-scoring choice and costs nothing on raspby1. If 7–10 hours of setup time is available June 3–4, Option C is the strongest long-term foundation. If setup time is constrained to one afternoon, Option B delivers a working community platform by June 5 with no technical risk.
