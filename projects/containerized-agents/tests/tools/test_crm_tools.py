"""
MCP tool tests: CRM operations against a real SQLite in-memory DB.
"""
from __future__ import annotations

import os
import sqlite3
import uuid
from unittest.mock import patch

import pytest

from agentcore.mcp.protocol import MCPContext
from agentcore.mcp.tools.crm import (
    AddNoteTool,
    GetContactTool,
    SearchContactsTool,
    UpdateContactStatusTool,
    _get_connection,
)


def _seed_db(db_path: str) -> tuple[str, str]:
    """Seed the CRM database with two test contacts. Returns (id1, id2)."""
    id1 = str(uuid.uuid4())
    id2 = str(uuid.uuid4())
    conn = _get_connection(db_path)
    conn.execute(
        "INSERT INTO contacts (id, name, email, phone, company, status) VALUES (?, ?, ?, ?, ?, ?)",
        (id1, "Alice Smith", "alice@example.com", "+15551001", "Acme Corp", "lead"),
    )
    conn.execute(
        "INSERT INTO contacts (id, name, email, phone, company, status) VALUES (?, ?, ?, ?, ?, ?)",
        (id2, "Bob Jones", "bob@example.com", "+15551002", "Beta Ltd", "customer"),
    )
    conn.commit()
    conn.close()
    return id1, id2


class TestSearchContactsTool:
    @pytest.mark.asyncio
    async def test_search_by_name(self, online_context, crm_db_path):
        """Search by name fragment returns matching contacts."""
        _seed_db(crm_db_path)
        tool = SearchContactsTool()
        with patch.dict(os.environ, {"CRM_DB_PATH": crm_db_path}):
            result = await tool.execute({"query": "Alice"}, online_context)
        assert result.success is True
        contacts = result.content["contacts"]
        assert len(contacts) == 1
        assert contacts[0]["name"] == "Alice Smith"

    @pytest.mark.asyncio
    async def test_search_by_email(self, online_context, crm_db_path):
        """Search by email fragment returns matching contacts."""
        _seed_db(crm_db_path)
        tool = SearchContactsTool()
        with patch.dict(os.environ, {"CRM_DB_PATH": crm_db_path}):
            result = await tool.execute({"query": "bob@example"}, online_context)
        assert result.success is True
        assert result.content["contacts"][0]["name"] == "Bob Jones"

    @pytest.mark.asyncio
    async def test_search_no_results(self, online_context, crm_db_path):
        """Search with no matching results returns empty list."""
        _seed_db(crm_db_path)
        tool = SearchContactsTool()
        with patch.dict(os.environ, {"CRM_DB_PATH": crm_db_path}):
            result = await tool.execute({"query": "NoOneLikethis123"}, online_context)
        assert result.success is True
        assert result.content["count"] == 0
        assert result.content["contacts"] == []

    @pytest.mark.asyncio
    async def test_search_by_company(self, online_context, crm_db_path):
        """Search by company name returns correct contacts."""
        _seed_db(crm_db_path)
        tool = SearchContactsTool()
        with patch.dict(os.environ, {"CRM_DB_PATH": crm_db_path}):
            result = await tool.execute({"query": "Acme"}, online_context)
        assert result.success is True
        assert result.content["contacts"][0]["company"] == "Acme Corp"

    @pytest.mark.asyncio
    async def test_search_returns_all_on_empty_query(self, online_context, crm_db_path):
        """Search with empty string matches all contacts."""
        _seed_db(crm_db_path)
        tool = SearchContactsTool()
        with patch.dict(os.environ, {"CRM_DB_PATH": crm_db_path}):
            result = await tool.execute({"query": ""}, online_context)
        assert result.success is True
        assert result.content["count"] >= 2


class TestGetContactTool:
    @pytest.mark.asyncio
    async def test_get_existing_contact(self, online_context, crm_db_path):
        """get_contact returns full record for existing ID."""
        id1, _ = _seed_db(crm_db_path)
        tool = GetContactTool()
        with patch.dict(os.environ, {"CRM_DB_PATH": crm_db_path}):
            result = await tool.execute({"contact_id": id1}, online_context)
        assert result.success is True
        assert result.content["name"] == "Alice Smith"

    @pytest.mark.asyncio
    async def test_get_nonexistent_contact(self, online_context, crm_db_path):
        """get_contact returns success=False for unknown ID."""
        _seed_db(crm_db_path)
        tool = GetContactTool()
        with patch.dict(os.environ, {"CRM_DB_PATH": crm_db_path}):
            result = await tool.execute({"contact_id": "not-a-real-id"}, online_context)
        assert result.success is False
        assert "not found" in result.error.lower()


class TestAddNoteTool:
    @pytest.mark.asyncio
    async def test_add_note_success(self, online_context, crm_db_path):
        """add_note appends a timestamped note to an existing contact."""
        id1, _ = _seed_db(crm_db_path)
        tool = AddNoteTool()
        with patch.dict(os.environ, {"CRM_DB_PATH": crm_db_path}):
            result = await tool.execute(
                {"contact_id": id1, "note": "Interested in Q3 deal"},
                online_context,
            )
        assert result.success is True
        assert result.content["contact_id"] == id1
        assert result.content["note_added"] == "Interested in Q3 deal"

    @pytest.mark.asyncio
    async def test_add_note_to_nonexistent_contact(self, online_context, crm_db_path):
        """add_note on a missing contact returns success=False."""
        _seed_db(crm_db_path)
        tool = AddNoteTool()
        with patch.dict(os.environ, {"CRM_DB_PATH": crm_db_path}):
            result = await tool.execute(
                {"contact_id": "fake-id", "note": "test note"},
                online_context,
            )
        assert result.success is False

    @pytest.mark.asyncio
    async def test_add_note_appends_not_overwrites(self, online_context, crm_db_path):
        """Multiple add_note calls must append, not overwrite."""
        id1, _ = _seed_db(crm_db_path)
        tool = AddNoteTool()
        with patch.dict(os.environ, {"CRM_DB_PATH": crm_db_path}):
            await tool.execute({"contact_id": id1, "note": "First note"}, online_context)
            await tool.execute({"contact_id": id1, "note": "Second note"}, online_context)
            contact_result = await GetContactTool().execute({"contact_id": id1}, online_context)
        notes = contact_result.content["notes"]
        assert "First note" in notes
        assert "Second note" in notes


class TestUpdateContactStatusTool:
    @pytest.mark.asyncio
    async def test_update_status_to_customer(self, online_context, crm_db_path):
        """update_contact_status changes lead → customer."""
        id1, _ = _seed_db(crm_db_path)
        tool = UpdateContactStatusTool()
        with patch.dict(os.environ, {"CRM_DB_PATH": crm_db_path}):
            result = await tool.execute(
                {"contact_id": id1, "status": "customer"},
                online_context,
            )
        assert result.success is True
        assert result.content["new_status"] == "customer"

    @pytest.mark.asyncio
    async def test_update_status_invalid_value(self, online_context, crm_db_path):
        """Invalid status must return success=False."""
        id1, _ = _seed_db(crm_db_path)
        tool = UpdateContactStatusTool()
        with patch.dict(os.environ, {"CRM_DB_PATH": crm_db_path}):
            result = await tool.execute(
                {"contact_id": id1, "status": "not_a_valid_status"},
                online_context,
            )
        assert result.success is False
        assert "Invalid status" in result.error

    @pytest.mark.asyncio
    async def test_update_status_nonexistent_contact(self, online_context, crm_db_path):
        """Update status for unknown contact returns success=False."""
        _seed_db(crm_db_path)
        tool = UpdateContactStatusTool()
        with patch.dict(os.environ, {"CRM_DB_PATH": crm_db_path}):
            result = await tool.execute(
                {"contact_id": "no-such-id", "status": "lead"},
                online_context,
            )
        assert result.success is False
