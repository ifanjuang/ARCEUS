# Changelog

Toutes les évolutions notables de Pantheon OS doivent être consignées ici.

Le projet suit SemVer : `MAJOR.MINOR.PATCH`.

---

## 0.5.0-alpha.1 — 2026-04-26

### Added

- Audit initial documentation / code dans `CODE_AUDIT.md`.
- `ManifestLoader` runtime tolérant pour agents, skills et workflows.
- Contrat manifest progressif `ComponentManifest`.
- Contrats `TaskDefinition` et `WorkflowDefinition`.
- Loader `workflow.yaml` / `tasks.yaml`.
- Workflow réel `document_analysis`.
- Endpoint debug `/debug/runtime-registry`.
- Module Approval Gate minimal, désactivé par défaut.
- Migration `approval_requests`.
- Installer UI autonome pour NAS + Ollama LAN.
- Script Windows pour préparer Ollama.
- `VERSION`, `CHANGELOG.md`, `VERSIONS.md`, `EXTERNAL_WATCHLIST.md`.

### Changed

- `platform/api/main.py` charge désormais les registries runtime et les workflow definitions au startup.
- `ModuleRegistry` normalise les manifests API via le contrat commun.
- `STATUS.md` distingue plus précisément les états : livré, partiel, désactivé, à vérifier.

### Known issues

- La migration Approval Gate contient `down_revision = None` et doit être vérifiée localement avec `alembic heads`.
- Le module `approvals` reste désactivé tant que migration et tests ne sont pas validés.
- L’Installer UI est ajoutée mais non testée sur NAS dans cette session.
- Les workflows sont chargés et exposés, mais pas encore connectés à un moteur d’exécution.
- Les traces `task_run` et `approval_event` ne sont pas encore implémentées.
