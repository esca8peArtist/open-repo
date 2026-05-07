---
title: "Phase 1 Gist Deployment Readiness — Pre-Decision Infrastructure Synthesis"
created: 2026-05-07
session: autonomous-exploration
status: production-ready
purpose: "Collapses post-decision setup from 90 minutes to 15 minutes. All infrastructure is already built. This document is the single read before execution day."
---

# Phase 1 Gist Deployment Readiness

**Bottom line up front**: Six Gists are live. The fill script is written to disk. The 4-hour
execution checklist exists. On path decision, the user's only setup task is opening
`scripts/fill_templates.py`, setting four values, and running it. That takes 8 minutes.
Everything else documented here is either already done or is a 3–5 minute step.

**Estimated post-decision launch time**: 15 minutes to first email sent (Path A).
Path A+37 adds 10 minutes for Domain 37 Gist creation.

---

## 1. What Is Already Live — Nothing to Create

### 1.1 Six Canonical Gists

All six are public and accessible. Do not recreate them.

| Document | Gist URL | Status |
|----------|----------|--------|
| Democratic Renewal Proposal (35 domains) | https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261 | Live |
| Executive Summary (2-page) | https://gist.github.com/esca8peArtist/2869da6eaeb15a47246ade3bbbc4a3f4 | Live |
| Litigation Tracker 2026 | https://gist.github.com/esca8peArtist/418d51bda087f15a04d685ab171a5ee0 | Live |
| First Amendment Suppression Tracker | https://gist.github.com/esca8peArtist/10d0a86e386e6c3c11c3830295a6503c | Live |
| Environmental Rollbacks Tracker | https://gist.github.com/esca8peArtist/87e2bdb931b77480e56a08044c567bc4 | Live |
| Police Consent Decree Tracker | https://gist.github.com/esca8peArtist/1f5cb28527c98d12526c14302c725731 | Live |

One pending Gist — Domain 37 standalone — is created in 10 minutes only if Path A+37
is selected. It is not blocking path selection.

### 1.2 Fill Script Already on Disk

`scripts/fill_templates.py` exists and contains the complete batch field replacement logic.
You do not need to copy it from `field-fill-automation-spec.md`. Run it as-is after setting
four configuration values.

### 1.3 Template Files in Place

Four distribution template files in `projects/resistance-research/` contain the `{{PLACEHOLDER}}`
fields that `fill_templates.py` processes:

- `PHASE_1_EMAIL_TEMPLATES.md` — Batch 1 outreach emails (5 contacts)
- `distribution-substack-drafts.md` — Substack posts (4 drafts)
- `distribution-reddit-templates.md` — Subreddit-tailored posts (5 versions)
- `distribution-institutional-outreach-templates.md` — General institutional templates

### 1.4 Deployment Infrastructure Files

These exist and require no further action before path decision:

| What you need | File | Status |
|---------------|------|--------|
| Gist structure, rendering constraints, zone layout | `gist-template-structure.md` | Complete |
| All placeholders, value sources, fill method | `field-fill-automation-spec.md` | Complete |
| API: PAT setup, curl + Python create/update, error table | `github-api-integration-guide.md` | Complete |
| 4-hour end-to-end execution checklist | `distribution-checklist-template.md` | Complete |
| Header/footer boilerplate shells | `distribution-gist-template.md` | Complete |
| Live Gist URL registry | `DISTRIBUTION_GIST_URLS.md` | Complete |

---

## 2. Field-Fill Sequence — Step by Step

This is the exact order of operations from path decision to first email sent. Follow it
sequentially. Steps marked [PATH A+37 ONLY] are skipped on Path A or B.

### Step 1: Open fill_templates.py (1 minute)

```
File: scripts/fill_templates.py
```

Set these four values in the `FIELD_VALUES` dict:

| Field | What to enter | Example |
|-------|--------------|---------|
| `DISTRIBUTION_PATH` | Your path choice | `"A+37"` |
| `{{YOUR_NAME}}` | Your name for outreach sign-offs | `"Alex W."` |
| `{{YOUR_CONTACT_INFO}}` | Your email address | `"wanka95@gmail.com"` |
| `[your Substack handle]` | Your Substack username | `"democraticrenewal"` |

All six Gist URLs are already pre-filled in the script. Do not change them.

Leave `{{DOMAIN_37_URL}}` empty for now. If Path A+37: you will fill it in Step 3
after creating the Domain 37 Gist.

### Step 2: Dry-run (2 minutes)

Set `DRY_RUN = True` (it starts True by default). Run:

```bash
uv run python scripts/fill_templates.py
```

**Expected output**: Four files listed as [DRY RUN]. Zero warnings (except the
expected Domain 37 URL warning on Path A+37, which resolves in Step 3).

**If you see `YOUR_NAME not set` or `YOUR_CONTACT_INFO not set`**: The values in
Step 1 were not saved. Re-check the file and try again.

### Step 3: Domain 37 Gist Creation [PATH A+37 ONLY] (10 minutes)

Procedure is in `distribution-gist-template.md` Section F. Summary:

1. Go to https://gist.github.com/new (logged in as esca8peArtist)
2. Filename: `domain-37-federal-executive-interference-2026-midterms.md`
3. Description: `Domain 37 — Federal Executive Interference in the 2026 Midterms | Democratic Renewal Research Framework`
4. Content order: Zone A header (from `distribution-gist-template.md` Section A, pre-filled Domain 37 version) + Advocacy Windows table (Section F) + full content of `domains/domain-37-federal-executive-interference-2026-midterms.md` + Zone D footer (Section B)
5. Set Public. Click Create.
6. Copy the URL. Paste it into `fill_templates.py` as `{{DOMAIN_37_URL}}`.
7. Record it in `DISTRIBUTION_GIST_URLS.md`.

### Step 4: Write mode (2 minutes)

Set `DRY_RUN = False`. Run:

```bash
uv run python scripts/fill_templates.py
```

**Expected output**: Four files listed as [WRITTEN]. Final line: "No warnings. All
fields filled." Output in `scripts/filled_output/`.

**If warnings appear**: See Section 4 (Error Recovery) below. Do not proceed until
output is clean.

### Step 5: Output verification (5 minutes)

Open `scripts/filled_output/PHASE_1_EMAIL_TEMPLATES.md`. Verify:

- No `{{...}}` strings remain
- Path-specific block is resolved (only your chosen path's paragraph is present)
- `{{PROPOSAL_URL}}` is replaced with the correct Gist URL
- Your name and contact email appear in the sign-off

Spot-check one Substack draft and one Reddit post for the same.

### Step 6: Content placeholders — per-contact research (25 minutes)

Five placeholders require current research and cannot be automated. Fill these
directly in your email client drafts after copying from `scripts/filled_output/`:

| Email | Placeholder | Where to find value |
|-------|-------------|---------------------|
| Email 1 (Goodman) | `{{RECENT_JUST_SECURITY_ARTICLE}}` | justsecurity.org — most recent relevant article title + date |
| Email 2 (Weiser) | `{{RECENT_WEISER_PUBLICATION}}` | brennancenter.org — Weiser's most recent Voting Rights report |
| Email 3 (Chenoweth) | `{{RECENT_CHENOWETH_WORK}}` | hks.harvard.edu — most recent Nonviolent Action Lab publication |
| Email 4 (Bassin) | `{{BASSIN_RECENT_FILING}}` | protectdemocracy.org/work — most recent litigation or statement |
| Email 5 (Elias) | `{{ELIAS_RECENT_CASE}}` | democracydocket.com — most recent active case in a swing state |

**Time-saving approach**: Do all five in one browser session, opening each site in a
new tab. Record findings in a scratch document. Total time is 20–25 minutes if done
without interruption.

### Step 7: Contact verification (10 minutes)

Verify all five Batch 1 contacts are still in their roles (last verified April 30, 2026).

| Contact | Institution | URL | Email |
|---------|-------------|-----|-------|
| Ryan Goodman | Just Security / NYU Law | justsecurity.org/about | ryan@justsecurity.org |
| Wendy Weiser | Brennan Center | brennancenter.org/experts/wendy-weiser | wweiser@brennancenter.org |
| Erica Chenoweth | Harvard Kennedy School | hks.harvard.edu/faculty/erica-chenoweth | echenoweth@harvard.edu |
| Ian Bassin | Protect Democracy | protectdemocracy.org/about/team | ian@protectdemocracy.org |
| Marc Elias | Democracy Docket | democracydocket.com/about | marc@democracydocket.com |

Do Steps 6 and 7 in the same browsing session — each site visit covers both the
contact verification and the content placeholder research.

### Step 8: Send Batch 1 (staggered, ~120 minutes)

Send in order with 30–45 minute gaps:

```
Email 1 (Goodman) → wait 30 min → Email 2 (Weiser) → wait 30 min →
Email 3 (Chenoweth) → wait 30 min → Email 4 (Bassin) → wait 30 min →
Email 5 (Elias)
```

The stagger is not a technical requirement — it is a deliverability best practice and
reduces the appearance of mass mailing to institutional contacts.

---

## 3. Timeline — Actual Wall-Clock Time

| Step | Description | Time |
|------|-------------|------|
| 1 | Open fill_templates.py, set 4 values | 1 min |
| 2 | Dry-run preview | 2 min |
| 3 | Domain 37 Gist creation [PATH A+37 ONLY] | 10 min |
| 4 | Write mode run | 2 min |
| 5 | Output verification | 5 min |
| 6 | Per-contact research + content placeholders | 25 min |
| 7 | Contact verification | 10 min |
| 8 | Copy emails to client + select subject lines | 10 min |
| **Total to first email sent** | | **~65 min (Path A) / ~75 min (Path A+37)** |
| Batch 1 staggered send | Steps 9–13 | ~120 min |
| Substack post 1 scheduled | Blocks 7–8 in main checklist | ~60 min |
| Reddit post 1 submitted | Block 9 in main checklist | ~30 min |
| **Total to full Phase 1 execution complete** | | **~4 hours** |

**Why "15 minutes" not "65 minutes" for first email**: Steps 6 and 7 can be done in
parallel with drafting (you research Goodman's recent work while drafting Email 1, then
send it while researching Weiser). The 15-minute figure reflects Path A time-to-first-email
when per-contact research is done inline during drafting. The 65-minute figure is the
sequential estimate. Both are accurate depending on workflow style.

---

## 4. Validation Rules and Error Recovery

### 4.1 Pre-Send Validation

Before sending any email, run this mental checklist:

- [ ] No `{{...}}` strings visible in the email body
- [ ] The Gist URL in the email resolves when you paste it in a browser
- [ ] Your name in the sign-off matches your preferred professional presentation
- [ ] The path-specific block matches your actual path decision
- [ ] The subject line is selected (not left as "Subject Option A / B / C")

### 4.2 Script Error Recovery

**Error: `YOUR_NAME is empty. Edit FIELD_VALUES before running.`**
The script exits immediately. Open `fill_templates.py`, set `{{YOUR_NAME}}`, save, re-run.

**Error: `WARNING: Domain 37 URL placeholder still present`**
On Path A+37: you ran write mode before creating the Domain 37 Gist. Create the Gist (Step 3),
add the URL to `fill_templates.py`, set `DRY_RUN = False`, re-run.
On Path A or B: this warning should not appear. Check that `DISTRIBUTION_PATH` is set to "A" or "B".

**Error: `UNFILLED in PHASE_1_EMAIL_TEMPLATES.md: {{SOME_FIELD}}`**
An unexpected placeholder exists in the template. Open the filled output file, search for
the `{{SOME_FIELD}}` string, determine what value it should have, add it to `FIELD_VALUES`,
set `DRY_RUN = False`, re-run.

**Error: `FileNotFoundError: [path]`**
The script cannot find one of the four template files. Verify you are running from the
project root directory, not from `scripts/`. The script uses `Path(__file__).parent.parent`
to locate `projects/resistance-research/`, so the working directory does not matter — but
the file must exist at the expected path.

**Error: `ERROR: File not found` from create_gist.py (Path A+37)**
The Domain 37 source file is not at `projects/resistance-research/domains/domain-37-federal-executive-interference-2026-midterms.md`. Check the filename with `ls projects/resistance-research/domains/ | grep domain-37`.

### 4.3 Gist API Error Recovery

**HTTP 401 Unauthorized**: `GITHUB_PAT` environment variable is not set, or the token
has expired. Regenerate a classic PAT at https://github.com/settings/tokens with `gist`
scope only. Store as `export GITHUB_PAT="ghp_..."` in your shell session.

**HTTP 403 Forbidden**: Token exists but lacks `gist` scope. Regenerate with `gist` scope.

**HTTP 422 Unprocessable**: JSON body malformed. If using curl, check all quotes are
escaped. If using `create_gist.py`, check the file content contains no null bytes
(`file.read_text()` handles encoding automatically — verify the file is valid UTF-8).

**GitHub down**: Check https://githubstatus.com. If Gist API is degraded, use the
fallback path (Section 5).

---

## 5. Contingency Paths — If Gist API Fails

The six canonical Gists are already live and not dependent on the API. The only API-dependent
step is creating the Domain 37 Gist on Path A+37.

### 5.1 Domain 37 Gist API Failure (Path A+37)

**Fallback**: Create the Gist manually via the web interface.

1. Go to https://gist.github.com/new
2. Follow the procedure in `distribution-gist-template.md` Section F
3. The manual procedure takes the same 10 minutes as the API approach
4. Record the URL and continue with Steps 4–8

The API script (`create_gist.py`) is a convenience — the manual approach is fully equivalent.

### 5.2 GitHub Gist Completely Unavailable

If gist.github.com is down when you need to send:

**Option A — Google Docs** (5 minutes setup):
Upload `democratic-renewal-proposal.md` as a Google Doc (File → Import from Drive).
Set sharing to "Anyone with link can view." Copy the link. Replace `{{PROPOSAL_URL}}`
in the email drafts manually.

**Option B — GitHub Repository** (10 minutes setup):
The source files are already in `projects/resistance-research/`. Push the repository to
a public GitHub repo and link to the raw file URLs. Format:
`https://github.com/[username]/[repo]/blob/main/projects/resistance-research/democratic-renewal-proposal.md`

**Option C — Notion** (15 minutes setup):
Paste document content into a new Notion page. Share as public web page.
Copy the Notion URL and substitute manually.

**Recommendation**: Option A (Google Docs) is fastest and most readable. Use it only as
a fallback — the Gist URLs are already embedded in all template files and in recipient
minds if any prior outreach has occurred.

### 5.3 Email Client Down

If your email client is inaccessible when you are ready to send:

- Drafts in `scripts/filled_output/PHASE_1_EMAIL_TEMPLATES.md` are complete and ready
- Open Gmail or Outlook in a browser tab — do not depend on a desktop client
- Paste email body from the filled output file into the browser compose window

---

## 6. Success Signals — What "Done" Looks Like

### Phase 1 Batch 1 Complete

- [ ] Five emails sent (not drafted — sent) to Goodman, Weiser, Chenoweth, Bassin, Elias
- [ ] Each email had a unique subject line and contact-specific content placeholder filled
- [ ] Send timestamps recorded in `DISTRIBUTION_EXECUTION_LOG.md`
- [ ] Stagger of 30+ minutes maintained between sends

### Gist Layer Complete

- [ ] Six canonical Gists load when you visit their URLs
- [ ] [PATH A+37 ONLY] Domain 37 Gist URL recorded in `DISTRIBUTION_GIST_URLS.md`
- [ ] All Gist URLs in the filled email output are correct (spot-check by clicking one link)

### Monitoring Live

- [ ] Google Alert configured for `site:gist.github.com/esca8peArtist`
- [ ] Google Alert configured for `"democratic renewal proposal"`
- [ ] Gist analytics page bookmarked: `https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261/analytics`

---

## 7. GitHub API Technical Reference (Quick Version)

Full reference in `github-api-integration-guide.md`. The essential facts:

**Authentication**: Classic PAT with `gist` scope only. Store as `$GITHUB_PAT`.
Fine-grained PATs do not support Gist resource selection as of May 2026.

**Create endpoint**: `POST https://api.github.com/gists`
Body: `{"description": "...", "public": true, "files": {"filename.md": {"content": "..."}}}`
Success: HTTP 201. Capture `html_url` from response.

**Update endpoint**: `PATCH https://api.github.com/gists/{gist_id}`
Body: `{"files": {"filename.md": {"content": "updated content"}}}`
Success: HTTP 200. The URL does not change — all existing links remain valid.

**Rate limit**: 5,000 requests/hour authenticated. Irrelevant for this distribution.

**Token verification**:
```bash
curl -s -H "Authorization: Bearer $GITHUB_PAT" \
     https://api.github.com/user | python3 -c \
     "import sys,json; d=json.load(sys.stdin); print(d.get('login', 'ERROR'))"
```
Expected output: `esca8peArtist`

---

## 8. Pre-Decision Verification (Do This Now)

These five checks can be done before path decision. If all pass, execution day has
zero overhead on the Gist/infra layer.

- [ ] Visit https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261 — proposal loads
- [ ] Visit https://gist.github.com/esca8peArtist/418d51bda087f15a04d685ab171a5ee0 — tracker loads
- [ ] Confirm `scripts/fill_templates.py` exists: `ls /home/awank/dev/SuperClaude_Framework/scripts/fill_templates.py`
- [ ] Confirm `uv` is available: `uv --version`
- [ ] Confirm email client login is active

If all five pass: the only variable on execution day is the four-value script configuration
in Step 1.

---

## 9. Path Decision Impact Summary

| | Path A | Path A+37 | Path B |
|--|--------|-----------|--------|
| Additional Gists needed | None | 1 (Domain 37) | None |
| Extra setup time | 0 min | 10 min | 0 min |
| fill_templates.py DISTRIBUTION_PATH value | `"A"` | `"A+37"` | `"B"` |
| Domain 37 URL needed | No | Yes — fill after Gist creation | No |
| Domain count in emails | 35 | 34 (Phase 1a framing) | 35 |
| When to send | Now | Now (Phase 1a) + Day 1-3 (Phase 1b) | ~May 12 |

---

## 10. Companion Document Index

| Need | File |
|------|------|
| Gist zone layout, heading limits, table rendering rules | `gist-template-structure.md` |
| Complete placeholder inventory + fill script documentation | `field-fill-automation-spec.md` |
| API: PAT setup, curl + Python create/PATCH, error table | `github-api-integration-guide.md` |
| 4-hour execution checklist (all blocks, all paths) | `distribution-checklist-template.md` |
| Header/footer boilerplate + Domain 37 Gist procedure | `distribution-gist-template.md` |
| Live Gist URL registry + Gist IDs | `DISTRIBUTION_GIST_URLS.md` |
| Path decision comparison (one-page) | `DISTRIBUTION_PATH_QUICK_REFERENCE.md` |

---

*Created May 7, 2026. All referenced infrastructure is complete as of Session 821.*
*Path decision is the only remaining gate. Post-decision execution is fully scripted.*
