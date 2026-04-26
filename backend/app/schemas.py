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
