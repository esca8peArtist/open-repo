"""
OPDS 1.2 Catalog endpoints for Kiwix in-app discovery.

Implements four REST endpoints that serve Atom/OPDS XML feeds compatible with
Kiwix (mobile/desktop) and other OPDS clients:

  GET /opds/v2/root.xml            — Navigation feed with links to sub-feeds
  GET /opds/v2/entries              — Acquisition feed listing all ZIM exports
  GET /opds/v2/entry/{uuid}        — Single-entry view with metadata
  GET /opds/v2/searchdescription.xml — OpenSearch description for catalog search

Design references:
  - PHASE_5_CANDIDATE_2_OPDS_IMPLEMENTATION_ROADMAP.md
  - OPDS 1.2 Specification: https://specs.opds.io/opds-1.2.html
  - Kiwix OPDS integration: https://wiki.kiwix.org/wiki/OPDS
"""

from __future__ import annotations

import logging
import uuid as uuid_lib
from typing import Optional

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models import ZimExport
from app.services.export.opds_generator import OPDSEntry, OPDSGenerator, OPDSVersionEntry

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/opds/v2", tags=["opds"])

# OPDS node configuration (would be loaded from config in production)
# For now, use defaults
OPDS_NODE_UUID = "550e8400-e29b-41d4-a716-446655440000"
OPDS_NODE_NAME = "Open-Repo Node"
OPDS_NODE_URL = "https://open-repo.example.org"


async def get_opds_generator(db: AsyncSession) -> OPDSGenerator:
    """
    Build an OPDSGenerator instance with all current ZIM exports.

    Queries the zim_exports table for all entries with status='available'
    and populates the generator. This is called by each endpoint to ensure
    the catalog is up-to-date.

    Args:
        db: AsyncSession database connection.

    Returns:
        Initialized OPDSGenerator ready to generate catalog XML.
    """
    # Query all current (is_current=True) ZIM exports
    result = await db.execute(
        select(ZimExport).where(ZimExport.is_current == True).order_by(
            ZimExport.name, ZimExport.period.desc()
        )
    )
    exports = result.scalars().all()

    # Create generator with appropriate catalog URL
    generator = OPDSGenerator(
        node_uuid=OPDS_NODE_UUID,
        node_name=OPDS_NODE_NAME,
        node_url=OPDS_NODE_URL,
        catalog_url=f"{OPDS_NODE_URL}/opds/v2/root.xml",
    )

    # Add each export as an OPDS entry
    for export in exports:
        if export.cdn_url and export.sha256:
            try:
                entry = OPDSEntry.from_zim_export(export)

                # Load version history if needed (fetch previous versions of same name+flavour)
                if export.is_current:
                    prev_result = await db.execute(
                        select(ZimExport)
                        .where(
                            (ZimExport.name == export.name)
                            & (ZimExport.flavour == export.flavour)
                            & (ZimExport.is_current == False)
                            & (ZimExport.cdn_url != None)
                        )
                        .order_by(ZimExport.period.desc())
                        .limit(generator.max_version_history)
                    )
                    prev_exports = prev_result.scalars().all()

                    entry.version_history = [
                        OPDSVersionEntry(
                            period=pe.period,
                            download_url=pe.cdn_url,
                            file_size_bytes=pe.file_size_bytes,
                            generated_at=pe.completed_at or pe.created_at,
                            sha256_checksum=pe.sha256,
                        )
                        for pe in prev_exports
                    ]

                generator.add_entry(entry)
                logger.debug(
                    "Added OPDS entry: name=%s, period=%s, uuid=%s",
                    export.name, export.period, export.zim_uuid
                )
            except ValueError as e:
                logger.warning("Skipping ZimExport %s: %s", export.id, e)
                continue

    return generator


@router.get("/root.xml", response_class=None)
async def get_opds_root_catalog(
    db: AsyncSession = Depends(get_db),
) -> tuple[bytes, dict]:
    """
    GET /opds/v2/root.xml — OPDS root navigation catalog.

    Returns a navigation feed with links to:
      - The acquisition feed (/opds/v2/entries)
      - OpenSearch description (/opds/v2/searchdescription.xml)

    Response:
      - Content-Type: application/atom+xml;profile=opds-catalog;kind=navigation
      - Body: Atom XML (UTF-8 encoded)

    Kiwix behavior:
      When a Kiwix user adds the URL of this endpoint to their catalog,
      Kiwix parses this root feed and shows the link to "All Offline Exports"
      which points to the acquisition feed.
    """
    try:
        generator = await get_opds_generator(db)
        xml_bytes = generator.generate_root_catalog()

        # Validate before serving
        errors = generator.validate_opds_xml(xml_bytes)
        if errors:
            logger.error("Root catalog validation errors: %s", errors)
            raise HTTPException(status_code=500, detail="Root catalog generation error")

        return (
            xml_bytes,
            {"media_type": "application/atom+xml;profile=opds-catalog;kind=navigation"},
        )
    except Exception as e:
        logger.exception("Error generating OPDS root catalog: %s", e)
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/entries", response_class=None)
async def get_opds_acquisition_feed(
    db: AsyncSession = Depends(get_db),
) -> tuple[bytes, dict]:
    """
    GET /opds/v2/entries — OPDS acquisition feed.

    Returns a feed with one entry per available ZIM export. Each entry includes:
      - Download link (MIME type application/x-zim)
      - File metadata (size, checksum, language, article count)
      - Version history (links to previous versions)
      - Illustration/thumbnail (if available)

    Response:
      - Content-Type: application/atom+xml;profile=opds-catalog;kind=acquisition
      - Body: Atom XML (UTF-8 encoded)

    Kiwix behavior:
      When a Kiwix user navigates to this feed, they see a list of all available
      ZIM files. Tapping an entry triggers one-click download and installation.
    """
    try:
        generator = await get_opds_generator(db)
        xml_bytes = generator.generate_acquisition_feed()

        # Validate before serving
        errors = generator.validate_opds_xml(xml_bytes)
        if errors:
            logger.error("Acquisition feed validation errors: %s", errors)
            raise HTTPException(status_code=500, detail="Acquisition feed generation error")

        return (
            xml_bytes,
            {"media_type": "application/atom+xml;profile=opds-catalog;kind=acquisition"},
        )
    except Exception as e:
        logger.exception("Error generating OPDS acquisition feed: %s", e)
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/entry/{entry_uuid}", response_class=None)
async def get_opds_single_entry(
    entry_uuid: str,
    db: AsyncSession = Depends(get_db),
) -> tuple[bytes, dict]:
    """
    GET /opds/v2/entry/{uuid} — Single ZIM entry view with full metadata.

    Returns a feed with a single entry (the ZIM export matching the given UUID).
    Useful for detailed metadata inspection in Kiwix or other OPDS clients.

    Args:
        entry_uuid: UUID of the ZIM export (matches OPDSEntry.uuid).

    Response:
      - Content-Type: application/atom+xml;profile=opds-catalog;kind=acquisition
      - Body: Atom XML with single entry (UTF-8 encoded)

    HTTP 404:
      If entry_uuid does not match any current ZIM export, returns 404.
    """
    try:
        # Validate UUID format
        try:
            uuid_lib.UUID(entry_uuid)
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid UUID format")

        generator = await get_opds_generator(db)
        xml_bytes = generator.generate_single_entry(entry_uuid)

        if xml_bytes is None:
            raise HTTPException(
                status_code=404,
                detail=f"Entry {entry_uuid} not found in catalog",
            )

        # Validate before serving
        errors = generator.validate_opds_xml(xml_bytes)
        if errors:
            logger.error("Single entry validation errors: %s", errors)
            raise HTTPException(status_code=500, detail="Single entry generation error")

        return (
            xml_bytes,
            {"media_type": "application/atom+xml;profile=opds-catalog;kind=acquisition"},
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.exception("Error generating OPDS single entry: %s", e)
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/searchdescription.xml", response_class=None)
async def get_opds_search_description(
    db: AsyncSession = Depends(get_db),
) -> tuple[bytes, dict]:
    """
    GET /opds/v2/searchdescription.xml — OpenSearch description.

    Returns an OpenSearch 1.1 description document that tells Kiwix and other
    OPDS clients how to search the catalog. The search template points to
    /opds/v2/entries?q={searchTerms}.

    Response:
      - Content-Type: application/opensearchdescription+xml
      - Body: OpenSearch XML (UTF-8 encoded)

    Kiwix behavior:
      Kiwix uses this endpoint to enable search integration. When a user types
      a search query, Kiwix constructs a URL using the template in this file.
    """
    try:
        generator = await get_opds_generator(db)
        xml_bytes = generator.generate_search_description()

        return (
            xml_bytes,
            {"media_type": "application/opensearchdescription+xml"},
        )
    except Exception as e:
        logger.exception("Error generating OpenSearch description: %s", e)
        raise HTTPException(status_code=500, detail=str(e))
