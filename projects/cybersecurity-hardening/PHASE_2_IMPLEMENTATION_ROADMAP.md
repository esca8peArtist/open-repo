---
title: "Phase 2 Implementation Roadmap — Decision Document for May 25-27 Review"
project: cybersecurity-hardening
created: 2026-05-19
status: ready-for-user-review
target-review-date: 2026-05-25
author: research-agent
depends-on:
  - PHASE_2_SEQUENCING_STRATEGY.md
  - PHASE_2_DETAILED_IMPLEMENTATION_ROADMAP.md
  - SCENARIO_PLAYBOOK_INDEX.md
  - PHASE_2_DEPLOYMENT_READINESS.md
---

# Phase 2 Implementation Roadmap

**Bottom line for review session**: Phase 2 content production is complete. All six scenario playbooks (~50,000 words) are written and production-ready. The outstanding Phase 2 work is entirely sequencing, distribution, and maintenance — not content creation. This document translates the full execution detail in `PHASE_2_DETAILED_IMPLEMENTATION_ROADMAP.md` into a decision-ready format: what to greenlight, in what order, with what criteria, and where the binding constraints are.

**What this document is**: A decision document for the May 25–27 review window. It identifies the choices the user must make to advance Phase 2, surfaces the three scenarios that require external validation before deployment, and maps the full 12-month execution arc against concrete quarterly gates.

**What this document is not**: Another execution spec. The detailed module-by-module breakdown, effort estimates, and sentinel monitoring procedures are in `PHASE_2_DETAILED_IMPLEMENTATION_ROADMAP.md`. Read that document for operational depth on any section below.

---

## Section 1: Current State — What Phase 2 Has Already Built

### Content Production: Complete

| Playbook | File | Status | Word Count | Pilot-Ready |
|----------|------|--------|------------|-------------|
| 1. Immigration Surveillance Evasion | `phase-2-immigration-surveillance-evasion-playbook.md` | v1.1 — Production-ready | ~7,100 | Yes |
| 2. Activist Organizing Security | `phase-2-activist-organizing-security-playbook.md` | v1.1 — Production-ready | ~9,500 | Yes |
| 3. Financial Resistance | `phase-2-financial-resistance-playbook.md` | v1.0 — Pending legal review | ~6,300 | After nonprofit attorney review |
| 4. Institutional Whistleblowing | `phase-2-institutional-whistleblowing-security-playbook.md` | v1.0 — Production-ready | ~8,700 | Yes |
| 5. Journalist Security | `phase-2-journalist-security-playbook.md` | v1.0 — Production-ready | ~9,800 | Yes |
| 6. DV Survivor Safety | `phase-2-dv-survivor-safety-playbook.md` | v1.0 — Pending DV advocate review | ~8,900 | After NNEDV Safety Net review |

### Distribution Infrastructure: Complete

- Tier 2 contact list: 33 organizations across 4 sectors (digital rights, journalist orgs, academic programs, security researcher communities)
- Tier 3 contact list: 30 organizations (policy institutions, labor unions, academic law/policy schools)
- Outreach messaging templates: Complete for all sectors
- Threat update cadence and sentinel monitoring: Infrastructure established

### Phase 1 Status: In Progress

Phase 1 Tier 1 outreach (the personal OpSec guide distributed to immigration legal aid, community organizations, and mutual aid networks) is at Step 1.3. Phase 2 content deployment is gated on Phase 1 Tier 1 outreach completing its Week 7 data collection — the earliest date for full Phase 2 wave launch is approximately August 2026. Pilot distribution (3–5 organizations) can begin at Week 4, without waiting for the gate.

---

## Section 2: Scenario Prioritization — Which Six to Launch First and Why

The six playbooks are prioritized by three factors: severity of the threat gap the playbook addresses, availability of a distribution channel from existing Tier 1/2 outreach, and whether the playbook requires external validation before deployment.

### Tier A — Deploy at the July 26 Quarterly Review (Wave 1)

These two are ready for immediate deployment at the first Phase 2 public content launch. No blocking dependencies. Distribution channels exist.

**1. Immigration Surveillance Evasion (Playbook 1) — Deploy first, July 26**

Rationale: The highest-risk population in the corpus. ELITE address scoring, ICE Mobile Fortify field biometrics, ICM social graph mapping, and post-SCOTUS DOGE/SSA data fusion are all operational against this population now. The Tier 1 immigration legal aid distribution channel (NILC, CLINIC, RAICES, ILRC) from Phase 1 outreach is the natural vehicle — legal aid case managers are already the trusted intermediaries for distributing this to the people who need it. The playbook is designed to be shared by a legal aid case manager with a client, not cold-distributed publicly.

Threat model snapshot: Palantir ELITE aggregates Medicaid, HHS, DMV, commercial broker location data, and ALPR hits to score address confidence. ICE Mobile Fortify runs handheld facial recognition and fingerprints against DHS biometric databases in any street-level encounter — 100,000+ field uses documented. ICM social graph maps family relationships as location anchors. Post-SCOTUS SSA access adds SSN-linked identity and address history to the DHS data pipeline.

**5. Journalist Security (Playbook 5) — Deploy concurrently, July 26**

Rationale: The June 12, 2026 FISA Section 702 reauthorization deadline creates a policy urgency window that makes pre-deadline distribution higher-value. The Tier 2D contact list (FPF, CPJ, RCFP, PEN America) maps directly to this playbook's content. FPF pilot engagement should begin at Week 4 (before the gate), making this the first pilot-eligible playbook alongside Playbook 4.

Threat model snapshot: CBP border device search authority (no warrant, no probable cause) is the primary evidence-destruction risk at international crossings. PRISM Section 702 compels access to journalist email and cloud storage when communicating with foreign sources; the failed warrant-reform amendment (42–50 Senate vote) confirms this continues unconstrained. NSLs compel carrier and provider disclosure of journalist metadata without judicial authorization. The border is the highest-risk physical encounter for journalists with source material.

---

### Tier B — Deploy September 2026 (Wave 2)

These two are ready to deploy and have distribution channels, but should follow the Wave 1 launch and the Week 7 adoption gate.

**4. Institutional Whistleblowing (Playbook 4) — Deploy September, pilot at Week 5**

Rationale: Government Accountability Project (GAP) and POGO are the natural pilot partners and have the fastest feedback cycle of any Tier 2 contact. The playbook should pilot at Week 5 (before the full gate) because GAP and POGO's engagement is high-probability and the feedback is likely to be substantive. The whistleblower legal protection landscape (WPA coverage gaps, parallel construction risk) is highly topical given current federal workforce restructuring.

Threat model snapshot: All government surveillance capabilities apply at elevated intensity to suspected insider disclosers. Cellebrite UFED physical extraction from a government-issued device in AFU state is the primary device-forensics threat. Government network monitoring is comprehensive and leaves audit logs accessible to agency security. PRISM-authorized access to email and cloud storage of suspected disclosers is legally available. The primary failure mode for whistleblowers is not disclosure-phase OpSec — it is using a government device, home network, or personal email anywhere in the chain.

**2. Activist Organizing Security (Playbook 2) — Deploy September**

Rationale: Drone aerial surveillance (Skydio X10D, LAPD/NYPD confirmed operational deployment at protests), Babel Street persistent social media OSINT, and Flock Safety ALPR tracking of vehicle approach to protest sites are all active threats now. The EFF, ACLU, and NLG contacts in Tier 2A are the distribution partners. Deploy after Wave 1 to allow Wave 1 feedback to inform framing.

Threat model snapshot: Babel Street continuously monitors public social media for keyword and sentiment patterns; content posted immediately before or during public actions is highest-risk. Flock Safety ALPR is deployed in 5,000+ communities and creates a vehicle-movement record correlating to protest attendance. Drone surveillance at oblique angles partially defeats ground-level mask countermeasures. The combination requires layered countermeasures across device, network, physical, and behavioral dimensions simultaneously.

---

### Tier C — Deploy November 2026 or later (Wave 3)

These two have binding external validation requirements before any distribution.

**6. DV Survivor Safety (Playbook 6) — Deploy November 2026 minimum**

Binding constraint: NNEDV Safety Net Project practitioner review is non-negotiable before any distribution. The escalation risk language in the safety planning section — specifically the finding that removing stalkerware from a device where an abuser has root access can trigger physical violence escalation — is clinically validated DV guidance that must be confirmed by a practitioner before it reaches survivors. No substitute validator exists. Distribution through general Tier 1/2 channels is not appropriate; this playbook must reach survivors via DV-advocate-mediated distribution (shelters, coalitions, VAWA-funded programs).

Contact timeline: Initiate NNEDV Safety Net outreach at Week 15. Review timeline typically 4–8 weeks for DV organizations. Earliest distribution: November 2026.

Threat model snapshot: The primary adversary is an intimate partner with pre-existing device access, shared account credentials, shared family plan location sharing, and potentially legal access to shared financial accounts. Stalkerware (FlexiSPY, Hoverwatch, mSpy) runs invisibly on a device with root access and survives factory resets if root access is maintained. Device replacement — not hardening — is the correct first countermeasure. The wrong action, executed in the wrong order, can increase physical danger. This is the highest-stakes deployment decision in Phase 2.

**3. Financial Resistance (Playbook 3) — Deploy October 2026, pending legal review**

Binding constraint: Nonprofit tax counsel review of the donor privacy, fiscal sponsorship, and organizational financial documentation sections before formal distribution. The financial and legal claims in this playbook are accurate at a general level but require practitioner validation before distribution to organizations whose staff may act on them with legal consequences. Initiate nonprofit attorney contact immediately — this is a Gate 1 action.

Options for expediting: The National Council of Nonprofits, Bolder Advocacy (Alliance for Justice), or a Tier 3 academic law contact with nonprofit tax expertise. An informal review (not a formal legal opinion) is sufficient. The playbook can circulate informally via Gist link while waiting for this review — the constraint applies to formal Tier 2/3 outreach, not to making the Gist accessible.

Threat model snapshot: The IRS LCA Palantir platform maps financial social networks among investigation targets — organizations with financial transactions connecting to entities under investigation are pulled into that entity's social graph. DOGE-era IRS-DHS data sharing (contested but partially operational) creates a pipeline between financial records and immigration enforcement. Cryptocurrency exchange KYC data (Coinbase specifically documented in IRS LCA contract language) is accessible to the platform. The threat is social graph expansion, not individual audit risk.

---

## Section 3: Scope of Each Scenario

### Tools and Techniques by Playbook

| Playbook | Core Countermeasures | Advanced Techniques | Format |
|----------|---------------------|--------------------|----|
| 1. Immigration | ELITE address admin hygiene, Medicaid address alignment, ICM family contact security, Mobile Fortify encounter protocol | Signal with disappearing messages for family, no new administrative records at shelter addresses | 1,500-word numbered protocol, Gist |
| 2. Activist | 72-hour pre-action social media hygiene, vehicle identity separation, mask+hat+sunglasses+clothing-swap physical protocol, emergency check-in with legal support | ADS-B Exchange drone monitoring, Faraday bag for devices, layered physical exit countermeasures | Two-part: printable one-page checklist + technical guide, Gist + PDF |
| 3. Financial | Organizational financial documentation, fiscal sponsorship donor privacy, Monero non-KYC entry/exit, account compartmentalization by activity | Cash structuring law awareness, financial social graph separation, FinCEN SAR triggers | Prose document, 3 sections, Gist |
| 4. Whistleblowing | SecureDrop via Tor on non-identity-linked device/network, BFU device state before any anticipated encounter, WPA protection framework | Parallel construction documentation protocol, OSC complaint pathway, congressional oversight channel | WPA coverage gap table + SecureDrop directory appendix, Gist |
| 5. Journalist | Border crossing clean device protocol, source Signal account on dedicated GrapheneOS device with VoIP number, SecureDrop deployment | PRISM-resistant foreign source communication, Safety Number in-person verification, FPF setup support | Scenario-structured (not tool-structured), 4 sections, Gist |
| 6. DV Survivor | Safety planning before any action (NNEDV Safety Net methodology), device replacement not hardening, new accounts on new device | Stalkerware detection, location tracking audit across all vectors, evidence preservation | Two-column practitioner format, PDF only |

### Research Requirements per Scenario

All six playbooks are already written with sourced threat models. Remaining research needs are for the July 26 quarterly threat model update and ongoing maintenance:

- **Immigration**: ICM biometric contract expected September 2026 — confirm deployment scope when awarded
- **Activist**: Flock Safety metro expansion tracking for LA, NYC, Chicago, Houston, Miami — monthly sentinel scan
- **Financial**: IRS-DHS data sharing litigation status (Fourth Circuit; confirm outcome before Wave 3 distribution)
- **Whistleblower**: WPA coverage gaps — confirm no legislative change before formal distribution
- **Journalist**: FISA Section 702 outcome post-June 12 deadline — update NSA section within 48 hours of resolution
- **DV Survivor**: NNEDV Safety Net current stalkerware guidance (techsafety.org) — confirm alignment with playbook's escalation risk language before review meeting

---

## Section 4: Timeline and Dependencies

### 12-Month Execution Arc

```
Q2 2026 (June–August)
  Week 0:    Pre-launch Phase 1 corpus corrections (Mobile Fortify, BFU/AFU additions)
  Weeks 1–3: Phase 1 Tier 1 active outreach (40+ immigration legal aid organizations)
  Weeks 4–5: Pilot — Journalist playbook → FPF; Whistleblower playbook → GAP/POGO
  Weeks 5–6: Tier 2 pilot wave (5 organizations: FPF, EFF, Access Now, GAP, STOP)
  Weeks 5–12: Full Tier 2 wave (33 organizations across digital rights, journalist, academic, researcher sectors)
  July 26:   GATE 1 — Quarterly review + Phase 2 Wave 1 launch
             → Publish Immigration playbook + Journalist playbook
             → Publish threat model update (Mobile Fortify, drone, HART, DOGE/SSA)
             → Nonprofit attorney contact for Financial playbook (if not already initiated)

Q3 2026 (September)
  Week 15+:  NNEDV Safety Net outreach (binding constraint for DV playbook)
  Weeks 11–12: Tier 3 Wave — Policy organizations (Georgetown CPT, ACLU SPT, Brennan Center, New America OTI)
  Weeks 13–14: Tier 3 Wave — Labor organizations (AFL-CIO, UFW, NDWA, SEIU, CWA)
  September: GATE 2 — Wave 2 launch (if: 25+ Tier 2 orgs contacted, 1 institutional validation)
             → Publish Activist organizing playbook
             → Publish Whistleblower playbook (full wave, post-pilot feedback incorporated)
             → Initiate Spanish Part 0 translation if Tier 1/2 feedback shows language barrier
  September: ICM biometric contract expected — update threat model within 1 week of confirmation

Q4 2026 (October–December)
  October:   Financial resistance playbook distribution — contingent on nonprofit attorney review complete
  October:   Tier 3 Wave — Academic law/policy schools (Georgetown Law, Harvard, Yale, UW, Columbia, Berkeley)
  November:  DV survivor safety playbook distribution — contingent on NNEDV Safety Net review complete
  December:  GATE 3 — Year-end review
             → Check: 20+ Tier 3 orgs contacted, 1 policy brief citation or 1 academic course integration
             → Spanish Part 0 published, used by at least 1 Tier 1 organization
             → All 5 sentinel threat vectors actively monitored

Q1–Q2 2027 (January–May)
  January–March: Video primer scripts (4 scripts: ELITE, Signal, ICE encounter, protest phone)
  February–March: Texas supplement decision tree (if geographic gap confirmed by feedback)
  Second-round Tier 3 outreach where initial response was weak
  May 31:    GATE 4 — Year 1 evaluation
             → Decision: maintain and continue, pivot distribution strategy, or transfer stewardship
```

### Parallel vs. Sequential Constraints

Modules that run in parallel (no dependency on each other):
- Threat model update production (Module 1) and Tier 2 pilot outreach (Module 4) can begin simultaneously
- Whistleblower playbook pilot (GAP, Week 5) and Journalist playbook pilot (FPF, Week 4) are parallel
- Tier 3 policy organizations (Weeks 11–12) and Tier 3 labor organizations (Weeks 13–14) are parallel within the same wave

Modules that must sequence:
- Full Tier 2 wave (Weeks 5–12) must precede Tier 3 launch by at least 6 weeks — Tier 3 benefits from Tier 2 credibility signals
- DV playbook distribution cannot begin before NNEDV Safety Net review complete — hard gate, no exception
- Financial playbook formal distribution cannot begin before nonprofit attorney review — hard gate for formal outreach; Gist access is acceptable pending review
- Academic law/policy school outreach (Tier 3C) must align with semester start — September is the earliest viable window; May–August sends are wasted

---

## Section 5: Audience Expansion Strategy

### Three-Tier Architecture (Current)

**Tier 1 — Personal security for high-risk individuals**: Immigration legal aid organizations receive the core corpus (threat model + playbook + implementation guide) and distribute it to their clients. Organizations include NILC, CLINIC, RAICES, ILRC, NLG chapters. These organizations are trusted intermediaries — the corpus reaches undocumented immigrants, DACA recipients, and individuals in removal proceedings via case managers, not via cold public distribution.

**Tier 2 — Institutional distribution through expert organizations**: 33 organizations across four sectors receive the full corpus plus relevant scenario playbooks. These organizations have research, training, or advocacy capacity to validate and amplify the corpus through their own networks. Sectors: digital rights (EFF, ACLU, CDT, Access Now, STOP), journalist organizations (FPF, CPJ, RCFP, PEN America, IRE), academic programs (law school clinics, technology policy centers), security researcher communities (academic mailing lists, privacy-focused conference channels).

**Tier 3 — Institutional policy and regulatory influence**: 30 organizations that shape regulatory, litigation, and legislative outcomes. These organizations are not the operational users of the corpus — they are the policy layer that can turn the documented surveillance infrastructure into legislative testimony, amicus briefs, or agency rule comments. Sectors: policy institutions (Georgetown CPT, Brennan Center, New America), labor unions (AFL-CIO, UFW, NDWA, SEIU), academic law schools (Georgetown, Harvard, Yale, Berkeley, Columbia).

### Expansion Tracks Not Yet in Pipeline

Three new audiences require outreach infrastructure that does not yet exist:

**DV organizations**: National Domestic Violence Hotline, NNEDV Safety Net Project, state DV coalitions, VAWA-funded programs. The DV playbook is the content vehicle; NNEDV Safety Net is both the gatekeeper (must review the playbook before distribution) and the distribution infrastructure (their Safety Net network reaches shelter technology safety staff nationally). This is a separate organizational outreach track from Tier 1/2/3 — do not route through existing channels.

**Election worker networks**: National Association of State Election Directors (NASED), Election Center (National Association of Election Officials). CISA's withdrawal of EI-ISAC election security support has created a security gap for local election officials with no existing federal replacement. The corpus addresses the government surveillance infrastructure used against public political activity — an election worker security playbook is not yet written but would serve this population. This is an identified Phase 2 extension, not yet scoped.

**Public defender offices**: National Legal Aid and Defender Association (NLADA), Federal Defender organizations. Public defenders representing immigration and civil rights defendants need to understand the surveillance infrastructure used to build cases against their clients. The corpus's threat model and playbooks are directly applicable. This outreach should frame the corpus as litigation-support documentation, not a security guide.

### Scaling Path: Tier 1 → Tier 2 → Tier 3 → General Public

The distribution architecture is designed to compound credibility at each tier. Tier 1 adoption by immigration legal aid organizations creates a track record of real-world use that makes Tier 2 outreach credible. Tier 2 engagement by digital rights organizations (EFF, Access Now) creates the institutional validation that makes Tier 3 policy outreach compelling to Georgetown CPT or the Brennan Center. Tier 3 citation in policy briefs or legislative testimony creates the public record that supports general public distribution without the corpus being dismissed as advocacy.

General public distribution (Reddit, social media, Substack) is appropriate after Tier 3 begins — not before. The goal is that by the time the corpus reaches general public channels, it has already been validated by press freedom organizations, civil liberties groups, and academic researchers.

---

## Section 6: Success Metrics

### Minimum Phase 2 Completion Criteria (All must be met)

- All six playbooks distributed to at least one organization in their primary target sector, with evidence of receipt (reply, click, or integration signal)
- At least one major digital rights organization (EFF, CDT, Access Now, or Privacy International) has acknowledged the corpus — this is the Tier 2 → Tier 3 gate
- DV survivor playbook has completed NNEDV Safety Net practitioner review and been distributed through at least one DV coalition
- Financial resistance playbook has completed nonprofit attorney review
- Threat model is current as of the last quarterly review date (all five sentinel vectors monitored, no stale claims)
- At least one Tier 1 immigration legal aid organization is using the immigration playbook in client intake

### Stretch Goals (Phase 2 Impact Tier)

- Legal or legislative citation: Any element of the corpus cited in a court filing, amicus brief, legislative testimony, or peer-reviewed paper. This is the highest-leverage outcome — it means the corpus is functioning as authoritative reference in an adversarial legal context.
- Organizational integration: At least one Tier 2 organization (FPF, EFF, or equivalent) includes a playbook in their own training materials or security program, crediting the corpus as a source.
- Media coverage: The threat model or a playbook is cited or excerpted in journalism from The Intercept, Wired, or equivalent outlet with documented surveillance beat. This is the fastest path to general public distribution.
- Spanish translation in use: At least one Tier 1 immigration legal aid organization reports using Spanish Part 0 (data broker opt-outs) directly with clients.

### Failure Indicators (Triggering Pivot Decision)

- Tier 1 response rate below 5% after 40+ sends: Pause Tier 2 full wave, re-evaluate framing and channel
- No Tier 2 institutional validation by September 30: Delay Tier 3 launch by 4 weeks, run secondary Tier 2 wave
- DV playbook NNEDV contact not initiated by December 31: Escalate to direct contact with NNEDV Safety Net Project director — this is a missed deadline, not an acceptable slip
- Threat model has a documented factual error cited by a Tier 2 contact: Correct within 48 hours; update all affected contacts; log in threat-update-cadence.md

---

## Section 7: Resource Allocation

### Orchestrator Hours by Module (12-Month Estimate)

| Module | Description | Estimated Hours | Status |
|--------|-------------|----------------|--------|
| 1 | Threat model update (Mobile Fortify, drone, HART, DOGE/SSA) | 12–16 | Research base complete |
| 2 | Advanced protection guides (compartmentalization, aerial counter-surveillance, forensic hardening) | 20–25 | Conceptual framework complete |
| 3 | Playbook deployment coordination (outreach drafts, tracking, feedback integration) | 15–20 | Playbooks written; distribution work needed |
| 4 | Tier 2 pilot + full wave execution | 25–30 | Templates complete; execution needed |
| 5 | Tier 3 institutional expansion | 28–37 | Contact lists complete; personalization needed |
| 6 | Threat model maintenance (12 months ongoing) | 40–48 | Infrastructure established |
| 7 | Format diversification (Spanish translation, Texas supplement, video scripts) | 24–34 | Contingent on adoption data |
| **Total** | | **164–210 hours** | |

Monthly average: 14–18 hours/month over 12 months. Module 7 is contingent — if adoption data does not confirm format as a barrier, reduce total to 140–176 hours.

### External Cost Estimate

| Item | Cost | Priority | Gate |
|------|------|----------|------|
| Bitly paid tier (6 playbook tracking links) | $35/year | Low | Gate 1 |
| Spanish Part 0 translation (if no Tier 1 partner) | $200–400 | Medium | Gate 2 |
| Nonprofit attorney review (financial playbook) | $0–500 | High | Immediate |
| Video production (4 primers, only if commissioned) | $3,200–8,000 | Low | Gate 3 |

**Total required cost**: Under $500. Video production is the only significant optional cost and should not be committed until Gate 3 confirms it is warranted by adoption data.

### No New Tools Required for Modules 1–6

Core infrastructure (GitHub Gist, Bitly free tier, Gmail, Google Sheets) is sufficient for the full Phase 2 deployment. PDF export via Google Docs is sufficient for the DV playbook's required PDF format. No new platform subscriptions are needed.

---

## Decision Points for May 25-27 Review

The following decisions require explicit user input to proceed. Each is a greenlight (proceed as designed), redirect (modify approach), or defer (hold pending more data):

**Decision 1: Wave 1 playbook launch authorization**
Which of the two Wave 1 playbooks (Immigration, Journalist) to release at the July 26 quarterly review, and whether to release them simultaneously or stagger by 2 weeks. Recommendation: release simultaneously, as they serve different distribution channels with no interference.

**Decision 2: Financial playbook nonprofit attorney outreach**
Initiate contact with a nonprofit tax attorney now, before Gate 1, to avoid it becoming a Wave 3 bottleneck. Recommend initiating this week. If no attorney contact is established by Gate 1 (July 26), the Financial playbook's formal distribution slips to Q1 2027.

**Decision 3: DV playbook NNEDV contact timeline**
NNEDV Safety Net outreach is currently scheduled for Week 15. Given the 4–8 week review timeline at DV organizations, initiating at Week 15 targets November distribution at the earliest. If the user wants November deployment rather than December, contact should begin at Week 12 instead.

**Decision 4: Tier 3 academic outreach semester alignment**
Academic law and policy schools (Tier 3C) should receive outreach at semester start. September 2026 (fall start) or February 2027 (spring start) are the options. The September window requires Tier 3C outreach to begin in Week 14–15 — which requires confirmed Tier 2 institutional validation by that point. If Tier 2 validation is delayed, defer Tier 3C to February.

**Decision 5: Video primer production decision**
This is a Gate 3 decision (December 2026), but the user should decide now whether to begin building relationships with potential production partners (FPF, IRE) through the Tier 2 outreach, or to defer the conversation until adoption data is available. Building the relationship early costs nothing and creates the option; not building it forecloses the FPF/IRE co-production path.

---

*Created: May 19, 2026. Synthesized from: PHASE_2_SEQUENCING_STRATEGY.md, PHASE_2_DETAILED_IMPLEMENTATION_ROADMAP.md, SCENARIO_PLAYBOOK_INDEX.md, PHASE_2_DEPLOYMENT_READINESS.md, PHASE_2_SEQUENCING.md. For detailed module-by-module execution specifications, effort breakdowns, and sentinel vector procedures, see PHASE_2_DETAILED_IMPLEMENTATION_ROADMAP.md. Quarterly review dates: Gate 1 July 26, 2026; Gate 2 September 30, 2026; Gate 3 December 31, 2026; Gate 4 May 31, 2027.*
