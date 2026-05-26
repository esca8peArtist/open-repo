---
title: "Domain 56 May 27 Pre-Testing Checklist"
created: 2026-05-26
status: PRODUCTION-READY — execute May 27 evening before May 28 send
distribution_target: May 28, 08:00 UTC (Domain 56 Tier 2)
scope: Operational readiness verification for May 27 evening
---

# Domain 56 May 27 Pre-Testing Checklist
## Pre-Distribution Verification — Evening of May 27, 2026

**Purpose**: Complete this checklist on May 27 evening (approximately 45 minutes). If all items check green, you are cleared for May 28 distribution. If any item fails, the fix procedure is documented inline.

**Total time**: 45 minutes if no blockers are hit.

---

## SECTION 1: Monitoring Infrastructure Health

Verify all three monitoring files are present, non-corrupted, and correctly linked before sending anything.

### 1.1 Reply Triage Framework

**File**: `projects/resistance-research/reply-triage-framework.md`

- [ ] File opens and is readable (not corrupted, not empty)
- [ ] Five scoring categories present: Score 5 (Implementation Signal), Score 4 (Partnership), Score 3 (Substantive/Question), Score 2 (Acknowledgment), Score 0 (Opt-out)
- [ ] Escalation thresholds table present (Score 5 = notify within 24h, Score 4 = notify within 24h)
- [ ] Quick-reference scoring decision tree present (the flowchart block starting "Read the reply")
- [ ] Weekly synthesis summary template present (the "Reply Scoring Summary (Week of...)" block)

**PASS if**: All five bullets checked. No action needed — proceed.
**FAIL if**: File missing or any section absent. Fix: the file was created May 26 and committed to master. Run `git log projects/resistance-research/reply-triage-framework.md` to confirm. If absent, re-run the monitoring infrastructure session.

### 1.2 Day 7/14/30 Decision Trees

**File**: `projects/resistance-research/day-7-14-30-decision-trees.md`

- [ ] File opens and is readable
- [ ] Day 7 tree present with four terminal branches: HOLD, MONITOR, ESCALATE, CONTACT_VERIFY
- [ ] Day 14 micro-checkpoint tree present with three terminal branches: HOLD (escalate from MONITOR), CONTINUE_MONITOR, FAILURE_IMMINENT
- [ ] Day 30 tree present with five terminal determinations: FAILURE, STRONG, MODERATE, WEAK, ASSESS
- [ ] Day 30 check order documented: FAILURE first, then STRONG, MODERATE, WEAK, ASSESS
- [ ] Pre-Day-30 rapid-response section present (Score 5 and Score 4 cluster triggers)
- [ ] Quick reference table present (Checkpoint / Date / Decision Options columns)
- [ ] All branches terminate in a named action — no dead ends. Spot-check: does FAILURE branch include "User decision required within 48 hours"? Does STRONG include "Launch Domain 39 by end of Day 1"? Does WEAK include all three Modifications?

**Dead-end audit** (fast): scan for any branch ending without an explicit named action:
- Day 7 HOLD branch: "Proceed to normal Phase 1 trajectory" -- terminal, named. PASS.
- Day 7 ESCALATE branch: "Within 24 hours: 1... 2... 3..." -- terminal, named. PASS.
- Day 30 FAILURE: "Update CHECKIN.md... Present three options... User selects within 48h" -- terminal, named. PASS.
- Day 30 STRONG: Five numbered immediate actions. PASS.
- Day 30 MODERATE: Five numbered actions. PASS.
- Day 30 WEAK: Three modifications with by-Day deadlines. PASS.
- Day 30 ASSESS: "Send Domain 39 only... Continue Phase 1... Wait for Day 60" -- terminal, named. PASS.

**PASS if**: All bullets above checked, dead-end audit clear.
**FAIL if**: Any branch has no terminal action. Fix: document the dead end and escalate to CHECKIN.md before proceeding.

### 1.3 Phase 1 Wave 1 Monitoring Dashboard

**File**: `projects/resistance-research/PHASE_1_WAVE_1_MONITORING_DASHBOARD.md`

- [ ] File opens and is readable
- [ ] Dashboard setup section present (Google Sheets creation steps, six sheet names)
- [ ] Six sheet specifications present: Contacts, Gist Views, Network Map, Adoptions, Constituencies, Weekly Synthesis
- [ ] Weekly operations protocol present (15-20 minutes per Monday)
- [ ] Day 7 checkpoint date confirmed as June 4-5 (7 days from May 28 send)
- [ ] Day 30 checkpoint date confirmed as June 27-28
- [ ] Companion file references are resolvable: `reply-triage-framework.md`, `day-7-14-30-decision-trees.md`, `PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md` — all three exist in the directory

**PASS if**: All bullets checked.
**FAIL if**: Setup section missing, or companion file references point to non-existent files. Fix: verify using `ls projects/resistance-research/` to confirm all three companion files exist.

**Infrastructure health verdict**: If all three sections above pass, write "MONITORING INFRASTRUCTURE: GREEN" in your send-day log.

---

## SECTION 2: Contact Verification

Verify all four Tier 2 contacts are accurate and the correct contact method for each is noted.

**Source of truth**: `projects/resistance-research/DOMAIN_56_TIER2_READINESS_MAY22.md` Section 3 (verified May 22, 2026)

### Contact Table

| # | Organization | Email / Method | Template | Last Verified |
|---|---|---|---|---|
| 6 | Volcker Alliance | volcker@volckeralliance.org (direct email) | Template 1 | May 22, 2026 |
| 7 | Democracy Forward | info@democracyforward.org (direct email) | Template 4 | May 22, 2026 |
| 8 | CREW | citizensforethics.org/contact (web form) | Template 4 | May 22, 2026 |
| 9 | Government Executive | editors@govexec.com (direct email) | Template 3 (op-ed pitch) | May 22, 2026 |

### Per-Contact Verification Steps

**Volcker Alliance** (volcker@volckeralliance.org):
- [ ] Visit https://volckeralliance.org — confirm site is live and organization is active
- [ ] No email format change suspected (nonprofit direct email, stable format)
- [ ] Template 1 in `execution/domain-56-email-template.md` (lines 20-52) is the correct template

**Democracy Forward** (info@democracyforward.org):
- [ ] Visit https://democracyforward.org — confirm organization is still active as of May 2026
- [ ] PEER v. Trump litigation (N.D. Cal.) is still active and Democracy Forward remains a plaintiff — confirms the litigation hook in the email is current
- [ ] Template 4 in `execution/domain-56-email-template.md` (lines 116-143) with the Democracy Forward paragraph is the correct template

**CREW** (citizensforethics.org/contact):
- [ ] Visit https://www.citizensforethics.org/contact/ — confirm contact form is still live and functional
- [ ] Test: can you reach the form page without authentication? (Should be public)
- [ ] Template 4 (CREW paragraph, lines 134-136) is the correct template — the Hungary/Poland case studies paragraph

**Government Executive** (editors@govexec.com):
- [ ] Visit https://www.govexec.com — confirm publication is still active
- [ ] Template 3 (op-ed pitch format, lines 82-113) is the correct template
- [ ] Note: this send is different in format — it is an op-ed pitch, not a standard research submission. Confirm you are comfortable with the op-ed pitch framing before sending.

**Verification verdict**: If all four contacts are confirmed reachable, write "CONTACTS: GREEN" in your send-day log. If any contact fails:
- Volcker Alliance bounce: Use contact form at volckeralliance.org/contact as fallback
- Democracy Forward bounce: Use contact form at democracyforward.org/contact as fallback
- CREW form down: Use any staff email found on their team page as fallback
- Government Executive bounce: Try senior editors directly (names listed on govexec.com/about/staff)

---

## SECTION 3: Template Audit

Verify all four email templates are complete, properly formatted, and that user placeholders are identified.

**Template source**: `projects/resistance-research/execution/domain-56-email-template.md`

### Gist URL Verification (applies to all templates)

**Domain 56 Gist URL**: `https://gist.github.com/esca8peArtist/8f11e868397921a4e6556b41196d1b1f`

- [ ] Open the URL in an incognito browser window — confirm the page loads without authentication
- [ ] Confirm the title reads "Domain 56: Civil Service Politicization and the Destruction of Nonpartisan Governance Architecture" (or similar)
- [ ] Confirm the document body is visible and renders in markdown — check that at least the section headers are visible
- [ ] Confirm the Gist URL is already pre-filled in all four templates (the URL appears in the template body, not as a placeholder)

If the Gist URL returns 404: check `projects/resistance-research/DISTRIBUTION_GIST_URLS.md` for the current URL. The Domain 56 Gist was created May 22, 2026 and confirmed live in `DOMAIN_56_TIER2_READINESS_MAY22.md`.

### Template 1 (Volcker Alliance) Audit

**Location**: `execution/domain-56-email-template.md` lines 20-52
**Recipient**: Volcker Alliance — volcker@volckeralliance.org

- [ ] Subject line present: "New democratic-design analysis of Schedule Policy/Career — different frame from employee-rights approach [H.R. 492 window]"
- [ ] Call-to-action present: Offer to "discuss the analysis, provide an adapted version suited to your publication standards, or connect on the H.R. 492 legislative strategy"
- [ ] Gist URL pre-filled: `https://gist.github.com/esca8peArtist/8f11e868397921a4e6556b41196d1b1f`
- [ ] User placeholders identified: `[YOUR_NAME]` (line ~49) and `[YOUR_CONTACT_INFO]` (line ~50) — these are the only fields requiring user input
- [ ] Five pathways listed in the body (Schedule Policy/Career reclassification; DOGE workforce reduction; MSPB/OSC hollowing; enforcement agency collapse; whistleblower protection elimination)
- [ ] German Berufsbeamtentum reference present (Template 1 serves civil service reform organizations; this is the Volcker-specific hook)
- [ ] H.R. 492 / Saving the Civil Service Act referenced with June 1-30 legislative window

### Template 2 (Federal Unions — not in Tier 2 but verify for record completeness)

**Status**: Template 2 is for AFGE, NTEU, NFFE. These are Tier 1 contacts (already sent May 18-26). Not applicable for May 28 Tier 2 sends. Skip.

### Template 3 (Government Executive) Audit

**Location**: `execution/domain-56-email-template.md` lines 82-113
**Recipient**: Government Executive — editors@govexec.com

- [ ] Subject line: "New democratic-design framing for Schedule Policy/Career — academic analysis, 47 citations"
- [ ] Format note confirmed: Template 3 is addressed to HR policy/academic audience. The DOMAIN_56_TIER2_SEND_GUIDE.md uses a separate op-ed pitch format for Government Executive (not raw Template 3) — confirm you are using the op-ed pitch format from DOMAIN_56_TIER2_SEND_GUIDE.md Section "Send 4: Government Executive," not raw Template 3
- [ ] Op-ed pitch format includes: headline, lead fact, angle, key points, author credentials, word count, Gist link
- [ ] Gist URL present: `https://gist.github.com/esca8peArtist/8f11e868397921a4e6556b41196d1b1f`
- [ ] User placeholders: `[YOUR_NAME]` and `[YOUR_CONTACT_INFO]` at the closing — these are the only fields requiring user input
- [ ] Tone is editorial/publication-focused (not advocacy): "I'm pitching a guest op-ed or analysis piece"

### Template 4 (Democracy Forward and CREW) Audit

**Location**: `execution/domain-56-email-template.md` lines 116-143
**Recipients**: Democracy Forward and CREW (both use Template 4 with different recipient-specific paragraphs)

- [ ] Subject line: "Domain 56 analysis: five-pathway civil service capture architecture — democratic-design argument and litigation support"
- [ ] Three recipient-specific sections present in the template body:
  - For GAP: Section 7 whistleblower architecture (lines ~132-133)
  - For Protect Democracy / CREW: Hungary/Poland case studies, V-Dem "electoral autocracy" classification (lines ~134-136)
  - For Democracy Forward: PEER v. Trump APA argument, Loper Bright statutory authority argument (lines ~137-138)
- [ ] Confirm: before sending to Democracy Forward, you are using the Democracy Forward paragraph (not the CREW paragraph)
- [ ] Confirm: before sending to CREW, you are using the CREW paragraph (not the Democracy Forward paragraph)
- [ ] Gist URL pre-filled: `https://gist.github.com/esca8peArtist/8f11e868397921a4e6556b41196d1b1f`
- [ ] User placeholders: `[YOUR_NAME]` (line ~141) and `[YOUR_CONTACT_INFO]` (line ~142)
- [ ] Call-to-action for Democracy Forward: litigation support framing (PEER v. Trump)
- [ ] Call-to-action for CREW: accountability framing (Hungary/Poland / FAQ extension)

### User Placeholder Summary (complete this before any send)

These fields appear across all templates and must be filled by the user. They cannot be pre-filled by the agent.

| Placeholder | Where it appears | What to fill |
|---|---|---|
| `[YOUR_NAME]` | All templates (approximately 8 total occurrences) | Your real name |
| `[YOUR_CONTACT_INFO]` | All templates (approximately 8 total occurrences) | Your email address |

**No other placeholders require filling.** The Gist URL is pre-filled. The recipient-specific paragraphs are pre-written (just verify you select the correct one per recipient).

**Template audit verdict**: If all four templates pass, write "TEMPLATES: GREEN" in your send-day log. Note any placeholders still unfilled.

---

## SECTION 4: Gist Staging Verification

**Domain 56 Gist** (confirmed live):
- URL: `https://gist.github.com/esca8peArtist/8f11e868397921a4e6556b41196d1b1f`
- Status: LIVE as of May 22, 2026 (verified in `DOMAIN_56_TIER2_READINESS_MAY22.md`)

**Verification test** (perform May 27 evening):
- [ ] Open `https://gist.github.com/esca8peArtist/8f11e868397921a4e6556b41196d1b1f` in an incognito browser (not logged in to GitHub)
- [ ] Page loads — no 404, no login prompt
- [ ] Document title visible
- [ ] Section headers visible (confirms markdown rendering)
- [ ] At least one external URL in the citations is clickable

**If Gist returns 404**:
1. Check `projects/resistance-research/DISTRIBUTION_GIST_URLS.md` — the Domain 56 row has the canonical URL
2. If the URL is the same and still 404, the Gist may have been deleted
3. To recreate: follow `execution/domain-56-gist-creation-steps.md`
4. Update the URL in all template files before sending

**Domain 39 Gist** (required for June 1 send — verify now while you are doing Gist checks):
- URL: `https://gist.github.com/esca8peArtist/131e8a94c955b973b87f7fb87d0f594b`
- Status: LIVE as of May 26, 2026 (verified in `DOMAIN_39_GIST_VERIFICATION_MAY26.md`)
- [ ] Open in incognito — confirm live and accessible

**Gist verification verdict**: If both Gists load in incognito, write "GISTS: GREEN" in your send-day log.

---

## SECTION 5: Decision Tree Walkthrough

Walk through each of the three primary decision trees to confirm all terminal branches have named, executable actions. This should take 10 minutes — read each tree as a user who just received the relevant data.

### Day 7 Tree Walkthrough

**Scenario A (HOLD)**: You check dashboard on June 4. 18 Bitly clicks, 3 replies. Walk the tree:
- Bounces < 3: continue
- Clicks >= 15: continue to reply check
- Replies >= 2: DETERMINATION: HOLD
- Action: "Proceed to normal Phase 1 trajectory / Continue monitoring / Checkpoint again at Day 30"
- Named action? YES. Next checkpoint? Day 30 (June 27-28). No dead end.

**Scenario B (ESCALATE)**: You check dashboard on June 4. 2 Bitly clicks, 0 replies.
- Bounces < 3: continue
- Clicks 0-4: ESCALATE branch
- Action: "Within 24 hours: 1. Verify Bitly link in incognito 2. Check Gmail spam folder 3. Forward to test account 4. If broken link: create new links and resend 5. If spam: contact email provider 6. If test works: possible audience issue — Modification 2"
- Named action? YES. No dead end.

**Scenario C (CONTACT_VERIFY)**: 4 bounces.
- Bounces >= 3: DETERMINATION: CONTACT_VERIFY
- Action: "Pull DISTRIBUTION_OUTREACH_CONTACTS.md / Verify all email addresses / Resend to corrected list / Restart Day 7 clock"
- Named action? YES. No dead end.

Day 7 tree: ALL BRANCHES TERMINATE WITH NAMED ACTIONS. PASS.

### Day 14 Tree Walkthrough (applies only if Day 7 = MONITOR)

**Scenario A**: Cumulative 28 clicks by June 11.
- >= 25 clicks: DETERMINATION: Escalate to HOLD
- Action: "No action; continue to Day 30"
- Named action? YES. No dead end.

**Scenario B**: Cumulative 15 clicks by June 11.
- 10-24 clicks: DETERMINATION: CONTINUE_MONITOR
- Action: "Apply Modification 2 (framing revision) / Prepare revised email / Plan Day 45 re-send"
- Named action? YES. No dead end.

**Scenario C**: Cumulative 7 clicks by June 11.
- < 10 clicks: DETERMINATION: FAILURE_IMMINENT
- Action: "Within 48 hours: 1. Contact Tier 1 directly (phone/video) 2. Resend if addresses wrong 3. Create new Bitly links 4. Full failure recovery protocol (PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md)"
- Named action? YES. No dead end.

Day 14 tree: ALL BRANCHES TERMINATE WITH NAMED ACTIONS. PASS.

### Day 30 Tree Walkthrough

**FAILURE check**: A<10%, C=0, D=0, Week 3+4 Bitly=0.
- Action: "User decision required within 48h / Update CHECKIN.md / Present 3 options: CONTINUE, PIVOT, or CLOSE / Send Domain 39 regardless"
- Named action? YES. User decision gate specified. No dead end.

**STRONG check**: A>=50%, B>=4, C>=3, D>=2.
- 5 numbered immediate actions within 24 hours, including Domain 39 send "by end of Day 1"
- Named action? YES. No dead end.

**MODERATE check**: A 20-49% OR B>=3 OR C>=1 OR D>=1.
- 5 numbered actions within 24-48 hours
- Named action? YES. No dead end.

**WEAK check**: A<20%, B<2, C=0, D=0.
- Three modifications with named by-Day deadlines (Mod 1 by Day 37, Mod 2 by Day 35, Mod 3 by Day 45)
- Named action? YES. No dead end.

**ASSESS**: Partial signals.
- "Send Domain 39 only / Continue Phase 1 / Wait for Day 60 / Do NOT activate WEAK recovery yet"
- Named action? YES. No dead end.

Day 30 tree: ALL BRANCHES TERMINATE WITH NAMED ACTIONS. PASS.

**Escalation path check**: Does every escalation path identify a named next file or next action?
- FAILURE → CHECKIN.md "Needs Your Input" section (user reads daily)
- STRONG → "Update CHECKIN.md with STRONG result" (Day 1 action)
- WEAK Modification 2 → "See failure recovery protocol in PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md"
- ESCALATE (Day 7) → file list: DISTRIBUTION_OUTREACH_CONTACTS.md, incognito test, Gmail spam check

All escalation paths reference a named file or a named executable action. No dead ends.

**Decision tree walkthrough verdict**: Write "DECISION TREES: GREEN — all branches terminate" in your send-day log.

---

## SECTION 6: TOO_EARLY / Contingency Activation Verification

The TOO_EARLY contingency path is relevant if the May 28 synthesis produces a "too early" classification rather than a clear STRONG/MODERATE/WEAK outcome.

**Source file**: `projects/resistance-research/TOO_EARLY_CONTINGENCY_STAGING_MAY26.md`

- [ ] File exists and is readable
- [ ] TOO_EARLY classification criteria documented: "Zero signals, no bounces (law school window still open)"
- [ ] Manual classification fallback present: "TOO EARLY: Zero replies AND zero Gist delta AND no bounces"
- [ ] Path-independent non-negotiable actions documented for any outcome:
  - Log outcome in synthesis-execution-log.txt
  - Post CHECKIN.md entry with outcome classification
  - Confirm Domain 56 Tier 2 sends complete
  - Confirm Domain 39 June 1 send window staged
- [ ] TOO_EARLY does not block May 28 Domain 56 Tier 2 distribution — the TOO_EARLY path is a synthesis outcome classification, not a distribution gate

**Synthesis window check**:
- Synthesis runs: May 28, 19:00 UTC
- Domain 56 distribution: May 28, 08:00 UTC
- These are independent. Distribution happens first. Synthesis outcome does not affect Tier 2 sends.

- [ ] Confirm: The synthesis and the Tier 2 distribution are on the same calendar day (May 28) but independent operations. Sends can proceed at 08:00 UTC without waiting for 19:00 UTC synthesis.

**Contingency verdict**: Write "CONTINGENCY PATH: GREEN — TOO_EARLY path staged and domain 56 send is synthesis-independent" in your send-day log.

---

## SECTION 7: Send-Day Readiness Summary

Complete this section after working through Sections 1-6.

| Section | Status | Notes |
|---|---|---|
| Monitoring infrastructure (reply triage, decision trees, dashboard) | | |
| Contact verification (all 4 Tier 2 contacts) | | |
| Template audit (all 4 templates, Gist URL confirmed) | | |
| Gist staging (Domain 56 + Domain 39 both live) | | |
| Decision tree walkthrough (no dead ends) | | |
| Contingency activation (TOO_EARLY staged, send-independent) | | |

**All six GREEN**: Cleared for May 28 distribution. Proceed to `DOMAIN_56_DISTRIBUTION_PACK.md` for the send sequence.

**Any RED**: Do not send until the red item is resolved. Document the blocker in `CHECKIN.md` under "Needs Your Input."

---

## Send Order for May 28 (Summary)

Recommended order per `TOO_EARLY_CONTINGENCY_STAGING_MAY26.md`:

1. Volcker Alliance — highest institutional credibility hook (send first)
2. Democracy Forward — active litigation alignment (send second)
3. CREW — FAQ framing, web form (send third)
4. Government Executive — op-ed pitch format, editorial review cycle (send last)

Stagger by 24-48 hours if possible. All four sends should be complete by May 28 end of day.

---

*Checklist created: May 26, 2026. Pre-testing window: May 27 evening. Distribution window: May 28, 08:00 UTC.*
