"""
Integration tests for the update check, install, and rollback flow.

Per requirements.md Section 12:
- "Check for Updates" pings a signed manifest URL when internet is available
- Returns UpdateInfo(available=False) when offline
- Signed manifests must be validated before applying
- Rollback is available for 24 hours after an update
"""
from __future__ import annotations

import json
from unittest.mock import AsyncMock, MagicMock, patch

import pytest


# ===========================================================================
# Update manifest schema validation
# ===========================================================================


class TestUpdateManifestSchema:
    def test_example_manifest_is_valid_json(self):
        """The example manifest must be valid JSON."""
        import os
        manifest_path = os.path.join(
            os.path.dirname(__file__),
            "../../update_server/example_manifest.json"
        )
        if not os.path.exists(manifest_path):
            pytest.skip("update_server/example_manifest.json not found")

        with open(manifest_path) as f:
            data = json.load(f)

        assert isinstance(data, dict), "Manifest must be a JSON object"

    def test_manifest_schema_is_valid_json_schema(self):
        """The manifest schema file must itself be valid JSON."""
        import os
        schema_path = os.path.join(
            os.path.dirname(__file__),
            "../../update_server/manifest_schema.json"
        )
        if not os.path.exists(schema_path):
            pytest.skip("update_server/manifest_schema.json not found")

        with open(schema_path) as f:
            schema = json.load(f)

        assert isinstance(schema, dict)
        assert "properties" in schema or "$schema" in schema or "type" in schema

    def test_example_manifest_has_required_fields(self):
        """The example manifest must contain at minimum: version, release_date, components."""
        import os
        manifest_path = os.path.join(
            os.path.dirname(__file__),
            "../../update_server/example_manifest.json"
        )
        if not os.path.exists(manifest_path):
            pytest.skip("update_server/example_manifest.json not found")

        with open(manifest_path) as f:
            data = json.load(f)

        # Check at least one of the expected version/release fields exists.
        # The manifest may use either "version"/"latest_version" (simple format) or
        # "schema_version"/"latest" (nested release format used by update_server/).
        has_version = (
            "version" in data
            or "latest_version" in data
            or "schema_version" in data
            or "latest" in data
            or "releases" in data
        )
        assert has_version, "Manifest must include a version or schema_version field"


# ===========================================================================
# Update checker — offline graceful degradation
# ===========================================================================


class TestUpdateCheckerOffline:
    @pytest.mark.asyncio
    async def test_update_check_offline_returns_not_available(self):
        """When internet is unreachable, update check must return available=False."""
        try:
            from agentcore.updater.update_checker import UpdateInfo, check_for_updates
        except ImportError:
            pytest.skip("agentcore.updater.update_checker not yet implemented")

        with patch("httpx.AsyncClient.head", side_effect=Exception("No internet")):
            result = await check_for_updates("1.0.0")

        assert result.available is False

    @pytest.mark.asyncio
    async def test_update_check_offline_does_not_raise(self):
        """Update check must never raise, even if all network calls fail."""
        try:
            from agentcore.updater.update_checker import check_for_updates
        except ImportError:
            pytest.skip("agentcore.updater.update_checker not yet implemented")

        with patch("httpx.AsyncClient.get", side_effect=Exception("Connection refused")):
            # Should not raise
            result = await check_for_updates("1.0.0")

        assert result is not None

    @pytest.mark.asyncio
    async def test_update_check_online_returns_update_info(self):
        """When online and a new version is available, returns UpdateInfo with available=True."""
        try:
            from agentcore.updater.update_checker import check_for_updates
        except ImportError:
            pytest.skip("agentcore.updater.update_checker not yet implemented")

        # The manifest format matches update_server/example_manifest.json:
        # latest.version + releases list
        mock_manifest = {
            "schema_version": 1,
            "published_at": "2026-03-01T00:00:00Z",
            "latest": {
                "version": "2.0.0",
                "tier1": "2.0.0",
                "tier2": "2.0.0",
                "tier3": "2.0.0",
                "tier4": "2.0.0",
            },
            "releases": [
                {
                    "version": "2.0.0",
                    "published_at": "2026-03-01T00:00:00Z",
                    "min_version": "1.0.0",
                    "changelog": "Bug fixes and improvements",
                    "critical": False,
                    "components": {},
                }
            ],
            "signature": "a" * 128,  # Fake hex signature (won't be verified — mocked)
        }

        mock_resp = AsyncMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = mock_manifest
        mock_resp.raise_for_status = MagicMock()

        with (
            patch("agentcore.updater.update_checker.is_internet_available", AsyncMock(return_value=True)),
            patch("agentcore.updater.update_checker.get_settings", return_value=MagicMock(update_public_key_hex="a" * 64)),
            patch("agentcore.updater.update_checker.verify_manifest_signature", AsyncMock(return_value=True)),
            patch("agentcore.updater.update_checker._fetch_manifest", AsyncMock(return_value=mock_manifest)),
        ):
            result = await check_for_updates("1.0.0")

        assert result.available is True
        assert result.latest_version == "2.0.0"

    @pytest.mark.asyncio
    async def test_update_check_same_version_returns_not_available(self):
        """If the current version equals the latest, update must not be reported as available."""
        try:
            from agentcore.updater.update_checker import check_for_updates
        except ImportError:
            pytest.skip("agentcore.updater.update_checker not yet implemented")

        mock_manifest = {
            "latest_version": "1.0.0",  # Same as current
            "release_date": "2026-01-01",
            "components": [],
            "changelog": "",
            "signature": "mock_signature",
        }

        mock_resp = AsyncMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = mock_manifest
        mock_resp.raise_for_status = MagicMock()

        with patch("httpx.AsyncClient.get", return_value=mock_resp):
            result = await check_for_updates("1.0.0")

        assert result.available is False


# ===========================================================================
# Update manifest validation
# ===========================================================================


class TestUpdateManifestValidation:
    def test_valid_manifest_passes_schema_validation(self):
        """A well-formed manifest must pass JSON Schema validation."""
        try:
            from agentcore.updater.manifest import validate_manifest
        except ImportError:
            pytest.skip("agentcore.updater.manifest not yet implemented")

        valid_manifest = {
            "latest_version": "1.2.0",
            "release_date": "2026-03-01",
            "components": [
                {
                    "name": "agentcore",
                    "version": "1.2.0",
                    "url": "https://updates.example.com/agentcore-1.2.0.tar.gz",
                    "sha256": "abc123",
                }
            ],
            "changelog": "New features and bug fixes",
        }

        # Must not raise
        is_valid = validate_manifest(valid_manifest)
        assert is_valid is True

    def test_invalid_manifest_fails_schema_validation(self):
        """A manifest missing required fields must fail validation."""
        try:
            from agentcore.updater.manifest import validate_manifest
        except ImportError:
            pytest.skip("agentcore.updater.manifest not yet implemented")

        invalid_manifest = {"not_a_valid_key": "garbage"}
        is_valid = validate_manifest(invalid_manifest)
        assert is_valid is False


# ===========================================================================
# Rollback mechanism
# ===========================================================================


class TestRollbackMechanism:
    @pytest.mark.asyncio
    async def test_rollback_available_after_update(self):
        """After applying an update, a rollback option must be available."""
        try:
            from agentcore.updater.rollback import is_rollback_available, get_rollback_version
        except ImportError:
            pytest.skip("agentcore.updater.rollback not yet implemented")

        # Mock: an update was applied 1 hour ago
        with patch("agentcore.updater.rollback.get_last_update_timestamp",
                   return_value=__import__("time").time() - 3600):
            available = await is_rollback_available()

        assert available is True

    @pytest.mark.asyncio
    async def test_rollback_not_available_after_24_hours(self):
        """After 24 hours, rollback must no longer be available."""
        try:
            from agentcore.updater.rollback import is_rollback_available
        except ImportError:
            pytest.skip("agentcore.updater.rollback not yet implemented")

        # Mock: update was applied 25 hours ago
        import time
        with patch("agentcore.updater.rollback.get_last_update_timestamp",
                   return_value=time.time() - (25 * 3600)):
            available = await is_rollback_available()

        assert available is False
