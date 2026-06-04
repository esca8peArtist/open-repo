---
title: "Phase 6 Wave 1 Author Recruitment Outreach Templates"
project: systems-resilience
phase: 6
wave: 1
status: PRODUCTION-READY — deploy June 10-12
created: 2026-06-10
purpose: "Four email variants (Tier A base + domain-specific hooks, Tier B, Tier C, and fallback reminder) for author recruitment. Ready to send after filling merge fields. No placeholder sections in subject or body — only merge fields."
send_schedule:
  tier_a: "June 10, Thursday 2:00 PM recipient local time"
  tier_b: "June 11, Thursday 2:00 PM recipient local time"
  tier_c: "June 11, Friday 9:00 AM recipient local time"
  reminder: "June 12, Saturday 9:00 AM if no response to June 10-11 outreach"
merge_fields:
  - "{{CANDIDATE_NAME}} — full name as listed in target list"
  - "{{DOMAIN_NAME}} — e.g. International Coordination, Intergenerational Knowledge"
  - "{{DOMAIN_HOOK}} — domain-specific paragraph (Section 2 of this document)"
  - "{{DOMAIN_NUMBER}} — 60, 61, 62, 63, 64, or 65"
  - "{{TIER_BENEFIT_PARAGRAPH}} — Tier-specific value proposition (Section 3)"
  - "{{SENDER_NAME}} — project lead name"
  - "{{SENDER_EMAIL}} — project lead email"
cross_references:
  - PHASE_6_AUTHOR_RECRUITMENT_TARGET_LIST.md
  - AUTHOR_DOMAIN_MAPPING_RUBRIC.md
  - JUNE_14_15_AUTHOR_MATCHING_SESSION_RUNBOOK.md
word_count: ~2,400
---

# Phase 6 Wave 1 Author Recruitment Outreach Templates
## June 10–12, 2026 Deployment — Domains 60–65

> **Deployment instructions**: Fill all {{MERGE_FIELDS}} before sending. Do not send any template with unfilled merge fields. The subject line, opening paragraph, and closing are fixed; only the domain hook and tier paragraph vary. Thursday 2 PM local time for Tier A (academic sending research). Friday 9 AM for Tier C (community/practitioner sending). Send via the project lead email account — not a mass mailer. Individual emails only.

---

## Template 1: Tier A Base Email (Primary Outreach)

**Subject line variants** (choose one):

- `Research invitation: {{DOMAIN_NAME}} for community resilience (8-week, paid)`
- `Contributing author invitation — systems resilience research project`
- `Paid research brief: {{DOMAIN_NAME}} in Zone 5 communities`

*Recommendation: Use the first subject line for academics; the second for practitioners not primarily identified as researchers.*

---

**Email body:**

Dear {{CANDIDATE_NAME}},

I am writing with an invitation to contribute a research brief to the Systems Resilience Project, a practitioner-oriented research initiative building a long-form publication suite on community-scale resilience — specifically how Zone 5 rural and semi-rural communities (northern Illinois, Iowa, southern Wisconsin) can build robust, multi-generational systems independent of institutional failure.

We are building Phase 6 of this project: six domain-specific research guides (approximately 8,000–10,000 words each), written for practitioners, community organizers, and policymakers — not academic audiences. Your work on {{DOMAIN_NAME}} makes you a strong candidate for the Domain {{DOMAIN_NUMBER}} brief.

{{DOMAIN_HOOK}}

{{TIER_BENEFIT_PARAGRAPH}}

**The commitment**: 8 weeks beginning June 20, 2026. Estimated 8 hours per week. Compensation is paid upon two milestones (outline approval at week 1, final draft at week 8). The format is practitioner Markdown, published under Creative Commons. Full scope brief, source library, and peer reviewer will be provided at kickoff.

**To confirm by June 12**: Please reply with a brief yes or conditional yes by June 12, 2026. A conditional yes (e.g., "yes, if the scope aligns with X") is welcome — we will schedule a 15-minute call to confirm scope fit before finalizing.

If this is not the right moment for you, a referral to a colleague who works in {{DOMAIN_NAME}} would be genuinely helpful.

Thank you for your work and your time in reading this.

{{SENDER_NAME}}
{{SENDER_EMAIL}}
Systems Resilience Project

---

## Template 2: Tier B Email (Standard Outreach)

**Subject line variants:**

- `Research contributor invitation — {{DOMAIN_NAME}}, paid 8-week project`
- `Practitioner research brief: {{DOMAIN_NAME}} for Zone 5 communities`

---

**Email body:**

Dear {{CANDIDATE_NAME}},

I am reaching out with an invitation to contribute to the Systems Resilience Project, a practitioner-oriented publication initiative focused on community-scale resilience in Zone 5 rural regions (northern Illinois, Iowa, southern Wisconsin).

Phase 6 of the project is building six long-form research guides — approximately 7,000–9,000 words each — for practitioners, community organizers, and policymakers. Your expertise in {{DOMAIN_NAME}} makes you a strong fit for the Domain {{DOMAIN_NUMBER}} brief.

{{DOMAIN_HOOK}}

{{TIER_BENEFIT_PARAGRAPH}}

**The commitment**: 8 weeks beginning June 20, 2026. Estimated 4–6 hours per week. Compensation is paid in two installments (outline approval at week 1, final draft at week 8). You will receive a full scope brief, pre-staged source library (25–35 verified citations), and a dedicated peer reviewer who provides feedback at week 5 and week 8.

The format is practitioner Markdown. You do not need to be a Markdown expert — we provide a formatting template and review pass. The peer reviewer and I provide structural editorial support throughout.

**To confirm by June 12**: Reply with a brief yes or conditional yes. If this is not the right window, a referral to a colleague with expertise in {{DOMAIN_NAME}} is equally helpful.

Thank you,

{{SENDER_NAME}}
{{SENDER_EMAIL}}
Systems Resilience Project

---

## Template 3: Tier C Email (Community/Practitioner Outreach)

**Subject line variants:**

- `Research contribution opportunity: {{DOMAIN_NAME}}, paid, with full support`
- `We're looking for practitioners in {{DOMAIN_NAME}} — paid research project`

---

**Email body:**

Dear {{CANDIDATE_NAME}},

The Systems Resilience Project is building a practitioner-facing publication suite on community resilience — specifically, how Zone 5 rural communities (northern Illinois, Iowa, southern Wisconsin) build durable systems in the face of institutional and ecological stress.

We are looking for contributors who have direct experience in {{DOMAIN_NAME}} — not just research credentials. Your work in this area is what we need. The document you would contribute is approximately 3,000–4,500 words and is written for community organizers and practitioners, not academics.

{{DOMAIN_HOOK}}

{{TIER_BENEFIT_PARAGRAPH}}

**The commitment is flexible**: 2–4 hours per week over 8 weeks, beginning June 20, 2026. You will receive a detailed scope brief, a pre-staged source library to build from, a structural template so you are not starting from a blank page, and weekly check-ins with the project lead. Compensation is paid at outline approval (week 1) and final draft submission (week 8).

You do not need to be a professional writer or academic researcher. If you have lived experience in {{DOMAIN_NAME}} and can write clearly about what you know, this project is designed for you.

**To confirm by June 12**: Reply with interest and 1–2 sentences about your experience in {{DOMAIN_NAME}}. We will schedule a brief call to talk through the scope before any commitment is finalized.

{{SENDER_NAME}}
{{SENDER_EMAIL}}
Systems Resilience Project

---

## Template 4: Reminder Email (Non-Respondents Only)

*Send June 12 AM to any Tier A or Tier B candidate who has not replied to the June 10–11 outreach. Do not send to Tier C contacts who received Friday outreach — give them through Monday.*

**Subject line:**

- `Following up: research brief invitation, {{DOMAIN_NAME}} (decision window closes June 13)`

---

**Email body:**

Dear {{CANDIDATE_NAME}},

I sent a brief note on {{ORIGINAL_SEND_DATE}} about a paid research contribution to the Systems Resilience Project — specifically a practitioner-facing brief on {{DOMAIN_NAME}} for Zone 5 communities, 8 weeks beginning June 20.

I am following up because the author matching session is June 14–15 and I want to confirm whether you are available or can point me to a colleague who might be.

If the answer is no, or not now, a one-line reply lets me close the loop and reach out to my next candidate without delay. Either way, a response by June 13 end of day is appreciated.

If you have questions about scope, commitment, or compensation before deciding, reply with those — I will turn around a direct answer the same day.

Thank you,

{{SENDER_NAME}}
{{SENDER_EMAIL}}

---

## Section 2: Domain-Specific Hooks ({{DOMAIN_HOOK}} Merge Field)

*Copy the relevant paragraph into the {{DOMAIN_HOOK}} position in the base email. Edit proper nouns only if needed for candidate-specific relevance.*

### Domain 60 — International Coordination

The Domain 60 brief asks a specific question: how does a Zone 5 rural community access international networks — seed sovereignty organizations, transnational mutual aid, diaspora agricultural networks — without routing through the US federal government? Your work on {{SPECIFIC_RESEARCH_AREA}} is directly relevant. The document will map accessible international frameworks, document legal pathways for community-level international coordination, and provide 3–5 case studies of communities that have successfully integrated international resources at the local scale. This is not a document about foreign policy or international relations — it is a practitioner guide for community organizers who want to plug into international networks that their neighbors and government agencies have largely ignored.

### Domain 61 — Intergenerational Knowledge Transmission

The Domain 61 brief addresses one of the most underserved gaps in community resilience literature: how skilled practice — farming, infrastructure repair, ecological knowledge — actually transfers between generations when institutional infrastructure is absent or failing. Your work on {{SPECIFIC_RESEARCH_AREA}} speaks directly to the tacit knowledge problem: documentation alone does not transmit practice. The document will cover non-formal skill transmission frameworks, apprenticeship and mentorship design for community settings, oral history and demonstration methods, and crisis-context knowledge preservation protocols. The goal is a practitioner guide that a Zone 5 community leader can use to design a knowledge transmission program starting in year one — not a theory of adult learning.

### Domain 62 — Infrastructure Interdependencies

The Domain 62 brief maps how infrastructure failures cascade through Zone 5 community systems — grid failure to water pumping failure to food storage failure to community health failure — and identifies where community-scale intervention can interrupt those cascades. Your work on {{SPECIFIC_RESEARCH_AREA}} gives you the grounding to write this without overstating technical complexity or understating community agency. The document will cover cascade failure mapping, community-scale redundancy design, prioritization frameworks for infrastructure investment, and Zone 5-specific failure scenarios. Every technical section must answer: what does a community member actually do? This is not an engineering report — it is a decision guide for communities operating with limited resources.

### Domain 63 — Ecosystem Restoration

The Domain 63 brief is a practitioner guide to Zone 5 soil and ecosystem restoration — specifically, what a community or farmer does over a 5-year horizon to rebuild soil biology, establish perennial food systems, and integrate native plant corridors, starting from degraded row-crop ground. Your work on {{SPECIFIC_RESEARCH_AREA}} is exactly the kind of field-grounded expertise this document needs. The brief will cover soil health assessment, cover crop succession protocols, no-till transition pathways, food forest establishment timelines, and community-scale restoration coordination. Every section must answer: what do you do, in what order, and how long does it take to see measurable results? Theory is background; implementation is the content.

### Domain 64 — Community Economic Resilience

The Domain 64 brief addresses the economics of Zone 5 community resilience: how communities build economic structures that function when the broader economy is stressed or inaccessible. Your work on {{SPECIFIC_RESEARCH_AREA}} — specifically {{RELEVANT_SUBTOPIC}} — maps directly to the practitioner questions this document addresses. The brief will cover complementary currency design, cooperative enterprise formation, community land trusts, local investment vehicles, and mutual aid economic structures. It must make real distinctions between different types of alternatives (time banks vs. mutual credit vs. local commodity currency operate very differently) and document implementation case studies from communities at Zone 5 scale. This is not a survey of heterodox economics — it is a decision guide for community organizers designing alternative economic infrastructure.

### Domain 65 — Institutional Learning and Governance Scaling

The Domain 65 brief addresses what breaks in community governance as communities grow — from 25 to 100 to 200 people — and what structural interventions work. Your work on {{SPECIFIC_RESEARCH_AREA}} provides grounding in governance failure modes that this document requires. The brief will cover Dunbar threshold governance transitions, founder concentration risk, legitimacy maintenance under stress, emergency governance design, and federation models for communities that want to coordinate without merging. Critically, this document must document failure as well as success — the underrepresented failure case studies are what differentiate it from existing governance literature. The goal is a practitioner guide for community leaders who are managing governance stress in real time, not a comparative study of governance models.

---

## Section 3: Tier-Specific Benefit Paragraphs ({{TIER_BENEFIT_PARAGRAPH}} Merge Field)

### Tier A Benefit Paragraph

Your role in this project would be as primary author and, if you are willing, as a peer mentor to one or two contributors in adjacent domains. The project publishes under Creative Commons Attribution — you are listed as primary author, the document is citable, and you retain full rights to republish or adapt in future work. If the domain produces publication-quality findings, we will offer to co-develop a condensed version for practitioner journal submission (your call). This project is structured for authors who work autonomously — you will receive a scope brief and source library at kickoff, and the first formal check-in is at week 4. Compensation is paid in two installments at outline approval and final draft.

### Tier B Benefit Paragraph

This project offers a structured pathway to practitioner-audience long-form publication — a different credential than academic peer review, and one that is increasingly valued in your field. You will receive a full scope brief, a pre-staged source library, and a peer reviewer who provides feedback mid-sprint and at final draft. The project lead reviews your outline before you begin prose production, which means structural problems are caught early. This is designed to make the writing process more efficient, not more burdened. Your name appears as primary author on the published brief, citable and under Creative Commons. For contributors who are building a practitioner writing portfolio alongside academic work, this project is designed to be a clean addition to your CV.

### Tier C Benefit Paragraph

This project is specifically designed for contributors who have direct experience but limited long-form writing history. You will not be asked to figure out structure, citation formatting, or scope definition on your own — all of that is provided via a scope brief, structural template, and weekly check-ins. The word target for your brief is 3,000–4,500 words: substantial but achievable. You will be paired with a senior contributor (Tier A) in an adjacent domain who is available for informal mentorship questions throughout the sprint. If you complete the brief to publication standard, your name appears as primary author — a practitioner-facing, Creative Commons publication that you can share with your network and cite in future applications or grant proposals.

---

## Section 4: Email Metadata and Sending Notes

**Send-time optimization**:
- Academic recipients (university affiliations): Thursday 2:00 PM recipient local time. Thursday afternoon is high open-rate for academic email; avoids Friday afternoon discard and Monday morning backlog.
- Practitioner recipients (think tanks, NGOs, cooperatives, independent): Friday 9:00 AM recipient local time. Practitioners review email before the weekend; Friday morning outperforms Thursday for non-academic networks.
- Reminder email: Saturday morning (June 12, 9:00 AM recipient local time) for Tier A non-respondents. Brief, direct, explicit close-by date.

**Timezone notes**:
- EST recipients (Cornell, Northeastern, NYU, Boston College, Duke, The New School): send at 14:00 EST.
- CST recipients (Land Institute/Salina KS, Iowa contacts, Illinois contacts): send at 14:00 CST.
- MST recipients (University of Colorado): send at 14:00 MST.
- International recipients (Rotterdam, Sydney, New Zealand): send at 09:00 recipient local time on Friday — avoids mid-week timing complexity.

**Personalization floor**: Every outreach email must include at minimum the candidate's name (not "Dear Colleague"), the specific domain they are being recruited for, and one sentence that references their actual published work or organization by name. Generic outreach to researchers yields near-zero response rates. The domain hook paragraph handles specificity; review it to ensure it actually references the candidate's work.

**Reply tracking**: Log every sent email in PHASE_6_AUTHOR_RECRUITMENT_TRACKING.md (entry: date sent, candidate, domain, tier, reply status). Update within 24 hours of any reply.

**Decline handling**: If a candidate declines, ask in one sentence: "Is there a colleague you'd recommend for this domain?" Referrals from declines are often the best leads. Log referral in tracking sheet and reach out to referral within 48 hours.

---

*Templates Version 1.0 — Phase 6 Wave 1 — Prepared June 10, 2026 (Item 69). Deploy June 10–12; author matching session June 14–15.*
