"""
Tests for Phase 1 execution infrastructure — Democratic Renewal Proposal

Coverage areas:
1. Email template rendering and structural completeness (15 tests)
2. Batch sequencing logic and contact validation (8 tests)
3. Decision-path-specific logic and content gates (7 tests)
4. Success metrics thresholds and gate logic (5 tests)

All tests are self-contained and do not require external network calls.
"""

import re
import os
import pytest
from pathlib import Path

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

EXEC_DIR = Path(__file__).parent
RESEARCH_DIR = EXEC_DIR.parent


def read_file(filename: str) -> str:
    """Read a file from the execution directory."""
    path = EXEC_DIR / filename
    assert path.exists(), f"Expected file not found: {path}"
    return path.read_text(encoding="utf-8")


def read_research_file(filename: str) -> str:
    """Read a file from the parent resistance-research directory."""
    path = RESEARCH_DIR / filename
    assert path.exists(), f"Expected research file not found: {path}"
    return path.read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# EMAIL TEMPLATE TESTS (15 tests)
# ---------------------------------------------------------------------------

class TestEmailTemplates:
    """Validate structure, content completeness, and variant presence."""

    @pytest.fixture(scope="class")
    def template_text(self):
        return read_file("outreach-email-templates.md")

    def test_three_template_types_present(self, template_text):
        """Templates A, B, C must all be present."""
        assert "TEMPLATE TYPE A" in template_text, "Template A (Academic/Think Tank) missing"
        assert "TEMPLATE TYPE B" in template_text, "Template B (Media/Journalist) missing"
        assert "TEMPLATE TYPE C" in template_text, "Template C (Legal/Institutional) missing"

    def test_three_variants_per_type(self, template_text):
        """Each template type must have Variant 1, 2, and 3."""
        for template in ["A", "B", "C"]:
            for variant in [1, 2, 3]:
                pattern = f"Template {template}-{variant}"
                assert pattern in template_text, f"Missing: {pattern}"

    def test_subject_lines_per_variant(self, template_text):
        """Each variant must contain at least one subject line option."""
        # Count "Subject A:" occurrences — should be at least 3 (one per template type)
        subject_a_count = template_text.count("Subject A:")
        assert subject_a_count >= 3, f"Expected at least 3 'Subject A:' blocks, found {subject_a_count}"

    def test_template_a_academic_framing(self, template_text):
        """Template A must include the 'peer-level scholarly' framing language."""
        a_section_start = template_text.find("TEMPLATE TYPE A")
        b_section_start = template_text.find("TEMPLATE TYPE B")
        a_section = template_text[a_section_start:b_section_start]
        assert "scholarly" in a_section.lower() or "academic" in a_section.lower(), \
            "Template A must include academic/scholarly framing"

    def test_template_b_media_specificity(self, template_text):
        """Template B must include 'newsworthiness' or specific finding language."""
        b_section_start = template_text.find("TEMPLATE TYPE B")
        c_section_start = template_text.find("TEMPLATE TYPE C")
        b_section = template_text[b_section_start:c_section_start]
        assert "newsworthy" in b_section.lower() or "specific finding" in b_section.lower(), \
            "Template B must include newsworthiness or specific finding language"

    def test_template_c_legal_framing(self, template_text):
        """Template C must include litigation or institutional reform language."""
        c_section_start = template_text.find("TEMPLATE TYPE C")
        c_section = template_text[c_section_start:]
        assert "litigation" in c_section.lower() or "institutional reform" in c_section.lower(), \
            "Template C must include litigation or institutional reform language"

    def test_hook_examples_present(self, template_text):
        """Template file must include hook examples referencing domains."""
        assert "Domain 28" in template_text or "Domain 29" in template_text, \
            "Templates must include domain-specific hook examples"

    def test_cta_variants_present(self, template_text):
        """Call-to-action options must be present in each template section."""
        # Check for at least two distinct CTA forms across the document
        cta_signals = ["feedback", "call", "Zoom", "send you", "colleague"]
        found = [s for s in cta_signals if s.lower() in template_text.lower()]
        assert len(found) >= 3, f"Expected at least 3 CTA variants, found signals: {found}"

    def test_cc_license_noted(self, template_text):
        """Creative Commons 4.0 license must be referenced in templates."""
        assert "Creative Commons" in template_text or "CC 4.0" in template_text, \
            "Templates must reference the CC 4.0 license"

    def test_response_handling_section(self, template_text):
        """File must include guidance on handling early responses."""
        assert "HANDLING RESPONSES" in template_text or "handling responses" in template_text.lower(), \
            "Must include response handling section"

    def test_positive_response_guidance(self, template_text):
        """Must include guidance for positive early response (72-hour window)."""
        assert "72 hours" in template_text or "24 hours" in template_text, \
            "Must include time-specific guidance for positive responses"

    def test_executive_summary_mention(self, template_text):
        """Templates must reference the executive summary as a CTA option."""
        assert "executive summary" in template_text.lower(), \
            "Templates must include executive summary as an option"

    def test_objection_handling_present(self, template_text):
        """Template file must address at least one objection scenario."""
        assert "credentials" in template_text.lower() or "objection" in template_text.lower(), \
            "Must address credentials or objection scenario"

    def test_subject_line_ab_test_framework(self, template_text):
        """A/B test framework for subject lines must be documented."""
        assert "A/B" in template_text or "a/b test" in template_text.lower(), \
            "Must include A/B testing framework for subject lines"

    def test_personalization_checklist(self, template_text):
        """Pre-send personalization checklist must be present."""
        assert "checklist" in template_text.lower() or "[ ]" in template_text, \
            "Must include a pre-send checklist"


# ---------------------------------------------------------------------------
# BATCH SEQUENCING TESTS (8 tests)
# ---------------------------------------------------------------------------

class TestBatchSequencing:
    """Validate batch structure, timing, contact counts, and sequencing logic."""

    @pytest.fixture(scope="class")
    def batch_text(self):
        return read_file("tier-1-contact-batches.md")

    def test_three_batches_defined(self, batch_text):
        """File must define Batch 1, Batch 2, and Batch 3."""
        assert "BATCH 1" in batch_text, "Batch 1 not defined"
        assert "BATCH 2" in batch_text, "Batch 2 not defined"
        assert "BATCH 3" in batch_text, "Batch 3 not defined"

    def test_batch_1_has_five_contacts(self, batch_text):
        """Batch 1 must specify 5 contacts (counted from section header lines only)."""
        batch1_start = batch_text.find("BATCH 1")
        batch2_start = batch_text.find("BATCH 2")
        batch1_section = batch_text[batch1_start:batch2_start]
        # Count only section header lines "### Contact B1-N:" to avoid inline references
        b1_headers = re.findall(r"###\s+Contact\s+B1-\d+", batch1_section)
        assert len(b1_headers) == 5, \
            f"Expected 5 Batch 1 contact headers (### Contact B1-1 ... B1-5), found: {b1_headers}"

    def test_batch_1_includes_goodman(self, batch_text):
        """Ryan Goodman must appear in Batch 1."""
        batch1_start = batch_text.find("BATCH 1")
        batch2_start = batch_text.find("BATCH 2")
        batch1_section = batch_text[batch1_start:batch2_start]
        assert "Goodman" in batch1_section, "Ryan Goodman must be in Batch 1"

    def test_batch_1_includes_chenoweth(self, batch_text):
        """Erica Chenoweth must appear in Batch 1."""
        batch1_start = batch_text.find("BATCH 1")
        batch2_start = batch_text.find("BATCH 2")
        batch1_section = batch_text[batch1_start:batch2_start]
        assert "Chenoweth" in batch1_section, "Erica Chenoweth must be in Batch 1"

    def test_batch_1_includes_weiser(self, batch_text):
        """Wendy Weiser must appear in Batch 1."""
        batch1_start = batch_text.find("BATCH 1")
        batch2_start = batch_text.find("BATCH 2")
        batch1_section = batch_text[batch1_start:batch2_start]
        assert "Weiser" in batch1_section, "Wendy Weiser must be in Batch 1"

    def test_batch_2_has_eight_to_ten_contacts(self, batch_text):
        """Batch 2 must specify 8-10 contacts."""
        batch2_start = batch_text.find("BATCH 2")
        batch3_start = batch_text.find("BATCH 3")
        batch2_section = batch_text[batch2_start:batch3_start]
        b2_contacts = re.findall(r"B2-\d+", batch2_section)
        assert 8 <= len(b2_contacts) <= 10, \
            f"Expected 8-10 Batch 2 contacts, found {len(b2_contacts)}: {b2_contacts}"

    def test_success_metrics_in_batch_file(self, batch_text):
        """Batch file must include success metrics with specific targets."""
        assert "SUCCESS METRICS" in batch_text or "response rate" in batch_text.lower(), \
            "Batch file must include success metrics"
        # Verify 30% target is specified
        assert "30%" in batch_text, "Must specify 30% response rate target"

    def test_contact_log_template_present(self, batch_text):
        """Contact log template must be present."""
        assert "CONTACT LOG" in batch_text or "contact log" in batch_text.lower(), \
            "Must include contact log template"
        assert "Date sent" in batch_text or "date sent" in batch_text.lower(), \
            "Contact log must include date tracking field"


# ---------------------------------------------------------------------------
# DECISION PATH TESTS (7 tests)
# ---------------------------------------------------------------------------

class TestDecisionPaths:
    """Validate that each path file contains required content and differentiation."""

    @pytest.fixture(scope="class")
    def path_a(self):
        return read_file("path-a-materials.md")

    @pytest.fixture(scope="class")
    def path_a_d37(self):
        return read_file("path-a-domain37-materials.md")

    @pytest.fixture(scope="class")
    def path_b(self):
        return read_file("path-b-materials.md")

    def test_path_a_emphasizes_completeness(self, path_a):
        """Path A must use 'comprehensive' or 'complete' framing."""
        assert "comprehensive" in path_a.lower() or "complete" in path_a.lower(), \
            "Path A must emphasize comprehensive/complete diagnostic framing"

    def test_path_a_d37_includes_domain_37_integration(self, path_a_d37):
        """Path A+Domain37 must explicitly address Domain 37 integration."""
        assert "Domain 37" in path_a_d37, "Path A+Domain37 must mention Domain 37"
        assert "integration" in path_a_d37.lower() or "integrate" in path_a_d37.lower(), \
            "Path A+Domain37 must address the integration step"

    def test_path_a_d37_references_advocacy_windows(self, path_a_d37):
        """Path A+Domain37 must reference Domain 37's advocacy windows."""
        assert "advocacy window" in path_a_d37.lower() or "May 30" in path_a_d37, \
            "Path A+Domain37 must reference the five advocacy windows"

    def test_path_b_emphasizes_rolling_release(self, path_b):
        """Path B must use 'rolling' or 'serial' or 'ongoing' framing."""
        assert "rolling" in path_b.lower() or "serial" in path_b.lower() or "ongoing" in path_b.lower(), \
            "Path B must emphasize rolling/serial release framing"

    def test_all_paths_include_media_outlets(self, path_a, path_a_d37, path_b):
        """Each path document must name at least one target media outlet."""
        # Expanded list includes outlets that appear in Path A+Domain37 specifically
        outlets = [
            "Just Security", "Vox", "Washington Monthly", "Atlantic", "Lawfare",
            "ProPublica", "NPR", "Substack", "Democracy Docket", "New York Times",
            "stateline", "Route Fifty",
        ]
        for name, content in [("Path A", path_a), ("Path A+D37", path_a_d37), ("Path B", path_b)]:
            found = any(outlet in content for outlet in outlets)
            assert found, f"{name}: Must name at least one target media outlet from: {outlets}"

    def test_all_paths_include_timeline(self, path_a, path_a_d37, path_b):
        """Each path document must include a timeline section."""
        for name, content in [("Path A", path_a), ("Path A+D37", path_a_d37), ("Path B", path_b)]:
            has_timeline = "timeline" in content.lower() or "T-Day" in content or "T+Week" in content
            assert has_timeline, f"{name}: Must include a timeline"

    def test_paths_are_distinguishable(self, path_a, path_a_d37, path_b):
        """The three path documents must have meaningfully different primary framing."""
        # Path A should mention "comprehensive diagnostic" more than Path B
        path_a_comprehensive = path_a.lower().count("comprehensive")
        path_b_rolling = path_b.lower().count("rolling")
        path_d37_integration = path_a_d37.lower().count("domain 37")
        assert path_a_comprehensive >= 1, "Path A must use 'comprehensive' framing"
        assert path_b_rolling >= 1, "Path B must use 'rolling' framing"
        assert path_d37_integration >= 5, "Path A+D37 must repeatedly reference Domain 37"


# ---------------------------------------------------------------------------
# SUCCESS METRICS TESTS (5 tests)
# ---------------------------------------------------------------------------

class TestSuccessMetrics:
    """Validate thresholds, checkpoint structure, and feedback loop logic."""

    @pytest.fixture(scope="class")
    def metrics_text(self):
        return read_file("success-metrics.md")

    def test_30_day_checkpoint_present(self, metrics_text):
        """30-day checkpoint must be explicitly defined."""
        assert "30-day" in metrics_text.lower() or "30 day" in metrics_text.lower() or \
               "DAY 28" in metrics_text or "T+30" in metrics_text, \
            "Must include explicit 30-day checkpoint"

    def test_90_day_checkpoint_present(self, metrics_text):
        """90-day checkpoint must be explicitly defined."""
        assert "90-day" in metrics_text.lower() or "90 day" in metrics_text.lower() or \
               "T+90" in metrics_text, \
            "Must include explicit 90-day checkpoint"

    def test_three_metric_tiers(self, metrics_text):
        """Must define engagement, adoption, and influence metrics."""
        assert "ENGAGEMENT" in metrics_text.upper(), "Must define engagement metrics tier"
        assert "ADOPTION" in metrics_text.upper(), "Must define adoption metrics tier"
        assert "INFLUENCE" in metrics_text.upper(), "Must define influence metrics tier"

    def test_forwarding_rate_threshold(self, metrics_text):
        """Must specify a forwarding rate target."""
        assert "forward" in metrics_text.lower(), "Must include forwarding rate metric"
        # Should reference the 10%+ forwarding target from the task specification
        assert "10%" in metrics_text or "12%" in metrics_text, \
            "Must specify a numeric forwarding rate target"

    def test_diagnostic_protocol_for_underperformance(self, metrics_text):
        """Must include a diagnostic protocol for when metrics underperform."""
        assert "diagnostic" in metrics_text.lower() or "below" in metrics_text.lower(), \
            "Must include diagnostic protocol for underperforming metrics"
        # Verify specific diagnostic steps are present
        assert "Step 1" in metrics_text or "step 1" in metrics_text.lower(), \
            "Diagnostic protocol must include numbered steps"


# ---------------------------------------------------------------------------
# CROSS-DOCUMENT CONSISTENCY TESTS (3 bonus tests)
# ---------------------------------------------------------------------------

class TestCrossDocumentConsistency:
    """Verify that companion documents are consistently cross-referenced."""

    @pytest.fixture(scope="class")
    def all_exec_texts(self):
        files = [
            "tier-1-contact-batches.md",
            "outreach-email-templates.md",
            "distribution-sequence.md",
            "path-a-materials.md",
            "path-a-domain37-materials.md",
            "path-b-materials.md",
            "success-metrics.md",
            "frequently-asked-questions.md",
            "objection-responses.md",
        ]
        return {f: read_file(f) for f in files}

    def test_all_seven_deliverable_files_exist(self, all_exec_texts):
        """All seven required deliverable files must exist."""
        required = [
            "tier-1-contact-batches.md",
            "outreach-email-templates.md",
            "distribution-sequence.md",
            "path-a-materials.md",
            "path-a-domain37-materials.md",
            "path-b-materials.md",
            "success-metrics.md",
            "frequently-asked-questions.md",
            "objection-responses.md",
        ]
        for f in required:
            assert f in all_exec_texts, f"Required deliverable missing: {f}"

    def test_distribution_sequence_references_batch_file(self, all_exec_texts):
        """Distribution sequence must reference the tier-1-contact-batches file."""
        dist_seq = all_exec_texts["distribution-sequence.md"]
        assert "tier-1-contact-batches" in dist_seq, \
            "distribution-sequence.md must cross-reference tier-1-contact-batches.md"

    def test_faq_cross_references_objection_doc(self, all_exec_texts):
        """FAQ must cross-reference the objection responses document."""
        faq = all_exec_texts["frequently-asked-questions.md"]
        assert "objection-responses" in faq, \
            "frequently-asked-questions.md must cross-reference objection-responses.md"


# ---------------------------------------------------------------------------
# Run instructions
# ---------------------------------------------------------------------------
#
# From the resistance-research/execution/ directory:
#   uv run pytest test_execution_infrastructure.py -v
#
# From the repo root:
#   uv run pytest projects/resistance-research/execution/test_execution_infrastructure.py -v
#
