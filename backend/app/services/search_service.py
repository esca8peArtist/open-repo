"""Meilisearch integration for full-text search."""

import os
from typing import Optional, List, Dict, Any
import meilisearch


class SearchService:
    """Service for managing Meilisearch indexing and search."""

    def __init__(self, host: str = None, api_key: str = None):
        """Initialize Meilisearch client."""
        self.host = host or os.getenv("MEILISEARCH_HOST", "http://localhost:7700")
        self.api_key = api_key or os.getenv("MEILISEARCH_API_KEY", "masterKey")
        self.client = meilisearch.Client(self.host, self.api_key)
        self.index_name = "items"

    def ensure_index_exists(self):
        """Create index if it doesn't exist."""
        try:
            self.client.get_index(self.index_name)
        except (meilisearch.errors.MeilisearchError, Exception):
            # Index doesn't exist or Meilisearch is unreachable, skip
            pass

    def index_item(self, cid: str, title: str, description: str = "",
                   tags: List[str] = None, domain: str = "", item_type: str = "",
                   author: str = "", created_at: str = ""):
        """Index a content item in Meilisearch."""
        if tags is None:
            tags = []

        document = {
            "cid": cid,
            "title": title,
            "description": description,
            "tags": tags,
            "domain": domain,
            "item_type": item_type,
            "author": author,
            "created_at": created_at,
        }

        try:
            index = self.client.get_index(self.index_name)
            index.add_documents([document])
        except meilisearch.errors.MeilisearchError:
            # Index doesn't exist, create it first
            self.ensure_index_exists()
            index = self.client.get_index(self.index_name)
            index.add_documents([document])

    def delete_item(self, cid: str):
        """Remove a content item from the search index."""
        try:
            index = self.client.get_index(self.index_name)
            index.delete_document(cid)
        except meilisearch.errors.MeilisearchError:
            # Index doesn't exist or document doesn't exist, silently ignore
            pass

    def search(self, query: str, limit: int = 10, offset: int = 0,
               item_type: Optional[str] = None, domain: Optional[str] = None,
               tags: Optional[List[str]] = None) -> Dict[str, Any]:
        """Search for content items.

        Args:
            query: Search query string
            limit: Number of results to return
            offset: Pagination offset
            item_type: Filter by item type
            domain: Filter by domain
            tags: Filter by tags (any match)

        Returns:
            Dictionary with search results and metadata
        """
        try:
            index = self.client.get_index(self.index_name)
        except Exception:
            # Index doesn't exist or Meilisearch is unreachable, return empty results
            return {
                "hits": [],
                "query": query,
                "limit": limit,
                "offset": offset,
                "estimated_total_hits": 0,
                "processing_time_ms": 0,
            }

        try:
            # Build filter expression
            filters = []
            if item_type:
                filters.append(f'item_type = "{item_type}"')
            if domain:
                filters.append(f'domain = "{domain}"')
            if tags:
                # Filter by any of the provided tags
                tag_filters = [f'tags = "{tag}"' for tag in tags]
                filters.append(f"({' OR '.join(tag_filters)})")

            filter_str = " AND ".join(filters) if filters else None

            # Perform search
            results = index.search(
                query,
                {
                    "limit": limit,
                    "offset": offset,
                    "filter": filter_str,
                }
            )

            return results
        except Exception:
            # Search failed, return empty results
            return {
                "hits": [],
                "query": query,
                "limit": limit,
                "offset": offset,
                "estimated_total_hits": 0,
                "processing_time_ms": 0,
            }

    def get_stats(self) -> Dict[str, Any]:
        """Get search index statistics."""
        try:
            index = self.client.get_index(self.index_name)
            stats = index.get_stats()
            return stats
        except meilisearch.errors.MeilisearchError:
            return {
                "numberOfDocuments": 0,
                "isIndexing": False,
            }


# Global instance
_search_service: Optional[SearchService] = None


def get_search_service() -> SearchService:
    """Get or create global SearchService instance."""
    global _search_service
    if _search_service is None:
        _search_service = SearchService()
        _search_service.ensure_index_exists()
    return _search_service


def reset_search_service():
    """Reset the global search service (for testing)."""
    global _search_service
    _search_service = None
