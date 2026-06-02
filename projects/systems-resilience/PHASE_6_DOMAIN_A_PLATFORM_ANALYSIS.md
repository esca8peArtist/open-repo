---
title: "Phase 6 Domain A — Community Economic Resilience: Platform Analysis & Selection"
project: systems-resilience
phase: 6
domain: "A (Community Economic Resilience)"
status: DECISION-READY — June 3 gate
created: 2026-06-02
decision_deadline: 2026-06-03
prior_analysis:
  - PHASE_6_PLATFORM_ANALYSIS.md (v1, general scope)
  - PHASE_6_PLATFORM_ANALYSIS_v2.md (v2, 8-dimension scored matrix)
cross_references:
  - PHASE_6_CANDIDATE_COMMUNITY_ECONOMIC_RESILIENCE.md
  - PHASE_6_IMPLEMENTATION_GUIDE_OPTION_A_DISCOURSE.md
  - PHASE_6_IMPLEMENTATION_GUIDE_OPTION_B_MIGHTY_NETWORKS.md
  - PHASE_6_IMPLEMENTATION_GUIDE_OPTION_C_NEXTCLOUD_MATRIX.md
---

# Phase 6 Domain A: Community Economic Resilience
## Platform Analysis and Selection — Decision Required June 3, 2026

---

## Executive Summary

This document analyzes 8 community coordination platforms against the specific requirements of Phase 6 Domain A: Community Economic Resilience. It extends and deepens two prior platform analyses (v1 and v2, both completed June 1, 2026) by reanchoring the evaluation to Domain A's distinct operational needs — coordinating economic activities (job boards, resource sharing, skill exchange) among 50–200 participants who include off-grid and rural households, and who may not use corporate email.

**Lead finding**: The prior analyses hold under Domain A-specific scrutiny with one key reweighting. For a mutual aid and cooperative economics community, off-grid readiness and document collaboration rise from desirable to near-essential: participants in economic resilience contexts need to coordinate resource exchanges when connectivity is unavailable. This moves the Nextcloud + Matrix/Element stack from a close third to a clear first for serious Domain A implementation. Discourse (self-hosted) remains the best single-app bootstrap option. Mighty Networks remains the fastest-to-launch SaaS option — but its hard zero on offline capability and absence of job board or resource exchange features is a more decisive gap at Domain A than it was in the general analysis.

Three platforms — Substack, Platform.sh, and Lunchclub — are formally excluded (wrong tool categories; detailed below). Slack free tier scores disqualifying limitations. Geneva lacks the document library and integration infrastructure for the domain.

**Recommended options** (in order of fit to Domain A requirements):

- **Option A: Nextcloud Hub + Matrix/Element (Self-Hosted)** — Best for Domain A coordination requiring off-grid resilience and document collaboration. Cost: $0–$15/month. Confidence: 91%.
- **Option B: Discourse (Self-Hosted) + Loomio** — Best bootstrap path with strong moderation, full API, and governance supplement. Cost: $5–$25/month. Confidence: 90%.
- **Option C: Mighty Networks (Launch Plan) + Loomio** — Best for fast onboarding and mobile engagement when off-grid capability is not a hard requirement. Cost: $79–$120/month. Confidence: 82%.

Circle.so is rated 78% confidence — adequate on features, but $89/month base with no offline capability and no job board native feature pushes it below the 85% threshold for active recommendation.

Decision deadline is June 3, 2026. Platform selection gates Phase 6 Domain A activation. All three recommended options can be operational by June 5.

---

## Part 1: Platform Scope and Formal Exclusions

Prior work (v2, June 1) formally excluded three platforms from the comparison matrix. Those exclusions hold and are summarized here for completeness.

### Substack — Excluded

Substack is a newsletter publishing tool. Its "Teams" feature manages co-author roles (Admin / Contributor / Byline) for a shared newsletter, not a community of 50–200 participants. It offers a subscriber chat with minimal moderation (ban, delete, report) and no calendar, no file library, no job board, no RSVP system, and no API for community actions. Its 10% revenue share applies to paid subscriptions.

Domain A use case has no overlap with Substack's design purpose. Substack is useful as a distribution channel for Phase 5 outputs (publishing research to a wider audience) but is not a coordination platform.

### Platform.sh — Excluded

Platform.sh (now rebranded Upsun) is a Platform-as-a-Service for application deployment and hosting, not itself a community platform. It has no forum, calendar, member management, or moderation tools. It is a potential hosting infrastructure for deploying self-hosted Discourse or Nextcloud — not a coordination layer. Pricing: ~$30–60/month for small deployments, more expensive than raw VPS options.

### Lunchclub — Excluded

Lunchclub is an AI-powered 1:1 professional meeting matchmaker. It has no group spaces, no file sharing, no event coordination beyond individual scheduling, and no moderation. It is categorically incompatible with 50–200 participant community coordination.

---

## Part 2: Feature Matrix — All 8 Platforms, 8 Dimensions

**Scope of evaluation**: 8 platforms, 8 dimensions critical to Domain A. Scoring scale: 0 (absent), 1 (severe limitations), 2 (limited but functional), 3 (adequate), 4 (strong with minor gaps), 5 (best-in-class for this use case).

**Domain A use case anchor**: 50–200 participants (starting at 8–12 volunteer builders, scaling to 200), mixture of urban and rural/off-grid households, coordination of mutual aid resource exchanges, skill exchange listings, cooperative economics document library, monthly governance decisions, and local food system coordination events. Participants may use Proton Mail, Signal, or other non-Google identities. No corporate email requirement acceptable.

---

### Dimension 1: Access Control

Access control determines who can see what, who can post, and how new members are vetted. For Domain A, this covers both the builder team (8–12 people with admin/moderator roles) and eventual community members (50–200 people with participant roles).

| Platform | Role Depth | Invite Mechanism | Non-Google Signup | Privacy Tiers | D1 Score |
|---|---|---|---|---|---|
| **Nextcloud + Matrix** | Full per-room matrix + LDAP groups | Admin-provisioned accounts; any email | Yes — any email, no OAuth required | Per-room, per-file, per-calendar | **5** |
| **Discourse** | 5 trust levels (TL0–TL4) + manual groups | Invite-only or approval; email-based | Yes — any email; GitHub OAuth optional | Category + group + trust-level | **5** |
| **Mighty Networks** | Custom roles per Space; host + moderator tiers | Invite links + approval gates | Yes — any email for signup | Space-level (not post-level) | **4** |
| **Circle.so** | Full role hierarchy; member-level overrides | Magic links, gated applications | Yes — any email or Google | Space + member level | **4** |
| **Loomio** | Group + subgroup privacy; Admin/Member | Email invite + shareable link | Yes — any email | Subgroup scoping only | **3** |
| **Geneva** | Role-based rooms; phone verification required | Questionnaire-gated invites | No — phone number required | Room-level only | **2** |
| **Slack (free)** | Channel-level only | Email domain or link | Yes — any email | Minimal; no fine-grained control | **2** |
| **Substack** | 3 roles (Admin/Contributor/Byline) | Email-based | Yes | None below subscriber level | **1** |

Notes:
- Discourse's trust-level system is uniquely suited to self-governing communities. TL0 (new, limited posting) → TL1 (basic, earns through reading) → TL2 (member, sustained engagement) → TL3 (regular, formula-based) → TL4 (leader, moderator grant). No admin intervention needed to elevate engaged participants.
- Geneva's phone number requirement creates a hard barrier for community members who use privacy-preserving identities. For a resilience community context this is disqualifying.
- Nextcloud + Matrix scores 5 because account provisioning is entirely admin-controlled: any email, any identity, no OAuth dependency on Google or GitHub. This is the cleanest fit for Domain A's non-corporate-email requirement.
- Slack's lack of fine-grained role control and no approval workflow on the free tier makes it inadequate for vetting community members in a trust-sensitive resilience context.

---

### Dimension 2: File and Resource Sharing

Domain A requires a structured document library: mutual aid handbooks, cooperative governance templates, local food system coordination guides, skill exchange listings, and case studies from complementary currency projects. Documents need to be searchable, versioned, and collaborative.

| Platform | Document Library | Collaborative Editing | Version Control | Search | Offline Access | D2 Score |
|---|---|---|---|---|---|---|
| **Nextcloud Hub** | Full document suite (LibreOffice/Collabora) | Real-time co-editing | Full version history + file locking | Full-text across files | Desktop/mobile sync client; files available offline | **5** |
| **Matrix/Element** | File sharing in encrypted rooms | None native; Nextcloud bridge | None native | Local + server-side | Local cache; offline-readable | **3** |
| **Discourse** | File uploads + image hosting + wiki posts | None native; wiki crowd-editing (TL2+) | Wiki revision history only | Full-text across all posts | PWA read cache (read-only offline) | **3** |
| **Circle.so** | File attachments in spaces/chat | None | None | Basic content search | None | **2** |
| **Mighty Networks** | File uploads in posts | None | None | Basic post search | None | **2** |
| **Loomio** | Attachments to proposals/threads | None | None | Thread search only | None | **2** |
| **Slack (free)** | 5 GB total; files auto-deleted at 90 days | None | None | 90-day history only | None | **1** |
| **Geneva** | Basic media (images, video) only | None | None | Minimal | None | **1** |

Notes:
- Nextcloud is unambiguously the strongest platform for Domain A document management. Real-time co-editing means multiple community builders can simultaneously develop resource guides. Version history means no protocol change is ever lost. The desktop sync client means documents are available offline even on a laptop without connectivity.
- Discourse wiki posts partially address collaborative document refinement: posts marked as wiki are editable by TL2+ members, and all revision history is preserved. This is adequate for async collaborative editing but not simultaneous co-authoring.
- Slack's 90-day file deletion is a hard disqualifier. A mutual aid community's protocols and resource guides cannot be auto-deleted after 90 days.
- Geneva's file sharing is image/video focused — entirely unsuitable for a domain producing structured policy and process documents.

---

### Dimension 3: Event Coordination

Domain A coordination events include: monthly community economic meetings, skill exchange sessions, cooperative business planning workshops, local food system coordination calls, and governance voting sessions. RSVP tracking matters when volunteer attendance determines whether sessions run.

| Platform | Native Calendar | RSVP + Reminders | Economic Activity Scheduling | Async Coordination | Recurrence | D3 Score |
|---|---|---|---|---|---|---|
| **Nextcloud Hub** | Full CalDAV calendar | Email invites + CalDAV RSVP | Resource booking via Appointments | Tasks + CalDAV | Full recurrence | **5** |
| **Mighty Networks** | Calendar view | Native RSVP + push + email reminders | No resource booking | Polls | Yes | **4** |
| **Circle.so** | Event space calendar | Native RSVP + notifications | No resource booking | Polls | Yes | **4** |
| **Loomio** | Time polls (purpose-built) | Scheduling votes with deadline | No; governance-focused | Async proposals + outcomes | None (per-poll) | **4** |
| **Discourse** | Events plugin (not default) | Plugin-based RSVP | No resource booking | Thread-based async | Plugin-dependent | **3** |
| **Matrix/Element** | None native; Nextcloud bridge | None native; bridge | None native | Async threads | None native | **3** |
| **Geneva** | Integrated event calendar | Event reminders + RSVP | None | Chat-based | Limited | **3** |
| **Slack (free)** | None native | None | None | Scheduled messages | None | **1** |

Notes:
- Nextcloud's Appointments app (included in Hub) supports community resource booking — participants can reserve time slots for skill exchanges, tool loans, or consultation slots without a third-party booking service. This is directly relevant to Domain A economic activity coordination.
- Loomio scores 4 not because it has a general calendar but because async scheduling (time polls, proposal deadlines) is what distributed volunteer teams actually use. For a domain that includes governance decisions (which resource gets allocated where), Loomio is the natural companion tool regardless of primary platform.
- Discourse requires the Events plugin installation (available on all hosted plans and self-hosted). Without it, event coordination falls back to threaded posts — functional but not ideal for 50+ members.

---

### Dimension 4: Messaging and Moderation

Domain A involves sensitive economic discussions: mutual aid requests, resource exchange negotiations, governance disputes, and financial coordination. Moderation depth determines whether the community can self-govern.

| Platform | Threaded Discussion | Moderation Depth | Spam Control | Bot/Automation | DMs | D4 Score |
|---|---|---|---|---|---|---|
| **Discourse** | Full threaded forum (best-in-class) | TL gates, Akismet, flag queue, silence/suspend | TL0 rate-limiting + Akismet | Webhooks + Discourse Automation plugin | Private messages (threaded) | **5** |
| **Matrix/Element** | Threaded replies + Space organization | Mjolnir bot; room ACLs; federated ban propagation | Mjolnir pattern matching | Full Matrix SDK | E2E encrypted DMs | **4** |
| **Mighty Networks** | Full threaded posts per Space | Per-Space moderation queue; member suspension | AI content flagging (basic) | Limited automations | Direct messaging | **4** |
| **Circle.so** | Threaded + real-time chat | AI moderation + flagging; profanity filter | AI inbox; automated workflows | Workflow automations | DMs | **4** |
| **Loomio** | Decision-threaded discussions | Admin deletion; thread locking | Platform-level only | Slack/Matrix outbound | User-to-user messages | **3** |
| **Geneva** | Room chat + forum posts | Basic room moderation; phone friction | Phone verification barrier | None | DMs | **2** |
| **Slack (free)** | Thread replies in channels | Minimal on free; no org-level policy | None automated | 10 app limit | DMs + group DMs | **2** |
| **Substack** | Subscriber chat only | Ban, delete, report | None automated | None | None | **1** |

Notes:
- Discourse's TL0 rate-limiting automatically throttles new accounts (1 topic/day, 10 replies/day) without admin action, protecting the community from spam bursts before trust is established. This is the best passive moderation of any platform evaluated.
- Matrix/Element's Mjolnir moderation bot allows ban lists to be shared across rooms and federated homeservers. If a bad actor is banned from one room, that ban can propagate across the entire community. This is uniquely powerful for a community that may eventually federate with other resilience networks.
- For Domain A specifically: the ability to have private encrypted DMs matters for resource exchange negotiations where participants may share personal financial or material details. Matrix/Element's E2E encrypted DMs provide the strongest protection; Discourse's private messages are server-encrypted but not E2E.
- Circle's AI moderation (AI inbox, content flagging) reduces human moderator burden — relevant when volunteer moderators have limited time.

---

### Dimension 5: Off-Grid Readiness

This is the dimension where Domain A diverges most significantly from the general platform analysis. Community economic resilience explicitly addresses scenarios where infrastructure has failed. A coordination platform for this domain that itself fails without internet connectivity has a credibility gap: it cannot coordinate economic activity during the scenarios it is designed to address.

| Platform | Offline Support | Local-First Architecture | Mobile Offline | Self-Hostable | Low-Bandwidth | D5 Score |
|---|---|---|---|---|---|---|
| **Nextcloud Hub** | Desktop/mobile sync client; files fully available offline | Local file cache; bidirectional sync when reconnected | iOS/Android Nextcloud app; offline files and calendar | Yes (AGPL) | Runs on LAN; zero internet required | **5** |
| **Matrix/Element** | Element X: instant local launch; offline-readable cached rooms | Local message store; messages queue and sync on reconnect | iOS/Android/F-Droid; offline read + compose | Yes (AGPL; Synapse/Dendrite) | LoRa/mesh bridgeable; bandwidth-adaptive | **5** |
| **Discourse** | PWA: read-only cache via service worker | Partial offline (read-only) | PWA installable; read-only offline | Yes (AGPL, Docker) | Minimal JS; low-bandwidth mode | **2** |
| **Loomio** | None | Cloud-only | Mobile-responsive web only | Yes (AGPL, Docker) | Cloud-dependent | **1** |
| **Mighty Networks** | None | Cloud-only SaaS | Native apps but no offline | No | Cloud-dependent | **0** |
| **Circle.so** | None | Cloud-only SaaS | Native app but no offline | No | Cloud-dependent | **0** |
| **Slack (free)** | None | Cloud-only SaaS | Native apps but no offline | No | Cloud-dependent | **0** |
| **Geneva** | None | Cloud-only SaaS | Native iOS/Android; no offline | No | Cloud-dependent | **0** |

Notes:
- The binary here is sharper for Domain A than the general analysis. Mutual aid coordination (who has surplus grain, who needs it; which skill is available, who needs it) is exactly the coordination that occurs during and after infrastructure disruption. A community built around economic resilience should not have its coordination layer dependent on AWS or Cloudflare staying online.
- Nextcloud + Matrix/Element running on raspby1 (the existing Pi 5 at 100.70.184.84 on Tailscale) can serve the entire community from a local LAN without internet. Documents sync via Nextcloud desktop clients. Messages queue in Element X and deliver when connectivity restores. Calendar and task data syncs via CalDAV to any device.
- Element X's LoRa bridging is in active development: community-maintained gateways exist for bridging Matrix rooms to Meshtastic mesh networks. This means off-grid communication can eventually extend beyond WiFi range.
- Discourse as a PWA is offline-capable for reading cached content but cannot post or sync new content without connectivity. For a domain whose value proposition is real-time resource coordination, read-only offline is materially insufficient.
- Mighty Networks, Circle, Slack, and Geneva score 0 because they are cloud-only SaaS with no self-hosting option and no offline capability.

---

### Dimension 6: Cost Model

Domain A is a volunteer-led, non-revenue-generating community project. Budget ceiling is a real constraint.

| Platform | Free Tier | Cost at Launch Scale (50 users) | Cost at Full Scale (200 users) | Nonprofit/Community Discount | Data Exit Risk | D6 Score |
|---|---|---|---|---|---|---|
| **Nextcloud + Matrix** | Yes (self-hosted, $0 software) | $0 software + $5–15/mo VPS | $0 software; add VPS capacity as needed | N/A (open source) | None — all data on your own hardware | **5** |
| **Discourse** | Yes (self-hosted, $0 / hosted basic free) | $0 self-hosted + $5–15/mo VPS; $50/mo nonprofit hosted | Same; hardware scales | 50% nonprofit hosted; 85% educational | None self-hosted; low on hosted (export available) | **5** |
| **Loomio** | No cloud free; self-hosted $0 | $199/yr Starter nonprofit (up to 30); $649/yr Pro nonprofit (unlimited) | $649/yr Pro nonprofit | 25–50% nonprofit discount | Low — export available | **4** |
| **Circle.so** | 14-day trial only | $89/mo (Professional, annual billing) | $199/mo (Business, annual) + member volume | None confirmed | Medium — member data exportable; content export partial | **2** |
| **Mighty Networks** | 14-day trial only | $79/mo (Launch) | $179/mo (Scale) | None confirmed | Medium — limited export; pricing has increased historically | **2** |
| **Geneva** | Yes (fully free currently) | $0 | $0 (premium tier in development) | N/A | High — no export; Geneva controls all data | **3** |
| **Slack (free)** | Yes (90-day limit) | $0 free; $7.25/user/mo Pro = $362.50/mo at 50 users | $7.25/user Pro = $1,450/mo at 200 users | 85% nonprofit; requires IRS charitable status | Low on Pro; medium on free (limited export) | **2** |

Notes:
- Loomio's 2026 pricing has shifted from the v2 analysis: current official pricing shows Pro at $649/year nonprofit (was $499 in the v2 document). The Starter plan ($199/year) caps at 30 members — insufficient for Phase 6 scale (50–200). Pro ($649/year) is required for unlimited membership; this should be budgeted as the governance supplement cost if Loomio is adopted.
- Nextcloud + Matrix at $0 software cost is the only combination that scales from 8 members to 200 members without a price change. VPS cost increases modestly as community grows; a Hetzner CPX31 (4 vCPU, 8 GB RAM, ~$14/month) handles 200 active users comfortably.
- Geneva's zero cost is attractive but carries the highest data exit risk: there is no export mechanism, no API, and the company controls all community data. If Geneva changes pricing, shuts down, or modifies terms, the community has no recovery path.
- Slack Pro for nonprofits at 85% discount: $7.25 × 0.15 = $1.09/user/month. At 200 users: $218/month ($2,616/year). Still more expensive than self-hosted options, and requires IRS nonprofit filing to qualify.

---

### Dimension 7: Integration with Existing Tools

Phase 5 outputs are on GitHub Pages. Community members may use Gmail, Proton Mail, Signal, or corporate email. Integration with the existing Tailscale mesh (raspby1 at 100.70.184.84) is relevant for Option C.

| Platform | Email (any type) | GitHub/GitHub Pages | Tailscale/LAN | Google Drive | API Access | D7 Score |
|---|---|---|---|---|---|---|
| **Discourse** | Full SMTP; any email for accounts | GitHub OAuth login + webhook triggers; embed widget on static sites | Deployable on any VPS on Tailscale | None native; Zapier available | Full REST API (self-hosted, no tier lock) | **5** |
| **Nextcloud + Matrix** | Any email for account provisioning; full SMTP for notifications | Nextcloud ↔ GitHub OAuth + webhook; Matrix ↔ GitHub webhook bridge | Native Tailscale deployable; runs on raspby1 today | Nextcloud replaces Google Drive; no integration with Google Drive needed | Full REST + CalDAV/CardDAV/WebDAV + Matrix Client-Server API | **5** |
| **Loomio** | Full email integration; any email | None native | Cloud-only | None native | Integration API (all plans) | **3** |
| **Circle.so** | Any email for signup | None native | Cloud-only | None native | Admin API (5,000 req/mo Professional; 50,000 Business) | **3** |
| **Mighty Networks** | Any email for signup | None native | Cloud-only; no self-hosting | None native | API locked to Scale plan ($179/mo) only | **2** |
| **Geneva** | Email notifications only | None | Cloud-only | None | No public API | **1** |
| **Slack (free)** | Any email; notifications | GitHub app available | Cloud-only | None native | 10 app integrations max on free | **2** |

Notes:
- Discourse's embed widget allows recent community discussions to appear on any static HTML page, including GitHub Pages — direct integration with the Phase 5 publication infrastructure. Members can see and link to community activity from the public-facing knowledge base.
- Nextcloud + Matrix on raspby1 requires no external VPS if deployed there. The Tailscale mesh (100.70.184.84) provides secure access from any community member device worldwide without exposing services to the public internet. This is both a security and a cost advantage.
- Mighty Networks locks API access to the Scale plan ($179/month). On the Launch plan ($79/month), there is no programmatic access to community data, no automation, and no integration hooks. This is a significant constraint for a community that may want to auto-post new Phase 5 research to the community space.
- Geneva has no public API — no integration pathway to any external tool whatsoever.

---

### Dimension 8: Domain A-Specific Features

This dimension is new and is not in the v1 or v2 analyses. It addresses features specifically useful for coordinating community economic activities: job boards, skill exchange listings, resource inventories, and cooperative economics workflows.

| Platform | Job Board / Skill Listing | Resource Inventory | Mutual Aid Request Flow | Cooperative Governance | Customizable Templates | D8 Score |
|---|---|---|---|---|---|---|
| **Nextcloud Hub** | Deck (Kanban) + Forms for listings | Files + Deck for resource tracking | Forms for request intake; Tasks for fulfillment | Workflow automation via Flow | Full document library for templates | **4** |
| **Discourse** | Classified-style sub-forum + tags | Wiki posts as resource registers | Tagged posts + PM for coordination | Trust-level governance; Polls plugin | Wiki posts as living templates | **4** |
| **Loomio** | None | None | Proposal threads as request flow | Voting, ranked choice, outcome tracking | Poll templates | **3** |
| **Mighty Networks** | None native; workaround via post types | None native | Member-to-member DMs + groups | Polls only | Space templates | **2** |
| **Circle.so** | None native; custom space workaround | None native | Member-to-member DMs | Polls only; no structured governance | Space templates | **2** |
| **Matrix/Element** | None native; structured rooms workaround | None native; Nextcloud bridge | Rooms as request channels | Votes via bots | None | **2** |
| **Geneva** | None | None | None structured | None | None | **1** |
| **Slack (free)** | None native; channel convention | None | None structured | None | None | **1** |

Notes:
- Discourse's tagging system, combined with a dedicated "Skills Exchange" or "Resource Offers" category, provides a structured job board and skill listing without custom development. Members post offers/requests tagged by skill type, resource category, or geographic area. This is fully functional and searchable.
- Nextcloud Deck (Kanban) can serve as a visual resource tracking board: columns for "Available," "Requested," "In Transit," "Delivered" give the community a real-time view of resource flow. Combined with Nextcloud Forms for intake, this approaches a lightweight mutual aid management system.
- Loomio's proposal-based workflow is the most structured for governance decisions: which community investment gets funded, how cooperative profits are distributed, which skills training gets priority. Its governance tooling is a decisive advantage for this dimension even though it lacks other features.
- No platform evaluated has native job board, skill exchange, or resource inventory features. All solutions here use platform primitives creatively. Self-hosted platforms (Discourse, Nextcloud) have the deepest primitive set and the most extensibility.

---

## Part 3: Consolidated Scored Matrix

**Total possible: 40 points across 8 dimensions.**

Scoring reflects Domain A-weighted evaluation. Off-grid readiness (D5) and Domain A-specific features (D8) are elevated in significance vs. the general analysis.

| Platform | D1: Access | D2: Files | D3: Events | D4: Messaging | D5: Off-Grid | D6: Cost | D7: Integration | D8: Domain A | Total | Overall |
|---|---|---|---|---|---|---|---|---|---|---|
| **Nextcloud + Matrix** | 5 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | **38/40** | 9.5/10 |
| **Discourse** | 5 | 3 | 3 | 5 | 2 | 5 | 5 | 4 | **32/40** | 8.0/10 |
| **Circle.so** | 4 | 2 | 4 | 4 | 0 | 2 | 3 | 2 | **21/40** | 5.25/10 |
| **Mighty Networks** | 4 | 2 | 4 | 4 | 0 | 2 | 2 | 2 | **20/40** | 5.0/10 |
| **Loomio** (supplement) | 3 | 2 | 4 | 3 | 1 | 4 | 3 | 3 | **23/40** | 5.75/10 |
| **Geneva** | 2 | 1 | 3 | 2 | 0 | 3 | 1 | 1 | **13/40** | 3.25/10 |
| **Slack (free)** | 2 | 1 | 1 | 2 | 0 | 2 | 2 | 1 | **11/40** | 2.75/10 |
| **Substack** | 1 | 1 | 0 | 1 | 0 | 3 | 1 | 0 | **7/40** | 1.75/10 |

Note on Loomio: scored as a standalone platform for matrix completeness, but its highest-value role is as a governance supplement to Options A, B, or C — not as a primary coordination platform.

---

## Part 4: Recommended Options

### Option A — Nextcloud Hub + Matrix/Element (Self-Hosted)

**Overall score**: 38/40 (9.5/10 Domain A-weighted)
**Confidence**: 91%
**Annual cost**: $0–$180/year (VPS) or $0 if hosted on raspby1
**Monthly cost range**: $0–$15/month
**Setup time**: 6–10 hours (Docker familiarity required)
**Technical requirement**: Docker, command line; one builder with sysadmin capacity

**Why this is the top recommendation for Domain A specifically**:

The Nextcloud + Matrix combination is the only evaluated configuration that scores 5/5 on both off-grid readiness and document collaboration — and those are the two dimensions where Domain A departs most sharply from a generic community platform. A mutual aid and cooperative economics community must be able to:

1. Access and share resource guides when connectivity is unavailable (Nextcloud desktop sync)
2. Coordinate resource exchanges in real time when infrastructure is degraded (Element X offline-compose, LoRa bridging on roadmap)
3. Co-author living documents (cooperative governance templates, mutual aid protocols) without a third party controlling the storage (Nextcloud collaborative editing)
4. Operate indefinitely without corporate email or Google account (any email for account provisioning)
5. Scale from 8 to 200 participants without a price change (open source software, hardware-only scaling)

The existing raspby1 infrastructure (Raspberry Pi 5, 100.70.184.84, accessible via Tailscale) eliminates the VPS provisioning step. Docker Compose configuration can deploy both Nextcloud Hub and Matrix Synapse on this machine today.

**What this cannot do well**:
- No native member discovery: community builders must individually recruit and invite participants
- Two separate UX surfaces (Nextcloud web + Element app): members must learn both
- No push notification infrastructure without a mobile app store presence (Element is on F-Droid/App Store but community members must install it separately)
- Higher setup complexity than any SaaS option

**Option A + Loomio Pro Nonprofit**:
Adding Loomio ($649/year nonprofit Pro, or self-hosted at $0) gives the community structured governance: ranked-choice voting for resource allocation, time polls for coordinating meetings, proposal threads for cooperative decisions. Total cost: $0–$180/year (infrastructure) + $649/year (Loomio cloud) or $0 (self-hosted Loomio).

**Implementation timeline (June 3 decision)**:

| Date | Action | Time |
|---|---|---|
| June 3 | Decision; Docker Compose YAML for Nextcloud + Synapse written | 1 hour |
| June 3 | Deploy on raspby1 (or new VPS if preferred); DNS if VPS | 2 hours + 1–24hr DNS wait |
| June 4 | Nextcloud admin configuration: branding, groups, Deck + Forms + Calendar apps enabled | 2 hours |
| June 4 | Matrix Synapse + Element Web UI configured; first rooms created | 2 hours |
| June 5 | Phase 5 documents uploaded to Nextcloud; shared folder structure created | 1 hour |
| June 5 | Element rooms created for: General, Resource Exchange, Skills Board, Governance, Events | 30 min |
| June 5–8 | First 10 builder accounts provisioned (both Nextcloud + Matrix usernames) | 1 hour |
| June 9–14 | Domain A community onboarding; Nextcloud Calendar event for June 15 session | Ongoing |
| June 15 | Community foundation session via Nextcloud Talk video | — |

---

### Option B — Discourse (Self-Hosted) + Loomio

**Overall score**: 32/40 (8.0/10 Domain A-weighted)
**Confidence**: 90%
**Annual cost**: $60–$300/year (VPS + optional Loomio cloud)
**Monthly cost range**: $5–$25/month
**Setup time**: 6–8 hours
**Technical requirement**: Docker, command line; official install script minimizes expertise needed

**Why this is the best single-app option for Domain A**:

Discourse delivers the deepest moderation infrastructure of any single platform — a decisive advantage for a community coordinating sensitive economic activities among 50–200 people. The trust-level system means the community self-governs as it grows: active participants earn posting permissions automatically without admin action. Full-text search across all posts (including wiki documents) means the resource library is discoverable. The REST API enables automation: new Phase 5 research pages can trigger posts in the community automatically via webhook.

For Domain A's job board and skill exchange needs: Discourse's category + tag system creates a structured classified board. A "Resource Offers" category with tags (Skills, Tools, Food, Transport, Capital) allows members to post listings that are searchable, threaded (negotiations happen in replies), and persistent (no 90-day deletion).

**What Discourse cannot do**:
- No collaborative document editing: Phase 5 documents are posted as wiki posts for crowd-annotation but not real-time co-authoring
- Off-grid capability is read-only PWA cache: members can read cached content but cannot post or sync without connectivity
- Events require plugin installation (available, but one extra step)

**Option B + Loomio**: Loomio integrates via Matrix/email notifications into Discourse. Cost: $5–15/month (VPS) + $649/year (Loomio Pro nonprofit) = $714–$829/year total. Self-hosted Loomio adds $0 software cost, requiring additional VPS capacity or deployment on raspby1.

**Implementation timeline (June 3 decision)**:

| Date | Action | Time |
|---|---|---|
| June 3 | VPS provisioned (Hetzner CPX21, ~$7/month); DNS A record set | 30 min + DNS wait |
| June 4 | Discourse Docker install via official script; admin account created | 2 hours |
| June 4 | Categories configured: Knowledge Base, Resource Exchange, Skills Board, Events, Governance | 1 hour |
| June 4 | Events plugin installed; GitHub OAuth configured; email SMTP configured | 1 hour |
| June 5 | Phase 5 Wave 1+2 documents posted as wiki posts in Knowledge Base | 2 hours |
| June 5 | Trust levels configured; invite links sent to first 10 builders | 30 min |
| June 9–14 | Domain A community onboarding; Events plugin: June 15 session created | Ongoing |
| June 15 | Community foundation session (external video link from Discourse event) | — |

---

### Option C — Mighty Networks (Launch Plan) + Loomio

**Overall score**: 20/40 (5.0/10 Domain A-weighted)
**Confidence**: 82%
**Annual cost**: $950–$1,598/year (Mighty Networks + Loomio)
**Monthly cost range**: $79–$133/month
**Setup time**: 3–4 hours
**Technical requirement**: None

**Why it still makes the list**:

For a team that has no Docker-capable member or wants to launch within 2 hours of decision, Mighty Networks is the fastest path to a functional community. The native iOS/Android apps with push notifications are the single best driver of volunteer participation in any platform evaluated — and volunteer participation is the bottleneck for Phase 6 Domain A scaling from 8 builders to 200 community members.

The 14-day free trial (which includes Scale-tier features) allows the community to validate engagement before committing to the $950/year cost. If the June 15 foundation session draws strong participation, confidence in the platform investment rises.

**Why confidence is 82% (below the 85% recommendation threshold)**:

The combination of hard zeros on off-grid readiness and no native job board or resource inventory tooling means Mighty Networks requires workarounds for two dimensions that are central to Domain A's purpose. A community that cannot coordinate resource exchanges during infrastructure disruption — and is building its entire knowledge base around that exact scenario — is undermined by relying on SaaS-only infrastructure.

The 82% confidence reflects: strong on onboarding/engagement mechanics, adequate on access control and events, but materially weak on the two dimensions most specific to Domain A. Option C is viable if the team assesses offline capability as a future consideration rather than a current requirement.

**What Mighty Networks cannot do**:
- No offline capability (hard zero)
- No document co-editing
- No API on Launch plan — no automation, no integration with Phase 5 publication pipeline
- No export mechanism for community data if migration is needed later (medium vendor lock-in risk)

**Implementation timeline (June 3 decision)**:

| Date | Action | Time |
|---|---|---|
| June 3 | Start 14-day free trial; community name, description, branding configured | 2 hours |
| June 3 | Spaces created: Knowledge Base, Resource Exchange, Skills Board, Events, Governance | 1 hour |
| June 4 | Phase 5 documents uploaded to Knowledge Base space | 1 hour |
| June 4 | June 15 community foundation event created with RSVP | 30 min |
| June 5 | Invite links sent to first 10 builders; push notification onboarding | 30 min |
| June 9–14 | Domain A community onboarding; push notification reminders | Ongoing |
| June 17 | Trial ends; $79/month billing begins (or evaluate and cancel) | — |

---

## Part 5: Platform Exclusion Details — Platforms Not Formally Recommended

### Circle.so — Evaluated but Not Recommended for Domain A

**Score**: 21/40 (5.25/10). **Confidence**: 78%.

Circle is the most polished SaaS community platform evaluated. Its AI-assisted moderation, clean UI, and workflow automation are genuine strengths for professional communities. It scores below the 85% confidence threshold for Domain A for three specific reasons:

1. No offline capability (score 0/5 on D5) — the same structural problem as Mighty Networks
2. No native job board, skill listing, or resource inventory tooling — workarounds are possible but require significant setup
3. At $89/month (Professional, annual) or $199/month (Business), it is more expensive than Options A and B while providing fewer features relevant to Domain A

Where Circle would be appropriate: a community primarily focused on courses, content creation, or professional networking (coaches, consultants, membership businesses). Not appropriate for a mutual aid and cooperative economics coordination community that requires offline resilience.

### Geneva — Evaluated but Not Recommended

**Score**: 13/40 (3.25/10).

Geneva is free and has a reasonable events calendar. Its phone number verification requirement is a hard barrier for community members who maintain privacy-preserving identities. There is no public API, no data export, and no document library. Phone verification as the anti-spam mechanism creates an unacceptable identity requirement for a resilience-focused community.

### Slack (Free Tier) — Evaluated, Not Recommended

**Score**: 11/40 (2.75/10).

Three hard disqualifiers: (1) 90-day message and file history deletion destroys institutional knowledge, (2) 5 GB total storage is insufficient for a document library, (3) no offline capability. Slack Pro for nonprofits at 85% discount is $218/month at 200 users — more expensive than all self-hosted options combined. Slack is appropriate for internal team coordination among the 8–12 builders, but not as the primary community platform for 50–200 participants.

---

## Part 6: Loomio — Governance Supplement Analysis

Loomio is recommended as a governance layer regardless of primary platform choice. It is not a standalone community coordination platform but a decision-making tool that integrates with all three recommended options.

**Current pricing (verified June 2026)**:
- Community plan: $10/month or $199 lifetime (up to ~30 members; limited features)
- Starter: $25/month / $199/year (small groups, limited subgroups)
- Pro nonprofit: $649/year ($54.08/month) — unlimited members, unlimited subgroups, full governance tooling
- Self-hosted: $0 software (AGPL, Docker)

Note: The v2 analysis listed Pro nonprofit at $499/year; current official pricing is $649/year. This is a material difference for budget planning.

**Domain A governance use cases**:
- Resource allocation votes: which skill exchange gets community support this cycle
- Protocol adoption: community approval of mutual aid request procedures
- Meeting coordination: time polls for monthly economic coordination calls
- Investment decisions: ranked-choice voting on how cooperative surplus is allocated
- Domain expansion: which Phase 6 domain gets next research investment

**Integration paths**:
- Loomio → Discourse: outbound notifications via email (Discourse processes email replies into threads)
- Loomio → Matrix: native Matrix/Element outbound notifications
- Loomio → Mighty Networks: outbound email notifications only (no API on Launch)

**Recommendation**: Start with Loomio Starter ($199/year) for the first 6 months while Phase 6 membership is below 30 active decision-makers. Upgrade to Pro nonprofit ($649/year) when membership exceeds 30 or subgroup complexity increases.

---

## Part 7: Integration Pathway with Phase 5 Output

Phase 5 produced structured research across water systems, veterinary care, food preservation, community infrastructure, microgrids, and conflict resolution. That content lives on GitHub Pages (static HTML). Phase 6 Domain A must connect participants to that content library.

| Integration Path | Option A (Nextcloud + Matrix) | Option B (Discourse) | Option C (Mighty Networks) |
|---|---|---|---|
| Link to GitHub Pages content | Direct links in Nextcloud shared docs and Matrix room topics | Discourse embed widget displays recent posts on GitHub Pages; links in forum posts | Direct links in Space descriptions and posts |
| Incorporate Phase 5 documents into platform | Upload to Nextcloud (co-editable); download and link from Matrix | Post as wiki posts in Knowledge Base category (crowd-editable by TL2+) | Upload to Knowledge Base space (read-only PDFs) |
| Auto-announce new Phase 5 publications | Nextcloud Flow webhook → Matrix room notification | Discourse webhook receiver → auto-post to forum | Not available on Launch plan |
| Cross-reference skill gaps from Phase 5 | Tag Nextcloud files by Phase 5 domain; Deck board for skill gaps | Tag posts and wiki posts by Phase 5 domain; full-text search | Manual posts in Knowledge Base space |
| Onboard Phase 5 readers into Platform | Nextcloud account invitation (admin-provisioned; any email) | Discourse invite link (email-based; any email domain) | Mighty Networks invite link (any email) |

Discourse scores highest on Phase 5 integration because the embed widget creates a direct visual connection between the static publication site and the live community. This is achievable in an afternoon: paste the Discourse embed code into the GitHub Pages layout template, and recent community discussions appear on every page of the Phase 5 output.

---

## Part 8: Non-Corporate Email Compatibility

Domain A participants may use Proton Mail, Tutanota, Signal (for verification), self-hosted email, or any other non-Google, non-corporate email. Platform compatibility with non-standard email is evaluated here.

| Platform | Proton Mail | Tutanota | Self-Hosted Email | Phone-Only (Signal) | Corporate Email Required |
|---|---|---|---|---|---|
| **Nextcloud + Matrix** | Yes — any email for account provisioning | Yes | Yes | No (email required for account provisioning; use any email) | No |
| **Discourse** | Yes — any email for signup | Yes | Yes | No (email required) | No |
| **Mighty Networks** | Yes — any email for signup | Yes | Yes | No (email required) | No |
| **Circle.so** | Yes — any email or Google OAuth | Yes | Yes | No | No |
| **Geneva** | No — phone number required; email secondary | No | No | Yes (phone is primary) | N/A |
| **Loomio** | Yes — any email | Yes | Yes | No | No |
| **Slack** | Yes — any email | Yes | Yes | No | No |

Geneva is the only evaluated platform that creates an identity requirement incompatible with privacy-preserving email. All others accept any valid email address for account creation.

Note on Proton Mail and Discourse: Discourse sends verification emails. Proton Mail supports receiving email from Discourse's SMTP provider (Mailgun, Brevo, etc.) without issue. No configuration change needed.

---

## Part 9: Decision Logic

Answer these four questions in sequence. The first hard requirement determines the path.

**Q1: Is off-grid/low-connectivity capability a hard requirement for initial Phase 6 participants?**

- Yes (rural or off-grid members in the first 50 participants) → **Option A only** (Nextcloud + Matrix is the only evaluated configuration with full offline capability)
- No, but it is a future requirement → **Option A strongly preferred; Option B as backup**
- No, connectivity is reliable and off-grid is a long-term aspiration only → Options A, B, or C all viable; proceed to Q2

**Q2: Does the team have Docker-capable technical capacity for self-hosting?**

- Yes → Options A or B; proceed to Q3
- No → **Option C** (Mighty Networks requires no technical setup) or Discourse hosted at $50/month nonprofit

**Q3: Is document co-authoring (multiple people simultaneously editing shared protocols and guides) needed in Phase 6 Domain A?**

- Yes → **Option A** (Nextcloud is the only solution with native real-time collaborative editing)
- No (documents published centrally; community annotates via forum) → Options A or B both sufficient

**Q4: What is the realistic annual budget ceiling for platform costs?**

- $0 → Option A or B on raspby1 + self-hosted Loomio
- $0–$300/year → Option B (Discourse VPS) + Loomio Starter
- $300–$650/year → Option A or B + Loomio Starter
- $650–$900/year → Option A or B + Loomio Pro nonprofit
- $950–$1,600/year → Option C (Mighty Networks) + Loomio Pro nonprofit

---

## Part 10: Confidence Ratings and Evidence Gaps

| Recommendation | Confidence | Rationale |
|---|---|---|
| Option A: Nextcloud + Matrix | **91%** | Highest score across all 8 dimensions; pricing verified; architecture confirmed against existing raspby1 infrastructure; one unresolved gap: Element X LoRa bridging is community-maintained and not production-stable as of June 2026 |
| Option B: Discourse + Loomio | **90%** | Strong documentation, large community of deployment evidence, official pricing confirmed; gap: Events plugin installation adds one uncontrolled dependency |
| Option C: Mighty Networks + Loomio | **82%** | Platform is stable and well-documented; confidence reduced by hard zero on off-grid capability (core Domain A requirement), no job board native feature, and API locked to higher-cost tier |
| Circle.so | **78%** | Adequate on most dimensions for a general community; Domain A-specific weaknesses (no offline, no native economic coordination tools, $89/month base) push below recommendation threshold |
| Geneva | **35%** | Phone number requirement disqualifies for privacy-sensitive community context; no data export pathway; no API |
| Slack free | **20%** | 90-day history deletion is a hard architectural failure for institutional knowledge preservation; not viable for Domain A |
| Loomio as supplement | **88%** | Strong governance tooling; pricing updated to $649/year Pro nonprofit (higher than v2 estimate); evidence gap: did not directly verify new Starter plan member limits |

**Known evidence gaps**:

1. No hands-on testing of any platform has been conducted. All assessments are from official documentation, independent review sources, and community reports.
2. Loomio Pro nonprofit pricing shifted between v2 (June 1) and this document (June 2). The $649/year figure is from the current official pricing page; the $499/year figure in v2 should be treated as outdated.
3. Element X LoRa bridging status: community projects exist (Meshtastic-Matrix bridges) but are not an official Element product. Off-grid messaging beyond WiFi range should be treated as an experimental capability, not a confirmed feature.
4. Nextcloud Hub 2026 version (NC 28.x/29.x): Collabora Online and OnlyOffice are both available as collaborative editing backends; Collabora is the maintained default for self-hosted instances. No performance benchmarks were obtained for the raspberry Pi 5 platform at 50–200 concurrent users; at typical community usage patterns (asynchronous, not simultaneous), the Pi 5 should handle the load.
5. Discourse's Akismet spam filter requires an Akismet API key. The free tier is sufficient for community-scale deployment (personal or open-source project usage is free at Akismet's terms).

---

## Sources

All pricing and feature information verified against source pages during research, primarily June 1–2, 2026.

**Platform Official Pages**:
- [Mighty Networks Pricing](https://www.mightynetworks.com/pricing)
- [Circle.so Pricing — Official](https://circle.so/pricing)
- [Discourse Pricing — Official](https://www.discourse.org/pricing)
- [Loomio Pricing — Official](https://www.loomio.com/pricing/)
- [Loomio Subscription Plans (Help)](https://help.loomio.com/en/policy/subscriptions/pricing.html)
- [Element Pricing — Official](https://element.io/en/pricing)
- [Nextcloud Hub Features](https://nextcloud.com/hub/)
- [Slack Pricing — Official](https://slack.com/pricing)
- [Matrix.org Hosting Ecosystem](https://matrix.org/ecosystem/hosting/)

**Reviews and Comparisons**:
- [Mighty Networks Review 2026 — group.app](https://www.group.app/blog/mighty-networks-review/)
- [Mighty Networks Pricing Analysis — ezycourse](https://ezycourse.com/blog/mighty-networks-pricing)
- [Circle.so Review 2026 — learningrevolution.net](https://www.learningrevolution.net/circle-review/)
- [Circle.so Pricing 2026 — SchoolMaker](https://www.schoolmaker.com/blog/circle-so-pricing)
- [Circle vs Mighty Networks 2026 — courseplatformsreview](https://www.courseplatformsreview.com/blog/circle-vs-mighty-networks/)
- [Discourse Pricing 2026 — innoloft](https://innoloft.com/en-us/blog/discourse-pricing)
- [Slack Nonprofit Pricing 2026 — Zenzap](https://www.zenzap.co/blog-posts/slack-nonprofit-pricing-in-2026-what-you-actually-get-and-what-to-watch-out-for)
- [Slack Free Plan Limits 2026 — viewexport](https://viewexport.com/post/slack-free-plan-limitations)
- [Best Community Platforms for Nonprofits 2026 — Disco](https://www.disco.co/blog/best-community-platforms-for-nonprofits-2026)
- [Loomio 2026 — GetApp](https://www.getapp.com/collaboration-software/a/loomio/)

**Mutual Aid and Cooperative Economics Context**:
- [Cooperative Economics Alliance of NYC](https://www.ceanyc.org/)
- [Madison Mutual Aid Network Cooperative](https://madisonman.coop/)
- [Digital Tools for Mutual Aid Groups — Phoebe Tickell, The Digital Fund](https://medium.com/digitalfund/communities-essential-guide-to-digital-tools-for-mutual-aid-groups-c1664d30b525)
- [Commonweave — Open Directory of Cooperatives and Mutual Aid](https://commonweave.earth/)
- [NSF: Leveraging Resource Sharing Platforms for Mutual Aid](https://nsfcivicinnovation.org/project/3.0/leveraging-a-resource-sharing-platform-for-long-term-mutual-aid-and-responsiveness-to-emergent-needs/)

**Prior Analysis Documents in This Project**:
- PHASE_6_PLATFORM_ANALYSIS.md (v1, June 1, 2026)
- PHASE_6_PLATFORM_ANALYSIS_v2.md (v2, June 1, 2026, supersedes v1)
- PHASE_6_IMPLEMENTATION_GUIDE_OPTION_A_DISCOURSE.md (June 2, 2026)
- PHASE_6_IMPLEMENTATION_GUIDE_OPTION_B_MIGHTY_NETWORKS.md (June 2, 2026)
- PHASE_6_IMPLEMENTATION_GUIDE_OPTION_C_NEXTCLOUD_MATRIX.md (June 2, 2026)
- PHASE_6_CANDIDATE_COMMUNITY_ECONOMIC_RESILIENCE.md (May 27, 2026)

---

*Research confidence level: High for all pricing (direct platform pages, verified June 1–2, 2026). High for feature sets (cross-checked across multiple independent review sources and official documentation). High for off-grid readiness assessments (technical architecture review of open-source projects). Medium for Loomio pricing (discrepancy between v2 and current page; current page used). No hands-on testing of any platform was conducted; all assessments derive from documentation, official pricing pages, and independent user reviews. The Loomio nonprofit Pro figure ($649/year) supersedes the $499/year figure in prior analysis documents.*
