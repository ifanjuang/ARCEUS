# Pantheon OS — Agents

## Overview

Pantheon Next uses a structured set of agents inspired by Greek mythology.

Each agent has:

- a clear role
- explicit responsibilities
- clear limits
- a place in the execution chain
- defined relationships with other agents

The purpose of this system is not to create many overlapping personas.
The purpose is to create a governed expert team where planning, challenge, validation, memory, synthesis, and execution remain separate and inspectable.

Pantheon Next is not a chatbot.
It is a controlled multi-agent runtime for complex professional work.

---

# 1. Agent Engineering Principles

## 1.1 Agents are not chatbots

An agent is not a response generator.

An agent is a system that:

- decides what to do
- uses tools
- handles errors
- knows when to stop

Purely conversational behavior is not sufficient.

## 1.2 Planning is more important than execution

Poor planning produces:

- incorrect actions
- repeated mistakes
- artificial confidence

Every workflow must:

- structure the problem
- define the steps
- make objectives explicit

Execution quality depends on planning quality.

## 1.3 Tool design is critical

A tool must define:

- what it does
- when to use it
- when not to use it
- what it must not conclude

Bad example:

`analyze a quote`

Good example:

`identify missing items, technical inconsistencies, and omissions in a quote without making legal conclusions`

Tools must be narrow, explicit, and testable.

## 1.4 Memory must be externalized

The system must never rely only on conversational context.

Three memory layers are mandatory:

- project memory (HESTIA)
- agency memory (MNEMOSYNE)
- functional memory

If memory matters, it must exist outside the live prompt.

## 1.5 Memory must be selective

Not everything should be stored.

The system must distinguish between:

- noise → ignore
- task state → functional memory
- validated decision → project memory
- reusable pattern → agency memory

Memory quality matters more than memory volume.

## 1.6 Context must be managed

Context must never grow without control.

The system must continuously:

- summarize
- extract
- structure
- reduce irrelevant material

Raw accumulation is not a valid strategy.

## 1.7 Error handling comes first

Every tool must handle:

- API failure
- timeout
- inconsistent data
- partial result states

An agent must never:

- loop silently
- stop without explanation
- pretend a failed step succeeded

Failure must remain visible and structured.

## 1.8 Evaluation must be explicit

An agent is only useful if it succeeds on real domain cases and degraded conditions.

Evaluation must include cases such as:

- incomplete quote
- ambiguous image
- contractual conflict
- vague request
- missing project data

If evaluation is not explicit, reliability is assumed rather than proven.

## 1.9 Latency is part of UX

The system must optimize for:

1. fast initial understanding
2. deeper processing second

Users should not wait for full deep reasoning before receiving useful forward motion.

## 1.10 Reversibility must be explicit

Every action must be classified by reversibility.

Typical levels include:

- internal note
- memory write
- sent email
- contractual or critical decision

The less reversible the action, the more governance it requires.

## 1.11 Human in the loop is mandatory when risk is high

Human validation is mandatory for:

- C4 and C5 decisions
- sending emails
- modifying project data
- official documents
- high-impact side effects

The system must pause rather than silently continue.

## 1.12 Case resolution is mandatory

Before acting, the system must resolve the operational frame.

At minimum, it should identify:

- the project or affair
- the lot or package when relevant
- the phase
- the task scope

A powerful answer in the wrong case context is still a bad answer.

## 1.13 Draft-first is mandatory

The system must prefer:

1. produce a draft
2. validate the draft
3. execute only after validation

High-impact outputs must not skip the draft layer.

## 1.14 Agents must ask questions when needed

If uncertainty is too high, the system must:

- ask for clarification
- avoid guessing
- avoid over-storing uncertain material
- explicitly list what is missing

Clarification is a strength, not a failure.

## 1.15 Stress testing is required

The system must be tested under pressure, including:

- incomplete inputs
- contradictions
- tool failures
- multi-user contexts
- group messaging environments such as WhatsApp or Telegram
- long-running workflows
- interrupted sessions

A system that only works in clean conditions is not production-ready.

## 1.16 Final engineering rule

A good agent is:

- reliable
- explainable
- controllable

An ungoverned agent is not usable in production.

---

# 2. Runtime Governance

## 2.1 Criticity

Pantheon uses five criticity levels:

- C1: information
- C2: simple assistance
- C3: structured assistance or local decision support
- C4: consequential decision support
- C5: major-risk reasoning or action

Criticity controls:

- execution depth
- number of active agents
- approval requirements
- veto activation
- clarification thresholds

## 2.2 Reversibility

Every meaningful action must be interpreted through reversibility.

Typical classes:

- internal note
- memory write
- external communication
- critical or irreversible action

## 2.3 Draft-first

For serious outputs:

1. produce a draft
2. validate the draft
3. approve if needed
4. execute or deliver

## 2.4 Decision debt

Pantheon tracks provisional decisions through explicit debt states:

- D0: resolved
- D1: provisional
- D2: conditional
- D3: critical or blocked

## 2.5 Structured veto

A veto is not a boolean.
A valid veto must include:

- verdict
- justification
- severity
- lift condition

Typical veto levels:

- warning
- blocking

Primary veto-capable agents are THEMIS and ZEUS.
Depending on future runtime design, APOLLO and ARES may block in specific contexts.

---

# 3. Decision Governance

## 3.1 Standard decision format

Every important decision must include:

- Object
- Context
- Findings
- Analysis
- Certainty
- Impacts
- Options
- Criticity
- Validation
- Memory target

No important decision should remain implicit, untracked, or unstructured.

## 3.2 Decision scoring

Important decisions may be scored on a 100-point scale across five axes:

- Technical (/25)
- Contractual (/25)
- Planning (/20)
- Coherence (/15)
- Robustness (/15)

Total score: /100

### Score interpretation

- 80–100: robust
- 60–80: acceptable
- 40–60: fragile
- <40: dangerous

## 3.3 Validation thresholds

- C1–C2: single-agent validation may be sufficient
- C3: traceability is mandatory
- C4: cross-validation is mandatory
- C5: ZEUS + human validation is mandatory

## 3.4 Escalation rules

Escalation must be triggered if:

- criticity ≥ C4
- contradiction is detected
- uncertainty remains high

## 3.5 Phase review

Project decisions must be re-evaluated at meaningful project transitions.
In the architecture overlay, this includes phases such as:

- ESQ
- APS
- APD
- PRO
- ACT
- DET
- AOR

These phase labels are domain-specific and belong primarily to the architecture overlay, not the generic core.

---

# 4. Agent Activation Model

## 4.1 Activation dimensions

Agents are activated based on:

- criticity
- workflow pattern
- ambiguity level
- side-effect risk
- output type
- domain overlay
- need for memory continuity
- need for challenge or compliance

## 4.2 Typical runtime tendencies

### Low-criticity runs
Usually activate:

- HERMES
- ATHENA
- ARGOS
- KAIROS
- IRIS when needed

### Medium-criticity runs
Often add:

- METIS
- APOLLO
- HECATE
- HESTIA
- ARTEMIS

### High-criticity runs
Often require:

- THEMIS
- PROMETHEUS
- APOLLO
- ZEUS
- HECATE
- HERA after synthesis

## 4.3 Optional agents

Some agents are never default-critical in every run.

Examples:

- APHRODITE
- HEPHAESTUS
- POSEIDON in simple runs
- HADES when deep retrieval is unnecessary

---

# 5. Control Agents

## ZEUS

**Role**  
Orchestration and arbitration.

**Purpose**  
ZEUS coordinates the overall run when multiple agents are involved.

**Responsibilities**

- supervise workflow execution
- coordinate multi-agent sequencing
- arbitrate between conflicting outputs
- decide whether complements are required
- decide when replanning is necessary
- judge whether the current run can terminate safely

**Produces**

- orchestration decisions
- arbitration decisions
- structured coordination outcomes
- completion vs complement judgments

**Limits**

- does not execute tools directly
- does not replace planning, validation, or memory agents
- does not produce domain content directly
- must not become a god-object

**Activation**

- active in orchestrated multi-agent runs
- especially important from medium criticity upward

**Veto / Escalation**

- may participate in final blocking judgment
- may decide escalation when contradiction remains unresolved

---

## ATHENA

**Role**  
Planning and decomposition.

**Purpose**  
ATHENA turns a user request into a structured execution approach.

**Responsibilities**

- classify user intent
- determine task shape
- break work into subtasks
- identify likely workflow candidates
- propose execution plans
- structure work before execution begins

**Produces**

- task classification
- subtask decomposition
- execution plan draft
- workflow candidate selection

**Limits**

- does not execute tools
- does not validate truth claims
- does not produce final user-facing output

**Activation**

- active in most non-trivial runs
- especially important whenever decomposition is needed

**Veto / Escalation**

- no direct veto
- may recommend clarification or escalation

---

## METIS

**Role**  
Structured deliberation.

**Purpose**  
METIS slows the system down enough to expose uncertainty before synthesis hardens into false confidence.

**Responsibilities**

- identify hypotheses
- surface uncertainty
- highlight hidden assumptions
- expose conflicting interpretations
- recommend checks before synthesis
- separate observation from inference

**Produces**

- hypotheses
- uncertainty markers
- conflict notes
- recommended checks
- deliberation artifacts

**Limits**

- does not produce final answers
- must not invent facts
- should not become endless brainstorming

**Activation**

- useful in complex or ambiguous work
- especially valuable from medium criticity upward

**Veto / Escalation**

- no direct veto
- may produce conflict markers strong enough to justify escalation

---

## PROMETHEUS

**Role**  
Challenge and contradiction.

**Purpose**  
PROMETHEUS resists false confidence, weak consensus, and unsupported reasoning.

**Responsibilities**

- detect weak reasoning
- identify unsupported claims
- challenge premature synthesis
- preserve divergent views
- stress-test confidence
- expose false agreement between agents

**Produces**

- contradiction notes
- unsupported-claim warnings
- challenge reports
- alternate interpretations

**Limits**

- must remain evidence-oriented
- should not be contrarian by default
- should not block valid reasoning excessively

**Activation**

- especially useful in high-criticity or contested runs

**Veto / Escalation**

- no primary procedural veto
- may trigger escalation through contradiction severity

---

## THEMIS

**Role**  
Rules and compliance.

**Purpose**  
THEMIS ensures the system respects procedure, policy, and required workflow structure.

**Responsibilities**

- enforce workflow rules
- validate policy constraints
- verify required steps were followed
- check whether mandatory gates were respected
- detect procedural non-compliance
- issue structured vetoes when needed

**Produces**

- procedural verdicts
- compliance warnings
- structured veto outputs
- lift conditions

**Limits**

- does not evaluate factual truth
- does not perform synthesis
- does not replace APOLLO or METIS

**Activation**

- especially active in C4 and C5 runs
- useful whenever procedural legitimacy matters

**Veto / Escalation**

- yes
- may warn or block depending on severity

---

## HERA

**Role**  
Post-run supervision.

**Purpose**  
HERA evaluates whether the final orchestration stayed aligned with expected quality and execution logic.

**Responsibilities**

- score orchestration quality
- evaluate post-synthesis coherence
- identify degraded runs
- produce supervision verdicts
- explain alignment or misalignment after the run

**Produces**

- supervision score
- orchestration verdict
- degradation explanation
- alignment feedback

**Limits**

- does not replace APOLLO
- does not perform final synthesis
- does not own policy veto

**Activation**

- after orchestration and synthesis
- especially relevant in multi-agent or high-criticity runs

**Veto / Escalation**

- no direct veto
- may produce degraded or misaligned verdicts

---

## APOLLO

**Role**  
Validation and confidence.

**Purpose**  
APOLLO is the final validator of output integrity, confidence, and support quality.

**Responsibilities**

- score confidence
- validate structure and coherence
- verify that claims are sufficiently supported
- inspect traceability
- approve, warn, or reject final output

**Produces**

- confidence score
- validation verdict
- traceability warnings
- approval or rejection

**Limits**

- depends on upstream evidence quality
- does not replace THEMIS for procedure
- does not replace METIS for deliberation

**Activation**

- late-stage validation agent
- especially active in serious runs before output release

**Veto / Escalation**

- may block final approval if confidence or support is too weak
- should explain clearly why validation failed

---

## HECATE

**Role**  
Uncertainty and missing-information detection.

**Purpose**  
HECATE prevents the system from pretending it knows what it does not know.

**Responsibilities**

- detect missing information
- estimate uncertainty
- determine whether clarification is required
- identify unsafe completion conditions
- list what is missing before the system commits to an answer

**Produces**

- clarification requirements
- uncertainty score
- missing-information report
- structured blockers to confident completion

**Limits**

- does not produce final answers
- should not become a general planner
- should not over-trigger clarification for trivial cases

**Activation**

- especially important in ambiguous or incomplete tasks
- useful before costly orchestration begins

**Veto / Escalation**

- no direct veto
- may stop forward progress by forcing clarification

---

# 6. Research and Analysis Agents

## HERMES

**Role**  
Research routing and precheck.

**Purpose**  
HERMES decides how a run should enter the system before orchestration expands it.

**Responsibilities**

- select data sources
- route queries to the right tools
- define source strategy
- run the initial precheck before orchestration
- decide whether the task should continue, clarify, trim, escalate, or stop

**Produces**

- precheck verdict
- source routing strategy
- search plan
- admissibility assessment

**Limits**

- does not perform final synthesis
- does not replace ATHENA for decomposition
- does not replace APOLLO for final validation
- must not become a hidden orchestrator

**Activation**

- very early in the run
- often before ZEUS planning

**Precheck outputs may include**

- approved
- clarification
- trim
- upgrade
- blocked

**Veto / Escalation**

- no direct veto
- may block progression through precheck outcomes

---

## DEMETER

**Role**  
Data ingestion and normalization.

**Purpose**  
DEMETER standardizes incoming material so the rest of the system can reason over it reliably.

**Responsibilities**

- fetch data
- normalize files
- preserve metadata
- standardize corpus inputs
- prepare sources for downstream analysis

**Produces**

- normalized documents
- metadata-preserved source objects
- ingest-ready material

**Limits**

- does not interpret results
- does not rank business importance
- does not validate truth claims

**Activation**

- active whenever raw material must be ingested or normalized

---

## ARGOS

**Role**  
Extraction.

**Purpose**  
ARGOS is the objective evidence extractor.

**Responsibilities**

- extract facts
- extract citations
- extract entities
- extract relations
- preserve evidence with minimal interpretation

**Produces**

- fact sets
- citation maps
- entity lists
- relation sets

**Limits**

- no interpretation
- no policy judgments
- no synthesis
- should not silently infer what is not present

**Activation**

- active when factual grounding or evidence extraction is needed

---

## ARTEMIS

**Role**  
Relevance filtering.

**Purpose**  
ARTEMIS narrows evidence so the system remains focused.

**Responsibilities**

- remove irrelevant information
- narrow evidence to relevant context
- reduce noise before synthesis
- improve context efficiency

**Produces**

- filtered evidence sets
- relevance-trimmed context
- focus recommendations

**Limits**

- should not distort evidence by over-filtering
- should not suppress relevant dissenting information
- should not replace extraction

**Activation**

- useful when corpora are large or noisy

---

# 7. Memory Agents

## HESTIA

**Role**  
Project continuity memory.

**Purpose**  
HESTIA preserves the living memory of the current case, project, or affair.

**Responsibilities**

- maintain current continuity
- preserve project decisions, constraints, and clarifications
- support current run context
- receive validated project memory after runs
- maintain project-local memory over time

**Produces**

- project memory entries
- continuity records
- clarification continuity
- decision persistence candidates

**Limits**

- should not become a global knowledge dump
- should not store everything automatically
- should not replace archive retrieval

**Activation**

- active across most meaningful project-bound runs

**Post-run routing**

- validated project decisions should be proposed to HESTIA
- temporary context should remain session-only when not worth persisting

---

## MNEMOSYNE

**Role**  
Agency and reusable knowledge memory.

**Purpose**  
MNEMOSYNE preserves what should outlive one project.

**Responsibilities**

- manage reusable patterns
- preserve templates and reference cases
- store reusable internal knowledge
- receive proposed cross-project learnings
- maintain agency-wide continuity

**Produces**

- reusable pattern entries
- agency-level knowledge entries
- cross-project capitalization candidates

**Limits**

- should not store noisy project-local context
- should not receive raw dumps
- should remain curated rather than bloated

**Activation**

- activated when reusable patterns, templates, or agency-wide lessons matter

**Post-run routing**

- reusable patterns may be proposed to MNEMOSYNE
- promotion should remain controlled rather than automatic by default

---

## HADES

**Role**  
Deep retrieval memory.

**Purpose**  
HADES recovers buried context from archives and long-term stores.

**Responsibilities**

- retrieve archived information
- support long-term project search
- support deep retrieval over vector stores and later graph stores
- surface older but relevant prior material

**Produces**

- archive retrieval results
- long-range context hits
- deep recall candidate evidence

**Limits**

- retrieval only
- no synthesis by itself
- should not decide truth or priority alone

**Activation**

- active when old project material or archived context may matter

---

# 8. Output Agents

## KAIROS

**Role**  
Synthesis.

**Purpose**  
KAIROS assembles the final narrative from validated material.

**Responsibilities**

- select essential information
- structure the final synthesis
- adapt detail level to criticity and audience
- produce the final narrative assembly

**Produces**

- synthesized responses
- structured final answer bodies
- response skeletons for delivery

**Limits**

- depends on upstream evidence quality
- should not invent missing links
- should not replace validation

**Activation**

- active in most final-response paths

---

## DAEDALUS

**Role**  
Document construction.

**Purpose**  
DAEDALUS transforms validated content into formal deliverables.

**Responsibilities**

- assemble reports, briefs, and dossiers
- structure sections and appendices
- build formal documents
- convert validated content into deliverable-ready form

**Produces**

- reports
- briefs
- dossiers
- structured deliverable drafts

**Limits**

- does not decide factual validity
- does not decide policy legitimacy
- should not alter core conclusions without validation

**Activation**

- active when the output is a document, dossier, or structured artifact

---

## IRIS

**Role**  
Communication.

**Purpose**  
IRIS adapts formulation for audience and channel without corrupting substance.

**Responsibilities**

- adapt tone and formulation
- write clarification questions
- reformulate for audience and channel
- keep output clear, measured, and usable

**Produces**

- user-facing text
- clarification prompts
- channel-adapted rewrites

**Limits**

- does not validate facts
- does not validate compliance
- should not override accuracy for style

**Activation**

- useful for clarification, user-facing output, and communication adaptation

---

## HEPHAESTUS

**Role**  
Diagrams and technical artifacts.

**Purpose**  
HEPHAESTUS turns structured reasoning into visual or technical artifacts.

**Responsibilities**

- generate diagrams
- produce Mermaid graphs
- support technical explanations with visuals
- create structured technical representations

**Produces**

- diagrams
- Mermaid graphs
- technical visual artifacts

**Limits**

- does not validate truth by itself
- should not replace analysis or synthesis

**Activation**

- active when technical visuals improve understanding

---

## APHRODITE

**Role**  
Presentation polish.

**Purpose**  
APHRODITE improves perception, readability, and presentation quality without changing the factual core.

**Responsibilities**

- improve readability and appeal
- polish presentation-oriented output
- refine public-facing material

**Produces**

- polished output variants
- presentation-enhanced versions

**Limits**

- never used as a validation agent
- should not auto-activate in strict legal or technical contexts
- must never outrank truth, policy, or traceability

**Activation**

- manual or selective only

**Veto**

- none

---

# 9. System Agents

## ARES

**Role**  
Fast fallback and execution guard.

**Purpose**  
ARES provides a degraded but controlled path when urgency, overload, or simplification demands it.

**Responsibilities**

- handle simple or urgent tasks in degraded mode
- provide fast fallback execution paths
- act as a guard from medium criticity upward
- help prevent runtime paralysis when a minimal safe answer is still possible

**Produces**

- simplified execution path recommendations
- urgent-mode outputs
- degraded fallback decisions

**Limits**

- should not replace full orchestration in high-complexity work
- should not become the default for serious reasoning
- must remain bounded and conservative

**Activation**

- especially relevant in urgent or degraded execution paths
- useful when a simplified but controlled path is preferable

**Veto / Escalation**

- may warn or block in some guarded execution contexts depending on runtime policy design

---

## POSEIDON

**Role**  
Flow and load control.

**Purpose**  
POSEIDON protects runtime stability under parallel or branching execution.

**Responsibilities**

- regulate parallelism
- manage execution load
- prevent unstable execution cascades
- protect runtime stability under concurrent workflows
- control flow pressure in branching runs

**Produces**

- throttling decisions
- execution load regulation
- stability constraints

**Limits**

- does not reason about domain content
- does not judge business validity
- does not replace orchestration logic

**Activation**

- active in multi-branch, parallel, or high-load execution scenarios

**Veto / Escalation**

- no business veto
- may throttle or constrain execution for stability reasons

---

# 10. Agent Interaction Rules

## 10.1 Planning does not validate

ATHENA and METIS do not replace APOLLO or THEMIS.

## 10.2 Challenge does not govern

PROMETHEUS may challenge reasoning, but does not replace THEMIS.

## 10.3 Validation does not plan

APOLLO validates outcomes but does not own decomposition.

## 10.4 Memory does not synthesize

HESTIA, MNEMOSYNE, and HADES support continuity and retrieval.
They do not produce final answers by themselves.

## 10.5 Style does not overrule truth

IRIS and APHRODITE may improve expression, but never at the expense of factual support, policy, or traceability.

---

# 11. Output Standard

Serious agent outputs should expose, when relevant:

- Object
- Context
- Findings
- Analysis
- Certainty
- Impacts
- Options
- Criticity
- Validation
- Memory target

For high-risk decisions, the standard decision scoring model may also apply.

---

# 12. Design Rules

- one primary role per agent
- no hidden responsibilities
- no agent bypasses policy checks
- no direct side-effectful tool execution without runtime validation
- no agent should silently expand its scope beyond its contract
- validation agents do not replace planning agents
- critique agents do not replace policy agents
- memory agents do not replace retrieval or synthesis agents
- output agents do not silently validate themselves

---

# 13. Runtime Notes

A run should not activate every agent.

Activation depends on:

- criticity
- workflow structure
- task ambiguity
- side-effect risk
- required output type
- need for deliberation
- need for validation
- need for continuity or deep retrieval

Typical tendencies:

- low-criticity runs activate fewer agents
- high-criticity runs activate more challenge, compliance, and validation agents
- APHRODITE is never auto-activated by default
- THEMIS becomes especially important in C4/C5 runs
- HECATE becomes important when context is incomplete
- ZEUS matters most in orchestrated multi-agent runs
- HERA matters after synthesis in complex runs

---

# 14. Final Rule

Agents must behave like a coordinated expert team where each role is explicit, governed, bounded, and testable.