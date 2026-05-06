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

Source spec: projects/resistance-research/field-fill-automation-spec.md Section 3
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
            problems.append(
                f"  WARNING in {filename}: Domain 37 URL placeholder still present "
                f"— create Gist first (see distribution-gist-template.md Section F)"
            )
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
        print("  Create the Domain 37 Gist first (distribution-gist-template.md Section F),")
        print("  then paste the URL into FIELD_VALUES above and re-run.")
        print("  Continuing — Domain 37 URL will remain unfilled in output.\n")

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
