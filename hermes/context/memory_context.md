# Memory model — context for Hermes

> Compact orientation. Source of truth: `docs/governance/MEMORY.md`,
> `docs/governance/KNOWLEDGE_TAXONOMY.md`,
> `docs/governance/MEMORY_EVENT_SCHEMA.md`,
> `docs/governance/EVIDENCE_PACK.md`.

Status: **Documented / not runtime**.

---

## 1. Four levels

```text
SESSION → CANDIDATES → PROJECT or SYSTEM
```

| Level | Status | Role | Authority |
|---|---|---|---|
| Session | temporary | working context for the current interaction | not reliable beyond the session |
| Candidates | persisted but not validated | proposed facts, patterns, rules, skills, workflows | not canonical |
| Project | validated project context | project-specific facts, decisions, constraints | canonical for that project only |
| System | validated reusable memory | reusable rules, methods, patterns, conventions | canonical across Pantheon |

Terminology rule:

```text
Use system memory, not agency memory.
```

---

## 2. Promotion cycle

```text
SESSION
→ CANDIDATES
→ Evidence Pack
→ THEMIS validation
→ APOLLO quality check
→ PROJECT or SYSTEM
```

Memory promotion is **at least C3**.

There is **no automatic promotion**. There is **no silent canonization**.

A candidate becomes memory only if all of the following hold:

- source is identifiable;
- evidence is available;
- scope is clear;
- target memory level is justified;
- usefulness is real;
- contradiction check is complete;
- privacy risk is reviewed;
- cross-project contamination risk is reviewed;
- stale-source risk is reviewed.

Reference: `docs/governance/MEMORY.md` §7-§8.

---

## 3. Knowledge ≠ Memory

| Element | Knowledge | Memory |
|---|---|---|
| Uploaded document (PDF, CCTP, devis, notice) | yes | no |
| OpenWebUI Knowledge collection | yes | no |
| Validated project fact | maybe source | project memory |
| Validated reusable rule | maybe source | system memory |
| Pantheon policy | can be mirrored in Knowledge | canonical in Markdown |

Hard boundaries Hermes must respect:

- **OpenWebUI Knowledge ≠ Pantheon Memory.** A document uploaded to a
  Knowledge Base is a source, not a validated fact.
- **OpenWebUI conversation history ≠ Pantheon Memory.**
- **Hermes local memory ≠ Pantheon canonical memory.** Hermes operational
  state is local execution context, not Pantheon truth.

Reference: `docs/governance/KNOWLEDGE_TAXONOMY.md`.

---

## 4. Allowed Hermes memory actions

Hermes may:

- read context exports under `hermes/context/`;
- read existing `memory/` content if scoped by task contract;
- propose memory **candidates**;
- include memory impact in task outputs;
- produce an Evidence Pack documenting the candidate;
- flag contradictions between sources;
- request a promotion review.

---

## 5. Forbidden Hermes memory actions

Hermes must not:

- mutate validated project memory;
- mutate validated system memory;
- promote candidates to project or system level;
- treat its local store as Pantheon truth;
- treat OpenWebUI Knowledge as Pantheon memory;
- read undocumented internal Pantheon state unless explicitly allowed;
- mix two project memory scopes without explicit trace and approval.

---

## 6. Memory candidate — minimal payload

A memory candidate produced by Hermes should carry:

```text
candidate_id
source_layer       (session | document | observation | extraction)
source_ref         (path, document id, run id)
target_level       (project | system) — proposed only
project_id         (when applicable)
scope_candidate    (specific | reusable)
sensitivity        (public | internal | project | sensitive)
evidence_pack_id
contradiction_flags
validation_status  (always: candidate)
```

Reference: `docs/governance/MEMORY_EVENT_SCHEMA.md`.

A candidate without an Evidence Pack is not promotable. A candidate
without a clear source is not promotable. Supersession is preferred over
deletion.

---

## 7. Final rule

```text
Validation matters more than accumulation.
No evidence, no promotion.
No validation, no memory.
```
