"""
OpenFarm → Open-Repo Content Import Pipeline
=============================================

Transforms OpenFarm crop/guide/stage data into open-repo procedure JSON-LD items.

IMPORTANT: OpenFarm servers shut down April 2025. This script works against
local MongoDB exports or Internet Archive snapshots — NOT against a live API.

Data acquisition (before running this script):
  Option A — Self-host from source:
    git clone https://github.com/openfarmcc/OpenFarm.git
    cd OpenFarm && rake db:setup   # seeds MongoDB
    mongoexport --collection=crops --jsonArray --out=data/raw_crops.json
    mongoexport --collection=guides --jsonArray --out=data/raw_guides.json

  Option B — Internet Archive crawl:
    Use wayback_machine_downloader or custom scraper targeting:
    https://web.archive.org/web/*/openfarm.cc/api/v1/crops/*
    Then reconstruct raw_crops.json and raw_guides.json from snapshots.

  Option C — Run OpenFarm locally via Docker (see docs/docker-compose.yml)
    then hit http://localhost:3000/api/v1/crops?filter=<name> for each crop.

Pipeline stages:
  1. load_raw_data()       — read JSON export files into memory
  2. fetch_crops()         — paginate through the in-memory crop list
  3. transform_crop()      — map OpenFarm fields → open-repo procedure schema
  4. validate_schema()     — enforce minimum quality gates
  5. export_jsonl()        — write newline-delimited JSON for bulk DB import

Usage:
  uv run python scripts/import_openFarm.py --crops data/raw_crops.json \
      --guides data/raw_guides.json --output data/openfarm_procedures.jsonl \
      --page 0 --per-page 50

Dependencies (add to pyproject.toml under [project.optional-dependencies]):
  import = ["requests", "rich", "pydantic>=2.0"]
"""

from __future__ import annotations

import hashlib
import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Data Loading
# ---------------------------------------------------------------------------

RawCrop = dict[str, Any]
RawGuide = dict[str, Any]
RawStage = dict[str, Any]


def load_raw_data(
    crops_path: str | Path,
    guides_path: str | Path,
    stages_path: str | Path | None = None,
) -> tuple[list[RawCrop], list[RawGuide], list[RawStage]]:
    """
    Load raw MongoDB export JSON files produced by mongoexport --jsonArray.

    Each file is expected to be a JSON array of documents. The _id field from
    MongoDB is normalised: both {"$oid": "..."} format (mongoexport default)
    and plain string IDs are accepted.

    Args:
        crops_path:  Path to raw_crops.json (MongoDB export of crops collection)
        guides_path: Path to raw_guides.json (MongoDB export of guides collection)
        stages_path: Optional path to raw_stages.json. If None, stages are
                     expected to be embedded in each guide document under
                     the key "stages".

    Returns:
        Tuple of (crops, guides, stages) as lists of plain dicts.
    """
    def _load(path: str | Path) -> list[dict]:
        p = Path(path)
        if not p.exists():
            raise FileNotFoundError(f"Data file not found: {p}")
        with p.open("r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, list):
            raise ValueError(f"Expected JSON array in {p}, got {type(data).__name__}")
        return data

    def _normalise_id(doc: dict) -> dict:
        """Flatten MongoDB ObjectId format {"$oid": "..."} → plain string."""
        raw_id = doc.get("_id", doc.get("id", ""))
        if isinstance(raw_id, dict) and "$oid" in raw_id:
            doc["_id"] = raw_id["$oid"]
        return doc

    crops = [_normalise_id(c) for c in _load(crops_path)]
    guides = [_normalise_id(g) for g in _load(guides_path)]
    stages: list[RawStage] = []

    if stages_path is not None:
        stages = [_normalise_id(s) for s in _load(stages_path)]
    else:
        # Stages may be embedded in guide documents
        for guide in guides:
            for stage in guide.get("stages", []):
                stage["_guide_id"] = guide.get("_id", "")
                stages.append(_normalise_id(stage))

    return crops, guides, stages


# ---------------------------------------------------------------------------
# Pagination helper
# ---------------------------------------------------------------------------

def fetch_crops(
    crops: list[RawCrop],
    guides: list[RawGuide],
    stages: list[RawStage],
    page: int = 0,
    per_page: int = 50,
    min_completeness: float = 0.60,
    min_popularity: int = 0,
) -> list[tuple[RawCrop, RawGuide, list[RawStage]]]:
    """
    Return one page of (crop, best_guide, guide_stages) tuples.

    Selection logic:
    - For each crop, select the guide with the highest completeness_score that
      passes the minimum filters.
    - Crops with no qualifying guide are skipped.
    - Results are sorted by popularity_score descending before pagination so
      the first pages contain the best-known crops.

    Args:
        crops:           Full list of raw crop documents.
        guides:          Full list of raw guide documents.
        stages:          Full list of raw stage documents (with _guide_id set).
        page:            Zero-indexed page number.
        per_page:        Items per page.
        min_completeness: Minimum guide completeness_score (0.0–1.0).
        min_popularity:  Minimum guide popularity_score.

    Returns:
        List of (crop, guide, stages) tuples for this page.
    """
    # Index guides by crop ID for fast lookup
    guides_by_crop: dict[str, list[RawGuide]] = {}
    for g in guides:
        crop_id = g.get("crop_id") or g.get("crop", {}).get("_id", "")
        if crop_id:
            guides_by_crop.setdefault(str(crop_id), []).append(g)

    # Index stages by guide ID
    stages_by_guide: dict[str, list[RawStage]] = {}
    for s in stages:
        guide_id = s.get("_guide_id") or s.get("guide_id", "")
        if guide_id:
            stages_by_guide.setdefault(str(guide_id), []).append(s)

    # Build qualifying (crop, guide) pairs
    qualified: list[tuple[RawCrop, RawGuide, list[RawStage]]] = []
    for crop in crops:
        crop_id = str(crop.get("_id", ""))
        candidate_guides = guides_by_crop.get(crop_id, [])

        # Filter guides by quality thresholds
        passing = [
            g for g in candidate_guides
            if not g.get("draft", True)
            and g.get("completeness_score", 0.0) >= min_completeness
            and g.get("popularity_score", 0) >= min_popularity
        ]

        if not passing:
            continue

        # Select best guide (highest completeness, tie-break by popularity)
        best_guide = max(
            passing,
            key=lambda g: (g.get("completeness_score", 0.0), g.get("popularity_score", 0))
        )

        guide_id = str(best_guide.get("_id", ""))
        guide_stages = sorted(
            stages_by_guide.get(guide_id, []),
            key=lambda s: s.get("order", 0)
        )

        qualified.append((crop, best_guide, guide_stages))

    # Sort by popularity for consistent pagination
    qualified.sort(
        key=lambda t: t[1].get("popularity_score", 0),
        reverse=True
    )

    total = len(qualified)
    start = page * per_page
    end = start + per_page

    if start >= total:
        return []

    return qualified[start:end]


# ---------------------------------------------------------------------------
# Core transform
# ---------------------------------------------------------------------------

def transform_crop(
    raw_crop: RawCrop,
    raw_guide: RawGuide,
    raw_stages: list[RawStage],
    node_base_url: str = "https://node.openrepo.example.org",
    import_timestamp: str | None = None,
) -> dict[str, Any]:
    """
    Transform one OpenFarm crop+guide+stages triple into an open-repo procedure
    JSON-LD item matching the schema defined in mvp-protocol-design.md.

    This function is fully implemented — it performs the complete field mapping
    described in content-import-openFarm.md Section 6.

    OpenFarm → open-repo mapping summary:
      crop.name + guide.name       → title.en
      crop.description             → description.en
      guide.overview               → outcome.en
      stages (ordered)             → steps[]
      stage.name                   → steps[].title.en
      stage.overview               → steps[].body.en
      stage.stage_length           → steps[].duration (ISO 8601)
      sum(stage.stage_length)      → timeRequired.execution
      crop.minimum_temperature     → safetyNotes[]
      crop.common_names + practices → tags[]
      crop.sun_requirements        → prepended to step 1 body
      crop.spread, row_spacing     → step 3 body (transplant/spacing note)

    Args:
        raw_crop:          Raw MongoDB crop document.
        raw_guide:         Raw MongoDB guide document.
        raw_stages:        Ordered list of raw stage documents for this guide.
        node_base_url:     Base URL of the open-repo node (no trailing slash).
        import_timestamp:  ISO 8601 timestamp to use for created/updated.
                           Defaults to now (UTC).

    Returns:
        Dict representing the open-repo JSON-LD procedure item.
        The `cid` field is None — caller must compute after serialisation.
    """
    ts = import_timestamp or datetime.now(timezone.utc).isoformat()

    crop_id = str(raw_crop.get("_id", ""))
    guide_id = str(raw_guide.get("_id", ""))

    # --- Base item ID ---
    item_id = f"{node_base_url}/items/openfarm-{crop_id}-{guide_id}"

    # --- Title ---
    guide_name = (raw_guide.get("name") or "").strip()
    crop_name = (raw_crop.get("name") or "").strip()
    title_en = guide_name if guide_name else f"How to Grow {crop_name}"

    # --- Description (crop-level) ---
    description_en = (raw_crop.get("description") or "").strip() or None

    # --- Outcome (guide overview) ---
    outcome_en = (raw_guide.get("overview") or "").strip() or None

    # --- Tags ---
    common_names: list[str] = raw_crop.get("common_names") or []
    practices: list[str] = raw_guide.get("practices") or []
    tags = list({
        crop_name.lower(),
        *[n.lower() for n in common_names if n],
        *[p.lower() for p in practices if p],
        "growing-guide",
        "openfarm",
        "agriculture",
        "gardening",
    } - {""})
    tags.sort()

    # --- Steps from stages ---
    sun_req = (raw_crop.get("sun_requirements") or "").strip()
    min_temp = raw_crop.get("minimum_temperature")
    row_spacing = raw_crop.get("row_spacing")
    spread = raw_crop.get("spread")

    steps: list[dict[str, Any]] = []
    total_days = 0

    for i, stage in enumerate(raw_stages):
        stage_name = (stage.get("name") or f"Stage {i + 1}").strip()
        stage_body = (stage.get("overview") or "").strip()
        stage_length = stage.get("stage_length") or 0
        stage_order = stage.get("order", i + 1)

        # Enrich first step with sun requirements
        if i == 0 and sun_req:
            prefix = f"Sun requirement: {sun_req}. "
            if min_temp is not None:
                prefix += f"Minimum growing temperature: {min_temp}°C. "
            stage_body = prefix + stage_body

        # Enrich transplant-like step (order 3 or name contains "transplant")
        if (stage_order == 3 or "transplant" in stage_name.lower()) and (row_spacing or spread):
            spacing_note = ""
            if row_spacing:
                spacing_note += f" Space rows {row_spacing} cm apart."
            if spread:
                spacing_note += f" Plant spread: {spread} cm."
            stage_body = stage_body + spacing_note

        # Warning note: minimum temperature on last frost / outdoor stage
        warning = None
        if min_temp is not None and "transplant" in stage_name.lower():
            warning = {
                "en": (
                    f"Do not transplant outdoors until nighttime temperatures "
                    f"consistently stay above {min_temp}°C. Frost will kill the plant."
                )
            }

        # Duration in ISO 8601
        duration_iso = f"P{stage_length}D" if stage_length else None
        if stage_length:
            total_days += stage_length

        # Environment/soil/light from arrays → keep as structured metadata
        env: list[str] = stage.get("environment") or []
        soil: list[str] = stage.get("soil") or []
        light: list[str] = stage.get("light") or []

        step: dict[str, Any] = {
            "stepNumber": stage_order,
            "title": {"en": stage_name},
            "body": {"en": stage_body} if stage_body else {"en": ""},
            "media": [],
            "warningNote": warning,
            "verificationStep": None,
        }

        # Preserve OpenFarm structured arrays as extension metadata
        if duration_iso:
            step["duration"] = duration_iso
        if env:
            step["_environment"] = env
        if soil:
            step["_soil"] = soil
        if light:
            step["_light"] = light

        steps.append(step)

    # Total time as ISO 8601
    execution_duration = f"P{total_days}D" if total_days else None

    # --- Safety notes ---
    safety_notes: list[dict[str, str]] = []
    if min_temp is not None:
        safety_notes.append({
            "en": (
                f"Minimum growing temperature: {min_temp}°C. "
                f"Protect from frost; do not expose plants to freezing conditions."
            )
        })

    # --- Difficulty ---
    # OpenFarm has no difficulty field; infer a simple default
    difficulty = "beginner"
    days_to_maturity = raw_crop.get("days_to_maturity")
    if days_to_maturity and days_to_maturity > 120:
        difficulty = "intermediate"

    # --- Assemble final item ---
    item: dict[str, Any] = {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://schema.org/",
            "https://openrepo.net/ns/v1",
        ],
        "@type": "procedure",
        "id": item_id,
        "cid": None,
        "title": {"en": title_en},
        "description": {"en": description_en} if description_en else None,
        "domain": "procedural",
        "type": "procedure",
        "license": "CC0-1.0",
        "language": ["en"],
        "created": ts,
        "updated": ts,
        "attribution": {
            "source": "https://openfarm.cc",
            "sourceTitle": "OpenFarm — Free and Open Database for Farming and Gardening Knowledge",
            "originalLicense": "CC0-1.0 (Public Domain)",
            "importedAt": ts,
        },
        "tags": tags,
        "wikidataLinks": [],
        "endorsements": [],
        "relatedItems": [],
        "mediaItems": [],
        "node": node_base_url,
        "version": "1",
        # Procedure-specific fields
        "outcome": {"en": outcome_en} if outcome_en else None,
        "difficulty": difficulty,
        "timeRequired": {
            "execution": execution_duration
        } if execution_duration else None,
        "tools": [],
        "materials": [],
        "steps": steps,
        "safetyNotes": safety_notes,
        "performanceData": None,
        "costEstimate": None,
        "relatedSchematics": [],
        "relatedProcedures": [],
        "adaptations": [],
        # Import traceability
        "_importMeta": {
            "source": "openfarm",
            "cropId": crop_id,
            "guideId": guide_id,
            "completenessScore": raw_guide.get("completeness_score"),
            "popularityScore": raw_guide.get("popularity_score"),
            "binomialName": raw_crop.get("binomial_name"),
            "daysToMaturity": days_to_maturity,
        },
    }

    return item


# ---------------------------------------------------------------------------
# Schema validation
# ---------------------------------------------------------------------------

# Fields required to pass the quality gate
_REQUIRED_FIELDS = ["title", "type", "license", "attribution", "steps"]
_MIN_STEPS = 2
_MIN_TITLE_LEN = 5


def validate_schema(item: dict[str, Any]) -> tuple[bool, list[str]]:
    """
    Validate that a transformed item meets the minimum quality gates for
    import into the open-repo seed node.

    Gates (all must pass):
      1. All required top-level fields are present and non-empty.
      2. title.en is non-empty and > MIN_TITLE_LEN characters.
      3. steps array has at least MIN_STEPS entries.
      4. At least one step has a non-empty body.en.
      5. license is set to a recognised open license string.
      6. attribution.source is present.

    Args:
        item: Transformed open-repo item dict.

    Returns:
        (passed: bool, issues: list[str]) — issues is empty if passed.
    """
    issues: list[str] = []

    # Gate 1: required fields present
    for field in _REQUIRED_FIELDS:
        if not item.get(field):
            issues.append(f"Missing or empty required field: {field!r}")

    # Gate 2: title length
    title_en = (item.get("title") or {}).get("en", "")
    if len(title_en) < _MIN_TITLE_LEN:
        issues.append(
            f"title.en too short ({len(title_en)} chars, minimum {_MIN_TITLE_LEN})"
        )

    # Gate 3: minimum steps
    steps = item.get("steps") or []
    if len(steps) < _MIN_STEPS:
        issues.append(
            f"Too few steps ({len(steps)}, minimum {_MIN_STEPS})"
        )

    # Gate 4: at least one step with body content
    has_body = any(
        (s.get("body") or {}).get("en", "").strip()
        for s in steps
    )
    if steps and not has_body:
        issues.append("No step has non-empty body.en")

    # Gate 5: licence is acceptable
    accepted_licenses = {
        "CC0-1.0", "CC-BY-4.0", "CC-BY-SA-4.0",
        "CC-BY-NC-4.0", "CC-BY-NC-SA-4.0", "ODbL-1.0",
        "CERN-OHL-S-2.0", "TAPR-OHL",
    }
    licence = item.get("license", "")
    if licence not in accepted_licenses:
        issues.append(f"Unrecognised or missing license: {licence!r}")

    # Gate 6: attribution source
    attribution = item.get("attribution") or {}
    if not attribution.get("source"):
        issues.append("attribution.source is missing")

    passed = len(issues) == 0
    return passed, issues


# ---------------------------------------------------------------------------
# JSONL export
# ---------------------------------------------------------------------------

def export_jsonl(
    items: list[dict[str, Any]],
    path: str | Path,
    append: bool = False,
) -> int:
    """
    Write a list of items to a newline-delimited JSON (JSONL) file.

    JSONL format is used because:
    - It is streamable — each line is a self-contained JSON object.
    - PostgreSQL COPY and Meilisearch bulk import both accept JSONL.
    - Files can be appended safely across multiple import runs.

    Args:
        items:  List of transformed open-repo item dicts.
        path:   Output file path. Parent directory must exist.
        append: If True, append to existing file. Default is overwrite.

    Returns:
        Number of items written.
    """
    mode = "a" if append else "w"
    out_path = Path(path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    written = 0
    with out_path.open(mode, encoding="utf-8") as f:
        for item in items:
            f.write(json.dumps(item, ensure_ascii=False))
            f.write("\n")
            written += 1

    return written


# ---------------------------------------------------------------------------
# CID computation (IPFS CIDv1 approximation)
# ---------------------------------------------------------------------------

def compute_cid_placeholder(item: dict[str, Any]) -> str:
    """
    Compute a deterministic placeholder CID for an item.

    NOTE: This is NOT a real IPFS CIDv1. A real CIDv1 requires the `multihash`
    and `multibase` libraries and the kubo daemon. This function produces a
    SHA2-256 hex digest of the canonical JSON body as a stand-in that can be
    replaced with a real CID after IPFS is available.

    The canonical form excludes mutable fields: `cid`, `updated`, `endorsements`.

    Args:
        item: Transformed open-repo item dict (cid field may be None).

    Returns:
        String in the form "sha256-<hex>" (not a valid IPFS CID).
        Replace with real CIDv1 in production.
    """
    # Build canonical body excluding mutable fields
    canonical = {
        k: v for k, v in item.items()
        if k not in {"cid", "updated", "endorsements", "_importMeta"}
    }
    serialised = json.dumps(canonical, sort_keys=True, ensure_ascii=False)
    digest = hashlib.sha256(serialised.encode("utf-8")).hexdigest()
    return f"sha256-{digest}"


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def _parse_args() -> dict[str, Any]:
    """Minimal argument parsing without argparse dependency."""
    args = sys.argv[1:]
    parsed: dict[str, Any] = {
        "crops": "data/raw_crops.json",
        "guides": "data/raw_guides.json",
        "stages": None,
        "output": "data/openfarm_procedures.jsonl",
        "rejected": "data/openfarm_rejected.jsonl",
        "page": 0,
        "per_page": 50,
        "node_url": "https://node.openrepo.example.org",
        "min_completeness": 0.60,
        "verbose": False,
    }

    i = 0
    while i < len(args):
        arg = args[i]
        if arg in ("--crops",) and i + 1 < len(args):
            parsed["crops"] = args[i + 1]; i += 2
        elif arg in ("--guides",) and i + 1 < len(args):
            parsed["guides"] = args[i + 1]; i += 2
        elif arg in ("--stages",) and i + 1 < len(args):
            parsed["stages"] = args[i + 1]; i += 2
        elif arg in ("--output", "-o") and i + 1 < len(args):
            parsed["output"] = args[i + 1]; i += 2
        elif arg in ("--page",) and i + 1 < len(args):
            parsed["page"] = int(args[i + 1]); i += 2
        elif arg in ("--per-page",) and i + 1 < len(args):
            parsed["per_page"] = int(args[i + 1]); i += 2
        elif arg in ("--node-url",) and i + 1 < len(args):
            parsed["node_url"] = args[i + 1]; i += 2
        elif arg in ("--min-completeness",) and i + 1 < len(args):
            parsed["min_completeness"] = float(args[i + 1]); i += 2
        elif arg in ("--verbose", "-v"):
            parsed["verbose"] = True; i += 1
        else:
            i += 1

    return parsed


if __name__ == "__main__":
    """
    Fetch the first page of qualifying crops, transform them, validate,
    and print one transformed item as a demonstration.

    Run with:
        uv run python scripts/import_openFarm.py --verbose

    Or with custom data paths:
        uv run python scripts/import_openFarm.py \
            --crops /path/to/raw_crops.json \
            --guides /path/to/raw_guides.json \
            --output /path/to/output.jsonl \
            --page 0 --per-page 50

    NOTE: Requires raw_crops.json and raw_guides.json to exist.
    If running without real data, this will print an informative error.
    """
    args = _parse_args()
    verbose = args["verbose"]

    print("=" * 60)
    print("OpenFarm → Open-Repo Import Pipeline")
    print("=" * 60)

    # Step 1: Load data
    print(f"\n[1/4] Loading data from:")
    print(f"      crops:  {args['crops']}")
    print(f"      guides: {args['guides']}")

    try:
        crops, guides, stages = load_raw_data(
            args["crops"],
            args["guides"],
            args.get("stages"),
        )
    except FileNotFoundError as e:
        print(f"\nERROR: {e}")
        print(
            "\nTo run this script, you need raw MongoDB export files."
            "\nSee the docstring at the top of this file for data acquisition options."
            "\n\nQuick start:"
            "\n  1. Clone OpenFarm: git clone https://github.com/openfarmcc/OpenFarm.git"
            "\n  2. Run: cd OpenFarm && rake db:setup"
            "\n  3. Export: mongoexport --collection=crops --jsonArray --out=../open-repo/data/raw_crops.json"
            "\n  4. Export: mongoexport --collection=guides --jsonArray --out=../open-repo/data/raw_guides.json"
        )
        sys.exit(1)

    print(f"      Loaded {len(crops)} crops, {len(guides)} guides, {len(stages)} stages")

    # Step 2: Fetch one page
    print(f"\n[2/4] Fetching page {args['page']} ({args['per_page']} per page, "
          f"min completeness: {args['min_completeness']})")

    page_items = fetch_crops(
        crops, guides, stages,
        page=args["page"],
        per_page=args["per_page"],
        min_completeness=args["min_completeness"],
    )
    print(f"      Page contains {len(page_items)} qualifying (crop, guide, stages) triples")

    if not page_items:
        print("\nNo items on this page. Try --page 0 or lower --min-completeness.")
        sys.exit(0)

    # Step 3: Transform + validate
    print(f"\n[3/4] Transforming and validating...")

    ts = datetime.now(timezone.utc).isoformat()
    transformed: list[dict[str, Any]] = []
    rejected: list[dict[str, Any]] = []

    for crop, guide, guide_stages in page_items:
        item = transform_crop(
            crop, guide, guide_stages,
            node_base_url=args["node_url"],
            import_timestamp=ts,
        )
        # Compute placeholder CID
        item["cid"] = compute_cid_placeholder(item)

        passed, issues = validate_schema(item)

        if passed:
            transformed.append(item)
        else:
            item["_validationErrors"] = issues
            rejected.append(item)
            if verbose:
                print(f"  REJECTED: {item['title']['en']!r} — {issues}")

    print(f"      Passed: {len(transformed)}  |  Rejected: {len(rejected)}")

    # Step 4: Export
    print(f"\n[4/4] Exporting to {args['output']}")
    written = export_jsonl(transformed, args["output"])
    print(f"      Wrote {written} items to {args['output']}")

    if rejected:
        export_jsonl(rejected, args["rejected"])
        print(f"      Wrote {len(rejected)} rejected items to {args['rejected']}")

    # Print first transformed item as demonstration
    if transformed:
        print("\n" + "=" * 60)
        print("SAMPLE OUTPUT — First transformed item:")
        print("=" * 60)
        sample = transformed[0]
        # Print a readable summary rather than the full JSON
        print(f"  id:          {sample['id']}")
        print(f"  title:       {sample['title']['en']}")
        print(f"  license:     {sample['license']}")
        print(f"  steps:       {len(sample['steps'])}")
        print(f"  tags:        {', '.join(sample['tags'][:6])}{'...' if len(sample['tags']) > 6 else ''}")
        print(f"  cid:         {sample['cid']}")
        if verbose:
            print("\nFull JSON:")
            print(json.dumps(sample, indent=2, ensure_ascii=False))

    print(f"\nDone. {written} items written.")
    print(
        "\nNext steps:"
        "\n  1. Review data/openfarm_procedures.jsonl"
        "\n  2. Run Wikidata enrichment for wikidataLinks"
        "\n  3. Load into seed node: POST /api/v1/items (batch)"
        "\n  4. Compute real IPFS CIDs and update cid field"
        "\n  5. Human review sample: SELECT * FROM items ORDER BY RANDOM() LIMIT 20"
    )
