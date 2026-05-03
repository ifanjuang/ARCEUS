# Quote vs CCTP Review — Workflow tests

> Documentation-level tests. They define expected behavior **before**
> any runtime implementation. Pantheon Next is governance-only; the
> test runner sits in Hermes / OpenWebUI / external CI.

```text
OpenWebUI expose.
Hermes Agent exécute.
Pantheon Next gouverne.
```

All inputs are fictional. No real project / client / address /
chantier / personal / budget data.

Reference: `workflow.yaml`, `tasks.yaml`,
`domains/architecture_fr/skills/quote_vs_cctp_consistency/tests.md`,
`docs/governance/WORKFLOW_SCHEMA.md` §7,
`docs/governance/WORKFLOW_ADAPTATION.md` §17.

---

# 1. Schema validity

## Given

`workflow.yaml` and `tasks.yaml` of this workflow.

## Expected

The workflow must satisfy `WORKFLOW_SCHEMA.md` §7:

- two tasks must not share the same `id`;
- every `dependencies` entry must reference a known task `id`;
- every task must declare an `expected output` (via `outputs`);
- every task with `execution_mode: skill` must declare an
  `assigned_skill` that exists;
- C3+ tasks must declare an approval path;
- consequential outputs must declare `evidence_required: true`;
- `memory_impact` must be defined at workflow level;
- external tools used must be allowlisted.

The workflow must additionally satisfy `WORKFLOW_ADAPTATION.md` §2:

- no silent approval lowering;
- no removal of THEMIS veto;
- no removal of APOLLO gate;
- no auto-promotion of memory;
- no canonization of a session-generated workflow.

---

# 2. Resolve project context first

## Given

A user request that depends on project documents.

## Expected

`resolve_project_context` runs first. If `status` is `unresolved` or
`ambiguous`, the workflow stops with explicit reason. No downstream
task is started.

---

# 3. Knowledge selection precedes extraction

## Given

`resolve_project_context` returns `resolved`.

## Expected

`select_knowledge_sources` runs before any `extract_*` task. The
selection must forbid cross-project mixing without explicit
authorization.

---

# 4. Extraction tasks may run in parallel

## Given

`extract_cctp_items`, `extract_quote_items`, `themis_precheck` are in
the same `parallel_group: extraction_pass`.

## Expected

These three tasks may start as soon as their dependencies are met,
without waiting for each other. `extract_dpgf_items` and
`extract_ccap_items` are optional and join the group only if their
inputs are present.

Parallel execution must be:

- bounded;
- read-only or non-authoritative;
- not modifying the same file or state;
- joined and checked before final output;
- recorded in the Evidence Pack.

(Per `WORKFLOW_ADAPTATION.md` §10.)

---

# 5. Match runs only after both extractions

## Given

`extract_cctp_items` and `extract_quote_items` are required upstream
of `match_items`.

## Expected

`match_items` waits for both. If either fails, `match_items` does not
start. Optional `dpgf_items` and `ccap_clauses` are joined per
`join_policy: wait_required_then_include_optional_if_ready`.

---

# 6. Risk passes are independent of each other

## Given

After `match_items`, four passes run:

- `technical_risk_pass`,
- `quantitative_risk_pass`,
- `contractual_risk_pass`,
- `regulatory_freshness_check`,

plus `contradictions_pass`.

## Expected

These five passes may run in parallel. Each declares
`evidence_required: true` where applicable. None mutates Pantheon
source-of-truth files. None sends anything externally.

---

# 7. Consolidation joins all required risk passes

## Given

Several risk passes returned.

## Expected

`consolidate_review` waits for `technical_risk_pass`,
`quantitative_risk_pass`, `contractual_risk_pass`,
`regulatory_freshness_check` and `contradictions_pass`. It produces
`quote_vs_cctp_consistency_result_draft`, `hypotheses` and `limits`.

---

# 8. APOLLO gate is mandatory before final result

## Given

`consolidate_review` returns a draft.

## Expected

`apollo_final_gate` runs and returns one of:

```text
review_complete
needs_more_evidence
review_blocked
```

A workflow run that bypasses `apollo_final_gate` is invalid.

---

# 9. THEMIS veto cannot be removed

## Given

`themis_precheck` and `contractual_risk_pass`.

## Expected

A workflow override that removes THEMIS from the run is rejected
under `WORKFLOW_ADAPTATION.md` §2 ("must not remove THEMIS veto").
The skill itself enforces a `review_blocked` if THEMIS is missing
from the consuming workflow (`skills/.../tests.md` §12).

---

# 10. Evidence Pack is composed before any external handoff

## Given

`apollo_final_gate` returned `review_complete`.

## Expected

`compose_evidence_pack` runs **before** any
`handoff_client_message_draft` (C4) is allowed to start. The
Evidence Pack must include both the canonical fields and the
domain-specific fields declared in `workflow.yaml`.

---

# 11. Client message draft handoff is C4 and never auto-sends

## Given

User intent to send a clarification message after the review.

## Expected

```yaml
handoff_client_message_draft:
  criticity: C4
  forbidden:
    - auto_send_message
    - publish_to_third_party_channel
```

The workflow hands off to
`output_formats.md#28-client_message_draft` and to the
`client_message_review` task contract. The user controls the channel.

---

# 12. Memory impact stays candidate-only by default

## Given

A run that surfaces a recurring matching pattern that looks like a
generalizable rule.

## Expected

`memory_impact: candidate_only_if reusable_pattern_detected`. No
project memory write, no system memory write. Promotion stays at
C3+ with explicit review.

---

# 13. Privacy leak in input blocks the workflow early

## Given

An input contains a real-looking name, address or client identifier.

## Expected

`themis_precheck` flags the leak. `match_items` does not start.
`final_quality_status: review_blocked` and the Evidence Pack records
the block without echoing the leaked content.

---

# 14. Cross-project comparison without authorization is blocked

## Given

CCTP and quote belong to different `project_id` values without an
explicit cross-project authorization.

## Expected

`resolve_project_context` (or `themis_precheck`) blocks the run with:

```yaml
final_quality_status: review_blocked
approval_required:
  level: C3
  reason: cross_project_comparison_requires_authorization
```

---

# 15. Adaptation does not lower approval

## Given

A session adaptation tries to set `approval_default.level: C0` to
"speed up" review-mode runs.

## Expected

The adaptation is rejected (`WORKFLOW_ADAPTATION.md` §2,
`adaptation.must_not.lower_approval_silently`). The workflow keeps
`C1` as the default and escalates per `approval_points`.

---

# 16. Reset to baseline preserves Evidence

## Given

A session override is reset to baseline.

## Expected

```yaml
reset_to_baseline:
  base_template: domains/architecture_fr/workflows/quote_vs_cctp_review/workflow.yaml
  keep_log: true
```

The Evidence Pack and the run log are kept. The session override is
discarded. Source documents are never deleted.

---

# 17. Final rule

```text
The tests above are the contract.
A passing run for any of them must remain candidate output.
A failing run blocks promotion of the workflow to active.
```
