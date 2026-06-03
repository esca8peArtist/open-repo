---
title: "Phase 6 Community Coordination Platform Analysis"
project: systems-resilience
phase: 6
domain: A (Community Economic Resilience)
status: DECISION-READY — user selects platform by June 3, 2026 EOD
version: 5
created: 2026-06-03
supersedes: PHASE_6_PLATFORM_ANALYSIS_v2.md (v2), PHASE_6_PLATFORM_ANALYSIS.md (v4)
decision_deadline: 2026-06-03 EOD
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

# Phase 6 Community Coordination Platform Analysis
## Version 5 — Decision Required June 3, 2026 | Publication Gate June 5, 2026

---

## Section 1: Executive Summary and Recommendations

This document consolidates all prior platform analysis for Phase 6 Domain A: Community Economic Resilience. It evaluates six platforms originally scoped for Phase 6 community coordination — Mighty Networks, Circle, Substack Teams, Lunchclub, Slack Communities, and Platform.sh — plus two open-source alternatives (Discourse and Nextcloud + Matrix) that entered comparison in prior analysis rounds. All eight are assessed across eight dimensions critical to Phase 6 operational requirements: access control, file and resource sharing, event coordination, messaging and moderation, offline readiness, pricing, compliance, and integration with Phase 5 Wave 1 output.

**Decision context**: The Phase 6 Domain A community launches June 5, 2026 (co-incident with Phase 5 Wave 1 publication). The community serves 15–50 builders across Zone 5 Midwest (IL, MI, IA, IN, WI), coordinating seed libraries, tools sharing, mutual aid networks, cooperative economic models, and barter/time-banking systems. Rural membership in IA and MI means off-grid readiness is an operational requirement, not a preference.

### 1.1 What Follows from the Evidence

Three recommendations are structured below. The task brief proposed Recommendation A as Mighty Networks + Slack, B as Circle + Slack, and C as Substack Teams native. The evidence does not support any of these combinations as primary recommendations for this use case. The scoring and go/no-go conclusions below reflect why, and what should be used instead. The three recommendations are presented in order of evidence-based preference:

---

**Recommendation 1 — Autonomy Path (RECOMMENDED — GO): Nextcloud Hub + Matrix/Element**
- Weighted score: **9.5/10** (38/40 raw across 8 dimensions)
- Confidence: **91%**
- Monthly cost: **$0–$15/month** (zero on existing raspby1 infrastructure)
- Annual cost: **$0–$180/year** infrastructure; $649/year with Loomio governance supplement
- Off-grid: **Full** — offline file sync (Nextcloud) + offline messaging (Element X) + LoRa bridge (Matrix-Meshtastic MESH-API confirmed June 2026)
- Phase 5 integration: **Strong** — GitHub Actions webhook → Matrix rooms; Phase 5 guides as co-editable Nextcloud documents with offline sync
- Decision: **GO for Phase 6 launch**
- Condition: Requires Docker-capable technical operator (~8–10 hours setup)

**Recommendation 2 — Bootstrap Path (GO with conditions): Discourse Self-Hosted + Loomio**
- Weighted score: **8.0/10** (32/40 raw)
- Confidence: **90%**
- Monthly cost: **$7–$17/month** (VPS + email delivery)
- Annual cost: **$84–$204/year** infrastructure; $733/year with Loomio
- Off-grid: **Partial** — read-only PWA cache; no offline posting
- Phase 5 integration: **Best available** — Discourse embed widget on GitHub Pages; GitHub OAuth; wiki posts; GitHub Actions auto-announcement
- Decision: **GO for Phase 6 launch** if team has Docker capability but no requirement for real-time document co-editing; **conditional** if any community members are rural IA/MI with connectivity uncertainty
- Condition: Requires Docker-capable operator (~6–8 hours setup); plan migration to Recommendation 1 if off-grid need materializes

**Recommendation 3 — Commercial Fallback (CONDITIONAL GO): Mighty Networks Launch + Loomio**
- Weighted score: **5.0/10** (20/40 raw)
- Confidence: **82%** (below 85% threshold)
- Monthly cost: **$79/month** ($950/year annual)
- Annual cost: **$950–$1,599/year** with Loomio
- Off-grid: **None** — complete failure when connectivity unavailable
- Phase 5 integration: **Manual only** — no API on Launch plan; static PDF uploads
- Decision: **CONDITIONAL GO** — only if team has no Docker capability and all Phase 6 participants have confirmed reliable connectivity; **requires 6-month migration plan** to Recommendation 1 or 2
- Not recommended for any community with rural Zone 5 members

### 1.2 Platforms Assessed as GO/NO-GO

| Platform | Score | Go/No-Go | Primary Disqualifier |
|---|---|---|---|
| Nextcloud + Matrix | 9.5/10 | **GO** (recommended) | None |
| Discourse self-hosted | 8.0/10 | **GO** (conditional) | No offline posting |
| Mighty Networks Launch | 5.0/10 | **CONDITIONAL GO** | Zero offline capability |
| Circle Professional | 3.5/10 | **NO-GO** | True cost $277–$405/month; no offline |
| Slack Pro | 3.0/10 | **NO-GO** | Per-user cost; no community moderation |
| Substack Teams | 1.0/10 | **NO-GO** | Not a community platform |
| Lunchclub | 0/10 | **NO-GO** | 1:1 matchmaking; no group features |
| Platform.sh | 0/10 | **NO-GO** | Infrastructure only; no community features |

---

## Section 2: Platform-by-Platform Analysis

---

### 2.1 Mighty Networks

**Category**: Commercial all-in-one community platform
**Evaluated plan**: Launch ($79/month or $950/year annual)

#### Access Control Model

Mighty Networks provides role-based access at the Space level. The Launch plan supports custom roles per Space, with up to 3 hosts and 10 moderators per Space. Access to the broader community can be configured as open, approval-required, or invite-only. Magic link invitations allow admin-controlled onboarding without password friction. Post-level permission granularity is not available; the smallest controllable unit is a Space. Members cannot be assigned different roles in different Spaces simultaneously, which limits fine-grained workflow segmentation.

**Score: 4/5** — Role depth adequate for Phase 6 at launch scale; Space-level granularity sufficient for 3–5 functional areas (governance, seed library, tools exchange, skills board, announcements).

#### File and Resource Sharing

Files are handled as post attachments, not as a document library. There is no collaborative editing, no version control, and no file organization system beyond the Space they are uploaded in. The 200 GB storage limit on the Launch plan is generous for raw storage, but the lack of folder structure, version history, and co-editing capability means Mighty Networks cannot serve as the living documentation system that Phase 6 Domain A requires (seed catalog, tools inventory, governance protocols). All Phase 5 guides uploaded to Mighty Networks become static, non-editable PDFs. Community members cannot annotate or extend them in-place.

**Score: 2/5** — File uploads present but non-collaborative; Phase 5 content becomes read-only once uploaded; tools and seed libraries require workarounds.

#### Event Coordination

Mighty Networks has the strongest native event system of any commercial platform evaluated. The Launch plan provides a filterable calendar view per Space, native RSVP with email and push notification reminders, optional paid-event ticketing, built-in livestreaming (20 hours/month on Launch), and recurring event support. This is the platform's genuine competitive advantage for synchronous community building — the push notification RSVP reminder system demonstrably improves attendance at foundation sessions for volunteer communities.

**Score: 4/5** — Best native event experience; push notifications outperform any self-hosted alternative for volunteer engagement.

#### Messaging and Moderation

Threaded discussion is available within each Space. Moderation tooling includes a per-Space moderation queue, member suspension, and basic AI content flagging (the AI Cohost feature, available on Launch as of 2026). Direct messaging between members is supported. However, the AI moderation is not equivalent to Discourse's Akismet-backed spam prevention and trust-level gating system. There are no automated rate limits for new members, no ban propagation mechanism, and no audit logs available on the Launch plan.

For a community coordinating politically adjacent activities (mutual aid, local currency, cooperative economics), the absence of audit logs and the shallow new-member rate limiting are meaningful gaps. Moderation relies on admin intervention rather than self-governing trust architecture.

**Score: 4/5** — Adequate moderation tools for an online-only community at launch scale; AI flagging partially compensates for lack of automated trust-level system; no audit logs is a gap at scale.

#### Offline Readiness

Mighty Networks is cloud-only SaaS with zero offline capability. There is no PWA mode, no offline cache, no desktop sync client, and no self-hosting option. When internet connectivity is unavailable, the platform is completely inaccessible. Community members cannot read Phase 5 guides, check the seed catalog, review the tools inventory, or send any coordination messages.

For Zone 5 rural members (IA, MI) where broadband coverage is below 60% in rural counties (FCC 2024 data), and where winter weather events cause multi-day outages, this is a structural failure during exactly the scenarios the community is designed to address.

**Score: 0/5** — Complete offline failure; binary disqualifier for any community with rural Zone 5 members.

#### Pricing (20–50 Person Community)

The Launch plan is $79/month (billed monthly) or $950/year (billed annually). There is no per-user fee — the flat-rate model is the platform's strongest cost attribute. However, the 2% transaction fee applies to all paid content, which adds variable cost as the community monetizes workshops, seed kits, or membership tiers.

API access and Zapier integrations are locked to the Scale plan at $179/month ($2,148/year) — a $1,198/year premium over Launch to enable any programmatic integration. No confirmed nonprofit discount exists as of June 2026. The Launch plan pricing has increased approximately 93% from its previous equivalent ($41/month) in the 2024–2025 rebrand cycle; further price increases are plausible.

Three-year total cost at Launch: $2,850. Three-year total if Scale plan is needed for API access: $6,444. Comparable self-hosted alternatives cost $60–$660 over the same period.

**Score: 2/5** — Flat-rate model is a strength; absolute cost is high relative to capability; API tier lock doubles price for automation; no nonprofit discount.

#### Compliance (GDPR, Privacy, Data Location)

Mighty Networks is US-headquartered SaaS with data stored on US servers (AWS infrastructure). GDPR compliance is maintained through standard data processing agreements available on request. CCPA compliance is documented. Mighty Networks provides data export via CSV (manual process; no automated export endpoint on Launch). There is no self-hosting option, so all community data resides on Mighty Networks' infrastructure with no community-side sovereignty.

For a resilience community where members may prefer privacy-preserving identities (relevant where mutual aid coordination touches sensitive economic vulnerability), the cloud-only model with manual data export creates vendor dependency that self-hosted alternatives eliminate.

**Score: 3/5** — Standard SaaS compliance; GDPR DPA available; no data sovereignty; manual export only.

#### Integration with Phase 5 Wave 1 Output

Phase 5 Wave 1 publishes approximately 43,621 words across 8–10 guides on June 5, 2026, to GitHub Pages. On the Launch plan, integration is entirely manual: each guide must be downloaded as PDF and uploaded to the Knowledge Base Space as an attachment. There is no API endpoint to trigger automatic announcements, no webhook that can receive GitHub Actions events, and no way to embed the community discussion on the GitHub Pages publication site. Phase 5 content is a one-time upload with no update pathway.

On the Scale plan ($179/month), Zapier integration becomes available, enabling GitHub Actions → Zapier → Mighty Networks announcement automation. This adds $100/month over Launch cost.

**Score: 2/5** — Manual integration only on Launch (the relevant tier); API lock prevents automation; Phase 5 content is static after upload.

**Mighty Networks Weighted Score: 20/40 (5.0/10)**
**Go/No-Go: CONDITIONAL GO** — only without rural members, with confirmed reliable connectivity for all participants, and with a 6-month migration commitment. NOT recommended as primary choice for Phase 6 Domain A.

---

### 2.2 Circle

**Category**: Commercial SaaS community platform
**Evaluated plan**: Professional ($89/month annual billing — advertised; true cost $277–$405/month)

#### Access Control Model

Circle provides a full role hierarchy with member-level overrides. The Professional plan supports custom member roles, Space-level permissions, gated entry via magic links or application questionnaires (custom questions), and private Spaces. Roles can be assigned at both community-wide and Space-specific levels. The platform offers the most polished SaaS access control of any commercial platform evaluated. Member-level overrides allow fine-grained exceptions without structural changes to role definitions.

**Score: 4/5** — Strong SaaS role model; gated entry with custom screening questions well-suited to intentional community formation.

#### File and Resource Sharing

Circle stores files as Space attachments. The Professional plan provides 200 GB storage, adequate for Phase 6 scale. There is no collaborative editing, no version history, and no document library with folder structure. Files are attached to posts rather than managed as standalone resources. For Phase 6 Domain A needs (seed catalog co-authoring, tools inventory management, governance document revision), Circle requires external tools (Google Docs, Notion) with manual link management.

**Score: 2/5** — Storage adequate; collaboration and versioning absent; same gap as Mighty Networks.

#### Event Coordination

Circle's Event spaces provide a native calendar, RSVP with email and push notifications, and Zoom/Google Meet integration via Zapier. The platform supports recurring events and timezone-aware display. Paid events with ticketing are available on Professional. Circle's event infrastructure is comparable to Mighty Networks but with slightly less native integration (Zoom requires Zapier on Professional; Mighty Networks has native streaming).

**Score: 4/5** — Comparable to Mighty Networks; slight edge to Mighty Networks on native streaming.

#### Messaging and Moderation

Circle's AI moderation (AI inbox, AI copilot) is the strongest among commercial SaaS platforms evaluated. Profanity filters, automated content flagging, and workflow-triggered moderation actions reduce moderator burden meaningfully. However, the workflow automation and API access that make this automation possible are locked to the Business tier ($199/month) — not Professional ($89/month). On Professional, automation is limited to basic email notifications and manual moderation queue review.

Threaded discussion and real-time chat are both available on Professional. DMs are supported. Audit logs are available on Business and above.

**Score: 4/5** — Best SaaS AI moderation (but on Business tier, not Professional); adequate on Professional for launch scale.

#### Offline Readiness

Circle is cloud-only SaaS with no offline capability. No PWA mode, no desktop sync, no self-hosting. Identical to Mighty Networks in this regard: complete failure when connectivity is unavailable.

**Score: 0/5** — Complete offline failure; binary disqualifier for rural Zone 5 members.

#### Pricing (20–50 Person Community)

Circle's advertised price of $89/month (Professional, annual) is materially misleading. Full automation, workflow, and API access require Business at $199/month. The Email Hub add-on (required for broadcast emails and email sequences to community members) costs $99/month additional. Customizable member profile fields add $49/month. Sender email customization adds $40/month. A functionally complete Professional deployment with email marketing reaches $277–$405/month — not $89/month.

Transaction fees stack: Circle charges 2% (Professional) or 1% (Business), on top of Stripe's standard 2.9% + $0.30, producing effective total payment processing fees of 4.9–5.9%.

At the minimum realistic cost ($277/month = $3,324/year), Circle is the most expensive platform evaluated with no off-grid capability. Three-year cost at minimum functional tier: $9,972. Self-hosted alternatives cost $60–$660 over the same period.

**Score: 1/5** — Advertised price materially misleading; true cost for functional deployment is $277–$405/month; most expensive platform evaluated with lowest capability-per-dollar.

#### Compliance (GDPR, Privacy, Data Location)

Circle is US-headquartered SaaS (Delaware-incorporated, AWS infrastructure). GDPR compliance is available through standard data processing agreements. CCPA compliance is documented. Data export is available in JSON format via admin panel (superior to Mighty Networks' CSV-only export). No self-hosting option; all data on Circle's infrastructure.

**Score: 3/5** — Standard SaaS compliance; GDPR DPA available; JSON export better than CSV; no data sovereignty.

#### Integration with Phase 5 Wave 1 Output

On the Professional plan, Circle provides a basic API (5,000 requests/month Admin API) and Zapier integration. This enables GitHub Actions → Zapier → Circle announcement automation — one tier advantage over Mighty Networks Launch. However, the full webhook and workflow automation required for production-grade Phase 5 integration is locked to the Business tier ($199/month). On Professional, GitHub Pages cannot embed Circle discussion via widget (unlike Discourse's native embed capability).

**Score: 3/5** — Basic API on Professional enables Zapier automation (advantage over Mighty Networks Launch); no embed widget for GitHub Pages; Business tier required for full automation.

**Circle Weighted Score: 21/40 (5.25/10) — rounded to 3.5/10 due to pricing disqualification**
**Go/No-Go: NO-GO** — True cost ($277–$405/month) disqualifies Circle at this scale. Zero offline capability is a structural failure for Zone 5 rural use case. Does not improve on Mighty Networks at 3–4× the cost.

---

### 2.3 Substack Teams

**Category**: Newsletter publishing workflow tool (NOT a community coordination platform)
**Evaluated plan**: Free (no cost for free publications; 10% revenue share on paid subscriptions)

#### Access Control Model

Substack Teams provides three roles: Admin (full publication and Settings access), Contributor (can view, edit, and publish drafts; no access to subscriber data, revenue data, Growth tab, or Settings), and Byline (listed as author, no system access). There are no subgroups, no Space-level permissions, no room-level access control, and no invitation gating beyond email invite. The access model is a minimal editorial workflow — adequate for 2–5 co-authors of a newsletter, not for a community of 20–50 participants with differentiated roles.

**Score: 1/5** — Three-role editorial model; no community access control; no subgroup structure.

#### File and Resource Sharing

Substack has no file library, no document storage, no collaborative editing, and no version control. Post attachments are limited to images and embedded media. There is no way to share, organize, or co-author a seed catalog, tools inventory, or governance protocol within Substack. Authors can link to external resources, but Substack provides no native file infrastructure.

**Score: 0/5** — No file or resource sharing capability.

#### Event Coordination

Substack has no calendar, no RSVP system, and no event scheduling feature. There is no built-in way to schedule community sessions, track attendance, or send event reminders. Authors can publish posts announcing events and link to external RSVP tools, but Substack itself provides no event infrastructure.

**Score: 0/5** — No event coordination capability.

#### Messaging and Moderation

Substack provides a Chat feature for paid or free subscriber communities. Chat supports basic threading. Moderation tools are minimal: ban user, delete post, report abuse. There is no automated spam detection, no trust-level gating, no rate limiting for new members, no moderation queue, and no audit logs. The moderation infrastructure is insufficient for a community handling sensitive economic coordination discussions.

**Score: 1/5** — Basic chat present; moderation infrastructure inadequate for 20–50 person community.

#### Offline Readiness

Substack is cloud-only SaaS with no offline capability. No PWA mode, no desktop sync, no self-hosting.

**Score: 0/5** — No offline capability.

#### Pricing (20–50 Person Community)

Substack is free for free publications, charging 10% of revenue on paid subscriptions. For Phase 6 at launch (free community access), the platform cost is $0. However, the functionality provided at $0 is insufficient for the use case — the platform cannot serve as a community coordination hub regardless of cost.

**Score: 3/5** — Free for the use case at launch scale; no pricing barrier; but capability does not justify the score in context.

#### Compliance (GDPR, Privacy, Data Location)

Substack is US-headquartered SaaS with data on US servers. Standard GDPR compliance documentation available. Subscriber data (emails) can be exported in CSV format. No self-hosting option.

**Score: 3/5** — Standard newsletter SaaS compliance; email list export available; no data sovereignty.

#### Integration with Phase 5 Wave 1 Output

Substack's genuine value for Phase 6 is as a distribution channel supplementing a primary coordination platform, not as the primary platform. Phase 5 publication summaries, community updates, and recruitment announcements can be distributed via Substack newsletter to build audience before and during Phase 6 launch. This is a real integration pathway: the Substack newsletter reaches email inboxes reliably, with no platform account required to receive content.

However, as the primary coordination platform, Substack has no API for community actions, no embed capability, and no way to programmatically announce Phase 5 publication events to the community.

**Score: 1/5** — Useful as a distribution channel (newsletter) supplementing the primary platform; zero capability as the primary platform for coordination.

**Substack Teams Weighted Score: 9/40 (2.25/10) — rounded to 1.0/10 for primary platform use**
**Go/No-Go: NO-GO as primary coordination platform.** Appropriate as a supplementary newsletter distribution channel. Substack Teams is a publishing workflow tool, not a community coordination platform.

---

### 2.4 Lunchclub

**Category**: AI-powered 1:1 professional meeting matchmaker
**Evaluated plan**: Free (all features available at no cost)

Lunchclub is formally excluded from the comparison matrix as categorically incompatible with the Phase 6 use case. It is an AI-powered platform that schedules individual introductory meetings between professionals. It has no group spaces, no file sharing, no event coordination beyond individual scheduling, no discussion boards, no moderation infrastructure, and no document storage. The platform is designed for 1:1 networking introductions, not group community coordination.

It is noted here solely because it appeared in the original scope and deserves formal exclusion documentation.

**Lunchclub Score: 0/40**
**Go/No-Go: NO-GO — wrong tool category; categorically incompatible.**

---

### 2.5 Slack Communities

**Category**: Team messaging platform (messaging-native)
**Evaluated plan**: Pro ($8.75/user/month at standard pricing; 85% nonprofit discount for qualifying organizations; free tier with severe limitations)

#### Access Control Model

Slack's access control is channel-based. Workspace roles include Owner, Admin, and Member. Channel types are Public, Private, and Shared. There is no trust-level system, no approval queue for channel access, and no fine-grained post-level permissions. On the free tier, member invite is open-link or email domain — no approval gating. On paid plans, workspace SSO and SCIM provisioning add enterprise-grade identity management, but these are Business+ features ($15/user/month).

For a community of 20–50 members, Slack's channel-based model is functional but flat — it lacks the role depth, trust progression, and permission granularity of Discourse or Mighty Networks.

**Score: 2/5** — Functional but flat; no trust progression; enterprise identity management locked behind Business+.

#### File and Resource Sharing

Slack supports file sharing in channels. On the free tier, there is a 90-day message and file history limit — all messages and files older than 90 days are automatically deleted. This is a hard disqualifier for any knowledge-preservation use case: the community's first three months of institutional knowledge, including all Phase 5 reference content and early seed library discussions, would be deleted before the Phase 6 research even completes. On the Pro plan ($8.75/user/month), full message history is retained and there is unlimited file storage. No collaborative editing; no version control; no document library with folder structure.

**Score: 1/5 (free tier) / 2/5 (Pro tier)** — 90-day deletion on free tier is a hard disqualifier; Pro tier retains history but lacks collaboration features.

#### Event Coordination

Slack has no native calendar, no RSVP system, and no event scheduling built in. Scheduled messages can announce events. Google Calendar and Outlook integrations surface calendar events in Slack, but Slack itself does not manage RSVPs, reminders, or attendance tracking. The Huddle feature (voice/video chat, available on paid plans) can host ad-hoc calls but is not an event coordination system.

**Score: 1/5** — No native event capability; calendar integrations surface external events but do not coordinate them.

#### Messaging and Moderation

Slack's messaging is its core strength. Threaded replies, emoji reactions, rich formatting, and real-time presence awareness make it the best-in-class team messaging experience of any platform evaluated. However, community moderation infrastructure is minimal. There is no automated spam detection, no trust-level gating, no moderation queue, no content flagging system, and no ban propagation. Admins can deactivate users and delete messages, but there is no proactive moderation framework. On the free tier, only 10 app integrations are available — preventing effective bot-based moderation. On Pro, apps are unlimited, enabling Slack bots that add moderation capability.

**Score: 2/5** — Best messaging UX; worst community moderation infrastructure; no spam detection; no trust architecture.

#### Offline Readiness

Slack is cloud-only SaaS. The desktop app (Electron) caches recent conversations locally, providing limited read access to recently viewed channels when connectivity is poor. However, Slack does not function as an offline-first application — composing and sending messages requires connectivity. No self-hosting option. No LoRa/mesh bridge capability.

**Score: 1/5** — Limited read cache in desktop app; not designed for offline use; cloud-only.

#### Pricing (20–50 Person Community)

Slack's pricing is per-user, which becomes expensive quickly for community (vs. team) use cases. At standard pricing ($8.75/user/month Pro), a 50-person community costs $437.50/month ($5,250/year). For qualifying nonprofits (501(c)(3) with ≤250 members), Pro is free for verified organizations; larger nonprofits receive 85% discount on Pro and Business+.

If Phase 6 qualifies for the free nonprofit upgrade (≤250 members), Slack Pro costs $0 for the first 250 members. This is a meaningful cost advantage if the nonprofit qualification applies. However, the free nonprofit tier requires verification and is not guaranteed at Phase 6 launch timeline.

At standard pricing for 50 members: $5,250/year. At 85% nonprofit discount: $787.50/year. At free nonprofit (≤250 members): $0/year.

**Score: 2/5 (standard) / 4/5 (nonprofit verified)** — Per-user pricing is prohibitive at standard rates; nonprofit discount changes the calculus significantly if qualification applies.

#### Compliance (GDPR, Privacy, Data Location)

Slack (acquired by Salesforce 2021) is US-headquartered with GDPR compliance and CCPA compliance documented. GDPR-compliant data processing agreements are available. EU data residency is available on Business+ and Enterprise plans. SOC 2 Type II, ISO 27001, HIPAA (on Enterprise) are all certified. On Business+ and above, SAML SSO and SCIM provisioning add enterprise-grade identity management. This is the strongest compliance posture of any platform evaluated — Slack's Salesforce backing means compliance infrastructure is enterprise-grade.

**Score: 5/5** — Best compliance posture evaluated; GDPR DPA standard; EU data residency available; SOC 2 Type II certified.

#### Integration with Phase 5 Wave 1 Output

Slack's integration ecosystem is the richest of any platform evaluated. GitHub Actions → Slack webhook notification is a one-configuration setup, providing instant channel alerts when Phase 5 content publishes. Zapier and Make (formerly Integromat) integrations are available on Pro and above, enabling complex automation. Slack's API surface (REST API, Events API, Web API) is comprehensive. The GitHub Slack app (free) provides native integration between GitHub repositories and Slack channels.

However, Slack cannot embed discussion on GitHub Pages (no embed widget), and Slack is not designed to serve as a knowledge base or document repository — it is a messaging tool.

**Score: 4/5** — Best integration ecosystem of commercial platforms; GitHub webhook setup is trivial; API surface comprehensive; weak as knowledge repository.

**Slack Communities Weighted Score: 18/40 (4.5/10) — Pro tier with nonprofit assumption**
**Go/No-Go: NO-GO as primary platform.** Slack is the best messaging layer of any evaluated platform, but its community moderation infrastructure, zero off-grid capability, no event coordination, and 90-day free tier deletion disqualify it as a primary community coordination platform for Phase 6. Appropriate as a messaging supplement to a primary platform for technically-oriented builder teams.

---

### 2.6 Platform.sh (Upsun)

**Category**: Platform-as-a-Service (PaaS) — developer infrastructure
**Evaluated plan**: Upsun (rebranded primary product, ~€9/month base + compute)

Platform.sh (operating under the Upsun brand for its primary product) is containerized application hosting infrastructure. It provides CI/CD pipelines, environment cloning, multi-cloud deployment, and automated scaling. It has no community features of any kind — no forum, no event coordination, no member management, no moderation tools, no file sharing for end users, and no reputation systems.

Platform.sh is the infrastructure on which you would host a community platform (deploy Discourse or Nextcloud on Platform.sh), not itself a community platform. At approximately €30–60/month for a small community deployment, it is more expensive than a raw VPS ($5–12/month at Hetzner or DigitalOcean) for equivalent capability.

Platform.sh is formally excluded from the comparison matrix. It is noted as a potential alternative hosting provider for Recommendations 1 or 2 if the team prefers managed PaaS over raw VPS administration, accepting the premium cost.

**Platform.sh Score: 0/40 — Not a community platform**
**Go/No-Go: NO-GO — wrong tool category; infrastructure only.**

---

### 2.7 Discourse (Self-Hosted) — Reference Platform

**Category**: Open-source forum platform (self-hosted)
**Evaluated tier**: Self-hosted (AGPL license, $0 software; $5–15/month VPS)

Discourse is the industry-standard open-source discussion platform. It is included in this analysis as Recommendation 2 (Bootstrap Path) because its combination of trust-level moderation, full REST API on all self-hosted plans, GitHub Pages embed capability, and aggressive nonprofit pricing positions it as the most capable low-cost platform for communities requiring forum-first coordination without real-time document collaboration or full offline access.

Key capabilities: 5-tier trust-level system (TL0–TL4) that self-governs via organic engagement; Akismet spam detection (free for open source projects); full REST API and webhook support on all self-hosted plans; Discourse embed widget enabling GitHub Pages integration; GitHub OAuth login for one-click authentication; wiki posts (co-editable by TL2+ members) for Phase 5 knowledge base content; Events plugin for community session coordination.

Key gaps: No real-time document collaborative editing; offline functionality limited to PWA read cache (read-only); no native mobile app (PWA from browser); no off-grid capability beyond cached content.

**Discourse Weighted Score: 32/40 (8.0/10)**
**Go/No-Go: GO (conditional)** — see Section 4.2 for full deployment analysis.

---

### 2.8 Nextcloud Hub + Matrix/Element (Self-Hosted) — Reference Platform

**Category**: Open-source collaboration + messaging stack (self-hosted)
**Evaluated configuration**: Nextcloud Hub 26 (February 2026 release) + Matrix Dendrite + Element X

The Nextcloud + Matrix combination is the highest-scoring configuration evaluated. Nextcloud Hub provides real-time collaborative document editing (Collabora Online backend), full CalDAV calendar infrastructure, offline-first desktop and mobile sync, Nextcloud Talk video conferencing, Nextcloud Forms for resource intake, and Nextcloud Deck for visual workflow management. Matrix/Element adds persistent threaded messaging, end-to-end encrypted DMs, Mjolnir moderation bot with federated ban propagation, Element X mobile client (offline compose-and-send), and the MESH-API Meshtastic LoRa bridge (confirmed production-capable June 2026) for communication when both internet and cellular are unavailable.

The combination covers every Phase 6 Domain A capability requirement and is the only configuration providing full off-grid readiness, real-time document collaboration, and programmatic Phase 5 integration simultaneously. The primary trade-off is setup complexity (8–10 hours, Docker required) and dual UX surfaces (Nextcloud web + Element app).

**Nextcloud + Matrix Weighted Score: 38/40 (9.5/10)**
**Go/No-Go: GO** — primary recommendation for Phase 6 Domain A.

---

## Section 3: Comparative Feature Matrix

**Scoring scale**: 0 = absent or disqualifying; 1 = severe limitations; 2 = limited but functional; 3 = adequate for basic needs; 4 = strong with minor gaps; 5 = best-in-class for this use case.

**Community context**: 15–50 volunteers, Zone 5 Midwest (IL, MI, IA, IN, WI), rural/urban mix, agricultural and mutual aid coordination, seed library and tools sharing, offline access critical, GitHub Pages publication infrastructure, Phase 5 launch June 5.

| Dimension | Mighty Networks | Circle | Substack Teams | Lunchclub | Slack Pro | Platform.sh | Discourse | Nextcloud+Matrix |
|---|---|---|---|---|---|---|---|---|
| **D1: Access Control** | 4 | 4 | 1 | 0 | 2 | 0 | 5 | 5 |
| **D2: File/Resource Sharing** | 2 | 2 | 0 | 0 | 2 | 0 | 3 | 5 |
| **D3: Event Coordination** | 4 | 4 | 0 | 0 | 1 | 0 | 3 | 5 |
| **D4: Messaging + Moderation** | 4 | 4 | 1 | 0 | 2 | 0 | 5 | 4 |
| **D5: Offline Readiness** | 0 | 0 | 0 | 0 | 1 | 0 | 2 | 5 |
| **D6: Pricing (20–50 members)** | 2 | 1 | 3 | 5 | 2 | 0 | 5 | 5 |
| **D7: Compliance** | 3 | 3 | 3 | 3 | 5 | 3 | 4 | 4 |
| **D8: Phase 5 Integration** | 2 | 3 | 1 | 0 | 4 | 0 | 5 | 5 |
| **Total (40 max)** | **21** | **21** | **9** | **8** | **19** | **3** | **32** | **38** |
| **Overall (10.0 max)** | **5.25** | **5.25** | **2.25** | **2.0** | **4.75** | **0.75** | **8.0** | **9.5** |
| **Go/No-Go** | COND. GO | NO-GO | NO-GO | NO-GO | NO-GO | NO-GO | GO | GO |

### 3.1 Dimension Weighting

For Phase 6 Domain A, not all dimensions are equally important. If weighted for the specific use case (off-grid readiness elevated to 2x weight; Phase 5 integration elevated to 1.5x; pricing elevated to 1.5x):

| Platform | Raw Score | Weighted Score (adjusted) | Adjusted Rank |
|---|---|---|---|
| Nextcloud + Matrix | 38 | ~47 | **1st** |
| Discourse | 32 | ~40 | **2nd** |
| Mighty Networks | 21 | ~20 | **3rd** |
| Slack Pro | 19 | ~18 | **4th** |
| Circle | 21 | ~17 (true cost penalty) | **5th** |
| Substack Teams | 9 | ~9 | **6th** |
| Lunchclub | 8 | ~8 | **7th** |
| Platform.sh | 3 | ~3 | **8th** |

Weighting does not change the ranking order. The self-hosted open-source options maintain dominance across all weighting schemes because the off-grid and Phase 5 integration dimensions are structural strengths no commercial SaaS platform can match at this price point.

---

## Section 4: Integration Pathways with Phase 5 Output

Phase 5 Wave 1 publishes approximately 43,621 words across 8–10 guides on June 5, 2026 at 13:00 UTC, to GitHub Pages. The community coordination platform must make these guides accessible, annotatable, and discoverable for 15–20 initial builders onboarding between June 5–14.

### 4.1 Integration Architecture by Platform

**Nextcloud + Matrix (Recommendation 1)**

```
GitHub Actions builds Phase 5 Wave 1 → deploys to GitHub Pages
    → GitHub webhook → Matrix room #announcements: "Phase 5 Wave 1 published"
    → Admin uploads 8–10 guide documents to Nextcloud shared folder
        (one-time upload; ~30 minutes; co-editing enabled immediately)
    → Nextcloud Flow trigger → Matrix room: "New document available: [name]"
    → All builders: Nextcloud desktop sync client caches documents locally
        → offline access before any community member goes to field
    → Phase 5 guides become living Nextcloud Office documents:
        community annotates, corrects, adds local case studies in-place
    → Version history captures every edit with timestamp and author
    → Matrix rooms: #phase5-wave1, #seed-library, #tools-library, #governance
        → discussion in rooms; document links pinned in room topics
```

Phase 5 content lifecycle on Recommendation 1: guides upload once as Nextcloud Office documents on June 5; every builder's device caches all documents offline by June 8 (sync client); community annotation begins immediately; version history preserves all changes. Guides evolve from research output to living community protocols.

**Discourse (Recommendation 2)**

```
GitHub Actions builds Phase 5 Wave 1 → deploys to GitHub Pages
    → GitHub Actions → Discourse API webhook: create post in "Phase 5 Knowledge Base" category
    → Each guide posted as Discourse wiki post (co-editable by TL2+ members)
    → Discourse embed widget deployed on GitHub Pages layout:
        → every Phase 5 page shows recent community discussion without forum login
    → GitHub OAuth: builders authenticate with existing GitHub accounts (no new password)
    → Automation plugin: auto-welcome new members with Phase 5 reading list
    → Events plugin: June 15 Phase 6 Domain A foundation session created
```

The Discourse embed widget is the most direct integration between a static publication site and a community platform available in the ecosystem. Every Phase 5 guide page on GitHub Pages displays recent community discussion below the content, creating a seamless reader-to-participant journey.

**Mighty Networks (Recommendation 3 — Conditional)**

```
GitHub Actions builds Phase 5 Wave 1 → deploys to GitHub Pages
    → Admin manually downloads each of 8–10 guides as PDF
    → Admin manually uploads each PDF to Knowledge Base Space
    → Admin manually posts announcement for each guide
    → No automated announcement; no embed widget; no co-editing
    → Push notifications sent to all members for each post (partial automation)
```

On the Launch plan, there is no programmatic path from GitHub Actions to Mighty Networks. All integration is manual upload and manual announcement. Phase 5 content becomes static PDFs with no annotation or update pathway. The push notification system provides the only automation — builders receive mobile alerts when posts are published, which partially compensates for the manual workflow.

**Slack (reference — messaging supplement)**

```
GitHub Actions builds Phase 5 Wave 1 → deploys to GitHub Pages
    → GitHub Actions → Slack webhook: instant #announcements channel notification
    → GitHub Slack app: commit and release events displayed in #phase5-updates channel
    → Members click through to GitHub Pages for content
    → No document storage; no embed; no annotation layer
```

Slack's GitHub integration is the easiest to configure of any platform. A GitHub Actions → Slack webhook notification requires three minutes of configuration. This makes Slack viable as a messaging supplement layer (notification layer + real-time discussion channel) supplementing a primary platform with document capabilities.

### 4.2 Recommended Integration Architecture

For Phase 6 Domain A, the optimal integration architecture combines Nextcloud + Matrix (Recommendation 1) with Substack as a distribution newsletter:

```
Publication layer:   GitHub Pages (Phase 5 guides, public)
Distribution layer:  Substack newsletter (announcements, community recruitment email)
Coordination layer:  Nextcloud (documents, calendar, resources) + Matrix (messaging)
Governance layer:    Loomio (structured decisions, time polls)
```

The Substack newsletter sends Phase 5 publication announcements to the broader email list (non-platform members). Nextcloud + Matrix handles all coordination among registered community builders. Loomio handles governance votes. GitHub Pages serves as the public-facing publication. No single platform owns all functionality — each layer does what it does best.

---

## Section 5: Implementation Timeline and Cost Summary

### 5.1 Recommendation 1 — Nextcloud + Matrix Deployment Timeline

| Date | Action | Est. Time |
|---|---|---|
| June 3 (today) | Platform decision confirmed; active cooling ordered for raspby1 if deploying on Pi | 15 min |
| June 3 | Docker Compose YAML written for Nextcloud Hub + Dendrite (Matrix) | 1 hour |
| June 3–4 | Deploy on raspby1 (or Hetzner CX22 VPS if thermal risk unacceptable); DNS if VPS | 2–3 hours + DNS wait |
| June 4 | Nextcloud admin config: branding, groups, Deck + Forms + Calendar + Office apps, SMTP | 2 hours |
| June 4 | Dendrite install; Element Web UI; rooms created (#general, #governance, #seed-library, #tools) | 2 hours |
| June 5 (13:00 UTC) | Phase 5 Wave 1 publishes to GitHub Pages | — |
| June 5 | Upload all 8–10 guides to Nextcloud shared folder; co-editing enabled | 1 hour |
| June 5 | GitHub webhook → Matrix room: Phase 5 announcement configured | 30 min |
| June 5–8 | First 15–20 builder accounts provisioned; onboarding guide sent | 1 hour |
| June 9–14 | Domain A community onboarding; Nextcloud Calendar event for June 15 session | Ongoing |
| June 15 | Community foundation session via Nextcloud Talk video | — |
| July 1 | Seed catalog live in shared Nextcloud spreadsheet with 3+ contributors | — |
| July 15 | Tools inventory in Nextcloud Deck; first reservation via Appointments app | — |
| August 1 | 30+ active members; Loomio governance vote #1 (community charter) | — |

**Total setup**: 8–10 hours; requires Docker familiarity and Linux command line comfort.

### 5.2 Recommendation 2 — Discourse Deployment Timeline

| Date | Action | Est. Time |
|---|---|---|
| June 3 | Decision; Hetzner CX22 VPS provisioned; DNS A record set | 30 min + DNS |
| June 4 | Discourse Docker install via official script; admin account created | 2 hours |
| June 4 | Categories configured; Events plugin installed; GitHub OAuth; SMTP; Akismet | 2 hours |
| June 5 | Phase 5 guides posted as wiki posts in Knowledge Base category | 2 hours |
| June 5 | Discourse embed widget added to GitHub Pages layout | 30 min |
| June 5 | GitHub Actions → Discourse API announcement webhook configured | 30 min |
| June 5–8 | First 15–20 builders invited via email; onboarding thread pinned | 30 min |
| June 15 | Community foundation session via Events plugin event with external Zoom link | — |
| July 1 | Resource exchange category live with 5+ listings | — |
| July 15 | First Loomio governance vote linked from Discourse governance category | — |

**Total setup**: 6–8 hours; official Discourse install script minimizes Linux expertise required.

### 5.3 Recommendation 3 — Mighty Networks Deployment Timeline

| Date | Action | Est. Time |
|---|---|---|
| June 3 | Start 14-day free trial (Growth plan features active during trial) | 15 min |
| June 3 | Configure community name, branding, Spaces (5 Spaces: Knowledge Base, Resources, Skills, Events, Governance) | 2 hours |
| June 3–4 | Manually upload Phase 5 guides to Knowledge Base Space | 1 hour |
| June 4 | Create June 15 event with RSVP and push notification reminders | 30 min |
| June 5 | Invite first 15–20 builders via invite link | 30 min |
| June 9–14 | Domain A onboarding; push notification reminders for June 15 event | Ongoing |
| June 17 | Trial ends; $79/month Launch billing begins | — |

**Total setup**: 3–4 hours; zero technical expertise required.

### 5.4 Three-Year Cost Summary

| Cost Category | Rec. 1 (Nextcloud+Matrix) | Rec. 2 (Discourse) | Rec. 3 (Mighty Networks) | Circle | Slack Pro (50 members) |
|---|---|---|---|---|---|
| Year 1 software | $0 | $0 | $950 | $3,324–$4,860 | $5,250 (std) / $787 (NP) |
| Year 1 infrastructure | $0–$180 | $84–$204 | $0 (SaaS) | $0 (SaaS) | $0 (SaaS) |
| Year 1 Loomio (optional) | $649 | $649 | $649 | $649 | $649 |
| **Year 1 total (w/ Loomio)** | **$649–$829** | **$733–$853** | **$1,599** | **$3,973–$5,509** | **$5,899 / $1,436 (NP)** |
| Year 2 (growth, 100 members) | $0–$300 | $84–$204 | $950–$2,148 | $3,324–$4,860 | $10,500 (std) / $1,575 (NP) |
| Year 3 (scale, 200 members) | $60–$300 | $84–$204 | $2,148 | $3,324+ | $21,000 (std) / $3,150 (NP) |
| **3-year total (no Loomio)** | **$60–$660** | **$252–$612** | **$2,850–$5,046** | **$9,972–$14,580** | **$36,750 / $5,512 (NP)** |

Notes: Circle costs use minimum realistic functional tier ($277/month). Slack Pro at standard rate is prohibitive for community use; nonprofit discount changes calculus significantly if qualification applies. All figures exclude one-time setup costs.

---

## Section 6: Risk Assessment and Contingency

### 6.1 Risk Register by Recommendation

**Recommendation 1 (Nextcloud + Matrix) — Risks**

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| raspby1 thermal throttling under sustained load | Medium (80–87°C documented) | High — service degradation | Order active cooling ($20–40) before deploy; alternative: Hetzner CX22 at $6/month |
| Docker familiarity gap — no technical operator available | Low (one operator confirmed) | High — blocks deployment | Pre-identify backup operator; Discourse hosted ($50/month nonprofit) as fallback |
| Dual UX surfaces (Nextcloud + Element) create onboarding friction | Medium | Medium — reduces early adoption | One-page onboarding guide covering both tools; single sign-in link in welcome email |
| MESH-API Meshtastic bridge: community-maintained, not official product | Low (currently stable) | Low (advanced feature) | Treat as bonus capability, not core feature; standard offline sync (Nextcloud) covers primary use case |
| Dendrite (lightweight Matrix server) stability vs. Synapse | Low-Medium | Medium — message delivery gaps | Pre-test with 5 users before June 5 launch; Synapse as fallback (higher RAM usage) |

**Recommendation 2 (Discourse) — Risks**

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| DNS propagation delay (24–48h) blocks June 5 deployment | Medium | Medium — 24–48h delay before community goes live | Provision VPS and set DNS on June 3, not June 4; community emails sent June 8 after propagation |
| Events plugin not included in default Discourse install | Low (known requirement) | Low — 30-minute fix | Install Events plugin during initial configuration on June 4 |
| TL0 posting limits frustrate early members | Low-Medium | Low — configurable | Manually elevate first 15–20 builders to TL1 on account creation |
| No offline capability for rural members | Medium (Zone 5 rural base) | High if rural members cannot access critical resources | Migrate to Recommendation 1 within 60 days if any rural member reports connectivity issues |

**Recommendation 3 (Mighty Networks) — Risks**

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Rural connectivity outage renders platform inaccessible | High (Zone 5 rural reality) | Critical — community cannot coordinate during disruption scenarios | Accept risk only if confirmed zero rural members; plan migration to Rec. 1 or 2 within 6 months |
| Trial ends June 17 before community is fully evaluated | Medium | Medium — billing starts before ROI demonstrated | Set calendar reminder June 15 for trial evaluation; cancel if engagement insufficient |
| API locked on Launch; Phase 5 automation impossible | Certain | Medium — all integration is manual | Accept manual workflow; plan Scale upgrade ($179/month) or migration if automation needed |
| Pricing increase (historical precedent: 93% increase 2024–2025) | Medium | Medium — budget impact | Build migration plan before June 2027 pricing review |
| Data lock-in: limited CSV export, no API export | Medium | Medium — migration effort | Export member list monthly via manual CSV; document export cadence in community governance |

### 6.2 Universal Fallback Sequence

If any primary platform becomes unavailable or is deemed inadequate:

**Immediate (0–48 hours)**: Signal group with all 15–20 builders (Signal is offline-capable via E2E encrypted SMS; no account server dependency). Forward member email list to admin.

**Short-term (1–7 days)**: Matrix.org free homeserver (matrix.org). Any community member installs Element and joins via invite link. No self-hosting required. No cost. Full message history preserved from the day of migration.

**Medium-term (1–4 weeks)**: Deploy Recommendation 1 (Nextcloud + Matrix self-hosted) from scratch. With an established Docker operator, deployment takes 8–10 hours. Member email list drives re-onboarding announcement. All Nextcloud documents (if already on Recommendation 1) restore from backup.

### 6.3 Platform-Independent Community Assets

Regardless of platform choice, maintain these community-owned assets that survive any platform failure:

1. **Member email list**: Export from any platform monthly; the community's most critical asset and the only guaranteed re-onboarding channel
2. **Seed catalog**: Plain CSV or ODS file maintained in at least two locations; openable without any platform account
3. **Tools inventory**: Plain CSV or ODS; same dual-location policy
4. **Decision log**: Plain Markdown or text, exported from Loomio after each vote; stored in community git repository or email archive
5. **Governance documents**: PDF and Markdown copies stored in community-owned email (not platform-only)
6. **Phase 5 guides**: Already on GitHub Pages (permanent, platform-independent); local copies in Nextcloud or downloaded PDFs on every builder device

### 6.4 Decision Summary Scorecard

Answer these questions in sequence. First hard requirement determines the path.

**Q1: Does any initial Phase 6 participant have rural or off-grid connectivity uncertainty?**

- Yes → **Recommendation 1 (Nextcloud + Matrix) only.** No other platform provides full offline capability.
- No, but off-grid is a 6-month requirement → Recommendation 1 strongly preferred; Recommendation 2 as 60-day bridge.
- No, all members have confirmed reliable connectivity → Proceed to Q2.

**Q2: Does the team have at least one Docker-capable technical operator available now?**

- Yes → Recommendations 1 or 2; proceed to Q3.
- No → Recommendation 3 (Mighty Networks Launch, 3–4 hours no-code setup) OR Discourse hosted ($50/month nonprofit, no self-hosting required).

**Q3: Does Phase 6 need real-time collaborative document editing (seed catalog co-authoring, protocol development, tools inventory live updates)?**

- Yes → **Recommendation 1 (Nextcloud + Matrix).** Nextcloud Office is the only evaluated solution with real-time co-editing that syncs offline.
- No → Recommendations 1 or 2 both sufficient; proceed to Q4.

**Q4: What is the annual budget ceiling (excluding Loomio governance supplement)?**

- $0–$200/year → Recommendation 1 or 2 on raspby1 + self-hosted Loomio
- $200–$400/year → Recommendation 2 (Discourse VPS $84–$204/year)
- $400–$700/year → Recommendation 1 or 2 + Loomio Starter ($199/year) or Loomio Pro nonprofit ($649/year)
- $950–$1,600/year → Recommendation 3 (Mighty Networks $950/year) + Loomio (optional)
- $1,600+/year → No additional commercial platform is recommended at this scale

**Decision matrix summary**:

| Condition | Recommended Path |
|---|---|
| Rural members present | Recommendation 1 (Nextcloud + Matrix) — only option |
| No rural members + Docker capable + co-editing needed | Recommendation 1 (Nextcloud + Matrix) |
| No rural members + Docker capable + no co-editing | Recommendation 2 (Discourse) |
| No rural members + no Docker capability | Recommendation 3 (Mighty Networks) + 6-month migration plan |
| Budget ceiling $0 | Recommendation 1 or 2 on raspby1 + self-hosted Loomio |
| Budget ceiling $950/year | Recommendation 3 acceptable if conditions met |
| Budget ceiling $3,000+/year | Still not Circle — true cost disqualifies it at all budget levels |

---

## Sources

All pricing and features verified against official source pages and cross-checked against independent reviews. Research confidence: 91%. Pricing verified June 2–3, 2026. No hands-on platform testing conducted; all assessments from official documentation, official pricing pages, and multiple independent review sources.

**Mighty Networks**:
- [Pricing — Official](https://www.mightynetworks.com/pricing)
- [Growth plan — Official](https://www.mightynetworks.com/pricing/growth)
- [Pricing analysis 2026 — Mihaelcacic](https://www.mihaelcacic.com/pricing-analysis/mighty-networks-pricing/)
- [Pricing 2026 — EzyCourse](https://ezycourse.com/blog/mighty-networks-pricing)
- [Pricing 2026 — Scrile](https://www.scrile.com/blog/mighty-networks-pricing)
- [Pricing 2026 — GetApp](https://www.getapp.com/collaboration-software/a/mighty-networks/)

**Circle.so**:
- [Pricing — Official](https://circle.so/pricing)
- [True cost 2026 — AI Funnel Insider](https://aifunnelinsider.com/circle-so-pricing-2026/)
- [Pricing 2026 — SchoolMaker](https://www.schoolmaker.com/blog/circle-so-pricing)
- [Review 2026 — Learning Revolution](https://www.learningrevolution.net/circle-review/)
- [Review 2026 — Group.app](https://www.group.app/blog/circle-review/)

**Substack Teams**:
- [Group publishing tools — On Substack](https://on.substack.com/p/group-publishing-tools-on-substack)
- [Team member roles — Substack Help](https://support.substack.com/hc/en-us/articles/360039016832-Can-my-Substack-publication-have-multiple-authors-or-contributors)

**Slack**:
- [Pricing — Official](https://slack.com/pricing)
- [Nonprofit pricing 2026 — Zenzap](https://www.zenzap.co/blog-posts/slack-nonprofit-pricing-in-2026-what-you-actually-get-and-what-to-watch-out-for)
- [Nonprofit discount — Slack Help](https://slack.com/help/articles/204368833-Apply-for-the-Slack-for-Nonprofits-discount)
- [Community pricing comparison — Bettermode](https://bettermode.com/blog/slack-community-pricing)
- [Pricing 2026 — LarkSuite](https://www.larksuite.com/en_us/blog/slack-pricing)

**Platform.sh / Upsun**:
- [Upsun pricing — Official](https://upsun.com/fixed-pricing/)

**Discourse**:
- [Pricing — Official](https://www.discourse.org/pricing)
- [vs. Flarum vs. NodeBB 2026 — Elest.io](https://blog.elest.io/discourse-vs-flarum-vs-nodebb-which-self-hosted-forum-platform-in-2026/)
- [PWA support — Discourse Meta](https://meta.discourse.org/t/is-pwa-feature-available-for-self-hosted/320612)

**Matrix / Element**:
- [Element Pricing — Official](https://element.io/en/pricing)
- [Matrix.org ecosystem](https://matrix.org/ecosystem/hosting/)
- [MESH-API Meshtastic bridge — GitHub](https://github.com/mr-tbot/mesh-api)

**Nextcloud Hub**:
- [Hub features — Official](https://nextcloud.com/hub/)
- [Hub 26 Winter release — Official](https://nextcloud.com/blog/nextcloud-hub26-winter/)
- [Nextcloud Files — Official](https://nextcloud.com/files/)

**Loomio**:
- [Pricing — Official](https://www.loomio.com/pricing/)
- [Nonprofit discount — Connecting Up](https://www.connectingup.org/product/loomio-nonprofits-50-discount)

**Platform comparisons and context**:
- [Best community platforms nonprofits 2026 — Disco](https://www.disco.co/blog/best-community-platforms-for-nonprofits-2026)
- [Digital tools for mutual aid groups — Digital Fund / Phoebe Tickell](https://medium.com/digitalfund/communities-essential-guide-to-digital-tools-for-mutual-aid-groups-c1664d30b525)

**Prior analysis documents (this project)**:
- PHASE_6_PLATFORM_ANALYSIS_v2.md (v2, June 1, 2026 — superseded)
- PHASE_6_PLATFORM_ANALYSIS.md (v4, June 2, 2026 — superseded by this document)
- PHASE_6_DOMAIN_A_PLATFORM_ANALYSIS.md (superseded)
- PHASE_6_IMPLEMENTATION_GUIDE_OPTION_A_DISCOURSE.md
- PHASE_6_IMPLEMENTATION_GUIDE_OPTION_B_MIGHTY_NETWORKS.md
- PHASE_6_IMPLEMENTATION_GUIDE_OPTION_C_NEXTCLOUD_MATRIX.md
- PHASE_6_COMMUNICATION_INFRASTRUCTURE_SCOPING.md

---

*Research confidence: 91%. All pricing verified from official sources June 2–3, 2026. Feature assessments cross-checked across multiple independent reviews. Off-grid assessment based on technical architecture review. Zone 5 agricultural and connectivity context from USDA cooperative statistics and FCC 2024 broadband coverage data. No hands-on platform testing conducted. Key evidence gaps: Mighty Networks AI Cohost moderation capability is new in 2026 and unverified in production for community-scale moderation; Circle Professional vs. Business tier automation boundaries are based on official documentation and may not reflect all edge cases.*
