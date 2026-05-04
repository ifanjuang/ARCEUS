# Quote vs CCTP Consistency — Examples

> Fictional examples only. No real project, client, address, person, chantier or budget tied to a real engagement.

---

# 1. Matched item with explicit reference

## Inputs (fictional)

```yaml
project_id: P-001
lot: LOT-07-VMC
cctp_reference:
  filename: "P-001_CCTP_LOT-07_v2.0.md"
  version: "2.0"
  date: "YYYY-MM-DD"
  source_status: signed
quote_reference:
  filename: "P-001_devis_entreprise_DEMO-A_v1.md"
  version: "1.0"
  date: "YYYY-MM-DD"
  source_status: draft
cctp_extract: |
  7.3.2 — VMC double flux haute efficacité, conforme NF DTU 68.3,
  isolation acoustique des gaines en traversée de plancher,
  bouches d'extraction réglables.
quote_extract: |
  L7.3 — VMC double flux, modèle DEMO-A-VMC-DF-200, isolation
  acoustique des gaines, bouches d'extraction réglables.
  Référence DTU 68.3.
```

## Result

```yaml
quote_vs_cctp_consistency_result:
  status: review_complete
  reviewed_at: YYYY-MM-DD
  scope:
    lot: LOT-07-VMC
  matched_items:
    - cctp_id: CCTP-7.3.2
      quote_id: L7.3
      label: "VMC double flux haute efficacité"
      normative_reference: "NF DTU 68.3"
      coverage: full
      notes: "Acoustique et bouches réglables présentes des deux côtés."
  approval_required:
    level: C1
    reason: review_mode_candidate_output
  next_safe_action: "Continue with the next CCTP item or return result for THEMIS/APOLLO review."
  evidence_pack_id: EP-DEMO-0001
```

---

# 2. Missing item (CCTP requirement not in quote)

## Inputs (fictional)

```yaml
cctp_extract: |
  7.5.1 — Coordination acoustique avec lot 06 — Faux-plafonds.
  Fourniture de joints acoustiques aux interfaces de plénum.
quote_extract: |
  (no line addresses inter-lot acoustic coordination)
```

## Result

```yaml
missing_items:
  - cctp_id: CCTP-7.5.1
    label: "Coordination acoustique avec lot 06 — Faux-plafonds"
    severity: technical_and_contractual
    risk: "Le quote ne couvre pas les joints acoustiques d'interface; risque d'imputation de défaut acoustique au mauvais lot."
    recommended_clarification:
      to: "MOE / entreprise"
      question: "Confirmer si 7.5.1 est inclus dans une ligne implicite ou doit être ajouté."
hypotheses:
  - "Aucune ligne du devis n'a été interprétée comme couvrant 7.5.1."
limits:
  - "Pas de plan transmis; coordination inter-lot non vérifiable au-delà du CCTP."
```

---

# 3. Divergence (quantity / unit anomaly)

## Inputs (fictional)

```yaml
cctp_extract: |
  7.4 — 12 bouches d'extraction Ø125, conformes NF EN 13141-2.
quote_extract: |
  L7.4 — 8 bouches d'extraction Ø100.
```

## Result

```yaml
divergent_items:
  - cctp_id: CCTP-7.4
    quote_id: L7.4
    divergence_type: quantity_and_unit
    cctp_value: { quantity: 12, diameter_mm: 125, normative_reference: "NF EN 13141-2" }
    quote_value: { quantity: 8, diameter_mm: 100, normative_reference: null }
    severity: contractual
    risk: "Sous-fourniture potentielle et changement de diamètre non motivé."
    recommended_clarification:
      to: "entreprise"
      question: "Justifier la quantité 8 vs 12 et le diamètre 100 vs 125; confirmer la conformité NF EN 13141-2."
quantitative_risk_flags:
  - { line: L7.4, flag: quantity_below_cctp, factor: 0.667 }
  - { line: L7.4, flag: unit_diameter_change, cctp: 125, quote: 100 }
contractual_risk_flags:
  - { line: L7.4, flag: missing_normative_reference }
```

---

# 4. Out-of-scope addition

## Inputs (fictional)

```yaml
cctp_extract: |
  (no scope line for cooling)
quote_extract: |
  L7.10 — Module de rafraîchissement adiabatique sur réseau VMC.
```

## Result

```yaml
out_of_scope_items:
  - quote_id: L7.10
    label: "Rafraîchissement adiabatique"
    reason: "Aucune section CCTP n'introduit ce poste."
    recommended_clarification:
      to: "MOA / MOE"
      question: "Confirmer si ce poste est demandé en variante; sinon, retirer du devis."
contractual_risk_flags:
  - { line: L7.10, flag: scope_addition_without_cctp_basis }
```

---

# 5. Stale regulatory reference (freshness flag)

## Inputs (fictional)

```yaml
cctp_extract: |
  7.6 — Conformité RT2012, isolation thermique selon coefficient U = 0,24.
quote_extract: |
  L7.6 — Isolation thermique conforme RT2012, U = 0,24.
freshness_window: "current_year"
```

## Result

```yaml
freshness_flags:
  - subject: regulatory_reference
    family: thermal_regulation
    cctp_value: "RT2012"
    quote_value: "RT2012"
    status: superseded_by_RE2020_for_new_construction
    recommended_action: "Vérifier la date du PC; si projet neuf postérieur à l'entrée en vigueur RE2020, mettre à jour la référence avant toute conclusion contractuelle."
limits:
  - "La date du permis de construire n'est pas dans les inputs; freshness flag non concluant sans cette info."
status: needs_more_evidence
approval_required:
  level: C1
  reason: review_mode_candidate_output_with_blockers
next_safe_action: "Demander la date du PC et le périmètre RE2020 vs RT2012, puis re-run."
```

---

# 6. Review blocked — privacy leak detected in input

## Inputs (fictional but illustrative of a block)

```yaml
quote_extract: |
  Devis pour [vrai nom de chantier], [vraie adresse], client [vrai nom].
```

## Result

```yaml
status: review_blocked
limits:
  - "L'input contient des données nominatives et d'adresse. Le résultat ne peut pas être stocké tel quel dans le dépôt."
next_safe_action: "Anonymiser ou ne pas sortir l'output du périmètre projet; ne pas commiter d'extrait dans les exemples ou tests."
approval_required:
  level: C1
  reason: privacy_leak_detected_in_input
```

---

# 7. Cross-project comparison without authorization

## Inputs (fictional)

```yaml
cctp_extract:
  project_id: P-001
quote_extract:
  project_id: P-002
```

## Result

```yaml
status: review_blocked
limits:
  - "Les documents appartiennent à deux projets distincts (P-001 et P-002) sans autorisation explicite de comparaison."
next_safe_action: "Demander une autorisation explicite de comparaison cross-project, puis re-run; sinon traiter chaque projet séparément."
approval_required:
  level: C3
  reason: cross_project_comparison_requires_authorization
```

---

# 8. Final note on examples

All scenarios above use placeholder values (`P-001`, `LOT-07-VMC`,
`DEMO-A-VMC-DF-200`, `EP-DEMO-0001`, `YYYY-MM-DD`). No real client,
project, address, person or chantier appears, and none must be added in
this folder.
