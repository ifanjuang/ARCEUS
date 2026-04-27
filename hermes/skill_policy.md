# Hermes Skill Policy — Pantheon OS

> Règles d’usage des skills Hermes dans Pantheon OS.

---

# 1. Principe

Hermes dispose déjà d’un système de skills built-in, optional et community.

Pantheon ne doit pas dupliquer une capacité Hermes existante.

```text
Hermes skill = capacité exécutable.
Pantheon skill = contrat métier, cadrage, privacy, approval et output attendu.
```

---

# 2. Règle avant création

Avant de créer une skill Pantheon :

```text
1. chercher une skill Pantheon existante ;
2. chercher une skill Hermes built-in ;
3. chercher une skill Hermes optional ;
4. regarder les skills community uniquement comme inspiration ;
5. décider : utiliser, wrapper, créer candidate, rejeter.
```

---

# 3. Décisions possibles

| Décision | Sens |
|---|---|
| `use_existing` | Une skill Pantheon existante suffit |
| `use_hermes_builtin` | Une skill Hermes built-in suffit, avec policy Pantheon |
| `wrap_hermes_skill` | Hermes exécute, Pantheon encadre |
| `create_candidate` | Nouvelle skill Pantheon candidate nécessaire |
| `extend_existing` | Une skill existante doit être améliorée |
| `reject_duplicate` | Le besoin est déjà couvert |
| `block_for_safety` | Skill trop risquée sans sandbox/policy |

---

# 4. Optional skills

Les optional skills Hermes ne sont pas actives par défaut.

Règle Pantheon :

```text
Aucune optional skill Hermes n’est installée ou activée sans review.
```

La review doit vérifier :

- utilité réelle ;
- dépendances ;
- clés API ;
- accès fichiers ;
- accès réseau ;
- actions externes ;
- risques privacy ;
- besoin de sandbox ;
- capacité de rollback.

---

# 5. Community skills

Les community skills sont des sources d’inspiration, pas des capacités approuvées.

Elles doivent être classées :

```text
à intégrer maintenant
à intégrer plus tard
intéressant mais non prioritaire
redondant
risqué
à rejeter
```

Aucune community skill ne doit être activée directement dans un environnement Pantheon réel.

---

# 6. Mapping dans manifest.yaml

Toute skill Pantheon qui utilise Hermes doit indiquer son mapping :

```yaml
hermes_mapping:
  type: wrap_hermes_skill
  hermes_skill: official/category/name
  activation_required: true
  sandbox_required: true
  approval_required: true
```

Si aucune skill Hermes ne correspond :

```yaml
hermes_mapping:
  type: none_found
  checked: true
```

---

# 7. Skills risquées

Sont risquées par défaut :

- terminal ;
- browser automation ;
- web actions ;
- MCP ;
- file mutation ;
- scheduler ;
- gateways ;
- credentials ;
- external APIs ;
- autonomous coding agents.

Règle :

```text
sandbox + visible execution + approval obligatoire
```

---

# 8. Privacy

Aucune donnée réelle issue de conversations privées, projets, clients, entreprises, adresses, chantiers ou personnes identifiables ne doit être injectée dans une skill Hermes sans validation explicite.

Les exemples et tests restent fictifs.

---

# 9. Update

Si une skill Hermes inspire une amélioration Pantheon :

```text
UPDATES.md d’abord.
SKILL.md ensuite seulement après validation.
```

---

# 10. Règle finale

Pantheon encadre Hermes.

Il ne le remplace pas, ne le duplique pas, et ne lui délègue jamais la gouvernance.
