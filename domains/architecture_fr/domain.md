# Domain — architecture_fr

> Source of truth: `docs/governance/MODULES.md` §2.2,
> `docs/governance/AGENTS.md`,
> `docs/governance/APPROVALS.md`,
> `docs/governance/EVIDENCE_PACK.md`,
> `docs/governance/TASK_CONTRACTS.md`,
> `docs/governance/WORKFLOW_SCHEMA.md`,
> `docs/governance/WORKFLOW_ADAPTATION.md`,
> `docs/governance/KNOWLEDGE_TAXONOMY.md`,
> `docs/governance/OPENWEBUI_DOMAIN_MAPPING.md`.

Status: **Documented / not runtime**.

```text
OpenWebUI expose.
Hermes Agent exécute.
Pantheon Next gouverne.
```

---

## 1. Identity

| Field | Value |
|---|---|
| Domain id | `architecture_fr` |
| Label | Architecture & Maîtrise d'Œuvre (FR) |
| Folder | `domains/architecture_fr/` |
| Manifest | `domains/architecture_fr/manifest.yaml` |
| Language | French |
| Forbidden alias | `domains/architecture/` (without `_fr`) — must not be recreated |
| Privacy | strict — no real client / project / address / chantier / personal data anywhere in this folder |

---

## 2. Scope

`architecture_fr` covers the French-speaking architecture / maîtrise
d'œuvre business domain:

```text
CCTP, DPGF, CCAP, devis
notices architecturales
permis (PC, DP, CU)
ERP / SDIS / accessibilité
PLU, ABF
RE2020, RT2012 (legacy)
Eurocodes (NF EN 199x)
NF C 15-100, autres normes
loi MOP, ordonnance 2018-1074, code de la commande publique, CCAG (Travaux, MOE, FCS, PI, MI)
NF P 03-001, contrats type d'architecte, recommandations MAF
code civil (responsabilité décennale, biennale, parfait achèvement)
code de la construction et de l'habitation
code de l'urbanisme
chantier, situations, avenants, OPR, réserves, levée de réserves, DOE, réception
avis techniques (CSTB), DTA, ATEx
```

For the full reference list and source tiers, see
`domains/architecture_fr/knowledge_policy.md`.

---

## 3. Operating posture

| Topic | Default |
|---|---|
| Approval default | C0 for read; C1 for review/draft; C3+ for persistent internal output; **C4** for any external send or contractual position |
| Evidence Pack | mandatory for any consequential output (review, contractual position, comparison, redaction draft, regulatory citation) |
| Memory impact | `candidate_only` by default; project memory needs C3 + Evidence Pack; system memory needs a separate generalization review |
| External communication | C4 — Pantheon Next does **not** auto-send; user controls signature and channel |
| Regulatory citations | source, tier, freshness check required; if status is unknown or stale, conclusion must mark `based on possibly outdated source` and stop short of contractual recommendation until re-check |
| Real-data hygiene | fictional / neutral examples only (`P-001`, `LOT-XX`, `CLIENT-DEMO`, `Adresse anonymisée`, `YYYY-MM-DD`, `€X XXX,XX`) |

For the full doctrine, see `domains/architecture_fr/rules.md`.

---

## 4. Structure

Canonical structure for this domain (per `docs/governance/MODULES.md` §2.2):

```text
domains/architecture_fr/
  domain.md                  # this file — top-level summary
  rules.md                   # doctrine: scope, agents, hard limits, defaults
  knowledge_policy.md        # source tiers, fetch-before-cite, regulatory references, freshness
  output_formats.md          # canonical output formats and approval mapping
  manifest.yaml              # domain manifest (skills/workflows registry)
  policies/                  # YAML policy fragments (e.g. veto patterns)
  prompts/                   # prompt context fragments
  skills/                    # candidate / active skills
    {skill_id}/
      SKILL.md
      manifest.yaml
      examples.md
      tests.md
      UPDATES.md
  workflows/                 # workflow templates and legacy flows
    {workflow_id}/           # canonical (per WORKFLOW_SCHEMA.md §2)
      workflow.yaml
      tasks.yaml
      examples.md
      tests.md
      UPDATES.md
    *.yaml                   # legacy flat workflows (kept until migrated)
  templates/                 # neutral, fictional Markdown output templates
    README.md
```

The legacy flat workflows (`recherche_documentaire.yaml`,
`decision_strategique.yaml`, `reponse_rapide.yaml`) follow an older
schema. New workflows must follow `WORKFLOW_SCHEMA.md` §2 (folder per
workflow). Migration of the legacy flows is out of scope here.

---

## 5. Abstract agents typically involved

These are reasoning roles, not autonomous workers. Reference:
`docs/governance/AGENTS.md`.

| Role | Typical contribution |
|---|---|
| ZEUS | workflow selection, escalation routing, arbitration |
| ATHENA | plan, decompose, identify task contract, arrange workflow steps |
| ARGOS | extract facts from CCTP / DPGF / quotes / notices |
| HEPHAESTUS | technical / structural / constructability review |
| DEMETER | quantities, costs, financial coherence |
| THEMIS | contractual / responsibility / approval / veto |
| PROMETHEUS | missing scope, contradictions, alternatives |
| APOLLO | final coherence, completeness, evidence gate |
| HECATE | uncertainty calls — block when source is missing or stale |
| CHRONOS | sequencing, deadlines, dependencies between steps |
| IRIS | drafting tone for client / authority / contractor messages — drafts only |
| HESTIA | project memory custodian (validated project context) |
| MNEMOSYNE | system memory custodian (only after explicit generalization review) |
| HERMES (role) | frames delegation to the Hermes runtime |

> Spelling note. `docs/governance/WORKFLOW_ADAPTATION.md` uses the
> French/Greek form **HEPHAISTOS**; `docs/governance/AGENTS.md` (the
> source of truth for role names) uses **HEPHAESTUS**. This domain
> aligns on the canonical `AGENTS.md` form. The variant is acknowledged
> here for traceability and is left for governance to reconcile in a
> dedicated PR.

---

## 6. Skills

Active skills inherited from the legacy domain (status as declared in
their manifests):

```text
domains/architecture_fr/skills/chantier/
domains/architecture_fr/skills/communications/
domains/architecture_fr/skills/decisions/
domains/architecture_fr/skills/finance/
domains/architecture_fr/skills/planning/
domains/architecture_fr/skills/webhooks/
```

First skill aligned with the post-pivot governance:

```text
domains/architecture_fr/skills/quote_vs_cctp_consistency/   # candidate
```

Other planned candidates (not created yet):

```text
cctp_review
dpgf_review
notice_architecturale_check
client_message_safety
chantier_situation_review
delai_penalite_analysis
plu_constraint_check
erp_sdis_check
re2020_compliance_summary
```

A new skill always starts as `candidate`. No level-up is automatic. No
active skill is modified directly without review (`SKILL_LIFECYCLE.md`).

---

## 7. Workflows

Legacy flat workflows kept for now (older schema):

```text
domains/architecture_fr/workflows/recherche_documentaire.yaml
domains/architecture_fr/workflows/decision_strategique.yaml
domains/architecture_fr/workflows/reponse_rapide.yaml
```

First workflow aligned with `WORKFLOW_SCHEMA.md` §2 + adaptive doctrine
of `WORKFLOW_ADAPTATION.md`:

```text
domains/architecture_fr/workflows/quote_vs_cctp_review/    # candidate template
```

Workflows are governed trajectories that may be selected, adapted,
composed, generated in-session or reset to a baseline template
(`WORKFLOW_ADAPTATION.md` §1). Adaptation never bypasses approvals,
THEMIS veto, APOLLO gate or the external-tools policy
(`WORKFLOW_ADAPTATION.md` §2).

---

## 8. Knowledge

Initial OpenWebUI Knowledge Bases for this domain (per
`OPENWEBUI_DOMAIN_MAPPING.md` §7):

```text
architecture_fr_cctp_models
architecture_fr_dpgf_models
architecture_fr_contract_clauses
architecture_fr_notices
architecture_fr_sdis_erp
architecture_fr_plu_reference
architecture_fr_site_reports
```

Project-specific Knowledge Bases must follow
`project_{project_id}_{safe_label}` with no real client name.

```text
Knowledge ≠ Memory.
A document is a source. A validated reusable fact is a memory candidate.
Pantheon alone canonizes memory.
```

---

## 9. Memory

```text
session     temporary, never the source of truth
candidates  persisted but not validated — default for this domain
project     validated project context (HESTIA, after C3 + Evidence Pack)
system      validated reusable rules / patterns (MNEMOSYNE, separate review)
```

Forbidden:

- promote a quote into a reusable rule;
- promote a project-specific clause into system memory without review;
- mix two project memory scopes without explicit trace and approval;
- treat OpenWebUI Knowledge or Hermes local memory as Pantheon memory.

---

## 10. Output formats

This domain produces outputs in one of the canonical formats defined in
`domains/architecture_fr/output_formats.md`:

```text
note
lettre
email
rapport
resume          # ASCII identifier; label "résumé" used in prose
cctp_review
dpgf_review
client_message_draft
quote_vs_cctp_analysis
evidence_summary
```

Each format declares default approval level, mandatory sections and
Evidence Pack expectations. Templates live under
`domains/architecture_fr/templates/`.

---

## 11. Forbidden patterns (summary)

```text
final legal opinion presented as canonical
regulatory validation without a current cited source
external send without C4 approval
mixing two real projects without explicit comparison authorization
promoting a project fact to system memory without review
treating OpenWebUI Knowledge as Pantheon memory
treating a search snippet as evidence
using obsolete templates without status warning
introducing real client / project / address / chantier / personal data
duplicating an autonomous runtime path inside Pantheon Next
recreating domains/architecture/ (without _fr)
```

---

## 12. Final rule

```text
This domain is contractual.
A draft is a draft.
A regulatory check is mandatory for consequential outputs.
A source trace is mandatory for consequential outputs.
A model statement is not evidence.
The user remains the legal author of any external output.
```
