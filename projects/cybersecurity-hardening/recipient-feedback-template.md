---
title: "Recipient Feedback Template — Tier 1 Distribution"
project: cybersecurity-hardening
created: 2026-05-05
revised: 2026-05-05
status: production-ready
use: Survey (async email) + interview script (synchronous call or Signal exchange)
companion: tier-1-effectiveness-framework.md, tier-1-feedback-collection-protocol.md
---

# Recipient Feedback Template

**Purpose**: Structured feedback collection from the 33-organization Tier 1 amplifier cohort at the 90-day mark. Cohort sectors: digital rights organizations, academic cybersecurity programs, researcher communities, and journalist organizations. Used in two modes: (1) async email survey for contacts who have engaged but are unlikely to take a call, and (2) interview script for contacts who have indicated willingness to discuss in depth (Stage 2+, meaning they are either actively using, citing, or distributing the corpus).

**Design principle**: The hardest implementation feedback to collect is also the most valuable — what prevented adoption, not what enabled it. Most survey instruments optimize for positive confirmation. This template is calibrated to surface barriers and gaps because those are the inputs that drive corpus revision before Phase 2. Every question has an explicit "what you are listening for" note and a "Phase 2 implication" note, because every answer should map to a specific Phase 2 decision.

**Duration**: Async survey: 5–8 minutes. Interview script: 25–40 minutes. Skip questions where you already have the answer from prior exchanges.

**Privacy**: Do not record or transcript calls without explicit consent. Do not attribute specific quotes to organizations without permission. Use anonymized aggregates in any public-facing reporting ("two immigration legal aid organizations reported...").

---

## Part 1: Async Email Survey (Day 90)

Send to all contacts at Stage 1 or above who have not explicitly opted out. The survey uses checkboxes for speed and a single open-text slot per question. Even a partial reply (checkboxes only, no open text) produces usable data.

---

**Subject**: Three months in — quick check-in on the ICE surveillance threat model (5 minutes)

> Hi [Name],
>
> Three months since I sent the digital security guide and ELITE threat model documentation. A few specific questions — reply with whatever you have. Checkboxes only is fine. Even "none of the above" is useful.
>
> ---
>
> **Q1 — Did your organization look at it?**
> - [ ] Yes — [Name] reviewed it
> - [ ] We shared it with [team, department, or partner org]
> - [ ] It's on the list but hasn't happened yet
> - [ ] Not the right fit for our work right now
>
> *If you checked "shared it": who did you share it with? (One line — org name or role is enough.)*
>
> ---
>
> **Q2 — If anyone looked at it: what section mattered most?**
> - [ ] The threat model (what the ELITE/Palantir system does and its primary data sources)
> - [ ] Part 0 (data broker opt-outs — the immediate action section for at-risk individuals)
> - [ ] The implementation guide (device setup, Signal, Tor, VeraCrypt)
> - [ ] The California DROP platform pathway (AB 60 → DELETE Act for undocumented residents)
> - [ ] The sourcing and primary documentation (FOIA disclosures, government contracts)
> - [ ] Haven't gotten to it yet
>
> ---
>
> **Q3 — What's the biggest gap?**
> What should the guide cover that it doesn't — or what was missing for your specific work or audience?
>
> (One sentence is fine. "No gap" is a valid answer. A specific scenario or use case that came up is the most useful answer.)
>
> ___
>
> ---
>
> **Q4 — What made it harder to use or share than expected?**
> - [ ] Too long to forward as a single resource — a shorter summary would help
> - [ ] Gist URL format is hard to distribute internally or include in a publication
> - [ ] The sourcing needs peer review or institutional vetting before we can cite it
> - [ ] The threat model covers confirmed capabilities but doesn't note uncertainty or limitations explicitly enough
> - [ ] Staff capacity — couldn't prioritize during a busy period
> - [ ] We need a version formatted for a specific use (print, course syllabus, training slide deck)
> - [ ] Other: ___
>
> ---
>
> **Q5 — Is the threat model sourced well enough to use publicly?**
> The guide's threat model is based on Palantir government contracts, FOIA disclosures, court filings, and government data-sharing agreements. Is that level of sourcing sufficient for your organization to cite, link to, or share with your audience?
> - [ ] Yes — the sourcing is sufficient for our use
> - [ ] Partially — the primary sources are solid but the interpretation needs strengthening
> - [ ] No — we'd need independent verification before citing
> - [ ] Can't assess — we haven't reviewed the sourcing in detail
>
> *If partially or no: what would make the sourcing stronger for your context?*
>
> ___
>
> ---
>
> **Q6 — Who else should have this?**
> A colleague, partner org, or network that would find this directly useful:
>
> ___ (Name/org, or just "type of org" if you prefer)
>
> ---
>
> That's the full ask. Reply with whatever you have — even one checkbox per question is useful.
>
> [Your name]

---

## Part 2: Interview Script (Stage 2+ Contacts, 25–40 minutes)

For contacts who indicate willingness to speak in depth. Use for synchronous calls or Signal exchanges. Before starting: review what you already know from their prior replies. Skip questions where email responses already provided a clear answer — the interview deepens, it does not repeat.

---

### Opening (2 minutes)

> Thanks for making time. I have four areas: adoption barriers, content gaps, threat model accuracy, and how the guide fits your sector specifically. We can stop at any point and I'll take whatever you're comfortable sharing.
>
> One ground rule: I won't attribute anything to [Organization] by name without asking you first. Everything I use from this conversation will be anonymized unless you say otherwise. OK?

---

### Section A: Adoption Barriers (8–10 minutes)

These questions diagnose what delayed or prevented implementation, citation, or sharing. The goal is to understand the obstacle before assuming a content fix is the right solution. For this cohort (digital rights, academic, researcher, journalist organizations), the most common barriers are credibility/sourcing concerns, format friction, and internal vetting requirements — not technical capacity.

**A1. Where did the guide land?**

> When the guide arrived, where did it go in your organization? Did it reach someone who could act on it directly — who could review, share, or publish it — or did it need routing first?

*What you are listening for*: Routing failure (general inbox instead of the relevant policy team, security team, or faculty). For digital rights organizations, the relevant person is a staff attorney, security researcher, or policy analyst — not a communications or development staffer. For academic programs, the relevant person is a faculty researcher or department director, not a department administrator.

*Phase 2 implication*: If routing failure appears in 2+ organizations in the same sector, the Phase 2 contact list for that sector needs to identify role-specific contacts. A Sector A organization should be addressed to its surveillance policy team, not its press address. A Sector B academic program should be addressed to a faculty researcher, not the department's general inquiry address.

> Did it eventually reach the right person? What happened?

**A2. Internal vetting and credibility threshold**

> Did your organization have an internal review process for the threat model before it could be used or shared publicly? What does that process look like — who reviews new research before your org cites or publishes it?

*What you are listening for*: Whether the corpus passed the organization's credibility bar, or whether it is still in review. Digital rights organizations and academic programs often have explicit review standards — EFF's team vets security research claims before publishing; university programs require peer review or institutional sign-off before citing non-peer-reviewed sources. Understanding the vetting process for each sector tells you how to strengthen Phase 2 submissions.

*Phase 2 implication*:
- If the vetting concern is sourcing depth: add a sourcing appendix listing primary sources with direct links
- If the vetting concern is author credentialing: consider whether a co-publication or endorsement from an established organization would satisfy the credibility threshold
- If the vetting concern is claims accuracy: offer to share the underlying documentation for independent review before publication

**A3. Format friction**

> The guide was distributed as a Gist link. Was that format easy to work with — easy to review, share internally, or include in your own resources?

*What you are listening for*: Format barriers specific to this cohort. Digital rights organizations often want PDFs they can post on their website or include in resource guides. Academic programs often want documents formatted for course management systems. Journalist organizations often want printable, citable documents with clear authorship and date. A Gist is a functional format for reading but a poor format for institutional distribution.

*Phase 2 implication*: If 3+ organizations in any sector cite format as a barrier, produce a PDF version with a clear title, date, and authorship line before Phase 2. This is a 2-hour fix with high adoption-barrier resolution value for institutional audiences.

**A4. Capacity and timing**

> Did staff or faculty capacity affect whether anyone had time to review this? Was there a point when the timing felt wrong — a deadline, a major campaign, a semester transition?

*What you are listening for*: Timing effects. Digital rights organizations have publication and campaign cycles that absorb bandwidth. Academic programs have semester transitions where faculty are unavailable. Journalist organizations have editorial cycles. A well-timed re-engagement window — after a major campaign ends, at the start of an academic term, after a news cycle breaks — can produce a different outcome than the initial send.

*Phase 2 implication*: If timing was the barrier, not content, the corpus does not need revision. Note the contact's bandwidth cycle and plan a re-engagement window accordingly. For academic programs: January (start of spring term) and August (start of fall term) are the optimal re-engagement windows.

**A5. Differentiation from existing resources**

> Are there other surveillance threat models or security guides your organization already uses or recommends? Where does this guide fit relative to what you already have?

*What you are listening for*: Whether the corpus is perceived as redundant. EFF, CDT, and similar organizations already have surveillance threat resources and security guides. If the corpus is not clearly differentiated from what they already have, they have no adoption incentive. The specific differentiators to probe: the ELITE/Palantir contract documentation, the DROP platform pathway (California-specific), the behavioral tier structure, and the integration of data broker sourcing with device hardening guidance.

*Phase 2 implication*: If an organization cannot name what the corpus does differently from existing resources after reading it, the Phase 2 cover message needs to lead with explicit differentiation before asking for engagement.

---

### Section B: Guide Gaps (8–10 minutes)

These questions identify missing content — scenarios the guide does not address, not features the recipient would like to see.

**B1. A scenario the guide didn't cover**

> Think about a client situation you've encountered in the past few months that felt like a security risk. Was there anything in that situation the guide didn't address?

*What you are listening for*: Specific operational scenarios — a client whose landlord may be informing to authorities; a client who had already been stopped by ICE and wanted to know if their device was compromised; a mixed-status family where one member was a DACA recipient and another was undocumented. These are real Tier 1 threat scenarios that may not map to the corpus's current structure.

*Examples of high-priority missing scenario signals*:
- "Client was detained and their phone may have been searched — what do they do now?" → post-detention scenario, not currently in any section; high-stakes gap
- "Client's employer is reporting to ICE — the risk is at work, not at home" → employer surveillance vector not currently addressed
- "Client is a DACA recipient worried about DOGE-related admin database access" → distinct from undocumented threat tier; may need separate guidance

**B2. The California DROP platform path**

> For California-based organizations — did the section on the California DELETE Act DROP platform and the AB 60 ID pathway make sense? Were there steps missing, or was it hard to explain to clients without a driver's license?

*What you are listening for*: Procedural gaps in the DROP platform walkthrough. The AB 60 → DELETE Act pathway is the corpus's most distinctive contribution for California-based undocumented residents. Any report that it was unclear or incomplete is a Category (a) wording fix with high priority — this section is the highest-confidence attribution signal for corpus impact.

> Did clients attempt the DROP platform enrollment? What did they encounter?

**B3. What happens after the opt-outs**

> Did clients or staff ask what happens after completing the opt-outs — whether brokers actually process them, how long it takes, whether it makes a meaningful difference?

*What you are listening for*: A gap in the guide around outcome expectations. The guide documents how to opt out but does not adequately explain what to expect after opting out. Unrealistic expectations (belief that opt-outs make someone invisible to ICE immediately) are a potential harm; under-realistic expectations (belief that opt-outs do nothing) undermine motivation. Both require additions.

*Phase 2 implication*: If this gap is mentioned by 2+ organizations, add a "What to expect after opting out" section: broker processing timelines (60–90 days for most), DROP platform timeline (August 1, 2026 broker processing deadline), partial vs. complete removal, and a realistic statement about what opt-outs accomplish vs. what they cannot.

**B4. Missing populations**

> Are there populations your organization serves that the guide doesn't seem written for? Elderly clients, clients without smartphones, DACA recipients vs. undocumented, mixed-status families?

*What you are listening for*: The guide's implicit population is mobile-phone-enabled, English-literate or Spanish-literate, individually at risk. Populations outside these parameters — clients with disabilities, elderly clients, clients in detention-adjacent housing — may require different countermeasure logic.

*Phase 2 implication*: Document any population gap. If a specific gap is mentioned by 2+ organizations, it becomes a required section for the next version before Phase 2 distribution to community organizations. If mentioned by 1 organization, document and note as a Phase 2 enhancement.

---

### Section C: Threat Model Accuracy (6–8 minutes)

These questions determine whether the guide's description of ELITE and its data sources matches what organizations observe on the ground. This is the most important feedback to collect for long-term credibility.

**C1. Does the ELITE documentation match what you observe?**

> The guide's threat model describes ICE using Palantir's ELITE system to generate deportation targeting scores by pulling from data brokers, Medicaid records, and DMV records. Does that match what you're seeing in your clients' cases — how ICE seems to be finding people?

*What you are listening for*: Ground-level corroboration or contradiction. If attorneys say their clients are being found through employer records, school records, or social media rather than the commercial data broker pipeline, that is Category (c) feedback — the guide's emphasis on data broker opt-outs may be overweighted.

*Phase 2 implication*:
- **If confirmed accurate**: This is Phase 2 social proof. "Immigration attorneys at [Tier 1 org type] have confirmed the threat model accurately describes the risks their clients face." Quote-permissioned if possible.
- **If partially accurate**: Document the discrepancy specifically. Determine whether the additional threat vector (employer records, utility records, social media) is documented in any primary source. If yes, add to threat model. If anecdotal, add to "Known gaps and limitations."
- **If inaccurate in a confirmed pattern**: Category (c) response — HOLD Phase 2, update threat model, re-verify with this organization before continuing.

**C2. Threat tier structure**

> The guide divides risk into tiers — Tier 1 (general population with low enforcement history), Tier 2 (individuals with prior encounters or in removal proceedings), Tier 3 (individuals facing active surveillance). Did that tier structure map onto how your organization thinks about client risk levels?

*What you are listening for*: Whether the tier framework resonates with practitioners who are already assessing client risk. If legal aid organizations use a different risk categorization in their practice (and many do — the "priority" framework from the Obama-era DHS memos still shapes legal practice), the guide's tier structure may create friction rather than alignment.

*Phase 2 implication*: If the tier structure conflicts with how practitioners already categorize clients, add a "Mapping to existing practitioner risk frameworks" note that translates between the corpus's tier language and the frameworks attorneys already use.

**C3. Temporal updates**

> The guide was built from documents available in early 2026. Have you seen any developments since then — new data sources ICE is using, new enforcement patterns, new risks — that the guide doesn't reflect?

*What you are listening for*: Temporal gaps. If there have been FOIA disclosures, court filings, or enforcement incidents since the corpus was written that reveal new ELITE capabilities or data sources, those need to be incorporated before Phase 2.

*Phase 2 implication*: Any temporal update confirmed by primary source must be incorporated before Tier 2 distribution to digital rights organizations and academic programs — those audiences will notice outdated threat model documentation.

---

### Section D: Organizational Fit and Phase 2 Readiness (5–7 minutes)

These questions identify how the guide was actually used and what Phase 2 framing will resonate with broader audiences.

**D1. Most useful actual use**

> Looking back at the past three months — what is the most useful thing the guide ended up doing for your organization, even if it wasn't how you expected to use it?

*What you are listening for*: Unanticipated use cases that signal Phase 2 framing angles:
- "It's the best-sourced single document we've seen on Palantir's government contracts" → lead Phase 2 with sourcing quality for policy and journalism audiences
- "We're using it to update our own surveillance threat briefings" → lead Phase 2 with the framing "organizations publishing their own threat analyses have been using this as a foundation"
- "A faculty member is citing it in a paper on commercial surveillance-as-service" → lead Phase 2 with academic rigor framing
- "We recommended it to a source who was worried about ICE" → the corpus is being used as an operational resource, not just a policy document — this is a high-value signal for journalist training programs

**D2. Sector generalizability**

> In your network — organizations doing similar work — do you think this guide would be useful to them, or would they face the same barriers you experienced?

*What you are listening for*: Whether the barriers this organization faced are idiosyncratic or structural to the sector. If structural, Phase 2 framing for that sector needs to acknowledge and address the barrier directly. If idiosyncratic, proceed to Phase 2 without changes.

*Phase 2 implication*:
- "All organizations like us want primary-source citations before we can share it publicly" → structural credibility barrier for Sector A; Phase 2 should provide a sourcing reference document as a companion to the corpus
- "Our specific issue was our editorial backlog, but other orgs wouldn't have that" → idiosyncratic timing barrier; proceed to Phase 2 as planned for this sector
- "Researchers I know would find this useful — the FOIA sourcing is actually better than most academic sources on this" → strong Phase 2 signal for Sector C and Sector B outreach framing

**D3. What would make this more citable or shareable**

> If you were going to share or cite this more widely — what would you need that isn't currently there?

*What you are listening for*: Specific format or credibility additions that would unlock broader sharing. Common answers from this cohort:
- "A clear author or organizational affiliation — anonymity creates credibility questions" → Phase 2 decision point: maintain anonymity or provide organizational context
- "An abstract or executive summary formatted as a standalone page" → 2-hour fix; produce a one-page brief version for institutional sharing
- "A version that's been reviewed or endorsed by [named organization]" → Phase 2 strategy: request endorsement from highest-Stage Sector A contact before Phase 2 launch
- "More explicit uncertainty language — 'confirmed in X court filing' vs. 'believed to include' — so we know which claims are verified vs. inferred" → high-value improvement to the threat model's epistemics for academic and journalist audiences

---

### Closing (2 minutes)

> That covers everything I wanted to ask. Anything that came up in our conversation you'd want me to know — something I didn't ask about?

> One last question: if I improve the guide based on feedback like yours and reach out to broader audiences for the next distribution phase — would [Organization] be willing to be named as an early user or reviewer? Even a general description ("a digital rights organization" or "an academic cybersecurity program") helps enormously with credibility. No obligation, and I understand if you prefer to stay anonymous.

*If yes*: Log as "named citation permitted." Record what specifically they are comfortable with being cited on (e.g., "used guide in client intake" vs. "confirmed threat model accuracy" — these are different and you may need both separately).

*If no*: Log as "anonymous only." Use organization type but not name in any Phase 2 communication ("a Tier 1A immigration legal aid organization confirmed...").

---

## Part 3: Aggregation Key

After collecting survey and interview data at the 90-day mark, aggregate responses into these four categories before making Phase 2 decisions. The aggregation should produce a one-page summary that drives the Phase 2 launch assessment.

### A. Adoption Barriers Summary

| Barrier | Count | Organizations (sector) | Triage Category | Phase 2 Action Required |
|---------|-------|----------------------|-----------------|------------------------|
| Credibility / sourcing concern (won't cite without verification) | | | (a) sourcing fix | Add sourcing reference document with primary source links |
| Format (PDF needed, not Gist) | | | (a) format | Produce PDF version before Phase 2 sends |
| Too long / needs executive summary | | | (a) format | Produce 1-page brief version |
| Author/affiliation anonymous — reduces institutional credibility | | | Decision point | Assess whether to provide organizational context |
| Internal vetting backlog (will review, hasn't yet) | | | Neither — re-engage later | Flag for 30-day re-engagement |
| Wrong routing (general address instead of relevant team/faculty) | | | Neither — contact fix | Update contact list with role-specific contacts |
| Staff/faculty capacity (timing, not content) | | | Neither — timing | Note; re-engage at semester start or after campaign cycle |
| Redundancy with existing resources (not differentiated) | | | (d) framing fix | Revise cover message to lead with differentiators explicitly |
| Uncertainty language insufficient (can't distinguish confirmed vs. inferred claims) | | | (b) missing section | Add epistemics annotations to threat model claims |

**Decision rule**: Any barrier cited by ≥3 organizations is a required fix before Phase 2 launch. Barriers cited by 1–2 organizations are Phase 2 enhancements. Routing and timing barriers are not content problems — do not revise corpus in response to them.

### B. Guide Gaps Summary

| Gap | Count | Organizations (type) | Priority | Phase 2 Timing |
|-----|-------|----------------------|----------|----------------|
| DROP platform instructions incomplete | | | Critical | Fix before any Phase 2 |
| Post-opt-out outcome expectations missing | | | High | Required if ≥2 orgs cite |
| Post-detention scenario missing | | | High | Required if ≥1 org cites |
| Specific population not addressed | | | Medium | Required if ≥2 orgs cite |
| Temporal update needed (new ELITE sources) | | | Critical if factual | Fix before Phase 2 if confirmed |

### C. Threat Model Accuracy Summary

| Assessment | Count | Organizations (type) |
|------------|-------|----------------------|
| Confirmed accurate across the board | | |
| Partially accurate (specific discrepancies noted below) | | |
| Inaccurate in confirmed pattern: [describe] | | |
| Can't assess (insufficient enforcement visibility) | | |

Discrepancies noted:
- 
- 

**Decision rule**: Any factual inaccuracy confirmed by ≥1 organization requires primary-source verification before Phase 2. One organization is sufficient for a Category (c) hold — do not wait for corroboration before investigating.

### D. Phase 2 Readiness Indicators

For each Phase 2 audience segment, which Tier 1 signal is present? This cohort (33 organizations across Sectors A–D) constitutes the Tier 1 amplifier layer. Phase 2 will reach broader public, policymaker, or practitioner audiences who will rely on this cohort's adoption as social proof.

| Phase 2 Audience Segment | Required Tier 1 Signal | Signal Present? | Source (anon) | Phase 2 Framing |
|---|---|---|---|---|
| Policymakers and legislative staff | Sector A org (EFF, CDT, Privacy International) has cited or linked to corpus in any published output | Y/N | | "Leading digital rights organizations have been using this threat model to..." |
| Broader civil society / advocacy coalitions | Sector A or D adoption confirmed; ≥2 organizations at "Understood" level | Y/N | | "Organizations working on digital rights and journalist protection have..." |
| Technical practitioner communities | Sector C researcher adoption confirmed; any technical critique incorporated | Y/N | | "Security researchers have reviewed and contributed to the threat model..." |
| Academic / research audiences | Sector B academic program has indicated curriculum interest or citation intent | Y/N | | "Academic cybersecurity programs are integrating this into..." |
| Media and public audiences | Sector D journalist org has incorporated into training OR published coverage exists | Y/N | | "Journalist security organizations have incorporated this..." |

**Decision rule**: Phase 2 outreach to a given audience segment requires its specific Tier 1 signal. Do not lead with social proof that is not present. If a required signal is absent, Phase 2 outreach to that segment should be delayed — not because the corpus is insufficient, but because the framing will be weaker without corroboration from a recognizable institutional source.

**Cross-sector rule**: If signals are present from ≥3 of 4 sectors, Phase 2 outreach may use multi-source framing: "Organizations across the digital rights, academic, and journalist security communities have engaged with this threat model." This framing is stronger than any single-sector citation for general audiences.

---

*Template complete. Calibrated for the 33-organization amplifier cohort (digital rights, academic cybersecurity, researcher communities, journalist organizations). The async email survey (Part 1) deploys at Day 90. The interview script (Part 2) deploys for any Stage 2+ contact who indicates willingness to speak. Log all responses in the feedback tracking spreadsheet. Cross-reference Section 5 of `tier-1-effectiveness-framework.md` for the four-category triage framework (wording fix / missing section / wrong threat model / framework isn't landing) and the Go/No-Go decision tree in Section 6.*

*Note: A separate feedback template for the direct-service cohort (12 organizations: immigration legal aid, community-based, mutual aid) uses the prior version of this document's Q4 (phone-first clients, Spanish gap, legal documentation concerns) and the Q5 framing about ground-level threat model observation. Do not use the amplifier cohort template for the direct-service cohort — the barriers and feedback goals are structurally different.*

*Last revised: 2026-05-05*
