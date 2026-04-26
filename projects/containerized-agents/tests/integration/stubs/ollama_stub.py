"""
Ollama stub server — mimics the Ollama HTTP API for integration testing.

Implements:
  GET  /api/tags         — returns a fake model list
  POST /api/chat         — streams a deterministic NDJSON response
  POST /api/generate     — streams a deterministic NDJSON response (legacy endpoint)

The stub is intentionally minimal: it returns a fixed response string so that
integration tests can assert on content without requiring a real LLM.

Run directly:
    uvicorn ollama_stub:app --host 0.0.0.0 --port 11434
"""
from __future__ import annotations

import asyncio
import json
import time

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, StreamingResponse

app = FastAPI(title="Ollama Stub")

STUB_RESPONSE = "This is a test response from the stub LLM."
FAKE_MODEL = "qwen2.5:7b-instruct"


# ---------------------------------------------------------------------------
# /api/tags — model list
# ---------------------------------------------------------------------------


@app.get("/api/tags")
async def list_tags():
    """Return a fake model list matching Ollama's /api/tags schema."""
    return JSONResponse(
        content={
            "models": [
                {
                    "name": FAKE_MODEL,
                    "model": FAKE_MODEL,
                    "modified_at": "2025-01-01T00:00:00Z",
                    "size": 4_700_000_000,
                    "digest": "sha256:stubstubstubstub",
                    "details": {
                        "format": "gguf",
                        "family": "qwen2",
                        "families": ["qwen2"],
                        "parameter_size": "7B",
                        "quantization_level": "Q4_K_M",
                    },
                }
            ]
        }
    )


# ---------------------------------------------------------------------------
# /api/chat — streaming NDJSON chat completion
# ---------------------------------------------------------------------------


async def _stream_chat_response(model: str) -> bytes:
    """Generate NDJSON streaming chunks matching Ollama's /api/chat format."""
    words = STUB_RESPONSE.split()
    for i, word in enumerate(words):
        # Add a space before each word except the first
        content = (" " if i > 0 else "") + word
        chunk = {
            "model": model,
            "created_at": "2025-01-01T00:00:00Z",
            "message": {
                "role": "assistant",
                "content": content,
            },
            "done": False,
        }
        yield (json.dumps(chunk) + "\n").encode()
        await asyncio.sleep(0.005)  # tiny delay to simulate streaming

    # Final done chunk
    final = {
        "model": model,
        "created_at": "2025-01-01T00:00:00Z",
        "message": {
            "role": "assistant",
            "content": "",
        },
        "done": True,
        "done_reason": "stop",
        "total_duration": 100_000_000,
        "load_duration": 10_000_000,
        "prompt_eval_count": 10,
        "eval_count": len(words),
        "eval_duration": 90_000_000,
    }
    yield (json.dumps(final) + "\n").encode()


@app.post("/api/chat")
async def chat(request: Request):
    """
    Ollama /api/chat endpoint stub.

    Supports both streaming (stream=true, default) and non-streaming
    (stream=false) modes so that the OpenAI-compatible client (which uses
    /v1/chat/completions) and direct Ollama clients both work.
    """
    body = await request.json()
    model = body.get("model", FAKE_MODEL)
    stream = body.get("stream", True)

    if stream:
        return StreamingResponse(
            _stream_chat_response(model),
            media_type="application/x-ndjson",
        )
    else:
        return JSONResponse(
            content={
                "model": model,
                "created_at": "2025-01-01T00:00:00Z",
                "message": {
                    "role": "assistant",
                    "content": STUB_RESPONSE,
                },
                "done": True,
                "done_reason": "stop",
                "total_duration": 100_000_000,
                "load_duration": 10_000_000,
                "prompt_eval_count": 10,
                "eval_count": len(STUB_RESPONSE.split()),
                "eval_duration": 90_000_000,
            }
        )


# ---------------------------------------------------------------------------
# /v1/chat/completions — OpenAI-compatible endpoint (used by AsyncOpenAI client)
# ---------------------------------------------------------------------------


async def _stream_openai_response(model: str):
    """Generate SSE chunks matching OpenAI's streaming format."""
    words = STUB_RESPONSE.split()
    for i, word in enumerate(words):
        content = (" " if i > 0 else "") + word
        chunk = {
            "id": "chatcmpl-stub001",
            "object": "chat.completion.chunk",
            "created": int(time.time()),
            "model": model,
            "choices": [
                {
                    "index": 0,
                    "delta": {"role": "assistant", "content": content},
                    "finish_reason": None,
                }
            ],
        }
        yield f"data: {json.dumps(chunk)}\n\n".encode()
        await asyncio.sleep(0.005)

    # Final chunk with finish_reason
    final_chunk = {
        "id": "chatcmpl-stub001",
        "object": "chat.completion.chunk",
        "created": int(time.time()),
        "model": model,
        "choices": [
            {
                "index": 0,
                "delta": {},
                "finish_reason": "stop",
            }
        ],
    }
    yield f"data: {json.dumps(final_chunk)}\n\n".encode()
    yield b"data: [DONE]\n\n"


@app.post("/v1/chat/completions")
async def openai_chat_completions(request: Request):
    """OpenAI-compatible /v1/chat/completions endpoint for the AsyncOpenAI client."""
    body = await request.json()
    model = body.get("model", FAKE_MODEL)
    stream = body.get("stream", False)

    if stream:
        return StreamingResponse(
            _stream_openai_response(model),
            media_type="text/event-stream",
        )
    else:
        return JSONResponse(
            content={
                "id": "chatcmpl-stub001",
                "object": "chat.completion",
                "created": int(time.time()),
                "model": model,
                "choices": [
                    {
                        "index": 0,
                        "message": {
                            "role": "assistant",
                            "content": STUB_RESPONSE,
                        },
                        "finish_reason": "stop",
                    }
                ],
                "usage": {
                    "prompt_tokens": 10,
                    "completion_tokens": len(STUB_RESPONSE.split()),
                    "total_tokens": 10 + len(STUB_RESPONSE.split()),
                },
            }
        )


# ---------------------------------------------------------------------------
# /api/generate — legacy Ollama endpoint (some clients use this)
# ---------------------------------------------------------------------------


@app.post("/api/generate")
async def generate(request: Request):
    """Legacy Ollama /api/generate endpoint."""
    body = await request.json()
    model = body.get("model", FAKE_MODEL)
    stream = body.get("stream", True)

    if stream:
        async def _generate_stream():
            for i, word in enumerate(STUB_RESPONSE.split()):
                content = (" " if i > 0 else "") + word
                chunk = {
                    "model": model,
                    "created_at": "2025-01-01T00:00:00Z",
                    "response": content,
                    "done": False,
                }
                yield (json.dumps(chunk) + "\n").encode()
                await asyncio.sleep(0.005)
            final = {
                "model": model,
                "created_at": "2025-01-01T00:00:00Z",
                "response": "",
                "done": True,
                "done_reason": "stop",
            }
            yield (json.dumps(final) + "\n").encode()

        return StreamingResponse(_generate_stream(), media_type="application/x-ndjson")
    else:
        return JSONResponse(
            content={
                "model": model,
                "created_at": "2025-01-01T00:00:00Z",
                "response": STUB_RESPONSE,
                "done": True,
            }
        )


# ---------------------------------------------------------------------------
# /api/v1/heartbeat — ChromaDB-style healthcheck (in case the port is reused)
# ---------------------------------------------------------------------------


@app.get("/health")
async def health():
    return {"status": "ok", "service": "ollama-stub"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=11434)
