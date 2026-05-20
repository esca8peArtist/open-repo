"""Admin routes for federation partner management.

Phase 4 Wave 4 — Seven endpoints for registering, listing, inspecting,
updating, key-rotating, auditing, and deleting federation partners.

All routes are prefixed /api/v1/admin/federation-partners.
"""

import logging
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.schemas import (
    ActivityLogResponse,
    ActivityLogEntryResponse,
    FederationPartnerDetailResponse,
    FederationPartnerListResponse,
    FederationPartnerRegisterRequest,
    FederationPartnerResponse,
    KeyRotationRequest,
    TrustStateUpdateRequest,
)
from app.services.federation_partner_service import FederationPartnerService

logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/api/v1/admin/federation-partners",
    tags=["admin", "federation"],
)


@router.post(
    "/register",
    response_model=FederationPartnerResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new federation partner",
)
async def register_partner(
    request: FederationPartnerRegisterRequest,
    db: AsyncSession = Depends(get_db),
) -> FederationPartnerResponse:
    """Register a new federation partner node.

    Creates a partner record with trust_state=pending. An admin must
    subsequently approve the partner via the trust-state endpoint before
    activities from that partner are accepted.

    Raises 409 Conflict if name, base_url, or key_id is already registered.
    Raises 400 Bad Request if the public_key_pem is not a valid RSA public key.
    """
    try:
        partner = await FederationPartnerService.register_partner(
            db=db,
            name=request.name,
            base_url=request.base_url,
            public_key_pem=request.public_key_pem,
            key_id=request.key_id,
        )
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A partner with this name, base_url, or key_id already exists.",
        )

    return FederationPartnerResponse.model_validate(partner)


@router.get(
    "",
    response_model=FederationPartnerListResponse,
    summary="List all federation partners",
)
async def list_partners(
    trust_state: Optional[str] = Query(
        None,
        description="Optional filter by trust state: pending, trusted, untrusted, revoked",
    ),
    db: AsyncSession = Depends(get_db),
) -> FederationPartnerListResponse:
    """List all registered federation partners with an optional trust-state filter."""
    try:
        partners = await FederationPartnerService.list_partners(
            db=db,
            filter_by_state=trust_state,
        )
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))

    return FederationPartnerListResponse(
        partners=[FederationPartnerResponse.model_validate(p) for p in partners],
        total=len(partners),
    )


@router.get(
    "/{partner_id}",
    response_model=FederationPartnerDetailResponse,
    summary="Get federation partner detail",
)
async def get_partner(
    partner_id: int,
    db: AsyncSession = Depends(get_db),
) -> FederationPartnerDetailResponse:
    """Get detailed information for a single federation partner.

    Includes trust state, key info, and signature failure statistics.
    Returns 404 if the partner does not exist.
    """
    try:
        partner = await FederationPartnerService.get_partner(db=db, partner_id=partner_id)
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Federation partner {partner_id} not found.",
        )

    return FederationPartnerDetailResponse.model_validate(partner)


@router.put(
    "/{partner_id}/trust-state",
    response_model=FederationPartnerResponse,
    summary="Update partner trust state",
)
async def update_trust_state(
    partner_id: int,
    request: TrustStateUpdateRequest,
    db: AsyncSession = Depends(get_db),
) -> FederationPartnerResponse:
    """Update the trust state of a federation partner.

    Valid transitions:
    - pending → trusted | untrusted | revoked
    - trusted → untrusted | revoked
    - untrusted → trusted | revoked
    - revoked → (terminal, no transitions allowed)

    Returns 400 Bad Request if the transition is invalid.
    Returns 404 if the partner does not exist.
    """
    try:
        partner = await FederationPartnerService.update_partner_trust_state(
            db=db,
            partner_id=partner_id,
            new_state=request.trust_state,
        )
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Federation partner {partner_id} not found.",
        )
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))

    return FederationPartnerResponse.model_validate(partner)


@router.post(
    "/{partner_id}/rotate-key",
    response_model=FederationPartnerDetailResponse,
    summary="Rotate partner public key",
)
async def rotate_key(
    partner_id: int,
    request: KeyRotationRequest,
    db: AsyncSession = Depends(get_db),
) -> FederationPartnerDetailResponse:
    """Rotate the public key stored for a federation partner.

    The new key is validated before being persisted, so a malformed key
    never replaces a working one.

    Returns 400 Bad Request if new_key_pem is invalid.
    Returns 404 if the partner does not exist.
    """
    try:
        partner = await FederationPartnerService.rotate_partner_public_key(
            db=db,
            partner_id=partner_id,
            new_key_pem=request.public_key_pem,
            new_key_id=request.key_id,
        )
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Federation partner {partner_id} not found.",
        )
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))

    return FederationPartnerDetailResponse.model_validate(partner)


@router.get(
    "/{partner_id}/activity-log",
    response_model=ActivityLogResponse,
    summary="Get partner activity audit log",
)
async def get_activity_log(
    partner_id: int,
    limit: int = Query(100, ge=1, le=500, description="Maximum number of log entries to return"),
    db: AsyncSession = Depends(get_db),
) -> ActivityLogResponse:
    """Return a chronological activity audit log for a federation partner.

    Shows all activities received from this partner, ordered most-recent first.
    Returns 404 if the partner does not exist.
    """
    try:
        activities = await FederationPartnerService.get_activity_log(
            db=db,
            partner_id=partner_id,
            limit=limit,
        )
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Federation partner {partner_id} not found.",
        )

    return ActivityLogResponse(
        partner_id=partner_id,
        activities=[ActivityLogEntryResponse.model_validate(a) for a in activities],
        total=len(activities),
    )


@router.delete(
    "/{partner_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Hard-delete a revoked federation partner",
)
async def delete_partner(
    partner_id: int,
    db: AsyncSession = Depends(get_db),
) -> None:
    """Hard-delete a federation partner record.

    The partner must be in REVOKED state and must have had no activity in the
    last 30 days. Use the trust-state endpoint to revoke a partner first.

    Returns 400 Bad Request if safety constraints are not met.
    Returns 404 if the partner does not exist.
    """
    try:
        await FederationPartnerService.delete_partner(db=db, partner_id=partner_id)
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Federation partner {partner_id} not found.",
        )
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))
