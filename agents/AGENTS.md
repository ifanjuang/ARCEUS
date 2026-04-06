# AGENTS.md — Panthéon ARCEUS : hiérarchie, flux, articulations

---

## Hiérarchie

```
                          ┌─────────────────┐
                          │      ZEUS        │
                          │  Orchestrateur   │
                          │  Arbitrage C3-C5 │
                          └────────┬────────┘
                                   │ distribue / juge / synthétise
              ┌────────────────────┼───────────────────────┐
              │                    │                        │
    ┌─────────▼──────────┐         │             ┌─────────▼──────────┐
    │       HERMÈS        │         │             │       THÉMIS        │
    │  Point d'entrée     │         │             │  Veto contractuel   │
    │  Routing C1-C5      │         │             └────────────────────┘
    └─────────────────────┘         │
                                    │
    ────────────── FAMILLES ─────────────────────────────────────────
    
    PERCEPTION         ANALYSE              CADRAGE
    ──────────         ───────              ───────
    Argos              Athéna               Thémis (veto)
                       Héphaïstos (veto)    Chronos
                       Prométhée            Arès
                       Apollon
                       Dionysos

    CONTINUITÉ         COMMUNICATION        PRODUCTION
    ──────────         ─────────────        ──────────
    Hestia             Iris                 Dédale
    Mnémosyne          Aphrodite
```

---

## Les 16 agents — rôle et position

| # | Agent | Famille | Rôle | Veto |
|---|-------|---------|------|------|
| 0 | **Zeus** | Orchestrateur | Planifie, distribue, arbitre, synthétise | Global |
| 1 | **Hermès** | Perception | Point d'entrée, qualification C1-C5, routing | — |
| 2 | **Argos** | Perception | Constat visuel objectif (photos, plans) — ne cause pas | — |
| 3 | **Athéna** | Analyse | Structuration des problèmes, scénarios, décisions | — |
| 4 | **Héphaïstos** | Analyse | Faisabilité technique, DTU, matériaux | Technique |
| 5 | **Prométhée** | Analyse | Contre-analyse, biais, adversarial | — |
| 6 | **Apollon** | Analyse | Recherche web+RAG, vérification normative, cohérence finale | — |
| 7 | **Dionysos** | Analyse | Pensée latérale, rupture créative | — |
| 8 | **Thémis** | Cadrage | Réglementation, contrat MOE, déontologie | Contractuel |
| 9 | **Chronos** | Cadrage | Délais légaux, planning, impacts cascade | — |
| 10 | **Arès** | Cadrage | Action terrain rapide, décisions réversibles C3 | — |
| 11 | **Hestia** | Continuité | Mémoire projet (décisions, dettes D0-D3) | — |
| 12 | **Mnémosyne** | Continuité | Mémoire agence (patterns, leçons cross-projets) | — |
| 13 | **Iris** | Communication | Emails humains, courriers, relances | — |
| 14 | **Aphrodite** | Communication | Marketing, réseaux sociaux, storytelling | — |
| 15 | **Dédale** | Production | Dossiers complets (PC, DCE, DOE, marchés) | — |

---

## Flux types

### Flux C1-C2 — Simple (sans Zeus)

```
Humain
  → Hermès (qualifie C1/C2, identifie 1-2 agents)
    → Agent(s) cible(s)
      → Réponse directe
```

Exemples : question normative (Apollon), vérification calendrier (Chronos), info projet (Hestia).

---

### Flux C3-C5 — Orchestration Zeus

```
Humain
  → Hermès (qualifie C3/C4/C5, reformule par agent)
    → Zeus : plan_agents
      → [HITL humain si C4/C5]
        → execute_agents (parallèle ou séquentiel)
          → veto_check (Thémis / Héphaïstos)
            → [HITL + interruption si veto C4/C5]
              → Zeus : judge
                → synthesize
                  → Réponse finale
```

---

### Flux veto

```
Thémis ou Héphaïstos émet {"veto": true, "motif": "...", "condition_levee": "..."}
  → veto_check détecte le veto
    → Si C4/C5 : interrupt() → validation humaine obligatoire
    → Si C3 : Zeus juge si on continue ou bloque
```

---

### Flux mémoire

```
Post-orchestration :
  Hestia ← décisions structurées (scope='projet', affaire_id=<uuid>)
  Mnémosyne ← leçons généralisables (scope='agence', affaire_id=NULL)

Pré-run :
  Toute session → système injecte mémoire Hestia (projet) + Mnémosyne (agence) dans le prompt
```

---

## Communications agent-à-agent

### Qui appelle qui et pourquoi

| De → Vers | Quand | Ce qui transite |
|-----------|-------|-----------------|
| **Hermès → Zeus** | Demande C3-C5 | Qualification + agents suggérés + criticité |
| **Hermès → Agent direct** | Demande C1-C2 | Question reformulée avec contexte projet |
| **Zeus → Agents** | Distribution | Instructions spécifiques par agent, rôle attendu |
| **Zeus → Humain** | HITL C4/C5 | Plan d'agents + motif de validation demandée |
| **Argos → Héphaïstos** | Photo / plan soumis | Constat objectif brut → interprétation technique |
| **Athéna → Prométhée** | Scénario structuré | Hypothèses → contre-analyse adversariale |
| **Athéna → Thémis** | Décision engageante | Scénario → vérification contractuelle/réglementaire |
| **Héphaïstos → Thémis** | Question DTU/AT | Faisabilité technique → validation réglementaire |
| **Apollon → tous** | Sur demande | Références normatives, extraits de documents RAG |
| **Dionysos → Athéna** | Option créative validée | Option latérale → structuration en scénario |
| **Chronos → Arès** | Décision terrain | Contrainte calendaire → action C3 |
| **Chronos → Thémis** | Délai légal dépassé | Alerte BLOQUANT → veto contractuel possible |
| **Hestia → tous** | Chaque session | Mémoire projet injectée en contexte système |
| **Mnémosyne → Zeus** | Orchestration | Patterns agence injectés dans le plan Zeus |
| **Zeus → Iris** | Synthèse validée | Décision → rédaction email/courrier |
| **Zeus → Dédale** | Synthèse validée | Décision → production dossier complet |
| **Apollon → Zeus** | Phase cohérence | Vérification croisée contradictions entre agents |

---

## Articulations clés

### Argos → Héphaïstos : perception → analyse

Argos ne cause jamais. Il décrit ce qu'il voit avec certitude géométrique.
Héphaïstos prend ce constat et l'interprète techniquement (DTU, pathologies, matériaux).
Sans Argos, Héphaïstos peut analyser sur description textuelle mais perd en précision visuelle.

### Athéna → Prométhée : construction → déconstruction

Athéna structure le problème et propose des scénarios.
Prométhée les attaque : hypothèses cachées, biais de confirmation, angles morts.
Le couple Athéna/Prométhée produit une analyse robuste double face.

### Thémis + Héphaïstos : les deux vetos

Thémis vérifie la légalité et la responsabilité contractuelle du MOE.
Héphaïstos vérifie la faisabilité technique (DTU, AT, compatibilité matériaux).
Leurs vetos sont indépendants. Les deux peuvent coexister sur une même décision C5.

### Chronos → Arès : calendrier → action

Chronos identifie les contraintes temporelles et les alertes BLOQUANT/URGENT.
Arès traduit ces contraintes en actions terrain réversibles (C3) sans attendre Zeus.
Pour les décisions engageantes, Arès remonte à Zeus.

### Hestia + Mnémosyne : les deux mémoires persistantes

Hestia = mémoire par affaire (décisions, hypothèses, dettes D1-D3 de ce projet).
Mnémosyne = mémoire transversale (patterns agence, précédents cross-projets).
Zeus consulte les deux avant de planifier une orchestration complexe.

### Apollon : vérificateur transversal

Mode 1 (recherche) : il cherche et sourcifie sur demande d'un autre agent.
Mode 2 (cohérence) : il est appelé en fin d'orchestration par Zeus pour détecter les contradictions entre agents avant la synthèse finale.

---

## Criticité C1-C5 — référence commune

| Niveau | Nature | Zeus | HITL | Veto |
|--------|---------|------|------|------|
| C1 | Information pure | ✗ | ✗ | ✗ |
| C2 | Question | ✗ | ✗ | ✗ |
| C3 | Décision réversible | optionnel | ✗ | ✗ |
| C4 | Décision engageante | ✓ | ✓ | ✗ |
| C5 | Risque majeur | ✓ | ✓ | ✓ |

---

## Règles communes à tous les agents

- Ne jamais inventer un chiffre (coût, délai, surface, article, norme) → `[NON VÉRIFIÉ]`
- Si l'information est absente des documents → le dire explicitement
- Veto émis → stopper, formuler `{"veto": true, "motif": "...", "condition_levee": "..."}`
- Décision engageante sans Thémis → escalader, ne pas décider seul
- Leçon utile en fin de session → la signaler pour Hestia (projet) ou Mnémosyne (agence)

---

## Contexte métier injecté automatiquement

À chaque run, le système injecte dans le prompt système :
- Typology, région, budget, honoraires, phase courante, ABF, zones de risque (depuis `affaires`)
- Mémoire projet Hestia (décisions, dettes D1-D3)
- Mémoire agence Mnémosyne (patterns pertinents)

Phases loi MOP : **ESQ → APS → APD → PRO → ACT → VISA → DET → AOR**

Interlocuteurs : MOA (particuliers, collectivités, promoteurs), entreprises, BET, BC, ABF, DREAL, mairie.
