"""
Multi-step task pipeline engine for AgentCore.

Each step can:
- Call the LLM with a specific prompt
- Dispatch a registered tool
- Transform / reshape data in-process
- Branch conditionally based on previous step output
- Fan-out to sub-steps concurrently (PARALLEL type)

Simple tasks are designed to complete in under 3 seconds.
Complex pipelines run asynchronously and update the pipeline record via the registry.
"""
from __future__ import annotations

import ast
import asyncio
import logging
import operator
import time
from datetime import datetime, timezone
from enum import Enum
from typing import TYPE_CHECKING, Any

from pydantic import BaseModel

from agentcore.models import PipelineStatus, TaskPipeline

if TYPE_CHECKING:
    from agentcore.core.agent import AgentInstance

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Step model
# ---------------------------------------------------------------------------


class StepType(str, Enum):
    LLM_CALL = "llm"
    TOOL_CALL = "tool"
    TRANSFORM = "transform"
    CONDITION = "condition"
    PARALLEL = "parallel"  # fan-out: sub-steps run concurrently


class PipelineStep(BaseModel):
    """Definition of a single pipeline step."""

    id: str
    type: StepType
    config: dict[str, Any] = {}
    depends_on: list[str] = []
    timeout_seconds: int = 30


# ---------------------------------------------------------------------------
# Safe condition evaluator
# ---------------------------------------------------------------------------

# Mapping from AST comparison operator nodes to callables
_CMP_OPS: dict[type, Any] = {
    ast.Eq: operator.eq,
    ast.NotEq: operator.ne,
    ast.Lt: operator.lt,
    ast.LtE: operator.le,
    ast.Gt: operator.gt,
    ast.GtE: operator.ge,
}

# AST node types that are unconditionally allowed
_ALLOWED_NODES = (
    ast.Expression,
    ast.BoolOp,
    ast.And,
    ast.Or,
    ast.UnaryOp,
    ast.Not,
    ast.Compare,
    ast.Name,
    ast.Constant,
    # Comparison operator sentinel nodes
    ast.Eq,
    ast.NotEq,
    ast.Lt,
    ast.LtE,
    ast.Gt,
    ast.GtE,
)


def _safe_eval_condition(expression: str, context: dict[str, Any]) -> bool:
    """
    Parse *expression* with the ``ast`` module and evaluate it safely.

    Allowed constructs:
    - Variable lookups resolved from *context*
    - Comparison operators: ==, !=, <, >, <=, >=
    - Boolean operators: and, or, not
    - String, number, and bool literals

    Raises:
        ValueError: if the expression contains any disallowed AST node type.
    """
    try:
        tree = ast.parse(expression, mode="eval")
    except SyntaxError as exc:
        raise ValueError(f"Invalid condition syntax: {exc}") from exc

    # Walk every node and reject anything not in the allow-list
    for node in ast.walk(tree):
        if not isinstance(node, _ALLOWED_NODES):
            raise ValueError(
                f"Disallowed expression node type '{type(node).__name__}' "
                f"in condition: {expression!r}"
            )

    return bool(_eval_node(tree.body, context))


def _eval_node(node: ast.expr, context: dict[str, Any]) -> Any:
    """Recursively evaluate a pre-validated AST node."""
    if isinstance(node, ast.Constant):
        return node.value

    if isinstance(node, ast.Name):
        try:
            return context[node.id]
        except KeyError:
            raise ValueError(f"Unknown variable in condition: '{node.id}'")

    if isinstance(node, ast.BoolOp):
        values = [_eval_node(v, context) for v in node.values]
        if isinstance(node.op, ast.And):
            result = True
            for v in values:
                result = result and v
            return result
        else:  # ast.Or
            result = False
            for v in values:
                result = result or v
            return result

    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Not):
        return not _eval_node(node.operand, context)

    if isinstance(node, ast.Compare):
        left = _eval_node(node.left, context)
        for op, comparator in zip(node.ops, node.comparators):
            right = _eval_node(comparator, context)
            op_fn = _CMP_OPS.get(type(op))
            if op_fn is None:
                raise ValueError(f"Unsupported comparison operator: {type(op).__name__}")
            if not op_fn(left, right):
                return False
            left = right
        return True

    raise ValueError(f"Unexpected node type during evaluation: {type(node).__name__}")


# ---------------------------------------------------------------------------
# Engine
# ---------------------------------------------------------------------------


class PipelineEngine:
    """
    Executes a TaskPipeline by resolving the dependency graph, parallelising
    independent steps, and sequencing dependent ones.
    """

    async def execute(self, pipeline: TaskPipeline, agent: AgentInstance) -> TaskPipeline:
        """
        Execute all pipeline steps in dependency order, parallelising where safe.

        Returns the mutated pipeline with results, status, and timing set.
        """
        pipeline.status = PipelineStatus.RUNNING
        context: dict[str, Any] = dict(pipeline.context)

        try:
            # Parse steps from raw dicts into PipelineStep objects
            steps = [PipelineStep(**s) for s in pipeline.steps]
            execution_order = self._resolve_order(steps)

            for batch in execution_order:
                if len(batch) == 1:
                    step = batch[0]
                    result = await asyncio.wait_for(
                        self._execute_step(step, context, agent),
                        timeout=step.timeout_seconds,
                    )
                    context[step.id] = result
                    pipeline.results.append({"step_id": step.id, "output": result})
                else:
                    # Parallel batch — run all concurrently
                    tasks = [
                        asyncio.wait_for(
                            self._execute_step(s, context, agent),
                            timeout=s.timeout_seconds,
                        )
                        for s in batch
                    ]
                    batch_results = await asyncio.gather(*tasks, return_exceptions=True)
                    for step, result in zip(batch, batch_results):
                        if isinstance(result, Exception):
                            logger.error("Parallel step %s failed: %s", step.id, result)
                            context[step.id] = {"error": str(result)}
                        else:
                            context[step.id] = result
                        pipeline.results.append(
                            {
                                "step_id": step.id,
                                "output": context[step.id],
                            }
                        )

            pipeline.status = PipelineStatus.COMPLETED
            pipeline.context = context  # write enriched context back

        except asyncio.TimeoutError as exc:
            pipeline.status = PipelineStatus.FAILED
            pipeline.error = f"Pipeline timed out: {exc}"
            logger.error("Pipeline %s timed out", pipeline.id)
        except Exception as exc:
            pipeline.status = PipelineStatus.FAILED
            pipeline.error = str(exc)
            logger.exception("Pipeline %s failed: %s", pipeline.id, exc)
        finally:
            pipeline.completed_at = datetime.now(timezone.utc)

        return pipeline

    # ------------------------------------------------------------------
    # Step execution
    # ------------------------------------------------------------------

    async def _execute_step(
        self, step: PipelineStep, context: dict[str, Any], agent: AgentInstance
    ) -> Any:
        """Dispatch to the correct handler based on step type."""
        start = time.monotonic()
        logger.debug("Executing step %s (type=%s)", step.id, step.type)

        try:
            if step.type == StepType.LLM_CALL:
                result = await self._step_llm(step, context, agent)
            elif step.type == StepType.TOOL_CALL:
                result = await self._step_tool(step, context, agent)
            elif step.type == StepType.TRANSFORM:
                result = await self._step_transform(step, context)
            elif step.type == StepType.CONDITION:
                result = await self._step_condition(step, context)
            elif step.type == StepType.PARALLEL:
                result = await self._step_parallel(step, context, agent)
            else:
                raise ValueError(f"Unknown step type: {step.type}")
        finally:
            elapsed = int((time.monotonic() - start) * 1000)
            logger.debug("Step %s completed in %d ms", step.id, elapsed)

        return result

    async def _step_llm(
        self, step: PipelineStep, context: dict[str, Any], agent: AgentInstance
    ) -> dict[str, Any]:
        """
        LLM_CALL step — renders a prompt template against context then calls the agent.
        config:
            prompt_template: str  (may reference {context[key]} values)
            session_id: str       (optional, defaults to pipeline id)
        """
        template: str = step.config.get("prompt_template", "")
        session_id: str = step.config.get("session_id", step.id)

        # Simple template substitution — replace {key} with context[key]
        try:
            prompt = template.format(**context)
        except KeyError:
            prompt = template  # use raw template if substitution fails

        response = await agent.chat(prompt, session_id=session_id, stream=False)
        return {"text": response.message, "tokens_used": response.tokens_used, "model": response.model}

    async def _step_tool(
        self, step: PipelineStep, context: dict[str, Any], agent: AgentInstance
    ) -> dict[str, Any]:
        """
        TOOL_CALL step — dispatches directly to a registered tool.
        config:
            tool_name: str
            arguments: dict  (may contain {key} templates)
        """
        if agent._dispatcher is None:
            return {"error": "No dispatcher configured"}

        tool_name: str = step.config.get("tool_name", "")
        raw_args: dict = step.config.get("arguments", {})

        # Resolve any template values in arguments
        resolved_args: dict[str, Any] = {}
        for k, v in raw_args.items():
            if isinstance(v, str):
                try:
                    resolved_args[k] = v.format(**context)
                except KeyError:
                    resolved_args[k] = v
            else:
                resolved_args[k] = v

        result = await agent._dispatcher.dispatch(tool_name, resolved_args)
        return result

    async def _step_transform(
        self, step: PipelineStep, context: dict[str, Any]
    ) -> dict[str, Any]:
        """
        TRANSFORM step — extracts, reshapes, or maps data within the context.
        config:
            source_step: str       (step id whose output to transform)
            extract_key: str       (dot-separated key path in the source output)
            output_key: str        (key to write result under in context)
        """
        source_step_id: str = step.config.get("source_step", "")
        extract_key: str = step.config.get("extract_key", "")
        output_key: str = step.config.get("output_key", "result")

        source = context.get(source_step_id, {})

        # Navigate dot-separated key path
        value: Any = source
        if extract_key:
            for part in extract_key.split("."):
                if isinstance(value, dict):
                    value = value.get(part)
                else:
                    value = None
                    break

        return {output_key: value}

    async def _step_condition(
        self, step: PipelineStep, context: dict[str, Any]
    ) -> dict[str, Any]:
        """
        CONDITION step — evaluates a simple expression and sets a branch result.
        config:
            condition: str   (expression evaluated safely against context)
            true_value: Any
            false_value: Any

        The condition expression supports:
        - Variable lookups from the context dict
        - Comparison operators: ==, !=, <, >, <=, >=
        - Boolean operators: and, or, not
        - String, number, and bool literals
        Any other AST node type raises ValueError.
        """
        condition: str = step.config.get("condition", "True")
        true_value: Any = step.config.get("true_value", True)
        false_value: Any = step.config.get("false_value", False)

        try:
            result = _safe_eval_condition(condition, context)
            return {"branch": "true" if result else "false", "value": true_value if result else false_value}
        except Exception as exc:
            logger.warning("Condition evaluation failed: %s", exc)
            return {"branch": "false", "value": false_value, "error": str(exc)}

    async def _step_parallel(
        self, step: PipelineStep, context: dict[str, Any], agent: AgentInstance
    ) -> dict[str, Any]:
        """
        PARALLEL step — runs a list of sub-steps concurrently.
        config:
            sub_steps: list[dict]  (list of PipelineStep dicts)
        """
        raw_sub_steps: list[dict] = step.config.get("sub_steps", [])
        sub_steps = [PipelineStep(**s) for s in raw_sub_steps]

        tasks = [
            asyncio.wait_for(
                self._execute_step(sub, context, agent),
                timeout=sub.timeout_seconds,
            )
            for sub in sub_steps
        ]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        return {
            sub.id: (str(r) if isinstance(r, Exception) else r)
            for sub, r in zip(sub_steps, results)
        }

    # ------------------------------------------------------------------
    # Dependency resolution
    # ------------------------------------------------------------------

    def _resolve_order(self, steps: list[PipelineStep]) -> list[list[PipelineStep]]:
        """
        Topological sort of pipeline steps.
        Returns a list of batches; steps within a batch can run concurrently.
        """
        step_map = {s.id: s for s in steps}
        completed: set[str] = set()
        batches: list[list[PipelineStep]] = []
        remaining = list(steps)

        while remaining:
            # Find all steps whose dependencies are satisfied
            ready = [s for s in remaining if all(dep in completed for dep in s.depends_on)]

            if not ready:
                # Circular dependency or missing dependency — force add first remaining
                logger.error(
                    "Pipeline has unresolvable dependencies. Forcing step: %s",
                    remaining[0].id,
                )
                ready = [remaining[0]]

            batches.append(ready)
            for s in ready:
                completed.add(s.id)
                remaining.remove(s)

        return batches
