# Rules — architecture_fr

> Source of truth: `docs/governance/MODULES.md`,
> `docs/governance/AGENTS.md`,
> `docs/governance/APPROVALS.md`,
> `docs/governance/EVIDENCE_PACK.md`,
> `docs/governance/TASK_CONTRACTS.md`,
> `docs/governance/KNOWLEDGE_TAXONOMY.md`,
> `docs/governance/OPENWEBUI_DOMAIN_MAPPING.md`,
> `domains/architecture_fr/knowledge_policy.md`,
> `domains/architecture_fr/output_formats.md`.

Status: **Documented / not runtime**.

Operating context:

```text
OpenWebUI expose.
Hermes Agent exécute.
Pantheon Next gouverne.
```

---

## 1. Domain scope

`architecture_fr` is the French-speaking architecture / maîtrise d'œuvre
business domain.

It governs how Pantheon Next handles:

```text
CCTP, DPGF, CCAP, devis
notices architecturales
permis (PC, DP, CU)
ERP / SDIS / accessibilité
PLU, ABF
RE2020, RT2012 (legacy)
Eurocodes (NF EN 199x)
NF C 15-100, autres normes électriques
loi MOP, ordonnance 2018-1074, CCP / CCAG (Travaux, MOE, FCS, PI)
code civil (responsabilité, garanties biennale/décennale)
code de l'urbanisme, code de la construction et de l'habitation
marchés privés (norme NF P 03-001), marchés publics
chantier, situations, avenants, OPR, réserves, levée de réserves, DOE, réception
recommandations et boîte à outils MAF (Mutuelle des Architectes Français)
avis techniques (CSTB), DTA, ATEx
```

This domain does not duplicate `general` or `software`. It is not the
runtime, the orchestrator, or the model provider.

The folder `domains/architecture/` (without `_fr`) **must not** be
recreated.

---

## 2. Abstract agents most often involved

These are reasoning roles, not autonomous workers. Reference:
`docs/governance/AGENTS.md`.

| Role | Typical contribution in this domain |
|---|---|
| ZEUS | Workflow selection, escalation routing |
| ATHENA | Plan, decompose into review steps, identify task contract |
| ARGOS | Extract facts from CCTP / DPGF / quotes / notices, separate facts from assumptions |
| HEPHAESTUS | Technical and constructability review (lots, interfaces, structure, fluides) |
| DEMETER | Quantities, costs, financial coherence |
| THEMIS | Contractual / responsibility / approval / veto |
| PROMETHEUS | Missing scope, contradictions, blind spots |
| APOLLO | Final coherence, completeness, confidence gate |
| HECATE | Uncertainty calls — block when source is missing or stale |
| IRIS | Drafting tone for client / authority / contractor messages — drafts only, does **not** send |
| HESTIA | Project memory custodian (validated project context) |
| MNEMOSYNE | System memory custodian (only after explicit generalization review) |
| HERMES (role) | Frames delegation to the Hermes runtime (see `docs/governance/HERMES_INTEGRATION.md`) |

Agents do not carry business logic. Skills, workflows, knowledge,
templates and task contracts do.

---

## 3. Hard limits

The following limits apply on every task in this domain.

### 3.1 No final legal advice

Pantheon Next does not produce a final legal opinion. It may:

- map a contractual position to references (CCAG, code civil, NF P 03-001);
- flag a clause as risky;
- prepare a draft for review.

It must not present a legal conclusion as canonical. The user, the
architect, the conseil juridique or the avocat remains the legal author.
Outputs of this kind are **C4 minimum**.

### 3.2 No regulatory validation without a current source

A regulatory claim (RE2020, ERP, accessibilité, PLU, urbanisme, normes
NF / EN, code de l'urbanisme, CCAG) is consequential and must:

- name the source;
- record its tier (T0–T5) and reliability (R0–R5) when known;
- check whether the source is current or possibly superseded;
- if freshness is unknown, mark the conclusion as
  `based on possibly outdated source` and stop short of a contractual
  recommendation without re-check;
- block escalation if the source is stale and the action is consequential.

Reference: `docs/governance/KNOWLEDGE_TAXONOMY.md`,
`domains/architecture_fr/knowledge_policy.md` §3 fetch-before-cite,
§3.2 (when added) regulatory references.

### 3.3 No external send without C4

Any output addressed to a third party — client, MOA, BCT, BET, BC,
entreprise, sous-traitant, coordonnateur SPS, ABF, instructeur, avocat,
assurance, MAF, contrôleur technique, expert, autorité — is **C4
minimum** and requires explicit user approval.

Hermes drafts. The user approves. The sending channel remains under
human control. Pantheon Next does not auto-send. Reference:
`docs/governance/APPROVALS.md` §3,
`docs/governance/TASK_CONTRACTS.md` §7.3 (`client_message_review`).

### 3.4 No project data leakage

No real client name, real address, real project reference, real
construction site, real budget tied to a real engagement, real personal
data, may be written into the repository (rules, examples, tests,
templates).

Examples must remain fictional, neutral and non-traceable. Convention:

```text
Allowed: "fictional renovation case A", "demo project P-001",
         "sample CCTP excerpt", "anonymized DPGF block".
Forbidden: real names, real addresses, real building references,
           real client identifiers, real budget data.
```

Cross-project use is restricted; see
`docs/governance/KNOWLEDGE_TAXONOMY.md` §6.

### 3.5 No autonomous runtime path

This domain does not implement an execution engine, an agent runtime, a
tool runtime, a provider router, a scheduler, a central orchestrator, a
memory auto-promotion job, or a self-evolution auto-merge.

If a task seems to require one of those, raise it through the standard
governance flow, not by adding code here.

---

## 4. Operating defaults

### 4.1 Default approval level

| Action | Default level | Comment |
|---|---:|---|
| read CCTP / DPGF / CCAP / devis / notices | C0 | `pdf_info_check`, `pdf_text_layer_check` mode |
| extract facts under task contract | C0 / C1 | depends on whether the output is presented as a fact or a draft |
| draft client wording for review | **C4** | drafted only, not sent — C4 from the start because it enters the client-communication workflow and must inherit THEMIS / APOLLO / IRIS controls; aligns with `TASK_CONTRACTS.md` §7.3 (`client_message_review`) and `output_formats.md` §2.8 (`client_message_draft`) |
| compare quote vs CCTP (`quote_vs_cctp_review`) | C1 | review mode, candidate output |
| produce a contractual position summary | C3+ | persistent internal output; if external, C4 |
| transmit a client message | C4 | explicit user approval; user controls the channel |
| sign off on a contractual / contentious position | not allowed | Pantheon Next does not sign |

Reference: `docs/governance/APPROVALS.md`.

### 4.2 Default Evidence Pack discipline

Every consequential output requires an Evidence Pack with at least the
fields enumerated in `docs/governance/EVIDENCE_PACK.md` §3. For this
domain, Evidence must additionally record:

```text
project_documents_used
source_status (signed / draft / superseded / unknown)
source_date_when_available
version_or_filename
chunks_or_excerpts_consulted
regulatory_references_used
regulatory_freshness_check
limits_specific_to_the_domain
```

Reference: `domains/architecture_fr/knowledge_policy.md` §7.

### 4.3 Project source priority

When project documents conflict with generic templates, the project
source controls unless marked obsolete. Order:

```text
signed / filed / validated project document
latest validated project document
official regulation or standard reference
current project instruction
agency template
external secondary source
model answer
```

Reference: `domains/architecture_fr/knowledge_policy.md` §4.

---

## 5. Skill posture

The first business-domain skill / workflow target is:

```text
quote_vs_cctp_review
```

It must remain a `review` mode skill (C1) with `memory_impact:
candidate_only`, agents `[ZEUS, ARGOS, HEPHAESTUS, DEMETER, THEMIS,
APOLLO]` and `evidence_required: true`. Reference:
`docs/governance/TASK_CONTRACTS.md` §7.2.

Other skill candidates relevant to this domain (status: planned /
candidate only):

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

A new skill starts as `candidate`. No level-up is automatic. No active
skill is modified directly without review (`SKILL_LIFECYCLE.md`).

---

## 6. Workflow posture

Workflows live under `domains/architecture_fr/workflows/*.yaml`.
Existing entries:

```text
recherche_documentaire
decision_strategique
reponse_rapide
```

Rules:

- a workflow is a method, not a long prompt;
- every durable workflow change starts as a **candidate update**;
- risky workflow changes require validation;
- a workflow may not bypass approvals or `quote_vs_cctp_review` framing.

Reference: `docs/governance/MODULES.md` §2.4.

---

## 7. Memory posture

This domain produces:

- `memory/candidates` only by default;
- `memory/project` only after THEMIS / APOLLO review and C3 promotion;
- `memory/system` only after a separate generalization review (rule must
  be reusable cross-project, anonymized, and validated against a
  non-private case).

Forbidden:

- promote a quote into a reusable rule;
- promote a project-specific clause into system memory without review;
- mix two project memory scopes without explicit trace and approval;
- treat OpenWebUI Knowledge or Hermes local memory as Pantheon canonical
  memory.

Reference: `docs/governance/MEMORY.md`,
`domains/architecture_fr/knowledge_policy.md` §8.

---

## 8. OpenWebUI mapping

Reference: `docs/governance/OPENWEBUI_DOMAIN_MAPPING.md` §7.

OpenWebUI may expose, for this domain:

```text
architecture_fr_cctp_models
architecture_fr_dpgf_models
architecture_fr_contract_clauses
architecture_fr_notices
architecture_fr_sdis_erp
architecture_fr_plu_reference
architecture_fr_site_reports
```

Project-specific Knowledge Bases must follow:

```text
project_{project_id}_{safe_label}
```

with no real client name. Workspace Models named after Pantheon roles
(ATHENA, ARGOS, THEMIS, HEPHAESTUS, APOLLO, IRIS) are user-facing
presets only — they do **not** define the role. The role definition
remains in `docs/governance/AGENTS.md`.

---

## 9. Forbidden behavior (summary)

```text
producing a final legal opinion as canonical
producing a regulatory validation without a current cited source
sending or publishing anything to a third party without C4 approval
mixing two real projects without explicit comparison authorization
promoting a project fact to system memory without review
promoting a quote into a reusable rule
treating OpenWebUI Knowledge as Pantheon memory
treating a search snippet as evidence
using obsolete templates without a status warning
introducing real client / address / project / chantier data anywhere in this repository
duplicating an autonomous runtime path inside Pantheon Next
```

---

## 10. Final rule

```text
This domain is contractual.
A draft is a draft.
A regulatory check is mandatory for consequential outputs.
A source trace is mandatory for consequential outputs.
A model statement is not evidence.
The user remains the legal author of any external output.
```
