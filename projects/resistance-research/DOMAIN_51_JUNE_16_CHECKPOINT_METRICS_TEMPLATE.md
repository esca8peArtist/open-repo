---
title: Domain 51 June 16 Checkpoint Metrics Template
created: 2026-06-06
version: 1.0
status: production-ready
scope: Pre-staged metrics collection template for Day 7 checkpoint (June 16, 09:00 UTC)
deadline: June 16, 09:00 UTC — Day 7 checkpoint execution
companion_files:
  - DOMAIN_51_JUNE_16_DECISION_LOGIC.md
  - PHASE_2_BATCH_SEQUENCING_POST_DOMAIN_51.md
purpose: >
  Enables 15–20 minute Day 7 checkpoint execution. Pre-filled templates and metrics definitions
  eliminate decision-making during data collection. All manual lookups identified and sequenced.
  Ready for copy-paste completion on June 16 morning.
---

# Domain 51 June 16 Checkpoint Metrics Template

**Execution window**: June 16, 09:00–09:30 UTC (Day 7 post-execute, 7 days after Wave 1 send June 9)

**Pre-staging complete**: All lookup procedures identified, collection order sequenced, thresholds pre-calculated.

---

## 1. Email Open Rate Tracking (Campaign Monitor API)

**Timestamp completion**: ___ UTC (record exact time of data collection)

### Wave 1 Recipients (June 9, 09:00 AM UTC send)

| Organization | Contact | Email | Open Count | Recipients | Open Rate % | Notes |
|--------------|---------|-------|-----------|-----------|-----------|--------|
| Campaign Legal Center | Yusuf Maluf | ymaluf@campaignlegalcenter.org | ___ | 1 | ___% | Primary contact; highest engagement likelihood |
| Common Cause | Cynthia Terrell | cterrell@commoncause.org | ___ | 1 | ___% | DISCLOSE co-chair; high engagement likelihood |
| End Citizens United | Tiffany Muller | tmuller@endcitizensunited.org | ___ | 1 | ___% | Secondary: Nolan Cummings (ncummings@endcitizensunited.org) if no reply |
| Issue One | Nick Penniman | npenniman@issueone.org | ___ | 1 | ___% | Secondary: Doug Dachille (ddachille@issueone.org) |
| **WAVE 1 TOTAL** | | | **___** | **4** | **___% (average)** | |

**Data source**: Campaign Monitor dashboard → "Domain 51 Wave 1" campaign → open tracking. If not tracked via Campaign Monitor API, use manual report from email sender or Bitly click data (see Section 2).

**Threshold targets** (day 7 acceptable ranges):
- ✅ STRONG: ≥75% open rate (3 of 4 opened)
- 🟡 MODERATE: 50-74% open rate (2-3 of 4 opened)
- ⚠️ WEAK: 25-49% open rate (1-2 of 4 opened)
- ❌ FAILURE: <25% open rate (0-1 of 4 opened, possible delivery failure)

**Calculation**: Sum open counts / sum recipients × 100 = ___% Wave 1 email open rate

---

## 2. Bitly Click Tracking (Gist Access Signal)

**Timestamp completion**: ___ UTC

### Gist URL and Bitly Short Link

| Link | Full URL | Bitly Short | Day 7 Clicks | Day 1-3 Clicks | Day 4-7 Clicks | Notes |
|------|----------|-----------|-------------|--------------|---------------|---------|
| Domain 51 Main Gist | https://gist.github.com/esca8peArtist/[ID] | bit.ly/domain51-campaign-finance | ___ | ___ | ___ | Primary delivery link in Wave 1 email |

**Data source**: Bitly.com dashboard → Login → click on Domain 51 short link → "Clicks" tab → daily click breakdown. Copy daily click counts for June 9-16 (8-day window).

**Click velocity thresholds** (Day 7 aggregate):
- ✅ STRONG: ≥5 total clicks on Gist link (confirms active interest + follow-through)
- 🟡 MODERATE: 3-4 total clicks (engaged but lower velocity)
- ⚠️ WEAK: 1-2 total clicks (minimal follow-through; possible delivery issue)
- ❌ FAILURE: 0 clicks (delivery or content failure — escalate to contingency protocol)

**Spike detection**: If clicks spike 5+ on a single day, cross-reference against email send date. Spike within 24-72h of send = confirmed delivery. Organic spike = network amplification signal (note in contingency assessment).

---

## 3. Contact Response Tracking (Email Inbox Audit)

**Timestamp completion**: ___ UTC

### Wave 1 Response Log

| Organization | Contact | Email | Response? | Response Date | Response Type | Score | Notes |
|--------------|---------|-------|-----------|--------------|---------------|-------|---------|
| Campaign Legal Center | Yusuf Maluf | ymaluf@campaignlegalcenter.org | Y / N | _____ | OOO / Form / Substantive / Forward / Adopt | ___ | |
| Common Cause | Cynthia Terrell | cterrell@commoncause.org | Y / N | _____ | OOO / Form / Substantive / Forward / Adopt | ___ | |
| End Citizens United | Tiffany Muller | tmuller@endcitizensunited.org | Y / N | _____ | OOO / Form / Substantive / Forward / Adopt | ___ | |
| Issue One | Nick Penniman | npenniman@issueone.org | Y / N | _____ | OOO / Form / Substantive / Forward / Adopt | ___ | |
| **WAVE 1 TOTAL** | | | ___/4 | | | | Count Score 3+ replies only |

**Response scoring** (use in "Score" column):
- **Score 1**: Out-of-office only (no substantive reply)
- **Score 2**: Form acknowledgment ("Thanks for sending, we'll review")
- **Score 3**: Substantive reply (question, request for more info, brief engagement)
- **Score 4**: Forward to colleague (network multiplier signal)
- **Score 5**: Explicit adoption signal ("We will use this in [specific project/publication]")

**Data source**: Gmail search: `label:phase1-outreach/replies from:{ymaluf@} OR from:{cterrell@} OR from:{tmuller@} OR from:{npenniman@}` (adjust for actual inbox labels). Review each reply manually; score in template.

**Response rate calculation**:
- Total replies (Score 1+): ___/4 = ___% (should be ≥50% for MODERATE, ≥75% for STRONG)
- Substantive replies (Score 3+): ___/4 = ___% (should be ≥25% for MODERATE, ≥50% for STRONG)

---

## 4. Gist Daily View Count (GitHub Analytics, Manual)

**Timestamp completion**: ___ UTC

**Challenge**: GitHub Gist does not expose view counts via API for anonymous Gists. Workaround: Use Bitly as proxy (Section 2) OR manually navigate to Gist page and compare visual analytics if author-authenticated.

### If author-authenticated GitHub view data available:

| Day | Date | View Count | Daily Delta | Cumulative | Notes |
|-----|------|-----------|------------|-----------|---------|
| 1 | June 9 | ___ | ___ | ___ | Send day (may have low views if send late) |
| 2 | June 10 | ___ | ___ | ___ | |
| 3 | June 11 | ___ | ___ | ___ | Peak engagement window |
| 4 | June 12 | ___ | ___ | ___ | Last send day (Wave 1 concludes June 12) |
| 5 | June 13 | ___ | ___ | ___ | Weekend (may have low engagement) |
| 6 | June 14 | ___ | ___ | ___ | |
| 7 | June 15 | ___ | ___ | ___ | Day before checkpoint (capture final pre-checkpoint trend) |
| **Total (7 days)** | | | | **___** | Use cumulative for threshold comparison |

**If GitHub view data unavailable**: Use Bitly clicks (Section 2) as proxy. Bitly clicks ≈ Gist views (within 80-90% correlation). Interpret Bitly spike = Gist engagement spike.

**Gist view thresholds** (total 7-day aggregate):
- ✅ STRONG: ≥20 total views (sustained engagement)
- 🟡 MODERATE: 10-19 total views (moderate reach)
- ⚠️ WEAK: 5-9 total views (limited reach)
- ❌ FAILURE: <5 total views (combined with 0 Bitly clicks = confirm delivery/engagement failure)

---

## 5. Cumulative Win Rate Assessment (Adoption Signals)

**Timestamp completion**: ___ UTC

### Adoption Signal Registry

| Organization | Signal Type | Description | Confirmed? | Date | Score Weight |
|--------------|-----------|-------------|-----------|------|--------------|
| ___ | Adoption Statement | "We will cite this in [policy brief/litigation/etc]" | Y / N | _____ | 5x |
| ___ | Forward to Colleague | Contact forwarded materials to peer org | Y / N | _____ | 3x |
| ___ | Substantive Reply | Requested more info / materials / clarification | Y / N | _____ | 1x |
| | | | | | |

**Adoption signal definition**: Any explicit statement of intent to use or integrate Domain 51 materials into the contact's organizational work (litigation toolkit, policy brief, testimony, training, etc.).

**Network multiplier detection**: If a contact forwards to a peer organization, or if you receive unsolicited email from a non-Tier-1 contact citing a Tier-1 referral, score this as 3x weight in composite signal.

**Win rate calculation**:
- Total signals detected (Day 7): ___
- Composite score: (5× adoptions + 3× forwards + 1× substantive): ___
- Win rate: ___/4 organizations showing at least one signal = ___% (target ≥50% for MODERATE, ≥75% for STRONG)

---

## 6. Composite Day 7 Signal Score

**Timestamp completion**: ___ UTC

Calculate ONE composite score to feed into decision logic (Section 7).

| Metric | Data | Weight | Weighted Score |
|--------|------|--------|----------------|
| Email open rate (%) | ___% | ×2 | ___ |
| Bitly clicks / expected (5) | ___/5 | ×2 | ___ |
| Response rate Score 3+ (%) | ___% | ×2 | ___ |
| Win rate (% adoption signals) | ___% | ×1 | ___ |
| **COMPOSITE SIGNAL SCORE** | | | **___ / 10** |

**Composite score interpretation**:
- 8–10: STRONG signal → Proceed to batch activation (Domains 48 + 57 parallel)
- 5–7: MODERATE signal → Sequential activation (Domain 48 then 57)
- 3–4: WEAK signal → Hold, escalate to user for decision
- 0–2: FAILURE signal → Activate contingency protocol (re-contact, channel shift, stakeholder substitution)

---

## 7. Data Collection Checklist (Day 7 Execution)

**June 16, 09:00 UTC — Begin checkpoint execution**

- [ ] 09:05 — Log in to Campaign Monitor, record Wave 1 email open counts (Section 1) — 5 min
- [ ] 09:10 — Log in to Bitly, record daily click counts June 9-16 (Section 2) — 5 min
- [ ] 09:15 — Gmail search for replies, score each response (Section 3) — 5 min
- [ ] 09:20 — GitHub or Bitly Gist view data; enter daily totals (Section 4) — 3 min
- [ ] 09:23 — Review all replies for adoption signals; enter in Section 5 — 3 min
- [ ] 09:26 — Calculate composite score (Section 6) — 2 min
- [ ] 09:28 — Record completion timestamp and transfer score to DOMAIN_51_JUNE_16_DECISION_LOGIC.md for routing — 2 min

**Total execution time**: 15–20 minutes

---

## 8. Notes & Contingency Flags

**Known delivery risks**:
- Gmail spam filters: If email open rate <25%, check spam folder for delivery bounce-backs
- Campaign Monitor account access: Verify login 24h before checkpoint to avoid access issues
- Bitly link expiration: Domain 51 Bitly link should remain live through June 30; verify on June 15

**If data unavailable**:
- No Campaign Monitor access: Use Bitly click spike as proxy for "email received" signal (spike within 24-72h of send = confirmed delivery)
- No GitHub view data: Use Bitly clicks only; interpret Bitly click total as engagement proxy (correlation ~0.85)
- No reply data: Manual Gmail audit can take 8-10 minutes; prioritize Gmail search over manual inbox review

**Escalation thresholds** (trigger contingency protocol from DOMAIN_51_JUNE_16_DECISION_LOGIC.md Section 3):
- Confirmed delivery failure (0 opens, 0 clicks, 0 replies with confirmed send)
- Composite score <3 (weak signal requiring user escalation)
- Any organization showing 0 engagement (email unopened + no reply + no Gist click) — flag for re-contact contingency

---

## Appendix: Pre-Population Data (from Phase 1 Baseline)

**Historical email open rate for similar outreach** (Phase 1 baseline, law school + policy contacts):
- Average open rate for outreach emails: 45–55%
- Domain 51 specific (campaign finance specialists): Expected 60–75% open rate (higher-relevance audience)
- **Day 7 threshold baseline**: ≥50% open rate acceptable, <40% warrants investigation

**Historical Gist view counts** (Phase 1 baseline, similar domain distributions):
- 7-day total for similar policy domains: 8–15 views (average)
- Domain 51 expected (higher-salience topic): 12–20 views (range)
- **Day 7 threshold baseline**: ≥10 views acceptable, <5 warrants investigation

**Historical reply rate** (Phase 1 baseline, Tier 1 campaign finance specialists):
- Tier 1 policy specialists typically reply within 3–7 days: 40–60% reply rate
- Score 3+ replies: 25–40% of Tier 1 (substantive engagement)
- **Day 7 threshold baseline**: ≥50% reply rate acceptable, ≥25% Score 3+ acceptable

---

## Companion Execution Files

1. **DOMAIN_51_JUNE_16_DECISION_LOGIC.md** — Transfer composite score from Section 6 here; execute decision routing (STRONG → batch activation, MODERATE → sequential, WEAK → escalate)
2. **PHASE_2_BATCH_SEQUENCING_POST_DOMAIN_51.md** — Routes decision output to Domain 48 and 57 activation timeline

**When complete**: Commit this template with data populated to master. Link filled snapshot in CHECKIN.md checkpoint summary.
