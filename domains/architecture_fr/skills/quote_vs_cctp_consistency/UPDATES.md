# Quote vs CCTP Consistency — Updates

> Candidate updates for the `quote_vs_cctp_consistency` skill.
> Active version stays in `SKILL.md` and `manifest.yaml` until reviewed.

```text
OpenWebUI expose.
Hermes Agent exécute.
Pantheon Next gouverne.
```

---

# 1. Current status

```yaml
state: candidate
level: 0
validated_xp: 0
pending_xp: 0
review_required: true
```

This skill is not active yet. Promotion to `active` requires review
against `SKILL_LIFECYCLE.md`, `TASK_CONTRACTS.md` §7.2,
`EVIDENCE_PACK.md`, `APPROVALS.md`, `KNOWLEDGE_TAXONOMY.md` and the
domain documents:

```text
domains/architecture_fr/rules.md
domains/architecture_fr/knowledge_policy.md
domains/architecture_fr/output_formats.md
```

---

# 2. Candidate improvements

The following are noted for later review. None of them is applied yet.

## 2.1 Lot-aware matching index

Build a deterministic matcher key from
`(lot_id, normative_reference, label_normalized)` to reduce false
matches when the same component is named differently between CCTP and
quote.

Risk: over-matching if normative references are missing on both sides.

## 2.2 DPGF cross-check

When `dpgf_document` is provided, add a second matching pass:

```text
DPGF item ↔ quote line ↔ CCTP item
```

This raises the chance to catch quantity anomalies when the CCTP is
qualitative and the DPGF is quantitative.

Risk: DPGF / CCTP version mismatch must be checked first; otherwise
the skill will report fake divergences.

## 2.3 CCAP responsibility cross-check

When `ccap_document` is provided, add a contractual-risk pass:

```text
quote line scope ↔ CCAP responsibility allocation
```

This helps surface scope items that look harmless technically but
shift responsibility.

Risk: CCAP wording is generic; THEMIS review remains mandatory before
any conclusion lands in a `client_message_draft` (C4).

## 2.4 Freshness presets

Allow `freshness_window` to take named presets:

```text
current_year
current_quarter
explicit_date_range
```

Risk: presets must not silently auto-extend windows when the regulator
publishes an update mid-year.

## 2.5 Project-context handoff

When the consumer workflow does not pass `project_context`, the skill
should call `project_context_resolution` once and refuse to proceed if
the result is `unresolved` or `ambiguous`. This is currently described
in `SKILL.md` §9 but not enforced.

Risk: implicit cross-project mixing if this guard is skipped.

## 2.6 Output telemetry for THEMIS / APOLLO

Add a small structured field listing the THEMIS / APOLLO items the
consuming workflow should review next, to reduce ambiguity at the
review gate:

```yaml
review_handoff:
  themis_targets: []
  apollo_targets: []
  iris_targets: []
```

Risk: must not be turned into an instruction list — it stays a hint.

---

# 3. Rejected proposals (kept here as memory)

## 3.1 Auto-decision "compliant" / "non-compliant"

Rejected. The skill is review-mode only. A compliance decision is
contractual and belongs to the architect / MOE / MOA / contrôleur
technique, not to Pantheon Next.

## 3.2 Auto-emit a `client_message_draft`

Rejected at this stage. The skill returns a candidate review. Any
client-facing wording must go through the
`client_message_draft` format (C4) and the
`client_message_review` task contract (`TASK_CONTRACTS.md` §7.3).

## 3.3 Auto-promote a recurring pattern to system memory

Rejected. Memory promotion is at least C3 with Evidence Pack and a
separate generalization review (`MEMORY.md`).

---

# 4. Open questions

- How should the skill handle a CCTP that itself cites obsolete
  references? Likely answer: emit a freshness flag on the CCTP itself,
  not just on the quote.
- Should the `risk_flags` schema be shared with other architecture_fr
  skills (`cctp_review`, `dpgf_review`)? Probably yes, but the shared
  schema must live in a domain-level file, not duplicated per skill.
- Should this skill emit a `next_workflow_signal` to suggest opening
  a `cctp_review` for unresolved CCTP items? Out of scope until the
  `cctp_review` skill exists.

---

# 5. Promotion gate (for memory)

When this skill graduates from `candidate` to `active`, it must
explicitly satisfy:

```text
SKILL_LIFECYCLE.md gate
TASK_CONTRACTS.md §7.2 alignment
EVIDENCE_PACK.md required fields produced on real-style runs
APPROVALS.md mapping verified
KNOWLEDGE_TAXONOMY.md sources verified (no cross-project mixing)
domains/architecture_fr/rules.md hard limits respected
domains/architecture_fr/knowledge_policy.md §6.bis freshness check applied
```

Until then: status remains `candidate`, level stays at `0`, no XP is
assigned.
