---
title: ModRun Wave 1 Launch Timeline — T+0 to T+7
date: 2026-05-06
status: pre-staged
trigger: T+0 = the moment test print is confirmed successful
related: post-test-print-staging-guide.md, post-test-print-supplier-outreach.md, post-test-print-fulfillment-dryrun.md, DAY1_LAUNCH_OPERATIONS_PLAYBOOK.md
---

# ModRun Wave 1 Launch Timeline

**Reading this document**: T+0 is the hour you confirm the test print passed all tolerance checks. Every subsequent day (T+1 through T+7) is a calendar day from that confirmation. The timeline is designed so that Etsy goes live on T+4 morning with enough buffer for supplier negotiation, photo refinement, and dry-run validation — but not so much buffer that momentum dies.

**Owner legend:**
- **User** = Physical actions that require your hands (photography, printing, packing, decisions)
- **Orchestrator** = Research, template generation, analytics, content drafting — delegatable to an AI agent
- **Both** = Requires human judgment plus pre-staged materials

---

## T+0 — Day 1: Test Print Confirmation

**Morning (upon receiving print)**

| Time | Action | Owner | Estimated Duration |
|---|---|---|---|
| 0:00 | Run tolerance validation table from DAY1_LAUNCH_OPERATIONS_PLAYBOOK.md Track A-1. Measure snap arm (1.4mm target), bore diameter, rail channel width with digital calipers | User | 15 min |
| 0:15 | Record all measurements. Circle Pass/Fail for each parameter | User | 5 min |
| 0:20 | Decision gate: All measurements within tolerance? → Proceed. Any functional failure? → Adjust FDM_TOLERANCE (±0.05mm increment), reprint one validation clip, re-measure. Do not proceed past this gate with known functional failures | User | — |
| 0:30 | Lock production settings card (from DAY1_LAUNCH_OPERATIONS_PLAYBOOK.md Track A-4) and post it at the printer | User | 5 min |
| 0:35 | If any STL regeneration was needed: `uv run python modrun_clip_b123d.py --output-dir ../stl/` and `uv run python modrun_rail_b123d.py --output-dir ../stl/` | User | 10 min |

**Success criteria for morning gate**: All 6 measurements from the tolerance table pass (or are within the ±0.5mm acceptable band). Production settings posted. STL files confirmed in `/projects/mfg-farm/stl/`.

---

**Afternoon (primary execution window)**

| Time | Action | Owner | Estimated Duration |
|---|---|---|---|
| 0:00 | Photo shoot — follow the shot list in post-test-print-staging-guide.md Phase 1 (8 shots, 25 min) | User | 25 min |
| 0:25 | Photo editing — Lightroom or Canva, apply settings from staging guide Phase 2. Export all 8 shots | User | 10 min |
| 0:35 | Etsy listing — open draft mode. Copy-paste title, description, tags from post-test-print-staging-guide.md Phase 3. Fill in actual dimensions. Upload photos | User | 15 min |
| 0:50 | Pre-flight checklist (staging guide Phase 4) — verify all 13 tags, confirm payment method active, check shipping template | User | 5 min |
| 0:55 | Supplier outreach — open post-test-print-supplier-outreach.md. Complete find-and-replace (YOUR_NAME, YOUR_CITY, YOUR_EMAIL). Send all 5 templates simultaneously | User | 20 min |
| 1:15 | Fulfillment dry run — begin Phase 1 pick list. QA parts. Pack 10 units. Generate test labels | User | 90–120 min |
| 3:00 | Fill in cost tracking spreadsheet (post-test-print-fulfillment-dryrun.md Phase 4) | User | 15 min |

**Decision gate at end of T+0 afternoon:**
- [ ] Etsy draft listing complete (not yet published — held until T+4 for full optimization and timing)
- [ ] All 5 supplier emails sent
- [ ] Dry run completed with cost tracking filled in
- [ ] Margin validation: all-in margin ≥ 60%?

If margin is below 60% or a major fulfillment issue was discovered, flag and resolve before T+1. Do not proceed to listing publication with an unresolved COGS problem.

**Evening (optional — defer if fatigued)**

| Action | Owner |
|---|---|
| Review dry-run defect log — any systemic issues (>10% defect rate) | User |
| Confirm Etsy shop-level settings are complete (banner, icon, About section, policies) | User |
| Set response to supplier outreach as a calendar reminder for T+3 | User |

---

## T+1 — Day 2: Supplier Negotiation Window Opens

**Morning**

| Action | Owner | Notes |
|---|---|---|
| Check inbox for supplier responses (eSUN and Shop4Mailers typically respond fastest — 24–48 hrs) | User | Use response tracker spreadsheet from supplier-outreach doc |
| If a response arrived with pricing above win threshold: draft counter-offer using negotiation guidance section | User | 5 min per counter-offer |
| Review Etsy listing draft one more time — does description read naturally? Are all dimensions filled in? | User | 10 min |

**Afternoon**

| Action | Owner | Notes |
|---|---|---|
| Etsy shop finalization: Complete all shop policies if not done on T+0 (return policy, shipping policy, privacy) | User | 20 min — incomplete policies suppress search ranking |
| Prepare Instagram launch post — crop the best lifestyle photo to 1080×1350px in Canva, draft caption | User | 15 min |
| Draft Reddit launch post for r/battlestations or r/cablefail — text and image ready, not yet posted | Orchestrator | Template below |
| Check: Is the Etsy shop URL clean and professional? (etsy.com/shop/[YOUR_SHOP_NAME]) | User | — |

**Reddit launch post draft (pre-written, ready to post on T+4):**

```
Title: Finally got my ModRun cable clips dialed in — parametric design, all the cables
  
r/battlestations (or r/cablefail)

After months of tolerating cable spaghetti under my desk, I designed these
from scratch in CadQuery and printed them on a Bambu P1S. The snap arm is 1.4mm
thick — tight enough to hold, flexible enough to remove without tools.

[ATTACH: lifestyle photo of desk with cables routed]

Available on Etsy if anyone wants a set: [ETSY LISTING URL]

Design notes in comments if anyone's curious about the parametric approach.
```

Customize the "design notes" comment with 2–3 sentences about the CadQuery parametric design process. Technical detail earns upvotes on r/battlestations and drives click-through to Etsy.

**Success criteria for T+1:**
- At least 1 supplier has responded (check Sent folder to confirm emails delivered)
- Etsy shop policies all complete
- Instagram post and Reddit post drafts ready (staged, not yet published)

---

## T+2 — Day 3: Supplier Negotiation + Listing Optimization

**Morning**

| Action | Owner | Notes |
|---|---|---|
| Respond to any supplier inquiries with counter-offers or confirmations | User | 5 min each |
| Log all supplier responses in tracking spreadsheet | User | — |
| Follow up on any supplier with no response (Template 5 one-sentence follow-up from supplier-outreach doc) | User | 5 min |

**Afternoon**

| Action | Owner | Notes |
|---|---|---|
| Return to Etsy draft listing — review once more with fresh eyes. Read the description aloud. Fix any awkward phrasing | User | 15 min |
| Prepare the "Complete the Setup" image (Shot 6 from staging guide — 3 clips on rail with cables routed) if not captured on T+0 | User | 20 min if needed |
| Research: Check eRank Keyword Explorer for your 13 tags. Are all within reasonable search volume? Any obvious swaps? | Orchestrator / User | 20 min — eRank Basic plan $9.99/month |
| Draft TikTok script (optional but high-return): 15-second video concept showing cable snapping into clip with audio. Script: [Cable goes in. Click. Done.] | Orchestrator | Pre-stage, film on T+3 |

**Success criteria for T+2:**
- Supplier negotiation is progressing (at least 2 of 5 have responded)
- Etsy listing is final — all fields complete, no placeholders, ready to publish
- eRank keyword check completed; any necessary tag swaps made in draft

---

## T+3 — Day 4: Pre-Launch Final Check

**Morning**

| Action | Owner | Notes |
|---|---|---|
| Print a test batch — 20 clips + 4 rails in production settings. This is your launch inventory | User | 90 min print time |
| While printing: Finalize any remaining supplier negotiations. Log final pricing in tracker | User | 30 min |
| Confirm at least 3 of 5 suppliers have responded. If Packlane or BETCKEY are non-responsive, that is acceptable — those are Phase 2 suppliers | User | — |

**Afternoon**

| Action | Owner | Notes |
|---|---|---|
| QA the launch inventory batch (same tolerance table as T+0 dry run) | User | 20 min |
| Set up the launch inventory shelf: sorted by color, counted, labeled | User | 10 min |
| Final Etsy listing review — one last read of the complete listing in preview mode | User | 10 min |
| Schedule the publish: Thursday 10 AM–2 PM Central is optimal for Etsy recency boost timing. Set a phone alarm if needed | User | 2 min |
| Final social media prep: TikTok filming if doing video (15-sec clip of snap engagement) | User | 20 min |

**Success criteria for T+3:**
- Launch inventory printed and QA'd (20+ clips, 4+ rail sections ready to ship)
- Etsy listing reviewed and scheduled for T+4 morning publish
- Supplier outreach: at least 3 of 5 with confirmed pricing or active negotiation
- Social media posts staged and ready

---

## T+4 — Day 5: Etsy Goes Live

**Morning (10 AM–12 PM Central — optimal publish window)**

| Time | Action | Owner | Notes |
|---|---|---|---|
| 10:00 AM | Publish Etsy listing | User | 2 minutes. Click Publish. |
| 10:05 AM | Post Reddit announcement (r/battlestations or r/cablefail) | User | Pre-written draft from T+1 |
| 10:30 AM | Post Instagram launch content | User | Pre-edited photo from T+0 |
| 11:00 AM | Optional: Post in r/3Dprinting (design post, not sales post — show the CadQuery parametric design process) | User | Community engagement, not direct sales pitch |

**Afternoon**

| Action | Owner | Notes |
|---|---|---|
| Check Etsy Search Visibility in Shop Manager — confirm listing has entered search | User | Takes 2–4 hours to index |
| Check Etsy listing on mobile — does thumbnail crop correctly? Is price visible? | User | 5 min |
| Respond to any Etsy messages within 2 hours | User | Critical for response rate metric |
| Log T+4 baseline: note listing views at end of day (even 1–3 views is normal on Day 1) | User | — |

**Success criteria for T+4:**
- Listing is live and indexed in Etsy search
- Social media posts published
- Zero critical errors (wrong price, wrong dimensions in description, broken listing URL)

---

## T+5 — Day 6: First Full Day of Monitoring

**Morning**

| Action | Owner | Notes |
|---|---|---|
| Check Etsy stats: Views, Favorites, Conversions. Log in a simple spreadsheet | User | 5 min |
| Review any new supplier responses — finalize agreements with anyone who hasn't been locked in | User | — |
| Respond to any Etsy messages from Day 1 | User | — |

**Benchmarks for Day 1 performance** (these are realistic for a new listing with no review history):
- Views: 5–25 (extremely variable based on recency boost timing and keyword match)
- Favorites: 0–3 (a favorite on Day 1 is a strong signal)
- Conversions: 0 (do not expect a purchase on Day 1 — this is normal and not a negative signal)

**Do not change anything** based on Day 1 data. The recency boost has not had time to run. Changes on Day 1 can reset the boost window. Observe only.

**Afternoon**

| Action | Owner | Notes |
|---|---|---|
| Check Reddit post performance — any upvotes, comments, or Etsy click-throughs? | User | — |
| Check Instagram post engagement | User | — |
| If TikTok video was posted: note view count | User | — |

---

## T+6 — Day 7: Emerging Signal Review

**Morning**

| Action | Owner | Notes |
|---|---|---|
| Log Day 2 stats: Views, Favorites, Conversions | User | Compare to Day 1 |
| Review Etsy listing in search — search for your primary keyword "cable management clips" and verify your listing appears somewhere on page 1 or 2. If not visible, check tags were saved correctly | User | 10 min |
| Finalize supplier agreements — anyone still in negotiation gets a deadline: "I'll lock this in today or move to backup supplier" | User | — |

**Afternoon**

| Action | Owner | Notes |
|---|---|---|
| Conversion calculation: If 10+ views and 0 conversions, not yet a signal. If 50+ views and 0 conversions, check: (a) Are photos showing the product clearly at scale? (b) Is the price competitive with search results visible on the same search? (c) Is the description answering the buyer's first objection? | Orchestrator | Diagnostic if needed |
| Tag audit: If you registered for eRank, check your listing's "Listing Audit" tab — are all 13 tags scoring as searchable? | Orchestrator | 10 min |

---

## T+7 — Day 8: First Week Retrospective

**Morning**

| Action | Owner | Notes |
|---|---|---|
| Log cumulative 7-day stats: Total views, total favorites, total conversions (sales) | User | — |
| Supplier summary: All 5 categories either locked in or explicitly deferred to Phase 2 | User | — |
| Fulfillment readiness: Sufficient inventory on shelf for 5–10 orders (reprinting if needed) | User | — |

### 7-Day Success Criteria and Go/No-Go Gates

| Metric | Strong | Acceptable | Investigate |
|---|---|---|---|
| Total 7-day views | 100+ | 30–99 | <30 |
| Total favorites | 5+ | 1–4 | 0 |
| Conversions (sales) | 1+ | 0 (normal for new listing) | N/A — too early |
| Listing visible in search for "cable management clips" | Page 1–2 | Page 3–5 | Not found |
| All 13 tags saved and searchable | All 13 | 10–12 | <10 |
| Supplier outreach: at least 3 of 5 confirmed | 5/5 | 3–4/5 | <3/5 |

**If views are below 30 after 7 days:**
1. Check that all 13 tags were actually saved (a common Etsy UI bug drops tags if the save times out).
2. Verify listing is not in "draft" state — confirm listing URL works when not logged in.
3. Check the category — ensure it is Home & Living → Storage & Organization, not a craft/supplies category.
4. Consider relisting (delete + republish) to restart the recency boost — this is a legitimate tactic if the listing has not built any LQS yet.

**If conversion rate is below 1% after 50+ views:**
1. Photo audit: Is the thumbnail showing product in context (lifestyle shot) or just a plain product shot? Lifestyle thumbnails outperform product-only by a documented margin.
2. Price check: Open Etsy in an incognito window and search "cable management clips." What are the prices of listings appearing above you? If you are priced significantly higher with fewer reviews, add a "4-pack starter" at $9.99 to capture price-sensitive buyers.
3. Tag audit: Are any of your tags returning zero results in Etsy search? Replace them with the alternates from the staging guide.

---

## Contingency Paths

### If test print photos are poor quality (T+0)

Trigger: Photos are blurry, lighting is uneven, or the product looks smaller/different than it does in person.

Action: Do not publish listing with poor photos. Delay Etsy launch by 1 day. On T+1 morning, reshoot following the staging guide shot list exactly. If indoor lighting is the problem: shoot near a window between 9 AM and 12 PM when sunlight is angled rather than direct. Do not publish until you have at minimum Shot 1 (lifestyle) and Shot 2 (hero) at acceptable quality.

The listing with good photos that goes live on T+5 will outperform the listing with bad photos that went live on T+4. One day of delay is worth it.

### If supplier lead time is above 2 weeks (T+3–T+5)

Trigger: A supplier confirms pricing but lead time is 15+ days.

Action for filament (eSUN or Anycubic): Do not wait. Place an Amazon Prime order for the immediate production run (10kg case at $12/kg) while the wholesale relationship is established. The $1–2/kg premium on the first order is acceptable. The wholesale lead time matters for Month 2, not Week 1.

Action for packaging (Shop4Mailers): Place the 1,000-unit order immediately regardless of lead time — you need time to receive it before orders start arriving. At 5 orders/week, you have 200 orders of runway from 1,000 mailers. Order on T+0, receive by T+5.

### If Etsy conversion stalls (T+7 and beyond)

Trigger: Listing has 50+ views over 14 days but 0 conversions.

Investigation order (address in sequence, not simultaneously):
1. Photos — lifestyle thumbnail test (swap thumbnail to the closest-up, most in-context shot you have)
2. Price — add a lower-price entry SKU ($9.99 for 4-clip starter pack) to appear in lower price filters
3. Tags — run eRank tag audit; replace any "not found" tags with alternates from staging guide
4. Description — confirm the first 250 characters read as a clear benefit statement, not a product spec list
5. If none of the above resolves after 7 more days: consider a fresh listing (new URL, restart recency boost) with improved photos

### If AMS multi-color test fails (T+0)

Trigger: A second or third color spool produces dimensional inconsistency (AMS diameter variance causing snap arm geometry errors in a different filament lot).

Action: Launch with single-color (Black) listing. Add "White and Grey available soon — message shop for timeline" to description. This is not a launch blocker. Most buyers are indifferent to color at launch; adding variants in Week 2 does not harm LQS if the base listing has already been indexed.

---

## Owner Assignments Summary

| Phase | Primary Owner | Orchestrator Role |
|---|---|---|
| T+0: Tolerance validation, photos, packing | User | Pre-staged materials ready (this document set) |
| T+0: Supplier outreach | User | Templates pre-written; user sends |
| T+1–T+3: Supplier negotiation | User (decisions) | Orchestrator can draft counter-offers if asked |
| T+1–T+3: Social media staging | User (User's voice) | Orchestrator pre-drafts Reddit/Instagram text |
| T+4: Etsy publish + social post | User | Orchestrator monitors search index confirmation |
| T+5–T+7: Daily monitoring | User (5 min/day) | Orchestrator provides analytics interpretation on request |
| T+7+: Tag/pricing/photo optimization | Orchestrator + User | Orchestrator diagnoses; User approves and implements |

**Core principle**: Everything that requires your physical presence, your voice, or your approval is User-owned. Everything that is research, drafting, or monitoring can be delegated to the orchestrator. The staging guides in this document set were pre-built so that your execution time on T+0 is under 3 hours total.
