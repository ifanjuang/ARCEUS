from datetime import datetime, timezone

import pytest
from pydantic import ValidationError

from apps.approvals.models import ApprovalRequest
from apps.approvals.schemas import ApprovalCreate, ApprovalDecision, ApprovalDecisionRequest, ApprovalStatus


def test_approval_create_requires_action_description():
    with pytest.raises(ValidationError):
        ApprovalCreate(
            action_type="external_email",
            action_description="",
        )


def test_approval_create_defaults_are_safe():
    payload = ApprovalCreate(
        action_type="memory_promotion",
        action_description="Promote candidate facts to active memory",
    )

    assert payload.criticity == "C3"
    assert payload.reversibility == "unknown"
    assert payload.payload == {}


def test_approval_decision_accepts_only_approve_or_reject():
    assert ApprovalDecisionRequest(decision="approved").decision == ApprovalDecision.APPROVED
    assert ApprovalDecisionRequest(decision="rejected").decision == ApprovalDecision.REJECTED

    with pytest.raises(ValidationError):
        ApprovalDecisionRequest(decision="expired")


def test_approval_status_contract_contains_runtime_states():
    assert {status.value for status in ApprovalStatus} == {
        "pending",
        "approved",
        "rejected",
        "expired",
        "escalated",
        "cancelled",
    }


def test_approval_model_decidable_states():
    pending = ApprovalRequest(
        action_type="browser_submit",
        action_description="Submit browser form",
        status="pending",
        created_at=datetime.now(timezone.utc),
    )
    escalated = ApprovalRequest(
        action_type="browser_submit",
        action_description="Submit browser form",
        status="escalated",
        created_at=datetime.now(timezone.utc),
    )
    approved = ApprovalRequest(
        action_type="browser_submit",
        action_description="Submit browser form",
        status="approved",
        created_at=datetime.now(timezone.utc),
    )

    assert pending.is_decidable() is True
    assert escalated.is_decidable() is True
    assert approved.is_decidable() is False
