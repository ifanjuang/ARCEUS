# AI LOG ENTRY — 2026-05-11

Branch: `work/claude/openwebui-hermes-specs`

A: Claude

## Objective

Bloc 7 (original) du plan de stabilisation Pantheon Next. Rédiger 4 specs OpenWebUI / Hermes **sans activation**, en vérifiant la doc officielle Hermes Agent (Nous Research) et OpenWebUI avant toute écriture technique. Aucun runtime ajouté, aucun Function/Pipe/Filter/Action installé, aucun skill Hermes activé, aucun `docker-compose.yml` / `.env` modifié, aucun Hermes Dashboard exposé.

## Vérification de la doc officielle (obligation du brief)

La sandbox bloque `docs.openwebui.com` et `nousresearch.com` (403 `host_not_allowed`). En revanche `raw.githubusercontent.com` est accessible. J'ai donc récupéré directement les README canoniques :

| Source vérifiée | Méthode | Faits cités dans les specs |
|---|---|---|
| `open-webui/open-webui` README (main) | `curl -s raw.githubusercontent.com/.../README.md` | Native Python Function Calling Tool, Pipelines Plugin Framework comme système séparé |
| `open-webui/pipelines` README (main) | `curl -s raw.githubusercontent.com/.../README.md` | Pipelines = "UI-Agnostic OpenAI API Plugin Framework", port `9099`, image `ghcr.io/open-webui/pipelines:main`, warning "**arbitrary code execution — don't fetch random pipelines**" |
| `NousResearch/hermes-agent` README (main) | `curl -s raw.githubusercontent.com/.../README.md` | CLI : `hermes`, `hermes model`, `hermes tools`, `hermes config set`, `hermes gateway`, `hermes setup`, `hermes claw migrate`, `hermes update`, `hermes doctor`. Install paths : `~/.hermes` (Linux/macOS), `%LOCALAPPDATA%\hermes` (Windows). Docs URL: `https://hermes-agent.nousresearch.com/docs/`. Terminal backends: local, Docker, SSH, Singularity, Modal, Daytona, Vercel Sandbox |
| `NousResearch/Hermes-Function-Calling` README (main) | `curl -s raw.githubusercontent.com/.../README.md` | Repo distinct, fine-tune function-calling, hors core Pantheon |

Aucune valeur n'a été inventée. Lorsque le brief impose un point dépendant de la version live (e.g., transport bridge, dashboard URL), la spec marque explicitement **À vérifier**.

## Changes

- `operations/openwebui_router_pipe_spec.md` (nouveau) — spec du Router Pipe :
  - vocabulaire vérifié contre `OPENWEBUI_PLUGIN_POLICY.md` (Pipe / Filter / Action / Tool) et `open-webui/pipelines` upstream ;
  - placement architectural : Pipe consomme `GET /runtime/context-pack`, `/domain/snapshot`, `POST /domain/approval/classify`, jamais OpenAI-compatible vers Pantheon ;
  - choix Pipe natif vs Pipelines framework explicitement **À vérifier** ;
  - bindings obligatoires : approval, Task Contract, Evidence Pack, Role Signal traceability, forbidden endpoints, legacy endpoints (PR #146), model routing, approval state.
- `operations/openwebui_actions_spec.md` (nouveau) — spec des Actions :
  - set Pantheon-aligné aligné sur `OPENWEBUI_PLUGIN_POLICY.md §"Recommended Pantheon OpenWebUI components"` (Evidence Pack display, Approval request, Approve / Reject candidate, Hermes rerun, Source formatting, Pantheon boundary reminder) ;
  - chaque Action carrie son status (Documenté / Candidate only / Non implémenté / Interdit pour core) ;
  - forbidden Action behaviour explicité (no canonization, no legacy endpoint, no Hermes execution sans Task Contract) ;
  - lifecycle 8 étapes avant promotion ; aucune Action installée.
- `operations/hermes_context_pack_verification.md` (nouveau) — checklist de vérification du Context Pack :
  - `GET /runtime/context-pack` cité depuis `HERMES_INTEGRATION.md §7` (verbatim) ;
  - procédure `curl` opérateur uniquement, pas d'invocation Hermes, pas de container démarré ;
  - couverture test : `tests/test_api_smoke.py::test_context_pack_endpoint`, `tests/test_governance_api.py` (Bloc 5) ;
  - mention explicite des paths Hermes (`~/.hermes`, `%LOCALAPPDATA%\hermes`) et de la doc URL upstream sans inviter à installer.
- `operations/hermes_task_contract_bridge_spec.md` (nouveau) — spec Bridge Pantheon ↔ Hermes :
  - schéma YAML `task_contract_dispatch` avec `transport: spec_only` et note **À vérifier** sur le choix CLI / HTTP / MCP ;
  - liste explicite des signaux qui pausent ou révisent le contrat (`workflow_revision_signal`, `veto_signal`, `stop_gate_signal`, `risk_warning`, `source_gap_signal`, `skill_gap_signal`, `handoff_signal`, `clarification_request`) ;
  - chaque ligne du spec mapped au schéma de Bloc 4 (`task_contract.schema.yaml`, `task_contract_revision.schema.yaml`, `evidence_pack.schema.yaml`) ;
  - Doctor cited : `forbidden_endpoints_absent` + `legacy_runtime_surfaces_absent` (PR #146).
- `ai_logs/2026-05-11-openwebui-hermes-specs.md` (cette entrée).

## Files Touched

- operations/openwebui_router_pipe_spec.md (nouveau)
- operations/openwebui_actions_spec.md (nouveau)
- operations/hermes_context_pack_verification.md (nouveau)
- operations/hermes_task_contract_bridge_spec.md (nouveau)
- ai_logs/2026-05-11-openwebui-hermes-specs.md (nouveau)

## Critical files impacted

Aucun. Pas de modification de :

- `platform/api/*`
- `docs/governance/*`
- `modules.yaml`, `plugins.yaml`
- `docker-compose.yml`, `.env.example`
- `schemas/*`
- `tests/*`
- `operations/doctor.py`, `operations/doctor.md`, `operations/validate_governance.py`
- existing operations files

Aucun endpoint API ajouté ou modifié. Aucun Hermes skill activé. Aucun plugin OpenWebUI installé.

## Tests

Aucun test logique modifié. Les specs sont purement Markdown. Sanity check de régression :

```text
python3 operations/doctor.py --no-write --print     → exit 0, 12 PASS + (1 WARN sur la branche PR #146 uniquement)
                                                       sur main pré-PR #146 : tous les checks PASS

ruff check platform/api/ tests/                      → All checks passed!  (inchangé)
ruff format --check platform/api/ tests/             → unchanged
```

Aucun test ajouté car le scope est strictement documentaire et que les specs ne déclenchent aucune exécution.

## Doctrine respectée

- `OpenWebUI expose. Hermes Agent exécute. Pantheon Next gouverne.`
- Aucun runtime, scheduler, agent loop, message bus, LangGraph central, mémoire auto-promue, plugin batch install, Hermes Dashboard public.
- Aucun Function / Pipe / Filter / Action / Tool / Skill activé. Aucun POST ajouté.
- Aucun secret lu, aucun Docker socket touché, aucun appel réseau réel (seulement `curl` vers `raw.githubusercontent.com` pour vérifier les README, en lecture seule).
- Vocabulaire trié par status (Documenté / À vérifier / Non implémenté / Interdit pour core / Candidate only) comme exigé par le brief.
- Pas de valeur inventée : tout point dépendant d'une version, d'un endpoint live, d'une variable d'env est marqué **À vérifier**.

## Open points

- `docs.openwebui.com` et `nousresearch.com` ne sont pas atteignables depuis la sandbox. Les README GitHub canoniques ont été utilisés comme source de vérité de premier niveau. Une revue par opérateur ayant accès à la doc live des deux projets est recommandée avant toute implémentation.
- Le transport du Bridge Pantheon ↔ Hermes (CLI local, HTTP gateway, MCP) reste **À vérifier** ; aucune option n'est privilégiée par cette PR.
- Aucune des specs n'autorise quoi que ce soit. Les implémentations correspondantes restent **Non implémenté** ou **Candidate only** ; chacune devra ouvrir sa propre PR C3+ avec revue dédiée.

## Next action

- Une fois la PR mergée, une PR `docs:` séparée pourra ajouter ces 4 specs à l'index `docs/governance/README.md` ou à `STATUS.md` si l'orchestration souhaite les rendre visibles côté gouvernance (hors scope ici).
- Optionnellement, faire un `hermes doctor` côté opérateur installé, après revue, pour valider la procédure de vérification décrite dans `hermes_context_pack_verification.md` §3.
- Le plan de stabilisation Bloc 1-7 du brief initial est désormais couvert (voir PRs #130, #132, #135, #141, #142, #143, #144, #146 et cette PR).
