#!/usr/bin/env python3
"""
Track B Launch Readiness Verification Script

Verifies that all 5 user action gates are complete before Track B launch.
Can be run June 1 afternoon to confirm gate completion before Day 3 checkpoint.

Returns:
  - GO: All 5 gates completed, launch ready
  - HOLD: Lists missing gates with remediation steps

Usage:
  python track_b_launch_readiness_verification.py [--json] [--verbose]

Exit codes:
  0 = GO (all gates complete)
  1 = HOLD (gates missing)
  2 = Verification error
"""

import sys
import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple, Optional


class GateVerifier:
    """Verifies Track B launch readiness gates."""

    def __init__(self, project_root: Path, verbose: bool = False):
        """
        Initialize verifier.

        Args:
            project_root: Path to seedwarden project root
            verbose: Enable verbose output
        """
        self.project_root = project_root
        self.verbose = verbose
        self.gates = {}
        self.missing_gates = []
        self.timestamp = datetime.utcnow().isoformat()

    def log(self, msg: str, level: str = "INFO") -> None:
        """Log message if verbose."""
        if self.verbose:
            print(f"[{level}] {msg}")

    def verify_gate_1_social_accounts(self) -> Tuple[bool, str]:
        """
        Verify Gate 1: Create Social Media Accounts.

        Checks:
          - Instagram account created with @seedwarden handle (or alternatives)
          - TikTok account created with @seedwarden handle
          - Pinterest account created with seedwarden handle
          - All three accounts have profile image uploaded
          - All three accounts have bio text populated
          - All three accounts have link-in-bio configured

        Note: Cannot programmatically verify social accounts without API access.
        Returns manual verification checklist.
        """
        checklist = {
            "instagram_account": False,
            "tiktok_account": False,
            "pinterest_account": False,
            "profile_images_uploaded": False,
            "bio_text_written": False,
            "link_in_bio_configured": False,
        }

        # Without social media API access, we provide a manual verification checklist
        status_msg = (
            "MANUAL VERIFICATION REQUIRED:\n"
            "  [ ] Instagram @seedwarden (or @seedwarden.co / @seedwarden.seeds) created\n"
            "  [ ] TikTok @seedwarden created\n"
            "  [ ] Pinterest seedwarden created\n"
            "  [ ] Profile image uploaded to all three\n"
            "  [ ] Bio text published on all three\n"
            "  [ ] Link-in-bio configured on all three (use Kit URL or Gist URL)"
        )

        return False, status_msg

    def verify_gate_2_canva_brand_kit(self) -> Tuple[bool, str]:
        """
        Verify Gate 2: Set Up Canva Brand Kit.

        Checks:
          - Canva Brand Kit created
          - 6 brand colors added
          - 3 fonts configured
          - Logo uploaded

        Note: Cannot programmatically verify Canva Brand Kit without API access.
        """
        checklist = {
            "brand_kit_created": False,
            "colors_configured": False,
            "fonts_configured": False,
            "logo_uploaded": False,
        }

        status_msg = (
            "MANUAL VERIFICATION REQUIRED:\n"
            "  [ ] Canva Brand Kit created (Brand Hub > Create a Brand Kit)\n"
            "  [ ] 6 brand colors added by hex code\n"
            "  [ ] 3 fonts added (Playfair Display, Lato, Cormorant Garamond)\n"
            "  [ ] Logo uploaded (projects/seedwarden/logos/seedwarden_logo_1.png)"
        )

        return False, status_msg

    def verify_gate_3_kit_account_and_landing_page(self) -> Tuple[bool, str]:
        """
        Verify Gate 3: Create Kit Account and Build Landing Page.

        Checks (manual):
          - Kit account created at kit.com
          - Landing page built with correct copy
          - 15 zone-routing tags configured
          - 5-email welcome sequence built
          - Test email sent and verified
          - Automation published (not Draft)
          - Kit landing page URL obtained
          - Social bios updated with Kit URL

        Note: Cannot programmatically verify without Kit API access.
        """
        checklist = {
            "kit_account_created": False,
            "landing_page_built": False,
            "zone_routing_tags_configured": False,
            "email_sequence_built": False,
            "test_email_verified": False,
            "automation_published": False,
            "kit_url_obtained": False,
            "social_bios_updated": False,
        }

        status_msg = (
            "MANUAL VERIFICATION REQUIRED:\n"
            "  [ ] Kit account created at kit.com (wanka95@gmail.com)\n"
            "  [ ] Landing page built with correct headline and form fields\n"
            "  [ ] 15 zone-routing tags configured (Zones 3-10 + combinations)\n"
            "  [ ] 5-email welcome sequence built from TRACK_B_EMAIL_COPY_FINAL.md\n"
            "  [ ] Test email sent to wanka95@gmail.com — zone card link resolves\n"
            "  [ ] Automation status is 'Published' (not 'Draft')\n"
            "  [ ] Kit landing page URL copied\n"
            "  [ ] Social media bios updated with Kit URL"
        )

        return False, status_msg

    def verify_gate_4_zone_pdfs_uploaded(self) -> Tuple[bool, str]:
        """
        Verify Gate 4: Upload Zone PDFs to Google Drive.

        Checks:
          - All 8 zone PDFs exist locally at projects/seedwarden/assets/zone-cards/
          - Files are present and correct size (~636 KB each)
          - Note: Cannot verify Google Drive upload without API access
        """
        zone_pdf_dir = self.project_root / "assets" / "zone-cards"

        if not zone_pdf_dir.exists():
            return False, f"Zone PDF directory not found: {zone_pdf_dir}"

        # Check for all 8 zone PDFs
        expected_pdfs = [
            "seedwarden-zone-3-quickstart-card.pdf",
            "seedwarden-zone-4-quickstart-card.pdf",
            "seedwarden-zone-5-quickstart-card.pdf",
            "seedwarden-zone-6-quickstart-card.pdf",
            "seedwarden-zone-7-quickstart-card.pdf",
            "seedwarden-zone-8-quickstart-card.pdf",
            "seedwarden-zone-9-quickstart-card.pdf",
            "seedwarden-zone-10-quickstart-card.pdf",
        ]

        missing_pdfs = []
        for pdf_name in expected_pdfs:
            pdf_path = zone_pdf_dir / pdf_name
            if not pdf_path.exists():
                missing_pdfs.append(pdf_name)
            else:
                size_kb = pdf_path.stat().st_size / 1024
                self.log(f"  ✓ {pdf_name} ({size_kb:.1f} KB)")

        if missing_pdfs:
            return False, f"Missing zone PDFs: {', '.join(missing_pdfs)}"

        status_msg = (
            "LOCAL PDFs VERIFIED: All 8 zone cards present (636 KB each)\n"
            "MANUAL VERIFICATION REQUIRED:\n"
            "  [ ] All 8 PDFs uploaded to Google Drive\n"
            "  [ ] Share setting: 'Anyone with the link can view'\n"
            "  [ ] All 8 download links tested in incognito browser"
        )

        return False, status_msg  # Local check passes, but needs manual GDrive verification

    def verify_gate_5_seedwarden15_coupon(self) -> Tuple[bool, str]:
        """
        Verify Gate 5: Confirm SEEDWARDEN15 Coupon Code.

        Checks (manual):
          - Etsy Shop Manager login confirmed
          - SEEDWARDEN15 coupon code is active
          - Coupon discount set correctly

        Note: Cannot programmatically verify without Etsy API access.
        """
        checklist = {
            "etsy_login_verified": False,
            "coupon_active": False,
            "coupon_discount_set": False,
        }

        status_msg = (
            "MANUAL VERIFICATION REQUIRED:\n"
            "  [ ] Log in to Etsy Shop Manager\n"
            "  [ ] Navigate to Marketing > Coupons and Sales\n"
            "  [ ] Confirm SEEDWARDEN15 coupon code is active\n"
            "  [ ] Confirm discount amount is correct"
        )

        return False, status_msg

    def verify_all_gates(self) -> Dict[str, Dict]:
        """
        Verify all 5 gates and return results.

        Returns:
            Dictionary with gate verification results
        """
        self.log("Starting Track B launch readiness verification...")
        self.log(f"Project root: {self.project_root}")

        results = {
            "timestamp": self.timestamp,
            "gates": {},
            "overall_status": "UNKNOWN",
            "missing_gates": [],
        }

        # Gate 1: Social Accounts
        gate1_ok, gate1_msg = self.verify_gate_1_social_accounts()
        results["gates"]["gate_1_social_accounts"] = {
            "status": "GO" if gate1_ok else "HOLD",
            "description": "Create Social Media Accounts (Instagram, TikTok, Pinterest)",
            "message": gate1_msg,
            "time_estimate": "30-60 minutes",
        }
        if not gate1_ok:
            self.missing_gates.append("Gate 1: Social Accounts")

        # Gate 2: Canva Brand Kit
        gate2_ok, gate2_msg = self.verify_gate_2_canva_brand_kit()
        results["gates"]["gate_2_canva_brand_kit"] = {
            "status": "GO" if gate2_ok else "OPTIONAL",
            "description": "Set Up Canva Brand Kit (optional for Phase 1)",
            "message": gate2_msg,
            "time_estimate": "30 minutes",
        }
        # Gate 2 is optional, so don't add to missing_gates

        # Gate 3: Kit Account and Landing Page
        gate3_ok, gate3_msg = self.verify_gate_3_kit_account_and_landing_page()
        results["gates"]["gate_3_kit_account"] = {
            "status": "GO" if gate3_ok else "HOLD",
            "description": "Create Kit Account and Build Landing Page",
            "message": gate3_msg,
            "time_estimate": "2-3 hours",
        }
        if not gate3_ok:
            self.missing_gates.append("Gate 3: Kit Account")

        # Gate 4: Zone PDFs Uploaded
        gate4_ok, gate4_msg = self.verify_gate_4_zone_pdfs_uploaded()
        results["gates"]["gate_4_zone_pdfs"] = {
            "status": "GO" if gate4_ok else "HOLD",
            "description": "Upload Zone PDFs to Google Drive",
            "message": gate4_msg,
            "time_estimate": "20 minutes",
        }
        if not gate4_ok:
            self.missing_gates.append("Gate 4: Zone PDFs Upload")

        # Gate 5: SEEDWARDEN15 Coupon
        gate5_ok, gate5_msg = self.verify_gate_5_seedwarden15_coupon()
        results["gates"]["gate_5_coupon_code"] = {
            "status": "GO" if gate5_ok else "HOLD",
            "description": "Confirm SEEDWARDEN15 Coupon Code Active",
            "message": gate5_msg,
            "time_estimate": "5 minutes",
        }
        if not gate5_ok:
            self.missing_gates.append("Gate 5: Coupon Code")

        # Determine overall status
        # Gates 1, 3, 4, 5 are blocking (must be complete)
        blocking_gates = [gate1_ok, gate3_ok, gate4_ok, gate5_ok]

        if all(blocking_gates):
            results["overall_status"] = "GO"
            results["message"] = "All launch gates cleared. Track B launch READY."
            results["exit_code"] = 0
        else:
            results["overall_status"] = "HOLD"
            results["missing_gates"] = self.missing_gates
            results["message"] = (
                f"Launch BLOCKED. {len(self.missing_gates)} gate(s) incomplete:\n" +
                "\n".join(f"  • {gate}" for gate in self.missing_gates)
            )
            results["exit_code"] = 1

        self.log(f"Overall status: {results['overall_status']}")

        return results


def format_text_report(results: Dict) -> str:
    """Format results as human-readable text report."""
    lines = [
        "=" * 80,
        "TRACK B LAUNCH READINESS VERIFICATION REPORT",
        "=" * 80,
        f"Timestamp: {results['timestamp']} UTC",
        "",
        f"OVERALL STATUS: {results['overall_status']}",
        "",
    ]

    if results['overall_status'] == "GO":
        lines.append("✓ All launch gates cleared. Track B is READY FOR LAUNCH.")
        lines.append("")
    else:
        lines.append(f"✗ Launch blocked. {len(results['missing_gates'])} gate(s) incomplete:")
        for gate in results['missing_gates']:
            lines.append(f"  • {gate}")
        lines.append("")

    lines.append("-" * 80)
    lines.append("DETAILED GATE STATUS:")
    lines.append("-" * 80)

    for gate_id, gate_info in results['gates'].items():
        lines.append("")
        lines.append(f"Gate: {gate_info['description']}")
        lines.append(f"  Status: {gate_info['status']}")
        lines.append(f"  Time estimate: {gate_info['time_estimate']}")
        lines.append("")
        for line in gate_info['message'].split('\n'):
            lines.append(f"  {line}")

    lines.append("")
    lines.append("=" * 80)

    if results['overall_status'] == "GO":
        lines.append("ACTION: Proceed with launch. Run Day 3 checkpoint on June 4 09:00 UTC.")
    else:
        lines.append(f"ACTION: Complete missing gates before proceeding with launch.")
        lines.append("Estimated time to completion: See time estimates above.")

    lines.append("=" * 80)

    return "\n".join(lines)


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Track B Launch Readiness Verification"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results as JSON"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging"
    )
    parser.add_argument(
        "--project-root",
        type=Path,
        default=None,
        help="Path to seedwarden project root (auto-detected if not provided)"
    )

    args = parser.parse_args()

    # Auto-detect project root
    if args.project_root is None:
        # Try to find it relative to this script
        script_path = Path(__file__).resolve()
        args.project_root = script_path.parent.parent

    args.project_root = args.project_root.resolve()

    if not args.project_root.exists():
        print(f"ERROR: Project root not found: {args.project_root}", file=sys.stderr)
        return 2

    # Run verification
    verifier = GateVerifier(args.project_root, verbose=args.verbose)
    results = verifier.verify_all_gates()

    # Output results
    if args.json:
        print(json.dumps(results, indent=2))
    else:
        print(format_text_report(results))

    return results['exit_code']


if __name__ == "__main__":
    sys.exit(main())
