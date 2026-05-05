---
title: "Tier 1 Feedback Collection Protocol"
project: cybersecurity-hardening
created: 2026-05-05
status: ready-for-use
item: 42 — Tier 1 Success Metrics & Feedback Loop Architecture
depends-on: tier-1-success-metrics-framework.md, post-distribution-impact-tracker.md, feedback-collection-template.csv
---

# Tier 1 Feedback Collection Protocol

**Lead finding**: Feedback design is a deployment choice, not a reporting choice. Most feedback protocols fail because they ask too much, ask too late, or ask in ways that require recipients to compose a substantive response. This protocol is built around the constraint that busy legal aid staff at high-volume immigration organizations have less than 60 seconds available for a follow-up from an external sender. Every request is calibrated to that ceiling.

---

## 1. Survey Design: Three Questions for Initial Contact Replies

When a Tier 1 contact replies to the initial outreach email, use the first reply exchange to collect three data points. Do not send a separate survey form. Collect feedback conversationally within the existing email thread.

**The three questions are not asked simultaneously.** They are embedded at natural points in the conversation depending on what the contact's reply indicates.

### Question 1: Discovery and Routing

**When to ask**: In your reply to any Stage 0 or Stage 1 response (routing message or initial positive).

**Ask**: "Could you let me know if this reached the right person at your organization for client digital security resources? If not, any routing would be helpful."

**What you are measuring**: Whether your initial contact point is the right person. A single routing correction can determine whether the corpus gets reviewed by someone with decision-making authority or sits in a general inbox.

**What a good answer looks like**: "I'm forwarding this to our client services director" or "You want our Tech team — I'll CC them." A routing answer is not a conversion, but it moves the contact from Stage 0 to Stage 1 and opens a new contact relationship.

### Question 2: Domain and Section Relevance

**When to ask**: In your reply to any Stage 1+ response (positive interest, questions, or "will review").

**Ask**: "Which section are you most interested in — the threat model documentation, the Part 0 data broker opt-outs, or the device implementation guide? That helps me know how to follow up."

**What you are measuring**: Which part of the corpus is driving interest. This determines where to invest revision effort and what to lead with in follow-up communications. If 70% of responses identify Part 0 as their primary interest, the next iteration of the corpus should begin with Part 0 rather than the threat model.

**What a good answer looks like**: "Mainly Part 0 — our clients need to take these steps immediately" or "The threat model is what I want to show our litigation team." Both answers tell you something concrete about how the corpus is being used.

### Question 3: Institutional Barriers

**When to ask**: In the 30-day follow-up email (see Section 3 below), not in the initial reply exchange. Asking about barriers before the contact has reviewed the corpus produces speculative answers.

**Ask**: "If any of your staff or clients have looked at the guide — are there any barriers that made implementation difficult? Technical complexity, language, or format are the most common ones we hear."

**What you are measuring**: What prevents the corpus from being actionable. The three most common barriers in civil society security guidance are: (1) technical complexity above staff capacity, (2) language (Spanish-language gap), (3) format mismatch (long Gist vs. short printable handout). Each has a documented fix.

**What a good answer looks like**: "Our clients don't have laptops — the device sections aren't relevant for them" or "We need a Spanish version of Part 0." Both drive specific product improvements for Phase 2.

---

## 2. Follow-Up Cadence

Three structured follow-up touchpoints. Each is designed to produce a specific category of data and to function even if the previous touchpoint received no reply.

### Week 1 Post-Send: Delivery Check-In

**Timing**: 7 calendar days after initial send.

**Trigger**: Only send if no reply received. If a reply was received at any stage, manage through the reply thread rather than this template.

**Template**:

> Subject: Re: [Original subject line] — quick check-in
>
> Hi [Name] — I wanted to follow up on the digital security guide I sent on [Date]. Just checking it reached you and didn't get buried. No action required — a quick reply to confirm receipt would be helpful.
>
> [Your name]

**What you are measuring**: Deliverability. A non-response after 7 days may indicate a spam filter, wrong contact, or organizational chaos (common in immigration legal organizations under current enforcement pressure). It is not an adoption failure at this stage.

**Action on non-response**: If no reply at Day 7, make one subject line adjustment. The most common Week 1 failure mode is the subject line landing in spam or being triaged as low-priority. Test: "Following up re: Palantir ELITE data broker documentation for immigration legal teams" — more specific, less likely to be filtered.

### 4-Week Adoption Signal Inquiry

**Timing**: 28–30 calendar days after initial send, regardless of initial reply status.

**Trigger**: Send to all 12 named contacts. Even organizations that replied positively benefit from a structured 30-day check-in — it keeps the corpus in their workflow rather than archived.

**Template**:

> Subject: 30-day check-in — OpSec corpus for [Organization Name]
>
> Hi [Name] — a month since I sent the digital security corpus for immigration legal teams. A brief check-in:
>
> 1. Did the document reach the right person for client digital security resources? (Reply: yes / no — should go to [Name])
> 2. Has anyone at [Org] had a chance to look at it?
> 3. Is there a colleague or partner organization who should also have this?
>
> That's the full ask. Any reply, even a single word per question, is useful.
>
> [Your name]

**What you are measuring**:
- Question 1: Routing verification (is this in the right hands?)
- Question 2: Stage-of-adoption signal (beyond receipt)
- Question 3: Referral generation (the most valuable question in the sequence)

**Key design choice**: Question 3 is framed as "partner organization" rather than "other contacts." This is deliberate — immigration legal aid staff think in terms of their network of partner organizations, not individual contacts. A response naming a partner organization produces a warm introduction that is more actionable than a cold contact.

**Success signal threshold**: 40% reply rate within 14 days of this follow-up email (i.e., by Day 42–44 post-initial send) = baseline success. This is consistent with the post-distribution-impact-tracker.md target of 35% Tier 1A acknowledgment rate at 30 days. 60%+ = strong engagement. Below 20% after this follow-up = reassess contact list and subject lines before Tier 2 launch.

### 12-Week Impact Assessment

**Timing**: 84–90 calendar days after initial send.

**Trigger**: Send to all contacts that showed Stage 1+ engagement at any prior point (replied, clicked, or acknowledged). Do not send to contacts that explicitly declined follow-up.

**Template**:

> Subject: 90-day check-in — digital security corpus impact
>
> Hi [Name] — three months since the OpSec corpus for immigration legal teams reached you. Three short questions:
>
> 1. Has [Org] reviewed or used any part of the guide? (Yes / Partially / Not yet / Not the right fit)
> 2. What's the biggest gap — what should the guide cover that it currently doesn't?
> 3. Any barriers to implementation we should know about? (Technical complexity, language, format)
>
> Your feedback directly shapes the next version. Reply with just the numbers if that's easier.
>
> [Your name]

**What you are measuring**:
- Question 1: Stage-of-adoption (quantifiable conversion data)
- Question 2: Content gaps for Phase 2 corpus update
- Question 3: Structural barriers for format decisions

**Action on responses**: Log all verbatim answers in `feedback-collection-template.csv` under `feedback_summary`. Flag answers that match three priority gap categories: Spanish language, phone-only access (no laptop), and legal-professional-grade citation. If two or more organizations cite the same gap, treat it as a required update before Tier 2 launch.

---

## 3. CRM Integration Approach

The campaign does not require a full CRM system. The tracking spreadsheet described in `TIER1_EXECUTION_RUNBOOK.md` is sufficient for 12–25 contacts. The following field structure ensures that all feedback-relevant data is captured in one place.

### Required Fields (Minimum Viable Tracking)

| Field | Type | Purpose |
|---|---|---|
| `organization` | Text | Full name of organization |
| `contact_name` | Text | Named contact or "general" |
| `contact_email` | Text | Email address used |
| `org_type` | Enum (1A/1B/1C) | Legal Aid / Community / Mutual Aid |
| `date_sent` | Date | Initial send date |
| `reply_received` | Boolean | Y/N |
| `reply_date` | Date | Date of first reply |
| `reply_type` | Enum | None / Positive / Routing / MoreInfo / Negative / Conversion |
| `reply_content_summary` | Text | 1–2 sentence verbatim or near-verbatim summary |
| `stage_of_adoption` | Integer (0–5) | Per the stage model in post-distribution-impact-tracker.md |
| `week1_followup_sent` | Boolean | Y/N |
| `week1_followup_reply` | Text | Brief summary |
| `day30_followup_sent` | Boolean | Y/N |
| `day30_q1_routing_correct` | Boolean | Y/N |
| `day30_q2_reviewed` | Text | Yes / Partially / Not yet |
| `day30_q3_referral` | Text | Organization name or blank |
| `day90_followup_sent` | Boolean | Y/N |
| `day90_q1_adoption_status` | Text | Yes / Partially / Not yet / Not right fit |
| `day90_q2_gap_identified` | Text | Verbatim gap description |
| `day90_q3_barrier` | Text | Verbatim barrier description |
| `referral_count` | Integer | Net new warm contacts from this organization |
| `adoption_signal_date` | Date | First observable adoption action |
| `case_study_eligible` | Boolean | Y/N (Stage 3+ at 90 days) |
| `notes` | Text | Any additional context |

### Fields That Drive Phase 2 Adaptation

Four fields in the above structure are specifically for feeding Phase 2 strategy:

1. **`day90_q2_gap_identified`**: Aggregate across all responses. Top two mentioned gaps become required updates before Tier 2 launch.
2. **`day90_q3_barrier`**: Aggregate for format decision (if 3+ contacts mention phone-only access, produce a mobile-optimized standalone handout).
3. **`day30_q3_referral`**: Every non-blank response here is a Tier 2 warm contact. Prioritize these over cold Tier 2 contacts.
4. **`reply_content_summary`**: Preserves verbatim language that may contain unique content marker references (DROP platform, address confidence scores). These are your highest-confidence attribution signals.

---

## 4. Success Signal Thresholds

These thresholds translate the per-organization tracking into campaign-level go/no-go decisions.

### 14-Day Assessment (After First Week of Sends)

| Signal | Threshold | Interpretation | Action |
|---|---|---|---|
| Any reply received | At least 1 of 12 | Baseline deliverability confirmed | No action required |
| Reply rate | ≥25% (3+ of 12) | On-track for strong engagement | Proceed as planned |
| Stage 1+ responses among replies | ≥50% of replies | Message reaching right contacts | No action required |
| Zero replies | 0 of 12 | Deliverability failure or wrong contacts | Check spam folder; verify contact addresses; test subject line variant |

### 30-Day Assessment

| Signal | Threshold | Strong | Below Threshold |
|---|---|---|---|
| Overall reply rate | ≥40% (5+ of 12) | ≥60% (7+) | Below 25% → message or deliverability problem |
| Stage 1+ rate among replies | ≥50% | ≥70% | Below 30% → content not reaching right person |
| Referrals generated | ≥2 new warm contacts | ≥4 | 0 → add referral prompt to follow-up template |
| Bitly click trajectory | 10+ incremental clicks beyond initial sends | 25+ | Flat → Gist URL may be blocked or filtered |

### 90-Day Assessment (Primary Gate for Tier 2 Launch)

| Signal | Threshold | Exceeded | Below Threshold |
|---|---|---|---|
| Organizations with Stage 2+ adoption | ≥2 of 12 (17%) | ≥4 (33%) | 0 → reassess corpus format before Tier 2 |
| Adoption signal rate | ≥15% (2+ orgs with observable adoption action) | ≥25% | Below 10% → corpus reaching wrong contact level; try escalation to organizational leadership |
| Referral factor | ≥1.5 (new contacts generated / sends completed) | ≥2.0 | Below 1.0 → secondary distribution not happening |
| Gap documentation complete | At least one gap identified and logged | 3+ distinct gaps | None → follow-up questions not reaching Stage 1+ contacts |

**Referral factor definition**: Total new warm contacts generated through Question 3 referrals, divided by the number of initial sends completed. A referral factor of 1.5 means the 12 initial sends produced 18 total relationships (12 original + 6 referred). This is the secondary distribution metric that indicates whether the corpus is spreading beyond direct outreach.

---

## 5. Privacy Considerations

### GDPR and Institutional Data Handling

The outreach campaign involves collecting names, email addresses, organizational affiliations, and reply content from contacts at U.S.-based nonprofit organizations. Most of these contacts are not EU residents, and the organizations are not EU institutions, but applying GDPR-equivalent data hygiene is both ethically sound and reduces organizational risk.

**Data minimization**: Collect only what is needed for follow-up and campaign analysis. Do not log reply content beyond a 1–2 sentence summary. Do not log information volunteered about an organization's clients or client identities.

**Storage security**: The tracking spreadsheet contains identifiable contact information. Store in:
- Google Sheets with access restricted to the sender's email address only (not shared with anyone else)
- Or a local CSV protected with device-level disk encryption
- Not in a public GitHub repository or shared workspace

**Retention limit**: Contacts that explicitly decline follow-up ("please remove me from your list") should be logged as `status = Closed` and not contacted again. Delete their personal data from the spreadsheet within 30 days of that request.

**Sensitive reply content**: If a contact's reply reveals organizational security vulnerabilities, client case details, or information about organizational capacity that could be harmful if disclosed, treat this as confidential and do not summarize it in external reports or Phase 2 outreach communications.

### Anonymization for Reporting

Any impact summary or Phase 2 outreach communication that references Tier 1 feedback results should use anonymized reporting:

- Acceptable: "Two Tier 1 immigration legal organizations reported using Part 0 with clients in the first 90 days."
- Not acceptable: "RAICES and CLINIC have implemented Part 0 guidance with their clients."

The exception is when an organization explicitly gives permission to be named. Ask at the 90-day or 180-day case study stage: "Would [Org Name] be comfortable being referenced by name in future outreach, or should I keep it anonymous?" Log the response and honor it.

### Contact Reuse Policy

Contact information collected during this campaign should not be reused for any purpose other than follow-up on this specific corpus. Do not add Tier 1 contacts to any general mailing list, marketing campaign, or separate advocacy effort without their explicit consent.

---

*Protocol complete. All templates above are immediately deployable. The three follow-up templates (Week 1, Day 30, Day 90) should be saved as Gmail draft templates before beginning the Day 1 send. Cross-reference `post-distribution-impact-tracker.md` Section 2 for the 180-day case study interview protocol.*
