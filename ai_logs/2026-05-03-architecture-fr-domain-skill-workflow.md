# AI LOG ENTRY — 2026-05-03

Branch: `work/claude/architecture-fr-domain-package`

A: Claude Code

## Objective

Extend the `domains/architecture_fr/` package (PR #97) with:

- the top-level `domain.md` summary (referenced in `MODULES.md` §2.2,
  previously missing on `main`);
- the first post-pivot candidate skill `quote_vs_cctp_consistency`
  (review-mode, candidate, no runtime);
- the first canonical workflow template `quote_vs_cctp_review` aligned
  with `WORKFLOW_SCHEMA.md` §2 (folder per workflow) and the adaptive
  doctrine of `WORKFLOW_ADAPTATION.md`.

Documentation only. No runtime, no code, no endpoint, no script, no
automation. Fictional examples only.

## Operating context

```text
OpenWebUI expose.
Hermes Agent exécute.
Pantheon Next gouverne.
```

## Coordination check

- `git fetch --all --prune` done before work.
- ChatGPT in flight on `work/chatgpt/sync-hermes-tools-policy`,
  `work/chatgpt/workflow-adaptation-doctrine`,
  `work/chatgpt/sync-workflow-adaptation-refs`. None of those branches
  touch `domains/architecture_fr/`.
- Forbidden files explicitly **not** modified:
  - `docs/governance/STATUS.md`
  - `docs/governance/ROADMAP.md`
  - `docs/governance/AGENTS.md`
  - `docs/governance/WORKFLOW_SCHEMA.md`
  - `docs/governance/WORKFLOW_ADAPTATION.md`
  - `docs/governance/TASK_CONTRACTS.md`
  - `platform/`
  - `hermes/context/`
  - `README.md`
- `domains/general/skills/knowledge_selection/` — referenced as a
  consumed skill in the new workflow `tasks.yaml`, but **not** modified.

## Changes

### Domain top-level

| File | Status | Summary |
|---|---|---|
| `domains/architecture_fr/domain.md` | new | Identity, scope, operating posture, structure, abstract agents most often involved, skills inventory, workflows inventory, Knowledge mapping, memory posture, output formats catalogue, forbidden patterns. References all governance docs and pre-existing files. Acknowledges the `HEPHAISTOS` (WORKFLOW_ADAPTATION.md) vs `HEPHAESTUS` (AGENTS.md) spelling variant and aligns on the canonical `AGENTS.md` form. |

### Skill — `quote_vs_cctp_consistency` (status: candidate)

| File | Status | Summary |
|---|---|---|
| `domains/architecture_fr/skills/quote_vs_cctp_consistency/SKILL.md` | new | Purpose, default operating mode (review, C1), inputs/outputs schema, comparison procedure, allowed/forbidden actions, need-for-context check, risk classes, confidence policy, integration with the workflow, privacy, status |
| `domains/architecture_fr/skills/quote_vs_cctp_consistency/manifest.yaml` | new | Canonical skill manifest (id, name, domain, status: candidate, version 0.1.0, lifecycle, mode: review, task_contract_reference, inputs, outputs, capabilities, allowed_actions, forbidden_actions, agents, knowledge_sources, approval_default + escalation, memory_impact, evidence_required + minimum + domain-specific fields, confidence_policy, privacy, risks, review gate). `api_module: null` — no runtime binding. |
| `domains/architecture_fr/skills/quote_vs_cctp_consistency/examples.md` | new | 8 fictional scenarios: matched item, missing item, divergence, out-of-scope, freshness flag, privacy block, cross-project block, final note on placeholders. |
| `domains/architecture_fr/skills/quote_vs_cctp_consistency/tests.md` | new | 14 documentation-level tests covering matching, missing, divergence, duplicates, freshness, privacy block, cross-project block, search-snippet rejection, candidate-only memory, no auto-send, THEMIS/APOLLO required, auditable Evidence Pack. |
| `domains/architecture_fr/skills/quote_vs_cctp_consistency/UPDATES.md` | new | Candidate improvements (lot-aware index, DPGF/CCAP cross-checks, freshness presets, project-context handoff guard, review-handoff telemetry), rejected proposals (auto-decision, auto-emit client message, auto memory promotion), open questions, promotion gate. |

### Workflow — `quote_vs_cctp_review` (status: candidate)

| File | Status | Summary |
|---|---|---|
| `domains/architecture_fr/workflows/quote_vs_cctp_review/workflow.yaml` | new | Metadata aligned with `WORKFLOW_SCHEMA.md` §3: id, name, domain, status: candidate, version 0.1.0, pattern: cascade, adaptive: true, purpose, inputs, outputs, agents, skills, approval_default + approval_points, memory_impact (candidate_only_if reusable_pattern_detected), evidence_required + minimum + domain-specific fields, knowledge_sources, allowed_tools / forbidden_tools, fallback (forbidden_fallbacks, on_blocked_or_incomplete: keep_as_diagnostic_if_sources_are_incomplete), remediation (no auto-fix), adaptation block (per WORKFLOW_ADAPTATION.md), execution_plan_reference, risks, review gate. |
| `domains/architecture_fr/workflows/quote_vs_cctp_review/tasks.yaml` | new | Dependency graph (per WORKFLOW_ADAPTATION.md §9) with 17 steps: resolve_project_context, select_knowledge_sources, parallel extraction pass (cctp / quote / dpgf-optional / ccap-optional / themis_precheck), match_items, four parallel risk passes + contradictions, consolidate_review (join), apollo_final_gate, compose_evidence_pack, optional handoff to client_message_draft (C4) and emit_revision_signal_if_needed. Each step declares role, execution_mode, inputs / dependencies / outputs, tools_allowed / tools_forbidden, criticity, evidence_required, approval_required_if. |
| `domains/architecture_fr/workflows/quote_vs_cctp_review/examples.md` | new | 7 fictional scenarios: standard run, RT2012 freshness adaptation with revision signal, reset_to_baseline, client_message_draft handoff (C4), privacy block, cross-project block, final note on placeholders. |
| `domains/architecture_fr/workflows/quote_vs_cctp_review/tests.md` | new | 17 documentation-level tests covering schema validity, ordering, parallel groups, joins, APOLLO gate non-bypass, THEMIS non-removal, Evidence Pack precedence, C4 handoff, candidate-only memory, privacy block, cross-project block, no-approval-lowering, reset preserves Evidence. |
| `domains/architecture_fr/workflows/quote_vs_cctp_review/UPDATES.md` | new | Candidate improvements (mandatory upstream freshness, future cctp_review handoff, shared freshness schema, optional `arena` for contradictions, run-graph hooks, IRIS handoff telemetry), rejected proposals (auto-decision, auto client message, skip APOLLO gate, cross-project mixing), open questions, promotion gate. |

### AI log

| File | Status | Summary |
|---|---|---|
| `ai_logs/2026-05-03-architecture-fr-domain-skill-workflow.md` | new | This log |

## Files Touched

- `domains/architecture_fr/domain.md`
- `domains/architecture_fr/skills/quote_vs_cctp_consistency/SKILL.md`
- `domains/architecture_fr/skills/quote_vs_cctp_consistency/manifest.yaml`
- `domains/architecture_fr/skills/quote_vs_cctp_consistency/examples.md`
- `domains/architecture_fr/skills/quote_vs_cctp_consistency/tests.md`
- `domains/architecture_fr/skills/quote_vs_cctp_consistency/UPDATES.md`
- `domains/architecture_fr/workflows/quote_vs_cctp_review/workflow.yaml`
- `domains/architecture_fr/workflows/quote_vs_cctp_review/tasks.yaml`
- `domains/architecture_fr/workflows/quote_vs_cctp_review/examples.md`
- `domains/architecture_fr/workflows/quote_vs_cctp_review/tests.md`
- `domains/architecture_fr/workflows/quote_vs_cctp_review/UPDATES.md`
- `ai_logs/2026-05-03-architecture-fr-domain-skill-workflow.md`

## Critical files impacted

- none. The legacy `domains/architecture_fr/manifest.yaml`, the legacy
  flat workflows (`recherche_documentaire.yaml`,
  `decision_strategique.yaml`, `reponse_rapide.yaml`), the legacy
  skill manifests (`chantier`, `communications`, `decisions`,
  `finance`, `planning`, `webhooks`) and the existing
  `knowledge_policy.md` (extended additively in PR #97 head) are
  **not** modified by this commit.

## Tests

- Not run. Documentation only.

## Validation

- Read `ai_logs/README.md`.
- Read `docs/governance/STATUS.md` (no modification).
- Read `docs/governance/MODULES.md`.
- Read `docs/governance/WORKFLOW_SCHEMA.md` (no modification).
- Read `docs/governance/WORKFLOW_ADAPTATION.md` (no modification).
- Read `docs/governance/TASK_CONTRACTS.md` (no modification — already
  loaded earlier in this session).
- Read existing skill format from
  `domains/general/skills/project_context_resolution/{SKILL.md,manifest.yaml,examples.md,tests.md,UPDATES.md}`
  to align skill structure.
- Read existing workflow format from
  `domains/architecture_fr/workflows/{decision_strategique.yaml,recherche_documentaire.yaml}`
  to acknowledge the legacy flat schema (not modified).
- All examples are fictional (`P-001`, `LOT-07-VMC`, `DEMO-A`,
  `EP-DEMO-0001`, `YYYY-MM-DD`, `€X XXX,XX`).
- No real client / project / address / chantier / personal / budget
  data introduced.
- No code, no endpoint, no script, no automation.
- No autonomous runtime path reactivated.
- Skill status is `candidate`. Workflow status is `candidate`. No
  level-up, no canonization.
- Workflow declares `adaptive: true` per `WORKFLOW_ADAPTATION.md` §1
  but enforces the non-negotiable boundaries in §2 (no silent approval
  lowering, no THEMIS/APOLLO removal, no auto memory promotion, no
  external send without C4, no canonization of session workflows).

## Doctrine alignment

- Pantheon governs, does not execute.
- Hermes executes the resulting Task Contract; not invoked here.
- OpenWebUI exposes; not invoked here.
- Workflow is a **dependency graph** (per `WORKFLOW_ADAPTATION.md` §9),
  not a linear chain.
- Parallel execution declared only for bounded, read-only / non-
  authoritative steps (extraction, risk passes, contradictions).
- THEMIS pre-check + final contractual risk pass + APOLLO gate are
  non-bypassable.
- External wording handoff to `client_message_draft` is **C4**;
  Pantheon Next does not own the sending channel.
- Memory is **candidate_only**; no automatic promotion.
- Regulatory citations require source, tier and freshness check
  (`domains/architecture_fr/knowledge_policy.md` §6.bis).
- Evidence Pack is mandatory for any consequential output.
- `domains/architecture/` (without `_fr`) **not** recreated.

## Open points

- **Spelling variant `HEPHAISTOS` vs `HEPHAESTUS`**:
  `WORKFLOW_ADAPTATION.md` (just merged) uses `HEPHAISTOS`; the
  canonical `AGENTS.md` and this domain align on `HEPHAESTUS`.
  Surfaced in `domain.md` §5; left for governance to reconcile in a
  dedicated PR.
- **Manifest stale field**: `domains/architecture_fr/manifest.yaml`
  carries `domain: architecture` (without `_fr`) on `main`. **Not**
  fixed here to keep this PR scoped; should be fixed in a follow-up
  alongside the legacy flat workflows migration.
- **Legacy flat workflows**: `recherche_documentaire.yaml`,
  `decision_strategique.yaml`, `reponse_rapide.yaml` follow an older
  schema (`flow:` block, French agent names like `APOLLON`,
  `KAIROS`, `DEDALE`). Not migrated here; out of scope.
- **`STATUS.md` / `ROADMAP.md`** should eventually mention this
  scaffold (`domain.md`, first post-pivot candidate skill, first
  canonical workflow template). Reserved for a separate sync PR
  (forbidden scope here).
- **Inherited CI**: this branch still inherits the `Lint` and `Tests`
  failures documented in PR #93 §10 (stale `modules.*` patches in
  test files; pending `ruff format`). PR #97 cannot fix those without
  scope creep.

## Next action

- Push commit on `work/claude/architecture-fr-domain-package` to
  extend PR #97. Update PR title / body to reflect the expanded
  scope.
- Once PR #93 (CI lint repair) merges, rebase #97 to inherit a green
  Lint baseline. Tests will still fail until the test rename PR
  ships.
