---
title: "Cybersecurity Hardening: OpSec Against Government Surveillance"
project: cybersecurity-hardening
updated: 2026-04-28
status: publication-ready
---

# Cybersecurity Hardening: OpSec Against Government Surveillance

This directory contains a complete corpus of threat-grounded security guidance for people facing government-level surveillance in the United States. All recommendations are sourced to confirmed government contracts, primary technical documentation, and verified legal analysis. See individual files for full citations.

---

## Core Reference Documents

These three documents form the primary corpus and should be read in sequence:

| File | Purpose | Audience |
|------|---------|----------|
| [threat-model.md](threat-model.md) | Confirmed government surveillance capabilities (Palantir, NSA, FBI, data brokers, DOGE) with primary-source citations | All |
| [opsec-playbook.md](opsec-playbook.md) | Countermeasures mapped directly to confirmed threat capabilities, organized by tier (1–3) | All |
| [implementation-guide.md](implementation-guide.md) | Step-by-step setup instructions for every countermeasure, with verification checkpoints | All |
| [device-hardening-guide.md](device-hardening-guide.md) | Deep technical guide to iOS and Android hardening against forensic extraction | Tier 2–3 |
| [palantir-threat-model.md](palantir-threat-model.md) | Palantir-specific: architecture, confirmed federal contracts, what it knows about U.S. persons | All |

---

## Profile-Specific Implementation Guides

These four guides distill the full corpus into actionable timelines for specific threat profiles. Start here if you know your profile. Each guide is 1,000–1,500 words and follows a Week 1 / Month 1 / Month 3 implementation timeline.

| Guide | Threat Model Focus | Tier |
|-------|-------------------|------|
| [journalist-implementation-guide.md](journalist-implementation-guide.md) | Source protection, device security, border crossing, confidential document receipt | 1–3 |
| [immigration-attorney-implementation-guide.md](immigration-attorney-implementation-guide.md) | Client communication confidentiality, government surveillance (ICE/CBP), case file protection | 1–2 |
| [undocumented-immigrant-implementation-guide.md](undocumented-immigrant-implementation-guide.md) | ICE detection/deportation (ELITE/ImmigrationOS), identity compartmentalization, data broker opt-outs | 2 |
| [activist-implementation-guide.md](activist-implementation-guide.md) | Government surveillance, location tracking, protest security, group communications | 2 |

---

## Supporting and Distribution Documents

| File | Purpose |
|------|---------|
| [high-risk-populations.md](high-risk-populations.md) | Population-specific risk analysis |
| [publication-prep.md](publication-prep.md) | Executive summary, full table of contents, 40-term glossary |
| [PUBLICATION_README.md](PUBLICATION_README.md) | Publishing instructions (GitHub Gist, MkDocs, PDF, SecureDrop) |
| [DISTRIBUTION_CHECKLIST.md](DISTRIBUTION_CHECKLIST.md) | Pre-distribution checklist |
| [TIER1_DISTRIBUTION_PREP.md](TIER1_DISTRIBUTION_PREP.md) | Distribution prep for Tier 1 (journalists, advocates) |
| [TIER2_DISTRIBUTION_PREP.md](TIER2_DISTRIBUTION_PREP.md) | Distribution prep for Tier 2 (activists, organizers) |
| [TIER3_DISTRIBUTION_PREP.md](TIER3_DISTRIBUTION_PREP.md) | Distribution prep for Tier 3 (direct investigation targets) |

---

## Tier Reference

The corpus uses three tiers, defined in `opsec-playbook.md`:

- **Tier 1** — Journalists, immigration advocates, healthcare workers who serve undocumented people, labor organizers. Primary threat: administrative data pipelines and OSINT aggregation.
- **Tier 2** — Activists, civil rights litigants, protest organizers, people with immigration status vulnerability. Primary threat: IMSI catchers, device seizure, social media surveillance, Palantir ELITE targeting.
- **Tier 3** — People with reason to believe they are direct targets of active investigation. Primary threat: advanced persistent access, forensic device extraction, targeted spyware.

The profile-specific guides each map to a tier. If your situation has escalated from one tier to another, supplement your guide with the tier-appropriate sections of `opsec-playbook.md`.

---

## Key Findings (Lead With These)

1. **Palantir ELITE** generates per-person address confidence scores (0–100) using IRS records, Medicaid data, DMV files, utility bills, and commercial broker data. Opt-outs from commercial brokers degrade these scores. See `implementation-guide.md` Part 0 for opt-out procedures.

2. **Signal content is a genuine capability gap** in Palantir's surveillance infrastructure. A subpoena to Signal returns only account creation date and last connection time. This has been confirmed via grand jury subpoena. Signal content with disappearing messages enabled is the most robust available protection for communication content.

3. **iCloud without Advanced Data Protection enabled** is the most productive legal process target for iPhone users. Apple provides iCloud content under a search warrant if ADP is not enabled. Enabling ADP takes 5 minutes and closes this attack surface.

4. **Smartphone advertising SDKs** harvest GPS location and sell it to ICE via commercial brokers without a warrant. Deleting your advertising ID and auditing app location permissions is the most accessible action to reduce this exposure.

5. **GrapheneOS on Google Pixel** has been confirmed as resistant to forensic extraction tools (Cellebrite UFED) in a leaked Cellebrite support matrix. For Tier 2–3 users, it is the strongest available Android platform.

---

## Currency

This corpus reflects the surveillance landscape as of **April 2026**. Key items to reassess quarterly:
- Palantir contract renewals and expansions (check USASpending.gov)
- Section 702 reauthorization status
- DOGE cross-agency database litigation outcomes (15+ active lawsuits as of April 2026)
- GrapheneOS supported device list (grapheneos.org/faq)
- SECURE Data Act (HR 8413) progress — would preempt California DROP platform if enacted
