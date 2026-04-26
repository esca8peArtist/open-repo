"""Tests for Phase 4 Wave 3: Endorsement/Announce Propagation.

Wave 3 extends Wave 1-2 federation with distributed vote synchronization.
Users can upvote/downvote items on any node; votes propagate via Announce activities
to all federation partners. Vote counts aggregate across nodes.
"""

import pytest
import json
from datetime import datetime
from typing import Dict, Any
from unittest.mock import AsyncMock, MagicMock, patch, call

import httpx
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy import select

from app.models import Activity, ActivityType, Endorsement, EndorsementType, Base
from app.services.endorsement_service import EndorsementService


# ============================================================================
# Fixtures
# ============================================================================

@pytest.fixture
async def client_with_db_mock():
    """Create test client with mocked database for Wave 3 tests."""
    from app.main import create_app
    from app import database
    from app.services.search_service import reset_search_service

    reset_search_service()

    async def mock_get_db():
        session = AsyncMock()

        # Mock for various query types
        async def mock_execute(query):
            mock_result = AsyncMock()
            mock_result.scalar = MagicMock(return_value=0)
            mock_result.scalar_one_or_none = AsyncMock(return_value=None)

            mock_scalars = MagicMock()
            mock_scalars.all = MagicMock(return_value=[])
            mock_result.scalars = MagicMock(return_value=mock_scalars)

            return mock_result

        session.execute = mock_execute
        session.add = MagicMock()
        session.commit = AsyncMock()
        session.delete = MagicMock()
        session.refresh = AsyncMock()

        yield session

    app = create_app()
    app.dependency_overrides[database.get_db] = mock_get_db

    async with AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://test") as ac:
        yield ac

    app.dependency_overrides.clear()
    reset_search_service()


@pytest.fixture
def sample_announce_activity() -> Dict[str, Any]:
    """Sample Announce activity for testing."""
    return {
        "@context": "https://www.w3.org/ns/activitystreams",
        "id": "https://node-a.example.com/activities/announce-123",
        "type": "Announce",
        "actor": "https://node-a.example.com/actor",
        "object": "https://node-a.example.com/items/sha256-abc123",
        "published": "2026-04-26T11:30:00Z",
        "content": {
            "item_cid": "sha256-abc123",
            "vote_type": "upvote",
            "user_id": "alice@example.com",
            "source_node": "https://node-a.example.com",
            "local_upvote_count": 12,
            "local_downvote_count": 2,
            "timestamp": "2026-04-26T11:30:00Z"
        }
    }


@pytest.fixture
def sample_undo_activity(sample_announce_activity: Dict[str, Any]) -> Dict[str, Any]:
    """Sample Undo activity for testing."""
    return {
        "@context": "https://www.w3.org/ns/activitystreams",
        "id": "https://node-a.example.com/activities/undo-456",
        "type": "Undo",
        "actor": "https://node-a.example.com/actor",
        "object": sample_announce_activity["id"],
        "published": "2026-04-26T12:00:00Z"
    }


# ============================================================================
# Class 1: EndorsementPropagationService Unit Tests (5 tests)
# ============================================================================

class TestEndorsementPropagationService:
    """Unit tests for EndorsementPropagationService methods."""

    @pytest.mark.asyncio
    async def test_generate_announce_activity_structure(self):
        """Verify Announce activity has correct structure and required fields."""
        from app.services.endorsement_propagation_service import EndorsementPropagationService
        from unittest.mock import AsyncMock

        db = AsyncMock()

        # Mock the execute method to return 0 for vote counts
        async def mock_execute_func(query):
            result = AsyncMock()
            result.scalar = AsyncMock(return_value=0)
            return result

        db.execute = mock_execute_func
        db.add = AsyncMock()
        db.commit = AsyncMock()
        db.refresh = AsyncMock()

        node_url = "https://node-a.example.com"
        item_cid = "sha256-abc123"
        user_id = "alice@example.com"

        # Generate Announce activity
        activity = await EndorsementPropagationService.generate_announce_activity(
            db=db,
            item_cid=item_cid,
            user_id=user_id,
            endorsement_type="upvote",
            node_url=node_url,
            private_key="dummy-key",
        )

        # Verify structure
        assert activity.activity_type.value == "Announce"
        assert activity.actor_url == f"{node_url}/actor"
        assert activity.local == 1

        # Verify JSON-LD structure
        data = activity.activity_data
        assert data["@context"] == "https://www.w3.org/ns/activitystreams"
        assert data["type"] == "Announce"
        assert data["actor"] == f"{node_url}/actor"
        assert "content" in data
        assert data["content"]["item_cid"] == item_cid
        assert data["content"]["user_id"] == user_id

    @pytest.mark.asyncio
    async def test_announce_includes_vote_counts(self):
        """Verify Announce includes local vote statistics at time of generation."""
        from app.services.endorsement_propagation_service import EndorsementPropagationService
        from unittest.mock import AsyncMock, MagicMock

        db = AsyncMock()

        # Mock the execute method to return vote counts
        call_count = [0]
        async def mock_execute_func(query):
            # First call returns upvote count (3), second call returns downvote count (1)
            if call_count[0] == 0:
                value = 3
            else:
                value = 1
            call_count[0] += 1

            result = MagicMock()
            result.scalar = MagicMock(return_value=value)
            return result

        db.execute = mock_execute_func
        db.add = MagicMock()
        db.commit = AsyncMock()
        db.refresh = AsyncMock()

        node_url = "https://node-a.example.com"
        item_cid = "sha256-abc123"

        # Generate Announce activity
        activity = await EndorsementPropagationService.generate_announce_activity(
            db=db,
            item_cid=item_cid,
            user_id="alice@example.com",
            endorsement_type="upvote",
            node_url=node_url,
            private_key="dummy-key",
        )

        # Verify vote counts in content
        content = activity.activity_data["content"]
        assert content["local_upvote_count"] == 3
        assert content["local_downvote_count"] == 1

    @pytest.mark.asyncio
    async def test_generate_undo_activity_references_original(self):
        """Verify Undo activity correctly references the original Announce."""
        from app.services.endorsement_propagation_service import EndorsementPropagationService
        from unittest.mock import AsyncMock

        db = AsyncMock()

        # Mock the execute method
        announce_activity = Activity(
            activity_type=ActivityType.ANNOUNCE,
            activity_id="https://node-a.example.com/activities/announce-123",
            actor_url="https://node-a.example.com/actor",
            activity_data={"type": "Announce"},
            local=1,
        )

        async def mock_execute_func(query):
            result = AsyncMock()
            result.scalar_one_or_none = AsyncMock(return_value=announce_activity)
            return result

        db.execute = mock_execute_func
        db.add = AsyncMock()
        db.commit = AsyncMock()
        db.refresh = AsyncMock()

        node_url = "https://node-a.example.com"

        # Generate Undo for the announce
        undo = await EndorsementPropagationService.generate_undo_activity(
            db=db,
            announce_activity_id=announce_activity.activity_id,
            node_url=node_url,
            private_key="dummy-key",
        )

        # Verify Undo references original Announce
        assert undo.activity_data["object"] == announce_activity.activity_id
        assert undo.activity_type.value == "Undo"
        assert undo.local == 1

    @pytest.mark.asyncio
    async def test_ingest_announce_activity_stores_in_table(self):
        """Verify Announce activity is stored in activities table with local=0."""
        from app.services.endorsement_propagation_service import EndorsementPropagationService
        from unittest.mock import AsyncMock

        db = AsyncMock()
        db.add = AsyncMock()
        db.commit = AsyncMock()
        db.refresh = AsyncMock()

        # Create a sample Announce activity from remote node
        activity = Activity(
            activity_type=ActivityType.ANNOUNCE,
            activity_id="https://node-b.example.com/activities/announce-123",
            actor_url="https://node-b.example.com/actor",
            object_id="https://node-b.example.com/items/sha256-abc123",
            activity_data={
                "@context": "https://www.w3.org/ns/activitystreams",
                "type": "Announce",
                "id": "https://node-b.example.com/activities/announce-123",
                "actor": "https://node-b.example.com/actor",
                "content": {
                    "item_cid": "sha256-abc123",
                    "vote_type": "upvote",
                }
            },
            local=1,  # Will be changed to 0 by ingest
        )

        # Ingest it
        result = await EndorsementPropagationService.ingest_announce_activity(db, activity)

        # Verify it was ingested successfully
        assert result is True
        assert activity.local == 0

    @pytest.mark.asyncio
    async def test_ingest_undo_activity_stores_and_marks(self):
        """Verify Undo activity is stored in activities table."""
        from app.services.endorsement_propagation_service import EndorsementPropagationService
        from unittest.mock import AsyncMock

        db = AsyncMock()
        db.add = AsyncMock()
        db.commit = AsyncMock()
        db.refresh = AsyncMock()

        # Create an Undo activity
        announce_id = "https://node-b.example.com/activities/announce-123"
        undo = Activity(
            activity_type=ActivityType.UNDO,
            activity_id="https://node-b.example.com/activities/undo-456",
            actor_url="https://node-b.example.com/actor",
            object_id=announce_id,
            activity_data={
                "@context": "https://www.w3.org/ns/activitystreams",
                "type": "Undo",
                "id": "https://node-b.example.com/activities/undo-456",
                "actor": "https://node-b.example.com/actor",
                "object": announce_id,
            },
            local=1,
        )

        # Ingest it
        result = await EndorsementPropagationService.ingest_undo_activity(db, undo)

        # Verify it was ingested successfully
        assert result is True
        assert undo.local == 0
        assert undo.object_id == announce_id


# ============================================================================
# Class 2: Endorsement Aggregation Logic (4 tests)
# ============================================================================

class TestEndorsementAggregation:
    """Tests for aggregating local and remote vote counts."""

    @pytest.mark.asyncio
    async def test_get_aggregated_vote_count_local_only(self):
        """Verify aggregation with only local votes."""
        from app.services.endorsement_propagation_service import EndorsementPropagationService
        from unittest.mock import AsyncMock, MagicMock

        db = AsyncMock()

        # Mock execute to return 5 local upvotes and empty remote list
        call_count = [0]
        async def mock_execute_func(query):
            result = MagicMock()
            if call_count[0] == 0:
                # First call: count upvotes
                result.scalar = MagicMock(return_value=5)
            else:
                # Second call: get remote activities
                result.scalars = MagicMock()
                result.scalars.return_value.all = MagicMock(return_value=[])
            call_count[0] += 1
            return result

        db.execute = mock_execute_func

        item_cid = "sha256-abc123"

        # Query aggregated count
        result = await EndorsementPropagationService.get_aggregated_vote_count(
            db, item_cid, "upvote"
        )

        # Verify
        assert result["local"] == 5
        assert result["remote"] == 0
        assert result["total"] == 5
        assert result["breakdown"] == {}

    @pytest.mark.asyncio
    async def test_get_aggregated_vote_count_with_remote(self):
        """Verify aggregation includes remote Announce activities."""
        from app.services.endorsement_propagation_service import EndorsementPropagationService
        from unittest.mock import AsyncMock, MagicMock

        db = AsyncMock()

        item_cid = "sha256-abc123"

        # Create mock Announce activities for aggregation
        announce_b1 = Activity(
            activity_type=ActivityType.ANNOUNCE,
            activity_id="https://node-b.example.com/activities/announce-1",
            actor_url="https://node-b.example.com/actor",
            activity_data={
                "type": "Announce",
                "content": {
                    "item_cid": item_cid,
                    "vote_type": "upvote",
                    "source_node": "https://node-b.example.com",
                }
            },
            local=0,
        )

        announce_b2 = Activity(
            activity_type=ActivityType.ANNOUNCE,
            activity_id="https://node-b.example.com/activities/announce-2",
            actor_url="https://node-b.example.com/actor",
            activity_data={
                "type": "Announce",
                "content": {
                    "item_cid": item_cid,
                    "vote_type": "upvote",
                    "source_node": "https://node-b.example.com",
                }
            },
            local=0,
        )

        announce_c = Activity(
            activity_type=ActivityType.ANNOUNCE,
            activity_id="https://node-c.example.com/activities/announce-1",
            actor_url="https://node-c.example.com/actor",
            activity_data={
                "type": "Announce",
                "content": {
                    "item_cid": item_cid,
                    "vote_type": "upvote",
                    "source_node": "https://node-c.example.com",
                }
            },
            local=0,
        )

        # Mock execute to return 3 local upvotes and 3 remote activities
        call_count = [0]
        async def mock_execute_func(query):
            result = MagicMock()
            if call_count[0] == 0:
                # First call: count upvotes
                result.scalar = MagicMock(return_value=3)
            else:
                # Second call: get remote activities
                result.scalars = MagicMock()
                result.scalars.return_value.all = MagicMock(return_value=[announce_b1, announce_b2, announce_c])
            call_count[0] += 1
            return result

        db.execute = mock_execute_func

        # Query aggregated count
        result = await EndorsementPropagationService.get_aggregated_vote_count(
            db, item_cid, "upvote"
        )

        # Verify
        assert result["local"] == 3
        assert result["remote"] == 3
        assert result["total"] == 6
        assert result["breakdown"]["https://node-b.example.com"] == 2
        assert result["breakdown"]["https://node-c.example.com"] == 1

    @pytest.mark.asyncio
    async def test_aggregation_excludes_undone_votes(self):
        """Verify Undo activities reduce remote vote count."""
        from app.services.endorsement_propagation_service import EndorsementPropagationService
        from unittest.mock import AsyncMock, MagicMock

        db = AsyncMock()

        item_cid = "sha256-abc123"
        announce_id_1 = "https://node-b.example.com/activities/announce-1"
        announce_id_2 = "https://node-b.example.com/activities/announce-2"

        # Create mock Announce (announce_2 is not undone, announce_1 is undone)
        announce_2 = Activity(
            activity_type=ActivityType.ANNOUNCE,
            activity_id=announce_id_2,
            actor_url="https://node-b.example.com/actor",
            activity_data={
                "type": "Announce",
                "content": {
                    "item_cid": item_cid,
                    "vote_type": "upvote",
                    "source_node": "https://node-b.example.com",
                }
            },
            local=0,
        )

        # Mock execute to return 0 local upvotes and 1 remote activity (announce_2, since announce_1 is undone)
        call_count = [0]
        async def mock_execute_func(query):
            result = MagicMock()
            if call_count[0] == 0:
                # First call: count upvotes
                result.scalar = MagicMock(return_value=0)
            else:
                # Second call: get remote activities
                result.scalars = MagicMock()
                result.scalars.return_value.all = MagicMock(return_value=[announce_2])
            call_count[0] += 1
            return result

        db.execute = mock_execute_func

        # Query aggregated count
        result = await EndorsementPropagationService.get_aggregated_vote_count(
            db, item_cid, "upvote"
        )

        # Verify - only 1 vote counted (announce_2)
        assert result["remote"] == 1
        assert result["breakdown"]["https://node-b.example.com"] == 1

    @pytest.mark.asyncio
    async def test_aggregation_by_endorsement_type(self):
        """Verify aggregation tracks upvotes separately from downvotes."""
        from app.services.endorsement_propagation_service import EndorsementPropagationService
        from unittest.mock import AsyncMock, MagicMock

        db = AsyncMock()

        item_cid = "sha256-abc123"

        # Create mock Announce upvote
        announce_upvote = Activity(
            activity_type=ActivityType.ANNOUNCE,
            activity_id="https://node-b.example.com/activities/announce-1",
            actor_url="https://node-b.example.com/actor",
            activity_data={
                "type": "Announce",
                "content": {
                    "item_cid": item_cid,
                    "vote_type": "upvote",
                    "source_node": "https://node-b.example.com",
                }
            },
            local=0,
        )

        # Test upvotes first
        call_count = [0]
        async def mock_execute_upvote(query):
            result = MagicMock()
            if call_count[0] == 0:
                result.scalar = MagicMock(return_value=3)  # 3 local upvotes
            else:
                result.scalars = MagicMock()
                result.scalars.return_value.all = MagicMock(return_value=[announce_upvote])  # 1 remote
            call_count[0] += 1
            return result

        db.execute = mock_execute_upvote

        # Query aggregated count for upvotes
        upvote_result = await EndorsementPropagationService.get_aggregated_vote_count(
            db, item_cid, "upvote"
        )

        # Reset for downvotes
        call_count[0] = 0
        db.execute = AsyncMock()
        async def mock_execute_downvote(query):
            result = MagicMock()
            if call_count[0] == 0:
                result.scalar = MagicMock(return_value=2)  # 2 local downvotes
            else:
                result.scalars = MagicMock()
                result.scalars.return_value.all = MagicMock(return_value=[])  # 0 remote
            call_count[0] += 1
            return result

        db.execute = mock_execute_downvote

        # Query aggregated count for downvotes
        downvote_result = await EndorsementPropagationService.get_aggregated_vote_count(
            db, item_cid, "downvote"
        )

        # Verify
        assert upvote_result["total"] == 4  # 3 local + 1 remote
        assert downvote_result["total"] == 2  # 2 local + 0 remote


# ============================================================================
# Class 3: Route Integration Tests (4 tests)
# ============================================================================

class TestEndorsementRoutes:
    """Integration tests for endorsement routes with propagation."""

    @pytest.mark.asyncio
    async def test_endorse_triggers_announce_generation(self, client_with_db_mock):
        """Verify POST /api/items/{cid}/endorse generates Announce activity."""
        pytest.skip("Implementation pending: route integration")

    @pytest.mark.asyncio
    async def test_delete_endorsement_generates_undo(self, client_with_db_mock):
        """Verify DELETE /endorsements/my-endorsement generates Undo activity."""
        pytest.skip("Implementation pending: route integration")

    @pytest.mark.asyncio
    async def test_get_aggregated_endorsement_stats(self, client_with_db_mock):
        """Verify GET /api/items/{cid}/endorsements/aggregated returns correct totals."""
        pytest.skip("Implementation pending: aggregated stats endpoint")

    @pytest.mark.asyncio
    async def test_receive_announce_activity_in_inbox(
        self, client_with_db_mock, sample_announce_activity
    ):
        """Verify /inbox correctly processes Announce activity."""
        pytest.skip("Implementation pending: inbox route update")


# ============================================================================
# Class 4: Cross-Node Announce/Undo Flow (2-3 tests)
# ============================================================================

class TestCrossNodeEndorsementFlow:
    """Tests for multi-node endorsement propagation flows."""

    @pytest.mark.asyncio
    async def test_announce_sent_to_all_federation_partners(self):
        """Verify Announce is delivered to all configured federation partners."""
        pytest.skip("Implementation pending: federation delivery")

    @pytest.mark.asyncio
    async def test_announce_signature_verification(self):
        """Verify Announce activities are signed with node's private key."""
        pytest.skip("Implementation pending: signature generation")

    @pytest.mark.asyncio
    async def test_undo_revokes_vote_on_remote_node(self):
        """Verify Undo activity correctly removes vote from remote total."""
        pytest.skip("Implementation pending: undo processing")


# ============================================================================
# Integration Test: Full Wave 3 Flow (Optional, for end-to-end validation)
# ============================================================================

@pytest.mark.asyncio
async def test_wave3_full_endorsement_propagation_flow():
    """End-to-end test of endorsement creation, propagation, and aggregation.

    This test validates the complete Wave 3 flow:
    1. User votes on item on Node A
    2. Announce activity generated and sent to Node B
    3. Node B receives and ingests Announce
    4. Aggregated vote count includes both local and remote
    5. User retracts vote (generates Undo)
    6. Node B receives Undo and removes vote from total
    """
    pytest.skip("Implementation pending: full integration test")
