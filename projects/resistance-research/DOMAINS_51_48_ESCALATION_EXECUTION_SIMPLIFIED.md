---
title: "Domains 51/48 Wave 1 Escalation Execution — Simplified 3-Email Sequence"
created: "2026-06-25 08:55 UTC"
status: "production-ready — orchestrator Item 37 contingency execution"
trigger: "June 25 12:00 UTC — execute IF Wave 1 sends have not been confirmed"
execution_time: "15-20 min total (copy-paste templates, send 3 emails, log sends)"
---

# Domains 51/48 Wave 1 Escalation Execution

## Context

Domains 51/48 Wave 1 sends are **production-ready** but **overdue** (expected June 23-27, now June 25 08:55 UTC).

Per DOMAINS_51_48_WAVE_1_CONTINGENCY_FRAMEWORK.md:
- **June 25 12:00 UTC** is the decision point
- If sends NOT confirmed by this time: execute simplified 3-email sequence (top contacts only)
- This maintains "on-track" status per Contingency A (June 25 sends still acceptable, 13-day response window)
- Hard deadline remains June 27 18:00 UTC (after which, response window becomes insufficient)

---

## Escalation Decision Tree

```
CONDITION CHECK: As of June 25 12:00 UTC, have Domains 51/48 Wave 1 sends been confirmed?

┌─ YES, both domains sent by 12:00 UTC
│  └─ ✅ NO ACTION NEEDED — Proceed to Wave 1 response monitoring (Item 23)
│
└─ NO, neither domain sent by 12:00 UTC
   └─ ⚠️  EXECUTE ESCALATION NOW — Proceed to "Simplified 3-Email Sequence" below
      - Send Domain 51 Email 1 (Campaign Legal Center) immediately
      - Wait 90 minutes
      - Send Domain 48 Email 1 (Sentencing Project) 
      - Send Domain 51 Email 2 (Issue One) next business day
      - Send Domain 48 Email 2 (Prison Policy Initiative) 2-3 hours after Email 1
      - Send Domain 48 Email 3 (ACLU) next business day
```

---

## Simplified 3-Email Sequence — Domain 51 (Campaign Finance)

### Domain 51 Email 1: Campaign Legal Center
**Recipient**: Erin Chlopak, Senior Director, Campaign Finance  
**Email address**: echlopak@campaignlegalcenter.org  
**Send time**: June 25, 12:15–13:00 UTC (or next available)  
**Template**: COPY ENTIRE SECTION BELOW and send

---

**To**: echlopak@campaignlegalcenter.org

**Subject**: Constitutional architecture research on Citizens United — Hawaii/Montana model + FEC collapse analysis

Dear Campaign Legal Center team,

I am sharing a research document that may be relevant to your current work on campaign finance enforcement and state-level reform:

**Domain 51** documents the Citizens United architecture from a democratic design perspective — specifically the structural consequence of the FEC's 200+ day enforcement quorum collapse and the constitutional theory behind Hawaii SB 2471 (signed May 15, 2026) and Montana I-194.

The sections most relevant to CLC's work:

- **Section 6.3** (Hawaii/Montana Corporate Charter Model): the theory that CLC's constitutional team will likely assess — does charter-revocation of corporate political spending authority survive Citizens United, or only state-derived-power rationale?
- **Section 3** (FEC Structural Failure): 200-day enforcement collapse with specific pending matters
- **Section 7** (Reform Architecture): DISCLOSE Act of 2026 legislative pathway + state-level equivalents

**Full document**: https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372

58 citations, CC Attribution 4.0. I would welcome feedback on whether the constitutional analysis accurately represents current scholarly consensus.

[YOUR_NAME]  
[YOUR_CONTACT_INFO]

---

**After sending Domain 51 Email 1**: Log the send to DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md. Then wait 90 minutes.

---

### Domain 51 Email 2: Issue One
**Recipient**: Issue One (general inbox)  
**Email address**: info@issueone.org  
**Send time**: June 25, 13:30–14:00 UTC (90 min after Email 1) OR June 26 morning  
**Template**: COPY ENTIRE SECTION BELOW and send

---

**To**: info@issueone.org

**Subject**: Dark money architecture research — FEC collapse documentation + state ballot measure analysis

Dear Issue One team,

I am sharing research that complements Issue One's work on FEC reform and dark money disclosure:

**Domain 51** is a structural analysis of the Citizens United architecture with a dedicated section on the FEC enforcement collapse — which Issue One has been documenting through your "Strengthening the Rules" reporting. The document uses Issue One's enforcement deadlock analysis as a primary source and extends it to the broader democratic accountability argument.

**Most relevant sections**:

- **Section 3** (FEC Structural Failure): 200+ day enforcement shutdown with specific pending matters — Issue One's reporting is cited directly
- **Section 7** (Reform Architecture): legislative and state-level remedies that complement Issue One's advocacy angles

Issue One is cited as a primary source throughout. The document is designed for distribution to organizations that can use the structural analysis in their own advocacy.

**Full document**: https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372

58 citations, CC Attribution 4.0. I would welcome feedback on whether the constitutional and structural analysis extends or diverges from Issue One's current position on FEC reform priorities.

[YOUR_NAME]  
[YOUR_CONTACT_INFO]

---

**After sending Domain 51 Email 2**: Log the send to DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md.

---

## Simplified 3-Email Sequence — Domain 48 (Criminal Justice Civic Exclusion)

### Domain 48 Email 1: Sentencing Project
**Recipient**: Nicole D. Porter, Sentencing Project  
**Email address**: nporter@sentencingproject.org  
**Send time**: June 25, 13:00–14:00 UTC (can overlap with Domain 51 Email 1) OR June 26 morning  
**Template**: COPY ENTIRE SECTION BELOW and send

---

**To**: nporter@sentencingproject.org

**Subject**: Democratic design framing for disenfranchisement architecture — research extending the "Locked Out" series

Dear Nicole,

I am writing to share a research document that provides structural democratic analysis to accompany the Sentencing Project's disenfranchisement research — and that I believe would extend the reach of "Locked Out" findings into democracy reform networks that do not currently engage criminal justice research as directly relevant.

**Domain 48: Criminal Justice, Civic Exclusion Architecture, and the Democratic Participation Crisis** (7,100 words, 48 citations) uses the Sentencing Project's research as empirical foundation and builds a democratic design argument: the criminal justice system has accumulated, across 50 years of policy choices, a parallel civic exclusion architecture that functions as a systematic voting restriction law.

**Key contributions**:

1. **Feedback loop documentation**: The Uggen and Manza finding (seven Senate elections would have reversed under enfranchisement) is evidence that disenfranchisement is not neutral collateral consequence — it is architecture with measurable democratic effects.

2. **Secondary mechanism integration**: Jury exclusion (20M figure), employment bars, LFO poll tax mechanics, housing instability — documenting all five pathways as unified civic exclusion system.

3. **Virginia 2026 argument**: King v. O'Bannon and the November amendment provide democratic design framework for reaching democracy reform voters who don't primarily identify with criminal justice reform.

**Full document**: https://gist.github.com/esca8peArtist/[DOMAIN_48_GIST_URL]

Intended for distribution to advocacy/litigation organizations working with your research — Brennan Center, Campaign Legal Center, NAACP LDF, M4BL, state-level partners.

I would welcome your assessment of whether the democratic design framing adds useful dimension to Sentencing Project's 2026 advocacy toolkit.

[YOUR_NAME]  
[YOUR_CONTACT_INFO]

---

**After sending Domain 48 Email 1**: Log the send to DOMAIN_48_DISTRIBUTION_EXECUTION_LOG.md.

---

### Domain 48 Email 2: Prison Policy Initiative
**Recipient**: Prison Policy Initiative (general inbox)  
**Email address**: info@prisonpolicy.org  
**Send time**: June 25 or June 26 (2-3 hours after Domain 48 Email 1, or next day morning)  
**Template**: COPY ENTIRE SECTION BELOW and send

---

**To**: info@prisonpolicy.org

**Subject**: Democratic design framing for "Rigging the Jury" and "Nowhere to Go" — civic exclusion architecture synthesis

Dear PPI team,

I am sharing research that synthesizes your jury exclusion and housing instability research with voting disenfranchisement data into a unified democratic design argument.

**Domain 48: Criminal Justice, Civic Exclusion Architecture, and the Democratic Participation Crisis** (7,100 words, 48 citations) is built on three PPI research pillars:
- "Rigging the Jury" (20M excluded from jury service)
- "Nowhere to Go" (formerly incarcerated 10x more likely to experience homelessness)
- "Winnable Criminal Justice Reforms in 2026"

The synthesis argument: jury exclusion and housing instability are not separate policy problems adjacent to voting disenfranchisement. They are components of the same civic exclusion architecture — "civil death," removal of the full bundle of democratic membership rights.

This framing positions PPI's research as democratic infrastructure analysis, creating distribution pathways into democracy reform, election law academia, governance funders — channels your existing network does not currently reach.

**Full document**: https://gist.github.com/esca8peArtist/[DOMAIN_48_GIST_URL]

I would welcome discussion on whether this framing would be useful for PPI's advocacy work.

[YOUR_NAME]  
[YOUR_CONTACT_INFO]

---

**After sending Domain 48 Email 2**: Log the send to DOMAIN_48_DISTRIBUTION_EXECUTION_LOG.md.

---

### Domain 48 Email 3: ACLU Voting Rights Project
**Recipient**: Sophia Lin Lakin, ACLU Voting Rights Project Director  
**Email address**: voting@aclu.org  
**Send time**: June 26 or June 27 (next business day after Email 2)  
**Template**: COPY ENTIRE SECTION BELOW and send

---

**To**: voting@aclu.org

**Subject**: Readmission Act extension theory and LFO poll tax architecture — democratic design brief for active litigation

Dear Sophia,

I am writing to share research providing democratic design analysis directly relevant to ACLU Voting Rights Project's active litigation and the Virginia 2026 campaign.

**Domain 48: Criminal Justice, Civic Exclusion Architecture, and the Democratic Participation Crisis** (7,100 words, 48 citations) provides analysis of King v. O'Bannon's Readmission Act theory and its extension potential.

**Most directly relevant sections**:

1. **Readmission Act extension theory**: Domain 48 documents how King v. O'Bannon's independence from Richardson v. Ramirez opens theory to application in other former Confederate states (AL, AR, FL, GA, LA, MS, NC, SC, TN, TX) readmitted under similar conditions. Could provide most significant federal constitutional route to mass restoration in 50 years.

2. **LFO poll tax architecture**: Five-mechanism civic exclusion system integrating disenfranchisement with jury exclusion, employment bars, housing discrimination, and collateral consequence stacking.

3. **Virginia 2026 amplification**: Ballot measure campaign angle positioning voting restoration as democratic system protection, not just individual rights framework.

**Full document**: https://gist.github.com/esca8peArtist/[DOMAIN_48_GIST_URL]

I would welcome discussion on whether the extension theory provides useful doctrinal roadmap for the litigation strategy.

[YOUR_NAME]  
[YOUR_CONTACT_INFO]

---

**After sending Domain 48 Email 3**: Log the send to DOMAIN_48_DISTRIBUTION_EXECUTION_LOG.md.

---

## Execution Checklist

### Pre-Execution (Before sending any email)

- [ ] Create Gist for Domain 51 from domain-51-campaign-finance-dark-money.md (if not already created)
- [ ] Create Gist for Domain 48 from domains/domain-48-criminal-justice-civic-exclusion.md (if not already created)
- [ ] Fill in [YOUR_NAME] and [YOUR_CONTACT_INFO] in all 5 email templates above
- [ ] Replace [DOMAIN_48_GIST_URL] with actual Gist URL in Domain 48 emails
- [ ] Verify all 5 recipient email addresses are current:
  - [ ] echlopak@campaignlegalcenter.org
  - [ ] info@issueone.org
  - [ ] nporter@sentencingproject.org
  - [ ] info@prisonpolicy.org
  - [ ] voting@aclu.org

### Send Sequence Execution

- [ ] **Send Domain 51 Email 1** (Campaign Legal Center) — June 25 12:15–13:00 UTC or morning of June 26
  - Log in DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md
  - Record time sent

- [ ] **Wait 90 minutes** (not a hard rule; 30-120 min window acceptable)

- [ ] **Send Domain 48 Email 1** (Sentencing Project) — June 25 13:00–14:00 UTC or morning of June 26
  - Can overlap with Domain 51 Email 1 send time if needed
  - Log in DOMAIN_48_DISTRIBUTION_EXECUTION_LOG.md
  - Record time sent

- [ ] **Send Domain 51 Email 2** (Issue One) — June 25 or June 26 morning
  - Ideally 90 min after Domain 51 Email 1
  - Log in DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md
  - Record time sent

- [ ] **Send Domain 48 Email 2** (PPI) — June 25 or June 26
  - 2-3 hours after Domain 48 Email 1, or next business day
  - Log in DOMAIN_48_DISTRIBUTION_EXECUTION_LOG.md
  - Record time sent

- [ ] **Send Domain 48 Email 3** (ACLU) — June 26 or June 27
  - Next business day after Email 2
  - Log in DOMAIN_48_DISTRIBUTION_EXECUTION_LOG.md
  - Record time sent

### Post-Execution

- [ ] Log all 5 sends to respective DOMAIN_{51,48}_DISTRIBUTION_EXECUTION_LOG.md files
- [ ] Post completion confirmation to CHECKIN.md with:
  - Date/time sends completed
  - Which emails sent to which recipients
  - Any issues encountered or notes for Wave 2 planning
  - Update "Since Last Session" section

---

## Timeline & Status

**Escalation trigger**: June 25 12:00 UTC  
**Execution window**: June 25–27 (hard deadline June 27 18:00 UTC per contingency framework)  
**Total user time**: ~15-20 minutes (copy-paste 5 emails, wait 90 min, log sends)  
**Response collection window**: June 25/26-July 8 (13-14 days, contingency A timeline)  
**Wave 2 decision**: June 28-29  
**Wave 2 sends**: July 1-2  

---

## Notes for Wave 2 Planning

- If this escalation executes, record in WORKLOG.md: "June 25 escalation execution — Wave 1 sends June 25-27"
- Wave 2 staging (Item 23) should monitor Wave 1 response rates June 25-27 and prepare Wave 2 templates accordingly
- If escalation executes successfully, Wave 2 timeline compresses by ~24 hours (decision June 28 instead of June 27)
- Domain 59 Tier 2 executes independently June 25-30 regardless of Domain 51/48 Wave 1 status

---

## Contingency: If Escalation Cannot Execute

If user cannot execute by June 27 18:00 UTC:
- Domain 59 Tier 2 still executes June 25-30 on independent track
- Domains 51/48 shift to async July execution (separate from rapid-response window)
- Response window becomes insufficient for Wave 2 refinement before July 1
- Phase 2 momentum broken but infrastructure remains intact

---

**File created**: 2026-06-25 08:55 UTC  
**Status**: Production-ready for June 25 12:00 UTC execution trigger  
**Orchestrator Item**: Item 37 (Domains 51/48 Wave 1 Escalation Execution & Contingency Trigger)
