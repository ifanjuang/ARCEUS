# Tools policy — context for Hermes

> Compact orientation. Source of truth: `docs/governance/EXTERNAL_TOOLS_POLICY.md`,
> `docs/governance/APPROVALS.md`,
> `docs/governance/TASK_CONTRACTS.md`,
> `docs/governance/MODEL_ROUTING_POLICY.md`.

Status: **Documented / not runtime**.

---

## 1. Default posture

```text
Unknown tools are blocked until reviewed.
External tools are capabilities, not authorities.
```

Default classification for any unknown tool:

```yaml
status: blocked
approval_level: C5
sandbox_required: true
secrets_access: forbidden
shell_access: forbidden
memory_access: none
network_exposure: none
```

A blocked tool may be reconsidered only through explicit review and an
update to `docs/governance/EXTERNAL_TOOLS_POLICY.md`.

---

## 2. Allowed status values

```text
allowed   → may be used inside policy and task contract
test      → sandbox only, no production use
blocked   → blocked by default, only revisitable through review
rejected  → rejected for Pantheon use
watch     → tracked as inspiration / future candidate, no execution
```

Reference: `docs/governance/EXTERNAL_TOOLS_POLICY.md` §5.

---

## 3. C-level mapping (summary)

| Action | Default level |
|---|---:|
| read file | C0 |
| search files | C0 |
| web search / extract | C0 / C1 |
| draft response / report | C1 |
| reversible local action | C2 |
| write file / patch candidate | C3 |
| safe diagnostic shell | C3 |
| local service install | C3 |
| OpenWebUI plugin install (one-by-one) | C3 |
| Hermes plugin install | C3 / C5 depending on capability |
| MCP server install | C3 / C4 |
| memory plugin install | C4 |
| external communication / web side effect | C4 |
| destructive shell / overwrite / force | C5 |
| secret access | C5 |
| Docker socket | C5 |
| batch plugin install | C5 / blocked |
| remote MCP server | C5 / blocked until audited |

Reference: `docs/governance/APPROVALS.md` §3-§5,
`docs/governance/EXTERNAL_TOOLS_POLICY.md` §7.

---

## 4. Forbidden by default

The following are forbidden by default and require an explicit policy
gate before any use:

- shell access for destructive or privileged operations;
- secret or credential access;
- Docker socket access;
- privileged volume mounts;
- public exposure of admin dashboards;
- batch installation of plugins from a remote source;
- self-evolution that mutates active skills, workflows or policies;
- runtime authority frameworks that would replace Pantheon governance;
- remote MCP servers that are not audited;
- direct repository mutation outside an approved task contract.

---

## 5. Already-classified tools

The following tools already have an entry in
`docs/governance/EXTERNAL_TOOLS_POLICY.md`. Hermes must follow the entry,
not a memory of past behavior:

```text
Stirling-PDF
OpenWebUI extensions
Hermes plugins
AgentScope
Hermes self-evolution
BrainAPI2
GBrain
Cycles / runcycles
Omnigraph
SearXNG (referenced in OPENWEBUI_INTEGRATION.md)
```

When a tool listed above is involved, the canonical policy entry wins.
Re-read it before each use.

---

## 6. Not yet integrated

The following tools are **not integrated** into Pantheon Next unless and
until a documented classification exists in
`docs/governance/EXTERNAL_TOOLS_POLICY.md`:

```text
RAGFlow
AKS
AgentRQ
Kanwas
Thoth
kontext-brain-ts
opencode-loop
six-hats-skill
```

Default status for these tools:

```yaml
status: blocked
approval_level: C5
default_decision: documentation_review_only
```

Hermes must not call them, install them, sandbox them or treat them as
authority. If a task seems to require one, the right move is to request
a policy entry through the normal contribution flow, not to use the
tool.

---

## 7. Fallback rule

A fallback cannot replace a blocked path with an unreviewed path. Allowed
fallback only if:

- intent is unchanged;
- tool stays allowlisted;
- risk is equal or lower;
- data exposure does not increase silently;
- Evidence Pack records the substitution.

Forbidden fallback regardless of context:

```text
unallowlisted tool
destructive action
external send
secret access
Docker socket
memory write
plugin installation
batch install
remote MCP server not audited
```

---

## 8. Pre-flight checklist before using any external tool

1. Locate the tool entry in `docs/governance/EXTERNAL_TOOLS_POLICY.md`.
2. Confirm `status` allows the intended use.
3. Confirm `approval_level` matches the task contract.
4. Confirm `allowed_usage` covers the action.
5. Confirm `forbidden_usage` does not block the action.
6. Confirm sandbox / network / secrets / shell constraints.
7. Confirm rollback is defined.
8. Record the use in the Evidence Pack.

If any step fails, **do not run the tool**.

---

## 9. Final rule

```text
Capabilities, not authorities.
Allowlist, not improvisation.
Policy, contract, evidence, rollback.
```
