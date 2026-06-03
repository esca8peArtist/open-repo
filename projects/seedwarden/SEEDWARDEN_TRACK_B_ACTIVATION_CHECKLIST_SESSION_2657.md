---
title: "Seedwarden Track B — Activation Runbook for User Decision"
session: 2657
date: 2026-06-03
prepared_by: seedwarden-agent (claude-sonnet-4-6)
status: STAGED — awaiting user decision (June 3 EOD)
confidence: 92%
---

# Seedwarden Track B — Activation Checklist and Runbook
## Session 2657 — June 3, 2026

**Decision due**: Today, June 3, EOD
**What this document is**: A concise activation runbook for rapid execution the moment you decide to proceed. Once you approve, Track B can be fully live within 45–60 minutes of setup time today, with the launch day itself requiring 3.5–4.0 hours of operator time.

---

## One-Line Activation Summary

Complete the 5 setup gates (social accounts, Canva, Kit, Google Drive, Etsy coupon), then follow ACTIVATION_RUNBOOK.md Section 2 for autonomous pre-launch substitutions, then execute the launch day sequence in Section 3 of the same file.

The activation command to execute each gate is documented at:
`projects/seedwarden/track-b-activation/ACTIVATION_RUNBOOK.md`

---

## Pre-Activation Verification (3 Steps, Under 5 Minutes)

Run these three checks before starting setup. They confirm no last-minute file-state regressions since the June 1 audit.

### Step 1: Confirm zone PDFs are intact

```bash
ls -la projects/seedwarden/assets/zone-cards/*.pdf | wc -l
```

Expected output: `8`

If output is less than 8, stop — file integrity issue. Reference:
`projects/seedwarden/ZONE_PDF_VERIFICATION_REPORT.md`

### Step 2: Confirm email copy file is present and non-empty

```bash
wc -l projects/seedwarden/execution/TRACK_B_EMAIL_COPY_FINAL.md
```

Expected: 330+ lines. If output is 0 or file not found, stop and investigate.

### Step 3: Confirm logo is at the expected path

```bash
ls -la projects/seedwarden/logos/seedwarden_logo_1.png
```

Expected: 919,135 bytes. Any significant deviation (> 10%) indicates a file was replaced — investigate before proceeding.

**If all 3 checks pass**: proceed to the 5-gate setup sequence below.

---

## The 5 Setup Gates

Execute in order. Gate 3 URL is required before autonomous pre-launch steps can run.

| Gate | What to do | Estimated time | Dependency |
|------|------------|----------------|------------|
| Gate 1 | Create Instagram, TikTok, Pinterest accounts. Download `seedwarden_logo_1.png`. Upload logo to each profile. Write zone guide bio copy (draft in `GATE_1_RAPID_SETUP_GUIDE.md`). | 45 min | None — start here |
| Gate 2 | Create Canva account (Pro trial OK). Set up Brand Kit: upload seedwarden_logo_1.png, set brand colors from zone card design, add Montserrat Bold + Inter as brand fonts. | 30 min | Gate 1 accounts created |
| Gate 3 | Create Kit account (free tier). Build landing page (template in `MAY_27_GATE_3_DEPLOYMENT_SCRIPT.md`). Build 5-email automation from copy in `TRACK_B_EMAIL_COPY_FINAL.md`. Publish both. Record Kit landing page URL. | 60–90 min | Most critical gate — URL needed for Steps 1–2 below |
| Gate 4 | Create Google Drive folder "Seedwarden Zone Cards". Upload all 8 PDFs from `assets/zone-cards/`. Set sharing to "Anyone with link" for each. Test each link in incognito. Log results. | 30 min | Kit URL from Gate 3 |
| Gate 5 | Log in to Etsy Shop Manager. Marketing > Coupons. Confirm SEEDWARDEN15 is Active at 15% off with no expiration. If not present, create it now. | 5 min | None — can run in parallel with Gate 1 |

**Total gate time**: 2.5–3.5 hours (can compress if gates run in parallel where noted)

---

## Autonomous Pre-Launch Steps (After All Gates Clear)

These two steps substitute placeholders in staged assets. Can be done by the orchestrator agent, or by you manually using find-and-replace.

**Step 1**: In `TRACK_B_SOCIAL_CALENDAR_MAY28_30.md`, replace all 9 instances of `[LANDING_PAGE_URL]` with the Kit landing page URL from Gate 3.

**Step 2**: In `TRACK_B_HERBALIST_OUTREACH_MATRIX.md`, replace all instances of `[LANDING_PAGE_URL]` with the same Kit URL.

**Verification**: Search both files for `[LANDING_PAGE_URL]` — zero remaining instances expected.

**Step 3**: Run the pre-launch delivery test (ACTIVATION_RUNBOOK.md Section 2, Step 4) — submit a test form, confirm Email 1 arrives with a working PDF download link, confirm Email 2 does not arrive within 2 minutes.

---

## Launch Day Sequence Summary

Full hour-by-hour detail: `projects/seedwarden/track-b-activation/ACTIVATION_RUNBOOK.md` Section 3

| Time (UTC) | Action |
|------------|--------|
| 07:30 | Log in to all 7 platforms (Kit, Instagram, TikTok, Pinterest, Etsy, Reddit, Buffer/Later) |
| 07:38–07:53 | Final checks: PDFs accessible, Kit Published, bios correct |
| 07:53 | GO/HOLD decision (must confirm: Kit Published, PDFs accessible, bios correct) |
| 08:00 | Post to Reddit r/herbalism (cannot pre-schedule) |
| 08:05 | Send Tier 1 influencer emails: Sabrena Gwin (AHG), Susan Leopold (UpS), John Gallagher (LearningHerbs) |
| 08:15 | Send DMs to all 15 influencer contacts |
| 08:30 | Instagram launch post |
| 08:45 | TikTok launch video (native upload — do not cross-post from Instagram) |
| 09:00 | Pinterest launch pin |
| 09:30–18:00 | Pulse checks every 60–90 minutes; log metrics |
| 18:00 | Day 1 wrap-up, queue Day 2 content |

**Operator time**: 3.5–4.0 hours distributed across the day.

---

## Estimated Total Time to Full Activation

| Phase | Time |
|-------|------|
| Pre-activation checks (3 steps above) | 5 minutes |
| 5-gate setup | 2.5–3.5 hours |
| Autonomous URL substitutions | 15 minutes |
| Pre-launch delivery test | 10 minutes |
| Launch day execution | 3.5–4.0 hours |
| **Total** | **6.5–8.0 hours** |

The 6.5–8 hours can be split across two days: gate setup on Day 1 (2.5–3.5 hours), launch day execution on Day 2 (3.5–4 hours).

---

## Contingency Triggers — June 22+ Timeline

If you defer activation beyond June 3, the following conditions determine when to reassess and what changes.

### If launch slips to June 6–10

No material impact. All assets remain valid. Social calendar dates in `TRACK_B_SOCIAL_CALENDAR_MAY28_30.md` reference "May 28–30" as launch window — these are post content templates, not time-locked. Substitute your actual launch date when posting. The Kit automation sequence is day-relative (Day 0, 2, 5, 7, 10) and does not depend on calendar date.

Action: None required. Launch when ready.

### If launch slips to June 22+ (Phase 3 assets ready)

Phase 3 is the medicinal herbs product expansion (see `PHASE_3_READINESS_CHECKLIST.md`). If Track B launches concurrently with Phase 3 readiness, the email sequence can be extended: Emails 3–4 can reference Phase 3 products in addition to Etsy shop links.

Contingency trigger: If Phase 3 guide PDFs are finalized before Track B launch, update Email 4 guide placeholder list to include Phase 3 titles.

Phase 3 tracking file: `projects/seedwarden/PHASE_3_JUNE_22_LAUNCH_CHECKLIST.md`

### If Track A (Etsy) resolves before Track B launches

If Etsy account verification completes and listings go live before Track B launch date, fill in Email 3 `[Your Etsy Shop URL]` and Emails 4–5 guide placeholders before Kit build. Track B launch sequence is otherwise unchanged.

Track A status file: `projects/seedwarden/TRACK_A_BLOCKER_RESOLUTION.md`

### If Kit account setup proves longer than estimated (Gate 3 delay)

Use the Gist fallback URL (`https://gist.github.com/esca8peArtist/db0b1798b5b70ff988367982176dc49d`) as a temporary zone card delivery URL. Share this in social bios and influencer outreach during launch day. Update to Kit URL when Kit DNS propagates (typically 24–48 hours).

This path is documented in ACTIVATION_RUNBOOK.md Section 5.

### If social handles are unavailable (Gate 1 partial block)

Instagram: If `@seedwarden` is taken, use `@seedwarden.co` or `@seedwarden_guide`.
TikTok: Same handle variants.
Pinterest: Handle competition is lower; `@seedwarden` is likely available.

Handle availability does not block launch. Document the chosen handles in ACTIVATION_RUNBOOK.md Section 1 gate completion record.

---

## Key File Reference

| Purpose | File |
|---------|------|
| Zone PDFs (8 files) | `projects/seedwarden/assets/zone-cards/` |
| Email automation copy (5 emails) | `projects/seedwarden/execution/TRACK_B_EMAIL_COPY_FINAL.md` |
| Influencer contacts (15) | `projects/seedwarden/HERBALIST_OUTREACH_CONTACT_LIST.md` |
| Influencer DM templates | `projects/seedwarden/TRACK_B_HERBALIST_OUTREACH_MATRIX.md` |
| Social post drafts (18 posts) | `projects/seedwarden/TRACK_B_SOCIAL_CALENDAR_MAY28_30.md` |
| Logo | `projects/seedwarden/logos/seedwarden_logo_1.png` |
| Activation runbook (definitive) | `projects/seedwarden/track-b-activation/ACTIVATION_RUNBOOK.md` |
| Readiness report (infrastructure audit) | `projects/seedwarden/track-b-activation/READINESS_REPORT_JUNE_1.md` |
| Gate 1 setup guide | `projects/seedwarden/GATE_1_RAPID_SETUP_GUIDE.md` |
| Gate 3 Kit setup guide | `projects/seedwarden/MAY_27_GATE_3_DEPLOYMENT_SCRIPT.md` |
| Launch day runbook | `projects/seedwarden/MAY_30_LAUNCH_DAY_RUNBOOK.md` |
| Common issues decision trees | `projects/seedwarden/TRACK_B_LAUNCH_DAY_COMMON_ISSUES_DECISION_TREES.md` |
| Rollback procedures | `projects/seedwarden/TRACK_B_LAUNCH_DAY_ROLLBACK_PROCEDURES.md` |
| Monitoring checkpoints | `projects/seedwarden/TRACK_B_MONITORING_CHECKPOINTS.md` |
| Track A blocker status | `projects/seedwarden/TRACK_A_BLOCKER_RESOLUTION.md` |
| Phase 3 launch checklist | `projects/seedwarden/PHASE_3_JUNE_22_LAUNCH_CHECKLIST.md` |

---

## Decision Options — June 3 EOD

**Option 1: Activate Track B today.**
Start Gate 1 now. Complete gates across today and tomorrow. Launch within 24–48 hours.

**Option 2: Defer to June 22 Track B + Phase 3 dual-track.**
No action required on assets — they remain valid. Check Phase 3 readiness at `PHASE_3_JUNE_22_LAUNCH_CHECKLIST.md`. Update email placeholders to include Phase 3 products when finalizing Kit build.

**Option 3: Activate Track A first (Etsy-first path).**
Requires resolving Etsy verification blocker (external timeline) and tag corrections (30 minutes). See `TRACK_A_BLOCKER_RESOLUTION.md`. Track B can follow independently at any time — it does not depend on Track A.

All options are ready for execution. The decision is yours.
