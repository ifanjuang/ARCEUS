# Pantheon OS — Project context for Claude Code agents

## Overview

**Pantheon OS** is a multi-agent intelligence platform for professional organizations (architecture/MOE, legal, audit, consulting, medicine, IT). It centralizes document management, semantic RAG, multi-agent orchestration, project tracking, planning, and finance across the full lifecycle of cases.

**Stack (MVP):** FastAPI · PostgreSQL + pgvector · Hermes Runtime (agents/skills/workflows) · OpenWebUI · Ollama/OpenAI · Docker Compose

---

## Architecture

```
pantheon-os/
│
├── ui/
│   ├── openwebui/              # OpenWebUI config and customizations
│   └── hermes-console/         # Next.js admin console (agents/skills/workflows/logs)
│
├── runtime/
│   └── hermes/                 # Hermes Runtime — agent engine
│       ├── agents/
│       │   ├── _base.py        # AgentBase — common contract
│       │   ├── meta/           # ZEUS, ATHENA, THEMIS, HERA, APOLLO
│       │   ├── analysis/       # HERMES, DEMETER, ARGOS, PROMETHEUS, ARTEMIS, HECATE, METIS
│       │   ├── memory/         # HESTIA, MNEMOSYNE, HADES
│       │   ├── output/         # KAIROS, DAEDALUS, IRIS, APHRODITE, HEPHAESTUS
│       │   └── system/         # ARES, POSEIDON
│       ├── skills/             # Research, document, synthesis, validation, communication
│       ├── workflows/          # Base, dynamic, template workflow definitions
│       ├── routing/            # Intent → workflow/agent routing (HermesRouter)
│       ├── state/              # Session state (SessionState)
│       ├── registries/         # AgentRegistry, SkillRegistry, WorkflowRegistry (YAML-backed)
│       ├── validation/         # Completeness and coherence checks
│       ├── prompts/            # Agent system prompts (SOUL.md override helpers)
│       └── adapters/           # Connectors: OpenWebUI, NAS, Notion, pgvector, web
│
├── api/                        # FastAPI server
│   ├── main.py                 # Entry point (lifespan, CORS, module registry)
│   ├── database.py             # SQLAlchemy async engine + Base
│   ├── core/
│   │   ├── settings.py         # Pydantic Settings (.env)
│   │   ├── auth.py             # JWT, RBAC (admin/moe/collaborateur/lecteur)
│   │   ├── registry.py         # Dynamic module loader
│   │   └── services/
│   │       ├── llm_service.py  # Ollama / OpenAI abstraction
│   │       ├── rag_service.py  # Chunking + embedding + pgvector search
│   │       └── storage_service.py  # Local file storage (V2: MinIO)
│   └── modules/
│       ├── auth/               # Login, register, seed admin
│       ├── admin/              # Config YAML, setup wizard, healthcheck
│       ├── affaires/           # Case/project CRUD + enriched context + domain
│       ├── documents/          # Upload, RAG ingest
│       ├── agent/              # ReAct loop, memory, RAG tools
│       ├── openai_compat/      # OpenAI API v1 compatibility layer (for OpenWebUI)
│       └── hermes_console/     # Console API: agents/skills/workflows/logs/settings
│
├── shared/
│   ├── tools/                  # Reusable tools: pdf_reader, web_search, db_query
│   ├── schemas/                # Shared Pydantic schemas
│   └── templates/              # Document templates
│
├── domains/
│   ├── architecture/           # BTP/MOE domain overlays (prompts, skills, workflows, policies)
│   ├── legal/                  # Legal domain
│   └── medical/                # Medical domain
│
├── config/
│   ├── agents.yaml             # Agent registry (enabled/disabled + metadata)
│   ├── skills.yaml             # Skill registry
│   ├── workflows.yaml          # Workflow definitions (steps, fallbacks)
│   ├── settings.yaml           # Runtime settings (mode, thresholds, RAG params)
│   └── policies.yaml           # Veto patterns, safety rules, domain constraints
│
├── data/
│   ├── db/                     # PostgreSQL init SQL
│   ├── vector/                 # pgvector data (managed by DB)
│   ├── runtime-state/          # Workflow state snapshots
│   └── logs/                   # Application logs
│
├── storage/
│   ├── nas/                    # Canonical project documents
│   ├── drive-sync/             # Google Drive sync
│   ├── notion-sync/            # Notion sync
│   └── exports/                # Generated exports
│
├── infra/
│   ├── docker/api/             # Dockerfile for API container
│   ├── compose/                # docker-compose.v2.yml (V2 full stack)
│   ├── migrations/             # Alembic migration copies
│   └── deploy/                 # Deployment scripts
│
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── workflow/
│   └── regression/
│
├── docs/
│   ├── architecture/
│   ├── agents/
│   ├── skills/
│   ├── workflows/
│   └── runbooks/
│
├── docker-compose.yml          # MVP stack (OpenWebUI + API + Postgres + Ollama)
├── modules.yaml                # API module registry (enabled/disabled)
├── alembic.ini                 # Alembic config
└── .env.example                # Environment template
```

---

## MVP vs V2

| Component | MVP | V2 |
|---|---|---|
| **OpenWebUI** | ✅ Chat UI + Hermes Console tab | ✅ |
| **FastAPI** | ✅ API server | ✅ |
| **Hermes Runtime** | ✅ Agents/skills/workflows | ✅ |
| **PostgreSQL + pgvector** | ✅ State + vector memory | ✅ |
| **Ollama / OpenAI** | ✅ LLM provider | ✅ |
| **LangGraph** | ❌ (not needed for MVP) | ✅ complex state machines |
| **Redis + ARQ** | ❌ (not needed for MVP) | ✅ background jobs |
| **MinIO** | ❌ (local storage) | ✅ large file S3 storage |
| **Advanced observability** | ❌ | ✅ |

---

## The Pantheon — 22 agents

### Naming convention

```python
class Zeus(AgentBase):
    agent = "ZEUS"          # stable identity (branding)
    role  = "orchestrator"  # stable responsibility (system logic)
```

### MVP agents (enabled at startup)

| Agent | Layer | Role | Description |
|---|---|---|---|
| **ZEUS** | meta | orchestrator | Global orchestration — execution order, merge/fork/child workflows |
| **ATHENA** | meta | planner | Planning and decomposition — task analysis, agent selection |
| **APOLLO** | meta | validator | Final validation — reliability scoring, release decision |
| **HERMES** | analysis | router | Research router — source selection, skill activation |
| **ARGOS** | analysis | extractor | Factual extraction — facts, figures, citations |
| **PROMETHEUS** | analysis | challenger | Contradiction detection — source comparison, inconsistency flags |
| **HECATE** | analysis | uncertainty_resolver | Uncertainty detection — missing info, clarification questions |
| **HESTIA** | memory | session_memory | Session memory — immediate context, run continuity |
| **HADES** | memory | vector_retrieval | Deep memory — pgvector semantic retrieval |
| **KAIROS** | output | synthesizer | Contextual synthesis — information hierarchization |
| **DAEDALUS** | output | builder | Deliverable construction — dossiers, briefs, reports |
| **IRIS** | output | communicator | Communication — context reformulation, tone adaptation |

### Extended agents (V2, disabled by default)

| Agent | Layer | Role |
|---|---|---|
| **THEMIS** | meta | Process integrity guardian (veto) |
| **HERA** | meta | Global coherence supervisor |
| **DEMETER** | analysis | Data collection and ingestion |
| **ARTEMIS** | analysis | Filtering and focus (signal/noise) |
| **METIS** | analysis | Tactical optimization |
| **MNEMOSYNE** | memory | Structured knowledge library |
| **APHRODITE** | output | Polish and presentation |
| **HEPHAESTUS** | output | Diagrams and technical production |
| **ARES** | system | Fast execution / fallback mode |
| **POSEIDON** | system | Load management and flow control |

Source of truth: `config/agents.yaml`

---

## Data model (MVP tables)

| Table | Description |
|---|---|
| `users` | User accounts, RBAC role |
| `affaires` | Project cases + context (domain, typology, region, budget, phase) |
| `affaire_permissions` | Per-case role override |
| `documents` | Uploaded files (PDF/DOCX/TXT/images) |
| `chunks` | RAG fragments, `vector(768)`, HNSW index |
| `agent_runs` | Agent execution traces (steps, RAG sources, duration) |
| `agent_memory` | Learned lessons — `scope`: `agence` or `projet` |

---

## Config files (source of truth)

### config/agents.yaml
```yaml
agents:
  ZEUS: { layer: meta, role: orchestrator, enabled: true }
  ATHENA: { layer: meta, role: planner, enabled: true }
```

### config/skills.yaml
```yaml
skills:
  - id: hybrid_research
    name: "Recherche hybride"
    enabled: true
    agents: [HERMES, HADES]
```

### config/workflows.yaml
```yaml
workflows:
  - id: research
    name: "Recherche documentaire"
    enabled: true
    steps: [HECATE, HERMES, ARGOS, PROMETHEUS, KAIROS, IRIS]
    fallback: simple_answer
```

### config/settings.yaml
```yaml
runtime:
  mode: balanced    # fast | balanced | expert
  max_agents_per_run: 8
  uncertainty_threshold: 0.7
  confidence_threshold: 0.6
```

---

## Hermes Console API (`/console`)

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| GET | `/console/dashboard` | user | Summary stats |
| GET | `/console/agents` | user | List all agents |
| POST | `/console/agents/{name}/toggle` | admin/moe | Enable/disable agent |
| GET | `/console/skills` | user | List all skills |
| POST | `/console/skills/{id}/toggle` | admin/moe | Enable/disable skill |
| GET | `/console/workflows` | user | List all workflows |
| POST | `/console/workflows/{id}/toggle` | admin/moe | Enable/disable workflow |
| GET | `/console/settings` | user | Get runtime settings |
| POST | `/console/settings` | admin | Update runtime settings |
| GET | `/console/logs` | user | Get recent logs |

---

## Creating a new agent

```
runtime/hermes/agents/{layer}/{name}.py
runtime/hermes/agents/{layer}/{name}/SOUL.md
```

```python
from pathlib import Path
from runtime.hermes.agents._base import AgentBase

class MyAgent(AgentBase):
    agent = "MYAGENT"
    role = "my_role"
    layer = "analysis"   # meta | analysis | memory | output | system
    veto = False
    _soul_dir = Path(__file__).parent / "myagent"
```

Then add to `config/agents.yaml` and the layer's `__init__.py`.

---

## Creating a new API module

```
api/modules/{name}/
├── __init__.py
├── manifest.yaml       # name, version, description, prefix, depends_on
├── models.py           # SQLAlchemy models (inherit database.Base)
├── schemas.py          # Pydantic request/response schemas
├── service.py          # Business logic
└── router.py           # def get_router(config: dict) -> APIRouter
```

### Important rules
- Always inherit `database.Base` for SQLAlchemy models
- Always declare new tables in `alembic/env.py`
- Always create an Alembic migration for schema changes
- Circular imports → late imports inside functions
- Shared services (`RagService`, `LlmService`) → classmethods
- Auth: `Depends(get_current_user)`, `Depends(require_role("admin", "moe"))`
- **No LangGraph in MVP** — use simple async pipelines
- **No Redis/ARQ in MVP** — use FastAPI `BackgroundTasks` if needed

---

## Code patterns

### SQLAlchemy 2.0
```python
result = await db.execute(select(Model).where(Model.field == value))
items = result.scalars().all()
```

### pgvector (cosine similarity)
```python
rows = await db.execute(
    text("SELECT ... 1 - (embedding <=> :vec::vector) AS score FROM chunks WHERE ..."),
    {"vec": str(embedding_list), ...}
)
```

---

## Launch

```bash
cp .env.example .env
# Edit .env — change DB_PASSWORD and JWT_SECRET_KEY at minimum
docker compose up -d
docker compose exec api alembic upgrade head
# API docs:  http://localhost:8000/docs  (DEBUG=true only)
# Chat UI:   http://localhost:3000
# Console:   http://localhost:3000 → Hermes Console tab
```

### V2 stack
```bash
docker compose -f docker-compose.yml -f infra/compose/docker-compose.v2.yml up -d
```

---

## Key environment variables

```bash
# Database
DATABASE_URL=postgresql+asyncpg://pantheon:password@db:5432/pantheon
DATABASE_URL_SYNC=postgresql://pantheon:password@db:5432/pantheon

# Auth
JWT_SECRET_KEY=your-secret-min-32-chars
ADMIN_EMAIL=admin@yourorg.com
ADMIN_PASSWORD=strongpassword

# LLM (choose one)
LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://ollama:11434
OLLAMA_MODEL=mistral:7b
# or: LLM_PROVIDER=openai  OPENAI_API_KEY=sk-...

# Embeddings
EMBEDDING_PROVIDER=ollama
OLLAMA_EMBEDDING_MODEL=nomic-embed-text
EMBEDDING_DIM=768

# Domain
DOMAIN=architecture
DOMAIN_LABEL="Architecture & Maîtrise d'Œuvre"

# Runtime
DEBUG=true
```

---

## Alembic migrations

Run `alembic upgrade head` after each schema change.

| Migration | Content |
|---|---|
| 0001 | users, affaires, permissions, documents, chunks |
| 0002 | agent_runs |
| 0003 | orchestra_runs |
| 0004 | agent_memory |
| 0005–0028 | V2 features (guards, wiki, scoring, etc.) |

---

## Changelog

`CHANGELOG.md` at root documents all notable changes.

**Rule**: every functional commit must add an entry in `[Unreleased]`. On release, rename with version + date.

SemVer:
- **MAJOR**: breaking API or non-retrocompatible DB schema change
- **MINOR**: new feature, module, or pattern
- **PATCH**: bug fix, optimization, internal refactoring

# currentDate
Today's date is 2026-04-19.
