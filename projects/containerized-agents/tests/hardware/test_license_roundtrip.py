"""
Hardware tests: generate license, validate against correct/incorrect hardware.
"""
from __future__ import annotations

import os
from unittest.mock import MagicMock, patch

import pytest

from security.hardware_binding.fallback_license import generate_license, validate_license


class TestLicenseRoundtrip:
    """Generate + validate license round-trip tests."""

    def _mock_fp(self, fp_hex: str, valid: bool = True):
        m = MagicMock()
        m.is_valid.return_value = valid
        m.sha256_fingerprint.return_value = bytes.fromhex(fp_hex)
        return m

    def test_tier1_roundtrip(self):
        """Tier 1 license must validate on matching hardware."""
        key = os.urandom(32)
        fp = "a" * 64
        lic = generate_license(fp, tier=1, signing_key=key)
        with patch("security.hardware_binding.fallback_license.collect_fingerprint", return_value=self._mock_fp(fp)):
            ok, msg = validate_license(lic, key)
        assert ok is True

    def test_tier2_roundtrip(self):
        """Tier 2 license must validate on matching hardware."""
        key = os.urandom(32)
        fp = "b" * 64
        lic = generate_license(fp, tier=2, signing_key=key)
        with patch("security.hardware_binding.fallback_license.collect_fingerprint", return_value=self._mock_fp(fp)):
            ok, _ = validate_license(lic, key)
        assert ok is True

    def test_tier3_roundtrip(self):
        key = os.urandom(32)
        fp = "c" * 64
        lic = generate_license(fp, tier=3, signing_key=key)
        with patch("security.hardware_binding.fallback_license.collect_fingerprint", return_value=self._mock_fp(fp)):
            ok, _ = validate_license(lic, key)
        assert ok is True

    def test_tier4_roundtrip(self):
        key = os.urandom(32)
        fp = "d" * 64
        lic = generate_license(fp, tier=4, signing_key=key)
        with patch("security.hardware_binding.fallback_license.collect_fingerprint", return_value=self._mock_fp(fp)):
            ok, _ = validate_license(lic, key)
        assert ok is True

    def test_wrong_hardware_fails(self):
        """License for hardware A must fail on hardware B."""
        key = os.urandom(32)
        fp_a = "e" * 64
        fp_b = "f" * 64
        lic = generate_license(fp_a, tier=1, signing_key=key)
        with patch("security.hardware_binding.fallback_license.collect_fingerprint", return_value=self._mock_fp(fp_b)):
            ok, msg = validate_license(lic, key)
        assert ok is False

    def test_wrong_signing_key_fails(self):
        """License signed with key1 must fail validation with key2."""
        key1 = os.urandom(32)
        key2 = os.urandom(32)
        fp = "0" * 64
        lic = generate_license(fp, tier=1, signing_key=key1)
        with patch("security.hardware_binding.fallback_license.collect_fingerprint", return_value=self._mock_fp(fp)):
            ok, _ = validate_license(lic, key2)
        assert ok is False

    def test_invalid_tier_raises(self):
        """Tier 0 and tier 5 must raise ValueError."""
        key = os.urandom(32)
        with pytest.raises(ValueError):
            generate_license("a" * 64, tier=0, signing_key=key)
        with pytest.raises(ValueError):
            generate_license("a" * 64, tier=5, signing_key=key)

    def test_short_fingerprint_raises(self):
        """Fingerprint shorter than 64 hex chars must raise ValueError."""
        key = os.urandom(32)
        with pytest.raises(ValueError):
            generate_license("tooshort", tier=1, signing_key=key)

    def test_invalid_hardware_fingerprint_fails(self):
        """If the machine cannot produce a valid fingerprint, validation must fail."""
        key = os.urandom(32)
        fp = "a" * 64
        lic = generate_license(fp, tier=1, signing_key=key)
        with patch("security.hardware_binding.fallback_license.collect_fingerprint", return_value=self._mock_fp(fp, valid=False)):
            ok, _ = validate_license(lic, key)
        assert ok is False
