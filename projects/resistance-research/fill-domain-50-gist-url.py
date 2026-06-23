#!/usr/bin/env python3
"""
Helper script to auto-fill Domain 50 Gist URL placeholders.

Usage:
  python fill-domain-50-gist-url.py "https://gist.github.com/esca8peArtist/..."

This script:
1. Takes the Domain 50 Gist URL as input
2. Finds all [INSERT GIST URL HERE] placeholders in resistance-research templates
3. Replaces them with the Gist URL
4. Commits the changes to master with a message
"""

import sys
import subprocess
import os
from pathlib import Path
from datetime import datetime


def fill_gist_urls(gist_url: str) -> None:
    """Fill all Domain 50 Gist URL placeholders and commit changes."""

    # Validate Gist URL format
    if not gist_url.startswith("https://gist.github.com/"):
        print("❌ ERROR: Invalid Gist URL. Must start with 'https://gist.github.com/'")
        sys.exit(1)

    # Get the resistance-research directory
    base_dir = Path(__file__).parent

    # Files to search and replace
    files_to_process = [
        base_dir / "SCOTUS_TRIGGER_5MIN_ACTION_GUIDE.md",
        base_dir / "SCOTUS_TRIGGER_1HOUR_ACTION_GUIDE.md",
        base_dir / "DOMAIN_50_EMAIL_TEMPLATE_SET.md",
        base_dir / "DOMAIN_50_GIST_PREP.md",
        base_dir / "DISTRIBUTION_GIST_URLS.md",
    ]

    # Also search for any other markdown files with placeholders
    all_md_files = list(base_dir.glob("*.md"))
    files_to_process = list(set(files_to_process + all_md_files))

    placeholder = "[INSERT GIST URL HERE]"
    changes_made = []

    print(f"\n🔍 Searching for placeholders in {len(files_to_process)} files...\n")

    for filepath in sorted(files_to_process):
        if not filepath.exists():
            continue

        with open(filepath, 'r') as f:
            content = f.read()

        if placeholder in content:
            count = content.count(placeholder)
            new_content = content.replace(placeholder, gist_url)

            with open(filepath, 'w') as f:
                f.write(new_content)

            changes_made.append((filepath.name, count))
            print(f"✅ {filepath.name}: {count} placeholder(s) replaced")

    if not changes_made:
        print("❌ No placeholders found. Domain 50 may already be filled.")
        sys.exit(1)

    # Add Gist URL to DISTRIBUTION_GIST_URLS.md if not present
    dist_file = base_dir / "DISTRIBUTION_GIST_URLS.md"
    with open(dist_file, 'a') as f:
        # Check if Domain 50 entry exists
        with open(dist_file, 'r') as rf:
            content = rf.read()

        if "Domain 50" not in content:
            creation_date = datetime.now().strftime("%Y-%m-%d")
            f.write(f"\n## Domain 50 — Anti-LGBTQ+ Ballot Initiative Voting Suppression\n")
            f.write(f"- Gist URL: {gist_url}\n")
            f.write(f"- Created: {creation_date}\n")
            f.write(f"- Status: Active — SCOTUS trigger active\n")
            print(f"✅ DISTRIBUTION_GIST_URLS.md: Domain 50 entry added")

    # Summary
    total_replaced = sum(count for _, count in changes_made)
    print(f"\n{'='*60}")
    print(f"📊 Total placeholders replaced: {total_replaced}")
    print(f"📁 Files modified: {len(changes_made)}")
    print(f"🔗 Gist URL: {gist_url}")
    print(f"{'='*60}\n")

    # Commit changes
    try:
        os.chdir(Path(__file__).parent.parent.parent)  # Go to repo root

        # Stage the modified files
        subprocess.run(["git", "add", "projects/resistance-research/"], check=True, capture_output=True)

        # Create commit message
        commit_msg = f"chore(resistance-research): Domain 50 Gist URL filled ({total_replaced} placeholders)\n\nGist URL: {gist_url}\nCreated: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}"

        # Commit
        subprocess.run(["git", "commit", "-m", commit_msg], check=True, capture_output=True)

        print("✅ Changes committed to master")
        print(f"\n🚀 Domain 50 is now ready for SCOTUS rapid-response execution!")
        print(f"   Execute: SCOTUS_TRIGGER_5MIN_ACTION_GUIDE.md (after decision at 14:00 UTC)")

    except subprocess.CalledProcessError as e:
        print(f"❌ Git commit failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fill-domain-50-gist-url.py <gist_url>")
        print("\nExample:")
        print("  python fill-domain-50-gist-url.py 'https://gist.github.com/esca8peArtist/abc123def456'")
        sys.exit(1)

    gist_url = sys.argv[1].strip()
    fill_gist_urls(gist_url)
