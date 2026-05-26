---
title: "Phase 1 Impact Monitoring Dashboard — Unified Operational Guide"
created: 2026-05-27
version: 1.0
status: production-ready
scope: >
  Unified monitoring infrastructure for Domain 56 (May 28) and Domain 39 (June 1)
  distributions. Operational from first send through Day 30 decision. Covers Google Sheets
  setup, Gist view tracking protocol, reply triage, weekly synthesis, and checkpoint logic.
  All four deliverables are cross-referenced here and in the companion files.
distributions:
  domain_56:
    send_date: "May 28, 2026"
    contacts: 11 (C001–C011: Volcker Alliance, Democracy Forward, CREW, Gov't Executive + 7 Tier 1)
    gist_url: "https://gist.github.com/esca8peArtist/8f11e868397921a4e6556b41196d1b1f"
    bitly_back_half: "drp-d56"
  domain_39:
    send_date: "June 1, 2026 (HHS hard stop)"
    contacts: 5 (C012–C016: Georgetown CCF, NHeLP, Brennan Center, IRG, Black Mamas Matter)
    gist_url: "https://gist.github.com/esca8peArtist/131e8a94c955b973b87f7fb87d0f594b"
    bitly_back_half: "drp-d39"
checkpoint_dates:
  day_7: "June 4, 2026"
  day_14: "June 11, 2026"
  day_30: "June 27, 2026"
weekly_time_budget: "15–20 minutes"
companion_files:
  - REPLY_TRIAGE_FRAMEWORK.md (this directory)
  - DAY_7_14_30_DECISION_TREES.md (this directory)
  - phase-1-monitoring-sheets-template.csv (root resistance-research directory)
  - PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md (root resistance-research directory)
  - DOMAIN_56_TIER_2_DISTRIBUTION_MAY28_CHECKLIST.md (root)
  - DOMAIN_39_JUNE1_PRE_PRODUCTION_CHECKLIST.md (root)
---

# Phase 1 Impact Monitoring Dashboard — Unified Operational Guide

**Version 1.0 — May 27, 2026**

**Lead finding**: Two distributions launch within 4 days of each other (Domain 56 May 28, Domain 39 June 1). Without a single shared measurement surface, you will lose track of which signals belong to which domain, miss the Day 7 checkpoint, and make Phase 2 timing decisions on incomplete data. This document is that shared surface. Follow it and nothing else for post-launch measurement.

The entire monitoring workflow from Day 1 through Day 30 requires 15–20 minutes per week. No analytics tools beyond Google Sheets and Bitly free tier. No Claude dependency in the checkpoint decision trees — every branch terminates in a named action you can execute the same day.

---

## Section 1: Pre-Launch Setup (Complete by May 27 Evening)

### 1.1 Google Sheets — One Spreadsheet for Both Domains

Create a single Google Sheet titled: `Phase 1 Impact Dashboard — Domain 56 + Domain 39`

Sharing setting: Share > Change to anyone with the link > Viewer. Copy the share URL and paste it into CHECKIN.md under the heading "Dashboard URL."

**Seven sheets, exact names (click the + tab at the bottom of the screen to add each)**:

| Tab Name | Purpose |
|----------|---------|
| `Contacts` | Master log — one row per contact, both domains |
| `Gist_Views` | Weekly Bitly click log — separate columns per domain |
| `Replies` | One row per reply received (contacts may reply more than once) |
| `Adoptions` | Confirmed adoption signals and network referral events |
| `Constituencies` | Aggregated metrics per constituency group |
| `Checkpoints` | Append-only log of checkpoint determinations |
| `Synthesis_Log` | Weekly synthesis entries (15–20 min fills) |

**Google Sheets URL — create this sheet and paste the share link here**:

```
DASHBOARD_URL: [paste here after creating]
```

### 1.2 Import Contacts

The CSV template at `projects/resistance-research/phase-1-monitoring-sheets-template.csv` contains 16 pre-populated contacts (C001–C016) plus a sample row. Import or manually copy these into the Contacts tab.

**Contacts tab column schema** (Row 1 headers):

| Col | Header | Notes |
|-----|--------|-------|
| A | Contact_ID | C001–C016 (pre-filled in CSV) |
| B | Full_Name | Last, First or Org Name |
| C | Organization | Institution |
| D | Domain | Domain 56 / Domain 39 |
| E | Constituency | See constituency list below |
| F | Tier | Tier 1 / Tier 2 / Tier 3 |
| G | Email | Verified send address |
| H | Send_Date | Fill when email is sent |
| I | Delivery_Status | Delivered / Bounced / OOO / Unknown |
| J | Open_Date | Date first Bitly click detected (proxy for open) |
| K | Click_Date | Same as Open_Date for Bitly tracking |
| L | Reply_Date | Date first non-OOO reply received |
| M | Reply_Category | From: Implementation Signal / Critique / Data Request / General Question / No Reply |
| N | Engagement_Score | 0–5 (see REPLY_TRIAGE_FRAMEWORK.md) |
| O | Tier2_Candidate | YES / blank — flag when Score >= 3 |
| P | Day_to_Open | Formula: `=IF(J2="","",J2-H2)` |
| Q | Day_to_Click | Formula: `=IF(K2="","",K2-H2)` |
| R | Day_to_Reply | Formula: `=IF(L2="","",L2-H2)` |
| S | Referral_Made | Name or org the contact forwarded to |
| T | Notes | Free text |

**Constituency values to use** (standardized for formula matching):
- Civil Service Reform
- Federal Employee Union
- Civil Rights / Rule of Law
- Watchdog / Media
- Healthcare Policy
- Maternal Health

### 1.3 Auto-Calculation Block (Contacts Tab)

Add these formulas in a frozen summary block above or below your data rows. Leave two blank rows between data and this block. These four numbers feed every checkpoint decision:

```
Total contacts sent:         =COUNTA(H2:H200)-COUNTBLANK(H2:H200)
Confirmed delivered:         =COUNTIF(I2:I200,"Delivered")
Total replies:               =COUNTA(L2:L200)-COUNTBLANK(L2:L200)
Overall reply rate:          =Total replies / Confirmed delivered
Score 3+ count:              =COUNTIF(N2:N200,">=3")
Score 3+ rate:               =COUNTIF(N2:N200,">=3")/COUNTIF(I2:I200,"Delivered")
Tier 2 candidates:           =COUNTIF(O2:O200,"YES")
Avg day-to-reply:            =AVERAGE(R2:R200)
Engagement velocity:         =COUNTA(L2:L200)/MAX(1,(TODAY()-MIN(H2:H200)))
Cross-org references:        =COUNTA(S2:S200)-COUNTBLANK(S2:S200)
```

`Engagement velocity` is replies per calendar day. Target at Day 7: >0.3 (at least 2 replies in 7 days).

### 1.4 Gist Views Tab Schema

One row per week. Start Week 1 on the Monday after your first send (June 2 for a May 28 send).

| Col | Header | Formula/Notes |
|-----|--------|--------------|
| A | Week_Number | 1, 2, 3... |
| B | Week_End_Date | The Monday of each snapshot |
| C | D56_Clicks | Enter manually from Bitly — Domain 56 link |
| D | D39_Clicks | Enter manually from Bitly — Domain 39 link |
| E | DRP_Proposal_Clicks | Bitly link: drp-2026 |
| F | DRP_Summary_Clicks | Bitly link: drp-summary |
| G | Other_Clicks | Any additional tracked links |
| H | Total_This_Week | `=SUM(C2:G2)` |
| I | Cumulative | `=IF(A2=1,H2,I1+H2)` |
| J | Delta_vs_Prior | `=IF(A2=1,"—",H2-H1)` |
| K | Spike_Flag | `=IF(MAX(C2:G2)>=5,"SPIKE","")` |
| L | Spike_Notes | Which link, probable cause |

**Weekly targets**:
- Week 1 (by June 4): 15+ total clicks across both domains
- Week 2 (by June 11): 25+ cumulative
- Week 4 (by June 25): 50+ cumulative

### 1.5 Bitly Short Links — Create Before May 28

These must exist before your first send. Creating them takes 5 minutes at bitly.com (free account sufficient).

| Document | Gist URL | Bitly Back-Half to Use |
|----------|----------|----------------------|
| Domain 56 | https://gist.github.com/esca8peArtist/8f11e868397921a4e6556b41196d1b1f | drp-d56 |
| Domain 39 | https://gist.github.com/esca8peArtist/131e8a94c955b973b87f7fb87d0f594b | drp-d39 |
| DRP Proposal | https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261 | drp-2026 |
| Executive Summary | https://gist.github.com/esca8peArtist/2869da6eaeb15a47246ade3bbbc4a3f4 | drp-summary |

After creating each link: click it yourself and verify it resolves to the correct Gist. Check that your test click increments the Bitly counter. If the counter does not increment after 5 minutes, the link tracking is not working — delete and recreate the short link.

**Use Bitly links — not raw Gist URLs — in every outreach email.** This is the only way click data flows to your dashboard.

### 1.6 Gist View Tracking Protocol

GitHub Gist does not expose anonymous view counts via its public API. Bitly click tracking is the primary passive engagement proxy.

**Per-recipient Bitly links (optional but recommended for Domain 56 Tier 2 wave)**:

For the 4 organizations receiving Domain 56 on May 28, you can create per-recipient Bitly links to see exactly which organization clicked through. Use these back-halves:
- Volcker Alliance: `d56-volcker`
- Democracy Forward: `d56-demfwd`
- CREW: `d56-crew`
- Government Executive: `d56-govexec`

Per-recipient tracking is optional. If you skip it, use the single `drp-d56` link for all Domain 56 sends — you will know total clicks but not per-organization clicks.

**Weekly snapshot ritual (5 minutes, every Monday)**:

1. Log in to bitly.com
2. For each tracked link, click the link name and record the "Total clicks (7 days)" figure
3. Enter figures in Gist_Views tab, one row per week
4. Review the Spike_Flag column — if SPIKE appears, add notes identifying which link, approximate spike date, and whether it correlates with a send
5. If a spike occurs with no corresponding send: flag as organic amplification in the Spike_Notes column and in WORKLOG.md

**Escalation from Gist tracking**:
- Week 1 clicks < 5 (with confirmed delivery): test Bitly links manually; check for broken short link
- Any week after Week 2 with 0 clicks: investigate whether Gist became private or Bitly link broke
- Week 4 cumulative < 30: add note to CHECKIN.md; consider resend to non-responders

### 1.7 Adoptions Tab Schema

Log every confirmed adoption signal here.

| Col | Header | Values |
|-----|--------|--------|
| A | Signal_ID | A001, A002... |
| B | Date_Detected | Date you learned of the adoption |
| C | Organization | Org name |
| D | Constituency | From constituency list |
| E | Signal_Type | Curriculum Integration / Litigation Use / Policy Brief Citation / Training Integration / Referral / Public Comment Citation / Media Coverage |
| F | Domains_Referenced | Domain 56 / Domain 39 / Both |
| G | Evidence_Source | How you know (direct reply, web search, referral report) |
| H | Verification_Status | Confirmed / Probable / Unconfirmed |
| I | People_Reached_Est | Estimated number exposed (leave blank if unknown) |
| J | Network_Event | YES if this adoption will generate further referrals |
| K | Description | Free text |

**Day 60 target formulas**:
```
Confirmed adoptions:   =COUNTIF(H2:H100,"Confirmed")
Day 60 target status:  =IF(COUNTIF(H2:H100,"Confirmed")>=15,"TARGET MET","Confirmed: "&COUNTIF(H2:H100,"Confirmed")&"/15")
People reached:        =SUM(I2:I100)
People target:         =IF(SUM(I2:I100)>=100,"TARGET MET","Reached: "&SUM(I2:I100)&"/100")
```

### 1.8 Pre-Launch Verification Checklist

Complete these before May 28 morning:

**Google Sheets (20 min)**:
- [ ] Spreadsheet created, titled correctly
- [ ] All 7 tabs added with exact names
- [ ] 16 contacts imported from CSV template
- [ ] Auto-calculation formulas in Contacts tab
- [ ] Gist_Views tab headers in place
- [ ] Share link set to "Anyone with link — Viewer"
- [ ] Dashboard URL pasted into CHECKIN.md

**Bitly (10 min)**:
- [ ] drp-d56 created, resolves to Domain 56 Gist
- [ ] drp-d39 created, resolves to Domain 39 Gist
- [ ] Test click done on each link — click count incremented
- [ ] Bitly links inserted in Domain 56 email templates (replacing raw Gist URL)
- [ ] Bitly links inserted in Domain 39 email templates

**Google Alerts (5 min)**:
- [ ] Alert: "35-domain democratic renewal framework"
- [ ] Alert: "democratic renewal framework" healthcare OR litigation
- [ ] Alert: "democratic renewal framework" civil service
- [ ] Alerts routed to Gmail label: phase1-alerts
- [ ] Frequency set to: once per week digest

**Calendar (2 min)**:
- [ ] June 4 — "Day 7 checkpoint (Domain 56 send +7)"
- [ ] June 8 — "Day 7 checkpoint (Domain 39 send +7)"
- [ ] June 11 — "Day 14 mid-cycle check"
- [ ] June 27 — "Day 30 Phase 2 go/no-go"

---

## Section 2: Post-Send Tracking (Days 1–7)

### 2.1 Immediately After Each Send

Fill in the Contacts tab for each sent email within 1 hour of sending:
- Column H (Send_Date): today's date
- Column I (Delivery_Status): set to Unknown initially; update to Delivered when no bounce received within 6 hours, or Bounced if a bounce reply arrives

Check for bounces or auto-replies at these intervals:
- T+4 hours (same day)
- T+24 hours (next morning)

If you receive a bounce: immediately correct the email address (check the organization's website for current staff), update Delivery_Status to Bounced, find the corrected address, and record it in the Notes column. Resend to the corrected address and start a new row in the Contacts tab with the corrected address and new send date.

### 2.2 Domain 56 72-Hour Window (May 28–31)

The Tier 2 sends to Volcker Alliance, Democracy Forward, CREW, and Government Executive are time-sensitive. Check your email at:
- May 28 evening (T+4h): auto-replies, bounces
- May 29 morning (T+24h): first substantive replies
- May 30 (T+48h): second check
- May 31 (T+72h): 72-hour window assessment

**72-hour target**: 2 of 4 substantive replies (Score 3+) is a strong early signal. 1 substantive reply is moderate. 0 substantive replies by May 31 triggers the follow-up template in DOMAIN_56_TIER_2_DISTRIBUTION_MAY28_CHECKLIST.md.

### 2.3 Domain 39 72-Hour Window (June 1–4)

Domain 39 contacts receive emails May 30–June 3 (staggered by organization — see DOMAIN_39_JUNE1_PRE_PRODUCTION_CHECKLIST.md for schedule). The 72-hour check for Domain 39 runs June 3–6.

**Domain 39 priority note**: Georgetown CCF and NHeLP are the highest-value Domain 39 contacts for immediate signal — they are the most likely to reply within 72 hours because the June 1 HHS rule is directly operational to their work. A reply from either of these two contacts by June 4 is your first real Phase 2 signal regardless of Domain 56 results.

---

## Section 3: Weekly Monitoring Rhythm (Weeks 1–4)

### 3.1 Weekly Synthesis Template

Run once per week, starting June 2. Budget: 15–20 minutes. The Synthesis_Log tab holds these entries.

---

**WEEKLY PHASE 1 SYNTHESIS — Week [N]**

**Date range**: [Monday] — [Sunday]  
**Domain 56 days since send**: Day [X]  
**Domain 39 days since send**: Day [X] (or "not yet sent" if before June 1)

**FOUR KEY NUMBERS** (auto-fill from dashboard):

| Metric | This Week | Cumulative |
|--------|-----------|------------|
| Gist clicks — Domain 56 | | |
| Gist clicks — Domain 39 | | |
| Total replies received | | |
| Score 3+ replies | | |
| Tier 2 candidates flagged | | |
| Confirmed adoptions | | |
| Cross-org references | | |

**ENGAGEMENT PATTERNS** (2–4 observations):
- [Which domain or contact is generating the strongest signal?]
- [Any reply pattern — timing, tone, content type?]
- [Any organic amplification events — spike with no send correlation?]
- [Which framing or subject line is working?]

**PROBLEM SIGNALS** (or write "None detected"):
- [Delivery failures?]
- [Zero-engagement constituencies for 2+ weeks?]
- [Critique rate above 30%?]
- [Gist click velocity declining?]

**TIER 2 CANDIDATES** (or write "No new candidates"):
- [Any contacts who hit Score 3+ this week]
- [Natural follow-up for each candidate]

**CHECKPOINT STATUS** (check if applicable this week):
- [ ] Day 7 — run DAY_7_14_30_DECISION_TREES.md Tree 1
- [ ] Day 14 — run Tree 2
- [ ] Day 30 — run Tree 3 (Phase 2 go/no-go)

**DECISION PROMPT**:  
Based on this week's data, should we escalate to Tier 2 outreach for either domain?
- [ ] YES — [which contacts, which domain, what is the trigger evidence]
- [ ] NOT YET — [what threshold is still pending]
- [ ] NEEDS INPUT — [what you observed and what you cannot decide alone]

---

*Fill only the Four Key Numbers and Decision Prompt if time-constrained. The narrative sections are useful for pattern detection but not required for checkpoint decisions.*

---

### 3.2 Per-Domain Signal Log

After each weekly synthesis, add a one-line entry to WORKLOG.md in this format:

```
[Date] — Phase 1 Week [N] snapshot: D56=[X] clicks / D39=[Y] clicks. 
Replies=[Z total]. Score3+=[N]. [Any spike or adoption event]. 
Next checkpoint: [date and type].
```

This creates a searchable signal history in WORKLOG.md without requiring review of the full spreadsheet.

---

## Section 4: Per-Domain Monitoring Specifics

### 4.1 Domain 56 Monitoring (Civil Service Politicization)

**Distribution window**: May 28 (Tier 2: Volcker Alliance, Democracy Forward, CREW, Government Executive), plus Tier 1 contacts (Partnership for Public Service, GAP, AFGE, Protect Democracy, NTEU) if they were sent earlier.

**Key signal to watch**: Any reply from Democracy Forward is a litigation use signal — they are the primary litigation org in this send wave. A Score 4+ from Democracy Forward (PEER v. Trump brief interest) is a Phase 2 acceleration trigger regardless of overall metrics.

**Government Executive note**: Their response cycle is different — publication pitches take 5–10 business days. Do not score Government Executive as a non-response before June 10. If they respond positively (editorial interest in the op-ed pitch), that is a media amplification signal, not an adoption signal — log it in the Adoptions tab under Signal_Type = "Media Coverage."

**H.R. 492 markup window sensitivity**: The June 1–30 pre-recess markup window is the external news hook for Domain 56. Any Click spike in the Gist_Views tab during this window that cannot be traced to your outreach emails is an organic amplification signal from the legislative advocacy space — flag it and consider whether a follow-up resend to Tier 3 contacts (Brookings, NAPA) is warranted.

**Tier 3 trigger**: Send to Brookings Governance Studies and NAPA no later than June 7 regardless of Tier 2 response. The H.R. 492 window closes June 30 — Tier 3 recipients need the document by June 15 to act on it.

### 4.2 Domain 39 Monitoring (Healthcare Access as Democratic Infrastructure)

**Distribution window**: May 30 (Georgetown CCF, NHeLP) + June 1 (Brennan Center, IRG) + June 2–3 (Black Mamas Matter Alliance).

**June 1 hard stop context**: The HHS interim final rule on OBBBA Medicaid work requirements drops June 1. Organizations receiving Domain 39 before June 1 can frame the rule as a democratic participation event. Organizations receiving it after are in reaction mode. The Georgetown CCF and NHeLP sends on May 30 are the highest-leverage sends in the entire Phase 1 operation — they are positioned as ahead of the rule.

**Domain 39 is non-negotiable**: Domain 39 sends to all 5 contacts regardless of Domain 56 engagement metrics and regardless of the Day 30 checkpoint determination. The HHS deadline overrides Phase 2 sequencing decisions. See DAY_7_14_30_DECISION_TREES.md, all three trees — Domain 39 send appears as a mandatory action in every branch.

**Regulations.gov monitoring**: After June 1, run a weekly search on Regulations.gov for the OBBBA Medicaid work requirement docket. Look for any public comment (even after the formal comment period was bypassed) that cites the healthcare-as-democratic-infrastructure framing. This is your highest-value adoption detection channel for Domain 39.

**Maternal health signal**: Black Mamas Matter Alliance (C016) is the strongest maternal health signal contact. If they reply at Score 3+, that is evidence the framework resonates in the maternal health advocacy space — a distinct sub-constituency that could generate referrals to state-level maternal health coalitions.

---

## Section 5: Four-Number Checkpoint Protocol

Every checkpoint decision in Phase 1 is made with four numbers. Pull them from the dashboard before running any checkpoint tree.

| Number | Where to Find It | What It Measures |
|--------|-----------------|-----------------|
| (A) Total Bitly clicks | Gist_Views tab, Total_This_Week or Cumulative column | Passive engagement — someone followed a link |
| (B) Total reply count | Contacts tab, auto-calculation row | Active engagement — someone wrote back |
| (C) Score 3+ rate | Contacts tab, auto-calculation row | Quality of engagement |
| (D) Constituencies with any signal | Constituencies tab, count of rows with Score > 0 | Breadth of engagement |

Once you have these four numbers, open DAY_7_14_30_DECISION_TREES.md and run the appropriate tree. The trees require no additional information beyond these four numbers plus your Checkpoints tab log.

---

## Section 6: Cross-Organizational Reference Detection

A cross-org reference occurs when a contact tells you they forwarded the framework to another person or organization, or when someone contacts you citing a Phase 1 recipient as the source.

**When a cross-org reference occurs**:
1. Record in Contacts tab, Column S (Referral_Made) — the name or organization referred to
2. Add a row to Adoptions tab: Signal_Type = "Referral," Network_Event = YES, Verification_Status = Probable
3. When the referred party contacts you: update Verification_Status to Confirmed in Adoptions tab
4. Add a note to WORKLOG.md: date, referring org, referred org, domain

Three confirmed cross-org references is one of the four STRONG threshold criteria at Day 30. Every referral — even tentative ones ("I shared this with my colleagues") — counts as a half-referral until confirmed.

**Network multiplier signal**: If any single contact's referral leads to 3 or more inbound contacts, that is a network multiplier event. Score it at 3x the weight of a standard reply in your Phase 2 timing decision. A single network multiplier from Domain 56 or Domain 39 accelerates the entire Phase 2 timeline regardless of aggregate metrics.

---

## Section 7: Failure Recovery Protocol

If Day 14 shows weak trajectory (cumulative clicks < 10, reply rate < 10%), do not wait for Day 30 to act.

**Modification 1 — Framing revision**: Replace the framework overview pitch with a single-domain pitch specific to each contact's current work. For Domain 56 contacts still silent after Day 14: lead with the H.R. 492 markup window as the operational hook, not the democratic-design argument. For Domain 39 contacts silent after Day 14: lead with the specific HHS rule implementation discretion argument, not the full healthcare-democracy thesis.

**Modification 2 — Subject line revision**: The most common cause of low click rates is a generic subject line. Resend to non-responders with a news-hook subject line: "H.R. 492 Pre-Recess Window Now Open — [Domain 56 analysis]" or "HHS Work Requirement Rule Dropped — [Domain 39 democratic participation analysis]."

**Modification 3 — Channel shift**: If direct email is not producing replies after 14 days, shift to: (a) network intermediary approach — any contact who replied at Score 3+ is now an intermediary; ask them to share internally rather than you sending directly, (b) conference distribution — identify any upcoming conferences your Tier 1 contacts are likely attending and deposit materials in pre-read packets, (c) publication platform — submit a 1,200-word version of the most urgent domain to Just Security, Lawfare, or a democracy-focused newsletter. One published piece creates the social proof layer that direct outreach cannot.

---

## Section 8: Quick-Reference Summary

**Distribution schedule**:
- May 28: Domain 56 Tier 2 (Volcker Alliance, Democracy Forward, CREW, Government Executive)
- May 30: Domain 39 Tier 1 (Georgetown CCF, NHeLP)
- June 1: Domain 39 Tier 1 (Brennan Center, IRG) — HHS rule drops today
- June 2–3: Domain 39 Tier 1 (Black Mamas Matter Alliance)
- June 7 at latest: Domain 56 Tier 3 (Brookings, NAPA) — regardless of Tier 2 response

**Checkpoint dates**:
- June 4: Day 7 (Domain 56 reference date)
- June 8: Day 7 (Domain 39 reference date)
- June 11: Day 14 mid-cycle
- June 27: Day 30 Phase 2 go/no-go

**Non-negotiable sends (execute regardless of metrics)**:
- Domain 39 to all 5 contacts before June 3
- Domain 56 Tier 3 (Brookings, NAPA) by June 7
- Domain 39 follow-up if HHS rule creates a news hook (resend to orgs that did not reply)

**STRONG threshold (Day 30)**: Score 3+ rate >= 50% AND 4+ constituencies strong AND 3+ cross-org refs AND 2+ confirmed adoptions = activate Phase 2 same day.

**Single-contact override**: A Score 5 reply (formal adoption, citation, institutional integration) from any contact at any time overrides checkpoint dates. Execute Phase 2 pre-activation immediately. See DAY_7_14_30_DECISION_TREES.md Score 5 Override section.

---

*This document governs monitoring from May 28 through Day 30 (June 27). The companion files handle specific decision logic (DAY_7_14_30_DECISION_TREES.md) and reply categorization (REPLY_TRIAGE_FRAMEWORK.md). For historical framework context, see PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md in the root resistance-research directory.*
