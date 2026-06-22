---
title: "Domain 48 — Distribution Execution Log (June 2026)"
created: "2026-06-22"
status: "in-progress"
wave_1_scheduled: "2026-06-16 to 2026-06-18"
wave_2_scheduled: "June 23-25 (contingent on T+7 signal)"
hard_deadline: "2026-07-15 (Virginia Right to Vote Coalition integration window)"
---

# Domain 48 — Distribution Execution Log (June 2026)

**Domain**: Criminal Justice / Civic Exclusion / Disenfranchisement Architecture
**Gist URL**: https://gist.github.com/esca8peArtist/00c1423e3da7bb4693fa285ec87f18a8
**Hard Deadline**: July 15, 2026 (Virginia Right to Vote Coalition integration deadline)

---

## Wave 1 — June 16-18, 2026 (STAGED)

**Status**: PENDING EXECUTION (scheduled June 16-18; overdue as of June 22)

### Wave 1 Sends — Tier A (Litigation Organizations)

| Contact | Email | Send Date | Send Time | Template | Confirmation |
|---------|-------|-----------|-----------|----------|--------------|
| Sentencing Project (Nicole D. Porter, Senior Director of Research) | nporter@sentencingproject.org | [ ] | [ ] | Template A, Sentencing Project variant (DOMAIN_48_EMAIL_TEMPLATE_SET.md) | [ ] |
| Prison Policy Initiative (Peter Wagner, Executive Director) | info@prisonpolicy.org | [ ] | [ ] | Template A, PPI variant | [ ] |

**Note**: Sentencing Project email should be sent 90 minutes before Prison Policy Initiative (same protocol as Domain 51).

---

## Wave 1 — Signal Assessment (June 23-25 T+7 Checkpoint)

### June 23 Morning Inbox Check

| Contact | Sent? (Y/N/date) | Reply received? (Y/N/date) | Signal (S/M/W/B/OOO/--) | Signal description |
|---------|-----------------|--------------------------|------------------------|-------------------|
| Sentencing Project | [ ] | [ ] | [ ] | |
| Prison Policy Initiative | [ ] | [ ] | [ ] | |

### T+7 Routing Decision (June 23)

**STRONG count from Wave 1**: _____ / 2

**Routing decision**:
- [ ] >= 1 STRONG: Activate Wave 2 Tier A (NAACP LDF + Fines & Fees Justice Center + ACLU VA) immediately. Flag Virginia July 15 deadline in all Wave 2 emails.
- [ ] 0 STRONG / >= 1 MODERATE: Activate NAACP LDF only. Hold Fines & Fees Justice Center and ACLU VA until June 30 (Day 14).
- [ ] 0 STRONG / 0 MODERATE: If Wave 1 sends were < 72 hours old at T+7 assessment: re-check June 25. If >= 72 hours old: run delivery diagnostic (verify Gist loads, test email, verify contact addresses).

**Action taken June 23**: [ ] Wave 2 activation sent / [ ] NAACP LDF only sent / [ ] Delivery diagnostic run

---

## Wave 1 — Supplementary Monitoring (June 23-25)

### June 24 Interim Check

| Contact | Any new reply since June 23 AM? | Updated signal | Notes |
|---------|----------------------------------|----------------|-------|
| Sentencing Project | [ ] | | |
| Prison Policy Initiative | [ ] | | |

### June 25 Final T+7 Check (if Wave 1 sent June 18)

| Contact | Any new reply since June 24? | Updated signal | Notes |
|---------|------------------------------|----------------|-------|
| Sentencing Project | [ ] | | |
| Prison Policy Initiative | [ ] | | |

---

## Wave 2 — June 23-25 (CONTINGENT ON T+7 SIGNAL)

**Status**: EXECUTION PENDING (triggered by June 23 T+7 routing decision)

### Wave 2 Sends — Tier B (Advocacy + Legal)

| Contact | Email | Send Date | Send Time | Template | Confirmation | T+7 Trigger |
|---------|-------|-----------|-----------|----------|--------------|-------------|
| NAACP Legal Defense Fund (LDF) | info@naacpldf.org | [ ] | [ ] | Template B variant (DOMAIN_48_EMAIL_TEMPLATE_SET.md) | [ ] | MODERATE or STRONG |
| Fines & Fees Justice Center | info@finesandfeesjusticecenter.org | [ ] | [ ] | Template C variant | [ ] | STRONG only |
| ACLU of Virginia | acluva@acluva.org | [ ] | [ ] | Template D variant | [ ] | STRONG only |

**Note**: If NAACP LDF sent June 23, this counts as Wave 2 send date. If Wave 2 full (all 3 orgs) sent June 23, ACLU VA and FFJI signal assessment window is June 30 (Day 7 from June 23 send).

### Virginia Right to Vote Coalition Integration Flag

**Critical**: All Wave 2 emails should include explicit flag: "The Virginia Right to Vote Coalition integration deadline is July 15 — this timeline is compressed and requires organizational uptake before the July 4 holiday window. We are flagging this opportunity urgently."

---

## Wave 2 — Signal Assessment (June 30 if Wave 2 sent June 23)

### June 30 Interim Check (Day 7 from Wave 2 if sent June 23)

| Contact | Reply received? | Reply date | Signal (S/M/W/B/OOO/--) | Signal description |
|---------|-----------------|------------|------------------------|-------------------|
| NAACP LDF | [ ] | | [ ] | |
| Fines & Fees Justice Center | [ ] | | [ ] | |
| ACLU of Virginia | [ ] | | [ ] | |

---

## Day 14 Checkpoint (June 30 for June 16-18 Wave 1 sends)

**Status**: PENDING (assess June 30)

**Decision**: If 0 STRONG after 14 days from Wave 1 send (June 16-18), activate Fines & Fees Justice Center and ACLU of Virginia regardless of signal strength. The Virginia July 15 integration window is too compressed to wait for STRONG signals.

| Contact | STRONG signal received? | Day 14 action |
|---------|------------------------|--------------|
| Sentencing Project | [ ] | |
| Prison Policy Initiative | [ ] | |
| NAACP LDF | [ ] | |
| FINES & FEES | [ ] | [ ] Activate regardless if 0 STRONG |
| ACLU VA | [ ] | [ ] Activate regardless if 0 STRONG |

---

## Contingency: No Replies (Delivery Diagnostic)

**If 0 replies by June 25 from both Wave 1 contacts**:

1. Load Gist URL (verify HTTP 200): https://gist.github.com/esca8peArtist/00c1423e3da7bb4693fa285ec87f18a8
   - [ ] Gist loads (HTTP 200)
   - [ ] Gist returns 404 — recreate using DOMAIN_48_GIST_CREATION_STEPS.md, resend

2. Send test email to yourself
   - [ ] Reaches inbox
   - [ ] Bounces to spam — adjust subject line, resend to 1 contact with plain text

3. Verify contact addresses on organization websites
   - [ ] nporter@sentencingproject.org verified on sentencingproject.org (date: _____)
   - [ ] info@prisonpolicy.org verified on prisonpolicy.org (date: _____)

4. Assessment
   - [ ] Delivery confirmed (email + Gist working) — recount on June 30
   - [ ] Delivery failed (Gist 404 or email bounced) — recreate and resend
   - [ ] Address mismatch — update and resend with correct address

**Diagnostic date**: ___________
**Findings**: ___________________________________________________
**Action taken**: [ ] Gist recreated / [ ] Test email sent / [ ] Addresses updated / [ ] Resend to 1 contact

---

## Post-Wave Monitoring

### Cross-Domain Signal Integration

Domain 48 (Criminal Justice) shares contact ecosystems with:
- **Domain 49** (Louisiana v. Callais / VRA redistricting) — NAACP LDF works both domains
- **Domain 51** (Campaign Finance) — if Domain 51 generates strong signal, this may warm up Domain 48 contacts through coalition activity

Monitor for cross-domain referrals (e.g., NAACP LDF saying "We're integrating this with our Callais work").

---

## Execution Timeline Summary

| Date | Event | Status | Owner |
|------|-------|--------|-------|
| June 16-18 | Wave 1 execution (Sentencing Project, PPI) | [ ] PENDING | User |
| June 23 AM | T+7 checkpoint — assess Wave 1 signals | [ ] PENDING | User |
| June 23 PM | Wave 2 activation (if triggered) — NAACP LDF ± others | [ ] PENDING | User |
| June 25 | Final T+7 check (if Wave 1 sent June 18) | [ ] PENDING | User |
| June 30 | Day 14 checkpoint — forced activation of FFJI + ACLU VA if 0 STRONG | [ ] PENDING | User |
| July 15 | Virginia Right to Vote Coalition integration deadline | [ ] MONITOR | -- |

---

## Notes & Metadata

### Contact Verification

- [ ] Sentencing Project — nporter@sentencingproject.org verified against sentencingproject.org/staff/ (date: _____)
- [ ] Prison Policy Initiative — info@prisonpolicy.org verified (date: _____)
- [ ] NAACP LDF — info@naacpldf.org verified (date: _____)
- [ ] Fines & Fees Justice Center — info@finesandfeesjusticecenter.org verified (date: _____)
- [ ] ACLU of Virginia — acluva@acluva.org verified (date: _____)

### Domain 48 Phase Sequencing

Wave 1 (Tier A, June 16-18) → T+7 checkpoint (June 23-25) → Wave 2 (Tier B, June 23-25 or Day 14) → July 15 deadline integration window

### Movement Integration

Domain 48 target audiences:
- Criminal justice reform (Sentencing Project, PPI, ACLU)
- Voting rights (NAACP LDF, ACLU)
- Economic justice (Fines & Fees Justice Center)
- State-level voter restoration (Virginia Right to Vote Coalition, state legislative races)

### Critical Deadline

July 15, 2026: Virginia Right to Vote Coalition must have integrated Domain 48 research into their legislative/electoral plans. This requires organizational uptake 7-10 days before deadline. Do not send Wave 2 after July 5.

---

## Log & Sign-Off

**Session created**: 3911 (June 22, 2026)
**Last updated**: [to be filled in as execution proceeds]
**Wave 1 execution**: [ ]
**T+7 checkpoint complete**: [ ]
**Wave 2 execution complete**: [ ]
**Day 14 checkpoint complete**: [ ]

---

*Prepared June 22, 2026. Use this log to track all Domain 48 distribution activity June-July. Wave 1 (June 16-18) STAGED and ready for user execution. T+7 checkpoint (June 23-25) determines Wave 2 activation. July 15 deadline is hard (Virginia Right to Vote Coalition integration). Update this log daily as sends execute and signals arrive.*
