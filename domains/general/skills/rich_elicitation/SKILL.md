# Skill — rich_elicitation

Status: candidate.

Domain: general.

Purpose: ask bounded, useful clarifying questions before starting ambiguous or high-variance tasks, so Pantheon can avoid silent assumptions and reduce revision loops.

Inspired by `CyberZenithX/Rich-Elicitation-Skill`, adapted to Pantheon Next governance.

---

## 1. Role in Pantheon

`rich_elicitation` is a request-framing skill.

It supports:

```text
METIS request framing
HECATE uncertainty detection
ATHENA method selection
APOLLO brief adherence
```

It does not replace `REQUEST_ORCHESTRATION.md`.

It does not create a new workflow runtime.

It does not ask questions by default for every request.

Core rule:

```text
Ask only when ambiguity changes the answer materially.
```

---

## 2. Use when

Use this skill when a user request has at least two substantial ambiguous dimensions and several reasonable answers.

Typical triggers:

```text
unknown audience
unknown tone
unclear scope
unclear output format
unclear depth
several valid strategic directions
unknown constraints
unknown source boundary
unclear deliverable definition
unclear success criteria
high cost of wrong first draft
```

Good use cases:

```text
complete report
dossier complet
article long
strategic roadmap
project plan
technical architecture choice
client-facing communication with unclear intent
creative direction
recommendation or comparison
research synthesis
CCTP or documentation package when source boundary is unclear
```

---

## 3. Do not use when

Do not use this skill for:

```text
simple factual question
simple calculation
clear rewrite request
clear translation request
simple spelling/grammar correction
single obvious output format
urgent answer where assumptions are acceptable
request where the user explicitly says not to ask questions
```

If ambiguity is minor, proceed and state assumptions.

---

## 4. Trigger decision

Before asking, assess:

```yaml
elicitation_trigger:
  ambiguous_dimensions: []
  material_to_output: true | false
  user_cost_if_wrong: low | medium | high
  can_reasonably_assume: true | false
  recommended_action: ask | proceed_with_assumptions | route_to_workflow
```

Ask only if:

```text
ambiguous_dimensions >= 2
and material_to_output = true
and can_reasonably_assume = false
```

Escalate to workflow if:

```text
risk is C3/C4/C5
sources must be gathered before questions
several roles must assess ambiguity
questions reveal a deliverable contract is needed
```

---

## 5. Question rounds

Maximum rounds:

```text
Round 1: up to 3 blocking questions
Round 2: up to 3 follow-up questions unlocked by Round 1
Round 3: up to 2 final detail questions, used sparingly
```

After Round 3:

```text
Proceed.
State remaining assumptions explicitly.
Do not keep asking indefinitely.
```

Stop earlier when enough context exists.

---

## 6. Question grouping

Group related questions.

Do:

```text
Ask 2–3 related questions in one block.
Explain briefly why the questions matter.
Offer recommended choices when a safe preference exists.
```

Do not:

```text
ask 6 separate question blocks
ask questions one by one if answers are independent
ask cosmetic questions before blocking questions
ask vague questions such as "what do you want?"
```

---

## 7. Question types

Supported types:

```text
single_select
multi_select
rank_priorities
free_text
confirm_assumption
```

Use:

```text
single_select for tone, format, scope, direction
multi_select for sections or included topics
rank_priorities for competing goals
free_text only when predefined options would be misleading
confirm_assumption when Pantheon has a strong safe default
```

---

## 8. Recommended options

Each question should include a recommendation when Pantheon has a defensible default.

Rules:

```text
recommend at most one option per question
mark it as Recommended
choose lowest-risk or most useful default
avoid recommendation if genuinely neutral
```

Example:

```text
Q1. Quel niveau de profondeur faut-il viser ?
- Synthèse courte
- Rapport structuré standard (Recommended)
- Analyse exhaustive
- Version décisionnelle avec risques et prochaines étapes
```

---

## 9. Output schema

Candidate output:

```yaml
rich_elicitation:
  round: 1
  framing_sentence: null
  questions:
    - id: Q1
      type: single_select
      question: null
      options:
        - label: null
          recommended: true | false
      why_it_matters: null
  assumptions_if_skipped: []
  stop_condition: enough_context | max_rounds | user_declines | workflow_required
  next_action: proceed | ask_round_2 | ask_round_3 | route_to_workflow
```

---

## 10. Pantheon role mapping

| Role | Contribution |
|---|---|
| METIS | Detects whether clarification is required. |
| HECATE | Identifies ambiguity and hidden uncertainty. |
| ATHENA | Determines whether the request needs direct answer, assumptions or workflow. |
| THEMIS | Flags if asking is required because risk is too high. |
| APOLLO | Checks that the final answer respects the clarified brief. |
| IRIS | Wording of the question block. |

---

## 11. Approval relationship

Question asking itself is normally C0/C1.

Escalate when the questions or answers could influence:

```text
contractual position
external send
memory promotion
file mutation
runtime activation
legal/financial commitment
```

Rich elicitation does not approve actions.

---

## 12. Evidence relationship

For simple clarification, no Evidence Pack is required.

For consequential work, the final Evidence Pack may record:

```text
clarifying questions asked
user-selected options
assumptions retained
scope decisions
unresolved ambiguities
```

Inline elicitation is not proof by itself.

---

## 13. Anti-patterns

Forbidden:

```text
asking questions to delay simple work
asking questions when user explicitly asked for best-effort output
asking for information already available in approved context
asking too many rounds
turning every answer into a survey
using elicitation to bypass research
using elicitation to avoid making a professional recommendation
marking multiple options Recommended for one question
```

---

## 14. Final rule

```text
Clarify before producing when ambiguity is material.
Assume and state limits when ambiguity is minor.
Escalate when ambiguity changes risk.
```
