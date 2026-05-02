# Hermes context exports — Pantheon Next

> Compact, read-only Markdown exports of Pantheon Next governance, intended
> for Hermes Agent to load as orientation context.

Status: **Documented / not runtime**.

---

## 1. Purpose

These files are **operational orientation exports**. They give Hermes a short,
actionable view of the rules, agents, memory model, tools policy and domain
boundaries it must respect when executing tasks under Pantheon Next.

Canonical formula:

```text
OpenWebUI expose.
Hermes Agent exécute.
Pantheon Next gouverne.
```

---

## 2. What these exports are not

These files are **not**:

- a Pantheon source of truth;
- a canonical memory store;
- a Pantheon runtime configuration;
- an authorization for Hermes to mutate Pantheon governance;
- an authorization for Hermes to push to `main`;
- an authorization for Hermes to install tools, plugins or skills;
- a substitute for `APPROVALS.md`, `TASK_CONTRACTS.md`, `EVIDENCE_PACK.md`,
  `MEMORY.md`, `HERMES_INTEGRATION.md`, `OPENWEBUI_INTEGRATION.md`,
  `EXTERNAL_TOOLS_POLICY.md`, `MODEL_ROUTING_POLICY.md`,
  `KNOWLEDGE_TAXONOMY.md`, `AGENTS.md`, `MODULES.md` or `ARCHITECTURE.md`.

If an export disagrees with the canonical Markdown under
`docs/governance/`, the canonical Markdown wins. The export is then stale and
must be updated through a normal documentation change.

---

## 3. Source of truth

The source of truth lives in:

```text
docs/governance/
```

These exports are derived. They do not replace those files. They do not give
Hermes the right to modify those files. Hermes may propose **patch
candidates** to those files through the normal Pantheon Next contribution
flow (branch + AI log entry + review).

---

## 4. File index

| File | Role |
|---|---|
| `README.md` | This index. Explains purpose and limits of the exports. |
| `pantheon_context.md` | Authority triptych, what Pantheon provides to Hermes, what Pantheon forbids. |
| `agents_context.md` | Pantheon agents as abstract reasoning roles, not autonomous workers. |
| `rules_context.md` | Transversal rules Hermes must apply on every task. |
| `memory_context.md` | Memory levels, candidate cycle, Knowledge ≠ Memory boundary. |
| `tools_policy.md` | External tools posture, allowlist principle, C-level mapping. |
| `openwebui_context.md` | OpenWebUI cockpit role and non-authority status. |
| `architecture_fr_context.md` | French architecture domain rules and contractual posture. |
| `software_context.md` | Software audit/refactor domain rules and legacy classification. |

---

## 5. Update rule

When a canonical document under `docs/governance/` is changed, the
corresponding export here may need to be refreshed. Refresh is a
**documentation change** like any other:

```text
branch → edit → AI log entry → review → merge
```

Hermes must not silently rewrite these exports. Hermes may propose updates
as patch candidates.

---

## 6. Privacy

These exports must contain **no real project data**, **no client data**,
**no personal data**, **no addresses**, **no construction site**, **no
identifiable engagement**. Examples must remain fictional, neutral and
non-traceable.
