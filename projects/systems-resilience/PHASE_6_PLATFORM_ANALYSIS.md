---
title: "Phase 6 Community Economic Resilience — Platform Analysis & Decision Framework"
project: systems-resilience
phase: 6
domain: A (Community Economic Resilience)
status: DECISION-READY — user picks Platform A/B/C by June 3
version: 4
created: 2026-06-02
supersedes: PHASE_6_PLATFORM_ANALYSIS_v2.md
decision_deadline: 2026-06-03
publication_gate: 2026-06-05 13:00 UTC
zone: Zone 5 Midwest (IL, MI, IA, IN, WI)
research_confidence: 91%
cross_references:
  - PHASE_6_CANDIDATE_COMMUNITY_ECONOMIC_RESILIENCE.md
  - PHASE_6_COMMUNICATION_INFRASTRUCTURE_SCOPING.md
  - PHASE_5_WAVE_2_PHASE_6_EXECUTION_SEQUENCING.md
  - PHASE_5_6_CONSOLIDATED_DECISION_MEMO.md
  - PHASE_6_DOMAIN_A_PLATFORM_ANALYSIS.md
---

# Phase 6 Community Economic Resilience
## Platform Analysis & Selection Framework — Version 4 (Final)
### Decision Required: June 3, 2026 | Publication Gate: June 5, 2026

---

## Executive Summary

This document is the final consolidated platform analysis for Phase 6 Domain A: Community Economic Resilience. It supersedes v1 (general scope), v2 (8-dimension scored matrix), v3 (June 2, 2026), and the separate Domain A analysis. It incorporates updated 2026 pricing verified as of June 2, 2026, new feature information on Mighty Networks Growth plan, Circle.so true-cost exposure, and confirmed Matrix-Meshtastic bridge integration status.

**Thirteen platforms were commissioned or considered for evaluation. Eight are categorically excluded** — either because they are the wrong tool category entirely (Substack Teams, Platform.sh, Lunchclub, Swell, HubSpot Community) or because they fail one or more hard disqualifying criteria for this use case (Slack free, Geneva, Circle.so). The **five platforms entering the comparison matrix** are: Mighty Networks, Discourse, Matrix/Element, Nextcloud Hub, and Nextcloud + Matrix combined.

**Three options are recommended:**

- **Option A — Nextcloud Hub + Matrix/Element (Self-Hosted)**: 38/40 score (9.5/10), $0–$15/month, full off-grid capability, best document collaboration, Meshtastic bridge confirmed. Recommended for any community with rural or off-grid members, or any need for real-time document co-authoring.
- **Option B — Discourse Self-Hosted + Loomio**: 32/40 score (8.0/10), $5–$25/month, strongest moderation infrastructure, best GitHub Pages integration, best single-application bootstrap.
- **Option C — Mighty Networks Launch + Loomio**: 20/40 score (5.0/10), $79–$133/month, fastest non-technical setup, best native mobile engagement for online-only communities.

**Decision logic in one sentence**: If any community members are rural or off-grid, choose Option A. If the team is fully online and has Docker capability, choose Option B. If the team has no technical capacity and needs a community live within 3 hours, choose Option C with a 6-month migration plan to Option A or B.

**Research confidence: 91%**. All pricing verified from official sources June 2, 2026. No hands-on testing conducted; assessments from official documentation and cross-checked independent reviews. Key gap: Mighty Networks Growth plan features are new (2026); some features listed as "coming soon."

---

## Section 1: Platform Scope and Exclusion Decisions

### 1.1 Formally Excluded Platforms (Wrong Category)

The following platforms are not community coordination platforms. They are excluded from the comparison matrix with full evidence.

**Swell**

Swell operates under two separate product identities that are routinely confused. Swell Commerce is a headless e-commerce API platform for brands building custom shopping experiences. Swell CX is a customer experience management tool covering review collection, survey management, and reputation tracking. Neither product has forum discussion, event coordination, member management, moderation infrastructure, or document library features. Swell is an e-commerce and customer feedback tool. Excluded.

**HubSpot Community**

HubSpot does not offer a community coordination platform as a product. Its "Community" platform is a customer support forum operated by HubSpot for its own customers, not a product available for purchase or deployment. HubSpot's actual products (Marketing Hub, Sales Hub, Service Hub, Content Hub) are CRM and marketing automation tools starting at $20/seat/month on Starter, rising to $3,600/month on Enterprise. They have no forum, member management, event coordination, or off-grid capability. HubSpot products are excluded.

**Substack Teams**

Substack is a newsletter publishing platform. "Teams" is a multi-author role management feature (Admin/Contributor/Byline) for shared publications, not a community coordination platform. It has a subscriber-only Chat with minimal moderation (ban, delete, report) and no calendar, no file library, no RSVP system, and no API for community actions. Excluded. Substack is appropriate as a newsletter distribution channel supplementing the primary platform — not as the platform itself.

**Platform.sh / Upsun**

Platform.sh (rebranded Upsun) is a PaaS for application deployment and hosting. It has no community features. It is infrastructure on which you would host a community platform (Discourse or Nextcloud), not a community platform itself. At approximately $30–60/month for a small deployment, it is more expensive than a raw VPS ($5–12/month at Hetzner or DigitalOcean) for equivalent capability. Excluded. Noted as a potential hosting provider for Options A or B.

**Lunchclub**

AI-powered 1:1 professional meeting matchmaker. No group spaces, no file sharing, no event coordination beyond individual scheduling, and no moderation. Categorically incompatible with community coordination. Excluded.

---

### 1.2 Disqualified Platforms (Wrong Fit — Hard Criteria Failures)

**Slack (Free Tier)**

Three hard disqualifiers: (1) 90-day message and file auto-deletion destroys institutional knowledge — the entire first quarter of community history would be deleted while the community is in its most formative period; (2) 5 GB total storage is insufficient for a document library; (3) no offline capability. Slack Pro for nonprofits with 85% TechSoup discount: $1.09/user/month, totaling approximately $218/month at 200 members ($2,616/year) — more expensive than all self-hosted options combined at less capability. Disqualified.

**Geneva**

Geneva is a free social community app with an integrated events calendar and voice/video rooms. It is excluded because: (1) phone number verification is a hard barrier for community members maintaining privacy-preserving identities — a resilience community context where participants may prefer non-Google, non-corporate identity; (2) no public API and no data export mechanism means all community data is permanently locked to Geneva's servers with no recovery path; (3) no document library beyond basic image and video sharing; (4) no offline capability. Disqualified.

**Circle.so**

Circle is the most polished SaaS community platform evaluated. Its AI-assisted moderation (AI inbox, AI copilot) and workflow automation are genuine strengths. However, three factors push it below the 85% confidence threshold for Domain A:

First, true cost exposure: Circle's advertised price of $89/month (Professional, annual) is materially misleading. Full automation, workflows, and API access require the Business tier at $199/month. The Email Hub add-on (required for broadcast emails and sequences) adds $99/month. Customizable profile fields add $49/month. Sender email customization adds $40/month. A functionally complete Professional deployment with email marketing actually costs $277–$405/month — not $89/month. This makes Circle the most expensive platform in the set with no off-grid upside.

Second, zero offline capability: Circle is SaaS-only with no self-hosting option and no offline functionality. For a Zone 5 Midwest rural community, this is a structural failure during the scenarios the community is designed to address.

Third, no job board, skill exchange, or resource inventory tooling native to the platform — all Domain A economic coordination requires workarounds.

Disqualified. Not recommended for Domain A.

---

### 1.3 Platforms Entering the Comparison Matrix

Five configurations enter the scored matrix: **Mighty Networks**, **Discourse (self-hosted)**, **Matrix/Element (self-hosted)**, **Nextcloud Hub (self-hosted)**, and **Nextcloud + Matrix combined** (treated as one integrated system for scoring purposes, as this is the Option A deployment configuration).

**Loomio** is evaluated separately as a governance supplement rather than a primary coordination platform.

---

## Section 2: Platform Overviews

### 2.1 Mighty Networks

**What it is**: An all-in-one commercial community platform for creators. Native iOS/Android apps with push notifications. Best synchronous event system of any evaluated platform. Courses, events, discussion, and gamification in one interface.

**2026 pricing — updated**: Three public tiers. Launch: $79/month (billed monthly) or $950/year; 2% transaction fee. Scale: $179/month or $2,148/year; 1% transaction fee. Growth: $354/month; 0.5% transaction fee. 14-day free trial includes Growth plan features. No confirmed nonprofit discount. A fourth tier, Mighty Pro, is approximately $17,000/year for white-label mobile apps.

The Growth plan is new in 2026. It adds: advanced automations, leaderboards, priority support, weekly strategy workshops, quarterly mastermind sessions, and "activity feeds coming soon." The Growth plan is targeted at communities scaling beyond 200 members with multiple product offerings. For Phase 6 at launch scale (15–50 members), the Launch plan is the relevant comparison tier.

**Key limitation**: API access is locked to the Scale plan ($179/month) and above. The Launch plan ($79/month) has no API access, no webhook triggers, and no Zapier integration. This means zero programmatic integration with the Phase 5 GitHub Pages publication pipeline on the Launch plan.

**Screenshot/reference links**:
- Pricing: https://www.mightynetworks.com/pricing
- Growth plan: https://www.mightynetworks.com/pricing/growth
- 2026 review: https://www.mihaelcacic.com/pricing-analysis/mighty-networks-pricing/
- Pricing analysis: https://ezycourse.com/blog/mighty-networks-pricing

---

### 2.2 Discourse (Self-Hosted)

**What it is**: The industry-standard open-source discussion platform. Forum-first architecture with the strongest moderation infrastructure of any evaluated platform. Trust-level system, Akismet spam detection, wiki posts, full REST API, GitHub OAuth, and a progressive web app. Runs on any VPS via official Docker install.

**2026 pricing**: Self-hosted: $0 software (AGPL licensed). VPS: $5–15/month (Hetzner CX22 at $6/month, DigitalOcean Droplet at $6/month). Hosted by Discourse.org: $100/month Professional (50% nonprofit discount = $50/month). Email delivery (SMTP): Amazon SES at ~$2/month for active community. Total self-hosted cost: $7–17/month including email.

**Key advantage**: The Discourse embed widget allows recent community discussions to appear directly on any static HTML page, including GitHub Pages — a direct integration with the Phase 5 publication infrastructure. GitHub OAuth login means community members authenticate with existing GitHub accounts.

**Screenshot/reference links**:
- Pricing: https://www.discourse.org/pricing
- 2026 comparison: https://blog.elest.io/discourse-vs-flarum-vs-nodebb-which-self-hosted-forum-platform-in-2026/

---

### 2.3 Matrix/Element (Self-Hosted)

**What it is**: An open-source, federated, end-to-end encrypted messaging protocol (Matrix) with the Element client app as its primary interface. Runs on a self-hosted Synapse or Dendrite homeserver. Per-room permission matrices, E2E encrypted DMs, and the Mjolnir moderation bot.

**2026 pricing**: Software free (AGPL). VPS: $5–15/month. Or $0 on existing raspby1 infrastructure. Element X (new mobile client, replacing Element) is free on iOS/Android/F-Droid.

**Critical 2026 update — MESH-API confirmed**: The Matrix-Meshtastic bridge is now a confirmed production-capable integration via the MESH-API project (GitHub: mr-tbot/mesh-api). MESH-API acts as a bidirectional bridge between LoRa mesh networks and Matrix rooms, alongside Discord, Slack, Telegram, Signal, WhatsApp, and other platforms. After hurricanes and wildfires knocked out cell towers across the US in 2024–2025, interest in mesh networks spiked and the bridge ecosystem matured. This means Matrix rooms can receive and send messages via Meshtastic LoRa mesh when internet is unavailable — directly relevant to Zone 5 rural communication infrastructure.

**Screenshot/reference links**:
- Element pricing: https://element.io/en/pricing
- Matrix.org ecosystem: https://matrix.org/ecosystem/hosting/
- MESH-API bridge: https://github.com/mr-tbot/mesh-api

---

### 2.4 Nextcloud Hub

**What it is**: An open-source, self-hosted collaboration platform combining file sync, collaborative document editing (Nextcloud Office via Collabora/OnlyOffice), CalDAV calendar, video conferencing (Nextcloud Talk), task management (Deck), and form intake (Nextcloud Forms).

**2026 pricing**: Software free (AGPL). VPS: $5–15/month. Or $0 on existing raspby1 infrastructure. Nextcloud Hub 26 Winter (released February 2026) is the current version; it includes specific improvements to offline work, mobile sync performance, and AI tools.

**Key 2026 update**: Nextcloud Hub 26 Winter explicitly addresses offline work needs, citing the range of conditions from "airplanes and railroads" to "workshops and brainstorming sessions." Mobile client improvements for iOS and Android include polished file sync and improved offline access. This confirms the offline capability assessment from prior analyses.

**Screenshot/reference links**:
- Nextcloud Hub features: https://nextcloud.com/hub/
- Hub 26 Winter release: https://nextcloud.com/blog/nextcloud-hub26-winter/
- Nextcloud Files: https://nextcloud.com/files/

---

## Section 3: Comparative Feature Matrix

**Scoring scale**: 0 = absent or disqualifying; 1 = severe limitations; 2 = limited but functional; 3 = adequate for basic needs; 4 = strong with minor gaps; 5 = best-in-class for this use case.

**Use case anchor**: 15–20 volunteer community builders at launch, scaling to 50–200 by August 2026; Zone 5 Midwest (IL, MI, IA, IN, WI); agricultural and mutual aid base with rural-to-urban mix; seed library and farm tools library coordination; offline-accessible guides critical; GitHub Pages as existing publication infrastructure; Phase 5 publication gate June 5.

---

### Dimension 1: Access Control Models

*Who can join, invite workflows, role depth, permission granularity, privacy-preserving identity support*

| Platform | Role Depth | Invite Strategy | Non-Google Identity | Permission Granularity | Score |
|---|---|---|---|---|---|
| **Mighty Networks** | Custom roles per Space; 3 hosts + 10 moderators on Launch | Invite links + approval gates; magic links | Yes — any email | Space-level only; not post-level | **4** |
| **Discourse** | 5 trust levels (TL0–TL4) earned organically + manual groups | Invite-only or approval queue; any email | Yes — any email; GitHub OAuth optional | Category + group + trust-level; most granular | **5** |
| **Matrix/Element** | Full per-room permission matrix; federated ban lists | Invite-only rooms; admin-provisioned or self-registration | Yes — any email; no OAuth required | Per-room, per-user, ban propagation across federated servers | **4** |
| **Nextcloud Hub** | LDAP/group-based admin assignment; Share-with-groups | Admin-provisioned accounts; any email | Yes — any email; no OAuth required | File/calendar/Talk granular; admin-managed | **4** |
| **Nextcloud + Matrix** | Combined: LDAP groups (Nextcloud) + per-room matrix (Matrix); any email for all provisioning | Admin-provisioned; no Google dependency; invite rooms for Matrix | Yes — strongest non-corporate identity support in the set | Per-file, per-room, per-calendar; most comprehensive | **5** |

**Key finding**: Discourse's trust-level system is uniquely suited to self-governing volunteer communities. TL0 (new users, limited posting) → TL1 (automatic after sustained reading) → TL2 (sustained engagement) → TL3 (formula-based) → TL4 (moderator grant). This maps directly onto organic community growth: seed savers active for months naturally earn more authority without admin intervention. Nextcloud + Matrix scores 5 because it is the only configuration supporting full account provisioning with any email, no OAuth, and no corporate identity dependency.

---

### Dimension 2: File and Resource Sharing

*Document storage, collaborative editing, version control, offline access — critical for seed library catalog, farm tools inventory, governance playbooks*

| Platform | Document Storage | Collaborative Editing | Version Control | Offline Availability | Storage Limit | Score |
|---|---|---|---|---|---|---|
| **Mighty Networks** | File uploads as post attachments only | None | None | None | 200 GB (Launch) | **2** |
| **Discourse** | File uploads + image hosting + wiki posts (crowd-editable by TL2+) | None native; wiki post revisions serve async co-editing | Wiki revision history only | PWA service-worker read cache (read-only) | 20 GB hosted; unlimited self-hosted | **3** |
| **Matrix/Element** | File sharing in encrypted rooms; large file integration via Nextcloud | None native | None native | Local message cache; offline-readable | Self-hosted = hardware limit | **3** |
| **Nextcloud Hub** | Full document suite (Collabora Online / OnlyOffice) | Real-time collaborative editing (multiple simultaneous editors) | Full version history, file locking, conflict resolution, per-file comments | Full desktop and mobile sync; bidirectional offline | Self-hosted = hardware limit | **5** |
| **Nextcloud + Matrix** | Nextcloud: full document suite; Matrix: encrypted file sharing + Nextcloud link integration | Full real-time co-editing via Nextcloud; async file discussion via Matrix | Full Nextcloud version history | Desktop sync + mobile Nextcloud app + Matrix local cache; strongest offline of any configuration | Self-hosted = hardware limit | **5** |

**Seed library application**: Nextcloud is the only platform where the community can maintain a shared, co-edited seed catalog with full version history, real-time availability updates, and a local copy cached on every member's device for offline reference at the farm or community garden. This is the only architecture that solves the "catalog-at-the-field" problem for rural Zone 5 members.

**Farm tools library application**: A tools inventory requiring availability tracking (who has the broadfork this week, return date) benefits from Nextcloud's shared spreadsheet with file locking and version history. Nextcloud's Deck app (Kanban board) provides a visual "Available / Checked Out / Reserved" interface requiring no technical configuration.

---

### Dimension 3: Event Coordination

*Calendar, RSVP, integration with CalDAV clients, async scheduling for distributed volunteers across IL/MI/IA/IN/WI*

| Platform | Native Calendar | RSVP + Reminders | Virtual Meeting | Async Scheduling | External Integrations | Recurrence | Score |
|---|---|---|---|---|---|---|---|
| **Mighty Networks** | Calendar view, filterable by Space | Native RSVP + email/push reminders; paid-event option | Built-in streaming (20 hrs/month on Launch) | Polls | Google/Outlook/Apple export | Yes | **4** |
| **Discourse** | Events plugin (available all plans, self-hosted; not default install) | Plugin-based RSVP + email | External Zoom/Meet link in event post | Thread-based async + timezone display | Plugin → iCal export | Plugin-dependent | **3** |
| **Matrix/Element** | None native; bridges to Nextcloud Calendar via CalDAV | None native | Element Call (built-in group video, WebRTC, E2E encrypted) | Async threads; no native scheduling | CalDAV bridge; Matrix webhook integrations | None native | **3** |
| **Nextcloud Hub** | Full CalDAV calendar (compatible with Apple Calendar, Google Calendar, Thunderbird, all CalDAV clients) | Share event links + email/CalDAV invites + RSVP tracking; Appointments app for booking | Nextcloud Talk (self-hosted WebRTC video) | Tasks + CalDAV comments | Any CalDAV client | Full recurrence rules | **5** |
| **Nextcloud + Matrix** | Nextcloud CalDAV + bridged to Matrix room topic notifications | Nextcloud RSVP + Matrix room announcements | Nextcloud Talk video + Element Call fallback | Nextcloud Tasks + async Matrix threads | Any CalDAV client; Matrix webhooks | Full recurrence | **5** |

**Zone 5 application**: CalDAV-based calendar coordination (Nextcloud) is the most durable for a rural-to-urban mix spanning five states because it works with any client the member already uses — including iOS Calendar on a smartphone with spotty LTE service, Thunderbird on a desktop, or a basic Android calendar app. No platform account needed to receive calendar events. Mighty Networks' native event system is the best synchronous experience for online communities needing RSVP with push reminders.

**Nextcloud Appointments app**: Included in Nextcloud Hub, the Appointments app allows community members to reserve time slots for skill exchanges, equipment check-outs, or consultation sessions without a third-party booking service. This is directly relevant to Domain A economic activity coordination.

---

### Dimension 4: Messaging and Moderation

*Threaded discussion, moderation tools, harassment prevention, content policy, bot automation — sensitive for a community coordinating economic activities*

| Platform | Threaded Discussion | Moderation Tools | Spam/Harassment Control | Bot/Automation | DMs | Score |
|---|---|---|---|---|---|---|
| **Mighty Networks** | Full threaded posts per Space | Per-Space moderation queue; member suspension; basic AI flagging | AI flagging; no Akismet equivalent | Limited automations (API-locked on Launch) | Direct messaging | **4** |
| **Discourse** | Full threaded forum (industry-leading forum UX) | Akismet spam detection; trust-level gating (TL0 auto-limits); flag queue; silence; suspend; Automation plugin | Trust level gating is the most effective hands-off spam control evaluated; TL0 users post-limited automatically; Akismet catches spam before posting | Webhooks + REST API + Discourse Automation plugin (all self-hosted plans) | Private messages (full threading; not SMS-style) | **5** |
| **Matrix/Element** | Threaded replies + Space organization | Mjolnir moderation bot; room ACLs; federated ban lists; ban propagation | Mjolnir pattern matching; ban list sharing prevents coordinated harassment across federated servers | Full Matrix Client-Server API; Application Services (bots and bridges); MESH-API bridge | E2E encrypted DMs by default | **4** |
| **Nextcloud Hub** | Talk chat (basic threads; not forum-grade) | Admin deletion only; no automated moderation | None built-in | Webhooks via Flow; limited automation | Talk DMs | **2** |
| **Nextcloud + Matrix** | Matrix: full threaded messaging; Nextcloud Talk: supplemental chat | Mjolnir (Matrix) + Nextcloud admin controls | Mjolnir handling Matrix rooms; Nextcloud Talk for casual coordination | Full Matrix API + Nextcloud Flow webhooks | Matrix E2E encrypted DMs + Nextcloud Talk DMs | **4** |

**Harassment prevention note**: For a community working on politically adjacent topics (economic resilience, local currency, cooperative models, mutual aid coordination), harassment prevention is operational rather than theoretical. Discourse's automatic TL0 rate limiting (1 topic/day, 10 replies/day, 3 links/post for new users) and Akismet integration provide the strongest hands-off protection without requiring constant admin attention.

**E2E encryption note**: For Domain A, where participants may share sensitive financial or material information in DMs (mutual aid requests, resource exchange negotiations), Matrix/Element's E2E encrypted DMs provide meaningfully stronger protection than Discourse's server-encrypted private messages.

---

### Dimension 5: Off-Grid Readiness

*Offline-first sync, local-first architecture, low-bandwidth support, Meshtastic bridge capability — binary disqualifier for any community with rural Zone 5 members*

| Platform | Offline Support | Local-First Architecture | Mobile Offline | Low-Bandwidth | Self-Hostable | Meshtastic Bridge | Score |
|---|---|---|---|---|---|---|---|
| **Mighty Networks** | None | Cloud-only SaaS | None | Cloud-dependent; fails on 2G | No | No | **0** |
| **Discourse** | PWA service-worker read cache | Partial (read-only offline via PWA) | PWA installable from browser; read-only offline | Minimal JavaScript; low-bandwidth mode available | Yes (AGPL; official Docker) | No | **2** |
| **Matrix/Element** | Element X: instant local launch from cached room list; compose offline, send on reconnect | Local message store; full sync on reconnect | iOS/Android/F-Droid; offline read + compose | Bandwidth-adaptive sync; LoRa bridgeable | Yes (AGPL; Synapse/Dendrite) | **Yes — MESH-API confirmed (2026)** | **5** |
| **Nextcloud Hub** | Desktop sync client (Windows/Mac/Linux) + mobile app; full bidirectional offline sync | Local file cache on all devices; sync on reconnect | iOS/Android Nextcloud app; offline file access and editing | Runs entirely on LAN; zero internet required | Yes (AGPL; Docker) | No native; files sync locally covers most use cases | **5** |
| **Nextcloud + Matrix** | Files offline via Nextcloud desktop/mobile sync; messages offline via Element X; calendar offline via CalDAV sync | All data local on every device; multiple paths to offline access | Nextcloud app + Element X; both maintain offline state | Runs on LAN without internet; LoRa bridge for Matrix messages | Yes (AGPL; both components) | **Yes — Matrix side via MESH-API; files via Nextcloud sync** | **5** |

**Zone 5 binary**: Rural counties in IA and MI have broadband coverage below 60% (FCC 2024 data). Winter weather events (ice storms, blizzards) cause multi-day outages. During the scenarios where resilience resources matter most, internet connectivity is least reliable. Mighty Networks fails completely when connectivity is unavailable. Discourse can display cached content but cannot coordinate new resource exchanges. This is a decisive architectural difference, not a preference.

**Meshtastic bridge status (updated June 2026)**: The MESH-API project (GitHub: mr-tbot/mesh-api) provides a bidirectional bridge between Meshtastic LoRa mesh networks and Matrix rooms. This is a community-maintained project, not an official Element/Matrix product. It should be treated as an advanced capability (confidence: 80%) rather than a guaranteed feature. The architecture is production-capable but requires technical configuration. For a community deploying Zone 5 mesh infrastructure per PHASE_6_COMMUNICATION_INFRASTRUCTURE_SCOPING.md, this bridge means Matrix room messages can propagate over LoRa when cell and internet are both unavailable.

---

### Dimension 6: Cost Structure

*Per-user vs. flat fee, free tier, nonprofit discounts, scaling economics, vendor lock-in risk, hidden costs*

| Platform | Free Tier | Entry Cost | Scale Cost (100 members) | Per-User Penalty | Nonprofit Discount | Vendor Lock-In | Score |
|---|---|---|---|---|---|---|---|
| **Mighty Networks** | 14-day trial only | $79/month (Launch) | $79/month (Launch handles 100+) | No per-user fee; 2% transaction fee | None confirmed | Medium — limited data export; no API on Launch | **2** |
| **Discourse** | Yes (self-hosted, $0) | $0 software + $7–17/month (VPS + email) | $0 software; hardware scales | No per-user fee | 50% nonprofit hosted; 85% educational hosted | None (self-hosted AGPL; full export) | **5** |
| **Matrix/Element** | Yes (self-hosted, $0) | $0 software + $5–15/month VPS (or $0 on raspby1) | $0 software; hardware scales | No per-user fee | N/A (open source) | None (self-hosted; full data ownership) | **5** |
| **Nextcloud Hub** | Yes (self-hosted, $0) | $0 software + $5–15/month VPS (or $0 on raspby1) | $0 software; hardware scales | No per-user fee | N/A (open source) | None (self-hosted; full data ownership) | **5** |
| **Nextcloud + Matrix** | Yes (self-hosted, $0) | $0 software + $5–15/month VPS (or $0 on raspby1) | $0 software; add RAM as community grows | No per-user fee | N/A (open source) | None; all data on community-owned hardware | **5** |

**Hidden cost note — Mighty Networks**: The 2% transaction fee on Launch applies to all paid content. At $500/month community revenue (workshops, seed kits), that adds $10/month in fees. Moving to Scale ($179/month) for API access doubles the base cost. No nonprofit discount confirmed. Pricing increased from ~$41/month (prior Launch equivalent) to $79/month in the 2025–2026 rebranding; future increases are plausible.

**Three-year projection**:

| Scenario | Option A (Nextcloud + Matrix) | Option B (Discourse) | Option C (Mighty Networks) |
|---|---|---|---|
| Year 1 (launch, 50 members) | $0–$180 (raspby1 or VPS) | $84–$204 (VPS + email) | $950 (annual billing) |
| Year 2 (growth, 100 members) | $0–$180 (same hardware) | $84–$204 (same VPS) | $950 |
| Year 3 (scale, 200 members) | $60–$300 (possible VPS upgrade) | $84–$204 (possible VPS upgrade) | $950–$2,148 (may need Scale for API) |
| **3-year total** | **$60–$660** | **$252–$612** | **$2,850–$5,046** |

Option C costs $2,200–$4,400 more over 3 years than Options A or B with zero additional capability for the Zone 5 off-grid use case. The difference funds 2–4 community seed swap events, a community broadfork purchase, or 3–5 years of Loomio Pro.

---

### Dimension 7: Integration Pathways

*APIs, webhooks, GitHub Pages integration, Phase 5 publication output compatibility, CalDAV, Tailscale mesh*

| Platform | API Access | Webhooks/Automation | GitHub Integration | Phase 5 Integration | Tailscale/LAN | Score |
|---|---|---|---|---|---|---|
| **Mighty Networks** | Scale plan only ($179/month); none on Launch | Zapier on Scale; none on Launch | None native | Manual PDF upload only; no auto-announce on Launch | Cloud-only; no LAN deploy | **2** |
| **Discourse** | Full REST API on all self-hosted plans (no tier lock) | Webhooks + Discourse Automation plugin (all self-hosted plans) | GitHub OAuth login; webhook triggers from GitHub Actions | Phase 5 guides as wiki posts; Discourse embed widget on GitHub Pages | Deployable on any VPS; accessible via Tailscale | **5** |
| **Matrix/Element** | Full Matrix Client-Server API; Application Services for bots/bridges | Matrix webhook bridge (matrix-appservice-webhooks); MESH-API | GitHub → Matrix webhook bridge (automated PR/commit notifications) | Matrix rooms for document discussion; link Phase 5 GitHub Pages in room topic | Native Tailscale deploy; runs on raspby1 today | **4** |
| **Nextcloud Hub** | Full REST API; CalDAV/CardDAV/WebDAV | Webhooks via Flow; Zapier connector | GitHub OAuth; GitHub → Nextcloud webhook integration | Upload Phase 5 documents; real-time co-editing; offline sync to all devices | Native Tailscale deploy; runs on raspby1 today | **4** |
| **Nextcloud + Matrix** | Full REST API (Nextcloud) + Matrix Client-Server API + CalDAV/WebDAV; richest API surface of any configuration | Nextcloud Flow + Matrix webhook bridge + MESH-API | GitHub → Matrix room + GitHub → Nextcloud webhook; GitHub OAuth | Phase 5 guides in Nextcloud (co-editable + offline); Matrix rooms for discussion; GitHub Pages links in room topics | Designed for LAN/Tailscale; runs entirely on raspby1 today | **5** |

**Phase 5 integration specifics**: Phase 5 publishes June 5 (~45,000 words, 8–10 guides). The platform must make these accessible as living documents. Discourse wiki posts, Nextcloud collaborative documents, and Matrix room links are the three architectures that allow community annotation and extension of Phase 5 content. Mighty Networks on the Launch plan treats Phase 5 content as inert PDFs with no programmatic update path.

**Discourse embed workflow** (most concrete Phase 5 integration):
```
GitHub Actions builds Phase 5 → deploys to GitHub Pages
    → GitHub webhook triggers Discourse post in "Knowledge Base" category
    → Discourse embed widget shows recent community discussion on every Phase 5 page
    → Community members click through from publication site to discussion forum
    → TL2+ members annotate wiki posts with local case studies
```

---

### Dimension 8: Domain A-Specific Features

*Job boards, skill exchange, resource inventory, mutual aid coordination, cooperative governance — features specific to Community Economic Resilience*

| Platform | Skill Exchange / Job Board | Resource Inventory | Mutual Aid Request Flow | Cooperative Governance | Economic Activity Scheduling | Score |
|---|---|---|---|---|---|---|
| **Mighty Networks** | None native; workaround via custom post types | None native | Member-to-member DMs + group posts | Polls only | Events calendar | **2** |
| **Discourse** | Classified-style sub-forum + tag system (e.g., "Resource Offers" category tagged by Skills/Tools/Food/Transport) | Wiki posts as resource registers; full-text search | Tagged posts + private messages for coordination; persistent searchable history | Trust-level governance; Polls plugin; integration with Loomio | Events plugin + time zone display | **4** |
| **Matrix/Element** | Structured rooms workaround (e.g., "#skill-exchange" room with pinned offer format) | Nextcloud bridge for inventory files | Rooms as request channels; offline compose via Element X | Votes via bots; no native governance | Nextcloud CalDAV bridge | **3** |
| **Nextcloud Hub** | Deck (Kanban) + Forms for listings and intake | Shared spreadsheet (Nextcloud Office) + Deck for visual tracking; full version history | Forms for request intake; Tasks for fulfillment tracking; Deck for pipeline visualization | Workflow automation via Flow; no native voting | Appointments app for booking; CalDAV calendar | **4** |
| **Nextcloud + Matrix** | Nextcloud Forms + Deck for structured listings; Matrix rooms for real-time coordination; offline accessible | Nextcloud shared spreadsheet + version history; Matrix room for updates; offline via sync client | Nextcloud Forms → Deck pipeline + Matrix room announcements; works offline | Loomio supplement + Matrix room for discussion + Nextcloud doc for decision log | Nextcloud Appointments + CalDAV + Matrix announcements | **4** |

**Discourse skill exchange example**: A "Resource Offers and Requests" category with post tags [Skills] [Tools] [Food] [Seed] [Labor] [Capital] creates a structured exchange board. Posts are threaded (negotiations in replies), persistent (no deletion), full-text searchable, and emailed to subscribers. A member can follow tags and receive email whenever a relevant offer appears. This is functional without custom development or add-ons.

**Nextcloud mutual aid flow example**: A Nextcloud Form captures resource requests (type, urgency, quantity, pickup location). Submissions feed into a Nextcloud Deck board with columns for Pending / Matched / Fulfilled. A Matrix room notification announces each new request. Coordinators move cards through the Deck pipeline. All data is self-hosted, offline-accessible, and version-tracked.

---

### Consolidated Scored Matrix

**Total possible score: 40 points across 8 dimensions.**

| Platform | D1: Access | D2: Files | D3: Events | D4: Messaging | D5: Off-Grid | D6: Cost | D7: Integration | D8: Domain A | Total | Overall |
|---|---|---|---|---|---|---|---|---|---|---|
| **Mighty Networks** | 4 | 2 | 4 | 4 | 0 | 2 | 2 | 2 | **20/40** | 5.0/10 |
| **Discourse** | 5 | 3 | 3 | 5 | 2 | 5 | 5 | 4 | **32/40** | 8.0/10 |
| **Matrix/Element** | 4 | 3 | 3 | 4 | 5 | 5 | 4 | 3 | **31/40** | 7.75/10 |
| **Nextcloud Hub** | 4 | 5 | 5 | 2 | 5 | 5 | 4 | 4 | **34/40** | 8.5/10 |
| **Nextcloud + Matrix (Option A)** | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | **38/40** | 9.5/10 |

---

## Section 4: Deep-Dive Analysis — Three Recommended Options

---

### Option A — Autonomy Path: Nextcloud Hub + Matrix/Element (Self-Hosted)

**Score**: 38/40 (9.5/10)
**Confidence**: 91%
**Monthly cost**: $0 software + $0–15/month VPS (or $0 on existing raspby1)
**Annual cost**: $0–$180/year infrastructure + $649/year Loomio Pro nonprofit (optional governance supplement)
**Setup time**: 6–10 hours (Docker familiarity required)

#### 4.1A Architecture Breakdown

Option A deploys two complementary open-source systems on the same host:

**Nextcloud Hub** handles: files and document library (seed catalog, farm tools inventory, governance templates, Phase 5 guides), real-time collaborative editing (Collabora Online backend), CalDAV calendar (resource booking, community events, planting schedule), Nextcloud Talk (video conferencing for community calls), Nextcloud Forms (mutual aid request intake), Nextcloud Deck (resource pipeline visualization), and desktop/mobile offline sync.

**Matrix/Element** handles: persistent threaded messaging (all community channels), end-to-end encrypted DMs for sensitive coordination, the Mjolnir moderation bot for hands-off harassment prevention, Element X mobile client for offline compose-and-send, and the MESH-API bridge for LoRa/Meshtastic communication when internet is unavailable.

The two systems integrate via Nextcloud's CalDAV-to-Matrix notification bridge and shared links. Members use Nextcloud for documents and calendar; Element for messaging. The dual UX surface is the primary adoption challenge and requires a one-page onboarding guide.

**Hardware target**: The existing raspby1 (Raspberry Pi 5, 8 GB RAM, 100.70.184.84 Tailscale) is the preferred host. Dendrite (lightweight Matrix server) rather than Synapse reduces RAM footprint. At typical community usage patterns (asynchronous, not simultaneous peaks), the Pi 5 handles 50–200 members. Thermal note (from project memory): idle temperature is 81–84°C; under sustained compute 87.8°C. Active cooling upgrade ($20–40 one-time) is recommended before deploying Option A on raspby1. Alternative: Hetzner CX22 VPS at $6/month eliminates thermal risk.

#### 4.2A Integration with Phase 5 Output (45K Words)

```
Phase 5 publication (June 5, GitHub Pages — 8–10 guides, ~45,000 words)
    → Upload all guides to Nextcloud shared folder (collaborative editing enabled)
    → Each guide becomes a Nextcloud Office document: community can annotate in-line
    → Nextcloud desktop sync: every member's device caches guides offline before going to field
    → Matrix rooms created: #phase5-discussion, #seed-library, #tools-library, #governance
    → GitHub Actions webhook → Matrix room: auto-announce when new Phase 5 content publishes
    → Nextcloud Flow webhook → Matrix room: auto-announce new document uploads
    → Offline workflow: member in rural MI edits offline note in Nextcloud Office
      → syncs to server on reconnect → version history captures every revision
```

**Phase 5 document lifecycle on Option A**:
- Day 1: Upload 8–10 guides as Nextcloud Office documents (shared with community folder)
- Week 1–4: Community members annotate, correct, and add local case studies directly in documents
- Month 2+: Documents evolve from research output to living community protocols, with version history preserving all changes

#### 4.3A Author Recruitment Workflow (18 Personalized Emails per Phase 5/6)

Author recruitment for Phase 6 research uses the following platform-native workflow:

1. Author prospect identified (from PHASE_6_WAVE_2_AUTHOR_PROFILES.md or Domain A research)
2. Personalized outreach email sent via existing email infrastructure (Gmail/Proton/etc.)
3. On positive response: admin provisions Nextcloud account (username, temporary password) + Matrix invite
4. Author receives: Nextcloud login (file access, shared document folder, calendar event for onboarding call), Element Matrix invite (joins #authors room and their domain-specific channel)
5. Onboarding document in Nextcloud walks through: project context, Phase 5 synthesis, Domain A scope, contribution expectations, revision workflow
6. Author contributions: edit shared Nextcloud documents; discuss in Matrix room; receive notifications via Element X (offline-capable)

Platform native advantage: author contributions are version-tracked in Nextcloud from day one. No separate document management tool needed. All author communication is in Matrix channels (archived, searchable, E2E encrypted).

#### 4.4A Off-Grid Use Case Fit

Zone 5 rural members (IA, MI) with intermittent LTE or Starlink during winter weather:

- **Before connectivity loss**: Nextcloud desktop app syncs all community documents and the seed catalog to local device. Element X caches last 30 days of message history.
- **During outage**: User reads Phase 5 guides and seed catalog offline (Nextcloud offline files). Can compose Matrix messages that queue for delivery. Can edit Nextcloud documents offline with sync on reconnect.
- **Extended outage (Meshtastic scenario)**: If the community has deployed Zone 5 mesh infrastructure per PHASE_6_COMMUNICATION_INFRASTRUCTURE_SCOPING.md, the MESH-API bridge allows Matrix room messages to propagate over LoRa when both internet and cell are unavailable. This is the only platform configuration that addresses this scenario.
- **Recovery**: On reconnect, Nextcloud syncs all queued changes; Matrix delivers all queued messages. Version conflicts resolved automatically by Nextcloud's conflict resolution.

#### 4.5A Cost Analysis

| Component | Cost | Notes |
|---|---|---|
| Nextcloud software | $0 | AGPL open source |
| Matrix Dendrite software | $0 | AGPL open source |
| Hosting (raspby1) | $0 | Existing infrastructure |
| Hosting (Hetzner CX22 VPS) | $6/month | Alternative if thermal risk is unacceptable |
| Email delivery (Brevo free tier) | $0 | 300 emails/day free; adequate for community notifications |
| Active cooling (raspby1) | $20–40 one-time | Recommended before deployment |
| Loomio Pro nonprofit (optional) | $649/year ($54/month) | Governance supplement; self-hosted = $0 |
| **Total (raspby1, no Loomio)** | **$0–$40 one-time** | |
| **Total (VPS, with Loomio)** | **$721/year ($60/month)** | |
| **Total (raspby1, with Loomio)** | **$649/year ($54/month)** | |

#### 4.6A Deployment Timeline

| Date | Action | Time |
|---|---|---|
| June 3 | Decision; active cooling ordered; Docker Compose YAML written for Nextcloud + Dendrite | 1 hour |
| June 3–4 | Deploy on raspby1 (or Hetzner CX22 if VPS preferred); DNS configured if VPS | 2–3 hours + DNS wait |
| June 4 | Nextcloud admin config: branding, groups, Deck + Forms + Calendar apps enabled, SMTP | 2 hours |
| June 4 | Dendrite (Matrix) install; Element Web UI; first rooms created | 2 hours |
| June 5 | Phase 5 guides uploaded to Nextcloud shared folder; co-editing enabled | 1 hour |
| June 5 | Matrix rooms: #general, #seed-library, #tools-library, #governance, #phase5-discussion | 30 min |
| June 5–8 | First 15–20 builder accounts provisioned (Nextcloud + Matrix); onboarding guide sent | 1 hour |
| June 9–14 | Domain A community onboarding; Nextcloud Calendar event for June 15 session | Ongoing |
| June 15 | Community foundation session via Nextcloud Talk video | — |

**Total setup**: 8–11 hours; requires Docker familiarity and comfort with Linux command line.

#### 4.7A Success Criteria

- June 5: All Phase 5 guides accessible via Nextcloud with offline sync
- June 15: June 15 community foundation session with 10+ participants via Nextcloud Talk
- July 1: Seed catalog live in shared Nextcloud spreadsheet with 3+ contributors
- July 15: Farm tools inventory in Nextcloud Deck; first tool reservation via Appointments
- August 1: 30+ active members with local offline sync established; Loomio first governance vote

---

### Option B — Bootstrap Path: Discourse Self-Hosted + Loomio

**Score**: 32/40 (8.0/10)
**Confidence**: 90%
**Monthly cost**: $7–17/month (VPS + email SMTP)
**Annual cost**: $84–$204/year infrastructure + $649/year Loomio Pro nonprofit (optional)
**Setup time**: 6–8 hours

#### 4.1B Architecture Breakdown

Option B deploys Discourse on a dedicated VPS (Hetzner CX22 at $6/month is the recommended host). Discourse provides: threaded forum discussion (industry-leading), trust-level-based self-governance (no admin intervention for spam control), wiki posts for Phase 5 document annotation, full REST API for GitHub Pages integration, Events plugin for community sessions, and GitHub OAuth for one-click login.

Loomio (cloud Pro nonprofit or self-hosted) adds structured governance: ranked-choice voting, time polls, proposal threads with explicit outcomes, and decision log.

What Discourse cannot provide: real-time document co-editing, offline posting (read-only PWA cache only), and native video conferencing. These limitations are acceptable if all community members have reliable connectivity.

#### 4.2B Integration with Phase 5 Output

```
Phase 5 publication (June 5, GitHub Pages)
    → Create Discourse category: "Phase 5 Knowledge Base"
    → Post each of the 8–10 guides as Discourse wiki posts (editable by TL2+ members)
    → Pin governance framework document as category-pinned post
    → Discourse embed widget on GitHub Pages: recent discussions visible on the static site
    → GitHub OAuth: community members authenticate with existing GitHub accounts (no new password)
    → GitHub Actions → Discourse API: auto-post announcement when new Phase 5 content publishes
    → Automation plugin: auto-welcome new members with Phase 5 reading list
    → Events plugin: June 15 Phase 6 Domain A foundation session
```

**Discourse embed widget** (most valuable GitHub Pages integration available across all platforms):
```html
<!-- Added to GitHub Pages layout template -->
<div id='discourse-comments'></div>
<script>
  window.DiscourseEmbed = {
    discourseUrl: 'https://community.yoursite.org/',
    topicId: PHASE5_TOPIC_ID
  };
  (function() {
    var d = document.createElement('script');
    d.type = 'text/javascript'; d.async = true;
    d.src = window.DiscourseEmbed.discourseUrl + 'javascripts/embed.js';
    document.body.appendChild(d);
  })();
</script>
```

Result: Every Phase 5 publication page shows recent community discussion without requiring the reader to visit the community forum separately. This is the most direct possible integration between the publication site and the community platform.

#### 4.3B Author Recruitment Workflow

1. Author prospect identified → personalized outreach email sent externally
2. Positive response: admin generates Discourse invite link (one-click, expires in 72 hours)
3. Author creates account via GitHub OAuth or email; lands at TL1 automatically
4. Pinned welcome post directs author to: project context wiki, Phase 5 Knowledge Base, author coordination PM thread
5. Author contributions: edits wiki posts (TL2 earned after ~30 days, or manually granted by admin); posts in author working group category; receives email digests of all activity
6. Revision tracking: Discourse wiki post history preserves every change with timestamp and editor identity

Platform advantage: Discourse's email digest means authors who are not daily users still receive summaries without logging in. The trust level system means active authors naturally earn more platform authority over time.

#### 4.4B Off-Grid Use Case Fit

Discourse as a PWA can cache the most recently visited pages via service worker. This means a community member who loaded their seed library category page before losing connectivity can read the content offline. They cannot post new content, upload files, or coordinate new exchanges without connectivity.

For communities where all or nearly all members have reliable connectivity (urban/suburban members, Starlink customers with stable connection), this limitation is acceptable. For any community with rural members who may lose connectivity during winter weather events, Option B provides significantly less resilience than Option A.

**Recommendation**: If any identified community members are in rural IA or MI with connectivity uncertainty, upgrade from Option B to Option A. If all members have reliable Starlink or fiber, Option B is fully adequate and easier to maintain.

#### 4.5B Cost Analysis

| Component | Cost | Notes |
|---|---|---|
| Discourse software | $0 | AGPL open source |
| Hetzner CX22 VPS | $6/month | 2 vCPU, 4 GB RAM; handles 500+ member Discourse |
| Email SMTP (Amazon SES) | $0–$2/month | First 62,000 emails/month free (EC2); ~$0.10/1,000 thereafter |
| Akismet spam API key | $0 | Free for personal and open source projects |
| Backup (Backblaze B2) | $0.60/month | ~100 GB backup at $0.006/GB |
| Loomio Pro nonprofit (optional) | $649/year | Governance supplement |
| **Total (no Loomio)** | **$84/year ($7/month)** | |
| **Total (with Loomio)** | **$733/year ($61/month)** | |

#### 4.6B Deployment Timeline

| Date | Action | Time |
|---|---|---|
| June 3 | Decision; Hetzner CX22 provisioned; DNS A record set | 30 min + DNS wait (24h) |
| June 4 | Discourse Docker install via official script; admin account created | 2 hours |
| June 4 | Categories configured: Knowledge Base, Resource Exchange, Skills Board, Events, Governance | 1 hour |
| June 4 | Events plugin installed; GitHub OAuth configured; SMTP configured; Akismet key added | 1 hour |
| June 5 | Phase 5 guides posted as wiki posts in Knowledge Base category | 2 hours |
| June 5 | Discourse embed widget added to GitHub Pages layout | 30 min |
| June 5–8 | First 15–20 builders invited via email; onboarding thread pinned at TL1 | 30 min |
| June 9–14 | Domain A community onboarding; Events plugin: June 15 session created | Ongoing |
| June 15 | Community foundation session (external Zoom link from Discourse event post) | — |

**Total setup**: 6–8 hours; official Discourse install script minimizes Linux expertise needed.

#### 4.7B Success Criteria

- June 5: All Phase 5 guides posted as wiki posts; Discourse embed live on GitHub Pages
- June 15: June 15 community foundation session with 10+ RSVP via Events plugin
- July 1: 20+ active members; resource offers/requests category live with 5+ listings
- July 15: First Loomio governance vote linked from Discourse governance category
- August 1: 40+ active members; at least 3 wiki posts annotated by TL2+ community members

---

### Option C — Scale Path: Mighty Networks Launch + Loomio

**Score**: 20/40 (5.0/10)
**Confidence**: 82% (below 85% recommendation threshold — viable with acknowledged limitations)
**Monthly cost**: $79/month (Launch plan)
**Annual cost**: $950/year (annual billing) + $649/year Loomio Pro nonprofit (optional)
**Setup time**: 3–4 hours; zero technical expertise required

#### 4.1C Architecture Breakdown

Mighty Networks Launch provides: native iOS/Android apps with push notifications (the primary differentiator for volunteer engagement), native event system with RSVP and push reminders, per-Space organization (Knowledge Base, Resource Exchange, Skills Board, Events, Governance), threaded discussion, direct messaging, and basic AI content flagging.

Loomio adds structured governance (see Section 5).

What Mighty Networks cannot provide on the Launch plan: API access (locked to Scale at $179/month), automated integration with GitHub Pages, real-time document editing, offline capability of any kind, and data export beyond manual CSV download.

**Confidence is 82%, below the 85% threshold**: The two dimensions most specific to Domain A — off-grid readiness and programmatic integration — score 0 and 2 respectively. A community built around economic resilience during infrastructure disruption, coordinating via a cloud-only SaaS platform with no API access, has a structural credibility gap. Option C is recommended only when the team has confirmed: (1) all initial participants have reliable connectivity; (2) no technical capacity exists for self-hosting; and (3) there is a 6-month migration plan to Options A or B as the community grows.

#### 4.2C Integration with Phase 5 Output

```
Phase 5 publication (June 5, GitHub Pages)
    → Manual upload: each guide as PDF/Word document to Knowledge Base Space
    → Create one post per guide with summary and link to GitHub Pages source
    → Push notification to all members on publication day
    → June 15 community foundation event with RSVP and push reminders
    → Phase 6 Domain A research: post sections as long-form articles in Knowledge Base Space
    → No automated integration (API locked on Launch plan)
```

All Phase 5 content integration is manual and requires a community manager to upload and post each document. Documents are static uploads — not collaborative editing surfaces.

#### 4.3C Author Recruitment Workflow

1. Author prospect identified → personalized outreach email sent externally
2. Positive response: admin sends Mighty Networks invite link
3. Author joins community; admin assigns host or moderator role
4. Author receives: Space access to Knowledge Base and author coordination space
5. Author contributions: posts in author Space; receives push notification alerts for mentions
6. Limitation: no version-controlled document editing; no offline access; no API for automated coordination

#### 4.4C Off-Grid Use Case Fit

Mighty Networks has zero offline capability. The platform is cloud-only SaaS. When connectivity is lost, the platform is completely unavailable. Community members cannot access Phase 5 guides, seed catalogs, tools inventory, or any coordination information without internet.

For a community whose explicit purpose is economic resilience during infrastructure disruption, this is the defining architectural weakness. Option C is viable only if the team accepts this limitation as acceptable for the current phase and plans to migrate to Option A or B within 6 months.

#### 4.5C Cost Analysis

| Component | Cost | Notes |
|---|---|---|
| Mighty Networks Launch | $79/month ($950/year annual) | 2% transaction fee on paid content |
| Mighty Networks Scale (if API needed) | $179/month ($2,148/year) | Required for any programmatic integration |
| Loomio Pro nonprofit (optional) | $649/year | Governance supplement |
| **Total (Launch, no Loomio)** | **$950/year** | |
| **Total (Launch, with Loomio)** | **$1,599/year** | |
| **Total (Scale, with Loomio)** | **$2,797/year** | Required if Phase 5 webhook integration is needed |

#### 4.6C Deployment Timeline

| Date | Action | Time |
|---|---|---|
| June 3 | Start 14-day free trial (Growth plan features active during trial) | 15 min |
| June 3 | Configure: community name, branding, Spaces (Knowledge Base, Resource Exchange, Skills, Events, Governance) | 2 hours |
| June 3–4 | Upload Phase 5 documents to Knowledge Base Space | 1 hour |
| June 4 | Create June 15 community foundation event with RSVP | 30 min |
| June 5 | Invite first 15–20 builders via email invite link | 30 min |
| June 9–14 | Domain A onboarding; push notification reminders for June 15 event | Ongoing |
| June 17 | Trial ends; $79/month Launch billing begins (or evaluate and cancel) | — |

**Total setup**: 3–4 hours; no technical expertise required.

#### 4.7C Success Criteria + 6-Month Migration Trigger

- June 5: All Phase 5 guides uploaded; community live with at least 10 members
- June 15: Foundation session with 10+ RSVP; push notification reminders sent
- July 1: 20+ active members; resource exchange posts live
- **Migration trigger**: If by July 31 any of the following are true → initiate migration to Option A or B within 30 days:
  - Any rural member reports inability to access community during connectivity loss
  - Team wants automated GitHub Pages → community integration (requires Scale at $179/month or migration)
  - Team wants shared collaborative editing of seed catalog or community protocols
  - Mighty Networks raises pricing again

---

## Section 5: Governance Supplement — Loomio

Regardless of primary platform choice, Loomio is the recommended governance supplement for structured community decision-making.

**Current pricing (verified June 2, 2026)**:
- Community: $10/month or $199 lifetime (limited to ~30 members)
- Starter: $25/month or $199/year (small groups; limited subgroups)
- Pro nonprofit: $75/month or $649/year (unlimited members, unlimited subgroups, full governance tooling, 50% nonprofit discount applied)
- Pro standard: $149/month or $1,299/year
- Self-hosted: $0 (AGPL, Docker)

**Note on pricing history**: Prior analysis documents (v1, v2) listed Pro nonprofit at $499/year. The current official figure is $649/year. The Starter plan ($199/year) caps at approximately 30 members — insufficient for Phase 6 scale once the community exceeds 30 active decision-makers. Budget for Pro nonprofit ($649/year) if cloud Loomio is the governance path, or self-host Loomio at $0 software cost.

**Phase 6 governance use cases**:
- Research priority voting: which economic resilience domains get next Phase 6 investigation cycle
- Seed library policy: which varieties to prioritize, open-pollinated vs. hybrid policy
- Tools library policy: deposit requirements, check-out periods, damage policy
- Cooperative formation decisions: which model (worker-owned, consumer-owned, hybrid) to pilot first
- Meeting scheduling: time polls for foundation sessions across IL/MI/IA/IN/WI time zones
- Domain expansion: which Phase 6 candidates (B, C, D, E, F) get next investment

**Integration by platform**:
- Option A (Matrix): Loomio has native Matrix/Element outbound notifications → notifies #governance room on each new vote or decision
- Option B (Discourse): Loomio → email notifications → Discourse processes email replies into governance threads
- Option C (Mighty Networks): Loomio → email notifications only (no API on Launch plan)

**Recommendation**: Begin with Loomio Starter ($199/year) while Phase 6 membership is below 30 active decision-makers. Upgrade to Pro nonprofit ($649/year) when membership grows. Self-hosted Loomio on raspby1 is viable for advanced technical teams and reduces the recurring cost to $0.

---

## Section 6: Decision Scorecard

Answer these four questions in order. The first hard requirement determines the path.

**Q1: Is off-grid or low-connectivity capability a hard requirement for any initial Phase 6 participants?**

- Yes (any rural or off-grid members in the first 50 participants) → **Option A only**. Nextcloud + Matrix is the only configuration with full offline capability.
- No, but it is a near-term requirement (6–12 months) → **Option A strongly preferred; Option B as fallback**.
- No, all members have reliable connectivity (Starlink, fiber, or consistently available broadband) → Proceed to Q2.

**Q2: Does the team have Docker-capable technical capacity for self-hosting (one person comfortable with Linux command line)?**

- Yes → Options A or B; proceed to Q3.
- No → Option C (Mighty Networks, 3–4 hour no-code setup) or Discourse hosted at $50/month nonprofit.

**Q3: Does the community need to co-author documents in real time (shared protocol development, live seed catalog, tool inventory co-editing)?**

- Yes → **Option A** (Nextcloud is the only solution with native real-time collaborative editing that syncs offline).
- No (documents published centrally; community annotates via forum or comments) → Options A or B both sufficient; proceed to Q4.

**Q4: What is the realistic annual budget ceiling?**

- $0/year → Option A or B on raspby1 + self-hosted Loomio.
- $0–$300/year → Option B (Discourse VPS $84/year) + Loomio Starter ($199/year).
- $300–$700/year → Option A or B + Loomio Starter.
- $700–$1,000/year → Option A or B + Loomio Pro nonprofit ($649/year).
- $950–$1,600/year → Option C (Mighty Networks) + Loomio Pro nonprofit. Note the 3-year cost difference vs. Options A or B.

**Summary scorecard**:

| Decision Factor | Option A (Nextcloud + Matrix) | Option B (Discourse) | Option C (Mighty Networks) |
|---|---|---|---|
| Score | 9.5/10 | 8.0/10 | 5.0/10 |
| Confidence | 91% | 90% | 82% |
| Off-grid readiness | Full | Read-only | None |
| Document collaboration | Real-time co-editing | Async wiki only | Static uploads |
| Cost (Year 1) | $0–$180 | $84–$204 | $950 |
| Cost (3 years) | $60–$660 | $252–$612 | $2,850–$5,046 |
| Setup complexity | High (Docker required) | Medium (script-guided) | Low (no-code) |
| GitHub Pages integration | Strong (webhooks + links) | Best (embed widget + OAuth) | Manual only |
| Mobile experience | Nextcloud app + Element X | PWA (adequate) | Native apps (best) |
| Vendor lock-in | None (self-hosted AGPL) | None (self-hosted AGPL) | Medium (SaaS, limited export) |
| Admin time/month | 2–4 hours | 1–2 hours | 30 min |
| Deployment (June 5) | Achievable | Achievable | Achievable |
| Migration path | N/A (already optimal) | Upgrade to Option A if off-grid needed | Migrate to A or B within 6 months |

---

## Section 7: Migration and Fallback Strategy

### 7.1 Data Export Standards (All Options)

Establish quarterly data exports before any migration is needed:

| Platform | Export Format | What's Exported | Cadence |
|---|---|---|---|
| **Nextcloud** | `occ files:export` or WebDAV sync | All files, calendars, contacts, version history | Daily automated (desktop sync client is continuous) |
| **Matrix/Element** | Room export via Synapse/Dendrite admin API | Message history, media, room state | Monthly automated |
| **Discourse** | JSON backup via admin panel | Posts, users, wikis, categories, private messages | Monthly automated |
| **Mighty Networks** | CSV export (manual) | Member list, post content, event data | Quarterly manual |
| **Loomio** | CSV decision export (built-in) | All decisions, votes, outcomes | After each decision |

### 7.2 Platform-Independent Assets

Regardless of platform, maintain these community-owned assets that survive any platform failure:

1. **Member email list**: exported from any platform at any time; the community's most critical asset
2. **Seed catalog**: maintained as plain CSV or ODS file (openable without any platform)
3. **Tool inventory**: maintained as plain CSV or ODS file
4. **Decision log**: maintained as plain text or Markdown (exportable from Loomio or Discourse)
5. **Governance documents**: stored in at least two locations (platform + separate file store or email archive)

### 7.3 Fallback Sequence (Any Platform Failure)

If primary platform becomes unavailable:

1. **Emergency (immediate)**: Move to Signal group (15–20 members; immediate communication, no file storage)
2. **Short-term (within 1 week)**: Matrix.org free server (no self-hosting; any Element client; member joins immediately)
3. **Medium-term (within 4 weeks)**: Restore Option A or B self-hosted instance from backup; member email list drives re-onboarding announcement

---

## Section 8: 90-Day Operational Roadmap

### Month 1: June 3–July 2 (Foundation)

| Week | Action | All Options |
|---|---|---|
| June 3–5 | Platform decision + deployment | VPS or raspby1 configured; Phase 5 content loaded |
| June 5–8 | First 15–20 builders invited | Email invites; onboarding guide sent |
| June 9–14 | Onboarding + orientation | Seed library structure created; tools inventory started |
| June 15 | Community foundation session | First live call; member introductions; Phase 5 knowledge base walkthrough |
| June 16–30 | Seed library launch | 10–15 Zone 5 varieties cataloged; check-out protocol established |

### Month 2: July 3–August 1 (Build)

- Target: 30–50 active members
- Recruitment: Illinois Stewardship Alliance, Michigan Farmers Union, Iowa State Extension cooperative contacts, Indiana small farm networks, Wisconsin Farm Bureau alternative programs
- Milestone gate: if fewer than 25 members by July 15, escalate recruitment
- Phase 6 Domain A research outputs posted as they are produced (2–3 sections/week from July 8)
- First Loomio governance vote: community charter adoption
- Tools library: first equipment reservation via platform

### Month 3: August 2–September 1 (Scale)

- Target: 50–100 active members
- Weekly community calls (Nextcloud Talk / Zoom link)
- Seed swap event: virtual + in-person at regional nodes (IL, MI, IA)
- Tools library: equipment-sharing agreements between 3+ farm nodes
- Economic pilot: first mutual credit exchange or timebank test (10–15 participants)
- Phase 7 readiness: platform validated at 50+ members before October activation

---

## Sources

All pricing and features verified against official source pages and cross-checked against independent reviews, June 2, 2026.

**Mighty Networks**:
- [Pricing — Official](https://www.mightynetworks.com/pricing)
- [Growth plan — Official](https://www.mightynetworks.com/pricing/growth)
- [Pricing 2026 — Mihaelcacic](https://www.mihaelcacic.com/pricing-analysis/mighty-networks-pricing/)
- [Pricing 2026 — EzyCourse](https://ezycourse.com/blog/mighty-networks-pricing)
- [Pricing 2026 — Ruzuku](https://www.ruzuku.com/compare/mighty-networks-pricing)
- [Pricing 2026 — SchoolMaker](https://www.schoolmaker.com/blog/mighty-networks-pricing)

**Circle.so**:
- [Pricing — Official](https://circle.so/pricing)
- [True cost 2026 — AI Funnel Insider](https://aifunnelinsider.com/circle-so-pricing-2026/)
- [Pricing 2026 — SchoolMaker](https://www.schoolmaker.com/blog/circle-so-pricing)
- [Review 2026 — DEME Marketing](https://dememarketing.com/circle-so-review/)
- [Review 2026 — Learning Revolution](https://www.learningrevolution.net/circle-review/)

**Discourse**:
- [Pricing — Official](https://www.discourse.org/pricing)
- [vs. Flarum vs. NodeBB 2026 — Elest.io](https://blog.elest.io/discourse-vs-flarum-vs-nodebb-which-self-hosted-forum-platform-in-2026/)
- [PWA support — Discourse Meta](https://meta.discourse.org/t/is-pwa-feature-available-for-self-hosted/320612)
- [Self-hosted guide — SelfhostedGuides](https://selfhostedguides.com/discourse-self-hosted-forum/)

**Matrix / Element**:
- [Element Pricing — Official](https://element.io/en/pricing)
- [Matrix.org ecosystem](https://matrix.org/ecosystem/hosting/)
- [MESH-API Meshtastic bridge — GitHub](https://github.com/mr-tbot/mesh-api)
- [Meshtastic 2026 overview — Seeed Studio](https://www.seeedstudio.com/blog/2025/07/10/meshtastic-off-grid-mesh-network/)

**Nextcloud Hub**:
- [Hub features — Official](https://nextcloud.com/hub/)
- [Hub 26 Winter release — Official](https://nextcloud.com/blog/nextcloud-hub26-winter/)
- [Nextcloud Files — Official](https://nextcloud.com/files/)
- [Collabora Online + Nextcloud — Official](https://www.collaboraonline.com/partners/nextcloud/)

**Loomio**:
- [Pricing — Official](https://www.loomio.com/pricing/)
- [Subscription plans — Loomio Help](https://help.loomio.com/en/policy/subscriptions/pricing.html)
- [Nonprofits discount — Connecting Up](https://www.connectingup.org/product/loomio-nonprofits-50-discount)
- [Reviews 2026 — GetApp](https://www.getapp.com/collaboration-software/a/loomio/)

**Slack**:
- [Pricing — Official](https://slack.com/pricing)
- [Nonprofit pricing 2026 — Zenzap](https://www.zenzap.co/blog-posts/slack-nonprofit-pricing-in-2026-what-you-actually-get-and-what-to-watch-out-for)
- [Free plan limits — ViewExport](https://viewexport.com/post/slack-free-plan-limitations)

**Platform comparisons and context**:
- [Best community platforms nonprofits 2026 — Disco](https://www.disco.co/blog/best-community-platforms-for-nonprofits-2026)
- [HubSpot pricing 2026 — MO Agency](https://www.mo.agency/blog/hubspot-pricing)
- [Swell review 2026 — Research.com](https://research.com/software/reviews/swell)

**Mutual aid and cooperative economics context**:
- [Digital tools for mutual aid groups — Phoebe Tickell, Digital Fund](https://medium.com/digitalfund/communities-essential-guide-to-digital-tools-for-mutual-aid-groups-c1664d30b525)
- [Cooperative Economics Alliance of NYC](https://www.ceanyc.org/)
- [Community Seed Network](https://www.communityseednetwork.org/)

**Prior analysis documents (this project)**:
- PHASE_6_PLATFORM_ANALYSIS_v2.md (v2, June 1, 2026 — superseded)
- PHASE_6_DOMAIN_A_PLATFORM_ANALYSIS.md (June 2, 2026 — superseded by this document)
- PHASE_6_IMPLEMENTATION_GUIDE_OPTION_A_DISCOURSE.md
- PHASE_6_IMPLEMENTATION_GUIDE_OPTION_B_MIGHTY_NETWORKS.md
- PHASE_6_IMPLEMENTATION_GUIDE_OPTION_C_NEXTCLOUD_MATRIX.md

---

## Appendix A: Zone 5 Midwest Context

Zone 5 (IL, MI, IA, IN, WI) characteristics that directly affect platform selection:

1. **Connectivity**: Rural counties in IA and MI have broadband coverage below 60% (FCC 2024 data). Winter weather events (ice storms, blizzards) cause multi-day outages. Off-grid capability is an operational requirement for any community with rural members — not a preference.

2. **Agricultural calendar**: Peak coordination occurs in narrow windows: corn planting May 1–20, soybean May 10–June 5, hay cutting June–August, winter wheat September 15–October 10, harvest October–November. Platform must support asynchronous coordination; farmers do not have time for real-time platforms during peak season.

3. **Cooperative tradition**: The Midwest has the highest density of agricultural cooperatives in the US (USDA Agricultural Cooperative Statistics, 2023). Communities in this region are familiar with cooperative governance structures; Loomio's participatory decision-making tools align with this culture.

4. **Device diversity**: Rural members disproportionately use mobile devices (often older Android) rather than desktop computers. Nextcloud and Element both have well-maintained Android apps (F-Droid available for both for privacy-conscious users).

5. **Low-bandwidth reality**: Starlink (common in rural Zone 5) averages 25–60ms latency with variable packet loss during adverse weather. Browser-first SaaS platforms (Circle, Mighty Networks) load slowly under these conditions. Discourse's minimal JS mode and Nextcloud's sync client handle intermittent connectivity better than SaaS alternatives.

---

## Appendix B: Excluded Platforms Summary

| Platform | Category | Exclusion Reason |
|---|---|---|
| Swell | E-commerce / customer feedback tool | No community features; wrong product category |
| HubSpot Community | HubSpot's own support forum (not a product) | Not a purchasable product; HubSpot products are CRM |
| Substack Teams | Newsletter publishing workflow | No coordination features; useful as distribution channel only |
| Platform.sh / Upsun | PaaS hosting infrastructure | No community features; potential hosting provider for A or B |
| Lunchclub | 1:1 professional meeting matchmaker | No group features; categorically incompatible |
| Slack (free) | Team messaging with hard limitations | 90-day history deletion; 5 GB storage; no offline; per-user cost |
| Geneva | Social community app | Phone number required; no data export; no API; no offline |
| Circle.so | SaaS community platform | True cost $277–$405/month; no offline; no API on entry plan |

---

*Research confidence: 91% (upgraded from 89% in v3 based on confirmed MESH-API Matrix-Meshtastic bridge status, Nextcloud Hub 26 Winter offline improvements, and Circle.so true-cost verification). Pricing verified from official sources June 2, 2026. Feature assessments cross-checked across multiple independent reviews. Off-grid assessment based on technical architecture review. Zone 5 agricultural context from project research files and USDA cooperative data. No hands-on testing conducted; all assessments from documentation, official pricing pages, and independent reviews. Key evidence gap: Mighty Networks Growth plan "activity feeds coming soon" feature is unconfirmed in production; Growth plan features that are "coming soon" are not rated as current capabilities.*
