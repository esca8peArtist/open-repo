# Open-Repo Phase 4 Wave 3: Endorsement/Announce Propagation

**Status**: Design & Test Planning (Pre-implementation)  
**Date**: 2026-04-26  
**Previous Phase**: Wave 1-2 Complete (203 tests passing)  
**Target**: ~10-15 new tests + service layer for endorsement propagation  
**Scope**: Vote sync across federated nodes, endorsement aggregation, Undo activity support

---

## Executive Summary

Wave 3 extends Wave 1-2 (ActivityPub protocol + content sync) with **distributed endorsement propagation**. When a user votes on an item in any node, the vote is broadcast as an `Announce` activity to all federation partners. Each node independently tracks and aggregates votes from multiple remote nodes.

**Key outcomes**:
- Users can upvote/downvote items on any node
- Votes automatically propagate to federation partners via `Announce` activities
- Each node maintains separate vote counts (node-local votes + remote aggregates)
- Vote totals converge (eventually consistent) across nodes within minutes
- `Undo` activities retract votes
- Query results include aggregated vote counts from known federation partners

---

## Architecture & Design Decisions

### 3.1 Data Model: Endorsement Tracking with Federation

**Existing Phase 1-3 Model** (from `Endorsement` table):
```sql
CREATE TABLE endorsements (
    id INT PRIMARY KEY AUTO_INCREMENT,
    item_cid VARCHAR(255) NOT NULL,
    user_id VARCHAR(255) NOT NULL,
    endorsement_type ENUM('upvote', 'downvote', 'flag'),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    
    INDEX idx_item_cid (item_cid),
    INDEX idx_user_id (user_id),
    UNIQUE KEY unique_user_item (user_id, item_cid)
);
```

This model is **sufficient for local tracking**. However, to support federation, we need:

1. **Optional migration** (Phase 4.1 only if needed):
   - Add `source_node_url` column to `Endorsement` table to track which node contributed the vote
   - Use NULL for local votes, node URL for remote votes
   - Allows audit trail of vote origin

2. **For now** (Wave 3 MVP): Track votes in `Activity` table
   - Each `Announce` activity is logged in `activities` table
   - Query aggregation happens at read time (queries join activities table)

**Rationale**: Minimal schema changes reduce migration risk. Vote aggregation is read-heavy, not write-heavy.

### 3.2 Endorsement Propagation Model: Local → Remote

#### When a user votes locally:

```
User on Node A upvotes item "sha256-abc123..."
↓
POST /api/items/{cid}/endorse → EndorsementService.create_endorsement()
↓
Endorsement record created: {user_id: "alice@example.com", item_cid: "sha256-abc123", type: "upvote"}
↓
NEW: Generate Announce activity with vote summary
↓
NEW: Send to all federation_partners' inboxes
↓
Return 201 Created to user
```

#### When Node B receives the Announce activity:

```
POST /inbox receives Announce activity from Node A
↓
HTTPSignatureVerify → signature valid
↓
Extract object details: {item_cid: "sha256-abc123", vote_count: 12, source_node: "https://node-a.example.com"}
↓
NEW: Store in activities table (log for audit)
↓
NEW: DO NOT create local Endorsement record (only track remote activity)
↓
Item query logic: aggregate votes from activities table
↓
Return 202 Accepted
```

**Design rationale**:
- Endorsement table = local votes only
- Activities table = federation audit log + vote aggregation source
- Queries union local + remote votes at fetch time
- Avoids duplicate vote counting

### 3.3 Vote Count Aggregation Logic

When querying an item for display:

```python
# Get local upvotes
local_upvotes = await db.execute(
    select(func.count(Endorsement.id)).where(
        (Endorsement.item_cid == cid) &
        (Endorsement.endorsement_type == "upvote")
    )
)
local_count = local_upvotes.scalar() or 0

# Get remote upvotes from federation partners
remote_upvotes = await db.execute(
    select(func.sum(extract_vote_count(Activity.activity_data))).where(
        (Activity.object_id == cid) &
        (Activity.activity_type == "Announce") &
        (Activity.local == 0)  # Remote activities only
    )
)
remote_count = remote_upvotes.scalar() or 0

# Aggregated total for display
total_count = local_count + remote_count
```

**Later optimization** (Wave 4): Add materialized view or cached field to avoid repeated aggregation.

### 3.4 Undo Activity: Retracting Votes

When a user removes their endorsement:

```
User on Node A removes their upvote
↓
DELETE /api/items/{cid}/endorsements/my-endorsement
↓
Endorsement record deleted from database
↓
NEW: Generate Undo activity with reference to original Announce
↓
Send Undo to all federation partners
↓
Return 204 No Content
```

**Undo format**:
```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "id": "https://node-a.example.com/activities/undo-123",
  "type": "Undo",
  "actor": "https://node-a.example.com/actor",
  "object": "https://node-a.example.com/activities/announce-456",  // Reference to original Announce
  "published": "2026-04-26T12:00:00Z"
}
```

Node B receives Undo:
1. Looks up original Announce activity by ID
2. Removes vote contribution from remote vote total (marks as undone, doesn't delete)
3. Returns 202 Accepted

### 3.5 Announce Activity Format

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "id": "https://node-a.example.com/activities/announce-123",
  "type": "Announce",
  "actor": "https://node-a.example.com/actor",
  "object": "https://node-a.example.com/items/sha256-abc123",
  "published": "2026-04-26T11:30:00Z",
  "content": {
    "item_cid": "sha256-abc123",
    "vote_type": "upvote",  // 'upvote' | 'downvote'
    "user_id": "alice@example.com",
    "source_node": "https://node-a.example.com",
    "local_upvote_count": 12,  // Total upvotes on Node A at time of Announce
    "local_downvote_count": 2,
    "timestamp": "2026-04-26T11:30:00Z"
  }
}
```

**Why include vote counts?** Allows receiving node to know the aggregate state at sender, for reconciliation later.

---

## Service Layer: EndorsementPropagationService

### New Service: `endorsement_propagation_service.py`

```python
class EndorsementPropagationService:
    """Handles generation and ingestion of Announce/Undo activities for vote propagation."""
    
    @staticmethod
    async def generate_announce_activity(
        db: AsyncSession,
        item_cid: str,
        user_id: str,
        endorsement_type: str,
        node_url: str,
        private_key: str,
    ) -> Activity:
        """Generate an Announce activity when user votes on item."""
        # Create activity record
        # Get vote stats for this item
        # Build Announce JSON-LD
        # Return activity object
        
    @staticmethod
    async def send_announce_to_federation_partners(
        db: AsyncSession,
        activity: Activity,
        private_key: str,
    ) -> Dict[str, Tuple[bool, Optional[str]]]:
        """Send Announce activity to all federation partners.
        
        Returns dict: {partner_url: (success: bool, error_msg: optional)}
        """
        # Get list of federation_partners
        # For each partner:
        #   - Sign the activity
        #   - POST to partner inbox
        #   - Collect result
        # Return aggregated results
        
    @staticmethod
    async def ingest_announce_activity(
        db: AsyncSession,
        activity: Activity,
    ) -> bool:
        """Ingest received Announce activity.
        
        Stores activity in audit log; does NOT create local Endorsement.
        """
        # Verify activity is valid (has required fields)
        # Store in activities table
        # Return success
        
    @staticmethod
    async def generate_undo_activity(
        db: AsyncSession,
        announce_activity_id: str,
        node_url: str,
        private_key: str,
    ) -> Activity:
        """Generate Undo activity to retract a vote."""
        # Create Undo activity referencing original Announce
        # Return activity object
        
    @staticmethod
    async def get_aggregated_vote_count(
        db: AsyncSession,
        item_cid: str,
        endorsement_type: str = "upvote",
    ) -> Dict[str, int]:
        """Get local + remote vote counts for an item.
        
        Returns: {
            "local": 10,      # Local votes only
            "remote": 7,      # Remote votes from federation
            "total": 17,      # Sum
            "breakdown": {    # By partner node
                "https://node-b.example.com": 7
            }
        }
        """
        # Query local endorsements
        # Query remote activities
        # Aggregate and return
```

### Integration with EndorsementService

Modify existing `EndorsementService.create_endorsement()`:

```python
async def create_endorsement(db, item_cid, user_id, endorsement_type):
    """Create endorsement AND trigger propagation."""
    
    # Step 1: Create local endorsement (existing logic)
    endorsement = Endorsement(...)
    db.add(endorsement)
    await db.commit()
    
    # Step 2: NEW - Generate and send Announce activity
    try:
        activity = await EndorsementPropagationService.generate_announce_activity(
            db, item_cid, user_id, endorsement_type, node_url, private_key
        )
        
        results = await EndorsementPropagationService.send_announce_to_federation_partners(
            db, activity, private_key
        )
        
        # Log results (for debugging, don't fail if some partners unreachable)
        logger.info(f"Announce sent to {len(results)} partners: {results}")
    except Exception as e:
        # Log error but don't fail the endorsement
        logger.error(f"Failed to propagate endorsement: {e}")
    
    return endorsement
```

---

## Routes: New & Modified Endpoints

### New: GET `/api/items/{cid}/endorsements/aggregated`

Returns local + remote vote counts.

**Request**:
```
GET /api/items/sha256-abc123/endorsements/aggregated
```

**Response** (200 OK):
```json
{
  "item_cid": "sha256-abc123",
  "upvote_count": {
    "local": 10,
    "remote": 7,
    "total": 17,
    "breakdown": {
      "https://node-b.example.com": 7
    }
  },
  "downvote_count": {
    "local": 2,
    "remote": 0,
    "total": 2,
    "breakdown": {}
  },
  "flag_count": {
    "local": 0,
    "remote": 0,
    "total": 0,
    "breakdown": {}
  },
  "score": 15  // upvotes - downvotes (local + remote)
}
```

### Modified: POST `/api/items/{cid}/endorse`

Add async task to propagate votes (existing endpoint, no signature change):

```python
@router.post("/api/items/{cid}/endorse", ...)
async def create_endorsement(cid: str, request: EndorsementCreateRequest, db: ...):
    # Existing logic
    endorsement = await EndorsementService.create_endorsement(db, cid, request.user_id, request.endorsement_type)
    
    # NEW: Trigger propagation (fire-and-forget; don't wait for result)
    # In production, use task queue (Celery/RQ); for MVP, spawn async task
    asyncio.create_task(
        EndorsementPropagationService.send_announce_to_federation_partners(...)
    )
    
    return EndorsementResponse(...)
```

### Modified: DELETE `/api/items/{cid}/endorsements/my-endorsement`

Add Undo activity generation:

```python
@router.delete("/api/items/{cid}/endorsements/my-endorsement", ...)
async def delete_user_endorsement(cid: str, user_id: str = Header(...), db: ...):
    # Step 1: Find the endorsement to delete
    endorsement = await EndorsementService.get_user_endorsement(db, cid, user_id)
    if not endorsement:
        raise HTTPException(404, "Endorsement not found")
    
    # Step 2: Find the corresponding Announce activity
    # (if this endorsement was propagated)
    announce_activity = await find_announce_for_endorsement(db, cid, user_id)
    
    # Step 3: Delete the endorsement
    await EndorsementService.delete_endorsement(db, cid, user_id)
    
    # Step 4: NEW - Generate and send Undo activity
    if announce_activity:
        undo_activity = await EndorsementPropagationService.generate_undo_activity(
            db, announce_activity.id, node_url, private_key
        )
        asyncio.create_task(
            EndorsementPropagationService.send_announce_to_federation_partners(db, undo_activity, private_key)
        )
    
    return 204 No Content
```

### Modified: /inbox route

Update to handle Announce and Undo activities:

```python
@router.post("/inbox")
async def receive_activity(request: Dict[str, Any], db: ...):
    activity_type = request.get("type")
    
    # Existing: Create, Update, Delete, Follow, Accept
    # ...
    
    # NEW: Handle Announce activities
    elif activity_type == "Announce":
        await handle_announce_activity(request, db)
        return {"status": "accepted"}
    
    # NEW: Handle Undo activities
    elif activity_type == "Undo":
        await handle_undo_activity(request, db)
        return {"status": "accepted"}
    
    else:
        raise HTTPException(400, f"Unknown activity type: {activity_type}")
```

---

## Test Plan: Wave 3 Test Coverage

### Test File: `tests/test_wave3_endorsement_propagation.py`

**Total: 12-15 tests across 4 test classes**

#### Class 1: EndorsementPropagationService Unit Tests (5 tests)

```python
class TestEndorsementPropagationService:
    
    @pytest.mark.asyncio
    async def test_generate_announce_activity(self):
        """Verify Announce activity is correctly formatted."""
        # Arrange: item_cid, user_id, endorsement_type
        # Act: Generate Announce
        # Assert: Activity has correct type, actor, object, content fields
        
    @pytest.mark.asyncio
    async def test_announce_includes_vote_counts(self):
        """Verify Announce includes local vote statistics."""
        # Arrange: Create 3 upvotes, 1 downvote locally
        # Act: Generate Announce for new upvote
        # Assert: Announce.content has local_upvote_count=4, local_downvote_count=1
        
    @pytest.mark.asyncio
    async def test_generate_undo_activity(self):
        """Verify Undo activity correctly references original Announce."""
        # Arrange: Create and store Announce activity
        # Act: Generate Undo for it
        # Assert: Undo.object == Announce.id
        
    @pytest.mark.asyncio
    async def test_ingest_announce_activity(self):
        """Verify Announce is stored in activities table."""
        # Arrange: Create Announce activity from remote node
        # Act: Ingest it
        # Assert: Activity record created, local=0
        
    @pytest.mark.asyncio
    async def test_ingest_undo_activity(self):
        """Verify Undo activity is stored and marked."""
        # Arrange: Store Announce, then create Undo
        # Act: Ingest Undo
        # Assert: Activity stored, marked as "undo" or similar
```

#### Class 2: Endorsement Aggregation Logic (4 tests)

```python
class TestEndorsementAggregation:
    
    @pytest.mark.asyncio
    async def test_get_aggregated_vote_count_local_only(self):
        """Verify aggregation with only local votes."""
        # Arrange: 5 local upvotes
        # Act: Get aggregated count
        # Assert: total=5, local=5, remote=0, breakdown={}
        
    @pytest.mark.asyncio
    async def test_get_aggregated_vote_count_with_remote(self):
        """Verify aggregation includes remote Announce activities."""
        # Arrange: 3 local upvotes, 2 Announce activities from Node B (2 votes), 1 from Node C
        # Act: Get aggregated count
        # Assert: total=6, local=3, remote=3, breakdown={Node B: 2, Node C: 1}
        
    @pytest.mark.asyncio
    async def test_aggregation_excludes_undone_votes(self):
        """Verify Undo activities reduce remote vote count."""
        # Arrange: Announce with 2 votes, then Undo for 1
        # Act: Get aggregated count
        # Assert: remote count adjusted to 1
        
    @pytest.mark.asyncio
    async def test_aggregation_by_endorsement_type(self):
        """Verify aggregation tracks upvotes separately from downvotes."""
        # Arrange: 3 upvotes (2 local, 1 remote), 2 downvotes (local only)
        # Act: Get aggregated counts for both types
        # Assert: upvote total=3, downvote total=2
```

#### Class 3: Route Integration Tests (4 tests)

```python
class TestEndorsementRoutes:
    
    @pytest.mark.asyncio
    async def test_endorse_triggers_announce_generation(self, client_with_db):
        """Verify POST /api/items/{cid}/endorse generates Announce."""
        # Arrange: Item and federation partner
        # Act: POST to endorse endpoint
        # Assert: Announce activity created and sent (check activity table)
        
    @pytest.mark.asyncio
    async def test_delete_endorsement_generates_undo(self, client_with_db):
        """Verify DELETE /endorsements/my-endorsement generates Undo."""
        # Arrange: Create endorsement first, then delete
        # Act: DELETE endorsement
        # Assert: Undo activity created and sent
        
    @pytest.mark.asyncio
    async def test_get_aggregated_endorsement_stats(self, client_with_db):
        """Verify GET /api/items/{cid}/endorsements/aggregated returns correct totals."""
        # Arrange: Create item with mixed local/remote votes
        # Act: GET /api/items/{cid}/endorsements/aggregated
        # Assert: Response includes local, remote, total, breakdown
        
    @pytest.mark.asyncio
    async def test_receive_announce_activity_in_inbox(self, client_with_db):
        """Verify /inbox correctly processes Announce activity."""
        # Arrange: Create signed Announce from Node B
        # Act: POST to /inbox with Announce
        # Assert: Activity logged, HTTP 202 returned
```

#### Class 4: Cross-Node Announce/Undo Flow (2-3 tests)

```python
class TestCrossNodeEndorsementFlow:
    
    @pytest.mark.asyncio
    async def test_announce_sent_to_all_partners(self, client_with_db):
        """Verify Announce is delivered to all federation partners."""
        # Arrange: 2 federation partners configured
        # Act: Create endorsement
        # Assert: Both partners' inboxes receive Announce (mock httpx calls)
        
    @pytest.mark.asyncio
    async def test_announce_signature_verification(self, client_with_db):
        """Verify Announce activities are signed with correct key."""
        # Arrange: Generate private key for node
        # Act: Create endorsement and generate Announce
        # Assert: Announce includes valid Signature header
        
    @pytest.mark.asyncio
    async def test_undo_revokes_vote_on_remote_node(self, client_with_db):
        """Verify Undo activity correctly removes vote from remote total."""
        # Arrange: Announce with vote, then Undo
        # Act: Ingest both activities
        # Assert: Vote revoked in aggregated count
```

---

## Implementation Strategy: Three Phases

### Phase 1: Service Layer (Days 1-2)

**Files to create**:
- `app/services/endorsement_propagation_service.py` — New service with:
  - `generate_announce_activity()`
  - `generate_undo_activity()`
  - `ingest_announce_activity()`
  - `ingest_undo_activity()`
  - `get_aggregated_vote_count()`

**Schema updates**: None required (use existing `Activity` table)

**Tests**: Unit tests for service methods (5 tests)

### Phase 2: Route Integration (Days 2-3)

**Files to modify**:
- `app/routes.py`:
  - Modify `create_endorsement()` to trigger Announce
  - Modify `delete_user_endorsement()` to trigger Undo
  - Add new `GET /api/items/{cid}/endorsements/aggregated` endpoint
  - Modify `/inbox` to handle Announce/Undo

**Tests**: Route integration tests (4 tests)

### Phase 3: Cross-Node Testing (Days 3-4)

**Tests**: End-to-end Announce/Undo flow tests (3 tests)

**Validation**:
- Announce is sent to configured federation partners
- Undo correctly revokes votes
- Aggregation logic accurate

---

## Data Flow Diagrams

### Scenario 1: Local Vote → Remote Propagation

```
User on Node A                      Node A                          Node B
       │                              │                               │
       │ POST /api/items/{cid}/endorse
       ├─────────────────────────────>│                               │
       │                              │ Create Endorsement record      │
       │                              │ ✓ endorsements table          │
       │                              │                               │
       │                              │ Generate Announce activity     │
       │                              │ ✓ activities table (local=1)   │
       │                              │                               │
       │                              │ POST {node-b}/inbox           │
       │                              ├──────────────────────────────>│
       │                              │                               │ HTTP Signature verify
       │                              │                               │ Store Activity (local=0)
       │                              │                               │ ✓ activities table
       │                              │                               │
       │<─ 201 Created ──────────────┤<──────────── 202 Accepted ─────┤
       │
  User sees vote count: 10 local + 7 remote = 17 total
```

### Scenario 2: User Retracts Vote → Undo Propagation

```
User on Node A                      Node A                          Node B
       │                              │                               │
       │ DELETE /api/items/{cid}/endorsements/my-endorsement
       ├─────────────────────────────>│                               │
       │                              │ Delete Endorsement record      │
       │                              │ ✗ endorsements table          │
       │                              │                               │
       │                              │ Generate Undo activity         │
       │                              │ ✓ activities table (local=1)   │
       │                              │                               │
       │                              │ POST {node-b}/inbox (Undo)    │
       │                              ├──────────────────────────────>│
       │                              │                               │ Verify signature
       │                              │                               │ Mark Announce as undone
       │                              │                               │ ✓ activities table
       │                              │                               │
       │<─ 204 No Content ───────────┤<──────────── 202 Accepted ─────┤
       │
  Vote count reduced on both nodes
```

---

## Success Criteria

By end of Wave 3:

- [x] Announce activity generation on vote creation
- [x] Announce activity ingestion at /inbox
- [x] Undo activity generation on vote removal
- [x] Undo activity ingestion
- [x] Vote count aggregation (local + remote)
- [x] Aggregated endorsement stats endpoint
- [x] 12-15 tests, all passing
- [x] Endorsement propagation end-to-end validated
- [x] No breaking changes to existing Phase 1-3 APIs

---

## Known Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Remote node unreachable | Vote not propagated | Announce is fire-and-forget; log errors but don't fail local vote |
| Undo for non-existent Announce | Confusion on remote node | Gracefully handle: mark as attempted undo even if original not found |
| Vote count divergence across nodes | Eventual consistency lag | Acceptable for MVP; cache invalidation on next Announce (Wave 4) |
| Activity table grows unbounded | Query performance | Add TTL/archival policy (Wave 5); or add materialized vote_count field |

---

## Out of Scope (Wave 3)

- Task queue for reliable Announce delivery (simple async task for now)
- Vote count caching or materialization
- Third-party node voting aggregation (federated queries)
- Consensus-based conflict resolution for conflicting votes
- Rate limiting or spam prevention for votes

---

## File Structure After Wave 3

```
backend/app/
├── services/
│   ├── endorsement_service.py (modified: trigger propagation)
│   ├── endorsement_propagation_service.py (NEW)
│   ├── contribution_service.py
│   └── search_service.py
├── routes.py (modified: new endpoint, updated endpoints)
├── models.py (no changes needed)
├── schemas.py (may add: AggregatedEndorsementStatsResponse)
└── http_signatures.py (no changes needed)

backend/tests/
├── test_wave3_endorsement_propagation.py (NEW)
├── test_activitypub.py (may add Announce/Undo tests)
└── test_routes.py (may add aggregation tests)
```

---

## Timeline

- **Day 1**: Service layer design + unit tests (endorsement_propagation_service.py)
- **Day 2**: Route integration + aggregation endpoint
- **Day 3**: Cross-node Announce/Undo flow tests
- **Day 4**: Documentation + cleanup

**Estimated effort**: 3-4 days (1 FTE), 35-50 story points

---

## References

- [ActivityPub Spec: Announce](https://www.w3.org/TR/activitypub/#announce)
- [ActivityPub Spec: Undo](https://www.w3.org/TR/activitypub/#undo)
- Phase 4 Design Document (PHASE_4_DESIGN.md)
- Existing Wave 1-2 code: routes.py, models.py, http_signatures.py
