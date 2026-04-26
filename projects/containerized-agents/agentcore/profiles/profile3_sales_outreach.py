"""
Profile 3: Sales Outreach
Hardware: Tier 2 recommended (16GB RAM), Tier 1 fallback with lighter model
Primary model: qwen2.5:14b-instruct  (requires 16GB — Tier 2)
Fallback model: qwen2.5:7b-instruct  (works on 8GB — Tier 1)

CRM-driven outreach via SMS/WhatsApp (Twilio, requires internet) and email.
All scheduling, contact management, and calendar operations are offline.
RAG is disabled — lead context comes from the local CRM database.
"""
from __future__ import annotations

from agentcore.models import AgentConfig, AgentProfile, ChannelConfig, ChannelType, ToolConfig

SYSTEM_PROMPT = """You are a sales outreach agent. Your role is to:
- Engage prospects via SMS and WhatsApp in a professional, personalized way
- Qualify leads based on their responses
- Book meetings and demos on behalf of the sales team
- Follow up with prospects on a scheduled cadence
- Track all interactions in the CRM

Guidelines:
- Keep messages SHORT — this is SMS/WhatsApp, not email
- Be conversational and human, never robotic or pushy
- Always provide value in each message
- Respect opt-out requests immediately and permanently
- Never spam — respect the configured outreach schedule
- Personalize using CRM data (name, company, last interaction)

You represent {company_name}. Your goal: qualify leads and book meetings."""

PROFILE_3_CONFIG = AgentConfig(
    name="Sales Outreach",
    profile=AgentProfile.SALES_OUTREACH,
    model="qwen2.5:14b-instruct",
    fallback_model="qwen2.5:7b-instruct",
    system_prompt=SYSTEM_PROMPT,
    tools=[
        ToolConfig(
            name="search_contacts",
            description="Search CRM contacts by name, company, status, or tag.",
            enabled=True,
            requires_internet=False,
        ),
        ToolConfig(
            name="get_contact",
            description="Retrieve full CRM record for a single contact by ID.",
            enabled=True,
            requires_internet=False,
        ),
        ToolConfig(
            name="add_note",
            description="Add an interaction note to a CRM contact record.",
            enabled=True,
            requires_internet=False,
        ),
        ToolConfig(
            name="update_contact_status",
            description=(
                "Update a contact's lead status in the CRM "
                "(e.g., new → contacted → qualified → meeting_booked → closed)."
            ),
            enabled=True,
            requires_internet=False,
        ),
        ToolConfig(
            name="schedule_task",
            description="Schedule a follow-up outreach task for a contact.",
            enabled=True,
            requires_internet=False,
        ),
        ToolConfig(
            name="list_scheduled_tasks",
            description="List all pending outreach tasks and follow-up reminders.",
            enabled=True,
            requires_internet=False,
        ),
        ToolConfig(
            name="cancel_task",
            description="Cancel a scheduled outreach task (e.g., after opt-out).",
            enabled=True,
            requires_internet=False,
        ),
        ToolConfig(
            name="get_calendar_events",
            description="Check sales team calendar availability for meeting booking.",
            enabled=True,
            requires_internet=True,
        ),
        ToolConfig(
            name="create_calendar_event",
            description="Book a meeting or demo on the sales team calendar.",
            enabled=True,
            requires_internet=True,
        ),
        ToolConfig(
            name="send_email",
            description="Send outreach or follow-up emails via SMTP.",
            enabled=True,
            requires_internet=False,
        ),
    ],
    channels=[
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
        ChannelConfig(channel_type=ChannelType.WEB, enabled=True),
    ],
    hardware_tier=2,
    rag_enabled=False,  # CRM-driven, not document-driven
    rag_collection=None,
    active=True,
    metadata={
        "company_name": "",          # populated during setup wizard
        "outreach_cadence_days": 3,  # days between follow-up attempts
        "max_follow_ups": 3,         # maximum follow-ups per lead before archiving
        "opt_out_keywords": ["stop", "unsubscribe", "remove me", "opt out"],
    },
)
