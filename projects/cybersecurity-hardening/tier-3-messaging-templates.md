---
title: "Tier 3 Sector-Specific Messaging Templates: DV Survivors, Labor Organizers, Election Workers"
project: cybersecurity-hardening
created: 2026-05-09
status: production-ready
phase: Phase 2 — Tier 3 Distribution Planning
session: 908
version: 1.0
word_count: ~3,000
depends_on:
  - tier-3-audience-segmentation-and-contact-list.md
  - phase-2-dv-survivor-safety-playbook.md
  - phase-2-threat-briefing-labor-organizers.md
  - election-worker-opSec-supplement.md
---

# Tier 3 Sector-Specific Messaging Templates

**Purpose**: Production-ready outreach email templates for the three Tier 3 segments. Each template is calibrated to the specific threat environment, decision-maker vocabulary, and organizational culture of its target audience. Templates are designed to be sent from a named individual, not an organization — personal credibility is the primary trust signal at Tier 3.

**Usage protocol**: Personalize the bracketed fields before sending. The personalization instructions at the end of each template are mandatory — a generic send to any Tier 3 contact will not produce engagement. Read the recipient organization's most recent public communications (annual report, newsletter, website homepage) before sending.

**Sending timeline**: Templates ready for use beginning June 1, 2026 per the 16-week deployment sequence (tier-3-deployment-sequence.md).

---

## Template 1: DV Survivor Organizations (NNEDV, State Coalitions)

**Target recipients**: NNEDV Safety Net Project (SafetyNet@NNEDV.org), Executive Directors and Technology Safety Coordinators at state DV coalitions

---

```
Subject: [Safety] Digital Safety Toolkit for Advocates + Survivors — Technology Stalking
         Prevention, Legal Evidence Preservation

Dear [Name / Safety Net Team]:

I'm writing to share a practical digital safety resource that may complement the work
[Organization] is doing to help survivors navigate technology-facilitated abuse.

The problem your advocates encounter daily has gotten materially worse: AirTag-based
stalking cases increased 317% by 2024, and NNEDV's own Safety Net research documents
that approximately half of victim service providers have clients whose partners use
stalkerware. The landscape is the same — covert GPS tracking, account credential
access, family plan surveillance — but the tools are cheaper, more available, and
increasingly layered with each other. An abuser may simultaneously use an AirTag
planted in a car, stalkerware on the phone, and carrier-level location access from
a shared family plan. Advocates who can address all three layers are rare.

We've developed a set of materials that may be useful as a training resource for
your advocates and shelter staff:

**For advocate training** — A threat model covering all current surveillance layers
used in technology-facilitated DV: stalkerware (mSpy, FlexiSPY, Hoverwatch), Bluetooth
trackers (AirTag, Samsung SmartTag, Tile), account credential access, carrier family
plan surveillance, and biometric coercion. Each layer includes practical detection and
response steps designed for a 15-minute safety planning session, not a technical
deep dive. The trauma-informed sequencing (safety planning before any technology
change) is built in — the framing matches what your advocates already know.

**For legal advocates and prosecution support** — A section on digital evidence
preservation: timestamped screenshot protocols, stalkerware behavior documentation
for courts, location tracking evidence chains for protective order proceedings and
criminal prosecution. This material addresses the gap between "we know surveillance
is happening" and "we have court-admissible documentation of it."

**For survivors (with advocate introduction)** — A simplified quick-start covering
the three most protective immediate actions: detecting Bluetooth trackers using
Android Safety or Apple Tracker Detect, checking for remote account access on
devices the abuser may know about, and separating from shared carrier plans.
Designed to be walked through by an advocate in a safety planning session.

All materials are freely available and can be adapted with attribution. They're
designed to be distributed by advocates, not handed to survivors as self-help
documents — the safety planning prerequisite is explicit throughout.

I'd welcome the opportunity to discuss how these materials might fit into
[Organization]'s technology safety curriculum, or to answer any questions about
the underlying research.

Full resource: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108

[Your name]
[Contact information]
```

**Personalization instructions**:

- **NNEDV Safety Net Project**: Reference their Safety Net Tech Summit 2026 specifically. Mention that the threat model cites NNEDV Safety Net data (half of victim service providers report stalkerware). Frame as a potential addition to the Safety Net curriculum or resource library. Ask specifically about the Technology Safety Summit working groups.

- **California CPEDV**: Note the California tech sector context — stalkerware companies are often California-based, and California DELETE Act (data broker opt-out) provisions are directly relevant to some surveillance layers. Reference any recent CPEDV publications on technology abuse.

- **Texas TCFV**: Texas has high rates of technology-facilitated stalking and limited civil protection order enforcement resources. Frame the legal evidence preservation section as particularly relevant for Texas advocates working in jurisdictions with variable protective order enforcement.

- **New York NYSCADV**: Note the overlap between DV survivor technology safety and the immigrant community technology safety work, given New York's large immigrant DV-affected population. NNEDV's DV-immigrant overlap is already documented in the corpus.

- **All other state coalitions**: Review their most recent annual report or newsletter for any technology-facilitated abuse programming and reference it specifically. Generic emails will not get responses from state coalition Executive Directors.

**Critical caution**: Do not send this email to survivors directly. The Safety Net Project and state coalitions are the appropriate recipients. These organizations will mediate distribution to survivors through appropriate advocate channels.

---

## Template 2: Labor Organizing Organizations (AFL-CIO, SEIU, UFW, CWA, Teamsters)

**Target recipients**: AFL-CIO Technology Institute (Lauren McFerran, ED), National IT Directors and Organizing Department heads at SEIU, UFW, CWA, UFCW, United Steelworkers, Teamsters

---

```
Subject: [Security] Organize Safely: Union OpSec Toolkit — Penlink Geofencing,
         Babel Street Surveillance, Member Protection

Dear [Name / Organizing Team]:

I'm writing to share a security resource that addresses a surveillance threat your
members and organizers are facing right now.

In September 2025, DHS awarded a $2.9M contract to Penlink PLX — a system that
geofences specific locations and identifies every phone present during a specified
timeframe using commercial advertising SDK data. Privacy advocates have documented
ICE using this system against individuals who observed or participated in enforcement
protests. For organizing campaigns in sectors with significant concentrations of
immigrant workers — agriculture, food processing, domestic work, hotel and
hospitality — an organizer's repeated presence at union meetings and rally sites
creates a location pattern accessible to ICE without a warrant. This is not a
speculative future threat. It is operational.

Simultaneously, the UAW/CWA/AFT lawsuit filed in October 2025 documented that DHS
and State Department AI-powered social media surveillance is already chilling union
speech: more than 60% of UAW members aware of the program had changed their social
media activity. For noncitizen members, that figure exceeds 80%. The mere existence
of the surveillance produces the suppression — no enforcement action is required.

The resource I'm sharing addresses these threats directly, in terms organizers can
use and with training structured for the union context:

**For organizers and organizing committees** — Operational security for an organizing
campaign: Signal for all pre-petition communications, need-to-know information
architecture before petition filing (what each role needs to know, and nothing more),
Penlink geofencing countermeasures (dedicated organizing devices not linked to normal
location history), and Babel Street social media exposure reduction for member
accounts most visible in organizing activity.

**For members in sectors with immigration enforcement exposure** — Three immediate
protective actions: data broker opt-outs that directly reduce Palantir ELITE address
confidence scores (2–4 hours, no technical expertise), location services discipline
on personal devices, and understanding which apps in the Penlink commercial SDK
network are most likely to be selling location data. This content can be delivered
by shop stewards in a 20-minute member meeting.

**For shop stewards** — A member coaching module for technology security conversations:
how to explain the surveillance threat without creating panic, how to walk members
through the three most protective immediate actions, and how to escalate to the
union's legal team when a member faces immigration enforcement.

**For IT and legal** — Infrastructure-level hardening for union communications
systems, Signal network architecture for organizing committees, whistleblower
documentation protocols, and attorney-client privilege protection for electronic
communications.

All materials are freely available and can be adapted for your union's style. The
research is FOIA-sourced — government contracts and court filings, not speculation.

I'd welcome the opportunity to discuss how this might fit into [Union]'s existing
security or member education programming.

Full resource: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108

[Your name]
[Contact information]
```

**Personalization instructions**:

- **AFL-CIO Technology Institute (Lauren McFerran)**: This is the priority contact. Reference the Workers First AI Summit (March 2026) and the AFL-CIO's AI Principles for Workers — the surveillance threat is a natural extension of AI workplace monitoring concerns. Frame as a potential addition to the Technology Institute's existing curriculum. Ask specifically about the format that works best for affiliated union training programs (in-person, webinar, self-paced module). McFerran comes from the NLRB — frame the NLRA protection angle (employer surveillance during organizing is an unfair labor practice) as directly relevant to her prior work.

- **SEIU National**: SEIU's healthcare membership is particularly relevant — healthcare workers face HIPAA-adjacent concerns about employer monitoring. The property services and security officer divisions have high concentrations of immigrant workers. Frame the Penlink threat in terms of property services and building services workers who are most exposed.

- **UFW**: Most direct member exposure to ELITE and Penlink. Frame around the agricultural worker community specifically. Note that corpus Part 0 (data broker opt-outs) is immediately actionable for UFW members and can be delivered at union halls. Mention Spanish translation is in development. UFW members face the highest convergence of immigration enforcement exposure and labor organizing activity.

- **CWA / CODE-CWA**: Two distinct frames. For CWA broadly: telecommunications worker context — CWA members work for the carriers that enable some of the surveillance infrastructure; there's both a worker protection and a worker accountability dimension. For CODE-CWA specifically: tech worker organizers in the sector building AI surveillance tools — the whistleblower angle and the employer surveillance angle are both relevant. Reference the NLRB's weakened electronic monitoring guidance.

- **Teamsters**: Logistics worker context — GPS tracking of union vehicles, monitoring of driver communications through company systems. The employer surveillance layer (non-government) is as relevant as the government layer for Teamsters members.

- **United Steelworkers**: Industrial sector context. USW has a strong existing IT security posture; frame as a complement to existing security programs, not a replacement. Focus on the organizing security and immigrant member protection angles.

**Union democracy framing note**: All labor outreach must use union democratic language — "member participation," "transparency about threats," "member-controlled security practices." Do not frame security as a management imposition. The organizing context means that any security measure perceived as top-down will face legitimate union democracy objections. Frame every recommendation as something the member can choose and control.

---

## Template 3: Election Worker Organizations (EAC, NASED, NASS, State Election Directors)

**Target recipients**: EAC (eac.gov contact), NASED (Mark Goins, 2026 President), NASS (mbenson@nass.org), state election directors via NASED membership directory

---

```
Subject: [Security] Election Infrastructure Protection: 2026 Insider Threat
         Prevention and Infrastructure Hardening Toolkit

Dear [Name]:

I'm writing to share a security resource that may be useful for [Organization/State]'s
election security preparation ahead of the 2026 midterms — particularly given the
changed federal support landscape.

The current environment is documented: since February 2026, CISA has cut more than
a third of its workforce and halted most programs working on elections, including
incident response units and regional election security advisors. The FY2027 budget
proposes eliminating the election security program and EI-ISAC entirely. 75% of
local election officials report insufficient replacement resources. Senator Warner's
letter to DHS in May 2026 highlights exactly the gap this creates heading into
November. Arizona's decision not to report the Iranian-linked intrusion attempt to
CISA — citing trust concerns — illustrates the breakdown in federal-state
coordination.

The resource I'm sharing is designed to address this gap at the jurisdictional level,
without depending on federal coordination:

**Hardware security for election management systems** — Practical guidance on USB
policy enforcement (disabling autorun, device inventory, chain-of-custody logging),
BIOS/UEFI password protection and secure boot configuration, physical tamper-evident
sealing of ports on election equipment, and firmware integrity verification. These
are the vectors that red teams have consistently found exploitable in election
infrastructure — and they are addressable without specialized tools or significant
budget.

**Credential compartmentalization and access control** — Separate administrative
accounts for election management system access (no shared credentials), MFA on
all EMS access using hardware tokens or TOTP authenticators (not SMS, which is
vulnerable to SS7 intercept), and credential rotation protocols tied to staff
transitions. These measures directly address the phishing and credential theft
vectors documented in CISA advisories.

**Insider threat detection and prevention** — A practical framework for the poll
worker context: physical access logs for election management areas, the two-person
integrity rule for sensitive procedures, USB device inventory at shift changes,
and an anomaly reporting protocol that allows poll workers to flag concerns without
creating hostile working environments. The CISA/EAC joint insider threat guidance
is the foundation; this extends it with operationally specific procedures.

**Incident response that doesn't depend on CISA** — Direct FBI field office liaison
contacts, state CISO escalation paths, and incident documentation protocols designed
to preserve chain of evidence for both law enforcement and post-election audit purposes.
Given the trust breakdown with CISA, having alternative federal coordination pathways
documented in advance is operationally important.

All materials meet or exceed the post-2020 CISA election security baseline and are
fully compatible with existing EAC cybersecurity guidance. They can be proposed as
a supplementary resource in the EAC's security resource library, and are designed
to be adapted for state-specific training programs.

I'd welcome the opportunity to discuss how these materials might be integrated into
[Organization]'s pre-election training program for [State]'s election officials
and poll workers.

Full resource: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108

[Your name]
[Contact information]
```

**Personalization instructions**:

- **EAC (Election Assistance Commission)**: Frame as a resource library submission request. The EAC publishes a cybersecurity resource library; ask specifically about the submission process for supplementary security resources. Reference the EAC's existing cybersecurity guidance page and position the toolkit as complementary to, not competitive with, EAC materials. Note the CISA coordination gap as context for why supplementary materials from non-CISA sources are now more valuable.

- **NASED (Mark Goins, Tennessee)**: Mark Goins comes from Tennessee elections administration. Frame the toolkit in terms of state election director peer needs — jurisdictions without dedicated IT staff are the most exposed. Reference that the materials are designed to be adapted for varying state contexts. Ask whether the NASED annual conference agenda includes cybersecurity programming where this could be presented.

- **NASS (Maria Benson)**: NASS's #TrustedInfo2026 initiative is an active outreach vehicle — frame the toolkit as supporting election official security so officials can speak with authority from a position of operational safety. Note that the physical security and personal information compartmentalization sections address the documented harassment and doxing threat (38% of officials report threats).

- **California Secretary of State**: California's scale (largest election administration in the country) means county-level variance is enormous. Frame around tools that can cascade from state to county without requiring uniform county IT capacity. Reference California's relatively strong data privacy framework (CPRA) as a context where the data security recommendations are legally grounded.

- **Texas Secretary of State**: Texas has a large number of county election offices with limited IT resources. Frame around the hardware security and USB/bootloader sections as the highest-leverage measures for under-resourced jurisdictions. Texas's refusal of federal Hava funds in some cycles means state-funded security resources are the only channel.

- **Florida Department of State**: Florida made significant post-2020 election security investments. Frame as building on that investment — position the toolkit as a next-layer supplement to their existing program. Reference the insider threat section specifically given Florida's poll worker recruitment challenges.

- **Defending Digital Democracy (D3P)**: D3P runs election security tabletop exercises independently of federal government. Frame as curriculum input for their training program. This is a peer-organization relationship, not a top-down submission. Reference their existing tabletop format and ask how the toolkit could be integrated into scenario planning.

**Regulatory compliance framing note**: Election officials are accustomed to compliance language. Frame every recommendation in terms of established standards where possible: NIST SP 800-53, NIST SP 800-171, CISA's Cybersecurity Toolkit for Elections, and the EAC's cybersecurity guidance. The toolkit should be positioned as meeting standards, not creating new ones. This framing reduces the "extra burden" objection that will otherwise slow adoption.

---

## General Messaging Principles Across All Three Templates

### Lead with the specific threat, not general security

DV coalitions get general security solicitations constantly. What makes this different is the specific threat model: stalkerware on Android, AirTag geofencing, biometric coercion. Lead with the specific, recent, documented threat. The same principle applies to labor (Penlink September 2025 contract) and election workers (CISA defunding timeline, NASED trust breakdown with federal agencies).

### Use the recipient's language and frameworks

- DV coalitions: "safety planning," "technology safety," "survivor-centered," "trauma-informed," "advocate-mediated"
- Labor organizations: "member protection," "union democracy," "organizing security," "worker-controlled," "steward-delivered"
- Election workers: "election integrity," "chain of custody," "regulatory compliance," "incident response," "federal coordination"

Generic security language signals that the sender doesn't understand the audience. The framing must be specific to each sector's professional vocabulary.

### Match the trust-mediation model to the audience

- DV: Materials distributed by advocates to survivors. No cold distribution to survivors.
- Labor: Materials adopted by union training programs and delivered by stewards to members. Not distributed to members directly without union channel endorsement.
- Election workers: Materials submitted to EAC resource library or presented through NASED/NASS channels. State directors cascade to county officials, not direct outreach to 3,000+ county offices.

### Offer a specific ask, not a general invitation

Each template includes a specific next step: a discussion of curriculum integration, a resource library submission, or a conversation about training format. Generic "let me know if you're interested" closings do not generate responses from Executive Directors with full inboxes.

### Timing

- Send DV coalition emails on Tuesdays or Wednesdays, morning (9–11am recipient local time). Avoid Mondays (staff catch-up) and Fridays (pre-weekend).
- Send labor organization emails when not during major contract negotiations or strike actions — check current news for the union before sending.
- Send election worker emails June–July 2026. Avoid August–November (active election cycle administration).

---

## Sources

- [NNEDV Safety Net Tech Summit 2026](https://nnedv.org/content/safety-nets-tech-summit-2026/)
- [Safety Net Project — Survivor resources](https://www.techsafety.org/resources-survivors)
- [AirTag stalking statistics — Cybernews](https://cybernews.com/editorial/apple-airtag-domestic-violence/)
- [Prism Reports — DHS Penlink PLX contract, April 2026](https://prismreports.org/2026/04/29/dhs-surveillance-location-data-penlink-plx/)
- [EFF — UAW/CWA/AFT lawsuit against ideological surveillance](https://www.eff.org/press/releases/labor-unions-eff-sue-trump-administration-stop-surveillance-free-speech-online)
- [Nextgov/FCW — CISA election security pullback, May 2026](https://www.nextgov.com/cybersecurity/2026/05/senator-warns-cisa-election-security-pullback-could-leave-midterms-vulnerable/413378/)
- [AFL-CIO Technology Institute](https://aflciotechinstitute.org/)
- [NASS #TrustedInfo2026](https://www.nass.org/node/2685)
- [EAC Election Security Preparedness](https://www.eac.gov/election-officials/election-security-preparedness)
- [Brennan Center — Federal government undermining election security](https://www.brennancenter.org/our-work/research-reports/how-federal-government-undermining-election-security)
- [Votebeat — CISA trust broken, January 2026](https://www.votebeat.org/2026/01/15/cisa-election-security-trust-broken-trump-chris-krebs-denise-merrill/)
