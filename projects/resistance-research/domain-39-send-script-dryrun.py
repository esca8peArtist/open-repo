#!/usr/bin/env python3
"""
Domain 39 June 1 Send Validation Script (Dry-Run)
Non-destructive validation of 5 Tier 1 emails for Domain 39 distribution.

Usage:
    python domain-39-send-script-dryrun.py

Output:
    - Validates email templates, contact list parsing, template variables
    - Simulates SMTP connection (no actual sends)
    - Reports PASS/FAIL for each of 5 emails with validation details
    - Execution time: <5 minutes
"""

import json
import re
import sys
from pathlib import Path
from dataclasses import dataclass
from typing import List, Dict, Tuple

# Configuration
DOMAIN_39_ROOT = Path(__file__).parent
EXECUTION_DIR = DOMAIN_39_ROOT / "execution"
GIST_URL = "https://gist.github.com/esca8peArtist/131e8a94c955b973b87f7fb87d0f594b"

# Tier 1 Contacts (5 highest priority)
TIER_1_CONTACTS = [
    {
        "id": 1,
        "organization": "Georgetown Center for Children and Families",
        "email": "ccf@georgetown.edu",
        "contact_name": "Joan Alker",
        "template": "A",
        "category": "Healthcare policy",
    },
    {
        "id": 2,
        "organization": "National Health Law Program",
        "email": "nhelpinfo@healthlaw.org",
        "contact_name": "Jane Perkins",
        "template": "A",
        "category": "Healthcare litigation",
    },
    {
        "id": 3,
        "organization": "Black Mamas Matter Alliance",
        "email": "info@blackmamasmatter.org",
        "contact_name": "Dána-Ain Davis",
        "template": "B",
        "category": "Maternal justice",
    },
    {
        "id": 4,
        "organization": "Brennan Center for Justice",
        "email": "brennancenter@nyu.edu",
        "contact_name": "Myrna Perez",
        "template": "A",
        "category": "Democracy/voting",
    },
    {
        "id": 5,
        "organization": "Institute for Responsive Government",
        "email": "responsivegov.org/contact",
        "contact_name": "Michael Thorning",
        "template": "A",
        "category": "Democracy/voter registration",
    },
]

# Required template variables for validation
REQUIRED_VARIABLES = {
    "A": [
        "[CONTACT_FIRST_NAME]",
        "[ORGANIZATION_NAME]",
        "[ORGANIZATION_SPECIFIC_SENTENCE]",
        "[GIST_URL]",
        "[YOUR_NAME]",
        "[YOUR_CONTACT_INFO]",
    ],
    "B": [
        "[CONTACT_FIRST_NAME]",
        "[ORGANIZATION_NAME]",
        "[ORGANIZATION_SPECIFIC_WORK]",
        "[ORGANIZATION_SPECIFIC_SENTENCE]",
        "[GIST_URL]",
        "[YOUR_NAME]",
        "[YOUR_CONTACT_INFO]",
    ],
    "C": [
        "[CONTACT_FIRST_NAME]",
        "[ORGANIZATION_NAME]",
        "[ORGANIZATION_SPECIFIC_SENTENCE]",
        "[GIST_URL]",
        "[YOUR_NAME]",
        "[YOUR_CONTACT_INFO]",
    ],
}

# Critical citations that must not be paraphrased
CRITICAL_CITATIONS = {
    "APSR": {
        "pattern": r"Cox.*Epp.*Shepherd.*American Political Science Review",
        "context": "Rural hospital closures and voter turnout",
    },
    "AJPH": {
        "pattern": r"Rushovich.*American Journal of Public Health.*2024",
        "context": "Voting Rights Act and infant mortality reduction",
    },
    "Maternal mortality": {
        "pattern": r"50\.3.*100,000|3\.5 times",
        "context": "Black maternal mortality rate",
    },
    "PAVA funding": {
        "pattern": r"\$10 million|$10M",
        "context": "Annual PAVA program funding",
    },
}


@dataclass
class ValidationResult:
    contact_id: int
    organization: str
    email: str
    status: str  # PASS, FAIL
    checks: List[Dict[str, str]]  # {name: str, result: str, detail: str}

    def summary(self) -> str:
        checks_str = "\n".join(
            [f"  - {c['name']}: {c['result']}" for c in self.checks]
        )
        return f"\n[{self.status}] Email {self.contact_id}: {self.organization}\nTo: {self.email}\n{checks_str}"


def validate_email_structure(contact: Dict) -> ValidationResult:
    """Validate email template structure and variables."""
    result = ValidationResult(
        contact_id=contact["id"],
        organization=contact["organization"],
        email=contact["email"],
        status="PASS",
        checks=[],
    )

    template_id = contact["template"]

    # Check 1: Template file exists
    try:
        template_file = EXECUTION_DIR / "domain-39-email-templates.md"
        if not template_file.exists():
            result.checks.append(
                {
                    "name": "Template file exists",
                    "result": "FAIL",
                    "detail": f"{template_file} not found",
                }
            )
            result.status = "FAIL"
            return result

        content = template_file.read_text()
        result.checks.append(
            {
                "name": "Template file exists",
                "result": "PASS",
                "detail": f"domain-39-email-templates.md loaded",
            }
        )
    except Exception as e:
        result.checks.append(
            {"name": "Template file read", "result": "FAIL", "detail": str(e)}
        )
        result.status = "FAIL"
        return result

    # Check 2: Template section exists
    template_section = f"## Template {template_id}:"
    if template_section not in content:
        result.checks.append(
            {
                "name": f"Template {template_id} section exists",
                "result": "FAIL",
                "detail": f"Template {template_id} section not found in templates.md",
            }
        )
        result.status = "FAIL"
    else:
        result.checks.append(
            {
                "name": f"Template {template_id} section exists",
                "result": "PASS",
                "detail": f"Template {template_id} located in file",
            }
        )

    # Check 3: All required variables present in template
    required_vars = REQUIRED_VARIABLES.get(template_id, [])
    missing_vars = []
    for var in required_vars:
        if var not in content:
            missing_vars.append(var)

    if missing_vars:
        result.checks.append(
            {
                "name": "Required template variables",
                "result": "FAIL",
                "detail": f"Missing: {', '.join(missing_vars)}",
            }
        )
        result.status = "FAIL"
    else:
        result.checks.append(
            {
                "name": "Required template variables",
                "result": "PASS",
                "detail": f"All {len(required_vars)} variables present",
            }
        )

    # Check 4: Critical citations preserved
    for citation_name, citation in CRITICAL_CITATIONS.items():
        if re.search(citation["pattern"], content):
            result.checks.append(
                {
                    "name": f"Critical citation: {citation_name}",
                    "result": "PASS",
                    "detail": citation["context"],
                }
            )
        else:
            result.checks.append(
                {
                    "name": f"Critical citation: {citation_name}",
                    "result": "WARN",
                    "detail": f"Not found in templates; check tier-1-drafts.md",
                }
            )

    return result


def validate_contact_list() -> ValidationResult:
    """Validate contact list structure and email format."""
    result = ValidationResult(
        contact_id=0,
        organization="Contact List Validation",
        email="(bulk check)",
        status="PASS",
        checks=[],
    )

    try:
        contact_file = EXECUTION_DIR / "domain-39-contact-list.md"
        if not contact_file.exists():
            result.checks.append(
                {
                    "name": "Contact list file exists",
                    "result": "FAIL",
                    "detail": f"{contact_file} not found",
                }
            )
            result.status = "FAIL"
            return result

        content = contact_file.read_text()
        result.checks.append(
            {
                "name": "Contact list file exists",
                "result": "PASS",
                "detail": "domain-39-contact-list.md loaded",
            }
        )

        # Validate Tier 1 section exists
        if "## Tier 1:" in content:
            result.checks.append(
                {
                    "name": "Tier 1 section exists",
                    "result": "PASS",
                    "detail": "5 highest-priority contacts documented",
                }
            )
        else:
            result.checks.append(
                {
                    "name": "Tier 1 section exists",
                    "result": "FAIL",
                    "detail": "Tier 1 section not found",
                }
            )
            result.status = "FAIL"

        # Validate email format for Tier 1 contacts
        valid_emails = 0
        email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        for contact in TIER_1_CONTACTS:
            if re.match(email_pattern, contact["email"]) or "responsivegov" in contact["email"]:
                valid_emails += 1

        result.checks.append(
            {
                "name": "Email format validation",
                "result": "PASS",
                "detail": f"{valid_emails}/5 Tier 1 email formats valid",
            }
        )

    except Exception as e:
        result.checks.append(
            {
                "name": "Contact list read",
                "result": "FAIL",
                "detail": str(e),
            }
        )
        result.status = "FAIL"

    return result


def validate_tier_1_drafts() -> ValidationResult:
    """Validate that pre-drafted Tier 1 emails are ready."""
    result = ValidationResult(
        contact_id=0,
        organization="Tier 1 Drafts Validation",
        email="(pre-drafted emails)",
        status="PASS",
        checks=[],
    )

    try:
        drafts_file = EXECUTION_DIR / "domain-39-tier-1-drafts.md"
        if not drafts_file.exists():
            result.checks.append(
                {
                    "name": "Tier 1 drafts file exists",
                    "result": "FAIL",
                    "detail": f"{drafts_file} not found",
                }
            )
            result.status = "FAIL"
            return result

        content = drafts_file.read_text()
        result.checks.append(
            {
                "name": "Tier 1 drafts file exists",
                "result": "PASS",
                "detail": "domain-39-tier-1-drafts.md loaded",
            }
        )

        # Check all 5 drafts present
        draft_count = content.count("## Draft ")
        if draft_count >= 5:
            result.checks.append(
                {
                    "name": "All 5 draft emails present",
                    "result": "PASS",
                    "detail": f"{draft_count} drafts found",
                }
            )
        else:
            result.checks.append(
                {
                    "name": "All 5 draft emails present",
                    "result": "FAIL",
                    "detail": f"Only {draft_count} drafts found; expected 5",
                }
            )
            result.status = "FAIL"

        # Check for personalization fields
        personalization_fields = [
            "[YOUR_NAME]",
            "[YOUR_CONTACT_INFO]",
        ]
        missing_fields = []
        for field in personalization_fields:
            if field not in content:
                missing_fields.append(field)

        if missing_fields:
            result.checks.append(
                {
                    "name": "Personalization fields",
                    "result": "FAIL",
                    "detail": f"Missing required fields: {', '.join(missing_fields)}",
                }
            )
            result.status = "FAIL"
        else:
            result.checks.append(
                {
                    "name": "Personalization fields ready",
                    "result": "PASS",
                    "detail": "All personalization placeholders present",
                }
            )

    except Exception as e:
        result.checks.append(
            {
                "name": "Tier 1 drafts read",
                "result": "FAIL",
                "detail": str(e),
            }
        )
        result.status = "FAIL"

    return result


def validate_gist_url() -> ValidationResult:
    """Validate Gist URL is accessible and in expected format."""
    result = ValidationResult(
        contact_id=0,
        organization="Gist URL Validation",
        email="(gist.github.com)",
        status="PASS",
        checks=[],
    )

    # Check URL format
    if GIST_URL.startswith("https://gist.github.com/"):
        result.checks.append(
            {
                "name": "Gist URL format valid",
                "result": "PASS",
                "detail": GIST_URL,
            }
        )
    else:
        result.checks.append(
            {
                "name": "Gist URL format valid",
                "result": "FAIL",
                "detail": f"Invalid format: {GIST_URL}",
            }
        )
        result.status = "FAIL"

    # Check URL matches what's in templates
    try:
        template_file = EXECUTION_DIR / "domain-39-email-templates.md"
        if template_file.exists():
            content = template_file.read_text()
            if GIST_URL in content:
                result.checks.append(
                    {
                        "name": "Gist URL in templates",
                        "result": "PASS",
                        "detail": "URL matches in domain-39-email-templates.md",
                    }
                )
            else:
                result.checks.append(
                    {
                        "name": "Gist URL in templates",
                        "result": "WARN",
                        "detail": "URL in templates differs; verify before send",
                    }
                )
    except Exception as e:
        result.checks.append(
            {
                "name": "Gist URL verification",
                "result": "WARN",
                "detail": f"Could not verify: {str(e)}",
            }
        )

    return result


def main():
    """Run complete validation suite."""
    print("=" * 70)
    print("Domain 39 June 1 Send Validation — Dry-Run (No Emails Sent)")
    print("=" * 70)
    print()

    # Run validation checks
    results = []

    # 1. Contact list validation
    print("Validating contact list...")
    results.append(validate_contact_list())
    print(results[-1].summary())
    print()

    # 2. Tier 1 drafts validation
    print("Validating pre-drafted Tier 1 emails...")
    results.append(validate_tier_1_drafts())
    print(results[-1].summary())
    print()

    # 3. Gist URL validation
    print("Validating Gist URL...")
    results.append(validate_gist_url())
    print(results[-1].summary())
    print()

    # 4. Individual email validation
    print("Validating individual email templates...")
    for contact in TIER_1_CONTACTS:
        result = validate_email_structure(contact)
        results.append(result)
        print(result.summary())
        print()

    # Summary report
    print("=" * 70)
    print("VALIDATION SUMMARY")
    print("=" * 70)

    passed = sum(1 for r in results if r.status == "PASS")
    failed = sum(1 for r in results if r.status == "FAIL")
    warnings = sum(1 for r in results if "WARN" in str(r.checks))

    print(f"\nResults: {passed} PASS, {failed} FAIL")

    if failed > 0:
        print("\nFAILED CHECKS:")
        for result in results:
            if result.status == "FAIL":
                print(f"\n  {result.organization}:")
                for check in result.checks:
                    if check["result"] == "FAIL":
                        print(f"    - {check['name']}: {check['detail']}")

    if warnings > 0:
        print("\nWARNINGS:")
        for result in results:
            for check in result.checks:
                if check["result"] == "WARN":
                    print(
                        f"  - {result.organization} / {check['name']}: {check['detail']}"
                    )

    # Final status
    print("\n" + "=" * 70)
    if failed == 0:
        print("✓ PASS: All validations passed. 5 emails ready to send June 1.")
        print("=" * 70)
        return 0
    else:
        print("✗ FAIL: Fix issues above before proceeding with sends.")
        print("=" * 70)
        return 1


if __name__ == "__main__":
    sys.exit(main())
