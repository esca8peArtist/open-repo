---
title: "Tier 1 Success Metrics — Engagement Scoring, Sector Signals, and Tier 2 Candidate Identification"
project: cybersecurity-hardening
created: 2026-05-06
status: production-ready
executor: Anya
cohort-size: 33
sectors: [immigration-legal-aid, community-based-orgs, mutual-aid-networks, digital-rights, academic-cybersecurity, researcher-communities, journalists, civil-rights]
depends-on:
  - TIER1_DISTRIBUTION_PREP.md
  - TIER1_OUTREACH_EXECUTION_PLAN.md
  - TIER2_DISTRIBUTION_PREP.md
  - TIER2_MESSAGING_TEMPLATES.md
  - tier-1-success-metrics-framework.md
  - tier-1-feedback-collection-protocol.md
---

# Tier 1 Success Metrics
## Engagement Scoring, Sector Signals, and Tier 2 Candidate Identification

**Lead finding**: The single most important decision this framework produces is not the final Tier 2 candidate list — it is the Day 7 mid-course correction. Organizations that opened but did not click by Day 7 are recoverable with a subject-line variant. Organizations that received a bounce are recoverable with a corrected address. Organizations that received a hard decline are not recoverable and must be excluded from Tier 2 targeting. That Day 7 sort, done rigorously, determines whether Tier 2 launches into warm soil or into a list contaminated with dead contacts and alienated declines.

**Cohort**: 33 organizations across three Tier 1 sectors (1A: immigration legal aid, 1B: community-based organizations, 1C: mutual aid networks) plus the 33-organization amplifier cohort (digital rights, academic cybersecurity, researcher communities, journalist organizations). This document covers the engagement mechanics applicable to both cohorts; sector-specific success definitions in Section 2 apply per sector regardless of cohort assignment.

**Key references**:
- Gist URL: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108
- Tier 2 materials: TIER2_DISTRIBUTION_PREP.md, TIER2_MESSAGING_TEMPLATES.md
- Execution runbook: TIER1_OUTREACH_EXECUTION_PLAN.md
- Tracking spreadsheet: tier-1-success-metrics-template.csv (companion file)
- Monitoring schedule: 4-week-monitoring-timeline.md (companion file)

---

## Section 1: Engagement Scoring System

### The 0–5 Scale

Every contact in the cohort carries exactly one engagement score at any moment. The score represents the highest confirmed engagement state for that organization — it does not average across contacts within the same organization or across time periods. Score evolution over time is tracked separately (see Score Trajectory below).

**Score 0 — No contact attempted**
- Definition: Email has been drafted but not yet sent. Organization is in the queue but has not entered the engagement cycle.
- Criteria: No send date recorded in tracker.
- Action: None until send date is logged.

**Score 1 — Sent, no response**
- Definition: Email was sent and delivered (no bounce notification received), but no reply, no Bitly click, and no open signal within the scoring window.
- Criteria: Send date logged + at least 3 days elapsed + no click, reply, or open signal.
- Note: Score 1 is provisional until Day 14. An organization that hasn't responded by Day 14 is confirmed Score 1 (non-responsive cohort). Before Day 14, Score 1 may recover to Score 2 or higher.
- Action: Day 7 check — consider subject-line follow-up if no click by Day 3.

**Score 2 — Open signal with no click**
- Definition: The email was opened (or forwarded to someone who opened a tracked version), but no click on the Bitly link was recorded.
- Criteria: Open indicator present in email tracking tool + no Bitly click. Alternatively: auto-reply or out-of-office message received (confirms delivery and some form of mailbox engagement, but not reading).
- Limitation: Email open tracking is unreliable (image-blocking, preview panes). Score 2 may undercount genuine opens. Do not treat Score 2 as strong signal; treat it as "possibly reading, possibly not."
- Action: Day 7 check — send a one-line follow-up with the Bitly link re-embedded. A Score 2 that converts to a click becomes Score 3.

**Score 3 — Click or initial interest**
- Definition: A Bitly click was recorded, or a reply was received that demonstrates the person read past the subject line (references specific content, asks a specific question, or mentions a specific section of the corpus).
- Criteria: Bitly click logged in analytics dashboard OR reply classified as Question or Request in the reply-type taxonomy (Section 4).
- This is the first score level that represents confirmed reading. A Score 3 means a real person at the organization encountered the corpus.
- Action: Reply immediately. The first reply window (within 24 hours) is the highest-leverage moment in the engagement cycle.

**Score 4 — Integration signal**
- Definition: The organization has taken an action that indicates the corpus is being evaluated for use, not just read as a one-time document.
- Criteria: Any ONE of the following:
  - Reply describes routing the corpus internally ("I'm forwarding this to our legal team / client services director / training coordinator")
  - Organization forwarded the Bitly link to a third party (visible as a new Bitly click from a distinct geographic location or referrer)
  - Reply describes a specific barrier to adoption ("we'd use this but our clients don't have smartphones") — barrier identification means they are actively evaluating fit
  - Reply classified as Integration Signal in reply-type taxonomy (Section 4)
  - Second click from same organization (internal distribution pattern)
- This is a strong positive signal. Score 4 organizations should receive a personalized follow-up within 48 hours that addresses the specific integration context they described.
- Action: Ask Question 2 (which section is most relevant) and begin tracking for Score 5 indicators.

**Score 5 — Active adoption**
- Definition: The organization is using the corpus, not merely reading or evaluating it.
- Criteria: Any ONE of the following:
  - Self-reported adoption ("our intake team is walking clients through Part 0 now")
  - Corpus link appears on the organization's published resource page (web search or screenshot)
  - Organization schedules or confirms a workshop or training using corpus content
  - Organization asks for a follow-up conversation to customize or adapt the corpus for their context
  - Reply classified as Implementation Feedback in reply-type taxonomy (reporting what worked and what didn't from actual use)
  - Organization cites the corpus in a published output (newsletter, brief, resource list)
- Score 5 is the campaign's end state. An organization at Score 5 is a confirmed adoption, not just an engagement. It counts toward the Tier 2 social proof inventory.

### Scoring Rules and Edge Cases

**Auto-responders and out-of-office messages**: Do not upgrade the score. An OOO reply confirms delivery; log the return date and send a fresh copy on that date. The new send restarts the clock.

**Hard bounce (immediate delivery failure)**: Do not assign any score. Flag the contact as Bounce-Unresolved. Investigate within 24 hours: check for typos, search the organization's website for a current general inbox, try an alternative contact method. If corrected and re-sent, start from Score 0 on the corrected contact.

**Hard decline (explicit "not interested")**: Assign Score 1 permanently. Add a Decline flag in the tracker. This contact is excluded from Tier 2 targeting regardless of the organization's subsequent engagement score through other contacts.

**Multiple contacts at same organization**: If two contacts at the same organization are messaged, the organization's score is the highest score across all contacts. If Contact A scores 1 and Contact B scores 4, the organization is at Score 4.

**Forwarded reply from a third party**: If an organization forwarded the corpus and the forwarding recipient replies to you, this counts as a Score 4 signal for the original organization (integration) and creates a new Score 3 contact for the forwarded recipient (who has read past the subject line, since they are now responding).

### Score Trajectory Tracking

A snapshot score is less informative than a score trajectory. An organization that moved 1 → 3 → 4 in five days is more valuable as a Tier 2 candidate than an organization that sat at Score 3 for two weeks with no further movement.

Track trajectory by recording the score at each checkpoint date:
- Day 3 score, Day 7 score, Day 14 score, Day 28 score.

A trajectory of 0 → 1 → 1 → 1 (no movement after Day 3) is a non-responsive contact.
A trajectory of 0 → 3 → 4 → 5 is a high-velocity adoption — prioritize these for Tier 2 pre-contact.
A trajectory of 0 → 1 → 3 → 4 (slow start, then acceleration) may indicate the Day 7 follow-up worked — note which follow-up text triggered the upgrade for use in future campaigns.

**Record trajectory scores in the Notes column of the CSV alongside the current score.** Do not overwrite previous scores — append the new score with the date (e.g., "Day 3: 1 | Day 7: 3 | Day 14: 4").

### Time Windows

| Window | Definition | Action |
|--------|-----------|--------|
| Day 0 | Send date | Log send timestamp |
| Day 3 | First checkpoint | Check Bitly for clicks; check Gmail for bounces, OOOs, declines |
| Day 7 | First follow-up decision point | Send follow-up to Score 0–2 contacts; reply to Score 3–4 contacts |
| Day 14 | Non-response finalization | Score 1 contacts with no engagement by Day 14 enter non-responsive cohort |
| Day 28 | Campaign close | Final engagement scores locked; Tier 2 candidate list generated |

**When is non-response final?** Day 14 is the non-response threshold for standard contacts. Two exceptions apply: (1) Academic program contacts receive a 21-day window because academic email volume and semester scheduling create longer latency. (2) Contacts where the Day 7 follow-up email bounced (wrong address confirmed late) receive a fresh 7-day window from the corrected send date.

---

## Section 2: Institutionally-Specific Success Signals

Each sector has a different institutional rhythm, a different output expectation, and a different observable adoption signal. Applying a uniform threshold misreads both positive and negative signals. The definitions below are calibrated to what is actually observable from an external sender without access to the organization's internal systems.

### Immigration Legal Aid Organizations (1A)

**Success signal hierarchy**:
1. Reply from a named legal staff member (attorney, paralegal, or legal director) that asks a substantive question about the corpus — confirms it reached the right desk, not just the general inbox.
2. Organization confirms routing the corpus to their client services, intake, or training function.
3. Organization confirms they have walked at least one client through Part 0 (data broker opt-outs) or the California DROP platform pathway.
4. Corpus appears on the organization's published resource list or internal practitioner toolkit.
5. Organization cites the corpus in a legal filing, policy brief, or amicus submission.

**What counts as integration signal (Score 4)**: Any routing to a client-facing function, or a reply that describes evaluating the corpus for use in client intake or training.

**What counts as active adoption (Score 5)**: Confirmed client walkthrough (any one client) OR corpus on published resource list. Both require a minimum of one implementation decision, not just evaluation.

**Depth vs. breadth**: A legal aid organization that walks five clients through Part 0 represents deeper adoption than one that shares the Gist URL in a staff newsletter — even though both qualify as Score 5. Track depth in the Notes column: "Score 5 — client walkthroughs (5 reported)" is more valuable than "Score 5 — newsletter mention."

**Timeline to expect signal**: 5–14 days for first reply; 30–60 days for confirmed adoption signal. Legal organizations under current immigration enforcement pressure are processing very high volumes. A 14-day response window is realistic; a 30-day adoption signal window is realistic. Do not close these contacts at Day 14 — send the 30-day follow-up regardless of initial response status.

**Timeline exception**: Organizations in high-enforcement zones (Texas, Arizona, Florida, Georgia) may respond faster due to immediate operational urgency. Organizations in lower-enforcement zones may respond on a slower institutional review cycle.

### Community-Based Organizations Serving Immigrant Communities (1B)

**Success signal hierarchy**:
1. Reply from a community organizer, communications staff, or program director that references specific community members or programs.
2. Organization shares the Gist link in their Signal group, newsletter, or community email list.
3. Organization adapts Part 0 into a handout, workshop, or community education session.
4. Organization translates Part 0 into Spanish or another community language (a uniquely strong adoption signal — translation requires active investment).
5. Organization integrates the corpus into an existing program (community legal education, Know Your Rights sessions, newcomer orientation).

**What counts as integration signal (Score 4)**: Internal distribution to community members (Signal group post, newsletter inclusion, workshop scheduling). Score 4 for community orgs is faster to achieve than for legal orgs because the output channels (Signal, newsletters) are lower-friction than formal policy adoption.

**What counts as active adoption (Score 5)**: Corpus used in at least one community education session, workshop, or Know Your Rights training. Self-report from the organization is sufficient evidence; ask Question 2 (which section) to get specificity.

**Timeline to expect signal**: 7–14 days for first reply; 14–30 days for adoption signal. Community organizations typically move faster than legal organizations because there is no formal review cycle — a community organizer who reads the corpus on a Tuesday can share it at a community meeting on Thursday. Watch for early Score 4 signals from this sector.

**Translation as a proxy for adoption depth**: If a community org mentions working on a Spanish-language adaptation, that is a uniquely strong adoption signal. It requires allocating staff time and indicates the organization considers the corpus worth significant investment. Elevate these contacts to top Tier 2 candidates regardless of other score factors.

### Mutual Aid Networks (1C)

**Success signal hierarchy**:
1. Corpus link shared in a Signal group, Telegram channel, or Discord server affiliated with the network.
2. Network posts Part 0 (data broker opt-outs) as a standalone resource, separated from the full corpus.
3. Network conducts an informal workshop or "security night" using the corpus.
4. Network contacts request a "lighter" version (shorter, more accessible) — indicates they are thinking about distribution to members with limited tech literacy.
5. Network connects you with another network or region that should have the corpus.

**What counts as integration signal (Score 4)**: Direct share in a network channel (confirmation by the contact or by observing the Bitly link appear in a new referrer context). Mutual aid networks often share without notifying the originator — a spike in Bitly clicks from a new geographic area following a send to a mutual aid network is a strong Score 4 indicator.

**What counts as active adoption (Score 5)**: Confirmed community distribution (member feedback reaching you, new contacts reaching out, workshop confirmed). Mutual aid networks generate organic reach faster than any other sector — a single Signal group post can reach 500 people. Organic reach is a Score 5 signal even without a formal adoption process.

**Timeline to expect signal**: 2–7 days for first reply (mutual aid networks have high security culture and respond quickly to security-adjacent content); 7–14 days for adoption signal. This is the fastest-moving sector. If you have not seen a click or reply from any mutual aid contact by Day 7, investigate the contact method (Signal vs. email makes a large difference for this sector).

**Channel preference**: Mutual aid contacts who can be reached via Signal should receive a Signal message, not an email. An email to a Signal-native network has significantly lower open rates. If your tracker shows a mutual aid contact with an email-only method, flag this for a Signal follow-up parallel to the email send.

### Digital Rights Organizations (amplifier cohort)

**Success signal hierarchy**:
1. Reply from a named policy, surveillance, or legal staff member (not a general info@ inbox response).
2. Organization publishes an analysis, blog post, or resource page that cites the corpus's threat model or countermeasures.
3. Organization routes the corpus to a specific team (privacy policy, data broker litigation, immigration surveillance) — a strong routing signal given the specificity of their internal structures.
4. Organization asks for a conversation about the corpus's primary source methodology (indicates they are evaluating it for citation-quality work).
5. Organization incorporates the corpus into published policy campaign material or litigation filings.

**What counts as integration signal (Score 4)**: Named team routing + second contact (the team member reaches out) constitutes Score 4. A generic "we'll pass it along" without follow-up is Score 3.

**What counts as active adoption (Score 5)**: Published citation (blog, report, filing, resource page) OR confirmed training material integration. Both are publicly verifiable.

**Timeline to expect signal**: 7–21 days for first reply; 14–45 days for adoption signal. Digital rights organizations publish quickly but have high inbound volume. Named contacts perform significantly better than generic press@ or info@ inboxes. Organizations like EFF, STOP, and EPIC have specialists whose work directly overlaps the corpus's threat model — if a reply comes from a named specialist (rather than a general communications staffer), that is a strong Score 4 indicator.

### Academic Cybersecurity Programs

**Success signal hierarchy**:
1. Reply from a named faculty member, clinic director, or research lead (not a department administrator).
2. Faculty member asks for a conversation about the corpus's methodology (indicating evaluation for research citation or teaching use).
3. Corpus appears on a course syllabus, clinic resource list, or program reading list.
4. Faculty member cites the corpus in a working paper, presentation, or research note.
5. Corpus cited in a peer-reviewed publication, amicus brief, or formal academic output.

**What counts as integration signal (Score 4)**: A faculty member who initiates a conversation specifically about research or teaching use — this requires a decision to invest time, not just forward an email.

**What counts as active adoption (Score 5)**: Confirmed syllabus inclusion, resource list, or citation. Both are publicly verifiable within a semester.

**Timeline to expect signal**: 21–60 days for first substantive reply; 45–120 days for adoption signal. Academic programs operate on semester cycles. A send in May will not convert academically until fall semester (September–October) for curriculum integration, though research citation can occur on a shorter timeline. Do not mark academic contacts as non-responsive at Day 14. Mark them as "hold — semester boundary" and send a follow-up in late August.

**Exception**: Clinic directors (Harvard Cyberlaw Clinic, law school immigration clinics) operate on a more responsive timeline than research faculty because clinics have active client caseloads. Clinic-directed sends may convert within 14–30 days.

### Journalist Organizations

**Success signal hierarchy**:
1. Reply from a journalist, training coordinator, or press freedom staff member that asks substantive questions about the corpus or its sourcing.
2. Organization integrates Part 0 or the corpus's source-protection section into journalist security training materials.
3. Organization publishes an article, newsletter, or resource referencing the corpus (either as a story or as a resource recommendation).
4. Individual journalist contacts Anya through the corpus's contact channel to request source verification or clarification.
5. Organization recommends the corpus to a journalist working on an enforcement-adjacent story.

**What counts as integration signal (Score 4)**: A training coordinator who asks to schedule a conversation about incorporating the corpus into a training program — this requires scheduling intent, not just reading interest.

**What counts as active adoption (Score 5)**: Confirmed training integration or published reference. Both are verifiable.

**Timeline to expect signal**: 7–14 days for first reply from a journalist or training staff member; 14–45 days for adoption signal. Journalist organizations respond quickly when the content is directly relevant to their members' safety. The June 12 FISA 702 deadline creates urgency around source protection — sends in May 2026 have a timely hook.

### Civil Rights Organizations (if targeted)

**Success signal hierarchy**:
1. Reply from a policy or advocacy staff member that connects the corpus to an active campaign or litigation.
2. Organization incorporates corpus data into a policy brief, coalition communication, or legislative testimony.
3. Organization coordinates with immigration advocacy partners on corpus distribution (coalition coordination).
4. Corpus cited in an amicus brief, regulatory comment, or congressional testimony.
5. Organization adopts corpus recommendations as an organizational policy (staff communications security protocol, client intake security guidance).

**What counts as active adoption (Score 5)**: Published citation in advocacy output, or confirmed policy integration.

**Timeline to expect signal**: 14–30 days for first substantive reply; 30–60 days for adoption signal. Civil rights organizations have slow review cycles for external resources but move quickly when content connects to active litigation or campaign timelines.

---

## Section 3: Early Warning Signs of Non-Engagement

Non-engagement is not failure — it is data. The goal of early warning monitoring is to distinguish between (a) contacts that need a follow-up intervention and (b) contacts that have definitively closed. Acting on the wrong category wastes effort; failing to intervene on recoverable contacts wastes an opportunity.

### Hard-Stop Indicators

**Bounce at 24 hours (Score: 0, flag: Bounce-Unresolved)**
- What happened: The email was undeliverable. The address is invalid, the mailbox is full, or the domain is unreachable.
- Action window: 24 hours from bounce receipt.
- Steps: (1) Check the address for typos against the organization's website. (2) Search the organization's website for an alternative general inbox or contact form. (3) If an alternative is found, re-send and log as a new send. (4) If no alternative found, flag as Bounce-Unresolved and exclude from all follow-up until a valid address is confirmed.
- Do NOT count as Score 1 (sent, no response). A bounced contact never received the email.
- Note: Some immigration legal organizations use web contact forms rather than direct email. A bounced email send does not mean the organization is unreachable — check for a contact form alternative.

**Hard decline at 48 hours (Score: 1 permanent, flag: Decline)**
- What happened: The organization explicitly responded "not interested," "not relevant to our work," "please remove us from your list," or equivalent.
- Action: Immediately log as Decline. Send a one-sentence acknowledgment reply ("Understood — I'll remove you from further outreach. Thank you for your time."). Add a Decline flag in the tracker. This contact is permanently excluded from Tier 2 targeting.
- Do not follow up. Do not add them to the 30-day follow-up wave. Do not contact them through a different contact at the same organization unless you have a compelling new hook and a significant time gap (90+ days minimum).
- Note: A hard decline from a general info@ inbox does not necessarily mean the organization is uninterested — it means the person who checks that inbox is not the right contact. If the corpus is clearly mission-aligned with the organization, one attempt through a different contact (a named staff member rather than the general inbox) is acceptable after 30+ days. Document this in the Notes column before proceeding.

**Zero clicks by Day 3 (Score: 1–2, flag: Low-Interest)**
- What happened: The email was delivered (no bounce) but generated no click on the Bitly link within 72 hours.
- What this means: The email may have been opened but did not generate enough interest to click through, or it was not opened at all. This is the borderline case — recoverable but declining.
- Action: On Day 7, send a one-line follow-up with the Bitly link re-embedded and a more specific subject line. Use the sector-specific subject line variants in TIER2_MESSAGING_TEMPLATES.md as a model for urgency framing. Example: "Following up — June 12 FISA 702 deadline and immigration surveillance update."
- Do not send a follow-up before Day 7. Two messages in three days reads as spam. Wait the full seven days.

**No response by Day 14 (Score: 1 confirmed, cohort: Non-Responsive)**
- What happened: No reply, no click, no open signal for 14 calendar days following the initial send.
- What this means: The contact is non-responsive. This may reflect wrong contact person, buried subject line, organizational capacity constraints, or genuine disinterest. It is not distinguishable from this data alone.
- Action: Mark as Non-Responsive in the tracker. Include in the 30-day follow-up wave only if the 30-day follow-up email has a substantially different hook (not just "checking in again"). A seasonal or event-triggered hook is acceptable (see Recovery Opportunities below).
- Non-responsive contacts are excluded from Tier 2 pre-contact but remain eligible for incidental Tier 2 outreach if they fall within the Tier 2 organizational target list.

### Escalation for Edge Cases

**Small teams with high workloads**: Immigration legal aid organizations and mutual aid networks often have very small staff relative to their organizational footprint. A 21-day non-response from a small-team organization is not equivalent to a 21-day non-response from a large institutional organization. If the organization has a staff list that suggests 3 or fewer people are handling communications, extend the non-response threshold to Day 21 and note the team-size constraint in the tracker.

**Academic calendar boundaries**: For academic programs and law school clinics, outreach sent within two weeks of a semester break (early May, late December, early January) should have the non-response threshold extended to Day 28. Academic contacts during semester breaks have high email backlog. Log the calendar context in the tracker: "Sent during finals week — extend deadline to Day 28."

**Signal-first organizations**: Mutual aid networks that primarily operate on Signal may not check email regularly. If Day 7 shows no click and no reply from a mutual aid contact, send a parallel outreach via Signal before concluding non-response. Signal-first outreach requires the contact's Signal number (not always available) — check the tracker notes for this.

### Recovery Opportunities

Non-responsive contacts are not permanently closed. Three categories of events can trigger late engagement:

**Policy deadline events**: The June 12, 2026 FISA 702 reauthorization deadline is a concrete hook for organizations in the digital rights and journalist sectors. An organization that did not respond to the initial send in May may respond to a follow-up framed around this deadline. Similarly, any major ICE enforcement action (mass detention event, court ruling on ELITE, Inspector General report) creates a re-engagement hook for legal aid and community organizations.

**Seasonal peaks**: Immigration legal aid organizations often see intake spikes in September–October following summer enforcement increases. A follow-up in late August ("as enforcement pressure increases this fall, sharing this resource again") is a legitimate re-engagement frame.

**Referral from a peer organization**: If Organization A adopts the corpus and Organization A has a coalition relationship with Organization B (which did not respond), a warm referral from A to B is the highest-probability recovery mechanism. This requires A's permission and a specific referral chain.

---

## Section 4: Feedback Triage Process

### When Engagement Converts to Response

Every reply to an outreach email must be classified before it is responded to. Classification determines the response template, the follow-up timeline, the score upgrade, and whether the feedback is routed for Phase 2 domain research or documentation improvement.

### Reply Type Taxonomy

**Type 1: Implementation Feedback**
- Definition: The responder has already used the corpus (or had clients use it) and is reporting what worked, what did not work, or what modifications they made.
- Identifiers: Past tense ("we tried," "our clients found," "we adapted"); specific operational detail ("the DROP platform was confusing because of the ID verification step"); references to staff or client experience.
- Score implication: Automatic Score 5. Implementation feedback means adoption has occurred.
- Priority: High. This is the highest-value feedback type. Reply within 12 hours. Ask: (1) What worked? (2) What was difficult? (3) May I share anonymized feedback with other organizations?
- Routing: Log in Notes with full detail. If the feedback identifies a documentation error, a missing step, or a technical gap — route immediately to Phase 2 domain research queue. Example: "California DROP platform path needs clarification on the ID verification step" → add to Phase 2 documentation revision queue.

**Type 2: Critique**
- Definition: The responder has substantive disagreement with a specific claim, methodology, or recommendation in the corpus.
- Identifiers: Conditional language ("I'm not sure this is accurate," "this conflicts with what we've found," "the sourcing here seems weak"); comparison to alternative sources; specific factual correction.
- Score implication: Score 3 (they read it carefully enough to disagree). May upgrade to 4 if the critique indicates ongoing engagement.
- Priority: Medium-High. Critiques from credible sources (attorneys, security researchers, faculty) require verification before a response. Reply within 24 hours with an acknowledgment ("Thank you — I want to review this carefully and get back to you with a substantive response"). Then verify the claim independently and respond within 72 hours.
- Routing: If the critique identifies a factual error → immediate correction in the corpus and acknowledgment in reply. If the critique is a methodological disagreement (not a factual error) → document the disagreement, respond with sourcing, note for Tier 2 messaging adjustment.

**Type 3: Request**
- Definition: The responder asks for something that does not currently exist in the corpus — a domain-specific update, a translated version, a different format, or a customized version for their context.
- Identifiers: "Do you have...," "Would it be possible to...," "We need something that..."; forward-looking; constructive intent.
- Score implication: Score 4. A request indicates the responder has found the corpus relevant to their work and is investing in making it more useful.
- Priority: Medium. Reply within 24 hours. Do not promise delivery timelines you cannot meet. Appropriate responses: "That's on our roadmap for Phase 2 — I'll let you know when it's available" or "I don't have that now, but if you can describe what you'd need specifically, I can include it in the next revision."
- Routing: Log the request in the Phase 2 demand queue. If the same request appears from 3+ organizations → high-priority Phase 2 deliverable. Example: Three organizations request a Spanish-language version of Part 0 → Spanish Part 0 is a confirmed Phase 2 priority.

**Type 4: Integration Signal**
- Definition: The responder explicitly confirms they are using, distributing, or integrating the corpus into their work.
- Identifiers: Present or future tense ("we're sending this to our network," "I'm adding this to our toolkit," "we're planning a workshop using this"); organization name as subject ("our team," "our clients," "our training program").
- Score implication: Score 4 or 5 depending on whether "integrating" means evaluating (Score 4) or confirmed use (Score 5). Ask a clarifying question to distinguish.
- Priority: High. Integration signals are the campaign's target outcome. Reply within 12 hours. Ask: (1) How can I support the integration? (2) Is there anything in the corpus that needs clarification for your specific use case? (3) Would you be willing to share feedback after your team has used it?
- Routing: Add to Tier 2 social proof inventory. With the organization's permission, document the integration for use in Tier 2 outreach ("This resource is in use at [Organization] for client intake" is a powerful credibility signal for Tier 2 recipients).

**Type 5: Question**
- Definition: The responder asks for clarification on a specific claim, procedure, or recommendation without expressing agreement or disagreement.
- Identifiers: Interrogative phrasing ("How does...," "What happens if...," "Is this applicable to..."); neutral or curious tone; references a specific section or step.
- Score implication: Score 3 (confirms reading) upgrading toward 4 if the question indicates evaluation for practical use ("Does this work for our clients who don't have state IDs?").
- Priority: Medium. Questions are engagement signals and should be answered quickly and completely. Reply within 24 hours. Treat each question as an opportunity to move the contact toward Score 4.
- Routing: If the same question appears from 3+ organizations → the corpus has a gap or an unclear section. Add a clarification note to that section in Phase 2 revision queue. Questions that cluster around a specific section indicate that section is generating confusion, which reduces adoption — treat repeated questions as documentation defects.

### Severity and Priority Matrix

| Reply Type | Response Window | Phase 2 Route? | Score Implication |
|-----------|----------------|----------------|-------------------|
| Implementation Feedback | 12 hours | Yes — if gap or error identified | 5 confirmed |
| Critique | 24 hours (acknowledge), 72 hours (substantive) | Yes — if factual error; document if methodological | 3–4 |
| Request | 24 hours | Yes — log in demand queue | 4 |
| Integration Signal | 12 hours | Yes — add to social proof inventory | 4–5 |
| Question | 24 hours | Yes — if question repeats 3+ times | 3 upgrading to 4 |

### Response Templates for Common Feedback Types

**Implementation Feedback response**:
> "Thank you for this — hearing that [specific detail they mentioned] is exactly the kind of ground-truth feedback that's most useful. A few follow-up questions if you have a moment: [1] What part was most difficult for clients to complete? [2] Did any step require clarification or simplification? [3] If you're open to it, may I reference this experience (anonymized) in conversations with other organizations? — [Anya]"

**Critique response (initial)**:
> "Thank you for pushing on this — substantive disagreement is valuable and I want to respond carefully rather than quickly. Let me review your point about [specific issue] and come back to you within the next couple of days with a direct response. I take sourcing seriously and if there's an error I want to correct it." — [Anya]"

**Request response**:
> "Noted, and this is useful. [The Spanish-language version of Part 0 / a format optimized for mobile / a version without smartphone requirements] is something I've heard from several organizations now, which means it's a real gap rather than a corner case. I'll flag this for Phase 2 revision and let you know when it's available. In the meantime, is there anything in the current version I can help you adapt for [your specific context]?" — [Anya]"

**Integration Signal response**:
> "That's great to hear. A few quick questions that would help me support you better: [1] Which section are your clients / staff finding most useful? [2] Is there anything that's creating friction or needs adaptation? [3] If you run into anything that requires clarification as you use it, I'd appreciate hearing about it — ground-level feedback improves the corpus for everyone." — [Anya]"

**Question response**:
> "Good question — [answer the specific question directly and completely, with reference to the relevant section]. If the corpus doesn't make this clear enough, that's a documentation gap I'll fix in the next revision. Is there a follow-up question, or does this address what you needed?" — [Anya]"

---

## Section 5: Tier 2 Candidate Identification

### Defining Tier 2 Readiness

A Tier 2 candidate is a Tier 1 organization whose engagement pattern indicates they are positioned to become an amplifier for the Tier 2 distribution phase, or whose feedback indicates they have specific needs that Tier 2 resources should be designed to address. Tier 2 selection is not about rewarding positive responders — it is about identifying organizations that will actively multiply the corpus's reach.

### Tier 2 Readiness Indicators

**Engagement score threshold**: Score 3 or higher by Day 14. A contact that has clicked through the corpus has confirmed reading intent. Score 3 is the minimum bar for Tier 2 consideration — below this, there is no evidence the contact has engaged with the content.

**Integration signal present**: Score 4 or 5 contacts should be prioritized for Tier 2 pre-contact. An organization that is actively integrating the corpus into their work is the highest-value Tier 2 ambassador — they can provide a credibility endorsement rather than just a referral.

**Cross-sector potential**: An organization that bridges multiple sectors (a digital rights org with strong immigration legal community ties, or an academic program with active clinical law components) is a higher-leverage Tier 2 candidate than an organization with a narrow single-sector focus. Flag cross-sector potential in the Notes column.

**Timing readiness**: A Tier 2 candidate should have completed at least initial review of the Tier 1 corpus before receiving Tier 2 materials. The timing target: Tier 2 outreach should not reach an organization before they have had at least 14 days with the Tier 1 corpus. This prevents Tier 2 materials from overwhelming a contact who has not yet processed Tier 1.

**Network reach**: Tier 2 candidate selection should account for the organization's inherent network reach. CLINIC (400+ affiliate programs nationally) is a higher-leverage Tier 2 target than a local sanctuary network with a regional footprint. Network reach is already partially documented in the per-organization notes in TIER1_DISTRIBUTION_PREP.md.

### Scoring Tier 2 Candidates

Apply a three-factor Tier 2 readiness score (0–3 points, one per factor):

**Factor 1: Engagement depth (0 or 1 point)**
- 0 points: Score 0–2 (no click or confirmed reading)
- 1 point: Score 3–5 (confirmed reading, integration signal, or adoption)

**Factor 2: Integration signal or social proof (0 or 1 point)**
- 0 points: Score 3 only (clicked, no further signal)
- 1 point: Score 4 or 5 (integration signal or confirmed adoption)

**Factor 3: Network multiplier (0 or 1 point)**
- 0 points: Local or regional reach only
- 1 point: National or cross-sector reach (network of 50+ organizations or individuals in direct contact)

**Tier 2 targeting threshold**:
- Score 3/3: Pre-contact before Tier 2 launch — reach out to prime them as ambassadors
- Score 2/3: Standard Tier 2 inclusion — they receive Tier 2 materials as part of the wave
- Score 1/3: Conditional Tier 2 inclusion — only if they fall within the Tier 2 organizational target list and the initial Score 3 engagement was from a confirmed reading (not just a click)
- Score 0/3: Exclude from Tier 2 targeting — no confirmed engagement basis for inclusion

### Hard Exclusions

**Decline-flagged contacts**: Any organization where a contact replied with an explicit "not interested" or "remove from list" is excluded from Tier 2 targeting permanently, regardless of Tier 2 readiness score. This applies to the specific contact; if the organization appears in the Tier 2 target list through a different channel (e.g., they are a Tier 2 organization in TIER2_DISTRIBUTION_PREP.md), use a different contact at the organization and note the prior decline.

**Bounce-Unresolved contacts**: Organizations where no valid email address has been confirmed are excluded until a confirmed address is available.

**Zero-engagement cohort**: Organizations at Score 1 on Day 28 with no click, no reply, and no follow-up engagement across the full 28-day window should not receive Tier 2 outreach through the same contact channel. They may receive Tier 2 materials through a different channel (e.g., if they are on the Tier 2 list via a different contact or if a referral from another Tier 1 org creates a warm introduction).

### The Tier 2 Candidate List

By Day 28, generate the Tier 2 candidate list by running the three-factor scoring against all 33 contacts. The output should be:

- **Pre-contact priority list** (Score 3/3): Organizations to reach before the Tier 2 launch date. Contact these organizations individually, reference their Tier 1 engagement, and ask if they would be willing to review Tier 2 materials and share them within their networks.
- **Standard Tier 2 list** (Score 2/3): Organizations to include in the Tier 2 send wave.
- **Conditional list** (Score 1/3): Organizations to include only if a specific condition is met (confirmed reading verified via a direct question; or warm introduction via a pre-contact list member).
- **Exclude list** (Score 0/3, Decline, Bounce-Unresolved): Organizations excluded from Tier 2 outreach.

Document the list in the CSV tracker under the Tier 2 Candidate? column (Y/N/Conditional) and include the Tier 2 readiness score in the Notes column.

---

## Section 6: Monitoring Timeline — 4-Week Checkpoint Schedule

### Operating Logic

The monitoring schedule has two jobs: (1) catch recoverable failures before they become permanent losses, and (2) accumulate evidence for Tier 2 targeting decisions. The checkpoints are not symmetric — Day 3 is a triage checkpoint, Day 7 is an intervention checkpoint, Day 14 is a finalization checkpoint, and Day 28 is a readout. Each has a different primary question it must answer.

Complete each checkpoint in under 30 minutes total for the full 33-org cohort. If a checkpoint takes longer, the tracker has a design problem — not a data problem.

---

### Day 3 Checkpoint — Triage

**Primary question**: Did the messages get through? Are there any hard failures (bounces, wrong addresses) that need same-week correction?

**Time budget**: 15 minutes. Pull up the tracking CSV and Bitly dashboard simultaneously.

**What to check**:

| Signal | Where to check | Action trigger |
|--------|---------------|----------------|
| Bounce notifications | Gmail inbox, filter `Tier1-Outreach/Bounce` | Any bounce → research alternate contact within 24 hours |
| Bitly click count | bitly.com dashboard, total clicks since launch | Zero clicks after 72 hours → subject line or deliverability issue |
| Early replies | Gmail inbox | Any reply → classify immediately (reply-type taxonomy, Section 4) |
| OOO messages | Gmail inbox, filter `Tier1-Outreach/OOO` | Log return date; schedule re-send for return date |

**Metric targets at Day 3**:

| Metric | Below threshold | On track | Strong |
|--------|----------------|----------|--------|
| Bitly clicks (total) | 0 | 3–8 | 9+ |
| Bounces | 3+ (systemic) | 1–2 | 0 |
| Replies received | 0 | 1–3 | 4+ |
| Score 3+ contacts | 0 | 1–2 | 3+ |

**Decision rules**:
- Zero clicks at Day 3 across all sectors: Stop sends if more remain. Check spam classification for sent emails (send a test to a personal address and verify it lands in inbox, not spam). Check that Bitly short URL is correctly embedded in the email body.
- Two or more bounces: Verify the contact list sources. If bounces cluster in one sector (e.g., all academic emails bouncing), that sector's addresses may have been compiled from outdated sources.
- First replies already at Score 4: Log these as Day 3 anomalies. An organization that signals integration intent within 72 hours of initial contact is a high-velocity candidate for Tier 2 pre-contact. Move to the pre-contact list.

---

### Day 7 Checkpoint — Intervention

**Primary question**: Which contacts are recoverable with a follow-up, and which have definitively closed?

**Time budget**: 25 minutes. Run through all 33 rows; update scores; identify follow-up actions.

**What to check**:

| Signal | Where to check | Action trigger |
|--------|---------------|----------------|
| Score stall at 1–2 | CSV tracker | Send Day 7 follow-up (see template below) |
| New clicks since Day 3 | Bitly dashboard | Update scores for any new clicks |
| Replies not yet classified | Gmail inbox | Classify all pending replies before follow-up sends |
| Score 4–5 contacts | CSV tracker | Personal follow-up within 24 hours |
| OOO return dates reached | OOO log | Send fresh copy on return date |

**Metric targets at Day 7**:

| Metric | Below threshold | On track | Strong |
|--------|----------------|----------|--------|
| Cumulative Bitly clicks | Under 5 | 8–15 | 16+ |
| Score 3+ contacts | 1 | 3–6 | 7+ |
| Score 4–5 contacts | 0 | 1–3 | 4+ |
| Replies received (cumulative) | Under 3 | 5–9 | 10+ |
| Declines | 3+ | 1–2 | 0 |

**Day 7 follow-up template** (for Score 0–2 contacts where no reply or click has been received):

> Subject: Following up — [specific hook for their sector]
>
> Hi [name / team],
>
> Briefly following up on the message I sent [Day 0 date] about the ICE/Palantir ELITE threat model and countermeasures guide.
>
> [Sector-specific hook sentence]:
> - Digital rights: "With the June 12 FISA 702 deadline approaching, the surveillance integration angle may be timely for your policy work."
> - Academic: "A colleague suggested your program's research focus on [surveillance/privacy/security] might make this worth a look."
> - Journalists: "Source protection pressure is increasing with the FISA renewal timeline — the source protection section may be directly relevant."
> - Researcher communities: "The Palantir ELITE contract documentation might be worth a second look if you work on commercial surveillance or law enforcement data pipelines."
>
> The corpus is at [Bitly URL]. Happy to answer questions if it's relevant to your work.
>
> [Anya]

**Decision rules**:
- Score 4+ contacts at Day 7 should not receive the generic follow-up template. They should receive a personal reply that references what they said or did ("Thanks for routing this to your policy team — wanted to make sure [specific question] is answered").
- Decline-flagged contacts: Do not send the Day 7 follow-up. Log as permanently closed.
- Score 0 contacts with no bounce: Eligible for Day 7 follow-up regardless of click history. The first message may have been received but not acted on; a follow-up with a different hook sometimes converts.

---

### Day 14 Checkpoint — Non-Response Finalization

**Primary question**: Which contacts are definitively non-responsive and can be excluded from Tier 2 pre-contact, and which Score 3–5 contacts are showing enough momentum to begin Tier 2 prep?

**Time budget**: 30 minutes. This is the most consequential checkpoint — decisions made here determine the Tier 2 pre-contact list.

**What to check**:

| Signal | Where to check | Action trigger |
|--------|---------------|----------------|
| Score stall at 1 since Day 3 | CSV tracker | Flag as Non-Responsive; exclude from Tier 2 pre-contact |
| Score trajectory acceleration (1→3→4) | Score trajectory column | Flag as high-velocity; prep personalized Tier 2 pre-contact |
| Feedback in queue | Gmail inbox | Clear all pending replies before reporting |
| Phase 2 demand queue | Notes column | Any requests or repeated questions logged for Phase 2 revision |
| Correction-eligible bounces | Bounce log | Final attempt at alternate contact for Bounce-Unresolved |

**Metric targets at Day 14**:

| Metric | Below threshold | On track | Strong |
|--------|----------------|----------|--------|
| Score 3+ contacts | Under 4 | 6–10 | 11+ |
| Score 4–5 contacts | 0 | 2–5 | 6+ |
| Non-responsive (Score 1, no change) | 20+ | 12–19 | Under 12 |
| Total Bitly clicks | Under 10 | 15–25 | 26+ |
| Phase 2 demand queue items | 0 | 2–4 | 5+ |

**Decision rules**:
- If Score 3+ contacts are below 4 at Day 14: Do not launch Tier 2 pre-contact. Wait for Day 28 and investigate whether the message framing or contact list are the limiting factor. Under 4 Score 3+ contacts from 33 sends is a 12% engagement rate — below the 25–35% realistic benchmark. Investigate subject line, spam classification, or contact quality before proceeding.
- Academic contacts at Day 14: Do not finalize as non-responsive. Mark as "Hold — academic latency" and extend threshold to Day 28. Academic email volume and semester cycle create genuine 21-day latency.
- Score 4–5 contacts at Day 14: Begin Tier 2 pre-contact prep. Draft a personalized note referencing their Tier 1 engagement. Do not send until Day 17+ to ensure they have had two full weeks with the corpus.

**Day 14 cohort sort** (the primary output of this checkpoint):

Run the three-factor Tier 2 scoring (Section 5) against all contacts that have reached Score 3+. Generate a preliminary Tier 2 pre-contact list. This list will be finalized at Day 28 but preparing it at Day 14 allows pre-contact messages to be drafted and personalized in advance.

---

### Day 28 Checkpoint — Campaign Close

**Primary question**: What is the final engagement distribution, and who goes on the Tier 2 list?

**Time budget**: 45 minutes. This is the readout session — generate outputs, not just status checks.

**What to check and produce**:

| Task | Output |
|------|--------|
| Final score for each contact | Update all 33 rows in CSV to final engagement score |
| Tier 2 readiness score (Section 5) for each contact | Add to Tier 2 Score column in CSV |
| Non-responsive cohort list | Extract all Score 0–1 at Day 28; note whether they should receive incidental Tier 2 |
| Decline list | Extract all Decline-flagged contacts; confirm excluded from Tier 2 |
| Phase 2 demand summary | Tally demand queue items; identify top 3 most-requested additions |
| Social proof inventory | List all Score 4–5 organizations (with permission level) for use in Tier 2 opens |
| Tier 2 candidate list | Generate three lists: Pre-contact, Standard, Conditional, Exclude |

**Metric targets at Day 28**:

| Metric | Below threshold | On track | Strong |
|--------|----------------|----------|--------|
| Score 3+ contacts (confirmed reading) | Under 7 | 8–14 | 15+ |
| Score 4+ contacts (integration signal) | 0–1 | 2–5 | 6+ |
| Score 5 contacts (active adoption) | 0 | 1–2 | 3+ |
| Total Bitly clicks | Under 12 | 18–30 | 31+ |
| Phase 2 demand queue items | 0–1 | 3–5 | 6+ |
| Tier 2 pre-contact list size | 0 | 2–4 | 5+ |

**Interpreting the Day 28 totals**:

The 33-organization amplifier cohort has a different conversion profile than the direct-service cohort. Digital rights organizations are the fastest converters (high mission alignment, professional information consumers). Academic programs are the slowest (semester latency, review cycles). Researcher communities have the highest variance (some respond in days, some never respond to email outreach). Journalist organizations have moderate latency with high conversion when the content hits a current story hook.

A campaign that closes at Day 28 with 8–14 Score 3+ contacts (24–42% engagement rate) and 2–5 Score 4+ contacts is performing at or above the realistic benchmark for targeted cold outreach to professional organizations. Do not interpret a 70% non-response rate as failure — it is normal for first-contact outreach to high-volume professional organizations.

**When Day 28 results are below threshold**:

If fewer than 7 contacts have reached Score 3 at Day 28, conduct a post-mortem before launching Tier 2:
1. Check Bitly referrer data — were clicks coming from expected geographic areas and domains?
2. Search Gmail sent folder for delivery errors not flagged as bounces (some organizational email systems silently filter without bouncing).
3. Verify that the Bitly URL was live throughout the campaign (Bitly free-tier links occasionally expire or are accidentally deleted).
4. Review the contact quality for each sector — if all Score 3+ contacts are from one sector, the other sector contact lists may have been miscollected.

**Day 28 outputs that feed directly into Tier 2 launch**:
- Finalized Tier 2 pre-contact list (Score 3/3 on Tier 2 readiness score): These organizations are contacted individually with a personalized message before the Tier 2 wave launches.
- Social proof inventory: Any Score 4–5 organization that gives permission to be referenced is documented for use as a credibility anchor in Tier 2 outreach opens.
- Phase 2 demand summary: The top 3 most-requested additions (Spanish Part 0, PDF format, mobile-optimized version) are flagged for completion before Tier 2 sends begin.
- Revised message framing: If Day 28 data shows one sector significantly outperforming others, the Tier 2 messaging for that sector should lead with the framing that worked in Tier 1.

---

### Monitoring Across All Four Checkpoints: Summary Table

| Checkpoint | Primary Action | Outputs | Time Budget |
|-----------|---------------|---------|-------------|
| Day 3 | Triage bounces and hard failures | Bounce-Unresolved list; first reply classifications | 15 min |
| Day 7 | Send follow-ups to Score 0–2; respond to Score 3–4 | Follow-up wave sent; Score 4+ personal replies | 25 min |
| Day 14 | Finalize non-responsive cohort; draft Tier 2 pre-contact list | Non-responsive list; preliminary Tier 2 pre-contacts | 30 min |
| Day 28 | Generate final scores; produce Tier 2 candidate list | Tier 2 pre-contact list; social proof inventory; Phase 2 demand summary | 45 min |

**Total monitoring time across 4 weeks**: approximately 115 minutes (under 2 hours) for a 33-organization cohort. The goal is operational efficiency — the monitoring should not consume more time than the outreach itself.

---

*This document is the strategic framework. The operational companions are:*
- *engagement-scoring-template.csv — the tracking spreadsheet with all 33 amplifier-cohort contacts pre-loaded and scoring columns*
- *tier-1-feedback-collection-protocol.md — feedback question templates and follow-up cadence*
- *tier-1-success-metrics-framework.md — the prior framework covering the 12-organization direct-service cohort*
- *tier-1-measurement-dashboard-spec.md — weekly reporting template*
