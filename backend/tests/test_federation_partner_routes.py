"""Tests for Wave 4 Phase 2: Federation Partner Service + Admin Routes.

Covers:
- Service layer unit tests (register, get, list, trust-state transitions,
  key rotation, signature verification, activity log, delete)
- Admin route tests (all 7 endpoints: register, list, get, trust-state,
  rotate-key, activity-log, delete)
- Integration tests (cross-endpoint flows, state machine paths)

Target: 14 passing tests, zero regressions on existing 125 tests.
"""

import pytest
from datetime import datetime, timedelta
from unittest.mock import AsyncMock, MagicMock, patch, call
from typing import List, Optional

from httpx import AsyncClient
import httpx

from app.models import FederationPartner, TrustStatus, Activity, ActivityType
from app.services.federation_partner_service import (
    FederationPartnerService,
    _parse_signature_field,
    _FAILURE_THRESHOLD,
)
from app.http_signatures import HTTPSignatureUtils


# ---------------------------------------------------------------------------
# Shared fixtures and helpers
# ---------------------------------------------------------------------------


def _make_partner(
    partner_id: int = 1,
    name: str = "Node B",
    base_url: str = "https://node-b.example.com",
    trust_state: TrustStatus = TrustStatus.PENDING,
    failed_signature_count: int = 0,
    last_activity_at: Optional[datetime] = None,
    public_key_pem: Optional[str] = None,
    key_id: str = "https://node-b.example.com#main-key",
) -> FederationPartner:
    """Build a FederationPartner instance for testing (no DB required)."""
    if public_key_pem is None:
        # Generate a real RSA keypair so signature tests work.
        _, public_key_pem = HTTPSignatureUtils.generate_keypair(key_id)

    partner = FederationPartner(
        name=name,
        base_url=base_url,
        public_key_pem=public_key_pem,
        key_id=key_id,
        trust_state=trust_state,
        failed_signature_count=failed_signature_count,
        last_activity_at=last_activity_at,
        created_at=datetime(2026, 4, 26, 10, 0, 0),
        updated_at=datetime(2026, 4, 26, 10, 0, 0),
    )
    partner.id = partner_id
    return partner


def _mock_db_with_partner(partner: FederationPartner) -> AsyncMock:
    """Return a minimal AsyncSession mock pre-loaded with a single partner."""
    db = AsyncMock()

    result_mock = MagicMock()
    result_mock.scalar_one_or_none = MagicMock(return_value=partner)
    scalars_mock = MagicMock()
    scalars_mock.all = MagicMock(return_value=[partner])
    result_mock.scalars = MagicMock(return_value=scalars_mock)

    db.execute = AsyncMock(return_value=result_mock)
    db.add = MagicMock()
    db.commit = AsyncMock()
    db.refresh = AsyncMock()
    db.delete = AsyncMock()
    return db


# ---------------------------------------------------------------------------
# Class 1: Service — Registration
# ---------------------------------------------------------------------------


class TestFederationPartnerServiceRegistration:
    """Unit tests for FederationPartnerService.register_partner."""

    @pytest.mark.asyncio
    async def test_register_partner_success(self):
        """register_partner creates a FederationPartner with PENDING state."""
        _, pub_pem = HTTPSignatureUtils.generate_keypair("https://node-b.example.com#main-key")

        db = AsyncMock()
        db.add = MagicMock()
        db.commit = AsyncMock()
        db.refresh = AsyncMock(side_effect=lambda obj: None)

        partner = await FederationPartnerService.register_partner(
            db=db,
            name="Node B",
            base_url="https://node-b.example.com",
            public_key_pem=pub_pem,
            key_id="https://node-b.example.com#main-key",
        )

        db.add.assert_called_once()
        db.commit.assert_awaited_once()
        # The partner object passed to db.add should have PENDING trust state.
        added_partner = db.add.call_args[0][0]
        assert added_partner.trust_state == TrustStatus.PENDING
        assert added_partner.name == "Node B"
        assert added_partner.base_url == "https://node-b.example.com"

    @pytest.mark.asyncio
    async def test_register_partner_invalid_pem_raises_value_error(self):
        """register_partner raises ValueError for a malformed public key PEM."""
        db = AsyncMock()

        with pytest.raises(ValueError, match="Invalid public key PEM"):
            await FederationPartnerService.register_partner(
                db=db,
                name="Bad Key Node",
                base_url="https://bad.example.com",
                public_key_pem="-----BEGIN PUBLIC KEY-----\nNOT_VALID\n-----END PUBLIC KEY-----",
                key_id="https://bad.example.com#main-key",
            )

        # DB should not have been touched.
        db.add.assert_not_called()

    @pytest.mark.asyncio
    async def test_register_partner_integrity_error_propagates(self):
        """register_partner propagates IntegrityError for duplicate keys."""
        from sqlalchemy.exc import IntegrityError

        _, pub_pem = HTTPSignatureUtils.generate_keypair("https://node-b.example.com#main-key")

        db = AsyncMock()
        db.add = MagicMock()
        db.commit = AsyncMock(side_effect=IntegrityError("unique", {}, None))
        db.rollback = AsyncMock()

        with pytest.raises(IntegrityError):
            await FederationPartnerService.register_partner(
                db=db,
                name="Node B",
                base_url="https://node-b.example.com",
                public_key_pem=pub_pem,
                key_id="https://node-b.example.com#main-key",
            )

        db.rollback.assert_awaited_once()


# ---------------------------------------------------------------------------
# Class 2: Service — Trust State Machine
# ---------------------------------------------------------------------------


class TestFederationPartnerTrustStateMachine:
    """Unit tests for FederationPartnerService.update_partner_trust_state."""

    @pytest.mark.asyncio
    async def test_pending_to_trusted_is_valid(self):
        """pending → trusted is a valid transition."""
        partner = _make_partner(trust_state=TrustStatus.PENDING)
        db = _mock_db_with_partner(partner)

        updated = await FederationPartnerService.update_partner_trust_state(
            db=db, partner_id=1, new_state="trusted"
        )
        assert updated.trust_state == TrustStatus.TRUSTED

    @pytest.mark.asyncio
    async def test_pending_to_revoked_is_valid(self):
        """pending → revoked is a valid transition (admin can immediately revoke)."""
        partner = _make_partner(trust_state=TrustStatus.PENDING)
        db = _mock_db_with_partner(partner)

        updated = await FederationPartnerService.update_partner_trust_state(
            db=db, partner_id=1, new_state="revoked"
        )
        assert updated.trust_state == TrustStatus.REVOKED

    @pytest.mark.asyncio
    async def test_revoked_to_trusted_is_invalid(self):
        """revoked → trusted is an invalid transition (revoked is terminal)."""
        partner = _make_partner(trust_state=TrustStatus.REVOKED)
        db = _mock_db_with_partner(partner)

        with pytest.raises(ValueError, match="Invalid state transition"):
            await FederationPartnerService.update_partner_trust_state(
                db=db, partner_id=1, new_state="trusted"
            )

    @pytest.mark.asyncio
    async def test_update_trust_state_partner_not_found_raises_key_error(self):
        """update_partner_trust_state raises KeyError for unknown partner_id."""
        db = AsyncMock()
        result_mock = MagicMock()
        result_mock.scalar_one_or_none = MagicMock(return_value=None)
        db.execute = AsyncMock(return_value=result_mock)

        with pytest.raises(KeyError, match="not found"):
            await FederationPartnerService.update_partner_trust_state(
                db=db, partner_id=999, new_state="trusted"
            )

    @pytest.mark.asyncio
    async def test_invalid_state_value_raises_value_error(self):
        """Passing an unrecognised state string raises ValueError."""
        partner = _make_partner(trust_state=TrustStatus.PENDING)
        db = _mock_db_with_partner(partner)

        with pytest.raises(ValueError, match="Invalid trust state"):
            await FederationPartnerService.update_partner_trust_state(
                db=db, partner_id=1, new_state="superTrusted"
            )


# ---------------------------------------------------------------------------
# Class 3: Service — HTTP Signature Verification
# ---------------------------------------------------------------------------


class TestHTTPSignatureVerification:
    """Unit tests for FederationPartnerService.verify_http_signature."""

    def _build_valid_signature(
        self,
        private_key_pem: str,
        key_id: str,
        request_target: str = "post /inbox",
        host: str = "node-b.example.com",
        date: str = "Sat, 26 Apr 2026 11:30:00 GMT",
    ) -> str:
        """Build a valid Signature header for the given private key."""
        return HTTPSignatureUtils.build_signature_header(
            key_id=key_id,
            private_key_pem=private_key_pem,
            request_target=request_target,
            host=host,
            date=date,
        )

    @pytest.mark.asyncio
    async def test_verify_valid_signature_returns_true(self):
        """A correctly signed request from a TRUSTED partner verifies successfully."""
        private_pem, public_pem = HTTPSignatureUtils.generate_keypair(
            "https://node-a.example.com#main-key"
        )
        key_id = "https://node-a.example.com#main-key"
        partner = _make_partner(
            trust_state=TrustStatus.TRUSTED,
            public_key_pem=public_pem,
            key_id=key_id,
        )
        db = _mock_db_with_partner(partner)

        sig_header = self._build_valid_signature(private_pem, key_id)
        valid, error, returned_partner = await FederationPartnerService.verify_http_signature(
            db=db,
            signature_header=sig_header,
            request_target="post /inbox",
            host="node-b.example.com",
            date="Sat, 26 Apr 2026 11:30:00 GMT",
        )

        assert valid is True
        assert error is None
        assert returned_partner is not None

    @pytest.mark.asyncio
    async def test_verify_invalid_signature_returns_false(self):
        """A tampered signature from a TRUSTED partner is rejected."""
        _, public_pem = HTTPSignatureUtils.generate_keypair(
            "https://node-a.example.com#main-key"
        )
        key_id = "https://node-a.example.com#main-key"
        partner = _make_partner(
            trust_state=TrustStatus.TRUSTED,
            public_key_pem=public_pem,
            key_id=key_id,
        )
        db = _mock_db_with_partner(partner)

        tampered_sig = (
            f'keyId="{key_id}",'
            'algorithm="rsa-sha256",'
            'headers="(request-target) host date",'
            'signature="dGhpcyBpcyBub3QgYSByZWFsIHNpZ25hdHVyZQ=="'
        )

        valid, error, returned_partner = await FederationPartnerService.verify_http_signature(
            db=db,
            signature_header=tampered_sig,
            request_target="post /inbox",
            host="node-b.example.com",
            date="Sat, 26 Apr 2026 11:30:00 GMT",
        )

        assert valid is False
        assert error is not None
        assert returned_partner is None

    @pytest.mark.asyncio
    async def test_missing_signature_header_returns_false(self):
        """An empty Signature header is rejected immediately."""
        db = AsyncMock()

        valid, error, partner = await FederationPartnerService.verify_http_signature(
            db=db,
            signature_header="",
            request_target="post /inbox",
            host="node-b.example.com",
            date="Sat, 26 Apr 2026 11:30:00 GMT",
        )

        assert valid is False
        assert "Missing" in error
        assert partner is None

    @pytest.mark.asyncio
    async def test_unknown_key_id_returns_false(self):
        """A Signature header with an unknown keyId is rejected."""
        db = AsyncMock()
        result_mock = MagicMock()
        result_mock.scalar_one_or_none = MagicMock(return_value=None)
        db.execute = AsyncMock(return_value=result_mock)

        sig_header = (
            'keyId="https://unknown.example.com#main-key",'
            'algorithm="rsa-sha256",'
            'headers="(request-target) host date",'
            'signature="abc123"'
        )

        valid, error, partner = await FederationPartnerService.verify_http_signature(
            db=db,
            signature_header=sig_header,
            request_target="post /inbox",
            host="node-b.example.com",
            date="Sat, 26 Apr 2026 11:30:00 GMT",
        )

        assert valid is False
        assert "Unknown keyId" in error
        assert partner is None

    @pytest.mark.asyncio
    async def test_untrusted_partner_signature_is_rejected(self):
        """A signature from an UNTRUSTED partner is rejected even if cryptographically valid."""
        private_pem, public_pem = HTTPSignatureUtils.generate_keypair(
            "https://untrusted.example.com#main-key"
        )
        key_id = "https://untrusted.example.com#main-key"
        partner = _make_partner(
            trust_state=TrustStatus.UNTRUSTED,
            public_key_pem=public_pem,
            key_id=key_id,
        )
        db = _mock_db_with_partner(partner)

        sig_header = self._build_valid_signature(private_pem, key_id)
        valid, error, returned_partner = await FederationPartnerService.verify_http_signature(
            db=db,
            signature_header=sig_header,
            request_target="post /inbox",
            host="node-b.example.com",
            date="Sat, 26 Apr 2026 11:30:00 GMT",
        )

        assert valid is False
        assert "not trusted" in error.lower()
        assert returned_partner is None

    @pytest.mark.asyncio
    async def test_auto_downgrade_after_repeated_failures(self):
        """Partner is auto-downgraded to UNTRUSTED after exceeding the failure threshold."""
        _, public_pem = HTTPSignatureUtils.generate_keypair(
            "https://node-a.example.com#main-key"
        )
        key_id = "https://node-a.example.com#main-key"
        # Start with failure count already at threshold.
        partner = _make_partner(
            trust_state=TrustStatus.TRUSTED,
            public_key_pem=public_pem,
            key_id=key_id,
            failed_signature_count=_FAILURE_THRESHOLD,
        )
        db = _mock_db_with_partner(partner)

        tampered_sig = (
            f'keyId="{key_id}",'
            'algorithm="rsa-sha256",'
            'headers="(request-target) host date",'
            'signature="dGhpcyBpcyBub3QgYSByZWFsIHNpZ25hdHVyZQ=="'
        )

        valid, _, _ = await FederationPartnerService.verify_http_signature(
            db=db,
            signature_header=tampered_sig,
            request_target="post /inbox",
            host="node-b.example.com",
            date="Sat, 26 Apr 2026 11:30:00 GMT",
        )

        assert valid is False
        # Partner should now be UNTRUSTED.
        assert partner.trust_state == TrustStatus.UNTRUSTED


# ---------------------------------------------------------------------------
# Class 4: Service — Key Rotation & Delete
# ---------------------------------------------------------------------------


class TestKeyRotationAndDelete:
    """Unit tests for key rotation and partner deletion."""

    @pytest.mark.asyncio
    async def test_rotate_key_updates_pem_and_key_id(self):
        """rotate_partner_public_key persists new PEM and key_id."""
        _, new_pub_pem = HTTPSignatureUtils.generate_keypair(
            "https://node-b.example.com#main-key-v2"
        )
        partner = _make_partner(trust_state=TrustStatus.TRUSTED)
        db = _mock_db_with_partner(partner)

        updated = await FederationPartnerService.rotate_partner_public_key(
            db=db,
            partner_id=1,
            new_key_pem=new_pub_pem,
            new_key_id="https://node-b.example.com#main-key-v2",
        )

        assert updated.public_key_pem == new_pub_pem
        assert updated.key_id == "https://node-b.example.com#main-key-v2"
        assert updated.last_key_refresh_at is not None

    @pytest.mark.asyncio
    async def test_rotate_key_invalid_pem_raises_value_error(self):
        """rotate_partner_public_key raises ValueError for a bad PEM."""
        partner = _make_partner(trust_state=TrustStatus.TRUSTED)
        db = _mock_db_with_partner(partner)

        with pytest.raises(ValueError, match="Invalid public key PEM"):
            await FederationPartnerService.rotate_partner_public_key(
                db=db,
                partner_id=1,
                new_key_pem="-----BEGIN PUBLIC KEY-----\nBAD\n-----END PUBLIC KEY-----",
                new_key_id="https://node-b.example.com#main-key-v2",
            )

    @pytest.mark.asyncio
    async def test_delete_revoked_inactive_partner_succeeds(self):
        """delete_partner succeeds for a REVOKED partner with no recent activity."""
        old_activity = datetime.utcnow() - timedelta(days=60)
        partner = _make_partner(
            trust_state=TrustStatus.REVOKED,
            last_activity_at=old_activity,
        )
        db = _mock_db_with_partner(partner)

        await FederationPartnerService.delete_partner(db=db, partner_id=1)
        db.delete.assert_awaited_once_with(partner)

    @pytest.mark.asyncio
    async def test_delete_non_revoked_partner_raises_value_error(self):
        """delete_partner refuses to delete a TRUSTED partner."""
        partner = _make_partner(trust_state=TrustStatus.TRUSTED)
        db = _mock_db_with_partner(partner)

        with pytest.raises(ValueError, match="must be REVOKED"):
            await FederationPartnerService.delete_partner(db=db, partner_id=1)

    @pytest.mark.asyncio
    async def test_delete_recently_active_partner_raises_value_error(self):
        """delete_partner refuses to delete a REVOKED partner with recent activity."""
        recent_activity = datetime.utcnow() - timedelta(days=5)
        partner = _make_partner(
            trust_state=TrustStatus.REVOKED,
            last_activity_at=recent_activity,
        )
        db = _mock_db_with_partner(partner)

        with pytest.raises(ValueError, match="activity in the last"):
            await FederationPartnerService.delete_partner(db=db, partner_id=1)


# ---------------------------------------------------------------------------
# Class 5: Admin Route Tests
# ---------------------------------------------------------------------------


@pytest.fixture
async def admin_client():
    """Create a test client with the federation admin router mounted."""
    from app.main import create_app
    from app import database
    from app.services.search_service import reset_search_service

    reset_search_service()

    async def mock_get_db():
        session = AsyncMock()
        result_mock = MagicMock()
        result_mock.scalar_one_or_none = MagicMock(return_value=None)
        scalars_mock = MagicMock()
        scalars_mock.all = MagicMock(return_value=[])
        result_mock.scalars = MagicMock(return_value=scalars_mock)
        session.execute = AsyncMock(return_value=result_mock)
        session.add = MagicMock()
        session.commit = AsyncMock()
        session.refresh = AsyncMock()
        session.delete = AsyncMock()
        session.rollback = AsyncMock()
        yield session

    app = create_app()
    app.dependency_overrides[database.get_db] = mock_get_db

    async with AsyncClient(
        transport=httpx.ASGITransport(app=app), base_url="http://test"
    ) as ac:
        yield ac

    app.dependency_overrides.clear()
    reset_search_service()


class TestFederationPartnerAdminRoutes:
    """Integration tests for the admin federation-partners endpoints."""

    @pytest.mark.asyncio
    async def test_register_partner_endpoint_returns_201(self, admin_client: AsyncClient):
        """POST /register returns 201 with valid input."""
        _, pub_pem = HTTPSignatureUtils.generate_keypair("https://node-b.example.com#main-key")

        with patch(
            "app.api.v1.admin.federation_partners.FederationPartnerService.register_partner",
            new_callable=AsyncMock,
            return_value=_make_partner(public_key_pem=pub_pem),
        ):
            resp = await admin_client.post(
                "/api/v1/admin/federation-partners/register",
                json={
                    "name": "Node B",
                    "base_url": "https://node-b.example.com",
                    "public_key_pem": pub_pem,
                    "key_id": "https://node-b.example.com#main-key",
                },
            )

        assert resp.status_code == 201
        data = resp.json()
        assert data["name"] == "Node B"
        assert data["trust_state"] == "pending"

    @pytest.mark.asyncio
    async def test_register_partner_endpoint_invalid_pem_returns_400(
        self, admin_client: AsyncClient
    ):
        """POST /register with an invalid PEM returns 400."""
        with patch(
            "app.api.v1.admin.federation_partners.FederationPartnerService.register_partner",
            new_callable=AsyncMock,
            side_effect=ValueError("Invalid public key PEM"),
        ):
            resp = await admin_client.post(
                "/api/v1/admin/federation-partners/register",
                json={
                    "name": "Bad Key Node",
                    "base_url": "https://bad.example.com",
                    "public_key_pem": "-----BEGIN PUBLIC KEY-----\nBAD\n-----END PUBLIC KEY-----",
                    "key_id": "https://bad.example.com#main-key",
                },
            )

        assert resp.status_code == 400

    @pytest.mark.asyncio
    async def test_list_partners_endpoint_returns_200(self, admin_client: AsyncClient):
        """GET /api/v1/admin/federation-partners returns 200 with partners list."""
        _, pub_pem = HTTPSignatureUtils.generate_keypair("https://node-b.example.com#main-key")
        partners = [_make_partner(public_key_pem=pub_pem)]

        with patch(
            "app.api.v1.admin.federation_partners.FederationPartnerService.list_partners",
            new_callable=AsyncMock,
            return_value=partners,
        ):
            resp = await admin_client.get("/api/v1/admin/federation-partners")

        assert resp.status_code == 200
        data = resp.json()
        assert data["total"] == 1
        assert len(data["partners"]) == 1

    @pytest.mark.asyncio
    async def test_get_partner_endpoint_returns_200(self, admin_client: AsyncClient):
        """GET /api/v1/admin/federation-partners/{id} returns 200 for known partner."""
        _, pub_pem = HTTPSignatureUtils.generate_keypair("https://node-b.example.com#main-key")
        partner = _make_partner(public_key_pem=pub_pem)

        with patch(
            "app.api.v1.admin.federation_partners.FederationPartnerService.get_partner",
            new_callable=AsyncMock,
            return_value=partner,
        ):
            resp = await admin_client.get("/api/v1/admin/federation-partners/1")

        assert resp.status_code == 200
        data = resp.json()
        assert data["id"] == 1
        assert "public_key_pem" in data  # detail response includes PEM

    @pytest.mark.asyncio
    async def test_get_partner_endpoint_returns_404_for_missing(
        self, admin_client: AsyncClient
    ):
        """GET /api/v1/admin/federation-partners/{id} returns 404 for unknown id."""
        with patch(
            "app.api.v1.admin.federation_partners.FederationPartnerService.get_partner",
            new_callable=AsyncMock,
            side_effect=KeyError("Federation partner 999 not found"),
        ):
            resp = await admin_client.get("/api/v1/admin/federation-partners/999")

        assert resp.status_code == 404

    @pytest.mark.asyncio
    async def test_update_trust_state_endpoint_returns_200(self, admin_client: AsyncClient):
        """PUT /trust-state updates trust state and returns 200."""
        _, pub_pem = HTTPSignatureUtils.generate_keypair("https://node-b.example.com#main-key")
        partner = _make_partner(trust_state=TrustStatus.TRUSTED, public_key_pem=pub_pem)

        with patch(
            "app.api.v1.admin.federation_partners.FederationPartnerService.update_partner_trust_state",
            new_callable=AsyncMock,
            return_value=partner,
        ):
            resp = await admin_client.put(
                "/api/v1/admin/federation-partners/1/trust-state",
                json={"trust_state": "trusted"},
            )

        assert resp.status_code == 200
        data = resp.json()
        assert data["trust_state"] == "trusted"

    @pytest.mark.asyncio
    async def test_rotate_key_endpoint_returns_200(self, admin_client: AsyncClient):
        """POST /rotate-key returns 200 on successful key rotation."""
        _, pub_pem = HTTPSignatureUtils.generate_keypair("https://node-b.example.com#main-key-v2")
        partner = _make_partner(
            trust_state=TrustStatus.TRUSTED,
            public_key_pem=pub_pem,
            key_id="https://node-b.example.com#main-key-v2",
        )

        with patch(
            "app.api.v1.admin.federation_partners.FederationPartnerService.rotate_partner_public_key",
            new_callable=AsyncMock,
            return_value=partner,
        ):
            resp = await admin_client.post(
                "/api/v1/admin/federation-partners/1/rotate-key",
                json={
                    "public_key_pem": pub_pem,
                    "key_id": "https://node-b.example.com#main-key-v2",
                },
            )

        assert resp.status_code == 200
        data = resp.json()
        assert data["key_id"] == "https://node-b.example.com#main-key-v2"

    @pytest.mark.asyncio
    async def test_activity_log_endpoint_returns_200(self, admin_client: AsyncClient):
        """GET /activity-log returns 200 with activities list."""
        with patch(
            "app.api.v1.admin.federation_partners.FederationPartnerService.get_activity_log",
            new_callable=AsyncMock,
            return_value=[],
        ):
            resp = await admin_client.get(
                "/api/v1/admin/federation-partners/1/activity-log"
            )

        assert resp.status_code == 200
        data = resp.json()
        assert data["partner_id"] == 1
        assert data["activities"] == []
        assert data["total"] == 0

    @pytest.mark.asyncio
    async def test_delete_partner_endpoint_returns_204(self, admin_client: AsyncClient):
        """DELETE /api/v1/admin/federation-partners/{id} returns 204 on success."""
        with patch(
            "app.api.v1.admin.federation_partners.FederationPartnerService.delete_partner",
            new_callable=AsyncMock,
            return_value=None,
        ):
            resp = await admin_client.delete("/api/v1/admin/federation-partners/1")

        assert resp.status_code == 204

    @pytest.mark.asyncio
    async def test_delete_non_revoked_partner_returns_400(self, admin_client: AsyncClient):
        """DELETE on a non-REVOKED partner returns 400."""
        with patch(
            "app.api.v1.admin.federation_partners.FederationPartnerService.delete_partner",
            new_callable=AsyncMock,
            side_effect=ValueError("Partner must be REVOKED before deletion"),
        ):
            resp = await admin_client.delete("/api/v1/admin/federation-partners/1")

        assert resp.status_code == 400


# ---------------------------------------------------------------------------
# Class 6: Integration — Cross-endpoint Flows
# ---------------------------------------------------------------------------


class TestFederationPartnerIntegrationFlows:
    """Integration tests spanning multiple service methods in sequence."""

    @pytest.mark.asyncio
    async def test_register_then_approve_partner_flow(self):
        """Service-level: register a partner then approve trust state."""
        _, pub_pem = HTTPSignatureUtils.generate_keypair("https://node-b.example.com#main-key")

        # --- Step 1: register ---
        db = AsyncMock()
        db.add = MagicMock()
        db.commit = AsyncMock()
        db.refresh = AsyncMock(side_effect=lambda obj: None)

        partner_obj = await FederationPartnerService.register_partner(
            db=db,
            name="Node B",
            base_url="https://node-b.example.com",
            public_key_pem=pub_pem,
            key_id="https://node-b.example.com#main-key",
        )

        # Confirm PENDING state after registration.
        added_partner = db.add.call_args[0][0]
        assert added_partner.trust_state == TrustStatus.PENDING

        # --- Step 2: approve (pending → trusted) ---
        # Simulate the partner now being persisted and fetchable.
        added_partner.id = 42
        db2 = _mock_db_with_partner(added_partner)

        trusted_partner = await FederationPartnerService.update_partner_trust_state(
            db=db2, partner_id=42, new_state="trusted"
        )
        assert trusted_partner.trust_state == TrustStatus.TRUSTED

    @pytest.mark.asyncio
    async def test_full_revoke_and_delete_flow(self):
        """Service-level: trust → revoke → delete (with old activity)."""
        _, pub_pem = HTTPSignatureUtils.generate_keypair("https://node-c.example.com#main-key")
        old_activity = datetime.utcnow() - timedelta(days=45)

        partner = _make_partner(
            partner_id=5,
            trust_state=TrustStatus.TRUSTED,
            public_key_pem=pub_pem,
            last_activity_at=old_activity,
        )
        db = _mock_db_with_partner(partner)

        # Step 1: trusted → revoked
        revoked = await FederationPartnerService.update_partner_trust_state(
            db=db, partner_id=5, new_state="revoked"
        )
        assert revoked.trust_state == TrustStatus.REVOKED

        # Step 2: delete (old activity, so allowed)
        # Re-build mock since partner state changed.
        db2 = _mock_db_with_partner(partner)
        await FederationPartnerService.delete_partner(db=db2, partner_id=5)
        db2.delete.assert_awaited_once_with(partner)

    @pytest.mark.asyncio
    async def test_list_partners_filters_by_state(self):
        """list_partners with filter_by_state='trusted' only returns trusted partners."""
        _, pub_pem = HTTPSignatureUtils.generate_keypair("https://node-d.example.com#main-key")
        trusted_partner = _make_partner(
            partner_id=10,
            name="Trusted Node",
            trust_state=TrustStatus.TRUSTED,
            public_key_pem=pub_pem,
        )

        db = AsyncMock()
        result_mock = MagicMock()
        scalars_mock = MagicMock()
        scalars_mock.all = MagicMock(return_value=[trusted_partner])
        result_mock.scalars = MagicMock(return_value=scalars_mock)
        db.execute = AsyncMock(return_value=result_mock)

        partners = await FederationPartnerService.list_partners(
            db=db, filter_by_state="trusted"
        )

        assert len(partners) == 1
        assert partners[0].trust_state == TrustStatus.TRUSTED

    @pytest.mark.asyncio
    async def test_list_partners_invalid_state_filter_raises_value_error(self):
        """list_partners raises ValueError for an unrecognised state filter."""
        db = AsyncMock()

        with pytest.raises(ValueError, match="Invalid filter_by_state"):
            await FederationPartnerService.list_partners(
                db=db, filter_by_state="hyperTrusted"
            )
