---
title: "Phase 1 Outreach Email Templates — Tier 1 Institutional Outreach"
created: 2026-04-30
status: ready-to-send
path-agnostic: true
purpose: "3 email template variants (primary, follow-up, relationship-building) for Tier 1 recipients: law schools, think tanks, policy organizations. Includes subject line A/B options, personalization variables, CTA variants, tone calibration per institution type."
companion_files:
  - phase-1-substack-setup-guide.md
  - phase-1-contact-list-structure.md
  - phase-1-email-sequence-framework.md
  - distribution-institutional-outreach-templates.md
  - DISTRIBUTION_GIST_URLS.md
---

# Phase 1 Outreach Email Templates — Tier 1 Institutions

**Scope**: These three templates (Primary, Follow-Up, Relationship-Building) cover the first two weeks of Tier 1 outreach. They work for law schools, think tanks, and policy organizations — the specific framing variables for each institution type are documented in Section 4.

**Before sending**: Fill all `{{placeholder}}` fields. Read one recent publication by the recipient (5–10 minutes) and add one specific, accurate reference in the personalization slot. Verify the contact's current role before sending — use the verification protocol in `BATCH_1_CONTACT_VERIFICATION.md`.

**What makes these work**: The research is substantive and free. The primary ask is feedback, not promotion. Every institutional contact at a law school, think tank, or policy org has received promotional materials disguised as research. These emails are not that — they lead with a specific, accurate reference to the recipient's actual work, offer something with immediate utility (the Litigation Tracker, a domain analysis relevant to their current docket), and ask for the one thing institutional contacts are most likely to provide: a practitioner's criticism of what the proposal gets wrong.

---

## Template 1: Primary Outreach (Cold or Warm Contact)

**Use for**: First contact with any Tier 1 institution. Works for both cold contacts (no prior relationship) and warm contacts where you have a shared network connection (reference it in the personalization line).

**Estimated time to personalize**: 10–15 minutes per contact.

**Subject line options (A/B test across Batch 1)**:

- **Subject A**: "Democratic Renewal Research — [Specific Domain Relevant to {{institution}}]'s Work"
- **Subject B**: "Free Research Resource for {{institution}}: 35-Domain Democratic Reform Analysis"
- **Subject C** (for law schools specifically): "Litigation Support Research — Democratic Renewal Proposal, CC 4.0"
- **Subject D** (for think tanks): "Independent Research: 35-Domain Democratic Structural Reform Analysis, Free to Use"

Note on subject line selection: Subject A performs best with known contacts (reference to specific domain signals you have read their work). Subject B is higher open-rate for cold contacts at organizations with strong research consumption habits. Subject C works specifically for law school contacts if you are leading with the Litigation Tracker. Test A and B across Batch 1 and observe open rates.

---

### Email Body — Primary Template

---

{{contact_name}},

I'm writing because {{institution}}'s work on {{specific_recent_work}} connects directly to a research project I've been developing, and I believe several sections are immediately useful to your team.

{{personalization_paragraph — 2–3 sentences: reference a specific recent publication, case, testimony, or report by the institution. Be accurate. Do not generalize.}}

The project is an independent, 35-domain proposal for democratic structural reform — every reform documented in at least one functioning democracy, every claim sourced, everything published under Creative Commons Attribution 4.0. It is not affiliated with any organization, party, or funder. It is research, offered freely.

The sections most directly relevant to {{institution}}'s work:

{{domain_block — 2–3 bullet points, each 2–3 sentences, drawn from the domain(s) most relevant to this specific institution. See Section 4 for institution-type-specific domain lists.}}

Two documents I am sending alongside this email because they are the most immediately actionable:

**The Litigation Tracker** documents active federal cases with current status, next deadlines, and links to case filings — designed as a working reference for attorneys and researchers. {{litigation_tracker_url}}

**The 35-Domain Proposal** covers electoral reform, judicial independence, prosecutorial accountability, war powers, immigration, healthcare access, academic freedom, environmental rollbacks, and more. {{full_proposal_url}}

The two-page executive summary is the fastest entry point: {{executive_summary_url}}

Everything is CC 4.0 — cite it, excerpt it, share it with colleagues, adapt it to your institution's specific context.

I have one direct request: feedback. What does the proposal get wrong from {{institution_sector}}'s perspective? What is missing from the analysis that practitioners in your field would immediately notice? I am genuinely trying to strengthen the research with input from organizations doing this work, and your team's perspective would materially improve it.

If the materials are useful and you are willing, I would also welcome introductions to colleagues at peer institutions who might find them relevant — particularly {{referral_target_type}}.

{{warm_close — one sentence, calibrated to institution type. See Section 4.}}

{{your_name}}
{{your_contact_info}}

---

### Personalization Variable Reference

| Variable | What to Fill | Notes |
|----------|-------------|-------|
| `{{contact_name}}` | First name only for known contacts; "Dr. [Last Name]" for senior academics; "[First Name]" for think tank staff | Check the institution's staff directory for current title |
| `{{institution}}` | Full institution name on first use; short name on second use ("the Center," "Yale Law," "Brennan Center") | |
| `{{specific_recent_work}}` | Title or brief description of a specific recent publication, testimony, or case | Must be accurate; do not guess. Visit the institution's publications page. |
| `{{personalization_paragraph}}` | 2–3 sentences referencing that specific work and making the connection to your research explicit | This is the most important field. Generic opening = email deleted. |
| `{{domain_block}}` | 2–3 bullet points from Section 4 for this institution type | Do not include more than 3 domains — overwhelming the recipient reduces engagement |
| `{{institution_sector}}` | "legal scholarship" / "policy research" / "national security law" / "civil rights litigation" / etc. | Match to their actual self-description, not your categorization |
| `{{referral_target_type}}` | "faculty working on administrative law" / "researchers tracking executive power" / "attorneys with active FISA dockets" | Be specific; generic referral requests get ignored |
| `{{warm_close}}` | See Section 4 by institution type | |
| `{{your_name}}` | Your preferred name for professional outreach | Consistent with your Substack and GitHub identity |
| `{{your_contact_info}}` | Email + Substack URL | |
| `{{litigation_tracker_url}}` | From `DISTRIBUTION_GIST_URLS.md` | Verify link is live before sending |
| `{{full_proposal_url}}` | From `DISTRIBUTION_GIST_URLS.md` | |
| `{{executive_summary_url}}` | From `DISTRIBUTION_GIST_URLS.md` | |

---

## Template 2: Follow-Up (No Response After 10–14 Days)

**Use for**: First and only follow-up to a non-responding Tier 1 contact. Send 10–14 days after the primary email. Do not follow up more than once on cold outreach; do not follow up more than twice if there was prior warm contact.

**Rule**: Follow-up should be shorter than the primary email, not longer. Its purpose is to resurface the primary email, not to add new information that should have been in the first message.

**Subject line options**:

- **Subject A** (reply chain — most effective): Respond to your own sent email with "Re:" to keep the thread. No new subject line needed.
- **Subject B** (new thread): "Following up — Democratic Renewal Research for {{institution}}"
- **Subject C**: "Quick note — {{specific_domain}} materials for {{institution}}"

---

### Email Body — Follow-Up Template

---

{{contact_name}},

Following up briefly on the research I shared two weeks ago — a 35-domain democratic renewal proposal with several sections directly relevant to {{institution}}'s work on {{specific_area}}.

If it landed in a busy week, the two-page executive summary is the fastest entry point: {{executive_summary_url}}

The Litigation Tracker ({{litigation_tracker_url}}) may be more immediately actionable if your team is tracking cases in real time.

Happy to answer any questions about specific domains or provide a tailored excerpt for your team's specific focus area.

No response necessary if the timing isn't right — the materials are there when they're useful.

{{your_name}}

---

### Follow-Up Calibration Notes

The follow-up's most important function is removing friction. The sentence "No response necessary if the timing isn't right" has two effects: it signals you are not a vendor pursuing a sale, and it reduces the cognitive burden on the recipient (they do not need to draft a polite decline). Both effects increase the probability of a genuine response when the materials become relevant.

Do not: apologize for the follow-up, extend new deadlines, offer to schedule a call in the follow-up (that belongs in the primary email or in response to a reply), or restate the full research scope.

Do: confirm the most immediately actionable document (Litigation Tracker for legal orgs, Executive Summary for general policy orgs), and leave the door open without pressure.

---

## Template 3: Relationship-Building (Response Follow-Through)

**Use for**: After receiving any positive response — acknowledgment, question, forwarding request, offer to share with colleagues. The purpose is to convert a first-touch interaction into an ongoing relationship.

**Critical rule**: Respond to every substantive response within 48 hours. Institutional relationships are built on responsiveness at the first engagement; a week-long delay after an interested response is nearly as damaging as no response.

**Subject line**: Always reply in the same thread as the response. Do not open a new thread.

---

### Email Body — Relationship-Building Template (Response to Positive Acknowledgment)

---

{{contact_name}},

Thank you for this — {{specific_reference_to_their_response}}.

{{response_to_their_specific_point — 2–4 sentences engaging directly with what they said, asked, or offered}}

{{conditional block A — if they offered feedback}}: Your point about {{their_feedback_topic}} is exactly the kind of practitioner input the research needs. I will incorporate {{specific_commitment}} in the next revision and note the source. If you have colleagues who would be willing to weigh in on {{related_area}}, I would genuinely welcome an introduction.

{{conditional block B — if they offered to share}}: I would be grateful if you shared it with {{their_forwarding_target}}. The most useful framing for forwarding: the Litigation Tracker is the most immediately actionable document for attorneys and researchers tracking active cases; the executive summary is the fastest way into the full scope of the proposal.

{{conditional block C — if they asked about a specific domain}}: The full Domain {{N}} analysis is at {{domain_specific_url}}. The most directly relevant sections for {{their_stated_focus}} are {{specific_sections}}. I am happy to walk through it by email or, if that's more efficient, a brief call.

One ongoing request: the proposal is updated on a monthly basis as new developments occur — FISA outcomes, circuit court rulings, legislative changes. If your organization tracks developments in {{their_focus_area}} that are not in the current tracker, I would welcome additions. The goal is a factual record maintained by the organizations closest to the issues.

{{your_name}}

---

### Relationship-Building Response Variables

| Variable | What to Fill |
|----------|-------------|
| `{{specific_reference_to_their_response}}` | Directly quote or paraphrase one thing they said. Shows you read their response fully. |
| `{{conditional blocks}}` | Select the one most relevant to their actual response. Do not include all three. |
| `{{their_feedback_topic}}` | Specific topic or domain they mentioned. |
| `{{specific_commitment}}` | What you will actually incorporate. Be concrete ("I will add a section on X" not "I will consider this"). |
| `{{their_forwarding_target}}` | What they said they would forward it to — their colleagues, a specific network, their team. |

---

## 4. Tone Calibration by Institution Type

The core email structure is identical across institution types. What changes is the domain emphasis, the warm close, and the specific feedback request. Use this section to select the correct variable fills for each institution category.

### Law Schools (Constitutional Law, Administrative Law, Civil Rights Clinics)

**Domain emphasis block — select 2–3 of these bullet points**:

- "Domain 6 (Judicial Independence) documents the post-CASA universal injunction landscape — including the three-track response to SCOTUS's narrowing of injunctive authority: statutory restoration, Rule 23 class action fortification, and state AG parens patriae standing. The analysis is directly relevant to clinic strategy for federal court challenges."
- "The Litigation Tracker documents 80+ active federal cases organized by category — immigration enforcement, civil service dismantling, civil rights, constitutional accountability — with current status, next deadlines, and case links. It is designed as a working reference for attorneys."
- "Domain 29 (Prosecutorial Weaponization) includes the full structural analysis of the SPLC indictment (April 21, 2026) — four identified doctrinal defects, the causal sequence from October 2025 FBI relationship severance to April 2026 indictment, and the reform proposals addressing accountability infrastructure dismantlement. Relevant to criminal law and civil rights clinic work."
- "Domain 28 (War Powers, Venezuela) analyzes the December 23, 2025 OLC memo's internal contradictions and forward-reach implications — the material most relevant to international law, war powers, and executive power seminars and clinics."

**Sector-specific feedback request**: "What does the proposal get wrong from a constitutional litigation perspective? Specifically: which reform proposals depend on legal theories that have low viability in the current SCOTUS composition, and which rely on statutory vehicles that are more durable?"

**Warm close**: "Thank you for the work your clinic does on [specific area]. The research is there when it's useful."

**Referral target type**: "constitutional law faculty working on executive power or administrative law"

---

### Think Tanks (Policy Research, Democracy Research, National Security)

**Domain emphasis block — select 2–3 of these bullet points**:

- "Domain 2 (Executive Power and Checks/Balances) documents the Schedule F → Schedule Policy/Career history, the OLC opinion record on emergency power use, and the structural reform proposals — including statutory civil service protections at the constitutional floor level. The comparative analysis covers Germany's Beamtenrecht model and the UK Senior Civil Service framework."
- "Domain 1 (Electoral Reform) documents the mid-decade redistricting record (Texas, North Carolina, Indiana, Missouri) with Cook Political Report seat-impact estimates, proportional representation implementation evidence from Germany and New Zealand, and the National Popular Vote Compact current status."
- "Domain 5 (Congressional Structure) covers the filibuster's constitutional history, reconciliation authority expansion, committee system reform, and the comparative evidence from Westminster systems and the Bundestag. The fiscal reform section (Domain 5) is directly relevant to think tanks working on budget process reform."
- "Domain 37 (Federal Executive Interference in 2026 Midterms) is the most time-sensitive domain — the SAVE Act Senate failure (April 22, 2026 cloture vote: 49-49), the voter ID implementation record, and the 12-organization election protection contact list with pending advocacy windows before August 7."

**Sector-specific feedback request**: "What does the proposal get wrong from a policy research perspective? Which reform proposals do you assess as politically non-viable in the current Congress, and which have realistic traction under a legislative scenario change?"

**Warm close**: "The research is yours to use — cite it, excerpt it, respond to it, or ignore it, as it fits your work."

**Referral target type**: "researchers working on democratic backsliding measurement or executive power reform"

---

### Policy Organizations (Advocacy, Reform Campaigns, Litigation Organizations)

**Domain emphasis block — select 2–3 of these bullet points**:

- "The four active trackers — Litigation, First Amendment Suppression, Environmental Rollbacks, Police Consent Decree — are designed as factual documentation tools for advocacy organizations. They are updated monthly and organized for citation by journalists, attorneys, and advocates. If your organization tracks incidents not currently documented, contributions are welcome."
- "Domain 7 (Rights Protection) covers the 28 state anti-protest laws enacted since 2021, the government data weaponization prohibition, and the constitutional analysis of immigration enforcement warrant requirements. The First Amendment Suppression Tracker [link] documents active cases by category with court status."
- "Domain 16 (Immigration) includes the community-based alternatives to detention evidence (cost: $20/day vs. $140–200/day for detention), the Article I immigration court independence argument, and the Abrego Garcia case analysis as the leading active precedent on deportation accountability."
- "Domain 37 (Federal Executive Interference in 2026 Midterms) documents the ICE-at-polling-place threat model, the SAVE Act's noncitizen voting evidence failure, and the election protection coordination infrastructure that needs to be in place before November. The advocacy window before the August 7 NVRA quiet period is the near-term action window."

**Sector-specific feedback request**: "What would your organization's advocacy team find most useful for current campaigns — and what is missing from the existing trackers or domain analyses that you are actively documenting yourselves?"

**Warm close**: "Everything is CC 4.0 — use it, adapt it, share it however serves your organization's work."

**Referral target type**: "peer organizations working on [specific area — fill from institution's issue portfolio]"

---

## 5. CTA Variants

Every primary outreach email should close with a clear, simple Call to Action. The CTA is not a sales close — it is an invitation to engage. Choose one per email; do not stack multiple CTAs.

**CTA Type 1 — Feedback request** (recommended for first contact with researchers and academics):
"One direct request: tell me what the proposal gets wrong from your perspective. What is missing? What would you correct?"

**CTA Type 2 — Referral invitation** (recommended for first contact with practitioners and advocates):
"If these materials are useful to your work, I would welcome an introduction to one or two colleagues who might find them relevant."

**CTA Type 3 — Tracker contribution** (recommended for organizations that document active cases or incidents):
"If your organization tracks incidents in [domain area] not currently in the tracker, I would welcome additions — the goal is a community-maintained factual record."

**CTA Type 4 — Discussion invitation** (for warm contacts where a call or meeting is plausible):
"I would welcome a 30-minute conversation about how these materials might be useful to your team's current work — happy to schedule whatever format works best."

**Do not use CTA Type 4 for cold contacts**. Requesting a call in a cold email is a high-ask that reduces response rates. Lead with CTAs 1 or 2 for first contact; offer CTA 4 after a positive response.

---

## 6. Subject Line A/B Testing Protocol

For Batch 1 (5 contacts), you do not have enough data to make subject line conclusions. Use Subject A for law school contacts, Subject B for think tank contacts. Record which subject line each contact received in the contact database (`phase-1-contact-list-structure.md`).

For Batch 2 (7–10 contacts): if Batch 1 generated any opens or responses, continue with the subject line that performed best. If no Batch 1 data, continue with Subject A for high-credentialing institutions (major law schools, established think tanks) and Subject B for policy organizations.

By Batch 3 you will have enough data to make an informed decision. Subject line testing is secondary to personalization quality — a weak subject on a highly personalized email outperforms a perfect subject line on a generic one.

---

*Companion documents: `phase-1-substack-setup-guide.md`, `phase-1-contact-list-structure.md`, `phase-1-email-sequence-framework.md`, `distribution-institutional-outreach-templates.md` (expanded templates for specific domain categories), `EMAIL_PERSONALIZATION_GUIDE.md`.*
