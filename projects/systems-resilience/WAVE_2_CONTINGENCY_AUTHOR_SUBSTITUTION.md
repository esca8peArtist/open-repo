# Wave 2 Contingency: Author Substitution & Fallback Activation
## Systems-Resilience Project | Domains 60–65

**Document Version**: 1.0  
**Effective Date**: June 2026  
**Status**: Production-Ready  
**Last Updated**: 2026-06-14

---

## 1. Decision Tree: Author No-Show Protocol

### 1.1 Trigger Conditions

An author is classified as **no-show** if:

- **T+3 (72 hours after submission window close)**: No email response from orchestrator's initial outreach
- **T+7 (7 days after submission window close)**: No draft or partial submission received
- **T+10 (10 days after submission window close)**: No acknowledgment from author despite two reminders

### 1.2 Decision Flow

```
┌─────────────────────────────────────┐
│  Author No-Show Detected (T+3)      │
│  Trigger: No response to reminder   │
└────────────┬────────────────────────┘
             │
             v
┌─────────────────────────────────────┐
│  Step 1: Escalation Attempt (T+3)   │
│  Send urgent email + Slack ping     │
│  Set callback expectation: T+5      │
└────────────┬────────────────────────┘
             │
             v
   ┌─────────────────────────────┐
   │ Response by T+5?            │
   └──────┬──────────────────┬───┘
    YES   │                  │   NO
          v                  v
    ┌──────────────┐  ┌─────────────────────────┐
    │ Accept draft │  │ Step 2: ALT Activation  │
    │ via extended │  │ (T+5)                   │
    │ review track │  │ Invite secondary Tier B │
    └──────────────┘  │ author for domain      │
                      └────────┬────────────────┘
                               │
                               v
                     ┌─────────────────────────┐
                     │ ALT accepts offer?      │
                     └──────┬──────────────┬───┘
                      YES   │              │   NO
                            v              v
                       ┌──────────┐   ┌─────────────────┐
                       │ Continue │   │ Step 3: EXT Pool│
                       │ with ALT │   │ Activation (T+7)│
                       │ T+7 start│   │ Invite EXT-01   │
                       └──────────┘   │ through EXT-10  │
                                      └────────┬────────┘
                                               │
                                               v
                                     ┌─────────────────────┐
                                     │ Any EXT accepts?    │
                                     └──────┬──────────┬───┘
                                      YES   │          │   NO
                                            v          v
                                       ┌───────┐  ┌──────────────┐
                                       │EXT    │  │ Step 4: Phase3│
                                       │starts │  │ Escalation   │
                                       │T+10  │  │ (T+14)       │
                                       └───────┘  │ Domain defer-│
                                                  │ red; reason  │
                                                  │ documented  │
                                                  └──────────────┘
```

---

## 2. Per-Domain Contingency Routing

### 2.1 Primary Author → ALT Pool → EXT Pool Hierarchy

| Domain | Primary Tier | ALT (Tier B, Secondary) | EXT Fallback | Notes |
|--------|--------------|------------------------|--------------|-------|
| **60** International Coordination | [Named Author] | Martha Santos | EXT-02 (David Greenberg) | Crisis response expertise required |
| **61** Intergenerational Knowledge | [Named Author] | David Greenberg | EXT-09 (James Akomea) | Education/anthropology background |
| **62** Infrastructure Resilience | [Named Author] | [ALT TBD] | EXT-08 (Patrick Carolan) | Engineering or systems planning |
| **63** Ecosystem Restoration | [Named Author] | [ALT TBD] | EXT-05 (iFixit) | Ecology or land management focus |
| **64** Economic Resilience | [Named Author] | Michael Linton | EXT-03 (La Via Campesina) | Alternative economics expertise |
| **65** Institutional Learning | [Named Author] | [ALT TBD] | EXT-07 (Post Carbon Institute) | Organizational/systems analysis |

### 2.2 EXT Pool Candidate Index

**EXT-01**: Cooperative Extension System (Land-Grant Universities)
- Expertise: Agricultural systems, community resilience, local adaptation
- Contact: Regional extension director (varies by state)
- Tier commitment: Secondary author, 10–15 hour engagement

**EXT-02**: La Via Campesina (International Peasant Movement)
- Expertise: Food sovereignty, agroecology, international coordination
- Contact: regional@viacampesina.org
- Tier commitment: Secondary author, 12–18 hour engagement

**EXT-03**: CARE International
- Expertise: Humanitarian response, household resilience, livelihoods
- Contact: policy@care.org
- Tier commitment: Secondary author, 10–12 hour engagement

**EXT-04**: Post Carbon Institute
- Expertise: Climate adaptation, systems thinking, institutional change
- Contact: research@postcarbon.org
- Tier commitment: Co-author or extended author, 12–15 hour engagement

**EXT-05**: iFixit (Repair Community)
- Expertise: Infrastructure repair, community resilience, right-to-repair
- Contact: editorial@ifixit.org
- Tier commitment: Secondary author, 8–10 hour engagement

**EXT-06**: Transition Network (UK-based)
- Expertise: Community transition, localism, social infrastructure
- Contact: hello@transitionnetwork.org
- Tier commitment: Contributing author, 10–12 hour engagement

**EXT-07**: Oral History Association
- Expertise: Intergenerational knowledge capture, documentary methods
- Contact: info@oralhistory.org
- Tier commitment: Secondary author, 10–14 hour engagement

**EXT-08**: Patrick Carolan (Agronomist, Rodale Institute)
- Expertise: Soil science, regenerative agriculture, systems resilience
- Contact: [Individual via Rodale]
- Tier commitment: Co-author, 15–20 hour engagement

**EXT-09**: James Akomea (Community Education, Ghana)
- Expertise: Intergenerational learning, indigenous knowledge, pedagogy
- Contact: [Individual via UNDP or regional education networks]
- Tier commitment: Secondary author, 12–18 hour engagement

**EXT-10**: Michael Linton (Community Exchange Systems)
- Expertise: Local currencies, timebanking, economic alternatives
- Contact: michael@community-exchange.org
- Tier commitment: Co-author or contributor, 10–15 hour engagement

---

## 3. Timeline Impact Analysis

### 3.1 Contingency Activation: Delay Scenarios

#### Scenario A: Author No-Show Detected at T+1 (Immediate)

**Action**: Activate ALT tier immediately upon detection

| Phase | Timeline | Activity | Publication Impact |
|-------|----------|----------|-------------------|
| Escalation | T+1 to T+3 | ALT author receives offer; accepts/declines | None if ALT accepts by T+3 |
| Delivery | T+3 to T+10 | ALT completes draft (compressed 7-day window) | +0 days if on schedule |
| Review | T+10 to T+21 | Peer review + orchestrator feedback (normal) | +0 days |
| **Total publication delay** | | | **0 days** (Wave 2 stays T+28) |

**Conditions**: ALT must accept by T+3 and deliver by T+10 (compressed timeline with support escalation).

#### Scenario B: Author No-Show Detected at T+7 (Peer Review Closure)

**Action**: Activate ALT tier at T+7; escalate to EXT pool if ALT declines by T+9

| Phase | Timeline | Activity | Publication Impact |
|-------|----------|----------|-------------------|
| ALT outreach | T+7 to T+9 | ALT receives offer; response deadline T+9 | None if ALT accepts by T+9 |
| Delivery | T+9 to T+16 | ALT completes draft (compressed 7-day window) | +1 week if ALT accepts late |
| Peer review | T+16 to T+23 | Compressed peer review (expedited) | +0 days (parallel with orchestrator) |
| **Total publication delay** | | | **+3 to 7 days** (Wave 2 shifts to T+31–35) |

**Conditions**: ALT must respond by T+9 and deliver draft by T+16. EXT activation occurs at T+9 if ALT declines.

#### Scenario C: Author & ALT No-Show (T+14, EXT Activation)

**Action**: Activate EXT pool author at T+14; escalate to Phase 3 if EXT declines by T+18

| Phase | Timeline | Activity | Publication Impact |
|-------|----------|----------|-------------------|
| EXT outreach | T+14 to T+18 | EXT candidate receives offer; response window 4 days | Large delay expected |
| Negotiation | T+18 to T+21 | EXT author scope/timeline agreement | Domain-specific |
| Delivery window | T+21 to T+28 | EXT completes draft (max 7 days; may extend) | **+7 to 14 days** (T+35–42) |
| **Total publication delay** | | | **+7 to 14 days** (Wave 2 partially deferred) |

**Conditions**: EXT author may request scope reduction (500–800 word limit) or extended timeline. Phase 3 escalation recommended if EXT response is "conditional accept" (requires extra resources).

#### Scenario D: Complete Cascade Failure (Author + ALT + EXT Decline)

**Action**: Escalate domain to Phase 3 (deferred publication) at T+21

| Phase | Timeline | Activity | Publication Impact |
|-------|----------|----------|-------------------|
| Escalation | T+14 to T+21 | All tiers exhausted; Phase 3 decision gate | **Domain deferred** |
| Documentation | T+21 | Reason documented in archive; timeline provided for Phase 3 re-engagement | **Entire domain publication deferred** |
| **Total publication delay** | | | **Indefinite (Phase 3)** |

**Conditions**: Rare scenario. Typical alternative is "scope reduction + extended EXT author" at T+18.

### 3.2 Summary: Delay Impact by Activation Point

| Activation Point | Delay to Wave 2 | Peer Review Required? | Domain Salvageable? |
|------------------|-----------------|----------------------|---------------------|
| **T+0–T+3** (Immediate) | 0 days | Yes (normal) | Yes (ALT on track) |
| **T+5–T+7** | 0–3 days | Yes (compressed) | Yes (ALT with support) |
| **T+10–T+14** | 3–7 days | Yes (expedited) | Yes (EXT, scope flexible) |
| **T+18–T+21** | 7–14 days | Maybe (conditional) | Partial (Phase 3 candidate) |
| **T+21+** | 14+ days | No (Phase 3) | No (deferred) |

---

## 4. No-Show Communication Templates

### 4.1 T+3: Escalation Email to Author

**Subject**: Urgent: Wave 2 Submission – Domain ## [Author Name]

```
Dear [Author Name],

We have not yet received your submission for Domain ## of the Systems-Resilience Wave 2 framework, 
which was due on [Date T+0].

We understand that circumstances can change. Before activating our fallback author roster, 
we wanted to reach out directly:

1. Can you confirm receipt of the submission guidelines (attached)?
2. Can you provide a revised completion timeline (e.g., T+7, T+14, or unable to proceed)?
3. If unable to proceed, would you recommend a colleague who could co-author or take the lead?

We need a response by [Date T+5] to coordinate next steps. Our contingency protocols activate at T+5 
if we do not hear from you.

Please respond to this email or contact us via Slack: @orchestrator.

Best regards,
[Orchestrator Name]
Systems-Resilience Project Lead
```

### 4.2 T+5: ALT Activation Email

**Subject**: Wave 2 Author Invitation – Domain ## [ALT Author Name]

```
Dear [ALT Name],

We are reaching out with an opportunity to author a domain submission for the Systems-Resilience 
Wave 2 framework. Your expertise in [domain topic] is directly aligned with Domain ##: [Domain Title].

**Overview**:
- **Domain scope**: [1–2 sentence description of domain prompt]
- **Word count**: 1000–1500 words (flexible for ALT tier)
- **Citations**: Minimum 5 authoritative sources
- **Timeline**: Initial draft due [Date T+10]; revisions completed by [Date T+21]
- **Tier commitment**: ALT secondary author (Tier B: bi-weekly check-ins, 2–3 revision rounds)
- **Support**: Orchestrator will provide mentoring, peer review feedback, and editorial guidance

**Why we're asking you**:
[Primary author] was originally assigned to this domain, but circumstances have required us to activate 
our secondary author roster. Based on your background in [specific credentials], we believe you can 
deliver a compelling, research-backed submission.

**Next steps**:
Please confirm your interest and availability by [Date T+7]. If you accept, we will schedule a 30-minute 
kickoff call to discuss the domain prompt, scope, and timeline.

If you cannot commit at this time, we would appreciate any recommendations for colleagues who might be suitable.

Please reply to this email or contact: [orchestrator contact]

Best regards,
[Orchestrator Name]
```

### 4.3 T+9: EXT Pool Activation Email (If ALT Declines)

**Subject**: Wave 2 Guest Author Opportunity – Domain ## [EXT Name/Organization]

```
Dear [EXT Author/Organization Contact],

The Systems-Resilience project is inviting contributions from our extended partner network to complete 
Wave 2 submissions. We are seeking authors with expertise in [domain topic area] to author Domain ##: 
[Domain Title].

**This is a one-time, focused engagement**:
- Estimated time commitment: 12–18 hours over 14 days
- Word count: 1000–1200 words (flexible; we can negotiate scope)
- Citations: Minimum 5 sources (we can assist with research if needed)
- Support: Full editorial and peer review guidance provided
- Credit: Full author attribution + byline in published Wave 2 collection
- Timeline: Draft due [Date T+16]; final submission [Date T+21]

**Why we're reaching out**:
Your organization's work in [specific focus area] directly addresses the systems resilience framework. 
We believe your perspective would significantly strengthen Wave 2 outcomes.

**Next steps**:
If interested, please respond with:
1. Confirmation of availability and time commitment
2. Any scope modifications needed (e.g., shorter word count, specific sub-topic focus)
3. One page of background on the author (credentials, relevant publications)

Response deadline: [Date T+12] (48 hours for decision).

We understand this is short notice. If the timeline doesn't work, please suggest an alternative contributor 
from your network.

Best regards,
[Orchestrator Name]
```

### 4.4 T+18: Phase 3 Escalation Notice (If Both Decline)

**Subject**: Domain ## Deferred to Phase 3 – Documentation & Next Steps

```
Dear [Project Leadership and Domain Team],

After outreach to our primary author, secondary (ALT) candidate, and extended (EXT) partnership roster, 
we have been unable to secure an author for Domain ##: [Domain Title] within the Wave 2 timeline.

**Decision**: Domain ## is being deferred to Phase 3 publication (tentative: [Future Quarter/Year]).

**Documented reasons**:
1. Primary author [Name]: [Reason for unavailability – e.g., illness, project conflict, declined without response]
2. ALT candidate Martha Santos: [Reason – e.g., Competing deadline, insufficient domain expertise]
3. EXT candidates [Names]: [Reasons – e.g., All declined; insufficient capacity]

**Implications**:
- Wave 2 will publish on schedule (T+28) with 5 of 6 domains live
- Domain ## authorship will be revisited in Phase 3 planning (Q3/Q4 2026 proposal window)
- This domain remains a priority; we recommend early outreach to potential authors in the Phase 3 planning cycle

**Archive documentation**:
- This decision and supporting communication logs are filed in: `/projects/systems-resilience/wave-2-deferred/Domain_60/`
- Phase 3 reopening will be triggered by project leadership decision

Best regards,
[Orchestrator Name]
```

---

## 5. ALT Tier Author Support & Escalation

### 5.1 Support Protocol: When ALT is Activated as Primary

When an ALT (Tier B) author is activated as primary due to no-show:

**Tier B baseline**:
- Bi-weekly check-ins (scheduled, 30-min calls)
- Moderate autonomy (no pre-approval required for outline)
- 2–3 revision rounds (normal)
- Optional mentoring (available but not mandated)

**ALT-as-Primary escalation** (T+5 to T+21):
- **Upgrade to Tier A support**: Weekly check-ins (instead of bi-weekly)
- **Editorial pre-review**: Orchestrator reviews draft outline before full write (optional, available)
- **Expedited feedback**: Peer review feedback delivered within 3 days (instead of 7)
- **Contingency peer backup**: Dedicated standby peer reviewer if primary reviewer unavailable
- **Scope flexibility**: Can reduce word count to 900–1200 if needed (down from 1000–1500)
- **Citation support**: Librarian or research assistant available for literature review (2–3 hours)
- **Revision flexibility**: May request additional revision round if editorial feedback is substantial (T+28 deadline may shift to T+35)

**Communication cadence**:
- T+5: Kickoff call (scope confirmation, timeline, support resources review)
- T+10: Check-in call (draft outline + progress update)
- T+14: Feedback delivery (peer review compiled + orchestrator notes)
- T+18: Revision check-in (progress toward T+21 deadline)
- T+21: Final sign-off call (publication confirmation)

### 5.2 Authorship Split Rules: If Work is Partially Complete

**Scenario**: Author A delivers 50% of a domain submission (e.g., 2 of 4 major sections); contingency activation occurs at T+14.

**Options**:

**Option 1: Continuation by Secondary Author**
- ALT author (B) completes remaining 50% of work
- Final attribution: "Co-authored by [A] and [B]"
- Only (B) receives revision feedback for their sections
- Peer review updated to verify continuity of voice/argument flow
- Timeline: No delay if (B) delivers by T+21

**Option 2: Full Rewrite by Secondary Author**
- (B) completes entire submission independently (ignores A's 50% draft)
- Final attribution: "Authored by [B]; based on initial work by [A]"
- Preferred if voice/approach significantly mismatched
- (B) may use A's citations and research notes as source material
- Timeline: +2–3 days (B needs extra time for full re-conceptualization)

**Option 3: Hybrid (Orchestrator-Edited)**
- Keep A's strongest sections; have (B) complete gaps and integrate
- Final attribution: "By [A] and [B]"
- Orchestrator conducts continuity editing (adds 2–3 hours)
- Timeline: +3–5 days (orchestrator editorial time)

**Decision logic**:
- If A's work is >70% complete and >80% aligned with domain prompt → Option 1 (continuation)
- If A's work is <50% complete or significantly off-topic → Option 2 (full rewrite)
- If A's work is 50–70% but well-written + solid research → Option 3 (orchestrator hybrid)

### 5.3 Author Credit & Attribution

All contingency publications include a **note on author tier in the YAML front matter and byline**:

```yaml
---
title: "Domain 60: International Coordination in Crisis Response"
author: "Martha Santos"
author_tier: "ALT (secondary Tier B, activated due to primary author no-show)"
author_affiliation: "[Organization]"
author_credentials: "[...]"
publication_note: "This domain was authored by secondary candidate due to primary author unavailability on [T+5]. 
                   Author received Tier A support (weekly check-ins, expedited review) during compressed 16-day timeline."
---
```

**Byline example**:
"By Martha Santos (Systems-Resilience Project, ALT Author Tier, Wave 2 Secondary Candidate)"

---

## 6. Fallback Author Tier Assignment & Capacity

### 6.1 ALT Author Capacity Table

| Domain | Primary Author | ALT (Tier B, Secondary) | Capacity (hrs available) | Mentoring offered? |
|--------|----------------|------------------------|--------------------------|-------------------|
| **60** | [Name] | Martha Santos | 18 | Yes |
| **61** | [Name] | David Greenberg | 16 | Yes (conditional) |
| **62** | [Name] | [TBD] | [TBD] | [TBD] |
| **63** | [Name] | [TBD] | [TBD] | [TBD] |
| **64** | [Name] | Michael Linton | 20 | Yes |
| **65** | [Name] | [TBD] | [TBD] | [TBD] |

### 6.2 ALT Tier Upgrade (When Activated as Primary)

When ALT author is activated as primary contingency author:

- **Tier B baseline**: 18–19 points, bi-weekly check-ins, moderate autonomy, 2–3 revisions
- **Temporary upgrade to Tier A equivalent**: 
  - Weekly check-ins (vs. bi-weekly)
  - High autonomy (pre-approval NOT required)
  - Up to 3 revision rounds (vs. 2–3)
  - Mentoring mandatory (vs. optional)
  - Editorial support prioritized
  - Deadline flexibility (T+21 → T+28 possible)

**Upgrade reverts after Wave 2 publication**: ALT author returns to Tier B status for subsequent projects (unless formally promoted).

---

## 7. Recovery Protocol: Partial Completion Scenarios

### 7.1 Primary Author Delivers <50% by T+14

**Trigger**: Author provides draft addressing <50% of domain prompts or <600 words

**Actions (orchestrator decision)**:
1. Send feedback letter noting gaps (T+14)
2. Set hard deadline: Major revision due T+18 OR contingency activation
3. Assess author's responsiveness: Can they realistically complete by T+21?

**If author confirms they can recover**:
- Set focused revision scope (list 3–5 specific gaps to address)
- Offer extended revision time (T+21 → T+25, if Wave 2 publication can shift)
- No contingency activation; author stays primary

**If author indicates they cannot complete**:
- Activate ALT immediately (T+14)
- ALT takes over primary authorship
- Original author credited as contributing researcher (if sections are usable)

### 7.2 Primary Author Delivers 50–75% by T+14

**Trigger**: Draft addresses 50–75% of prompts; >600 words but <1000 words; major sections present but gaps remain

**Assessment**:
- Is the gap conceptual (missing entire topic) or editorial (shallow coverage)?
- Is the voice/approach aligned with domain prompt?
- Can a 2–3 day revision cycle close the gap?

**Outcome scenarios**:

**Scenario 1: Gaps are editorial (shallow coverage)**
- Feedback: "Expand section X and add 2 citations to section Y"
- Author revises (T+14 to T+18)
- Continue with peer review (no contingency needed)

**Scenario 2: Gaps are conceptual (missing major section)**
- Feedback: "Add entirely new section on [topic]"
- Decision: Can author realistically add 400+ words in 4 days?
  - YES → Revised deadline T+18, contingency standby
  - NO → Activate ALT, offer author "co-author" role if work is strong

**Scenario 3: Approach is misaligned with prompt**
- Example: Author focuses on policy (prompt asks for systems analysis)
- Decision: Request reframe vs. activate ALT?
  - Light reframe (fixable in 3 days) → Author continues
  - Heavy reframe (needs reconceptualization) → Activate ALT immediately

### 7.3 Authorship Preservation When Contingency Activates Late

If contingency is activated **after** primary author has delivered substantial work (T+14+):

**Option A: Co-authorship**
```yaml
author: "Martha Santos and [Primary Author Name]"
author_roles: "Santos: Lead author (sections 1–3, revision rounds); [Primary]: Contributing author (initial research, section 4)"
publication_note: "This domain was originally authored by [Primary], with substantial revision and completion by Martha Santos (ALT author) 
                   due to timeline constraints. Both authors contributed to final publication."
```

**Option B: Attribution in Supplementary Section**
```markdown
## Acknowledgments & Author Contributions

This domain was authored by Martha Santos with significant contributions to initial research and 
outline development by [Primary Author Name]. The final submission represents a collaborative effort 
to meet Wave 2 publication deadlines.
```

**When to use each**:
- **Co-authorship**: Primary author contributed >30% of final text or core research framework; both approved final version
- **Attribution**: Primary author contributed 15–30% (research, outline, initial draft); ALT author substantially rewrote for publication
- **Solo attribution (ALT only)**: Primary author contributed <15% or ALT author rewrote >80% of content; original author mentioned in notes only

---

## 8. Phase 3 Escalation: Domain Deferral

### 8.1 Conditions for Phase 3 Escalation

A domain is escalated to Phase 3 (deferred publication) if:

1. **Primary author no-shows AND ALT author declines AND all EXT candidates decline** (by T+21)
2. **Partial author delivery + contingency fails**: Author delivers <50% by T+14; ALT declines to take over; EXT candidates insufficient (by T+18)
3. **Scope mismatch discovered too late**: At T+14, feedback reveals author's work is >50% off-topic; rewrite time exceeds available hours; contingency authors unable to absorb (rare)

### 8.2 Phase 3 Documentation Requirements

Before escalating to Phase 3, orchestrator must document:

```markdown
---
Domain: 60
Title: "International Coordination in Crisis Response"
Escalation Decision Date: 2026-06-21 (T+21)
Reason for Deferral: [Select: Author No-Show, ALT/EXT Declined, Scope Reframe Required, Other]

Author Outreach Log:
- [Date]: Initial author invitation sent
- [Date]: Reminder sent (no response)
- [Date]: Escalation attempt (no callback)
- [Date]: ALT activation (declined reason: [e.g., insufficient capacity])
- [Date]: EXT-02 contacted (declined reason: [e.g., partner conflict])
- [Date]: EXT-03 contacted (declined reason: [e.g., no response])

Contingency Options Exhausted:
- ALT author: [Name] – Declined [reason]
- EXT-01 through EXT-10: [Summary of responses]
- Internal reallocation: Not feasible

Recommendation for Phase 3:
- Suggested author(s) for re-engagement: [Names from different pool or expanded EXT]
- Estimated timeline for Phase 3 Wave 2 catch-up: Q3 2026 or Q4 2026
- Priority level: High (critical domain for systems resilience framework)

---
```

### 8.3 Archive & Phase 3 Reopening

Deferred domains are archived with full communication trail:

**Archive location**: `/projects/systems-resilience/wave-2-deferred/Domain_##/`

**Contents**:
- Initial domain prompt and acceptance criteria
- Author invitation and all escalation communication
- ALT/EXT decision logs
- Feedback on partial work (if any)
- Recommendation letter for Phase 3 team

**Phase 3 reopening**:
- Project leadership reviews deferred domains in Phase 3 planning cycle (Q2 2026 or later)
- Archive materials inform author selection and timeline adjustments
- Phase 3 Wave 2 catch-up domains may have extended timelines (T+30 days instead of T+28)

---

## 9. Communication Decision Matrix

### 9.1 Who Notifies Whom

| Event | Orchestrator Notifies | Method | Timing | Template |
|-------|----------------------|--------|--------|----------|
| **Author no-show** | Author | Email + Slack | T+3 | Section 4.1 |
| **ALT activation** | ALT author | Email + phone call | T+5 | Section 4.2 |
| **ALT declines** | Orchestrator (internal note) | Project lead notification | T+9 | Internal log |
| **EXT activation** | EXT candidate/organization | Email + phone call | T+9 | Section 4.3 |
| **Domain deferred** | Project lead + original author | Email + formal memo | T+21 | Section 4.4 |
| **Publication** | All team + authors | Email announcement | T+28 | Customized |

### 9.2 Escalation Notification Rules

- **Primary author no-show**: Notify project lead at T+5 (before ALT activation)
- **ALT declines**: Notify project lead at T+9 (before EXT activation, unless EXT already contacted in parallel)
- **Domain deferred**: Notify executive sponsor + steering committee within 24 hours of T+21 decision

---

## 10. Contingency Author Compensation & Recognition

### 10.1 ALT Tier Compensation (If Activated as Primary)

- **ALT base compensation** (Tier B): [Fee/Recognition as defined in project contract]
- **Premium for primary activation**: +20–30% above ALT base (acknowledges compressed timeline + Tier A support)
- **Mentoring bonus** (if provided): +10% above activation premium
- **Early completion bonus** (if delivered by T+18): +5% above activation premium

### 10.2 EXT Tier Compensation

- **EXT standard honorarium**: [Flat fee or hourly rate, defined per project]
- **EXT expedited rate**: +25% above standard (compressed 7–10 day timeline)
- **EXT scope reduction credit**: If author negotiates <1000 word limit, honorarium adjusted proportionally
- **EXT co-author bonus**: If EXT author contributes as co-author (not solo), +15% recognition premium

### 10.3 Author Attribution & Publication Credit

All Wave 2 submissions (primary, ALT, EXT) receive:

- Full author byline in published document (name, affiliation, credentials)
- Listed in Wave 2 published credits + author index
- Social media announcement and project newsletter mention
- PDF certificate of publication (optional)
- Invitation to Wave 2 launch event (if virtual or in-person)

---

## 11. Success Metrics: Contingency Protocol Effectiveness

### 11.1 Metrics to Track

| Metric | Target | Success Threshold |
|--------|--------|------------------|
| **Activation response time** | ALT responds within 2 days of outreach | 80%+ ALT authors respond by T+7 |
| **ALT acceptance rate** | Primary contingency activated successfully | ≥75% of ALT outreach results in acceptance |
| **ALT delivery on-time** | ALT author delivers draft by T+10 (primary no-show) | ≥80% of ALT authors meet compressed deadline |
| **EXT acceptance rate** | Secondary contingency activated if ALT declines | ≥50% of EXT candidates accept (target: 1 per 3 outreach) |
| **Publication timeline preservation** | Wave 2 publishes on T+28 (or <+7 days delay) | ≥90% of domains published by T+35 |
| **Quality of contingency submissions** | ALT/EXT submissions meet acceptance rubric | ≥85% of contingency submissions achieve "Proficient" or higher |

### 11.2 Post-Wave 2 Review

After Wave 2 publication, conduct 30-minute retrospective with orchestrator team:

- How many domains required contingency activation? (Target: <2 of 6)
- What triggered no-shows? (Insufficient planning, scope confusion, competing commitments, etc.)
- Did ALT/EXT authors meet quality standards?
- What improvements to contingency process should inform Wave 3?

---

**Document Status**: Ready for deployment  
**Version Control**: Tracked in `/projects/systems-resilience/WAVE_2_CONTINGENCY_AUTHOR_SUBSTITUTION.md`  
**Last Review**: 2026-06-14  
**Next Review Date**: 2026-07-21 (post-Wave 2 publication; post-implementation retrospective)
