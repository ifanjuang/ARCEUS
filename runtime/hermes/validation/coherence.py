"""Check internal coherence of a multi-agent response set."""


def check_coherence(responses: list[dict]) -> dict:
    """Lightweight coherence check: verifies agents didn't produce contradictory verdicts."""
    if not responses:
        return {"coherent": True, "issues": []}

    verdicts = [r.get("verdict") for r in responses if r.get("verdict")]
    issues = []

    if "veto" in verdicts and "approved" in verdicts:
        issues.append("Conflicting veto/approved verdicts detected")

    return {
        "coherent": len(issues) == 0,
        "issues": issues,
    }
