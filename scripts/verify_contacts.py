#!/usr/bin/env python3
"""
verify_contacts.py — Contact verification helper for Phase 1 distribution.

Reads all contacts from the distribution infrastructure files and produces:
  1. A verification checklist with URL and email for each contact
  2. A CSV for import into a contact tracking spreadsheet
  3. A progress-tracking JSON file

Usage:
  uv run python scripts/verify_contacts.py              # Print checklist
  uv run python scripts/verify_contacts.py --csv        # Write CSV
  uv run python scripts/verify_contacts.py --batch 1    # Batch 1 contacts only
  uv run python scripts/verify_contacts.py --status     # Show verification progress

This script does NOT make network requests. Verification is manual — the script
produces the checklist and tracks what the user has confirmed.

To mark a contact as verified:
  Edit the VERIFIED_CONTACTS dict at the bottom of this file.
  Set verified=True and add the verification date and confirmed email.
"""

import json
import csv
import sys
from datetime import date
from pathlib import Path

# ---------------------------------------------------------------------------
# CONTACT DATABASE
# All contacts from policy-influencer-mapping.md, DISTRIBUTION_OUTREACH_CONTACTS.md,
# execution/tier-1-contact-batches.md, and DOMAIN_37_SEQUENCING_PLAN.md
# ---------------------------------------------------------------------------

CONTACTS = [
    # -------------------------------------------------------------------------
    # BATCH 1 — Days 1-3 (send first)
    # -------------------------------------------------------------------------
    {
        "id": "B1-001", "batch": 1, "send_order": 1,
        "name": "Ryan Goodman",
        "title": "Co-Editor-in-Chief, Just Security; Ehrenkranz Professor of Law",
        "institution": "Just Security / NYU School of Law",
        "email_primary": "ryan.goodman@nyu.edu",
        "email_alternate": "ryan@justsecurity.org",
        "verify_url": "https://www.law.nyu.edu/faculty/profiles/GOODMANR",
        "verify_url_alt": "https://justsecurity.org/about-us/",
        "domain_alignment": "Domain 28 (War Powers), Domain 29 (DOJ Capture), Domain 6 (Judicial Independence)",
        "tier": 1,
        "notes": "Fastest credibility move — Just Security publishes within days of submission",
    },
    {
        "id": "B1-002", "batch": 1, "send_order": 2,
        "name": "Wendy Weiser",
        "title": "Vice President, Democracy Program",
        "institution": "Brennan Center for Justice",
        "email_primary": "wweiser@brennancenter.org",
        "email_alternate": "brennancenter@nyu.edu",
        "verify_url": "https://www.brennancenter.org/experts/wendy-weiser",
        "verify_url_alt": "https://www.brennancenter.org/about/leadership",
        "domain_alignment": "Domain 1 (Voting Rights), Domain 33 (Gerrymandering), Domain 37 (Election Interference)",
        "tier": 1,
        "notes": "Single most important think tank contact — Brennan Center Democracy VP",
    },
    {
        "id": "B1-003", "batch": 1, "send_order": 3,
        "name": "Erica Chenoweth",
        "title": "Frank Stanton Professor; Director, Nonviolent Action Lab",
        "institution": "Harvard Kennedy School",
        "email_primary": "echenoweth@hks.harvard.edu",
        "email_alternate": "echenoweth@harvard.edu",
        "verify_url": "https://www.hks.harvard.edu/faculty/erica-chenoweth",
        "verify_url_alt": "https://carrcenter.hks.harvard.edu/nonviolent-action-lab",
        "domain_alignment": "Resistance meta-analysis; Domain 7 (Participation Rights); 160-case movement corpus",
        "tier": 1,
        "notes": "3.5% threshold research is the most-cited piece in the proposal",
    },
    {
        "id": "B1-004", "batch": 1, "send_order": 4,
        "name": "Ian Bassin",
        "title": "Co-Founder and Executive Director",
        "institution": "Protect Democracy",
        "email_primary": "ian@protectdemocracy.org",
        "email_alternate": None,
        "verify_url": "https://protectdemocracy.org/about/team/",
        "verify_url_alt": "https://protectdemocracy.org/work",
        "domain_alignment": "Domain 6 (Judicial Independence), Domain 29 (Prosecutorial Weaponization), Domain 37",
        "tier": 1,
        "notes": "Protect Democracy is active co-plaintiff in multiple cases documented in the framework",
    },
    {
        "id": "B1-005", "batch": 1, "send_order": 5,
        "name": "Marc Elias",
        "title": "Founder, Democracy Docket; Partner, Perkins Coie",
        "institution": "Democracy Docket / Perkins Coie",
        "email_primary": "marc@democracydocket.com",
        "email_alternate": "melias@perkinscoie.com",
        "verify_url": "https://democracydocket.com/about/",
        "verify_url_alt": "https://www.perkinscoie.com/en/professionals/marc-elias.html",
        "domain_alignment": "Domain 1 (Voting Rights litigation), Domain 33 (gerrymandering), Watson v. RNC tracking",
        "tier": 1,
        "notes": "Democracy Docket is primary tracker for cases documented in Domain 1 and Domain 37",
    },

    # -------------------------------------------------------------------------
    # BATCH 2 — Days 8-12
    # -------------------------------------------------------------------------
    {
        "id": "B2-001", "batch": 2, "send_order": 6,
        "name": "Nikolas Bowie",
        "title": "Louis D. Brandeis Professor of Law",
        "institution": "Harvard Law School",
        "email_primary": "nbowie@law.harvard.edu",
        "email_alternate": None,
        "verify_url": "https://hls.harvard.edu/faculty/nikolas-bowie/",
        "verify_url_alt": None,
        "domain_alignment": "Domain 2 (Institutional Integrity), Domain 6 (Judicial Independence), Domain 34 (Impoundment)",
        "tier": 1,
        "notes": None,
    },
    {
        "id": "B2-002", "batch": 2, "send_order": 7,
        "name": "Ruth Greenwood",
        "title": "Director, Voting Rights Litigation and Advocacy Clinic",
        "institution": "Harvard Law School",
        "email_primary": None,
        "email_alternate": None,
        "verify_url": "https://today.law.harvard.edu/voting-rights-litigation-and-advocacy-clinic-launches-at-hls",
        "verify_url_alt": "https://hls.harvard.edu/clinics/",
        "domain_alignment": "Domain 1 (Voting Rights), Domain 33 (Gerrymandering/Ballot Initiative Capture), Domain 37",
        "tier": 1,
        "notes": "Contact via HLS clinic page — no direct public email",
    },
    {
        "id": "B2-003", "batch": 2, "send_order": 8,
        "name": "Jonathan Gould",
        "title": "Professor of Law",
        "institution": "NYU School of Law",
        "email_primary": "j.gould@nyu.edu",
        "email_alternate": None,
        "verify_url": "https://its.law.nyu.edu/facultyprofiles/index.cfm?fuseaction=profile.overview&personid=59559",
        "verify_url_alt": None,
        "domain_alignment": "Domain 1, Domain 33, Domain 37",
        "tier": 1,
        "notes": "Former co-director, Edley Center for Law and Democracy",
    },
    {
        "id": "B2-004", "batch": 2, "send_order": 9,
        "name": "Michael Waldman",
        "title": "President and CEO",
        "institution": "Brennan Center for Justice",
        "email_primary": "brennancenter@nyu.edu",
        "email_alternate": None,
        "verify_url": "https://www.brennancenter.org/about/leadership",
        "verify_url_alt": None,
        "domain_alignment": "Full proposal — The Fight to Vote framing aligns throughout",
        "tier": 1,
        "notes": "Send after Wendy Weiser (B1-002) has landed — reinforcing signal",
    },
    {
        "id": "B2-005", "batch": 2, "send_order": 10,
        "name": "Molly E. Reynolds",
        "title": "Vice President and Director, Governance Studies",
        "institution": "Brookings Institution",
        "email_primary": "governance@brookings.edu",
        "email_alternate": None,
        "verify_url": "https://www.brookings.edu/programs/governance-studies/",
        "verify_url_alt": "https://www.brookings.edu/programs/governance-studies/staff/",
        "domain_alignment": "Domain 2 (Civil Service), Domain 26 (Accountability), Domain 34 (Congressional Power)",
        "tier": 1,
        "notes": None,
    },
    {
        "id": "B2-006", "batch": 2, "send_order": 11,
        "name": "Shahrzad Shams",
        "title": "Deputy Director, Democratic Institutions",
        "institution": "Roosevelt Institute",
        "email_primary": None,
        "email_alternate": None,
        "verify_url": "https://rooseveltinstitute.org/our-people/",
        "verify_url_alt": None,
        "domain_alignment": "Domain 2 (Institutional Integrity), Domain 26 (Accountability), Domain 34",
        "tier": 1,
        "notes": "Contact via Roosevelt Institute main line: 212.459.9600",
    },
    {
        "id": "B2-007", "batch": 2, "send_order": 12,
        "name": "Celine McNicholas",
        "title": "Director of Policy and General Counsel",
        "institution": "Economic Policy Institute",
        "email_primary": None,
        "email_alternate": None,
        "verify_url": "https://www.epi.org/about/staff/",
        "verify_url_alt": None,
        "domain_alignment": "Domain 17 (Labor — sectoral bargaining, PRO Act), Domain 2 (Civil Service/NLRB)",
        "tier": 1,
        "notes": "Contact via EPI: 202.775.8810",
    },
    {
        "id": "B2-008", "batch": 2, "send_order": 13,
        "name": "ACLU Voting Rights Project",
        "title": "Staff Attorney / Director",
        "institution": "ACLU",
        "email_primary": None,
        "email_alternate": None,
        "verify_url": "https://www.aclu.org/voting-rights",
        "verify_url_alt": "https://www.aclu.org/about/affiliates/national-offices",
        "domain_alignment": "Domain 1 (Voting Rights), Domain 7 (Civil Liberties), VRA Section 2 post-Callais",
        "tier": 1,
        "notes": "Contact via ACLU national office; identify current VRP director before sending",
    },

    # -------------------------------------------------------------------------
    # BATCH 3 — Days 15-21
    # -------------------------------------------------------------------------
    {
        "id": "B3-001", "batch": 3, "send_order": 14,
        "name": "Nicholas Stephanopoulos",
        "title": "Kirkland & Ellis Professor of Law",
        "institution": "Harvard Law School",
        "email_primary": "n.stephanopoulos@law.harvard.edu",
        "email_alternate": None,
        "verify_url": "https://hls.harvard.edu/faculty/nicholas-stephanopoulos/",
        "verify_url_alt": None,
        "domain_alignment": "Domain 1 (Electoral Reform — he invented the efficiency gap metric), Domain 33, Domain 37",
        "tier": 1,
        "notes": "Lead with efficiency gap metric in Domain 1",
    },
    {
        "id": "B3-002", "batch": 3, "send_order": 15,
        "name": "Erwin Chemerinsky",
        "title": "Dean and Jesse H. Choper Distinguished Professor of Law",
        "institution": "UC Berkeley School of Law",
        "email_primary": "chemerins@law.berkeley.edu",
        "email_alternate": None,
        "verify_url": "https://www.law.berkeley.edu/our-faculty/faculty-profiles/erwin-chemerinsky/",
        "verify_url_alt": None,
        "domain_alignment": "Full proposal — he runs We Hold These Truths democracy education project; Domain 6, Domain 29",
        "tier": 1,
        "notes": "Lead with We Hold These Truths alignment",
    },
    {
        "id": "B3-003", "batch": 3, "send_order": 16,
        "name": "Theda Skocpol",
        "title": "Victor S. Thomas Professor of Government and Sociology",
        "institution": "Harvard Kennedy School / GSAS",
        "email_primary": "skocpol@fas.harvard.edu",
        "email_alternate": None,
        "verify_url": "https://scholar.harvard.edu/thedaskocpol",
        "verify_url_alt": None,
        "domain_alignment": "Resistance meta-analysis; Domain 3 (Democratic Participation); Diminished Democracy alignment",
        "tier": 1,
        "notes": None,
    },
    {
        "id": "B3-004", "batch": 3, "send_order": 17,
        "name": "Janai Nelson",
        "title": "President and Director-Counsel",
        "institution": "NAACP Legal Defense Fund",
        "email_primary": None,
        "email_alternate": None,
        "verify_url": "https://www.naacpldf.org/about-us/leadership/",
        "verify_url_alt": None,
        "domain_alignment": "Domain 22 (Racial Justice), Domain 29 (Prosecutorial Weaponization), Domain 1 (Voting Rights)",
        "tier": 1,
        "notes": "Contact via LDF media office; lead with Domain 22 + Domain 29 (SPLC prosecutorial weaponization)",
    },
    {
        "id": "B3-005", "batch": 3, "send_order": 18,
        "name": "Damon Hewitt",
        "title": "President and Executive Director",
        "institution": "Lawyers' Committee for Civil Rights Under Law",
        "email_primary": None,
        "email_alternate": None,
        "verify_url": "https://lawyerscommittee.org/about/staff/",
        "verify_url_alt": None,
        "domain_alignment": "Domain 1 (Voting Rights), Domain 7 (Civil Rights), Election Protection coalition alignment",
        "tier": 1,
        "notes": None,
    },
    {
        "id": "B3-006", "batch": 3, "send_order": 19,
        "name": "Ian Bassin",
        "title": "Co-Founder and Executive Director",
        "institution": "Protect Democracy",
        "email_primary": "ian@protectdemocracy.org",
        "email_alternate": None,
        "verify_url": "https://protectdemocracy.org/about/team/",
        "verify_url_alt": None,
        "domain_alignment": "Domain 6, Domain 29, Domain 37 (all active litigation areas)",
        "tier": 1,
        "notes": "Already in Batch 1. This batch-3 entry is for Path A+37 Domain 37 follow-up",
    },
    {
        "id": "B3-007", "batch": 3, "send_order": 20,
        "name": "Olatunde Johnson",
        "title": "Ruth Bader Ginsburg Professor of Law; Faculty Director, Constitutional Democracy Initiative",
        "institution": "Columbia Law School",
        "email_primary": "oj2109@columbia.edu",
        "email_alternate": None,
        "verify_url": "https://constitutional-democracy.law.columbia.edu/directory/olatunde-c-johnson",
        "verify_url_alt": None,
        "domain_alignment": "Domain 2, Domain 6, Domain 7, Domain 29 — CDI is most structurally aligned law school center",
        "tier": 1,
        "notes": "Columbia email format is initials+number@columbia.edu; verify",
    },
    {
        "id": "B3-008", "batch": 3, "send_order": 21,
        "name": "Archon Fung",
        "title": "Winthrop Laflin McCormack Professor of Citizenship and Self-Government",
        "institution": "Harvard Kennedy School / Ash Center",
        "email_primary": "ash_center@hks.harvard.edu",
        "email_alternate": None,
        "verify_url": "https://ash.harvard.edu",
        "verify_url_alt": None,
        "domain_alignment": "Domain 3 (Citizens' Assemblies, Participatory Budgeting), Domain 9, Domain 26",
        "tier": 1,
        "notes": "Lead with Domain 3 — Ash Center is the leading academic center on democratic innovation",
    },
    {
        "id": "B3-009", "batch": 3, "send_order": 22,
        "name": "Pamela Karlan",
        "title": "Thomas Reid Professor of Law; Co-Director, Supreme Court Litigation Clinic",
        "institution": "Stanford Law School",
        "email_primary": "karlan@law.stanford.edu",
        "email_alternate": None,
        "verify_url": "https://law.stanford.edu/pamela-s-karlan/",
        "verify_url_alt": None,
        "domain_alignment": "Domain 1 (Voting Rights), Domain 6 (Judicial Independence), Domain 35 (post-Loper SCOTUS)",
        "tier": 1,
        "notes": None,
    },
    {
        "id": "B3-010", "batch": 3, "send_order": 23,
        "name": "Ian Bassin / Justin Florence",
        "title": "Executive Director / Legal Director",
        "institution": "Protect Democracy",
        "email_primary": "ian@protectdemocracy.org",
        "email_alternate": None,
        "verify_url": "https://protectdemocracy.org/about/team/",
        "verify_url_alt": None,
        "domain_alignment": "Domain 29 (DOJ Capture), Domain 6 (Judicial Independence) — they are co-plaintiffs",
        "tier": 1,
        "notes": "Second wave Protect Democracy contact",
    },
    {
        "id": "B3-011", "batch": 3, "send_order": 24,
        "name": "Jacob Hacker",
        "title": "Stanley B. Resor Professor of Political Science",
        "institution": "Yale",
        "email_primary": "jacob.hacker@yale.edu",
        "email_alternate": None,
        "verify_url": "https://politicalscience.yale.edu/people/jacob-hacker",
        "verify_url_alt": None,
        "domain_alignment": "Domain 5 (Fiscal Reform), Domain 17 (Labor), Domain 18 (Social Safety Net)",
        "tier": 1,
        "notes": "Lead with Power and Progress framing alignment",
    },
    {
        "id": "B3-012", "batch": 3, "send_order": 25,
        "name": "Todd Tucker",
        "title": "Director, Industrial Policy and Trade",
        "institution": "Roosevelt Institute",
        "email_primary": None,
        "email_alternate": None,
        "verify_url": "https://rooseveltinstitute.org/authors/todd-tucker/",
        "verify_url_alt": None,
        "domain_alignment": "Domain 23 (Trade Policy, Tariff Unilateralism) — his work directly overlaps",
        "tier": 1,
        "notes": None,
    },

    # -------------------------------------------------------------------------
    # DOMAIN 37 TIER — Path A+37 only (Phase B, Week 9+)
    # -------------------------------------------------------------------------
    {
        "id": "D37-001", "batch": "D37", "send_order": 26,
        "name": "Joanna Lydgate",
        "title": "CEO",
        "institution": "States United Democracy Center",
        "email_primary": None,
        "email_alternate": None,
        "verify_url": "https://statesuniteddemocracy.org/team/",
        "verify_url_alt": None,
        "domain_alignment": "Domain 37 (Election Security), Domain 33 (State Legislative Autocratization)",
        "tier": "D37",
        "notes": "Domain 37 Phase B contact — verify at Week 9",
    },
    {
        "id": "D37-002", "batch": "D37", "send_order": 27,
        "name": "Lawyers' Committee — Voting Rights Project",
        "title": "Director, Voting Rights Project",
        "institution": "Lawyers' Committee for Civil Rights",
        "email_primary": None,
        "email_alternate": None,
        "verify_url": "https://lawyerscommittee.org/project/voting-rights-project/",
        "verify_url_alt": None,
        "domain_alignment": "Domain 37 (Election Security), Domain 1 (VRA Section 2 post-Callais)",
        "tier": "D37",
        "notes": "Domain 37 Phase B contact — verify at Week 9",
    },
    {
        "id": "D37-003", "batch": "D37", "send_order": 28,
        "name": "Common Cause",
        "title": "Policy Director",
        "institution": "Common Cause",
        "email_primary": None,
        "email_alternate": None,
        "verify_url": "https://www.commoncause.org/about-us/who-we-are/staff/",
        "verify_url_alt": None,
        "domain_alignment": "Domain 37 (Election Security), Domain 33 (Redistricting Reform)",
        "tier": "D37",
        "notes": "Domain 37 Phase B contact — verify at Week 9",
    },
    {
        "id": "D37-004", "batch": "D37", "send_order": 29,
        "name": "ACLU Voting Rights Project",
        "title": "Staff Attorney / Director",
        "institution": "ACLU",
        "email_primary": None,
        "email_alternate": None,
        "verify_url": "https://www.aclu.org/voting-rights",
        "verify_url_alt": None,
        "domain_alignment": "Domain 37 (Election Security), VRA Section 11(b), HAVA enforcement",
        "tier": "D37",
        "notes": "Domain 37 Phase B contact — cross-reference with B2-008",
    },
    {
        "id": "D37-005", "batch": "D37", "send_order": 30,
        "name": "Democracy Docket — Election Security Staff",
        "title": "Staff Attorney",
        "institution": "Democracy Docket",
        "email_primary": None,
        "email_alternate": None,
        "verify_url": "https://democracydocket.com/about/",
        "verify_url_alt": None,
        "domain_alignment": "Domain 37 (Election Security), Watson v. RNC, Louisiana v. Callais",
        "tier": "D37",
        "notes": "Marc Elias is in Batch 1. This entry is for Domain 37 Phase B follow-up with litigation staff",
    },

    # -------------------------------------------------------------------------
    # ADDITIONAL TIER 2 CONTACTS (for Weeks 3-5 outreach beyond Tier 1)
    # -------------------------------------------------------------------------
    {
        "id": "T2-001", "batch": "T2", "send_order": 31,
        "name": "Heather Gerken",
        "title": "President, Ford Foundation (former Yale Law Dean)",
        "institution": "Ford Foundation / Yale Law School",
        "email_primary": "heather.gerken@fordfoundation.org",
        "email_alternate": "gerken@law.yale.edu",
        "verify_url": "https://www.fordfoundation.org/about/people/heather-gerken/",
        "verify_url_alt": "https://law.yale.edu/heather-gerken",
        "domain_alignment": "Domain 1, Domain 9 (Federalism), Domain 33, Domain 37 — she now controls Ford grantmaking",
        "tier": 2,
        "notes": "Warm introduction through Yale Law connection strongly preferred over cold email",
    },
    {
        "id": "T2-002", "batch": "T2", "send_order": 32,
        "name": "Yuval Levin",
        "title": "Director, Social, Cultural, and Constitutional Studies; Beth and Ravenel Curry Scholar",
        "institution": "American Enterprise Institute",
        "email_primary": "ylevin@aei.org",
        "email_alternate": None,
        "verify_url": "https://www.aei.org/profile/yuval-levin/",
        "verify_url_alt": None,
        "domain_alignment": "Domain 2 (Institutional Integrity) — cross-partisan frame; institutional character argument",
        "tier": 2,
        "notes": "Use cross-partisan framing exclusively; lead with institutional integrity, not political reform",
    },
    {
        "id": "T2-003", "batch": "T2", "send_order": 33,
        "name": "A.J. D'Amico",
        "title": "Vice President, Information and Society Program",
        "institution": "Knight Foundation",
        "email_primary": None,
        "email_alternate": None,
        "verify_url": "https://knightfoundation.org/about/",
        "verify_url_alt": None,
        "domain_alignment": "Domain 8 (Information Ecosystem), Domain 4 (Media/Platform Accountability)",
        "tier": 2,
        "notes": "Foundation contact — use Foundation/Movement-Building email template",
    },
    {
        "id": "T2-004", "batch": "T2", "send_order": 34,
        "name": "Democracy Fund",
        "title": "Program Director",
        "institution": "Democracy Fund",
        "email_primary": None,
        "email_alternate": None,
        "verify_url": "https://www.democracyfund.org/about/staff/",
        "verify_url_alt": None,
        "domain_alignment": "Domain 1, Domain 37 — core Democracy Fund issue areas",
        "tier": 2,
        "notes": "Identify current program director before sending",
    },
    {
        "id": "T2-005", "batch": "T2", "send_order": 35,
        "name": "Suzanne Mettler",
        "title": "John L. Senior Professor of American Institutions",
        "institution": "Cornell",
        "email_primary": "sm235@cornell.edu",
        "email_alternate": None,
        "verify_url": "https://government.cornell.edu/suzanne-mettler",
        "verify_url_alt": None,
        "domain_alignment": "Domain 3 (Civic Infrastructure), Domain 18 (Social Safety Net), Domain 26",
        "tier": 2,
        "notes": "Lead with submerged state research connection",
    },
]

# ---------------------------------------------------------------------------
# VERIFICATION TRACKING
# Edit this dict to mark contacts as verified before sending.
# Format: "contact_id": {"verified": True, "date": "2026-05-XX", "email_confirmed": "..."}
# ---------------------------------------------------------------------------

VERIFIED_CONTACTS: dict[str, dict] = {
    # Batch 1 — position-verified April 29, 2026 (Session 658/662)
    "B1-001": {"verified": True, "date": "2026-04-29", "email_confirmed": None,
               "notes": "Position confirmed via justsecurity.org + NYU Law faculty page"},
    "B1-002": {"verified": True, "date": "2026-04-29", "email_confirmed": None,
               "notes": "Position confirmed via brennancenter.org team page"},
    "B1-003": {"verified": True, "date": "2026-04-29", "email_confirmed": None,
               "notes": "Position confirmed via HKS faculty directory"},
    "B1-004": {"verified": True, "date": "2026-04-29", "email_confirmed": None,
               "notes": "Position confirmed via protectdemocracy.org team page"},
    "B1-005": {"verified": True, "date": "2026-04-29", "email_confirmed": None,
               "notes": "Position confirmed via democracydocket.com + Perkins Coie"},
    # All others: unverified. Verify at send time.
}

# ---------------------------------------------------------------------------
# OUTPUT FUNCTIONS
# ---------------------------------------------------------------------------

def print_checklist(batch_filter: int | str | None = None):
    """Print a human-readable verification checklist."""
    contacts = CONTACTS
    if batch_filter is not None:
        contacts = [c for c in CONTACTS if str(c["batch"]) == str(batch_filter)]

    total = len(contacts)
    verified = sum(1 for c in contacts if VERIFIED_CONTACTS.get(c["id"], {}).get("verified"))

    print(f"\nContact Verification Checklist — Phase 1 Distribution")
    print(f"Total contacts: {total}  |  Verified: {verified}  |  Pending: {total - verified}")
    print(f"Generated: {date.today()}\n")
    print("-" * 80)

    current_batch = None
    for c in contacts:
        if c["batch"] != current_batch:
            current_batch = c["batch"]
            if isinstance(current_batch, int):
                batch_label = f"BATCH {current_batch}"
                if current_batch == 1:
                    batch_label += " — Send Days 1-3 (VERIFY IMMEDIATELY BEFORE SEND)"
                elif current_batch == 2:
                    batch_label += " — Send Days 8-12"
                elif current_batch == 3:
                    batch_label += " — Send Days 15-21"
            else:
                batch_label = f"BATCH {current_batch}"
                if current_batch == "D37":
                    batch_label += " — Path A+37 only (Phase B, Week 9+)"
                elif current_batch == "T2":
                    batch_label += " — Tier 2 (Weeks 3-5)"
            print(f"\n{'=' * 40}")
            print(f"  {batch_label}")
            print(f"{'=' * 40}")

        vdata = VERIFIED_CONTACTS.get(c["id"], {})
        is_verified = vdata.get("verified", False)
        status = "[V]" if is_verified else "[ ]"
        email_conf = vdata.get("email_confirmed") or c["email_primary"] or "(no email — see verify_url)"
        verified_note = f" — verified {vdata['date']}" if is_verified else ""

        print(f"\n{status} {c['id']:8s}  {c['name']}")
        print(f"         {c['title']}")
        print(f"         {c['institution']}")
        print(f"         Email: {email_conf}{verified_note}")
        if c["email_alternate"]:
            print(f"         Alt email: {c['email_alternate']}")
        print(f"         Verify at: {c['verify_url']}")
        print(f"         Domains: {c['domain_alignment'][:70]}...")
        if c["notes"]:
            print(f"         Note: {c['notes']}")

    print("\n" + "-" * 80)
    print(f"Verification complete: {verified}/{total}")
    print(f"\nTo mark as verified: edit VERIFIED_CONTACTS dict in this script.")
    print(f"To write CSV: uv run python scripts/verify_contacts.py --csv")


def write_csv():
    """Write contact list to CSV for spreadsheet import."""
    output_dir = Path(__file__).parent / "filled_output"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "contact_verification_checklist.csv"

    fieldnames = [
        "id", "batch", "send_order", "name", "title", "institution",
        "email_primary", "email_alternate", "verify_url", "verify_url_alt",
        "domain_alignment", "tier", "notes",
        "verified", "verification_date", "email_confirmed", "verification_notes",
    ]

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for c in CONTACTS:
            vdata = VERIFIED_CONTACTS.get(c["id"], {})
            row = {
                **c,
                "verified": vdata.get("verified", False),
                "verification_date": vdata.get("date", ""),
                "email_confirmed": vdata.get("email_confirmed", ""),
                "verification_notes": vdata.get("notes", ""),
            }
            writer.writerow(row)

    print(f"CSV written to: {output_path}")
    print(f"Total contacts: {len(CONTACTS)}")
    print(f"Import into Google Sheets or Excel for tracking.")


def show_status():
    """Show verification progress summary."""
    total = len(CONTACTS)
    verified = sum(1 for c in CONTACTS if VERIFIED_CONTACTS.get(c["id"], {}).get("verified"))
    batch_counts = {}
    for c in CONTACTS:
        b = str(c["batch"])
        if b not in batch_counts:
            batch_counts[b] = {"total": 0, "verified": 0}
        batch_counts[b]["total"] += 1
        if VERIFIED_CONTACTS.get(c["id"], {}).get("verified"):
            batch_counts[b]["verified"] += 1

    print(f"\nVerification Status — {date.today()}")
    print(f"Overall: {verified}/{total} verified\n")
    print(f"{'Batch':<8}  {'Verified':<10}  {'Total':<8}  Status")
    print("-" * 45)
    for batch, counts in sorted(batch_counts.items()):
        pct = int(counts["verified"] / counts["total"] * 100)
        bar = "#" * (pct // 10) + "." * (10 - pct // 10)
        print(f"  {batch:<8}  {counts['verified']:<10}  {counts['total']:<8}  [{bar}] {pct}%")


# ---------------------------------------------------------------------------
# ENTRY POINT
# ---------------------------------------------------------------------------

def main():
    args = sys.argv[1:]
    if "--csv" in args:
        write_csv()
    elif "--status" in args:
        show_status()
    elif "--batch" in args:
        idx = args.index("--batch")
        batch_val = args[idx + 1] if idx + 1 < len(args) else None
        print_checklist(batch_filter=batch_val)
    else:
        print_checklist()


if __name__ == "__main__":
    main()
