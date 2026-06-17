#!/usr/bin/env python3
"""
Phase 2 Multi-Domain Wave Orchestration Script
Supports: Domain 51 (Campaign Finance), Domain 59 (Economic Precarity / Senate Finance CTC),
          Domain 48 (Criminal Justice / Civic Exclusion Architecture)

Coordinates Wave 1-2-3 execution across both domains. Generates domain-specific
execution guides, logs send results to WORKLOG.md, and provides recovery commands
for failures.

Usage:
    # Domain selection (required for most commands)
    uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --domain 51 --status
    uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --domain 59 --status

    # Execute (prints copy-paste guide + logs intent to WORKLOG)
    uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --domain 59 --execute wave1
    uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --domain 51 --execute wave1
    uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --domain 51 --execute wave2
    uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --domain 51 --execute wave3
    uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --domain 51 --execute all

    # Multi-domain status (no --domain needed)
    uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --all-domains-status

    # Sequencing recommendation (which domain executes first)
    uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --sequence-check

    # Log results
    uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --domain 59 --log-send 1 --time "2026-06-17 14:05 UTC"
    uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --domain 51 --log-bounce 5 --fallback
    uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --domain 59 --log-reply 2 --signal STRONG --summary "CBPP replied asking about Senate Finance testimony"

    # T+7 checkpoint (per-domain)
    uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --domain 51 --t7-check
    uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --domain 59 --t7-check

    # Day 7 multi-domain checkpoint (all 3 domains — June 17-18 checkpoint execution)
    uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --t7-checkpoint

    # Routing decision (takes domain IDs + signal strengths, outputs Tier 2 activation sequence)
    uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py \\
        --routing-decision 59 51 48 STRONG MODERATE WEAK

    # Activate Tier 2 for a domain with signal strength
    uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py \\
        --activate-tier2 59 STRONG
    uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py \\
        --activate-tier2 51 MODERATE
    uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py \\
        --activate-tier2 48 WEAK

    # Generate guide (stdout only, no WORKLOG entry)
    uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --domain 59 --generate-guide wave1
    uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --domain 51 --generate-guide wave3

Environment variable:
    RESISTANCE_RESEARCH_DIR: path to projects/resistance-research/ (auto-detected if not set)
"""

import argparse
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Domain 51 Configuration
# ---------------------------------------------------------------------------

DOMAIN_51_GIST = "https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372"
DOMAIN_51_DEADLINE = "2026-07-01"
DOMAIN_51_BALLOT_CHECK = "https://ballotpedia.org/California_Public_Funding_of_Elections_Measure_(2026)"
DOMAIN_51_TOPIC = "Campaign Finance / Dark Money Architecture / FEC Enforcement Collapse"
DOMAIN_51_STATE_FILE = "wave_orchestration_state_d51.json"
DOMAIN_51_LOG_FILE = "DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md"

DOMAIN_51_CONTACTS = {
    # Wave 1 — National policy organizations
    1: {
        "wave": 1,
        "org": "Campaign Legal Center",
        "contact_name": "Erin Chlopak",
        "role": "Senior Director, Campaign Finance",
        "primary_email": "echlopak@campaignlegalcenter.org",
        "backup_email": "info@campaignlegal.org",
        "verified_date": "2026-06-11",
        "confidence": "HIGH",
        "domain_hook": "Citizens United / FEC enforcement / Hawaii-Montana charter model",
        "response_probability": "65-75%",
        "notes": (
            "Confirmed via ZoomInfo and CLC legal filing metadata. "
            "Domain quirk: campaignlegalcenter.org (confirmed) vs campaignlegal.org (general inbox). "
            "Adav Noti is Executive Director — Chlopak is the campaign finance program lead."
        ),
    },
    2: {
        "wave": 1,
        "org": "Issue One",
        "contact_name": "General inbox (Nick Penniman, Founder/CEO)",
        "role": "Research team routing",
        "primary_email": "info@issueone.org",
        "backup_email": None,
        "verified_date": "2026-06-05",
        "confidence": "HIGH",
        "domain_hook": "FEC enforcement deadlock / dark money disclosure / DISCLOSE Act",
        "response_probability": "40-60%",
        "notes": (
            "Confirmed at issueone.org/contact. "
            "Penniman is high-profile (TIME100); general inbox routes to policy team. "
            "Cory Combs (ccombs@issueone.org) handles media routing."
        ),
    },
    # Wave 2 — California campaign organizations
    3: {
        "wave": 2,
        "org": "Common Cause California",
        "contact_name": "Darius Kemp",
        "role": "Executive Director (since June 2025)",
        "primary_email": "dkemp@commoncause.org",
        "backup_email": "ca@commoncause.org",
        "cc_email": "info@commoncause.org",
        "verified_date": "2026-06-11",
        "confidence": "HIGH",
        "domain_hook": "California Fair Elections Act ballot campaign / Citizens United workaround",
        "response_probability": "20-30%",
        "notes": (
            "Personnel change: Jonathan Mehta Stein departed; Kemp appointed June 2025. "
            "dkemp@ is confirmed handle. Salutation 'Dear Darius' appropriate."
        ),
    },
    4: {
        "wave": 2,
        "org": "League of Women Voters California",
        "contact_name": "Jenny Farrell",
        "role": "Executive Director",
        "primary_email": "lwvc@lwvc.org",
        "backup_email": None,
        "verified_date": "2026-06-11",
        "confidence": "HIGH",
        "domain_hook": "Voter education / California Fair Elections Act / dark money disclosure",
        "response_probability": "20-30%",
        "notes": (
            "Personnel change: Carol Moon Goldberg no longer listed; Farrell is current ED. "
            "No direct email for Farrell publicly listed — lwvc@lwvc.org is org inbox."
        ),
    },
    5: {
        "wave": 2,
        "org": "Clean Money Action Fund",
        "contact_name": "Trent Lange",
        "role": "President & Executive Director (since 2009)",
        "primary_email": "info@CAclean.org",
        "backup_email": "Trent.Lange@CAclean.org",
        "phone_fallback": "(310) 397-0200",
        "verified_date": "2026-06-11",
        "confidence": "HIGH",
        "domain_hook": "California Fair Elections Act / dark money architecture / campaign operations",
        "response_probability": "5-10%",
        "notes": (
            "CRITICAL: Use info@CAclean.org. Do NOT use cleanmoney.org — unreachable since June 5, 2026. "
            "Trent.Lange@CAclean.org also documented on org About page as direct contact."
        ),
    },
    # Wave 3 — National policy amplifiers (conditional on T+7)
    6: {
        "wave": 3,
        "org": "End Citizens United / Let America Vote",
        "contact_name": "David Donnelly",
        "role": "President & Executive Director",
        "primary_email": "info@endcitizensunited.org",
        "backup_email": None,
        "verified_date": "2026-06-11",
        "confidence": "MEDIUM",
        "domain_hook": "Citizens United litigation and advocacy / DISCLOSE Act / FEC enforcement",
        "response_probability": "30-45%",
        "notes": "ECU and Let America Vote merged operations. Donnelly leads both.",
    },
    7: {
        "wave": 3,
        "org": "Public Citizen Democracy Program",
        "contact_name": "Craig Holman",
        "role": "Policy Advocate, Campaign Finance",
        "primary_email": "cholman@citizen.org",
        "backup_email": None,
        "verified_date": "2026-06-11",
        "confidence": "HIGH",
        "domain_hook": "FEC enforcement / SEC disclosure / AI PAC / DISCLOSE Act",
        "response_probability": "35-50%",
        "notes": (
            "CRITICAL EMAIL QUIRK: cholman@citizen.org is confirmed — shortform handle. "
            "Do NOT use craig.holman@citizen.org."
        ),
    },
    8: {
        "wave": 3,
        "org": "Brennan Center for Justice",
        "contact_name": "Saurav Ghosh",
        "role": "Program Director, Democracy Program",
        "primary_email": "ghoshs@brennan.law.nyu.edu",
        "backup_email": "saurav.ghosh@nyu.edu",
        "verified_date": "2026-06-11",
        "confidence": "HIGH",
        "domain_hook": "Constitutional law / FEC enforcement / Hawaii-Montana charter model / Citizens United",
        "response_probability": "40-55%",
        "notes": "Brennan Center uses NYU law domain format. Salutation 'Dear Saurav' appropriate.",
    },
    9: {
        "wave": 3,
        "org": "Democracy 21",
        "contact_name": "Fred Wertheimer",
        "role": "President & Founder",
        "primary_email": "fwertheimer@democracy21.org",
        "backup_email": None,
        "verified_date": "2026-06-11",
        "confidence": "HIGH",
        "domain_hook": "DISCLOSE Act / FEC quorum repair / campaign finance reform elder statesman",
        "response_probability": "50-65%",
        "notes": (
            "CRITICAL EMAIL QUIRK: fwertheimer@democracy21.org is confirmed — shortform handle. "
            "Not first.last format. Wertheimer publishes weekly newsletter. Salutation 'Dear Fred' appropriate."
        ),
    },
    10: {
        "wave": 3,
        "org": "OpenSecrets",
        "contact_name": "Hilary Braseth (ED, since Jan 2024)",
        "role": "Executive Director",
        "primary_email": "info@opensecrets.org",
        "backup_email": None,
        "verified_date": "2026-06-11",
        "confidence": "HIGH",
        "domain_hook": "Dark money database / 501(c)(4) disclosure gap / AI PAC tracking",
        "response_probability": "30-45%",
        "notes": (
            "Personnel change: Sheila Krumholz departed late 2023. Hilary Braseth is ED since Jan 2024. "
            "info@opensecrets.org still valid."
        ),
    },
}

# ---------------------------------------------------------------------------
# Domain 59 Configuration
# ---------------------------------------------------------------------------

DOMAIN_59_GIST = "https://gist.github.com/esca8peArtist/70b18a6f26dc879e3399c6d147d882ba"
DOMAIN_59_DEADLINE_PRIMARY = "2026-06-30"  # Senate Finance markup
DOMAIN_59_DEADLINE_SECONDARY = "2026-08-01"  # pre-midterm GOTV lock
DOMAIN_59_SENATE_FINANCE_CHECK = "https://www.finance.senate.gov/hearings"
DOMAIN_59_TOPIC = "Economic Precarity / Senate Finance CTC / Democratic Participation"
DOMAIN_59_STATE_FILE = "wave_orchestration_state_d59.json"
DOMAIN_59_SEND_LOG = "domain-59-send-log-june1.md"

DOMAIN_59_CONTACTS = {
    # Wave 1 — Tier 1, highest-leverage Senate Finance / CTC contacts
    1: {
        "wave": 1,
        "org": "AFL-CIO",
        "contact_name": "Jody Calemine (Director of Advocacy) via general inbox",
        "role": "Director of Advocacy / Legislative Affairs",
        "primary_email": "feedback@aflcio.org",
        "backup_email": None,
        "form_fallback": "https://www.aflcio.org/contact",
        "verified_date": "2026-06-10",
        "confidence": "MEDIUM",
        "domain_hook": "Minimum wage / time poverty / CTC and Senate Finance timing",
        "response_probability": "Moderate",
        "notes": (
            "feedback@aflcio.org is standard AFL-CIO general inbox. "
            "ROUTING: add 'For the Legislative Affairs team / Jody Calemine' as first line of body. "
            "Form fallback at aflcio.org/contact if feedback@ bounces."
        ),
    },
    2: {
        "wave": 1,
        "org": "Center on Budget and Policy Priorities",
        "contact_name": "Sharon Parrott",
        "role": "President (since 2021)",
        "primary_email": "cbpp@cbpp.org",
        "backup_email": None,
        "verified_date": "2026-06-10",
        "confidence": "HIGH",
        "domain_hook": "CTC refundability / OBBBA distributional analysis / Senate Finance testimony",
        "response_probability": "55-70%",
        "notes": (
            "CBPP's CTC analysis is the primary citation in Domain 59. "
            "Research-to-research warm — citing their work increases routing to Economic Security team."
        ),
    },
    3: {
        "wave": 1,
        "org": "National Women's Law Center",
        "contact_name": "Emily Martin",
        "role": "Chief Program Officer (since Dec 2023)",
        "primary_email": "info@nwlc.org",
        "backup_email": None,
        "verified_date": "2026-06-10",
        "confidence": "HIGH",
        "domain_hook": "Childcare cost as civic exclusion / gendered democratic deficit / CTC expansion",
        "response_probability": "50-65%",
        "notes": (
            "NWLC has active 'Tell the Senate: Pass the expanded CTC' campaign — warm framing. "
            "Emily Martin confirmed at nwlc.org as CPO since Dec 2023."
        ),
    },
    4: {
        "wave": 1,
        "org": "MomsRising",
        "contact_name": "Kristin Rowe-Finkbeiner",
        "role": "Executive Director, CEO & Co-Founder",
        "primary_email": "info@momsrising.org",
        "backup_email": None,
        "verified_date": "2026-06-10",
        "confidence": "HIGH",
        "domain_hook": "5M+ member network / childcare as civic exclusion / Senate Finance CTC timing",
        "response_probability": "45-60%",
        "notes": (
            "Rowe-Finkbeiner has testified before Senate on childcare affordability. "
            "info@momsrising.org confirmed via org contact page."
        ),
    },
    5: {
        "wave": 1,
        "org": "Institute on Taxation and Economic Policy",
        "contact_name": "Steve Wamhoff",
        "role": "Director of Federal Tax Policy",
        "primary_email": "itep@itep.org",
        "backup_email": None,
        "verified_date": "2026-06-10",
        "confidence": "HIGH",
        "domain_hook": "ITEP '99% of poorest fifth receive $0' stat is primary quantitative claim in Domain 59",
        "response_probability": "55-70%",
        "notes": (
            "Steve Wamhoff confirmed via itep.org/contact. "
            "Opening line citing ITEP's specific finding signals research-to-research correspondence."
        ),
    },
    # Tier 2 — activate T+6 if 2+ Tier 1 STRONG responses
    6: {
        "wave": 2,
        "org": "Economic Policy Institute",
        "contact_name": "Heidi Shierholz",
        "role": "President (since 2021)",
        "primary_email": "researchdept@epi.org",
        "backup_email": None,
        "form_fallback": "https://www.epi.org/about/contact",
        "verified_date": "2026-06-10",
        "confidence": "UNCONFIRMED",
        "domain_hook": "EPI wage/labor data foundational to time-poverty pathway; $30K productivity-pay gap",
        "response_probability": "30-45%",
        "notes": (
            "CRITICAL: researchdept@epi.org is unconfirmed against live contact page. "
            "EPI uses contact form on website. Verify via epi.org/about/contact before send. "
            "Use contact form as primary if direct email not confirmed."
        ),
    },
    7: {
        "wave": 2,
        "org": "Demos",
        "contact_name": "Taifa Smith Butler",
        "role": "President (current — KEY CHANGE from Chiraag Bains who left 2021)",
        "primary_email": "info@demos.org",
        "backup_email": None,
        "verified_date": "2026-06-10",
        "confidence": "HIGH",
        "domain_hook": "Demos mission: 'equal say in democracy + equal chance in economy' — direct overlap",
        "response_probability": "35-50%",
        "notes": (
            "DEAD CONTACT PURGE: Chiraag Bains left Demos in 2021 (Biden White House; now Democracy Fund/Brookings). "
            "Taifa Smith Butler is current president. info@demos.org is unchanged."
        ),
    },
    8: {
        "wave": 2,
        "org": "National Employment Law Project",
        "contact_name": "Rebecca Dixon",
        "role": "President & CEO (since 2020)",
        "primary_email": "info@nelp.org",
        "backup_email": None,
        "verified_date": "2026-06-10",
        "confidence": "HIGH",
        "domain_hook": "Gig economy / worker classification / temporal exclusion from civic participation",
        "response_probability": "35-50%",
        "notes": "info@nelp.org confirmed via nelp.org. Rebecca Dixon confirmed as President & CEO.",
    },
    9: {
        "wave": 2,
        "org": "National Housing Law Project",
        "contact_name": "Policy team",
        "role": "Policy Director (named contact not confirmed — verify on send day)",
        "primary_email": "info@nhlp.org",
        "backup_email": None,
        "verified_date": "2026-06-10",
        "confidence": "HIGH",
        "domain_hook": "Housing cost-burden pathway; one of five causal pathways in Domain 59",
        "response_probability": "20-35%",
        "notes": "Named contact not confirmed — use org inbox. Verify current policy director at nhlp.org on send day.",
    },
    # Tier 3 — activate T+15 after Tier 1/2 signal confirmed
    10: {
        "wave": 3,
        "org": "Common Cause National",
        "contact_name": "Virginia Kase Solomón",
        "role": "President & CEO (since Dec 2023)",
        "primary_email": "commoncause@commoncause.org",
        "backup_email": None,
        "verified_date": "2026-06-10",
        "confidence": "HIGH",
        "domain_hook": "Voting rights + campaign finance networks; post-League of Women Voters leadership",
        "response_probability": "25-40%",
        "notes": (
            "CRITICAL PERSONNEL CHANGE: Prior docs listed Karen Hobert Flynn. "
            "Hobert Flynn DIED March 2023. Virginia Kase Solomón is tenth President (appointed Dec 2023). "
            "kflynn@commoncause.org will hard-bounce. Use commoncause@commoncause.org."
        ),
    },
    11: {
        "wave": 3,
        "org": "People For the American Way",
        "contact_name": "Michael Keegan",
        "role": "President",
        "primary_email": "pfaw@pfaw.org",
        "backup_email": None,
        "verified_date": "2026-06-10",
        "confidence": "HIGH",
        "domain_hook": "Midterm voter engagement / GOTV infrastructure / democratic participation frame",
        "response_probability": "25-40%",
        "notes": "pfaw@pfaw.org confirmed via pfaw.org.",
    },
    12: {
        "wave": 3,
        "org": "Families USA",
        "contact_name": "Frederick Isasi",
        "role": "Executive Director",
        "primary_email": "info@familiesusa.org",
        "backup_email": None,
        "verified_date": "2026-06-10",
        "confidence": "HIGH",
        "domain_hook": "Medicaid work requirements / OBBBA tracking — direct overlap with Domain 59 Medicaid pathway",
        "response_probability": "25-40%",
        "notes": "info@familiesusa.org confirmed via familiesusa.org.",
    },
    13: {
        "wave": 3,
        "org": "Robert Wood Johnson Foundation",
        "contact_name": "Program Officer (health/democracy — named contact not confirmed)",
        "role": "Program Officer",
        "primary_email": "mail@rwjf.org",
        "backup_email": None,
        "verified_date": "2026-06-10",
        "confidence": "HIGH",
        "domain_hook": "Health equity as civic participation framing; RWJF funding priority",
        "response_probability": "15-25%",
        "notes": (
            "mail@rwjf.org confirmed via rwjf.org. "
            "Named contact not confirmed — RWJF has program officer rotation. "
            "Verify specific program officer for democracy/health funding before send."
        ),
    },
}

# ---------------------------------------------------------------------------
# Domain 48 Configuration
# ---------------------------------------------------------------------------

DOMAIN_48_GIST = "https://gist.github.com/esca8peArtist/00c1423e3da7bb4693fa285ec87f18a8"
DOMAIN_48_DEADLINE = "2026-07-15"  # Virginia Right to Vote Coalition integration window
DOMAIN_48_DEADLINE_SECONDARY = "2026-11-03"  # Virginia ballot measure
DOMAIN_48_TOPIC = "Criminal Justice / Civic Exclusion Architecture / Democratic Participation"
DOMAIN_48_STATE_FILE = "wave_orchestration_state_d48.json"
DOMAIN_48_LOG_FILE = "DOMAIN_48_DISTRIBUTION_SEND_LOG_TEMPLATE.md"

DOMAIN_48_CONTACTS = {
    # Wave 1 — Research infrastructure organizations
    1: {
        "wave": 1,
        "org": "The Sentencing Project",
        "contact_name": "Nicole D. Porter",
        "role": "Senior Director of Advocacy",
        "primary_email": "nporter@sentencingproject.org",
        "backup_email": None,
        "form_fallback": "https://www.sentencingproject.org/about/contact-us/",
        "verified_date": "2026-06-05",
        "confidence": "HIGH",
        "domain_hook": (
            "Primary source: 'Locked Out 2024' data; 1-in-22 Black Americans disenfranchisement; "
            "Virginia, Florida, Maryland advocacy priority"
        ),
        "response_probability": "40-60%",
        "notes": (
            "Email format: first_initial + last_name @ sentencingproject.org (91.9% staff format). "
            "Applied: nporter@sentencingproject.org. "
            "Backup: sentencingproject.org/about/contact-us/ form. "
            "HIGHEST PRIORITY — primary data source acknowledgment makes this non-cold outreach."
        ),
    },
    2: {
        "wave": 1,
        "org": "Prison Policy Initiative",
        "contact_name": "Peter Wagner",
        "role": "Executive Director",
        "primary_email": "info@prisonpolicy.org",
        "backup_email": None,
        "verified_date": "2026-06-05",
        "confidence": "HIGH",
        "domain_hook": (
            "'Rigging the Jury' jury exclusion analysis; 'Nowhere to Go' housing barriers; "
            "'Winnable Criminal Justice Reforms in 2026' practitioner framework"
        ),
        "response_probability": "35-50%",
        "notes": (
            "PPI does not publish individual staff emails. info@prisonpolicy.org is verified general inbox. "
            "Check prisonpolicy.org/about for any direct contact before June 17 send. "
            "Secondary contacts: Wendy Sawyer (Research Director), Leah Wang (Senior Research Analyst)."
        ),
    },
    # Wave 2 — Advocacy and litigation partners
    3: {
        "wave": 2,
        "org": "Brennan Center for Justice — Voting Rights and Elections Program",
        "contact_name": "Sean Morales-Doyle",
        "role": "Director, Voting Rights and Elections Program",
        "primary_email": None,
        "backup_email": None,
        "form_fallback": "https://www.brennancenter.org/about/contact",
        "verified_date": "2026-06-05",
        "confidence": "HIGH",
        "domain_hook": (
            "Readmission Act constitutional theory (Section 4.4); post-King v. O'Bannon strategy; "
            "Virginia voting rights restoration; LFO equal protection"
        ),
        "response_probability": "25-40%",
        "notes": (
            "Brennan Center does NOT publish individual staff emails. "
            "Contact pathway: brennancenter.org/about/contact (web inquiry form) — specify Voting Rights and Elections Program. "
            "PERSONNEL NOTE: Myrna Pérez left Oct 2021 (now Second Circuit judge). Sean Morales-Doyle is current director. "
            "VP supervising: Wendy R. Weiser (wweiser@brennan.law.nyu.edu)."
        ),
    },
    4: {
        "wave": 2,
        "org": "Worth Rises",
        "contact_name": "Bianca Tylek",
        "role": "Executive Director and Founder",
        "primary_email": "info@worthrises.org",
        "backup_email": "press@worthrises.org",
        "verified_date": "2026-06-05",
        "confidence": "HIGH",
        "domain_hook": (
            "LFO research primary source: 83% of formerly incarcerated carry court debt, avg $13,607; "
            "Florida Amendment 4 poll tax analysis; prison industrial complex financial flows"
        ),
        "response_probability": "40-55%",
        "notes": (
            "info@worthrises.org confirmed via worthrises.org. "
            "Secondary contacts: Antonya Jeffrey (Director of Policy Campaigns), Peter Mayer (Director of Research). "
            "HIGHEST ALIGNMENT — Domain 48 Section 4 (LFO as poll tax) relies on Worth Rises as primary empirical source."
        ),
    },
    5: {
        "wave": 2,
        "org": "Campaign Legal Center — Restore Your Vote",
        "contact_name": "Blair Bowie",
        "role": "Director, Restore Your Vote",
        "primary_email": "info@campaignlegal.org",
        "backup_email": None,
        "verified_date": "2026-06-05",
        "confidence": "HIGH",
        "domain_hook": (
            "Restore Your Vote direct services; Florida LFO poll tax litigation; "
            "Virginia post-King v. O'Bannon implementation; Readmission Act theory"
        ),
        "response_probability": "25-40%",
        "notes": (
            "Use info@campaignlegal.org — specify 'Restore Your Vote program' in subject line. "
            "DOMAIN OVERLAP NOTE: Domain 51's CLC contact is Adav Noti (campaign finance). "
            "Domain 48's CLC contact is Blair Bowie (Restore Your Vote). Different staff, no conflict."
        ),
    },
    6: {
        "wave": 2,
        "org": "Movement for Black Lives",
        "contact_name": "Policy Table",
        "role": "Policy team (named current contact — verify at m4bl.org/contact before sending)",
        "primary_email": "info@m4bl.org",
        "backup_email": None,
        "form_fallback": "https://m4bl.org/contact",
        "verified_date": "2026-06-05",
        "confidence": "MEDIUM",
        "domain_hook": (
            "Structural racial justice and abolitionist democracy framework; "
            "Virginia Right to Vote Coalition network (M4BL Virginia affiliates); "
            "Alabama, Florida, Mississippi, Georgia high-disenfranchisement state networks"
        ),
        "response_probability": "15-30%",
        "notes": (
            "policy@m4bl.org may not be current — verify at m4bl.org/contact before sending. "
            "info@m4bl.org is safer fallback. Decentralized coalition org with variable inbox routing. "
            "CONTINGENCY: if M4BL unresponsive by July 10, activate ACLU of Virginia (acluva@acluva.org) "
            "as Virginia Right to Vote Coalition bridge to M4BL Virginia affiliates."
        ),
    },
    # Tier 2 — activate on strong signal from Wave 1-2
    7: {
        "wave": 3,
        "org": "NAACP Legal Defense Fund",
        "contact_name": "Janai Nelson",
        "role": "President and Director-Counsel (since March 2022)",
        "primary_email": "info@naacpldf.org",
        "backup_email": None,
        "verified_date": "2026-06-05",
        "confidence": "HIGH",
        "domain_hook": (
            "Felony disenfranchisement litigation; LFO equal protection; Eleventh Circuit SB 7066; "
            "Readmission Act applicability to other former Confederate states"
        ),
        "response_probability": "20-35%",
        "notes": (
            "Activate after Day 7 checkpoint ONLY if Tier A/B sends return 2+ STRONG. "
            "LDF is a relationship organization — warm follow-on framing after Sentencing Project engagement. "
            "Do not send cold without prior Tier A/B engagement."
        ),
    },
    8: {
        "wave": 3,
        "org": "Fines and Fees Justice Center",
        "contact_name": "Joanna Weiss",
        "role": "Co-Executive Director",
        "primary_email": "info@finesandfeesjusticecenter.org",
        "backup_email": None,
        "verified_date": "2026-06-05",
        "confidence": "MEDIUM",
        "domain_hook": (
            "LFO/court fees as voter suppression mechanism; Florida Amendment 4 poll tax; "
            "state legislative campaigns on fines and fees reform"
        ),
        "response_probability": "30-45%",
        "notes": (
            "jweiss@finesandfeesjusticecenter.org is likely direct address (standard FLast@ format) — "
            "verify before use. info@finesandfeesjusticecenter.org is confirmed general inbox. "
            "Can activate with Worth Rises on Wave 2 as co-distribution partner for Section 4 poll tax material."
        ),
    },
    9: {
        "wave": 3,
        "org": "ACLU of Virginia",
        "contact_name": "Mary Bauer",
        "role": "Executive Director",
        "primary_email": "acluva@acluva.org",
        "backup_email": None,
        "verified_date": "2026-06-05",
        "confidence": "HIGH",
        "domain_hook": (
            "Virginia Right to Vote Coalition member; King v. Youngkin precedent; "
            "November 3 ballot measure campaign; M4BL Virginia affiliate bridge"
        ),
        "response_probability": "30-45%",
        "notes": (
            "Contingency path — use if M4BL national contact does not respond by July 10. "
            "Chris Kaiser (Policy Director) is also a valid contact. "
            "acluva@acluva.org confirmed via acluva.org. "
            "ACLU Virginia is confirmed Virginia Right to Vote Coalition member — "
            "can route materials to M4BL Virginia affiliates and broader coalition."
        ),
    },
}

# ---------------------------------------------------------------------------
# Domain dispatch table
# ---------------------------------------------------------------------------

DOMAINS = {
    48: {
        "name": "Domain 48",
        "topic": DOMAIN_48_TOPIC,
        "gist_url": DOMAIN_48_GIST,
        "deadline": DOMAIN_48_DEADLINE,
        "check_url": "https://ballotpedia.org/Virginia_Voting_Rights_Restoration_Amendment_(2026)",
        "state_file": DOMAIN_48_STATE_FILE,
        "log_file": DOMAIN_48_LOG_FILE,
        "contacts": DOMAIN_48_CONTACTS,
        "waves": {
            1: "Research infrastructure (Sentencing Project, PPI)",
            2: "Advocacy and litigation partners (Brennan Center, Worth Rises, CLC/RYV, M4BL)",
            3: "Tier 2 — conditional on T+7 signal (NAACP LDF, FFJC, ACLU VA)",
        },
        "t7_gate": {"full": 2, "conditional": 1, "weak": 0},
        "priority_note": (
            "Domain 48 executes after Domain 59 and 51. Virginia Right to Vote Coalition "
            "integration deadline July 15 — all Tier 2 sends must initiate by June 27."
        ),
    },
    51: {
        "name": "Domain 51",
        "topic": DOMAIN_51_TOPIC,
        "gist_url": DOMAIN_51_GIST,
        "deadline": DOMAIN_51_DEADLINE,
        "check_url": DOMAIN_51_BALLOT_CHECK,
        "state_file": DOMAIN_51_STATE_FILE,
        "log_file": DOMAIN_51_LOG_FILE,
        "contacts": DOMAIN_51_CONTACTS,
        "waves": {1: "National policy orgs (CLC, Issue One)", 2: "California campaign orgs", 3: "National amplifiers (conditional on T+7)"},
        "t7_gate": {"full": 4, "conditional": 2, "weak": 1},
        "priority_note": "Domain 51 executes AFTER Domain 59 when both approved simultaneously.",
    },
    59: {
        "name": "Domain 59",
        "topic": DOMAIN_59_TOPIC,
        "gist_url": DOMAIN_59_GIST,
        "deadline": DOMAIN_59_DEADLINE_PRIMARY,
        "check_url": DOMAIN_59_SENATE_FINANCE_CHECK,
        "state_file": DOMAIN_59_STATE_FILE,
        "log_file": DOMAIN_59_SEND_LOG,
        "contacts": DOMAIN_59_CONTACTS,
        "waves": {1: "Tier 1 — Senate Finance / CTC core (5 contacts)", 2: "Tier 2 — conditional on 2+ Tier 1 STRONG", 3: "Tier 3 — activate T+15 after confirmation"},
        "t7_gate": {"full": 3, "conditional": 2, "weak": 1},
        "priority_note": "Domain 59 executes FIRST when both domains approved simultaneously (Senate Finance markup closes June 25-30).",
    },
}

# ---------------------------------------------------------------------------
# Path resolution
# ---------------------------------------------------------------------------

def get_research_dir() -> Path:
    """Resolve the resistance-research directory."""
    import os
    env_dir = os.environ.get("RESISTANCE_RESEARCH_DIR")
    if env_dir:
        return Path(env_dir)
    script_dir = Path(__file__).parent
    if script_dir.name == "resistance-research":
        return script_dir
    for parent in [script_dir] + list(script_dir.parents):
        candidate = parent / "projects" / "resistance-research"
        if candidate.is_dir():
            return candidate
    return script_dir


RESEARCH_DIR = get_research_dir()
WORKLOG_PATH = RESEARCH_DIR / "WORKLOG.md"


def get_state_path(domain_id: int) -> Path:
    state_file = DOMAINS[domain_id]["state_file"]
    return RESEARCH_DIR / "phase-1-adoption" / "data" / state_file


# ---------------------------------------------------------------------------
# State management
# ---------------------------------------------------------------------------

def load_state(domain_id: int) -> dict:
    """Load send state from disk for a given domain."""
    state_path = get_state_path(domain_id)
    state_path.parent.mkdir(parents=True, exist_ok=True)
    if state_path.exists():
        try:
            with open(state_path) as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
    return {
        "domain": domain_id,
        "sends": {},
        "bounces": {},
        "replies": {},
        "created": datetime.now(timezone.utc).isoformat(),
    }


def save_state(domain_id: int, state: dict) -> None:
    """Persist state to disk for a given domain."""
    state_path = get_state_path(domain_id)
    state_path.parent.mkdir(parents=True, exist_ok=True)
    with open(state_path, "w") as f:
        json.dump(state, f, indent=2)


# ---------------------------------------------------------------------------
# WORKLOG writer
# ---------------------------------------------------------------------------

def append_worklog(domain_id: int, entry: str) -> None:
    """Append a timestamped entry to WORKLOG.md."""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    block = f"\n---\n\n## {now} — Domain {domain_id} Wave Orchestration\n\n{entry.strip()}\n"
    try:
        with open(WORKLOG_PATH, "a") as f:
            f.write(block)
        print(f"[worklog] Entry appended to {WORKLOG_PATH}")
    except IOError as e:
        print(f"[warn] Could not write to WORKLOG.md: {e}", file=sys.stderr)


# ---------------------------------------------------------------------------
# Status display
# ---------------------------------------------------------------------------

def cmd_status(domain_id: int, state: dict) -> None:
    """Print current execution status for all contacts in a domain."""
    domain = DOMAINS[domain_id]
    contacts = domain["contacts"]
    now = datetime.now(timezone.utc)

    try:
        deadline_dt = datetime.fromisoformat(domain["deadline"]).replace(tzinfo=timezone.utc)
        days_remaining = (deadline_dt - now).days
    except ValueError:
        days_remaining = "?"

    print(f"\n=== {domain['name']} — Wave Execution Status ===")
    print(f"Topic:    {domain['topic']}")
    print(f"Date:     {now.strftime('%Y-%m-%d %H:%M UTC')}")
    print(f"Deadline: {domain['deadline']} ({days_remaining} days remaining)")
    print(f"Gist URL: {domain['gist_url']}")
    print(f"Priority: {domain['priority_note']}")
    print()

    for send_num in sorted(contacts):
        contact = contacts[send_num]
        send_record = state["sends"].get(str(send_num), {})
        bounce_record = state["bounces"].get(str(send_num), {})
        reply_record = state["replies"].get(str(send_num), {})

        sent = bool(send_record)
        bounced = bool(bounce_record)
        replied = bool(reply_record)

        status = "PENDING"
        if sent and not bounced:
            status = "SENT"
        elif sent and bounced and send_record.get("fallback_sent"):
            status = "SENT (via fallback)"
        elif sent and bounced:
            status = "BOUNCED — action required"

        reply_label = "—"
        if replied:
            reply_label = reply_record.get("signal", "LOGGED")

        wave_label = f"Wave {contact['wave']}"
        print(
            f"  Send {send_num:2d} | {wave_label} | {contact['org']}\n"
            f"           Contact: {contact['contact_name']} <{contact['primary_email']}>\n"
            f"           Status:  {status}\n"
            f"           Reply:   {reply_label}"
        )
        if sent:
            print(f"           Sent at: {send_record.get('timestamp', 'unknown')}")
        print()

    # T+7 summary from Wave 1 sends
    wave1_keys = [k for k, c in contacts.items() if c["wave"] == 1]
    sent_timestamps = [
        state["sends"][str(k)]["timestamp"]
        for k in wave1_keys
        if str(k) in state["sends"]
    ]
    if sent_timestamps:
        earliest = min(sent_timestamps)
        print(f"Wave 1 first send:  {earliest}")
        try:
            wave1_dt = datetime.fromisoformat(earliest.replace(" UTC", "+00:00"))
            t7 = wave1_dt + timedelta(days=7)
            t14 = wave1_dt + timedelta(days=14)
            print(f"T+7 checkpoint:     {t7.strftime('%Y-%m-%d')}")
            print(f"T+14 checkpoint:    {t14.strftime('%Y-%m-%d')}")
        except ValueError:
            pass
    print()


def cmd_all_domains_status() -> None:
    """Print summary status for all three domains side by side."""
    print("\n=== Multi-Domain Status Summary ===")
    print(f"Date: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    print()
    print("SEQUENCING RULE: Domain 59 → Domain 51 → Domain 48")
    print("  D59: Senate Finance markup closes June 25-30 (hardest deadline)")
    print("  D51: California ballot deadline July 1")
    print("  D48: Virginia Right to Vote Coalition integration July 15")
    print()
    for domain_id in [59, 51, 48]:
        state = load_state(domain_id)
        domain = DOMAINS[domain_id]
        contacts = domain["contacts"]
        total = len(contacts)
        sent = sum(1 for k in contacts if str(k) in state["sends"])
        strong = sum(1 for r in state["replies"].values() if r.get("signal") == "STRONG")
        moderate = sum(1 for r in state["replies"].values() if r.get("signal") == "MODERATE")
        print(f"Domain {domain_id} ({domain['topic'][:55]})")
        print(f"  Sends completed: {sent}/{total}")
        print(f"  STRONG replies:  {strong}")
        print(f"  MODERATE replies:{moderate}")
        print(f"  Deadline:        {domain['deadline']}")
        print()


# ---------------------------------------------------------------------------
# Sequence check
# ---------------------------------------------------------------------------

def cmd_sequence_check() -> None:
    """Print the activation sequence recommendation and rationale."""
    print("\n=== Phase 2 Activation Sequence Recommendation ===")
    print()
    print("EXECUTE IN THIS ORDER when both domains approved at June 17-18 checkpoint:")
    print()
    print("  Day 0 (checkpoint day):  Domain 59 Wave 1 — AFL-CIO, CBPP, NWLC, MomsRising, ITEP")
    print("    Active time:           ~60 minutes | Clock time: ~3.5 hours (45-min stagger)")
    print("    Rationale:             Senate Finance markup closes June 25-30. This is an immovable deadline.")
    print()
    print("  Day 1 (next morning):    Domain 51 Wave 1 — CLC (Chlopak), Issue One")
    print("    Active time:           ~30-45 minutes | Clock time: ~2 hours (90-min stagger)")
    print("    Rationale:             California ballot deadline July 1 — 5 days after Domain 59 Senate window.")
    print()
    print("  Day 1 (afternoon):       Domain 51 Wave 2 — Common Cause CA, LWV CA, Clean Money")
    print("    Active time:           ~45-60 minutes | Clock time: ~3 hours (90-min stagger)")
    print()
    print("  Day 6 (T+6 after D59):   Domain 59 Tier 2 — IF 2+ STRONG from Tier 1")
    print("    Contacts:              EPI, Demos, NELP, NHLP")
    print()
    print("  Day 7 (T+7 gate):        Assess both domains. Run --t7-check for each.")
    print()
    print("Reference: DOMAINS_51_59_SEQUENTIAL_ACTIVATION_TIMING.md")
    print()


# ---------------------------------------------------------------------------
# Execution guide generators
# ---------------------------------------------------------------------------

def _contact_block(send_num: int, contact: dict, gist_url: str, domain_id: int) -> str:
    """Generate a compact execution block for a single contact."""
    fallback_note = ""
    if contact.get("backup_email"):
        fallback_note = f"\n  Backup:  {contact['backup_email']}"
    elif contact.get("form_fallback"):
        fallback_note = f"\n  Fallback: {contact['form_fallback']} (form)"
    if contact.get("notes"):
        note_text = f"\n  NOTE:    {contact['notes'][:200]}"
    else:
        note_text = ""
    return (
        f"SEND {send_num} — {contact['org']}\n"
        f"  To:      {contact['primary_email']}{fallback_note}\n"
        f"  Contact: {contact['contact_name']}\n"
        f"  Hook:    {contact['domain_hook']}\n"
        f"  P(reply): {contact['response_probability']}{note_text}\n"
        f"  Gist:    {gist_url}\n"
    )


def generate_wave_guide(domain_id: int, wave: int) -> str:
    """Generate a self-contained execution guide for a given domain wave."""
    domain = DOMAINS[domain_id]
    contacts = domain["contacts"]
    wave_contacts = {k: v for k, v in contacts.items() if v["wave"] == wave}

    if not wave_contacts:
        return f"[error] No contacts defined for Domain {domain_id} Wave {wave}."

    wave_label = domain["waves"].get(wave, f"Wave {wave}")
    stagger = 90 if domain_id == 51 else 45

    lines = [
        f"=== DOMAIN {domain_id} WAVE {wave} EXECUTION GUIDE (generated) ===",
        f"Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        f"Topic:     {domain['topic']}",
        f"Gist URL:  {domain['gist_url']}",
        f"Wave:      {wave_label}",
        f"Stagger:   {stagger} minutes between sends",
        "",
        f"PRE-FLIGHT: Confirm Gist resolves: {domain['gist_url']}",
        f"PRE-FLIGHT: Check {domain['check_url']}",
        "",
    ]

    for i, (send_num, contact) in enumerate(sorted(wave_contacts.items())):
        timing = f"T+0" if i == 0 else f"T+{i * stagger} min"
        lines.append(f"--- {timing} ---")
        lines.append(_contact_block(send_num, contact, domain["gist_url"], domain_id))
        if i < len(wave_contacts) - 1:
            lines.append(f"[After Send {send_num}]: Wait {stagger} minutes.")
        else:
            lines.append(f"[After Send {send_num}]: Wave {wave} complete. Log all sends.")
        lines.append("")

    lines.append(f"Full execution package: DOMAIN_{domain_id}_WAVE_1_EMAIL_EXECUTION_PACKAGE.md")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Execute command
# ---------------------------------------------------------------------------

def cmd_execute(domain_id: int, wave_arg: str, state: dict) -> None:
    """Print execution guide and log intent to WORKLOG."""
    domain = DOMAINS[domain_id]
    contacts = domain["contacts"]
    waves_to_run = []

    if wave_arg == "all":
        waves_to_run = sorted(set(c["wave"] for c in contacts.values()))
    elif wave_arg.startswith("wave"):
        try:
            w = int(wave_arg.replace("wave", ""))
            waves_to_run = [w]
        except ValueError:
            print(f"[error] Unknown wave: {wave_arg}", file=sys.stderr)
            sys.exit(1)
    else:
        print(f"[error] Unknown wave argument: {wave_arg}", file=sys.stderr)
        sys.exit(1)

    for wave in waves_to_run:
        guide = generate_wave_guide(domain_id, wave)
        print(guide)
        wave_contacts = {k: v for k, v in contacts.items() if v["wave"] == wave}
        contact_lines = "\n".join(
            f"- Send {k}: {v['contact_name']} / {v['org']} ({v['primary_email']})"
            for k, v in sorted(wave_contacts.items())
        )
        worklog_entry = (
            f"**Action**: Domain {domain_id} Wave {wave} execution guide generated.\n\n"
            f"**Contacts**:\n{contact_lines}\n\n"
            f"**Next step**: User executes sends with {45 if domain_id == 59 else 90}-minute stagger. "
            f"Log results with --domain {domain_id} --log-send after each send."
        )
        append_worklog(domain_id, worklog_entry)

    save_state(domain_id, state)


def cmd_generate_guide(domain_id: int, wave_arg: str) -> None:
    """Print a self-contained execution guide to stdout (no WORKLOG entry)."""
    try:
        wave = int(wave_arg.replace("wave", ""))
    except (ValueError, AttributeError):
        print(f"[error] Unknown wave: {wave_arg}. Use 'wave1', 'wave2', 'wave3'.", file=sys.stderr)
        sys.exit(1)
    print(generate_wave_guide(domain_id, wave))


# ---------------------------------------------------------------------------
# Log send
# ---------------------------------------------------------------------------

def cmd_log_send(domain_id: int, send_num: int, timestamp: str, state: dict) -> None:
    """Record that a send was completed at a given timestamp."""
    contacts = DOMAINS[domain_id]["contacts"]
    contact = contacts.get(send_num)
    if not contact:
        valid = sorted(contacts.keys())
        print(f"[error] Unknown send number: {send_num}. Valid for Domain {domain_id}: {valid}", file=sys.stderr)
        sys.exit(1)

    record = {
        "send_num": send_num,
        "org": contact["org"],
        "email": contact["primary_email"],
        "timestamp": timestamp,
        "logged_at": datetime.now(timezone.utc).isoformat(),
        "fallback_sent": False,
    }
    state["sends"][str(send_num)] = record
    save_state(domain_id, state)

    worklog_entry = (
        f"**Send {send_num} logged**: {contact['org']}\n\n"
        f"- Email: {contact['primary_email']}\n"
        f"- Sent at: {timestamp}\n"
        f"- Reply status: PENDING\n\n"
        f"Wave {contact['wave']} | Contact: {contact['contact_name']}"
    )
    append_worklog(domain_id, worklog_entry)

    print(f"[ok] Domain {domain_id} Send {send_num} logged: {contact['org']} at {timestamp}")

    # Advise on next step
    stagger = 45 if domain_id == 59 else 90
    next_num = send_num + 1
    if next_num in contacts:
        next_contact = contacts[next_num]
        if next_contact["wave"] == contact["wave"]:
            print(f"[next] Wait {stagger} minutes, then send Send {next_num}: {next_contact['org']} ({next_contact['primary_email']})")
        else:
            print(f"[next] Wave {contact['wave']} complete. Wave {next_contact['wave']} activates after T+7 gate (2+ STRONG required).")
    else:
        print("[next] All sends logged. Set T+7 calendar reminder.")


# ---------------------------------------------------------------------------
# Log bounce
# ---------------------------------------------------------------------------

def cmd_log_bounce(domain_id: int, send_num: int, use_fallback: bool, state: dict) -> None:
    """Record a bounce and optionally note fallback was sent."""
    contacts = DOMAINS[domain_id]["contacts"]
    contact = contacts.get(send_num)
    if not contact:
        print(f"[error] Unknown send number: {send_num} for Domain {domain_id}.", file=sys.stderr)
        sys.exit(1)

    fallback = contact.get("backup_email")
    if not fallback:
        fallback = contact.get("form_fallback")

    bounce_record = {
        "send_num": send_num,
        "org": contact["org"],
        "bounced_address": contact["primary_email"],
        "fallback_address": fallback,
        "fallback_sent": use_fallback and bool(fallback),
        "logged_at": datetime.now(timezone.utc).isoformat(),
    }
    state["bounces"][str(send_num)] = bounce_record

    if str(send_num) in state["sends"]:
        state["sends"][str(send_num)]["fallback_sent"] = bounce_record["fallback_sent"]

    save_state(domain_id, state)

    worklog_entry = (
        f"**Send {send_num} BOUNCE**: {contact['org']}\n\n"
        f"- Bounced: {contact['primary_email']}\n"
        f"- Fallback: {fallback if fallback else 'none available'}\n"
        f"- Fallback sent: {'YES' if bounce_record['fallback_sent'] else 'NO'}"
    )
    append_worklog(domain_id, worklog_entry)

    if bounce_record["fallback_sent"]:
        print(f"[ok] Bounce logged for Domain {domain_id} Send {send_num}. Fallback sent to: {fallback}")
    elif fallback:
        print(f"[warn] Bounce logged for Domain {domain_id} Send {send_num}. Fallback available: {fallback}")
        print(f"       Resend to {fallback}, then run: --domain {domain_id} --log-bounce {send_num} --fallback")
    else:
        print(f"[warn] Bounce logged for Domain {domain_id} Send {send_num}. No backup address available.")
        print(f"       Notes: {contact.get('notes', 'see contact audit')}")


# ---------------------------------------------------------------------------
# Log reply
# ---------------------------------------------------------------------------

def cmd_log_reply(domain_id: int, send_num: int, signal: str, summary: str, state: dict) -> None:
    """Record a reply for a given send number."""
    valid_signals = {"STRONG", "MODERATE", "WEAK", "NONE"}
    if signal not in valid_signals:
        print(f"[error] Signal must be one of: {', '.join(sorted(valid_signals))}", file=sys.stderr)
        sys.exit(1)

    contacts = DOMAINS[domain_id]["contacts"]
    contact = contacts.get(send_num)
    if not contact:
        print(f"[error] Unknown send number: {send_num} for Domain {domain_id}.", file=sys.stderr)
        sys.exit(1)

    reply_record = {
        "send_num": send_num,
        "org": contact["org"],
        "signal": signal,
        "summary": summary,
        "logged_at": datetime.now(timezone.utc).isoformat(),
    }
    state["replies"][str(send_num)] = reply_record
    save_state(domain_id, state)

    action_guidance = {
        "STRONG": (
            "Reply within 24 hours. "
            "Offer to send a one-page summary for internal distribution. "
            "This is a Phase 2 gate signal."
        ),
        "MODERATE": (
            "Log in execution log. "
            "If reply includes a named contact, note for next-wave follow-up."
        ),
        "WEAK": (
            "Log in execution log. "
            "If 'unsubscribe' or 'please remove,' do not contact that address again."
        ),
        "NONE": "No action needed. Continue to Day 14 before drawing conclusions.",
    }

    worklog_entry = (
        f"**Reply received — Domain {domain_id} Send {send_num}**: {contact['org']}\n\n"
        f"- Signal: {signal}\n"
        f"- Summary: {summary}\n"
        f"- Action: {action_guidance[signal]}"
    )
    append_worklog(domain_id, worklog_entry)

    print(f"[ok] Domain {domain_id} Reply logged: Send {send_num} — {signal}")
    print(f"     {action_guidance[signal]}")

    strong_count = sum(1 for r in state["replies"].values() if r.get("signal") == "STRONG")
    gate = DOMAINS[domain_id]["t7_gate"]
    total_wave1 = sum(1 for c in contacts.values() if c["wave"] == 1)
    print(f"\n[gate] Domain {domain_id} STRONG reply count: {strong_count}/{total_wave1}")
    if strong_count >= gate["full"]:
        print(f"       FULL ACTIVATION threshold met ({gate['full']}+ STRONG). Activate Tier 2 and 3.")
    elif strong_count >= gate["conditional"]:
        print(f"       CONDITIONAL threshold met ({gate['conditional']}+ STRONG). Activate Tier 2; hold Tier 3.")
    else:
        print(f"       Below threshold. Continue monitoring to Day 14.")


# ---------------------------------------------------------------------------
# T+7 checkpoint
# ---------------------------------------------------------------------------

def cmd_t7_check(domain_id: int, state: dict) -> None:
    """Assess the T+7 checkpoint status for a domain."""
    domain = DOMAINS[domain_id]
    contacts = domain["contacts"]
    gate = domain["t7_gate"]
    wave1_contacts = {k: v for k, v in contacts.items() if v["wave"] == 1}

    print(f"\n=== Domain {domain_id} T+7 Checkpoint Assessment ===")
    print(f"Checked: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}\n")

    sends_logged = len(state["sends"])
    replies_logged = len(state["replies"])
    strong_count = sum(1 for r in state["replies"].values() if r.get("signal") == "STRONG")
    bounce_count = len(state["bounces"])
    total = len(contacts)

    print(f"Sends logged:     {sends_logged}/{total}")
    print(f"Bounces:          {bounce_count}")
    print(f"Replies logged:   {replies_logged}")
    print(f"STRONG signals:   {strong_count}")
    print()

    wave1_keys = list(wave1_contacts.keys())
    wave1_sent = sum(1 for k in wave1_keys if str(k) in state["sends"])
    if wave1_sent < len(wave1_keys):
        pending = [k for k in wave1_keys if str(k) not in state["sends"]]
        print(f"[warn] Not all Wave 1 sends completed. Pending: {pending}")
        print(f"       Execute remaining sends before assessing T+7 results.")
        return

    print("Phase 2 gate decision:")
    if strong_count >= gate["full"]:
        print(f"  FULL ACTIVATION — {gate['full']}+ STRONG signals.")
        print(f"  Action: Activate all remaining waves for Domain {domain_id}.")
    elif strong_count >= gate["conditional"]:
        print(f"  CONDITIONAL APPROVAL — {gate['conditional']}+ STRONG signals.")
        print(f"  Action: Activate Wave 2 contacts sequentially. Hold Wave 3 for secondary checkpoint.")
    elif strong_count >= gate["weak"]:
        print(f"  WEAK THRESHOLD — 1 STRONG signal.")
        print(f"  Action: Continue monitoring to Day 14 before activating next wave.")
    else:
        print(f"  BELOW THRESHOLD — 0 STRONG signals.")
        print(f"  Action: Hold. User decision required. Consider Day 14 follow-up to highest-probability contacts.")

    print()
    worklog_entry = (
        f"**T+7 checkpoint run — Domain {domain_id}**\n\n"
        f"- Sends logged: {sends_logged}/{total}\n"
        f"- Bounces: {bounce_count}\n"
        f"- Replies: {replies_logged}\n"
        f"- STRONG signals: {strong_count}\n\n"
        f"Gate decision: see console output."
    )
    append_worklog(domain_id, worklog_entry)


# ---------------------------------------------------------------------------
# T+7 multi-domain checkpoint (--t7-checkpoint)
# ---------------------------------------------------------------------------

# Threshold tables grounded in PHASE_2_T7_ROUTING_DECISION_TREE.md Section 1.1
_T7_THRESHOLDS = {
    # domain_id: (strong_for_strong, strong_for_moderate, notes)
    59: (2, 1, "FORCED activation if Senate Finance markup still active regardless of signal"),
    51: (2, 1, "CLC reply (any quality) auto-elevates to MODERATE"),
    48: (2, 1, "Sentencing Project reply (any quality) auto-elevates to MODERATE"),
}

_TIER2_CONTACTS = {
    59: {
        "STRONG": [
            ("EPI — Heidi Shierholz", "researchdept@epi.org (UNCONFIRMED — verify via epi.org/about/contact)"),
            ("Demos — Taifa Smith Butler", "info@demos.org"),
            ("NELP — Rebecca Dixon", "info@nelp.org"),
            ("NHLP — Policy team", "info@nhlp.org"),
        ],
        "MODERATE": [
            ("EPI — Heidi Shierholz", "researchdept@epi.org (UNCONFIRMED — verify first)"),
            ("NELP — Rebecca Dixon", "info@nelp.org"),
        ],
        "WEAK": [
            ("EPI — Heidi Shierholz", "researchdept@epi.org (UNCONFIRMED)"),
            ("Demos — Taifa Smith Butler", "info@demos.org"),
            ("NELP — Rebecca Dixon", "info@nelp.org"),
            ("NOTE: FORCED activation — Senate markup deadline", ""),
        ],
    },
    51: {
        "STRONG": [
            ("True North Research — Lisa Graves", "info@truenorthresearch.org"),
            ("Montana I-194 Campaign", "via ballotpedia.org (verify current contact)"),
            ("Michigan Clean Elections Coalition", "via michiganadvance.com"),
            ("+ Secondary 5 after 48h: NM Common Cause, Issue One ReFormers, ACLU VRP, Hasen, Levitt", ""),
            ("+ Extended 5 after signal: ECU, Public Citizen, Brennan, Democracy 21, OpenSecrets", ""),
        ],
        "MODERATE": [
            ("True North Research — Lisa Graves", "info@truenorthresearch.org"),
            ("Montana I-194 Campaign", "via ballotpedia.org"),
            ("Michigan Clean Elections Coalition", "via michiganadvance.com"),
            ("+ Secondary 5 after 48h (hold extended 5 for Day 14)", ""),
        ],
        "WEAK": [
            ("True North Research — Lisa Graves", "info@truenorthresearch.org"),
            ("Montana I-194 Campaign", "via ballotpedia.org"),
            ("Michigan Clean Elections Coalition", "via michiganadvance.com"),
            ("Hold secondary 5 and extended 5; Day 14 CLC follow-up", ""),
        ],
    },
    48: {
        "STRONG": [
            ("NAACP LDF — Janai Nelson", "info@naacpldf.org"),
            ("Fines and Fees Justice Center — Joanna Weiss", "info@finesandfeesjusticecenter.org"),
            ("ACLU of Virginia — Mary Bauer (June 27)", "acluva@acluva.org"),
        ],
        "MODERATE": [
            ("Fines and Fees Justice Center — Joanna Weiss", "info@finesandfeesjusticecenter.org"),
            ("ACLU of Virginia — Mary Bauer (June 27, if M4BL unresponsive)", "acluva@acluva.org"),
        ],
        "WEAK": [
            ("ACLU of Virginia — Mary Bauer (contingency path)", "acluva@acluva.org"),
            ("Hold NAACP LDF until warm introduction via ACLU VA", ""),
        ],
    },
}


def _classify_signal(domain_id: int, state: dict) -> str:
    """Classify domain signal as STRONG, MODERATE, WEAK, or DIAGNOSTIC.

    Grounded in PHASE_2_T7_ROUTING_DECISION_TREE.md Section 1.1.
    Delivery rate is calculated against Wave 1 contacts only. At the Day 7 checkpoint,
    only Wave 1 contacts are expected to have been sent. Wave 2/3 (Tier 2/3) contacts
    activate based on signal strength — they are not in the delivery rate denominator.
    """
    contacts = DOMAINS[domain_id]["contacts"]
    wave1_contacts = {k: c for k, c in contacts.items() if c["wave"] == 1}
    wave1_total = len(wave1_contacts)
    # Only count Wave 1 sends for delivery rate
    wave1_sent = sum(1 for k in wave1_contacts if str(k) in state["sends"])
    wave1_bounced = sum(1 for k in wave1_contacts if str(k) in state["bounces"])
    delivered = max(0, wave1_sent - wave1_bounced)
    # If no Wave 1 sends logged at all, we cannot assess delivery (not yet sent)
    # Only flag DIAGNOSTIC if Wave 1 sends exist but delivery rate is low
    if wave1_sent == 0:
        delivery_rate = 1.0  # not yet sent — do not flag DIAGNOSTIC
    else:
        delivery_rate = (delivered / wave1_total) if wave1_total > 0 else 1.0
    sent_count = len(state["sends"])
    bounce_count = len(state["bounces"])

    if delivery_rate < 0.80 and sent_count > 0:
        return "DIAGNOSTIC"

    strong_count = sum(1 for r in state["replies"].values() if r.get("signal") == "STRONG")
    moderate_count = sum(1 for r in state["replies"].values() if r.get("signal") == "MODERATE")

    strong_thresh, mod_thresh, _ = _T7_THRESHOLDS.get(domain_id, (2, 1, ""))

    if strong_count >= strong_thresh:
        return "STRONG"

    # Auto-elevate rules per PHASE_2_T7_ROUTING_DECISION_TREE.md Section 1.1
    if domain_id == 51:
        # CLC reply (send 1) at any quality level auto-elevates to MODERATE
        clc_replied = "1" in state["replies"]
        if clc_replied or strong_count >= mod_thresh or moderate_count >= 2:
            return "MODERATE"
    elif domain_id == 48:
        # Sentencing Project reply (send 1) at any quality level auto-elevates to MODERATE
        sp_replied = "1" in state["replies"]
        if sp_replied or strong_count >= mod_thresh or moderate_count >= 2:
            return "MODERATE"
    else:
        if strong_count >= mod_thresh or moderate_count >= 3:
            return "MODERATE"

    return "WEAK"


def _cross_domain_coalition_check(signals: dict[int, str]) -> list[str]:
    """Identify cross-domain coalition opportunities per PHASE_2_T7_ROUTING_DECISION_TREE.md Section 4."""
    opportunities = []
    d59 = signals.get(59, "WEAK")
    d51 = signals.get(51, "WEAK")
    d48 = signals.get(48, "WEAK")

    if d59 == "STRONG" and d51 == "STRONG":
        opportunities.append(
            "D59+D51 STRONG: Activate Demos (info@demos.org) and Common Cause National "
            "(commoncause@commoncause.org) with cross-domain economic-democracy / campaign-finance "
            "bridge framing. Estimated 2.0-2.5x reach multiplier from bridging both ecosystems."
        )
    if d59 in ("STRONG", "MODERATE") and d48 in ("STRONG", "MODERATE"):
        opportunities.append(
            "D59+D48 both active: Add Domain 48 criminal-record employment bar context to NELP "
            "(Domain 59 Tier 2) email. Route NAACP LDF send (Domain 48 Tier 2) with a cross-domain "
            "note referencing economic precarity findings from Domain 59."
        )
    if d51 == "STRONG" and d48 == "STRONG":
        opportunities.append(
            "D51+D48 STRONG: Send both documents to Brennan Center on same day — "
            "Domain 51 to Saurav Ghosh (ghoshs@brennan.law.nyu.edu), "
            "Domain 48 to Sean Morales-Doyle (brennancenter.org web form). "
            "Internal routing may surface the campaign-finance + voting-rights overlap."
        )
    if d59 == "STRONG" and d51 == "STRONG" and d48 == "STRONG":
        opportunities.append(
            "ALL DOMAINS STRONG: Full coalition protocol. Activate all three Tier 2 sequences on "
            "same day. Cross-domain coordination via Demos + Brennan Center + NAACP LDF. "
            "See PHASE_2_T7_ROUTING_DECISION_TREE.md Section 2.2."
        )
    return opportunities


def cmd_t7_checkpoint() -> None:
    """Run the Day 7 multi-domain checkpoint across Domains 59, 51, and 48.

    Collects state for each domain, classifies signal strength, outputs routing
    recommendation per PHASE_2_T7_ROUTING_DECISION_TREE.md, and writes summary
    to WORKLOG.md.
    """
    now = datetime.now(timezone.utc)
    print(f"\n=== Day 7 Multi-Domain Checkpoint ===")
    print(f"Executed: {now.strftime('%Y-%m-%d %H:%M UTC')}")
    print(f"Reference: JUNE_17_DAY7_CHECKPOINT_EXECUTION_CHECKLIST.md")
    print()

    signals: dict[int, str] = {}
    domain_summaries: list[str] = []

    for domain_id in [59, 51, 48]:
        domain = DOMAINS[domain_id]
        state = load_state(domain_id)
        contacts = domain["contacts"]
        total = len(contacts)
        sent = len(state["sends"])
        bounces = len(state["bounces"])
        replies = len(state["replies"])
        strong = sum(1 for r in state["replies"].values() if r.get("signal") == "STRONG")
        moderate = sum(1 for r in state["replies"].values() if r.get("signal") == "MODERATE")

        signal = _classify_signal(domain_id, state)
        signals[domain_id] = signal

        try:
            deadline_dt = datetime.fromisoformat(domain["deadline"]).replace(tzinfo=timezone.utc)
            days_to_deadline = (deadline_dt - now).days
        except ValueError:
            days_to_deadline = "?"

        print(f"--- Domain {domain_id}: {domain['topic'][:55]} ---")
        print(f"  Sends: {sent}/{total} | Bounces: {bounces} | Replies: {replies}")
        print(f"  STRONG: {strong} | MODERATE: {moderate}")
        print(f"  Deadline: {domain['deadline']} ({days_to_deadline} days)")
        print(f"  Gist: {domain['gist_url']}")
        print(f"  COMPOSITE SIGNAL: {signal}")
        print()

        tier2_contacts = _TIER2_CONTACTS.get(domain_id, {}).get(signal, [])
        if tier2_contacts:
            print(f"  Tier 2 activation ({signal}):")
            for org, email in tier2_contacts:
                if email:
                    print(f"    - {org} — {email}")
                else:
                    print(f"    - {org}")
        print()

        summary_line = (
            f"D{domain_id}: {signal} | sent {sent}/{total} | {strong} STRONG | "
            f"{days_to_deadline}d to deadline"
        )
        domain_summaries.append(summary_line)

    # Cross-domain coalition opportunities
    coalition_opps = _cross_domain_coalition_check(signals)
    if coalition_opps:
        print("=== Cross-Domain Coalition Opportunities ===")
        for opp in coalition_opps:
            print(f"  * {opp}")
        print()

    # Escalation check
    all_weak = all(s == "WEAK" for s in signals.values())
    any_diagnostic = any(s == "DIAGNOSTIC" for s in signals.values())
    print("=== Escalation Check ===")
    if any_diagnostic:
        print("  DIAGNOSTIC CONDITION: Delivery rate below 80% on at least one domain.")
        print("  Action: Run delivery diagnostic before Tier 2 activation.")
        print("  See JUNE_17_DAY7_CHECKPOINT_EXECUTION_CHECKLIST.md Section 1.4")
    elif all_weak:
        print("  ALL DOMAINS WEAK at Day 7.")
        print("  Domain 59: FORCED Tier 2 activation (Senate markup deadline immovable)")
        print("  Domain 51: Hold to Day 14. Day 14 CLC follow-up is the pivot point.")
        print("  Domain 48: Hold to Day 14.")
        print("  If all WEAK at Day 14: flag in CHECKIN.md per Section 8.1 of checklist.")
    else:
        print("  No escalation required. Proceed with routing above.")
    print()

    # Write to WORKLOG
    worklog_entry = (
        f"**Day 7 Multi-Domain Checkpoint**\n\n"
        + "\n".join(f"- {s}" for s in domain_summaries)
        + f"\n\nSignals: D59={signals.get(59,'?')} | D51={signals.get(51,'?')} | D48={signals.get(48,'?')}"
        + (f"\n\nCoalition opportunities: {len(coalition_opps)} identified." if coalition_opps else "")
        + f"\n\nReference: PHASE_2_T7_ROUTING_DECISION_TREE.md for full routing logic."
    )
    # Use domain 59 for worklog attribution (primary deadline domain)
    append_worklog(59, worklog_entry)
    print("[worklog] Day 7 checkpoint summary written to WORKLOG.md")


# ---------------------------------------------------------------------------
# Routing decision (--routing-decision)
# ---------------------------------------------------------------------------

def cmd_routing_decision(domain_ids: list[int], signal_strs: list[str]) -> None:
    """Take domain IDs + signal strengths and output Tier 2 activation sequence.

    Per PHASE_2_T7_ROUTING_DECISION_TREE.md Section 2.
    """
    valid_signals = {"STRONG", "MODERATE", "WEAK", "DIAGNOSTIC"}
    if len(domain_ids) != len(signal_strs):
        print(
            f"[error] domain count ({len(domain_ids)}) must match signal count ({len(signal_strs)})",
            file=sys.stderr,
        )
        sys.exit(1)
    for s in signal_strs:
        if s not in valid_signals:
            print(f"[error] Signal '{s}' not valid. Use: {', '.join(sorted(valid_signals))}", file=sys.stderr)
            sys.exit(1)
    for d in domain_ids:
        if d not in DOMAINS:
            print(f"[error] Domain {d} not in dispatch table. Supported: {sorted(DOMAINS.keys())}", file=sys.stderr)
            sys.exit(1)

    signals = dict(zip(domain_ids, signal_strs))
    now = datetime.now(timezone.utc)

    print(f"\n=== Routing Decision Output ===")
    print(f"Generated: {now.strftime('%Y-%m-%d %H:%M UTC')}")
    print(f"Input signals: {' | '.join(f'D{d}={s}' for d, s in signals.items())}")
    print()

    # Per-domain activation sequences
    for domain_id, signal in signals.items():
        domain = DOMAINS[domain_id]
        tier2 = _TIER2_CONTACTS.get(domain_id, {}).get(signal, [])
        print(f"Domain {domain_id} ({signal}):")
        if tier2:
            for org, email in tier2:
                if email:
                    print(f"  -> {org}")
                    print(f"     {email}")
                else:
                    print(f"  -> {org}")
        else:
            print("  -> No Tier 2 contacts prescribed for this signal level.")
        print()

    # Cross-domain coalition check
    coalition_opps = _cross_domain_coalition_check(signals)
    if coalition_opps:
        print("=== Cross-Domain Coalition Opportunities ===")
        for opp in coalition_opps:
            print(f"  * {opp}")
        print()

    # Execution order recommendation
    print("=== Recommended Execution Order ===")
    # D59 always first (hardest deadline); then D51; then D48
    ordered = [d for d in [59, 51, 48] if d in signals]
    for i, d in enumerate(ordered, 1):
        sig = signals[d]
        domain = DOMAINS[d]
        print(f"  {i}. Domain {d} ({sig}) — deadline {domain['deadline']}")
        if sig == "WEAK" and d == 59:
            print(f"     NOTE: FORCED activation due to Senate Finance markup deadline.")

    # Write to WORKLOG (domain 59 or first domain in list)
    primary_domain = domain_ids[0]
    worklog_entry = (
        f"**Routing decision executed**\n\n"
        f"Input: {' | '.join(f'D{d}={s}' for d, s in signals.items())}\n\n"
        f"Coalition opportunities identified: {len(coalition_opps)}\n\n"
        f"Reference: PHASE_2_T7_ROUTING_DECISION_TREE.md"
    )
    append_worklog(primary_domain, worklog_entry)


# ---------------------------------------------------------------------------
# Activate Tier 2 (--activate-tier2)
# ---------------------------------------------------------------------------

def cmd_activate_tier2(domain_id: int, signal: str) -> None:
    """Deploy Tier 2 contacts per PHASE_2_TIER_2_ACTIVATION_PROTOCOLS.md.

    Prints the activation guide, logs to WORKLOG.md, and updates domain state.
    """
    valid_signals = {"STRONG", "MODERATE", "WEAK"}
    if signal not in valid_signals:
        print(f"[error] Signal must be one of: {', '.join(sorted(valid_signals))}", file=sys.stderr)
        sys.exit(1)
    if domain_id not in DOMAINS:
        print(f"[error] Domain {domain_id} not in dispatch table. Supported: {sorted(DOMAINS.keys())}", file=sys.stderr)
        sys.exit(1)

    domain = DOMAINS[domain_id]
    state = load_state(domain_id)
    tier2_contacts = _TIER2_CONTACTS.get(domain_id, {}).get(signal, [])
    now = datetime.now(timezone.utc)

    try:
        deadline_dt = datetime.fromisoformat(domain["deadline"]).replace(tzinfo=timezone.utc)
        days_to_deadline = (deadline_dt - now).days
    except ValueError:
        days_to_deadline = "?"

    print(f"\n=== Domain {domain_id} Tier 2 Activation ({signal}) ===")
    print(f"Generated: {now.strftime('%Y-%m-%d %H:%M UTC')}")
    print(f"Deadline: {domain['deadline']} ({days_to_deadline} days remaining)")
    print(f"Gist URL: {domain['gist_url']}")
    print()

    if not tier2_contacts:
        print("[info] No Tier 2 contacts prescribed for this domain + signal combination.")
        print(f"       See PHASE_2_TIER_2_ACTIVATION_PROTOCOLS.md for Domain {domain_id}.")
        return

    print("Tier 2 contacts to deploy (in order):")
    for i, (org, email) in enumerate(tier2_contacts, 1):
        if email:
            print(f"  {i}. {org}")
            print(f"     Email: {email}")
        else:
            print(f"  {i}. {org}")
    print()

    print("Pre-flight checks:")
    print(f"  [ ] Confirm Gist URL resolves: {domain['gist_url']}")
    print(f"  [ ] Verify all email addresses on send day (contacts may have changed)")
    if domain_id == 59:
        print(f"  [ ] Confirm Senate Finance markup status: {domain['check_url']}")
        print(f"      If markup closed: pivot to '2027 Reform Coalition' framing")
    elif domain_id == 51:
        print(f"  [ ] Confirm California ballot measure status: {domain['check_url']}")
        print(f"      If CA ballot failed: shift to national-only framing (CLC, Issue One, Democracy 21)")
    elif domain_id == 48:
        print(f"  [ ] Confirm Virginia Right to Vote Coalition integration window still active")
        print(f"      Soft deadline: June 27 for Tier 2 sends before July 15 coalition deadline")
    print()

    print("Full templates: PHASE_2_TIER_2_ACTIVATION_PROTOCOLS.md")
    print(f"Sequencing: see PHASE_2_T7_ROUTING_DECISION_TREE.md Section 2 for D{domain_id} {signal} path")
    print()

    # Log to WORKLOG
    contact_lines = "\n".join(
        f"- {org}: {email}" if email else f"- {org}"
        for org, email in tier2_contacts
    )
    worklog_entry = (
        f"**Domain {domain_id} Tier 2 Activation — {signal}**\n\n"
        f"Signal at checkpoint: {signal}\n"
        f"Contacts activated:\n{contact_lines}\n\n"
        f"Templates: PHASE_2_TIER_2_ACTIVATION_PROTOCOLS.md (Domain {domain_id} section)\n"
        f"Deadline: {domain['deadline']} ({days_to_deadline} days)"
    )
    append_worklog(domain_id, worklog_entry)

    # Record tier2 activation in state
    state["tier2_activation"] = {
        "signal": signal,
        "activated_at": now.isoformat(),
        "contacts_count": len([c for c in tier2_contacts if c[1]]),
    }
    save_state(domain_id, state)
    print("[worklog] Tier 2 activation logged to WORKLOG.md and state file.")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Phase 2 Multi-Domain Wave Orchestration Script (Domain 51 + Domain 59)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )

    parser.add_argument(
        "--domain",
        type=int,
        choices=[48, 51, 59],
        help="Domain to operate on (48=Criminal Justice, 51=Campaign Finance, 59=Economic Precarity/CTC)",
    )
    parser.add_argument(
        "--status",
        action="store_true",
        help="Show current execution status for all sends in the selected domain",
    )
    parser.add_argument(
        "--all-domains-status",
        action="store_true",
        help="Show summary status for both domains without --domain flag",
    )
    parser.add_argument(
        "--sequence-check",
        action="store_true",
        help="Print the activation sequence recommendation and rationale (no --domain needed)",
    )
    parser.add_argument(
        "--execute",
        type=str,
        metavar="WAVE",
        help="Print execution guide and log intent (wave1, wave2, wave3, all)",
    )
    parser.add_argument(
        "--generate-guide",
        type=str,
        metavar="WAVE",
        help="Print a self-contained execution guide to stdout (no WORKLOG entry)",
    )
    parser.add_argument(
        "--log-send",
        type=int,
        metavar="SEND_NUM",
        help="Record that a send was completed",
    )
    parser.add_argument(
        "--time",
        type=str,
        default=None,
        help='Timestamp for --log-send (e.g., "2026-06-17 14:05 UTC"). Defaults to now.',
    )
    parser.add_argument(
        "--log-bounce",
        type=int,
        metavar="SEND_NUM",
        help="Record that a send bounced",
    )
    parser.add_argument(
        "--fallback",
        action="store_true",
        help="With --log-bounce: indicate fallback address was also sent",
    )
    parser.add_argument(
        "--log-reply",
        type=int,
        metavar="SEND_NUM",
        help="Record a reply received for a send",
    )
    parser.add_argument(
        "--signal",
        choices=["STRONG", "MODERATE", "WEAK", "NONE"],
        help="Signal tier for --log-reply",
    )
    parser.add_argument(
        "--summary",
        type=str,
        default="",
        help="One-sentence summary of the reply for --log-reply",
    )
    parser.add_argument(
        "--t7-check",
        action="store_true",
        help="Run the T+7 checkpoint assessment and print Phase 2 gate recommendation (per-domain)",
    )
    parser.add_argument(
        "--t7-checkpoint",
        action="store_true",
        help=(
            "Run the Day 7 multi-domain checkpoint across Domains 59, 51, and 48. "
            "Collects send/reply state, classifies signal strength per domain, "
            "outputs routing recommendation, and logs to WORKLOG.md. "
            "Does not require --domain."
        ),
    )
    parser.add_argument(
        "--routing-decision",
        nargs="+",
        metavar="DOMAIN_OR_SIGNAL",
        help=(
            "Takes domain IDs followed by signal strengths and outputs Tier 2 activation sequence. "
            "Example: --routing-decision 59 51 48 STRONG MODERATE WEAK"
        ),
    )
    parser.add_argument(
        "--activate-tier2",
        nargs=2,
        metavar=("DOMAIN", "SIGNAL"),
        help=(
            "Deploy Tier 2 contacts for a domain per PHASE_2_TIER_2_ACTIVATION_PROTOCOLS.md. "
            "Example: --activate-tier2 59 STRONG"
        ),
    )

    args = parser.parse_args()

    # Commands that do not require --domain
    if args.all_domains_status:
        cmd_all_domains_status()
        return
    if args.sequence_check:
        cmd_sequence_check()
        return
    if args.t7_checkpoint:
        cmd_t7_checkpoint()
        return
    if args.routing_decision:
        raw = args.routing_decision
        valid_signals = {"STRONG", "MODERATE", "WEAK", "DIAGNOSTIC"}
        domain_ids_raw = [x for x in raw if x.isdigit()]
        signal_strs_raw = [x.upper() for x in raw if x.upper() in valid_signals]
        if not domain_ids_raw or not signal_strs_raw:
            print(
                "[error] --routing-decision requires domain IDs followed by signal strengths.\n"
                "        Example: --routing-decision 59 51 48 STRONG MODERATE WEAK",
                file=sys.stderr,
            )
            sys.exit(1)
        domain_ids_parsed = [int(d) for d in domain_ids_raw]
        cmd_routing_decision(domain_ids_parsed, signal_strs_raw)
        return
    if args.activate_tier2:
        domain_arg, signal_arg = args.activate_tier2
        try:
            domain_id_t2 = int(domain_arg)
        except ValueError:
            print(f"[error] Domain must be an integer. Got: {domain_arg}", file=sys.stderr)
            sys.exit(1)
        cmd_activate_tier2(domain_id_t2, signal_arg.upper())
        return

    # All other commands require --domain
    if args.domain is None:
        if any([args.status, args.execute, args.generate_guide, args.log_send is not None,
                args.log_bounce is not None, args.log_reply is not None, args.t7_check]):
            print("[error] --domain 48, 51, or 59 is required for this command.", file=sys.stderr)
            parser.print_help()
            sys.exit(1)
        parser.print_help()
        sys.exit(0)

    domain_id = args.domain
    if domain_id not in DOMAINS:
        print(f"[error] Unsupported domain: {domain_id}. Supported: {sorted(DOMAINS.keys())}.", file=sys.stderr)
        sys.exit(1)

    state = load_state(domain_id)

    if args.status:
        cmd_status(domain_id, state)

    elif args.execute:
        cmd_execute(domain_id, args.execute, state)

    elif args.generate_guide:
        cmd_generate_guide(domain_id, args.generate_guide)

    elif args.log_send is not None:
        timestamp = args.time or datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        cmd_log_send(domain_id, args.log_send, timestamp, state)

    elif args.log_bounce is not None:
        cmd_log_bounce(domain_id, args.log_bounce, args.fallback, state)

    elif args.log_reply is not None:
        if not args.signal:
            print("[error] --log-reply requires --signal (STRONG/MODERATE/WEAK/NONE)", file=sys.stderr)
            sys.exit(1)
        cmd_log_reply(domain_id, args.log_reply, args.signal, args.summary, state)

    elif args.t7_check:
        cmd_t7_check(domain_id, state)

    else:
        parser.print_help()
        sys.exit(0)


if __name__ == "__main__":
    main()
