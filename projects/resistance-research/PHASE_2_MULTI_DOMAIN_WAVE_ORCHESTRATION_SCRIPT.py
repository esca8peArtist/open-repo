#!/usr/bin/env python3
"""
Phase 2 Multi-Domain Wave Orchestration Script
Domain 51 — Campaign Finance / Dark Money Architecture

Coordinates Wave 1-2 execution for the orchestrator. Generates domain-specific
execution guides dynamically, logs send results to WORKLOG.md, and provides
recovery commands for failures.

Usage:
    uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --status
    uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --execute wave1
    uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --execute wave2
    uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --execute all
    uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --log-send 1 --time "2026-06-14 16:03 UTC"
    uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --log-bounce 1 --fallback
    uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --log-reply 2 --signal STRONG --summary "Chlopak replied asking about Hawaii/Montana model"
    uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --t7-check
    uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --generate-guide wave1
    uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --generate-guide wave2

Environment variable:
    RESISTANCE_RESEARCH_DIR: path to projects/resistance-research/ (auto-detected if not set)
"""

import argparse
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Optional

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

GIST_URL = "https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372"
HARD_DEADLINE = "2026-07-01"
BALLOT_CHECK_URL = "https://ballotpedia.org/California_Public_Funding_of_Elections_Measure_(2026)"

# All 5 contacts for Phase 2 Wave 1+2
CONTACTS = {
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
            "Do not confuse the two domains."
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
            "No confirmed backup address — use issueone.org/contact form as fallback."
        ),
    },
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
            "Confirmed at commoncause.org/california/people/darius-kemp/. "
            "Personnel change: Jonathan Mehta Stein departed; Kemp appointed June 2025. "
            "dkemp@ is confirmed handle (not first.last format). "
            "Salutation 'Dear Darius' appropriate during campaign mode."
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
            "Confirmed at lwvc.org/about/staff. "
            "Personnel change: Carol Moon Goldberg no longer listed; Farrell is current ED. "
            "No direct email for Farrell publicly listed — lwvc@lwvc.org is org inbox. "
            "No confirmed backup address."
        ),
    },
    5: {
        "wave": 2,
        "org": "Clean Money Action Fund",
        "contact_name": "Trent Lange",
        "role": "President & Executive Director (since 2009)",
        "primary_email": "info@CAclean.org",
        "backup_email": None,
        "phone_fallback": "(310) 397-0200",
        "verified_date": "2026-06-11",
        "confidence": "HIGH",
        "domain_hook": "California Fair Elections Act / dark money architecture / campaign operations",
        "response_probability": "5-10%",
        "notes": (
            "CRITICAL: Use info@CAclean.org. Do NOT use cleanmoney.org — unreachable since June 5, 2026. "
            "Confirmed at yesfairelections.org/about. "
            "Trent.Lange@CAclean.org also documented on org About page as direct contact."
        ),
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
    # Auto-detect from script location
    script_dir = Path(__file__).parent
    if script_dir.name == "resistance-research":
        return script_dir
    # Walk up to find projects/resistance-research/
    for parent in [script_dir] + list(script_dir.parents):
        candidate = parent / "projects" / "resistance-research"
        if candidate.is_dir():
            return candidate
    return script_dir  # fallback to script directory


RESEARCH_DIR = get_research_dir()
WORKLOG_PATH = RESEARCH_DIR / "WORKLOG.md"
EXECUTION_LOG_PATH = RESEARCH_DIR / "DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md"
STATE_PATH = RESEARCH_DIR / "phase-1-adoption" / "data" / "wave_orchestration_state.json"

# ---------------------------------------------------------------------------
# State management
# ---------------------------------------------------------------------------

def load_state() -> dict:
    """Load send state from disk."""
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    if STATE_PATH.exists():
        try:
            with open(STATE_PATH) as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
    return {
        "sends": {},       # send_number -> send record
        "bounces": {},     # send_number -> bounce record
        "replies": {},     # send_number -> reply record
        "created": datetime.now(timezone.utc).isoformat(),
    }


def save_state(state: dict) -> None:
    """Persist state to disk."""
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(STATE_PATH, "w") as f:
        json.dump(state, f, indent=2)


# ---------------------------------------------------------------------------
# WORKLOG writer
# ---------------------------------------------------------------------------

def append_worklog(entry: str) -> None:
    """Append a timestamped entry to WORKLOG.md."""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    block = f"\n---\n\n## {now} — Wave Orchestration\n\n{entry.strip()}\n"
    try:
        with open(WORKLOG_PATH, "a") as f:
            f.write(block)
        print(f"[worklog] Entry appended to {WORKLOG_PATH}")
    except IOError as e:
        print(f"[warn] Could not write to WORKLOG.md: {e}", file=sys.stderr)


# ---------------------------------------------------------------------------
# Status display
# ---------------------------------------------------------------------------

def cmd_status(state: dict) -> None:
    """Print current execution status for all 5 contacts."""
    now = datetime.now(timezone.utc)
    deadline = datetime(2026, 7, 1, tzinfo=timezone.utc)
    days_remaining = (deadline - now).days

    print("\n=== Phase 2 Wave 1-2 Execution Status ===")
    print(f"Date: {now.strftime('%Y-%m-%d %H:%M UTC')}")
    print(f"Hard deadline: {HARD_DEADLINE} ({days_remaining} days remaining)")
    print(f"Gist URL: {GIST_URL}")
    print()

    for send_num, contact in CONTACTS.items():
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

        print(
            f"  Send {send_num} | Wave {contact['wave']} | {contact['org']}\n"
            f"           Contact: {contact['contact_name']} <{contact['primary_email']}>\n"
            f"           Status:  {status}\n"
            f"           Reply:   {reply_label}"
        )
        if sent:
            print(f"           Sent at: {send_record.get('timestamp', 'unknown')}")
        print()

    # T+7 summary
    sent_timestamps = [
        state["sends"][str(k)]["timestamp"]
        for k in [1, 2]
        if str(k) in state["sends"]
    ]
    if sent_timestamps:
        earliest = min(sent_timestamps)
        print(f"Wave 1 first send: {earliest}")
        try:
            wave1_dt = datetime.fromisoformat(earliest.replace(" UTC", "+00:00"))
            t7 = wave1_dt + timedelta(days=7)
            t14 = wave1_dt + timedelta(days=14)
            print(f"T+7 checkpoint:    {t7.strftime('%Y-%m-%d')}")
            print(f"T+14 checkpoint:   {t14.strftime('%Y-%m-%d')}")
        except ValueError:
            pass
    print()


# ---------------------------------------------------------------------------
# Execution guide generation
# ---------------------------------------------------------------------------

def generate_wave1_guide() -> str:
    """Generate a self-contained Wave 1 execution guide for printing or clipboard."""
    c1 = CONTACTS[1]
    c2 = CONTACTS[2]
    lines = [
        "=== WAVE 1 EXECUTION GUIDE (generated) ===",
        f"Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        "SEND 1 — Campaign Legal Center",
        f"  To:      {c1['primary_email']}",
        f"  Backup:  {c1['backup_email']}",
        "  Subject: Constitutional architecture research on Citizens United — Hawaii/Montana model + FEC collapse analysis",
        "",
        "  Body (copy-paste, fill YOUR_NAME and YOUR_CONTACT_INFO):",
        "  ---",
        "  Dear Campaign Legal Center team,",
        "",
        "  I am sharing a research document that may be relevant to your current work on campaign finance enforcement and state-level reform:",
        "",
        "  Domain 51 documents the Citizens United architecture from a democratic design perspective — specifically the structural consequence of the FEC's 200+ day enforcement quorum collapse and the constitutional theory behind Hawaii SB 2471 (signed May 15, 2026) and Montana I-194 (approximately 1,000 signatures from qualification).",
        "",
        "  The sections most relevant to CLC's work:",
        "",
        "  - Section 6.3 (Hawaii/Montana Corporate Charter Model): the Center for American Progress theory that CLC's constitutional team will likely be asked to assess — does charter-revocation of corporate political spending authority survive the 'associations of citizens' rationale in Citizens United, or only the state-derived-power rationale?",
        "  - Section 3 (FEC Structural Failure): 200-day enforcement collapse with specific pending matters — useful documentation for FEC enforcement advocacy",
        "  - Section 7 (Reform Architecture): DISCLOSE Act of 2026 legislative pathway + state-level equivalents + SEC disclosure rule status",
        "",
        f"  The document is at: {GIST_URL}",
        "",
        "  58 citations, CC Attribution 4.0. I would welcome any feedback on whether the constitutional analysis of the Hawaii/Montana model accurately represents the current scholarly and litigation consensus.",
        "",
        "  [YOUR_NAME]",
        "  [YOUR_CONTACT_INFO]",
        "  ---",
        "",
        "  After sending Send 1: wait 90 minutes.",
        "",
        "SEND 2 — Issue One (90 minutes after Send 1)",
        f"  To:      {c2['primary_email']}",
        "  Subject: Dark money architecture research — FEC collapse documentation + state ballot measure analysis",
        "",
        "  Body (copy-paste, fill YOUR_NAME and YOUR_CONTACT_INFO):",
        "  ---",
        "  Dear Issue One team,",
        "",
        "  I am sharing research that complements Issue One's work on FEC reform and dark money disclosure:",
        "",
        "  Domain 51 is a structural analysis of the Citizens United architecture with a dedicated section on the FEC enforcement collapse — which Issue One has been documenting through your 'Strengthening the Rules' reporting. The document uses Issue One's enforcement deadlock analysis as a primary source and extends it to the broader democratic accountability argument.",
        "",
        "  The most relevant sections:",
        "",
        "  - Section 3 (FEC Structural Failure): 200+ day enforcement shutdown with specific pending matters — Issue One's reporting is cited directly; the document extends your analysis to the constitutional design argument",
        "  - Section 5 (2026 State Ballot Measures): four-state analysis including California, Missouri, Montana, and Hawaii — the landscape your ReFormers Caucus work is operating in",
        "  - Section 7 (Reform Architecture): DISCLOSE Act pathway + the Hawaii corporate charter workaround as a parallel track that does not require DISCLOSE Act passage",
        "",
        "  Issue One is cited as a primary source throughout. The document is designed for distribution to organizations that can use the structural analysis in their own advocacy:",
        f"  {GIST_URL}",
        "",
        "  58 citations, CC Attribution 4.0. I would be grateful if this reaches your research team.",
        "",
        "  [YOUR_NAME]",
        "  [YOUR_CONTACT_INFO]",
        "  ---",
        "",
        "Wave 1 complete after Send 2 is logged.",
    ]
    return "\n".join(lines)


def generate_wave2_guide() -> str:
    """Generate a self-contained Wave 2 execution guide."""
    c3 = CONTACTS[3]
    c4 = CONTACTS[4]
    c5 = CONTACTS[5]
    lines = [
        "=== WAVE 2 EXECUTION GUIDE (generated) ===",
        f"Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        f"PRE-CHECK: Confirm CA Fair Elections Act is still on ballot: {BALLOT_CHECK_URL}",
        "  If removed: change subject lines from 'California Fair Elections Act campaign' to 'California campaign finance reform analysis'",
        "",
        "SEND 3 — Common Cause California",
        f"  To:      {c3['primary_email']}",
        f"  CC:      {c3.get('cc_email', 'n/a')}",
        f"  Backup:  {c3['backup_email']}",
        "  Subject: Research on Citizens United architecture for California Fair Elections Act campaign — July 1 window",
        "",
        "  Body (copy-paste, fill YOUR_NAME and YOUR_CONTACT_INFO):",
        "  ---",
        "  Dear Darius,",
        "",
        "  I am sharing a research document on the Citizens United dark money architecture that may be directly useful to the California Fair Elections Act campaign ahead of the November 3 ballot.",
        "",
        "  Domain 51 documents the structural mechanism through which the Citizens United decision — combined with the SpeechNow.org ruling creating super PACs and the 501(c)(4) vehicle for non-disclosure — has produced $1.9 billion in dark money in the 2024 federal cycle alone. The document includes dedicated sections on the California Fair Elections Act (your current campaign), the Hawaii SB 2471 Citizens United workaround (signed May 15, 2026, relevant to the legal theory arguments your campaign will face), and the Montana Plan ballot initiative operating on the same model.",
        "",
        "  The most relevant sections for your campaign work:",
        "",
        "  - Section 5 (The 2026 State Ballot Measures): California Fair Elections Act analysis, the FEC enforcement vacuum as a 'why now' urgency frame for voters, and the meta-structure of the four simultaneous state campaigns",
        "  - Section 6.3 (The Hawaii/Montana Corporate Charter Model): the legal architecture that makes state-level reform viable under Citizens United — directly responsive to the 'unconstitutional' attacks your campaign will receive",
        "  - Section 3 (FEC Structural Failure): the 200+ day FEC enforcement shutdown as evidence that federal self-regulation has collapsed, making state-level action the only viable near-term reform",
        "",
        "  The document is publicly available under Creative Commons Attribution 4.0 — use it, excerpt it, share it with campaign staff and legal team:",
        f"  {GIST_URL}",
        "",
        "  The July 1 date is our hard window — that is when California ballot campaigns typically lock their messaging infrastructure before shifting to field execution. I would welcome any indication the research reaches your campaign team.",
        "",
        "  [YOUR_NAME]",
        "  [YOUR_CONTACT_INFO]",
        "  ---",
        "",
        "  After Send 3: wait 90 minutes.",
        "",
        "SEND 4 — League of Women Voters California (90 min after Send 3)",
        f"  To:      {c4['primary_email']}",
        "  Subject: Dark money architecture research for California Fair Elections Act campaign — July 1 window",
        "",
        "  Body (copy-paste, fill YOUR_NAME and YOUR_CONTACT_INFO):",
        "  ---",
        "  Dear League of Women Voters California,",
        "",
        "  I am writing to share research that may support your work on the California Fair Elections Act ahead of the November 3 ballot.",
        "",
        "  Domain 51 — 'Campaign Finance, Dark Money Architecture, and the Corporate Capture of Democratic Institutions' — documents the structural history of how Citizens United, SpeechNow.org, and FEC enforcement collapse have created the dark money system, and analyzes the four simultaneous 2026 state reform campaigns including California's.",
        "",
        "  For LWV California's voter education mission, the most immediately applicable sections:",
        "",
        "  - Executive Summary (standalone, 500 words): a non-technical explanation of how the dark money architecture works, suitable for voter guides and public education materials",
        "  - Section 6 (International Comparison): UK and Canada have robust political speech protections and robust disclosure requirements — directly answering the 'but First Amendment' objection",
        "  - Section 5 (California Fair Elections Act): specific analysis of the public financing mechanism and what it would structurally change in California campaigns",
        "",
        f"  The research is 58 citations, CC Attribution 4.0. It is designed to be used — excerpted in voter guides, cited in public education materials, shared with your member network:\n  {GIST_URL}",
        "",
        "  I would be grateful if this reaches your campaign research team before the July 1 messaging infrastructure window.",
        "",
        "  [YOUR_NAME]",
        "  [YOUR_CONTACT_INFO]",
        "  ---",
        "",
        "  After Send 4: wait 90 minutes.",
        "",
        "SEND 5 — Clean Money Action Fund (90 min after Send 4)",
        f"  To:      {c5['primary_email']}",
        "  NOTE:    Do NOT use cleanmoney.org — that domain is unreachable. Use CAclean.org.",
        "  Subject: Dark money research for California Fair Elections Act — 58 citations, CC Attribution 4.0",
        "",
        "  Body (copy-paste, fill YOUR_NAME and YOUR_CONTACT_INFO):",
        "  ---",
        "  Dear Clean Money Action Fund team,",
        "",
        "  I am sharing a research document on the Citizens United dark money architecture timed to the California Fair Elections Act campaign window.",
        "",
        "  Domain 51 is a 58-citation structural analysis of how dark money works, why state-level reform is the most viable near-term pathway, and what the 2026 state campaigns — including California — mean for the broader reform movement. The document covers:",
        "",
        "  - The $1.9B in dark money in the 2024 federal cycle and the structural reason this number keeps growing without FEC enforcement",
        "  - The California Fair Elections Act's public financing mechanism and the arguments it will face from dark money opposition",
        "  - Hawaii SB 2471 (signed May 15) as the first Citizens United workaround through corporate charter law — a legal theory your organization should be aware of for the post-November period if the ballot measure passes",
        "  - The FEC enforcement shutdown (200+ consecutive days without quorum as of June 2026) as a structural frame for why federal reform has stalled and state action is necessary",
        "",
        f"  CC Attribution 4.0 — use it, adapt it, share it with your campaign legal team and communications staff:\n  {GIST_URL}",
        "",
        "  [YOUR_NAME]",
        "  [YOUR_CONTACT_INFO]",
        "  ---",
        "",
        "Wave 2 complete after Send 5 is logged.",
    ]
    return "\n".join(lines)


def cmd_generate_guide(wave: str) -> None:
    """Print a self-contained execution guide to stdout."""
    if wave == "wave1":
        print(generate_wave1_guide())
    elif wave == "wave2":
        print(generate_wave2_guide())
    else:
        print(f"[error] Unknown wave: {wave}. Use 'wave1' or 'wave2'.", file=sys.stderr)
        sys.exit(1)


# ---------------------------------------------------------------------------
# Execute command — print guide and log intent
# ---------------------------------------------------------------------------

def cmd_execute(wave: str, state: dict) -> None:
    """Print execution guide and log the intent to WORKLOG."""
    if wave in ("wave1", "all"):
        print(generate_wave1_guide())
        worklog_entry = (
            "**Action**: Wave 1 execution guide generated and printed for user.\n\n"
            "**Contacts**:\n"
            "- Send 1: Erin Chlopak / Campaign Legal Center (echlopak@campaignlegalcenter.org)\n"
            "- Send 2: Issue One general inbox (info@issueone.org)\n\n"
            "**Next step**: User executes sends with 90-minute stagger. "
            "Log results with --log-send after each send."
        )
        append_worklog(worklog_entry)
        save_state(state)

    if wave in ("wave2", "all"):
        print()
        print(generate_wave2_guide())
        worklog_entry = (
            "**Action**: Wave 2 execution guide generated and printed for user.\n\n"
            "**Contacts**:\n"
            "- Send 3: Darius Kemp / Common Cause CA (dkemp@commoncause.org)\n"
            "- Send 4: LWV California (lwvc@lwvc.org)\n"
            "- Send 5: Clean Money Action Fund (info@CAclean.org)\n\n"
            "**Next step**: User executes sends with 90-minute stagger. "
            "Log results with --log-send after each send."
        )
        append_worklog(worklog_entry)
        save_state(state)


# ---------------------------------------------------------------------------
# Log send
# ---------------------------------------------------------------------------

def cmd_log_send(send_num: int, timestamp: str, state: dict) -> None:
    """Record that a send was completed at a given timestamp."""
    contact = CONTACTS.get(send_num)
    if not contact:
        print(f"[error] Unknown send number: {send_num}. Valid: 1-5.", file=sys.stderr)
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
    save_state(state)

    worklog_entry = (
        f"**Send {send_num} logged**: {contact['org']}\n\n"
        f"- Email: {contact['primary_email']}\n"
        f"- Sent at: {timestamp}\n"
        f"- Reply status: PENDING\n\n"
        f"Wave {contact['wave']} | Contact: {contact['contact_name']}"
    )
    append_worklog(worklog_entry)

    print(f"[ok] Send {send_num} logged: {contact['org']} at {timestamp}")

    # Advise on next step
    next_num = send_num + 1
    if next_num in CONTACTS:
        next_contact = CONTACTS[next_num]
        if next_contact["wave"] == contact["wave"]:
            print(f"[next] Wait 90 minutes, then send Send {next_num}: {next_contact['org']} ({next_contact['primary_email']})")
        else:
            print(f"[next] Wave {contact['wave']} complete. Wave 2 can start 90+ minutes after this send, or next morning.")
    else:
        print("[next] All 5 sends complete. Set T+7 calendar reminder.")


# ---------------------------------------------------------------------------
# Log bounce
# ---------------------------------------------------------------------------

def cmd_log_bounce(send_num: int, use_fallback: bool, state: dict) -> None:
    """Record a bounce and optionally note fallback was sent."""
    contact = CONTACTS.get(send_num)
    if not contact:
        print(f"[error] Unknown send number: {send_num}.", file=sys.stderr)
        sys.exit(1)

    fallback = contact.get("backup_email")
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

    save_state(state)

    worklog_entry = (
        f"**Send {send_num} BOUNCE**: {contact['org']}\n\n"
        f"- Bounced: {contact['primary_email']}\n"
        f"- Fallback: {fallback if fallback else 'none available'}\n"
        f"- Fallback sent: {'YES' if bounce_record['fallback_sent'] else 'NO'}"
    )
    append_worklog(worklog_entry)

    if bounce_record["fallback_sent"]:
        print(f"[ok] Bounce logged for Send {send_num}. Fallback sent to: {fallback}")
    elif fallback:
        print(f"[warn] Bounce logged for Send {send_num}. Fallback address available: {fallback}")
        print(f"       Resend to {fallback} with the same subject and body, then run: --log-bounce {send_num} --fallback")
    else:
        print(f"[warn] Bounce logged for Send {send_num}. No backup address available.")
        print(f"       Contact: {contact['notes']}")


# ---------------------------------------------------------------------------
# Log reply
# ---------------------------------------------------------------------------

def cmd_log_reply(
    send_num: int,
    signal: str,
    summary: str,
    state: dict,
) -> None:
    """Record a reply for a given send number."""
    valid_signals = {"STRONG", "MODERATE", "WEAK", "NONE"}
    if signal not in valid_signals:
        print(f"[error] Signal must be one of: {', '.join(sorted(valid_signals))}", file=sys.stderr)
        sys.exit(1)

    contact = CONTACTS.get(send_num)
    if not contact:
        print(f"[error] Unknown send number: {send_num}.", file=sys.stderr)
        sys.exit(1)

    reply_record = {
        "send_num": send_num,
        "org": contact["org"],
        "signal": signal,
        "summary": summary,
        "logged_at": datetime.now(timezone.utc).isoformat(),
    }
    state["replies"][str(send_num)] = reply_record
    save_state(state)

    action_guidance = {
        "STRONG": (
            "Reply within 24 hours. "
            "Offer to send a one-page summary for internal distribution. "
            "This is a Phase 2 gate signal — log in DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md."
        ),
        "MODERATE": (
            "Log in execution log. "
            "If reply includes a named contact, note them for Wave 3 follow-up."
        ),
        "WEAK": (
            "Log in execution log. "
            "If 'unsubscribe' or 'please remove,' do not contact that address again."
        ),
        "NONE": "No action needed. Continue to Day 14 before drawing conclusions.",
    }

    worklog_entry = (
        f"**Reply received — Send {send_num}**: {contact['org']}\n\n"
        f"- Signal: {signal}\n"
        f"- Summary: {summary}\n"
        f"- Action: {action_guidance[signal]}"
    )
    append_worklog(worklog_entry)

    print(f"[ok] Reply logged: Send {send_num} — {signal}")
    print(f"     {action_guidance[signal]}")

    # Phase 2 gate advisory
    strong_count = sum(
        1 for r in state["replies"].values() if r.get("signal") == "STRONG"
    )
    print(f"\n[gate] Current STRONG reply count across all sends: {strong_count}/5")
    if strong_count >= 4:
        print("       Phase 2 gate: FULL ACTIVATION threshold met (4+ STRONG). Activate Domain 48 + Domain 57.")
    elif strong_count >= 2:
        print("       Phase 2 gate: MODERATE threshold met (2-3 STRONG). Activate Domain 48; hold Domain 57.")
    else:
        print("       Phase 2 gate: Below threshold (0-1 STRONG). Continue monitoring to Day 14.")


# ---------------------------------------------------------------------------
# T+7 checkpoint
# ---------------------------------------------------------------------------

def cmd_t7_check(state: dict) -> None:
    """Assess the T+7 checkpoint status across all 5 contacts."""
    print("\n=== T+7 Checkpoint Assessment ===")
    print(f"Checked: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}\n")

    sends_logged = len(state["sends"])
    replies_logged = len(state["replies"])
    strong_count = sum(
        1 for r in state["replies"].values() if r.get("signal") == "STRONG"
    )
    bounce_count = len(state["bounces"])

    print(f"Sends logged:     {sends_logged}/5")
    print(f"Bounces:          {bounce_count}")
    print(f"Replies logged:   {replies_logged}")
    print(f"STRONG signals:   {strong_count}")
    print()

    if sends_logged < 5:
        pending = [k for k in range(1, 6) if str(k) not in state["sends"]]
        print(f"[warn] Not all sends completed. Pending sends: {pending}")
        print(f"       Execute remaining sends before assessing T+7 results.")
        return

    # Phase 2 gate routing
    print("Phase 2 gate decision:")
    if strong_count >= 4:
        print("  FULL ACTIVATION — 4+ STRONG signals.")
        print("  Action: Activate Domain 48 + Domain 57 in parallel (June 21-27 window).")
    elif strong_count >= 2:
        print("  CONDITIONAL APPROVAL — 2-3 STRONG signals.")
        print("  Action: Activate Domain 48 sequentially. Hold Domain 57 for secondary June 28 checkpoint.")
    elif strong_count >= 1:
        print("  WEAK THRESHOLD — 1 STRONG signal.")
        print("  Action: Continue monitoring to Day 14 before activating either domain.")
        print("          Send Wave 3 follow-up to Common Cause CA only on Day 14 if still at 1 STRONG.")
    else:
        print("  BELOW THRESHOLD — 0 STRONG signals.")
        print("  Action: Hold both domains. User decision required.")
        print("          On Day 14: send brief follow-up to CLC (Send 1) and Common Cause CA (Send 3).")

    print()
    worklog_entry = (
        f"**T+7 checkpoint run**\n\n"
        f"- Sends logged: {sends_logged}/5\n"
        f"- Bounces: {bounce_count}\n"
        f"- Replies: {replies_logged}\n"
        f"- STRONG signals: {strong_count}\n\n"
        f"Gate decision: see console output."
    )
    append_worklog(worklog_entry)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Phase 2 Wave 1-2 Email Campaign Orchestration Script — Domain 51",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )

    parser.add_argument(
        "--status",
        action="store_true",
        help="Show current execution status for all 5 sends",
    )
    parser.add_argument(
        "--execute",
        choices=["wave1", "wave2", "all"],
        help="Print execution guide for the specified wave(s) and log intent to WORKLOG",
    )
    parser.add_argument(
        "--generate-guide",
        choices=["wave1", "wave2"],
        help="Print a self-contained execution guide to stdout (no WORKLOG entry)",
    )
    parser.add_argument(
        "--log-send",
        type=int,
        metavar="SEND_NUM",
        help="Record that a send was completed (1-5)",
    )
    parser.add_argument(
        "--time",
        type=str,
        default=None,
        help='Timestamp for --log-send (e.g., "2026-06-14 16:03 UTC"). Defaults to now.',
    )
    parser.add_argument(
        "--log-bounce",
        type=int,
        metavar="SEND_NUM",
        help="Record that a send bounced (1-5)",
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
        help="Record a reply received for a send (1-5)",
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

    # Load state once
    state = load_state()

    if args.status:
        cmd_status(state)

    elif args.execute:
        cmd_execute(args.execute, state)

    elif args.generate_guide:
        cmd_generate_guide(args.generate_guide)

    elif args.log_send is not None:
        timestamp = args.time or datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        cmd_log_send(args.log_send, timestamp, state)

    elif args.log_bounce is not None:
        cmd_log_bounce(args.log_bounce, args.fallback, state)

    elif args.log_reply is not None:
        if not args.signal:
            print("[error] --log-reply requires --signal (STRONG/MODERATE/WEAK/NONE)", file=sys.stderr)
            sys.exit(1)
        cmd_log_reply(args.log_reply, args.signal, args.summary, state)

    elif args.t7_check:
        cmd_t7_check(state)

    else:
        parser.print_help()
        sys.exit(0)


if __name__ == "__main__":
    main()
