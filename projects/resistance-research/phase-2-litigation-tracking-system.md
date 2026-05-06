---
title: Phase 2 Litigation Tracking & Attribution System Design
project: resistance-research
created: 2026-05-06
status: ready-for-implementation
confidence: high — based on post-distribution-adoption-framework.md + institutional-adoption-playbooks.md
related: post-distribution-adoption-framework.md, institutional-adoption-playbooks.md, phase-1-baseline-metrics.md
---

# Phase 2 Litigation Tracking & Attribution System

**Status**: Pre-distribution research and system design. Ready for implementation on **Day 1 of Phase 1 launch**.

**Business purpose**: Enable quantitative measurement of resistance-research framework's institutional adoption and impact. Track litigation, policy changes, and framework citation to support Phase 1→Phase 2 transition decisions.

**Key success metric**: Post-distribution adoption gradient (Day 0 → 30 → 90 → 180 days) with sector-specific leading indicators.

---

## Executive Summary

Once the resistance-research 35-domain framework is distributed to 150+ institutional contacts (Phase 1, awaiting user distribution path decision), three classes of impact need quantification:

1. **Litigation impact** — Tracking active cases where framework was cited or adopted in briefs
2. **Institutional adoption** — Vocabulary migration, framework integration into organizational work
3. **Framework attribution** — Distinguishing framework influence from coincidental parallel work

This document specifies the **monitoring infrastructure, data sources, analysis procedures, and decision frameworks** for Phase 2 (post-distribution measurement and Phase 2 trigger decisions).

**Implementation timeline**: Design complete (this document). Deploy on Day 1 of Phase 1 launch. Monitoring window: 6 months (Day 1–180).

---

## Part 1: Data Sources & Collection Infrastructure

### Litigation Data Sources

**Primary source: PACER (Public Access to Court Electronic Records)**
- **URL**: pacer.uscourts.gov
- **Coverage**: Federal courts (district + appellate)
- **Search strategy**: Query per domain topic
- **Lead time**: Filing appears in PACER 1–3 days after filing
- **Implementation**: Automated queries via Python requests + BeautifulSoup, daily 09:00 UTC (prior to market open)

**Query examples by domain**:
- Domain 2 (presidential removal power): Search `Trump v.` + `Wilcox` + `removal power`
- Domain 6 (executive office operations): Search `DOGE` OR `efficiency commission` + `executive branch`
- Domain 25 (surveillance): Search `FISA` + `702` + `warrant`
- Domain 29 (prosecutorial weaponization): Search `DOJ` + `election interference`

**Secondary source: Google Scholar Alerts**
- **URL**: scholar.google.com/scholar_alerts
- **Coverage**: All case citations (state + federal)
- **Advantage**: Catches state-court cases before PACER indexing
- **Implementation**: Automated email parsing + keyword extraction
- **Domains monitored**: 10–15 highest-impact domains (prioritize based on Phase 1 feedback)

**Tertiary source: Legal opinion aggregators**
- **Tools**: 
  - Justia (justia.com) — aggregates federal + state + administrative decisions
  - Google Scholar direct API (scholar.nih.gov) — if institutional access available
  - LexisNexis API (if institutional subscription available via library)
- **Coverage**: Delayed 2–4 weeks vs. PACER, but more comprehensive
- **Implementation**: Weekly batch queries, Thursday evening

### Institutional Adoption Data Sources

**Primary source: Email reply tracking**
- **Method**: Bcc monitoring address on all Phase 1 distribution emails
- **Data**: Reply volume, sender organization, keyword extraction (framework mention, domain reference)
- **Timeline**: Collect Day 1–14, Day 15–30, Day 31–90, Day 91–180
- **Implementation**: Gmail filter + Python mail parsing

**Secondary source: Citation tracking**
- **Google Scholar Alerts**: Set alert for "35-domain framework" OR "resistance-research" phrase
- **Web search**: Weekly Google News search for framework name + key domain names
- **Implementation**: Automated daily query, archive results in SQLite database

**Tertiary source: Organizational websites**
- **Organizations to monitor**: 
  - State attorney general offices (ag.ny.gov, ag.ca.gov, etc.)
  - Civil rights organizations (ACLU, LDF, Brennan Center, Protect Democracy)
  - Law schools (sample: Harvard Law, Yale Law, Berkeley Law)
  - Think tanks (Brookings, AEI, Wilson Center, CAP)
- **Method**: Monthly snapshot of web pages, keyword search for framework vocabulary
- **Implementation**: Weekly scraping via Selenium, keyword search in database

### Attribution Data Collection

**Evidence of framework impact vs. coincidence**:
1. **Vocabulary marker** — Institutional document uses framework's specific terminology (e.g., "35-domain", "institutional playbooks", domain-specific naming)
2. **Structural convergence** — Document adopts framework's organizational structure (5-layer proposal, 6-month implementation roadmap, etc.)
3. **Timing-and-contact test** — Document published within 30 days of Phase 1 distribution to that institution
4. **Counterfactual baseline** — Compare post-distribution adoption rate to pre-distribution baseline (0 mentions) and parallel adoption trend (if framework hadn't been distributed)

---

## Part 2: Database Schema & Tracking Infrastructure

### SQLite Schema

```sql
-- Cases table
CREATE TABLE litigation_cases (
    id INTEGER PRIMARY KEY,
    case_name TEXT NOT NULL,
    court TEXT,  -- "District Court", "Circuit Court", "SCOTUS"
    state TEXT,
    filing_date DATE,
    first_framework_mention_date DATE,
    domain_referenced TEXT,  -- "Domain 2", "Domain 6", etc.
    brief_type TEXT,  -- "plaintiff", "defendant", "amicus"
    brief_excerpt TEXT,
    pacer_link TEXT,
    google_scholar_link TEXT,
    analysis_status TEXT,  -- "confirmed", "unrelated", "investigation"
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Institutional adoption table
CREATE TABLE institutional_adoption (
    id INTEGER PRIMARY KEY,
    institution_name TEXT,
    institution_type TEXT,  -- "state_ag", "law_school", "think_tank", "civil_rights_org", "union"
    contact_email TEXT,
    phase_1_email_sent_date DATE,
    email_reply_received_date DATE,
    reply_excerpt TEXT,
    framework_vocabulary_score FLOAT,  -- 0.0–1.0 (0 = no evidence, 1 = strong vocabulary adoption)
    structural_adoption_score FLOAT,
    timing_score FLOAT,  -- 1.0 if within 30 days, 0.5 if 30–90 days, 0 if >90 days
    overall_adoption_confidence FLOAT,  -- 0.0–1.0
    domain_specific_requests TEXT,  -- Domains they asked about or emphasized
    follow_up_action TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Citation tracking table
CREATE TABLE citations (
    id INTEGER PRIMARY KEY,
    source_organization TEXT,
    document_title TEXT,
    document_date DATE,
    framework_mention TEXT,  -- Quoted text from document
    domain_referenced TEXT,
    url TEXT,
    collection_method TEXT,  -- "google_scholar", "web_scrape", "email_reply"
    confidence_score FLOAT,  -- 0.0–1.0 (confidence it's really framework adoption)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Attribution scoring table
CREATE TABLE attribution_analysis (
    id INTEGER PRIMARY KEY,
    case_id OR institution_id,
    vocabulary_evidence TEXT,  -- Specific phrases from document
    structural_evidence TEXT,
    timing_calculation TEXT,  -- Days since distribution
    counterfactual_baseline TEXT,  -- Pre-distribution baseline for comparison
    attribution_probability FLOAT,  -- 0.0–1.0 estimated P(framework caused this | observed evidence)
    confidence TEXT,  -- "high", "medium", "low"
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Python Monitoring Script

```python
# monitoring/phase2_tracker.py

import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)

class Phase2Tracker:
    def __init__(self, db_path="phase2_data.db"):
        self.db = sqlite3.connect(db_path)
        self.cursor = self.db.cursor()
        self.framework_keywords = [
            "35-domain framework",
            "resistance-research",
            "institutional playbooks",
        ]
    
    def search_pacer(self, domain_keywords):
        """Query PACER for domain-relevant litigation"""
        base_url = "https://www.pacer.gov/cgi-bin/casequery.pl"
        
        for keyword in domain_keywords:
            try:
                response = requests.get(base_url, params={
                    "query": keyword,
                    "action": "runquery"
                })
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Parse results, extract case name, date, link
                for case_row in soup.find_all('tr')[1:]:
                    case_data = case_row.find_all('td')
                    case_name = case_data[0].text
                    filing_date = case_data[1].text
                    court = case_data[2].text
                    
                    # Store in database
                    self.cursor.execute("""
                        INSERT INTO litigation_cases (case_name, court, filing_date, domain_referenced)
                        VALUES (?, ?, ?, ?)
                    """, (case_name, court, filing_date, keyword))
                
                self.db.commit()
                logger.info(f"Indexed {len(soup.find_all('tr'))} cases for keyword: {keyword}")
            
            except Exception as e:
                logger.error(f"PACER query failed for {keyword}: {e}")
    
    def analyze_vocabulary_adoption(self, institution_id):
        """Score institutional adoption based on vocabulary migration"""
        # Query institution email reply
        reply = self.cursor.execute(
            "SELECT reply_excerpt FROM institutional_adoption WHERE id = ?",
            (institution_id,)
        ).fetchone()
        
        if not reply:
            return 0.0
        
        # Score vocabulary adoption (simple keyword matching, can be enhanced)
        score = 0.0
        for keyword in self.framework_keywords:
            if keyword.lower() in reply[0].lower():
                score += 0.25
        
        return min(score, 1.0)
    
    def generate_daily_report(self):
        """Generate daily monitoring report"""
        print(f"\n=== Phase 2 Tracking Report ({datetime.now().isoformat()}) ===\n")
        
        # Litigation count
        litigation = self.cursor.execute(
            "SELECT COUNT(*) FROM litigation_cases WHERE first_framework_mention_date >= DATE('now', '-1 day')"
        ).fetchone()[0]
        print(f"New litigation cases (last 24h): {litigation}")
        
        # Institutional adoption count
        adoption = self.cursor.execute(
            "SELECT COUNT(*) FROM institutional_adoption WHERE email_reply_received_date >= DATE('now', '-1 day')"
        ).fetchone()[0]
        print(f"Institutional replies (last 24h): {adoption}")
        
        # High-confidence citations
        citations = self.cursor.execute(
            "SELECT COUNT(*) FROM citations WHERE confidence_score > 0.75 AND created_at >= DATE('now', '-1 day')"
        ).fetchone()[0]
        print(f"High-confidence citations (last 24h): {citations}")

# Run daily
if __name__ == "__main__":
    tracker = Phase2Tracker()
    tracker.search_pacer(["presidential removal", "FISA warrant", "prosecutorial weaponization"])
    tracker.generate_daily_report()
```

---

## Part 3: Measurement Timeline & Milestones

### Day 0 (Phase 1 Launch)

**Initialization**:
- [ ] Deploy SQLite database (`phase2_data.db`)
- [ ] Configure Google Scholar Alerts (10–15 priority domains)
- [ ] Set up Gmail reply monitoring (Bcc tracking address)
- [ ] Schedule daily PACER queries (09:00 UTC)
- [ ] Create initial baseline: pre-distribution litigation count + institutional awareness

**Baseline metrics**:
- Litigation cases citing framework-relevant topics (control group): e.g., 10–15 FISA cases filed per week nationally
- Institutional vocabulary baseline: 0 mentions of "35-domain framework" on state AG websites
- Citation baseline: 0 mentions in Google Scholar

### Day 1–7 (Early adoption window)

**Metrics to track**:
- Email reply rate (expected: 15–25% Day 1-7, assuming ~25 of 150 early adopters)
- Vocabulary adoption (expected: 3–5 reply emails mention framework by name)
- Domain-specific requests (track which domains are triggering follow-up)
- Litigation filing acceleration (looking for correlation between distribution and filing increase)

**Daily check**: PACER query, Google Scholar Alerts, email parsing

**Decision gate (Day 7)**: Is reply rate tracking toward 40% open rate? If <20%, investigate delivery issues.

### Day 8–30 (Active adoption window)

**Metrics to track**:
- Cumulative email reply rate (target: 40–50% by Day 30)
- Vocabulary adoption gradient (% of replies mentioning framework by name)
- Institutional website vocabulary (scrape websites, look for framework terminology)
- Litigation trend (Is filing rate accelerating among contacted organizations' focus areas?)

**Analysis**:
- Attribution scoring: For each positive signal, score vocabulary + structural + timing evidence
- Baseline comparison: Is adoption rate outpacing control group?

**Decision gate (Day 30)**: Assess Phase 2 readiness
- **Go**: ≥40% reply rate + ≥8 high-confidence vocabul adoption signals → Proceed to Phase 2 design
- **Investigate**: 20–40% reply rate → Analyze why replies are low; contact sample for feedback
- **Abort or adjust**: <20% reply rate → Distribution may have failed; consider Path B re-activation

### Day 31–90 (Substantive adoption window)

**Metrics to track**:
- Domain-specific requests (Which domains are getting follow-up questions? Which are adopted into institutional work?)
- Litigation trend analysis (Correlation between domain citation and litigation filings 7–14 days later)
- Vocabulary migration (Is framework terminology appearing in new institutional documents?)
- Sector-specific adoption (Which sectors fastest to adopt? State AGs vs. law schools vs. think tanks?)

**Analysis**:
- Time-lag analysis: Measure days from Phase 1 email → institutional action (litigation filing, vocabulary adoption)
- Counterfactual: Estimate P(action | framework influence) using Bayesian framework

**Decision gate (Day 90)**: Phase 2 candidate selection
- **High-adoption domains** (≥3 independent institutional citations): Priority for Phase 2 expansion
- **Low-adoption domains** (<1 citation): Deprioritize or revise for Phase 2
- **New demand signals**: Unsolicited requests for new domains or cross-domain frameworks

### Day 91–180 (Long-tail adoption window)

**Metrics to track**:
- Cumulative adoption gradient (Plot adoption rate over time to identify S-curve phase)
- Litigation correlation (Six-month lookback: litigation trend vs. distribution timing)
- Policy impact (Did any Phase 1 domains trigger policy changes, state bills, executive orders?)
- Attribution strength (High-confidence vs. medium-confidence vs. low-confidence attribution signals)

**Analysis**:
- Rogers S-curve positioning: Is Phase 1 framework reaching "early majority" (15–50% adoption) or still in "early adopter" (2–15%)?
- Phase 2 ROI projection: Based on 180-day adoption rate, project Phase 2 demand and resource allocation

**Final decision gate (Day 180)**: Phase 2 launch readiness
- **Ready**: S-curve shows 20–40% adoption gradient, high-confidence signals > 20, policy impact emerging → Full Phase 2 launch
- **Deferred**: S-curve flat or slow, low-confidence signals → Extend monitoring, refine messaging, relaunch Phase 2 on Month 7+
- **Complete**: S-curve reaches equilibrium (adoption plateau), framework integrated into institutional baseline → Phase 2 is new baseline for Phase 3

---

## Part 4: Attribution Scoring Methodology

### Four-Test Attribution Framework

When a positive signal emerges (litigation citation, institutional adoption), score using these four tests:

**Test 1: Vocabulary Marker** (0.0–0.4 points)
- **Score 0.4**: Document uses framework's specific phrase or domain name
  - Example: "As outlined in the 35-domain framework, Domain 6 addresses..."
  - Example: "Following the institutional playbooks model..."
- **Score 0.2**: Document uses framework's distinctive vocabulary but without explicit attribution
  - Example: "A comprehensive approach to institutional reform across 35 policy domains..."
- **Score 0.0**: No vocabulary overlap

**Test 2: Structural Convergence** (0.0–0.3 points)
- **Score 0.3**: Document adopts framework's structure (5-layer proposal, 6-month implementation timeline, institutional playbooks format)
  - Example: Litigation brief organizes arguments around institutional playbooks structure
- **Score 0.15**: Document shows partial structural convergence
  - Example: Uses 5-layer analysis but doesn't explicitly reference framework
- **Score 0.0**: Different structure

**Test 3: Timing-and-Contact Test** (0.0–0.2 points)
- **Score 0.2**: Document dated within 30 days of Phase 1 distribution AND organization was Phase 1 recipient
  - Example: State AG office receives framework June 1, publishes brief using framework July 15 (Day 44 post-distribution, still warm)
- **Score 0.1**: Document dated 30–90 days post-distribution (adoption possible but not certain)
  - Example: Brief published 60 days after distribution — could be influence, could be coincidence
- **Score 0.0**: Document predates distribution or organization was not contacted in Phase 1

**Test 4: Counterfactual Baseline** (0.0–0.1 points)
- **Score 0.1**: Document exhibits novelty uncommon in pre-distribution baseline
  - Example: State AG publishing 35-domain analysis pre-distribution = 0 instances; post-distribution = 3 instances in 90 days
  - Inference: P(increase | framework influence) > P(increase | random variation)
- **Score 0.0**: Document exhibits common pre-distribution pattern
  - Example: Litigation arguments about FISA section 702 were common pre-distribution; post-distribution frequency unchanged

**Attribution Probability** (sum of above):
- **0.7–1.0**: High confidence framework influenced this action
- **0.4–0.7**: Medium confidence (adoption possible)
- **0.0–0.4**: Low confidence (likely coincidence)

---

## Part 5: Phase 2 Decision Framework

### Go/No-Go Scoring Model

At each decision gate (Day 7, 30, 90, 180), score the following criteria:

| Criterion | Weight | Day 7 | Day 30 | Day 90 | Day 180 |
|---|---|---|---|---|---|
| Email reply rate | 20% | ≥10% | ≥40% | ≥50% | ≥60% |
| Vocabulary adoption signals | 20% | ≥1 | ≥5 | ≥15 | ≥30 |
| Litigation trend (acceleration vs. control) | 20% | ≥10% faster | ≥25% faster | ≥40% faster | ≥50% faster |
| Domain-specific requests (new demand) | 15% | ≥1 domain | ≥5 domains | ≥10 domains | ≥12+ domains |
| Sector diversity (# sectors with adoption) | 15% | ≥1 sector | ≥2 sectors | ≥4 sectors | ≥5 sectors |
| **Go/No-Go Threshold** | **100%** | **≥3 of 5 green** | **≥4 of 5 green** | **≥4 of 5 green** | **≥5 of 5 green** |

**Color coding**:
- **Green** (≥threshold): Criterion met
- **Yellow** (75–99% of threshold): Criterion nearly met
- **Red** (<75% of threshold): Criterion not met

**Decision rules**:
- **Day 7**: If Red criteria, investigate. If ≥3 Green, continue.
- **Day 30**: If ≥4 Green, proceed to Phase 2 design. If <4 Green, extend Phase 1 or abort.
- **Day 90**: If ≥4 Green, begin Phase 2 limited launch (3–5 domains, sector-targeted). If <4 Green, extend Phase 1 measurement.
- **Day 180**: If ≥5 Green, full Phase 2 launch (12+ new domains, all sectors). If <5 Green, framework may need revision; consider Phase 3 delay.

---

## Part 6: Implementation Roadmap

### Pre-Phase-1-Launch Setup (Day -7 to Day 0)

1. **Database setup** — Deploy SQLite, test queries
2. **Monitoring infrastructure** — Google Scholar Alerts, Gmail Bcc setup, PACER script deployment
3. **Baseline documentation** — Pre-distribution litigation count, institutional awareness, vocabulary baseline
4. **Reporting templates** — Daily report format, weekly summary, monthly deep dive
5. **Team access** — Ensure orchestrator/user can access real-time dashboard (if applicable)

### Phase 1 (Day 0–180)

**Daily**:
- [ ] PACER query (09:00 UTC)
- [ ] Email parsing (refresh Gmail Bcc address)
- [ ] Citation count (Google Scholar Alerts review)
- [ ] Log to SQLite

**Weekly** (Monday 09:00 UTC):
- [ ] Weekly summary email (reply rate, new litigation, citations, next week focus)
- [ ] Deeper analysis (vocabulary adoption scorecard, sector comparison, attribution scoring)

**Monthly** (1st of month, 09:00 UTC):
- [ ] Comprehensive analysis report (30-day adoption snapshot, forecasting, Phase 2 readiness assessment)
- [ ] Decision gate review (Is tracking toward next milestone?)

### Decision-Gate Reviews

**Day 7 (Week 2)**: Is reply rate >10%? Are monitoring systems working?  
**Day 30 (Month 1)**: Is reply rate >40%? Proceed to Phase 2 design?  
**Day 90 (Month 3)**: Is adoption gradient >25% faster than control? Proceed to Phase 2 limited launch?  
**Day 180 (Month 6)**: Is full adoption threshold met? Full Phase 2 launch?

---

## Part 7: Risk Mitigation & Contingencies

### Risk: Email delivery failures

**Symptoms**: Reply rate stuck <10% after Day 7
**Diagnosis**: Are Phase 1 emails being delivered? Check bounce rate, spam folder filtering
**Mitigation**:
- Resend framework to email bounces on Day 10 with corrected address
- Contact sample of orgs directly (phone, LinkedIn) to confirm receipt
- Use alternate email delivery channel (direct upload to Gist, separate cloud share)

### Risk: Coincidental litigation trend

**Symptoms**: Litigation filing rate accelerates post-distribution, but high-confidence attribution signals remain low
**Diagnosis**: May be industry-wide trend unrelated to framework (e.g., Supreme Court decision affecting entire field)
**Mitigation**:
- Run counterfactual comparison with parallel control group (litigation in non-distributed domains)
- If trend is broad, adjust baseline expectation; do not falsely attribute adoption

### Risk: Low adoption in expected sectors

**Symptoms**: State AGs adopt at <20% rate, but civil rights orgs at 60%
**Diagnosis**: May indicate framework is more useful for civil rights orgs than executive-branch accountability (or vice versa)
**Mitigation**:
- Investigate why low-adoption sector is uninterested (survey feedback)
- Consider Phase 2 pivot toward high-adoption sectors
- Develop sector-specific variants of framework if needed

---

## Part 8: Success Metrics & Long-Term Impact

### Short-term success (Month 1–3)

✅ **Reply rate ≥40%** (Day 30 gate)
✅ **Vocabulary adoption ≥5 signals** (Day 30 gate)
✅ **Litigation trend ≥25% acceleration vs. control** (Day 90 gate)
✅ **Domain-specific follow-up requests ≥5** (Day 90 gate)

### Medium-term success (Month 3–6)

✅ **Institutional playbook adoption** (≥3 sectors publishing custom playbooks using framework)
✅ **Policy impact** (≥1 state bill or executive action citing framework)
✅ **Citation momentum** (≥30 high-confidence citations in published documents)
✅ **S-curve adoption** (Framework positioning as "early majority" adoption, 15–50% within sector)

### Long-term success (Month 6+)

✅ **Framework baseline integration** (Framework vocabulary becomes institutional baseline, future Phase 2 work built on framework instead of competing proposals)
✅ **Policy amplification** (Federal or state policy changes driven by framework adoption)
✅ **Cross-sector coordination** (Institutions adopting framework form ad-hoc coalition for coordinated action)

---

## Tools & Technology Stack

### Automation Tools (No Code)

- **Gmail filtering**: Bcc address + filter rules, export to CSV daily
- **Google Sheets**: Manual tracking dashboard (if preferred to SQLite)
- **IFTTT / Zapier**: Route email alerts → Slack → daily digest

### Python Scripts (Code)

- **PACER monitoring**: requests + BeautifulSoup + SQLite
- **Email parsing**: imapalib + email + sqlite3
- **Reporting**: Jinja2 templates + SQLite queries → HTML email report
- **Data export**: pandas → CSV/Excel for analysis

### Optional: Cloud Infrastructure

- **AWS Lambda**: Run daily PACER query on cron schedule
- **S3**: Archive SQLite database snapshots
- **CloudWatch**: Monitor job success/failures, alert on errors

---

## Next Steps

**Status**: Design complete, ready for Day 1 deployment  
**Awaiting**: Phase 1 launch decision (user distribution path: A / A+37 / B)

**On Day 1 of Phase 1 launch**:
1. Deploy SQLite database
2. Configure monitoring tools (Google Scholar, PACER script, Gmail Bcc)
3. Begin daily tracking
4. Generate first baseline report
5. Schedule weekly reviews + decision gates

**Monthly**: Comprehensive adoption report + Phase 2 readiness assessment

