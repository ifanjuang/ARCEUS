# software domain — context for Hermes

> Compact orientation. Source of truth: `docs/governance/MODULES.md`,
> `docs/governance/ARCHITECTURE.md`,
> `docs/governance/CODE_AUDIT_POST_PIVOT.md`,
> `docs/governance/PRE_REFACTOR_ARCHITECTURE_FINDINGS.md`,
> `docs/governance/APPROVALS.md`,
> `docs/governance/EVIDENCE_PACK.md`,
> domain folder `domains/software/`.

Status: **Documented / not runtime**.

---

## 1. Domain scope

`software` is the audit / governance / refactor domain for the Pantheon
Next repository itself.

It carries:

- repository audit;
- Markdown / code consistency audit;
- legacy classification post-pivot;
- API layer analysis;
- minimal security review;
- dependency review;
- context export drafting;
- naming and structural conventions;
- test coverage observations;
- patch candidate proposals.

The domain folder is `domains/software/`.

---

## 2. Default posture

```text
Document first.
Patch candidate, never direct refactor.
Diagnose before deletion.
Never reactivate the autonomous runtime path by accident.
```

A repository audit is **C0** by default (read / diagnostic). Any output
that mutates files becomes **C3** (file mutation, candidate patch). Any
output that touches `docs/governance/` source-of-truth Markdown is at
least **C3** and requires explicit validation.

Reference: `docs/governance/APPROVALS.md` §3,
`docs/governance/TASK_CONTRACTS.md` §7.1 (`repo_consistency_audit`),
`docs/governance/TASK_CONTRACTS.md` §7.6 (`legacy_component_audit`).

---

## 3. Legacy classification

Before modifying any legacy component, classify it in
`docs/governance/CODE_AUDIT_POST_PIVOT.md` using one of:

```text
keep
reorient
archive
delete_later
to_verify
legacy
```

Hard rules:

- **Do not delete useful legacy code before diagnosis.**
- **Do not reactivate** the previous autonomous runtime path
  (Execution Engine, Agent Runtime, Tool Runtime, Provider Router,
  central scheduler, central LangGraph, memory auto-promotion,
  self-evolution auto-merge, batch plugin install).
- Preferred outcome for ambiguous legacy code: **reorient or
  archive**, not delete.

Reference: `docs/governance/PRE_REFACTOR_ARCHITECTURE_FINDINGS.md` for
patterns and assets worth preserving (Domain Layer API, context-pack
endpoint, manifest contracts, task/workflow contracts, approval queue,
hybrid retrieval, OCR fallback pattern, circuit breaker, trusted source
registry, Evidence trace fields, memory supersession model, Hermes skill
lifecycle).

---

## 4. Allowed Hermes actions in this domain

Under task contract and within approval scope, Hermes may:

- read repository files;
- search files;
- run `git diff` / `git log` style read-only inspection;
- run scoped, safe diagnostic commands;
- compare Markdown source-of-truth files with the current tree;
- prepare candidate Markdown updates;
- prepare candidate code patches **on a dedicated branch**;
- propose tests;
- propose rollback;
- produce Evidence Packs.

---

## 5. Forbidden Hermes actions in this domain

Hermes must not, by default:

- push to `main`;
- delete files marked `to_verify`, `legacy`, `delete_later` or unclassified;
- mutate files outside the task contract scope;
- reactivate or recreate the autonomous runtime path;
- introduce a new Pantheon scheduler, provider router, tool runtime or
  agent runtime;
- silently merge a candidate patch;
- run destructive shell commands;
- access secrets;
- access the Docker socket;
- skip hooks / signing;
- amend or force-push shared branches.

---

## 6. Patch candidate discipline

Every patch produced by Hermes is, by default, a **candidate**:

```text
branch:        work/<agent>/<short-slug>  or  feature/<agent>/<short-slug>
status:        candidate_patch
mode:          read-and-propose
final_apply:   requires explicit approval
ai_log_entry:  required after meaningful intervention
```

A candidate patch must include:

- a clear scope statement;
- the files touched;
- the diff;
- a test plan (or "no test run" with the reason);
- a rollback note;
- an Evidence Pack reference.

Reference: `docs/governance/EVIDENCE_PACK.md`,
`docs/governance/TASK_CONTRACTS.md`.

---

## 7. AI log discipline

After any meaningful intervention on the repository (audit, candidate,
governance proposal), add:

```text
ai_logs/YYYY-MM-DD-slug.md
```

Reference: `ai_logs/README.md`.

The entry should record: branch, agent, objective, files touched, critical
files impacted, tests run (or not), open points, next action.

---

## 8. Coordination with other agents

Multiple AI agents (Claude, ChatGPT, others) may work on this repository
in parallel. Before opening a branch:

1. `git fetch --all --prune`;
2. read the recent `ai_logs/` entries (≥ last 14 days);
3. inspect open `work/*` and `claude/*` branches;
4. avoid touching files already in flight on another agent's branch
   unless coordinated through an explicit AI log entry.

If a conflict is detected, prefer a smaller, narrower patch on a
non-overlapping file set.

---

## 9. Final rule

```text
Documentation first.
Diagnostic before mutation.
Candidate before canonization.
Reorient before deletion.
Never resurrect the autonomous runtime path by accident.
```
