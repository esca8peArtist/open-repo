---
title: "Phase 1 Contingency Communication Strategy"
item: 44
created: 2026-05-14
status: production-ready — deploy Day 1, consult only if metrics trigger contingency
scope: "Pre-emptive contingency playbook for Phase 1 distribution (May 15–June 4). Covers binary decision triggers, pre-written escalation messaging by sector, secondary contact pool, backup amplification channels, stakeholder framing, and day-by-day activation checklist."
reference_sources:
  - PHASE_1_DISTRIBUTION_EXECUTION_BLUEPRINT.md (primary operational document)
  - execution/tier-1-contact-batches.md (contact sequencing and targets)
  - execution/success-metrics.md (measurement architecture)
  - PHASE_1_CONTINGENCY_PLAYBOOK.md (technical failure recovery)
  - execution/phase-1-personalized-batch-1.md
  - execution/phase-1-personalized-batch-2.md
  - execution/phase-1-personalized-batch-3.md
  - BATCH_1_CONTACT_LOG.md
trigger_condition: "Consult this document only when a metric threshold below is breached. Do not modify primary execution plan based on anxiety about potential underperformance — only on confirmed metric breach."
---

# Phase 1 Contingency Communication Strategy

**Prepared**: May 14, 2026  
**Applies to**: Path A+37 Hybrid distribution, May 15 – June 4, 2026  
**Primary execution document**: PHASE_1_DISTRIBUTION_EXECUTION_BLUEPRINT.md (Section 8 contains technical failure recovery; this document covers strategic communication contingency)

---

## 1. Executive Summary

This document answers one question: if Phase 1 metrics underperform, what do you do, when, and in what exact words?

The primary distribution plan (Path A+37) is sound. The targets it sets are ambitious relative to industry benchmarks — cold outreach to academic and policy organizations yields 5–8% average reply rates across all sectors (M+R Benchmarks 2026; Backlinko 2025). The Phase 1 plan targets 20–40% reply rates from highly personalized, research-grounded outreach to contacts whose published work is directly cited. That gap between benchmark and target is intentional: this is not cold outreach in the conventional sense. It is a warm academic pitch with primary-source grounding and personal relevance to each recipient's current work. That difference typically produces 3–5x the average response rate for policy outreach when executed correctly.

Nevertheless: underperformance is possible. Contingency is not a plan for failure — it is a plan for reducing decision latency so that if a threshold is breached, the response is already written, the contacts are already identified, and the framing is already tested.

**The three core contingency decisions:**

1. **Day 3 (May 17)**: If Batch 1 reply rate is below 8% (zero of five or one non-substantive reply), escalate before sending Wave 2 on May 20.
2. **Day 7 (May 21)**: If cumulative Tier 1 reply rate is below 12% across all emails sent to date, activate secondary contact pool and modify subject line approach for Wave 2 remainder.
3. **Day 14 (May 28)**: If media mentions are zero and Domain 42 participation notices are zero, activate backup amplification via preprint submission and coalition briefings.

Two additional triggers — one organizational (Day 10) and one election-track-specific (Day 16) — are defined in Section 2.

**What contingency does not change**: the framework itself, the Gist URLs, the domain content, the Phase 2 roadmap, or the August 7 NVRA hard deadline. Those are fixed. Contingency modifies how and to whom the outreach is directed.

---

## 2. Contingency Triggers — Five Scenarios with Thresholds

### Trigger 1 — Day 3 (May 17): Batch 1 Early Warning

**Metric**: Batch 1 reply rate at 72 hours post-send (Batch 1 sent May 14–15)

**Threshold for contingency**: Zero substantive replies, OR one reply that is acknowledgment-only (not engagement, question, or referral signal).

**Context**: The Batch 1 contacts (Goodman, Weiser, Chenoweth, Bassin, Elias) have average expected response cycles of 2–7 days based on their institutional context (Democracy Docket: 2–3 days; Brennan Center: 5–7 days; Harvard: 5–10 days). A zero at 72 hours is early but meaningful because at least Goodman (Just Security) and Elias (Democracy Docket) should have acknowledged within 48 hours if they received and read the email. Brennan Center and Harvard at 72 hours is not yet alarming.

**What this trigger means**: Not a fundamental messaging failure. Most likely causes: delivery issue on one or more addresses, subject line filtered, or timing issue.

**Trigger 1 Action**: Before sending any Wave 2 emails:
1. Verify delivery: send test email to yourself from the same account, confirm no spam trigger language
2. Check contact addresses against BATCH_1_CONTACT_LOG.md (Goodman = ryan@justsecurity.org; Weiser = wweiser@brennancenter.org; Chenoweth = erica_chenoweth@hks.harvard.edu; Bassin = ian@protectdemocracy.org; Elias = melias@elias.law)
3. If no bounce notifications and no delivery failure indicators: proceed with Wave 2 on schedule; the reply window has not closed
4. If any address bounced: re-verify on institutional website and resend within 24 hours with a revised subject line (see Section 3.1)

**Do not**: Accelerate Wave 2, resend Batch 1 without modification, or treat 72-hour silence as failure.

---

### Trigger 2 — Day 7 (May 21): Cumulative Reply Rate Gate

**Metric**: Total substantive replies received from all emails sent to date (Batch 1 + any Phase 1b Tier 1 sends + Domain 42 Category A–B)

**Threshold for contingency**: Cumulative reply rate below 12% of total emails sent. At Day 7, expected sends are approximately 17–22 emails total (5 Batch 1 + 7 Phase 1b Tier 1 + 5 Domain 42 Category A). A 12% rate = 2–3 replies. If fewer than 2 substantive replies have arrived, activate this trigger.

**Historical benchmark context**: The M+R Benchmarks 2026 study shows nonprofit advocacy email generates a 1.4% response rate on mass lists. However, highly personalized cold outreach to senior policy contacts — with specific citation of their published work — typically achieves 15–30% in comparable campaigns (Backlinko 2025 research on targeted outreach vs. mass send; see also Instantly.ai cold email benchmarks showing small-list, high-personalization campaigns achieve 6x the average rate). A 12% floor at Day 7 represents approximately half of the lower bound of the targeted personalization range, meaning genuine underperformance.

**Trigger 2 Action**: Activate secondary contact pool (Section 4) for Day 10+ outreach. Modify subject lines for remaining Wave 2 sends using the escalation variants in Section 3.2. Do not send Wave 3 until at least one Wave 2 response is received.

---

### Trigger 3 — Day 10 (May 24): Organizational Engagement Gate

**Metric**: Number of distinct organizations showing any adoption signal (categories 3–6 from the tracking scale: interest signal, referral, implementation signal, or public adoption)

**Threshold for contingency**: Zero organizations at Category 3 or above by Day 10.

**Context**: This is distinct from reply rate. A reply that is acknowledgment-only ("thanks for sharing") is not an engagement signal. An organization asking a follow-up question, requesting a specific domain section, or routing to a colleague is Category 3 and counts.

**Why this trigger matters**: The framework's credibility-building architecture depends on at least one Tier 1 organization showing engagement before Wave 3 goes out (Days 15–21). Wave 3 emails open with credibility anchors referencing Batch 1–2 responses. If no credibility anchor exists, the Wave 3 opener must be revised.

**Trigger 3 Action**: 
- Revise all remaining email openers from credibility-anchor framing to standalone-pitch framing: remove references to "since distributing to [contact]" and replace with specific domain data hooks (see Section 3.3)
- Send one follow-up email to Batch 1 contacts who have not replied, using the follow-up variant in Section 3.4
- Identify two additional contacts from the secondary pool (Section 4) who are explicitly tagged for organizational depth rather than credibility signaling

---

### Trigger 4 — Day 14 (May 28): Media and Domain 42 Zero-Detection Gate

**Metric A**: Media mentions — total count of external references to the framework discovered via Google Alerts or manual search
**Metric B**: Domain 42 participation notices — organizations that have signaled intent to file a DEA-1362 hearing participation notice

**Threshold for contingency**: Metric A = zero, AND Metric B = zero or one

**Context**: By Day 14, the DEA-1362 hearing deadline has closed. Any Domain 42 traction is now historical, not activatable. The Day 14 gate is therefore a combined assessment: has the framework achieved any external presence at all?

**Why both metrics together**: A framework that has media pickup but no Domain 42 traction has demonstrated public interest but not institutional action. A framework with one Domain 42 filer but no media coverage has institutional action but no discovery pathway. Zero on both indicates a distribution reach problem, not a content problem.

**Trigger 4 Action (Media)**:
- Upload the executive summary to SSRN (Social Science Research Network) within 48 hours — see Section 5.1 for filing procedure
- Send a 500-word press pitch to 10 targeted journalists covering democracy and election law — see Section 5.2 for the pre-written pitch text
- Post a Twitter thread structured as a litigation-documentation thread, not a framework-overview thread — see Section 5.3 for the thread template

**Trigger 4 Action (Domain 42)**:
- Log the final Domain 42 outcome in DISTRIBUTION_EXECUTION_LOG.md
- Forward the completed Domain 42 Gist URL to any Tier 1 contacts who had expressed general interest in regulatory reform, with a one-sentence note: "The May 28 DEA hearing closed today — the regulatory capture analysis (Domain 42) is now archival documentation. Forwarding in case it is useful for any administrative law contexts your work touches."
- No further Domain 42 escalation is available after May 28.

---

### Trigger 5 — Day 16 (May 30): Election Protection Track Zero Gate

**Metric**: Domain 37 election protection engagement — any of the 12 Phase 1b organizations have replied, requested a document, asked a follow-up question, or referenced Domain 37 in any context

**Threshold for contingency**: Zero replies from Phase 1b Tier 1 contacts (Weiser/Brennan Center, Elias/Democracy Docket, Bassin/Protect Democracy, Lawyers' Committee VRP, ACLU VRA, Lydgate/States United, Common Cause) by May 30 — the DOJ consent decree advocacy window close date

**Why May 30 is the threshold**: The DOJ consent decree window was the primary strategic rationale for the Path A+37 election-track send. May 30 closes that window. If no election-protection organization has engaged with Domain 37 by the date of the window's close, the election-track opportunity is deferred to August 7 (NVRA quiet period) and beyond.

**Trigger 5 Action**:
- Do not treat zero May 30 response as permanent failure — the August 7 deadline creates a second window. Document May 30 as "consent decree window closed without confirmed election-org engagement" and log for Phase 2 planning
- Send one brief (3–4 sentence) follow-up to any Phase 1b contacts who did not reply, framing the August 7 NVRA deadline as the next actionable window: "Following up on the Domain 37 materials from earlier this month — the August 7 NVRA quiet-period deadline is now 68 days out, which is within the 90-day documentation preparation window for pre-period injunctions. If the voter roll litigation map is useful for any cases your team is tracking, I'm happy to extract the August 7 section as a standalone document." Send this follow-up May 31–June 2.
- Begin Phase 2 election-track planning: identify August 7-specific contacts from secondary pool (Section 4, tagged NVRA-priority) for June outreach.

---

## 3. Escalation Messaging — Pre-Written Variants by Sector

All variants below are ready for immediate use. Select the variant matching the sector and the specific underperformance scenario. Do not combine multiple variants in one email. Each is designed to stand alone as a complete, minimal follow-up.

---

### 3.1 Revised Subject Lines (Trigger 1 — Delivery/Filtering Suspected)

If a Batch 1 contact has not acknowledged within 72 hours and you suspect spam filtering, resend with a modified subject. Remove any words that commonly trigger spam filters: "advocacy," "action," "democratic reform," "deadline," "urgent." Replace with subject lines that read as peer-to-peer research communication.

**Original (Batch 1 Goodman)**: "Domain 28/29 War Powers + DOJ Capture Research — Submission for Just Security"  
**Revised**: "War powers appropriations-as-constraint analysis — would value your read"

**Original (Batch 1 Weiser)**: "35-domain democratic reform framework — Brennan Center expertise on Domains 1, 6 needed"  
**Revised**: "Voting rights statutory pathway analysis — built on Brennan Center's Section 2 research"

**Original (Batch 1 Chenoweth)**: "Nonviolent resistance meta-analysis that cites your 3.5% threshold — would value your feedback on the methodology"  
**Revised**: "3.5% threshold in democracy-erosion contexts — methodological question for your lab"

**Original (Batch 1 Bassin)**: "Full-spectrum democratic accountability research — Domains 2, 6, 29, 34 — would value Protect Democracy's input"  
**Revised**: "Schedule F cascade mechanism — statutory remedy analysis for Protect Democracy's review"

**Original (Batch 1 Elias)**: "DOJ Voter Roll Litigation Documentation (23 Active Cases) + Systematic Election Interference Framework"  
**Revised**: "24 DOJ voter roll cases — cross-district coordination pattern documentation"

---

### 3.2 Law Schools: "Academic Contribution Opportunity" Frame

Use when: Batch 2 or 3 law school contacts (Stephanopoulos, Shams, McNicholas, Gerken, Balkin, Brest) have not replied after 10 days and Trigger 2 is active.

**Variant A — Methodology Review Frame**:

> Subject: Independent research on [their specific area] — methodological question before wider circulation
>
> [Name],
>
> I'm an independent researcher who has built a 35-domain comparative framework on democratic institutional erosion. Before distributing more broadly to legal practitioners, I want to verify the constitutional analysis holds up against [their specific area of expertise]. The domain most directly in your lane is [Domain X — 5 pages], which argues [specific one-sentence claim from that domain].
>
> My specific question: is the [statutory / doctrinal / procedural] mechanism I've identified in Section [X] the right frame, or does [their recent publication, e.g., "your work on Callais"] suggest a more direct pathway?
>
> Not asking for endorsement or distribution — asking whether the analysis is defensible before it reaches practitioners who might rely on it.
>
> [Link to domain Gist]
>
> [Your name]

**Variant B — Clinic Resource Frame**:

> Subject: Election law clinic resource — [specific domain] documentation
>
> [Name],
>
> The [Domain X] analysis may be useful for [clinic name or course name] as a documentation resource — specifically [one specific section: e.g., "the NVRA August 7 quiet-period injunction preparation timeline"]. It's published under CC Attribution 4.0, so students and clinic staff can use and cite it without restriction.
>
> I'm reaching out because the domain directly cites [their recent publication or case they worked on]. I want to make sure the legal analysis is accurate before it reaches wider use.
>
> Does this match anything your clinic is currently working on?
>
> [Your name]

---

### 3.3 Civil Rights Organizations: "Coalition Building" Frame

Use when: NAACP LDF (Hewitt), Lawyers' Committee (VRP Team), ACLU VRA, or other civil rights contacts have not replied by Day 10 and Trigger 3 is active.

**Variant A — Litigation Coordination Frame**:

> Subject: Coalition documentation for [active case or issue area] — [organization name]
>
> [Name],
>
> [Organization name]'s [specific litigation or advocacy work, e.g., "Callais redistricting response"] has moved quickly since [specific date or development]. I wanted to make sure the documentation framework I've developed is in the hands of organizations working on [specific constitutional issue] before the [next deadline or hearing].
>
> The two sections most directly relevant to your current work: [Section X — one sentence description] and [Section Y — one sentence description]. Both are in [Domain X], at [Gist URL].
>
> I'm not asking for partnership or endorsement — I'm asking whether the documentation adds anything to what your team is already tracking, and whether there's anyone on your staff who handles [specific issue area] who should have access to it.
>
> [Your name]

**Variant B — Coalition Amplification Frame**:

> Subject: [Domain X] documentation — coalition briefing for [issue area] organizations
>
> [Name],
>
> As the coalition of organizations working on [specific issue, e.g., "voter roll litigation"] grows ahead of August 7, I wanted to make sure [organization name] has access to the cross-case documentation I've compiled: [specific resource, e.g., "24 active DOJ voter roll cases with court, status, and next deadline"]. Several organizations in adjacent work are using the litigation tracker to coordinate documentation across cases.
>
> I'm reaching out specifically to [organization name] because [one sentence on why this org's work connects to this specific resource].
>
> If it's useful, I can extract [specific section] as a standalone document for your team. No ask beyond that.
>
> [Your name]

---

### 3.4 State Attorneys General: "Enforcement Precedent" Frame

Use when: State AG contacts (Colorado, California, Michigan, Washington) have not replied by Day 10 and Trigger 3 is active.

**Variant A — Multistate Coalition Frame**:

> Subject: [State] AG enforcement theory — [Domain X] multistate coalition analysis
>
> [AG office or staff name],
>
> The [Domain X] federalism analysis identifies [State] as one of [number] states where the [specific legal mechanism, e.g., "HSGP conditionality / SAVE Act 81% false positive rate / Medicaid-NVRA enforcement nexus"] creates a viable multistate AG coalition enforcement theory. The specific legal theory is in Section [X] of [Domain X] at [Gist URL].
>
> Several [neighboring or like-positioned] AG offices are reviewing whether this enforcement framework supports a coordinated comment or filing. I'm forwarding to [State] AG's office because [one sentence on state-specific standing or interest].
>
> The question for your office: does [State]'s [specific statutory or case law context] support the enforcement theory in Section [X], and would a multistate coalition framing strengthen or complicate your office's position?
>
> [Your name]

**Variant B — Enforcement Deadline Frame**:

> Subject: [State] AG — [Domain X] enforcement deadline: [specific date]
>
> [AG staff name],
>
> The [specific deadline, e.g., "June 1 HHS comment window"] is [X days] away. The [Domain X] analysis documents the NVRA Section 7 enforcement theory that gives [State] AG's office standing to file comments on the Medicaid work requirement provisions — specifically the argument that OBBBA administrative burden constitutes a constructive NVRA Section 7 violation [52 U.S.C. § 20507].
>
> I'm forwarding the enforcement-pathway extract at [Gist URL]. If it's useful for the comment filing, I can prepare a one-page standalone for staff use.
>
> [Your name]

---

### 3.5 Follow-Up Variant for Non-Responsive Batch 1 Contacts (Trigger 3 Active)

Use when: A Batch 1 contact (Goodman, Weiser, Chenoweth, Bassin, or Elias) has not replied after 10 days and zero organizational engagement has been recorded.

This follow-up is sent once, one time only. It does not repeat the domain pitch. It offers a minimal, low-friction entry point.

> Subject: Following up — [one specific new development since original send]
>
> [Name],
>
> Following up on the [domain] research I sent [specific date]. Since then, [one factual update: e.g., "the NVRA August 7 quiet-period documentation has been updated to include [X]" or "the Callais redistricting cascade has added [state] to the affected districts"].
>
> If the methodology review I proposed is low-priority right now, the single most useful thing I could ask is: is there someone on your team or at a peer organization who handles [specific sub-issue] who would find this documentation useful? I'm not asking for introduction without permission — just whether the referral makes sense.
>
> [Gist URL for the specific domain]
>
> [Your name]

---

## 4. Secondary Contact Activation — 40+ Tier 2 Contacts for Day 7+ Supplemental Outreach

The following contacts are drawn from Phase 1 materials (Batch 2, Batch 3, and Phase 1b Tier 2) and are identified as secondary/escalation contacts for activation if Trigger 2 or Trigger 3 fires. They are organized by sector and tagged with the activation priority and the specific domain hook.

**Activation rule**: Do not contact Tier 2 contacts until Day 7 at the earliest, and only after Trigger 2 threshold is confirmed breached. The credibility-building architecture requires Tier 1 responses to precede Tier 2 outreach wherever possible.

---

### Law Schools and Policy Schools (12 contacts)

| Contact | Organization | Role | Email | Priority Domain | Activation Tag |
|---------|-------------|------|-------|-----------------|---------------|
| Michael Waldman | Brennan Center | President | waldman@brennancenter.org | Full framework | T2-Day7 |
| Phil Brest | American Constitution Society | President | pbrest@acslaw.org | Domain 6 | T2-Day7 |
| Jack Balkin | Yale Law / Balkinization | Professor | balkin@yale.edu | Domains 6, 8, 35 | T2-Day8 |
| Akhil Amar | Yale Law | Professor | akhil.amar@yale.edu | Constitutional theory | T2-Day10 |
| Heather Gerken | Yale Law / Dean | Dean | heather.gerken@yale.edu | Domain 37, federalism | T2-Day10 |
| Richard Hasen | UCLA Law | Professor | rhasen@law.ucla.edu | Domains 1, 33, 37 | T2-Day7 — election law focus |
| Erwin Chemerinsky | UC Berkeley Law | Dean | chemerinsky@law.berkeley.edu | Domains 6, 29, 34 | T2-Day8 |
| Nicholas Stephanopoulos | Harvard Law | Professor | nsteph@law.harvard.edu | Domain 37, gerrymandering | T2-Day8 |
| Leah Litman | Michigan Law | Professor | llitman@umich.edu | Shadow docket, Domain 6 | T2-Day9 |
| Melissa Murray | NYU Law | Professor | mm12177@nyu.edu | Domains 29, 34 | T2-Day10 |
| Mason Marks | FSU Law | Professor | mason.marks@fsu.edu | Domain 42 (APA analysis) | T2-Day10 — Domain 42 specific |
| ACS Scholars Network | ACS | Via pbrest@acslaw.org | — | Full framework submission | T2-Day7 — institutional |

---

### Civil Rights and Advocacy Organizations (10 contacts)

| Contact | Organization | Role | Contact | Priority Domain | Activation Tag |
|---------|-------------|------|---------|-----------------|---------------|
| Virginia Kase Solomón | Common Cause | CEO | commoncause.org/contact | Domains 1, 2, 3 | T2-Day7 |
| Anthony Romero | ACLU | Executive Director | national@aclu.org | Domains 7, 8, 16 | T2-Day8 |
| Damon T. Hewitt | Lawyers' Committee | President | dhewitt@lawyerscommittee.org | Domains 1, 14, 22 | T2-Day7 |
| Janai Nelson | NAACP LDF | President/Director-Counsel | contact@naacpldf.org | Domains 1, 22, 14 | T2-Day7 |
| Jonathan Greenblatt | ADL | CEO | adl.org/contact | Domain 29, civil society | T2-Day10 |
| Fatima Goss Graves | NWLC | President | nwlc.org/contact | Domains 18, 31 | T2-Day10 |
| Vanita Gupta | Lawyers' Committee | Former head, current advocacy | lawyers committee network | Domain 29, DOJ accountability | T2-Day9 |
| Leah Greenberg / Ezra Levin | Indivisible | Co-Founders | indivisible.org/contact | Resistance meta-analysis | T2-Day8 |
| Josh Orton | Demand Justice | Policy Director | demandjustice.org | Domain 6, 35 | T2-Day9 |
| Becky Bond | Movement orgs advisor | Via network | — | Organizing infrastructure | T2-Day12 |

---

### State Attorneys General and Legislative Staff (8 contacts)

| Contact | State/Office | Role | Contact | Priority Domain | Activation Tag |
|---------|-------------|------|---------|-----------------|---------------|
| Phil Weiser's office | Colorado AG | Voting rights / antitrust | coag.gov | Domains 1, 37, 9 | T2-Day7 — NVRA priority |
| Rob Bonta's office | California AG | Civil rights enforcement | oag.ca.gov/contact | Domains 22, 29, 6 | T2-Day8 |
| Dana Nessel's office | Michigan AG | Election protection | michigan.gov/ag | Domain 37, SAVE Act | T2-Day7 — election priority |
| Bob Ferguson's office | Washington AG | Multistate coalitions | atg.wa.gov | Domains 9, 35 | T2-Day9 |
| Kris Mayes's office | Arizona AG | NVRA enforcement | azag.gov | Domains 37, 1 | T2-Day7 — NVRA priority |
| Josh Kaul's office | Wisconsin AG | Election law | doj.state.wi.us | Domain 37 | T2-Day8 |
| Senate Rules Minority Staff | Sen. Klobuchar | Electoral reform | (202) 224-6352 | Domains 1, 2, 3 | T2-Day9 |
| Senate Judiciary Minority Staff | Sen. Durbin | Judicial accountability | (202) 224-5225 | Domains 6, 29 | T2-Day9 |

---

### Think Tanks and Research Institutions (7 contacts)

| Contact | Organization | Role | Contact | Priority Domain | Activation Tag |
|---------|-------------|------|---------|-----------------|---------------|
| Quinta Jurecic | The Atlantic / Lawfare | Senior Editor | theatlantic.com/contact | Domains 29, 28, 6 | T2-Day7 — media crossover |
| Zack Beauchamp | Vox | Senior Correspondent | vox.com | Full framework | T2-Day8 — media crossover |
| Heidi Shierholz | Economic Policy Institute | President | epi@epi.org | Domains 17, 5, 20 | T2-Day8 |
| Neera Tanden | Center for American Progress | President | americanprogress.org | Full framework | T2-Day10 |
| Cecilia Muñoz | New America | VP | newamerica.org/contact | Domains 16, 18 | T2-Day10 |
| Brookings Governance Studies | Brookings | Program | brookings.edu/contact | Domains 2, 26, 34 | T2-Day10 |
| Roosevelt Institute | Roosevelt | Policy team | rooseveltinstitute.org | Domains 17, 18 | T2-Day10 |

---

### Election Protection Organizations (Phase 1b Tier 2) (5 contacts)

These contacts are specifically for the Domain 37 election track (Trigger 5). They are Phase 1b Tier 2 designates from DOMAIN_37_SEQUENCING_PLAN.md.

| Contact | Organization | Contact | Domain 37 Focus | Activation Tag |
|---------|-------------|---------|-----------------|---------------|
| Sylvia Albert | Common Cause (state division) | commoncause.org | HSGP conditionality | T5-Day16 |
| Eliza Sweren-Becker | Brennan Center (Democracy) | brennancenter.org | NVRA enforcement | T5-Day16 |
| Sarah Walker | ACLU State Affiliates | aclu.org | SAVE Act implementation | T5-Day16 |
| Myrna Pérez | Brennan Center Voting Rights | brennancenter.org | Voter roll litigation | T5-Day16 |
| Wendy Weiser (follow-up) | Brennan Center | wweiser@brennancenter.org | August 7 re-engagement | T5-June1 |

---

**Total secondary contacts available for activation**: 42 identified contacts across all sectors.

---

## 5. Backup Amplification Channels

Activate these channels only if Trigger 4 (Day 14 zero-detection gate) fires. They are not supplements to the primary distribution — they are alternatives to the media-pickup pathway if that pathway has not opened by Day 14.

---

### 5.1 Academic Preprint Submission — SSRN

**Platform**: SSRN (Social Science Research Network) — ssrn.com  
**Category**: Law, Political Science / Political Economy — Democratic Theory subsection  
**Submission format**: PDF of executive summary + full framework (convert Gist to PDF via browser print-to-PDF)

**SSRN filing procedure (estimated time: 45 minutes)**:
1. Create SSRN author account at authors.ssrn.com
2. Upload PDF — set title: "Democratic Institutional Erosion in the United States: A 35-Domain Comparative Framework (2026)"
3. Abstract (use executive summary introduction, 250 words max)
4. Keywords: democratic backsliding, rule of law, comparative constitutional law, electoral integrity, administrative law, NVRA, voting rights
5. Set as "open access" — do not restrict
6. After submission, post the SSRN URL to Twitter/X with thread: "Just uploaded the 35-domain framework to SSRN for academic use and citation. Thread on what's in it: [thread]"

**Expected effect**: SSRN papers in political science and law are indexed by Google Scholar within 48–72 hours of submission. This creates a citable URL that reporters, academics, and policy staff can reference by name. SSRN top-downloads lists in law and political science are watched by law review editors and legal journalists.

**Note on arXiv**: arXiv.org cs.CY (computers and society) accepts policy-adjacent computational work. The litigation tracker could be submitted as a data paper to arXiv cs.CY if presented as a structured dataset. This is a secondary option — SSRN is the primary pathway for legal/policy content.

---

### 5.2 Coalition Briefings — 5–8 Policy Coalitions

If media pickup is zero by Day 14, direct briefings to policy coalitions are the most efficient remaining amplification channel. These coalitions have internal listservs, staff networks, and regular briefings that reach hundreds of practitioners without requiring individual outreach.

**Coalition 1: Democracy Alliance**  
Contact: democracyalliance.org/contact  
Briefing request: "35-domain democratic reform framework available for DA member organizations — request for distribution through DA partner network"  
Domain emphasis: Full framework; emphasize litigation tracker for member funders

**Coalition 2: State Innovation Exchange (SiX)**  
Contact: stateinnovation.org/contact  
Briefing request: State-level domain emphasis (Domains 9, 33, 37, 31) — "state legislator and AG resource"  
Domain emphasis: State autocratization (Domain 33), federalism (Domain 9), NVRA enforcement (Domain 37)

**Coalition 3: Protect Our Care**  
Contact: protectourcare.org  
Briefing request: Healthcare-democracy nexus (Domain 31) for coalition education  
Domain emphasis: Domain 31 (OBBBA Medicaid-NVRA nexus), Domain 18

**Coalition 4: Alliance for Voting Rights**  
Contact: Via NAACP LDF, Brennan Center, Lawyers' Committee VRP coalition infrastructure  
Briefing request: Domain 37 voter roll litigation documentation; NVRA August 7 quiet-period analysis  
Domain emphasis: Domain 37 complete; litigation tracker Category 10

**Coalition 5: Constitutional Accountability Center (CAC) network**  
Contact: theusconstitution.org/contact  
Briefing request: Constitutional litigation framework (Domains 6, 29, 34, 35) for CAC practitioner network  
Domain emphasis: Domains 6, 29, 34, 35

**Coalition 6: Pro-Democracy Policy Network (PDPN) / Issue One**  
Contact: issueonemn.org/contact  
Briefing request: Anti-corruption and democratic accountability framing (Domain 26)  
Domain emphasis: Domain 26 (anti-corruption), Domain 2 (civil service)

**Coalition 7: Economic Analysis and Research Network (EARN)**  
Contact: earncentral.org  
Briefing request: Labor and economic democracy framing (Domain 17, 18) for state policy staff  
Domain emphasis: Domains 17 (sectoral bargaining), 18 (economic inequality), 23 (tariff unilateralism)

**Coalition 8: Movement Voter Project network**  
Contact: movementvoterproject.org  
Briefing request: Organizing infrastructure framing for grassroots coalition distribution  
Domain emphasis: Resistance meta-analysis; Domain 7 (participation rights); Domain 37 (election protection)

---

### 5.3 Local Media and State-Level Outreach

If national media pickup is zero by Day 14, state-level outlets are lower-threshold entry points. State-level coverage also has direct policy value: state AG offices and state legislatures read state publications more reliably than national outlets.

**State outlets to target (prioritize states with active Domain 37 AG contacts)**:

| State | Outlet | Beat Reporter Target | Domain Hook |
|-------|--------|---------------------|-------------|
| Colorado | Colorado Sun | Democracy/politics beat | Domain 37 NVRA; Weiser Colorado connections |
| Michigan | Bridge Michigan | Elections and politics | SAVE Act 81% false positive Michigan impact |
| Wisconsin | Wisconsin Examiner | Courts and democracy | Domain 37 DOJ voter roll cases in 7th Circuit |
| Arizona | Arizona Mirror | Voting rights | SAVE Act implementation; Kris Mayes AG connection |
| Pennsylvania | Pennsylvania Capital-Star | Judicial independence | Domain 6 circuit vacancy analysis |
| Georgia | Georgia Recorder | Civil rights / elections | Domain 22, Domain 1 redistricting cascade |

**State-level pitch template (2–3 sentences)**:

> I'm an independent researcher who has documented [specific state-relevant finding, e.g., "the 81% false positive rate of the SAVE Act's citizenship verification mechanism and its projected impact on [State] voter rolls"]. The full analysis is available at [Gist URL] under Creative Commons license. I'd be happy to walk through the [State]-specific data if you're interested in covering the [specific issue] angle.

---

### 5.4 Pre-Written Press Pitch (Trigger 4 Media Activation)

For the 500-word press pitch referenced in Trigger 4, use this template. Customize the opening sentence with the most recent new development (a court filing, a new Domain 42 participant, or a new NVRA data point).

**Subject**: Research alert: 24 active DOJ voter roll cases — systematic documentation for [journalist name/outlet]

---

I'm an independent researcher who has spent two years building a 35-domain comparative framework on democratic institutional erosion. The most time-sensitive finding is one I am not seeing covered systematically: there are 24 active Department of Justice lawsuits targeting voter rolls, coordinated across five federal circuits, all filed since January 2025.

The significance is in the August 7 date: 52 U.S.C. § 20507(c)(2), the NVRA's quiet period provision, prohibits systematic voter roll removals in the 90 days before a federal election. August 7 is the start of that quiet period for November 2026. Several of the 24 active DOJ cases are structured to complete voter roll removals before that date activates.

The documentation is primary-source only: court filings, congressional records, official government documents, peer-reviewed research. It's published under Creative Commons Attribution 4.0 at [Gist URL for Domain 37 + main framework URL].

Three specific data points:

1. The SAVE Act citizenship verification mechanism has an 81% false positive rate in the states where it has been applied — meaning 8 in 10 flagged voters are in fact eligible citizens.

2. Eight named election-denier officials currently hold senior positions in DHS and DOJ agencies with direct authority over election administration.

3. The HSGP (Homeland Security Grant Program) conditionality mechanism allows federal withholding of state election security funds from states that resist voter roll challenge frameworks — creating a financial incentive structure for state cooperation with federal voter roll activities.

The full 35-domain framework, executive summary, and litigation tracker are at [URLs]. I'm available for background conversation or on-the-record comment.

[Your name and contact information]

---

## 6. Outcome Communication Frameworks

If Phase 1 participation is lower than expected at the Day 21 (June 4) review, the following frames provide accurate, non-defeatist characterizations of the outcome for any stakeholders, partners, or collaborators who ask for a Phase 1 assessment.

---

### 6.1 "Phase 1 Foundation" Frame

**When to use**: When a collaborator or potential partner asks about Phase 1 response and the overall reply rate is below the 30% target.

**Core framing principle**: Phase 1 is the distribution and credibility-establishment phase. Its function is to place high-quality documentation in the hands of the highest-leverage contacts before Phase 2 amplification. Any contact who received the framework — regardless of whether they replied — now has access to documentation they can use in their own work. That is a permanent, non-reversible outcome.

**Language**:

> Phase 1 placed the 35-domain framework with [number] researchers, lawyers, advocates, and policy staff across [number] organizations. We received [number] substantive engagements, including [one specific positive signal — even if small: a request for a domain extract, a forwarding event, a positive acknowledgment]. Phase 2, planned for August, expands the coalition and adds [specific Phase 2 element: e.g., additional domains, direct AG briefings, preprint citation network]. Phase 1's primary function was to establish the research in the institutional memory of key organizations — that work is complete.

---

### 6.2 Emphasizing Small Signals

**When to use**: When even small signals exist (one reply, one Substack subscriber from an org, one social share from a Tier 1 contact) and a stakeholder is asking for evidence that the outreach worked.

**Principle**: In policy research distribution, a single high-quality signal from the right person is worth more than dozens of low-quality signals. A reply from Marc Elias asking one question is a policy-circuit signal. A Substack share from Erica Chenoweth reaches every Nonviolent Action Lab researcher in her network.

**Language**:

> The most significant signal from Phase 1 was [specific signal in plain language]. In policy research distribution, the credibility signal that matters is not volume — it is whether the research is in the institutional awareness of organizations that will cite it, litigate with it, or build on it in the next 12–18 months. [Signal] indicates the framework is in that pathway. Phase 2 is designed to accelerate that trajectory.

---

### 6.3 Phase 2 August Amplification Frame

**When to use**: In all Phase 1 assessment communications where Phase 2 planning is relevant.

**Key elements**:
- Phase 2 is not a restart — it is a second wave with a larger coalition and updated domains
- The August 7 NVRA deadline creates a hard-anchored organizing moment that will generate media and organizational attention independent of Phase 1 traction
- Any engagement from Phase 1, however small, becomes a credibility anchor for Phase 2 outreach ("Since Phase 1, we have engaged with [org] and [org]...")

**Language**:

> Phase 2 is planned for [July–August], timed to the August 7 NVRA quiet-period start. That deadline is a hard external anchor that will generate organizational attention regardless of Phase 1 traction — any election protection organization active in voter roll litigation will be focused on it. Phase 1 contacts who did not engage in May have an August 7-specific reason to engage in July. Phase 2 outreach will reference Phase 1 distribution and add the domain content updates produced since May.

---

## 7. Activation Procedure — Day-by-Day Checklist

This checklist assumes Phase 1 launch on May 14–15 (Batch 1 send). All day references are calendar days from launch. Execute only the steps corresponding to your current day. Check each step before proceeding.

---

**Day 0 (May 14–15) — Launch**

[ ] Batch 1 sent: Weiser, Elias, Goodman, Chenoweth, Bassin (in the updated priority order from BATCH_1_CONTACT_LOG.md)  
[ ] BATCH_1_CONTACT_LOG.md updated with send timestamps  
[ ] Google Alerts configured for: "Democratic Renewal Research Framework" | "NVRA quiet period August 7" | "SAVE Act false positive" | "Domain 42 DEA regulatory capture" | "35-domain"  
[ ] This document open and bookmarked — contingency review scheduled for Day 3  
[ ] Phase 1b Tier 1 personalization in progress (7 election org emails for Day 1 PM send)

---

**Day 3 (May 17) — Trigger 1 Assessment**

[ ] Count Batch 1 substantive replies received  
[ ] IF replies ≥ 1 substantive: no action required, proceed normally  
[ ] IF replies = 0 or 1 acknowledgment-only:  
  - [ ] Verify all 5 Batch 1 sends landed: check sent folder, check for bounces  
  - [ ] Review address list against BATCH_1_CONTACT_LOG.md verified emails  
  - [ ] If any address shows as bounced: resend with revised subject (Section 3.1) within 24 hours  
  - [ ] Log Trigger 1 assessment in DISTRIBUTION_EXECUTION_LOG.md  
[ ] Substack Post 1 publishes today — share on Twitter and LinkedIn  
[ ] Domain 42 Category D state AG outreach today (Colorado, California, Michigan, Washington AGs)

---

**Day 7 (May 21) — Trigger 2 Assessment**

[ ] Count all substantive replies to date (Batch 1 + Phase 1b Tier 1 + Domain 42 Category A–B)  
[ ] Count total emails sent to date (approximate: 17–22)  
[ ] Calculate cumulative reply rate  
[ ] IF reply rate ≥ 12%: no action required, proceed with Wave 2 Batch 1 today as planned  
[ ] IF reply rate < 12%:  
  - [ ] Activate secondary contact pool: identify 5–7 contacts from Section 4, tag for Day 10+ sends  
  - [ ] Revise Wave 2 subject lines using Section 3.2 variants appropriate to each sector  
  - [ ] Log Trigger 2 activation in DISTRIBUTION_EXECUTION_LOG.md  
  - [ ] Do not send Wave 3 until at least one Wave 2 substantive reply received  
[ ] Phase 1b Day 7 checkpoint: any Domain 37 follow-up requests from Tier 1 election orgs?

---

**Day 10 (May 24) — Trigger 3 Assessment**

[ ] Count organizations showing Category 3+ engagement signal  
[ ] IF ≥ 1 organization at Category 3+: credibility anchor exists for Wave 3 opens — proceed normally  
[ ] IF zero organizations at Category 3+:  
  - [ ] Revise Wave 3 email openers: remove credibility-anchor references, replace with standalone domain data hooks (see Section 3.3 for civil rights framing; adapt for other sectors)  
  - [ ] Send one Trigger 3 follow-up to the most promising non-responsive Batch 1 contact using Section 3.5 template  
  - [ ] Activate 2 additional secondary contacts from Section 4, prioritizing those tagged T2-Day10  
  - [ ] Log Trigger 3 status in DISTRIBUTION_EXECUTION_LOG.md  
[ ] Twitter Thread 3 today; Substack Post 3 today (Domains 7–22 synthesis)

---

**Day 14 (May 28) — Trigger 4 Assessment**

[ ] Check Google Alerts: any external media mentions?  
[ ] Check regulations.gov Docket DEA-1362: any participation notices filed that reference democratic design, regulatory capture, or Domain 42 framing?  
[ ] IF external mentions ≥ 1 OR Domain 42 participation notices ≥ 1: log as Phase 1 media signal; no further amplification action required today  
[ ] IF external mentions = 0 AND Domain 42 notices = 0 or 1:  
  - [ ] Upload executive summary to SSRN within 48 hours (Section 5.1 procedure)  
  - [ ] Draft 500-word press pitch from Section 5.4, customize opening sentence with most recent new development  
  - [ ] Identify first coalition briefing target from Section 5.2 — request by email today  
  - [ ] Log Trigger 4 activation in DISTRIBUTION_EXECUTION_LOG.md  
[ ] Log final Domain 42 tracking: which organizations filed, what framing did they use  
[ ] DEA hard deadline closes at midnight — no further Domain 42 outreach possible after today

---

**Day 16 (May 30) — Trigger 5 Assessment (Election Track)**

[ ] Count Phase 1b replies to date from 7 Tier 1 election protection orgs  
[ ] IF ≥ 1 substantive reply from any Phase 1b Tier 1 contact: log as election-track signal; plan August 7 re-engagement  
[ ] IF zero replies from all 7 Phase 1b Tier 1 contacts:  
  - [ ] Log as "consent decree window closed without confirmed election-org engagement"  
  - [ ] Draft August 7 NVRA follow-up using Trigger 5 language from Section 2  
  - [ ] Schedule Phase 1b Tier 1 follow-up sends for May 31–June 2  
  - [ ] Activate 3–5 Phase 1b Tier 2 contacts from Section 4 for June outreach  
  - [ ] Log Trigger 5 status in DISTRIBUTION_EXECUTION_LOG.md  
[ ] Document all Domain 37 engagement signals (even small: open notifications, any reply) as Phase 2 August re-engagement baseline

---

**Day 21 (June 4) — Phase 1 Complete Assessment**

[ ] Calculate aggregate response rates against targets:
  - Wave 1 target: 40–60% (minimum viable: 20%)
  - Wave 2 target: 25–40% (minimum viable: 10%)
  - Wave 3 target: 15–25% (this is expected range, not a contingency trigger)
  - Phase 1b target: 25–40% (minimum viable: 15%)
[ ] Record total adoption signals (Categories 3–6)  
[ ] Record total media mentions  
[ ] Draft Phase 1 outcome summary using Section 6 framing  
[ ] Log Phase 1 complete in WORKLOG.md  
[ ] Begin Phase 2 planning: identify August 7-specific contacts, confirm additional domains for Phase 2 release  

---

## Sources

- [M+R Benchmarks 2026 — Nonprofit advocacy email engagement rates](https://mrbenchmarks.com/email-messaging/)
- [M+R Benchmarks 2026 — Main report](https://mrbenchmarks.com/)
- [Average Cold Email Response Rates 2025 — Mailforge](https://www.mailforge.ai/blog/average-cold-email-response-rates)
- [40+ Cold Email Statistics For 2026 — Growth List](https://growthlist.co/cold-email-statistics/)
- [Cold Email Reply-Rate Benchmarks 2025 — The Digital Bloom](https://thedigitalbloom.com/learn/cold-outbound-reply-rate-benchmarks/)
- [State of Email Outreach 2026 Report — Hunter.io](https://hunter.io/the-state-of-cold-email)
- [Promotion of Scientific Publications on ArXiv and X — arXiv paper](https://arxiv.org/html/2401.11116v1)
- [SSRN Social Science Research Network](https://www.ssrn.com/ssrn/)
- [Advocacy engagement is getting harder in 2026 — Newmode](https://www.newmode.net/blog/advocacy-engagement-is-getting-harder-in-2026.-heres-what-to-do-about-it)
- [Instantly.ai cold email reply rate benchmarks](https://instantly.ai/blog/cold-email-reply-rate-benchmarks/)

---

## 8. International Advocacy Amplification Hook (Trigger 4 Supplement)

This section supplements Section 5.2 (Coalition Briefings) with international advocacy organizations that carry a distinct legitimacy frame — useful when domestic media and coalition pathways have not activated by Day 14. International citations of U.S. democratic erosion create a different credibility signal than domestic coverage: they position the research within a global democratic backsliding literature and reach audiences (OECD governments, European policy networks, international media) that domestic think tanks cannot reach.

**When to activate**: Trigger 4 fires (Day 14, zero media pickup) and domestic coalition briefings are either in progress or have not responded within 5 days.

---

### 8.1 IFES — International Foundation for Electoral Systems

**Contact**: ifes@ifes.org | ifes.org/contact  
**Relevance**: IFES advises election administration in 40+ countries. Their staff includes technical experts who regularly review U.S. election systems as a comparative benchmark for work in other democracies. A U.S. researcher citing the same international evidence they use (German Federal Returning Officer, Elections Canada, Electoral Commission UK) is a peer-to-peer research engagement, not an external pitch.  
**Domain focus**: Domain 37 (five-mechanism federal interference infrastructure, CISA destruction, EAC capture), Domain 37b (state election security — ES&S/Liberty Vote vendor concentration, RLA adoption map), Domain 1 (NVRA analysis, SAVE Act false positive rate).  

**Email template**:

> Subject: U.S. election security documentation — comparative benchmarks for IFES program staff
>
> Dear IFES staff,
>
> I am an independent researcher who has documented the structural changes to U.S. federal election security infrastructure since January 2025, using primary sources and the same international comparative benchmarks IFES uses in its technical assistance work.
>
> The specific areas where my documentation may intersect with your program work:
>
> - CISA election security funding: confirmed $39.6M elimination and FY2027 $707M proposal documentation with source citations
> - Election denier personnel in EAC and DHS: eight named senior officials with sourced appointment records
> - Vendor concentration risk: ES&S/Hart InterCivic/Liberty Vote controlling approximately 90% of voting equipment market, including the Liberty Vote acquisition completed without security review
>
> The full documentation is at [bit.ly/drp-2026]. Domain 37 is the election-security-specific section; Domain 37b covers state-level security architecture in depth.
>
> I would welcome the opportunity to discuss whether any of this documentation is useful for IFES's comparative analysis of U.S. election administration, or whether it belongs in any program staff's reading files.
>
> [Your name and contact information]

**Expected timeline**: IFES is a mid-size organization with a responsive program staff. Expect a 5–14 day response cycle. This is a Day 14+ channel — start it on Day 14, do not wait for a response before activating domestic channels.

---

### 8.2 International Republican Institute (IRI)

**Contact**: iri.org/contact  
**Relevance**: IRI is a democracy assistance organization with bipartisan credibility that advises civil service reform and democratic institution-building globally. Engaging IRI signals cross-partisan institutional concern — the framework is not positioned as progressive advocacy but as comparative institutional documentation.  
**Domain focus**: Domain 2 (Schedule F and civil service resilience), domain-civil-service-resilience (cross-domain synthesis), Domain 26 (accountability infrastructure).  

**Email template**:

> Subject: U.S. civil service accountability documentation — comparative institutional analysis
>
> Dear IRI program staff,
>
> I have documented the structural changes to U.S. civil service accountability mechanisms since January 2025, drawing on comparative international evidence from OECD merit system research and the Westminster model's Senior Executive Service architecture.
>
> The documentation addresses the Schedule F reclassification mechanism and its effect on merit-based career protections — an area where IRI's international civil service reform work has direct comparative relevance. The international benchmarks I have used (New Zealand State Services Commission, German Federal Personnel Act, Canada's Public Service Employment Act) are the same evidence base IRI uses in program design for partner countries.
>
> My question: Is U.S. civil service resilience something IRI program staff are currently analyzing as a comparative benchmark case? If so, I would welcome the opportunity to share the documentation and hear whether the framing is consistent with IRI's institutional analysis.
>
> Full framework: [bit.ly/drp-2026]
>
> [Your name and contact information]

---

### 8.3 Human Rights Watch — Americas Division

**Contact**: hrw.org/about/contact | press@hrw.org (media inquiries)  
**Relevance**: HRW publishes annual U.S. country reports. If any framework documentation reaches their Americas researcher, it can influence their reporting cycle. HRW citations carry international legitimacy that domestic citations cannot replicate.  
**Domain focus**: Domain 16 (immigration enforcement), Domain 29 (prosecutorial weaponization — SPLC indictment), Domain 7 (rights protection), Domain 22 (racial justice).  

**Email template**:

> Subject: Documentation for U.S. country reporting — prosecutorial weaponization and immigration enforcement
>
> Dear HRW Americas team,
>
> I have compiled primary-source documentation of prosecutorial weaponization and immigration enforcement patterns in the U.S. since January 2025, relevant to HRW's ongoing U.S. country monitoring work.
>
> Two areas where this documentation may be most useful for your team:
>
> - Domain 29: 22-case retaliatory prosecution pattern, including the April 21, 2026 SPLC indictment — this is documented to the charging document, case filings, and the ACLU/LDF mutual defense response
> - Domain 16: immigration enforcement documentation including the ICE detention expansion, judicial deference erosion, and the constitutional due process framework under active litigation
>
> The documentation is primary-source only and uses HRW's own evidentiary standard for political prosecution (legal basis, timing correlation to political activity, comparison to similarly situated non-political actors).
>
> Full documentation: [bit.ly/drp-2026]
>
> I am available to discuss any section of the documentation that would be useful for HRW's U.S. country reporting.
>
> [Your name and contact information]

---

### 8.4 Amnesty International USA

**Contact**: aiusa.org/contact | media@aiusa.org  
**Relevance**: Parallel to HRW — international legitimacy frame. AIUSA focuses more on individual cases and rights protection frameworks; HRW focuses more on systemic documentation. Both channels are worth activating if Trigger 4 fires.  
**Domain focus**: Domain 7 (rights protection infrastructure), Domain 16 (immigration enforcement), Domain 29 (prosecutorial weaponization).  

**Email template**: Use the HRW template above with one modification — replace HRW-specific language with: "I am reaching out to AIUSA because [Domain 7 / Domain 29 documentation] may be relevant to your U.S. rights protection monitoring work, particularly the [specific current AIUSA campaign area, if known, or: 'prosecutorial accountability and immigration enforcement' framing that AIUSA has used in recent country monitoring]."

---

### 8.5 Activation Decision Tree for International Channels

```
Trigger 4 fires (Day 14 — zero media pickup):
│
├── Are domestic coalition briefings (Section 5.2) already sent?
│   ├── YES → Activate international channels in parallel (same day)
│   └── NO → Send domestic coalition briefings first; start international
│            channels Day 15–16 if no response within 48 hours
│
├── Priority order for international channel activation:
│   1. IFES (election administration — most direct domain overlap)
│   2. Human Rights Watch (country reporting — broadest institutional credibility)
│   3. IRI (civil service — cross-partisan legitimacy signal)
│   4. Amnesty International USA (rights protection — parallel to HRW)
│
├── Timeline to response:
│   - IFES: 5–14 days
│   - HRW Americas: 7–21 days (country reporters have long lead times)
│   - IRI: 5–14 days
│   - AIUSA: 7–14 days
│
└── What a positive international response enables:
    - An IFES engagement creates a citation reference usable in Phase 2 outreach
      to all election security contacts ("IFES program staff are reviewing the
      Domain 37 election security documentation")
    - A HRW response creates a pathway to their U.S. country report
    - An IRI engagement creates a cross-partisan institutional credibility anchor
      for any Senate-staff outreach in Phase 2
```

---

## 9. Tier 2 Activation Scenario Matrix — Full Decision Trees

This section provides explicit decision trees for Tier 2 contact activation, keyed to the underperformance scenarios identified in Section 2. The contacts named here are drawn from Section 4 (secondary contact pool) and are organized by the specific scenario that warrants their activation.

### 9.1 Scenario: Law School Sector Silence at Day 14

**Condition**: All law school contacts (Batch 2: Stephanopoulos, Shams, Balkin, Gerken, Chemerinsky, Hasen) have produced zero replies by Day 14.

**Decision tree**:

```
Law school silence at Day 14:
│
├── Check: Did any law school contact show Bitly clicks without replying?
│   ├── YES → Email landed, ask is failing. Send one follow-up using
│   │         the "Clinic Resource Frame" from Section 3.2 Variant B.
│   │         Target: Hasen (UCLA) and Stephanopoulos (Harvard) first —
│   │         both are most actively publishing in the election law space.
│   └── NO → Zero engagement. Either email is not landing or contacts
│            are genuinely not reading. Switch channel.
│
├── Channel switch for law schools (if zero clicks):
│   1. Georgetown Law ICAP: icap.georgetown.edu/contact
│      → Frame as "constitutional accountability documentation for ICAP's
│        litigation support work" — ICAP is operationally focused, faster
│        response cycle than academic faculty
│   2. ACS Scholars Network: pbrest@acslaw.org
│      → Frame as "ACS member-facing research resource" — institutional
│        distribution through ACS reaches 100+ law school chapters
│   3. Duke Law CLRP: law.duke.edu/clrp/
│      → Domain 22 and Domain 1 entry point
│
└── Timeline: Send Tier 2 law school contacts Day 14–16.
    Do not wait for law school Tier 1 response before activating.
    Law school response cycles are 21–42 days (longer than other sectors).
```

---

### 9.2 Scenario: Civil Rights Sector Underperformance at Day 10

**Condition**: Fewer than 2 civil rights organization contacts have replied by Day 10.

**Decision tree**:

```
Civil rights underperformance at Day 10:
│
├── Which contacts are silent?
│   ├── NAACP LDF and Lawyers' Committee VRP both silent?
│   │   → These are the two highest-priority contacts. Something structural.
│   │   → Check: Are the contacts still in their roles?
│   │     (LDF: Janai Nelson as President; Lawyers' Committee: Damon Hewitt)
│   │   → If in role: send follow-up using "Litigation Coordination Frame"
│   │     (Section 3.3 Variant A), referencing the most recent active case
│   │     their organization has filed (check their website same day)
│   │
│   └── ACLU VRA silent but civil rights contacts replied?
│       → Domain 37 Phase 1b specific issue. Send ACLU VRA the August 7
│         NVRA analysis extract as a standalone document — not the full
│         framework. Subject: "SAVE Act 81% false positive — NVRA quiet
│         period documentation for VRA team"
│
├── Tier 2 civil rights contacts for Day 10+ activation:
│   1. UnidosUS: unidosus.org/about-us/contact
│      → Domains 16, 18, 22 — large member reach, rapid internal distribution
│   2. Damon T. Hewitt (Lawyers' Committee) follow-up to dhewitt@lawyerscommittee.org
│      → If original email went to general VRP address, try direct to Hewitt
│   3. Color of Change: colorofchange.org/about/contact
│      → Domains 22, 29 — digital-native advocacy, faster response cycle
│
└── Escalation note: If zero civil rights replies by Day 14, activate
    Human Rights Watch (Section 8.3) and AFL-CIO (Section 5.2) in parallel —
    the labor-civil rights nexus (Domain 22 cross-reference to Domain 17)
    creates a coalition pathway even without direct civil rights org engagement.
```

---

### 9.3 Scenario: Labor Union Complete Silence at Day 14

**Condition**: AFL-CIO and SEIU contacts have produced zero replies, zero Bitly clicks, by Day 14.

**Decision tree**:

```
Labor silence at Day 14:
│
├── Labor union staff are high-volume recipients of policy research.
│   Zero clicks at Day 14 almost always means one of three things:
│   (a) Email routed to a communications department that does not forward
│   (b) Contact is no longer in the role listed
│   (c) Domain 17 framing is too academic for their intake process
│
├── Diagnosis step: Check AFL-CIO and SEIU "Government Affairs" or
│   "Policy" staff listings on their current websites.
│   Are the names you emailed still in those roles?
│
├── If contacts have changed:
│   → Update with current government affairs/policy staff name
│   → Resend with revised subject: "[Union name] — PRO Act research update"
│     (shorter, more specific, uses language their staff uses)
│
├── If contacts are current (email is just not converting):
│   → Switch channel: call (202) area code government affairs office directly
│   → 5-minute phone call with a specific question: "I have research on the
│     NLRB capture timeline that may be useful for PRO Act testimony — can I
│     send it to the right policy staff person?"
│
├── Tier 2 labor contacts for Day 14+ activation:
│   1. CWA (Communications Workers): cwa-union.org/contact
│      → Domain 8 (media workers) + Domain 17 — CWA represents media workers
│        and tech workers; this is a more specific domain alignment than AFL-CIO
│   2. UAW: uaw.org/contact
│      → Domain 17 + Domain 23 (tariff/auto supply chain) — highly specific
│   3. AFSCME: afscme.org/contact
│      → Domain 2 (civil service/Schedule F directly threatens AFSCME members)
│        — this is the most specific domain-to-union alignment in the framework
│
└── AFSCME is the highest-priority Tier 2 labor contact:
    Schedule F directly threatens AFSCME members' civil service protections.
    The ask is not "review this framework" — it is "Schedule F eliminates
    the civil service protections your members rely on; here is the statutory
    analysis." That is an interest-alignment pitch, not a research pitch.
```

---

### 9.4 Summary Activation Table — Tier 2 by Scenario and Day

| Underperformance Scenario | Day to Activate | Priority Tier 2 Contacts (in order) |
|--------------------------|----------------|-------------------------------------|
| Law school sector silence | Day 14 | Georgetown ICAP, ACS Scholars, Duke CLRP |
| Civil rights sector < 2 replies | Day 10 | UnidosUS, Color of Change, LDF Hewitt direct |
| Labor complete silence | Day 14 | AFSCME, CWA, UAW |
| Think tank silence | Day 14 | Niskanen Center, Bipartisan Policy Center, Federation of American Scientists |
| Zero media pickup | Day 14 | Democracy Fund, New America, state outlets (Section 5.3) |
| Domain 42 zero participation | Day 10 | Prison Policy Initiative, Drug Policy Reform Network, FAMM |
| Election protection zero | Day 16 | Eliza Sweren-Becker (Brennan Center), Myrna Pérez (Brennan Center), Sarah Walker (ACLU affiliates) |
| All sectors silent | Day 7 | SSRN (Section 5.1) + phone to CAP + phone to Roosevelt Institute |

---

## 10. Final Assessment Framework — May 31 Classification

The May 31 final assessment produces one of three Phase 1 outcome classifications. The classification determines the Phase 2 launch approach and the internal framing narrative.

### Classification Criteria

| Metric | Success | Mixed | Underperformance |
|--------|---------|-------|------------------|
| Cumulative reply rate | ≥ 15% | 8–14% | < 8% |
| Organizational adoption actions (Category 3+) | ≥ 3 | 1–2 | 0 |
| Media mentions | ≥ 1 confirmed | 0 (but Bitly clicks detected) | 0 (zero engagement signals) |
| Domain 42 DEA participation notices | ≥ 2 filed | 1 filed | 0 filed |

**Note on mixed classification**: A contact is Mixed if any two of the four metrics are above their floor threshold. A contact is Underperformance only if all four metrics are at floor. This is intentionally conservative — a single strong signal (e.g., one NAACP LDF reply that is an Integration Request) upgrades the classification even if all other metrics are at floor.

### Phase 2 Implications by Classification

**Success**: Proceed to Phase 2 with standard sequencing. The warm contacts from Phase 1 are the credibility anchors for Phase 2 Wave 1. Frame Phase 2 to new contacts as "building on Phase 1 engagement from [named organizations that replied]."

**Mixed**: Proceed to Phase 2 but adjust the first-wave sequencing — lead with the sectors that showed the highest Phase 1 reply rates, not the highest prestige contacts. If civil rights organizations replied and think tanks did not, Phase 2 Wave 1 goes to civil rights organizations and Tier 2 civil rights contacts, not think tanks. Adjust Phase 2 domain emphasis to lead with the domains that generated Phase 1 engagement.

**Underperformance**: Phase 2 requires a diagnostic reset before launching. The reset involves three questions:
1. Was the failure a delivery problem (fix: re-verify all contact addresses, test email deliverability)?
2. Was the failure a personalization problem (fix: reduce scope of each email to one domain, one finding, one ask)?
3. Was the failure a channel problem (fix: shift primary channel from email to Substack-first distribution, using email as a follow-up to Substack public engagement rather than the initial contact)?

Do not launch Phase 2 with the same approach that produced Underperformance in Phase 1. The diagnostic reset is mandatory.

---

### Outcome Narrative Summaries (Cross-Reference to Section 6)

For full narrative language, see Section 6 above. Summary references:

- **Success**: "Phase 1 established the coalition foundation for Phase 2 scale" — cite specific engagement signals; name organizations that engaged. Avoid hedging. Report the strongest signals prominently.
- **Mixed**: "Phase 1 strengthened policy infrastructure; Phase 2 deepens integration" — identify the specific sectors that engaged and make those the Phase 2 priority. Frame the mixed outcome as calibration data, not failure.
- **Underperformance**: "Phase 1 establishes the knowledge base; Phase 2 targets high-leverage sectors more precisely" — present the diagnostic reset as intentional strategy refinement. Frame the content quality (37 domains, 6 Gists, full measurement infrastructure) as the durable asset. The distribution approach is what is being refined, not the research.

**Universal principle for all narratives**: Never attribute Phase 1 underperformance to content quality. The 37-domain framework is the long-term asset. Distribution approach is a variable that can be refined. Keep these analytically separate in all communication.

---

*Updated: May 15, 2026 (Session 1032, Item 44) — Sections 8–10 added: International advocacy amplification hook (IFES, IRI, HRW, AIUSA), Tier 2 scenario activation decision trees (law schools, civil rights, labor), and May 31 final assessment classification framework. Original document: May 14, 2026.*  
*Status: Production-ready — deploy Day 1, consult only if metric thresholds above are breached.*  
*Primary execution document: PHASE_1_DISTRIBUTION_EXECUTION_BLUEPRINT.md.*
