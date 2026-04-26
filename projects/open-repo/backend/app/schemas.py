"""Pydantic schemas for request/response validation."""

from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, field_validator, ConfigDict


class StepModel(BaseModel):
    """Procedure step."""

    stepNumber: int
    title: Dict[str, str]
    body: Dict[str, str]
    media: List[Any] = []
    warningNote: Optional[Dict[str, str]] = None
    verificationStep: Optional[Dict[str, str]] = None


class AttributionModel(BaseModel):
    """Attribution metadata."""

    author: Optional[str] = None
    source: Optional[str] = None
    sourceTitle: Optional[str] = None


class ContentItemCreateRequest(BaseModel):
    """Request to create a new content item."""

    title: Dict[str, str]
    item_type: str = Field(..., alias="type")
    domain: str
    license: str
    description: Optional[Dict[str, str]] = None
    language: List[str] = ["en"]
    tags: List[str] = []
    wikidataLinks: List[str] = []
    attribution: Optional[AttributionModel] = None

    # Procedure-specific fields
    outcome: Optional[Dict[str, str]] = None
    difficulty: Optional[str] = None
    timeRequired: Optional[Dict[str, str]] = None
    tools: List[Dict[str, Any]] = []
    materials: List[Dict[str, Any]] = []
    steps: List[StepModel] = []
    safetyNotes: List[Dict[str, str]] = []
    performanceData: Optional[Dict[str, Any]] = None
    costEstimate: Optional[Dict[str, Any]] = None
    relatedProcedures: List[str] = []
    relatedSchematics: List[str] = []
    adaptations: List[Dict[str, Any]] = []

    # Recipe-specific fields
    category: Optional[str] = None
    subcategory: Optional[str] = None
    yield_: Optional[Dict[str, Any]] = Field(None, alias="yield")
    ingredients: List[Dict[str, Any]] = []
    equipment: List[Dict[str, Any]] = []
    storageInstructions: Optional[Dict[str, Any]] = None
    foodSafety: Optional[Dict[str, str]] = None
    scalingNotes: Optional[Dict[str, str]] = None

    model_config = ConfigDict(populate_by_name=True, extra="allow")

    @field_validator("item_type")
    @classmethod
    def validate_item_type(cls, v):
        """Validate item type is one of the allowed types."""
        allowed_types = ["procedure", "recipe", "schematic", "plan", "service-listing"]
        if v not in allowed_types:
            raise ValueError(f"Invalid item_type. Must be one of: {', '.join(allowed_types)}")
        return v


class ContentItemResponse(BaseModel):
    """Response for a content item."""

    cid: str
    title: Dict[str, str]
    item_type: str
    domain: str
    license: str
    description: Optional[Dict[str, str]] = None
    language: List[str]
    tags: List[str]
    created_at: datetime
    updated_at: datetime
    content_jsonld: Dict[str, Any]

    model_config = ConfigDict(from_attributes=True)


class ContentItemsListResponse(BaseModel):
    """Paginated list of content items."""

    items: List[ContentItemResponse]
    total: int
    limit: int
    offset: int
    has_more: bool


class HealthCheckResponse(BaseModel):
    """Health check response."""

    status: str
    version: str
    database: str


class SearchResultItem(BaseModel):
    """Individual search result item."""

    cid: str
    title: str
    description: Optional[str] = None
    tags: List[str] = []
    domain: str
    item_type: str
    author: Optional[str] = None
    created_at: Optional[str] = None


class SearchResponse(BaseModel):
    """Search results response."""

    query: str
    hits: List[SearchResultItem]
    limit: int
    offset: int
    estimated_total_hits: int
    processing_time_ms: int


class EndorsementCreateRequest(BaseModel):
    """Request to create an endorsement."""

    user_id: str
    endorsement_type: str = Field(..., pattern="^(upvote|downvote|flag)$")

    @field_validator("endorsement_type")
    @classmethod
    def validate_endorsement_type(cls, v):
        """Validate endorsement type."""
        if v not in ["upvote", "downvote", "flag"]:
            raise ValueError("endorsement_type must be one of: upvote, downvote, flag")
        return v


class EndorsementResponse(BaseModel):
    """Response for an endorsement."""

    id: int
    item_cid: str
    user_id: str
    endorsement_type: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class EndorsementStatsResponse(BaseModel):
    """Aggregated endorsement statistics."""

    item_cid: str
    upvote_count: int
    downvote_count: int
    flag_count: int
    total_count: int
    score: int


class EndorsementAuditResponse(BaseModel):
    """Audit log entry for endorsement."""

    id: int
    item_cid: str
    user_id: str
    endorsement_type: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class UserEndorsementResponse(BaseModel):
    """User's endorsement on an item (if any)."""

    endorsement: Optional[EndorsementResponse] = None


class VoteCountBreakdown(BaseModel):
    """Vote count breakdown with local, remote, and source breakdown."""

    local: int = Field(0, description="Local votes from this node")
    remote: int = Field(0, description="Remote votes from federation partners")
    total: int = Field(0, description="Total votes (local + remote)")
    breakdown: Dict[str, int] = Field(
        default_factory=dict,
        description="Vote count by source node URL"
    )


class AggregatedEndorsementStatsResponse(BaseModel):
    """Comprehensive aggregated endorsement statistics with local/remote breakdown."""

    item_cid: str
    upvote_count: VoteCountBreakdown
    downvote_count: VoteCountBreakdown
    flag_count: VoteCountBreakdown
    score: int = Field(0, description="Upvotes - downvotes (local + remote)")


# ============================================================================
# Phase 3: Contribution & Moderation Schemas
# ============================================================================


class RevisionRequest(BaseModel):
    """Individual revision request for a contribution."""

    field: str
    suggestion: str


class ContributionCreateRequest(BaseModel):
    """Request to submit a new contribution (new item or edit)."""

    contribution_type: str  # 'new_item' | 'edit_item'
    item_data: Dict[str, Any]  # Full proposed JSON-LD content
    target_item_cid: Optional[str] = None  # For edit_item: CID of item being edited
    edit_diff: Optional[Dict[str, Any]] = None  # For edit_item: structured diff
    contributor_id: Optional[str] = None  # User email or ID (anonymous if omitted)

    @field_validator("contribution_type")
    @classmethod
    def validate_contribution_type(cls, v):
        """Validate contribution type."""
        if v not in ["new_item", "edit_item"]:
            raise ValueError("contribution_type must be 'new_item' or 'edit_item'")
        return v


class ContributionUpdate(BaseModel):
    """Request to update a contribution (for resubmission after revision request)."""

    item_data: Dict[str, Any]  # Updated JSON-LD content
    edit_diff: Optional[Dict[str, Any]] = None  # For edit_item: updated diff
    submission_notes: Optional[str] = None  # Comments on revisions made


class ContributionResponse(BaseModel):
    """Response for a contribution."""

    id: int
    contribution_type: str
    status: str
    contributor_id: Optional[str]
    created_at: datetime
    updated_at: datetime
    target_item_cid: Optional[str]
    proposed_cid: Optional[str]
    reviewer_notes: Optional[str]
    rejection_reason: Optional[str]
    required_revisions: Optional[List[RevisionRequest]]
    item_data: Dict[str, Any]
    edit_diff: Optional[Dict[str, Any]]

    model_config = ConfigDict(from_attributes=True)


class ContributionDetailResponse(ContributionResponse):
    """Detailed contribution response with all metadata."""

    pass


class ContributionListResponse(BaseModel):
    """Paginated list of contributions."""

    items: List[ContributionResponse]
    total: int
    limit: int
    offset: int
    has_more: bool


class ReviewerQueueItemResponse(BaseModel):
    """Response for a reviewer queue item."""

    id: int
    contribution_id: int
    reviewer_id: str
    assigned_at: datetime
    decided_at: Optional[datetime]
    decision: Optional[str]
    reviewer_notes: Optional[str]

    model_config = ConfigDict(from_attributes=True)


class ReviewQueueItemWithContribution(BaseModel):
    """Contribution awaiting review with context."""

    contribution: ContributionResponse
    target_item: Optional[ContentItemResponse] = None  # Original item (if edit)
    review_status: str  # 'pending' | 'reviewed' | 'recused'
    assigned_at: datetime


class ReviewQueueListResponse(BaseModel):
    """Paginated list of items in the review queue."""

    items: List[ReviewQueueItemWithContribution]
    total: int
    limit: int
    offset: int
    has_more: bool


class ContributionFeedbackResponse(BaseModel):
    """Response for contribution feedback."""

    id: int
    contribution_id: int
    feedback_type: str
    severity: str
    message: str
    resolved: bool
    resolved_at: Optional[datetime]
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ReviewDecision(BaseModel):
    """Decision to approve/reject/request revisions on a contribution."""

    decision: str  # 'approve' | 'reject' | 'revision_requested'
    reviewer_notes: Optional[str] = None
    revision_requests: Optional[List[RevisionRequest]] = None

    @field_validator("decision")
    @classmethod
    def validate_decision(cls, v):
        """Validate decision type."""
        if v not in ["approve", "reject", "revision_requested"]:
            raise ValueError("decision must be 'approve', 'reject', or 'revision_requested'")
        return v


class ReviewDecisionResponse(BaseModel):
    """Response after reviewer submits a decision."""

    id: int
    review_status: str  # 'pending' | 'reviewed'
    feedback_submitted: bool
    total_feedback_count: int
    consensus_reached: bool
    final_state: Optional[str]  # 'approved', 'rejected', 'revision_requested', or None if pending consensus

    model_config = ConfigDict(from_attributes=True)


class ReviewHistoryItemResponse(BaseModel):
    """Individual review history entry."""

    id: int
    reviewer_id: str
    decision: str
    reviewer_notes: Optional[str]
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ContributorStatsResponse(BaseModel):
    """Contributor reputation and statistics."""

    user_id: str
    total_submissions: int
    approved_count: int
    rejected_count: int
    pending_count: int
    revision_requested_count: int
    approval_rate: float
    endorsement_score: int
    reputation_tier: str  # 'none' | 'trusted' | 'expert'
    first_submission: Optional[datetime]
    last_submission: Optional[datetime]


class FinalizeDecisionRequest(BaseModel):
    """Request to finalize a contribution decision (admin endpoint)."""

    final_decision: str  # 'approved' | 'rejected'
    reason: str


class FinalizeDecisionResponse(BaseModel):
    """Response after finalizing a contribution."""

    id: int
    state: str
    review_decision_reason: Optional[str]
    reviewed_at: datetime
    reviewed_by: str
    published_item_cid: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class RequestRevisionRequest(BaseModel):
    """Request revision from contributor."""

    revision_requests: List[RevisionRequest]
    deadline_days: int = 7


class RequestRevisionResponse(BaseModel):
    """Response after requesting revision."""

    id: int
    state: str
    revision_deadline: datetime
    revision_requests: List[RevisionRequest]

    model_config = ConfigDict(from_attributes=True)


# ============================================================================
# Phase 4: ActivityPub Schemas
# ============================================================================


class PublicKeyObject(BaseModel):
    """Public key object for actor."""

    id: str
    owner: str
    publicKeyPem: str


class ActorResponse(BaseModel):
    """ActivityPub actor object (node identity)."""

    id: str
    type: str = "Service"  # Actor type
    name: str
    summary: Optional[str] = None
    url: str
    inbox: str
    outbox: str
    followers: str
    following: str
    publicKey: PublicKeyObject
    preferredUsername: Optional[str] = None


class ActivityObject(BaseModel):
    """Base ActivityPub activity object."""

    context: Dict[str, Any] = Field(default_factory=lambda: [
        "https://www.w3.org/ns/activitystreams",
        "https://w3id.org/security/v1"
    ], alias="@context")
    type: str
    id: str
    actor: str
    object: Dict[str, Any]
    published: str
    to: Optional[List[str]] = None
    cc: Optional[List[str]] = None

    model_config = ConfigDict(populate_by_name=True)


class CreateActivityRequest(BaseModel):
    """Request to receive a Create activity."""

    context: Dict[str, Any] = Field(default_factory=lambda: [
        "https://www.w3.org/ns/activitystreams",
        "https://w3id.org/security/v1"
    ], alias="@context")
    type: str = "Create"
    id: str
    actor: str
    object: Dict[str, Any]
    published: str
    to: Optional[List[str]] = None
    cc: Optional[List[str]] = None

    model_config = ConfigDict(populate_by_name=True)


class UpdateActivityRequest(BaseModel):
    """Request to receive an Update activity."""

    context: Dict[str, Any] = Field(default_factory=lambda: [
        "https://www.w3.org/ns/activitystreams",
        "https://w3id.org/security/v1"
    ], alias="@context")
    type: str = "Update"
    id: str
    actor: str
    object: Dict[str, Any]
    published: str
    to: Optional[List[str]] = None
    cc: Optional[List[str]] = None

    model_config = ConfigDict(populate_by_name=True)


class DeleteActivityRequest(BaseModel):
    """Request to receive a Delete activity."""

    context: Dict[str, Any] = Field(default_factory=lambda: [
        "https://www.w3.org/ns/activitystreams",
        "https://w3id.org/security/v1"
    ], alias="@context")
    type: str = "Delete"
    id: str
    actor: str
    object: Dict[str, Any]
    published: str
    to: Optional[List[str]] = None
    cc: Optional[List[str]] = None

    model_config = ConfigDict(populate_by_name=True)


class AnnounceActivityRequest(BaseModel):
    """Request to receive an Announce activity (endorsement)."""

    context: Dict[str, Any] = Field(default_factory=lambda: [
        "https://www.w3.org/ns/activitystreams",
        "https://w3id.org/security/v1"
    ], alias="@context")
    type: str = "Announce"
    id: str
    actor: str
    object: Dict[str, Any]
    published: str
    to: Optional[List[str]] = None
    cc: Optional[List[str]] = None

    model_config = ConfigDict(populate_by_name=True)


class UndoActivityRequest(BaseModel):
    """Request to receive an Undo activity."""

    context: Dict[str, Any] = Field(default_factory=lambda: [
        "https://www.w3.org/ns/activitystreams",
        "https://w3id.org/security/v1"
    ], alias="@context")
    type: str = "Undo"
    id: str
    actor: str
    object: Dict[str, Any]
    published: str
    to: Optional[List[str]] = None
    cc: Optional[List[str]] = None

    model_config = ConfigDict(populate_by_name=True)


class ActivityResponse(BaseModel):
    """Response for stored activity."""

    id: int
    activity_type: str
    activity_id: str
    actor_url: str
    object_id: Optional[str]
    object_data: Optional[Dict[str, Any]]
    activity_data: Dict[str, Any]
    created_at: datetime
    published: datetime
    local: bool

    model_config = ConfigDict(from_attributes=True)


class OrderedCollectionItem(BaseModel):
    """Item in an ordered collection."""

    id: str
    type: str
    actor: str
    object: Dict[str, Any]
    published: str


class OrderedCollectionResponse(BaseModel):
    """OrderedCollection response (for outbox, followers, following)."""

    context: str = "https://www.w3.org/ns/activitystreams"
    id: str
    type: str = "OrderedCollection"
    totalItems: int
    first: str  # Link to first page
    last: Optional[str] = None


class OrderedCollectionPageResponse(BaseModel):
    """OrderedCollectionPage response (paginated collection)."""

    context: str = "https://www.w3.org/ns/activitystreams"
    id: str
    type: str = "OrderedCollectionPage"
    partOf: str  # Link back to the collection
    startIndex: int
    orderedItems: List[Dict[str, Any]]
    next: Optional[str] = None
    prev: Optional[str] = None


class WebFingerResponse(BaseModel):
    """WebFinger response (RFC 7033)."""

    subject: str
    links: List[Dict[str, str]]
