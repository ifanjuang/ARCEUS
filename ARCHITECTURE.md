# OS Projet — Architecture & flux de données

---

## Vue d'ensemble

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                            POINTS D'ENTRÉE                                  ║
║                                                                              ║
║  [Upload fichier]  [Question chat]  [CR réunion]  [Journal]  [Email SMTP]  ║
║       PDF/DOCX      langage naturel   texte brut   terrain    entrant       ║
╚══════════════╤═══════════════╤══════════════╤═══════════════╤═══════════════╝
               │               │              │               │
               ▼               ▼              ▼               ▼
╔══════════════════════════════════════════════════════════════════════════════╗
║                          FASTAPI — Cerveau central                          ║
║                                                                              ║
║   ┌─────────────┐  ┌──────────────┐  ┌──────────────┐  ┌───────────────┐  ║
║   │ RAG Engine  │  │ LLM Service  │  │ Event Engine │  │ Doc Engine    │  ║
║   │ (recherche) │  │ (génération) │  │ (alertes)    │  │ (génération)  │  ║
║   └──────┬──────┘  └──────┬───────┘  └──────┬───────┘  └───────┬───────┘  ║
║          │                │                  │                  │           ║
╚══════════╪════════════════╪══════════════════╪══════════════════╪═══════════╝
           │                │                  │                  │
     ┌─────▼──────┐   ┌─────▼──────┐          │                  │
     │ PostgreSQL │   │   Ollama   │          │                  │
     │ + pgvector │   │  (local)   │          │                  │
     │            │   │ ou OpenAI  │          │                  │
     │ Vecteurs   │   │  (cloud)   │          │                  │
     │ Données    │   └────────────┘          │                  │
     └────────────┘                           │                  │
                                              │                  │
╔═════════════════════════════════════════════╪══════════════════╪═══════════╗
║                         POINTS DE SORTIE   ▼                  ▼           ║
║                                                                             ║
║  [Réponse sourcée]  [CR structuré]  [Planning]  [Alerte]  [Doc générée]   ║
║   chat OpenWebUI    décisions+       JSON+        email     CCTP / OS /    ║
║   + références      actions          Gantt        SMTP      courrier       ║
╚═════════════════════════════════════════════════════════════════════════════╝
```

---

## Les 4 niveaux de connaissance

Chaque requête ne consulte que les couches auxquelles l'utilisateur a accès.

```
┌──────────────────────────────────────────────────────────────────────────┐
│  COUCHE 4 — SENSIBLE              Accès : MOE + Admin uniquement         │
│                                                                          │
│  Contenu : honoraires, contrats, litiges, situations financières         │
│  Exemples : avenant signé, mémoire de réclamation, tableau marché        │
│  Stockage : PostgreSQL (chiffré) + MinIO                                 │
├──────────────────────────────────────────────────────────────────────────┤
│  COUCHE 3 — MÉMOIRE PROJET        Accès : selon rôle affaire             │
│                                                                          │
│  Contenu : tout ce qui concerne UNE opération                            │
│  Exemples :                                                              │
│    • CCTP du projet Résidence Voltaire (lot 03 — Maçonnerie)             │
│    • Courrier de mise en demeure à l'entreprise Dupont TP                │
│    • Note de calcul thermique déposée en APD                             │
│    • Planning chantier + avenants                                        │
│    • CR de réunion du 14 mars — décisions et actions                     │
│  Stockage : PostgreSQL + pgvector (embeddings) + MinIO (fichiers bruts)  │
├──────────────────────────────────────────────────────────────────────────┤
│  COUCHE 2 — INTELLIGENCE AGENCE   Accès : Collaborateur → Admin          │
│                                                                          │
│  Contenu : ce que l'agence a appris sur TOUS ses projets                 │
│  Exemples :                                                              │
│    • "Sur les projets avec ITEe, on retient systématiquement X"          │
│    • Détail constructif acrotère éprouvé sur 3 chantiers                 │
│    • Fiche fournisseur Knauf validée (référence, contact, retour terrain) │
│    • Q&R récurrente : règle PLU sur les retraits en zone UB              │
│  Stockage : PostgreSQL + pgvector                                        │
├──────────────────────────────────────────────────────────────────────────┤
│  COUCHE 1 — CONNAISSANCE PUBLIQUE Accès : Tous les rôles                 │
│                                                                          │
│  Contenu : normes, réglementation, référentiels                          │
│  Exemples :                                                              │
│    • DTU 20.1 — Maçonnerie d'ouvrages de petite section                  │
│    • RE2020 — exigences thermiques et carbone                            │
│    • Eurocode 2 — béton armé                                             │
│    • Avis technique CSTB isolant X (version 2024)                        │
│    • CCTP type CSPS (base de référence générique)                        │
│  Stockage : PostgreSQL + pgvector                                        │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## Composants techniques & rôles

| Composant | Rôle | Ce qu'il stocke / fait | Connexions |
|-----------|------|------------------------|------------|
| **PostgreSQL** | Base de données principale | Tables métier (affaires, lots, actions, événements) + vecteurs pgvector | ← FastAPI lit/écrit ↔ pgvector pour la similarité |
| **pgvector** | Extension PostgreSQL | Embeddings des documents — permet la recherche sémantique | ← Ollama/OpenAI génère les vecteurs → stockés ici |
| **MinIO** | Stockage fichiers | PDFs, DOCXs, photos chantier bruts — accès par URL signée | ← FastAPI upload/download, URL transmise à l'UI |
| **Ollama** | LLM + Embeddings local | Génère les réponses et les vecteurs — tourne sur le serveur de l'agence | ← FastAPI l'interroge via HTTP local |
| **OpenAI (optionnel)** | LLM + Embeddings cloud | Idem Ollama — performance max, données envoyées à OpenAI | ← FastAPI l'interroge si `LLM_PROVIDER=openai` |
| **FastAPI** | API centrale | Orchestre tout : RAG, agents, planning, finance, meeting | ↔ Tous les composants |
| **OpenWebUI** | Interface chat | Conversation naturelle + accès aux agents | → Appelle FastAPI via `Tools` |
| **OpenClaw PWA** | Interface terrain | Journal chantier, observations, photos — mobile first | → Appelle FastAPI via REST |

---

## Flux détaillé : question technique

```
1. [Utilisateur OpenWebUI]
   "Quelle est la résistance thermique minimale en toiture selon la RE2020 ?"
        │
        ▼
2. [FastAPI — RAG Engine]
   Génère l'embedding de la question (Ollama nomic-embed-text)
        │
        ▼
3. [PostgreSQL pgvector]
   Recherche cosine similarity dans les couches autorisées
   → Résultats : RE2020 §3.2 (score 0.94) + Note calcul thermique projet (score 0.87)
        │
        ▼
4. [FastAPI — LLM Service]
   Injecte les sources dans le prompt + prompt système admin
   Appelle Ollama (ou OpenAI)
        │
        ▼
5. [Réponse à l'utilisateur]
   "Selon la RE2020 §3.2 (source : base normative), la valeur Bbio max est…
    Sur votre projet Résidence Voltaire, la note de calcul APD (déposée 03/2024)
    retient une résistance de X m²K/W pour la toiture-terrasse."
        │
        ▼
6. [FastAPI — Memory Engine]
   La Q&R est automatiquement enregistrée dans la mémoire du projet (Couche 3)
   Si la question est récurrente inter-projets → proposée en Couche 2
```

---

## Flux détaillé : CR de réunion

```
1. [Utilisateur]
   Colle un CR brut dans le chat ou upload le fichier
        │
        ▼
2. [Agent Meeting — OpenWebUI Tool]
   Appelle FastAPI → POST /meeting/analyze
        │
        ▼
3. [FastAPI — LLM]
   Extrait : décisions / actions (responsable + date) / blocages / avancements
        │
        ├── → PostgreSQL : enregistre les actions et événements
        ├── → Planning Engine : met à jour les lots concernés
        │                       calcule les impacts en cascade
        └── → Memory Engine : enregistre les décisions en mémoire projet
        │
        ▼
4. [Sortie]
   CR structuré affiché dans l'UI
   Alertes email si délais dépassés
   Sync Notion (si activé)
```

---

## Flux détaillé : upload CCTP

```
1. [Utilisateur]
   Upload CCTP_ResidenceVoltaire_v3.pdf via interface
        │
        ▼
2. [FastAPI — Document Engine]
   Stockage brut → MinIO
   Extraction texte (PyMuPDF / python-docx)
        │
        ▼
3. [FastAPI — RAG Engine]
   Découpe en chunks (~500 tokens, overlap 50)
   Génère embeddings (Ollama ou OpenAI)
   Stocke dans PostgreSQL pgvector (affaire_id = Voltaire, source_type = cctp)
        │
        ▼
4. [FastAPI — Planning Engine] (optionnel, si demandé)
   LLM extrait les lots depuis le CCTP
   Génère le planning avec dépendances
        │
        ▼
5. [Disponible immédiatement]
   → Questions sur ce CCTP via chat
   → Génération de documents basés sur ce CCTP
   → Comparaison avec d'autres CCTPs de l'agence (Couche 2)
```

---

## Exemples de documents par couche

| Document | Couche | Qui l'importe | Qui peut le consulter |
|----------|--------|---------------|-----------------------|
| DTU 20.1 (maçonnerie) | 1 — Publique | Admin | Tous |
| RE2020 — texte complet | 1 — Publique | Admin | Tous |
| Avis technique CSTB — Rockwool | 1 — Publique | Admin | Tous |
| PLU de la commune du projet | 3 — Projet | MOE | Selon affaire |
| CCTP lot 03 Résidence Voltaire | 3 — Projet | MOE | Selon affaire |
| Courrier entreprise Dupont TP | 3 — Projet | MOE | MOE + Admin |
| Note de calcul thermique APD | 3 — Projet | Ingénieur BE | Selon affaire |
| CR réunion chantier 14/03 | 3 — Projet | Auto (Meeting) | Selon affaire |
| Détail constructif acrotère validé | 2 — Agence | Auto (capitalisation) | Collaborateurs |
| Fiche fournisseur Knauf | 2 — Agence | MOE | Collaborateurs |
| Honoraires et situations | 4 — Sensible | Admin / MOE | MOE + Admin |
| Contrat MOE signé | 4 — Sensible | Admin | Admin uniquement |

---

## Agents disponibles dans OpenWebUI

| Agent | Ce qu'il fait | Tools qu'il appelle |
|-------|---------------|---------------------|
| **OS Chantier** | Assistant général — questions, avancement, risques | `rag_query`, `get_planning`, `get_events` |
| **Agent Planning** | Génère et simule le planning à partir du CCTP | `generate_planning`, `simulate_scenario`, `rag_query` |
| **Agent Meeting** | Analyse un CR brut → décisions + actions + planning | `analyze_meeting`, `get_open_actions`, `update_action` |
| **Agent Documents** | Génère CCTP, OS, courriers depuis les données projet | `get_project_data`, `rag_query`, `generate_document` |

Chaque agent appelle FastAPI. FastAPI orchestre PostgreSQL + Ollama. L'agent ne répond jamais de mémoire.

---

## Où sont les agents et comment ils sont connectés

```
╔══════════════════════════════════════════════════════════════════════════╗
║                         INTERFACE UTILISATEUR                           ║
║                                                                          ║
║   OpenWebUI (desktop)              OpenClaw PWA (terrain / mobile)      ║
║   ┌──────────────────────┐         ┌──────────────────────────────────┐ ║
║   │  Chat langage naturel │         │  Journal chantier                │ ║
║   │  ┌────────────────┐  │         │  Photos, observations             │ ║
║   │  │ Agent Chantier │  │         │  Pointage lots                   │ ║
║   │  │ Agent Planning │  │         └──────────────┬───────────────────┘ ║
║   │  │ Agent Meeting  │  │                        │                     ║
║   │  │ Agent Documents│  │                        │                     ║
║   │  └───────┬────────┘  │                        │                     ║
║   └──────────┼───────────┘                        │                     ║
╚═════════════╪════════════════════════════════════╪════════════════════╝
              │  Tools HTTP                         │ REST API
              ▼                                     ▼
╔══════════════════════════════════════════════════════════════════════════╗
║                           FASTAPI — MODULES                             ║
║                                                                          ║
║  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────┐ ║
║  │ RAG      │ │ Planning │ │ Meeting  │ │ Finance  │ │ Document     │ ║
║  │ /rag/    │ │ /planning│ │ /meeting │ │ /finance │ │ /document    │ ║
║  │          │ │          │ │          │ │          │ │              │ ║
║  │ Cherche  │ │ Génère   │ │ Analyse  │ │ Situations│ │ Génère CCTP │ ║
║  │ sources  │ │ planning │ │ CR brut  │ │ Avenants │ │ OS, courrier│ ║
║  │ répond   │ │ + impacts│ │ → actions│ │ Alertes  │ │ depuis data │ ║
║  └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘ └──────┬───────┘ ║
║       │            │            │             │              │          ║
║  ┌────▼────────────▼────────────▼─────────────▼──────────────▼────────┐ ║
║  │                    SERVICES PARTAGÉS (core/)                       │ ║
║  │  llm_service.py        rag_service.py        event_engine.py       │ ║
║  │  (Ollama / OpenAI)     (embedding + search)  (règles + alertes)    │ ║
║  └──────────┬─────────────────────┬──────────────────────┬────────────┘ ║
╚════════════╪═════════════════════╪══════════════════════╪═════════════╝
             │                     │                      │
      ┌──────▼──────┐      ┌───────▼──────┐      ┌───────▼──────┐
      │   Ollama    │      │  PostgreSQL  │      │    MinIO     │
      │  (local)    │      │  + pgvector  │      │  (fichiers)  │
      │  ou OpenAI  │      │              │      │              │
      │             │      │  Tables +    │      │  PDFs, docs, │
      │  LLM +      │      │  Vecteurs +  │      │  photos      │
      │  Embeddings │      │  Événements  │      │              │
      └─────────────┘      └──────────────┘      └──────────────┘

╔══════════════════════════════════════════════════════════════════════════╗
║                         INTÉGRATIONS EXTERNES                           ║
║                                                                          ║
║   Notion (sync bidirectionnel)      SMTP (alertes, diffusion)           ║
║   Affaires, actions, CR             Notifications automatiques          ║
║   Polling 5 min (v1)                                                    ║
╚══════════════════════════════════════════════════════════════════════════╝
```

### Agents — ce qu'ils appellent exactement

| Agent | Logé dans | Déclenché par | Appelle (FastAPI) | Écrit dans |
|-------|-----------|---------------|-------------------|------------|
| **OS Chantier** | OpenWebUI | Question chat | `GET /rag/query` + `GET /planning/{id}` + `GET /events/{id}` | — (lecture seule) |
| **Agent Planning** | OpenWebUI | "Génère le planning" | `POST /planning/generate` + `POST /planning/simulate` + `GET /rag/query` | PostgreSQL planning |
| **Agent Meeting** | OpenWebUI | CR collé dans le chat | `POST /meeting/analyze` + `PUT /actions/{id}` + `POST /events` | PostgreSQL actions + events |
| **Agent Documents** | OpenWebUI | "Génère le CCTP lot X" | `GET /rag/query` + `GET /affaires/{id}` + `POST /document/generate` | MinIO (fichier) + PostgreSQL (meta) |
| **Event Engine** | FastAPI (background) | Changement de données (LISTEN/NOTIFY) | Interne — lit PostgreSQL | PostgreSQL events + SMTP |
| **Memory Engine** | FastAPI (background) | Q&R répondues + CR analysés | Interne | PostgreSQL pgvector (Couche 2/3) |
