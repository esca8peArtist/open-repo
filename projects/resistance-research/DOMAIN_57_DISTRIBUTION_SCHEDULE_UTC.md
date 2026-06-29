---
title: "Domain 57 — Deterministic Distribution Schedule (UTC-Stamped)"
domain: 57
created: "2026-06-29"
session: "Item 51 — Domain 57 Phase 2 Pre-Staging"
status: "PRODUCTION-READY — mechanical execution, zero user decisions at August 10 trigger"
trigger: "August 10, 2026 00:00 UTC — run this schedule"
gist_url: "https://gist.github.com/esca8peArtist/a94ef436fd4a678f89e867ac8ed3dd61"
total_sends: 42
primary_window: "August 10–22, 2026"
escalation_window: "August 23–30, 2026"
---

# Domain 57 — Deterministic Distribution Schedule
## UTC-Stamped Send Sequence: August 10–30, 2026

This schedule is fully mechanical. At the August 10 trigger, execute sends in order. No user decisions required unless escalation gates specify otherwise. All decisions are pre-made in this document.

---

## PRE-SEND CHECKLIST (August 8–9, 2026)

Execute these 6 steps on August 8 or August 9 before any sends:

```
[ ] Step 1: Verify Gist URL (5 min)
    - Open https://gist.github.com/esca8peArtist/a94ef436fd4a678f89e867ac8ed3dd61 in incognito browser
    - Confirm: page loads without login, markdown renders, citation section visible, word count ~7,200
    - If Gist is unavailable: see contingency in Section 7 below

[ ] Step 2: Spot-check Tier 1 named contacts (20 min)
    - Ryan Goodman: confirm current co-editor-in-chief at justsecurity.org
    - Tanya Greene: confirm current US Program Director at hrw.org/about/people
    - Tamara Cofman Wittes: confirm current president at ndi.org
    - Gerardo Berthin / Annie Boyajian: confirm co-presidents at freedomhouse.org/about-us/board-leadership
    - Nadia Daar: confirm executive director at amnestyusa.org/about-us/who-we-are/executive-team/
    - Thomas Carothers: confirm director at carnegieendowment.org/about/staff
    - Michael Cooper: confirm executive director at asil.org/about/asil-staff/

[ ] Step 3: Verify Senate Foreign Relations Committee contact (10 min)
    - Confirm current Ranking Member identity at foreign.senate.gov
    - Find Ranking Member staff director or foreign policy counsel name and email
    - Update Template 3 send entry (Contact #20) with confirmed name/email

[ ] Step 4: Verify DOMAIN_57_GIST_URL.txt is updated (2 min)
    - Open DOMAIN_57_GIST_URL.txt
    - Confirm it contains the live URL (not [HASH_TO_BE_FILLED_AFTER_CREATION])
    - If still placeholder: update with https://gist.github.com/esca8peArtist/a94ef436fd4a678f89e867ac8ed3dd61

[ ] Step 5: Fill [YOUR_NAME] and [YOUR_CONTACT_INFO] in all templates (10 min)
    - Open DOMAIN_57_AUG10_EMAIL_TEMPLATES.md
    - Find-replace [YOUR_NAME] and [YOUR_CONTACT_INFO] in all 16 templates
    - Confirm all 15 Gist URL instances are pre-filled (they are — no action needed)

[ ] Step 6: Test one send (5 min)
    - Send Template 1 to yourself first
    - Confirm: not landing in spam, formatting correct, Gist URL clickable
    - If landing in spam: add plain-text fallback (strip markdown formatting from body)
```

---

## WAVE 1 — CONSTITUTIONAL SCHOLARS AND ACLU (August 10–13)

**Objective**: Establish constitutional framing in the academic/legal advocacy community before UNGA-facing orgs receive the document.

| UTC Time | Contact # | Organization | Email | Template | Spacing |
|---------|-----------|-------------|-------|----------|---------|
| Aug 10, 14:00 UTC | 1 | Just Security (Ryan Goodman) | ryan.goodman@nyu.edu | Template 1 | — |
| Aug 10, 15:30 UTC | 2 | Just Security (Tess Bridgeman) | submissions@justsecurity.org | Template 2 | 90 min |
| Aug 11, 14:00 UTC | 3 | Lawfare (editorial) | press@lawfaremedia.org | Template 3 | Next day |
| Aug 11, 15:30 UTC | 4 | Thomas Ginsburg (U of Chicago) | tginsburg@uchicago.edu | Template 4 | 90 min |
| Aug 12, 14:00 UTC | 5 | ACLU Center for Democracy | media@aclu.org | Template 5 | Next day |
| Aug 12, 15:30 UTC | 6 | ACLU International Human Rights | humanrights@aclu.org | Template 6 | 90 min |
| Aug 13, 14:00 UTC | 7 | ACLU National Security Project | nsproject@aclu.org | Template 7 | Next day |
| Aug 13, 15:30 UTC | 8 | Democracy Forward (Somil Trivedi) | info@democracyforward.org | Template 8 | 90 min |

**Wave 1 checkpoint**: August 13, 23:59 UTC
- Check: any responses received from contacts 1-8?
- Log responses in DOMAIN_57_DISTRIBUTION_LOG.csv (file created in Section 6)
- Gate: proceed to Wave 2 regardless of response rate (Wave 2 is not contingent on Wave 1 responses)

---

## WAVE 2 — DEMOCRACY FORWARD AND TIER 1 INTERNATIONAL ORGS (August 14–16)

**Objective**: Reach ICC/HRW/Freedom House community while Wave 1 constitutional framing is still in their reading queue.

| UTC Time | Contact # | Organization | Email | Template | Spacing |
|---------|-----------|-------------|-------|----------|---------|
| Aug 14, 14:00 UTC | 9 | Democracy Forward (Bradley Girard) | info@democracyforward.org | Template 9 | Next day |
| Aug 14, 15:30 UTC | 10 | Democracy Forward (Lydia Hubert-Peterson) | info@democracyforward.org | Template 10 | 90 min |
| Aug 15, 14:00 UTC | 11 | Human Rights Watch (US Program) | advocacy@hrw.org | Template 11 | Next day |
| Aug 15, 15:30 UTC | 12 | Coalition for the ICC | info@coalitionfortheicc.org | Template 12 | 90 min |
| Aug 16, 14:00 UTC | 13 | Freedom House | policy@freedomhouse.org | Template 13 | Next day |
| Aug 16, 15:30 UTC | 14 | Amnesty International USA | contactus@aiusa.org | Template 14 | 90 min |

**Wave 2 checkpoint**: August 16, 23:59 UTC
- Check: any responses from contacts 1-14?
- Classification gate: apply Wave 2 signal classification (see Section 4 below)
- Gate: log classification, proceed to Wave 3 per schedule regardless of classification
- Note: Python decision tree (DOMAIN_57_WAVE2_DECISION_TREE.py) automates this classification

---

## WAVE 3 — NDI, CARNEGIE, AND ESCALATION (August 17–18)

**Objective**: Reach democracy promotion organizations and trigger escalation if Wave 1-2 generated no response.

| UTC Time | Contact # | Organization | Email | Template | Spacing |
|---------|-----------|-------------|-------|----------|---------|
| Aug 17, 14:00 UTC | 15 | NDI (Tamara Cofman Wittes) | contact@ndi.org | T2 variant | Next day |
| Aug 17, 15:30 UTC | 16 | Carnegie Endowment (Thomas Carothers) | info@ceip.org | Template 16 | 90 min |
| Aug 18, 14:00 UTC | 17 | ASIL (Michael Cooper) | info@asil.org | Template 15 | Next day |
| Aug 18, 15:30 UTC | 18 | Carnegie (escalation if no Wave 1-2 response) | info@ceip.org | Template 16 | 90 min |

**Escalation gate at Aug 18, 13:00 UTC**:
- If 0 responses from contacts 1-16 → proceed to Contact 17 AND Contact 18 (send both)
- If 1+ responses from contacts 1-16 → send Contact 17 (ASIL) only; skip Contact 18 (Carnegie already sent Aug 17)
- If 3+ responses → skip Contact 17; focus on response follow-up

---

## WAVE 4 — INTERNATIONAL LAW NETWORK (August 19–22)

**Objective**: Reach universal jurisdiction and specialized international law organizations.

| UTC Time | Contact # | Organization | Email | Template | Spacing |
|---------|-----------|-------------|-------|----------|---------|
| Aug 19, 14:00 UTC | 19 | Democracy Forward (CEO escalation) | info@democracyforward.org | Template 10 | Next day |
| Aug 19, 15:30 UTC | 20 | Senate Foreign Relations Committee | [verified Aug 8-9] | T3 variant | 90 min |
| Aug 20, 14:00 UTC | 21 | Senate Int'l Human Rights Caucus | [verified Aug 8-9] | T3 variant | Next day |
| Aug 20, 15:30 UTC | 22 | FIDH | fidh@fidh.org | T4 variant | 90 min |
| Aug 21, 14:00 UTC | 23 | Council on Foreign Relations | info@cfr.org | T2 variant | Next day |
| Aug 21, 15:30 UTC | 24 | Stimson Center | info@stimson.org | T2 variant | 90 min |
| Aug 22, 14:00 UTC | 25 | PIIE (Adam Posen) | comments@piie.com | T2 variant | Next day |
| Aug 22, 15:30 UTC | 26 | International Crisis Group | info@crisisgroup.org | T2 variant | 90 min |

**Note on Contact 19 (Democracy Forward CEO escalation)**: Send only if no response from contacts 8-10 (Democracy Forward earlier sends) by August 18, 23:59 UTC.

---

## WAVE 5 — EXTENDED CONTACTS (August 23–30)

**Execute only if**: Wave 2 checkpoint signal is HIGH or MODERATE (see Section 4). If ZERO signal, pause at Wave 5 and reassess framing.

| UTC Time | Contact # | Organization | Email | Template |
|---------|-----------|-------------|-------|----------|
| Aug 23, 14:00 UTC | 27 | HIAS | info@hias.org | T1 variant (ICC + refugee) |
| Aug 23, 15:30 UTC | 28 | IRAP | info@refugeerights.org | T1 variant |
| Aug 24, 14:00 UTC | 29 | Stanley Foundation | info@stanleyfoundation.org | T2 variant |
| Aug 24, 15:30 UTC | 30 | UN Association of the USA | info@unausa.org | T2 variant (UNGA lead) |
| Aug 25, 14:00 UTC | 31 | Brennan Center | brennan.center@nyu.edu | T2 variant (domestic electoral) |
| Aug 25, 15:30 UTC | 32 | Protect Democracy | contact@protectdemocracy.org | T8 variant (executive power) |
| Aug 26, 14:00 UTC | 33 | REDRESS | info@redress.org | T4 variant |
| Aug 26, 15:30 UTC | 34 | Civitas Maxima | info@civitas-maxima.org | T4 variant |
| Aug 27, 14:00 UTC | 35 | CICC member NGOs (US-based) | [via CICC directory] | T12 variant |
| Aug 27, 15:30 UTC | 36 | Atlantic Council (Scowcroft) | info@atlanticcouncil.org | T3 variant |
| Aug 28, 14:00 UTC | 37 | IJRC | info@ijrcenter.org | T15 variant |
| Aug 28, 15:30 UTC | 38 | GCR2P | globalr2p@globalr2p.org | T12 variant |
| Aug 29, 14:00 UTC | 39 | Just Security (research submission) | submissions@justsecurity.org | T1 adapted |
| Aug 29, 15:30 UTC | 40 | Human Rights First | info@humanrightsfirst.org | T1 variant |
| Aug 30, 14:00 UTC | 41 | LRWC | lrwc@portal.ca | T4 variant |
| Aug 30, 15:30 UTC | 42 | Opinio Juris | [contact form] | T1 variant (academic) |

---

## SECTION 4: WAVE 2 SIGNAL CLASSIFICATION

**Classification window**: August 13 23:59 UTC – August 16 23:59 UTC (Days 3-6 post-send)

Run `python3 DOMAIN_57_WAVE2_DECISION_TREE.py` on August 16, 23:00 UTC for automated classification. Or use this manual guide:

| Signal Level | Definition | Wave 5 Action | Carnegie/ASIL Acceleration |
|---|---|---|---|
| **HIGH** | 2+ substantive replies OR 1 reply requesting follow-up meeting/publication | Execute Wave 5 in full | Accelerate Carnegie to Aug 12 if possible |
| **MODERATE** | 1 substantive reply (any engagement beyond acknowledgment) | Execute Wave 5 in full | Standard schedule |
| **LOW** | 1-2 automated acknowledgments only, OR 1 bounce | Execute Wave 5, skip contacts 35-42 | Standard schedule |
| **ZERO** | No replies, no acknowledgments, no bounces | Pause at Wave 5; review framing before contacts 35-42 | Delay Carnegie; reassess August 25 |

**Substantive reply definition**: Any reply that (a) asks a follow-up question about the research, (b) requests an adapted version, (c) indicates the research has been forwarded to a program team, or (d) proposes a meeting or call. Automated acknowledgments, out-of-office replies, and generic "thanks for sharing" do not qualify.

---

## SECTION 5: ESCALATION DECISION TREE

**Day 3 Escalation Gate (August 13, 14:00 UTC)**:
- 0 responses from contacts 1-7 → send Contact 17 (ASIL) on August 13 instead of August 18
- 1+ responses → proceed as scheduled

**Day 7 Escalation Gate (August 17, 14:00 UTC)**:
- 0 responses from contacts 1-16 → add CC to Contacts 17 and 18 of an adapted "2-week follow-up" note referencing the UNGA 81 timing (September 22 is now 5 weeks away)
- 3+ responses → skip Wave 4 escalation; focus on response threading

**Day 14 Follow-up Gate (August 24, 14:00 UTC)**:
- For any Tier 1-2 contacts who have not responded → send one brief follow-up email (under 100 words): "I'm following up on the Domain 57 research I shared on [date]. With UNGA 81 High-Level Week opening September 22, I wanted to confirm the document reached your team. Happy to provide an adapted version or answer any questions."
- For contacts who responded → continue the conversation; do not send follow-up to active threads

**If ALL sends complete with ZERO engagement by August 30**:
- File: review DOMAIN_57_ZERO_SIGNAL_CONTINGENCY in DOMAIN_57_WAVE2_DECISION_TREE.py output
- Action: Switch lead hook from ICC sanctions to constitutional asymmetry argument (no Senate role in exit); this argument is not news-dependent and doesn't require active news hook to land
- Framing reset: consider UNGA 81 real-time hook (September 22-28) for second distribution wave to same contacts with updated framing

---

## SECTION 6: LOGGING

**File to create (August 10, before first send)**:
```
DOMAIN_57_DISTRIBUTION_LOG.csv
```

**CSV headers**:
```
contact_id,organization,email,template,sent_utc,response_received,response_date,response_type,notes
```

**Response types**:
- SUBSTANTIVE — asks question, proposes meeting, requests adaptation
- ACKNOWLEDGMENT — automated or generic "thanks for sharing"
- OUT_OF_OFFICE — auto-reply; log expected return date
- BOUNCE — email undeliverable; log error code
- NO_RESPONSE — no reply by T+14

**T+30 checkpoint (September 9, 2026)**:
- Complete the response log for all 42 contacts
- Update WORKLOG.md with Domain 57 distribution completion entry
- Note any secondary distribution (organizations that shared the research forward)
- File DOMAIN_57_SEND_COMPLETE confirmation in CHECKIN.md

---

## SECTION 7: CONTINGENCY — IF GIST UNAVAILABLE ON AUGUST 10

If the Gist URL returns anything other than HTTP 200:

**Step 1**: Try alternate URL: check DOMAIN_57_GIST_URL.txt and DISTRIBUTION_GIST_URLS.md for any alternate URL.

**Step 2**: If Gist is deleted or account suspended: create a new public Gist under the same content from a new anonymous account. The domain document source is at `domains/domain-57-multilateral-withdrawal-executive-authority.md`. New Gist creation: 30 minutes.

**Step 3**: Update the Gist URL in all 16 templates (find-replace `https://gist.github.com/esca8peArtist/a94ef436fd4a678f89e867ac8ed3dd61` with new URL).

**Step 4**: Update DISTRIBUTION_GIST_URLS.md with new URL.

**Step 5**: Delay Wave 1 by 2 hours to allow Gist verification.

---

*Schedule created: June 29, 2026 (Session Item 51). All send times in UTC. Spacing: 90 minutes between same-day sends (minimum); overnight between consecutive waves (optimal). Send window optimized for US Eastern working hours (14:00-15:30 UTC = 10:00-11:30 AM ET). Pre-send checklist must be completed August 8-9. August 10 execution: mechanical, zero user decisions required.*
