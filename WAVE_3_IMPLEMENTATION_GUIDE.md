# Phase 4 Wave 3 Implementation Guide

**Quick reference for implementing Endorsement/Announce propagation**

## Files to Implement

### 1. `app/services/endorsement_propagation_service.py`
**Status**: Stub created with method signatures and TODOs  
**Lines**: 7 methods, ~130 lines with TODOs  
**Priority**: HIGH - Core service logic

#### Methods to implement (in order):

```python
# 1. Core activity generation
generate_announce_activity(db, item_cid, user_id, endorsement_type, node_url, private_key)
→ Returns: Activity object with Announce type

# 2. Activity delivery
send_announce_to_federation_partners(db, activity, private_key)
→ Returns: Dict[partner_url] → (success: bool, error_msg: str)

# 3. Activity ingestion
ingest_announce_activity(db, activity)
→ Returns: bool (success)

# 4. Vote retraction
generate_undo_activity(db, announce_activity_id, node_url, private_key)
→ Returns: Activity object with Undo type

ingest_undo_activity(db, activity)
→ Returns: bool (success)

# 5. Vote aggregation (read-heavy, critical for queries)
get_aggregated_vote_count(db, item_cid, endorsement_type)
→ Returns: Dict with local, remote, total, breakdown

get_all_vote_stats(db, item_cid)
→ Returns: Dict with upvotes, downvotes, flags, score
```

### 2. `app/routes.py`
**Status**: Mostly ready, needs 3 modifications  
**Changes**:

#### a. Modify `create_endorsement()` endpoint
```python
# After creating endorsement record, add:
asyncio.create_task(
    EndorsementPropagationService.send_announce_to_federation_partners(
        db, activity, private_key
    )
)
```

#### b. Modify `delete_user_endorsement()` endpoint
```python
# After deleting endorsement, add:
undo_activity = await EndorsementPropagationService.generate_undo_activity(...)
asyncio.create_task(
    EndorsementPropagationService.send_announce_to_federation_partners(...)
)
```

#### c. Add new endpoint `GET /api/items/{cid}/endorsements/aggregated`
```python
# Returns: AggregatedEndorsementStatsResponse
# Uses: get_aggregated_vote_count() for all endorsement types
```

#### d. Update `/inbox` POST handler
```python
# Add cases for:
# - activity_type == "Announce" → handle_announce_activity()
# - activity_type == "Undo" → handle_undo_activity()
```

### 3. `app/schemas.py`
**Status**: May need 1 addition  
**Addition**: 

```python
class AggregatedVoteCountResponse(BaseModel):
    """Aggregated vote count including local + remote."""
    local: int
    remote: int
    total: int
    breakdown: Dict[str, int]  # {partner_url: count}

class AggregatedEndorsementStatsResponse(BaseModel):
    """Comprehensive vote statistics."""
    item_cid: str
    upvote_count: AggregatedVoteCountResponse
    downvote_count: AggregatedVoteCountResponse
    flag_count: AggregatedVoteCountResponse
    score: int
```

## Implementation Order

### Phase 1: Service Layer (Day 1-2)
1. Implement `generate_announce_activity()`
   - Get item vote stats from endorsements table
   - Build Announce JSON-LD structure
   - Store Activity record with local=1
   
2. Implement `ingest_announce_activity()`
   - Validate required fields
   - Store Activity with local=0
   
3. Implement `generate_undo_activity()`
   - Fetch original Announce
   - Build Undo JSON-LD
   - Store Activity with local=1
   
4. Implement `ingest_undo_activity()`
   - Fetch original Announce
   - Store Undo with local=0
   
5. Implement `get_aggregated_vote_count()`
   - Count local endorsements
   - Count remote activities (Announce only, exclude Undo)
   - Group by source_node for breakdown
   
6. Implement `send_announce_to_federation_partners()`
   - Fetch federation_partners
   - Create HTTP Signature for each
   - POST to partner inboxes
   - Return results

**Tests**: Run `pytest tests/test_wave3_endorsement_propagation.py::TestEndorsementPropagationService -v`

### Phase 2: Route Integration (Day 2-3)
1. Update `create_endorsement()` route
   - Call `generate_announce_activity()`
   - Fire async task to send
   
2. Update `delete_user_endorsement()` route
   - Call `generate_undo_activity()`
   - Fire async task to send
   
3. Add `/api/items/{cid}/endorsements/aggregated` endpoint
   - Use `get_aggregated_vote_count()` for all types
   - Return `AggregatedEndorsementStatsResponse`
   
4. Update `/inbox` handler
   - Add Announce case: call `ingest_announce_activity()`
   - Add Undo case: call `ingest_undo_activity()`

**Tests**: Run `pytest tests/test_wave3_endorsement_propagation.py::TestEndorsementRoutes -v`

### Phase 3: Cross-Node Testing (Day 3-4)
1. Mock federation partners
2. Test Announce delivery to multiple partners
3. Test Undo vote revocation
4. Validate aggregation across nodes

**Tests**: Run `pytest tests/test_wave3_endorsement_propagation.py::TestCrossNodeEndorsementFlow -v`

## Key Implementation Details

### Announce Activity Format
```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "id": "{node_url}/activities/announce-{uuid}",
  "type": "Announce",
  "actor": "{node_url}/actor",
  "object": "{node_url}/items/{item_cid}",
  "published": "{iso_timestamp}",
  "content": {
    "item_cid": "{item_cid}",
    "vote_type": "upvote|downvote",
    "user_id": "{user_id}",
    "source_node": "{node_url}",
    "local_upvote_count": {count},
    "local_downvote_count": {count},
    "timestamp": "{iso_timestamp}"
  }
}
```

### Undo Activity Format
```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "id": "{node_url}/activities/undo-{uuid}",
  "type": "Undo",
  "actor": "{node_url}/actor",
  "object": "{original_announce_id}",
  "published": "{iso_timestamp}"
}
```

### Vote Aggregation Query Pattern
```python
# 1. Local votes (fast, indexed)
SELECT COUNT(*) FROM endorsements
WHERE item_cid = ? AND endorsement_type = ?

# 2. Remote votes (from activities, exclude undo'd)
SELECT source_node, COUNT(*) FROM activities
WHERE object_id = ? AND activity_type = "Announce"
  AND local = 0
  AND id NOT IN (SELECT object_id FROM activities WHERE type = "Undo")
GROUP BY source_node

# 3. Aggregate locally in Python
local_count + sum(remote counts)
```

## Database Queries Needed

### No schema changes required!
Use existing tables:
- `endorsements` - local votes
- `activities` - remote votes (Announce) and audit log
- `federation_partners` - list of partners for delivery

### SQL hints:
```sql
-- Count local votes by type
SELECT endorsement_type, COUNT(*) FROM endorsements
WHERE item_cid = ?
GROUP BY endorsement_type;

-- Extract vote counts from Announce activities
SELECT 
  activity_data->>'content.source_node' as source,
  COUNT(*) as vote_count
FROM activities
WHERE JSON_EXTRACT(activity_data, '$.content.item_cid') = ?
  AND activity_type = 'Announce'
  AND local = 0
GROUP BY source;
```

## Testing Strategy

### Unit Tests (5 tests)
Focus on service method logic independently.
Mock DB, no actual network calls.

### Integration Tests (4 tests)
Test route + service together.
Mock DB and federation partners.

### End-to-End Tests (4 tests)
Full Announce/Undo flow.
Mock two "nodes" with federation partners.

### Test Execution
```bash
# All Wave 3 tests
pytest tests/test_wave3_endorsement_propagation.py -v

# By class
pytest tests/test_wave3_endorsement_propagation.py::TestEndorsementPropagationService -v
pytest tests/test_wave3_endorsement_propagation.py::TestEndorsementAggregation -v
pytest tests/test_wave3_endorsement_propagation.py::TestEndorsementRoutes -v
pytest tests/test_wave3_endorsement_propagation.py::TestCrossNodeEndorsementFlow -v

# Single test
pytest tests/test_wave3_endorsement_propagation.py::TestEndorsementPropagationService::test_generate_announce_activity_structure -v
```

## Important Notes

1. **No breaking changes** - Existing Phase 1-3 APIs remain unchanged
2. **Async propagation** - Announce/Undo sent fire-and-forget (don't block local vote)
3. **No task queue yet** - Use `asyncio.create_task()` for now; upgrade to Celery in Wave 4
4. **Eventually consistent** - Vote counts may lag minutes across nodes; acceptable for MVP
5. **Signature verification** - Use existing `http_signatures.py` utilities
6. **Atomic operations** - Each activity generation + storage must be atomic

## Success Metrics

- [ ] All 17 Wave 3 tests passing
- [ ] No regressions in Wave 1-3 tests (116 tests must pass)
- [ ] Announce activities properly formatted per ActivityPub spec
- [ ] Undo activities correctly reference original Announce
- [ ] Vote counts aggregated correctly across local + remote
- [ ] HTTP signatures valid for all sent activities
- [ ] Inbox accepts and stores Announce/Undo activities
- [ ] Cross-node Announce delivery to all partners
- [ ] No breaking changes to existing API responses

## Common Pitfalls

1. **Forgetting to mark remote activities with `local=0`** - Required for aggregation query
2. **Including local Endorsement records in remote aggregation** - Only count activities
3. **Not handling missing federation partners gracefully** - Log errors but don't fail local vote
4. **Duplicate Undo processing** - Idempotency check needed
5. **Missing HTTP signature headers** - Activities won't be trusted by remote nodes

## Performance Considerations

- Vote aggregation is read-heavy; queries run at display time
- Remote vote counts cached implicitly (rarely changes between requests)
- Consider materialized view or cache in Wave 4 if aggregation queries slow
- Activity table will grow; add TTL/archival in Wave 5

## References

- **WAVE_3_PLAN.md** - Full design document
- **PHASE_4_DESIGN.md** - Phase 4 overall architecture
- **test_wave3_endorsement_propagation.py** - Test specifications
- **HTTPSignatureUtils** (http_signatures.py) - Signature generation/verification
- **ActivityPub Spec**: https://www.w3.org/TR/activitypub/
