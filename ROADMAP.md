# ROADMAP
> Feuille de route consolidée pour faire évoluer Pantheon OS vers un système multi-agents modulaire, gouverné, portable par conception et exploitable dans des contextes professionnels à forte exigence.
>
> Thèse produit :
> Pantheon Next n’est pas un chatbot.
> C’est un environnement d’exécution contrôlé où des agents spécialisés, des workflows explicites, des skills réutilisables, des tools gouvernés et des politiques de risque coopèrent comme une équipe experte structurée.
---
# 1. Vision
Pantheon Next est un système multi-agents pour le travail professionnel complexe.
Il vise les contextes à forte densité de règles, de documents, de coordination et de responsabilité :
- architecture
- maîtrise d’œuvre
- conformité
- juridique
- audit
- conseil
- IT
- recherche documentaire
Le système doit rester :
- modulaire
- explicable
- inspectable
- gouverné
- portable entre métiers
Le moteur doit rester générique.
La valeur métier doit vivre dans des overlays de domaine.
---
# 2. Règles de préservation
Cette section est la plus importante.
Tout refactoring, toute nouvelle brique, toute optimisation ou expérimentation doit respecter ces règles.
## 2.1 Le core reste générique
Le core fournit :
- contrats
- exécution
- routing
- state
- registries
- policies
- évaluation
- observabilité
- mémoire
- services documentaires
Le core ne doit pas contenir de logique métier spécifique à l’architecture, au droit ou à un secteur donné.
## 2.2 Le filesystem reste la source de vérité
L’ajout d’un agent, d’un skill, d’un tool ou d’un workflow doit rester piloté par :
- un dossier
- un manifest
- un contrat valide
Le runtime découvre les briques.
Le code central ne doit pas être modifié pour chaque ajout.
## 2.3 Agent, skill, tool et workflow restent distincts
- un agent raisonne
- un skill applique une capacité réutilisable
- un tool exécute une action technique ou externe
- un workflow structure l’exécution globale
Ces couches ne doivent pas se confondre.
## 2.4 Les workflows restent explicites
L’exécution doit rester :
- structurée
- lisible
- traçable
- testable
Le système ne doit pas dériver vers une chaîne implicite de prompts.
## 2.5 La gouvernance reste explicite
Pantheon doit préserver :
- criticité
- réversibilité
- draft-first
- veto
- escalade
- validation humaine sur les actions risquées
- dette décisionnelle
## 2.6 La mémoire reste multi-couches et sélective
Pantheon doit préserver :
- mémoire session
- mémoire projet
- mémoire agence / globale
La mémoire ne doit jamais devenir un dump de contexte.
## 2.7 Les sorties restent structurées
Pour les runs sérieux, la sortie doit continuer à expliciter :
- contexte
- constats
- analyse
- niveau de certitude
- impacts
- options
- validation requise
- cible mémoire
## 2.8 Les overlays métier restent hors du core
La valeur métier doit être portée par :
- `domains/architecture/`
- `domains/legal/`
- `domains/software/`
- autres overlays futurs
Pas par le noyau runtime.
---
# 3. Architecture cible
```text
platform/
  api/              FastAPI apps
  ui/               OpenWebUI integration + admin console
  data/             persistence and runtime state
  infra/            Docker, deployment, scripts
core/
  contracts/        base types and interfaces
  registry/         agent, skill, tool, workflow registries
  decision/         control plane
  execution/        data plane
  state/            session and run state
  policies/         policy engine and action gate
  evaluation/       scorecards and tests
  learning/         controlled improvement loop
  observability/    traces, logs, runs
  memory/           session, project, agency adapters
  documents/        ingestion, indexing, retrieval, citation
  packaging/        context and artifact bundles
  llm/              provider abstraction, budget, routing
modules/
  agents/           modular agents
  skills/           reusable reasoning skills
  tools/            external actions and connectors
  workflows/        workflow packs
  prompts/          prompt libraries
  templates/        output templates
domains/
  architecture/
  legal/
  software/
  consulting/

⸻

4. Modèle overlays métier

Chaque overlay métier doit pouvoir embarquer ses propres briques sans modifier le core.

Chaque overlay peut contenir :

* prompts/
* skills/
* workflows/
* policies/
* trusted_sources/
* templates/
* evaluation_cases/
* agents spécifiques si nécessaire

Activation prévue par configuration :

* domaine actif
* overlays activés
* injection runtime déterministe

Exemple :

domains/
  architecture/
    prompts/
    skills/
    workflows/
    policies/
    templates/
    trusted_sources/

⸻

5. Panthéon d’agents

5.1 Agents meta / contrôle

ZEUS

Orchestration globale, arbitrage, coordination finale.

ATHENA

Planification, classification, décomposition, choix de workflow.

METIS

Délibération structurée, hypothèses, conflits, incertitudes.

PROMETHEUS

Contradiction, critique, adversarial review, prévention du faux consensus.

THEMIS

Légitimité procédurale, cohérence des règles, contrôle process.

HERA

Supervision post-run, scoring d’orchestration, verdict de cohérence.

APOLLO

Validation finale, confiance, traçabilité des sources.

HECATE

Détection des manques, score d’incertitude, clarification nécessaire.

5.2 Agents recherche et analyse

HERMES

Précheck, routing des recherches, stratégie de sources.

DEMETER

Collecte et normalisation documentaire.

ARGOS

Extraction objective : faits, citations, entités, relations.

ARTEMIS

Filtrage de pertinence, réduction du bruit.

5.3 Agents mémoire

HESTIA

Continuité de session et mémoire projet.

MNEMOSYNE

Capitalisation agence, patterns, templates, documentation réutilisable.

HADES

Recherche profonde, archive, retrieval longue durée.

5.4 Agents de sortie

KAIROS

Synthèse contextuelle, niveau de détail adapté.

DAEDALUS

Assemblage documentaire, dossiers, rapports, annexes.

IRIS

Formulation, tonalité, questions de clarification, reformulation.

HEPHAESTUS

Diagrammes, artefacts techniques, visuels structurés.

APHRODITE

Polish, impact, marketing. Jamais auto-activée par défaut.

5.5 Agents système

ARES

Mode rapide dégradé, fallback, garde d’exécution.

POSEIDON

Charge, parallélisme, régulation de flux.

⸻

6. Modèle de gouvernance

6.1 Criticité C1 à C5

* C1 : information
* C2 : question simple / assistance
* C3 : décision locale / assistance structurée
* C4 : décision engageante
* C5 : risque majeur

La criticité doit piloter :

* profondeur d’exécution
* nombre d’agents
* besoin de validation
* activation des vetos
* exigences de traçabilité

6.2 Réversibilité

Chaque action doit être classée :

* note interne
* écriture mémoire
* communication externe
* action critique / irréversible

6.3 Draft-first

Toute action sérieuse doit suivre :

* génération
* validation
* exécution

6.4 Dette décisionnelle

États :

* D0 : résolue
* D1 : provisoire
* D2 : sous réserve
* D3 : bloquée / critique

Chaque dette doit garder :

* justification
* condition de levée
* échéance éventuelle
* phase de revue

6.5 Chaîne de veto structurée

Le veto n’est pas un booléen brut.

Chaque veto doit inclure :

* verdict
* justification
* severity
* lift_condition

Chaîne cible :

execute_agents
→ veto_check
→ veto_themis
→ veto_zeus
→ zeus_judge

Niveaux de veto :

* warning
* blocking

⸻

7. Mémoire

7.1 Couches mémoire

Session

Contexte court terme de run.

Projet

Décisions, contraintes, hypothèses, dette, arbitrages.

Agence / globale

Patterns, templates, cas récurrents, capitalisation.

7.2 Règles de routage

Après un run :

* contexte temporaire → session
* décision projet validée → Hestia
* pattern réutilisable détecté → proposition Mnemosyne
* bruit → ignoré

7.3 Post-run memory routing

Cette mécanique doit devenir explicite.

Après synthèse :

* si décision validée → mémoire projet
* si pattern utile → proposition de capitalisation
* pas de dump automatique brut

⸻

8. Stratégie documentaire

Le système doit limiter le contexte chargé au démarrage.

8.1 Noyau documentaire auto-chargé

* AGENTS.md
* ARCHITECTURE.md
* éventuellement un QUICK_START.md

8.2 Documentation non auto-chargée

* docs/learnings/
* docs/archive/
* runs/
* sessions/
* historiques anciens

8.3 Compression ciblée

À terme, certains documents de contexte peuvent avoir :

* une version humaine source
* une version runtime condensée

Sans changer le style de réponse global.

⸻

9. Phases d’implémentation

La roadmap est structurée en 10 grandes phases.

⸻

10. Phase A — Fondation MVP

Objectif

Construire une boucle d’exécution contrôlée qui fonctionne de bout en bout.

Tâches

* squelette FastAPI
* PostgreSQL + pgvector + SQLAlchemy async
* auth JWT + RBAC simple
* manifests pour agents, skills, tools, workflows
* AgentBase, SkillBase, ToolBase, WorkflowBase
* SessionState, RunState, Artifact
* un workflow minimal
* un agent minimal avec SOUL.md
* un tool derrière gate policy
* route OpenWebUI compatible
* streaming SSE
* ingestion documentaire simple
* retrieval simple avec citations
* logs de run

Références Git

Infrastructure et API :

* tiangolo/fastapi
* sqlalchemy/sqlalchemy
* pgvector/pgvector-python

Contrats et runtime :

* All-Hands-AI/OpenHands
* pydantic/pydantic-ai
* instructor-ai/instructor
* guardrails-ai/guardrails

Documentation agent-facing :

* agentsmd/agents.md

Manifests et modularité :

* mnfst/manifest

Démarrage documentaire minimal :

* nadimtuhin/claude-token-optimizer  ￼

Critères de réussite

* API qui démarre proprement
* manifests validés au boot
* un workflow bout en bout fonctionne
* une réponse streamée atteint OpenWebUI
* un document peut être ingéré et cité

⸻

11. Phase B — Orchestration contrôlée

Objectif

Séparer clairement décision et exécution.

Tâches

* DecisionContext
* DecisionAction
* DecisionPlan
* DecisionEngine
* séparation control plane / data plane
* DAG de workflow
* patterns :
    * solo
    * parallel
    * cascade
    * arena
* criticité C1-C5
* checkpoints HITL
* veto nodes
* limites cognitives par criticité
* triggers d’activation par agent
* résolution de conflits structurée

Références Git

Orchestration et graphes :

* langchain-ai/langgraph

Délibération :

* beomwookang/deliberate

Planification / routing :

* salesforce-misc/switchplane

Spécification avant exécution :

* JuliusBrussee/cavekit pour la logique sketch → map → make → check et la structuration requirements / acceptance criteria / dependency graph.  ￼

Critères de réussite

* le système produit un plan avant d’exécuter
* la criticité modifie réellement l’exécution
* un workflow peut être stoppé, validé et repris
* les vetos sont visibles et justifiés

⸻

12. Phase C — Contexte, mémoire et efficacité

Objectif

Réduire le contexte inutile, préserver la continuité et limiter le gaspillage de tokens.

Tâches

* mémoire session / projet / agence formalisée
* externalisation des gros résultats
* récupération ciblée par recherche
* checkpoints de session
* smart_read
* smart_diff
* smart_grep
* cache persistant
* analytics de session
* démarrage avec contexte minimal
* reprise après compaction / crash

Références Git

Gestion du contexte et continuité :

* mksglu/context-mode pour :
    * garder le brut hors du contexte
    * tracer les événements de session en SQLite
    * récupérer le pertinent via FTS/BM25
    * pousser l’agent à “penser en code” quand c’est plus efficace.  ￼

Optimisation de lecture et cache :

* ooples/token-optimizer-mcp pour :
    * smart tool replacements
    * cache persistant SQLite
    * analytics de session
    * compression et récupération optimisée.  ￼

Réduction du contexte de départ :

* nadimtuhin/claude-token-optimizer pour la séparation entre fichiers essentiels et documentation dormante.  ￼

Compression ciblée :

* JuliusBrussee/caveman pour l’idée de compression de documents de contexte et de réduction forte des tokens de sortie, sans reprendre le style caveman lui-même.  ￼

Critères de réussite

* le système ne réinjecte plus massivement du brut dans le prompt
* la continuité de session est robuste
* les lectures répétées coûtent moins
* la console expose des métriques de contexte et de tokens

⸻

13. Phase D — Policy, sécurité et gouvernance

Objectif

Rendre les actions risquées gouvernables, auditables et bloquables.

Tâches

* PolicyEngine
* ActionGate
* allow / block / require_approval
* secret isolation
* approval API
* lineage source → tool → agent → output
* veto severity
* lift conditions
* escalade
* représentation explicite de la dette décisionnelle

Références Git

Policy engine :

* open-policy-agent/opa

Protection et garde-fous :

* wiserautomation/SupraWall
* guardrails-ai/guardrails

Critères de réussite

* aucune action risquée n’est exécutée silencieusement
* les approbations sont traçables
* chaque sortie peut être reliée à ses sources et à ses étapes de production

⸻

14. Phase E — Évaluation et délibération

Objectif

Mesurer la qualité et réduire les raisonnements faibles ou sur-confiants.

Tâches

* EvaluationRunner
* scorecards
* comparaison de workflows
* metrics :
    * confiance
    * structure
    * citations
    * latence
    * clarification count
    * feedback
* Hera supervision scoring
* Metis deliberation artifacts
* Prometheus contradiction checks
* bullshit risk scoring
* Apollo validation enrichie

Références Git

Évaluation :

* langchain-ai/openevals
* promptfoo/promptfoo
* langfuse/langfuse

Délibération et anti-bullshit :

* beomwookang/deliberate
* jrcruciani/baloney-detection-kit

Critères de réussite

* un workflow candidat peut être benchmarké
* les claims faibles peuvent être rejetés
* l’orchestration reçoit un score de supervision explicite

⸻

15. Phase F — Skills structurés et workflow packs

Objectif

Transformer les patterns répétés en blocs réutilisables et versionnés.

Tâches

* SkillRegistry
* manifests de skills
* versions de skills
* versions de workflows
* statuts :
    * draft
    * candidate
    * active
    * archived
* diff
* rollback
* promotion
* CRUD flows
* seed YAML → DB
* visibilité Hermes Console

Références Git

Skills :

* Hermes Skills system pour :
    * progressive disclosure
    * skills documentaires chargés à la demande
    * taxonomie claire
    * logique de catalogue.  ￼

Catalogue canonique :

* micpet7514088/skills-manager pour :
    * registre d’identité des skills
    * déduplication
    * alias
    * provenance
    * séparation identité / source / activation.  ￼

Manifests :

* mnfst/manifest

Autres inspirations :

* microsoft/semantic-kernel
* JustVugg/distillery

Critères de réussite

* un skill peut être versionné et testé isolément
* un workflow peut être promu ou rollbacké
* le runtime connaît explicitement la version active

⸻

16. Phase G — Intelligence documentaire et knowledge layer

Objectif

Construire une couche documentaire forte, multimodale et traçable.

Tâches

* ingestion PDF, DOCX, MD, TXT
* métadonnées :
    * fichier
    * page
    * section
    * langue
    * source id
* hybrid retrieval
* fusion sémantique + lexicale
* citations fiables
* synthèse réutilisable
* indexation markdown
* à terme multimodal :
    * images
    * plans
    * coupes
    * photos chantier
    * descriptions visuelles
    * qualification technique

Références Git

RAG documentaire :

* deepset-ai/haystack
* run-llama/llama_index
* sahilalaknur21/SmartDocs-Multillingual-Agentic-Rag

Markdown et graphe :

* Fusion/mdidx
* ADVASYS/ragraph
* neo4j/neo4j-python-driver

Critères de réussite

* citations fiables avec page/section
* retrieval hybride plus robuste
* les synthèses critiques peuvent être réutilisées
* les documents internes deviennent une vraie base de connaissance

⸻

17. Phase H — Overlay architecture

Objectif

Porter la valeur métier architecture/BTP sans contaminer le core.

Sous-briques cibles

decisions

* dette décisionnelle D0-D3
* scoring décisionnel
* filtre par état de dette

planning

* lots
* jalons
* dépendances
* dérives
* impacts cascade

chantier

* observations
* non-conformités
* photos
* réserves
* levées

finance

* situations
* avenants
* lignes budget
* alertes dépassement

communications

* registre courriers
* relances
* liens avec actions et CR

webhooks

* Telegram / WhatsApp
* mention-based routing
* support photo
* historique Hestia
* auth expéditeur

Vitruve

* agent d’exploration projet
* programme
* topo
* sol
* PLU
* ABF
* risques
* cohérence budget / contraintes

Critères de réussite

* overlay activable sans toucher au core
* skills métier visibles dans la console
* flux chantier / planning / décision cohérents

⸻

18. Phase I — Observabilité et console

Objectif

Rendre Pantheon inspectable et pilotable.

Tâches

* traces de prompts
* traces de décisions
* traces de tool calls
* scores et feedback
* blocked actions
* workflow comparison UI
* run state
* metrics runtime
* toggles agents/skills/workflows
* logs
* erreurs
* replay plus tard

Références Git

Observabilité :

* langfuse/langfuse
* dagster-io/dagster
* wandb/wandb

Critères de réussite

* on comprend pourquoi un run a produit une sortie
* on visualise les blocages, scores, chemins et versions
* on pilote agents et skills proprement

⸻

19. Phase J — Learning contrôlé

Objectif

Faire progresser le système sans mutation silencieuse.

Tâches

* FeedbackEvent
* feedback explicite :
    * positif
    * négatif
    * tags
* signaux implicites :
    * copy
    * export
    * continue
    * rewrite
* LearningEngine
* GapAnalyzer
* proposition de workflow candidat
* approbation humaine avant activation
* promotion pattern → Mnemosyne
* plus tard pattern → skill sous contrôle

Références Git

Learning et amélioration :

* stanfordnlp/dspy
* micpet7514088/autogap
* swapedoc/hermes2anti

Pour autogap, ce qu’il faut retenir est la logique :

* inférence d’objectif
* top 3 gaps
* top 3 macro-steps
* séparation diagnostic / choix / exécution.  ￼

Critères de réussite

* un feedback négatif produit une amélioration de process
* le système propose des versions candidates, jamais des mutations silencieuses
* Mnemosyne reçoit des patterns utiles, pas du bruit

⸻

20. Phase K — Branche software / code

Objectif

Ajouter une spécialisation code sans la rendre centrale pour tous les domaines.

Tâches

* minimal_code_context
* change_impact_analysis
* architecture_map
* review workflows
* debug workflows
* repo onboarding
* pre-merge checks

Références Git

* tirth8205/code-review-graph pour :
    * graph structurel
    * blast radius
    * contexte minimal
    * revue incrémentale ciblée.  ￼

Critères de réussite

* la branche software améliore les workflows code
* elle reste un overlay / sous-système de domaine
* elle ne devient pas une dépendance universelle

⸻

21. Phase L — Exécution durable et portabilité

Objectif

Préparer les runs longs, la reprise et la migration.

Tâches

* checkpoints
* retries
* replay runner
* export/import des mémoires
* bundles de workflow
* migration inter-serveurs
* plus tard durable orchestration si réellement utile

Références Git

* samuelcolvin/arq
* temporalio/temporal
* awizemann/scarf

Critères de réussite

* un workflow long peut reprendre
* la mémoire projet et agence est exportable
* les runs sont rejouables pour debug et validation

⸻

22. Plan d’optimisation phasé

L’optimisation pilotée par exemples doit rester disciplinée.

Phase 1

Instrumentation seulement.

Phase 2

Optimisation ciblée sur tâches stables et structurées :

* classification criticité
* extraction d’actions
* extraction de métadonnées
* transformations répétitives

Phase 3

Éventuellement extension à Hermes ou Zeus si les exemples sont suffisants.

Règles

* ne jamais optimiser aveuglément les SOUL.md
* ne pas toucher aux agents créatifs ou fortement identitaires au début
* ne pas sacrifier la personnalité du système au profit de l’optimisation

⸻

23. Canaux externes et voix

À intégrer en extension, pas dans le noyau initial.

Cibles

* Telegram
* WhatsApp
* voix
* TTS
* STT
* mapping expéditeur authentifié
* routing par mention
* fallback Hermes
* continuité Hestia entre canaux

⸻

24. Gouvernance Git du repo

Branchement recommandé :

* main : stable
* develop : intégration
* experiment/* : explorations
* overlay/* : overlays métier

Règles :

* toute évolution de schéma → migration
* toute brique critique → test de non-régression
* toute expérimentation V3 reste isolée

⸻

25. Cartographie des inspirations externes

Adopt now

agentsmd/agents.md

Pour le rôle de AGENTS.md comme fichier racine agent-facing.

Hermes Skills system

Pour les skills comme unités documentées, catégorisées, activables.

mnfst/manifest

Pour le déclaratif fort et les manifests enrichis.

nadimtuhin/claude-token-optimizer

Pour le contexte de démarrage minimal.  ￼

Claude Cowork rules

Pour :

* hard rules
* retros
* final-pass gates
* read in full
* crash resilience

V2

mksglu/context-mode

Pour :

* externalisation du brut
* session continuity
* state retrieval ciblé
* analyse par code plutôt que par surcharge de contexte.  ￼

micpet7514088/autogap

Pour :

* gap analysis
* goal hypothesis
* top 3 blockers
* macro-step planning.  ￼

ooples/token-optimizer-mcp

Pour :

* smart reads
* cache persistant
* analytics de session.  ￼

JuliusBrussee/cavekit

Pour :

* spec-first
* acceptance criteria
* dependency graph
* build/check loop.  ￼

V3

swapedoc/hermes2anti

Pour :

* learning loops
* promotion de patterns
* mémoire d’échec/réussite

JuliusBrussee/caveman

Pour :

* compression documentaire runtime
* pas pour le ton de sortie.  ￼

Domaine spécifique code

tirth8205/code-review-graph

Pour :

* blast radius
* minimal code context
* review ciblée.  ￼

Watchlist

All-Hands-AI/OpenHands

Pour :

* packaging public/private
* ordre de chargement
* patterns de runtime

OpenHands/software-agent-sdk

À surveiller pour :

* SDK runtime
* contrats
* registry

⸻

26. Cibles finales

Pantheon Next doit devenir un environnement où :

* les agents restent remplaçables
* les workflows restent versionnés
* les skills restent réutilisables
* les tools restent gouvernés
* la mémoire reste structurée
* l’évaluation pilote l’amélioration
* la validation humaine contrôle les risques
* les overlays métier portent la valeur
* le core reste mince, portable et générique

Thèse finale :

Transformer l’IA d’une interface de chat en une équipe de travail structurée pour les tâches professionnelles complexes.

Les deux compléments les plus logiques après ça sont :
- `domains/architecture/ROADMAP.md`
- `AGENTS.md` final aligné sur cette roadmap