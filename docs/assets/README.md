# README diagram assets

This folder is reserved for exported diagrams used by `README.md` and governance documentation.

The editable source diagrams currently live in Lucidchart. PNG/SVG exports should be committed here only when the rendering is stable and readable in GitHub.

---

## Current Lucid sources

| Diagram | Status | Editable source | Target export path |
|---|---|---|---|
| README overview | Draft source ready | https://lucid.app/lucidchart/6bfe723f-4ad9-4545-b520-5de0833ccecf/edit?invitationId=inv_0c02b419-0fdc-4257-b52c-7ad4e9b612f6 | `docs/assets/pantheon-next-overview.png` |
| Governed execution flow | Draft source ready | https://lucid.app/lucidchart/6bfe723f-4ad9-4545-b520-5de0833ccecf/edit?invitationId=inv_0c02b419-0fdc-4257-b52c-7ad4e9b612f6 | `docs/assets/pantheon-governed-flow.png` |
| Knowledge vs Memory | Draft source ready | https://lucid.app/lucidchart/6bfe723f-4ad9-4545-b520-5de0833ccecf/edit?invitationId=inv_0c02b419-0fdc-4257-b52c-7ad4e9b612f6 | `docs/assets/pantheon-knowledge-vs-memory.png` |
| Repository map | Draft source ready | https://lucid.app/lucidchart/6bfe723f-4ad9-4545-b520-5de0833ccecf/edit?invitationId=inv_0c02b419-0fdc-4257-b52c-7ad4e9b612f6 | `docs/assets/pantheon-repository-map.png` |
| Pantheon ↔ Hermes contract | Draft source ready | https://lucid.app/lucidchart/6bfe723f-4ad9-4545-b520-5de0833ccecf/edit?invitationId=inv_0c02b419-0fdc-4257-b52c-7ad4e9b612f6 | `docs/assets/pantheon-hermes-contract.png` |
| Agent roles | README-safe source ready | https://lucid.app/lucidchart/33869062-1228-4edc-a4ae-9a68ceeb7465/edit?invitationId=inv_3b16c914-108e-4bae-b6ba-0d48d6c09396 | `docs/assets/pantheon-agent-roles.png` |

---

## Integration policy

Do not commit diagram exports that are illegible, cropped, monochrome when color is required, or visually misleading.

Before adding a PNG/SVG export to the repository, verify:

```text
text is readable on GitHub
colors are preserved
no labels overlap
no cropped boxes
no private data appears
terms match docs/governance vocabulary
```

---

## README inclusion template

Use this only after exports are committed:

```md
## Architecture at a glance

![Pantheon Next overview](docs/assets/pantheon-next-overview.png)

## Governed execution

![Governed execution flow](docs/assets/pantheon-governed-flow.png)

## Pantheon ↔ Hermes contract

![Pantheon Hermes contract](docs/assets/pantheon-hermes-contract.png)

## Agent roles

![Pantheon agent roles](docs/assets/pantheon-agent-roles.png)

## Knowledge vs Memory

![Knowledge vs Memory](docs/assets/pantheon-knowledge-vs-memory.png)
```

---

## Diagram doctrine

The diagrams must preserve these boundaries:

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

They must not visually imply:

```text
Pantheon executes tools directly
OpenWebUI canonizes memory
Hermes can bypass approvals
External tools are allowed by default
Agents are autonomous Pantheon workers
```
