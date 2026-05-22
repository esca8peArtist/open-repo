"""
Phase 5.2 Content Type Schema Tests

Tests for the five domain content schemas in app/services/importers/schemas.py.
These tests validate safety-critical field requirements, slug formatting,
and data integrity constraints.

All tests are pure Python (no database, no libzim required). Run with:
    uv run pytest tests/test_phase52_schemas.py -v

Safety-critical tests are marked with @pytest.mark.data_integrity.
These must never be skipped in CI.
"""

import pytest
from app.services.importers.schemas import (
    FOOD_SAFETY_DISCLAIMER,
    MEDICAL_DISCLAIMER,
    BotanicalSpecies,
    FoodSafetyTable,
    MedicalArticle,
    SeedSpecies,
    WaterProcedure,
)


# ---------------------------------------------------------------------------
# MedicalArticle tests
# ---------------------------------------------------------------------------

class TestMedicalArticle:
    """Validation tests for the MedicalArticle schema."""

    def _valid_drug(self, **overrides) -> dict:
        base = dict(
            article_type="drug_monograph",
            title="Amoxicillin",
            slug="amoxicillin",
            disclaimer=MEDICAL_DISCLAIMER,
            source_citation="WHO Model Formulary 2008, p.45",
            drug_name="Amoxicillin",
            indication="Bacterial infections (strep, H. pylori, Lyme disease)",
            adult_dose="500 mg three times daily for 7–10 days",
        )
        base.update(overrides)
        return base

    def test_valid_drug_monograph_constructs(self):
        article = MedicalArticle(**self._valid_drug())
        assert article.title == "Amoxicillin"
        assert article.zim_path == "medical/amoxicillin"

    def test_valid_procedure_guide_constructs(self):
        article = MedicalArticle(
            article_type="procedure_guide",
            title="Wound Closure with Steri-Strips",
            slug="wound-closure-steri-strips",
            disclaimer=MEDICAL_DISCLAIMER,
            source_citation="ICRC First Aid Guidelines 2016, p.112",
            procedure_steps=["Clean wound thoroughly", "Approximate wound edges", "Apply strips"],
            equipment_list=["Steri-Strips", "Saline solution", "Gauze"],
        )
        assert article.zim_path == "medical/wound-closure-steri-strips"

    def test_valid_evacuation_criteria_constructs(self):
        article = MedicalArticle(
            article_type="evacuation_criteria",
            title="Evacuation Criteria — Sepsis",
            slug="evacuation-sepsis",
            disclaimer=MEDICAL_DISCLAIMER,
            source_citation="ICRC First Aid Guidelines 2016, p.203",
        )
        assert article.article_type == "evacuation_criteria"

    @pytest.mark.data_integrity
    def test_null_disclaimer_raises(self):
        with pytest.raises(ValueError, match="disclaimer must not be null"):
            MedicalArticle(**self._valid_drug(disclaimer=""))

    @pytest.mark.data_integrity
    def test_missing_source_citation_raises(self):
        with pytest.raises(ValueError, match="source_citation must reference"):
            MedicalArticle(**self._valid_drug(source_citation=""))

    @pytest.mark.data_integrity
    def test_drug_monograph_without_adult_dose_raises(self):
        with pytest.raises(ValueError, match="adult_dose is required"):
            MedicalArticle(**self._valid_drug(adult_dose=None))

    def test_invalid_article_type_raises(self):
        with pytest.raises(ValueError, match="article_type must be one of"):
            MedicalArticle(**self._valid_drug(article_type="invalid"))

    def test_invalid_slug_raises(self):
        with pytest.raises(ValueError, match="slug must be lowercase alphanumeric"):
            MedicalArticle(**self._valid_drug(slug="Amoxicillin 500mg"))

    def test_empty_slug_raises(self):
        with pytest.raises(ValueError, match="slug must not be empty"):
            MedicalArticle(**self._valid_drug(slug=""))

    def test_slug_with_uppercase_raises(self):
        with pytest.raises(ValueError, match="slug must be lowercase alphanumeric"):
            MedicalArticle(**self._valid_drug(slug="Amoxicillin"))

    def test_slug_with_underscore_raises(self):
        with pytest.raises(ValueError, match="slug must be lowercase alphanumeric"):
            MedicalArticle(**self._valid_drug(slug="drug_name"))

    def test_zim_path_format(self):
        article = MedicalArticle(**self._valid_drug(slug="metronidazole"))
        assert article.zim_path == "medical/metronidazole"

    def test_related_articles_default_empty(self):
        article = MedicalArticle(**self._valid_drug())
        assert article.related_articles == []

    def test_tags_default_empty(self):
        article = MedicalArticle(**self._valid_drug())
        assert article.tags == []


# ---------------------------------------------------------------------------
# WaterProcedure tests
# ---------------------------------------------------------------------------

class TestWaterProcedure:
    """Validation tests for the WaterProcedure schema."""

    def _valid_procedure(self, **overrides) -> dict:
        base = dict(
            title="Household Chlorination",
            slug="household-chlorination",
            procedure_name="Emergency Water Chlorination for Household Use",
            steps=[
                "Fill clean container with water.",
                "Add 2 drops of 5.25% unscented bleach per litre.",
                "Stir and let stand 30 minutes before drinking.",
            ],
            source_citation="CDC Emergency Water Disinfection, Table 2 (2022)",
        )
        base.update(overrides)
        return base

    def test_valid_procedure_constructs(self):
        proc = WaterProcedure(**self._valid_procedure())
        assert proc.zim_path == "water/household-chlorination"

    @pytest.mark.data_integrity
    def test_empty_steps_raises(self):
        with pytest.raises(ValueError, match="steps must contain at least one step"):
            WaterProcedure(**self._valid_procedure(steps=[]))

    @pytest.mark.data_integrity
    def test_missing_source_citation_raises(self):
        with pytest.raises(ValueError, match="source_citation must reference"):
            WaterProcedure(**self._valid_procedure(source_citation=""))

    def test_invalid_slug_raises(self):
        with pytest.raises(ValueError, match="slug must be lowercase alphanumeric"):
            WaterProcedure(**self._valid_procedure(slug="Household Chlorination"))

    def test_empty_slug_raises(self):
        with pytest.raises(ValueError, match="slug must not be empty"):
            WaterProcedure(**self._valid_procedure(slug=""))

    def test_safety_thresholds_optional(self):
        proc = WaterProcedure(**self._valid_procedure())
        assert proc.acceptable_turbidity_ntu is None
        assert proc.disinfection_contact_time_minutes is None

    def test_safety_thresholds_set(self):
        proc = WaterProcedure(
            **self._valid_procedure(
                acceptable_turbidity_ntu=1.0,
                disinfection_contact_time_minutes=30.0,
                minimum_free_chlorine_mg_per_l=0.2,
            )
        )
        assert proc.acceptable_turbidity_ntu == 1.0


# ---------------------------------------------------------------------------
# SeedSpecies tests
# ---------------------------------------------------------------------------

class TestSeedSpecies:
    """Validation tests for the SeedSpecies schema."""

    def _valid_species(self, **overrides) -> dict:
        base = dict(
            common_name="Corn",
            latin_binomial="Zea mays",
            family="Poaceae",
            slug="zea-mays",
            grin_accession_number="PI 612928",
            storage_temperature_celsius_min=0.0,
            storage_temperature_celsius_max=10.0,
            storage_humidity_pct_max=35.0,
            expected_viability_years=5,
            germination_rate_pct=85.0,
        )
        base.update(overrides)
        return base

    def test_valid_species_constructs(self):
        species = SeedSpecies(**self._valid_species())
        assert species.zim_path == "seeds/zea-mays"

    def test_germination_rate_above_100_raises(self):
        with pytest.raises(ValueError, match="germination_rate_pct must be 0.0–100.0"):
            SeedSpecies(**self._valid_species(germination_rate_pct=101.0))

    def test_germination_rate_below_0_raises(self):
        with pytest.raises(ValueError, match="germination_rate_pct must be 0.0–100.0"):
            SeedSpecies(**self._valid_species(germination_rate_pct=-1.0))

    def test_germination_rate_zero_valid(self):
        species = SeedSpecies(**self._valid_species(germination_rate_pct=0.0))
        assert species.germination_rate_pct == 0.0

    def test_invalid_difficulty_raises(self):
        with pytest.raises(ValueError, match="seed_saving_difficulty must be easy/moderate/difficult"):
            SeedSpecies(**self._valid_species(seed_saving_difficulty="very_hard"))

    def test_valid_difficulties(self):
        for difficulty in ("easy", "moderate", "difficult"):
            species = SeedSpecies(**self._valid_species(seed_saving_difficulty=difficulty))
            assert species.seed_saving_difficulty == difficulty

    def test_empty_slug_raises(self):
        with pytest.raises(ValueError, match="slug must not be empty"):
            SeedSpecies(**self._valid_species(slug=""))

    def test_all_optional_fields_default_none(self):
        species = SeedSpecies(
            common_name="Corn", latin_binomial="Zea mays",
            family="Poaceae", slug="zea-mays",
        )
        assert species.grin_accession_number is None
        assert species.expected_viability_years is None
        assert species.germination_rate_pct is None


# ---------------------------------------------------------------------------
# FoodSafetyTable tests
# ---------------------------------------------------------------------------

class TestFoodSafetyTable:
    """
    Data integrity tests for the FoodSafetyTable schema.

    These tests are all safety-critical. A bug in food safety processing time
    records can cause botulism — the data_integrity mark ensures they never skip.
    """

    def _valid_table(self, **overrides) -> dict:
        base = dict(
            food_category="tomatoes",
            food_item="Whole or halved tomatoes",
            jar_size="pint",
            processing_method="water_bath",
            processing_time_minutes=35,
            usda_edition="USDA 2015",
            slug="tomatoes-whole-pint-water-bath",
            disclaimer=FOOD_SAFETY_DISCLAIMER,
            additional_minutes_1001_3000ft=5,
            additional_minutes_3001_6000ft=10,
            additional_minutes_above_6000ft=15,
        )
        base.update(overrides)
        return base

    @pytest.mark.data_integrity
    def test_valid_water_bath_record_constructs(self):
        record = FoodSafetyTable(**self._valid_table())
        assert record.zim_path == "food-safety/tomatoes-whole-pint-water-bath"

    @pytest.mark.data_integrity
    def test_valid_pressure_canning_constructs(self):
        record = FoodSafetyTable(
            food_category="low-acid vegetables",
            food_item="Green beans",
            jar_size="pint",
            processing_method="pressure",
            processing_time_minutes=20,
            usda_edition="USDA 2015",
            slug="green-beans-pint-pressure",
            disclaimer=FOOD_SAFETY_DISCLAIMER,
            pressure_psi_0_2000ft=10.0,
            pressure_psi_2001_4000ft=11.0,
            pressure_psi_4001_6000ft=12.0,
            pressure_psi_above_6000ft=13.0,
            botulism_risk_level="high",
            source_page="USDA Guide p.34",
        )
        assert record.processing_time_minutes == 20

    @pytest.mark.data_integrity
    def test_empty_usda_edition_raises(self):
        with pytest.raises(ValueError, match="usda_edition is required"):
            FoodSafetyTable(**self._valid_table(usda_edition=""))

    @pytest.mark.data_integrity
    def test_null_disclaimer_raises(self):
        with pytest.raises(ValueError, match="disclaimer must not be null"):
            FoodSafetyTable(**self._valid_table(disclaimer=""))

    @pytest.mark.data_integrity
    def test_zero_processing_time_raises(self):
        with pytest.raises(ValueError, match="processing_time_minutes must be positive"):
            FoodSafetyTable(**self._valid_table(processing_time_minutes=0))

    @pytest.mark.data_integrity
    def test_negative_processing_time_raises(self):
        with pytest.raises(ValueError, match="processing_time_minutes must be positive"):
            FoodSafetyTable(**self._valid_table(processing_time_minutes=-5))

    def test_invalid_jar_size_raises(self):
        with pytest.raises(ValueError, match="jar_size must be half-pint, pint, or quart"):
            FoodSafetyTable(**self._valid_table(jar_size="gallon"))

    def test_invalid_processing_method_raises(self):
        with pytest.raises(ValueError, match="processing_method must be"):
            FoodSafetyTable(**self._valid_table(processing_method="oven"))

    def test_invalid_botulism_risk_raises(self):
        with pytest.raises(ValueError, match="botulism_risk_level must be high/moderate/low"):
            FoodSafetyTable(**self._valid_table(botulism_risk_level="extreme"))

    def test_valid_jar_sizes(self):
        for jar_size in ("half-pint", "pint", "quart"):
            record = FoodSafetyTable(**self._valid_table(
                jar_size=jar_size,
                slug=f"test-{jar_size}",
            ))
            assert record.jar_size == jar_size

    @pytest.mark.data_integrity
    def test_source_page_optional(self):
        record = FoodSafetyTable(**self._valid_table())
        assert record.source_page is None


# ---------------------------------------------------------------------------
# BotanicalSpecies tests
# ---------------------------------------------------------------------------

class TestBotanicalSpecies:
    """Validation tests for the BotanicalSpecies schema."""

    def _valid_edible(self, **overrides) -> dict:
        base = dict(
            common_name="Elderberry",
            latin_binomial="Sambucus nigra",
            family="Adoxaceae",
            slug="sambucus-nigra",
            edibility_classification="edible_with_preparation",
        )
        base.update(overrides)
        return base

    def _valid_toxic(self, **overrides) -> dict:
        base = dict(
            common_name="Water Hemlock",
            latin_binomial="Cicuta maculata",
            family="Apiaceae",
            slug="cicuta-maculata",
            edibility_classification="toxic",
            toxicity_notes="Highly toxic — cicutoxin causes seizures within 15 min of ingestion.",
            toxicity_source_citation="Kingsbury JM. Poisonous Plants of the US and Canada. p.112",
        )
        base.update(overrides)
        return base

    def test_valid_edible_species_constructs(self):
        species = BotanicalSpecies(**self._valid_edible())
        assert species.zim_path == "botany/sambucus-nigra"

    def test_valid_toxic_species_constructs(self):
        species = BotanicalSpecies(**self._valid_toxic())
        assert species.edibility_classification == "toxic"

    @pytest.mark.data_integrity
    def test_toxic_species_without_toxicity_notes_raises(self):
        with pytest.raises(ValueError, match="toxicity_notes must be set"):
            BotanicalSpecies(
                common_name="Water Hemlock",
                latin_binomial="Cicuta maculata",
                family="Apiaceae",
                slug="cicuta-maculata",
                edibility_classification="toxic",
                toxicity_notes=None,
            )

    @pytest.mark.data_integrity
    def test_toxicity_notes_without_citation_raises(self):
        with pytest.raises(ValueError, match="toxicity_source_citation is required"):
            BotanicalSpecies(
                common_name="Water Hemlock",
                latin_binomial="Cicuta maculata",
                family="Apiaceae",
                slug="cicuta-maculata",
                edibility_classification="toxic",
                toxicity_notes="Highly toxic.",
                toxicity_source_citation=None,
            )

    def test_invalid_edibility_classification_raises(self):
        with pytest.raises(ValueError, match="edibility_classification must be one of"):
            BotanicalSpecies(**self._valid_edible(edibility_classification="maybe_edible"))

    def test_valid_edibility_classifications(self):
        for classification in ("edible", "edible_with_preparation", "toxic", "unknown"):
            species = BotanicalSpecies(**self._valid_edible(
                edibility_classification=classification,
                slug=f"test-{classification.replace('_', '-')}",
                toxicity_notes=("Toxic." if classification == "toxic" else None),
                toxicity_source_citation=("Source." if classification == "toxic" else None),
            ))
            assert species.edibility_classification == classification

    @pytest.mark.data_integrity
    def test_medicinal_evidence_a_without_citation_raises(self):
        with pytest.raises(ValueError, match="medicinal_source_citation is required"):
            BotanicalSpecies(
                **self._valid_edible(),
                medicinal_uses=["Anti-inflammatory"],
                medicinal_evidence_level="A",
                medicinal_source_citation=None,
            )

    @pytest.mark.data_integrity
    def test_medicinal_evidence_b_without_citation_raises(self):
        with pytest.raises(ValueError, match="medicinal_source_citation is required"):
            BotanicalSpecies(
                **self._valid_edible(),
                medicinal_uses=["Antifungal"],
                medicinal_evidence_level="B",
                medicinal_source_citation=None,
            )

    def test_medicinal_evidence_c_without_citation_allowed(self):
        species = BotanicalSpecies(
            **self._valid_edible(),
            medicinal_uses=["Reported mood elevation"],
            medicinal_evidence_level="C",
            medicinal_source_citation=None,
        )
        assert species.medicinal_evidence_level == "C"

    def test_medicinal_uses_without_level_defaults_to_c(self):
        species = BotanicalSpecies(
            **self._valid_edible(),
            medicinal_uses=["Reported anti-inflammatory effects"],
        )
        assert species.medicinal_evidence_level == "C"

    def test_invalid_evidence_level_raises(self):
        with pytest.raises(ValueError, match="medicinal_evidence_level must be A, B, or C"):
            BotanicalSpecies(
                **self._valid_edible(),
                medicinal_uses=["Anti-inflammatory"],
                medicinal_evidence_level="D",
            )

    def test_related_medical_articles_default_empty(self):
        species = BotanicalSpecies(**self._valid_edible())
        assert species.related_medical_articles == []
        assert species.lookalike_species == []

    def test_zim_path_format(self):
        species = BotanicalSpecies(**self._valid_edible(slug="sambucus-nigra"))
        assert species.zim_path == "botany/sambucus-nigra"
