"""
Pydantic request/response models for AgentCore.
"""
from __future__ import annotations

import uuid
from datetime import datetime, timezone
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# Enumerations
# ---------------------------------------------------------------------------


class AgentProfile(str, Enum):
    """Pre-built agent personas matching the product profiles."""

    GENERAL = "general"
    CUSTOMER_SERVICE = "customer_service"
    LEGAL = "legal"
    MEDICAL = "medical"
    REAL_ESTATE = "real_estate"
    ACCOUNTING = "accounting"
    # v1.1 product profiles
    PERSONAL_PRODUCTIVITY = "personal_productivity"
    CUSTOMER_SUPPORT = "customer_support"
    SALES_OUTREACH = "sales_outreach"
    DEVELOPER_ASSISTANT = "developer_assistant"
    BUSINESS_INTELLIGENCE = "business_intelligence"
    ENTERPRISE_ORCHESTRATOR = "enterprise_orchestrator"


class MessageRole(str, Enum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"
    TOOL = "tool"


class PipelineStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class ChannelType(str, Enum):
    WEB = "web"
    TELEGRAM = "telegram"
    SMS = "sms"
    WHATSAPP = "whatsapp"
    VOICE = "voice"


# ---------------------------------------------------------------------------
# Agent configuration
# ---------------------------------------------------------------------------


class ToolConfig(BaseModel):
    """Configuration for a single tool available to an agent."""

    name: str
    description: str = ""
    enabled: bool = True
    requires_internet: bool = False
    config: dict[str, Any] = Field(default_factory=dict)


class ChannelConfig(BaseModel):
    """Configuration for a communication channel bound to an agent."""

    channel_type: ChannelType
    enabled: bool = True
    config: dict[str, Any] = Field(default_factory=dict)


class AgentConfig(BaseModel):
    """Full configuration record for one agent — stored in PostgreSQL."""

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    profile: AgentProfile = AgentProfile.GENERAL
    model: str = "llama3.1:8b"
    fallback_model: str | None = None  # used when hardware_tier < profile's required tier
    system_prompt: str = "You are a helpful AI assistant."
    tools: list[ToolConfig] = Field(default_factory=list)
    channels: list[ChannelConfig] = Field(default_factory=list)
    hardware_tier: int = 1
    rag_enabled: bool = False
    rag_collection: str | None = None  # ChromaDB collection name
    active: bool = True
    metadata: dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    class Config:
        from_attributes = True


# ---------------------------------------------------------------------------
# Messages
# ---------------------------------------------------------------------------


class Message(BaseModel):
    """A single turn in a conversation."""

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    role: MessageRole
    content: str
    metadata: dict[str, Any] = Field(default_factory=dict)
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ChannelMessage(BaseModel):
    """
    A message arriving from any external channel (Telegram, SMS, WhatsApp, web).
    Normalised form used internally by the message router.
    """

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    channel: ChannelType
    sender_id: str  # channel-native user identifier (e.g., Telegram chat_id)
    content: str
    session_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    metadata: dict[str, Any] = Field(default_factory=dict)
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


# ---------------------------------------------------------------------------
# Chat request / response
# ---------------------------------------------------------------------------


class ChatRequest(BaseModel):
    """Inbound request for the /api/chat and /api/chat/stream endpoints."""

    agent_id: str
    message: str
    session_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    conversation_id: str | None = None  # PostgreSQL conversations.id; created if not provided
    stream: bool = True
    metadata: dict[str, Any] = Field(default_factory=dict)


class ChatResponse(BaseModel):
    """Response from the synchronous /api/chat endpoint."""

    message: str
    agent_id: str
    session_id: str
    tokens_used: int = 0
    model: str
    duration_ms: int
    metadata: dict[str, Any] = Field(default_factory=dict)


class StreamChunk(BaseModel):
    """A single SSE payload chunk for the /api/chat/stream endpoint."""

    delta: str
    done: bool = False
    session_id: str
    metadata: dict[str, Any] = Field(default_factory=dict)


# ---------------------------------------------------------------------------
# Tool calls
# ---------------------------------------------------------------------------


class ToolCall(BaseModel):
    """A single tool invocation — request and result."""

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    tool_name: str
    arguments: dict[str, Any] = Field(default_factory=dict)
    result: dict[str, Any] | None = None
    error: str | None = None
    duration_ms: int = 0


# ---------------------------------------------------------------------------
# Pipeline
# ---------------------------------------------------------------------------


class TaskPipeline(BaseModel):
    """
    A multi-step task pipeline.  Each step can be an LLM call, tool call,
    data transform, conditional branch, or a parallel fan-out.
    """

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    agent_id: str
    session_id: str
    steps: list[dict[str, Any]] = Field(default_factory=list)
    context: dict[str, Any] = Field(default_factory=dict)
    status: PipelineStatus = PipelineStatus.PENDING
    results: list[dict[str, Any]] = Field(default_factory=list)
    error: str | None = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    completed_at: datetime | None = None
