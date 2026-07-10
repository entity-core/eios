# About EIOS and the Entity Core initiative

This document covers everything *around* the EIOS specification — the initiative, origin, naming, governance, licensing, and project structure. The framework itself lives in the [master documentation](spec/eios-1.0-master-documentation.md).

## The initiative

**Entity Core** ([entitycore.org](https://entitycore.org)) is an open initiative for entity-centered information operating systems. Its purpose is to define how an organization can preserve, govern, operationalize, and improve its operating memory — knowledge, decisions, agreements, financials, customer signals — in a form usable by both its people and its AI agents.

The initiative maintains one framework and its surrounding assets:

| Name | What it is |
| --- | --- |
| **Entity Core** | The public initiative, website, and GitHub organization |
| **EIOS** | Entity Information Operating System — the open framework and specification |
| **Keel** | The reference implementation of EIOS: a durable information spine |
| **Weave** | The Entity Context Blueprint: the organizing logic of entity information |
| **Entity Keel** | One organization's own running instance — its private source of truth |
| **Keel Managed / Keel Self-Hosted** | The two deployment profiles |

## Origin and lineage

EIOS originated as a sibling framework to **PIOS** (Personal Information Operating System, [github.com/peecos](https://github.com/peecos)), created by [Valto Loikkanen](https://github.com/valto). PIOS asks how an *individual person* can preserve, organize, govern, and use their information over time. EIOS asks the same question for an *entity* — a company, cooperative, association, foundation, public body, or other structured organization that must justify its continued existence through stakeholder value.

On **2026-07-08**, EIOS was founded as an independent framework. The founding decision established four rules that govern the relationship:

1. **Copy at fork, not shared dependency.** Principles, terms, and patterns inherited from PIOS are copied into EIOS and owned here. Neither framework references the other as a live dependency.
2. **Attribution carries lineage.** Recognition of origins is expressed through attribution, not through name matching or structural coupling.
3. **No backwards compatibility.** Neither framework constrains the other. Inherited terms may be redefined in EIOS without coordination, and vice versa.
4. **Divergence is documented, not accidental.** The specification's [Naming and Terminology Mapping](spec/eios-1.0-master-documentation.md#37-naming-and-terminology-mapping) section records which terms were inherited, from where, and how their EIOS meaning differs.

## Why the names

- **Keel** is intentionally structural rather than cognitive or organizational. The keel is the structural spine of a vessel: it is laid first, everything else is built on and around it, and while crews, cargo, engines, and flags change, the keel is what makes it the same ship. That is entity continuity in one word.
- **Weave** describes how an entity's many threads — people, agents, agreements, decisions, customers, finances, obligations — are structured into one coherent fabric. It extends the fiber metaphor inherited from PIOS, where **Cotton** is the personal fiber: personal fiber, woven into entity fabric.
- **EIOS** parallels PIOS deliberately: sibling frameworks, different centers of gravity.

Names were ratified 2026-07-08: EIOS / Keel / Weave / Entity Keel / Keel Managed / Keel Self-Hosted.

## Canonical source and document policy

- **This repository is the canonical source of the EIOS specification** (decided 2026-07-09). All edits happen here; every other copy or render is derived.
- The specification is versioned as a working master. The current version is **v1.2** (2026-07-10, adding agent communication and authority patterns after the origin-discussion incorporation of v1.1; v1.0 was generated 2026-07-08 from the EIOS Framework working draft with inherited sections incorporated at fork).
- Derived renders (HTML, PDF, website summaries) may exist but never diverge intentionally; if they disagree with this repository, this repository wins.

## Licensing

**© 2026 Valto Loikkanen.** Entity Core, EIOS, Keel, and Weave — the frameworks, specifications, and documentation — are created by Valto Loikkanen and published under open licenses. Attribution under CC BY 4.0 credits Valto Loikkanen / Entity Core.

Two licenses, split by artifact type, chosen to match the recognition-of-source intent:

| Artifact | License |
| --- | --- |
| Specification and documentation (this repository and the EIOS/Weave framework texts) | [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) |
| Reference code, schemas, and tooling (Keel implementations and related software, published separately) | [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) |

CC BY 4.0 allows sharing and adapting for any purpose, including commercially, with attribution. Apache-2.0 adds an explicit patent grant for the code side.

**Attribution statement** (for reuse):

> EIOS originated as a sibling framework to PIOS (Personal Information Operating System, github.com/peecos), created by Valto Loikkanen. EIOS inherits architectural principles and terminology from PIOS 2.0 with permission and attribution. The frameworks evolve independently; no compatibility between them is implied or maintained.

## Project structure

| Where | What |
| --- | --- |
| [entitycore.org](https://entitycore.org) | Initiative website: overview pages for EIOS, Keel, Weave, principles, and the documentation index |
| [github.com/entity-core/eios](https://github.com/entity-core/eios) | This repository — the canonical EIOS specification |
| [github.com/entity-core](https://github.com/entity-core) | The GitHub organization: all Entity Core repositories |
| [github.com/entity-core/brand](https://github.com/entity-core/brand) | Visual design guide: logo, typography, colors, component conventions |
| [github.com/entity-core/media](https://github.com/entity-core/media) | Overview media: video, audio, and visual briefs |
| [github.com/entity-core/keel](https://github.com/entity-core/keel) | Keel — the reference implementation (currently: reference architecture seed) |
| valto@valtoai.com | Contact for pilots, contributors, reviewers, and media |

## Status and roadmap

EIOS is early and developed openly. Current state and planned documentation:

| Item | Status |
| --- | --- |
| EIOS 1.0 master documentation | **Published** (this repository) |
| Governing principles | Published (in the spec; summarized on the website) |
| Minimum viable EIOS | **Published** ([docs/minimum-viable-eios.md](docs/minimum-viable-eios.md)) |
| Weave — standalone context blueprint | Planned (spec §21 is the seed) |
| Portability and export | Planned (spec §35 is the seed) |
| Recognized entity views | Planned (spec §22 is the seed) |
| Entity Glossary | Planned (spec §19 defines the model) |
| Keel reference architecture | **Seed draft published** ([entity-core/keel](https://github.com/entity-core/keel)) |
| Keel implementations (managed / self-hosted) | Not started — follows the reference architecture |

## Getting involved

The work is open to collaborators interested in entity memory, AI-native organizations, governance, financial context, agreements, customer signal loops, and agent-ready information architecture. Reach out at **valto@valtoai.com**, or open an issue in this repository.
