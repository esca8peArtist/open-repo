#!/usr/bin/env python3
"""
Automated A11y audit runner using axe-core.
Scans /docs and /redoc endpoints and generates findings documentation.
"""

import asyncio
import json
import csv
import sys
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any

from playwright.async_api import async_playwright, Page
import subprocess


class A11yAuditRunner:
    """Run automated accessibility audits using axe-core."""

    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self.results: Dict[str, Any] = {
            "timestamp": datetime.now().isoformat(),
            "base_url": base_url,
            "scans": {},
            "violations": [],
            "summary": {}
        }
        self.output_dir = Path(__file__).parent.parent / "a11y-audit-results"
        self.output_dir.mkdir(exist_ok=True)

    async def run_axe_scan(self, page: Page, url: str, page_name: str) -> Dict[str, Any]:
        """Run axe-core scan on a page."""
        print(f"\n[*] Scanning {page_name} ({url})...")

        try:
            response = await page.goto(url, wait_until="networkidle")
            if response.status != 200:
                print(f"  ERROR: Page returned status {response.status}")
                return {"page": page_name, "url": url, "status": "failed", "violations": []}

            # Inject axe-core using local/inline method
            print(f"  [*] Injecting axe-core library (local)...")

            # Try to inject from node_modules first
            try:
                axe_path = Path(__file__).parent.parent / "node_modules" / "axe-core" / "axe.min.js"
                if axe_path.exists():
                    with open(axe_path, "r") as f:
                        axe_script = f.read()
                    await page.evaluate(axe_script)
                else:
                    # Fallback: use inline eval
                    await page.evaluate("""
                        if (typeof window.axe === 'undefined') {
                            console.log('axe-core will be loaded via npx');
                        }
                    """)
            except Exception as e:
                print(f"  WARNING: Could not inject axe.min.js: {e}, will use npx CLI instead")

            # Run axe analysis
            print(f"  [*] Running axe analysis...")
            result = await page.evaluate("""
                async () => {
                    try {
                        if (typeof axe === 'undefined' || typeof axe.run !== 'function') {
                            return {
                                error: 'axe-core not available in page context, will use CLI',
                                violations: [],
                                passes: [],
                                incomplete: [],
                                inapplicable: []
                            };
                        }
                        const results = await axe.run({
                            rules: {
                                // Enable all rules
                            }
                        });
                        return {
                            violations: results.violations || [],
                            passes: results.passes || [],
                            incomplete: results.incomplete || [],
                            inapplicable: results.inapplicable || []
                        };
                    } catch (error) {
                        return {
                            error: error.message,
                            violations: [],
                            passes: [],
                            incomplete: [],
                            inapplicable: []
                        };
                    }
                }
            """)

            if "error" in result and "will use CLI" in result.get("error", ""):
                # Fall back to npx CLI
                return await self.run_axe_scan_cli(url, page_name)

            if "error" in result:
                print(f"  WARNING: {result['error']}, falling back to npx CLI")
                return await self.run_axe_scan_cli(url, page_name)

            violation_count = len(result.get("violations", []))
            print(f"  [✓] Found {violation_count} violations")
            print(f"  [✓] Found {len(result.get('passes', []))} passing checks")

            return {
                "page": page_name,
                "url": url,
                "status": "success",
                "violations": result.get("violations", []),
                "passes": result.get("passes", []),
                "incomplete": result.get("incomplete", []),
                "inapplicable": result.get("inapplicable", [])
            }

        except Exception as e:
            print(f"  ERROR: {e}, will try npx CLI")
            return await self.run_axe_scan_cli(url, page_name)

    async def run_axe_scan_cli(self, url: str, page_name: str) -> Dict[str, Any]:
        """Run axe-core scan using npx CLI."""
        print(f"  [*] Using npx axe CLI for scanning...")

        try:
            # Create temp JSON file for output
            temp_output = Path(f"/tmp/axe_scan_{page_name.replace(' ', '_')}.json")

            # Run npx axe
            cmd = [
                "npx",
                "axe",
                url,
                "--json",
                "--timeout=30000"
            ]

            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=60,
                cwd=str(Path(__file__).parent.parent)
            )

            if result.returncode != 0:
                print(f"  WARNING: npx axe returned {result.returncode}")
                print(f"  STDERR: {result.stderr[:200]}")
                return {"page": page_name, "url": url, "status": "failed", "violations": []}

            # Parse JSON output
            try:
                axe_result = json.loads(result.stdout)
                violations = axe_result.get("violations", [])
                passes = axe_result.get("passes", [])

                violation_count = len(violations)
                print(f"  [✓] Found {violation_count} violations")
                print(f"  [✓] Found {len(passes)} passing checks")

                return {
                    "page": page_name,
                    "url": url,
                    "status": "success",
                    "violations": violations,
                    "passes": passes,
                    "incomplete": axe_result.get("incomplete", []),
                    "inapplicable": axe_result.get("inapplicable", [])
                }
            except json.JSONDecodeError as e:
                print(f"  ERROR: Failed to parse axe output: {e}")
                print(f"  OUTPUT: {result.stdout[:500]}")
                return {"page": page_name, "url": url, "status": "failed", "violations": []}

        except subprocess.TimeoutExpired:
            print(f"  ERROR: Scan timeout")
            return {"page": page_name, "url": url, "status": "failed", "violations": []}
        except Exception as e:
            print(f"  ERROR: {e}")
            return {"page": page_name, "url": url, "status": "failed", "violations": []}

    async def scan_pages(self):
        """Scan both /docs and /redoc pages."""
        pages_to_scan = [
            ("Swagger UI (FastAPI /docs)", f"{self.base_url}/docs"),
            ("ReDoc (API documentation)", f"{self.base_url}/redoc"),
        ]

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)

            for page_name, url in pages_to_scan:
                page = await browser.new_page()
                try:
                    scan_result = await self.run_axe_scan(page, url, page_name)
                    self.results["scans"][page_name] = scan_result

                    # Collect all violations
                    for violation in scan_result.get("violations", []):
                        violation["page"] = page_name
                        violation["url"] = url
                        self.results["violations"].append(violation)

                finally:
                    await page.close()

            await browser.close()

    def generate_summary(self):
        """Generate summary statistics."""
        violations = self.results["violations"]

        # Group by severity/impact
        by_impact = {}
        by_wcag = {}

        for violation in violations:
            impact = violation.get("impact", "unknown")
            by_impact[impact] = by_impact.get(impact, 0) + 1

            # Extract WCAG criteria if available
            tags = violation.get("tags", [])
            for tag in tags:
                if tag.startswith("wcag"):
                    by_wcag[tag] = by_wcag.get(tag, 0) + 1

        self.results["summary"] = {
            "total_violations": len(violations),
            "by_impact": by_impact,
            "by_wcag": by_wcag,
            "scan_timestamp": self.results["timestamp"],
            "scans_completed": len([s for s in self.results["scans"].values() if s.get("status") == "success"])
        }

    def export_json(self, filename: str = "june1-automated-scan.json"):
        """Export raw results as JSON."""
        output_file = self.output_dir / filename
        with open(output_file, "w") as f:
            json.dump(self.results, f, indent=2)
        print(f"\n[✓] JSON export: {output_file}")
        return output_file

    def export_csv(self, filename: str = "june1-findings-summary.csv"):
        """Export findings as CSV."""
        output_file = self.output_dir / filename

        violations = self.results["violations"]

        with open(output_file, "w", newline="") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=[
                    "WCAG Level",
                    "Violation",
                    "Element",
                    "Severity",
                    "Remediation",
                    "Status",
                    "Page"
                ]
            )
            writer.writeheader()

            for violation in violations:
                # Determine WCAG level from tags
                wcag_level = "N/A"
                tags = violation.get("tags", [])
                for tag in tags:
                    if "wcag2" in tag or "wcag" in tag:
                        if "aaa" in tag.lower():
                            wcag_level = "AAA"
                        elif "aa" in tag.lower():
                            wcag_level = "AA"
                        elif "a" in tag.lower():
                            wcag_level = "A"

                # Get element info
                nodes = violation.get("nodes", [])
                if nodes:
                    element = nodes[0].get("target", ["unknown"])[0]
                else:
                    element = "N/A"

                # Map axe impact to severity
                impact_map = {
                    "critical": "critical",
                    "serious": "serious",
                    "moderate": "moderate",
                    "minor": "minor"
                }
                severity = impact_map.get(violation.get("impact", "unknown"), "unknown")

                writer.writerow({
                    "WCAG Level": wcag_level,
                    "Violation": f"{violation.get('id', 'N/A')}: {violation.get('description', 'N/A')}",
                    "Element": element,
                    "Severity": severity,
                    "Remediation": violation.get("help", "See axe-core documentation"),
                    "Status": "Open",
                    "Page": violation.get("page", "N/A")
                })

        print(f"[✓] CSV export: {output_file}")
        return output_file

    def generate_findings_report(self, filename: str = "JUNE1_FINDINGS_REPORT.md"):
        """Generate human-readable findings report."""
        output_file = self.output_dir / filename
        violations = self.results["violations"]

        # Group by page and impact
        by_page = {}
        for violation in violations:
            page = violation.get("page", "Unknown")
            if page not in by_page:
                by_page[page] = []
            by_page[page].append(violation)

        # Sort each page's violations by impact
        impact_order = {"critical": 0, "serious": 1, "moderate": 2, "minor": 3}
        for page in by_page:
            by_page[page].sort(
                key=lambda v: impact_order.get(v.get("impact", "unknown"), 999)
            )

        # Build report
        lines = [
            "# Accessibility Audit Findings Report",
            "## June 1, 2026 - Automated Scanning Phase",
            "",
            f"**Audit Timestamp**: {self.results['timestamp']}",
            f"**Base URL**: {self.base_url}",
            "",
            "## Executive Summary",
            "",
            f"- **Total Violations Found**: {len(violations)}",
        ]

        # Add impact summary
        summary = self.results["summary"]
        by_impact = summary.get("by_impact", {})
        if by_impact:
            lines.append("- **Violations by Severity**:")
            for impact in ["critical", "serious", "moderate", "minor"]:
                count = by_impact.get(impact, 0)
                if count > 0:
                    lines.append(f"  - {impact.capitalize()}: {count}")

        lines.extend([
            "",
            "## Findings by Page",
            ""
        ])

        # Add findings by page
        for page, page_violations in by_page.items():
            lines.extend([
                f"### {page}",
                f"**Total violations**: {len(page_violations)}",
                ""
            ])

            # Group by impact for this page
            by_impact_page = {}
            for violation in page_violations:
                impact = violation.get("impact", "unknown")
                if impact not in by_impact_page:
                    by_impact_page[impact] = []
                by_impact_page[impact].append(violation)

            # Add violations grouped by impact
            for impact in ["critical", "serious", "moderate", "minor"]:
                if impact in by_impact_page:
                    violations_for_impact = by_impact_page[impact]
                    lines.extend([
                        f"#### {impact.upper()} Violations ({len(violations_for_impact)})",
                        ""
                    ])

                    for i, violation in enumerate(violations_for_impact, 1):
                        lines.extend([
                            f"**{i}. {violation.get('id', 'N/A')}**",
                            f"- **Description**: {violation.get('description', 'N/A')}",
                            f"- **Impact**: {violation.get('impact', 'N/A')}",
                            f"- **Help**: {violation.get('help', 'N/A')}",
                        ])

                        # Add WCAG criteria from tags
                        tags = violation.get("tags", [])
                        wcag_tags = [t for t in tags if "wcag" in t.lower()]
                        if wcag_tags:
                            lines.append(f"- **WCAG Criteria**: {', '.join(wcag_tags)}")

                        # Add affected elements
                        nodes = violation.get("nodes", [])
                        if nodes:
                            lines.append(f"- **Affected Elements**: {len(nodes)}")
                            for node in nodes[:3]:  # Show first 3
                                target = node.get("target", ["unknown"])
                                lines.append(f"  - {target[0]}")
                            if len(nodes) > 3:
                                lines.append(f"  - ... and {len(nodes) - 3} more")

                        lines.extend([
                            f"- **Recommended Fix**: {violation.get('helpUrl', 'See documentation')}",
                            ""
                        ])

        lines.extend([
            "## Pass/Fail Metrics by WCAG Criterion",
            ""
        ])

        # Add WCAG metrics
        by_wcag = summary.get("by_wcag", {})
        if by_wcag:
            for criterion in sorted(by_wcag.keys()):
                lines.append(f"- {criterion.upper()}: {by_wcag[criterion]} violations")
        else:
            lines.append("- No specific WCAG criteria identified")

        lines.extend([
            "",
            "## Next Steps",
            "",
            "1. **Triage violations** by severity (P0/P1/P2/P3)",
            "2. **Prioritize critical issues** for immediate remediation",
            "3. **Create remediation tasks** for each violation",
            "4. **Plan manual testing** phase (June 2-3)",
            "5. **Document known limitations** and third-party library behaviors",
        ])

        with open(output_file, "w") as f:
            f.write("\n".join(lines))

        print(f"[✓] Findings report: {output_file}")
        return output_file

    def create_triage_checklist(self, filename: str = "TRIAGE_CHECKLIST.md"):
        """Create triage checklist for violations."""
        output_file = self.output_dir / filename
        violations = self.results["violations"]

        # Group by impact
        critical = [v for v in violations if v.get("impact") == "critical"]
        serious = [v for v in violations if v.get("impact") == "serious"]
        moderate = [v for v in violations if v.get("impact") == "moderate"]
        minor = [v for v in violations if v.get("impact") == "minor"]

        lines = [
            "# A11y Triage Checklist",
            "## June 1, 2026 - Automated Scan Results",
            "",
            "## P0 - Critical Issues (Must Fix Before Deployment)",
            f"**Count**: {len(critical)} violations",
            "",
        ]

        for violation in critical:
            rule_id = violation.get("id", "unknown")
            description = violation.get("description", "N/A")
            lines.append(f"- [ ] **{rule_id}**: {description}")

        lines.extend([
            "",
            "## P1 - Serious Issues (Should Fix Before Deployment)",
            f"**Count**: {len(serious)} violations",
            ""
        ])

        for violation in serious:
            rule_id = violation.get("id", "unknown")
            description = violation.get("description", "N/A")
            lines.append(f"- [ ] **{rule_id}**: {description}")

        lines.extend([
            "",
            "## P2 - Moderate Issues (Can Fix Post-Deployment)",
            f"**Count**: {len(moderate)} violations",
            ""
        ])

        for violation in moderate:
            rule_id = violation.get("id", "unknown")
            description = violation.get("description", "N/A")
            lines.append(f"- [ ] **{rule_id}**: {description}")

        lines.extend([
            "",
            "## P3 - Minor Issues (Future Enhancements)",
            f"**Count**: {len(minor)} violations",
            ""
        ])

        for violation in minor:
            rule_id = violation.get("id", "unknown")
            description = violation.get("description", "N/A")
            lines.append(f"- [ ] **{rule_id}**: {description}")

        lines.extend([
            "",
            "## Known Limitations & Third-Party Behaviors",
            "",
            "- FastAPI Swagger UI (/docs): Third-party library, axe-core may flag CDN-delivered components",
            "- ReDoc (/redoc): Third-party library, limited control over generated HTML",
            "- Dynamic content: Items loaded post-initial-render not scanned (static analysis only)",
            "",
            "## Triage Status",
            "",
            f"- Scanned: {self.results['summary'].get('scans_completed', 0)} pages",
            f"- Total violations: {len(violations)}",
            f"- Critical: {len(critical)}",
            f"- Serious: {len(serious)}",
            f"- Moderate: {len(moderate)}",
            f"- Minor: {len(minor)}",
        ])

        with open(output_file, "w") as f:
            f.write("\n".join(lines))

        print(f"[✓] Triage checklist: {output_file}")
        return output_file


async def main():
    """Main execution."""
    print("\n" + "="*60)
    print("A11y Automated Audit Runner")
    print("="*60)

    # Create runner
    runner = A11yAuditRunner(base_url="http://localhost:8000")

    # Run scans
    print("\n[*] Starting automated accessibility scanning...")
    await runner.scan_pages()

    # Generate summary
    print("\n[*] Generating summary...")
    runner.generate_summary()

    # Export results
    print("\n[*] Exporting results...")
    runner.export_json()
    runner.export_csv()
    runner.generate_findings_report()
    runner.create_triage_checklist()

    # Print summary
    summary = runner.results["summary"]
    print("\n" + "="*60)
    print("SCAN COMPLETE")
    print("="*60)
    print(f"Total violations found: {summary['total_violations']}")
    print(f"Scans completed: {summary['scans_completed']}")
    print(f"Output directory: {runner.output_dir}")
    print("\nFiles generated:")
    print(f"  - june1-automated-scan.json")
    print(f"  - june1-findings-summary.csv")
    print(f"  - JUNE1_FINDINGS_REPORT.md")
    print(f"  - TRIAGE_CHECKLIST.md")
    print("="*60 + "\n")


if __name__ == "__main__":
    asyncio.run(main())
