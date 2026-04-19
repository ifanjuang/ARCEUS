"""Loads workflow registry from config/workflows.yaml."""
from pathlib import Path
from typing import Optional
import yaml


class WorkflowRegistry:
    _config_path: Path = Path("config/workflows.yaml")
    _registry: dict = {}

    @classmethod
    def load(cls, path: Optional[Path] = None) -> None:
        p = path or cls._config_path
        if not p.exists():
            return
        data = yaml.safe_load(p.read_text())
        cls._registry = {w["id"]: w for w in data.get("workflows", [])}

    @classmethod
    def is_enabled(cls, workflow_id: str) -> bool:
        return cls._registry.get(workflow_id, {}).get("enabled", True)

    @classmethod
    def all_workflows(cls) -> list:
        return list(cls._registry.values())

    @classmethod
    def toggle(cls, workflow_id: str, enabled: bool) -> None:
        if workflow_id not in cls._registry:
            cls._registry[workflow_id] = {"id": workflow_id}
        cls._registry[workflow_id]["enabled"] = enabled
