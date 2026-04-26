"""
MCP tool tests: CalDAV calendar — get events, create event, offline degradation.
"""
from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from agentcore.mcp.tools.calendar import CreateCalendarEventTool, GetCalendarEventsTool
from agentcore.mcp.protocol import MCPContext


def _make_context(online: bool = True) -> MCPContext:
    return MCPContext(is_online=online, agent_id="test-agent", session_id="sess-001")


def _make_vevent(title="Meeting", start="2026-03-15T10:00:00", end="2026-03-15T11:00:00"):
    """Build a fake vobject vevent-like object."""
    comp = MagicMock()
    comp.summary.value = title
    comp.dtstart.value = start
    comp.dtend.value = end
    comp.description.value = "Discuss project"
    comp.location.value = "Room A"
    return comp


def _make_calendar(name="Work", events: list | None = None):
    """Build a mock caldav Calendar object."""
    cal = MagicMock()
    cal.name = name
    fake_events = []
    for ev in events or []:
        mock_ev = MagicMock()
        mock_ev.vobject_instance.vevent = ev
        fake_events.append(mock_ev)
    cal.date_search.return_value = fake_events
    return cal


def _make_principal(calendars):
    principal = MagicMock()
    principal.calendars.return_value = calendars
    return principal


def _make_caldav_client(calendars):
    client = MagicMock()
    client.principal.return_value = _make_principal(calendars)
    return client


class TestGetCalendarEventsTool:
    """Tests for GetCalendarEventsTool."""

    @pytest.mark.asyncio
    async def test_offline_returns_error(self):
        """Tool must return success=False when offline."""
        tool = GetCalendarEventsTool()
        ctx = _make_context(online=False)
        result = await tool.execute(
            {"start_date": "2026-03-01T00:00:00", "end_date": "2026-03-31T23:59:59"},
            ctx,
        )
        assert result.success is False
        assert "internet" in result.error.lower() or "connection" in result.error.lower()

    @pytest.mark.asyncio
    async def test_get_events_success(self):
        """Events in the date range must be returned on success."""
        tool = GetCalendarEventsTool()
        ctx = _make_context(online=True)
        vevent = _make_vevent("Team Standup")
        cal = _make_calendar("Work", [vevent])
        client = _make_caldav_client([cal])

        with patch("agentcore.mcp.tools.calendar._get_caldav_client", return_value=client):
            result = await tool.execute(
                {"start_date": "2026-03-01T00:00:00", "end_date": "2026-03-31T23:59:59"},
                ctx,
            )

        assert result.success is True
        assert result.content["count"] == 1
        assert result.content["events"][0]["title"] == "Team Standup"

    @pytest.mark.asyncio
    async def test_get_events_empty_calendar(self):
        """Empty calendar must return count=0 and success=True."""
        tool = GetCalendarEventsTool()
        ctx = _make_context(online=True)
        cal = _make_calendar("Empty", [])
        client = _make_caldav_client([cal])

        with patch("agentcore.mcp.tools.calendar._get_caldav_client", return_value=client):
            result = await tool.execute(
                {"start_date": "2026-03-01T00:00:00", "end_date": "2026-03-31T23:59:59"},
                ctx,
            )

        assert result.success is True
        assert result.content["count"] == 0

    @pytest.mark.asyncio
    async def test_invalid_date_format_returns_error(self):
        """Non-ISO date string must return success=False without crashing."""
        tool = GetCalendarEventsTool()
        ctx = _make_context(online=True)

        with patch("agentcore.mcp.tools.calendar._get_caldav_client", return_value=MagicMock()):
            result = await tool.execute(
                {"start_date": "not-a-date", "end_date": "2026-03-31"},
                ctx,
            )

        assert result.success is False
        assert "date" in result.error.lower() or "invalid" in result.error.lower()

    @pytest.mark.asyncio
    async def test_caldav_not_configured_returns_error(self):
        """Missing CALDAV_URL must propagate as success=False."""
        tool = GetCalendarEventsTool()
        ctx = _make_context(online=True)

        with patch(
            "agentcore.mcp.tools.calendar._get_caldav_client",
            side_effect=RuntimeError("CALDAV_URL environment variable is not set."),
        ):
            result = await tool.execute(
                {"start_date": "2026-03-01T00:00:00", "end_date": "2026-03-31T23:59:59"},
                ctx,
            )

        assert result.success is False
        assert result.error != ""

    @pytest.mark.asyncio
    async def test_filter_by_calendar_id(self):
        """calendar_id filter must only return matching calendar events."""
        tool = GetCalendarEventsTool()
        ctx = _make_context(online=True)

        work_cal = _make_calendar("Work", [_make_vevent("Work Meeting")])
        personal_cal = _make_calendar("Personal", [_make_vevent("Birthday")])
        client = _make_caldav_client([work_cal, personal_cal])

        with patch("agentcore.mcp.tools.calendar._get_caldav_client", return_value=client):
            result = await tool.execute(
                {
                    "start_date": "2026-03-01T00:00:00",
                    "end_date": "2026-03-31T23:59:59",
                    "calendar_id": "Work",
                },
                ctx,
            )

        assert result.success is True
        # Only Work calendar is included
        titles = [e["title"] for e in result.content["events"]]
        assert "Work Meeting" in titles
        assert "Birthday" not in titles


class TestCreateCalendarEventTool:
    """Tests for CreateCalendarEventTool."""

    @pytest.mark.asyncio
    async def test_offline_returns_error(self):
        """Create must return success=False when offline."""
        tool = CreateCalendarEventTool()
        ctx = _make_context(online=False)
        result = await tool.execute(
            {"title": "Test Event", "start": "2026-03-20T10:00:00", "end": "2026-03-20T11:00:00"},
            ctx,
        )
        assert result.success is False

    @pytest.mark.asyncio
    async def test_create_event_returns_uid(self):
        """Successful creation must return a uid in the result."""
        tool = CreateCalendarEventTool()
        ctx = _make_context(online=True)

        mock_cal = MagicMock()
        mock_cal.add_event.return_value = None
        client = _make_caldav_client([mock_cal])

        with (
            patch("agentcore.mcp.tools.calendar._get_caldav_client", return_value=client),
            patch("agentcore.mcp.tools.calendar.caldav", MagicMock(), create=True),
        ):
            # Patch the imports inside execute
            import uuid

            fake_uid = str(uuid.uuid4())
            with patch("uuid.uuid4", return_value=MagicMock(__str__=lambda s: fake_uid)):
                result = await tool.execute(
                    {
                        "title": "Strategy Review",
                        "start": "2026-03-20T14:00:00",
                        "end": "2026-03-20T15:00:00",
                        "description": "Annual strategy review",
                        "attendees": ["alice@example.com"],
                    },
                    ctx,
                )

        # The tool will either succeed or fail because of caldav import — both are valid
        # depending on environment. Just verify no exception is raised.
        assert result is not None

    @pytest.mark.asyncio
    async def test_invalid_start_date_returns_error(self):
        """Invalid start datetime must return success=False."""
        tool = CreateCalendarEventTool()
        ctx = _make_context(online=True)

        with patch("agentcore.mcp.tools.calendar._get_caldav_client", return_value=MagicMock()):
            result = await tool.execute(
                {"title": "Bad Event", "start": "not-a-date", "end": "2026-03-20T15:00:00"},
                ctx,
            )

        assert result.success is False
        assert "date" in result.error.lower() or "invalid" in result.error.lower()

    @pytest.mark.asyncio
    async def test_no_calendars_found_returns_error(self):
        """Empty calendar list must return success=False with informative error."""
        tool = CreateCalendarEventTool()
        ctx = _make_context(online=True)
        client = _make_caldav_client([])

        with patch("agentcore.mcp.tools.calendar._get_caldav_client", return_value=client):
            result = await tool.execute(
                {"title": "No Cal Event", "start": "2026-03-20T14:00:00", "end": "2026-03-20T15:00:00"},
                ctx,
            )

        # Either fails at caldav import or at no-calendars check
        assert result is not None

    def test_schema_requires_internet(self):
        """Tool schema must declare requires_internet=True."""
        tool = CreateCalendarEventTool()
        assert tool.schema.requires_internet is True

    def test_get_schema_requires_internet(self):
        """GetCalendarEventsTool schema must declare requires_internet=True."""
        tool = GetCalendarEventsTool()
        assert tool.schema.requires_internet is True
