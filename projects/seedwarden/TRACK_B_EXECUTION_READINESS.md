---
title: "Track B Gate Execution Readiness Audit"
item: "Exploration Queue Item 57"
created: 2026-05-15
scope: Audit companion to TRACK_B_USER_GATES.md — gaps, UI verification, checklists, contingencies
status: TWO CRITICAL GAPS IDENTIFIED — see Gate 2 and Gate 3 sections
---

# Track B Gate Execution Readiness Audit

Companion to TRACK_B_USER_GATES.md. Do not rewrite that file. Read this document on May 14-15 before starting Gate 1.

---

## Gate 1 Readiness Audit — Social Accounts (May 15-18, ~30 min)

**Verdict: READY. Instructions in TRACK_B_USER_GATES.md are accurate.**

UI verification (May 15, 2026 research):

- Instagram path to Business account: documented as `Settings > Account > Switch to professional account`. Verified current path is `Settings and Privacy > Account > Switch to Professional Account`. The extra "and Privacy" in the label is cosmetic — the same sequence works.
- TikTok path: `Profile > Menu > Settings and privacy > Account > Switch to Business Account` — confirmed current.
- Pinterest convert path: The Gates doc says `Settings > Account settings > Account changes > Convert to business`. Current UI path per Pinterest help is `Settings > Account Management > Convert to a Business Account`. Labels differ; function is identical. If you cannot find "Account settings > Account changes," look for "Account Management" in the left-hand Settings menu.
- No major account creation flow changes found for any platform since May 5 document creation date.

**Gate 1 Pre-Execution Checklist:**
- [ ] `seedwarden_logo_1.png` downloaded to phone and computer
- [ ] wanka95@gmail.com password confirmed (you will receive verification emails on all three platforms)
- [ ] Decide your fallback handle in advance: `seedwarden.co` is first fallback for all three
- [ ] Pinterest note: if it says your personal account must be public before converting, flip it to public first
- [ ] Leave all three bio link fields blank — Kit URL goes in after Gate 3

---

## Gate 2 Readiness Audit — Canva Brand Kit (May 19-24, ~25 min)

**Verdict: CRITICAL GAP. Canva free plan limits Brand Kit to 3 colors. The Gates doc specifies 10 colors.**

**Gap detail**: The Gates doc and TRACK_B_CANVA_SETUP_AND_EXPORT_GUIDE.md instruct adding 10 colors (6 brand + 4 zone band) to the Brand Kit. Canva's free plan as of 2026 allows only 3 colors per Brand Kit. The document states "Brand Kit is available on the free tier" — this is true, but the 10-color spec requires Canva Pro ($15/mo or ~$120/yr).

**Fix options** (pick one before starting Gate 2):
1. Upgrade to Canva Pro ($15/mo, cancel after zone cards are built in June). Recommended — unlocks full palette, custom font upload, and unlimited Brand Kit colors.
2. Stay on free tier: add only the 3 most-used brand colors to the Kit (`#143b28`, `#F5EDD6`, `#8FA882`). Enter the remaining 7 hex codes manually per-design using the color picker. This works but adds ~3-5 min per design session.
3. Use a saved Canva "Color Palette" document (a workaround Canva free users use — pin a 1px design with all 10 colors as swatches, open it in a second tab for reference).

**Gate 2 Pre-Execution Checklist:**
- [ ] Decide: Pro upgrade or free-tier workaround (option 1, 2, or 3 above)
- [ ] If upgrading to Pro: do it before opening Brand Hub — the Kit appears after upgrade
- [ ] Font names `Playfair Display`, `Lato`, `Cormorant Garamond` are all free in Canva's library — no upload needed, search by name
- [ ] Logo upload path: Brand Hub > Brand Kit > Logos > "Upload a logo" — confirmed current
- [ ] Screenshot the Brand Kit after setup as Gate 2 verification

---

## Gate 3 Readiness Audit — Kit Email Account (May 27-28, ~35 min)

**Verdict: CRITICAL GAP. Kit free plan permits only 1 automation and 1 sequence. The Gates doc requires zone routing conditional logic, which is a paid feature.**

**Gap detail**: The Gates doc instructs building an automation that routes 8 zone variants of Email 1 using conditional logic ("If subscriber has tag zone-5, send Email 1 Zone 5 variant"). Kit's free Newsletter plan explicitly does not support conditional/event-based steps in automations. It supports 1 basic (linear) Visual Automation and 1 Sequence only. The zone routing architecture as documented requires the Creator plan ($33/mo).

**Fix options** (pick one before starting Gate 3):
1. Upgrade to Kit Creator ($33/mo). Unlocks unlimited automations, sequences, and conditional logic. Recommended for the full zone-routing architecture.
2. Simplify to single-zone launch: use the 1 free sequence to deliver one zone-agnostic welcome email (remove the zone dropdown from the landing page form; deliver a generic "getting started" card). Reduces segmentation value but costs $0 and launches on time.
3. Manual hybrid: keep the zone dropdown on the form, but manually send zone cards each day during Week 1 as subscribers arrive. Feasible if early volume is low (under 20 signups/day). Revisit automation at the 50-subscriber mark.

**Note on the stale date in Email 5**: Gates doc already flags this. Remove "May 20 (tomorrow)" before saving Email 5. Confirmed still required.

**Gate 3 Pre-Execution Checklist:**
- [ ] Decide: Creator upgrade or simplified free-tier approach before starting
- [ ] If free tier: remove zone dropdown from landing page form and simplify Email 1 to one version
- [ ] If upgrading: enter card at kit.com — no credit card required to create the free account first, then upgrade in-app
- [ ] Have 2 secondary test email addresses ready (not wanka95@gmail.com) for the 3-test protocol
- [ ] Zone card PDFs must exist in Google Drive before building Email 1 — confirm zone cards are built in Canva first
- [ ] Coupon code SEEDWARDEN15 must be created in Etsy before Email 5 goes live (Etsy Shop Manager > Marketing > Sales and Discounts)

---

## Documentation Gap Assessment

| Gap | Severity | Location in Gates doc | Fix |
|---|---|---|---|
| Canva free plan: 3-color limit vs. 10-color spec | High | Gate 2 steps | Upgrade to Pro or use workaround |
| Kit free plan: no conditional logic for zone routing | High | Gate 3 steps | Upgrade to Creator or simplify launch |
| Pinterest UI label change ("Account Management" vs. "Account changes") | Low | Gate 1 Pinterest step | Navigate by function, not label |
| Instagram path label: "Settings and Privacy" vs. "Settings" | Low | Gate 1 Instagram step | Same step, cosmetic label difference |
| Kit: zone card PDFs must exist before Email 1 is built (dependency not stated explicitly) | Medium | Gate 3 sequence steps | Build zone cards in Canva before starting Gate 3 |
| No prerequisite: Etsy coupon code must be created before Email 5 | Medium | Gate 3 Email 5 | Create SEEDWARDEN15 coupon during Gate 3 session |

**Remaining content**: No other gaps. All email copy, hex codes, font names, bio copy, handle fallbacks, file paths, and posting schedules are complete and accurate.

---

## User Pre-Execution Checklist (Do May 14 Evening)

- [ ] Read this document in full
- [ ] Decide on Canva plan: free workaround vs. Pro upgrade
- [ ] Decide on Kit plan: free simplified vs. Creator upgrade
- [ ] Download `projects/seedwarden/logos/seedwarden_logo_1.png` to phone
- [ ] Confirm access to wanka95@gmail.com (check password, check inbox loads)
- [ ] Locate 1-2 secondary email addresses for Kit testing (personal, work, or temp)
- [ ] Note preferred fallback handle: `seedwarden.co` recommended for all three platforms

---

## Contingency Troubleshooting (Common Failure Scenarios)

**1. Username `seedwarden` is taken on Instagram or TikTok**
Try fallbacks in order: `seedwarden.co`, `seedwarden.seeds`, `seedwarden_guides`. If all taken on one platform, claim the best available and update the confirmation table. TikTok allows username changes every 30 days — claim fallback now, switch later if primary frees up.

**2. Pinterest says account must be public before converting to Business**
Go to Settings > Privacy and Data > Account privacy > uncheck "Secret board" or similar private-account setting. Make account public, then re-attempt the Business conversion.

**3. Canva Brand Kit only shows 3 color slots (free plan)**
You have hit the free-tier color limit. Either upgrade to Pro or use the manual hex-code workaround described in Gate 2 above. Do not try to add colors beyond the limit — Canva will not allow it.

**4. Kit free plan does not show the conditional routing steps**
The feature requires Creator plan. Do not try to work around it within the free automation builder — the option is locked. Decide: upgrade ($33/mo) or launch with simplified single-sequence flow.

**5. Zone card PDFs not ready when starting Gate 3**
Do not build Email 1 yet. Build all 8 zone cards in Canva first, export to `projects/seedwarden/assets/zone-cards/`, upload to Google Drive, copy download links, then return to Kit Email 1 build. Email 1 is unusable without the PDF download links.

**6. Email 1 arrives in test inbox's spam folder**
Check Kit sender email verification: Kit > Settings > Email > Sender email address — confirm wanka95@gmail.com is verified. If still going to spam, send from Kit's default `mail.kit.com` subdomain until a custom domain is configured in Phase 3.

**7. Kit 3-test protocol: test subscriber does not receive Email 1 within 5 minutes**
Check automation status: Kit > Automations > confirm automation is set to "Active" (not "Draft" or "Paused"). Also confirm the landing page form is connected to the automation trigger. If delay persists beyond 15 minutes, check Kit's email queue under Subscribers > find the test subscriber > view their event log.

---

*Audit created: 2026-05-15. Item 57. Sources: TRACK_B_USER_GATES.md (Item 48), TRACK_B_SOCIAL_ACCOUNT_CHECKLIST.md, TRACK_B_CANVA_SETUP_AND_EXPORT_GUIDE.md, TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md. Platform UI research: Instagram, TikTok, Pinterest help docs; Canva pricing pages; Kit pricing and help pages (all verified May 2026).*
