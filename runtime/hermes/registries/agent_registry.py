"""Loads agent registry from config/agents.yaml and manages enabled/disabled state."""
from pathlib import Path
from typing import Optional
import yaml


class AgentRegistry:
    _config_path: Path = Path("config/agents.yaml")
    _registry: dict = {}

    @classmethod
    def load(cls, path: Optional[Path] = None) -> None:
        p = path or cls._config_path
        if not p.exists():
            return
        data = yaml.safe_load(p.read_text())
        cls._registry = data.get("agents", {})

    @classmethod
    def is_enabled(cls, agent_name: str) -> bool:
        entry = cls._registry.get(agent_name.upper(), {})
        return entry.get("enabled", True)

    @classmethod
    def all_agents(cls) -> dict:
        return dict(cls._registry)

    @classmethod
    def toggle(cls, agent_name: str, enabled: bool) -> None:
        name = agent_name.upper()
        if name not in cls._registry:
            cls._registry[name] = {}
        cls._registry[name]["enabled"] = enabled
