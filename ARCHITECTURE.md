# Pantheon OS — Architecture

> Document de référence.
> Ce fichier décrit la structure cible stable de Pantheon OS.
> Il ne sert pas de changelog et ne doit pas contenir de détails d’implémentation obsolètes.

---

# 1. Vue d’ensemble

Pantheon OS est un système d’exécution multi-agent modulaire pour des environnements professionnels complexes : architecture, conduite de projet, audit, juridique, conseil, IT et documentation technique.

Pantheon OS n’est pas un chatbot. C’est un environnement gouverné où agents, skills, tools, workflows, politiques, mémoire et documents coopèrent dans un runtime contrôlé.

Le système repose sur une séparation stricte entre :

- le control plane, qui décide, planifie, arbitre, valide et gouverne ;
- le data plane, qui exécute les actions autorisées, appelle les outils, persiste les résultats et produit les artefacts.

---

# 2. Architecture générale

```text
User / External Channel
        ↓
OpenWebUI / API Adapters
        ↓
FastAPI API Layer
        ↓
Session Manager
        ↓
Manifest Loader / Registries
        ↓
Workflow Engine
        ↓
Decision Engine / Control Plane
        ↓
Execution Engine / Data Plane
        ↓
Agents / Skills / Tools
        ↓
Memory / Documents / Knowledge
        ↓
Artifacts / Outputs
```

---

# 3. Principes structurants

## 3.1 Core générique

Le dossier `core/` reste indépendant des métiers. Il fournit les contrats, registres, états, moteurs d’exécution, politiques, évaluation, observabilité, mémoire abstraite, documents et fournisseurs LLM.

Aucune logique métier architecture, juridique, chantier, finance ou software ne doit vivre dans le core.

## 3.2 Modularité filesystem-first

Les agents, skills, tools, workflows, prompts et templates sont découverts depuis le filesystem par manifests. Le runtime ne doit pas nécessiter d’enregistrement codé en dur pour chaque nouveau bloc.

## 3.3 Domain overlays hors core

Les comportements métier vivent dans `domains/{domain}/`.

Exemples :

- `domains/architecture/`
- `domains/legal/`
- `domains/software/`
- `domains/consulting/`

Un overlay peut fournir prompts, skills, workflows, policies, trusted sources, templates, evaluation cases et agents spécifiques si nécessaire.

## 3.4 Gouvernance runtime

La criticité, la réversibilité, le draft-first, les veto, les approbations, les escalades et la traçabilité appartiennent au runtime. Ces règles ne doivent pas exister seulement comme instructions de prompt.

## 3.5 Pas de mutation silencieuse

Aucun agent, workflow, outil, skill, mémoire ou politique active ne doit être modifié silencieusement. Les évolutions doivent passer par proposition, validation, versioning ou migration explicite.

---

# 4. Structure du dépôt

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
```

---

# 5. Core layers

## 5.1 Core

Le core contient le moteur générique : contrats, registries, state management, workflow engine, decision engine, execution engine, policy engine, evaluation, learning, observability, memory routing, document intelligence et abstraction LLM.

## 5.2 Modules

Les modules contiennent les blocs réutilisables : agents, skills, tools, workflows, prompts, templates. Ils sont portables et ne doivent pas embarquer de logique métier spécifique sauf si le module est explicitement rattaché à un overlay.

## 5.3 Domains

Les domains portent la valeur métier. Ils peuvent définir des règles de décision, des workflows de dossier, des politiques de sources, des templates et des skills spécialisés.

## 5.4 Platform

La plateforme porte l’API, l’UI, la persistance, les jobs background, le déploiement, le streaming et la console d’administration.

---

# 6. Control plane

Le control plane décide ce qui doit être fait avant exécution.

Responsabilités :

- classification de tâche ;
- décomposition ;
- planification ;
- détection d’incertitude ;
- détection de contradiction ;
- choix de workflow ;
- criticité ;
- routage politique ;
- escalade ;
- arbitrage final.

Objets principaux :

- `DecisionContext`
- `DecisionAction`
- `DecisionPlan`

Agents typiques : ZEUS, ATHENA, METIS, PROMETHEUS, THEMIS, APOLLO, HECATE, HERMES.

---

# 7. Data plane

Le data plane exécute les décisions validées.

Responsabilités :

- exécuter les agents ;
- injecter skills et tools ;
- gérer exécution séquentielle ou parallèle ;
- produire artefacts ;
- persister résultats ;
- journaliser traces et erreurs.

Le data plane ne doit jamais contourner policy, criticité, veto ou validation.

---

# 8. Workflow engine

Un workflow est une structure d’exécution explicite, pas une chaîne de prompts implicite.

Patterns cibles :

- solo ;
- parallel ;
- cascade ;
- arena ;
- conditional routing ;
- clarification checkpoint ;
- pause / resume ;
- merge / fork ;
- child workflows plus tard.

Extensions possibles : LangGraph adapter, checkpoints persistants, exécution graph-based pour workflows complexes.

---

# 9. Manifest loader et registries

Les manifests et registries sont le mécanisme de découverte runtime.

Responsabilités :

- découvrir agents, skills, tools, workflows ;
- valider les manifests au démarrage ;
- exposer état enabled / disabled ;
- maintenir des registries séparées ;
- préparer le versioning futur.

Champs manifest recommandés : `id`, `name`, `type`, `version`, `enabled`, `domain`, `inputs`, `outputs`, `dependencies`, `constraints`, `policy`, `activation`, `tags`.

---

# 10. Governance layer

## 10.1 Criticité

Les niveaux C1-C5 contrôlent profondeur d’exécution, nombre d’agents, approbations, veto, clarification et traçabilité.

## 10.2 Réversibilité

Toute action significative est classée : note interne, écriture mémoire, communication externe, action critique ou irréversible.

## 10.3 Draft-first

Les sorties sérieuses suivent : générer, valider, exécuter ou livrer.

## 10.4 Decision debt

Les décisions provisoires, conditionnelles ou bloquées sont suivies par états explicites D0-D3.

## 10.5 Escalade

Les contradictions, incertitudes fortes, actions C4/C5 ou impacts irréversibles déclenchent escalation ou validation humaine.

---

# 11. Policy layer

Tout appel d’outil ou action à effet de bord passe par un policy gate.

Décisions possibles :

- allow ;
- block ;
- require_approval.

Actions à risque : envoi d’email, modification de données persistantes, action externe, suppression de fichier, mutation de workflow, écriture mémoire forte.

---

# 12. Veto chain

Un veto est une décision structurée : verdict, justification, severity, lift condition.

Chaîne cible :

```text
execute_agents
→ veto_check
→ veto_themis
→ veto_zeus
→ zeus_judge
```

Niveaux : warning ou blocking.

---

# 13. Memory system

Pantheon OS utilise une mémoire multi-couches, sélective et auditable. La mémoire ne doit jamais devenir un dump de contexte.

## 13.1 Typologie mémoire

La mémoire distingue au minimum :

- `raw_history` : messages bruts, événements, tool outputs, actions, documents, traces ;
- `candidate_facts` : faits proposés par extraction, réflexion ou import, non encore validés ;
- `active_facts` : faits durables validés et sourcés ;
- `summaries` : résumés de session, workflow, document, affaire ou fenêtre temporelle ;
- `cards` : vues compactes synthétiques utilisées pour l’injection rapide ;
- `traces` : décisions d’orchestration, veto, validations, erreurs, jobs, statuts ;
- `knowledge` : corpus documentaire, markdown indexé, templates, sources de référence.

## 13.2 Source de vérité

Les sources brutes restent prioritaires. Les facts, summaries et cards sont des couches dérivées et reconstruisibles.

Une carte compacte n’est pas une source de vérité. Elle est une vue synthétique destinée à réduire le coût de contexte.

## 13.3 Exigence d’auditabilité

Toute mémoire injectée dans un prompt doit être :

- inspectable ;
- sourcée ;
- reliée à une affaire, session, agent, document, message ou action ;
- révisable ;
- rétractable ou supersédable ;
- visible dans les traces d’exécution.

## 13.4 Cycle mémoire cible

```text
raw input / event / document / message
→ extraction ou réflexion
→ candidate fact
→ validation agent ou règle déterministe
→ active fact
→ consolidation prudente
→ card / summary / context injection
```

## 13.5 Dry-run obligatoire

Toute opération qui promeut, fusionne, rétracte, supersède ou condense la mémoire doit supporter un mode dry-run ou preview avant application, sauf écriture triviale de trace brute.

## 13.6 Propriétaires agents

- HESTIA : mémoire projet et continuité d’affaire ;
- MNEMOSYNE : mémoire agence, patterns, templates, capitalisation ;
- HADES : retrieval profond et archives ;
- ARGOS : extraction objective de faits et preuves ;
- THEMIS : légitimité procédurale des promotions sensibles ;
- ZEUS : arbitrage des conflits mémoire importants.

## 13.7 Stockage cible

Pantheon conserve PostgreSQL + pgvector comme socle principal. Les idées issues de systèmes local-first type Hermes Local Memory sont retenues au niveau doctrine : inspectabilité, raw history, facts candidats, cards compactes, dry-runs, consolidation explicite. Elles ne justifient pas de remplacer PostgreSQL/pgvector par SQLite.

---

# 14. Post-run memory routing

Après synthèse, le runtime route explicitement :

- contexte temporaire → session memory ;
- décision projet validée → HESTIA ;
- pattern réutilisable → proposition MNEMOSYNE ;
- contradiction → debt ou escalation ;
- bruit → ignoré.

Aucun output complet ne doit être automatiquement promu comme mémoire durable sans extraction, filtrage et validation.

---

# 15. Knowledge layer

La knowledge layer est distincte de la mémoire runtime. Elle contient prompts, templates, markdown indexé, documentation, exemples, trusted sources et corpus de référence.

Elle supporte retrieval et génération, mais ne remplace pas la mémoire de continuité.

---

# 16. Document intelligence layer

Responsabilités : ingestion, parsing, chunking, indexation, retrieval hybride, citations, cache de synthèse, support multilingue et extension multimodale.

Métadonnées cibles : fichier, page, section, langue, source id, affaire, version, date d’ingestion, statut de fiabilité.

---

# 17. Evaluation and learning

Pantheon évalue structure, confiance, qualité des citations, latence, clarification, workflow, supervision et feedback.

Le learning reste contrôlé : feedback, gap analysis, propositions candidates, promotion validée. Pas de self-mutation silencieuse.

---

# 18. Observability

Le système trace agents, tools, prompts, décisions, workflows, scores, feedback, actions bloquées, approvals, vetoes, coûts, latences, mémoire injectée et changements de mémoire.

La console doit permettre d’inspecter pourquoi un résultat a été produit et quel contexte a été injecté.

---

# 19. External interfaces

OpenWebUI est l’interface principale, pas le runtime. Les canaux futurs Telegram, WhatsApp, voix ou API externe passent par le même runtime gouverné.

---

# 20. Contraintes de conception

- pas de logique métier dans `core/` ;
- pas d’exécution d’outil non gouvernée ;
- pas de workflow caché dans des prompts ;
- pas de mutation silencieuse ;
- pas de dépendance runtime à l’UI ;
- pas de confusion agent / skill / tool / workflow ;
- pas de croissance mémoire incontrôlée ;
- pas de mémoire injectée non inspectable.

---

# 21. Relation avec ROADMAP.md

`ARCHITECTURE.md` décrit les principes stables. `ROADMAP.md` définit le séquençage d’implémentation.

---

# 22. Relation avec STATUS.md

`STATUS.md` dit ce qui est réellement livré, partiel, à faire ou en exploration. En cas d’écart entre ce document et le code, le statut doit clarifier la situation.

---

# 23. Résultat cible

Pantheon OS doit rester un système multi-agent contrôlé où raisonnement, exécution, validation, mémoire et gouvernance sont explicites, modulaires, portables, testables et inspectables.
