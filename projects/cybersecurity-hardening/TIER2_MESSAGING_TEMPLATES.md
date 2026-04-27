---
title: "Tier 2 Messaging Templates: Sector-Customized Email Variants"
project: cybersecurity-hardening
created: 2026-04-27
status: ready-for-use
gist-url: "https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108"
---

# Tier 2 Messaging Templates: Sector-Customized Email Variants

## Messaging Strategy

The templates in TIER2_DISTRIBUTION_PREP.md do the job of describing the corpus accurately. What they don't do is lead with why the corpus is specifically a problem for each sector's own work. This document provides tighter, more persuasive variants for each of the four Tier 2 sectors.

**The core principle**: Tier 2 audiences are not the direct threat population. They need to understand why this matters to their institutional mission before they will act. Generic descriptions of the corpus produce polite acknowledgment. Mission-first framing produces referrals, curriculum integration, and publication.

**What "mission-first" means for each sector**:

- **Digital rights organizations** spend their credibility selectively — they need to know this threat model is sourced well enough to cite, and that the data broker angle connects to their existing policy campaigns.
- **Academic programs** will only assign or cite material that is methodologically defensible. They need to understand what primary sources underpin the claims, and that the corpus is designed to survive peer scrutiny.
- **Security researcher communities** are skeptical of advocacy-adjacent work. They need a peer-to-peer framing that invites critique, not endorsement. Their CTA is technical review, not distribution.
- **Journalist organizations** have one primary concern: will this hold up when a source is at risk? They need to understand that the countermeasures are documented against a specific known system, not generic advice, and that the threat model section gives them reportable primary-source material.

Each template below is 150–250 words. Use the original templates in TIER2_DISTRIBUTION_PREP.md for complete context on contact details, personalization notes, and follow-up strategy. These variants replace the body copy; the pre-send checklist and outreach execution plan in TIER2_DISTRIBUTION_PREP.md still apply.

---

## Template 2A-v2: Digital Rights Organizations

**Target organizations**: EFF, CDT, Access Now, Privacy International, Tor Project, Mozilla Foundation, STOP, EPIC, Fight for the Future, Demand Progress, CDD, Restore the Fourth

**Recommended subject line**: `Data broker purchases driving deportation targeting — sourced threat model + countermeasures`

```
To whom it may concern at [Organization]:

Your organization tracks the ecosystem of commercial data brokers selling
location data to government agencies without warrants. I want to share a
corpus that documents a specific active instance of that pipeline: ICE's
Palantir ELITE system, which converts commercial data broker purchases —
app-derived GPS data, Medicaid records, DMV data — into ranked deportation
target lists through "address confidence scores."

This is not speculation. The threat model is built from FOIA disclosures,
published government contracts, and federal court filings, structured so
that each claim is individually citable. The data broker section documents
the specific vendors and purchase mechanisms in ELITE's data supply chain
— directly relevant to policy and litigation work in this space.

The countermeasures playbook includes a Part 0 opt-out section that
covers the California DELETE Act's DROP platform, which provides a
documented pathway for residents without government-issued ID — a gap
that existing opt-out guides do not address.

If this is relevant to ongoing policy work or litigation at [Organization],
I'd welcome a conversation. If it belongs with a specific team (privacy
policy, surveillance, legal), any routing you can provide is appreciated.

Full corpus: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108
```

**What this does differently from the base template**: Leads with the policy and litigation angle rather than the human interest angle. Makes explicit that the sourcing is designed to survive citation scrutiny. Includes the DROP platform gap specifically because data broker policy orgs care about opt-out mechanism coverage. Closes with a routing request rather than a generic "happy to discuss" — more respectful of these orgs' triage process.

**Organization-specific adjustments**:
- **EFF / EPIC**: Mention that the contracts section draws on FOIA-obtained procurement documents; these orgs file FOIA themselves and will recognize the sourcing quality.
- **STOP (Albert Fox Cahn)**: Reference the NY-specific ICE surveillance context; Cahn has published on ICE surveillance in New York directly.
- **Privacy International**: Note that the data broker supply chain documentation covers international vendor relationships, not just US-domiciled brokers.
- **Tor Project**: Mention specifically that Tor is recommended in the countermeasures playbook for the at-risk population, and that informing them of the documented use case for Tor may be useful to their own advocacy.
- **Access Now**: Lead with the Digital Security Helpline angle — the corpus is designed to be usable by the Helpline's target population. Contact security@accessnow.org rather than press.

---

## Template 2B-v2: Academic Cybersecurity Programs

**Target organizations**: CMU CyLab, UC Berkeley CLTC, MIT CSAIL/IPRI, UW Allen School Security Lab, Stanford Cyber Policy Center, RPI, Harvard Berkman Cyberlaw Clinic, Georgia Tech IISP, Northeastern CPI

**Recommended subject line**: `Primary-source threat model for commercial surveillance in enforcement — potential curriculum or research resource`

```
Dear [Program/Center] team,

I'm sharing a documented threat model for a specific active system that
may have value for your research program or course curriculum: ICE's
Palantir ELITE platform, which aggregates commercial data broker location
data, Medicaid records, and DMV records into deportation target scoring.

The methodological basis: every claim in the threat model is sourced to
FOIA-obtained government documents, published procurement contracts, or
federal court filings. The model documents not just what ELITE does, but
where each data category originates — the commercial data broker supply
chain, the data integration architecture, and the confidence-scoring
mechanism. It is structured to be usable as a primary-source reference in
research on commercial surveillance, data broker ecosystems, and the
intersection of algorithmic decision-making with enforcement.

The countermeasures playbook covers tiered technical responses to this
specific threat model: data minimization, device hardening, and
communications security calibrated to the documented attack surface, not
generic best-practice advice.

I'm actively seeking technical review from people with security expertise.
If the countermeasures contain errors or gaps visible to your researchers,
that feedback would directly improve a corpus designed to reach a
population under active threat.

Full corpus: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108
```

**What this does differently from the base template**: Leads with methodological defensibility rather than the humanitarian angle, because academics need to know they can assign or cite this without exposing themselves to methodological critique. Frames the countermeasures as calibrated to a documented attack surface, not generic — this matters for security courses. The peer review ask is positioned as a genuine research contribution opportunity, not just flattery.

**Organization-specific adjustments**:
- **CMU CyLab / Lorrie Faith Cranor**: CyLab's usable privacy focus makes Part 0 (the accessible opt-out section, no technical expertise required) particularly relevant — the countermeasures are designed for usability first.
- **UC Berkeley CLTC**: CLTC funds applied research with policy implications; frame the ELITE threat model as a case study in the policy consequences of commercial data broker deregulation.
- **MIT CSAIL/IPRI**: IPRI sits at the law-technology intersection; note that the corpus is designed for cross-disciplinary use (legal citations alongside technical documentation).
- **Stanford Cyber Policy Center**: Following the Stanford Internet Observatory closure, Cyber Policy Center has room to engage with surveillance documentation work; don't reference SIO.
- **Harvard Berkman Cyberlaw Clinic**: Christopher Bavitz's clinic works on surveillance law; the FOIA-sourced contract documentation is directly relevant to their legal clinic case development.
- **Georgia Tech IISP / Northeastern CPI**: These programs have strong applied crypto and privacy-preserving systems research lineages — emphasize the data minimization architecture section.

---

## Template 2C-v2: Security Researcher Communities

**Target venues**: DEF CON, CCC, Black Hat, ShmooCon, independent researchers

**Recommended subject line**: `ICE/Palantir ELITE threat model — looking for technical critique before wider distribution`

```
Hi,

I'm distributing a threat model and countermeasures corpus on ICE's
Palantir ELITE system to security researchers before pushing it harder
to mainstream channels, specifically because I want technical eyes on it
first.

What ELITE does, per FOIA and court filings: aggregates commercial data
broker location data (purchased from app SDK networks, no warrant),
Medicaid enrollment records, DMV data, and other commercial sources into
address confidence scores used to rank deportation targets. The threat
model documents the data flows and source categories with citations —
this is not advocacy conjecture, it's documented procurement architecture.

The countermeasures playbook is where I'd most want review. It covers:
data broker opt-outs (Part 0, accessible to non-technical users),
GrapheneOS migration, Signal/Tor/VeraCrypt deployment, and network
hardening (DNS, VPN, router configuration). I've verified the tooling
recommendations against the documented attack surface, but I'm not
infallible about what I've missed.

If you find technical errors, gaps in the countermeasures, or places
where the threat model overstates or understates the documented
capability — I'd genuinely like to know. The corpus is published openly
and I'm treating critique as a contribution.

Full corpus: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108
```

**What this does differently from the base template**: Positions this as researcher-first distribution, making the recipient feel like a valued early reviewer rather than a later-stage audience. The technical vulnerability admission ("I'm not infallible about what I've missed") reads as credible to security researchers who are trained to distrust overconfident claims. Frames critique as contribution, not feedback — researchers respond to that framing.

**Channel-specific adjustments**:
- **DEF CON community forum (forum.defcon.org)**: Post as a research thread, not a promotional post. Frame it as sharing work in progress and inviting critique. DEF CON 34 CFP will open late 2025; if planning a talk proposal, the above text becomes an abstract — add: "I'm considering proposing this as a briefing for 34. Has anyone built on similar surveillance architecture documentation for a talk?"
- **CCC (info@ccc.de / 39C3 submission)**: CCC's civil liberties tradition makes this an excellent fit. Lead with the warrantless commercial data purchase angle — CCC cares about the legality and architectural features of state surveillance, not just the tools. Submission portal: events.ccc.de.
- **Black Hat (cfp@blackhat.com)**: Black Hat's audience skews corporate and government-adjacent. Lead with the CISO-relevant angle: commercial data broker purchases are a supply chain risk that shows up in adversaries' intelligence collection, not just government enforcement. The ELITE data supply chain is a model for how attackers aggregate commercial data at scale.
- **ShmooCon**: Small venue, DC-based, source protection / opsec tradition. The journalist + undocumented source communication security angle fits ShmooCon's community. Use the personal email approach, not a formal CFP.
- **Individual researchers (via Twitter/Mastodon, security.txt)**: Find 3–5 researchers who have published on surveillance tech, data broker ecosystems, or immigration enforcement technology. Reference their specific published work in the outreach. Do not blast generically.

---

## Template 2D-v2: Journalist Organizations

**Target organizations**: Freedom of the Press Foundation (FPF), IRE, CPJ, RCFP, SPJ, NAHJ, AAJA

**Recommended subject line**: `Source protection gap — undocumented sources and the commercial surveillance layer`

```
Dear [Organization] team,

Journalists protecting undocumented sources face a surveillance layer that
most source protection training doesn't cover: the commercial data broker
ecosystem that ICE queries without warrants to generate deportation
targeting scores.

ICE's Palantir ELITE system pulls location data purchased from smartphone
app SDK networks, Medicaid records, and DMV databases to build "address
confidence scores" on deportation targets. An undocumented source who
follows standard journalist-recommended opsec — Signal, encrypted devices,
safe meeting locations — may still be exposed through commercial data their
apps have already sold to brokers that ELITE queries. This gap is
documented in the threat model with FOIA-obtained contracts and court
filings.

The corpus I'm sharing covers both the threat and the countermeasures:

- **For training programs**: The countermeasures playbook's Part 0
  (data broker opt-outs, no technical expertise required) and the
  communication security section are directly integrable into source
  protection training curricula. They are calibrated to this specific
  threat, not generic digital hygiene.

- **For investigative coverage**: The threat model section documents
  the ELITE data supply chain from primary sources — government contracts,
  FOIA disclosures, court filings — and may serve as background or
  sourcing for coverage of the system itself.

Full corpus: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108

Happy to discuss training integration or answer questions about sourcing.
```

**What this does differently from the base template**: Opens with the source protection gap — the specific scenario where standard journalist-recommended opsec fails because it doesn't account for pre-existing commercial data exposure. This is a genuine problem that journalist trainers will recognize immediately, not a hypothetical. Clearly separates the training-use CTA from the reporting-use CTA so each recipient can route appropriately. Avoids implying a specific endorsement before the organization has reviewed the corpus.

**Organization-specific adjustments**:
- **Freedom of the Press Foundation (press@freedom.press)**: Lead with the SecureDrop overlap. The corpus recommends SecureDrop for journalist-source communication. FPF builds SecureDrop and has a direct mission stake in this. Also note: FPF's digital security team (security@freedom.press) is the more targeted contact than press.
- **IRE (info@ire.org)**: IRE's strength is training journalists on investigation tools; frame the threat model section as NICAR-ready material on the commercial surveillance data pipeline. NICAR 2026 training session potential.
- **CPJ (info@cpj.org)**: CPJ's focus is international; note that the data broker architecture documented in ELITE is a model being exported internationally. The countermeasures apply wherever app-derived location data is commercially available — which is most countries.
- **RCFP (hotline@rcfp.org)**: RCFP's Legal Hotline addresses journalist legal risk; frame this specifically as a legal-risk disclosure document. An undocumented source whose data was in the commercial pipeline before the journalist-source relationship began raises legal exposure questions (shield law scope). Their hotline attorneys should know this threat model exists.
- **SPJ (spj@spj.org)**: SPJ Journalists Toolbox integration. Keep the email short and point directly to the toolbox team. Offer to supply a brief summary formatted for toolbox integration.
- **NAHJ / AAJA**: These community-specific journalist associations have members who cover communities directly affected by ELITE targeting, and may themselves have sources from those communities. The personal connection to the threat model is more direct here than at any other journalist organization. Lead with the community journalism angle, not the abstract "source protection" framing.

---

## Organization-to-Template Mapping

Use this table to select the right template variant for each Tier 2 organization.

### 2A. Digital Rights Organizations — Template 2A-v2

| Organization | Contact | Priority Note |
|-------------|---------|---------------|
| EFF | press@eff.org | Mention FOIA-sourced procurement documents in personalization |
| CDT | press@cdt.org | Emphasize policy/surveillance team routing |
| Access Now | security@accessnow.org | Use Helpline contact, not press; focus on at-risk population |
| Privacy International | contact@privacyinternational.org | Mention international vendor documentation |
| Tor Project | press@torproject.org | Lead with Tor recommendation in countermeasures playbook |
| Mozilla Foundation | advocacy@mozillafoundation.org | Mozilla has published surveillance analyses — reference theirs |
| STOP | info@stopspying.org | Reference Albert Fox Cahn's NYC/ICE surveillance work directly |
| EPIC | epic@epic.org | Highlight FOIA-sourced contracts; EPIC files FOIA themselves |
| Fight for the Future | team@fightforthefuture.org | Action-oriented; mention amplification potential |
| Demand Progress | info@demandprogress.org | Coalition angle: labor + immigration advocacy overlap |
| CDD | jchester@democraticmedia.org | Jeff Chester tracks data broker misuse; direct relevance |
| Restore the Fourth | info@restorethe4th.com | Fourth Amendment / warrantless purchase angle |

### 2B. Academic Programs — Template 2B-v2

| Institution | Contact | Priority Note |
|------------|---------|---------------|
| CMU CyLab | cylab@cmu.edu | Lead with usable privacy angle; Part 0 accessibility |
| UC Berkeley CLTC | cltc@berkeley.edu | Frame as policy-consequence case study |
| MIT CSAIL/IPRI | ipri-contact@mit.edu | Cross-disciplinary legal + technical framing |
| UW Allen School | seclab@cs.washington.edu | Human-centered security research alignment |
| Stanford Cyber Policy Center | cyber@stanford.edu | Do not reference SIO; focus on surveillance documentation |
| RPI | compsci@rpi.edu | Student group RPISEC; community outreach angle |
| Harvard Berkman | cyber@law.harvard.edu | Bavitz/Cyberlaw Clinic; surveillance law and FOIA context |
| Georgia Tech IISP | iisp@gatech.edu | Applied security; data minimization architecture |
| Northeastern CPI | cpi@northeastern.edu | Applied crypto; privacy-preserving systems |

### 2C. Security Researcher Communities — Template 2C-v2

| Channel | Contact | Priority Note |
|---------|---------|---------------|
| DEF CON forum | forum.defcon.org | Post as research thread, not promotional |
| CCC | info@ccc.de / events.ccc.de | Civil liberties + warrantless purchase angle |
| Black Hat | cfp@blackhat.com | CISO / supply chain risk framing |
| ShmooCon | info@shmoocon.org | Source protection / DC community angle |
| Individual researchers | Via published contact | Reference their specific published work |

### 2D. Journalist Organizations — Template 2D-v2

| Organization | Contact | Priority Note |
|-------------|---------|---------------|
| FPF | security@freedom.press | Lead with SecureDrop overlap; use security team, not press |
| IRE | info@ire.org | NICAR training session framing |
| CPJ | info@cpj.org | International export of architecture; global applicability |
| RCFP | hotline@rcfp.org | Legal-risk framing for hotline attorneys |
| SPJ | spj@spj.org | Journalists Toolbox integration; short pitch |
| NAHJ | nahj@nahj.org | Community journalism angle; personal connection to threat |
| AAJA | national@aaja.org | Same as NAHJ; communities disproportionately surveilled |

---

## Using These Templates Alongside TIER2_DISTRIBUTION_PREP.md

These templates replace the body copy of the four templates in TIER2_DISTRIBUTION_PREP.md. Everything else in that document — pre-send checklist, outreach execution plan, sequencing strategy, tracking template, FAQ — applies unchanged.

**One adjustment to the sequencing guidance**: When leading with Template 2A-v2, the policy and litigation framing makes EFF and EPIC the highest-priority first contacts within the digital rights sector (both have litigation infrastructure and FOIA expertise that directly uses well-sourced threat model material). STOP (Albert Fox Cahn) is the fastest-moving target and may respond quickly given his direct ICE/NYC surveillance focus.

For journalist organizations, send to FPF and IRE in the same week, before CPJ, RCFP, and SPJ. FPF and IRE have training infrastructure they can immediately act on; the others are more likely to cite or reference than to integrate directly.

---

Last updated: 2026-04-27
