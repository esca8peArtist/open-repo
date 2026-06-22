---
title: "Kit Email Send Sequence — Phase 3 Launch Sprint"
created: 2026-06-22
session: 3904
status: verified-ready
platform: Kit (ConvertKit)
scope: Launch day through Week 4 (June 22 – July 13)
---

# Kit Email Send Sequence — Phase 3 Launch Sprint

Verified session 3904 (June 22). Four kit emails staged in `projects/seedwarden/phase-3/`. Sequence covers launch day through Week 4 retrospective.

---

## Template Consistency Audit

All four emails reviewed against the following standards:

| Standard | Launch Email | Week 2 | Week 3 | Week 4 |
|----------|-------------|--------|--------|--------|
| Subject line present | YES | YES | YES | YES |
| Preview text present | YES | YES | NO | YES |
| Body prose complete | YES | YES | YES | Template (fill-ins) |
| Unsubscribe footer | YES | YES | YES | YES |
| Etsy link placeholder | YES | YES | YES | YES |
| Sender name placeholder | YES | NO | NO | YES |
| Pre-send checklist | YES | NO | NO | YES |

Issues found and noted per email below.

---

## Email 1: Launch Day

**File**: `projects/seedwarden/phase-3/kit-email-launch-day-june22.md`
**Send date**: 2026-06-22 (today)
**Send time**: 9am subscriber time (Kit timezone setting)
**Audience**: Full list — existing 500-buyer list + pre-launch sign-ups
**Subject**: Medicinal herbs collection — live today
**Preview text**: Five practitioner bundles. Early-buyer code inside.
**Word count**: ~200

### Species Data Accuracy

- Five bundles named: Women's Health, Respiratory, Immunity, Sleep, Digestive — correct
- Price range: $25–$40 per bundle; full practitioner set $120–$150 — matches Phase 3 pricing architecture
- Evidence-tier claims: "Evidence-tiered therapeutic claims" — accurate and FTC-compliant
- Drug-herb interactions: "Complete contraindication tables with drug-herb interactions" — accurate
- FGV sourcing: "Forest Grown Verified sourcing guidance for every at-risk species" — accurate (Black Cohosh, Goldenseal, Echinacea angustifolia are all at-risk species in the collection)
- All species data: verified against PHOTO_ATTRIBUTION_LOG.md species list

### Fill-Ins Required Before Send

- [ ] Replace `[ETSY_SHOP_URL]` in "SHOP NOW" CTA with full Etsy collection URL
- [ ] Replace `[Your name]` with sender name
- [ ] Verify EXISTING15 discount code is active in Etsy seller dashboard with June 28 expiry date
- [ ] Set Kit send time to 9am in subscriber timezone

### Early-Buyer Code

Code: **EXISTING15** (15% off)
Expiry: **June 28** (6-day window from launch)
After June 28: Code must be deactivated in Etsy seller dashboard to prevent continued use

---

## Email 2: Week 2 — Inside the Immunity Bundle

**File**: `projects/seedwarden/phase-3/kit-email-week2-immunity-bundle.md`
**Send date**: 2026-06-29
**Send time**: 9am subscriber time
**Audience**: Full list
**Subject**: Goldenseal, Echinacea, Ashwagandha — what the Immunity bundle covers
**Preview text**: And why the CITES sidebar is in there.
**Word count**: ~310

### Species Data Accuracy

- Echinacea: two species treated as separate entries (E. purpurea and E. angustifolia) — correct
- Cochrane review (Karsch-Völk, 2015) — verified citation; Rauš 2021 trial — plausible; verify spelling of author name before send (Rauš vs. Raus)
- Asteraceae allergy caution noted — correct and clinically important
- Ashwagandha thyroid medication and pregnancy contraindications — mandatory warnings correctly flagged
- Elderberry immunity framing (fermentation, immune activation) distinct from Respiratory framing (raw berry toxicity, sambunigrin) — correct
- 2019 Hawkins meta-analysis for elderberry — verified, consistent with Week 1 blog post citations
- Goldenseal CITES Appendix II sidebar described as 200-word, written for direct client distribution — consistent with attribution log entries

### Issues Found

- [ ] **Missing preview text in file**: File does not have a `preview-text` header label (though the text "And why the CITES sidebar is in there." is present). Verify this maps to Kit's preview text field when setting up the broadcast.
- [ ] **Missing sender name**: No `[Your name]` signature. Week 2 email ends without a sign-off name. Add sender name before scheduling.
- [ ] **Bundle upload date placeholder**: Body says "The Immunity bundle uploads July 20." Verify this date is confirmed before send. If Immunity bundle upload date changes, update this sentence.
- [ ] **Link placeholder**: `[Link to Week 2 blog post: Goldenseal conservation and CITES]` — replace with actual URL of Week 2 blog post once published July 1. If scheduling the email before July 1, use a placeholder URL or hold the email until after publication.
- [ ] **Etsy shop link**: `[Etsy shop link]` placeholder — replace with full collection URL

### Fill-Ins Required Before Send

1. Add sender name sign-off
2. Confirm Immunity bundle upload date (July 20 — verify)
3. Replace blog post link with actual URL (post publishes July 1)
4. Replace Etsy shop link with collection URL

---

## Email 3: Week 3 — Community Week / Questions Answered

**File**: `projects/seedwarden/phase-3/kit-email-week3-community-faq.md`
**Send date**: 2026-07-06
**Send time**: 9am subscriber time
**Audience**: Full list
**Subject**: Questions answered + a free species profile
**Preview text**: Three questions we have been seeing in our inbox, and a free download.
**Word count**: ~340

### Species Data Accuracy

- Student bundle recommendation (Women's Health or Respiratory): correct — both cover entry-level curriculum species
- Evidence-tier framing vocabulary: accurate description of Gold/Silver/Bronze system
- Wildcrafting bundle (Respiratory and Digestive): mullein, elderberry, dandelion — all correctly identified as having wildcrafting context
- Dandelion root content (roasted root coffee, bitters, inulin) — accurate; consistent with Digestive bundle scope as described in attribution log
- Mullein noxious weed designation in western states — accurate
- S. nigra vs. S. canadensis identification note — accurate
- Practitioner tier pricing ($120–$150, three-guide set) — consistent with launch email
- Practitioner tier goes live July 15 — verify this date

### Issues Found

- [ ] **Missing preview text in frontmatter**: File has `note:` metadata but no `preview-text:` field. Body states "Three questions we have been seeing in our inbox, and a free download." — this is what should go in Kit's preview text field.
- [ ] **Missing sender name**: No sign-off name in body.
- [ ] **Free download link placeholder**: `[BLACK COHOSH PROFILE LINK]` — replace with actual download URL (hosted file, Dropbox, or Etsy listing link) before sending.
- [ ] **Practitioner tier URL**: "The practitioner tier goes live July 15" — add link to Etsy listing or landing page when available.
- [ ] **Etsy shop link**: Replace with collection URL.

### Fill-Ins Required Before Send

1. Confirm practitioner tier July 15 launch date
2. Create Black Cohosh species profile as a free download (hosted file or Etsy free listing)
3. Replace `[BLACK COHOSH PROFILE LINK]` with actual URL
4. Add sender name sign-off
5. Add practitioner tier listing URL once available
6. Replace Etsy shop link with collection URL

**Note**: The free Black Cohosh profile serves as a re-engagement hook for non-purchasers. If the profile is not ready by July 3, replace that section with a free excerpt (2-3 paragraphs from the Women's Health bundle Black Cohosh chapter) embedded directly in the email body. Do not send with a broken or missing download link.

---

## Email 4: Week 4 — Retrospective

**File**: `projects/seedwarden/phase-3/kit-email-week4-retrospective.md`
**Send date**: 2026-07-13
**Send time**: 9am subscriber time (after pulling Etsy stats at 8am)
**Audience**: Full list
**Subject**: Three weeks of medicinal herbs — what happened + what's next
**Preview text**: A number, a quote, and a look at what's coming.
**Word count**: ~260

### Template Status

This email is a template with data fill-ins — not a complete email. It is correctly staged; all fill-in fields are documented and cannot be resolved without live data. The template will be complete once the following are available:

### Fill-Ins Required Before Send

- [ ] `[X]` — total practitioners / bundles sold: pull from Etsy Stats dashboard at 8am July 13 (before 9am scheduled send)
- [ ] `[TESTIMONIAL NAME]` and `[TESTIMONIAL QUOTE]` — written permission from practitioner required by July 12. If no testimonial secured by July 12, delete that section and replace with the alternative paragraph documented in the template file.
- [ ] `[PHASE 4 TEASER]` — one sentence. Confirm Phase 4 scope before July 10. If scope not confirmed, use: "Phase 4 scope is still being finalized — I will share details when the first draft is in."
- [ ] `[PRICE ADJUSTMENT NOTE]` — include or delete depending on pricing decision
- [ ] Replace `[Your name]` with sender name
- [ ] Replace `[Etsy shop link]` with collection URL

### Testimonial Permission Protocol

Written permission is mandatory before including any practitioner quote. Acceptable forms:
- Email reply confirming permission
- Direct message screenshot showing "yes, you can use that"
- Signed permission form

Do not include a testimonial based on a verbal agreement only.

---

## Full Send Sequence Timeline

| # | Email | File | Send Date | Status | Days Until Send |
|---|-------|------|-----------|--------|-----------------|
| 1 | Launch Day | `kit-email-launch-day-june22.md` | June 22, 9am | Send-ready (2 fill-ins) | TODAY |
| 2 | Week 2 — Immunity Bundle | `kit-email-week2-immunity-bundle.md` | June 29, 9am | Send-ready (5 fill-ins) | 7 days |
| 3 | Week 3 — Community FAQ | `kit-email-week3-community-faq.md` | July 6, 9am | Send-ready (5 fill-ins, free download needed) | 14 days |
| 4 | Week 4 — Retrospective | `kit-email-week4-retrospective.md` | July 13, 9am | Template (live data needed July 13 morning) | 21 days |

---

## Audience Segmentation Notes

All four emails send to the full list in this sprint. No segmentation is required for launch cadence.

Post-launch segmentation (automatic via Kit tags):
- Subscribers who click but do not purchase → tag `practitioner_nurture` → trigger Sequence B (see TRACK_B_EMAIL_SEQUENCES.md)
- Subscribers who purchase a bundle → standard post-purchase sequence (see PRE_LAUNCH_EMAIL_SEQUENCES.md)

---

## Subject Line Assessment

| Email | Subject Line | Character Count | Assessment |
|-------|-------------|-----------------|------------|
| Launch | "Medicinal herbs collection — live today" | 39 | Strong. Clear, no hype. |
| Week 2 | "Goldenseal, Echinacea, Ashwagandha — what the Immunity bundle covers" | 66 | Good. Species names function as search-intent keywords. Slightly long for mobile preview — first 40 chars carry the species names. |
| Week 3 | "Questions answered + a free species profile" | 43 | Good. "Free" and "answers" both drive open rate. |
| Week 4 | "Three weeks of medicinal herbs — what happened + what's next" | 59 | Good. Retrospective + forward hook structure proven for retention emails. |

All four subject lines are within 70 characters and avoid spam trigger words.

---

## Photo Attribution in Email Footers

Current email templates do not include embedded images requiring attribution. Photos appear in the PDF guides only, not in the email bodies. No photo attribution needed in email footers for this sprint.

If images are added to any email body (e.g. a feature image in a Substack broadcast version), use the attribution strings from `assets/phase-3-medicinal-herbs/PHOTO_ATTRIBUTION_LOG.md`.

---

*Sequence verified: 2026-06-22, session 3904.*
*Email files in `projects/seedwarden/phase-3/`.*
*Attribution log: `projects/seedwarden/assets/phase-3-medicinal-herbs/PHOTO_ATTRIBUTION_LOG.md`.*
