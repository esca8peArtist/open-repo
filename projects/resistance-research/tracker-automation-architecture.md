---
title: "Tracker Automation Architecture — Data Pipeline Design"
subtitle: "Source ingestion, validation, deduplication, database schema, and governance for four civil liberties trackers"
date: 2026-05-05
status: design-phase
project: resistance-research
purpose: Post-Phase-1 automation infrastructure
cross_references:
  - tracker-data-source-audit.md
  - tracker-dashboard-mockups.md
  - tracker-maintenance-playbook.md
---

# Tracker Automation Architecture

*Created: May 5, 2026. Purpose: Design the full data pipeline from source ingestion through validation, deduplication, and publication for all four active trackers. Implementation-ready: all tools named, all endpoints specified, all decision rules documented.*

---

## 1. High-Level Architecture

The pipeline follows a five-stage model. Each stage is independent and can be upgraded without rebuilding the others.

```
INGESTION LAYER
┌─────────────────────────────────────────────────────────────────┐
│  Source 1: CourtListener RECAP API  (polling: hourly)           │
│  Source 2: Federal Register API     (polling: 8:45 AM ET daily) │
│  Source 3: DOJ USAO RSS             (polling: hourly)           │
│  Source 4: Press Freedom Tracker    (polling: 4x daily)         │
│  Source 5: GDELT DOC 2.0            (polling: every 15 min)     │
│  Source 6: Regulations.gov API      (polling: 2x daily)         │
│  Source 7: MuckRock API             (polling: daily)            │
│  Source 8: State AG RSS feeds       (polling: 4x daily)         │
│  Source N: [additional sources]                                 │
└───────────────────────┬─────────────────────────────────────────┘
                        │ raw events (JSON)
                        ▼
NORMALIZATION LAYER
┌─────────────────────────────────────────────────────────────────┐
│  Schema normalization: map each source's fields to canonical    │
│  event schema (date, headline, description, source, URL, type)  │
│  Encoding cleanup: UTF-8, strip HTML, truncate overlength fields│
└───────────────────────┬─────────────────────────────────────────┘
                        │ normalized events (canonical schema)
                        ▼
VALIDATION LAYER
┌─────────────────────────────────────────────────────────────────┐
│  Scope filter: Does event match tracker's defined scope?        │
│  Confidence scoring: High / Medium / Low based on source tier   │
│  Flag for human review if score < Medium or scope unclear       │
└───────────────────────┬─────────────────────────────────────────┘
                        │ validated events (with confidence score)
                        ▼
DEDUPLICATION LAYER
┌─────────────────────────────────────────────────────────────────┐
│  Hash-based matching: event_date + location + headline keywords │
│  Fuzzy match: 80% similarity threshold (Levenshtein distance)   │
│  Merge duplicates: keep earliest source, add all URLs           │
└───────────────────────┬─────────────────────────────────────────┘
                        │ deduplicated events
                        ▼
TRACKER DATABASE (SQLite for local; PostgreSQL for production)
┌─────────────────────────────────────────────────────────────────┐
│  entries table   │  sources table   │  edits table              │
│  tags table      │  trackers table  │  reviews table            │
└───────────────────┬─────────────────────────────────────────────┘
                    │
                    ▼
PUBLISHING LAYER
┌─────────────────────────────────────────────────────────────────┐
│  Static export: CSV, JSON, Markdown (GitHub Pages / Obsidian)   │
│  Dashboard: Observable Framework or Datasette (open source)     │
│  RSS feed: auto-generated from new entries                      │
│  Partner briefing: automated weekly Markdown → PDF              │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. Ingestion Layer

### 2.1 Polling vs. Webhooks

Most sources in the civil liberties data ecosystem do not offer webhooks (push-based real-time notifications). All sources below require polling.

| Source | Polling Interval | Rationale |
|--------|-----------------|-----------|
| GDELT DOC 2.0 | Every 15 minutes | GDELT updates every 15 minutes; fastest available signal |
| DOJ USAO RSS | Hourly | DOJ publishes press releases throughout the business day |
| CourtListener RECAP API | Hourly | New filings processed continuously |
| Press Freedom Tracker API | Every 6 hours | Incidents verified before publication; more frequent is unnecessary |
| Federal Register API | Once daily at 9 AM ET | Federal Register publishes once per business day |
| Regulations.gov API | Twice daily (9 AM, 5 PM) | Agencies add documents throughout the day |
| State AG RSS feeds | Every 6 hours | Press releases posted during business hours |
| MuckRock API | Once daily | FOIA updates are slow-moving; daily is sufficient |
| Harvard EELP (change-detection) | Once daily | EELP updates are weekly at most |
| Protect Democracy tracker | Once daily | Updated 2–5 days after events |

### 2.2 Implementation: Polling Script

The ingestion engine should be implemented in Python using the `requests` library and `schedule` or `APScheduler`. A minimal implementation runs as a single Python process or as individual AWS Lambda functions triggered by CloudWatch Events (estimated cost: under $5/month for this load).

**Recommended hosting**: Raspberry Pi (already in use per project infrastructure notes) or a $6/month DigitalOcean Droplet. For production scale with institutional partners, AWS Lambda + S3 + EventBridge is appropriate.

**Core loop per source**:
```python
import requests, json, hashlib, schedule

def poll_federal_register():
    url = "https://www.federalregister.gov/api/v1/documents.json"
    params = {
        "conditions[agencies][]": ["environmental-protection-agency"],
        "conditions[type][]": ["RULE", "PRORULE", "NOTICE"],
        "per_page": 20,
        "order": "newest"
    }
    response = requests.get(url, params=params)
    raw_events = response.json()["results"]
    for event in raw_events:
        normalized = normalize_federal_register(event)
        pipeline.ingest(normalized)

schedule.every().day.at("09:00").do(poll_federal_register)
```

### 2.3 Source Outage Handling

Each source should implement:
- **Retry logic**: Exponential backoff on failed requests (1 min, 2 min, 4 min, 8 min), up to 4 retries before logging an error.
- **Timeout**: 30 seconds per request; do not let a slow source block the queue.
- **Dead source alert**: If a source fails for 3 consecutive polling cycles, send an alert to the maintainer (email via `smtplib` or Slack webhook).
- **Fallback mode**: During a source outage, log the gap and increase cadence of manual check for that source. Do not substitute a lower-quality source automatically — that would create inconsistency in the data lineage.

### 2.4 Data Format Normalization

Each source returns different schemas. The normalization layer maps to the canonical event schema:

**Canonical event schema**:
```json
{
  "event_id": "sha256 hash of (source_id + source_event_id)",
  "tracker": "first-amendment | environmental | police-brutality | prosecutorial",
  "date": "YYYY-MM-DD (date of underlying event, not publication date)",
  "date_published": "YYYY-MM-DD (date source published the record)",
  "headline": "string (max 200 chars)",
  "description": "string (max 2000 chars)",
  "source_name": "string (e.g., 'CourtListener', 'DOJ Press Release')",
  "source_url": "string (direct URL to source document)",
  "additional_urls": ["array of secondary source URLs"],
  "category": "string (see category taxonomy below)",
  "tags": ["array of keyword tags"],
  "state": "2-letter state code or 'federal'",
  "confidence": "high | medium | low",
  "review_status": "auto-approved | pending-review | approved | rejected",
  "added_by": "automated | [username]",
  "added_at": "ISO 8601 timestamp",
  "edit_history": []
}
```

**Source-specific normalizers** (one function per source):

```python
def normalize_courtlistener(raw):
    return {
        "date": raw.get("date_filed"),
        "date_published": raw.get("date_filed"),
        "headline": raw.get("case_name", "Untitled Case")[:200],
        "description": f"Federal case filed in {raw.get('court')}. "
                       f"Docket: {raw.get('docket_number')}",
        "source_name": "CourtListener RECAP",
        "source_url": f"https://www.courtlistener.com{raw.get('absolute_url')}",
        "state": extract_state_from_court(raw.get("court")),
        "confidence": "medium"  # court filings are real but scope match uncertain
    }

def normalize_federal_register(raw):
    return {
        "date": raw.get("effective_on") or raw.get("publication_date"),
        "date_published": raw.get("publication_date"),
        "headline": raw.get("title", "")[:200],
        "description": raw.get("abstract", "")[:2000],
        "source_name": "Federal Register",
        "source_url": raw.get("html_url"),
        "state": "federal",
        "confidence": "high"  # official government publication
    }
```

---

## 3. Validation Layer

### 3.1 Scope Boundaries Per Tracker

Each tracker has a defined scope. The validation layer applies a scope check before any event enters the database.

**First Amendment tracker scope**: Any action by a government actor (federal, state, or local) that restricts, punishes, or chills speech, press, assembly, or petition rights. Includes: press credential denial, journalist arrest, book bans imposed by government entities, anti-protest laws, government-coerced platform deplatforming, SLAPP suits with government involvement. Excludes: purely private actions, opinion pieces, commentary about First Amendment issues without a concrete governmental action.

**Environmental rollbacks tracker scope**: Any formal regulatory action (proposed rule, final rule, interim final rule, guidance withdrawal, enforcement policy change) that reduces environmental protections. Also includes litigation seeking to block such actions. Excludes: routine permit approvals, news commentary, academic analysis.

**Police brutality tracker scope**: Documented incidents of police use of force resulting in death or serious injury; consent decree filings, compliance hearings, and violations; federal pattern-or-practice investigations; civil rights settlements with police departments. Excludes: opinion pieces, policy debates not tied to specific incidents or cases, general crime news.

**Prosecutorial weaponization tracker scope**: Federal or state criminal investigations, charges, or convictions targeting individuals or organizations where: (a) the target is a political opponent, civil society organization, journalist, or former official; and (b) the legal theory is novel, unprecedented, or has not been applied to similarly situated non-political actors. Excludes: routine criminal prosecutions without political dimension, clearly meritorious prosecutions of political figures.

### 3.2 Confidence Scoring Rules

Confidence scores are assigned based on source reliability and scope clarity, not on the seriousness of the event.

| Condition | Score |
|-----------|-------|
| Source is an official government document (Federal Register, court filing, DOJ press release) | Start at High |
| Source is an established nonprofit watchdog (Press Freedom Tracker, Earthjustice, ACLU) | Start at Medium |
| Source is news media (GDELT, Media Cloud, general news) | Start at Medium |
| Source is a single outlet, unconfirmed | Downgrade one level |
| Source is corroborated by 2+ independent outlets | Upgrade one level (max High) |
| Event clearly within tracker scope (no ambiguity) | Keep current level |
| Event scope is ambiguous (may or may not qualify) | Downgrade one level |
| Event scope clearly outside tracker | Reject |

Final confidence levels:
- **High**: Official source + clear scope match. Auto-approved for publication.
- **Medium**: Credible source + clear scope match, OR official source + ambiguous scope. Requires human review before publication.
- **Low**: Unconfirmed source, ambiguous scope, or novel category. Requires human review; default to rejection if reviewer unavailable within 48 hours.

### 3.3 Scope Filter Implementation

```python
FIRST_AMENDMENT_KEYWORDS = [
    "first amendment", "press freedom", "journalist", "press credential",
    "book ban", "anti-protest", "SLAPP", "prior restraint", "shield law",
    "defamation", "chilling effect", "gag order", "subpoena journalist",
    "espionage act reporter", "qualified immunity press"
]

FIRST_AMENDMENT_EXCLUSIONS = [
    "private company", "terms of service", "content moderation",
    "lawsuit dismissed", "commentary", "op-ed"
]

def scope_check(event, tracker):
    text = (event["headline"] + " " + event["description"]).lower()
    keywords = TRACKER_KEYWORDS[tracker]
    exclusions = TRACKER_EXCLUSIONS[tracker]
    
    keyword_hits = sum(1 for kw in keywords if kw in text)
    exclusion_hits = sum(1 for ex in exclusions if ex in text)
    
    if exclusion_hits > keyword_hits:
        return "rejected", "Exclusion terms outweigh keyword matches"
    if keyword_hits == 0:
        return "rejected", "No tracker keywords present"
    if keyword_hits >= 2:
        return "in-scope", "high"
    return "in-scope", "medium"  # single keyword hit = needs review
```

---

## 4. Deduplication

### 4.1 The Problem

The same event will frequently appear across multiple sources. A new criminal indictment will appear in: the PACER/CourtListener filing, the DOJ USAO press release, GDELT coverage from AP, GDELT coverage from the Washington Post, and a Media Cloud story from a local outlet. Without deduplication, this one event creates five entries.

### 4.2 Deduplication Algorithm

**Step 1: Exact match check**
Generate a deterministic identifier for each event:
```python
import hashlib

def event_fingerprint(event):
    # Normalize: lowercase, strip punctuation, take first 8 words of headline
    words = event["headline"].lower().split()[:8]
    key = event["date"] + "|" + " ".join(words)
    return hashlib.sha256(key.encode()).hexdigest()[:16]
```
If the fingerprint matches an existing database entry, treat as duplicate → add the new source URL to `additional_urls` and update `date_published` if newer.

**Step 2: Fuzzy match check**
For events that do not exact-match, compute Levenshtein distance between the new event's headline and all events within a 7-day window. If similarity > 80%, flag as probable duplicate and queue for human review.

```python
from difflib import SequenceMatcher

def fuzzy_match(new_headline, candidate_headline):
    ratio = SequenceMatcher(None, new_headline.lower(), 
                           candidate_headline.lower()).ratio()
    return ratio > 0.80
```

**Step 3: Manual override**
Some events that appear as duplicates are actually distinct (e.g., two separate journalists arrested at the same protest). The review interface allows a reviewer to mark a flagged duplicate as "not a duplicate" with a note explaining the distinction. This decision is stored and used to train the threshold.

### 4.3 Merge Rules

When a duplicate is confirmed:
- Keep the earliest-published record as canonical
- Add all source URLs to `additional_urls`
- Update `headline` only if new source provides substantially more information
- Update `description` by appending update information in brackets: `[Update, May 5: Court issued ruling — see [source URL]]`
- Increment `source_count` field for analytics

---

## 5. Database Schema

The tracker database uses SQLite for local/development use and PostgreSQL for production deployment. Both use the same schema.

### 5.1 Core Tables

```sql
-- Primary tracker entries table
CREATE TABLE entries (
    id              TEXT PRIMARY KEY,    -- SHA-256 fingerprint (16 chars)
    tracker         TEXT NOT NULL,       -- 'first-amendment', 'environmental', etc.
    date            DATE NOT NULL,       -- Date of underlying event
    date_published  DATE,               -- Date source published it
    headline        TEXT NOT NULL,
    description     TEXT,
    category        TEXT,               -- See taxonomy below
    state           TEXT,               -- 2-letter state code or 'federal'
    confidence      TEXT NOT NULL,      -- 'high', 'medium', 'low'
    review_status   TEXT NOT NULL DEFAULT 'pending-review',
    added_by        TEXT,
    added_at        TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_published    BOOLEAN DEFAULT FALSE,
    fingerprint     TEXT UNIQUE
);

-- Source URLs for each entry (one entry can have multiple sources)
CREATE TABLE entry_sources (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    entry_id    TEXT REFERENCES entries(id),
    source_name TEXT NOT NULL,
    source_url  TEXT NOT NULL,
    is_primary  BOOLEAN DEFAULT TRUE,
    added_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tags (many-to-many)
CREATE TABLE tags (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    name    TEXT UNIQUE NOT NULL
);

CREATE TABLE entry_tags (
    entry_id    TEXT REFERENCES entries(id),
    tag_id      INTEGER REFERENCES tags(id),
    PRIMARY KEY (entry_id, tag_id)
);

-- Edit history (all changes tracked, never deleted)
CREATE TABLE edits (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    entry_id    TEXT REFERENCES entries(id),
    field       TEXT NOT NULL,
    old_value   TEXT,
    new_value   TEXT,
    edited_by   TEXT,
    edited_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    reason      TEXT
);

-- Human review log
CREATE TABLE reviews (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    entry_id        TEXT REFERENCES entries(id),
    reviewer        TEXT,
    action          TEXT,   -- 'approved', 'rejected', 'needs-more-info', 'marked-duplicate'
    notes           TEXT,
    reviewed_at     TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 5.2 Category Taxonomy

Each tracker has its own category taxonomy. Categories are used for dashboard filtering and briefing segmentation.

**First Amendment**:
- `press-exclusion` — credential denial, access restrictions
- `journalist-arrest` — criminal arrest of journalist in reporting context
- `journalist-surveillance` — government monitoring of journalists
- `book-ban` — government-imposed book removal
- `protest-restriction` — anti-protest law or enforcement
- `slapp-suit` — strategic litigation against public participation
- `platform-coercion` — government pressure on platforms to remove speech
- `espionage-act` — Espionage Act charges against journalists or sources
- `gag-order` — court-imposed silence on parties or witnesses

**Environmental Rollbacks**:
- `final-rule-rollback` — formally published rollback of existing rule
- `proposed-rule-rollback` — proposed rollback in comment period
- `guidance-withdrawal` — withdrawal of agency guidance without rulemaking
- `enforcement-cutback` — reduction in enforcement activity or funding
- `permit-approval` — approval of controversial permit (drilling, pipeline, etc.)
- `eis-action` — Environmental Impact Statement action
- `budget-cut` — EPA or agency budget reduction affecting environmental programs
- `international-withdrawal` — exit from international environmental agreements

**Police Brutality**:
- `police-killing` — police use of deadly force
- `consent-decree-violation` — documented violation of active consent decree
- `consent-decree-withdrawal` — DOJ withdrawal from or termination of decree
- `excessive-force-other` — serious injury without death
- `pattern-practice-finding` — DOJ or state AG finding of unconstitutional pattern
- `settlement` — civil rights settlement with police department
- `qualified-immunity` — court ruling on QI that affects accountability

**Prosecutorial Weaponization**:
- `political-prosecution` — criminal charges against political opponents
- `investigation-political` — investigation opened against political opponent
- `selective-enforcement` — different treatment for similarly situated actors based on political alignment
- `civil-society-targeting` — prosecution of civil society organizations
- `retaliation-prosecution` — prosecution that follows public criticism of the administration
- `section-3-action` — Fourteenth Amendment disqualification proceedings

---

## 6. Automation Governance

### 6.1 The Automation Decision Matrix

Not all events should be published automatically. This matrix defines when human review is required.

| Condition | Action |
|-----------|--------|
| Confidence = High + scope = clear + category = established | Auto-approve, publish immediately |
| Confidence = High + category = novel or undefined | Auto-draft, require human review within 24 hours |
| Confidence = Medium + scope = clear | Auto-draft, require human review within 48 hours |
| Confidence = Medium + scope = ambiguous | Queue for review; mark Low confidence until reviewed |
| Confidence = Low | Never auto-publish; queue for human review; auto-expire after 7 days without review |
| Source = GDELT or other news API | Always Medium or Low; news alone is not sufficient for High confidence |
| Source = official government doc + corroborated by watchdog | High; can auto-approve |

**Auto-approve threshold**: An event auto-approves if and only if: source tier is official government OR established watchdog, confidence is High, and the category maps unambiguously to an established category in the taxonomy.

### 6.2 Human Review Queue Interface

The review queue is implemented as a simple web interface using Datasette (open source, Python-based, renders SQLite/PostgreSQL data as a browseable, filterable web app). A reviewer sees:

- **Entry headline and description**
- **Source URL** (click to verify)
- **Confidence score and reason**
- **Category suggested by system**
- **Similar entries** (possible duplicates flagged by fuzzy match)
- **Action buttons**: Approve / Reject / Mark Duplicate / Needs More Info

Datasette installation: `pip install datasette datasette-edit-schema`. Can be hosted locally or on a small VPS. No database credentials exposed to the web.

### 6.3 Escalation Triggers

The following conditions trigger immediate escalation to a senior researcher:

- A single source adds 20+ events in a 24-hour period (possible source malfunction or spam attack)
- An event is flagged as potentially legally sensitive (accusations naming private individuals; claims of criminal conduct)
- A source has not been reachable for 48 hours (infrastructure investigation needed)
- A reviewer marks an entry "Needs More Info" and no response within 72 hours

Escalation mechanism: email alert via Python `smtplib` to the orchestrator address documented in ORCHESTRATOR_STATE.md.

---

## 7. Operational Procedures

### 7.1 Daily Automated Checks

A daily diagnostic script runs at 7:00 AM ET and produces a brief status report:

```
=== Tracker Pipeline Daily Status — 2026-05-05 ===
Sources polled in last 24h: 12/12 (100%)
New raw events ingested: 147
After scope filter: 38 relevant
After deduplication: 29 unique
Auto-approved: 14
Pending human review: 15
Currently failing sources: 0
Entries published since yesterday: 14
Review queue backlog: 22 items
```

This report is written to `projects/resistance-research/CHECKIN.md` under a daily timestamp header.

### 7.2 Alert Thresholds

| Metric | Threshold | Alert Type |
|--------|-----------|------------|
| New events from single source in 24h | > 20 | Email alert |
| Source failure duration | > 2 polling cycles | Email alert |
| Review queue backlog | > 50 items | Email alert |
| Auto-reject rate from source | > 50% over 7 days | Source quality review |
| Duplicate rate | > 30% from single source | Deduplication parameter review |

### 7.3 API Credential Rotation Schedule

| Credential | Service | Rotation Frequency | Notes |
|------------|---------|-------------------|-------|
| CourtListener token | CourtListener | Annual or on compromise | Free account; token is stable; 5,000 requests/hour authenticated |
| data.gov API key | Federal Register, GovInfo, Regulations.gov | Annual | Shared key works across data.gov services; note Regulations.gov POST restricted to federal agencies since Aug 2025 — GET/read still available |
| PACER login | PACER | Every 180 days | Federal judiciary now requires 180-day password rotation for all PACER accounts (effective 2025) |
| MuckRock API key | MuckRock | Annual | Account-based |
| GDELT | None needed | N/A | Public API, no auth |

Credentials are stored in environment variables, never in code. Use a `.env` file locally; use AWS Secrets Manager or equivalent in production.

---

## 8. Technology Stack Summary

| Component | Technology | Cost |
|-----------|-----------|------|
| Ingestion scripts | Python 3.11 + `requests` + `APScheduler` | $0 |
| Database (dev) | SQLite | $0 |
| Database (production) | PostgreSQL on $6/mo DigitalOcean | $6/month |
| Review interface | Datasette | $0 |
| Hosting (dev) | Raspberry Pi 4 | $0 (existing hardware) |
| Hosting (production) | $6/mo DigitalOcean Droplet or AWS Lambda | $6–15/month |
| Alert emails | Python `smtplib` + SendGrid free tier | $0 |
| Change-detection (EELP, Protect Democracy) | Changedetection.io (self-hosted) or Distill.io | $0–$14/month |
| Dashboard export | Observable Framework (open source) | $0 |
| PDF briefing generation | Pandoc + LaTeX | $0 |

**Total monthly operational cost estimate**: $6–30/month depending on hosting choices.

---

*Sources: [CourtListener API](https://www.courtlistener.com/help/api/) | [Federal Register API](https://www.federalregister.gov/developers/documentation/api/v1) | [Regulations.gov API](https://open.gsa.gov/api/regulationsgov/) | [GDELT API](https://blog.gdeltproject.org/gdelt-doc-2-0-api-debuts/) | [MuckRock API](https://www.muckrock.com/api/) | [GovInfo API](https://www.govinfo.gov/developers) | [Datasette](https://datasette.io/) | [Python APScheduler](https://apscheduler.readthedocs.io/)*
