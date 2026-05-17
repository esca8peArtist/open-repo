# Wave 1 Contingency Activation Playbook

**Created**: May 17, 2026 — Orchestrator Session 1151  
**For use**: May 18 12:00 UTC onward, if Wave 1 underperforms  
**Source documents**: PHASE_1_POST_WAVE1_CONTINGENCY.md (all variants); WAVE_1_PREFLIGHT_AND_PATH_DECISION.md  
**Status**: Executable — activate only when a threshold in Section 1 is confirmed breached

---

## Part 1: When to Activate

Do NOT activate based on anxiety or slow early response. Academic and policy contacts reply on 2–10 day cycles. Activate only when a specific threshold below is confirmed breached.

### Activation Thresholds

**May 18 12:00 UTC (2-hour post-send check — delivery only, not response):**

Activate same-day triage if:
- Fewer than 5 Batch 1 sends appear in your sent folder (send failure)
- 2 or more hard bounces received within 30 minutes of send
- Domain 37 Gist returns 404 (test: open in incognito browser)
- Spam warnings or account flags from your email provider

If none of the above: no action needed. Pre-select your most likely contingency variant and bookmark its section below. Wait for May 21 10:00 UTC.

**May 21 10:00 UTC (72-hour final assessment — responses and engagement):**

| Tier 1 replies | Domain 37 replies | Verdict | Activate |
|----------------|-------------------|---------|---------|
| 2+ substantive | 1+ | SUCCESS | Nothing — proceed to Tier 2 |
| 1 substantive | 1+ | Acceptable | A2 retarget + Tier 2 on schedule |
| 1 ack-only | Any | Borderline | A2 retarget + hold Tier 2 48h |
| 0, delivery confirmed | 1+ | Tier 1 silent | A3 only |
| 0, delivery confirmed | 0 | Both tracks silent | A3 + B3 parallel |
| 0, delivery suspected failure | Any | Delivery failure | A1 first |
| All channels silent | — | Full underperformance | Escalate to user for A4 |

---

## Part 2: The 2-Gate Decision Tree

### Gate 1 — May 18 12:00 UTC (Pre-Select)

Run this within 2 hours of completing Wave 1 sends:

1. Are all 5 Batch 1 sends in your sent folder? NO: debug send first, do not start contingency clock.
2. Hard bounces of 2 or more? YES: pre-select **Variant A1**.
3. Domain 37 Gist live (test in incognito)? NO: pre-select **Variant B2**.
4. Any spam flags or account warnings? YES: pause, diagnose before any further sends.
5. No issues: pre-select whichever variant matches your read of early signals. Bookmark it. Wait for May 21.

The May 18 12:00 UTC gate is NOT for measuring response — it is for catching delivery failures before they compound.

### Gate 2 — May 21 10:00 UTC (Activate or Stand Down)

Use the threshold table above. Confirm your pre-selected variant against the actual 72h data. Activate by end of May 21. All variants except A4 are within orchestrator authority to execute without user decision.

---

## Part 3: Step-by-Step Activation for Each Variant

### Variant A1 — Expanded Contact Pool (Delivery Failure)

**Trigger**: 2+ hard bounces, or 0 replies with suspected delivery failure.  
**Activate by**: Same day as discovery (May 18 if immediate bounces, or May 21 if suspected).  
**Time to execute**: 2 hours.

Steps:
- [ ] Check each bounced address against the alternate addresses below
- [ ] Resend to alternates using revised subject lines (PHASE_1_CONTINGENCY_STRATEGY.md Section 3.1 — drop any advocacy language from original subject)
  - Goodman: ryan@justsecurity.org
  - Weiser: brennancenter.org/contact (web form)
  - Chenoweth: hks.harvard.edu faculty contact form
  - Bassin: protectdemocracy.org contact form
  - Elias: marc@democracydocket.com
- [ ] Add 3 high-confidence alternates to the cohort: Richard Hasen (hasen@law.ucla.edu), Damon T. Hewitt (dhewitt@lawyerscommittee.org), Virginia Kase Solomón (commoncause.org/contact)
- [ ] Reset 72h monitoring window from resend time
- [ ] Log: "Variant A1 activated [time] — [bounced contacts]. Resent to alternates. New 72h window closes [date+time]."

Success marker: 1+ substantive reply from the expanded 8-contact cohort within new 72h window.

---

### Variant A2 — Retarget with Narrowed Pitch (Low Engagement)

**Trigger**: 1 substantive reply (20% rate), or 1 acknowledgment-only reply at 72h.  
**Activate by**: May 21 (same day as 72h assessment).  
**Time to execute**: 90 minutes.

Steps:
- [ ] For each non-responding Tier 1 contact, identify the single most time-sensitive hook (table below)
  - Goodman: April 21 SPLC indictment charging defects — is Just Security covering it?
  - Weiser: SAVE Act 81% false positive rate — ask her Senate defector bloc interpretation
  - Chenoweth: 3.5% threshold question — is U.S. closer to Poland or Hungary on reversibility?
  - Bassin: DOJ enforcement gap litigation theory — one specific question
  - Elias: August 7 NVRA quiet-period — 90-day window, pre-filing strategy question
- [ ] Draft one email per non-responding contact using the A2 template: 150 words maximum, one Gist URL only, one direct question
- [ ] Subject line: "[First name] — one question on [specific topic]" — no advocacy language
- [ ] Send A2 retargets May 21 afternoon, staggered 15 min apart
- [ ] Launch Tier 2 on May 23 as scheduled — do NOT delay Tier 2 for A2 results
- [ ] Log: "Variant A2 activated May 21 — retargeting [N] contacts with narrowed hooks."

Success marker: Any additional substantive reply from the retarget cohort.

---

### Variant A3 — Parallel Tier 2 + Tier 3 Launch (Zero Engagement, Confirmed Delivery)

**Trigger**: Zero replies at 72h, confirmed delivery (no bounces, no spam signals).  
**Activate by**: May 21 12:00 UTC.  
**Time to execute**: 3-4 hours Day 1; 45 min Day 2 (SSRN); Day 3 Tier 3 prep.

Steps:
- [ ] Pull the 10 A3 priority Tier 2 contacts (PHASE_1_CONTINGENCY_STRATEGY.md Section 4) in this priority order: Democracy Alliance, NAACP LDF, Lawyers' Committee, Indivisible, Richard Hasen, Color of Change, UnidosUS, Erwin Chemerinsky, Jack Balkin, Michael Waldman
- [ ] Personalize each email with standalone data hook (no credibility anchors — do not reference Tier 1 contacts). Lead with the single most time-sensitive finding for each contact's sector
- [ ] Send all 10 contacts May 21–22
- [ ] Submit to SSRN on May 22 (45 min — procedure at PHASE_1_CONTINGENCY_STRATEGY.md Section 5.1). This creates a citable URL discoverable independently of email
- [ ] Begin Tier 3 preparation May 22–24; target May 25 send (4 days early). Priority sectors: Colorado AG, Michigan AG, Arizona AG offices + state NVRA contacts
- [ ] Log: "Variant A3 activated May 21 — 10 Tier 2 contacts, SSRN submission, Tier 3 accelerated to May 25."

Success marker: 2+ substantive Tier 2 replies by May 25. Pipeline is 5 days behind but recovering.

---

### Variant A4 — Pivot to Path B / Discovery-First (Full Underperformance)

**Trigger**: All tiers silent at 72h confirmed delivery AND Tier 2 under A3 also produces 1 or fewer replies by May 25.  
**REQUIRES USER DECISION — do not activate autonomously.**  
**Activate by**: User decision required before end of May 26.

Steps (only after user approves):
- [ ] Suspend all contact-focused outreach for 2 weeks
- [ ] Set up Substack publication per published/substack-posts/ infrastructure (already built)
- [ ] Submit to SSRN (45 min, if not already done under A3)
- [ ] Archive Domain 37 specialized election-org templates to "Phase 2 August window" folder (do not delete)
- [ ] Plan email outreach as follow-up to Substack/SSRN discovery, not as primary channel
- [ ] Target relaunch date: no earlier than June 4

Do not present A4 to user as a failure. Frame as: "Email-first yielded X results. Discovery-first is the standard academic pathway and often produces higher-quality engagement. Recommend 2-week pivot with relaunch June 4."

Success marker: SSRN indexed within 72h; first independent discovery engagement by June 11.

---

### Variant B1 — Revert to Pure Path A (Domain 37 Track Fails with No Return)

**Trigger**: Domain 37 hybrid produces zero engagement AND is consuming time without return.  
**Activate by**: May 21, after 48h of Domain 37 sends.  
**Time to execute**: 30 minutes.

Steps:
- [ ] Cancel any remaining Domain 37 specialized sends not yet sent
- [ ] Archive Domain 37 specialized templates to "Phase 2 August window" folder (do not delete — August 7 NVRA window is a second opportunity)
- [ ] Add Domain 37 Gist URL to the standard Tier 2 template as one resource among the 8, with no special treatment
- [ ] Log: "Domain 37 hybrid discontinued [date] — content folded into general Tier 2 distribution."

Success marker: Tier 2 general outreach proceeds without disruption. Domain 37 content reaches broader audience through standard pipeline.

---

### Variant B2 — Troubleshoot Domain 37 Technical Issue

**Trigger**: Gist 404, template error, wrong contact list used, or zero click signals on Domain 37 Gist within 48h.  
**Activate by**: Within 4 hours of detecting the issue.  
**Time to execute**: 1–2 hours.

Steps:
- [ ] Open Domain 37 Gist in incognito: https://gist.github.com/esca8peArtist/1277f5d5bcb0fe46604bbaba8fa37fd0
  - If 404: re-create Gist from source at `domains/domain-37-federal-executive-interference-2026-midterms.md` (see PHASE_1_LAUNCH_RISK_PLAYBOOK.md Section 1.1)
  - If loads: Gist is live — problem is elsewhere
- [ ] Check Domain 37 email template: all placeholders filled? Correct org type in "To" field? Correct messaging variant?
- [ ] Check click data: zero views at 48h means delivery or open failure. Views but no replies means content did not convert — consider B3 instead
- [ ] Verify each election-org contact is still in their listed role (staff turnover is frequent)
- [ ] Resend corrected emails with apology line if original was visibly broken: "Resending — the original email had a formatting issue with the Domain 37 link. Corrected version below."
- [ ] Reset 48h monitoring window from corrected send
- [ ] Log: "Variant B2 activated [time] — issue: [description]. Fix: [description]. Resent to [N] contacts."

Success marker: Domain 37 Gist shows click activity within 24h of corrected resend; 1+ reply within 48h.

---

### Variant B3 — Repurpose Domain 37 Assets for Tier 2 (Clicks But No Replies)

**Trigger**: Domain 37 sends confirmed delivered (clicks recorded), but zero substantive replies from 12 specialized election-protection orgs.  
**Activate by**: May 22, after 72h of Domain 37 sends.  
**Time to execute**: 75 minutes.

Steps:
- [ ] Accept that the specialized election-org track is closed for this window
- [ ] Do not use the specialized election-org template for remaining sends
- [ ] Send Domain 37 as the specific entry point to these Tier 2 contacts (front-load from Tier 2 wave):
  - Richard Hasen, UCLA Law (hasen@law.ucla.edu) — NVRA quiet period, SAVE Act false positive rate
  - Nicholas Stephanopoulos, Harvard Law — gerrymandering + redistricting cascade
  - Heather Gerken, Yale Law Dean — federalism framing of HSGP conditionality
  - Kris Mayes's office, Arizona AG — SAVE Act implementation, NVRA Section 7 enforcement
  - Dana Nessel's office, Michigan AG — SAVE Act 81% false positive impact on Michigan voter rolls
  - Josh Kaul's office, Wisconsin AG — Domain 37 DOJ voter roll cases in 7th Circuit
  - Senate Rules Minority Staff (Sen. Klobuchar) — Domains 1, 2, 3 electoral reform
- [ ] Use law school or state AG sector templates (not specialized election-org template)
- [ ] Send May 22–23 on Tier 2 wave schedule — these contacts were in Tier 2 anyway
- [ ] Log: "Variant B3 activated May 22 — Domain 37 assets repurposed for law school and state AG Tier 2."

Success marker: Domain 37 content reaches law school and state AG audiences. May 30 DOJ window still accessible to state AGs via B3 even without specialized election-org engagement.

---

## Part 4: Quick Reference (Cut Out and Keep)

**May 18 10:00–12:00 UTC — Gate 1 (delivery check):**
1. All 5 sends confirmed in sent folder? NO: debug first.
2. 2+ bounces? YES: pre-select A1.
3. Domain 37 Gist live in incognito? NO: pre-select B2.
4. No issues: pre-select likely variant, bookmark playbook section above, wait.

**May 21 10:00 UTC — Gate 2 (72h assessment):**
- 2+ substantive replies: SUCCESS — standard Tier 2 launch May 23.
- 1 reply: A2 retarget + Tier 2 May 23 as scheduled.
- 0 replies, delivery confirmed: A3 immediately (and B3 if D37 also silent).
- 0 replies, delivery failure suspected: A1 first.
- Everything silent confirmed delivery: Escalate to user for A4 decision.

**What requires user decision**: Only A4 (full pivot). All others are within execution authority.

**What to log after each action**: Variant activated, contacts sent to, timestamp, new monitoring window, next check-in point.

---

*Sources: PHASE_1_POST_WAVE1_CONTINGENCY.md (Sections 1–8), WAVE_1_PREFLIGHT_AND_PATH_DECISION.md*  
*Confidence: 92% (per source document's own assessment). Single gap: if all 42 secondary contacts also produce zero engagement, a full diagnostic reset is required per PHASE_1_CONTINGENCY_STRATEGY.md Section 10.*
