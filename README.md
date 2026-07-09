# EIOS — Entity Information Operating System

**EIOS** is an open framework for entity-centered information operating systems. It defines how an entity — a company, cooperative, association, foundation, public body, or other structured organization — can capture, preserve, organize, govern, retrieve, and use its information over time, so it can keep creating value for its stakeholders beyond dependence on any single person, tool, or AI platform.

EIOS is part of the [Entity Core](https://entitycore.org) open initiative.

## The specification

The complete framework is in one document:

**[EIOS 1.0, Keel, and Weave — Master Documentation](spec/eios-1.0-master-documentation.md)** — 39 sections covering definitions, information zones, the event model, entity circles and access layers, governance, self-improving loops, portability, and the naming/terminology mapping.

## The stack

| Layer | Name | Role |
| --- | --- | --- |
| Public initiative | **Entity Core** | The open initiative and website: [entitycore.org](https://entitycore.org) |
| Open framework | **EIOS** | Entity Information Operating System — the architecture, concepts, rules, and portability requirements (this repository) |
| Implementation | **Keel** | The reference implementation: a durable information spine running the entity information core |
| Context blueprint | **Weave** | The organizing canon for how entity information is named, classified, related, and made understandable |
| Entity instance | **Entity Keel** | One organization's own running instance — its private source of truth |
| Deployment profiles | **Keel Managed / Keel Self-Hosted** | Managed service or portable self-hosted distribution |

## Core ideas

EIOS separates three things that many enterprise products collapse together:

- **What happened** — canonical events and immutable originals
- **What it means** — knowledge objects, entity context, glossary terms, interpretations
- **How it is used** — retrieval APIs, agents, applications, dashboards, entity views, governance surfaces

An EIOS-compliant core preserves originals, records events append-only, maintains living knowledge, treats derived views as rebuildable projections, and keeps system rules — agents, permissions, decision rights — as first-class information. The complete entity information core must be exportable, recoverable, and runnable outside the current provider or tool environment.

## Status

Working master v1.0 (2026-07-08). Names ratified: EIOS / Keel / Weave / Entity Keel / Keel Managed / Keel Self-Hosted. The framework is early and being drafted openly — see [entitycore.org](https://entitycore.org) for the initiative.

## Origin and attribution

EIOS originated as a sibling framework to **PIOS** (Personal Information Operating System, [github.com/peecos](https://github.com/peecos)), created by Valto Loikkanen. EIOS inherits architectural principles and terminology from PIOS 2.0 with permission and attribution. The frameworks evolve independently; no compatibility between them is implied or maintained. Inherited terms and their EIOS-specific divergences are documented in the master documentation's Naming and Terminology Mapping section.

## License

- **Specification and documentation** (this repository): [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) — share and adapt for any purpose, including commercially, with attribution.
- **Reference code, schemas, and tooling** (Keel implementations, published separately): Apache License 2.0.
