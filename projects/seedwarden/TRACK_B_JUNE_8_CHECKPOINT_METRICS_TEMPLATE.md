---
title: "Track B Day 3 Checkpoint Metrics Template — June 8, 2026"
created: 2026-06-06
status: pre-staged
execution-date: 2026-06-08
tracking-window: "2026-06-04 to 2026-06-07 (72 hours post-launch)"
purpose: >
  Pre-populated metrics collection template for June 8 Day 3 checkpoint.
  Fill in actual values from systems below. All thresholds pre-calculated.
  Execution time: 5–10 minutes to fill. Compare results to thresholds.
  Decision routing handled by TRACK_B_JUNE_8_DECISION_LOGIC_FLOWCHART.md
---

# Track B Day 3 Checkpoint — Metrics Template
**Checkpoint date**: June 8, 2026 at 08:00 UTC  
**Tracking window**: June 4, 13:00 UTC → June 7, 23:59 UTC (72 hours)  
**Decision**: Record metrics below. Route to decision flowchart. Execute escalation if CAUTION/NO-GO triggered.

---

## Metric 1: Email Open Rate (Campaign Monitor)

**Data source**: Campaign Monitor > Campaigns > [Launch broadcast name] > View Report

| Metric | Value | Threshold (GO/CAUTION/NO-GO) |
|--------|-------|------------------------------|
| Total sent | ___ | — |
| Unique opens | ___ | — |
| **Open rate %** | **___ %** | **GO: ≥20% / CAUTION: 10–19% / NO-GO: <10%** |
| Click rate % | ___ % | — |
| Unsubscribes | ___ | CAUTION: 2–5% / NO-GO: >5% |
| Bounce rate % | ___ % | — (diagnostic only) |

**How to collect**: Log in to Campaign Monitor > Campaigns. Find the June 4 launch broadcast. Click "View Report". Record the numbers above.

**Status**: ☐ GO ☐ CAUTION ☐ NO-GO | **Confidence**: ___/10

**Notes**: 
- If broadcast status shows "Draft" or "Scheduled": it was not sent. Send immediately.
- If bounce rate > 5%, investigate list quality (Scenario 4 in CONTINGENCY_TRIGGER_DECISION_TREE.md).

---

## Metric 2: Gist View Count (GitHub)

**Data source**: The Gist URL from outreach (check directly — GitHub API does not expose view counts)

| Metric | Value | Threshold (GO/CAUTION/NO-GO) |
|--------|-------|------------------------------|
| **Gist view count (cumulative)** | **___ views** | **GO: >70 / CAUTION: 30–70 / NO-GO: <30** |
| Gist comments | ___ | — |
| Gist forks | ___ | — |

**How to collect**: 
1. Open the Gist URL in browser
2. View count is displayed at the top right (next to star count)
3. Record the cumulative number

**Status**: ☐ GO ☐ CAUTION ☐ NO-GO | **Confidence**: ___/10

**Notes**:
- If Gist URL returns 404: the Gist was deleted. Recreate immediately.
- Check URL placement: Instagram bio, Reddit posts, Kit CTA, launch email. Missing placements = reduced views.

---

## Metric 3: Influencer Activity (Twitter/Instagram/Email)

**Data source**: Twitter search, Instagram mentions, email inbox

| Influencer contact response | Count | Notes |
|------------------------------|-------|-------|
| Total outreach sent (of 15) | ___ | — |
| Responses received (any email/DM) | ___ | — |
| **Public shares confirmed** | **___ shares** | **GO: ≥1 / CAUTION: 0 shares, responses rcvd / NO-GO: 0 responses from all 15** |
| Organic third-party mentions | ___ | (bonus, not threshold) |

**How to collect**:
1. Twitter: search "seedwarden", "zone quick-start" OR "zone card", "wild edibles" + zone
2. Instagram: check Profile > Tags, search #seedwarden / #zonecard / #wildedibles
3. Email inbox: check for replies to outreach messages
4. Record any shares or responses from the 15 influencer contacts

**Status**: ☐ GO ☐ CAUTION ☐ NO-GO | **Confidence**: ___/10

**Notes**:
- "Public share" = Instagram post, Twitter post, or story mentioning the Gist or Zone cards
- Response but no public share yet = CAUTION range, expected at 72h
- 0 responses after 72h + correct email sent = likely list issue or messaging problem

---

## Metric 4: Sales & Kit Funnel (Etsy + Kit)

**Data source**: Etsy Shop Manager, Kit account, PayPal activity

| Channel | Metric | Value | Threshold (GO/CAUTION/NO-GO) |
|---------|--------|-------|------------------------------|
| **Etsy** | Listing status | [Draft/Active/Deactivated] | **Active required for sales** |
| | Listing views | ___ | — |
| | Orders | ___ | **GO: ≥1 / CAUTION: views but 0 / NO-GO: 0** |
| | Revenue | $___  | — |
| **Kit** | New subscribers | ___ | **GO: ≥5 / CAUTION: 1–4 / NO-GO: 0** |
| | PDF downloads (from Kit) | ___ | — |
| | Email clicks (from Kit funnel) | ___ | — |
| **PayPal** | Transactions (seedwarden-related) | ___ | — |

**How to collect**:
1. Etsy: Log in > Shop Manager > Stats. Select date range June 4 → today.
2. Kit: Log in > Dashboard. Check subscriber count and funnel conversion.
3. PayPal: Log in > Activity. Filter by date June 4 onwards. Search for seedwarden transactions.

**Status**: ☐ GO ☐ CAUTION ☐ NO-GO | **Confidence**: ___/10

**Notes**:
- Etsy listing must be Active to generate sales (not Draft)
- Kit funnel: Subscribers → PDF access → Email follow-up. Track each stage.
- No sales by Day 3 is normal if Etsy listing is Draft. Expected at Day 7.

---

## Summary Decision Matrix

| Metric | Status | Decision |
|--------|--------|----------|
| Email open rate | ☐ GO ☐ CAUTION ☐ NO-GO | — |
| Gist views | ☐ GO ☐ CAUTION ☐ NO-GO | — |
| Influencer activity | ☐ GO ☐ CAUTION ☐ NO-GO | — |
| Sales/Kit | ☐ GO ☐ CAUTION ☐ NO-GO | — |
| **OVERALL** | **☐ GO ☐ CAUTION ☐ NO-GO** | **→ See TRACK_B_JUNE_8_DECISION_LOGIC_FLOWCHART.md** |

---

## Next Steps

1. **Fill in all metrics above** (5–10 minutes)
2. **Compare each to threshold** and mark GO/CAUTION/NO-GO
3. **If any metric is CAUTION or NO-GO**: Open TRACK_B_JUNE_8_CONTINGENCY_ESCALATION_PROTOCOL.md
4. **If all metrics are GO**: Log in CHECKIN.md "Track B on track for Day 7 checkpoint" + continue normal social calendar

---

## Troubleshooting

**"I can't find the metric"**
- Metric 1 (email): If Campaign Monitor broadcast is in Draft, send it first
- Metric 2 (Gist): If 404, recreate immediately. Check URL in all outreach materials.
- Metric 3 (influencers): Check email Sent folder, not just Inbox. DMs may be in Instagram/Twitter DMs.
- Metric 4 (sales): Ensure Etsy listing is published (not Draft) before checking stats

**"Multiple metrics triggered CAUTION"**
- See CONTINGENCY_TRIGGER_DECISION_TREE.md Scenario 8 (Multi-Failure Escalation)
- Do not execute individual scenario responses in parallel. Escalate to user first.

---

**Completed by**: ___________ | **Date/Time**: ___________ | **Overall Status**: ☐ GO ☐ CAUTION ☐ NO-GO
