---
title: "Wave 2 Gist Creation Workflow — Domains 38 and 40 (Parallel)"
created: 2026-05-30
purpose: "Parallel Gist creation workflow for Domain 38 (June 12–14) and Domain 40 (June 15–17), ready before respective Tier A send windows"
domain_38_create_before: "June 14, 2026 (one day before Tier A send June 15)"
domain_40_create_before: "June 17, 2026 (one day before Tier A send June 18)"
parallelism_note: "Domain 38 Gist created June 12–14 (pre-send staging). Domain 40 Gist created June 15–17 (parallel to Domain 38 Tier A day 1–3 sends). Both can be completed in the same week without conflict."
status: execution-ready
source_documents:
  - DOMAIN_38_GIST_CREATION_STEPS.md (Domain 38 10-step procedure — production-ready)
  - DOMAIN_40_GIST_CREATION_STEPS.md (Domain 40 10-step procedure — production-ready)
  - DOMAIN_39_GIST_CREATION_TEMPLATE.md (reference: same 10-step structure)
zone_separation: "Zone A = public distribution URL (same URL for all tiers); Zone D = internal movement use (Gist raw URL + local file path)"
---

# Wave 2 Gist Creation — Domains 38 and 40
## Parallel Creation Workflow for June 12–17 Pre-Production Window

*Both Gist creation procedures are fully documented in DOMAIN_38_GIST_CREATION_STEPS.md and DOMAIN_40_GIST_CREATION_STEPS.md. This document provides the parallel scheduling and Zone A/D separation framework so both Gists can be created in the same week without coordination delays.*

---

## Part 1: Parallel Scheduling

### 1.1 Why Parallel Creation is Feasible

Domain 38 Gist creation and Domain 40 Gist creation are independent operations. They use different source files, different Gist descriptions, and different filenames. They share the same GitHub account and the same 10-step procedure. Creating both in the same week requires approximately 20 minutes of total work (10 minutes per Gist) plus verification time.

**The parallel window**:

| Date | Domain 38 Activity | Domain 40 Activity |
|---|---|---|
| June 12 (Fri) | Create Domain 38 Gist (10 min) | — |
| June 13 (Sat) | Verify Domain 38 Gist (5 min); pre-fill email templates | — |
| June 14 (Sun) | Final pre-flight check; all 16 Tier A emails ready | — |
| June 15 (Mon) | **Domain 38 Tier A send begins** | Create Domain 40 Gist (10 min) |
| June 16 (Tue) | Domain 38 Tier A day 2 | Verify Domain 40 Gist (5 min); pre-fill email templates |
| June 17 (Wed) | Domain 38 Tier A day 3 | Final pre-flight check; all 15 Tier A emails ready |
| June 18 (Thu) | Domain 38 Tier A day 4 | **Domain 40 Tier A send begins** |

This schedule requires no coordination or scheduling decisions during execution. The only judgment call is whether to create the Domain 40 Gist on June 15 (while starting Domain 38 sends) or to create it June 13–14 (before any sends begin). Creating Domain 40 Gist earlier provides more verification buffer.

**Recommendation**: Create Domain 40 Gist on June 13 alongside Domain 38 Gist creation. Both are ready before any sends begin. Total June 13 time investment: 25 minutes.

### 1.2 File Naming Convention

Both Gist filenames match the source document names exactly:

| Domain | Gist Filename | Source File |
|---|---|---|
| Domain 38 | `domain-38-ai-regulatory-capture-governance.md` | `/projects/resistance-research/domain-38-ai-regulatory-capture-governance.md` |
| Domain 40 | `domain-40-surveillance-capitalism-electoral-manipulation.md` | `/projects/resistance-research/domain-40-surveillance-capitalism-electoral-manipulation.md` |
| Domain 39 (reference) | `domain-39-healthcare-access-democratic-infrastructure.md` | Gist URL: https://gist.github.com/esca8peArtist/131e8a94c955b973b87f7fb87d0f594b |

The `.md` extension is mandatory. Without it, GitHub Gist renders as unformatted plain text. All three Wave 2 Gist filenames follow the same hyphenated lowercase naming convention.

---

## Part 2: Domain 38 Gist — 10-Step Checklist

*This is the condensed 10-step checklist for Domain 38. The full procedure with rationale for each step is in DOMAIN_38_GIST_CREATION_STEPS.md.*

### Step 1 — Navigate

Go to: https://gist.github.com. Confirm logged in as esca8peArtist (or your GitHub account).

**Checkpoint**: Username visible in top right corner.

### Step 2 — Enter Description

In the "Gist description..." field, enter exactly:

```
Domain 38: Regulatory Capture in AI Governance — How Industry Shapes the Rules That Were Supposed to Govern It
```

### Step 3 — Enter Filename

In the filename field, enter exactly:

```
domain-38-ai-regulatory-capture-governance.md
```

The `.md` extension is required for Markdown rendering.

### Step 4 — Paste Full Document

Open `/home/awank/dev/SuperClaude_Framework/projects/resistance-research/domain-38-ai-regulatory-capture-governance.md` and copy the entire contents. Paste into the large text editor area.

**Post-paste verification scroll** (verify these sections are visible):

- [ ] YAML frontmatter block at top (`---` block with `hard_deadline: August 2, 2026`)
- [ ] "Leading Finding" section (xAI/Colorado case)
- [ ] Section 1: "The Statutory Vacuum"
- [ ] Section 2: "The Four Capture Mechanisms" with subsections (2.1 Revolving Door, 2.2 Standards Body Capture)
- [ ] Section 3: EU-US regulatory arbitrage
- [ ] Section 4: Preemption EO and state law dismantlement
- [ ] Section 5: Reform architecture
- [ ] Sources section (43 citations) visible at bottom
- [ ] No truncation at bottom of editor (scroll to confirm last citation is present)

### Step 5 — Set Visibility

Set to **"Create secret gist"**. Secret Gists are accessible to anyone with the URL but do not appear in public Gist search or your profile's public listing. This is appropriate for targeted professional distribution.

### Step 6 — Create

Click **"Create secret gist"**. GitHub redirects to:

```
https://gist.github.com/[username]/[32-character-hash]
```

Copy this URL immediately.

### Step 7 — Record URL

Paste URL here:

```
DOMAIN 38 GIST URL: _______________________________________________
```

Record this URL in:
- All 16 Tier A email templates (replace `[Gist URL — insert before send]`)
- `DISTRIBUTION_EXECUTION_LOG.md` (Domain 38 section)
- `PROJECTS.md` (update Domain 38 distribution status field)
- `WAVE_2_EXECUTION_TIMELINE.md` Domain 38 section (fill Gist URL field)

### Step 8 — Test (Incognito Browser)

Open the Gist URL in a private/incognito browser window. Verify all items:

- [ ] URL opens without requiring GitHub login
- [ ] Document renders as formatted Markdown (headings are bold/large, not `#` symbols)
- [ ] YAML frontmatter renders cleanly
- [ ] "Leading Finding" section visible near top
- [ ] xAI/Colorado case text present
- [ ] "The Four Capture Mechanisms" section header visible
- [ ] EU AI Act August 2 deadline text present
- [ ] Sources section (43 citations) present at bottom
- [ ] All source URLs are clickable blue links
- [ ] No visible truncation — scroll from top to bottom
- [ ] URL in incognito window address bar matches recorded URL from Step 7

**If all 10 items pass**: Domain 38 Gist is ready for distribution.

**If any item fails**: See troubleshooting in DOMAIN_38_GIST_CREATION_STEPS.md Step 10.

### Step 9 — Pre-Fill Email Templates

Before the June 15 Tier A send, insert the Gist URL into all 16 planned email templates.

**Search in email drafts for**: `[Gist URL — insert before send]`
**Replace with**: The URL from Step 7

Complete this on June 14 (one day before send) or the morning of June 15 before beginning the send sequence.

**Email templates requiring Gist URL insertion**:
- EFF (info@eff.org) — personalized template
- CDT (info@cdt.org) — personalized template
- Senate Commerce Committee (commerce@commerce.senate.gov) — cover email
- AI Now Institute (form submission) — form field
- Brennan Center (brennancenter@nyu.edu) — personalized template
- Georgetown ITLP (itlp@law.georgetown.edu) — personalized template
- Mozilla Foundation (incubator@mozillafoundation.org) — personalized template
- ACLU (nationaloffice@aclu.org) — standard template
- Remaining 8 contacts — standard template with Gist URL

### Step 10 — Log Completion

After completing Steps 7–9, record in `DISTRIBUTION_EXECUTION_LOG.md`:

```
Domain 38 Gist created: [DATE, UTC]
Gist URL: [URL]
Gist visibility: [Secret / Public]
Step 8 checklist: [All passed / Failures: list]
Email templates pre-filled: [Yes / No]
Ready for June 15 Tier A send: [Yes / No]
```

---

## Part 3: Domain 40 Gist — 10-Step Checklist

*Condensed 10-step checklist for Domain 40. Full procedure with rationale in DOMAIN_40_GIST_CREATION_STEPS.md.*

### Step 1 — Navigate

Go to: https://gist.github.com. Confirm logged in.

### Step 2 — Enter Description

In the "Gist description..." field, enter exactly:

```
Domain 40: Surveillance Capitalism and Electoral Manipulation — How Commercial Data Infrastructure Became Democratic Attack Infrastructure
```

### Step 3 — Enter Filename

In the filename field, enter exactly:

```
domain-40-surveillance-capitalism-electoral-manipulation.md
```

### Step 4 — Paste Full Document

Open `/home/awank/dev/SuperClaude_Framework/projects/resistance-research/domain-40-surveillance-capitalism-electoral-manipulation.md` and copy the entire contents. Paste into the large text editor area.

**Post-paste verification scroll** (verify these sections are visible):

- [ ] YAML frontmatter block at top (includes `hard_deadline: 2026-11-03` and `eu_enforcement_hook: 2026-08-02`)
- [ ] Executive Summary section present and leads with NRSC deepfake finding (March 11, 2026)
- [ ] Section 1.1: "The Commercial Data Pipeline" (includes Thomson Reuters CLEAR, LexisNexis Accurint, L2, TargetSmart reference)
- [ ] Section 1.2: "The Government-Private Data Synthesis: DOJ Voter File Demands" (DOJ MOU analysis)
- [ ] Section 1.3: "Geofencing, Location Targeting, and Digital Suppression Infrastructure" (PNAS study: 1.86% turnout reduction, 4x disparity)
- [ ] Section 2: AI-generated synthetic content deployment (NRSC deepfake section)
- [ ] Section 3: FEC paralysis (deadlock since May 2025)
- [ ] Section 4: EU comparison (DSA, EU AI Act Article 50, Regulation 2024/900)
- [ ] Section 5: Reform architecture (four proposals)
- [ ] Sources section (47 citations) visible at bottom
- [ ] No truncation at bottom of editor

### Step 5 — Set Visibility

Set to **"Create secret gist"**. Same rationale as Domain 38.

### Step 6 — Create

Click **"Create secret gist"**. Copy the URL immediately.

### Step 7 — Record URL

Paste URL here:

```
DOMAIN 40 GIST URL: _______________________________________________
```

Record this URL in:
- All 15 Tier A email templates for Domain 40 (replace `[Gist URL — insert before send]`)
- `DISTRIBUTION_EXECUTION_LOG.md` (Domain 40 section)
- `PROJECTS.md` (update Domain 40 distribution status)
- `WAVE_2_EXECUTION_TIMELINE.md` Domain 40 section (fill Gist URL field)

### Step 8 — Test (Incognito Browser)

Open the Gist URL in a private/incognito browser window. Verify all items:

- [ ] URL opens without requiring GitHub login
- [ ] Document renders as formatted Markdown
- [ ] YAML frontmatter renders cleanly
- [ ] Executive Summary section visible near top
- [ ] NRSC deepfake reference (March 11, 2026) present in Executive Summary
- [ ] PNAS study finding (1.86% turnout reduction) appears in Section 1.3
- [ ] FEC deadlock reference (May 2025) appears in Section 3
- [ ] EU AI Act August 2 enforcement date appears in Section 4
- [ ] DSA political microtargeting prohibition text present
- [ ] Reform architecture section (four proposals) visible near end
- [ ] Sources section (47 citations) present at bottom
- [ ] All source URLs render as clickable blue links
- [ ] No visible truncation
- [ ] URL in incognito matches recorded URL

**If all 14 items pass**: Domain 40 Gist is ready for distribution.

**If any item fails**: See troubleshooting in DOMAIN_40_GIST_CREATION_STEPS.md Step 10.

### Step 9 — Pre-Fill Email Templates

Before the June 18 Tier A send, insert the Domain 40 Gist URL into all 15 Tier A email drafts.

**Key hook sentences by recipient to verify URL placement**:
- EPIC: "Full empirical record: [Gist URL]"
- Common Cause: "Domain 40 analysis: [Gist URL]"
- Brennan Center (voting rights desk): "Full documentation: [Gist URL]"
- Voting Rights Lab: "Suppression infrastructure analysis: [Gist URL]"
- ACLU: "Complete supply chain documentation: [Gist URL]"

Complete this on June 17 (one day before send) or the morning of June 18.

### Step 10 — Log Completion

After completing Steps 7–9, record in `DISTRIBUTION_EXECUTION_LOG.md`:

```
Domain 40 Gist created: [DATE, UTC]
Gist URL: [URL]
Gist visibility: [Secret / Public]
Step 8 checklist: [All passed / Failures: list]
Email templates pre-filled: [Yes / No]
WAVE_2_EXECUTION_TIMELINE.md updated: [Yes / No]
Ready for June 18 Tier A send: [Yes / No]
```

---

## Part 4: Zone A / Zone D Separation

### 4.1 Zone A — Public Distribution URL

**Definition**: The Gist URL is the Zone A distribution asset. It is the URL that goes into all outreach emails, Reddit posts, Twitter threads, LinkedIn articles, and any external distribution.

- Zone A URL is the same for all Tier A, B, C, and D distribution. There is no separate URL for different tiers.
- Zone A is accessible without GitHub authentication (Secret Gist setting).
- Zone A URL format: `https://gist.github.com/[username]/[hash]`

**Do not**:
- Use the "raw" Gist URL (`https://gist.githubusercontent.com/...`) in outreach emails. The raw URL shows unrendered plain text. Recipients need the rendered Markdown view.
- Create a separate Gist for internal use. There is no need for a restricted internal version.

### 4.2 Zone D — Internal Movement Use

**Definition**: Zone D encompasses internal-use assets that are not sent externally. For Domains 38 and 40, Zone D consists of:

1. **Source document file paths**: The local file paths (`/home/awank/dev/SuperClaude_Framework/projects/resistance-research/domain-38-ai-regulatory-capture-governance.md` and the equivalent for Domain 40) are Zone D. These are used by the orchestrator for research, not shared externally.

2. **This document and all execution planning files** (`phase-2-execution/` directory contents): Zone D. Not distributed externally.

3. **Contact stratification files**: Zone D. Not shared with outreach recipients.

4. **Gist raw URL** (`https://gist.githubusercontent.com/...`): Zone D / internal. Use only for verifying document completeness, not for outreach.

5. **DISTRIBUTION_EXECUTION_LOG.md entries**: Zone D. Internal tracking only.

### 4.3 Zone Boundary Enforcement

The only artifact that crosses from Zone D to Zone A is the Gist rendered URL. Everything in the `phase-2-execution/` directory, the source document files, and the contact list files remain Zone D.

**At no point should**:
- The contact stratification files be shared with outreach recipients
- The execution timeline documents be referenced in outreach emails
- The source file paths be included in Gist content

The Gist content itself (the source document) is Zone A. The planning and contact infrastructure surrounding it is Zone D.

---

## Part 5: GitHub Authentication and API Notes

### 5.1 Manual Creation (Recommended for Wave 2)

Wave 2 Gist creation requires creating two Gists — approximately 20 minutes of manual work total. Manual creation via https://gist.github.com is recommended because:
- The verification checklist (Step 8) must be completed regardless of creation method
- The total time savings from API automation vs. manual is less than 5 minutes per Gist
- API creation introduces authentication state management that adds complexity without meaningful time benefit at this scale

### 5.2 GitHub Gist API (For Future Automation Reference)

If automating Gist creation in a future cycle, the relevant API endpoint is:

```
POST https://api.github.com/gists
Authorization: Bearer [GITHUB_TOKEN]
Content-Type: application/json

{
  "description": "Domain 38: Regulatory Capture in AI Governance...",
  "public": false,
  "files": {
    "domain-38-ai-regulatory-capture-governance.md": {
      "content": "[full document text]"
    }
  }
}
```

The response includes the Gist URL in the `html_url` field. A `public: false` Gist is equivalent to a "secret" Gist in the web UI.

**Authentication**: Personal Access Token (PAT) with `gist` scope, or OAuth token with `gist` scope. Store as `GITHUB_GIST_TOKEN` environment variable. Never hardcode in scripts.

### 5.3 Gist Update Procedure

If a source document is revised after the Gist is created:

1. Navigate to the Gist URL while logged in as the creating account
2. Click the pencil edit icon
3. Replace the content in the text editor with the updated document text
4. Click "Update secret gist"
5. The Gist URL remains unchanged; all previously sent links continue to work

There is no need to create a new Gist for document updates. Update the existing Gist. Note the update date in DISTRIBUTION_EXECUTION_LOG.md.

---

## Part 6: Three-Gist Wave 2 Reference Table

After both Wave 2 Gists are created, all three Gists for the current distribution cycle are live:

| Domain | Gist Description | Source File | Create Before | Tier A Send Date | Gist URL |
|---|---|---|---|---|---|
| Domain 39 | Healthcare Access as Democratic Infrastructure | domain-39-healthcare-access-democratic-infrastructure.md | May 29 | June 1 | https://gist.github.com/esca8peArtist/131e8a94c955b973b87f7fb87d0f594b |
| Domain 38 | Regulatory Capture in AI Governance | domain-38-ai-regulatory-capture-governance.md | June 14 | June 15 | [Record after creation] |
| Domain 40 | Surveillance Capitalism and Electoral Manipulation | domain-40-surveillance-capitalism-electoral-manipulation.md | June 17 | June 18 | [Record after creation] |

All three Gists use identical 10-step creation procedure. Only the content, description, filename, and deadline context differ.

---

*Procedure created May 30, 2026. Domain 38 full procedure in DOMAIN_38_GIST_CREATION_STEPS.md (production-ready). Domain 40 full procedure in DOMAIN_40_GIST_CREATION_STEPS.md (production-ready). Domain 39 Gist already live at https://gist.github.com/esca8peArtist/131e8a94c955b973b87f7fb87d0f594b.*
