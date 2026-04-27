# MODULES — Pantheon OS

> Ce document définit le découpage fonctionnel réel du système Pantheon OS.  
> Les modules représentent les composants structurants du Domain Operating Layer.

---

# 1. Principe

Pantheon OS n’est pas un runtime.

C’est un système de définition structuré autour de :

- skills  
- workflows  
- agents  
- mémoire  
- knowledge  
- règles  

Chaque module doit être :

- lisible  
- isolé  
- maintenable  
- aligné avec les Markdown  

---

# 2. Modules principaux

## 2.1 Agents

text agents/ 

Rôle :

- définir les fonctions cognitives du système  
- structurer l’analyse  
- organiser les workflows  

Contenu :

- un fichier par agent  
- rôle  
- responsabilités  
- limites  

Important :

Les agents sont abstraits et non métier.

---

## 2.2 Skills

text skills/ 

Rôle :

- représenter les capacités du système  
- porter la logique métier  
- produire des outputs exploitables  

Structure :

text skills/   generic/   architecture/     cctp_audit/       SKILL.md 

Contenu d’une skill :

- objectif  
- inputs  
- outputs  
- règles  
- risques  
- conditions d’activation  

Important :

Toute logique métier doit être dans les skills.

---

## 2.3 Workflows

text workflows/ 

Rôle :

- structurer les enchaînements d’actions  
- orchestrer les agents et les skills  

Structure :

text workflows/   generic/   architecture/     cctp_review.yaml 

Contenu :

- étapes  
- ordre  
- agents mobilisés  
- skills utilisées  
- points de validation  

Important :

Un workflow = une méthode claire.

---

## 2.4 Domains (overlays métier)

text domains/ 

Rôle :

- spécialiser le système par métier  
- injecter contexte, règles et contraintes  

Structure :

text domains/   architecture/     overlay.md     workflows/     skills/ 

Contenu :

- règles métier  
- contraintes réglementaires  
- conventions  

Important :

Le domaine ne modifie pas les agents.  
Il influence uniquement skills et workflows.

---

## 2.5 Memory

text memory/ 

Rôle :

- structurer la connaissance du système  

Structure :

text memory/   session/   candidates/   project/   system/ 

### session

- temporaire  
- non persistée  

### candidates

- persistée  
- non validée  

### project

- spécifique à un projet  
- contexte opérationnel  

### system

- globale  
- validée  
- réutilisable  

Règle :

Aucune promotion sans validation THEMIS.

---

## 2.6 Knowledge

text knowledge/ 

Rôle :

- définir la stratégie documentaire  
- organiser OpenWebUI  

Contenu :

- collections  
- source policy  
- classification  

Important :

La knowledge n’est pas la mémoire.  
Elle alimente les skills.

---

## 2.7 Hermes Integration

text hermes/ 

Rôle :

- connecter Pantheon au runtime Hermes  

Structure :

text hermes/   context/     pantheon_context.md     agents_context.md     rules_context.md 

Contenu :

- règles transmises à Hermes  
- contexte système  
- contraintes  

Important :

Pantheon ne remplace pas Hermes.  
Il le pilote.

---

## 2.8 Operations

text operations/ 

Rôle :

- exploitation du système  
- installation  
- maintenance  

Contenu :

- installation NAS  
- update  
- versioning  
- monitoring  

---

# 3. Modules legacy

Certains éléments existants sont considérés comme legacy :

- runtime FastAPI autonome  
- module registry  
- workflow loader  
- approval API initiale  
- installer UI  

Règle :

- ne pas supprimer sans audit  
- classer  
- réorienter ou archiver  

---

# 4. Règles de conception

Un module doit :

- avoir une responsabilité claire  
- ne pas dépendre implicitement d’un autre  
- être documenté  
- être testable  

---

# 5. Ce qui n’est PAS un module

text ❌ agent métier ❌ runtime complet ❌ interface UI ❌ base de données métier implicite ❌ logique cachée dans le code 

---

# 6. Flux global

text User → OpenWebUI → Pantheon (agents + workflows + skills) → Hermes (exécution) → résultats → mémoire (si validé) 

---

# 7. Résumé

text agents     → raisonnement skills     → métier workflows  → méthode domains    → contexte métier memory     → connaissance validée knowledge  → sources hermes     → exécution operations → exploitation 

---

FIN DU FICHIER