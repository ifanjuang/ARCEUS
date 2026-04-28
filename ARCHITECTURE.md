# ARCHITECTURE — Pantheon OS

> Document de référence technique. Décrit l’architecture réelle après pivot Hermes-backed.

---

# 1. Décision structurante

Pantheon OS est un Domain Operating Layer.

```text
Pantheon définit.
Hermes exécute.
OpenWebUI expose et retrouve.
```

Pantheon ne doit pas réimplémenter les sous-systèmes déjà présents dans Hermes Agent : boucle agentique, prompt assembly, provider resolution, tool registry, terminal/browser/web/MCP backends, session storage, scheduler, gateways, optional skills ou skills hub.

---

# 2. Architecture en couches

```text
OpenWebUI
  interface utilisateur
  knowledge documentaire

Pantheon OS
  agents abstraits
  domain packages
  skills métier
  workflows
  memory policies
  approval policies
  Hermes skill policy

Hermes Agent
  agent loop
  prompt assembly
  provider runtime resolution
  tool registry
  session storage
  cron scheduler
  gateways
  optional skills
```

Hermes est le runtime. Pantheon est le système de définition, gouvernance et spécialisation métier.

---

# 3. Domain packages

Structure officielle :

```text
domains/
  general/
    domain.md
    skills/
    workflows/
    templates/
  architecture_fr/
    domain.md
    skills/
    workflows/
    templates/
  software/
    domain.md
    skills/
    workflows/
    templates/
```

`general` contient les capacités invariantes du système : triage, vérification, création à la volée, memory promotion, skill/workflow design, repo inspiration, source check, prompt system design.

`architecture_fr` contient les capacités métiers francophones : CCTP, devis, DPGF, notices, chantier, PLU, ERP/SDIS, responsabilités et marchés travaux.

Règle : le domaine métier français ne doit pas être recréé sous `domains/architecture/`.

---

# 4. Hermes skill strategy

Avant de créer une skill Pantheon :

```text
1. chercher une skill Pantheon existante ;
2. chercher une skill Hermes built-in ou optional ;
3. vérifier les skills community uniquement comme inspiration ;
4. décider : use_existing, wrap_hermes_skill, create_candidate, reject_duplicate ;
5. créer seulement après validation.
```

Règle :

```text
Pantheon skill = contrat métier + gouvernance.
Hermes skill = capacité exécutable.
```

Si Hermes possède déjà une capacité technique, Pantheon ne la recode pas. Il crée éventuellement un wrapper métier qui définit contexte, inputs, outputs, approvals, privacy, memory impact et templates.

---

# 5. Skills et lifecycle

Structure minimale d’une skill Pantheon :

```text
SKILL.md
manifest.yaml
examples.md
tests.md
UPDATES.md
```

`SKILL.md` est la version active.
`UPDATES.md` contient les propositions.
`manifest.yaml` contient statut, level, XP, policy et éventuel mapping Hermes.

Aucun level ne change sans review, optimisation et validation.

XP possible uniquement si :

- amélioration réelle ;
- blocage identifié ;
- blocage corrigé ;
- méthode simplifiée ;
- garde-fou ajouté.

---

# 6. Workflows

Les workflows sont des YAML dans :

```text
domains/{domain}/workflows/*.yaml
```

Ils décrivent des procédures structurées et testables.

Un workflow ne doit pas être un prompt long déguisé.

---

# 7. Mémoire

Structure :

```text
memory/
  session/
  candidates/
  project/
  system/
```

Règles :

```text
session    = temporaire
candidates = persisté non validé
project    = contexte projet validé
system     = règles, méthodes, patterns validés
```

Cycle :

```text
SESSION → CANDIDATES → validation → PROJECT ou SYSTEM
```

Aucune promotion automatique.

---

# 8. Privacy by default

Aucune donnée réelle issue de conversations privées, projets, clients, entreprises, chantiers, adresses, personnes ou situations identifiables ne doit être inscrite dans le repo.

Les exemples, tests et templates doivent être fictifs, neutres et non traçables.

Toute promotion mémoire doit vérifier l’anonymisation.

---

# 9. Change triage

Avant toute modification, Pantheon doit classifier la demande :

```text
situation
project_memory
system_memory
skill_update
workflow_update
new_capability
policy_update
```

La classification détermine la cible et le niveau de validation.

---

# 10. Sécurité runtime

Les capacités risquées restent côté Hermes mais doivent être policy-gated par Pantheon :

- browser automation ;
- terminal ;
- web actions ;
- MCP ;
- file mutations ;
- scheduler ;
- gateways ;
- memory providers ;
- optional/community skills.

Règles minimales :

- sandbox ou Docker pour outils risqués ;
- pas de Docker socket au démarrage ;
- pas d’accès secrets sans policy ;
- pas d’action externe sans approval ;
- visible execution obligatoire ;
- logs et traçabilité.

---

# 11. Hermes context strategy

Hermes assemble le prompt depuis personnalité, mémoire, skills, context files, tool guidance et instructions modèle.

Pantheon fournit donc des contextes contrôlés :

```text
hermes/context/
  pantheon_context.md
  agents_context.md
  memory_context.md
  rules_context.md
  architecture_fr_context.md
  software_context.md
```

Ces fichiers ne remplacent pas les Markdown de référence. Ils exportent une version opérationnelle stable pour Hermes.

---

# 12. Installation et exploitation

Environnement cible : NAS avec Portainer, OpenWebUI existant, PostgreSQL existant et Ollama sur PC LAN.

Règles :

- ne jamais écraser une stack existante ;
- détecter avant d’installer ;
- isoler Hermes Lab ;
- ne pas exposer inutilement PostgreSQL ;
- ne pas utiliser de tag Docker instable en production ;
- tester localement avant merge.

---

# 13. Code existant

Le dépôt contient encore des éléments de l’ancienne architecture autonome : FastAPI apps, registries, workflow loader, approvals, installer UI, migrations et tests legacy.

Statut : legacy à auditer.

Aucune suppression automatique avant diagnostic.

---

# 14. Règle finale

Pantheon doit rester plus simple que le runtime qu’il gouverne.

Si une capacité existe déjà dans Hermes, Pantheon doit l’encadrer, pas la dupliquer.
