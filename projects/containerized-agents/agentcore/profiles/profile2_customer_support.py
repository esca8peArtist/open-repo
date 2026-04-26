"""
Profile 2: Customer Support
Hardware: Tier 1 (8GB RAM)
Primary model: qwen2.5:7b-instruct + RAG over company knowledge base

All inference is fully offline. Email alerts use SMTP (LAN-capable).
Ticket tracking uses a local SQLite DB via query_database.
business_hours and company_name are populated during the setup wizard.
"""
from __future__ import annotations

from agentcore.models import AgentConfig, AgentProfile, ChannelConfig, ChannelType, ToolConfig

SYSTEM_PROMPT = """You are a professional customer support agent for {company_name}.
You help customers with questions, issues, and requests based on the company knowledge base.

Guidelines:
- Always be polite, empathetic, and solution-oriented
- Use the knowledge base (RAG) to find accurate answers — don't guess
- For issues you cannot resolve, create a support ticket and escalate
- Respect business hours: {business_hours} — if outside hours, let customer know
- Never share internal information, pricing details not in the KB, or competitor comparisons
- If a customer is frustrated, acknowledge their frustration first before providing solutions

You have access to: company knowledge base, ticketing system, email notifications."""

PROFILE_2_CONFIG = AgentConfig(
    name="Customer Support",
    profile=AgentProfile.CUSTOMER_SUPPORT,
    model="qwen2.5:7b-instruct",
    fallback_model=None,  # Tier 1 is the minimum; no lighter fallback needed
    system_prompt=SYSTEM_PROMPT,
    tools=[
        ToolConfig(
            name="read_file",
            description="Read a document from the company knowledge base (/data/company_kb/).",
            enabled=True,
            requires_internet=False,
        ),
        ToolConfig(
            name="search_files",
            description="Search the company knowledge base by filename or content.",
            enabled=True,
            requires_internet=False,
        ),
        ToolConfig(
            name="send_email",
            description="Send email alerts to the support team via SMTP.",
            enabled=True,
            requires_internet=False,
        ),
        ToolConfig(
            name="schedule_task",
            description="Schedule follow-up reminders for open tickets.",
            enabled=True,
            requires_internet=False,
        ),
        ToolConfig(
            name="query_database",
            description=(
                "Query the local SQLite ticket database to look up, create, "
                "or update support tickets."
            ),
            enabled=True,
            requires_internet=False,
            config={"db_path": "/data/tickets/tickets.db"},
        ),
    ],
    channels=[
        ChannelConfig(channel_type=ChannelType.WEB, enabled=True),
        ChannelConfig(channel_type=ChannelType.VOICE, enabled=True),
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
    rag_collection="company_kb",
    active=True,
    metadata={
        "company_name": "",           # populated during setup wizard
        "business_hours": "Mon-Fri 9am-5pm",
        "escalation_email": "",       # support team email set during wizard
        "ticket_db_path": "/data/tickets/tickets.db",
    },
)
