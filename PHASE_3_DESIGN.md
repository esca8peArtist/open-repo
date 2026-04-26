# Open-Repo Phase 3: Contributions & Moderation Workflow

**Status**: Design Document (Pre-implementation)  
**Version**: 1.0  
**Date**: 2026-04-26  
**Target**: ~280–320 story points (3–4 weeks, 2 FTE)

---

## Executive Summary

Phase 3 introduces a **community-driven contribution workflow** that allows anonymous users to submit new items or propose edits to existing items, with a structured moderation pipeline for approval, rejection, or revision requests. This enables collaborative content improvement while maintaining editorial quality through peer review.

**Key outcomes**:
- Users can submit new items as **drafts** (non-published)
- Users can propose **edits** to existing items via a diff-like mechanism
- Reviewers (elected/admin) approve, reject, or request revisions
- Rejected submissions are logged with feedback; accepted submissions merge into published items
- Contribution history is auditable; endorsements count toward contributor reputation

---

## Architecture Overview

### Data Model Extensions

#### 1. **Contribution Table** (new)

Tracks all user submissions (new items or edits).

```sql
CREATE TABLE contributions (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    contribution_type VARCHAR(20) NOT NULL,  -- 'new_item' | 'edit_item'
    state VARCHAR(20) NOT NULL,  -- 'pending' | 'approved' | 'rejected' | 'revision_requested'
    
    -- Contributor metadata
    submitted_by VARCHAR(255) NOT NULL,  -- user_id, email, or DID
    submitted_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    reviewed_by VARCHAR(255),  -- reviewer_id who made final decision
    reviewed_at DATETIME,
    
    -- Content references
    target_item_cid VARCHAR(255),  -- NULL for new_item, populated for edit_item (FK to content_items)
    proposed_cid VARCHAR(255),  -- CID of the proposed content (for new items)
    proposed_content_jsonld JSON NOT NULL,  -- Full proposed JSON-LD
    
    -- Edit-specific: what changed?
    edit_diff JSON,  -- Structured diff showing {field: {old: x, new: y}} for edits
    
    -- Decision metadata
    review_decision_reason TEXT,  -- Why approved/rejected/revision-requested
    revision_requests JSON,  -- Array of {field: string, suggestion: string}[]
    
    -- Status tracking
    approval_score INT,  -- Net endorsement score from reviewers (if endorsement-based review)
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    INDEX idx_state (state),
    INDEX idx_submitted_by (submitted_by),
    INDEX idx_target_item_cid (target_item_cid),
    INDEX idx_created_at (created_at)
);
```

#### 2. **ReviewerQueueItem Table** (new)

Tracks which reviewers are assigned to which contributions.

```sql
CREATE TABLE reviewer_queue_items (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    contribution_id BIGINT NOT NULL,  -- FK to contributions
    reviewer_user_id VARCHAR(255) NOT NULL,
    assigned_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    reviewed_at DATETIME,
    review_status VARCHAR(20),  -- 'pending' | 'reviewed' | 'recused'
    
    FOREIGN KEY (contribution_id) REFERENCES contributions(id),
    INDEX idx_reviewer (reviewer_user_id),
    INDEX idx_status (review_status),
    UNIQUE KEY unique_contribution_reviewer (contribution_id, reviewer_user_id)
);
```

#### 3. **ContributionFeedback Table** (new)

Individual reviewer comments/decisions (supports round-robin review).

```sql
CREATE TABLE contribution_feedback (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    contribution_id BIGINT NOT NULL,  -- FK to contributions
    reviewer_user_id VARCHAR(255) NOT NULL,
    decision VARCHAR(20) NOT NULL,  -- 'approve' | 'reject' | 'revision_requested'
    feedback TEXT,  -- Reviewer's justification
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    
    FOREIGN KEY (contribution_id) REFERENCES contributions(id),
    INDEX idx_contribution (contribution_id),
    INDEX idx_reviewer (reviewer_user_id)
);
```

### Pydantic Schemas (New)

```python
# Contribution schemas

class ContributionCreateRequest(BaseModel):
    """Request to submit a new contribution (new item or edit)."""
    contribution_type: str  # 'new_item' | 'edit_item'
    proposed_content_jsonld: Dict[str, Any]  # Full proposed content
    
    # For edit_item only
    target_item_cid: Optional[str] = None  # CID of item being edited
    edit_diff: Optional[Dict[str, Any]] = None  # {field: {old: x, new: y}}
    
    # Metadata
    submitted_by: Optional[str] = None  # User email or ID (anonymous if omitted)
    submission_notes: Optional[str] = None  # Optional comments from contributor


class ContributionResponse(BaseModel):
    """Response for a contribution."""
    id: int
    contribution_type: str
    state: str
    submitted_by: Optional[str]
    submitted_at: datetime
    target_item_cid: Optional[str]
    proposed_cid: Optional[str]
    review_decision_reason: Optional[str]
    approval_score: int
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


class ContributionReviewDecision(BaseModel):
    """Decision to approve/reject/revise a contribution."""
    decision: str  # 'approve' | 'reject' | 'revision_requested'
    feedback: Optional[str] = None
    revision_requests: Optional[List[Dict[str, str]]] = None  # [{field: "...", suggestion: "..."}]


class ContributionListResponse(BaseModel):
    """Paginated list of contributions."""
    items: List[ContributionResponse]
    total: int
    limit: int
    offset: int
    has_more: bool


class ReviewQueueResponse(BaseModel):
    """Contribution awaiting review."""
    contribution: ContributionResponse
    target_item: Optional[ContentItemResponse] = None  # Original item (if edit)
    review_status: str  # 'pending' | 'reviewed' | 'recused'
    assigned_at: datetime
```

---

## API Endpoints (Phase 3)

### Contribution Submission

#### `POST /api/contributions`

Submit a new item or propose an edit to an existing item (anonymous or authenticated).

**Request Body**:
```json
{
  "contribution_type": "new_item",
  "proposed_content_jsonld": {
    "@context": [...],
    "@type": "procedure",
    "title": {"en": "Composting 101"},
    "domain": "procedural",
    "license": "CC-BY-4.0",
    ...
  },
  "submitted_by": "user@example.com",
  "submission_notes": "OpenFarm content, verified accuracy"
}
```

For edits:
```json
{
  "contribution_type": "edit_item",
  "target_item_cid": "sha256-...",
  "proposed_content_jsonld": { ... full updated item ... },
  "edit_diff": {
    "title": {
      "en": {"old": "Old Title", "new": "Better Title"}
    },
    "description": {
      "en": {"old": "...", "new": "Improved description..."}
    }
  },
  "submitted_by": "user@example.com",
  "submission_notes": "Fixed typos and clarified steps 3-5"
}
```

**Response** (201 Created):
```json
{
  "id": 1,
  "contribution_type": "new_item",
  "state": "pending",
  "submitted_by": "user@example.com",
  "submitted_at": "2026-04-26T10:15:00Z",
  "target_item_cid": null,
  "proposed_cid": "sha256-abc123...",
  "review_decision_reason": null,
  "approval_score": 0,
  "created_at": "2026-04-26T10:15:00Z",
  "updated_at": "2026-04-26T10:15:00Z"
}
```

**Status codes**:
- **201 Created**: Contribution accepted for review
- **400 Bad Request**: Invalid content structure or missing required fields
- **409 Conflict**: For new_item, if proposed_cid already exists as published item

---

#### `GET /api/contributions`

List contributions (public: pending only; admin: all states).

**Query Parameters**:
- `limit` (default: 10, max: 100)
- `offset` (default: 0)
- `state` (optional): Filter by state (`pending`, `approved`, `rejected`, `revision_requested`)
- `contribution_type` (optional): Filter by type (`new_item`, `edit_item`)
- `submitted_by` (optional): Filter by submitter (admin only)

**Response** (200 OK):
```json
{
  "items": [ ... ],
  "total": 42,
  "limit": 10,
  "offset": 0,
  "has_more": true
}
```

---

#### `GET /api/contributions/{contribution_id}`

Retrieve a single contribution (with diff and proposed content).

**Response** (200 OK):
```json
{
  "id": 1,
  "contribution_type": "edit_item",
  "state": "pending",
  "submitted_by": "user@example.com",
  "submitted_at": "2026-04-26T10:15:00Z",
  "target_item_cid": "sha256-existing...",
  "proposed_cid": "sha256-proposed...",
  "proposed_content_jsonld": { ... },
  "edit_diff": {
    "title": {"en": {"old": "...", "new": "..."}},
    ...
  },
  "revision_requests": [
    {"field": "steps[2].body", "suggestion": "Add safety note about heat"},
    {"field": "materials", "suggestion": "Include sourcing links"}
  ],
  "review_decision_reason": null,
  "approval_score": 2,
  "created_at": "2026-04-26T10:15:00Z",
  "updated_at": "2026-04-26T10:45:00Z"
}
```

**Error responses**:
- **404 Not Found**: Contribution ID does not exist

---

### Review Workflow (Reviewer/Admin endpoints)

#### `GET /api/review/queue`

Get pending contributions awaiting review (paginated). Reviewers see assigned items.

**Query Parameters**:
- `limit` (default: 10, max: 50)
- `offset` (default: 0)
- `assignment_status` (optional): `pending` | `reviewed` | `recused`

**Response** (200 OK):
```json
{
  "items": [
    {
      "contribution": { ... },
      "target_item": { ... },  // Null for new_item
      "review_status": "pending",
      "assigned_at": "2026-04-26T09:00:00Z"
    }
  ],
  "total": 15,
  "limit": 10,
  "offset": 0,
  "has_more": true
}
```

---

#### `POST /api/contributions/{contribution_id}/review`

Reviewer submits a review decision (approve, reject, or revision-requested).

**Request Body**:
```json
{
  "decision": "revision_requested",
  "feedback": "Good submission! A few improvements would strengthen it.",
  "revision_requests": [
    {
      "field": "steps[3].body",
      "suggestion": "Add warning about pH levels"
    },
    {
      "field": "safetyNotes",
      "suggestion": "Include precautions for sensitive skin"
    }
  ]
}
```

**Response** (200 OK):
```json
{
  "id": 1,
  "review_status": "pending",  // Stays pending until consensus or threshold reached
  "feedback_submitted": true,
  "total_feedback_count": 1,
  "consensus_reached": false,
  "final_state": null
}
```

**Status codes**:
- **200 OK**: Feedback recorded
- **403 Forbidden**: User not assigned as reviewer
- **404 Not Found**: Contribution ID does not exist
- **409 Conflict**: Contribution already in terminal state (approved/rejected)

---

#### `POST /api/contributions/{contribution_id}/review/{review_decision}`

**Shorthand endpoint** for simple approve/reject decisions (no detailed feedback).

- `POST /api/contributions/1/review/approve` → Auto-approves (if threshold met or solo reviewer)
- `POST /api/contributions/1/review/reject` → Auto-rejects with optional reason
- `POST /api/contributions/1/review/recuse` → Reviewer withdraws from review queue

---

#### `GET /api/contributions/{contribution_id}/review-history`

Get all reviewer feedback for a contribution (audit log).

**Response** (200 OK):
```json
[
  {
    "id": 1,
    "reviewer_user_id": "alice@example.com",
    "decision": "revision_requested",
    "feedback": "Good content, needs clarification on step 3",
    "created_at": "2026-04-26T10:30:00Z"
  },
  {
    "id": 2,
    "reviewer_user_id": "bob@example.com",
    "decision": "approve",
    "feedback": null,
    "created_at": "2026-04-26T11:00:00Z"
  }
]
```

---

### Contribution Resolution

#### `POST /api/contributions/{contribution_id}/finalize`

Admin endpoint to finalize a contribution (transition to approved/rejected/revision_requested).

**Request Body**:
```json
{
  "final_decision": "approved",
  "reason": "Consensus of 3 reviewers reached"
}
```

**Response** (200 OK):
```json
{
  "id": 1,
  "state": "approved",
  "review_decision_reason": "Consensus of 3 reviewers reached",
  "reviewed_at": "2026-04-26T12:00:00Z",
  "reviewed_by": "admin@example.com",
  "published_item_cid": "sha256-..." // Only if approved
}
```

**Side effects when approved**:
- For `new_item`: Create new `ContentItem` with `proposed_content_jsonld`
- For `edit_item`: Update target `ContentItem` with merged changes, increment version
- Update contribution state to `approved`
- Log contributor ID in item's JSON-LD (`contributedBy` array)

---

#### `POST /api/contributions/{contribution_id}/request-revision`

Admin/reviewers request revision from contributor (response expected within 7 days).

**Request Body**:
```json
{
  "revision_requests": [
    {"field": "steps[2].body", "suggestion": "Clarify the heating temperature"},
    {"field": "safetyNotes", "suggestion": "Add warning for children"}
  ],
  "deadline_days": 7
}
```

**Response** (200 OK):
```json
{
  "id": 1,
  "state": "revision_requested",
  "revision_deadline": "2026-05-03T12:00:00Z",
  "revision_requests": [ ... ]
}
```

---

### Contributor Reputation & Metrics

#### `GET /api/contributors/{user_id}/stats`

Contributor's submission statistics and reputation score.

**Response** (200 OK):
```json
{
  "user_id": "user@example.com",
  "total_submissions": 5,
  "approved_count": 3,
  "rejected_count": 1,
  "pending_count": 1,
  "approval_rate": 0.75,
  "endorsement_score": 24,  // Sum of endorsement scores on their approved items
  "reputation_tier": "trusted",  // none | trusted | expert (based on approval_rate & endorsement_score)
  "first_submission": "2026-04-01T...",
  "last_submission": "2026-04-26T..."
}
```

---

## State Machine Diagram

```
    ┌─────────────┐
    │   PENDING   │  (awaiting reviewer assignment & feedback)
    └──────┬──────┘
           │
        (reviewer submits feedback or admin decision)
           │
      ┌────┴────────────────────────┐
      │                             │
      ↓                             ↓
┌──────────────────┐      ┌──────────────────┐
│ REVISION_REQUESTED│      │ APPROVED/REJECTED │
└────────┬─────────┘      └──────────────────┘
         │                         ↓
    (contributor                 FINAL
     resubmits)              (published or
         │                    archived)
         ↓
    ┌─────────┐
    │ PENDING │ (new review cycle)
    └─────────┘


Legend:
- PENDING: Awaiting reviewer decision
- REVISION_REQUESTED: Contributor invited to improve; re-enters PENDING after resubmit
- APPROVED: Content merged into live items; contributor credited
- REJECTED: Archived with feedback; contributor can resubmit
```

---

## Implementation Strategy

### Wave 1: Data Model & Schemas (Days 1–2)

- [x] Create `contributions`, `reviewer_queue_items`, `contribution_feedback` tables
- [x] Define Pydantic schemas for all contribution types
- [x] Add SQLAlchemy ORM models
- [ ] Run migrations (Alembic)
- **Tests**: 8 (schema validation, ORM instantiation)

### Wave 2: Contribution Submission API (Days 3–4)

- [ ] `POST /api/contributions` → Store new/edit submissions
- [ ] `GET /api/contributions`, `GET /api/contributions/{id}`
- [ ] Compute `edit_diff` for edit-type submissions (JSON field comparison)
- [ ] Validate proposed content against schema
- [ ] Auto-assign reviewers (round-robin or reputation-based)
- **Tests**: 12 (submission CRUD, diff computation, auto-assignment)

### Wave 3: Review Workflow (Days 5–7)

- [ ] `GET /api/review/queue` (paginated with assignment status)
- [ ] `POST /api/contributions/{id}/review` (feedback submission)
- [ ] `GET /api/contributions/{id}/review-history` (audit log)
- [ ] Reviewer consensus logic (e.g., 2+ approve → auto-approve; 1+ reject + no approvals → auto-reject)
- [ ] State transitions (PENDING → REVISION_REQUESTED or APPROVED/REJECTED)
- **Tests**: 15 (review feedback, consensus, state machine transitions)

### Wave 4: Finalization & Content Merge (Days 8–9)

- [ ] `POST /api/contributions/{id}/finalize` (admin endpoint)
- [ ] For approved `new_item`: Create new `ContentItem`
- [ ] For approved `edit_item`: Merge changes into existing item, version increment
- [ ] Update `content_jsonld` to include `contributedBy` metadata
- [ ] `POST /api/contributions/{id}/request-revision` (deadline tracking)
- **Tests**: 10 (content merge, version incrementing, contrib history)

### Wave 5: Contributor Stats & Reputation (Days 10)

- [ ] `GET /api/contributors/{user_id}/stats`
- [ ] Compute approval_rate, endorsement_score aggregates
- [ ] Reputation tier logic (none/trusted/expert)
- [ ] Dashboard/leaderboard endpoint (optional Phase 3.5)
- **Tests**: 8 (aggregation queries, tier computation)

---

## Test Strategy

**Total new tests: ~53–60 tests** (across 5 test files)

| Feature | Test Count | Examples |
|---------|-----------|----------|
| **Schemas** | 8 | Valid/invalid contribution types, required fields, diff validation |
| **Submission** | 12 | Create new_item, create edit_item, duplicate detection, auto-assign |
| **Review** | 15 | Submit feedback, consensus logic, state transitions, recusal |
| **Finalization** | 10 | Merge new item, apply edits, version bump, metadata |
| **Reputation** | 8 | Approval rate, endorsement aggregation, tier assignment |

**Coverage target**: ≥90% for contribution_service.py, >85% overall

---

## Data Model: Full Contribution Lifecycle

### Example: New Item Submission

```json
POST /api/contributions
{
  "contribution_type": "new_item",
  "proposed_content_jsonld": {
    "@context": [...],
    "@type": "procedure",
    "title": {"en": "Rainwater Harvesting"},
    "domain": "procedural",
    ...
  },
  "submitted_by": "alex@community.org",
  "submission_notes": "Original content, tested locally"
}

→ HTTP 201

{
  "id": 42,
  "state": "pending",
  "proposed_cid": "sha256-rain123...",
  "submitted_at": "2026-04-26T14:00:00Z",
  ...
}

[Reviewers assigned automatically: alice@..., bob@..., charlie@...]

(7 hours later)

POST /api/contributions/42/review
{
  "decision": "approve",
  "feedback": "Great content, well-structured"
}

→ HTTP 200, feedback recorded (1/3 approvals)

(4 hours later)

POST /api/contributions/42/review
{
  "decision": "approve",
  "feedback": null
}

→ HTTP 200, feedback recorded (2/3 approvals)
→ Triggers auto-approval (consensus reached)
→ state transitions: "pending" → "approved"

[System auto-calls POST /api/contributions/42/finalize]

→ HTTP 200
→ New ContentItem created with cid "sha256-rain123..."
→ Contributor alex@community.org credited in item's contributedBy[]
→ GET /api/contributors/alex@community.org/stats shows +1 approved
```

### Example: Edit Submission

```json
POST /api/contributions
{
  "contribution_type": "edit_item",
  "target_item_cid": "sha256-potato456...",
  "proposed_content_jsonld": { ...full updated content... },
  "edit_diff": {
    "steps[2].body": {
      "en": {
        "old": "Hill the soil around plants",
        "new": "Hill the soil around plants when they reach 6-8 inches tall"
      }
    },
    "safetyNotes": {
      "old": [...],
      "new": [..., "Wear gloves when handling lime-based fertilizers"]
    }
  },
  "submitted_by": "bot@openfarm.org",
  "submission_notes": "Clarification from user feedback"
}

→ HTTP 201

[2-reviewer consensus required for edits; both approve within 2 hours]

→ state: "pending" → "approved"
→ Target item (sha256-potato456...) updated with changes
→ Item version incremented: 1 → 2
→ contributedBy field includes both original author and bot@openfarm.org
→ GET /api/items/sha256-potato456... returns merged content + updated_at timestamp
```

---

## Permission Model

| Role | Can Submit | Can Review | Can Finalize | Can See All |
|------|-----------|-----------|-------------|-----------|
| **Anonymous User** | Yes (pending only) | No | No | No (own only) |
| **Authenticated User** | Yes | If assigned | No | No (own + queue) |
| **Reviewer (elected)** | Yes | Yes (assigned) | No | Yes (pending) |
| **Admin** | Yes | Yes (all) | Yes | Yes (all) |

**Access control**:
- `POST /api/contributions`: Public (no auth required)
- `GET /api/review/queue`: Requires reviewer role
- `POST /api/contributions/{id}/finalize`: Requires admin role
- `GET /api/contributors/{user_id}/stats`: Public (aggregate data only)

---

## Performance Considerations

1. **Indexing**: State, submitted_by, target_item_cid, created_at
2. **Pagination**: Max 100 items per page (review queue may be large)
3. **Diff computation**: For large items (>10KB JSON), defer diff calculation to background job
4. **Endorsement aggregation**: Cache `approval_score` in contributions table; refresh on endorsement change
5. **Queue assignment**: Use database read lock to prevent race conditions in round-robin

---

## Future Enhancements (Phase 3.5+)

- **Email notifications** for reviewers, contributors (revision requests, approvals)
- **Weighted reputation** based on endorsement scores of approved items
- **Bulk operations** for admins (batch approve, reject, reassign)
- **Contribution templates** for common item types
- **API key auth** for bot submissions (OpenFarm import pipeline)
- **Webhook events** when contributions transition state (for external dashboards)
- **Revision history** tracking: Store old proposed_content_jsonld versions on revision request

---

## Effort Estimation

| Component | Hours | Story Points | Rationale |
|-----------|-------|--------------|-----------|
| Data model + migrations | 4 | 3 | Straightforward SQL; Alembic auto-generation |
| Pydantic schemas | 4 | 3 | Schema definition + validators |
| Submission API (CRUD) | 8 | 5 | Diff computation, auto-assignment logic |
| Review workflow | 12 | 8 | Consensus logic, state transitions |
| Finalization + merge | 8 | 5 | Content merging, version incrementing |
| Reputation service | 6 | 4 | Aggregation queries, tier logic |
| Tests (comprehensive) | 16 | 10 | 53–60 tests, mocking reviewers/state |
| **Total** | **58 hours** | **38 points** | **3.5–4 weeks (1 FTE)** |

---

## Success Metrics

By end of Phase 3:
- ✓ 53+ tests, all passing, ≥90% coverage on new services
- ✓ All 5 endpoint groups fully functional (submission, review queue, finalization, history, stats)
- ✓ State machine handles edge cases (reviewer recusal, revision deadlines, consensus logic)
- ✓ Contributor reputation scores populate and rank correctly
- ✓ Endorsements on approved items correctly attributed to original + contributor
- ✓ Full audit trail: all review decisions logged with timestamps and feedback

---
