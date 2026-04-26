"""
MCP tool tests: email tools — mock SMTP/IMAP, test send/read, auth failure handling.
"""
from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from agentcore.config import get_settings
from agentcore.mcp.protocol import MCPContext
from agentcore.mcp.tools.email import SendEmailTool, ReadEmailsTool


class TestSendEmailTool:
    """send_email tool tests with mocked SMTP."""

    def _smtp_env(self, host: str = "localhost") -> dict:
        return {
            "SMTP_HOST": host,
            "SMTP_PORT": "587",
            "SMTP_USE_TLS": "false",  # Simpler for test
            "EMAIL_USER": "test@example.com",
            "EMAIL_PASSWORD": "secret",
            "EMAIL_FROM": "test@example.com",
        }

    @pytest.mark.asyncio
    async def test_send_email_success(self, online_context):
        """send_email must return success=True when SMTP send succeeds."""
        tool = SendEmailTool()

        get_settings.cache_clear()
        try:
            with patch("agentcore.mcp.tools.email._send_email_sync", return_value={"sent_to": ["recipient@example.com"], "subject": "Test Subject"}):
                with patch.dict("os.environ", self._smtp_env()):
                    result = await tool.execute(
                        {
                            "to": ["recipient@example.com"],
                            "subject": "Test Subject",
                            "body": "Hello from test",
                        },
                        online_context,
                    )
        finally:
            get_settings.cache_clear()

        assert result.success is True
        assert result.content["subject"] == "Test Subject"

    @pytest.mark.asyncio
    async def test_send_email_smtp_auth_failure(self, online_context):
        """SMTP auth failure must return success=False gracefully."""
        tool = SendEmailTool()
        import smtplib

        with patch("agentcore.mcp.tools.email._send_email_sync", side_effect=smtplib.SMTPAuthenticationError(535, b"Auth failed")):
            with patch.dict("os.environ", self._smtp_env()):
                result = await tool.execute(
                    {
                        "to": ["recipient@example.com"],
                        "subject": "Test",
                        "body": "Body",
                    },
                    online_context,
                )

        assert result.success is False
        assert result.error is not None

    @pytest.mark.asyncio
    async def test_send_email_no_host_configured(self, online_context):
        """No SMTP_HOST must return success=False."""
        tool = SendEmailTool()
        with patch.dict("os.environ", {"SMTP_HOST": "", "EMAIL_USER": "", "EMAIL_PASSWORD": ""}):
            result = await tool.execute(
                {"to": ["a@b.com"], "subject": "X", "body": "Y"},
                online_context,
            )
        assert result.success is False

    @pytest.mark.asyncio
    async def test_send_email_with_cc(self, online_context):
        """send_email must handle CC recipients correctly."""
        tool = SendEmailTool()

        with patch("agentcore.mcp.tools.email._send_email_sync", return_value={"sent_to": ["a@b.com", "cc@b.com"], "subject": "CC Test"}):
            with patch.dict("os.environ", self._smtp_env()):
                result = await tool.execute(
                    {
                        "to": ["a@b.com"],
                        "subject": "CC Test",
                        "body": "Body",
                        "cc": ["cc@b.com"],
                    },
                    online_context,
                )

        assert result.success is True
        assert "cc@b.com" in result.content["sent_to"]

    @pytest.mark.asyncio
    async def test_send_email_smtp_connection_refused(self, online_context):
        """Connection refused to SMTP server must return success=False."""
        tool = SendEmailTool()
        import socket

        with patch("agentcore.mcp.tools.email._send_email_sync", side_effect=ConnectionRefusedError("Connection refused")):
            with patch.dict("os.environ", self._smtp_env()):
                result = await tool.execute(
                    {"to": ["a@b.com"], "subject": "X", "body": "Y"},
                    online_context,
                )

        assert result.success is False


class TestReadEmailsTool:
    """read_emails tool tests with mocked IMAP."""

    def _imap_env(self) -> dict:
        return {
            "IMAP_HOST": "localhost",
            "IMAP_PORT": "993",
            "IMAP_USE_SSL": "false",
            "EMAIL_USER": "test@example.com",
            "EMAIL_PASSWORD": "secret",
        }

    @pytest.mark.asyncio
    async def test_read_emails_success(self, online_context):
        """read_emails must return a list of emails on success."""
        tool = ReadEmailsTool()
        mock_messages = [
            {"id": "1", "from": "a@b.com", "to": "test@example.com", "subject": "Hello", "date": "Mon, 1 Jan 2026", "body": "Test body"},
        ]

        with patch("agentcore.mcp.tools.email._read_emails_sync", return_value=mock_messages):
            with patch.dict("os.environ", self._imap_env()):
                result = await tool.execute({}, online_context)

        assert result.success is True
        assert result.content["count"] == 1
        assert result.content["emails"][0]["subject"] == "Hello"

    @pytest.mark.asyncio
    async def test_read_emails_auth_failure(self, online_context):
        """IMAP auth failure must return success=False."""
        tool = ReadEmailsTool()
        import imaplib

        with patch("agentcore.mcp.tools.email._read_emails_sync", side_effect=imaplib.IMAP4.error("Authentication failed")):
            with patch.dict("os.environ", self._imap_env()):
                result = await tool.execute({}, online_context)

        assert result.success is False

    @pytest.mark.asyncio
    async def test_read_emails_no_host(self, online_context):
        """No IMAP_HOST must return success=False."""
        tool = ReadEmailsTool()
        with patch.dict("os.environ", {"IMAP_HOST": "", "EMAIL_USER": "", "EMAIL_PASSWORD": ""}):
            result = await tool.execute({}, online_context)
        assert result.success is False

    @pytest.mark.asyncio
    async def test_read_emails_with_limit(self, online_context):
        """limit parameter must be passed through correctly."""
        tool = ReadEmailsTool()

        with patch("agentcore.mcp.tools.email._read_emails_sync", return_value=[]) as mock_fn:
            with patch.dict("os.environ", self._imap_env()):
                await tool.execute({"limit": 5}, online_context)

        # Verify limit was passed
        call_args = mock_fn.call_args
        assert call_args is not None
        assert 5 in call_args[0] or call_args[1].get("limit") == 5 or call_args[0][1] == 5

    @pytest.mark.asyncio
    async def test_read_emails_unread_only_flag(self, online_context):
        """unread_only=True must be passed through to the sync function."""
        tool = ReadEmailsTool()

        with patch("agentcore.mcp.tools.email._read_emails_sync", return_value=[]) as mock_fn:
            with patch.dict("os.environ", self._imap_env()):
                await tool.execute({"unread_only": True}, online_context)

        call_args = mock_fn.call_args
        # unread_only=True should be in the positional or keyword args
        assert True in call_args[0] or call_args[1].get("unread_only") is True
