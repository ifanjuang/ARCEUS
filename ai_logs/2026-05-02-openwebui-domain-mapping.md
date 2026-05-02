# AI LOG ENTRY — 2026-05-02

Branch: `work/chatgpt/openwebui-domain-mapping`

A: ChatGPT

## Objective

Add a governance policy mapping Pantheon canonical domains to OpenWebUI-facing Knowledge Bases, Workspace Models and operator Skills.

## Context

Domains remain canonical in Pantheon.

OpenWebUI may expose domain-facing assets, but must not become the domain authority.

Target separation:

```text
Pantheon defines domains.
OpenWebUI exposes domain-facing assets.
Hermes applies the selected domain through Task Contracts at execution time.
```

## Changes

- Added `docs/governance/OPENWEBUI_DOMAIN_MAPPING.md`.
- Added `config/openwebui_domain_mapping.example.yaml`.
- Updated `docs/governance/README.md` to index the new mapping policy.
- Defined mapping rules for:
  - `domains/general`
  - `domains/architecture_fr`
  - `domains/software`
- Clarified that OpenWebUI Knowledge Bases are sources, not Pantheon memory.
- Clarified that OpenWebUI Workspace Models may mirror agent roles but do not define Pantheon agents.
- Clarified that OpenWebUI Skills are operator aids and are not Pantheon active skills unless reviewed.
- Added Evidence Pack trace fields for OpenWebUI-mapped assets.

## Files Touched

- `docs/governance/OPENWEBUI_DOMAIN_MAPPING.md`
- `config/openwebui_domain_mapping.example.yaml`
- `docs/governance/README.md`
- `ai_logs/2026-05-02-openwebui-domain-mapping.md`

## Critical files impacted

- `docs/governance/OPENWEBUI_DOMAIN_MAPPING.md`
- `config/openwebui_domain_mapping.example.yaml`
- `docs/governance/README.md`

## Tests

- Not run. Documentation and example configuration only.

## Guardrails

- No OpenWebUI configuration mutated.
- No Knowledge Base created automatically.
- No Workspace Model created automatically.
- No OpenWebUI Skill installed automatically.
- No endpoint added.
- No runtime behavior changed.

## Open points

- Future read-only endpoint may expose mapping as `GET /domain/openwebui-mapping`.
- Future validator may compare live OpenWebUI configuration with this policy.
- Dynamic Knowledge Registry remains planned separately.

## Next action

- Review and merge PR.
- Then consider creating `knowledge/registry.example.yaml` or an operations checklist for manual OpenWebUI setup.
