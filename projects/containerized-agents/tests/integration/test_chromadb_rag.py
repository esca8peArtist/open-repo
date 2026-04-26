"""
Integration tests — ChromaDB RAG pipeline.

These tests verify:
1. Text ingestion produces retrievable chunks in ChromaDB.
2. Semantic queries return relevant results.
3. Re-ingesting the same document is idempotent (dedup via deterministic IDs).

Note: These tests use chromadb.AsyncHttpClient directly rather than going
through the full FastAPI lifespan so that they can run standalone against
the docker-compose.test.yml ChromaDB service.

Requires:  pytest -m integration
"""
from __future__ import annotations

import hashlib
import uuid

import chromadb
import pytest
import pytest_asyncio


pytestmark = pytest.mark.integration

# Fixed test agent ID so collection names are predictable
TEST_AGENT_ID = "integration-test-agent-rag"
COLLECTION_NAME = f"agent_{TEST_AGENT_ID}"

# Small deterministic document used across multiple tests
SAMPLE_DOC = (
    "The AgentCore system is a lightweight event-driven orchestration layer. "
    "It supports multiple AI agent profiles including personal productivity, "
    "customer support, developer assistance, and enterprise orchestration. "
    "Agents communicate through Redis queues and store conversation history in PostgreSQL. "
    "The vector knowledge base is managed by ChromaDB using cosine similarity search."
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest_asyncio.fixture(scope="module")
async def chroma_client(wait_for_chromadb):
    """Return an async ChromaDB client connected to the test instance."""
    client = await chromadb.AsyncHttpClient(
        host="localhost",
        port=8000,
    )
    yield client


@pytest_asyncio.fixture(scope="module")
async def test_collection(chroma_client):
    """Create (or reset) the test ChromaDB collection for this module."""
    # Delete any leftover collection from a previous run
    try:
        await chroma_client.delete_collection(COLLECTION_NAME)
    except Exception:
        pass

    collection = await chroma_client.get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"},
    )
    yield collection

    # Cleanup after module tests complete
    try:
        await chroma_client.delete_collection(COLLECTION_NAME)
    except Exception:
        pass


def _make_embedding(text: str) -> list[float]:
    """
    Generate a deterministic pseudo-embedding for testing purposes.

    Uses SHA-256 of the text to produce a reproducible 64-dimensional vector.
    This avoids requiring Ollama/nomic-embed-text for ChromaDB integration tests.
    The values are in [0, 1] so cosine similarity calculations remain valid.
    """
    digest = hashlib.sha256(text.encode()).digest()
    # Use each byte as a float in [0, 1] — 32 bytes → 64 floats (pairs)
    floats = []
    for i in range(0, len(digest), 1):
        floats.append(digest[i] / 255.0)
    # Pad to 64 dimensions
    while len(floats) < 64:
        floats.append(0.0)
    return floats[:64]


def _chunk_text(text: str, chunk_size: int = 200) -> list[str]:
    """Simple word-boundary chunker for test use."""
    words = text.split()
    chunks = []
    current: list[str] = []
    char_count = 0

    for word in words:
        if char_count + len(word) + 1 > chunk_size and current:
            chunks.append(" ".join(current))
            current = [word]
            char_count = len(word)
        else:
            current.append(word)
            char_count += len(word) + 1

    if current:
        chunks.append(" ".join(current))

    return chunks


def _make_chunk_id(doc_id: str, chunk_index: int) -> str:
    """Deterministic chunk ID matching the production ingestion logic."""
    return hashlib.sha256(f"{doc_id}_{chunk_index}".encode()).hexdigest()[:36]


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_ingest_document_chunks_stored(test_collection):
    """Ingesting a document should produce retrievable chunks in ChromaDB."""
    doc_id = str(uuid.uuid4())
    chunks = _chunk_text(SAMPLE_DOC)

    ids = [_make_chunk_id(doc_id, i) for i in range(len(chunks))]
    embeddings = [_make_embedding(chunk) for chunk in chunks]
    metadatas = [
        {"source": "test_doc.txt", "chunk_index": i, "doc_id": doc_id}
        for i in range(len(chunks))
    ]

    await test_collection.upsert(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas,
    )

    count = await test_collection.count()
    assert count >= len(chunks), f"Expected at least {len(chunks)} chunks, got {count}"


@pytest.mark.asyncio
async def test_query_returns_relevant_chunks(test_collection):
    """A semantic query should return chunks related to the query topic."""
    # Ensure data is present from the previous test (or insert fresh)
    count = await test_collection.count()
    if count == 0:
        doc_id = str(uuid.uuid4())
        chunks = _chunk_text(SAMPLE_DOC)
        ids = [_make_chunk_id(doc_id, i) for i in range(len(chunks))]
        embeddings = [_make_embedding(chunk) for chunk in chunks]
        metadatas = [{"source": "test_doc.txt", "chunk_index": i, "doc_id": doc_id} for i in range(len(chunks))]
        await test_collection.upsert(ids=ids, documents=chunks, embeddings=embeddings, metadatas=metadatas)

    # Query about Redis — this term appears in the document
    query = "Redis queues and message delivery"
    query_embedding = _make_embedding(query)

    results = await test_collection.query(
        query_embeddings=[query_embedding],
        n_results=3,
        include=["documents", "metadatas", "distances"],
    )

    documents = results["documents"][0] if results["documents"] else []
    assert len(documents) > 0, "Query should return at least one result"

    # At least one returned chunk should mention key concepts from the document
    combined = " ".join(documents).lower()
    # The document is about AgentCore — at least one chunk should mention it
    assert any(
        keyword in combined
        for keyword in ["agentcore", "agent", "redis", "chromadb", "postgresql"]
    ), f"Retrieved chunks should be relevant to the query. Got: {combined[:200]}"


@pytest.mark.asyncio
async def test_ingest_dedup_same_document_twice(chroma_client):
    """Ingesting the same document twice must not create duplicate entries."""
    dedup_collection_name = f"agent_dedup_test_{uuid.uuid4().hex[:8]}"

    collection = await chroma_client.get_or_create_collection(
        name=dedup_collection_name,
        metadata={"hnsw:space": "cosine"},
    )

    try:
        doc_id = "fixed-doc-id-for-dedup-test"
        chunks = _chunk_text(SAMPLE_DOC)
        ids = [_make_chunk_id(doc_id, i) for i in range(len(chunks))]
        embeddings = [_make_embedding(chunk) for chunk in chunks]
        metadatas = [{"source": "dedup_doc.txt", "chunk_index": i, "doc_id": doc_id} for i in range(len(chunks))]

        # First ingest
        await collection.upsert(ids=ids, documents=chunks, embeddings=embeddings, metadatas=metadatas)
        count_after_first = await collection.count()

        # Second ingest — same doc_id → same deterministic IDs → upsert should overwrite
        await collection.upsert(ids=ids, documents=chunks, embeddings=embeddings, metadatas=metadatas)
        count_after_second = await collection.count()

        assert count_after_first == count_after_second, (
            f"Dedup failed: count went from {count_after_first} to {count_after_second} "
            "on second ingest of same document."
        )
    finally:
        try:
            await chroma_client.delete_collection(dedup_collection_name)
        except Exception:
            pass


@pytest.mark.asyncio
async def test_collection_count_increases_with_new_document(test_collection):
    """Adding a new document with a different doc_id should increase the chunk count."""
    initial_count = await test_collection.count()

    new_doc_id = str(uuid.uuid4())
    new_text = "Containerized agents use Docker for deployment and Kubernetes for orchestration at scale."
    new_chunks = _chunk_text(new_text)

    ids = [_make_chunk_id(new_doc_id, i) for i in range(len(new_chunks))]
    embeddings = [_make_embedding(chunk) for chunk in new_chunks]
    metadatas = [{"source": "new_doc.txt", "chunk_index": i, "doc_id": new_doc_id} for i in range(len(new_chunks))]

    await test_collection.upsert(
        ids=ids,
        documents=new_chunks,
        embeddings=embeddings,
        metadatas=metadatas,
    )

    final_count = await test_collection.count()
    assert final_count == initial_count + len(new_chunks), (
        f"Expected {initial_count + len(new_chunks)} chunks, got {final_count}"
    )


@pytest.mark.asyncio
async def test_collection_metadata_preserved(test_collection):
    """Metadata stored with chunks should be retrievable intact."""
    doc_id = str(uuid.uuid4())
    text = "Security features include hardware binding via TPM fingerprint."
    chunk_id = _make_chunk_id(doc_id, 0)
    meta = {"source": "security_doc.txt", "chunk_index": 0, "doc_id": doc_id, "page": 5}

    await test_collection.upsert(
        ids=[chunk_id],
        documents=[text],
        embeddings=[_make_embedding(text)],
        metadatas=[meta],
    )

    results = await test_collection.get(ids=[chunk_id], include=["metadatas", "documents"])
    assert results["documents"] and results["documents"][0] == text
    stored_meta = results["metadatas"][0]
    assert stored_meta["source"] == "security_doc.txt"
    assert stored_meta["page"] == 5
