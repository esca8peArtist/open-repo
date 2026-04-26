"""
Calendar MCP tools — CalDAV backend.

Tools
-----
get_calendar_events   — fetch events in a date range
create_calendar_event — create a new event

Backend: caldav library (works with Google Calendar, Nextcloud, Apple Calendar).

Config (env vars)
-----------------
CALDAV_URL       — e.g. https://caldav.example.com/dav/
CALDAV_USERNAME
CALDAV_PASSWORD

Profiles: personal_productivity (1), customer_support (2)
"""
from __future__ import annotations

import logging
from datetime import datetime, timezone
from typing import Any

from agentcore.config import get_settings
from agentcore.mcp.protocol import MCPContext, MCPTool, MCPToolResult, MCPToolSchema

logger = logging.getLogger(__name__)

_PROFILES = ["personal_productivity", "customer_support"]


def _get_caldav_client():
    """Return an authenticated caldav.DAVClient, or raise if not configured."""
    try:
        import caldav  # type: ignore[import]
    except ImportError as exc:
        raise RuntimeError("caldav library is not installed. Run: pip install caldav") from exc

    s = get_settings()
    url = s.caldav_url
    username = s.caldav_username
    password = s.caldav_password

    if not url:
        raise RuntimeError("CALDAV_URL environment variable is not set.")

    return caldav.DAVClient(url=url, username=username, password=password)


# ---------------------------------------------------------------------------
# Tool 1: get_calendar_events
# ---------------------------------------------------------------------------


class GetCalendarEventsTool(MCPTool):
    """Fetch calendar events within a date range."""

    @property
    def schema(self) -> MCPToolSchema:
        return MCPToolSchema(
            name="get_calendar_events",
            description=(
                "Retrieve calendar events between start_date and end_date. "
                "Optionally filter by calendar_id. Returns a list of events with "
                "title, start, end, description, and attendees."
            ),
            input_schema={
                "type": "object",
                "properties": {
                    "start_date": {
                        "type": "string",
                        "description": "Start of the date range (ISO 8601, e.g. '2026-03-01T00:00:00').",
                    },
                    "end_date": {
                        "type": "string",
                        "description": "End of the date range (ISO 8601, e.g. '2026-03-31T23:59:59').",
                    },
                    "calendar_id": {
                        "type": "string",
                        "description": "Optional calendar identifier/name to filter by.",
                    },
                },
                "required": ["start_date", "end_date"],
            },
            requires_internet=True,
            profiles=_PROFILES,
        )

    async def execute(self, arguments: dict, context: MCPContext) -> MCPToolResult:
        if not context.is_online:
            return MCPToolResult(
                success=False,
                content=None,
                error="Calendar requires internet connection",
            )

        start_str: str = arguments["start_date"]
        end_str: str = arguments["end_date"]
        calendar_id: str | None = arguments.get("calendar_id")

        try:
            start_dt = datetime.fromisoformat(start_str).replace(tzinfo=timezone.utc)
            end_dt = datetime.fromisoformat(end_str).replace(tzinfo=timezone.utc)
        except ValueError as exc:
            return MCPToolResult(success=False, content=None, error=f"Invalid date format: {exc}")

        try:
            client = _get_caldav_client()
            principal = client.principal()

            calendars = principal.calendars()
            if calendar_id:
                calendars = [c for c in calendars if calendar_id in (c.name or "")]

            events: list[dict] = []
            for cal in calendars:
                try:
                    cal_events = cal.date_search(start=start_dt, end=end_dt, expand=True)
                    for event in cal_events:
                        comp = event.vobject_instance.vevent
                        events.append(
                            {
                                "title": str(getattr(comp, "summary", {}).value or ""),
                                "start": str(getattr(comp, "dtstart", {}).value or ""),
                                "end": str(getattr(comp, "dtend", {}).value or ""),
                                "description": str(getattr(comp, "description", {}).value or ""),
                                "location": str(getattr(comp, "location", {}).value or ""),
                                "calendar": cal.name or "",
                            }
                        )
                except Exception as exc:
                    logger.warning("Error fetching events from calendar '%s': %s", cal.name, exc)

            return MCPToolResult(success=True, content={"events": events, "count": len(events)})

        except Exception as exc:
            logger.error("get_calendar_events error: %s", exc)
            return MCPToolResult(success=False, content=None, error=str(exc))


# ---------------------------------------------------------------------------
# Tool 2: create_calendar_event
# ---------------------------------------------------------------------------


class CreateCalendarEventTool(MCPTool):
    """Create a new calendar event via CalDAV."""

    @property
    def schema(self) -> MCPToolSchema:
        return MCPToolSchema(
            name="create_calendar_event",
            description=(
                "Create a new event on the default CalDAV calendar. "
                "Returns the created event's UID."
            ),
            input_schema={
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "Event title/summary.",
                    },
                    "start": {
                        "type": "string",
                        "description": "Event start datetime (ISO 8601).",
                    },
                    "end": {
                        "type": "string",
                        "description": "Event end datetime (ISO 8601).",
                    },
                    "description": {
                        "type": "string",
                        "description": "Optional event description/notes.",
                    },
                    "attendees": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Optional list of attendee email addresses.",
                    },
                },
                "required": ["title", "start", "end"],
            },
            requires_internet=True,
            profiles=_PROFILES,
        )

    async def execute(self, arguments: dict, context: MCPContext) -> MCPToolResult:
        if not context.is_online:
            return MCPToolResult(
                success=False,
                content=None,
                error="Calendar requires internet connection",
            )

        title: str = arguments["title"]
        start_str: str = arguments["start"]
        end_str: str = arguments["end"]
        description: str = arguments.get("description", "")
        attendees: list[str] = arguments.get("attendees", [])

        try:
            start_dt = datetime.fromisoformat(start_str)
            end_dt = datetime.fromisoformat(end_str)
        except ValueError as exc:
            return MCPToolResult(success=False, content=None, error=f"Invalid date format: {exc}")

        try:
            import uuid

            import caldav  # type: ignore[import]
            from icalendar import Calendar, Event  # type: ignore[import]

            client = _get_caldav_client()
            principal = client.principal()
            calendars = principal.calendars()
            if not calendars:
                return MCPToolResult(success=False, content=None, error="No calendars found.")

            cal = calendars[0]

            uid = str(uuid.uuid4())
            ical = Calendar()
            ical.add("prodid", "-//AgentCore//MCP//EN")
            ical.add("version", "2.0")

            event = Event()
            event.add("uid", uid)
            event.add("summary", title)
            event.add("dtstart", start_dt)
            event.add("dtend", end_dt)
            event.add("dtstamp", datetime.now(timezone.utc))
            if description:
                event.add("description", description)
            for email in attendees:
                event.add("attendee", f"mailto:{email}")

            ical.add_component(event)
            cal.add_event(ical.to_ical().decode())

            return MCPToolResult(
                success=True,
                content={"uid": uid, "title": title, "start": start_str, "end": end_str},
            )

        except Exception as exc:
            logger.error("create_calendar_event error: %s", exc)
            return MCPToolResult(success=False, content=None, error=str(exc))
