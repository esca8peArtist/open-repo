"""
Chat endpoints — synchronous and SSE streaming.

POST /api/chat         — complete response in one JSON payload
POST /api/chat/stream  — Server-Sent Events stream of response chunks

Both endpoints accept a ChatRequest body and require X-API-Key authentication.

The sub-3-second response target is achieved by:
1. Streaming directly from Ollama rather than buffering the full completion
2. Avoiding synchronous blocking I/O (all database and cache calls are async)
3. Reusing AgentInstance objects across requests (cached in AgentRegistry)
"""
from __future__ import annotations

import asyncio
import json
import logging

from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.responses import StreamingResponse

from agentcore.models import ChatRequest, ChatResponse

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api", tags=["chat"])


# ---------------------------------------------------------------------------
# Auth dependency (shared with agents router)
# ---------------------------------------------------------------------------


async def _require_api_key(request: Request) -> None:
    """Validate X-API-Key header against the configured secret."""
    settings = request.app.state.settings
    provided = request.headers.get("X-API-Key", "")
    if not provided or provided != settings.api_secret_key:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or missing API key.")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


async def _get_agent(request: Request, agent_id: str):
    """Retrieve a live AgentInstance from the registry or raise 404."""
    registry = request.app.state.registry
    agent = await registry.get_agent(agent_id)
    if agent is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Agent '{agent_id}' not found or inactive.",
        )
    return agent


def _sse_event(data: dict) -> str:
    """Format a dict as a Server-Sent Events 'data:' line."""
    return f"data: {json.dumps(data)}\n\n"


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------


@router.post("/chat", response_model=ChatResponse, dependencies=[Depends(_require_api_key)])
async def chat(chat_req: ChatRequest, request: Request) -> ChatResponse:
    """
    Synchronous chat endpoint.

    Blocks until the full response is available.  Suitable for programmatic
    callers that prefer a single JSON response over a stream.

    Enforces the request_timeout setting; returns 504 if the agent exceeds it.
    """
    settings = request.app.state.settings
    agent = await _get_agent(request, chat_req.agent_id)

    try:
        response = await asyncio.wait_for(
            agent.chat(
                chat_req.message,
                session_id=chat_req.session_id,
                stream=False,
                conversation_id=chat_req.conversation_id,
            ),
            timeout=settings.request_timeout,
        )
    except asyncio.TimeoutError:
        raise HTTPException(
            status_code=status.HTTP_504_GATEWAY_TIMEOUT,
            detail=f"Agent did not respond within {settings.request_timeout} seconds.",
        )
    except Exception as exc:
        logger.exception("Chat error for agent %s: %s", chat_req.agent_id, exc)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while processing your message.",
        )

    return response


@router.post("/chat/stream", dependencies=[Depends(_require_api_key)])
async def chat_stream(chat_req: ChatRequest, request: Request) -> StreamingResponse:
    """
    Streaming chat endpoint — returns an SSE stream.

    Each event has the form:
        data: {"delta": "...", "done": false, "session_id": "..."}

    The final event has `done: true` with an empty delta.

    Designed for the web chat UI and any SSE-capable client.  The first chunk
    should arrive within ~1 second for a warm Ollama instance (sub-3-second
    requirement per the spec).
    """
    # Validate agent exists before initiating stream (avoids silent 404 mid-stream)
    agent = await _get_agent(request, chat_req.agent_id)
    session_id = chat_req.session_id
    conversation_id = chat_req.conversation_id

    async def event_generator():
        try:
            async for chunk in agent.chat_stream(
                chat_req.message,
                session_id=session_id,
                conversation_id=conversation_id,
            ):
                if await request.is_disconnected():
                    logger.debug("SSE client disconnected mid-stream for session %s", session_id)
                    break
                yield _sse_event({"delta": chunk, "done": False, "session_id": session_id})

            # Final "done" event
            yield _sse_event({"delta": "", "done": True, "session_id": session_id})

        except Exception as exc:
            logger.exception("Stream error for agent %s session %s: %s", chat_req.agent_id, session_id, exc)
            yield _sse_event(
                {
                    "delta": "",
                    "done": True,
                    "session_id": session_id,
                    "error": "Stream interrupted. Please try again.",
                }
            )

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",  # disable nginx buffering
        },
    )


@router.delete("/chat/session/{session_id}", dependencies=[Depends(_require_api_key)])
async def clear_session(agent_id: str, session_id: str, request: Request):
    """
    Clear a conversation session's history for the given agent.

    Useful when the user wants to start a fresh conversation without switching agents.
    """
    agent = await _get_agent(request, agent_id)
    agent.clear_session(session_id)
    return {"session_id": session_id, "status": "cleared"}


@router.get("/chat/session/{session_id}/history", dependencies=[Depends(_require_api_key)])
async def get_session_history(agent_id: str, session_id: str, request: Request):
    """Return the full conversation history for a session (for debugging / UI display)."""
    agent = await _get_agent(request, agent_id)
    messages = agent.get_session_messages(session_id)
    return {"session_id": session_id, "messages": [m.model_dump() for m in messages]}
