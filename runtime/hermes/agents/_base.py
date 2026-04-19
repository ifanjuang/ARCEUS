"""Base class for all Hermes Runtime agents."""
from pathlib import Path
from typing import ClassVar


class AgentBase:
    """Common contract for every agent — identity != responsibility."""

    agent: ClassVar[str] = ""
    role: ClassVar[str] = ""
    layer: ClassVar[str] = ""
    veto: ClassVar[bool] = False
    enabled: ClassVar[bool] = True

    _soul_dir: ClassVar[Path] = Path()

    @classmethod
    def soul(cls) -> str:
        path = cls._soul_dir / "SOUL.md"
        return path.read_text(encoding="utf-8") if path.exists() else ""

    @classmethod
    def identity(cls) -> dict:
        return {"agent": cls.agent, "role": cls.role, "layer": cls.layer}
