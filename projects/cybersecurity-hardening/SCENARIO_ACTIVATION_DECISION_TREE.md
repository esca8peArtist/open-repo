---
title: "Scenario Activation Decision Tree — Tier 1 Escalation Triggers"
project: cybersecurity-hardening
created: 2026-05-15
status: user-ready
phase: Phase 1 — Tier 1 Launch
source-documents:
  - SCENARIO_PLAYBOOK_INDEX.md
  - phase-2-threat-intelligence-trigger-assessment.md
  - PHASE_1_FLAGS_ASSESSMENT.md
  - PHASE_1_EXECUTION_CALENDAR.md
---

# Scenario Activation Decision Tree

**Purpose**: Decision trees for the 3 threat scenarios most likely to trigger immediate Tier 1 escalation, acceleration, or messaging adjustment during Phase 1 outreach (June 1–21, 2026). These scenarios are drawn from the 6 Phase 2 scenario playbooks, with specific focus on triggers relevant to the current Tier 1 contact cohort (Senate staff, think tanks, law school clinics, civil rights organizations).

**How to use**: These are pre-committed escalation protocols. When a trigger condition is met, activate the corresponding contact group and messaging variant. Do not improvise.

---

## Scenario 1: Palantir ELITE or ICE Enforcement Surge / Public Crisis Event

**Threat profile**: A high-profile ICE enforcement action, new ELITE-related court filing, congressional hearing, or investigative news story puts Palantir's immigration surveillance infrastructure into the national spotlight during the Phase 1 outreach window (June 1–21, 2026).

**Why this is the highest-probability Tier 1 escalation trigger**: The corpus is built around ELITE documentation. Any event that increases public attention to ELITE, Palantir, or ICE data practices creates a window where Tier 1 contacts (Senate staff, think tanks) are actively looking for primary-source documentation — which is exactly what the corpus provides.

**Examples that would trigger this scenario**:
- Major ICE enforcement action generating national news (mass arrest operation, school or church raid, etc.)
- Congressional hearing called on ICE technology or Palantir contracts
- New court filing or FOIA disclosure revealing ELITE operational parameters
- Investigative report from 404 Media, The Intercept, or major outlet on ELITE/Palantir

### Decision Tree

```
TRIGGER: Major ICE enforcement news OR congressional ELITE hearing announced
         OR new Palantir/ELITE FOIA disclosure OR investigative report published

   |
   v

IS THE EVENT DIRECTLY RELATED TO ELITE, Palantir, or commercial data broker ICE pipeline?
   |
   |-- YES --> Activate Wave A: Time-Anchored Outreach (see below)
   |
   |-- NO (general enforcement news) --> Continue standard schedule
   |    Add ONE sentence in next send referencing the news as context
   |
   |-- UNSURE --> Check: Does the event involve the specific systems in the corpus?
                 (Palantir, ELITE address scores, Venntel, Babel Street, LexisNexis DHS)
                 YES → Treat as YES branch
                 NO → Continue standard schedule
```

**Wave A: Time-Anchored Outreach**

Contacts to accelerate or re-engage immediately (within 24 hours of trigger event):

| Contact Group | Action | Messaging Variant |
|--------------|--------|------------------|
| Senate staff — all offices with active ELITE jurisdiction (Judiciary, Intel, Homeland, Wyden, Markey) | Send or re-send with time-anchored subject line | "ELITE documentation — directly relevant to [today's news event]" |
| Think tanks (Brennan Center, Georgetown CPT, EPIC) | Send or follow up with time anchor | Reference the news event as reason the primary-source documentation is newly urgent |
| Law school clinics (all active dockets) | Alert to new development | Frame: "This confirms what the threat model documents — the corpus's primary sourcing is citable in any litigation this triggers" |
| Civil rights organizations (ACLU, Lawyers' Committee) | Escalate immediately to phone if no reply yet | Frame: equity angle on enforcement concentration in majority-minority communities |

**Time-anchored subject line variants** (use within 48 hours of trigger):
- `ELITE documentation — relevant to [news event reference]`
- `Palantir corpus — primary sources for today's [hearing/report/filing]`
- `Briefing memo: FOIA-sourced ELITE documentation for oversight response`

**Do not use these subject lines after 72 hours of the trigger event** — they lose their news-hook value and read as opportunistic.

**Corpus section to highlight for this scenario**:
- Playbook 1 (Immigration surveillance evasion) — forward to Tier 1A contacts (immigration legal aid)
- Threat model Section 1 (Palantir ELITE architecture) — send to Senate staff for oversight letter use
- Part 0 (data broker opt-outs) — forward to community-based contacts for immediate client distribution

---

## Scenario 2: Section 702 FISA Reauthorization Crisis / Surveillance Law Breaking Point

**Threat profile**: The June 12, 2026 Section 702 FISA reauthorization deadline creates a specific congressional pressure event during the Phase 1 window. If reauthorization fails, is significantly amended, or generates major public controversy, Senate staff contacts become sharply more attentive to the commercial surveillance documentation in the corpus.

**Why this is a high-probability Tier 1 escalation trigger**: The corpus explicitly documents the commercial data broker pipeline that interfaces with Section 702 collection (Venntel, Babel Street data entering NSA's supply chain without a warrant). This is a gap in most public Section 702 debate that the corpus directly fills. Senate staff working the reauthorization will have a specific use for this documentation.

**June 12 is a fixed date-certain trigger within the Phase 1 window.**

**Examples that would trigger this scenario**:
- Section 702 reauthorization vote scheduled (even if eventually passes)
- Senate floor debate on Section 702 amendments
- Public controversy about Section 702 scope or commercial data interface
- Any senator's office asking for documentation on commercial surveillance pipeline

### Decision Tree

```
DATE-CERTAIN TRIGGER: June 12, 2026 (Section 702 FISA reauthorization deadline)
OPTIONAL EARLIER TRIGGER: Any Senate floor debate or committee markup before June 12

   |
   v

DAY 12 (JUNE 12): Activate Senate Escalation Protocol regardless of prior reply status

   |
   v

WHICH SENATE CONTACTS HAVE NOT REPLIED BY JUNE 12?
   |
   |-- ALL SENATE CONTACTS HAVE REPLIED → Send a brief update note only
   |   "With today's 702 deadline, wanted to flag Part 2 of the threat model as
   |    relevant to the commercial data pipeline debate — happy to discuss."
   |
   |-- SOME SENATE CONTACTS HAVE NOT REPLIED → Send time-anchored follow-up:

Subject: "FISA reauthorization today — the ELITE documentation may be relevant"

Body template (from PHASE_1_EXECUTION_CALENDAR.md Section 4, Day 12):
"One follow-up on the briefing I sent June 1st.

With the Section 702 reauthorization deadline today, I wanted to resurface the
commercial data broker pipeline documentation in the corpus — specifically how
Venntel and Babel Street data is acquired under Section 702 interfaces and sold
to ICE without a warrant requirement.

The FOIA documentation in Part 2 of the threat model is structured to be citable
in oversight letters or hearing prep.

Happy to do 20 minutes at any point this week — [Calendly link] — or send a
briefing memo if that format is more useful.

[Your name]"

   |
   v

PARALLEL ACTION: Alert Think Tank contacts (Brennan, Georgetown CPT, EPIC, Cato)
"The 702 deadline creates a natural moment for the commercial surveillance
pipeline documentation — specifically the Venntel/Babel Street interface
that bypasses the warrant requirement. The corpus is citable for any
published analysis of the commercial data broker gap in 702 oversight."
```

**Contacts to activate for Scenario 2**:

| Contact Group | Activation Condition | Message Frame |
|--------------|---------------------|--------------|
| All 8 Senate staff contacts | June 12 regardless of prior reply status | Legislative tool — citable documentation for oversight letters and hearing prep |
| Brennan Center, Georgetown CPT, EPIC | June 12 or any day 702 controversy spikes | Research gap — primary-source commercial surveillance pipeline documentation |
| Cato Institute | June 12 — bipartisan constitutional framing | Fourth Amendment, warrant requirement, commercial surveillance gap |
| ACLU | June 12 if active Section 702 litigation | Litigation-support — Section 702 commercial interface documentation |

---

## Scenario 3: ICE Mobile Fortify Incident / Biometric Field Enforcement Crisis

**Threat profile**: A high-profile incident involving ICE biometric identification in the field — a wrongful detention based on Mobile Fortify misidentification, a protest where Mobile Fortify was used against demonstrators, a court challenge to field biometric data collection without consent — creates an escalation moment specifically for immigration legal aid organizations and civil liberties contacts.

**Why this is a high-probability Tier 1 escalation trigger**: The corpus's Flag 1 (documented in PHASE_1_FLAGS_ASSESSMENT.md) is specifically about Mobile Fortify field deployment — the system that enables ICE agents to biometrically scan anyone in any public encounter without consent. This is the threat scenario most likely to generate a news event during Phase 1. Immigration legal aid organizations (the Tier 1A contacts — NILC, CLINIC, RAICES, ILRC, NLG) will have the most immediate need for this documentation.

**Note**: This scenario may also be triggered by a Cell-site simulator (Stingray) disclosure, a Clearview AI misidentification case, or any facial recognition field-use controversy. The activation logic is the same.

**Examples that would trigger this scenario**:
- Court filing or news story involving ICE Mobile Fortify field biometric collection
- Wrongful detention linked to facial recognition misidentification
- Protest or community encounter where ICE agents photographed individuals for biometric scanning
- New court challenge to warrantless biometric collection in field encounters

### Decision Tree

```
TRIGGER: News or court filing involving ICE field biometric collection
         OR Mobile Fortify misidentification incident
         OR any facial recognition enforcement controversy

   |
   v

IS THE INCIDENT DIRECTLY RELEVANT TO THE CORPUS'S FLAG 1 (MOBILE FORTIFY)?
   |
   |-- YES: ICE field biometric, no formal processing step → Full Tier 1A Activation
   |
   |-- RELATED (Clearview, Stingray, ALPR) → Partial Activation: Tier 1A + activist contacts
   |
   |-- GENERAL surveillance news → Standard schedule, add one-sentence news hook

FULL TIER 1A ACTIVATION:

   Step 1: Verify Gist biometric section is updated to address Mobile Fortify
   (Per PHASE_1_FLAGS_ASSESSMENT.md, this update should be complete before Day 1;
    if not yet done, do it NOW before sending — it takes 15 minutes)

   Step 2: Activate Tier 1A contacts immediately
   Priority order:
   1. RAICES (Texas — highest ELITE exposure zone, direct field biometric risk)
   2. NILC (national reach, litigation-ready audience)
   3. NLG Mass Defense (civil liberties response, legal observer network)
   4. CLINIC (400+ affiliated programs, rapid network distribution)
   5. ILRC (practitioner network, publications distribution)

   Step 3: Message variant for Tier 1A biometric incident activation

Subject: "Resource for clients — biometric surveillance documentation (Mobile Fortify context)"

Frame: "Given [today's news], I wanted to make sure the biometric documentation in
the corpus reached your team. The guide now includes specific context on Mobile Fortify
field deployment — the system ICE agents use to biometrically scan individuals in any
public encounter without a formal processing step. The countermeasures section documents
what remains effective.

The Part 0 data broker opt-outs are the highest-leverage action for most clients —
they do not require technical expertise and directly degrade the address confidence
scoring that determines ELITE targeting priority.

[Corpus URL]"

   Step 4: Activate Playbook 1 (Immigration Surveillance Evasion) distribution
   This playbook is specifically ready for Tier 1A distribution (per SCENARIO_PLAYBOOK_INDEX.md:
   "Ready now"). If the biometric incident accelerates demand, distribute Playbook 1
   directly to Tier 1A contacts as a follow-up resource within 48 hours.

   Step 5: Alert think tanks
   Brennan Center and Georgetown CPT: "Mobile Fortify incident creates a specific
   documentation need — the corpus's biometric section (updated to clarify field
   deployment context) may be useful for any analysis or response."
```

**Contacts to activate for Scenario 3**:

| Contact Group | Activation Priority | Playbook |
|--------------|---------------------|---------|
| RAICES (Texas) | Immediate (highest-exposure zone) | Playbook 1 + corpus biometric section |
| NILC | Immediate | Playbook 1 + corpus biometric section |
| NLG Mass Defense | Immediate | Corpus biometric section (activist-facing) |
| CLINIC | Within 24 hours | Playbook 1 for affiliate distribution |
| ILRC | Within 24 hours | Practitioner resource framing |
| Brennan Center, Georgetown CPT | Within 48 hours | Policy/research documentation |
| ACLU | Within 48 hours | Litigation support documentation |

---

## Cross-Scenario Notes

### Scenario Combination Protocol
If multiple scenarios trigger simultaneously (e.g., an ICE enforcement surge that also involves Mobile Fortify), prioritize the most specific trigger first (Scenario 3 — biometric activation) and stack the broader political outreach (Scenario 1 — enforcement surge) as a parallel track within 24 hours.

### Corpus Accuracy Gate (Must Complete Before Escalation Sends)
Before sending any escalation messaging, confirm the relevant corpus section is accurate:
- Scenario 1/2: Verify threat model DOGE litigation status is correctly framed (Flag 2 in PHASE_1_FLAGS_ASSESSMENT.md — acceptable to launch as-is, but prepare verbal update if asked)
- Scenario 3: Verify Mobile Fortify paragraph has been added to opsec-playbook.md biometric section (Flag 1 — must be resolved before any Tier 1A biometric sends)

### What These Scenarios Do NOT Cover
These trees address Tier 1 outreach acceleration. They do not cover:
- Phase 2 Scenario Playbook distribution (that is governed by PHASE_2_SEQUENCING.md)
- Tier 2 amplifier contact escalation (governed by TIER_2_DISTRIBUTION_STRATEGY.md)
- Internal security incidents affecting the corpus or the user (no playbook covers this)

---

*Created: 2026-05-15. Sources: SCENARIO_PLAYBOOK_INDEX.md, PHASE_1_FLAGS_ASSESSMENT.md, PHASE_1_EXECUTION_CALENDAR.md, phase-2-threat-intelligence-trigger-assessment.md.*
