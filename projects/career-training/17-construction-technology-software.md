---
title: "Construction Technology and Software for the Residential General Contractor"
module: 17
discipline: ["technology", "software", "construction-management", "estimating", "field-tools"]
audience: "Residential GC — currently using spreadsheets, evaluating software investment"
status: "reference"
tags: [career-training, technology, software, Buildertrend, Procore, estimating, scheduling, BIM, field-tools, QuickBooks]
created: 2026-05-12
---

# Construction Technology and Software for the Residential General Contractor

> **Headline:** The single highest-ROI move a spreadsheet-and-paper GC can make is **photo documentation + a real job-costing setup in QuickBooks + one central construction-management platform**. Everything else is sequencing. Buying software does not fix a broken process — it accelerates whatever process you already have, good or bad.

---

## 0. Read This First — The Five Honest Rules

1. **Software does not fix process problems.** If your foremen don't fill out paper daily logs, they won't fill out digital ones either. Fix the habit first; then digitize it.
2. **One platform beats five "best-in-class" platforms.** Integration friction (re-typing the same data) eats every productivity gain. Pick the platform with 80% of what you need and accept its weaknesses.
3. **The mobile app is the product.** For a residential GC, the desktop UI is almost irrelevant. If the foreman, sub, and homeowner experience on a phone is bad, the tool will die — regardless of what the dashboard looks like.
4. **Expect a 60–90 day productivity dip.** Plan for it. Don't roll out new software during your busiest two months.
5. **Shadow spreadsheets are the leading indicator of failure.** If, six months in, your PM still has the "real" schedule in Excel and the software is "for the client," you have failed the implementation.

---

## 1. Construction Management Software — The Core Platform

### 1.1 What a CM Platform Actually Does

A modern construction management platform is a **system of record** that ties together five workflows that used to live in separate tools:

| Workflow | What it replaces | What "good" looks like |
|---|---|---|
| Project management | Whiteboards, Excel checklists, "you got the email?" | Task ownership, due dates, audit trail |
| Scheduling | Wall calendars, paper Gantt, text threads | Gantt with dependencies, sub notifications |
| Document control | Email attachments, USB sticks, "current set?" | Single source of truth, version control |
| Field communication | Group texts, phone calls, foreman knowledge | Daily logs, photos, time-stamped messages |
| Financials | Spreadsheets, QuickBooks-only | Budget vs. actual, change orders, draws, sub bills |

The point is not "more features." The point is **one place** where the answer to "what was approved, by whom, and when?" lives.

### 1.2 Major Platforms — Head-to-Head

| Platform | Best For | Typical Monthly Cost (2026) | Mobile App | Learning Curve | Sweet Spot |
|---|---|---|---|---|---|
| **Buildertrend** | Residential GCs, custom homes, remodels | $339–$1,099 (Essential / Advanced / Complete) + $400–$1,500 onboarding | Good, mature | Moderate–steep (lots of features) | 5–50 employee residential GC |
| **CoConstruct** (now folded into Buildertrend) | Custom home builders, selections-heavy work | Migrating users moved to Buildertrend tiers | N/A (legacy) | N/A | Legacy users only |
| **JobTread** | Budget-focused remodelers, smaller GCs | $149–$399 | Improving, simpler | Lower | 1–10 employee remodeler |
| **Procore** | Mid-to-large commercial; residential at >$5M volume | $10K–$60K+ /year (priced by annual construction volume — ACV) | Excellent | Steep | Larger residential, multi-family, mixed portfolio |
| **Houzz Pro** | Designer-builders, smaller remodelers, lead-gen focus | $49 entry, $399+ for full features | Good for design, lighter on field | Easy | Solo/small remodel with design component |

**Notes on the contenders:**

- **Buildertrend** is the **default choice** for residential GCs in the U.S. — roughly 20 years of development means almost every workflow a residential builder has thought of is in there somewhere. The cost of that maturity is **interface complexity**: new users frequently call it overwhelming. Expect 4–8 hours of structured onboarding per user.
- **CoConstruct** was acquired and merged into Buildertrend. New customers can't buy CoConstruct anymore. Existing users have been migrated to Buildertrend tiers; the **selections** workflow that made CoConstruct famous now lives inside Buildertrend.
- **JobTread** is the rising challenger. Clean UI, strong **budget-to-actual** reporting, transparent pricing. Weakness: scheduling and client portal are not as polished as Buildertrend's.
- **Procore** is genuinely industry-leading for commercial, but it is **priced and scoped for commercial**. If your annual revenue is under ~$5M, Procore is almost certainly overkill — both in cost and in the amount of fields/forms your team has to fill out.
- **Houzz Pro** is the right tool for a designer-builder who lives on the Houzz marketplace for leads. It is **not a serious field tool**: weak punchlist, weak schedule, weak sub management.

### 1.3 What to Look For (Buyer's Checklist)

When demoing any platform, drive the demo yourself through these seven items:

1. **Mobile schedule view for a sub.** Show me the screen a plumber sees on his phone when you reschedule rough-in.
2. **Client portal selection workflow.** Tile selection, allowance overage, owner signature — end to end.
3. **Change order approval chain.** From field-identified to owner-signed to QuickBooks line item.
4. **QuickBooks sync errors.** Ask to see the sync log. Every platform has sync issues; the question is how they are surfaced.
5. **Document version control.** Upload "Plans Rev 2," then "Plans Rev 3." What happens to subs who had Rev 2 on their phone?
6. **Daily log + photo upload offline.** Foremen often work in basements with no signal. What happens?
7. **Permissions granularity.** Can a sub see the schedule but not the budget?

### 1.4 Implementation Reality

**The 60–90 day curve is real.** A realistic rollout:

- **Weeks 1–2:** Configure account, chart of accounts mapping, user permissions, templates (proposal, contract, daily log).
- **Weeks 3–4:** Migrate ONE active project as the pilot. Run it in parallel with your existing process. Resist the urge to do all projects at once.
- **Weeks 5–8:** Add new projects only into the software (no parallel paper). Old projects finish on the old system.
- **Weeks 9–12:** Mandatory daily log + photo upload by foremen. Weekly "platform stand-up" — what's working, what's broken.

**The four most common failure modes:**

1. **Too many modules turned on at once.** Pick three workflows (e.g. schedule + daily log + change orders). Turn everything else off until those are habitual.
2. **The owner is the only user.** If only you log in, it's a $500/month CRM. Subs and foremen must be in the system.
3. **No data hygiene rules.** "Anyone can create a cost code" produces 400 garbage cost codes within six months.
4. **Skipping the QuickBooks mapping.** Cost codes in Buildertrend must mirror cost codes / items in QuickBooks. Get this wrong and you'll never trust the financial reports.

---

## 2. Estimating Software

### 2.1 The Estimation Workflow

```
Plans + Specs  →  Takeoff (quantities)  →  Pricing (unit cost × qty)
                                              ↓
                                          Markup (OH&P, contingency)
                                              ↓
                                          Proposal (client-facing)
                                              ↓
                                          Contract (executed)
                                              ↓
                                          Budget (project baseline)
```

Each arrow is a place where information gets lost or retyped. Good estimating software collapses arrows.

### 2.2 Takeoff Software Comparison

| Tool | Type | Strengths | Weaknesses | Cost (approx.) | Best For |
|---|---|---|---|---|---|
| **STACK** | Cloud, browser | Easy collaboration, drag-and-drop, residential-friendly | Per-user pricing scales fast | ~$2,000–$3,000 / yr / user | Residential, multiple estimators |
| **PlanSwift** | Desktop (Windows) | Fast point-and-click, accurate, mature | Desktop-only, dated UI, steeper learning curve | ~$1,800–$2,500 / yr | Commercial, single-estimator shops |
| **Bluebeam Revu** | Desktop/cloud hybrid | Best-in-class PDF markup; Studio sessions for live collaboration; takeoff via measurement tools | Not purpose-built for estimating — no built-in cost database | $240–$400 / yr (Basics → Core) | Every GC. Bluebeam earns its seat regardless of what other tool you use. |
| **Buildertrend Estimating** | Integrated | Lives next to your project budget; clean handoff to project | Weak takeoff tools — you'll do takeoff elsewhere and import quantities | Included in subscription | Residential GCs already on Buildertrend |
| **Hover** | Photo-based | Smartphone photos → 3D model with exterior dimensions; eliminates ladder measurements for siding/roofing | Exterior only; per-report pricing | $30–$80 / report | Roofers, siding, exterior remodelers |

**Recommendation for a typical residential GC:**
- Own **Bluebeam Revu** ($240/yr) — non-negotiable. It is the de facto language of the industry for PDF markup and you will receive marked-up sets from architects in `.bcx` format.
- Use **Buildertrend Estimating** for the cost side once you're on Buildertrend.
- Add **STACK** only if you have a dedicated estimator running 10+ bids/month.

### 2.3 Pricing Databases

| Database | What it is | Best Use | Caveats |
|---|---|---|---|
| **RSMeans** (Gordian) | Industry-standard cost data, updated annually, ~30,000 line items, **regional location factors** (e.g. SF Bay: ~1.30; Phoenix: ~0.92) | Plug numbers for trades you don't bid often (e.g. you're a remodeler asked to price a small elevator) | Lags 6–12 months behind real-time market; over-conservative on labor in tight markets |
| **Craftsman National Estimator** | Annual book + software, residential-focused | Solo remodelers, quick rule-of-thumb | Less granular than RSMeans; light on commercial assemblies |
| **Your historical data** | Closed-out project actuals | Anything you bid more than 3x/year | Requires discipline: every closeout, the actuals must be entered as a unit cost into a database |

**The truth about pricing databases:** They are a **sanity check**, not a primary estimating method. Your own historical unit costs — labor hours per LF of framing, dollars per SF of drywall, hours per fixture for trim plumbing — will always beat RSMeans for the work you do every week.

**How to build a unit-cost database from scratch:**

1. Close out one project. Pull actual labor hours from time tracking, actual material from QuickBooks vendor bills, actual sub costs from your subcontractor payments.
2. Divide by quantity installed (LF, SF, EA, hours).
3. Record in a Google Sheet with columns: trade, assembly, unit, my cost, date, project, conditions (new construction vs. remodel, occupied vs. unoccupied).
4. After 5 closed projects you will already trust your data more than any book.

### 2.4 Proposal Generation

A **good proposal** does five things:

1. Clearly states scope **by trade** (not by room — by trade, so subs can read their portion).
2. Lists **inclusions and exclusions** explicitly.
3. Lists **allowances** with the line-item budget (fixtures, finishes, appliances).
4. States **assumptions** (working hours, permit responsibility, utility connection, dump fees).
5. Has a **payment schedule** tied to verifiable milestones (not "30% on signing").

Buildertrend, JobTread, and Houzz Pro all generate decent proposals from the estimate. Procore's proposals are designed for commercial bid-day language and feel wrong for a homeowner.

### 2.5 Bid Management

Track at minimum:

| Metric | Why |
|---|---|
| Bids sent (count, $ volume) | Pipeline health |
| Win rate by lead source | Where your real channel is |
| Win rate by project type | What you actually do well |
| Days bid-to-decision | When to walk away |
| Reason lost (price, schedule, scope) | Fixing what you can fix |

If your annual revenue is under $3M, this can live in a single Google Sheet. Above that, you want this inside Buildertrend, JobTread, or a CRM (Pipedrive, HubSpot).

---

## 3. Scheduling Software

### 3.1 Why Schedules Fail (It's Not the Software)

The four reasons schedules don't work, in order of frequency:

1. **They're not updated.** A schedule that hasn't been touched in 10 days is fiction.
2. **They're too detailed.** A 600-line Gantt for a 4-month remodel is unmaintainable.
3. **Subs don't see them.** If your plumber doesn't get a push notification, the software didn't notify him.
4. **The PM doesn't believe them.** If the "real" schedule is in the PM's head and the software is for show, nothing in the software is true.

Software helps with #1 and #3. It cannot solve #2 and #4 — those are management problems.

### 3.2 Scheduling Tools Comparison

| Tool | Type | Strengths | Weaknesses | Cost | Best For |
|---|---|---|---|---|---|
| **Microsoft Project** | Desktop / Project Online | Most powerful Gantt, resource leveling, critical-path math | Steep learning curve; almost no one on site uses it | $10–$55 / user / month | Large custom homes, design-build, projects with 200+ activities |
| **Buildertrend Scheduling** | Integrated | Gantt + dependency linking; **sub notifications via email/text/app**; tied to daily logs | Less flexible than MS Project; gets cluttered above ~150 activities | Included | Residential GC's primary schedule |
| **JobTread Scheduling** | Integrated | Simple, fast to update, mobile-first | Light on dependency logic; no critical path | Included | Smaller remodelers |
| **Smartsheet** | Cloud spreadsheet + Gantt | Excel-like, collaborative, decent Gantt, integrates with anything | Not purpose-built for construction — you'll build the structure | $9–$32 / user / month | Multi-project portfolio view, owner-facing reporting |
| **FastTrack Schedule** | Desktop (Mac/Win) | Simpler than MS Project, attractive output | Limited collaboration, aging | ~$349 / user (one-time) | Solo PM who likes a polished printed Gantt |
| **Excel / Google Sheets 2-week look-ahead** | Spreadsheet | Free; everyone reads it; easy to print | Manual; no notifications | Free | Every project, regardless of what else you use |

### 3.3 The Two-Week Look-Ahead (The One Schedule That Actually Gets Used)

Even with Buildertrend running, **the schedule that drives field work is the 2-week look-ahead.** Structure:

| Day | AM | PM | Sub on site | Inspection | Notes |
|---|---|---|---|---|---|
| Mon 5/12 | Frame ext walls | Frame ext walls | Carpenters (2) | — | Lumber Friday — confirm |
| Tue 5/13 | Frame interior | Roof sheathing | Carpenters (3) | — | Crane 7 AM |
| Wed 5/14 | Roof sheathing | Window install | Carpenters (3) | — | Windows 8 AM Marvin |
| Thu 5/15 | Roof felt | Roof felt | Roofers | — | — |
| Fri 5/16 | Rough plumb | Rough plumb | Plumber (Mark) | — | — |
| Mon 5/19 | Rough plumb | Rough plumb | Plumber | — | — |
| Tue 5/20 | Rough elec | Rough elec | Electrician (Tom) | — | — |
| Wed 5/21 | Rough elec | Rough HVAC | Electrician + HVAC | — | Coordination meeting 7 AM |
| Thu 5/22 | Rough HVAC | Rough HVAC | HVAC | — | — |
| Fri 5/23 | Inspections | Inspections | — | **Rough framing, plumbing, electrical** | Confirm with city Tue |

This goes out **every Friday at 4 PM** to every sub. If you do nothing else, do this.

### 3.4 Sub Notification Tools

| Method | Audit trail? | Read receipt? | File attach? | Sub adoption |
|---|---|---|---|---|
| Group text | No | No | Limited | High |
| WhatsApp group | Limited | Yes | Yes | High |
| Email | Yes | Spotty | Yes | Moderate |
| Buildertrend sub portal | **Yes** | **Yes** | **Yes** | Low at first, climbs with training |
| Slack channel per project | Yes | Yes | Yes | Low (subs hate creating accounts) |

The honest answer: **most subs respond fastest to text.** Use Buildertrend for the audit trail and to send the 2-week look-ahead, but expect to follow up critical items with a text.

---

## 4. Document Management and Drawing Coordination

### 4.1 The Tools

| Tool | Strength | Cost | Use Case |
|---|---|---|---|
| **Bluebeam Revu** | PDF markup, **Studio Sessions** for live multi-party markup, takeoffs | $240–$400 / yr | Plan review, RFIs, markup, takeoff |
| **PlanGrid (now Autodesk Build)** | Field drawing access with version control; sheet-pinned punch items | $39 / user / month (Build entry) | Mid-to-large projects; teams already in Autodesk ecosystem |
| **Autodesk Build / BIM 360** | Full PM + drawing + BIM; deep RFI/submittal workflows | $39–$120+ / user / month per module | Larger residential, custom homes with BIM-capable design teams |
| **Buildertrend Documents** | Native to your project; integrates with daily logs and selections | Included | Residential GCs already on Buildertrend |
| **Google Drive** | Free, universal, dead simple | Free–$18 / user / month (Workspace) | Backup, archive, owner deliverables |

### 4.2 The One Thing That Matters: Drawing Revision Control

The single biggest source of field rework is **subs building from old drawings.** A working version-control discipline:

1. **One canonical folder location** for current plans. Bluebeam Studio project, Buildertrend Documents folder, or Google Drive `/Plans/CURRENT/`. Only one.
2. **Naming convention:** `2024-CarsonAve-Plans-Rev-04-2026-04-22.pdf`. Date in filename, revision number in filename. No exceptions.
3. **Old revisions move to `/Plans/SUPERSEDED/`** — do not delete them; you need the audit trail for change-order disputes.
4. **A "what changed" cover memo** with every revision. One paragraph. "Rev 4 changes: kitchen island moved 6" east; bath 2 shower relocated to north wall; structural beam at LR sized up to 5.5×11.875 LVL."
5. **Push notification to all subs** when a revision drops. Buildertrend can do this automatically when a document is replaced.

### 4.3 Google Drive Folder Structure for a Construction Project

```
/2024-CarsonAve-Smith/
├── 00-Contract/
│   ├── Signed-Contract-2026-02-14.pdf
│   ├── Insurance-Certificates/
│   └── Change-Orders/
│       ├── CO-001-Kitchen-Island.pdf
│       └── CO-002-Bath-Relocation.pdf
├── 01-Plans/
│   ├── CURRENT/
│   │   └── Plans-Rev-04-2026-04-22.pdf
│   ├── SUPERSEDED/
│   └── Markups/
├── 02-Specs/
├── 03-Permits/
├── 04-Submittals/
│   ├── 01-Windows-Marvin-Approved.pdf
│   └── 02-Cabinets-Pending.pdf
├── 05-RFIs/
│   └── RFI-Log.xlsx
├── 06-Subs/
│   ├── Plumbing-Acme/
│   ├── Electrical-Tom/
│   └── ...
├── 07-Daily-Logs/
├── 08-Photos/ (or use CompanyCam)
├── 09-Invoices-Draws/
└── 10-Closeout/
    ├── Warranties/
    ├── O-and-M-Manuals/
    └── Final-Lien-Releases/
```

Even if you also use Buildertrend, mirror critical documents to Drive. You will leave Buildertrend someday; you will not leave Google.

### 4.4 RFI Tracking

A working RFI log has these columns:

| # | Date Issued | From | To | Subject | Question | Response | Response Date | Days Open | Schedule Impact | Cost Impact |
|---|---|---|---|---|---|---|---|---|---|---|

Three rules:

- **Every RFI gets a number.** Sequential. Even verbal ones get logged.
- **Five-business-day response standard** by default. Faster if the trade is on site.
- **An open RFI past 10 days is a schedule risk.** Escalate.

In residential the RFI log can be a Google Sheet. Buildertrend has an RFI module; Procore and Autodesk Build have very mature ones. The discipline matters more than the tool.

---

## 5. Field Communication Tools

### 5.1 Daily Logs

The single highest-value field tool is the **daily log**, because it is the audit trail that defends you in change-order disputes and litigation.

A daily log must contain:

- Date, weather, on-site temperatures (matters for concrete, paint, asphalt)
- Subs on site, hours, number of workers
- Work completed
- Work scheduled but not started (and why)
- Deliveries received
- Visitors (owner, architect, inspector)
- Safety incidents
- Photos (minimum 10/day on active projects)
- Issues / RFIs raised

Buildertrend, Procore, and CompanyCam all do this. Paper works too — what matters is **every day, even slow days**.

### 5.2 CompanyCam

**This is the field tool with the clearest ROI for a residential GC.** Cost: ~$19–$29 / user / month, unlimited storage.

What it does:

- Every photo is **geotagged, timestamped, user-tagged, and auto-organized by project.**
- Photos are **searchable** by location, date, project, tag.
- Before/after comparisons in two taps.
- Project galleries are **shareable with owners** by link — no app install required.
- LiDAR-based measurement on newer iPhones.
- AI-generated report summaries from photos + voice notes.

Why it matters:

- **Insurance / litigation defense.** A geotagged photo from 7:42 AM on March 12 inside the basement before you started is unimpeachable evidence.
- **Owner communication.** "Here are 40 photos from today" is the most effective owner-relations tool ever invented.
- **Sub accountability.** "These are the photos from Friday — your crew left at 11:30, not 4:30 like the time sheet says."

CompanyCam **complements** Buildertrend — it does not replace daily logs, but it solves the "where are the photos" problem better than any built-in module.

### 5.3 Subcontractor Communication

| Channel | Audit Trail | Search | File Sharing | Sub Adoption | Best Use |
|---|---|---|---|---|---|
| Group text (SMS) | No | No | Photos only | High | Day-of urgent |
| WhatsApp group | Limited | Limited | Yes | High in some trades | Day-of, week-of |
| Buildertrend Messages | Yes | Yes | Yes | Moderate (requires login) | Schedule, change orders, anything documented |
| Email | Yes | Yes | Yes | Variable | Formal — contracts, approvals |
| Slack channel | Yes | Yes | Yes | Low for trades | Office-side only |

**A workable hybrid:** Text for urgency, Buildertrend for record. Anything that affects scope, schedule, or money goes through Buildertrend even if you also text about it.

### 5.4 Punch List Management

| Tool | Strength | Cost | When to Use |
|---|---|---|---|
| **FieldWire** | Drawing-pinned tasks, offline-capable, simple UI; widely adopted | $39 / user / month (Pro) | Any project with a drawing set; superb for new construction punch |
| **Buildertrend Punch List** | Integrated with project; owner can sign off | Included | Residential remodels where the owner is doing the walkthrough |
| **Autodesk Build / PlanGrid** | Best for projects already in Autodesk | $39+ / user / month | Larger projects already in Autodesk |
| **Paper + iPad photos** | Free | Free | Solo / small remodelers, simple punch lists under 20 items |

**What matters in a punch list tool:** (a) drawing-pin location, (b) photo per item, (c) assignment to a specific sub with notification, (d) status tracking with sign-off, (e) printable report for closeout.

---

## 6. Financial and Accounting Integration

### 6.1 QuickBooks Online vs. Desktop

| Dimension | QuickBooks Online | QuickBooks Desktop (Premier Contractor / Enterprise) |
|---|---|---|
| Job costing | Adequate (Plus or Advanced tier) | Stronger — purpose-built reports |
| Class tracking | Yes (Plus+) | Yes |
| Progress invoicing | Yes | Yes — more flexible |
| Item-level estimating | Light | Robust |
| Multi-user | Native cloud | Hosted (Right Networks etc.) — extra cost |
| Buildertrend / JobTread sync | **Native, mature** | Works via Web Connector — flakier |
| Cost | $35–$235 / month | ~$1,922 / year (Enterprise Contractor) + hosting |
| **Recommendation** | **Default for GCs under ~$10M revenue** | Larger volume, complex job costing, payroll in-house |

For most residential GCs in 2026, **QuickBooks Online Plus or Advanced** is the right answer. The cost is lower, the integration with construction platforms is better, and remote access from the field is native.

### 6.2 Job Costing in QuickBooks — The Single Most Important Configuration

This is the most consequential setup decision in a GC's accounting system. Done right, you have project-level P&L within minutes. Done wrong, you spend two days every quarter trying to figure out if you made money.

**The setup:**

1. **Every project = a Customer:Job** (or sub-customer in QBO). Format: `Smith-CarsonAve-2024`.
2. **Every expense is tagged to a Customer:Job** AND to an **Item** (cost code).
3. **Items are mapped to two-sided accounts:** an income account (e.g. `Construction Income — Framing`) and a COGS account (e.g. `COGS — Framing`).
4. **Class tracking** (optional but useful) for division (e.g. New Construction vs. Remodel) for company-level P&L by line of business.

**Cost code structure (CSI-aligned, simplified for residential):**

```
01 - General Conditions
02 - Site Work / Demo
03 - Concrete / Foundation
06 - Framing
07 - Roofing / Waterproofing
08 - Windows / Doors
09 - Drywall / Finishes
10 - Tile / Stone
11 - Cabinets / Millwork
15 - Plumbing
16 - HVAC
17 - Electrical
22 - Landscape / Exterior
26 - Owner Allowances
27 - Change Orders
28 - Permits / Fees
29 - Overhead Allocation
30 - Profit
```

Every Buildertrend cost code should map exactly to a QuickBooks Item with the same number.

### 6.3 Buildertrend + QuickBooks Sync

What syncs:
- Customers / Jobs
- Invoices (Buildertrend → QBO)
- Vendor bills (Buildertrend purchase orders → QBO bills)
- Payments received (QBO → Buildertrend)

What does NOT sync (commonly):
- Cost code edits made after sync
- Time entries (handled by TSheets / QB Time)
- Sub payment status if paid outside QBO
- Retention amounts (handled differently in each system)

**Common sync issues:**
- Duplicate customers (slightly different spelling)
- Items not mapped → expenses fall into "Ask My Accountant"
- Payments received in Buildertrend but recorded in QBO → double-count
- Edits made to a synced invoice in QBO that don't reflect back

**Rule:** decide where each transaction type **originates** and never edit it on the other side. E.g., invoices originate in Buildertrend; payments are recorded in QBO and sync back. Stick to it.

### 6.4 Chart of Accounts for a GC (Skeleton)

```
INCOME
  4000 - Construction Income
    4010 - New Construction
    4020 - Remodel / Addition
    4030 - Service / Repair
    4040 - Change Orders
    4050 - Allowance Reconciliation

COST OF GOODS SOLD
  5000 - Direct Job Costs
    5010 - Materials
    5020 - Subcontractors
    5030 - Direct Labor (field, by job)
    5040 - Equipment Rental
    5050 - Permits & Fees
    5060 - Disposal
    5070 - Job Site Utilities
  5100 - Cost of Labor (job-coded payroll)
  5200 - Workers Comp (job-coded)
  5300 - Liability Insurance Allocation

OVERHEAD
  6000 - Office Salaries (non-field)
  6100 - Office Rent / Utilities
  6200 - Vehicle (truck, fuel, maint)
  6300 - Software / Subscriptions
  6400 - Marketing / Advertising
  6500 - Professional Fees (legal, accounting)
  6600 - General Insurance
  6700 - Bank / Merchant Fees
```

**Critical principle:** anything you can charge to a **specific job** belongs in COGS (5000s). Overhead (6000s) is only for unallocable cost. Get this wrong and your project-level gross margin is meaningless.

### 6.5 Invoicing and Draws

A **progress billing** workflow:

1. Approved schedule of values (SOV) at contract signing.
2. At month end (or milestone), measure % complete by line.
3. Generate **AIA-style G702/G703** or its residential equivalent (Buildertrend has this).
4. Net new billing = (% complete × line total) – (previously billed) – (retainage held).
5. Submit with backup: lien releases from subs, photos of completed work, inspector signoffs.

**Retainage** (typical residential: 5–10% held until substantial completion) must be tracked on a **separate ledger** — most accounting failures in GC firms involve retainage that nobody remembered to bill at the end.

### 6.6 Lien Waivers

Lien waiver management is one of those problems that doesn't matter until it does — and when it does, it's a $50,000–$200,000 problem.

| Approach | Cost | Best For |
|---|---|---|
| Manual (Word templates, PDF, email) | Free | <10 subs per project, <$1M projects |
| **Levelset** | $149+ / month | Multi-project, multi-state, larger volumes |
| **Textura** (Oracle) | Enterprise pricing | Large commercial — rare in residential |
| Built into Buildertrend / Procore | Included | Most residential GCs |

A workable manual process:
- **Conditional waiver** sent with the sub's draw request (covers payment when received).
- **Unconditional waiver** received with check delivery (covers payment now received).
- Both stored in `/Subs/[SubName]/Waivers/` for the project.

For residential GCs in California, where lien law is contractor-friendly but homeowner-protective, get this right — it is a real source of homeowner disputes.

---

## 7. Time Tracking and Payroll

### 7.1 Time Tracking Comparison

| Tool | Strengths | Weaknesses | Cost (2026) | Best For |
|---|---|---|---|---|
| **QuickBooks Time** (formerly TSheets) | Native to QuickBooks; clean payroll handoff; good GPS | Photo features feel bolted on; geofencing is decent not great | $10/mo base + $8/user/mo (Premium) | QBO-based GCs |
| **ClockShark** | Best-in-class geofencing for crews; built for construction; simple foreman experience | Less mature reporting | $40/mo base + $9/user/mo | Mid-size construction (10–100 employees) |
| **Busybusy** | Photo-first (construction-grade), GPS breadcrumbing, equipment tracking, project budgets | Smaller ecosystem of integrations | Free tier; $11–$15/user/mo paid | Construction-only firms; equipment-heavy contractors |
| **Buildertrend Time Tracking** | Integrated with project / cost codes | Less robust than dedicated time apps | Included | Smaller GCs already on Buildertrend |

**The honest comparison:**
- Pure QBO shop, small crew → **QuickBooks Time**. Friction-free.
- Multiple crews across multiple jobsites, geofence-critical → **ClockShark**.
- Heavy equipment, want photo + GPS breadcrumbing → **Busybusy**.

What matters more than the tool: **time entries must be job-coded and cost-code-coded at clock-in**, not at week-end. If a framer clocks in to "Smith Project" with cost code "06-Framing," labor flows straight to your job cost report. If he clocks in to "Smith Project" with no cost code, you have data garbage.

### 7.2 Payroll Comparison

| Platform | Strengths | Weaknesses | Cost | Best For |
|---|---|---|---|---|
| **Gusto** | Best UX, easy onboarding, good benefits admin, contractor 1099 support | Weaker construction-specific features (certified payroll is extra) | $40 + $6/employee/mo (Simple) → $80 + $12 (Plus) | Solo GCs, small crews |
| **ADP RUN** | Powerful, full HR suite, multi-state | More expensive, sales-driven pricing, dated UI | Quoted; typically $150–$400/mo for small GC | 20+ employees, multi-state |
| **QuickBooks Payroll** | Native to QBO; cheap; adequate | Weak HR features; certified payroll add-on extra | $50 + $6/employee/mo (Core) → $130 + $11 (Elite) | QBO shops who want one bill |
| **Paychex** | Strong construction industry support; certified payroll capable; workers' comp pay-as-you-go is mature | Pricing opaque; can feel old-school | Quoted | Public-works contractors, prevailing wage |

### 7.3 Workers' Comp Pay-As-You-Go

This is one of the **highest-ROI integrations** a GC can set up and it's almost universally ignored.

**The problem:** traditional workers' comp is paid as an estimated annual premium based on estimated payroll. At year-end, the carrier audits actual payroll. If your actual was higher (you had a busy year), you owe a big check. If your actual was lower, you wait for a refund.

**The fix:** Pay-as-you-go integration. Your payroll platform (Gusto, ADP, Paychex, QB Payroll) reports **actual wages per class code each pay period** to the workers' comp carrier (e.g. The Hartford, Travelers, AmTrust, Employers, Pie). Premium is debited in real time based on actual payroll.

**Why this matters in construction:** worker class codes vary wildly (carpenter at ~7%, roofer at ~25%+). If you're doing certified payroll under one classification but actually framing roofs under another, year-end audits can be catastrophic. Real-time reporting eliminates surprise.

**Action item:** when you switch payroll providers, **insist on pay-as-you-go integration** with your workers' comp carrier. If they don't support it, change one of them.

### 7.4 Certified Payroll (California Public Works)

If you bid public-works projects in California you must register with the **DIR (Department of Industrial Relations)** under SB 854, pay prevailing wage, and submit **certified payroll reports** electronically.

- **DIR eCPR system** (free) — direct online entry or XML upload to the DIR Public Works portal. Submissions due **at least monthly**, sometimes weekly per contract.
- **LCPtracker / LCPcertified** — the dominant third-party platform. Generates the DIR-compliant XML, manages multi-agency reporting (some cities require their own submission in addition to DIR), tracks apprenticeship hours, and produces CAC-2 forms.
- **Elation Systems** — alternative used by several CA agencies and Caltrans.
- **Sunburst Time Tracker / Certified Payroll Solution** — popular QuickBooks add-on for small contractors who don't want the LCPtracker subscription.

If you are bidding **any** public work, install LCPtracker before the first pay period. Trying to back-fill certified payroll a month in is the surest way to a stop-work order.

---

## 8. BIM and 3D Modeling for Residential

### 8.1 The Tools

| Tool | Type | Cost | Best For |
|---|---|---|---|
| **SketchUp** | Push/pull 3D modeling | $349/yr (Pro) | Visualization, simple coordination, marketing renderings |
| **Revit** | Full BIM (parametric) | $2,945/yr (Autodesk) | Custom homes >$2M, design-build with architect partner, anything with structural steel |
| **Chief Architect** | Residential-specific BIM | $2,995 one-time (Premier) or $199/mo | Designers and design-build GCs; generates real construction drawings |
| **Matterport** | 3D laser scan / photogrammetry | $99–$309 / mo (depends on plan) + ~$3K camera (Pro2) or use Pro3 ~$5,995 | As-builts for remodels, marketing, owner documentation, insurance |
| **Hover** | Photo-to-3D exterior | Per-report ($30–$80) | Exterior measurement only |

### 8.2 When BIM Matters in Residential (And When It Doesn't)

**It matters when:**
- Custom home over ~$2M with complex structure (steel moment frames, long spans, unusual geometry).
- Mechanical/plumbing routing in tight conditions where clash detection saves real rework (radiant slab + structural, multi-level mechanical chases).
- Design-build with an in-house architect — model-once, document-once efficiency.
- You're selling the model to the owner as a marketing/value differentiator.

**It doesn't matter when:**
- Standard 2,500 SF spec home with conventional framing and clear MEP runs.
- Kitchen / bath remodels (the value is in the **as-built scan**, not the design model).
- Production / tract homes (the design is already amortized).

### 8.3 Matterport — The Single Most Useful 3D Tool for Residential

Matterport (or competitors like CupixWorks, OpenSpace, DroneDeploy) generates a **walkable 3D scan** of a space. For a residential GC:

- **Pre-demo as-built** — scan before tearing into walls; preserves a record of what was there for change-order disputes.
- **Inside-the-wall documentation** — scan rough plumbing/electrical before drywall. Six months later, when the owner asks where the closest wire is for a new sconce, you can find it.
- **Punch list reference** — owner walkthroughs become asynchronous; client tours the space remotely and tags issues.
- **Marketing** — every closed project becomes a portfolio asset.

Cost is real (~$5K camera + $99–$309/mo plan) but the per-project value is high. If you do 5+ remodels a year over $250K each, it pays back inside a year.

---

## 9. Mobile Apps for the Field

### 9.1 Apps That Foremen Actually Use

| Category | App | Cost | Why |
|---|---|---|---|
| Concrete testing | **ACI Concrete Field Testing** | Free | Slump, air, temp logging; emails to office |
| Safety | **iAuditor (SafetyCulture)** | Free–$24/user/mo | Toolbox talks, JHAs, inspections — OSHA evidence |
| Smart-phone measurement | **Magicplan** | Free–$59/mo | Room scanning, layouts; useful for restoration |
| Measurement (LiDAR) | **Canvas** | $179/scan or subscription | Higher accuracy for remodel as-built |
| Code reference | **ICC Digital Codes Premium** | $59–$595/yr | IRC/IBC/CRC searchable on phone |
| Electrical reference | **NEC Quick Card / NFPA 70** | $5–$200 | NEC lookup in field |
| PDF markup | **Adobe Acrobat / Notability / GoodNotes / PDF Expert** | $0–$13/mo | Field markup of plans |
| Communication | **WhatsApp / Slack / Teams** | Free–$12.50/user/mo | Sub coordination |
| Photo docs | **CompanyCam** | $19–$29/user/mo | (see §5.2) |
| Time tracking | **QB Time / ClockShark / Busybusy** | (see §7.1) | (see §7.1) |

### 9.2 The Six-App Foreman Loadout

For a working residential foreman, install on the iPhone/iPad:

1. **Buildertrend (or JobTread)** — schedule, daily log, RFIs
2. **CompanyCam** — photos
3. **QB Time / ClockShark** — clock-in for crew
4. **Bluebeam Revu / PDF Expert** — plans
5. **iAuditor** — safety inspections / toolbox talks
6. **ICC Digital Codes** — code lookup

This is enough. Adding a seventh app reduces adoption of all six.

---

## 10. Technology Implementation Strategy

### 10.1 Stack Recommendations by Company Size

| Size | Project Mgmt | Estimating | Field | Accounting | Time | Total Approx. Monthly |
|---|---|---|---|---|---|---|
| **Solo / 1–2 person** | Google Workspace + simple proposal tool (e.g. Houzz Pro Essential) | Bluebeam Revu + Excel | CompanyCam | QBO Plus | QB Time (1 user) | ~$200–$400 |
| **3–10 employees** | Buildertrend Essential **or** JobTread | Bluebeam Revu + Buildertrend Estimating | CompanyCam + Buildertrend daily logs | QBO Plus + Buildertrend sync | ClockShark or QB Time | ~$800–$1,400 |
| **10–25 employees** | Buildertrend Advanced or Procore (residential edition) | Bluebeam Revu + STACK | CompanyCam + FieldWire (if separate punch) | QBO Advanced or QB Desktop | ClockShark + Gusto | ~$2,500–$5,000 |
| **25+ employees, public works** | Procore + Autodesk Build | STACK + Bluebeam | CompanyCam + FieldWire | QB Enterprise or Sage 100 Contractor | ClockShark + ADP + LCPtracker | ~$8,000–$20,000+ |

### 10.2 Change Management — Getting People to Actually Use It

Software adoption is **a people problem dressed up as a tech problem**. The five levers that actually move adoption:

1. **Train in pairs.** No one learns alone. The PM and the foreman go through Buildertrend together for 4 hours, then leave the office and use it on a real job that afternoon.
2. **Make the new tool the only tool.** As soon as you allow "you can keep doing it the old way for now," the new tool will die. Set a date and stop accepting the old way.
3. **The boss uses it visibly.** If the GC owner is still texting and asking the PM to "put it in Buildertrend later," nothing changes. The owner must enter daily logs personally for the first month.
4. **Reward, don't punish.** First foreman to upload 50 photos in a month gets a $200 gift card. Cheap, public, repeated.
5. **Kill the shadow spreadsheet.** Six months in, audit. If there's a "real" spreadsheet somewhere, find out what the software is failing to do and fix it.

### 10.3 Data Migration: Start Fresh or Bring It Over?

| Data | Migrate or Start Fresh? |
|---|---|
| Active projects (in flight) | **Bring over essentials only**: schedule, budget, contacts. Don't migrate every email. |
| Closed projects (last 5 years) | **Archive to Google Drive**, do not import into the new platform. |
| Customer / vendor list | **Migrate.** Clean it first (remove duplicates, dead vendors). |
| Cost codes / templates | **Build fresh in the new platform.** Use migration as the excuse to rationalize your code structure. |
| Historical estimates | **Selectively.** Bring 5–10 archetypal jobs as templates; ignore the rest. |
| Photos | **Move to CompanyCam** with project tags; archive raw originals to Drive. |

**Rule of thumb:** if migrating it would take more than 30 minutes and the data is more than 12 months old, archive it instead.

### 10.4 ROI — What These Tools Actually Save

A 2026-honest ROI breakdown for a $3M-annual-revenue residential GC moving from spreadsheet/paper to Buildertrend + CompanyCam + QB Time:

| Saving | Approx. Annual Value | Source |
|---|---|---|
| Faster billing cycle (avg 7 days sooner) | $15,000–$30,000 (interest + cash flow) | Better invoicing + photo backup |
| Fewer missed change orders | $25,000–$80,000 | 1–3 CO's per project caught that would've been absorbed |
| Reduced RFI resolution time | $10,000–$20,000 | Schedule recovery + sub idle time |
| Fewer disputes won (photo evidence) | $20,000–$50,000 | One avoided dispute per year pays for the stack 5x over |
| PM time savings (2–4 hrs/week) | $10,000–$20,000 | Less retyping, less "find the email" |
| Insurance loss-run improvement | $3,000–$10,000 | Better safety docs lower premiums |
| **Total** | **$83,000–$210,000** | |
| **Software cost** | ~$15,000–$25,000 | |
| **Net ROI** | **5x–10x in year 2** | (Year 1 is breakeven due to learning curve) |

These are real numbers, not vendor marketing.

### 10.5 Integration Red Flags

Watch for these signals that your "tech stack" is actually a tech swamp:

- **Duplicate data entry.** Anyone retyping the same number into two systems = process broken.
- **The "export to Excel" workflow.** If your reporting requires exporting to Excel and pivoting manually, the tools are not integrated.
- **Sync errors logged but ignored.** A Buildertrend → QBO sync log with 200 unresolved errors = your financials are wrong.
- **Shadow spreadsheets persisting.** Especially in scheduling and budget-vs-actual.
- **Foremen carrying a clipboard alongside the iPad.** They've decided the iPad is for show.
- **The bookkeeper's "real" file.** A QuickBooks file plus a "tracking" Excel file = the QuickBooks file isn't trusted.

If you see three or more of these, the answer is **not more software**. The answer is to **pick one platform, kill the others, and rebuild the workflow.**

---

## Sources

- [Buildertrend Pricing 2026 — Volume-Based Quotes Explained (Projul)](https://projul.com/blog/buildertrend-pricing-analysis-2026/)
- [Buildertrend Pricing 2026: Plans, Costs & Hidden Fees (toricentlabs)](https://toricentlabs.com/blog/buildertrend-pricing-2026.html)
- [Buildertrend Software Overview 2026 (Software Advice)](https://www.softwareadvice.com/construction/buildertrend-profile/)
- [Buildertrend Pricing 2026 (TrustRadius)](https://www.trustradius.com/products/buildertrend/pricing)
- [JobTread vs Buildertrend Comparison 2026 (constructionbids.ai)](https://constructionbids.ai/blog/jobtread-vs-buildertrend-comparison)
- [JobTread vs Buildertrend (Projul)](https://projul.com/competitors/jobtread-vs-buildertrend/)
- [Custom Home Builder Software Compared 2026 — Buildertrend vs CoConstruct (constructionbids.ai)](https://constructionbids.ai/blog/coconstruct-vs-buildertrend-comparison)
- [Procore Pricing 2026 (procorepricing.com)](https://www.procorepricing.com/)
- [Procore vs Buildertrend (Projul)](https://projul.com/competitors/procore-vs-buildertrend/)
- [Procore Cost 2026 Hidden Fees (ITQlick)](https://www.itqlick.com/procore/pricing)
- [CompanyCam Pricing](https://companycam.com/pricing)
- [CompanyCam Review 2026 (Field Tech Tools)](https://www.fieldtechtools.land/tools/companycam)
- [Bluebeam Revu vs PlanSwift Comparison (Software Advice)](https://www.softwareadvice.com/cms/bluebeam-revu-profile/vs/planswift-takeoff-estimating/)
- [Hover vs STACK vs PlanSwift vs Bluebeam (Hover Blog)](https://hover.to/blog/hover-vs-stack-vs-planswift-vs-bluebeam-whats-the-best-blueprint-takeoff-tool-for-builders)
- [Bluebeam vs PlanSwift — Which Is Better for Takeoffs (Universe Estimating)](https://universeestimating.com/bluebeam-vs-planswift-which-is-better-for-takeoffs/)
- [busybusy vs QuickBooks Time Comparison](https://busybusy.com/blog/busybusy-vs-quickbooks-time-comparison/)
- [ClockShark vs QuickBooks Time (Timeero)](https://timeero.com/post/clockshark-vs-quickbooks-time)
- [QuickBooks Time vs ClockShark (GetApp)](https://www.getapp.com/hr-employee-management-software/a/tsheets/compare/clockshark/)
- [Fieldwire vs PlanGrid (Autodesk Build) Comparison 2026 (contractorsandbuilders.com)](https://contractorsandbuilders.com/compare/plangrid-vs-fieldwire/)
- [Fieldwire — see why teams choose over PlanGrid](https://www.fieldwire.com/lp/plangrid-alternative/)
- [Best Construction Punch List Software 2026 (constructionbids.ai)](https://constructionbids.ai/blog/construction-punch-list-software-2026)
- [Levelset — Lien Waiver Software Overview](https://www.levelset.com/lien-waivers/lien-waiver-software/)
- [Best Lien Waiver Software for Contractors Comparison 2026 (US Tech Automations)](https://ustechautomations.com/resources/blog/construction-lien-waiver-software-comparison-2026)
- [Houzz Pro Pricing](https://www.houzz.com/houzz-pro/pricing)
- [Houzz Pro 2026 Benefits, Features & Pricing (Software Advice)](https://www.softwareadvice.com/construction/houzz-pro-profile/)
- [LCPcertified — Certified Payroll Solution (LCPtracker)](https://lcptracker.com/solutions/lcpcertified/)
- [California DIR FAQ on Certified Payroll Reporting](https://www.dir.ca.gov/Public-Works/FAQ-certified-payroll-reporting.html)
- [California DIR Certified Payroll Reporting](https://www.dir.ca.gov/public-works/certified-payroll-reporting.html)
- [California DIR eCPR / PRISM / LCPtracker upload for QuickBooks (Sunburst Software)](https://sunburstsoftwaresolutions.com/california-dir-ecpr-prism-lcptracker-upload-feature-for-quickbooks.htm)
