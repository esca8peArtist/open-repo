---
title: "Track B Launch Day Checklist — 2-Minute Pre-Launch Verification"
date: 2026-05-30
version: 1.0
status: production-ready
purpose: "Final 2-minute verification at 07:55 UTC before launch window begins. Confirms all systems are ready to go."
---

# Track B Launch Day Checklist
## 2-Minute Pre-Launch Verification (07:55–08:00 UTC)

**Timing**: Run this checklist at exactly 07:55 UTC on May 30 (5 minutes before launch).

**Time budget**: 2 minutes maximum. This is a final gate, not a deep review. If any item is UNCHECKED at 07:59 UTC, STOP and resolve it before proceeding.

**Pass criteria**: All items checked ✓. If any item is ✗, do not launch. Resolve, then restart the checklist.

---

## CHECKLIST

### Step 1: Email System Ready (30 seconds)

- [ ] **Kit account login works**: Open kit.co, log in, confirm dashboard loads
  - **If fails**: Stop. Contact Kit support immediately. Cannot proceed.
- [ ] **Launch broadcast visible**: Kit > Broadcasts > find "Seedwarden is live" broadcast
  - **If missing**: Stop. Create broadcast now (takes 5 min). Use copy from `marketing/email-and-launch-plan.md`.
- [ ] **Broadcast status shows "Scheduled"**: Confirm status is NOT "Draft"
  - **If Draft**: Click Schedule, set time to 12:00 UTC today, confirm status changes to "Scheduled"

**30-second result**: ✓ Kit ready to send at 12:00 UTC OR ✗ STOP and resolve

---

### Step 2: Etsy Store Ready (30 seconds)

- [ ] **Etsy Shop Manager loads**: Open Etsy Shop Manager, confirm you see "Listings" tab
  - **If fails**: Stop. Clear browser cache / try incognito / restart browser. Etsy must be accessible.
- [ ] **All 21 Phase 2 listings exist**: Etsy Shop Manager > Listings, filter "Draft", confirm count shows 21
  - **If <21**: Stop. Missing listings must be created before launch.
- [ ] **SEEDWARDEN15 coupon active**: Etsy > Marketing > Sales and Coupons, confirm "SEEDWARDEN15" shows "Active"
  - **If "Expired" or missing**: Create it now (5 sec: copy SEEDWARDEN15 existing coupon OR create 15% off, no min, no expiry)

**30-second result**: ✓ Etsy ready to publish at 10:00 UTC OR ✗ STOP and resolve

---

### Step 3: Social Media Scheduled (30 seconds)

- [ ] **Buffer/Later opens**: Go to buffer.com or later.com, log in, confirm queue page loads
  - **If fails**: Stop. Social posting cannot proceed. Fix login.
- [ ] **May 30 posts visible**: In queue, find posts scheduled for May 30. Confirm you see:
  - Instagram post (scheduled 08:30 UTC)
  - TikTok post (scheduled 08:45 UTC)
  - Pinterest pins (3+, scheduled 09:00 UTC)
  - **If any missing**: Stop. Schedule it now (takes 2 min per missing post).
- [ ] **All platform connections green**: Buffer Settings > Connected Accounts, confirm Instagram, TikTok, Pinterest all show green/active status
  - **If any red/error**: Click "Reconnect" and re-authorize (takes 2 min). Then return to this checklist.

**30-second result**: ✓ Social media ready to post automatically OR ✗ STOP and resolve

---

### Step 4: Landing Page Live (20 seconds)

- [ ] **Gist URL accessible**: Open [GIST_URL] in a new incognito browser tab. Confirm page loads without error.
  - **If 404 or access denied**: Stop. Check if Gist is public sharing is enabled (GitHub > Gist > Share > Anyone with link).
- [ ] **All 8 zone PDFs listed**: On the Gist page, count the PDFs. Should see Zone 3, 4, 5, 6, 7, 8, 9, 10.
  - **If fewer than 8**: Stop. Check which zones are missing. Re-upload missing PDFs to Gist.

**20-second result**: ✓ Gist ready OR ✗ STOP and resolve with backup URL

---

## FINAL GATE (10 seconds)

All 4 steps checked and ready?

- [ ] **YES — All systems GREEN**: Proceed to launch. Open the Hour-by-Hour Runbook. Begin at 08:00 UTC.
- [ ] **NO — Any item UNCHECKED or RED**: STOP. Resolve the item. Return to that step of this checklist. When resolved, verify again, then proceed.

---

## IF YOU MUST STOP

If any item is ✗ at 07:55 UTC:

1. **Identify the blocker**: Which step failed? (Email / Etsy / Social / Landing page)
2. **Resolve using these quick fixes**:
   | Blocker | Quick Fix | Time |
   |---------|-----------|------|
   | Kit won't load | Restart browser, clear cache, try incognito | 2 min |
   | Broadcast missing | Create new broadcast in Kit, paste copy | 5 min |
   | Etsy listings <21 | Check if in Draft view. If missing, create draft listings | 5–10 min |
   | Coupon missing | Create "SEEDWARDEN15" coupon (15% off) | 2 min |
   | Social post missing | Open Buffer, create post, schedule for May 30 time | 5 min |
   | Gist 404 | Check GitHub Gist sharing (public?). If broken, use backup Google Drive URL | 3 min |
   | Platform connection red | Click Reconnect, re-authorize on that platform | 2 min |

3. **Re-check the item**: Once fixed, return to the matching step and re-verify.
4. **Proceed only when all 4 steps show ✓**.

---

## WHAT HAPPENS AT 08:00 UTC

Once this checklist is complete and all items ✓:

1. **Close this checklist**
2. **Open TRACK_B_LAUNCH_DAY_HOUR_BY_HOUR_RUNBOOK.md**
3. **Begin Hour 0 (08:00–09:00 UTC)**: Pre-launch verification section
4. **Follow the runbook sequentially through Hour 6**

---

## Emergency Contacts

**If you cannot resolve a blocker**:

| System | Support | Time to help |
|--------|---------|-------------|
| Kit (email) | support@kit.com or chat.kit.com | 30 min – 2 hours |
| Etsy (store) | help.etsy.com > Contact Support | 2–8 hours (delays during peak) |
| Buffer/Later (social) | buffer.com/support or later.com/help | 30 min – 2 hours |
| GitHub (Gist) | github.com/support | 1–24 hours |

**If you cannot reach support within 15 minutes**: Activate **backup URL** (Google Drive folder) for Gist or **manual posting** for social media. Launch proceeds even if one system has issues.

---

## Print This (Paste to phone for launch day reference)

```
TRACK B LAUNCH DAY — FINAL 2-MIN CHECK (07:55 UTC)

[ ] Kit dashboard login + broadcast "Scheduled"
[ ] Etsy 21 listings + SEEDWARDEN15 coupon
[ ] Buffer/Later: IG/TT/Pinterest posts queued + connections green
[ ] Gist URL loads + all 8 zones visible

ALL ✓? → Open Hour-by-Hour Runbook. Begin 08:00 UTC.
ANY ✗? → Resolve blocker. Re-check. Then proceed.

Kit down? Manually BCC email. TT won't post? Manual upload. Gist 404? Use backup URL.
Launch continues.
```

---

*Document status: Production-ready. May 30, 2026.*
*This is your final gate before launch. Complete at 07:55 UTC. All items must be ✓ to proceed.*
*If any item fails after you begin the Hour-by-Hour Runbook, use the Common Issues Decision Trees.*
