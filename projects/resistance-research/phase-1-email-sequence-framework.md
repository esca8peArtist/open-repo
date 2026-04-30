---
title: "Phase 1 Email Sequence Framework — Multi-Touch Nurture Sequence"
created: 2026-04-30
status: ready-to-execute
path-agnostic: true
purpose: "3–5 touchpoint nurture sequence over 4 weeks for Tier 1 institutional contacts. Timing, personalization triggers, success metrics per sequence step."
companion_files:
  - phase-1-outreach-email-templates.md
  - phase-1-contact-list-structure.md
  - phase-1-substack-setup-guide.md
  - distribution-institutional-outreach-templates.md
---

# Phase 1 Email Sequence Framework — Multi-Touch Nurture Sequence

**Purpose**: This document specifies the timing, content, and success metrics for a 3–5 touchpoint institutional engagement sequence per Tier 1 contact. The sequence is designed to move a contact from cold (no relationship) to engaged (feedback, referrals, or distribution) within 28 days — or to identify that the contact is not currently available for engagement and move on without wasted effort.

**Underlying logic**: Institutional policy professionals receive many cold outreach emails. The ones that convert do so because: (a) the research is immediately useful to their current work, (b) the sender has clearly read their recent publications, and (c) the ask is low-friction and reciprocal (feedback, not sales). Each touchpoint in this sequence is designed to provide value before requesting action. Touchpoints that add no new value are not included — this is a 3–5 step sequence, not a 7-step cadence, because longer sequences lose institutional contacts who feel they are in a sales funnel.

---

## Sequence Overview

| Step | Timing | Email Type | Primary Purpose | Success Metric |
|------|--------|-----------|----------------|----------------|
| 1 | Day 0 | Primary Outreach | Establish contact, deliver materials, request feedback | Open; any response |
| 2 | Day 3–5 | Substack Share | Provide new value (post they haven't seen), deepen connection | Click or comment on Substack post |
| 3 | Day 10–14 | Follow-Up | Re-surface primary email for non-responders | Response from previously non-responding contact |
| 4 | Day 16–21 | Relevance Deepen | Specific domain content tied to their recent publication | Substantive engagement — feedback or question |
| 5 | Day 28 | Relationship or Close | Either deepen an emerging relationship or close the loop gracefully | Referral or confirmed non-engagement |

Not all contacts will receive all 5 steps. Steps 2 and 4 are conditional on Substack being live and specific domain content being available. If a contact responds after Step 1, proceed directly to the Relationship-Building template — the remaining steps are only for non-responding contacts.

---

## Step 1: Primary Outreach (Day 0)

**Template**: Primary Outreach (Template 1 from `phase-1-outreach-email-templates.md`)

**Timing**: Send between 9:00 a.m. and 11:00 a.m. in the recipient's time zone, Tuesday through Thursday. Monday morning emails compete with weekend backlog. Friday emails sit over a weekend. Tuesday–Thursday 9–11 a.m. is the consistently highest-performing window for professional institutional outreach.

**Content checklist**:
- [ ] Contact name is verified current (check institution staff page day-of)
- [ ] Personalization paragraph references a specific publication by the institution published within the past 6 months
- [ ] Domain bullet points selected from Section 4 of `phase-1-outreach-email-templates.md` for this institution type
- [ ] All `{{placeholder}}` fields filled — none remain
- [ ] All Gist links verified live (click each link yourself before sending)
- [ ] Subject line variant recorded in contact database (`phase-1-contact-list-structure.md`)
- [ ] Email sent from the same address as your Substack account (so replies go to one inbox)

**Success metrics**:
- Primary: Any response (acknowledgment, question, feedback, forwarding offer)
- Secondary: Email opened (if you are using a tracked sending tool)
- Failure signal: No response after 14 days AND email not bounced

**Personalization trigger check**: Before sending, confirm: "If I received this email, would I know it was written specifically for me, or does it read like it was sent to 100 people?" If the latter, revise the personalization paragraph.

---

## Step 2: Substack Share (Day 3–5)

**Precondition**: This step requires that your Substack is live and has published at least one post relevant to this contact's work (Post 1 from the series is sufficient; a domain-specific post is better). If Substack is not yet live on Day 3–5, skip this step and proceed to Step 3 on Day 10–14.

**Template**: Short, value-added email. Not a template in the traditional sense — write it fresh based on the specific post you are sharing. The email should be 4–6 sentences.

**Purpose**: This step serves two functions. First, it provides new value (a post they have not seen) without requiring them to respond to the initial email. Second, it establishes that you are producing ongoing work, not sending a one-time outreach.

**Content structure**:

---

{{contact_name}},

Sharing a Substack post that's directly relevant to {{institution}}'s work on {{specific_area}} — it covers {{one-sentence summary of what the post covers}} with a particular focus on {{the angle most relevant to this contact}}.

{{Post title and URL}}

The post builds on the {{domain name}} analysis I shared last week. The full domain document is at {{domain_specific_url}} if you haven't had a chance to look yet.

{{your_name}}

---

**What not to do**: Do not re-send the original email. Do not ask again for feedback in this step. Do not attach documents. Keep it short — this is a value delivery, not a sales follow-up.

**Success metrics**:
- Primary: Click on Substack link (measurable if you track Substack analytics)
- Secondary: Reply to this email (even a one-line acknowledgment)
- Failure signal: No response + no Substack engagement; proceed to Step 3

**Personalization trigger**: The "particular focus on {{the angle most relevant to this contact}}" sentence is the key personalizer. If you cannot write it specifically — if the post is not actually relevant to their specific work — skip this step and go directly to Step 3.

---

## Step 3: Follow-Up (Day 10–14)

**Trigger**: Send only if no response received to Step 1 (and Step 2 if applicable). If a response was received at any earlier step, skip Step 3 and go to relationship-building (see Step 5).

**Template**: Follow-Up (Template 2 from `phase-1-outreach-email-templates.md`)

**Timing**: 10 days after primary email is the minimum. 14 days is better — it signals patience rather than urgency. Do not follow up at 7 days; the implicit message is that you are managing a pipeline, not building a relationship.

**Key principle**: The follow-up is shorter than the primary email. It does not add new information. Its sole function is to resurface the primary email in the recipient's inbox during a moment when they have bandwidth. The "No response necessary if the timing isn't right" sentence is load-bearing — it reduces cognitive burden and signals you are not a vendor.

**Content calibration by contact type**:

For law school contacts: Lead with the Litigation Tracker URL. Legal researchers often engage with a specific, immediately actionable document before engaging with a broader framework.

For think tank contacts: Lead with the Executive Summary. Think tank researchers are high-volume consumers of research — the two-page summary respects their time.

For policy organizations: Lead with the tracker most relevant to their active campaigns. If they are doing election protection work, lead with the election protection angle of Domain 37. If they are doing environmental advocacy, lead with the Environmental Rollbacks Tracker.

**Success metrics**:
- Primary: Any response within 7 days of follow-up
- Secondary: Substack subscription after follow-up
- Failure signal: No response after 7 days post-follow-up; move to Step 5 (graceful close)

**Do not send a second follow-up after this one** for cold contacts. For warm contacts (mutual connection), a second follow-up at Day 28 is appropriate — reference the mutual connection in the subject line.

---

## Step 4: Relevance Deepen (Day 16–21)

**Trigger**: Send only if Step 3 generated a response that opened a conversation but did not move to full engagement — for example, a brief acknowledgment ("Thanks, will look at this") without substantive engagement, or a response expressing interest but not yet asking questions or offering feedback.

**This step is conditional**: Do not send Step 4 to all non-engaging contacts. Use it specifically when a contact has shown some signal of interest (open, click, brief response) but has not yet engaged substantively. If there is no engagement signal, proceed to Step 5 (graceful close) instead.

**Template**: Write fresh, based on their most recent publication or public statement. The Step 4 email is the most personalized in the sequence.

**Purpose**: Connect a specific piece of their recent public work to a specific section of the research. Show them, concretely, how the research is relevant to what they are currently doing — not how it is generally relevant to their field.

**Content structure**:

---

{{contact_name}},

I came across {{institution}}'s recent {{publication/testimony/report — title}} — specifically the section on {{specific argument or finding}}.

The research in Domain {{N}} addresses the structural dimension of what you've identified: {{one sentence connecting their argument to the proposal's structural analysis}}. The specific section is {{section number or heading}} at {{Gist URL}}. 

I think the {{international precedent or reform proposal from the domain}} would either confirm or challenge the {{specific claim from their work}} — and I'd be curious whether you see it the same way.

{{your_name}}

---

**Why this structure works**: You are not re-pitching the research. You are engaging with their intellectual work and showing how the two sets of thinking connect. The closing question invites a response that is analytically substantive, not politely obligatory.

**What to avoid**: Do not make this email long. Two or three short paragraphs maximum. Do not re-attach documents. Do not re-list the full scope of the proposal.

**Success metrics**:
- Primary: Substantive reply engaging with the analytical question
- Secondary: Request to discuss further (call, meeting, email thread)
- Failure signal: No response within 7 days; proceed to Step 5

---

## Step 5: Relationship Deepening or Graceful Close (Day 28)

**This step branches based on the contact's response history.**

### Branch A — Relationship Deepening (for contacts who have engaged)

Use the Relationship-Building template (Template 3 from `phase-1-outreach-email-templates.md`). The specific conditional blocks to use:

**If they gave feedback**: Acknowledge specifically what they said, commit to incorporating it, and ask for one more specific input or a referral. This is the highest-value outcome — turn feedback into an ongoing intellectual relationship.

**If they offered to share or forward**: Follow up on what happened with that sharing. Ask if they know of a specific person who engaged with it. This is both good tracking and an opportunity to extend the relationship to their network.

**If they asked questions about a specific domain**: Provide a detailed response to the question, with the specific section number and relevant international precedents. Then ask the follow-up analytical question that naturally arises from their question. This turns a question into a substantive exchange.

### Branch B — Graceful Close (for contacts with no engagement after Steps 1–4)

Do not send a final email that asks one more time for engagement. The graceful close is internal — update the contact database with status "Cold — no engagement" and move them to the dormant list.

**Exception**: If you subsequently publish a Substack post that is directly, specifically relevant to their work — not generally relevant, but directly relevant to something they have published — a single post-notification email is appropriate at any time. This is not a follow-up; it is a value delivery.

**Re-engagement window**: Contacts who did not engage in the initial 28-day sequence can be re-engaged after 60 days if: (1) the framework has been updated with content directly relevant to their work, or (2) an institutional development (court ruling, legislative action) makes the research more timely for their docket.

---

## Success Metrics Per Sequence Step (Consolidated)

| Step | Primary Success | Secondary Success | Move-On Signal |
|------|----------------|-------------------|----------------|
| Step 1 (Primary) | Substantive response | Any response | No response, 14 days |
| Step 2 (Substack) | Link click + reply | Substack subscription | No click, no reply |
| Step 3 (Follow-Up) | Response from non-responder | Any reply | No response, 7 days post-follow-up |
| Step 4 (Deepen) | Substantive analytical engagement | Request for further discussion | No response, 7 days |
| Step 5A (Deepen) | Referral or ongoing feedback relationship | Follow-on question or co-research interest | Engagement drops after initial warmth |
| Step 5B (Close) | Relationship updated correctly in database | — | — |

### 30-Day Sequence Health Metrics

At the end of 28 days across all Tier 1 contacts, a healthy Phase 1 outreach operation looks like:

- **Response rate**: 20–35% of contacts respond to Steps 1–3 (industry benchmark for cold institutional outreach is 15–20%; personalized research outreach should exceed this)
- **Engagement rate**: 10–15% of contacts move to substantive engagement (feedback, referral, distribution)
- **Referrals generated**: 3–8 new contacts introduced by Tier 1 contacts (each Tier 1 contact has potential to introduce 1–3 Tier 2 contacts)
- **Tracker contributions**: 1–2 organizations contribute documentation to the trackers (a signal of deep engagement)
- **Substack subscribers from outreach**: 5–15 (not the primary goal, but a secondary health signal)

If response rate is below 10% after Batch 1, review: (a) whether the personalization paragraph is specific enough, (b) whether the domain emphasis is well-matched to the institution, and (c) whether the contacts are currently in the role listed. Low response rates are almost always an accurate feedback signal rather than a noise problem.

---

## Personalization Triggers — Quick Reference

These are the conditions under which a personalization decision is made at each step:

| Trigger | Decision |
|---------|---------|
| Contact has published in the past 6 months on a topic covered in the proposal | Use that publication in the personalization paragraph |
| Contact's institution has an active case in the Litigation Tracker | Reference the case specifically; offer the tracker as a working resource |
| Contact responded with feedback | Respond within 48 hours; commit to specific incorporation; do not let the thread go cold |
| Contact responded with a brief acknowledgment but no substance | Send Step 4 (Relevance Deepen) with their most recent publication as the hook |
| Contact has not responded after Step 3 and there is no engagement signal | Close gracefully; do not follow up a fourth time |
| A new Substack post publishes that is directly relevant to a non-engaging contact | Single post-notification email regardless of where they are in the sequence |
| A new court ruling, legislation, or executive action directly affects a domain relevant to this contact | Single update email regardless of sequence stage — timely relevance overrides sequence timing |

---

## Email Sending Logistics

**Send from**: Your primary professional email (the same address as your Substack account). Do not use a bulk-sending tool for Tier 1 outreach — institutional contacts can tell, and it undermines the relationship-building frame.

**Tracking**: Use Gmail's "Read Receipts" (or equivalent) sparingly — some professional recipients find read receipts intrusive. Better: use your Substack analytics to track link clicks for contacts you've referred to specific posts.

**Calendar blocking**: Block time for email responses at 48-hour intervals. Institutional outreach that receives a warm response and then goes cold for 5+ days loses the relationship. Response time is the single most controllable quality signal.

**Gmail / email client note**: When sending the follow-up (Step 3), reply to your own sent email rather than composing a new message. This keeps the original email content visible and reminds the recipient of what you sent — they do not need to search their inbox to remember what this is about.

---

*Companion documents: `phase-1-outreach-email-templates.md` (complete email templates), `phase-1-contact-list-structure.md` (institution database and batch assignments), `phase-1-substack-setup-guide.md` (Substack setup and post scheduling), `measurement-and-iteration-framework.md` (30-day post-distribution measurement).*
