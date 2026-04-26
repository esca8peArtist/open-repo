"""
Embedding generation via nomic-embed-text through Ollama.
All embeddings are computed locally — no external API calls.

nomic-embed-text is an Apache 2.0-licensed embedding model that runs via
Ollama's /api/embeddings endpoint. Produces 768-dimensional vectors suitable
for semantic search with ChromaDB.
"""

import asyncio
import httpx
from typing import List

OLLAMA_BASE_URL = "http://ollama:11434"
EMBEDDING_MODEL = "nomic-embed-text"

# Timeout for a single embedding request. nomic-embed-text is fast (typically
# <200ms per request on CPU), but we allow 30s for cold-start model loading.
_REQUEST_TIMEOUT = 30.0


async def embed_text(text: str) -> List[float]:
    """Generate embedding for a single text string.

    Args:
        text: The text to embed. Will be truncated by Ollama if it exceeds
              the model's context window (8192 tokens for nomic-embed-text).

    Returns:
        A list of 768 floats representing the embedding vector.

    Raises:
        httpx.HTTPStatusError: If Ollama returns a non-2xx response.
        httpx.ConnectError: If Ollama is not reachable.
    """
    async with httpx.AsyncClient(timeout=_REQUEST_TIMEOUT) as client:
        response = await client.post(
            f"{OLLAMA_BASE_URL}/api/embeddings",
            json={
                "model": EMBEDDING_MODEL,
                "prompt": text,
            },
        )
        response.raise_for_status()
        data = response.json()
        return data["embedding"]


async def embed_batch(texts: List[str], batch_size: int = 32) -> List[List[float]]:
    """Generate embeddings for a batch of texts efficiently.

    Processes texts in batches to avoid overwhelming Ollama with concurrent
    requests. Within each batch, requests are sent concurrently.

    Args:
        texts: List of text strings to embed.
        batch_size: Number of concurrent embedding requests per batch.
                    32 is a safe default for CPU inference; reduce if OOM.

    Returns:
        List of embedding vectors in the same order as the input texts.
        Each vector is a list of 768 floats.

    Raises:
        httpx.HTTPStatusError: If any Ollama request returns a non-2xx response.
        httpx.ConnectError: If Ollama is not reachable.
    """
    if not texts:
        return []

    all_embeddings: List[List[float]] = []

    # Process in batches to control concurrency.
    for batch_start in range(0, len(texts), batch_size):
        batch = texts[batch_start : batch_start + batch_size]

        # Fire all requests in this batch concurrently.
        embeddings = await asyncio.gather(
            *[embed_text(text) for text in batch]
        )
        all_embeddings.extend(embeddings)

    return all_embeddings
