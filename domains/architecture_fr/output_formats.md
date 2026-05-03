# Output formats — architecture_fr

> Source of truth: `docs/governance/EVIDENCE_PACK.md`,
> `docs/governance/APPROVALS.md`,
> `docs/governance/TASK_CONTRACTS.md`,
> `docs/governance/OPENWEBUI_DOMAIN_MAPPING.md`,
> `domains/architecture_fr/rules.md`,
> `domains/architecture_fr/knowledge_policy.md`.

Status: **Documented / not runtime**.

This file enumerates the canonical output formats this domain may
produce, with default approval level, mandatory sections, default
Evidence Pack expectations and a list of forbidden patterns.

A format is a **frame**, not a prompt. A workflow or skill chooses the
format; the user (or THEMIS / APOLLO) accepts or refuses.

```text
OpenWebUI expose.
Hermes Agent exécute.
Pantheon Next gouverne.
```

---

## 1. Default discipline

Every output in this domain must:

- declare its **format** (one of those listed below);
- declare its **approval level** (C0–C5);
- declare its **status** (`draft`, `candidate`, `for_review`, `for_user_approval`);
- carry an **Evidence Pack** when consequential (see
  `docs/governance/EVIDENCE_PACK.md`);
- separate **fact**, **inference**, **assumption** and **draft wording**;
- never present a model statement as evidence;
- never present a regulatory citation without source, tier and freshness
  status (see `domains/architecture_fr/knowledge_policy.md` §6.bis.3).

Forbidden across all formats:

```text
real client / project / address / chantier / personal data
auto-send to a third party
contractual or legal final conclusion presented as canonical
regulatory validation without a current cited source
mixing project documents across projects without explicit trace
hidden chain-of-thought as deliverable
```

---

## 2. Format catalogue

### 2.1 `note`

Short internal note for the user.

| Field | Value |
|---|---|
| Default approval | C1 |
| Status | `draft` or `candidate` |
| Evidence Pack | recommended; mandatory if cites a source |
| Audience | internal / user only |

Mandatory sections:

```text
objet
contexte
constat
recommandation interne (drafted only)
limites
prochaine action sûre
```

### 2.2 `lettre`

Letter intended for an external recipient (client, MOA, MOA assistance,
BCT, BC, BET, ABF, instructeur, autorité, contrôleur technique, MAF,
assurance, expert, avocat, entreprise).

| Field | Value |
|---|---|
| Default approval | **C4** (external send / responsibility) |
| Status | `for_user_approval` only — never `final` from Pantheon Next |
| Evidence Pack | mandatory |
| Audience | third party |

Mandatory sections:

```text
en-tête (anonymisé en repo)
objet
références (numéro affaire, lot, document, date)
corps (rédaction proposée)
limites de la rédaction
prochaine action sûre (envoi par l'utilisateur, canal au choix de l'utilisateur)
```

Hermes drafts. The user signs and sends. Pantheon Next does not auto-send.

### 2.3 `email`

Same posture as `lettre` but in email form.

| Field | Value |
|---|---|
| Default approval | **C4** |
| Status | `for_user_approval` |
| Evidence Pack | mandatory |
| Audience | third party |

Mandatory sections:

```text
sujet
destinataires (rôle uniquement, pas de PII en repo)
corps (rédaction proposée)
pièces jointes proposées (références internes)
limites de la rédaction
prochaine action sûre
```

If the email touches a contractual or contentious matter, it is **C4
minimum** and may require IRIS drafting + THEMIS risk check + APOLLO
final review before user approval. Reference:
`docs/governance/TASK_CONTRACTS.md` §7.3.

### 2.4 `rapport`

Structured technical or contractual report.

| Field | Value |
|---|---|
| Default approval | C3 (internal); C4 if shared externally |
| Status | `candidate` or `for_review` |
| Evidence Pack | mandatory |
| Audience | internal review, then optionally external |

Mandatory sections:

```text
résumé exécutif
périmètre
méthode
constatations (faits + sources)
analyse (inférences, marquées comme telles)
risques et limites
recommandations (drafted only)
annexes (extraits de sources)
prochaine action sûre
```

### 2.5 `résumé`

Short summary of a longer document, exchange or workflow run.

| Field | Value |
|---|---|
| Default approval | C0 / C1 |
| Status | `draft` or `candidate` |
| Evidence Pack | recommended |
| Audience | internal |

Mandatory sections:

```text
source résumée (référence interne)
points clés
limites du résumé
prochaine action sûre
```

A `résumé` must not present an interpretation as a fact. If the source
is private, the summary stays project-scoped.

### 2.6 `cctp_review`

Structured review of a CCTP excerpt or full CCTP.

| Field | Value |
|---|---|
| Default approval | C1 (review mode); C3+ if drives a file mutation |
| Status | `candidate` |
| Evidence Pack | mandatory |
| Audience | internal review |

Mandatory sections:

```text
références CCTP (lot, version, date, statut)
synthèse du périmètre
points clairs
ambiguïtés
manques
risques techniques (HEPHAESTUS)
risques contractuels / responsabilité (THEMIS)
risques quantitatifs (DEMETER)
contradictions internes / avec d'autres pièces (PROMETHEUS)
recommandations de modification (drafted only)
limites
prochaine action sûre
```

### 2.7 `dpgf_review`

Structured review of a DPGF or DQE.

| Field | Value |
|---|---|
| Default approval | C1 |
| Status | `candidate` |
| Evidence Pack | mandatory |
| Audience | internal review |

Mandatory sections:

```text
références DPGF (lot, version, date, statut)
unités et quantités vérifiées
prix unitaires manquants ou anormaux
postes manquants
postes redondants
incohérences avec CCTP
limites de l'analyse
prochaine action sûre
```

### 2.8 `client_message_draft`

Drafted message intended for a client. Always presented as a **draft for
user approval**, never as final.

| Field | Value |
|---|---|
| Default approval | **C4** |
| Status | `for_user_approval` |
| Evidence Pack | mandatory |
| Audience | client (after user approval) |

Mandatory sections:

```text
intention détectée
contexte projet (références internes uniquement)
rédaction proposée
ton et niveau de formalité
points sensibles (THEMIS)
risques de responsabilité
limites
prochaine action sûre (relecture utilisateur, signature, envoi)
```

Reference: `docs/governance/TASK_CONTRACTS.md` §7.3
(`client_message_review`).

### 2.9 `quote_vs_cctp_analysis`

Comparison of a contractor quote against a CCTP / DPGF / programme.

| Field | Value |
|---|---|
| Default approval | C1 (review); C4 if drives a contractual position |
| Status | `candidate` |
| Evidence Pack | mandatory |
| Audience | internal review, then optionally architect / MOA |

Mandatory sections:

```text
références (devis, CCTP, DPGF, version, date, statut)
items concordants
items manquants
items divergents
hors-périmètre
risques contractuels / responsabilité (THEMIS)
risques techniques (HEPHAESTUS)
risques de coût / quantité (DEMETER)
hypothèses
limites
prochaine action sûre
```

Reference: `docs/governance/TASK_CONTRACTS.md` §7.2
(`quote_vs_cctp_review`).

### 2.10 `evidence_summary`

User-facing Evidence Pack summary derived from the canonical Evidence
Pack defined in `docs/governance/EVIDENCE_PACK.md`.

| Field | Value |
|---|---|
| Default approval | C0 / C1 (it describes what was done) |
| Status | `for_review` |
| Evidence Pack | itself |
| Audience | internal review, OpenWebUI display |

Mandatory display fields (mirror of OpenWebUI surface):

```text
task_id
task_contract_id
criticality
files_read
sources_used
documents_used
tools_used
knowledge_bases_consulted
assumptions
unsupported_claims
limitations
outputs
approval_required
next_safe_action
```

This format is the canonical surface for THEMIS / APOLLO review and
OpenWebUI approval display. Reference:
`docs/governance/OPENWEBUI_INTEGRATION.md` §6.

---

## 3. Format selection

| Situation | Format |
|---|---|
| User asks for a quick internal opinion | `note` |
| User asks for a draft to send to a client | `client_message_draft` (then `email` or `lettre` after user approval) |
| User asks for a CCTP review | `cctp_review` |
| User asks for a DPGF review | `dpgf_review` |
| User asks for a quote vs CCTP comparison | `quote_vs_cctp_analysis` |
| User asks for a written report | `rapport` |
| User asks for a summary of a long document | `résumé` |
| User asks "what did you do" / "what did you check" | `evidence_summary` |
| User asks for a letter to a third party | `lettre` |
| User asks for an email to a third party | `email` |

When ambiguous, the safer format wins (lower exposure, drafted, candidate
status, more limits stated).

---

## 4. Evidence Pack mapping

| Format | Evidence Pack required | Extra fields specific to this domain |
|---|---|---|
| `note` | recommended | `project_documents_used` if cited |
| `lettre` | yes | `project_documents_used`, `regulatory_references_used`, `regulatory_freshness_check` |
| `email` | yes | same as `lettre` |
| `rapport` | yes | `project_documents_used`, `regulatory_references_used`, `regulatory_freshness_check`, `before_after_metrics` if applicable |
| `résumé` | recommended | `source_status` |
| `cctp_review` | yes | `project_documents_used`, `version_or_filename`, `chunks_or_excerpts_consulted` |
| `dpgf_review` | yes | `project_documents_used`, `version_or_filename`, `chunks_or_excerpts_consulted` |
| `client_message_draft` | yes | `project_documents_used`, `recipient_role` (no PII), `risk_notes` |
| `quote_vs_cctp_analysis` | yes | `project_documents_used`, `version_or_filename`, `risk_flags` |
| `evidence_summary` | itself | — |

Reference: `docs/governance/EVIDENCE_PACK.md` §3,
`domains/architecture_fr/knowledge_policy.md` §7.

---

## 5. Approval mapping

| Format | Default level | Escalation triggers |
|---|---:|---|
| `note` | C1 | turns into a contractual position → C3+ |
| `lettre` | C4 | always external |
| `email` | C4 | always external |
| `rapport` | C3 | shared externally → C4 |
| `résumé` | C0 / C1 | summary used as authoritative → C3 |
| `cctp_review` | C1 | drives a file mutation → C3 |
| `dpgf_review` | C1 | drives a file mutation → C3 |
| `client_message_draft` | C4 | always external once approved |
| `quote_vs_cctp_analysis` | C1 | drives a contractual position → C4 |
| `evidence_summary` | C0 / C1 | — |

Reference: `docs/governance/APPROVALS.md`.

---

## 6. Final rule

```text
The format is a contract.
The status is honest (draft, candidate, for_review, for_user_approval).
The Evidence Pack is the trace.
The user remains the legal author of any external output.
```
