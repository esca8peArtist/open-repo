---
title: "Wave 1 Execution Checklist — May 18–20, 2026"
created: 2026-05-17
status: ready for execution
scope: "Hour-by-hour / day-by-day guide for Wave 1 distribution. May 18 launch, May 19 monitoring, May 20 closing and analysis."
audience: thorn (executing solo)
estimated_time: "10–15 hours across 3 days"
companion_files:
  - WAVE_1_MONITORING_DASHBOARD.md
  - WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv
  - PHASE_1_WAVE1_EXECUTION_PREP.md
  - WAVE_1_PRESTAGING_READINESS.md
  - PHASE_1_CONTINGENCY_STRATEGY.md
  - PHASE_1_EMAIL_TEMPLATES.md
  - DISTRIBUTION_EXECUTION_LOG.md
---

# Wave 1 Execution Checklist

**May 18–20, 2026**
**Batch 1**: 5 contacts (Goodman, Weiser, Chenoweth, Bassin, Elias)
**All 8 Gists**: Live and verified (see WAVE_1_PRESTAGING_READINESS.md Section 2)
**Email templates**: Ready in execution/phase-1-personalized-batch-1.md
**Total time**: 10–15 hours across 3 days

One rule: if something breaks, consult PHASE_1_CONTINGENCY_STRATEGY.md. Do not improvise. Every failure mode has a pre-written response.

---

## May 18 — Launch Day (6–8 hours total)

### Pre-Launch Block (07:00–09:00 UTC — 1.5 hours)

This block happens before the first email leaves your drafts folder. Do not skip any item — these catches prevent wasted sends.

**Gist pre-flight (8 minutes)**

- [ ] Open https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261 in incognito — main proposal loads, tables render
- [ ] Open https://gist.github.com/esca8peArtist/2869da6eaeb15a47246ade3bbbc4a3f4 in incognito — executive summary loads
- [ ] Open https://gist.github.com/esca8peArtist/1277f5d5bcb0fe46604bbaba8fa37fd0 in incognito — Domain 37 standalone loads
- [ ] Open https://gist.github.com/esca8peArtist/418d51bda087f15a04d685ab171a5ee0 in incognito — litigation tracker loads
- [ ] Open https://gist.github.com/esca8peArtist/98dc61a3294a612482b37bd80f5c94ab in incognito — Domain 42 loads
- [ ] Record baseline Gist view counts for main proposal and Domain 37 in WAVE_1_MONITORING_DASHBOARD.md (you need a pre-send baseline to measure delta)

If any Gist returns 404: wait 60 seconds, retry. If still failing, do not send until resolved. See PHASE_1_LAUNCH_RISK_PLAYBOOK.md Section 1.1 for recovery steps.

**Contact re-verification (10 minutes)**

All five Batch 1 contacts were verified May 15. Run a 90-second spot-check for each — open the institutional page, confirm the name is still listed. This catches any role changes in the past 3 days.

- [ ] Goodman: visit justsecurity.org or law.nyu.edu/faculty — name and role confirmed
- [ ] Weiser: visit brennancenter.org/about/leadership — VP Democracy confirmed active
- [ ] Chenoweth: visit hks.harvard.edu faculty directory — Academic Dean + Frank Stanton Professor confirmed
- [ ] Bassin: visit protectdemocracy.org — org confirmed active (team page 404 is known; check homepage)
- [ ] Elias: visit democracydocket.com or elias.law — confirmed active; email is melias@elias.law (NOT perkinscoie.com)

**Template final scan (15 minutes)**

- [ ] Open all 5 email drafts in your drafts folder
- [ ] Scan each for remaining {{placeholder}} or [bracket] strings — there should be zero
- [ ] Confirm {{YOUR_NAME}} is filled in all 5 (your actual name)
- [ ] Confirm {{YOUR_CONTACT_INFO}} is filled in all 5 (your email/phone)
- [ ] Confirm Elias email says "decided April 29, 2026" for Callais (not "pending")
- [ ] Confirm Watson v. RNC is correctly framed as "pending — decision expected end of June term"
- [ ] Confirm path-specific block is selected (A / A+37 / B) — only one block per email, the other two deleted
- [ ] Check that Gist URLs in the email bodies are the correct canonical URLs (not old versions)

**Spreadsheet baseline (5 minutes)**

- [ ] Open WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv (or your Google Sheets equivalent)
- [ ] Confirm all 5 Batch 1 rows are populated with contact name, org, sector, send date (today), email status = blank
- [ ] Record baseline Gist view counts in the tracking sheet

**Test send (5 minutes)**

- [ ] Send one test email to yourself from the same account you'll use for Batch 1
- [ ] Confirm: arrives in inbox (not spam) within 3 minutes, formatting intact, Gist links render when clicked
- [ ] If test email lands in spam: stop. Address the spam flag before sending to any contacts. See PHASE_1_LAUNCH_RISK_PLAYBOOK.md Section 1.3.

---

### Send Block (08:00–12:00 UTC — 2 hours active, 4 hours window)

Stagger sends by 15 minutes minimum, 30 minutes preferred. Midday East Coast (12:00–14:00 EDT) is optimal for inbox visibility.

Recommended UTC times (adjust to your schedule — keep the stagger):

- [ ] **08:00 UTC**: Send Email 1 — Ryan Goodman (ryan.goodman@nyu.edu)
  - Log timestamp in tracking sheet
  - Note: alternate is ryan@justsecurity.org if NYU address bounces

- [ ] **08:30 UTC**: Send Email 2 — Wendy Weiser (wweiser@brennancenter.org)
  - Log timestamp
  - Check inbox for bounce notification 5 minutes after send

- [ ] **09:00 UTC**: Send Email 3 — Erica Chenoweth (erica_chenoweth@hks.harvard.edu)
  - Log timestamp
  - Note: underscore format is required — echenoweth@hks.harvard.edu will bounce

- [ ] **09:30 UTC**: Send Email 4 — Ian Bassin (ian@protectdemocracy.org)
  - Log timestamp
  - Alternate: protectdemocracy.org contact form if address bounces

- [ ] **10:00 UTC**: Send Email 5 — Marc Elias (melias@elias.law)
  - Log timestamp
  - Note: perkinscoie.com is permanently stale (left 2021). Do not use.

**30-minute post-send check (10:30 UTC)**

- [ ] Scan inbox for bounce notifications from any of the 5 sends
- [ ] If zero bounces: log "0 bounces" in tracking sheet
- [ ] If 1+ bounce: identify the contact, check the alternate address in PHASE_1_WAVE1_EXECUTION_PREP.md Section 1, resend to alternate before moving on
- [ ] Update Status column in tracking sheet: all 5 should now show "Sent/Pending"

---

### Initial Monitoring Block (10:30–14:00 UTC — 30 minutes active)

- [ ] Check Bitly dashboard (if Bitly shortlinks were used in email bodies) — note any clicks since send
- [ ] Check Gist view count for main proposal and Domain 37 — any delta from baseline?
- [ ] Respond to any auto-replies (out-of-office) — log in tracking sheet as delivery confirmation, not engagement
- [ ] If any substantive reply arrives (unusual for same-day sends but possible from Elias): respond within 4 hours; log reply type and score in tracking sheet

---

### LinkedIn / Social Block (optional — 14:00–16:00 UTC — 30 minutes)

If you staged LinkedIn posts in WAVE_1_PRESTAGING_READINESS.md Section 4.4, schedule or publish now.

- [ ] Post 1 (Domain 42 / DEA deadline framing) — schedule for 08:00 UTC May 19 if not already scheduled
- [ ] Post 2 (litigation tracker / voting rights) — schedule for 09:00 UTC May 20
- [ ] Twitter/X Thread 1 — publish now or schedule for tomorrow morning

---

### Day 1 Evening Block (20:00 UTC — 20 minutes)

- [ ] Final inbox check: any replies, bounces, or auto-responses since last check?
- [ ] Update all rows in tracking sheet with current status
- [ ] Record Gist view count delta from morning baseline
- [ ] Complete May 18 Reflection in WAVE_1_MONITORING_DASHBOARD.md Section 6
- [ ] Paste Day 1 status summary into DISTRIBUTION_EXECUTION_LOG.md using the status block template from WAVE_1_MONITORING_DASHBOARD.md Section 2
- [ ] Set a reminder for 10:00 UTC May 19 morning check

**Day 1 expected state**: 5 sent, 0 bounces, 0 replies (normal), possibly 1–2 Gist views above baseline. No action required if this matches expectations.

**Day 1 total time**: 6–8 hours (including setup, send window, monitoring, and evening block)

---

## May 19 — Monitoring and Responding (2–4 hours total)

### Morning Check (10:00 UTC — 30 minutes)

- [ ] Check inbox for overnight replies or bounces (anything since 20:00 UTC May 18)
- [ ] If any substantive reply received: classify using WAVE_1_MONITORING_DASHBOARD.md Section 1 Reply Type table; assign score 0–5; update tracking sheet immediately
- [ ] Respond to any replies requiring a response within 4 hours of your morning check
- [ ] Check Bitly dashboard — note cumulative clicks since send
- [ ] Check Gist view count for main proposal and Domain 37 — record in tracking sheet

**If a reply arrived overnight from Elias (2–3 day cycle is possible)**:
This is the most likely early reply. Elias handles active litigation and may respond quickly if the Callais cascade framing is directly relevant to his current caseload.
- Read the full reply before responding
- If the reply mentions a specific case or asks a specific domain question: this is a Score 4–5 signal; mark as Tier 2 candidate immediately; respond with specificity (reference the domain directly, offer a domain extract if relevant)
- If the reply is general ("interesting, will read"): Score 1; update tracking; no immediate follow-up needed

---

### Active Monitoring Block (12:00–16:00 UTC — 1 hour active)

- [ ] Check inbox again at 12:00 UTC and 16:00 UTC (two spot-checks during business hours)
- [ ] Respond to any clarification requests within 4 hours of receipt
- [ ] For any reply that mentions a specific colleague or organization: immediately extract the secondary contact name/org and add to the Tier 2 referral list in WAVE_1_MONITORING_DASHBOARD.md Section 4

**Stockport infrastructure checkpoint reminder**: May 19 20:00 UTC is the stockbot infrastructure checkpoint. If this requires your attention, block 18:00–21:00 UTC as potentially occupied. Plan the Day 2 evening update for 21:30 UTC if needed.

---

### Clarification Response Protocol

If a contact asks for clarification on any domain, respond same-day using this structure:

1. Thank them briefly (one sentence — do not over-effuse)
2. Answer the specific question directly (2–3 sentences maximum)
3. Offer one concrete next step (e.g., "I can send you the Domain 37 standalone document which goes deeper on the redistricting cascade" or "I could send you a plain-language extract if that's more useful for your context")
4. Do not volunteer additional domains or send additional Gist links unless they ask — keep the cognitive load low

Log the clarification topic in the Notes column. If multiple contacts ask about the same domain, this is a distribution intelligence signal — note it in the Day 2 reflection.

---

### Day 2 Evening Block (20:00 UTC or 21:30 UTC if checkpoint conflicts — 20 minutes)

- [ ] Update all tracking rows with current status
- [ ] Record cumulative Gist view counts
- [ ] Compute 48h preliminary rates: opens estimated (Bitly clicks), click rate, reply rate
- [ ] Complete May 19 Reflection in WAVE_1_MONITORING_DASHBOARD.md Section 6
- [ ] Log Day 2 status summary in DISTRIBUTION_EXECUTION_LOG.md
- [ ] Identify any preliminary Tier 2 candidates (even tentative) — add to Section 4 candidate list

**Day 2 expected state**: 0–1 replies (Elias or Bassin most likely first movers). Gist view counts should be 3–8 above baseline. Zero bounces. Reply rate of 0–20% at 48h is normal.

**48-hour contingency gate**: If reply rate is below 8% (zero replies) AND Bitly shows zero clicks AND no bounce notifications: this is unusual. Run the delivery self-test. See PHASE_1_CONTINGENCY_STRATEGY.md Trigger 1 for diagnosis sequence. Do not panic — this is recoverable.

**Day 2 total time**: 2–4 hours (monitoring, responses if any, evening block)

---

## May 20 — Closing and Analysis (2–3 hours total)

### Morning Check (10:00 UTC — 30 minutes)

- [ ] Check inbox for any overnight replies (48–72h window is the peak for policy org contacts)
- [ ] Update tracking sheet with any new signals
- [ ] Final Gist view count record for Day 3

---

### Analysis Block (14:00–17:00 UTC — 2 hours)

**48–72h Engagement Snapshot**

Compile this snapshot now. You need it for the May 25–28 adoption assessment.

- [ ] Total sent (should be 5)
- [ ] Delivered (confirmed non-bounced): [ ] / 5
- [ ] Replies received: [ ]
- [ ] Reply rate: [ ]% (target was 10–15%)
- [ ] Clicks (Bitly or Gist analytics): [ ]
- [ ] Click rate: [ ]% (target was 20%)
- [ ] Score breakdown: 0s [ ], 1s [ ], 2s [ ], 3s [ ], 4s [ ], 5s [ ]
- [ ] Average score: [ ] / 5
- [ ] Tier 2 candidates identified: [ ] (target: 3–5)

**Sector comparison**

- [ ] Law schools (Goodman, Chenoweth): replies: [ ], avg score: [ ]
- [ ] Policy orgs (Weiser, Bassin): replies: [ ], avg score: [ ]
- [ ] Immigration legal (Elias): replies: [ ], avg score: [ ]

Record whether law schools or policy orgs showed higher engagement in the 48–72h window. This informs which sector to prioritize in Batch 2 personalization.

---

### Batch 2 Prep Block (17:00–19:00 UTC — 1 hour)

Use engagement data from Batch 1 to sharpen Batch 2 personalization.

- [ ] Review Batch 2 contacts in execution/tier-1-contact-batches.md
- [ ] For each Batch 2 contact in the same sector as your highest-engagement Batch 1 contact: update their personalization hook to reflect the specific engagement signal ("Erica Chenoweth asked about the bandwidth depletion mechanism in Section 2 — I think you'd find the same connection relevant here")
- [ ] Identify whether any Batch 1 replies flagged a specific domain as particularly salient — use this to adjust Batch 2 subject line variants
- [ ] Prepare 5–10 Batch 2 email drafts for send window May 22–25

Note: Batch 2 preparation is not a Wave 1 deliverable — it is optional work. If you have no Batch 1 replies yet, Batch 2 personalization is premature. In that case, skip this block and focus on the summary and reflection.

---

### Summary for May 25 Assessment (19:00–20:00 UTC — 30 minutes)

Create a brief 2-page (or 400–600 word) summary covering:

1. Send and delivery summary (5 sent, X delivered, X bounced)
2. 48–72h engagement snapshot (reply rate, click rate, score distribution)
3. Top 3 signals (verbatim quotes or descriptions of the most significant replies or engagement indicators)
4. Sector breakdown (which sector showed strongest early response)
5. Tier 2 candidates identified (names, organizations, qualifying criteria)
6. Surprises (anything that contradicted expectations)
7. One recommendation for Wave 2 framing or sequencing based on the data

This summary is the primary input for the May 25–28 adoption assessment. Write it in plain prose, not bullet points — the assessment will use it to make decisions about Tier 2 activation, messaging pivots, and Wave 2 timing.

Save as a dated note in DISTRIBUTION_EXECUTION_LOG.md (heading: "Wave 1 Closing Summary — May 20, 2026").

---

### Day 3 Evening Block (20:00 UTC — 20 minutes)

- [ ] Final update to all tracking rows in WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv
- [ ] Complete May 20 Reflection in WAVE_1_MONITORING_DASHBOARD.md Section 6
- [ ] Log Day 3 status summary in DISTRIBUTION_EXECUTION_LOG.md
- [ ] Confirm Tier 2 candidate list is complete and documented in WAVE_1_MONITORING_DASHBOARD.md Section 4
- [ ] Review Wave 1 contingency status one final time — are there any open issues before the monitoring period extends to May 25?

**Day 3 expected state**: 1–2 replies total (Elias most likely; Weiser or Bassin possible). Click rate 15–25%. Reply rate 10–20% at 72h. 2–4 Tier 2 candidates identified. Zero unresolved bounces.

**Day 3 total time**: 2–3 hours (analysis, batch prep if applicable, summary, evening block)

---

## Time Investment Summary

| Day | Phase | Active time | Total window |
|-----|-------|-------------|-------------|
| May 18 | Pre-launch + send + monitoring | 3–4 hours | 6–8 hours |
| May 19 | Monitoring + responding | 1–2 hours | 2–4 hours |
| May 20 | Analysis + summary + prep | 2–3 hours | 2–3 hours |
| **Total** | | **6–9 hours active** | **10–15 hours** |

The difference between active and total time accounts for the send window (you are available but not actively working), async response waits, and the stockbot checkpoint on May 19.

---

## Contingency Quick Reference

If something goes wrong, use this table to find the pre-written response:

| Problem | Where to look |
|---------|--------------|
| Hard bounce — 1 contact | PHASE_1_WAVE1_EXECUTION_PREP.md Section 1, alternate addresses |
| Hard bounce — 3+ contacts | PHASE_1_LAUNCH_RISK_PLAYBOOK.md Section 1.3 — delivery failure protocol |
| Zero replies at 72h | PHASE_1_CONTINGENCY_STRATEGY.md Trigger 1 — delivery diagnosis sequence |
| Spam filter triggered | PHASE_1_LAUNCH_RISK_PLAYBOOK.md Section 1.3 — subject line variants |
| Contact opts out | WAVE_1_MONITORING_DASHBOARD.md Section 5 — decline protocol |
| Gist URL returns 404 | PHASE_1_LAUNCH_RISK_PLAYBOOK.md Section 1.1 — Gist recovery |
| Unexpected hostile reply | OBJECTION_HANDLING_FRAMEWORK.md |
| Reply requests something not in Gists | Create a domain extract (1–2 pages from the relevant domain file); send within 48h |

---

*Document prepared: May 17, 2026. Sources: PHASE_1_WAVE1_EXECUTION_PREP.md (May 15); WAVE_1_PRESTAGING_READINESS.md (May 15); PHASE_1_CONTINGENCY_STRATEGY.md; PHASE_1_LAUNCH_RISK_PLAYBOOK.md (May 6); PHASE_1_WAVE_1_EXECUTION_DASHBOARD.md (May 14); BATCH_1_CONTACT_LOG.md.*
