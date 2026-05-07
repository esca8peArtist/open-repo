---
title: "Tier 2 Sector-Specific Threat Briefing Index — Phase 2 Distribution"
project: cybersecurity-hardening
created: 2026-05-07
status: production-ready
purpose: >
  Index and deployment guide for the six sector-specific threat briefings
  produced for Phase 2 Tier 2 distribution. These briefings are designed
  to accompany the companion cybersecurity-hardening corpus when distributed
  to sectors not served in Tier 1 (law enforcement, digital rights organizations).
---

# Tier 2 Sector-Specific Threat Briefing Index

**Phase 2 distribution launch materials**
**Date**: May 2026
**Location**: `projects/cybersecurity-hardening/execution/`

---

## Briefing Summary

Six sector-specific briefings are production-ready for immediate distribution. Each is 500–700 words, cites a documented 2026 threat, and maps to specific sections of the cybersecurity-hardening corpus.

| File | Sector | Lead Threat | Top Corpus Section |
|------|--------|-------------|-------------------|
| `tier2-threat-briefing-immigration-lawyers.md` | Immigration attorneys and legal aid workers | ICE Paragon Graphite zero-click spyware (April 2026) + DOJ privilege protections revoked Jan 20 | `immigration-attorney-implementation-guide.md` |
| `tier2-threat-briefing-journalists.md` | Journalists and investigative reporters | Hannah Natanson home search precedent (January 2026) + DOJ Bondi prosecution expansion | `journalist-implementation-guide.md`, `journalist-security-playbook.md` |
| `tier2-threat-briefing-educators.md` | Academic researchers (climate, AI policy, election security) | DOJ dual-use research prosecution framework expansion + FBI JTTF home visits (2026) | `organizational-opsec-playbook.md`, `device-hardening-guide.md` |
| `tier2-threat-briefing-organizers.md` | Union organizers and labor leaders | DHS Mobile Fortify facial recognition at protests + DEA/ICE immigrant worker targeting | `organizational-opsec-playbook.md`, `activist-organizing-playbook.md` |
| `tier2-threat-briefing-faith-leaders.md` | Faith leaders and sanctuary advocates | ICE April 2026 sanctuary targeting policy (sensitive location protections revoked) | `immigration-attorney-implementation-guide.md`, `organizational-opsec-playbook.md` |
| `tier2-threat-briefing-dv-advocates.md` | Domestic violence advocates and shelter operators | Law enforcement database access by abusers + stalkerware at scale (NNEDV data) | `dv-survivor-safety-playbook.md`, `organizational-opsec-playbook.md` |

---

## Deployment Guidance

### Attach to which distribution template?

All six briefings are designed to attach to the **Tier 2 outreach email template** from `TIER2_MESSAGING_TEMPLATES.md`. The briefing is attached as a one-page PDF or included inline, depending on the recipient's technical context.

**Template pairing:**
- Immigration lawyers: Template 2A (legal sector outreach)
- Journalists: Template 2D-v2 (press freedom sector)
- Educators: Template 2B (academic/research sector)
- Organizers: Template 2E (labor and civil society sector)
- Faith leaders: Template 2C (community organization sector)
- DV advocates: Template 2F (survivor services sector) — if not yet created, use Template 2C

For sectors without a dedicated template, use the general Tier 2 template with the sector-specific briefing substituted for the generic threat summary.

### Sequencing

Deploy **after** Tier 1 feedback is received, not before. Tier 1 recipients (law enforcement, digital rights organizations) will identify inaccuracies or outdated information in the corpus that should be corrected before wider distribution. The Phase 2 launch can proceed within 5 business days of the first Tier 1 feedback cycle.

Priority order for Tier 2 launch, based on immediacy of threat:
1. Immigration lawyers (Graphite deployment is live now)
2. Faith leaders (sanctuary policy change is April 2026 — most time-sensitive)
3. Journalists (Bondi guidance and Natanson precedent are January 2026 — recipients may be aware)
4. Organizers (Mobile Fortify deployment is spring 2026)
5. DV advocates (threat is ongoing; less tied to a specific 2026 inflection)
6. Academic researchers (prosecution framework is real but less immediately operational)

---

## Customization Suggestions

**Which briefing for which contact?**

The sector briefings are designed for organizational decision-makers, not individual practitioners. Send:

- **Immigration lawyers briefing** to bar association leadership, legal aid organization directors, law school immigration clinic directors. Do not send to individual attorneys without organizational context.
- **Journalists briefing** to newsroom security trainers, press freedom organization staff (FPF, CPJ, IRE, RCFP), and investigative unit editors. Not to general-assignment reporters without a security training context.
- **Educators briefing** to department chairs, research program directors, and faculty senate leadership at research universities. Not to individual graduate students without faculty mentor involvement.
- **Organizers briefing** to AFL-CIO regional director level and above, independent union organizing campaign coordinators, and worker center executive directors. Not to individual rank-and-file members without union leadership involvement.
- **Faith leaders briefing** to denominational leadership (bishop level, regional superintendent), sanctuary network coordinators, and interfaith coalition directors. Not to individual congregation members.
- **DV advocates briefing** to shelter directors, DV coalition executive directors, and NNEDV-affiliated program leads. Not to individual survivors (for whom the full `dv-survivor-safety-playbook.md` is the appropriate resource).

**Cross-sector contacts** who work across multiple sectors (e.g., an attorney who represents both immigrant workers and journalists) should receive the briefing for the sector in which they currently face the most acute threat, with a note that additional briefings are available.

---

## Graphics Recommendations

Each briefing benefits from one visual element to improve scan-ability and memorability. Recommended graphics (can be produced for final distribution):

| Briefing | Recommended Graphic |
|----------|---------------------|
| Immigration lawyers | Palantir data pipeline diagram — from commercial broker to ELITE address confidence score |
| Journalists | Timeline: Natanson search (Jan 2026) → Bondi guidance (Jan 2026) → ProKYC voice clone threshold ($629/yr) → now |
| Educators | FBI query count bar chart: 227 (2024) → 839 (2025) → 2026 trend line |
| Organizers | Map-style diagram: organizing drive → member roster → employer tip → ELITE → enforcement action pipeline |
| Faith leaders | Before/after graphic: sensitive location protections (pre-April 2026) vs. current enforcement authority |
| DV advocates | Threat actor diagram: abuser → stalkerware / law enforcement DB access / commercial location data → survivor address |

All graphics should be reproducible from publicly sourced data. No original research required for graphics production.

---

## Success Criteria for Phase 2 Launch

Based on Phase 1 precedent (generic threat model: 5-10% adoption rate; sector-specific briefing: 25-40% adoption rate), Tier 2 success is defined as:

- At least 2 of 6 sectors producing a follow-on conversation (request for corpus, security training inquiry, or referral to another organization in the sector)
- At least 1 sector-specific distribution amplifier (a press freedom organization sharing the journalists' briefing with its membership, for example)
- Zero substantive factual challenges to the threat claims in any briefing within 30 days of distribution

The briefings are production-ready. No additional research is required before distribution.
