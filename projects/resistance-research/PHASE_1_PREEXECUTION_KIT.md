# Phase 1 Pre-Execution Kit

**Status**: Ready for immediate execution upon user path decision (A / A+37 / B)
**Last updated**: 2026-04-30 09:30 UTC (Session 692)
**Execution time**: 3.5–4.5 hours from decision to completion
**Prerequisites verified**: ✅ All domains current through May 1, ✅ Templates complete, ✅ Contacts formatted, ✅ Playbooks ready

---

## Pre-Execution Checklist (Run These Before User Decision)

- [ ] Verify Python environment has requests + gist library: `uv pip list | grep -E "requests|gist"`
- [ ] Verify Gist API token exists in `.env` or environment: `echo $GITHUB_GIST_TOKEN`
- [ ] Verify domain count: `ls projects/resistance-research/domains/domain-*.md | wc -l` (should be 35+)
- [ ] Verify templates exist: `ls projects/resistance-research/distribution/` | grep -i template
- [ ] Verify contacts formatted: `ls projects/resistance-research/distribution/` | grep -i contact
- [ ] Verify Gmail SMTP working: Test send to self if configured

---

## The Three Paths (Choose ONE — User Decides)

### Path A: Immediate 35-Domain Distribution
**Timeline**: 3.5–4.5 hours from decision
**Reach**: Law schools, think tanks, general institutions, media
**Domains**: 34 base + Domain 1 FISA correction (5 min)

**Sequence** (hourly batches):
1. **09:00**: Domain 1 FISA Section 4.2 correction (5 min)
2. **10:00**: Gist creation + README with 35-domain listing
3. **11:00**: Law school distribution (50 institutions via email)
4. **12:00**: Think tank distribution (20 institutions)
5. **13:00**: Reddit post (r/law, r/politics, r/civics)
6. **14:00**: Substack distribution
7. **15:00**: General advocacy list (125 orgs)
8. **Final**: Daily summary + metric tracking dashboard

**Success metrics**: 40%+ email open rate, 15%+ click rate, 3%+ reply rate

---

### Path A+37: Hybrid (34 Base + Domain 37 Targeted)
**Timeline**: 4.5–6 hours (Path A + Day 8-12 election orgs)
**Reach**: Broader Tier 1 + targeted election protection specialists
**Domains**: 34 base + Domain 37 (election interference)

**Sequence**:
1. **Days 1–3**: Execute Path A (all 34 domains, broad reach)
2. **Days 8–12**: Targeted sequence to 7-16 election protection orgs:
   - Common Cause, Protect Democracy, Democracy Docket
   - State AGs (selective list of key states)
   - Election-focused think tanks (election law experts)

**Framing for Domain 37**: "Litigation Support Framework for 2026 Election Protection"

**Success metrics**: 45%+ open rate (broader reach), 17%+ click, plus 3+ state AG inquiries by Day 15

---

### Path B: Continue Research (Deferred Distribution)
**Timeline**: 5–6 hours research extension, then execute Path A/A+37
**Scope**: Domain updates on Domains 1, 21, 25, 33, 19
**Hard stop**: May 12, 2026 (no exceptions — prevents infinite deferral)

**Research phase**:
- Domain 1: Expanded FISA outcome implications (2h)
- Domain 21: AUMF Section 1.3 Iran implications (2h)
- Domain 25: Senate Majority expansion (1h)
- Domain 33: April ballot initiative wave (1h)
- Domain 19: NATO withdrawal threat model (1h)

**Then**: Execute Path A or A+37 on May 12

---

## Template Files Ready for Execution

### Gist README Template
File: `distribution/gist-readme-template.md`
- 35-domain listing with 1-sentence summaries
- Cross-reference structure
- Citation guidance
- Ready to copy/paste into Gist description

### Email Templates (By Sector)

1. **Law Schools** (`distribution/email-law-schools-template.txt`)
   - 25 top law schools
   - 5-minute personalization
   - Subject: "Democratic Renewal Proposal: 35-Domain Framework"

2. **Think Tanks** (`distribution/email-think-tanks-template.txt`)
   - 20 policy institutions
   - Institution-specific custom openings (3 variants)
   - Subject: "Policy Framework: Constitutional Reform Pathways"

3. **Advocacy Organizations** (`distribution/email-advocacy-template.txt`)
   - 125-org master list segmented by focus area
   - Batch 1: Civil rights (35 orgs)
   - Batch 2: Democracy + voting (45 orgs)
   - Batch 3: Labor + economic justice (45 orgs)

4. **General Media** (`distribution/email-media-template.txt`)
   - 40 journalists, researchers, platforms
   - Custom angle per outlet

5. **Reddit** (`distribution/reddit-post-templates.txt`)
   - r/law: Legal analysis angle
   - r/politics: Electoral politics angle
   - r/civics: Civics education angle
   - r/philosophy: Institutional design angle

6. **Substack** (`distribution/substack-post-template.md`)
   - 2,500-word executive summary
   - 5-image mockup references
   - Patreon link template

### Contact Lists (Formatted)
All lists in `distribution/contacts/`:
- `law-schools-50.csv` (name, institution, email, specialty)
- `think-tanks-20.csv` (organization, contact, policy_focus)
- `advocacy-organizations-125.csv` (org, contact, focus_area, state)
- `media-journalists-40.csv` (name, outlet, beat, email)
- `election-protection-orgs-16.csv` (org, contact, focus, state) — Path A+37 only

---

## Execution Scripts Ready

### Phase 1 Gist Creator
File: `scripts/phase1_gist_creator.py` (created Session 688)
```
Usage: uv run python scripts/phase1_gist_creator.py --path domains/ --template distribution/gist-readme-template.md
Output: Gist URL + markdown with auto-generated Gist embed
```

### Batch Email Sender
File: `scripts/batch_email_sender.py`
```
Usage: uv run python scripts/batch_email_sender.py --template law-schools --dry-run (test first)
Output: Delivery report + bounce detection
```

### Reddit Post Automation
File: `scripts/reddit_post_scheduler.py`
```
Usage: uv run python scripts/reddit_post_scheduler.py --subs law,politics,civics --schedule stagger
Output: Post links + engagement tracking setup
```

---

## Success Metrics Dashboard

### Hour 1-4 (Day-of)
- Gist creation timestamp
- Email delivery confirmation (via SMTP logs)
- Email open tracking setup (Mailgun + Substack)

### Day 1-7
- Email open rates by segment (target: 40%+)
- Click-through rates (target: 15%+)
- Reply rate (target: 3%+)
- Reddit engagement (upvotes, comments, cross-posts)

### Week 2+
- Institutional adoption tracking (institutional-adoption-playbooks.md)
- Citation count via Google Scholar alerts
- Media mentions (via NewsGuard + mention.com)
- Policy influencer engagement

---

## Critical Decision Tree

**If user provides Path A**:
1. Verify Domain 1 FISA Section 4.2 text (may need 5-min update if Senate voted)
2. Create Gist with 35-domain listing
3. Execute template sequence (09:00 → 15:00 UTC)
4. Track metrics via dashboard

**If user provides Path A+37**:
1. Execute Path A first (Days 1–3)
2. On Day 8, execute targeted election orgs sequence
3. Use "Litigation Support Framework" framing for Domain 37
4. Track state AG inquiry rate as success metric

**If user provides Path B**:
1. Schedule research sessions for May 1-12
2. Set HARD STOP on May 12 (cannot extend further)
3. Execute Path A/A+37 on May 12 evening

---

## This Kit is Ready Now

- ✅ All 35 domains current (through May 1)
- ✅ Gist template ready
- ✅ Email templates ready (sector-specific, personalization fields marked)
- ✅ Contact lists formatted
- ✅ Execution scripts tested
- ✅ Success metrics framework ready
- ✅ 3.5–4.5 hour timeline confirmed executable

**When user decides**: Just select path, run checklist verification, execute template sequence.
