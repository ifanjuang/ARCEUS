# OpenWebUI — context for Hermes

> Compact orientation. Source of truth: `docs/governance/OPENWEBUI_INTEGRATION.md`,
> `docs/governance/HERMES_INTEGRATION.md`,
> `docs/governance/MODEL_ROUTING_POLICY.md`.

Status: **Documented / not runtime**.

---

## 1. Role

OpenWebUI is the **user cockpit**. It exposes:

- chat;
- Knowledge Bases;
- conversations;
- results;
- approval requests;
- Evidence Pack summaries;
- user-facing actions.

OpenWebUI is **interface only**. It does not govern. It does not execute
Hermes tasks. It does not canonize memory.

---

## 2. Authority boundary

```text
OpenWebUI = presentation, interaction, validation surface.
Hermes Agent = runtime.
Pantheon Next = source of truth and authority.
```

OpenWebUI must not become:

- the business authority;
- the canonical memory layer;
- the runtime engine;
- the source of truth.

---

## 3. Connection model

OpenWebUI should connect to **Hermes Agent Gateway**, not to Pantheon API.

Target shape:

```text
OPENAI_API_BASE_URL = http://hermes_agent_gateway:8642/v1
OPENAI_API_KEY      = API_SERVER_KEY / HERMES_API_SERVER_KEY
```

Pantheon API is **not** an OpenAI-compatible model backend. Pantheon API
exposes governance and context endpoints such as:

```text
/runtime/context-pack
/domain/snapshot
/domain/approval/policy
/domain/approval/classify
/domain/task-contracts
/domain/evidence-schema
```

OpenWebUI must not point to Pantheon API as a model gateway unless a
dedicated, explicitly documented `/v1` model gateway is created later.
That is **not** the current target.

---

## 4. Workspace Models and Skills

OpenWebUI Workspace Models and OpenWebUI Skills are **operator presets and
operator tools**. They are **not** Pantheon agents and **not** Pantheon
canonical skills.

Rule:

```text
A Workspace Model preset named "ATHENA Planner" is a UI shortcut.
The actual ATHENA role is defined in docs/governance/AGENTS.md.
```

If a Workspace preset disagrees with Pantheon policy, Pantheon wins.
The preset must be updated. Reference:
`docs/governance/MODEL_ROUTING_POLICY.md` §8.

---

## 5. Knowledge surface

OpenWebUI Knowledge is a **document retrieval surface**. It is not
Pantheon memory.

A document uploaded to a Knowledge Base may be a source. It becomes
Pantheon memory only after:

```text
extraction
→ memory candidate
→ Evidence Pack
→ THEMIS / APOLLO review
→ C3 minimum
→ promotion to memory/project or memory/system
```

OpenWebUI conversation history is not Pantheon memory.

Reference: `docs/governance/OPENWEBUI_INTEGRATION.md` §4,
`docs/governance/MEMORY.md`,
`docs/governance/KNOWLEDGE_TAXONOMY.md`.

---

## 6. Approval surface

OpenWebUI may display approval requests created by Pantheon or returned by
Hermes under Pantheon policy.

Possible user actions:

- approve;
- reject;
- request clarification;
- ask for another Evidence Pack;
- ask for a rerun with stricter constraints;
- request THEMIS / APOLLO review.

OpenWebUI does not define the approval level. Approval levels live in
`docs/governance/APPROVALS.md`.

---

## 7. Evidence display

OpenWebUI may display a user-facing Evidence Pack summary with at least:

```text
task_id
task_contract_id
criticality
sources_used
files_read
tools_used
assumptions
limitations
unsupported_claims
approval_required
next_safe_action
```

The canonical Evidence Pack format lives in
`docs/governance/EVIDENCE_PACK.md`.

---

## 8. Plugins and extensions

OpenWebUI plugins and extensions are **external tools**. They are not
Pantheon skills. They are not Pantheon governance.

They must be classified before use in
`docs/governance/EXTERNAL_TOOLS_POLICY.md`.

Default rule:

```text
blocked until reviewed
```

Forbidden by default:

- batch install from GitHub;
- plugins with hidden memory write;
- plugins with shell access;
- plugins that send external messages without approval;
- plugins that bypass Evidence Packs;
- plugins that turn OpenWebUI into the runtime authority.

---

## 9. Non-goals

OpenWebUI must not implement:

- Pantheon governance;
- canonical memory promotion;
- autonomous runtime orchestration;
- uncontrolled plugin installation;
- secret access;
- direct repository mutation;
- skill activation;
- workflow activation;
- external communication without approval.

---

## 10. Final rule

```text
OpenWebUI exposes.
Hermes executes.
Pantheon canonizes.
OpenWebUI does not become any of the others.
```
