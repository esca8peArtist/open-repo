---
title: "HackerNews Distribution Strategy — Phase 1"
created: 2026-05-06
status: production-ready
path_compatibility: "Path A, Path A+37, Path B — identical HN strategy across all paths"
purpose: "Full HN angle, submission template, comment response playbook, and timing guidance"
---

# HackerNews Distribution Strategy — Phase 1

**Bottom line**: HN is a viable but constrained channel for this framework. Pure political posts
are flagged. The correct framing is methodological, data-structural, and comparative — the
research methodology and civic tooling aspects of this work are genuinely on-topic for HN.
The political advocacy dimension should be absent from the post title and body; the research
and its tools carry the weight.

---

## HN Norms Assessment

**What HN accepts**: Anything that "gratifies intellectual curiosity." This includes:
- Comparative political science methodology
- Civic technology / government data tooling
- Historical movement research and datasets
- Legal research infrastructure and case analysis
- Cryptographic voting systems and verifiable democracy (strong fit — documented in the research)

**What HN flags and downgrades**:
- Explicit political advocacy or partisan framing
- Standard news recycling
- Posts that look like campaigns or organized voting
- Inflammatory or emotionally manipulative language
- Self-promotional content that lacks inherent technical interest

**Assessment for this framework**: The 35-domain research corpus has genuine HN-worthy
dimensions: the data architecture, the comparative analysis methodology, the civic tracker
Python implementation, and the cryptographic democracy research thread. These are the
angles to lead with. The political reform proposals are the context, not the headline.

**Expected outcome**: A well-framed HN post should score 30-150 points. Upvotes in this
range produce 3,000-15,000 unique visitors to the Gist in 48 hours. Top-400 HN posts
regularly drive this. The target is the top 200-400 range — not the front page
(which is extremely competitive and typically requires technical product launches).

**Risk**: HN moderators downrank posts tagged politically. This is mitigated by framing
the submission around the data and methodology, not the conclusions.

---

## Recommended HN Submission Format

### Format: Show HN

"Show HN" is the appropriate format. The research output is a substantive document corpus
hosted on GitHub Gist — that is a thing the user has built and is sharing. "Show HN"
posts are treated as a distinct category, appear on the `/show` listing, and receive some
protection from mass flagging because they represent original work rather than reposts of
news.

Do NOT use plain submission (without "Show HN" prefix) — plain submissions of policy
analysis without a project hook are more likely to be flagged as politically motivated.
The "Show HN" framing signals: "here is something I built," which is the correct frame.

---

## Primary Post Template (Show HN — Methodology Angle)

**Submission title** (choose one — A/B test based on which feels more natural):

Option A:
```
Show HN: 35-domain comparative analysis of U.S. democratic institutions — methodology and data
```

Option B:
```
Show HN: Open research corpus on democratic backsliding — 160 movement case studies, case law analysis
```

Option C (if the civic tracker is mentioned — strongest technical hook):
```
Show HN: Python civic tracker + 35-domain open research corpus on democratic institutions
```

**Submission URL**: Use the Proposal Gist URL:
`https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261`

**Post body** (HN post body text — do NOT repeat title, per HN norms):

```
I've spent 18 months building an open research corpus on U.S. democratic institutions, 
covering 35 domains from judicial independence to war powers to algorithmic decision-making 
in immigration enforcement.

The methodology draws on:

- Chenoweth's 3.5% nonviolent movement threshold research (applied to 160 historical cases 
  spanning 1917–2024)
- V-Dem democratic backsliding indicators as a comparative benchmark
- 640+ primary sources including federal court filings, federal register rules, congressional 
  testimony, and OLC memos
- International benchmarks from functioning democracies (Germany, Canada, UK, Finland, 
  New Zealand) for each reform domain

The output is a 35-domain diagnostic framework — each domain documents: what is broken, 
the evidentiary record, international comparisons, reform proposals, and fiscal estimates. 
Domains include areas like cryptographic voting architecture, algorithmic due process in 
benefits determinations, prosecutorial independence mechanisms, and emergency powers reform.

I also built a Python civic tracker (civic-tracker.py in the repository) that automates 
monitoring of federal regulatory actions, court filings via CourtListener, and congressional 
votes. The tracker data feeds into the research corpus.

The complete corpus is open-licensed (CC BY 4.0) and published as GitHub Gists. The executive 
summary is at [link]. The litigation tracker (250+ cases) is at [link]. The primary 35-domain 
analysis is at the URL above.

Happy to discuss methodology, data sources, or any of the specific domain analyses.
```

**Fill in [link] placeholders before submitting:**
- Executive Summary link: `https://gist.github.com/esca8peArtist/2869da6eaeb15a47246ade3bbbc4a3f4`
- Litigation Tracker link: `https://gist.github.com/esca8peArtist/418d51bda087f15a04d685ab171a5ee0`

---

## Secondary Post Template (Ask HN — Cryptographic Democracy Angle)

This is a separate, distinct submission — do not post both on the same day. Submit this
post 5-7 days after the primary Show HN post (or in a separate session if the first performs
well but the second angle has not been covered).

**Submission format**: Ask HN (text post, no URL required — HN text posts perform well for
genuine questions that invite discussion)

**Submission title**:
```
Ask HN: Cryptographic voting and verifiable democracy — what's the current state of the art?
```

**Post body**:

```
I've been researching election security and democratic institution design for about 18 months, 
including verifiable remote voting systems, threshold signature schemes for election certification, 
and zero-knowledge proofs for voter eligibility verification.

The political science literature on this is pretty well developed (Rivest's RLA work, the 
E2E-V verifiable systems literature, STAR-Vote architecture). I'm less current on the cryptographic 
and engineering implementation side.

What I'm specifically interested in:

1. Current status of end-to-end verifiable (E2E-V) systems in production — which jurisdictions 
   are actually running them?
2. Threshold signature schemes for distributed vote certification — has anyone implemented 
   this outside of research prototypes?
3. The gap between cryptographic security and UX accessibility — the main political criticism 
   of E2E-V systems is that voters can't meaningfully verify without technical knowledge. 
   What are the current best approaches to this?
4. Zero-knowledge proofs for voter eligibility — is this a real deployment path or still 
   theoretical?

Context: I'm writing up the governance architecture dimension of this for a research corpus 
on democratic institution reform. The broader corpus is at [Proposal Gist URL]. Specifically 
the remote voting and digital democracy research is in the corpus but I want to make sure 
I'm current on the cryptographic engineering side.
```

**Expected HN response**: This question sits at the exact intersection of HN's interests —
cryptography, engineering, civics, and democratic systems. It should generate substantive
responses from people working in election technology and applied cryptography. The corpus
link provides context without making the post feel like promotion.

---

## Timing Guidance

| Post | Type | Timing | Day of Week | Time (ET) |
|------|------|---------|-------------|-----------|
| Primary (Show HN methodology) | Show HN | T+3 days from Batch 1 email send | Tuesday or Wednesday | 9:00–11:00 AM |
| Secondary (Ask HN cryptographic voting) | Ask HN | T+10 days | Wednesday or Thursday | 10:00 AM–12:00 PM |

**Why Tuesday/Wednesday morning ET**: HN traffic peaks between 8 AM and 12 PM ET on weekdays.
Posts submitted during this window have maximum exposure in their first 2 hours, which
determines whether they reach the front page or the new queue. Weekend posts perform poorly
for sustained visibility.

**Why T+3 (not T+0)**: Do not post to HN on the same day as institutional emails. The sequence
should be: (1) Batch 1 institutional emails, (2) Substack Post 1, (3) Reddit r/PoliticalScience,
(4) HN Show HN. Each step builds credibility before the next. HN requires the least preparation
but has the highest risk of flagging; let the earlier steps establish the project's existence
before HN sees it.

---

## Comment Response Playbook

HN rewards substantive engagement with comments. For the first 24 hours after submission,
monitor the thread and respond to every substantive comment (not obvious trolling). Template
responses by comment type:

**Comment type: "This is political advocacy, not research"**

Response:
> The methodology is what I'd ask you to evaluate, not the conclusions. The comparative
> framework uses V-Dem indicators and 160 case studies because those are the established
> academic tools for this analysis. If the methodology is sound and the evidentiary record
> is accurate, the conclusions follow. Happy to discuss any specific domain where you think
> the evidence doesn't support the analysis.

**Comment type: "This belongs in r/politics not HN"**

Response:
> Fair point about the political dimension — the reason I posted it here is the methodology
> and tooling. The civic tracker (Python + CourtListener API + APScheduler) is probably the
> most HN-relevant piece. The cryptographic voting architecture research is in Domain [X].
> If either of those is more useful to discuss I'm happy to focus there.

**Comment type: "Your methodology is flawed [specific criticism]"**

Response:
> [Engage directly with the specific criticism. Do not deflect. If the criticism is valid,
> acknowledge it. If it is not, explain why with citations. HN rewards intellectual honesty
> more than defensiveness.]

**Comment type: Substantive question about a specific domain**

Response:
> [Answer the question directly. Provide the relevant section or source. If the question
> exposes a gap in the research, note it. Follow up by linking to the relevant Gist section.]

**Comment type: Genuine interest / "How can I contribute or use this?"**

Response:
> Everything is CC BY 4.0 — use it freely. If you want to engage further, the best way is
> to email [your contact info]. The tracker automation infrastructure is documented if you
> want to build on it.

---

## What Success Looks Like

| Outcome | Definition | Action |
|---------|-----------|--------|
| Strong performance | 80+ points, top 300 on front page | Respond to every comment for 48 hours; note in BATCH_1_CONTACT_LOG.md |
| Moderate performance | 20-79 points, stays on /show page | Respond to substantive comments; good enough outcome |
| Flagged / killed | Points stop accumulating, post disappears from /new | Do not resubmit. Submit secondary (Ask HN cryptographic voting) on a different day. Note that the institutional email + Reddit channels are the primary distribution; HN is supplemental. |
| Front page | 200+ points, front page visibility | This is the high-variance outcome — possible if the methodology angle resonates. Follow up with a Substack post describing the HN discussion while it is live. |

---

## Integration with Deployment Checklist

In `distribution-checklist-template.md`, HN fits between Block 8 (Reddit) and Block 9
(Path A+37 Domain 37 emails). It is not a separate block — it is a scheduled action:

- **Block 8 (Reddit prep)**: Add a line — "Also: stage HN Show HN post using HN_STRATEGY.md template"
- **Calendar reminder** (Block 11): Set for T+3 for HN submission
- **Block 11 (Monitoring)**: Add HN comment monitoring to the daily check

---

## Platform Formatting Constraints for HN

HN uses extremely minimal markup. Understanding this prevents formatting errors:

| Element | HN behavior |
|---------|-------------|
| Markdown headers (##) | Not rendered — display as literal # symbols |
| Bold (**text**) | Not rendered — display as literal asterisks |
| Bullet lists | Rendered if lines start with `*` or `-` followed by space |
| Numbered lists | Rendered correctly (1. 2. 3.) |
| URLs | Displayed as plain text unless used as submission URL |
| Code blocks | Rendered with indent (4 spaces) |
| Italics | Not rendered — display as literal asterisks |

**Implication**: Write the post body as plain prose with numbered lists where structure is
needed. Do not use Markdown headers or bold. The templates above conform to these constraints.

---

*Created May 6, 2026. Companion: `distribution-checklist-template.md` (execution),*
*`PHASE1_EXECUTION_MATERIALS/REDDIT_OUTREACH_THREADS.md` (Reddit strategy).*
