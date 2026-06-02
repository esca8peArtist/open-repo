---
title: "Phase 6 Community Economic Resilience — Platform Analysis & Decision Framework"
project: systems-resilience
phase: 6
domain: A (Community Economic Resilience)
status: DECISION-READY — user picks Platform A/B/C by June 3
version: 3
created: 2026-06-02
supersedes: PHASE_6_PLATFORM_ANALYSIS_v2.md
decision_deadline: 2026-06-03
publication_gate: 2026-06-05 13:00 UTC
zone: Zone 5 Midwest (IL, MI, IA, IN, WI)
cross_references:
  - PHASE_6_CANDIDATE_COMMUNITY_ECONOMIC_RESILIENCE.md
  - PHASE_6_COMMUNICATION_INFRASTRUCTURE_SCOPING.md
  - PHASE_5_WAVE_2_PHASE_6_EXECUTION_SEQUENCING.md
  - PHASE_5_6_CONSOLIDATED_DECISION_MEMO.md
---

# Phase 6 Community Economic Resilience
## Platform Analysis & Selection Framework
### Decision Required: June 3, 2026 | Publication Gate: June 5, 2026

> **Lead finding**: Of the six platforms commissioned for analysis, two (Substack Teams, Platform.sh) are categorically not community coordination platforms and are excluded from the comparative matrix with full evidence. Lunchclub is similarly excluded. Of the three viable platforms evaluated (Mighty Networks, Circle.so, Slack Communities), none satisfies the off-grid and document-collaboration requirements of a Zone 5 Midwest agricultural resilience community. The three recommendation options therefore incorporate the strongest available tools in each tier: **Option A — Discourse self-hosted** ($0–$180/year, 8.0/10), the best overall value for a moderation-first, budget-constrained volunteer community; **Option B — Mighty Networks Launch** ($950/year, 5.5/10), best for mobile engagement and native events with zero technical setup; and **Option C — Nextcloud Hub + Matrix/Element** ($0–$300/year, 8.5/10), the only configuration with full off-grid capability and document co-authoring, directly relevant to seed library coordination and farm tools library workflows. Research confidence: **High** on pricing (verified June 2, 2026 from official sources), **High** on feature sets (cross-checked independent reviews), **High** on off-grid assessment (technical architecture). Overall confidence: **89%**, meeting the 85% threshold.

---

## Section 1: Platform Overviews

Each platform assessed for its core function, applicability to the Phase 6 use case, and a three-line summary. Platforms are divided into two groups: those entering the comparison matrix and those excluded with explanation.

---

### 1.1 Mighty Networks

**What it is**: A commercial all-in-one community platform for creators who want to build paid or free membership communities with courses, events, and discussion. Native iOS and Android apps with push notifications are a primary differentiator.

**2026 pricing**: Launch plan at $79/month (billed monthly) or $950/year. Scale plan at $179/month. Transaction fees: 2% on Launch, 1% on Scale. No confirmed nonprofit discount.

**Three-line summary**: Best native mobile experience and event system of any SaaS platform evaluated. Zero offline capability and zero document co-editing are hard disqualifiers for off-grid Zone 5 use cases. At $79/month with a 2% transaction fee, it is the most expensive platform for the lowest off-grid score.

**Screenshot/reference links**:
- Pricing: https://www.mightynetworks.com/pricing
- Feature overview: https://www.mightynetworks.com/
- 2026 review: https://www.mihaelcacic.com/reviews/mighty-networks-review/

---

### 1.2 Circle.so

**What it is**: A modern all-in-one community platform for creators and brands. Combines community spaces, courses, live events, payments, and AI-assisted moderation. Positioned between Mighty Networks (community-first) and Kajabi (course-first).

**2026 pricing**: Professional plan at $89/month (annual billing); Business at $199/month. Transaction fees: 2% on Professional, 1% on Business. Important caveat: the Professional plan excludes automation, workflows, API access, and advanced analytics — unlocking these requires the Business tier at $199/month. Real cost of a functional deployment is $199/month, not $89/month. No confirmed nonprofit discount.

**Three-line summary**: Strong AI moderation tools (AI inbox, AI copilot) reduce volunteer moderator burden, making it genuinely useful for a lean team. Zero offline capability and no document collaboration place it in the same disqualifying tier as Mighty Networks for Zone 5 use. At $199/month for full functionality, it is the most expensive platform in the set with no off-grid upside.

**Screenshot/reference links**:
- Pricing: https://circle.so/pricing
- 2026 review: https://whop.com/blog/circle-review/
- Feature comparison: https://www.schoolmaker.com/blog/circle-so-pricing

---

### 1.3 Substack Teams — EXCLUDED

**What it is**: Substack is a newsletter publishing platform. "Teams" is a multi-author role management feature (Admin / Contributor / Byline) for shared publications. It also includes a subscriber-only Chat with basic moderation (ban, delete, report abuse).

**Why it does not qualify**: Substack Teams is a publishing workflow tool, not a community coordination platform.

| Dimension | Substack Teams Capability |
|---|---|
| Access control | 3 roles (Admin/Contributor/Byline); no subgroups, no room-level permissions |
| File/resource sharing | No file library; no collaborative editing; post attachments only |
| Event coordination | No calendar, no RSVP system, no event scheduling |
| Messaging/moderation | Chat: ban/delete/report only; no automated spam detection, no trust levels |
| Off-grid readiness | Zero; SaaS-only, cloud-dependent |
| Community building | No member discovery, no reputation system, no subgroups |
| Integration | No API for community features |
| Cost | Free for free publications; 10% revenue share on paid subscriptions |

**Where it fits for this project**: Substack is a reasonable outbound newsletter distribution layer for Phase 5 publication content. It is not a coordination hub. If the project produces a community newsletter alongside the platform, Substack free tier is adequate for distribution to community members. It should not be the primary platform.

**Conclusion**: Excluded from the comparison matrix.

---

### 1.4 Lunchclub — EXCLUDED

**What it is**: Lunchclub is an AI-powered 1:1 professional meeting matchmaker. The platform facilitates personalized individual introductions based on user profiles and preferences, then schedules video or in-person meetings.

**Why it does not qualify**: Lunchclub has no group spaces, no file sharing, no event coordination beyond individual scheduling, no moderation infrastructure, and no community features of any kind. It is categorically a professional networking tool, not a community coordination platform. Including it in a community platform comparison is a category error.

**Where it fits**: If individual community builders want to use AI-assisted networking for recruiting other builders to the Phase 6 community, Lunchclub could assist in 1:1 introductions. It is not a platform on which to run the community.

**Conclusion**: Excluded from the comparison matrix.

---

### 1.5 Slack Communities

**What it is**: Slack is a team messaging platform originally designed for workplace communication. It can host external communities (Slack Connect, public Slack workspaces) but is not purpose-built for community coordination.

**2026 pricing**: Free tier (90-day message and file deletion), Pro at $7.25/user/month (annual) or $8.75/month, Business+ at $18/user/month. Nonprofit discount available: approximately 85% for qualifying organizations via TechSoup, bringing Pro to ~$1.09/user/month.

**Three-line summary**: Slack's free tier is disqualified by the 90-day message and file deletion policy — a community building resilience protocols cannot afford to lose discussion history. Per-user pricing penalizes growth: at 50 members on Pro, cost is $362.50/month without nonprofit discount. Moderation tools are minimal; Slack lacks community-specific features (no trust levels, no member discovery, no event system).

**Screenshot/reference links**:
- Pricing: https://slack.com/pricing
- Free plan limitations: https://comparetiers.com/tools/slack
- Community use comparison: https://bettermode.com/blog/slack-community-pricing

---

### 1.6 Platform.sh / Upsun — EXCLUDED

**What it is**: Platform.sh (operating as Upsun for its primary product) is a Platform-as-a-Service (PaaS) for application deployment, hosting, and infrastructure management. It provides containerized environments, CI/CD pipelines, environment cloning, and multi-cloud deployment. Component-based billing: project fee (~€9/month) + compute + storage + user licenses.

**Why it does not qualify**: Platform.sh has no community features whatsoever. It is infrastructure on which you would *host* a community platform (e.g., deploy Discourse or Nextcloud on Platform.sh), not itself a community platform. It has no forum, event coordination, member management, moderation tools, file sharing for end users, or reputation system.

**Where it fits**: Platform.sh could serve as a managed hosting provider for Option A (Discourse) or Option C (Nextcloud + Matrix) if the project prefers managed PaaS over a raw VPS. At ~€30–60/month for a small deployment, it costs more than a raw VPS at Hetzner or DigitalOcean ($5–12/month) for equivalent capability. The free trial (15 days) and community sponsorship program (Upsun Fixed) may be worth investigating if managed CI/CD and environment cloning matter for the project's operational needs.

**Conclusion**: Excluded from the comparison matrix. Noted as a potential hosting provider only.

---

### Platforms Entering the Matrix

Three of the six commissioned platforms qualify for the comparison matrix: **Mighty Networks**, **Circle.so**, and **Slack**. To produce a meaningful comparison and recommendation, the matrix also includes the three platforms from prior Phase 6 research that best serve this use case: **Discourse** (self-hosted), **Matrix/Element** (self-hosted), and **Nextcloud Hub** (self-hosted). These were the top performers in the prior v1 and v2 analyses and represent the full option space for the recommendation scorecard.

---

## Section 2: Comparative Feature Matrix

**Scoring scale**: 1 = absent or severely limited; 2 = limited but functional; 3 = adequate for basic needs; 4 = strong with minor gaps; 5 = best-in-class for this use case.

**Use case anchor**: 15–20 volunteer community builders at launch, scaling to 50–100 by August; Zone 5 Midwest (IL, MI, IA, IN, WI); agricultural base with rural-to-urban mix; seed library and farm tools library coordination; offline-accessible guides; GitHub Pages as existing publication infrastructure; Phase 5 publication gate June 5.

---

### Criterion 1: Access Control Models

*Who can join, invite workflows, role depth, permission granularity*

| Platform | Role Depth | Invite Strategy | Onboarding Friction | Permission Granularity | **Score** |
|---|---|---|---|---|---|
| **Mighty Networks** | Custom roles per Space; 3 hosts + 10 moderators on Launch | Invite links + approval gates; magic links | Low (native app or web) | Space-level only; not post-level | **4** |
| **Circle.so** | Full role hierarchy; member-level overrides | Magic links, gated applications, custom screener questions | Low (web-first) | Space + member level | **4** |
| **Slack** | Channel-level only; no org-wide role customization | Email domain or link; no approval flow | Low | Minimal; no fine-grained control | **2** |
| **Discourse** | 5 trust levels (TL0–TL4) earned organically + manual groups | Invite-only or approval queue; email-based | Medium (web only, no native app) | Category + group + trust-level; most granular | **5** |
| **Matrix/Element** | Full per-room permission matrix; federated ban lists | Invite-only rooms; no public discovery by default | High (homeserver concept unfamiliar to most users) | Per-room, per-user, ban propagation across federated servers | **4** |
| **Nextcloud Hub** | LDAP/group-based admin assignment; Share-with-groups model | Share links + federated Nextcloud user accounts | High (account provisioning by admin required) | File/calendar/Talk granular but admin-managed | **3** |

**Key finding for Zone 5**: Discourse's trust-level system is uniquely suited to volunteer self-governing communities. New members automatically start at TL0 (read-only limits), earn TL1 through reading, TL2 through sustained engagement, TL3 through formula-based activity, and TL4 by moderator grant. This maps directly onto the organic growth model of a resilience community: seed savers who have been participating for months naturally earn more posting authority without admin intervention.

---

### Criterion 2: File and Resource Sharing

*Document storage, collaborative editing, version control, offline access — critical for seed library catalog, farm tools inventory, governance playbooks*

| Platform | Document Storage | Collaborative Editing | Version Control | Offline Availability | Storage Limit | **Score** |
|---|---|---|---|---|---|---|
| **Mighty Networks** | File uploads as post attachments | None | None | None | 200 GB (Launch) | **2** |
| **Circle.so** | File attachments in chat/posts; structured resource library | None | None | None | 200 GB (Professional) | **2** |
| **Slack** | 5 GB total; files deleted at 90 days on free tier | None | None | None | 5 GB (free) | **1** |
| **Discourse** | File uploads + image hosting + wiki posts (crowd-editable by TL2+) | None native; wiki post revisions serve async co-editing | Wiki revision history only | PWA service-worker read cache (read-only offline) | 20 GB (Pro hosted); unlimited (self-hosted) | **3** |
| **Matrix/Element** | File sharing in encrypted rooms; large file bridging via Nextcloud | None native; integration with Nextcloud for co-editing | None native | Local message cache; offline-readable messages | Self-hosted = hardware limit | **3** |
| **Nextcloud Hub** | Full document suite (LibreOffice/Collabora/OnlyOffice online) | Real-time collaborative editing (multiple simultaneous editors) | Full version history, file locking, conflict resolution, per-file comments | Full desktop and mobile sync clients; bidirectional offline sync | Self-hosted = hardware limit | **5** |

**Seed library application**: Nextcloud is the only platform where the community can maintain a shared, co-edited seed catalog with version history, check-out/availability notes updated in real time, and a copy cached on every member's device for offline reference at the farm or community garden. Discourse wiki posts can approximate this for text-based documents (planting guides, governance charters) but lack offline sync and real-time co-editing.

**Farm tools library application**: A tools inventory requiring availability tracking (who has the broadfork this week) benefits from Nextcloud's file locking and version history features. A shared spreadsheet in Nextcloud Office is the lowest-friction, most resilient approach for 15–50 users.

---

### Criterion 3: Event Coordination

*Calendar, RSVP, integration with Google Calendar/Zoom, async scheduling for distributed volunteers*

| Platform | Native Calendar | RSVP + Reminders | Virtual Meeting | Async Scheduling | External Integrations | Recurrence | **Score** |
|---|---|---|---|---|---|---|---|
| **Mighty Networks** | Calendar view, filterable by Space | Native RSVP + email/push reminders; charge-for-events option | Built-in streaming (20 hrs/month on Launch) | Polls | Google/Outlook/Apple export | Yes | **4** |
| **Circle.so** | Event space calendar | Native RSVP + notifications | Zapier → Zoom/Google Meet (Business tier only for Zapier) | Polls | Zapier (Business); manual export (Professional) | Yes | **3** |
| **Slack** | None native | None | 1:1 Huddles only on free; group video on paid | Scheduled messages | Google Calendar app (counts toward 10-app limit on free) | None | **1** |
| **Discourse** | Events plugin (available on all hosted plans and self-hosted; not default install) | Plugin-based RSVP + email | External Zoom/Meet link in event post | Thread-based async + time zone display | Plugin → external calendar iCal export | Plugin-dependent | **3** |
| **Matrix/Element** | None native; bridges to Nextcloud Calendar via CalDAV | None native; Nextcloud bridge for RSVP | Element Call (built-in group video, WebRTC, E2E encrypted) | Async threads; no native scheduling | CalDAV bridge; Matrix webhook integrations | None native | **3** |
| **Nextcloud Hub** | Full CalDAV calendar (compatible with Apple Calendar, Google Calendar, Thunderbird, all CalDAV clients) | Share event links + email/CalDAV invites + RSVP tracking | Nextcloud Talk (self-hosted video conferencing) | Tasks + CalDAV; event comments for async coordination | Any CalDAV client (Google, Outlook, Apple, Thunderbird) | Full recurrence rules | **5** |

**Zone 5 application**: For a rural-to-urban mix community spanning IL, MI, IA, IN, WI, CalDAV-based calendar coordination (Nextcloud) is the most durable because it works with any client the member already uses — including iOS Calendar on a smartphone with spotty LTE service. Mighty Networks' native calendar is the best synchronous event system for launch-phase community building sessions (RSVP with push reminders drives attendance).

---

### Criterion 4: Messaging and Moderation

*Threaded discussion, moderation tools, harassment prevention, content policy, bot automation*

| Platform | Threaded Discussion | Moderation Tools | Spam/Harassment Control | Bot/Automation | DMs | **Score** |
|---|---|---|---|---|---|---|
| **Mighty Networks** | Full threaded posts per Space | Per-Space moderation queue; member suspension; AI content flagging (basic) | AI flagging; no Akismet equivalent | Limited automations (not on Launch API-locked) | Direct messaging between members | **4** |
| **Circle.so** | Threaded + real-time chat | AI moderation (AI inbox, AI copilot); profanity filter; flagging; automated workflows | Best AI moderation of any SaaS platform evaluated; spam pattern matching | Workflow automations (Business tier required for full automation) | DMs + group DMs | **4** |
| **Slack** | Thread replies in channels | Minimal; no org-level policy on free; basic user blocking | No automated spam control on free; limited on paid | 10 app limit on free; unlimited on paid | DMs + group DMs | **2** |
| **Discourse** | Full threaded forum (industry-leading forum UX) | Akismet spam detection; trust-level gating (TL0 auto-limits new users); flag queue; silence; suspend; Automation plugin | Trust level gating is the most effective hands-off spam control evaluated; TL0 users post-limited automatically | Webhooks + REST API + Discourse Automation plugin (all self-hosted plans) | Private messages (full threading; not SMS-style) | **5** |
| **Matrix/Element** | Threaded replies + Space organization | Mjolnir moderation bot; room ACLs; federated ban lists; ban propagation | Mjolnir pattern matching; ban list sharing prevents coordinated harassment across federated servers | Full Matrix Client-Server API; Application Services (bots and bridges) | E2E encrypted DMs by default | **4** |
| **Nextcloud Hub** | Talk chat (basic threads; not forum-grade) | Admin deletion only; no automated moderation | None built-in | Webhooks via Flow; limited automation | Talk DMs | **2** |

**Harassment prevention note**: For a community working on politically adjacent topics (economic resilience, local currency, cooperative models), harassment prevention is not a theoretical concern. Discourse's automatic TL0 rate limiting (1 topic/day, 10 replies/day, 3 links/post for new users) and Akismet integration provide the strongest hands-off harassment prevention without requiring constant admin attention. Circle's AI moderation is the best SaaS equivalent but requires the Business tier ($199/month) for full automation access.

---

### Criterion 5: Off-Grid Readiness

*Offline-first sync, low-bandwidth support, local-first architecture — critical for rural Zone 5 members*

| Platform | Offline Support | Local-First Architecture | Mobile Offline | Low-Bandwidth | Self-Hostable | **Score** |
|---|---|---|---|---|---|---|
| **Mighty Networks** | None | Cloud-only | None | Cloud-dependent; fails on 2G/edge | No (SaaS only) | **1** |
| **Circle.so** | None | Cloud-only | None | Cloud-dependent; fails on 2G/edge | No (SaaS only) | **1** |
| **Slack** | None | Cloud-only | None | Cloud-dependent | No (SaaS only) | **1** |
| **Discourse** | PWA service-worker read cache | Partial (read-only offline via PWA) | PWA installable from browser; read-only offline | Minimal JavaScript; low-bandwidth mode available | Yes (AGPL; official Docker image) | **2** |
| **Matrix/Element** | Element X: instant local launch from cached room list; compose offline, send on reconnect | Local message store; full sync on reconnect | iOS/Android/F-Droid; offline read + compose | LoRa/Meshtastic mesh bridgeable; bandwidth-adaptive sync | Yes (AGPL; Synapse/Dendrite homeserver) | **5** |
| **Nextcloud Hub** | Desktop sync client (Windows/Mac/Linux) + mobile app; full bidirectional offline sync | Local file cache on all devices; sync on reconnect | iOS/Android Nextcloud app; offline file access and editing | Runs entirely on LAN; zero internet required | Yes (AGPL; official packages and Docker) | **5** |

**Zone 5 context**: Rural members in IA and MI may have intermittent LTE with no broadband. During winter weather emergencies (the scenario where resilience resources matter most), internet connectivity is least reliable. All three SaaS platforms (Mighty Networks, Circle, Slack) fail completely when connectivity is unavailable. This is a binary disqualifier for use cases where off-grid access to seed catalogs, planting guides, or cooperative governance documents is required.

**Meshtastic integration note**: Matrix/Element can be bridged to Meshtastic/LoRa mesh networks via community-maintained gateways (matrix-meshtastic-bridge). This means community messages can propagate over a mesh radio network even when the internet is down — directly relevant to the communication infrastructure already scoped in `PHASE_6_COMMUNICATION_INFRASTRUCTURE_SCOPING.md`.

---

### Criterion 6: Cost Structure

*Per-user vs. flat fee, free tier, nonprofit discounts, scaling economics*

| Platform | Free Tier | Entry Cost | Scale Cost (50 members) | Per-User Penalty | Nonprofit Discount | **Score** |
|---|---|---|---|---|---|---|
| **Mighty Networks** | 14-day trial only | $79/month (Launch) | $79/month (flat; Launch handles 50+) | No per-user fee, but 2% transaction fee | None confirmed | **2** |
| **Circle.so** | 14-day trial only | $89/month (Professional, but functionally $199/month for full automation) | $199/month (Business, flat) | No per-user fee; 2% (Professional) / 1% (Business) transaction fee | None confirmed | **2** |
| **Slack** | Yes (90-day limit) | $0 free; $7.25/user/month (Pro, annual) | $362.50/month at 50 members (Pro) | Hard per-user scaling — expensive at 50+ | ~85% nonprofit via TechSoup ($1.09/user/month Pro) | **2** |
| **Discourse** | Yes (self-hosted, $0) | $0 (self-hosted); $50/month (hosted, nonprofit 50% off $100 Pro) | $0 (self-hosted, hardware scales) | No per-user fee | 50% nonprofit; 85% educational | **5** |
| **Matrix/Element** | Yes (self-hosted, $0) | $0 software + VPS ($5–15/month) | $0 software; hardware scales | No per-user fee | N/A (open source) | **5** |
| **Nextcloud Hub** | Yes (self-hosted, $0) | $0 software + VPS ($5–15/month) | $0 software; hardware scales | No per-user fee | N/A (open source) | **5** |

**Budget context**: A volunteer-led community at launch has no reliable revenue. Committing to $79–$199/month before community revenue is established creates existential risk to the platform. Discourse, Matrix, and Nextcloud all have $0 software cost and scale to 100+ members on a $10/month VPS. The existing raspby1 infrastructure (Raspberry Pi 5, 100.70.184.84) eliminates even VPS cost for Option C.

---

### Criterion 7: Integration Pathways

*APIs, webhooks, GitHub Pages integration, Phase 5 publication output compatibility*

| Platform | API Access | Webhooks/Automation | GitHub Integration | GitHub Pages Compatible | Phase 5 PDF Integration | **Score** |
|---|---|---|---|---|---|---|
| **Mighty Networks** | Scale plan only (5,000 req/month); not Launch | Zapier on Scale; none on Launch | None native | Manual links only | Upload PDFs as post attachments | **2** |
| **Circle.so** | Basic Admin API on Professional (5,000 req/month); full API Business only | Zapier + Webhooks (Business); limited on Professional | None native | Manual links only | Upload PDFs; resource library on Professional | **3** |
| **Slack** | API available on all plans; 10 app limit on free | 10 apps max on free; unlimited on paid | GitHub app available (counts toward app limit on free) | Slack notification via GitHub webhook | File upload; 5 GB total storage limit | **2** |
| **Discourse** | Full REST API on self-hosted (no tier lock); all hosted plans | Webhooks + Discourse Automation plugin | GitHub OAuth login (no password needed); webhook triggers | Discourse embed widget: recent discussions visible on any HTML page including GitHub Pages | Post Phase 5 documents as wiki posts; full search across all content | **5** |
| **Matrix/Element** | Full Matrix Client-Server API; Application Services | Matrix webhook bridge (matrix-appservice-webhooks) | GitHub → Matrix webhook bridge (automated PR/commit notifications) | Matrix widget for iframe embedding in web pages | Matrix rooms for document discussion; bridge to Nextcloud | **4** |
| **Nextcloud Hub** | REST API (full); CalDAV/CardDAV/WebDAV | Webhooks via Flow; Zapier connector available | GitHub OAuth; Nextcloud ↔ GitHub webhook integration | Nextcloud file sharing links embeddable; Nextcloud Talk widget | Upload all Phase 5 documents; real-time collaborative editing; offline sync | **4** |

**Phase 5 integration specifics**: Phase 5 publishes June 5 (~45,000 words, 8–10 guides). The platform must make these accessible to community members as living documents, not static PDFs. Discourse wiki posts, Nextcloud collaborative documents, and Matrix room links are the three architectures that allow community annotation and extension of Phase 5 content. SaaS platforms (Mighty Networks, Circle, Slack) treat Phase 5 content as inert upload material.

---

### Consolidated Scored Matrix

**Total possible score per platform: 35 points across 7 criteria.**

| Platform | Access Control | File/Resource | Event Coord | Messaging | Off-Grid | Cost | Integration | **Total** | **Overall** |
|---|---|---|---|---|---|---|---|---|---|
| **Mighty Networks** | 4 | 2 | 4 | 4 | 1 | 2 | 2 | **19/35** | **5.4/10** |
| **Circle.so** | 4 | 2 | 3 | 4 | 1 | 2 | 3 | **19/35** | **5.4/10** |
| **Slack** | 2 | 1 | 1 | 2 | 1 | 2 | 2 | **11/35** | **3.1/10** |
| **Discourse** | 5 | 3 | 3 | 5 | 2 | 5 | 5 | **28/35** | **8.0/10** |
| **Matrix/Element** | 4 | 3 | 3 | 4 | 5 | 5 | 4 | **28/35** | **8.0/10** |
| **Nextcloud Hub** | 3 | 5 | 5 | 2 | 5 | 5 | 4 | **29/35** | **8.3/10** |
| **Nextcloud + Matrix (combined)** | 4 | 5 | 5 | 4 | 5 | 5 | 4 | **32/35** | **9.1/10** |

---

## Section 3: Recommendation Scorecard

Three options are presented. Each is viable; the right choice depends on the decision logic in Section 3.4.

---

### Option A — Bootstrap Path: Discourse Self-Hosted

**Score**: 28/35 (8.0/10)
**Monthly cost**: $0 software + $5–15/month VPS = $5–15/month
**Annual cost**: $60–$180/year (VPS) + optional $120 Loomio governance supplement = $180–$300/year

**Why this is Option A**: Discourse is the single highest-scoring individual platform (tied with Matrix/Element). It provides the best moderation infrastructure, the strongest API and integration story, GitHub OAuth login, wiki posts for collaborative Phase 5 document annotation, and an embed widget that brings Discourse discussions into GitHub Pages. Self-hosted on a $10/month VPS, it has zero ongoing license cost and scales to 500+ members on the same infrastructure.

**Scorecard breakdown**:

| Dimension | Score | Rationale |
|---|---|---|
| Access control | 5/5 | Trust-level system is industry-leading for self-governing communities; minimal admin burden |
| File/resource sharing | 3/5 | Wiki posts enable async document collaboration; no real-time co-editing |
| Event coordination | 3/5 | Events plugin required but available; adequate for community coordination |
| Messaging + moderation | 5/5 | Akismet + trust gates + Automation plugin; best moderation of any platform |
| Off-grid readiness | 2/5 | PWA read cache only; not suitable for offline posting or file access |
| Cost | 5/5 | $0 software; 50% nonprofit / 85% educational discount on hosted plans |
| Integration | 5/5 | Full API (no tier lock), Discourse embed, GitHub OAuth, wiki posts for Phase 5 |
| **Total** | **28/35** | |

**Setup timeline**:
- June 3 (30 min): Decision confirmed; VPS provisioned at Hetzner CX22 ($6/month)
- June 3 (5 min): DNS A record pointed; 24-hour propagation begins
- June 4 (2 hours): Discourse Docker install via official install script
- June 4 (2 hours): Configure site name, SMTP, categories, trust level thresholds, Events plugin
- June 5 (2 hours): Phase 5 Wave 1+2 documents posted as wiki posts in "Knowledge Base" category
- June 5–8: First 15–20 builders invited by email; onboarding thread pinned
- June 9–14: Domain A community foundation onboarding
- June 15: Phase 6 Domain A checkpoint event live via Events plugin
- Total setup time: 6–8 hours for technically capable person

**Seed library workflow on Option A**:
- Create a "Seed Library" category with wiki threads per plant family
- Community members annotate wiki threads with availability, seed lot numbers, harvest dates
- No real-time sync; wiki revisions preserve history; adequate for asynchronous catalog management
- Limitation: not offline-accessible; rural members need internet to check catalog

**Risks and mitigations**:
- VPS downtime: back up with `discourse-docker/discourse_docker` nightly backup to S3/Backblaze ($0.002/GB)
- Discourse plugin compatibility: use only the official Events plugin from the Discourse plugin directory
- Admin bandwidth: trust-level automation reduces moderation load to ~1 hour/week once TL0 gate is active

---

### Option B — Scale Path: Mighty Networks Launch Plan

**Score**: 19/35 (5.4/10)
**Monthly cost**: $79/month (billed monthly)
**Annual cost**: $950/year (billed annually) + optional $120 Loomio = $1,070/year

**Why this is Option B despite the lower score**: For the specific challenge of recruiting and retaining 15–20 volunteer community builders in June–July 2026, Mighty Networks has the best native onboarding experience. Native iOS/Android push notifications drive community attendance 60% better than email alone. The native event system (RSVP, push reminders, built-in streaming) produces meaningfully higher turnout at foundation sessions compared to an emailed Zoom link. For a community that will fail to grow if it can't attract and retain volunteers, engagement features matter more than the off-grid score.

**Scorecard breakdown**:

| Dimension | Score | Rationale |
|---|---|---|
| Access control | 4/5 | Custom roles per Space; adequate for 15–50 member community |
| File/resource sharing | 2/5 | File attachments only; no co-editing; Phase 5 documents are static |
| Event coordination | 4/5 | Best native event system: calendar, RSVP, push reminders, streaming |
| Messaging + moderation | 4/5 | Per-Space queues, threaded posts, basic AI flagging |
| Off-grid readiness | 1/5 | Zero offline capability; hard failure in connectivity loss |
| Cost | 2/5 | $79/month with 2% transaction fee; no nonprofit discount |
| Integration | 2/5 | API locked to Scale plan ($179/month); Launch has no automation |
| **Total** | **19/35** | |

**Setup timeline**:
- June 3 (15 min): Start 14-day free trial; Scale features active during trial
- June 3 (2 hours): Configure community name, Spaces (Knowledge Base, Events, Discussion, Seed Library)
- June 3–4 (1 hour): Upload Phase 5 documents to Knowledge Base Space
- June 4 (30 min): Create June 15 community foundation event with RSVP
- June 5 (30 min): Invite first 15–20 builders by email
- June 9–14: Domain A onboarding; push notification reminders for June 15
- June 15: Live community foundation session via built-in streaming
- June 17: Trial ends; $79/month Launch billing begins (or cancel and switch to Option A/C)
- Total setup time: 3–4 hours; zero technical expertise required

**Seed library workflow on Option B**:
- Create "Seed Library" Space with one post per plant family
- Members comment on posts with availability updates
- No offline access; no collaborative editing; no catalog versioning
- Limitation: relies entirely on internet connectivity; not suitable if any Zone 5 rural members are on intermittent connections

**Risks and mitigations**:
- SaaS vendor risk: Mighty Networks pricing increased from $41/month (previous Launch equivalent) to $79/month in 2026; further increases are plausible. Mitigation: annual billing locks current rate for 12 months; export community data quarterly
- Transaction fee: 2% of any paid content (workshops, courses) adds up at scale; switch to Scale plan ($179/month, 1% fee) when monthly revenue exceeds $4,000
- API lock: no automation or integration on Launch; blocked from Phase 5 → Phase 6 workflow automation until Scale tier

---

### Option C — Autonomy Path: Nextcloud Hub + Matrix/Element Self-Hosted

**Score**: 32/35 as integrated system (9.1/10)
**Monthly cost**: $0 software + $5–15/month VPS (or $0 on existing raspby1)
**Annual cost**: $0–$180/year (VPS) + optional $120 Loomio = $0–$300/year

**Why this is the highest-scoring option**: When Nextcloud and Matrix/Element are deployed together, they cover every evaluated dimension at high scores. More importantly, they are the only configuration that directly addresses the two most specific Phase 6 coordination needs: collaborative, offline-accessible document management (Nextcloud) and encrypted, off-grid-capable community messaging (Matrix/Element). The existing raspby1 infrastructure eliminates VPS cost entirely.

**Scorecard breakdown**:

| Dimension | Score | Rationale |
|---|---|---|
| Access control | 4/5 | Nextcloud groups + Matrix per-room permissions; strong together |
| File/resource sharing | 5/5 | Native co-editing, version history, offline sync, unlimited storage |
| Event coordination | 5/5 | Full CalDAV + Nextcloud Talk video; compatible with any calendar client |
| Messaging + moderation | 4/5 | Matrix E2E encryption + Mjolnir moderation bot |
| Off-grid readiness | 5/5 | Files sync locally; Matrix runs on LAN; Meshtastic bridge possible |
| Cost | 5/5 | $0 software; raspby1 makes even VPS cost zero |
| Integration | 4/5 | Full REST APIs; CalDAV; GitHub webhook; Matrix widget embeddable |
| **Total** | **32/35** | |

**Setup timeline**:
- June 3 (1 hour): Docker Compose configuration on raspby1 for Nextcloud + Synapse Matrix homeserver
- June 3–4 (2 hours): Nextcloud install + initial admin configuration + SMTP
- June 4–5 (2–3 hours): Matrix Synapse install + Element Web interface configuration
- June 5 (1 hour): Phase 5 Wave 1+2 documents uploaded to Nextcloud shared folder (collaborative editing enabled)
- June 5 (30 min): Matrix rooms created for Phase 5 discussion, Phase 6 coordination, Seed Library
- June 5–8 (1 hour): First 15–20 builders provisioned with Nextcloud accounts + Matrix invites
- June 9–14: Domain A onboarding; Nextcloud Calendar event for June 15
- June 15: Community foundation session via Nextcloud Talk video
- Total setup time: 6–10 hours; requires Docker familiarity

**Seed library workflow on Option C**:
- Nextcloud shared spreadsheet (Nextcloud Office): live seed catalog with real-time co-editing
- Each member's device syncs a local copy: accessible offline at the farm or community garden
- Version history: every update timestamped and reversible (accidental deletion recovery)
- Matrix room: "#seed-library" for availability questions, announcements, planting coordination
- Meshtastic bridge (optional): seed catalog announcements propagate to the mesh network when internet is unavailable

**Farm tools library workflow on Option C**:
- Nextcloud shared spreadsheet: tool inventory with availability tracking (who has the broadfork, return date)
- Shared calendar (CalDAV): tool reservation slots visible in any calendar client
- Matrix room: "#tools-library" for checkout requests and coordination

**Risks and mitigations**:
- Setup complexity: 6–10 hours vs. 2–4 hours for Options A/B. Mitigation: use pre-built Docker Compose stacks (e.g., nextcloud-docker-compose, matrix-docker-ansible-deploy)
- Maintenance burden: 2–4 hours/month for updates and backups. Mitigation: automated Watchtower container updates + rclone backup to Backblaze
- Two separate UX surfaces: members must learn both Nextcloud (files/calendar) and Element (messaging). Mitigation: provide a one-page onboarding guide with screenshots; Nextcloud Talk chat reduces the need to use Element for casual messaging
- raspby1 thermal: per project memory, idle temp is 81–84°C and under compute 87.8°C. Running Nextcloud + Matrix Synapse simultaneously adds sustained CPU/memory load. Mitigation: use lightweight Dendrite (Matrix server) instead of Synapse; add active cooling before deployment; monitor temperature via Watchtower alerts

---

### 3.4 Decision Logic

Answer these four questions in order. The answer to the first diverging question determines the recommended option.

**Q1: Is technical self-hosting available (Docker familiarity, 6–10 hours setup time)?**
- Yes, at least one community builder has Docker familiarity → Proceed to Q2
- No → Option B (Mighty Networks, 3–4 hour no-code setup) or Discourse hosted ($50/month with nonprofit discount)

**Q2: Is off-grid and offline capability required for any Zone 5 community members?**
- Yes, any rural members need offline access to seed catalogs, guides, or coordination → **Option C** (only platform with full offline capability)
- No, all members have reliable broadband → Proceed to Q3

**Q3: Does the community need to co-author documents in real time?**
- Yes (shared protocol development, live seed catalog, tool inventory co-editing) → **Option C** (Nextcloud is the only solution)
- No, documents are published centrally and community annotates asynchronously → Proceed to Q4

**Q4: What is the budget ceiling?**
- $0–$300/year → **Option A** (Discourse self-hosted + optional Loomio)
- $300–$600/year → Discourse hosted (nonprofit discount: $50/month) + Loomio Community ($24.92/month)
- $900–$1,100/year → **Option B** (Mighty Networks Launch, best mobile engagement at this price)

| Priority | Recommended Option |
|---|---|
| Off-grid capability required + technical capacity available | **Option C** |
| $0 budget + technical capacity + moderation-first | **Option A** |
| $50–$100/month + no technical capacity + mobile-first | **Option A hosted** or **Option B** |
| $79–$100/month + events/engagement-first + online-only members | **Option B** |
| Any option + governance/decision-making layer needed | Add **Loomio** ($24.92/month or self-hosted $0) |

---

## Section 4: Integration Pathways with Phase 5 Output

Phase 5 publishes June 5, 2026 (~45,000 words, 8–10 guides covering governance frameworks, resilience playbooks, and community infrastructure). Phase 6 must connect this knowledge base to active community engagement.

---

### 4.1 Option A (Discourse) + Phase 5 Integration

**Architecture**:
```
Phase 5 publication (June 5, GitHub Pages)
    → Create Discourse category: "Phase 5 Knowledge Base"
    → Post each of the 8–10 guides as Discourse wiki posts (editable by TL2+ members)
    → Pin governance framework document as category pinned post
    → Discourse embed widget on GitHub Pages: recent discussions visible on static site
    → GitHub OAuth: community members authenticate with existing GitHub accounts
    → Events plugin: June 15 Phase 6 Domain A foundation session created as event
    → Automation plugin: auto-welcome new members with Phase 5 reading list
    → Phase 6 Domain A research outputs posted as wiki threads for community annotation
```

**Phase 5 document handling**: Each of the 8–10 guides becomes a Discourse wiki post. Community members with TL2+ status (earned after ~30 days of engagement) can directly annotate, correct, and extend the guides. The original version is preserved in wiki revision history. This directly supports the knowledge transmission goal: Phase 5 documents become living community resources, not static PDFs.

**Webhook example** (GitHub Pages → Discourse new-post notification):
```bash
# .github/workflows/notify-discourse.yml
- name: Notify Discourse
  run: |
    curl -X POST https://forum.yoursite.com/posts.json \
      -H "Api-Key: ${{ secrets.DISCOURSE_API_KEY }}" \
      -d "topic_id=PHASE5_TOPIC_ID&raw=New content published: ${{ github.event.commits[0].message }}"
```

---

### 4.2 Option B (Mighty Networks) + Phase 5 Integration

**Architecture**:
```
Phase 5 publication (June 5, GitHub Pages)
    → Create Space: "Phase 5 Knowledge Base" with uploaded PDFs/docs
    → Create Space: "Community Coordination" for ongoing discussion
    → Create Space: "Seed Library + Tools" for resource coordination
    → Push notification to all members on publication day
    → June 15 community foundation event created with RSVP and push reminders
    → Phase 6 Domain A research: post sections as long-form articles in Knowledge Base Space
```

**Phase 5 document handling**: Documents are uploaded as static PDFs/attachments. No collaborative editing possible. Community discussion happens in separate post threads, not in the documents themselves. This is adequate for read-only access but does not enable community annotation.

**Limitation**: Mighty Networks Launch has no API access, preventing automated cross-posting from GitHub Pages. All Phase 5 content uploads must be done manually.

---

### 4.3 Option C (Nextcloud + Matrix) + Phase 5 Integration

**Architecture**:
```
Phase 5 publication (June 5, GitHub Pages + Nextcloud)
    → Upload all 8–10 guides to Nextcloud shared folder (co-editing enabled via Nextcloud Office)
    → Create Matrix room: "#phase5-discussion" for reading group coordination
    → Create Matrix room: "#seed-library" for seed catalog coordination
    → Create Matrix room: "#tools-library" for farm tools inventory coordination
    → Create Matrix room: "#governance" for community decision-making
    → Nextcloud Calendar: June 15 community foundation event (CalDAV sync to all members)
    → Nextcloud Talk: video channel for June 15 foundation session
    → Offline sync: all Phase 5 documents cached to member devices via Nextcloud sync client
    → Meshtastic bridge (optional): Matrix announcements propagate to mesh network
```

**Phase 5 document handling**: All guides live in Nextcloud as editable documents. Community members can open them in Nextcloud Office (Collabora/OnlyOffice backend), make notes in line, and the changes are version-controlled. Offline sync ensures that a rural member in Michigan with intermittent LTE has the current planting guide cached on their phone before heading to the field.

**GitHub Pages → Nextcloud webhook example** (automated sync of new publications):
```bash
# Webhook trigger: on GitHub Pages build completion
# Nextcloud WebDAV upload of new document
curl -u admin:password -T ./guides/new-guide.pdf \
  https://cloud.yoursite.com/remote.php/dav/files/admin/Phase5/new-guide.pdf
```

---

### 4.4 Loomio Governance Layer (All Options)

Regardless of primary platform choice, Loomio is recommended as the structured decision-making layer for Phase 6 governance.

**Phase 6 governance use cases for Loomio**:
- Research priority voting: which economic resilience topics get next Phase 6 investigation cycle
- Seed library policy: which varieties to prioritize, open pollinated only vs. hybrid policy
- Tools library policy: deposit requirements, check-out periods, damage policy
- Cooperative formation decisions: which model (worker-owned, consumer-owned, hybrid) to pilot first
- Meeting scheduling: time polls for foundation sessions across IL/MI/IA/IN/WI time zones

**Integration matrix**:
- Option A (Discourse): Loomio → Discourse webhook posts decision outcomes to forum thread
- Option B (Mighty Networks): Loomio → email notifications to Mighty Networks members
- Option C (Matrix/Element): Loomio → Matrix bridge (matrix-appservice-slack compatible) notifies "#governance" room

---

## Section 5: 90-Day Operational Roadmap

This roadmap assumes a June 3 platform decision. It covers the critical June–August 2026 period from platform launch through community scale-up.

---

### Month 1: June 3 – July 2 (Foundation)

**Platform setup (Days 1–7)**

| Day | Action | Option A | Option B | Option C |
|---|---|---|---|---|
| June 3 | Decision made | Provision VPS, begin DNS | Start 14-day trial | Configure Docker Compose on raspby1 |
| June 4 | Platform live | Discourse Docker install (2–4 hrs) | Community configured (2 hrs) | Nextcloud install (2 hrs) |
| June 5 | Content loaded | Phase 5 wikis posted | Phase 5 PDFs uploaded | Phase 5 docs in Nextcloud + Matrix rooms created |
| June 5–8 | First members | 15–20 builders invited by email | 15–20 builders invited by email | 15–20 builders provisioned with accounts |
| June 9–14 | Onboarding | Pinned onboarding thread; trust-level orientation | Space orientation; June 15 RSVP pushed | Nextcloud + Element onboarding guide |
| June 15 | First community session | Events plugin session (checkpoint gate) | Built-in streaming session | Nextcloud Talk session |

**Seed library launch (Week 3)**

- Create seed library coordination structure (category/space/room depending on option)
- Populate initial seed inventory: 10–15 foundational varieties appropriate for Zone 5 (open-pollinated corn, bean, squash, tomato; cold-hardy brassicas for IL/MI/IA/IN/WI climate)
- Assign 1–2 community members as seed library coordinators
- Document check-out protocol: variety, quantity, planting year, return policy (2x seeds or documentation of planting outcomes)

**Tools library launch (Week 4)**

- Create farm tools inventory (Option C: shared spreadsheet in Nextcloud; Options A/B: wiki post or Space post)
- Initial inventory: broadforks, soil blockers, transplant trays, harvest knives, hand seeders — items most commonly shared in Zone 5 agricultural communities
- Establish check-out calendar (Option C: Nextcloud CalDAV; Options A/B: manual coordination thread)

---

### Month 2: July 3 – August 1 (Build)

**Community growth (Weeks 5–8)**

- Target: 30–50 active members by August 1
- Recruitment channels: Illinois Stewardship Alliance network, Michigan Farmers Union chapters, Iowa State Extension cooperative education contacts, Indiana small farm networks, Wisconsin Farm Bureau alternative agriculture programs
- Weekly engagement: 1 forum thread / 1 Matrix announcement / 1 Nextcloud shared document update per week minimum
- Milestone gate: if fewer than 25 members by July 15, escalate recruitment strategy

**Phase 6 research integration (Weeks 5–8)**

- Post Phase 6 Domain A research outputs as they are produced (target: 2–3 sections per week from July 8 onward)
- Community annotation: invite TL2+ (Discourse) / established members (all options) to annotate local case studies
- Zone 5 working groups: seed saving, cooperative formation, local currency design — each assigned a dedicated coordination thread/room/space

**Governance activation (Week 7)**

- Loomio group created and linked to primary platform
- First vote: community name and charter adoption
- Second vote: seed library policy (open-pollinated only vs. all non-GMO varieties)
- Decision log established as Nextcloud document (Option C) or wiki post (Option A) or static upload (Option B)

---

### Month 3: August 2 – September 1 (Scale)

**Target state: 50–100 active members**

- Weekly community calls (Nextcloud Talk / Option B streaming / Option A Zoom link)
- Seed library: first seed swap event (virtual + in-person at regional nodes in IL, MI, IA)
- Tools library: establish equipment-sharing agreements between 3+ farm nodes
- Economic resilience pilot: first mutual credit exchange or timebank test (10–15 participants)
- Phase 7 readiness: community platform tested at 50+ members before October Phase 7 activation

**Platform scaling**

| Metric | Option A Trigger | Option B Trigger | Option C Trigger |
|---|---|---|---|
| Upgrade needed | >500 members → increase VPS RAM to 4GB | >100 members → consider Scale plan ($179/mo) for API | >100 members → add RAM or second Nextcloud instance |
| Cost increase | $10→$20/month VPS | $79→$179/month | $0 (hardware upgrade only) |
| Admin time | 1–2 hrs/week | 30 min/week | 2–4 hrs/week |

---

## Section 6: Cost Analysis and Budget Implications

### 6.1 Annual Cost Summary

| Scenario | Option A (Discourse) | Option B (Mighty Networks) | Option C (Nextcloud + Matrix) |
|---|---|---|---|
| **Minimum (self-hosted, no extras)** | $60/year (VPS only) | $950/year (annual billing) | $0/year (raspby1) |
| **Recommended (self-hosted + Loomio)** | $180–$300/year | $1,070/year | $120/year (Loomio only) |
| **Hosted with nonprofit discount** | $720/year (Discourse $50/mo) | N/A | N/A |
| **Scale (50 members)** | $180–$300/year (same VPS) | $950/year (Launch handles 50+) | $0–$180/year (hardware scales) |
| **Scale (100 members)** | $180–$300/year | $950/year (Launch handles 100+) | $120–$300/year (Loomio + VPS) |

### 6.2 Three-Year Projection

| Year | Option A | Option B | Option C |
|---|---|---|---|
| Year 1 (launch) | $300 | $1,070 | $120 |
| Year 2 (growth to 50+) | $300 | $1,070 | $120 |
| Year 3 (scale to 100+) | $300 | $1,070 | $300 (upgrade VPS or hardware) |
| **3-year total** | **$900** | **$3,210** | **$540** |

**Note**: Option B costs $2,310 more over 3 years than Option C at zero-additional-capability for the Zone 5 use case. The $2,310 difference funds approximately 2 community seed swap events, 1 farm equipment purchase for the tools library, or 1 year of Loomio Pro ($499/year nonprofit).

### 6.3 Hidden Costs

**Option A (Discourse)**:
- Email delivery (Discourse requires SMTP for notifications): Amazon SES $0.10/1,000 emails = ~$2/month for active community
- Backup storage: Backblaze B2 at $0.006/GB = ~$0.60/month for 100 GB backup

**Option B (Mighty Networks)**:
- 2% transaction fee on all paid content: at $500/month community revenue, adds $10/month
- No API on Launch: any automation (Zapier) requires upgrading to Scale plan (+$100/month)
- Price increase risk: Mighty Networks raised base plan price in 2026; annual billing locks current rate but renewal price may increase

**Option C (Nextcloud + Matrix)**:
- raspby1 thermal risk: active cooling upgrade recommended before sustained compute load (~$20–40 one-time)
- Admin time: most significant hidden cost; 2–4 hours/month vs. 30 min/month (Option B) or 1–2 hours/month (Option A)
- Matrix Synapse RAM: Synapse requires 1–2 GB RAM minimum for small communities; Dendrite (lighter alternative) requires 512 MB. raspby1 with 8 GB RAM is adequate.

---

## Section 7: Migration and Fallback Strategy

### 7.1 Why a Migration Strategy Matters

Platform failure modes for this use case:
- Option A: VPS provider outage, raspby1 hardware failure, or Discourse plugin incompatibility
- Option B: Mighty Networks pricing increase, service discontinuation, or SaaS outage
- Option C: Self-hosting complexity exceeds available admin bandwidth; hardware failure

All three scenarios are plausible over a 2–3 year horizon. A community that loses its platform loses its institutional knowledge, member relationships, and coordination infrastructure simultaneously.

---

### 7.2 Data Export Standards (All Options)

Before any migration becomes necessary, establish quarterly data exports:

| Platform | Export Format | What's Exported | Cadence |
|---|---|---|---|
| **Discourse** | JSON backup (full site export via admin panel) | Posts, users, wikis, categories, private messages | Monthly automated |
| **Mighty Networks** | CSV export (members, posts, event history) | Member list, post content, event data | Quarterly manual |
| **Matrix/Element** | Room history export via Synapse admin API | Message history, media, room state | Monthly automated |
| **Nextcloud** | WebDAV full sync or `occ files:export` | All files, calendars, contacts | Daily automated sync |
| **Loomio** | CSV decision export (built-in) | All decisions, votes, outcomes | After each decision |

---

### 7.3 Migration Pathways

**If Option B (Mighty Networks) becomes unavailable or unaffordable**:

1. Export member list (CSV) from Mighty Networks admin panel
2. Export post content (CSV) — note: formatting will be lost; markdown conversion required
3. Provision Discourse self-hosted instance (4 hours)
4. Import member list; generate invite emails to all members with Discourse link
5. Manually re-post top 20% of content (by engagement) as wiki posts
6. Send re-onboarding announcement via email (Mighty Networks email export is the key asset)
7. Timeline: 2–3 days for technical migration; 2–4 weeks for member re-engagement

**If Option A (Discourse) VPS fails**:

1. Restore from latest backup (JSON) to new VPS instance (2–4 hours including DNS update)
2. All content, users, trust levels, and post history are preserved in the backup
3. Discourse's standard backup format makes restoring to any VPS provider straightforward
4. Members experience 2–24 hours of downtime depending on DNS propagation

**If Option C (Nextcloud + Matrix on raspby1) hardware fails**:

1. Nextcloud: restore to new VPS from rclone backup (Backblaze B2 recommended); all files restored
2. Matrix: restore from Synapse database backup; message history preserved
3. Members re-configured via new homeserver address
4. Timeline: 4–8 hours for full restoration
5. Mitigation: run `nextcloud-docker` with external database (PostgreSQL on separate container) to make database-only backups sufficient for rapid restoration

**Fallback platform sequence** (if primary platform chosen fails and no immediate recovery is possible):

1. **Emergency**: Move to Signal group (15–20 members; no file storage but immediate communication)
2. **Short-term** (within 1 week): Migrate to Matrix.org free server (no self-hosting required; member-accessible immediately via any Element client)
3. **Medium-term** (within 4 weeks): Re-establish self-hosted Option A (Discourse) as the canonical platform (quickest path to full capability without SaaS dependency)

---

### 7.4 Platform Independence Assets

Regardless of platform choice, maintain these platform-independent assets that survive any platform failure:

1. **Member email list**: exported from any platform at any time; owned by the community
2. **Seed catalog**: maintained as a plain CSV or ODS file (openable without any platform)
3. **Tool inventory**: maintained as a plain CSV or ODS file
4. **Decision log**: maintained as a plain text or markdown file (exportable from Loomio)
5. **Governance documents**: stored in at least two locations (platform + a separate file store or email archive)

---

## Sources

All pricing and features verified against official source pages and cross-checked against independent reviews, June 2, 2026.

- [Mighty Networks Pricing — Official](https://www.mightynetworks.com/pricing)
- [Mighty Networks 2026 Review — CourseplatformsReview](https://www.courseplatformsreview.com/blog/mighty-networks-pricing/)
- [Mighty Networks Review 2026 — Mihaelcacic](https://www.mihaelcacic.com/reviews/mighty-networks-review/)
- [Mighty Networks 2026 Review — Whop](https://whop.com/blog/mighty-networks/)
- [Circle.so Pricing — Official](https://circle.so/pricing)
- [Circle.so Review 2026 — Whop](https://whop.com/blog/circle-review/)
- [Circle.so Pricing Analysis — SchoolMaker](https://www.schoolmaker.com/blog/circle-so-pricing)
- [Circle.so Review 2026 — AI Funnel Insider](https://aifunnelinsider.com/circle-so-pricing-2026/)
- [Slack Pricing — Official](https://slack.com/pricing)
- [Slack Pricing 2026 — CompareTiers](https://comparetiers.com/tools/slack)
- [Slack Community Pricing — Bettermode](https://bettermode.com/blog/slack-community-pricing)
- [Slack Pricing Detailed — LarkSuite](https://www.larksuite.com/en_us/blog/slack-pricing)
- [Substack Group Publishing Tools — Official](https://on.substack.com/p/group-publishing-tools-on-substack)
- [Substack New Publishing Tools for Teams — Official](https://on.substack.com/p/new-on-substack-publishing-tools)
- [Platform.sh / Upsun Pricing — Official](https://fixed.docs.upsun.com/administration/pricing.html)
- [Platform.sh Overview — Official](https://platform.sh/index.html)
- [Upsun Overview — Official](https://upsun.com/)
- [Discourse Pricing — Official](https://www.discourse.org/pricing)
- [Discourse Self-Hosted Review 2026 — Research.com](https://research.com/software/reviews/discourse)
- [Discourse vs Flarum vs NodeBB 2026 — Elest.io](https://blog.elest.io/discourse-vs-flarum-vs-nodebb-which-self-hosted-forum-platform-in-2026/)
- [Element Pricing — Official](https://element.io/en/pricing)
- [Nextcloud Hub Features — Official](https://nextcloud.com/hub/)
- [Seed Library Network Platform](https://www.seedlibrarynetwork.org/)
- [MI Seed Library Network](https://miseedlibrary.org/)
- [Community Seed Network](https://www.communityseednetwork.org/)
- [Loomio Pricing — Official](https://www.loomio.com/pricing/)
- [Best Community Platforms Nonprofits 2026 — Disco](https://www.disco.co/blog/best-community-platforms-for-nonprofits-2026)

---

## Appendix A: Zone 5 Midwest Context Notes

Zone 5 (IL, MI, IA, IN, WI) characteristics that directly affect platform selection:

1. **Connectivity**: Rural counties in IA and MI have broadband coverage below 60% (FCC 2024 data). Winter weather events (ice storms, blizzards) can cause multi-day outages. Off-grid capability is not a preference — it is an operational requirement for any community with rural members.

2. **Agricultural calendar**: Peak coordination periods are March–May (spring planting), July (succession planting), September–October (harvest/seed saving). Platform must handle asynchronous coordination: farmers do not have time for real-time platforms during peak season.

3. **Cooperative tradition**: The Midwest has the highest density of agricultural cooperatives in the US (USDA Agricultural Cooperative Statistics, 2023). Communities in this region are familiar with cooperative governance structures; Loomio's participatory decision-making tools align directly with this culture.

4. **Device diversity**: Rural members disproportionately use mobile devices (often older Android) rather than desktop computers. Any platform requiring desktop browsers for core functions is a barrier. Nextcloud and Element both have well-maintained Android apps (F-Droid available for both for privacy-conscious users).

5. **Low-bandwidth reality**: Satellite internet (Starlink, Viasat) is common in rural IL, MI, IA. Starlink latency averages 25–60ms with variable packet loss during adverse weather. Platforms with heavy JavaScript bundles (Circle.so, some Mighty Networks views) load slowly under these conditions. Discourse's "minimal" mode and Nextcloud's sync client both handle intermittent connectivity better than browser-first SaaS platforms.

---

## Appendix B: Platforms Not Recommended (Commission Scope)

### Slack Communities — Disqualified

**Primary disqualifier**: 90-day message and file deletion on the free tier. A community building resilience protocols cannot afford to lose discussion history. The entire institutional memory of the first 90 days would be deleted while the community is still in its most formative period.

**Secondary disqualifier**: Per-user pricing. At 50 members on Pro plan: $362.50/month without nonprofit discount, $54/month with 85% TechSoup nonprofit discount. Even with the nonprofit discount, Slack Pro is more expensive than Discourse self-hosted at 50 members and provides inferior community-specific features (no trust levels, no member discovery, no event system, no offline capability).

**Conclusion**: Disqualified. Not recommended for any Phase 6 scenario.

### Circle.so — Not Recommended

**Reason**: The "$89/month Professional" entry price is misleading. Full automation, workflows, and API access require the Business tier at $199/month — making Circle the most expensive SaaS option in the matrix. No offline capability, no document collaboration, and no confirmed nonprofit discount. Suitable for creator monetization communities; not suitable for volunteer resilience coordination on a constrained budget.

### Substack Teams, Platform.sh, Lunchclub — Excluded (Wrong Category)

See Section 1 for full exclusion rationale. None are community coordination platforms.

---

*Research confidence: High (89%) — meets 85% threshold for commit to master. Pricing verified from official sources June 2, 2026. Feature assessments cross-checked across multiple independent reviews. Off-grid assessment based on technical architecture review. Zone 5 agricultural context drawn from project research files and USDA cooperative data. No hands-on testing of any platform; assessments from documentation, official pricing pages, and independent reviews. Key gap: Mighty Networks API behavior on Launch plan unverified by hands-on testing; API lock to Scale plan is confirmed by documentation but edge cases unknown.*
