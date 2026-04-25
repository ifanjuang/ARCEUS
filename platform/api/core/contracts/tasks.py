"""Task and workflow contracts for Pantheon OS.

Tasks are explicit, assignable and testable units of work. They are not prompt
fragments. A task must say what it expects, who or what can execute it, which
inputs it consumes and how success is evaluated.
"""

from __future__ import annotations

from enum import StrEnum
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator


class TaskStatus(StrEnum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    BLOCKED = "blocked"
    SKIPPED = "skipped"
    WAITING_APPROVAL = "waiting_approval"


class TaskExecutionMode(StrEnum):
    AGENT = "agent"
    SKILL = "skill"
    ACTION = "action"
    TOOL = "tool"
    WORKFLOW = "workflow"
    MANUAL = "manual"


class TaskCriticity(StrEnum):
    C1 = "C1"
    C2 = "C2"
    C3 = "C3"
    C4 = "C4"
    C5 = "C5"


class TaskDefinition(BaseModel):
    """Definition of one workflow task."""

    model_config = ConfigDict(extra="allow", use_enum_values=True)

    id: str
    description: str
    expected_output: str

    execution_mode: TaskExecutionMode = TaskExecutionMode.AGENT
    assigned_agent: str | None = None
    assigned_role: str | None = None
    assigned_skill: str | None = None
    assigned_action: str | None = None
    assigned_tool: str | None = None
    assigned_workflow: str | None = None

    inputs: list[str] = Field(default_factory=list)
    dependencies: list[str] = Field(default_factory=list)
    tools_allowed: list[str] = Field(default_factory=list)
    memory_scope: str | None = None
    approval_required_if: list[str] = Field(default_factory=list)
    guardrails: list[str] = Field(default_factory=list)
    success_criteria: list[str] = Field(default_factory=list)
    failure_modes: list[str] = Field(default_factory=list)
    output_schema: str | None = None
    criticity: TaskCriticity = TaskCriticity.C1
    tags: list[str] = Field(default_factory=list)

    @field_validator("id", "description", "expected_output")
    @classmethod
    def _required_text(cls, value: str) -> str:
        value = str(value).strip()
        if not value:
            raise ValueError("must not be empty")
        return value

    @model_validator(mode="after")
    def _assignment_matches_execution_mode(self) -> "TaskDefinition":
        assigned_by_mode: dict[TaskExecutionMode, str | None] = {
            TaskExecutionMode.AGENT: self.assigned_agent or self.assigned_role,
            TaskExecutionMode.SKILL: self.assigned_skill,
            TaskExecutionMode.ACTION: self.assigned_action,
            TaskExecutionMode.TOOL: self.assigned_tool,
            TaskExecutionMode.WORKFLOW: self.assigned_workflow,
            TaskExecutionMode.MANUAL: self.assigned_role or self.assigned_agent,
        }
        if assigned_by_mode[self.execution_mode] is None:
            raise ValueError(f"execution_mode '{self.execution_mode}' requires a matching assignment")
        return self

    def is_critical(self) -> bool:
        return self.criticity in {TaskCriticity.C4, TaskCriticity.C5}

    def requires_approval_by_default(self) -> bool:
        return self.is_critical() or bool(self.approval_required_if)


class WorkflowPattern(StrEnum):
    SOLO = "solo"
    PARALLEL = "parallel"
    CASCADE = "cascade"
    ARENA = "arena"
    CREW = "crew"
    FLOW = "flow"
    CONDITIONAL = "conditional"


class WorkflowDefinition(BaseModel):
    """Workflow contract with explicit task list."""

    model_config = ConfigDict(extra="allow", use_enum_values=True)

    id: str
    description: str
    pattern: WorkflowPattern = WorkflowPattern.CASCADE
    version: str = "0.1.0"
    enabled: bool = True
    inputs: list[str] = Field(default_factory=list)
    outputs: list[str] = Field(default_factory=list)
    tasks: list[TaskDefinition] = Field(default_factory=list)
    fallback: str | None = None
    tags: list[str] = Field(default_factory=list)

    @field_validator("id", "description", "version")
    @classmethod
    def _required_text(cls, value: str) -> str:
        value = str(value).strip()
        if not value:
            raise ValueError("must not be empty")
        return value

    @model_validator(mode="after")
    def _task_ids_are_unique_and_dependencies_exist(self) -> "WorkflowDefinition":
        ids = [task.id for task in self.tasks]
        duplicate_ids = {task_id for task_id in ids if ids.count(task_id) > 1}
        if duplicate_ids:
            raise ValueError(f"duplicate task ids: {sorted(duplicate_ids)}")

        known_ids = set(ids)
        missing_dependencies: dict[str, list[str]] = {}
        for task in self.tasks:
            missing = [dep for dep in task.dependencies if dep not in known_ids]
            if missing:
                missing_dependencies[task.id] = missing
        if missing_dependencies:
            raise ValueError(f"unknown task dependencies: {missing_dependencies}")

        return self

    def critical_tasks(self) -> list[TaskDefinition]:
        return [task for task in self.tasks if task.is_critical()]

    def task_map(self) -> dict[str, TaskDefinition]:
        return {task.id: task for task in self.tasks}


def load_workflow_definition(raw: dict[str, Any]) -> WorkflowDefinition:
    """Parse a workflow definition from YAML-compatible data."""
    if not isinstance(raw, dict):
        raise TypeError("workflow definition must be an object")
    return WorkflowDefinition.model_validate(raw)
