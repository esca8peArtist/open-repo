"""
Admin dashboard FastAPI router.
Mounted at /dashboard in agentcore/server.py.

Authentication: cookie-based session or X-API-Key header.
All HTML routes redirect to /dashboard/login if unauthenticated.
All JSON routes return 401 if unauthenticated.
"""
from __future__ import annotations

import asyncio
import json
import logging
import os
import platform
import secrets
import subprocess
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from fastapi import APIRouter, Depends, Form, HTTPException, Request, status
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse, StreamingResponse
from fastapi.templating import Jinja2Templates

from agentcore import __version__
from agentcore.config import get_settings
from agentcore.models import (
    AgentConfig,
    AgentProfile,
    ChannelConfig,
    ChannelType,
    ToolConfig,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/dashboard")

# Resolve templates directory relative to this file so the path works
# regardless of where uvicorn is launched from.
_TEMPLATES_DIR = Path(__file__).parent / "templates"
templates = Jinja2Templates(directory=str(_TEMPLATES_DIR))

# ---------------------------------------------------------------------------
# Human-readable profile descriptions shown in the New Agent form
# ---------------------------------------------------------------------------

_PROFILE_META: dict[str, dict[str, str]] = {
    "personal_productivity": {
        "label": "Personal Productivity",
        "description": "Calendar management, task tracking, reminders, email drafting.",
        "min_tier": "1",
        "recommended_model": "qwen2.5:7b",
    },
    "customer_support": {
        "label": "Customer Support",
        "description": "FAQ answering, ticket triage, polite escalation handling.",
        "min_tier": "1",
        "recommended_model": "qwen2.5:7b",
    },
    "sales_outreach": {
        "label": "Sales Outreach",
        "description": "Lead qualification, follow-up sequences, objection handling.",
        "min_tier": "2",
        "recommended_model": "qwen2.5:14b",
    },
    "developer_assistant": {
        "label": "Developer Assistant",
        "description": "Code review, debugging, documentation generation.",
        "min_tier": "2",
        "recommended_model": "qwen3-coder:30b",
    },
    "business_intelligence": {
        "label": "Business Intelligence",
        "description": "Data analysis, report generation, trend summarisation.",
        "min_tier": "3",
        "recommended_model": "deepseek-r1:14b",
    },
    "enterprise_orchestrator": {
        "label": "Enterprise Orchestrator",
        "description": "Multi-agent coordination, complex workflow management.",
        "min_tier": "4",
        "recommended_model": "qwen3:72b",
    },
    "general": {
        "label": "General Assistant",
        "description": "All-purpose assistant suitable for any task.",
        "min_tier": "1",
        "recommended_model": "qwen2.5:7b",
    },
    "customer_service": {
        "label": "Customer Service",
        "description": "Customer-facing support with empathetic, on-brand responses.",
        "min_tier": "1",
        "recommended_model": "qwen2.5:7b",
    },
    "legal": {
        "label": "Legal Assistant",
        "description": "Contract review, legal research, compliance checks.",
        "min_tier": "3",
        "recommended_model": "deepseek-r1:14b",
    },
    "medical": {
        "label": "Medical Assistant",
        "description": "Clinical notes, symptom triage (non-diagnostic aid).",
        "min_tier": "3",
        "recommended_model": "deepseek-r1:14b",
    },
    "real_estate": {
        "label": "Real Estate Agent",
        "description": "Property listings, buyer queries, market summaries.",
        "min_tier": "1",
        "recommended_model": "qwen2.5:7b",
    },
    "accounting": {
        "label": "Accounting Assistant",
        "description": "Invoice processing, expense categorisation, financial summaries.",
        "min_tier": "2",
        "recommended_model": "qwen2.5:14b",
    },
}

_AVAILABLE_TOOLS = [
    "web_search",
    "calendar",
    "email",
    "calculator",
    "rag_query",
    "code_interpreter",
    "file_reader",
    "weather",
    "crm_lookup",
    "ticket_create",
]

_AVAILABLE_CHANNELS = [ct.value for ct in ChannelType]

# ---------------------------------------------------------------------------
# Session store — maps opaque token → expiry timestamp (UTC)
# ---------------------------------------------------------------------------

# In-memory session store: {token: expiry_datetime_utc}
# For multi-process deployments replace with Redis-backed store.
_SESSION_STORE: dict[str, datetime] = {}
_SESSION_TTL = timedelta(hours=24)


def _create_session_token() -> tuple[str, datetime]:
    """Generate a cryptographically random session token and its expiry."""
    token = secrets.token_urlsafe(32)
    expiry = datetime.now(tz=timezone.utc) + _SESSION_TTL
    return token, expiry


def _store_session(token: str, expiry: datetime) -> None:
    """Persist the session token and purge any expired tokens."""
    _SESSION_STORE[token] = expiry
    # Prune expired entries to avoid unbounded growth
    now = datetime.now(tz=timezone.utc)
    expired = [t for t, exp in _SESSION_STORE.items() if exp <= now]
    for t in expired:
        _SESSION_STORE.pop(t, None)


def _session_is_valid(token: str) -> bool:
    """Return True if the token exists in the store and has not expired."""
    expiry = _SESSION_STORE.get(token)
    if expiry is None:
        return False
    if datetime.now(tz=timezone.utc) >= expiry:
        _SESSION_STORE.pop(token, None)
        return False
    return True


def _revoke_session(token: str) -> None:
    """Remove a session token from the store (logout)."""
    _SESSION_STORE.pop(token, None)


# ---------------------------------------------------------------------------
# Authentication helpers
# ---------------------------------------------------------------------------


def _get_api_key(request: Request) -> str:
    """Return the configured API key from app state settings."""
    return request.app.state.settings.api_secret_key


def _is_authenticated(request: Request) -> bool:
    """Check cookie-based session token or X-API-Key header."""
    expected = _get_api_key(request)
    # Header auth: compare directly to the API key (server-to-server calls)
    if request.headers.get("X-API-Key") == expected:
        return True
    # Cookie-based session: validate opaque token, NOT the raw key
    session_token = request.cookies.get("dashboard_session")
    if session_token and _session_is_valid(session_token):
        return True
    return False


async def _require_auth_html(request: Request) -> None:
    """Dependency: redirect to login page if not authenticated (HTML routes)."""
    if not _is_authenticated(request):
        raise HTTPException(
            status_code=status.HTTP_302_FOUND,
            headers={"Location": "/dashboard/login"},
        )


async def _require_auth_json(request: Request) -> None:
    """Dependency: return 401 JSON if not authenticated (API routes)."""
    if not _is_authenticated(request):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required.",
        )


# ---------------------------------------------------------------------------
# Login / logout
# ---------------------------------------------------------------------------


@router.get("/login", response_class=HTMLResponse, include_in_schema=False)
async def login_page(request: Request):
    """Render the login form."""
    return templates.TemplateResponse(
        "login.html",
        {"request": request, "error": None},
    )


@router.post("/login", include_in_schema=False)
async def login_submit(request: Request, api_key: str = Form(...)):
    """Validate key, issue an opaque session token, and set it as the cookie."""
    expected = _get_api_key(request)
    if api_key != expected:
        return templates.TemplateResponse(
            "login.html",
            {"request": request, "error": "Invalid API key."},
            status_code=401,
        )
    # Generate a short-lived opaque session token — the raw API key is never
    # stored in or transmitted via the cookie.
    token, expiry = _create_session_token()
    _store_session(token, expiry)
    ttl_seconds = int(_SESSION_TTL.total_seconds())

    response = RedirectResponse(url="/dashboard/", status_code=303)
    response.set_cookie(
        "dashboard_session",
        token,           # opaque token, not the API key
        httponly=True,
        samesite="strict",
        max_age=ttl_seconds,
    )
    return response


@router.get("/logout", include_in_schema=False)
async def logout(request: Request):
    """Revoke the session token and redirect to login."""
    session_token = request.cookies.get("dashboard_session")
    if session_token:
        _revoke_session(session_token)
    response = RedirectResponse(url="/dashboard/login", status_code=303)
    response.delete_cookie("dashboard_session")
    return response


# ---------------------------------------------------------------------------
# Helpers: read system resources
# ---------------------------------------------------------------------------


def _read_proc_meminfo() -> dict[str, int]:
    """Parse /proc/meminfo into a dict of {key: value_in_kB}."""
    info: dict[str, int] = {}
    try:
        with open("/proc/meminfo", encoding="utf-8") as fh:
            for line in fh:
                parts = line.split()
                if len(parts) >= 2:
                    key = parts[0].rstrip(":")
                    try:
                        info[key] = int(parts[1])
                    except ValueError:
                        pass
    except OSError:
        pass
    return info


def _get_ram_stats() -> dict[str, Any]:
    """Return RAM stats in MB."""
    mem = _read_proc_meminfo()
    total_mb = mem.get("MemTotal", 0) // 1024
    available_mb = mem.get("MemAvailable", 0) // 1024
    used_mb = total_mb - available_mb
    pct = round(used_mb / total_mb * 100, 1) if total_mb else 0
    return {
        "total_mb": total_mb,
        "used_mb": used_mb,
        "available_mb": available_mb,
        "pct": pct,
    }


def _get_vram_stats() -> dict[str, Any] | None:
    """Try nvidia-smi; return None if unavailable."""
    try:
        result = subprocess.run(
            [
                "nvidia-smi",
                "--query-gpu=memory.total,memory.used",
                "--format=csv,noheader,nounits",
            ],
            capture_output=True,
            text=True,
            timeout=5,
        )
        if result.returncode == 0 and result.stdout.strip():
            parts = result.stdout.strip().split(",")
            total_mb = int(parts[0].strip())
            used_mb = int(parts[1].strip())
            pct = round(used_mb / total_mb * 100, 1) if total_mb else 0
            return {"total_mb": total_mb, "used_mb": used_mb, "pct": pct, "source": "nvidia-smi"}
    except (FileNotFoundError, subprocess.TimeoutExpired, ValueError, IndexError):
        pass
    return None


def _get_uptime_seconds() -> int:
    """Read system uptime from /proc/uptime."""
    try:
        with open("/proc/uptime", encoding="utf-8") as fh:
            return int(float(fh.read().split()[0]))
    except OSError:
        return 0


def _format_uptime(seconds: int) -> str:
    days = seconds // 86400
    hours = (seconds % 86400) // 3600
    minutes = (seconds % 3600) // 60
    if days:
        return f"{days}d {hours}h {minutes}m"
    if hours:
        return f"{hours}h {minutes}m"
    return f"{minutes}m"


async def _get_ollama_models(ollama_base_url: str) -> list[str]:
    """Fetch available model names from the local Ollama instance."""
    try:
        import httpx

        async with httpx.AsyncClient(timeout=5.0) as client:
            resp = await client.get(f"{ollama_base_url}/api/tags")
            if resp.status_code == 200:
                data = resp.json()
                return [m["name"] for m in data.get("models", [])]
    except Exception:
        pass
    return []


async def _get_system_context(request: Request) -> dict[str, Any]:
    """Gather all system context data for templates."""
    settings = request.app.state.settings
    registry = request.app.state.registry

    agents = await registry.list_agents()
    live_instances = list(getattr(registry, "_instances", {}).keys())
    ram = _get_ram_stats()
    vram = _get_vram_stats()
    uptime_secs = _get_uptime_seconds()

    return {
        "version": __version__,
        "hardware_tier": settings.hardware_tier,
        "ram": ram,
        "vram": vram,
        "uptime": _format_uptime(uptime_secs),
        "uptime_seconds": uptime_secs,
        "agents": agents,
        "live_instances": live_instances,
        "agent_count": len(agents),
        "active_agent_count": sum(1 for a in agents if a.active),
    }


# ---------------------------------------------------------------------------
# Overview dashboard
# ---------------------------------------------------------------------------


@router.get("/", response_class=HTMLResponse, dependencies=[Depends(_require_auth_html)])
async def dashboard_index(request: Request):
    """Main dashboard — system overview, all agents, health summary."""
    ctx = await _get_system_context(request)
    ctx["request"] = request
    ctx["page"] = "overview"
    return templates.TemplateResponse("index.html", ctx)


# ---------------------------------------------------------------------------
# Agent management
# ---------------------------------------------------------------------------


@router.get("/agents", response_class=HTMLResponse, dependencies=[Depends(_require_auth_html)])
async def list_agents_page(request: Request):
    """List all configured agents with status indicators."""
    ctx = await _get_system_context(request)
    ctx["request"] = request
    ctx["page"] = "agents"
    return templates.TemplateResponse("index.html", ctx)


@router.get("/agents/new", response_class=HTMLResponse, dependencies=[Depends(_require_auth_html)])
async def new_agent_form(request: Request):
    """New agent form — select profile template to start from."""
    settings = request.app.state.settings
    ollama_models = await _get_ollama_models(settings.ollama_base_url)
    if not ollama_models:
        ollama_models = ["qwen2.5:7b", "llama3.1:8b", "phi4-mini:latest"]

    return templates.TemplateResponse(
        "agent_new.html",
        {
            "request": request,
            "page": "agents",
            "profiles": _PROFILE_META,
            "ollama_models": ollama_models,
            "available_tools": _AVAILABLE_TOOLS,
            "available_channels": _AVAILABLE_CHANNELS,
            "version": __version__,
        },
    )


@router.post("/agents/new", dependencies=[Depends(_require_auth_html)])
async def create_agent(
    request: Request,
    name: str = Form(...),
    profile: str = Form(...),
    model: str = Form(...),
    system_prompt: str = Form("You are a helpful AI assistant."),
    hardware_tier: int = Form(1),
    rag_enabled: str = Form("off"),
    rag_collection: str = Form(""),
):
    """Create a new agent from the submitted form."""
    registry = request.app.state.registry

    # Parse multi-value form fields (tools/channels are checkboxes)
    form_data = await request.form()
    tools_selected: list[str] = form_data.getlist("tools")
    channels_selected: list[str] = form_data.getlist("channels")

    tools = [
        ToolConfig(name=t, enabled=True)
        for t in tools_selected
        if t in _AVAILABLE_TOOLS
    ]
    channels = []
    for ch in channels_selected:
        try:
            channels.append(ChannelConfig(channel_type=ChannelType(ch), enabled=True))
        except ValueError:
            pass

    try:
        profile_enum = AgentProfile(profile)
    except ValueError:
        profile_enum = AgentProfile.GENERAL

    config = AgentConfig(
        name=name.strip(),
        profile=profile_enum,
        model=model,
        system_prompt=system_prompt,
        tools=tools,
        channels=channels,
        hardware_tier=hardware_tier,
        rag_enabled=(rag_enabled == "on"),
        rag_collection=rag_collection.strip() or None,
        active=True,
    )

    agent_id = await registry.create_agent(config)
    logger.info("Agent created via dashboard: %s (%s)", name, agent_id)

    session_token = request.cookies.get("dashboard_session", "api-key")
    await audit_log(
        "agent.create",
        target_id=agent_id,
        actor=session_token,
        details={"name": name, "profile": profile, "model": model},
    )

    return RedirectResponse(url=f"/dashboard/agents/{agent_id}", status_code=303)


@router.get("/agents/{agent_id}", response_class=HTMLResponse, dependencies=[Depends(_require_auth_html)])
async def agent_detail(request: Request, agent_id: str):
    """Single agent detail — config, stats, recent conversations, tool usage."""
    registry = request.app.state.registry
    agents = await registry.list_agents()
    agent: AgentConfig | None = next((a for a in agents if a.id == agent_id), None)
    if agent is None:
        raise HTTPException(status_code=404, detail=f"Agent '{agent_id}' not found.")

    live_instances = list(getattr(registry, "_instances", {}).keys())
    is_live = agent_id in live_instances

    return templates.TemplateResponse(
        "agent_detail.html",
        {
            "request": request,
            "page": "agents",
            "agent": agent,
            "is_live": is_live,
            "version": __version__,
        },
    )


@router.get("/agents/{agent_id}/edit", response_class=HTMLResponse, dependencies=[Depends(_require_auth_html)])
async def edit_agent_form(request: Request, agent_id: str):
    """Edit agent configuration form."""
    registry = request.app.state.registry
    settings = request.app.state.settings

    agents = await registry.list_agents()
    agent: AgentConfig | None = next((a for a in agents if a.id == agent_id), None)
    if agent is None:
        raise HTTPException(status_code=404, detail=f"Agent '{agent_id}' not found.")

    ollama_models = await _get_ollama_models(settings.ollama_base_url)
    if not ollama_models:
        ollama_models = ["qwen2.5:7b", "llama3.1:8b", "phi4-mini:latest"]
    if agent.model not in ollama_models:
        ollama_models.insert(0, agent.model)

    enabled_tools = {t.name for t in agent.tools if t.enabled}
    enabled_channels = {c.channel_type.value for c in agent.channels if c.enabled}

    return templates.TemplateResponse(
        "agent_edit.html",
        {
            "request": request,
            "page": "agents",
            "agent": agent,
            "ollama_models": ollama_models,
            "available_tools": _AVAILABLE_TOOLS,
            "available_channels": _AVAILABLE_CHANNELS,
            "enabled_tools": enabled_tools,
            "enabled_channels": enabled_channels,
            "profiles": _PROFILE_META,
            "version": __version__,
        },
    )


@router.post("/agents/{agent_id}/edit", dependencies=[Depends(_require_auth_html)])
async def update_agent(
    request: Request,
    agent_id: str,
    name: str = Form(...),
    profile: str = Form(...),
    model: str = Form(...),
    system_prompt: str = Form(""),
    hardware_tier: int = Form(1),
    rag_enabled: str = Form("off"),
    rag_collection: str = Form(""),
):
    """Save agent configuration changes."""
    registry = request.app.state.registry

    # Fetch existing config to preserve created_at
    agents = await registry.list_agents()
    existing: AgentConfig | None = next((a for a in agents if a.id == agent_id), None)
    if existing is None:
        raise HTTPException(status_code=404, detail=f"Agent '{agent_id}' not found.")

    form_data = await request.form()
    tools_selected: list[str] = form_data.getlist("tools")
    channels_selected: list[str] = form_data.getlist("channels")

    tools = [
        ToolConfig(name=t, enabled=True)
        for t in tools_selected
        if t in _AVAILABLE_TOOLS
    ]
    channels = []
    for ch in channels_selected:
        try:
            channels.append(ChannelConfig(channel_type=ChannelType(ch), enabled=True))
        except ValueError:
            pass

    try:
        profile_enum = AgentProfile(profile)
    except ValueError:
        profile_enum = AgentProfile.GENERAL

    updated = AgentConfig(
        id=agent_id,
        name=name.strip(),
        profile=profile_enum,
        model=model,
        system_prompt=system_prompt,
        tools=tools,
        channels=channels,
        hardware_tier=hardware_tier,
        rag_enabled=(rag_enabled == "on"),
        rag_collection=rag_collection.strip() or None,
        active=existing.active,
        created_at=existing.created_at,
    )

    success = await registry.update_agent(agent_id, updated)
    if not success:
        raise HTTPException(status_code=500, detail="Update failed.")

    logger.info("Agent updated via dashboard: %s", agent_id)

    session_token = request.cookies.get("dashboard_session", "api-key")
    await audit_log(
        "agent.update",
        target_id=agent_id,
        actor=session_token,
        details={"name": name, "profile": profile, "model": model},
    )

    return RedirectResponse(url=f"/dashboard/agents/{agent_id}", status_code=303)


@router.post(
    "/agents/{agent_id}/toggle",
    dependencies=[Depends(_require_auth_json)],
    response_class=JSONResponse,
)
async def toggle_agent(request: Request, agent_id: str):
    """Enable or disable an agent (JSON)."""
    registry = request.app.state.registry
    agents = await registry.list_agents()
    agent: AgentConfig | None = next((a for a in agents if a.id == agent_id), None)
    if agent is None:
        raise HTTPException(status_code=404, detail="Agent not found.")

    agent.active = not agent.active
    await registry.update_agent(agent_id, agent)
    logger.info("Agent %s toggled active=%s via dashboard", agent_id, agent.active)

    session_token = request.cookies.get("dashboard_session", "api-key")
    await audit_log(
        "agent.toggle",
        target_id=agent_id,
        actor=session_token,
        details={"active": agent.active},
    )

    return JSONResponse({"agent_id": agent_id, "active": agent.active})


@router.delete(
    "/agents/{agent_id}",
    dependencies=[Depends(_require_auth_json)],
    response_class=JSONResponse,
)
async def delete_agent(request: Request, agent_id: str):
    """Delete an agent (JSON — requires explicit confirmation via request body)."""
    body = await request.json()
    if not body.get("confirm"):
        raise HTTPException(status_code=400, detail="Must send {\"confirm\": true} to delete.")

    registry = request.app.state.registry
    success = await registry.delete_agent(agent_id)
    if not success:
        raise HTTPException(status_code=404, detail="Agent not found or delete failed.")

    logger.info("Agent deleted via dashboard: %s", agent_id)

    session_token = request.cookies.get("dashboard_session", "api-key")
    await audit_log(
        "agent.delete",
        target_id=agent_id,
        actor=session_token,
        details={},
    )

    return JSONResponse({"agent_id": agent_id, "status": "deleted"})


# ---------------------------------------------------------------------------
# Resource allocation
# ---------------------------------------------------------------------------


@router.get("/resources", response_class=HTMLResponse, dependencies=[Depends(_require_auth_html)])
async def resources_page(request: Request):
    """Hardware resource view — RAM/VRAM usage per agent, tier compatibility."""
    ctx = await _get_system_context(request)
    ctx["request"] = request
    ctx["page"] = "resources"

    settings = request.app.state.settings
    tier = settings.hardware_tier
    tier_info = {
        1: {"label": "Tier 1 — Entry", "ram": "8–16 GB", "profiles": "1, 2", "models": "7B–8B"},
        2: {"label": "Tier 2 — Mid", "ram": "24 GB", "profiles": "1–4", "models": "up to 32B"},
        3: {"label": "Tier 3 — Pro", "ram": "64 GB", "profiles": "1–5", "models": "up to 70B"},
        4: {"label": "Tier 4 — Enterprise", "ram": "128+ GB", "profiles": "All", "models": "up to 200B"},
    }
    ctx["tier_info"] = tier_info.get(tier, tier_info[1])
    ctx["all_tier_info"] = tier_info

    return templates.TemplateResponse("resources.html", ctx)


# ---------------------------------------------------------------------------
# Audit log
# ---------------------------------------------------------------------------

# In-memory audit log ring buffer (max 500 entries). For production this would
# persist to PostgreSQL via a dedicated audit_log table.
_AUDIT_LOG: list[dict[str, Any]] = []
_AUDIT_LOG_MAX = 500


def _log_audit(event: str, agent_id: str = "", details: str = "") -> None:
    """Append an entry to the in-memory audit log."""
    entry = {
        "timestamp": datetime.now(tz=timezone.utc).isoformat(),
        "event": event,
        "agent_id": agent_id,
        "details": details,
    }
    _AUDIT_LOG.append(entry)
    if len(_AUDIT_LOG) > _AUDIT_LOG_MAX:
        _AUDIT_LOG.pop(0)


async def audit_log(
    action: str,
    *,
    target_id: str = "",
    actor: str = "system",
    details: dict[str, Any] | None = None,
) -> None:
    """Persist an audit log entry to PostgreSQL.

    Inserts a row into the ``audit_log`` table using asyncpg.
    If the database write fails the error is logged but NOT re-raised so
    that the dashboard operation that triggered the audit is never blocked.

    Args:
        action:    Event type string, e.g. "agent.create", "agent.delete".
        target_id: UUID of the affected agent (or empty string if not applicable).
        actor:     Session token or "system" identifying who performed the action.
        details:   Additional structured data to store in the JSONB ``details`` column.
    """
    # Also append to the in-memory ring buffer so the logs page stays live.
    _log_audit(action, agent_id=target_id, details=json.dumps(details or {}))

    try:
        import asyncpg  # optional; available inside agentcore container

        payload: dict[str, Any] = {"actor": actor, **(details or {})}
        # agent_id column is uuid-typed; pass None if no valid target_id.
        agent_uuid: str | None = target_id if target_id else None

        conn = await asyncpg.connect(dsn=get_settings().postgres_url)
        try:
            await conn.execute(
                """
                INSERT INTO audit_log (event_type, agent_id, details)
                VALUES ($1, $2::uuid, $3::jsonb)
                """,
                action,
                agent_uuid,
                json.dumps(payload),
            )
        finally:
            await conn.close()
    except Exception as exc:
        logger.error("audit_log DB write failed (action=%s, target=%s): %s", action, target_id, exc)


@router.get("/logs", response_class=HTMLResponse, dependencies=[Depends(_require_auth_html)])
async def audit_logs(
    request: Request,
    page: int = 1,
    event_type: str = "",
    agent_id: str = "",
):
    """Paginated audit log viewer with filters."""
    page_size = 25
    entries = list(reversed(_AUDIT_LOG))  # newest first

    if event_type:
        entries = [e for e in entries if event_type.lower() in e["event"].lower()]
    if agent_id:
        entries = [e for e in entries if e["agent_id"] == agent_id]

    total = len(entries)
    total_pages = max(1, (total + page_size - 1) // page_size)
    page = max(1, min(page, total_pages))
    offset = (page - 1) * page_size
    page_entries = entries[offset : offset + page_size]

    registry = request.app.state.registry
    agents = await registry.list_agents()

    return templates.TemplateResponse(
        "logs.html",
        {
            "request": request,
            "page": "logs",
            "entries": page_entries,
            "current_page": page,
            "total_pages": total_pages,
            "total": total,
            "event_type_filter": event_type,
            "agent_id_filter": agent_id,
            "agents": agents,
            "version": __version__,
        },
    )


# ---------------------------------------------------------------------------
# Updates (Task 25)
# ---------------------------------------------------------------------------


@router.get("/updates", response_class=HTMLResponse, dependencies=[Depends(_require_auth_html)])
async def updates_page(request: Request):
    """Update management page — current version, check for updates, install."""
    # Check rollback availability
    from agentcore.updater.installer import _ROLLBACK_DIR, _ROLLBACK_TTL_HOURS

    rollback_available = False
    rollback_ttl_remaining = 0
    rollback_version = ""

    rollback_meta_path = _ROLLBACK_DIR / "rollback_meta.json"
    if rollback_meta_path.exists():
        try:
            meta = json.loads(rollback_meta_path.read_text(encoding="utf-8"))
            saved_at = meta.get("saved_at", "")
            if saved_at:
                saved_dt = datetime.fromisoformat(saved_at)
                age_hours = (datetime.now(tz=timezone.utc) - saved_dt).total_seconds() / 3600
                if age_hours < _ROLLBACK_TTL_HOURS:
                    rollback_available = True
                    rollback_ttl_remaining = int((_ROLLBACK_TTL_HOURS - age_hours) * 3600)
                    rollback_version = meta.get("version", "")
        except Exception as exc:
            logger.debug("Could not read rollback metadata: %s", exc)

    return templates.TemplateResponse(
        "updates.html",
        {
            "request": request,
            "page": "updates",
            "version": __version__,
            "rollback_available": rollback_available,
            "rollback_ttl_remaining": rollback_ttl_remaining,
            "rollback_version": rollback_version,
        },
    )


@router.post(
    "/updates/check",
    dependencies=[Depends(_require_auth_json)],
    response_class=JSONResponse,
)
async def check_updates(request: Request):
    """Trigger update check. Returns JSON with update info."""
    from agentcore.updater.update_checker import check_for_updates

    update_info = await check_for_updates(__version__)
    return JSONResponse(
        {
            "available": update_info.available,
            "current_version": update_info.current_version,
            "latest_version": update_info.latest_version,
            "changelog": update_info.changelog,
            "components": update_info.components,
            "error": update_info.error,
        }
    )


@router.get(
    "/updates/install/stream",
    dependencies=[Depends(_require_auth_json)],
)
async def install_update_stream(request: Request):
    """
    SSE stream for update installation progress.

    The client subscribes to this endpoint after receiving update info from
    POST /updates/check. The stream emits newline-delimited SSE events:
        data: {"phase": "download|apply|restart|complete|error",
               "progress": 0.0-1.0,
               "message": "..."}

    This endpoint performs the full update: check -> download -> apply.
    """
    from agentcore.updater.installer import apply_update
    from agentcore.updater.update_checker import check_for_updates

    async def generate():
        # Emit initial event
        yield _sse({"phase": "check", "progress": 0.0, "message": "Checking for updates..."})

        update_info = await check_for_updates(__version__)

        if update_info.error == "offline":
            yield _sse({"phase": "error", "progress": 0.0, "message": "Device is offline — cannot download update."})
            return

        if not update_info.available:
            yield _sse({"phase": "complete", "progress": 1.0, "message": f"Already up to date ({update_info.current_version})."})
            return

        yield _sse({
            "phase": "download",
            "progress": 0.05,
            "message": f"Downloading update {update_info.latest_version}...",
        })

        # Progress callback bridges installer progress to SSE
        progress_queue: asyncio.Queue[tuple[str, float]] = asyncio.Queue()

        async def progress_cb(message: str, pct: float) -> None:
            await progress_queue.put((message, pct))

        # Run installer in a background task
        install_task = asyncio.create_task(apply_update(update_info, progress_callback=progress_cb))

        # Stream progress events while installer runs
        try:
            while not install_task.done():
                try:
                    msg, pct = await asyncio.wait_for(progress_queue.get(), timeout=1.0)
                    # Map 0-1 installer progress to 0.1-0.95 SSE range
                    sse_progress = 0.1 + pct * 0.85
                    phase = "download" if pct < 0.6 else ("apply" if pct < 0.85 else "restart")
                    yield _sse({"phase": phase, "progress": round(sse_progress, 2), "message": msg})
                except asyncio.TimeoutError:
                    yield _sse({"phase": "heartbeat", "progress": -1, "message": ""})

            # Drain remaining queue items
            while not progress_queue.empty():
                msg, pct = progress_queue.get_nowait()
                sse_progress = 0.1 + pct * 0.85
                phase = "download" if pct < 0.6 else ("apply" if pct < 0.85 else "restart")
                yield _sse({"phase": phase, "progress": round(sse_progress, 2), "message": msg})

            success = await install_task
            if success:
                await audit_log(
                    "update.apply",
                    actor="system",
                    details={"new_version": update_info.latest_version},
                )
                yield _sse({
                    "phase": "complete",
                    "progress": 1.0,
                    "message": f"Update to {update_info.latest_version} complete! Services are restarting.",
                    "new_version": update_info.latest_version,
                })
            else:
                yield _sse({
                    "phase": "error",
                    "progress": 0.0,
                    "message": "Update failed. Check server logs. A rollback may have been applied automatically.",
                })
        except Exception as exc:
            logger.exception("Unexpected error during SSE update stream: %s", exc)
            yield _sse({"phase": "error", "progress": 0.0, "message": f"Unexpected error: {exc}"})

    return StreamingResponse(generate(), media_type="text/event-stream")


@router.post(
    "/updates/rollback",
    dependencies=[Depends(_require_auth_json)],
    response_class=JSONResponse,
)
async def rollback_update(request: Request):
    """Rollback to the previous version (available for 24h after an update)."""
    from agentcore.updater.installer import rollback

    success = await rollback()
    if success:
        session_token = request.cookies.get("dashboard_session", "api-key")
        await audit_log(
            "update.rollback",
            actor=session_token,
            details={"reason": "manual rollback via dashboard"},
        )
        return JSONResponse({"status": "ok", "message": "Rollback successful. Services are restarting."})
    return JSONResponse(
        {"status": "error", "message": "Rollback failed. See server logs for details."},
        status_code=500,
    )


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _sse(data: dict) -> str:
    """Format a dict as a Server-Sent Event string."""
    return f"data: {json.dumps(data)}\n\n"
