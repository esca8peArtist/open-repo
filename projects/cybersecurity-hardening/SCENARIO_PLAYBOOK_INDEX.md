---
title: "Phase 2 Scenario Playbook Index"
project: cybersecurity-hardening
created: 2026-05-07
status: index
phase: Phase 2
depends_on:
  - PHASE_2_SEQUENCING_STRATEGY.md
  - PHASE_2_SEQUENCING.md
cross_references:
  - immigration-surveillance-evasion-playbook.md
  - activist-organizing-playbook.md
  - financial-resistance-playbook.md
  - whistleblower-playbook.md
  - journalist-security-playbook.md
  - dv-survivor-safety-playbook.md
---

# Phase 2 Scenario Playbook Index

**Status**: All 6 playbooks complete as of May 7, 2026. Total corpus: ~50,000 words across 6 standalone documents. Each playbook is independently deployable without requiring the reader to have read any other document in the corpus.

**Deployment authorization gate**: Per PHASE_2_SEQUENCING.md Section 2, playbook distribution should not begin before the Week 7 Tier 1 data gate. The July 26, 2026 quarterly review is the natural launch moment for the first playbook (immigration) concurrent with a threat model update.

---

## Playbook Directory

| # | File | One-Line Description | Primary Audience | Tier 2 Sector | Words | Pilot Readiness |
|---|------|---------------------|-----------------|---------------|-------|-----------------|
| 1 | `immigration-surveillance-evasion-playbook.md` | Defeats ICE ELITE address scoring, Mobile Fortify biometrics, and ImmigrationOS social graph — with 12-week implementation timeline for undocumented individuals and legal aid orgs | Undocumented immigrants, immigration attorneys, legal aid organizations | Immigration legal services (Tier 1 distribution overlap) | ~7,100 | **Ready now** |
| 2 | `activist-organizing-playbook.md` | Counters Babel Street persistent OSINT, drone aerial surveillance (Skydio X10/MQ-9), Flock Safety ALPR protest tracking, Mobile Fortify at perimeters, and DHS administrative subpoenas — with role-specific guidance for 5 participant types | Protest organizers, political activists, community defense networks, legal observers | Digital rights orgs, civil liberties coalitions (Tier 2A) | ~9,500 | **Ready now** |
| 3 | `financial-resistance-playbook.md` | Addresses IRS LCA Palantir platform financial social graph mapping, DOGE/SSA cross-agency fusion, FinCEN SAR pipeline, and Monero vs. Bitcoin privacy tradespace for advocacy organizations | Advocacy organizations, mutual aid networks, individual donors under political scrutiny | Nonprofit networks, labor organizations (Tier 3) | ~6,300 | Ready after legal review |
| 4 | `whistleblower-playbook.md` | Full SecureDrop protocol + WPA coverage analysis + parallel construction defense documentation for federal employees and contractors with evidence of government illegality | Federal employees, government contractors, private sector employees with government contract evidence | Government accountability organizations, congressional offices | ~8,700 | **Ready now** |
| 5 | `journalist-security-playbook.md` | CBP border device protocol, Signal safety number verification (the non-negotiable prerequisite), PRISM/Section 702 source communication architecture, SecureDrop deployment for newsrooms, NSL metadata minimization | Investigative journalists, photojournalists, newsroom IT, press freedom organizations | Journalist organizations, press freedom groups (Tier 2D) | ~9,800 | **Ready now** |
| 6 | `dv-survivor-safety-playbook.md` | Safety-planning-first framework for intimate partner surveillance — stalkerware detection, device replacement (not hardening), location tracking audit across all vectors, account separation, evidence preservation for court | DV survivors, DV advocates, shelter staff, legal service providers, healthcare providers | DV coalitions, NNEDV Safety Net network | ~8,900 | Ready after DV advocate review |

**Total corpus**: ~50,200 words across 6 playbooks. Minimum viable distribution: any single playbook is self-contained.

---

## Deployment Sequencing

### Recommended distribution order (per PHASE_2_SEQUENCING_STRATEGY.md Section 5, Month 5–6)

**Wave 1 — July 26, 2026 (quarterly review launch)**: Distribute concurrently with threat model update (Mobile Fortify, drone surveillance, HART biometrics, post-SCOTUS DOGE/SSA update).

1. **Immigration advocacy playbook** (Playbook 1) — first because Tier 1 distribution to immigration legal aid creates the natural distribution channel. This playbook is the content that makes Phase 1 Tier 1 outreach directly actionable for the audience those organizations serve.

2. **Journalist security playbook** (Playbook 5) — second because Tier 2D journalist organization outreach provides the distribution channel and the playbook's scope (CBP border device protocol, Signal safety number verification, SecureDrop deployment) maps directly to the FPF, CPJ, and RCFP contacts in the Tier 2 contact list.

**Wave 2 — September 2026 (post-adoption-gate)**: Contingent on Tier 1 adoption gate metrics being met.

3. **Activist organizing playbook** (Playbook 2) — distribution via Tier 3 policy and labor outreach. The EFF, ACLU, and NLG contacts in the Tier 2A pipeline are natural distribution partners given the playbook's integration of documented EFF/NLG resources.

4. **Whistleblower playbook** (Playbook 4) — SecureDrop's presence at 65+ news organizations is the distribution infrastructure. FPF and SecureDrop administrators are natural distribution partners. Congressional staff contacts (per Tier 2 contact list) can facilitate distribution to federal employee-serving organizations.

**Wave 3 — Requires new outreach tracks not yet established**:

5. **Financial resistance playbook** (Playbook 3) — requires nonprofit legal counsel network outreach not currently in Tier 1–3 pipeline. Suggested contacts: Lawyers Committee for Civil Rights Under Law, Bolder Advocacy (Alliance for Justice), Center for Constitutional Rights.

6. **DV survivor playbook** (Playbook 6) — requires NNEDV Safety Net and DV coalition outreach that is a separate track from the current Tier 1–3 distribution. The National Domestic Violence Hotline and state coalition network are the distribution infrastructure. This playbook should not be distributed without a DV advocate review of the safety planning framing — specifically to confirm that the escalation risk discussion accurately reflects current best practice per NNEDV Safety Net guidance.

---

## Tier 2 Audience Mapping

| Playbook | Primary Tier 2 Audience | Tier 2 Contact Reference | Rationale |
|----------|------------------------|--------------------------|-----------|
| 1 — Immigration | Tier 1 legal aid networks (immigration legal services); also: VITA tax preparer networks (ITIN filer risk) | Tier 1 distribution pipeline (already established) | Playbook is Tier 1 content delivered to Tier 1 audiences; their clients are the end beneficiaries |
| 2 — Activist | Tier 2A: Digital rights orgs (EFF, ACLU), civil liberties coalitions | TIER_2_DISTRIBUTION_STRATEGY.md Tier 2A contacts | Activist organizing content is appropriate for digital rights organizations to distribute to their networks |
| 3 — Financial | Tier 3: Nonprofit networks, legal defense organizations, labor union financial departments | Tier 3 pipeline + new outreach to nonprofit legal counsel | Requires Tier 3 nonprofit relationships to distribute; does not fit cleanly in Tier 2 |
| 4 — Whistleblower | Tier 2A: Government accountability organizations; also: Congressional staff (Tier 2B) | TIER_2_DISTRIBUTION_STRATEGY.md Tier 2A contacts | GAP, POGO, and congressional oversight staff are natural partners; FPF provides SecureDrop infrastructure |
| 5 — Journalist | Tier 2D: Journalist organizations, press freedom groups | TIER_2_DISTRIBUTION_STRATEGY.md Tier 2D contacts | FPF, CPJ, RCFP, PEN America are direct distribution partners; newsroom IT security teams are end-users |
| 6 — DV Survivor | New track: DV coalitions, NNEDV Safety Net network, shelters | Not yet in Tier 1–3 pipeline — new outreach required | National Domestic Violence Hotline, NNEDV, state coalitions are the distribution infrastructure; requires advocate review |

---

## Tier 2 Pilot Readiness Assessment

### Ready for immediate Tier 2 pilot (can be tested with Phase 1 early adopters today)

**Playbook 5 — Journalist Security**: This is the strongest candidate for an immediate Tier 2 pilot. Reasons:
- The target audience (investigative journalists, newsroom IT, press freedom organizations) overlaps directly with Tier 2D contacts already identified in the distribution strategy
- The content (CBP border device protocol, Signal safety number verification, SecureDrop deployment) is specific enough to generate concrete feedback from practitioners
- FPF, CPJ, and RCFP all have established relationships with the corpus from prior engagement; any of them could serve as a pilot partner
- The playbook's Signal safety number verification section fills a documented gap — most "Signal is secure" guides do not address the man-in-the-middle attack vector that verification prevents, and this is a section that practitioners will test against their existing practices
- The Section 702/PRISM framing is time-sensitive (authorization expires mid-June 2026 minimum; next reauthorization debate will generate practitioner attention)

**Playbook 4 — Whistleblower**: Second-strongest pilot candidate. Reasons:
- Government Accountability Project (GAP) is cited as the primary legal resource throughout and actively represents whistleblowers in the current political environment; they are the natural pilot partner
- The SecureDrop protocol in this playbook is complementary to the journalist playbook — distributing both to the same FPF contact creates a coherent source-journalist pair
- The parallel construction risk discussion is a substantive gap in most existing whistleblower guides and is likely to generate specific feedback from practitioners (the MuckRock/Reuters DEA material is well-sourced but underutilized in the advocacy community)
- The WPA coverage/gap table is immediately useful to attorneys advising current federal employees — the probationary period gap, the intelligence community gap, and the press disclosure protection gap are all highly topical

**Playbook 2 — Activist Organizing**: Third candidate. Reasons:
- The 5-tier role-specific guidance (frontline participant / lead organizer / legal observer / communications coordinator / organizational leadership) is a structural innovation that existing protest security guides lack
- The Flock Safety ALPR documentation and the drone countermeasures section are specific, sourced, and actionable — practitioners at EFF, ACLU, and NLG can verify the claims against their own documentation
- The escalation matrix (Level 1 / Level 2 / Level 3) provides a triage tool that legal support organizations can use to advise clients at different risk levels

**Playbook 1 — Immigration**: Fourth, but should be first to distribute per sequencing rationale. The Tier 1 distribution pipeline is the vehicle; the playbook is content for Tier 1 partners' clients. It is highly actionable for the target audience with no prerequisite reading.

### Requires additional review before Tier 2 pilot

**Playbook 6 — DV Survivor Safety**: Flagged for DV advocate review before any distribution. The safety planning framework, escalation risk discussion (removing stalkerware can trigger physical violence escalation), and the specific advice on device replacement timing all require validation by practitioners with real-world DV safety planning experience. The NNEDV Safety Net project (techsafety.org) is the appropriate review partner. Distributing before this review creates risk of harm if the safety framing is miscalibrated for any specific survivor population (e.g., technology-facilitated DV by highly sophisticated abusers, or DV situations with immigration dimensions that compound the threat model).

**Playbook 3 — Financial Resistance**: Flagged for nonprofit tax counsel review before distribution. The financial and tax claims in this playbook (Schedule B confidentiality, IRS structuring law, Monero entry/exit vulnerability) are accurate at a general level but require practitioner review for application to specific organizational situations. Legal disclaimers are present throughout, but a practitioner review by a nonprofit tax attorney (e.g., from the National Council of Nonprofits or Bolder Advocacy) would strengthen distribution confidence.

---

## Internal Cross-References

The six playbooks are internally consistent and cross-reference each other where relevant:

- **Immigration playbook** references: activist playbook (Part 2 social media hygiene is relevant for immigrant organizers), device hardening guide (Part 4 GrapheneOS configuration), opsec-playbook.md
- **Activist playbook** references: immigration playbook (Part 4 device hardening is identical), opsec-playbook.md Part 1 (account separation), implementation-guide.md, PHASE_2_SEQUENCING_STRATEGY.md Sections 1.2–1.3 and 3.3
- **Financial playbook** references: palantir-threat-model.md (LCA social graph mechanism), threat-model.md, PHASE_2_SEQUENCING_STRATEGY.md Sections 1.1 and 2.4
- **Whistleblower playbook** references: implementation-guide.md (BFU/AFU), journalist security playbook (SecureDrop receiving side), PHASE_2_SEQUENCING_STRATEGY.md Sections 1.2 and 2.5
- **Journalist security playbook** references: activist playbook Part 4 (physical countermeasures), whistleblower playbook Part 3 (SecureDrop source side), encrypted-messaging-implementation-guide.md, PHASE_2_SEQUENCING_STRATEGY.md Sections 1.2–1.3 and 2.1
- **DV survivor playbook** references: device-hardening-guide.md, implementation-guide.md, PHASE_2_SEQUENCING_STRATEGY.md Section 4.1 (new audience identification)

No playbook duplicates the core technical content in opsec-playbook.md or implementation-guide.md — each cross-references those documents for foundational guidance rather than repeating it. The scenario-specific content in each playbook is additive.

---

## What Is Not Covered (Planned Phase 2 Extensions)

The following topics are identified in PHASE_2_SEQUENCING_STRATEGY.md but are not addressed in the current six playbooks and represent Phase 2 extension work:

1. **Election worker security** — PHASE_2_SEQUENCING_STRATEGY.md Section 4.1 Community 3 identifies election workers and poll watchers as a new high-priority audience following CISA's EI-ISAC shutdown. No playbook currently addresses this audience.

2. **Labor organizer specific guidance** — The activist playbook addresses protest security generally; a separate labor organizing supplement would address employer surveillance of union organizing drives (workplace monitoring software, NLRB protected activity overlaps, USDA Palantir workforce monitoring precedent).

3. **State-specific routing** — PHASE_2_SEQUENCING_STRATEGY.md Section 4.3 identifies a Texas supplement as a priority for readers without access to California's DROP platform. No state-specific supplement exists yet.

4. **Spanish translation** — The immigration playbook's Part 2 (data broker opt-outs) is the highest-ROI translation target. Not yet produced.

5. **Video primer scripts** — Short 3–5 minute video scripts for: "What is ELITE and why does my address matter?", "How to use Signal safely", "What to do if ICE approaches you". Not yet produced.

---

## Document Maintenance Schedule

All six playbooks are scheduled for quarterly review on **July 26, 2026** (aligned with the corpus quarterly review gate in PHASE_2_SEQUENCING.md). The July 26 review should specifically assess:

- Section 702/FISA authorization status (current extension expires mid-June 2026)
- DOGE/SSA access litigation status (Fourth Circuit vacated injunction April 2026; underlying merits unresolved)
- ICE Mobile Fortify accuracy update (any new court filings challenging misidentification)
- SecureDrop mobile app release status (pending security audit as of May 2026)
- GAP whistleblower program operational capacity update (DOGE-era restructuring effects)
- Monero exchange landscape (Haveno/Bisq operational status, LocalMonero-successor developments)

---

*Index created: May 7, 2026. Playbooks created: May 6, 2026. All content is current as of that date. Next scheduled review: July 26, 2026.*
