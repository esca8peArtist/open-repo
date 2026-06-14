#!/usr/bin/env python3
"""
Phase 2 Multi-Domain Wave Orchestration Script
Supports: Domain 51 (Campaign Finance), Domain 59 (Economic Precarity / Senate Finance CTC)

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

    # T+7 checkpoint
    uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --domain 51 --t7-check
    uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --domain 59 --t7-check

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
# Domain dispatch table
# ---------------------------------------------------------------------------

DOMAINS = {
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
    """Print summary status for both domains side by side."""
    print("\n=== Multi-Domain Status Summary ===")
    print(f"Date: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    print()
    print("SEQUENCING RULE: Domain 59 → Domain 51 (Senate Finance window closes before CA ballot deadline)")
    print()
    for domain_id in [59, 51]:
        state = load_state(domain_id)
        domain = DOMAINS[domain_id]
        contacts = domain["contacts"]
        total = len(contacts)
        sent = sum(1 for k in contacts if str(k) in state["sends"])
        strong = sum(1 for r in state["replies"].values() if r.get("signal") == "STRONG")
        print(f"Domain {domain_id} ({domain['topic'][:50]})")
        print(f"  Sends completed: {sent}/{total}")
        print(f"  STRONG replies:  {strong}")
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
        choices=[51, 59],
        help="Domain to operate on (51=Campaign Finance, 59=Economic Precarity/CTC)",
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
        help="Run the T+7 checkpoint assessment and print Phase 2 gate recommendation",
    )

    args = parser.parse_args()

    # Commands that do not require --domain
    if args.all_domains_status:
        cmd_all_domains_status()
        return
    if args.sequence_check:
        cmd_sequence_check()
        return

    # All other commands require --domain
    if args.domain is None:
        if any([args.status, args.execute, args.generate_guide, args.log_send is not None,
                args.log_bounce is not None, args.log_reply is not None, args.t7_check]):
            print("[error] --domain 51 or --domain 59 is required for this command.", file=sys.stderr)
            parser.print_help()
            sys.exit(1)
        parser.print_help()
        sys.exit(0)

    domain_id = args.domain
    if domain_id not in DOMAINS:
        print(f"[error] Unsupported domain: {domain_id}. Supported: 51, 59.", file=sys.stderr)
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
