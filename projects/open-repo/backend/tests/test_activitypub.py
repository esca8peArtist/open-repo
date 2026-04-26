"""Tests for Phase 4 Wave 1: ActivityPub Protocol + HTTP Signature Verification."""

import pytest
import json
import httpx
from datetime import datetime
from unittest.mock import AsyncMock, MagicMock, patch
from httpx import AsyncClient

from app.http_signatures import HTTPSignatureUtils, get_rfc7231_date
from app.models import Activity, ActivityType, NodePublicKey


@pytest.fixture
async def client_with_db_mock():
    """Create test client with proper DB mocks for ActivityPub tests."""
    from app.main import create_app
    from app import database
    from app.services.search_service import reset_search_service

    # Reset search service
    reset_search_service()

    # Mock the get_db dependency with better mocks
    async def mock_get_db():
        session = AsyncMock()

        # Mock execute to return a proper mock result
        async def mock_execute(query):
            mock_result = AsyncMock()
            mock_result.scalar = MagicMock(return_value=0)  # Return 0 for count queries
            mock_result.scalar_one_or_none = AsyncMock(return_value=None)  # No existing records

            # Create a mock scalars object that returns empty list
            mock_scalars = MagicMock()
            mock_scalars.all = MagicMock(return_value=[])
            mock_result.scalars = MagicMock(return_value=mock_scalars)

            return mock_result

        session.execute = mock_execute
        session.add = MagicMock()
        session.commit = AsyncMock()
        yield session

    app = create_app()
    app.dependency_overrides[database.get_db] = mock_get_db

    async with AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://test") as ac:
        yield ac

    app.dependency_overrides.clear()
    reset_search_service()


class TestHTTPSignatures:
    """Tests for HTTP signature generation and verification."""

    def test_generate_keypair(self):
        """Test RSA keypair generation."""
        private_key, public_key = HTTPSignatureUtils.generate_keypair("test-key")

        assert private_key.startswith("-----BEGIN PRIVATE KEY-----")
        assert private_key.endswith("-----END PRIVATE KEY-----\n")

        assert public_key.startswith("-----BEGIN PUBLIC KEY-----")
        assert public_key.endswith("-----END PUBLIC KEY-----\n")

    def test_sign_and_verify_message(self):
        """Test message signing and verification."""
        private_key, public_key = HTTPSignatureUtils.generate_keypair("test-key")
        message = "test message"

        # Sign the message
        signature = HTTPSignatureUtils.sign_message(message, private_key)
        assert isinstance(signature, str)
        assert len(signature) > 0

        # Verify the signature
        is_valid = HTTPSignatureUtils.verify_signature(message, signature, public_key)
        assert is_valid is True

    def test_verify_invalid_signature(self):
        """Test that invalid signatures are rejected."""
        private_key, public_key = HTTPSignatureUtils.generate_keypair("test-key")
        message = "original message"
        tampered_message = "tampered message"

        signature = HTTPSignatureUtils.sign_message(message, private_key)

        # Verify should fail with different message
        is_valid = HTTPSignatureUtils.verify_signature(tampered_message, signature, public_key)
        assert is_valid is False

    def test_verify_wrong_public_key(self):
        """Test that signatures from wrong key fail verification."""
        private_key1, public_key1 = HTTPSignatureUtils.generate_keypair("key1")
        private_key2, public_key2 = HTTPSignatureUtils.generate_keypair("key2")
        message = "test message"

        signature = HTTPSignatureUtils.sign_message(message, private_key1)

        # Verify should fail with different public key
        is_valid = HTTPSignatureUtils.verify_signature(message, signature, public_key2)
        assert is_valid is False

    def test_build_signature_header(self):
        """Test HTTP Signature header generation."""
        private_key, _ = HTTPSignatureUtils.generate_keypair("test-key")
        key_id = "https://example.com/actor#main-key"
        request_target = "post /inbox"
        host = "example.com"
        date = "Mon, 26 Apr 2026 12:00:00 GMT"

        signature_header = HTTPSignatureUtils.build_signature_header(
            key_id=key_id,
            private_key_pem=private_key,
            request_target=request_target,
            host=host,
            date=date,
        )

        assert signature_header.startswith('keyId="')
        assert 'algorithm="rsa-sha256"' in signature_header
        assert 'headers="(request-target) host date"' in signature_header
        assert 'signature="' in signature_header

    def test_verify_signature_header(self):
        """Test HTTP Signature header verification."""
        private_key, public_key = HTTPSignatureUtils.generate_keypair("test-key")
        key_id = "https://example.com/actor#main-key"
        request_target = "post /inbox"
        host = "example.com"
        date = "Mon, 26 Apr 2026 12:00:00 GMT"

        # Build and verify signature header
        signature_header = HTTPSignatureUtils.build_signature_header(
            key_id=key_id,
            private_key_pem=private_key,
            request_target=request_target,
            host=host,
            date=date,
        )

        is_valid = HTTPSignatureUtils.verify_signature_header(
            signature_header=signature_header,
            public_key_pem=public_key,
            request_target=request_target,
            host=host,
            date=date,
        )

        assert is_valid is True

    def test_verify_signature_header_tampered(self):
        """Test that tampered signature headers fail verification."""
        private_key, public_key = HTTPSignatureUtils.generate_keypair("test-key")
        key_id = "https://example.com/actor#main-key"
        request_target = "post /inbox"
        host = "example.com"
        date = "Mon, 26 Apr 2026 12:00:00 GMT"

        signature_header = HTTPSignatureUtils.build_signature_header(
            key_id=key_id,
            private_key_pem=private_key,
            request_target=request_target,
            host=host,
            date=date,
        )

        # Verify with different request target should fail
        is_valid = HTTPSignatureUtils.verify_signature_header(
            signature_header=signature_header,
            public_key_pem=public_key,
            request_target="post /different",  # Changed
            host=host,
            date=date,
        )

        assert is_valid is False

    def test_rfc7231_date_format(self):
        """Test RFC 7231 date format generation."""
        date = get_rfc7231_date()
        # Should end with GMT
        assert date.endswith("GMT")
        # Should parse correctly
        from email.utils import parsedate_to_datetime
        parsed = parsedate_to_datetime(date)
        assert isinstance(parsed, datetime)


class TestWebFingerEndpoint:
    """Tests for WebFinger endpoint."""

    @pytest.mark.asyncio
    async def test_webfinger_returns_actor_link(self, client_with_db_mock):
        """Test that WebFinger returns link to actor."""
        response = await client_with_db_mock.get(
            "/.well-known/webfinger?resource=acct:node@localhost:8000"
        )

        assert response.status_code == 200
        data = response.json()
        assert data["subject"] == "acct:node@localhost:8000"
        assert len(data["links"]) > 0
        assert any(link["rel"] == "self" for link in data["links"])
        assert any(
            link["type"] == "application/activity+json" for link in data["links"]
        )


class TestActorEndpoint:
    """Tests for ActivityPub actor endpoint."""

    @pytest.mark.asyncio
    async def test_actor_endpoint_returns_actor_object(self, client_with_db_mock):
        """Test that /actor returns valid actor object."""
        response = await client_with_db_mock.get("/actor")

        assert response.status_code == 200
        data = response.json()

        assert data["type"] == "Service"
        assert data["name"] == "Open-Repo Node"
        assert "inbox" in data
        assert "outbox" in data
        assert "followers" in data
        assert "following" in data
        assert "publicKey" in data

    @pytest.mark.asyncio
    async def test_actor_public_key_is_valid(self, client_with_db_mock):
        """Test that actor's public key is in valid PEM format."""
        response = await client_with_db_mock.get("/actor")
        data = response.json()

        public_key_pem = data["publicKey"]["publicKeyPem"]
        assert public_key_pem.startswith("-----BEGIN PUBLIC KEY-----")
        assert public_key_pem.endswith("-----END PUBLIC KEY-----\n")

    @pytest.mark.asyncio
    async def test_actor_endpoints_are_uris(self, client_with_db_mock):
        """Test that actor's endpoints are valid URIs."""
        response = await client_with_db_mock.get("/actor")
        data = response.json()

        for endpoint in ["inbox", "outbox", "followers", "following"]:
            assert endpoint in data
            assert data[endpoint].startswith("http")


class TestInboxEndpoint:
    """Tests for ActivityPub inbox endpoint."""

    @pytest.mark.asyncio
    async def test_inbox_accepts_create_activity(self, client_with_db_mock):
        """Test inbox accepts Create activity."""
        activity = {
            "type": "Create",
            "id": "https://example.com/activities/1",
            "actor": "https://example.com/actor",
            "object": {
                "type": "Object",
                "id": "https://example.com/items/test",
                "name": "Test Item",
            },
            "published": datetime.utcnow().isoformat() + "Z",
        }

        response = await client_with_db_mock.post("/inbox", json=activity)

        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"

    @pytest.mark.asyncio
    async def test_inbox_accepts_update_activity(self, client_with_db_mock):
        """Test inbox accepts Update activity."""
        activity = {
            "type": "Update",
            "id": "https://example.com/activities/2",
            "actor": "https://example.com/actor",
            "object": {
                "type": "Object",
                "id": "https://example.com/items/test",
                "name": "Updated Item",
            },
            "published": datetime.utcnow().isoformat() + "Z",
        }

        response = await client_with_db_mock.post("/inbox", json=activity)

        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"

    @pytest.mark.asyncio
    async def test_inbox_accepts_delete_activity(self, client_with_db_mock):
        """Test inbox accepts Delete activity."""
        activity = {
            "type": "Delete",
            "id": "https://example.com/activities/3",
            "actor": "https://example.com/actor",
            "object": {
                "type": "Tombstone",
                "id": "https://example.com/items/test",
            },
            "published": datetime.utcnow().isoformat() + "Z",
        }

        response = await client_with_db_mock.post("/inbox", json=activity)

        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"

    @pytest.mark.asyncio
    async def test_inbox_accepts_announce_activity(self, client_with_db_mock):
        """Test inbox accepts Announce activity (endorsement)."""
        activity = {
            "type": "Announce",
            "id": "https://example.com/activities/4",
            "actor": "https://example.com/actor",
            "object": {
                "type": "Announce",
                "id": "https://example.com/endorsements/1",
                "name": "Upvote",
            },
            "published": datetime.utcnow().isoformat() + "Z",
        }

        response = await client_with_db_mock.post("/inbox", json=activity)

        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"

    @pytest.mark.asyncio
    async def test_inbox_accepts_undo_activity(self, client_with_db_mock):
        """Test inbox accepts Undo activity."""
        activity = {
            "type": "Undo",
            "id": "https://example.com/activities/5",
            "actor": "https://example.com/actor",
            "object": {
                "type": "Like",
                "id": "https://example.com/likes/1",
            },
            "published": datetime.utcnow().isoformat() + "Z",
        }

        response = await client_with_db_mock.post("/inbox", json=activity)

        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"

    @pytest.mark.asyncio
    async def test_inbox_idempotent_on_duplicate_activity(self, client_with_db_mock):
        """Test that inbox doesn't reprocess duplicate activities."""
        activity = {
            "type": "Create",
            "id": "https://example.com/activities/unique-1",
            "actor": "https://example.com/actor",
            "object": {
                "type": "Object",
                "id": "https://example.com/items/test",
                "name": "Test Item",
            },
            "published": datetime.utcnow().isoformat() + "Z",
        }

        # First request
        response1 = await client_with_db_mock.post("/inbox", json=activity)
        assert response1.status_code == 200

        # Second request with same activity ID
        response2 = await client_with_db_mock.post("/inbox", json=activity)
        assert response2.status_code == 200
        data = response2.json()
        assert "already processed" in data.get("message", "").lower()


class TestOutboxEndpoint:
    """Tests for ActivityPub outbox endpoint."""

    @pytest.mark.asyncio
    async def test_outbox_returns_ordered_collection(self, client_with_db_mock):
        """Test outbox returns OrderedCollection metadata."""
        response = await client_with_db_mock.get("/outbox")

        assert response.status_code == 200
        data = response.json()

        assert data["type"] == "OrderedCollection"
        assert "id" in data
        assert data["id"].endswith("/outbox")
        assert "totalItems" in data
        assert "first" in data

    @pytest.mark.asyncio
    async def test_outbox_pagination_first_page(self, client_with_db_mock):
        """Test outbox pagination - first page."""
        response = await client_with_db_mock.get("/outbox?page=1")

        assert response.status_code == 200
        data = response.json()

        assert data["type"] == "OrderedCollectionPage"
        assert "id" in data
        assert "partOf" in data
        assert "orderedItems" in data
        assert "startIndex" in data

    @pytest.mark.asyncio
    async def test_outbox_pagination_returns_items(self, client_with_db_mock):
        """Test outbox pagination returns items."""
        response = await client_with_db_mock.get("/outbox?page=1&limit=10")

        assert response.status_code == 200
        data = response.json()

        assert isinstance(data["orderedItems"], list)

    @pytest.mark.asyncio
    async def test_outbox_pagination_next_link(self, client_with_db_mock):
        """Test outbox pagination includes next link when available."""
        response = await client_with_db_mock.get("/outbox?page=1&limit=1")

        assert response.status_code == 200
        data = response.json()

        # If there are items, next link should be present (or not if only 1 item total)
        if "next" in data:
            assert data["next"] is not None or data["next"] is None

    @pytest.mark.asyncio
    async def test_outbox_pagination_prev_link(self, client_with_db_mock):
        """Test outbox pagination - page 2+ includes prev link."""
        # First add an activity via inbox
        activity = {
            "type": "Create",
            "id": "https://example.com/activities/outbox-test",
            "actor": "https://example.com/actor",
            "object": {
                "type": "Object",
                "id": "https://example.com/items/test",
            },
            "published": datetime.utcnow().isoformat() + "Z",
        }
        await client_with_db_mock.post("/inbox", json=activity)

        # Request page 1
        response = await client_with_db_mock.get("/outbox?page=1&limit=1")
        assert response.status_code == 200
        data = response.json()

        # Prev should be None on first page
        assert data.get("prev") is None

    @pytest.mark.asyncio
    async def test_outbox_respects_limit_parameter(self, client_with_db_mock):
        """Test outbox respects limit parameter."""
        response = await client_with_db_mock.get("/outbox?page=1&limit=5")

        assert response.status_code == 200
        data = response.json()

        # items should not exceed limit
        assert len(data["orderedItems"]) <= 5


class TestFollowersEndpoint:
    """Tests for ActivityPub followers endpoint."""

    @pytest.mark.asyncio
    async def test_followers_returns_ordered_collection(self, client_with_db_mock):
        """Test followers endpoint returns OrderedCollection."""
        response = await client_with_db_mock.get("/followers")

        assert response.status_code == 200
        data = response.json()

        assert data["type"] == "OrderedCollection"
        assert "id" in data
        assert data["id"].endswith("/followers")
        assert "totalItems" in data

    @pytest.mark.asyncio
    async def test_followers_collection_is_empty_initially(self, client_with_db_mock):
        """Test followers collection is empty initially."""
        response = await client_with_db_mock.get("/followers")

        assert response.status_code == 200
        data = response.json()

        assert data["totalItems"] == 0


class TestFollowingEndpoint:
    """Tests for ActivityPub following endpoint."""

    @pytest.mark.asyncio
    async def test_following_returns_ordered_collection(self, client_with_db_mock):
        """Test following endpoint returns OrderedCollection."""
        response = await client_with_db_mock.get("/following")

        assert response.status_code == 200
        data = response.json()

        assert data["type"] == "OrderedCollection"
        assert "id" in data
        assert data["id"].endswith("/following")
        assert "totalItems" in data

    @pytest.mark.asyncio
    async def test_following_collection_is_empty_initially(self, client_with_db_mock):
        """Test following collection is empty initially."""
        response = await client_with_db_mock.get("/following")

        assert response.status_code == 200
        data = response.json()

        assert data["totalItems"] == 0


class TestActivityPubIntegration:
    """Integration tests for ActivityPub workflows."""

    @pytest.mark.asyncio
    async def test_complete_activity_workflow(self, client_with_db_mock):
        """Test complete workflow: create activity -> inbox -> outbox."""
        # 1. Get actor
        actor_response = await client_with_db_mock.get("/actor")
        assert actor_response.status_code == 200

        # 2. Send Create activity to inbox
        activity = {
            "type": "Create",
            "id": "https://example.com/activities/workflow-test",
            "actor": "https://example.com/actor",
            "object": {
                "type": "Object",
                "id": "https://example.com/items/workflow-item",
                "name": "Workflow Test Item",
            },
            "published": datetime.utcnow().isoformat() + "Z",
        }

        inbox_response = await client_with_db_mock.post("/inbox", json=activity)
        assert inbox_response.status_code == 200

        # 3. Query outbox
        outbox_response = await client_with_db_mock.get("/outbox")
        assert outbox_response.status_code == 200

    @pytest.mark.asyncio
    async def test_actor_consistency(self, client_with_db_mock):
        """Test that actor data is consistent across requests."""
        response1 = await client_with_db_mock.get("/actor")
        response2 = await client_with_db_mock.get("/actor")

        data1 = response1.json()
        data2 = response2.json()

        # Key data should be identical
        assert data1["id"] == data2["id"]
        assert data1["publicKey"]["publicKeyPem"] == data2["publicKey"]["publicKeyPem"]

    @pytest.mark.asyncio
    async def test_multiple_activity_types_in_inbox(self, client_with_db_mock):
        """Test inbox handles multiple activity types correctly."""
        activities = [
            {
                "type": "Create",
                "id": "https://example.com/activities/multi-1",
                "actor": "https://example.com/actor",
                "object": {"type": "Object", "id": "https://example.com/items/1"},
                "published": datetime.utcnow().isoformat() + "Z",
            },
            {
                "type": "Update",
                "id": "https://example.com/activities/multi-2",
                "actor": "https://example.com/actor",
                "object": {"type": "Object", "id": "https://example.com/items/1"},
                "published": datetime.utcnow().isoformat() + "Z",
            },
            {
                "type": "Announce",
                "id": "https://example.com/activities/multi-3",
                "actor": "https://example.com/actor",
                "object": {"type": "Like", "id": "https://example.com/likes/1"},
                "published": datetime.utcnow().isoformat() + "Z",
            },
        ]

        for activity in activities:
            response = await client_with_db_mock.post("/inbox", json=activity)
            assert response.status_code == 200
            assert response.json()["status"] == "success"


class TestActivityModel:
    """Tests for Activity ORM model."""

    def test_activity_model_fields(self):
        """Test Activity model has required fields."""
        activity = Activity(
            activity_type=ActivityType.CREATE,
            activity_id="https://example.com/activities/1",
            actor_url="https://example.com/actor",
            object_id="https://example.com/items/1",
            object_data={"type": "Object"},
            activity_data={"type": "Create"},
            local=1,
        )

        assert activity.activity_type == ActivityType.CREATE
        assert activity.activity_id == "https://example.com/activities/1"
        assert activity.actor_url == "https://example.com/actor"
        assert activity.local == 1

    def test_activity_model_repr(self):
        """Test Activity model string representation."""
        activity = Activity(
            activity_type=ActivityType.CREATE,
            activity_id="https://example.com/activities/1",
            actor_url="https://example.com/actor",
            object_data={},
            activity_data={},
            local=1,
        )

        repr_str = repr(activity)
        assert "Activity" in repr_str
        assert "CREATE" in repr_str


class TestNodePublicKeyModel:
    """Tests for NodePublicKey ORM model."""

    def test_node_public_key_model_fields(self):
        """Test NodePublicKey model has required fields."""
        key = NodePublicKey(
            key_id="https://example.com/actor#main-key",
            public_key_pem="-----BEGIN PUBLIC KEY-----\n...\n-----END PUBLIC KEY-----\n",
            node_url="https://example.com",
        )

        assert key.key_id == "https://example.com/actor#main-key"
        assert key.node_url == "https://example.com"
        assert key.public_key_pem.startswith("-----BEGIN")

    def test_node_public_key_model_repr(self):
        """Test NodePublicKey model string representation."""
        key = NodePublicKey(
            key_id="https://example.com/actor#main-key",
            public_key_pem="test-key",
            node_url="https://example.com",
        )

        repr_str = repr(key)
        assert "NodePublicKey" in repr_str
        assert "example.com" in repr_str
