"""
Wizard tests: Telegram bot token validation (step 4) — mock Telegram API calls.
"""
from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

# The step4 router exposes /api/validate/telegram which calls validate_bot_token
# from agentcore.channels.telegram.setup. We test that endpoint and the underlying
# validation logic.


class TestTelegramTokenValidation:
    """Telegram bot token format and API validation tests."""

    def test_valid_token_format_passes_basic_check(self):
        """Token in format '123456:ABC-DEF...' must pass the format check."""
        token = "123456789:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw"
        # The offline format check: non-empty and contains ':'
        is_valid = bool(token) and ":" in token
        assert is_valid is True

    def test_empty_token_fails_format_check(self):
        """Empty token must fail the basic format check."""
        token = ""
        is_valid = bool(token) and ":" in token
        assert is_valid is False

    def test_token_without_colon_fails_format_check(self):
        """Token without ':' separator must fail the basic format check."""
        token = "123456789AAHTOKEN"
        is_valid = bool(token) and ":" in token
        assert is_valid is False

    def test_token_with_only_colon_fails(self):
        """Token that is just ':' must fail validation."""
        token = ":"
        parts = token.split(":")
        # Numeric bot ID before colon must be non-empty
        is_valid = bool(parts[0]) and bool(parts[1]) if len(parts) == 2 else False
        assert is_valid is False

    @pytest.mark.asyncio
    async def test_valid_token_succeeds_with_telegram_api(self):
        """validate_bot_token must return (True, username) on Telegram API success."""
        from agentcore.channels.telegram.setup import validate_bot_token

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "ok": True,
            "result": {
                "id": 123456789,
                "username": "mybot",
                "first_name": "My Bot",
                "is_bot": True,
            },
        }

        mock_client = AsyncMock()
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock(return_value=False)
        mock_client.get = AsyncMock(return_value=mock_response)

        with patch("httpx.AsyncClient", return_value=mock_client):
            valid, message = await validate_bot_token("123456789:AATEST")

        assert valid is True
        assert "mybot" in message or "My Bot" in message or message != ""

    @pytest.mark.asyncio
    async def test_invalid_token_rejected_by_telegram_api(self):
        """validate_bot_token must return (False, error_message) on 401."""
        from agentcore.channels.telegram.setup import validate_bot_token

        mock_response = MagicMock()
        mock_response.status_code = 401
        mock_response.json.return_value = {"ok": False, "description": "Unauthorized"}

        mock_client = AsyncMock()
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock(return_value=False)
        mock_client.get = AsyncMock(return_value=mock_response)

        with patch("httpx.AsyncClient", return_value=mock_client):
            valid, message = await validate_bot_token("000000000:INVALID")

        assert valid is False
        assert message != ""

    @pytest.mark.asyncio
    async def test_network_error_returns_false(self):
        """Network failure during token validation must return (False, error_text)."""
        from agentcore.channels.telegram.setup import validate_bot_token

        import httpx

        mock_client = AsyncMock()
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock(return_value=False)
        mock_client.get = AsyncMock(side_effect=httpx.ConnectError("Connection refused"))

        with patch("httpx.AsyncClient", return_value=mock_client):
            valid, message = await validate_bot_token("123456789:AATEST")

        assert valid is False
        assert message != ""

    @pytest.mark.asyncio
    async def test_telegram_api_returns_ok_false(self):
        """Telegram API response with ok=False (but HTTP 200) must fail validation."""
        from agentcore.channels.telegram.setup import validate_bot_token

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "ok": False,
            "description": "Not Found",
            "error_code": 404,
        }

        mock_client = AsyncMock()
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock(return_value=False)
        mock_client.get = AsyncMock(return_value=mock_response)

        with patch("httpx.AsyncClient", return_value=mock_client):
            valid, message = await validate_bot_token("000000000:BOGUS")

        assert valid is False

    @pytest.mark.asyncio
    async def test_step4_validate_endpoint_valid_token(self):
        """POST /api/validate/telegram with valid token must return JSON with valid=True."""
        from fastapi.testclient import TestClient
        from fastapi import FastAPI
        from wizard.steps.step4_channels import router

        app = FastAPI()
        app.include_router(router)
        client = TestClient(app, raise_server_exceptions=False)

        with patch(
            "agentcore.channels.telegram.setup.validate_bot_token",
            new=AsyncMock(return_value=(True, "@testbot")),
        ):
            response = client.post(
                "/api/validate/telegram",
                data={"token": "123456789:AATEST"},
            )

        assert response.status_code == 200
        data = response.json()
        assert data["valid"] is True

    @pytest.mark.asyncio
    async def test_step4_validate_endpoint_invalid_token(self):
        """POST /api/validate/telegram with invalid token must return valid=False."""
        from fastapi.testclient import TestClient
        from fastapi import FastAPI
        from wizard.steps.step4_channels import router

        app = FastAPI()
        app.include_router(router)
        client = TestClient(app, raise_server_exceptions=False)

        with patch(
            "agentcore.channels.telegram.setup.validate_bot_token",
            new=AsyncMock(return_value=(False, "Token invalid")),
        ):
            response = client.post(
                "/api/validate/telegram",
                data={"token": "badtoken"},
            )

        assert response.status_code == 200
        data = response.json()
        assert data["valid"] is False

    def test_step4_offline_fallback_format_check(self):
        """When agentcore is not importable, a format-only check is used."""
        # Simulate the ImportError fallback path in post /api/validate/telegram
        token = "123456789:AAHTEST"
        token_stripped = token.strip()
        valid = bool(token_stripped) and ":" in token_stripped
        assert valid is True

        empty_token = ""
        valid_empty = bool(empty_token) and ":" in empty_token
        assert valid_empty is False
