"""
RAG retrieval — semantic search over the agent's knowledge base.

Uses ChromaDB's cosine similarity search to find the most relevant document
chunks for a given query. Embeddings are generated via nomic-embed-text
through Ollama (same model used at ingestion time).
"""

import logging
from typing import List, Tuple

from agentcore.server import get_chroma_client
from .embeddings import embed_text

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Retrieval
# ---------------------------------------------------------------------------


async def retrieve(
    query: str,
    agent_id: str,
    top_k: int = 5,
    min_score: float = 0.7,
) -> List[Tuple[str, float, dict]]:
    """Retrieve top_k most relevant chunks for query.

    Embeds the query using nomic-embed-text and performs a cosine similarity
    search in the agent's ChromaDB collection.

    Args:
        query:     The user's question or search query.
        agent_id:  The agent whose knowledge base to search.
        top_k:     Maximum number of results to return (before score filtering).
        min_score: Minimum relevance score (0.0–1.0). Results below this
                   threshold are discarded to avoid surfacing irrelevant chunks.
                   ChromaDB returns distances in [0, 2] for cosine; we convert
                   to similarity = 1 - (distance / 2).

    Returns:
        List of (chunk_text, relevance_score, metadata) tuples, sorted by
        descending relevance. Empty list if no results meet min_score.

    Raises:
        chromadb.errors.InvalidCollectionException: If the agent has no
            knowledge base yet (collection does not exist).
    """
    collection_name = f"agent_{agent_id}"
    client = get_chroma_client()

    # Check if collection exists; return empty list gracefully if not.
    try:
        collection = await client.get_collection(name=collection_name)
    except Exception:
        logger.info(
            "No knowledge base found for agent '%s' (collection '%s' does not exist)",
            agent_id,
            collection_name,
        )
        return []

    # Check collection is non-empty.
    count = await collection.count()
    if count == 0:
        logger.info("Knowledge base for agent '%s' is empty", agent_id)
        return []

    # Embed the query.
    query_embedding = await embed_text(query)

    # Query ChromaDB. We request top_k results and filter by score afterwards.
    results = await collection.query(
        query_embeddings=[query_embedding],
        n_results=min(top_k, count),  # can't request more than exist
        include=["documents", "metadatas", "distances"],
    )

    # Unpack results. ChromaDB returns nested lists (one per query).
    documents: List[str] = results["documents"][0] if results["documents"] else []
    metadatas: List[dict] = results["metadatas"][0] if results["metadatas"] else []
    distances: List[float] = results["distances"][0] if results["distances"] else []

    output: List[Tuple[str, float, dict]] = []

    for doc, meta, dist in zip(documents, metadatas, distances):
        # Convert cosine distance [0, 2] → similarity [0, 1].
        # dist=0 means identical vectors (similarity=1.0).
        similarity = 1.0 - (dist / 2.0)

        if similarity >= min_score:
            output.append((doc, similarity, meta or {}))

    # Sort by descending similarity (already sorted by ChromaDB, but be explicit).
    output.sort(key=lambda x: x[1], reverse=True)

    logger.debug(
        "Retrieval for agent '%s': query='%s...' → %d/%d results above min_score=%.2f",
        agent_id,
        query[:50],
        len(output),
        len(documents),
        min_score,
    )

    return output


# ---------------------------------------------------------------------------
# Context builder
# ---------------------------------------------------------------------------


async def build_context(
    query: str,
    agent_id: str,
    max_tokens: int = 2000,
) -> str:
    """Build RAG context string for LLM prompt.

    Retrieves relevant chunks, formats them with source citations, and
    truncates the result to fit within max_tokens (approximated as
    max_tokens * 4 characters, the rough average for English text).

    Args:
        query:      The user's question.
        agent_id:   The agent whose knowledge base to search.
        max_tokens: Approximate maximum token budget for the context block.
                    Each token ≈ 4 characters; this is a conservative estimate.

    Returns:
        A formatted context string ready to be injected into the LLM prompt.
        Returns an empty string if no relevant chunks are found.

    Example output:
        [1] Source: /data/docs/policy.pdf (page 3, score: 0.92)
        The company's refund policy states that...

        [2] Source: https://example.com/faq (score: 0.88)
        Customers may request a refund within 30 days...
    """
    chunks = await retrieve(query, agent_id)

    if not chunks:
        return ""

    # Approximate char budget: 4 chars/token, leave 10% headroom.
    char_budget = int(max_tokens * 4 * 0.9)
    parts: List[str] = []
    used_chars = 0

    for idx, (text, score, meta) in enumerate(chunks, start=1):
        # Build citation line.
        source = meta.get("source", "unknown")
        page = meta.get("page")
        if page is not None:
            citation = f"[{idx}] Source: {source} (page {page}, score: {score:.2f})"
        else:
            citation = f"[{idx}] Source: {source} (score: {score:.2f})"

        block = f"{citation}\n{text}"
        block_chars = len(block) + 2  # +2 for separator newline

        if used_chars + block_chars > char_budget:
            # Truncate the text to fit remaining budget.
            remaining = char_budget - used_chars - len(citation) - 2
            if remaining > 100:  # only include if we can fit a meaningful chunk
                truncated_text = text[:remaining].rsplit(" ", 1)[0] + " [...]"
                block = f"{citation}\n{truncated_text}"
                parts.append(block)
            break

        parts.append(block)
        used_chars += block_chars

    if not parts:
        return ""

    context = "\n\n".join(parts)
    logger.debug(
        "Built RAG context for agent '%s': %d blocks, ~%d chars",
        agent_id,
        len(parts),
        len(context),
    )
    return context
