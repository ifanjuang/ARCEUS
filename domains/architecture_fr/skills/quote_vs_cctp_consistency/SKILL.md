# Quote vs CCTP Consistency

> Candidate Pantheon skill (status: `candidate`).
> Compares a contractor quote against the CCTP (and where relevant the
> DPGF / programme) and reports concordances, gaps, divergences,
> out-of-scope items and risk flags as a structured **review-mode** output.

Status: **Documented / not runtime**.

```text
OpenWebUI expose.
Hermes Agent exécute.
Pantheon Next gouverne.
```

Source of truth: `domains/architecture_fr/rules.md`,
`domains/architecture_fr/knowledge_policy.md`,
`domains/architecture_fr/output_formats.md`,
`docs/governance/TASK_CONTRACTS.md` §7.2 (`quote_vs_cctp_review`),
`docs/governance/EVIDENCE_PACK.md`,
`docs/governance/APPROVALS.md`,
`docs/governance/KNOWLEDGE_TAXONOMY.md`.

---

# 1. Purpose

`quote_vs_cctp_consistency` prevents Pantheon Next from validating or
critiquing a contractor quote without a structured comparison against
the contractual specification.

It produces a **review** output (mode `review`, not `decision`):
matched items, missing items, divergent items, out-of-scope items,
contractual / responsibility risk flags, technical risk flags,
quantitative risk flags, hypotheses and limits.

The skill does **not** replace the architect / MOE / MOA. It supports
the user. The user remains the author of any external position.

---

# 2. Core rule

```text
Compare quote against CCTP under task contract.
Return a candidate review, never a final contractual position.
Cite project document references and version/date when known.
Flag missing or stale sources instead of guessing.
```

---

# 3. Default operating mode

| Field | Value |
|---|---|
| Mode | `review` |
| Default approval | C1 (review-mode); C3+ if drives a file mutation; **C4** if presented externally |
| Status | `candidate` (this manifest) |
| Memory impact | `candidate_only` (no automatic promotion) |
| Evidence Pack | **mandatory** |
| External send | forbidden — drafts only |
| Privacy | fictional examples only — no real client / project / address / chantier data |

---

# 4. Inputs

Required:

```text
cctp_document            # references + extracted text or chunks (project-controlled source)
quote_document           # references + extracted text or chunks (contractor source)
lot_scope                # which lot or lots are being compared
```

Optional:

```text
dpgf_document            # additional contractual reference (DPGF / DQE)
ccap_document            # administrative clauses if responsibility-relevant
project_context          # resolved by domains/general/skills/project_context_resolution
freshness_window         # how recent the cited regulatory references must be
priority_aspects         # technical | contractual | quantitative | mixed
```

Forbidden as inputs:

```text
real client identifiers
real addresses
real budget amounts tied to a real engagement
private conversation history
search-snippet-only sources (must be fetched and read)
```

---

# 5. Outputs

The skill produces a single structured review object. The output
contract is:

```yaml
quote_vs_cctp_consistency_result:
  status: review_complete | review_blocked | needs_more_evidence
  reviewed_at: YYYY-MM-DD
  scope:
    lot: LOT-XX
    cctp_reference: { filename: "", version: "", date: "", source_status: "" }
    quote_reference: { filename: "", version: "", date: "", source_status: "" }
    dpgf_reference: { filename: "", version: "", date: "", source_status: "" }
  matched_items: []           # quote line covers a CCTP requirement
  missing_items: []           # CCTP requirement with no quote line
  divergent_items: []         # quote line conflicts with CCTP wording / quantity / unit
  out_of_scope_items: []      # quote line not in CCTP scope (added scope, suspect)
  duplicate_items: []         # same scope priced twice in the quote
  technical_risk_flags: []    # HEPHAESTUS-level: lots interfaces, structure, fluides
  contractual_risk_flags: []  # THEMIS-level: clauses, responsibilities, missing waivers
  quantitative_risk_flags: [] # DEMETER-level: unit price anomaly, quantity anomaly
  freshness_flags: []         # regulatory or normative reference unknown / stale
  hypotheses: []              # explicit assumptions made by the skill
  limits: []                  # what was not checked, why
  approval_required:
    level: C1            # default; escalated by output use
    reason: ""
  next_safe_action: ""
  evidence_pack_id: ""
```

Forbidden in output:

```text
a final contractual position
a final legal opinion
a final regulatory validation
a quantity certified as "correct" without a recomputation trace
a recommendation that an item should be paid / not paid
auto-generated text addressed to a third party
```

---

# 6. Comparison procedure

The procedure is bounded and read-only.

```text
1. Resolve project context           (general/skills/project_context_resolution)
2. Confirm task contract             (TASK_CONTRACTS.md §7.2 quote_vs_cctp_review)
3. Inventory CCTP requirements       (ARGOS — extract structured items)
4. Inventory quote items             (ARGOS — extract structured items)
5. Map CCTP↔quote items              (skill core: matching by lot, function, label, normative reference)
6. Detect divergences                (quantity, unit, scope, exclusion clause)
7. Detect duplicates                 (same scope priced twice)
8. Detect out-of-scope additions     (priced item not in CCTP)
9. Technical risk pass               (HEPHAESTUS — interfaces, lots adjacents)
10. Contractual risk pass            (THEMIS — clauses, responsibility)
11. Quantitative risk pass           (DEMETER — unit prices, quantities)
12. Freshness pass on regulatory refs (knowledge_policy.md §6.bis.3)
13. Compose Evidence Pack
14. Return structured result with approval_required and next_safe_action
```

Each step records source references in the Evidence Pack.

---

# 7. Allowed actions

```text
read CCTP / DPGF / CCAP / quote text and structured fields under task contract
extract items and metadata into structured form
match items by lot / label / normative reference
flag mismatches as candidate findings
emit hypotheses and limits explicitly
ask the user one targeted clarification when ambiguity blocks a flag
produce Evidence Pack
return result as a candidate review
```

---

# 8. Forbidden actions

```text
mark a quote as "compliant" or "non-compliant" as final
recommend payment / refusal of an item as final
issue a regulatory validation
sign or apply a contractual position
mutate any Pantheon source-of-truth file
canonize a finding as Pantheon memory
promote a finding to project or system memory automatically
send anything to a client / MOA / contractor / authority
mix two real projects without explicit comparison authorization
use a search snippet as evidence
fabricate a CCTP or quote reference (filename, version, date) when unknown
drop THEMIS or APOLLO from the workflow that consumes this skill
```

---

# 9. Need-for-context check

Before running, the skill checks whether project context is required.
For this skill it almost always is, but the skill must still run
`project_context_resolution` (or accept a resolved context as input)
and refuse to proceed when:

- the project is unresolved;
- the user requested cross-project comparison without explicit
  authorization;
- the CCTP and the quote belong to different projects;
- private project data would have to be embedded into a fictional
  example.

---

# 10. Risk classes

The skill emits risk flags but does not block by itself. Blocking is
THEMIS / APOLLO / HECATE responsibility.

| Class | Examples |
|---|---|
| Technical | structural interface gap, fluid coordination missing, accessibility/ERP feature missing |
| Contractual | scope exclusion clause, missing penalty clause reference, responsibility transfer ambiguity |
| Quantitative | unit price anomaly vs DPGF, quantity anomaly vs plans, missing unit |
| Regulatory | RE2020 / DTU / Eurocode / NF / CCAG citation missing or stale |
| Freshness | source older than freshness window, status `unknown` or `superseded` |
| Privacy | real-data leakage detected in input |

---

# 11. Confidence policy

```yaml
review_complete:
  threshold: high coverage of CCTP items mapped to quote lines
  action: return_structured_review_with_evidence

needs_more_evidence:
  threshold: low coverage or missing source(s)
  action: return_structured_review_with_blockers_and_request_more_sources

review_blocked:
  threshold: input invalidates the review (mixed projects, real-data leakage, stale regulation in critical path)
  action: stop_with_explicit_reason
```

Even with `review_complete`, downstream use as a contractual position
is **C4** and requires user approval and IRIS / THEMIS / APOLLO review.

---

# 12. Interaction with the workflow

Consumed by:

```text
domains/architecture_fr/workflows/quote_vs_cctp_review/   (this domain, candidate template)
```

The workflow may compose this skill with:

```text
domains/general/skills/project_context_resolution/
domains/general/skills/knowledge_selection/
```

This skill is **not** an orchestrator. It is a bounded review function.

---

# 13. Privacy

```text
fictional examples only
no real client / project / chantier / address / personal data
real data in inputs is allowed at runtime, but the skill must not echo
  it into outputs in ways that produce repository-stored artifacts
real data in Evidence Pack must follow the project privacy scope
templates and tests must remain neutral and non-traceable
```

---

# 14. Status

Current status: **`candidate`**.

This skill is not active until reviewed against:

```text
docs/governance/SKILL_LIFECYCLE.md
docs/governance/TASK_CONTRACTS.md §7.2
docs/governance/EVIDENCE_PACK.md
docs/governance/APPROVALS.md
docs/governance/KNOWLEDGE_TAXONOMY.md
domains/architecture_fr/knowledge_policy.md §6.bis (regulatory freshness)
```

XP and level changes follow `SKILL_LIFECYCLE.md`. No level-up is
automatic.

---

# 15. Final rule

```text
Compare. Cite. Flag. Limit. Hand off to review.
Never canonize a contractual position from a quote-vs-CCTP comparison alone.
```
