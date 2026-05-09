# DEVELOPMENT PHASES — Pantheon Next

> Companion document for `ROADMAP.md`.
>
> This file gives the roadmap a phase-based development reading without replacing the detailed roadmap.

Last update: 2026-05-09

---

## 1. Purpose

`ROADMAP.md` remains the detailed roadmap.

`DEVELOPMENT_PHASES.md` is a navigation layer that explains the recommended order of development.

The purpose is to avoid turning the roadmap into an unprioritized list of topics.

Canonical doctrine remains:

```text
OpenWebUI expose.
Hermes Agent exécute.
Pantheon Next gouverne.
```

No phase below creates a Pantheon runtime.

---

## 2. Phase overview

| Phase | Theme | Status | Main references |
|---|---|---|---|
| P0 | Doctrine and source of truth | Mostly documented | `README.md`, `ARCHITECTURE.md`, `STATUS.md`, `ROADMAP.md` |
| P1 | Request framing and orchestration | Candidate branch | `AGENTS.md`, pending `REQUEST_ORCHESTRATION.md` |
| P2 | Visibility and run observation | Candidate branch | pending `RUN_GRAPH.md`, pending Inline Run Stream docs |
| P3 | OpenWebUI / Hermes controlled integration | Partially documented | `HERMES_INTEGRATION.md`, `OPENWEBUI_INTEGRATION.md` |
| P4 | Domain skills and workflows | Started | `domains/general`, `domains/architecture_fr` |
| P5 | Governance API and observable state | Partial | `platform/api/pantheon_domain`, `platform/api/pantheon_runtime` |
| P6 | Evaluation and quality gates | Planned | future `EVALUATION.md` |
| P7 | Operations and controlled deployment | Partially documented | `operations/doctor.md`, OpenWebUI/Hermes operations docs |
| P8 | Optional advanced capabilities | Watch / later | external option reviews |

---

## 3. P0 — Doctrine and source of truth

Objective:

```text
Keep the authority model stable and documented.
```

Current state:

```text
mostly documented
code partially aligned
legacy runtime still requires audit
```

Main work:

```text
maintain governance docs
avoid runtime drift
complete code audit post-pivot
keep ai_logs discipline
keep README and STATUS aligned
```

Activation criteria:

```text
all critical docs agree
no hidden runtime expansion
all major interventions logged
```

---

## 4. P1 — Request framing and orchestration

Objective:

```text
Before answering, Pantheon classifies the request, understands intent, detects implicit needs and chooses the right response strategy.
```

Target concepts:

```text
METIS request framing
request_classification
request_intent_enrichment
context_scope_expansion
brief_adherence_review
agent_revision_request
variant_generation
agent_forum_review
AGORA consultation mode
decision_arbitration
ZEUS arbitration
```

Status:

```text
candidate documentation branch exists
not active on main unless merged
```

Branch:

```text
work/chatgpt/metis-agora-governance
```

Non-goals:

```text
no autonomous agent forum
no majority vote authority
no hidden chain-of-thought
no workflow execution
no memory promotion
```

---

## 5. P2 — Visibility and run observation

Objective:

```text
Show task progress clearly without exposing private reasoning or creating a Pantheon runtime.
```

Target concepts:

```text
Run Graph
Inline Run Stream V1
workflow_live_narrator
OpenWebUI temporary status display
warnings / vetoes / approvals visibility
```

Status:

```text
candidate documentation branch exists
not active on main unless merged
```

Branch:

```text
work/chatgpt/inline-run-stream-v1
```

V1 posture:

```text
plain text
non-technical
no emoji
no D3
no live panel
no raw chain-of-thought
no sensitive data
```

---

## 6. P3 — OpenWebUI / Hermes controlled integration

Objective:

```text
Expose Hermes-backed work through OpenWebUI while Pantheon supplies context, rules, task contracts, approvals and Evidence Pack expectations.
```

Main work:

```text
OpenWebUI Router Pipe specification
OpenWebUI Actions specification
Evidence Pack summary display
approval display
Hermes context-pack consumption verification
Hermes retrieval preflight using knowledge_selection
```

Non-goals:

```text
OpenWebUI as runtime
OpenWebUI as memory authority
Pantheon API as model backend
Pipe as orchestrator
Function with broad filesystem or secret access
```

---

## 7. P4 — Domain skills and workflows

Objective:

```text
Build useful professional capabilities as candidate skills and workflow templates before activation.
```

Current candidates:

```text
domains/general/skills/adaptive_orchestration/
domains/general/skills/project_context_resolution/
domains/general/skills/knowledge_selection/
domains/architecture_fr/skills/quote_vs_cctp_consistency/
domains/architecture_fr/workflows/quote_vs_cctp_review/
```

Priority next candidates:

```text
dpgf_quantity_sanity_check
client_message_safety
cctp_review
plu_constraint_check
erp_sdis_check
repo_md_audit
code_audit_post_pivot
```

Activation criteria:

```text
candidate package complete
examples and tests present
privacy reviewed
Evidence Pack requirements explicit
Hermes mapping reviewed
human approval before active state
```

---

## 8. P5 — Governance API and observable state

Objective:

```text
Expose read-only governance state without creating execution endpoints.
```

Existing or expected read endpoints:

```text
GET /health
GET /runtime/context-pack
GET /domain/health
GET /domain/snapshot
GET /domain/agents
GET /domain/skills
GET /domain/workflows
GET /domain/memory
GET /domain/knowledge
GET /domain/legacy
GET /domain/approval/classify
```

Forbidden for now:

```text
POST /agents/run
POST /runtime/execute
POST /workflow/run
POST /tools/install
POST /plugins/install
POST /memory/promote/auto
POST /scheduler/create
```

---

## 9. P6 — Evaluation and quality gates

Objective:

```text
Measure output quality without making evaluation tools authoritative.
```

Possible future checks:

```text
Evidence Pack completeness
source quality
unsupported claim count
limitation clarity
approval correctness
brief adherence
request classification correctness
context expansion correctness
workflow adaptation trace correctness
```

Rule:

```text
Evaluation may measure.
It must not canonize, approve, promote or activate.
```

---

## 10. P7 — Operations and controlled deployment

Objective:

```text
Make the system installable, diagnosable, backed up and testable without hidden automation.
```

Existing docs:

```text
operations/openwebui_hermes_pantheon.md
operations/openwebui_manual_setup.md
operations/doctor.md
operations/n8n_email_automation.md
operations/n8n_workflows/email_received_operator_notification.md
```

Target docs:

```text
operations/install.md
operations/update.md
operations/backup.md
operations/hermes_lab.md
operations/openwebui_knowledge.md
operations/domain_api.md
operations/n8n_portainer_sandbox.md
```

Rule:

```text
Doctor observes and reports only.
n8n may detect and notify only.
No Docker socket or secrets by default.
```

---

## 11. P8 — Optional advanced capabilities

Objective:

```text
Explore advanced options only after P0-P7 are stable.
```

Examples:

```text
LangGraph as Hermes-side execution library only
Langflow as lab / visual editing only
Promptfoo evaluation suite
Instructor / Outlines structured output adapters
D3 Run Panel after text stream validation
external memory/runtime options as watch-only unless reclassified
```

Forbidden drift:

```text
external runtime becoming Pantheon
external memory becoming Pantheon Memory
LangGraph central Pantheon orchestrator
Langflow canonical workflow editor
D3 live panel before V1 text stream validation
```

---

## 12. Merge order recommendation

Recommended order for pending documentation branches:

```text
1. work/chatgpt/roadmap-dev-phases
2. work/chatgpt/metis-agora-governance
3. work/chatgpt/inline-run-stream-v1
```

Reason:

```text
First clarify the development map.
Then add request orchestration.
Then add execution visibility.
```

---

## 13. Final rule

```text
Phase the work.
Keep detailed doctrine intact.
Do not replace governance with execution.
```
