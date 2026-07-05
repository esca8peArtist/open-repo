---
title: "Tier 1 + Tier 2 Contact Escalation Reference (Item 45.3)"
subtitle: "Domain 51 + Domain M — Consolidated Send Order, Addresses, and Fallbacks"
created: "2026-07-04"
item: "Item 45.3"
status: "production-ready"
verification_date: "June 29-30, 2026 (primary); July 4, 2026 (cross-check)"
purpose: "Single-page reference for orchestrator and user: who to contact, in what order, via which path"
cross_reference_item_44: "CONTINGENCY_ACTIVATION_DECISION_TREE_ITEM44.py — run this script first to determine PATH_A, PATH_A_AND_B, PATH_B, or PATH_B_LATE; this file gives you the contacts for each path"
---

# Tier 1 + Tier 2 Contact Escalation Reference

This file is a consolidated lookup. It does not contain email bodies — those are in the runbooks. It answers one question: given the current date and execution status, which contacts are active and in what order?

**Run Item 44 classifier first:**

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/resistance-research
python3 CONTINGENCY_ACTIVATION_DECISION_TREE_ITEM44.py
```

The classifier reads INBOX.md and outputs your current path (BRANCH_0, PATH_A, PATH_A_AND_B, PATH_B, PATH_B_LATE). Then use the table for that path below.

---

## Path Lookup Table

| Path | Condition | Tier 1 Active | Tier 2 Active | Runbook to Open |
|------|-----------|---------------|---------------|-----------------|
| BRANCH_0 | Domain 51 sent by June 30 23:59 UTC | None (Domain 51 succeeded) | None | No contingency |
| PATH_A | Deadline missed; before July 8 23:59 UTC | Domain M: BISC, DD, CC | Domain 51 Tier 2: July 1-8 send sequence | DOMAIN_M_CONTINGENCY_ACTIVATION_RUNBOOK.md + DOMAIN_51_TIER_2_ACCELERATED_SEND_SEQUENCE.md |
| PATH_A_AND_B | Deadline missed; July 1-8 UTC (both active) | Domain M: BISC, DD, CC | Domain 51 Tier 2: all 14 sends July 1-8 | Both runbooks in parallel |
| PATH_B | July 9-14 UTC; Domain 51 Tier 2 window closing | Domain M: BISC, DD, CC | Domain M Tier 2: LWV, Brennan, MFFG, Represent.Us | DOMAIN_M_CONTINGENCY_ACTIVATION_RUNBOOK.md |
| PATH_B_LATE | July 15+ UTC | Domain M Tier 1 still open through August 1 | Domain M Tier 2 continues | DOMAIN_M_CONTINGENCY_ACTIVATION_RUNBOOK.md |

---

## Tier 1 Contacts — Domain M Contingency (July 1-15)

These are the three highest-leverage contacts for the Domain M contingency. They activate July 1 if Domain 51 missed its deadline.

Full email templates in: `DOMAIN_M_CONTINGENCY_ACTIVATION_RUNBOOK.md` (Section 2)

| Send | Organization | Role | Email / Method | Target Date | Fallback |
|------|--------------|------|----------------|-------------|----------|
| 1 | Ballot Initiative Strategy Center (BISC) | National coalition coordinator for 93+ nonprofits in 26 initiative states | Contact form at ballot.org/contact | July 1, 14:00 UTC | info@ballot.org |
| 2 | Democracy Docket | Constitutional litigation and public education on democracy rights | info@democracydocket.com | July 4, 10:00 UTC | melias@democracydocket.com (Marc Elias, Founder) |
| 3 | Common Cause National | National advocacy; routes to state chapter staff in MO, ND, SD, UT | commoncause@commoncause.org | July 8, 14:00 UTC | commoncause.org/contact (contact form) |

**Rationale**: BISC first because they coordinate the 93-organization coalition running Defend Direct Democracy campaigns. Democracy Docket second because they add constitutional litigation framing. Common Cause National third because they route to active state chapter staff in all four target states (Missouri, North Dakota, South Dakota, Utah).

**Critical notes**:
- Do NOT use kflynn@commoncause.org — Karen Hobert Flynn is deceased (March 2023). Virginia Kase Solomón is current President and CEO.
- July 4 send to Democracy Docket is intentional — they monitor urgent democracy matters continuously.
- BISC contact form is the primary channel, not a personal email.

---

## Tier 2 Contacts — Domain M (July 10-22)

Activate Tier 2 regardless of Tier 1 reply status. Do not wait for BISC/DD/Common Cause replies before sending Tier 2.

Full email templates in: `DOMAIN_M_CONTINGENCY_ACTIVATION_RUNBOOK.md` (Section 4)

| Send | Organization | Email / Method | Target Date | Fallback |
|------|--------------|----------------|-------------|----------|
| 4 | League of Women Voters National | contact@lwv.org (CC: MO@lwv.org, ND@lwv.org, SD@lwv.org, UT@lwv.org) | July 10, 14:00 UTC | lwv@lwv.org |
| 5 | Brennan Center for Justice | democracy@brennancenter.org | July 14, 14:00 UTC | brennancenter.org/contact |
| 6 | Missourians for Fair Governance (Respect Missouri Voters) | Contact form at respectmissourivoters.org | July 16, 14:00 UTC | inquiries@respectmissourivoters.org |
| 7 | Represent.Us | info@represent.us | July 22, 14:00 UTC | represent.us/contact |

**Tier 2 gate rule**: Do NOT wait for Tier 1 replies before executing Tier 2. Silence from BISC, DD, or Common Cause for 5-7 days is normal. The contact window is what matters, not confirmed interest.

---

## Tier 2 Contacts — Domain 51 Contingency (July 1-8, PATH_A)

These are the 14 Domain 51 Tier 2 contacts for the accelerated send sequence if the June 30 deadline was missed. Full email bodies in: `DOMAIN_51_FALLBACK_TIER_2_CONTACTS.md` and `DOMAIN_51_48_TIER_2_CONTACT_MATRIX_CURRENT.md`.

Full send schedule in: `TIER_2_ACCELERATED_SEND_MASTER_SCHEDULE.md`

### Block A — Research and Academic (Priority 1, July 1-2)

| Send | Contact | Organization | Email | Response Probability |
|------|---------|--------------|-------|---------------------|
| 1 | Lisa Graves | True North Research | lisa@truenorthresearch.org | 50-65% |
| 2 | Rick Hasen | UCLA Safeguarding Democracy Project | rhasen@law.ucla.edu | 40-55% |

**Graves hook**: Section 4 (ALEC donor network architecture) and Section 6.2 (501(c)(4) routing) — her primary investigative territory.
**Hasen hook**: Section 6.3 (Hawaii/Montana corporate charter theory) — doctrinal novelty for Election Law Blog readership.

### Block B — Advocacy Organizations (Priority 2, July 2-4)

| Send | Contact | Organization | Email | Response Probability |
|------|---------|--------------|-------|---------------------|
| 3 | Taifa Smith Butler | Demos | info@demos.org | 35-50% |
| 4 | Sophia Lin Lakin | ACLU Voting Rights Project | slakin@aclu.org (tentative) | 25-40% |
| 5 | Lawrence Norden | Brennan Center — Elections Program | nordenl@brennan.law.nyu.edu | 35-50% |
| 6 | Virginia Kase Solomón | Common Cause National | commoncause@commoncause.org | 35-50% |
| 7 | Joshua Douglas | Election Law Journal | jdoug2@uky.edu | 30-45% |
| 8 | Justin Levitt | Loyola Law School | jlevitt@lls.edu | 30-40% |

**Slakin note**: slakin@aclu.org is from prior session documentation — treat as tentative; verify before sending.
**Norden note**: This is a separate contact from Brennan Center Tier 2 Send 5 (Saurav Ghosh, ghoshs@brennan.law.nyu.edu). Do NOT send both Norden and Ghosh in the same week.

### Block C — Institutional (Priority 3, July 7-8)

| Send | Contact | Organization | Email | Response Probability |
|------|---------|--------------|-------|---------------------|
| 9 | Heidi Shierholz | Economic Policy Institute | hshierholz@epi.org | 25-40% |
| 10 | Kara Gotsch | The Sentencing Project | info@sentencingproject.org | 25-35% |
| 11 | Jeff Mangan | Transparent Election Initiative (Montana I-194) | Contact form at transparentelection.org | 25-40% |
| 12 | Fred Wertheimer | Democracy 21 | fwertheimer@democracy21.org | 40-55% |
| 13 | Craig Holman | Public Citizen | cholman@citizen.org | 35-50% |
| 14 | Saurav Ghosh | Brennan Center — Democracy Program | ghoshs@brennan.law.nyu.edu | 35-50% |

**Sentencing Project note**: This Domain 51 send goes to info@sentencingproject.org with a dark money + voter suppression angle. It is DISTINCT from the Domain 48 send to Nicole D. Porter (nporter@sentencingproject.org). Do not conflate.

---

## Domain 51 Wave 1 Contacts (Tier 1 — Pre-Deadline)

For reference: these 5 contacts were the June 30 23:59 UTC deadline sends. If the deadline was not missed, these are your Tier 1 sends and no contingency activates.

Full templates in: `DOMAIN_51_WAVE_1_EXECUTION_RUNBOOK.md` (Section 2)

| Send | Contact | Organization | Email | Fallback |
|------|---------|--------------|-------|----------|
| 1 | Erin Chlopak, Sr. Director Campaign Finance | Campaign Legal Center | echlopak@campaignlegalcenter.org | info@campaignlegal.org |
| 2 | General inbox (Nick Penniman, CEO) | Issue One | info@issueone.org | nick@issueone.org |
| 3 | Darius Kemp, Executive Director | Common Cause California | dkemp@commoncause.org | info@commoncause.org |
| 4 | Jenny Farrell, Executive Director | League of Women Voters California | lwvc@lwvc.org | No fallback — omit if bounces |
| 5 | Trent Lange, President | Clean Money Action Fund | info@CAclean.org | CRITICAL: NOT info@cleanmoney.org (unreachable since June 5, 2026) |

---

## Dead Contacts — Never Use

| Name | Organization | Former Email | Reason |
|------|--------------|-------------|--------|
| Karen Hobert Flynn | Common Cause National | kflynn@commoncause.org | DECEASED March 2023 |
| Sheila Krumholz | OpenSecrets | Former CEO email (varies) | Departed late 2023 |
| Jonathan Mehta Stein | Common Cause California | Former ED email | Departed June 2025; replaced by Darius Kemp |
| Trent Lange via cleanmoney.org | Clean Money Action Fund | info@cleanmoney.org | Domain unreachable since June 5, 2026 — use info@CAclean.org |

---

## Escalation Log Template

Create or append to `DOMAIN_M_CONTINGENCY_EXECUTION_LOG.md` after each send:

```
| [Send #] | [Organization] | [Target Date] | [Actual UTC] | SENT | [Reply Y/N] |
```

Existing Domain 51 send log: `DOMAIN_51_DISTRIBUTION_SEND_LOG.md`

---

## Cross-Reference: Item 44 Decision Tree Integration

The Item 44 classifier (`CONTINGENCY_ACTIVATION_DECISION_TREE_ITEM44.py`) outputs a path classification that directly maps to which contacts in this file to activate. The mapping:

| Classifier Output | Contacts to Activate |
|-------------------|---------------------|
| BRANCH_0 | None — Domain 51 succeeded |
| PATH_A | Domain 51 Tier 2: Blocks A-C above (14 sends, July 1-8) |
| PATH_A_AND_B | Domain 51 Tier 2 Blocks A-C + Domain M Tier 1 Sends 1-3 (parallel) |
| PATH_B | Domain M Tier 1 Sends 1-3 + Tier 2 Sends 4-7 |
| PATH_B_LATE | Domain M Tier 1 Sends 1-3 (still open through August 1) + Tier 2 Sends 4-7 |
| UNKNOWN | Post outcome to INBOX.md; Domain M Tier 1 proceeds independently |

**Template files the classifier copies to `./next-action/` for PATH_A or PATH_A_AND_B:**
- `DOMAIN_51_TIER_2_ACCELERATED_SEND_SEQUENCE.md`
- `TIER_2_ACCELERATED_SEND_MASTER_SCHEDULE.md`
- `DOMAIN_51_48_TIER_2_CONTACT_MATRIX_CURRENT.md`
- `DOMAIN_M_JULY_1_15_ACTIVATION_SEQUENCE.md` (PATH_A_AND_B only)
- `DOMAIN_M_TIER_1_SEND_TEMPLATES.md` (PATH_A_AND_B only)

---

## Quick-Reference Timing Summary

```
CURRENT STATUS (as of July 4, 2026):
Domain 51 deadline: MISSED (June 30 23:59 UTC passed)
Domain M contingency: ACTIVE (auto-triggered July 1 00:00 UTC)

ACTIVE SENDS:
Domain M Send 1 (BISC)         — TARGET: July 1 14:00 UTC   — STATUS: check log
Domain M Send 2 (Democracy Docket) — TARGET: July 4 10:00 UTC — STATUS: today
Domain M Send 3 (Common Cause) — TARGET: July 8 14:00 UTC   — UPCOMING
Domain M Send 4 (LWV National) — TARGET: July 10 14:00 UTC  — UPCOMING
Domain M Send 5 (Brennan Center) — TARGET: July 14 14:00 UTC — UPCOMING
Domain M Send 6 (MFFG)         — TARGET: July 16 14:00 UTC  — UPCOMING
Domain M Send 7 (Represent.Us) — TARGET: July 22 14:00 UTC  — UPCOMING

WINDOW FOR DOMAIN 51 TIER 2 (PATH_A):
July 1-8 accelerated window — if these sends have NOT yet gone out, they should
go immediately. Each day past July 1 reduces value by approximately 3-5%.
The window does not close hard on July 8 — sends through July 14 still reach
value at 50-60%. After July 15: hold remaining sends, focus on Domain M.
```

---

*Item 45.3 — Tier 1+2 Contact Escalation Reference. Produced July 4, 2026.*
*Contact data verified June 29-30, 2026 (primary). July 4, 2026 cross-check against runbooks.*
*Full email bodies: DOMAIN_51_WAVE_1_EXECUTION_RUNBOOK.md (Domain 51 Tier 1), DOMAIN_M_CONTINGENCY_ACTIVATION_RUNBOOK.md (Domain M Tier 1+2), DOMAIN_51_FALLBACK_TIER_2_CONTACTS.md (Domain 51 Tier 2 detailed bodies).*
*Decision tree integration: CONTINGENCY_ACTIVATION_DECISION_TREE_ITEM44.py (Item 44).*
