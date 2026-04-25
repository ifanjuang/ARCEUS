"""Approval Gate schemas."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Any
from uuid import UUID

from pydantic import BaseModel, Field, field_validator


class ApprovalStatus(StrEnum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    EXPIRED = "expired"
    ESCALATED = "escalated"
    CANCELLED = "cancelled"


class ApprovalDecision(StrEnum):
    APPROVED = "approved"
    REJECTED = "rejected"


class ApprovalCreate(BaseModel):
    run_id: str | None = None
    workflow_id: str | None = None
    agent_id: str | None = None
    action_type: str
    action_description: str
    agent_reasoning: str = ""
    criticity: str = "C3"
    reversibility: str = "unknown"
    assignee: str | None = None
    assignee_type: str | None = None
    escalate_to: str | None = None
    timeout_at: datetime | None = None
    payload: dict[str, Any] = Field(default_factory=dict)

    @field_validator("action_type", "action_description", "criticity", "reversibility")
    @classmethod
    def _required_text(cls, value: str) -> str:
        value = str(value).strip()
        if not value:
            raise ValueError("must not be empty")
        return value


class ApprovalDecisionRequest(BaseModel):
    decision: ApprovalDecision
    decision_note: str | None = None


class ApprovalResponse(BaseModel):
    id: UUID
    run_id: str | None
    workflow_id: str | None
    agent_id: str | None
    action_type: str
    action_description: str
    agent_reasoning: str
    criticity: str
    reversibility: str
    assignee: str | None
    assignee_type: str | None
    escalate_to: str | None
    status: ApprovalStatus
    decided_by: str | None
    decision_note: str | None
    payload: dict[str, Any]
    created_at: datetime
    decided_at: datetime | None
    timeout_at: datetime | None

    model_config = {"from_attributes": True}
