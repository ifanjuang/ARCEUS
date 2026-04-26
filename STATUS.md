# Pantheon OS — Project Status

> Source de vérité sur l’état actuel du projet après pivot architectural.
> Les fichiers Markdown de référence pilotent le développement : `README.md`, `ARCHITECTURE.md`, `MODULES.md`, `AGENTS.md`, `ROADMAP.md`, `STATUS.md`.

Dernière mise à jour : 2026-04-26

---

# 1. Décision structurante

Statut : ✅ Décision documentaire actée.

Pantheon OS adopte une trajectoire Hermes-backed.

```text
OpenWebUI = interface chat + knowledge documentaire
Hermes Agent = runtime agentique + skills + tools + scheduler + doctor + gateway + mémoire opérationnelle
Pantheon OS = Domain Operating Layer + agents abstraits + workflows + skills contracts + mémoire validée + gouvernance
```

Formule de conception :

```text
Pantheon définit.
Hermes exécute.
OpenWebUI expose et retrouve.
```

Cette décision remplace la trajectoire antérieure où Pantheon devait devenir un runtime agentique autonome complet.

---

# 2. État global

| Élément | Statut | Commentaire |
|---|---|---|
| Pivot documentaire Hermes-backed | ✅ Fait | `README.md`, `ARCHITECTURE.md`, `AGENTS.md`, `MODULES.md`, `ROADMAP.md` mis à jour |
| Code existant | ⚠️ À réauditer | Le dépôt contient encore l’ancienne trajectoire FastAPI/runtime autonome |
| Tests | ⚠️ Non exécutés | Aucune exécution locale/CI pendant cette intervention documentaire |
| Hermes Agent | ⬜ Non installé | À tester plus tard en Hermes Lab isolé |
| OpenWebUI Knowledge Strategy | ⬜ À faire | Collections et source policy à créer |
| Agents abstraits | 🔄 Documentés | À matérialiser ensuite dans `agents/*.md` |
| Skills métier | ⬜ À faire | `SKILL.md`, manifests, exemples, tests à créer |
| Mémoire validée Pantheon | ⬜ À faire | Structure `memory/project`, `memory/agency`, `memory/candidates` à créer |
| Ancien Approval Gate API | ⚠️ À classer | Peut être conservé, réorienté ou archivé après audit post-pivot |
| Installer UI existante | ⚠️ À classer | Utile comme inspiration Smart Installer, mais doit être réévaluée avec Hermes-backed model |

---

# 3. Cohérence documentation / code

## 3.1 Documentation

Statut : ✅ Alignée sur la nouvelle trajectoire.

Les fichiers suivants décrivent désormais Pantheon comme Domain Operating Layer :

- `README.md` ;
- `ARCHITECTURE.md` ;
- `AGENTS.md` ;
- `MODULES.md` ;
- `ROADMAP.md`.

`STATUS.md` confirme ce pivot et marque le code comme à réauditer.

## 3.2 Code

Statut : ⚠️ Partiellement obsolète par rapport à la nouvelle cible.

Le dépôt contient encore des éléments de l’ancienne architecture autonome :

- FastAPI runtime ;
- `platform/api/apps/*` ;
- `modules.yaml` ;
- registries ;
- workflow loader ;
- `TaskDefinition` / `WorkflowDefinition` ;
- module `approvals` ;
- migration Alembic `approval_requests` ;
- Installer UI ;
- tests contractuels.

Ces éléments ne sont pas supprimés. Ils doivent être classés lors d’un audit post-pivot.

Décisions possibles :

- conserver comme utilitaire ;
- réorienter vers Hermes Integration Layer ;
- archiver ;
- supprimer après validation documentaire ;
- garder comme option avancée.

---

# 4. Ce qui reste fiable

## 4.1 Source de vérité documentaire

Les Markdown de référence font foi. Toute évolution du code doit découler de ces documents.

## 4.2 Agents abstraits

Les agents doivent rester neutres métier. Le métier vient des domain overlays, workflows, skills et knowledge policies.

## 4.3 Séparation des mémoires

La règle cible est :

```text
Hermes peut apprendre.
Pantheon valide.
OpenWebUI documente.
```

## 4.4 Séparation des responsabilités

OpenWebUI ne définit pas les agents. Hermes n’est pas autorisé à redéfinir la doctrine Pantheon. Pantheon ne réimplémente pas les capacités Hermes sans gain clair.

---

# 5. Chantiers immédiats

## P0 — Audit post-pivot

Objectif : comparer l’ancien code à la nouvelle architecture documentaire.

À vérifier :

- `platform/api/` ;
- `core/` ;
- `modules/` ;
- `modules.yaml` ;
- `alembic/versions/` ;
- `docker-compose.yml` ;
- `scripts/install/` ;
- tests existants.

Livrable attendu : diagnostic de cohérence code/docs et décision de conservation/réorientation/archivage.

## P0/P1 — Créer les dossiers contractuels

À créer :

```text
agents/
domains/architecture/
skills/
workflows/
memory/
knowledge/
hermes/context/
operations/
```

## P1 — Hermes Lab isolé

À faire :

- installer Hermes Agent dans un environnement isolé ;
- ne pas donner accès au Docker socket ;
- ne pas donner accès aux volumes Pantheon ;
- ne pas exposer les secrets Pantheon ;
- tester CLI, doctor, mémoire, skills, Ollama LAN ;
- documenter les résultats.

## P1 — OpenWebUI Knowledge Strategy

À faire :

- définir collections ;
- définir source policy ;
- définir taxonomy ;
- distinguer documents projet, agence, réglementaire, modèle, obsolète.

## P1 — Skills métier initiales

À créer :

- `cctp_audit` ;
- `dpgf_check` ;
- `notice_architecturale` ;
- `repo_md_audit` ;
- `source_check` ;
- `client_message`.

---

# 6. Chantiers ralentis ou dépriorisés

Les éléments suivants ne doivent plus être traités comme cœur prioritaire :

- runtime agentique FastAPI complet ;
- scheduler maison ;
- gateway messagerie maison ;
- terminal backend maison ;
- runtime skills maison ;
- dashboard lourd ;
- marketplace interne ;
- Browser Tool avant discipline safety ;
- microservices.

Ils peuvent rester en option, être réorientés ou être archivés après audit.

---

# 7. Points de vigilance

- Ne pas installer Hermes Agent globalement sur le NAS sans isolation.
- Ne pas donner à Hermes accès aux volumes Pantheon ou au Docker socket au début.
- Ne pas laisser OpenWebUI devenir source officielle des agents ou de la mémoire validée.
- Ne pas promouvoir automatiquement une mémoire Hermes dans Pantheon.
- Ne pas activer une skill générée par Hermes sans validation.
- Ne pas supprimer l’ancien code avant audit post-pivot.

---

# 8. Prochaine action recommandée

1. Ajouter l’entrée correspondante dans `AI_LOG.md`.
2. Faire un audit post-pivot du code existant.
3. Créer les dossiers contractuels minimaux.
4. Préparer `hermes/context/pantheon_context.md` et `hermes/context/agents_context.md`.
5. Installer Hermes en lab isolé uniquement après clarification des permissions.

---

# 9. Résumé final

Fiable maintenant : la direction documentaire.

Non fiable encore : l’alignement du code avec cette direction.

Prochaine étape logique : audit post-pivot, puis création du squelette contractuel Pantheon Domain Layer.
