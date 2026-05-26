---
title: "Phase 1 Wave 1 Post-Distribution Impact Monitoring Dashboard"
subtitle: "Domains 56 + 39 — May 28 / June 1 Distributions"
created: 2026-05-26
version: 1.0
status: production-ready
scope: >
  Unified monitoring infrastructure for Domain 56 (Civil Service Politicization, send May 28)
  and Domain 39 (Healthcare Access as Democratic Infrastructure, send June 1).
  Five deliverables: Google Sheets template spec, Gist tracking protocol, reply triage
  framework, weekly synthesis template, and Day 7/14/30 decision trees.
gists:
  domain_56: "https://gist.github.com/esca8peArtist/8f11e868397921a4e6556b41196d1b1f"
  domain_39: "https://gist.github.com/esca8peArtist/131e8a94c955b973b87f7fb87d0f594b"
checkpoint_dates:
  domain_56_day_7: "June 4, 2026"
  domain_56_day_14: "June 11, 2026"
  domain_56_day_30: "June 27, 2026"
  domain_39_day_7: "June 8, 2026"
  domain_39_day_14: "June 15, 2026"
  domain_39_day_30: "July 1, 2026"
contacts_tracked: 16
companion_files:
  - phase-1-monitoring-sheets-template.csv
  - phase-1-monitoring-decision-trees.md
  - DOMAIN_56_DISTRIBUTION_STRATEGY.md
  - DOMAIN_39_DISTRIBUTION_STRATEGY.md
---

# Phase 1 Wave 1 Post-Distribution Impact Monitoring Dashboard

**Purpose**: Measure adoption of Domain 56 and Domain 39 in real time. Guide Phase 2 timing decisions. This document is the single reference for monitoring workflow from first send through Day 30.

**How to use this document**:
- Before first send: complete Deliverable 1 (create the Sheets tracker).
- Daily for first 7 days: run Deliverable 3 (reply triage) as signals arrive.
- Weekly (Sunday evening): complete Deliverable 4 (synthesis template).
- On Day 7 / 14 / 30: run Deliverable 5 (decision trees).

---

## DELIVERABLE 1 — Google Sheets Tracker: Setup and Schema

### 1.1 Sheet Structure

Create one Google Sheet with six tabs. Share view-access with any collaborators. Do not make it publicly editable.

**Sheet name**: `Phase 1 Wave 1 Monitoring — D56 + D39`

| Tab | Name | Purpose |
|-----|------|---------|
| 1 | Contacts | One row per outreach contact. Primary data entry. |
| 2 | Gist Views | Weekly Gist analytics snapshots. |
| 3 | Replies | Full reply log with triage classification. |
| 4 | Adoptions | Integration signals and Tier 2 pipeline. |
| 5 | Constituencies | Per-sector aggregation. |
| 6 | Checkpoints | Day 7 / 14 / 30 determination records. |

---

### 1.2 Tab 1 — Contacts Schema

**Column definitions** (one row per contact, 16 initial rows from `phase-1-monitoring-sheets-template.csv`):

| Col | Header | Type | Notes |
|-----|--------|------|-------|
| A | Contact_ID | Text | C001-C016 (see CSV for pre-seeded rows) |
| B | Full_Name | Text | Contact person's name |
| C | Organization | Text | Full org name |
| D | Domain | Text | "Domain 56" or "Domain 39" |
| E | Constituency | Text | Civil Rights / Labor / Academic / Healthcare / Elections |
| F | Tier | Text | Tier 1 / Tier 2 / Tier 3 |
| G | Email | Text | Verified address |
| H | Send_Date | Date | YYYY-MM-DD format |
| I | Delivery_Status | Dropdown | Pending / Sent / Delivered / Bounced / OOO |
| J | Open_Date | Date | Date email confirmed opened (Gist click or reply) |
| K | Click_Date | Date | Date Gist link first clicked (if Bitly used) |
| L | Reply_Date | Date | Date of first substantive reply |
| M | Reply_Category | Dropdown | Implementation / Question / Critique / Partisan_Misframe / None |
| N | Engagement_Score | Number | 0-5 per scoring rubric |
| O | Tier2_Candidate | Dropdown | YES / NO / MAYBE |
| P | Day_to_Open | Formula | `=IF(J{n}<>"", J{n}-H{n}, "")` |
| Q | Day_to_Click | Formula | `=IF(K{n}<>"", K{n}-H{n}, "")` |
| R | Day_to_Reply | Formula | `=IF(L{n}<>"", L{n}-H{n}, "")` |
| S | Notes | Text | Free-text field |

**Auto-calculation rows** (insert below last contact row, label clearly):

```
Row: "Domain 56 subtotals"
  Total sent (D56):     =COUNTIF(D:D,"Domain 56")
  Delivered:            =COUNTIFS(D:D,"Domain 56",I:I,"Delivered")
  Replies:              =COUNTIFS(D:D,"Domain 56",L:L,"<>")
  Reply rate (%):       =replies/delivered * 100
  Score 3+ count:       =COUNTIFS(D:D,"Domain 56",N:N,">=3")
  Score 3+ rate (%):    =score3+count/delivered * 100
  Tier 2 candidates:    =COUNTIFS(D:D,"Domain 56",O:O,"YES")

Row: "Domain 39 subtotals"  [same formulas filtered to Domain 39]
Row: "Combined totals"      [sum of D56 + D39 rows]
```

---

### 1.3 Tab 2 — Gist Views Schema

Track each Gist weekly. Pull data via GitHub API (see Deliverable 2) or manually (incognito browser check).

| Col | Header | Notes |
|-----|--------|-------|
| A | Week | "Week 1 (May 28 - June 3)", etc. |
| B | Snapshot_Date | Date you captured this row |
| C | D56_Gist_Views | Cumulative views on D56 Gist |
| D | D56_Gist_Views_Delta | `=C{n}-C{n-1}` |
| E | D39_Gist_Views | Cumulative views on D39 Gist |
| F | D39_Gist_Views_Delta | `=E{n}-E{n-1}` |
| G | D56_Gist_Forks | Integer |
| H | D39_Gist_Forks | Integer |
| I | D56_Gist_Comments | Integer |
| J | D39_Gist_Comments | Integer |
| K | Total_Clicks_This_Week | Bitly clicks if Bitly is used; else leave blank |
| L | Cumulative_Clicks | Running Bitly total |
| M | Notes | Anomalies, spikes, referral sources if available |

**Sparkline formulas** (insert in row 1 of each column):
```
D56 views trend:  =SPARKLINE(D2:D10, {"charttype","line"})
D39 views trend:  =SPARKLINE(F2:F10, {"charttype","line"})
```
These sparklines automatically draw the weekly trend as new rows are added.

**Baseline row** (Row 2, pre-distribution): Capture Gist views *before* first send (likely 0 or near 0 for D56/D39 since they are new). Label as "Baseline (pre-send)". Every delta is measured from this baseline.

---

### 1.4 Tab 3 — Replies Schema

Every reply gets its own row. Do not summarize — log each reply.

| Col | Header | Notes |
|-----|--------|-------|
| A | Log_ID | Auto-increment: R001, R002... |
| B | Contact_ID | Foreign key to Contacts tab |
| C | Date_Received | Date |
| D | Time_UTC | Time string |
| E | Domain | Domain 56 / Domain 39 |
| F | Reply_Type | See Deliverable 3 for five categories |
| G | Score | 0-5 |
| H | Escalate_Immediately | YES / NO |
| I | Response_Due | Date (leave blank if None category) |
| J | Response_Sent | Date |
| K | Referral_Made | Name of referred contact (if any) |
| L | Key_Quote | Short excerpt |
| M | Triage_Notes | Your assessment |

---

### 1.5 Tab 4 — Adoptions Schema

Only add a row here when there is evidence of actual use (not just a positive reply).

| Col | Header | Notes |
|-----|--------|-------|
| A | Adoption_ID | A001, A002... |
| B | Contact_ID | Foreign key to Contacts tab |
| C | Date_Observed | Date you confirmed this |
| D | Adoption_Type | Cited_In_Work / Used_In_Litigation / Forwarded_Network / Testimony / Op-Ed / Internal_Brief |
| E | Evidence_URL | URL to public evidence, or "Private (email)" |
| F | Verification_Status | Confirmed / Claimed / Suspected |
| G | Domain | Domain 56 / Domain 39 |
| H | Notes | Details |

---

### 1.6 Tab 5 — Constituencies Schema

Aggregate by sector. Update when you run the weekly synthesis.

| Col | Header | Pre-seeded values |
|-----|--------|-------------------|
| A | Constituency | Civil Rights / Labor / Academic / Healthcare / Elections |
| B | Domain | Domain 56 / Domain 39 |
| C | Tier1_Sent | Integer |
| D | Tier1_Replies | Integer |
| E | Tier1_Reply_Rate | Formula: D/C |
| F | Tier2_Sent | Integer |
| G | Score3plus_Count | Integer |
| H | Day7_Status | HOLD / MONITOR / ESCALATE / Not yet |
| I | Day30_Strong | YES / NO / Not yet |
| J | Day30_Moderate | YES / NO / Not yet |

---

### 1.7 Tab 6 — Checkpoints Schema

| Col | Header | Notes |
|-----|--------|-------|
| A | Checkpoint_Date | June 4, June 11, June 27, July 1... |
| B | Domain | Domain 56 / Domain 39 / Combined |
| C | Metric_A | Bitly clicks (or Gist delta if Bitly not used) |
| D | Metric_B | Total replies |
| E | Metric_C | Day 7 determination (Tree 1) or reply rate (Trees 2-3) |
| F | Metric_D | Score 3+ rate (Trees 2-3) or adoption count (Tree 3) |
| G | Determination | STRONG / MODERATE / WEAK / HOLD / MONITOR / ESCALATE |
| H | Action_Taken | Free text |
| I | Next_Checkpoint | Date |

---

## DELIVERABLE 2 — Gist View Tracking Protocol

### 2.1 The Two Methods

**Method A — GitHub API (automated, recommended if you are comfortable with curl)**

The GitHub Gist API returns view counts without authentication for public Gists.

```bash
# Domain 56 Gist stats
curl -s "https://api.github.com/gists/8f11e868397921a4e6556b41196d1b1f" \
  | python3 -c "import sys,json; g=json.load(sys.stdin); print('D56 forks:', g.get('forks',[]))"

# Domain 39 Gist stats
curl -s "https://api.github.com/gists/131e8a94c955b973b87f7fb87d0f594b" \
  | python3 -c "import sys,json; g=json.load(sys.stdin); print('D39 forks:', g.get('forks',[]))"
```

Note: GitHub's public Gist API does not expose view counts in the standard endpoint — it exposes forks and comments. View counts require authentication. See Method B for views.

**Authenticated view count query** (requires GitHub personal access token — gist scope):

```bash
# Set token once:
export GITHUB_TOKEN="your_pat_here"

# Query forks, comments, and last-updated (views not in API):
curl -s -H "Authorization: token $GITHUB_TOKEN" \
  "https://api.github.com/gists/8f11e868397921a4e6556b41196d1b1f" \
  | python3 -c "
import sys, json
g = json.load(sys.stdin)
print('D56 | Updated:', g['updated_at'], '| Comments:', g['comments'], '| Forks:', len(g.get('forks',[])))
"
```

**Method B — Manual weekly snapshot (10 minutes, no authentication required)**

1. Open an incognito browser window (eliminates your own view bias).
2. Navigate to each Gist URL. The view count displayed on GitHub is the cumulative total.
3. Record in the Gist Views tab.
4. Check the "Revisions" tab on each Gist for any edits you made — edits do not reset views but are worth noting.
5. Check the "Comments" section for any public comments.

---

### 2.2 Tracking Cadence

| Timing | Action | Method | Time |
|--------|--------|--------|------|
| Day 0 (before first send) | Capture baseline view count | B (manual) | 5 min |
| Day 3 | First post-send snapshot | B (manual) | 5 min |
| Day 7 (checkpoint) | Snapshot + record in Checkpoints tab | B (manual) | 5 min |
| Every Sunday after | Weekly snapshot until Day 60 | B (manual) | 5 min |
| Any day: spike detected | Immediate investigation | A (API) | 10 min |

---

### 2.3 Decision Thresholds

Record these in the Checkpoints tab. Each threshold tells you something specific.

**Gist views (Domain 56 Gist — D56)**:

| Cumulative views at Day 7 | Interpretation | Action |
|---------------------------|----------------|--------|
| 0 | Email may not have been opened | Check Replies tab for OOO; verify Bitly |
| 1–4 | At least one contact clicked | Delivery confirmed; below baseline threshold |
| 5–14 | Moderate engagement from direct contacts | On-track; record as MONITOR |
| 15+ | Network sharing likely (>5 direct contacts = 3 sends max) | Flag as STRONG signal; investigate who shared |

**Gist views (Domain 39 Gist — D39)** — same thresholds, measured from June 1 send:

| Cumulative views at Day 7 (June 8) | Interpretation |
|-------------------------------------|----------------|
| 0 | Delivery failure risk — investigate |
| 1–4 | Direct contact only |
| 5–14 | Moderate — on track |
| 15+ | Network amplification — flag in Checkpoints tab |

**Forks** (any count):

Any fork is a Tier 2 signal. Forks mean a contact is treating the Gist as working material. Log in Adoptions tab immediately.

**Comments** (any count):

Any GitHub comment is a high-value signal — public intellectual engagement. Log in Replies tab with score 4+ and escalate per Deliverable 3.

---

### 2.4 Template Query Block

Copy this into your notes each time you run a manual check:

```
GIST SNAPSHOT — [DATE] — Week [N]
Captured: [your local time / UTC]

D56 Gist (8f11e868...):
  Views (cumulative):    [___]
  Views (delta since last): +[___]
  Comments:              [___]
  Forks:                 [___]
  Last Revision Date:    [___]

D39 Gist (131e8a94...):
  Views (cumulative):    [___]
  Views (delta since last): +[___]
  Comments:              [___]
  Forks:                 [___]
  Last Revision Date:    [___]

Notes / anomalies:       [___]
```

Paste completed block into Tab 2 of the tracker and into `DISTRIBUTION_EXECUTION_LOG.md`.

---

## DELIVERABLE 3 — Reply Triage Framework

Every incoming reply is assigned to exactly one of five categories. Assign the category before you respond. The category determines the response timeline and template.

---

### Category 1 — Implementation Signal

**Definition**: Contact has already adopted Domain 56 or 39 content in their work, or is actively moving toward doing so. Examples: citing the document in a brief being filed, sharing it in a staff meeting, integrating the democratic-infrastructure frame into testimony, forwarding to three or more colleagues by name, requesting a formatted extract for an amicus brief.

**Distinguishing marker**: The contact's language shifts from evaluative ("this is interesting") to operational ("I'm using / I've shared / I'm forwarding this to"). The distinction is time-referenced action, not sentiment.

**Escalation threshold**: IMMEDIATE. Do not wait for a batch response cycle.

**Response action (within 24 hours)**:
1. Log in Replies tab (Score 4 or 5) and Adoptions tab.
2. Update Contacts tab — set Tier2_Candidate = YES.
3. Add STRONG SIGNAL note to CHECKIN.md with contact name, org, and what they said.
4. Reply same day. Offer:
   - A formatted extract tailored to their specific use case (brief, testimony, policy memo).
   - A call if they want to discuss methodology.
   - Referral to any companion domain that directly strengthens their use case.
5. If they cited the document publicly (blog post, filing, testimony), document the URL in Adoptions tab as Verification_Status = Confirmed.

**Response template for Category 1**:

> Thank you for this — I'm glad the democratic-infrastructure framing is directly useful for [their specific use]. I've attached a formatted extract that pulls the [specific section] into a standalone two-page brief format, which may be easier to circulate to [colleagues/co-counsel/policymakers]. Let me know if you need the citations in a different format or if there is a specific analytical angle that would strengthen [the brief / the testimony / the memo]. I'm also happy to schedule a call if it would be useful to talk through the methodology.

Customize the brackets. Keep it under 150 words. No forward-looking asks in this first reply.

---

### Category 2 — Question or Clarification Request

**Definition**: Contact is engaging with the content and wants more. Examples: asking about a specific statistic's source, requesting a different section, asking how Domain 56 relates to another issue they work on, asking about the methodology for a quantitative claim.

**Distinguishing marker**: The reply is oriented toward the document, not away from it. The contact wants more information, not less engagement.

**Escalation threshold**: Standard — respond within 5 business days. Batch responses acceptable (group similar questions from different contacts into one response session).

**Batch response schedule**: Every Tuesday and Friday. Set a calendar reminder.

**Response template for Category 2**:

> The [statistic / claim / methodology] question is a good one. [Answer the question directly in 2-4 sentences.] The primary source for that finding is [citation with URL if available]. If it's useful, [Section X of the full document] goes into more detail on [related topic]. Happy to send you a focused extract if that would be easier to work from.

Keep replies focused. Do not offer calls for Category 2 questions unless the question suggests the contact is moving toward implementation (which would upgrade them to Category 1).

**Note**: If two or more contacts ask the same question about the same claim, this is a framing signal. Add a note in the Checkpoints tab and consider whether the underlying claim needs a clarification addendum in the Gist.

---

### Category 3 — Critique or Methodology Challenge

**Definition**: Contact pushes back on a claim, methodology, or framing. Examples: challenging the causality in the rural hospital/voter turnout finding, questioning the V-Dem score for the US, disputing whether Schedule Policy/Career can be characterized as "democratic infrastructure attack."

**Distinguishing marker**: Critique is substantive (specific claim challenged with reasoning) versus partisan (generalized dismissal — see Category 4). A critic who names the specific section they dispute is engaging with the document on its terms.

**Triage by source credibility**:

| Critic type | Triage action |
|-------------|---------------|
| Academic / researcher (named institution) | Treat as high-value peer review. Engage fully. |
| Policy org staff (named org) | Engage with the specific claim. Medium priority. |
| Congressional staff | Engage immediately. Understand their objection before the markup window closes. |
| Anonymous or no institutional affiliation | Respond briefly. Do not invest deeply. |

**Response threshold**: Respond only when:
- The critique names a specific claim and offers a counter-argument.
- The critic has institutional standing relevant to your target constituency.
- The critique is substantive enough that a non-response would look like you cannot defend the claim.

**Do not respond when**:
- The critique consists only of conclusory disagreement ("this is wrong").
- The critic cannot be identified or does not have relevant standing.
- You have already responded once and the critic is repeating the same objection.

**Response template for Category 3**:

> Thank you for engaging with the [specific section / claim]. The [specific claim] rests on [primary source — brief citation]. You're right that [acknowledge any valid limitation]. The framing I've used is [X] because [methodological rationale in 1-2 sentences]. I'm happy to share the underlying [dataset / source document] if you want to evaluate the claim directly — the full citation is [URL]. If you see a different framing that better captures the dynamic, I'd be interested in hearing it.

Do not become defensive. If the critique identifies a genuine error, acknowledge it and correct the Gist with a revision note. Log the correction in the Notes column of the Contacts tab.

---

### Category 4 — Partisan Misframing

**Definition**: Reply frames the document as partisan political advocacy, attempts to recharacterize the research as attack material, or applies a left/right political framing to a structural analysis document.

**Detection patterns**:
- "This is Democrat talking points" or equivalent.
- Characterizing civil service merit protections as "protecting Biden appointees."
- Characterizing the healthcare-democracy nexus as "pro-Obamacare advocacy."
- Any framing that substitutes the party label for the institutional analysis.

**De-escalation response** (send once, do not re-engage):

> The document analyzes structural mechanisms — the merit civil service's function as democratic infrastructure predates and is independent of current party politics. The Pendleton Act was signed by a Republican president in 1883; Germany's constitutional civil service model exists under a Christian Democratic government. The democratic-infrastructure argument applies to any party that captures the merit system for political appointment purposes. I understand this framing may not be what you were expecting, but that's the analytical frame the evidence supports.

Do not apologize. Do not negotiate the frame. Log in Replies tab as Category 4, Score 1. No follow-up.

**If the misframing comes from a high-value contact** (congressional staff, senior org official): add a note to CHECKIN.md flagging that the democratic-infrastructure reframe may need to be made more explicit in the subject line or opening paragraph for that constituency. This is a framing revision signal, not a content problem.

---

### Category 5 — Non-Engagement or Bounce

**Definition**: No reply within 14 days (tracking only), or a hard bounce (delivery failure), or an autoresponder that does not indicate the contact will read the email later.

**Non-engagement**: Log Score 0 on Day 14. No action required unless the Day 14 decision tree (Deliverable 5) triggers a resend.

**Bounce** (hard):
1. Log immediately in Contacts tab — set Delivery_Status = Bounced.
2. Find correct email address: check organization website directly. If no direct address, try the media/press contact.
3. Resend within 48 hours to corrected address.
4. If 3+ hard bounces from a single send batch, pause all sends in that batch and run delivery diagnostics (check spam score, verify sender domain, test with a personal email first).

**OOO autoresponder**:
1. Log in Contacts tab — set Delivery_Status = OOO. Note the return date if stated.
2. Calendar a resend or follow-up for the stated return date + 2 business days.
3. Do not count OOO contacts in reply rate calculations until they have returned and the monitoring window has passed.

**Category 5 is not a failure signal on its own.** Many high-value contacts in academic and policy settings have 5-14 day response cycles. The signal becomes meaningful only at the Day 14 checkpoint.

---

### Escalation Summary Table

| Category | Score | Escalate? | Response Window | Batch OK? |
|----------|-------|-----------|-----------------|-----------|
| 1. Implementation Signal | 4-5 | YES — same day | 24 hours | No |
| 2. Question/Clarification | 3 | No | 5 business days | Yes (Tue/Fri) |
| 3. Critique | 2-3 | Only if high-value critic | 5 business days | No |
| 4. Partisan Misframe | 1 | No | Once, no follow-up | No |
| 5. Non-Engagement/Bounce | 0 | Only if bounce | Bounce: 48h; Silence: Day 14 | N/A |

---

## DELIVERABLE 4 — Weekly Synthesis Template

**Frequency**: Complete every Sunday at a time that works for you. Target: 15-20 minutes.

**Where to store**: Copy each completed instance into `DISTRIBUTION_EXECUTION_LOG.md` under a date header. Keep the blank template here for reuse.

---

### Blank Weekly Synthesis Template

Copy everything between the dashes for each new week:

```
---
PHASE 1 WAVE 1 WEEKLY SYNTHESIS — Week [N] — [Date Range]
Completed: [Your name / date / UTC time]
---

## 1. METRICS SNAPSHOT (5 minutes — pull from Contacts tab and Gist Views tab)

Distribution status:
  Domain 56 sent to:          [N] contacts (Tier 1: [N], Tier 2: [N])
  Domain 56 delivered:        [N]   Bounced: [N]   OOO: [N]
  Domain 39 sent to:          [N] contacts
  Domain 39 delivered:        [N]   Bounced: [N]   OOO: [N]
  Total delivered (combined): [N]

Engagement this week:
  New replies received:       [N]
  Cumulative replies:         [N]
  Combined reply rate:        [N]% (cumulative replies / cumulative delivered)
  Score 3+ replies (cumulative): [N] ([N]% of delivered)
  Score 4+ replies (cumulative): [N]

Gist views:
  Domain 56 Gist views (cumulative): [N]
  Domain 56 Gist delta this week:    +[N]
  Domain 39 Gist views (cumulative): [N]
  Domain 39 Gist delta this week:    +[N]
  Any forks this week:               [N]
  Any comments this week:            [N] (log separately in Replies tab)

---

## 2. KEY REPLIES THIS WEEK (5 minutes — pull from Replies tab)

[List each reply received this week. One line per reply.]

Format: [Date] | [Contact] | [Org] | Category [1-5] | Score [0-5] | "[Key quote, 1 sentence]"

Example:
  2026-06-02 | Jane Smith | Partnership for Public Service | Cat 1 | Score 4 | "I forwarded this to our policy team and three congressional offices."

Replies this week:
  [Date] | [Contact] | [Org] | Cat [N] | Score [N] | "[Quote]"
  [If none: "No replies this week. See Contacts tab for OOO statuses and Day N status."]

---

## 3. SENTIMENT TREND (2 minutes — assess based on cumulative replies)

Overall tone of engagement:
  Primarily supportive / Primarily questioning / Mixed / No signal yet

Category breakdown (cumulative to date):
  Category 1 (Implementation):    [N] replies
  Category 2 (Questions):         [N] replies
  Category 3 (Critique):          [N] replies
  Category 4 (Partisan Misframe): [N] replies
  Category 5 (No engagement):     [N] contacts

Notable shifts from last week:
  [Any change in tone, new objections surfacing, or consistent themes across multiple replies]

---

## 4. TIER 2 SIGNALS IDENTIFIED (2 minutes — pull from Adoptions and Contacts tabs)

New Tier 2 candidates this week:
  [Contact] | [Org] | [Why — specific signal] | [Next action by date]
  [If none: "No new Tier 2 candidates this week."]

Cumulative Tier 2 pipeline:
  Confirmed:  [N] contacts
  MAYBE:      [N] contacts
  Target by Day 30: 3-5 confirmed

---

## 5. ACTION ITEMS FOR NEXT WEEK (3 minutes)

[List only items you will actually do. Max 5.]

[ ] [Action] — [Contact / Domain] — Due: [Date]
[ ] [Action] — [Contact / Domain] — Due: [Date]
[ ] [Action] — [Contact / Domain] — Due: [Date]

Upcoming checkpoint dates:
  Domain 56 Day 7:  June 4, 2026
  Domain 56 Day 14: June 11, 2026
  Domain 39 Day 7:  June 8, 2026
  Domain 39 Day 14: June 15, 2026
  Combined Day 30:  June 27 - July 1, 2026

---
END SYNTHESIS WEEK [N]
---
```

---

### When to Shorten the Synthesis

If you are at Week 3 or later and no replies have been received (Category 5 for all contacts), collapse Sections 2 and 4 to one line each. Do not skip the Metrics Snapshot — it takes 3 minutes and keeps the historical record intact for Day 30 review.

---

## DELIVERABLE 5 — Day 7 / Day 14 / Day 30 Decision Trees

**How to use**: On each checkpoint date, pull the required numbers from the tracker (noted at the top of each tree). Follow the branches. Every branch ends in a named action. Do not skip steps.

**Checkpoint dates**:

| Domain | Day 7 | Day 14 | Day 30 |
|--------|-------|--------|--------|
| Domain 56 | June 4, 2026 | June 11, 2026 | June 27, 2026 |
| Domain 39 | June 8, 2026 | June 15, 2026 | July 1, 2026 |

Run each domain's tree independently. Record determination in the Checkpoints tab.

---

### TREE 1 — Day 7 Checkpoint (run separately for Domain 56 on June 4 and Domain 39 on June 8)

**Pull before starting**:
- (A) Gist views delta for this domain since send date (Tab 2, delta column for this week)
- (B) Total replies for this domain (Tab 1, Replies auto-calculation filtered to this domain)

```
PULL NUMBERS A AND B
        |
        v
STEP 1 — DELIVERY CHECK
        |
Any hard bounces in Contacts tab for this domain?
        |
      YES                              NO
        |                              |
  How many?                       Go to Step 2
        |
   3 or more             1 or 2
        |                  |
  PAUSE: Re-verify    Log bounce.
  all email addrs.    Find corrected
  Fix and resend.     address on org
  Restart Day 7       website. Resend
  clock from          to corrected
  corrected send.     address within
  Note in             48 hours.
  CHECKIN.md.         Continue tree.
        |
        v
STEP 2 — GIST VIEWS CHECK (Number A)
        |
    A >= 5         A = 1 to 4       A = 0
        |               |               |
  NETWORK          DIRECT         DELIVERY
  SIGNAL:          CONTACT        RISK:
  At least one     ONLY:          Were emails
  forward          Delivery        definitely
  likely.          confirmed       sent?
  Note in          but limited      |
  Checkpoints      amplification.    YES / UNSURE:
  as STRONG        Continue.        Check Gmail
  initial signal.  Go to Step 3.   Sent folder.
  Go to Step 3.                    If NOT sent,
                                   send now and
                                   restart clock.
                                   If sent but
                                   zero views:
                                   check spam
                                   folder.
                                   Note in
                                   CHECKIN.md.
        |
        v
STEP 3 — REPLY COUNT CHECK (Number B)
        |
    B >= 2         B = 1         B = 0
        |            |              |
  STRONG:        MODERATE:      WATCH:
  Record         Note in        Record.
  HOLD in        Checkpoints    Check
  Checkpoints.   as MONITOR.    again
  Continue       Check at       Day 10-12
  to Day 30.     Day 10-12.     (no formal
                 Go to Tree 2   checkpoint
                 on Day 14.     — just pull
                                number B
                                again).
                                If 0 at
                                Day 14:
                                run Tree 2
                                framing
                                review.
```

**Day 7 determination record** (Tab 6 Checkpoints):

| Result | Criteria | Record as |
|--------|----------|-----------|
| HOLD | A >= 5 AND B >= 2, no bounce issues | HOLD |
| MONITOR | A = 1-4 OR B = 0-1 (confirmed delivery) | MONITOR |
| ESCALATE | A = 0 with confirmed send, OR 3+ bounces | ESCALATE |

---

### TREE 2 — Day 14 Checkpoint

**Pull before starting**:
- (A) Cumulative Gist views delta since send date (Tab 2, sum all delta rows to date)
- (B) Total replies for this domain (Tab 1 auto-calculation)
- (C) Day 7 determination (Tab 6)
- (D) Overall reply rate (Tab 1 auto-calculation: replies / delivered)

```
PULL NUMBERS A, B, C, D
        |
        v
STEP 1 — DAY 7 STATUS CHECK (Number C)
        |
    C = HOLD        C = MONITOR         C = ESCALATE
        |               |                   |
  Go to Step 2.   Go to Step 2.        Delivery
                                       problem
                                       resolved?
                                           |
                                      YES     NO
                                       |       |
                                  Go to    ADD to
                                  Step 2.  CHECKIN.md:
                                           "Delivery
                                           failure
                                           unresolved
                                           — [domain]
                                           Day 14."
                                           Do not
                                           count
                                           undelivered
                                           in any
                                           threshold.
                                           STOP.
        |
        v
STEP 2 — CUMULATIVE CLICKS CHECK (Number A)
        |
    A >= 15        A = 5 to 14       A < 5
        |               |               |
  ON TRACK.       BELOW TARGET:     LOW SIGNAL:
  Go to Step 3.   Go to Step 3.     Consider
                                    resend to
                                    non-responders
                                    with revised
                                    subject line.
                                    See subject
                                    line options
                                    in Section
                                    5.4 of this
                                    document
                                    before
                                    resending.
        |
        v
STEP 3 — REPLY RATE CHECK (Number D)
        |
    D >= 20%       D = 10 to 19%      D < 10%
        |               |                 |
  STRONG START.  MODERATE:           LOW SIGNAL:
  Go to Step 4.  Go to Step 4.       Note WEAK
                                     trajectory.
                                     See WEAK
                                     actions
                                     below.
                                     Go to Step 4.
        |
        v
STEP 4 — EARLY ACTIVATION CHECK
        |
Any Score 5 reply received at any point?
(Score 5 = public citation, formal adoption, institutional use)
        |
      YES                         NO
        |                          |
  EARLY SIGNAL:             Any 2+ Score 4 replies?
  Execute                   (Score 4 = forward to
  Phase 2                   colleague, collaboration
  activation.               request)
  Add STRONG to                  |
  CHECKIN.md.             YES         NO
  Contact list                |          |
  is in                  PRE-DAY 30  No early
  DOMAIN_56 /            STRONG.     activation.
  DOMAIN_39              Flag in     Day 30 is
  _DISTRIBUTION          CHECKIN.md. next gate.
  _STRATEGY.md.          Continue.   Record in
  Begin Tier 2                       Checkpoints
  outreach                           tab and stop.
  within 48h.
```

**If Day 14 shows WEAK trajectory** (D < 10% AND A < 5):

Do not wait for Day 30. Diagnose before resending:
1. Did the subject line signal the domain deadline? (Domain 56: H.R. 492 markup window; Domain 39: June 1 HHS rule)
2. Did the opening sentence name the recipient organization's specific work?
3. Was the Gist link placed in the first 100 words of the email or buried at the bottom?

Subject line alternatives for a resend to non-responders:

- Domain 56: "Civil service analysis for your [H.R. 492 / PEER v. Trump / June markup] work — new framing"
- Domain 39: "Healthcare + voter registration connection — analysis for [their org's specific issue]"

Wait at least 72 hours between original send and resend. Do not resend to contacts who already replied.

---

### TREE 3 — Day 30 Checkpoint

**Pull before starting**:
- (A) Score 3+ reply rate (Tab 1: Score 3+ count / delivered)
- (B) Constituencies meeting Day 30 Strong threshold (Tab 5: count rows where Day30_Strong = YES)
- (C) Cross-org references confirmed (Tab 3: COUNTA of Referral_Made column)
- (D) Confirmed adoption signals (Tab 4: COUNTIF Verification_Status = Confirmed)
- (E) Gist click velocity in Weeks 3-4 (Tab 2: delta rows for Weeks 3 and 4 — above zero?)

```
PULL NUMBERS A, B, C, D, E
        |
        v
GATE 1 — STRONG THRESHOLD
Does A >= 50% AND B >= 3 AND C >= 2 AND D >= 1?
        |
      YES                     NO
        |                      |
  DETERMINATION:          Go to Gate 2.
  STRONG
        |
  Execute same-day:
  (1) Record STRONG in
      Checkpoints tab.
  (2) Add STRONG to
      CHECKIN.md with
      evidence.
  (3) If Domain 56 is STRONG:
      Begin Domain 56 Tier 2
      outreach (Volcker Alliance,
      Democracy Forward, CREW,
      Government Executive) within
      48 hours if not already sent.
  (4) If Domain 39 is STRONG:
      Begin Domain 39 extended
      outreach (Brennan Center,
      IRG, Black Mamas Matter)
      within 48 hours.
  (5) Begin Tier 2 law school
      pre-contact using social
      proof framing (cite specific
      adopting orgs by name).
  (6) Flag to CHECKIN.md:
      Phase 2 activation window
      open. User decision needed.
  STOP TREE. Phase 2 ready.
        |
        v
GATE 2 — MODERATE THRESHOLD
Does A = 20-49% OR B >= 2 OR C >= 1 OR D >= 1?
        |
      YES                     NO
        |                      |
  DETERMINATION:          Go to Gate 3.
  MODERATE
        |
  Execute within 24-48 hours:
  (1) Record MODERATE in
      Checkpoints tab.
  (2) Add MODERATE to
      CHECKIN.md.
  (3) Send Domain 39 regardless
      (June 1 HHS deadline
      overrides all thresholds —
      if not already sent, send
      immediately).
  (4) Extend Phase 1 monitoring
      to Day 60 for this domain.
  (5) Hold Tier 2 expansion
      until Day 60 unless a
      Score 4+ reply is received.
  (6) Prepare next domain for
      launch at Day 37-40.
  STOP TREE.
        |
        v
GATE 3 — WEAK SIGNAL CHECK
Does A < 20% AND B < 2 AND C = 0 AND D = 0?
        |
      YES                     NO (mixed signals)
        |                      |
  DETERMINATION:          DETERMINATION:
  WEAK                    INCONCLUSIVE
        |                      |
  Execute within            Add INCONCLUSIVE
  48 hours:                 to Checkpoints.
  (1) Record WEAK.          Pull specific
  (2) Add WEAK to           data point that
      CHECKIN.md.           is above
  (3) Pull                  threshold. If
      WEAK_OUTCOME          one Gist has
      _CONTINGENCY          10+ views and
      _PLAN.md from         another has 0,
      post-wave-1-          investigate
      monitoring/ and       asymmetry first.
      read Section 1        Revisit in 2
      (Diagnosis Protocol)  weeks.
      before any
      messaging change.
  (4) Do NOT send
      additional
      domains until
      WEAK is diagnosed.
  (5) Run the five-question
      diagnosis checklist
      (Section 6 below).
  STOP TREE.
```

---

### TREE 3 Supplement — WEAK Signal Diagnosis Checklist

If Day 30 produces a WEAK determination, run this five-question checklist before modifying any messaging or expanding distribution.

```
WEAK DIAGNOSIS CHECKLIST

1. Were emails actually delivered?
   Check: Any Gist views > 0? Any OOO replies?
   YES (some evidence of delivery) → continue checklist.
   NO (zero signals of any kind) → delivery failure.
     Action: Re-verify all email addresses from org websites.
     Re-send with a test email to yourself first.

2. Was the subject line specific to the recipient's work?
   Check: Pull your sent email. Does the subject line name
   a bill, case, or org-specific issue?
   YES → subject line is not the problem.
   NO → subject line is likely the problem.
     Action: Resend to all non-responders with revised
     subject line. Wait 14 days before Day 30 re-assessment.

3. Did the email open with the recipient's specific context?
   Check: Read the first two sentences of the email you sent.
   Do they name something specific to that org's work?
   YES → opening is not the problem.
   NO → framing gap.
     Action: Use org-specific hook sentences from
     DOMAIN_56_DISTRIBUTION_STRATEGY.md or
     DOMAIN_39_DISTRIBUTION_STRATEGY.md.
     Resend to non-responders with revised opening.

4. Was the Gist link placed prominently?
   Check: Is the Gist URL in the first 150 words of the email?
   YES → placement is not the problem.
   NO → buried link.
     Action: Move Gist link to second paragraph in resend.

5. Are there external factors suppressing response rates?
   Check: Is there a major news event dominating the
   orgs' attention this week? (Check: did civil service or
   healthcare news break this week that would occupy all
   staff bandwidth?)
   YES → timing, not content.
     Action: Wait 5-7 business days and resend with
     a one-sentence note tying the news to the document.
   NO → content or framing issue.
     Action: Consult WEAK_OUTCOME_CONTINGENCY_PLAN.md
     for full messaging revision options.
```

---

### Section 5.4 — Subject Line Options for Resends

Domain 56 resend subject lines (pick the one closest to the recipient's current news context):

- "Civil service merit system analysis for H.R. 492 co-sponsorship — [June markup window]"
- "DOGE workforce cuts — democratic-design analysis for your June testimony"
- "Schedule Policy/Career: new democratic-infrastructure framing for [org name]'s litigation"
- "Why 30 → 6 voting rights attorneys is a democratic accountability crisis, not just a staffing story"

Domain 39 resend subject lines:

- "HHS OBBBA work rule — healthcare-as-voter-infrastructure analysis for your June work"
- "NVRA + Medicaid enrollment: 50x gap in voter registration rates — new analysis"
- "Rural hospital closures and voter turnout: the causal mechanism, documented"
- "June 1 HHS rule — analysis your team can use before the rule drops"

---

## Quick-Reference Card

Print or pin this section for daily use during the monitoring period.

```
PHASE 1 WAVE 1 MONITORING — QUICK REFERENCE
=============================================
Domain 56 Gist:  https://gist.github.com/esca8peArtist/8f11e868397921a4e6556b41196d1b1f
Domain 39 Gist:  https://gist.github.com/esca8peArtist/131e8a94c955b973b87f7fb87d0f594b
Tracker:         "Phase 1 Wave 1 Monitoring — D56 + D39" (Google Sheets)
Send dates:      Domain 56: May 28 | Domain 39: June 1
Contacts:        16 total (D56: C001-C011, D39: C012-C016)

CHECKPOINTS:
  D56 Day 7:  June 4  | D39 Day 7:  June 8
  D56 Day 14: June 11 | D39 Day 14: June 15
  Combined Day 30: June 27 (D56) / July 1 (D39)

DAILY TRIAGE (when reply arrives):
  Cat 1 Implementation → respond within 24h, log Adoptions, flag CHECKIN.md
  Cat 2 Question       → batch response Tue/Fri
  Cat 3 Critique       → engage if named source; triage by credibility
  Cat 4 Partisan Frame → one reply, no follow-up
  Cat 5 Bounce/Silence → re-verify email if bounce; wait for Day 14 if silence

GIST SNAPSHOT: manual, incognito, weekly (Sunday)
  Record in Tab 2 and in DISTRIBUTION_EXECUTION_LOG.md

WEEKLY SYNTHESIS: Sunday evening, 15-20 min
  Deliverable 4 template → paste to DISTRIBUTION_EXECUTION_LOG.md
=============================================
```

---

*Created: May 26, 2026 | Version 1.0 | Companion files: phase-1-monitoring-sheets-template.csv, phase-1-monitoring-decision-trees.md*
