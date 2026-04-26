"""
Unit tests for PipelineEngine.

Covers:
- Sequential step execution and ordering
- Parallel step concurrency (timing proof)
- Dependency ordering (B waits for A)
- Step timeout -> pipeline FAILED
- TRANSFORM step data extraction
- CONDITION step branching
- Missing dependency / circular dependency fallback
"""
from __future__ import annotations

import asyncio
import time
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from agentcore.core.pipeline import PipelineEngine, PipelineStep, StepType
from agentcore.models import PipelineStatus, TaskPipeline


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_pipeline(steps: list[dict], agent_id: str = "test-agent") -> TaskPipeline:
    """Build a minimal TaskPipeline from a list of step dicts."""
    return TaskPipeline(
        agent_id=agent_id,
        session_id="test-session",
        steps=steps,
        context={},
    )


def _transform_step(
    step_id: str,
    source_step: str,
    extract_key: str,
    output_key: str,
    depends_on: list[str] | None = None,
) -> dict:
    return {
        "id": step_id,
        "type": StepType.TRANSFORM.value,
        "config": {
            "source_step": source_step,
            "extract_key": extract_key,
            "output_key": output_key,
        },
        "depends_on": depends_on or [],
    }


def _condition_step(
    step_id: str,
    condition: str,
    true_value: object = "yes",
    false_value: object = "no",
    depends_on: list[str] | None = None,
) -> dict:
    return {
        "id": step_id,
        "type": StepType.CONDITION.value,
        "config": {
            "condition": condition,
            "true_value": true_value,
            "false_value": false_value,
        },
        "depends_on": depends_on or [],
    }


# ---------------------------------------------------------------------------
# Mock agent that records which steps called it and in what order
# ---------------------------------------------------------------------------


class _RecordingAgent:
    """Fake AgentInstance that records call order and timing."""

    def __init__(self, delay: float = 0.0) -> None:
        self._delay = delay
        self.calls: list[str] = []
        self._dispatcher = None

    async def chat(self, message: str, session_id: str, stream: bool = False):
        await asyncio.sleep(self._delay)
        self.calls.append(f"llm:{message}")
        resp = MagicMock()
        resp.message = f"response to: {message}"
        resp.tokens_used = 5
        resp.model = "test-model"
        return resp


# ===========================================================================
# Sequential execution
# ===========================================================================


class TestSequentialExecution:
    @pytest.mark.asyncio
    async def test_single_llm_step_executes(self):
        """A pipeline with one LLM step completes successfully."""
        agent = _RecordingAgent()
        engine = PipelineEngine()
        pipeline = _make_pipeline([
            {
                "id": "step_a",
                "type": StepType.LLM_CALL.value,
                "config": {"prompt_template": "Say hello"},
                "depends_on": [],
            }
        ])
        result = await engine.execute(pipeline, agent)

        assert result.status == PipelineStatus.COMPLETED
        assert len(result.results) == 1
        assert result.results[0]["step_id"] == "step_a"

    @pytest.mark.asyncio
    async def test_sequential_steps_execute_in_order(self):
        """Steps A -> B -> C must execute in that order."""
        agent = _RecordingAgent()
        engine = PipelineEngine()

        pipeline = _make_pipeline([
            {
                "id": "step_a",
                "type": StepType.LLM_CALL.value,
                "config": {"prompt_template": "Step A"},
                "depends_on": [],
            },
            {
                "id": "step_b",
                "type": StepType.LLM_CALL.value,
                "config": {"prompt_template": "Step B"},
                "depends_on": ["step_a"],
            },
            {
                "id": "step_c",
                "type": StepType.LLM_CALL.value,
                "config": {"prompt_template": "Step C"},
                "depends_on": ["step_b"],
            },
        ])
        result = await engine.execute(pipeline, agent)

        assert result.status == PipelineStatus.COMPLETED
        step_ids = [r["step_id"] for r in result.results]
        assert step_ids == ["step_a", "step_b", "step_c"]

    @pytest.mark.asyncio
    async def test_dependency_order_respected(self):
        """Step B that depends_on Step A must run after A, even if B appears first in list."""
        agent = _RecordingAgent()
        engine = PipelineEngine()

        pipeline = _make_pipeline([
            # B listed first — should still run after A
            {
                "id": "step_b",
                "type": StepType.LLM_CALL.value,
                "config": {"prompt_template": "B"},
                "depends_on": ["step_a"],
            },
            {
                "id": "step_a",
                "type": StepType.LLM_CALL.value,
                "config": {"prompt_template": "A"},
                "depends_on": [],
            },
        ])
        result = await engine.execute(pipeline, agent)

        assert result.status == PipelineStatus.COMPLETED
        step_ids = [r["step_id"] for r in result.results]
        assert step_ids.index("step_a") < step_ids.index("step_b")


# ===========================================================================
# Parallel execution
# ===========================================================================


class TestParallelExecution:
    @pytest.mark.asyncio
    async def test_independent_steps_execute_concurrently(self):
        """Two independent steps (no depends_on) should run concurrently, not sequentially."""
        # Each step takes 0.15 s. Sequential = ~0.30 s. Parallel = ~0.15 s.
        STEP_DELAY = 0.15
        TOLERANCE = 0.10

        agent = _RecordingAgent(delay=STEP_DELAY)
        engine = PipelineEngine()

        pipeline = _make_pipeline([
            {
                "id": "step_x",
                "type": StepType.LLM_CALL.value,
                "config": {"prompt_template": "X"},
                "depends_on": [],
            },
            {
                "id": "step_y",
                "type": StepType.LLM_CALL.value,
                "config": {"prompt_template": "Y"},
                "depends_on": [],
            },
        ])

        start = time.monotonic()
        result = await engine.execute(pipeline, agent)
        elapsed = time.monotonic() - start

        assert result.status == PipelineStatus.COMPLETED
        # Elapsed should be close to one step delay (parallel), not two (sequential)
        assert elapsed < STEP_DELAY * 2 - TOLERANCE, (
            f"Steps appeared to run sequentially: elapsed={elapsed:.3f}s "
            f"(expected < {STEP_DELAY * 2 - TOLERANCE:.3f}s)"
        )

    @pytest.mark.asyncio
    async def test_parallel_batch_all_results_recorded(self):
        """All results from a parallel batch must appear in pipeline.results."""
        agent = _RecordingAgent()
        engine = PipelineEngine()

        pipeline = _make_pipeline([
            {
                "id": f"step_{i}",
                "type": StepType.LLM_CALL.value,
                "config": {"prompt_template": f"Step {i}"},
                "depends_on": [],
            }
            for i in range(4)
        ])
        result = await engine.execute(pipeline, agent)

        assert result.status == PipelineStatus.COMPLETED
        recorded_ids = {r["step_id"] for r in result.results}
        assert recorded_ids == {"step_0", "step_1", "step_2", "step_3"}


# ===========================================================================
# Timeouts
# ===========================================================================


class TestStepTimeout:
    @pytest.mark.asyncio
    async def test_step_timeout_marks_pipeline_failed(self):
        """A step that exceeds its timeout must cause PipelineStatus.FAILED."""

        async def _slow_chat(message, session_id, stream=False):
            await asyncio.sleep(999)  # Hangs forever

        agent = MagicMock()
        agent.chat = _slow_chat
        agent._dispatcher = None

        engine = PipelineEngine()
        pipeline = _make_pipeline([
            {
                "id": "step_slow",
                "type": StepType.LLM_CALL.value,
                "config": {"prompt_template": "slow step"},
                "depends_on": [],
                "timeout_seconds": 1,
            }
        ])

        result = await engine.execute(pipeline, agent)
        assert result.status == PipelineStatus.FAILED

    @pytest.mark.asyncio
    async def test_pipeline_error_field_set_on_timeout(self):
        """pipeline.error must be set (not None) when a step times out."""

        async def _slow_chat(message, session_id, stream=False):
            await asyncio.sleep(999)

        agent = MagicMock()
        agent.chat = _slow_chat
        agent._dispatcher = None

        engine = PipelineEngine()
        pipeline = _make_pipeline([
            {
                "id": "step_slow",
                "type": StepType.LLM_CALL.value,
                "config": {"prompt_template": "x"},
                "depends_on": [],
                "timeout_seconds": 1,
            }
        ])
        result = await engine.execute(pipeline, agent)
        assert result.error is not None


# ===========================================================================
# TRANSFORM step
# ===========================================================================


class TestTransformStep:
    @pytest.mark.asyncio
    async def test_transform_extracts_nested_key(self):
        """TRANSFORM step must extract a dot-separated key from the source step's output."""
        agent = _RecordingAgent()
        engine = PipelineEngine()

        pipeline = _make_pipeline([
            {
                "id": "llm_step",
                "type": StepType.LLM_CALL.value,
                "config": {"prompt_template": "give me data"},
                "depends_on": [],
            },
            _transform_step(
                step_id="extract_step",
                source_step="llm_step",
                extract_key="text",
                output_key="extracted_text",
                depends_on=["llm_step"],
            ),
        ])

        result = await engine.execute(pipeline, agent)
        assert result.status == PipelineStatus.COMPLETED

        # The transform step should appear in results
        transform_result = next(
            (r for r in result.results if r["step_id"] == "extract_step"), None
        )
        assert transform_result is not None
        output = transform_result["output"]
        assert "extracted_text" in output

    @pytest.mark.asyncio
    async def test_transform_missing_key_returns_none(self):
        """TRANSFORM with a non-existent key should produce None gracefully, not raise."""
        agent = _RecordingAgent()
        engine = PipelineEngine()

        pipeline = _make_pipeline([
            {
                "id": "llm_step",
                "type": StepType.LLM_CALL.value,
                "config": {"prompt_template": "test"},
                "depends_on": [],
            },
            _transform_step(
                step_id="extract_step",
                source_step="llm_step",
                extract_key="nonexistent.deep.key",
                output_key="result",
                depends_on=["llm_step"],
            ),
        ])
        result = await engine.execute(pipeline, agent)
        assert result.status == PipelineStatus.COMPLETED

        transform_result = next(
            (r for r in result.results if r["step_id"] == "extract_step"), None
        )
        assert transform_result is not None
        # Should be None or empty, not an exception
        assert transform_result["output"].get("result") is None


# ===========================================================================
# CONDITION step
# ===========================================================================


class TestConditionStep:
    @pytest.mark.asyncio
    async def test_condition_true_branch(self):
        """A true condition should set branch='true' and the true_value."""
        agent = _RecordingAgent()
        engine = PipelineEngine()

        # Put a known value in context first
        pipeline = _make_pipeline([
            _condition_step(
                "cond_step",
                condition="True",
                true_value="went_true",
                false_value="went_false",
            )
        ])
        result = await engine.execute(pipeline, agent)
        assert result.status == PipelineStatus.COMPLETED
        cond = next(r for r in result.results if r["step_id"] == "cond_step")
        assert cond["output"]["branch"] == "true"
        assert cond["output"]["value"] == "went_true"

    @pytest.mark.asyncio
    async def test_condition_false_branch(self):
        """A false condition should set branch='false' and the false_value."""
        agent = _RecordingAgent()
        engine = PipelineEngine()

        pipeline = _make_pipeline([
            _condition_step(
                "cond_step",
                condition="False",
                true_value="went_true",
                false_value="went_false",
            )
        ])
        result = await engine.execute(pipeline, agent)
        assert result.status == PipelineStatus.COMPLETED
        cond = next(r for r in result.results if r["step_id"] == "cond_step")
        assert cond["output"]["branch"] == "false"
        assert cond["output"]["value"] == "went_false"

    @pytest.mark.asyncio
    async def test_invalid_condition_returns_false_branch(self):
        """An unresolvable condition expression should gracefully return false branch."""
        agent = _RecordingAgent()
        engine = PipelineEngine()

        pipeline = _make_pipeline([
            _condition_step(
                "cond_step",
                condition="undefined_var > 5",
                true_value="yes",
                false_value="no",
            )
        ])
        result = await engine.execute(pipeline, agent)
        # Should not fail the whole pipeline
        assert result.status == PipelineStatus.COMPLETED
        cond = next(r for r in result.results if r["step_id"] == "cond_step")
        assert cond["output"]["branch"] == "false"


# ===========================================================================
# Dependency resolution edge cases
# ===========================================================================


class TestDependencyResolution:
    def test_topological_sort_linear_chain(self):
        """A -> B -> C linear chain must produce three sequential batches."""
        engine = PipelineEngine()
        steps = [
            PipelineStep(id="a", type=StepType.TRANSFORM, depends_on=[]),
            PipelineStep(id="b", type=StepType.TRANSFORM, depends_on=["a"]),
            PipelineStep(id="c", type=StepType.TRANSFORM, depends_on=["b"]),
        ]
        batches = engine._resolve_order(steps)
        assert len(batches) == 3
        assert batches[0][0].id == "a"
        assert batches[1][0].id == "b"
        assert batches[2][0].id == "c"

    def test_topological_sort_fan_out(self):
        """A -> (B, C, D) fan-out must put B, C, D in the same batch."""
        engine = PipelineEngine()
        steps = [
            PipelineStep(id="a", type=StepType.TRANSFORM, depends_on=[]),
            PipelineStep(id="b", type=StepType.TRANSFORM, depends_on=["a"]),
            PipelineStep(id="c", type=StepType.TRANSFORM, depends_on=["a"]),
            PipelineStep(id="d", type=StepType.TRANSFORM, depends_on=["a"]),
        ]
        batches = engine._resolve_order(steps)
        assert len(batches) == 2
        assert batches[0][0].id == "a"
        batch_two_ids = {s.id for s in batches[1]}
        assert batch_two_ids == {"b", "c", "d"}

    def test_no_deadlock_with_missing_dependency(self):
        """If a dep is missing, the engine must not hang — it should force-progress."""
        engine = PipelineEngine()
        steps = [
            PipelineStep(id="b", type=StepType.TRANSFORM, depends_on=["missing_dep"]),
        ]
        # Should not raise or loop forever
        batches = engine._resolve_order(steps)
        assert len(batches) == 1
        assert batches[0][0].id == "b"
