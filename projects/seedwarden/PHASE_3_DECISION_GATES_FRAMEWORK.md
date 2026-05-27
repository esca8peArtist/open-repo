---
title: "Phase 3 Decision Gates Framework — Medicinal Herbs"
date: 2026-05-27
status: production-ready
tags: [seedwarden, phase-3, decision-gates, go-no-go, milestone, production]
---

# Phase 3 Decision Gates Framework

**Four gates govern the June 22–July 13 sprint.** Each gate has clear inputs, a binary go/no-go evaluation, and explicit escalation procedures if the gate fails. No gate failure cancels the sprint — each has a defined recovery path.

---

## Gate 1 — Pre-Sprint Authorization (June 15 Deadline)

**Purpose**: Confirm all sourcing, design, and outreach actions that have non-zero lead times are either complete or in-progress before they become blocking.

**Check by**: June 15, 2026.

| Input | Standard | Status if Green | Status if Red |
|---|---|---|---|
| Mountain Rose Herbs order placed | Placed by June 13 (recommended) or June 15 (hard) | Confirmed order receipt email in hand | Not placed: order immediately + place Frontier Co-op simultaneously |
| Elderberry potted shrub purchased | Purchased from local garden center | Plant in hand | Not available locally: check Prairie Moon + activate iNaturalist CC fallback |
| Canva palette decision | 6 hex codes confirmed or auto-locked | Logged in WORKLOG.md | No decision: auto-lock to production hex codes — no further action needed |
| Goldenseal path decision | Path 1 order receipt OR Path 2 CC filenames logged | Logged in WORKLOG.md | Neither done by June 8 (already missed by June 15): log Path 2 immediately |
| AHG peer reviewer outreach initiated | 5–8 emails sent June 8 | At least 1 response received | No response yet: send follow-up wave same day + expand to UpS network |

**Gate 1 Go decision**: At least Mountain Rose Herbs order placed + palette decision logged = proceed to pre-sprint photography window.

**Gate 1 No-Go**: Mountain Rose Herbs order not placed by June 15 — emergency action: place order and Frontier Co-op backup simultaneously on June 15. Sprint start date unchanged. Photography may compress to June 21 only (dried herb session, 4 hours — still sufficient for all 5 bundles). No upload dates change.

---

## Gate 2 — Photography and Pre-Sprint Assets Complete (June 21 Deadline)

**Purpose**: Confirm all sprint-prerequisite assets are in place before the June 22 Day 1 writing session.

**Check by**: June 21, 2026 EOD.

| Input | Standard | Pass | Fail + Response |
|---|---|---|---|
| Attribution log complete | All CC sources logged in PHOTO_ATTRIBUTION_LOG.md | File exists, all heroes attributed | Missing attributions: complete same day; sprint cannot start without this |
| Canva Brand Kit loaded | Phase 3 palette visible in Brand Kit | Test export shows correct colors | Kit not loaded: load now (15 min); zero float on this |
| At least 1 flat-lay photo per bundle | 5 flat-lay images exported at 2400×2400px | PHOTO_MANIFEST.csv shows 5 flat-lays | Missing flat-lays: use Wikimedia CC bundle-appropriate images as listing slot 3 placeholder; shoot retroactively Week 1 |
| Kit landing pages tested | 3 lead magnet pages functional | Test download confirmed | Pages broken: sprint proceeds; Kit landing pages are Week 1 parallel task, not a June 22 blocker |
| Phase 2 launch gates still met | Forager cohort >20%, native plants >1.5% | Both above threshold | One gate below: continue sprint and hold upload until June 29 re-check shows recovery |

**Gate 2 Go**: Attribution log complete + Brand Kit loaded = sprint proceeds June 22. All other inputs are preferable but not sprint-blocking.

**Gate 2 No-Go**: Attribution log incomplete — complete it June 21 evening. If still incomplete at midnight June 21, log the available CC sources and mark any unlogged sources in red for completion by June 24 D3 pace gate. Do not delay sprint start for attribution completion.

---

## Gate 3 — Mid-Sprint Checkpoint (June 29 Milestone)

**Purpose**: Verify writing is on pace and Women's Health is live before committing full resource to Immunity + Sleep writing.

**Check by**: June 29, 2026 EOD.

| Input | Standard | Pass | Fail + Response |
|---|---|---|---|
| Women's Health upload live | Listed on Etsy, download confirmed | Etsy listing URL in hand | Not live: upload immediately; compress upload checklist to 30 min; do not write anything else until upload complete |
| Writing velocity confirmed | 300+ words/hour over Days D1–D7 | WH delivered 3,800w in 7 days = ~20 hrs writing | Below velocity: already activated Option C at D3 pace gate; confirm Option C is in effect |
| Week 2 writing plan finalized | Option A or C confirmed | Option locked, Day 8 task clear | Unclear: default to Option C; begin Immunity writing June 29 afternoon after upload |
| AHG reviewer status | Reviewer confirmed OR no-reviewer path confirmed | Either state documented in WORKLOG.md | Still pursuing: continue sprint; add reviewer quote retroactively; no action needed today |
| Design progress | WH and Resp covers complete | Both exported and visible in Canva | Covers not done: Google Docs PDF fallback for Resp; continue writing |

**Gate 3 Go**: Women's Health live on Etsy = full green. Proceed with Immunity and Sleep writing as planned.

**Gate 3 Partial (Women's Health not yet uploaded)**: Upload June 29 is zero-float. If upload is blocked by a QA failure (file over 5MB, broken link, etc.) — fix and upload before any other activity that day. Do not write until WH is live.

**Gate 3 No-Go**: Women's Health upload impossible June 29 due to Etsy technical issue — attempt at 2pm, 6pm, and 10pm ET same day. If Etsy downtime persists past midnight: upload June 30 morning. Resp shifts from July 6 to July 8. Sleep from July 13 to July 15. Practitioner tier from July 15 to July 17. Revenue delay is 2 days, not a sprint failure.

---

## Gate 4 — Pre-Upload Assets Complete (July 8 Deadline)

**Purpose**: Verify all 5 PDFs are export-ready, FTC compliance is confirmed, and queued listings for Sleep, Immunity, and Digestive are staged before the July 13 sprint close upload.

**Check by**: July 8, 2026 EOD (5 days before sprint close).

| Input | Standard | Pass | Fail + Response |
|---|---|---|---|
| All 5 PDFs exported | Under 5MB, no placeholder text, no broken image links | 5 files confirmed in `/products/` folder | Failing file: identify specific issue; oversized PDF = compress images in Canva; placeholder = find and fix |
| FTC compliance review complete | All therapeutic claims use qualifying language (see Appendix A, critical path v8.0) | No red-flag claims in any bundle | Uncorrectable claim found: hold that bundle upload 48 hrs for rewrite; do not hold other bundles |
| Cover images confirmed for all 5 bundles | 5 covers exported at 2400×2400px; thumbnails readable at 170×135px | All 5 verified | Missing cover: Google Docs placeholder cover (20 min) enables upload; swap for Canva cover retroactively |
| Etsy draft listings staged | Sleep, Immunity, Digestive drafts staged in Seller Dashboard | 3 listings ready to publish | Not staged: 20 min per listing; do now before any other task |
| Practitioner variant staged | 10-pack listing ready for July 15 activation | Draft visible in Seller Dashboard | Not staged: stage July 11–12 (D20–D21); 30 min |

**Gate 4 Go**: At minimum, PDF for Sleep bundle is export-ready and Etsy draft staged = July 13 sprint close upload proceeds.

**Gate 4 No-Go** (Sleep PDF not ready July 8): Float Day 1 (July 12) resolves the outstanding issue. Sleep upload shifts from July 13 to July 14 maximum — still within practitioner tier activation window (2-day gap between July 14 Sleep upload and July 16 practitioner tier activation is preserved). This is not a sprint failure; it is a 1-day slip absorbed by existing float.

---

## Gate Decision Authority and Escalation

All gate decisions are made by the user. There are no external approval dependencies.

**At each gate, the decision log entry in WORKLOG.md should contain**:
- Date and time of check
- Pass/fail status per input row
- Go/no-go decision
- If no-go: specific recovery action taken, revised dates if applicable

**Escalation rule**: If two consecutive gates show the same failure mode (e.g., writing pace below threshold at both D3 pace gate and June 29 checkpoint), escalate immediately to Option C if not already activated. Option C is the pre-designed recovery path — there is no further escalation beyond Option C.

**Post-sprint gates** (not part of the June 22–July 13 window):
- July 20 Immunity upload: no formal gate; proceed unless FTC issue found in final review pass
- August 3 Digestive upload: no formal gate; Kit FORAGER20 trigger activates automatically on upload
