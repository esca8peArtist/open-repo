"""
Export services package for Phase 5 offline ZIM distribution.

This package provides:
  - ZimWriter: writes ZIM files from open-repo content items via python-libzim
  - OPDSGenerator: generates OPDS Atom catalog XML for ZIM discovery
  - ExportConfig / ExportScope: configuration models for export jobs

All classes in this package use stub interfaces designed for post-PR-#1 completion.
The interfaces are stable; implementations will be filled in once Phase 4 merges.
"""

from .zim_writer import ZimWriter, ZimMetadata, ZimEntry, ExportScope, ExportConfig
from .opds_generator import OPDSGenerator, OPDSEntry

__all__ = [
    "ZimWriter",
    "ZimMetadata",
    "ZimEntry",
    "ExportScope",
    "ExportConfig",
    "OPDSGenerator",
    "OPDSEntry",
]
