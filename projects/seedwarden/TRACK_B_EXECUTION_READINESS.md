---
title: "Track B Gate Execution Readiness Audit"
item: "Exploration Queue Item 57"
created: 2026-05-15
scope: Audit companion to TRACK_B_USER_GATES.md — gaps, UI verification, checklists, contingencies
status: TWO CRITICAL GAPS IDENTIFIED — user decision required before Gate 2 and Gate 3 execution
---

# Track B Gate Execution Readiness Audit

Companion to TRACK_B_USER_GATES.md. Read this document before starting Gate 1. Do not rewrite TRACK_B_USER_GATES.md — this audit supplements it.

---

## Gate 1 Readiness Audit — Social Accounts (May 15-18, ~30 min)

**Verdict: READY. Instructions in TRACK_B_USER_GATES.md are accurate and actionable.**

### UI Verification (researched May 15, 2026)

- Instagram path to Business account: documented as `Settings > Account > Switch to professional account`. Current Instagram path is `Settings and Privacy > Account > Switch to Professional Account`. The extra "and Privacy" in the label is cosmetic — the same sequence reaches the same screen.
- TikTok path: `Profile > Menu > Settings and privacy > Account > Switch to Business Account` — confirmed current as of May 2026.
- Pinterest convert path: TRACK_B_USER_GATES.md says `Settings > Account settings > Account changes > Convert to business`. Current Pinterest UI path is `Settings > Account Management > Convert to a Business Account`. Labels differ; function is identical. If you cannot find "Account settings > Account changes," look for "Account Management" in the left-hand Settings menu.
- Instagram and Pinterest UI labels have drifted slightly from the documented steps (both written May 5). No major account creation flow changes found for any platform.

### Documentation Completeness

Gate 1 is fully documented. Every field value, bio text, handle fallback, and file path is specified. No decisions are required during execution — all values are pre-loaded in the steps.

One minor gap: TRACK_B_SOCIAL_ACCOUNT_CHECKLIST.md Step 4 for Pinterest includes optional steps for claiming your website domain and enabling Rich Pins (Steps 4-5). These are Phase 3 enhancements and are correctly marked optional, but TRACK_B_USER_GATES.md does not mention them at all. This is not a blocker — skip those steps at Gate 1 execution time.

### Gate 1 Pre-Execution Checklist

- [ ] `seedwarden_logo_1.png` downloaded to phone and computer (file confirmed at `projects/seedwarden/logos/seedwarden_logo_1.png`)
- [ ] wanka95@gmail.com password confirmed — you will receive verification emails on all three platforms
- [ ] Decide fallback handle in advance: `seedwarden.co` is first fallback for all three platforms
- [ ] Pinterest note: if it says your personal account must be public before converting to Business, flip it to public first, then convert
- [ ] Leave all three bio link fields blank — Kit URL goes in after Gate 3

---

## Gate 2 Readiness Audit — Canva Brand Kit (May 19-24, ~25 min)

**Verdict: CRITICAL GAP. Canva free plan limits Brand Kit to 3 colors. The Gates doc specifies 10 colors. A decision is required before starting Gate 2.**

### Gap Detail

TRACK_B_USER_GATES.md and TRACK_B_CANVA_SETUP_AND_EXPORT_GUIDE.md both instruct adding 10 colors to the Brand Kit (6 brand colors + 4 zone band colors). Canva's free plan as of 2026 allows only 3 colors per Brand Kit.

The contradiction is internal: TRACK_B_CANVA_SETUP_AND_EXPORT_GUIDE.md Part 8 footer states "Export specs reflect May 2026 Canva Free tier capabilities. Canva Pro not required for any Track B deliverable." However, the 10-color Brand Kit spec in that same document requires Canva Pro ($15/mo). The footer statement is incorrect.

### Fix Options (pick one before starting Gate 2)

1. **Upgrade to Canva Pro ($15/mo, ~$120/yr).** Recommended — unlocks full palette (up to 100 Brand Kits, unlimited colors per Kit), custom font upload, and advanced export options. Cancel after zone cards are built in June. Total cost: $15-30 for two months.
2. **Stay on free tier — 3-color Brand Kit.** Add only the 3 most-used brand colors: `#143b28` (Deep Forest Green), `#F5EDD6` (Warm Cream), `#8FA882` (Sage). Enter the remaining 7 hex codes manually per-design using the color picker. Adds ~3-5 min per design session but costs $0.
3. **Free-tier workaround — "color reference" document.** Create a 1-page Canva design with all 10 colors as swatches, pin it in a second browser tab during design sessions as a reference. Paste hex codes from that tab. This is the same net effect as Option 2 but slightly faster lookup.

### Additional Gate 2 Notes

- Font names `Playfair Display`, `Lato`, `Cormorant Garamond` are all free in Canva's library. No upload needed regardless of plan tier.
- Logo upload path `Brand Hub > Brand Kit > Logos > "Upload a logo"` is confirmed current.
- Zone card production (7.5-9 hours, documented in CANVA_ZONE_CARD_BATCH_WORKFLOW.md) must be complete before Gate 3 Email 1 can be built. Do not start Gate 3 until all 8 zone card PDFs are exported and uploaded to Google Drive.

### Gate 2 Pre-Execution Checklist

- [ ] Decision made: Pro upgrade or free-tier workaround (Option 1, 2, or 3 above)
- [ ] If upgrading to Pro: upgrade before opening Brand Hub — the expanded color slots appear after upgrade
- [ ] 8 zone card PDFs are not required at Gate 2 start — Brand Kit setup comes first, then card production
- [ ] Screenshot the Brand Kit overview screen after setup (colors, fonts, logo visible) — this is the Gate 2 verification artifact

---

## Gate 3 Readiness Audit — Kit Email Account (May 27-28, ~35 min)

**Verdict: CRITICAL GAP. Kit free plan does not include email sequences and restricts automations to 1 basic flow. The zone routing architecture as documented requires the Creator plan. A decision is required before starting Gate 3.**

### Gap Detail

TRACK_B_USER_GATES.md and TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md instruct building a 5-email welcome sequence with zone-routing conditional logic ("If subscriber has tag zone-5, send Email 1 Zone 5 variant"). Kit's free Newsletter plan as of 2026 provides only 1 basic Visual Automation and no email sequences. KIT_SETUP_NOTES.md Step 1 states "Conditional logic for zone routing is available on free tier" — this statement is inaccurate. Sequences are a Creator-tier feature.

Confirmed from Kit pricing (kit.com/pricing, May 2026): Free plan = 1 automation, no sequences. Creator plan ($33/mo) = unlimited automations, unlimited sequences, conditional logic.

### Fix Options (pick one before starting Gate 3)

1. **Upgrade to Kit Creator ($33/mo).** Recommended for the full zone-routing architecture documented. Unlocks unlimited automations, unlimited sequences, and tag-based conditional routing. Required if you want all 8 zone variants delivered automatically.
2. **Stay on free tier — simplified single-sequence launch.** Remove the zone dropdown from the landing page form. Build 1 generic welcome email (Email 1, no zone personalization) using the 1 free sequence. Delivers a one-size-fits-all welcome message instead of a zone-specific card. Reduces segmentation value but costs $0 and launches on time. Zone personalization can be added in Phase 3 after upgrading.
3. **Manual hybrid.** Keep the zone dropdown on the form, but manually email zone cards each day during Week 1 as subscribers arrive. Feasible only if early volume is very low (under 10-15 signups/day). Revisit automation upgrade at the 30-subscriber mark.

### Tag Naming Discrepancy (Documentation Conflict)

TRACK_B_USER_GATES.md specifies these 7 cohort tags: `seed-saver`, `forager`, `food-preserver`, `homesteader`, `medicinal-herbs`, `vip-buyer`, `phase-1-buyer`.

KIT_SETUP_NOTES.md and TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md specify different names: `seed-saver`, `city-grower`, `preservationist`, `forager`, `prepper`, `homesteader`, `etsy-buyer` (and add `gift-buyer` in KIT_SETUP_NOTES.md).

These two tag lists do not match. The automation logic in TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md (which builds the actual click-to-tag rules) uses `seed-saver`, `city-grower`, and `preservationist`. Use the TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md tag names when creating tags in Kit — those are wired to the automation logic. Ignore the tag names in TRACK_B_USER_GATES.md for this purpose.

### The 3-Test Protocol — Who Are the Test Recipients?

TRACK_B_USER_GATES.md mentions a "3-person test delivery procedure." This is not 3 separate people — it is 3 automated system tests using Gmail address aliases. The tests use `wanka95+test1@gmail.com` and `wanka95+test2@gmail.com` (Gmail plus-addressing: all mail routes to wanka95@gmail.com). A third secondary email address is needed for the behavioral tag test (TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md Step 6 Test 3). Prepare these before Gate 3:

- `wanka95+test1@gmail.com` — Zone 5 signup test
- `wanka95+test2@gmail.com` — Zone 8 signup test
- A third address: a personal secondary Gmail, work email, or any mailbox you can access

### Additional Gate 3 Dependencies

- Zone card PDFs must exist in Google Drive before Email 1 can be built. Build all 8 zone cards in Canva, export to `projects/seedwarden/assets/zone-cards/`, upload to Google Drive, then return to Kit Email 1.
- Coupon code `SEEDWARDEN15` must be created in Etsy before Email 5 goes live. Path: Etsy Shop Manager > Marketing > Sales and Discounts > Create Discount. This is not mentioned in TRACK_B_USER_GATES.md and is only documented in TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md Step 5.
- Email 5 stale date: Remove "May 20 (tomorrow)" from the body before saving. Replace with "the guide preview." Already flagged in TRACK_B_USER_GATES.md — confirmed still required.

### Gate 3 Pre-Execution Checklist

- [ ] Decision made: Creator plan upgrade or simplified free-tier approach
- [ ] If free tier: plan to remove zone dropdown and simplify Email 1 to one version
- [ ] If upgrading: enter card at kit.com — no credit card required for free account creation; upgrade in-app
- [ ] 2-3 secondary test email addresses identified and accessible (not wanka95@gmail.com)
- [ ] Zone card PDFs confirmed built and uploaded to Google Drive before starting Email 1
- [ ] Etsy coupon code `SEEDWARDEN15` created before Email 5 is loaded

---

## Documentation Gap Assessment

| Gap | Severity | Location in Gates doc | Fix |
|---|---|---|---|
| Canva free plan: 3-color limit vs. 10-color spec | High | Gate 2 steps | Upgrade to Pro or use manual hex workaround |
| Kit free plan: no sequences for zone routing | High | Gate 3 steps | Upgrade to Creator or simplify to single-sequence launch |
| KIT_SETUP_NOTES.md incorrect claim ("conditional logic free on free tier") | High | KIT_SETUP_NOTES.md Step 1 | Do not rely on this statement; see actual kit.com pricing |
| Tag name conflict between TRACK_B_USER_GATES.md and KIT_SETUP_NOTES.md | Medium | Gate 3 tag list | Use TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md tag names — those are wired to automation logic |
| Etsy coupon SEEDWARDEN15 must exist before Email 5 goes live | Medium | Gate 3 — not mentioned | Create during Gate 3 session |
| Zone card PDFs must exist before Email 1 build (dependency not stated explicitly) | Medium | Gate 3 sequence steps | Build zone cards in Canva before starting Gate 3 |
| Pinterest UI label change ("Account Management" vs. "Account changes") | Low | Gate 1 Pinterest step | Navigate by function, not label |
| Instagram path label: "Settings and Privacy" vs. "Settings" | Low | Gate 1 Instagram step | Same step, cosmetic label difference |
| TRACK_B_CANVA_SETUP_AND_EXPORT_GUIDE.md footer incorrectly states "Pro not required" | Low | Part 8 footer note | Disregard that footer claim; Pro is required for 10-color Kit |

**Everything else is complete and accurate.** All email copy, hex codes, font names, bio copy, handle fallbacks, file paths, export specs, and posting schedules are present and consistent across the referenced documents.

---

## User Pre-Execution Checklist (Do Before Gate 1 Start)

- [ ] Read this document in full before starting any gate
- [ ] Decide on Canva plan: free workaround vs. Pro upgrade ($15/mo)
- [ ] Decide on Kit plan: free simplified vs. Creator upgrade ($33/mo)
- [ ] Download `projects/seedwarden/logos/seedwarden_logo_1.png` to phone and computer
- [ ] Confirm wanka95@gmail.com is accessible (check password, confirm inbox loads, check no 2FA issues)
- [ ] Identify 2-3 secondary email addresses for Kit testing — these should be inboxes you can actually open to check delivery
- [ ] Note preferred fallback handle: `seedwarden.co` recommended for all three platforms
- [ ] Note: Gates 1 and 2 can run in parallel (no dependency). Gate 3 cannot start fully until Gate 2 (Canva Brand Kit and zone card production) is complete.

---

## Contingency Troubleshooting (Common Failure Scenarios)

**1. Username `seedwarden` is taken on Instagram or TikTok.**
Try fallbacks in order: `seedwarden.co`, `seedwarden.seeds`, `seedwarden_guides`. If all taken on one platform, claim the best available and update the confirmation table in TRACK_B_SOCIAL_ACCOUNT_CHECKLIST.md. TikTok allows username changes once every 30 days — claim fallback now, change later if primary frees up.

**2. Pinterest says account must be public before converting to Business.**
Go to Settings > Privacy and Data > Account Privacy > uncheck any private account or secret setting. Make account public, then re-attempt the Business conversion.

**3. Canva Brand Kit only shows 3 color slots (free plan).**
You have hit the free-tier limit. Either upgrade to Pro or use the manual hex-code workaround from Gate 2 above. Do not attempt to add colors beyond the limit — Canva will block it.

**4. Kit free plan does not show sequences or conditional routing steps.**
These features require the Creator plan. Do not try to build around the limitation inside the free automation builder — the option is locked. Decision: upgrade ($33/mo) or launch with the simplified single-sequence flow.

**5. Zone card PDFs not ready when starting Gate 3.**
Do not build Email 1. Build all 8 zone cards in Canva first, export to `projects/seedwarden/assets/zone-cards/`, upload to Google Drive, copy the direct download links (use the `/uc?export=download&id=` URL format, not the standard `/view` share URL), then return to Kit Email 1 build.

**6. Email 1 arrives in the test inbox's spam folder.**
Check Kit sender email verification: Kit > Settings > Email > Sender email address — confirm wanka95@gmail.com is verified. If still going to spam, send from Kit's default `mail.kit.com` subdomain. Adding a custom domain is a Phase 3 improvement.

**7. Kit 3-test protocol: test subscriber does not receive Email 1 within 5 minutes.**
Check automation status: Kit > Automations > confirm automation is set to "Active" (not "Draft" or "Paused"). Confirm the landing page form is connected to the automation trigger. If delay persists beyond 15 minutes, check Kit's email queue: Subscribers > find the test subscriber > view their event log.

**8. Canva export fails after multiple attempts (PDF or PNG).**
Most common causes: browser cache issue (clear cache, retry), browser incompatibility (try Chrome instead of Safari), or design file too complex (reduce element count). If export still fails after 3 attempts in Chrome, contact Canva support at help.canva.com. Alternative: Figma free tier supports similar export specs and is a viable fallback for zone card production.

---

*Audit created: 2026-05-15 (Item 57). Updated with complete tag conflict analysis, Kit pricing verification, and 3-test protocol clarification. Sources: TRACK_B_USER_GATES.md, TRACK_B_SOCIAL_ACCOUNT_CHECKLIST.md, TRACK_B_CANVA_SETUP_AND_EXPORT_GUIDE.md, TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md, KIT_SETUP_NOTES.md. Platform pricing verified against kit.com/pricing and Canva pricing pages, May 2026.*
