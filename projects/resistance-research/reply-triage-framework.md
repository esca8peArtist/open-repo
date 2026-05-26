---
title: "Reply Triage Framework — Phase 1 Wave 1"
created: 2026-05-26
version: 1.0
status: production-ready
scope: >
  5-category triage system for classifying Phase 1 email replies. Maps reply type
  to Engagement Score (1–5), escalation pathway, and Phase 2 signal strength.
  Used during weekly synthesis (Step 1) to score incoming replies in real time.
word_count: ~1800
companion_files:
  - PHASE_1_WAVE_1_MONITORING_DASHBOARD.md
  - PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md
---

# Reply Triage Framework — Phase 1 Wave 1

**Version 1.0 — May 26, 2026**

## Overview

Every email reply to Phase 1 outreach must be classified into one of five categories. Each category maps to:
- An **Engagement Score** (1–5) for the Contacts sheet
- A **Tier 2 signal strength** (YES/MAYBE/NO)
- An **action** (immediate escalation, response email, FAQ entry, or removal)
- An **escalation threshold** (when to notify user of urgent developments)

This framework is applied during the **weekly synthesis** (Monday Step 1) when you review new replies. It takes 2–3 minutes per reply.

---

## The Five Categories

### Category 1: Implementation Signal

**Definition**: The recipient's organization is actively building on Phase 1 frameworks. They are integrating the material into operational practice: curriculum, litigation toolkit, policy brief, training program, governance document, or similar.

**Evidence phrases**:
- "We are incorporating this into our [curriculum / clinic / training / advisory]"
- "We will be citing this in our [brief / policy paper / statement]"
- "Our [students / staff / members] are now using [this framework]"
- "We've already started integrating [specific domain] into..."
- "We're using this as the basis for our [litigation / policy / training] work"
- Published document already incorporating framework language (detected via web search)

**Engagement Score**: 5 (highest)

**Tier 2 Signal**: YES — immediate escalation

**What to do**:
1. Record in **Contacts sheet**:
   - Column N: Engagement_Score = 5
   - Column L: Reply_Date = (date reply received)
   - Column O: Tier2_Candidate = YES
   - Column S: Notes = "Implementation signal: [specific practice they're adopting]"
2. Within 24 hours: Add entry to **Adoptions sheet** with:
   - Organization name, constituency, signal type, domains referenced, verification status "Confirmed"
   - Description: Brief quote or description of what they're adopting
3. **Escalate to user**: Send email within 24 hours saying "Score 5 detected from [Organization]" with 2–3 sentence summary
4. Do NOT wait for Day 30 checkpoint. Score 5 events trigger **immediate Phase 2 pre-activation planning**

**Follow-up action**: Send response email within 48 hours. Offer to:
- Provide a shareable/adaptable version if they want to customize for their audience
- Discuss how their implementation aligns with Phase 2 research agenda
- Include them in Tier 2 pre-briefing before broader Phase 2 launch

**Frequency in Phase 1**: Expected 1–3 Score 5 events across all Tier 1 contacts by Day 30. If you get 0 by Day 30, this is a signal to apply failure recovery modifications.

---

### Category 2: Critique / Feedback / Request for Elaboration

**Definition**: The recipient engages substantively with the framework but offers critique, feedback, or asks for clarification / additional detail. They are not adopting yet, but their engagement is deep enough to shape Phase 2 or generate FAQ content.

**Evidence phrases**:
- "I have a question about [specific domain/claim in framework]"
- "I see a gap in your analysis regarding [topic]"
- "Have you considered [alternative approach / additional evidence]?"
- "This is good, but [minor critique or suggestion]"
- "Can you explain more about [specific section]?"
- "I'd like to better understand the [claim or methodology]"
- "Could you elaborate on how this applies to [specific scenario]?"

**Engagement Score**: 3 (substantive engagement)

**Tier 2 Signal**: MAYBE — potential growth opportunity

**What to do**:
1. Record in **Contacts sheet**:
   - Column N: Engagement_Score = 3
   - Column L: Reply_Date = (date reply received)
   - Column S: Notes = "Critique: [topic of question/feedback]"
2. **Create FAQ entry**: Extract the question/feedback and add to a growing FAQ document (internal tracking only, not sent to contact yet). Example:
   - "Q: How does Domain X address [specific concern]? A: [2–3 sentence answer from the framework + reference to specific section]"
3. **Send response email within 48 hours**:
   - Thank them for the substantive feedback
   - Address their specific question or critique with 2–3 sentence answer
   - Offer brief follow-up conversation if they want to discuss further
   - If their question reveals a genuine gap in the framework, note this for Phase 2 refinement
4. Log the FAQ entry for post-Phase-1 synthesis (helpful for Phase 2 messaging to similar audiences)

**Escalation**: Not urgent. Include in weekly synthesis notes but do not escalate to user unless the critique reveals a fundamental framework weakness.

**Follow-up signal**: If this contact replies again to your response and their tone shifts toward adoption interest (moving toward Score 4 or 5), escalate immediately.

**Frequency in Phase 1**: Expected 5–12 Score 3 events across Tier 1 by Day 30. This is normal and healthy engagement.

---

### Category 3: Partnership / Collaboration Request

**Definition**: The recipient explicitly offers to work with you on adjacent research, co-author something, or launch a joint initiative. This is not yet adoption of existing framework, but it's partnership interest that may lead to Phase 2 co-development.

**Evidence phrases**:
- "Would you be interested in collaborating on [project]?"
- "I'd like to discuss partnership opportunities around [topic]"
- "Could we co-author a [brief / working paper / white paper] on [topic]?"
- "I'd love to set up a call to discuss how we might work together"
- "Our org is interested in partnering on [specific research or initiative]"
- "Can we schedule time to talk about joint development of [something]?"

**Engagement Score**: 4 (collaboration signal)

**Tier 2 Signal**: YES — escalation required

**What to do**:
1. Record in **Contacts sheet**:
   - Column N: Engagement_Score = 4
   - Column L: Reply_Date = (date reply received)
   - Column O: Tier2_Candidate = YES
   - Column S: Notes = "Partnership request: [type of collaboration they proposed]"
2. Within 24 hours: Note in **Adoptions sheet** as "Collaboration Request" (not yet "Confirmed" adoption, but strong Phase 2 signal)
3. **Escalate to user**: Send email within 24 hours with:
   - Subject: "Collaboration Request from [Organization]"
   - Brief summary of what they're proposing
   - Recommendation: user decision on whether to pursue partnership or focus on Phase 1 impact measurement
4. **Send response to contact**: Within 48 hours, express interest and suggest scheduling a call. Keep it brief: "Thank you — this is exciting. [User name] would like to discuss this further. I'll have them reach out within 3 business days."

**Follow-up action**: User decides:
- YES to partnership: Coordinate Phase 2 co-development timing; this contact becomes a core Tier 2 ambassador
- NO: Politely decline and refocus on Phase 1 framework adoption (likely Score 3 or 5 will still be achievable)

**Frequency in Phase 1**: Expected 1–2 Score 4 events by Day 30. Two or more Score 4 events within the first 14 days is a pre-Day-30 "STRONG" signal (triggers early Phase 2 pre-activation).

---

### Category 4: General Question / Clarification Request / Permission Request

**Definition**: The recipient asks a specific question about how to adapt the framework, seeks permission to use it in a specific way, or requests additional resources. This is engaged-but-not-yet-adopting, similar to Category 2, but the tone is more practical ("How do I use this?") than analytical ("What does this mean?").

**Evidence phrases**:
- "Can I use this in my [specific context]?"
- "How would I adapt this for [scenario]?"
- "Do you have a version that's simpler for [audience]?"
- "Can we share this with [specific group]?"
- "Is there a [specific format] version available?"
- "Do you have materials for [specific constituency / sector]?"
- "How would a [specific role / organization] use this?"

**Engagement Score**: 3 (substantive engagement, but more transactional than transformational)

**Tier 2 Signal**: MAYBE — indicates receptivity and potential future adoption

**What to do**:
1. Record in **Contacts sheet**:
   - Column N: Engagement_Score = 3
   - Column L: Reply_Date = (date reply received)
   - Column S: Notes = "Question: [what they're asking about]"
2. **Create FAQ entry**: Same as Category 2. Extract the question, draft a brief answer, file for future reference.
3. **Send response email within 24 hours**:
   - Answer their specific question directly (1–2 sentences max)
   - If they're asking for a simpler version or format, offer to create one and send within 3 days
   - If they're asking permission to share/adapt, give permission and offer to help customize
4. **If they ask for a custom version**: This is a "lead signal" for Phase 2 targeted materials. Note in **Notes column**: "Custom [format/simplification] requested — potential Tier 2 candidate for Phase 2 targeted outreach"

**Escalation**: Not urgent. Include in weekly synthesis but do not escalate to user unless the question volume (3+ similar questions) suggests a common need for a new format or explains a barrier to adoption.

**Frequency in Phase 1**: Expected 8–15 Score 3 events by Day 30. High score-3 volume is actually good — indicates people are engaged enough to ask for clarification.

---

### Category 5: Opt-Out / Unsubscribe / Not Interested

**Definition**: The recipient explicitly asks to be removed from future outreach, says they are not interested, or indicates the framework is not relevant to their work.

**Evidence phrases**:
- "Please remove me from your mailing list"
- "Not interested"
- "Please stop sending me [these materials]"
- "This isn't relevant to our organization"
- "We don't have capacity to engage with this"
- "Unsubscribe"

**Engagement Score**: 0 (no engagement — removal status)

**Tier 2 Signal**: NO — do not include in Phase 2 outreach

**What to do**:
1. Record in **Contacts sheet**:
   - Column I: Delivery_Status = "Opted Out"
   - Column N: Engagement_Score = 0
   - Column S: Notes = "Opt-out request: [reason if provided]"
2. **Remove from Phase 2**: Do NOT include this contact in any future Phase 2 outreach
3. **No response email needed** (respect their preference)
4. Do NOT escalate to user — this is normal and expected

**Important note**: Opt-outs should be rare in Phase 1 (Tier 1 are pre-qualified, high-relevance targets). If you see 3+ opt-outs by Day 14, it may signal:
- Wrong audience (check if contact list was validated correctly)
- Wrong framing in email subject line or opening (check if they read past the first line)
- Genuine lack of relevance to some contacts

Document opt-outs and discuss with user if volume becomes unusual.

**Frequency in Phase 1**: Expected 0–1 opt-outs from 16 Tier 1 contacts. If you get 3+, this is a red flag.

---

## Escalation Thresholds (When to Notify User Immediately)

| Event | Notify When | How | Timing |
|-------|------------|-----|--------|
| Score 5 (Implementation Signal) | Any single Score 5 | Email: "Score 5 Detected" | Within 24 hours of reply |
| Score 4 (Partnership) | 1st Score 4 OR 2+ Score 4 within 14 days | Email: "Partnership Request from [Org]" | Within 24 hours of reply |
| Multiple Score 3+ in one week | 4+ Score 3+ replies in a single week | Weekly synthesis summary | Every Monday |
| Opt-out cluster | 2+ opt-outs within 7 days | Email: "Opt-out pattern detected" | Within 24 hours of 2nd opt-out |
| Criticism revealing gap | Critique that repeats from 2+ contacts | Email: "Framework gap identified" | When pattern detected |

---

## Scoring Decision Tree (Quick Reference)

Use this flowchart when you open a new reply:

```
Read the reply
    │
    ├─ "We are now using this for [operational practice]" OR
    │  "We've adopted this into [curriculum/toolkit/training]" OR
    │  Published document cites the framework
    │  → SCORE 5 (Implementation Signal)
    │     Escalate within 24h
    │
    ├─ "Would you collaborate on [research/project]?" OR
    │  "Can we partner on [initiative]?"
    │  → SCORE 4 (Partnership)
    │     Escalate within 24h if 1st or 2nd occurrence
    │
    ├─ "I have a question about..." OR
    │  "I see a gap where..." OR
    │  "Can you elaborate on..." OR
    │  "How do I adapt this for..." OR
    │  "Can I use this in [context]?"
    │  → SCORE 3 (Substantive/Question)
    │     Create FAQ entry, respond within 48h
    │
    ├─ "Thanks for this, interesting work" OR
    │  "Good stuff" OR
    │  "Thanks for thinking about this"
    │  (No specific engagement, no follow-up questions)
    │  → SCORE 2 (Polite Acknowledgment)
    │     Log but do not respond unless warranted
    │
    ├─ Out-of-office auto-reply OR
    │  Form confirmation only
    │  → SCORE 1 (OOO/Form Only)
    │     Do not count toward reply rate
    │
    └─ "Please remove me" OR
       "Not interested" OR
       "Unsubscribe"
       → SCORE 0 (Opt-Out)
          Remove from Contacts sheet; do not include in Phase 2
```

---

## How Scores Feed into Checkpoint Decisions

**Day 7 Checkpoint**:
- Minimum: At least 2 Score 3+ replies by Day 7 across all constituencies

**Day 30 Checkpoint**:
- Overall Score 3+ reply rate ≥50% for STRONG determination
- Each constituency: 3+ Score 3+ replies for "strong threshold met"
- Any single Score 5 reply counts as "strong threshold met" for that constituency immediately

**Day 60 Checkpoint**:
- Score 5 replies = confirmed adoption events (count toward the 15 adoption target)
- Score 4 replies = partnership signals, documented separately, may lead to co-development arrangements

---

## Common Scoring Ambiguities

| Situation | How to Score | Reasoning |
|-----------|-------------|-----------|
| Reply says "This is great, but have you thought about X?" | Score 3 (Critique/Feedback) | Substantive engagement + suggestion |
| Reply asks "Can you send me a simpler version?" | Score 3 (Question) | Indicates receptivity, practical barrier |
| Reply says "We're passing this to [colleague]" but no adoption claim | Score 2–3 (depends on tone) | If forward is casual = 2; if forward is "they specifically asked for this" = 3 |
| Reply from someone not on original contact list, citing Tier 1 contact | Not directly scored; log in **Adoptions** as "Referral" | This is network multiplier evidence, separate from scoring |
| "I'll review this and send feedback" | Score 2 (Acknowledgment) | Intent to engage later ≠ current substantive engagement |
| Detailed critique with multiple specific suggestions | Score 3 (Critique) | High substantive engagement |
| "Our student clinic is using this in a case" | Score 5 (Implementation) | Operational adoption confirmed |
| "We'd like to use this in our training. Can we discuss options?" | Score 4 (Partnership + Permission) | Adoption interest + collaboration interest |

---

## Weekly Synthesis: Scoring Summary

Every Monday, your weekly synthesis should include a section like this:

```
## Reply Scoring Summary (Week of [Date])

New replies this week: [count]

Score 5 (Implementation Signal): [count] — [names/orgs]
Score 4 (Partnership Request): [count] — [names/orgs]
Score 3 (Substantive/Question): [count] — [list topics of questions]
Score 2 (Acknowledgment): [count]
Score 1 (OOO only): [count]
Score 0 (Opt-out): [count]

Escalations this week: [YES/NO — list any Score 4–5 escalations]

New FAQ entries: [count] — [brief topic list]

Tier 2 candidates flagged this week: [count] — [list orgs flagged as "YES" in Column O]
```

This summary goes in your `weekly-synthesis-template.md` for the week.

---

**Status**: Production-ready. Use this framework starting week 1 of Phase 1 (Week of June 3, 2026).

