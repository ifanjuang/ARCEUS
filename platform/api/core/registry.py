"""
ModuleRegistry — auto-discovery et chargement des modules API.
main.py ne connaît aucun module : tout passe par registry.load_all().
"""

import importlib
from pathlib import Path

import yaml
from fastapi import FastAPI
from pydantic import ValidationError

from core.contracts.manifest import ComponentManifest, normalize_manifest
from core.logging import get_logger

log = get_logger("registry")

# Instance globale accessible depuis health.py et les modules
registry: "ModuleRegistry | None" = None


class ModuleRegistry:
    def __init__(self, app: FastAPI):
        self.app = app
        self._modules: dict[str, dict] = {}

    def load_all(self, modules_yaml: str = "modules.yaml") -> None:
        """Charge tous les modules activés dans modules.yaml."""
        global registry
        registry = self

        config_path = Path(modules_yaml)
        if not config_path.exists():
            log.warning("registry.modules_yaml_not_found", path=modules_yaml)
            return

        config = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
        for entry in config.get("modules", []):
            if entry.get("enabled", True):
                try:
                    self._load_module(entry["name"])
                except Exception as e:  # noqa: BLE001 - registry should keep loading other modules
                    log.error("registry.load_failed", module=entry["name"], error=str(e))

    def _load_module(self, name: str) -> None:
        base = Path(f"apps/{name}")
        if not base.exists():
            log.warning("registry.module_dir_missing", module=name, path=str(base))
            return

        manifest_path = base / "manifest.yaml"
        if not manifest_path.exists():
            log.warning("registry.manifest_missing", module=name)
            return

        raw_manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8")) or {}
        try:
            manifest_model = normalize_manifest(raw_manifest, fallback_id=name, default_type="api_app")
        except ValidationError as exc:
            log.error("registry.manifest_invalid", module=name, path=str(manifest_path), error=str(exc))
            return

        for issue in manifest_model.issues():
            log.warning(
                "registry.manifest_quality_issue",
                module=name,
                field=issue.field,
                severity=issue.severity,
                message=issue.message,
            )

        manifest = manifest_model.model_dump(mode="json")
        config_path = base / "config.yaml"
        config = yaml.safe_load(config_path.read_text(encoding="utf-8")) if config_path.exists() else {}

        # Vérifier que les dépendances sont chargées
        for dep in manifest_model.dependencies:
            if dep not in self._modules:
                raise RuntimeError(
                    f"Module '{name}' requiert '{dep}' qui n'est pas encore chargé. Vérifier l'ordre dans modules.yaml."
                )

        if not manifest_model.prefix:
            log.error("registry.manifest_missing_prefix", module=name)
            return

        # Charger le router du module
        try:
            mod = importlib.import_module(f"apps.{name}.router")
            router = mod.get_router(config)
            self.app.include_router(
                router,
                prefix=manifest_model.prefix,
                tags=[name],
            )
        except (ImportError, AttributeError) as e:
            log.error("registry.router_load_failed", module=name, error=str(e))
            return

        self._modules[name] = {"manifest": manifest, "config": config, "manifest_model": manifest_model}
        log.info("registry.module_loaded", module=name, prefix=manifest_model.prefix)

    def is_enabled(self, name: str) -> bool:
        return name in self._modules

    def get_config(self, name: str) -> dict:
        return self._modules.get(name, {}).get("config", {})

    def get_manifest(self, name: str) -> dict:
        return self._modules.get(name, {}).get("manifest", {})

    def get_manifest_model(self, name: str) -> ComponentManifest | None:
        return self._modules.get(name, {}).get("manifest_model")

    def get_all_behaviors(self) -> str:
        """Retourne les behaviors de tous les modules chargés, concaténés.

        Utilisé par Zeus pour injecter les contraintes métier actives dans son
        contexte de planification sans modifier les SOUL.md des agents.
        """
        parts = []
        for name, data in self._modules.items():
            behavior = data["manifest"].get("behavior", "").strip()
            if behavior:
                parts.append(f"[{name}]\n{behavior}")
        return "\n\n".join(parts)

    @property
    def loaded_modules(self) -> list[str]:
        return list(self._modules.keys())
