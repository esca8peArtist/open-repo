---
title: "Phase 1 Block 5 — Send Checklist"
created: 2026-05-14
status: ready-to-execute
purpose: "Final gate checklist and send sequence log for all 5 Batch 1 emails"
time_estimate: "15-20 minutes (plus 2-hour stagger window)"
dependency: "Blocks 2, 3, 4 all complete; all 5 emails staged in email client"
---

# Phase 1 Block 5 — Send Checklist

**What this block is**: The final gate before sending. Confirm all prior blocks are done, run the final pre-flight checks, then execute the send sequence in order.

---

## Final Gate Checklist (Must Pass Before First Send)

Run through these before sending email 1. If any item is unchecked, do not send until it is resolved.

**Block 2 complete**:
- [ ] All link placeholders replaced in distribution-institutional-outreach-templates.md
- [ ] All link placeholders replaced in distribution-substack-drafts.md
- [ ] All link placeholders replaced in distribution-reddit-templates.md
- [ ] URL placeholders replaced in PHASE_1_EMAIL_TEMPLATES.md

**Block 3 complete**:
- [ ] All 5 contact email addresses verified and recorded in PHASE_1_BLOCK_3_CONTACT_VERIFICATION.md

**Block 4 complete (all 5 email drafts ready)**:
- [ ] Goodman email: all placeholders filled, one subject line selected, one path paragraph selected, email staged in client
- [ ] Weiser email: all placeholders filled, one subject line selected, one path paragraph selected, email staged in client
- [ ] Chenoweth email: all placeholders filled, one subject line selected, one path paragraph selected, email staged in client
- [ ] Bassin email: all placeholders filled, one subject line selected, one path paragraph selected, availability windows filled, email staged in client
- [ ] Elias email: all placeholders filled, one subject line selected, one path paragraph selected, case statuses updated if needed, email staged in client

**Final sweep (each email, before sending)**:
- [ ] Search each draft for `{{` or `[` — any remaining placeholder means the email is not ready
- [ ] Recipient email address in To: field matches verified address from Block 3
- [ ] No attachments accidentally included (these are link-based emails, not attachment-based)
- [ ] Subject line is the one you selected — not "Option A / B / C" header text

All items above checked? Proceed to send sequence.

---

## Send Sequence and Timing

**Send order**: Weiser first, then Elias, then Goodman, then Chenoweth, then Bassin.

Wait — this is the override from the user's task instructions. The standard order in BATCH_1_CONTACT_LOG.md is Goodman first. The override order specified for this execution is:

**OVERRIDE SEND ORDER: Weiser → Elias → Goodman → Chenoweth → Bassin**

Reason for override: Weiser (May 30 advocacy window — 16 days from May 14) and Elias (May 30 DOJ consent decree window; NVRA August 7 window) have the most time-sensitive advocacy windows. Getting them into the queue earliest maximizes the probability of response before the first domain 37 window closes.

| Order | Contact | Email | Send Time | Time Gap |
|-------|---------|-------|-----------|----------|
| 1st | Wendy Weiser | wweiser@brennancenter.org | T+0:00 | — |
| 2nd | Marc Elias | melias@perkinscoie.com | T+0:30 | 30 min after Weiser |
| 3rd | Ryan Goodman | ryan.goodman@nyu.edu | T+1:00 | 30 min after Elias |
| 4th | Erica Chenoweth | echenoweth@hks.harvard.edu | T+1:30 | 30 min after Goodman |
| 5th | Ian Bassin | ian@protectdemocracy.org | T+2:00 | 30 min after Chenoweth |

Total elapsed time for all 5 sends: 2 hours from first send to last send.

---

## Send Log (Fill In During Execution)

| # | Contact | Sent Date | Sent Time | Delivery Confirmation | Notes |
|---|---------|-----------|-----------|----------------------|-------|
| 1 | Wendy Weiser | | | | |
| 2 | Marc Elias | | | | |
| 3 | Ryan Goodman | | | | |
| 4 | Erica Chenoweth | | | | |
| 5 | Ian Bassin | | | | |

After each send: record the time in the log above. This log is also referenced in BATCH_1_CONTACT_LOG.md — copy the send dates and times there after all 5 are sent.

---

## If an Email Bounces

**Goodman**: Try ryan@justsecurity.org as alternate
**Weiser**: Confirm spelling at brennancenter.org and retry; if bounced again, contact via Brennan Center general contact form
**Chenoweth**: Try echenoweth@harvard.edu (without the hks subdomain) as alternate
**Bassin**: Try a@protectdemocracy.org (for admin routing) — or check protectdemocracy.org/contact
**Elias**: Try marc@democracydocket.com as alternate

If any bounce cannot be resolved: log the contact as "undeliverable — Batch 2 reattempt" in the send log, and continue with the remaining emails. Do not delay the sequence for a single bounce.

---

## Timing Guidance

**Best days to send**: Tuesday, Wednesday, or Thursday  
**Best time window**: 9:00 AM - 12:00 PM ET (before the contact's inbox fills with afternoon volume)  
**Worst days**: Monday (inbox recovery from weekend), Friday (pre-weekend disengagement)  
**Avoid**: Any day with a major news event that would dominate your contacts' attention

If you are sending on May 15-17 (optimal window per execution plan), that is Thursday-Saturday. Thursday May 15 is ideal. Saturday May 17 is marginal — if you must send Saturday, be aware response rate is typically lower.

---

## Post-Send Actions (Within 2 Hours of Last Email)

- [ ] Copy send dates and times from the log above into BATCH_1_CONTACT_LOG.md (the table under "Contact Verification & Log")
- [ ] Set a calendar reminder for T+7 (7 days from first send) to assess response rate — target is 2 of 5 respond substantively
- [ ] Set a calendar reminder for T+14 to prepare Batch 2 (if Batch 1 hits the 2-of-5 target, proceed with Batch 2; if below target, reassess before sending more)
- [ ] Stage Substack and Reddit posts for T+2 to T+3 (see distribution-substack-drafts.md and distribution-reddit-templates.md)

---

## What Success Looks Like

**Strong outcome (Batch 1 goals)**:
- 2 of 5 respond substantively within 14 days
- 1 of 5 mentions the research to a colleague
- 1 response includes a specific correction or question — this is the most valuable signal

**Adequate outcome**:
- 1 of 5 responds substantively
- No bounces
- Proceed to Batch 2 with revised framing

**Investigate if**:
- 0 of 5 respond after 14 days — check email delivery logs; consider whether subject lines need adjustment for Batch 2; consider whether the research/framing needs refinement
- 2+ emails bounce — verify the institutional email formats; update BATCH_1_CONTACT_LOG.md accordingly

---

**Block 5 complete when**: All 5 emails sent, log filled in, reminders set.

---

*Reference: BATCH_1_CONTACT_LOG.md (response tracking), PHASE_1_EXECUTION_CHECKLIST.md Block 6, distribution-timeline.md (Week 1 sequencing)*
