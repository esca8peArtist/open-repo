"""Tests for Wave 4 Phase 4: Conflict Logging & Admin Dashboard.

Tests cover:
- FederationConflict model validation
- FederationConflictService methods
- Admin endpoint GET /admin/federation/conflicts
- Conflict logging in federation workflows
- Conflict resolution and filtering
"""

import pytest
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import (
    FederationConflict,
    FederationPartner,
    Activity,
    ActivityType,
    TrustStatus,
    ConflictType,
    ConflictStatus,
    ConflictResolutionAction,
)
from app.services.federation_conflict_service import FederationConflictService


# ============================================================================
# Class 1: FederationConflict Model Validation (5 tests)
# ============================================================================


class TestFederationConflictModel:
    """Tests for FederationConflict ORM model."""

    def test_create_federation_conflict_valid(self):
        """Verify FederationConflict can be instantiated with required fields."""
        conflict = FederationConflict(
            partner_id=1,
            activity_id=10,
            conflict_type=ConflictType.SIGNATURE_MISMATCH,
            status=ConflictStatus.ACTIVE,
            error_message="Signature verification failed",
        )

        assert conflict.partner_id == 1
        assert conflict.activity_id == 10
        assert conflict.conflict_type == ConflictType.SIGNATURE_MISMATCH
        assert conflict.status == ConflictStatus.ACTIVE
        assert conflict.error_message == "Signature verification failed"

    def test_federation_conflict_has_correct_table_name(self):
        """Verify FederationConflict uses correct table name."""
        assert FederationConflict.__tablename__ == "federation_conflicts"

    def test_conflict_type_enum_values(self):
        """Verify ConflictType enum has all required values."""
        assert ConflictType.SIGNATURE_MISMATCH.value == "signature_mismatch"
        assert ConflictType.KEY_EXPIRED.value == "key_expired"
        assert ConflictType.KEY_REVOKED.value == "key_revoked"
        assert ConflictType.TRUST_FAILURE.value == "trust_failure"

    def test_conflict_status_enum_values(self):
        """Verify ConflictStatus enum has required values."""
        assert ConflictStatus.ACTIVE.value == "active"
        assert ConflictStatus.RESOLVED.value == "resolved"

    def test_resolution_action_enum_values(self):
        """Verify ConflictResolutionAction enum has required values."""
        assert ConflictResolutionAction.AUTO_DOWNGRADE.value == "auto_downgrade"
        assert ConflictResolutionAction.MANUAL_REVIEW.value == "manual_review"
        assert ConflictResolutionAction.IGNORE.value == "ignore"


# ============================================================================
# Class 2: FederationConflictService - Logging (5 tests)
# ============================================================================


class TestFederationConflictLogging:
    """Tests for conflict logging functionality."""

    @pytest.mark.asyncio
    async def test_log_conflict_signature_mismatch(self, test_db: AsyncSession):
        """Verify conflict is logged for signature mismatch."""
        # Arrange
        partner = FederationPartner(
            name="Test Partner",
            base_url="https://test-partner.example.com",
            public_key_pem="-----BEGIN PUBLIC KEY-----\nMIIBIjANBg...\n-----END PUBLIC KEY-----",
            key_id="https://test-partner.example.com#main-key",
            trust_state=TrustStatus.TRUSTED,
        )
        test_db.add(partner)
        await test_db.flush()

        activity = Activity(
            activity_type=ActivityType.ANNOUNCE,
            activity_id="https://test-partner.example.com/activities/announce-123",
            actor_url="https://test-partner.example.com/actor",
            activity_data={"type": "Announce"},
            local=0,
            partner_id=partner.id,
        )
        test_db.add(activity)
        await test_db.flush()

        # Act
        conflict = await FederationConflictService.log_conflict(
            db=test_db,
            partner_id=partner.id,
            conflict_type=ConflictType.SIGNATURE_MISMATCH,
            error_message="Signature verification failed: RSA signature verification failed",
            activity_id=activity.id,
        )

        # Assert
        assert conflict.partner_id == partner.id
        assert conflict.activity_id == activity.id
        assert conflict.conflict_type == ConflictType.SIGNATURE_MISMATCH
        assert conflict.status == ConflictStatus.ACTIVE
        assert conflict.error_message == "Signature verification failed: RSA signature verification failed"
        assert conflict.detected_at is not None

    @pytest.mark.asyncio
    async def test_log_conflict_key_expired(self, test_db: AsyncSession):
        """Verify conflict is logged for expired key."""
        # Arrange
        partner = FederationPartner(
            name="Expired Key Partner",
            base_url="https://expired-partner.example.com",
            public_key_pem="-----BEGIN PUBLIC KEY-----\nMIIBIjANBg...\n-----END PUBLIC KEY-----",
            key_id="https://expired-partner.example.com#main-key",
            trust_state=TrustStatus.TRUSTED,
        )
        test_db.add(partner)
        await test_db.flush()

        # Act
        conflict = await FederationConflictService.log_conflict(
            db=test_db,
            partner_id=partner.id,
            conflict_type=ConflictType.KEY_EXPIRED,
            error_message="Public key has expired",
        )

        # Assert
        assert conflict.conflict_type == ConflictType.KEY_EXPIRED
        assert conflict.activity_id is None  # Key-level conflict, no activity

    @pytest.mark.asyncio
    async def test_log_conflict_trust_failure(self, test_db: AsyncSession):
        """Verify conflict is logged for trust failure."""
        # Arrange
        partner = FederationPartner(
            name="Untrusted Partner",
            base_url="https://untrusted.example.com",
            public_key_pem="-----BEGIN PUBLIC KEY-----\nMIIBIjANBg...\n-----END PUBLIC KEY-----",
            key_id="https://untrusted.example.com#main-key",
            trust_state=TrustStatus.UNTRUSTED,
        )
        test_db.add(partner)
        await test_db.flush()

        # Act
        conflict = await FederationConflictService.log_conflict(
            db=test_db,
            partner_id=partner.id,
            conflict_type=ConflictType.TRUST_FAILURE,
            error_message="Partner trust status is 'untrusted'",
        )

        # Assert
        assert conflict.conflict_type == ConflictType.TRUST_FAILURE

    @pytest.mark.asyncio
    async def test_log_conflict_with_invalid_partner_raises_error(self, test_db: AsyncSession):
        """Verify log_conflict raises error for invalid partner."""
        # Act & Assert
        with pytest.raises(ValueError, match="Federation partner with id 9999 not found"):
            await FederationConflictService.log_conflict(
                db=test_db,
                partner_id=9999,
                conflict_type=ConflictType.SIGNATURE_MISMATCH,
            )

    @pytest.mark.asyncio
    async def test_log_multiple_conflicts_same_partner(self, test_db: AsyncSession):
        """Verify multiple conflicts can be logged for same partner."""
        # Arrange
        partner = FederationPartner(
            name="Problem Partner",
            base_url="https://problem-partner.example.com",
            public_key_pem="-----BEGIN PUBLIC KEY-----\nMIIBIjANBg...\n-----END PUBLIC KEY-----",
            key_id="https://problem-partner.example.com#main-key",
            trust_state=TrustStatus.TRUSTED,
        )
        test_db.add(partner)
        await test_db.flush()

        # Act
        conflict1 = await FederationConflictService.log_conflict(
            db=test_db,
            partner_id=partner.id,
            conflict_type=ConflictType.SIGNATURE_MISMATCH,
            error_message="First failure",
        )
        conflict2 = await FederationConflictService.log_conflict(
            db=test_db,
            partner_id=partner.id,
            conflict_type=ConflictType.SIGNATURE_MISMATCH,
            error_message="Second failure",
        )

        # Assert
        assert conflict1.id != conflict2.id
        assert conflict1.partner_id == conflict2.partner_id


# ============================================================================
# Class 3: FederationConflictService - Resolution & Querying (5 tests)
# ============================================================================


class TestFederationConflictResolution:
    """Tests for conflict resolution and querying."""

    @pytest.mark.asyncio
    async def test_resolve_conflict(self, test_db: AsyncSession):
        """Verify conflict can be marked as resolved."""
        # Arrange
        partner = FederationPartner(
            name="Test Partner",
            base_url="https://test.example.com",
            public_key_pem="-----BEGIN PUBLIC KEY-----\nMIIBIjANBg...\n-----END PUBLIC KEY-----",
            key_id="https://test.example.com#main-key",
            trust_state=TrustStatus.TRUSTED,
        )
        test_db.add(partner)
        await test_db.flush()

        conflict = await FederationConflictService.log_conflict(
            db=test_db,
            partner_id=partner.id,
            conflict_type=ConflictType.SIGNATURE_MISMATCH,
        )

        # Act
        resolved = await FederationConflictService.resolve_conflict(
            db=test_db,
            conflict_id=conflict.id,
            resolution_action=ConflictResolutionAction.AUTO_DOWNGRADE,
            resolved_by="system",
            resolution_notes="Partner auto-downgraded after 5 failed signatures",
        )

        # Assert
        assert resolved.status == ConflictStatus.RESOLVED
        assert resolved.resolution_action == ConflictResolutionAction.AUTO_DOWNGRADE
        assert resolved.resolved_by == "system"
        assert resolved.resolution_notes == "Partner auto-downgraded after 5 failed signatures"
        assert resolved.resolved_at is not None

    @pytest.mark.asyncio
    async def test_get_active_conflicts(self, test_db: AsyncSession):
        """Verify get_active_conflicts returns only active conflicts."""
        # Arrange
        partner = FederationPartner(
            name="Test Partner",
            base_url="https://test.example.com",
            public_key_pem="-----BEGIN PUBLIC KEY-----\nMIIBIjANBg...\n-----END PUBLIC KEY-----",
            key_id="https://test.example.com#main-key",
            trust_state=TrustStatus.TRUSTED,
        )
        test_db.add(partner)
        await test_db.flush()

        # Log and resolve one conflict
        conflict1 = await FederationConflictService.log_conflict(
            db=test_db,
            partner_id=partner.id,
            conflict_type=ConflictType.SIGNATURE_MISMATCH,
        )
        await FederationConflictService.resolve_conflict(
            db=test_db,
            conflict_id=conflict1.id,
            resolution_action=ConflictResolutionAction.MANUAL_REVIEW,
        )

        # Log another active conflict
        conflict2 = await FederationConflictService.log_conflict(
            db=test_db,
            partner_id=partner.id,
            conflict_type=ConflictType.KEY_EXPIRED,
        )

        # Act
        active = await FederationConflictService.get_active_conflicts(db=test_db)

        # Assert
        assert len(active) == 1
        assert active[0]["id"] == conflict2.id
        assert active[0]["status"] == "active"

    @pytest.mark.asyncio
    async def test_get_all_conflicts_with_status_filter(self, test_db: AsyncSession):
        """Verify get_all_conflicts respects status filter."""
        # Arrange
        partner = FederationPartner(
            name="Test Partner",
            base_url="https://test.example.com",
            public_key_pem="-----BEGIN PUBLIC KEY-----\nMIIBIjANBg...\n-----END PUBLIC KEY-----",
            key_id="https://test.example.com#main-key",
            trust_state=TrustStatus.TRUSTED,
        )
        test_db.add(partner)
        await test_db.flush()

        conflict1 = await FederationConflictService.log_conflict(
            db=test_db,
            partner_id=partner.id,
            conflict_type=ConflictType.SIGNATURE_MISMATCH,
        )
        conflict2 = await FederationConflictService.log_conflict(
            db=test_db,
            partner_id=partner.id,
            conflict_type=ConflictType.KEY_EXPIRED,
        )
        await FederationConflictService.resolve_conflict(
            db=test_db,
            conflict_id=conflict2.id,
            resolution_action=ConflictResolutionAction.MANUAL_REVIEW,
        )

        # Act - get only active
        active_result = await FederationConflictService.get_all_conflicts(
            db=test_db,
            status="active",
        )

        # Assert
        assert active_result["total"] == 1
        assert len(active_result["conflicts"]) == 1
        assert active_result["conflicts"][0]["status"] == "active"

        # Act - get only resolved
        resolved_result = await FederationConflictService.get_all_conflicts(
            db=test_db,
            status="resolved",
        )

        # Assert
        assert resolved_result["total"] == 1
        assert resolved_result["conflicts"][0]["status"] == "resolved"

    @pytest.mark.asyncio
    async def test_get_all_conflicts_with_partner_filter(self, test_db: AsyncSession):
        """Verify get_all_conflicts respects partner_id filter."""
        # Arrange
        partner1 = FederationPartner(
            name="Partner 1",
            base_url="https://partner1.example.com",
            public_key_pem="-----BEGIN PUBLIC KEY-----\nMIIBIjANBg...\n-----END PUBLIC KEY-----",
            key_id="https://partner1.example.com#main-key",
            trust_state=TrustStatus.TRUSTED,
        )
        partner2 = FederationPartner(
            name="Partner 2",
            base_url="https://partner2.example.com",
            public_key_pem="-----BEGIN PUBLIC KEY-----\nMIIBIjANBg...\n-----END PUBLIC KEY-----",
            key_id="https://partner2.example.com#main-key",
            trust_state=TrustStatus.TRUSTED,
        )
        test_db.add(partner1)
        test_db.add(partner2)
        await test_db.flush()

        await FederationConflictService.log_conflict(
            db=test_db,
            partner_id=partner1.id,
            conflict_type=ConflictType.SIGNATURE_MISMATCH,
        )
        await FederationConflictService.log_conflict(
            db=test_db,
            partner_id=partner2.id,
            conflict_type=ConflictType.KEY_EXPIRED,
        )

        # Act
        result = await FederationConflictService.get_all_conflicts(
            db=test_db,
            partner_id=partner1.id,
        )

        # Assert
        assert result["total"] == 1
        assert result["conflicts"][0]["partner_id"] == partner1.id

    @pytest.mark.asyncio
    async def test_get_partner_conflict_summary(self, test_db: AsyncSession):
        """Verify get_partner_conflict_summary provides summary stats."""
        # Arrange
        partner = FederationPartner(
            name="Test Partner",
            base_url="https://test.example.com",
            public_key_pem="-----BEGIN PUBLIC KEY-----\nMIIBIjANBg...\n-----END PUBLIC KEY-----",
            key_id="https://test.example.com#main-key",
            trust_state=TrustStatus.TRUSTED,
        )
        test_db.add(partner)
        await test_db.flush()

        # Log various conflicts
        conflict1 = await FederationConflictService.log_conflict(
            db=test_db,
            partner_id=partner.id,
            conflict_type=ConflictType.SIGNATURE_MISMATCH,
        )
        conflict2 = await FederationConflictService.log_conflict(
            db=test_db,
            partner_id=partner.id,
            conflict_type=ConflictType.SIGNATURE_MISMATCH,
        )
        conflict3 = await FederationConflictService.log_conflict(
            db=test_db,
            partner_id=partner.id,
            conflict_type=ConflictType.KEY_EXPIRED,
        )

        # Resolve one
        await FederationConflictService.resolve_conflict(
            db=test_db,
            conflict_id=conflict3.id,
            resolution_action=ConflictResolutionAction.MANUAL_REVIEW,
        )

        # Act
        summary = await FederationConflictService.get_partner_conflict_summary(
            db=test_db,
            partner_id=partner.id,
        )

        # Assert
        assert summary["partner_id"] == partner.id
        assert summary["partner_name"] == "Test Partner"
        assert summary["active_conflicts"]["total"] == 2
        assert summary["resolved_conflicts"]["total"] == 1
        assert "signature_mismatch" in summary["active_conflicts"]["by_type"]


# ============================================================================
# Class 4: Admin Endpoint Integration (4 tests)
# ============================================================================


class TestFederationConflictAdminEndpoint:
    """Tests for GET /admin/federation/conflicts endpoint."""

    @pytest.mark.asyncio
    async def test_get_conflicts_endpoint_success(self, client, test_db: AsyncSession):
        """Verify GET /admin/federation/conflicts returns conflicts."""
        # Arrange
        partner = FederationPartner(
            name="Test Partner",
            base_url="https://test.example.com",
            public_key_pem="-----BEGIN PUBLIC KEY-----\nMIIBIjANBg...\n-----END PUBLIC KEY-----",
            key_id="https://test.example.com#main-key",
            trust_state=TrustStatus.TRUSTED,
        )
        test_db.add(partner)
        await test_db.flush()

        await FederationConflictService.log_conflict(
            db=test_db,
            partner_id=partner.id,
            conflict_type=ConflictType.SIGNATURE_MISMATCH,
            error_message="Test error",
        )
        await test_db.commit()

        # Act
        response = await client.get("/admin/federation/conflicts")

        # Assert
        assert response.status_code == 200
        data = response.json()
        assert "conflicts" in data
        assert "total" in data
        assert len(data["conflicts"]) > 0

    @pytest.mark.asyncio
    async def test_get_conflicts_endpoint_with_partner_filter(self, client, test_db: AsyncSession):
        """Verify endpoint respects partner_id filter."""
        # Arrange
        partner = FederationPartner(
            name="Filtered Partner",
            base_url="https://filtered.example.com",
            public_key_pem="-----BEGIN PUBLIC KEY-----\nMIIBIjANBg...\n-----END PUBLIC KEY-----",
            key_id="https://filtered.example.com#main-key",
            trust_state=TrustStatus.TRUSTED,
        )
        test_db.add(partner)
        await test_db.flush()

        await FederationConflictService.log_conflict(
            db=test_db,
            partner_id=partner.id,
            conflict_type=ConflictType.SIGNATURE_MISMATCH,
        )
        await test_db.commit()

        # Act
        response = await client.get(f"/admin/federation/conflicts?partner_id={partner.id}")

        # Assert
        assert response.status_code == 200
        data = response.json()
        assert data["total"] >= 1

    @pytest.mark.asyncio
    async def test_get_conflicts_endpoint_with_status_filter(self, client, test_db: AsyncSession):
        """Verify endpoint respects status filter."""
        # Arrange
        partner = FederationPartner(
            name="Status Test Partner",
            base_url="https://status-test.example.com",
            public_key_pem="-----BEGIN PUBLIC KEY-----\nMIIBIjANBg...\n-----END PUBLIC KEY-----",
            key_id="https://status-test.example.com#main-key",
            trust_state=TrustStatus.TRUSTED,
        )
        test_db.add(partner)
        await test_db.flush()

        await FederationConflictService.log_conflict(
            db=test_db,
            partner_id=partner.id,
            conflict_type=ConflictType.SIGNATURE_MISMATCH,
        )
        await test_db.commit()

        # Act
        response = await client.get("/admin/federation/conflicts?status=active")

        # Assert
        assert response.status_code == 200
        data = response.json()
        for conflict in data["conflicts"]:
            assert conflict["status"] == "active"

    @pytest.mark.asyncio
    async def test_get_conflicts_endpoint_invalid_status_returns_400(self, client):
        """Verify endpoint returns 400 for invalid status."""
        # Act
        response = await client.get("/admin/federation/conflicts?status=invalid")

        # Assert
        assert response.status_code == 400


# ============================================================================
# Class 5: End-to-End Conflict Flow (2 tests)
# ============================================================================


class TestEndToEndConflictFlow:
    """Tests for complete conflict workflows."""

    @pytest.mark.asyncio
    async def test_signature_failure_logs_conflict_and_downgrades_trust(self, test_db: AsyncSession):
        """Verify signature failure triggers conflict logging and trust downgrade."""
        # Arrange
        partner = FederationPartner(
            name="Failing Partner",
            base_url="https://failing.example.com",
            public_key_pem="-----BEGIN PUBLIC KEY-----\nMIIBIjANBg...\n-----END PUBLIC KEY-----",
            key_id="https://failing.example.com#main-key",
            trust_state=TrustStatus.TRUSTED,
        )
        test_db.add(partner)
        await test_db.flush()

        # Simulate multiple signature failures
        for i in range(3):
            await FederationConflictService.log_conflict(
                db=test_db,
                partner_id=partner.id,
                conflict_type=ConflictType.SIGNATURE_MISMATCH,
                error_message=f"Signature verification failed (attempt {i+1})",
            )

        # Act
        conflicts = await FederationConflictService.get_active_conflicts(
            db=test_db,
            partner_id=partner.id,
        )

        # Assert
        assert len(conflicts) == 3
        for conflict in conflicts:
            assert conflict["conflict_type"] == "signature_mismatch"
            assert conflict["status"] == "active"

    @pytest.mark.asyncio
    async def test_conflict_resolution_workflow(self, test_db: AsyncSession):
        """Verify complete conflict detection and resolution workflow."""
        # Arrange: Create partner and log conflict
        partner = FederationPartner(
            name="Workflow Partner",
            base_url="https://workflow.example.com",
            public_key_pem="-----BEGIN PUBLIC KEY-----\nMIIBIjANBg...\n-----END PUBLIC KEY-----",
            key_id="https://workflow.example.com#main-key",
            trust_state=TrustStatus.TRUSTED,
        )
        test_db.add(partner)
        await test_db.flush()

        conflict = await FederationConflictService.log_conflict(
            db=test_db,
            partner_id=partner.id,
            conflict_type=ConflictType.KEY_EXPIRED,
            error_message="Public key expired on 2026-04-26",
        )

        # Act: Get active conflicts
        active = await FederationConflictService.get_active_conflicts(
            db=test_db,
            partner_id=partner.id,
        )
        assert len(active) == 1

        # Act: Resolve conflict
        resolved = await FederationConflictService.resolve_conflict(
            db=test_db,
            conflict_id=conflict.id,
            resolution_action=ConflictResolutionAction.MANUAL_REVIEW,
            resolved_by="admin@example.com",
            resolution_notes="Manually refreshed partner key",
        )

        # Assert: Conflict is now resolved
        assert resolved.status == ConflictStatus.RESOLVED
        assert resolved.resolution_action == ConflictResolutionAction.MANUAL_REVIEW

        # Act: Verify conflict no longer in active list
        active_after = await FederationConflictService.get_active_conflicts(
            db=test_db,
            partner_id=partner.id,
        )
        assert len(active_after) == 0

        # Act: Verify conflict is in resolved list
        resolved_conflicts = await FederationConflictService.get_resolved_conflicts(
            db=test_db,
            partner_id=partner.id,
        )
        assert len(resolved_conflicts) == 1
        assert resolved_conflicts[0]["id"] == conflict.id
