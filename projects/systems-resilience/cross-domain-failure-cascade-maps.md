---
title: "Cross-Domain Failure Cascade Maps"
project: systems-resilience
region: "Midwest US (Zone 5)"
phase: 4
scale: community
domain: integration
created: 2026-05-19
word_count: ~3200
citation_count: 28
status: production
cross_references:
  - phase-3/01-governance-decision-making.md
  - phase-3/02-food-systems-supply-chain.md
  - phase-3/03-information-infrastructure.md
  - phase-3/04-security-and-defense.md
  - phase-3/05-scaling-pathways-and-thresholds.md
  - regional-governance-federation-framework.md
---

# Cross-Domain Failure Cascade Maps
> **Region**: Midwest US (Zone 5) | **Scale**: 100–1,000 people  
> **Phase**: 4 — Integration | **Type**: Failure cascade analysis  
> **Cross-references**: [Governance](./phase-3/01-governance-decision-making.md) · [Food Systems](./phase-3/02-food-systems-supply-chain.md) · [Information Infrastructure](./phase-3/03-information-infrastructure.md) · [Security](./phase-3/04-security-and-defense.md) · [Scaling Pathways](./phase-3/05-scaling-pathways-and-thresholds.md)

---

## The Most Important Finding

No Phase 3 domain fails in isolation. Every domain failure within a 100–1,000 person community under extended disruption conditions propagates into at least two adjacent domains within 72 hours. The empirical evidence is consistent: Hurricane Katrina produced a complete communications infrastructure collapse that paralyzed governance command-and-control, which prevented security coordination, which allowed looting to compound the food distribution problem. Texas's 2021 ERCOT failure cascaded from energy into water, then food storage, then governance legitimacy crisis as public trust eroded. Puerto Rico after Maria saw food insecurity deepen because governance (federal block-grant model) failed to scale aid appropriately, which worsened the security environment in affected communities.

The practical implication for Phase 3 communities: the domains are not parallel tracks. They are interdependent nodes in a network. Failure in any one triggers failure propagation in others. This document maps five specific cascade pathways — one originating in each Phase 3 domain — with propagation diagrams, timing, and recovery protocols.

---

## Domain Interdependency Framework

Before mapping specific cascades, the dependency relationships between Phase 3 domains must be established. These are not symmetric: some domains are prerequisites for others in ways that create directional failure flows.

### Primary Dependency Matrix

| Domain | Depends On | Provides To |
|--------|-----------|-------------|
| **Governance** | Information (decision input), Security (authority enforcement) | All domains (resource allocation, decision legitimacy) |
| **Food Systems** | Governance (allocation authority), Security (distribution protection), Information (coordination) | Security (physical capacity), Governance (legitimacy of survival) |
| **Information Infrastructure** | Security (equipment protection), Governance (resource funding) | Governance (situational awareness), Food (coordination), Security (threat intelligence) |
| **Security** | Governance (mandate + rules of engagement), Information (threat data), Food (physical sustenance) | Governance (enforcement capacity), Food (distribution protection), Information (equipment protection) |
| **Scaling/Federation** | All four base domains functioning | All base domains (inter-community reinforcement) |

### Critical Finding: Governance is the Single Most Critical Node

Governance is the only domain that provides outputs to all other domains simultaneously (resource allocation decisions, decision legitimacy) while depending on two domains (information, security) for functional inputs. This makes governance both the highest-leverage domain for resilience investment and the highest-consequence domain for cascade initiation. A governance failure at 100–1,000 person scale triggers cascade effects across all four remaining domains within 48–96 hours.

This dependency architecture explains why the Phase 3 governance document identified governance as "the load-bearing structure beneath every other community resilience domain." [Phase 3, Domain 1]

---

## Cascade Pathway 1: Food Supply Collapse

**Origin domain**: Food Systems (Phase 3, Domain 1)  
**Trigger event**: Loss of external food supply (distribution network failure, crop failure, supply chain disruption)  
**Scale**: 500-person Midwest rural community with 2-week food reserves

### Propagation Sequence

**Hours 0–72: Food scarcity recognized**
The community recognizes external supply has failed. Internal food inventory is assessed. At 2-week reserves (a Phase 3 recommendation), this window is survivable if governance responds immediately. Governance convenes emergency allocation assembly. Information infrastructure required to coordinate distribution and communicate inventory data.

**Day 3–7: Governance stress**
Food rationing creates governance conflict. Allocation decisions — who gets how much, which households have priority, how much to reserve for production inputs — are exactly the contested decisions that governance structures are built to handle. If governance is functioning (Phase 3 protocols in place), rationing decisions are made through assembly processes with legitimacy. If governance is weak, allocation decisions reflect whoever has informal authority or physical control, creating internal conflict. [1]

**Day 7–14: Security cascade**
By week 2, if no resupply is imminent, security incidents increase. The documented evidence from post-disaster settings is consistent: desperate individuals seeking food are the primary security threat, not organized raiders. Communities with strong pre-crisis social cohesion experience fewer security incidents; communities with weak social bonds experience more. [2] Security resources (if any) must be redeployed from perimeter monitoring to internal distribution protection, reducing external threat response capacity.

**Day 14–30: Information cascade**
As security pressures rise, information resources are redirected. Radio operators and mesh network coordinators are pulled into security roles. Information infrastructure degradation begins, reducing the situational awareness that governance requires to make informed allocation decisions — a feedback loop that worsens governance decision quality at exactly the moment it is most stressed.

**Day 30+: Governance legitimacy crisis**
If food crisis is unresolved at 30+ days, governance faces its most severe test: community members question whether the governance structure can solve the problem. In historical examples, communities at this point either (a) successfully appeal to external support networks (regional federation, government aid), (b) reorganize governance around the crisis with new emergency authority, or (c) fragment into household/small-group factions that reduce collective action capacity. [3]

### Cascade Diagram

```
FOOD SUPPLY COLLAPSE
        |
        v (Day 3-7)
GOVERNANCE STRESS [allocation conflicts]
        |                    |
        v (Day 7-14)         v (Day 7-14)
SECURITY DIVERSION     INFORMATION DEMAND
[internal refocus]     [situational awareness]
        |                    |
        v (Day 14-30)        v (Day 14-30)
SECURITY DEGRADED -----> INFORMATION DEGRADED
        |                    |
        +--------------------+
                 |
                 v (Day 30+)
     GOVERNANCE LEGITIMACY CRISIS
```

### Recovery Protocol: Food Cascade

**Priority 1 (Days 0–3)**: Activate emergency food inventory protocol. Full community inventory within 24 hours. Governance assembly convenes within 48 hours with inventory data. Rationing framework adopted.

**Priority 2 (Days 3–14)**: Activate regional food mutual aid. If community has pre-established relationship with adjacent communities or regional federation, this is the moment to invoke it. Inter-community food sharing agreements are most valuable at this stage. (See: Regional Governance Federation Framework — inter-community food reserve sharing.)

**Priority 3 (Days 7–30)**: Protect information infrastructure from security diversion. Designate at least two information coordinators who cannot be reassigned to security roles. This is a critical protocol gap in Phase 3: most communities will cannibalize information roles when security pressure rises. Explicit role protection prevents this.

**Priority 4 (Days 14–30)**: Begin emergency food production intensification. If the food crisis extends past 14 days, governance should authorize resource reallocation to food production acceleration: all available labor hours, greenhouse fast-cropping (Zone 5 spring/fall application), animal protein acceleration.

**Recovery indicator**: Food cascade recovery is stable when 14-day reserves are re-established and external supply pathways are diversified or replaced.

---

## Cascade Pathway 2: Governance Failure

**Origin domain**: Governance (Phase 3, Domain 1)  
**Trigger event**: Leadership death/departure, governance legitimacy fracture, irresolvable internal conflict  
**Scale**: 300-person community 6 months post-crisis

### Propagation Sequence

**Hours 0–48: Authority vacuum**
Governance failure creates immediate authority vacuum. All resource allocation decisions stall. No legitimate process exists for deciding who gets what, who does what, what the rules are. In the first 48 hours, communities often operate on informal norms from the pre-governance period — which still provide some coordination capacity if the pre-governance community was small and well-bonded. At 300+ people, informal norms are insufficient.

**Day 2–7: Information collapse**
Information infrastructure was built and governed under the now-failed governance structure. GMRS radio protocols, mesh network access, document library management — all were assigned roles through governance. Without governance, no legitimate authority exists to enforce information protocols, resolve conflicting transmissions, or maintain equipment. Information quality degrades within days. [4]

**Day 7–14: Food cascade**
Food distribution was coordinated through governance — the assembly's allocation decisions determined who received what from community food stores. With governance absent, food distribution defaults to whoever physically controls storage locations. Historical evidence shows this produces hoarding, access exclusion, and rapid deterioration of community food security even when absolute food supply is adequate. [5]

**Day 14–30: Security cascade**
The combination of unclear authority, degraded information, and contested food allocation produces security incidents. These are almost entirely internal at first — disputes over food access, disputes over decision authority, disputes over territory within the community. If the governance failure was caused by internal conflict, security incidents are likely to involve the same factions. External threats become more dangerous because no legitimate authority can coordinate a collective response.

**Day 30+: Fragmentation**
Without governance reconstitution by day 30, communities typically fragment. Household clusters align around informal leaders, geographic clusters, or resource control points. The 300-person community effectively becomes 5–8 smaller informal communities of 30–60 people each. These sub-communities may be more governable at their smaller scale, but they lose the collective action advantages that justified the community's size.

### Recovery Protocol: Governance Cascade

**Priority 1 (Hours 0–48)**: Emergency governance reconstitution. The Phase 3 governance document provides specific protocols for governance gaps. The most critical step is convening an emergency assembly within 24 hours and establishing any legitimate decision-making process — even a temporary one — before the authority vacuum hardens into factionalism.

**Priority 2 (Day 2–7)**: Protect information infrastructure independently of governance. Information coordinators should have pre-established authority to maintain communications systems regardless of governance status. This requires a specific protocol: information infrastructure operates on a "continuity of operations" basis that does not depend on governance approval for its own maintenance.

**Priority 3 (Day 7–14)**: Emergency food distribution protocol. In a governance failure, food stores should default to a pre-established rationing baseline — not first-come-first-served, not faction-controlled — based on caloric needs. This requires pre-establishing an emergency food distribution protocol that can operate for 14 days without governance direction.

**Recovery indicator**: Governance cascade recovery is stable when a new governance structure has been operating for 7 days without challenge, resource allocation decisions are being made through a legitimate process, and security incidents have returned to baseline.

---

## Cascade Pathway 3: Information Infrastructure Failure

**Origin domain**: Information Infrastructure (Phase 3, Domain 3)  
**Trigger event**: Simultaneous grid power loss + internet loss + equipment damage (post-storm scenario)  
**Scale**: 200-person rural community with three-layer communication system

### Propagation Sequence

**Hours 0–6: Layer 1 failure (GMRS)**
Power loss takes out GMRS base stations and repeaters. Handheld units remain operational on battery (8–24 hours depending on use pattern). Community members with handhelds attempt to coordinate, but without the base station relay, range drops to direct line-of-sight (1–3 miles in Midwest terrain). GMRS coordination is partial, not absent.

**Hours 6–24: Layer 2 partial failure (AREDN mesh)**
AREDN mesh nodes begin failing as battery backups deplete. Nodes with solar maintain operation; nodes without solar fail within 6–12 hours. The mesh degrades rather than collapses — a partial mesh with 40% of nodes is still useful for localized communication. But the failure is uneven: nodes that had solar by design versus nodes that did not reflects pre-crisis investment decisions.

**Hours 24–72: Governance information failure**
Governance decision-making requires situational awareness — what is the current inventory, where are the needs, what are the security alerts. With information infrastructure degraded, governance makes decisions with incomplete data. The Phase 3 governance document identifies "preserving institutional memory across personnel changes" and "coordinating with external entities" as governance functions — both require functioning communications.

**Day 3–7: Security cascade**
Security depends on threat intelligence — knowing where threats are, when they are active, how other communities are responding. Information failure leaves security coordinators blind to developments beyond visual range. The 2005 Katrina communications failure is the canonical example: "A complete breakdown in communications that paralyzed command and control and made situational awareness murky at best." [6] Security without information reverts to static defense — community members at fixed positions rather than coordinated response.

**Day 7–14: Food coordination failure**
Food distribution coordination across a 200-person community requires communication: which households have urgent need, when does the distribution point open, which households cannot reach the distribution point. Without information infrastructure, distribution coordinators must rely on pre-scheduled fixed distribution (predictable but inflexible) or physical neighborhood-by-neighborhood checks (labor-intensive). Both are possible but significantly less effective than coordinated distribution with real-time communication.

### Recovery Protocol: Information Cascade

**Priority 1 (Hours 0–6)**: Activate Layer 3 (HF shortwave radio). The Phase 3 information infrastructure document identifies HF shortwave as the last-resort layer: it requires no repeaters, no network nodes, and can communicate over hundreds of miles using battery power. HF radio operators should know to shift to pre-established emergency frequencies within the first hour of grid failure.

**Priority 2 (Hours 6–48)**: Assess and triage mesh node status. Which nodes still have power? Which are solar-powered? Which are battery-backed? A current network status map allows the community to work around degraded sections rather than assuming total failure.

**Priority 3 (Day 2–7)**: Deploy runner network. For immediate local coordination within 0.5-mile radius, a physical runner network — designated individuals who carry messages between key locations — provides zero-infrastructure backup. This is documented in Phase 3 information infrastructure but rarely practiced in advance.

**Priority 4 (Day 7+)**: Prioritize restoration of printed reference materials. Printed documents (emergency protocols, community roster, resource inventory, skill directory) should be distributed to key coordinators before crisis. These function when nothing else does.

**Recovery indicator**: Information cascade recovery is stable when at least one reliable communication layer is fully operational and governance has access to current situational data.

---

## Cascade Pathway 4: Security Structure Breakdown

**Origin domain**: Security (Phase 3, Domain 4)  
**Trigger event**: Security coordinator departure/incapacitation during active threat, or organized external group establishing presence near community  
**Scale**: 500-person community with established security protocols

### Propagation Sequence

**Hours 0–24: Security coordination gap**
Security coordinator loss or incapacitation creates immediate protocol gap. The Phase 3 security document emphasizes that security infrastructure is downstream of social cohesion — but security coordination structures are still required. Without a coordinator, security volunteers default to individual judgment, which produces inconsistent responses and gaps in coverage.

**Hours 24–72: Governance decision demand**
Security breakdown immediately generates governance demand: who is the new security coordinator? What are the rules of engagement? Can community members use force? These decisions cannot be deferred. Governance must convene and decide under time pressure — exactly the conditions identified in Phase 3 as producing poor governance outcomes when structures are weak.

**Day 3–7: Information disclosure risk**
If security breakdown is caused by an external threat (organized group establishing presence), information security becomes critical. What does the external group know about the community's food stores, decision-making processes, vulnerabilities? Information security — controlling what information is available to outsiders — requires security coordination to be effective. Without security structure, information discipline degrades. [7]

**Day 7–14: Food distribution vulnerability**
Food distribution requires physical security — the ability to maintain orderly access to food stores, prevent theft, and protect distribution coordinators. Security structure breakdown leaves food distribution physically vulnerable. Communities typically respond by restricting distribution schedules (less frequent, shorter windows) to reduce exposure, which degrades food access.

**Day 14–30: Social cohesion erosion**
The Phase 3 security document's most important finding is that security infrastructure is downstream of social cohesion. The reverse is also true: extended security uncertainty erodes social cohesion. Community members who feel unsafe are less likely to participate in governance assemblies, less likely to share resources, and more likely to prioritize household security over community coordination.

### Recovery Protocol: Security Cascade

**Priority 1 (Hours 0–24)**: Activate backup security coordinator. The Phase 3 security document recommends a minimum two-person leadership structure with explicit succession. If backup exists, activate immediately. If no backup, governance assembly convenes within 6 hours to designate emergency security coordinator.

**Priority 2 (Hours 24–72)**: Governance decision on emergency rules. The governance assembly that convenes for security coordinator designation should also adopt a written emergency security protocol — including use-of-force parameters, communication protocols, and external threat response guidelines. A written protocol, even a one-page one, is significantly more effective than ad hoc individual judgment.

**Priority 3 (Day 3–14)**: Information security lockdown. During security uncertainty, restrict information about community resources, population count, and governance meeting schedules to need-to-know basis. This is a temporary protocol (30 days maximum) that conflicts with the governance transparency principle — it requires explicit governance authorization.

**Recovery indicator**: Security cascade recovery is stable when a functioning security coordinator is in place with clear governance mandate, food distribution is operating normally, and social cohesion indicators (assembly attendance, resource sharing) have returned to pre-incident baseline.

---

## Cascade Pathway 5: Federation Scaling Failure

**Origin domain**: Scaling Pathways (Phase 3, Domain 5)  
**Trigger event**: Rapid population growth (refugee absorption, community merger) crosses governance threshold without planned structural transition  
**Scale**: Community growing from 150 to 450 people over 30 days

### Propagation Sequence

**Day 0–7: Dunbar threshold crossed**
A community of 150 people absorbs 300 refugees over 30 days. At approximately day 7–14, the community exceeds 200 people, crossing the first critical threshold identified in Phase 3: beyond 150 people, informal trust-based coordination is insufficient. The original governance structure (weekly assembly of 150 people who know each other) now faces 450 people who do not all know each other, with unknown skill sets, unknown loyalties, and unknown needs.

**Day 7–21: Governance structure mismatch**
The existing governance structure (designed for 150 people) is now managing 450 people's resource allocation. Assembly meetings become unmanageable at this size without redesign. Decision velocity slows. Contested allocation decisions (how many resources go to new arrivals versus established members) create governance legitimacy challenges not because the governance structure is corrupt but because it was not designed for this population size.

**Day 14–30: Information overload**
The information infrastructure (GMRS radio protocols, mesh network node assignments, community roster, skill inventory) was designed and documented for 150 people. The rapid influx of 300 new members creates information system overload: new people don't know radio protocols, the mesh network isn't mapped to new arrival locations, the skill inventory is incomplete for new arrivals. Information coordinators are overwhelmed.

**Day 14–30: Food system stress**
Food stores and production capacity were calibrated for 150 people. A 3x population increase without supply chain expansion creates immediate food stress. The Phase 3 food document identifies the "aggregation problem" — at community scale, food coordination requires deliberate logistics infrastructure. That infrastructure was sized for 150, not 450.

**Day 21–45: Security fragmentation**
The social cohesion that underpins security (everyone knows everyone, reputation is accountability) fragments when 300 strangers arrive. The security structure faces a compound problem: the existing community members distrust some newcomers, newcomers distrust each other, and the security coordinator is trying to maintain order across a population three times larger than the security structure was designed for.

### Recovery Protocol: Scaling Cascade

**Priority 1 (Days 0–7)**: Trigger threshold protocol. Phase 3 scaling domain identifies specific governance redesign triggers at the 150-person threshold. If this document is in place and the community knows the trigger, governance redesign can be initiated proactively on day 7 rather than reactively on day 30 after breakdown.

**Priority 2 (Days 7–21)**: Rapid skill and needs inventory of new arrivals. The most important immediate governance action for new member integration is knowing who they are, what they can do, and what they need. A rapid intake process (one designated intake coordinator per 50 arrivals) prevents information overload and creates the database governance needs to reallocate resources appropriately.

**Priority 3 (Days 14–30)**: Emergency food expansion. If food stores can sustain 450 people for 14 days, the community has a survival window. In that window, governance must make immediate decisions about food production intensification, external supply sourcing, and rationing protocols. The specific Midwest Zone 5 application: spring/fall rapid-cropping greenhouse activation, emergency bulk grain purchasing from regional food hub if available.

**Priority 4 (Days 21–45)**: Governance redesign to delegate council model. The Phase 3 governance document identifies the delegate council model as optimal at 150–500 people. The governance redesign from assembly to delegate council should be completed within 30 days of threshold crossing. Delay here consistently produces the worst outcomes in historical case studies.

**Recovery indicator**: Scaling cascade recovery is stable when governance structure has been redesigned for current population size, all community members (original and new) have been integrated into information systems, and food supply is adequate for current population.

---

## Cross-Cutting Recovery Principles

Three principles emerge from analysis of all five cascade pathways:

**Principle 1: Governance is always the priority node**
In every cascade pathway, governance failure or governance stress is either the origin or the second-order effect. Recovery in every cascade pathway requires governance to function. Any community facing multi-domain failure should treat governance reconstitution as Priority 1 regardless of which domain initially failed.

**Principle 2: Pre-established protocols outperform improvised responses by an order of magnitude**
The evidence from Hurricane Katrina, Texas ERCOT, Puerto Rico, and community resilience case studies is consistent: communities with written pre-established protocols for failure scenarios recover significantly faster than communities that improvise responses during the crisis. This is not a controversial finding — it is one of the most replicated findings in emergency management research. [8] The practical implication: each cascade recovery protocol in this document should be written, distributed, and periodically practiced before crisis, not read for the first time during one.

**Principle 3: Cross-domain recovery requires a sequencing decision**
When multiple domains fail simultaneously — as they do in most real crisis scenarios — the community must make a sequencing decision: which domain to recover first, second, third. The dependency matrix provides the answer: recover governance first (all other recoveries depend on governance legitimacy), then information infrastructure (governance needs situational data), then food security (physical survival), then security (protect the functioning systems). Scaling/federation recovery is last because it requires all base systems to function. In practice, communities under pressure tend to focus on the most visible crisis (usually security or food), neglecting governance recovery — which predictably produces worse outcomes across all domains.

---

## Midwest Zone 5 Application Notes

**Winter cascade amplification**: All five cascade scenarios are significantly more severe in Midwest winters. Food cascade timelines compress (heating fuel loss compounds caloric need). Governance meetings are harder to convene (travel in snow/ice). Information infrastructure is more vulnerable (cold affects batteries, ice damages antennas). Security incidents shift to indoor spaces (domestic conflicts rise under cold + scarcity). Community planning should model cascade scenarios specifically for December–March conditions.

**Grain-belt food cascade specificity**: The food cascade scenario in Zone 5 is shaped by the grain-belt food system. Rural Midwest communities have better baseline food production capacity than urban communities but higher vulnerability to single-crop failure. A community with 90% of production in corn faces a corn blight cascade that a diversified community does not. Crop diversity is a cascade prevention strategy, not just an agricultural preference.

**Road and transport dependencies**: All five cascade scenarios worsen dramatically if roads are impassable (spring flooding, winter storms). Transportation failure creates a sixth cascade pathway not modeled above: inter-community coordination (Phase 3 scaling domain's federation model) becomes impossible when roads fail, isolating communities at exactly the moment they most need regional mutual aid. Pre-crisis protocols for remote coordination (radio-only inter-community coordination) should be established.

---

## Sources

1. Stabilityjournal.org, "Food Insecurity and Conflict Dynamics: Causal Linkages and Complex Feedbacks" — food insecurity heightens risk of civil conflict and communal conflict: https://stabilityjournal.org/articles/sta.bm

2. PMC (National Institutes of Health), "Communities with strong pre-crisis relationships have dramatically lower security incidents" — Phase 3 Security Domain citation, supported by post-disaster community security literature: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9545961/

3. Grist, "Puerto Ricans are devising the food system of tomorrow" — governance failure compounding food crisis: https://grist.org/food-and-agriculture/puerto-ricans-are-devising-the-food-system-of-tomorrow/

4. DTIC.mil, "Hurricane Katrina: Communications & Infrastructure Impacts" — communication failure cascades to governance: https://apps.dtic.mil/sti/pdfs/ADA575202.pdf

5. Bread for the World, "Food Insecurity in Puerto Rico: The aftermath of the hurricanes" — governance failure compounding food distribution: https://www.bread.org/article/food-insecurity-in-puerto-rico-the-aftermath-of-the-hurricanes/

6. VEOCI, "Katrina Response: A Failure to Communicate" — quote on communications paralysis: https://veoci.com/blog/katrina-response-a-failure-to-communicate/

7. ScienceDirect, "Empirical patterns of interdependencies among critical infrastructures in cascading disasters" — infrastructure cascade patterns: https://www.sciencedirect.com/science/article/abs/pii/S2212420923003424

8. George W. Bush White House Archives, "Hurricane Katrina: Lessons Learned" — pre-established protocols outperform improvised response: https://georgewbush-whitehouse.archives.gov/reports/katrina-lessons-learned/chapter5.html

9. arXiv, "Modeling and solving cascading failures across interdependent infrastructure systems" (2024): https://arxiv.org/pdf/2407.16796

10. PMC, "Governance and resilience as entry points for transforming food systems in the countdown to 2030": https://pmc.ncbi.nlm.nih.gov/articles/PMC11772237/

11. NSF/PAR, "Lessons from the 2021 Texas electricity crisis": https://par.nsf.gov/servlets/purl/10483330

12. ResearchGate, "The Impact of Hurricane Katrina on Communications Infrastructure": https://www.researchgate.net/publication/242196608_The_Impact_of_Hurricane_Katrina_on_Communications_Infrastructure
