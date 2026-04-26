# Pantheon OS — External Watchlist

Ce fichier suit les dépôts, guides et projets externes utilisés comme veille ou inspiration.

Règle : ces dépôts ne sont pas des dépendances runtime de Pantheon OS sauf décision explicite. Toute idée externe doit d’abord être comparée aux Markdown de référence avant modification du code.

---

## Table de veille

| Source | Usage Pantheon OS | Statut | Dernier audit | Décision |
|---|---|---|---|---|
| `smarzola/hermes-local-memory` | Doctrine mémoire locale | Veille | 2026-04-26 | Idées retenues, pas de dépendance |
| `suryamr2002/langgraph-approval-hub` | Approval Gate / HITL | Veille | 2026-04-26 | Idées retenues, pas de dépendance |
| `browser-use/browser-harness` | Browser Tool gouverné | Plus tard | 2026-04-26 | À reporter après Approval + Observability |
| `elizaOS/eliza` | Actions / providers / evaluators / services | Veille | 2026-04-26 | Concepts retenus, runtime rejeté |
| `crewAIInc/crewAI` | Task Contract / workflow crew pattern | Veille | 2026-04-26 | Concepts retenus, runtime rejeté |
| `agentscope-ai/agentscope` | Multi-agent runtime | Veille | 2026-04-26 | Intéressant, non prioritaire |
| `FlowiseAI/Flowise` | Visual workflow builder | Plus tard | 2026-04-26 | À reporter |
| `agentsmd/agents.md` | Convention agents | Veille | 2026-04-26 | À intégrer comme convention documentaire |
| `agentskills/agentskills` | Skill contract | Veille | 2026-04-26 | À intégrer plus tard |
| `NirDiamant/GenAI_Agents` | Patterns agents | Veille | 2026-04-26 | Inspiration seulement |
| `NirDiamant/agents-towards-production` | Production hardening | Veille | 2026-04-26 | Inspiration seulement |
| `e2b-dev/awesome-ai-agents` | Catalogue | Veille | 2026-04-26 | Pas d’import massif |
| `ashishpatel26/500-AI-Agents-Projects` | Catalogue | Veille | 2026-04-26 | Pas d’import massif |
| `contains-studio/agents` | Catalogue agents | Veille | 2026-04-26 | Pas d’import massif |
| `msitarzewski/agency-agents` | Catalogue agents | Veille | 2026-04-26 | Pas d’import massif |
| `hermesguide.xyz` | Guide Hermes | Veille | 2026-04-26 | À utiliser pour patterns, pas comme source unique |

---

## Classification obligatoire des idées externes

Chaque idée externe doit être classée :

- À intégrer maintenant
- À intégrer plus tard
- Intéressant mais non prioritaire
- À rejeter
- Risqué
- Redondant avec l’existant

---

## Fiche d’intégration obligatoire

Pour chaque idée retenue :

| Champ | Contenu attendu |
|---|---|
| Problème résolu | Ce que l’idée corrige réellement |
| Fichier MD à modifier | `STATUS.md`, `ROADMAP.md`, `ARCHITECTURE.md`, `AGENTS.md`, `MODULES.md`, `README.md` |
| Section concernée | Section précise |
| Impact architecture | Faible / moyen / fort |
| Impact code | Fichiers ou modules touchés |
| Risques | Dette, sécurité, couplage, complexité |
| Priorité | P0 / P1 / P2 / P3 |

---

## Règle finale

Ne pas copier mécaniquement une architecture externe.

Pantheon OS conserve son identité : modularité, agents spécialisés, orchestration contrôlée, mémoire projet, RAG, workflows, validation, observability, self-hosting.
