#!/usr/bin/env python
"""Load OpenFarm seed data into the database."""

import asyncio
import json
import sys
from pathlib import Path

# Add app to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from app.models import ContentItem, Base


async def load_seed_data(db_url: str, data_file: Path):
    """Load seed data from JSONL file into database."""
    # Create engine
    engine = create_async_engine(db_url, echo=False)

    # Create tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # Create session factory
    async_session_maker = async_sessionmaker(
        engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )

    # Read and load data
    loaded = 0
    skipped = 0

    async with async_session_maker() as session:
        with open(data_file, "r") as f:
            for line_num, line in enumerate(f, 1):
                try:
                    item_data = json.loads(line.strip())

                    # Extract CID
                    cid = item_data.get("cid")
                    if not cid:
                        print(f"Line {line_num}: Skipping - no CID")
                        skipped += 1
                        continue

                    # Check if already exists
                    from sqlalchemy import select
                    existing = await session.execute(
                        select(ContentItem).where(ContentItem.cid == cid)
                    )
                    if existing.scalar_one_or_none():
                        print(f"Line {line_num}: Item {cid} already exists")
                        skipped += 1
                        continue

                    # Create item
                    item = ContentItem(
                        cid=cid,
                        title=item_data.get("title", {}).get("en", "Untitled"),
                        item_type=item_data.get("type", "procedure"),
                        domain=item_data.get("domain", "procedural"),
                        license=item_data.get("license", "CC0-1.0"),
                        content_jsonld=item_data,
                        source_url=item_data.get("attribution", {}).get("source"),
                        source_title=item_data.get("attribution", {}).get("sourceTitle"),
                    )

                    session.add(item)
                    loaded += 1

                    if loaded % 10 == 0:
                        await session.commit()
                        print(f"Loaded {loaded} items...")

                except json.JSONDecodeError as e:
                    print(f"Line {line_num}: JSON decode error: {e}")
                    skipped += 1
                except Exception as e:
                    print(f"Line {line_num}: Error: {e}")
                    skipped += 1

        # Final commit
        await session.commit()

    await engine.dispose()

    print(f"\nSeed data load complete!")
    print(f"  Loaded: {loaded}")
    print(f"  Skipped: {skipped}")
    print(f"  Total: {loaded + skipped}")


async def main():
    """Main entry point."""
    import os

    # Get database URL
    db_url = os.getenv(
        "DATABASE_URL",
        "postgresql+asyncpg://postgres:postgres@localhost:5432/open_repo"
    )

    # Get data file
    data_file = Path(__file__).parent.parent.parent / "data" / "openfarm_procedures.jsonl"

    if not data_file.exists():
        print(f"Error: Data file not found at {data_file}")
        sys.exit(1)

    print(f"Loading seed data from {data_file}")
    print(f"Database: {db_url}")
    print()

    await load_seed_data(db_url, data_file)


if __name__ == "__main__":
    asyncio.run(main())
