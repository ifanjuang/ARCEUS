# EXTERNAL AI OPTION REVIEWS — Pantheon Next

> Focused classification addendum for external AI runtimes and AI-configuration tools reviewed after `EXTERNAL_RUNTIME_OPTIONS.md`.

---

## 1. Purpose

This document records targeted reviews for external AI systems that do not yet deserve installation or integration, but may influence Pantheon Next governance.

It complements:

```text
docs/governance/EXTERNAL_RUNTIME_OPTIONS.md
docs/governance/EXTERNAL_TOOLS_POLICY.md
```

Core rule:

```text
OpenWebUI expose.
Hermes Agent exécute.
Pantheon Next gouverne.
```

---

## 2. Summary table

| Tool | Repository | Type | Status | Core decision | Pantheon value | Main risk | Priority |
|---|---|---|---|---|---|---|---|
| AnimoCerebro | `xunharry4-source/AnimoCerebro` | external cognitive runtime / brain | `blocked_until_reviewed` | `rejected_for_core` | precheck loop, audit trace, truthfulness boundary | autonomous cognitive runtime drift | P3 |
| Caliber AI Setup | `caliber-ai-org/ai-setup` | AI config sync / audit tool | `test_read_only` / `inspiration_for_doctor` | `rejected_for_core` | doctor/config parity, deterministic AI config scoring, multi-tool alignment | automatic mutation of governance files and learning hooks | P1/P2 |

---

## 3. AnimoCerebro classification

Classification:

```text
blocked_until_reviewed
rejected_for_core
```

Repository:

```text
https://github.com/xunharry4-source/AnimoCerebro
```

### 3.1 Pantheon fit

AnimoCerebro is relevant as an external cognitive-runtime reference, not as a Pantheon component.

Potential ideas worth studying:

```text
Nine Questions loop
allowed / forbidden action precheck
truthfulness boundary
trace_id audit trail
plugin separation language
cognitive decision log vocabulary
```

Pantheon-compatible reclassification:

| AnimoCerebro idea | Pantheon-compatible form |
|---|---|
| Nine Questions loop | Task Contract precheck checklist |
| “What am I allowed to do?” | `APPROVALS.md` + `allowed_tools` |
| “What should I not do even if I can?” | veto / `forbidden_tools` / THEMIS guardrail |
| trace_id audit trail | Evidence Pack run id / task id / tool trace |
| truthfulness boundary | unsupported claims / evidence-required rule |
| plugin separation | External Tools Policy review and sandbox model |

### 3.2 Allowed use

Allowed now:

```text
read documentation
extract governance vocabulary
compare precheck ideas with TASK_CONTRACTS.md
compare audit trail ideas with EVIDENCE_PACK.md
compare truthfulness ideas with APOLLO/THEMIS validation rules
```

### 3.3 Forbidden use

Forbidden:

```text
replace Hermes
add Pantheon cognitive runtime
enable daemon/background autonomy
enable continuous learning
enable automatic long-term memory
enable self-upgrading
connect to OpenClaw without review
connect to private project data
write Pantheon memory
mutate governance Markdown
install plugins automatically
```

### 3.4 Risk

Risk level:

```text
high
```

Reason:

```text
AnimoCerebro is positioned around autonomous cognition, memory, plugins, daemon behavior and self-improvement. Those properties directly conflict with the Pantheon Next pivot if adopted as runtime.
```

Decision:

```text
Keep as inspiration only.
Do not install.
Do not connect.
Do not treat as Pantheon or Hermes replacement.
```

---

## 4. Caliber AI Setup classification

Classification:

```text
test_read_only
inspiration_for_doctor
rejected_for_core
```

Repository:

```text
https://github.com/caliber-ai-org/ai-setup
```

### 4.1 Observed capabilities

Caliber is an AI-configuration setup and maintenance tool. It targets AI-facing repository instruction files and agent configs, including:

```text
CLAUDE.md
CALIBER_LEARNINGS.md
AGENTS.md
copilot-instructions.md
.cursor/rules/*.mdc
.claude/skills/*/SKILL.md
.cursor/skills/*/SKILL.md
.agents/skills/*/SKILL.md
.opencode/skills/*/SKILL.md
.mcp.json
.cursor/mcp.json
.claude/settings.json
```

Notable properties from the upstream documentation:

```text
Node.js >= 20
npx bootstrap flow
deterministic scoring without LLM/API calls
diff review before writes
backup and undo behavior
score comparison against a git ref
pre-commit refresh hooks
session-end refresh hooks
session learning hooks
MCP server discovery
multi-agent config parity across Claude Code, Cursor, Codex, OpenCode and Copilot
optional telemetry with opt-out
```

### 4.2 Pantheon fit

Caliber is relevant because Pantheon Next has many AI-facing configuration files that must remain synchronized with the real repository state.

Potential Pantheon value:

```text
AI config parity across Claude, Cursor, Codex, OpenCode, Copilot and Hermes context exports
checks for stale paths and obsolete references
checks for missing files referenced by governance docs
checks for drift between CLAUDE.md, AGENTS.md, README.md and docs/governance
inspiration for operations/doctor.md
inspiration for repo_md_audit and code_vs_docs_check
inspiration for config scoring without LLM calls
structured patch-candidate review flow
```

Pantheon-compatible reclassification:

| Caliber idea | Pantheon-compatible form |
|---|---|
| deterministic score | operations doctor / repo governance check |
| config freshness | `STATUS.md` / `README.md` / `CLAUDE.md` coherence check |
| multi-tool config generation | suggestion-only config candidate |
| path grounding | code/docs path existence check |
| score comparison against `main` | branch quality report |
| diff review before writes | patch candidate + approval |
| backup / undo | rollback plan requirement |
| skill generation | skill candidate only, never active directly |
| session learning | memory candidates only, never canonical memory |
| MCP discovery | external tool candidate list, never auto-install |
| pre-commit refresh | rejected for Pantheon unless explicitly approved later |

### 4.3 Allowed use

Allowed now:

```text
read documentation
study deterministic scoring
study config freshness criteria
study generated AI config formats
study path-grounding checks
study rollback and undo patterns
extract ideas for operations/doctor.md
extract ideas for repo_md_audit and code_vs_docs_check
```

Allowed later after review:

```text
run score on a sandbox branch
run read-only audit against non-sensitive repo state
generate suggestions only
produce patch candidates only
compare a branch against main for AI-context drift
```

Any future test must be:

```text
read-only or sandbox branch first
no private project data
no automatic commit
no automatic hook installation
no direct mutation of governance source of truth
Evidence Pack required
```

### 4.4 Forbidden use

Forbidden:

```text
auto-refresh hooks on main
pre-commit mutation of governance files
session-end mutation of governance files
automatic overwrite of CLAUDE.md or AGENTS.md
automatic overwrite of hermes/context exports
automatic overwrite of OpenWebUI/Cursor/Copilot configs
automatic MCP discovery / installation
automatic skill activation
community skill installation
learning hooks writing canonical memory
CALIBER_LEARNINGS.md as Pantheon source of truth
auto-commit or auto-merge
telemetry-enabled run on sensitive/private project data
API key or provider config committed to repo
```

### 4.5 Risk

Risk level:

```text
medium
```

Reason:

```text
The audit/scoring model is useful and close to Pantheon Doctor goals, but automatic refresh hooks, session learning hooks, generated configs and MCP discovery could mutate Pantheon governance files, create a parallel memory channel or expose too much environment context without C3/C4/C5 review.
```

### 4.6 Pantheon decision

Decision:

```text
Use as doctor/config-parity inspiration first.
Future testing must be read-only or sandbox-branch only.
Do not install hooks.
Do not let Caliber write canonical Pantheon files automatically.
```

Best next reuse inside Pantheon:

```text
operations/doctor.md
future read-only doctor report
repo_md_audit skill candidate
code_vs_docs_check skill candidate
AI-context drift check
Hermes context export freshness check
```

---

## 5. Approval policy

| Action | Approval |
|---|---:|
| Read repository/docs | C0 |
| Add classification entry | C1/C3 depending persistence |
| Run Caliber score read-only on sandbox branch | C2 |
| Run Caliber score read-only on Pantheon repo | C2/C3 |
| Generate patch candidates for AI configs | C3 |
| Modify `CLAUDE.md`, `AGENTS.md`, `.cursor`, `.github` configs | C3 |
| Modify `hermes/context/*` exports | C3 |
| Enable hooks that mutate files | C4/C5 |
| Enable learning hooks | C4/C5 |
| Enable MCP auto-discovery / install | C5 |
| Install plugin/runtime or connect private data | C4/C5 |
| Enable autonomous learning or self-upgrade | C5 / blocked |

---

## 6. Recommended follow-up

Recommended next document:

```text
operations/doctor.md
```

It should include checks inspired by Caliber, but implemented under Pantheon governance:

```text
critical Markdown files exist
paths referenced by governance docs exist
forbidden legacy paths are absent or classified
OpenWebUI mapping files exist
model routing config exists
Hermes context exports exist and match governance docs
context pack endpoint is tested
AI-facing config files are not stale
no secret-like values are committed
no automatic hooks are enabled without policy
no MCP config appears without policy
```

---

## 7. Final rule

```text
AnimoCerebro may inspire precheck/audit language.
Caliber may inspire doctor/config-parity checks.
Neither becomes Pantheon authority.
```
