"""SessionState — holds context for a single run/conversation."""
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Optional
import uuid


@dataclass
class SessionState:
    session_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    thread_id: Optional[str] = None
    user_message: str = ""
    intent: Optional[str] = None
    workflow: Optional[str] = None
    agents_used: list[str] = field(default_factory=list)
    clarifications: list[dict] = field(default_factory=list)
    artifacts: list[dict] = field(default_factory=list)
    final_answer: Optional[str] = None
    started_at: datetime = field(default_factory=datetime.utcnow)
    metadata: dict[str, Any] = field(default_factory=dict)

    def add_artifact(self, agent: str, content: Any) -> None:
        self.artifacts.append({
            "agent": agent,
            "content": content,
            "timestamp": datetime.utcnow().isoformat(),
        })
