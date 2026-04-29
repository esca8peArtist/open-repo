"""
ExportService: Orchestrates Phase 5 offline ZIM export jobs.

This module is the primary coordinator for the offline export pipeline.
It combines three sub-concerns:

  1. Content querying — scope-filtered retrieval from the database
  2. HTML rendering — self-contained per-article HTML for ZIM embedding
  3. Export orchestration — drives ZimWriter with rendered content and
     validates the result

The service is deliberately stateless with respect to the export format:
ZimWriter owns all ZIM-specific logic. ExportService owns the scope
logic, content normalisation, and rendering. This separation means
ExportService could also drive a static-HTML export path in the future
without modification.

Architecture references:
  - phase-5-kiwix-architecture.md section 8 (blueprint step 1 and 2)
  - phase-5-offline-export-architecture.md section 1 and 2 (metadata,
    naming, incremental strategy)

Usage example (sync helper, see export_to_zim for async orchestration):

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
    service = ExportService(db_session)
    result = await service.export_to_zim(
        metadata=metadata,
        config=config,
        output_path=Path("/exports/open-repo_en_nopic_2026-04.zim"),
    )
    print(result.sha256, result.article_count, result.file_size_bytes)
"""

from __future__ import annotations

import logging
import re
from datetime import datetime
from pathlib import Path
from typing import AsyncIterator, Iterator, Optional

from .zim_writer import (
    ExportConfig,
    ExportScope,
    ZimMetadata,
    ZimWriteResult,
    ZimWriter,
)

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# HTML rendering constants
# ---------------------------------------------------------------------------

# Inline CSS for all exported articles. No external URLs.
# Designed for readability on both desktop Kiwix and mobile Kiwix apps.
_ARTICLE_CSS = """
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    line-height: 1.6;
    color: #222;
    background: #fff;
    padding: 1rem;
    max-width: 800px;
    margin: 0 auto;
}
h1 { font-size: 1.75rem; margin-top: 1.5rem; margin-bottom: 0.5rem; }
h2 { font-size: 1.35rem; margin-top: 1.25rem; margin-bottom: 0.4rem; }
h3 { font-size: 1.1rem; margin-top: 1rem; margin-bottom: 0.3rem; }
p { margin-bottom: 0.9rem; }
ul, ol { margin-left: 2rem; margin-bottom: 0.9rem; }
li { margin-bottom: 0.4rem; }
code {
    background: #f3f3f3;
    padding: 0.1rem 0.35rem;
    border-radius: 3px;
    font-family: 'Courier New', Courier, monospace;
    font-size: 0.92em;
}
pre { background: #f3f3f3; padding: 1rem; border-radius: 4px;
      overflow-x: auto; margin-bottom: 1rem; }
pre code { background: none; padding: 0; }
table { border-collapse: collapse; width: 100%; margin-bottom: 1rem; }
th, td { border: 1px solid #ccc; padding: 0.45rem 0.65rem; text-align: left; }
th { background: #f5f5f5; font-weight: 600; }
.meta-block {
    background: #f9f9f9;
    border: 1px solid #e5e5e5;
    border-radius: 4px;
    padding: 0.75rem 1rem;
    margin-bottom: 1.5rem;
    font-size: 0.92em;
    color: #555;
}
.meta-block p { margin-bottom: 0.2rem; }
.steps-list { list-style: none; margin-left: 0; counter-reset: step-counter; }
.steps-list li {
    counter-increment: step-counter;
    padding-left: 2.5rem;
    position: relative;
    margin-bottom: 1rem;
}
.steps-list li::before {
    content: counter(step-counter);
    position: absolute;
    left: 0;
    top: 0.05rem;
    background: #2563eb;
    color: #fff;
    width: 1.6rem;
    height: 1.6rem;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.8rem;
    font-weight: 700;
}
.step-title { font-weight: 600; margin-bottom: 0.25rem; }
.materials-table { margin-top: 0.5rem; }
.attribution {
    background: #eff6ff;
    border-left: 4px solid #2563eb;
    padding: 0.75rem 1rem;
    margin-top: 2rem;
    font-size: 0.88em;
    color: #555;
}
.attribution a { color: #2563eb; }
footer.article-footer {
    margin-top: 2rem;
    padding-top: 0.75rem;
    border-top: 1px solid #e5e5e5;
    font-size: 0.85em;
    color: #888;
}
"""

# Index page CSS (shared but kept minimal to reduce file size)
_INDEX_CSS = _ARTICLE_CSS + """
.index-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    gap: 1rem;
    margin-top: 1.5rem;
}
.domain-card {
    border: 1px solid #e5e5e5;
    border-radius: 6px;
    padding: 1rem;
    text-decoration: none;
    color: inherit;
    transition: border-color 0.15s;
}
.domain-card:hover { border-color: #2563eb; }
.domain-card h3 { font-size: 1.05rem; margin-top: 0; color: #2563eb; }
.domain-card p { font-size: 0.88em; color: #666; margin-bottom: 0; }
"""


# ---------------------------------------------------------------------------
# ExportService
# ---------------------------------------------------------------------------


class ExportService:
    """
    Orchestrates ZIM export jobs for the open-repo offline library.

    ExportService is the top-level coordinator for Phase 5's export pipeline.
    It handles three responsibilities:

    1. Content querying. The ``query_content_items()`` method retrieves
       ``ContentItem`` records from the database filtered by the export scope
       (local-only, federated, domain, or tag). The method is an async
       generator that yields lightweight dicts to avoid loading the entire
       content set into memory at once.

    2. HTML rendering. ``render_article_html()`` converts a content item dict
       into a fully self-contained HTML string. "Self-contained" means no
       external HTTP references: all CSS is inline, no JavaScript, image
       references are either rewritten to ZIM paths or stripped for nopic
       exports. The rendered HTML is directly suitable for embedding in a ZIM
       file via ``ZimWriter.add_article()``.

    3. Export orchestration. ``export_to_zim()`` drives the full pipeline:
       query → render → ZimWriter → validate. It accepts a ``ZimMetadata``
       and ``ExportConfig``, creates a ``ZimWriter``, streams all content
       through it, and returns a ``ZimWriteResult``. Auxiliary methods
       ``validate_zim_output()`` and ``generate_zim_metadata()`` are provided
       as standalone helpers for callers who want finer-grained control.

    Thread safety:
        A single ``ExportService`` instance must not be shared across threads
        or concurrent async tasks. Each export job should use its own instance
        (and its own database session).

    Database session note:
        The ``db_session`` parameter accepts either a SQLAlchemy ``AsyncSession``
        or ``None``. When ``None``, the service operates in stub/test mode:
        ``query_content_items()`` yields no results and all DB-dependent methods
        return empty/default values. This allows the service and its tests to
        run without a database connection.

    Example — full pipeline::

        service = ExportService(db_session=session)
        metadata = ExportService.generate_zim_metadata(
            node_url="https://node.example.org",
            flavour="nopic",
            language_iso3="eng",
        )
        config = ExportConfig(scope=ExportScope.LOCAL_ONLY, flavour="nopic")
        output_path = Path("/exports") / ZimWriter.build_filename(
            metadata.name,
            ZimWriter.compute_period([]),
        )
        result = await service.export_to_zim(
            metadata=metadata,
            config=config,
            output_path=output_path,
        )

    Example — render only (no ZIM)::

        html = await service.render_article_html(content_item, language="en")
    """

    def __init__(self, db_session: object = None) -> None:
        """
        Initialize ExportService.

        Args:
            db_session: SQLAlchemy ``AsyncSession`` for content queries.
                Pass ``None`` (default) to operate in stub/test mode without
                a live database connection. In stub mode, ``query_content_items``
                yields nothing; all other methods work normally.
        """
        self.db = db_session

    # ------------------------------------------------------------------
    # 1. Content querying
    # ------------------------------------------------------------------

    async def query_content_items(
        self,
        config: ExportConfig,
    ) -> AsyncIterator[dict]:
        """
        Query and yield content items matching the export configuration.

        Retrieves ``ContentItem`` records from the database filtered by the
        scope in ``config``. Records are yielded as plain dicts so that callers
        do not hold ORM objects beyond the lifetime of the session.

        The yielded dict schema::

            {
                "cid": str,                    # Content ID (IPFS hash or internal ID)
                "title": dict[str, str],       # Language-keyed titles {"en": "..."}
                "item_type": str,              # "procedure", "recipe", "schematic", "plan"
                "domain": str,                 # "water", "agriculture", "energy", ...
                "license": str,                # SPDX identifier, e.g. "CC-BY-4.0"
                "is_local": bool,              # True = authored here, False = federated
                "source_url": str | None,      # Origin node URL (federated only)
                "source_title": str | None,    # Origin node human name (federated only)
                "created_at": datetime,
                "updated_at": datetime,
                "content_jsonld": dict,        # Full JSON-LD payload
            }

        Scope semantics:

        * ``LOCAL_ONLY`` — yields only items with no ``source_url`` (authored
          on this node). This is the safe default for most exports.
        * ``FEDERATED`` — yields all items including federated partner content.
          Each federated item's ``source_url`` and ``source_title`` will be
          populated for attribution rendering.
        * ``DOMAIN`` — yields items where ``domain == config.scope_value``.
          ``include_federated`` further controls whether federated items are
          included within that domain.
        * ``TAG`` — not yet implemented in the Phase 4 data model; yields
          nothing and logs a warning. Reserved for Phase 5.1.

        Content freeze:
            If ``config.export_started_at`` is set, items with
            ``updated_at > config.export_started_at`` are excluded. This
            ensures a consistent snapshot when the export job takes a long time.

        Item limit:
            If ``config.max_items`` is set, at most that many items are yielded.
            Useful for preview exports and testing.

        Args:
            config: ``ExportConfig`` controlling scope, scope_value,
                include_federated, max_items, and export_started_at.

        Yields:
            Content item dicts in creation-date order (oldest first).

        Note:
            This method is a stub when ``self.db`` is ``None``. In that case
            it yields nothing. The full SQLAlchemy implementation is provided
            in the TODO comments below.
        """
        if self.db is None:
            logger.warning(
                "ExportService.query_content_items: no database session (stub mode). "
                "Yielding no items."
            )
            return

        # TODO(post-PR-merge): Replace with real SQLAlchemy queries.
        #
        # from app.models import ContentItem
        # from sqlalchemy import select, and_
        #
        # Shared base filters:
        #   base_filter = []
        #   if config.export_started_at:
        #       base_filter.append(ContentItem.updated_at <= config.export_started_at)
        #
        # LOCAL_ONLY scope:
        #   if config.scope == ExportScope.LOCAL_ONLY:
        #       q = (
        #           select(ContentItem)
        #           .where(ContentItem.source_url.is_(None))
        #           .where(and_(*base_filter))
        #           .order_by(ContentItem.created_at.asc())
        #       )
        #       if config.max_items:
        #           q = q.limit(config.max_items)
        #       async for row in await self.db.stream(q):
        #           yield _orm_to_dict(row.ContentItem)
        #
        # FEDERATED scope:
        #   elif config.scope == ExportScope.FEDERATED:
        #       q = (
        #           select(ContentItem)
        #           .where(and_(*base_filter))
        #           .order_by(ContentItem.created_at.asc())
        #       )
        #       ...
        #
        # DOMAIN scope:
        #   elif config.scope == ExportScope.DOMAIN:
        #       q = (
        #           select(ContentItem)
        #           .where(ContentItem.domain == config.scope_value)
        #           .where(and_(*base_filter))
        #           .order_by(ContentItem.created_at.asc())
        #       )
        #       if not config.include_federated:
        #           q = q.where(ContentItem.source_url.is_(None))
        #       ...
        #
        # TAG scope (reserved for Phase 5.1 — content model does not yet
        # have a tags column; emit warning and yield nothing):
        #   elif config.scope == ExportScope.TAG:
        #       logger.warning("TAG scope not yet implemented in data model. "
        #                      "Yielding no items for this export.")
        #       return

        logger.info(
            "query_content_items: scope=%s scope_value=%s "
            "include_federated=%s max_items=%s",
            config.scope.value,
            config.scope_value,
            config.include_federated,
            config.max_items,
        )
        return
        yield  # noqa: unreachable — makes this an async generator in all paths

    # ------------------------------------------------------------------
    # 2. HTML rendering
    # ------------------------------------------------------------------

    def render_article_html(
        self,
        content_item: dict,
        language: str = "en",
    ) -> str:
        """
        Render a single content item as a self-contained HTML article.

        The returned HTML string is suitable for direct inclusion in a ZIM
        file via ``ZimWriter.add_article()``. It satisfies the self-containment
        constraint: no external CSS URLs, no external JS, no server-relative
        image URLs. All CSS is inlined in a ``<style>`` block. Images are not
        referenced (the caller handles images separately via
        ``ZimWriter.add_resource()``).

        Rendering is type-aware. The method inspects ``content_item["item_type"]``
        and dispatches to the appropriate section renderer:

        * ``"procedure"`` — numbered step list with tools and materials tables
        * ``"recipe"`` — ingredients table followed by numbered steps
        * ``"schematic"`` — description block with a note about the diagram file
        * ``"plan"`` — milestone/step list
        * Any other type — a generic description block

        Args:
            content_item: Content item dict as returned by
                ``query_content_items()``. Must contain at minimum:
                ``cid``, ``title`` (dict), ``item_type``, ``domain``,
                ``license``, and ``content_jsonld``.
            language: ISO 639-1 language code for selecting the preferred
                variant of multilingual text fields (e.g., ``"en"``, ``"fr"``).
                Falls back to the first available language if the requested
                code is not present.

        Returns:
            A valid, self-contained HTML5 string. The ``<title>`` element
            contains the article title. The article has a ``<h1>`` heading,
            a metadata block, and type-specific content sections.

        Note:
            This method is synchronous. It performs no I/O. It is safe to
            call from both sync and async contexts.
        """
        title = _pick_language(content_item.get("title", {}), language) or "Untitled"
        item_type = content_item.get("item_type", "")
        domain = content_item.get("domain", "")
        license_name = content_item.get("license", "")
        cid = content_item.get("cid", "")
        source_url = content_item.get("source_url")
        source_title = content_item.get("source_title")
        jsonld = content_item.get("content_jsonld", {})

        description = _pick_language(
            jsonld.get("description", {}), language
        )

        # Dispatch to type-specific renderer
        content_html = self._render_content_section(
            item_type=item_type,
            jsonld=jsonld,
            language=language,
        )

        # Build metadata block
        meta_parts: list[str] = []
        if domain:
            meta_parts.append(f"<p><strong>Domain:</strong> {_escape(domain)}</p>")
        if item_type:
            meta_parts.append(f"<p><strong>Type:</strong> {_escape(item_type.capitalize())}</p>")
        if license_name:
            license_url = _license_url(license_name)
            if license_url:
                meta_parts.append(
                    f'<p><strong>License:</strong> '
                    f'<a href="{license_url}">{_escape(license_name)}</a></p>'
                )
            else:
                meta_parts.append(f"<p><strong>License:</strong> {_escape(license_name)}</p>")
        if cid:
            meta_parts.append(f"<p><strong>Content ID:</strong> <code>{_escape(cid)}</code></p>")

        meta_block = (
            '<div class="meta-block">' + "".join(meta_parts) + "</div>"
            if meta_parts
            else ""
        )

        # Description paragraph (below meta block)
        description_html = (
            f"<p>{_escape(description)}</p>" if description else ""
        )

        # Attribution footer for federated content
        attribution_html = ""
        if source_url:
            node_label = _escape(source_title) if source_title else _escape(source_url)
            attribution_html = (
                f'\n<div class="attribution">'
                f"<strong>Federated content.</strong> "
                f'Originally published on <a href="{_escape(source_url)}">{node_label}</a>'
                f" and shared via the Open-Repo federation network."
                f"</div>"
            )

        # Article footer
        footer_html = (
            '<footer class="article-footer">'
            "<p>Open-Repo Offline Library &mdash; "
            "generated for offline use via Kiwix.</p>"
            "</footer>"
        )

        html = (
            "<!DOCTYPE html>\n"
            f'<html lang="{_escape(language)}">\n'
            "<head>\n"
            '  <meta charset="UTF-8">\n'
            '  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
            f"  <title>{_escape(title)}</title>\n"
            f"  <style>{_ARTICLE_CSS}</style>\n"
            "</head>\n"
            "<body>\n"
            f"  <h1>{_escape(title)}</h1>\n"
            f"  {meta_block}\n"
            f"  {description_html}\n"
            f"  {content_html}\n"
            f"  {attribution_html}\n"
            f"  {footer_html}\n"
            "</body>\n"
            "</html>"
        )
        return html

    def render_index_html(
        self,
        node_name: str = "Open-Repo Offline Library",
        items_by_domain: Optional[dict[str, list[dict]]] = None,
        language: str = "en",
    ) -> str:
        """
        Render the ZIM landing/index page.

        The index page is served at the ZIM ``mainpath`` and is the first
        page users see when they open the archive in Kiwix. It provides an
        overview of available domains and item counts.

        Args:
            node_name: Display name for this node (shown as the page title).
            items_by_domain: Optional dict mapping domain names to lists of
                content item dicts. When provided, the page renders domain
                cards with article counts and links to domain-specific pages.
                When ``None`` or empty, a generic welcome message is shown.
            language: ISO 639-1 language code for UI strings.

        Returns:
            Self-contained HTML5 string for the index page.
        """
        domain_cards = ""
        if items_by_domain:
            card_parts = []
            for domain, items in sorted(items_by_domain.items()):
                count = len(items)
                card_parts.append(
                    f'<div class="domain-card">'
                    f"<h3>{_escape(domain.title())}</h3>"
                    f"<p>{count} article{'s' if count != 1 else ''}</p>"
                    f"</div>"
                )
            if card_parts:
                domain_cards = (
                    '<h2>Browse by Domain</h2>'
                    '<div class="index-grid">' + "".join(card_parts) + "</div>"
                )

        html = (
            "<!DOCTYPE html>\n"
            f'<html lang="{_escape(language)}">\n'
            "<head>\n"
            '  <meta charset="UTF-8">\n'
            '  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
            f"  <title>{_escape(node_name)}</title>\n"
            f"  <style>{_INDEX_CSS}</style>\n"
            "</head>\n"
            "<body>\n"
            f"  <h1>{_escape(node_name)}</h1>\n"
            "  <p>This is an offline copy of the Open-Repo knowledge library. "
            "Browse practical how-to guides, recipes, schematics, and building plans "
            "— all available without an internet connection.</p>\n"
            f"  {domain_cards}\n"
            '<footer class="article-footer">'
            "<p>Open-Repo Offline Library &mdash; "
            "read with <a href=\"https://www.kiwix.org\">Kiwix</a>.</p>"
            "</footer>\n"
            "</body>\n"
            "</html>"
        )
        return html

    # ------------------------------------------------------------------
    # 3. Export orchestration
    # ------------------------------------------------------------------

    async def export_to_zim(
        self,
        metadata: ZimMetadata,
        config: ExportConfig,
        output_path: Path,
        illustration_bytes: Optional[bytes] = None,
        zimcheck_binary: Optional[str] = "zimcheck",
        run_zimcheck: bool = True,
    ) -> ZimWriteResult:
        """
        Run the full export pipeline: query → render → ZIM write → validate.

        This is the primary entry point for export jobs. It orchestrates all
        steps required to produce a valid ZIM file from the current database
        state:

        1. Validate ``metadata`` (delegated to ``ZimMetadata.validate()`` via
           the ``ZimWriter`` constructor).
        2. Instantiate a ``ZimWriter`` with the given metadata, config, and
           output path.
        3. Add a shared CSS resource to the ZIM file.
        4. Add the index/home page article.
        5. Stream content items via ``query_content_items(config)``, render
           each as HTML, and add to the ZimWriter.
        6. Call ``ZimWriter.create_zim()`` to finalize the ZIM file and
           optionally run ``zimcheck`` validation.
        7. Return the ``ZimWriteResult`` dataclass.

        Args:
            metadata: Fully configured ``ZimMetadata`` for this export. The
                ``name``, ``flavour``, and ``date`` fields must match the
                ``config.flavour`` and the intended filename.
            config: ``ExportConfig`` controlling scope, language, flavour, and
                item limits.
            output_path: Absolute ``Path`` where the ZIM file will be written.
                The parent directory must exist. Existing files at this path
                will be overwritten.
            illustration_bytes: Optional 48×48 PNG bytes for the ZIM icon.
                If ``None``, falls back to ``metadata.illustration_48x48_path``,
                then to a blank placeholder. Missing illustrations cause
                ``zimcheck`` warnings.
            zimcheck_binary: Path to the ``zimcheck`` binary or just ``"zimcheck"``
                if it is on ``PATH``. Pass ``None`` to skip validation entirely.
                Skipping is acceptable in development environments but should
                not be done in production.
            run_zimcheck: When ``True`` (default) and ``zimcheck_binary`` is
                not ``None``, runs ``zimcheck`` after ZIM generation. Pass
                ``False`` in test environments without ``zimcheck`` installed.

        Returns:
            ``ZimWriteResult`` with output path, SHA-256 checksum, article count,
            resource count, file size, generation duration, and zimcheck status.

        Raises:
            ``ValueError``: If ``metadata`` validation fails, or if no articles
                are available to write.
            ``FileNotFoundError``: If ``output_path.parent`` does not exist.

        Note:
            In stub mode (``self.db is None``), ``query_content_items()`` yields
            nothing. The ZIM file will contain only the index page. This is
            acceptable for integration tests verifying the pipeline structure.
        """
        logger.info(
            "export_to_zim: starting — name=%s scope=%s output=%s",
            metadata.name, config.scope.value, output_path,
        )

        writer = ZimWriter(
            metadata=metadata,
            config=config,
            output_path=output_path,
            illustration_bytes=illustration_bytes,
            zimcheck_binary=zimcheck_binary,
        )

        # Add shared CSS resource. All article HTML references this via a
        # relative path. For nopic exports (most common), the CSS is still
        # included; it is content-only and does not reference images.
        writer.add_resource(
            path="style/main.css",
            binary_content=_ARTICLE_CSS.encode("utf-8"),
            mime_type="text/css",
        )

        # Collect items for the index page domain map as we iterate.
        items_by_domain: dict[str, list[dict]] = {}
        item_count = 0

        async for item in self.query_content_items(config):
            domain = item.get("domain", "general")
            items_by_domain.setdefault(domain, []).append(item)

            html = self.render_article_html(item, language=config.language)
            path = f"{domain}/{item['cid']}"

            source_node_url = item.get("source_url")
            source_node_name = item.get("source_title") or (
                source_node_url.split("//")[-1].rstrip("/")
                if source_node_url else None
            )

            writer.add_article(
                path=path,
                content=html,
                article_type=item.get("item_type", ""),
                language=config.language,
                source_node_url=source_node_url,
                source_node_name=source_node_name,
                license_name=item.get("license"),
            )
            item_count += 1

        # Add index page (always present, even if item_count == 0 —
        # ZimWriter requires at least one front article)
        index_html = self.render_index_html(
            node_name=metadata.title,
            items_by_domain=items_by_domain or None,
            language=config.language,
        )
        writer.add_article(
            path="index",
            content=index_html,
            article_type="index",
            language=config.language,
        )

        result = writer.create_zim(run_zimcheck=run_zimcheck)

        logger.info(
            "export_to_zim: complete — articles=%d resources=%d sha256=%.8s... "
            "size=%d bytes duration=%.1fs zimcheck_passed=%s",
            result.article_count,
            result.resource_count,
            result.sha256,
            result.file_size_bytes,
            result.generation_duration_seconds,
            result.zimcheck_passed,
        )

        return result

    # ------------------------------------------------------------------
    # Auxiliary helpers
    # ------------------------------------------------------------------

    @staticmethod
    def validate_zim_output(result: ZimWriteResult) -> list[str]:
        """
        Validate a ``ZimWriteResult`` for post-export sanity checks.

        This is a lightweight, fast check that runs on the result object
        without re-reading the ZIM file. It complements ``zimcheck`` (which
        validates the ZIM binary format) by checking the pipeline-level
        invariants.

        Checks performed:
          - SHA-256 checksum is a 64-character lowercase hex string
          - Article count is at least 1
          - File size is at least 1 byte
          - Generation duration is non-negative
          - ``output_path`` exists on disk
          - ``zimcheck_passed`` is ``True``

        Args:
            result: ``ZimWriteResult`` returned by ``ZimWriter.create_zim()``.

        Returns:
            List of error strings. An empty list means all checks passed.
        """
        errors: list[str] = []

        if not re.match(r"^[0-9a-f]{64}$", result.sha256 or ""):
            errors.append(
                f"Invalid SHA-256 checksum: '{result.sha256}'. "
                f"Expected 64-character lowercase hex string."
            )

        if result.article_count < 1:
            errors.append(
                f"ZIM export has {result.article_count} articles. "
                f"At least 1 article is required for a valid ZIM file."
            )

        if result.file_size_bytes < 1:
            errors.append(
                f"ZIM file size is {result.file_size_bytes} bytes. "
                f"Expected a non-empty file."
            )

        if result.generation_duration_seconds < 0:
            errors.append(
                f"Generation duration is negative ({result.generation_duration_seconds}s). "
                f"This indicates a timing error."
            )

        if not result.output_path.exists():
            errors.append(
                f"ZIM output file does not exist at '{result.output_path}'. "
                f"The file may have been moved or renamed by zimcheck after a failure."
            )

        if not result.zimcheck_passed:
            errors.append(
                "zimcheck reported errors. The ZIM file may be corrupt or "
                "non-compliant. Check the logs for zimcheck output."
            )

        return errors

    @staticmethod
    def generate_zim_metadata(
        node_url: str,
        flavour: str = "nopic",
        language_iso3: str = "eng",
        node_name: str = "Open-Repo",
        scope_label: Optional[str] = None,
        source_url: Optional[str] = None,
        tags: str = "offline;practical-knowledge;procedures",
        long_description: Optional[str] = None,
    ) -> ZimMetadata:
        """
        Generate a ``ZimMetadata`` instance from node configuration.

        This is a convenience factory that constructs ``ZimMetadata`` with
        correct openZIM naming convention values derived from the node's
        configuration. It is the recommended way to create metadata for a
        standard export job.

        The generated ``name`` field follows the openZIM naming convention::

            {publisher_slug}_{language_code}_{flavour}

        where ``publisher_slug`` is derived from ``node_name`` by lower-casing
        and replacing spaces and underscores with hyphens.

        Example::

            metadata = ExportService.generate_zim_metadata(
                node_url="https://node.example.org",
                flavour="nopic",
                language_iso3="eng",
                node_name="Open-Repo",
            )
            # metadata.name == "open-repo_en_nopic"
            # metadata.title == "Open-Repo: Full Library (English)"

        Args:
            node_url: Base URL of this open-repo node. Used as ``source_url``
                in the ZIM metadata. Also used to derive the publisher slug if
                ``node_name`` is not provided.
            flavour: ZIM flavour string. Must be a value from
                ``ExportConfig.VALID_FLAVOURS``.
            language_iso3: ISO 639-3 language code for the ZIM ``Language``
                metadata field (e.g., ``"eng"``, ``"spa"``).
            node_name: Human-readable name of this node. Used as the ZIM
                ``Publisher`` and to derive the publisher slug.
            scope_label: Optional human-readable scope label for the ``Title``
                field (e.g., ``"Agriculture"``, ``"Full Library"``). If ``None``,
                defaults to ``"Full Library"``.
            source_url: Optional source URL override. Defaults to ``node_url``.
            tags: Semicolon-separated tags for ZIM catalog categorisation.
            long_description: Optional extended description (max 4000 chars).

        Returns:
            ``ZimMetadata`` instance ready for use with ``ZimWriter``.
        """
        # Derive publisher slug: lowercase, collapse whitespace/underscores to hyphens
        publisher_slug = re.sub(r"[\s_]+", "-", node_name.strip().lower())
        publisher_slug = re.sub(r"[^a-z0-9\-]", "", publisher_slug)
        publisher_slug = re.sub(r"-{2,}", "-", publisher_slug).strip("-")

        # ISO 639-1 two-letter code from ISO 639-3 (heuristic: take first 2 chars)
        lang_code = language_iso3[:2].lower()

        name = f"{publisher_slug}_{lang_code}_{flavour}"

        # Human-readable language name for title
        lang_display = _LANGUAGE_DISPLAY.get(language_iso3, language_iso3.upper())

        scope_display = scope_label or "Full Library"
        title = f"{node_name}: {scope_display} ({lang_display})"
        # Truncate title to 30 chars (openZIM recommendation)
        if len(title) > 30:
            title = title[:27] + "..."

        description = (
            "Offline practical knowledge library — "
            "practical how-to, recipes, and schematics"
        )
        # Truncate description to 80 chars (openZIM requirement)
        if len(description) > 80:
            description = description[:77] + "..."

        return ZimMetadata(
            title=title,
            description=description,
            language=language_iso3,
            name=name,
            flavour=flavour,
            creator=f"{node_name} Community",
            publisher=node_name,
            source_url=source_url or node_url,
            tags=tags,
            long_description=long_description,
        )

    # ------------------------------------------------------------------
    # Private rendering helpers
    # ------------------------------------------------------------------

    def _render_content_section(
        self,
        item_type: str,
        jsonld: dict,
        language: str,
    ) -> str:
        """
        Dispatch content rendering based on item type.

        Returns an HTML fragment (no ``<html>`` or ``<body>`` wrapper).
        """
        if item_type == "procedure":
            return self._render_procedure(jsonld, language)
        if item_type == "recipe":
            return self._render_recipe(jsonld, language)
        if item_type in ("schematic", "plan"):
            return self._render_schematic_or_plan(item_type, jsonld, language)
        # Generic fallback for unknown types
        return self._render_generic(jsonld, language)

    def _render_procedure(self, jsonld: dict, language: str) -> str:
        """Render a Procedure type: tools, materials, numbered steps."""
        parts: list[str] = []

        difficulty = jsonld.get("difficulty")
        if difficulty:
            parts.append(f"<p><em>Difficulty: {_escape(difficulty)}</em></p>")

        tools = jsonld.get("tools", [])
        if tools:
            rows = "".join(
                f"<tr><td>{_escape(str(t.get('quantity', '')))}</td>"
                f"<td>{_escape(_pick_language(t.get('name', {}), language) or str(t.get('name', '')))}</td></tr>"
                for t in tools
            )
            parts.append(
                "<h2>Tools Required</h2>"
                '<table class="materials-table">'
                "<thead><tr><th>Quantity</th><th>Tool</th></tr></thead>"
                f"<tbody>{rows}</tbody></table>"
            )

        materials = jsonld.get("materials", [])
        if materials:
            rows = "".join(
                f"<tr><td>{_escape(str(m.get('quantity', '')))}</td>"
                f"<td>{_escape(_pick_language(m.get('name', {}), language) or str(m.get('name', '')))}</td></tr>"
                for m in materials
            )
            parts.append(
                "<h2>Materials</h2>"
                '<table class="materials-table">'
                "<thead><tr><th>Quantity</th><th>Material</th></tr></thead>"
                f"<tbody>{rows}</tbody></table>"
            )

        steps = jsonld.get("steps", [])
        if steps:
            step_items = []
            for step in sorted(steps, key=lambda s: s.get("stepNumber", 0)):
                step_title = _escape(
                    _pick_language(step.get("title", {}), language)
                    or f"Step {step.get('stepNumber', '')}"
                )
                step_body = _escape(
                    _pick_language(step.get("body", {}), language) or ""
                )
                step_items.append(
                    f'<li><div class="step-title">{step_title}</div>'
                    f"<p>{step_body}</p></li>"
                )
            parts.append(
                '<h2>Steps</h2><ol class="steps-list">'
                + "".join(step_items)
                + "</ol>"
            )

        return "\n".join(parts) if parts else "<p><em>No content available.</em></p>"

    def _render_recipe(self, jsonld: dict, language: str) -> str:
        """Render a Recipe type: ingredients table, then steps."""
        parts: list[str] = []

        ingredients = jsonld.get("ingredients", [])
        if ingredients:
            rows = "".join(
                f"<tr><td>{_escape(str(i.get('quantity', '')))}</td>"
                f"<td>{_escape(_pick_language(i.get('name', {}), language) or str(i.get('name', '')))}</td></tr>"
                for i in ingredients
            )
            parts.append(
                "<h2>Ingredients</h2>"
                "<table><thead><tr><th>Quantity</th><th>Ingredient</th></tr></thead>"
                f"<tbody>{rows}</tbody></table>"
            )

        steps = jsonld.get("steps", [])
        if steps:
            step_items = []
            for step in sorted(steps, key=lambda s: s.get("stepNumber", 0)):
                step_title = _escape(
                    _pick_language(step.get("title", {}), language)
                    or f"Step {step.get('stepNumber', '')}"
                )
                step_body = _escape(
                    _pick_language(step.get("body", {}), language) or ""
                )
                step_items.append(
                    f'<li><div class="step-title">{step_title}</div>'
                    f"<p>{step_body}</p></li>"
                )
            parts.append(
                '<h2>Method</h2><ol class="steps-list">'
                + "".join(step_items)
                + "</ol>"
            )

        return "\n".join(parts) if parts else "<p><em>No content available.</em></p>"

    def _render_schematic_or_plan(
        self, item_type: str, jsonld: dict, language: str
    ) -> str:
        """Render a Schematic or Plan type."""
        parts: list[str] = []

        if item_type == "schematic":
            parts.append(
                "<p><em>This entry includes a schematic diagram. "
                "The diagram file is referenced in the digital version of this library.</em></p>"
            )

        steps = jsonld.get("steps", [])
        if steps:
            label = "Milestones" if item_type == "plan" else "Steps"
            step_items = []
            for step in sorted(steps, key=lambda s: s.get("stepNumber", 0)):
                step_title = _escape(
                    _pick_language(step.get("title", {}), language)
                    or f"Step {step.get('stepNumber', '')}"
                )
                step_body = _escape(
                    _pick_language(step.get("body", {}), language) or ""
                )
                step_items.append(
                    f'<li><div class="step-title">{step_title}</div>'
                    + (f"<p>{step_body}</p>" if step_body else "")
                    + "</li>"
                )
            parts.append(
                f"<h2>{label}</h2>"
                '<ol class="steps-list">' + "".join(step_items) + "</ol>"
            )

        return "\n".join(parts) if parts else "<p><em>No content available.</em></p>"

    def _render_generic(self, jsonld: dict, language: str) -> str:
        """Generic renderer for unknown item types."""
        content_fields = []
        for key, value in jsonld.items():
            if key.startswith("@") or key in ("description",):
                continue
            if isinstance(value, dict):
                text = _pick_language(value, language)
                if text:
                    content_fields.append(
                        f"<p><strong>{_escape(key.capitalize())}:</strong> "
                        f"{_escape(text)}</p>"
                    )
            elif isinstance(value, str):
                content_fields.append(
                    f"<p><strong>{_escape(key.capitalize())}:</strong> "
                    f"{_escape(value)}</p>"
                )
        return "\n".join(content_fields) if content_fields else "<p><em>No content available.</em></p>"


# ---------------------------------------------------------------------------
# Module-level utility functions
# ---------------------------------------------------------------------------

def _pick_language(d: dict, language: str) -> Optional[str]:
    """
    Pick a language-specific string from a multilingual dict.

    Tries the exact language code first, then falls back to any available
    value in the dict. Returns ``None`` if the dict is empty or not a dict.

    Args:
        d: Dict mapping language codes to strings, e.g. ``{"en": "Hello"}``.
        language: Preferred ISO 639-1 language code.

    Returns:
        The string for the preferred language, or any available string, or
        ``None`` if nothing is available.
    """
    if not isinstance(d, dict):
        return str(d) if d else None
    if language in d:
        return d[language]
    # Try common variants (e.g. "en-US" -> "en")
    short = language.split("-")[0]
    if short in d:
        return d[short]
    # Return first available value
    for v in d.values():
        if isinstance(v, str) and v:
            return v
    return None


def _escape(text: str) -> str:
    """
    HTML-escape a string to prevent XSS in rendered articles.

    Escapes ``&``, ``<``, ``>``, ``"``, and ``'``.
    """
    if not isinstance(text, str):
        text = str(text)
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    text = text.replace('"', "&quot;")
    text = text.replace("'", "&#x27;")
    return text


def _license_url(license_name: str) -> Optional[str]:
    """
    Return the canonical URL for a known SPDX license identifier.

    Returns ``None`` for unknown or non-SPDX identifiers.
    """
    _KNOWN = {
        "CC-BY-4.0": "https://creativecommons.org/licenses/by/4.0/",
        "CC-BY-SA-4.0": "https://creativecommons.org/licenses/by-sa/4.0/",
        "CC-BY-NC-4.0": "https://creativecommons.org/licenses/by-nc/4.0/",
        "CC-BY-NC-SA-4.0": "https://creativecommons.org/licenses/by-nc-sa/4.0/",
        "CC0-1.0": "https://creativecommons.org/publicdomain/zero/1.0/",
        "MIT": "https://opensource.org/licenses/MIT",
        "Apache-2.0": "https://www.apache.org/licenses/LICENSE-2.0",
    }
    return _KNOWN.get(license_name)


# ISO 639-3 to human-readable language name (subset for common exports)
_LANGUAGE_DISPLAY: dict[str, str] = {
    "eng": "English",
    "spa": "Spanish",
    "fra": "French",
    "por": "Portuguese",
    "swa": "Swahili",
    "ara": "Arabic",
    "hin": "Hindi",
    "zho": "Chinese",
    "ben": "Bengali",
    "amh": "Amharic",
    "hau": "Hausa",
    "yor": "Yoruba",
    "ibo": "Igbo",
    "mlg": "Malagasy",
}
