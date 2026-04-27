# Pantheon OS — Modules

> Document de référence. Définit la structure réelle du système après pivot Hermes-backed.

---

# 1. Principe

Pantheon ne réimplémente pas le runtime.

```text
Pantheon = définition et gouvernance
Hermes = exécution
OpenWebUI = interface + knowledge
```

Un module Pantheon doit être lisible, versionnable et gouvernable.

---

# 2. Structure des modules

## 2.1 Agents (transverse)

```text
agents/
```

Agents = rôles cognitifs abstraits.

Aucun métier ici.

---

## 2.2 Domain packages

```text
domains/
  general/
  architecture/
  software/
```

Chaque domaine contient :

```text
domains/{domain}/
  domain.md
  skills/
  workflows/
  templates/
```

Règle stricte :

```text
Une capacité ne peut exister que dans un seul domaine.
```

---

## 2.3 Skills

Structure :

```text
SKILL.md
manifest.yaml
examples.md
tests.md
UPDATES.md
```

Cycle :

```text
candidate → review → active → upgrade → version
```

Règles :

- une skill n’est jamais modifiée directement ;
- toute évolution passe par UPDATES.md ;
- validation humaine obligatoire ;
- aucune donnée réelle autorisée.

---

## 2.4 Workflows

```text
domains/{domain}/workflows/*.yaml
```

Workflow = procédure structurée.

Pas de prompt déguisé.

---

## 2.5 Memory

```text
memory/
  session/
  candidates/
  project/
  system/
```

Cycle :

```text
SESSION → CANDIDATE → validation → PROJECT ou SYSTEM
```

Aucune promotion automatique.

---

## 2.6 Knowledge

```text
knowledge/
```

Pantheon définit.
OpenWebUI stocke.

---

## 2.7 Policies

```text
policies/
```

Contient les règles globales :

- approval
- privacy
- tool access
- memory

---

# 3. Triage obligatoire

Avant toute modification :

```text
classifier la demande
```

Types :

```text
situation
project memory
system memory
skill
workflow
new capability
policy
```

Aucune modification directe sans classification.

---

# 4. Création à la volée

Si une capacité n’existe pas :

```text
1. vérifier existant
2. vérifier nom
3. proposer candidate
4. valider
5. créer
```

Jamais de création directe.

---

# 5. Naming

Format :

```text
objet_action
```

Exemples :

```text
devis_cctp
cctp_completude
chantier_cr
```

Pas de phrases longues.

---

# 6. Évolution et XP

XP uniquement si :

- amélioration réelle
- blocage détecté
- correction

Règles :

```text
XP → review → validation → level éventuel
```

Pas d’auto-level.

---

# 7. Privacy

Règle absolue :

```text
aucune donnée réelle dans le repo
```

- pas de client
- pas de projet
- pas d’adresse
- pas de nom

Exemples fictifs uniquement.

---

# 8. Hermes integration

Pantheon n’exécute pas.

Il :

- référence les skills Hermes
- les encadre
- filtre leur usage

---

# 9. Anti-patterns

- duplication Hermes
- skill non validée active
- mémoire automatique
- données réelles stockées
- multi sources de vérité

---

# 10. Règle finale

```text
Simple, lisible, gouverné.
```

Tout ce qui complexifie sans gain est rejeté.
