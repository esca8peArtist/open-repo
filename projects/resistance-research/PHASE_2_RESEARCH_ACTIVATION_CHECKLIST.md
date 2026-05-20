---
title: "Phase 2 Research Activation Checklist — May 21 Evening Execution Version"
subtitle: "Domain Readiness Verification, Infrastructure Staging, Blocking Assumption Audit, and Kick-Off Preparation"
created: 2026-05-21
session: "General Research Agent — Phase 2 Activation Prep"
status: "authoritative — supersedes all prior activation checklists"
authority_note: |
  This document consolidates and supersedes PHASE_2_RESEARCH_ACTIVATION_CHECKLIST.md (May 19, Session 1361)
  and phase-2-research-activation-checklist.md (May 20, Sessions 1405/1408). The authoritative
  finding from the May 20 file audit: all four Phase 2 domains are FULLY WRITTEN and production-complete.
  Total remaining effort is 19–40 hours of distribution preparation, not research production.
  Any document referencing a 120–130 hour production window for Domains 57 and 59 is obsolete.
supersedes:
  - PHASE_2_RESEARCH_ACTIVATION_CHECKLIST.md (May 19)
  - phase-2-research-activation-checklist.md (May 20)
domain_production_status_verified: "May 20, 2026 — direct file audit (wc -w + grep -c https://)"
domain_totals:
  word_count: 35306
  citation_urls: 237
  domains_complete: 4
decision_gate: "May 21 synthesis outcome → Phase 2 distribution activation May 21 evening"
execute_within: "1 hour of reading synthesis outcome in CHECKIN.md"
companion_files:
  - phase-2-research-timeline-template.md
  - PHASE_2_RESEARCH_TIMELINE_TEMPLATE.md
  - phase-2-research-kick-off-email-template.txt
  - PHASE_2_DOMAINS_56_59_RESEARCH_ACTIVATION_PREP.md
  - MAY_21_SYNTHESIS_EXECUTION_FRAMEWORK.md
---

# Phase 2 Research Activation Checklist
## May 21 Evening Execution Version

*General Research Agent — May 21, 2026*

**How to use this document**: Read Section 1 (15 min) to confirm domain production status against the May 20 verified baseline. Section 2 (15 min) confirms source libraries and infrastructure are staged. Section 3 (10 min) provides the distribution timeline in its final form. Section 4 (15 min) audits blocking assumptions and time-sensitive dependencies for each domain. Section 5 (5 min) lists user decisions required before any distribution email sends.

**Lead finding**: All four Phase 2 domains (56–59) are production-complete as of May 15–20, 2026. The multi-week production writing schedules in earlier planning documents are eliminated. Phase 2 is a distribution-preparation and distribution-execution operation from May 21 forward.

**If synthesis outcome is WEAK**: Domain 56, 58, and 59 distribution proceed on their scheduled dates regardless. Domain 57 August 10 distribution proceeds. What changes under WEAK is Tier 2 outreach timing. See Section 5, Decision Gate, for outcome-specific adjustments.

---

## Section 1: Domain Outline Audit — Production-Readiness Verification

*Audit basis: May 20 direct file verification. Word counts via `wc -w`, citation URL counts via `grep -c "https://"`, section architecture by header scan. All findings from the authoritative May 20 checklist at `phase-2-research-activation-checklist.md`.*

### Audit Criteria

For each domain, five criteria apply:

- **(a) Canonical file exists at verified path** — confirmed by direct file check
- **(b) Word count at or above target (6,000+ words)** — verified by wc -w
- **(c) Citation URL count at or above target (40+ confirmed https:// URLs)** — verified by grep count
- **(d) Section architecture complete** — executive summary, causal pathways, reform architecture, movement/distribution contacts present
- **(e) Currency: no blocking external event has rendered the document factually outdated since production** — assessed per domain

---

### Domain 56: Civil Service Politicization and Nonpartisan Governance Architecture

**Canonical file**: `projects/resistance-research/domain-56-civil-service-politicization-governance.md`
(Root level — not in `domains/` subdirectory. Confirm this path before Gist upload.)

**May 20 verified audit results**:

| Criterion | Status | Detail |
|-----------|--------|--------|
| (a) File exists | CONFIRMED | Root level of projects/resistance-research/ |
| (b) Word count | AT TARGET | 6,267 words (target: 6,000–7,000) |
| (c) Citation count | AT TARGET | 45 confirmed https:// URLs (threshold: 40+) |
| (d) Section architecture | CONFIRMED | 10 sections: Central Finding, Pendleton Foundation, Schedule P/C Pathway, DOGE Workforce Pathway, MSPB Hollowing, Enforcement Agency Collapse, Whistleblower Dismantlement, International Precedents, Reform Architecture, What Is at Stake |
| (e) Currency | LOW RISK | Schedule Policy/Career Final Rule is enacted law; no court stay as of May 20. H.R. 492 / Saving the Civil Service Act enters June 1–30 legislative window — distribution accelerant, not currency risk |

**Source staging**: `DOMAIN_56_SOURCE_STAGING.md` confirmed present. All primary sources are open-access federal documents (Federal Register, OPM.gov, Congress.gov) or established civil society publications. No paywall dependencies.

**Cross-domain bridges**: Domain 29 (DOJ Capture — DOJ Civil Rights Division 250-attorney departure figure must be consistent between documents), Domain 26 (Government Accountability — IG office capacity), Domain 6 (Judicial Independence — MSPB and Humphrey's Executor argument). These bridges are pre-documented; verify before any cross-domain citations in cover emails.

**Pre-launch action (May 21 evening, 2 hours)**:
- [ ] URL spot-check: browser-test all 45 citation URLs. Replace any dead links.
- [ ] Check Congress.gov for H.R. 492 status — if advanced since May 20, add one sentence to distribution cover email noting committee status.
- [ ] Mark Domain 56 distribution-ready in CHECKIN.md.

**Verdict**: VERIFIED PRODUCTION-COMPLETE. Enters distribution pipeline immediately post-synthesis. First send: May 26 – June 7.

---

### Domain 57: Multilateral Withdrawal and US Commitment Collapse

**Canonical file**: `projects/resistance-research/domains/domain-57-multilateral-withdrawal-and-us-commitment-collapse.md`

**Critical correction from prior checklists**: Sessions 1321–1361 expected Domain 57 to be an unwritten outline requiring 45–51 hours of July production work. The May 20 audit confirmed Domain 57 is FULLY WRITTEN at 9,201 words. The 45–51 hour production window is eliminated.

**May 20 verified audit results**:

| Criterion | Status | Detail |
|-----------|--------|--------|
| (a) File exists | CONFIRMED | domains/ subdirectory |
| (b) Word count | ABOVE TARGET | 9,201 words (target: 6,000–7,000; actual is 47% above target) |
| (c) Citation count | ABOVE TARGET | 51 confirmed https:// URLs (threshold: 40+; YAML shows 47, scan found 51) |
| (d) Section architecture | CONFIRMED | 8+ major sections: Executive Summary, Architecture of What Was Withdrawn, Five Causal Pathways, Global Pattern, Resistance Architecture, Policy Leverage Windows, Movement Infrastructure and Organizational Contacts, Reform Architecture, Cross-Domain Integration, Sources |
| (e) Currency | MEDIUM RISK (one section) | ICC sanctions section — ongoing diplomatic developments. January 7, 2026 Presidential Memorandum and 66-organization catalog are stable. ICC section requires spot-check before August 10 distribution, not before May 21 launch |

**Source library**: `DOMAIN_57_SOURCE_LIBRARY.md` confirmed with 57 sources staged; document integrates 51 confirmed. Prior checklist concern about Ikenberry "Liberal Leviathan" paywall access is resolved — Domain 57 is written with confirmed sourcing at 51 URLs. No paywall access required.

**Cross-domain bridges**: Domain 23 (Trade Policy — do NOT duplicate IEEPA/Youngstown constitutional analysis; Domain 57 must cross-reference Domain 23 and differentiate), Domain 28 (War Powers — constitutional-asymmetry argument must be clearly differentiated from war powers analysis), Domain 51 (Campaign Finance — multilateral withdrawal from OSCE/ODIHR election integrity monitoring).

**Distribution timing**: August 10, 2026 is the first distribution date. This is 43 days before UNGA 81 High-Level Week (September 22–28) — the minimum viable lead time for Senate Foreign Relations Committee staff and international organizations to have reading time. Missing August 10 shifts the primary distribution anchor to November 3 domestic midterm framing.

**Pre-launch action (May 21 evening, 1 hour)**:
- [ ] Confirm canonical file at `domains/domain-57-multilateral-withdrawal-and-us-commitment-collapse.md` is accessible.
- [ ] Check hrw.org and cicc.org for any post-May 15 ICC sanctions developments. Flag for pre-distribution spot-check in July.
- [ ] Record August 10 as the first distribution date in working calendar.
- [ ] Mark Domain 57 distribution-ready in CHECKIN.md.

**Verdict**: VERIFIED PRODUCTION-COMPLETE. August 10 distribution requires no production work — only pre-distribution URL spot-check and ICC section currency verification in July.

---

### Domain 58: Tribal Sovereignty as Democratic Infrastructure

**Canonical file**: `projects/resistance-research/domains/domain-58-tribal-sovereignty.md`
(Not the earlier draft at `domains/domain-38-tribal-sovereignty-indigenous-democratic-design.md` — confirm correct file before any distribution action.)

**Critical correction from prior checklists**: Sessions 1321–1361 identified Domain 58 as having a 5,200-word draft requiring an 8–12 hour execution pass. The May 20 audit confirmed the canonical file is FULLY WRITTEN at 11,388 words — the highest word count and citation count of all four Phase 2 domains.

**May 20 verified audit results**:

| Criterion | Status | Detail |
|-----------|--------|--------|
| (a) File exists | CONFIRMED | domains/domain-58-tribal-sovereignty.md (canonical) |
| (b) Word count | SIGNIFICANTLY ABOVE TARGET | 11,388 words (target: 7,000–8,000; actual is 42–62% above target) |
| (c) Citation count | WELL ABOVE TARGET | 90 confirmed https:// URLs (threshold: 40+; actual is 125% above threshold) |
| (d) Section architecture | CONFIRMED | 11 major sections including: Executive Summary, Legal Foundation/Treaty Rights, 2025–2026 Assault, Trump v. Barbara Citizenship Threat, Seven Causal Pathways, Democratic Design Analysis, Post-Callais Voting Rights Landscape, Cross-Domain Architecture, Reform Pathways, Actionable Intelligence for Resistance Networks, Distribution Contacts, Bibliography. Rapid-response protocol for Trump v. Barbara is pre-documented in Section 9. |
| (e) Currency | HIGH RISK — managed | Updated May 19, 2026 to reflect May 18 SCOTUS GVR in Turtle Mountain Band of Chippewa Indians v. Howe. Trump v. Barbara ruling (expected late June/early July 2026) will require rapid-response update, but rapid-response protocol is pre-written in Section 9. |

**Source staging**: `DOMAIN_58_SOURCE_STAGING.md` confirmed with 42+ supplemental sources. Document integrates 90 confirmed URLs. All primary sources are open-access (NARF case pages, SCOTUS docket, Congress.gov, tribal voting rights organizations).

**Cross-domain bridges**: Domain 49 (Callais/VRA Redistricting — post-Callais tribal district impact; confirm Callais ruling characterization is consistent), Domain 39 (Healthcare — IHS as treaty-obligated healthcare; Oregon Medicaid RCT citation shared), Domain 1 (Voting Rights — NVRA-tribal enrollment nexus).

**Trump v. Barbara rapid-response protocol**: Pre-built in Section 9 of canonical file. Expected update time: 2–3 hours after ruling is issued. Monitor: SCOTUSblog (scotusblog.com) and NARF Tribal Supreme Court Project (sct.narf.org).

**Pre-launch action (May 21 evening, 30 minutes)**:
- [ ] Confirm `domains/domain-58-tribal-sovereignty.md` is the canonical file — NOT `domains/domain-38-tribal-sovereignty-indigenous-democratic-design.md`.
- [ ] Activate SCOTUS monitoring: bookmark SCOTUSblog and sct.narf.org for Trump v. Barbara updates.
- [ ] Check SCOTUSblog before starting any Domain 58 distribution work — confirm ruling has NOT issued before May 21.
- [ ] Mark Domain 58 distribution-ready in CHECKIN.md.

**NARF peer review**: Strongly recommended before June 15 distribution to validate legal accuracy of tribal voting rights and Callais analysis. Send request June 1–5; allow 5–7 business days async; incorporate by June 14. Not a blocker for May 21 launch confirmation.

**Verdict**: VERIFIED PRODUCTION-COMPLETE. June 15 distribution requires NARF peer review (5–7 days; schedule now). Trump v. Barbara rapid-response is pre-built and ready.

---

### Domain 59: Economic Precarity and the Civic Participation Crisis

**Canonical file**: `projects/resistance-research/domains/domain-59-economic-precarity-and-civic-participation.md`

**Critical correction from prior checklists**: Sessions 1321–1361 expected Domain 59 to be an unwritten outline (with one 3,200-word Section 1 draft) requiring 59–65 hours of June–July production work. The May 20 audit confirmed Domain 59 is FULLY WRITTEN at 8,450 words with a separate 13-contact verified expert list.

**May 20 verified audit results**:

| Criterion | Status | Detail |
|-----------|--------|--------|
| (a) File exists | CONFIRMED | domains/domain-59-economic-precarity-and-civic-participation.md |
| (b) Word count | ABOVE TARGET | 8,450 words (target: 6,000–7,000; actual is 20–40% above target) |
| (c) Citation count | AT TARGET | 49 confirmed https:// URLs (threshold: 40+; 22.5% above threshold) |
| (d) Section architecture | CONFIRMED | 8 major sections: Executive Summary, Time-Poverty Architecture (quantified barriers), Five Causal Pathways, Policy Leverage Windows 2026–2027, Movement Landscape, Cross-Domain Architecture, Distribution Strategy/Democratic Design Reframe, Unique Contribution, Sources Summary |
| (e) Currency | LOW RISK | HHS OBBBA interim final rule is required by statute to be issued by June 1, 2026. Initial CMS guidance released December 2025. If the June 1 rule introduces material changes to work requirement implementation, Section 2 may need a one-paragraph update — but this is a monitoring item, not a structural concern |

**Source library**: `DOMAIN_59_SOURCE_LIBRARY.md` confirmed with 48 sources and 13 expert contacts with verified email addresses (verified May 19). Dallas Fed wp2517 (causal anchor), PNAS 2024, EPI wage reports — all open-access. No paywall dependencies for distribution-critical sources.

**Cross-domain bridges**: Domain 31 (Healthcare/OBBBA — Medicaid work requirements; Domain 59 covers only civic participation effects, not healthcare consequences), Domain 47 (Housing Security — housing policy failures; Domain 59 covers only voter registration disruption mechanism), Domain 50 (Healthcare-Democracy Nexus — NVRA-Medicaid enrollment cross-reference must be consistent).

**HHS OBBBA June 1 guidance monitoring**: Flag June 1 as both distribution launch date and HHS interim final rule monitoring date in working calendar. If the rule is materially significant, integrate into cover email rather than rewriting the document. The causal backbone (Dallas Fed wp2517, Slee/Desmond, PNAS 2024) is not affected by implementation guidance.

**Pre-launch action (May 21 evening, 15 minutes)**:
- [ ] Confirm `domains/domain-59-economic-precarity-and-civic-participation.md` is the canonical file.
- [ ] Flag June 1 as both distribution date AND HHS interim final rule monitoring date in working calendar.
- [ ] Mark Domain 59 distribution-ready in CHECKIN.md.

**Verdict**: VERIFIED PRODUCTION-COMPLETE. June 1 distribution target is confirmed. No production work remaining.

---

### Domain 60: Status and Decision

**Finding**: No Domain 60 file has been identified in the resistance-research directory as of May 20, 2026. There is no Domain 60 outline, source library, or scoping document.

**Decision framework by synthesis outcome**:
- **STRONG**: Domain 60 can be scoped June 1–5 as an optional expansion. Two strongest candidates from prior analysis: (A) IEEPA/Trade Policy Economic Sovereignty domain (SCOTUS ruling February 2026 creates a new anchor); (B) consolidated disability rights domain (SSA 7,000-job cut + OBBBA disability population impact). Neither is required for Phase 2 launch.
- **MODERATE**: Domains 56–59 are adequate. Domain 60 deferred indefinitely.
- **WEAK**: No Domain 60. Focus on completing Domains 58 and 59 distribution on schedule.

**Pre-launch action**: None required.

---

### Section 1 Summary — Domain Readiness Matrix

| Domain | Canonical File Path | Words | Citations | Status | Currency Risk | Pre-Launch Effort |
|--------|---------------------|-------|-----------|--------|---------------|-------------------|
| 56 | `domain-56-civil-service-politicization-governance.md` (root) | 6,267 | 45 | COMPLETE | LOW | 2 hrs (URL spot-check) |
| 57 | `domains/domain-57-multilateral-withdrawal-and-us-commitment-collapse.md` | 9,201 | 51 | COMPLETE | MEDIUM (ICC section) | 1 hr (ICC currency check) |
| 58 | `domains/domain-58-tribal-sovereignty.md` | 11,388 | 90 | COMPLETE | HIGH (Trump v. Barbara — managed) | 0.5 hr (file path confirmation + SCOTUS check) |
| 59 | `domains/domain-59-economic-precarity-and-civic-participation.md` | 8,450 | 49 | COMPLETE | LOW (HHS rule monitoring) | 0.25 hr (calendar flag) |
| **Total** | | **35,306** | **235** | **ALL COMPLETE** | | **~4 hrs** |

**Bottom line**: All four Phase 2 domains are production-complete. No research or writing work is required before distribution launches. Phase 2 is a distribution-preparation and outreach-execution operation.

---

## Section 2: Pre-Stage Research Databases

*Estimated time: 15 minutes. Confirm source libraries, expert contact lists, and technical infrastructure.*

### Source Libraries — Status by Domain

**Domain 56**: All sources open-access. Federal Register, OPM.gov, Congress.gov, established civil society publications. `DOMAIN_56_SOURCE_STAGING.md` present. Zero access barriers. CONFIRMED READY.

**Domain 57**: All distribution-critical sources open-access. 51 confirmed URLs integrate into the full document. Prior paywall concern for Ikenberry "Liberal Leviathan" is resolved — the document is written without requiring it. ICC sanctions materials are HRW and CICC open-access publications. `DOMAIN_57_SOURCE_LIBRARY.md` (57 sources staged) present. CONFIRMED READY.

**Domain 58**: All primary sources open-access. NARF case pages (narf.org, sct.narf.org), SCOTUS docket (scotusblog.com), federal statutes, Congress.gov. 90 confirmed URLs in the document. `DOMAIN_58_SOURCE_STAGING.md` (42+ supplemental sources) present. CONFIRMED READY.

**Domain 59**: All distribution-critical sources open-access. Dallas Fed wp2517 (confirmed open-access), PNAS 2024 (open-access after 6 months), EPI wage data (open-access), Eviction Lab (open-access). `DOMAIN_59_SOURCE_LIBRARY.md` (48 sources + 13 expert contacts with verified email addresses) present. CONFIRMED READY.

**Finding**: Zero API keys required. Zero proprietary database subscriptions required. Zero paywall access barriers for any launch action. Git write access to master branch and email client for outreach are the only technical requirements.

### Expert Contact Lists — Distribution-Ready by Domain

**Domain 56 (distribute May 26 – June 7)**:
- Partnership for Public Service (civil service reform flagship)
- AFGE, NTEU (federal employee unions — primary constituency)
- National Academy of Public Administration
- Brookings Governance Studies
- House Oversight Committee staff, Senate HSGAC staff (H.R. 492 window)

**Domain 57 (distribute August 10)**:
- HRW, Amnesty International USA (international law and human rights)
- CFR, Carnegie Endowment for International Peace
- NED, NDI, Freedom House (democracy assistance organizations)
- Senate Foreign Relations Committee staff
- Sierra Club, 350.org (UNFCCC withdrawal angle)

**Domain 58 (distribute June 15)**:
- NARF (peer review first; primary distribution contact)
- National Congress of American Indians
- First Nations Development Institute, National Indian Health Board
- Native Organizers Alliance
- Senate Indian Affairs Committee staff, ACLU Voting Rights Project

**Domain 59 (distribute June 1)**:
- League of Women Voters, Demos (electoral participation focus)
- EPI, NLIHC, CBPP (economic policy analysis)
- SEIU, Working Families Party (labor and working-class constituency)
- CIRCLE, Campus Vote Project, NextGen America (youth and civic engagement)
- 13 expert contacts with verified email addresses in `DOMAIN_59_SOURCE_LIBRARY.md`

**Contact sequencing gate**: Before any Phase 2 domain distribution email, verify the contact is not in `BATCH_1_CONTACT_LOG.md` as an unresponded Phase 1 Wave 1 target. The 72-hour Wave 1 Batch 1 reply window closes May 21. Run this check as part of the May 21 synthesis procedure.

### Obsidian Vault Structure

Phase 2 distribution tracking directories exist at `projects/resistance-research/phase-2-research/`:

```
projects/resistance-research/
├── phase-2-research/
│   ├── domain-56/
│   │   └── execution-log.md         (distribution wave tracking)
│   ├── domain-57/
│   │   └── library-access-log.md    (repurpose as distribution tracking; paywall concern resolved)
│   ├── domain-58/
│   │   └── rapid-response-log.md    (Trump v. Barbara rapid-response tracking — ACTIVATE NOW)
│   ├── domain-59/
│   │   └── source-confirmations.md  (URL verification record; 13 expert contacts staged)
│   └── coordination/
│       ├── daily-production-log.md  (repurpose as distribution tracking log)
│       └── cross-domain-bridge-status.md
```

Canonical domain files are in `domains/` (for 57–59) and root level (for 56). Distribution tracking logs are in `phase-2-research/`. These are separate directories — do not confuse tracking logs with canonical documents.

---

## Section 3: Research Execution Timeline Templates

*Distribution calendar only. Production writing is complete. Estimated time to review: 10 minutes.*

### Revised Effort Summary (Distribution Only)

| Domain | URL Spot-Check | Cover Email Prep | Wave 1 Execution | Rapid-Response | Wave 2 Execution | Total |
|--------|----------------|-----------------|-----------------|----------------|-----------------|-------|
| 56 | 2 hrs | 3–4 hrs | 1–2 hrs | — | 1–2 hrs | 7–10 hrs |
| 57 | 1–2 hrs | 2–3 hrs | 1–2 hrs | — (ICC check July) | 1–2 hrs | 5–9 hrs |
| 58 | 2–3 hrs | 1–2 hrs | 1–2 hrs | 3–4 hrs (Trump v. Barbara) | 1–2 hrs | 8–13 hrs |
| 59 | — (already staged) | 2–3 hrs | 1–2 hrs | 1 hr (HHS rule update if needed) | 1–2 hrs | 5–8 hrs |
| **Total** | | | | | | **25–40 hrs** |

Prior planning documents projected 120–130 hours. Actual remaining effort is 25–40 hours — an 80% reduction attributable to the domains being complete rather than requiring production.

### Publication Staging Timeline

| Domain | Document Status | First Distribution | Hard Policy Anchor |
|--------|----------------|-------------------|--------------------|
| 56 | COMPLETE | May 26 – June 7, 2026 | H.R. 492 legislative window (June 1–30) |
| 59 | COMPLETE | June 1, 2026 | HHS OBBBA interim final rule; CTC/RTC Senate Finance markup |
| 58 | COMPLETE | June 15, 2026 | Pre-Trump v. Barbara ruling; Montana SB 490 injunction |
| 57 | COMPLETE | August 10, 2026 | UNGA 81 High-Level Week (September 22–28, 2026) |

### Peer Review Status

**Domain 56**: Production-ready. No additional peer review required before distribution.

**Domain 57**: Document complete and YAML status "complete." No formal peer review required. ICC section currency check (July, 1–2 hours) is the only pre-distribution validation needed.

**Domain 58**: NARF peer review strongly recommended before June 15 distribution. Send request June 1–5; 5–7 business days async review; incorporate by June 14. This validates legal accuracy of the tribal voting rights and Callais analysis. It is not a production gap — the document is complete. It is a distribution credibility enhancement.

**Domain 59**: CBPP or EPI peer review on OBBBA compounding argument is recommended but not required for June 1 launch. Can follow in Wave 2 distribution (July–August).

### Parallel Execution Opportunities

Three windows allow simultaneous work across domains:

1. **May 22 – June 10**: Domain 56 URL spot-check and distribution prep (6–8 hours) runs simultaneously with Domain 58 NARF peer review coordination (schedule request and wait). Fully independent tasks.

2. **June 1 – June 14**: Domain 59 Wave 1 distribution (June 1–7) and Domain 58 peer review incorporation (June 7–14) overlap. Domain 59 distribution emails send; simultaneously NARF feedback is being incorporated into Domain 58 for June 15 launch.

3. **July – August**: Domain 57 pre-distribution ICC spot-check and staging (July, 3–4 hours) runs in parallel with Domain 58 post-Trump-v.-Barbara rapid-response update (if ruling issues). Both are short tasks — neither blocks the other.

---

## Section 4: Blocking Assumptions Audit

*Estimated time: 15 minutes. Review each domain's time-sensitive dependencies and confirm current status.*

### Domain 56 — No Blocking Assumptions

Domain 56 is complete and distribution-ready. The sole operational constraint is URL verification before distribution (addressed in Section 3, 2 hours).

**Monitoring (not blocking)**: PEER et al. v. Trump/OPM preliminary injunction ruling (expected Q3 2026). If issued before Domain 56 distribution, update the document with ruling outcome — this strengthens the domain, it does not complicate it.

**H.R. 492/S. 134 legislative window (June 1–30)**: Distribution accelerant. The domain does not require this window to be active; the window enhances distribution positioning. If the bill has advanced since May 20, note it in the cover email.

**Status on May 21**: No blocking assumption active. Two-hour URL spot-check is the only pre-distribution task.

---

### Domain 57 — One Soft Assumption (ICC Section Currency)

**SOFT ASSUMPTION — ICC section currency**: The ICC sanctions documentation (CICC "Criminalising Accountability" report, HRW ICC sanctions analysis) reflects conditions as of May 15, 2026. ICC sanctions are subject to ongoing diplomatic developments (Hungary ICC deadline June 2, 2026 is one active monitor item from the May 20 breaking developments scan). The January 7, 2026 Presidential Memorandum and 66-organization catalog are stable.

**Resolution**: Required before August 10 distribution, not before May 21 launch. The July pre-distribution spot-check (1–2 hours) is the action. If ICC developments between May 21 and August 10 are material, update the relevant section before distributing.

**August 10 UNGA hard constraint**: Structural, not strategic. Domain 57 must be distributed 43 days before UNGA 81 High-Level Week (September 22–28) to give Senate Foreign Relations Committee staff and international organizations adequate reading time. If distribution slips past August 10, the primary distribution anchor shifts to November 3 domestic midterm framing — still viable but loses the international constituency access.

**Status on May 21**: No blocking action required. Note the July ICC spot-check in working calendar.

---

### Domain 58 — One Hard Timing Constraint (Trump v. Barbara)

**HARD TIMING — Trump v. Barbara ruling**: The ruling (expected late June/early July 2026, argued April 1, 2026) will require a rapid-response update to Domain 58 Sections covering citizenship threat and the rapid-response protocol. The domain must be in pre-ruling distribution status by June 15 — sending the document to organizations before the ruling issues so the update arrives as a follow-up, not the primary send.

**Current status (May 21)**: Domain 58 is production-complete (11,388 words, 90 citations). The rapid-response protocol is pre-written in Section 9. The NARF peer review needs to be scheduled immediately (send request by June 1). The timeline is: peer review June 1–14, incorporate feedback June 14, launch June 15.

**Buffer calculation**: June 15 distribution to NARF, NCAI, and ACLU Voting Rights provides a minimum 1–2 week buffer before the earliest plausible ruling date. The pre-ruling distribution means organizations have the full document in hand before the ruling drops and will receive the rapid-response update as a high-relevance follow-up.

**Rapid-response protocol**: Pre-documented in Domain 58 Section 9. Expected update time: 2–3 hours after ruling is issued. Monitor: SCOTUSblog, sct.narf.org. Log updates in `phase-2-research/domain-58/rapid-response-log.md`.

**Status on May 21**: First check on this checklist. Has Trump v. Barbara issued before May 21? Check SCOTUSblog NOW before any other Domain 58 action. If ruled: execute rapid-response protocol from Section 9 before distribution.

---

### Domain 59 — One Conditional Policy Dependency (Non-Blocking)

**MONITORING — HHS OBBBA interim final rule (June 1, 2026)**: The rule is required by statute to be issued by June 1. Initial CMS guidance released December 2025. If the June 1 rule introduces material changes to work requirement implementation timelines or state notification requirements, Section 2 (Policy Leverage Windows) may need a one-paragraph update. This is a framing update, not a structural change. The causal backbone (Dallas Fed wp2517, Slee/Desmond, PNAS 2024) is unaffected by implementation guidance.

**Resolution**: Flag June 1 as monitoring date. Check HHS.gov on June 1 before sending Domain 59 distribution emails. If rule is materially significant, integrate into cover email language rather than rewriting the document.

**NOT BLOCKING**: The Georgetown CCF OBBBA URL confirmation noted in earlier checklists is resolved — the document is written with 49 confirmed URLs. No missing-source risk.

**NOT BLOCKING**: Mullainathan/Shafir library access concern is resolved — the document uses this framework without requiring library-gated chapter citations.

**Status on May 21**: No blocking assumption active. June 1 is both distribution launch date and HHS rule monitoring date. Calendar both.

---

### Cross-Domain Dependencies (All Domains)

**Domain 59 bridges to Domains 31, 47, 50**: Domain 59 is written. Before any cross-domain cover email references to these domains, confirm the cited claims are accurate against the canonical domain files. This is a 1-hour verification task before the first cross-domain outreach (not a blocking pre-launch requirement).

**Domain 57 bridges to Domains 23, 28**: Domain 57 constitutional asymmetry analysis and trade policy adjacency must not duplicate these domains when cross-referenced in cover emails or briefings. The cross-reference boundaries are documented in `PHASE_2_DOMAINS_56_59_RESEARCH_ACTIVATION_PREP.md` Section 2.3.

**Domain 58 bridges to Domain 37b (VRA enforcement)**: Before Domain 58 distribution, confirm the Domain 37b file is the canonical version and that the specific voting rights cross-references in Domain 58 point to accurate claims.

---

### Outcome-Specific Adjustments

**STRONG synthesis (QRP >= 2 AND response rate >= 40%, OR Score 5 override)**:
All four domains on standard distribution calendar. Domain 56 May 26 – June 7, Domain 59 June 1, Domain 58 June 15, Domain 57 August 10. Tier 2 activation begins June 15–21 using Wave 1 social proof.

**MODERATE synthesis (QRP >= 1 OR Gist delta > 10)**:
Same distribution calendar as STRONG. Tier 2 activation shifts 7–10 days to June 22–28.

**WEAK synthesis (QRP < 1 AND response rate < 20% AND Gist delta <= 5)**:
Domain 56, 58, and 59 distribution are path-independent — proceed on schedule regardless. Domain 57 August 10 proceeds. What changes: Tier 2 expansion defers until Domain 59 June 1 distribution produces a first engagement signal. The research corpus itself is unaffected — all four domains are complete. See `PHASE_2_CONTINGENCY_PLAYBOOK.md` for full WEAK path procedures.

**TOO EARLY (zero signals, no bounces)**:
Classify at May 25 rather than May 21. Domain production is complete and independent of classification. Domain 59 June 1 distribution proceeds regardless.

---

## Section 5: User Decision Requirements

*The following decisions must be made before any distribution email sends. None block the May 21 synthesis, but all must be confirmed before the first send.*

### Decision 1: Domain Sequencing

**Question**: Are domains distributing on the staggered schedule or simultaneously?

| Option | Schedule | Recommendation |
|--------|---------|----------------|
| A — Staggered (default) | D56: May 26–June 7 / D59: June 1 / D58: June 15 / D57: Aug 10 | Recommended. Aligns each domain with its natural policy anchor; avoids contact fatigue for organizations on multiple lists |
| B — Front-loaded | All four domains: June 1–7 to all contacts | Creates contact overlap risk; organizations on multiple lists receive 2–3 documents in one week |

**Required response**: Confirm Option A or override with Option B.

### Decision 2: Parallel vs. Sequential Execution (Phase 1 / Phase 2)

**Question**: Can Phase 2 distribution launch (Domains 56 and 59, May 26 – June 1) while Phase 1 distribution is still executing?

Phase 1 and Phase 2 contact lists have minimal overlap (Phase 2 targets policy specialists and advocacy organizations; Phase 1 targets academic, civic, and media networks). Parallel reduces setup overhead by approximately one day. Sequential delays Domain 59 by two weeks, potentially missing the HHS rule window.

**Recommendation**: Parallel (Option A). **Required response**: Confirm.

### Decision 3: Domain 58 Pre-Ruling Distribution

**Question**: Distribute Domain 58 June 15 (pre-ruling), or wait until Trump v. Barbara issues?

Pre-ruling distribution (Option A) sends the full document now and the rapid-response update as a high-relevance follow-up when the ruling drops. Post-ruling distribution (Option B) waits for the ruling, updates first, then sends. Option A produces stronger two-wave engagement; Option B simplifies sequencing.

**Recommendation**: Option A (pre-ruling June 15). **Required response**: Confirm.

### Decision 4: Hard Deadline Approval

**Question**: Does the user approve the following deadlines as binding calendar commitments?

| Domain | Hard Deadline | Reason |
|--------|--------------|--------|
| 56 | June 7 (Wave 1 complete) | H.R. 492 window first three weeks |
| 59 | June 1 (launch) | HHS interim final rule release |
| 58 | June 15 (Wave 1 launch) | Pre-Trump v. Barbara window |
| 58 | Within 24 hrs of Trump v. Barbara ruling | Rapid-response protocol |
| 57 | August 10 (Wave 1 launch) | UNGA 81 lead time (43 days) |

**Required response**: Confirm "yes" to these deadlines, or request modification, before first distribution email sends.

### Decision 5: Domain 60 Scope (STRONG Outcome Only)

If synthesis outcome is STRONG, confirm whether to scope Domain 60 in June 2026. Two candidates: (A) IEEPA/Trade Policy Economic Sovereignty — SCOTUS ruling February 2026 creates anchor; (B) consolidated disability rights — SSA 7,000-job cut + OBBBA disability population impact. Neither is required for Phase 2 launch.

**Required response (STRONG only)**: Confirm whether to scope Domain 60 in June.

---

## Section 6: 10-Item Pre-Launch Quick Check

*Run on May 21 evening, immediately after reading synthesis outcome in CHECKIN.md. 5-minute scan.*

- [ ] **1. All four canonical domain files confirmed at verified paths**
  - `domain-56-civil-service-politicization-governance.md` (root level — 6,267 words, 45 citations)
  - `domains/domain-57-multilateral-withdrawal-and-us-commitment-collapse.md` (9,201 words, 51 citations)
  - `domains/domain-58-tribal-sovereignty.md` (11,388 words, 90 citations) — not the old `domain-38-...` file
  - `domains/domain-59-economic-precarity-and-civic-participation.md` (8,450 words, 49 citations)

- [ ] **2. Synthesis outcome posted in CHECKIN.md** — STRONG / MODERATE / WEAK / TOO EARLY

- [ ] **3. Trump v. Barbara has NOT issued before May 21** — check SCOTUSblog first; if ruled, execute Domain 58 Section 9 rapid-response protocol before any distribution work

- [ ] **4. Phase 1 Batch 1 contact log checked** (`BATCH_1_CONTACT_LOG.md`) — verify no Phase 2 distribution contacts overlap with unresponded Phase 1 Wave 1 outreach

- [ ] **5. Domain 56 URL spot-check scheduled** — either complete by May 22 or explicitly calendared for May 21–22

- [ ] **6. Domain 57 ICC section currency check** — flagged in working calendar for July (before August 10 distribution)

- [ ] **7. Domain 58 canonical file confirmed** — `domains/domain-58-tribal-sovereignty.md` (not `domain-38-tribal-sovereignty-indigenous-democratic-design.md`)

- [ ] **8. NARF peer review request scheduled** — send by June 1–5 for June 15 distribution gate

- [ ] **9. Domain 59 June 1 and HHS rule release both flagged** in working calendar as the same monitoring date

- [ ] **10. User decisions confirmed** — Decisions 1–4 above confirmed before first distribution email sends

---

*Document produced: May 21, 2026. Audit basis: May 20 direct file verification of all four canonical domain files (word counts via wc -w, citation URL counts via grep -c "https://", section header extraction by direct read). Source data: DOMAIN_56_SOURCE_STAGING.md (May 15), DOMAIN_57_SOURCE_LIBRARY.md (May 17), DOMAIN_58_SOURCE_STAGING.md (May 15), DOMAIN_59_SOURCE_LIBRARY.md (May 17), DOMAINS_57_59_PRODUCTION_ROADMAP.md (May 15), phase-2-research-activation-checklist.md (authoritative May 20 version).*
