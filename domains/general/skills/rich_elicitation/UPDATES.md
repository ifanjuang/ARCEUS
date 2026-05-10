# UPDATES — rich_elicitation

## 2026-05-10 — Initial candidate

Status: candidate.

Added the initial Pantheon-compatible definition of `rich_elicitation`.

External inspiration:

```text
CyberZenithX/Rich-Elicitation-Skill
```

Adaptation decisions:

```text
not copied as a Claude skill
aligned with REQUEST_ORCHESTRATION.md
bounded to 3 rounds maximum
asks only when ambiguity is material
supports METIS / HECATE / ATHENA / APOLLO
escalates to workflow when risk or deliverable complexity requires it
```

Not implemented:

```text
Hermes skill activation
OpenWebUI widget
runtime prompt router
automatic question UI
tool execution
memory persistence
```

Review required before activation.
