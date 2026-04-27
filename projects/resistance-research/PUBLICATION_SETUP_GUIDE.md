---
title: "Phase 1 Publication Setup Guide"
created: 2026-04-28
status: pre-launch-ready
purpose: "Accelerate document publication infrastructure setup upon user path decision"
---

# Phase 1 Publication Setup Guide

**Session 554, 2026-04-28**

When user selects distribution path (A / A+37 / B), this guide automates the publication setup to move from decision to first email send within 5 hours.

---

## Option 1: GitHub Repository (RECOMMENDED)

**Rationale**: Permanent, citeable, version-controlled, professional, enables ongoing updates without republishing

### Setup Steps (15 minutes)

1. **Create public repository**: `esca8peArtist/democratic-renewal-framework`
   ```bash
   gh repo create democratic-renewal-framework \
     --public \
     --description="Comprehensive diagnostic framework for democratic renewal: 35 policy domains, institutional reform pathways, and implementation architecture" \
     --homepage="https://github.com/esca8peArtist/democratic-renewal-framework"
   ```

2. **Clone and initialize**:
   ```bash
   cd ~/github
   git clone git@github.com:esca8peArtist/democratic-renewal-framework.git
   cd democratic-renewal-framework
   touch README.md
   ```

3. **Create folder structure**:
   ```
   democratic-renewal-framework/
   ├── README.md                           # Landing page
   ├── EXECUTIVE_SUMMARY_2PAGE.md          # 2-page summary
   ├── EXECUTIVE_SUMMARY_8PAGE.md          # 8-page summary
   ├── FULL_FRAMEWORK_35DOMAINS.md         # Complete document
   ├── ACTIVATION_ARCHITECTURE.md          # Implementation roadmap
   ├── domains/                            # Individual domain files
   │   ├── domain-01-voting-rights.md
   │   ├── domain-02-executive-power.md
   │   ├── ... (all 35 base domains)
   │   ├── domain-36-ai-governance.md
   │   └── domain-37-federal-election-2026.md (Path A+37 only)
   ├── APRIL_2026_UPDATES.md               # April content updates summary
   ├── litigation-tracker.md                # Current litigation status
   └── contact-batches/                    # Distribution metadata (private)
       └── README.md                       # "Contact distribution — not public"
   ```

4. **Copy documents** (1 hour, can parallelize):
   ```bash
   cp /home/awank/dev/SuperClaude_Framework/projects/resistance-research/domains/*.md ./domains/
   cp /home/awank/dev/SuperClaude_Framework/projects/resistance-research/ACTIVATION_ARCHITECTURE.md ./
   cp /home/awank/dev/SuperClaude_Framework/projects/resistance-research/litigation-tracker.md ./
   # Create executive summaries from existing docs
   ```

5. **Create README.md** (landing page):
   ```markdown
   # Democratic Renewal: A 35-Domain Diagnostic Framework
   
   **Status**: April 2026 | **Scope**: Complete | **Citation-Ready**: Yes
   
   This repository contains a comprehensive diagnostic of 35 policy domains across U.S. government 
   structure, function, and reform. Each domain includes:
   - Current institutional failure analysis
   - International comparative precedent (40+ democracies)
   - Litigation and legislative reform pathways
   - Implementation timeline and feasibility assessment
   
   ## Quick Links
   - [Executive Summary (2-page)](/EXECUTIVE_SUMMARY_2PAGE.md) — High-level overview
   - [Executive Summary (8-page)](/EXECUTIVE_SUMMARY_8PAGE.md) — Domain-by-domain summary
   - [Full Framework (35 domains)](/FULL_FRAMEWORK_35DOMAINS.md) — Complete analysis
   - [Activation Architecture](/ACTIVATION_ARCHITECTURE.md) — Implementation roadmap
   - [Domain Listing](/domains/) — Individual domain files
   - [April 2026 Updates](/APRIL_2026_UPDATES.md) — Latest legislative/judicial developments
   - [Litigation Tracker](/litigation-tracker.md) — Active reform litigation
   
   ## For Researchers, Advocates, and Practitioners
   - **Domain-specific outreach**: Each domain is individually actionable. Extract the 2-3 domains most relevant to your work.
   - **Academic use**: All domains cite primary sources, international precedent, and academic literature.
   - **Practitioner implementation**: See Activation Architecture for sector-specific playbooks and sequencing.
   
   ## Citing This Framework
   ```bibtex
   @online{democratic-renewal-2026,
     title = {Democratic Renewal: A 35-Domain Diagnostic Framework},
     author = {Wanka, Anya},
     year = {2026},
     month = {04},
     url = {https://github.com/esca8peArtist/democratic-renewal-framework},
     note = {Comprehensive institutional reform analysis, April 2026}
   }
   ```
   
   ---
   
   ## Framework Domains
   
   [Auto-generated table of all 35 domains with 1-line descriptions]
   
   ---
   
   ## Contact & Questions
   For questions, academic collaboration, or implementation partnership inquiries, 
   see [Institutional Adoption Playbooks](/institutional-adoption-playbooks.md).
   ```

6. **Push to GitHub**:
   ```bash
   git add .
   git commit -m "docs: democratic renewal framework — 35-domain diagnostic"
   git push -u origin main
   ```

7. **Verify public access**:
   ```bash
   open https://github.com/esca8peArtist/democratic-renewal-framework
   ```

**Permanent links generated**:
- `https://github.com/esca8peArtist/democratic-renewal-framework` — repo root
- `https://github.com/esca8peArtist/democratic-renewal-framework/blob/main/EXECUTIVE_SUMMARY_2PAGE.md` — 2-page
- `https://github.com/esca8peArtist/democratic-renewal-framework/blob/main/domains/` — domain directory
- `https://github.com/esca8peArtist/democratic-renewal-framework/blob/main/ACTIVATION_ARCHITECTURE.md` — roadmap

---

## Option 2: Substack Newsletter (FOR AUDIENCE BUILDING)

**Rationale**: Public-facing publication channel, email subscriber tracking, community engagement

### Setup Steps (30 minutes)

1. **Create Substack publication**:
   - Go to substack.com/new
   - Publication name: "Democratic Renewal" (or personalized: "Anya's Democratic Renewal")
   - Tagline: "Institutional reform for democratic stability"
   - Description: "A 35-domain diagnostic framework for democratic renewal, with policy solutions, international precedent, and implementation pathways."

2. **Configure settings**:
   - Visibility: Public
   - Email domain: use Substack's default or custom (anya@newsletter.democratic-renewal.org — requires domain)
   - Recommendation: Start with Substack domain, upgrade if needed

3. **Prepare first post** (scheduled for T+3 days):
   ```markdown
   # Democratic Renewal: A Comprehensive 35-Domain Framework
   
   [Substack-optimized version of executive summary — 2,000–3,000 words]
   
   [Link to GitHub repository]
   [Call-to-action: Subscribe for weekly updates]
   ```

4. **Schedule for T+3 days** (don't publish immediately):
   - Rationale: Allow Batch 1 institutional contacts to engage before public launch
   - This preserves the "institutional adoption first" framing

5. **Optional: Set up weekly update cadence**:
   - Sunday update: Week's legislative/judicial changes affecting framework
   - Maintains audience engagement and framework currency

**Permanent links generated**:
- `https://democratic-renewal.substack.com` — publication root
- `https://democratic-renewal.substack.com/p/[slug]` — individual posts

---

## Option 3: Dedicated Website (PROFESSIONAL/LONG-TERM)

**Rationale**: Professional presentation, custom domain, analytics, long-term institutional presence

### Setup (NOT recommended for T-Day 0 execution, suitable for T+2-4 weeks)

Tools: Jekyll (GitHub Pages), Hugo, Webflow, or Squarespace

Setup time: 3-6 hours

Not recommended for immediate Phase 1 launch — suggest GitHub + Substack instead.

---

## Option 4: Direct Document Distribution (FASTEST FOR T-DAY 0)

**Rationale**: Minimal setup, maximum speed, doesn't require GitHub/publishing infrastructure

### Setup Steps (5 minutes)

1. **Create contact-specific PDFs**:
   ```bash
   # Using existing Markdown files, convert to PDF for email attachment
   pandoc domains/domain-01-voting-rights.md -o domain-01-voting-rights.pdf
   ```

2. **Attach to outreach emails**:
   - Batch 1 emails include domain PDFs as attachments
   - Include GitHub/Substack links for full framework access

3. **Permanent storage**:
   - Documents remain in `projects/resistance-research/` locally
   - GitHub repo created separately for public access (non-blocking for T-Day 0)

**Advantage**: Zero setup required, can send within hours of decision
**Disadvantage**: Less professional, harder to track who has what version, no public link for media/advocates

---

## Recommended Strategy: GitHub + Substack (HYBRID)

**T-Day 0 (Decision Day)**:
- ✅ GitHub repo created with documents (1 hour)
- ✅ Batch 1 emails sent with GitHub links (immediate, within 4 hours of decision)
- ✅ Substack post drafted (within 2 hours)

**T+3 days (Social Media Launch)**:
- Substack post published (only after institutional response or 72-hour delay)
- Reddit posts queued (domain-specific to subreddits)
- X/Bluesky thread posted (with GitHub and Substack links)

**Permanent architecture**:
- GitHub: Official, citeable, permanent repository
- Substack: Public audience building, weekly updates, subscriber engagement
- Email: Direct institutional outreach (Batch 1-3 over 28 days)
- Reddit: Community discussion and engagement
- Social: Media amplification and awareness

---

## Pre-Decision: What You Can Do Now (Without User Decision)

**Option**: Create the GitHub repository structure NOW, empty, ready for documents

```bash
cd ~/github
git clone git@github.com:esca8peArtist/democratic-renewal-framework.git
cd democratic-renewal-framework

# Create folders and placeholder files
mkdir -p domains contact-batches
touch README.md EXECUTIVE_SUMMARY_2PAGE.md EXECUTIVE_SUMMARY_8PAGE.md

# Create .gitignore
echo "contact-batches/*" >> .gitignore
echo "!contact-batches/README.md" >> .gitignore

# Initial commit
git add .
git commit -m "docs: initialize democratic renewal framework repository structure"
git push -u origin main
```

**Benefit**: Repository is live and shareable immediately upon decision, no additional setup needed

---

## Checklist for T-Day 0 Execution

### If GitHub + Substack Hybrid Chosen

- [ ] **Hour 0**: Confirm user decision (Path A / A+37 / B)
- [ ] **Hour 0**: Copy documents to GitHub repo, push to main
- [ ] **Hour 1**: Verify GitHub links work
- [ ] **Hour 2**: Create Substack publication, draft first post (scheduled for T+3)
- [ ] **Hour 3**: Verify contact emails, personalize Batch 1 templates
- [ ] **Hour 4**: Send Batch 1 emails (with GitHub links)
- [ ] **Hour 4**: Post X/Bluesky announcement with GitHub and "Substack coming T+3 days" note

**Time to Phase 1 launch**: 4 hours from user decision

### If Direct Distribution Chosen (Fastest)

- [ ] **Hour 0**: Confirm user decision
- [ ] **Hour 1**: Verify contact emails, personalize templates
- [ ] **Hour 2**: Send Batch 1 emails (with domain document attachments)
- [ ] **Optional Hour 3**: Create GitHub repo for future public access

**Time to Phase 1 launch**: 2 hours from user decision

---

## Integration with Distribution Sequence

See `/execution/distribution-sequence.md` for full T-Day 0 through T+28 day timeline.

Publishing setup is the pre-launch prerequisite; once complete, distribution sequence executes automatically per the documented schedule.

---

**Status**: Ready for immediate execution upon user path decision.
