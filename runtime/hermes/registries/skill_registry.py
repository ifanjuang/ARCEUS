"""Loads skill registry from config/skills.yaml."""
from pathlib import Path
from typing import Optional
import yaml


class SkillRegistry:
    _config_path: Path = Path("config/skills.yaml")
    _registry: dict = {}

    @classmethod
    def load(cls, path: Optional[Path] = None) -> None:
        p = path or cls._config_path
        if not p.exists():
            return
        data = yaml.safe_load(p.read_text())
        cls._registry = {s["id"]: s for s in data.get("skills", [])}

    @classmethod
    def is_enabled(cls, skill_id: str) -> bool:
        return cls._registry.get(skill_id, {}).get("enabled", True)

    @classmethod
    def all_skills(cls) -> list:
        return list(cls._registry.values())

    @classmethod
    def toggle(cls, skill_id: str, enabled: bool) -> None:
        if skill_id not in cls._registry:
            cls._registry[skill_id] = {"id": skill_id}
        cls._registry[skill_id]["enabled"] = enabled
