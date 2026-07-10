# Minimum Viable EIOS

`Status: v1.0 (2026-07-10)` `Expands: spec §36` `License: CC BY 4.0`

The smallest useful entity memory an organization can adopt — and how to adopt it. This guide expands [§36 of the EIOS master documentation](https://github.com/entity-core/eios/blob/main/spec/eios-1.0-master-documentation.md); the specification wins on any divergence.

## Who this is for

An organization — company, association, cooperative, public body, or initiative — that wants to stop losing its operating memory to scattered tools, departed people, and disposable AI conversations, without committing to a large system project. A minimum viable EIOS (MVE) can be run by a small team; nothing in it requires a platform decision that cannot be reversed, because everything in it is exportable by design.

## What "minimum viable" means here

An MVE is not a small pilot of software. It is the **smallest set of information practices and structures that makes the entity's memory durable and usable**:

- New information lands in one place and is preserved as received.
- What happened becomes an event trail.
- What was decided is recorded with rationale.
- Who the entity serves, why it exists, and what it is pursuing are written down and used.
- Humans and agents can retrieve all of the above.

If the organization stopped there — no agents, no automation — it would already have durable institutional memory. Everything else compounds from it.

## The ten components

Each component below names its purpose, its minimum form, and what it deliberately defers. The minimum forms assume nothing more than files, folders, and discipline; tooling can be layered on later.

### 1. Entity foundation

**Purpose:** the entity's DNA as usable information — the decision lens for everything else.
**Minimum:** one document set covering purpose, mission, vision, values, strategy, and roadmap; a stakeholder map; customer segments and value propositions; the basic governance roles (who decides what, at what threshold, and who is the operational owner).
**Defer:** formal recognized views (business plan, SWOT) — they become projections later.

### 2. Information core

**Purpose:** the five zones, however small.
**Minimum:** an *originals* area (files kept exactly as received, never edited), an *events* log (even a dated append-only journal), a *knowledge* area (living notes that cite their sources), a *derived* area (summaries and views, understood as rebuildable), and a *system* area (the rules, roles, and agent definitions themselves).
**Defer:** databases, indexes, embeddings — until retrieval pain justifies them.

### 3. Communication capture

**Purpose:** meetings and threads are where entity truth appears first.
**Minimum:** meeting summaries with decisions and action items extracted; a way to forward email threads and documents into the inbox; approvals recorded explicitly (a notification is not an approval).
**Defer:** full transcription pipelines, chat connectors.

### 4. Actor model

**Purpose:** who acts for the entity — humans and agents alike.
**Minimum:** a record per actor (person, team, agent) with role, responsibilities, decision rights, and access rules; channel identities (email, phone) for key stakeholders so communication can be identity-resolved; the unknown-party posture defined.
**Defer:** fine-grained access systems; start with clear rules and few people.

### 5. Value and market context

**Purpose:** the served world as operating memory, not tribal knowledge.
**Minimum:** customer/user/buyer distinctions where they differ; jobs to be done for the main segments; market signals captured with source and date; customer evidence (quotes, objections, wins, churn reasons) linked to segments.
**Defer:** the full market-context area model; add areas as evidence accumulates.

### 6. Financial context

**Purpose:** viability visible, not felt.
**Minimum:** revenue model and cost structure written down; budget vs actuals; cash position and runway; reserves; the financial guarded-action list adopted (who may approve payments, change payment details, commit budget).
**Defer:** management-finance depth (unit economics, scenario plans) until the basics are routine.

### 7. Agreements and obligations

**Purpose:** what the entity has promised, owed, and been promised.
**Minimum:** an agreement register (type, parties, dates, status, where the signed original lives); extracted obligations and renewal dates; contract-sensitive handling flagged.
**Defer:** clause-level extraction and legal-review workflows.

### 8. Governance basics

**Purpose:** decisions distinguishable from discussion; sensitive material handled deliberately.
**Minimum:** decision records with rationale and alternatives; the decision-qualification criteria adopted (what counts as decided); sensitivity levels (normal / sensitive / guarded) applied; need-to-know sharing as the default posture.
**Defer:** approval workflow tooling; earned-autonomy rules for agents.

### 9. Self-improving loops

**Purpose:** memory that acts back on the entity.
**Minimum:** pick two loops and close them fully rather than five loosely — typically the *customer signal loop* (signal → owned action → outcome → recurrence check) and the *meeting-to-decision loop* (discussion → decision record → follow-through). Completion is not resolution: a loop closes when the originating signal declines.
**Defer:** the remaining loop families; add one per cycle.

### 10. Continuity views

**Purpose:** the entity can see itself.
**Minimum:** an entity history (curated, human-readable); a decision log; project status; a risk register; a financial viability view; a knowledge-gaps note (what the entity knows it doesn't know).
**Defer:** dashboards and automated projections.

## The adoption path

Per spec §36, an MVE is adopted in stages, not switched on:

```
pre-load context → informed first engagement → scope ratified with stakeholders → minimal viable instance → expand by loop
```

1. **Pre-load context.** Before involving stakeholders, gather what already exists — strategy documents, stakeholder lists, financials, agreements, notes — into the inbox and the foundation documents. The system should know the entity before the entity meets the system.
2. **Informed first engagement.** The first stakeholder-facing session (a scoping workshop is the natural form) happens with the pre-loaded foundation in the room: stakeholders are recognized, current strategy is citable, and gaps become visible live.
3. **Scope ratified with stakeholders.** Decide together — and record as decisions — what the MVE will and will not do first. This is also the first exercise of the decision-record practice.
4. **Minimal viable instance.** Stand up the ten components at their minimum forms, scoped to the ratified ambition.
5. **Expand by loop.** Growth follows the self-improving loops: each cycle adds sources, views, structure, or agent autonomy only where the previous cycle earned it. Resist expanding all ten components simultaneously.

## Common failure modes

- **Tool-first adoption.** Choosing platforms before practicing the information behaviors. The MVE is deliberately tool-agnostic; files and discipline are enough to start.
- **Capture without loops.** Collecting everything and acting on nothing — insight-heavy, action-light. Two closed loops beat ten open channels.
- **Decision inflation.** Recording every discussion as if it decided something. Apply the qualification criteria; protect the meaning of "decided."
- **Skipping the foundation.** Starting with capture while purpose, strategy, and decision rights stay undocumented — producing a well-organized archive with no decision lens.
- **Agent-first automation.** Granting agents autonomy before the governance basics exist. Agents recommend; authorized humans decide — from day one.

## Readiness checklist

- [ ] Purpose, mission, strategy, and roadmap written and owned
- [ ] Stakeholder map with the operational owner identified
- [ ] Originals preserved as received; events journaled append-only
- [ ] Decision records with rationale in use; qualification criteria adopted
- [ ] Meeting summaries flowing into the core
- [ ] Actor records with roles, decision rights, and channel identities
- [ ] Customer segments, JTBD, and signals being captured with sources
- [ ] Budget/actuals, runway, and financial guarded actions in place
- [ ] Agreement register with obligations and renewal dates
- [ ] Sensitivity levels and need-to-know sharing applied
- [ ] Two loops running and closing
- [ ] History, decision log, and risk register readable by a newcomer
- [ ] Everything exportable — a departure of any tool or person loses nothing

---

© 2026 Valto Loikkanen. Licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) with attribution to Valto Loikkanen / Entity Core. For the implementation counterpart, see the [Keel reference architecture](https://github.com/entity-core/keel/blob/main/docs/reference-architecture.md) and its Minimum Viable Keel checklist.
