"""
OPDS 1.2 Feed endpoints for Kiwix in-app catalog discovery.

Endpoints:
  GET /opds/v2/root.xml — Root navigation catalog (OPDS navigation feed)
  GET /opds/v2/entries — Acquisition feed listing all published ZIM exports
  GET /opds/v2/entry/{uuid} — Single-entry view with version history
  GET /opds/v2/searchdescription.xml — OpenSearch description for Kiwix search

All endpoints return Atom XML with OPDS profile links, compatible with Kiwix
readers' built-in OPDS parser.

Design references:
  - PHASE_5_ARCHITECTURE.md: OPDS Catalog Integration
  - PHASE_5_CANDIDATE_2_OPDS_IMPLEMENTATION_ROADMAP.md: Detailed implementation plan
"""

from __future__ import annotations

import logging

from fastapi import APIRouter, Depends, HTTPException, Request
from starlette.responses import Response
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models import ZimExport
from app.services.export.opds_generator import (
    MIME_OPDS_ACQ,
    MIME_OPDS_NAV,
    MIME_OPENSEARCH,
    OPDSEntry,
    OPDSGenerator,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/opds/v2", tags=["opds"])

# TODO: Make these configurable from node settings
DEFAULT_NODE_UUID = "550e8400-e29b-41d4-a716-446655440000"
DEFAULT_NODE_NAME = "Open-Repo"
DEFAULT_NODE_URL = "https://open-repo.example.org"


async def _get_generator(db: AsyncSession, base_url: str) -> OPDSGenerator:
    """
    Construct an OPDSGenerator populated with current ZIM exports.

    Args:
        db: Database session.
        base_url: Base URL for the OPDS catalog (e.g., https://node.example.org).

    Returns:
        OPDSGenerator instance with all current ZIM exports as entries.

    Raises:
        No exceptions — returns an empty generator if no exports found.
    """
    catalog_url = f"{base_url}/opds/v2/root.xml"
    generator = OPDSGenerator(
        node_uuid=DEFAULT_NODE_UUID,
        node_name=DEFAULT_NODE_NAME,
        node_url=DEFAULT_NODE_URL,
        catalog_url=catalog_url,
    )

    # Load all current (is_current=1) exports with status='available'
    stmt = select(ZimExport).where(
        (ZimExport.is_current == 1) & (ZimExport.status == "available")
    ).order_by(ZimExport.name, ZimExport.period.desc())

    result = await db.execute(stmt)
    exports = result.scalars().all()

    for export in exports:
        try:
            entry = OPDSEntry.from_zim_export(export)
            generator.add_entry(entry)
        except ValueError as exc:
            logger.warning(
                f"Skipping ZimExport {export.id} ({export.name}): {exc}"
            )

    return generator


@router.get("/root.xml")
async def get_root_catalog(
    request: Request,
    db: AsyncSession = Depends(get_db),
) -> Response:
    """
    GET /opds/v2/root.xml — OPDS root navigation catalog.

    Returns a navigation feed with links to:
      - Acquisition feed (/opds/v2/entries)
      - OpenSearch description (/opds/v2/searchdescription.xml)

    Content-Type: application/atom+xml;profile=opds-catalog;kind=navigation
    """
    # Infer base_url from request
    base_url = str(request.base_url).rstrip("/")

    generator = await _get_generator(db, base_url)
    xml_bytes = generator.generate_root_catalog()

    # Validate
    errors = OPDSGenerator.validate_opds_xml(xml_bytes)
    if errors:
        logger.error(f"OPDS validation failed: {errors}")

    return Response(content=xml_bytes, media_type=MIME_OPDS_NAV)


@router.get("/entries")
async def get_entries_feed(
    request: Request,
    db: AsyncSession = Depends(get_db),
) -> Response:
    """
    GET /opds/v2/entries — OPDS acquisition feed listing all ZIM exports.

    Each entry includes:
      - Title, description, language metadata
      - Download link (with MIME type application/x-zim)
      - SHA-256 checksum sidecar
      - Version history (if available)

    Content-Type: application/atom+xml;profile=opds-catalog;kind=acquisition
    """
    base_url = str(request.base_url).rstrip("/")

    generator = await _get_generator(db, base_url)
    xml_bytes = generator.generate_acquisition_feed()

    # Validate
    errors = OPDSGenerator.validate_opds_xml(xml_bytes)
    if errors:
        logger.error(f"OPDS validation failed: {errors}")

    return Response(content=xml_bytes, media_type=MIME_OPDS_ACQ)


@router.get("/entry/{entry_uuid}")
async def get_single_entry(
    entry_uuid: str,
    request: Request,
    db: AsyncSession = Depends(get_db),
) -> Response:
    """
    GET /opds/v2/entry/{uuid} — Single entry with full version history.

    Used by Kiwix to view a specific archive's version history and metadata.

    Args:
        entry_uuid: UUID of the ZIM export.

    Returns:
        OPDS entry as Atom XML, or 404 if not found.

    Content-Type: application/atom+xml;profile=opds-catalog;kind=acquisition
    """
    base_url = str(request.base_url).rstrip("/")

    generator = await _get_generator(db, base_url)
    xml_bytes = generator.generate_single_entry(entry_uuid)

    if xml_bytes is None:
        raise HTTPException(status_code=404, detail=f"Entry {entry_uuid} not found")

    return Response(content=xml_bytes, media_type=MIME_OPDS_ACQ)


@router.get("/searchdescription.xml")
async def get_search_description(
    request: Request,
    db: AsyncSession = Depends(get_db),
) -> Response:
    """
    GET /opds/v2/searchdescription.xml — OpenSearch description for catalog search.

    Tells Kiwix how to query the OPDS catalog (e.g., by title search).
    Used by Kiwix's integrated search bar.

    Content-Type: application/opensearchdescription+xml
    """
    base_url = str(request.base_url).rstrip("/")

    generator = await _get_generator(db, base_url)
    xml_bytes = generator.generate_search_description()

    return Response(content=xml_bytes, media_type=MIME_OPENSEARCH)
