# ARCEUS

> Intelligence opérationnelle pour agences MOE — du programme client à la levée des réserves.

**Stack :** FastAPI · PostgreSQL + pgvector · LangGraph · MinIO · Ollama/OpenAI · ARQ/Redis · Docker Compose

→ Fonctionnement interne : [ARCHITECTURE.md](ARCHITECTURE.md) | Développer : [CLAUDE.md](CLAUDE.md) | Backlog : [DEVLIST.md](DEVLIST.md)

---

## Démarrage rapide

```bash
cp .env.example .env          # DB_PASSWORD, JWT_SECRET_KEY, ADMIN_EMAIL, ADMIN_PASSWORD
docker compose up -d
docker compose exec api alembic upgrade head
# http://localhost:8000 | Docs : http://localhost:8000/docs (DEBUG=true)
```

---

## Le Panthéon — 15 agents + Zeus

| Famille | Agent | Rôle |
|---|---|---|
| **Perception** | Hermès | Interface, routage, qualification C1-C5 |
| | Argos | Observation visuelle, constat objectif (photos, plans) |
| **Analyse** | Athéna | Structuration des problèmes, scénarios |
| | Héphaïstos | Faisabilité technique, DTU, matériaux, fiches produits — *veto technique* |
| | Prométhée | Contre-analyse, détection biais, critique logique |
| | Apollon | Recherche web + RAG, vérification normative, cohérence finale |
| | Dionysos | Pensée latérale, rupture créative |
| **Cadrage** | Thémis | Réglementation + contrat MOE + déontologie — *veto contractuel* |
| | Chronos | Temps, planning, délais légaux, impacts cascade |
| | Arès | Action terrain rapide, décisions réversibles C3 |
| **Continuité** | Hestia | Mémoire projet (décisions, hypothèses, dettes D0-D3) |
| | Mnémosyne | Mémoire agence (patterns, leçons, précédents) |
| **Communication** | Iris | Emails humains, correspondance, relances délicates |
| | Aphrodite | Marketing, réseaux sociaux, storytelling architectural |
| **Production** | Dédale | Dossiers complets (PC, DCE, DOE, marchés) |
| **Orchestrateur** | Zeus | Arbitrage stratégique, distribution, jugement, veto global |

---

## Criticité C1-C5

| Niveau | Nature | Mode |
|---|---|---|
| **C1** | Information pure | Agent unique, pas de Zeus |
| **C2** | Question | 1-2 agents spécialisés |
| **C3** | Décision locale réversible | Zeus optionnel, Arès peut agir |
| **C4** | Décision engageante | Zeus obligatoire + validation humaine (HITL) |
| **C5** | Risque majeur | Zeus + HITL + veto check (Thémis / Héphaïstos) |

---

## Les 3 mémoires

| Mémoire | Durée | Agent | Contenu |
|---|---|---|---|
| **Agence** | Permanente | Mnémosyne | Patterns, leçons, comportements d'entreprises |
| **Projet** | Durée affaire | Hestia | Décisions validées, contraintes, dettes D0-D3 |
| **Fonctionnelle** | Session | LangGraph state | Tâches en cours, blocages, échanges actifs |

---

## Roadmap

| Module | Statut | Description |
|---|---|---|
| `auth` | ✅ | JWT, RBAC 4 rôles |
| `admin` | ✅ | Config YAML, setup wizard |
| `affaires` | ✅ | CRUD + contexte projet enrichi |
| `documents` | ✅ | Upload + RAG + trigger Thémis |
| `agent` | ✅ | ReAct, mémoire dynamique, outils |
| `orchestra` | ✅ | LangGraph Zeus, C1-C5, HITL, veto, SSE |
| `meeting` | ✅ | Analyse CR, actions, ordre du jour |
| `decisions` | ⬜ | CRUD project_decisions, dette D0-D3 |
| `planning` | ⬜ | Gantt, lots, impacts cascade |
| `webhooks` | ⬜ | Telegram / WhatsApp bot |
| `finance` | ⬜ | Situations, avenants, budget |
| `communications` | ⬜ | Registre courrier |
| `chantier` | ⬜ | Observations terrain, non-conformités |
