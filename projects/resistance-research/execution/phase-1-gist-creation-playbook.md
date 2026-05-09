---
title: "Phase 1 Gist Creation Playbook"
created: 2026-05-09
session: Item-41
status: ready-to-execute
purpose: "Path-specific Gist creation procedures for all three distribution paths. Execute after selecting path in phase-1-path-decision-template.md."
reference_urls:
  main_gist: "https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261"
  exec_summary: "https://gist.github.com/esca8peArtist/2869da6eaeb15a47246ade3bbbc4a3f4"
  litigation_tracker: "https://gist.github.com/esca8peArtist/418d51bda087f15a04d685ab171a5ee0"
  first_amendment: "https://gist.github.com/esca8peArtist/10d0a86e386e6c3c11c3830295a6503c"
  environmental: "https://gist.github.com/esca8peArtist/87e2bdb931b77480e56a08044c567bc4"
  police_decrees: "https://gist.github.com/esca8peArtist/1f5cb28527c98d12526c14302c725731"
---

# Phase 1 Gist Creation Playbook

**Purpose**: Exact step-by-step Gist creation procedure, organized by distribution path. After completing the 7-step setup checklist, follow your path's section here.

**Pre-condition**: You have confirmed the 6 canonical Gists from `DISTRIBUTION_GIST_URLS.md` are live (Step 3 of the setup checklist). You are logged in to GitHub as esca8peArtist.

---

## What Each Path Requires

| Path | New Gists to Create | Existing Gists Used | Total Gist Count |
|------|--------------------|--------------------|-----------------|
| A | Domain 42 Gist (1 new) | All 6 existing | 7 |
| A+37 | Domain 42 Gist (1 new) | All 6 existing | 7 |
| B | Domain 42 Gist + 6-8 cluster Gists (7-9 new) | Full proposal Gist (existing) | 13-15 |

**Critical note on Path A and A+37**: The main proposal Gist (https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261) already exists and is the primary send artifact. For Paths A and A+37, you do not rebuild this — you link to it. The only new Gist required is Domain 42.

---

## Section 1: Domain 42 Gist (Required for All Three Paths)

This Gist is required regardless of which path you choose. Create it first.

**Source file**: `projects/resistance-research/domains/domain-42-drug-policy-democratic-legitimacy-regulatory-capture.md` (55 KB, current as of May 7, 2026)

**Full step-by-step procedure**: `execution/domain-42-gist-creation-steps.md` (this playbook was created before that detailed guide; follow the dedicated guide for Domain 42 — it has the exact Zone A/B/D block text to paste)

**Summary**:
1. Navigate to https://gist.github.com/new
2. Filename: `domain-42-drug-policy-democratic-legitimacy-regulatory-capture-2026.md`
3. Description: `Domain 42 — Drug Policy, Regulatory Capture, and Democratic Legitimacy | Democratic Renewal Research Framework | DEA Hearing DEA-1362 deadline May 28, 2026`
4. Paste Zone A header + Zone B context block (from `domain-42-gist-creation-steps.md` Steps 3-4)
5. Paste full domain-42 file content
6. Paste Zone D footer block (from `domain-42-gist-creation-steps.md` Step 6)
7. Set to Public, click Create
8. Copy URL and add to `DISTRIBUTION_GIST_URLS.md`
9. Replace `[GIST URL — fill when created...]` in `domain-42-email-template.md` (5 instances)

**Estimated time**: 10 minutes

**Record URL here**: `https://gist.github.com/esca8peArtist/` ________________

---

## Section 2: Path A — Single Consolidated Gist Verification

For Path A, you do not create new distribution Gists beyond Domain 42. The main proposal Gist is already live.

**All six canonical Gists are your send infrastructure**:

| # | Document | URL | Role |
|---|----------|-----|------|
| 1 | Democratic Renewal Proposal (35 domains) | https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261 | Primary send artifact (all Tier 1 emails) |
| 2 | Executive Summary | https://gist.github.com/esca8peArtist/2869da6eaeb15a47246ade3bbbc4a3f4 | Send to contacts who prefer brief overviews |
| 3 | Litigation Tracker 2026 | https://gist.github.com/esca8peArtist/418d51bda087f15a04d685ab171a5ee0 | Include in legal/academic outreach |
| 4 | First Amendment Suppression Tracker | https://gist.github.com/esca8peArtist/10d0a86e386e6c3c11c3830295a6503c | Include in civil liberties and press freedom outreach |
| 5 | Environmental Rollbacks Tracker | https://gist.github.com/esca8peArtist/87e2bdb931b77480e56a08044c567bc4 | Include in environmental/climate organization outreach |
| 6 | Police Consent Decree Tracker | https://gist.github.com/esca8peArtist/1f5cb28527c98d12526c14302c725731 | Include in civil rights and policing reform outreach |
| 7 | Domain 42 (Drug Policy / DEA) | [create per Section 1 above] | Include in drug policy sub-batch emails |

### Path A Template Placeholder Fill Procedure

After confirming Domain 42 Gist URL, fill placeholders across all template files:

**In `execution/outreach-email-templates.md`**:
- Replace `{{GIST_URL}}` with: https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261
- Replace `{{EXEC_SUMMARY_URL}}` with: https://gist.github.com/esca8peArtist/2869da6eaeb15a47246ade3bbbc4a3f4
- Replace `{{LITIGATION_URL}}` with: https://gist.github.com/esca8peArtist/418d51bda087f15a04d685ab171a5ee0
- Replace `{{YOUR_NAME}}` with your name
- Replace `{{YOUR_CONTACT_INFO}}` with your contact information

**In `distribution-institutional-outreach-templates.md`**:
- Replace `[link]` with appropriate Gist URL per section (main proposal for most; tracker-specific for legal/environmental/civil rights sections)
- Replace `[Your name]` and `[Contact information]`

**In `distribution-substack-drafts.md`**:
- Replace `[link]` with main proposal Gist URL for all proposal references
- Replace tracker-specific `[link]` instances with the corresponding tracker Gist

**In `distribution-reddit-templates.md`**:
- Replace `[link]` instances with appropriate Gist URLs per subreddit context (r/law gets litigation tracker; r/environment gets environmental tracker; r/USPolitics gets main proposal)

**Estimated time for placeholder fill**: 20 minutes

---

## Section 3: Path A+37 — Two-Wave Gist Structure

Path A+37 uses the same Gists as Path A, plus one additional step: preparing the Domain 37 outreach for Phase 1b.

### Phase 1a Gists (identical to Path A)

Same 7 Gists as Path A. Same placeholder fill procedure.

### Phase 1b: Domain 37 Targeted Outreach

For Phase 1b, you do NOT create a new Domain 37 Gist (unless you want a standalone one). Domain 37 is already in the main proposal Gist. Instead:

**Option 1 (Recommended)**: Reference the main proposal Gist in Phase 1b emails, with a direct anchor link to Domain 37 content. The main Gist URL + a note to "see Domain 37 — Federal Executive Interference in 2026 Midterms" is sufficient.

**Option 2**: Create a standalone Domain 37 Gist for contacts who want to share it independently.

If you choose Option 2, follow this structure:

**Standalone Domain 37 Gist**:
- Source file: `domains/domain-37-federal-executive-interference-2026-midterms.md` (89 KB)
- Filename: `domain-37-federal-executive-interference-2026-midterms.md`
- Description: `Domain 37 — Federal Executive Interference in 2026 Midterms | Democratic Renewal Framework | Election Protection Resource — 2026 cycle`
- Zone A header: same structure as Domain 42 Zone A (from `domain-42-gist-creation-steps.md`) but substituting Domain 37 details
- Zone B context block:
  ```
  **Domain**: 37 — Federal Executive Interference in 2026 Midterms
  **Framework domains total**: 43 (as of May 2026)
  **Advocacy windows**:
    - May 30, 2026: DOJ consent decree active enforcement deadline (Domain 37 Section 6)
    - August 7, 2026: NVRA voter registration quiet period begins (90 days before November 4, 2026 general election)
    - September–November 2026: Certification season (53 election deniers in certification-authority positions)
  **Cross-reference domains**: Domain 1 (Voting Rights), Domain 6 (Judicial Independence), Domain 33 (State Legislative Autocratization), Domain 37b (State Election Security)
  **Baseline metrics document**: domain-37-baseline-metrics.md
  ```
- Zone D footer: same standard footer as Domain 42 Zone D (from `domain-42-gist-creation-steps.md`)

**Estimated time**: 10 minutes for Option 1 (no new Gist); 15 minutes for Option 2 (new Domain 37 Gist)

### Phase 1b Template Placeholders

Phase 1b uses targeted email templates from `DOMAIN_37_SEQUENCING_PLAN.md`. Fill the same identity placeholders (`{{YOUR_NAME}}`, `{{YOUR_CONTACT_INFO}}`) plus the Domain 37 Gist URL if you created Option 2.

---

## Section 4: Path B — Multi-Gist Cluster Structure

Path B requires creating 6-8 new cluster Gists. This is the most Gist-creation-intensive path.

**Estimated time**: 90 minutes for 8 Gists (10-12 minutes per Gist including rendering verification)

### Cluster Gist Plan

Each cluster is a standalone Gist that can be shared independently. Create them in this order (Cluster 1 first — it's the most time-sensitive for election orgs):

---

**Cluster 1: Voting and Election Security**

- Domains: Domain 01 (Voting Rights), Domain 33 (State Legislative Autocratization), Domain 37 (Federal Executive Interference), Domain 37b (State Election Security), Domain E (Election Administration Seizure)
- Gist filename: `cluster-1-voting-election-security-2026.md`
- Gist description: `Cluster 1: Voting Rights, State Autocratization, and Election Security | Democratic Renewal Framework 2026`
- Structure: README (cluster overview + links to other clusters) followed by each domain in sequence, separated by `---` dividers
- Send to: Election protection organizations, voting rights litigators, state election officials, Common Cause, EAC contacts
- Estimated Gist size: ~300-350 KB

**Cluster 2: Law Enforcement and Criminal Justice**

- Domains: Domain 06 (Judicial Independence), Domain 20 (Corruption and Accountability), Domain 29 (Prosecutorial Weaponization), Domain 42 (Drug Policy / DEA)
- Gist filename: `cluster-2-law-enforcement-criminal-justice-2026.md`
- Gist description: `Cluster 2: Judicial Independence, DOJ Capture, Prosecutorial Weaponization, Drug Policy | Democratic Renewal Framework 2026`
- Send to: ACLU Criminal Law Reform, NAACP Legal Defense Fund, SPLC, law school clinical programs, civil rights litigators

**Cluster 3: Media, Epistemic Infrastructure, and AI**

- Domains: Domain 43 (Epistemic Infrastructure / Disinformation), Domain 36 (AI Governance), Domain F (Civil Society Suppression), domain-information-access-recovery.md, domain-media-freedom-recovery.md
- Gist filename: `cluster-3-media-epistemic-ai-2026.md`
- Gist description: `Cluster 3: Media Freedom, Epistemic Infrastructure, Disinformation, AI Governance | Democratic Renewal Framework 2026`
- Send to: Press freedom organizations, journalism school faculty, digital rights orgs, AI policy researchers, EFF

**Cluster 4: Institutional Integrity and Civil Service**

- Domains: Domain 26 (Government Accountability), Domain 27 (Higher Education), domain-civil-service-resilience.md, domain-legislative-branch-capacity.md, Domain 34 (Congressional Power of the Purse)
- Gist filename: `cluster-4-institutional-integrity-civil-service-2026.md`
- Gist description: `Cluster 4: Government Accountability, Civil Service Resilience, Congressional Authority | Democratic Renewal Framework 2026`
- Send to: Public sector union officials, civil service reform advocates, AFGE, congressional staff networks, public administration faculty

**Cluster 5: Foreign Policy, Trade, and War Powers**

- Domains: Domain 19f (War Powers Reform), Domain 23 (Trade Policy / Tariff Unilateralism), Domain 28 (War Powers Venezuela), Domain 25 (FISA 702), domain-foreign-interference-in-democratic-institutions.md
- Gist filename: `cluster-5-foreign-policy-war-powers-trade-2026.md`
- Gist description: `Cluster 5: War Powers, Trade Unilateralism, Foreign Interference, FISA | Democratic Renewal Framework 2026`
- Send to: National security law scholars, Just Security, foreign policy think tanks, Brookings governance studies, EPI trade policy team

**Cluster 6: Healthcare, Labor, and Economic Democracy**

- Domains: Domain 31 (Healthcare / OBBBA), Domain 31x (Healthcare Tariff Collision), Domain B (Healthcare Access), Domain 38 (Financial Sector), Domain 39 (Immigration Enforcement), Domain 41b (Disability Rights)
- Gist filename: `cluster-6-healthcare-labor-economic-2026.md`
- Gist description: `Cluster 6: Healthcare Access, Labor Rights, Economic Democracy, Immigration | Democratic Renewal Framework 2026`
- Send to: AFL-CIO, SEIU, UFW, EPI, faith-based social justice networks, NILC, RAICES, disability rights orgs

**Cluster 7: Recovery Architecture and Implementation**

- Domains: domain-implementation-roadmap.md, domain-judicial-independence-recovery.md, domain-legislative-branch-capacity.md, Domain 35 (SCOTUS OT2026), Domain 38a (FISA Intel Oversight Reform)
- Gist filename: `cluster-7-recovery-architecture-implementation-2026.md`
- Gist description: `Cluster 7: Democratic Recovery Architecture, Implementation Roadmap, Judicial Independence Recovery | Democratic Renewal Framework 2026`
- Send to: Reform-minded law school deans, Democratic caucus policy staff, foundations focused on democracy infrastructure

### Gist Creation Procedure for Each Cluster

Each cluster Gist follows the same 4-block structure:

**Block 1: Cluster README header** (write fresh for each cluster, ~300-500 words):
```
# Cluster [N]: [Title]

**Part of**: The Democratic Renewal Research Framework (43 domains, May 2026)
**Full framework**: [main proposal Gist URL]

## This Cluster

[2-3 sentence description of what this cluster covers and why these domains are grouped]

## Domains in This Cluster

- **Domain [X]**: [Brief title and one-sentence description]
- [repeat for each domain in cluster]

## Related Clusters

- Cluster 1 (Voting and Election Security): [URL when available]
- [list other clusters with URLs as they are created]

## About This Framework

[3-4 sentence overview of the 43-domain framework, CC 4.0 license notice, contact info placeholder]
```

**Block 2**: Standard Zone A header (from `domain-42-gist-creation-steps.md`)

**Block 3**: Domain content, each domain separated by `---` and a clear H2 heading

**Block 4**: Standard Zone D footer (from `domain-42-gist-creation-steps.md`)

### URL Recording Table for Path B

Fill as each Gist is created:

| Cluster | Gist URL |
|---------|----------|
| Cluster 1 (Voting) | https://gist.github.com/esca8peArtist/ ________________ |
| Cluster 2 (Law Enforcement) | https://gist.github.com/esca8peArtist/ ________________ |
| Cluster 3 (Media/AI) | https://gist.github.com/esca8peArtist/ ________________ |
| Cluster 4 (Institutional) | https://gist.github.com/esca8peArtist/ ________________ |
| Cluster 5 (Foreign Policy) | https://gist.github.com/esca8peArtist/ ________________ |
| Cluster 6 (Healthcare/Labor) | https://gist.github.com/esca8peArtist/ ________________ |
| Cluster 7 (Recovery) | https://gist.github.com/esca8peArtist/ ________________ |
| Domain 42 | https://gist.github.com/esca8peArtist/ ________________ |

After creating all clusters, add all URLs to `DISTRIBUTION_GIST_URLS.md` and update the cross-links in each cluster README.

---

## Post-Creation Verification (All Paths)

After creating any new Gist, verify:

- [ ] Gist URL loads in browser without authentication
- [ ] Markdown renders correctly (H1 headings display as headings, not raw `#` symbols; tables display with borders; code blocks display with gray background)
- [ ] Zone A header block renders as a formatted metadata section at the top
- [ ] Zone D footer renders after the Sources section at the bottom
- [ ] The main framework Gist URL in the footer (https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261) is correct
- [ ] URL recorded in `DISTRIBUTION_GIST_URLS.md`

**If Markdown does not render**: Confirm the Gist filename ends in `.md` (not `.txt`). Edit the Gist and rename the file if needed.

---

## Quick Reference: Gist Creation URL

Navigate to: https://gist.github.com/new

Confirm account: esca8peArtist (check top-right avatar)

---

*Created May 9, 2026 — Item 41 Phase 1 Distribution Setup Kit*
*Companion to: `phase-1-distribution-setup-checklist.md`, `phase-1-path-decision-template.md`, `phase-1-contact-verification-checklist.md`*
*See also: `execution/domain-42-gist-creation-steps.md` for the detailed Domain 42 procedure*
