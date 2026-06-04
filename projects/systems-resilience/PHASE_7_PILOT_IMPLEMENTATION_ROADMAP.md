---
title: "Phase 7 Pilot Implementation Roadmap"
project: systems-resilience
phase: 7
status: DECISION-READY — platform selection gate June 3, 2026 EOD
created: 2026-06-03
revised: 2026-06-03
purpose: "Map actual community deployment of the chosen platform (Nextcloud+Matrix or Discourse) across a 6-month pilot cycle. Supports platform decision needed EOD today."
cross_references:
  - PHASE_6_PLATFORM_ANALYSIS.md
  - PHASE_6_IMPLEMENTATION_GUIDE_OPTION_A_DISCOURSE.md
  - PHASE_7_SCOPING_MEMO.md
  - phase-3/01-governance-decision-making.md
  - phase-3/02-food-systems-supply-chain.md
  - phase-3/03-information-infrastructure.md
  - phase-3/04-security-and-defense.md
  - phase-3/05-scaling-pathways-and-thresholds.md
word_count: ~3500
confidence: High on domain selection rationale and scaling structure; Medium on cost and timeline (community selection speed is the primary variable); Medium on adoption failure probabilities (draws on published research on mutual aid tech adoption).
supersedes: PHASE_7_PILOT_IMPLEMENTATION_ROADMAP.md (June 3 initial draft)
---

# Phase 7 Pilot Implementation Roadmap
## Systems Resilience — Community Deployment, Month 1–6

**Prepared**: June 3, 2026 (revised)
**Decision context**: Phase 6 platform analysis complete. User deciding between Nextcloud+Matrix (9.5/10) and Discourse (8.0/10) by EOD today. This roadmap maps the 6-month pilot for either platform selection, and provides the domain and community-size analysis needed to make the pilot design decision alongside the platform decision.

**The question this document answers**: Once the platform is chosen, what does it take — in time, money, community relationships, and governance structure — to go from "corpus and platform recommendation" to "a real community is running it and generating validated learning"?

---

## 1. Pilot Domain Selection: Why Governance First

Of the five Phase 3 community-scale domains — governance and decision-making, food systems and supply chain, information infrastructure, security and defense, and scaling pathways — **governance is the correct first pilot domain**.

The reasoning is structural, not preferential. Every other domain depends on governance being operational first. Food distribution protocols require a community assembly that can allocate equitably. Information infrastructure requires someone with authority to make channel assignments and enforce protocols. Security postures require accountability mechanisms. The Phase 3 governance document states this dependency explicitly: governance is the load-bearing structure beneath every other domain, and it cannot be retrofitted once social trust fractures.

A pilot that starts with food systems or information infrastructure will produce data about what hardware and protocols work. A pilot that starts with governance produces data about what actually determines whether communities can act collectively — which is the dependency on which all other domains rest.

**The specific governance mechanism**: The delegate council model documented in `phase-3/01-governance-decision-making.md` at the 100–500 person scale. The platform — whichever is selected — implements the "institutional memory" infrastructure that Phase 3 identifies as the critical missing element when communities cross the 150-person Dunbar threshold: offline-accessible decision records, real-time delegate communication, shared resource inventories, and assembly scheduling.

**Domains deferred to Gate 2**: Food systems (Phase 3 Domain 2) and information infrastructure (Phase 3 Domain 3) are the natural Gate 2 expansions. Food systems requires working governance before resource allocation functions are feasible. Information infrastructure adds the off-grid communication layer (Meshtastic mesh, GMRS radio) that supplements but does not replace the primary platform. Security and scaling pathways are Gate 3 work — they require the first two domains to be operational before they are legible to the community.

---

## 2. Community Size and Type: Three Scenarios

### Scenario A — Small Mutual Aid Network (50–100 members)

**Profile**: A Zone 5 mutual aid organization operating for 12+ months, covering food distribution, emergency coordination, or resource sharing within a single neighborhood or rural township.

**Strengths for pilot purposes**:
- Social trust is high at this scale; informal relationships supplement formal governance structures during learning friction
- Platform setup failures and governance missteps are absorbed without community fracture
- Onboarding is achievable in 2–3 weeks with async support
- Qualitative learning is rich: at 50–100 people, it is possible to interview most members in Month 6 evaluation

**Weaknesses**:
- At this scale, informal coordination naturally works — the formal delegate council and platform infrastructure may produce friction without proportionate benefit, making it hard to demonstrate the governance value proposition
- Data from a 50-person community does not transfer cleanly to the 200–500 person communities that represent the most significant scaling challenge
- Risk: the community may not actually need the platform, and data from a low-need context overstates ease of adoption

**Assessment**: Appropriate as a fallback if no 80–150 person community can be confirmed by July 15. Produces valid platform usability data but limited governance necessity data. If selected, treat as a "platform validation" pilot rather than a "governance necessity" pilot.

### Scenario B — Town-Scale or Regional Mutual Aid Network (80–200 members) — RECOMMENDED

**Profile**: A rural cooperative, mutual aid network, or intentional community with 80–150 active members, weekly coordination needs, and documented coordination friction (lost decisions, unclear resource allocation, over-dependence on one primary organizer).

**Strengths for pilot purposes**:
- This is the exact scale at which the Phase 3 Dunbar threshold applies: too large for pure informal coordination, small enough that social trust can absorb early platform and governance failures
- The delegate council model is genuinely needed at this scale — governance structures are not bureaucratic overhead but a practical coordination necessity
- Data transfers well to the 100–500 person communities that the corpus is calibrated for
- Zone 5 extension service and cooperative development networks have strong concentrations of organizations in this size range

**Weaknesses**:
- Community selection takes longer: the 12+ months operational requirement and governance gap requirement rule out many candidates
- Technical onboarding takes 3–5 weeks (vs. 2–3 for Scenario A) due to the larger membership

**Assessment**: The primary target for Gate 1. This is the community type for which Phase 3 governance frameworks are calibrated and for which the platform comparison was conducted.

### Scenario C — Town or Watershed District (1,000+ members)

**Profile**: A small town civic organization, a watershed council, or a multi-township cooperative federation operating at 1,000–10,000 person scale.

**Strengths**: Scale diversity; more representative of governance challenges in established civic structures.

**Weaknesses for pilot purposes**:
- A 1,000-person town has existing governance (municipal government, county infrastructure) that will compete with, co-opt, or ignore the pilot framework. The pilot becomes a study of institutional adoption dynamics rather than community self-governance — a different and more complex research question than Phase 3 was designed to answer.
- A 10,000-person watershed district involves regulatory complexity, multi-jurisdictional authority, and institutional politics that are out of scope for Phase 7. Watershed governance research (Barriers to Coordination, ACM SIGCAS 2025; A Multilevel Community Capacity Model, ResearchGate) consistently documents that cross-jurisdictional coordination at this scale requires years of relationship-building before platform adoption is meaningful.
- Technical onboarding at this scale is a multi-month organizational change effort, not a pilot project.
- The failure modes at this scale are institutional (bureaucratic resistance, elected official authority) rather than social (trust, adoption friction) — a different problem set that the corpus has not been optimized to address.

**Assessment**: Not recommended for Phase 7. Return to this scale in Phase 8 or the scenario playbook phase (Phase 7c per the Scoping Memo) once the governance pilot has been validated at Scenario B scale.

---

## 3. Platform-Specific 6-Month Pilot Roadmaps

### Option 1: Nextcloud + Matrix (9.5/10 — Recommended)

**Pilot profile**: Designed for communities with at least one Docker-capable technical operator, any rural or off-grid members, and a need for real-time collaborative document editing (seed catalog, governance protocols, resource inventories). Full offline capability is the decisive factor.

#### Month 1 (June 3 – July 3): Infrastructure Build + Community Outreach

- **June 3–14 (Weeks 1–2)**: Platform build on raspby1. Docker Compose for Nextcloud Hub + Dendrite (Matrix). Target: Nextcloud, Matrix/Element, Tailscale VPN operational; admin account and test users verified; Phase 3 corpus uploaded to shared Nextcloud folder. Estimated: 8–10 hours. Active cooling ordered for raspby1 before deployment (thermal constraint documented in project memory: 81–84°C idle, 87.8°C under compute).

- **June 15 – July 3 (Weeks 3–4)**: Community outreach. Tier 1 contacts: Zone 5 cooperative development networks, Iowa State and University of Wisconsin extension services, Mutual Aid Hub organizers. Outreach frame: "Testing a coordination platform for rural communities — 8 weeks of supported deployment in exchange for honest feedback." Three to five candidates engaged simultaneously; first to confirm 80+ active members and coordination friction advances.

**July 3 go/no-go gate**: If no community confirmed, extend two weeks via secondary channels (Transition Network regional coordinators, USDA Rural Development offices). If still no community by July 15, activate the self-hosted test community fallback (8–12 community builders from the platform volunteer network).

#### Month 2 (July 3 – August 3): Onboarding and First Use

- Leadership cohort onboarding (3–5 delegates): Tailscale on all devices; shared Nextcloud folder structure (Community Governance, Resource Inventory, Meeting Records, Phase 3 Reference Library); Matrix rooms (#general, #delegate-coordination, one per working group); CalDAV calendar linked to assembly schedule.
- Full membership onboarding (target 50–80%): Low-stakes first uses only — meeting notice via Nextcloud, one shared document annotated by the group. The first hard governance decision is deliberately held for Month 3.
- **Key insight from CHI 2025 mutual aid technology research**: Technology adoption in mutual aid communities fails most commonly at value misalignment and trust friction, not technical complexity. Framing platform use as "infrastructure you govern, not a service you use" reduces adoption resistance.

#### Month 3 (August 3 – September 3): Governance Structures Live

- First community assembly using the platform: agenda via Nextcloud 48 hours in advance, minutes recorded in real-time collaborative editing, decisions logged in Decision Registry folder, delegate reports in Matrix.
- Formalize delegate assignments (written role descriptions in Nextcloud), domain specialists identified, conflict resolution protocol acknowledged.
- Risk management: governance structures feel bureaucratic at first contact. Keep Month 3 structures minimal — one assembly per month, one weekly delegate check-in, written records for major decisions only.

#### Month 4 (September 3 – October 3): Operational Infrastructure

- Resource inventory spreadsheet live in Nextcloud (community-held supplies, updated monthly by domain specialists).
- Skill inventory in Nextcloud, searchable by delegates.
- Emergency protocols drafted for 3–5 most likely disruption scenarios.
- Optional: Meshtastic LoRa bridge deployment (5 solar nodes, $200–500 total) for communities with geographic spread or cellular coverage gaps. MESH-API Matrix-Meshtastic bridge confirmed production-capable June 2026.

#### Month 5 (October 3 – November 3): Stress Testing

Tabletop exercises (2–3 hours each, one per fortnight):
1. Resource allocation dispute — walk through conflict resolution protocol.
2. Delegate departure — test institutional memory transfer: can a successor find prior decisions within 10 minutes?
3. 48-hour grid-down scenario — offline tools only (Nextcloud desktop sync, Meshtastic if deployed, printed reference documents). What coordination is impossible?

Each exercise produces a written after-action report — the primary data for Gate 1 evaluation and Phase 7b case study research.

#### Month 6 (November 3 – December 3): Evaluation and Handoff

- Structured interviews with 8–12 community members.
- Platform usage review: Nextcloud document access patterns, Matrix message volume, calendar adoption.
- Decision register audit: formal vs. informal decision ratio.
- Pilot case study document produced (8,000–12,000 words) for Phase 7b.
- Gate 2 decision based on evaluation findings.

**Cost model (Nextcloud+Matrix)**:

| Category | Year 1 | Year 2 | Year 3 |
|---|---|---|---|
| Platform software | $0 | $0 | $0 |
| Infrastructure (raspby1 existing) | $0–$140 | $0–$140 | $60–$300 |
| Loomio governance (optional) | $649 | $649 | $649 |
| Meshtastic (optional, one-time) | $200–500 | $0 | $0 |
| Printed reference kit | $30–60 | $0 | $0 |
| **Total range (no Loomio, no Meshtastic)** | **$30–200** | **$0–140** | **$60–300** |
| **Total range (full stack)** | **$879–1,349** | **$649–789** | **$709–949** |

**Technical operator requirement**: One person comfortable with Docker and Linux command line. Total setup: 8–10 hours. Ongoing maintenance: 2–3 hours/month.

---

### Option 2: Discourse Self-Hosted (8.0/10 — Conditional)

**Pilot profile**: Designed for communities with Docker capability but no rural/off-grid members, no need for real-time document co-editing, and preference for a single interface (forum) over dual interface (Nextcloud + Element). The Discourse embed widget's direct integration with GitHub Pages is the decisive advantage over other platforms.

#### Month 1 (June 3 – July 3): VPS Setup + Community Outreach

- **June 3 (Day 1)**: Hetzner CX22 VPS provisioned, DNS A record set immediately (24–48h propagation is the longest uncontrollable delay; start before installation). Ubuntu 22.04 LTS.
- **June 4 (Day 2)**: Official Discourse Docker install script. Admin account, categories configured, Events plugin installed, GitHub OAuth enabled, Akismet spam protection configured, SMTP via Brevo free tier.
- **June 5**: Phase 5 guides posted as wiki posts in Knowledge Base category. Discourse embed widget deployed on GitHub Pages layout. GitHub Actions → Discourse API webhook configured (one-configuration setup).
- **June 5–14**: Community outreach using same Tier 1 channels as Option 1. Frame: "A community forum integrated with our published guides — see discussions appear directly alongside the content."

**July 3 go/no-go gate**: Same as Option 1.

#### Month 2 (July 3 – August 3): Onboarding and First Use

- Leadership cohort: invite via GitHub OAuth (one-click authentication; no new account required if community members have GitHub accounts). Manually elevate first 15–20 builders to Trust Level 1 on account creation to avoid new-member posting limits that create friction.
- Full membership onboarding via email invite. The Discourse trust-level system (TL0 through TL4) self-governs progressively — new members begin with posting restrictions, earn full access through organic engagement over 2–4 weeks.
- First community use: Phase 5 guides discussion in wiki posts (TL2+ can co-edit). Events plugin for June 15 foundation session with Zoom link.

**Key Discourse advantage for onboarding**: The embed widget means community members discover the forum through the published guides on GitHub Pages — they see active discussion below content they are already reading, with no platform account required to read. This passive-discovery onboarding path reduces the "cold start" problem common to forum launches.

#### Month 3 (August 3 – September 3): Governance Structures Live

- Governance category configured with sub-categories: Decision Records, Delegate Coordination, Working Groups.
- Wiki posts used for living governance documents (delegate role descriptions, conflict resolution protocol) — any TL2+ member can edit.
- Loomio integration: structured governance votes linked from Discourse governance category. Loomio's interface handles formal vote mechanics; Discourse handles discussion.
- First community assembly: agenda as a Discourse pinned topic 48 hours in advance, discussion thread during and after assembly, decision documented in Decision Records category.

**Discourse-specific risk**: No offline posting capability. If any community member reports multi-day connectivity outages (rural Zone 5 counties below 60% broadband coverage per FCC 2024 data), escalate immediately to the migration path: Signal group for time-sensitive coordination, then evaluate migrating to Nextcloud+Matrix within 60 days.

#### Months 4–5 (September 3 – November 3): Operational Infrastructure and Stress Testing

- Resource exchange category configured with standardized listing format (Discourse structured fields or post template).
- Skill roster maintained as a wiki post in the Skills category, updated monthly.
- Tabletop exercises 1 and 2 (resource allocation dispute; delegate departure) conducted identically to Option 1.
- Tabletop exercise 3 (grid-down scenario): Discourse-specific finding expected — all coordination is impossible without internet. Document explicitly. This finding determines whether migration to Nextcloud+Matrix is recommended before Gate 2, regardless of platform adoption success.

#### Month 6 (November 3 – December 3): Evaluation and Handoff

- Structured interviews with specific Discourse-specific questions: single-surface UX ease vs. dual-surface (Option 1) complexity; offline limitation impact; wiki post co-editing sufficiency.
- Discourse plugin ecosystem review: has any governance or resource-tracking need emerged that requires a plugin not yet installed?
- Gate 2 decision includes platform recommendation: if grid-down scenario was tested and connectivity failures affected any participant, Gate 2 deployment defaults to Nextcloud+Matrix regardless of Discourse adoption satisfaction.

**Cost model (Discourse)**:

| Category | Year 1 | Year 2 | Year 3 |
|---|---|---|---|
| VPS (Hetzner CX22) | $84 | $84 | $84 |
| Domain registration | $12–15 | $12–15 | $12–15 |
| Email delivery (Brevo free) | $0 | $0 | $0 |
| Loomio governance (optional) | $649 | $649 | $649 |
| **Total range (no Loomio)** | **$96–99** | **$96–99** | **$96–99** |
| **Total range (with Loomio)** | **$745–748** | **$745–748** | **$745–748** |

**Technical operator requirement**: One person with Docker familiarity and Linux SSH comfort. Setup: 6–8 hours. Ongoing maintenance: 1–2 hours/month (lower than Nextcloud+Matrix because single service stack).

---

## 4. Success Metrics by Domain

### Governance Domain (Gate 1 — Months 1–6)

These are the primary pilot metrics. The governance domain is the test of whether the platform enables formal collective decision-making to replace informal one-person coordination.

| Metric | Month 2 Target | Month 4 Target | Month 6 Target |
|---|---|---|---|
| Active platform users (past 30 days) | 60% enrolled | 70% | 65%+ sustained |
| Decisions with formal written record | — | 5+ | 10+ |
| Assembly agendas distributed via platform | 1 | 3 | 5 |
| Delegate role turnover handled without governance vacuum | — | — | 1+ documented |
| Institutional memory test passed (successor finds decision in 10 min) | — | — | Yes |
| Members report reduced coordination friction | — | — | >60% agree |

**Anti-metrics** (failure indicators): Community returns to informal tools (WhatsApp, email) for governance decisions after Month 3; platform used for one function only (files or chat) but not both; governance documents created but never invoked in real decisions; decision authority accumulates in one person.

### Food Systems Domain (Gate 2+)

Success for food systems looks qualitatively different from governance because it involves physical resource management, not decision coordination.

| Metric | Definition |
|---|---|
| Resource inventory coverage | Community holds inventories of food storage, tools, and seeds that are readable by any delegate without asking the holder directly |
| Surplus allocation decisions | At least 3 documented decisions about surplus distribution made using the governance structures from Gate 1 |
| Supply chain mapping | Community has documented 3+ local supply chain alternatives for 2+ critical food categories |
| Exchange coordination | At least 5 resource exchanges (barter, time-banking, or surplus distribution) documented in the platform |

### Information Infrastructure Domain (Gate 2+)

Information infrastructure success is primarily about resilience architecture — can communication continue when the primary platform is unavailable?

| Metric | Definition |
|---|---|
| Offline fallback tested | Grid-down scenario (48 hours, no internet) completed with documented coordination outcome |
| Off-grid message delivery | If Meshtastic deployed: at least one Matrix message successfully relayed over LoRa during a test |
| Reference library accessibility | Phase 3 documents accessible to at least 70% of community members without internet (Nextcloud desktop sync, downloaded PDFs) |
| Communication chain documented | Written protocol exists specifying who contacts whom in what order when primary platform is unavailable |

---

## 5. Risk Assessment and Adoption Failure Handling

### Primary Risks

**Platform abandonment after first governance friction** (HIGH likelihood, MEDIUM impact): Communities that experience their first difficult governance decision while learning a new platform will attribute the difficulty to the platform rather than the governance challenge. This is the primary documented failure mode in community technology adoption research (CHI 2025: mutual aid groups attribute tech-mediated value tensions to the tool, not the underlying coordination challenge). Mitigation: deliberately hold the first difficult governance decision until Month 3, after the platform is familiar. Month 2 uses the platform for low-stakes coordination only.

**Key-person dependency** (MEDIUM likelihood, HIGH impact): If the technical operator who set up and maintains the platform leaves, the community loses institutional knowledge. Mitigation: require two community members with admin-level access from Month 2. Document all admin procedures in a dedicated platform administration folder accessible to both.

**Offline capability gap revealing itself too late** (Discourse-specific, MEDIUM likelihood, HIGH impact): A community that chooses Discourse and then experiences multi-day connectivity outages discovers the disqualifying limitation after investment. Mitigation: explicitly test the grid-down scenario in Month 5. If any connectivity failure affected any participant, Gate 2 defaults to Nextcloud+Matrix.

**raspby1 thermal throttling** (Nextcloud+Matrix-specific, HIGH likelihood, LOW impact): The Pi 5 runs at 81–84°C idle; sustained community use will approach or exceed safe operating range. Mitigation: active cooling before deployment; monitoring cron job; if throttling detected, migrate Docker stack to Hetzner CX22 ($6/month) — fully portable.

**Dual-interface friction** (Nextcloud+Matrix-specific, MEDIUM likelihood, MEDIUM impact): Communities may adopt Nextcloud but not Element, or vice versa, defeating the integrated use case. Mitigation: onboarding flow requires both from the first community task — assembly agenda in Nextcloud, delegate check-in in Matrix. Joint use from day one prevents split-adoption drift.

### Adoption Failure Playbook

If platform adoption stalls (fewer than 40% of members active after 6 weeks of full membership onboarding):

**Step 1 (immediate)**: Stop pushing platform adoption. Hold a community meeting (in person or by phone, not on the platform) to understand what friction exists. Listen without defending the platform.

**Step 2 (within 2 weeks)**: Identify whether friction is technical (can't install, too complex) or social (feels unnecessary, distrust of new tools). 

- **If technical**: Simplify the onboarding path. For Nextcloud+Matrix: switch to public domain access (Caddy proxy, no Tailscale) if Tailscale installation is the barrier. For Discourse: reduce trust-level posting restrictions manually for all founding members.
- **If social**: Identify one high-value use case that makes the platform demonstrably worth the friction. For governance: the next resource allocation decision that would otherwise generate confusion is done publicly on the platform. The contrast with previous informal confusion is the adoption argument.

**Step 3 (Month 3)**: If adoption is still below 40% after adjustment, activate the self-sustaining test community protocol: a cohort of 8–12 committed builders uses the platform for 30 days as a closed test environment. This validates platform functionality and produces onboarding documentation improvements, even without the target community's full participation.

**Step 4**: Gate 1 evaluation is honest about what happened. A pilot that documents a specific failure mode is more valuable than a pilot that obscures partial adoption. The failure mode data directly informs Gate 2 community selection criteria and onboarding design.

### Platform-Independent Community Assets

Regardless of platform choice, maintain these community-owned assets that survive any platform failure:
- **Member email list**: Export monthly; the community's most critical asset and the only guaranteed re-onboarding channel
- **Resource inventories**: Plain CSV maintained in at least two locations; openable without any platform account
- **Decision log**: Plain Markdown or text; exported from Loomio after each vote; stored in community-owned email or Git repository
- **Governance documents**: PDF and Markdown copies stored outside the platform
- **Phase 3 corpus**: Already on GitHub Pages; local copies on every builder device

---

## 6. Scaling Pathway: 10-Community Network to 50-Community Federation

### Gate 2 Configuration (December 2026)

Month 6 evaluation determines Gate 2. Three scenarios:

**Scenario A — Governance pilot succeeded, expand domain scope**: Gate 2 deploys governance infrastructure to a second community AND adds one domain (food systems or information infrastructure) to the original community. Original community's governance structures are functional enough to absorb domain expansion.

**Scenario B — Governance pilot succeeded, replicate only**: Gate 2 deploys identical single-domain governance pilot to two new communities, emphasizing community type diversity (if Gate 1 was rural cooperative, Gate 2 includes urban mutual aid). Original community enters self-sustaining mode.

**Scenario C — Governance pilot partially succeeded, refine before scaling**: Platform or governance friction documented. Gate 2 deferred 1–2 months for implementation guide revision and targeted re-pilot.

### 10-Community Network (2027 Horizon)

Beyond Gates 1–3, scaling follows a train-the-trainer model. Gate 1 produces a community with at least 2 members who have platform admin experience and governance facilitation experience. These members become Gate 2 peer support resources. Gate 2 produces 4–6 such members. By Gate 4, the deployment network is self-replicating.

The deployment materials from Gate 1 onward are designed to be executable by a community with a single technically-capable member and the written guides — no direct support from the orchestrating project required.

**10-community threshold significance**: At 10+ communities using shared infrastructure, a federated deployment becomes architecturally and socially feasible — cross-community Matrix rooms, shared Nextcloud governance document library, and inter-community delegate coordination. Phase 3 Domain 5 (Scaling Pathways) documents the delegate council coordination model for 3–5 communities coordinating across 500–1,000 people. The same infrastructure deployed in Gate 1 scales to this federation with configuration changes rather than new technology.

**Inter-community coordination requirements at 10 communities**: Two infrastructure additions differentiate a 10-community federation from 10 independent communities:
1. A shared Nextcloud instance (or federated instances with cross-instance document sharing) providing a common governance document library
2. Bridged Matrix rooms connecting delegates across communities, enabling cross-community coordination without requiring one central coordinator

Both additions are available within the current technology stack with no additional licensing cost. The organizational addition is a quarterly inter-community delegate council — one delegate per community, rotating chair, documented decisions visible to all 10 communities' members.

### 50-Community Federation (2028–2029 Horizon)

The transition from 10 to 50 communities introduces three qualitatively new challenges that require explicit design:

**Challenge 1 — Federated identity and access management**: At 50 communities, a single Nextcloud instance serving all communities becomes a single point of failure and a governance bottleneck (who administers it?). Solution: each community operates its own Nextcloud and Matrix instances, federated via Matrix's native federation protocol and Nextcloud's External Storage or cross-instance share capability. This is architecturally available in Nextcloud Hub 26 and Matrix protocol today; it requires each community to have a local technical operator — which the train-the-trainer model produces.

**Challenge 2 — Decision legitimacy at federation scale**: At 50 communities, inter-community decisions cannot be made by a small delegate council without accountability mechanisms that span back to individual communities. The Iroquois Confederacy and Swiss cantonal models (documented in Phase 3 Domain 5) provide the design template: nested delegate structures, consensus-based inter-community decisions with community ratification for major matters, and subsidiary principle (decisions made at the lowest effective scale). Loomio's multi-committee structure supports this architecture directly.

**Challenge 3 — Network effects and information overload**: At 50 communities, the shared document library and cross-community Matrix rooms accumulate more information than any delegate can track. Solution: structured information hierarchy (community-level, regional cluster-level, federation-level Matrix rooms; tiered document access with cross-community search), documented in the Cross-Scale Integration Guide that the Phase 7 Scoping Memo identifies as the highest-priority Phase 7a deliverable.

**Quantitative architecture for 50-community federation**:
- 50 community Nextcloud instances, each serving 80–200 members
- 50 community Matrix homeservers, federated via Matrix protocol
- ~5 regional cluster Matrix rooms (10 communities per cluster)
- 1 federation-level Matrix room (50 community delegates)
- 1 federated Nextcloud governance library (cross-instance shared folder, read-access for all communities)
- Total population served: 4,000–10,000 people across 50 communities
- Infrastructure cost at full federation: $3,000–7,500/year in VPS costs across all communities (50 × $60–150/year each)

The train-the-trainer chain from Gate 1 must be explicit about this horizon from the beginning. Communities joining at Gate 3 and Gate 4 need to know they are joining a federation architecture, not an isolated pilot. This shapes early governance document language, technical setup choices, and operator training scope.

---

## 7. Decision Items — June 3 Gate

1. **Platform authorization**: Confirm Nextcloud+Matrix (Option C) or Discourse (Option A) as the Phase 6 community platform. The 6-month pilot builds on this same infrastructure — one setup serves both Phase 6 and Gate 1.

2. **Community outreach authorization**: Confirm Tier 1 outreach contacts (cooperative development networks, extension services) can be approached with the pilot framing beginning mid-June, after Phase 5 Wave 1 publishes June 5.

3. **Governance domain as pilot scope**: Confirm Phase 3 Domain 1 (governance and decision-making) is the first pilot domain, and the delegate council model is the specific governance structure to deploy.

4. **Gate 1 success threshold**: Confirm that the Section 4 metrics above are appropriate Gate 2 decision inputs, or calibrate before community selection.

5. **Offline capability confirmation**: If any initial Phase 6 participant or target pilot community has rural or off-grid connectivity uncertainty, select Nextcloud+Matrix. This single question determines the platform decision for communities where it is relevant.

---

**Confidence level**: High on governance as the correct first pilot domain and on Scenario B (80–150 person mutual aid/cooperative) as the optimal community type. High on the 10-community federation architecture (draws directly from Phase 3 Domain 5 and is implementable with current infrastructure). Medium on the 50-community federation pathway (structural design is sound; organizational execution at that scale has dependencies on train-the-trainer chain and community uptake rate that are not predictable from Gate 1 data). Medium on 6-month timeline (community selection speed is the most variable element). The primary uncertainty is how long finding the right community takes — everything else in the timeline is contingent on confirming a pilot community by July 3.

---

## Sources

- [Maintaining a Community of Care: ICTs for Mutual Aid — ACM CSCW 2024](https://dl.acm.org/doi/10.1145/3678884.3681857)
- [It Doesn't Actually Feel Very Mutual: How Technology Impacts Mutual Aid — CHI 2025](https://dl.acm.org/doi/full/10.1145/3706598.3714192)
- [Signals Through the Storm: Designing Networks for Mutual Aid Communities — ACM IX Magazine Sept-Oct 2025](https://interactions.acm.org/archive/view/september-october-2025/signals-through-the-storm-designing-networks-for-mutual-aid-communities-in-southeast-louisiana)
- [Beyond Adoption: Nonadoption, Abandonment, and Challenges to Scale-Up — JMIR 2017](https://www.jmir.org/2017/11/e367/)
- [Barriers to Coordination and the Role of Technology in Community-Managed Watersheds — ACM SIGCAS 2025](https://dl.acm.org/doi/10.1145/3715335.3735469)
- [Understanding Discourse Trust Levels — Discourse Blog](https://blog.discourse.org/2018/06/understanding-discourse-trust-levels/)
- [How to Launch an Enterprise Community in 30 Days with Discourse — Discourse Blog 2025](https://blog.discourse.org/2025/06/how-to-launch-an-enterprise-community-in-30-days-with-discourse/)
- [Institutional Infrastructure for Cooperatives, Communities, and Federations — InterCooperative Network](https://intercooperative.network/)
- [Nextcloud Hub Features — Official](https://nextcloud.com/hub/)
- [MESH-API Meshtastic Matrix Bridge — GitHub](https://github.com/mr-tbot/mesh-api)
- [7 Best Community Platforms for Nonprofits in 2026 — Disco](https://www.disco.co/blog/best-community-platforms-for-nonprofits-2026)
- [Digital Tools for Mutual Aid Groups — Digital Fund / Phoebe Tickell](https://medium.com/digitalfund/communities-essential-guide-to-digital-tools-for-mutual-aid-groups-c1664d30b525)
- [A Connected Community Approach: Citizens and Institutions Building Community-Centred Resilience — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8507759/)

*Prior project documents informing this roadmap: PHASE_6_PLATFORM_ANALYSIS.md (v5, June 3, 2026); PHASE_7_SCOPING_MEMO.md; PHASE_7_ROADMAP.md; phase-3/01-governance-decision-making.md through phase-3/05-scaling-pathways-and-thresholds.md.*
