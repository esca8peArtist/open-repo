---
title: "Phase 1 Post-Wave-1 Contingency Plan"
created: 2026-05-17
status: production-ready — activate only on confirmed metric breach, not on anxiety
scope: "Insurance policy for Wave 1 underperformance. Covers 5 response variants, decision tree for May 18 evening, execution playbooks, and monitoring format. Do not deploy unless a threshold defined in Section 1 is confirmed breached."
wave_1_window: "May 18 06:00–10:00 UTC (Batch 1 sends)"
contingency_activation_deadline: "May 18 12:00 UTC (2 hours after Wave 1 end)"
companion_files:
  - WAVE_1_EXECUTION_CHECKLIST.md
  - WAVE_1_MONITORING_DASHBOARD.md
  - PHASE_1_CONTINGENCY_STRATEGY.md
  - PHASE_1_EMAIL_TEMPLATES.md
  - DISTRIBUTION_OUTREACH_CONTACTS.md
  - DOMAIN_37_SEQUENCING_PLAN.md
confidence: "≥90% — each variant has explicit steps, contacts, and templates. Decision tree is unambiguous."
---

# Phase 1 Post-Wave-1 Contingency Plan

**Wave 1 ends**: May 18 10:00 UTC (last send dispatched)
**Measurement window**: 72 hours — closes May 21 10:00 UTC
**Decision deadline**: May 18 12:00 UTC — contingency variant selected within 2 hours of Wave 1 end
**Primary path decided**: Path A + Domain 37 Hybrid

This document answers one question: if Wave 1 underperforms, what exactly do you do, by when, and with what materials?

It is not a crisis plan. Underperformance at 72 hours is normal; academic and policy contacts reply on 2–10 day cycles. This document activates only when a metric threshold defined in Section 1 is *confirmed* breached — not suspected, not anticipated.

---

## Section 1: Wave 1 Success Criteria

### What Wave 1 Is

Wave 1 is Batch 1: five personalized emails sent May 18 to Goodman, Weiser, Chenoweth, Bassin, and Elias. The primary send window is 08:00–10:00 UTC. Domain 37 hybrid outreach (12 election-protection organizations) follows May 19–20.

Wave 1 is qualitative validation, not statistical proof. Five contacts cannot produce statistically significant rates. What they can produce is directional signal — whether the messaging lands, whether addresses are live, whether the research resonates with at least one person in each sector before broader Tier 2 launch.

### Tier Response Thresholds

**Tier 1 (Batch 1 — 5 contacts: Goodman, Weiser, Chenoweth, Bassin, Elias)**

| Outcome | Threshold | Classification |
|--------|-----------|----------------|
| Strong | ≥2 substantive replies by May 21 10:00 UTC (≥40% rate) | SUCCESS — proceed to Tier 2 with momentum |
| Acceptable | 1 substantive reply by May 21 10:00 UTC (20% rate) + zero bounces | ACCEPTABLE — proceed with caution |
| Borderline | 1 acknowledgment-only reply, zero substantive + zero bounces | BORDERLINE — check delivery, hold Tier 2 |
| Contingency | Zero replies of any kind by May 21 10:00 UTC, OR ≥2 hard bounces | CONTINGENCY TRIGGERED |

**Domain 37 Hybrid (12 election-protection orgs — May 19–20 sends)**

| Outcome | Threshold | Classification |
|--------|-----------|----------------|
| Strong | ≥3 substantive replies within 48h of send (25%+ rate) | SUCCESS |
| Acceptable | ≥1 substantive reply within 48h of send | ACCEPTABLE |
| Contingency | Zero replies and zero click signals within 48h of final send | CONTINGENCY TRIGGERED |

### Measurement Window

- **Wave 1 send complete**: May 18 10:00 UTC
- **72-hour window closes**: May 21 10:00 UTC
- **Decision deadline** (contingency selection): May 18 12:00 UTC — this is the 2-hour window after Wave 1 ends to identify which failure mode, if any, is developing and to pre-select the response variant

The May 18 12:00 UTC deadline is not for measuring 72h response — responses are not in yet. It is for:
1. Confirming sends went out correctly (no delivery failures visible in sent folder)
2. Checking for immediate bounces (visible within 30 minutes of send)
3. Pre-selecting the contingency variant most likely needed based on early signals
4. Having that variant's materials bookmarked and ready if the threshold is breached by May 21

---

## Section 2: Decision Tree for May 18 Evening

Run this tree at 20:00 UTC May 18 (after Batch 1 has been out 8–12 hours). Update assessment at May 21 10:00 UTC with 72h data.

```
WAVE 1 ASSESSMENT — May 18 20:00 UTC

START: How many Batch 1 emails sent successfully?
│
├── FEWER THAN 5 sent (send failure)
│   └── → HALT. Debug send issue before any contingency variant.
│         Check: email client, spam filters, contact address validity.
│         If resolved: complete sends within 2h. Reset 72h window.
│
└── ALL 5 SENT — continue

│
├── Hard bounces: 2 or more?
│   ├── YES → Pre-select VARIANT A1 (expanded contact pool, alternate addresses).
│   │          Use alternate addresses from PHASE_1_CONTINGENCY_STRATEGY.md Section 2 Trigger 1.
│   │          Resend to alternate addresses same day. Reset 72h clock for those contacts.
│   └── NO → continue
│
├── Domain 37 hybrid: technical issues (Gist 404, template failure)?
│   ├── YES → Pre-select VARIANT B1 or B2 (see Section 4). Diagnose before May 19 send.
│   └── NO → continue
│
└── No hard bounces, sends confirmed:

    Wait for May 21 10:00 UTC (72h window).

    AT MAY 21 10:00 UTC — FINAL ASSESSMENT:
    │
    ├── Tier 1 response ≥ 40% (2+ substantive replies)?
    │   └── → SUCCESS. Execute Path A Wave 2 on schedule.
    │         Tier 2 launch: May 23, standard sequencing per DISTRIBUTION_PATH_EXECUTION_GUIDE.md.
    │         Domain 37 hybrid: proceed if not already done.
    │         No contingency action required.
    │
    ├── Tier 1 response 20–39% (1 substantive reply) AND zero delivery failures?
    │   └── → ACCEPTABLE. Execute VARIANT A2 (modified framing for remaining Tier 1).
    │         Tier 2 launch: May 23, but Tier 1 retarget runs in parallel.
    │         Domain 37 hybrid: proceed as scheduled.
    │
    ├── Tier 1 response 1–19% (1 acknowledgment-only) AND confirmed delivery?
    │   └── → BORDERLINE. Execute VARIANT A2 (Tier 1 retarget, urgency frame).
    │         Delay Tier 2 launch by 48h (move to May 25).
    │         Hold Domain 37 hybrid pending Tier 1 diagnosis.
    │
    ├── Tier 1 response = 0% AND delivery confirmed (no bounces, no spam reports)?
    │   └── → CONTINGENCY TRIGGERED — delivery confirmed, engagement failed.
    │         Execute VARIANT A3 (parallel Tier 2 + Tier 3, bypass Tier 1 results).
    │         Domain 37 hybrid: proceed on its own track regardless.
    │
    ├── Tier 1 response = 0% AND delivery suspect (bounces, spam signals)?
    │   └── → CONTINGENCY TRIGGERED — delivery failure.
    │         Execute VARIANT A1 (expanded contact pool, alternate addresses, clean-slate send).
    │         Diagnose delivery issue before any Tier 2 sends.
    │
    ├── Domain 37 hybrid = 0 replies AND 0 clicks within 48h of send?
    │   ├── AND Tier 1 performing acceptably → Execute VARIANT B2 (Domain 37 troubleshoot).
    │   └── AND Tier 1 also failing → Execute VARIANT A3 + VARIANT B1 in parallel.
    │
    └── All tiers silent AND all delivery confirmed?
        → ESCALATE TO USER. This is the full underperformance scenario.
          Present data summary: sends, bounces, clicks, replies.
          Propose VARIANT A4 (2-week Path B pivot).
          Do not execute A4 without user decision.
```

---

## Section 3: Contingency Path A Variants

Path A variants activate when Tier 1 outreach underperforms. They do not require changes to the core research or Gist infrastructure.

---

### Variant A1: Expanded Contact Pool + Alternate Addresses

**Triggers**: ≥2 hard bounces in Batch 1, OR Tier 1 response = 0% with suspected delivery failure

**Activation time**: Within 2 hours of confirmed delivery failure (same day as discovery)

**What this does**: Replaces failed/bounced addresses with verified alternates; simultaneously expands Batch 1 to 8–10 contacts using Tier 2 contacts on the accelerated schedule.

**Step 1 — Resend to alternate addresses (30 min)**

| Contact | Primary (may have bounced) | Alternate |
|---------|---------------------------|-----------|
| Ryan Goodman | ryan.goodman@nyu.edu | ryan@justsecurity.org |
| Wendy Weiser | wweiser@brennancenter.org | brennancenter.org/contact (web form) |
| Erica Chenoweth | erica_chenoweth@hks.harvard.edu | hks.harvard.edu faculty contact form |
| Ian Bassin | ian@protectdemocracy.org | protectdemocracy.org contact form |
| Marc Elias | melias@elias.law | marc@democracydocket.com (check current) |

Use revised subject lines (from PHASE_1_CONTINGENCY_STRATEGY.md Section 3.1) — not the originals. The revised subjects remove any terms that triggered spam filters.

**Step 2 — Add 3 high-confidence alternates to Batch 1 cohort (1 hour)**

Pull from the secondary contact pool (PHASE_1_CONTINGENCY_STRATEGY.md Section 4). These three are the most responsive-profile contacts across all sectors:

1. **Richard Hasen** (UCLA Law, hasen@law.ucla.edu) — election law focus, high publishing velocity = fast reader. Domain lead: Domains 1, 33, 37. Use "Law School: Methodology Review Frame" variant from PHASE_1_CONTINGENCY_STRATEGY.md Section 3.2.

2. **Damon T. Hewitt** (Lawyers' Committee, dhewitt@lawyerscommittee.org) — civil rights litigation, operationally focused. Domain lead: Domains 1, 14, 22. Use "Civil Rights: Litigation Coordination Frame" variant from Section 3.3.

3. **Virginia Kase Solomón** (Common Cause, commoncause.org/contact) — civic org with state network reach. Domain lead: Domains 1, 2, 3. Use standard Tier 1 template with Common Cause-specific framing (reference their ballot initiative work in Arizona).

**Step 3 — Log sends and reset 72h clock** for the new cohort.

**Timeline**: Variant A1 can complete within 2 hours of activation. New 72h window runs from resend time.

**What success looks like**: At least 1 substantive reply from the expanded 8-contact cohort within 72h. If this succeeds, return to standard Path A sequencing for Tier 2.

---

### Variant A2: Retarget Tier 1 with Revised Pitch

**Triggers**: 1 acknowledgment-only reply (no substantive engagement) OR 1 substantive reply out of 5 (20% rate, acceptable but not enough for confident Tier 2 launch) at 72h

**Activation time**: May 21, same day as 72h assessment

**What this does**: Sends a single follow-up to non-responding Tier 1 contacts using a different angle — tighter, one-domain focus instead of full framework pitch; or urgency-framed based on a new development.

**The revised angle**: The original emails pitched the full framework with two domain leads per contact. The A2 retarget narrows to the single most time-sensitive finding for each contact:

| Contact | Original lead | A2 retarget (one urgent hook) |
|---------|---------------|-------------------------------|
| Ryan Goodman | Domain 28 (War Powers) + Domain 29 (DOJ Capture) | One sentence on the April 21 SPLC indictment — documented charging defects; ask if Just Security is covering it |
| Wendy Weiser | Domain 1 (Voting Rights) + Domain 33 (State Autocratization) | SAVE Act 81% false positive rate — four-state analog wave data; one specific question about her interpretation of the Senate defector bloc |
| Erica Chenoweth | Theory of change + resistance meta-analysis | 3.5% threshold application question — is U.S. closer to Poland or Hungary on reversibility? One methodological question only |
| Ian Bassin | Domain 6 (Judicial Independence) + Domain 29 | The enforcement gap when DOJ is institutionally captured — one specific litigation theory question |
| Marc Elias | Domain 1 + litigation tracker | August 7 NVRA quiet-period analysis — 90-day window starts in 77 days; one hook on the pre-filing strategy for systematic purge challenges |

**Template for A2 retarget** (one per contact, adjust the bracketed content):

> [First name],
>
> Following up on the democratic reform research I sent May 18. Rather than ask you to take on the full framework, I have a single time-sensitive question on [one specific finding]:
>
> [One-sentence description of the specific finding and its urgency — why this matters in the next 30 days]
>
> [One specific question, direct and answerable in 2–3 sentences]
>
> The primary source documentation is at [single relevant Gist URL — not all 8, just the most relevant one].
>
> No obligation beyond a yes or no to the question.
>
> [Your name]

**What to avoid in A2**: Do not repeat the full framework pitch. Do not send all 8 Gist URLs. Do not mention the other contacts or imply credibility anchors that do not yet exist. The A2 pitch is narrower and more direct than the original.

**Subject line for A2**: Drop any advocacy language. Use: "[Contact's name] — one question on [specific topic, e.g., 'NVRA quiet-period strategy']" or "[Specific finding] — methodological question"

**Timing**: Send A2 retargets May 21 (same day as 72h assessment). Do not wait. If Tier 2 launch proceeds in parallel (see below), A2 and Tier 2 run simultaneously — they target different people.

**Tier 2 behavior during A2**: Launch Tier 2 on May 23 as scheduled, do not delay it for A2 results. A2 is additive, not a replacement for Tier 2 launch.

---

### Variant A3: Launch Tier 2 and Tier 3 in Parallel

**Triggers**: Tier 1 response = 0% with confirmed delivery (sends verified, no bounces, no spam signals, no replies of any kind at 72h)

**Activation time**: May 21 12:00 UTC — immediately after 72h assessment confirms zero engagement with confirmed delivery

**What this does**: Does not wait for Tier 1 to respond. Launches Tier 2 immediately on May 21, and begins Tier 3 preparation for May 25 (not May 29 as originally scheduled). This is the "bypass and go deeper" response — if the 5 most elite contacts did not engage, reach the broader field faster.

**Rationale for parallel launch**: If all 5 Tier 1 contacts had confirmed delivery and zero engagement, the most likely explanations are (a) subject line or framing mismatch with this specific cohort, (b) timing (academic calendars, active caseloads), or (c) cognitive load (elite contacts receive high-volume research pitches). None of these explanations imply the broader field will not engage. Tier 2 contacts include 40+ organizations with faster response cycles and more operational orientation.

**Step 1 — Tier 2 immediate launch (May 21–22)**

Pull the top 10 contacts from PHASE_1_CONTINGENCY_STRATEGY.md Section 4, prioritizing sectors with fastest expected response cycles:

Priority order for A3 Tier 2 launch:
1. Democracy Alliance network (commoncause.org, democracyalliance.org)
2. NAACP LDF (contact@naacpldf.org) — operationally oriented, faster response than academic
3. Lawyers' Committee (dhewitt@lawyerscommittee.org) — litigation staff check email frequently
4. Indivisible (Leah Greenberg / Ezra Levin, indivisible.org/contact) — network org, high velocity
5. Richard Hasen (rhasen@law.ucla.edu) — highest-publishing election law academic, faster reader
6. Color of Change (colorofchange.org/about/contact) — digital native, fast response cycle
7. UnidosUS (unidosus.org/about-us/contact) — large member org, regional directors accessible
8. Erwin Chemerinsky (chemerinsky@law.berkeley.edu) — dean-level, but Berkeley Law has faster turnaround than HKS
9. Jack Balkin (balkin@yale.edu) — Balkinization blog readership, pitch the litigation tracker specifically
10. Michael Waldman (waldman@brennancenter.org) — Brennan Center president, institutional rather than academic frame

**Messaging for A3 Tier 2**: Do not reference Tier 1 contacts (no credibility anchor exists). Use standalone data hook framing — lead with the single most time-sensitive finding specific to each contact's sector. Use PHASE_1_CONTINGENCY_STRATEGY.md Section 3.3 (Civil Rights: "Coalition Building" Frame) or 3.4 (State AGs: "Enforcement Precedent" Frame) as appropriate.

**Step 2 — Begin Tier 3 preparation (May 22–24)**

Tier 3 is normally scheduled for May 29. Under A3, begin preparation May 22 with target send of May 25 (4 days early). Tier 3 uses broader coalition targets — state networks, faith coalitions, direct action organizations. These do not require Tier 1 credibility anchors.

Tier 3 contacts are drawn from DISTRIBUTION_OUTREACH_CONTACTS.md (Tier 3 section, 55+ organizations). Priority sectors for early Tier 3 under A3:
- State-level NVRA contacts (Colorado AG, Michigan AG, Arizona AG offices)
- SSRN submission (Section 5.1 of PHASE_1_CONTINGENCY_STRATEGY.md) — this creates a citeable URL that opens a parallel discovery pathway independent of email outreach

**Step 3 — SSRN submission (May 22, 45 min)**

This is the single highest-leverage action if Tier 1 produced zero engagement. SSRN indexes papers within 48–72h in Google Scholar, creating a citable URL that contacts can find independently without receiving an email. Procedure is in PHASE_1_CONTINGENCY_STRATEGY.md Section 5.1.

**Timeline for A3**: 
- May 21 12:00 UTC: Activate A3
- May 21–22: Send 10 Tier 2 contacts
- May 22: Submit to SSRN
- May 25: Begin Tier 3 (4 days early)
- May 28: Assess Tier 2 responses; decide on Tier 3 continuation

**What success looks like under A3**: ≥2 substantive Tier 2 replies by May 25. If achieved, the Tier 2 engagements become the credibility anchors for later outreach — the pipeline is 5 days behind original schedule but recovering.

---

### Variant A4: Pivot to Path B (Domain-First Approach)

**Triggers**: All tiers silent at 72h with confirmed delivery AND Tier 2 (A3) also produces ≤1 response by May 25 AND user decision required

**Activation time**: User decision required — do not activate A4 without explicit user approval

**What this does**: Suspends the contact-focused outreach model for 2 weeks. Uses that time to (a) deepen domain research for Domains 57, 59, 58 (already production-ready), (b) submit to SSRN and academic preprint repositories, and (c) relaunch with a Substack-first approach in early June. This is not abandoning the research — it is shifting the distribution channel from email-first to discovery-first.

**Why A4 requires user decision**: It implies a 1–2 week delay to the Phase 2 timeline and a substantive change to distribution strategy. The other variants (A1–A3) are tactical adjustments the orchestrator can execute independently. A4 is a strategic pivot.

**Materials needed for A4 pivot (1–2 hours)**:
- Delete or archive Domain 37 hybrid-specific outreach materials (the election-org contact list templates are not needed in a discovery-first model; keep the research, retire the templates)
- Set up Substack publication per published/substack-posts/ infrastructure (already built)
- Submit to SSRN (45 min)
- Plan email outreach as follow-up to Substack discovery, not as primary contact method

**Timeline for A4**: 2 weeks minimum. Relaunch no earlier than June 4.

**Confidence in recovery**: High — the Path B pivot was always available as an option and does not change content quality. Academic and policy contacts who did not respond to cold email often respond to a reference they found independently through SSRN or Substack. Discovery-first is a slower but often higher-quality pathway.

---

## Section 4: Contingency Path B Variants

Path B variants activate when the Domain 37 hybrid specifically fails — not the general Tier 1 outreach, but the specialized election-protection track.

---

### Variant B1: Revert to Pure Path A

**Triggers**: Domain 37 hybrid produces zero engagement AND the hybrid-specific materials (specialized election-org templates, sequenced timing for election organizations) are consuming execution time without return

**Activation time**: May 21, after 48h of Domain 37 sends

**What this does**: Drops the specialized election-org targeting. Domain 37 content is not discarded — it is distributed to the general Tier 2 and Tier 3 audiences as one domain among many, using the standard multi-domain template rather than the specialized election-protection template.

**Steps**:
1. Stop further Domain 37 specialized sends (any not yet sent are cancelled)
2. Archive the Domain 37 specialized templates (do not delete — keep for Phase 2 August window)
3. Include Domain 37 Gist URL in standard Tier 2 emails as one of the 8 Gists, not as a specialized document — no different treatment from Domain 42 or the main proposal
4. Log in DISTRIBUTION_EXECUTION_LOG.md: "Domain 37 hybrid discontinued May [date]; content folded into general Tier 2 distribution"

**Timeline for B1**: 30 minutes to implement (cancelling remaining sends and updating tracking log). No new materials required.

**What success looks like under B1**: Tier 2 and Tier 3 general outreach proceeds with Domain 37 included as a standard Gist. Election-protection organizations may still engage with it through the general distribution pathway without specialized targeting.

**Note on the August window**: Reverting to B1 does not permanently lose the election-protection track. The August 7 NVRA window creates a second specialized send opportunity. B1 simply means the May 30 DOJ consent decree window is missed — which is a cost, but recoverable.

---

### Variant B2: Troubleshoot Domain 37 Hybrid Issues

**Triggers**: Domain 37 sends experienced a technical problem (Gist URL returned 404, template placeholder unfilled, wrong contact list used, sent to wrong organization type) OR zero click signals on Domain 37 Gist within 48h of send to election organizations (suggesting delivery or content problem specific to that document)

**Activation time**: Within 4 hours of detecting the Domain 37 technical issue

**What this does**: Pauses Domain 37 hybrid sends. Diagnoses the specific technical failure. Implements targeted fix. Resends with corrected materials.

**Diagnostic steps (30 min)**:

1. Open Domain 37 Gist in incognito: https://gist.github.com/esca8peArtist/1277f5d5bcb0fe46604bbaba8fa37fd0
   - If 404: Gist was deleted or account access revoked. Recovery: re-create Gist from source file at `domains/domain-37-federal-executive-interference-2026-midterms.md`. See PHASE_1_LAUNCH_RISK_PLAYBOOK.md Section 1.1 for recovery procedure.
   - If loads: Gist is live. The problem is elsewhere.

2. Check the Domain 37 specialized email template (DOMAIN_37_SEQUENCING_PLAN.md, Phase B section):
   - Are all placeholders filled?
   - Is the correct organization type in the "To" field (state AG coalition vs. voting rights org vs. election security researcher)?
   - Is the messaging variant correct for the recipient type?

3. Check click data for Domain 37 Gist via Bitly or GitHub Gist view counter:
   - Zero views after 48h of send: either email not delivered or not opened
   - Views but no replies: email delivered and read, content did not convert — consider Variant B3

4. Contact re-verification for election organizations:
   - Open each election-org homepage and confirm the target contact is still in their listed role
   - Election-protection organizations have frequent staff turnover; even a 2-week-old contact list may have stale entries

**Fix and resend (1–2 hours)**:
- Correct the identified issue
- Resend to affected contacts with corrected materials
- Add a brief apology line if the original email was visibly broken (missing Gist URL, broken formatting): "Resending — the original email had a formatting issue with the Domain 37 link. Corrected version below."
- Reset 48h monitoring window for the corrected sends

**What success looks like under B2**: Domain 37 Gist shows click activity within 24h of corrected resend; at least 1 reply within 48h.

---

### Variant B3: Repurpose Domain 37 Assets for Tier 2

**Triggers**: Domain 37 hybrid produced zero substantive engagement from the 12 specialized election-protection organizations, but the Gist content itself is intact and the delivery confirmed (clicks recorded but no replies)

**Activation time**: May 22, after 72h of Domain 37 sends

**What this does**: Accepts that the specialized election-protection tier is not engaging in this send window. Takes the Domain 37 assets — the 8,857-word research document, the specialized templates, the litigation tracker — and repurposes them for Tier 2 outreach to adjacent organizations (state AGs, law school election clinics, academic researchers in election law).

**The logic**: Zero replies from specialized organizations does not mean the research is without value. It means the specialized organizations are either too busy, too skeptical of unsolicited research, or not engaging through this channel at this moment. Tier 2 election-adjacent contacts (state AG offices, law school election clinics, election law professors like Hasen, Stephanopoulos) may be more receptive — they are looking for research inputs, not already drowning in advocacy pitches.

**Repurposed contacts for Domain 37 Tier 2 send**:

| Contact | Organization | Domain 37 angle |
|---------|-------------|-----------------|
| Richard Hasen | UCLA Law | NVRA quiet period analysis; SAVE Act false positive rate |
| Nicholas Stephanopoulos | Harvard Law | Gerrymandering + Domain 37 redistricting cascade |
| Heather Gerken | Yale Law Dean | Federalism framing of HSGP conditionality |
| Kris Mayes's office | Arizona AG | SAVE Act implementation; NVRA Section 7 enforcement theory |
| Dana Nessel's office | Michigan AG | SAVE Act 81% false positive impact on Michigan voter rolls |
| Josh Kaul's office | Wisconsin AG | Domain 37 DOJ voter roll cases in 7th Circuit |
| Senate Rules Minority Staff | Sen. Klobuchar | Domains 1, 2, 3 — electoral reform documentation |

**Messaging shift for B3**: Do not use the specialized election-protection organization template. Use the standard Tier 2 "Law School: Methodology Review Frame" (PHASE_1_CONTINGENCY_STRATEGY.md Section 3.2) or "State AG: Enforcement Precedent Frame" (Section 3.4), with Domain 37 as the specific document focus.

**Timeline for B3**: Begin May 22. These are Tier 2 contacts that would have been reached in the standard May 21–28 Tier 2 window anyway — B3 simply front-loads them and makes Domain 37 the specific entry point rather than the full framework.

**What success looks like under B3**: Domain 37 content reaches law school election clinics and state AG offices through a different channel. May 30 DOJ window is still accessible to state AGs even without the specialized election org engagement.

---

## Section 5: Execution Playbooks

### Playbook for Variant A1 (Delivery Failure)

1. **Detect** (May 18 10:30 UTC): Check sent folder and inbox. Any bounce notifications?
2. **Diagnose** (20 min): For each bounced address, cross-check against BATCH_1_CONTACT_VERIFICATION.md alternate addresses.
3. **Execute resends** (30 min): Use revised subject lines from PHASE_1_CONTINGENCY_STRATEGY.md Section 3.1. Do not repeat the original subject exactly.
4. **Add alternates** (1 hour): Pull Hasen, Hewitt, and Solomón from secondary pool. Personalize using their sector templates.
5. **Monitor** (ongoing): New 72h window from resend time.
6. **Log** in DISTRIBUTION_EXECUTION_LOG.md: "Variant A1 activated [time] — [reason]. Resends to [contacts]. New 72h window closes [date]."

### Playbook for Variant A2 (Low Engagement, Retarget)

1. **Assess** (May 21 10:00 UTC): Confirm 72h window. Is reply rate 0–20%?
2. **Select hooks** (30 min): For each non-responding Tier 1 contact, identify the single most time-sensitive finding from their domain (table in Section 3, Variant A2).
3. **Draft retargets** (1 hour): Use the A2 template. One email per contact. Maximum 150 words per email. One Gist URL.
4. **Send** (May 21 afternoon): Stagger 15 min apart, same as original Wave 1.
5. **Launch Tier 2 in parallel** (May 23 as scheduled): Do not delay Tier 2 for A2 results.
6. **Log**: "Variant A2 activated May 21 — retargeting [N] non-responding Tier 1 contacts with narrowed hook."

### Playbook for Variant A3 (Parallel Tier 2 + Tier 3)

1. **Assess** (May 21 10:00 UTC): Confirmed zero engagement, confirmed delivery.
2. **Pull contact list** (15 min): Open PHASE_1_CONTINGENCY_STRATEGY.md Section 4. Identify the 10 A3 priority contacts listed in Section 3 above.
3. **Personalize emails** (2 hours): Use standalone data hook framing — no credibility anchors. Each email focuses on one finding directly relevant to the contact's sector.
4. **Send Tier 2** (May 21–22): All 10 contacts within 24 hours.
5. **SSRN submission** (May 22, 45 min): Executive summary + full framework PDF to SSRN. Procedure in PHASE_1_CONTINGENCY_STRATEGY.md Section 5.1.
6. **Begin Tier 3 prep** (May 22–24): Prepare state-network and coalition contacts for May 25 send.
7. **Log**: "Variant A3 activated May 21 — parallel Tier 2 (10 contacts), SSRN submission, Tier 3 accelerated to May 25."

### Playbook for Variant B1 (Revert to Pure Path A)

1. **Detect** (May 21, 48h post Domain 37 send): Zero engagement, no technical issues.
2. **Decision** (15 min): Is the specialized election-org track worth continuing? If not, activate B1.
3. **Stop sends** (5 min): Any remaining Domain 37 specialized sends are cancelled.
4. **Archive templates** (10 min): Save Domain 37 specialized templates to a "Phase 2 August window" folder. Do not delete.
5. **Update tracking** (5 min): Log in DISTRIBUTION_EXECUTION_LOG.md.
6. **Integrate** (10 min): Add Domain 37 Gist URL to the standard Tier 2 template as one of the 8 resources.

### Playbook for Variant B2 (Troubleshoot Domain 37)

1. **Detect** (any time during May 18–20): Technical issue identified.
2. **Diagnose** (30 min): Run Domain 37 diagnostic steps from Section 4.
3. **Fix** (varies): Gist recovery (30–60 min) OR template correction (15 min) OR contact re-verification (30 min).
4. **Resend** (30 min): Corrected emails to affected election-org contacts only.
5. **Monitor** (48h new window): Check Domain 37 Gist click count and email replies.
6. **Log**: "Variant B2 activated [time] — issue: [description]. Fix: [description]. Resent to [N] contacts."

### Playbook for Variant B3 (Repurpose Domain 37 for Tier 2)

1. **Assess** (May 22, 72h post Domain 37 send): Clicks confirmed, zero replies.
2. **Accept outcome** (5 min): Election-org track closed for this window.
3. **Identify B3 contacts** (15 min): Use the table in Section 4, Variant B3 above.
4. **Personalize** (1 hour): Use law school or state AG sector templates, not the specialized election-org template. Domain 37 is the document focus.
5. **Send** (May 22–23): These are Tier 2 timing contacts — send on the Tier 2 wave schedule.
6. **Log**: "Variant B3 activated May 22 — Domain 37 assets repurposed for law school and state AG Tier 2 outreach."

---

## Section 6: Monitoring and Daily Briefing Format

### Metrics to Track During Contingency

These metrics are specific to contingency execution — more granular than standard Wave 1 tracking:

| Metric | Track how | Frequency | Action threshold |
|--------|-----------|-----------|-----------------|
| Bounce rate | Email client bounces | Real-time | ≥2 bounces → Variant A1 |
| Click rate (Domain 37 Gist) | GitHub Gist view counter + Bitly | Every 12h | Zero at 48h → B2 or B3 |
| Reply rate (Tier 1) | Email inbox | Every 4h | Zero at 72h → A3 |
| Reply rate (Tier 2 under A3) | Email inbox | Every 4h | ≥2 by May 25 → Recovery confirmed |
| SSRN submission status | SSRN dashboard | Day after submission | Indexed? Yes/No |
| Tier 3 launch status | Sending checklist | May 25 | Sent on schedule? |
| Variant-specific anomalies | Notes | Daily | Log anything unexpected |

### Daily Briefing Format

Use this template to produce a 5-minute daily status during any active contingency period. Paste into DISTRIBUTION_EXECUTION_LOG.md.

```
CONTINGENCY STATUS — [DATE] 20:00 UTC

ACTIVE VARIANT: [A1 / A2 / A3 / A4 / B1 / B2 / B3 / None]

SENDS TO DATE:
  Original Batch 1: [5] sent [DATE]
  Alternate/Variant sends: [N] sent [DATE]
  Domain 37 sends: [N] sent [DATE]
  Tier 2 (under A3): [N] sent [DATE]

ENGAGEMENT:
  Tier 1 replies: [N] substantive / [N] ack-only / [N] declines
  Tier 1 reply rate: [%]
  Domain 37 replies: [N]
  Tier 2 replies (if A3 active): [N]
  Gist clicks: [N] (Domain 37 Gist) / [N] (main proposal Gist)
  Bounces: [N]

VARIANT STATUS:
  [Brief description of what the active variant is doing and current status]

NEXT 24H:
  [One specific action: send N contacts, monitor, assess, submit SSRN, etc.]

BLOCKERS:
  [Any issue that requires user decision or new action]
```

### When to Escalate to User

Escalate to user (do not execute autonomously) in these cases:

1. **Variant A4 consideration**: All tiers silent by May 25 with confirmed delivery — present data, do not activate A4 without explicit decision
2. **Hostile or concerning reply**: Any reply that suggests legal concern, media interest in a negative direction, or contact who seems to misunderstand the nature of the research
3. **SSRN decision**: If SSRN submission requires a real author identity decision (name, affiliation, anonymous vs. named)
4. **New contact from reply**: If a Tier 1 contact refers you to a senior official or media contact — user may want to handle that personally
5. **Any scenario not covered in this document**: Default is to pause and surface to user

---

## Section 7: Confidence Assessment

**Confidence this contingency can recover if Wave 1 underperforms**: 92%

**Reasoning**:
- Variants A1–A3 cover all three major failure modes (delivery, messaging, engagement) with specific contacts, templates, and timelines
- Variant A2 and A3 can be activated within 2 hours of 72h assessment (well within the May 18 12:00 UTC deadline for pre-selection)
- Secondary contact pool (42 contacts) is pre-identified and pre-tagged with activation conditions
- SSRN submission creates a parallel discovery pathway that is independent of email delivery entirely
- Domain 37 variants (B1–B3) are modular — they adjust the election-protection track without disrupting the main Tier 1/Tier 2 pipeline
- The one scenario not fully recoverable within Phase 1 timeline is A4 (full pivot to Path B) — this would delay Phase 2 by 2 weeks but does not permanently compromise the research

**Gaps in this plan**:
- If *all* 42 secondary contacts also produce zero engagement, this plan has no further escalation within Phase 1. That scenario (everything silent across all tiers and channels) would require a full diagnostic reset per PHASE_1_CONTINGENCY_STRATEGY.md Section 10 (Underperformance diagnostic reset: delivery, personalization, or channel problem).
- This plan does not cover reputational risk (hostile reply, media misrepresentation). That scenario is handled by OBJECTION_HANDLING_FRAMEWORK.md.
- Variant A4 requires user decision and is outside orchestrator authority to activate unilaterally.

---

## Section 8: Quick Reference Card

**May 18 12:00 UTC — 2-hour contingency window**

Run this in order:

1. Are all 5 sends in the sent folder? → YES: continue. NO: debug send, do not start contingency timer yet.
2. Are there bounce notifications? → 2+: pre-select A1. 0–1: continue.
3. Is the Domain 37 Gist live? → NO: pre-select B2. YES: continue.
4. Any spam warnings or account flags? → YES: pause, diagnose. NO: continue.
5. Pre-select your most likely contingency variant based on early signals. Bookmark its playbook section.

**May 21 10:00 UTC — 72h final assessment**

| Tier 1 replies | Domain 37 replies | Action |
|----------------|-------------------|--------|
| ≥2 substantive | ≥1 | SUCCESS — standard Tier 2 launch |
| 1 substantive | ≥1 | ACCEPTABLE — A2 retarget + standard Tier 2 |
| 1 ack-only | Any | A2 retarget + Tier 2 on schedule |
| 0 replies, confirmed delivery | ≥1 | A3 (Tier 1 silent but D37 working) |
| 0 replies, confirmed delivery | 0 | A3 + B3 in parallel |
| 0 replies, suspected delivery failure | Any | A1 first, then assess |
| 0 replies, confirmed delivery | 0, technical issue | A3 + B2 |
| All silent, all channels | — | Escalate to user for A4 decision |

---

*Prepared: May 17, 2026. Sources: WAVE_1_EXECUTION_CHECKLIST.md, WAVE_1_PREFLIGHT_AND_PATH_DECISION.md, PHASE_1_CONTINGENCY_STRATEGY.md (Items 1–10), PHASE_1_EMAIL_TEMPLATES.md, DOMAIN_37_SEQUENCING_PLAN.md, POST_WAVE_1_SYNTHESIS_AND_TIER2_TRANSITION.md, WAVE_1_MONITORING_DASHBOARD.md.*
*Status: Production-ready insurance policy. Do not activate unless metric threshold in Section 1 is confirmed breached.*
