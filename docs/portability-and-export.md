# Portability and Export

`Status: v1.0 (2026-07-10)` `Expands: spec §35` `License: CC BY 4.0`

A complete Entity Keel must be exportable, recoverable, and runnable outside whatever infrastructure currently hosts it. This document expands [§35 of the EIOS master documentation](https://github.com/entity-core/eios/blob/main/spec/eios-1.0-master-documentation.md); the specification wins on any divergence.

## 1. Portability is a survival property

For an entity, portability is not a data-rights checkbox — it is the continuity mechanism for events entities actually face (spec §35.3):

- **Ownership change.** In an acquisition or succession, the export bundle *is* the institutional memory being transferred. Due diligence becomes "inspect the bundle," not "interview the departing founders."
- **Provider change.** Moving between Keel Managed and Keel Self-Hosted — or between clouds — moves the bundle, not a migration project.
- **Wind-down.** Obligations, records, and IP remain governed and retrievable through and after dissolution.
- **Audit and due diligence.** Scoped bundles give governed, evidence-linked views without exposing the full Entity Core.

> **The export is not a folder of files.** It is a *reconstructable entity information core*: data plus the definitions and instructions needed to stand it back up.

## 2. What a full export contains

Per spec §35.1: originals, canonical events, knowledge objects, the entity glossary, system definitions and governance rules, agent definitions and permissions, connector configuration (secrets excluded), derived data where useful, rebuild instructions, and deployment configuration.

Two items are commonly forgotten and are non-negotiable:

- **The glossary.** Ten years of records are unreadable without the vocabulary that names them.
- **Rebuild instructions.** A bundle that requires the original operators to interpret it fails the takeover test.

## 3. The three artifacts

| Artifact | Role | Test |
| --- | --- | --- |
| **Keel Template** | The parameterized infrastructure shape of an *empty* Keel: zones, keys, policies, roles, indexes, guardrails. Secret-free by design. | A new empty instance can be provisioned from it by someone who has never seen the entity. |
| **Keel Export Bundle** | The entity's data payload — full (migration, rebuild, takeover) or scoped (audits, due diligence, partner projections). | Template + full bundle = the same entity, elsewhere. |
| **Provisioning Manifest** | Binds template version, entity, account, region, security posture, and optional bundle hydration into one rebuildable instance. | The manifest alone answers "what exactly is running, and how would we recreate it?" |

Credentials never travel in any of the three; the receiving side supplies them at provisioning (spec §35.2).

## 4. Scoped bundles

Not every export is a takeover. Scoped bundles apply the same mechanics to narrower purposes, and inherit the boundary rules of what they contain:

- **Audit scope** — events, decisions, approvals, and their sources for a period; guarded content included per the auditor's authority.
- **Due-diligence scope** — agreements, financials, IP, decision history; customer identities generalized where the process stage demands it.
- **Partner projection** — the shared-project view as a bundle rather than a live feed (spec §33.3: collaboration through governed projections, never merged storage).

A scoped bundle is itself a governed act: producing one is event-logged, its scope recorded, and its contents traceable.

## 5. Backup, versioning, recovery

- Originals and events: versioned, tested backup — they are irreplaceable.
- Knowledge objects: version history (they change; their trail matters).
- Derived data: may be excluded wherever rebuild instructions exist.
- System definitions: versioned like code, because they are.

> **A backup that has never been restored is a hypothesis, not a continuity plan** (spec §35.4). Rehearse recovery: provision from template, hydrate from bundle, verify the result answers real questions. Do this before the day it matters, on a schedule, and log the rehearsal as an event.

## 6. Adoption checklist

- [ ] A full export can be produced today, on demand, without vendor assistance
- [ ] The export includes glossary, system definitions, and rebuild instructions
- [ ] No secrets in templates or bundles; provisioning-time credential supply works
- [ ] A restore rehearsal has actually been performed (and logged)
- [ ] Scoped bundle types defined for audit and due-diligence needs
- [ ] Export capability is contractual, not goodwill, in any managed arrangement

---

© 2026 Valto Loikkanen. Licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) with attribution to Valto Loikkanen / Entity Core.
