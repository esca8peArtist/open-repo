---
title: "Tier 3 Audience Expansion Roadmap: From 33 Organizations to 600+"
project: cybersecurity-hardening
created: 2026-05-07
status: planning
phase: Phase 3 Pre-Launch
session: 896
version: 1.0
depends_on:
  - TIER2_DISTRIBUTION_PREP.md
  - TIER3_DISTRIBUTION_PREP.md
  - phase-2-immigration-surveillance-evasion-playbook.md
  - phase-2-activist-organizing-security-playbook.md
  - phase-2-dv-survivor-safety-playbook.md
  - phase-2-journalist-security-playbook.md
  - phase-2-whistleblowing-playbook.md
  - phase-2-financial-resistance-playbook.md
word_count: ~2,050
---

# Tier 3 Audience Expansion Roadmap

**Context**: Phase 2 produced six sector-specific playbooks (immigration, activist organizing, DV survivor safety, journalist security, whistleblowing, financial resistance) and a distribution infrastructure reaching approximately 33 Tier 1 organizations. Tier 2 extends that to amplifier networks (digital rights orgs, academic cybersecurity, security researchers, journalist organizations). This roadmap defines the path to Tier 3: direct-audience materials for non-expert populations at scale, targeting 600+ distribution touchpoints by end of Phase 3.

**The core Tier 3 shift**: Tiers 1 and 2 reached organizations that already understand surveillance risk and have technical or advocacy capacity. Tier 3 reaches individuals with no prior security background, whose primary interaction with these materials may be a printable one-page guide passed at a community meeting, a Reddit thread, or a bilingual clinic session. The content must be simpler. The distribution must be more decentralized. The success metrics must reflect adoption in places without institutional gatekeepers.

---

## Section 1: Tier 3 Audience Segments

### 1.1 Immigrant Communities — 10M+ via NNEDV and Coalition Infrastructure

**Population**: Undocumented immigrants, DACA recipients, visa holders under enforcement risk, and their family and community networks. Estimated population of undocumented immigrants in the U.S.: 11 million (Pew Research, 2023); DACA-eligible individuals with prior approval: approximately 580,000.

**Why they need a different material format**: The Phase 2 immigration playbook (3,200 words, 8 sections) is designed for immigration attorneys and legal aid workshop facilitators — people who can adapt it for their clients. Tier 3 requires materials the community member can use directly. Literacy levels vary. English proficiency varies widely (Spanish is the primary non-English language in the undocumented community; indigenous Mayan languages are increasingly relevant in specific regions). Immigration enforcement creates fear-based barriers to technology adoption — recommendations must be implementable without creating new exposure vectors.

**Primary channel**: NNEDV (National Network to End Domestic Violence) has documented reach into immigrant communities through DV advocacy overlap. The AFL-CIO and UFW have direct membership channels into agricultural and service-sector immigrant workers. Catholic Charities, Lutheran Immigration and Refugee Service, and local mutual aid networks are secondary channels.

**Adoption definition**: A community member completes data broker opt-outs (Part 0 of `implementation-guide.md`), removes precise location from social media, and turns off location sharing on their primary phone. These three actions meaningfully reduce their ELITE address confidence score.

### 1.2 Domestic Violence Survivors — 10M+ Annual DV Contact Points via NNEDV

**Population**: Approximately 1 in 4 women and 1 in 9 men experience severe intimate partner violence. NNEDV's Safety Net Project reports approximately half of victim service providers have clients whose partners use stalkerware. NNEDV's member organizations serve over 1.6 million survivors annually through its hotline, shelters, and legal advocacy network.

**Why they need a different material format**: The DV survivor safety playbook leads with a critical safety warning that is structurally correct but operationally complex — it requires a survivor to already be in contact with an advocate before reading the guide. Tier 3 materials must be designed for the moment before that contact: the person who has not yet called the hotline, who is reading a printout in a bathroom, who needs one immediate action (not eight sections).

**Primary channel**: NNEDV Safety Net Project, National DV Hotline (1-800-799-7233), state DV coalitions, and shelter staff. These organizations are already trained to do technology safety planning — the Tier 3 quick-start guide for DV survivors is a tool to hand to a client who needs to take the first step before a full safety planning session.

**Adoption definition**: A survivor contacts the National DV Hotline or a local shelter technology safety advocate, and begins the process of account separation — changing passwords on a device the abuser does not have access to.

### 1.3 Election Workers — 8,000+ Jurisdictions via Election Assistance Commission (EAC)

**Population**: Approximately 775,000 election workers across all U.S. jurisdictions, including 8,000+ county and municipal election offices. Poll workers (roughly 600,000 temporary staff per major election cycle) are the most decentralized audience; election administrators (full-time staff at county and state election offices) are more accessible.

**Why they need a different material format**: Election infrastructure cybersecurity has been a documented gap since the 2024 CISA workforce reduction (1,000+ positions eliminated, EI-ISAC defunded). Election administrators face specific threats: phishing targeting election management systems, credential theft, ransomware, and disinformation campaigns targeting their offices. However, election workers are not a surveillance-risk population in the same sense as immigrants or DV survivors. Their primary need is device security and credential protection — a different threat model than the other Tier 3 segments. The EAC's existing training infrastructure (over 8,000 registered users on EAVS) is a distribution channel that already reaches this population.

**Primary channel**: EAC (Election Assistance Commission) — the federal agency with direct relationships to every election jurisdiction in the country. Secondary channels: National Association of Secretaries of State (NASS), National Association of State Election Directors (NASED), and state election director offices.

**Adoption definition**: An election office implements MFA on all election management system access, and a poll worker understands not to connect personal devices to election networks.

### 1.4 Labor Organizers — 12M Union Members via AFL-CIO

**Population**: AFL-CIO represents 57 affiliated unions with approximately 12.5 million members. The most surveillance-exposed labor organizers are in sectors where organizing campaigns attract employer counter-surveillance (warehouse, logistics, tech, healthcare) and sectors where members overlap with immigration enforcement targets (agriculture, construction, meatpacking, hospitality).

**Why they need a different material format**: The Phase 2 activist organizing playbook addresses protest security and government surveillance of organizers. Labor organizers face additional threats not fully covered: employer surveillance tools (GPS tracking of union vehicles, monitoring of company email and Slack for organizing activity, use of union-avoidance consultants who use OSINT against organizers), and NLRB case exposure if organizing communications are disclosed before a petition is filed. The Tier 3 quick-start for labor organizers focuses on communications security during an organizing campaign — a more specific and actionable frame than "protest security."

**Primary channel**: AFL-CIO Technology Institute (new Executive Director Lauren McFerran, since February 2026). Secondary: CWA CODE-CWA for tech sector, NDWA for domestic worker campaigns, UFW for agricultural workers.

**Adoption definition**: An organizing committee uses Signal for all organizing communications and establishes a "need to know" information sharing protocol before filing a union petition.

### 1.5 General Public — Open Access via Reddit and Medium

**Population**: The general public with diffuse privacy concerns, no immediate enforcement exposure, but awareness of surveillance risks from news coverage of ELITE, Palantir contracts, and protest biometric scanning. This segment is the largest by volume (potentially millions of readers) but the lowest urgency and lowest conversion rate.

**Why they need a different material format**: The general public does not have a specific threat they are defending against — they have generalized concern. The Tier 3 general public quick-start should therefore be organized around the three highest-impact, lowest-effort actions: data broker opt-outs, Signal adoption, and disappearing messages. It should not attempt to be comprehensive.

**Primary channel**: Reddit communities (r/privacy, r/opsec, r/piracy, r/legal), Medium publication, and any journalist who covers the corpus as a story. These channels are inherently viral and self-distributing if the content is clear and useful.

**Adoption definition**: A reader completes OptOutPrescreen.com, one data broker opt-out (Spokeo or Whitepages), and installs Signal.

---

## Section 2: Expansion Strategy by Audience

### 2.1 Immigrant Communities — Coalition-Mediated Distribution

**Strategy**: Do not attempt direct-to-individual distribution for this population. The fear of surveillance means that unsolicited digital outreach from unknown sources will not be trusted. Trust is mediated through known organizations — immigration attorneys, legal aid staff, parish clergy, mutual aid coordinators.

**What adoption looks like**: A legal aid clinic prints the Spanish-language version of the quick-start guide and walks through it with a client during an appointment. A faith community's migrant support ministry has copies at the welcome table. A mutual aid network includes the checklist in its orientation materials for new members.

**Channel priority**: NNEDV Safety Net Project (already has DV-immigrant overlap infrastructure), CLINIC (Catholic Legal Immigration Network), ILRC (Immigrant Legal Resource Center), and UFW for agricultural worker channels. These organizations already have trust infrastructure — the corpus is a tool for staff, not a replacement for the relationship.

**Key requirement**: Spanish translation of the immigration quick-start guide is mandatory before this channel can function. The full immigration playbook should translate second.

### 2.2 DV Survivors — Hotline and Shelter Integration

**Strategy**: Partner with NNEDV Safety Net Project to integrate the DV quick-start guide into existing technology safety curriculum. The guide should be designed to be distributed by an advocate, not handed out cold. The hotline integration (texting the quick-start URL to callers who ask about technology safety) is the highest-reach channel.

**What adoption looks like**: A DV advocate uses the quick-start guide as a conversation starter in a safety planning session. A shelter puts the guide in its orientation folder. The National DV Hotline staff have the guide as a reference.

**Channel priority**: NNEDV Safety Net Project is the single highest-value contact for this segment — it reaches all 1,600+ member organizations simultaneously.

### 2.3 Election Workers — EAC Training Integration

**Strategy**: Submit the election worker quick-start guide to the EAC's existing training program as a supplementary resource. The EAC publishes a cybersecurity guide library; the quick-start can be proposed as an addition to that library without a formal organizational partnership.

**What adoption looks like**: An election administrator downloads the quick-start guide from the EAC resource library and distributes it at a pre-election training session for poll workers.

**Channel priority**: EAC first (direct relationship with all jurisdictions), then state election director offices for state-level amplification.

### 2.4 Labor Organizers — Union Hall Distribution

**Strategy**: The AFL-CIO Technology Institute is the gateway. A training module built around the labor organizer quick-start guide can be submitted to the AFL-CIO's technology curriculum. Individual union hall distribution (physical printing) is a secondary channel for non-digitally-connected workforces.

**What adoption looks like**: An AFL-CIO staff trainer uses the quick-start guide in a communications security workshop for organizing committee members. The guide appears in the AFL-CIO digital toolbox alongside other organizing resources.

**Channel priority**: AFL-CIO Technology Institute for national reach; CWA CODE-CWA for tech sector; UFW for agricultural workers (requires Spanish translation).

### 2.5 General Public — Open Publication

**Strategy**: Publish the general public quick-start guide as an open-access document (GitHub, a public-facing website, and a PDF link). Seed it in relevant Reddit communities with a clear post explaining what it is and why. Write a Medium post targeting the guide at readers who followed news coverage of ELITE or Palantir.

**What adoption looks like**: A Reddit post in r/privacy linking to the guide gets upvoted and discussed. The Medium post gets 1,000+ reads. Someone shares the PDF in a group chat.

**Channel priority**: Reddit seeding first (organic amplification if the content is clear); Medium second (longer form audience); journalist coverage third (the guide itself can be offered as a resource in any media interview about the corpus).

---

## Section 3: Spanish Translation Priority Assessment

### 3.1 Priority Order

Spanish translation should proceed in the following order, based on direct-to-individual utility (the materials an individual can use without an intermediary are highest priority):

1. **Quick-start guides** (6 documents, estimated 250 words each) — translate first, before any playbook. These are the primary Tier 3 distribution materials and are short enough that one translator can complete all six in under two weeks.

2. **Immigration quick-start guide** (already in priority 1 above) — specifically, this must be the first document translated, as it is required for the immigrant community distribution channel to function.

3. **Phase 2 DV Survivor Safety Playbook** — the second highest priority for Spanish translation, given the overlap between immigrant and DV populations. NNEDV's member organizations serve significant Spanish-speaking populations.

4. **Phase 2 Immigration Surveillance Evasion Playbook** — for workshop facilitator use in Spanish-speaking communities. At approximately 3,200 words, this is a full translation project (estimated 20–25 hours with a qualified translator).

5. **Data broker opt-out section of implementation-guide.md (Part 0)** — the single most actionable section for Tier 3 audiences. A standalone Spanish-language version of Part 0 is more useful than translating the entire guide.

6. **Phase 2 Activist Organizing Security Playbook** — for labor organizers and activist groups in Spanish-speaking communities. Estimated 3,400 words (20–25 hours).

7. **Core opsec-playbook.md and implementation-guide.md** — lower priority; these documents are used primarily by organizations that have English-capable staff, not by individuals directly.

### 3.2 Bilingual Distribution Strategy

**Separate Spanish versions preferred over bilingual documents.** The primary distribution channel for Spanish materials is print (community clinics, shelter orientation folders, union halls). A bilingual document that alternates Spanish and English paragraphs is harder to read in both languages and harder to print as a single-language resource for a single-language audience. Produce standalone Spanish-language PDFs for each priority document.

**Naming convention**: `[filename]-es.md` for source files; `[filename]-es.pdf` for distribution versions.

**Quality standard**: Translation should be done by a qualified human translator with familiarity with immigration and technology vocabulary. Machine translation (DeepL or similar) may be used for a first draft, but must be reviewed by a human with community familiarity before distribution. Terms like "stalkerware," "data broker opt-out," and "end-to-end encryption" require translator judgment about which Spanish term (or which phonetic/descriptive rendering) will be understood by the target community.

**Gist/public distribution**: Spanish-language versions should be published to the same GitHub Gist as the English originals, with a README that lists available languages and links to each version.

---

## Section 4: Decision Tree Framework

### 4.1 Branching Logic Overview

The decision tree is a non-expert entry point into the corpus. Rather than presenting six playbooks and asking a reader to identify which applies, the decision tree asks one question at a time and routes the reader to the most relevant quick-start guide or playbook section.

**Design principles**:
- Maximum three branch levels per path (question 1 > question 2 > recommendation)
- Every end state is a specific, actionable resource (a playbook section or a quick-start guide)
- Language is plain: no acronyms, no technical jargon on entry questions
- The tree must work when printed in black-and-white (no color-dependent logic)

### 4.2 Five Entry Points

Each entry point corresponds to a primary concern a reader might present:

1. **"I'm worried about ICE or immigration enforcement"** → routes to immigration quick-start guide, then Phase 2 immigration playbook for those who want more depth

2. **"My organizing group or workplace might be under surveillance"** → routes to either labor organizer quick-start guide (if organizing context) or activist quick-start guide (if protest/political context)

3. **"I'm a journalist or I work with sensitive sources"** → routes to journalist quick-start guide, then Phase 2 journalist security playbook

4. **"I'm a domestic violence survivor or I think my partner is tracking me"** → routes to DV survivor quick-start guide, with an immediate safety warning and hotline number before any other content

5. **"I work in election administration or I'm a poll worker"** → routes to election worker quick-start guide

6. **"None of these but I want to improve my privacy"** → routes to general public quick-start guide, with emphasis on data broker opt-outs and Signal

The full decision tree with branching logic is documented in `decision-tree-prototype.md`.

### 4.3 Implementation Formats

The decision tree should exist in three formats:

1. **Printed flowchart** (PDF, 8.5x11, black-and-white printable) — for distribution at community events, clinics, union halls
2. **Interactive web version** (simple HTML/JavaScript, hosted on GitHub Pages or a static site) — for digital distribution, embeddable on organizational websites
3. **Linear text version** (Markdown) — for accessibility, screen reader compatibility, and situations where a flowchart cannot be rendered

---

## Section 5: Phase 3 Readiness Gates

These conditions must be met before Tier 3 audience distribution begins. Failure to meet any gate creates a risk of distributing materials to audiences who cannot use them (because translation is incomplete) or who are not expecting them (because organizational relationships have not been established).

### Gate 1: Spanish Translation Baseline (Hard Requirement)

All six quick-start guides must be translated into Spanish before Tier 3 launch. Without Spanish quick-starts, the immigrant community and agricultural labor channels cannot function. The immigration and DV survivor quick-starts are the minimum viable set; all six should be complete before general launch.

**Verification**: Six Spanish-language quick-start guide PDFs exist, have been reviewed by a qualified translator, and are published to the distribution Gist.

### Gate 2: Organizational Relationships Established (Two Minimum)

At least two Tier 3 gateway organizations must have confirmed receipt of and interest in the materials before mass distribution. The two highest-priority candidates are NNEDV Safety Net Project (for DV survivor and immigrant community channels) and AFL-CIO Technology Institute (for labor organizer channel). A confirmed relationship means a named staff contact who has reviewed the quick-start guide and agreed to use or share it.

**Verification**: Email confirmation from a named contact at NNEDV or AFL-CIO (or equivalent organization) that they have reviewed the quick-start guide(s) and will use them.

### Gate 3: Decision Tree Published and Tested (Soft Requirement)

The decision tree must be published in printable PDF format and tested with at least one non-technical reader (someone outside the project) before general distribution. The test is simple: can they navigate from entry question to a useful resource without confusion?

**Verification**: One non-technical reader completes the decision tree and arrives at the correct quick-start guide for their simulated scenario without requiring explanation.

### Gate 4: Tier 2 Engagement Underway (Sequencing Requirement)

Tier 3 should not begin before Tier 2 outreach has been underway for at least six weeks. Tier 2 organizations (digital rights orgs, academic programs, journalist organizations) will amplify the corpus to audiences that include Tier 3 readers. Starting Tier 3 before Tier 2 has any traction means the corpus arrives in Tier 3 channels without the credibility signals that Tier 2 endorsements provide.

**Verification**: At least one Tier 2 organization has published a reference to the corpus (a newsletter mention, a tweet, a blog post, a curriculum citation, or a direct recommendation to their audience).

---

## Section 6: Timeline and Milestones

### Phase 3 Launch Timeline

The timeline is organized around the readiness gates defined in Section 5. All dates are relative to the Tier 2 launch date, which is the trigger event for the Phase 3 clock.

**Week 0**: Tier 2 outreach launches (EFF, CDT, academic programs, journalist organizations). Phase 3 preparation begins in parallel.

**Weeks 1–2**: Spanish translation sprint — all six quick-start guides translated and reviewed. Immigration quick-start guide should be complete by end of Week 1.

**Weeks 2–4**: Decision tree design and publication — printable PDF version first, then web version.

**Weeks 3–6**: Organizational relationship outreach — contact NNEDV Safety Net Project, AFL-CIO Technology Institute, EAC, and at least two additional Tier 3 gateway organizations. Goal: confirmed interest from two organizations by Week 6.

**Week 6**: Phase 3 readiness assessment — verify all four gates. If Gates 1 and 2 are met, proceed to launch. If Gate 2 is not met, delay by two weeks and re-evaluate.

**Week 7 or later**: Tier 3 launch — immigrant community and DV survivor channels first (highest urgency), then labor organizer and election worker channels, then general public open publication.

**Weeks 8–12**: General public open publication — Reddit seeding, Medium publication, journalist outreach with quick-start guides as media resources.

**Week 12**: First Tier 3 metrics check — review adoption signals (downloads, organizational uptake, community feedback) and determine whether any quick-start guides need revision.

### Success Metrics

**6-week milestone**: Spanish translations complete; two organizational relationships confirmed; decision tree published.

**12-week milestone**: At least 500 downloads of Spanish-language quick-start guides; at least three organizational partners have distributed materials to their networks; at least one general-public post (Reddit or Medium) has exceeded 1,000 views.

**6-month milestone**: Quick-start guides are referenced in at least two organizational training curricula; at least one Tier 3 organization has provided feedback that led to a revision; 600+ total distribution touchpoints achieved.
