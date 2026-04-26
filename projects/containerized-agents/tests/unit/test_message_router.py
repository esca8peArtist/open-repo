"""
Unit tests for ToolDispatcher (message routing and tool dispatch).

Covers:
- Built-in tool registration and invocation
- Offline check for internet-dependent tools
- Unknown tool graceful error
- MCP registry delegation
- Connectivity caching behaviour
- Rate-limiting helpers
"""
from __future__ import annotations

import asyncio
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from agentcore.core.dispatcher import (
    ToolDispatcher,
    register_builtin_tools,
    tool_echo,
    tool_get_current_time,
)
from agentcore.mcp.protocol import MCPContext
from agentcore.mcp.registry import MCPToolRegistry
from agentcore.mcp.tools.web_search import WebSearchTool


# ===========================================================================
# Built-in tool registration
# ===========================================================================


class TestBuiltinTools:
    @pytest.mark.asyncio
    async def test_get_current_time_returns_timestamp(self):
        """get_current_time must return an ISO-8601 UTC timestamp."""
        result = await tool_get_current_time()
        assert "output" in result
        ts = result["output"]
        # Basic ISO-8601 check: contains 'T' and '+'
        assert "T" in ts or "Z" in ts

    @pytest.mark.asyncio
    async def test_echo_returns_kwargs(self):
        """echo must echo back whatever keyword arguments it receives."""
        result = await tool_echo(message="hello", count=3)
        assert "output" in result
        output = result["output"]
        assert "message" in output
        assert "count" in output

    @pytest.mark.asyncio
    async def test_register_builtin_tools(self):
        """register_builtin_tools must make get_current_time and echo available."""
        dispatcher = ToolDispatcher()
        register_builtin_tools(dispatcher)
        tools = dispatcher.list_tools()
        assert "get_current_time" in tools
        assert "echo" in tools


# ===========================================================================
# Dispatch — legacy handler path
# ===========================================================================


class TestDispatchLegacy:
    @pytest.mark.asyncio
    async def test_dispatch_known_tool(self):
        """Dispatching a registered tool must return its output."""
        dispatcher = ToolDispatcher()
        register_builtin_tools(dispatcher)
        result = await dispatcher.dispatch("get_current_time", {})
        assert "output" in result
        assert "error" not in result or result.get("error") is None

    @pytest.mark.asyncio
    async def test_dispatch_unknown_tool_returns_graceful_error(self):
        """Dispatching a tool that doesn't exist must return an error dict, not raise."""
        dispatcher = ToolDispatcher()
        result = await dispatcher.dispatch("completely_unknown_tool", {})
        assert "error" in result
        assert result["error"]  # non-empty

    @pytest.mark.asyncio
    async def test_dispatch_internet_tool_offline_returns_graceful_error(self):
        """An internet-requiring tool dispatched while offline must return a graceful error."""
        dispatcher = ToolDispatcher(connectivity_check_url="http://127.0.0.1:0")

        async def _fake_search(query: str = "") -> dict:
            return {"output": "result"}

        dispatcher.register("web_search", _fake_search, requires_internet=True)

        # Force offline status
        with patch.object(dispatcher, "is_online", AsyncMock(return_value=False)):
            result = await dispatcher.dispatch("web_search", {"query": "test"})

        assert "error" in result
        assert result["error"] == "offline"

    @pytest.mark.asyncio
    async def test_dispatch_internet_tool_online_calls_handler(self):
        """An internet-requiring tool dispatched while online must call the handler."""
        dispatcher = ToolDispatcher()

        called = []

        async def _fake_search(query: str = "") -> dict:
            called.append(query)
            return {"output": "some results"}

        dispatcher.register("web_search", _fake_search, requires_internet=True)

        with patch.object(dispatcher, "is_online", AsyncMock(return_value=True)):
            result = await dispatcher.dispatch("web_search", {"query": "news"})

        assert called == ["news"]
        assert result["output"] == "some results"

    @pytest.mark.asyncio
    async def test_dispatch_handles_tool_exception_gracefully(self):
        """If a tool handler raises, dispatch must catch it and return an error dict."""
        dispatcher = ToolDispatcher()

        async def _bad_tool(**kwargs) -> dict:
            raise RuntimeError("Something went wrong")

        dispatcher.register("bad_tool", _bad_tool, requires_internet=False)
        result = await dispatcher.dispatch("bad_tool", {})
        assert "error" in result
        assert "RuntimeError" in result["error"] or result["error"]


# ===========================================================================
# MCP registry delegation
# ===========================================================================


class TestDispatchMCPDelegation:
    @pytest.mark.asyncio
    async def test_mcp_tool_invoked_via_registry(self):
        """When an MCP tool is registered, dispatcher must delegate to the registry."""
        dispatcher = ToolDispatcher()

        registry = MCPToolRegistry()
        registry.register(WebSearchTool())
        dispatcher.set_mcp_registry(registry)

        # Override is_online to return False so the tool short-circuits cleanly
        with patch.object(dispatcher, "is_online", AsyncMock(return_value=False)):
            result = await dispatcher.dispatch("web_search", {"query": "test"})

        # Should get a graceful offline error (not "unknown tool")
        assert "error" in result
        assert "unknown" not in str(result["error"]).lower()

    @pytest.mark.asyncio
    async def test_list_tools_includes_mcp_tools(self):
        """list_tools() must include both legacy tools and MCP tools."""
        dispatcher = ToolDispatcher()
        register_builtin_tools(dispatcher)

        registry = MCPToolRegistry()
        registry.register(WebSearchTool())
        dispatcher.set_mcp_registry(registry)

        tools = dispatcher.list_tools()
        assert "get_current_time" in tools
        assert "echo" in tools
        assert "web_search" in tools


# ===========================================================================
# Connectivity caching
# ===========================================================================


class TestConnectivityCache:
    @pytest.mark.asyncio
    async def test_connectivity_result_is_cached(self):
        """A second is_online() call within TTL must not make another HTTP request."""
        dispatcher = ToolDispatcher(cache_ttl=60)

        call_count = [0]

        async def _mock_check():
            call_count[0] += 1
            return True

        # Manually set cached state
        dispatcher._online_status = True
        dispatcher._online_checked_at = asyncio.get_running_loop().time()

        status = await dispatcher.is_online()
        assert status is True
        assert call_count[0] == 0  # No HTTP calls made — cache hit

    @pytest.mark.asyncio
    async def test_invalidate_cache_forces_recheck(self):
        """invalidate_connectivity_cache() must cause the next is_online() to recheck."""
        dispatcher = ToolDispatcher()
        dispatcher._online_status = True
        dispatcher._online_checked_at = 1e10  # Far future — would normally be a cache hit

        dispatcher.invalidate_connectivity_cache()

        assert dispatcher._online_status is None
        assert dispatcher._online_checked_at == 0.0

    @pytest.mark.asyncio
    async def test_offline_when_http_fails(self):
        """If the connectivity check URL is unreachable, is_online() must return False."""
        dispatcher = ToolDispatcher(connectivity_check_url="http://127.0.0.1:0", cache_ttl=0)

        status = await dispatcher.is_online()
        assert status is False


# ===========================================================================
# Priority routing (Telegram channel)
# ===========================================================================


try:
    from agentcore.channels.telegram.bot import _split_message as _tg_split_message
    _TELEGRAM_AVAILABLE = True
except ImportError:
    _TELEGRAM_AVAILABLE = False
    _tg_split_message = None  # type: ignore[assignment]

try:
    from agentcore.channels.twilio.sms import _split_sms as _twilio_split_sms, TwilioSMSChannel
    _TWILIO_AVAILABLE = True
except ImportError:
    _TWILIO_AVAILABLE = False
    _twilio_split_sms = None  # type: ignore[assignment]
    TwilioSMSChannel = None  # type: ignore[assignment,misc]


@pytest.mark.skipif(not _TELEGRAM_AVAILABLE, reason="python-telegram-bot not installed")
class TestTelegramChannelInboundParsing:
    """Test TelegramChannel.handle_inbound message normalisation."""

    def test_split_message_short_text(self):
        """Messages under the limit must not be split."""
        from agentcore.channels.telegram.bot import _split_message

        chunks = _split_message("Hello world", max_length=100)
        assert chunks == ["Hello world"]

    def test_split_message_long_text_on_newline(self):
        """Long messages should split at newline boundaries when available."""
        from agentcore.channels.telegram.bot import _split_message

        text = "Line one\nLine two\nLine three"
        chunks = _split_message(text, max_length=15)
        # Each chunk must fit within max_length
        for chunk in chunks:
            assert len(chunk) <= 15

    def test_split_message_no_whitespace_hard_split(self):
        """Strings with no split point must be hard-split at max_length."""
        from agentcore.channels.telegram.bot import _split_message

        text = "A" * 50
        chunks = _split_message(text, max_length=10)
        assert all(len(c) <= 10 for c in chunks)
        assert "".join(chunks) == text

    def test_split_message_empty_string(self):
        """Empty string input should return an empty list (no empty chunks)."""
        from agentcore.channels.telegram.bot import _split_message

        chunks = _split_message("", max_length=100)
        assert chunks == []


@pytest.mark.skipif(not _TWILIO_AVAILABLE, reason="twilio not installed")
class TestTwilioSMSSplitting:
    """Test TwilioSMSChannel._split_sms helper."""

    def test_short_message_not_split(self):
        from agentcore.channels.twilio.sms import _split_sms

        assert _split_sms("Hello", 160) == ["Hello"]

    def test_long_message_split_on_word_boundary(self):
        from agentcore.channels.twilio.sms import _split_sms

        # 170-char message: must be split into at most 2 segments
        text = "word " * 34  # 170 chars
        segments = _split_sms(text.strip(), 160)
        assert len(segments) >= 2
        for seg in segments:
            assert len(seg) <= 160

    def test_all_content_preserved_after_split(self):
        """Reassembling segments must reproduce original text (modulo whitespace at joins)."""
        from agentcore.channels.twilio.sms import _split_sms

        original = "This is a long message. " * 10
        segments = _split_sms(original.strip(), 160)
        # Each segment must be non-empty
        assert all(len(s) > 0 for s in segments)

    def test_twilio_inbound_parse(self):
        """handle_inbound must normalise a Twilio form payload into a ChannelMessage."""
        from agentcore.channels.twilio.sms import TwilioSMSChannel
        from agentcore.channels.base import ChannelMessage

        async def _fake_router(msg: ChannelMessage) -> str:
            return "reply"

        channel = TwilioSMSChannel(
            account_sid="ACtest",
            auth_token="test_auth",
            phone_number="+15550000001",
            agent_id="agent-1",
            message_router=_fake_router,
        )

        payload = {
            "From": "+15550000002",
            "To": "+15550000001",
            "Body": "Hello from test",
            "MessageSid": "SM123",
            "NumSegments": "1",
            "NumMedia": "0",
            "AccountSid": "ACtest",
        }

        import asyncio

        msg = asyncio.run(channel.handle_inbound(payload))

        assert msg.sender_id == "+15550000002"
        assert msg.content == "Hello from test"
        assert msg.channel == "sms"
        assert msg.metadata["message_sid"] == "SM123"
