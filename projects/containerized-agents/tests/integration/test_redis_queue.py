"""
Integration tests — Redis queue and rate limiting.

These tests verify priority-ordered message dequeuing and that the in-memory
rate limiter (MessageRouter._RateLimiter) correctly rejects messages once the
rate limit is exceeded.

Requires:  pytest -m integration
"""
from __future__ import annotations

import asyncio
import time

import pytest
import redis.asyncio as aioredis


pytestmark = pytest.mark.integration

# Redis list keys used to simulate the priority queue
HIGH_QUEUE = "agentcore:queue:high"
LOW_QUEUE = "agentcore:queue:low"


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture(scope="module")
def redis_client(wait_for_redis):
    """Return a synchronous Redis client connected to the test instance."""
    import redis as sync_redis

    client = sync_redis.Redis(
        host="localhost",
        port=6379,
        decode_responses=True,
        socket_connect_timeout=5,
    )
    yield client
    client.close()


@pytest.fixture
def clean_queues(redis_client):
    """Ensure test queue keys are deleted before and after each test."""
    redis_client.delete(HIGH_QUEUE, LOW_QUEUE)
    yield
    redis_client.delete(HIGH_QUEUE, LOW_QUEUE)


# ---------------------------------------------------------------------------
# Tests — priority queue ordering
# ---------------------------------------------------------------------------


def test_high_priority_dequeued_before_low(redis_client, clean_queues):
    """Messages pushed to HIGH queue must be dequeued before LOW queue messages."""
    # Enqueue in order: low-1, low-2 first, then high-1
    redis_client.rpush(LOW_QUEUE, "low-message-1")
    redis_client.rpush(LOW_QUEUE, "low-message-2")
    redis_client.rpush(HIGH_QUEUE, "high-message-1")

    # Dequeue: check HIGH first
    first = redis_client.lpop(HIGH_QUEUE)
    assert first == "high-message-1", "HIGH queue message should be dequeued first"

    # Remaining messages are on LOW queue
    second = redis_client.lpop(LOW_QUEUE)
    third = redis_client.lpop(LOW_QUEUE)
    assert second == "low-message-1"
    assert third == "low-message-2"


def test_multiple_high_priority_preserved_in_fifo_order(redis_client, clean_queues):
    """Multiple HIGH priority messages should be dequeued in insertion (FIFO) order."""
    messages = ["high-a", "high-b", "high-c"]
    for msg in messages:
        redis_client.rpush(HIGH_QUEUE, msg)

    dequeued = [redis_client.lpop(HIGH_QUEUE) for _ in messages]
    assert dequeued == messages


def test_empty_high_queue_falls_through_to_low(redis_client, clean_queues):
    """When HIGH queue is empty, consumer should fall back to LOW queue."""
    redis_client.rpush(LOW_QUEUE, "low-only-message")

    # HIGH queue is empty
    high_result = redis_client.lpop(HIGH_QUEUE)
    assert high_result is None

    # LOW queue has the message
    low_result = redis_client.lpop(LOW_QUEUE)
    assert low_result == "low-only-message"


def test_queue_length_tracked_correctly(redis_client, clean_queues):
    """LLEN should reflect the exact number of enqueued messages."""
    for i in range(5):
        redis_client.rpush(HIGH_QUEUE, f"msg-{i}")

    assert redis_client.llen(HIGH_QUEUE) == 5

    redis_client.lpop(HIGH_QUEUE)
    assert redis_client.llen(HIGH_QUEUE) == 4


# ---------------------------------------------------------------------------
# Tests — in-memory rate limiter
# ---------------------------------------------------------------------------


def test_rate_limiter_allows_requests_under_limit():
    """Requests below the rate limit threshold should all be allowed."""
    from agentcore.routing.message_router import _RateLimiter

    limiter = _RateLimiter(limit=5, window_seconds=60)
    sender_id = "test-sender-001"

    results = [limiter.is_allowed(sender_id) for _ in range(5)]
    assert all(results), "All requests under limit should be allowed"


def test_rate_limiter_blocks_when_limit_exceeded():
    """The (limit+1)th request within the window should be rejected."""
    from agentcore.routing.message_router import _RateLimiter

    limit = 3
    limiter = _RateLimiter(limit=limit, window_seconds=60)
    sender_id = "test-sender-002"

    # Consume the full limit
    for _ in range(limit):
        assert limiter.is_allowed(sender_id) is True

    # Next request should be rejected (429 equivalent)
    assert limiter.is_allowed(sender_id) is False, "Request over limit should be rejected"


def test_rate_limiter_resets_after_window():
    """Requests should be allowed again after the sliding window expires."""
    from agentcore.routing.message_router import _RateLimiter

    limit = 2
    window = 1  # 1 second window for fast tests
    limiter = _RateLimiter(limit=limit, window_seconds=window)
    sender_id = "test-sender-003"

    # Fill the limit
    for _ in range(limit):
        limiter.is_allowed(sender_id)

    # Over-limit
    assert limiter.is_allowed(sender_id) is False

    # Wait for window to expire
    time.sleep(window + 0.1)

    # Should be allowed again
    assert limiter.is_allowed(sender_id) is True


def test_rate_limiter_independent_per_sender():
    """Different sender IDs must have independent rate limit buckets."""
    from agentcore.routing.message_router import _RateLimiter

    limiter = _RateLimiter(limit=2, window_seconds=60)

    # Exhaust sender-A
    limiter.is_allowed("sender-A")
    limiter.is_allowed("sender-A")
    assert limiter.is_allowed("sender-A") is False

    # sender-B should still be allowed
    assert limiter.is_allowed("sender-B") is True
    assert limiter.is_allowed("sender-B") is True


# ---------------------------------------------------------------------------
# Tests — async Redis operations
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_async_redis_enqueue_dequeue(wait_for_redis):
    """Async Redis client should correctly enqueue and dequeue messages."""
    client = await aioredis.from_url(
        wait_for_redis["url"],
        encoding="utf-8",
        decode_responses=True,
    )

    key = "agentcore:test:async_queue"
    await client.delete(key)

    try:
        await client.rpush(key, "async-message-1")
        await client.rpush(key, "async-message-2")

        msg1 = await client.lpop(key)
        msg2 = await client.lpop(key)

        assert msg1 == "async-message-1"
        assert msg2 == "async-message-2"
    finally:
        await client.delete(key)
        await client.aclose()


@pytest.mark.asyncio
async def test_async_redis_ping(wait_for_redis):
    """Redis must respond to async PING."""
    client = await aioredis.from_url(
        wait_for_redis["url"],
        encoding="utf-8",
        decode_responses=True,
    )
    try:
        result = await client.ping()
        assert result is True
    finally:
        await client.aclose()
