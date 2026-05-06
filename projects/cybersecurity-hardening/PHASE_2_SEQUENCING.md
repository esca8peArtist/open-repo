---
title: "Phase 2 Distribution Sequencing: Tier Execution Timeline, Metrics, and Launch Checklist"
project: cybersecurity-hardening
created: 2026-05-06
status: production-ready
executor: Anya
gist-url: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108
depends-on:
  - TIER1_DISTRIBUTION_PREP.md
  - TIER1_OUTREACH_EXECUTION_PLAN.md
  - TIER2_DISTRIBUTION_PREP.md
  - TIER2_MESSAGING_TEMPLATES.md
  - TIER3_DISTRIBUTION_PREP.md
  - tier-1-success-metrics.md
---

# Phase 2 Distribution Sequencing

## What This Document Is For

This document answers three questions you need answered before sending a single email:

1. **When** should each tier launch relative to the others?
2. **How** do you know when you are actually ready to move to the next tier?
3. **What** do you do when something goes wrong?

Read this document through before starting Tier 1 outreach. Then return to it at the end of each tier week to confirm you are on track or need to adjust.

The companion file `DISTRIBUTION_TIMELINE.csv` gives you the machine-readable schedule. This document gives you the reasoning behind every date and the judgment calls you will need to make.

---

## Section 1: Tier Execution Timeline

### The Fundamental Principle

Each tier does a different job. Tier 1 gets the corpus to the people who need it most, immediately, through organizations that already have their trust. Tier 2 amplifies it to networks that can validate and spread it to technically literate audiences. Tier 3 embeds it in institutions that shape long-term policy and legal norms. These are not parallel jobs — they are sequential, and the success of each tier creates the conditions for the next.

The timeline below is relative to Tier 1 Day 1, which you choose. Once you set Day 1, the rest follows.

---

### Phase 0: Pre-Launch (Before Tier 1 Day 1)

**Duration**: 1 week  
**Who**: Anya alone  
**Time commitment**: 4–5 hours total

This phase is non-negotiable. Do not skip any step. Sending emails before this is done is how campaigns fail technically before they can fail strategically.

| Task | Time | Why It Cannot Be Skipped |
|------|------|--------------------------|
| Gist accessibility verification (incognito, not logged in) | 15 min | A locked Gist sends 50 people to a dead link |
| Bitly short link setup and redirect confirmation | 30 min | You cannot measure click-through without this |
| Gmail label structure creation (7 labels) | 20 min | Without labels, response data mixes with inbox noise |
| Response template library saved (R1–R5) | 30 min | Slow replies to engagement lose the momentum window |
| Tracking spreadsheet created and pre-populated | 60 min | Source of truth; do not trust memory for 50+ contacts |
| Contact list built: Weeks 1–2 (50 organizations) | 90 min | Research in advance, not morning-of |
| Email deliverability test at mail-tester.com | 15 min | Failing this means your emails land in spam |
| Confirm your send-from address is final | 5 min | You cannot change this mid-campaign without confusing recipients |

**Gate**: Do not begin Tier 1 outreach until all eight tasks above are checked. This is a hard gate, not a soft recommendation.

---

### Tier 1: Weeks 1–3 (Active Outreach) + Weeks 4–7 (Follow-Up)

**Total duration**: 7 weeks from Day 1  
**Contact volume**: 50–60 organizations across 1A (legal aid), 1B (community orgs), 1C (mutual aid networks)  
**Anya time**: 4 hours/week active (Weeks 1–3), then 2–3 hours/week follow-up (Weeks 4–7)

**Send cadence**:
- 5 contacts per morning, 7:00–9:00 AM, with 3–5 minute gaps between sends
- Sends before 9 AM land in inboxes before daily inbox management; sends after noon face much higher competition
- Do not compress: sending 25 in a day triggers Gmail rate limits and looks like spam to recipient mail servers

**Internal tier sequence** (order matters):

| Week | Contacts | Category | Why This Order |
|------|----------|----------|----------------|
| Week 1, Days 1–5 | 25 contacts | 1A: immigration legal aid | Fastest path to at-risk population; best contact info; highest mission alignment |
| Week 2, Days 8–12 | 25 contacts | 1B: community orgs + second 1A wave | Community orgs distribute internally; second 1A wave catches regional orgs |
| Week 3, Days 15–19 | 10–15 contacts | 1C: mutual aid + catch-up | Lower barrier, faster share velocity; 1C does not need 1A's relationship warmth |
| Weeks 4–7 | Follow-up loop only | No new outreach | Two contacts max per organization: one initial email, one follow-up |

**The response window that matters**: Day 7 for each week's sends is the mid-course correction moment. Review the engagement scores (from tier-1-success-metrics.md) at Day 7. Score 1 contacts (sent, no signal) may need a subject-line variant. Score 2 contacts (opened, no click) may need a follow-up with the Bitly link re-embedded. This is not optional housekeeping — it is how you recover 10–15% of otherwise-lost contacts.

---

### Transition Window: End of Week 3 → Beginning of Week 5

**Duration**: 2 weeks of parallel activity  
**What happens**: Tier 1 active outreach is complete; follow-up loop is running; Tier 2 preparation begins  
**Anya time**: 2–3 hours/week Tier 1 follow-up + 2 hours Tier 2 prep

Use this window to:
1. Review Week 1 and Week 2 engagement scores and classify all 50 contacts by type
2. Identify the 3–5 Tier 1 organizations with Score 4–5 (integration signals) — these become Tier 1 case study sources for Tier 2 emails
3. Research Tier 2 contacts (current staff, recent publications, relevant campaigns)
4. Draft the first 5 Tier 2 emails (2A digital rights organizations first)

Do not launch Tier 2 before the Tier 1 transition criteria below are met.

---

### Tier 2: Weeks 5–12

**Start condition**: See Section 2 (Success Metrics and Transition Criteria).  
**Do not start Tier 2 before Week 5** even if Tier 1 response is excellent. The 2-week gap lets response data accumulate, follow-ups complete, and Tier 2 prep finish properly.

**Contact volume**: 33 organizations across 2A (digital rights), 2B (academic), 2C (security researcher communities), 2D (journalist orgs)  
**Anya time**: 3–4 hours/week active (Weeks 5–8), then 2 hours/week follow-up (Weeks 9–12)

**Internal Tier 2 sequence**:

| Weeks | Contacts | Category | Rationale |
|-------|----------|----------|-----------|
| Weeks 5–6 | 2A digital rights (12 orgs) | 3–4 contacts/day | Fastest response cycles; EFF/CDT endorsement raises credibility for all subsequent Tier 2 outreach |
| Weeks 7–8 | 2D journalist orgs (7 orgs) | 3–4 contacts/day | News cycles move fast; send early to capture potential coverage windows |
| Weeks 9–11 | 2B academic programs (9 orgs) | 2–3 contacts/day | Semester-driven response cycles; slower but high-value if they integrate corpus into curriculum |
| Weeks 9–12 | 2C researcher communities (5 channels) | 1–2 contacts/week | Conference submissions and individual researcher contact; ongoing rather than batched |

**Key timing constraint for 2B academic contacts**: Do not send to academic programs during end-of-semester crunch (typically mid-April through end of May, and mid-November through December). The optimal academic windows are: September–October (fall start) and February–March (spring semester, pre-crunch). If your Tier 2 window lands in a bad academic timing period, delay 2B contacts by 4–6 weeks and run 2A and 2D first.

---

### Gap Window: End of Week 8 → Beginning of Week 11

**Duration**: 3 weeks  
**What happens**: Tier 2 active outreach complete; follow-up loop running; Tier 3 preparation begins  
**Anya time**: 2 hours/week Tier 2 follow-up + 2 hours Tier 3 prep per week

Use this window to:
1. Identify any Tier 2 acknowledgments or publications that can be referenced in Tier 3 outreach (the credibility compounding benefit)
2. Research Tier 3 contacts (much harder — see TIER3_DISTRIBUTION_PREP.md contact research methodology)
3. Verify semester timing for academic law and policy school contacts

---

### Tier 3: Weeks 11–20

**Start condition**: See Section 2 (Success Metrics and Transition Criteria).  
**Do not start Tier 3 before Week 11** regardless of Tier 2 performance.

**Contact volume**: ~30 organizations across 3A (policy/think tanks), 3B (labor), 3C (academic law/policy schools)  
**Anya time**: 2–3 hours/week active (Weeks 11–14), then 1–2 hours/week follow-up (Weeks 15–20)

**Internal Tier 3 sequence**:

| Weeks | Contacts | Category | Rationale |
|-------|----------|----------|-----------|
| Weeks 11–12 | 3A policy organizations (12 orgs) | 2–3 contacts/day | Georgetown CPT, ACLU SPT, Brennan Center — these reference any Tier 2 credibility signals already available |
| Weeks 13–14 | 3B labor organizations (8 orgs) | 2–3 contacts/day | AFL-CIO Tech Institute, UFW, NDWA — direct member protection angle requires less credibility runway than policy orgs |
| Weeks 14–18 | 3C academic law/policy schools (10 orgs) | 1–2 contacts/day | Semester-dependent; target September–October for fall start or February–March for spring |
| Months 4–6 | Second-round outreach | Any tier | Use any accumulated Tier 2 publications or Tier 3 acknowledgments as updated credibility signals |

**Tier 3 reality check**: Response timelines here are weeks to months, not days. A policy organization that engages may take 3–6 months to produce a brief. A law clinic may take a semester to take on a related project. Track these on a separate long-horizon tracking tab in your spreadsheet. Do not apply the same weekly follow-up cadence to Tier 3 contacts — use a monthly check-in pattern instead.

---

## Section 2: Success Metrics Per Tier and Transition Criteria

### What "Transition Readiness" Means

You are not waiting for perfection. You are waiting for enough signal to know the campaign is reaching real people who are doing something with the corpus. The thresholds below are calibrated to be achievable without being so low they let you move forward on empty data.

---

### Tier 1 → Tier 2 Transition Criteria

**Minimum criteria** (all three must be true before launching Tier 2):

1. **Volume**: At least 40 of the targeted 50–60 organizations have been contacted (Weeks 1–3 complete, at minimum 40 sends recorded)

2. **Response signal**: At least one of the following:
   - 10%+ response rate (5+ responses of any type from 50 sends) — confirms the email is reaching inboxes and the subject is compelling enough to reply
   - 3+ Score 3 contacts (confirmed clicks on the Bitly link) — confirms the corpus is being read, not just received
   - 1+ Score 4–5 contact (integration signal or active adoption) — the highest-confidence indicator that Tier 1 is working

3. **No critical failure**: The Gist URL is still publicly accessible; no email deliverability block has been issued by Gmail

**Strong transition signal** (these are positive but not required):

- Score 4–5 from a named national organization (NILC, CLINIC, RAICES, EFF — the first-order targets from TIER1_DISTRIBUTION_PREP.md) — these can be specifically referenced in Tier 2 outreach
- A Tier 1 organization has asked to adapt or translate Part 0 — this signals the content is practically useful, not just interesting
- Bitly shows click traffic from outside your known contact list — the corpus is being forwarded organically
- You have received a question about a specific threat scenario or tool (means people are reading past the cover email)
- The CA DROP platform path has been cited specifically by a California-based contact — highest-confidence signal that the corpus is reaching undocumented people

**Weak transition signal** (adjust Tier 2 framing if these are all you have):

- Only acknowledgment responses (Score 2–3 but no integration signals)
- Click traffic in Bitly but no replies
- Positive signal from only 1C mutual aid contacts (their engagement does not transfer as credibility signal to Tier 2 digital rights organizations)

---

### Tier 2 → Tier 3 Transition Criteria

**Minimum criteria** (all must be true):

1. **Volume**: At least 25 of 33 Tier 2 organizations contacted

2. **Institutional validation signal**: At least one of the following:
   - EFF, CDT, Access Now, or Privacy International has acknowledged the corpus (even a "received, will review" from one of these carries Tier 3 weight)
   - Freedom of the Press Foundation has expressed interest in training integration
   - An academic program has requested additional technical details or expressed interest in curriculum use
   - A security researcher has provided substantive technical feedback (validation or corrections) — both are useful

3. **6-week minimum gap from Tier 2 launch** — even if strong signals appear earlier. Tier 3 contacts will ask "who else has engaged with this?" — you need time to accumulate a real answer

**Strong transition signal**:

- A published acknowledgment from a Tier 2 organization (social media mention, newsletter citation, published resource listing) — these are directly quotable in Tier 3 emails
- Two or more Tier 2 organizations have responded with substantive engagement
- A Tier 2 journalist organization is covering the ELITE system as a story using the corpus as source material

**Weak transition signal** (do not treat as sufficient for Tier 3 launch alone):

- Only Tier 2C researcher community responses (conference community channels respond but rarely produce the institutional credibility Tier 3 expects)
- High Bitly click volume without any organizational reply

---

### Tier 3 Monitoring Metrics

Tier 3 has no downstream tier. Success here is measured over a 6–12 month horizon, not a 4-week response window. Track at monthly intervals on a separate sheet:

**Short-term (Month 1–3)**:
- Did any policy organization acknowledge and begin internal review?
- Did any law clinic director respond with interest in a specific legal question the corpus raises?
- Did any labor organization request an adapted version for member education?

**Medium-term (Month 3–6)**:
- Policy brief or white paper citing the corpus
- Law school clinic taking on a related case or research project
- Academic course integrating the threat model as a case study
- Labor organization distributing Part 0 to members via internal communications

**Long-term (Month 6–12)**:
- Legislative testimony or agency comment letters citing the corpus
- Academic paper citing the threat model
- Journalism school integrating source protection content into digital security curriculum
- Coalition of Tier 3 organizations producing joint policy advocacy based on corpus documentation

---

## Section 3: Contingency Sequencing

### Scenario A: Tier 1 Response Is Low (Below 5% Response Rate After Week 2)

**Definition**: Fewer than 3 responses of any type from 50 sends after 2 full weeks.

**Immediate diagnosis** (before changing anything):
1. Check Bitly — are people clicking but not responding? (Corpus is not compelling enough, or no clear action after reading.) Or are people not clicking at all? (Email not getting read, or subject line not compelling.)
2. Check response types — are you getting bounces? (Contact quality problem.) Declines? (Framing problem.) Silence? (Deliverability or contact quality problem.)
3. Review your subject line variants — did you actually test more than one?

**Adjustment options by diagnosis**:

| Diagnosis | Adjustment |
|-----------|------------|
| Many bounces (>15%) | Research alternate contacts before Week 3. Do not send more emails to bad addresses. |
| High opens, low clicks | Rewrite the call-to-action: make Part 0 the explicit CTA ("The most actionable thing: click through to Part 0 on the Gist"). |
| Low opens | Change subject line. Try: "Security resource for clients facing ICE targeting" instead of the current formulation. |
| Declines from 1A legal orgs | Check if framing sounds like you are selling consulting rather than sharing a resource. Remove any advisory-adjacent language. |
| Declines from 1B community orgs | Ensure you are reaching a program staff member, not a fundraising inbox. Re-research contacts. |

**Impact on Tier 2 timing**: If 5% response threshold is not met after Week 3, delay Tier 2 by 2 weeks and run an adjusted Week 3–4 with corrected subject lines and framing before transitioning. Do not launch Tier 2 into a framing that has already shown it does not work for Tier 1 audiences.

---

### Scenario B: Tier 1 Response Is Unexpectedly High (>25% Response Rate)

**Definition**: More than 12 responses from 50 sends, or 3+ Score 4–5 contacts, by end of Week 2.

**This is a good problem.** The risk is not overconfidence — it is getting pulled into deep follow-up conversations with Tier 1 contacts when you should be moving to Tier 2 preparation.

**Management approach**:
- Continue follow-up loop as planned (Weeks 4–7); do not abbreviate it
- Begin Tier 2 preparation 1 week earlier than planned (start of Week 4 instead of Week 5)
- Capture case study language from high-engagement Tier 1 contacts — these become the opening sentences in Tier 2 emails ("A legal aid organization using this guide with clients said...")
- Do not reference specific organizations by name without explicit permission. Use category descriptions: "an immigration legal aid organization in [state]" is specific enough to be credible and general enough to be safe

**Impact on Tier 2 timing**: Move Tier 2 launch from Week 5 to Week 4. Do not move it earlier than Week 4 — you need at least 3 weeks of Tier 1 response data before Tier 2 outreach.

---

### Scenario C: A Named Organization Publicly References the Corpus

**Definition**: EFF, ACLU, Freedom of the Press Foundation, Georgetown CPT, or a comparably prominent organization mentions the corpus in public-facing content (newsletter, social media, published resource).

**This changes the sequencing significantly**:
1. Immediately update your Tier 2 and Tier 3 email templates to reference the citation: "The corpus has been referenced by [Organization] as a resource for..."
2. Move Tier 2 outreach for the 2A digital rights sector forward if you are still in Week 3 or later — momentum compounds
3. Begin Tier 3 research immediately, even if Tier 2 has just started — a prominent citation compresses the credibility-building timeline
4. Consider a social media post citing the reference (if you have a public presence for this project) to create secondary distribution

---

### Scenario D: A Significant Risk Event (Political Change, Funding Cut, Media Backlash)

**Political change** (e.g., administration reversal of ELITE program, or new legislative immunity for data brokers):
- Do not halt outreach unless the threat model itself is factually wrong
- Update the corpus date-sensitive sections (FISA 702 status, Palantir contract figures, DOGE litigation) if material changes occur
- The quarterly review scheduled for July 26, 2026 is the formal update checkpoint; do not do ad hoc updates mid-campaign unless the error is factually critical

**Funding cuts to recipient organizations**:
- Some Tier 1 organizations (immigration legal aid) face funding threats in the current environment. If a target organization has publicly announced layoffs or program cuts, delay outreach to them until their situation stabilizes — they do not have capacity to evaluate new resources during internal crisis.
- Mark as "Pause — organizational disruption" in tracking spreadsheet with a revisit date

**Media backlash against the corpus or author**:
- This is unlikely given the corpus's primary-source grounding, but if it occurs: do not withdraw the corpus. Instead, let the FOIA-sourced citations speak for themselves. Refer any critics to the primary sources directly. Do not engage defensively.
- If a security researcher publicly critiques specific countermeasures, evaluate the critique on the merits. If a correction is warranted, update the Gist and note the version change. This is a feature, not a failure — it makes the corpus more trustworthy.

---

## Section 4: Resource Constraints and Workload Model

### Can Tiers Run Concurrently?

**Short answer**: Partially. The active outreach phases of each tier should be strictly sequential. The follow-up loops can overlap with the next tier's active phase.

**Detailed breakdown by week**:

| Week | Tier 1 Activity | Tier 2 Activity | Tier 3 Activity | Anya Hours |
|------|----------------|----------------|----------------|------------|
| Phase 0 (setup) | Pre-launch setup | — | — | 4–5 hrs |
| Week 1 | Active outreach (25 sends) | — | — | 4 hrs |
| Week 2 | Active outreach (25 sends) | — | — | 4 hrs |
| Week 3 | Active outreach (10–15 sends) | — | — | 3 hrs |
| Week 4 | Follow-up loop | T2 prep begins | — | 4–5 hrs (split) |
| Week 5 | Follow-up loop | Active outreach begins (2A) | — | 5–6 hrs (split) |
| Week 6 | Follow-up loop | Active outreach (2A + 2D) | — | 5–6 hrs (split) |
| Week 7 | Close-out, final log | Active outreach (2D) | — | 4–5 hrs (split) |
| Week 8 | — | Active outreach (2B + 2C) | — | 3–4 hrs |
| Week 9 | — | Active outreach (2B + 2C) | — | 3–4 hrs |
| Week 10 | — | Follow-up loop | T3 prep begins | 4–5 hrs (split) |
| Week 11 | — | Follow-up loop | Active outreach begins (3A) | 5–6 hrs (split) |
| Week 12 | — | Follow-up loop | Active outreach (3A + 3B) | 5–6 hrs (split) |
| Weeks 13–14 | — | Close-out | Active outreach (3B + 3C) | 3–4 hrs |
| Weeks 15–20 | — | — | Follow-up + long-horizon monitoring | 1–2 hrs/week |

**Peak load weeks**: Weeks 5–7 (Tier 1 follow-up overlapping with Tier 2 active outreach) and Weeks 11–12 (Tier 2 follow-up overlapping with Tier 3 active outreach). These are the weeks where the time commitment spikes to 5–6 hours. If Anya's bandwidth is constrained during these windows, prioritize the active outreach tier over follow-ups — follow-ups are valuable but active outreach closes faster.

**Total estimated time over 20 weeks**: 65–85 hours. This is approximately 3–4 hours per week sustained over 20 weeks, with peak weeks at 5–6 hours.

---

## Section 5: Cross-Tier Coordination and Messaging Dependencies

### How Tier 2 Messaging Reinforces Tier 1

Tier 2 messaging does not repeat Tier 1. It builds on it in three specific ways:

**1. Credibility compounding**: Tier 2 emails can reference Tier 1 engagement without naming organizations. "Legal aid organizations working with undocumented clients have begun integrating Part 0 into their client intake process" is both true (if you have a Score 4–5 contact from 1A) and compelling (it answers the question "is this actually being used?"). Use this language only if you have genuine Tier 1 engagement to reference.

**2. Case study integration**: If a Tier 1 organization describes a specific use case (e.g., "we're using this with clients in sanctuary cities"), that use case can be anonymized and incorporated into Tier 2 emails for the 2D journalist sector: "This guide is already being used by legal aid organizations in [state context] to walk clients through data broker opt-outs before enforcement encounters." This answers the journalist's first question: is this newsworthy because it is actually being used?

**3. Sector-specific messaging inheritance**: Tier 1 response patterns tell you which sections of the corpus generate the most engagement. If Tier 1 legal organizations are most responsive to the data broker opt-out angle and less responsive to the device hardening sections, weight your Tier 2 messaging accordingly. The ELITE threat model framing that lands with legal audiences may need adjustment for security researchers (who want technical depth on the ELITE data pipeline) or journalists (who want reportable primary sources).

### Messaging Dependencies: What Requires What

| Tier 2 Claim | Requires | Source |
|-------------|---------|--------|
| "Being used by legal aid organizations" | At least 1 Score 4–5 Tier 1 contact | Tier 1 tracking spreadsheet |
| "Available for curriculum integration" | Nothing — it is always true | No dependency |
| "Has been reviewed by security researchers" | At least 1 researcher providing substantive feedback | Tier 2C engagement |
| "Cited by [Org]" | Documented public citation | Web evidence |
| Reference to May 2026 threat intelligence updates | TIER2_MESSAGING_TEMPLATES.md integration | Pre-existing materials |

### What Not to Claim

Do not imply endorsement unless the endorsing organization has explicitly agreed to be named. "EFF has seen this corpus" is true if you sent them an email and they opened it. "EFF endorses this corpus" is only true if they have published something to that effect. The difference is the difference between accurate attribution and misrepresentation that could damage the project's credibility.

---

## Section 6: Signoff Gates

These are the decision points that require Anya's explicit judgment before proceeding. They are not administrative; they are the moments where the campaign could go wrong if you advance without the right data.

### Gate 1: Tier 1 Launch Authorization (Before Day 1)

**What you are authorizing**: Sending ~50 emails over 3 weeks, using your personal email, representing the corpus, to organizations that work with people in active legal jeopardy.

**Decision inputs to review**:
- [ ] Gist is publicly accessible and contains correct content
- [ ] All five response templates are saved in Gmail (R1–R5)
- [ ] Tracking spreadsheet pre-populated with Week 1 contacts
- [ ] You are satisfied with the email templates and how they represent the corpus
- [ ] You accept that some organizations will decline or not respond, and that this is expected, not a failure

**If you are not satisfied** with any of the above: stop and fix it before Day 1. There is no penalty for delaying Day 1 by a week.

---

### Gate 2: Tier 2 Launch Authorization (End of Week 4)

**What you are authorizing**: Sending ~33 emails over 4–6 weeks to digital rights organizations, academic programs, security researcher communities, and journalist organizations. This tier changes the audience from direct-service organizations to amplifier organizations — the stakes for accurate representation are higher because errors in how you describe the corpus will be evaluated by more technically sophisticated recipients.

**Decision inputs to review**:
- [ ] Tier 1 transition criteria met (see Section 2)
- [ ] You have at least one concrete Tier 1 engagement result to reference (or are comfortable launching without one)
- [ ] Your Tier 2 subject lines have been updated with the May 2026 threat intelligence variants from TIER2_MESSAGING_TEMPLATES.md
- [ ] The sector-specific threat briefings from TIER2_MESSAGING_TEMPLATES.md are ready to attach
- [ ] You have researched and verified current contacts for at least the top 5 Tier 2A priority organizations

**If Tier 1 criteria are not met**: Wait one additional week and re-evaluate. Do not launch Tier 2 on an empty result set.

---

### Gate 3: Tier 3 Launch Authorization (End of Week 10)

**What you are authorizing**: Reaching out to policy organizations, labor unions, and law school clinics — institutions that operate on longer timelines, have higher expectations for evidence, and where a poor first impression is harder to recover from than in Tier 1 or 2.

**Decision inputs to review**:
- [ ] Tier 2 transition criteria met (see Section 2)
- [ ] You have at least one Tier 2 institutional acknowledgment available to reference in Tier 3 emails
- [ ] Semester timing is appropriate for 3C academic law/policy contacts (not May–August)
- [ ] Tier 3 contacts for 3A priority organizations have been researched and verified
- [ ] You have personalized the Tier 3 emails to reference specific publications or programs of each target organization — generic Tier 3 emails will not work

**If Tier 2 criteria are not met**: Delay Tier 3 by 2 weeks. The credibility compounding effect that Tier 3 depends on requires genuine Tier 2 engagement to be real, not asserted.

---

### Gate 4: Quarterly Review (July 26, 2026)

**What this is**: A scheduled check on whether the corpus itself requires updates, not a campaign review.

**Decision inputs to review**:
- [ ] Has the FISA 702 reauthorization status changed since April 26, 2026?
- [ ] Have any Palantir contract figures been updated in public reporting?
- [ ] Has DOGE litigation produced material changes to the surveillance infrastructure documented in the corpus?
- [ ] Is GrapheneOS still the recommended device option (check grapheneos.org/faq)?
- [ ] Has any security researcher identified a factual error in the countermeasures?

**If material updates are required**: Update the Gist and note the version date in the frontmatter. Send a brief update email to all Score 3+ contacts from Tier 1 and Tier 2: "A quarterly update has been made to the corpus at [Gist URL], primarily covering [summary of changes]."

---

## Section 7: Risk Mitigation

### Risks That Could Derail the Sequence

**Risk 1: Gmail deliverability block**

*Probability*: Low if send cadence is respected (5 emails per morning with 3–5 minute gaps). High if you try to batch-send 25 in an hour.

*Indicators*: Gmail warning message; bouncebacks from multiple organizations simultaneously; contact feedback that email went to spam.

*Mitigation*: Run mail-tester.com before Day 1. Respect the cadence. If Gmail issues a temporary sending block, wait 24 hours and resume at normal pace. Do not try to catch up by sending more the next day.

---

**Risk 2: Gist becomes inaccessible**

*Probability*: Low, but GitHub occasionally has outages or restricts content under certain circumstances.

*Indicators*: Gist URL returns 404 or requires login.

*Mitigation*: Keep a local backup of all three corpus files. The Bitly link can be redirected to an alternative host (HackMD, a personal domain, or a zip file shared via secure channel) if GitHub becomes unavailable. Update the Bitly redirect rather than re-sending emails with a new URL.

---

**Risk 3: A Tier 1 organization's leadership objects publicly to the corpus**

*Probability*: Very low. The corpus is factual, legally analyzed, and practically useful. However, some organizations have conservative leadership that may push back on security recommendations they perceive as adversarial to law enforcement.

*Indicators*: A reply asking you to stop contacting them; a public social media post disagreeing with the corpus.

*Mitigation*: Honor any "stop contact" request immediately. Do not engage in public arguments. The corpus speaks through its primary sources — a public objection does not change the FOIA-sourced documentation. Log the organization as "Declined — do not contact" and move on.

---

**Risk 4: Major political shift affecting the threat model**

*Probability*: Moderate over a 6-month campaign window. The threat environment documented (ELITE, FISA 702, data broker pipelines) is unlikely to disappear, but enforcement priorities, contract structures, and legal status can shift.

*Indicators*: A policy change that directly affects a core claim in the threat model (e.g., ELITE contract formally terminated; FISA 702 reform passes with warrant requirement).

*Mitigation*: The quarterly review (Gate 4, July 26, 2026) is the structured response mechanism. For changes that occur between reviews: if a claim in the threat model is factually incorrect, update the Gist immediately and note the correction. If the broader threat has intensified (FISA 702 reform fails, ELITE expands), update the urgency framing in subsequent Tier outreach but do not re-contact organizations you have already reached.

---

**Risk 5: Anya's time is not available for a week or more**

*Probability*: Moderate — life happens over a 20-week campaign.

*Mitigation*: The campaign structure already anticipates this through its "no more than 5 sends per morning" and low-overhead weekly cadence. A one-week pause during active outreach is not damaging — follow-up deadlines simply shift by one week. A two-week pause during the active Tier 1 window (Weeks 1–3) would be harder to recover from without losing contact timing momentum. The mitigation: if you know a gap is coming, batch-prepare the next week's contacts before the gap so you can resume immediately.

---

## Section 8: Tier 1 Practical Launch Checklist

This section is for Anya to use on the morning of Day 1. Keep it open on screen while executing.

### Pre-Send Verification (30 minutes, before sending the first email)

**Gist verification** — do this every Day 1 of each week:
- [ ] Open https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108 in an incognito/private browser window
- [ ] Confirm it loads without a login prompt
- [ ] Confirm all three files are present: threat-model.md, opsec-playbook.md, implementation-guide.md
- [ ] Confirm Part 0 (data broker opt-outs) is intact and the California DROP platform path is documented
- [ ] Record the current file count (3 or 4 including publication-prep.md)

**Contact list verification** — do this the evening before each send day:
- [ ] Today's 5 contacts are pre-identified in the tracking spreadsheet
- [ ] Each email address is verified (checked against the organization's current website, not just the spreadsheet)
- [ ] Each contact has 2–3 personalization sentences drafted in the Notes column
- [ ] No duplicate organizations (search tracking spreadsheet for each org name before adding)
- [ ] No organizations previously marked "Declined — closed" or "Bounce — unreachable"

**From-address confirmation** — do this once at the start of the campaign:
- [ ] Your send-from email address is set and final
- [ ] You have tested deliverability at mail-tester.com (score >8/10 preferred)
- [ ] BCC-self address is the same email (to create labeled archive copies)

**Bitly dashboard** — check at the start of each send day:
- [ ] Log into bitly.com and confirm the short URL is still active
- [ ] Note total click count from prior sends (your baseline for today's comparison)
- [ ] Confirm the Bitly URL redirects correctly (click it yourself in a private browser)

---

### Email Send Instructions

**Batch size**: 5 per morning. Never more than 5 per morning to new domains.

**Timing**: 7:00–9:00 AM in your local timezone. This window correlates with highest email open rates for professional inboxes.

**Gap between sends**: 3–5 minutes minimum between each email. Use this time to update the tracking spreadsheet row for the email you just sent.

**Send sequence for each email**:
1. Open the tracking spreadsheet row for this contact
2. Open Gmail compose window
3. Paste the appropriate template (1A, 1B, or 1C from TIER1_DISTRIBUTION_PREP.md)
4. Insert personalized opening (2–3 sentences from your pre-drafted Notes)
5. Insert your name in place of [Your name]
6. Verify the Gist URL is correct: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108
7. Add yourself to BCC
8. Send
9. Immediately update the tracking spreadsheet: Date Sent, Time Sent, Template Used, Email Variant
10. Apply `Tier1-Outreach/Sent` label to the BCC copy in your inbox
11. Wait 3–5 minutes before the next send

**Subject line rotation**: Use at least two different subject line variants across your weekly batch. A/B variants let you identify which framing performs better (Bitly clicks and response rate per variant). Track which variant you used in the tracking spreadsheet's Email Variant column.

---

### Monitoring for Bounces and Blocks

**Bounces — check within 2 hours of each send**:
- A permanent bounce (Mailer-Daemon with "550 user not found" or similar) requires immediate action
- Research the correct alternate contact (organization website → contact page → communications team email)
- Update the tracking spreadsheet before moving on
- If no alternate found within 15 minutes: note "Bounce — unresolved, fallback to web form" and use the organization's web contact form as the alternate channel

**Temporary failures ("451 try again later")**: These are server-side delays, not permanent failures. Wait 24 hours and the message will typically be retried automatically. No action needed unless the failure persists.

**Gmail rate limit warning**: Stop sending immediately. Wait 24 hours. This means you sent too fast. Resume at the normal pace the next morning — do not try to compensate by sending more.

**Spam complaint feedback**: If a recipient tells you directly that your email went to spam, do not re-send. Instead: ask them to whitelist your address, and use the web contact form for that organization as the channel going forward.

---

### Response Capture: Folder Structure and Reply Triage

**Gmail label structure** (create before Day 1):

```
Tier1-Outreach/
  Sent              — BCC copy of every outreach email sent
  Response-Engagement     — Questions, interest, forwarding intent
  Response-Acknowledgment — "Received, will review" responses  
  Response-Declination    — "Not for us" or explicit declines
  OOO               — Out-of-office auto-replies
  Bounce            — Delivery failure notifications
  Follow-Up-Pending — Contacts awaiting a follow-up from you
```

**Triage process for each incoming reply**:
1. Read the reply fully before classifying
2. Apply the correct label (one label per reply — use the most specific one)
3. Update the tracking spreadsheet: Response Received (Y), Response Date, Response Type
4. If Engagement (Class 1): Reply within 24 hours using Template R1
5. If Acknowledgment (Class 2): Log it; schedule a follow-up for 10 days later
6. If Declination (Class 3): Send Template R3; mark as "Declined — closed" in spreadsheet
7. If OOO (Class 4): Log return date; set calendar reminder for 2 business days after return date
8. If Bounce (Class 5): Research alternate contact immediately

**Referral tracking**: If a contact says "I forwarded this to [person/team]," update the tracking spreadsheet Notes column with the recipient name/role if given. This is a Score 4 signal and should be tracked carefully — a forwarded link to an internal team means the corpus is potentially reaching multiple people at that organization.

---

### First-Week Dashboard

Run this check every Friday during active outreach. It takes 15 minutes.

| Metric | How to Calculate | Target for Week 1 | Signal If Below Target |
|--------|-----------------|------------------|----------------------|
| Emails sent | Count from tracking spreadsheet Sent column | 25 | Execution gap — identify what slowed you |
| Response rate | (Responses / Sends) × 100 | >10% | Framing or contact quality problem |
| Click rate (Bitly) | (Unique clicks / Sends) × 100 | >15% | Subject line not compelling enough to open |
| Engagement responses | Count of Class 1 (Engagement) replies | 2+ | Corpus may not be landing as immediately useful |
| Bounces | Count of Class 5 replies | <5 | >5 bounces suggests contact list quality problem |
| OOO replies | Count of Class 4 | Track only | Do not count as responses |
| Tracking spreadsheet completeness | All 25 rows filled with send data | 100% | Tracking gaps mean you will miss follow-up windows |

**Response rate benchmark context**: Cold email to professional advocacy organizations typically achieves 5–15% response rates. The corpus has strong subject-matter relevance to Tier 1 organizations, which should push toward the upper end of that range. Below 5% after Week 1 is the trigger for a pivot review (see Scenario A in Section 3).

**Sentiment classification**: For each Engagement response, note in the spreadsheet whether the sentiment is:
- *Adoption-intent* — they plan to use it with clients or integrate it
- *Referral-intent* — they plan to share it with their network
- *Research-intent* — they want to verify or extend the claims
- *Neutral-positive* — interested but no specific action stated

The distribution across these sentiment types tells you how the corpus is actually being received versus how you thought it would land.

---

## Section 9: Files Referenced in This Document

| File | Purpose |
|------|---------|
| `TIER1_DISTRIBUTION_PREP.md` | Contact lists, email templates 1A/1B/1C, strategy overview |
| `TIER1_OUTREACH_EXECUTION_PLAN.md` | Full execution guide with daily schedule, response handling, contingency plans |
| `TIER1_OUTREACH_PREPARED.md` | Personalized email drafts for 5 named Tier 1A national organizations |
| `TIER2_DISTRIBUTION_PREP.md` | Tier 2 contact lists, email templates 2A/2B/2C/2D |
| `TIER2_MESSAGING_TEMPLATES.md` | Sector-customized messaging variants with May 2026 threat intelligence integration |
| `TIER3_DISTRIBUTION_PREP.md` | Tier 3 contact lists, email templates 3A/3B/3C, timeline |
| `tier-1-success-metrics.md` | Engagement scoring system (0–5 scale), sector-specific success definitions |
| `engagement-scoring-template.csv` | Pre-populated contact list with scoring columns |
| `DISTRIBUTION_TIMELINE.csv` | Machine-readable schedule with target dates, organizations, and success criteria |
| `DISTRIBUTION_CHECKLIST.md` | Full Tier 1/2/3 contact lists and sharing scripts |

**Canonical Gist URL**: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108

---

*Last updated: 2026-05-06. Corpus reflects surveillance landscape as of April 26, 2026. Quarterly review scheduled: July 26, 2026.*
