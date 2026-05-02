# Pantheon Doctor — Operations Checklist

> Read-only operational checklist for checking Pantheon Next repository coherence before refactor, deployment or external-tool testing.

This document is inspired by AI configuration scoring and path-grounding patterns, but it remains Pantheon-governed.

It does not install Caliber, AnimoCerebro, Symphony, Graphify, CTX, Langflow or any other external tool.

---

## 1. Purpose

Pantheon Doctor is a manual or future-scriptable checklist.

Its role is to verify that the repository still follows the active operating model:

```text
OpenWebUI expose.
Hermes Agent exécute.
Pantheon Next gouverne.
```

The doctor may report:

```text
PASS
WARN
FAIL
NOT_APPLICABLE
TO_VERIFY
```

It must not automatically fix anything.

---

## 2. Authority and approval level

Default mode:

```text
C0 read-only diagnostic
```

Allowed:

```text
read files
list paths
check text references
check file existence
run safe local read-only commands
call local health endpoints if already running
produce a report
```

Forbidden:

```text
create files automatically
modify files automatically
install dependencies
run migrations
start containers
stop containers
read secrets
print secrets
push branches
merge PRs
call external services
mutate OpenWebUI
mutate Hermes
promote memory
activate skills
```

Any remediation must become a separate C3 patch candidate.

---

## 3. Output format

Doctor output should use this table:

| Check | Status | Evidence | Risk | Next action |
|---|---|---|---|---|
| governance_docs_exist | PASS | paths found | low | none |
| forbidden_paths_absent | WARN | `domains/architecture` found | medium | classify or rename |

Each `FAIL` must include:

```text
file or path involved
expected state
actual state
risk
recommended next action
approval level for fix
```

---

## 4. Baseline checks

### 4.1 Root entry points

Required:

```text
README.md
CLAUDE.md
CHANGELOG.md
VERSION
```

Expected:

```text
README.md uses Pantheon Next naming.
README.md references the OpenWebUI / Hermes / Pantheon split.
CLAUDE.md is aligned with Pantheon Next governance.
VERSION exists and is readable.
```

Failure mode:

```text
WARN if optional entry is missing.
FAIL if README.md is missing.
```

---

### 4.2 AI logs

Required:

```text
ai_logs/README.md
```

Expected:

```text
One intervention = one dated log file.
No direct main mutation is documented as allowed.
No private client/project data is written into logs.
```

Doctor should verify recent log naming:

```text
ai_logs/YYYY-MM-DD-slug.md
```

Failure mode:

```text
WARN if logs exist but naming is inconsistent.
FAIL if ai_logs/README.md is missing.
```

---

### 4.3 Governance docs

Required under `docs/governance/`:

```text
README.md
STATUS.md
ROADMAP.md
ARCHITECTURE.md
MODULES.md
AGENTS.md
MEMORY.md
APPROVALS.md
TASK_CONTRACTS.md
EVIDENCE_PACK.md
HERMES_INTEGRATION.md
OPENWEBUI_INTEGRATION.md
OPENWEBUI_DOMAIN_MAPPING.md
MODEL_ROUTING_POLICY.md
EXTERNAL_TOOLS_POLICY.md
EXTERNAL_RUNTIME_OPTIONS.md
EXTERNAL_AI_OPTION_REVIEWS.md
KNOWLEDGE_TAXONOMY.md
CODE_AUDIT_POST_PIVOT.md
WORKFLOW_SCHEMA.md
SKILL_LIFECYCLE.md
MEMORY_EVENT_SCHEMA.md
VERSIONS.md
```

Expected:

```text
docs/governance/README.md indexes every required governance document.
STATUS.md matches current completed documents.
ROADMAP.md does not resurrect Pantheon autonomous runtime.
ARCHITECTURE.md states that Pantheon governs and Hermes executes.
```

Failure mode:

```text
FAIL if a required governance document is missing.
WARN if it exists but is not indexed.
WARN if status/roadmap appear stale.
```

---

## 5. Forbidden drift checks

Doctor must detect these forbidden or suspicious paths:

```text
domains/architecture
skills/generic
workflows/generic
memory/agency
```

Expected canonical replacements:

```text
domains/architecture_fr
domains/general/skills
domains/general/workflows
memory/system
```

Failure mode:

```text
WARN if forbidden path exists and is classified as legacy.
FAIL if forbidden path exists and is unclassified.
```

Doctor must also detect risky terminology in active governance docs:

```text
Pantheon runtime
Execution Engine
Agent Runtime
Tool Runtime
LLM Provider Router
scheduler
memory auto-promotion
self-evolution auto-merge
```

Interpretation:

```text
PASS if terms appear only in forbidden-drift, rejection, legacy or external runtime sections.
WARN if terms appear ambiguously.
FAIL if terms are described as active Pantheon target architecture.
```

---

## 6. Domain checks

Required canonical domain folders:

```text
domains/general
domains/architecture_fr
domains/software
```

Expected minimum files per domain:

```text
domain.md
rules.md
knowledge_policy.md
output_formats.md
```

Expected optional folders:

```text
skills/
workflows/
templates/
```

Failure mode:

```text
PASS if folder and minimum files exist.
WARN if folder exists but minimum files are incomplete.
TO_VERIFY if STATUS.md marks the domain as targeted but not started.
FAIL if docs claim the domain is active but folder is missing.
```

---

## 7. Skill and workflow checks

Candidate skills must follow:

```text
domains/{domain}/skills/{skill_id}/SKILL.md
domains/{domain}/skills/{skill_id}/manifest.yaml
domains/{domain}/skills/{skill_id}/examples.md
domains/{domain}/skills/{skill_id}/tests.md
domains/{domain}/skills/{skill_id}/UPDATES.md
```

Expected candidate skills currently referenced by STATUS:

```text
domains/general/skills/adaptive_orchestration/
domains/general/skills/project_context_resolution/
```

Doctor should verify:

```text
manifest exists
status is draft/candidate/active/deprecated/rejected
approval level is declared
memory impact is declared
Hermes mapping is explicit or null
```

Failure mode:

```text
WARN if candidate skill folder is incomplete.
FAIL if a skill is marked active without lifecycle evidence.
```

---

## 8. OpenWebUI checks

Required docs/config:

```text
docs/governance/OPENWEBUI_INTEGRATION.md
docs/governance/OPENWEBUI_DOMAIN_MAPPING.md
operations/openwebui_manual_setup.md
config/openwebui_domain_mapping.example.yaml
```

Expected rules:

```text
OpenWebUI is cockpit only.
OpenWebUI Knowledge is not Pantheon memory.
OpenWebUI Workspace Models are presets, not Pantheon agents.
OpenWebUI Skills are operator aids, not active Pantheon skills.
OpenWebUI must point to Hermes Gateway, not Pantheon API, unless a compliant model gateway is explicitly added later.
```

Failure mode:

```text
FAIL if docs instruct OpenWebUI to point directly to Pantheon API as OpenAI-compatible backend.
WARN if Knowledge Base names are used without source tier or privacy level.
```

---

## 9. Model routing checks

Required:

```text
docs/governance/MODEL_ROUTING_POLICY.md
config/model_routing.example.yaml
```

Expected:

```text
single_ollama_instance mode documented
multi_ollama_instance mode documented
fallback C0-C5 documented
agent-role model preferences documented
Evidence Pack trace for model substitution documented
```

Forbidden:

```text
Pantheon LLM Provider Router as active component
silent fallback for C4/C5
remote model use for private data without policy
```

Failure mode:

```text
WARN if config exists but lacks fallback policy.
FAIL if Pantheon is described as active LLM provider router.
```

---

## 10. Hermes checks

Required docs/templates:

```text
docs/governance/HERMES_INTEGRATION.md
hermes/templates/pantheon-os/
```

Expected API/context paths:

```text
GET /runtime/context-pack
GET /domain/snapshot
GET /domain/approval/classify
```

Expected rules:

```text
Hermes executes.
Pantheon provides Task Contract, Context Pack, policies and Evidence requirements.
Hermes outputs remain candidates until approved.
Hermes does not canonize memory.
Hermes does not mutate governance Markdown without approval.
```

Failure mode:

```text
WARN if Hermes template exists but is not installed locally.
FAIL if docs allow Hermes to bypass approvals.
```

---

## 11. API checks

If the Pantheon API is running locally, safe checks may include:

```text
GET /health
GET /runtime/context-pack
GET /domain/snapshot
GET /domain/agents
GET /domain/skills
GET /domain/workflows
GET /domain/memory
GET /domain/knowledge
GET /domain/legacy
GET /domain/approval/classify
```

Rules:

```text
read-only requests only
no POST except documented classify endpoint if test payload is non-sensitive
no secrets
no external network dependency
no mutation
```

Failure mode:

```text
NOT_APPLICABLE if API is not running.
WARN if endpoint exists but returns stale/static data.
FAIL if endpoint mutates state unexpectedly.
```

---

## 12. External tool and runtime checks

Required:

```text
docs/governance/EXTERNAL_TOOLS_POLICY.md
docs/governance/EXTERNAL_RUNTIME_OPTIONS.md
docs/governance/EXTERNAL_AI_OPTION_REVIEWS.md
```

Expected classifications include:

```text
Stirling-PDF
OpenWebUI extensions
Hermes plugins
Cycles / runcycles
Omnigraph
LangChain / LangGraph
Langflow
OpenClaw
OpenAI Symphony
Graphify
Layer Infinite / Layer
CTX
Binderly
NeverWrite
AnimoCerebro
Caliber / ai-setup
```

Expected rules:

```text
unknown tools are blocked until classified
external runtimes may assist Pantheon but must not become Pantheon
Caliber is test_read_only / rejected_for_core
AnimoCerebro is blocked_until_reviewed / rejected_for_core
```

Failure mode:

```text
WARN if a discussed tool lacks classification.
FAIL if an external tool is installed or configured without policy entry.
```

---

## 13. Knowledge checks

Required or planned:

```text
docs/governance/KNOWLEDGE_TAXONOMY.md
config/openwebui_domain_mapping.example.yaml
operations/openwebui_manual_setup.md
```

Planned but not necessarily present yet:

```text
knowledge/registry.yaml
```

Expected:

```text
Knowledge and Memory are separated.
OpenWebUI Knowledge is source material.
Pantheon Memory requires candidate → Evidence Pack → validation.
Project-private Knowledge is not mixed across projects.
```

Failure mode:

```text
WARN if Knowledge Registry is missing while still marked planned.
FAIL if documents say Knowledge Base equals canonical memory.
```

---

## 14. Memory checks

Required:

```text
docs/governance/MEMORY.md
docs/governance/MEMORY_EVENT_SCHEMA.md
```

Expected canonical memory folders:

```text
memory/session
memory/candidates
memory/project
memory/system
```

Expected rules:

```text
no automatic promotion
memory promotion is C3 minimum
Evidence Pack required
system memory replaces agency memory
Hermes local memory is not canonical
OpenWebUI history is not canonical
```

Failure mode:

```text
WARN if folders are missing but memory runtime is not implemented yet.
FAIL if docs describe automatic promotion as active policy.
```

---

## 15. Security and secrets checks

Doctor must never print secret values.

It may report only:

```text
secret-like pattern detected
file path
line number if safe
redacted key name
```

Patterns to flag:

```text
OPENAI_API_KEY=
ANTHROPIC_API_KEY=
GITHUB_TOKEN=
HERMES_API_SERVER_KEY=
API_SERVER_KEY=
password=
secret=
token=
private_key
BEGIN RSA PRIVATE KEY
BEGIN OPENSSH PRIVATE KEY
```

Allowed files for placeholders:

```text
.env.example
*.example.yaml
```

Failure mode:

```text
WARN if placeholder appears in example file.
FAIL if plausible real secret appears in tracked non-example file.
```

---

## 16. Docker / deployment checks

Doctor may inspect Docker files only.

It must not run containers.

Check for:

```text
docker-compose.yml
infra/compose/
.env.example
operations/install.md
operations/openwebui_manual_setup.md
```

Expected rules:

```text
OpenWebUI points to Hermes Gateway, not Pantheon API as /v1 backend.
Postgres OpenWebUI and Postgres Pantheon remain separated if both are used.
No Docker socket mounted into Hermes Lab.
No public Hermes Dashboard without auth/VPN.
No latest tag for critical storage services if avoidable.
```

Failure mode:

```text
WARN if compose docs are incomplete.
FAIL if Docker socket is mounted into Hermes or if secrets are hardcoded.
```

---

## 17. Suggested local commands

These are examples for a future manual run.

They are read-only.

```bash
find docs/governance -maxdepth 1 -type f -name "*.md" | sort
find ai_logs -maxdepth 1 -type f -name "*.md" | sort
find domains -maxdepth 3 -type f | sort
find operations -maxdepth 2 -type f | sort
```

Potential grep checks:

```bash
grep -R "domains/architecture\|skills/generic\|workflows/generic\|memory/agency" -n . --exclude-dir=.git
grep -R "OPENAI_API_KEY=\|GITHUB_TOKEN=\|private_key\|BEGIN RSA PRIVATE KEY" -n . --exclude-dir=.git
```

Rules:

```text
Do not paste secret values into reports.
Redact any suspicious value.
```

---

## 18. Doctor report template

```md
# Pantheon Doctor Report — YYYY-MM-DD

Branch / ref: `<ref>`
Mode: C0 read-only
Operator: `<name>`

## Summary

| Category | Status | Notes |
|---|---|---|
| Governance docs | PASS | |
| AI logs | PASS | |
| Domains | WARN | |
| Skills | WARN | |
| OpenWebUI | PASS | |
| Hermes | WARN | |
| External tools | PASS | |
| Secrets | PASS | |
| Docker | TO_VERIFY | |

## Findings

| Check | Status | Evidence | Risk | Next action |
|---|---|---|---|---|

## Required approvals before fix

| Finding | Approval |
|---|---|

## Evidence Pack references

- files read:
- commands run:
- assumptions:
- limitations:
```

---

## 19. Future automation boundary

A future script may be added only if it remains:

```text
read-only by default
no network by default
no secret printing
no automatic fix
no commit
no push
no dependency install
```

Potential path:

```text
operations/doctor.py
```

Approval before adding script:

```text
C3
```

---

## 20. Final rule

```text
Doctor observes and reports.
Doctor does not repair.
```
