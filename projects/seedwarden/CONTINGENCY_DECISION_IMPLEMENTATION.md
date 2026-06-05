---
title: "Contingency Decision Implementation — Python Translation of 8-Scenario Tree"
created: 2026-06-05
item: 85
status: production-ready
purpose: >
  Python translation of CONTINGENCY_TRIGGER_DECISION_TREE.md: numeric thresholds,
  deterministic GO/CAUTION/NO-GO routing, worked example, and integration notes
  for TRACK_B_MONITORING_AUTOMATION_SCRIPTS.py.
references:
  - CONTINGENCY_TRIGGER_DECISION_TREE.md (primary source — full runbooks)
  - TRACK_B_MONITORING_AUTOMATION_FRAMEWORK.md (metric collection procedures)
  - TRACK_B_MONITORING_AUTOMATION_SCRIPTS.py (implementation: ContingencyDecisionEngine)
  - DAY_3_AND_7_DECISION_GATES.md (predecessor threshold reference)
---

# Contingency Decision Implementation
## Python Translation of the 8-Scenario Decision Tree

This document explains how `CONTINGENCY_TRIGGER_DECISION_TREE.md` maps to the
`ContingencyDecisionEngine` class in `TRACK_B_MONITORING_AUTOMATION_SCRIPTS.py`.
It serves three audiences:

1. **Automation reviewers** — verifying the script faithfully implements the runbook thresholds
2. **Operators** — understanding why the script produced a specific decision on a given day
3. **Future maintainers** — updating thresholds when the campaign evolves

---

## 1. The 4 Input Metrics

The decision tree consumes exactly 4 data streams. All other signals (Reddit upvotes,
Instagram reach, Twitter mentions) are supplementary and feed the social traction
scenario (S6) rather than the primary go/no-go gate.

| Stream | Variable name in script | Source module |
|--------|------------------------|---------------|
| Email performance | `email_open_rate_pct`, `email_unsub_rate_pct` | CampaignMonitorClient |
| Gist view count | `gist_views` | GistViewPoller |
| Etsy sales | `etsy_orders`, `etsy_total_revenue_usd`, `etsy_attribution` | EtsySalesExtractor |
| Kit funnel | `kit_new_subscribers` | KitFunnelFetcher |

Manual overrides (passed via CLI flags) supplement or replace any of these values when
API data is unavailable. The decision engine cannot distinguish API-fetched from
manually-entered values — it only sees the final metric dict.

---

## 2. The 8 Named Scenarios

Each scenario maps to a method in `ContingencyDecisionEngine`. The method signature is:

```python
_evaluate_s{N}_{name}(metric_value, checkpoint_day) -> dict
# Returns: {scenario_key, name, status, metric_value, rationale}
```

### Scenario A — Email Open Rate (S1)

**Source doc**: CONTINGENCY_TRIGGER_DECISION_TREE.md Scenario 1

**Thresholds** (checkpoint-day independent):

| Range | Status | Script constant |
|-------|--------|----------------|
| >= 20% | GO | `go_threshold = 20.0` |
| 10% – 19.9% | CAUTION | `caution_range = (10.0, 19.9)` |
| < 10% | NO-GO | `nogo_threshold = 10.0` |

**Python logic** (from `_evaluate_s1_email_open_rate`):
```python
if open_rate >= 20.0:
    status = "GO"
elif open_rate >= 10.0:
    status = "CAUTION"   # send re-engagement to non-openers
else:
    status = "NO-GO"     # SPF/DKIM check; Gmail fallback for Tier 1
```

**Rationale for >30% drop anomaly detection** (separate from status classification):
The `detect_anomalies` method in `CampaignMonitorClient` applies an additional rule:
if any consecutive template pair shows >30% open-rate drop, a LOW-ENGAGEMENT WARNING
is appended to `email_anomalies`. This rule fires independently of the GO/CAUTION/NO-GO
classification and is reported in the checkpoint markdown as a separate anomalies block.

---

### Scenario B — Gist View Count (S2)

**Source doc**: CONTINGENCY_TRIGGER_DECISION_TREE.md Scenario 2

**Thresholds** (checkpoint-day dependent):

| Checkpoint | GO threshold | CAUTION range | NO-GO threshold |
|------------|-------------|---------------|----------------|
| Day 3 | > 70 views | 30–70 | < 30 |
| Day 7 | > 200 views | 100–200 | < 50 |
| Day 14 | > 400 views | 150–400 | < 150 |

**Python logic** (from `_evaluate_s2_gist_views`):
```python
day_t = SCENARIOS["S2_gist_views"]["thresholds_by_day"][checkpoint_day]
if views >= day_t["go"]:
    status = "GO"
elif views >= day_t["caution_lo"]:
    status = "CAUTION"   # cross-post to new community
else:
    status = "NO-GO"     # audit URL placement; check Reddit post removal
```

Note: Day 7 has a separate NO-GO floor of 50 views that is lower than the CAUTION floor
of 100. This means the status sequence at Day 7 is: GO (>200) > CAUTION (100–200) >
CAUTION (50–99) > NO-GO (<50). The 50-100 band is still CAUTION, not NO-GO, because the
Item 59 framework treats Day 7 views < 50 specifically as the "despite correct URL
placement and Reddit posts live" NO-GO trigger.

---

### Scenario C — Zero Sales / Revenue (S3)

**Source doc**: CONTINGENCY_TRIGGER_DECISION_TREE.md Scenario 3

**Thresholds** (checkpoint-day dependent):

| Checkpoint | GO | CAUTION | NO-GO |
|------------|-----|---------|-------|
| Day 3 | >= 1 order | 0 orders (note but don't escalate) | — (not applicable Day 3) |
| Day 7 | >= 1 order | 0 orders + listing Active | 0 orders + listing not Active |
| Day 14 | >= 3 orders | 1–2 orders | 0 orders + listing Active 5+ days |

**Python logic** (from `_evaluate_s3_sales`):
```python
if checkpoint_day == 3:
    if orders >= 1: status = "GO"
    else: status = "CAUTION"   # expected — no escalation at Day 3
elif checkpoint_day == 7:
    if orders >= 1: status = "GO"
    elif not listing_active: status = "NO-GO"   # publish listing immediately
    else: status = "CAUTION"   # SEO/thumbnail investigation
else:  # Day 14
    if orders >= 3: status = "GO"
    elif orders >= 1: status = "CAUTION"   # price test, sale badge
    else: status = "NO-GO"   # $2 price drop; pivot to Kit-gated PDF
```

The `etsy_listing_active` metric defaults to `True` in the script (Etsy API does not
return listing status through the orders endpoint). Override with
`--etsy-listing-active False` if the listing is Draft or Deactivated.

---

### Scenario D — Influencer Silence (S4)

**Source doc**: CONTINGENCY_TRIGGER_DECISION_TREE.md Scenario 4

**Thresholds** (checkpoint-day dependent):

| Checkpoint | GO | CAUTION | NO-GO |
|------------|-----|---------|-------|
| Day 3 | >= 1 response | 0 responses (normal — no action) | — |
| Day 7 | >= 3 public shares | 1–2 shares | 0 responses from all 15 |
| Day 14 | >= 3 public shares | 1–2 shares | 0 (if email channel also failed) |

**Python logic** (from `_evaluate_s4_influencer`):
```python
if checkpoint_day == 3:
    if responses >= 1: status = "GO"
    else: status = "CAUTION"   # 3-7d response time — no action yet
elif checkpoint_day == 7:
    if responses == 0: status = "NO-GO"   # follow-up to top 5 Tier 1 contacts
    elif responses >= 3: status = "GO"
    else: status = "CAUTION"
else:  # Day 14
    if responses >= 3: status = "GO"
    elif responses >= 1: status = "CAUTION"
    else: status = "NO-GO"   # pivot to platform engagement
```

`influencer_responses` is always a manual override — there is no API to count influencer
replies or public shares. Pass via `--influencer-responses N` when running the script.

---

### Scenario E — High Unsubscribe Rate (S5)

**Source doc**: CONTINGENCY_TRIGGER_DECISION_TREE.md Scenario 5

**Thresholds** (checkpoint-day independent):

| Range | Status |
|-------|--------|
| >= 5% unsubscribes | NO-GO |
| 2% – 4.9% | CAUTION |
| < 2% | GO |

**Python logic** (from `_evaluate_s5_unsub_rate`):
```python
if unsub_rate > 5.0:
    status = "NO-GO"    # pause all broadcasts; audit subscriber source
elif unsub_rate >= 2.0:
    status = "CAUTION"  # pause broadcasts 48h; revise next send
else:
    status = "GO"
```

This scenario is populated from Campaign Monitor's `Unsubscribed` field in the campaign
summary response, divided by `TotalRecipients`. It is computed automatically by
`CampaignMonitorClient.compute_template_metrics`.

---

### Scenario F — Social Media Zero Traction (S6)

**Source doc**: CONTINGENCY_TRIGGER_DECISION_TREE.md Scenario 6

**Thresholds** (Day 7+ only — not evaluated at Day 3):

| Condition | Status |
|-----------|--------|
| Instagram reach >= 200 | GO |
| Instagram reach < 200 (alone) | CAUTION |
| Instagram reach < 200 AND (Twitter = 0 OR Reddit = 0) | NO-GO |

**Python logic** (from `_evaluate_s6_social`):
```python
if checkpoint_day == 3:
    return "GO"  # not evaluated at Day 3
reach_low = instagram_reach < 200
twitter_zero = twitter_mentions == 0
reddit_zero = reddit_upvotes == 0
if reach_low and (twitter_zero or reddit_zero):
    status = "NO-GO"    # check account standing; shift to community participation
elif reach_low:
    status = "CAUTION"
else:
    status = "GO"
```

Instagram reach, Twitter mentions, and Reddit upvotes are all manual overrides (no
automated API integration in this version). Pass them via `--instagram-reach`,
`--twitter-mentions`, `--reddit-upvotes`.

---

### Scenario G — Revenue Channel Mismatch (S7)

**Source doc**: CONTINGENCY_TRIGGER_DECISION_TREE.md Scenario 7

This is a qualitative scenario detected by comparing email performance against Etsy
revenue data. The script implements a simplified rule: if email is at GO level but Etsy
shows 0 orders, the mismatch is flagged as CAUTION (not NO-GO, because it may indicate a
funnel gap rather than a campaign failure).

**Python logic** (from `_evaluate_s7_channel_mismatch`):
```python
email_strong = open_rate >= 20.0
no_sales = orders == 0
if checkpoint_day == 3 or open_rate is None or orders is None:
    return "GO"  # insufficient data
if email_strong and no_sales:
    status = "CAUTION"  # above-the-fold CTA on Gist; check Etsy listing SEO
else:
    status = "GO"
```

A full channel mismatch analysis (Etsy attribution by coupon code vs email click source)
is available in the `etsy_attribution` field of the checkpoint result. The script does not
auto-classify S7 based on attribution ratios because that requires knowing total email
clicks, which Campaign Monitor's summary endpoint does not break down by click destination.

---

### Scenario H — Multi-Failure Escalation (S8)

**Source doc**: CONTINGENCY_TRIGGER_DECISION_TREE.md Scenario 8

This scenario fires automatically when 2 or more of S1–S7 are simultaneously in NO-GO.
It preempts all individual scenario runbooks — the operator must complete the root-cause
triage from Scenario 8 before executing any individual scenario.

**Python logic** (inside `evaluate` method):
```python
nogo_scenarios = [key for key, result in results if result["status"] == "NO-GO"]
multi_failure = len(nogo_scenarios) >= 2
if multi_failure:
    overall_status = "NO-GO"
    recommended_action = (
        "Execute Scenario 8 root-cause triage BEFORE any individual scenario."
    )
```

**Root causes A/B/C** are described in the report rationale string:
- **Root cause A** (launch did not execute): check sent folders, Kit automation status,
  Reddit post history
- **Root cause B** (distribution infrastructure broken): test Gist URL in incognito,
  check Kit landing page accessibility, verify email domain on blocklists
- **Root cause C** (audience mismatch): all infrastructure working but engagement near
  zero across all channels — requires positioning revision before Day 14

---

## 3. Overall Status Derivation

The overall GO/CAUTION/NO-GO decision is determined by the following logic in
`ContingencyDecisionEngine.evaluate`:

```python
nogo_scenarios = [s for s in results if s["status"] == "NO-GO"]
caution_scenarios = [s for s in results if s["status"] == "CAUTION"]

if len(nogo_scenarios) >= 2:      # multi-failure
    overall = "NO-GO"
elif len(nogo_scenarios) >= 1:    # single NO-GO
    overall = "NO-GO"
elif len(caution_scenarios) >= 1: # any caution
    overall = "CAUTION"
else:
    overall = "GO"
```

Any single NO-GO scenario produces an overall NO-GO result (conservative by design).
This matches the CONTINGENCY_TRIGGER_DECISION_TREE.md guidance: "Stabilize before
committing to Phase 2 expansion."

---

## 4. Threshold Consolidation Table

All 8 scenarios with their numeric thresholds consolidated for quick reference:

| Scenario | Metric | Day 3 GO | Day 3 CAUTION | Day 3 NO-GO | Day 7 GO | Day 7 CAUTION | Day 7 NO-GO | Day 14 GO | Day 14 CAUTION | Day 14 NO-GO |
|----------|--------|---------|--------------|------------|---------|--------------|------------|---------|---------------|------------|
| A: Email open rate | email_open_rate_pct | >=20% | 10–19% | <10% | >=20% | 10–19% | <10% | >=20% | — | <20% cumulative |
| B: Gist views | gist_views | >70 | 30–70 | <30 | >200 | 100–200 | <50 | >400 | 150–400 | <150 |
| C: Zero sales | etsy_orders | >=1 | 0 | — | >=1 | 0+active | 0+inactive | >=3 | 1–2 | 0+active |
| D: Influencer silence | influencer_responses | >=1 | 0 | — | >=3 | 1–2 | 0 | >=3 | 1–2 | 0 |
| E: Unsub rate | email_unsub_rate_pct | <2% | 2–5% | >5% | <2% | 2–5% | >5% | <2% | 2–5% | >5% |
| F: Social traction | instagram_reach | n/a | n/a | n/a | >=200 | <200 (alone) | <200+other0 | >=200 | <200 | <200+other0 |
| G: Channel mismatch | email+etsy combined | — | email GO+0 sales | — | — | email GO+0 sales | — | — | — | — |
| H: Multi-failure | count of NO-GO | — | — | >=2 NO-GO | — | — | >=2 NO-GO | — | — | >=2 NO-GO |

---

## 5. Worked Example — Day 7 Checkpoint

Assume the following metric values are returned by the 4 modules after a live run on
June 11, 2026 (Day 7):

```
email_open_rate_pct = 15.2
email_unsub_rate_pct = 1.8
gist_views = 145
etsy_orders = 1
etsy_listing_active = True
influencer_responses = 2
instagram_reach = 280
twitter_mentions = 1
reddit_upvotes = 22
kit_new_subscribers = 18
```

**Scenario-by-scenario evaluation:**

**S1 (Email open rate)**: 15.2% is in range 10–19% → **CAUTION**
- Rationale: send re-engagement broadcast to non-openers with revised subject line.

**S2 (Gist views)**: 145 is in range 100–200 for Day 7 → **CAUTION**
- Rationale: below GO threshold (200) but above NO-GO floor (50). Cross-post to one
  new community not yet reached.

**S3 (Sales)**: 1 order, listing Active → **GO**
- Rationale: at least 1 sale validates the Etsy channel.

**S4 (Influencer)**: 2 responses at Day 7 → **CAUTION**
- Rationale: below GO threshold of 3 shares. Continue monitoring. Send one follow-up
  to remaining Tier 1 contacts.

**S5 (Unsub rate)**: 1.8% → **GO**
- Rationale: below 2% CAUTION floor, list health is good.

**S6 (Social traction)**: Instagram reach 280 >= 200 → **GO**
- Rationale: reach threshold met.

**S7 (Channel mismatch)**: Email at 15.2% (CAUTION) and 1 Etsy order → **GO**
- Rationale: email not at GO level, so mismatch rule does not fire.

**S8 (Multi-failure)**: 0 NO-GO scenarios → **GO** (multi-failure not triggered)

**Active NO-GO scenarios**: none

**Active CAUTION scenarios**: S1, S2, S4

**Overall status**: **CAUTION** (no NO-GO, but multiple CAUTION)

**Recommended action**: "CAUTION on some metrics. Continue current plan. Investigate
the specific gap. Do not expand scope until gap is understood."

**Interpretation**: The campaign is running below target on email open rate, Gist
distribution, and influencer engagement — but none of these are critical failures.
This maps to the "YELLOW" outcome in TRACK_B_CHECKPOINT_DECISION_FRAMEWORK.md:
Phase 3 deferred to June 29 contingency window. Activate Week 2 acceleration sprint
(Tier 2 influencer outreach, 1×/day social posting frequency, founding subscriber
referral campaign).

---

## 6. Updating Thresholds

If campaign performance data suggests the thresholds need revision (e.g., the product
launches later than June 4 and a different Gist growth curve applies), update the
`THRESHOLDS` dict at the top of `TRACK_B_MONITORING_AUTOMATION_SCRIPTS.py` and the
`thresholds_by_day` dict inside `ContingencyDecisionEngine.SCENARIOS["S2_gist_views"]`.

The unit tests in `TestContingencyDecisionEngine` will catch threshold regressions —
run them after any update:

```bash
uv run python TRACK_B_MONITORING_AUTOMATION_SCRIPTS.py --test
```

All 21 unit tests should pass. If a threshold change causes a test to fail, either
update the test to match the new threshold or investigate whether the change was
intentional.

---

## 7. Mapping to CONTINGENCY_TRIGGER_DECISION_TREE.md Sections

For traceability, the Python implementation maps to the source document as follows:

| Python class / method | Source section |
|----------------------|----------------|
| `ContingencyDecisionEngine._evaluate_s1_email_open_rate` | Scenario 1: Low Email Open Rate |
| `ContingencyDecisionEngine._evaluate_s2_gist_views` | Scenario 2: Low Gist View Count |
| `ContingencyDecisionEngine._evaluate_s3_sales` | Scenario 3: Zero Sales |
| `ContingencyDecisionEngine._evaluate_s4_influencer` | Scenario 4: Influencer Silence |
| `ContingencyDecisionEngine._evaluate_s5_unsub_rate` | Scenario 5: High Unsubscribe Rate |
| `ContingencyDecisionEngine._evaluate_s6_social` | Scenario 6: Social Media Zero Traction |
| `ContingencyDecisionEngine._evaluate_s7_channel_mismatch` | Scenario 7: Sales/Revenue Channel Mismatch |
| `ContingencyDecisionEngine.evaluate` (S8 block) | Scenario 8: Multi-Failure Escalation Protocol |
| `CampaignMonitorClient.detect_anomalies` | Scenario 1, Step B (deliverability signals) |
| `THRESHOLDS` dict | Threshold Master Table |

The complete step-by-step runbooks for each scenario (Steps A–E in each scenario) are in
`CONTINGENCY_TRIGGER_DECISION_TREE.md` and are intentionally not reproduced here. This
document focuses on the numeric translation and routing logic only.

---

*Document version: 1.0 — June 5, 2026 (Item 85)*
*Script: TRACK_B_MONITORING_AUTOMATION_SCRIPTS.py (ContingencyDecisionEngine class)*
*Source: CONTINGENCY_TRIGGER_DECISION_TREE.md*
