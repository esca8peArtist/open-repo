---
title: "Feedback Collection Template — Organizational Checklist and Metrics Dashboard"
project: cybersecurity-hardening
created: 2026-05-06
status: ready-for-use
use: Organizational self-assessment checklist + campaign metrics dashboard
companion:
  - post-distribution-impact-tracker.md (v3.0)
  - tier-1-feedback-collection-protocol.md
  - feedback-collection-template.csv
---

# Feedback Collection Template
## Organizational Implementation Checklist and Metrics Dashboard

**Purpose**: Two-part document. Part 1 is a checklist for organizations that have received the corpus and want to assess their own implementation. It is designed to be distributed directly to organizational contacts as a self-evaluation tool. Part 2 is the campaign operator's metrics dashboard — a structured view of the data that the CSV tracker accumulates, formatted for the 30/90/180-day assessment gates.

**Design principle**: Organizations do not implement security guidance because they are asked to fill out feedback forms. They implement because the guidance is useful and actionable. The checklist in Part 1 is designed to be genuinely useful to the organization — not just a reporting tool — so that completing it produces adoption behavior rather than just adoption data.

---

## Part 1: Organizational Implementation Checklist

*Intended for distribution to organizational contacts. Copy-paste the section below into an email or attach as a standalone document. The checklist works as both a self-evaluation and a feedback mechanism — ask the contact to return it completed or to reply noting which items they completed.*

---

### OpSec Corpus Implementation Checklist
**For: [Organization Name]**
**Date sent**: [Date]
**Corpus**: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108

This checklist helps your organization track which elements of the digital security corpus have been implemented for your staff and clients. It is also a feedback mechanism — returning it (even partially completed) tells us what is working and what needs to improve.

You do not need to complete every item. Mark what applies to your organization's capacity and client base. A single completed item is a meaningful start.

---

#### Block A: Staff Digital Security (Complete for all staff who work with at-risk clients)

These items protect your organization's own communications and devices from surveillance. They are the prerequisite for safely implementing guidance with clients.

- [ ] **A1** — At least one staff member has reviewed the corpus threat model section (Section I-II of the guide)
  - Who reviewed: _______________
  - Date reviewed: _______________

- [ ] **A2** — Staff use Signal for sensitive client communications (not SMS, not unencrypted email)
  - Approximate % of staff with Signal installed: ____%
  - Is Signal used for client intake? Yes / No / Sometimes

- [ ] **A3** — Staff email for sensitive correspondence uses end-to-end encryption (ProtonMail, Tutanota, or PGP)
  - Current setup: _______________
  - Barrier if not implemented: _______________

- [ ] **A4** — Staff devices use full-disk encryption and screen lock
  - Policy in place: Yes / No / Informal
  - Barrier if not: _______________

- [ ] **A5** — Staff have been advised against discussing sensitive client matters over unencrypted channels (phone calls, standard SMS, Gmail)
  - Training provided: Yes / No / Planned
  - Format (informal, written policy, training session): _______________

---

#### Block B: Client Data Broker Opt-Outs (Highest-priority, no technical expertise required)

These items reduce clients' exposure in commercial data broker databases that feed ICE's ELITE targeting system. This is Part 0 of the corpus — it requires no devices, no apps, and no technical skill. It is the single highest-leverage action for any client at risk of enforcement targeting.

- [ ] **B1** — At least one staff member has reviewed Part 0 of the corpus (data broker opt-out procedures)
  - Staff member: _______________

- [ ] **B2** — At least one client has been walked through the manual data broker opt-out process
  - Number of clients assisted to date: ___
  - Barriers encountered: _______________

- [ ] **B3** — For California-based clients with AB 60 driver's license: at least one client has been walked through the DELETE Act DROP platform enrollment (privacy.ca.gov/drop)
  - Number of DROP platform enrollments assisted: ___
  - Barrier if none: _______________
  - Note: Data brokers begin processing DROP deletions August 1, 2026. Enrollments before that date are legally valid but deletion will not process until after August 1.

- [ ] **B4** — Organization has added a data broker opt-out prompt or the DROP platform to its client intake form or intake interview
  - Added to intake: Yes / No / In progress
  - If in progress: anticipated date _______________

- [ ] **B5** — Clients have been advised on address masking (mail forwarding service, P.O. box, or organizational intermediary address) to reduce ELITE address confidence scores
  - Advice provided: Yes / No
  - Format (verbal, written handout, intake): _______________

---

#### Block C: Client Device and Communication Security

These items require more technical setup than Block B. Prioritize Block B first. Block C items are appropriate for clients at elevated risk (Tier 2 or Tier 3 in the corpus's threat tier structure).

- [ ] **C1** — Clients at elevated risk have been advised to install Signal and use it for communications with your organization
  - Client Signal adoption (rough estimate): ____%
  - Barrier if low: _______________

- [ ] **C2** — Client intake includes a question about device security (is the device shared? does anyone else have the PIN?)
  - Intake question added: Yes / No

- [ ] **C3** — Clients facing imminent enforcement risk have been advised about Tails OS (anonymous operating system) or device-clearing procedures
  - Staff familiar with Tails OS: Yes / No
  - Corpus section referenced: Implementation Guide, Section 5

- [ ] **C4** — Clients have been advised about the risk of location-sharing apps (Life360, Find My Friends, etc.) and social media check-ins
  - Advice provided: Yes / No / Informal

---

#### Block D: Organizational Integration

These items measure whether the corpus has been integrated into organizational practice beyond initial review.

- [ ] **D1** — The corpus has been shared with at least one other staff member beyond the initial recipient
  - Shared with: _______________

- [ ] **D2** — The corpus or a summary of its recommendations has been added to the organization's resource library or intranet
  - Location: _______________

- [ ] **D3** — The corpus has been referenced in any staff training, onboarding, or professional development
  - Event name/date: _______________
  - Format (formal training / informal discussion): _______________

- [ ] **D4** — The organization has shared the corpus with a partner organization or network
  - Partner(s): _______________

- [ ] **D5** — The organization has cited or linked to the corpus in any published output (newsletter, website, report, legal brief)
  - Publication/URL: _______________

---

#### Block E: Feedback and Gaps

This section is the most important part of the checklist. These responses directly determine what the next version of the corpus covers.

**E1 — Which section was most useful for your organization's work?**
- [ ] Threat model documentation (ELITE system, Palantir contracts)
- [ ] Part 0 (data broker opt-outs — no tech required)
- [ ] California DROP platform pathway (AB 60 → DELETE Act)
- [ ] Device hardening guide (Signal, encrypted storage, Tails)
- [ ] Threat tier structure (Tier 1 / 2 / 3 graduated guidance)
- [ ] Sourcing and citations (FOIA disclosures, government contracts)
- [ ] Haven't gotten to it yet

**E2 — What is the biggest gap in the corpus for your organization's clients?**

*Please describe a client situation or scenario that the corpus does not address. One sentence is enough.*

_______________________________________________________________________________

**E3 — What was the biggest barrier to using or sharing the corpus?**
- [ ] Too long to share directly with clients
- [ ] Need a Spanish-language version of Part 0
- [ ] Gist URL is difficult to share internally (need a PDF)
- [ ] Sourcing needs peer review before our organization can cite it publicly
- [ ] Staff capacity — couldn't prioritize
- [ ] Clients don't have smartphones / laptops (hardware barrier)
- [ ] Not the right fit for our work
- [ ] Other: _______________

**E4 — Does the threat model description of ELITE match what you observe in your clients' cases?**
- [ ] Yes — the data broker pipeline and address scoring mechanism matches what we see
- [ ] Partially — some aspects match, but there are additional threat vectors we've observed
- [ ] Unclear — we don't have visibility into how ICE locates our clients
- [ ] No — the guide describes risks that don't match our clients' experience

If partially or no: *What threat vector have you observed that the guide doesn't cover?*

_______________________________________________________________________________

**E5 — Is there anyone else who should have this corpus?**

*Organization name or type is fine. This is the most valuable piece of feedback you can provide.*

_______________________________________________________________________________

**E6 — Would your organization be comfortable being referenced (anonymously) in communications about this corpus's impact?**
- [ ] Yes — reference by organization type only (e.g., "an immigration legal aid organization")
- [ ] Yes — reference by name
- [ ] No — please keep all references anonymous

---

*Return this checklist to: [feedback email or Signal number]*
*Or call/Signal: [number]*
*Your responses shape the next version of the corpus and help us understand what's working for organizations like yours.*

---

## Part 2: Campaign Operator Metrics Dashboard

*For internal use by the campaign operator. Complete at each assessment gate using data from the CSV tracker, Gist traffic logs, and feedback responses.*

---

### Dashboard Version: [Date] (Day 30 / Day 90 / Day 180 / Day 365 — circle one)

---

### Module 1: Distribution Status

| Cohort | Total in List | Sent | Pending | Percent Sent |
|--------|--------------|------|---------|--------------|
| Cohort A — direct-service (12) | 12 | | | |
| Cohort B — amplifier (33) | 33 | | | |
| **Total** | **45** | | | |

**Sends pending explanation** (if any): _______________

---

### Module 2: Engagement Snapshot

| Cohort | Stage 0 (no reply) | Stage 1 (ack'd) | Stage 2 (reviewed) | Stage 3+ (adopted) | Reply Rate |
|--------|-------------------|-----------------|-------------------|-------------------|------------|
| Cohort A | | | | | |
| Cohort B | | | | | |
| **Total** | | | | | |

**Stage 3+ organizations (list each):**

| Organization | Cohort | Sector | Adoption Action Taken | Date | Attribution Confidence |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |

---

### Module 3: Referral Network

| Metric | Count | Notes |
|--------|-------|-------|
| Total referral contacts generated (Question 3 responses) | | |
| New warm contacts added to Tier 2 list | | |
| Referral factor (new contacts / initial sends) | | Target: ≥1.5 at Day 90 |
| Unprompted secondary distributions observed | | (corpus forwarded without being asked) |

**Top referring organizations** (by number of referrals generated):
1. _______________  — ___ referrals
2. _______________  — ___ referrals
3. _______________  — ___ referrals

---

### Module 4: Content Feedback Aggregation

Complete after collecting 30-day and 90-day follow-up responses.

**Most useful section** (count responses per section):

| Section | Count |
|---------|-------|
| Threat model / ELITE documentation | |
| Part 0 — data broker opt-outs | |
| California DROP platform pathway | |
| Device hardening guide | |
| Threat tier structure | |
| Sourcing and citations | |
| No response / haven't reviewed | |

**Gaps identified** (log each unique gap with count of organizations citing it):

| Gap Description | Organizations Citing | Category (a/b/c/d) | Required Before Tier 2? |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

*Category key: (a) wording fix, (b) missing section, (c) wrong threat model, (d) framing not landing*

**Barriers identified** (log each unique barrier with count):

| Barrier | Count | Fix Required |
|---------|-------|-------------|
| | | |
| | | |
| | | |

---

### Module 5: Threat Model Accuracy

| Assessment | Count | Organizations (type) |
|------------|-------|----------------------|
| Confirmed accurate | | |
| Partially accurate | | |
| Not accurate (specify below) | | |
| Insufficient visibility to assess | | |

**Inaccuracies noted** (for any "not accurate" response, log specifics):

_______________________________________________________________________________

**Category (c) determination**: Is any inaccuracy confirmed by primary source documentation?
- [ ] No confirmed inaccuracy — proceed per standard timeline
- [ ] Confirmed inaccuracy — HOLD Tier 2 until threat model updated

---

### Module 6: Passive Monitoring

| Signal | Date | Value | Notes |
|--------|------|-------|-------|
| Gist view count | | | |
| Gist view delta since last check | | | |
| Top referrer source | | | |
| Social media mentions | | | |
| Google Alert hits | | | |
| Overton.io results (quarterly) | | | |
| Google Scholar alerts | | | |
| CourtListener / PACER results | | | |
| GitHub Gist stars (if migrated to repo) | | | |
| GitHub forks (if migrated to repo) | | | |

---

### Module 7: Implementation Checklist Return Data

Summary of returned Block E feedback across all organizations that returned the organizational checklist.

| Item | Responses Received | Most Common Answer | Phase 2 Implication |
|------|-------------------|-------------------|---------------------|
| E1 — Most useful section | | | |
| E2 — Biggest gap | | | |
| E3 — Biggest barrier | | | |
| E4 — Threat model accuracy | | | |
| E5 — Referral (who else should have this) | | | |
| E6 — Citation permission | | | |

---

### Module 8: Assessment Gate Status

Complete at each gate date.

#### Day 90 Gate Assessment (from Section 3.2 of post-distribution-impact-tracker.md)

| Gate | Criterion | Status | Notes |
|------|-----------|--------|-------|
| Gate 1 — Distribution | ≥28 of 45 contacted | PASS / FAIL / PARTIAL | |
| Gate 2 — Engagement | Reply rate and Stage 1+ threshold | PASS / FAIL / PARTIAL | |
| Gate 3 — Adoption signals | ≥3 of 6 signals present | PASS / FAIL / PARTIAL | |
| Gate 4 — Feedback quality | ≥6 structured responses | PASS / FAIL / PARTIAL | |
| Gate 5 — Threat model integrity | No confirmed Category (c) | PASS / FAIL / HOLD | |

**Overall Day 90 decision**: Proceed to Tier 2 / Conditional hold / Hold

**Rationale**: _______________

---

#### Day 180 Gate Assessment (from Section 4.2 of post-distribution-impact-tracker.md)

| Criterion | Target | Actual | Status |
|-----------|--------|--------|--------|
| Organizations at Stage 3+ | ≥5 of 45 | | PASS / FAIL |
| Organizations at Stage 4+ | ≥1 | | PASS / FAIL |
| External citations | ≥1 | | PASS / FAIL |
| Case study interview | ≥1 completed | | PASS / FAIL |
| Sector coverage at Stage 3+ | ≥3 sectors | | PASS / FAIL |

**Overall Day 180 decision**: Proceed to Tier 3 / Conditional hold / Hold

**Rationale**: _______________

---

#### Day 365 Indicators (from Section 5.2 of post-distribution-impact-tracker.md)

| Indicator | Level (Strong / Moderate / Weak) | Evidence |
|-----------|--------------------------------|---------|
| Organic diffusion (Gist trajectory) | | |
| Attribution-confirmed citations | | |
| Academic or policy citation | | |
| Stage 4+ (sustained) organizations | | |
| Stage 5 (multiplier) organizations | | |
| DROP platform effectiveness confirmed | | |
| Near-miss narratives received | | |

**12-month strategic decision**: Replicate / Partial pivot / Full pivot

**Primary evidence for decision**: _______________

---

### Module 9: Near-Miss Narrative Log

| Date | Channel | Segment | Countermeasure Referenced | Outcome Described | Attribution Confidence |
|------|---------|---------|--------------------------|------------------|----------------------|
| | | | | | |
| | | | | | |
| | | | | | |

*Reminder: Do not include any information that could identify a specific undocumented individual. Log at the level of "undocumented client in California completed DROP enrollment and attorney reported no ICE home visit in following 90 days." Do not log address, name, case number, or any detail beyond what is needed for the attribution assessment.*

---

### Module 10: Corpus Revision Log

Track all changes made to the corpus in response to feedback. This log is evidence of active iteration and is a credibility signal for Tier 2/3 framing ("the corpus has been updated based on practitioner feedback").

| Date | Version | Change Made | Triggered By | Category (a/b/c/d) | Applied Before Tier 2? |
|------|---------|------------|-------------|-------------------|----------------------|
| | | | | | |
| | | | | | |
| | | | | | |

**Revision cadence target**: At least one revision every 90 days (quarterly review cycle). Tool installation steps (Signal, Tails, DROP platform) are the highest-frequency revision candidates — these change with software updates.

---

### Quick Reference: Success Definitions

Use this reference when assessing whether any given organizational contact or campaign milestone counts as success.

**"A contact has adopted"** means: they took at least one action that required a decision to use this specific corpus (not general security guidance). See Section 1.1 of `post-distribution-impact-tracker.md` for the full criteria.

**"The corpus is effective"** means: at least one individual implemented a countermeasure that reduced a specific documented attack surface (ELITE address data, SIGINT collection, device seizure risk). Attack surface reduction is the proxy for effectiveness. Incident non-occurrence is not measurable and should not be claimed.

**"The campaign is succeeding"** means: Referral factor ≥ 1.5 AND at least one Stage 3+ adoption per cohort AND feedback is actionable enough to drive corpus revision.

**"Tier 2 is ready to launch"** means: All 5 Day 90 gates pass (or 4 of 5 with a documented conditional). Social proof is present from at least one identified adopter. At least two corpus revisions reflect practitioner feedback. No unresolved Category (c) threat model concerns.

**"Tier 3 is ready to launch"** means: Day 180 criteria met, including sector coverage. Tier 2 results (if available) show engagement at or above Tier 1 benchmarks. The corpus framing for Tier 3 audiences (broader public, policymakers) has been updated to reflect Tier 1/2 social proof.

---

*Template complete. Part 1 (Organizational Checklist) is ready to attach to any follow-up email to organizational contacts. Customize Block headers to match the organization type (legal aid organizations need Block B emphasized; mutual aid networks need Blocks A and C; researcher organizations need Block E). Part 2 (Metrics Dashboard) should be completed at each 30/90/180/365-day assessment gate by copying this template to a date-stamped file and populating the modules from the CSV tracker data.*

*Cross-reference: `post-distribution-impact-tracker.md` (v3.0) for assessment gate definitions and decision logic. `feedback-collection-template.csv` for the per-organization data entry. `tier-1-effectiveness-framework.md` for the Go/No-Go decision tree and failure mode taxonomy.*

*Last updated: 2026-05-06*
