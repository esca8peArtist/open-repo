---
title: "Tier 2 Implementation Checklist: Phase 2 Launch Readiness and Risk Mitigations"
project: cybersecurity-hardening
created: 2026-05-09
status: production-ready
phase: Phase 2 — Organizational Playbook Adoption
session: Exploration Queue Item (cybersecurity-hardening Phase 2 launch)
depends_on:
  - tier-2-launch-sequencing-strategy.md
  - tier-2-organizational-adoption-messaging.md
  - ORGANIZATIONAL_OPSEC_PLAYBOOKS.md
  - engagement-scoring-template.csv
  - phase-2-tier2-candidate-scorecard.csv
  - tier-2-launch-checklist.md
audience: Internal — user action checklist for Phase 2 launch execution
---

# Tier 2 Implementation Checklist: Phase 2 Launch Readiness and Risk Mitigations

**How to use this document**: Work through Section 1 before sending any Tier 2 invitations. Section 2 covers active risk management during outreach. Section 3 provides the 30/60/90-day review gates. The items in each section are sequenced in execution order, not priority order — earlier items are prerequisites for later items.

---

## Section 1: Pre-Launch Readiness — What Must Be Ready Before Sending Tier 2 Invitations

### 1A. Materials Verification

- [ ] **`ORGANIZATIONAL_OPSEC_PLAYBOOKS.md` is complete and production-ready.** Verify four playbooks are present and substantive: Playbook 1 (NGO/Nonprofit), Playbook 2 (Labor Union), Playbook 3 (Legal Services), Playbook 4 (Academic Institutions). Each playbook should cover governance-level protections, staff safety, data architecture, and subpoena response. This was produced in Session 847 and should not require revision before launch.

- [ ] **`opsec-playbook.md` Part 0 is current and includes the California DROP platform documentation.** Part 0 is the most frequently requested individual section in Phase 1 and is the primary client-facing integration point for immigration legal aid organizations. Confirm the DROP platform pathway for residents without government-issued ID is accurately documented and the URL/process is current.

- [ ] **`implementation-guide.md` Tier 1 and Tier 2 checklists are formatted for non-technical readers.** These are the documents that intake coordinators, paralegals, and member liaisons will work from. Verify they are readable without technical background.

- [ ] **The Gist corpus URL is live and current**: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108. Check directly in a browser. Do not assume it is live because it was live at Phase 1 launch.

- [ ] **Sector-specific threat briefings from `TIER2_MESSAGING_TEMPLATES.md` are current for May 2026.** Four threat vectors confirmed operational in Q1–Q2 2026 should be reflected: ProKYC voice cloning, Shai-Hulud supply chain attacks (Bitwarden CLI), FISA 702 no-warrant protection through June 12, and CISA election security coverage gap. If any of these has changed status since May 6, update the briefings before sending.

- [ ] **`phase-2-board-briefing-template.md` exists and is complete.** This is required before any organizational orientation session — the executive director needs a document they can take back to their board. If this file is incomplete, produce it before scheduling the first orientation session. See `phase-2-tier2-organizational-outreach-strategy.md` Section 3, Gap 1 for content scope.

- [ ] **At least one sector-specific adoption messaging template from `tier-2-organizational-adoption-messaging.md` has been reviewed and personalized** for the first 3–5 contacts on the pre-contact list. Do not send generic templates. Personalization is not optional; it determines response rate.

### 1B. Contact List Verification

- [ ] **Phase 1 Tier 1 engagement data has been populated in `engagement-scoring-template.csv`.** Every Tier 1 contact needs a current Day 7 or Day 14 engagement score before three-factor readiness scoring can run. If engagement data is missing for any contact (bounces not logged, web-form sends not tracked), estimate conservatively: treat untracked contacts as Score 0 unless a reply has been received.

- [ ] **Three-factor readiness scoring has been run for all 45 Tier 1 contacts.** Generate four sub-lists: pre-contact (3/3), standard wave (2/3), conditional (1/3), exclude (0/3). Document the sub-lists — do not hold them in working memory. The pre-contact list is the top operational priority.

- [ ] **Pre-contact (3/3) organizations have verified current contact information.** Check the organization's website directly for current staff directories. Leadership changes frequently; do not use cached contact information from `engagement-scoring-template.csv` or `TIER2_DISTRIBUTION_PREP.md` without direct verification. Estimated time: 5–10 minutes per organization.

- [ ] **Academic contacts have not been scored on Factor A before Day 28.** Academic sector latency means a non-response at Day 14 is not a Factor A = 0 score. Do not finalize academic readiness scoring until Day 28 minimum, and extend to Day 42 for large research centers.

- [ ] **New Tier 2 organizations (from `tier-2-launch-sequencing-strategy.md` Section 2) have verified contacts.** At minimum, verify the national office contact for: AILA (aila@aila.org), National Immigration Project (info@nipnlg.org), National Council of Nonprofits (ncn@councilofnonprofits.org), and AFL-CIO Technology Institute (aflcio@aflcio.org). These four are the highest-priority new organizations for Week 1 outreach.

- [ ] **`phase-2-tier2-candidate-scorecard.csv` is updated** with any changes from Phase 1 engagement that affect the provisional Factor B or C scores in the scorecard.

### 1C. Capacity Check

- [ ] **Response management capacity is assessed before launch.** If 30 organizations respond within 2 weeks — a plausible outcome given the pre-contact list quality — the sender needs approximately 15 hours of capacity for: reading and routing responses (30 responses x 15 minutes each = 7.5 hours), drafting personalized replies (30 responses x 15 minutes average = 7.5 hours). If this capacity is not available, stagger the launch rather than launching the full pre-contact and standard wave in the same week.

- [ ] **Orientation session scheduling capacity is assessed.** The orientation session offer in the pre-contact invitations proposes specific dates. Have calendar availability confirmed for at least 4 sessions in the 2-week window after invitations go out. Offering sessions that cannot be honored damages credibility.

- [ ] **The written orientation session summary template is ready.** Post-session written summaries must be sent within 48 hours. Prepare a template in advance: [Organization name], [Date], [Playbook discussed], [Specific integration next step agreed to], [30-day check-in date]. This takes 15 minutes per session to complete from the template.

---

## Section 2: Active Risk Mitigations During Outreach

### Risk 1: Managing 30+ Organizational Inbound Inquiries

**The risk**: A successful initial send generates more inbound interest than the sender can handle while maintaining response quality. Delayed responses to organizational contacts damage the relationship and reduce adoption probability. Overwhelmed response management also creates the risk that high-priority contacts (3/3 pre-contact list organizations) receive slower responses than standard-wave contacts who happened to reply first.

**Mitigations**:

- [ ] **Maintain a dedicated response queue.** Every inbound response goes into a single tracked list with: organization name, date received, response type (acknowledgment, question, meeting request, decline), and required action. Do not triage from email alone — the context collapses. Keep the queue in a separate document or spreadsheet.

- [ ] **Prioritize by readiness score, not arrival order.** A response from a 3/3 pre-contact organization requires same-day or next-day action. A response from a standard-wave (2/3) organization can wait 48–72 hours. A response from a conditional (1/3) organization can wait 5 days. Systematic prioritization prevents the situation where you spend 2 hours on a low-priority response and miss a 3-day window with ACLU or CLINIC.

- [ ] **Set a capacity ceiling and stick to it.** Maximum orientation sessions per week: 3. Maximum pre-contact conversations active simultaneously: 8. When at ceiling, new session requests are scheduled for the following week rather than slotted into an overcrowded calendar. Orientation session quality degrades when sessions are back-to-back; the written summary suffers, the follow-through suffers.

- [ ] **Decline-and-defer language is prepared in advance.** For contacts that are a genuine fit but arrive when capacity is at ceiling: "I want to give this the attention it deserves — can we schedule a session in [2-week window]?" This preserves the relationship without overcommitting.

### Risk 2: Versioning Organizational Derivatives

**The risk**: Organizations that adopt the corpus will modify it — translating it, adapting it for their intake process, integrating sections into their own training materials, or excerpting sections for client handouts. Without a versioning protocol, the original corpus and organizational derivatives become indistinguishable. A derivative with errors gets attributed to the original; an updated version of the original is not distributed to organizations using an old derivative.

**Mitigations**:

- [ ] **Establish a clear citation and versioning instruction** in every orientation session and written summary. Standard language: "When adapting this material for your organization's use, please note which sections were adapted, what was changed, and the date of adaptation. Cite the original corpus [Gist URL] in any publication or training material. If you identify errors in the original, I want to know so I can update it."

- [ ] **Request copies of derivative products** from all organizations that confirm they have created them. This is not a demand — it is a request for feedback and an offer of attribution. Organizations that have invested staff time in a derivative have an interest in knowing if the source material has been updated.

- [ ] **Maintain a derivatives log.** When an organization confirms they have created a derivative (intake checklist, staff training slide deck, translated handout), add it to a simple tracking list: [Organization], [Type of derivative], [Date produced], [Contact for updates], [Errors identified]. This log is the foundation for v1.1 revision decisions.

- [ ] **Version control the organizational playbooks.** When Playbook 1, 2, 3, or 4 is updated in `ORGANIZATIONAL_OPSEC_PLAYBOOKS.md`, the version number and change log should be visible in the document header. Organizations with derivatives need to know when the source material has changed. A quarterly email to all active partners noting version changes is sufficient.

- [ ] **Distinguish between "use freely" and "cite the source" provisions.** The corpus is designed to be cited and adapted. Organizations can reproduce Part 0 verbatim in a client handout without editorial control from the sender. They should cite the source (the Gist URL), but the adaptation is theirs to make. This reduces adoption friction; organizations should not feel that adaptation requires permission.

### Risk 3: Preventing Confidentiality Breaches

**The risk**: Some organizational contacts will disclose sensitive information — about their own organization's security vulnerabilities, about specific clients at risk, about active investigations or subpoenas. This information, if shared or referenced improperly, can create legal exposure for the organization and the sender. The corpus is designed for public distribution; the organizational context around its adoption is not public.

**Mitigations**:

- [ ] **Establish a clear information handling protocol before the first orientation session.** Standard language at the start of each session: "Everything we discuss about your organization's specific situation is confidential. The corpus itself is publicly available. Anything you share about your organization's operations, client situations, or security vulnerabilities will not be shared with anyone, including other organizations in this program." State this explicitly; do not assume it is understood.

- [ ] **Do not share one organization's adoption details with another without permission.** Social proof (referencing that "a legal services organization in California has integrated Part 0 into their intake process") is appropriate and useful. Naming the organization without permission is not. Before using any organizational adoption as social proof, ask explicitly: "Can I reference this in conversations with other organizations? I'd keep the details vague unless you're comfortable being named."

- [ ] **Keep session notes in a secure, non-cloud format.** Session summaries and orientation notes contain sensitive organizational information. Store them encrypted (Veracrypt, iCloud with ADP enabled) rather than in Google Docs, Notion, or other cloud platforms with government access agreements. This is consistent with the corpus's own guidance.

- [ ] **Do not solicit information beyond what is operationally necessary.** If an organization discloses that they have received a subpoena, that disclosure is relevant to scoping the Playbook 3 discussion. It is not an invitation to ask for details of the subpoena or the investigation. Take what is offered; do not probe for more.

- [ ] **If an organization discloses an active legal emergency** (active subpoena, imminent ICE raid on a partner organization, ongoing investigation), treat this as out-of-scope for the corpus distribution relationship. Refer them to legal counsel (their own or, if they have none, to the NLG Legal Support Hotline: 212-679-6018). The corpus is a resource for security planning, not emergency response.

---

## Section 3: Quarterly Review Gates

### 30-Day Review (June 28 or equivalent date, one month after Phase 2 launch)

**Goal**: Validate that outreach has generated meaningful engagement and that at least one orientation session has produced a confirmed adoption intent. This is a pivot point: findings at 30 days should alter the messaging approach for the Month 2 sends.

**Checklist items**:

- [ ] Count responses received from all three categories: pre-contact (3/3), standard wave (2/3), new Tier 2 organizations. Calculate response rates by category and sector.
- [ ] Count orientation sessions completed. Target: 3 sessions completed by Day 30. Below 2: diagnose whether the invitation framing or the session scheduling is the bottleneck.
- [ ] Count confirmed adoption intent signals (Factor B = 1 based on post-session confirmation, not pre-campaign estimate). Any confirmed intent to modify a workflow is a meaningful signal.
- [ ] Review the top 3 objections or framing questions that appeared across all responses and sessions. These are the gaps in the messaging that the Month 2 wave needs to address.
- [ ] Assess the sector distribution of responses. If all responses are from one sector (e.g., all from academic programs, none from legal services), the cross-sector strategy is not working and messaging refinement for the underperforming sectors is needed before Month 2 sends.
- [ ] Update `engagement-scoring-template.csv` with all engagement data received through Day 30. Do not allow tracking to fall behind; data quality at the 30-day mark determines the quality of the 60-day assessment.

**Decision gate**: If fewer than 2 orientation sessions are confirmed at Day 30 and no confirmed adoption intent has been received: delay Month 2 sends by 2 weeks, spend the delay revising the pre-contact invitation copy based on observed objections, and re-contact the 3/3 pre-contact list with a single follow-up anchored to a current time-sensitive policy hook (June 12 GSRA deadline if still upcoming; DocketWise breach if contacting legal services organizations).

**30-day decision options**:
- Proceed to Month 2 sends on schedule (at least 2 sessions confirmed, 1+ adoption intent)
- Delay Month 2 by 2 weeks with messaging revision (fewer than 2 sessions, some responses)
- Conduct full messaging diagnostic before Month 2 (zero confirmed sessions, below 10% response rate)

---

### 60-Day Review (July 28 or equivalent, two months after Phase 2 launch)

**Goal**: Assess organizational adoption velocity and identify whether the corpus is being used operationally or only being reviewed. Two months is sufficient time for a motivated organization to integrate Part 0 into intake or to draft a first version of their subpoena response protocol. If no workflow modifications have occurred in two months, the adoption process is stalled — not just slow.

**Checklist items**:

- [ ] Count confirmed workflow modifications (not adoption intent — confirmed operational change). Target for Month 2: at least 1 organization has made a documented change to an intake checklist, training curriculum, or communications protocol.
- [ ] Conduct 30-day check-in calls with all organizations that completed orientation sessions in Month 1. Standard agenda: (a) What section has been most useful? (b) What has not been integrated, and why? (c) What would make the next step easier? (d) Confirm 60-day follow-up date. These calls are 20–30 minutes each.
- [ ] Count derivative products received or confirmed. Any organizational material (client handout, staff briefing, intake checklist) that uses corpus content counts.
- [ ] Assess the derivatives log. Are organizations creating derivatives that diverge significantly from the corpus? If so, determine whether the divergence reflects a legitimate sector-specific adaptation (acceptable) or a factual correction the corpus should incorporate (priority update).
- [ ] Review the standard Tier 2 wave response data. What is the response rate from 2/3 standard-wave organizations? If below 10%: the wave messaging needs revision. If above 20%: flag any 4–5 score contacts for expedited follow-up.
- [ ] Assess whether any Tier 2 organization has shared the corpus with organizations the sender did not contact. Even one inbound referral from a Tier 2 partner organization is a meaningful signal of self-sustaining distribution.
- [ ] Check media and citation monitoring. Search "[organization names] + Palantir" and "[organization names] + ELITE" on social media and in press databases. Document any references.

**Decision gate**: If zero workflow modifications at Day 60 and fewer than 3 orientation sessions completed: extend the pilot window to 90 days and switch from session-first to document-first approach for remaining 3/3 contacts. Send the sector-specific playbook directly without requiring session commitment; make the 90-day check-in the primary follow-up. Some organizations adopt materials before they schedule a call.

---

### 90-Day Review (August 28 or equivalent, three months after Phase 2 launch)

**Goal**: Determine whether Phase 2 has achieved minimum threshold for Tier 3 planning. The minimum threshold is 3 organizations with confirmed workflow modification across at least 2 sectors. If this is not met at 90 days, Tier 3 launch is premature.

**Checklist items**:

- [ ] Count total confirmed workflow modifications across all sectors. Target: 3 minimum, 6 target.
- [ ] Document workflow modifications specifically: organization name, sector, which playbook section was integrated, what the specific workflow change was, and how many clients, members, or staff are now reached by the change. This documentation is the evidence base for any funder conversations in Month 4.
- [ ] Count derivative products with citations. Target: 2 published or distributed derivatives at Month 3.
- [ ] Count inbound referrals from Tier 2 organizations. Target for self-sustaining distribution signal: 1 inbound contact citing a Tier 2 organization. Zero inbound referrals at Day 90 is a signal that organizations are adopting but not propagating — diagnose and address before Tier 3 launch.
- [ ] Conduct 60-day check-in calls with Month 1 orientation cohort. Agenda: (a) Has the workflow modification been sustained? (b) What feedback have staff or clients given? (c) What would prompt them to share the corpus with peer organizations?
- [ ] Conduct initial outreach to funder sector (Ford, MacArthur, OSF) with concrete adoption data, if minimum threshold is met. Do not contact funders without confirmed adoption data to present.
- [ ] Assess whether to publish v1.1 of the organizational playbooks. If feedback from 60- and 90-day calls has produced factual corrections or procedural gaps, incorporate and version before launching Tier 3.
- [ ] Make Tier 3 launch decision. Tier 3 launch requires: minimum threshold met (3 organizations, 2 sectors), at least 1 organizational partner willing to be named publicly, and v1.1 playbooks published.

**Decision gate at Day 90**:

| Condition | Action |
|---|---|
| 3+ workflow modifications, 2+ sectors, 1+ named partner | Proceed to Tier 3 launch planning |
| 3+ workflow modifications, 2+ sectors, 0 named partners | Extend to 120 days; pursue co-promotion discussions with confirmed adopters |
| 1–2 workflow modifications, any sectors | Extend pilot to 120 days; apply document-first approach to all remaining conditional contacts; do not launch Tier 3 |
| 0 workflow modifications | Full diagnostic of content, messaging, and contact targeting; revise before any further launch |

---

## Quick Reference: Key Contacts, Documents, and URLs

**Corpus Gist URL**: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108

**Primary organizational playbook file**: `ORGANIZATIONAL_OPSEC_PLAYBOOKS.md`

**Engagement scoring**: `engagement-scoring-template.csv`

**Candidate scorecard**: `phase-2-tier2-candidate-scorecard.csv`

**Adoption messaging templates**: `tier-2-organizational-adoption-messaging.md` (Templates OA-1 through OA-5)

**Launch sequencing**: `tier-2-launch-sequencing-strategy.md`

**Amplifier network messaging** (different from organizational adoption): `TIER2_MESSAGING_TEMPLATES.md`

**Board briefing template**: `phase-2-board-briefing-template.md` (verify completeness before first orientation session)

**NLG Emergency Legal Support Hotline** (for contacts with active legal emergencies): 212-679-6018

**California DROP Platform** (for Part 0 opt-out, no government ID required): deleteact.oag.ca.gov

---

*Created: 2026-05-09. Section 1 is a pre-launch checklist; execute before sending any Tier 2 invitations. Section 2 is an active-outreach risk management reference; keep accessible throughout Phase 2. Section 3 review gates are calendar anchors; mark Day 30, 60, and 90 immediately after Phase 2 launch date is confirmed.*
