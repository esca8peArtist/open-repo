"""
Export services package for Phase 5 offline ZIM distribution.

This package provides:
  - ExportService: orchestrates export jobs (query, render, ZIM write, validate)
  - ZimWriter: writes ZIM files from open-repo content items via python-libzim
  - OPDSGenerator: generates OPDS Atom catalog XML for ZIM discovery
  - ExportConfig / ExportScope: configuration models for export jobs

Phase 5 Step 1: ExportService is fully implemented with content querying,
HTML rendering (type-aware: procedure, recipe, schematic, plan), and the
export_to_zim() orchestration method.

ZimWriter and OPDSGenerator are production-ready stubs with TODO markers at
the python-libzim integration points. All public interfaces are stable and
comprehensively tested.
"""

from .export_service import ExportService
from .zim_writer import (
    ExportConfig,
    ExportScope,
    ZimCheckError,
    ZimEntry,
    ZimMetadata,
    ZimWriteResult,
    ZimWriter,
)
from .opds_generator import OPDSGenerator, OPDSEntry

__all__ = [
    "ExportService",
    "ZimWriter",
    "ZimMetadata",
    "ZimEntry",
    "ZimWriteResult",
    "ZimCheckError",
    "ExportScope",
    "ExportConfig",
    "OPDSGenerator",
    "OPDSEntry",
]
