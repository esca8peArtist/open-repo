"""
CRM MCP tools — local SQLite CRM database operations.

Database schema (auto-created if missing)
------------------------------------------
contacts(
    id          TEXT PRIMARY KEY,
    name        TEXT NOT NULL,
    email       TEXT,
    phone       TEXT,
    company     TEXT,
    status      TEXT DEFAULT 'lead',
    notes       TEXT DEFAULT '',
    created_at  TEXT DEFAULT CURRENT_TIMESTAMP
)

Config (env vars)
-----------------
CRM_DB_PATH — path to SQLite file (default: /data/crm.db)

Profiles: sales_outreach (3)
"""
from __future__ import annotations

import asyncio
import logging
import os
import sqlite3
import uuid
from datetime import datetime, timezone
from functools import partial
from typing import Any

from agentcore.config import get_settings
from agentcore.mcp.protocol import MCPContext, MCPTool, MCPToolResult, MCPToolSchema

logger = logging.getLogger(__name__)

_PROFILES = ["sales_outreach"]
_DEFAULT_DB_PATH = "/data/crm.db"

_SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS contacts (
    id         TEXT PRIMARY KEY,
    name       TEXT NOT NULL,
    email      TEXT,
    phone      TEXT,
    company    TEXT,
    status     TEXT DEFAULT 'lead',
    notes      TEXT DEFAULT '',
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
"""


def _db_path() -> str:
    return get_settings().crm_db_path or _DEFAULT_DB_PATH


def _get_connection(path: str) -> sqlite3.Connection:
    """Open (and initialise if necessary) the CRM SQLite database."""
    os.makedirs(os.path.dirname(path) if os.path.dirname(path) else ".", exist_ok=True)
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.execute(_SCHEMA_SQL)
    conn.commit()
    return conn


# ---------------------------------------------------------------------------
# Tool 1: search_contacts
# ---------------------------------------------------------------------------


def _search_contacts_sync(path: str, query: str) -> list[dict]:
    q = f"%{query}%"
    conn = _get_connection(path)
    try:
        cursor = conn.execute(
            """
            SELECT id, name, email, phone, company, status, notes, created_at
            FROM contacts
            WHERE name LIKE ? OR email LIKE ? OR company LIKE ? OR phone LIKE ?
            ORDER BY name LIMIT 50
            """,
            (q, q, q, q),
        )
        return [dict(r) for r in cursor.fetchall()]
    finally:
        conn.close()


class SearchContactsTool(MCPTool):
    """Search the local CRM for contacts by name, email, company, or phone."""

    @property
    def schema(self) -> MCPToolSchema:
        return MCPToolSchema(
            name="search_contacts",
            description=(
                "Search the local CRM database for contacts. "
                "Searches across name, email, company, and phone fields. "
                "Returns up to 50 matching contacts."
            ),
            input_schema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search term (partial match on name, email, company, phone).",
                    }
                },
                "required": ["query"],
            },
            requires_internet=False,
            profiles=_PROFILES,
        )

    async def execute(self, arguments: dict, context: MCPContext) -> MCPToolResult:
        query: str = arguments["query"]
        try:
            loop = asyncio.get_running_loop()
            contacts = await loop.run_in_executor(
                None, partial(_search_contacts_sync, _db_path(), query)
            )
            return MCPToolResult(success=True, content={"contacts": contacts, "count": len(contacts)})
        except Exception as exc:
            logger.error("search_contacts error: %s", exc)
            return MCPToolResult(success=False, content=None, error=str(exc))


# ---------------------------------------------------------------------------
# Tool 2: get_contact
# ---------------------------------------------------------------------------


def _get_contact_sync(path: str, contact_id: str) -> dict | None:
    conn = _get_connection(path)
    try:
        row = conn.execute(
            "SELECT id, name, email, phone, company, status, notes, created_at FROM contacts WHERE id = ?",
            (contact_id,),
        ).fetchone()
        return dict(row) if row else None
    finally:
        conn.close()


class GetContactTool(MCPTool):
    """Retrieve a single CRM contact by ID."""

    @property
    def schema(self) -> MCPToolSchema:
        return MCPToolSchema(
            name="get_contact",
            description="Retrieve a single CRM contact record by its ID.",
            input_schema={
                "type": "object",
                "properties": {
                    "contact_id": {
                        "type": "string",
                        "description": "The contact's unique identifier.",
                    }
                },
                "required": ["contact_id"],
            },
            requires_internet=False,
            profiles=_PROFILES,
        )

    async def execute(self, arguments: dict, context: MCPContext) -> MCPToolResult:
        contact_id: str = arguments["contact_id"]
        try:
            loop = asyncio.get_running_loop()
            contact = await loop.run_in_executor(
                None, partial(_get_contact_sync, _db_path(), contact_id)
            )
            if contact is None:
                return MCPToolResult(
                    success=False,
                    content=None,
                    error=f"Contact '{contact_id}' not found.",
                )
            return MCPToolResult(success=True, content=contact)
        except Exception as exc:
            logger.error("get_contact error: %s", exc)
            return MCPToolResult(success=False, content=None, error=str(exc))


# ---------------------------------------------------------------------------
# Tool 3: add_note
# ---------------------------------------------------------------------------


def _add_note_sync(path: str, contact_id: str, note: str) -> dict:
    timestamp = datetime.now(timezone.utc).isoformat()
    new_entry = f"[{timestamp}] {note}"
    conn = _get_connection(path)
    try:
        row = conn.execute("SELECT notes FROM contacts WHERE id = ?", (contact_id,)).fetchone()
        if row is None:
            raise ValueError(f"Contact '{contact_id}' not found.")
        existing = row["notes"] or ""
        updated = (existing + "\n" + new_entry).strip()
        conn.execute("UPDATE contacts SET notes = ? WHERE id = ?", (updated, contact_id))
        conn.commit()
        return {"contact_id": contact_id, "note_added": note, "timestamp": timestamp}
    finally:
        conn.close()


class AddNoteTool(MCPTool):
    """Append a timestamped note to a CRM contact."""

    @property
    def schema(self) -> MCPToolSchema:
        return MCPToolSchema(
            name="add_note",
            description="Append a timestamped note to a CRM contact's notes field.",
            input_schema={
                "type": "object",
                "properties": {
                    "contact_id": {"type": "string", "description": "The contact's ID."},
                    "note": {"type": "string", "description": "The note text to append."},
                },
                "required": ["contact_id", "note"],
            },
            requires_internet=False,
            profiles=_PROFILES,
        )

    async def execute(self, arguments: dict, context: MCPContext) -> MCPToolResult:
        contact_id: str = arguments["contact_id"]
        note: str = arguments["note"]
        try:
            loop = asyncio.get_running_loop()
            result = await loop.run_in_executor(
                None, partial(_add_note_sync, _db_path(), contact_id, note)
            )
            return MCPToolResult(success=True, content=result)
        except ValueError as exc:
            return MCPToolResult(success=False, content=None, error=str(exc))
        except Exception as exc:
            logger.error("add_note error: %s", exc)
            return MCPToolResult(success=False, content=None, error=str(exc))


# ---------------------------------------------------------------------------
# Tool 4: update_contact_status
# ---------------------------------------------------------------------------


_VALID_STATUSES = {"lead", "prospect", "customer", "churned", "do_not_contact"}


def _update_status_sync(path: str, contact_id: str, status: str) -> dict:
    conn = _get_connection(path)
    try:
        row = conn.execute("SELECT id FROM contacts WHERE id = ?", (contact_id,)).fetchone()
        if row is None:
            raise ValueError(f"Contact '{contact_id}' not found.")
        conn.execute("UPDATE contacts SET status = ? WHERE id = ?", (status, contact_id))
        conn.commit()
        return {"contact_id": contact_id, "new_status": status}
    finally:
        conn.close()


class UpdateContactStatusTool(MCPTool):
    """Update the status field of a CRM contact."""

    @property
    def schema(self) -> MCPToolSchema:
        return MCPToolSchema(
            name="update_contact_status",
            description=(
                "Update the status of a CRM contact. "
                f"Valid statuses: {', '.join(sorted(_VALID_STATUSES))}."
            ),
            input_schema={
                "type": "object",
                "properties": {
                    "contact_id": {"type": "string", "description": "The contact's ID."},
                    "status": {
                        "type": "string",
                        "enum": sorted(_VALID_STATUSES),
                        "description": "New status value.",
                    },
                },
                "required": ["contact_id", "status"],
            },
            requires_internet=False,
            profiles=_PROFILES,
        )

    async def execute(self, arguments: dict, context: MCPContext) -> MCPToolResult:
        contact_id: str = arguments["contact_id"]
        status: str = arguments["status"]

        if status not in _VALID_STATUSES:
            return MCPToolResult(
                success=False,
                content=None,
                error=f"Invalid status '{status}'. Must be one of: {', '.join(sorted(_VALID_STATUSES))}",
            )

        try:
            loop = asyncio.get_running_loop()
            result = await loop.run_in_executor(
                None, partial(_update_status_sync, _db_path(), contact_id, status)
            )
            return MCPToolResult(success=True, content=result)
        except ValueError as exc:
            return MCPToolResult(success=False, content=None, error=str(exc))
        except Exception as exc:
            logger.error("update_contact_status error: %s", exc)
            return MCPToolResult(success=False, content=None, error=str(exc))
