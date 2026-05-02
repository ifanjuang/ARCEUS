# Pantheon Next agents — context for Hermes

> Compact orientation. Source of truth: `docs/governance/AGENTS.md`.

Status: **Documented / not runtime**.

---

## 1. Core principle

Pantheon agents are **abstract cognitive roles**.

They are **not** autonomous workers, runtime processes, daemons or background
agents. They do not execute tools by themselves. They reason, classify,
arbitrate, validate and supervise.

```text
Agents = reasoning and governance roles.
Skills, workflows, knowledge, memory, task contracts = the actual matter.
Hermes = the execution layer.
```

Hermes is the runtime. The Pantheon role named **HERMES** is an interface
role inside the agent set; it is **not** the Hermes Agent runtime. They
share a name only to mark the boundary between Pantheon governance and
Hermes execution.

---

## 2. Principal roles

The roles below are the principal Pantheon roles for current operations.
The full canonical list lives in `docs/governance/AGENTS.md`.

| Role | Function |
|---|---|
| ZEUS | Global orchestration, workflow selection, escalation routing |
| ATHENA | Planning, task decomposition, task contract identification |
| ARGOS | Observation, fact extraction, separating facts from assumptions |
| THEMIS | Rules and responsibility, approval-level classification, veto |
| APOLLO | Final validation, coherence, completeness, confidence check |
| PROMETHEUS | Contradiction detection, blind spots, counterarguments |
| HEPHAESTUS | Technical and structural analysis, constructability, implementation critique |
| HECATE | Uncertainty handling, missing-information detection, blocker calls |
| HESTIA | Project memory custodian (validated project context only) |
| MNEMOSYNE | System memory custodian (validated reusable rules and patterns) |
| IRIS | Communication drafting and tone control (does not send) |
| CHRONOS | Sequencing, deadlines, time-dependent constraints |
| HERMES | Execution-interface role inside Pantheon (frames delegation to the Hermes runtime) |

> Note on spelling. Some upstream prompts use the French/Greek form
> **HEPHAISTOS**. The canonical English form in `docs/governance/AGENTS.md`
> is **HEPHAESTUS**. Treat them as the same role; align on the canonical
> form for traceability.

`docs/governance/AGENTS.md` also defines additional roles (METIS, HERA,
ARES, DIONYSOS, DEMETER, POSEIDON, DAEDALUS) which Hermes should consult
when the task explicitly invokes them.

---

## 3. Hard limits

Agents must never:

- contain business-specific rules directly;
- bypass workflows when a workflow exists;
- mutate files without approval;
- promote memory directly;
- activate a skill directly;
- send an external message directly;
- access secrets directly;
- override THEMIS or APOLLO;
- replace human approval where `APPROVALS.md` requires it.

THEMIS can veto. APOLLO can refuse final validation. ZEUS can reroute but
cannot bypass approval.

---

## 4. Approval mapping (summary)

| Approval area | Primary | Secondary |
|---|---|---|
| C0 read / diagnostic | ATHENA | ARGOS, APOLLO |
| C1 draft / suggestion | ATHENA | IRIS, APOLLO |
| C2 reversible low-risk action | THEMIS | ZEUS, APOLLO |
| C3 persistent internal change | THEMIS | ZEUS, APOLLO |
| C4 external / contractual / responsibility action | THEMIS | IRIS, APOLLO, human |
| C5 critical / irreversible / destructive | THEMIS | ZEUS, APOLLO, human |

Reference: `docs/governance/APPROVALS.md`.

---

## 5. HERMES role vs Hermes Agent runtime

| Concept | Where it lives | What it does |
|---|---|---|
| **HERMES** (Pantheon role) | inside Pantheon agent set | frames delegation: defines what is delegated, with which task contract, under which approval, with which expected evidence |
| **Hermes Agent** (runtime) | external to Pantheon | executes the delegated work: tools, skills, sandbox, local memory |

Rule:

```text
HERMES the role decides what is delegated.
Hermes the runtime executes inside the contract.
Neither HERMES nor Hermes canonizes.
```

---

## 6. Typical orchestration patterns

Repository consistency audit:

```text
ATHENA → scope and task contract
ARGOS → files and facts
PROMETHEUS → contradictions
THEMIS → approval and policy risks
APOLLO → final diagnostic
ZEUS → final routing
```

Consequential review (e.g. quote vs CCTP — generic example only):

```text
ATHENA → review plan
ARGOS → extraction
HEPHAESTUS → technical coherence
THEMIS → contractual / responsibility risks
PROMETHEUS → missing scope and contradictions
APOLLO → final review
IRIS → client-readable wording (drafting only)
```

Memory candidate review:

```text
ARGOS → collect candidate
HESTIA → project relevance
MNEMOSYNE → system relevance
THEMIS → legitimacy
APOLLO → quality
```

These patterns are **frames**, not autonomous agent runs. They describe
which roles must contribute to a governed task.
