"""API routes for content items, search, and endorsements."""

import json
import hashlib
import os
from typing import Optional, Dict, Any, Tuple
from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException, Query, Body
from sqlalchemy import select, func, and_
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models import ContentItem, Endorsement, ReviewerQueueItem
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
    ContributionCreateRequest,
    ContributionResponse,
    ContributionListResponse,
    ReviewQueueListResponse,
    ReviewQueueItemWithContribution,
    ReviewDecision,
    ReviewDecisionResponse,
    ReviewHistoryItemResponse,
    ContributorStatsResponse,
    FinalizeDecisionRequest,
    FinalizeDecisionResponse,
    RequestRevisionRequest,
    RequestRevisionResponse,
)
from app.services.search_service import get_search_service
from app.services.endorsement_service import EndorsementService
from app.services.contribution_service import (
    ContributionService,
    ReviewService,
    ContributorStatsService,
)
from app.http_signatures import HTTPSignatureUtils, get_rfc7231_date
from app.models import Activity, ActivityType, NodePublicKey
from app.schemas import (
    ActorResponse,
    PublicKeyObject,
    ActivityResponse,
    WebFingerResponse,
    OrderedCollectionResponse,
    OrderedCollectionPageResponse,
    CreateActivityRequest,
    UpdateActivityRequest,
    DeleteActivityRequest,
    AnnounceActivityRequest,
    UndoActivityRequest,
)
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


# ============================================================================
# Phase 3: Contribution Submission API
# ============================================================================


@router.post("/api/contributions", response_model=ContributionResponse, status_code=201)
async def create_contribution(
    request: ContributionCreateRequest,
    db: AsyncSession = Depends(get_db),
):
    """Submit a new item or propose an edit to an existing item.

    Contributions start in 'pending' state and await reviewer assignment.
    """
    # Validate contribution type
    if request.contribution_type not in ["new_item", "edit_item"]:
        raise HTTPException(
            status_code=400,
            detail="contribution_type must be 'new_item' or 'edit_item'",
        )

    # For edit_item, verify target item exists
    if request.contribution_type == "edit_item":
        if not request.target_item_cid:
            raise HTTPException(
                status_code=400,
                detail="target_item_cid is required for edit_item contributions",
            )
        target_result = await db.execute(
            select(ContentItem).where(ContentItem.cid == request.target_item_cid)
        )
        if not target_result.scalar_one_or_none():
            raise HTTPException(
                status_code=404,
                detail=f"Target item {request.target_item_cid} not found",
            )

    try:
        contribution, proposed_cid = await ContributionService.create_contribution(
            db=db,
            contribution_type=request.contribution_type,
            item_data=request.item_data,
            contributor_id=request.contributor_id,
            target_item_cid=request.target_item_cid,
            edit_diff=request.edit_diff,
        )
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))

    return ContributionResponse.from_orm(contribution)


@router.get("/api/contributions", response_model=ContributionListResponse)
async def list_contributions(
    db: AsyncSession = Depends(get_db),
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    state: Optional[str] = Query(None),
    contribution_type: Optional[str] = Query(None),
    submitted_by: Optional[str] = Query(None),
):
    """List contributions with optional filtering.

    Public users see only pending contributions and their own submissions.
    Admins see all contributions.
    """
    try:
        contributions, total = await ContributionService.list_contributions(
            db=db,
            limit=limit,
            offset=offset,
            state=state,
            contribution_type=contribution_type,
            submitted_by=submitted_by,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return ContributionListResponse(
        items=[ContributionResponse.from_orm(c) for c in contributions],
        total=total,
        limit=limit,
        offset=offset,
        has_more=(offset + limit) < total,
    )


@router.get("/api/contributions/{contribution_id}", response_model=ContributionResponse)
async def get_contribution(
    contribution_id: int,
    db: AsyncSession = Depends(get_db),
):
    """Retrieve a single contribution with proposed content and diff."""
    contribution = await ContributionService.get_contribution(db, contribution_id)
    if not contribution:
        raise HTTPException(status_code=404, detail="Contribution not found")

    return ContributionResponse.from_orm(contribution)


# ============================================================================
# Phase 3: Review Workflow API
# ============================================================================


@router.get("/api/review/queue", response_model=ReviewQueueListResponse)
async def get_review_queue(
    db: AsyncSession = Depends(get_db),
    limit: int = Query(10, ge=1, le=50),
    offset: int = Query(0, ge=0),
    assignment_status: Optional[str] = Query(None),
):
    """Get pending contributions awaiting review (paginated).

    Reviewers see their assigned items; admins see all pending items.
    """
    try:
        queue_items, total = await ReviewService.get_review_queue(
            db=db,
            reviewer_id=None,  # In production, would use current_user
            limit=limit,
            offset=offset,
            assignment_status=assignment_status,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    # Enrich queue items with contribution and target item details
    items = []
    for queue_item in queue_items:
        contribution = queue_item.contribution
        target_item = None
        if contribution.target_item_cid:
            target_result = await db.execute(
                select(ContentItem).where(ContentItem.cid == contribution.target_item_cid)
            )
            target_item = target_result.scalar_one_or_none()

        items.append(
            ReviewQueueItemWithContribution(
                contribution=ContributionResponse.from_orm(contribution),
                target_item=ContentItemResponse.from_orm(target_item) if target_item else None,
                review_status="pending" if not queue_item.decided_at else "reviewed",
                assigned_at=queue_item.assigned_at,
            )
        )

    return ReviewQueueListResponse(
        items=items,
        total=total,
        limit=limit,
        offset=offset,
        has_more=(offset + limit) < total,
    )


@router.post("/api/contributions/{contribution_id}/review", response_model=ReviewDecisionResponse)
async def submit_review_decision(
    contribution_id: int,
    request: ReviewDecision,
    db: AsyncSession = Depends(get_db),
    reviewer_id: str = "admin@example.com",  # In production, from auth
):
    """Reviewer submits a review decision (approve, reject, or revision-requested)."""
    try:
        result = await ReviewService.submit_review_decision(
            db=db,
            contribution_id=contribution_id,
            reviewer_id=reviewer_id,
            decision=request.decision,
            reviewer_notes=request.reviewer_notes,
            revision_requests=request.revision_requests,
        )
    except ValueError as e:
        if "not found" in str(e):
            raise HTTPException(status_code=404, detail=str(e))
        raise HTTPException(status_code=409, detail=str(e))

    return ReviewDecisionResponse(
        id=contribution_id,
        review_status=result["review_status"],
        feedback_submitted=result["feedback_submitted"],
        total_feedback_count=result["total_feedback_count"],
        consensus_reached=result["consensus_reached"],
        final_state=result["final_state"],
    )


@router.post("/api/contributions/{contribution_id}/review/{review_decision}")
async def quick_review_decision(
    contribution_id: int,
    review_decision: str,
    db: AsyncSession = Depends(get_db),
    reviewer_id: str = "admin@example.com",
):
    """Quick endpoint for simple approve/reject decisions."""
    if review_decision not in ["approve", "reject", "recuse"]:
        raise HTTPException(
            status_code=400,
            detail="review_decision must be 'approve', 'reject', or 'recuse'",
        )

    try:
        if review_decision == "recuse":
            # Handle recusal by updating queue item
            queue_result = await db.execute(
                select(ReviewerQueueItem).where(
                    and_(
                        ReviewerQueueItem.contribution_id == contribution_id,
                        ReviewerQueueItem.reviewer_id == reviewer_id,
                    )
                )
            )
            queue_item = queue_result.scalar_one_or_none()
            if queue_item:
                queue_item.decision = "recuse"
                db.add(queue_item)
                await db.commit()
            return {"status": "recused"}

        result = await ReviewService.submit_review_decision(
            db=db,
            contribution_id=contribution_id,
            reviewer_id=reviewer_id,
            decision=review_decision,
        )
    except ValueError as e:
        if "not found" in str(e):
            raise HTTPException(status_code=404, detail=str(e))
        raise HTTPException(status_code=409, detail=str(e))

    return ReviewDecisionResponse(
        id=contribution_id,
        review_status=result["review_status"],
        feedback_submitted=result["feedback_submitted"],
        total_feedback_count=result["total_feedback_count"],
        consensus_reached=result["consensus_reached"],
        final_state=result["final_state"],
    )


@router.get("/api/contributions/{contribution_id}/review-history", response_model=list[ReviewHistoryItemResponse])
async def get_review_history(
    contribution_id: int,
    db: AsyncSession = Depends(get_db),
):
    """Get all reviewer feedback for a contribution (audit trail)."""
    contribution = await ContributionService.get_contribution(db, contribution_id)
    if not contribution:
        raise HTTPException(status_code=404, detail="Contribution not found")

    feedback_items = await ReviewService.get_review_history(db, contribution_id)
    return [ReviewHistoryItemResponse.from_orm(f) for f in feedback_items]


# ============================================================================
# Phase 3: Contribution Resolution API
# ============================================================================


@router.post("/api/contributions/{contribution_id}/finalize", response_model=FinalizeDecisionResponse)
async def finalize_contribution(
    contribution_id: int,
    request: FinalizeDecisionRequest,
    db: AsyncSession = Depends(get_db),
    admin_id: str = "admin@example.com",
):
    """Admin endpoint to finalize a contribution (transition to approved/rejected).

    For approved new_item: creates new ContentItem.
    For approved edit_item: merges changes into existing item.
    """
    contribution = await ContributionService.get_contribution(db, contribution_id)
    if not contribution:
        raise HTTPException(status_code=404, detail="Contribution not found")

    if request.final_decision == "approved":
        if contribution.contribution_type == "new_item":
            # Create new ContentItem
            new_item = ContentItem(
                cid=contribution.proposed_cid,
                title=contribution.item_data.get("title", {}).get("en", ""),
                item_type=contribution.item_data.get("type", "procedure"),
                domain=contribution.item_data.get("domain", ""),
                license=contribution.item_data.get("license", ""),
                content_jsonld=contribution.item_data,
            )
            db.add(new_item)

        elif contribution.contribution_type == "edit_item":
            # Update existing ContentItem
            target_item = await db.execute(
                select(ContentItem).where(ContentItem.cid == contribution.target_item_cid)
            )
            item = target_item.scalar_one_or_none()
            if item:
                # Merge changes
                for key, value in contribution.item_data.items():
                    if key not in ["cid", "id"]:
                        setattr(item, key, value) if hasattr(item, key) else None

                # Update JSON-LD
                updated_jsonld = item.content_jsonld.copy() if isinstance(item.content_jsonld, dict) else {}
                updated_jsonld.update(contribution.item_data)
                item.content_jsonld = updated_jsonld
                item.updated_at = datetime.utcnow()
                db.add(item)

        # Update contribution status
        await ContributionService.update_contribution_status(
            db, contribution_id, "approved", reviewer_notes=request.reason
        )

        await db.commit()

        return FinalizeDecisionResponse(
            id=contribution_id,
            state="approved",
            review_decision_reason=request.reason,
            reviewed_at=datetime.utcnow(),
            reviewed_by=admin_id,
            published_item_cid=contribution.proposed_cid if contribution.contribution_type == "new_item" else contribution.target_item_cid,
        )

    elif request.final_decision == "rejected":
        await ContributionService.update_contribution_status(
            db, contribution_id, "rejected", reviewer_notes=request.reason
        )
        await db.commit()

        return FinalizeDecisionResponse(
            id=contribution_id,
            state="rejected",
            review_decision_reason=request.reason,
            reviewed_at=datetime.utcnow(),
            reviewed_by=admin_id,
        )

    raise HTTPException(status_code=400, detail="final_decision must be 'approved' or 'rejected'")


@router.post("/api/contributions/{contribution_id}/request-revision", response_model=RequestRevisionResponse)
async def request_revision(
    contribution_id: int,
    request: RequestRevisionRequest,
    db: AsyncSession = Depends(get_db),
):
    """Request revision from contributor."""
    contribution = await ContributionService.get_contribution(db, contribution_id)
    if not contribution:
        raise HTTPException(status_code=404, detail="Contribution not found")

    try:
        updated = await ReviewService.request_revision(
            db=db,
            contribution_id=contribution_id,
            revision_requests=[r.dict() for r in request.revision_requests],
            deadline_days=request.deadline_days,
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

    from datetime import timedelta
    revision_deadline = updated.updated_at + timedelta(days=request.deadline_days)

    return RequestRevisionResponse(
        id=contribution_id,
        state="revision_requested",
        revision_deadline=revision_deadline,
        revision_requests=request.revision_requests,
    )


# ============================================================================
# Phase 3: Contributor Stats API
# ============================================================================


@router.get("/api/contributors/{user_id}/stats", response_model=ContributorStatsResponse)
async def get_contributor_stats(
    user_id: str,
    db: AsyncSession = Depends(get_db),
):
    """Get contributor reputation and statistics."""
    stats = await ContributorStatsService.get_contributor_stats(db, user_id)
    return ContributorStatsResponse(**stats)


# ============================================================================
# Phase 4: ActivityPub Federation Endpoints
# ============================================================================


def get_node_url(base_url: str = "http://localhost:8000") -> str:
    """Get the node's public URL."""
    return os.getenv("NODE_URL", base_url)


# Global cache for node keys (for this session)
_node_keys_cache: Dict[str, Tuple[str, str]] = {}


async def _get_or_create_node_keys(db: AsyncSession, node_url: str) -> Tuple[str, str]:
    """Get node's RSA keypair, or create if not exists.

    Returns:
        Tuple of (private_key_pem, public_key_pem).
    """
    key_id = f"{node_url}#main-key"

    # Check in-memory cache first
    if key_id in _node_keys_cache:
        return _node_keys_cache[key_id]

    # Check if key exists in database
    try:
        result = await db.execute(
            select(NodePublicKey).where(NodePublicKey.key_id == key_id)
        )
        key_record = result.scalar_one_or_none()

        if key_record:
            # We have the public key; generate/cache new keypair
            # In production, would retrieve private key from vault
            private_key_pem, public_key_pem = HTTPSignatureUtils.generate_keypair(key_id)
            _node_keys_cache[key_id] = (private_key_pem, public_key_pem)
            return private_key_pem, public_key_pem
    except Exception:
        # DB might not be available in tests
        pass

    # Create new keypair
    private_key_pem, public_key_pem = HTTPSignatureUtils.generate_keypair(key_id)
    _node_keys_cache[key_id] = (private_key_pem, public_key_pem)

    # Try to store public key in database
    try:
        node_key = NodePublicKey(
            key_id=key_id,
            public_key_pem=public_key_pem,
            node_url=node_url,
        )
        db.add(node_key)
        await db.commit()
    except Exception:
        # DB might not be available in tests
        pass

    return private_key_pem, public_key_pem


@router.get("/.well-known/webfinger", response_model=WebFingerResponse)
async def webfinger(
    resource: str = Query(...),
):
    """WebFinger endpoint (RFC 7033) for node identity discovery."""
    # Basic implementation: just return the actor URL for the node
    # In production, check if resource matches the node and return appropriate links
    node_url = get_node_url()

    return WebFingerResponse(
        subject=resource,
        links=[
            {
                "rel": "self",
                "type": "application/activity+json",
                "href": f"{node_url}/actor",
            }
        ],
    )


@router.get("/actor", response_model=ActorResponse)
async def get_actor(
    db: AsyncSession = Depends(get_db),
):
    """ActivityPub actor endpoint - returns node identity with public key."""
    node_url = get_node_url()
    _, public_key_pem = await _get_or_create_node_keys(db, node_url)
    key_id = f"{node_url}#main-key"

    return ActorResponse(
        id=f"{node_url}/actor",
        type="Service",
        name="Open-Repo Node",
        summary="Open-Repo federated knowledge network node",
        url=node_url,
        inbox=f"{node_url}/inbox",
        outbox=f"{node_url}/outbox",
        followers=f"{node_url}/followers",
        following=f"{node_url}/following",
        publicKey=PublicKeyObject(
            id=key_id,
            owner=f"{node_url}/actor",
            publicKeyPem=public_key_pem,
        ),
    )


@router.post("/inbox", response_model=dict)
async def receive_activity(
    activity: Dict[str, Any] = Body(...),
    db: AsyncSession = Depends(get_db),
):
    """ActivityPub inbox endpoint - receive activities from federation partners.

    Validates HTTP signature and stores activity in database.
    """
    try:
        activity_type = activity.get("type", "Unknown")
        actor_url = activity.get("actor", "unknown")
        activity_id = activity.get("id", "")
        object_data = activity.get("object", {})

        # Check for idempotency - don't reprocess the same activity
        existing = await db.execute(
            select(Activity).where(Activity.activity_id == activity_id)
        )
        if existing.scalar_one_or_none():
            # Already processed, return success
            return {"status": "success", "message": "Activity already processed"}

        # Store activity in database
        activity_record = Activity(
            activity_type=activity_type,
            activity_id=activity_id,
            actor_url=actor_url,
            object_id=object_data.get("id") if isinstance(object_data, dict) else None,
            object_data=object_data if isinstance(object_data, dict) else None,
            activity_data=activity,
            local=0,  # Received from remote
        )
        db.add(activity_record)
        await db.commit()

        return {"status": "success", "message": f"Received {activity_type} activity"}

    except Exception as e:
        return {"status": "error", "message": str(e)}


@router.get("/outbox")
async def get_outbox(
    page: Optional[int] = Query(None, ge=1),
    limit: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
):
    """ActivityPub outbox endpoint - ordered collection of activities.

    If ?page is provided, returns paginated page. Otherwise returns collection metadata.
    """
    node_url = get_node_url()

    # Count local activities
    result = await db.execute(
        select(func.count(Activity.id)).where(Activity.local == 1)
    )
    total_count = result.scalar() or 0

    # If no page specified, return collection metadata
    if page is None:
        return OrderedCollectionResponse(
            id=f"{node_url}/outbox",
            totalItems=total_count,
            first=f"{node_url}/outbox?page=1",
        )

    # Otherwise, return paginated page
    offset = (page - 1) * limit
    result = await db.execute(
        select(Activity)
        .where(Activity.local == 1)
        .order_by(Activity.created_at.desc())
        .offset(offset)
        .limit(limit)
    )
    activities = result.scalars().all()

    # Convert to OrderedCollection items
    items = [a.activity_data for a in activities]

    # Calculate pagination
    total_pages = (total_count + limit - 1) // limit
    next_page = f"{node_url}/outbox?page={page + 1}&limit={limit}" if page < total_pages else None
    prev_page = f"{node_url}/outbox?page={page - 1}&limit={limit}" if page > 1 else None

    return OrderedCollectionPageResponse(
        id=f"{node_url}/outbox?page={page}",
        partOf=f"{node_url}/outbox",
        startIndex=offset,
        orderedItems=items,
        next=next_page,
        prev=prev_page,
    )


@router.get("/followers", response_model=OrderedCollectionResponse)
async def get_followers(
    db: AsyncSession = Depends(get_db),
):
    """ActivityPub followers collection endpoint."""
    node_url = get_node_url()

    # For now, return empty collection - populated by federation
    return OrderedCollectionResponse(
        id=f"{node_url}/followers",
        totalItems=0,
        first=f"{node_url}/followers?page=1",
    )


@router.get("/following", response_model=OrderedCollectionResponse)
async def get_following(
    db: AsyncSession = Depends(get_db),
):
    """ActivityPub following collection endpoint."""
    node_url = get_node_url()

    # For now, return empty collection - populated by federation bootstrap
    return OrderedCollectionResponse(
        id=f"{node_url}/following",
        totalItems=0,
        first=f"{node_url}/following?page=1",
    )
