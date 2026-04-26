"""API routes for content items, search, and endorsements."""

import json
import hashlib
from typing import Optional
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models import ContentItem, Endorsement
from app.schemas import (
    ContentItemCreateRequest,
    ContentItemResponse,
    ContentItemsListResponse,
    HealthCheckResponse,
    SearchResponse,
    SearchResultItem,
    EndorsementCreateRequest,
    EndorsementResponse,
    EndorsementStatsResponse,
    EndorsementAuditResponse,
    UserEndorsementResponse,
)
from app.services.search_service import get_search_service
from app.services.endorsement_service import EndorsementService
from app import __version__

router = APIRouter()


def compute_cid(content: dict) -> str:
    """Compute SHA256-based CID for content."""
    content_str = json.dumps(content, sort_keys=True, separators=(',', ':'))
    sha256_hash = hashlib.sha256(content_str.encode()).hexdigest()
    return f"sha256-{sha256_hash}"


def build_jsonld_object(request: ContentItemCreateRequest, cid: str, node_url: str) -> dict:
    """Build full JSON-LD object from request."""
    # Base object
    obj = {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://schema.org/",
            "https://openrepo.net/ns/v1"
        ],
        "@type": request.item_type,
        "id": f"{node_url}/items/{cid}",
        "cid": cid,
        "title": request.title,
        "domain": request.domain,
        "type": request.item_type,
        "license": request.license,
        "language": request.language,
        "created": datetime.utcnow().isoformat() + "Z",
        "updated": datetime.utcnow().isoformat() + "Z",
        "tags": request.tags,
        "wikidataLinks": request.wikidataLinks,
        "endorsements": [],
        "relatedItems": [],
        "mediaItems": [],
        "node": node_url,
        "version": "1",
    }

    # Add optional fields
    if request.description:
        obj["description"] = request.description
    if request.attribution:
        obj["attribution"] = request.attribution.dict(exclude_none=True)

    # Add procedure-specific fields
    if request.item_type == "procedure":
        obj.update({
            "outcome": request.outcome,
            "difficulty": request.difficulty,
            "timeRequired": request.timeRequired,
            "tools": request.tools,
            "materials": request.materials,
            "steps": [s.dict(exclude_none=True) for s in request.steps],
            "safetyNotes": request.safetyNotes,
            "performanceData": request.performanceData,
            "costEstimate": request.costEstimate,
            "relatedSchematics": request.relatedSchematics,
            "relatedProcedures": request.relatedProcedures,
            "adaptations": request.adaptations,
        })

    # Add recipe-specific fields
    if request.item_type == "recipe":
        obj.update({
            "category": request.category,
            "subcategory": request.subcategory,
            "yield": request.yield_,
            "ingredients": request.ingredients,
            "difficulty": request.difficulty,
            "timeRequired": request.timeRequired,
            "equipment": request.equipment,
            "storageInstructions": request.storageInstructions,
            "foodSafety": request.foodSafety,
            "scalingNotes": request.scalingNotes,
            "steps": [s.dict(exclude_none=True) for s in request.steps],
        })

    return {k: v for k, v in obj.items() if v is not None}


@router.get("/health", response_model=HealthCheckResponse)
async def health_check(db: AsyncSession = Depends(get_db)):
    """Health check endpoint."""
    try:
        await db.execute(select(1))
        db_status = "healthy"
    except Exception:
        db_status = "unhealthy"

    return HealthCheckResponse(
        status="healthy" if db_status == "healthy" else "degraded",
        version=__version__,
        database=db_status,
    )


@router.post("/api/items", response_model=ContentItemResponse, status_code=201)
async def create_item(
    request: ContentItemCreateRequest,
    db: AsyncSession = Depends(get_db),
    node_url: str = "https://node.openrepo.example.org",
):
    """Create a new content item."""
    # Build the full JSON-LD object (without CID first)
    temp_obj = {
        "title": request.title,
        "domain": request.domain,
        "type": request.item_type,
        "license": request.license,
    }

    # Compute CID based on content
    cid = compute_cid(temp_obj)

    # Build full JSON-LD object
    jsonld = build_jsonld_object(request, cid, node_url)

    # Check if item already exists
    existing = await db.execute(
        select(ContentItem).where(ContentItem.cid == cid)
    )
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=409, detail="Item with this CID already exists")

    # Create database record
    item = ContentItem(
        cid=cid,
        title=request.title.get("en", ""),
        item_type=request.item_type,
        domain=request.domain,
        license=request.license,
        content_jsonld=jsonld,
        source_url=request.attribution.source if request.attribution else None,
        source_title=request.attribution.sourceTitle if request.attribution else None,
    )

    db.add(item)
    await db.commit()
    await db.refresh(item)

    # Index in Meilisearch
    try:
        search_service = get_search_service()
        description = ""
        if request.description:
            description = request.description.get("en", "")

        author = ""
        if request.attribution and request.attribution.author:
            author = request.attribution.author

        search_service.index_item(
            cid=cid,
            title=item.title,
            description=description,
            tags=request.tags,
            domain=request.domain,
            item_type=request.item_type,
            author=author,
            created_at=item.created_at.isoformat(),
        )
    except Exception as e:
        # Log error but don't fail the request if indexing fails
        print(f"Warning: Failed to index item {cid} in Meilisearch: {e}")

    return ContentItemResponse.from_orm(item)


@router.get("/api/items/{cid}", response_model=ContentItemResponse)
async def get_item(cid: str, db: AsyncSession = Depends(get_db)):
    """Retrieve a single content item by CID."""
    result = await db.execute(
        select(ContentItem).where(ContentItem.cid == cid)
    )
    item = result.scalar_one_or_none()

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    return ContentItemResponse.from_orm(item)


@router.get("/api/items", response_model=ContentItemsListResponse)
async def list_items(
    db: AsyncSession = Depends(get_db),
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    item_type: Optional[str] = Query(None),
    domain: Optional[str] = Query(None),
    tags: Optional[str] = Query(None),
):
    """List content items with pagination and optional filters."""
    # Build query
    query = select(ContentItem)

    # Apply filters
    if item_type:
        query = query.where(ContentItem.item_type == item_type)
    if domain:
        query = query.where(ContentItem.domain == domain)
    if tags:
        # Simple tag filter: any of the provided tags
        tag_list = [t.strip() for t in tags.split(",")]
        # This is a simplified implementation; a more robust version would use
        # PostgreSQL JSON operators or full-text search
        query = query.where(
            ContentItem.content_jsonld["tags"].astext.contains(tag_list[0])
        )

    # Get total count
    count_result = await db.execute(
        select(func.count(ContentItem.cid)).select_from(ContentItem)
    )
    total = count_result.scalar()

    # Get paginated results
    query = query.order_by(ContentItem.created_at.desc())
    query = query.limit(limit).offset(offset)

    result = await db.execute(query)
    items = result.scalars().all()

    return ContentItemsListResponse(
        items=[ContentItemResponse.from_orm(item) for item in items],
        total=total,
        limit=limit,
        offset=offset,
        has_more=(offset + limit) < total,
    )


@router.get("/api/items/search", response_model=SearchResponse)
async def search_items(
    q: str = Query(..., min_length=1, description="Search query"),
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    item_type: Optional[str] = Query(None),
    domain: Optional[str] = Query(None),
    tags: Optional[str] = Query(None),
):
    """Search for content items using full-text search.

    Search is performed against: title, description, categories, author, tags
    """
    search_service = get_search_service()

    # Parse tags if provided
    tag_list = None
    if tags:
        tag_list = [t.strip() for t in tags.split(",")]

    # Perform search
    results = search_service.search(
        query=q,
        limit=limit,
        offset=offset,
        item_type=item_type,
        domain=domain,
        tags=tag_list,
    )

    # Transform results
    hits = [
        SearchResultItem(
            cid=hit.get("cid"),
            title=hit.get("title", ""),
            description=hit.get("description"),
            tags=hit.get("tags", []),
            domain=hit.get("domain", ""),
            item_type=hit.get("item_type", ""),
            author=hit.get("author"),
            created_at=hit.get("created_at"),
        )
        for hit in results.get("hits", [])
    ]

    return SearchResponse(
        query=q,
        hits=hits,
        limit=limit,
        offset=offset,
        estimated_total_hits=results.get("estimated_total_hits", 0),
        processing_time_ms=results.get("processing_time_ms", 0),
    )


@router.post("/api/items/{cid}/endorse", response_model=EndorsementResponse, status_code=201)
async def create_endorsement(
    cid: str,
    request: EndorsementCreateRequest,
    db: AsyncSession = Depends(get_db),
):
    """Submit an endorsement for a content item.

    Endorsement types: upvote, downvote, flag
    If the user already has an endorsement, it will be updated.
    """
    # Verify item exists
    result = await db.execute(select(ContentItem).where(ContentItem.cid == cid))
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    # Create or update endorsement
    endorsement = await EndorsementService.create_endorsement(
        db=db,
        item_cid=cid,
        user_id=request.user_id,
        endorsement_type=request.endorsement_type,
    )

    return EndorsementResponse.from_orm(endorsement)


@router.get("/api/items/{cid}/endorsements", response_model=EndorsementStatsResponse)
async def get_endorsement_stats(
    cid: str,
    db: AsyncSession = Depends(get_db),
):
    """Get aggregated endorsement statistics for an item.

    Returns upvote count, downvote count, flag count, and overall score.
    """
    # Verify item exists
    result = await db.execute(select(ContentItem).where(ContentItem.cid == cid))
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    stats = await EndorsementService.get_endorsement_stats(db=db, item_cid=cid)
    return EndorsementStatsResponse(**stats)


@router.get("/api/items/{cid}/endorsements/my-endorsement", response_model=UserEndorsementResponse)
async def get_user_endorsement(
    cid: str,
    user_id: str = Query(..., description="User identifier"),
    db: AsyncSession = Depends(get_db),
):
    """Get a specific user's endorsement for an item (if any).

    Returns null if the user has not endorsed the item.
    """
    # Verify item exists
    result = await db.execute(select(ContentItem).where(ContentItem.cid == cid))
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    endorsement = await EndorsementService.get_user_endorsement(
        db=db, item_cid=cid, user_id=user_id
    )

    return UserEndorsementResponse(
        endorsement=EndorsementResponse.from_orm(endorsement) if endorsement else None
    )


@router.delete("/api/items/{cid}/endorsements/my-endorsement", status_code=204)
async def delete_user_endorsement(
    cid: str,
    user_id: str = Query(..., description="User identifier"),
    db: AsyncSession = Depends(get_db),
):
    """Delete a user's endorsement for an item."""
    # Verify item exists
    result = await db.execute(select(ContentItem).where(ContentItem.cid == cid))
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    await EndorsementService.delete_endorsement(db=db, item_cid=cid, user_id=user_id)
    return None


@router.get("/admin/items/{cid}/endorsements", response_model=list[EndorsementAuditResponse])
async def get_endorsement_audit_log(
    cid: str,
    db: AsyncSession = Depends(get_db),
):
    """Get full endorsement audit log for an item (admin endpoint).

    Returns all endorsements for the item in reverse chronological order.
    """
    # Verify item exists
    result = await db.execute(select(ContentItem).where(ContentItem.cid == cid))
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    endorsements = await EndorsementService.get_endorsements_for_item(db=db, item_cid=cid)
    return [EndorsementAuditResponse.from_orm(e) for e in endorsements]
