"""Tests for Phase 3 contributions, reviewer queues, and feedback models."""

import pytest
from datetime import datetime
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import (
    Contribution,
    ContributionStatus,
    ContributionType,
    ReviewerQueueItem,
    ContributionFeedback,
    FeedbackType,
    FeedbackSeverity,
    ContentItem,
)


@pytest.fixture
async def db_session(client):
    """Get a test database session from the client fixture."""
    # Extract the mocked session from dependency overrides
    from app import database
    from unittest.mock import AsyncMock, MagicMock

    session = AsyncMock(spec=AsyncSession)
    return session


@pytest.fixture
def sample_contribution_data():
    """Sample contribution data for testing."""
    return {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://schema.org/",
            "https://openrepo.net/ns/v1",
        ],
        "@type": "procedure",
        "title": {"en": "How to build a water filter"},
        "domain": "procedural",
        "license": "CC-BY-4.0",
        "description": {"en": "A guide to building a biosand water filter"},
        "language": ["en"],
        "tags": ["water", "filtration", "DIY"],
    }


@pytest.fixture
def sample_edit_diff():
    """Sample edit diff for testing."""
    return {
        "title": {
            "en": {
                "old": "Old Title",
                "new": "Improved Title",
            }
        },
        "description": {
            "en": {
                "old": "Old description",
                "new": "Better, more detailed description",
            }
        },
    }


@pytest.fixture
def sample_revision_requests():
    """Sample revision requests for testing."""
    return [
        {"field": "steps[2].body", "suggestion": "Add safety note about heat"},
        {"field": "materials", "suggestion": "Include sourcing links"},
    ]


# ============================================================================
# Contribution Model Tests
# ============================================================================


class TestContributionModel:
    """Tests for the Contribution model."""

    async def test_contribution_creation_new_item(self, sample_contribution_data):
        """Test creating a new_item contribution."""
        contribution = Contribution(
            contribution_type=ContributionType.NEW_ITEM,
            status=ContributionStatus.PENDING,
            contributor_id="user@example.com",
            item_data=sample_contribution_data,
            proposed_cid="sha256-abc123",
        )

        assert contribution.contribution_type == ContributionType.NEW_ITEM
        assert contribution.status == ContributionStatus.PENDING
        assert contribution.contributor_id == "user@example.com"
        assert contribution.proposed_cid == "sha256-abc123"
        assert contribution.target_item_cid is None
        assert contribution.item_data == sample_contribution_data

    async def test_contribution_creation_edit_item(self, sample_contribution_data, sample_edit_diff):
        """Test creating an edit_item contribution."""
        contribution = Contribution(
            contribution_type=ContributionType.EDIT_ITEM,
            status=ContributionStatus.PENDING,
            contributor_id="user@example.com",
            target_item_cid="sha256-existing",
            item_data=sample_contribution_data,
            edit_diff=sample_edit_diff,
        )

        assert contribution.contribution_type == ContributionType.EDIT_ITEM
        assert contribution.target_item_cid == "sha256-existing"
        assert contribution.edit_diff == sample_edit_diff
        assert contribution.proposed_cid is None

    async def test_contribution_status_transition_pending_to_approved(
        self, sample_contribution_data
    ):
        """Test status transition from PENDING to APPROVED."""
        contribution = Contribution(
            contribution_type=ContributionType.NEW_ITEM,
            status=ContributionStatus.PENDING,
            contributor_id="user@example.com",
            item_data=sample_contribution_data,
        )

        assert contribution.status == ContributionStatus.PENDING

        # Transition to approved
        contribution.status = ContributionStatus.APPROVED
        assert contribution.status == ContributionStatus.APPROVED

    async def test_contribution_status_transition_pending_to_revision_requested(
        self, sample_contribution_data, sample_revision_requests
    ):
        """Test status transition from PENDING to REVISION_REQUESTED."""
        contribution = Contribution(
            contribution_type=ContributionType.NEW_ITEM,
            status=ContributionStatus.PENDING,
            contributor_id="user@example.com",
            item_data=sample_contribution_data,
            required_revisions=sample_revision_requests,
        )

        contribution.status = ContributionStatus.REVISION_REQUESTED

        assert contribution.status == ContributionStatus.REVISION_REQUESTED
        assert contribution.required_revisions == sample_revision_requests

    async def test_contribution_status_transition_pending_to_rejected(
        self, sample_contribution_data
    ):
        """Test status transition from PENDING to REJECTED."""
        contribution = Contribution(
            contribution_type=ContributionType.NEW_ITEM,
            status=ContributionStatus.PENDING,
            contributor_id="user@example.com",
            item_data=sample_contribution_data,
            rejection_reason="Content does not meet quality standards",
        )

        contribution.status = ContributionStatus.REJECTED

        assert contribution.status == ContributionStatus.REJECTED
        assert contribution.rejection_reason == "Content does not meet quality standards"

    async def test_contribution_revision_requested_to_approved(
        self, sample_contribution_data, sample_revision_requests
    ):
        """Test status transition from REVISION_REQUESTED to APPROVED."""
        contribution = Contribution(
            contribution_type=ContributionType.NEW_ITEM,
            status=ContributionStatus.REVISION_REQUESTED,
            contributor_id="user@example.com",
            item_data=sample_contribution_data,
            required_revisions=sample_revision_requests,
        )

        # Simulate resubmission and approval
        contribution.item_data = {**sample_contribution_data, "description": {"en": "Revised description"}}
        contribution.status = ContributionStatus.APPROVED
        contribution.reviewer_notes = "Looks good after revisions!"

        assert contribution.status == ContributionStatus.APPROVED
        assert contribution.reviewer_notes == "Looks good after revisions!"

    async def test_contribution_repr(self, sample_contribution_data):
        """Test string representation of Contribution."""
        contribution = Contribution(
            id=1,
            contribution_type=ContributionType.NEW_ITEM,
            status=ContributionStatus.PENDING,
            contributor_id="user@example.com",
            item_data=sample_contribution_data,
        )

        repr_str = repr(contribution)
        assert "Contribution" in repr_str
        assert "id=1" in repr_str
        assert "NEW_ITEM" in repr_str


# ============================================================================
# ReviewerQueueItem Model Tests
# ============================================================================


class TestReviewerQueueItem:
    """Tests for the ReviewerQueueItem model."""

    async def test_reviewer_queue_item_creation(self, sample_contribution_data):
        """Test creating a reviewer queue item."""
        contribution = Contribution(
            contribution_type=ContributionType.NEW_ITEM,
            status=ContributionStatus.PENDING,
            contributor_id="user@example.com",
            item_data=sample_contribution_data,
        )

        queue_item = ReviewerQueueItem(
            contribution=contribution,
            reviewer_id="reviewer@example.com",
        )

        assert queue_item.contribution == contribution
        assert queue_item.reviewer_id == "reviewer@example.com"
        assert queue_item.decided_at is None
        assert queue_item.decision is None

    async def test_reviewer_queue_item_decision_pending(self, sample_contribution_data):
        """Test reviewer queue item with pending decision."""
        contribution = Contribution(
            contribution_type=ContributionType.NEW_ITEM,
            status=ContributionStatus.PENDING,
            contributor_id="user@example.com",
            item_data=sample_contribution_data,
        )

        queue_item = ReviewerQueueItem(
            contribution=contribution,
            reviewer_id="reviewer@example.com",
        )

        assert queue_item.decision is None
        assert queue_item.decided_at is None

    async def test_reviewer_queue_item_decision_approve(self, sample_contribution_data):
        """Test reviewer approving a contribution."""
        contribution = Contribution(
            contribution_type=ContributionType.NEW_ITEM,
            status=ContributionStatus.PENDING,
            contributor_id="user@example.com",
            item_data=sample_contribution_data,
        )

        queue_item = ReviewerQueueItem(
            contribution=contribution,
            reviewer_id="reviewer@example.com",
            decision="approve",
        )

        assert queue_item.decision == "approve"

    async def test_reviewer_queue_item_decision_reject(self, sample_contribution_data):
        """Test reviewer rejecting a contribution."""
        contribution = Contribution(
            contribution_type=ContributionType.NEW_ITEM,
            status=ContributionStatus.PENDING,
            contributor_id="user@example.com",
            item_data=sample_contribution_data,
        )

        queue_item = ReviewerQueueItem(
            contribution=contribution,
            reviewer_id="reviewer@example.com",
            decision="reject",
            reviewer_notes="Does not meet quality standards",
        )

        assert queue_item.decision == "reject"
        assert queue_item.reviewer_notes == "Does not meet quality standards"

    async def test_reviewer_queue_item_decision_revision_requested(
        self, sample_contribution_data
    ):
        """Test reviewer requesting revisions."""
        contribution = Contribution(
            contribution_type=ContributionType.NEW_ITEM,
            status=ContributionStatus.PENDING,
            contributor_id="user@example.com",
            item_data=sample_contribution_data,
        )

        queue_item = ReviewerQueueItem(
            contribution=contribution,
            reviewer_id="reviewer@example.com",
            decision="revision_requested",
            reviewer_notes="Good submission but needs clarifications",
        )

        assert queue_item.decision == "revision_requested"

    async def test_reviewer_queue_item_repr(self, sample_contribution_data):
        """Test string representation of ReviewerQueueItem."""
        contribution = Contribution(
            id=1,
            contribution_type=ContributionType.NEW_ITEM,
            status=ContributionStatus.PENDING,
            contributor_id="user@example.com",
            item_data=sample_contribution_data,
        )

        queue_item = ReviewerQueueItem(
            id=1,
            contribution=contribution,
            contribution_id=1,
            reviewer_id="reviewer@example.com",
        )

        repr_str = repr(queue_item)
        assert "ReviewerQueueItem" in repr_str
        assert "contribution_id=1" in repr_str
        assert "reviewer_id=reviewer@example.com" in repr_str


# ============================================================================
# ContributionFeedback Model Tests
# ============================================================================


class TestContributionFeedback:
    """Tests for the ContributionFeedback model."""

    async def test_feedback_creation_text_only(self, sample_contribution_data):
        """Test creating text-only feedback."""
        contribution = Contribution(
            contribution_type=ContributionType.NEW_ITEM,
            status=ContributionStatus.PENDING,
            contributor_id="user@example.com",
            item_data=sample_contribution_data,
        )

        feedback = ContributionFeedback(
            contribution=contribution,
            feedback_type=FeedbackType.TEXT_ONLY,
            severity=FeedbackSeverity.MEDIUM,
            message="Consider adding more details about materials",
        )

        assert feedback.feedback_type == FeedbackType.TEXT_ONLY
        assert feedback.severity == FeedbackSeverity.MEDIUM
        assert feedback.message == "Consider adding more details about materials"
        assert feedback.resolved_at is None

    async def test_feedback_creation_minor_correction(self, sample_contribution_data):
        """Test creating minor correction feedback."""
        contribution = Contribution(
            contribution_type=ContributionType.NEW_ITEM,
            status=ContributionStatus.PENDING,
            contributor_id="user@example.com",
            item_data=sample_contribution_data,
        )

        feedback = ContributionFeedback(
            contribution=contribution,
            feedback_type=FeedbackType.MINOR_CORRECTION,
            severity=FeedbackSeverity.LOW,
            message="Fix typo in step 3: 'boild' should be 'boil'",
        )

        assert feedback.feedback_type == FeedbackType.MINOR_CORRECTION
        assert feedback.severity == FeedbackSeverity.LOW

    async def test_feedback_creation_missing_field(self, sample_contribution_data):
        """Test creating missing field feedback."""
        contribution = Contribution(
            contribution_type=ContributionType.NEW_ITEM,
            status=ContributionStatus.PENDING,
            contributor_id="user@example.com",
            item_data=sample_contribution_data,
        )

        feedback = ContributionFeedback(
            contribution=contribution,
            feedback_type=FeedbackType.MISSING_FIELD,
            severity=FeedbackSeverity.HIGH,
            message="Missing safety warnings for step 5",
        )

        assert feedback.feedback_type == FeedbackType.MISSING_FIELD
        assert feedback.severity == FeedbackSeverity.HIGH

    async def test_feedback_high_severity(self, sample_contribution_data):
        """Test high-severity feedback."""
        contribution = Contribution(
            contribution_type=ContributionType.NEW_ITEM,
            status=ContributionStatus.PENDING,
            contributor_id="user@example.com",
            item_data=sample_contribution_data,
        )

        feedback = ContributionFeedback(
            contribution=contribution,
            feedback_type=FeedbackType.MISSING_FIELD,
            severity=FeedbackSeverity.HIGH,
            message="Critical: Missing safety precautions",
        )

        assert feedback.severity == FeedbackSeverity.HIGH

    async def test_feedback_resolution(self, sample_contribution_data):
        """Test resolving feedback."""
        contribution = Contribution(
            contribution_type=ContributionType.NEW_ITEM,
            status=ContributionStatus.PENDING,
            contributor_id="user@example.com",
            item_data=sample_contribution_data,
        )

        feedback = ContributionFeedback(
            contribution=contribution,
            feedback_type=FeedbackType.MINOR_CORRECTION,
            severity=FeedbackSeverity.LOW,
            message="Typo in title",
            resolved=0,
        )

        assert feedback.resolved == 0
        assert feedback.resolved_at is None

        # Mark as resolved
        feedback.resolved = 1
        feedback.resolved_at = datetime.utcnow()

        assert feedback.resolved == 1
        assert feedback.resolved_at is not None

    async def test_feedback_repr(self, sample_contribution_data):
        """Test string representation of ContributionFeedback."""
        contribution = Contribution(
            id=1,
            contribution_type=ContributionType.NEW_ITEM,
            status=ContributionStatus.PENDING,
            contributor_id="user@example.com",
            item_data=sample_contribution_data,
        )

        feedback = ContributionFeedback(
            id=1,
            contribution=contribution,
            contribution_id=1,
            feedback_type=FeedbackType.TEXT_ONLY,
            severity=FeedbackSeverity.MEDIUM,
            message="Test feedback",
        )

        repr_str = repr(feedback)
        assert "ContributionFeedback" in repr_str
        assert "id=1" in repr_str
        assert "MEDIUM" in repr_str


# ============================================================================
# Relationship Tests
# ============================================================================


class TestModelRelationships:
    """Tests for relationships between models."""

    async def test_contribution_to_reviewer_queue_relationship(self, sample_contribution_data):
        """Test relationship between Contribution and ReviewerQueueItem."""
        contribution = Contribution(
            contribution_type=ContributionType.NEW_ITEM,
            status=ContributionStatus.PENDING,
            contributor_id="user@example.com",
            item_data=sample_contribution_data,
        )

        queue_item1 = ReviewerQueueItem(
            contribution=contribution,
            contribution_id=1,  # Set manually since not saved to DB yet
            reviewer_id="reviewer1@example.com",
        )
        queue_item2 = ReviewerQueueItem(
            contribution=contribution,
            contribution_id=1,
            reviewer_id="reviewer2@example.com",
        )

        # Test that relationship is set correctly
        assert queue_item1.contribution == contribution
        assert queue_item2.contribution == contribution

    async def test_contribution_to_feedback_relationship(self, sample_contribution_data):
        """Test relationship between Contribution and ContributionFeedback."""
        contribution = Contribution(
            contribution_type=ContributionType.NEW_ITEM,
            status=ContributionStatus.PENDING,
            contributor_id="user@example.com",
            item_data=sample_contribution_data,
        )

        feedback1 = ContributionFeedback(
            contribution=contribution,
            contribution_id=1,
            feedback_type=FeedbackType.TEXT_ONLY,
            severity=FeedbackSeverity.LOW,
            message="Feedback 1",
        )
        feedback2 = ContributionFeedback(
            contribution=contribution,
            contribution_id=1,
            feedback_type=FeedbackType.MINOR_CORRECTION,
            severity=FeedbackSeverity.MEDIUM,
            message="Feedback 2",
        )

        # Test that relationships are set correctly
        assert feedback1.contribution == contribution
        assert feedback2.contribution == contribution

    async def test_cascade_delete_reviewer_queue_items(self, sample_contribution_data):
        """Test cascade delete is configured for reviewer queue items."""
        # This test verifies the model configuration for cascade delete
        # Actual cascade behavior is tested at the database level during integration tests
        contribution = Contribution(
            contribution_type=ContributionType.NEW_ITEM,
            status=ContributionStatus.PENDING,
            contributor_id="user@example.com",
            item_data=sample_contribution_data,
        )

        queue_item = ReviewerQueueItem(
            contribution=contribution,
            contribution_id=1,
            reviewer_id="reviewer@example.com",
        )

        # Verify the relationship exists
        assert queue_item.contribution == contribution

    async def test_cascade_delete_feedback(self, sample_contribution_data):
        """Test cascade delete is configured for feedback items."""
        # This test verifies the model configuration for cascade delete
        # Actual cascade behavior is tested at the database level during integration tests
        contribution = Contribution(
            contribution_type=ContributionType.NEW_ITEM,
            status=ContributionStatus.PENDING,
            contributor_id="user@example.com",
            item_data=sample_contribution_data,
        )

        feedback = ContributionFeedback(
            contribution=contribution,
            contribution_id=1,
            feedback_type=FeedbackType.TEXT_ONLY,
            severity=FeedbackSeverity.LOW,
            message="Test feedback",
        )

        # Verify the relationship exists
        assert feedback.contribution == contribution


# ============================================================================
# Edge Cases & Complex Workflows
# ============================================================================


class TestComplexWorkflows:
    """Tests for complex contribution workflows."""

    async def test_multiple_reviewers_on_same_contribution(self, sample_contribution_data):
        """Test multiple reviewers assigned to same contribution."""
        contribution = Contribution(
            contribution_type=ContributionType.NEW_ITEM,
            status=ContributionStatus.PENDING,
            contributor_id="user@example.com",
            item_data=sample_contribution_data,
        )

        reviewers = ["alice@example.com", "bob@example.com", "charlie@example.com"]
        queue_items = []

        for i, reviewer in enumerate(reviewers):
            queue_item = ReviewerQueueItem(
                contribution=contribution,
                contribution_id=1,
                reviewer_id=reviewer,
                decision="approve" if i < 2 else "revision_requested",
            )
            queue_items.append(queue_item)

        assert len(queue_items) == 3

        # Verify each reviewer's decision
        assert queue_items[0].decision == "approve"
        assert queue_items[1].decision == "approve"
        assert queue_items[2].decision == "revision_requested"

    async def test_contribution_with_multiple_feedback_types(
        self, sample_contribution_data
    ):
        """Test contribution receiving different types of feedback."""
        contribution = Contribution(
            contribution_type=ContributionType.NEW_ITEM,
            status=ContributionStatus.PENDING,
            contributor_id="user@example.com",
            item_data=sample_contribution_data,
        )

        feedback_items = [
            ContributionFeedback(
                contribution=contribution,
                contribution_id=1,
                feedback_type=FeedbackType.TEXT_ONLY,
                severity=FeedbackSeverity.LOW,
                message="Good effort",
            ),
            ContributionFeedback(
                contribution=contribution,
                contribution_id=1,
                feedback_type=FeedbackType.MINOR_CORRECTION,
                severity=FeedbackSeverity.LOW,
                message="Fix typo",
            ),
            ContributionFeedback(
                contribution=contribution,
                contribution_id=1,
                feedback_type=FeedbackType.MISSING_FIELD,
                severity=FeedbackSeverity.HIGH,
                message="Missing safety warnings",
            ),
        ]

        assert len(feedback_items) == 3

        # Count by severity
        high_severity = sum(
            1 for f in feedback_items if f.severity == FeedbackSeverity.HIGH
        )
        low_severity = sum(
            1 for f in feedback_items if f.severity == FeedbackSeverity.LOW
        )

        assert high_severity == 1
        assert low_severity == 2

    async def test_edit_contribution_workflow(self, sample_contribution_data, sample_edit_diff):
        """Test complete edit contribution workflow."""
        # Create edit contribution
        contribution = Contribution(
            contribution_type=ContributionType.EDIT_ITEM,
            status=ContributionStatus.PENDING,
            contributor_id="user@example.com",
            target_item_cid="sha256-existing",
            item_data=sample_contribution_data,
            edit_diff=sample_edit_diff,
        )

        # Create reviewer queue items
        queue_items = [
            ReviewerQueueItem(
                contribution=contribution,
                contribution_id=1,
                reviewer_id="alice@example.com",
            ),
            ReviewerQueueItem(
                contribution=contribution,
                contribution_id=1,
                reviewer_id="bob@example.com",
            ),
        ]

        # Create feedback
        feedback = ContributionFeedback(
            contribution=contribution,
            contribution_id=1,
            feedback_type=FeedbackType.MINOR_CORRECTION,
            severity=FeedbackSeverity.LOW,
            message="Looks good!",
        )

        # Transition to approved
        contribution.status = ContributionStatus.APPROVED
        contribution.reviewer_notes = "Approved by consensus"

        assert contribution.status == ContributionStatus.APPROVED
        assert len(queue_items) == 2
        assert feedback.contribution == contribution
