---
title: "Track B Activation Runbook — June 2, 2026"
date: 2026-06-01
status: STAGED — execute once all 5 gates are cleared
scope: >
  Exact step-by-step autonomous sequence from gate completion to launch.
  User-facing steps clearly marked. Autonomous steps clearly marked.
  No ambiguity at go-time.
---

# Track B Activation Runbook
## June 2, 2026 Launch Sequence

**How to use this document**: Complete the 5 user gates (Section 1). Then follow
Section 2 (autonomous pre-launch steps) and Section 3 (launch day sequence).

---

## Section 1: Gate Completion Record

Fill in each row as you complete it. The Kit landing page URL (Gate 3) is needed
before proceeding to Section 2 Step 3.

| Gate | Status | Completion Notes |
|------|--------|-----------------|
| Gate 1: Instagram account | [ ] | Handle: |
| Gate 1: TikTok account | [ ] | Handle: |
| Gate 1: Pinterest account | [ ] | Handle: |
| Gate 2: Canva Brand Kit | [ ] | Brand Kit URL: |
| Gate 3: Kit account live | [ ] | Kit account URL: |
| Gate 3: Landing page published | [ ] | Landing page URL: |
| Gate 3: Automation Published | [ ] | Status confirmed: |
| Gate 4: All 8 PDFs on Google Drive | [ ] | Drive folder URL: |
| Gate 4: All 8 download links tested | [ ] | Logged in WORKLOG.md: |
| Gate 5: SEEDWARDEN15 coupon active | [ ] | Etsy coupon status: |

**Gate 3 — Kit Landing Page URL** (fill in, needed for Step 3 below):
```
Kit landing page URL: _________________________________
```

---

## Section 2: Autonomous Pre-Launch Steps (After All Gates Clear)

These steps are autonomous — the orchestrator can execute them. They are listed in
dependency order. Do not proceed to Section 3 until all items here are checked.

### Step 1: Replace [LANDING_PAGE_URL] in Social Post Drafts

File: `projects/seedwarden/TRACK_B_SOCIAL_CALENDAR_MAY28_30.md`

All 18 post drafts contain the placeholder `[LANDING_PAGE_URL]`. Replace all
instances with the confirmed Kit landing page URL (from Gate 3 above).

If Kit URL is not yet available, use Gist URL as temporary:
`https://gist.github.com/esca8peArtist/db0b1798b5b70ff988367982176dc49d`

Update to Kit URL in social bios when Kit landing page is published.

**Verification**: Search file for `[LANDING_PAGE_URL]` — zero remaining instances.

---

### Step 2: Replace [LANDING_PAGE_URL] in Influencer DM Templates

File: `projects/seedwarden/TRACK_B_HERBALIST_OUTREACH_MATRIX.md`

Same substitution as Step 1 but in the DM templates.

**Verification**: Search file for `[LANDING_PAGE_URL]` — zero remaining instances.

---

### Step 3: Verify Kit Automation Status

Log in to Kit. Navigate to Automations. Confirm:
- Automation name: "Seedwarden Welcome" (or equivalent)
- Status: Published (NOT Draft, NOT Paused)
- Trigger: "When subscriber joins via landing page"
- Email count: 5 emails in sequence
- Delays: Day 0, Day 2, Day 5, Day 7, Day 10

If status shows Draft: click Publish before proceeding. Launch cannot proceed
with automation in Draft state.

---

### Step 4: Run Pre-Launch Delivery Test

From an incognito browser (not logged into Kit):
1. Open Kit landing page URL
2. Submit form: use a personal email address, select Zone 5
3. Wait up to 60 seconds
4. Verify Email 1 arrives with Zone 5 PDF download link
5. Click the link — confirm PDF downloads (no "Request access" error, no viewer page)
6. Wait 2 minutes — confirm Email 2 does NOT arrive (delay logic active)

If test fails: see `projects/seedwarden/TRACK_B_LAUNCH_DAY_COMMON_ISSUES_DECISION_TREES.md`

---

### Step 5: Verify Social Bio Links

On each social platform, navigate to the profile and confirm:
- The Kit landing page URL (from Gate 3) is in the bio/website field
- The URL is clickable and loads the Kit landing page without errors

Platforms: Instagram, TikTok, Pinterest

If any bio is missing the link: add it directly on that platform before proceeding.

---

### Step 6: Confirm SEEDWARDEN15 Coupon (Gate 5 Verification)

Log in to Etsy Shop Manager. Marketing > Coupons. Confirm SEEDWARDEN15 is Active,
15% off, no expiration issues.

This check takes 2 minutes and eliminates the only remaining dependency for Email 5.

---

### Step 7: Prepare Scheduling Queue

For non-Reddit posts (Instagram, TikTok, Pinterest), Buffer or Later can pre-schedule
the launch post so it goes out automatically at the target time without manual login.

If using Buffer/Later:
- Connect Instagram, TikTok, Pinterest accounts (these were just created in Gate 1)
- Queue the launch post from `TRACK_B_SOCIAL_CALENDAR_MAY28_30.md` (June 2 launch post)
- Schedule time: Instagram 18:00 UTC, TikTok 16:00 UTC, Pinterest 20:00 UTC

If not using a scheduler: note exact post times and set a phone reminder for each.

Reddit posts CANNOT be scheduled — they require manual posting on launch day.

---

### Pre-Launch Verification Checklist (Complete Before Launch Day)

- [ ] Kit automation status: Published
- [ ] Pre-launch delivery test: passed (PDF downloads, delay logic active)
- [ ] All 18 social posts: `[LANDING_PAGE_URL]` replaced
- [ ] All DM templates: `[LANDING_PAGE_URL]` replaced
- [ ] Instagram bio: Kit landing page URL present
- [ ] TikTok bio: Kit landing page URL present
- [ ] Pinterest website field: Kit landing page URL present
- [ ] SEEDWARDEN15 coupon: Active in Etsy
- [ ] Launch post scheduled or manual posting reminders set
- [ ] Phone charged and accessible for launch day

**When all items above are checked: LAUNCH IS CLEARED. Proceed to Section 3.**

---

## Section 3: Launch Day Execution Sequence

**Reference runbook**: `projects/seedwarden/MAY_30_LAUNCH_DAY_RUNBOOK.md`
Read "May 30" throughout that document as your launch date (June 2).

Summary of launch day operator tasks (all UTC):

| Time (UTC) | Action | Operator |
|------------|--------|----------|
| 07:30 | Log in to all 7 platforms: Kit, Instagram, TikTok, Pinterest, Etsy, Reddit, Buffer/Later | User |
| 07:38 | Verify all 8 PDFs accessible at Gist URL; Kit shows Published; bios have correct URL | User |
| 07:48 | Send one final test email from Kit landing page; scan for placeholder text | User |
| 07:53 | GO/HOLD decision: all 3 criteria must be YES (Kit Published, PDFs accessible, bios correct) | User |
| 08:00 | Post to Reddit r/herbalism (manual — cannot pre-schedule) | User |
| 08:05 | Send outreach emails to Tier 1 influencer contacts (Sabrena Gwin, Susan Leopold, John Gallagher) | User |
| 08:15 | Send DMs to all 15 contacts via platform DM routes | User |
| 08:30 | Post Instagram launch post (manual or Buffer/Later) | User |
| 08:45 | Upload TikTok launch video natively (NOT cross-posted from Instagram) | User |
| 09:00 | Post Pinterest launch pin (manual or scheduled) | User |
| 09:30 | First pulse check: Reddit comments, Kit signups, social engagement | User |
| 11:00 | Second pulse check | User |
| 12:00 | Third pulse check | User |
| 13:00 | Fourth pulse check | User |
| 14:30 | Fifth pulse check | User |
| 16:00 | Mid-day check: TikTok boost post (optional) | User |
| 18:00 | Day 1 wrap-up: log Day 0 snapshot metrics, queue Day 2 content | User |
| 20:00 | Final check, close out launch day | User |

Total operator time: 3.5–4.0 hours across the day.

---

## Section 4: Post-Launch Monitoring Schedule

| Date (June 2 launch) | Checkpoint | Key Decision |
|----------------------|------------|--------------|
| June 5 | Day 3 checkpoint | Go/Marginal/Fail initial read vs. metrics in READINESS_REPORT_JUNE_1.md |
| June 9 | Day 7 checkpoint | Tier 2 partnership candidates identified |
| June 16 | Day 14 checkpoint | Phase 3 GO/GO-with-adjustments/DEFER decision |

Checkpoint thresholds: `projects/seedwarden/TRACK_B_MONITORING_CHECKPOINTS.md`

---

## Section 5: Contingency Quick-Reference

| Situation | Action |
|-----------|--------|
| Kit automation still in Draft at 07:53 | Publish immediately; if cannot, proceed with manual email fallback per Contingency D in `SEEDWARDEN_TRACK_B_GATES_RUNBOOK.md` |
| A social platform bio link missing | Add it now; delay that platform's launch post by 15 min |
| PDF download shows "Request access" | Change Google Drive sharing to "Anyone with link"; if urgent, use Gist URL instead |
| Reddit post removed by moderators | Wait 60 minutes; if not restored, post to r/homesteading and r/foraging instead |
| TikTok upload fails | Post natively in the app; do not use web upload tool |
| Kit landing page returns error | Check Kit status page; if outage, share Gist URL in bios temporarily |

Full decision trees: `projects/seedwarden/TRACK_B_LAUNCH_DAY_COMMON_ISSUES_DECISION_TREES.md`
Rollback procedures: `projects/seedwarden/TRACK_B_LAUNCH_DAY_ROLLBACK_PROCEDURES.md`

---

## Section 6: Key File Index

| Purpose | File |
|---------|------|
| Zone PDFs (8 files) | `projects/seedwarden/assets/zone-cards/` |
| Email automation copy | `projects/seedwarden/execution/TRACK_B_EMAIL_COPY_FINAL.md` |
| Social calendar (18 posts) | `projects/seedwarden/TRACK_B_SOCIAL_CALENDAR_MAY28_30.md` |
| Influencer contacts (15) | `projects/seedwarden/HERBALIST_OUTREACH_CONTACT_LIST.md` |
| Influencer DM templates (18 + 3 templates) | `projects/seedwarden/TRACK_B_HERBALIST_OUTREACH_MATRIX.md` |
| Launch-day runbook | `projects/seedwarden/MAY_30_LAUNCH_DAY_RUNBOOK.md` |
| Kit setup guide | `projects/seedwarden/MAY_27_GATE_3_DEPLOYMENT_SCRIPT.md` |
| Monitoring checkpoints | `projects/seedwarden/TRACK_B_MONITORING_CHECKPOINTS.md` |
| Contingency decision trees | `projects/seedwarden/TRACK_B_LAUNCH_DAY_COMMON_ISSUES_DECISION_TREES.md` |
| Rollback procedures | `projects/seedwarden/TRACK_B_LAUNCH_DAY_ROLLBACK_PROCEDURES.md` |
| Logo | `projects/seedwarden/logos/seedwarden_logo_1.png` |
| Pre-activation readiness report | `projects/seedwarden/track-b-activation/READINESS_REPORT_JUNE_1.md` |

---

*Activation runbook created: June 1, 2026.*
*Execute Section 2 and 3 once all 5 user gates in Section 1 are marked complete.*
