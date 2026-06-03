"""Deep accessibility audit using locally-injected axe-core.

Injects axe-core from local node_modules to avoid CDN dependencies.
Scans all accessible pages/endpoints and produces structured violation output.

Run: TEST_BASE_URL=http://127.0.0.1:8000 uv run pytest tests/test_a11y_deep_scan.py -v -s
"""

import pytest
import json
from pathlib import Path
from datetime import datetime

pytestmark = pytest.mark.accessibility

# Local axe-core bundle (installed in projects/open-repo/node_modules)
# Path: tests/ -> backend/ -> open-repo/ -> node_modules/
AXE_CORE_PATH = Path(__file__).parent.parent.parent / "node_modules/axe-core/axe.min.js"
REPORTS_DIR = Path(__file__).parent.parent / "reports"
BASE_URL = "http://127.0.0.1:8000"

# WCAG 2.1 AA tags to check
AXE_TAGS = ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa", "best-practice"]

# Pages to scan (page_name, url)
PAGES_TO_SCAN = [
    ("swagger_ui", f"{BASE_URL}/docs"),
    ("redoc", f"{BASE_URL}/redoc"),
]


def get_axe_script():
    """Load the axe-core script content."""
    if AXE_CORE_PATH.exists():
        return AXE_CORE_PATH.read_text()
    pytest.skip(f"axe-core not found at {AXE_CORE_PATH}")


def run_axe_scan(page, url: str, tags: list[str] = None) -> dict:
    """Load a page and run axe-core scan, returning results."""
    axe_script = get_axe_script()
    tags = tags or AXE_TAGS

    # Navigate to page
    response = page.goto(url, wait_until="networkidle", timeout=30000)
    assert response is not None, f"No response from {url}"

    # Wait for JS a11y fixes to execute (SwaggerUI renders asynchronously;
    # our nested-interactive fix uses setTimeout(4000) as final fallback).
    page.wait_for_timeout(5000)

    # Inject axe-core
    page.evaluate(axe_script)

    # Run axe analysis
    results = page.evaluate(f"""
        async () => {{
            return await axe.run(document, {{
                runOnly: {{
                    type: 'tag',
                    values: {json.dumps(tags)}
                }},
                reporter: 'v2'
            }});
        }}
    """)

    return results


def save_scan_results(page_name: str, results: dict) -> Path:
    """Save scan results to JSON file."""
    REPORTS_DIR.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = REPORTS_DIR / f"deep_scan_{page_name}_{timestamp}.json"
    with open(report_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    return report_path


def format_violation(v: dict) -> str:
    """Format a single violation for readable output."""
    elements = [n.get("target", ["(unknown)"])[0] if n.get("target") else "(unknown)"
                for n in v.get("nodes", [])[:3]]
    return (
        f"\n  [{v['impact'].upper()}] {v['id']}: {v['description']}\n"
        f"    WCAG: {', '.join(v.get('tags', []))}\n"
        f"    Elements ({len(v.get('nodes', []))} total): {', '.join(elements)}\n"
        f"    Help: {v.get('helpUrl', '')}"
    )


@pytest.mark.parametrize("page_name,url", PAGES_TO_SCAN)
def test_axe_deep_scan(page, page_name, url):
    """Run full axe-core scan on the given page.

    This test passes unless there are CRITICAL violations.
    All violations (including serious/moderate) are reported.
    """
    results = run_axe_scan(page, url)
    report_path = save_scan_results(page_name, results)

    violations = results.get("violations", [])
    passes = results.get("passes", [])
    incomplete = results.get("incomplete", [])

    print(f"\n{'='*60}")
    print(f"Page: {page_name} ({url})")
    print(f"{'='*60}")
    print(f"Violations:  {len(violations)}")
    print(f"Passes:      {len(passes)}")
    print(f"Incomplete:  {len(incomplete)} (needs manual review)")
    print(f"Report:      {report_path}")

    if violations:
        print(f"\nVIOLATIONS FOUND ({len(violations)}):")
        for v in violations:
            print(format_violation(v))

    if incomplete:
        print(f"\nINCOMPLETE CHECKS (require manual verification):")
        for item in incomplete[:5]:
            print(f"  - {item.get('id')}: {item.get('description')}")
        if len(incomplete) > 5:
            print(f"  ... and {len(incomplete)-5} more")

    # Only fail hard on critical violations (P0 blockers)
    critical = [v for v in violations if v.get("impact") == "critical"]
    if critical:
        ids = [v["id"] for v in critical]
        pytest.fail(f"CRITICAL (P0) violations found: {ids}")

    # Report serious as warnings (P1)
    serious = [v for v in violations if v.get("impact") == "serious"]
    if serious:
        ids = [v["id"] for v in serious]
        print(f"\nWARNING: Serious (P1) violations require fix before deployment: {ids}")


def test_axe_deep_scan_violations_consolidated(page):
    """Consolidated scan across all pages — builds structured findings table.

    Does not fail the test suite but prints a complete findings matrix.
    """
    all_findings = []
    scan_summary = []

    for page_name, url in PAGES_TO_SCAN:
        results = run_axe_scan(page, url)
        violations = results.get("violations", [])
        passes = results.get("passes", [])
        incomplete = results.get("incomplete", [])

        scan_summary.append({
            "page": page_name,
            "url": url,
            "violations": len(violations),
            "passes": len(passes),
            "incomplete": len(incomplete),
            "critical": sum(1 for v in violations if v.get("impact") == "critical"),
            "serious": sum(1 for v in violations if v.get("impact") == "serious"),
            "moderate": sum(1 for v in violations if v.get("impact") == "moderate"),
            "minor": sum(1 for v in violations if v.get("impact") == "minor"),
        })

        for v in violations:
            nodes = v.get("nodes", [])
            elements = [n.get("target", ["(unknown)"])[0] if n.get("target") else "(unknown)"
                        for n in nodes[:5]]
            all_findings.append({
                "page": page_name,
                "url": url,
                "rule_id": v["id"],
                "impact": v.get("impact", "unknown"),
                "description": v.get("description", ""),
                "help_url": v.get("helpUrl", ""),
                "wcag_tags": [t for t in v.get("tags", []) if t.startswith("wcag")],
                "affected_count": len(nodes),
                "elements": elements,
            })

    # Print consolidated findings table
    print(f"\n{'='*70}")
    print("CONSOLIDATED A11Y AUDIT FINDINGS — Phase 5 Wave 2")
    print(f"{'='*70}")
    print(f"Scan date: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}")
    print(f"\nSCAN SUMMARY:")
    for s in scan_summary:
        total = s['critical'] + s['serious'] + s['moderate'] + s['minor']
        print(f"  {s['page']:20} — {total} violations "
              f"(C:{s['critical']} S:{s['serious']} M:{s['moderate']} m:{s['minor']}) "
              f"| {s['passes']} passes | {s['incomplete']} incomplete")

    total_violations = sum(s['violations'] for s in scan_summary)
    total_critical = sum(s['critical'] for s in scan_summary)
    total_serious = sum(s['serious'] for s in scan_summary)

    print(f"\n  TOTAL: {total_violations} violations | "
          f"P0(critical)={total_critical} P1(serious)={total_serious}")

    if all_findings:
        print(f"\nFINDINGS DETAIL:")
        for f in all_findings:
            severity = f['impact'].upper()
            wcag = ', '.join(f['wcag_tags']) or 'best-practice'
            elements = '; '.join(f['elements'])
            print(f"\n  [{severity}] {f['rule_id']} ({wcag})")
            print(f"    Page: {f['page']} | Affected: {f['affected_count']} element(s)")
            print(f"    Description: {f['description']}")
            print(f"    Elements: {elements}")
            print(f"    Fix: {f['help_url']}")
    else:
        print("\n  NO VIOLATIONS FOUND — All pages pass automated WCAG 2.1 AA checks!")

    # Save consolidated report
    REPORTS_DIR.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    consolidated_report = {
        "audit_date": datetime.now().isoformat(),
        "audit_phase": "Phase 5 Wave 2 — Deep Scan",
        "scanner": "axe-core 4.11.x (locally injected)",
        "tags": AXE_TAGS,
        "scan_summary": scan_summary,
        "findings": all_findings,
        "totals": {
            "violations": total_violations,
            "critical": total_critical,
            "serious": total_serious,
        }
    }
    report_path = REPORTS_DIR / f"deep_scan_consolidated_{timestamp}.json"
    with open(report_path, "w") as f:
        json.dump(consolidated_report, f, indent=2, default=str)
    print(f"\nConsolidated report saved: {report_path}")

    # Only fail on critical
    assert total_critical == 0, (
        f"DEPLOYMENT BLOCKER: {total_critical} critical (P0) violations found. "
        f"Fix before June 12 deployment."
    )
