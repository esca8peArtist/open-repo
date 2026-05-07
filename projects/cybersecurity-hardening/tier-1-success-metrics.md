---
title: "Tier 1 Success Metrics — Engagement Scoring, Sector Signals, and Tier 2 Candidate Identification"
project: cybersecurity-hardening
created: 2026-05-06
revised: 2026-05-06
status: production-ready
version: 2.0
executor: Anya
cohort-size: 45
sectors:
  - immigration-legal-aid (1A)
  - community-based-orgs (1B)
  - mutual-aid-networks (1C)
  - digital-rights
  - academic-cybersecurity
  - researcher-communities
  - journalist-orgs
supersedes: tier-1-success-metrics-framework.md (direct-service cohort v1), tier-1-success-metrics.md v1 (amplifier cohort)
depends-on:
  - TIER1_DISTRIBUTION_PREP.md
  - TIER1_OUTREACH_EXECUTION_PLAN.md
  - TIER2_DISTRIBUTION_PREP.md
  - TIER2_MESSAGING_TEMPLATES.md
  - tier-1-feedback-collection-protocol.md
companion-files:
  - engagement-scoring-template.csv (45-org tracking spreadsheet, all cohorts)
  - tier-1-measurement-dashboard-spec.md (weekly reporting template)
---

# Tier 1 Success Metrics
## Engagement Scoring, Sector Signals, and Tier 2 Candidate Identification

**Lead finding**: The single most consequential decision point in the entire Tier 1 campaign is not the Day 28 readout — it is the Day 7 triage. Organizations that opened but did not click by Day 3 are recoverable with a subject-line follow-up on Day 7. Organizations with a hard bounce are recoverable if researched within 24 hours. Organizations that received a hard decline are permanently closed. Everything downstream — Tier 2 candidate list quality, social proof inventory, Phase 2 demand signal — depends on executing Day 7 triage cleanly. Do not skip it or defer it.

**Cohort**: 45 organizations across two cohorts:
- **Direct-service cohort** (12 organizations): Tier 1A immigration legal aid (5), Tier 1B community-based organizations (5), Tier 1C mutual aid networks (2). These organizations have direct trust relationships with the population under immediate threat.
- **Amplifier cohort** (33 organizations): Digital rights (12), academic cybersecurity (9), researcher communities (5), journalist organizations (7). These organizations have professional reach and publication channels that multiply the corpus's effect.

**Gist URL**: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108

---

## Section 1: Engagement Scoring System

### The 0–5 Scale

Every contact carries exactly one engagement score at any given moment. The score represents the highest confirmed engagement state for that contact — it does not average across multiple contacts at the same organization or across time periods. Score trajectory (Day 3 / Day 7 / Day 14 / Day 28) is tracked alongside the current score in the Notes column.

**Score 0 — Not yet sent**
- Definition: Email has been drafted or contact is queued, but no send has been logged.
- Criteria: No send date in tracker. Organization is in queue but has not entered the engagement cycle.
- Scoring is not provisional at Score 0 — it is simply pre-campaign. Do not interpret Score 0 as non-engagement; it means outreach has not yet occurred.
- Action: None until send date logged.

**Score 1 — Sent, no engagement signal**
- Definition: Email delivered (no bounce received) but no reply, click, or open signal within the scoring window.
- Criteria: Send date logged + at least 3 days elapsed + no Bitly click, no reply, no open indicator.
- Provisional until Day 14: A Score 1 contact may still recover to Score 2+ if the Day 7 follow-up generates a late click. After Day 14 with no movement, Score 1 is confirmed non-responsive.
- Hard decline variant: If the organization replied explicitly declining engagement ("not for us," "remove from list"), assign Score 1 with a Decline flag. A decline is a response — it is not Score 0.
- Action: Day 7 checkpoint — send follow-up with sector-specific hook. After Day 14 with no movement: mark non-responsive; exclude from Tier 2 pre-contact list.

**Score 2 — Open signal, no click**
- Definition: Email was opened (or an auto-reply was received indicating mailbox engagement), but no Bitly click was recorded.
- Criteria: Open indicator in tracking tool OR auto-reply/OOO received + no Bitly click recorded.
- Limitation: Email open tracking is unreliable due to image blocking, preview-pane rendering, and iOS Mail Privacy Protection. Score 2 may undercount genuine opens and should not be treated as a strong positive signal. Treat Score 2 as "possibly reading, not confirmed."
- OOO messages: An OOO reply confirms delivery. Assign Score 2 provisionally; log the return date; send a fresh copy on the contact's return date. The new send restarts the clock.
- Action: Day 7 — send one-line follow-up with Bitly link re-embedded and sector-specific subject. A Score 2 that generates a click upgrades to Score 3.

**Score 3 — Click or confirmed reading**
- Definition: A Bitly click was recorded, or a reply demonstrates the person read past the subject line (references specific section, asks a specific question, or describes how they plan to use the corpus).
- Criteria: Bitly click in dashboard OR reply classified as Question or Request in the reply-type taxonomy (Section 4).
- This is the first score level representing confirmed reading. A Score 3 means a real person at the organization encountered the corpus content. All Tier 2 candidate eligibility begins at Score 3.
- Action: Reply immediately (within 24 hours). The first substantive exchange is the highest-leverage moment in the engagement cycle. Ask Question 2 (which section is most relevant to their context).

**Score 4 — Integration signal**
- Definition: The organization is evaluating the corpus for integration into their work — not just reading it as a one-time document.
- Criteria: Any ONE of the following:
  - Reply describes routing the corpus internally ("forwarding this to our legal team / client services / training coordinator")
  - Reply identifies a specific barrier to adoption ("we'd use this but clients lack smartphones") — barrier identification means they are actively evaluating fit
  - Second Bitly click from the same organization (indicates internal forwarding)
  - Bitly click from a new geographic area following send to a mutual aid network (indicates share in a network channel)
  - Reply classified as Integration Signal in reply-type taxonomy
- Strong positive signal. Score 4 contacts should receive a personal follow-up within 48 hours that addresses their specific integration context.
- Action: Ask Question 2 (section relevance) and begin monitoring for Score 5 indicators. Begin tracking for Tier 2 pre-contact candidacy.

**Score 5 — Active adoption**
- Definition: The organization is using the corpus, not merely evaluating it.
- Criteria: Any ONE of the following:
  - Self-reported use ("our intake team is walking clients through Part 0 now")
  - Corpus link appears on the organization's published resource page (verifiable by web search)
  - Organization schedules or confirms a workshop or training using corpus content
  - Organization asks to customize or adapt the corpus for their specific context
  - Reply classified as Implementation Feedback (reporting what worked and what did not from actual use)
  - Organization cites the corpus in a published output (newsletter, brief, resource list)
  - Organization translates Part 0 into a community language (Spanish, Haitian Creole, etc.) — translation requires active investment; it is always Score 5
- Score 5 is the campaign's end state for any individual contact. Score 5 counts toward the Tier 2 social proof inventory.

### Scoring Rules and Edge Cases

**Auto-responders and OOO messages**: Assign Score 2 provisionally. Log return date. Send a fresh copy on return date + 2 business days. New send restarts the 28-day window for that contact.

**Hard bounce (permanent delivery failure)**: Do not assign any score. Flag as Bounce-Unresolved. Research alternate contact within 24 hours. If corrected and re-sent, start from Score 0 on the corrected contact.

**Hard decline**: Score 1 permanent, Decline flag. Send one acknowledgment reply ("Understood — no further outreach from me. Thank you for your time."). Do not contact again from the same contact point for 90+ days minimum. Decline from a general info@ inbox does not necessarily close the organization — a named staff contact at a mission-aligned organization is eligible for one attempt through a different contact after 30 days, with the prior decline noted.

**Multiple contacts at same organization**: The organization score is the highest score across all contacts. Contact A at Score 1, Contact B at Score 4 = organization at Score 4.

**Forwarded reply from a third party**: If an organization forwarded the corpus and the recipient replies to you, this counts as Score 4 for the original organization (integration signal) and Score 3 for the new contact (confirmed reading, since they engaged directly with you).

### Score Trajectory Tracking

A snapshot score is less informative than trajectory. Record score at each checkpoint:

| Trajectory Pattern | Interpretation | Action |
|-------------------|----------------|--------|
| 0 → 1 → 1 → 1 | Non-responsive; no movement after initial send | Close; exclude from Tier 2 pre-contact |
| 0 → 1 → 3 → 4 | Slow start, Day 7 follow-up triggered engagement | High-value; note which follow-up text triggered upgrade |
| 0 → 3 → 4 → 5 | High-velocity adoption | Top Tier 2 pre-contact candidate |
| 0 → 2 → 2 → 2 | Open indicator, no click, no conversion | Likely wrong contact person; try alternate |
| 0 → 4 → 4 → 5 | Rapid integration signal, confirmed adoption | Social proof inventory priority |

Record trajectory in the Notes column: "Day3:1 | Day7:3 | Day14:4" — do not overwrite previous entries, append with date.

---

## Section 2: Sector-Specific Success Signals

Each sector has a different institutional rhythm, output expectation, and observable adoption signal. Applying a uniform threshold misreads both positive and negative signals. The definitions below are calibrated to what is actually observable from an external sender.

### Immigration Legal Aid Organizations (1A — Direct-Service)

**Observable integration signals (Score 4 criteria)**:
- Reply from a named legal staff member (attorney, paralegal, or legal director) asking a substantive question — confirms corpus reached the right desk
- Organization confirms routing to client services, intake, or training function
- Organization asks which section is most relevant for clients in specific enforcement zones (California, Texas, Arizona, Florida)

**Observable adoption signals (Score 5 criteria)**:
- Organization confirms walking at least one client through Part 0 (data broker opt-outs) or the California DROP platform pathway
- Corpus appears on the organization's published resource list or internal practitioner toolkit
- Organization cites corpus in a legal filing, policy brief, or amicus submission

**What distinguishes depth**: A legal aid org that walks five clients through Part 0 is deeper adoption than one that shares the Gist URL in a staff newsletter — even though both qualify as Score 5. Track depth in Notes: "Score 5 — client walkthroughs (5 reported)" carries different weight than "Score 5 — newsletter mention."

**Expected timeline**: 5–14 days to first reply; 30–60 days to confirmed adoption signal. Immigration legal organizations under active enforcement pressure are processing very high caseloads. A 14-day response window is realistic; 30 days for adoption signal is realistic. Do not close these contacts at Day 14 — send the 30-day follow-up regardless of initial response status.

**Exception**: Organizations in high-enforcement zones (Texas, Arizona, Georgia, Florida) may respond faster due to immediate operational urgency.

### Community-Based Organizations Serving Immigrant Communities (1B — Direct-Service)

**Observable integration signals (Score 4 criteria)**:
- Organization shares the Gist link in a Signal group, newsletter, or community email list (Score 4 because it required a distribution decision)
- Organization schedules a workshop or community education session using corpus content
- Reply from a community organizer, communications staff, or program director that references specific community members or programs

**Observable adoption signals (Score 5 criteria)**:
- Corpus used in at least one community education session, workshop, or Know Your Rights training (self-report is sufficient; ask Question 2 to get specificity)
- Organization adapts Part 0 into a community handout or translated version
- Corpus integrated into an existing program (newcomer orientation, Know Your Rights series, community legal education)
- Translation into Spanish or another community language (uniquely strong signal — translation requires active staff investment)

**Expected timeline**: 7–14 days to first reply; 14–30 days to adoption signal. Community organizations move faster than legal organizations because there is no formal review cycle — a community organizer who reads the corpus on Tuesday can share it at a community meeting on Thursday.

**Watch for**: Early Score 4 signals from this sector. They are the most likely to show Score 3 → 4 progression within the first week.

### Mutual Aid Networks (1C — Direct-Service)

**Observable integration signals (Score 4 criteria)**:
- Contact confirms sharing corpus link in a Signal group, Telegram channel, or Discord server affiliated with the network (not just promising to do so)
- Bitly click spike from a new geographic area following a mutual aid send (strong indicator of network distribution without direct notification)
- Network asks for a "lighter" or shorter version — indicates they are actively planning distribution to members with limited tech literacy

**Observable adoption signals (Score 5 criteria)**:
- Network posts Part 0 as a standalone resource, separated from the full corpus
- Network conducts an informal workshop or "security night" using corpus content
- Network connects you with another network or region (organic amplification)
- Any organic reach visible as new inbound contacts referencing the mutual aid network as their source

**Channel preference**: Mutual aid contacts reachable via Signal should receive Signal outreach parallel to email. An email to a Signal-native network has significantly lower open rates than email to institutional organizations. If your tracker shows a mutual aid contact with only an email method, flag for Signal follow-up.

**Expected timeline**: 2–7 days to first reply; 7–14 days to adoption signal. This is the fastest-moving sector. If no click or reply from any mutual aid contact by Day 7, investigate the contact method before concluding non-engagement.

### Digital Rights Organizations (Amplifier Cohort)

**Observable integration signals (Score 4 criteria)**:
- Reply from a named policy, surveillance, or legal staff member — not a general info@ response
- Organization routes corpus to a specific internal team (privacy policy, data broker litigation, immigration surveillance)
- Organization asks for a conversation about primary source methodology (indicates evaluation for citation-quality work)

**Observable adoption signals (Score 5 criteria)**:
- Organization publishes an analysis, blog post, or resource page citing the corpus
- Organization incorporates corpus into published policy campaign material or litigation filings
- Named specialist (rather than communications staffer) engages substantively — strong indicator of Score 5 potential

**Expected timeline**: 7–21 days to first reply; 14–45 days to adoption signal. Digital rights organizations publish quickly but have high inbound volume. Named contacts perform significantly better than generic press@ or info@ inboxes.

### Academic Cybersecurity Programs (Amplifier Cohort)

**Observable integration signals (Score 4 criteria)**:
- Reply from a named faculty member, clinic director, or research lead — not a department administrator
- Faculty member asks for a conversation about research or teaching use (requires a decision to invest time)

**Observable adoption signals (Score 5 criteria)**:
- Corpus appears on a course syllabus, clinic resource list, or program reading list
- Faculty member cites corpus in a working paper, presentation, or research note
- Corpus cited in a peer-reviewed publication, amicus brief, or formal academic output

**Expected timeline**: 21–60 days to first substantive reply; 45–120 days for curriculum integration (semester cycle dependent). Do not mark academic contacts as non-responsive at Day 14. Mark as "Hold — semester boundary" and send a follow-up in late August for any sends in May.

**Exception**: Clinic directors (Harvard Cyberlaw Clinic, law school immigration clinics) operate on a more responsive timeline than research faculty. Clinic-directed sends may convert within 14–30 days because clinics have active client caseloads.

### Researcher Communities (Amplifier Cohort)

**Observable integration signals (Score 4 criteria)**:
- Individual researcher replies substantively about corpus methodology or sourcing
- Conference/community organization asks about submitting a presentation or talk based on corpus findings

**Observable adoption signals (Score 5 criteria)**:
- Researcher publicly discusses or links the corpus via Mastodon, Bluesky, or a security-community forum
- Conference presentation or community workshop using corpus content confirmed

**Expected timeline**: Highly variable. Some researchers respond in days; others never respond to email outreach. A Bitly click without a reply from researcher community contacts may indicate the person is evaluating the corpus in-depth before engaging. Do not treat click-without-reply as non-response for this sector.

### Journalist Organizations (Amplifier Cohort)

**Observable integration signals (Score 4 criteria)**:
- Reply from a journalist, training coordinator, or press freedom staff member asking substantive questions about corpus sourcing
- Training coordinator asks to schedule a conversation about incorporating corpus into a training program

**Observable adoption signals (Score 5 criteria)**:
- Organization integrates Part 0 or source-protection section into journalist security training materials
- Organization publishes an article, newsletter, or resource referencing the corpus
- Organization recommends corpus to a journalist working on an enforcement-adjacent story

**Expected timeline**: 7–14 days to first reply; 14–45 days to adoption signal. The June 12, 2026 FISA 702 reauthorization deadline creates urgency for source protection content — sends in May 2026 have a timely hook for this sector.

---

## Section 3: Early Warning Detection

Non-engagement is data, not failure. The goal of early warning monitoring is to distinguish between contacts that need an intervention and contacts that have definitively closed. Acting on the wrong category wastes effort; failing to intervene on recoverable contacts wastes an opportunity.

### Hard-Stop Indicators — Require Immediate Action

**Bounce within 24 hours (flag: Bounce-Unresolved)**
- Signal: Mailer-daemon notification, "user not found," or "address does not exist."
- Do not assign Score 1. A bounced contact never received the email.
- Action: Research alternate contact within 24 hours. Check organization website for current general inbox. Search "[organization] communications director" or use web contact form. If no alternate found, flag as Bounce-Unresolved and exclude from all follow-up until a valid address is confirmed.
- Do not count against response rates. Bounces are infrastructure failures, not non-responses.

**Hard decline within 48 hours (Score 1 permanent, flag: Decline)**
- Signal: Explicit "not interested," "not relevant to our work," "remove from list," or equivalent.
- Action: Log immediately. Send one-sentence acknowledgment reply. Add Decline flag. Do not follow up. Do not contact same person again.
- Note: Decline from general info@ inbox does not necessarily close the organization. One attempt through a named staff contact is acceptable after 30 days at mission-aligned organizations. Document the prior decline before proceeding.

### Threshold Triggers — Require Decision at Named Checkpoint

**No click by Day 3 (trigger: Day 7 follow-up required)**
- Signal: Bitly shows zero clicks from a specific send, 72 hours after send.
- What this may mean: Email not opened, opened but did not generate interest, or link was visually passed over in preview.
- Do not send a follow-up before Day 7. Two messages in three days reads as spam.
- Action at Day 7: Send one-line follow-up with Bitly link re-embedded and a sector-specific subject hook. Example hooks by sector:
  - Digital rights: "Following up — June 12 FISA 702 deadline and immigration surveillance update"
  - Academic: "Flagging this for your research — Palantir ELITE primary-source documentation"
  - Legal aid: "Following up — Part 0 client opt-out guide for ELITE targeting database"
  - Journalists: "Source protection resource — FISA 702 renewal context"
  - Mutual aid: "Security guide for ICE enforcement risk — Part 0 requires no tech knowledge"

**No reply by Day 7 (score stays at 1–2, flag: Low-Interest)**
- Signal: No reply or click 7 days after send.
- The Day 7 follow-up should already be sent (above). If Score 0–2 by Day 7, send it now if not yet done.
- Do not send a second follow-up before Day 14.

**No engagement by Day 14 (Score 1 confirmed: Non-Responsive)**
- Signal: No reply, click, or open signal for 14 calendar days following initial send.
- Action: Mark Non-Responsive in tracker. Include in 30-day follow-up wave only if a substantially different hook exists (event-triggered, not a generic "checking in").
- Exceptions:
  - Academic program contacts: Extend threshold to Day 28 (semester cycle latency).
  - Sends made within 2 weeks of a semester break: Extend threshold to Day 28 and log calendar context.
  - Small-team organizations (3 or fewer communications staff): Extend threshold to Day 21.
  - Any contact where the Day 7 follow-up bounced: Start fresh 7-day window from corrected send date.

**Zero Bitly clicks from all contacts in a sector by Day 7 (sector-level failure signal)**
- Signal: No clicks at all from emails sent to an entire sector (e.g., all five academic sends show zero clicks by Day 7).
- What this likely means: Wrong contact person for that sector, or a sector-specific spam filter pattern.
- Action: Pause further sends to that sector. Verify contact quality (are you reaching general inboxes vs. named people?). Check spam classification by sending a test email to a personal account at a domain in that sector category.

### Recovery Opportunities for Non-Responsive Contacts

Non-responsive contacts are not permanently closed. Three events justify a re-engagement attempt:

1. **Policy deadline event**: The June 12, 2026 FISA 702 reauthorization deadline is a concrete hook for digital rights and journalist contacts. A major ICE enforcement action, a court ruling on ELITE, or an Inspector General report is a hook for legal aid and community contacts. Event-triggered follow-up ("given this week's [event], wanted to resurface this guide") has higher open rates than generic follow-ups.

2. **Seasonal peak**: Immigration legal aid organizations see intake spikes in September–October following summer enforcement increases. A late-August follow-up ("as fall enforcement increases, resharing this resource") is a legitimate re-engagement frame.

3. **Warm referral**: If a Score 4–5 organization has a direct coalition relationship with a non-responsive organization, a warm referral from the former to the latter is the highest-probability recovery mechanism. Requires the Score 4–5 organization's permission. Ask Question 3 in the 30-day follow-up to generate referral opportunities.

---

## Section 4: Feedback Triage Protocol

Every reply must be classified before responding. Classification determines response template, follow-up timeline, score upgrade, and routing for Phase 2 improvement.

### Reply Type Taxonomy

**Type 1: Implementation Feedback**
- Definition: The responder has already used the corpus and is reporting what worked, what did not, or what modifications they made.
- Identifiers: Past tense ("we tried," "our clients found," "we adapted"); specific operational detail; references to staff or client experience.
- Score: Automatic Score 5. Implementation feedback means adoption has occurred.
- Response window: 12 hours.
- Phase 2 routing: If feedback identifies a documentation error, missing step, or technical gap — add to Phase 2 documentation revision queue immediately. Example: "California DROP platform path needs clarification on the ID verification step" → Phase 2 revision queue.
- Response text: "Thank you for this — hearing that [specific detail] is exactly the kind of ground-truth feedback most useful. Follow-up: [1] What part was most difficult for clients? [2] Any step that needed clarification? [3] May I reference this experience (anonymized) in conversations with other organizations?"

**Type 2: Critique**
- Definition: The responder has substantive disagreement with a specific claim, methodology, or recommendation.
- Identifiers: Conditional language ("I'm not sure this is accurate," "this conflicts with what we've found"); factual correction; sourcing challenge.
- Score: Score 3 (careful reading). May upgrade to 4 if critique indicates ongoing engagement.
- Response window: 24 hours (acknowledge); 72 hours (substantive response).
- Rule: Never respond defensively to a critique before verifying the claim independently.
- Phase 2 routing: If critique identifies a factual error → correct immediately and acknowledge in reply. If it is a methodological disagreement → document, respond with sourcing, note for Tier 2 messaging adjustment.
- Response text: "Thank you for pushing on this — I want to respond carefully rather than quickly. Let me review your point about [specific issue] and get back to you within 72 hours. I take sourcing seriously and if there's an error I want to correct it."

**Type 3: Request**
- Definition: The responder asks for something that does not currently exist (a translated version, a different format, a domain-specific update, a customized version).
- Identifiers: "Do you have...," "Would it be possible to...," "We need something that..."; forward-looking; constructive.
- Score: Score 4. A request indicates the responder considers the corpus relevant and is investing in making it more useful.
- Response window: 24 hours.
- Rule: Do not promise delivery timelines you cannot meet. "That's on the Phase 2 roadmap" is an honest answer.
- Phase 2 routing: Log in Phase 2 demand queue. If the same request comes from 3+ organizations → confirmed Phase 2 priority. The threshold flag: three independent requests for Spanish Part 0 = Spanish Part 0 is a confirmed Phase 2 deliverable.
- Response text: "Noted, and useful. [The request] is something I've heard from several organizations, which means it's a real gap rather than a corner case. I'll flag it for Phase 2 and let you know when it's available. Is there anything in the current version I can help you adapt in the meantime?"

**Type 4: Integration Signal**
- Definition: The responder explicitly confirms they are using, distributing, or integrating the corpus.
- Identifiers: Present or future tense ("we're sending this to our network," "I'm adding this to our toolkit," "we're planning a workshop"); organization as subject.
- Score: Score 4 (evaluating) or Score 5 (confirmed use) depending on whether "integrating" means planning or actual deployment. Ask a clarifying question to distinguish.
- Response window: 12 hours.
- Phase 2 routing: Add to Tier 2 social proof inventory. With the organization's permission, document the integration for use in Tier 2 outreach. "This resource is in use at [Organization] for client intake" is a powerful Tier 2 credibility anchor.
- Response text: "Great to hear. Quick follow-up: [1] Which section are your clients/staff finding most useful? [2] Anything creating friction or needing adaptation? [3] If you run into anything that needs clarification as you use it, I'd appreciate hearing — ground-level feedback improves the corpus for everyone."

**Type 5: Question**
- Definition: The responder asks for clarification on a specific claim, procedure, or recommendation without expressing agreement or disagreement.
- Identifiers: Interrogative phrasing ("How does...," "What happens if...," "Is this applicable to..."); neutral or curious tone; references a specific section or step.
- Score: Score 3 (confirmed reading), upgrading toward 4 if the question indicates evaluation for practical use.
- Response window: 24 hours.
- Phase 2 routing: If the same question arrives from 3+ organizations → the corpus has a gap or an unclear section. Add a clarification note to that section in Phase 2 revision queue. Repeated questions about the same section are documentation defects, not user errors.
- Response text: "Good question — [answer the specific question directly, with reference to the relevant section]. If the corpus doesn't make this clear enough, that's a gap I'll fix in the next revision. Is there a follow-up question, or does this address what you needed?"

### Feedback Triage Decision Tree

```
New reply received
│
├─ Is it past-tense operational detail about actual use?
│   └─ YES → Type 1: Implementation Feedback → Score 5 → 12-hour response → Phase 2 revision queue if gap
│
├─ Does it challenge a specific factual claim?
│   └─ YES → Type 2: Critique → Score 3/4 → 24h acknowledge, 72h substantive → verify before responding
│
├─ Does it ask for something that doesn't currently exist?
│   └─ YES → Type 3: Request → Score 4 → 24-hour response → add to Phase 2 demand queue
│
├─ Does it confirm distribution or integration is underway?
│   └─ YES → Type 4: Integration Signal → Score 4/5 → 12-hour response → Tier 2 social proof inventory
│
├─ Does it ask a specific question about a section or procedure?
│   └─ YES → Type 5: Question → Score 3→4 → 24-hour response → track for repeated-question pattern
│
└─ Is it a generic "thanks, received" with no specific content?
    └─ YES → Acknowledgment only (not a feedback type) → Score 2 maintained → Day 10 follow-up per Template R2
```

### Priority and Routing Matrix

| Reply Type | Response Window | Phase 2 Routing | Score Implication |
|-----------|----------------|-----------------|-------------------|
| Implementation Feedback | 12 hours | Yes — if gap or error identified | 5 confirmed |
| Critique | 24h acknowledge / 72h substantive | Yes — if factual error; document if methodological | 3–4 |
| Request | 24 hours | Yes — log in Phase 2 demand queue | 4 |
| Integration Signal | 12 hours | Yes — add to social proof inventory | 4–5 |
| Question | 24 hours | Yes — if repeated 3+ times | 3 upgrading toward 4 |

---

## Section 5: Tier 2 Candidate Pre-Identification

### Defining Tier 2 Readiness

A Tier 2 candidate is a Tier 1 organization whose engagement pattern indicates they are positioned to actively multiply the corpus's reach in the Tier 2 distribution phase — either as ambassadors who provide credibility endorsement, or as amplifiers whose networks extend the corpus to new populations. Tier 2 selection is not about rewarding positive responders. It is about identifying organizations that will make the Tier 2 launch land better.

### Minimum Eligibility Threshold

Score 3 or higher by Day 14. A contact that has clicked through the corpus has confirmed reading intent. Below Score 3, there is no evidence the contact has engaged with the content. Tier 2 targeting below this threshold is not supported by the engagement data.

### Three-Factor Tier 2 Readiness Score (0–3 points)

**Factor 1: Engagement depth (0 or 1 point)**
- 0 points: Score 0–2 (no confirmed click or reading)
- 1 point: Score 3–5 (confirmed reading, integration signal, or adoption)

**Factor 2: Integration or adoption signal (0 or 1 point)**
- 0 points: Score 3 only (confirmed click, no further engagement signal)
- 1 point: Score 4 or 5 (integration signal present or confirmed adoption)

**Factor 3: Network multiplier potential (0 or 1 point)**
- 0 points: Local or regional reach only (single-city mutual aid network, small regional legal aid org)
- 1 point: National or cross-sector reach (a network of 50+ affiliated organizations, or an organization with publication channels reaching a professional community)
  - Automatic 1 point: NILC, CLINIC (400+ affiliates), NLG, EFF, CDT, Freedom of the Press Foundation, any national journalist organization
  - Conditional 1 point: Regional organizations with documented coalition relationships where they could make a warm referral to 10+ organizations

### Targeting Decision by Score

| Tier 2 Readiness Score | Action |
|------------------------|--------|
| 3/3 | Pre-contact before Tier 2 launch: reach out individually, reference their Tier 1 engagement, ask if they would review Tier 2 materials and share within their networks. These are your ambassadors. |
| 2/3 | Standard Tier 2 inclusion: receive Tier 2 materials as part of the send wave. |
| 1/3 | Conditional inclusion: only if they fall within the Tier 2 organizational target list AND Score 3 was confirmed reading (not just a click). |
| 0/3 | Exclude from Tier 2 targeting: no confirmed engagement basis for inclusion. |

### Hard Exclusions from Tier 2

**Decline-flagged contacts**: Permanently excluded from Tier 2 targeting regardless of Tier 2 readiness score. This applies to the specific contact. If the organization appears in the Tier 2 target list through a different channel, use a different contact and note the prior decline.

**Bounce-Unresolved contacts**: Excluded until a confirmed delivery address is available.

**Score 1 at Day 28 with no intervening movement**: Excluded from Tier 2 pre-contact but may receive Tier 2 materials if they appear on the Tier 2 list via a different contact or a warm referral creates a new introduction.

### Sector Diversity Logic

The Tier 2 pre-contact list should include at least one organization from each sector represented in the Tier 1 cohort (if engagement exists). A Tier 2 pre-contact list composed entirely of digital rights organizations does not generate the cross-sector credibility that makes Tier 2 outreach to legal aid or academic organizations more effective. Aim for:
- At least 1 direct-service organization (1A, 1B, or 1C) in the pre-contact list
- At least 1 digital rights organization
- At least 1 journalist or academic organization

If the engagement data doesn't support sector diversity in the pre-contact list (e.g., all Score 4+ contacts are from one sector), note this in the Day 28 readout and adjust Tier 2 messaging to lead with the social proof you actually have.

### The Tier 2 Candidate List Output (Day 28)

Generate four sub-lists at the Day 28 checkpoint:
1. **Pre-contact list** (Score 3/3): Individual, personalized outreach before Tier 2 launch wave
2. **Standard Tier 2 list** (Score 2/3): Included in the Tier 2 send wave
3. **Conditional list** (Score 1/3): Included only if specific conditions are met (documented above)
4. **Exclude list** (Score 0/3, Decline, Bounce-Unresolved): Excluded from Tier 2

Record each organization's Tier 2 readiness score and list assignment in the CSV tracker (Tier2_Readiness_Score column, Tier2_Candidate? column).

---

## Section 6: 4-Week Monitoring Timeline

### Operating Logic

The monitoring schedule has two jobs: (1) catch recoverable failures before they become permanent losses, and (2) accumulate evidence for Tier 2 targeting decisions. The four checkpoints are not symmetric — Day 3 is a triage checkpoint, Day 7 is an intervention checkpoint, Day 14 is a finalization checkpoint, and Day 28 is a readout. Complete each checkpoint in under 30 minutes for the full 45-organization cohort.

---

### Day 3 Checkpoint — Triage
**Primary question**: Did the messages get through? Are there hard failures requiring same-week correction?
**Time budget**: 15 minutes.

**What to check**:

| Signal | Where to check | Action trigger |
|--------|---------------|----------------|
| Bounce notifications | Gmail, filter Tier1-Outreach/Bounce | Any bounce → research alternate contact within 24 hours |
| Bitly click count | bitly.com dashboard, total clicks since launch | Zero clicks across all sectors after 72 hours → deliverability issue |
| Early replies | Gmail inbox | Any reply → classify immediately using reply-type taxonomy |
| OOO messages | Gmail, filter Tier1-Outreach/OOO | Log return date; schedule re-send for return date +2 business days |

**Day 3 metric targets**:

| Metric | Below threshold | On track | Strong |
|--------|----------------|----------|--------|
| Bitly clicks (total) | 0 | 3–8 | 9+ |
| Bounces received | 3+ (systemic) | 1–2 | 0 |
| Replies received | 0 | 1–3 | 4+ |
| Score 3+ contacts | 0 | 1–2 | 3+ |

**Day 3 decision rules**:
- Zero clicks from all 45 sends: Stop remaining sends. Check spam classification at mail-tester.com. Verify Bitly link is live and correctly embedded in email body. Do not send additional outreach until deliverability is confirmed.
- Two or more bounces in same sector: That sector's contact list was likely compiled from outdated sources. Verify all remaining contacts in that sector before sending.
- Score 4 signal at Day 3 (integration signal within 72 hours of send): Flag as high-velocity candidate. Move to Tier 2 pre-contact list. These rare early-movers are the most valuable Tier 2 ambassadors.

---

### Day 7 Checkpoint — Intervention
**Primary question**: Which contacts are recoverable with a follow-up, and which have definitively closed?
**Time budget**: 25 minutes. Review all 45 rows; update scores; identify follow-up actions.

**What to check**:

| Signal | Where to check | Action trigger |
|--------|---------------|----------------|
| Score stall at 1–2 | CSV tracker | Send Day 7 follow-up (see template below) |
| New clicks since Day 3 | Bitly dashboard | Update scores for any new clicks |
| Pending reply classifications | Gmail inbox | Classify all pending replies before sending follow-ups |
| Score 4–5 contacts | CSV tracker | Personal follow-up within 24 hours |
| OOO return dates reached | OOO log | Send fresh copy on return date |

**Day 7 metric targets**:

| Metric | Below threshold | On track | Strong |
|--------|----------------|----------|--------|
| Cumulative Bitly clicks | Under 5 | 8–15 | 16+ |
| Score 3+ contacts | 1 | 3–8 | 9+ |
| Score 4–5 contacts | 0 | 1–4 | 5+ |
| Cumulative replies | Under 3 | 5–10 | 11+ |
| Declines | 3+ | 1–2 | 0 |

**Day 7 follow-up template** (for Score 0–2 contacts):

> Subject: Following up — [sector-specific hook]
>
> Hi [name / team],
>
> Briefly following up on the message I sent [Day 0 date] about the ICE/Palantir ELITE threat model and countermeasures guide.
>
> [Sector-specific hook — use the relevant line]:
> - Digital rights / journalists: "With the June 12 FISA 702 deadline approaching, the surveillance integration analysis may be timely."
> - Academic: "The Palantir ELITE primary-source documentation may be worth a look for your research or teaching context."
> - Immigration legal aid: "Part 0 (data broker opt-outs) is actionable for clients immediately — no technical expertise required."
> - Mutual aid / community orgs: "The guide includes a specific path for undocumented CA residents without government-issued ID."
>
> Corpus is at [Bitly URL]. Happy to answer questions if relevant.
>
> [Anya]

**Day 7 decision rules**:
- Score 4+ contacts: Do not send the generic template. Send a personal reply referencing what they said or did.
- Decline-flagged contacts: Do not send Day 7 follow-up. Log as permanently closed.
- Score 0 contacts (no bounce): Eligible for Day 7 follow-up regardless of click history. A different hook sometimes converts after a first miss.

---

### Day 14 Checkpoint — Non-Response Finalization
**Primary question**: Which contacts are definitively non-responsive? Which Score 3–5 contacts have enough momentum to begin Tier 2 prep?
**Time budget**: 30 minutes. This is the most consequential checkpoint — decisions here determine the Tier 2 pre-contact list.

**What to check**:

| Signal | Where to check | Action trigger |
|--------|---------------|----------------|
| Score stall at 1 since Day 3 | CSV tracker | Flag Non-Responsive; exclude from Tier 2 pre-contact |
| Score trajectory acceleration (1→3→4) | Trajectory notes | Flag high-velocity; begin drafting Tier 2 pre-contact |
| All pending reply feedback | Gmail inbox | Clear all pending replies before reporting |
| Phase 2 demand queue items | Notes column | Log any requests or repeated questions |
| Bounce-Unresolved contacts | Bounce log | Final attempt at alternate contact |

**Day 14 metric targets**:

| Metric | Below threshold | On track | Strong |
|--------|----------------|----------|--------|
| Score 3+ contacts | Under 5 | 7–13 | 14+ |
| Score 4–5 contacts | 0 | 2–6 | 7+ |
| Non-responsive (Score 1, no change) | 25+ | 15–24 | Under 15 |
| Total Bitly clicks | Under 10 | 18–30 | 31+ |
| Phase 2 demand queue items | 0 | 2–5 | 6+ |

**Day 14 decision rules**:
- If fewer than 5 contacts at Score 3+ from 45 sends (below 11% engagement): Do not launch Tier 2 pre-contact. Investigate whether the subject line, spam classification, or contact quality are the limiting factor. The realistic benchmark is 25–35% engagement from targeted personalized outreach to professional organizations.
- Academic contacts at Day 14: Do not finalize as non-responsive. Mark "Hold — academic latency" and extend to Day 28.
- Score 4–5 contacts at Day 14: Begin drafting Tier 2 pre-contact notes. Do not send until Day 17+ to ensure at least 2 full weeks with the corpus.

**Day 14 primary output**: Run the three-factor Tier 2 readiness scoring against all Score 3+ contacts. Generate a preliminary Tier 2 pre-contact list. Finalizing this list at Day 28 is cleaner if the prep work is done at Day 14.

---

### Day 28 Checkpoint — Campaign Close
**Primary question**: What is the final engagement distribution, and who goes on the Tier 2 list?
**Time budget**: 45 minutes. Generate outputs, not just status checks.

**What to produce at Day 28**:

| Task | Output |
|------|--------|
| Final score for each contact | Update all 45 rows in CSV to final engagement score |
| Tier 2 readiness score (Section 5) for each contact | Add to Tier2_Readiness_Score column in CSV |
| Non-responsive cohort list | Extract all Score 0–1 at Day 28; note whether incidental Tier 2 applies |
| Decline list | Extract all Decline-flagged contacts; confirm excluded from Tier 2 |
| Phase 2 demand summary | Tally demand queue items; identify top 3 most-requested additions |
| Social proof inventory | List all Score 4–5 organizations (with permission level) for Tier 2 opens |
| Tier 2 candidate list | Generate: Pre-contact, Standard, Conditional, Exclude |

**Day 28 metric targets**:

| Metric | Below threshold | On track | Strong |
|--------|----------------|----------|--------|
| Score 3+ contacts (confirmed reading) | Under 9 | 11–18 | 19+ |
| Score 4+ contacts (integration signal) | 0–1 | 3–7 | 8+ |
| Score 5 contacts (active adoption) | 0 | 1–3 | 4+ |
| Total Bitly clicks | Under 15 | 22–38 | 39+ |
| Phase 2 demand queue items | 0–1 | 4–6 | 7+ |
| Tier 2 pre-contact list size | 0 | 2–5 | 6+ |

**Interpreting the Day 28 distribution by sector**:
- Direct-service cohort (1A, 1B, 1C): Expect highest conversion from 1B (community orgs) and 1C (mutual aid) due to lower institutional friction. 1A (immigration legal aid) may show slower conversion with deeper eventual adoption.
- Amplifier cohort: Digital rights organizations convert fastest. Academic programs convert slowest. Journalist organizations have high variance depending on how closely the send timing aligns with FISA 702 / enforcement news cycles.

**A campaign that closes at Day 28 with 11–18 Score 3+ contacts (24–40% engagement rate) and 3–7 Score 4+ contacts is at or above the realistic benchmark** for targeted cold outreach to professional organizations. A 60–75% non-response rate is normal for first-contact outreach to high-volume institutional organizations.

**When Day 28 results are below threshold (fewer than 9 Score 3+ contacts)**:
1. Check Bitly referrer data — clicks coming from expected geographic areas and domains?
2. Search Gmail sent folder for delivery errors not flagged as bounces (some institutional email systems silently filter).
3. Verify Bitly URL was live throughout the campaign (free-tier links can expire).
4. Review contact quality per sector — if all Score 3+ contacts are from one sector, the other sector's contact lists may have been miscollected.

---

### 4-Week Monitoring Summary

| Checkpoint | Primary Action | Key Outputs | Time Budget |
|-----------|---------------|-------------|-------------|
| Day 3 | Triage bounces and hard failures | Bounce-Unresolved list; first reply classifications | 15 min |
| Day 7 | Send follow-ups to Score 0–2; respond to Score 3–4 | Follow-up wave sent; Score 4+ personal replies | 25 min |
| Day 14 | Finalize non-responsive cohort; draft Tier 2 pre-contact | Non-responsive list; preliminary Tier 2 pre-contacts | 30 min |
| Day 28 | Generate final scores; produce Tier 2 candidate list | Tier 2 candidate list; social proof inventory; Phase 2 demand summary | 45 min |

**Total monitoring time across 4 weeks**: approximately 115 minutes for the full 45-organization cohort. The monitoring should consume less time than the outreach itself.

---

*Companion files:*
- *engagement-scoring-template.csv — 45-organization tracking spreadsheet (direct-service + amplifier cohorts combined). Columns: org_name, sector, contact_email, playbook_sent, send_date, day3_score, day7_score, day14_score, day28_score, current_score, reply_type, bounce_decline_flag, tier2_readiness_score, tier2_candidate, notes. The `playbook_sent` column identifies which Phase 1 playbook(s) were distributed (journalist-security, whistleblower, activist-organizing, dv-survivor-safety, financial-resistance, immigration-surveillance-evasion); some orgs receive multiple. The `current_score` field is updated at each checkpoint and reflects the live engagement score; `day28_score` is the campaign-close snapshot.*
- *tier-1-feedback-collection-protocol.md — feedback question templates and follow-up cadence*
- *tier-1-measurement-dashboard-spec.md — weekly reporting template*
- *TIER1_OUTREACH_EXECUTION_PLAN.md — daily execution runbook*
