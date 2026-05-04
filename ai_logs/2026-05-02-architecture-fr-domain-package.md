# AI LOG ENTRY — 2026-05-02

Branch: `work/claude/architecture-fr-domain-package`

A: Claude Code

## Objective

Materialize the `domains/architecture_fr/` domain package — French
architecture / maîtrise d'œuvre business domain — without runtime,
without code, without endpoints, without any real client / project /
address / chantier data.

## Operating context

```text
OpenWebUI expose.
Hermes Agent exécute.
Pantheon Next gouverne.
```

## Coordination check

- `git fetch --all --prune` done.
- ChatGPT branch `work/chatgpt/sync-hermes-tools-policy` is currently
  behind `main` (its diff vs main shows only deletions of files now on
  main), so no collision yet on `domains/architecture_fr/`.
- Did **not** touch `hermes/context/tools_policy.md` (reserved for
  ChatGPT).
- Did **not** touch `docs/governance/STATUS.md`.
- Did **not** touch `docs/governance/ROADMAP.md`.
- Did **not** touch `domains/general/skills/knowledge_selection/`.
- Pre-existing `domains/architecture_fr/knowledge_policy.md` was
  augmented additively (one new tier 2 line, one new section §6.bis).
  No previously written content was removed or rephrased.

## Changes

| File | Status | Summary |
|---|---|---|
| `domains/architecture_fr/rules.md` | new | Domain scope, abstract agents, hard limits (no final legal opinion, no regulatory validation without current source, no external send without C4, no real data, no autonomous runtime), default approval mapping, default Evidence Pack discipline, project-source priority, skill / workflow / memory posture, OpenWebUI mapping, forbidden-behavior summary |
| `domains/architecture_fr/knowledge_policy.md` | edited (additive only) | Added MAF and Ordre des Architectes to Tier 2 sources. Added §6.bis: regulatory and normative reference families (RE2020, RT2012, DTU, Eurocodes, NF C 15-100, ERP/IGH, SDIS, accessibilité, PLU, ABF, CSTB AT/DTA/ATEx, loi MOP, ordonnance 2018-1074, CCAG Travaux/MOE/FCS/PI/MI, NF P 03-001, contrat type d'architecte, code civil, code de la construction et de l'habitation, code de l'urbanisme, recommandations MAF) with a `freshness:` block schema and the rule that any unknown / superseded source forbids contractual recommendation until re-check |
| `domains/architecture_fr/output_formats.md` | new | Catalogue of canonical output formats: `note`, `lettre`, `email`, `rapport`, `résumé`, `cctp_review`, `dpgf_review`, `client_message_draft`, `quote_vs_cctp_analysis`, `evidence_summary`. Each format declares default approval level, mandatory sections, audience, status discipline, Evidence Pack expectations. Cross-references `APPROVALS.md`, `EVIDENCE_PACK.md`, `TASK_CONTRACTS.md` §7.2 / §7.3 |
| `domains/architecture_fr/templates/README.md` | new | Template folder index. Hard rules (no real data, no runtime artifact, no final legal/regulatory conclusion, no external send). Naming convention `<format>__<short_label>.md`. Skeleton (frame / references / body / limits / Evidence Pack pointer). Lifecycle. List of first priority templates to add in separate scoped PRs |
| `ai_logs/2026-05-02-architecture-fr-domain-package.md` | new | This log |

## Files Touched

- `domains/architecture_fr/rules.md`
- `domains/architecture_fr/knowledge_policy.md`
- `domains/architecture_fr/output_formats.md`
- `domains/architecture_fr/templates/README.md`
- `ai_logs/2026-05-02-architecture-fr-domain-package.md`

## Critical files impacted

- `domains/architecture_fr/knowledge_policy.md` — additive only. Existing
  text preserved verbatim. New content does not change the existing tier
  list, fetch-before-cite rule, RAG discipline, Evidence Pack
  requirement, memory boundary or forbidden behavior. The new §6.bis is
  appended after §6 and before §7.

## Tests

- Not run. Documentation only.

## Validation

- Read `ai_logs/README.md`.
- Read `docs/governance/STATUS.md`.
- Read `docs/governance/MODULES.md`.
- Read `docs/governance/KNOWLEDGE_TAXONOMY.md` (in earlier turn this
  session).
- Read `docs/governance/APPROVALS.md` (in earlier turn this session).
- Read `docs/governance/EVIDENCE_PACK.md` (in earlier turn this session).
- Read `docs/governance/TASK_CONTRACTS.md` (in earlier turn this session).
- Read `docs/governance/OPENWEBUI_DOMAIN_MAPPING.md`.
- Read existing `domains/architecture_fr/knowledge_policy.md` and
  `manifest.yaml`.
- No code added.
- No endpoint added.
- No script added.
- No external tool integrated.
- No autonomous runtime path reactivated.
- No real client / project / address / person / chantier data introduced.
- All examples are fictional and neutral (`P-001`, `LOT-XX`, `CLIENT-DEMO`,
  `Affaire fictive de démonstration`, `Adresse anonymisée`,
  `YYYY-MM-DD`, `€X XXX,XX`).
- `templates/` folder created empty (only `README.md`); first concrete
  template files explicitly deferred to separate scoped PRs.

## Doctrine alignment

- Pantheon governs, does not execute.
- Hermes executes, does not canonize.
- OpenWebUI exposes, does not canonize.
- This domain produces drafts and candidates. Final legal / contractual
  authorship stays with the user.
- Knowledge ≠ Memory. Memory promotion is C3 + Evidence Pack.
- Regulatory citations require source, tier, freshness check.
- External outputs are C4 with explicit user approval; the user controls
  the channel.
- No autonomous runtime path inside Pantheon Next.
- `domains/architecture_fr/` is canonical. `domains/architecture/` (without
  `_fr`) must not be recreated.

## Open points

- `templates/` folder currently contains only `README.md`. The first
  concrete templates (`quote_vs_cctp_analysis__lot_xx_devis_x.md`,
  `cctp_review__lot_xx.md`, `client_message_draft__contexte_neutre.md`,
  `evidence_summary__example.md`) are deferred to one PR per template
  to keep review small.
- A `domain.md` file (top-level domain summary) is referenced in
  `docs/governance/MODULES.md` §2.2 as part of the canonical structure
  but does not exist on `main`. Not added here to keep this PR scoped to
  the four files explicitly requested. Should be added in a follow-up.
- `STATUS.md` and `ROADMAP.md` should eventually mention "domains/
  architecture_fr/ rules + output_formats + templates/ scaffold added".
  Left to the next sync PR (reserved scope).
- ChatGPT's `work/chatgpt/sync-hermes-tools-policy` branch may need to
  rebase on main once the `tools_policy.md` sync work is committed and
  pushed; this PR does not block that work.

## Next action

- Open PR `work/claude/architecture-fr-domain-package → main`.
- After merge, add `domain.md` (top-level summary) and the first
  concrete templates in separate scoped PRs.
