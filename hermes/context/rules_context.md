# Transversal rules — context for Hermes

> Compact orientation. Source of truth: `docs/governance/APPROVALS.md`,
> `docs/governance/EVIDENCE_PACK.md`, `docs/governance/HERMES_INTEGRATION.md`,
> `docs/governance/MEMORY.md`, `docs/governance/EXTERNAL_TOOLS_POLICY.md`,
> `docs/governance/MODEL_ROUTING_POLICY.md`.

Status: **Documented / not runtime**.

---

## 1. Default posture

```text
Documentation first.
Contracts before execution.
Evidence before conclusion.
Candidates before canonization.
```

When in doubt: stop, ask, do not escalate silently.

---

## 2. Hard rules

Hermes must always respect the following, on every task:

1. **No push to `main`.** Work on a dedicated branch.
2. **No modification of Markdown source-of-truth files** under
   `docs/governance/` or root governance entry points (`README.md`,
   `CLAUDE.md`, `CHANGELOG.md`, `VERSION`) without an explicit task
   contract and approval. Patch candidates only by default.
3. **No Pantheon runtime resurrection.** No execution engine, no agent
   runtime, no tool runtime, no provider router, no scheduler, no
   LangGraph central orchestrator inside Pantheon Next.
4. **No external tool without policy.** Unknown tools are blocked until
   classified in `docs/governance/EXTERNAL_TOOLS_POLICY.md`.
5. **No memory auto-promotion.** Promotion is at least C3 and requires an
   Evidence Pack.
6. **Fallbacks are bounded.** A blocked path cannot be replaced by an
   unreviewed path. A higher-risk fallback requires new approval.
7. **Remediation is candidate-only.** Detect → document → propose →
   validate → apply. Never auto-apply.
8. **Evidence Pack is mandatory** for any consequential output. A model
   statement is not evidence.
9. **Privacy by default.** No real client, project, address, person or
   construction site data may be written into the repository.

---

## 3. Approval levels (summary)

| Level | Definition | Default rule |
|---|---|---|
| C0 | read / diagnostic | proceed within scope |
| C1 | draft / suggestion | proceed unless sensitive |
| C2 | low-risk reversible action | trace required |
| C3 | persistent internal change | explicit validation required |
| C4 | external / contractual / financial / responsibility | explicit user approval required |
| C5 | critical / irreversible / secrets / destructive | blocked by default |

Reference: `docs/governance/APPROVALS.md`.

---

## 4. Allowed Hermes actions (default)

Hermes may, under task contract and within approval scope:

- read repository files;
- search files;
- compare documentation and code;
- run scoped, safe diagnostic commands;
- prepare candidate patches;
- draft local skills;
- propose Pantheon skill / workflow / memory candidates;
- produce Evidence Packs;
- inspect external repositories as inspiration only.

---

## 5. Forbidden Hermes actions (default)

Hermes must never, by default:

- push to `main`;
- mutate validated project memory;
- mutate validated system memory;
- promote a skill to active;
- change active workflows directly;
- bypass `APPROVALS.md`;
- bypass THEMIS or APOLLO when their review is required;
- read undocumented internal state unless policy explicitly allows it;
- access secrets;
- access the Docker socket;
- send external communications without C4 approval;
- install plugins outside the allowlist;
- batch-install skills, plugins or tools;
- self-modify Pantheon governance;
- silently use a higher-risk fallback;
- silently use a remote / unreviewed model for C4 / C5 outputs.

---

## 6. Fallback rule

A fallback is allowed inside the task contract only if:

- intent is unchanged;
- tool stays allowlisted;
- risk is equal or lower;
- data exposure does not increase silently;
- the Evidence Pack records the failed attempt and the substitution.

Forbidden fallbacks:

```text
unallowlisted tool
destructive action
external send
secret access
Docker socket
memory write
plugin install
remote MCP server not audited
bypassing a blocked policy
```

Reference: `docs/governance/APPROVALS.md` §7,
`docs/governance/TASK_CONTRACTS.md` §5,
`docs/governance/EXTERNAL_TOOLS_POLICY.md` §8.

---

## 7. Remediation rule

When something fails, blocks or is inconsistent, Hermes may open a
remediation candidate lane:

- analyze the issue;
- identify the affected component;
- propose a fix;
- prepare a patch candidate;
- propose tests;
- propose rollback;
- produce an Evidence Pack.

It must not auto-apply, bypass approval, mutate validated memory, activate
skills, change workflows, alter policies, modify runtime configuration,
access secrets or use the Docker socket.

```text
Detect → document → propose → validate → apply.
```

---

## 8. Evidence Pack — minimum frame

Every consequential output must include:

```text
files_read
sources_used
commands_run
tools_used
knowledge_bases_consulted
documents_used
assumptions
unsupported_claims
limitations
outputs
approval_required
next_safe_action
```

If a test was not run, say so. If a source was not verified, say so. If a
claim is inferred, say so. Limitations are not optional.

Reference: `docs/governance/EVIDENCE_PACK.md`.

---

## 9. Model routing rule

Pantheon defines the policy. Hermes resolves and executes the call.
OpenWebUI exposes presets.

For C4 / C5 outputs, Hermes must not silently fall back to a less
qualified or remote model. Fallback must stop or escalate.

Reference: `docs/governance/MODEL_ROUTING_POLICY.md`.

---

## 10. AI log discipline

After any meaningful intervention, add an entry under `ai_logs/`:

```text
ai_logs/YYYY-MM-DD-slug.md
```

Reference: `ai_logs/README.md`.

This applies to Hermes-driven sessions when the resulting output is meant
to land in the Pantheon repository.
