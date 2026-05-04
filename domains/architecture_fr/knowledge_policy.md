# Knowledge Policy — architecture_fr

> Domain policy for French architecture / maîtrise d'œuvre Knowledge use.
> Documents remain Knowledge. Validated reusable facts may become memory candidates only after review.

---

## 1. Principle

```text
Knowledge supports analysis.
Memory canonizes validated context.
Evidence proves consequential claims.
```

OpenWebUI Knowledge, uploaded documents and RAG results are not Pantheon memory.

---

## 2. Trusted source tiers

### Tier 1 — official / primary

```text
legifrance.gouv.fr
service-public.fr
boamp.fr
construction.gouv.fr
cohesion-territoires.gouv.fr
```

### Tier 2 — professional / technical reference

```text
cstb.fr (avis techniques, DTA, ATEx)
afnor.org (NF, NF EN, NF DTU)
oppbtp.fr (prévention chantier)
qualibat.fr (qualifications entreprises)
maf.fr (Mutuelle des Architectes Français — recommandations, boîte à outils, fiches sinistres)
ordre-des-architectes.fr (déontologie, missions, modèles)
```

### Tier 3 — project-controlled sources

```text
signed contracts
CCTP
CCAP
DPGF
plans
notices
RFCT
commission feedback
validated client instructions
site reports
```

### Tier 4 — secondary / contextual

```text
supplier documentation
manufacturer datasheets
company quotes
press or blog articles
non-official summaries
```

Tier 4 may inform analysis but must not override project-controlled or official sources.

---

## 3. Fetch-before-cite rule

Search result snippets are not evidence.

A source may support a consequential claim only if the content has been opened, read or extracted, and recorded in the Evidence Pack.

```text
Search result = lead.
Read source = possible evidence.
Evidence Pack = trace.
```

---

## 4. Project source priority

When project documents conflict with generic templates, the project source controls unless marked obsolete.

Priority order:

```text
signed / filed / validated project document
latest validated project document
official regulation or standard reference
current project instruction
agency template
external secondary source
model answer
```

---

## 5. RAG discipline

RAG must be scoped.

Allowed filters:

```text
project_id
source_type
lot
phase
document_status
source_tier
freshness
```

Default rule:

```text
Do not mix project Knowledge Bases without explicit trace and approval when the output is consequential.
```

---

## 6. Architecture document types

Common source types:

```text
cctp
ccap
dpgf
quote
plan
notice
permit
site_report
technical_report
email
commission_feedback
standard_reference
```

CCTP, DTU and standards benefit from contextual chunking when available.

---

## 6.bis Regulatory and normative reference families

Pantheon Next must **name the family** when an output cites or relies on
one of these references. Each citation must be backed by a fetched and
read source recorded in the Evidence Pack (see §3 fetch-before-cite).

### 6.bis.1 Construction and architecture references

```text
RE2020 (réglementation environnementale 2020) — bâtiments neufs
RT2012 — legacy, peut encore s'appliquer à certains projets
DTU (NF DTU) — règles de l'art exécution travaux
Eurocodes (NF EN 1990 à NF EN 1999) — calcul des structures
NF C 15-100 — installations électriques basse tension
règles ERP / IGH (code de la construction et de l'habitation)
règles SDIS — sécurité incendie locale
règles d'accessibilité (PMR, ERP, logements)
PLU / PLUi / RNU — règles d'urbanisme locales et nationales
ABF — périmètre monuments historiques
recommandations CSTB — avis techniques, DTA, ATEx
```

### 6.bis.2 Contractual and procurement references

```text
loi MOP (loi 85-704 modifiée) — maîtrise d'ouvrage publique
ordonnance 2018-1074, décret 2018-1075 — code de la commande publique
CCAG Travaux, MOE, FCS, PI, MI — clauses administratives générales
NF P 03-001 — marchés privés de travaux
contrat type d'architecte (Ordre, MAF) — missions et honoraires
code civil — responsabilité décennale, biennale, parfait achèvement
code de la construction et de l'habitation
code de l'urbanisme
recommandations MAF — boîte à outils, fiches contrats, fiches sinistres
```

### 6.bis.3 Reliability and freshness rule

A regulatory or normative reference is **time-sensitive**. For each
citation, record:

```yaml
freshness:
  source_family: "RE2020 | DTU | Eurocode | NF C 15-100 | CCAG | code civil | …"
  source_id: ""              # e.g. "NF EN 1992-1-1:2005+A1:2014"
  source_url_or_path: ""
  last_checked: null
  check_required_after: null
  status: "current | superseded | unknown"
```

If `status` is `unknown` or the source is older than the configured
freshness window, the conclusion **must** be marked
`based on possibly outdated source` and any contractual recommendation
**must stop** until re-check.

Reference: `docs/governance/KNOWLEDGE_TAXONOMY.md` §4–§8,
`domains/architecture_fr/rules.md` §3.2.

---

## 7. Evidence Pack requirements

For consequential architecture outputs, record:

```text
project documents used
source status
source date when available
version or filename
chunks or excerpts consulted
unsupported claims
assumptions
limits
approval required
```

Consequential outputs include:

```text
contractual position
technical compliance claim
financial recommendation
delay or penalty analysis
external message
memory promotion
file mutation
```

---

## 8. Memory boundary

A project document can produce a memory candidate only when the extracted fact is useful, scoped and traceable.

Example:

```text
Document: CCTP Lot 07
Candidate: The project requires a separate AirBnB shower VMC.
Scope: project
Evidence: filename + section + extracted quote or paraphrase
```

System memory requires a separate generalization review.

---

## 9. Forbidden behavior

```text
using a search snippet as evidence
mixing projects silently
promoting a quote into a reusable rule
promoting a project-specific fact into system memory without review
using obsolete templates without status warning
turning OpenWebUI Knowledge into Pantheon memory
```

---

## 10. Final rule

```text
In architecture_fr, sources must be scoped, dated when possible, and traceable.
No source trace, no consequential claim.
```
