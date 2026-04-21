# ROADMAP — Pantheon OS

> Feuille de route V2 / V3 consolidant ce qui fonctionne déjà (agents spécialisés,
> pipeline RAG, criticité, mémoires) et traçant une évolution vers une architecture
> modulaire, transversale et multi‑domaine.
>
> Référentiel d'architecture : `CLAUDE.md` · Backlog détaillé : `DEVLIST.md`

---

## 1. Acquis à préserver

Ces briques sont stables, testées et constituent la base que toute évolution doit
protéger.

### 1.1 Architecture hexagonale
- **API FastAPI** (`platform/api/`) avec apps modulaires auto‑découvertes
  (`auth`, `admin`, `affaires`, `documents`, `agent`, `openai_compat`,
  `hermes_console`).
- Séparation claire **stockage** (PostgreSQL + pgvector) / **traitements**
  (Hermes Runtime — agents, skills, workflows).
- En V2 : réintroduction maîtrisée de **LangGraph** (machines à états),
  **Redis + ARQ** (jobs asynchrones), **MinIO** (S3 fichiers volumineux).

### 1.2 Pipeline RAG
- Extraction → chunking → embedding → index pgvector (HNSW, cosinus).
- Retrieval hybride BM25 + sémantique avec Reciprocal Rank Fusion.
- Réinjection dans les prompts agents — pipeline à conserver tel quel.

### 1.3 Panthéon d'agents (22 rôles)
- Répartition par couches : `meta`, `analysis`, `memory`, `output`, `system`.
- Noms canoniques : **@ZEUS** (orchestration), **@ATHENA** (planification),
  **@APOLLO** (validation), **@Hermes** (routing), **@Argos** (extraction),
  **@Prometheus** (contradictions), **@Hecate** (incertitudes),
  **@Hestia** (mémoire projet), **@Hades** (mémoire vectorielle),
  **@Kairos** (synthèse), **@Daedalus** (livrables), **@Iris** (communication).
- **Veto** : **@THEMIS** (intégrité process) — granularité qui garantit
  traçabilité et expertise par domaine.

### 1.4 Gestion de la criticité C1–C5
- Activation du HITL sur C4/C5, règles d'escalade, politique *draft first*.
- Limite les risques sur les livrables à fort impact.

### 1.5 Trois couches de mémoire
- **@Hestia** — mémoire projet (décisions, contraintes, dette décisionnelle).
- **@Mnemosyne** — mémoire agence (patterns, capitalisation inter‑projets).
- **Mémoire fonctionnelle** — état de run partagé entre agents.

### 1.6 Principes d'ingénierie agent
Planning avant exécution · tool design explicite · gestion d'erreurs ·
évaluation mesurable · réversibilité. Voir `AGENT_ENGINEERING_PRINCIPLES.md`.

---

## 2. Roadmap V2 — modernisation & modularisation

### 2.1 Contrat agent unifié et registre dynamique

- **Contrat unique** : signature `run(context, task, artifacts)` sur
  `AgentBase` (`core/contracts/agent.py`).
- Chaque agent vit dans son dossier `modules/agents/{layer}/{myth}_{role}/`
  avec :
  - `agent.py` — classe spécifique ;
  - `manifest.yaml` — id, rôle, couche, veto, version ;
  - `SOUL.md` — prompt système / identité ;
  - `skills/` — fonctions testables indépendamment ;
  - `tests/` — couverture par agent.
- **Registre dynamique** : au démarrage, `ManifestLoader` parcourt
  `modules/agents/` et `modules/skills/` pour instancier et publier les
  métadonnées — ajout/retrait d'un agent sans toucher au code cœur.

### 2.2 Modularisation des services

- Séparer nettement **API FastAPI**, **orchestrateur Hermes/LangGraph** et
  **interface OpenWebUI** en packages distincts → orchestrateur réutilisable
  hors contexte architecture.
- **Config centralisée** : 5 fichiers canoniques
  (`runtime.yaml`, `settings.yaml`, `sources.yaml`, `ui.yaml`,
  `domains.yaml`) + loader générique. Secrets isolés dans `.env`.

### 2.3 État et reprise sur plantage

- **State manager centralisé** : persistance des runs (`agent_runs`,
  `orchestra_runs`) en PostgreSQL + snapshot dans
  `platform/data/runtime-state/`.
- Reprise possible après crash + simplification du streaming SSE.
- **Mémoire fonctionnelle unifiée** en Redis (V2) pour le partage d'état
  inter‑agents pendant l'exécution.

### 2.4 Console Hermes et observabilité

- Onglet **Hermes Console** (Next.js) dans OpenWebUI — API déjà prévue
  sous `/console` (dashboard, agents, skills, workflows, settings, logs).
- Activation / désactivation à chaud des agents, skills, workflows.
- Monitoring jobs ARQ, `agent_runs`, `orchestra_runs` (durée moyenne, taux
  d'échec, agents les plus sollicités).

### 2.5 Tests automatisés

- Unitaires : `agent/tools.py`, skills critiques.
- Intégration : `orchestra/service.py` sur cycles C1–C5.
- End‑to‑end : flux RAG, orchestration multi‑agents, veto, sauvegarde
  mémoire — cas limites (devis incomplet, contradiction de planning, etc.).

---

## 3. Roadmap V3 — ouverture & généralisation

### 3.1 Transversalité disciplinaire

- Abstraire **`projet`**, **`affaire`**, **`phase`** via le système de
  *domain overlays* (`domains/architecture/`, `domains/legal/`,
  `domains/medical/`…).
- Modèles de données interchangeables, prompts et workflows overlayables
  par domaine via `config/domains.yaml`.
- **Plugins skills** : chaque domaine ajoute ses fonctions (calcul
  structurel, analyse normative, scoring juridique, cotation médicale…).

### 3.2 Micro‑services et scalabilité

- Découpage progressif : service **RAG**, service **Agents**, service
  **Orchestration** — indépendants et scalables.
- Messaging asynchrone : ARQ/Redis en interne, RabbitMQ pour les besoins
  inter‑services.
- **Abstraction LLM** : provider‑agnostic (Ollama, OpenAI, Anthropic,
  Mistral…) configurable à chaud via `settings.yaml`.

### 3.3 Versioning et portabilité

- **SemVer** par agent, skill, workflow — déploiement versionné selon le
  métier.
- **Export / import** de la mémoire projet (Hestia) et agence (Mnémosyne)
  — backups, migrations inter‑serveurs sans perte de données.

### 3.4 Expérience utilisateur

- Intégration **voix** : transcription (NoobScribe) + synthèse TTS dans
  OpenWebUI.
- **Hermes‑Agent** : création de variations d'agents sur mesure (ex.
  *Prometheus junior* pour générer des questions de clarification plus
  douces).
- Retrieval **multimodal** : chunks image + description générée par
  @Argos (plans, coupes, photos chantier).

---

## 4. Garde‑fous — ne rien perdre de l'existant

- **Documenter** chaque agent, skill et workflow en Markdown de référence
  (objectifs, entrées, sorties, limites) → reprise facilitée lors des
  refactorisations.
- **Tests de non‑régression** reproduisant les flux critiques (RAG,
  orchestration multi‑agents, veto, mémoire) — filet de sécurité à chaque
  évolution.
- **Migrations Alembic** systématiques pour toute modification de schéma
  (voir table dans `CLAUDE.md`).
- **Conserver** les helpers qui marchent (extraction PDF, streaming SSE,
  retrieval hybride) tant qu'ils sont stables.
- **Branches Git** :
  - `main` — version stable en production ;
  - `develop` — travaux V2 ;
  - `experiment/v3-*` — explorations V3.

---

## 5. Synthèse des phases

| Phase | Objectif | Livrable clé |
|---|---|---|
| **MVP** (actuel) | Runtime Hermes stable, 12 agents actifs, RAG hybride | API + OpenWebUI + Console |
| **V2** | Modularité, registre dynamique, state manager, tests | Hermes Console + LangGraph + Redis |
| **V3** | Transversalité, micro‑services, multimodal, voix | Plateforme multi‑domaine + plugins skills |

Cette feuille de route consolide **ce qui fonctionne déjà** (agents
spécialisés, pipeline RAG, criticité, mémoires) tout en ouvrant la voie à
une architecture **modulaire, évolutive et multi‑domaine**.
