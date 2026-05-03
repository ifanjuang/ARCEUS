# Templates — architecture_fr

> Source of truth: `domains/architecture_fr/rules.md`,
> `domains/architecture_fr/knowledge_policy.md`,
> `domains/architecture_fr/output_formats.md`,
> `docs/governance/EVIDENCE_PACK.md`,
> `docs/governance/APPROVALS.md`,
> `docs/governance/TASK_CONTRACTS.md`.

Status: **Documented / not runtime**.

---

## 1. Purpose

This folder hosts **neutral, fictional Markdown templates** that
materialize the formats listed in
`domains/architecture_fr/output_formats.md`.

A template is a **shape**, not a finished output. A workflow or a skill
fills the shape; THEMIS / APOLLO and the user review the result.

```text
OpenWebUI expose.
Hermes Agent exécute.
Pantheon Next gouverne.
```

---

## 2. Hard rules

### 2.1 No real data

A template **must not** contain real client, project, address,
construction site, person, budget or contract reference data.

Examples must be fictional, neutral and non-traceable. Convention:

```text
Allowed placeholders:
  P-001                         (fictional project id)
  CLIENT-DEMO                   (role label, not a name)
  LOT-XX                        (CCTP lot reference)
  Lot 07 — VMC                  (anonymized lot label)
  "Affaire fictive de démonstration"
  "Adresse anonymisée"
  YYYY-MM-DD                    (placeholder date)
  €X XXX,XX                     (placeholder amount)

Forbidden:
  real names, real addresses, real RCS / SIRET, real building references,
  real phone, real email, real budget figures, real chantier identifiers.
```

### 2.2 No autonomous-runtime artifact

A template **must not** include code, scripts, agents, runtime
configuration, schedulers, providers or executable plugins. Templates are
Markdown only.

If a template needs structured fields (front-matter, YAML block), it
remains declarative and reviewable.

### 2.3 No final legal or regulatory conclusion

A template **must not** present a legal opinion or a regulatory validation
as canonical. It can host a section that flags risk and quotes a source
(see `knowledge_policy.md` §6.bis), but the conclusion remains the user's
to draw.

### 2.4 No external send

A template never embeds a sending action. It is a draft surface; the user
controls signature and channel.

---

## 3. Naming convention

```text
domains/architecture_fr/templates/<format>__<short_label>.md
```

Where `<format>` matches one of the canonical formats from
`output_formats.md`:

```text
note
lettre
email
rapport
resume
cctp_review
dpgf_review
client_message_draft
quote_vs_cctp_analysis
evidence_summary
```

Identifiers are ASCII to keep filesystem and validator behavior
predictable. The human-readable label remains French ("résumé") in prose
and section headings; the canonical identifier used in filenames, tables
and code-formatted references is `resume`.

Examples (fictional):

```text
note__internal_briefing.md
lettre__moa_demande_complement.md
email__bct_demande_visite.md
rapport__opr_lot_07.md
resume__cctp_lot_07.md
cctp_review__lot_07_vmc.md
dpgf_review__lot_07_vmc.md
client_message_draft__avenant_explication.md
quote_vs_cctp_analysis__lot_07_devis_a.md
evidence_summary__quote_vs_cctp_lot_07.md
```

A template that does not match a canonical format must propose a new
entry in `output_formats.md` first.

---

## 4. Template skeleton

Every Markdown template should follow this skeleton:

```markdown
# <Format> — <short fictional label>

> Status: template / fictional example.
> Source of truth: domains/architecture_fr/output_formats.md (<format>).

## 1. Frame
- format: <format>
- default_approval_level: <C0..C5>
- status: draft | candidate | for_review | for_user_approval
- audience: internal | third_party
- evidence_pack_required: yes | no | recommended

## 2. References (fictional)
- project_id: P-001
- lot: LOT-XX — <fictional label>
- documents:
  - <document_type>: <fictional reference>
- regulatory_references_used (when relevant):
  - family: <RE2020 | DTU | Eurocode | NF C 15-100 | CCAG | code civil | ...>
  - source_id: <fictional reference>
  - status: current | superseded | unknown

## 3. Body
<sections required by output_formats.md for this format>

## 4. Limits
- <what was not checked>
- <what is inferred vs what is sourced>
- <fallbacks attempted, if any>

## 5. Evidence Pack pointer
- evidence_pack_id: <placeholder>
- next_safe_action: <one sentence>
```

The skeleton above is **illustrative**. Each format-specific template
must include the mandatory sections listed in `output_formats.md` for
that format.

---

## 5. Lifecycle of a template

```text
candidate (this folder, marked status: template / fictional example)
  → reviewed (THEMIS / APOLLO)
  → active template (still here, fictional only)
  → superseded (kept until removal review) or archived
```

A template is never `final`. Outputs derived from a template are what
get reviewed, not the template itself.

Adding a new template requires:

1. naming it per §3;
2. ensuring it follows the skeleton in §4;
3. confirming no real data appears (§2.1);
4. confirming the matching format exists in `output_formats.md`;
5. an `ai_logs/YYYY-MM-DD-<slug>.md` entry covering the addition.

---

## 6. Current contents

Status: empty (besides this `README.md`).

The first templates to add, in order of priority, mirror the most likely
day-one workflows:

```text
quote_vs_cctp_analysis__lot_xx_devis_x.md   (review mode, C1)
cctp_review__lot_xx.md                      (review mode, C1)
client_message_draft__contexte_neutre.md    (C4)
evidence_summary__example.md                (C0/C1)
```

These additions should land in separate, scoped PRs — one PR per
template — to keep review small.

---

## 7. Forbidden behavior

```text
real client / project / address / chantier / personal data
auto-send action embedded in the template
final legal opinion presented as canonical
regulatory validation without a current cited source
hidden chain-of-thought as deliverable
templates that reactivate an autonomous runtime path
templates that bypass APPROVALS.md or EVIDENCE_PACK.md
duplication of an existing format under a new name
```

---

## 8. Final rule

```text
Templates are shapes.
Outputs are reviewed.
Evidence is the trace.
The user remains the legal author of any external output.
```
