---
title: "Phase 7 Pilot Implementation Roadmap"
project: systems-resilience
phase: 7
status: DECISION-READY — June 3 author gate
created: 2026-06-03
decision_gate: "June 3, 2026 — Phase 6 author and platform selection"
purpose: "Map actual community deployment of the Nextcloud+Matrix platform and systems-resilience framework across a 6-month pilot cycle. This document follows Phase 6 platform analysis completion and the NEXTCLOUD+MATRIX (9.5/10) recommendation."
cross_references:
  - PHASE_7_ROADMAP.md
  - PHASE_7_SCOPING_MEMO.md
  - PHASE_6_IMPLEMENTATION_GUIDE_OPTION_C_NEXTCLOUD_MATRIX.md
  - phase-3/01-governance-decision-making.md
  - phase-3/02-food-systems-supply-chain.md
  - phase-3/03-information-infrastructure.md
  - phase-3/04-security-and-defense.md
  - phase-3/05-scaling-pathways-and-thresholds.md
word_count: ~3800
confidence: High on structure and domain selection rationale; Medium on cost modeling (depends on hardware procurement lead times and community tech literacy); Medium on timeline (dependent on community selection and onboarding speed).
---

# Phase 7 Pilot Implementation Roadmap
## Systems Resilience — Community Deployment, Month 1–6

**Prepared**: June 3, 2026
**Decision context**: Phase 6 platform analysis is complete. Nextcloud+Matrix on raspby1 scores 9.5/10 and is the recommended platform. Phase 7 converts the 130,000+ word knowledge corpus and its recommended platform into working community infrastructure at a real community site, producing the first validated deployment case that informs all subsequent community rollouts.

**The central question this roadmap answers**: What does it take — in time, money, technical capacity, and social organization — to go from "we have the systems-resilience corpus and a platform recommendation" to "a real community is running it, using it, and telling us what works"?

---

## 1. Pilot Domain Selection

### Why Governance Is the Right First Pilot Domain

Of the five Phase 3 community-scale domains — governance and decision-making, food systems and supply chain, information infrastructure, security and defense, and scaling pathways — **governance is the correct first pilot domain**. The reasoning is structural, not preference-based.

Every other domain depends on governance being functional first. Food distribution protocols require a community assembly that can allocate equitably. Communication infrastructure requires someone with authority to make channel assignments and enforce protocols. Security postures require accountability mechanisms that govern who has access to what. The Phase 3 governance document makes this point explicitly: governance is the load-bearing structure beneath every other domain, and it cannot be retrofitted once social trust fractures.

A pilot that starts with food systems or communications infrastructure and lacks governance will produce data about what hardware works. A pilot that starts with governance produces data about what actually determines whether communities can act collectively — which is the question all other domains depend on.

**The specific governance mechanism to pilot**: The **delegate council model** documented in `phase-3/01-governance-decision-making.md` at the 100–500 person scale, using Nextcloud+Matrix as the coordination infrastructure. Nextcloud provides document storage and collaborative editing for decision records, resource inventories, and role descriptions. Matrix/Element provides real-time communication between delegates. Together they implement the "institutional memory" infrastructure that Phase 3 identifies as the critical missing element when communities cross the 150-person Dunbar threshold.

This pairing is not incidental. Phase 6's Nextcloud+Matrix recommendation scored highest precisely because it provides "best Phase 5 integration" — meaning its feature set maps directly to what the governance and information infrastructure domains require: offline document access, real-time messaging, collaborative editing, CalDAV scheduling for assembly meetings, and (via Matrix-Meshtastic bridge in MESH-API June 2026) a path to off-grid communication when grid infrastructure fails.

**What the pilot does not cover**: The food systems and security domains are explicitly deferred to Gate 2. Starting with all five domains simultaneously produces a pilot with too many simultaneous failure modes to diagnose. Governance first, then expand.

---

## 2. Community Selection Criteria

### Optimal Community Size: 80–150 People

The Phase 3 scaling document establishes that the governance transition point — where informal trust-based coordination breaks down and formal structures become necessary — occurs somewhere in the 150-person range (Dunbar's limit for stable personal relationships). This defines the ideal pilot community: **large enough that governance structures are genuinely needed but small enough that informal relationships can still supplement formal systems during the learning phase**.

An 80–150 person mutual aid network or cooperative community hits this target window. It is too large for pure informal coordination, forcing real use of the platform and governance structures. It is small enough that social trust can absorb early failures without fracturing the community.

**Why not a 1,000-person town or 10,000-person watershed district**: Scale mismatches in the wrong direction are the primary risk for a Phase 7 pilot. A 1,000-person town has existing governance (municipal government) that will compete with, ignore, or co-opt the pilot framework. A 10,000-person watershed district involves regulatory complexity and institutional politics that are out of scope for Phase 7. Both produce data about institutional adoption dynamics, not community-scale self-governance — which is what the corpus was built to inform.

**Why not a 20-person household cluster**: Too small. The Phase 3 governance structures and the Nextcloud+Matrix platform are both designed for the 100–1,000 person range. A 20-person cluster uses informal coordination naturally; implementing formal delegate councils and platform infrastructure at this scale produces friction without benefit, and the data won't transfer to target communities.

### Community Type: Mutual Aid Network or Rural Cooperative

The Phase 3 governance document cites three high-confidence case studies: Zapatista autonomous communities, Rojava communes, and Mondragon cooperatives. The US equivalent with the most direct analog is **Zone 5 rural cooperative and mutual aid networks** — the same context all five Phase 3 domains are calibrated for.

**Specific criteria for community selection**:

1. **Size**: 80–150 active members with at least weekly coordination needs (not just emergency response)
2. **Geography**: Zone 5 Midwest, ideally within 2–3 county areas where members can physically meet monthly
3. **Existing social infrastructure**: Has been operating for at least 12 months (not newly formed — the pilot tests infrastructure on a community with established relationships, not one in formation)
4. **Technical baseline**: At least 3–5 members comfortable with basic computer use; does not require universal technical literacy
5. **Governance gap**: Currently using informal coordination (group chats, email lists, one primary organizer) and experiencing coordination friction — missing decisions, lost documents, unclear resource allocation, difficulty bringing in new members
6. **Willingness to document**: Agrees to regular check-ins and allows honest documentation of what works and what doesn't, including failures

**Red flags that disqualify a candidate community**: Ongoing internal governance conflict (the pilot cannot resolve pre-existing disputes; it will be blamed for them); leadership by a single person who has not shared decision-making authority; community formed around a specific emergency response (once the emergency ends, the community dissolves); heavy dependence on commercial platforms (WhatsApp, Facebook groups) with strong resistance to migrating away.

**Where to find candidate communities**: USDA-funded rural cooperative development networks, Iowa State and University of Wisconsin extension service contacts, Mutual Aid Hub organizer networks, and Transition Town regional coordinators are the four highest-density channels. Extension contacts for Zone 5 have been pre-identified in the Phase 7 distribution packages as Tier 1 outreach targets.

---

## 3. Six-Month Timeline

The timeline maps from June 3 (Phase 6 decision gate) to December 2026, with four phases: site selection, platform deployment, operational infrastructure, and evaluation.

### Month 1 (June 3 – July 3): Site Selection and Outreach

**Week 1–2 (June 3–14)**: Platform infrastructure built on raspby1 per the Option C implementation guide. This is the 8–10 hours of Docker setup documented in Phase 6. Target: Nextcloud and Matrix/Synapse operational, Tailscale VPN configured, admin account created, test user accounts verified. This work can begin June 3 as part of the Phase 6 activation decision — the platform is needed regardless of pilot launch.

**Week 3–4 (June 15–July 3)**: Community outreach begins. The Tier 1 outreach contact list (50+ organizations per domain) assembled in Phase 7 distribution packages provides starting candidates. For the governance pilot specifically: cooperative development contacts, extension service coordinators, and mutual aid network organizers are the priority channel. Outreach email template: frame the pilot as "testing a coordination platform built for rural communities — 8 weeks of support in exchange for honest feedback."

**Selection criteria in practice**: Three to five candidate communities are engaged simultaneously. The first to (a) confirm 80+ active members, (b) express genuine coordination friction, and (c) commit to monthly check-ins advances to pilot status. Target: one confirmed pilot community by July 3.

**Go/No-Go gate at July 3**: If no community confirmed, extend search by two weeks using secondary outreach channels (Transition Network regional coordinators, USDA RD offices, county extension services not yet contacted). If still no community confirmed by July 15, activate the self-hosted test community fallback (a cohort of 8–12 community builders from the platform's own volunteer network), which produces lower-quality data but validates platform functionality.

### Month 2 (July 3 – August 3): Platform Deployment and Onboarding

**Week 5–6 (July 3–17)**: Initial onboarding of community leadership cohort (3–5 people). These are the delegate council members or coordination leads, not the full membership. Goal: they can use Nextcloud for document sharing and Matrix/Element for real-time messaging before the full community is onboarded. This keeps the platform-specific failure modes from overwhelming governance-specific learning.

Setup tasks in this phase:
- Tailscale installed on all leadership devices (or public domain access configured if community members are geographically dispersed beyond Tailscale practicality)
- Nextcloud shared folder structure created: Community Governance, Resource Inventory, Meeting Records, Reference Documents (Phase 3 corpus)
- Matrix rooms created: General, Delegate Coordination, Working Groups (one per domain specialist)
- CalDAV calendars linked to Phase 3 assembly meeting schedule (monthly assemblies, weekly working group check-ins)
- Phase 3 governance documents uploaded to shared Nextcloud folder as reference library

**Week 7–8 (July 17 – August 3)**: Full community onboarding. Target: 50–80% of active membership (40–120 people) with working Tailscale + Nextcloud + Element access. The 20–50% who do not adopt in this phase are documented but not chased — forced platform adoption is a well-documented failure mode. The first documented community decision using the platform (meeting record in Nextcloud, vote in Matrix, resource allocation recorded in shared doc) is the milestone marker for this phase.

**Technical support budget**: 3–5 hours of async support per week from the orchestrating researcher during onboarding. Platform issues escalate to the Option C implementation guide's troubleshooting section. Issues not covered there are documented and fed back into the guide.

### Month 3 (August 3 – September 3): Governance Structures Go Live

This is the critical phase where the platform infrastructure supports actual governance operation rather than test use.

**August checkpoint**: First community assembly conducted using the platform. Agenda distributed via Nextcloud shared document 48 hours in advance. Minutes recorded in real time by a designated scribe using Nextcloud collaborative editing. Decisions logged in the Decision Registry folder. Post-meeting: delegates report outcomes in their Matrix rooms.

**Governance structures to deploy in Month 3** (per Phase 3 delegate council model):
- Delegate assignments formalized with written role descriptions (Nextcloud document)
- Domain specialists identified: food/supply coordinator, communications lead, medical/health coordinator, resource allocation lead
- Conflict resolution protocol documented and acknowledged by all delegates
- Recall mechanism explained at community assembly and recorded in governance documents

**Month 3 risk**: Governance structures feel bureaucratic to communities using them for the first time. The most common failure mode documented in the Phase 3 literature is that communities implement formal structures and then immediately abandon them under the pressure of real decisions. Mitigation: keep Month 3 governance structures minimal — one assembly per month, one delegate council per week, written records for major decisions only (not every discussion).

### Month 4 (September 3 – October 3): Operational Infrastructure

Platform and governance structures are functioning. Month 4 expands the platform's role to cover the operational domains.

**Priority expansions in Month 4**:
- Resource inventory: shared Nextcloud spreadsheet tracking community-held supplies (food storage, medical, tools) updated monthly by domain specialists
- Skill inventory: roster of who has what skills, documented in Nextcloud, searchable by domain specialists during coordination
- Emergency protocols: written (Nextcloud document) response procedures for the 3–5 most likely disruption scenarios for this specific community

**Meshtastic integration (if community is geographically dispersed)**: The MESH-API Matrix-Meshtastic bridge confirmed for June 2026 enables Matrix messages to pass over LoRa mesh when internet is unavailable. For rural Zone 5 communities spread across 10–30 km, deploying 3–5 Meshtastic nodes (RAK WisBlock solar-powered backbone, $25–37 each) extends the communication infrastructure to grid-down scenarios. This is optional in Month 4 but strongly recommended for communities with geography that makes cellular coverage unreliable.

**Phase 4 cross-reference**: The farm equipment repair research committed in Phase 6 Track A (44,000 words, 78 sources) can be uploaded to Nextcloud at this stage as a reference library. Communities accessing it through Nextcloud offline sync have it available without internet dependency.

### Month 5 (October 3 – November 3): Stress Testing

Month 5 introduces deliberate stress to the governance and platform systems. This is not manufactured crisis — it is structured scenarios drawn from Phase 3 failure mode documentation.

**Tabletop exercises** (each 2–3 hours, one per fortnight):
1. **Resource allocation dispute**: Two domain specialists disagree about how to allocate a shared resource. Walk through the documented conflict resolution protocol. Does it resolve the dispute? Where does it break down?
2. **Delegate departure**: A key delegate announces they are leaving the community in 30 days. Walk through the institutional memory transfer protocol. Is the documentation sufficient for a successor to step in?
3. **Grid-down communication**: For 48 hours, the community uses only offline tools (Nextcloud desktop sync, Meshtastic if deployed, printed reference documents). What information is unavailable? What decisions cannot be made?

**Stress test documentation**: Each tabletop exercise produces a written after-action report in Nextcloud. These reports are the primary data source for the Phase 7 evaluation and for the future case study research (Phase 7b per the Scoping Memo).

### Month 6 (November 3 – December 3): Evaluation and Handoff

**Evaluation activities**:
- Structured interviews with 8–12 community members covering: platform usability, governance friction, what worked, what was abandoned and why
- Platform usage data review: Nextcloud document access patterns, Matrix message volume, calendar adoption
- Decision register audit: how many decisions were formally recorded vs. informally made? What categories of decisions bypassed the formal process?

**Handoff**: The community transitions from active pilot support to self-sustaining operation. The orchestrating researcher produces a pilot case study document (target: 8,000–12,000 words) that feeds directly into the Phase 7b case study research phase described in the Scoping Memo.

**Gate 2 decision**: At the end of Month 6, the evaluation determines whether to deploy to a second community with the same governance pilot scope, or to add a second domain (food systems or information infrastructure) to the second community's deployment. This gate is documented as part of the scaling pathway in Section 7 below.

---

## 4. Cost Modeling

### Infrastructure Costs

**Platform (Nextcloud+Matrix on raspby1)**: $0/year for base infrastructure — the Raspberry Pi 5 (raspby1) is already operational. Optional additions:
- Loomio for structured governance votes: $120/year (documented in Phase 6 Option C guide)
- Domain registration and dynamic DNS for public access (if Tailscale-only is insufficient): $12–20/year
- External USB storage for Nextcloud data volume growth: $40–80 one-time (500 GB–1 TB drive)
- Email (Brevo free tier covers 300 emails/day, sufficient for a 150-person community): $0

**Meshtastic infrastructure (optional, recommended for rural communities)**:
- 5x RAK WisBlock solar repeater nodes: $125–185 total
- Antenna upgrades (fiberglass omnidirectional, ~3 dBi gain): $20–40 per node installed outdoors
- Weatherproof enclosures if custom-built: $10–20 per node (alternative: Seeed SenseCAP P1 at $80–120 per node, weatherproof out of box)
- Total Meshtastic build for 5-node Zone 5 rural community: $200–500 depending on enclosure and antenna choices

**Printed reference materials**: Phase 3 documents (5 domains, ~28,000 words total) printed as laminated field references at local print shop: approximately $30–60 for a community kit of 10 copies.

**Total infrastructure cost range**: $0 (Tailscale-only, no Meshtastic, no printing) to $700 (full deployment with Meshtastic, printing, and Loomio). The 8–10 hour setup time documented in Phase 6 represents the only mandatory cost if raspby1 is available.

### Setup Labor

Phase 6 documents the 8–10 hour setup estimate for Option C (Nextcloud+Matrix). Broken down for the pilot:

| Task | Hours | Notes |
|---|---|---|
| Platform installation (Docker Compose, initial config) | 3–4 | Per Option C guide, Steps A1–A6 |
| Matrix/Synapse setup and federation | 2–3 | Per Option C guide, Steps B1–B5 |
| Community structure creation (users, groups, folders) | 1–2 | Per Option C guide, Step A3 |
| Tailscale integration and access testing | 0.5–1 | Per checklist items |
| Initial content upload (Phase 3 corpus) | 0.5–1 | Document upload and folder structure |
| **Total setup** | **7–11 hours** | Consistent with Phase 6 estimate |

**Onboarding labor** (not included in the Phase 6 8–10 hour estimate):
- Leadership cohort onboarding (3–5 people): 2–4 hours async support
- Full community onboarding (40–120 people): 4–8 hours over 2 weeks (mostly self-service with written guide)
- Monthly check-in calls during 6-month pilot: 1 hour/month = 6 hours total

**Total labor estimate**: 20–30 hours over 6 months. This is within a single experienced orchestrator's capacity.

### Ongoing Maintenance

After the 6-month pilot, ongoing maintenance for a self-sustaining community deployment:
- Platform updates (Docker image pulls, Nextcloud app updates): 2–4 hours/year
- raspby1 hardware monitoring and storage management: 1–2 hours/month
- Community technical support (password resets, access issues): 0.5–1 hour/month average
- Annual backup verification: 2 hours

**Annual ongoing cost**: approximately 20–30 hours of technical time, $0–140 in software costs (Loomio optional), and periodic hardware maintenance (SD card replacement every 2–3 years: $15–30).

---

## 5. Risk Assessment

### Technical Risks

**Risk 1: raspby1 thermal throttling under sustained load (HIGH likelihood, LOW impact)**
The MEMORY.md note documents that the Raspberry Pi 5 runs at 81–84°C idle and 87.8°C under compute. Nextcloud+Synapse under active community use will add sustained CPU load. Mitigation: active cooling (already noted as a hardware action in project memory), monitoring via `vcgencmd measure_temp` in a cron job, and documented threshold (>85°C sustained = restart Docker services to reduce load). If hardware replacement is needed, the Option C setup is fully Docker-portable to any Linux machine.

**Risk 2: Community members cannot or will not install Tailscale (MEDIUM likelihood, MEDIUM impact)**
Tailscale requires device-level installation and a short setup flow. For communities with low tech literacy or older hardware, this is a real barrier. Mitigation: deploy Option C2 (public domain + Caddy proxy) for communities where Tailscale adoption is below 60% after 2 weeks. This adds $12–20/year in domain cost and requires port forwarding, but eliminates the Tailscale adoption barrier. Decision point at end of Week 6 onboarding.

**Risk 3: Matrix federation complexity causes setup delays (MEDIUM likelihood, LOW ongoing impact)**
The Matrix/Synapse server configuration is the most technically demanding part of the Option C setup. Misconfigured federation keys, PostgreSQL initialization errors, and Nginx proxy headers are the documented failure modes. Mitigation: the Option C implementation guide has explicit troubleshooting steps; allow 10–12 hours instead of 7–10 for first deployment until the setup is fully documented from real-world execution.

**Risk 4: Platform split — Nextcloud vs. Matrix adoption asymmetry (LOW likelihood, HIGH impact)**
Communities may adopt one service and ignore the other. Nextcloud for files, nothing for messaging (they stay on WhatsApp). Or Matrix for messaging, nothing for documents (Nextcloud never used). Either split defeats the integrated coordination use case. Mitigation: onboarding flow explicitly requires both — the first community governance task (assembly agenda) requires Nextcloud access; the first real-time coordination task (delegate check-in) requires Matrix. Joint use from day one prevents split-adoption drift.

### Community Adoption Risks

**Risk 5: Platform abandonment after first governance friction (HIGH likelihood, MEDIUM impact)**
This is the primary risk. Communities that experience their first difficult governance decision while learning a new platform will attribute the difficulty to the platform rather than the governance challenge. This is documented behavior in every technology-change context. Mitigation: deliberately hold the first difficult governance decision for Month 3 or later, after the platform is familiar. Month 2 onboarding uses the platform for low-stakes coordination (meeting notices, document sharing). This separation between platform learning and governance learning is explicitly built into the timeline.

**Risk 6: Key person dependency — pilot collapses if primary technical lead leaves (MEDIUM likelihood, HIGH impact)**
If the community member who set up and maintains the platform leaves, the community loses institutional knowledge of the system. Mitigation: require two community members to have admin-level platform access from Month 2 onward. Document all admin procedures in a Nextcloud "Platform Administration" folder accessible to both. This is the same principle as the Phase 3 institutional memory requirement applied to the platform itself.

**Risk 7: Social conflict predating the pilot contaminates results (LOW likelihood, HIGH impact if present)**
A community with unresolved internal conflict will use the pilot as a proxy battleground. Any platform or governance decision becomes a flashpoint. Mitigation: community selection criteria explicitly screen for this (12+ months of operation, no ongoing formal disputes, distributed decision-making already present). If conflict emerges post-selection, the pilot is paused and conflict resolution resources from Phase 5 Wave 2 are provided before continuing.

### Scaling Constraints

**Risk 8: Findings don't transfer to communities different from the pilot community (MEDIUM likelihood, MEDIUM impact)**
A single pilot community produces case data for one community type. If the pilot is a rural Zone 5 agricultural cooperative, the findings are most transferable to similar communities and least transferable to urban mutual aid networks or small-town governance contexts. Mitigation: document the pilot community's characteristics precisely, flag which findings are likely context-specific, and design Gate 2 to select a community from a different type (e.g., if Gate 1 is rural cooperative, Gate 2 is urban mutual aid).

---

## 6. Success Metrics

The pilot succeeds if it produces validated, transferable learning about what works when real communities deploy the systems-resilience framework with Nextcloud+Matrix infrastructure. This requires both quantitative platform metrics and qualitative governance outcome data.

### Platform Adoption Metrics (measured monthly)

| Metric | Month 2 Target | Month 4 Target | Month 6 Target |
|---|---|---|---|
| Active Nextcloud users (logged in past 30 days) | 60% of enrolled | 70% | 65%+ sustained |
| Documents created in governance folder | 3+ | 10+ | 20+ |
| Matrix active users (past 30 days) | 50% of enrolled | 60% | 55%+ sustained |
| Assembly agendas distributed via Nextcloud | 1 | 3 | 5 |
| Decision records in Decision Registry | 1 | 5 | 10+ |

Note: sustained adoption in Month 6 is a lower bar than peak adoption in Month 4. This is intentional — the goal is sustainable use, not peak engagement.

### Governance Quality Metrics (measured at Month 3, 5, 6)

| Metric | Target |
|---|---|
| Decisions made with formal record (assembly vote, documented reasoning) | >70% of major decisions |
| Delegate role turnover handled without governance vacuum | 1+ instance documented without crisis |
| Conflict resolution invoked and resolved | At least 1 instance |
| Institutional memory: successor can find prior decisions within 10 minutes | Test conducted Month 6 |
| Community members report reduced coordination friction | >60% agree on exit survey |

### Phase 3 Framework Validation Metrics

These are the metrics that feed directly into Phase 7b case study research:

- **Dunbar threshold observation**: Did governance stress appear as community grew or during high-load periods? What triggered it? What resolved it?
- **Delegate council effectiveness**: Did delegates actually implement assembly decisions rather than making independent decisions? What accountability mechanisms were invoked?
- **Off-grid communication readiness**: During the Month 5 grid-down tabletop, what percentage of coordination was possible with offline tools alone?
- **Platform gap identification**: What coordination tasks did the community need to do that neither Nextcloud nor Matrix handled well? (This is the input to Option C guide revision and the Phase 7 Scoping Memo's integration guide work.)

### Anti-Metrics (Signs the Pilot Is Failing)

- Community returns to informal coordination tools (WhatsApp, email) for governance decisions after Month 3
- Platform used exclusively for one function (files or chat) but not both
- Governance structures documented but not invoked in real decisions
- Key leadership concentrates in one person (specialist accumulation of power failure mode from Phase 3)

---

## 7. Scaling Pathway

The pilot produces two distinct outputs: validated deployment knowledge and a working platform installation that can be replicated. The scaling pathway converts both into a structured program for subsequent community deployments (Gates 2+).

### Gate 2 Decision Framework (December 2026)

The Month 6 evaluation determines the Gate 2 configuration. Three scenarios:

**Scenario A — Governance pilot succeeded, expand domain scope**: Gate 2 deploys the same governance infrastructure to a second community AND adds one additional domain (food systems or information infrastructure) to the original pilot community. The original community's governance structures are functioning well enough to absorb domain expansion.

**Scenario B — Governance pilot succeeded, replicate only**: Gate 2 deploys the same single-domain governance pilot to two new communities simultaneously, emphasizing geographic and community-type diversity. Original pilot community moves to self-sustaining mode. This scenario prioritizes learning from community type variation over domain expansion.

**Scenario C — Governance pilot partially succeeded, refine before scaling**: Significant platform or governance friction identified. Gate 2 is deferred 1–2 months while the Option C guide is revised, onboarding materials improved, and the specific friction points addressed. One targeted re-pilot with the same community or a replacement community. This is not a failure — it is the expected outcome of a first pilot.

### What Pilot Learning Produces for Gates 2+

**Revised deployment materials**: The Option C implementation guide will be updated with real-world time estimates (replacing the current theoretical 8–10 hour estimate with data from actual deployment), specific failure mode documentation, and a community onboarding script refined from what worked at Gate 1.

**Community type calibration**: The selection criteria in Section 2 above will be revised based on which characteristics of the Gate 1 community were load-bearing (predicted adoption and governance quality) and which were noise. The characteristics that proved predictive become required selection criteria for Gates 2+.

**Domain expansion sequencing**: After governance is operational, the Phase 3 domain sequence matters. The information infrastructure domain (Phase 3, Domain 3) is the natural second deployment because it adds the off-grid communication layer (AREDN mesh, GMRS radio coordination) that is documented alongside but not implemented by the Nextcloud+Matrix platform. Food systems (Domain 2) is the natural third domain because it introduces resource allocation functions that require working governance before they are feasible.

**Phase 7b case study input**: The Gate 1 pilot produces the primary documentation for one of the 4–6 case studies described in the Phase 7 Scoping Memo (Candidate 1: Implementation Case Studies). The after-action reports from Month 5 tabletop exercises, the Month 6 structured interviews, and the platform usage data together constitute the raw material for a 10,000–12,000 word case study document. This case study is explicitly designed to test Phase 3 framework claims against real community behavior — producing the framework validation data that the Scoping Memo identifies as the highest-value contribution of Phase 7b.

### Scaling to 10+ Communities (2027–2028 Horizon)

Beyond Gates 1–3, scaling follows a train-the-trainer model rather than direct deployment by the project team. Gate 1 produces a deployment-literate community with at least 2 members who have platform admin experience and governance facilitation experience. These members become Gate 2 peer support resources. Gate 2 produces 4–6 such members. By Gate 4, the deployment network is self-replicating.

The infrastructure for this is already present in the project: the Tier 1 outreach contact list (cooperative development networks, extension services) connects to organizations that routinely train facilitators and organizers. The deployment materials developed from Gate 1 onward are designed to be executable by a community with a single technically-capable member and the written guides — not requiring direct support from the orchestrating project.

**The 10-community threshold** is significant because it is the scale at which federation between communities becomes feasible and valuable. Phase 3 Domain 5 (Scaling Pathways) documents the delegate council coordination model for 3–5 communities coordinating across 500–1,000 people. At 10+ communities using shared infrastructure, a federated deployment with cross-community Matrix rooms, shared Nextcloud governance document library, and inter-community delegate coordination is architecturally possible using the same infrastructure deployed in the Gate 1 pilot.

---

## Decision Items for June 3 Gate

The following decisions are needed at or immediately after the June 3 Phase 6 decision gate for Phase 7 pilot work to begin in parallel with Phase 6 content production:

1. **Platform build authorization**: Confirm Option C (Nextcloud+Matrix on raspby1) is authorized to proceed. The 8–10 hour setup should begin June 3–5. This is both the Phase 6 community platform and the Gate 1 pilot deployment infrastructure — one build serves both purposes.

2. **Community outreach authorization**: Confirm that Tier 1 outreach contacts (cooperative development networks, extension services) can be approached with the pilot framing in mid-June. This requires the Phase 5 Wave 1+2 publication to be live (anchor artifact for outreach) — compatible with the June 5 Wave 1+2 publication target.

3. **Governance domain as pilot scope**: Confirm that Phase 3 Domain 1 (governance and decision-making) is the right first pilot domain, and that the delegate council model is the specific governance structure to deploy. Alternative argument would be information infrastructure as first domain (more technically tractable, less socially complex) — but the dependency argument for governance first is compelling.

4. **Gate 1 success threshold**: Confirm that the Month 6 evaluation criteria in Section 6 above are appropriate as the Gate 2 decision inputs. If the success bar should be higher or lower, calibrate before community selection.

---

**Confidence level for this roadmap**: High on governance as the correct first pilot domain (dependency argument is strong and consistent with Phase 3 framework). High on 80–150 person mutual aid/cooperative as the target community type (matches Phase 3 calibration exactly). Medium on 6-month timeline (community selection is the most variable element — finding the right community with the right characteristics could take 2–8 weeks). Medium on cost modeling for Meshtastic optional layer (hardware procurement lead times vary). The primary uncertainty is community selection speed — everything else in the timeline is contingent on having a confirmed pilot community by July 3.
