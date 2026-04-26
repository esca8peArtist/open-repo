"""
Channel tests: Twilio webhook signature validation — accept/reject.
"""
from __future__ import annotations

import base64
import hashlib
import hmac
from unittest.mock import AsyncMock

import pytest

twilio = pytest.importorskip("twilio")

from agentcore.channels.twilio.sms import TwilioSMSChannel


def _sign(auth_token: str, url: str, params: dict) -> str:
    """Compute valid Twilio HMAC-SHA1 signature."""
    s = url + "".join(k + params[k] for k in sorted(params.keys()))
    mac = hmac.new(auth_token.encode(), s.encode(), hashlib.sha1)
    return base64.b64encode(mac.digest()).decode()


class TestTwilioSignatureValidation:
    """Webhook signature accept/reject tests."""

    def _make_channel(self, token="testtoken123"):
        async def _r(msg):
            return "ok"
        return TwilioSMSChannel(
            account_sid="ACtest",
            auth_token=token,
            from_number="+15550000",
            message_router=_r,
        )

    def test_valid_signature_accepted(self):
        """Correct HMAC signature must be accepted."""
        channel = self._make_channel("correcttoken")
        url = "https://agent.local/twilio/sms"
        params = {"From": "+15559999", "Body": "Hi", "To": "+15550000"}
        sig = _sign("correcttoken", url, params)
        assert channel.validate_signature(url, params, sig) is True

    def test_empty_signature_rejected(self):
        """Empty signature string must be rejected."""
        channel = self._make_channel()
        assert channel.validate_signature("https://agent.local/twilio/sms", {}, "") is False

    def test_wrong_token_rejected(self):
        """Signature computed with wrong token must be rejected."""
        channel = self._make_channel("realtoken")
        url = "https://agent.local/twilio/sms"
        params = {"From": "+15559999", "Body": "Hi"}
        sig = _sign("wrongtoken", url, params)
        assert channel.validate_signature(url, params, sig) is False

    def test_tampered_body_rejected(self):
        """Changing message body after signing must invalidate signature."""
        channel = self._make_channel("mytoken")
        url = "https://agent.local/twilio/sms"
        orig = {"From": "+15559999", "Body": "Original"}
        sig = _sign("mytoken", url, orig)
        modified = {"From": "+15559999", "Body": "HACKED"}
        assert channel.validate_signature(url, modified, sig) is False

    def test_different_url_rejected(self):
        """Signature for URL A must fail validation against URL B."""
        channel = self._make_channel("mytoken")
        url_a = "https://agent.local/twilio/sms"
        url_b = "https://agent.local/twilio/evil"
        params = {"From": "+15559999", "Body": "Hi"}
        sig = _sign("mytoken", url_a, params)
        assert channel.validate_signature(url_b, params, sig) is False

    def test_extra_param_in_request_rejected(self):
        """Adding extra params to the request (not in signature) must fail."""
        channel = self._make_channel("mytoken")
        url = "https://agent.local/twilio/sms"
        orig = {"From": "+15559999", "Body": "Hi"}
        sig = _sign("mytoken", url, orig)
        modified = {"From": "+15559999", "Body": "Hi", "ExtraParam": "evil"}
        assert channel.validate_signature(url, modified, sig) is False

    def test_replay_attack_same_url_same_params_same_sig_accepted(self):
        """The same valid request (replay) — signature itself is stateless (by design)."""
        channel = self._make_channel("mytoken")
        url = "https://agent.local/twilio/sms"
        params = {"From": "+15559999", "Body": "Hi"}
        sig = _sign("mytoken", url, params)
        # Both calls accepted — rate limiting is handled at the channel layer
        assert channel.validate_signature(url, params, sig) is True
        assert channel.validate_signature(url, params, sig) is True
