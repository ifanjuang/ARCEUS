# MEMORY_STORAGE_MODEL.md

## Purpose

This document defines where Pantheon Next memory is stored, indexed, displayed and promoted.

It separates:

- canonical memory;
- memory candidates;
- evidence;
- approvals;
- operational memory;
- retrieval indexes;
- optional editorial mirrors.

Core doctrine:

```text
Hermes may propose memory.
Pantheon governs canonical memory.
OpenWebUI displays and validates.
```

---

# Storage principle

Canonical memory must remain:

- human-readable;
- versioned;
- diffable;
- reviewable;
- auditable;
- recoverable;
- compatible with Git review.

Therefore:

```text
Git + Markdown = canonical source of truth.
Postgres = index and workflow state.
OpenWebUI = display and validation UI.
Hermes = candidate extraction and evidence generation.
Mem0 = optional operational memory only.
Notion = optional mirror only.
```

---

# Canonical structure

Recommended repository structure:

```text
memory/
  README.md
  registry.yaml

  system/
    canonical/
    candidates/
    evidence/
    approvals/

  projects/
    <project_id>/
      canonical/
      candidates/
      evidence/
      approvals/
```

---

# Scopes

## System memory

System memory stores reusable rules, methods, patterns and preferences.

Examples:

- CCTP formatting preferences;
- governance doctrine;
- reusable contract clauses;
- common Evidence Pack structures;
- recurring agency writing preferences;
- validated domain methods.

System memory must not contain private project facts unless explicitly generalized and sanitized.

---

## Project memory

Project memory stores facts, decisions, constraints and risks tied to a specific project.

Examples:

- project constraints;
- accepted decisions;
- rejected options;
- budget facts;
- planning anchors;
- regulatory assumptions;
- unresolved risks.

Project memory must not leak automatically into system memory.

---

# Lifecycle

Every canonical memory entry must follow this lifecycle:

```text
candidate
  ↓
evidence
  ↓
approval
  ↓
canonical
  ↓
retrieval/index
```

Direct write to canonical memory is prohibited unless explicitly approved by a governance process.

---

# Folder semantics

## `canonical/`

Validated memory.

Requirements:

- clear source;
- stable wording;
- approval reference;
- linked evidence;
- scope marker;
- owner or responsible role.

---

## `candidates/`

Unvalidated proposals.

Sources may include:

- Hermes extraction;
- user instruction;
- meeting summary;
- document analysis;
- repeated pattern detection;
- Mem0 operational memory suggestion.

Candidates must be marked as non-canonical.

---

## `evidence/`

Proof material supporting a candidate or canonical entry.

Evidence may contain:

- source excerpts;
- document references;
- repo diffs;
- tool outputs;
- uncertainty notes;
- timestamps;
- extraction metadata.

---

## `approvals/`

Human or governed validation records.

Approval records should include:

- candidate reference;
- evidence reference;
- approval level;
- approver or approval mechanism;
- decision;
- timestamp;
- residual risks.

---

# Postgres role

Postgres may index memory files.

Allowed uses:

- search;
- filtering;
- relation graph;
- approval status;
- candidate status;
- Evidence Pack links;
- UI performance;
- audit queries;
- synchronization state.

Postgres must not be the only canonical source for memory.

If Postgres contradicts Markdown, Markdown wins.

---

# OpenWebUI role

OpenWebUI may display memory and approval workflows.

Allowed uses:

- browse canonical memory;
- browse candidates;
- display evidence;
- request approval;
- approve/reject candidates;
- route user review back to Hermes/Pantheon.

OpenWebUI must not silently promote memory.

---

# Hermes role

Hermes may:

- extract candidates;
- generate Evidence Packs;
- detect contradictions;
- propose promotion;
- update candidate files on branch;
- build indexes;
- query memory during execution.

Hermes must not:

- write directly to canonical memory without approval;
- auto-promote candidates;
- treat operational memory as truth;
- merge memory branches automatically.

---

# Mem0 role

Mem0 may be used only as Hermes operational memory.

Allowed examples:

- recurring preferences;
- workflow habits;
- interaction history;
- local reminders;
- operator adaptation.

Mem0 may produce memory candidates.

Mem0 must not store or become canonical memory.

---

# Notion role

Notion may be used only as an editorial mirror or reading surface.

Allowed uses:

- browsing memory;
- editorial organization;
- team-friendly presentation;
- manual notes marked as non-canonical.

Notion must not be the source of truth unless a future governance decision explicitly changes this model.

---

# Retrieval role

Retrieval systems may index memory.

Allowed retrieval systems:

- OpenWebUI Knowledge;
- Postgres full-text search;
- pgvector;
- structural retrieval lab;
- PageIndex-style document navigation;
- Hermes retrieval adapter.

Retrieval is not memory promotion.

Search results must preserve status:

```text
canonical
candidate
evidence
approval
obsolete
contradictory
```

---

# File format

Canonical memory files should use Markdown with YAML frontmatter.

Example:

```markdown
---
id: memory-system-cctp-format-001
scope: system
status: canonical
source: ai_logs/2026-05-07-example.md
approval: memory/system/approvals/approval-001.md
updated: 2026-05-07
owner: HESTIA
---

# CCTP format preference

Validated memory content.
```

---

# Prohibited patterns

The following are prohibited:

- vector database as sole canonical memory;
- Mem0 as canonical memory;
- Notion as ungoverned source of truth;
- automatic canonical promotion;
- hidden memory mutation;
- project memory leaking into system memory;
- contradictory memory without status marker;
- irreversible memory deletion without approval.

---

# Decision principle

```text
Hermes remembers operationally.
Pantheon remembers canonically.
OpenWebUI helps humans see and approve.
```
