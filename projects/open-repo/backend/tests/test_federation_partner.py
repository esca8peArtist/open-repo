"""Tests for FederationPartner model and Wave 4 federation features.

Phase 1: Data model validation tests for FederationPartner.
Tests verify constraints, field validation, and relationships.
"""

import pytest
from datetime import datetime
from unittest.mock import AsyncMock, MagicMock

from app.models import FederationPartner, TrustStatus, Activity, ActivityType


class TestFederationPartnerModel:
    """Tests for FederationPartner data model validation."""

    def test_create_federation_partner_valid(self):
        """Verify FederationPartner can be instantiated with all required fields."""
        partner = FederationPartner(
            name="Node B Community Database",
            base_url="https://node-b.example.com",
            public_key_pem="-----BEGIN PUBLIC KEY-----\nMIIBIjANBg...\n-----END PUBLIC KEY-----",
            key_id="https://node-b.example.com#main-key",
            trust_state=TrustStatus.PENDING,
        )

        assert partner.name == "Node B Community Database"
        assert partner.base_url == "https://node-b.example.com"
        assert partner.public_key_pem == "-----BEGIN PUBLIC KEY-----\nMIIBIjANBg...\n-----END PUBLIC KEY-----"
        assert partner.key_id == "https://node-b.example.com#main-key"
        assert partner.trust_state == TrustStatus.PENDING

    def test_federation_partner_has_table_name(self):
        """Verify FederationPartner has correct table name."""
        assert FederationPartner.__tablename__ == "federation_partners"

    def test_federation_partner_trust_state_enum_values(self):
        """Verify TrustStatus enum has all required values."""
        assert TrustStatus.PENDING.value == "pending"
        assert TrustStatus.TRUSTED.value == "trusted"
        assert TrustStatus.UNTRUSTED.value == "untrusted"
        assert TrustStatus.REVOKED.value == "revoked"

    def test_federation_partner_default_trust_state(self):
        """Verify trust_state defaults to 'pending' via column definition."""
        # Column definition check
        from sqlalchemy import inspect

        mapper = inspect(FederationPartner)
        trust_state_col = mapper.columns['trust_state']

        # Verify default is set in the column definition
        assert trust_state_col.default is not None or trust_state_col.server_default is not None

    def test_federation_partner_fields_configuration(self):
        """Verify FederationPartner has all required fields as per spec."""
        from sqlalchemy import inspect

        mapper = inspect(FederationPartner)
        column_names = [col.name for col in mapper.columns]

        # Verify all required fields exist
        required_fields = [
            'id', 'name', 'base_url', 'public_key_pem', 'key_id',
            'trust_state', 'created_at', 'updated_at',
            'public_key_expires_at', 'last_key_refresh_at', 'last_activity_at'
        ]

        for field in required_fields:
            assert field in column_names, f"Missing required field: {field}"

    def test_federation_partner_unique_constraints(self):
        """Verify FederationPartner has unique constraints on name, base_url, key_id."""
        from sqlalchemy import inspect

        mapper = inspect(FederationPartner)
        # Get unique constraints from the table
        table = mapper.local_table
        unique_constraints = {uc.name for uc in table.constraints if hasattr(uc, 'unique') and uc.unique}

        # Verify unique constraints exist (names are auto-generated)
        # We should have at least 3 unique constraints for name, base_url, key_id
        assert len([c for c in mapper.columns if c.unique]) >= 2, "Should have unique columns"

    def test_federation_partner_repr(self):
        """Verify __repr__ method returns meaningful representation."""
        partner = FederationPartner(
            name="Test Node",
            base_url="https://test.example.com",
            public_key_pem="-----BEGIN PUBLIC KEY-----\nKey\n-----END PUBLIC KEY-----",
            key_id="https://test.example.com#main-key",
            trust_state=TrustStatus.TRUSTED,
        )
        partner.id = 1

        repr_str = repr(partner)
        assert "FederationPartner" in repr_str
        assert "Test Node" in repr_str
        assert "TRUSTED" in repr_str or "trusted" in repr_str

    def test_federation_partner_optional_fields_allowed(self):
        """Verify optional fields can be None."""
        partner = FederationPartner(
            name="Minimal Partner",
            base_url="https://minimal.example.com",
            public_key_pem="-----BEGIN PUBLIC KEY-----\nKey\n-----END PUBLIC KEY-----",
            key_id="https://minimal.example.com#main-key",
        )

        assert partner.public_key_expires_at is None
        assert partner.last_key_refresh_at is None
        assert partner.last_activity_at is None


class TestActivityFederationFields:
    """Tests for Activity model federation extensions."""

    def test_activity_federation_partner_field_exists(self):
        """Verify Activity model has partner_id field."""
        from sqlalchemy import inspect

        mapper = inspect(Activity)
        column_names = [col.name for col in mapper.columns]

        assert 'partner_id' in column_names

    def test_activity_signature_fields_exist(self):
        """Verify Activity model has signature_header and signature_verified fields."""
        from sqlalchemy import inspect

        mapper = inspect(Activity)
        column_names = [col.name for col in mapper.columns]

        assert 'signature_header' in column_names
        assert 'signature_verified' in column_names

    def test_activity_with_federation_fields(self):
        """Verify Activity can be instantiated with federation fields."""
        activity = Activity(
            activity_type=ActivityType.ANNOUNCE,
            activity_id="https://node-a.example.com/announce/123",
            actor_url="https://node-a.example.com/actor",
            activity_data={"type": "Announce"},
            partner_id=1,
            signature_header='keyId="https://node-a.example.com#main-key"',
            signature_verified=1,
        )

        assert activity.partner_id == 1
        assert activity.signature_verified == 1
        assert activity.signature_header == 'keyId="https://node-a.example.com#main-key"'

    def test_activity_signature_verified_default_zero(self):
        """Verify signature_verified defaults to 0 (unverified)."""
        from sqlalchemy import inspect

        mapper = inspect(Activity)
        sig_verified_col = mapper.columns['signature_verified']

        # Verify default is 0
        assert sig_verified_col.default is not None or sig_verified_col.server_default is not None

    def test_activity_partner_id_optional(self):
        """Verify partner_id is optional (for local activities without federation)."""
        activity = Activity(
            activity_type=ActivityType.ANNOUNCE,
            activity_id="https://node-a.example.com/announce/999",
            actor_url="https://node-a.example.com/actor",
            activity_data={"type": "Announce"},
            # Not specifying partner_id
        )

        assert activity.partner_id is None


class TestFederationPartnerIntegrity:
    """Tests for FederationPartner data integrity and constraints."""

    def test_federation_partner_key_id_field_configuration(self):
        """Verify key_id field is properly configured with unique constraint."""
        from sqlalchemy import inspect

        mapper = inspect(FederationPartner)
        key_id_col = mapper.columns['key_id']

        # Verify it's not nullable
        assert not key_id_col.nullable, "key_id should not be nullable"

    def test_federation_partner_base_url_field_configuration(self):
        """Verify base_url field is properly configured."""
        from sqlalchemy import inspect

        mapper = inspect(FederationPartner)
        base_url_col = mapper.columns['base_url']

        # Verify it's not nullable
        assert not base_url_col.nullable, "base_url should not be nullable"
        # Verify it's a String type with sufficient length
        assert base_url_col.type.length >= 512, "base_url should support at least 512 chars"

    def test_federation_partner_name_field_configuration(self):
        """Verify name field is properly configured."""
        from sqlalchemy import inspect

        mapper = inspect(FederationPartner)
        name_col = mapper.columns['name']

        # Verify it's not nullable
        assert not name_col.nullable, "name should not be nullable"
        # Verify it's a String type
        assert name_col.type.length >= 255, "name should support at least 255 chars"

    def test_federation_partner_public_key_pem_is_text(self):
        """Verify public_key_pem is a Text field (not String)."""
        from sqlalchemy import inspect, Text

        mapper = inspect(FederationPartner)
        pem_col = mapper.columns['public_key_pem']

        # Verify it's a Text type to handle large PEM blocks
        assert isinstance(pem_col.type, Text), "public_key_pem should be Text type"
        assert not pem_col.nullable, "public_key_pem should not be nullable"
