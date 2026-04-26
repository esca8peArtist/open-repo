"""
Profile 6: Enterprise Orchestrator
Hardware: Tier 4 (64GB+ RAM, DGX Spark or equivalent)
Orchestrator model: qwen3:72b (quantized, Apache 2.0)
Sub-agent model: qwen2.5:7b-instruct (multiple parallel instances, Apache 2.0)
Requires: Redis (multi-agent message bus via agentcore:bus:enterprise)

The orchestrator decomposes incoming enterprise requests into sub-tasks, dispatches
them to specialized sub-agents (customer support, sales), aggregates results, and
delivers a coherent final response.

All significant actions are written to the audit log (PostgreSQL).
User role-based access control is enforced before any action is taken.
"""
from __future__ import annotations

from agentcore.models import (
    AgentConfig,
    AgentProfile,
    ChannelConfig,
    ChannelType,
    ToolConfig,
)

# ---------------------------------------------------------------------------
# System prompt
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """You are an enterprise AI orchestrator managing a team of specialized AI sub-agents.

Your role:
- Decompose complex enterprise requests into parallel sub-tasks
- Delegate to the right specialized agent (customer support, sales, BI, developer)
- Aggregate results and deliver coherent responses
- Monitor all agents and escalate failures
- Maintain audit log of all significant actions
- Manage multi-user access across the organization

Enterprise guidelines:
- All significant actions are logged to the audit trail
- User permissions are enforced — check role before acting
- Prefer parallel execution of independent tasks
- For ambiguous requests, clarify before acting
- Escalate to human administrators for: data deletion, permission changes, financial actions > threshold
- Maintain confidentiality: users only see data appropriate to their role

You coordinate: {active_agent_names}"""

# ---------------------------------------------------------------------------
# Sub-agent configs
# ---------------------------------------------------------------------------

SUBAGENT_CONFIGS: list[AgentConfig] = [
    # Customer Support sub-agent — handles customer queries via company KB
    AgentConfig(
        name="CS Sub-Agent",
        profile=AgentProfile.CUSTOMER_SUPPORT,
        model="qwen2.5:7b-instruct",
        fallback_model=None,
        system_prompt=(
            "You are a customer support specialist operating as part of an enterprise AI team. "
            "Handle customer queries efficiently using the company knowledge base and ticket database. "
            "Escalate to the orchestrator when: the question is out of scope, "
            "the customer is escalating, or a refund/exception is requested."
        ),
        tools=[
            ToolConfig(
                name="read_file",
                description="Read files from the company knowledge base directory.",
                enabled=True,
                requires_internet=False,
            ),
            ToolConfig(
                name="search_files",
                description="Search files in the knowledge base by glob pattern.",
                enabled=True,
                requires_internet=False,
            ),
            ToolConfig(
                name="query_database",
                description="Query the ticket database (read-only) to look up customer history.",
                enabled=True,
                requires_internet=False,
            ),
            ToolConfig(
                name="send_email",
                description="Send resolution emails to customers. Requires internet.",
                enabled=True,
                requires_internet=True,
            ),
            ToolConfig(
                name="schedule_task",
                description="Schedule a follow-up task or reminder.",
                enabled=True,
                requires_internet=False,
            ),
        ],
        channels=[],    # no direct channel — orchestrator routes all messages
        hardware_tier=4,
        rag_enabled=True,
        rag_collection="company_kb",
        active=True,
        metadata={
            "role": "customer_support",
            "escalation_keywords": ["refund", "cancel", "legal", "manager", "complaint"],
        },
    ),

    # Sales sub-agent — lead qualification, CRM updates, meeting booking
    AgentConfig(
        name="Sales Sub-Agent",
        profile=AgentProfile.SALES_OUTREACH,
        model="qwen2.5:7b-instruct",
        fallback_model=None,
        system_prompt=(
            "You are a sales specialist. Handle lead qualification, CRM updates, and "
            "meeting scheduling as directed by the orchestrator. "
            "Always verify a contact exists before updating. "
            "Do not disclose deal values or pipeline data to non-sales roles."
        ),
        tools=[
            ToolConfig(
                name="search_contacts",
                description="Search the CRM for contacts by name, email, or company.",
                enabled=True,
                requires_internet=False,
            ),
            ToolConfig(
                name="get_contact",
                description="Retrieve full contact details and history from the CRM.",
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
                description="Update a CRM contact's pipeline stage or status.",
                enabled=True,
                requires_internet=False,
            ),
            ToolConfig(
                name="schedule_task",
                description="Schedule a follow-up task for a lead.",
                enabled=True,
                requires_internet=False,
            ),
            ToolConfig(
                name="create_calendar_event",
                description="Book a sales call or demo on the calendar.",
                enabled=True,
                requires_internet=False,
            ),
        ],
        channels=[],    # orchestrator-routed only
        hardware_tier=4,
        rag_enabled=False,
        active=True,
        metadata={
            "role": "sales",
            "crm_db": "",           # set during wizard
        },
    ),
]

# ---------------------------------------------------------------------------
# Orchestrator config
# ---------------------------------------------------------------------------

PROFILE_6_CONFIG = AgentConfig(
    name="Enterprise Orchestrator",
    profile=AgentProfile.ENTERPRISE_ORCHESTRATOR,
    model="qwen3:72b",
    fallback_model=None,            # no fallback — Tier 4 is required
    system_prompt=SYSTEM_PROMPT,
    tools=[
        # Calendar
        ToolConfig(
            name="get_calendar_events",
            description="Retrieve calendar events for a given date range.",
            enabled=True,
            requires_internet=False,
        ),
        ToolConfig(
            name="create_calendar_event",
            description="Create a new calendar event.",
            enabled=True,
            requires_internet=False,
        ),
        # Email
        ToolConfig(
            name="send_email",
            description="Send an email via SMTP. Requires internet.",
            enabled=True,
            requires_internet=True,
        ),
        ToolConfig(
            name="read_emails",
            description="Read recent emails from the configured IMAP account. Requires internet.",
            enabled=True,
            requires_internet=True,
        ),
        # Web
        ToolConfig(
            name="web_search",
            description="Search the web for external context. Requires internet.",
            enabled=True,
            requires_internet=True,
        ),
        # Database
        ToolConfig(
            name="query_database",
            description="Execute a read-only SQL query against a configured database.",
            enabled=True,
            requires_internet=False,
        ),
        # Code execution
        ToolConfig(
            name="execute_python",
            description="Execute Python code for analysis or automation tasks.",
            enabled=True,
            requires_internet=False,
        ),
        # Reports
        ToolConfig(
            name="generate_pdf_report",
            description="Generate a structured PDF report.",
            enabled=True,
            requires_internet=False,
        ),
        # CRM
        ToolConfig(
            name="search_contacts",
            description="Search CRM contacts.",
            enabled=True,
            requires_internet=False,
        ),
        ToolConfig(
            name="get_contact",
            description="Get full CRM contact details.",
            enabled=True,
            requires_internet=False,
        ),
        ToolConfig(
            name="add_note",
            description="Add a note to a CRM contact.",
            enabled=True,
            requires_internet=False,
        ),
        ToolConfig(
            name="update_contact_status",
            description="Update a CRM contact pipeline status.",
            enabled=True,
            requires_internet=False,
        ),
        # Scheduler
        ToolConfig(
            name="schedule_task",
            description="Schedule a recurring or one-off task.",
            enabled=True,
            requires_internet=False,
        ),
        ToolConfig(
            name="list_scheduled_tasks",
            description="List all currently scheduled tasks.",
            enabled=True,
            requires_internet=False,
        ),
        ToolConfig(
            name="cancel_task",
            description="Cancel a scheduled task by ID.",
            enabled=True,
            requires_internet=False,
        ),
        # GitHub (online only)
        ToolConfig(
            name="search_code",
            description="Search code on GitHub. Requires internet.",
            enabled=True,
            requires_internet=True,
        ),
        ToolConfig(
            name="get_file",
            description="Retrieve a file from a GitHub repository. Requires internet.",
            enabled=True,
            requires_internet=True,
        ),
        ToolConfig(
            name="create_issue",
            description="Create a GitHub issue. Requires internet.",
            enabled=True,
            requires_internet=True,
        ),
        # Filesystem
        ToolConfig(
            name="read_file",
            description="Read a file from /data or /workspace.",
            enabled=True,
            requires_internet=False,
        ),
        ToolConfig(
            name="list_directory",
            description="List a directory in /data or /workspace.",
            enabled=True,
            requires_internet=False,
        ),
        ToolConfig(
            name="search_files",
            description="Search for files by glob pattern.",
            enabled=True,
            requires_internet=False,
        ),
    ],
    channels=[
        ChannelConfig(channel_type=ChannelType.WEB, enabled=True),
        ChannelConfig(channel_type=ChannelType.VOICE, enabled=True),
        ChannelConfig(channel_type=ChannelType.TELEGRAM, enabled=True),
        ChannelConfig(channel_type=ChannelType.SMS, enabled=True),
        ChannelConfig(channel_type=ChannelType.WHATSAPP, enabled=True),
    ],
    hardware_tier=4,
    rag_enabled=True,
    rag_collection="enterprise_kb",
    active=True,
    metadata={
        "subagent_ids": [],                     # populated after sub-agents are seeded
        "redis_bus_channel": "agentcore:bus:enterprise",
        "audit_log_enabled": True,
        "admin_escalation_email": "",           # set during wizard
        "max_parallel_subagents": 4,
        "min_hardware_tier": 4,
        "model_license": "Apache 2.0",
        "escalation_threshold_usd": 1000,       # financial actions above this require human approval
        "roles": ["admin", "manager", "analyst", "viewer"],
    },
)
