"""
POST /api/v1/export — trigger a ZIM export job.

Phase 5.1 MVP pre-deployment endpoint. Accepts a JSON body specifying the
export format and optional list of content IDs, enqueues a synchronous export
job (async background in Phase 5.2), and returns a tracking response.

For MVP (Phase 5.1) the job runs synchronously in the request handler using
a background thread so the HTTP response returns immediately with status
"in_progress" and a polling URL. The ZimWriter stub works without libzim
installed; when libzim is installed, it produces a real ZIM file.

Design references:
  - PHASE_5_ARCHITECTURE.md: export pipeline overview
  - phase-5-offline-export-architecture.md: end-to-end flow
  - backend/app/services/export/zim_writer.py: ZimWriter API
  - backend/app/models.py: ZimExport ORM model
"""

from __future__ import annotations

import logging
import os
import tempfile
import threading
import uuid
from datetime import datetime
from pathlib import Path
from typing import List, Optional

from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models import ContentItem, ZimExport
from app.services.export.zim_writer import (
    ExportConfig,
    ExportScope,
    ZimMetadata,
    ZimWriter,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/v1", tags=["export"])

# ---------------------------------------------------------------------------
# Request / Response schemas
# ---------------------------------------------------------------------------


class ExportRequest(BaseModel):
    """Request body for POST /api/v1/export."""

    format: str = Field(
        default="zim",
        description=(
            "Export format. MVP supports 'zim' only. "
            "Future: 'pdf', 'epub'."
        ),
    )
    content_ids: Optional[List[str]] = Field(
        default=None,
        description=(
            "List of ContentItem CIDs to include. "
            "When null or empty, all local content is exported."
        ),
    )
    scope: str = Field(
        default="local",
        description=(
            "Export scope: 'local' (default), 'federated', 'domain', 'tag'. "
            "When content_ids is provided, scope is ignored."
        ),
    )
    scope_value: Optional[str] = Field(
        default=None,
        description="Required when scope is 'domain' or 'tag'.",
    )
    flavour: str = Field(
        default="nopic",
        description="ZIM flavour: nopic, all, mini, agriculture, recipes, etc.",
    )
    language: str = Field(
        default="en",
        description="ISO 639-1 language code for content filtering.",
    )


class ExportResponse(BaseModel):
    """Response body for POST /api/v1/export."""

    status: str = Field(
        description="'success' | 'in_progress' | 'error'"
    )
    export_id: str = Field(
        description="UUID identifying this export job for tracking."
    )
    download_url: Optional[str] = Field(
        default=None,
        description="URL to download the export file. Set when status='success'.",
    )
    poll_url: Optional[str] = Field(
        default=None,
        description="URL to poll for job status. Set when status='in_progress'.",
    )
    error: Optional[str] = Field(
        default=None,
        description="Human-readable error message. Set when status='error'.",
    )
    article_count: Optional[int] = Field(
        default=None,
        description="Number of articles exported. Set when status='success'.",
    )
    file_size_bytes: Optional[int] = Field(
        default=None,
        description="Output file size in bytes. Set when status='success'.",
    )


# ---------------------------------------------------------------------------
# In-memory job registry (MVP — replace with DB-backed queue in Phase 5.2)
# ---------------------------------------------------------------------------

# Maps export_id (str UUID) -> dict with keys: status, result, error
_export_jobs: dict[str, dict] = {}
_export_jobs_lock = threading.Lock()


def _get_job(export_id: str) -> Optional[dict]:
    with _export_jobs_lock:
        return _export_jobs.get(export_id)


def _set_job(export_id: str, state: dict) -> None:
    with _export_jobs_lock:
        _export_jobs[export_id] = state


# ---------------------------------------------------------------------------
# Export output directory
# ---------------------------------------------------------------------------


def _get_export_dir() -> Path:
    """Return the directory where ZIM files are written.

    Uses EXPORT_OUTPUT_DIR env var if set; falls back to a temp directory that
    persists for the process lifetime. The directory is created on first call.
    """
    env_dir = os.getenv("EXPORT_OUTPUT_DIR")
    if env_dir:
        path = Path(env_dir)
    else:
        # Use a stable temp directory under /tmp/open-repo-exports
        path = Path(tempfile.gettempdir()) / "open-repo-exports"

    path.mkdir(parents=True, exist_ok=True)
    return path


# ---------------------------------------------------------------------------
# Helper: render a ContentItem to self-contained HTML
# ---------------------------------------------------------------------------


def _render_item_html(item: ContentItem) -> str:
    """Render a ContentItem ORM object to a minimal self-contained HTML string.

    For MVP this is a lightweight template. Phase 5.2 will replace this with
    a Jinja2 template that matches the open-repo visual design.
    """
    jsonld = item.content_jsonld or {}
    description = ""
    desc_field = jsonld.get("description", {})
    if isinstance(desc_field, dict):
        description = desc_field.get("en", "")
    elif isinstance(desc_field, str):
        description = desc_field

    steps_html = ""
    steps = jsonld.get("steps", [])
    if steps:
        steps_html = "<ol>"
        for step in steps:
            title = step.get("title", {})
            body = step.get("body", {})
            if isinstance(title, dict):
                title = title.get("en", "")
            if isinstance(body, dict):
                body = body.get("en", "")
            steps_html += f"<li><strong>{title}</strong><br>{body}</li>"
        steps_html += "</ol>"

    license_text = item.license or "Unknown"
    item_type = item.item_type or "item"
    domain = item.domain or ""

    return (
        f"<!DOCTYPE html>\n"
        f"<html lang='en'>\n"
        f"<head>\n"
        f"  <meta charset='utf-8'>\n"
        f"  <title>{item.title}</title>\n"
        f"  <style>\n"
        f"    body {{font-family: sans-serif; margin: 1rem; max-width: 800px;}}\n"
        f"    .meta {{font-size: 0.85em; color: #666; margin-bottom: 1rem;}}\n"
        f"    .steps ol li {{margin-bottom: 0.5rem;}}\n"
        f"  </style>\n"
        f"</head>\n"
        f"<body>\n"
        f"  <h1>{item.title}</h1>\n"
        f"  <div class='meta'>"
        f"Type: {item_type} | Domain: {domain} | License: {license_text}"
        f"</div>\n"
        f"  <p>{description}</p>\n"
        f"  <div class='steps'>{steps_html}</div>\n"
        f"</body>\n"
        f"</html>"
    )


# ---------------------------------------------------------------------------
# Core export logic (runs synchronously in background thread)
# ---------------------------------------------------------------------------


def _run_export_job(
    export_id: str,
    content_items: list[dict],
    export_config: ExportConfig,
    zim_name: str,
    node_url: str,
) -> None:
    """Execute the ZIM export job in a background thread.

    Writes the ZIM file, updates the in-memory job registry with final status.
    In Phase 5.2 this will update the ZimExport DB row and push to object storage.

    Args:
        export_id: UUID string for this job.
        content_items: List of dicts with keys: cid, title, item_type, domain,
            license, content_html (rendered HTML string).
        export_config: ExportConfig controlling scope and flavour.
        zim_name: ZIM Name metadata value (e.g., "open-repo_en_nopic").
        node_url: The node's public base URL for ZIM Source metadata.
    """
    logger.info("Export job %s: starting (%d items)", export_id, len(content_items))
    _set_job(export_id, {"status": "in_progress", "started_at": datetime.utcnow().isoformat()})

    try:
        output_dir = _get_export_dir()
        now = datetime.utcnow()
        period = now.strftime("%Y-%m")
        filename = ZimWriter.build_filename(zim_name, period)
        output_path = output_dir / filename

        # Resolve period collision: if file already exists, compute suffix
        if output_path.exists():
            existing_periods = [period]
            new_period = ZimWriter.compute_period(existing_periods, now=now)
            filename = ZimWriter.build_filename(zim_name, new_period)
            output_path = output_dir / filename

        metadata = ZimMetadata(
            title="Open-Repo Offline Library",
            description="Offline practical knowledge library",
            language="eng",
            name=zim_name,
            flavour=export_config.flavour,
            creator="Open-Repo Community",
            publisher="Open-Repo",
            source_url=node_url,
            tags="offline;practical-knowledge;procedures",
        )

        writer = ZimWriter(
            metadata=metadata,
            config=export_config,
            output_path=output_path,
            zimcheck_binary=None,  # Skip zimcheck for MVP; enable in production
        )

        for item in content_items:
            writer.add_article(
                path=f"{item['domain']}/{item['cid']}",
                content=item["content_html"],
                article_type=item["item_type"],
                language=export_config.language,
            )

        # Add minimal index page
        writer.add_article(
            path="index",
            content=(
                "<!DOCTYPE html><html><head><title>Open-Repo Offline Library</title>"
                "<style>body{font-family:sans-serif;margin:1rem;}</style></head>"
                "<body><h1>Open-Repo Offline Library</h1>"
                f"<p>This archive contains {writer.article_count} knowledge items.</p>"
                "</body></html>"
            ),
            article_type="index",
        )

        result = writer.create_zim(run_zimcheck=False)

        download_url = os.getenv("EXPORT_CDN_BASE_URL", f"file://{output_dir}")
        if not download_url.endswith("/"):
            download_url += "/"
        download_url += filename

        logger.info(
            "Export job %s: complete — %d articles, %d bytes, sha256=%s...",
            export_id, result.article_count, result.file_size_bytes,
            result.sha256[:8] if result.sha256 else "n/a",
        )

        _set_job(export_id, {
            "status": "success",
            "output_path": str(output_path),
            "filename": filename,
            "download_url": download_url,
            "article_count": result.article_count,
            "file_size_bytes": result.file_size_bytes,
            "sha256": result.sha256,
            "completed_at": datetime.utcnow().isoformat(),
        })

    except Exception as exc:
        logger.error("Export job %s: failed — %s", export_id, exc, exc_info=True)
        _set_job(export_id, {
            "status": "error",
            "error": str(exc),
            "failed_at": datetime.utcnow().isoformat(),
        })


# ---------------------------------------------------------------------------
# Endpoint: POST /api/v1/export
# ---------------------------------------------------------------------------


@router.post("/export", response_model=ExportResponse, status_code=202)
async def trigger_export(
    request: ExportRequest,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db),
) -> ExportResponse:
    """Trigger an offline content export job.

    For Phase 5.1 MVP only 'zim' format is supported. The job runs in a
    background thread and returns immediately with status 'in_progress'.
    Poll GET /api/v1/export/{export_id} to check completion.

    Request body:
        format: "zim" (only supported value for MVP)
        content_ids: optional list of CIDs to export (null = all local content)
        scope: "local" | "federated" | "domain" | "tag"
        scope_value: required when scope is "domain" or "tag"
        flavour: ZIM flavour (default "nopic")
        language: ISO 639-1 language code (default "en")

    Returns:
        202 Accepted with export_id and poll_url when job is enqueued.
    """
    # Validate format
    if request.format != "zim":
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported export format '{request.format}'. Only 'zim' is supported in Phase 5.1 MVP.",
        )

    # Validate scope
    scope_map = {
        "local": ExportScope.LOCAL_ONLY,
        "federated": ExportScope.FEDERATED,
        "domain": ExportScope.DOMAIN,
        "tag": ExportScope.TAG,
    }
    if request.scope not in scope_map:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid scope '{request.scope}'. Must be one of: {', '.join(scope_map)}.",
        )

    # Validate domain/tag scope requires scope_value
    if request.scope in ("domain", "tag") and not request.scope_value:
        raise HTTPException(
            status_code=400,
            detail=f"scope_value is required when scope is '{request.scope}'.",
        )

    # Build ExportConfig — validates flavour internally
    try:
        export_config = ExportConfig(
            scope=scope_map[request.scope],
            scope_value=request.scope_value,
            language=request.language,
            language_iso3=_iso2_to_iso3(request.language),
            flavour=request.flavour,
            include_images=False,  # nopic default; expandable in Phase 5.2
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))

    # Query content items from DB
    try:
        if request.content_ids:
            # Specific IDs requested
            result = await db.execute(
                select(ContentItem).where(ContentItem.cid.in_(request.content_ids))
            )
        else:
            # All local content (no federation filter at model level yet; select all)
            result = await db.execute(select(ContentItem))

        items = result.scalars().all()
    except Exception as exc:
        logger.error("Export: DB query failed — %s", exc)
        raise HTTPException(
            status_code=503,
            detail=f"Database unavailable: {exc}",
        )

    if not items:
        raise HTTPException(
            status_code=404,
            detail="No content items found matching the export criteria.",
        )

    # Render items to HTML (serializable dicts for background thread)
    content_dicts = []
    for item in items:
        content_dicts.append({
            "cid": item.cid,
            "title": item.title,
            "item_type": item.item_type,
            "domain": item.domain,
            "license": item.license,
            "content_html": _render_item_html(item),
        })

    # Build ZIM name from language and flavour
    zim_name = f"open-repo_{request.language}_{request.flavour}"
    node_url = os.getenv("NODE_URL", "http://localhost:8000")

    # Assign a unique export ID
    export_id = str(uuid.uuid4())

    logger.info(
        "Export job %s: accepted — format=%s, items=%d, scope=%s, flavour=%s",
        export_id, request.format, len(content_dicts), request.scope, request.flavour,
    )

    # Enqueue background job
    background_tasks.add_task(
        _run_export_job,
        export_id=export_id,
        content_items=content_dicts,
        export_config=export_config,
        zim_name=zim_name,
        node_url=node_url,
    )

    # Mark job as in_progress immediately so poll endpoint can find it
    _set_job(export_id, {
        "status": "in_progress",
        "enqueued_at": datetime.utcnow().isoformat(),
    })

    poll_url = f"/api/v1/export/{export_id}"

    return ExportResponse(
        status="in_progress",
        export_id=export_id,
        poll_url=poll_url,
    )


# ---------------------------------------------------------------------------
# Endpoint: GET /api/v1/export/{export_id}
# ---------------------------------------------------------------------------


@router.get("/export/{export_id}", response_model=ExportResponse)
async def get_export_status(export_id: str) -> ExportResponse:
    """Poll the status of an export job.

    Returns the current status of the export job identified by export_id.

    Responses:
        status='in_progress': job is still running
        status='success': job completed; download_url and article_count are set
        status='error': job failed; error message is set
        404: export_id not found
    """
    job = _get_job(export_id)
    if job is None:
        raise HTTPException(
            status_code=404,
            detail=f"Export job '{export_id}' not found. "
                   f"Export jobs are held in memory and lost on server restart. "
                   f"Submit a new export request.",
        )

    status = job.get("status", "unknown")

    if status == "success":
        return ExportResponse(
            status="success",
            export_id=export_id,
            download_url=job.get("download_url"),
            article_count=job.get("article_count"),
            file_size_bytes=job.get("file_size_bytes"),
        )

    if status == "error":
        return ExportResponse(
            status="error",
            export_id=export_id,
            error=job.get("error", "Unknown error"),
        )

    # in_progress or unknown
    return ExportResponse(
        status="in_progress",
        export_id=export_id,
        poll_url=f"/api/v1/export/{export_id}",
    )


# ---------------------------------------------------------------------------
# Helper: ISO 639-1 -> ISO 639-3 conversion (minimal subset)
# ---------------------------------------------------------------------------

_ISO2_TO_ISO3 = {
    "en": "eng",
    "es": "spa",
    "fr": "fra",
    "de": "deu",
    "pt": "por",
    "ar": "ara",
    "zh": "zho",
    "sw": "swa",
    "hi": "hin",
    "bn": "ben",
}


def _iso2_to_iso3(lang: str) -> str:
    """Convert ISO 639-1 two-letter code to ISO 639-3 three-letter code.

    Falls back to appending 'g' for unknown codes (a safe default that passes
    libzim's language validation for most cases).
    """
    return _ISO2_TO_ISO3.get(lang.lower(), f"{lang}g"[:3])
