---
title: "Phase 1 Adoption Tracking — Deployment README"
created: 2026-06-03
version: 2.0
status: production-ready
activation: June 3, 2026 morning
---

# Phase 1 Adoption Tracking — June 3 Deployment

**System ready date**: June 3, 2026
**Activation window**: June 3 morning (any time)
**Phase 1 distribution**: Domain 56 sent May 28, Domain 39 sent June 1
**Day 7 checkpoint**: June 7-8
**Day 30 checkpoint**: June 27-28

This directory contains the complete Phase 1 adoption tracking system. Everything needed for June 3 activation is here. No external dependencies or additional setup required for basic operation.

---

## What This System Does

Every Monday at 09:00 UTC (automated via cron):
1. Polls all 8 Phase 1 Gist IDs for engagement signals (comments, forks)
2. Fetches Bitly click counts if configured
3. Retrieves Gmail replies from `phase-1-responses` label if configured
4. Evaluates data against Day 7/14/30 thresholds
5. Generates a weekly summary Markdown file in `data/`
6. Appends urgent alerts to `CHECKIN.md` if thresholds breached
7. Persists state for cumulative tracking across weeks

After cron runs, you review the summary file (5-10 min/week), update Google Sheets manually (10 min/week), and run the decision tree at checkpoint weeks (20 min).

Total user time: ~15 min/week normal weeks, ~40 min checkpoint weeks.

---

## File Index

| File | Purpose | Action needed |
|------|---------|---------------|
| `phase-1-adoption-tracking-script.py` | Main automation script | Run --run-now to start |
| `adoption-tracking-config.json` | Configuration (all Gist IDs pre-filled) | Add github_token (optional); enable Gmail if desired |
| `oauth2_login.py` | Gmail OAuth2 setup helper | Run once if enabling Gmail |
| `phase-1-adoption-tracking-setup.sh` | One-command setup script | Run for first-time install |
| `DEPLOYMENT_CHECKLIST.md` | Step-by-step June 3 activation | Follow this first |
| `GOOGLE_SHEETS_TEMPLATE_COMPLETE.md` | 7-tab Sheets setup with all formulas | Create dashboard if not done |
| `WEEK_1_DATA_COLLECTION_FRAMEWORK.md` | Day 1-7 checklist, reply triage, scoring | Read before Day 7 checkpoint |
| `DAY_7_CHECKPOINT_DECISION_TREE.md` | Day 7 + Phase 2 Domain 58/59 logic | Run June 7-8 |
| `data/` | Auto-created weekly summaries and state | Review after each Monday run |
| `logs/` | Execution log | Check if any run fails |

---

## 10-Minute Quick Start

```bash
# 1. Navigate to this directory
cd /home/awank/dev/SuperClaude_Framework/projects/resistance-research/phase-1-adoption

# 2. Install dependencies (one-time)
pip3 install requests

# 3. Check configuration
python3 phase-1-adoption-tracking-script.py --check-config

# 4. Run first collection
python3 phase-1-adoption-tracking-script.py --run-now

# 5. Install weekly cron
python3 phase-1-adoption-tracking-script.py --schedule-weekly
# Copy the printed line into: crontab -e

# 6. Verify everything
crontab -l | grep adoption-tracking
ls data/
```

That is all that is required for basic operation. Gmail and Bitly integrations are optional enhancements.

---

## Weekly Operations (after setup)

**Every Monday, automated** (no user action):
- Cron runs at 09:00 UTC
- Generates `data/week-NN-YYYY-MM-DD-summary.md`
- Appends alerts to CHECKIN.md if any are triggered

**Every Monday, manual (15 min)**:
1. Read the weekly summary file in `data/`
2. Pull Bitly click counts from bitly.com (3 min)
3. Update Google Sheets Gist_Views tab
4. Score any new Gmail replies from `phase-1-responses` label
5. Enter scored replies in Sheets Replies tab
6. Update Sheets Contacts tab (Reply_Date, Reply_Score, Delivery_Status)
7. Complete PHASE_1_WEEKLY_SYNTHESIS_TEMPLATE.md Sections 1-6

**Checkpoint weeks (Days 7, 14, 30, 60)**:
```bash
# Day 7 (June 7-8)
python3 phase-1-adoption-tracking-script.py --day7-report

# Day 30 (June 27-28)
python3 phase-1-adoption-tracking-script.py --day30-report
```
Follow the printed decision trees. Enter results in Sheets Checkpoints tab. Update CHECKIN.md.

---

## Key Thresholds

| Checkpoint | HOLD (pass) | MONITOR (watch) | ESCALATE (action needed) |
|-----------|-------------|-----------------|--------------------------|
| Day 7 | 15+ clicks AND 2+ replies | 5-14 clicks OR 0-1 replies | 0-4 clicks, confirmed delivery |
| Day 14 | 25+ cumulative clicks | 10-24 cumulative clicks | <10 cumulative clicks |
| Day 30 | STRONG (A>=50%, B>=4, C>=3, D>=2) | MODERATE (partial) | FAILURE (all zeros) |
| Day 60 | 15+ confirmed adoptions, 100+ reached | 8+ adoptions, 50+ reached | <8 adoptions, <4 constituencies |

Key: A=Score3+ rate, B=constituencies at strong threshold, C=cross-org refs, D=confirmed adoptions

---

## Alert Levels

| Level | Meaning | Response time |
|-------|---------|---------------|
| INFO | Informational; no action | — |
| MONITOR | Below target; recheck next checkpoint | Before next checkpoint |
| ESCALATE | Possible delivery failure; diagnostic needed | Within 24 hours |
| FAILURE_IMMINENT | Critical threshold breached | Within 48 hours |
| ESCALATE_NOW | Score 5 adoption or Score 4 cluster | Same day |
| URGENT | Bounce threshold exceeded | Within 24 hours |

Alerts above MONITOR level are auto-appended to CHECKIN.md.

---

## Live Gist URLs (Phase 1 Distribution)

All verified accessible as of June 1, 2026:

| Domain | Gist URL |
|--------|---------|
| Domain 56 — Civil Service | https://gist.github.com/esca8peArtist/8f11e868397921a4e6556b41196d1b1f |
| Domain 39 — Healthcare | https://gist.github.com/esca8peArtist/131e8a94c955b973b87f7fb87d0f594b |
| Domain 59 — Economic Precarity | https://gist.github.com/esca8peArtist/70b18a6f26dc879e3399c6d147d882ba |
| Domain 37 — Fed Interference | https://gist.github.com/esca8peArtist/1277f5d5bcb0fe46604bbaba8fa37fd0 |
| Domain 58 — Tribal Sovereignty | https://gist.github.com/esca8peArtist/0caf4e1ab5661355ea2df5e53d3c169f |
| Full Proposal | https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261 |
| Executive Summary | https://gist.github.com/esca8peArtist/2869da6eaeb15a47246ade3bbbc4a3f4 |
| Litigation Tracker | https://gist.github.com/esca8peArtist/418d51bda087f15a04d685ab171a5ee0 |

---

## Phase 2 Activation Summary

The Day 30 determination drives all Phase 2 sequencing:

**STRONG** (A>=50%, B>=4, C>=3, D>=2):
- Domain 39 + 56 launch immediately
- Domain 58 + 59 activate Weeks 5-8
- Tier 2 (91 contacts) begins

**MODERATE** (partial signals, not STRONG):
- Domain 39 Day 1 (non-negotiable)
- Domain 56 holds to Day 37
- Domain 58 + 59 stage for Day 60

**WEAK/FAILURE**: Apply recovery Modifications 1-3 before any Phase 2 sends.

Early activation (pre-Day-30): Score 5 adoption or Score 4 cluster in Days 1-14 triggers immediate Phase 2 pre-activation — see `DAY_7_CHECKPOINT_DECISION_TREE.md` Part 2.

---

## Troubleshooting

**Script fails with ImportError**:
```bash
pip3 install requests
# For Gmail monitoring:
pip3 install google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

**GitHub rate limit (60 req/hr)**:
- Add a GitHub personal access token to config (`github_token` field)
- Token needs no scopes — public read is sufficient

**Gmail token expired (401 error)**:
```bash
rm token.json
python3 oauth2_login.py
```

**Cron not running**:
```bash
# Check daemon
systemctl status cron
# Check crontab
crontab -l
# Test manually
python3 phase-1-adoption-tracking-script.py --run-now
```

**Gist returns HTTP 404**:
- Verify the Gist ID is correct (from DISTRIBUTION_GIST_URLS.md)
- Check that the Gist is set to "Public" (not "Secret")

---

## Reference Files (parent directory)

| File | Purpose |
|------|---------|
| `PHASE_1_MEASUREMENT_SYSTEM.md` | Adoption levels, thresholds, overhead analysis |
| `PHASE_1_MEASUREMENT_SPREADSHEET_SPEC.md` | Sheets schema (canonical reference) |
| `day-7-14-30-decision-trees.md` | Full decision trees for all checkpoints |
| `PHASE_1_WEEKLY_SYNTHESIS_TEMPLATE.md` | Monday synthesis template (copy each week) |
| `reply-triage-framework.md` | Reply scoring decision tree |
| `DISTRIBUTION_GIST_URLS.md` | All live Gist URLs with verification status |
| `CHECKIN.md` | Escalation target for urgent alerts |
| `PHASE_2_ACTIVATION_DECISION_TREE.md` | Full Phase 2 sequencing |

---

**Version**: 2.0 — June 3, 2026
**Status**: Production-ready for immediate activation
**Last updated**: June 3, 2026 (session 2507)
