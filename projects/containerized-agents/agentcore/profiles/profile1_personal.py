"""
Profile 1: Personal Productivity
Hardware: Tier 1 (8GB RAM)
Primary model: qwen2.5:7b-instruct
Fallback model: phi4-mini (for Tier 1 with less RAM, e.g. 4–6GB)

Tools (all offline-capable except web_search and calendar tools):
  - get_calendar_events / create_calendar_event  (CalDAV — requires internet)
  - send_email / read_emails                     (IMAP/SMTP — LAN-capable)
  - web_search                                   (requires internet — degrades gracefully)
  - schedule_task / list_scheduled_tasks / cancel_task  (local scheduler)
  - read_file / search_files                     (personal docs in /data/personal/)

Channels: web, voice (always offline), telegram/sms/whatsapp (online only)
"""
from __future__ import annotations

from agentcore.models import AgentConfig, AgentProfile, ChannelConfig, ChannelType, ToolConfig

SYSTEM_PROMPT = """You are a personal productivity assistant. You help with:
- Managing calendar events and scheduling
- Drafting and managing emails
- Searching personal documents and notes (via RAG)
- Web research and summaries (when internet available)
- Setting reminders and scheduling tasks

You are direct, efficient, and respect the user's time. Keep responses concise.
When internet is unavailable, you note this and help with what you can offline."""

PROFILE_1_CONFIG = AgentConfig(
    name="Personal Assistant",
    profile=AgentProfile.PERSONAL_PRODUCTIVITY,
    model="qwen2.5:7b-instruct",
    fallback_model="phi4-mini",
    system_prompt=SYSTEM_PROMPT,
    tools=[
        ToolConfig(
            name="get_calendar_events",
            description="Retrieve upcoming calendar events from CalDAV.",
            enabled=True,
            requires_internet=True,
        ),
        ToolConfig(
            name="create_calendar_event",
            description="Create a new calendar event in CalDAV.",
            enabled=True,
            requires_internet=True,
        ),
        ToolConfig(
            name="send_email",
            description="Send an email via IMAP/SMTP (works on LAN mail servers).",
            enabled=True,
            requires_internet=False,
        ),
        ToolConfig(
            name="read_emails",
            description="Read emails from the configured IMAP account.",
            enabled=True,
            requires_internet=False,
        ),
        ToolConfig(
            name="web_search",
            description="Search the web for information. Requires internet — degrades gracefully when offline.",
            enabled=True,
            requires_internet=True,
        ),
        ToolConfig(
            name="schedule_task",
            description="Schedule a future task or reminder (local scheduler).",
            enabled=True,
            requires_internet=False,
        ),
        ToolConfig(
            name="list_scheduled_tasks",
            description="List all pending scheduled tasks and reminders.",
            enabled=True,
            requires_internet=False,
        ),
        ToolConfig(
            name="cancel_task",
            description="Cancel a previously scheduled task by ID.",
            enabled=True,
            requires_internet=False,
        ),
        ToolConfig(
            name="read_file",
            description="Read a personal document from /data/personal/.",
            enabled=True,
            requires_internet=False,
        ),
        ToolConfig(
            name="search_files",
            description="Search personal documents and notes by filename or content.",
            enabled=True,
            requires_internet=False,
        ),
    ],
    channels=[
        ChannelConfig(channel_type=ChannelType.WEB, enabled=True),
        ChannelConfig(channel_type=ChannelType.VOICE, enabled=True),
        ChannelConfig(
            channel_type=ChannelType.TELEGRAM,
            enabled=True,
            config={"note": "requires_internet"},
        ),
        ChannelConfig(
            channel_type=ChannelType.SMS,
            enabled=True,
            config={"provider": "twilio", "note": "requires_internet"},
        ),
        ChannelConfig(
            channel_type=ChannelType.WHATSAPP,
            enabled=True,
            config={"provider": "twilio", "note": "requires_internet"},
        ),
    ],
    hardware_tier=1,
    rag_enabled=True,
    rag_collection="personal_docs",
    # active=False — user enables during the setup wizard
    active=False,
)
