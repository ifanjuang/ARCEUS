# Pantheon Next — operating context for Hermes

> Compact orientation. Source of truth: `docs/governance/ARCHITECTURE.md`,
> `docs/governance/HERMES_INTEGRATION.md`, `docs/governance/OPENWEBUI_INTEGRATION.md`.

Status: **Documented / not runtime**.

---

## 1. Triptych

```text
OpenWebUI expose.
Hermes Agent exécute.
Pantheon Next gouverne.
```

| Layer | Role | Authority |
|---|---|---|
| OpenWebUI | User cockpit, chat, Knowledge surface, approval surface | Interface only. Does not canonize. |
| Hermes Agent | Operational worker, executable skills, tools, local execution | Runtime only. Does not canonize. |
| Pantheon Next | Governed Domain Operating Layer, source-of-truth Markdown, policies, candidates | Final authority. |

Short rule:

```text
Hermes proposes.
Pantheon canonizes.
OpenWebUI displays.
```

---

## 2. What Pantheon provides to Hermes

Pantheon supplies, through this `hermes/context/` export and through the
Markdown under `docs/governance/`:

- domain definitions (`general`, `architecture_fr`, `software`);
- abstract agent roles;
- task contracts;
- approval policy (C0-C5);
- evidence requirements;
- memory policy and promotion cycle;
- knowledge taxonomy and source tiers;
- external tools policy and allowlist principle;
- model routing policy (capability labels and fallback rules);
- candidate skill / workflow lifecycle;
- legacy classification rules.

Hermes consumes these to execute safely.

---

## 3. What Pantheon forbids

Pantheon Next does not authorize Hermes to:

- push to `main`;
- modify Markdown source-of-truth files without review;
- canonize memory;
- promote a candidate skill to active without review;
- activate or change a workflow without review;
- bypass `APPROVALS.md`;
- bypass THEMIS / APOLLO when their review is required;
- send external communications without C4 approval;
- access secrets by default;
- access the Docker socket by default;
- install plugins outside the allowlist;
- batch-install skills, plugins or tools;
- treat OpenWebUI Knowledge as Pantheon memory;
- treat Hermes local memory as Pantheon canonical memory;
- run high-risk fallbacks silently;
- self-evolve actively (only candidate proposals).

---

## 4. What Pantheon must not become

Pantheon Next must not silently re-create:

```text
Execution Engine
Agent Runtime
Tool Runtime
LLM Provider Router
Scheduler
LangGraph central orchestrator
memory auto-promotion
self-evolution auto-merge
plugin batch install
public admin dashboard
```

These responsibilities stay on the Hermes side and remain framed by Pantheon
policy. Hermes runtime authority is bounded by task contracts, approval
levels, evidence requirements and tools policy.

---

## 5. How Hermes should use this context

For every task:

1. read the relevant `hermes/context/*.md` exports;
2. confirm the task contract (or request one);
3. classify the action against `APPROVALS.md` (C0-C5);
4. respect the tools policy and the allowlist;
5. produce an Evidence Pack for any consequential output;
6. return outputs as **candidates**, not as canonical Pantheon truth;
7. surface approval requests through OpenWebUI when required.

Default posture if anything is unclear:

```text
Stop. Ask. Do not escalate silently.
```
