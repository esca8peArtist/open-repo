---
title: "Domain 51 — Contingency: SB-299 Fallback Plan"
created: "2026-06-04"
item: "Exploration Queue Item 63"
status: "production-ready"
trigger_window: "Activate before June 11 Gist creation if SB-42 path blocked"
cross_references:
  - DOMAIN_51_JUNE_9_12_EXECUTION_CHECKLIST.md
  - DOMAIN_51_CONTACT_STRATIFICATION_AND_TIMING.md
  - DOMAIN_51_RESEARCH_EXECUTION_CHECKLIST.md
---

# Domain 51 — Contingency: SB-299 Voter Registration Fallback Plan
## If the SB-42 Distribution Path Is Blocked Before June 11

*Prepared June 4, 2026. This document is the contingency layer. The primary path (SB-42 / California Fair Elections Act distribution) is fully staged and production-ready. This fallback activates only if specific trigger conditions below are met. Read Section 1 first — most "problems" with SB-42 do not require this fallback.*

---

## Pre-Read: What This Fallback Is NOT For

The following conditions do NOT require activating this fallback:

- The Gist URL becomes inaccessible (404): Recreate the Gist using `GIST_TEMPLATE_DOMAIN_56.md` as a pattern. 10-minute procedure. Do not activate this fallback.
- A California contact is unresponsive: This is expected. Unresponsive contacts do not mean the path is blocked.
- A contact email bounces: Verify the correct address and resend. Do not activate this fallback.
- The Montana Plan I-194 fails to qualify: This affects one postscript item on June 12, not the core research distribution.

**This fallback activates only if the SB-42 research itself is no longer useful for distribution** — meaning the ballot measure has been removed from the November 2026 ballot, or the research's central factual claims have been materially undermined before the sends go out.

---

## Section 1: Trigger Conditions — When to Activate This Fallback

### Trigger Condition A: SB-42 Removed from Ballot (Critical)
**What it looks like**: News reporting that a California court has removed the California Fair Elections Act from the November 2026 ballot (successful legal challenge to the ballot measure itself, not to the underlying SB-42 legislation).

**Numeric threshold**: Any credible news source (CalMatters, Los Angeles Times, San Francisco Chronicle, Sacramento Bee, Ballotpedia) reporting ballot removal confirmed by the California Secretary of State.

**When to check**: June 8 (pre-send verification day) and June 11 morning (before Wave 2 California sends).

**Activation timeline**: If confirmed before June 9, do not proceed with primary distribution. Instead pivot immediately to SB-299 fallback research planning. If confirmed between June 9 (after Wave 1 sends) and June 11, proceed with June 11 CA sends but reframe the email subject line from "for California Fair Elections Act campaign" to "California campaign finance analysis — structural research."

---

### Trigger Condition B: Research Core Facts Materially Undermined (High)
**What it looks like**: A major correction, retraction, or contradictory finding that undermines a primary claim in Domain 51 — specifically, if the FEC enforcement shutdown data (200+ days, zero fines FY2026) is publicly contradicted by an FEC action before June 9, or if the SB-42 signing or ballot placement is found to have been misreported.

**Numeric threshold**: Official FEC announcement of a fine assessment exceeding $1M (indicating enforcement quorum restored and operating), OR California Secretary of State withdrawal of SB-42 ballot certification.

**When to check**: June 8 (check FEC.gov for any posted enforcement actions; check sos.ca.gov for ballot measure status).

**Activation timeline**: If triggered before June 9, hold all sends and assess domain update requirements. A domain update (adding the new FEC action as a postscript, updating the enforcement timeline) is faster than pivoting to SB-299 — attempt domain update first before declaring the fallback activated.

---

### Trigger Condition C: Primary Source Unavailable (Low)
**What it looks like**: leginfo.legislature.ca.gov is completely inaccessible and the SB-42 bill text and legislative history cannot be independently verified by a recipient who checks the citation.

**Numeric threshold**: leginfo.legislature.ca.gov returns error for 24+ consecutive hours before the send date.

**When to check**: June 8 pre-send verification.

**Activation decision**: Do NOT activate the SB-299 fallback for this trigger alone. Use Ballotpedia (https://ballotpedia.org/California_Public_Funding_of_Elections_Measure_(2026)) and yesfairelections.org as substitute verification sources for SB-42 bill text. The primary source outage does not invalidate the research — substitute sources are sufficient. Activate the fallback only if all SB-42 verification sources are simultaneously inaccessible, which is an extremely unlikely scenario.

---

### Trigger Condition D: All Expert Contacts Unresponsive (Low — Does Not Require Full Fallback)
**What it looks like**: All 5 contacts are unresponsive by June 16 Day 7 checkpoint.

**Activation decision**: Do NOT activate the SB-299 fallback for this trigger. Unresponsive contacts do not indicate the research path is blocked — they indicate the contact strategy needs adjustment. Follow the phone follow-up protocol in `DOMAIN_51_EXECUTION_MONITORING.md` before considering any pivot.

---

## Section 2: The SB-299 Alternative Domain

### What SB-299 Is

California SB-299 (2023–2024 legislative session, authored by Senator Monique Limón and Senator Caroline Menjivar) is the Secure Automatic Voter Registration (Secure AVR) bill, also known as the "California New Motor Voter Program" upgrade. The bill passed the California Assembly and was sent to Governor Newsom in August 2024. It would upgrade the existing California Motor Voter program at the DMV to implement Secure AVR — automatically registering eligible Californians when they interact with DMV, with an opt-out mechanism — and could register over 4 million currently unregistered but eligible Californians.

**Note on bill number conflict**: "SB-290" (referenced in the original task brief as a fallback) is California SB-290 (2025–2026), which is a CalWORKs welfare-to-work bill authored by Senator Lola Smallwood-Cuevas — not a voter registration bill. The correct voter registration modernization fallback is SB-299 (2023–2024) and its successor legislation in the 2025–2026 session. Verify the current 2025–2026 automatic voter registration bill number at leginfo.legislature.ca.gov before drafting the fallback research.

**Why SB-299 is the correct fallback domain**: It addresses structural voter access — the same democratic accountability framework as Domain 51 — through a different mechanism (participation infrastructure vs. campaign finance architecture). The research contacts for voter registration modernization overlap partially with the Domain 51 contacts (League of Women Voters California covers both; Common Cause CA is active on voter registration) while adding distinct organizations (Brennan Center's voting rights team, National Voter Registration Act coalition organizations).

---

## Section 3: SB-299 Research Plan

### Can This Be Compressed to 4 Hours?
**Yes, with caveats.** Domain 51 required 8,500 words across 58 citations because it is a meta-analysis of a complex constitutional architecture. SB-299 / Secure AVR is a narrower, more technically defined research question — a 4,000–5,000 word document is sufficient for distribution purposes. Here is the compressed research plan:

**2-Hour Draft (minimum viable distribution document)**
This produces a 2,500–3,000 word focused brief, not a full domain expansion:

- Hour 0:00–0:30: Source staging
  - California SB-299 bill text: leginfo.legislature.ca.gov
  - Current automatic voter registration state tracker: Brennan Center (brennancenter.org/our-work/research-reports/automatic-voter-registration)
  - California Motor Voter program data: sos.ca.gov/elections/california-motor-voter
  - 4.7 million unregistered eligible Californians figure: verify at California Secretary of State
  - Brennan Center AVR impact analysis: brennancenter.org

- Hour 0:30–1:30: Draft structure
  - Section 1: The gap — 4.7M eligible but unregistered Californians and structural barriers
  - Section 2: SB-299 mechanism — what Secure AVR does and how it differs from current Motor Voter
  - Section 3: Evidence base — AVR impact in other states (Oregon, Colorado, Georgia post-2020)
  - Section 4: Opposition landscape — voter fraud objections and their empirical rebuttals
  - Section 5: Contact organizations and advocacy entry points

- Hour 1:30–2:00: Citations, verification, final polish (target: 20+ citations)

**4-Hour Full Brief**
This produces a 4,000–5,000 word substantive brief with fuller analysis:
Add to the 2-hour plan: (1) National Voter Registration Act compliance section (NVRA motor voter mandate and SB-299 as fulfillment); (2) Youth voter registration analysis cross-referencing Domain 54; (3) historical comparison (Motor Voter Act 1993 impact) and international comparison; (4) 2026 midterm timing analysis — at what date does AVR take effect to impact 2026 registration rolls.

---

## Section 4: SB-299 Alternate Contact Organizations

The following 5 organizations replace or supplement the 5 primary Domain 51 contacts if the SB-299 fallback is activated. League of Women Voters California and Common Cause California appear in both lists — no reintroduction is needed for them.

### Fallback Contact 1: Brennan Center for Justice — Voting Rights Team
**Organization**: Premier nonpartisan law and policy organization; leads national research on automatic voter registration.
**Contact**: justice@brennancenter.org (general) or use Contact Us form at brennancenter.org
**Primary contact area**: Democracy Program / Voting Rights team
**Website**: brennancenter.org/issues/ensure-every-american-can-vote/voting-reform/automatic-voter-registration
**Why this contact**: Brennan Center publishes the authoritative state-by-state AVR tracker and would recognize SB-299 research as extending their existing database.
**Response likelihood**: Tier A (40–50%) — research organizations with a direct interest in the subject area.

### Fallback Contact 2: League of Women Voters California (retained from primary list)
**Organization**: Already Tier B in Domain 51 list; covers both campaign finance AND voter registration.
**Contact**: lwvc@lwvc.org
**Engagement shift if fallback activated**: Lead with voter registration hook (SB-299 and the 4.7M unregistered eligible Californians) rather than campaign finance hook. LWV's NVRA lawsuit history makes voter registration their primary domain.
**Response likelihood**: Tier B (20–30%) — retained from primary list.

### Fallback Contact 3: Common Cause California (retained from primary list)
**Organization**: Already Tier B in Domain 51 list; actively advocates for automatic voter registration nationally and in California.
**Contact**: ca@commoncause.org
**Engagement shift if fallback activated**: Common Cause's national "One Voice" automatic voter registration campaign is directly relevant. Lead with the 4.7M gap figure rather than the ballot campaign hook.
**Response likelihood**: Tier B (25–35%) — slightly higher than primary list because AVR is a core programmatic priority, not a ballot campaign task.

### Fallback Contact 4: National Vote At Home Institute
**Organization**: Nonpartisan nonprofit advocating for accessible, secure voting by mail and automatic voter registration.
**Contact**: info@voteatHome.org (verify at voteathome.org/about/contact)
**Website**: voteathome.org
**Why this contact**: Vote-at-home and automatic voter registration are connected access infrastructure issues. If SB-299 passes and AVR updates registration rolls, vote-by-mail infrastructure must scale accordingly — a direct connection.
**Response likelihood**: Tier B (20–30%) — issue-aligned but not direct research intake organizations.

### Fallback Contact 5: Institute for Responsive Government
**Organization**: Nonpartisan organization focused on state-level election administration reform; actively supported SB-299 in the California Senate.
**Contact**: info@responsivegov.org
**Website**: responsivegov.org
**Twitter/X**: @IRGovorg
**Why this contact**: IRG issued a press release supporting SB-299 ("California Senate Advances Secure Automatic Voter Registration Legislation") and has existing public engagement with this bill — they already know the research terrain.
**Response likelihood**: Tier A (40–50%) — small organization with direct public stake in SB-299 outcome; high probability of engagement with external research that extends their public advocacy.

---

## Section 5: Fallback Timeline — Can the SB-299 Research Be Distributed by June 12?

**Short answer: No, if the full 4-hour research plan is needed. Yes, if a 2-hour focused brief is sufficient.**

### Scenario A: Fallback activated June 8 (before any sends)
- June 8: Activate fallback. Determine whether 2-hour brief or 4-hour brief is needed.
- June 9: Execute 2-hour brief research. Draft 2,500-word document. No Gist creation yet.
- June 10: Create Gist from brief. Verify SB-299 bill status (leginfo.legislature.ca.gov).
- June 11: Send to Brennan Center and Institute for Responsive Government (Tier A wave).
- June 12: Send to LWV CA, Common Cause CA, National Vote At Home Institute (Tier B wave).
- June 16: Day 7 checkpoint — same success thresholds as primary plan.

**Can this meet the July 1 deadline?** Yes. The July 1 deadline is the California ballot campaign messaging lock — SB-299 voter registration research is not time-bounded by the same ballot campaign calendar. The July 1 urgency is reduced in the fallback scenario; the correct hard deadline for SB-299 distribution is the 2026 California primary registration deadline or the Secretary of State AVR certification timeline.

### Scenario B: Fallback activated June 10–11 (after Wave 1 sends, before Wave 2)
- June 11: Hold CA sends. Execute 2-hour brief research.
- June 12: Create Gist. Send to Brennan Center and IRG.
- June 15: Send to LWV CA, Common Cause CA, National Vote At Home Institute.
- **Wave 1 sends (CLC, Issue One) already went out June 9** — those do not need to be withdrawn. The Domain 51 dark money document stands on its own. Only the California campaign framing needs adjustment.

### Scenario C: Fallback activated June 12 or later (after all 5 sends complete)
**Do not activate the fallback.** All sends are complete. The distribution window closes regardless of fallback status. Monitor responses through June 16 Day 7 checkpoint and July 1 as originally planned. If the CA ballot measure has been removed from the ballot, update the research document with a note and treat it as a structural analysis of campaign finance architecture rather than a ballot campaign resource.

---

## Section 6: Quick-Reference Fallback Decision Tree

```
START: June 8 or 9 morning — check SB-42 status

Is the CA Fair Elections Act still on the November 2026 ballot?
├── YES → Proceed with primary distribution. Do not activate fallback.
└── NO (confirmed removal by CA Secretary of State)
    └── Have the June 9 Wave 1 sends (CLC, Issue One) already gone out?
        ├── YES (sends complete) → Do NOT withdraw sends. Reframe CA sends
        │   as structural analysis, not ballot campaign support.
        │   Update email subject lines for June 11 sends.
        │   No full fallback pivot needed.
        └── NO (sends not yet sent)
            └── Is the research's core factual claims still accurate?
                ├── YES (FEC collapse, dark money data still accurate)
                │   → Proceed with sends but remove ballot campaign framing.
                │   Replace "for California Fair Elections Act campaign" in
                │   subject lines with "California campaign finance analysis."
                │   Do NOT activate full SB-299 fallback.
                └── NO (core facts materially undermined)
                    └── ACTIVATE SB-299 FALLBACK
                        → Execute Section 3 research plan.
                        → Use Section 4 alternate contacts.
                        → Follow Section 5 Scenario A timeline.
```

---

## Section 7: Source References for SB-299 Research

When executing the SB-299 fallback research, use these verified sources:

- **Bill text**: [SB-299 California New Motor Voter Program — California Legislature](https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=202320240SB299)
- **AVR state tracker**: [Automatic Voter Registration — Brennan Center for Justice](https://www.brennancenter.org/our-work/research-reports/automatic-voter-registration)
- **California Motor Voter existing program**: [California Motor Voter — Secretary of State](https://www.sos.ca.gov/elections/california-motor-voter)
- **IRG press release on SB-299**: [California Senate Advances Secure Automatic Voter Registration — Institute for Responsive Government](https://responsivegov.org/california-senate-advances-secure-automatic-voter-registration-legislation/)
- **4.7M unregistered eligible Californians**: [Secure AVR in California Could Mean 100,000+ More Young Voters/Year — The Civics Center](https://www.thecivicscenter.org/blog/california-needs-secure-automatic-voter-registration)
- **LWV CA Motor Voter FAQ** (existing program context): [CA New Motor Voter Law FAQs — LWV California](https://lwvc.org/ca-new-motor-voter-law-faqs/)

---

*Prepared June 4, 2026 — Exploration Queue Item 63. This fallback document is a contingency only. The primary SB-42 distribution path is fully production-ready. Fallback activation probability is estimated at less than 10% given current ballot measure status (confirmed qualified, signed by Governor Newsom October 2, 2025).*

*Primary path verification: [California Public Funding of Election Campaigns Measure (2026) — Ballotpedia](https://ballotpedia.org/California_Public_Funding_of_Elections_Measure_(2026)); [SB-42 Bill Status — California Legislature](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260SB42)*
