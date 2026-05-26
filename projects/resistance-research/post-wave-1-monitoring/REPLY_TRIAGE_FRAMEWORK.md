---
title: "Reply Triage Framework — Domain 56 + Domain 39 Distributions"
created: 2026-05-27
version: 1.0
status: production-ready
scope: >
  Standalone triage guide for all replies received after Domain 56 (May 28) and Domain 39
  (June 1) sends. Five reply categories, per-category response protocols, escalation thresholds,
  and the escalation matrix for Phase 2 activation triggers.
distributions:
  domain_56_send: "May 28, 2026"
  domain_39_send: "June 1, 2026"
response_time_targets:
  category_1: "Same day"
  category_2: "Within 48 hours"
  category_3: "Within 48 hours"
  category_4: "Within 72 hours"
  category_5: "No action until Day 14"
---

# Reply Triage Framework — Domain 56 + Domain 39

**Version 1.0 — May 27, 2026**

**Lead finding**: A reply is not a win or a loss — it is a signal that must be classified within 24 hours of receipt, or you will miss the response window and lose the contact. Every reply maps to one of five categories. The category determines your response time, your response tone, and whether it triggers a Phase 2 escalation action. This document contains the classification logic, response scripts, and escalation matrix.

---

## The Five Categories

### Category 1: Implementation Signal

**Definition**: The contact expresses intent to use, adapt, or integrate Phase 1 materials into their organization's work. This includes explicit adoption statements, requests for permission to adapt, requests for a tailored version, and statements that materials have already been forwarded for operational use.

**Domain 56 indicators**:
- "We'd like to incorporate the Pendleton Act analysis into our H.R. 492 testimony"
- "Can we adapt the democratic-design framing for our litigation brief?"
- "I've shared this with our legal team — they want to use the APA analysis"
- "This would be useful for our civil service training curriculum"
- "We're citing this in our markup hearing submission"

**Domain 39 indicators**:
- "We're incorporating this in our public comment on the HHS rule"
- "Can we use the democratic participation argument in our state advocacy?"
- "I've forwarded this to our policy director for the Medicaid work requirement response"
- "This supports our maternal health coalition's framing on Medicaid"
- "We're including this in our brief for the state health commission"

**Engagement Score**: 4 (forward/collaboration request) or 5 (explicit citation or adoption statement).

**Response time**: Same day — within business hours of receiving the reply.

**Response protocol**:
1. Thank them specifically (reference the exact use they described, not a generic acknowledgment)
2. Confirm permission to use and adapt — blanket permission, no restrictions
3. Offer to connect by phone if they want to discuss application to their specific context (one sentence, keep low-pressure)
4. If they asked for a tailored version: commit to a timeline (24–48 hours for a summary; 5–7 days for a full adaptation)

**Dashboard action**:
- Update Engagement_Score to 4 or 5 in Contacts tab
- Set Tier2_Candidate to YES
- Add a row to Adoptions tab: Verification_Status = Confirmed or Probable depending on specificity
- If Score 5: immediate Phase 2 pre-activation — see Escalation Matrix below

**Sample response (Domain 56 — litigation use)**:

> Thank you for the quick reply — and yes, please use and adapt the Domain 56 analysis for your brief work on [case/submission]. There are no restrictions on adaptation. The APA arbitrary-and-capricious section (Section 4) and the Loper Bright statutory authority analysis (Section 5) are the most directly applicable to the PEER v. Trump litigation framing. If it would be useful to discuss the brief's specific needs, I'm happy to connect — otherwise, everything in the Gist is yours to use as you see fit.

**Sample response (Domain 39 — public comment)**:

> Thank you — the democratic participation argument in Domain 39 is exactly what we had in mind for this window. Please use and adapt freely. The June 1 HHS rule drops today, so I understand the urgency. Section 3 (Pathway 2: Civic Participation Infrastructure) has the most direct language for a public comment frame, and Section 5 has the comparative evidence. Let me know if you need any of the underlying citations in a different format.

---

### Category 2: Critique or Objection

**Definition**: The contact raises a substantive challenge to a claim, methodology, framing, or conclusion in the Phase 1 materials. This is intellectually engaged pushback — not a hostile reply and not a general question. The contact has read the document closely enough to identify something they disagree with.

**Domain 56 indicators**:
- "Your claim that the Pendleton Act was primarily a democratic infrastructure statute overstates the historical record"
- "The PEER v. Trump APA argument is stronger than you've framed it — the inadequate engagement with organizational comments is the lead, not the statutory authority question"
- "The Hungary comparison conflates electoral autocracy with executive overreach; they're different trajectories"
- "Your 'DOJ Voting Section: 30 to 6' figure needs a source — I can't verify it"

**Domain 39 indicators**:
- "The framing of healthcare access as electoral infrastructure overstates the causal link to voter participation"
- "The rural hospital closure figure of 417 facilities doesn't match the HRSA data I have access to"
- "The work requirement exemption analysis is outdated — HHS has since clarified its position on caretaker exemptions"
- "I agree with the substance but the 'democratic participation suppression' framing will alienate the HHS career staff you're trying to reach"

**Engagement Score**: 3 (substantive engagement even if critical).

**Response time**: Within 48 hours.

**Response protocol**:
1. Acknowledge the specific critique (not generically — say the thing they said)
2. One of three responses: (a) concede the point if valid; (b) provide supporting evidence if you have it; (c) acknowledge the ambiguity and explain your reasoning
3. Do not be defensive — a substantive critique from a domain expert is more valuable than a polite acknowledgment
4. Close with a question that invites continued engagement: "Does that address your concern, or is there a specific source you'd want to see cited?"

**Dashboard action**:
- Update Engagement_Score to 3 in Contacts tab
- Record the specific critique in the Key_Content column of the Replies tab
- If the same critique appears from 3+ contacts in a 14-day window: trigger the 30%+ critique rate escalation protocol (see Escalation Matrix)

**Framing note for Domain 39 critiques**: If a contact pushes back on the "healthcare as democratic infrastructure" framing specifically, this is a signal that the framing may be misaligned with HHS career staff or congressional staff audiences. The substantive argument (healthcare enrollment barriers reduce civic participation) may be sound even if the frame is wrong for the audience. Note any framing-specific critiques separately in the Replies tab — if 3+ contacts critique the framing (not the substance), that triggers a framing revision before Domain 39 Tier 2 outreach.

---

### Category 3: Data Request

**Definition**: The contact asks for additional data, sources, updated statistics, or a version of the materials in a different format. They are engaged enough to want more — this is a latent adoption signal.

**Domain 56 indicators**:
- "Do you have the H.R. 492 committee status confirmed? I can't find the current markup schedule"
- "Can you send the underlying citations in a bibliography format?"
- "Is there a condensed version suitable for sharing with congressional staff?"
- "Do you have updated figures on the Schedule Policy/Career reclassification numbers?"

**Domain 39 indicators**:
- "Can you provide the full Georgetown CCF citation for the Medicaid enrollment impact study?"
- "Do you have a slide deck version of the democratic participation framework?"
- "Is there a version of this framed specifically for state health department advocacy?"
- "What's the regulation citation for the HHS interim rule? I need to include it in our submission"

**Engagement Score**: 3.

**Response time**: Within 48 hours.

**Response protocol**:
1. Provide what was requested immediately if you have it (the Gist documents have sources sections — link to specific sections rather than the whole document)
2. If a new format is requested (slides, one-pager, Spanish): acknowledge the request, note it in the Key_Content column, and tell them your timeline
3. If multiple contacts request the same format: prioritize creating it — the format is the friction point, not the content

**High-priority data requests to turn around same-day**:
- H.R. 492 committee markup schedule (check Congress.gov, takes 5 minutes)
- Updated HHS rule regulation citation (check Federal Register)
- Bibliography-format citation list (Gist sources section is already formatted — copy and paste)

**Dashboard action**:
- Update Engagement_Score to 3
- Note format request in Key_Content if applicable
- If same format requested by 3+ contacts, add to CHECKIN.md under "Materials to Create"

---

### Category 4: General Question

**Definition**: The contact asks about the framework without expressing intent to adopt and without raising a critique. These are orientation questions — they haven't decided yet.

**Domain 56 indicators**:
- "Who produced this research?"
- "Is this peer-reviewed?"
- "What organization are you affiliated with?"
- "What's the publication status of this?"
- "How does this relate to the current Schedule Policy/Career debate?"

**Domain 39 indicators**:
- "What's the intended use of Domain 39?"
- "Is this connected to a larger organization?"
- "What's your background in healthcare policy?"
- "I'm not sure how this connects to our Medicaid work — can you clarify?"

**Engagement Score**: 2.

**Response time**: Within 72 hours.

**Response protocol**:
1. Answer the question directly and briefly (2–3 sentences max per question)
2. Close with one question that invites them to describe their current work: "Are you working on anything where the [civil service / healthcare] democratic-infrastructure framing might be useful?"
3. Do not pitch — let them move toward adoption on their own timeline
4. On peer review question: answer honestly — this is independently produced research, not formally peer-reviewed, but it draws on peer-reviewed sources throughout and cites them transparently

**Dashboard action**:
- Update Engagement_Score to 2
- Note that they replied — this contact is no longer in the No Reply category
- Check back at Day 30: if they haven't moved to Category 1–3 by then, they are in the WEAK constituency data

---

### Category 5: No Reply

**Definition**: No reply by the checkpoint date. The most common outcome.

**What it is not**: a failure signal by itself. No reply at Day 7 is normal. No reply at Day 14 in the context of 0 Bitly clicks is a monitoring flag. No reply at Day 30 is a data point in the WEAK threshold calculation.

**Engagement Score**: 0.

**No action required until Day 14** — see DAY_7_14_30_DECISION_TREES.md for checkpoint logic.

**Special cases for No Reply**:

*Government Executive (editors@govexec.com)*: Publication pitches take 5–10 business days. Do not score as No Reply before June 10. After June 10 with no reply, that contact is in the No Reply category.

*CREW (contact form submission)*: Form submissions have no delivery confirmation. If you submitted the form and received no confirmation, attempt resubmission or find a direct email via their website. Do not score as No Reply until you have confirmed delivery.

*Any contact whose OOO return date is after Day 7*: Record the OOO reply in the Replies tab as Score 1. Add their return date to the Notes column. Check for a substantive reply after their return date before scoring as No Reply.

---

## Classification Decision Tree

When a reply arrives, run this sequence:

```
REPLY RECEIVED
      |
      v
IS THIS AN OUT-OF-OFFICE AUTORESPONSE ONLY?
      |
   YES -> Score 1. Note return date. No action.
      |
      v
DOES THE REPLY CONTAIN ANY OF THESE?
  - "incorporate / use / adapt / curriculum / training / brief / clinic"
  - "forwarded / shared with / passed to"
  - "we are / we plan to / we would like to"
  - "citing this in / including this in"
      |
   YES -> Category 1: Implementation Signal
          Score 4 or 5. Respond same day.
          Record in Adoptions tab.
      |
      v
DOES THE REPLY CHALLENGE A SPECIFIC CLAIM,
METHODOLOGY, DATA POINT, OR FRAMING?
      |
   YES -> Category 2: Critique or Objection
          Score 3. Respond within 48 hours.
          Record critique text in Replies tab.
      |
      v
DOES THE REPLY REQUEST ADDITIONAL DATA,
SOURCES, OR A DIFFERENT FORMAT?
      |
   YES -> Category 3: Data Request
          Score 3. Respond within 48 hours.
      |
      v
DOES THE REPLY ASK A GENERAL QUESTION ABOUT
THE FRAMEWORK, ITS ORIGIN, OR ITS USE?
      |
   YES -> Category 4: General Question
          Score 2. Respond within 72 hours.
          Close with one forward-looking question.
      |
      v
IS THE REPLY A POLITE ACKNOWLEDGMENT
WITH NO SPECIFIC ENGAGEMENT?
      |
   YES -> Score 2. Category 4 protocol.
          Respond within 72 hours.
```

---

## Escalation Matrix

### Trigger 1: Score 5 Reply — Immediate Phase 2 Pre-Activation

A Score 5 reply is: explicit citation or adoption statement, institutional integration statement, or a request to co-author, brief colleagues, or build on the framework for a publication.

**Score 5 in Domain 56**: A reply from any contact stating they are citing Domain 56 in a formal document (brief, testimony, report) or incorporating it into a program.

**Score 5 in Domain 39**: A reply from any contact stating they are citing Domain 39 in a public comment, policy brief, or formal advocacy document.

**When Score 5 is received — execute same day, regardless of checkpoint schedule**:
1. Update CHECKIN.md: "SCORE 5 RECEIVED — [date, org name, domain, brief description]"
2. Run the Phase 2 pre-activation checklist from PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md Section 6.1
3. Pull the Tier 2 contact list for the relevant domain
4. Within 48 hours: send Tier 2 outreach using the social proof framing ("this framework has been cited by [org name from Score 5 reply]")
5. Log in Adoptions tab: Verification_Status = Confirmed, Signal_Type = the specific adoption type

### Trigger 2: 30% Critique Rate — Messaging Pivot Signal

Calculate: (Number of Category 2 replies in any 14-day window) / (Total replies in same window) >= 0.30

**What 30% critique rate means in practice**: With 11 Domain 56 contacts, if you receive 7 replies and 3+ are substantive critiques, that is >= 30%. With 5 Domain 39 contacts, 2 critiques out of 4 replies reaches 50%.

**Response to 30%+ critique rate**:
1. Add to CHECKIN.md: "Critique rate [X]% — messaging review needed. Domain [56/39]."
2. Review all critiques for common themes — do they cluster around a single claim, a framing choice, a data source, or the overall argument?
3. **If critiques cluster around a factual claim**: verify and either correct or add a caveat to the Gist document
4. **If critiques cluster around framing**: revise the outreach email subject line and opening paragraph — address the critique directly ("Some colleagues have raised questions about the democratic-infrastructure framing — here is how I'm thinking about it..."). Do not revise the underlying Gist documents in response to email critiques without separate deliberate review.
5. **If the critique is valid and significant**: flag in CHECKIN.md under "Needs Your Input" with the specific claim being challenged and the evidence cited by the contact

### Trigger 3: Zero Clicks After 7 Days with Confirmed Delivery

If Week 1 Bitly clicks are 0–4 across both domains combined, and you have confirmed that emails were sent and not bounced:

1. Test your Bitly links manually: click each short link yourself and verify the counter increments
2. If a link is broken (does not resolve, does not increment): delete and recreate the short link; send a brief follow-up to all contacts with the corrected link: "Quick correction to my previous email — the correct link is [new Bitly URL]. My apologies for any confusion."
3. If links work but clicks are zero: the emails may have reached spam filters. Check whether your outreach email domain has any spam reputation issues (check MXToolbox if you're using a custom domain; use Gmail's native spam testing if sending from Gmail)
4. If spam is confirmed: resend from an alternative address (personal Gmail vs. organizational domain) with a modified subject line

### Trigger 4: Domain 39 — Non-Reply Before June 3

Because of the June 1 HHS hard stop, Domain 39 contacts who have not responded by June 3 (72 hours after the last send) need a news-hook follow-up immediately.

**June 3 follow-up template for Domain 39 non-respondents**:

Subject: `HHS OBBBA Rule Now Published — Domain 39 democratic participation analysis`

```
The HHS interim final rule on OBBBA Medicaid work requirement implementation 
was published today/yesterday. I wanted to follow up on the Domain 39 research 
I sent — the democratic participation argument is directly relevant to the 
implementation choices that remain within HHS's discretion even under this rule.

The analysis is at: [drp-d39 Bitly link]

Section 3 (Pathway 2) and Section 5 (state flexibility) are the most actionable 
for immediate implementation advocacy. Let me know if there's a format or framing 
that would be more useful for your current work.

[NAME]
```

Do not send this follow-up to anyone who has already replied. Do not send more than one follow-up to any contact.

---

## Escalation Summary Table

| Trigger | Threshold | Action | Timeline |
|---------|-----------|--------|----------|
| Score 5 reply | Any single reply | Phase 2 pre-activation | Same day |
| Score 4 reply (2+ total) | 2 or more Score 4s | Flag in CHECKIN.md as "Pre-Day 30 STRONG signal" | Same day |
| 30%+ critique rate | >= 30% of replies in 14 days | Messaging pivot review | Within 48 hours |
| Zero clicks, confirmed delivery | 0–4 clicks in Week 1 | Test Bitly links; investigate delivery | Same day |
| D39 non-reply by June 3 | No reply from any D39 contact | June 3 follow-up with rule news hook | June 3 |
| 3+ cross-org references | 3 confirmed referrals | Add STRONG threshold check to CHECKIN.md | Within 24 hours |

---

## Domain-Specific Response Priority Stack

**Domain 56** (civil service, H.R. 492 window):
1. Democracy Forward — highest priority reply to; litigation use is Phase 2 accelerant
2. Volcker Alliance — second priority; civil service policy org with bipartisan credibility
3. CREW — third priority; watchdog with media reach
4. Government Executive — different cadence (10 days for editorial response)
5. Tier 1 contacts (Partnership for Public Service, GAP, AFGE, NTEU, Protect Democracy) — same-day response if Score 4+

**Domain 39** (healthcare, HHS June 1 window):
1. Georgetown CCF — highest priority; their reply carries credibility signal for all subsequent sends
2. NHeLP — second priority; litigation-oriented healthcare org
3. Brennan Center — third priority; democracy + healthcare intersection
4. IRG and Black Mamas Matter — respond within 72 hours per standard protocol

---

*This framework applies from May 28 through Day 60. After Day 60, reply volume should have decreased to a manageable trickle and individual judgment governs. All scoring definitions are compatible with the Contacts tab schema in PHASE_1_IMPACT_MONITORING_DASHBOARD.md.*
