# Quote vs CCTP Review — Workflow examples

> Fictional examples only. No real client / project / address / chantier / personal / budget data.
>
> Source of truth: `workflow.yaml`, `tasks.yaml`,
> `domains/architecture_fr/skills/quote_vs_cctp_consistency/examples.md`.

```text
OpenWebUI expose.
Hermes Agent exécute.
Pantheon Next gouverne.
```

---

# 1. Standard internal review run (review_complete)

## Inputs (fictional)

```yaml
project_context_result:
  status: resolved
  selected_project_id: P-001
  selected_project_label: "Demo project P-001"
  confidence: 0.92
inputs:
  cctp_document:
    filename: "P-001_CCTP_LOT-07_v2.0.md"
    version: "2.0"
    date: "YYYY-MM-DD"
    source_status: signed
  quote_document:
    filename: "P-001_devis_DEMO-A_v1.md"
    version: "1.0"
    date: "YYYY-MM-DD"
    source_status: draft
  lot_scope: LOT-07-VMC
```

## Trajectory (selected, no adaptation)

```text
resolve_project_context
  → select_knowledge_sources
    → [extract_cctp_items | extract_quote_items | themis_precheck] (parallel)
      → match_items
        → [technical_risk_pass | quantitative_risk_pass | contractual_risk_pass | regulatory_freshness_check | contradictions_pass] (parallel)
          → consolidate_review
            → apollo_final_gate
              → compose_evidence_pack
```

## Output (compact)

```yaml
final_quality_status: review_complete
quote_vs_cctp_consistency_result:
  matched_items: 18
  missing_items: 1
  divergent_items: 2
  duplicate_items: 0
  out_of_scope_items: 1
  technical_risk_flags: 0
  contractual_risk_flags: 1
  quantitative_risk_flags: 1
  freshness_flags: 0
approval_required:
  level: C1
  reason: review_mode_candidate_output
next_safe_action: "Return result to user; if external use intended, escalate to client_message_draft (C4)."
evidence_pack: EP-DEMO-0001
```

---

# 2. Adapted run — CCTP cites RT2012 on a recent project (revision signal)

## Trigger

`regulatory_freshness_check` flags `RT2012` as `superseded_by_RE2020_for_new_construction` while the PC date is unknown.

## Adaptation (per `WORKFLOW_ADAPTATION.md` §11–§12)

```yaml
workflow_revision_signal:
  emitted_by: HECATE
  severity: C1
  reason: "Regulatory freshness unknown; cannot conclude on RT2012 vs RE2020."
  current_step: regulatory_freshness_check
  recommendation: pause_for_zeus_arbitration
```

ZEUS arbitration:

```yaml
zeus_arbitration:
  decision: combine_options
  modifications:
    - add_step: ask_user_pc_date_and_project_type
    - require_apollo_gate_to_remain_strict_on_freshness
  approval:
    internal_analysis: C1
    external_use: C4
```

## Output (compact)

```yaml
final_quality_status: needs_more_evidence
freshness_flags:
  - subject: regulatory_reference
    family: thermal_regulation
    cctp_value: "RT2012"
    status: superseded_or_unknown
approval_required:
  level: C1
next_safe_action: "Obtain PC date and project type; re-run regulatory_freshness_check."
```

The session workflow is **not** canonized; the adaptation lives only as
a `workflow_candidate` if a reusable pattern is later confirmed.

---

# 3. Reset to baseline — over-broad session option

## Trigger

The workflow was adapted in-session to add a heavy CCAP responsibility
matrix that turned out to over-extend the scope for a one-lot review.

## Reset (per `WORKFLOW_ADAPTATION.md` §13)

```yaml
reset_to_baseline:
  base_template: domains/architecture_fr/workflows/quote_vs_cctp_review/workflow.yaml
  discarded_override: session_2026_05_03_variant_01
  reason: "Generated option was too broad for a single-lot devis vs CCTP."
  keep_log: true
```

The Evidence Pack records the reset event. The baseline workflow above
is re-loaded for the next attempt.

---

# 4. Optional handoff — client message draft (C4)

## Trigger

After `apollo_final_gate` returns `review_complete`, the user requests
a wording for an `entreprise` clarification email.

## Handoff (per `tasks.yaml` step 16)

```yaml
handoff_client_message_draft:
  target_format: domains/architecture_fr/output_formats.md#28-client_message_draft
  target_task_contract: docs/governance/TASK_CONTRACTS.md#73-client_message_review
  source_findings:
    - missing_items: [CCTP-7.5.1]
    - divergent_items: [L7.4]
  approval_required:
    level: C4
    reason: external_communication
  next_safe_action: "Drafted message for user approval; user controls signature and channel."
```

The workflow does **not** auto-send. Pantheon Next does not own the
sending channel.

---

# 5. Review blocked — privacy leak in input

## Trigger

`themis_precheck` detects a real-looking name and address in the
quote excerpt.

## Result

```yaml
final_quality_status: review_blocked
limits:
  - "Privacy leak detected in input (real-looking name and address)."
approval_required:
  level: C1
next_safe_action: "Anonymise input or run outside the repository scope; do not commit any extract here."
```

No artifact is produced for the repository. The Evidence Pack records
the block reason without echoing the leaked content.

---

# 6. Cross-project comparison without authorization

## Trigger

`resolve_project_context` returns CCTP for `P-001` and quote for
`P-002` without an explicit cross-project authorization.

## Result

```yaml
final_quality_status: review_blocked
approval_required:
  level: C3
  reason: cross_project_comparison_requires_authorization
next_safe_action: "Request explicit cross-project authorization or split into two single-project runs."
```

---

# 7. Final note

All examples above use placeholder values (`P-001`, `LOT-07-VMC`,
`DEMO-A`, `EP-DEMO-0001`, `YYYY-MM-DD`). No real client / project /
address / chantier / personal / budget data appears, and none must be
added in this folder.
