"""Check if a response has all required fields for a given workflow."""
from typing import Optional


def check_completeness(response: dict, required_fields: Optional[list[str]] = None) -> dict:
    """Returns completeness report for a workflow response."""
    required_fields = required_fields or []
    missing = [f for f in required_fields if not response.get(f)]
    return {
        "complete": len(missing) == 0,
        "missing_fields": missing,
        "completeness_score": 1.0 - (len(missing) / max(len(required_fields), 1)),
    }
