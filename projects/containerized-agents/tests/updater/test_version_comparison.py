"""
Update system tests: semver comparison and min_version enforcement.
"""
from __future__ import annotations

import json
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from agentcore.updater.update_checker import check_for_updates, _extract_components


def _make_mock_settings(pub_key_hex: str = "a" * 64):
    """Return a MagicMock that satisfies get_settings().update_public_key_hex."""
    mock = MagicMock()
    mock.update_public_key_hex = pub_key_hex
    return mock


def _build_manifest(latest_version: str, min_version: str = "", current_sim: str = "1.0.0") -> dict:
    """Build a minimal signed-ish manifest for version tests."""
    return {
        "schema_version": 1,
        "generated_at": "2026-03-11T00:00:00Z",
        "latest": {"version": latest_version},
        "releases": [
            {
                "version": latest_version,
                "min_version": min_version,
                "changelog": "Changes here.",
                "components": {
                    "agentcore": {
                        "image_url": "https://example.com/agentcore.tar.gz",
                        "sha256": "a" * 64,
                        "docker_tag": latest_version,
                    }
                },
            }
        ],
        "signature": "a" * 128,  # fake sig; we'll patch verify
    }


class TestVersionComparison:
    """Version comparison and min_version constraint tests."""

    @pytest.mark.asyncio
    async def test_newer_version_triggers_update(self):
        """Latest version 1.2.0 > current 1.0.0 must set available=True."""
        manifest = _build_manifest("1.2.0")

        with (
            patch("agentcore.updater.update_checker.is_internet_available", new=AsyncMock(return_value=True)),
            patch("agentcore.updater.update_checker.get_settings", return_value=_make_mock_settings()),
            patch("agentcore.updater.update_checker._fetch_manifest", new=AsyncMock(return_value=manifest)),
            patch("agentcore.updater.update_checker.verify_manifest_signature", new=AsyncMock(return_value=True)),
        ):
            result = await check_for_updates("1.0.0")

        assert result.available is True
        assert result.latest_version == "1.2.0"

    @pytest.mark.asyncio
    async def test_same_version_no_update(self):
        """Latest == current must return available=False."""
        manifest = _build_manifest("1.0.0")

        with (
            patch("agentcore.updater.update_checker.is_internet_available", new=AsyncMock(return_value=True)),
            patch("agentcore.updater.update_checker.get_settings", return_value=_make_mock_settings()),
            patch("agentcore.updater.update_checker._fetch_manifest", new=AsyncMock(return_value=manifest)),
            patch("agentcore.updater.update_checker.verify_manifest_signature", new=AsyncMock(return_value=True)),
        ):
            result = await check_for_updates("1.0.0")

        assert result.available is False

    @pytest.mark.asyncio
    async def test_older_latest_no_update(self):
        """Latest (0.9.0) < current (1.0.0) must return available=False."""
        manifest = _build_manifest("0.9.0")

        with (
            patch("agentcore.updater.update_checker.is_internet_available", new=AsyncMock(return_value=True)),
            patch("agentcore.updater.update_checker.get_settings", return_value=_make_mock_settings()),
            patch("agentcore.updater.update_checker._fetch_manifest", new=AsyncMock(return_value=manifest)),
            patch("agentcore.updater.update_checker.verify_manifest_signature", new=AsyncMock(return_value=True)),
        ):
            result = await check_for_updates("1.0.0")

        assert result.available is False

    @pytest.mark.asyncio
    async def test_min_version_enforced(self):
        """Update requiring min_version 1.1.0 must be blocked for current 1.0.0."""
        manifest = _build_manifest("1.2.0", min_version="1.1.0")

        with (
            patch("agentcore.updater.update_checker.is_internet_available", new=AsyncMock(return_value=True)),
            patch("agentcore.updater.update_checker.get_settings", return_value=_make_mock_settings()),
            patch("agentcore.updater.update_checker._fetch_manifest", new=AsyncMock(return_value=manifest)),
            patch("agentcore.updater.update_checker.verify_manifest_signature", new=AsyncMock(return_value=True)),
        ):
            result = await check_for_updates("1.0.0")

        assert result.available is False
        assert "1.1.0" in result.error or "min" in result.error.lower()

    @pytest.mark.asyncio
    async def test_min_version_satisfied(self):
        """Update requiring min_version 1.1.0 must be offered to current 1.1.5."""
        manifest = _build_manifest("1.2.0", min_version="1.1.0")

        with (
            patch("agentcore.updater.update_checker.is_internet_available", new=AsyncMock(return_value=True)),
            patch("agentcore.updater.update_checker.get_settings", return_value=_make_mock_settings()),
            patch("agentcore.updater.update_checker._fetch_manifest", new=AsyncMock(return_value=manifest)),
            patch("agentcore.updater.update_checker.verify_manifest_signature", new=AsyncMock(return_value=True)),
        ):
            result = await check_for_updates("1.1.5")

        assert result.available is True

    @pytest.mark.asyncio
    async def test_invalid_signature_blocks_update(self):
        """Tampered manifest must not produce an update offer."""
        manifest = _build_manifest("2.0.0")

        with (
            patch("agentcore.updater.update_checker.is_internet_available", new=AsyncMock(return_value=True)),
            patch("agentcore.updater.update_checker.get_settings", return_value=_make_mock_settings()),
            patch("agentcore.updater.update_checker._fetch_manifest", new=AsyncMock(return_value=manifest)),
            patch("agentcore.updater.update_checker.verify_manifest_signature", new=AsyncMock(return_value=False)),
        ):
            result = await check_for_updates("1.0.0")

        assert result.available is False
        assert "signature" in result.error.lower() or "invalid" in result.error.lower()


class TestExtractComponents:
    """_extract_components helper tests."""

    def test_extract_agentcore_component(self):
        """Agentcore component must be extracted from release dict."""
        release = {
            "version": "1.2.0",
            "components": {
                "agentcore": {
                    "image_url": "https://example.com/agentcore.tar.gz",
                    "sha256": "b" * 64,
                    "docker_tag": "1.2.0",
                }
            },
        }
        components = _extract_components(release)
        assert len(components) >= 1
        types = [c["type"] for c in components]
        assert "agentcore" in types

    def test_extract_model_components(self):
        """Model entries must be included in the component list."""
        release = {
            "version": "1.2.0",
            "components": {
                "models": [
                    {
                        "name": "llama3.1:8b",
                        "version": "1",
                        "download_url": "https://example.com/model",
                        "sha256": "c" * 64,
                        "tiers": [1, 2, 3],
                    }
                ]
            },
        }
        components = _extract_components(release)
        assert any(c["type"] == "model" for c in components)

    def test_empty_components_returns_empty_list(self):
        """Release with no components must return empty list."""
        release = {"version": "1.0.0", "components": {}}
        components = _extract_components(release)
        assert components == []
