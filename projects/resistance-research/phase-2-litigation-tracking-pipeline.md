# Phase 2 Litigation Tracking and Domain Intelligence Pipeline

**Specification version**: 1.0 — May 15, 2026
**Status**: Production-ready — activates on Wave 1 send completion
**Predecessor documents**: `phase-2-litigation-tracking-system.md` (institutional adoption tracking), `phase2-litigation-tracking.md` (FISA/VRA/redistricting monitoring), `post-distribution-adoption-framework.md` (diffusion theory and attribution methodology)
**Scope**: This specification covers the surveillance layer that runs *parallel* to adoption tracking — monitoring for legal and legislative developments that change what the domain documents say, not merely whether they are being read. The adoption tracking system in `phase-2-litigation-tracking-system.md` remains the authoritative spec for contact intelligence, attribution classification, and the Airtable CRM architecture. This document specifies the complementary signal intake, domain currency maintenance, and institutional citation tracking layers.

---

## Section 1: Litigation Signal Taxonomy — Per-Domain Matrix

The core design principle: not every domain generates litigation signal at equal velocity. Domains 1, 6, 16, and 29 are inside active circuit-level litigation cycles right now. Domains 15, 22, and 34 generate legislative signal faster than judicial signal. Domains 27 and 35 generate both simultaneously. Monitoring overhead is minimized by calibrating alert density to actual signal velocity per domain, not treating all 50+ domains identically.

### 1.1 High-Velocity Litigation Domains (check weekly)

These domains have active cases already in the tracker that are approaching decision. New filings appear frequently enough that a weekly CourtListener digest is necessary.

**Domain 1 / Domain 37 (Voting Rights, Electoral Interference)**
- Primary courts: SCOTUS (Callais, Turtle Mountain, Watson v. RNC — all expected by late June/July 2026), D.C. District (Trump EO election cases, LULAC v. EOP), Ninth Circuit (California voter data), Sixth Circuit (Michigan voter data)
- Case-level CourtListener alerts: All five named cases above
- New case search terms: `election executive order`, `voter roll`, `SAVE Act`, `CISA`, `Election Day preemption`
- Circuit split status: Eighth Circuit (no private right of action for VRA Section 2) vs. all other circuits — watch for cert grant in Turtle Mountain
- What constitutes a significant ruling: Any SCOTUS opinion narrowing Section 2; any circuit opinion eliminating private enforcement; any district court ruling on DOJ voter database

**Domain 6 (Judicial Independence)**
- Primary courts: D.C. Circuit (administrative removal cases), SCOTUS (Trump v. Slaughter — independent agency removal power, expected late June)
- The Slaughter ruling is the highest-stakes pending item for domain currency: if SCOTUS eliminates the for-cause removal protection for independent agency heads, Domain 6 Sections 3 and 4 require immediate supplement
- Case-level CourtListener alert: Trump v. Slaughter docket
- New case search terms: `Article III`, `judicial removal`, `good behavior clause`, `jurisdiction stripping`

**Domain 16 / Domain 39 (Immigration Enforcement, ICE Detention)**
- Primary courts: D.C. District (CASA v. DHS), Colorado District (Ramirez Ovando), Minnesota District (Hussen/Operation Metro Surge), Ohio District (ACLU Ohio), North Carolina District (ACLU-NC), Maryland District (Williamsport warehouse), 11th Circuit (Alligator Alcatraz)
- The 11th Circuit no-bond ruling (May 2026, per Session 929) deepened a circuit split — 2nd and 11th Circuits against no-bond, 5th and 8th uphold. This split is now the single most important pending litigation question for immigration detention
- New case search terms: `warrantless arrest`, `ICE detention`, `flight risk`, `habeas corpus`, `immigration detention NEPA`, `8 U.S.C. 1226`
- Watch for: Social Circle, Georgia preemption suit (anticipated DHS/DOJ filing)

**Domain 29 (Prosecutorial Weaponization)**
- Primary courts: Nashville (Crenshaw vindictive prosecution — ruling imminent as of May 9), SPLC indictment federal proceedings, any DOJ retaliatory filing
- The Nashville ruling is imminently expected. If Judge Crenshaw issues a dismissal on vindictive prosecution grounds, Domain 29 Section 4 gets a Causal adoption signal and an immediate supplement to the case law
- New case search terms: `vindictive prosecution`, `selective prosecution`, `DOJ indictment`, `retaliatory`, `18 U.S.C. 242`

**Domain 35 (SCOTUS Post-Loper Landscape)**
- This entire domain tracks SCOTUS term output — every opinion from now through late June is potentially domain-relevant
- Rather than case-level alerts, use SCOTUSblog's decision-day tracking and Democracy Docket's case page for the full docket
- Significant ruling threshold: Any opinion that expands Loper Bright beyond administrative law into constitutional deference; any opinion on independent agency removal; any ERISA/APA case that reshapes regulatory authority

### 1.2 Medium-Velocity Litigation Domains (check monthly)

These domains have active cases but on slower docket cycles, or are primarily legislative battlegrounds with judicial validation as a secondary track.

**Domain 14 (Criminal Justice, Consent Decrees)**
- Track: Police brutality consent decree defiance tracker, Seventh Circuit Castañon Nava pending ruling, Cleveland exit motion, 10th Circuit Denver ruling (circuit split on pattern-and-practice, Session 507 documentation)
- Monthly: Check for any DOJ motion to terminate existing consent decrees; any court granting or refusing termination. Consent decree tracker (`police-brutality-consent-decree-tracker.md`) already maintains this layer — monthly sync is sufficient
- Significant ruling threshold: Any circuit opinion holding that DOJ can unilaterally terminate a consent decree without court approval

**Domain 25 (FISA/Surveillance)**
- June 12, 2026 FISA Section 702 declassification deadline is next hard date
- Statutory rather than litigation signal: track Senate floor action, warrant amendment vote outcome, any long-term reauthorization passage
- Surveillance-tracking.md is the operational file — monthly sync

**Domain 27 (Academic Freedom)**
- Harvard funding freeze litigation, Columbia settlement monitoring, student visa revocation cases (Khalil, Oztürk, Mahdawi, Khan Suri)
- New case search terms: `student visa revocation`, `F-1 visa`, `academic freedom`, `Title VI`, `federal funding condition`
- Monthly check on accreditation weaponization rulemaking in Federal Register

**Domain 33 (State Legislative Autocratization)**
- Primary courts: State supreme courts in Missouri (Wise v. State — already decided adversely), Arkansas, Oklahoma, Florida (direct democracy restriction challenges); Vermont Supreme Court (Burlington noncitizen voting)
- Monthly: LegiScan state-level alerts for mid-decade redistricting bills introduced in any state beyond Missouri; MALDEF cert petition status

**Domain 34 (Congressional Fiscal Authority)**
- Not primarily a litigation domain — track through legislative signals (Section 2 below)
- If an OMB impoundment case is filed in D.C. District, add immediately
- Monthly: Check GAO bid protest decisions involving apportionment disputes

### 1.3 Low-Velocity Domains (quarterly review only)

Domains where the analytical framework is durable and unlikely to require update except on major systemic developments: Domains 4, 7, 8, 9, 10, 12, 13, 17, 18, 19, 20, 21, 22, 23, 26, 28, 30, 32, 36, 38, 40, 41, 43, 44, 47.

For these domains, a quarterly scan of the Just Security litigation tracker (https://www.justsecurity.org/107087/) captures any major developments without generating weekly alert fatigue.

Exception rule: if a low-velocity domain generates two or more Tier 1 contact inquiries in the same month, bump it to monthly monitoring for 90 days regardless of the default cadence.

---

## Section 2: Legislative Signal Tracking

### 2.1 Federal Legislative Signals

**API: Congress.gov API** (api.congress.gov)
- Free API key from api.data.gov
- Key endpoints: `/bill/{congress}/{billType}/{billNumber}` for bill detail and sponsor data; `/bill/{congress}` with `query` parameter for subject-area search; `/committee-report` for committee report text
- Update frequency: Bill data is updated six times per day; sponsors and co-sponsors update within 24 hours of floor action
- Search configuration: Set up keyword alerts for the following term clusters, each corresponding to a domain group

### 2.2 State Legislative Signals

**API: LegiScan** (legiscan.com/legiscan)
- Covers all 50 states and Congress
- Free tier: 30,000 queries/month — sufficient for targeted monitoring of 15-20 bills per domain across 10-12 priority states
- Priority states for monitoring: voting rights (Indiana, Alabama, Georgia, Texas, Florida, Oklahoma, Arkansas); state autocratization (Missouri, Wisconsin, Virginia, New York); cannabis/drug policy (California, Colorado, Michigan, Nevada)
- Alert configuration: LegiScan's email alerts trigger on committee hearings, amendments, and floor votes
- Sponsor tracking: LegiScan's `getSponsoredList` endpoint identifies model legislation coordination across states

**Significant legislative signals:**
- Same bill text in 3+ states within 60 days: flag as potential model-legislation coordination event
- State ballot initiative qualification: track via Secretary of State websites for priority states
- State supreme court ruling on redistricting/initiative: immediate entry in litigation tracker and domain update queue

---

## Section 3: Feedback Loop Design — Domain Update Protocol

### 3.1 The Supplement Model (not rewrite)

When domain documents have been cited at specific URLs, rewriting retroactively modifies what was cited. The supplement model preserves citation integrity while keeping analysis current.

Each domain maintains a `## Development Log` section:

```
### [YYYY-MM-DD] Session [NNN]: [Brief title]
**Trigger**: [What court ruling, legislative vote triggered this]
**Domain sections affected**: [Section numbers]
**Change type**: Supplement / Correction / Supersession
**Summary**: [2-4 sentences on what changed]
**Source**: [URL]
**Currency date updated**: Yes / No
```

**Change type definitions:**
- *Supplement*: New information extends existing analysis; prior analysis remains valid
- *Correction*: Factual error or outdated data corrected
- *Supersession*: Prior section's analytical conclusion no longer holds; requires versioning

### 3.2 Currency Dating

Every domain includes `**Research current through**: [date]` in the header. This signals staleness to recipients.

**Update rule**: Currency date advances only on full review, not mere supplement entries.

**Cadence by domain velocity:**
- High-velocity: monthly review
- Medium-velocity: quarterly
- Low-velocity: semiannually

### 3.3 Version Tracking

Gist-hosted documents maintain revision history at `[gist-url]/revisions`. Protocol:
1. Record current revision URL in Development Log before edit
2. Verify new revision appears in Gist history
3. For non-Gist documents, Git commit history serves the same function

### 3.4 Contact Notification Protocol

When domain receives Supersession-level update, institutional contacts warrant direct notification.

Notification threshold: Supersession only (not Supplement or Correction).

Notification format: One sentence identifying development, one on what changed, link to document. No more than three sentences total.

---

## Section 4: Institutional Citation Tracking

### 4.1 The Detection Problem

Most consequential citations will be invisible to passive monitoring. The detection architecture has three layers:
- Passive automated search (catches ~40% of citations)
- PACER/CourtListener full-text search (catches ~25% more)
- Active contact intelligence (catches remaining invisible citations)

### 4.2 Google Scholar Configuration

Set up Scholar alerts for:
- Framework title in exact quotes
- Distinctive analytical coinages unlikely to appear elsewhere
- Gist URL (expect 2-4 week indexing lag)

Scholar alert frequency: weekly digest (daily would create alert fatigue).

**Limitation**: Scholar indexes with days-to-weeks lag. For active case monitoring, CourtListener is more reliable.

### 4.3 CourtListener Full-Text Search for Brief Citations

Monthly manual search protocol (10 minutes):
- Query 1: `"Democratic Renewal"`
- Query 2: `"prosecutorial weaponization"`
- Query 3: `"warrantless arrest" "pattern and practice"`
- Query 4: `"state legislative autocratization"`
- Query 5: Any other distinctive coinage from recently distributed domains

Use courtlistener.com/recap/ (RECAP Archive), not main case search.

### 4.4 State Bar Databases and Legislative Records

Practical approach: 
- Google Alert for `[framework title] site:[state].gov` for states with confirmed adoption
- State legislature hearing transcripts: quarterly manual search for priority states
- Voting Rights Lab 2026 tracker for voting legislation citations

### 4.5 Overton Index

Overton.io indexes 21+ million policy documents and tracks citations within them. Cost: $99-$300/month. Optional until Tier 1 adoption in think tank/legislative sector justifies investment.

### 4.6 Active Contact Intelligence

For each Tier 1 engagement, structured check-in question: *"Since we last spoke, have you incorporated any domain analysis into briefs, testimony, research memos, or advocacy materials?"*

Only reliable detection mechanism for invisible citation layer.

---

## Section 5: Monitoring Checklist

### 5.1 Weekly (Tuesdays, 30-45 minutes)

**Court monitoring (15 minutes)**
- Review CourtListener alert digest
- Scan for ruling in high-velocity tracked cases
- Log immediately if ruling arrives; assess domain update need
- Check CHECKIN.md for pending urgent items

**Contact log (10 minutes)**
- Log replies in Airtable CRM
- Check for responses requiring 48-hour reply
- Note referral contacts (high-priority)

**Citation sweep (10 minutes)**
- Scan Google News alerts
- Scan Google Scholar weekly digest
- Classify any citations found

**Anomaly check (5 minutes)**
- Does any data point fall outside expected ranges?
- Note for investigation if yes

### 5.2 Monthly (First Monday, 3-4 hours)

**Court and legislation (60 minutes)**
- Run CourtListener RECAP searches (five queries)
- Run Congress.gov API queries
- Run LegiScan priority state checks
- Update litigation-tracker-2026.md
- Check Just Security tracker for new cases

**Domain currency review (60 minutes)**
- For high-velocity domains: confirm currency date <45 days old
- Run targeted review if stale
- Complete pending Development Log entries
- Update monthly tracker with domain dates

**Adoption and attribution (60 minutes)**
- Run monthly Airtable CRM activation rollup
- Run attribution_export.py
- Classify pending entries
- Identify sectors with high engagement/low adoption (maturation gap)
- Schedule check-in outreach if gap detected

**Monthly output (30 minutes)**
- Write WORKLOG entry: trajectory on/above/below target, named events, next priority
- Update PROJECTS.md tracker table with "last updated" dates

---

## Monitoring Overhead Estimate

| Task | Frequency | Time |
|---|---|---|
| Weekly court/contact/citation sweep | Weekly | 30-45 min |
| Monthly analytical review + WORKLOG | Monthly | 3-4 hours |
| Development Log entry (per Level 2+ signal) | As triggered | 15-30 min |
| Structured check-in outreach | Monthly | 20-30 min per contact batch |
| Overton manual check (if not subscribing) | Quarterly | 30 min |
| Annual link rot check in Sources | Annually | 2-3 hours |

**Total monthly overhead: 4-5 hours** (variance depending on signal volume; up to 7-8 hours in heavy SCOTUS decision weeks).

---

## Critical Pending Signals (as of May 15, 2026)

Monitor these every Tuesday — resolution will immediately trigger domain updates:

1. **Nashville Crenshaw ruling** — vindictive prosecution dismissal triggers Domain 29 update
2. **SCOTUS Callais** — Section 2 determination triggers Domains 1/33/37 cascade
3. **Trump v. Slaughter** — independent agency removal ruling triggers Domain 6 Supersession
4. **Watson v. RNC** — mail ballot grace period determination triggers Domain 1/37
5. **DEA Section 591 floor vote** — rescheduling block triggers Domain 42 update and Tier 1 contact notification

---

**Related files:**
- `phase-2-litigation-tracking-system.md` (institutional adoption tracking, Airtable CRM, attribution decision tree)
- `phase2-litigation-tracking.md` (FISA/VRA/redistricting background research)
- `litigation-tracker-2026.md` (active case log)
- `post-distribution-adoption-framework.md` (diffusion theory, adoption typology, version tracking)
- `CHECKIN.md` (Level 4 escalation filings)
