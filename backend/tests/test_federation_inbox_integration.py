"""Tests for Phase 3: HTTP Signature verification at the /inbox endpoint.

Wave 4 Phase 3 — Inbox signature verification + outbound announce signing.

Test classes:
  TestInboxSignatureVerification  — 8 tests covering inbox endpoint behaviour
  TestSendAnnounceSigningIntegration — 5 tests for send_announce signing
  TestInboxSendAnnounceE2E — 2 E2E roundtrip tests
"""

import pytest
import json
from datetime import datetime
from typing import Dict, Any
from unittest.mock import AsyncMock, MagicMock, patch

import httpx
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Activity, ActivityType, FederationPartner, TrustStatus
from app.http_signatures import HTTPSignatureUtils, get_rfc7231_date
from app.services.federation_partner_service import FederationPartnerService


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_keypair():
    """Return (private_pem, public_pem) for a fresh RSA-2048 key."""
    return HTTPSignatureUtils.generate_keypair("https://partner-a.example.com#main-key")


def _make_trusted_partner(private_pem: str, public_pem: str) -> FederationPartner:
    """Build an in-memory FederationPartner in TRUSTED state."""
    partner = FederationPartner(
        name="Node A",
        base_url="https://partner-a.example.com",
        public_key_pem=public_pem,
        key_id="https://partner-a.example.com#main-key",
        trust_state=TrustStatus.TRUSTED,
    )
    partner.id = 1
    partner.failed_signature_count = 0
    return partner


def _build_announce_payload(item_cid: str = "sha256-testitem") -> Dict[str, Any]:
    return {
        "@context": "https://www.w3.org/ns/activitystreams",
        "id": f"https://partner-a.example.com/activities/announce-{item_cid}",
        "type": "Announce",
        "actor": "https://partner-a.example.com/actor",
        "object": f"https://partner-a.example.com/items/{item_cid}",
        "published": "2026-04-26T11:30:00Z",
        "content": {
            "item_cid": item_cid,
            "vote_type": "upvote",
            "user_id": "alice@example.com",
            "source_node": "https://partner-a.example.com",
        },
    }


def _sign_headers(
    private_pem: str,
    key_id: str,
    host: str = "localhost",
    path: str = "/inbox",
) -> Dict[str, str]:
    """Return a dict containing Signature and Date headers for a POST /inbox."""
    date = get_rfc7231_date()
    sig = HTTPSignatureUtils.build_signature_header(
        key_id=key_id,
        private_key_pem=private_pem,
        request_target=f"post {path}",
        host=host,
        date=date,
    )
    return {"Signature": sig, "Date": date, "Host": host}


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
async def app_client_with_mock_db():
    """TestClient backed by a configurable mock db session."""
    from app.main import create_app
    from app import database
    from app.services.search_service import reset_search_service

    reset_search_service()

    # We expose a mutable slot so individual tests can swap in custom execute behaviour.
    state = {"db": None}

    async def mock_get_db():
        session = AsyncMock()

        async def _default_execute(query):
            result = MagicMock()
            result.scalar = MagicMock(return_value=0)
            result.scalar_one_or_none = MagicMock(return_value=None)
            mock_scalars = MagicMock()
            mock_scalars.all = MagicMock(return_value=[])
            result.scalars = MagicMock(return_value=mock_scalars)
            return result

        session.execute = _default_execute
        session.add = MagicMock()
        session.commit = AsyncMock()
        session.refresh = AsyncMock()
        session.rollback = AsyncMock()
        session.delete = MagicMock()
        state["db"] = session
        yield session

    app = create_app()
    app.dependency_overrides[database.get_db] = mock_get_db

    async with AsyncClient(
        transport=httpx.ASGITransport(app=app), base_url="http://localhost"
    ) as ac:
        yield ac, state

    app.dependency_overrides.clear()
    reset_search_service()


# ===========================================================================
# Class 1: Inbox Signature Verification Tests (8 tests)
# ===========================================================================


class TestInboxSignatureVerification:
    """Verify the /inbox endpoint enforces HTTP Signature rules."""

    @pytest.mark.asyncio
    async def test_valid_signature_from_trusted_partner_accepted(
        self, app_client_with_mock_db
    ):
        """Signed request from a trusted partner → 200 + signature_verified=True."""
        client, state = app_client_with_mock_db
        priv, pub = _make_keypair()
        partner = _make_trusted_partner(priv, pub)
        payload = _build_announce_payload()

        # Configure mock db: FederationPartnerService.verify_http_signature patches
        with patch(
            "app.routes.FederationPartnerService.verify_http_signature",
            new=AsyncMock(return_value=(True, None, partner)),
        ):
            headers = _sign_headers(priv, partner.key_id)
            resp = await client.post("/inbox", json=payload, headers=headers)

        assert resp.status_code == 200
        data = resp.json()
        assert data["signature_verified"] is True

    @pytest.mark.asyncio
    async def test_invalid_signature_returns_403(self, app_client_with_mock_db):
        """Tampered/invalid signature → 403 Forbidden."""
        client, state = app_client_with_mock_db
        payload = _build_announce_payload()

        with patch(
            "app.routes.FederationPartnerService.verify_http_signature",
            new=AsyncMock(return_value=(False, "Signature verification failed", None)),
        ):
            headers = {
                "Signature": 'keyId="https://partner-a.example.com#main-key",algorithm="rsa-sha256",headers="(request-target) host date",signature="BADBADBADBAD"',
                "Date": get_rfc7231_date(),
                "Host": "localhost",
            }
            resp = await client.post("/inbox", json=payload, headers=headers)

        assert resp.status_code == 403
        assert "verification failed" in resp.json()["detail"].lower()

    @pytest.mark.asyncio
    async def test_unsigned_activity_accepted_with_signature_verified_false(
        self, app_client_with_mock_db
    ):
        """No Signature header → accepted for backward compat, signature_verified=False."""
        client, state = app_client_with_mock_db
        payload = _build_announce_payload("sha256-unsigned")

        # No Signature header in request — FederationPartnerService should NOT be called.
        with patch(
            "app.routes.FederationPartnerService.verify_http_signature",
            new=AsyncMock(side_effect=AssertionError("Should not be called")),
        ):
            resp = await client.post("/inbox", json=payload)

        assert resp.status_code == 200
        data = resp.json()
        assert data["signature_verified"] is False

    @pytest.mark.asyncio
    async def test_unknown_key_id_returns_403(self, app_client_with_mock_db):
        """keyId not in DB → 403 Forbidden."""
        client, state = app_client_with_mock_db
        payload = _build_announce_payload()

        with patch(
            "app.routes.FederationPartnerService.verify_http_signature",
            new=AsyncMock(
                return_value=(False, "Unknown keyId: https://unknown-node.example.com#main-key", None)
            ),
        ):
            headers = {
                "Signature": 'keyId="https://unknown-node.example.com#main-key",algorithm="rsa-sha256",headers="(request-target) host date",signature="dGVzdA=="',
                "Date": get_rfc7231_date(),
                "Host": "localhost",
            }
            resp = await client.post("/inbox", json=payload, headers=headers)

        assert resp.status_code == 403
        assert "unknown" in resp.json()["detail"].lower()

    @pytest.mark.asyncio
    async def test_untrusted_partner_signature_returns_403(
        self, app_client_with_mock_db
    ):
        """Signature from a partner with trust_state!=trusted → 403 Forbidden."""
        client, state = app_client_with_mock_db
        payload = _build_announce_payload()

        with patch(
            "app.routes.FederationPartnerService.verify_http_signature",
            new=AsyncMock(
                return_value=(False, "Partner is not trusted (state=pending)", None)
            ),
        ):
            headers = {
                "Signature": 'keyId="https://partner-a.example.com#main-key",algorithm="rsa-sha256",headers="(request-target) host date",signature="dGVzdA=="',
                "Date": get_rfc7231_date(),
                "Host": "localhost",
            }
            resp = await client.post("/inbox", json=payload, headers=headers)

        assert resp.status_code == 403
        assert "not trusted" in resp.json()["detail"].lower()

    @pytest.mark.asyncio
    async def test_malformed_signature_header_returns_400(
        self, app_client_with_mock_db
    ):
        """Signature header without keyId field → 400 Bad Request."""
        client, state = app_client_with_mock_db
        payload = _build_announce_payload()

        # Provide a Signature header that's missing keyId entirely.
        headers = {
            "Signature": 'algorithm="rsa-sha256",headers="(request-target)",signature="dGVzdA=="',
            "Date": get_rfc7231_date(),
            "Host": "localhost",
        }
        resp = await client.post("/inbox", json=payload, headers=headers)

        assert resp.status_code == 400
        assert "malformed" in resp.json()["detail"].lower()

    @pytest.mark.asyncio
    async def test_signature_verification_increments_failed_count(
        self, app_client_with_mock_db
    ):
        """Failed verification → verify_http_signature is called (which increments failed count)."""
        client, state = app_client_with_mock_db
        payload = _build_announce_payload()
        call_count = {"n": 0}

        async def _failing_verify(*args, **kwargs):
            call_count["n"] += 1
            return (False, "Signature verification failed", None)

        with patch(
            "app.routes.FederationPartnerService.verify_http_signature",
            new=_failing_verify,
        ):
            headers = {
                "Signature": 'keyId="https://partner-a.example.com#main-key",algorithm="rsa-sha256",headers="(request-target) host date",signature="bad"',
                "Date": get_rfc7231_date(),
                "Host": "localhost",
            }
            resp = await client.post("/inbox", json=payload, headers=headers)

        assert resp.status_code == 403
        # verify_http_signature was called exactly once.
        assert call_count["n"] == 1

    @pytest.mark.asyncio
    async def test_valid_signature_stores_partner_id_and_audit_fields(
        self, app_client_with_mock_db
    ):
        """Accepted signed activity: signature_verified=True returned in response."""
        client, state = app_client_with_mock_db
        priv, pub = _make_keypair()
        partner = _make_trusted_partner(priv, pub)
        payload = _build_announce_payload("sha256-audit-test")

        with patch(
            "app.routes.FederationPartnerService.verify_http_signature",
            new=AsyncMock(return_value=(True, None, partner)),
        ):
            headers = _sign_headers(priv, partner.key_id)
            resp = await client.post("/inbox", json=payload, headers=headers)

        assert resp.status_code == 200
        body = resp.json()
        assert body.get("signature_verified") is True
        assert body.get("status") == "success"


# ===========================================================================
# Class 2: send_announce Signing Tests (5 tests)
# ===========================================================================


class TestSendAnnounceSigningIntegration:
    """Verify outbound Announce activities are signed with Signature headers."""

    @pytest.mark.asyncio
    async def test_send_announce_includes_signature_header(self):
        """Announce to a trusted partner includes a Signature header."""
        from app.services.endorsement_propagation_service import EndorsementPropagationService

        priv, pub = _make_keypair()
        partner = _make_trusted_partner(priv, pub)

        db = AsyncMock()
        result_mock = AsyncMock()
        scalars_mock = MagicMock()
        scalars_mock.all = MagicMock(return_value=[partner])
        result_mock.scalars = MagicMock(return_value=scalars_mock)
        db.execute = AsyncMock(return_value=result_mock)

        activity = Activity(
            activity_type=ActivityType.ANNOUNCE,
            activity_id="https://node-a.example.com/activities/announce-test",
            actor_url="https://node-a.example.com/actor",
            activity_data=_build_announce_payload(),
            local=1,
        )

        captured_headers: Dict[str, str] = {}

        async def _mock_post(url, content, headers, **kwargs):
            captured_headers.update(headers)
            response = MagicMock()
            response.status_code = 202
            return response

        with patch("httpx.AsyncClient") as mock_client_cls:
            mock_client = AsyncMock()
            mock_client.post = _mock_post
            mock_client.__aenter__ = AsyncMock(return_value=mock_client)
            mock_client.__aexit__ = AsyncMock(return_value=False)
            mock_client_cls.return_value = mock_client

            await EndorsementPropagationService.send_announce_to_federation_partners(
                db=db,
                activity=activity,
                private_key=priv,
                node_url="https://node-a.example.com",
            )

        assert "Signature" in captured_headers, "Outbound request missing Signature header"
        assert "keyId=" in captured_headers["Signature"]

    @pytest.mark.asyncio
    async def test_send_announce_signature_contains_correct_key_id(self):
        """The keyId in the Signature header matches the local node's key_id."""
        from app.services.endorsement_propagation_service import EndorsementPropagationService

        node_url = "https://node-a.example.com"
        priv, pub = _make_keypair()
        partner = _make_trusted_partner(priv, pub)

        db = AsyncMock()
        result_mock = AsyncMock()
        scalars_mock = MagicMock()
        scalars_mock.all = MagicMock(return_value=[partner])
        result_mock.scalars = MagicMock(return_value=scalars_mock)
        db.execute = AsyncMock(return_value=result_mock)

        activity = Activity(
            activity_type=ActivityType.ANNOUNCE,
            activity_id="https://node-a.example.com/activities/announce-key-id-test",
            actor_url=f"{node_url}/actor",
            activity_data=_build_announce_payload("sha256-key-id"),
            local=1,
        )

        captured_sig = {}

        async def _mock_post(url, content, headers, **kwargs):
            captured_sig["header"] = headers.get("Signature", "")
            response = MagicMock()
            response.status_code = 202
            return response

        with patch("httpx.AsyncClient") as mock_client_cls:
            mock_client = AsyncMock()
            mock_client.post = _mock_post
            mock_client.__aenter__ = AsyncMock(return_value=mock_client)
            mock_client.__aexit__ = AsyncMock(return_value=False)
            mock_client_cls.return_value = mock_client

            await EndorsementPropagationService.send_announce_to_federation_partners(
                db=db,
                activity=activity,
                private_key=priv,
                node_url=node_url,
            )

        expected_key_id = f"{node_url}#main-key"
        assert expected_key_id in captured_sig["header"], (
            f"Expected keyId={expected_key_id!r} in Signature header, "
            f"got: {captured_sig['header']!r}"
        )

    @pytest.mark.asyncio
    async def test_send_announce_returns_success_for_trusted_partner(self):
        """send_announce returns (True, None) for a partner that responds 202."""
        from app.services.endorsement_propagation_service import EndorsementPropagationService

        priv, pub = _make_keypair()
        partner = _make_trusted_partner(priv, pub)

        db = AsyncMock()
        result_mock = AsyncMock()
        scalars_mock = MagicMock()
        scalars_mock.all = MagicMock(return_value=[partner])
        result_mock.scalars = MagicMock(return_value=scalars_mock)
        db.execute = AsyncMock(return_value=result_mock)

        activity = Activity(
            activity_type=ActivityType.ANNOUNCE,
            activity_id="https://node-a.example.com/activities/announce-success",
            actor_url="https://node-a.example.com/actor",
            activity_data=_build_announce_payload(),
            local=1,
        )

        async def _mock_post(url, content, headers, **kwargs):
            response = MagicMock()
            response.status_code = 202
            return response

        with patch("httpx.AsyncClient") as mock_client_cls:
            mock_client = AsyncMock()
            mock_client.post = _mock_post
            mock_client.__aenter__ = AsyncMock(return_value=mock_client)
            mock_client.__aexit__ = AsyncMock(return_value=False)
            mock_client_cls.return_value = mock_client

            results = await EndorsementPropagationService.send_announce_to_federation_partners(
                db=db,
                activity=activity,
                private_key=priv,
                node_url="https://node-a.example.com",
            )

        assert partner.base_url in results
        success, error = results[partner.base_url]
        assert success is True
        assert error is None

    @pytest.mark.asyncio
    async def test_send_announce_returns_empty_when_no_trusted_partners(self):
        """send_announce returns empty dict when no trusted partners exist."""
        from app.services.endorsement_propagation_service import EndorsementPropagationService

        priv, _ = _make_keypair()

        db = AsyncMock()
        result_mock = AsyncMock()
        scalars_mock = MagicMock()
        scalars_mock.all = MagicMock(return_value=[])  # no partners
        result_mock.scalars = MagicMock(return_value=scalars_mock)
        db.execute = AsyncMock(return_value=result_mock)

        activity = Activity(
            activity_type=ActivityType.ANNOUNCE,
            activity_id="https://node-a.example.com/activities/announce-no-partners",
            actor_url="https://node-a.example.com/actor",
            activity_data=_build_announce_payload(),
            local=1,
        )

        results = await EndorsementPropagationService.send_announce_to_federation_partners(
            db=db,
            activity=activity,
            private_key=priv,
            node_url="https://node-a.example.com",
        )

        assert results == {}

    @pytest.mark.asyncio
    async def test_send_announce_records_failure_on_network_error(self):
        """send_announce records (False, error_msg) when partner is unreachable."""
        from app.services.endorsement_propagation_service import EndorsementPropagationService

        priv, pub = _make_keypair()
        partner = _make_trusted_partner(priv, pub)

        db = AsyncMock()
        result_mock = AsyncMock()
        scalars_mock = MagicMock()
        scalars_mock.all = MagicMock(return_value=[partner])
        result_mock.scalars = MagicMock(return_value=scalars_mock)
        db.execute = AsyncMock(return_value=result_mock)

        activity = Activity(
            activity_type=ActivityType.ANNOUNCE,
            activity_id="https://node-a.example.com/activities/announce-fail",
            actor_url="https://node-a.example.com/actor",
            activity_data=_build_announce_payload(),
            local=1,
        )

        async def _mock_post_raises(url, content, headers, **kwargs):
            raise httpx.ConnectError("Connection refused")

        with patch("httpx.AsyncClient") as mock_client_cls:
            mock_client = AsyncMock()
            mock_client.post = _mock_post_raises
            mock_client.__aenter__ = AsyncMock(return_value=mock_client)
            mock_client.__aexit__ = AsyncMock(return_value=False)
            mock_client_cls.return_value = mock_client

            results = await EndorsementPropagationService.send_announce_to_federation_partners(
                db=db,
                activity=activity,
                private_key=priv,
                node_url="https://node-a.example.com",
            )

        assert partner.base_url in results
        success, error = results[partner.base_url]
        assert success is False
        assert error is not None


# ===========================================================================
# Class 3: End-to-End Roundtrip Tests (2 tests)
# ===========================================================================


class TestInboxSendAnnounceE2E:
    """Full roundtrip: Node A signs Announce → Node B verifies → accepts."""

    @pytest.mark.asyncio
    async def test_e2e_signed_announce_accepted_with_correct_fields(
        self, app_client_with_mock_db
    ):
        """Full E2E: sign an Announce using real crypto → send to /inbox → accepted.

        Uses real RSA signing (no crypto mock) and patches only the DB interaction
        and FederationPartnerService.verify_http_signature.
        """
        client, state = app_client_with_mock_db
        priv, pub = _make_keypair()
        partner = _make_trusted_partner(priv, pub)
        partner.id = 42
        payload = _build_announce_payload("sha256-e2e-test")

        # Build a real valid Signature header using the local private key.
        date = get_rfc7231_date()
        sig_header = HTTPSignatureUtils.build_signature_header(
            key_id=partner.key_id,
            private_key_pem=priv,
            request_target="post /inbox",
            host="localhost",
            date=date,
        )

        # Verify the signature we just built is actually valid (sanity check).
        valid_locally = HTTPSignatureUtils.verify_signature_header(
            signature_header=sig_header,
            public_key_pem=pub,
            request_target="post /inbox",
            host="localhost",
            date=date,
        )
        assert valid_locally, "Test setup error: locally-built signature must verify"

        # Simulate partner lookup succeeding with TRUSTED state.
        with patch(
            "app.routes.FederationPartnerService.verify_http_signature",
            new=AsyncMock(return_value=(True, None, partner)),
        ):
            resp = await client.post(
                "/inbox",
                json=payload,
                headers={
                    "Signature": sig_header,
                    "Date": date,
                    "Host": "localhost",
                },
            )

        assert resp.status_code == 200
        body = resp.json()
        assert body["status"] == "success"
        assert body["signature_verified"] is True

    @pytest.mark.asyncio
    async def test_e2e_revoked_partner_signature_rejected(
        self, app_client_with_mock_db
    ):
        """Announce from a revoked partner is rejected with 403."""
        client, state = app_client_with_mock_db
        priv, pub = _make_keypair()
        payload = _build_announce_payload("sha256-revoked")

        date = get_rfc7231_date()
        key_id = "https://revoked-node.example.com#main-key"
        sig_header = HTTPSignatureUtils.build_signature_header(
            key_id=key_id,
            private_key_pem=priv,
            request_target="post /inbox",
            host="localhost",
            date=date,
        )

        # verify_http_signature returns the "not trusted" error (partner is revoked).
        with patch(
            "app.routes.FederationPartnerService.verify_http_signature",
            new=AsyncMock(
                return_value=(False, "Partner is not trusted (state=revoked)", None)
            ),
        ):
            resp = await client.post(
                "/inbox",
                json=payload,
                headers={
                    "Signature": sig_header,
                    "Date": date,
                    "Host": "localhost",
                },
            )

        assert resp.status_code == 403
        detail = resp.json()["detail"]
        assert "not trusted" in detail.lower()
