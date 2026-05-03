# Quote vs CCTP Review — Workflow updates

> Candidate updates for the `quote_vs_cctp_review` workflow.
> Active version stays in `workflow.yaml` and `tasks.yaml` until reviewed.

```text
OpenWebUI expose.
Hermes Agent exécute.
Pantheon Next gouverne.
```

---

# 1. Current status

```yaml
state: candidate
version: 0.1.0
review_required: true
```

This workflow is not active yet. Promotion to `active` requires review
against `WORKFLOW_SCHEMA.md` §7, `WORKFLOW_ADAPTATION.md` §2,
`TASK_CONTRACTS.md` §7.2, `EVIDENCE_PACK.md`, `APPROVALS.md`,
`KNOWLEDGE_TAXONOMY.md` and the domain documents:

```text
domains/architecture_fr/rules.md
domains/architecture_fr/knowledge_policy.md
domains/architecture_fr/output_formats.md
domains/architecture_fr/skills/quote_vs_cctp_consistency/SKILL.md
```

---

# 2. Candidate improvements

The following are noted for later review. None of them is applied yet.

## 2.1 Make the freshness check mandatory upstream of consolidation

Today `regulatory_freshness_check` is one of five parallel passes
joined by `consolidate_review`. A safer variant blocks consolidation
when freshness is `unknown` for a regulation that the matching pass
flagged as load-bearing for the conclusion.

Risk: false positives that block low-risk reviews; would need a
regulation-importance gate.

## 2.2 Add a `cctp_review` handoff for unresolved CCTP items

When `missing_items` are large or structural, the workflow could hand
off to a future `cctp_review` skill / workflow rather than ask the
user a clarification question.

Risk: depends on `cctp_review` not yet existing.

## 2.3 Promote the freshness schema to a domain-level shared file

The freshness payload (`source_family`, `source_id`, `last_checked`,
`check_required_after`, `status`) is duplicated between this workflow,
the `quote_vs_cctp_consistency` skill and `knowledge_policy.md` §6.bis.
A shared `domains/architecture_fr/policies/freshness_schema.yaml`
would centralize it.

Risk: must not duplicate `KNOWLEDGE_TAXONOMY.md` §8 — the canonical
source stays in governance.

## 2.4 Optional `arena` pattern for contradiction surfacing

For very contentious quotes, run two `contradictions_pass` instances
with different framings and have ZEUS arbitrate.

Risk: cost / time; should be opt-in only.

## 2.5 Run-graph hooks

Emit lightweight events at each step (`run.created`, `agent.started`,
`agent.completed`, `consultation.requested`, `veto.warning`,
`approval.required`, `artifact.created`, `run.completed`,
`run.failed`) per `MODULES.md` §2.14.

Risk: must avoid raw chain-of-thought in the trace.

## 2.6 Output telemetry for the `client_message_draft` handoff

When the user later requests a draft, surface the most relevant
findings to IRIS in a small structured payload to reduce the chance
of misalignment between the review and the wording.

Risk: must not act as instructions; remains hint only.

---

# 3. Rejected proposals (kept here as memory)

## 3.1 Auto-decision "compliant" / "non-compliant"

Rejected. The workflow is review-mode. Compliance is contractual and
belongs to the architect / MOE / MOA / contrôleur technique.

## 3.2 Auto-emit a `client_message_draft`

Rejected. Drafting external wording is C4 and goes through the
`client_message_review` task contract (`TASK_CONTRACTS.md` §7.3).

## 3.3 Skip `apollo_final_gate` to speed up internal reviews

Rejected. APOLLO gate is non-negotiable
(`WORKFLOW_ADAPTATION.md` §2).

## 3.4 Allow cross-project mixing without authorization

Rejected. Privacy and `KNOWLEDGE_TAXONOMY.md` §6 require explicit
authorization.

---

# 4. Open questions

- Should `quantitative_risk_pass` be promoted to **always** require
  `dpgf_items` when DPGF is provided? Currently the join policy
  includes optional inputs if ready; making it required when present
  could be safer.
- Should `themis_precheck` be split into a "policy precheck" (fast,
  parallel-safe) and a "responsibility precheck" (slower, joined into
  `contractual_risk_pass`)? Probably yes, but only after a real-world
  baseline.
- How should the workflow handle a CCTP that itself cites obsolete
  standards (cf. `quote_vs_cctp_consistency/UPDATES.md` §4)? Likely
  by emitting a freshness flag on the CCTP itself.

---

# 5. Promotion gate (for memory)

When this workflow graduates from `candidate` to `active`, it must
explicitly satisfy:

```text
WORKFLOW_SCHEMA.md §7 validation rules
WORKFLOW_ADAPTATION.md §2 non-negotiable boundaries
TASK_CONTRACTS.md §7.2 alignment
EVIDENCE_PACK.md required and domain-specific fields produced on real-style runs
APPROVALS.md mapping verified
KNOWLEDGE_TAXONOMY.md sources verified (no cross-project mixing)
domains/architecture_fr/rules.md hard limits respected
domains/architecture_fr/knowledge_policy.md §6.bis freshness check applied
domains/architecture_fr/output_formats.md handoff to client_message_draft preserved as C4
```

Until then: status remains `candidate`, version stays at `0.1.0`, no
canonization.
