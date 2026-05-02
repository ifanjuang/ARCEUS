# architecture_fr domain — context for Hermes

> Compact orientation. Source of truth: `docs/governance/MODULES.md`,
> `docs/governance/ARCHITECTURE.md`,
> `docs/governance/APPROVALS.md`,
> `docs/governance/EVIDENCE_PACK.md`,
> `docs/governance/KNOWLEDGE_TAXONOMY.md`,
> domain folder `domains/architecture_fr/`.

Status: **Documented / not runtime**.

---

## 1. Domain scope

`architecture_fr` is the French-speaking architecture / MOE business
domain.

It carries domain-specific governance and capabilities for:

```text
CCTP
DPGF
CCAP
devis (quotes)
notices architecturales
permis (PC / DP / CU)
ERP / SDIS
PLU
ABF
RE2020
marchés privés
marchés publics
chantier (site)
situations / avenants
réserves
DOE
réception
```

The domain folder is `domains/architecture_fr/`. It must not be recreated
under `domains/architecture/`.

---

## 2. Privacy by default

No real client, project, address, person, building name or construction
site may be written into the repository.

Examples, tests and templates must remain **fictional, neutral and
non-traceable**.

```text
Allowed: "fictional renovation case A", "sample CCTP excerpt", "demo project P-001".
Forbidden: real names, real addresses, real building references, real client identifiers, real budget data tied to a real engagement.
```

Memory candidates touching real engagements must check anonymization
before promotion.

---

## 3. Contractual posture

Any output that may become or feed a contractual, financial or
responsibility-bearing artifact is **at least C4**.

Examples that trigger C4 by default:

- a draft response to a client about a contractual position;
- a quote / CCTP comparison conclusion presented as final;
- a redaction of a clause meant for a marché;
- a revised notice meant for an external authority;
- any output addressed to a third party.

C4 requires explicit user approval. Hermes must not send, publish or
transmit on behalf of the user. Hermes drafts; the user approves; the
sending channel remains under human control.

Reference: `docs/governance/APPROVALS.md` §2,
`docs/governance/TASK_CONTRACTS.md` §7.3 (`client_message_review`).

---

## 4. Regulatory and normative sources

For any output that depends on a regulatory or normative source (PLU,
RE2020, ERP / SDIS, accessibility, urbanism, codes, public procurement
rules, French construction law), Hermes must:

- name the source;
- record its tier (T0-T5) and reliability (R0-R5) when known;
- check whether the source is **current** or possibly superseded;
- mark inferences as inferences, not as proven facts;
- block escalation if the source is stale and the action is consequential.

Reference: `docs/governance/KNOWLEDGE_TAXONOMY.md` §4-§8.

If freshness is unknown:

```text
Mark the conclusion as "based on possibly outdated source".
Stop short of contractual recommendation without re-check.
```

---

## 5. Allowed Hermes actions in this domain

Under task contract and within approval scope, Hermes may:

- read CCTP / DPGF / CCAP / devis / notices content from authorized sources;
- compare a quote against a CCTP (`quote_vs_cctp_review`, C1 by default);
- draft client-facing wording for review (`client_message_review`, C4);
- prepare candidate sanity checks (responsibility, scope, missing items);
- propose memory candidates for **system** memory only when the rule is
  reusable and validated against a non-private case.

---

## 6. Forbidden Hermes actions in this domain

Hermes must not, in this domain:

- send anything to a client, an authority, an architect, an engineer or a
  contractor;
- publish anything externally;
- canonize a clause as Pantheon truth;
- promote a project fact to system memory without explicit review;
- mix two real projects without explicit comparison authorization;
- treat an OpenWebUI Knowledge collection labelled with a real project as
  general knowledge;
- redact a contractual clause as final;
- replace a regulatory source with a model statement.

---

## 7. Skills posture

The first business-domain skill / workflow target is:

```text
quote_vs_cctp_review
```

It must remain a **review** mode skill (C1), with `memory_impact:
candidate_only`, agents `[ZEUS, ARGOS, HEPHAESTUS, DEMETER, THEMIS, APOLLO]`
and `evidence_required: true`.

Hermes must not bypass this contract by inventing a parallel "quick"
version that drops THEMIS or APOLLO. Reference:
`docs/governance/TASK_CONTRACTS.md` §7.2.

---

## 8. Knowledge collections

Initial planned collections under OpenWebUI Knowledge for this domain:

```text
architecture_fr_cctp_models
architecture_fr_dpgf_models
architecture_fr_contract_clauses
architecture_fr_notices
architecture_fr_sdis_erp
```

Project-specific collections must follow:

```text
project_{project_id}_{safe_label}
```

with no real client name. Cross-project use is restricted; see
`docs/governance/KNOWLEDGE_TAXONOMY.md` §6.

---

## 9. Final rule

```text
This domain is contractual.
A draft is a draft.
A regulatory check is mandatory for consequential outputs.
A model statement is not evidence.
The user remains the legal author of any external output.
```
