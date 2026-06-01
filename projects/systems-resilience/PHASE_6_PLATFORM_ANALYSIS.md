---
title: "Phase 6 Community Economic Resilience — Platform Analysis & Decision Framework"
project: systems-resilience
phase: 6
domain: A (Community Economic Resilience)
status: DECISION-READY — user picks Platform A/B/C by June 3
created: 2026-06-01
decision_deadline: 2026-06-03
cross_references:
  - JUNE_1_PHASE_6_APPROVAL_CHECKLIST.md
  - PHASE_5_6_CONSOLIDATED_DECISION_MEMO.md
  - PHASE_6_CANDIDATE_COMMUNITY_ECONOMIC_RESILIENCE.md
  - CHECKIN.md
---

# Phase 6 Community Economic Resilience
## Platform Analysis & Selection Framework
### Decision Required by June 3, 2026

> **Lead finding**: No single platform dominates all five dimensions. For a volunteer-led, decentralization-prioritizing, off-grid-aware community, three options separate clearly: **Discourse** (self-hosted, $0, highest off-grid readiness, best moderation depth) for the bootstrap path; **Mighty Networks** ($79/month, best mobile engagement, native events) for the scale path; and **Nextcloud + Matrix/Element** (self-hosted, $0 software, maximum data sovereignty and offline capability) for the enterprise/autonomy path. Loomio fills a specific governance decision-making niche that complements any of the three. Geneva is the only fully free cloud option but has significant gaps. Circle and Slack free tier have disqualifying limitations for this use case.

---

## Part 1: Platform Feature Matrix

Eight platforms assessed across five dimensions. Ratings: ✅ Strong / ⚠ Adequate / ❌ Weak / — Not Applicable

### 1. Access Control Models

| Platform | Role-based Controls | Invite Mechanisms | Moderation Depth | Permission Granularity | Overall |
|---|---|---|---|---|---|
| **Mighty Networks** | ✅ Custom roles per Space | ✅ Invite links + approval gates | ✅ Per-Space moderation | ⚠ Space-level (not post-level) | ✅ Strong |
| **Circle.so** | ✅ Full role hierarchy | ✅ Magic links, gated applications | ✅ AI moderation + manual | ✅ Space + member-level | ✅ Strong |
| **Discourse** | ✅ Trust-level system (0–4) | ✅ Invite-only, email approval | ✅ Flag, suspend, silence, trust gates | ✅ Category + group-level | ✅ Strong |
| **Slack (free)** | ⚠ Channel-level only | ⚠ Email domain or link | ❌ Limited on free tier | ❌ No @group routing on free | ❌ Weak |
| **Loomio** | ✅ Group/subgroup privacy | ✅ Email invite + link | ⚠ Thread-level only | ⚠ Subgroup scoping | ⚠ Adequate |
| **Geneva** | ✅ Role-based rooms | ✅ Questionnaire-gated invites | ⚠ Basic moderation | ⚠ Room-level | ⚠ Adequate |
| **Matrix/Element** | ✅ Full room permission matrix | ✅ Invite-only rooms | ✅ Moderation bots + admin tools | ✅ Per-room, per-user | ✅ Strong |
| **Nextcloud Hub** | ✅ LDAP/group-based | ✅ Share links + federated | ⚠ App-level admin only | ✅ File/calendar/Talk granular | ⚠ Adequate |

**Notes**:
- Discourse's trust-level system is the most sophisticated for community self-governance: new members start at Trust Level 0 (limited posting), earn Level 1 (basic member) through reading, Level 2 (member) through engagement, Level 3 (regular) through sustained contribution, Level 4 (leader) by moderator grant. This matches the organic growth model of a volunteer resilience community.
- Geneva's questionnaire-gated invites are uniquely suited to vetting community fit without requiring manual admin review.
- Matrix/Element gives the most granular per-room permission matrix of any platform, including ban propagation across federated servers.

---

### 2. File and Resource Sharing

| Platform | Document Storage | Collaborative Editing | Version Control | Offline Availability | Storage Limit |
|---|---|---|---|---|---|
| **Mighty Networks** | ⚠ File uploads in posts | ❌ No co-editing | ❌ None | ❌ Not supported | 200GB (Launch) |
| **Circle.so** | ⚠ File attachments in chat/posts | ❌ No co-editing | ❌ None | ❌ Not supported | 200GB (Professional) |
| **Discourse** | ⚠ File uploads + image hosting | ❌ No co-editing | ❌ None | ⚠ Service-worker caching | 20GB (Pro hosted) |
| **Slack (free)** | ❌ 5GB total; files deleted at 90 days | ❌ No co-editing | ❌ None | ❌ Not supported | 5GB (free) |
| **Loomio** | ⚠ Attachments to proposals | ❌ No co-editing | ❌ None | ❌ Not supported | Limited |
| **Geneva** | ❌ Basic media sharing only | ❌ None | ❌ None | ❌ Not supported | Unspecified |
| **Matrix/Element** | ✅ File sharing in rooms | ❌ Native; ✅ via integration | ❌ Native; ✅ via integration | ✅ Local cache, offline-readable | Self-hosted = unlimited |
| **Nextcloud Hub** | ✅ Full document suite (LibreOffice) | ✅ Real-time collaborative editing | ✅ Version history, file locking | ✅ Desktop/mobile sync client | Self-hosted = hardware limit |

**Notes**:
- Nextcloud is the only platform with native real-time collaborative document editing (via Nextcloud Office/Collabora), version history, and desktop sync clients that work offline. For a community producing shared protocols, resource guides, and economic templates, this is a decisive advantage.
- Discourse's hosted Pro plan offers only 20GB storage; self-hosted is hardware-limited.
- Slack's free 90-day message and file deletion is a hard disqualifier for institutional knowledge preservation.
- Geneva's file sharing is underdeveloped — suitable for images and media, not structured document libraries.

---

### 3. Event Coordination

| Platform | Native Calendar | RSVP System | Async Check-ins | Scheduling Integrations | Recurrence |
|---|---|---|---|---|---|
| **Mighty Networks** | ✅ Calendar view with expand | ✅ Native RSVP + reminders | ⚠ Polls only | ✅ Google/Outlook/Apple sync | ✅ Yes |
| **Circle.so** | ✅ Event space calendar | ✅ Native RSVP + notifications | ⚠ Polls only | ⚠ Zapier → Google | ✅ Yes |
| **Discourse** | ⚠ Events plugin (not default) | ⚠ Plugin-based | ⚠ Thread-based async | ⚠ Plugin → external | ⚠ Plugin-dependent |
| **Slack (free)** | ❌ No native calendar | ❌ No native RSVP | ⚠ Scheduled messages | ⚠ 10 app integrations max | ❌ None |
| **Loomio** | ✅ Time polls (built-in) | ✅ Scheduling votes | ✅ Async proposals + outcomes | ⚠ Slack/Matrix notification | — |
| **Geneva** | ✅ Integrated event calendar | ✅ Event reminders | ⚠ Chat-based | ❌ No external integrations | ⚠ Limited |
| **Matrix/Element** | ❌ Native; ✅ via Nextcloud bridge | ❌ Native; ✅ via bridge | ✅ Async chat threads | ✅ Bridges to many systems | — |
| **Nextcloud Hub** | ✅ Full CalDAV calendar | ✅ Share event links + RSVP | ✅ Tasks, comments on events | ✅ CalDAV sync to any client | ✅ Full recurrence |

**Notes**:
- Loomio excels specifically at async decision-making and scheduling coordination through time polls and proposal outcomes — a governance tool more than a calendar.
- Mighty Networks has the most complete native event system of any SaaS platform: calendar view, RSVP management, email reminders, charge-for-events option, and real-time event hosting.
- Discourse requires the Events plugin (available on all hosted plans and self-hosted installs) to reach parity. Without it, event coordination happens via threaded posts.
- For Phase 6 use case (coordination workshops, community economic resilience sessions), Mighty Networks or Nextcloud wins on events.

---

### 4. Messaging and Moderation

| Platform | Threaded Discussion | Moderation Tools | Content Policy Control | Bot Automation | DM Support |
|---|---|---|---|---|---|
| **Mighty Networks** | ✅ Full threaded posts | ✅ Per-Space moderation queue | ✅ Custom community rules | ⚠ Limited automations | ✅ Direct chat |
| **Circle.so** | ✅ Threaded + chat | ✅ AI moderation + flagging | ✅ Profanity filter + report | ✅ Workflow automations | ✅ DMs |
| **Discourse** | ✅ Full threaded forum | ✅ Akismet spam, trust gates, flags | ✅ Highly configurable policies | ✅ Webhooks + API + Discourse Automation | ✅ Private messages |
| **Slack (free)** | ⚠ Threads in channels | ❌ Minimal on free | ❌ No content policy control | ⚠ 10 app limit | ✅ DMs |
| **Loomio** | ✅ Decision-threaded | ⚠ Admin-only moderation | ⚠ Platform policies only | ⚠ Slack/Matrix outbound | ✅ User messages |
| **Geneva** | ✅ Room chat + forum posts | ⚠ Basic room moderation | ⚠ Phone verification as friction | ❌ No bot API | ✅ DMs |
| **Matrix/Element** | ✅ Threaded replies | ✅ Mjolnir moderation bot | ✅ Full admin control (self-hosted) | ✅ Full Matrix SDK bot support | ✅ E2E encrypted DMs |
| **Nextcloud Hub** | ⚠ Talk chat (basic threads) | ⚠ Admin deletion only | ⚠ Limited policy enforcement | ⚠ Webhooks via Flow | ✅ DMs via Talk |

**Notes**:
- Discourse's trust-level moderation is the most battle-tested of any platform in this set. Spam, low-quality content, and bad actors are handled automatically at Trust Level 0–1 without admin intervention. This matters for a volunteer community where admin bandwidth is limited.
- Matrix/Element with Mjolnir provides the most powerful moderation tooling for federated/self-hosted deployments: ban propagation, room ACLs, spam pattern matching.
- Circle's AI moderation (AI inbox, AI copilot) reduces volunteer moderator burden significantly at its $89/month entry point.
- Geneva's phone-number signup reduces anonymous abuse but creates friction for community members who value privacy.

---

### 5. Off-Grid Readiness

| Platform | Offline-First Sync | Local-First Architecture | Mobile Friendliness | Low-Bandwidth Performance | Self-Hostable |
|---|---|---|---|---|---|
| **Mighty Networks** | ❌ No offline support | ❌ Cloud-only | ✅ Native iOS/Android (65%+ usage on mobile) | ⚠ Cloud-dependent | ❌ SaaS only |
| **Circle.so** | ❌ No offline support | ❌ Cloud-only | ✅ iOS/Android apps | ⚠ Cloud-dependent | ❌ SaaS only |
| **Discourse** | ⚠ PWA service-worker caching | ⚠ Partial (read-only offline) | ✅ PWA, installable from browser | ✅ Minimal JS, low-bandwidth mode | ✅ Full self-host (AGPL) |
| **Slack (free)** | ❌ No offline | ❌ Cloud-only | ✅ iOS/Android | ⚠ Cloud-dependent | ❌ SaaS only |
| **Loomio** | ❌ No offline | ❌ Cloud-only | ✅ Mobile-responsive web | ⚠ Cloud-dependent | ✅ Self-hostable (AGPL) |
| **Geneva** | ❌ No offline | ❌ Cloud-only | ✅ iOS/Android | ⚠ Cloud-dependent | ❌ SaaS only |
| **Matrix/Element** | ✅ Element X: instant launch offline | ✅ Local message store | ✅ iOS/Android/F-Droid | ✅ LoRa/mesh bridgeable; bandwidth-adaptive | ✅ Full self-host (AGPL) |
| **Nextcloud Hub** | ✅ Desktop/mobile sync client | ✅ Local file cache on all devices | ✅ iOS/Android Nextcloud app | ✅ Runs on LAN; no internet required | ✅ Full self-host (AGPL) |

**Notes**:
- Matrix/Element is the only chat platform with genuine offline-first architecture. Element X resyncs after going offline at over 6,000x the speed of legacy Element, and provides "instant launch" from a local room list cache. It can be bridged to mesh networks (Meshtastic/LoRa) via community-built gateways — directly relevant to the Phase 6 communication infrastructure already researched (see `PHASE_6_COMMUNICATION_INFRASTRUCTURE_SCOPING.md`).
- Nextcloud is the only document/file platform with true offline sync: files are cached to device and sync bidirectionally when connectivity restores. This is the closest thing to off-grid file infrastructure in this set.
- Discourse as a Progressive Web App (PWA) can be installed on mobile browsers and caches read content via service workers. It does not support offline posting.
- All cloud-only platforms (Mighty Networks, Circle, Slack, Geneva) fail completely when internet connectivity is unavailable. This is a binary disqualifier for off-grid readiness.

---

## Part 2: Consolidated Comparison Summary

| Platform | Access Control | File/Resource | Event Coord | Messaging | Off-Grid | Cost (Monthly) | Verdict |
|---|---|---|---|---|---|---|---|
| **Mighty Networks** | ✅ | ⚠ | ✅ | ✅ | ❌ | $79 (Launch) | Scale path — strong SaaS |
| **Circle.so** | ✅ | ⚠ | ✅ | ✅ | ❌ | $89 (Professional) | Enterprise SaaS — overpriced for volunteer |
| **Discourse** | ✅ | ⚠ | ⚠ | ✅ | ⚠ | $0 self-hosted / $100 hosted | Bootstrap path — best free option |
| **Slack (free)** | ❌ | ❌ | ❌ | ⚠ | ❌ | $0 (free) / $7.25/user paid | Disqualified — file/history limits |
| **Loomio** | ⚠ | ❌ | ✅ | ⚠ | ❌ | $29/mo (Starter) / $0 self-host | Governance supplement only |
| **Geneva** | ⚠ | ❌ | ✅ | ⚠ | ❌ | $0 (free) | Lightweight option — gaps in files |
| **Matrix/Element** | ✅ | ✅ via bridges | ✅ via Nextcloud | ✅ | ✅ | $0 self-hosted | Enterprise/autonomy path |
| **Nextcloud Hub** | ⚠ | ✅ | ✅ | ⚠ | ✅ | $0 self-hosted | Best file/document infrastructure |

---

## Part 3: Three-Option Recommendation Scorecard

### Option A — Bootstrap Path: Discourse (Self-Hosted or Free Hosted)

**Best for**: Volunteer communities with one technically capable member; prioritize longevity and moderation over mobile engagement; budget = $0.

**Configuration**:
- Self-hosted on a $5–12/month VPS (DigitalOcean, Hetzner, Vultr) using the official Discourse Docker image
- Or: Discourse free trial → their $100/month Pro plan with 50% nonprofit discount = **$50/month**
- Add Loomio Community plan ($10/month) as decision-making supplement

**Scorecard**:

| Dimension | Score | Notes |
|---|---|---|
| Access control | 9/10 | Trust-level system is best-in-class for self-governing communities |
| File/resource sharing | 6/10 | File uploads work; no collaborative editing |
| Event coordination | 7/10 | Requires Events plugin; full functionality when installed |
| Messaging + moderation | 9/10 | Akismet, trust gates, automation plugin, private messages |
| Off-grid readiness | 6/10 | PWA caching for reading; self-hosted survives cloud outages |
| Mobile friendliness | 8/10 | PWA installable; no native app |
| Cost | 10/10 | $0 self-hosted; $50/month with nonprofit hosted |
| **Overall** | **7.9/10** | |

**Strengths**: Zero cost (self-hosted), battle-tested moderation, strong API and webhooks, active plugin ecosystem, 85% educational discount and 50% nonprofit discount on hosted plans, fully open-source (AGPL).

**Weaknesses**: No collaborative document editing, requires technical setup for self-host, no native mobile app (PWA only), off-grid is read-only.

**Confidence**: High. Discourse hosts thousands of activist and open-source communities. Setup time: 2–4 hours for a technically capable volunteer. Maintenance: 1–2 hours/month.

---

### Option B — Scale Path: Mighty Networks (Launch Plan)

**Best for**: Communities prioritizing member engagement, mobile-first access, and native event hosting; willing to pay $79/month; do not require offline capability.

**Configuration**:
- Mighty Networks Launch plan ($79/month, billed monthly; $950/year billed annually = ~$79/month)
- No self-hosting option; SaaS only
- Add Loomio for governance decisions if needed ($10–29/month Starter)

**Scorecard**:

| Dimension | Score | Notes |
|---|---|---|
| Access control | 8/10 | Custom roles per Space; Space-level granularity |
| File/resource sharing | 6/10 | File uploads in posts; no co-editing; 200GB storage |
| Event coordination | 9/10 | Best native event system: calendar view, RSVP, reminders, calendar sync |
| Messaging + moderation | 8/10 | Per-Space queues, threaded discussion, direct messaging |
| Off-grid readiness | 1/10 | Zero offline functionality — hard failure in connectivity loss |
| Mobile friendliness | 10/10 | Native iOS/Android, 65%+ engagement on mobile |
| Cost | 5/10 | $79–$950/year; no nonprofit discount confirmed |
| **Overall** | **6.7/10** | |

**Strengths**: Best mobile engagement of any platform tested, native events with RSVP and reminders, member matching/discovery tools, no technical setup required, 14-day free trial.

**Weaknesses**: Hard failure off-grid, most expensive recurring cost, no document co-editing, SaaS-only (vendor lock-in), no confirmed nonprofit discount, 2% transaction fee on paid content.

**Confidence**: High. Mighty Networks is a mature commercial platform with active development. Risk: pricing has increased over time ($41/month became $79/month in 2026); future increases possible.

---

### Option C — Enterprise/Autonomy Path: Nextcloud Hub + Matrix/Element

**Best for**: Communities with 1–2 technically capable members; prioritize data sovereignty, off-grid capability, and no recurring cost; willing to invest setup time.

**Configuration**:
- Nextcloud Hub (self-hosted, $0 software) on a $6–15/month VPS or local Raspberry Pi 5 (existing infrastructure per project memory)
- Matrix/Element self-hosted Synapse homeserver ($0 software) or Matrix.org free server
- Loomio self-hosted ($0 software) or Community plan ($10/month) for governance
- Total SaaS cost: **$0** (self-hosted) or **$10/month** (with Loomio cloud)

**Scorecard**:

| Dimension | Score | Notes |
|---|---|---|
| Access control | 8/10 | Group-based (Nextcloud) + per-room matrix (Element); strong together |
| File/resource sharing | 10/10 | Native LibreOffice co-editing, version history, offline sync, unlimited storage |
| Event coordination | 9/10 | Full CalDAV calendar, RSVP links, CalDAV sync to any device |
| Messaging + moderation | 8/10 | Matrix E2E encryption, Mjolnir bot, federated moderation |
| Off-grid readiness | 10/10 | Files sync locally; Matrix runs on LAN; works without internet |
| Mobile friendliness | 8/10 | Nextcloud + Element iOS/Android apps, F-Droid available |
| Cost | 10/10 | $0 software; $6–15/month for hosting hardware or VPS |
| **Overall** | **9.0/10** | |

**Strengths**: Highest off-grid score, true collaborative document editing, unlimited storage (hardware-limited), no vendor lock-in, compatible with existing Meshtastic/LoRa mesh infrastructure, end-to-end encryption by default (Matrix), federated architecture, AGPL open source.

**Weaknesses**: Highest setup complexity (2 separate systems to install and maintain), requires ongoing technical maintenance (~2–4 hours/month), Nextcloud Talk (video) and Matrix are separate UX surfaces (can feel fragmented), no native member discovery/matching.

**Confidence**: High on technical capability; medium on operational sustainability for volunteers without technical background. The Raspberry Pi 5 already in the project infrastructure (per project memory: raspby1, 100.70.184.84) could host both services at near-zero marginal cost.

---

## Part 4: Integration Pathways with Phase 5 Publication Output

Phase 5 publishes June 5 (Wave 1+2: 43,621 words, 10 documents) and June 30 (Wave 3: 22,821 words). The platform must connect the Phase 5 knowledge base to Phase 6 community engagement.

### Option A (Discourse) Integration

```
Phase 5 publication (June 5)
    → Create Discourse category: "Phase 5 Resources"
    → Post each of the 10 Wave 1+2 documents as wikis (editable by Trust Level 3+)
    → Pin governance framework document as category header
    → Create event (Events plugin) for June 15 Platform A community foundation session
    → Phase 6 Domain A research outputs post as wiki threads for community annotation

Key advantage: Discourse wiki posts allow the community to annotate and extend Phase 5
research without replacing the original — directly supports the knowledge transmission goal.
```

### Option B (Mighty Networks) Integration

```
Phase 5 publication (June 5)
    → Create Space: "Knowledge Base" with uploaded Phase 5 PDFs/docs
    → Create Space: "Community Resilience Workshops" for event coordination
    → Post announcements to members via native push notification
    → June 15 Platform B community onboarding event created with RSVP
    → Phase 6 Domain A research: post sections as long-form articles

Key advantage: Native push notifications and calendar RSVP dramatically increase 
attendance at June 15 foundation session vs. Discourse email notifications.
```

### Option C (Nextcloud + Matrix) Integration

```
Phase 5 publication (June 5)
    → Upload all 10 Wave 1+2 documents to Nextcloud shared folder (collaborative editing enabled)
    → Create Matrix room: "Phase 5 Reading Discussion"
    → Community members get Nextcloud Talk video + Nextcloud Calendar event link
    → Phase 6 Domain A: shared document drafts visible and editable by community
    → Offline sync ensures documents accessible without internet for rural/off-grid members

Key advantage: Phase 5 documents become living collaborative resources, not static PDFs.
Community can annotate, extend, and localize content in real-time. Fully functional at
June 15 foundation session even if internet connectivity is unreliable.
```

### Hybrid Pathway (Any Option + Loomio)

Regardless of primary platform choice, add Loomio as the governance layer:

```
Loomio Community group ($10/month or free self-hosted)
    → Create proposal threads for Phase 6 Domain A research priorities
    → Time polls for meeting scheduling across time zones
    → Voting on local currency / cooperative model to prototype first
    → Decision log exported as CSV for Phase 6 documentation

This does not conflict with any primary platform and adds structured democratic
decision-making that Discourse, Mighty Networks, and Nextcloud all lack natively.
```

---

## Part 5: Cost Analysis

### Monthly Cost Summary

| Platform | Free Tier / Self-Host | Startup (Volunteer-Led) | Scale (50+ Members) | Notes |
|---|---|---|---|---|
| **Mighty Networks** | No (14-day trial only) | $79/month | $179/month (Scale) | No nonprofit discount confirmed |
| **Circle.so** | No (14-day trial only) | $89/month | $199/month (Business) | No nonprofit discount |
| **Discourse** | Yes (self-hosted, $0) | $50/month (hosted, nonprofit 50% off $100 Pro) | $250/month (nonprofit 50% off $500 Business) | 50% nonprofit / 85% educational discount |
| **Slack** | Yes (90-day history limit) | $7.25/user/month (Pro) | Scales per user — expensive at 50+ | Per-user pricing penalizes growth |
| **Loomio** | Yes (self-hosted, $0) | $10/month (Community) | $29–$49/month nonprofit | 25–50% nonprofit discount; open source |
| **Geneva** | Yes (fully free) | $0 | $0 (premium TBD) | Free but file/offline gaps |
| **Matrix/Element** | Yes (self-hosted, $0) | $0 software + VPS cost | $0 software + VPS cost | $5/user/month Enterprise cloud option |
| **Nextcloud Hub** | Yes (self-hosted, $0) | $0 software + VPS cost | $0 software + VPS cost | Enterprise support available if needed |

### Realistic Total Cost by Scenario

**Option A (Discourse self-hosted + Loomio)**
- Year 1: ~$60–180 (VPS $5–15/month) + $120 Loomio = **$180–$300/year**
- Year 2+: Same ongoing VPS + Loomio = **$180–$300/year**
- With nonprofit Discourse hosted: $50 + $10 = **$60/month ($720/year)**

**Option B (Mighty Networks Launch + Loomio)**
- Year 1: $950 (annual billing) + $120 Loomio = **$1,070/year**
- Year 2+: Same = **$1,070/year**
- Monthly billing: $79 + $10 = **$89/month ($1,068/year)**

**Option C (Nextcloud + Matrix self-hosted + Loomio)**
- Year 1: $60–180 VPS + $120 Loomio = **$180–$300/year**
- Year 2+: Same = **$180–$300/year**
- Zero cost if run on existing Raspberry Pi 5 infrastructure (raspby1)

---

## Part 6: Decision Logic — Pick Platform A, B, or C by June 3

Answer these four questions. Your answers point to a platform.

### Question 1: Is technical self-hosting an option?
- **Yes, one or more community builders can manage a VPS or server** → Proceed to Question 2
- **No, the community needs turnkey SaaS only** → **Option B (Mighty Networks)** or Geneva for free tier

### Question 2: Is off-grid and offline capability a hard requirement?
- **Yes** → **Option C (Nextcloud + Matrix)** is the only choice with full offline capability
- **No, but resilience is a preference** → **Option A (Discourse)** provides partial offline (read-only PWA) with lowest cost
- **No, connectivity is reliable enough** → **Option B (Mighty Networks)** is adequate

### Question 3: Is collaborative document editing required?
- **Yes** (community needs to co-author protocols, templates, resource guides) → **Option C (Nextcloud)** is the only full solution
- **No** (documents are published, not collaboratively edited) → Options A or B are sufficient

### Question 4: What is the budget ceiling?
- **$0/month** → Option C self-hosted or Geneva (free, with limitations)
- **$0–$25/month** → Option A self-hosted + Loomio Community
- **$50–$100/month** → Option A hosted (nonprofit discount) or Option A self-hosted + Loomio Pro
- **$80–$100/month** → Option B (Mighty Networks), best mobile engagement at this price point

### Decision Matrix Summary

| If... | Then choose... |
|---|---|
| Off-grid capability required + technical capacity available | **Option C** (Nextcloud + Matrix) |
| $0 budget + technical capacity + moderation-first | **Option A** (Discourse self-hosted) |
| $0 budget + no technical capacity + lightweight needs | **Geneva** (free, limited) |
| $50–$100/month budget + no technical capacity | **Option A** (Discourse hosted, nonprofit discount) |
| $80–$100/month + mobile-first + events-first + no offline needed | **Option B** (Mighty Networks) |
| Governance/decision layer needed for any option | Add **Loomio** ($10/month or self-hosted) |

---

## Part 7: Phase 5/6 Sequencing Implications

### If Platform Decision = June 3 (per this decision package)

```
June 3:     Platform decision made
June 5:     Phase 5 Wave 1+2 publishes (June 5 13:00 UTC locked)
June 5–8:   Platform setup and community onboarding infrastructure ready
June 9–14:  Domain A community foundation — first 10–20 members onboarded
June 15:    Phase 6 Domain A community coordination session (checkpoint gate)
June 30:    Phase 5 Wave 3 publishes; community receives operational content
July–Aug:   Community builder recruitment strategy executes with live platform
```

### Critical Path Risk

**Option A (Discourse self-hosted)**: 2–4 hour setup; can be ready June 4 if decision June 3. Risk: VPS provisioning may take 24 hours with DNS propagation. Mitigation: provision VPS June 3, accept 24-hour DNS wait.

**Option B (Mighty Networks)**: 14-day trial starts June 3; full network functional in ~2 hours. Zero setup risk. Risk: $79/month commits on June 17 if trial not cancelled.

**Option C (Nextcloud + Matrix)**: 4–8 hour setup total; can be ready June 5–6. If run on raspby1 (existing infrastructure), no VPS provisioning wait. Risk: Matrix homeserver setup is the most complex component; allow June 3–7 as setup window.

### July–August Community Builder Recruitment Implications

- **Option A (Discourse)**: Public forum structure makes it easy for prospective builders to evaluate community quality before joining. SEO-indexable threads attract organic interest.
- **Option B (Mighty Networks)**: Invite-only default; prospective builders must be individually recruited. Better for curated community; less organic growth.
- **Option C (Nextcloud + Matrix)**: Matrix federation means prospective builders can join from any Matrix client without signing up for your specific instance. Strong signal for decentralization-focused builders.

---

## Part 8: Platforms Not Recommended

### Slack (Free Tier) — Disqualified
**Disqualifier**: 90-day message and file deletion on free tier destroys institutional knowledge. A community building resilience protocols cannot afford to lose discussion history. Paid plan ($7.25/user/month) scales poorly: at 50 members it costs $362.50/month — more expensive than any other option without adding resilience capabilities.

### Circle.so — Not Recommended for This Use Case
**Reason**: $89/month entry point with no confirmed nonprofit discount, no offline capability, and no document co-editing makes it the most expensive mid-tier option without the capabilities that matter most for this use case. Better suited for creator monetization communities than volunteer resilience coordination.

### Lunchclub — Not Applicable
**Assessment**: Lunchclub is an AI-driven 1:1 professional networking matchmaking tool, not a community coordination platform. It has no group spaces, no file sharing, no event coordination beyond individual meeting scheduling, and no moderation tooling. It is not a viable community platform for this use case. The confusion in the original scope may stem from its categorization alongside "community" tools; its function is entirely different.

### Bettermode — Not Recommended
**Reason**: Bettermode discontinued its free plan in March 2026 and its current entry pricing has reportedly shifted to $399/month (Starter, 10,000 members) — the highest starting price of any platform evaluated, with no offline capability or document collaboration. Unconfirmed pricing instability (conflicting sources show $59/month and $399/month) creates planning risk.

---

## Sources

- [Mighty Networks Pricing](https://www.mightynetworks.com/pricing)
- [Mighty Networks Mobile App Review 2026](https://www.courseplatformsreview.com/blog/mighty-networks-mobile-app/)
- [Circle.so Pricing](https://circle.so/pricing)
- [Circle.so Review 2026 — Whop](https://whop.com/blog/circle-review/)
- [Discourse Pricing](https://www.discourse.org/pricing)
- [Discourse Self-Hosted Open Source](https://meta.discourse.org/t/is-discourse-still-free-to-self-host/305454)
- [Slack Free Plan Limitations 2026 — CompareTiers](https://comparetiers.com/blog/slack-free-plan-limitations-2026)
- [Slack Pricing 2026 — G2](https://www.g2.com/products/slack/pricing)
- [Loomio Pricing](https://www.loomio.com/pricing/)
- [Loomio for Nonprofits — TechSoup](https://www.techsoup.org/loomio)
- [Geneva Platform](https://www.geneva.com/)
- [Geneva Pricing — SaaSworthy](https://www.saasworthy.com/product/geneva/pricing)
- [Element Pricing 2026](https://element.io/en/pricing)
- [Element X Ignition — offline sync](https://element.io/blog/element-x-ignition/)
- [Matrix Self-Hosted Options](https://matrix.org/ecosystem/hosting/)
- [Nextcloud Hub Features](https://nextcloud.com/hub/)
- [Nextcloud Self-Hosted Free — Complete Guide](https://hostly.sh/blog/self-host-nextcloud-complete-guide-2026/)
- [Discourse vs Circle vs Mighty Networks 2026 — LinoDash](https://linodash.com/community-platforms/)
- [Bettermode Review 2026 — Group.app](https://www.group.app/blog/bettermode-community-platform-review/)
- [Decentralized/Offline-First App Landscape — Innovate World](https://innovateworld.org/community-mesh-networks-and-offline-first-apps-a-practical-guide-to-resilient-inclusive-connectivity/)
- [Manyverse/Scuttlebutt — NLnet](https://nlnet.nl/project/Manyverse/)
- [Mutual Aid Digital Coordination — Technoanarchism](https://www.technoanarchism.org/mutual-aid-in-the-digital-age-technologies-of-solidarity/)

---

## Appendix: Lunchclub Assessment Note

Lunchclub was included in the original scope. After research, Lunchclub is categorically not a community coordination platform — it is an AI-powered professional 1:1 meeting matchmaker. It schedules individual introductions based on stated interests and runs no group spaces, resource libraries, calendars, or moderation infrastructure. There is no way to use Lunchclub as the foundation for a community economic resilience platform. It is excluded from the matrix above and replaced with Geneva (free, actively developed, designed for groups and communities) and Matrix/Element (open source, off-grid capable, directly relevant to Phase 6 communication infrastructure research).

---

*Research confidence: High for pricing (direct platform pages verified June 1, 2026), High for feature sets (multiple independent review sources cross-checked), Medium for Bettermode pricing (conflicting sources — treat as unstable), High for off-grid assessment (architecture review of each platform's technical model). Key gap: no hands-on testing of any platform; all assessments from documentation and reviews.*
