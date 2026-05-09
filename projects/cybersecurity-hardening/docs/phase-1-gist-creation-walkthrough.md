---
title: "Phase 1 Gist Creation & Verification Walkthrough"
project: cybersecurity-hardening
created: 2026-05-09
status: production-ready
executor: Anya
gist-url: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108
cross-references:
  - docs/phase-1-launch-runbook.md
  - TIER1_OUTREACH_PREPARED.md
  - PUBLICATION_README.md
---

# Phase 1 Gist Creation & Verification Walkthrough

**Status note**: The Gist for Phase 1 is already published at the canonical URL below. This document serves two purposes: (1) a verification guide to confirm the Gist remains publicly accessible before each send wave, and (2) a reference for creating new Gists (e.g., for Phase 2 sector-specific versions or updated corpus releases).

**Canonical Phase 1 Gist URL**:
`https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108`

---

## Section 1: What Is a GitHub Gist?

A GitHub Gist is a lightweight code and document sharing service. For this project, it serves as the publicly accessible hosting point for the three-part OpSec corpus (threat model, countermeasures playbook, implementation guide).

**Why Gist for this corpus**:

- **Zero infrastructure**: No server, no domain, no maintenance. Content is hosted by GitHub indefinitely.
- **Version history**: Every edit creates a new revision. Recipients who saved the URL see the current version; prior versions are archived.
- **View tracking**: GitHub displays a view count on each Gist file. This is a proxy metric for how many people accessed the corpus after receiving the outreach email.
- **Markdown rendering**: GitHub renders Markdown natively. The corpus files — formatted as Markdown — display as readable, formatted documents rather than raw text.
- **Incognito-accessible**: A public Gist requires no GitHub account to view. Recipients without GitHub accounts can access the corpus directly.

**Public vs. Secret Gists**:

A Public Gist is indexed by search engines and accessible to anyone with the URL. A Secret Gist is accessible only via the direct URL (not indexed). For Phase 1, the Gist must be **Public** — it needs to be accessible to the 40–60 contacts you email, including any recipients who forward the link.

---

## Section 2: Pre-Send Gist Verification (Before Each Wave)

Before sending each email wave, spend 2 minutes confirming the Gist is still accessible. This takes less time than a failed email campaign.

### Verification Steps

1. Open a private/incognito browser window (important — must be logged out of GitHub).
2. Navigate to: `https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108`
3. Confirm the page loads without a login prompt.
4. Verify all three files are present:
   - `threat-model.md`
   - `opsec-playbook.md`
   - `implementation-guide.md`
   - Optional: `publication-prep.md` (executive summary + glossary)
5. Scroll to Part 0 of the implementation guide. Confirm the data broker opt-out section is intact and readable.
6. Check that the Gist displays "Public" (not "Secret") in the visibility indicator.

**If the Gist loads but shows as Secret**: Sign into GitHub, navigate to the Gist, click the gear icon, select "Make public." Confirm the change. Re-verify in incognito.

**If the Gist is inaccessible (404 or login required)**: Do not send any emails until resolved. Follow the troubleshooting steps in Section 5 of this document.

---

## Section 3: Creating a New Gist (If Needed)

Use these steps if you need to create a new Gist — for example, a Phase 2 sector-specific version, an updated corpus release, or if the Phase 1 Gist ever needs to be re-created.

### Step-by-Step Creation

**Step 1: Navigate to GitHub**
- Go to `https://github.com`. Sign into your account.
- Note: Use the account `esca8peArtist` (the account that hosts the Phase 1 Gist) to maintain consistency. If that account is unavailable, a new account will generate a new URL — update all email templates accordingly.

**Step 2: Open the Gist creator**
- Click your profile icon in the top-right corner.
- Select "Your Gists" from the dropdown.
- Click the "+" icon or the "New Gist" button (top-right of the Gists page).

**Step 3: Name the first file**
- In the "Filename including extension" field, enter: `threat-model.md`
- This must match the filename exactly — it affects how GitHub renders the Markdown.

**Step 4: Paste the threat model content**
- Open `threat-model.md` from your local project directory.
- Copy the full file content.
- Paste into the editor area below the filename field.
- Verify the preview renders correctly (click the "Preview" tab).

**Step 5: Add additional files**
- Click "Add file" below the first editor block.
- Name the second file: `opsec-playbook.md`
- Paste the full content of `opsec-playbook.md`.
- Click "Add file" again.
- Name the third file: `implementation-guide.md`
- Paste the full content of `implementation-guide.md`.
- Optional: Add a fourth file `publication-prep.md` (executive summary + glossary).

**Step 6: Set description**
- In the "Gist description" field at the top, enter:
  `Three-part operational security guide for high-risk populations: threat model (primary-sourced), countermeasures playbook, and implementation guide. Covers Palantir ELITE surveillance, data broker opt-outs, device hardening, and communications security. Free, open-source.`

**Step 7: Set visibility to Public**
- The visibility toggle is near the "Create Gist" button.
- Confirm it shows "Create public Gist" (not "Create secret Gist").
- If it shows Secret, toggle it to Public before proceeding.

**Step 8: Click "Create public Gist"**
- GitHub creates the Gist and redirects to its URL.
- The URL format is: `https://gist.github.com/[username]/[hash]`
- Copy this URL immediately.

**Step 9: Verify in incognito**
- Open a new incognito browser window.
- Navigate to the Gist URL.
- Confirm it loads without login, all files are present, and Markdown renders correctly.

**Step 10: Save the URL**
- Save the Gist URL to your tracking notepad.
- Update the email templates in `TIER1_OUTREACH_PREPARED.md` if creating a new Gist (replace the placeholder URL with the new one).
- Update the `gist-url` field in the frontmatter of all relevant documents.

---

## Section 4: URL Shortening for Tracking

### Why Shorten

The full Gist URL is long and opaque: `https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108`. A Bitly short URL:
- Looks cleaner in email text (less chance of line-break corruption)
- Provides click analytics (total clicks, click timing, geography)
- Allows you to estimate engagement without email-level open tracking (which can trigger spam filters)

### Bitly Setup

1. Go to `bitly.com`.
2. Create a free account with a non-primary email address.
3. In the Bitly dashboard, paste the full Gist URL in the "Shorten your link" field.
4. Click "Shorten."
5. Optional: Click "Edit" on the generated short link and set a custom back-half. Suggested: `opsec-guide` or `opsec-corpus`. The resulting URL will be `bit.ly/opsec-guide`.
6. Confirm the short URL redirects correctly in a private browser window.
7. Save the short URL alongside the full Gist URL in your notepad.

**Use the short URL in all outreach emails.** The Bitly free tier shows:
- Total click count
- Click timeline (when clicks happened)
- Geographic distribution (country-level)
- Referrer data (where clicks originated)

Check the Bitly dashboard daily during Days 1–14. A click spike on a day you didn't send an email indicates someone forwarded the link to others.

### TinyURL Alternative

If Bitly is unavailable or you prefer not to create an account:
1. Go to `tinyurl.com`.
2. Paste the Gist URL.
3. Click "Make TinyURL."
4. Save the short URL.

TinyURL provides no analytics. You will rely on Gist view counts and email response rate as your engagement signals.

---

## Section 5: Troubleshooting

### Gist Shows as Private (Login Required)

**Symptoms**: Incognito browser shows a GitHub login page when navigating to the Gist URL.

**Cause**: Gist visibility was changed to Secret (accidentally or by GitHub's default on re-creation).

**Fix**:
1. Sign into GitHub.
2. Navigate to the Gist.
3. Click the "Edit" pencil icon.
4. Look for the visibility toggle near the save button.
5. Change from "Create secret Gist" to "Create public Gist."
6. Click "Update public Gist."
7. Re-verify in incognito.

Do not send any emails until the Gist is confirmed publicly accessible.

### Gist Returns 404 (Not Found)

**Symptoms**: Incognito browser shows a GitHub 404 page for the Gist URL.

**Cause**: The Gist was deleted, or the URL was copied incorrectly.

**Fix**:
1. Sign into the `esca8peArtist` GitHub account.
2. Click your profile icon → "Your Gists."
3. Check if the Gist appears in your Gists list.
4. If it appears: copy the correct URL from the Gist page (the URL may have changed after an edit).
5. If it does not appear: the Gist was deleted. Re-create it following Section 3 of this document. Update all email templates with the new URL before sending.

### Markdown Renders Incorrectly

**Symptoms**: The Gist content displays as raw text with visible asterisks, brackets, and pound signs rather than formatted headings and bold text.

**Cause**: File was named without the `.md` extension (e.g., `threat-model` instead of `threat-model.md`).

**Fix**:
1. Sign into GitHub. Navigate to the Gist.
2. Click "Edit."
3. In the filename field, add `.md` to the end of each filename.
4. Click "Update public Gist."
5. Re-verify in incognito — Markdown should now render.

### Recipients Report Unable to Access Gist

**Symptoms**: A contact emails back saying the link doesn't work or asks them to sign in.

**Cause**: Usually one of: (a) the Gist is Secret, (b) a URL formatting issue caused link corruption in their email client, or (c) they are accessing from a network with GitHub blocked.

**Steps**:
1. First: verify the Gist is Public in incognito (yourself). If it loads for you, the issue may be on their end.
2. Reply with the raw full URL (not the short URL) in case the short URL is being blocked: `https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108`
3. If they are on a network that blocks GitHub: offer to email them the three Markdown files as attachments, or direct them to an alternate hosting location (HackMD book, static site) if Phase 2 infrastructure has been set up.

### Gist View Count Not Updating

**Symptoms**: The Gist view counter shows 0 or doesn't increase after you share the link with multiple contacts.

**Note**: GitHub Gist view counts are not real-time. They update periodically and may lag by hours. They also do not count views from logged-in GitHub users (those are excluded from public counts). The count is a rough proxy, not an exact click tracker. Rely on Bitly for accurate click analytics.

---

## Section 6: Monitoring Gist View Counts

GitHub Gist displays a view count on the Gist page, visible when you are signed in. Check this weekly during the Phase 1 campaign:

1. Sign into GitHub.
2. Navigate to: `https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108`
3. Note the view count displayed near the top of the page.
4. Record in your tracking spreadsheet (Sheet 4: Amplification_Tracker, "Gist views" row).

**Interpretation**:
- Gist views are a floor estimate (undercounts due to GitHub's filtering of bot traffic and authenticated users).
- A large jump in views (e.g., 10+ new views in one day) when you have not sent a new email wave suggests someone forwarded the link.
- Consistent slow growth (1–3 views/day) suggests organic search discovery — less likely for a specialized corpus but possible.

Gist view counts are useful context, not primary evidence. Use Bitly clicks and email response rate as your primary engagement signals.

---

## Section 7: Phase 2 Gist Planning

For Phase 2 (Tier 2 institutional outreach), consider whether to use:

**Option A: Same Gist, same URL**
- Simpler. No URL changes in templates.
- Risk: If the corpus is updated (e.g., threat model currency update), all links point to the updated version automatically. Recipients who saved the old URL see the current version.
- Recommended for minor corpus updates.

**Option B: New Gist per major version**
- Create a new Gist (e.g., `opsec-corpus-v2.md`) for Phase 2.
- Risk: Two URLs in circulation; potential confusion if contacts share the old URL.
- Recommended only for major corpus revisions where the old version would be actively misleading.

**Option C: Sector-specific Gists**
- Create separate Gists for each Tier 2 sector (journalists, labor organizers, academics, etc.) with the corpus plus a sector-specific cover note at the top.
- Allows sector-specific tracking (which sector views which Gist most).
- Requires maintaining multiple Gist files in sync during corpus updates.
- Recommended if Phase 2 messaging diverges significantly by sector.

For Phase 1, Option A is the correct choice — a single canonical Gist linked from all outreach.
