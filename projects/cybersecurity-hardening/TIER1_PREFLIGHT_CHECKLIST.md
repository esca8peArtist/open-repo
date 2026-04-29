---
title: "Tier 1 Pre-Flight Checklist"
project: cybersecurity-hardening
created: 2026-04-29
status: ready-for-execution
executor: Anya
gist-url: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108
---

# Tier 1 Pre-Flight Checklist

**Purpose**: Decision-gate checklist to verify all systems operational before sending first Tier 1 outreach email.

**Estimated time**: 45–60 minutes to complete all items

**Deadline**: Must complete before Day 1 of Week 1 outreach

---

## Section 1: Gist Accessibility (10 minutes)

**Critical**: The Gist URL must be publicly accessible with all content intact before any emails are sent.

### 1.1 Public Access

- [ ] Open https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108 in **private/incognito browser window**
- [ ] Do NOT log into GitHub
- [ ] Confirm: Page loads without login wall
- [ ] Confirm: Gist is marked as **Public** (check GitHub settings if unsure)

**If Gist requires login**: Stop. Do not proceed with outreach. Change visibility to Public in GitHub Gist settings (click "Secret" dropdown → "Public" → Save).

### 1.2 Content Verification

- [ ] Gist contains all **three core documents**:
  - [ ] `threat-model.md` (present and readable)
  - [ ] `opsec-playbook.md` (present and readable)
  - [ ] `implementation-guide.md` (present and readable)
- [ ] Optional: `publication-prep.md` (executive summary + glossary)

### 1.3 Critical Sections Spot-Check

- [ ] **Part 0 (Data Broker Opt-Outs)**: Located in implementation-guide.md, intact
- [ ] **California Path**: AB 60/AB 1766 → DELETE Act DROP platform is documented
- [ ] **Primary sources**: FOIA citations, government contract links, court filing references are visible

**If any section is missing or inaccessible**: Stop. Contact content owner. Do not send emails until all sections verified.

---

## Section 2: URL Tracking Setup (10 minutes)

**Purpose**: Create trackable short URL to measure engagement independently of email open rates.

### 2.1 Bitly Configuration

- [ ] Go to bitly.com
- [ ] Create free account (use non-primary email so account is linked to this project, not personal)
- [ ] Shorten the Gist URL: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108
- [ ] Create custom back-half (e.g., `bit.ly/opsec-corpus` or `bit.ly/opsec-guide`)
- [ ] Note the short URL here: `_________________________`

### 2.2 Redirect Verification

- [ ] Open the short URL in private/incognito browser window
- [ ] Confirm: Redirects to the full Gist URL
- [ ] Confirm: Full Gist loads correctly from the redirect

**Alternative (no analytics)**: Use tinyurl.com for simpler setup if Bitly unavailable.

---

## Section 3: Email Infrastructure (15 minutes)

**Purpose**: Set up Gmail labels, templates, and filters for organized campaign tracking.

### 3.1 Gmail Labels

Create these nested labels under a parent label `Tier1-Outreach`:

- [ ] `Tier1-Outreach/Sent` — all outreach emails sent by you
- [ ] `Tier1-Outreach/Response-Engagement` — questions, interest, forwarding intent
- [ ] `Tier1-Outreach/Response-Acknowledgment` — "received, will review" responses
- [ ] `Tier1-Outreach/Response-Declination` — "not for us" or "too busy"
- [ ] `Tier1-Outreach/OOO` — auto-responder out-of-office replies
- [ ] `Tier1-Outreach/Bounce` — undeliverable email notifications
- [ ] `Tier1-Outreach/Follow-Up-Pending` — contacts awaiting your follow-up

**How to create**: Gmail → Settings → Labels → "Create new label" → Name: `Tier1-Outreach` → Create → Then create nested labels with same "parent" setting.

### 3.2 Gmail Templates

Enable and save response templates (so you can quickly reply to common response types):

- [ ] Gmail Settings → Advanced → Enable Templates (checkbox)
- [ ] Compose a reply using Template R1 (Engagement follow-up) and save as draft: `R1-Engagement-Followup`
- [ ] Compose Template R2 (Acknowledgment follow-up) and save as draft: `R2-Acknowledgment-Followup`
- [ ] Compose Template R3 (Declination) and save as draft: `R3-Declination`

**Where to find templates**: See TIER1_OUTREACH_EXECUTION_PLAN.md Section 1.4

### 3.3 BCC Setup

- [ ] Confirm Gmail has "BCC myself" option visible in compose window
- [ ] (If not visible: Settings → Labels → check "Show labels in message list" or use keyboard shortcut Ctrl+Shift+B)

---

## Section 4: Tracking Spreadsheet (10 minutes)

**Purpose**: Create master tracking record for all 50+ outreach emails and responses.

### 4.1 Create Spreadsheet

- [ ] Open Google Sheets (or create local CSV file)
- [ ] Title: "Tier 1 Outreach Tracker — [today's date]"
- [ ] Add column headers (minimum):
  - Organization | Category (1A/1B/1C) | Contact Name | Contact Email/Method | Template Used | Date Sent | Time Sent | Bitly Click | Response Received | Response Date | Response Type | Follow-Up Sent | Follow-Up Date | Notes

### 4.2 Pre-Populate First Wave

- [ ] Add rows for all 5 Tier 1A national organizations (Day 1):
  - [ ] NILC
  - [ ] CLINIC
  - [ ] RAICES
  - [ ] ILRC
  - [ ] NLG
- [ ] Fill in: Organization name, Category (1A), Contact email, Notes

### 4.3 Storage

- [ ] Google Sheet: Share with yourself; verify accessible from multiple devices
- [ ] Local CSV: Save to `/projects/cybersecurity-hardening/outreach-backups/` (create directory if needed)
- [ ] Note spreadsheet location here: `_________________________`

---

## Section 5: Email Deliverability Test (5 minutes)

**Purpose**: Confirm your email address is trusted and emails don't land in spam.

### 5.1 Self-Test

- [ ] Send test email to yourself from the outreach email address
- [ ] Confirm: Test email arrives in inbox (not spam)
- [ ] Confirm: Sender address shows your name (not garbled)

### 5.2 (Optional) Mail-Tester Score

- [ ] Go to mail-tester.com
- [ ] Send test email to their generated address
- [ ] Get deliverability score (aim for 8/10 or higher)
- [ ] If score <8: Review their specific flags and fix (check for spam trigger words, authentication issues, etc.)

### 5.3 Confirm Sender Address

- [ ] The "from" address is the one you want permanently associated with this project: `_________________________`
- [ ] Double-check spelling (no typos in name)

---

## Section 6: Discord/Notification Webhook (5 minutes, Optional)

**Purpose**: Set up notifications for engagement responses (optional; Gmail labels are sufficient alternative).

### 6.1 Webhook Configuration

- [ ] If using Discord for notifications:
  - [ ] Create Discord webhook in project channel
  - [ ] Copy webhook URL to secure location (do NOT commit to GitHub)
  - [ ] Webhook URL: `_________________________`
  - [ ] Send test message: "Tier 1 outreach pre-launch test — webhook operational"
  - [ ] Verify message appears in Discord channel

### 6.2 Alternative (No External Dependency)

- [ ] Using Gmail labels + filters instead: No additional setup needed (labels from Section 3 are sufficient)

---

## Section 7: Contact List Readiness (5 minutes)

**Purpose**: Confirm contact research is complete for Week 1.

### 7.1 Day 1 Contacts (High Priority — Named Organizations)

- [ ] NILC contact info verified: info@nilc.org + https://www.nilc.org/about-us/contact-us/
- [ ] CLINIC contact info verified: national@cliniclegal.org
- [ ] RAICES contact info verified: communications@raicestexas.org
- [ ] ILRC contact info verified: kbello@ilrc.org
- [ ] NLG contact info verified: massdef@nlg.org

### 7.2 Days 2–5 Contacts (Research Completed)

- [ ] Have you researched 5 regional immigration legal aid organizations for Days 2–5? (Recommended to do this the Sunday before Week 1 starts)
  - If not yet: Schedule Sunday research session (2 hours)
  - If yes: Confirm 20 contact details (name, email, organization) are noted in tracking spreadsheet

### 7.3 Contact Info Accuracy Spot-Check

- [ ] Verify domain names (.org vs. .com, hyphenation):
  - CLINIC is `cliniclegal.org` (not `clinic.org` — that's different org)
  - ILRC is `ilrc.org`
  - RAICES is `raicestexas.org`
  - NLG is `nlg.org`

---

## Section 8: Email Draft Review (Optional but Recommended)

**Purpose**: Final verification that all email templates are ready to use.

### 8.1 Template Review

- [ ] Open TIER1_OUTREACH_PREPARED.md
- [ ] Read all 5 personalized drafts for Tier 1A national organizations
- [ ] Confirm: No placeholder text left (like `[Your name]`, `[Organization]`)
- [ ] Confirm: Gist URL is correct in all drafts

### 8.2 Custom Opening Hook

- [ ] For each Day 1 organization, write a 2–3 sentence personalization hook in the tracking spreadsheet's Notes column
  - Example for NILC: "NILC has been at the forefront of litigation on immigration enforcement tech. Given your work on Palantir and data privacy, [this corpus is relevant because...]"
  - Do NOT copy-paste from template; write specific to each org

---

## Section 9: Decision Gate — Final Verification

**Purpose**: Final confirmation before sending first email. If any item fails, do not proceed.

### 9.1 Gist Status

- [ ] Gist is publicly accessible (verified in Section 1)
- [ ] All three core documents present and readable
- [ ] Part 0 intact and California path documented

**STOP if not confirmed**: Do not send emails.

### 9.2 Email Infrastructure

- [ ] Gmail labels created (7 labels nested under `Tier1-Outreach`)
- [ ] Gmail templates saved (R1, R2, R3 ready to use)
- [ ] Bitly short URL created and tested
- [ ] Tracking spreadsheet created and pre-populated

**STOP if not confirmed**: Do not send emails.

### 9.3 Contact Information

- [ ] All 5 Day 1 contacts verified with correct email addresses
- [ ] Domain name accuracy confirmed
- [ ] Personalization notes written for each Day 1 organization

**STOP if not confirmed**: Do not send emails.

### 9.4 Email Deliverability

- [ ] Test email to self confirmed delivered (not spam)
- [ ] "From" address is correct and permanent for this project
- [ ] Mail-tester score ≥8/10 (if checked)

**STOP if not confirmed**: Diagnose and fix before proceeding.

---

## Section 10: Per-Email Pre-Send Checklist

**Use this checklist for each individual email before clicking Send.**

- [ ] Gist URL in email body is correct
- [ ] All `[Your name]` placeholders replaced with your actual name
- [ ] All organization-specific placeholder text replaced (e.g., `[organization]` → "NILC")
- [ ] Opening 2–3 sentences are specific to this organization (not generic copy-paste)
- [ ] Correct template used (1A for legal orgs, 1B for community, 1C for mutual aid)
- [ ] Email is marked as BCC to yourself
- [ ] Time is between 7:00–9:00 AM local time
- [ ] At least 3–5 minutes since last send (if sending multiple in one session)
- [ ] Tracking spreadsheet row is pre-filled for this contact

---

## Ready to Launch Checklist

**Before 7:00 AM on Day 1 of Week 1, verify ALL of the following:**

- [ ] Sections 1–7 above are completely checked off
- [ ] Section 9 (Decision Gate) shows no "STOP" warnings
- [ ] Tracking spreadsheet is open and visible
- [ ] First 5 organization emails are composed and ready to send
- [ ] Bitly dashboard is accessible for checking clicks
- [ ] Gmail is open and ready to compose/send

---

## If Any Item Fails

**Stop immediately. Do not send emails.**

Diagnose the issue:

| Item | Issue | Solution |
|------|-------|----------|
| Gist inaccessible | Login required | Change GitHub Gist visibility to Public |
| Gist missing sections | Sections not published | Contact content owner, do not send |
| Email bounces in deliverability test | Spam filtering | Review mail-tester flags, fix, re-test |
| Contact email incorrect | Bounce received in test | Verify email on org website, research alternate |
| Gmail labels not creating | Permission issue | Try again or use simpler flat label structure |
| Bitly not redirecting | URL error | Verify source URL in bitly settings, re-shorten |

---

## Launch Confirmation

**Once all sections are complete, you are cleared to send.**

- [ ] All sections 1–10 verified and checked
- [ ] No "STOP" warnings remain
- [ ] You have confidence in:
  - Gist accessibility ✓
  - Email infrastructure ✓
  - Contact accuracy ✓
  - Email templates ✓

---

## Quick Reference: File Locations

| File | Purpose | Location |
|------|---------|----------|
| Gist (canonical) | Published corpus | https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108 |
| TIER1_EXECUTION_LOG.md | Master sequencing + contact list + tracking | `/projects/cybersecurity-hardening/TIER1_EXECUTION_LOG.md` |
| TIER1_OUTREACH_PREPARED.md | Personalized email drafts for 1A national orgs | `/projects/cybersecurity-hardening/TIER1_OUTREACH_PREPARED.md` |
| TIER1_OUTREACH_EXECUTION_PLAN.md | Full execution guide + response handling | `/projects/cybersecurity-hardening/TIER1_OUTREACH_EXECUTION_PLAN.md` |
| Tracking Spreadsheet | Live campaign tracking (Google Sheet or CSV) | Note location in Section 4.3 above |
| Outreach Backups | CSV backups of tracking spreadsheet | `/projects/cybersecurity-hardening/outreach-backups/` |

---

**Status**: TIER1_PREFLIGHT_CHECKLIST.md ready for daily use.

**When to use this checklist**: Day -1 (one day before first email sends). Follow all sections in order. Expected duration: 45–60 minutes.

Last updated: 2026-04-29
