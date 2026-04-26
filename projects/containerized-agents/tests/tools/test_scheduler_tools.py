"""
MCP tool tests: task scheduling, listing, and cancellation against SQLite.
"""
from __future__ import annotations

import os
import uuid
from unittest.mock import patch

import pytest

from agentcore.mcp.protocol import MCPContext
from agentcore.mcp.tools.scheduler import (
    CancelTaskTool,
    ListScheduledTasksTool,
    ScheduleTaskTool,
    _sqlite_conn,
)


@pytest.fixture
def scheduler_env(tmp_path):
    """Patch SCHEDULER_DB_URL and _SQLITE_FALLBACK to use a temp db."""
    db = str(tmp_path / "scheduler_test.db")
    env = {"SCHEDULER_DB_URL": "", "DB_POSTGRES_URL": ""}
    with patch.dict(os.environ, env):
        with patch("agentcore.mcp.tools.scheduler._SQLITE_FALLBACK", db):
            yield db


class TestScheduleTaskTool:
    @pytest.mark.asyncio
    async def test_schedule_task_success(self, online_context, scheduler_env):
        """schedule_task must create a new task and return its ID."""
        tool = ScheduleTaskTool()
        result = await tool.execute(
            {
                "task_type": "send_email",
                "target": "alice@example.com",
                "scheduled_at": "2026-12-01T10:00:00",
                "payload": {"subject": "Follow up"},
            },
            online_context,
        )
        assert result.success is True
        assert "task_id" in result.content
        assert result.content["task_type"] == "send_email"
        assert result.content["status"] == "pending"

    @pytest.mark.asyncio
    async def test_schedule_task_invalid_datetime(self, online_context, scheduler_env):
        """Invalid scheduled_at format must return success=False."""
        tool = ScheduleTaskTool()
        result = await tool.execute(
            {
                "task_type": "follow_up",
                "target": "bob@example.com",
                "scheduled_at": "not-a-valid-date",
            },
            online_context,
        )
        assert result.success is False
        assert "Invalid" in result.error

    @pytest.mark.asyncio
    async def test_schedule_task_without_payload(self, online_context, scheduler_env):
        """schedule_task without payload must use empty dict as default."""
        tool = ScheduleTaskTool()
        result = await tool.execute(
            {
                "task_type": "send_sms",
                "target": "+15551000",
                "scheduled_at": "2026-06-01T09:00:00",
            },
            online_context,
        )
        assert result.success is True


class TestListScheduledTasksTool:
    @pytest.mark.asyncio
    async def test_list_empty_db(self, online_context, scheduler_env):
        """list_scheduled_tasks on empty DB must return empty list."""
        tool = ListScheduledTasksTool()
        result = await tool.execute({}, online_context)
        assert result.success is True
        assert result.content["tasks"] == []
        assert result.content["count"] == 0

    @pytest.mark.asyncio
    async def test_list_shows_created_tasks(self, online_context, scheduler_env):
        """Tasks created with schedule_task must appear in list."""
        schedule_tool = ScheduleTaskTool()
        list_tool = ListScheduledTasksTool()

        await schedule_tool.execute(
            {"task_type": "email", "target": "a@b.com", "scheduled_at": "2026-12-01T10:00:00"},
            online_context,
        )
        await schedule_tool.execute(
            {"task_type": "sms", "target": "+15550000", "scheduled_at": "2026-12-02T10:00:00"},
            online_context,
        )

        result = await list_tool.execute({}, online_context)
        assert result.content["count"] == 2

    @pytest.mark.asyncio
    async def test_list_filter_by_status(self, online_context, scheduler_env):
        """list_scheduled_tasks with status filter returns only matching tasks."""
        tool = ListScheduledTasksTool()
        result = await tool.execute({"status": "pending"}, online_context)
        assert result.success is True

    @pytest.mark.asyncio
    async def test_list_invalid_status_rejected(self, online_context, scheduler_env):
        """Invalid status filter must return success=False."""
        tool = ListScheduledTasksTool()
        result = await tool.execute({"status": "not_a_valid_status"}, online_context)
        assert result.success is False
        assert "Invalid status" in result.error


class TestCancelTaskTool:
    @pytest.mark.asyncio
    async def test_cancel_pending_task(self, online_context, scheduler_env):
        """cancel_task must cancel a pending task successfully."""
        schedule_tool = ScheduleTaskTool()
        cancel_tool = CancelTaskTool()

        schedule_result = await schedule_tool.execute(
            {"task_type": "email", "target": "a@b.com", "scheduled_at": "2026-12-01T10:00:00"},
            online_context,
        )
        task_id = schedule_result.content["task_id"]

        cancel_result = await cancel_tool.execute({"task_id": task_id}, online_context)
        assert cancel_result.success is True
        assert cancel_result.content["new_status"] == "cancelled"

    @pytest.mark.asyncio
    async def test_cancel_nonexistent_task(self, online_context, scheduler_env):
        """Cancelling a non-existent task must return success=False."""
        cancel_tool = CancelTaskTool()
        result = await cancel_tool.execute({"task_id": "nonexistent-uuid"}, online_context)
        assert result.success is False
        assert "not found" in result.error.lower() or "pending" in result.error.lower()

    @pytest.mark.asyncio
    async def test_cancel_already_cancelled_task(self, online_context, scheduler_env):
        """Cancelling an already-cancelled task must return success=False."""
        schedule_tool = ScheduleTaskTool()
        cancel_tool = CancelTaskTool()

        schedule_result = await schedule_tool.execute(
            {"task_type": "sms", "target": "+1555", "scheduled_at": "2026-12-01T10:00:00"},
            online_context,
        )
        task_id = schedule_result.content["task_id"]

        # Cancel once
        await cancel_tool.execute({"task_id": task_id}, online_context)
        # Try to cancel again — must fail (not in pending state)
        second_cancel = await cancel_tool.execute({"task_id": task_id}, online_context)
        assert second_cancel.success is False
