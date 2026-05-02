# AI LOG ENTRY — 2026-05-02

Branch: `work/claude/hermes-context-exports`

A: Claude Code

## Objective

Create the Hermes context exports under `hermes/context/` as a compact,
read-only Markdown layer that orients Hermes Agent inside Pantheon Next
governance — without adding any runtime, endpoint, script, code or
automation.

## Operating context

```text
OpenWebUI expose.
Hermes Agent exécute.
Pantheon Next gouverne.
```

## Coordination check

- Verified that ChatGPT branch `work/chatgpt/knowledge-selection-skill`
  touches only `domains/general/skills/knowledge_selection/*` and does
  not touch `hermes/context/`.
- Verified that no branch on `origin/` already creates `hermes/context/`.
- Did **not** modify `domains/general/skills/knowledge_selection/`.
- Did **not** modify `docs/governance/STATUS.md`.
- Did **not** modify `docs/governance/ROADMAP.md`.

## Changes

Created the `hermes/context/` directory and the 9 expected exports:

- `hermes/context/README.md`
- `hermes/context/pantheon_context.md`
- `hermes/context/agents_context.md`
- `hermes/context/rules_context.md`
- `hermes/context/memory_context.md`
- `hermes/context/tools_policy.md`
- `hermes/context/openwebui_context.md`
- `hermes/context/architecture_fr_context.md`
- `hermes/context/software_context.md`

All files:

- declare `Status: Documented / not runtime`;
- point back to `docs/governance/` as source of truth;
- forbid Hermes from canonizing memory or mutating governance Markdown
  without review;
- forbid plugin batch install, secret access, Docker socket access, push
  to `main`, autonomous runtime resurrection;
- include only fictional / generic examples — no real client, project,
  address, person or construction-site data.

## Files Touched

- `hermes/context/README.md`
- `hermes/context/pantheon_context.md`
- `hermes/context/agents_context.md`
- `hermes/context/rules_context.md`
- `hermes/context/memory_context.md`
- `hermes/context/tools_policy.md`
- `hermes/context/openwebui_context.md`
- `hermes/context/architecture_fr_context.md`
- `hermes/context/software_context.md`
- `ai_logs/2026-05-02-hermes-context-exports.md`

## Critical files impacted

- none (no source-of-truth Markdown was modified)

## Tests

- Not run. Documentation only.

## Validation

- Read `ai_logs/README.md` before writing.
- Read `docs/governance/STATUS.md` before writing.
- Read the required governance files: `ARCHITECTURE.md`,
  `HERMES_INTEGRATION.md`, `OPENWEBUI_INTEGRATION.md`, `AGENTS.md`,
  `MEMORY.md`, `APPROVALS.md`, `TASK_CONTRACTS.md`, `EVIDENCE_PACK.md`,
  `EXTERNAL_TOOLS_POLICY.md`, `MODEL_ROUTING_POLICY.md`,
  `KNOWLEDGE_TAXONOMY.md`.
- No code added.
- No endpoint added.
- No script added.
- No external tool integrated.
- No runtime behavior changed.
- No private data added.

## Doctrine alignment

Each export reflects the canonical doctrine:

- Pantheon governs, does not execute.
- Hermes executes, does not canonize.
- OpenWebUI exposes, does not canonize.
- Knowledge ≠ Memory.
- Hermes local memory ≠ Pantheon canonical memory.
- Memory promotion is C3 minimum with Evidence Pack.
- Unknown external tools are blocked until classified.
- Fallbacks cannot replace blocked paths with unreviewed paths.
- Remediation is candidate-only.
- Patches are candidates by default.

## Open points

- **Spelling discrepancy**: the upstream task prompt used the French
  variant `HEPHAISTOS`. The canonical Markdown uses `HEPHAESTUS`
  (`docs/governance/AGENTS.md`). The export aligns on the canonical form
  and explicitly notes the variant. If the canonical Markdown later
  switches to `HEPHAISTOS`, this export must be updated.
- **Tools mentioned without classification**: the upstream task prompt
  mentioned `RAGFlow`, `AKS`, `AgentRQ`, `Kanwas`, `Thoth`,
  `kontext-brain-ts`, `opencode-loop`, `six-hats-skill`. These are not
  present in `docs/governance/EXTERNAL_TOOLS_POLICY.md` at the time of
  writing. The export marks them as "not yet integrated, blocked by
  default until a classification entry is added". Several ChatGPT
  branches (`work/chatgpt/classify-kanwas-aks-agentrq-opencode-sixhats`,
  `work/chatgpt/classify-ragflow-thoth-kontext`) appear to be in flight
  on these classifications; once merged, this export should be
  re-checked.
- **AGENTS.md scope**: the export lists the 13 principal roles named in
  the task prompt and references `docs/governance/AGENTS.md` for the
  remaining roles (METIS, HERA, ARES, DIONYSOS, DEMETER, POSEIDON,
  DAEDALUS). If the canonical principal-role set changes, the export
  must be updated.
- These exports are derived. They will go stale if the canonical
  Markdown moves. They should be reviewed whenever a governance file
  under `docs/governance/` changes.

## Next action

- Open a pull request from `work/claude/hermes-context-exports` into
  `main` for review and merge. No runtime change is required to land
  this PR.
