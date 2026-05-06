---
title: "Tier 2 Threat Briefings Integration Guide"
project: cybersecurity-hardening
created: 2026-05-06
status: operational
purpose: >
  Definitive reference for how to attach, reference, and time-coordinate the
  five sector-specific threat briefings across the Tier 2 outreach campaign.
  Covers which briefing goes with which messaging template, exact timing windows,
  subject-line variants, and how to reference the briefing in the outreach body.
depends-on:
  - TIER2_MESSAGING_TEMPLATES.md
  - TIER2_DISTRIBUTION_PREP.md
  - tier2-journalists-threat-briefing.md
  - tier-2-threat-briefing-digital-rights.md
  - tier-2-threat-briefing-academic.md
  - tier-2-threat-briefing-researcher-community.md
  - tier2-technical-advocates-threat-briefing.md
---

# Tier 2 Threat Briefings: Integration Guide

## Purpose of This Document

This guide is the operational reference for attaching threat briefings to Tier 2 outreach. It answers three questions for each sector:

1. Which briefing file goes with which email template?
2. When do you send the briefing — same message as the intro email, or a follow-up?
3. How do you reference the briefing in the outreach message itself?

This guide does not reproduce the briefings or the outreach templates. Cross-references to those files are provided throughout.

---

## Master Mapping: Template to Briefing

| Sector | Template | Briefing File | Send Timing |
|--------|----------|--------------|-------------|
| Digital rights organizations | Template 2A-v2 | `tier-2-threat-briefing-digital-rights.md` | Attach in the initial outreach email |
| Academic cybersecurity programs | Template 2B-v2 | `tier-2-threat-briefing-academic.md` | Attach in the initial outreach email |
| Security researcher communities | Template 2C-v2 | `tier-2-threat-briefing-researcher-community.md` | Send as follow-up only if initial outreach gets acknowledgment |
| Journalist organizations | Template 2D-v2 | `tier2-journalists-threat-briefing.md` | Attach in the initial outreach email |
| Technical advocates | Template 2E-v1 | `tier2-technical-advocates-threat-briefing.md` | Attach in the initial outreach email |

**General principle**: Sector briefings go in the initial email for audience types who explicitly evaluate credibility before acting (digital rights, journalists, academics, technical advocates). For researcher communities specifically, the brief is higher signal if held back until after the initial email lands — researchers are skeptical of cold contacts who load them with attachments; the peer-to-peer framing of Template 2C-v2 works better alone first.

**The visual deck** (`tier2-threat-briefing-slides.md`) is an optional third attachment for any sector. Offer it explicitly only when the recipient is likely to use slides for internal presentations — academic programs and press freedom organizations (who train their members) are the primary cases.

---

## Sector-by-Sector Integration Details

### Sector 2A: Digital Rights Organizations

**Outreach template**: Template 2A-v2 (TIER2_MESSAGING_TEMPLATES.md)
**Briefing file**: `tier-2-threat-briefing-digital-rights.md`
**Send with**: Initial email — attach as PDF or paste link to rendered version
**Briefing focus**: Marginalized community threat matrix; FISA 702 policy advocacy window; election infrastructure defense gap; ProKYC-specific vulnerabilities for undocumented, refugee, and trans individuals

**How to reference the briefing in the email body**:

After the opening paragraph of Template 2A-v2, insert one of these linking sentences depending on attachment method:

- If attaching the file directly: `I've attached a sector-specific threat briefing on the May 2026 landscape that may be useful for your policy teams — it documents the specific threat vectors affecting the communities you serve, with countermeasures and policy advocacy windows.`
- If linking to a hosted version: `The May 2026 threat briefing for digital rights organizations [link] documents the specific threat vectors affecting undocumented, refugee, and trans communities, alongside the June 12 FISA advocacy window.`
- If the contact is EFF or EPIC (FOIA-fluent organizations): `The attached briefing draws on FOIA-obtained procurement documents for the specific capability claims — the same documentation type your teams use. The data broker section covers the ELITE data supply chain in citable detail.`

**Subject line variants** (choose one based on the organization's primary campaign focus):

- Data broker / surveillance focus: `May 2026 threat briefing: data broker loophole — June 12 deadline`
- Marginalized community / undocumented focus: `May 2026: ProKYC identity attacks on immigrant and refugee communities — sourced briefing`
- Election focus: `May 2026: election infrastructure defense gap — community impact brief`

**Audience-specific briefing callouts** (reference the specific section most relevant to the contact):

| Organization | Section to Highlight in Email |
|-------------|-------------------------------|
| EFF / EPIC | Part III (FISA 702) + closing policy advocacy windows |
| Access Now | Part I (marginalized community threats) + Immediate Actions for populations served |
| Privacy International | Part I (international data broker dimension) + threat-impact matrix |
| STOP (Albert Fox Cahn) | Part IV (election infrastructure + ICE polling place) |
| CDT | Part III (FISA 702 data broker loophole provision specifically) |
| Tor Project | Part II (supply chain; Tor installation path guidance in countermeasures) |

---

### Sector 2B: Academic Cybersecurity Programs

**Outreach template**: Template 2B-v2 (TIER2_MESSAGING_TEMPLATES.md)
**Briefing file**: `tier-2-threat-briefing-academic.md`
**Send with**: Initial email — attach or link
**Briefing focus**: Research opportunities; curriculum integration; supply chain sophistication curve; election infrastructure threat modeling research agenda; Palantir academic freedom implications

**How to reference the briefing in the email body**:

Template 2B-v2 already establishes methodological credibility as its core pitch. The briefing reinforces this by providing primary-source citation material. Reference it as follows in the closing of the template:

- Standard: `I've attached a research-oriented briefing on the May 2026 threat landscape that documents specific modeling opportunities and dataset pointers for each threat area — including NSF/DARPA funding angles for the supply chain and synthetic identity research domains.`
- For programs with active policy research: `The briefing includes the six open research questions the Q2 2026 data raises, alongside funding pathway mapping for SaTC, DARPA AIE, and NSF Law and Science programs.`
- If the program has published on election security: `The election infrastructure section quantifies the federal investment drawdown (2018–2027) and frames the academic external vantage point opportunity created by CISA's withdrawal.`

**Subject line variants**:

- Research focus: `May 2026 threat briefing: ProKYC + supply chain + CISA gap — research agenda`
- Curriculum focus: `May 2026 threat landscape: primary-source case studies for curriculum integration`
- Policy research focus: `May 2026: FISA 702, Palantir, and the NSF funding landscape — research briefing`

**Audience-specific briefing callouts**:

| Program | Section to Highlight |
|---------|---------------------|
| CMU CyLab (Lorrie Faith Cranor) | Part I (ProKYC procedural countermeasure efficacy research) |
| UC Berkeley CLTC | Part III (election infrastructure investment drawdown chart) + closing funding section |
| MIT CSAIL/IPRI | Part IV (Palantir academic freedom implications + law-tech intersection) |
| Stanford Cyber Policy Center | Part III (election infrastructure + deepfake political ad research gap) |
| Harvard Berkman Cyberlaw Clinic | Part IV (IRS-ICE data sharing litigation + FISA circuit court research opportunity) |
| Georgia Tech IISP | Part II (supply chain sophistication curve + SBOM/OIDC architecture) |

**Special note for academic outreach**: The briefing's Figure 2 (Supply Chain Attack Sophistication Curve, 2021–2026) and Figure 3 (Election Infrastructure Budget Impact) are designed to be assignable visualizations in lecture slides. Mention availability of these figures explicitly if the contact is a course instructor.

---

### Sector 2C: Security Researcher Communities

**Outreach template**: Template 2C-v2 (TIER2_MESSAGING_TEMPLATES.md)
**Briefing file**: `tier-2-threat-briefing-researcher-community.md`
**Send with**: Follow-up only — do not attach in the initial cold outreach
**Briefing focus**: Dataset pointers; malware signature analysis playbooks; conference CFP angles; open research questions with dataset access paths

**Rationale for delayed send**: Template 2C-v2 is framed as a peer-to-peer technical critique request. Opening with a document attachment signals an advocacy ask rather than a peer exchange. Let the initial exchange establish mutual technical credibility; send the briefing when the researcher asks for more detail or when the conversation reaches the natural "here's what I'm working with" stage.

**How to reference the briefing in the follow-up**:

- First follow-up: `Here's the more detailed technical briefing — the dataset pointers section covers FaceForensics++, DFDC, ASVspoof, and WildDeepfake with specific gaps for the ProKYC attack chain. The analysis playbooks for Shai-Hulud forensics may be directly usable.`
- If the researcher has expressed conference submission interest: `The briefing has IEEE S&P, USENIX, and ACM CCS CFP angles mapped to each research question — may be useful for framing.`

**Subject line variants** (for follow-up email):

- Datasets focus: `Follow-up: dataset pointers + forensic playbooks for the questions you raised`
- Conference focus: `Follow-up: CFP angles for the IEEE S&P and USENIX threads`
- Research question focus: `Follow-up: TD-VIM gap in ASVspoof baselines — the specific research contribution I had in mind`

**Channel-specific integration**:

| Channel | Integration Approach |
|---------|---------------------|
| DEF CON community forum | Post the briefing's dataset and analysis playbook sections as a research thread; invite critique |
| CCC (39C3 submission) | Use the election infrastructure and supply chain sections as abstract material |
| Black Hat CFP | Lead with the supply chain and ProKYC technical depth; briefing serves as extended abstract |
| Individual researcher cold contact | Reference their specific prior published work; send briefing only after initial exchange |

---

### Sector 2D: Journalist Organizations

**Outreach template**: Template 2D-v2 (TIER2_MESSAGING_TEMPLATES.md)
**Briefing file**: `tier2-journalists-threat-briefing.md`
**Send with**: Initial email — attach or link
**Briefing focus**: Source protection gap (pre-contact commercial data); voice cloning and deepfakes for journalists specifically; interview security protocols for 2026; tool security updates; election infrastructure as a reporting beat

**How to reference the briefing in the email body**:

Template 2D-v2 opens with the source protection gap and commercial surveillance layer. After establishing that angle, reference the briefing:

- Standard: `The attached May 2026 briefing goes deeper on two specific changes for journalists: the voice cloning threshold that has been crossed (inbound impersonation of sources and colleagues, outbound fabricated content) and the updated interview security protocol that accounts for commercial location data captured before contact.`
- For training program contacts: `The briefing's tool update table and interview security protocol section are directly integrable into newsroom security training curricula — formatted for practitioner use, not technical audiences.`
- For investigative reporting contacts (IRE, NICAR): `The election infrastructure section documents the CISA drawdown and the alternative support infrastructure for election offices — the Defending Digital Democracy, CDT, state-level programs angle — as a reporting beat, with primary source citations.`

**Subject line variants**:

- Source protection: `May 2026 source protection: voice cloning threshold crossed + election infrastructure gap`
- Tool security: `May 2026: Bitwarden CLI compromise + updated source protection protocol`
- Election reporting: `May 2026: election infrastructure reporting beat — CISA gap documentation`
- Training focus: `May 2026 threat briefing: newsroom training update — voice cloning and interview protocol`

**Audience-specific briefing callouts**:

| Organization | Section to Highlight |
|-------------|---------------------|
| Freedom of the Press Foundation | Part I (voice/deepfake countermeasures) + Part III (tool security; YubiKey upgrade) |
| IRE | Part IV (election infrastructure as reporting beat; primary source citations) + Part II (interview security protocol) |
| CPJ | Part II (international dimension of commercial data; coordination pressure on journalists) |
| RCFP | Part II (IRS relationship mapping; legal risk for journalists with connections to monitored organizations) |
| SPJ | Part III (Bitwarden tool update; YubiKey upgrade) |
| NAHJ / AAJA | Part I (community-specific source protection; commercial data pre-contact exposure) + Part II (interview protocol) |

---

### Sector 2E: Technical Advocates

**Outreach template**: Template 2E-v1 (TIER2_MESSAGING_TEMPLATES.md)
**Briefing file**: `tier2-technical-advocates-threat-briefing.md`
**Send with**: Initial email — attach
**Briefing focus**: Peer-level technical depth; SBOM tooling; OIDC migration; firmware patch management; documentation language for updating security guides; ten specific countermeasure changes for May 2026

**How to reference the briefing in the email body**:

Template 2E-v1 is already a peer-level technical communication. Reference the briefing as companion documentation:

- Standard: `The attached briefing is the peer-level deep dive — SBOM tooling references, OIDC migration specifics, firmware patch management procedures, and the ten specific changes needed in April-era guidance. It's formatted for practitioner review, not advocacy circulation.`
- If the contact works in guide or documentation maintenance: `The ten specific countermeasure changes section (changes 1–10, with priority designations) is intended as a direct input to any guide that was last updated before May 2026.`

---

## Timing and Sequencing

### Pre-Outreach Checklist

Before sending any Tier 2 outreach with an attached briefing:

- [ ] Convert the briefing `.md` to PDF using Pandoc or similar — attach PDF, not the raw Markdown file
- [ ] Verify the companion corpus gist link is still live: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108
- [ ] Confirm the FISA 702 advocacy window: if the send date is after June 12, update the policy advocacy section language in the briefing before attaching (the June 12 deadline reference will be stale)
- [ ] Update the Bitwarden CLI window reference: the "April 21–May 31 2026" compromise window language should be updated to "April 22, 2026 specific incident, now patched" if sending after June 2026

### Send Sequencing Within a Campaign

**Week 1**: Journalist organizations and digital rights organizations — these sectors have the highest time sensitivity (June 12 policy window, election security beat)
**Week 2**: Academic programs — less time-sensitive; allow journalist responses to accumulate as social proof
**Week 3**: Security researcher communities — slowest-moving audience; researcher review is a slow process; earlier send gives more runway
**Week 4**: Technical advocates — these are often internal technical staff at organizations already reached in earlier waves; let institutional engagement happen first

**Tier 2 total timeline**: 4 weeks from Tier 1 completion to last Tier 2 send. This matches the campaign calendar in `tier-2-distribution-calendar.md`.

### Follow-Up Timing

| Sector | Initial Send | Follow-Up Window | Follow-Up Trigger |
|--------|-------------|-----------------|-------------------|
| Digital rights | Week 1 | 10–14 days after initial | No reply, or acknowledgment without action |
| Academic | Week 2 | 14–21 days after initial | No reply (one follow-up only) |
| Researchers | Week 3 | 7–10 days after initial | Always send briefing as follow-up after initial exchange |
| Journalists | Week 1 | 7–10 days after initial | No reply |
| Technical advocates | Week 4 | 10 days after initial | No reply |

---

## Using Briefings in Outreach Beyond Email

### For Presentations

The visual deck (`tier2-threat-briefing-slides.md`) is Marp-compatible and provides a 5-slide sector-neutral master with 5 sector-specific appendix slides. If a Tier 2 contact requests a presentation or a webinar:

1. Use slides 1–5 (master deck) as the base
2. Add the sector-appropriate appendix (slides 6–10 by sector, as labeled in the deck file)
3. Reference the relevant sector briefing as supplementary material for download

### For Training Integration

For journalist organizations (FPF, IRE) and academic programs integrating materials into training curricula:

- The journalist briefing's Part II (interview security protocol) and Part III (tool update table) are designed as standalone handouts — they can be extracted and reformatted without the full briefing context
- The academic briefing's research questions and curriculum integration section is designed as a course syllabus addendum

### For Policy Advocacy Contexts

For digital rights organizations using the briefing in policy advocacy (Senate staff meetings, regulatory comment letters):

- The FISA 702 section (Part III of the digital rights briefing) is formatted for policy-audience consumption
- The sources section at the end of every briefing uses URL citation format that is appropriate for legislative reference
- All capability claims are sourced to FOIA documents, government contracts, or peer-reviewed security research — the sourcing quality matches what congressional staff require

---

## Briefing File Reference Summary

| Sector | File | Word Count (approx.) | Audience Level |
|--------|------|---------------------|----------------|
| Digital rights | `tier-2-threat-briefing-digital-rights.md` | ~2,200 | Policy-technical hybrid |
| Academic | `tier-2-threat-briefing-academic.md` | ~2,800 | Research/curriculum |
| Researchers | `tier-2-threat-briefing-researcher-community.md` | ~2,600 | Technical peer |
| Journalists | `tier2-journalists-threat-briefing.md` | ~2,400 | Practitioner |
| Technical advocates | `tier2-technical-advocates-threat-briefing.md` | ~2,000 | Technical practitioner |
| Visual deck | `tier2-threat-briefing-slides.md` | N/A (slides) | All sectors |
| Synthesis (all sectors) | `may-2026-tier2-threat-briefing.md` | ~1,500 | General |

**For contacts who ask for "the short version"**: Send `may-2026-tier2-threat-briefing.md` — it is the sector-neutral 1,500-word synthesis designed for recipients who want a fast-read entry point before going deeper.
