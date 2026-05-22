"""
Phase 5.2 Domain Content Type Schemas

Defines validated dataclass schemas for the five domain-specific content modules
planned in Phase 5.2. Each schema produces ZIM article records that feed into
the existing ZimWriter pipeline.

Domain modules (to be implemented in Wave 1–3, June–July 2026):
  - MedicalArticle       (Wave 1 — medical_importer.py)
  - WaterProcedure       (Wave 1 — water_importer.py)
  - SeedSpecies          (Wave 2 — seed_importer.py)
  - FoodSafetyTable      (Wave 2 — food_importer.py)
  - BotanicalSpecies     (Wave 3 — botanical_importer.py)

Each schema validates required fields at instantiation time. Fields that are
safety-critical (medical disclaimers, USDA source citations, toxicity flags)
are non-nullable with explicit validation.

Usage (post-implementation):
    article = MedicalArticle(
        drug_name="Amoxicillin",
        indication="Bacterial infections",
        adult_dose="500 mg three times daily",
        disclaimer=MEDICAL_DISCLAIMER,  # required, non-null
        source_citation="WHO Model Formulary 2008, p.45",
    )
    zim_entry = article.to_zim_entry()

Design references:
  - PHASE_5.2_IMPLEMENTATION_ROADMAP.md (schema definitions, field specs)
  - PHASE_5.2_ZIM_VALIDATION_MATRIX.md  (validation requirements per field)
  - MEDICAL_CONTENT_SOURCING_CHECKLIST.md (medical content policy)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional
import re


# ---------------------------------------------------------------------------
# Shared constants
# ---------------------------------------------------------------------------

MEDICAL_DISCLAIMER = (
    "IMPORTANT: This information is for reference use in austere or resource-limited "
    "environments when professional medical care is unavailable. It does not replace "
    "professional medical judgment. Always consult a qualified healthcare provider "
    "when one is available. Drug dosing errors can be fatal. Verify all dosages "
    "against current clinical guidelines before administration."
)

FOOD_SAFETY_DISCLAIMER = (
    "Processing times and pressures listed here are from the USDA Complete Guide to "
    "Home Canning (2015 edition) and must not be modified. Insufficient processing "
    "can cause botulism, which is fatal. Do not use recipes from other sources unless "
    "they have been tested by the USDA, Ball, or an accredited food safety laboratory."
)

BOTANICAL_TOXICITY_DISCLAIMER = (
    "Toxicity and edibility classifications are based on documented sources. "
    "Misidentification of wild plants is dangerous. Never consume any plant unless "
    "you are certain of the identification. When in doubt, do not eat."
)


# ---------------------------------------------------------------------------
# Wave 1: Medical Reference
# ---------------------------------------------------------------------------

@dataclass
class MedicalArticle:
    """
    A single drug monograph or medical procedure article.

    Source documents:
      - WHO Model Formulary (drug monographs)
      - WHO Essential Medicines List 23rd edition (2023)
      - ICRC First Aid Guidelines (procedure protocols)

    Safety-critical fields (non-nullable, validated at instantiation):
      - disclaimer: Must be the canonical MEDICAL_DISCLAIMER string (or equivalent)
      - source_citation: Must reference a specific page/section in a named source
      - adult_dose: Non-empty for drug monographs

    ZIM path convention: medical/{slug}
    """

    # Required fields
    article_type: str       # "drug_monograph" | "procedure_guide" | "evacuation_criteria"
    title: str              # Article title, used as ZIM title and <h1>
    slug: str               # URL-safe identifier, becomes ZIM path component
    disclaimer: str         # Must not be null; must contain MEDICAL_DISCLAIMER text
    source_citation: str    # Must reference a specific source document + page/section

    # Drug monograph fields (required when article_type == "drug_monograph")
    drug_name: Optional[str] = None
    indication: Optional[str] = None
    adult_dose: Optional[str] = None
    pediatric_dose: Optional[str] = None
    weight_based_dose: Optional[str] = None    # e.g., "10 mg/kg every 8h, max 500 mg/dose"
    contraindications: Optional[str] = None
    drug_interactions: Optional[str] = None    # Clinically significant only
    supply_quantity_1yr: Optional[str] = None  # Stock recommendation for 1-year supply
    evacuation_criteria: Optional[str] = None  # When to evacuate despite treatment

    # Procedure article fields (required when article_type == "procedure_guide")
    procedure_steps: list[str] = field(default_factory=list)
    equipment_list: list[str] = field(default_factory=list)
    contraindications_procedure: Optional[str] = None

    # Optional enrichment
    tags: list[str] = field(default_factory=list)
    related_articles: list[str] = field(default_factory=list)  # ZIM internal paths

    def __post_init__(self) -> None:
        """Validate safety-critical fields at instantiation."""
        if not self.disclaimer:
            raise ValueError("MedicalArticle.disclaimer must not be null or empty.")
        if not self.source_citation:
            raise ValueError("MedicalArticle.source_citation must reference a specific source.")
        if not self.slug:
            raise ValueError("MedicalArticle.slug must not be empty.")
        if not re.match(r'^[a-z0-9\-]+$', self.slug):
            raise ValueError(
                f"MedicalArticle.slug must be lowercase alphanumeric with hyphens; got: {self.slug!r}"
            )
        if self.article_type not in ("drug_monograph", "procedure_guide", "evacuation_criteria"):
            raise ValueError(
                f"MedicalArticle.article_type must be one of: drug_monograph, "
                f"procedure_guide, evacuation_criteria; got: {self.article_type!r}"
            )
        if self.article_type == "drug_monograph" and not self.adult_dose:
            raise ValueError(
                "MedicalArticle: adult_dose is required for drug_monograph articles."
            )

    @property
    def zim_path(self) -> str:
        """ZIM article path: medical/{slug}"""
        return f"medical/{self.slug}"


# ---------------------------------------------------------------------------
# Wave 1: Water Systems
# ---------------------------------------------------------------------------

@dataclass
class WaterProcedure:
    """
    A water treatment, storage, or well construction procedure.

    Source documents:
      - WHO Drinking Water Quality Guidelines 4th edition (2022)
      - CDC Emergency Water Disinfection guidance
      - USDA NRCS well yield and construction guides

    ZIM path convention: water/{slug}
    """

    # Required fields
    title: str
    slug: str
    procedure_name: str
    steps: list[str]                        # Ordered list of procedure steps
    source_citation: str                    # Source document + section

    # Equipment and sizing
    equipment_list: list[str] = field(default_factory=list)
    sizing_inputs: list[str] = field(default_factory=list)   # e.g., "household size (persons)"
    sizing_outputs: list[str] = field(default_factory=list)  # e.g., "liters per day capacity"

    # Safety thresholds
    acceptable_turbidity_ntu: Optional[float] = None  # Maximum turbidity NTU before treatment
    disinfection_contact_time_minutes: Optional[float] = None
    minimum_free_chlorine_mg_per_l: Optional[float] = None

    # Optional enrichment
    tags: list[str] = field(default_factory=list)
    related_articles: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.slug:
            raise ValueError("WaterProcedure.slug must not be empty.")
        if not re.match(r'^[a-z0-9\-]+$', self.slug):
            raise ValueError(
                f"WaterProcedure.slug must be lowercase alphanumeric with hyphens; got: {self.slug!r}"
            )
        if not self.steps:
            raise ValueError("WaterProcedure.steps must contain at least one step.")
        if not self.source_citation:
            raise ValueError("WaterProcedure.source_citation must reference a specific source.")

    @property
    def zim_path(self) -> str:
        """ZIM article path: water/{slug}"""
        return f"water/{self.slug}"


# ---------------------------------------------------------------------------
# Wave 2: Seed Preservation
# ---------------------------------------------------------------------------

@dataclass
class SeedSpecies:
    """
    A single seed species record from GRIN accession data.

    Source:
      - GRIN (Germplasm Resources Information Network) bulk CSV downloads
      - USDA PLANTS database (for native range and hardiness zones)

    ZIM path convention: seeds/{slug}
    """

    # Required fields
    common_name: str
    latin_binomial: str
    family: str
    slug: str

    # GRIN reference
    grin_accession_number: Optional[str] = None  # GRIN accession if available

    # Storage specifications
    storage_temperature_celsius_min: Optional[float] = None
    storage_temperature_celsius_max: Optional[float] = None
    storage_humidity_pct_max: Optional[float] = None
    expected_viability_years: Optional[int] = None
    germination_rate_pct: Optional[float] = None   # Expected germination rate 0.0–100.0

    # Growing information
    usda_hardiness_zones: Optional[str] = None     # e.g., "3-8"
    seed_saving_difficulty: Optional[str] = None   # "easy" | "moderate" | "difficult"

    # Optional enrichment
    notes: Optional[str] = None
    tags: list[str] = field(default_factory=list)
    related_articles: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.slug:
            raise ValueError("SeedSpecies.slug must not be empty.")
        if not re.match(r'^[a-z0-9\-]+$', self.slug):
            raise ValueError(
                f"SeedSpecies.slug must be lowercase alphanumeric with hyphens; got: {self.slug!r}"
            )
        if self.germination_rate_pct is not None:
            if not (0.0 <= self.germination_rate_pct <= 100.0):
                raise ValueError(
                    f"SeedSpecies.germination_rate_pct must be 0.0–100.0; got {self.germination_rate_pct}"
                )
        if self.seed_saving_difficulty is not None:
            if self.seed_saving_difficulty not in ("easy", "moderate", "difficult"):
                raise ValueError(
                    f"SeedSpecies.seed_saving_difficulty must be easy/moderate/difficult; "
                    f"got: {self.seed_saving_difficulty!r}"
                )

    @property
    def zim_path(self) -> str:
        """ZIM article path: seeds/{slug}"""
        return f"seeds/{self.slug}"


# ---------------------------------------------------------------------------
# Wave 2: Food Safety
# ---------------------------------------------------------------------------

@dataclass
class FoodSafetyTable:
    """
    A food safety processing time table (canning, pickling, preservation).

    CRITICAL REQUIREMENT: Every record must carry a usda_edition field
    confirming the source. Processing times must be reproduced verbatim from
    the USDA source — do not derive, interpolate, or estimate values.
    Incorrect processing times can cause botulism, which is fatal.

    Source:
      - USDA Complete Guide to Home Canning (2015 edition, public domain)

    ZIM path convention: food-safety/{slug}
    """

    # Required fields — all non-nullable
    food_category: str         # e.g., "tomatoes", "low-acid vegetables", "fruits", "meats", "pickles"
    food_item: str             # e.g., "Whole or halved tomatoes"
    jar_size: str              # "pint" | "quart" | "half-pint"
    processing_method: str     # "pressure" | "water_bath"
    processing_time_minutes: int
    usda_edition: str          # "USDA 2015" — mandatory, cannot be blank
    slug: str
    disclaimer: str            # Must contain FOOD_SAFETY_DISCLAIMER

    # Pressure canning parameters (required when processing_method == "pressure")
    pressure_psi_0_2000ft: Optional[float] = None   # Pressure at 0–2,000 ft altitude
    pressure_psi_2001_4000ft: Optional[float] = None
    pressure_psi_4001_6000ft: Optional[float] = None
    pressure_psi_above_6000ft: Optional[float] = None

    # Water bath altitude adjustments (required when processing_method == "water_bath")
    additional_minutes_1001_3000ft: Optional[int] = None
    additional_minutes_3001_6000ft: Optional[int] = None
    additional_minutes_above_6000ft: Optional[int] = None

    # Safety classification
    botulism_risk_level: Optional[str] = None  # "high" | "moderate" | "low"
    source_page: Optional[str] = None          # Page number in source document

    # Optional enrichment
    notes: Optional[str] = None
    tags: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.usda_edition:
            raise ValueError(
                "FoodSafetyTable.usda_edition is required and must not be blank. "
                "Processing times without a source edition cannot be published."
            )
        if not self.disclaimer:
            raise ValueError("FoodSafetyTable.disclaimer must not be null or empty.")
        if not self.slug:
            raise ValueError("FoodSafetyTable.slug must not be empty.")
        if not re.match(r'^[a-z0-9\-]+$', self.slug):
            raise ValueError(
                f"FoodSafetyTable.slug must be lowercase alphanumeric with hyphens; "
                f"got: {self.slug!r}"
            )
        if self.processing_method not in ("pressure", "water_bath"):
            raise ValueError(
                f"FoodSafetyTable.processing_method must be 'pressure' or 'water_bath'; "
                f"got: {self.processing_method!r}"
            )
        if self.jar_size not in ("half-pint", "pint", "quart"):
            raise ValueError(
                f"FoodSafetyTable.jar_size must be half-pint, pint, or quart; "
                f"got: {self.jar_size!r}"
            )
        if self.processing_time_minutes <= 0:
            raise ValueError(
                f"FoodSafetyTable.processing_time_minutes must be positive; "
                f"got: {self.processing_time_minutes}"
            )
        if self.botulism_risk_level is not None:
            if self.botulism_risk_level not in ("high", "moderate", "low"):
                raise ValueError(
                    f"FoodSafetyTable.botulism_risk_level must be high/moderate/low; "
                    f"got: {self.botulism_risk_level!r}"
                )

    @property
    def zim_path(self) -> str:
        """ZIM article path: food-safety/{slug}"""
        return f"food-safety/{self.slug}"


# ---------------------------------------------------------------------------
# Wave 3: Botanical Knowledge
# ---------------------------------------------------------------------------

EVIDENCE_LEVELS = {
    "A": "Clinical trial evidence — peer-reviewed study confirms this use.",
    "B": "Traditional use — documented in ethnobotanical literature.",
    "C": "Anecdotal — reported but not formally documented.",
}


@dataclass
class BotanicalSpecies:
    """
    A botanical species record combining edibility, toxicity, and medicinal use.

    Extends SeedSpecies with edibility classification, toxicity notes, and
    medicinal evidence levels. Edibility/toxicity fields are safety-critical:
    a misclassification could cause harm.

    Sources:
      - USDA PLANTS database (44,000 species; filtered to ~1,000–3,000)
      - Wikimedia Commons (illustration images, CC BY/BY-SA)
      - off-grid-living/08-medical-health.md (internal cross-references)

    ZIM path convention: botany/{slug}
    """

    # Required fields (inherited from seed base)
    common_name: str
    latin_binomial: str
    family: str
    slug: str

    # Edibility classification — safety-critical, non-nullable
    edibility_classification: str   # "edible" | "edible_with_preparation" | "toxic" | "unknown"

    # Toxicity — required if edibility_classification is "toxic"
    toxicity_notes: Optional[str] = None
    toxicity_source_citation: Optional[str] = None  # Required if toxicity_notes is not None

    # Lookalike hazard
    lookalike_species: list[str] = field(default_factory=list)  # Latin names of dangerous lookalikes
    lookalike_hazard_warning: Optional[str] = None

    # Medicinal use — evidence must be classified
    medicinal_uses: list[str] = field(default_factory=list)
    medicinal_evidence_level: Optional[str] = None  # "A" | "B" | "C" — default C
    medicinal_source_citation: Optional[str] = None  # Required if medicinal_evidence_level is "A" or "B"

    # GRIN reference
    grin_accession_number: Optional[str] = None

    # Growing information
    usda_hardiness_zones: Optional[str] = None
    native_range: Optional[str] = None       # e.g., "Eastern North America"

    # Illustration
    wikimedia_image_url: Optional[str] = None   # CC BY or CC BY-SA only
    wikimedia_image_license: Optional[str] = None

    # Cross-domain links
    related_medical_articles: list[str] = field(default_factory=list)  # ZIM internal paths
    related_seed_articles: list[str] = field(default_factory=list)

    # Optional enrichment
    tags: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.slug:
            raise ValueError("BotanicalSpecies.slug must not be empty.")
        if not re.match(r'^[a-z0-9\-]+$', self.slug):
            raise ValueError(
                f"BotanicalSpecies.slug must be lowercase alphanumeric with hyphens; "
                f"got: {self.slug!r}"
            )
        valid_edibility = ("edible", "edible_with_preparation", "toxic", "unknown")
        if self.edibility_classification not in valid_edibility:
            raise ValueError(
                f"BotanicalSpecies.edibility_classification must be one of {valid_edibility}; "
                f"got: {self.edibility_classification!r}"
            )
        # Safety rule: toxicity notes require a source citation
        if self.toxicity_notes and not self.toxicity_source_citation:
            raise ValueError(
                "BotanicalSpecies.toxicity_source_citation is required when toxicity_notes is set. "
                "Toxicity classifications must be sourced."
            )
        # Safety rule: toxic classification requires toxicity notes
        if self.edibility_classification == "toxic" and not self.toxicity_notes:
            raise ValueError(
                "BotanicalSpecies with edibility_classification='toxic' must have toxicity_notes set."
            )
        # Evidence level validation
        if self.medicinal_evidence_level is not None:
            if self.medicinal_evidence_level not in EVIDENCE_LEVELS:
                raise ValueError(
                    f"BotanicalSpecies.medicinal_evidence_level must be A, B, or C; "
                    f"got: {self.medicinal_evidence_level!r}"
                )
            # High-confidence claims (A, B) require a citation
            if self.medicinal_evidence_level in ("A", "B") and not self.medicinal_source_citation:
                raise ValueError(
                    f"BotanicalSpecies.medicinal_source_citation is required for evidence level "
                    f"'{self.medicinal_evidence_level}'. Level A and B claims must be sourced."
                )
        # Default evidence to C if medicinal uses provided but no level set
        if self.medicinal_uses and self.medicinal_evidence_level is None:
            self.medicinal_evidence_level = "C"

    @property
    def zim_path(self) -> str:
        """ZIM article path: botany/{slug}"""
        return f"botany/{self.slug}"
