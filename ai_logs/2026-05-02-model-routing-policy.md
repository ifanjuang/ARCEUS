# AI LOG ENTRY — 2026-05-02

Branch: `work/chatgpt/model-routing-policy`

A: ChatGPT

## Objective

Add a governance policy for model routing across OpenWebUI, Ollama instances, Hermes execution and Pantheon abstract agents.

## Context

The goal is not to create a Pantheon LLM provider router.

The target separation remains:

```text
OpenWebUI exposes configured models and presets.
Hermes resolves and executes model calls.
Pantheon Next defines policy, allowed mappings and fallback rules.
```

## Changes

- Added `docs/governance/MODEL_ROUTING_POLICY.md`.
- Added `config/model_routing.example.yaml`.
- Updated `docs/governance/README.md` to index the model routing policy.
- Covered both `single_ollama_instance` and `multi_ollama_instance` modes.
- Defined fallback behavior for C0-C5.
- Defined role-based mappings for abstract agents:
  - ATHENA
  - ARGOS
  - THEMIS
  - APOLLO
  - IRIS
  - HESTIA
  - MNEMOSYNE
  - HEPHAESTUS
  - PROMETHEUS
  - ZEUS
- Added required Evidence Pack trace fields for model substitutions.

## Files Touched

- `docs/governance/MODEL_ROUTING_POLICY.md`
- `config/model_routing.example.yaml`
- `docs/governance/README.md`
- `ai_logs/2026-05-02-model-routing-policy.md`

## Critical files impacted

- `docs/governance/MODEL_ROUTING_POLICY.md`
- `config/model_routing.example.yaml`

## Tests

- Not run. Documentation and example configuration only.

## Guardrails

- No LLM router added to Pantheon.
- No runtime model execution added.
- No OpenWebUI configuration mutated.
- No Ollama instance configured automatically.
- No endpoint added.
- No secrets added.

## Open points

- Future read-only endpoint may expose model routing policy as `GET /domain/model-routing`.
- Future validation can check that OpenWebUI presets and Hermes runtime configuration align with this policy.
- C4/C5 fallback should remain blocked or require manual review unless explicitly approved.

## Next action

- Review and merge PR.
- Then add OpenWebUI domain mapping policy if needed:
  - Pantheon domains remain canonical.
  - OpenWebUI Knowledge Bases and Workspace Models only mirror or expose domain assets.
