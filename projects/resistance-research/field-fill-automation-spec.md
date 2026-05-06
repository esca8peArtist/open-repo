---
title: "Field-Fill Automation Specification"
created: 2026-05-06
status: production-ready
purpose: "Complete spec for identifying, sourcing, and batch-filling all template placeholder fields across distribution files. Includes Python script skeleton and contact verification workflow."
applies_to: "PHASE_1_EMAIL_TEMPLATES.md, distribution-substack-drafts.md, distribution-reddit-templates.md, distribution-institutional-outreach-templates.md"
---

# Field-Fill Automation Specification

## Summary

Three template files and one batch email file contain placeholder fields that must be
filled before distribution. The total fill operation — using the Python script in Section 4 —
takes approximately 8 minutes once the input values are assembled. Manual find-replace is
viable but slower and error-prone across four files.

This document specifies every placeholder, its value source, and the fill method.

---

## 1. Complete Placeholder Inventory

### 1.1 URL Placeholders (Highest Priority — Same Values Across All Files)

These six URLs appear in every distribution file. All six Gists are already live.
The only task is copying the URL values into the fill script input.

| Placeholder | Document | Gist URL (already live) |
|-------------|----------|------------------------|
| `{{PROPOSAL_URL}}` | Full 35-domain proposal | https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261 |
| `{{EXEC_SUMMARY_URL}}` | 2-page executive summary | https://gist.github.com/esca8peArtist/2869da6eaeb15a47246ade3bbbc4a3f4 |
| `{{LITIGATION_TRACKER_URL}}` | Litigation Tracker 2026 | https://gist.github.com/esca8peArtist/418d51bda087f15a04d685ab171a5ee0 |
| `{{FIRST_AMENDMENT_TRACKER_URL}}` | First Amendment Suppression | https://gist.github.com/esca8peArtist/10d0a86e386e6c3c11c3830295a6503c |
| `{{ENV_ROLLBACKS_URL}}` | Environmental Rollbacks | https://gist.github.com/esca8peArtist/87e2bdb931b77480e56a08044c567bc4 |
| `{{CONSENT_DECREE_TRACKER_URL}}` | Police Consent Decree | https://gist.github.com/esca8peArtist/1f5cb28527c98d12526c14302c725731 |
| `{{DOMAIN_37_URL}}` | Domain 37 standalone | PENDING — fill after Gist creation (Path A+37 only) |

Also appears as legacy `[link]` bracket syntax in some template files (older format).
The fill script handles both `{{PLACEHOLDER}}` and `[link]` forms — see Section 4.

### 1.2 Identity Placeholders (Institutional Outreach Only)

These appear only in `distribution-institutional-outreach-templates.md` and the
five Batch 1 email templates in `PHASE_1_EMAIL_TEMPLATES.md`.

| Placeholder | Value Source | Fill Method |
|-------------|-------------|-------------|
| `{{YOUR_NAME}}` | User's preferred name for professional outreach | Manual or script |
| `{{YOUR_CONTACT_INFO}}` | Email address + optional Signal/website | Manual or script |
| `[Your name]` | Legacy bracket form of the above | Script (same replacement) |
| `[Contact information]` | Legacy bracket form | Script (same replacement) |

Reddit and Substack templates do not require identity fields — they support pseudonymous
distribution. Do not add identity fields to those templates.

### 1.3 Content Placeholders (Per-Email — Cannot Be Batch-Filled)

These placeholders require 5–10 minutes of per-contact research and cannot be automated.
They must be filled manually immediately before sending each email.

| Placeholder | Appears In | Value Source |
|-------------|-----------|-------------|
| `{{RECENT_JUST_SECURITY_ARTICLE}}` | Email 1 (Goodman) | Visit justsecurity.org — most recent relevant article title + date |
| `{{RECENT_WEISER_PUBLICATION}}` | Email 2 (Weiser) | Visit brennancenter.org — Weiser's most recent Voting Rights report |
| `{{RECENT_CHENOWETH_WORK}}` | Email 3 (Chenoweth) | Visit hks.harvard.edu — most recent Nonviolent Action Lab publication |
| `{{BASSIN_RECENT_FILING}}` | Email 4 (Bassin) | Visit protectdemocracy.org/work — most recent litigation or public statement |
| `{{ELIAS_RECENT_CASE}}` | Email 5 (Elias) | Visit democracydocket.com — most recent active case in a swing state |
| `{{DOMAIN_COUNT}}` | All emails | 35 (or 34 if Path A+37 Phase 1a framing) |
| `{{PATH_SPECIFIC_BLOCK}}` | All emails | Replace the `[PATH A]` / `[PATH A+37]` / `[PATH B]` blocks per chosen path |

### 1.4 Date Placeholders

| Placeholder | Value | Notes |
|-------------|-------|-------|
| `{{CURRENT_DATE}}` | 2026-05-06 (or date of send) | Use ISO format YYYY-MM-DD in document headers; use "May 6, 2026" in email body text |
| `{{FRAMEWORK_VERSION}}` | May 2026 | Fixed for this distribution cycle |
| `[DATE]` | Same as above | Legacy bracket form in tracker footers |

### 1.5 Substack-Specific Placeholders

| Placeholder | Appears In | Value |
|-------------|-----------|-------|
| `[your Substack handle]` | distribution-substack-drafts.md (all posts) | Your Substack username — set this once |
| `[SUBSTACK_URL]` | Post bodies with self-reference | https://[handle].substack.com |

### 1.6 Reddit-Specific Placeholders

| Placeholder | Appears In | Value |
|-------------|-----------|-------|
| `[PROPOSAL_LINK]` | distribution-reddit-templates.md | Same as `{{PROPOSAL_URL}}` |
| `[SUMMARY_LINK]` | distribution-reddit-templates.md | Same as `{{EXEC_SUMMARY_URL}}` |

---

## 2. Structured Field Spec Table

Complete mapping of every placeholder to its value source and fill method.

| Field Name | Value Source | Fill Method | Files Affected | Priority |
|------------|-------------|-------------|---------------|----------|
| `{{PROPOSAL_URL}}` | Live Gist (already known) | Script | All 4 template files | P0 — fill first |
| `{{EXEC_SUMMARY_URL}}` | Live Gist | Script | All 4 template files | P0 |
| `{{LITIGATION_TRACKER_URL}}` | Live Gist | Script | All 4 template files | P0 |
| `{{FIRST_AMENDMENT_TRACKER_URL}}` | Live Gist | Script | All 4 template files | P0 |
| `{{ENV_ROLLBACKS_URL}}` | Live Gist | Script | All 4 template files | P0 |
| `{{CONSENT_DECREE_TRACKER_URL}}` | Live Gist | Script | All 4 template files | P0 |
| `{{DOMAIN_37_URL}}` | Create Gist first | Script after creation | Path A+37 emails only | P1 |
| `{{YOUR_NAME}}` | User provides | Script or manual | Institutional templates + emails | P1 |
| `{{YOUR_CONTACT_INFO}}` | User provides | Script or manual | Institutional templates + emails | P1 |
| `[link]` (legacy) | Same as Proposal URL | Script (regex) | Older template files | P1 |
| `[Your name]` (legacy) | Same as YOUR_NAME | Script (regex) | Older template files | P1 |
| `[Contact information]` (legacy) | Same as YOUR_CONTACT_INFO | Script (regex) | Older template files | P1 |
| `{{DOMAIN_COUNT}}` | "35" or "34" per path | Script | Email templates | P1 |
| `{{RECENT_JUST_SECURITY_ARTICLE}}` | Manual research | Manual only | Email 1 | P2 — before send |
| `{{RECENT_WEISER_PUBLICATION}}` | Manual research | Manual only | Email 2 | P2 |
| `{{RECENT_CHENOWETH_WORK}}` | Manual research | Manual only | Email 3 | P2 |
| `{{BASSIN_RECENT_FILING}}` | Manual research | Manual only | Email 4 | P2 |
| `{{ELIAS_RECENT_CASE}}` | Manual research | Manual only | Email 5 | P2 |
| `{{PATH_SPECIFIC_BLOCK}}` | Path choice | Manual selection | All 5 emails | P2 |
| `[your Substack handle]` | User provides | Script or manual | Substack drafts | P1 |
| `[PROPOSAL_LINK]` | Live Gist | Script (regex) | Reddit templates | P0 |
| `[SUMMARY_LINK]` | Live Gist | Script (regex) | Reddit templates | P0 |
| `{{CURRENT_DATE}}` | Today's date | Script | Template headers | P1 |
| `{{FRAMEWORK_VERSION}}` | "May 2026" | Script | Template headers | P1 |

---

## 3. Python Script Skeleton for Batch Field Replacement

Save as `scripts/fill_templates.py`. Run with `uv run python scripts/fill_templates.py`.

```python
#!/usr/bin/env python3
"""
fill_templates.py — Batch field replacement for resistance-research distribution templates.

Usage:
  uv run python scripts/fill_templates.py

Before running:
  1. Edit the FIELD_VALUES dict below with your actual values.
  2. Set DISTRIBUTION_PATH to "A", "A+37", or "B".
  3. Confirm DRY_RUN = True for a preview, then set to False to apply.

The script writes modified copies to scripts/filled_output/ and does NOT overwrite
the source templates. Review the output before copying to your email client.
"""

import re
import shutil
from datetime import date
from pathlib import Path

# ---------------------------------------------------------------------------
# CONFIGURATION — edit these before running
# ---------------------------------------------------------------------------

DISTRIBUTION_PATH = "A+37"   # "A" | "A+37" | "B"

FIELD_VALUES = {
    # URL placeholders — all six live Gists
    "{{PROPOSAL_URL}}":
        "https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261",
    "{{EXEC_SUMMARY_URL}}":
        "https://gist.github.com/esca8peArtist/2869da6eaeb15a47246ade3bbbc4a3f4",
    "{{LITIGATION_TRACKER_URL}}":
        "https://gist.github.com/esca8peArtist/418d51bda087f15a04d685ab171a5ee0",
    "{{FIRST_AMENDMENT_TRACKER_URL}}":
        "https://gist.github.com/esca8peArtist/10d0a86e386e6c3c11c3830295a6503c",
    "{{ENV_ROLLBACKS_URL}}":
        "https://gist.github.com/esca8peArtist/87e2bdb931b77480e56a08044c567bc4",
    "{{CONSENT_DECREE_TRACKER_URL}}":
        "https://gist.github.com/esca8peArtist/1f5cb28527c98d12526c14302c725731",

    # Domain 37 — fill after creating the Gist (Path A+37 only)
    # Leave empty string if on Path A or B; the script will warn if it finds
    # {{DOMAIN_37_URL}} in the output with an empty replacement.
    "{{DOMAIN_37_URL}}": "",   # <-- paste Domain 37 Gist URL here for Path A+37

    # Identity fields — fill with your own information
    "{{YOUR_NAME}}": "",       # <-- e.g. "Alex W." or "Democratic Renewal Research Team"
    "{{YOUR_CONTACT_INFO}}": "", # <-- e.g. "wanka95@gmail.com"

    # Content metadata
    "{{DOMAIN_COUNT}}": "35" if DISTRIBUTION_PATH in ("A", "B") else "34",
    "{{CURRENT_DATE}}": date.today().strftime("%B %-d, %Y"),
    "{{FRAMEWORK_VERSION}}": "May 2026",

    # Substack handle — fill with your actual handle
    "[your Substack handle]": "",  # <-- e.g. "democraticrenewal"
}

# Legacy bracket-form aliases (map to same values as above)
LEGACY_ALIASES = {
    "[link]": FIELD_VALUES["{{PROPOSAL_URL}}"],
    "[Your name]": FIELD_VALUES["{{YOUR_NAME}}"],
    "[Contact information]": FIELD_VALUES["{{YOUR_CONTACT_INFO}}"],
    "[PROPOSAL_LINK]": FIELD_VALUES["{{PROPOSAL_URL}}"],
    "[SUMMARY_LINK]": FIELD_VALUES["{{EXEC_SUMMARY_URL}}"],
    "[DATE]": date.today().strftime("%B %-d, %Y"),
}

# Files to process (relative to project root)
PROJECT_ROOT = Path(__file__).parent.parent / "projects" / "resistance-research"

TARGET_FILES = [
    "distribution-substack-drafts.md",
    "distribution-reddit-templates.md",
    "distribution-institutional-outreach-templates.md",
    "PHASE_1_EMAIL_TEMPLATES.md",
]

OUTPUT_DIR = Path(__file__).parent / "filled_output"
DRY_RUN = True   # Set to False to write files

# ---------------------------------------------------------------------------
# PATH-SPECIFIC BLOCK HANDLING
# ---------------------------------------------------------------------------

PATH_BLOCK_PATTERN = re.compile(
    r"\[PATH A\](.*?)\[PATH A\+37\](.*?)\[PATH B\](.*?)(?=\n\n|\Z)",
    re.DOTALL,
)

def select_path_block(text: str, path: str) -> str:
    """Replace the [PATH X] inline selectors with only the chosen path's content."""
    def replacer(match: re.Match) -> str:
        path_a_text = match.group(1).strip()
        path_a37_text = match.group(2).strip()
        path_b_text = match.group(3).strip()
        if path == "A":
            return path_a_text
        elif path == "A+37":
            return path_a37_text
        else:
            return path_b_text
    return PATH_BLOCK_PATTERN.sub(replacer, text)

# ---------------------------------------------------------------------------
# SAFETY CHECKS
# ---------------------------------------------------------------------------

def check_unfilled_fields(text: str, filename: str) -> list[str]:
    """Return list of placeholder strings still present after fill."""
    problems = []
    # Check for any remaining {{...}} placeholders
    remaining = re.findall(r"\{\{[A-Z_]+\}\}", text)
    for r in remaining:
        problems.append(f"  UNFILLED in {filename}: {r}")
    # Check for empty-value replacements that left the placeholder
    if "{{DOMAIN_37_URL}}" in text or "[domain 37 link]" in text:
        if DISTRIBUTION_PATH == "A+37":
            problems.append(f"  WARNING in {filename}: Domain 37 URL placeholder still present — create Gist first")
    if "{{YOUR_NAME}}" in text or "[Your name]" in text:
        problems.append(f"  WARNING in {filename}: YOUR_NAME not set")
    if "{{YOUR_CONTACT_INFO}}" in text or "[Contact information]" in text:
        problems.append(f"  WARNING in {filename}: YOUR_CONTACT_INFO not set")
    return problems

# ---------------------------------------------------------------------------
# MAIN FILL LOGIC
# ---------------------------------------------------------------------------

def fill_file(source_path: Path, output_path: Path) -> list[str]:
    """Fill all placeholders in a single file. Returns list of warnings."""
    text = source_path.read_text(encoding="utf-8")

    # Apply path-specific block selection
    text = select_path_block(text, DISTRIBUTION_PATH)

    # Apply {{PLACEHOLDER}} substitutions
    for placeholder, value in FIELD_VALUES.items():
        if value:  # Only replace if value is non-empty
            text = text.replace(placeholder, value)

    # Apply legacy [bracket] substitutions
    for placeholder, value in LEGACY_ALIASES.items():
        if value:
            text = text.replace(placeholder, value)

    warnings = check_unfilled_fields(text, source_path.name)

    if not DRY_RUN:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(text, encoding="utf-8")

    return warnings

def main():
    all_warnings = []

    # Validate that critical fields are set
    if not FIELD_VALUES["{{YOUR_NAME}}"]:
        print("ERROR: {{YOUR_NAME}} is empty. Edit FIELD_VALUES before running.")
        return
    if not FIELD_VALUES["{{YOUR_CONTACT_INFO}}"]:
        print("ERROR: {{YOUR_CONTACT_INFO}} is empty. Edit FIELD_VALUES before running.")
        return
    if DISTRIBUTION_PATH == "A+37" and not FIELD_VALUES["{{DOMAIN_37_URL}}"]:
        print("WARNING: Path A+37 selected but {{DOMAIN_37_URL}} is empty.")
        print("  Create the Domain 37 Gist first, then fill this value.")
        print("  Continuing — Domain 37 URL will remain unfilled in output.")

    if DRY_RUN:
        print(f"DRY RUN — no files will be written. Distribution path: {DISTRIBUTION_PATH}\n")
    else:
        print(f"WRITING FILES to {OUTPUT_DIR}. Distribution path: {DISTRIBUTION_PATH}\n")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for filename in TARGET_FILES:
        source = PROJECT_ROOT / filename
        output = OUTPUT_DIR / filename

        if not source.exists():
            print(f"  SKIPPED (not found): {filename}")
            continue

        warnings = fill_file(source, output)
        status = "DRY RUN" if DRY_RUN else "WRITTEN"
        print(f"  [{status}] {filename}")
        all_warnings.extend(warnings)

    if all_warnings:
        print("\nWarnings:")
        for w in all_warnings:
            print(w)
    else:
        print("\nNo warnings. All fields filled.")

    if not DRY_RUN:
        print(f"\nOutput files in: {OUTPUT_DIR}")
        print("Review before sending. Originals in projects/resistance-research/ are unchanged.")

if __name__ == "__main__":
    main()
```

### 3.1 Script Usage Sequence

```bash
# Step 1: Edit the script — fill FIELD_VALUES dict
# Step 2: Dry run to preview
uv run python scripts/fill_templates.py   # DRY_RUN = True

# Step 3: Check warnings output. If none, set DRY_RUN = False
# Step 4: Write filled files to scripts/filled_output/
uv run python scripts/fill_templates.py   # DRY_RUN = False

# Step 5: Review scripts/filled_output/ before sending
# Step 6: Copy email body text from filled PHASE_1_EMAIL_TEMPLATES.md to email client
```

### 3.2 Safety Design Notes

- Script never overwrites source template files. Output goes to `scripts/filled_output/`.
- Empty `FIELD_VALUES` entries are skipped, not replaced with empty strings.
- The `check_unfilled_fields()` function explicitly catches the most likely errors:
  Domain 37 URL missing on Path A+37, and identity fields left blank.
- Path-specific block selection uses a non-greedy regex that matches the inline
  `[PATH A]` / `[PATH A+37]` / `[PATH B]` markers in the Batch 1 email templates.

---

## 4. Contact Verification Workflow

### 4.1 Batch 1 — Five Contacts (Verify Before Send)

Verification was completed in Session 658. The contacts and emails below are current
as of April 30, 2026. Verify again on the day of send if more than 7 days have elapsed.

| Contact | Institution | Verified Email | Verify At |
|---------|-------------|---------------|-----------|
| Ryan Goodman | Just Security / NYU Law | ryan@justsecurity.org | justsecurity.org/about |
| Wendy Weiser | Brennan Center | wweiser@brennancenter.org | brennancenter.org/experts/wendy-weiser |
| Erica Chenoweth | Harvard Kennedy School | echenoweth@harvard.edu | hks.harvard.edu/faculty |
| Ian Bassin | Protect Democracy | ian@protectdemocracy.org | protectdemocracy.org/about |
| Marc Elias | Democracy Docket | marc@democracydocket.com | democracydocket.com/about |

**Verification procedure** (2 minutes per contact):
1. Visit the institutional URL in the table above
2. Confirm the person is still in the listed role (title, organization)
3. Confirm the email format is still correct (if the institutional website lists a different format, use the newer one)
4. Note any April–May 2026 publications or litigation activity for the content placeholder

Full verification details and April 2026 topical hooks are in `BATCH_1_CONTACT_VERIFICATION.md`.

### 4.2 Which Contacts to Verify Before Send vs. After Path Decision

| Contact | Verify Before Send | Verify Now (pre-decision) |
|---------|-------------------|--------------------------|
| Batch 1 (5 contacts) | Yes — 2 min each | Session 658 verification is current; re-verify on send day if >7 days |
| Batch 2 (8 contacts) | Yes — 2 min each | No — verify on Days 8-12 when sending |
| Batch 3 (12 contacts) | Yes — 2 min each | No — verify on Days 15-21 when sending |
| Domain 37 election-protection tier (7 orgs) | Yes — 2 min each | Path A+37 only — verify at Phase B launch (Week 9) |

Do not pre-verify Batches 2 and 3 before path decision — the 2-3 week gap means any
pre-decision verification will be stale by send time.

### 4.3 Automation vs. Manual Entry — Decision Matrix

| Field Type | Method | Rationale |
|-----------|--------|-----------|
| URL fields (6 known Gists) | Script | No judgment required; same value in every file |
| Identity fields | Script (after human sets value once) | Same value in every file; reduces transcription errors |
| Content placeholders (recent publications) | Manual only | Requires current web research; cannot be safely cached |
| Path-specific block selection | Script | Deterministic based on path decision |
| Contact email addresses | Manual verification + script | Human confirms accuracy; script populates if using a contact management tool |
| Send timing / sequencing | Manual only | Human judgment on timing and spacing |

---

## 5. Timing Sequence: Automation vs. Manual

```
T+0:00  PATH DECISION MADE
        → Immediately run fill_templates.py (URL + identity fields)
        → Estimated time: 5 minutes (edit dict, dry run, write)

T+0:05  REVIEW FILLED OUTPUT
        → Open scripts/filled_output/PHASE_1_EMAIL_TEMPLATES.md
        → Confirm no {{PLACEHOLDER}} strings remain
        → Confirm path-specific blocks are correctly resolved
        → Estimated time: 5 minutes

T+0:10  CONTENT PLACEHOLDER FILL (manual, per-contact research)
        → Email 1 (Goodman): Visit justsecurity.org — fill {{RECENT_JUST_SECURITY_ARTICLE}}
        → Email 2 (Weiser): Visit brennancenter.org — fill {{RECENT_WEISER_PUBLICATION}}
        → Emails 3-5: Same pattern
        → Estimated time: 25-30 minutes for all five

T+0:40  PATH A+37 ONLY — DOMAIN 37 GIST CREATION
        → Create Domain 37 Gist (5 minutes, see gist-template-structure.md)
        → Update {{DOMAIN_37_URL}} in fill script
        → Re-run script for Phase 1b templates only
        → Estimated time: 10 minutes

T+0:50  CONTACT VERIFICATION
        → Visit each of the 5 institutional URLs, confirm role + email current
        → Estimated time: 10 minutes

T+1:00  COPY TO EMAIL CLIENT
        → Copy each email body from filled output to email client (Gmail, Outlook, etc.)
        → Set subject lines (choose one variant per contact)
        → Set send order: Goodman → Weiser → Chenoweth → Bassin → Elias
        → Estimated time: 10 minutes

T+1:10  BATCH 1 SEND BEGINS
        → Send Email 1 (Goodman)
        → Wait 30-45 minutes, send Email 2 (Weiser)
        → Continue staggered sequence
```

---

*Created May 6, 2026. Companion: `github-api-integration-guide.md` (API operations),*
*`distribution-checklist-template.md` (full 4-hour sequence).*
