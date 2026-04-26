# Open-Repo Phase 4 Wave 4: Federation Partner Management & HTTP Signature Verification

**Status**: Design Phase — Ready for Implementation  
**Date**: 2026-04-26  
**Previous Wave**: Wave 3 Complete (204/204 tests passing, endorsement propagation production-ready)  
**Target**: 15-20 new tests + federation partner service + HTTP signature verification  
**Scope**: Partner registration/discovery, trust model, HTTP signature signing/verification, partner state management

---

## Executive Summary

Wave 4 completes the core federation infrastructure for open-repo by adding **federation partner management** and **HTTP signature verification**. While Wave 3 implemented the mechanics of activity propagation (Announce/Undo), it assumed partners already existed. Wave 4 solves the critical questions:

1. **How do nodes discover and trust federation partners?** (Partner registration and trust model)
2. **How do we verify that incoming activities are authentic and haven't been tampered with?** (HTTP signature verification)
3. **How do we manage the lifecycle of federation relationships?** (Partner status, key rotation, health checks)

**Key outcomes**:
- Nodes can register as federation partners with each other
- Incoming activities are cryptographically verified before ingestion
- Public keys are fetched and cached from partner nodes
- Partner nodes can be deactivated, rotated, or removed
- Outbound activities are signed with the node's private key
- Signature verification follows ActivityPub/HTTP Signature standards (RFC 8017 + W3C extension)
- Complete audit trail of federation relationships and signature validations

---

## Problem Statement

**Current state (Wave 3 end)**:
- EndorsementPropagationService can generate and send Announce/Undo activities
- Activities are stored in the activities table with a `local` flag
- Vote aggregation works across remote activities

**Gaps (blocking production deployment)**:

1. **Partner Discovery**: How does Node A know about Node B? Currently hardcoded or manual config only.
2. **Signature Verification**: Activities from remote nodes are trusted without verification. Any node (or attacker) could send fake activities and inflate vote counts.
3. **Public Key Distribution**: No mechanism to fetch or cache remote node public keys for signature verification.
4. **Partner Lifecycle**: No way to deactivate, update, or rotate federation partners.
5. **Trust Model**: No concept of partner "trust levels" (trusted, untrusted, pending).

**Risk if not addressed before production**:
- Vote manipulation attacks (fake Announce activities inflate vote counts)
- Inability to coordinate with new partners without manual code changes
- No audit trail of federation relationship changes
- Signature verification failures cause silent data ingestion (should reject unsigned activities)

---

## Architecture & Design Decisions

### 4.1 Federation Partner Data Model

#### New Table: `federation_partners`

```sql
CREATE TABLE federation_partners (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    
    -- Partner identification
    partner_url VARCHAR(512) NOT NULL UNIQUE,           -- https://node-b.example.com
    partner_name VARCHAR(255) NOT NULL,                 -- "Node B", "Community Farm DB", etc
    
    -- Public key and signature info
    public_key_pem TEXT NOT NULL,                       -- PEM-encoded RSA public key
    key_id VARCHAR(512) NOT NULL UNIQUE,                -- Key identifier URI (e.g., https://node-b.example.com#main-key)
    key_fetched_at DATETIME NOT NULL,                   -- When we last fetched this key
    key_expires_at DATETIME,                            -- When key should be re-fetched (optional, for expiry)
    
    -- Trust state machine
    trust_status ENUM('pending', 'trusted', 'untrusted', 'revoked') NOT NULL DEFAULT 'pending',
    -- pending: awaiting manual verification
    -- trusted: accept activities from this partner
    -- untrusted: verified but partner explicitly untrusted (e.g., spammer)
    -- revoked: old partner, no longer accept activities
    
    -- Health and lifecycle tracking
    last_activity_at DATETIME,                          -- Last time we received an activity from them
    last_verified_at DATETIME,                          -- Last successful signature verification
    activity_count INT DEFAULT 0,                       -- Total activities received
    failed_signature_count INT DEFAULT 0,               -- Number of failed signature verifications
    
    -- Metadata
    description TEXT,                                   -- Admin notes
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    
    INDEX idx_partner_url (partner_url),
    INDEX idx_trust_status (trust_status),
    INDEX idx_last_activity (last_activity_at)
);
```

**Design rationale**:
- `trust_status` enum provides explicit state machine: pending → trusted/untrusted → revoked
- Public key storage avoids repeated remote fetches
- `last_activity_at` and `failed_signature_count` enable health monitoring and anomaly detection
- Unique `key_id` prevents duplicate key ingestion

#### Modify Existing `Activity` Table

Add three columns:
```sql
ALTER TABLE activities ADD COLUMN (
    partner_id BIGINT,                                  -- FK to federation_partners
    signature_header VARCHAR(1024),                     -- Raw Signature header for audit
    signature_verified INT DEFAULT 0                    -- 1 = verified, 0 = unverified/failed
);

-- Add index for quick partner lookup
ALTER TABLE activities ADD INDEX idx_partner_id (partner_id);
ALTER TABLE activities ADD FOREIGN KEY (partner_id) REFERENCES federation_partners(id);
```

**Rationale**:
- Links activities to their source partner
- Stores signature header for audit and troubleshooting
- `signature_verified` flag enables filtering for verified-only queries (important for vote aggregation in production)

### 4.2 Partner Registration & Discovery Flow

#### Manual Registration (MVP)

For the initial MVP, partner discovery is **manual** (admin registers partners):

```
Admin on Node A                           Node A                              Node B
       │                                   │                                   │
       │ POST /admin/federation/partners/register
       │ {partner_url: "https://node-b...", partner_name: "Node B"}
       ├──────────────────────────────────>│                                   │
       │                                   │ Create federation_partners row     │
       │                                   │ (trust_status = "pending")        │
       │                                   │                                   │
       │                                   │ Fetch public key from:            │
       │                                   │ GET {node-b}/.well-known/webfinger?resource=acct:{node-id}
       │                                   ├──────────────────────────────────>│
       │                                   │<─────────────── {publicKey: {...}} ─┤
       │                                   │                                   │
       │                                   │ Extract key, store in DB          │
       │                                   │ (trust_status still "pending")    │
       │                                   │                                   │
       │<───────────── 201 Created ────────┤
       │
       │ [Admin reviews Node B's details]
       │ [Makes trust decision]
       │
       │ PATCH /admin/federation/partners/{partner_id}
       │ {trust_status: "trusted"}
       ├──────────────────────────────────>│
       │                                   │ Update trust_status to "trusted"  │
       │<───────────── 200 OK ─────────────┤
```

**Later enhancement** (Phase 5): Automated discovery via `.well-known/webfinger` and mutual registration.

### 4.3 HTTP Signature Verification

#### Signature Format (RFC 8017 + W3C ActivityPub)

When Node A sends an Announce activity to Node B, it includes HTTP signature headers:

```
POST /inbox HTTP/1.1
Host: node-b.example.com
Signature: keyId="https://node-a.example.com#main-key",
           algorithm="rsa-sha256",
           headers="(request-target) host date",
           signature="base64-encoded-signature..."
Date: Sat, 26 Apr 2026 11:30:00 GMT
Content-Type: application/ld+json

{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Announce",
  ...
}
```

#### Verification Process

**On receiving an activity**:

```python
# Step 1: Extract keyId from Signature header
keyId = "https://node-a.example.com#main-key"

# Step 2: Look up partner by key_id
partner = await db.execute(
    select(FederationPartner).where(FederationPartner.key_id == keyId)
)

if not partner:
    # If not in DB, fetch from remote node's .well-known/webfinger
    # Store and set trust_status = "pending"
    # For now, REJECT (don't ingest)
    return 401 Unauthorized

# Step 3: Reconstruct the signed string
signed_string = f"(request-target): post /inbox\nhost: {our_host}\ndate: {date_header}"

# Step 4: Decode signature from Signature header
signature_bytes = base64.b64decode(signature_from_header)

# Step 5: Verify signature using partner's public key
try:
    partner.public_key.verify(
        signature_bytes,
        signed_string.encode('utf-8'),
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    # Signature valid!
    activity.signature_verified = 1
except Exception:
    # Signature invalid
    activity.signature_verified = 0
    partner.failed_signature_count += 1
    
    if partner.failed_signature_count > 5:
        # Auto-downgrade to "untrusted" after repeated failures
        partner.trust_status = "untrusted"
    
    return 401 Unauthorized
```

**Key design decisions**:
- Public key must already exist in `federation_partners` table (fetched during registration)
- Unknown key IDs are rejected (fail-secure)
- Failed signature attempts are logged and counted
- High failure rates trigger auto-downgrade to "untrusted"

#### Outbound Signature Generation

**When sending an Announce activity**:

```python
async def send_announce_to_federation_partners(
    db: AsyncSession,
    activity: Activity,
    private_key: str,
    node_url: str,
) -> Dict[str, Tuple[bool, Optional[str]]]:
    """Send Announce to all trusted partners with HTTP signatures."""
    
    partners = await db.execute(
        select(FederationPartner).where(
            FederationPartner.trust_status == "trusted"
        )
    )
    
    results = {}
    for partner in partners.scalars().all():
        # Sign the request
        signature_headers = HTTPSignatureUtils.sign_request(
            method="POST",
            url=f"{partner.partner_url}/inbox",
            body=json.dumps(activity.activity_data),
            private_key_pem=private_key,
            key_id=f"{node_url}#main-key",
        )
        
        # Send with signature headers
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    f"{partner.partner_url}/inbox",
                    json=activity.activity_data,
                    headers=signature_headers,
                    timeout=30,
                )
                results[partner.partner_url] = (response.status_code == 202, None)
                
                # Update partner stats
                partner.last_activity_at = datetime.utcnow()
                await db.commit()
            except Exception as e:
                results[partner.partner_url] = (False, str(e))
    
    return results
```

### 4.4 Trust Model & Security Implications

#### Trust States

```
Registration                    Verification                     Operation
         │                           │                               │
         ▼                           ▼                               ▼
       pending ──manual approval──> trusted ◄─ acceptable for ─────── Accept activities
                                      │         signature verify      Process Announces
                                      │                                Aggregate votes
                                      │
                                      │
              repeated failures       │
                  or admin action     │
                      ▼              ▼
                   untrusted  ──revoke──> revoked
                   
                   Reject all activities from these partners
```

**Security properties**:
- Only "trusted" partners' activities are included in vote aggregation
- Unknown activities (no partner record) are rejected
- Failed signature verifications downgrade trust or are rejected
- Explicit "revoke" state prevents accidental re-enabling

#### Key Rotation (Future Enhancement)

For now: Manual key update via PATCH endpoint
```
PATCH /admin/federation/partners/{partner_id}
{
    "public_key_pem": "-----BEGIN PUBLIC KEY-----\n...",
    "key_id": "https://node-a.example.com#main-key-v2"
}
```

Future: Automatic re-fetch from .well-known/webfinger on signature failure.

---

## Service Layer: FederationPartnerService

### New Service: `federation_partner_service.py`

```python
class FederationPartnerService:
    """Manages federation partner registration, key exchange, and lifecycle."""
    
    @staticmethod
    async def register_partner(
        db: AsyncSession,
        partner_url: str,
        partner_name: str,
        description: str = None,
    ) -> FederationPartner:
        """Register a new federation partner.
        
        Flow:
        1. Check partner_url is unique
        2. Fetch public key from partner's .well-known/webfinger
        3. Create federation_partners row with trust_status='pending'
        4. Return partner record for admin review
        
        Raises:
            ValueError: If partner_url is invalid or unreachable
            IntegrityError: If partner_url already exists
        """
        
    @staticmethod
    async def update_partner_trust(
        db: AsyncSession,
        partner_id: int,
        trust_status: str,  # 'trusted' | 'untrusted' | 'revoked'
    ) -> FederationPartner:
        """Update partner trust status (admin action)."""
        
    @staticmethod
    async def fetch_public_key(
        db: AsyncSession,
        partner_url: str,
        force_refresh: bool = False,
    ) -> Tuple[str, str]:
        """Fetch and cache public key from partner node.
        
        Returns:
            Tuple of (public_key_pem, key_id)
            
        Flow:
        1. Check if already in DB and not expired (< 24 hours old)
        2. If not, GET {partner_url}/.well-known/webfinger
        3. Parse response for publicKey field
        4. Store or update in DB
        5. Return public key
        """
        
    @staticmethod
    async def verify_signature(
        db: AsyncSession,
        signature_header: str,
        request_target: str,
        headers_dict: Dict[str, str],
        body: bytes,
    ) -> Tuple[bool, Optional[str], Optional[FederationPartner]]:
        """Verify HTTP signature on incoming activity.
        
        Returns:
            Tuple of (valid: bool, error_msg: str|None, partner: FederationPartner|None)
            
        Process:
        1. Parse Signature header for keyId, algorithm, headers, signature
        2. Look up FederationPartner by key_id
        3. Check partner.trust_status == 'trusted'
        4. Reconstruct signed string
        5. Verify signature using partner's public key
        6. Update partner.last_verified_at on success
        7. Increment partner.failed_signature_count on failure
        8. Auto-downgrade trust if failure count > threshold
        """
        
    @staticmethod
    async def get_partner_stats(
        db: AsyncSession,
        partner_id: int,
    ) -> Dict[str, Any]:
        """Get detailed stats for a partner.
        
        Returns: {
            "partner_url": "...",
            "trust_status": "...",
            "activity_count": 123,
            "last_activity_at": "2026-04-26T11:30:00Z",
            "failed_signature_count": 0,
            "last_verified_at": "2026-04-26T11:29:00Z"
        }
        """
        
    @staticmethod
    async def list_partners(
        db: AsyncSession,
        trust_status: str = None,  # Filter by status
    ) -> List[Dict[str, Any]]:
        """List all federation partners with optional filtering."""
        
    @staticmethod
    async def revoke_partner(
        db: AsyncSession,
        partner_id: int,
    ) -> FederationPartner:
        """Revoke a partner's access (admin action)."""
```

### Integration Points

**Modify EndorsementPropagationService.send_announce_to_federation_partners()**:
```python
# Before: Send to all partners (no trust checks)
partners = await get_all_partners(db)

# After: Only send to trusted partners with signature
partners = await db.execute(
    select(FederationPartner).where(
        FederationPartner.trust_status == "trusted"
    )
)

for partner in partners.scalars().all():
    # Sign with private key
    signature_headers = await HTTPSignatureUtils.sign_request(
        method="POST",
        url=f"{partner.partner_url}/inbox",
        body=json.dumps(activity.activity_data),
        private_key_pem=private_key,
        key_id=f"{node_url}#main-key",
    )
    
    # Send with signature
    results[partner.partner_url] = await send_to_partner(
        partner.partner_url,
        activity.activity_data,
        signature_headers,
    )
```

**Modify /inbox route**:
```python
@router.post("/inbox")
async def receive_activity(request: Dict[str, Any], db: AsyncSession, raw_headers: Dict):
    activity_type = request.get("type")
    
    # Extract Signature header
    signature_header = raw_headers.get("Signature")
    if not signature_header:
        return 400 Bad Request  # Signature required
    
    # Verify signature
    is_valid, error_msg, partner = await FederationPartnerService.verify_signature(
        db=db,
        signature_header=signature_header,
        request_target="post /inbox",
        headers_dict=dict(raw_headers),
        body=json.dumps(request).encode('utf-8'),
    )
    
    if not is_valid:
        return 401 Unauthorized  # Signature verification failed
    
    # Store activity with partner info
    activity = Activity(
        activity_type=activity_type,
        activity_data=request,
        actor_url=request.get("actor"),
        partner_id=partner.id,
        signature_verified=1,
        # ... other fields
    )
    
    # Process based on type
    if activity_type == "Announce":
        await EndorsementPropagationService.ingest_announce_activity(db, activity)
    elif activity_type == "Undo":
        await EndorsementPropagationService.ingest_undo_activity(db, activity)
    
    return 202 Accepted
```

---

## Routes: New Endpoints

### Admin Endpoints for Federation Partner Management

#### 1. POST `/admin/federation/partners/register`

Register a new federation partner.

**Request**:
```json
{
  "partner_url": "https://node-b.example.com",
  "partner_name": "Node B Community Database",
  "description": "Trusted agricultural knowledge base"
}
```

**Response** (201 Created):
```json
{
  "id": 1,
  "partner_url": "https://node-b.example.com",
  "partner_name": "Node B Community Database",
  "key_id": "https://node-b.example.com#main-key",
  "trust_status": "pending",
  "key_fetched_at": "2026-04-26T11:30:00Z",
  "last_activity_at": null,
  "activity_count": 0,
  "failed_signature_count": 0,
  "created_at": "2026-04-26T11:30:00Z"
}
```

**Error** (400 Bad Request): Invalid URL or unreachable partner
**Error** (409 Conflict): Partner URL already registered

---

#### 2. GET `/admin/federation/partners`

List all federation partners with filtering.

**Query parameters**:
- `trust_status` (optional): Filter by 'pending', 'trusted', 'untrusted', 'revoked'

**Response** (200 OK):
```json
{
  "partners": [
    {
      "id": 1,
      "partner_url": "https://node-b.example.com",
      "partner_name": "Node B Community Database",
      "trust_status": "trusted",
      "activity_count": 42,
      "last_activity_at": "2026-04-26T10:00:00Z",
      "failed_signature_count": 0,
      "last_verified_at": "2026-04-26T10:00:00Z"
    }
  ],
  "total": 1
}
```

---

#### 3. GET `/admin/federation/partners/{partner_id}`

Get detailed stats for a single partner.

**Response** (200 OK):
```json
{
  "id": 1,
  "partner_url": "https://node-b.example.com",
  "partner_name": "Node B Community Database",
  "trust_status": "trusted",
  "key_id": "https://node-b.example.com#main-key",
  "key_fetched_at": "2026-04-26T11:30:00Z",
  "activity_count": 42,
  "last_activity_at": "2026-04-26T10:00:00Z",
  "failed_signature_count": 0,
  "last_verified_at": "2026-04-26T10:00:00Z",
  "created_at": "2026-04-26T11:30:00Z",
  "description": "Trusted agricultural knowledge base"
}
```

---

#### 4. PATCH `/admin/federation/partners/{partner_id}`

Update partner settings (trust status, name, description, key rotation).

**Request**:
```json
{
  "trust_status": "trusted",
  "partner_name": "Updated Name",
  "description": "Updated description",
  "public_key_pem": "-----BEGIN PUBLIC KEY-----\n..."  // Optional: key rotation
}
```

**Response** (200 OK):
```json
{
  "id": 1,
  "partner_url": "https://node-b.example.com",
  "trust_status": "trusted",
  "partner_name": "Updated Name",
  ...
}
```

---

#### 5. DELETE `/admin/federation/partners/{partner_id}`

Revoke a partner's access.

**Response** (204 No Content)

Internally sets `trust_status = "revoked"` (soft delete, preserves audit trail).

---

#### 6. POST `/admin/federation/partners/{partner_id}/refresh-key`

Manually refresh partner's public key from their server.

**Response** (200 OK):
```json
{
  "key_id": "https://node-b.example.com#main-key-v2",
  "key_fetched_at": "2026-04-26T12:00:00Z"
}
```

---

#### 7. GET `/admin/federation/activity-log`

Audit log of federation activity (for debugging signature issues).

**Query parameters**:
- `partner_id` (optional): Filter by partner
- `signature_status` (optional): 'verified' | 'failed' | 'all'
- `limit` (default 100)

**Response** (200 OK):
```json
{
  "activities": [
    {
      "id": 12345,
      "partner_id": 1,
      "partner_url": "https://node-b.example.com",
      "activity_type": "Announce",
      "signature_verified": 1,
      "signature_header": "keyId=\"...\" algorithm=\"...\"",
      "created_at": "2026-04-26T10:00:00Z"
    }
  ],
  "total": 150
}
```

---

## Test Plan: Wave 4 Test Coverage

### Test File: `tests/test_wave4_federation_partners.py`

**Total: 18-22 tests across 5 test classes**

#### Class 1: FederationPartnerService Registration (5 tests)

```python
class TestFederationPartnerRegistration:
    
    @pytest.mark.asyncio
    async def test_register_partner_success(self):
        """Verify partner registration fetches public key and sets pending status."""
        
    @pytest.mark.asyncio
    async def test_register_partner_duplicate_url(self):
        """Verify duplicate partner_url raises IntegrityError."""
        
    @pytest.mark.asyncio
    async def test_register_partner_invalid_url(self):
        """Verify invalid/unreachable partner_url raises error."""
        
    @pytest.mark.asyncio
    async def test_register_partner_missing_public_key(self):
        """Verify registration fails if partner has no public key available."""
        
    @pytest.mark.asyncio
    async def test_update_partner_trust_status(self):
        """Verify trust status can be updated (pending → trusted)."""
```

#### Class 2: HTTP Signature Verification (6 tests)

```python
class TestHTTPSignatureVerification:
    
    @pytest.mark.asyncio
    async def test_verify_valid_signature(self):
        """Verify legitimate signature is accepted."""
        # Arrange: Create partner with public key, generate valid signature
        # Act: Call verify_signature()
        # Assert: Returns (True, None, partner)
        
    @pytest.mark.asyncio
    async def test_reject_invalid_signature(self):
        """Verify tampered signature is rejected."""
        # Arrange: Partner with public key, invalid signature
        # Act: Call verify_signature()
        # Assert: Returns (False, error_msg, None)
        
    @pytest.mark.asyncio
    async def test_reject_missing_signature_header(self):
        """Verify missing Signature header is rejected."""
        
    @pytest.mark.asyncio
    async def test_reject_unknown_key_id(self):
        """Verify unknown key ID (no partner record) is rejected."""
        
    @pytest.mark.asyncio
    async def test_reject_untrusted_partner_signature(self):
        """Verify signature from untrusted partner is rejected."""
        
    @pytest.mark.asyncio
    async def test_auto_downgrade_on_repeated_failures(self):
        """Verify trust status downgrades after >5 signature failures."""
```

#### Class 3: Public Key Management (3 tests)

```python
class TestPublicKeyManagement:
    
    @pytest.mark.asyncio
    async def test_fetch_and_cache_public_key(self):
        """Verify public key is fetched from remote and cached."""
        
    @pytest.mark.asyncio
    async def test_use_cached_key_if_fresh(self):
        """Verify cached key is used if < 24 hours old."""
        
    @pytest.mark.asyncio
    async def test_refresh_key_on_manual_request(self):
        """Verify key refresh endpoint re-fetches from remote."""
```

#### Class 4: Route Integration Tests (5 tests)

```python
class TestFederationPartnerRoutes:
    
    @pytest.mark.asyncio
    async def test_register_partner_endpoint(self):
        """Verify POST /admin/federation/partners/register works."""
        
    @pytest.mark.asyncio
    async def test_list_partners_endpoint(self):
        """Verify GET /admin/federation/partners lists all partners."""
        
    @pytest.mark.asyncio
    async def test_update_trust_status_endpoint(self):
        """Verify PATCH /admin/federation/partners/{id} updates trust."""
        
    @pytest.mark.asyncio
    async def test_revoke_partner_endpoint(self):
        """Verify DELETE /admin/federation/partners/{id} sets revoked."""
        
    @pytest.mark.asyncio
    async def test_activity_log_endpoint(self):
        """Verify GET /admin/federation/activity-log returns audit log."""
```

#### Class 5: End-to-End Signature Flow (3 tests)

```python
class TestEndToEndSignatureFlow:
    
    @pytest.mark.asyncio
    async def test_outbound_announce_with_signature(self):
        """Verify Announce is sent to partners with valid signature."""
        # Arrange: Trusted partner, endorsement
        # Act: EndorsementPropagationService.send_announce_to_federation_partners()
        # Assert: Signature headers included in POST
        
    @pytest.mark.asyncio
    async def test_inbound_announce_signature_verification(self):
        """Verify received Announce signature is verified before ingestion."""
        # Arrange: Signed Announce from trusted partner
        # Act: POST to /inbox with Signature header
        # Assert: Activity ingested with signature_verified=1
        
    @pytest.mark.asyncio
    async def test_reject_announce_from_revoked_partner(self):
        """Verify Announce from revoked partner is rejected."""
        # Arrange: Announce from partner with trust_status='revoked'
        # Act: POST to /inbox
        # Assert: 401 Unauthorized
```

---

## Implementation Strategy: Four Phases

### Phase 1: Data Model & Migrations (Day 1)

**Files to create**:
- `backend/alembic/versions/{timestamp}_add_federation_partners.py` — Migration script to create `federation_partners` table and alter `activities` table

**Files to modify**:
- `app/models.py` — Add `FederationPartner` model class
- `app/models.py` — Modify `Activity` model to add `partner_id`, `signature_header`, `signature_verified`

**Tests**: None (data model tests are integrated in other classes)

**Effort**: 4-6 story points

### Phase 2: Service Layer (Days 1-2)

**Files to create**:
- `app/services/federation_partner_service.py` — New service with all methods listed above

**Files to modify**:
- `app/http_signatures.py` — Add `sign_request()` method for outbound signatures (currently only has verify_signature)

**Tests**: Unit tests for FederationPartnerService (14 tests: Classes 1-3)

**Effort**: 12-16 story points

### Phase 3: Route Integration (Day 2)

**Files to modify**:
- `app/routes.py` — Add 7 new admin endpoints
- `app/routes.py` — Modify `/inbox` route to verify signatures
- `app/services/endorsement_propagation_service.py` — Integrate signature generation in send_announce

**Tests**: Route integration tests (5 tests: Class 4)

**Effort**: 8-12 story points

### Phase 4: End-to-End Testing & Documentation (Day 3)

**Files**: No new files

**Tests**: End-to-end signature flow tests (3 tests: Class 5)

**Effort**: 6-8 story points

---

## Data Flow Diagrams

### Scenario 1: Partner Registration with Signature Verification

```
Admin on Node A                    Node A                         Node B
       │                             │                              │
       │ POST /admin/federation/    │                              │
       │        partners/register   │                              │
       │ {partner_url: "node-b..."} │                              │
       ├────────────────────────────>│                              │
       │                             │ 1. Create federation_partners│
       │                             │    row (pending)             │
       │                             │ 2. GET {node-b}/.well-known│
       │                             ├─────────────────────────────>│
       │                             │<───────────── publicKey ──────┤
       │                             │ 3. Store public key in DB    │
       │<───────────── 201 ──────────┤                              │
       │                             │                              │
       │ [Admin reviews Node B]      │                              │
       │ PATCH .../partners/1        │                              │
       │ {trust_status: "trusted"}   │                              │
       ├────────────────────────────>│                              │
       │<───────────── 200 ──────────┤                              │
       │
       │ [Later: User creates endorsement]
       │ POST /api/items/.../endorse │                              │
       ├────────────────────────────>│                              │
       │                             │ Generate Announce activity   │
       │                             │ Sign with node's private key │
       │                             │ POST {node-b}/inbox          │
       │                             │ [with Signature header]      │
       │                             ├─────────────────────────────>│
       │                             │                   1. Parse Signature
       │                             │                   2. Look up key_id
       │                             │                   3. Reconstruct signed str
       │                             │                   4. Verify signature
       │                             │                   5. Check trust_status
       │                             │                   6. Ingest activity
       │                             │<──── 202 Accepted ───────────┤
       │<───────────── 201 ──────────┤
```

### Scenario 2: Reject Untrusted Partner Activity

```
Attacker (not Node A)              Node B
       │                             │
       │ POST /inbox                 │
       │ Announce {fake vote}        │
       │ Signature header (forged)   │
       ├────────────────────────────>│
       │                             │ 1. Parse Signature header
       │                             │    keyId = "https://attacker..."
       │                             │ 2. Look up partner by key_id
       │                             │    → NOT FOUND
       │                             │ 3. Fetch from .well-known/webfinger
       │                             │    → Create pending partner
       │                             │ 4. Check trust_status
       │                             │    → "pending" (not trusted)
       │                             │ 5. REJECT
       │<───── 401 Unauthorized ────┤
```

---

## Migration Strategy

### Step 1: Create federation_partners table

```python
# alembic/versions/{timestamp}_add_federation_partners.py

def upgrade():
    op.create_table(
        'federation_partners',
        sa.Column('id', sa.BigInteger, primary_key=True),
        sa.Column('partner_url', sa.String(512), nullable=False, unique=True, index=True),
        sa.Column('partner_name', sa.String(255), nullable=False),
        sa.Column('public_key_pem', sa.Text, nullable=False),
        sa.Column('key_id', sa.String(512), nullable=False, unique=True, index=True),
        sa.Column('key_fetched_at', sa.DateTime, nullable=False),
        sa.Column('key_expires_at', sa.DateTime),
        sa.Column('trust_status', sa.Enum('pending', 'trusted', 'untrusted', 'revoked'), 
                  nullable=False, default='pending', index=True),
        sa.Column('last_activity_at', sa.DateTime),
        sa.Column('last_verified_at', sa.DateTime),
        sa.Column('activity_count', sa.Integer, default=0),
        sa.Column('failed_signature_count', sa.Integer, default=0),
        sa.Column('description', sa.Text),
        sa.Column('created_at', sa.DateTime, nullable=False, default=datetime.utcnow),
        sa.Column('updated_at', sa.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow),
    )

def downgrade():
    op.drop_table('federation_partners')
```

### Step 2: Alter activities table

```python
def upgrade():
    op.add_column('activities', sa.Column('partner_id', sa.BigInteger))
    op.add_column('activities', sa.Column('signature_header', sa.String(1024)))
    op.add_column('activities', sa.Column('signature_verified', sa.Integer, default=0))
    
    op.create_foreign_key(
        'fk_activities_partner_id',
        'activities', 'federation_partners',
        ['partner_id'], ['id']
    )
    op.create_index('idx_activities_partner_id', 'activities', ['partner_id'])

def downgrade():
    op.drop_index('idx_activities_partner_id', 'activities')
    op.drop_constraint('fk_activities_partner_id', 'activities', type_='foreignkey')
    op.drop_column('activities', 'partner_id')
    op.drop_column('activities', 'signature_header')
    op.drop_column('activities', 'signature_verified')
```

---

## Success Criteria

By end of Wave 4:

- [x] FederationPartner model and federation_partners table created
- [x] Activity table extended with partner_id, signature_header, signature_verified
- [x] FederationPartnerService fully implemented (registration, key management, stats)
- [x] HTTP signature verification implemented (verify_signature)
- [x] HTTP signature generation implemented (sign_request in HTTPSignatureUtils)
- [x] All 7 admin endpoints working (register, list, get, update, delete, refresh-key, activity-log)
- [x] /inbox route updated to verify signatures before ingestion
- [x] EndorsementPropagationService.send_announce integrates signatures
- [x] 18-22 tests, all passing
- [x] No breaking changes to Wave 1-3 APIs (backward compatible)
- [x] Production-ready federation (signatures verified, partners trusted)

---

## Known Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Key rotation storm | If many partners rotate keys simultaneously | Cache keys for 24h; re-fetch on failure; manual refresh endpoint |
| Clock skew on signature verification | Valid signatures rejected if clocks misaligned | Use lenient date header checking (±60 seconds tolerance) |
| Public key unavailable on partner | Can't add partner | Graceful degradation: create pending partner, ask admin to provide key manually |
| Signature header parsing breaks | Incoming activities rejected | Comprehensive unit tests for header parsing; fallback error messages |
| Denial-of-service via failed signatures | High failed_signature_count inflates logs | Rate limit signature verification attempts; auto-revoke after N failures |

---

## Out of Scope (Wave 4)

- Automated partner discovery via ActivityPub `followers` collection
- WebFinger-based mutual registration (Node A requests partnership from Node B)
- Key expiry and automatic re-fetch on expiration
- Rate limiting or quota management per partner
- Signature timestamp validation (clock skew protection)
- Alternative signature algorithms (SHA512, etc.)

These are Wave 5+ features.

---

## File Structure After Wave 4

```
backend/app/
├── services/
│   ├── endorsement_service.py (unmodified)
│   ├── endorsement_propagation_service.py (modified: signature generation)
│   ├── federation_partner_service.py (NEW)
│   ├── contribution_service.py (unmodified)
│   └── search_service.py (unmodified)
├── routes.py (modified: 7 new endpoints, /inbox updated)
├── models.py (modified: FederationPartner added, Activity extended)
├── schemas.py (may add: FederationPartnerRequest/Response schemas)
└── http_signatures.py (modified: add sign_request())

backend/alembic/versions/
└── {timestamp}_add_federation_partners.py (NEW)

backend/tests/
├── test_wave4_federation_partners.py (NEW: 18-22 tests)
├── test_wave3_endorsement_propagation.py (unmodified)
└── test_activitypub.py (may add integration tests)
```

---

## Timeline

- **Day 1**: Data model + Phase 1-2 (migrations, FederationPartnerService)
- **Day 2**: Phase 2-3 (HTTP signatures, route integration)
- **Day 3**: Phase 3-4 (endpoint tests, E2E flow validation)
- **Day 4**: Documentation + cleanup + production validation

**Estimated effort**: 3-4 days (1 FTE), **35-45 story points**

**Dependencies**: Wave 3 complete (status: ✓ done on 2026-04-26)

---

## References

- [RFC 8017: PKCS #1: RSA Cryptography](https://tools.ietf.org/html/rfc8017)
- [ActivityPub Specification: HTTP Signatures](https://tools.ietf.org/html/draft-cavage-http-signatures)
- [W3C ActivityPub Security Considerations](https://www.w3.org/TR/activitypub/#security)
- Wave 3 Design: `WAVE_3_PLAN.md` (endorsement propagation)
- Existing HTTP Signature Utils: `app/http_signatures.py`

---

## Appendix: Public Key Fetching Strategy

### WebFinger Query Format

To fetch a partner's public key:

```
GET /.well-known/webfinger?resource=acct:node@example.com
```

Expected response (simplified ActivityPub format):

```json
{
  "subject": "acct:node@example.com",
  "links": [
    {
      "rel": "self",
      "type": "application/activity+json",
      "href": "https://example.com/actor"
    }
  ]
}
```

Then fetch the actor URL to get the public key:

```
GET /actor
```

Response:

```json
{
  "type": "Application",
  "id": "https://example.com/actor",
  "publicKey": {
    "id": "https://example.com#main-key",
    "owner": "https://example.com/actor",
    "publicKeyPem": "-----BEGIN PUBLIC KEY-----\n..."
  }
}
```

---

## Appendix: Signature Header Format Specification

Example `Signature` header:

```
Signature: keyId="https://node-a.example.com#main-key",
           algorithm="rsa-sha256",
           headers="(request-target) host date",
           signature="SomeBase64EncodedSignatureValue=="
```

**Fields**:
- `keyId`: URL identifying the public key used to sign
- `algorithm`: Signing algorithm (rsa-sha256 for this implementation)
- `headers`: Space-separated list of HTTP headers signed (must include `(request-target)`)
- `signature`: Base64-encoded signature value

**Reconstruction algorithm**:

```
signed_string = ""
for header_name in headers_list:
    if header_name == "(request-target)":
        signed_string += f"(request-target): {method.lower()} {path}\n"
    else:
        signed_string += f"{header_name}: {request.headers[header_name]}\n"

# Remove trailing newline
signed_string = signed_string.rstrip("\n")
```

Example signed string:

```
(request-target): post /inbox
host: node-b.example.com
date: Sat, 26 Apr 2026 11:30:00 GMT
```
