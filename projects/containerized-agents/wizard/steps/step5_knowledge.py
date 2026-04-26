"""Step 5 — Knowledge base: upload documents and provide URLs for RAG."""
from __future__ import annotations

import logging
from pathlib import Path

from fastapi import APIRouter, Form, Request, UploadFile
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from wizard.config import TOTAL_STEPS
from wizard.state import get_state, save_state

router = APIRouter()
templates = Jinja2Templates(directory="wizard/templates")
logger = logging.getLogger(__name__)

_UPLOAD_DIR = Path("/tmp/wizard-uploads")
_ALLOWED_SUFFIXES = {".pdf", ".docx", ".txt", ".md", ".csv"}


@router.get("/step/5", response_class=HTMLResponse)
async def get_step5(request: Request) -> HTMLResponse:
    state = get_state()
    return templates.TemplateResponse(
        "step5.html",
        {
            "request": request,
            "state": state,
            "current_step": 5,
            "total_steps": TOTAL_STEPS,
            "step_title": "Knowledge Base",
        },
    )


@router.post("/api/upload-document")
async def upload_document(file: UploadFile) -> JSONResponse:
    """Accept a document upload, save it to /tmp/wizard-uploads/."""
    if not file.filename:
        return JSONResponse({"success": False, "error": "No filename"}, status_code=400)

    suffix = Path(file.filename).suffix.lower()
    if suffix not in _ALLOWED_SUFFIXES:
        return JSONResponse(
            {"success": False, "error": f"File type '{suffix}' not supported. Allowed: {', '.join(_ALLOWED_SUFFIXES)}"},
            status_code=400,
        )

    try:
        _UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
        dest = _UPLOAD_DIR / file.filename
        content = await file.read()
        dest.write_bytes(content)

        state = get_state()
        if str(dest) not in state.uploaded_documents:
            state.uploaded_documents.append(str(dest))
            save_state(state)

        return JSONResponse({"success": True, "filename": file.filename, "path": str(dest)})
    except Exception as exc:
        logger.exception("Document upload failed: %s", exc)
        return JSONResponse({"success": False, "error": str(exc)}, status_code=500)


@router.post("/step/5")
async def post_step5(
    request: Request,
    rag_urls: str = Form(""),
) -> RedirectResponse:
    state = get_state()
    urls = [u.strip() for u in rag_urls.splitlines() if u.strip()]
    state.rag_urls = urls
    if 5 not in state.completed_steps:
        state.completed_steps.append(5)
    state.current_step = 6
    save_state(state)
    return RedirectResponse("/step/6", status_code=303)
