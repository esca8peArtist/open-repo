"""Integration tests for Phase 3 API endpoints."""

import pytest
from datetime import datetime, timedelta
from unittest.mock import AsyncMock, MagicMock, patch


@pytest.fixture
def sample_contribution_data():
    """Sample contribution data for testing."""
    return {
        "title": {"en": "How to build a water filter"},
        "domain": "procedural",
        "license": "CC-BY-4.0",
        "description": {"en": "A guide to building a biosand water filter"},
        "type": "procedure",
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
    }


@pytest.fixture
def sample_revision_requests():
    """Sample revision requests for testing."""
    return [
        {"field": "steps[2].body", "suggestion": "Add safety note about heat"},
        {"field": "materials", "suggestion": "Include sourcing links"},
    ]


class TestContributionSubmissionEndpoints:
    """Tests for contribution submission endpoints (POST/GET /api/contributions)."""

    @pytest.mark.asyncio
    async def test_create_new_item_contribution(self, client, sample_contribution_data):
        """Test POST /api/contributions for new_item submission."""
        request_body = {
            "contribution_type": "new_item",
            "item_data": sample_contribution_data,
            "contributor_id": "user@example.com",
        }

        # Mock the service layer
        with patch('app.routes.ContributionService.create_contribution') as mock_create:
            from app.models import Contribution, ContributionStatus, ContributionType

            # Create a mock contribution object
            mock_contribution = MagicMock(spec=Contribution)
            mock_contribution.id = 1
            mock_contribution.contribution_type = ContributionType.NEW_ITEM
            mock_contribution.status = ContributionStatus.PENDING
            mock_contribution.contributor_id = "user@example.com"
            mock_contribution.created_at = datetime.utcnow()
            mock_contribution.updated_at = datetime.utcnow()
            mock_contribution.target_item_cid = None
            mock_contribution.proposed_cid = "sha256-abc123"
            mock_contribution.item_data = sample_contribution_data
            mock_contribution.edit_diff = None
            mock_contribution.reviewer_notes = None
            mock_contribution.rejection_reason = None
            mock_contribution.required_revisions = None

            mock_create.return_value = (mock_contribution, "sha256-abc123")

            response = await client.post("/api/contributions", json=request_body)

        assert response.status_code == 201
        data = response.json()
        assert data["id"] == 1
        assert data["contribution_type"] == "new_item"
        assert data["status"] == "pending"

    @pytest.mark.asyncio
    async def test_create_contribution_invalid_type(self, client, sample_contribution_data):
        """Test POST /api/contributions with invalid contribution_type."""
        request_body = {
            "contribution_type": "invalid_type",
            "item_data": sample_contribution_data,
        }

        response = await client.post("/api/contributions", json=request_body)

        assert response.status_code == 422  # Pydantic validation error

    @pytest.mark.asyncio
    async def test_create_contribution_duplicate_new_item(self, client, sample_contribution_data):
        """Test POST /api/contributions for duplicate new_item raises 409."""
        request_body = {
            "contribution_type": "new_item",
            "item_data": sample_contribution_data,
        }

        with patch('app.routes.ContributionService.create_contribution') as mock_create:
            mock_create.side_effect = ValueError("Item with CID sha256-dup already exists")

            response = await client.post("/api/contributions", json=request_body)

        assert response.status_code == 409

    @pytest.mark.asyncio
    async def test_list_contributions_all(self, client):
        """Test GET /api/contributions lists all contributions."""
        with patch('app.routes.ContributionService.list_contributions') as mock_list:
            from app.models import Contribution, ContributionStatus, ContributionType

            mock_contrib = MagicMock(spec=Contribution)
            mock_contrib.id = 1
            mock_contrib.contribution_type = ContributionType.NEW_ITEM
            mock_contrib.status = ContributionStatus.PENDING
            mock_contrib.created_at = datetime.utcnow()
            mock_contrib.updated_at = datetime.utcnow()
            mock_contrib.contributor_id = "user@example.com"
            mock_contrib.target_item_cid = None
            mock_contrib.proposed_cid = "sha256-abc"
            mock_contrib.item_data = {}
            mock_contrib.edit_diff = None
            mock_contrib.reviewer_notes = None
            mock_contrib.rejection_reason = None
            mock_contrib.required_revisions = None

            mock_list.return_value = ([mock_contrib], 1)

            response = await client.get("/api/contributions?limit=10&offset=0")

        assert response.status_code == 200
        data = response.json()
        assert data["total"] == 1
        assert len(data["items"]) == 1
        assert data["has_more"] is False

    @pytest.mark.asyncio
    async def test_get_contribution_by_id(self, client, sample_contribution_data):
        """Test GET /api/contributions/{id} retrieves a single contribution."""
        with patch('app.routes.ContributionService.get_contribution') as mock_get:
            from app.models import Contribution, ContributionStatus, ContributionType

            mock_contrib = MagicMock(spec=Contribution)
            mock_contrib.id = 1
            mock_contrib.contribution_type = ContributionType.NEW_ITEM
            mock_contrib.status = ContributionStatus.PENDING
            mock_contrib.item_data = sample_contribution_data
            mock_contrib.created_at = datetime.utcnow()
            mock_contrib.updated_at = datetime.utcnow()
            mock_contrib.contributor_id = "user@example.com"
            mock_contrib.target_item_cid = None
            mock_contrib.proposed_cid = "sha256-abc"
            mock_contrib.edit_diff = None
            mock_contrib.reviewer_notes = None
            mock_contrib.rejection_reason = None
            mock_contrib.required_revisions = None

            mock_get.return_value = mock_contrib

            response = await client.get("/api/contributions/1")

        assert response.status_code == 200
        data = response.json()
        assert data["id"] == 1

    @pytest.mark.asyncio
    async def test_get_contribution_not_found(self, client):
        """Test GET /api/contributions/{id} with non-existent ID."""
        with patch('app.routes.ContributionService.get_contribution') as mock_get:
            mock_get.return_value = None

            response = await client.get("/api/contributions/9999")

        assert response.status_code == 404


class TestReviewQueueEndpoints:
    """Tests for review queue endpoints."""

    @pytest.mark.asyncio
    async def test_get_review_queue(self, client):
        """Test GET /api/review/queue returns pending contributions."""
        with patch('app.routes.ReviewService.get_review_queue') as mock_get:
            from app.models import ReviewerQueueItem

            # Create mock review queue item
            mock_queue = MagicMock(spec=ReviewerQueueItem)
            mock_queue.assigned_at = datetime.utcnow()
            mock_queue.decided_at = None
            mock_queue.reviewer_id = "reviewer@example.com"

            # Mock contribution
            mock_contribution = MagicMock()
            mock_contribution.id = 1
            mock_contribution.status = "pending"
            mock_contribution.contribution_type = "new_item"
            mock_contribution.contributor_id = "user@example.com"
            mock_contribution.created_at = datetime.utcnow()
            mock_contribution.updated_at = datetime.utcnow()
            mock_contribution.target_item_cid = None
            mock_contribution.proposed_cid = "sha256-abc"
            mock_contribution.item_data = {}
            mock_contribution.edit_diff = None
            mock_contribution.reviewer_notes = None
            mock_contribution.rejection_reason = None
            mock_contribution.required_revisions = None

            mock_queue.contribution = mock_contribution

            mock_get.return_value = ([mock_queue], 1)

            response = await client.get("/api/review/queue?limit=10&offset=0")

        assert response.status_code == 200
        data = response.json()
        assert data["total"] == 1


class TestReviewDecisionEndpoints:
    """Tests for review decision endpoints."""

    @pytest.mark.asyncio
    async def test_submit_review_decision_approve(self, client):
        """Test POST /api/contributions/{id}/review with approve decision."""
        request_body = {
            "decision": "approve",
            "reviewer_notes": "Looks good!",
        }

        with patch('app.routes.ReviewService.submit_review_decision') as mock_submit:
            mock_submit.return_value = {
                "contribution_id": 1,
                "review_status": "pending",
                "feedback_submitted": True,
                "total_feedback_count": 1,
                "consensus_reached": False,
                "final_state": None,
            }

            response = await client.post("/api/contributions/1/review", json=request_body)

        assert response.status_code == 200
        data = response.json()
        assert data["feedback_submitted"] is True

    @pytest.mark.asyncio
    async def test_submit_review_decision_revision_requested(self, client, sample_revision_requests):
        """Test POST /api/contributions/{id}/review with revision_requested decision."""
        request_body = {
            "decision": "revision_requested",
            "reviewer_notes": "Needs improvements",
            "revision_requests": sample_revision_requests,
        }

        with patch('app.routes.ReviewService.submit_review_decision') as mock_submit:
            mock_submit.return_value = {
                "contribution_id": 1,
                "review_status": "pending",
                "feedback_submitted": True,
                "total_feedback_count": 1,
                "consensus_reached": False,
                "final_state": None,
            }

            response = await client.post("/api/contributions/1/review", json=request_body)

        assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_submit_review_decision_consensus_reached(self, client):
        """Test consensus detection when enough approvals received."""
        request_body = {
            "decision": "approve",
        }

        with patch('app.routes.ReviewService.submit_review_decision') as mock_submit:
            mock_submit.return_value = {
                "contribution_id": 1,
                "review_status": "reviewed",
                "feedback_submitted": True,
                "total_feedback_count": 2,
                "consensus_reached": True,
                "final_state": "approved",
            }

            response = await client.post("/api/contributions/1/review", json=request_body)

        assert response.status_code == 200
        data = response.json()
        assert data["consensus_reached"] is True
        assert data["final_state"] == "approved"

    @pytest.mark.asyncio
    async def test_quick_review_approve(self, client):
        """Test POST /api/contributions/{id}/review/approve shorthand."""
        with patch('app.routes.ReviewService.submit_review_decision') as mock_submit:
            mock_submit.return_value = {
                "contribution_id": 1,
                "review_status": "pending",
                "feedback_submitted": True,
                "total_feedback_count": 1,
                "consensus_reached": False,
                "final_state": None,
            }

            response = await client.post("/api/contributions/1/review/approve")

        assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_review_decision_not_found(self, client):
        """Test review decision on non-existent contribution."""
        request_body = {"decision": "approve"}

        with patch('app.routes.ReviewService.submit_review_decision') as mock_submit:
            mock_submit.side_effect = ValueError("not found")

            response = await client.post("/api/contributions/9999/review", json=request_body)

        assert response.status_code == 404


class TestReviewHistoryEndpoint:
    """Tests for review history endpoint."""

    @pytest.mark.asyncio
    async def test_get_review_history(self, client):
        """Test GET /api/contributions/{id}/review-history returns audit trail."""
        with patch('app.routes.ContributionService.get_contribution') as mock_get_contrib, \
             patch('app.routes.ReviewService.get_review_history') as mock_get_history:
            from app.models import Contribution, ContributionFeedback

            mock_contrib = MagicMock(spec=Contribution)
            mock_get_contrib.return_value = mock_contrib

            mock_feedback = MagicMock(spec=ContributionFeedback)
            mock_feedback.id = 1
            mock_feedback.reviewer_id = "reviewer@example.com"
            mock_feedback.decision = "approve"
            mock_feedback.reviewer_notes = "Good content"
            mock_feedback.created_at = datetime.utcnow()

            mock_get_history.return_value = [mock_feedback]

            response = await client.get("/api/contributions/1/review-history")

        assert response.status_code == 200
        data = response.json()
        assert len(data) == 1
        assert data[0]["decision"] == "approve"

    @pytest.mark.asyncio
    async def test_get_review_history_not_found(self, client):
        """Test review history for non-existent contribution."""
        with patch('app.routes.ContributionService.get_contribution') as mock_get:
            mock_get.return_value = None

            response = await client.get("/api/contributions/9999/review-history")

        assert response.status_code == 404


class TestFinalizationEndpoints:
    """Tests for contribution finalization endpoints."""

    @pytest.mark.asyncio
    async def test_finalize_contribution_approved(self, client):
        """Test POST /api/contributions/{id}/finalize with approved decision."""
        request_body = {
            "final_decision": "approved",
            "reason": "Consensus of 3 reviewers reached",
        }

        with patch('app.routes.ContributionService.get_contribution') as mock_get, \
             patch('app.routes.ContributionService.update_contribution_status') as mock_update:
            from app.models import Contribution, ContributionType, ContributionStatus

            mock_contrib = MagicMock(spec=Contribution)
            mock_contrib.id = 1
            mock_contrib.contribution_type = ContributionType.NEW_ITEM
            mock_contrib.status = ContributionStatus.PENDING
            mock_contrib.proposed_cid = "sha256-abc123"
            mock_contrib.item_data = {"title": {"en": "Test"}, "type": "procedure", "domain": "procedural", "license": "CC-BY-4.0"}

            mock_get.return_value = mock_contrib

            response = await client.post("/api/contributions/1/finalize", json=request_body)

        assert response.status_code == 200
        data = response.json()
        assert data["state"] == "approved"
        assert data["published_item_cid"] == "sha256-abc123"

    @pytest.mark.asyncio
    async def test_finalize_contribution_rejected(self, client):
        """Test POST /api/contributions/{id}/finalize with rejected decision."""
        request_body = {
            "final_decision": "rejected",
            "reason": "Content does not meet quality standards",
        }

        with patch('app.routes.ContributionService.get_contribution') as mock_get, \
             patch('app.routes.ContributionService.update_contribution_status') as mock_update:
            from app.models import Contribution, ContributionStatus

            mock_contrib = MagicMock(spec=Contribution)
            mock_contrib.id = 1
            mock_contrib.status = ContributionStatus.PENDING

            mock_get.return_value = mock_contrib

            response = await client.post("/api/contributions/1/finalize", json=request_body)

        assert response.status_code == 200
        data = response.json()
        assert data["state"] == "rejected"

    @pytest.mark.asyncio
    async def test_finalize_contribution_not_found(self, client):
        """Test finalize on non-existent contribution."""
        request_body = {
            "final_decision": "approved",
            "reason": "Test",
        }

        with patch('app.routes.ContributionService.get_contribution') as mock_get:
            mock_get.return_value = None

            response = await client.post("/api/contributions/9999/finalize", json=request_body)

        assert response.status_code == 404


class TestRequestRevisionEndpoint:
    """Tests for request revision endpoint."""

    @pytest.mark.asyncio
    async def test_request_revision(self, client, sample_revision_requests):
        """Test POST /api/contributions/{id}/request-revision."""
        request_body = {
            "revision_requests": sample_revision_requests,
            "deadline_days": 7,
        }

        with patch('app.routes.ContributionService.get_contribution') as mock_get, \
             patch('app.routes.ReviewService.request_revision') as mock_request:
            from app.models import Contribution, ContributionStatus

            mock_contrib = MagicMock(spec=Contribution)
            mock_contrib.id = 1
            mock_contrib.status = ContributionStatus.PENDING
            mock_contrib.updated_at = datetime.utcnow()

            mock_get.return_value = mock_contrib
            mock_request.return_value = mock_contrib

            response = await client.post("/api/contributions/1/request-revision", json=request_body)

        assert response.status_code == 200
        data = response.json()
        assert data["state"] == "revision_requested"
        assert len(data["revision_requests"]) == 2


class TestContributorStatsEndpoint:
    """Tests for contributor stats endpoint."""

    @pytest.mark.asyncio
    async def test_get_contributor_stats(self, client):
        """Test GET /api/contributors/{user_id}/stats."""
        with patch('app.routes.ContributorStatsService.get_contributor_stats') as mock_stats:
            mock_stats.return_value = {
                "user_id": "user@example.com",
                "total_submissions": 5,
                "approved_count": 3,
                "rejected_count": 1,
                "pending_count": 1,
                "revision_requested_count": 0,
                "approval_rate": 0.75,
                "endorsement_score": 15,
                "reputation_tier": "trusted",
                "first_submission": datetime.utcnow(),
                "last_submission": datetime.utcnow(),
            }

            response = await client.get("/api/contributors/user@example.com/stats")

        assert response.status_code == 200
        data = response.json()
        assert data["user_id"] == "user@example.com"
        assert data["total_submissions"] == 5
        assert data["approval_rate"] == 0.75
        assert data["reputation_tier"] == "trusted"

    @pytest.mark.asyncio
    async def test_get_contributor_stats_new_contributor(self, client):
        """Test stats for contributor with no submissions."""
        with patch('app.routes.ContributorStatsService.get_contributor_stats') as mock_stats:
            mock_stats.return_value = {
                "user_id": "newuser@example.com",
                "total_submissions": 0,
                "approved_count": 0,
                "rejected_count": 0,
                "pending_count": 0,
                "revision_requested_count": 0,
                "approval_rate": 0.0,
                "endorsement_score": 0,
                "reputation_tier": "none",
                "first_submission": None,
                "last_submission": None,
            }

            response = await client.get("/api/contributors/newuser@example.com/stats")

        assert response.status_code == 200
        data = response.json()
        assert data["total_submissions"] == 0
        assert data["reputation_tier"] == "none"
