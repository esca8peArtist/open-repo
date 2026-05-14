---
title: "Phase 1 Block 2 — Template URL Replacement Guide"
created: 2026-05-14
status: ready-to-execute
purpose: "Complete find-replace guide for all link and personalization placeholders across the 3 template files"
time_estimate: "20-30 minutes"
dependency: "Block 1 Gist URLs confirmed accessible"
---

# Phase 1 Block 2 — Template URL Replacement Guide

**Estimated time**: 20-30 minutes  
**What you are doing**: Replacing placeholder text with actual Gist URLs and your name/contact info in 3 template files. Every placeholder must be replaced before any email can be sent.

---

## The 7 URL Placeholders and Their Replacements

Use this table for every find-replace operation below.

| Placeholder Text (exact) | Replace With |
|--------------------------|-------------|
| `[link to proposal]` | `https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261` |
| `[link to executive summary]` | `https://gist.github.com/esca8peArtist/2869da6eaeb15a47246ade3bbbc4a3f4` |
| `[link to litigation tracker]` | `https://gist.github.com/esca8peArtist/418d51bda087f15a04d685ab171a5ee0` |
| `[link to first amendment tracker]` | `https://gist.github.com/esca8peArtist/10d0a86e386e6c3c11c3830295a6503c` |
| `[link to environmental rollbacks]` | `https://gist.github.com/esca8peArtist/87e2bdb931b77480e56a08044c567bc4` |
| `[link to police consent decree tracker]` | `https://gist.github.com/esca8peArtist/1f5cb28527c98d12526c14302c775731` |
| `[link to domain 37]` | `https://gist.github.com/esca8peArtist/1277f5d5bcb0fe46604bbaba8fa37fd0` |

Note: The email templates (PHASE_1_EMAIL_TEMPLATES.md) use `{{PROPOSAL_URL}}`, `{{EXEC_SUMMARY_URL}}`, and `{{LITIGATION_TRACKER_URL}}` as placeholders rather than `[link to ...]`. Use the same URLs from the table above for those.

---

## The 2 Personalization Placeholders

| Placeholder Text | Replace With |
|-----------------|-------------|
| `[Your name]` | Your preferred outreach name (first name, or first + last) |
| `[Contact information]` | Your email address (and Signal handle if desired) |

In the email templates (PHASE_1_EMAIL_TEMPLATES.md), these appear as `{{YOUR_NAME}}` and `{{YOUR_CONTACT_INFO}}`.

---

## File 1: distribution-institutional-outreach-templates.md

**Path**: `/home/awank/dev/SuperClaude_Framework/projects/resistance-research/distribution-institutional-outreach-templates.md`

**How to edit**: Open the file in any text editor. Use Find & Replace (Ctrl+H or Cmd+H).

**Replacements to make**:

1. Find: `[link]` (or any variant like `[link to proposal]`, `[proposal link]`) — replace with the appropriate Gist URL from the table above based on context
2. Find: `[Your name]` — replace with your outreach name
3. Find: `[Contact information]` — replace with your email

**Verification**: After replacing, search for remaining `[link`, `[Your name`, `[Contact information` — if the search returns zero results, this file is complete.

- [ ] All `[link]` placeholders replaced
- [ ] `[Your name]` replaced
- [ ] `[Contact information]` replaced
- [ ] Verification search returns zero remaining placeholders

---

## File 2: distribution-substack-drafts.md

**Path**: `/home/awank/dev/SuperClaude_Framework/projects/resistance-research/distribution-substack-drafts.md`

**Replacements to make**:

1. Find: any `[link]`, `[proposal link]`, `[executive summary link]` — replace with Gist URLs
2. Find: `[Your name]` — replace with your name

**Verification**: Search for `[link` — zero results means complete.

- [ ] All link placeholders replaced
- [ ] Name placeholder replaced
- [ ] Verification search returns zero remaining

---

## File 3: distribution-reddit-templates.md

**Path**: `/home/awank/dev/SuperClaude_Framework/projects/resistance-research/distribution-reddit-templates.md`

**Replacements to make**:

1. Find: any `[link]` variants — replace with Gist URLs
2. Find: `[Your name]` — replace with your name (if present)

**Verification**: Search for `[link` — zero results means complete.

- [ ] All link placeholders replaced
- [ ] Verification search returns zero remaining

---

## File 4: PHASE_1_EMAIL_TEMPLATES.md (the 5 Batch 1 email drafts)

**Path**: `/home/awank/dev/SuperClaude_Framework/projects/resistance-research/PHASE_1_EMAIL_TEMPLATES.md`

This file uses `{{double-brace}}` placeholders. The URL placeholders:

1. Find: `{{PROPOSAL_URL}}` — replace with: `https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261`
2. Find: `{{EXEC_SUMMARY_URL}}` — replace with: `https://gist.github.com/esca8peArtist/2869da6eaeb15a47246ade3bbbc4a3f4`
3. Find: `{{LITIGATION_TRACKER_URL}}` — replace with: `https://gist.github.com/esca8peArtist/418d51bda087f15a04d685ab171a5ee0`

Note: Do NOT yet replace `{{YOUR_NAME}}`, `{{YOUR_CONTACT_INFO}}`, `{{DOMAIN_COUNT}}`, or the research-specific placeholders (`{{RECENT_JUST_SECURITY_ARTICLE}}`, etc.) in this file — those are handled per-email in Block 4 (or they are pre-filled in the individual email draft files created for Block 4).

**Verification**: Search for `{{PROPOSAL_URL}}`, `{{EXEC_SUMMARY_URL}}`, `{{LITIGATION_TRACKER_URL}}` — each should return zero results.

- [ ] `{{PROPOSAL_URL}}` replaced (appears in emails 1, 2, 3, 4, 5)
- [ ] `{{EXEC_SUMMARY_URL}}` replaced (appears in emails 1, 2, 3, 4, 5)
- [ ] `{{LITIGATION_TRACKER_URL}}` replaced (appears in emails 1 and 5)
- [ ] Verification search for remaining URL placeholders returns zero

---

## Master Verification Checklist

Run this after all four files are edited:

- [ ] File 1 (institutional outreach templates) — no remaining link or name placeholders
- [ ] File 2 (Substack drafts) — no remaining link placeholders
- [ ] File 3 (Reddit templates) — no remaining link placeholders
- [ ] File 4 (PHASE_1_EMAIL_TEMPLATES.md) — URL placeholders replaced; research and identity placeholders left for Block 4

**Block 2 complete when all four items above are checked.**

---

## Common Errors to Avoid

- Do not replace `[link]` placeholders with shortened URLs or redirects — use the full gist.github.com URLs exactly as shown
- Do not replace the research-specific placeholders in PHASE_1_EMAIL_TEMPLATES.md (e.g., `{{RECENT_JUST_SECURITY_ARTICLE}}`) — those are intentionally left for Block 4
- Do not add your email address to the To: field yet — that happens in Block 4
- If you see a placeholder in a different format (e.g., `(link)` or `[URL]`), treat it as equivalent and replace with the appropriate Gist URL

---

*Dependency: Block 1 Gist URLs. Next: Block 3 (Contact Verification) — can run in parallel with Block 2 in a separate browser tab.*
