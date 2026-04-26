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
