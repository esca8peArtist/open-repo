---
title: "Seedwarden Contingency Activation Paths — May 23-28 Recovery Playbooks"
date: 2026-05-26
version: 1.0
status: production-ready-fallback-guide
purpose: >
  Five scenarios covering gate delays and blockers (May 23-28). If X slips, here's 
  the specific recovery playbook: immediate actions, timeline impact, decision point, 
  and Phase 3 mitigation. Prevents red panic; enables calm execution.
---

# Seedwarden Contingency Activation Paths — May 23-28 Recovery Playbooks

**Prepared**: May 26, 2026  
**Contingency window**: May 23-28, 2026  
**Decision point**: May 28-29, 2026 (evaluate which contingency is active)  
**May 30 launch status**: Confirmed on chosen date OR escalation call scheduled  

---

## Overview: Five Contingency Scenarios

If any of these conditions occur during May 23-28, activate the corresponding contingency path immediately. Each path includes:
- **Immediate actions** (what to do first)
- **Phase 3 timeline impact** (does launch date slip?)
- **Recovery timeline** (how long to fix?)
- **Decision point** (May 28-29: can this be fixed in time?)
- **Playbook** (step-by-step recovery procedure)

---

## **Scenario A: Gate 1 (Social Accounts) Delays Past May 24**

### Trigger
- [ ] Instagram not created by May 24
- [ ] TikTok not created by May 24  
- [ ] Pinterest not created by May 24
- [ ] Two or more platforms incomplete

### Why This Happens
- TikTok mobile app unavailable (only phone in use elsewhere)
- Confusion about business account setup (takes longer than expected)
- Email verification delays (recovery email not checked)
- Handle already taken (fallback username needs testing)

### Immediate Actions (Within 1 hour of detection)

1. **Identify which platform(s) are stuck**: Instagram? TikTok? Pinterest?
2. **Root cause**: Why delayed?
   - If TikTok: mobile phone needed? Schedule mobile session for May 25
   - If Instagram/Pinterest: business account type issue? Try "Professional" instead of "Business"
   - If email verification: check spam folder; request new verification email
3. **Prioritize**: Which platform is closest to completion?
   - Complete that one first (gives at least one social account live by May 25)
   - Circle back to others May 25-26

### Timeline Impact

**Phase 3 launch date**: ✅ ZERO impact

**Why**: Gate 1 is NOT on critical path. Email automation (Gate 3) is the launch blocker. Social accounts are traffic accelerator, not requirement.

**May 30 launch**: Proceeds on schedule even if Gate 1 is incomplete

### Phase 3 Impact (June 22 launch)

- **All 3 accounts live by May 24**: Full social reach from Day 1 ✅
- **2 accounts live by May 24, 1 delayed to May 26**: 33% reduced reach Week 1; recover on May 27
- **1 account live by May 24, 2 delayed to May 26-27**: 66% reduced reach Week 1; social ramps up May 27-31
- **All 3 accounts delayed past May 27**: Email launch proceeds; social added June 1-2 post-launch (late, but recoverable)

### Recovery Playbook

**If Gate 1 score = 2/3 by May 24**:

1. **May 24 evening**: Complete whichever platform is closest (likely 15-30 min of work)
2. **May 25 morning**: Verify all uploaded accounts are live with profiles correct
3. **May 25 afternoon**: If third platform still pending, add Kit landing page URL to the two live accounts NOW (do not wait for all three)
4. **May 25 end-of-day**: May 25 end-of-day: Add Kit landing page URL to whichever accounts are live:
   - Instagram: Edit profile > Website > paste Kit URL
   - TikTok: Edit profile > Add link > paste Kit URL
   - Pinterest: Settings > Website > paste Kit URL
5. **May 26-27**: Complete remaining platform(s) and add Kit URL

**If Gate 1 score = 1/3 by May 25**:

1. **Escalate immediately**: Flag in May 28 standup
2. **May 26-27 intensive work**: Dedicate 2-3 hours May 26 and May 27 morning to complete all three accounts
3. **May 27 end-of-day**: All accounts must be live with Kit URL in bio
4. **Decision**: If all three live by May 27 PM, Gate 1 = 3/3 (recovery complete). If not, proceed with May 30 launch using whichever accounts are live.

**If Gate 1 score = 0/3 by May 26 evening** (no accounts created):

1. **Immediate escalation** (May 26 evening): Call or email — Gate 1 is stalled
2. **Decision point**: 
   - Option A: Intensive May 27-28 work to complete all three accounts (4-6 hours focused work)
   - Option B: Accept email-only launch; add social May 31-June 2 post-launch
3. **Recommendation**: Unless there's a hard blocker, go with Option A (May 27-28 completion) so social reach is available June 22 Phase 3 launch

### Contingency Go/No-Go

- **Gate 1 score ≥2/3 by May 28**: ✅ **Proceed with launch**
- **Gate 1 score 1/3 by May 28**: ✅ **Proceed; add remaining platforms June 1-2**
- **Gate 1 score 0/3 by May 28**: ✅ **Proceed with email-only; social is nice-to-have, not requirement**

---

## **Scenario B: Gate 2 (Canva Brand Kit) Delays Past May 26**

### Trigger
- [ ] Canva Brand Kit not created by May 26
- [ ] Colors not entered by May 26
- [ ] Fonts not added by May 26
- [ ] Logo not uploaded by May 26
- [ ] **OR** Color palette decision (A/B/C) not made by May 26

### Why This Happens
- Canva account not created (recovery: 5 min to create account)
- Hex code entry errors (color not appearing as expected)
- Confusion about which fonts to add (recovery: use fallback fonts)
- Indecision on color palette (hard choice between A/B/C)
- Logo file corruption or upload failure

### Immediate Actions (Within 1 hour of detection)

1. **Isolate the blocker**:
   - Is Brand Kit created? YES/NO
   - Are colors entered? 0/10? 5/10? 8/10?
   - Are fonts added? 0/3? 1/3? 3/3?
   - Is logo uploaded? YES/NO
   - Is color palette decision pending? YES/NO

2. **Prioritize by severity**:
   - **CRITICAL**: Color palette decision not made (impacts all downstream work) → Decide NOW (pick Option B as default)
   - **HIGH**: Brand Kit not created or incomplete → Create/finish immediately (20-30 min)
   - **MEDIUM**: Logo not uploaded → Re-upload or use temporary placeholder (5 min)

3. **Time estimate for recovery**:
   - Partial Brand Kit (5+ colors done): 15-30 min to finish
   - Brand Kit not started: 30-45 min to complete
   - Color decision pending: 30-60 min to decide (or default to Option B now)

### Timeline Impact

**Phase 3 launch date**: 

- **Brand Kit complete by May 26, 6 PM UTC**: ✅ ZERO impact (zone card production starts May 26 evening, completes May 27-28)
- **Brand Kit complete by May 26, 11 PM UTC**: ✅ MINIMAL (zone cards start May 27 AM, complete May 28)
- **Brand Kit complete by May 27 AM**: 🟡 TIGHT (zone cards must finish by May 28 11 PM for Gate 3 setup May 28 PM)
- **Brand Kit complete by May 27 PM or later**: 🛑 RISK (zone cards may not complete on time; Gate 3 timeline compressed)

### Zone Card Production Ripple Effect

Zone card production CANNOT start until Brand Kit is locked (May 26 latest). If Gate 2 slips:

- May 26 Brand Kit locked: Zone cards May 24-25 ✅ (on schedule)
- May 27 AM Brand Kit locked: Zone cards May 27 (compressed, but OK)
- May 27 PM Brand Kit locked: Zone cards May 28 morning only (very tight)
- May 28 Brand Kit locked: Zone cards May 28, cannot upload to Drive by May 28 11 PM ⚠️

### Recovery Playbook

**If Brand Kit is 50% done by May 26 evening (5 colors, some fonts missing)**:

1. **May 26 evening** (30 min focused work):
   - Finish remaining 5 colors (copy-paste hex codes from runbook, save)
   - Add remaining fonts (search + add, 5 min)
   - Upload logo (5 min)
   - **Total: 15-20 min additional work**

2. **May 26, 11 PM UTC**: Brand Kit locked ✅
3. **May 27**: Start zone card production (compressed but achievable)

**If color palette decision is pending (Brand Kit is structurally complete, but color choice not made)**:

1. **Decision time**: 30-60 min of review OR default to Option B now
   - Option A (Simple): Minimal colors; good for refined aesthetic
   - Option B (Multi-Color): Maximum flexibility; safest choice ← RECOMMENDED
   - Option C (Monochrome): Bold; good for strong brand identity

2. **How to decide**:
   - Review phase-3-gantt-timeline.csv: Will you have time to explore color variations? (If yes, Option B gives flexibility. If no, Option A or C is simpler.)
   - Ask: Do I want design experimentation or fast execution? (Experimentation = B. Speed = A or C.)
   - **Default recommendation**: Pick Option B now if indecisive. It's the most forgiving.

3. **May 26, 6 PM UTC**: Lock color palette
4. **May 26, 7 PM UTC**: Start zone card production using the locked palette

**If Brand Kit is not created at all by May 26, 6 PM**:

1. **Escalation call** (May 26 evening, 15 min):
   - What's blocking Brand Kit creation?
   - Is it time availability? Unknown? Canva account issue?
   - Decision: Intensive May 27 morning work OR defer zone cards to May 28 (and Gate 3 to May 28 PM)

2. **May 27 morning** (45-60 min intensive):
   - Create Canva account
   - Create Brand Kit "Seedwarden"
   - Enter all 10 colors (copy-paste from runbook, 10 min)
   - Add 3 fonts (search + add, 5 min)
   - Upload logo (2 min)
   - **Total: 45-60 min**
   - **By 10 AM May 27**: Brand Kit is locked

3. **May 27, 10 AM - 4 PM**: Zone card production (5-6 hours)
4. **May 27, 4 PM - 11 PM**: Upload zone cards to Google Drive, test links
5. **May 28, 12 AM UTC**: Gate 3 setup begins

### Contingency Go/No-Go

- **Brand Kit locked by May 26, 6 PM + color decision made**: ✅ **Proceed on schedule**
- **Brand Kit locked by May 26, 11 PM + color decision made**: ✅ **Proceed; zone cards May 27**
- **Brand Kit locked by May 27, 12 PM + color decision made**: 🟡 **YELLOW; tight timeline, still recoverable**
- **Brand Kit not locked by May 27, 6 PM**: 🛑 **Escalation required; consider Scenario E (all gates blocked)**

---

## **Scenario C: Gate 3 (Kit Automation) Fails or Stuck in Draft**

### Trigger
- [ ] Kit account not created by May 27
- [ ] Landing page not live by May 27
- [ ] Email automation not built by May 27
- [ ] Automation stuck in Draft (not Published) by May 28, 6 PM UTC

### Why This Happens
- Kit signup process slow (account verification delayed)
- Landing page setup confusion (zone dropdown not working)
- Email copy not finalized or missing
- DNS propagation issues (automation published, but SPF/DKIM not propagated)
- 3-test protocol failed (Email 1 not arriving; PDF links broken)

### Immediate Actions (Within 1 hour of detection)

1. **Identify the blocker**:
   - Kit account: Created? YES/NO. Verified? YES/NO.
   - Landing page: Created? Drafted? Published?
   - Email automation: Created? How many of 5 emails built? Status: Draft/Published?
   - 3-test protocol: Passed? Passed with issues? Not yet run?

2. **Prioritize by severity**:
   - **CRITICAL**: Automation not published by May 28, 6 PM (blocks DNS propagation window)
   - **HIGH**: 3-test protocol failed (email not arriving or PDF links broken)
   - **MEDIUM**: Only 2-3 of 5 emails built (missing Email 4 or 5)

3. **Time estimate to fix**:
   - Kit account not verified: 5-10 min (check spam folder, resend verification)
   - Landing page not working: 15-30 min (test form, fix zone dropdown)
   - 1 email missing from sequence: 10-15 min (copy email from marketing/email-and-launch-plan.md, add to Kit)
   - 3-test failed: 30-60 min (troubleshoot email delivery, fix PDF links, re-test)

### Timeline Impact

**Phase 3 launch date**: ✅ ZERO impact (Kit is not the launch blocker; email capture is the launch enhancement)

**May 30 launch**:
- If Kit automation publishes by May 28, 6 PM: ✅ Full functionality on Day 1
- If Kit automation publishes May 28 evening: ✅ Minimal impact (28 hours DNS propagation instead of 48, but still works)
- If Kit automation cannot be published until May 29: 🟡 YELLOW (only 24 hours propagation; may have DNS delays on May 30 afternoon)
- If Kit automation cannot be published until May 30 morning: 🛑 RED (zero propagation; email may be marked as spam on Day 1)

### Recovery Playbook

**If Kit account not verified by May 27, 6 PM**:

1. **May 27, 6 PM**: Check wanka95@gmail.com inbox (including spam folder) for Kit verification email
2. **If not received**: 
   - Log into Kit > Resend verification email
   - Check inbox again (check spam again)
   - Verification takes 5-10 min once link is clicked
3. **May 27, 7 PM**: Kit account verified and ready for setup ✅
4. **May 27, 7-9 PM**: Create tags + landing page + automation (3 hours)
5. **May 28, 12 PM UTC**: Publish automation

**If landing page not working (form not submitting) by May 27, 6 PM**:

1. **May 27, 6 PM**: Test landing page in incognito browser
2. **If form doesn't submit**: 
   - Check Kit > Landing Pages > Form settings
   - Verify zone dropdown has all 8 zones listed
   - Verify "Subscribe and apply tags" action is selected
   - Test form submission
3. **If still not working**: 
   - Try simplifying form (remove optional fields, keep only Email + Zone)
   - Re-save and republish landing page
4. **May 27, 7 PM**: Landing page working ✅
5. **May 27, 7-9 PM**: Build email automation (2-3 hours)
6. **May 28, 12 PM UTC**: Publish automation

**If 3-test protocol fails (Email 1 not arriving or PDF download broken)**:

1. **May 28, 12 PM**: Run 3-test protocol
   - Test 1: Sign up with Zone 5 → check email arrives within 60 sec
   - **If Email 1 doesn't arrive**: Check Kit > Automations > automation is set to "Active" (not Draft). If Draft, publish now.
   - **If Email 1 arrives but PDF link is broken**: Check Google Drive link is in "export=download" format (not standard share link). Fix link, re-test.

2. **If Email 1 arrives with working PDF**: Tests 2-3 pass ✅

3. **If Email 1 is not arriving**:
   - Check Kit > Automations > status is "Active" or "Published"
   - If still Draft: Publish immediately (5-10 min)
   - If already published: Check email filtering (is Email 1 going to spam?)
   - If email is in spam: May indicate DNS/SPF issue (see next recovery step)

4. **If automation status is Published but Email 1 still not arriving**: DNS/SPF issue
   - This is a Kit platform issue; escalate to Kit support
   - **Contingency fallback** (May 28 evening): Set up Gmail SMTP relay to send Email 1 manually instead of Kit (advanced; requires workaround)
   - **Decision point** (May 28 evening): Proceed with May 30 launch using Kit if fixed; or activate manual email fallback

**If automation is created but stuck in Draft by May 28, 6 PM**:

1. **May 28, 6 PM**: Publish automation immediately (1-2 min button click)
   - Kit > Automations > "Seedwarden Welcome Sequence" > Click "Publish" or toggle from "Draft" to "Active"
   - **Confirm status now shows "Published" or "Active" (not "Draft")**

2. **May 28, 6:05 PM**: Automation is live ✅
   - DNS propagation window: May 28 6:05 PM to May 30 2:05 PM (48 hours) ✅ Sufficient

3. **May 28, 6:30 PM**: Run 3-test protocol again
   - Confirm Email 1 arrives and PDF downloads
   - If passes: Gate 3 = 3/3 ✅

### Contingency Fallback (If Kit Cannot Be Fixed by May 28)

**Fallback option: Manual email sending**

If Kit automation cannot be published or is having technical issues beyond May 28, 6 PM:

1. **Landing page option 1** (recommended): Keep Kit landing page for zone signup collection
   - Zone selector works: users sign up, data collected in Kit subscriber list
   - But emails don't auto-send

2. **Landing page option 2** (if Kit is completely down): Switch to Google Form
   - Create Google Form with zone selector (8 options)
   - Copy responses to spreadsheet manually
   - Send Email 1 manually to each signup via Gmail BCC list

3. **Email 1 manual sending**:
   - Export Kit subscriber list (or Google Form responses) as CSV
   - Create email in Gmail with personalized zone PDF link
   - Send Email 1 via BCC (all addresses in one email to you, BCC to subscribers)
   - **Timing**: Send May 30, 12:00 PM UTC (same as automated version would send)
   - **Limitation**: Email 2-5 sequence will not auto-send (Kit automation down). Send manually on Days 3, 7, 10, 14.

4. **Recovery plan post-launch**:
   - May 31 or June 1: Troubleshoot Kit issue + restore automation
   - Deploy Email 2-5 sequence on June 3-4 (2 days late, but functional)
   - Document delay in WORKLOG.md

### Contingency Go/No-Go

- **Automation published by May 28, 6 PM + 3-test passes**: ✅ **Proceed on schedule**
- **Automation published by May 28, 11 PM + 3-test passes**: ✅ **Proceed; 28-hour DNS window acceptable**
- **Automation published May 29 morning before 8 AM**: 🟡 **YELLOW; 24-hour DNS window tight, but likely OK**
- **Automation cannot be published by May 29, 6 PM**: 🛑 **Activate manual fallback (Email 1 via Gmail, Email 2-5 deferred)**

---

## **Scenario D: Supplier Confirmations Not Received (May 25-28)**

### Trigger
- [ ] Top 3 suppliers (Prairie Moon, Strictly Medicinal, Mountain Rose) have not responded by May 25
- [ ] Goldenseal or Black Cohosh availability cannot be confirmed by May 25
- [ ] Critical lead-time species (Elderberry, Echinacea) appear to be out of stock
- [ ] Fewer than 3 of 5 suppliers confirmed by May 28

### Why This Happens
- Supplier outreach emails sent May 20-23 but responses slow (May business)
- Automated "out of office" replies; actual response delayed to May 26+
- Supplier inventory depleted by late May (seasonal sourcing window closed)
- Supplier contact info outdated (phone disconnected, email not monitored)
- Wikimedia Commons / CC-licensed backup images not identified yet

### Immediate Actions (Within 1 hour of detection)

1. **Assess supplier status** (May 25 morning):
   - Prairie Moon Nursery: Responded? Available? Lead time?
   - Strictly Medicinal Seeds: Responded? Available? Lead time?
   - Mountain Rose Herbs: Responded? Available? Lead time?
   - Southern Exposure / Fedco: Responded? (secondary; guide citations only)

2. **Escalate unresponsive suppliers**:
   - If no response by May 25: Phone call (if number available) OR second email with 24-hour deadline
   - Goldenseal decision tree (phase-3-supplier-confirmation-tracker.md, Section 7): If no supplier confirms by May 25, activate Wikimedia CC path May 25-June 7

3. **Time estimate for recovery**:
   - 24-hour supplier deadline: May 25 morning to May 26 morning (catch replies by May 26 PM)
   - Wikimedia CC path activation: 30-60 min (search for images, log URLs, verify license)
   - Backup supplier substitution: 15-30 min per species (update supplier tracker)

### Timeline Impact

**Phase 3 launch date**: 
- **Goldenseal/Black Cohosh decision by June 8**: ✅ ZERO impact (orders placed by deadline)
- **Goldenseal/Black Cohosh decision by June 10**: 🟡 MINIMAL (Wikimedia CC path confirmed, no supplier order needed)
- **Goldenseal decision delayed past June 8 without CC path activated**: 🛑 HIGH (photography sourcing uncertain)

**Phase 3 timeline (June 22-July 13)**:
- All suppliers confirmed, orders placed June 8-15: ✅ Full timeline intact; live plants available June 21 photography
- 4 of 5 suppliers confirmed, 1 using CC images: ✅ MINIMAL (1 species uses CC image instead of live plant)
- 3 of 5 suppliers confirmed, 2 using CC images: 🟡 ACCEPTABLE (2 species use CC images; photography still high quality)
- Fewer than 3 confirmed + no CC backup: 🛑 CRITICAL (all 14 species rely on Wikimedia, loses quality differentiation)

### Recovery Playbook

**If all 3 primary suppliers confirm by May 25 AM**:

1. **May 25 AM - PM**: Place Tier 1 orders (Goldenseal + Black Cohosh) with confirmed supplier
2. **May 26 PM**: Place Tier 2 orders (Elderberry + Mountain Rose dried herbs)
3. **June 8**: Hard deadline — Goldenseal order must be confirmed or Wikimedia CC path activated
4. **June 22 Phase 3**: All live plants available for photography June 17-21 ✅

**If suppliers respond slowly (May 26-27 responses) but confirm availability**:

1. **May 25-26**: Call suppliers directly (phone number from website) for same-day response
   - "Hi, I'm looking to place an order for X species. Can you confirm current availability and lead time?"
   - Script should take 5 min per supplier × 3 = 15 min

2. **May 27**: If phone calls confirm all 3 suppliers available, place orders immediately
   - Tier 1 (Goldenseal + Black Cohosh): Order by May 27 PM
   - Tier 2 (Elderberry + Mountain Rose): Order by May 28 PM
   - Tight timeline, but lead times allow June 21 delivery

3. **June 21 photography**: All live plants available ✅

**If Goldenseal/Black Cohosh suppliers are out of stock**:

1. **May 25-26**: Activate Wikimedia CC path immediately
   - Search Wikimedia Commons for Hydrastis canadensis (Goldenseal) and Actaea racemosa (Black Cohosh)
   - Requirements: CC-BY, CC-BY-SA, or CC0 license; clear habit photos (full plant, not just flower)
   - Find 3-5 images per species (backup for image if one doesn't work)
   - Log URLs and license details in WORKLOG.md per project protocol

2. **May 28**: Email NC Botanical Garden + Missouri Botanical Garden (if not already done)
   - Request: "Can we use your Goldenseal/Black Cohosh photo for educational guide?"
   - Attribution requirements from each institution
   - This is optional but adds institutional credibility if approved

3. **June 1**: Log final decision in WORKLOG.md
   - "Goldenseal sourcing: Wikimedia CC path (decision May 26, confirmed May 28)"
   - No live specimen ordered; phase 3 timeline unaffected

4. **June 17-21 photography**: Skip live plant photos for out-of-stock species; use CC images only ✅

**If Mountain Rose Herbs (dried herbs) is out of stock or slow to respond**:

1. **May 26**: Immediately contact backup (Frontier Co-op)
   - "Do you have 1 oz each of [12 species] available for June 13 delivery?"
   - Frontier lead time: 3-5 business days (order June 13, arrive June 18-20, still in time for June 17-21 studio shoot)

2. **May 27**: If Mountain Rose confirms by May 27 PM, order from them
   - If not confirmed, place backup order with Frontier by May 28 PM

3. **June 21 photography**: Dried herb props available (either supplier) ✅

### Contingency Go/No-Go

- **All 5 suppliers confirmed by May 25**: ✅ **Proceed on schedule; orders placed June 8-15**
- **3-4 of 5 confirmed by May 27; remainder using Wikimedia CC path**: ✅ **Proceed; Phase 3 photography quality slightly reduced but acceptable**
- **Fewer than 3 confirmed by May 28 + no CC backup images identified**: 🛑 **Escalation required; Phase 3 photography may need to defer to June 29 after CC images finalized**

---

## **Scenario E: Phase 3 Timeline Unrealistic (Gantt Review Shows Overcommitment)**

### Trigger
- [ ] Gantt review (May 28) shows 160+ hours required for June 22-July 13 sprint
- [ ] Available hours <12/week (cannot fit 120 hours into 22-day window)
- [ ] Multiple projects active in parallel (stockbot, resistance-research, cybersecurity) with overlapping deadlines
- [ ] Supplier delays push photography to June 24-25 (compresses Phase 3 sprint timeline)

### Why This Happens
- Underestimate of writing hours (8,000 words takes 40-50 hours, not 30)
- Social graphics production underestimated (20 pieces × 20 min = 6.5 hours, plus feedback loops)
- Multiple projects during Phase 3 window (resistance-research Phase 2, stockbot monitoring)
- Etsy listing setup takes longer than expected (SEO research, A/B testing variants)
- Supplier delays push photography window (June 24-25 instead of June 17-21)

### Immediate Actions (Within 1 hour of detection)

1. **Reassess Gantt timeline** (May 28):
   - Break down each Phase 3 activity: hours needed?
   - Guide writing: 8,000 words ÷ 200 words/hour = 40 hours (not 30)
   - Social graphics: 20 pieces × 30 min = 10 hours (plus feedback)
   - Etsy listings: 5 listings × 2 hours = 10 hours
   - Photography: 16 hours (including shoot + editing)
   - **Revised total**: 100-120 hours (more realistic)

2. **Calculate available hours** (May 28):
   - You available: _______ hours/week
   - June 22-July 13: 3 weeks = _______ hours/week × 3 = _______ total hours
   - **Do total hours fit timeline?** YES / NO

3. **Identify time conflicts**:
   - Resistance-research Phase 2: Requires _____ hours during June 22-July 13? (check ORCHESTRATOR_STATE.md)
   - Stockbot: Requires _____ hours during June 22-July 13?
   - Cybersecurity-hardening: Requires _____ hours during June 22-July 13?
   - Other: _____ hours/week?
   - **Total non-Seedwarden time**: _____ hours/week
   - **Available for Seedwarden**: Your total hours - non-Seedwarden = _____ hours/week

### Timeline Impact

- **Available hours = 18-20/week**: ✅ June 22 launch, full quality, timeline TIGHT but achievable
- **Available hours = 15-18/week**: ✅ June 22 launch, quality OK, some items may slip internal deadlines (but not external)
- **Available hours = 12-15/week**: 🟡 YELLOW — June 22 timeline marginal; **recommend June 24 or July 1**
- **Available hours = <12/week**: 🛑 RED — June 22 is NOT realistic; **recommend July 1 with extended timeline**

### Recovery Playbook

**If timeline is marginal (12-15 hrs/week available, Gantt shows 100-120 hours needed)**:

**Option 1: Compress to June 24 (2-day slip)**
- Start sprint June 24 instead of June 22
- Extends timeline to June 24-July 15 (22 days, still fits)
- Gives 2 extra days for final supplier confirmation + Gate 3 cleanup
- Recommendation: Preferred option if available hours are 12-15/week

**Decision steps**:
1. Confirm supplier status by June 13
2. Photography by June 21
3. Phase 3 sprint June 24-July 15
4. Quality maintained, timeline achievable with 15 hrs/week commitment

**Option 2: Reduce Phase 3 scope for June 22**
- Launch only 2 of 5 guides on June 22 (Women's Health + Respiratory)
- Remaining 3 guides launch in Phase 4 (July 15-31)
- Phase 3 sprint June 22-July 13 focuses on 2 guides only (50 hours, easier to fit)
- Recommendation: Only if you want June 22 launch AND <15 hrs/week available

**Decision steps**:
1. Defer Digestion, Sleep, Immune guides to Phase 4
2. June 22 launch with 2 guides (Women's Health + Respiratory)
3. Higher quality for core guides, lower stress
4. Phase 4 (July 15-31) completes remaining 3

**Option 3: Defer to July 1 with extended timeline**
- Phase 3 sprint July 1-31 (31 days, not 22)
- Allows 100-120 hours spread over 4+ weeks = 25-30 hrs/week is NOT required
- Achievable with 12-15 hrs/week commitment
- Recommendation: Preferred if <12 hrs/week available or multiple projects overlap June 22-July 13

**Decision steps**:
1. May 30: Choose July 1 launch
2. June 1-30: Phase 2 optimization + prep Phase 3 assets
3. July 1-31: Phase 3 sprint at relaxed pace
4. All 5 guides complete by July 31; higher quality, less stress

### Contingency Go/No-Go

- **18+ hours/week available + realistic Gantt**: ✅ **Proceed June 22 launch**
- **15-18 hours/week available + realistic Gantt**: ✅ **Proceed June 22 (tight) OR choose June 24**
- **12-15 hours/week available**: 🟡 **Recommend June 24 OR July 1**
- **<12 hours/week available**: 🛑 **Strongly recommend July 1 with 31-day timeline**

---

## Escalation Decision Tree (May 28-29)

**Use this tree if multiple contingencies are active**:

```
Are any gates in RED status (score 0/3)?
├─ YES → Escalation call required
│   ├─ Which gate? _______
│   ├─ Can be fixed by May 29 AM? YES/NO
│   └─ If NO → Activate corresponding contingency fallback
│
└─ NO → All gates are GREEN/YELLOW (3/3 or 2/3)
    ├─ Are zone cards complete and on Google Drive?
    │  ├─ YES → Proceed with Gate 3 May 28
    │  └─ NO → Activate Contingency B recovery
    │
    └─ Is Phase 3 timeline realistic given available hours?
       ├─ YES (15+ hrs/week) → Choose Path A (June 22) or Path B (June 24)
       └─ NO (<15 hrs/week) → Choose Path C (July 1)
```

---

## Quick Reference: Contingency Status Checks

**Use this checklist May 28-29 to assess which contingencies are active**:

| Contingency | Check | Status | Action |
|---|---|---|---|
| **A: Gate 1 delays** | Instagram + TikTok + Pinterest all live? | ☐ YES (0/3 active) | Proceed |
| | At least 2 platforms live? | ☐ YES (1/3 active) | Add missing by June 1 |
| | Fewer than 2 platforms? | ☐ YES (2/3 active) | 🔴 Escalation |
| **B: Gate 2 delays** | Canva Brand Kit + colors + fonts + logo complete? | ☐ YES (0/3 active) | Proceed |
| | Color palette decision locked (A/B/C)? | ☐ YES (0/3 active) | Proceed |
| | Brand Kit not finished OR color not decided? | ☐ YES (1/3 active) | May 27 intensive |
| | Brand Kit not created at all? | ☐ YES (2/3 active) | 🔴 Escalation |
| **Zone Cards** | All 8 PDFs on Google Drive? | ☐ YES (0/3 active) | Proceed |
| | 6-7 PDFs on Drive? | ☐ YES (1/3 active) | Complete missing May 28 |
| | Fewer than 6 PDFs? | ☐ YES (2/3 active) | 🔴 Escalation |
| **C: Gate 3 delays** | Kit automation published (not Draft)? | ☐ YES (0/3 active) | Proceed |
| | Automation in Draft but can publish by May 28? | ☐ YES (1/3 active) | Publish May 28 AM |
| | 3-test protocol passed? | ☐ YES (0/3 active) | Proceed |
| | 3-test failed; Kit support needed? | ☐ YES (2/3 active) | Activate fallback |
| **D: Supplier delays** | Top 3 suppliers confirmed by May 25? | ☐ YES (0/3 active) | Orders June 8-15 |
| | 2-3 suppliers confirmed; 1 using CC? | ☐ YES (1/3 active) | Proceed, quality -10% |
| | Fewer than 2 suppliers confirmed? | ☐ YES (2/3 active) | 🔴 Escalation |
| **E: Timeline unrealistic** | Available hours = 15+ per week? | ☐ YES (0/3 active) | June 22 launch OK |
| | Available hours = 12-15 per week? | ☐ YES (1/3 active) | Choose June 24 or July 1 |
| | Available hours = <12 per week? | ☐ YES (2/3 active) | Recommend July 1 |

---

## Final Summary

By May 28 evening, you will know which (if any) contingencies are active. Use the status checks above to assess:

1. **All contingencies GREEN**: Gates 1-3 all ≥2/3 score, zone cards done, suppliers confirmed, timeline realistic
   - ✅ **May 30: Choose Path A (June 22) or Path B (June 24)**

2. **One or two contingencies YELLOW**: One gate partially delayed or one supplier pending, but all recoverable
   - 🟡 **May 30: Choose Path B (June 24) for buffer, or Path A if high confidence**

3. **Three or more contingencies RED or multiple gates = 0/3**: Multiple blockers
   - 🛑 **May 28-29: Escalation call required. Recommend Path C (July 1) for recovery.**

---

**Document version**: 1.0 (May 26, 2026)  
**Maintained by**: You (user)  
**Status check deadline**: May 28, 6 PM UTC  
**Escalation decision point**: May 28-29, 2 PM UTC  
**Launch decision**: May 30, 2 PM UTC
