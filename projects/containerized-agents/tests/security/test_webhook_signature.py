"""
Security tests: Twilio webhook signature validation.
Verifies that unsigned and tampered Twilio webhook requests are rejected.
"""
from __future__ import annotations

import hashlib
import hmac
import base64
from unittest.mock import MagicMock, patch

import pytest

twilio = pytest.importorskip("twilio")

from agentcore.channels.twilio.sms import TwilioSMSChannel


def _compute_twilio_signature(auth_token: str, url: str, params: dict) -> str:
    """Compute a valid Twilio webhook signature for test use.

    Algorithm from Twilio docs:
    1. Take the full URL.
    2. Sort POST params alphabetically and append key+value pairs.
    3. Sign with HMAC-SHA1 using auth_token.
    4. Base64-encode.
    """
    s = url
    for key in sorted(params.keys()):
        s += key + params[key]
    mac = hmac.new(auth_token.encode("utf-8"), s.encode("utf-8"), hashlib.sha1)
    return base64.b64encode(mac.digest()).decode("utf-8")


class TestTwilioWebhookSignature:
    """Webhook signature validation tests."""

    def _make_channel(self, auth_token: str = "test_auth_token_abc") -> TwilioSMSChannel:
        """Create a TwilioSMSChannel with a mock router."""
        async def _mock_router(msg):
            return "reply"

        return TwilioSMSChannel(
            account_sid="ACtest123",
            auth_token=auth_token,
            from_number="+15550001234",
            message_router=_mock_router,
        )

    def test_valid_signature_accepted(self):
        """A request with a valid HMAC signature must pass validation."""
        channel = self._make_channel("secret_token")
        url = "https://agent.local/twilio/sms"
        params = {"From": "+15559999", "Body": "Hello", "To": "+15550001234"}
        valid_sig = _compute_twilio_signature("secret_token", url, params)

        result = channel.validate_signature(url, params, valid_sig)
        assert result is True

    def test_unsigned_request_rejected(self):
        """A request with no signature header must be rejected."""
        channel = self._make_channel()
        url = "https://agent.local/twilio/sms"
        params = {"From": "+15559999", "Body": "Hello"}

        result = channel.validate_signature(url, params, "")
        assert result is False

    def test_tampered_signature_rejected(self):
        """A request with a modified signature must fail validation."""
        channel = self._make_channel("real_token")
        url = "https://agent.local/twilio/sms"
        params = {"From": "+15559999", "Body": "Hello"}
        valid_sig = _compute_twilio_signature("real_token", url, params)

        # Tamper: change one char at the end
        tampered = valid_sig[:-3] + "AAA"
        result = channel.validate_signature(url, params, tampered)
        assert result is False

    def test_wrong_auth_token_rejected(self):
        """A signature computed with the wrong token must fail."""
        channel = self._make_channel("correct_token")
        url = "https://agent.local/twilio/sms"
        params = {"From": "+15559999", "Body": "Hello"}

        # Signed with wrong token
        wrong_sig = _compute_twilio_signature("wrong_token", url, params)
        result = channel.validate_signature(url, params, wrong_sig)
        assert result is False

    def test_different_url_rejected(self):
        """Same params + token but different URL → different signature → rejected."""
        channel = self._make_channel("mytoken")
        real_url = "https://agent.local/twilio/sms"
        other_url = "https://agent.local/twilio/evil"
        params = {"From": "+15559999", "Body": "Test"}
        valid_sig = _compute_twilio_signature("mytoken", real_url, params)

        # Validate against a different URL — must fail
        result = channel.validate_signature(other_url, params, valid_sig)
        assert result is False

    def test_modified_body_rejected(self):
        """Signature for 'Hello' must fail if body is changed to 'Evil'."""
        channel = self._make_channel("secrettoken")
        url = "https://agent.local/twilio/sms"
        original_params = {"From": "+15559999", "Body": "Hello"}
        modified_params = {"From": "+15559999", "Body": "Evil payload"}

        valid_sig = _compute_twilio_signature("secrettoken", url, original_params)
        result = channel.validate_signature(url, modified_params, valid_sig)
        assert result is False

    def test_constant_time_comparison_used(self):
        """Signature comparison must use hmac.compare_digest to prevent timing attacks."""
        import inspect
        import agentcore.channels.twilio.sms as sms_module

        source = inspect.getsource(sms_module)
        assert "compare_digest" in source or "hmac.compare_digest" in source, (
            "Twilio signature validation must use hmac.compare_digest for constant-time comparison"
        )
