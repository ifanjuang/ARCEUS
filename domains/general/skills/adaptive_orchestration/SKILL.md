# Adaptive Orchestration

> Candidate Pantheon skill. Defines how ZEUS selects, adapts, simplifies, switches, composes or extends workflows before and during execution.
>
> Reference doctrine: `docs/governance/WORKFLOW_ADAPTATION.md`.

---

# 1. Purpose

`adaptive_orchestration` prevents Pantheon from executing workflows mechanically.

Before a workflow starts, it checks whether the selected workflow fits the user request and the available context.

During execution, it checks whether the workflow still fits the evolving role outputs, evidence, dependency graph and risk level.

After execution, it may propose candidate improvements when a reusable pattern appears.

This skill governs **session workflow adaptation**, not canonical workflow mutation.

---

# 2. Core rule

```text
Before execution: select, adapt, compose or generate.
During execution: reevaluate, pause, revise or resume.
After execution: propose candidate improvement when useful.
```

Canonical split:

```text
ATHENA agence les workflows.
HEPHAISTOS forge les skills.
CHRONOS règle les dépendances.
ZEUS arbitre les options.
THEMIS bloque.
APOLLO valide.
Hermes exécute.
```

---

# 3. Responsibilities

This skill may propose to:

- use an existing workflow as-is;
- adapt an existing workflow;
- compose a workflow from several patterns;
- generate a session workflow from scratch;
- add an agent/role block;
- remove an unnecessary role block;
- add a step;
- skip a step;
- insert a subworkflow;
- switch to another workflow;
- expand context;
- ask specific roles for consultation;
- ask the user only if uncertainty remains;
- propose a candidate workflow;
- propose a candidate skill or workflow update;
- emit or process a `workflow_revision_signal`;
- propose a `workflow_patch`;
- propose a `task_contract_revision`;
- define a `resume_policy`;
- reset a session workflow to a baseline template.

---

# 4. Non-responsibilities

This skill must not:

- create a canonical workflow automatically;
- permanently modify a workflow without validation;
- promote memory automatically;
- upgrade a skill level automatically;
- activate a skill automatically;
- expose raw chain-of-thought;
- perform risky external actions without approval;
- silently change the user’s intended output;
- bypass THEMIS veto;
- bypass APOLLO final gate;
- lower approval level silently;
- authorize unclassified tools;
- turn Pantheon into a runtime.

---

# 5. Preflight phase

Before using a workflow, ZEUS must run a preflight check.

The preflight checks:

```text
intent_match
context_match
risk_level
missing_information
available_workflow_templates
required_roles
unnecessary_roles
memory_need
knowledge_need
user_validation_need
external_tool_need
```

Possible decisions:

```text
use_as_is
adapt_existing
compose_from_patterns
generate_session_workflow
insert_subworkflow
switch_workflow
ask_roles
expand_context
ask_user
propose_candidate_workflow
```

---

# 6. Role consultation phase

ZEUS may consult roles before execution or after a revision signal.

Expected structured outputs include:

```text
role_need_statement
workflow_option
workflow_revision_signal
workflow_patch_candidate
```

Roles and expected contributions:

| Role | Contribution |
|---|---|
| ARGOS | source/input needs, facts available, missing material |
| ATHENA | workflow arrangement, step composition, strategy |
| CHRONOS | dependencies, parallel groups, joins, waits, resume points |
| HEPHAISTOS | missing skills, weak methods, robustness gaps |
| PROMETHEUS | alternatives, variants, counter-paths |
| HECATE | ambiguity, uncertainty and hidden risks |
| THEMIS | approval level, forbidden transitions, vetoes |
| APOLLO | evidence feasibility, quality gate requirements |
| IRIS | output form and communication constraints |

No raw chain-of-thought is emitted.

---

# 7. Dependency graph phase

Pantheon workflows are dependency graphs, not necessarily linear chains.

Each role-bound step may declare:

```text
requires
optional_requires
produces
can_start_when
pause_conditions
join_policy
approval_impact
evidence_required
```

Hermes may execute all unblocked bounded steps in parallel.

Sequential or gated steps include:

```text
ZEUS arbitration
THEMIS final veto
APOLLO final gate
memory promotion
external communication
file mutation
workflow canonization
skill promotion
C4/C5 actions
```

---

# 8. Runtime adaptation phase

After each significant role output, ZEUS checks whether the current workflow is still appropriate.

Runtime checks:

```text
workflow_still_relevant
new_signal_detected
role_needed
role_no_longer_needed
step_needed
step_no_longer_needed
subworkflow_needed
memory_needed
knowledge_needed
user_input_needed
risk_changed
confidence_changed
dependency_changed
source_conflict_detected
```

Allowed runtime actions:

```text
continue
add_role
remove_role
add_step
skip_step
insert_subworkflow
switch_workflow
pause_for_user
pause_for_zeus_arbitration
revise_dependencies
reset_to_baseline
propose_candidate_update
```

---

# 9. Confidence-driven adaptation

ZEUS may adapt directly only when:

```text
confidence = high
risk = low
change = reversible
privacy = safe
no external action
no contractual commitment
no memory promotion
no skill activation
```

If confidence is medium, ZEUS asks the relevant roles.

If confidence is low or roles disagree, ZEUS expands context.

Context expansion order:

```text
session memory
project memory
system memory
knowledge
external sources when policy allows
```

If uncertainty remains, ZEUS asks the user.

---

# 10. Signals

Agents/roles must not emit raw reasoning.

They emit structured signals:

```yaml
agent: THEMIS
signal: liability_risk
severity: high
summary: "The requested output may be interpreted as contractual validation."
recommended_action: add_step
recommended_target: liability_warning
requires_user_validation: true
```

Signal types:

```text
missing_data
contradiction
scope_conflict
liability_risk
technical_gap
cost_gap
privacy_risk
workflow_mismatch
unnecessary_step
confidence_drop
candidate_pattern
dependency_conflict
source_conflict
approval_escalation
```

---

# 11. Adaptation report

Every workflow adaptation must be visible in OpenWebUI through a concise report.

Required fields:

```text
initial_workflow_or_none
workflow_origin
decision
reason
signal
roles_consulted
workflow_options_considered
selected_option
rejected_options
roles_added
roles_removed
steps_added
steps_skipped
subworkflow_inserted
workflow_switched_to
dependencies_revised
parallel_groups
join_policy
context_expanded
approval_required
resume_policy
next_action
```

No raw chain-of-thought is displayed.

---

# 12. User validation

User validation is required when the adaptation is:

- irreversible;
- risky;
- externally visible;
- legally or contractually sensitive;
- a memory promotion;
- a permanent workflow change;
- a skill level-up;
- a new canonical workflow creation;
- unresolved after role consultation and context expansion;
- a task contract revision that raises approval level;
- a workflow reset that discards meaningful user-visible work.

Preferred prompt:

```text
The workflow needs a trajectory change. Do you want me to proceed with the proposed adaptation?
```

---

# 13. Candidate updates

After a workflow completes, this skill may propose:

- a candidate workflow update;
- a candidate skill update;
- a new candidate workflow;
- pending XP for a skill;
- a memory candidate.

It must not apply these changes directly.

Candidate path:

```text
session_workflow
→ workflow_candidate
→ Evidence Pack
→ review
→ approval
→ possible template
```

---

# 14. Output discipline

Adaptive orchestration should reduce unnecessary complexity.

It may add structure when required, but it must also remove or skip unnecessary steps.

Rule:

```text
Add when needed.
Remove when unnecessary.
Switch when misaligned.
Insert when a prerequisite is missing.
Create only when nothing fits.
Validate when durable or risky.
Reset when the generated path becomes weaker than the baseline.
```

---

# 15. Status

Current status: `candidate`.

This skill is not active until reviewed against `SKILL_LIFECYCLE.md`, `MODULES.md`, `WORKFLOW_SCHEMA.md`, `WORKFLOW_ADAPTATION.md` and the first real domain workflows.
