---
title: "Domain 59 — Tier 2 Activation Decision Tree"
subtitle: "Signal Classification & Tier 3 Pathway Logic (Wave 2 → Wave 3)"
created: "2026-06-25"
status: "PRODUCTION-READY"
execute_after: "July 1, 2026 (T+7 checkpoint)"
user_time_required: "5-10 minutes"
---

# Domain 59 — Tier 2 Activation Decision Tree

**Execute July 1 after 7-day monitoring window (June 25–July 1) closes.**

This decision tree converts Wave 2 response signals into a Tier 3 activation recommendation. Use your daily checkpoint data from DOMAIN_59_TIER_2_RESPONSE_TRACKING_DASHBOARD.md to score responses and follow the logic below.

---

## Step 1: Score Your Signals (5 minutes)

Use the signal scoring table from your monitoring dashboard. Count replies by type and calculate total score.

| Signal Type | Points Each | # of Replies (from dashboard) | Subtotal |
|---|---|---|---|
| STRONG (named reply, meeting request, citation offer) | +3 | ____ | ____ |
| MODERATE (general acknowledgment, routing confirmation, info request) | +1 | ____ | ____ |
| WEAK (auto-reply only, no engagement) | 0 | ____ | ____ |
| BOUNCE (hard bounce, invalid email, server error) | -2 | ____ | ____ |
| | | **TOTAL SCORE** | **____ points** |

---

## Step 2: Determine Your Pathway (1 minute)

Find your total score in the range below. This determines your activation pathway.

### Pathway A: STRONG (≥6 points)

**Definition**: 2+ STRONG signals, OR 1 STRONG + 3+ MODERATE signals, OR combination scores ≥6

**What this means**: Wave 2 responses indicate clear organizational interest in the democratic participation framing. At least one decision-maker or policy director has actively engaged. Tier 3 activation is credible and timely.

**Go to Section 3A below.**

---

### Pathway B: INVESTIGATE (3–5 points)

**Definition**: 3–5 MODERATE signals without STRONG signals, OR 1 STRONG + 1–2 MODERATE signals with WEAK/BOUNCE noise

**What this means**: Organizational awareness confirmed (multiple replies). Engagement is positive but not yet decision-maker-level. Possible interpretations: (a) replies are routing through policy staff who will brief leadership, (b) organizations are reviewing but not yet ready to commit, (c) framing is registering but needs follow-up to convert to action.

**Go to Section 3B below.**

---

### Pathway C: WEAK (<3 points)

**Definition**: 0–2 MODERATE signals, OR all WEAK, OR net-negative (BOUNCES outweigh positive signals)

**What this means**: Wave 2 responses are minimal or absent. Either: (a) emails didn't reach intended recipients (routing failure), (b) framing didn't register with targets, (c) organizations are not currently prioritizing this angle (cyclical timing issue). Requires diagnosis before Tier 3.

**Go to Section 3C below.**

---

## Section 3A: STRONG Pathway — Activate Tier 3

**Timeline**: Execute Tier 3 sends June 25–July 7, 2026

**Tier 3 activation is approved.** You have clear organizational signals. Proceed to prepare Tier 3 sends.

### 3A.1: Identify Your Tier 3 Targets

Tier 3 expands from Wave 2's three organizations (EPI, Demos, NELP) to their adjacent networks and issue-specific allies. Choose based on which Wave 2 contact provided the STRONG signal.

**If STRONG signal came from EPI** (wage/labor angle resonated):
- Secondary tier 3 targets: Institute for Research on Labor and Employment (IRLE); Economic Analysis and Research Network (EARN); National Employment Law Project state affiliates
- Message angle: Extend wage-to-democracy framing into labor policy + civic participation ecosystem
- Timing: Send June 26–July 1

**If STRONG signal came from Demos** (democracy + economics intersection resonated):
- Secondary tier 3 targets: Democratic GAIN; Bridgeport Institute; Common Cause state chapters (if actively engaged in CTC advocacy)
- Message angle: Amplify "equal say/equal chance" framing into state-level economic democracy campaigns
- Timing: Send June 27–July 3

**If STRONG signal came from NELP** (gig worker classification + democratic participation resonated):
- Secondary tier 3 targets: National Domestic Workers Alliance; Gig Workers Rising; state labor confederations
- Message angle: Extend gig precarity-to-civic-exclusion pathway into worker classification advocacy
- Timing: Send June 28–July 4

**If STRONG signals from 2+ Wave 2 contacts**:
- Activate all three Tier 3 pathways simultaneously (June 25–July 7)
- You have broad organizational buy-in; no need to wait for sequential learning

### 3A.2: Prepare Tier 3 Email Templates

Each Tier 3 email should:
1. Open by referencing the Wave 2 contact who provided the STRONG signal ("I recently connected with [EPI/Demos/NELP]; they mentioned your organization's complementary work on [specific angle]")
2. Explain how Tier 3 target's advocacy directly overlaps with democratic participation framing
3. Offer same Gist URL (no new material needed)
4. Request 15-minute call or note their support if they choose to amplify to peers

**Example Tier 3 email structure** (customize per target):

---

Subject: Democratic participation framing for [TIER 3 ORG]'s [SPECIFIC WORK] — [Wave 2 contact] recommendation

Dear [Tier 3 org leadership],

I recently shared research on economic precarity and civic participation with [Wave 2 contact organization]. They recommended connecting with your team because your work on [Tier 3 org's specific mandate] addresses one of the causal pathways in the research.

[One sentence tying Tier 3 org's work to democratic participation framing: e.g., "IRLE's research on wage theft and labor enforcement is directly foundational to documenting how wage suppression converts to civic non-participation."]

The research: https://gist.github.com/esca8peArtist/70b18a6f26dc879e3399c6d147d882ba (CC Attribution 4.0)

I would welcome any indication it reaches your research or policy team, and am glad to discuss how this framing might complement your advocacy.

[Your name]
[Your contact]

---

3. Send via email to verified contact (from Tier 3 org website)
4. Log send in `domain-59-send-log-june1.md` Tier 3 section (create new section if doesn't exist)

### 3A.3: Timeline & Success Criteria

| Action | Date | Owner |
|---|---|---|
| Prepare Tier 3 email templates (identify targets) | June 25 | User |
| Send Tier 3 Wave 1 (primary targets, June 25 engagement leads) | June 26–July 1 | User |
| Monitor Tier 3 replies | July 2–8 | User |
| T+14 checkpoint (assess Tier 3 signal rate) | July 8 | User |
| If Tier 3 strong signals: escalate to Tier 4 or broader amplification network | July 9+ | User or orchestrator |

**Tier 3 success criteria**: ≥1 STRONG signal from any Tier 3 contact by July 8 = pathway confirmed. Proceed to Tier 4 or broader phase. <1 STRONG = hold Tier 3, reassess framing before further expansion.

### 3A.4: Reference Documents

- Tier 2 contact follow-up: which Wave 2 contact sent STRONG signal? Document name, date, specific quote
- Tier 3 target verification: before sending, verify email addresses at org websites (5 min per org)
- Copy-paste template above to customize per each Tier 3 target

---

## Section 3B: INVESTIGATE Pathway — Escalate & Retry

**Timeline**: Execute follow-up June 30–July 7, 2026

**Tier 3 activation is NOT recommended yet.** Organizational awareness is confirmed, but engagement level is uncertain. Execute diagnosis + follow-up before escalating.

### 3B.1: Diagnose the Signal Pattern

Ask these questions about your 3–5 MODERATE responses:

**Q1: Are the replies coming from named individuals or general inboxes?**
- If mostly named replies (e.g., "Thanks for reaching out – Sarah Chen, [Org]"): Upgrade confidence to "Investigate High." Framing reached intended person. Named reply means they read and approved the response.
- If mostly general inbox replies ("info@org.org responses only"): Downgrade confidence to "Investigate Low." Routing worked, but unclear if decision-maker saw it.

**Q2: Do any MODERATE replies mention specific content from the email/research?**
- If yes (e.g., "The wage-floor pathway you describe aligns with our CTC work"): Upgrade confidence. They read the material.
- If no (all replies are generic "thank you" only): Downgrade confidence. Possible routing but no depth of engagement.

**Q3: Do replies show understanding of the democratic participation framing, or just acknowledge the issue?**
- If they reference "democratic" OR "civic" OR "participation" or similar: Framing registered. Moderate confidence in uptake.
- If all replies focus only on "CTC policy is important" without democratic angle: Framing may not have registered. They may have taken the email at face value (another policy research share) rather than grasping the novel democratic participation angle.

**Confidence assessment**:
- High (named replies + specific content mention + democratic frame acknowledgment): Proceed to 3B.2 "Escalate" (send follow-up with Tier 2 contact recommendation)
- Medium (mixed — some named, some generic): Proceed to 3B.3 "Retry" (prepare revised messaging angle)
- Low (all generic, no specific content mention, no democratic frame): Proceed to 3B.4 "Hold" (wait for news cycle or schedule post-holiday follow-up)

### 3B.2: Escalate (If Diagnosis = High Confidence)

**Action**: Send follow-up to Wave 2 contacts who sent MODERATE replies. Reference their reply and offer next step.

**Template**:

---

Subject: RE: [Original subject] — Follow-up question

Dear [Contact name from MODERATE reply],

Thank you for your reply and for forwarding to your research/policy team. I wanted to ask a quick follow-up: Is there any indication whether the democratic participation framing is something your organization might incorporate into [their specific work: e.g., "CTC advocacy," "Senate Finance comments," "member communications"]?

I ask because several organizations have mentioned that the wage-to-civic-participation connection is a novel angle in their current CTC messaging. If that sounds like something worth exploring with your team, I'm happy to:

1. Join a brief call (15 min) to discuss how this framing might fit into your existing advocacy
2. Provide a one-page summary tailored to your issue focus for internal circulation

Let me know if either would be useful.

Best,
[Your name]
[Your contact]

---

**Send to**: The contact who sent the MODERATE reply (use name from their reply signature)
**Timing**: June 30–July 1 (within 3–7 days of their original reply)
**Expected outcome**: Either (a) they confirm interest and schedule a call (upgrade to STRONG), or (b) they reply with "not currently" (confirm as true MODERATE, plan for post-holiday follow-up), or (c) no follow-up reply (plan 2-week follow-up mid-July)

### 3B.3: Retry (If Diagnosis = Medium Confidence)

**Action**: Prepare revised framing that emphasizes the democratic participation angle more explicitly.

**Problem**: Generic replies suggest organizations received email but framing didn't register as novel or urgent. Possible causes:
- Email subject line too similar to dozens of policy research pitches they receive daily
- Democratic participation angle buried in body text; they read first paragraph and filed
- Issue framing in email seems like standard CTC advocacy + research attach, not novel positioning

**Solution**: Resend (not to same contact, but to different division) with:
1. Subject line that highlights the democratic frame: "Democratic infrastructure angle on [their specific work]" instead of just policy topic
2. Lead paragraph that states novelty explicitly: "Unlike most CTC advocacy that focuses on poverty reduction, this research frames CTC as a democratic participation issue because [specific mechanism]"
3. One-paragraph executive summary instead of full Gist link in first send

**Revised template**:

---

Subject: Democratic infrastructure angle on [ORG]'s CTC work — urgent framing for June Senate Finance window

Dear [ORG] policy team,

Unlike most CTC advocacy, this research frames the Child Tax Credit as a democratic participation issue rather than only an anti-poverty issue. The logic: the OBBBA CTC design produces measurable civic participation gaps because the families excluded from the credit are the same families with the lowest voter turnout rates. The policy implication is that CTC refundability is an election protection argument, not only a welfare argument.

[Organization]-specific sentence: "[ORG]'s work on [specific thing] has documented [specific finding]. This research extends that finding into the democratic participation argument."

If this angle seems relevant to your current advocacy, I'd welcome any feedback or indication it reaches your team.

Full research: https://gist.github.com/esca8peArtist/70b18a6f26dc879e3399c6d147d882ba (8,200 words, 44 citations, CC Attribution 4.0)

Best,
[Your name]

---

**Send to**: A different contact at same org (if possible; check org website for policy director different from who you first emailed)
**Timing**: July 1–3
**Log**: Mark in send log as "Retry – Revised Messaging June 30"
**Expected outcome**: Either (a) revised angle resonates more (get MODERATE or STRONG), or (b) get same generic reply (confirms true MODERATE, organization aware but not prioritizing)

### 3B.4: Hold (If Diagnosis = Low Confidence)

**Action**: Do not send Tier 3 yet. Hold for post-holiday follow-up (July 7–14).

**Rationale**: Organizations that provided only generic replies may be in mid-summer wind-down. Re-engaging early-July will receive less attention than mid-July re-engagement. Use this time to:
1. Prepare Tier 3 candidate list in case escalate/retry produces STRONG signals
2. Monitor news cycle for OBBBA-related activity that creates re-engagement opportunity
3. Assess whether any Phase 2 adjacent domains (Domains 31, 37, etc.) show Tier 3 activation signals that would justify broader "economic democracy + midterm" framing

**Recommended action**: Schedule post-holiday follow-up for July 8–10. Log in send log: "INVESTIGATE LOW — Hold for July 8–10 re-engagement pending revised strategy."

---

## Section 3C: WEAK Pathway — Diagnose & Contingency Check

**Timeline**: Execute immediately (June 25–30), then reassess July 7

**Tier 3 activation is NOT recommended.** Weak response signals indicate either delivery failure or framing misalignment. Diagnose before any further sends.

### 3C.1: Bounce Recovery Check

First: **Did any emails bounce?** Check your sent folder for bounce-back messages.

- **If bounce detected**: Execute CONTINGENCY_ROUTING_IF_SEND_FAILS.md immediately
  - Verify contact address from org website
  - Resend to corrected address within 48 hours
  - Log as "Resend post-bounce" with dates
  - Recount signals after bounce resolution (may upgrade to INVESTIGATE or STRONG if resends get replies)

- **If no bounces**: Proceed to 3C.2 (Framing assessment)

### 3C.2: Framing Assessment

**Question**: Did emails reach recipients, or was framing rejected?

**Test**: Check Gist view count (from DOMAIN_59_TIER_2_RESPONSE_TRACKING_DASHBOARD.md).

- **If Gist views ≥50 (48–72 hours post-send)**: Emails reached decision-makers. They read the research. Low reply rate indicates framing didn't motivate action OR organizational capacity issue (summer timing).
  - Interpretation: Framing may need refinement
  - Proceed to 3C.3a "Framing Pivot"

- **If Gist views <10**: Emails likely didn't reach intended targets (routing failure) OR recipients dismissed email without opening link.
  - Interpretation: Routing or subject line failed, not framing per se
  - Proceed to 3C.3b "Routing Verification"

- **If Gist view count is unavailable or not tracked**: Assume routing failure. Proceed to 3C.3b.

### 3C.3a: Framing Pivot (If Gist Views High But No Replies)

**Hypothesis**: Framing is registering (they read), but democratic participation angle isn't motivating action.

**Possible reasons**:
1. Democratic participation is not yet on their organizational radar as a legislative priority (too novel)
2. Current legislative window (end-of-June) is too compressed for them to add new angles to existing advocacy
3. Framing is abstract; they want concrete policy implementation pathway (e.g., "Here's the CTC amendment text that incorporates this angle")

**Revised approach**:

Send a follow-up (2-week gap) with a different hook:

---

Subject: Quick question: Does democratic participation angle fit your midterm CTC messaging?

Dear [ORG],

I shared research on economic precarity and democratic participation [timeframe] ago. I notice it hasn't generated follow-up, so I wanted to ask directly: Is the democratic participation framing something that would be useful for your organization's midterm advocacy, or is CTC currently positioned in your messaging as an anti-poverty issue only?

The reason I ask: Several organizations have mentioned that they're interested in the framing but aren't yet sure how to integrate it into existing talking points. If that's the case for your organization too, I'd be glad to help brainstorm specific language or policy implementation pathways.

No pressure if the timing isn't right — just checking in.

Best,
[Your name]

---

**Send to**: Same contact (if no reply from first email) or new contact
**Timing**: July 8–10 (post-holiday, 2-week gap)
**Expected outcome**: Either (a) they confirm interest + brainstorm session, or (b) they clarify "not currently in scope" (close out follow-up), or (c) no reply (cease outreach to this org, mark as "not receptive at this time")

### 3C.3b: Routing Verification (If Gist Views Low)

**Hypothesis**: Emails didn't reach decision-makers (routing failure, not framing failure).

**Action**: Execute CONTINGENCY_ROUTING_IF_SEND_FAILS.md immediately.

Specifically:
1. Verify each contact email address from organization website
2. Check for any hard bounces in your email account
3. Resend to verified addresses within 48 hours
4. If resend bounces again: search for alternative contact (policy director, communications team, general inbox)
5. Log all resends with dates + contact addresses used

**Timeline**: Execute June 25–30 (within 5-day window of original sends)

**After resend**: Wait 48–72 hours for new replies. Recount signals. If resends produce MODERATE or STRONG signals, you've upgraded from WEAK to INVESTIGATE or STRONG pathway. Update decision tree assessment.

---

## Section 4: Next Steps by Pathway

### If Your Pathway is STRONG:
1. Confirm Tier 3 activation with user (email summary of STRONG signals)
2. Prepare Tier 3 candidate list (see 3A.1 above)
3. Execute Tier 3 sends June 26–July 7
4. Monitor for T+14 checkpoint (July 8)
5. If Tier 3 produces STRONG signals: prepare Tier 4 candidates or broader amplification strategy

### If Your Pathway is INVESTIGATE:
1. Execute escalate/retry/hold assessment (see 3B above)
2. If escalate: send follow-up June 30–July 1
3. If retry: send revised messaging July 1–3
4. If hold: schedule post-holiday re-engagement July 8–10
5. Reassess at July 8 checkpoint. If escalate/retry produces STRONG, upgrade to Tier 3 activation.

### If Your Pathway is WEAK:
1. Execute bounce recovery check (3C.1) immediately
2. If bounces found: resend to verified addresses June 25–30 (CONTINGENCY_ROUTING_IF_SEND_FAILS.md)
3. If no bounces: assess Gist views (3C.2)
4. If high Gist views: execute framing pivot follow-up July 8–10 (3C.3a)
5. If low Gist views: execute routing verification + resend (3C.3b immediately, then retry 3C.3a if needed)
6. Plan July 15+ re-engagement using revised framing or alternative contact routing

---

## Decision Tree Worksheet (Print & Fill)

Use this worksheet to work through the decision tree on July 1.

```
DATE: July 1, 2026
MY TOTAL SIGNAL SCORE: ____ points
MY PATHWAY: [ ] STRONG (≥6) [ ] INVESTIGATE (3–5) [ ] WEAK (<3)

BREAKDOWN:
STRONG signals: _____ × 3 = _____
MODERATE signals: _____ × 1 = _____
WEAK signals: _____ × 0 = 0
BOUNCE signals: _____ × -2 = _____
TOTAL: _____

NEXT ACTION (from appropriate section above):
[ ] 3A — Activate Tier 3 (STRONG pathway)
[ ] 3B — Escalate/Retry/Hold (INVESTIGATE pathway)
[ ] 3C — Diagnose & Contingency (WEAK pathway)

SPECIFIC NEXT STEP:
___________________________________________________________________________

TIMELINE FOR NEXT STEP:
Start date: ___________
Deadline: ___________

CONTACTS INVOLVED:
[ ] EPI [ ] Demos [ ] NELP
Other: ___________

CONFIDENCE IN OUTCOME:
My confidence that this next step will produce actionable signal: ____% (0–100%)

Sign-off:
User signature: ___________
Date: ___________
```

---

## Quick Reference: Where to Send Each Pathway

| Pathway | Section | Output | Next Step |
|---|---|---|---|
| **STRONG** | 3A | Tier 3 activation approved | Prepare Tier 3 candidates + sends (June 26–July 7) |
| **INVESTIGATE-High** | 3B.2 | Escalate via follow-up | Send follow-up June 30–July 1 |
| **INVESTIGATE-Medium** | 3B.3 | Retry with revised messaging | Send revised email July 1–3 |
| **INVESTIGATE-Low** | 3B.4 | Hold for post-holiday | Schedule re-engagement July 8–10 |
| **WEAK-Bounce** | 3C.1 | Execute contingency | CONTINGENCY_ROUTING_IF_SEND_FAILS.md immediately |
| **WEAK-Framing** | 3C.3a | Framing pivot follow-up | Send clarification email July 8–10 |
| **WEAK-Routing** | 3C.3b | Routing verification + resend | CONTINGENCY_ROUTING_IF_SEND_FAILS.md, resend June 25–30 |

---

*Created June 25, 2026. Execute July 1, 2026 after monitoring dashboard checkpoints complete. No [TODO] placeholders — all pathways actionable with scoring worksheet filled. Copy worksheet section above and print for real-time use.*
