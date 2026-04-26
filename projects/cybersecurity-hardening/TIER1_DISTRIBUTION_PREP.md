---
title: "Tier 1 Distribution Prep: Ready for Outreach"
project: cybersecurity-hardening
created: 2026-04-26
status: ready-for-user-approval
gist-url: "https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108"
---

# Tier 1 Distribution Prep: Ready for Outreach

This document consolidates the Tier 1 distribution strategy, provides ready-to-use email templates, and outlines exact next steps for the user to execute the outreach phase.

**Status**: All materials prepared. Awaiting user approval to execute.

---

## Summary: Why Tier 1 First

The OpSec corpus addresses a population under active threat from ICE's ELITE system and Palantir's data integration. Distribution speed matters. Tier 1 organizations have **direct trust relationships** with the people most targeted by these systems — they can immediately act on Part 0 (data broker opt-outs, no technical expertise required) and distribute the Tier 1 checklist to their clients and networks.

**Distribution order matters**: Direct-need networks first → Amplifier networks → Researcher/policy networks.

---

## Tier 1 Organizations: Contact Points and Strategy

### **1A. Immigration Legal Aid Organizations**

Organizations that work directly with undocumented clients and their families.

| Organization | Contact Point | Key Notes |
|-------------|---------------|-----------|
| National Immigration Law Center (NILC) | nilc.org contact form | Tech/security team specifically |
| CLINIC — Catholic Legal Immigration Network | clinic.org/contact | 400+ affiliated programs nationally |
| RAICES (Texas) | communications@raicestexas.org | High-volume client base |
| Immigrant Legal Resource Center (ILRC) | ilrc.org publications channel | May want to host as resource |
| National Lawyers Guild (NLG) | nlg.org tech & law committee | Signal expertise, will understand threat model |

**What to send to 1A**: 
- Executive summary (from publication-prep.md, 600 words)
- Link to the Gist: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108
- Call out Part 0 (data broker opt-outs) as immediately actionable for their clients

---

### **1B. Community-Based Organizations Serving Immigrant Communities**

Ground-level organizations with direct trust relationships with people most targeted.

- **Local interfaith sanctuary networks**: Search "[city] sanctuary network" — most have Signal or email lists
- **CASA (casaforall.org)**: Mid-Atlantic immigrant advocacy with community education infrastructure
- **Make the Road Network (maketheroadamerica.org)**: State chapters with community education programs
- **United We Dream (unitedwedream.org)**: National DACA-focused network with comms infrastructure
- **Centro de los Derechos del Migrante (centrocdm.org)**: Migrant worker organizing (Mexico + U.S.)

**What to send to 1B**:
- Simplified version: Part 0 + Tier 1 checklist extracted as a standalone two-page handout
- Plain-language cover sheet in Spanish and English (not yet created — optional enhancement)
- Link to full corpus on Gist

---

### **1C. Mutual Aid Networks**

Mutual aid networks reach people not accessible through formal legal organizations.

- **National Bail Fund Network (nationalbailfund.org)**: Reaches people in legal jeopardy
- **Local mutual aid networks**: Search "[city] mutual aid" — Slack, Signal, Telegram groups
- **Food Not Bombs local chapters**: Street-level presence in most major cities
- **Anarchist Black Cross**: Prison support network with security culture experience

**What to send to 1C**:
- Part 0 (data broker opt-outs) + Tier 1 checklist
- Emphasize: Part 0 is highest-leverage, no tech expertise, 2–4 hours, directly reduces ELITE targeting

---

## Email Templates (Ready to Customize)

All templates below are ready to personalize for each relationship. **Do not copy-paste verbatim** — adjust for the specific organization and your relationship to them.

### **Template 1A: Legal Aid Organizations (Immigration Legal Aid)**

```
Subject: Resource — practical OpSec guide for immigration enforcement threat landscape

Body:

I'm passing along a practical security guide I think is directly relevant to [organization]'s work.

The short version: The federal government is using Palantir's ELITE platform, which generates "address confidence scores" to prioritize deportation targets by pulling from Medicaid records, DMV records, commercial data brokers, and location data sold by smartphone apps without a warrant. The guide explains these systems in detail — all sourced from FOIA disclosures, court filings, and government contracts — and then gives step-by-step instructions for what individuals can do about it.

The most important section requires no technical expertise: Part 0 walks through submitting opt-outs to the data brokers that ICE queries without warrants. It takes 2–4 hours and directly degrades the confidence scoring used in ELITE targeting. There's a specific path documented for California residents without government-issued ID (using AB 60/AB 1766 state IDs to access the California DELETE Act's DROP platform).

The corpus is three documents:
- Threat model (what the government can actually see, with sources)
- Countermeasures playbook (what to do about it, by threat tier)
- Implementation guide (exact steps, verification checkpoints, troubleshooting)

URL: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108

Happy to discuss if useful.
```

---

### **Template 1B: Community-Based Organizations**

```
Subject: Sharing: Security guide for immigration enforcement threat landscape

Body:

We're sharing a practical three-part guide with organizations working on immigration justice and community protection.

What it covers:
- What Palantir's ELITE platform actually does (with government sources)
- What people can do to protect themselves (no tech expertise required for Tier 1)
- Step-by-step implementation (verified, tested)

Why now: ICE is actively using this system to generate deportation target lists by querying commercial data brokers without warrants. The Tier 1 countermeasures in this guide are immediately actionable.

The most important action for most people: Part 0 — data broker opt-outs. No technical expertise needed. 2–4 hours. Directly reduces your profile in the databases ICE queries.

Full guide: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108

If you'd like to discuss adaptation for your community or client base, happy to connect.
```

---

### **Template 1C: Mutual Aid Networks (Signal/Slack/Discord)**

```
Posting this because it's directly relevant to people in our network facing immigration enforcement risk.

This is a three-part guide:
1. What the federal government's surveillance systems actually do (sourced from contracts and court filings)
2. What you can do to protect yourself
3. Exact step-by-step instructions

Most important action for most people: Part 0, data broker opt-outs. No tech expertise needed. 2–4 hours. Directly reduces your profile in the databases ICE queries without warrants.

https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108
```

---

## Outreach Execution Steps

### **Step 1: Prepare Local Context**

Before sending the first email, research local organizations:

```bash
# For each city/region where you have contacts or focus:
# Search: "[city] sanctuary network" → email/Signal contact
# Search: "[city] mutual aid" → local network
# Verify current contact info for CASA, Make the Road, United We Dream chapters
```

### **Step 2: Prioritize Contacts**

Create a spreadsheet with:
- Organization name
- Contact person/email (if known) or contact form
- Organization type (1A/1B/1C)
- Your relationship to them (colleague, referral, etc.)
- Notes (why they're a priority, best channel, etc.)

### **Step 3: Customize and Send Emails**

For each organization:

1. **Select the appropriate template** (1A, 1B, or 1C above)
2. **Personalize** for the specific relationship:
   - Use the contact person's name if you know it
   - Reference a recent project or mutual connection if appropriate
   - Adjust subject line if it improves fit (e.g., "Resource for clients facing ELITE targeting")
3. **Send via**:
   - Email (for 1A legal organizations)
   - Email or Signal (for 1B community organizations)
   - Signal/Slack/Discord DM (for 1C mutual aid channels)

### **Step 4: Track and Follow Up**

Create a tracking document:
- Date sent
- Organization
- Contact method
- Response received (yes/no)
- Response type (forwarded, acknowledged, needs follow-up)
- Follow-up date (if needed)

**Follow-up timeline**: 
- After 1 week: If no response and email was the contact method, consider a Signal follow-up
- After 2 weeks: If no response and it's a key contact, consider a phone call

### **Step 5: Quarterly Review**

Set a calendar reminder for July 26, 2026 to review:
- Did the corpus require corrections or updates?
- Have any new Tier 1 organizations emerged?
- Should we prepare a Spanish-language summary for 1B organizations?

---

## Email Checklist (Before Sending)

For each outreach email, verify:

- [ ] Subject line is clear and specific
- [ ] Body is personalized (not copy-pasted verbatim)
- [ ] Gist URL is correct: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108
- [ ] Organization type is correct (1A/1B/1C)
- [ ] Tone matches channel (formal for legal orgs, friendly for community orgs)
- [ ] No attachments (direct link to Gist is cleaner and more durable)
- [ ] Contact method is appropriate (email for legal orgs, Signal for mutual aid)

---

## What to Expect After Each Email

**Likely positive responses**:
- Legal organizations will acknowledge and forward to their networks
- Community organizations will share the Gist in their Signal groups or newsletters
- Mutual aid networks will spread Part 0 widely among their members

**Likely questions you may receive**:

1. **"Is this legal?"** 
   - Yes — everything described is legal in the United States. Opting out from data brokers is a statutory right. Signal, GrapheneOS, Tor, VeraCrypt are all legal.

2. **"Can I adapt this for my community?"**
   - Yes. The corpus is designed to be primary-source-citable. If you adapt excerpts, note what was changed and cite the original. Spanish-language adaptations of Part 0 are particularly useful.

3. **"Is one person really protected by this?"**
   - This corpus explicitly states: No individual countermeasure is foolproof against a targeted investigation with full government resources and a valid court order. What this addresses is bulk commercial surveillance infrastructure that operates without warrants and at scale. The goal is to not be an easy target.

4. **"Can you help us adapt this for our specific use case?"**
   - Response: Happy to discuss. For litigation or policy use, the threat model section is designed for citation. For community education, the implementation guide's verification checkpoints can be adapted to your workflow.

---

## Sample Tracking Template

Copy this template into a document to track your outreach:

```markdown
# Tier 1 Outreach Tracking

## 1A. Legal Aid Organizations

| Organization | Contact | Date Sent | Method | Response | Follow-up |
|-------------|---------|-----------|--------|----------|-----------|
| NILC | [contact] | [date] | Email | [yes/no] | [notes] |
| CLINIC | [contact] | [date] | Email | [yes/no] | [notes] |
| RAICES | comms@... | [date] | Email | [yes/no] | [notes] |
| ILRC | [contact] | [date] | Email | [yes/no] | [notes] |
| NLG | [contact] | [date] | Email | [yes/no] | [notes] |

## 1B. Community-Based Organizations

| Organization | Contact | Date Sent | Method | Response | Follow-up |
|-------------|---------|-----------|--------|----------|-----------|
| CASA | [contact] | [date] | Email/Signal | [yes/no] | [notes] |
| Make the Road | [chapter] | [date] | Email | [yes/no] | [notes] |
| United We Dream | [contact] | [date] | Email | [yes/no] | [notes] |
| Local sanctuary networks | [city] | [date] | Signal | [yes/no] | [notes] |

## 1C. Mutual Aid Networks

| Network | Contact | Date Sent | Method | Response | Follow-up |
|---------|---------|-----------|--------|----------|-----------|
| [Local] | [contact] | [date] | Signal | [yes/no] | [notes] |
| National Bail Fund | [contact] | [date] | Email | [yes/no] | [notes] |

## Summary
- Total contacts: [X]
- Sent: [X]
- Responses received: [X] ([X%])
- Follow-ups pending: [X]
```

---

## Success Metrics

You'll know the outreach is working when:

1. **Legal organizations** forward the link to their member organizations and staff
2. **Community organizations** post the Gist in their Signal groups or newsletters
3. **Mutual aid networks** distribute Part 0 to their members (data broker opt-outs)
4. **You receive questions** about specific threat scenarios or tool setup (means people are actually reading it)
5. **The CA DROP path** gets cited specifically by California-based advocates (this is your highest-confidence indicator that the corpus is reaching undocumented people)

---

## Next Steps (User Approval Required)

To proceed with Tier 1 outreach:

1. **Review and approve** the email templates above
2. **Research local organizations** using the lists in sections 1A, 1B, 1C
3. **Build your outreach list** (spreadsheet with contact info and relationship context)
4. **Send outreach emails** starting with organizations you have direct relationships with
5. **Track responses** using the template provided
6. **Follow up after 1–2 weeks** if you don't hear back
7. **Set a quarterly review date** (July 26, 2026) to check if the threat model needs updating

---

## Files Created/Referenced in This Prep

| File | Purpose | Status |
|------|---------|--------|
| DISTRIBUTION_CHECKLIST.md | Full distribution strategy (Tier 1, 2, 3) | ✓ Reviewed |
| PUBLICATION_README.md | Publication instructions (Gist, MkDocs, PDF, SecureDrop) | ✓ Reviewed |
| threat-model.md | Threat model (440 lines, primary sources) | ✓ Published on Gist |
| opsec-playbook.md | Countermeasures by tier (635 lines) | ✓ Published on Gist |
| implementation-guide.md | Step-by-step setup (1,030 lines) | ✓ Published on Gist |
| publication-prep.md | Executive summary, TOC, glossary | ✓ Published on Gist |

---

## Key Contacts and URLs

**Published Gist**: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108

**Tier 1 Organizations (Primary Contacts)**:
- NILC: nilc.org/contact
- CLINIC: clinic.org/contact
- RAICES: communications@raicestexas.org
- ILRC: ilrc.org
- NLG: nlg.org (tech & law committee)
- CASA: casaforall.org
- Make the Road: maketheroadamerica.org
- United We Dream: unitedwedream.org

---

## Appendix: Why Tier 1 First (Strategic Rationale)

**Direct threat population**: Undocumented people, legal aid organizations serving them, community educators with direct trust relationships.

**Speed matters**: These populations face immediate risk from ELITE targeting. Legal organizations and community educators can immediately distribute Part 0 (data broker opt-outs) to their networks.

**Leverage**: Part 0 requires no technical expertise and directly degrades the address confidence scoring that drives ELITE targeting. 2–4 hours per person. Measurable impact.

**Trust relationships**: Legal aid organizations and community-based organizations already have established channels to the people most vulnerable to ELITE targeting. They can integrate the corpus into their existing client education workflows.

**Amplification comes second**: Tier 2 (digital rights organizations, security researchers, journalists) will amplify to their own audiences. But they reach an audience already somewhat informed about surveillance risks. Tier 1 reaches the people who need this information now.

---

**Status**: TIER1_DISTRIBUTION_PREP.md complete and ready for user review.

Last updated: 2026-04-26
