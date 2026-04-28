# Pantheon OS — Project Status

> Source de vérité sur l’état actuel du projet après pivot architectural.
> Les fichiers Markdown de référence pilotent le développement : `README.md`, `ARCHITECTURE.md`, `MODULES.md`, `AGENTS.md`, `MEMORY.md`, `ROADMAP.md`, `STATUS.md`.

Dernière mise à jour : 2026-04-27

---

# 1. Décision structurante

Statut : ✅ Décision documentaire actée.

Pantheon OS adopte une trajectoire Hermes-backed.

```text
OpenWebUI = interface chat + knowledge documentaire
Hermes Agent = runtime agentique + skills + tools + scheduler + gateway + mémoire opérationnelle
Pantheon OS = Domain Operating Layer + agents abstraits + domain packages + workflows + skills contracts + mémoire validée + gouvernance
```

Formule de conception :

```text
Pantheon définit.
Hermes exécute.
OpenWebUI expose et retrouve.
```

---

# 2. État global

| Élément | Statut | Commentaire |
|---|---|---|
| Pivot Hermes-backed | ✅ Fait | Direction validée : Pantheon Domain Layer + Hermes + OpenWebUI |
| README produit | ✅ Aligné | Version simplifiée, non redondante avec `MODULES.md` |
| MODULES.md | ✅ Aligné | Domain packages, triage, naming, privacy, lifecycle, XP |
| ARCHITECTURE.md | ✅ Aligné Hermes | Tient compte des concepts Hermes : AIAgent loop, prompt assembly, provider runtime, tool registry, session storage, gateways, cron, optional skills |
| Hermes skill policy | ✅ Créée | `hermes/skill_policy.md` ajouté |
| AGENTS.md | 🔄 À mettre à jour | Panthéon étendu validé conceptuellement ; agents abstraits, non métier |
| MEMORY.md | ⬜ À créer | Nouveau fichier de référence : session / candidates / project / system |
| Branche code post-pivot | ✅ Créée | `work/chatgpt/hermes-code-rewrite` |
| PR draft | ✅ Ouverte | PR #50 : `WIP: rewrite API around Hermes-backed domain layer` |
| Nouvelle API Domain Layer | ✅ Première passe | `platform/api/pantheon_domain/*` + `platform/api/main.py` |
| Ancien runtime autonome | ⚠️ Legacy non supprimé | Conservé dans le repo, mais plus booté par défaut dans la nouvelle entrée API |
| Tests Domain Layer | 🔄 Écrits, non exécutés ici | `tests/test_domain_layer_api.py` ajouté, exécution locale/CI à faire |
| Hermes Agent | ⬜ Non installé | À tester plus tard en Hermes Lab isolé |
| OpenWebUI Knowledge Strategy | ⬜ À faire | Collections et source policy à créer |
| Skills métier | 🔄 À formaliser | Première priorité : `devis_cctp` / `devis_cctp_review` |
| Mémoire validée Pantheon | 🔄 Modèle clarifié | Quatre niveaux actés : session, candidates, project, system |

---

# 3. Cohérence documentation / code

## 3.1 Documentation

Statut : 🔄 En cours de réalignement final.

Déjà aligné :

- `README.md` ;
- `MODULES.md` ;
- `ARCHITECTURE.md` ;
- `hermes/skill_policy.md`.

À finaliser :

- `AGENTS.md` avec panthéon étendu ;
- `MEMORY.md` ;
- `ROADMAP.md` si nécessaire ;
- `AI_LOG.md` à compléter après chaque intervention.

## 3.2 Code nouveau

Statut : 🔄 Première couche alignée.

Ajouts et changements effectués sur `work/chatgpt/hermes-code-rewrite` :

- `platform/api/pantheon_domain/__init__.py` ;
- `platform/api/pantheon_domain/contracts.py` ;
- `platform/api/pantheon_domain/repository.py` ;
- `platform/api/pantheon_domain/router.py` ;
- `platform/api/main.py` remplacé par une entrée FastAPI simple Domain Layer ;
- `tests/test_domain_layer_api.py`.

Endpoints principaux :

- `/health` ;
- `/domain/health` ;
- `/domain/snapshot` ;
- `/domain/agents` ;
- `/domain/skills` ;
- `/domain/workflows` ;
- `/domain/memory` ;
- `/domain/knowledge` ;
- `/domain/legacy` ;
- `/domain/approval/classify`.

## 3.3 Code legacy

Statut : ⚠️ Présent, non supprimé.

Éléments legacy à auditer :

- `platform/api/apps/*` ;
- `modules.yaml` ;
- registries ;
- workflow loader ;
- module `approvals` legacy ;
- migration Alembic `approval_requests` ;
- Installer UI ;
- tests contractuels legacy.

Aucune suppression n’a été faite.

---

# 4. Décisions Hermes intégrées

Statut : ✅ Acté dans `ARCHITECTURE.md` et `hermes/skill_policy.md`.

Décisions :

- Pantheon ne duplique pas le runtime Hermes.
- Avant de créer une skill Pantheon, vérifier les skills Hermes built-in et optional.
- Les community skills ne servent que d’inspiration tant qu’elles ne sont pas reviewées.
- Une skill Pantheon peut wrapper une skill Hermes, mais doit garder la gouvernance : inputs, outputs, privacy, approval, memory impact, risques.
- Les tools risqués Hermes doivent être policy-gated : terminal, browser, web actions, MCP, file mutation, scheduler, gateways, credentials, external APIs.
- Les contextes envoyés à Hermes doivent rester des exports contrôlés, pas la source de vérité.

---

# 5. Panthéon retenu

Statut : 🔄 À inscrire dans `AGENTS.md`.

Agents abstraits retenus :

- ZEUS : orchestration, arbitrage, décision finale ;
- ATHENA : planification, structuration, stratégie ;
- ARGOS : extraction factuelle, données, contradictions ;
- THEMIS : règles, responsabilité, validation, veto ;
- APOLLO : validation finale, qualité, cohérence ;
- PROMETHEUS : contradiction, stress-test, angles morts ;
- HEPHAESTUS : technique, faisabilité, robustesse ;
- HESTIA : mémoire projet ;
- MNEMOSYNE : mémoire système ;
- IRIS : communication, rédaction, ton ;
- HERMES : interface vers runtime ;
- CHRONOS : planning, délais, dépendances ;
- HERA : supervision, amélioration continue ;
- HECATE : incertitude, manque d’informations ;
- ARES : urgence, mode dégradé ;
- DIONYSOS : créativité, contenu, storytelling ;
- DEMETER : budget, quantités, ressources ;
- POSEIDON : site, environnement, réseaux, eaux ;
- DAEDALUS : conception système, workflows, architecture.

Règle : aucun agent métier. Le métier est injecté par skills, workflows, domains, knowledge et memory.

---

# 6. Modèle mémoire retenu

Statut : 🔄 À formaliser dans `MEMORY.md`.

Quatre niveaux :

```text
session    = réflexion temporaire
candidates = propositions persistées non validées
project    = contexte projet validé
system     = vérité globale validée
```

Cycle :

```text
SESSION → CANDIDATES → validation THEMIS → PROJECT ou SYSTEM
```

---

# 7. Premier use case métier prioritaire

Statut : ✅ Priorisé conceptuellement, ⬜ fichiers à créer.

Use case : analyse de devis vis-à-vis d’un CCTP.

Skill cible :

```text
devis_cctp
```

Workflow cible :

```text
devis_cctp_review
```

Rappel privacy : les exemples et tests seront fictifs et non traçables.

---

# 8. Tests

Statut : ⚠️ Non exécutés dans cette intervention.

Tests ajoutés :

```text
tests/test_domain_layer_api.py
```

Commandes à lancer localement :

```bash
pytest tests/test_domain_layer_api.py
```

Puis, si le legacy doit rester importable :

```bash
pytest
```

---

# 9. Chantiers immédiats

## P0 — Finaliser les Markdown structurants

À faire :

- remplacer `AGENTS.md` par la version panthéon étendu ;
- créer `MEMORY.md` ;
- mettre `ROADMAP.md` en cohérence si nécessaire ;
- compléter `AI_LOG.md`.

## P0 — Créer le noyau `domains/general`

À créer :

```text
domains/general/domain.md
domains/general/skills/name_check/
domains/general/skills/change_request_triage/
domains/general/skills/skill_design/
domains/general/skills/workflow_design/
domains/general/skills/hermes_skill_check/
domains/general/workflows/capability_creation.yaml
domains/general/workflows/change_request_triage.yaml
domains/general/workflows/method_before_code.yaml
```

## P1 — Formaliser le premier use case réel

À créer :

```text
domains/architecture/domain.md
domains/architecture/skills/devis_cctp/SKILL.md
domains/architecture/skills/devis_cctp/manifest.yaml
domains/architecture/skills/devis_cctp/UPDATES.md
domains/architecture/workflows/devis_cctp_review.yaml
```

## P1 — Tester la première couche Domain Layer

À faire :

- lancer `pytest tests/test_domain_layer_api.py` ;
- lancer l’API localement ;
- vérifier `/health` ;
- vérifier `/domain/snapshot` ;
- vérifier `/domain/approval/classify`.

---

# 10. Points de vigilance

- Ne pas installer Hermes Agent globalement sur le NAS sans isolation.
- Ne pas donner à Hermes accès aux volumes Pantheon ou au Docker socket au début.
- Ne pas laisser OpenWebUI devenir source officielle des agents ou de la mémoire validée.
- Ne pas activer une skill Hermes optional/community sans review Pantheon.
- Ne pas promouvoir automatiquement une mémoire Hermes dans Pantheon.
- Ne pas supprimer l’ancien code avant audit post-pivot.
- Ne pas merger la PR #50 sans tests locaux.
- Ne jamais inscrire dans le repo des informations issues de discussions privées ou de projets réels.

---

# 11. Résumé final

Fiable maintenant : la direction documentaire, le modèle domain package, la première API Domain Layer, la séparation Pantheon/Hermes/OpenWebUI et la policy Hermes skills.

Non fiable encore : exécution réelle des tests, création physique des domain packages et alignement complet de `AGENTS.md` / `MEMORY.md`.

Prochaine étape logique : créer le noyau `domains/general`, puis la première skill métier `devis_cctp`.
