"""HermesRouter — decides which workflow/agents to activate based on intent."""
from typing import Optional


class HermesRouter:
    """Routes incoming requests to the appropriate workflow and agent set."""

    SIMPLE_WORKFLOWS = {"simple_answer", "clarification"}
    RESEARCH_WORKFLOWS = {"research", "document_analysis"}
    BUILD_WORKFLOWS = {"dossier_build", "report_build"}

    @staticmethod
    def route(intent: str, context: Optional[dict] = None) -> dict:
        """Return routing decision: workflow_id + primary agents."""
        context = context or {}

        if intent in ("question", "clarification"):
            return {
                "workflow": "simple_answer",
                "agents": ["HECATE", "HERMES", "KAIROS", "IRIS"],
                "pattern": "cascade",
            }

        if intent in ("research", "search", "find"):
            return {
                "workflow": "research",
                "agents": ["HERMES", "DEMETER", "ARGOS", "PROMETHEUS", "KAIROS"],
                "pattern": "cascade",
            }

        if intent in ("build", "dossier", "document"):
            return {
                "workflow": "dossier_build",
                "agents": ["ATHENA", "HERMES", "ARGOS", "KAIROS", "DAEDALUS"],
                "pattern": "cascade",
            }

        # Default: full research pipeline via Zeus planning
        return {
            "workflow": "research",
            "agents": ["ZEUS", "ATHENA", "HERMES", "ARGOS", "KAIROS", "IRIS"],
            "pattern": "zeus_planned",
        }
