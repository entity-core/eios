# Weave — The Entity Context Blueprint

`Status: v1.0 (2026-07-10)` `Expands: spec §21` `License: CC BY 4.0`

Weave is the organizing logic of entity information: how everything an entity captures is named, classified, grouped, related, titled, summarized, and made understandable — to its people and its agents. This document expands [§21 of the EIOS master documentation](https://github.com/entity-core/eios/blob/main/spec/eios-1.0-master-documentation.md); the specification wins on any divergence.

Weave is the EIOS counterpart of PIOS's **Cotton**: where Cotton organizes the personal fiber of one life, Weave structures entity threads — people, agents, agreements, decisions, customers, finances, obligations — into one coherent fabric.

## 1. What Weave is, and is not

Weave is **not** a database schema, a folder tree, or an application taxonomy. Those are implementations. Weave is the conceptual canon those implementations must express — the answer an agent needs *before* choosing any storage format:

- What kind of information is this?
- What is it about — the entity itself, its served world, its operations, its viability, or its memory?
- Which stakeholders, projects, agreements, products, decisions, or time frames does it relate to?
- What should it be called, how should it be summarized, and which terms describe it?
- Which external vocabulary should it map to, if any?

> **Meaning before format** (spec Principle 23): agents first understand what an item *is* and where it fits; only then do they choose event types, metadata, storage, or processing routes.

## 2. The five core areas

Every item relates to one or more of five organizing areas. They are lenses over one connected core — never silos to copy items into.

| Area | Asks | Typical content |
| --- | --- | --- |
| **The Entity** | Who are we? | Identity, purpose, mission, vision, values, strategy, roadmap, ownership, governance, people, capabilities, products, assets |
| **The Served World** | Whom do we serve, among whom do we exist? | Customers, users, buyers, segments, JTBD, value propositions, competitors and alternatives, positioning, channels, business model, research, customer evidence, regulators, communities |
| **The Entity Operating System** | How do we work? | Processes, meetings, tools, agents, permissions, decisions, approvals, routines, metrics |
| **Entity Viability** | Can we continue? | Financials, value creation and capture, costs, reserves, risks, stakeholder support, transition state |
| **Entity Memory** | What do we hold? | Originals, events, knowledge, derived views, system rules |

A single customer email about a contractual issue touches the Served World (the customer), the Entity OS (the support process), Viability (the revenue at risk), and Memory (the preserved original + event). Weave classification records those relationships; it does not pick one winner.

## 3. Stability layers

Storage, review cadence, and agent confidence differ by how fast information changes (spec §16.2):

- **Stable** — founding facts, legal identity, purpose. Strong provenance; changes only through explicit versioned correction.
- **Slowly changing** — strategy, capability map, positioning, org structure. Living profiles with last-reviewed dates and source-linked updates.
- **Dynamic** — tasks, meetings, signals, actuals, tickets. Events, records, and derived summaries.

Misclassifying stability is a common failure: treating strategy as dynamic churns it into noise; treating metrics as stable fossilizes them.

## 4. Classification in practice

The Weave classification template (spec §21.4) is guidance, not a rigid schema. Worked examples of the *thinking*, compressed:

**A signed customer contract (PDF via email):**
area `entity_viability` + `served_world` · stability `stable` · disposition `canonical` · original preserved raw · event `contract_signed` · knowledge projection into the agreement register · sensitivity `guarded` · glossary link to the customer's canonical name · standards mapping to the agreement-type vocabulary.

**A support thread revealing a recurring confusion:**
area `served_world` + `entity_operating_system` · stability `dynamic` · original: the thread · event `customer_feedback_received` · knowledge: attach evidence to the existing signal theme (duplicate prevention — new evidence joins existing work) · routes into the support→product loop.

**A voice memo from the operational owner about strategy direction:**
area `entity` · stability `slowly changing` *candidate* · original preserved · event `message_received` · knowledge: proposal to update the strategy profile — **not** a direct edit, because strategy changes through governance, not through capture.

**An unclassifiable item:** preserve the original, attach best-effort metadata, state the uncertainty, and ask whether the missing concept should become a glossary term, taxonomy value, or area extension (spec §21.4 agent rule). Capture first, organize later — required metadata stays rare.

## 5. Naming, titling, and summarizing

Conventions that keep ten years of records legible:

- **Titles state the thing, not the container.** "Customer X service agreement 2026 renewal" — not "Document scan (3).pdf".
- **Summaries answer "so what."** One or two sentences: what this is, why it matters to the entity, what (if anything) it obligates.
- **Canonical names come from the glossary.** One customer, one name; aliases recorded, not proliferated.
- **Dates are absolute** (2026-07-10, not "last Friday"); actors named by role and record, not only by first name.
- **Sensitivity is part of naming discipline:** titles and summaries of guarded items must themselves be safe to appear in lists and search results.

## 6. DNA, Performance Context, and Settings

Weave keeps three inputs distinct (spec §21.5): **Entity DNA** (what guides interpretation — changes rarely, through governance), **Entity Performance Context** (what success currently means — OKRs, KPIs, targets; changes per planning cycle), and **System Settings** (what the system may do — changes operationally). An agent interpreting a signal needs all three, as separate inputs. Mixing them produces strategy documents polluted with quarterly targets and configuration files that quietly redefine the mission.

## 7. Standards as mappings, not masters

Weave uses established vocabularies — accounting standards, legal agreement categories, project/product terminology, CX vocabularies, industry models — as **mappings and references**. The entity's own language, jurisdiction, and operating reality are preserved; the mapping is recorded alongside, so a financial item can carry both the entity's internal category and its IFRS mapping without either overwriting the other. Historical internal schemas are treated the same way: useful as migration aids, never as the primary organizing logic.

## 8. Domain blueprints

Weave grows through **domain blueprints** (spec §21.6): modular definitions of object types, attributes, relationships, lifecycle states, and documentation projections for one domain — governance, actors, meetings, products, customers, markets, processes. The core areas stay stable while domains deepen independently.

A domain blueprint answers, for its domain: which objects exist, which attributes matter, how objects link to zones/events/glossary, which lifecycle states apply, and which views project from them. The spec's product-knowledge and recognized-views models are the first two worked instances; further blueprints are published as separate documents as they mature.

## 9. Weave for agents — the decision rules

1. Understand meaning before choosing format (Principle 23).
2. Classify by relationships, not by single category; preserve every relevant area link.
3. Use glossary terms; propose candidates instead of inventing synonyms.
4. Respect stability layers — updates to stable/slowly-changing content are proposals unless a standing rule applies.
5. State uncertainty rather than hiding it; low-confidence classification with preserved original beats confident misfiling.
6. Record the reason for each classification decision — the classification trail is itself entity memory.

---

© 2026 Valto Loikkanen. Licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) with attribution to Valto Loikkanen / Entity Core. Sibling concept: PIOS Cotton (github.com/peecos) — inherited pattern, independently evolved.
