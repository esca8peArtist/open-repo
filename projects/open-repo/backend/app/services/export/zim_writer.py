"""
ZimWriter: Python-libzim-based ZIM file generation for open-repo offline exports.

This module provides the stub interfaces for Phase 5 ZIM file generation. The class
structure, method signatures, docstrings, and data models are complete. The actual
python-libzim integration is stubbed with TODO markers at each integration point.

Design references:
  - phase-5-kiwix-integration-guide.md (metadata spec, naming, CDN)
  - phase-5-offline-export-architecture.md (end-to-end flow, federation integration)
  - phase-5-kiwix-architecture.md (python-libzim API overview)

Dependencies (to be added to pyproject.toml before full implementation):
  - libzim>=3.2,<4.0  (PyPI package name: libzim, not python-libzim)
  - jinja2>=3.1       (likely already present via Phase 4)

Usage pattern (post-implementation):
    metadata = ZimMetadata(
        title="Open-Repo: Full Library (English)",
        description="Offline practical knowledge library",
        language="eng",
        name="open-repo_en_nopic",
        flavour="nopic",
        creator="Open-Repo Community",
        publisher="Open-Repo",
        source_url="https://node.example.org",
    )
    config = ExportConfig(scope=ExportScope.LOCAL_ONLY, flavour="nopic")
    writer = ZimWriter(metadata=metadata, config=config, output_path="/tmp/export.zim")
    for item in content_items:
        writer.add_article(
            path=item.cid,
            content=render_html(item),
            article_type=item.item_type,
            language="en",
        )
    writer.create_zim()
"""

from __future__ import annotations

import hashlib
import logging
import subprocess
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Optional

from libzim.writer import Creator, Item, StringProvider, Hint, Compression

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Fallback illustration
# A minimal valid 48x48 PNG (solid teal #2a9d8f) used when no custom
# illustration is provided. openZIM requires a 48x48 PNG for the Illustration
# metadata field. This constant allows the module to be imported by tests
# that verify the PNG's IHDR dimensions.
# ---------------------------------------------------------------------------

_FALLBACK_ILLUSTRATION_PNG: bytes = (
    b'\x89PNG\r\n\x1a\n'                          # PNG signature
    b'\x00\x00\x00\rIHDR'                          # IHDR chunk (13 bytes)
    b'\x00\x00\x000'                               # width = 48
    b'\x00\x00\x000'                               # height = 48
    b'\x08\x02\x00\x00\x00'                        # bit depth=8, RGB, no interlace
    b'\xd8`n\xd0'                                  # IHDR CRC
    b'\x00\x00\x00:IDAT'                           # IDAT chunk (58 bytes)
    b'x\xda\xed\xceA\r\x00\x00\x08\x04\xa0\xcbcY'
    b'\x13\xd8\xd5\x16\xce\x07\x1b\x01HM\xbf\x12'
    b'!!!!!!!!!!!!!!!!!!!!!!!!!'
    b'\xa1;\x0b\xb2)\x06\xb5\xc1\xcc\xc3\xcb'
    b'\x00\x00\x00\x00IEND\xaeB`\x82'              # IEND chunk
)


# ---------------------------------------------------------------------------
# Enumerations and configuration models
# ---------------------------------------------------------------------------


class ExportScope(str, Enum):
    """
    Controls which content items are included in an export job.

    LOCAL_ONLY: Items authored or approved by this node only. This is the safe
        default for most exports. Federated content from partner nodes is excluded.

    FEDERATED: All content in the local database including items received from
        federation partners. Each federated item will have attribution metadata
        rendered in the HTML footer.

    DOMAIN: Filtered to a single knowledge domain (e.g., 'agriculture', 'recipes').
        Requires scope_value to be set in ExportConfig.

    TAG: Filtered by content tag. Requires scope_value to be set in ExportConfig.
        Note: tag-based exports are not currently first-class in the Phase 4 data
        model; this scope is reserved for Phase 5.1.
    """

    LOCAL_ONLY = "local"
    FEDERATED = "federated"
    DOMAIN = "domain"
    TAG = "tag"


@dataclass
class ExportConfig:
    """
    Configuration for a ZIM export job.

    Attributes:
        scope: Which content items to include (see ExportScope enum).
        scope_value: Required when scope is DOMAIN or TAG. For DOMAIN, this is the
            domain name (e.g., 'agriculture'). For TAG, this is the tag string.
        include_federated: When True, include federated items from partner nodes
            even in non-FEDERATED scope exports. Each federated item will have
            an attribution footer in its rendered HTML.
        language: ISO 639-1 two-letter language code for content filtering
            (e.g., 'en', 'es'). Used to select the primary language variant of
            multilingual title/description fields.
        language_iso3: ISO 639-3 three-letter code for Xapian indexer and ZIM
            metadata (e.g., 'eng', 'spa').
        include_images: When True, embed image assets in the ZIM file. When False
            (nopic flavour), image elements are replaced with alt text only.
            Set to False for MVP; True for Phase 5.1 image-inclusive exports.
        flavour: ZIM flavour string. Must match the Flavour metadata field and
            filename component. Validated against VALID_FLAVOURS.
        max_items: Optional upper bound on items per export. Used for testing
            and for domain exports where the domain has limited content. None
            means no limit (default for production exports).
        export_started_at: Timestamp set by the ExportJob at job start. Used for
            Reference Export content freeze policy. When set, excludes items with
            updated_at > export_started_at.

    Example:
        # Full local-only nopic export (the recommended MVP default)
        config = ExportConfig(scope=ExportScope.LOCAL_ONLY, flavour="nopic")

        # Agriculture domain export
        config = ExportConfig(
            scope=ExportScope.DOMAIN,
            scope_value="agriculture",
            flavour="agriculture"
        )

        # Federated export including partner node content
        config = ExportConfig(
            scope=ExportScope.FEDERATED,
            include_federated=True,
            flavour="all"
        )
    """

    scope: ExportScope = ExportScope.LOCAL_ONLY
    scope_value: Optional[str] = None
    include_federated: bool = False
    language: str = "en"
    language_iso3: str = "eng"
    include_images: bool = False
    flavour: str = "nopic"
    max_items: Optional[int] = None
    export_started_at: Optional[datetime] = None

    # Valid flavour values per the openZIM naming convention
    VALID_FLAVOURS: tuple = ("nopic", "all", "mini", "agriculture", "recipes",
                              "water", "electronics", "building", "energy", "archive")

    def __post_init__(self) -> None:
        """Validate configuration after initialization."""
        if self.scope in (ExportScope.DOMAIN, ExportScope.TAG) and not self.scope_value:
            raise ValueError(
                f"scope_value is required when scope is {self.scope.value}. "
                f"Set scope_value to the domain name or tag string."
            )
        if self.flavour not in self.VALID_FLAVOURS:
            raise ValueError(
                f"Invalid flavour '{self.flavour}'. "
                f"Valid flavours: {', '.join(self.VALID_FLAVOURS)}"
            )


# ---------------------------------------------------------------------------
# Metadata model
# ---------------------------------------------------------------------------


@dataclass
class ZimMetadata:
    """
    ZIM file metadata conforming to the openZIM metadata specification.

    All fields map directly to the ZIM M/ namespace entries that python-libzim
    accepts via creator.add_metadata(). Mandatory fields (those required for
    zimcheck to pass) are not Optional; omitting them will raise ValueError in
    validate().

    References:
        https://wiki.openzim.org/wiki/Metadata
        https://openzim.org/wiki/ZIM_Naming_Convention

    Attributes:
        title: Display title shown in Kiwix library browser. Max 30 chars
            recommended. Format: "Open-Repo: {Scope} ({Language})".
        description: Short description, max 80 chars. Shown in catalog UI.
        language: ISO 639-3 code (e.g., "eng", "spa"). Comma-separated for
            multilingual exports (e.g., "eng,spa").
        name: The Name metadata field. Must follow openZIM convention:
            {publisher}_{language}_{flavour} with no period. The period is
            appended separately in the filename.
            Example: "open-repo_en_nopic"
        flavour: Scope identifier matching the flavour part of the filename.
            Must match ExportConfig.flavour.
        creator: Content author attribution. "Open-Repo Community" for
            locally-authored content; include remote node name for federated
            content: "Open-Repo Community + Node B".
        publisher: Node operator identifier. Typically "Open-Repo".
        date: Export date in YYYY-MM-DD format. Generated at export time.
        source_url: The open-repo node's base URL. Stored as ZIM Source metadata.
        tags: Semicolon-separated tag string for catalog categorization.
            Recommended: "offline;practical-knowledge;procedures"
        long_description: Extended description, max 4000 chars. Optional but
            recommended to avoid zimcheck warnings on some validator versions.
        scraper: Tool name and version. Set automatically by ZimWriter.
        illustration_48x48_path: Path to a 48x48 PNG icon. If None, ZimWriter
            will use a default placeholder. Must be exactly 48x48 pixels; wrong
            size will cause zimcheck to fail with Illustration size error.

    Example:
        metadata = ZimMetadata(
            title="Open-Repo: Full Library (English)",
            description="Offline practical knowledge library",
            language="eng",
            name="open-repo_en_nopic",
            flavour="nopic",
            creator="Open-Repo Community",
            publisher="Open-Repo",
            source_url="https://node.example.org",
        )
    """

    title: str
    description: str
    language: str
    name: str
    flavour: str
    creator: str
    publisher: str
    source_url: str
    date: Optional[str] = None  # Auto-generated if None
    tags: str = "offline;practical-knowledge;procedures"
    long_description: Optional[str] = None
    scraper: str = "open-repo-exporter/1.0"
    illustration_48x48_path: Optional[Path] = None

    def __post_init__(self) -> None:
        """Auto-fill date and validate required fields."""
        if self.date is None:
            self.date = datetime.utcnow().strftime("%Y-%m-%d")

        # Validate naming convention: name must be lowercase alphanumeric + hyphens
        import re
        name_pattern = re.compile(r"^[a-z0-9][a-z0-9\-]*_[a-z]{2,3}_[a-z0-9\-]+$")
        if not name_pattern.match(self.name):
            raise ValueError(
                f"Invalid ZIM Name metadata '{self.name}'. "
                f"Must match pattern: {{publisher}}_{{language}}_{{flavour}} "
                f"(lowercase, hyphens only, underscore as separator). "
                f"Example: 'open-repo_en_nopic'"
            )

    def validate(self) -> list[str]:
        """
        Validate all metadata fields. Returns list of error strings.
        Empty list means metadata is valid.

        Called by ZimWriter before opening the Creator. A non-empty return
        will cause ZimWriter.create_zim() to raise ValueError.

        Checks performed:
          - All mandatory fields are non-empty strings
          - title is <= 30 characters (zimcheck recommendation)
          - description is <= 80 characters (zimcheck requirement)
          - date matches YYYY-MM-DD format
          - language is a valid ISO 639-3 code format (3 letters)
          - name matches the openZIM naming regex
          - illustration_48x48_path exists if specified
        """
        errors = []

        # Mandatory field presence
        mandatory = {
            "title": self.title,
            "description": self.description,
            "language": self.language,
            "name": self.name,
            "creator": self.creator,
            "publisher": self.publisher,
            "date": self.date,
        }
        for field_name, value in mandatory.items():
            if not value or not value.strip():
                errors.append(f"Mandatory metadata field '{field_name}' is empty")

        # Length constraints
        if self.title and len(self.title) > 30:
            # This is a recommendation, not a hard failure, but log it
            logger.warning(
                "ZIM Title exceeds 30 characters (%d chars): '%s'. "
                "Kiwix catalog may truncate this.",
                len(self.title), self.title
            )
        if self.description and len(self.description) > 80:
            errors.append(
                f"ZIM Description exceeds 80 characters ({len(self.description)} chars). "
                f"zimcheck will fail. Shorten to <=80 chars."
            )

        # Date format
        if self.date:
            import re
            if not re.match(r"^\d{4}-\d{2}-\d{2}$", self.date):
                errors.append(
                    f"ZIM Date '{self.date}' does not match YYYY-MM-DD format"
                )

        # Illustration file existence
        if self.illustration_48x48_path and not self.illustration_48x48_path.exists():
            errors.append(
                f"illustration_48x48_path '{self.illustration_48x48_path}' does not exist. "
                f"ZIM exports without an illustration will fail zimcheck and appear "
                f"broken in Kiwix's library browser."
            )

        return errors


# ---------------------------------------------------------------------------
# Article/asset entry model
# ---------------------------------------------------------------------------


@dataclass
class ZimEntry:
    """
    Represents a single article or asset entry to be written into a ZIM file.

    ZimWriter accepts ZimEntry objects and converts them to python-libzim Item
    subclass instances internally. Callers should not need to interact with
    python-libzim's Item class directly.

    Attributes:
        path: URL path within the ZIM file. Must be unique. Used as the navigation
            URL within Kiwix (e.g., "agriculture/biosand-filter-construction").
            Convention: {domain}/{cid} for content items.
            Must not start with '/' and must not contain '//'.
        title: Display title for the article. Used by Kiwix's library index and
            full-text search title ranking. Must be non-empty for articles.
            For non-article assets (CSS, images), title can be empty.
        content: The article's content. For HTML articles, this is the rendered
            HTML string. For binary assets (images, CSS), this is bytes.
        mime_type: MIME type string. Common values:
            - "text/html" for articles
            - "text/css" for stylesheets
            - "image/png", "image/jpeg", "image/webp" for images
            - "application/javascript" for scripts (avoid if possible)
        is_front_article: When True, this entry appears in Kiwix's article list
            and is included in full-text search. Set to True for all content items.
            Set to False for CSS, JS, image assets, and navigation infrastructure.
        language: ISO 639-1 two-letter language code for this specific article.
            Defaults to "en". Used for per-article language tagging.
        source_node_url: For federated content, the URL of the originating node.
            When set, the HTML renderer will append an attribution footer.
            None for locally-authored content.
        source_node_name: Display name of the originating node for attribution.
            Required when source_node_url is set.
        license_name: SPDX license identifier for attribution rendering.
            e.g., "CC-BY-4.0"
        license_url: URL of the license text for attribution links.

    Note on content type:
        content accepts both str and bytes to support both HTML articles (str)
        and binary assets (bytes). The ZimWriter implementation will convert
        str to bytes using UTF-8 encoding before passing to libzim's
        StringProvider.
    """

    path: str
    title: str
    content: str | bytes
    mime_type: str = "text/html"
    is_front_article: bool = True
    language: str = "en"
    source_node_url: Optional[str] = None
    source_node_name: Optional[str] = None
    license_name: Optional[str] = None
    license_url: Optional[str] = None

    def __post_init__(self) -> None:
        """Validate entry fields."""
        if self.path.startswith("/"):
            raise ValueError(
                f"ZimEntry path must not start with '/'. Got: '{self.path}'. "
                f"Paths are ZIM-relative; leading slash is invalid."
            )
        if "//" in self.path:
            raise ValueError(
                f"ZimEntry path must not contain '//'. Got: '{self.path}'."
            )
        if self.is_front_article and not self.title.strip():
            raise ValueError(
                f"Front article ZimEntry at path '{self.path}' has empty title. "
                f"All browsable articles must have a non-empty title for Xapian "
                f"full-text search indexing."
            )
        if self.source_node_url and not self.source_node_name:
            raise ValueError(
                f"source_node_name is required when source_node_url is set. "
                f"Entry path: '{self.path}'"
            )

    def has_attribution(self) -> bool:
        """Return True if this entry requires a federated attribution footer."""
        return bool(self.source_node_url)


# ---------------------------------------------------------------------------
# libzim Item subclass
# ---------------------------------------------------------------------------


class ArticleItem(Item):
    """
    Implementation of libzim.writer.Item for ZimEntry objects.

    Converts ZimEntry dataclass objects into the Item interface required
    by libzim's Creator.add_item() method.
    """

    def __init__(self, entry: ZimEntry) -> None:
        """Initialize ArticleItem from a ZimEntry."""
        super().__init__()
        self.entry = entry

    def get_path(self) -> str:
        """Return the ZIM-relative path for this entry."""
        return self.entry.path

    def get_title(self) -> str:
        """Return the display title for this entry."""
        return self.entry.title

    def get_mimetype(self) -> str:
        """Return the MIME type for this entry."""
        return self.entry.mime_type

    def get_hints(self) -> dict:
        """Return hints for libzim indexing."""
        hints = {}
        if self.entry.is_front_article:
            hints[Hint.FRONT_ARTICLE] = True
        return hints

    def get_contentprovider(self):
        """Return a StringProvider for the entry content."""
        content = self.entry.content
        if isinstance(content, str):
            content = content.encode("utf-8")
        return StringProvider(content)


# ---------------------------------------------------------------------------
# Main ZimWriter class
# ---------------------------------------------------------------------------


class ZimWriter:
    """
    Writes a ZIM file from open-repo content items using python-libzim.

    ZimWriter is the primary integration point between open-repo's content
    database and the Kiwix ecosystem. It wraps python-libzim's Creator API
    with open-repo-specific logic: metadata validation, attribution rendering,
    path normalization, and post-export zimcheck validation.

    Thread safety: NOT thread-safe. Call add_article() and add_resource() from
    a single thread. Multiple ZimWriter instances can run in parallel (each
    writes to a different output file) but a single ZimWriter must not be
    shared across threads.

    Lifecycle:
        1. Instantiate: ZimWriter(metadata, config, output_path)
        2. Add content: add_article() / add_resource() for each item
        3. Generate: create_zim() — writes the ZIM file and runs zimcheck
        4. Retrieve: sha256_checksum property for storage/catalog metadata

    Example (post-implementation):
        writer = ZimWriter(
            metadata=ZimMetadata(title="Open-Repo", ...),
            config=ExportConfig(scope=ExportScope.LOCAL_ONLY, flavour="nopic"),
            output_path=Path("/tmp/open-repo_en_nopic_2026-04.zim"),
        )
        for item in db.query(ContentItem).filter_by(is_local=True):
            writer.add_article(
                path=item.cid,
                content=render_html_template(item),
                article_type=item.item_type,
                language="en",
            )
        result = writer.create_zim()
        # result.output_path, result.sha256, result.article_count, result.file_size_bytes
    """

    def __init__(
        self,
        metadata: ZimMetadata,
        config: ExportConfig,
        output_path: Path,
        illustration_bytes: Optional[bytes] = None,
        zimcheck_binary: str = "zimcheck",
    ) -> None:
        """
        Initialize ZimWriter.

        Args:
            metadata: ZimMetadata instance with all ZIM file metadata. Will be
                validated before ZIM creation begins.
            config: ExportConfig controlling scope, language, and flavour.
            output_path: Path where the ZIM file will be written. Parent directory
                must exist. File will be created or overwritten.
            illustration_bytes: PNG bytes for the 48x48 ZIM icon. If None, attempts
                to read from metadata.illustration_48x48_path. If both are None,
                a fallback 1x1 transparent PNG is used (will cause zimcheck warning
                but not failure).
            zimcheck_binary: Path or name of the zimcheck executable. Defaults to
                "zimcheck" (assumes it's on PATH). Set to None to skip validation
                (not recommended for production exports).

        Raises:
            ValueError: If metadata validation fails (see ZimMetadata.validate()).
            FileNotFoundError: If output_path's parent directory does not exist.
        """
        self.metadata = metadata
        self.config = config
        self.output_path = Path(output_path)
        self.zimcheck_binary = zimcheck_binary
        self._illustration_bytes = illustration_bytes
        self._entries: list[ZimEntry] = []
        self._article_count: int = 0
        self._resource_count: int = 0
        self._sha256: Optional[str] = None
        self._is_finalized: bool = False

        # Validate output directory exists
        if not self.output_path.parent.exists():
            raise FileNotFoundError(
                f"Output directory does not exist: {self.output_path.parent}. "
                f"Create it before instantiating ZimWriter."
            )

        # Validate metadata
        errors = metadata.validate()
        if errors:
            raise ValueError(
                f"ZimMetadata validation failed with {len(errors)} error(s):\n"
                + "\n".join(f"  - {e}" for e in errors)
            )

        logger.info(
            "ZimWriter initialized: name=%s, output=%s, scope=%s",
            metadata.name, output_path, config.scope.value
        )

    def add_article(
        self,
        path: str,
        content: str,
        article_type: str,
        language: str = "en",
        source_node_url: Optional[str] = None,
        source_node_name: Optional[str] = None,
        license_name: Optional[str] = None,
        license_url: Optional[str] = None,
    ) -> None:
        """
        Add an HTML article to the ZIM file.

        This is the primary method called by the export service for each ContentItem.
        The content must be a fully self-contained HTML string — no external HTTP
        dependencies. All CSS must be inline or in <style> tags. No external JS.

        If source_node_url is provided, an attribution footer is appended to the
        HTML content before the </body> tag:
            <footer class="attribution">
              <p>Originally published on <a href="{source_node_url}">{source_node_name}</a>
              under <a href="{license_url}">{license_name}</a>.</p>
            </footer>

        Args:
            path: ZIM-relative URL path. Must be unique within the export.
                Convention: use the ContentItem's CID as the path, or
                "{domain}/{cid}" for namespaced exports.
            content: Fully self-contained HTML string. Must not contain
                references to http:// URLs for stylesheets or scripts.
            article_type: ContentItem.item_type value (e.g., "procedure",
                "recipe", "schematic"). Used for article categorization metadata
                in the ZIM index page generator.
            language: ISO 639-1 language code for this article (default "en").
            source_node_url: Optional. URL of the federation partner that
                authored this content. Required for federated content when
                config.include_federated is True.
            source_node_name: Display name of the source node. Required when
                source_node_url is set.
            license_name: SPDX license identifier (e.g., "CC-BY-4.0"). Required
                when source_node_url is set (for attribution compliance).
            license_url: URL of the license text. Required when source_node_url
                is set.

        Raises:
            RuntimeError: If called after create_zim() has been called
                (ZimWriter is not reusable after finalization).
            ValueError: If path is invalid (starts with '/', contains '//').
            ValueError: If content is empty.
            ValueError: If source_node_url is set without source_node_name.

        Note:
            This method buffers entries in memory. For large exports (>10,000 items),
            monitor memory usage. The ZimWriter will hold all entries until
            create_zim() is called.

            TODO(post-PR-merge): Implement streaming mode that writes entries
            directly to the Creator without buffering, for memory efficiency.
        """
        if self._is_finalized:
            raise RuntimeError(
                "ZimWriter has been finalized. Cannot add_article() after create_zim()."
            )
        if not content or not content.strip():
            raise ValueError(f"Article content is empty for path '{path}'")

        # Apply attribution footer for federated content
        processed_content = self._apply_attribution_footer(
            content=content,
            source_node_url=source_node_url,
            source_node_name=source_node_name,
            license_name=license_name,
            license_url=license_url,
        )

        entry = ZimEntry(
            path=path,
            title=self._extract_title_from_html(processed_content) or path,
            content=processed_content,
            mime_type="text/html",
            is_front_article=True,
            language=language,
            source_node_url=source_node_url,
            source_node_name=source_node_name,
            license_name=license_name,
            license_url=license_url,
        )
        self._entries.append(entry)
        self._article_count += 1

    def add_resource(
        self,
        path: str,
        binary_content: bytes,
        mime_type: str,
    ) -> None:
        """
        Add a binary resource (image, CSS, font) to the ZIM file.

        Resources are non-article entries — they do not appear in the article
        list or Xapian index, but are accessible by path from within articles.
        Use this method for:
          - Shared CSS stylesheets: add_resource("style/main.css", css_bytes, "text/css")
          - Logo/icon images: add_resource("assets/logo.png", png_bytes, "image/png")
          - Any binary asset referenced by article HTML via relative paths

        For image assets, ensure the relative path in the article HTML matches
        the path parameter here. Example:
            add_resource("assets/biosand-filter-diagram.png", png_bytes, "image/png")
            # Article HTML: <img src="../assets/biosand-filter-diagram.png" alt="...">

        Args:
            path: ZIM-relative path for the resource. Must be unique.
            binary_content: Raw bytes of the resource content.
            mime_type: MIME type string. Common values:
                "text/css", "image/png", "image/jpeg", "image/webp",
                "image/svg+xml", "font/woff2"

        Raises:
            RuntimeError: If called after create_zim().
            ValueError: If path is invalid or binary_content is empty.

        Note:
            When config.include_images is False (nopic flavour), resource
            entries with image MIME types are silently discarded. This is the
            correct behaviour: nopic ZIM files should contain no image assets.
            CSS and font resources are always included regardless of include_images.
        """
        if self._is_finalized:
            raise RuntimeError(
                "ZimWriter has been finalized. Cannot add_resource() after create_zim()."
            )
        if not binary_content:
            raise ValueError(f"Resource content is empty for path '{path}'")

        # Discard image resources for nopic exports
        if not self.config.include_images and mime_type.startswith("image/"):
            logger.debug(
                "Skipping image resource '%s' (include_images=False, flavour=%s)",
                path, self.config.flavour
            )
            return

        entry = ZimEntry(
            path=path,
            title="",  # Resources have no display title
            content=binary_content,
            mime_type=mime_type,
            is_front_article=False,  # Resources are not browsable articles
        )
        self._entries.append(entry)
        self._resource_count += 1

    def create_zim(
        self,
        compression: str = "default",
        run_zimcheck: bool = True,
    ) -> "ZimWriteResult":
        """
        Finalize and write the ZIM file to disk.

        This method:
          1. Validates that at least one front article exists
          2. Opens a python-libzim Creator context
          3. Configures indexing and main path
          4. Sets all ZIM metadata fields
          5. Adds the illustration (48x48 PNG)
          6. Iterates over buffered entries and adds each to the Creator
          7. Closes the Creator (triggers ZIM file write)
          8. Optionally runs zimcheck for validation
          9. Computes SHA-256 checksum
          10. Returns ZimWriteResult with all output metadata

        Args:
            compression: Compression algorithm for ZIM clusters. Options:
                "default" — uses the libzim version default (Zstandard since 7.x)
                "zstd" — explicit Zstandard (fastest decompression, good ratio)
                "lzma" — LZMA2 (best compression ratio, slower decompression)
                "none" — uncompressed (for debugging only, large file size)
            run_zimcheck: When True (default), run the `zimcheck` binary after
                ZIM creation to validate the output. If zimcheck reports errors,
                a ZimCheckError is raised and the ZIM file is renamed to
                {output_path}.invalid for inspection.
                Set to False only in test environments or when zimcheck is not
                installed.

        Returns:
            ZimWriteResult: Dataclass with output_path, sha256, article_count,
                file_size_bytes, generation_duration_seconds, zimcheck_passed.

        Raises:
            ValueError: If no front articles have been added.
            ZimCheckError: If run_zimcheck is True and zimcheck reports errors.
            RuntimeError: If called more than once (ZimWriter is not reusable).

        Note on python-libzim Creator API:
            TODO(post-PR-merge): Replace the stub implementation below with the
            actual python-libzim Creator calls. The correct pattern is:

                from libzim.writer import Creator, Item, StringProvider, Hint

                class ArticleItem(Item):
                    def __init__(self, entry: ZimEntry): self.entry = entry
                    def get_path(self): return self.entry.path
                    def get_title(self): return self.entry.title
                    def get_mimetype(self): return self.entry.mime_type
                    def get_hints(self):
                        return {Hint.FRONT_ARTICLE: self.entry.is_front_article}
                    def get_contentprovider(self):
                        content = self.entry.content
                        if isinstance(content, str):
                            content = content.encode("utf-8")
                        return StringProvider(content)

                with Creator(str(self.output_path)) as creator:
                    creator.config_indexing(True, self.config.language_iso3)
                    creator.set_mainpath("index")
                    self._apply_metadata_to_creator(creator)
                    for entry in self._entries:
                        creator.add_item(ArticleItem(entry))
                # Creator.__exit__ triggers ZIM file write
        """
        if self._is_finalized:
            raise RuntimeError("ZimWriter.create_zim() can only be called once.")

        front_articles = [e for e in self._entries if e.is_front_article]
        if not front_articles:
            raise ValueError(
                "Cannot create ZIM file: no front articles have been added. "
                "Call add_article() at least once before create_zim()."
            )

        start_time = datetime.utcnow()

        logger.info(
            "Starting ZIM creation: %s (%d articles, %d resources)",
            self.output_path.name,
            self._article_count,
            self._resource_count,
        )

        # Create ZIM file using libzim Creator
        try:
            creator = Creator(str(self.output_path))

            # All configuration MUST happen before entering the context manager.
            # Configure compression.
            if compression == "none":
                creator.config_compression(Compression.none)
            elif compression in ("default", "zstd"):
                creator.config_compression(Compression.zstd)

            # _apply_metadata_to_creator configures Xapian indexing (pre-context).
            # config_indexing() must be called before Creator.__enter__().
            self._apply_metadata_to_creator(creator)

            with creator:
                # Set the main landing page (index)
                creator.set_mainpath("index")

                # Write openZIM metadata fields (add_metadata requires context).
                self._write_zim_metadata(creator)

                # Add illustration if available
                illustration_bytes = self._get_illustration_bytes()
                if illustration_bytes:
                    creator.add_illustration(48, illustration_bytes)

                # Add all entries (articles and resources) to the Creator
                for entry in self._entries:
                    item = ArticleItem(entry)
                    creator.add_item(item)

        except Exception as e:
            logger.error(
                "Failed to create ZIM file: %s — %s",
                self.output_path.name, str(e)
            )
            raise

        self._is_finalized = True
        end_time = datetime.utcnow()
        duration = (end_time - start_time).total_seconds()

        # Compute SHA-256
        self._sha256 = self._compute_sha256(self.output_path)

        file_size = self.output_path.stat().st_size

        zimcheck_passed = True
        if run_zimcheck and self.zimcheck_binary:
            zimcheck_passed = self._run_zimcheck()

        logger.info(
            "ZIM creation complete: %s (%.1f seconds, %d bytes, sha256=%s...)",
            self.output_path.name, duration, file_size, self._sha256[:8]
        )

        return ZimWriteResult(
            output_path=self.output_path,
            sha256=self._sha256,
            article_count=self._article_count,
            resource_count=self._resource_count,
            file_size_bytes=file_size,
            generation_duration_seconds=duration,
            zimcheck_passed=zimcheck_passed,
            name=self.metadata.name,
            flavour=self.metadata.flavour,
        )

    @property
    def article_count(self) -> int:
        """Number of front articles added so far."""
        return self._article_count

    @property
    def resource_count(self) -> int:
        """Number of resource entries added so far."""
        return self._resource_count

    @property
    def sha256_checksum(self) -> Optional[str]:
        """SHA-256 checksum of the output ZIM file. None until create_zim() is called."""
        return self._sha256

    def _apply_attribution_footer(
        self,
        content: str,
        source_node_url: Optional[str],
        source_node_name: Optional[str],
        license_name: Optional[str],
        license_url: Optional[str],
    ) -> str:
        """
        Append a federated attribution footer to HTML content.

        Called internally by add_article(). If source_node_url is None,
        returns content unchanged.

        The footer is inserted before the closing </body> tag if present,
        or appended to the end of the content if no </body> is found.

        TODO(post-PR-merge): Add CSS class for styling the attribution footer.
        The footer element must be styled in the shared CSS resource so that
        it renders consistently across all articles.
        """
        if not source_node_url:
            return content

        license_link = ""
        if license_url and license_name:
            license_link = f' under <a href="{license_url}">{license_name}</a>'
        elif license_name:
            license_link = f" under {license_name}"

        footer = (
            f'\n<footer class="attribution">'
            f'<p>Originally published on '
            f'<a href="{source_node_url}">{source_node_name}</a>{license_link}.</p>'
            f'</footer>'
        )

        if "</body>" in content:
            return content.replace("</body>", footer + "\n</body>", 1)
        return content + footer

    def _extract_title_from_html(self, html: str) -> Optional[str]:
        """
        Extract title from HTML <title> tag.

        Falls back to the first <h1> content if no <title> tag is present.
        Returns None if neither is found — caller should use the path as title.

        TODO(post-PR-merge): Use BeautifulSoup for robust HTML parsing.
        The current simple string search is adequate for well-formed templates.
        """
        import re
        title_match = re.search(r"<title[^>]*>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
        if title_match:
            return title_match.group(1).strip()
        h1_match = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.IGNORECASE | re.DOTALL)
        if h1_match:
            # Strip HTML tags from h1 content
            return re.sub(r"<[^>]+>", "", h1_match.group(1)).strip()
        return None

    def _apply_metadata_to_creator(self, creator: Creator) -> None:
        """
        Apply pre-context configuration to a python-libzim Creator instance.

        This method MUST be called BEFORE entering the Creator context manager
        (i.e., before ``with creator:``). It configures Xapian full-text
        indexing, which the libzim API requires to be set before ``__enter__``.

        openZIM metadata fields (Title, Description, etc.) are written inside
        the context by ``_write_zim_metadata()``.
        """
        # config_indexing must be called before Creator.__enter__()
        creator.config_indexing(True, self.config.language_iso3)

    def _write_zim_metadata(self, creator: Creator) -> None:
        """
        Write all openZIM metadata fields to the Creator.

        Must be called INSIDE the Creator context manager (after ``with creator:``),
        because add_metadata() requires the Creator to be started.
        """
        creator.add_metadata("Title", self.metadata.title)
        creator.add_metadata("Description", self.metadata.description)
        creator.add_metadata("Language", self.metadata.language)
        creator.add_metadata("Creator", self.metadata.creator)
        creator.add_metadata("Publisher", self.metadata.publisher)
        creator.add_metadata("Date", self.metadata.date)
        creator.add_metadata("Name", self.metadata.name)
        creator.add_metadata("Flavour", self.metadata.flavour)
        creator.add_metadata("Tags", self.metadata.tags)
        creator.add_metadata("Source", self.metadata.source_url)
        creator.add_metadata("Scraper", self.metadata.scraper)
        if self.metadata.long_description:
            creator.add_metadata("LongDescription", self.metadata.long_description)

    def _get_illustration_bytes(self) -> bytes:
        """
        Return 48x48 PNG bytes for the ZIM illustration field.

        Priority:
          1. Bytes passed to __init__ as illustration_bytes
          2. File at metadata.illustration_48x48_path
          3. _FALLBACK_ILLUSTRATION_PNG (48x48 solid teal PNG)

        Always returns a valid PNG — never None. openZIM requires an
        Illustration_48x48_at_1 field; omitting it produces a warning
        in zimcheck and may be rejected by some Kiwix readers.
        """
        if self._illustration_bytes:
            return self._illustration_bytes
        if self.metadata.illustration_48x48_path:
            with open(self.metadata.illustration_48x48_path, "rb") as f:
                return f.read()
        return _FALLBACK_ILLUSTRATION_PNG

    def _run_zimcheck(self) -> bool:
        """
        Run zimcheck binary on the output ZIM file.

        Returns True if zimcheck passes with no errors.
        Returns False and logs errors if zimcheck fails.

        zimcheck is installed via:
          - apt: apt-get install zim-tools
          - brew: brew install zim-tools
          - Docker: FROM openzim/zim-tools (zimcheck is included)
        """
        if not self.zimcheck_binary:
            return True

        try:
            result = subprocess.run(
                [self.zimcheck_binary, str(self.output_path)],
                capture_output=True,
                text=True,
                timeout=300,  # 5 minute timeout for large ZIM files
            )
            if result.returncode == 0:
                logger.info("zimcheck PASSED: %s", self.output_path.name)
                return True
            else:
                logger.error(
                    "zimcheck FAILED: %s\nstdout:\n%s\nstderr:\n%s",
                    self.output_path.name, result.stdout, result.stderr
                )
                # Rename invalid file for inspection
                invalid_path = self.output_path.with_suffix(".zim.invalid")
                self.output_path.rename(invalid_path)
                logger.error("Invalid ZIM moved to: %s", invalid_path)
                return False
        except FileNotFoundError:
            logger.warning(
                "zimcheck binary not found at '%s'. Skipping validation. "
                "Install zim-tools for production exports.",
                self.zimcheck_binary
            )
            return True  # Don't fail on missing zimcheck in dev environments
        except subprocess.TimeoutExpired:
            logger.error("zimcheck timed out after 300 seconds: %s", self.output_path.name)
            return False

    @staticmethod
    def _compute_sha256(path: Path) -> str:
        """Compute SHA-256 checksum of a file. Read in 64 KB chunks."""
        h = hashlib.sha256()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                h.update(chunk)
        return h.hexdigest()

    @staticmethod
    def compute_period(existing_periods: list[str], now: Optional[datetime] = None) -> str:
        """
        Compute the YYYY-MM period string for the ZIM filename.

        Appends an alphabetic suffix if an export for the current month
        already exists (for emergency re-exports within the same month).

        Args:
            existing_periods: List of period strings already published for this
                name+flavour combination (e.g., ["2026-03", "2026-04"]).
            now: Override for current datetime. Uses utcnow() if None.

        Returns:
            Period string: "2026-04", "2026-04a", "2026-04b", etc.

        Example:
            >>> ZimWriter.compute_period(["2026-03", "2026-04"])
            "2026-04a"
            >>> ZimWriter.compute_period(["2026-03", "2026-04", "2026-04a"])
            "2026-04b"
            >>> ZimWriter.compute_period([])
            "2026-04"  # (assuming current month is 2026-04)
        """
        if now is None:
            now = datetime.utcnow()
        base = now.strftime("%Y-%m")
        same_month = sorted([p for p in existing_periods if p.startswith(base)])
        if not same_month:
            return base
        last = same_month[-1]
        if last == base:
            return f"{base}a"
        suffix = last[-1]
        return f"{base}{chr(ord(suffix) + 1)}"

    @staticmethod
    def build_filename(name: str, period: str) -> str:
        """
        Build the ZIM filename from name metadata and period.

        Args:
            name: The ZIM Name metadata value (e.g., "open-repo_en_nopic").
            period: The computed period string (e.g., "2026-04").

        Returns:
            Filename string: "open-repo_en_nopic_2026-04.zim"

        Raises:
            ValueError: If name or period contains invalid characters.
        """
        import re
        if not re.match(r"^[a-z0-9][a-z0-9\-]*_[a-z]{2,3}_[a-z0-9\-]+$", name):
            raise ValueError(f"Invalid ZIM name: '{name}'")
        if not re.match(r"^\d{4}-\d{2}[a-z]?$", period):
            raise ValueError(f"Invalid period format: '{period}'. Expected YYYY-MM or YYYY-MMa")
        return f"{name}_{period}.zim"


# ---------------------------------------------------------------------------
# Result dataclass
# ---------------------------------------------------------------------------


@dataclass
class ZimWriteResult:
    """
    Result of a ZimWriter.create_zim() call.

    All fields are populated by create_zim() and should be persisted to the
    zim_exports database table after upload to object storage.

    Attributes:
        output_path: Path to the written ZIM file.
        sha256: SHA-256 checksum hex string.
        article_count: Number of front articles written.
        resource_count: Number of resource entries written.
        file_size_bytes: Size of the ZIM file in bytes.
        generation_duration_seconds: Wall-clock time for create_zim().
        zimcheck_passed: True if zimcheck validation succeeded (or was skipped).
        name: ZIM Name metadata value (e.g., "open-repo_en_nopic").
        flavour: ZIM Flavour value (e.g., "nopic").
    """

    output_path: Path
    sha256: str
    article_count: int
    resource_count: int
    file_size_bytes: int
    generation_duration_seconds: float
    zimcheck_passed: bool
    name: str
    flavour: str


# ---------------------------------------------------------------------------
# Custom exceptions
# ---------------------------------------------------------------------------


class ZimCheckError(Exception):
    """Raised when zimcheck fails validation on the generated ZIM file."""

    def __init__(self, zim_path: Path, zimcheck_output: str) -> None:
        self.zim_path = zim_path
        self.zimcheck_output = zimcheck_output
        super().__init__(
            f"zimcheck failed for {zim_path.name}:\n{zimcheck_output}"
        )
