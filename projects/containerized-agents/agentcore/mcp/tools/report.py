"""
PDF report generator MCP tool.

Generates a structured PDF report from a title and a list of sections.
Each section can contain a heading, body text, and an optional table.

Backend: reportlab (preferred, pure Python) with weasyprint as fallback.
Install: pip install reportlab   or   pip install weasyprint

Output: saved to /data/reports/<output_filename>.pdf
Config (env vars)
-----------------
REPORT_OUTPUT_DIR — directory to save reports (default: /data/reports)

Profiles: business_intelligence (5)
"""
from __future__ import annotations

import asyncio
import logging
import os
from datetime import datetime, timezone
from functools import partial
from pathlib import Path
from typing import Any

from agentcore.config import get_settings
from agentcore.mcp.protocol import MCPContext, MCPTool, MCPToolResult, MCPToolSchema

logger = logging.getLogger(__name__)

_PROFILES = ["business_intelligence"]
_DEFAULT_REPORT_DIR = "/data/reports"


def _report_dir() -> str:
    return get_settings().report_output_dir or _DEFAULT_REPORT_DIR


# ---------------------------------------------------------------------------
# reportlab implementation
# ---------------------------------------------------------------------------


def _generate_pdf_reportlab(title: str, sections: list[dict], output_path: str) -> None:
    from reportlab.lib import colors  # type: ignore[import]
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import cm
    from reportlab.platypus import (  # type: ignore[import]
        SimpleDocTemplate,
        Paragraph,
        Spacer,
        Table,
        TableStyle,
    )

    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=2 * cm,
        leftMargin=2 * cm,
        topMargin=2.5 * cm,
        bottomMargin=2 * cm,
    )

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "ReportTitle",
        parent=styles["Title"],
        fontSize=18,
        spaceAfter=20,
    )
    heading_style = ParagraphStyle(
        "SectionHeading",
        parent=styles["Heading2"],
        fontSize=13,
        spaceBefore=14,
        spaceAfter=6,
    )
    body_style = styles["Normal"]
    meta_style = ParagraphStyle(
        "Meta",
        parent=styles["Normal"],
        fontSize=9,
        textColor=colors.grey,
        spaceAfter=20,
    )

    elements = []

    # Title and metadata
    elements.append(Paragraph(title, title_style))
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    elements.append(Paragraph(f"Generated: {generated_at}", meta_style))
    elements.append(Spacer(1, 0.3 * cm))

    for section in sections:
        heading = section.get("heading", "")
        content = section.get("content", "")
        table_data = section.get("table")

        if heading:
            elements.append(Paragraph(heading, heading_style))

        if content:
            # Split into paragraphs by blank lines
            for para in content.split("\n\n"):
                para = para.strip()
                if para:
                    elements.append(Paragraph(para.replace("\n", "<br/>"), body_style))
                    elements.append(Spacer(1, 0.2 * cm))

        if table_data and isinstance(table_data, dict):
            headers = table_data.get("headers", [])
            rows = table_data.get("rows", [])
            if headers and rows:
                table_rows = [headers] + rows
                tbl = Table(table_rows, hAlign="LEFT")
                tbl.setStyle(
                    TableStyle(
                        [
                            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#4472C4")),
                            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                            ("FONTSIZE", (0, 0), (-1, -1), 9),
                            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#EBF3FB")]),
                            ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#AAAAAA")),
                            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                            ("LEFTPADDING", (0, 0), (-1, -1), 6),
                            ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                            ("TOPPADDING", (0, 0), (-1, -1), 4),
                            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                        ]
                    )
                )
                elements.append(tbl)
                elements.append(Spacer(1, 0.3 * cm))

    doc.build(elements)


# ---------------------------------------------------------------------------
# weasyprint fallback
# ---------------------------------------------------------------------------


def _generate_pdf_weasyprint(title: str, sections: list[dict], output_path: str) -> None:
    from weasyprint import HTML  # type: ignore[import]

    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    sections_html = ""
    for section in sections:
        heading = section.get("heading", "")
        content = section.get("content", "")
        table_data = section.get("table")

        section_html = ""
        if heading:
            section_html += f"<h2>{heading}</h2>\n"
        if content:
            for para in content.split("\n\n"):
                para = para.strip()
                if para:
                    section_html += f"<p>{para.replace(chr(10), '<br/>')}</p>\n"
        if table_data and isinstance(table_data, dict):
            headers = table_data.get("headers", [])
            rows = table_data.get("rows", [])
            if headers and rows:
                section_html += "<table><thead><tr>"
                for h in headers:
                    section_html += f"<th>{h}</th>"
                section_html += "</tr></thead><tbody>"
                for row in rows:
                    section_html += "<tr>"
                    for cell in row:
                        section_html += f"<td>{cell}</td>"
                    section_html += "</tr>"
                section_html += "</tbody></table>\n"
        sections_html += section_html

    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8"/>
<style>
body {{ font-family: Arial, sans-serif; margin: 2cm; font-size: 11pt; }}
h1 {{ color: #2E4057; font-size: 18pt; }}
h2 {{ color: #4472C4; font-size: 13pt; margin-top: 1.2em; }}
p {{ line-height: 1.5; }}
table {{ border-collapse: collapse; width: 100%; margin: 0.8em 0; }}
th {{ background: #4472C4; color: white; padding: 6px; text-align: left; }}
td {{ padding: 5px 6px; border: 0.5px solid #aaa; }}
tr:nth-child(even) {{ background: #EBF3FB; }}
.meta {{ color: #888; font-size: 9pt; }}
</style>
</head>
<body>
<h1>{title}</h1>
<p class="meta">Generated: {generated_at}</p>
{sections_html}
</body>
</html>"""

    HTML(string=html).write_pdf(output_path)


# ---------------------------------------------------------------------------
# MCP Tool
# ---------------------------------------------------------------------------


class GeneratePdfReportTool(MCPTool):
    """Generate a structured PDF report with sections and optional tables."""

    @property
    def schema(self) -> MCPToolSchema:
        return MCPToolSchema(
            name="generate_pdf_report",
            description=(
                "Generate a PDF report with a title and one or more sections. "
                "Each section can contain a heading, body text, and an optional table. "
                "The report is saved to /data/reports/ and the file path is returned."
            ),
            input_schema={
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "Report title.",
                    },
                    "sections": {
                        "type": "array",
                        "description": "List of report sections.",
                        "items": {
                            "type": "object",
                            "properties": {
                                "heading": {
                                    "type": "string",
                                    "description": "Section heading.",
                                },
                                "content": {
                                    "type": "string",
                                    "description": "Section body text (supports paragraph breaks via blank lines).",
                                },
                                "table": {
                                    "type": "object",
                                    "description": "Optional table to include in this section.",
                                    "properties": {
                                        "headers": {
                                            "type": "array",
                                            "items": {"type": "string"},
                                            "description": "Column header labels.",
                                        },
                                        "rows": {
                                            "type": "array",
                                            "items": {
                                                "type": "array",
                                                "items": {},
                                            },
                                            "description": "Table data rows.",
                                        },
                                    },
                                },
                            },
                        },
                    },
                    "output_filename": {
                        "type": "string",
                        "description": (
                            "Output filename without path or extension "
                            "(default: auto-generated from title + timestamp)."
                        ),
                    },
                },
                "required": ["title", "sections"],
            },
            requires_internet=False,
            profiles=_PROFILES,
        )

    async def execute(self, arguments: dict, context: MCPContext) -> MCPToolResult:
        title: str = arguments["title"]
        sections: list[dict] = arguments["sections"]
        raw_filename: str = arguments.get("output_filename", "")

        # Sanitise filename
        if not raw_filename:
            safe_title = "".join(c if c.isalnum() or c in "-_ " else "_" for c in title)
            safe_title = safe_title.replace(" ", "_")[:60]
            timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
            filename = f"{safe_title}_{timestamp}.pdf"
        else:
            safe = "".join(c if c.isalnum() or c in "-_." else "_" for c in raw_filename)
            filename = safe if safe.endswith(".pdf") else safe + ".pdf"

        report_dir = _report_dir()
        os.makedirs(report_dir, exist_ok=True)
        output_path = os.path.join(report_dir, filename)

        try:
            loop = asyncio.get_running_loop()
            await loop.run_in_executor(
                None, partial(_generate_pdf, title, sections, output_path)
            )
            file_size = os.path.getsize(output_path)
            return MCPToolResult(
                success=True,
                content={
                    "file_path": output_path,
                    "filename": filename,
                    "size_bytes": file_size,
                    "sections_count": len(sections),
                },
            )
        except Exception as exc:
            logger.error("generate_pdf_report error: %s", exc)
            return MCPToolResult(success=False, content=None, error=str(exc))


def _generate_pdf(title: str, sections: list[dict], output_path: str) -> None:
    """Try reportlab first, then weasyprint, then raise a clear error."""
    try:
        _generate_pdf_reportlab(title, sections, output_path)
        return
    except ImportError:
        pass

    try:
        _generate_pdf_weasyprint(title, sections, output_path)
        return
    except ImportError:
        pass

    raise RuntimeError(
        "PDF generation requires either 'reportlab' or 'weasyprint'. "
        "Install with: pip install reportlab   or   pip install weasyprint"
    )
