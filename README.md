# Pantheon OS

Pantheon OS est un Domain Operating Layer pour systèmes d’agents appliqués aux environnements professionnels à forte densité documentaire : architecture, chantier, urbanisme, conduite de projet, audit, juridique, conseil et software.

Pantheon OS n’est plus conçu prioritairement comme un runtime agentique autonome complet. La trajectoire retenue est désormais Hermes-backed :

- OpenWebUI expose l’interface de chat et les knowledge bases documentaires.
- NousResearch/Hermes Agent fournit le runtime agentique, les skills exécutables, la mémoire opérationnelle, les tools, le scheduler, le doctor, les gateways et les backends d’exécution.
- Pantheon OS définit la gouvernance métier : agents abstraits, domain overlays, workflows, skills contracts, règles d’approbation, stratégie knowledge, mémoire validée et documentation source de vérité.

Formule de conception :

```text
Pantheon définit.
Hermes exécute.
OpenWebUI expose et retrouve.
```

---

# 1. Rôle de Pantheon OS

Pantheon OS contient les règles qui spécialisent un runtime agentique généraliste pour un usage professionnel contrôlé.

Il définit :

- les agents abstraits et leurs responsabilités ;
- les domain overlays ;
- les workflows métier ;
- les skills contracts ;
- les policies d’action ;
- les règles de mémoire ;
- les règles d’approbation ;
- les formats de sortie ;
- les sources documentaires fiables ;
- la mémoire projet et agence validée ;
- la veille externe ;
- le protocole de coordination IA.

Pantheon ne doit pas dupliquer inutilement les capacités déjà fournies par Hermes Agent : CLI, gateway, scheduler, terminal backends, runtime de skills, doctor et mémoire opérationnelle.

---

# 2. Architecture cible

```text
Utilisateur
  ↓
OpenWebUI
  - chat
  - knowledge documentaire
  - RAG simple
  ↓
Hermes Agent
  - runtime agentique
  - skills exécutables
  - tools
  - scheduler
  - gateway
  - doctor
  - mémoire opérationnelle
  ↓
Pantheon OS
  - agents abstraits
  - domain overlays
  - workflows
  - skills contracts
  - policies
  - mémoire validée
  - documentation source de vérité
```

Pantheon n’est pas un simple dossier de prompts. C’est le référentiel contractuel qui encadre l’usage de Hermes et d’OpenWebUI.

---

# 3. Répartition des responsabilités

| Couche | Responsabilité | Ne doit pas faire |
|---|---|---|
| OpenWebUI | Interface chat, knowledge documentaire, RAG simple | Définir les agents officiels, porter la mémoire validée, gouverner les actions |
| Hermes Agent | Exécuter, utiliser les skills, automatiser, mémoriser opérationnellement, diagnostiquer | Redéfinir seul la doctrine Pantheon, promouvoir une mémoire non validée comme vérité |
| Pantheon OS | Définir, gouverner, versionner, valider, documenter | Réimplémenter sans gain le runtime agentique, scheduler, gateway ou doctor |

---

# 4. Agents

Les agents Pantheon restent neutres métier. Ils sont des rôles cognitifs génériques, pas des agents spécialisés architecture ou software.

Exemples :

- ZEUS : orchestration et arbitrage ;
- ATHENA : planification et décomposition ;
- ARGOS : extraction factuelle et preuves ;
- THEMIS : procédure, règles, risques et légitimité ;
- APOLLO : validation finale et confiance ;
- PROMETHEUS : contradiction et stress-test ;
- HESTIA : mémoire projet ;
- MNEMOSYNE : mémoire agence ;
- IRIS : communication ;
- HEPHAESTUS : analyse technique.

Le métier vient des overlays, skills, workflows et knowledge sources.

---

# 5. Domain overlays

Les domaines portent la spécialisation.

Exemples :

```text
domains/
  architecture/
  software/
  legal/
  consulting/
```

Un domain overlay peut contenir :

- règles métier ;
- workflows ;
- skills ;
- templates ;
- politiques de sources ;
- formats de sortie ;
- exemples ;
- tests ;
- règles de mémoire.

Exemple : THEMIS reste un agent abstrait de conformité. Dans le domaine architecture, l’overlay lui fournit les contrôles liés aux missions, CCTP, DPGF, DOE, DGD, réception, ERP, SDIS, PLU ou clauses contractuelles.

---

# 6. Skills

Les skills sont définies dans Pantheon et exécutées par Hermes.

Règle :

```text
Pantheon définit la skill.
Hermes l’exécute.
Toute skill auto-créée reste candidate tant qu’elle n’est pas validée.
```

Structure cible :

```text
skills/
  architecture/
    cctp_audit/
      SKILL.md
      manifest.yaml
      examples.md
      tests.md
    dpgf_check/
      SKILL.md
      manifest.yaml
  software/
    repo_md_audit/
      SKILL.md
      manifest.yaml
```

Chaque skill doit définir : objectif, inputs, outputs, agents mobilisés, sources autorisées, risques, approval nécessaire, format attendu, exemples et tests.

---

# 7. Knowledge

OpenWebUI peut porter les collections documentaires.

Pantheon conserve la stratégie :

```text
knowledge/
  openwebui_collections.md
  source_policy.md
  document_taxonomy.md
```

Règle :

```text
OpenWebUI retrouve.
Pantheon décide ce qui fait foi.
Hermes exploite.
```

Les documents lourds, PDF, CCTP, notices, PLU, rapports, guides et modèles peuvent être placés dans OpenWebUI Knowledge. Les règles de gouvernance et les décisions projet doivent rester dans Pantheon.

---

# 8. Mémoire

La mémoire est séparée en trois niveaux :

| Mémoire | Emplacement | Statut |
|---|---|---|
| documentaire | OpenWebUI Knowledge | consultable |
| opérationnelle | Hermes Agent | vivante, pratique, non souveraine |
| validée | Pantheon OS | source de vérité |

Règle :

```text
Hermes peut apprendre.
Pantheon valide.
OpenWebUI documente.
```

Toute information issue de Hermes qui modifie une règle, une décision, une skill ou une mémoire durable doit être proposée comme candidate avant intégration dans Pantheon.

---

# 9. Approval et sécurité

Au stade Hermes-backed, l’Approval Gate peut d’abord être documentaire et opératoire, puis logiciel si nécessaire.

Règles minimales :

- diagnostic : autorisé ;
- modification de fichier : validation requise ;
- envoi d’email : validation requise ;
- suppression : confirmation explicite ;
- commande shell hors allowlist : validation requise ;
- promotion mémoire : validation requise ;
- activation d’une skill candidate : validation requise ;
- action web avec effet de bord : validation requise.

Hermes peut exécuter, mais ne doit pas contourner les règles Pantheon.

---

# 10. Structure cible simplifiée

```text
Pantheon-OS/
  README.md
  STATUS.md
  ROADMAP.md
  ARCHITECTURE.md
  AGENTS.md
  MODULES.md
  AI_LOG.md
  EXTERNAL_WATCHLIST.md

  agents/
    zeus.md
    athena.md
    argos.md
    themis.md
    apollo.md
    prometheus.md
    hestia.md
    mnemosyne.md
    iris.md
    hephaestus.md

  domains/
    architecture/
      overlay.md
      rules.md
      knowledge_policy.md
      output_formats.md
      workflows/
      skills/
      templates/

  skills/
    architecture/
    software/
    generic/

  workflows/
    architecture/
    software/
    generic/

  memory/
    project/
    agency/
    candidates/

  knowledge/
    openwebui_collections.md
    source_policy.md
    document_taxonomy.md

  hermes/
    context/
    exports/

  operations/
    install.md
    update.md
    backup.md
    doctor.md
```

---

# 11. Développement

Les Markdown restent la base du développement.

Les six fichiers de référence sont :

- `STATUS.md` ;
- `ROADMAP.md` ;
- `ARCHITECTURE.md` ;
- `AGENTS.md` ;
- `MODULES.md` ;
- `README.md`.

Avant toute modification du code, vérifier la cohérence avec ces fichiers. Si le code existant est meilleur que la documentation, mettre à jour la documentation avant de généraliser ce code.

---

# 12. État actuel

Le dépôt contient encore des éléments de l’ancienne trajectoire Pantheon autonome : FastAPI, registries, workflows, approvals, installer UI, manifests et tests partiels.

Ces éléments ne sont pas supprimés. Ils sont à réauditer après le pivot :

- soit conservés comme outils d’intégration ;
- soit simplifiés ;
- soit archivés ;
- soit réorientés vers Hermes-backed Pantheon.

La prochaine étape n’est pas d’ajouter du code. La prochaine étape est l’audit de cohérence post-pivot.
