---
title: "Phase 1 Rapid-Response — Quick-Reference Command Card"
created: 2026-05-31
version: 1.0
status: production-ready
scope: >
  0.5-page reference card. Five Sheets formulas, three shell commands,
  and decision thresholds. Print this or pin it open alongside the dashboard
  during Day 7 checkpoint execution.
companion_files:
  - PHASE_1_RAPID_RESPONSE_OPERATIONAL_GUIDE.md
  - PHASE_1_RAPID_RESPONSE_DECISION_TREES.md
  - PHASE_1_RAPID_RESPONSE_SHEETS_TEMPLATES.md
---

# Phase 1 Rapid-Response — Quick-Reference Command Card

**Version 1.0 — May 31, 2026**

---

## 5 Sheets Formulas — Copy-Paste Into the Dashboard

All formulas use the exact column references from PHASE_1_MEASUREMENT_SPREADSHEET_SPEC.md.
Place in the Summary Block area at the top of the Contacts tab or in a dedicated cell.

---

**Formula 1: Overall Engagement Rate (all sectors combined)**

```
=IFERROR(COUNTIF(Contacts!N2:N200,">=3")/COUNTIF(Contacts!I2:I200,"Delivered"),0)
```

Paste into a labeled cell. Format as percentage, 1 decimal. This is input (B) for Tree 1.

---

**Formula 2: Sector Weak-Signal Flag (for Sector_Engagement tab, Column H)**

```
=IF(AND(IFERROR(COUNTIFS(Contacts!E:E,A2,Contacts!N:N,">=3")/COUNTIFS(Contacts!E:E,A2,Contacts!I:I,"Delivered"),0)<0.15,IFERROR((COUNTIFS(Contacts!E:E,A2,Contacts!I:I,"Delivered")-COUNTIFS(Contacts!E:E,A2,Contacts!L:L,"<>"))/COUNTIFS(Contacts!E:E,A2,Contacts!I:I,"Delivered"),0)>0.70),"WEAK","OK")
```

Place in H2 of Sector_Engagement tab, drag down to H7. Returns "WEAK" when engagement < 15% AND no-reply > 70%.

---

**Formula 3: Phase 2 Trigger Status (for Phase2_Readiness tab, Cell D5)**

```
=IF(AND(IFERROR((COUNTA(Contacts!L2:L200)-COUNTBLANK(Contacts!L2:L200))/(TODAY()-MIN(Contacts!H2:H200)),0)>=0.5,COUNTIF(Sector_Engagement!H2:H7,"STRONG")+COUNTIF(Sector_Engagement!H2:H7,"MODERATE")>=3,COUNTIFS(Adoptions!E:E,"Referral",Adoptions!H:H,"Confirmed")>=1),"PHASE 2 TRIGGER — ACTIVATE NOW","Waiting on: "&IF(IFERROR((COUNTA(Contacts!L2:L200)-COUNTBLANK(Contacts!L2:L200))/(TODAY()-MIN(Contacts!H2:H200)),0)<0.5,"velocity ","")&IF(COUNTIF(Sector_Engagement!H2:H7,"STRONG")+COUNTIF(Sector_Engagement!H2:H7,"MODERATE")<3,"cross-sector ","")&IF(COUNTIFS(Adoptions!E:E,"Referral",Adoptions!H:H,"Confirmed")<1,"network",""))
```

---

**Formula 4: Follow-Up Queue Count (contacts in List A needing follow-up)**

```
=COUNTIFS(Followup_Matrix!I2:I200,"LIST A*",Followup_Matrix!E2:E200,"Delivered",Followup_Matrix!K2:K200,"")
```

Place in a labeled cell in the Followup_Matrix tab or in a dashboard summary cell. Shows the count of cold contacts with no follow-up sent yet.

---

**Formula 5: Cumulative Engagement Velocity (replies per day since first send)**

```
=IFERROR((COUNTA(Contacts!L2:L200)-COUNTBLANK(Contacts!L2:L200))/(TODAY()-MIN(Contacts!H2:H200)),0)
```

Format as decimal, 2 places. Target at Day 7: >= 0.30 (at least 2 replies in 7 days). Target at Day 14: >= 0.50.

---

## 3 Shell Commands — Gist View Export

Run these on the machine where the tracking script lives. Output feeds the Gist_Views tab manually.

---

**Command 1: Pull current Gist view counts (tracking script)**

```bash
python3 /home/awank/dev/SuperClaude_Framework/projects/resistance-research/phase-1-adoption-tracking-script.py --run-now --config /home/awank/dev/SuperClaude_Framework/projects/resistance-research/phase-1-adoption-tracking.json --output-dir /home/awank/dev/SuperClaude_Framework/projects/resistance-research/monitoring
```

Output: JSON summary in `monitoring/week-[date]-summary.md` with Gist view counts, email reply count, and any alerts. Run this first at the Day 7 checkpoint.

---

**Command 2: Fetch Gist metadata via GitHub API (manual view count check)**

```bash
curl -s -H "Authorization: token ${GITHUB_TOKEN}" \
  "https://api.github.com/gists/131e8a94c955b973b87f7fb87d0f594b" \
  | jq '{id: .id, description: .description, comments: .comments, updated_at: .updated_at}'
```

Replace `131e8a94c955b973b87f7fb87d0f594b` with any canonical Gist ID from the list below. Requires `GITHUB_TOKEN` environment variable set. The GitHub API does not expose raw view counts — use Bitly for click tracking; use this command only to verify the Gist is accessible and unchanged.

**Canonical Gist IDs:**
- Domain 39 (healthcare): `131e8a94c955b973b87f7fb87d0f594b`
- Domain 56 (civil service): `8f11e868397921a4e6556b41196d1b1f`
- Full proposal: `2dec7fd03b08ab5b41c55d402f44c261`
- Executive summary: `2869da6eaeb15a47246ade3bbbc4a3f4`
- Litigation tracker: `418d51bda087f15a04d685ab171a5ee0`

---

**Command 3: Export recent monitoring summaries to a single view**

```bash
ls -lt /home/awank/dev/SuperClaude_Framework/projects/resistance-research/monitoring/*.md \
  | head -5 \
  && echo "---" \
  && cat $(ls -t /home/awank/dev/SuperClaude_Framework/projects/resistance-research/monitoring/*.md | head -1)
```

Lists the 5 most recent monitoring summaries by date and prints the most recent. Use this to quickly review the last tracking script output without opening the directory.

---

## Decision Thresholds — All in One Place

### Engagement Cutoffs (Tree 1 Gate 2 and Gate 3)

| Metric | STRONG | MODERATE | WEAK |
|--------|--------|----------|------|
| Overall reply rate | >= 30% | 15-29% | < 15% |
| Sector engagement rate | >= 30% | 15-29% | < 15% |
| Cumulative Bitly clicks (Day 7) | >= 25 | 10-24 | < 10 |
| Cumulative Bitly clicks (Day 14) | >= 25 | 10-24 | < 10 |
| Engagement velocity | >= 0.5 replies/day | 0.3-0.49 | < 0.3 |

### No-Reply Thresholds (Weak-Signal Detection)

| Band | Engagement Rate | No-Reply Rate | Follow-Up Urgency |
|------|----------------|---------------|-------------------|
| DEFINITE WEAK | <= 8% | >= 85% | 6 hours |
| PROBABLE WEAK | 8-14% | 71-84% | 12 hours |
| POSSIBLE WEAK | 15-19% (or no-reply 60-70%) | 60-70% | 48-hour watch |
| MODERATE | 15-29% | 40-70% | None (standard cadence) |
| STRONG | >= 30% | < 40% | None (Playbook A if Score 4-5) |

### Cross-Sector Trending Triggers

| Signal | Threshold | Action |
|--------|-----------|--------|
| Score 5 (Implementation) | 1 event | Immediate Phase 2 pre-activation (Playbook A) |
| Score 4 (Partnership) | 1 event | Escalate within 24h |
| Score 4 cluster | 2+ in 14 days | Pre-Day-30 STRONG determination |
| Sector rebase success | WEAK → MODERATE in 48h | Remove from follow-up queue |
| Phase 2 velocity trigger | >= 0.5 replies/day for 5 days | Phase 2 Tier 2 activation |
| Cross-sector signal | >= 3 sectors MODERATE or STRONG | Phase 2 Tier 2 activation |
| Network activation | >= 1 confirmed referral | Phase 2 Tier 2 activation |
| Bounce rate | >= 3 bounces | CONTACT_VERIFY — fix emails before analysis |
| Opt-out cluster | >= 2 in 7 days | CHECKIN.md alert — messaging review |

### Sector-Specific Day 7 Red Lines

| Sector | Red Line (DEFINITE WEAK trigger) |
|--------|----------------------------------|
| Law School | > 85% no-reply |
| Immigration Legal | > 75% no-reply (lower threshold — fastest expected sector) |
| Civil Rights | > 80% no-reply |
| Academic | > 90% no-reply (longest expected lag — high threshold) |
| Faith Networks | > 85% no-reply |
| Labor | > 85% no-reply |

### Day 30 Phase 2 Decision Gates (from day-7-14-30-decision-trees.md)

| Determination | Condition |
|---------------|-----------|
| STRONG — launch Phase 2 immediately | Score 3+ rate >= 50% AND 4+ constituencies strong AND 3+ cross-org refs AND 2+ adoptions |
| MODERATE — Domain 39 launches, Domain 56 holds | Score 3+ rate 20-49% OR 3+ constituencies moderate OR 1+ cross-org ref OR 1+ adoption |
| WEAK — 3-modification recovery | Score 3+ rate < 20% AND < 2 constituencies passing AND 0 cross-org refs AND 0 adoptions |
| FAILURE — user decision required | Score 3+ rate < 10% AND 0 cross-org refs AND 0 adoptions AND Week 3-4 clicks = 0 |

---

**Print or bookmark this card. Keep it open during Day 7 checkpoint (June 8, 08:00 UTC).**

**Status**: Production-ready. All thresholds consistent with day-7-14-30-decision-trees.md and PHASE_1_MEASUREMENT_SPREADSHEET_SPEC.md.
